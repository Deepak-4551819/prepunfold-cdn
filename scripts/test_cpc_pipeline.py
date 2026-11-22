# -*- coding: utf-8 -*-
import pymupdf
import re
import json
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

PDF_PATH = r'C:\Users\yedde\Downloads\Judicial\CPC Youth PYQ.pdf'
CACHE_FILE = r'D:\Android Project\prepunfold-cdn\scripts\judiciary_translation_cache.json'

trans_cache = {}
try:
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        trans_cache = json.load(f)
except:
    trans_cache = {}

def is_hindi(text):
    return bool(re.search(r'[\u0900-\u097F]', text))

def translate_batch(texts, sl='en', tl='hi', max_workers=10):
    to_fetch = [t for t in set(texts) if t and t.strip() and t not in trans_cache]
    if tl == 'hi':
        to_fetch = [t for t in to_fetch if not is_hindi(t)]

    def fetch_one(text):
        clean_t = text.strip()
        if not clean_t:
            return text, text
        url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={sl}&tl={tl}&q={urllib.parse.quote(clean_t)}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        for _ in range(3):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=8) as resp:
                    res = json.loads(resp.read().decode('utf-8'))
                    if isinstance(res, list) and len(res) > 0 and isinstance(res[0], str):
                        return text, res[0]
            except:
                pass
        return text, text

    if to_fetch:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for orig, trans in executor.map(fetch_one, to_fetch):
                if trans and trans != orig:
                    trans_cache[orig] = trans
        try:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(trans_cache, f, ensure_ascii=False)
        except:
            pass

    return [trans_cache.get(t, t) for t in texts]

def is_akruti_text(text):
    if not text:
        return False
    akruti_tokens = [
        'keâ', 'efm', 'efJ', 'efv', 'efh', 'efk', 'efu', 'efM', 'efl', 'efL', 'efo', 'efO',
        'efY', 'efy', 'efI', 'efÛ', 'efš', 'ef[', 'efC', 'efK', 'efP', 'ef<', 'efj',
        '›eâ', 'Heâ', 'òeâ', 'DeeB', 'Deew', 'Dees',
        'kesâ', 'ceW', 'ueeiet', 'efoveebkeâ', 'oerJeeveer', 'mebefnlee', 'Øeef›eâÙee',
        'vÙeeÙeeueÙe', 'ef[›eâer', 'Jeeo', 'efveCe&Ùe', 'DeeosMe', 'heefjYeeef<ele',
        'ØeejefcYekeâ', 'Debeflece', 'DeefOekeâej'
    ]
    for tok in akruti_tokens:
        if tok in text:
            return True
    akruti_chars = set('Ø›«¥šþªÛÚõüý§')
    if any(c in akruti_chars for c in text):
        return True
    return False

EXAM_PAT = r'\n?\s*((?:(?:U\.?P\.?|M\.?P\.?|B\.?P\.?|R\.?J\.?S|HJS|PCS|CJ|JS|JLO|Bihar|Chhatt|Uttarakhand|Jharkhand|Rajasthan|Haryana|Delhi|HP|Civil Judge|Paper|Shift|Part)[^\n]*\b(19\d\d|20\d\d)\b[^\n]*)+)\s*$'

def parse_topic_questions(doc, p_start, p_end):
    full_lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s == 'efmeefJeue Øeef›eâÙee mebefnlee, 1908' or re.match(r'^\d+$', s):
                continue
            full_lines.append(s)
    full_text = '\n'.join(full_lines)
    all_ans = list(re.finditer(r'(?:^|\n)Ans\.\s*\(([a-eA-E])\)\s*:?', full_text))

    questions = []
    for i, ans_m in enumerate(all_ans):
        prev = all_ans[i-1].end() if i > 0 else 0
        w = full_text[prev:ans_m.start()]

        d_matches = list(re.finditer(r'(?:^|\n|\s)\(d\)\s*', w, re.I))
        if not d_matches: continue
        m_d = d_matches[-1]
        c_matches = list(re.finditer(r'(?:^|\n|\s)\(c\)\s*', w[:m_d.start()], re.I))
        if not c_matches: continue
        m_c = c_matches[-1]
        b_matches = list(re.finditer(r'(?:^|\n|\s)\(b\)\s*', w[:m_c.start()], re.I))
        if not b_matches: continue
        m_b = b_matches[-1]
        a_matches = list(re.finditer(r'(?:^|\n|\s)\(a\)\s*', w[:m_b.start()], re.I))
        if not a_matches: continue
        m_a = a_matches[-1]

        before_a = w[:m_a.start()]
        q_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)(?:\.|\s+)', before_a))
        if q_matches:
            last_q = q_matches[-1]
            q_num = int(last_q.group(1))
            stem_raw = before_a[last_q.end():].strip()
        else:
            q_num = i + 1
            stem_raw = before_a.strip()

        # Clean any leading headers that leaked into stem_raw
        stem_raw = re.sub(r'^(?:1908|\d+|YCT|DeOÙeeÙe\s*–?\s*\d+|[^\n]*\(\s*Oeeje\s*[\d\-]+\))\s*\n?', '', stem_raw).strip()

        opt_a_raw = w[m_a.end():m_b.start()].strip()
        opt_b_raw = w[m_b.end():m_c.start()].strip()
        opt_c_raw = w[m_c.end():m_d.start()].strip()
        opt_d_raw = w[m_d.end():].strip()

        # Strip exam tag from opt_d_raw
        exam_tag = ''
        m_tag = re.search(EXAM_PAT, opt_d_raw, re.I)
        if m_tag:
            exam_tag = re.sub(r'\s+', ' ', m_tag.group(1)).strip()
            opt_d_raw = opt_d_raw[:m_tag.start()].strip()

        # Parse stem into EN
        lines = [l.strip() for l in stem_raw.split('\n') if l.strip()]
        en_lines = []
        for l in lines:
            if '/' in l:
                en_p = l.split('/')[0].strip()
                if en_p and not is_akruti_text(en_p):
                    en_lines.append(en_p)
                break
            elif not is_akruti_text(l):
                en_lines.append(l)
            else:
                break
        q_en = ' '.join(en_lines).strip()
        q_en = re.sub(r'\s+', ' ', q_en)

        opts_en = []
        for opt_raw in [opt_a_raw, opt_b_raw, opt_c_raw, opt_d_raw]:
            if '/' in opt_raw:
                o_en = opt_raw.split('/')[0].strip()
            else:
                o_lines = [l.strip() for l in opt_raw.split('\n') if l.strip()]
                o_en_lines = [l for l in o_lines if not is_akruti_text(l)]
                o_en = ' '.join(o_en_lines).strip() if o_en_lines else opt_raw.strip()
            o_en = re.sub(r'\s+', ' ', o_en)
            opts_en.append(o_en)

        # Fallback for empty options
        for o_idx in range(4):
            if not opts_en[o_idx] or is_akruti_text(opts_en[o_idx]):
                opts_en[o_idx] = f"Option {chr(ord('A') + o_idx)}"

        corr_letter = ans_m.group(1).upper()
        if corr_letter not in 'ABCD':
            corr_letter = 'A'

        m_yr = re.search(r'\b(19\d\d|20\d\d)\b', exam_tag)
        exam_year = int(m_yr.group(1)) if m_yr else 2024

        questions.append({
            "idx": i + 1,
            "orig_num": q_num,
            "stem_raw": stem_raw,
            "q_en": q_en,
            "opts_en": opts_en,
            "correct_option": corr_letter,
            "exam_tag": exam_tag if exam_tag else "State Judiciary & PCS (J) PYQ",
            "exam_year": exam_year
        })

    return questions

if __name__ == '__main__':
    doc = pymupdf.open(PDF_PATH)
    qs = parse_topic_questions(doc, 4, 15)
    print(f"Total parsed: {len(qs)}")
    for q in qs:
        if q['orig_num'] in [1, 14, 29]:
            print(f"=== Q{q['orig_num']} (Ans: {q['correct_option']}) ===")
            print("Tag:", q['exam_tag'])
            print("Q_EN:", q['q_en'])
            print("OPTS_EN:", q['opts_en'])
