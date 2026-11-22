import os
import re
import json
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
import pymupdf

PDF_PATH = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
CACHE_FILE = "scripts/judiciary_translation_cache.json"
OUT_DIR = "tests/judiciary_pyq/minor_acts"
os.makedirs(OUT_DIR, exist_ok=True)

trans_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            trans_cache = json.load(f)
    except:
        trans_cache = {}

def is_hindi(text):
    return any(0x0900 <= ord(c) <= 0x097F for c in text)

def translate_batch(texts, max_workers=10):
    to_fetch = [t for t in set(texts) if t and t.strip() and t not in trans_cache and not is_hindi(t)]

    def fetch_one(text):
        clean_text = text.strip()
        if not clean_text:
            return text, text
        url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=hi&q={urllib.parse.quote(clean_text)}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
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
        print(f"Translating {len(to_fetch)} new phrases...")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for orig, trans in executor.map(fetch_one, to_fetch):
                if is_hindi(trans):
                    trans_cache[orig] = trans
        try:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(trans_cache, f, ensure_ascii=False)
        except:
            pass

    return [trans_cache.get(t, t) for t in texts]

def cluster_spans_into_lines(spans):
    if not spans: return []
    sorted_spans = sorted(spans, key=lambda s: s['bbox'][1])
    lines = []
    current_line = []
    for s in sorted_spans:
        if not current_line:
            current_line.append(s)
        else:
            avg_y0 = sum(x['bbox'][1] for x in current_line) / len(current_line)
            if abs(s['bbox'][1] - avg_y0) <= 4:
                current_line.append(s)
            else:
                current_line.sort(key=lambda x: x['bbox'][0])
                line_txt = "".join(x['text'] for x in current_line).strip()
                if line_txt:
                    lines.append(line_txt)
                current_line = [s]
    if current_line:
        current_line.sort(key=lambda x: x['bbox'][0])
        line_txt = "".join(x['text'] for x in current_line).strip()
        if line_txt:
            lines.append(line_txt)
    return lines

def extract_clean_page_en(page):
    d = page.get_text("dict")
    col1_spans = []
    col2_spans = []

    for b in d["blocks"]:
        if "lines" not in b: continue
        for l in b["lines"]:
            full_line = " ".join(s["text"] for s in l["spans"]).strip()
            if "Gòejceeuee" in full_line or "Answer Key" in full_line or re.match(r'^\d+\.\s*\([a-e]\)', full_line):
                continue
            for s in l["spans"]:
                txt = s["text"]
                if not txt.strip(): continue
                font = s["font"]
                if "Times" in font or "Arial" in font:
                    x0, y0, x1, y1 = s["bbox"]
                    if y0 < 50 or y1 > 730: continue
                    if x0 < 308:
                        col1_spans.append(s)
                    else:
                        col2_spans.append(s)

    lines = cluster_spans_into_lines(col1_spans) + cluster_spans_into_lines(col2_spans)
    return "\n".join(lines)

def find_options_in_clean_en(s):
    OPT_PAT = r'(?:^|\n|\s|/|\d|\))'
    m_a = re.search(r'(?:^|\n|\s|/)\(a\)\s*', s, re.I)
    if not m_a: return None
    m_b = re.search(OPT_PAT + r'\(b\)\s*', s[m_a.end():], re.I)
    if not m_b: return None
    b_start = m_a.end() + m_b.start()
    b_end = m_a.end() + m_b.end()

    m_c = re.search(OPT_PAT + r'\(c\)\s*', s[b_end:], re.I)
    if not m_c: return None
    c_start = b_end + m_c.start()
    c_end = b_end + m_c.end()

    m_d = re.search(OPT_PAT + r'\(d\)\s*', s[c_end:], re.I)
    if not m_d: return None
    d_start = c_end + m_d.start()
    d_end = c_end + m_d.end()

    m_e = re.search(OPT_PAT + r'\(e\)\s*', s[d_end:], re.I)
    if m_e:
        e_start = d_end + m_e.start()
        e_end = d_end + m_e.end()
        return [
            ("a", s[m_a.end():b_start].strip().rstrip("/").strip()),
            ("b", s[b_end:c_start].strip().rstrip("/").strip()),
            ("c", s[c_end:d_start].strip().rstrip("/").strip()),
            ("d", s[d_end:e_start].strip().rstrip("/").strip()),
            ("e", s[e_end:].strip().rstrip("/").strip()),
        ]

    return [
        ("a", s[m_a.end():b_start].strip().rstrip("/").strip()),
        ("b", s[b_end:c_start].strip().rstrip("/").strip()),
        ("c", s[c_end:d_start].strip().rstrip("/").strip()),
        ("d", s[d_end:].strip().rstrip("/").strip()),
    ]

MINOR_ACTS_CONFIG = [
    (1, 'minor_acts_pyq_t01_persons_with_disabilities', 'Rights of Persons with Disabilities Act, 2016', 'दिव्यांगजन अधिकार अधिनियम, 2016', 3, 11),
    (2, 'minor_acts_pyq_t02_maintenance_parents_senior_citizens', 'Maintenance and Welfare of Parents and Senior Citizens Act, 2007', 'माता-पिता और वरिष्ठ नागरिकों का भरण-पोषण एवं कल्याण अधिनियम, 2007', 12, 19),
    (3, 'minor_acts_pyq_t03_dowry_prohibition', 'The Dowry Prohibition Act, 1961', 'दहेज प्रतिषेध अधिनियम, 1961', 20, 27),
    (4, 'minor_acts_pyq_t04_domestic_violence', 'Protection of Women from Domestic Violence Act, 2005', 'घरेलू हिंसा से महिलाओं का संरक्षण अधिनियम, 2005', 28, 42),
    (5, 'minor_acts_pyq_t05_sexual_harassment_workplace', 'Sexual Harassment of Women at Workplace Act, 2013', 'महिलाओं का कार्यस्थल पर लैंगिक उत्पीड़न (निवारण, प्रतिषेध और प्रतितोष) अधिनियम, 2013', 43, 52),
    (6, 'minor_acts_pyq_t06_pcpndt_act', 'Pre-Conception and Pre-Natal Diagnostic Techniques (PCPNDT) Act, 1994', 'गर्भधारण पूर्व और प्रसव पूर्व निदान तकनीक अधिनियम, 1994', 53, 62),
    (7, 'minor_acts_pyq_t07_medical_termination_of_pregnancy', 'Medical Termination of Pregnancy Act, 1971', 'गर्भ का चिकित्सीय समापन अधिनियम, 1971', 63, 64),
    (8, 'minor_acts_pyq_t08_indecent_representation_of_women', 'Indecent Representation of Women (Prohibition) Act, 1986', 'स्त्री अशिष्ट रूपण (प्रतिषेध) अधिनियम, 1986', 65, 67),
    (9, 'minor_acts_pyq_t09_pocso_act', 'Protection of Children from Sexual Offences (POCSO) Act, 2012', 'लैंगिक अपराधों से बालकों का संरक्षण (पॉक्सो) अधिनियम, 2012', 68, 80),
]

def build_minor_act(doc, t_num, test_id, title_en, title_hi, p_start, p_end):
    # 1. Collect answer key
    ans_dict = {}
    for p in range(p_start - 1, p_end):
        page = doc[p]
        for b in page.get_text("blocks"):
            if b[6] != 0:
                continue
            for m in re.finditer(r'(\d+)\.\s*\(([a-e])\)', b[4]):
                ans_dict[int(m.group(1))] = m.group(2).lower()

    # 2. Extract clean English text using span clustering
    act_text = ""
    for p in range(p_start - 1, p_end):
        act_text += "\n" + extract_clean_page_en(doc[p])

    act_text = re.sub(r'\n(\d+)\.\s*\n', r'\n\1. ', act_text)
    q_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\.\s*', act_text))

    valid_qs = []
    for i, m in enumerate(q_matches):
        q_num = int(m.group(1))
        if q_num not in ans_dict:
            continue
        start_idx = m.end()
        end_idx = q_matches[i+1].start() if i+1 < len(q_matches) else len(act_text)
        block = act_text[start_idx:end_idx].strip()
        valid_qs.append((q_num, block))

    ans_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}

    raw_items = []
    all_texts_to_trans = []

    for q_num, block in valid_qs:
        ans_letter = ans_dict[q_num]
        correct_idx = ans_map.get(ans_letter, 0)

        opts_parsed = find_options_in_clean_en(block)
        if opts_parsed:
            m_a = re.search(r'(?:^|\n|\s|/)\(a\)\s*', block, re.I)
            stem_raw = block[:m_a.start()].strip() if m_a else block
            stem_en = " ".join(stem_raw.split()).rstrip("/").strip()
            opts_en = [" ".join(opt_txt.split()).rstrip("/").strip() for _, opt_txt in opts_parsed]
        else:
            stem_en = " ".join(block.split()).rstrip("/").strip()
            opts_en = ["A", "B", "C", "D"]

        all_texts_to_trans.append(stem_en)
        all_texts_to_trans.extend(opts_en)

        raw_items.append({
            'q_num': q_num,
            'stem_en': stem_en,
            'opts_en': opts_en,
            'correct_idx': correct_idx,
            'ans_letter': ans_letter
        })

    # Batch translate
    translate_batch(all_texts_to_trans)

    questions = []
    for item in raw_items:
        stem_en = item['stem_en']
        opts_en = item['opts_en']
        stem_hi = trans_cache.get(stem_en, stem_en)
        opts_hi = [trans_cache.get(o, o) for o in opts_en]
        correct_idx = item['correct_idx']
        ans_char = item['ans_letter'].upper()

        explanation_en = f"Official Answer: Option ({ans_char}). Enacted under the relevant provisions of {title_en}."
        explanation_hi = f"आधिकारिक उत्तर: विकल्प ({ans_char})। {title_hi} के संबंधित प्रावधानों के अंतर्गत अधिनियमित।"

        q_obj = {
            "id": f"{test_id}_q{item['q_num']:03d}",
            "questionNumber": item['q_num'],
            "questionTextEn": stem_en,
            "questionTextHi": stem_hi,
            "optionsEn": opts_en,
            "optionsHi": opts_hi,
            "correctOption": correct_idx,
            "explanationEn": explanation_en,
            "explanationHi": explanation_hi,
            "examTag": "UPPCS (J) Minor Acts Special",
            # Legacy compatibility
            "question_en": stem_en,
            "question_hi": stem_hi,
            "options_en": opts_en,
            "options_hi": opts_hi,
            "correct_index": correct_idx,
            "explanation_en": explanation_en,
            "explanation_hi": explanation_hi
        }
        questions.append(q_obj)

    test_json = {
        "testId": test_id,
        "titleEn": f"UP Judiciary Minor Acts: {title_en}",
        "titleHi": f"यूपी न्यायिक सेवा लघु अधिनियम: {title_hi}",
        "subject": "Minor Acts",
        "subjectHi": "लघु अधिनियम (Minor Acts)",
        "topicId": f"part14_minor_acts_t{t_num:02d}",
        "totalQuestions": len(questions),
        "durationMinutes": max(15, int(len(questions) * 0.9)),
        "marksPerQuestion": 1,
        "negativeMarks": 0.33,
        "source": "Youth Competition Times UP Judicial Service Minor Acts (9 in 1)",
        "questions": questions
    }

    out_file = os.path.join(OUT_DIR, f"{test_id}.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(test_json, f, ensure_ascii=False, indent=2)

    print(f"Generated {out_file} with {len(questions)} questions")
    return len(questions)

def main():
    doc = pymupdf.open(PDF_PATH)
    total_q = 0
    print(f"Starting Minor Acts Build: {len(MINOR_ACTS_CONFIG)} topics...")
    for item in MINOR_ACTS_CONFIG:
        t_num, test_id, title_en, title_hi, p_start, p_end = item
        print(f"Building {test_id} (pages {p_start}-{p_end})...")
        count = build_minor_act(doc, t_num, test_id, title_en, title_hi, p_start, p_end)
        total_q += count
    print("=" * 75)
    print(f"Minor Acts Build Complete: {len(MINOR_ACTS_CONFIG)} Tests Built | Total Questions: {total_q}")

if __name__ == "__main__":
    main()
