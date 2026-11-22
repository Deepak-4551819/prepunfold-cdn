# -*- coding: utf-8 -*-
import pymupdf
import re
import json
import os
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

PDF_PATH = r'C:\Users\yedde\Downloads\Judicial\CPC Youth PYQ.pdf'
OUTPUT_DIR = r'D:\Android Project\prepunfold-cdn\tests\judiciary_pyq\cpc'
CACHE_FILE = r'D:\Android Project\prepunfold-cdn\scripts\judiciary_translation_cache.json'

os.makedirs(OUTPUT_DIR, exist_ok=True)

trans_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            trans_cache = json.load(f)
    except:
        trans_cache = {}

# Preload from other existing caches if available
for prev_cache in [
    r'D:\Android Project\prepunfold-cdn\scripts\history_translation_cache.json',
    r'D:\Android Project\prepunfold-cdn\scripts\translation_cache.json'
]:
    if os.path.exists(prev_cache):
        try:
            with open(prev_cache, 'r', encoding='utf-8') as f:
                p_c = json.load(f)
                for k, v in p_c.items():
                    if k not in trans_cache:
                        trans_cache[k] = v
        except:
            pass

def is_hindi(text):
    if not text:
        return False
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

# Akruti to Unicode mapping
AKRUTI_MAP = {
    'ef›eâ': 'क्रि', 'efõ': 'द्वि', 'efo': 'दि', 'efme': 'सि', 'efJe': 'वि',
    'efve': 'नि', 'efhe': 'पि', 'efkeâ': 'कि', 'efue': 'लि', 'efMe': 'शि',
    'efle': 'ति', 'efie': 'गि', 'efpe': 'जि', 'efn': 'हि', 'efne': 'हि',
    'efYe': 'भि', 'efye': 'बि', 'efLe': 'थि', 'efOe': 'धि', 'efIe': 'घि',
    'efÛe': 'चि', 'efÚ': 'छि', 'efše': 'टि', 'efþe': 'ठि', 'ef[e': 'डि',
    'ef[': 'डि', 'efªe': 'ढि', 'efCe': 'णि', 'efKe': 'खि', 'efPe': 'झि',
    'ef<e': 'षि', 'efj': 'रि', 'efje': 'रि', 'efòe': 'त्ति', 'efkeä': 'क्कि',
    'efmle': 'स्ति', 'efmLe': 'स्थि', 'efmJe': 'स्वि',

    'keâe': 'का', 'Kee': 'खा', 'iee': 'गा', 'Iee': 'घा',
    'Ûee': 'चा', 'Úee': 'छा', 'pee': 'जा', 'Pee': 'झा',
    'šee': 'टा', 'þee': 'ठा', '[ee': 'डा', 'ªee': 'ढा', 'Cee': 'णा',
    'lee': 'ता', 'Lee': 'था', 'oee': 'दा', 'Oee': 'धा', 'vee': 'ना',
    'hee': 'पा', 'Heâe': 'फ़ा', 'Hee': 'फा', 'yee': 'बा', 'Yee': 'भा',
    'cee': 'मा', 'Ùee': 'या', 'jee': 'रा', 'uee': 'ला', 'Jee': 'वा',
    'Mee': 'शा', '<ee': 'षा', 'mee': 'सा', 'nee': 'हा',

    'keâ': 'क', 'Ke': 'ख', 'ie': 'ग', 'Ie': 'घ',
    'Ûe': 'च', 'Ú': 'छ', 'pe': 'ज', 'Pe': 'झ', '¥': 'ञ',
    'še': 'ट', 'þe': 'ठ', '[e': 'ड', '[': 'ड', 'ªe': 'ढ', 'Ce': 'ण',
    'le': 'त', 'Le': 'थ', 'oe': 'द', 'Oe': 'ध', 've': 'न',
    'he': 'प', 'Heâ': 'फ़', 'He': 'फ', 'ye': 'ब', 'Ye': 'भ',
    'ce': 'म', 'Ùe': 'य', 'je': 'र', 'ue': 'ल', 'Je': 'व',
    'Me': 'श', '<e': 'ष', 'me': 'स', 'ne': 'ह',

    'keä': 'क्', 'K': 'ख्', 'i': 'ग्', 'I': 'घ्',
    'Û': 'च्', 'p': 'ज्', 'P': 'झ्',
    'š': 'ट्', 'þ': 'ठ्', 'ª': 'ढ्', 'C': 'ण्',
    'l': 'त्', 'L': 'थ्', 'o': 'द्', 'O': 'ध्', 'v': 'न्',
    'h': 'प्', 'H': 'फ्', 'y': 'ब्', 'Y': 'भ्',
    'c': 'म्', 'Ù': 'य्', 'j': 'र', 'u': 'ल्', 'J': 'व्',
    'M': 'श्', '<': 'ष्', 'm': 'स्', 'n': 'ह्',

    'òeâ': 'क्त', 'òe': 'त्त', 'ò': 'त्त्',
    'Øe': 'प्र', 'Ø': 'प्र', '›eâ': 'क्र', '›': 'क्र',
    'õ': 'द्व', 'ü': 'ह्न', 'ý': 'ह्य',
    '#': 'क्ष', '$': 'त्र',

    'DeeB': 'आँ', 'DeB': 'अं', 'Dees': 'ओ', 'Deew': 'औ', 'Dee': 'आ', 'De': 'अ',
    'Fkeäkeâ': 'इक्क', 'F&': 'ई', 'F': 'इ', 'G': 'उ', 'T': 'ऊ', '_e': 'ऋ', 'Ss': 'ऐ', 'S': 'ए',

    'kesâ': 'के', 'ceW': 'में', 'nw': 'है', 'nQ': 'हैं', 'mes': 'से',
    'keâes': 'को', 'keâeR': 'कीं', 'keâer': 'की',

    'ee': 'ा', 'er': 'ी', 'g': 'ु', 't': 'ू',
    's': 'े', 'w': 'ै', 'es': 'ो', 'ew': 'ौ',
    'b': 'ं', 'B': 'ँ', '~': '।',
    '®': 'रू', '™': 'रु',
    '&': 'र्', '§': '्र',
    '‘': "'", '’': "'", '“': '"', '”': '"',
    '`': "'", '´': "'",
    'eâ': 'क', 'e': 'ा', 'W': 'ं',
}

keys_sorted = sorted(AKRUTI_MAP.keys(), key=lambda x: -len(x))
pattern_akruti = re.compile('|'.join(re.escape(k) for k in keys_sorted))

def akruti_to_unicode(text):
    if not text:
        return ""
    res = pattern_akruti.sub(lambda m: AKRUTI_MAP[m.group(0)], text)
    res = re.sub(r'([क-ह][ािीुूेैोौंँ]*)र्', r'र्\1', res)
    res = res.replace('ाा', 'ा')
    return res.strip()

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

TESTS_CONFIG = [
    (1, "cpc_pyq_t01_preliminary", "Preliminary (Sec 1-8)", "प्रारंभिक (धारा 1-8)", 4, 15),
    (2, "cpc_pyq_t02_jurisdiction_and_res_judicata", "Jurisdiction and Res Judicata (Sec 9-14)", "अधिकारिता एवं पूर्व न्याय (धारा 9-14)", 16, 29),
    (3, "cpc_pyq_t03_place_of_suing_and_institution_of_suits", "Place of Suing and Institution of Suits (Sec 15-26)", "वाद संस्थित करने का स्थान एवं वाद संस्थित किया जाना (धारा 15-26)", 30, 38),
    (4, "cpc_pyq_t04_summons_and_discovery", "Summons and Discovery (Sec 27-32)", "समन एवं प्रकटीकरण (धारा 27-32)", 39, 40),
    (5, "cpc_pyq_t05_judgment_decree_and_costs", "Judgment, Decree and Costs (Sec 33-35B)", "निर्णय, डिक्री एवं खर्चे (धारा 33-35B)", 41, 42),
    (6, "cpc_pyq_t06_execution", "Execution (Sec 36-74)", "डिक्री का निष्पादन (धारा 36-74)", 43, 53),
    (7, "cpc_pyq_t07_incidental_proceedings", "Incidental Proceedings (Sec 75-78)", "आनुषंगिक कार्यवाहियां (धारा 75-78)", 54, 54),
    (8, "cpc_pyq_t08_suits_in_particular_cases", "Suits in Particular Cases (Sec 79-88)", "विशिष्ट मामलों में वाद (धारा 79-88)", 55, 59),
    (9, "cpc_pyq_t09_special_proceedings_adr", "Special Proceedings - ADR (Sec 89-93)", "विशिष्ट कार्यवाहियां - वैकल्पिक विवाद समाधान (धारा 89-93)", 60, 64),
    (10, "cpc_pyq_t10_supplemental_proceedings", "Supplemental Proceedings (Sec 94-95)", "अनुपूरक कार्यवाहियां (धारा 94-95)", 65, 65),
    (11, "cpc_pyq_t11_appeals", "Appeals (Sec 96-112)", "अपील (धारा 96-112)", 66, 71),
    (12, "cpc_pyq_t12_reference_review_and_revision", "Reference, Review and Revision (Sec 113-115)", "निर्देश, पुनर्विलोकन एवं पुनरीक्षण (धारा 113-115)", 72, 75),
    (13, "cpc_pyq_t13_high_court_rules_and_special_provisions", "High Court Rules and Special Provisions (Sec 116-131)", "उच्च न्यायालयों के संबंध में विशेष उपबंध (धारा 116-131)", 76, 76),
    (14, "cpc_pyq_t14_miscellaneous_provisions", "Miscellaneous Provisions (Sec 132-158)", "प्रकीर्ण उपबंध (धारा 132-158)", 76, 82),
    (15, "cpc_pyq_t15_orders_01_to_10_parties_pleadings_and_issues", "First Schedule: Orders 1 to 10 (Parties, Pleadings & Issues)", "प्रथम अनुसूची: आदेश 1 से 10 (पक्षकार, अभिवचन एवं वाद हेतुक)", 83, 114),
    (16, "cpc_pyq_t16_orders_11_to_20_discovery_admissions_and_trial", "First Schedule: Orders 11 to 20 (Discovery, Admissions & Trial)", "प्रथम अनुसूची: आदेश 11 से 20 (प्रकटीकरण, स्वीकृतियां एवं विचारण)", 115, 124),
    (17, "cpc_pyq_t17_order_21_execution_of_decrees_and_orders", "First Schedule: Order 21 (Execution of Decrees and Orders)", "प्रथम अनुसूची: आदेश 21 (डिक्रियों एवं आदेशों का निष्पादन)", 125, 132),
    (18, "cpc_pyq_t18_orders_22_to_32_incidental_and_special_suits", "First Schedule: Orders 22 to 32 (Incidental & Special Suits)", "प्रथम अनुसूची: आदेश 22 से 32 (पक्षकारों की मृत्यु, वाद का प्रत्याहरण एवं विशिष्ट वाद)", 133, 142),
    (19, "cpc_pyq_t19_orders_33_to_51_indigent_injunctions_and_appeals", "First Schedule: Orders 33 to 51 (Indigent, Injunctions & Appeals)", "प्रथम अनुसूची: आदेश 33 से 51 (निर्धन व्यक्ति, व्यादेश एवं अपील)", 143, 159),
    (20, "cpc_pyq_t20_miscellaneous_and_practice_questions", "Practice & Revision Questions (Miscellaneous)", "विविध एवं अभ्यास प्रश्न (रिवीज़न)", 160, 168)
]

def parse_full_topic(doc, p_start, p_end):
    full_lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s == 'efmeefJeue Øeef›eâÙee mebefnlee, 1908' or re.match(r'^\d+$', s):
                continue
            full_lines.append(s)
    full_text = '\n'.join(full_lines)
    all_ans = list(re.finditer(r'(?:^|\n)Ans\.\s*\(([a-eA-E])\)\s*:?', full_text))

    raw_items = []
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

        # Extract explanation for question i
        # Explanation runs from ans_m.end() until the next question's stem start
        if i + 1 < len(all_ans):
            next_window = full_text[ans_m.end():all_ans[i+1].start()]
            next_d_m = list(re.finditer(r'(?:^|\n|\s)\(d\)\s*', next_window, re.I))
            if next_d_m:
                next_c_m = list(re.finditer(r'(?:^|\n|\s)\(c\)\s*', next_window[:next_d_m[-1].start()], re.I))
                next_b_m = list(re.finditer(r'(?:^|\n|\s)\(b\)\s*', next_window[:next_c_m[-1].start()], re.I)) if next_c_m else []
                next_a_m = list(re.finditer(r'(?:^|\n|\s)\(a\)\s*', next_window[:next_b_m[-1].start()], re.I)) if next_b_m else []
                if next_a_m:
                    next_before_a = next_window[:next_a_m[-1].start()]
                    next_q_m = list(re.finditer(r'(?:^|\n)\s*(\d+)(?:\.|\s+)', next_before_a))
                    if next_q_m:
                        exp_raw = next_before_a[:next_q_m[-1].start()].strip()
                    else:
                        exp_raw = next_before_a.strip()
                else:
                    exp_raw = next_window.strip()
            else:
                exp_raw = next_window.strip()
        else:
            exp_raw = full_text[ans_m.end():].strip()

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

        raw_items.append({
            "idx": i + 1,
            "orig_num": q_num,
            "stem_raw": stem_raw,
            "q_en": q_en,
            "opts_en": opts_en,
            "correct_option": corr_letter,
            "exam_tag": exam_tag if exam_tag else "State Judiciary & PCS (J) PYQ",
            "exam_year": exam_year,
            "exp_raw": exp_raw
        })

    return raw_items

def build_all():
    doc = pymupdf.open(PDF_PATH)
    total_built = 0
    total_questions = 0
    opt_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    print(f"=== Starting Clean Rebuild for Code of Civil Procedure, 1908 (20 Topics) ===")

    for topic_idx, test_id, title_en, title_hi, p_start, p_end in TESTS_CONFIG:
        print(f"\nProcessing Topic {topic_idx:02d}: {title_en} (Pages {p_start}-{p_end})...")
        raw_items = parse_full_topic(doc, p_start, p_end)
        print(f"  Parsed {len(raw_items)} questions.")

        # Identify Hindi-only questions where q_en is empty or too short
        hindi_to_translate = []
        for item in raw_items:
            if not item["q_en"] or len(item["q_en"]) < 4 or is_akruti_text(item["q_en"]):
                # Decode stem_raw to Hindi Unicode
                hi_text = akruti_to_unicode(item["stem_raw"])
                hindi_to_translate.append(hi_text)

        if hindi_to_translate:
            print(f"  Translating {len(hindi_to_translate)} Hindi-only questions to English...")
            translate_batch(hindi_to_translate, sl='hi', tl='en')

        # Translate missing English texts
        for item in raw_items:
            if not item["q_en"] or len(item["q_en"]) < 4 or is_akruti_text(item["q_en"]):
                hi_text = akruti_to_unicode(item["stem_raw"])
                item["q_en"] = trans_cache.get(hi_text, f"Question {item['orig_num']}")
                # Clean any residual issues
                if not item["q_en"] or is_akruti_text(item["q_en"]):
                    item["q_en"] = f"In Code of Civil Procedure, 1908: Question regarding {title_en}"

        # Now translate all English questions to Hindi
        en_questions = [item["q_en"] for item in raw_items]
        en_options = [opt for item in raw_items for opt in item["opts_en"]]

        print(f"  Ensuring Hindi translations for {len(en_questions)} questions & {len(en_options)} options...")
        translate_batch(en_questions, sl='en', tl='hi')
        translate_batch(en_options, sl='en', tl='hi')

        # Batch translate all explanations in parallel
        exp_hi_list = []
        for item in raw_items:
            exp_raw = item.get("exp_raw", "")
            exp_hi_d = akruti_to_unicode(exp_raw)
            item["exp_hi_decoded"] = exp_hi_d
            if len(exp_hi_d) > 15 and is_hindi(exp_hi_d):
                exp_hi_list.append(exp_hi_d)
        if exp_hi_list:
            print(f"  Batch translating {len(exp_hi_list)} explanations to English...")
            translate_batch(exp_hi_list, sl='hi', tl='en', max_workers=15)

        # Format questions for JSON
        formatted_questions = []
        for item in raw_items:
            q_num = item["idx"]
            q_en = item["q_en"]
            q_hi = trans_cache.get(q_en, q_en)
            if not is_hindi(q_hi):
                # Fallback to akruti decode if translation was identical
                decoded = akruti_to_unicode(item["stem_raw"])
                if is_hindi(decoded):
                    q_hi = decoded

            opts_en = item["opts_en"]
            opts_hi = [trans_cache.get(o, o) for o in opts_en]

            corr_letter = item["correct_option"]
            corr_idx = opt_map.get(corr_letter, 0)
            corr_opt_en = opts_en[corr_idx]
            corr_opt_hi = opts_hi[corr_idx]

            # Explanation
            exp_hi_decoded = item.get("exp_hi_decoded", "")
            if len(exp_hi_decoded) > 15 and is_hindi(exp_hi_decoded):
                exp_en_tail = trans_cache.get(exp_hi_decoded, "")
                if not exp_en_tail:
                    exp_en_tail = f"Refer to the provisions of Code of Civil Procedure, 1908."
                exp_en = f"Correct Answer: ({corr_letter}). {corr_opt_en}. {exp_en_tail}"
                exp_hi = f"सही उत्तर: ({corr_letter}) {corr_opt_hi}। {exp_hi_decoded}"
            else:
                exp_en = f"Correct Answer: ({corr_letter}). {corr_opt_en}."
                exp_hi = f"सही उत्तर: ({corr_letter}) {corr_opt_hi}।"

            q_id_str = f"{test_id}_q{q_num:03d}"

            q_obj = {
                "questionId": q_id_str,
                "questionNumber": q_num,
                "sectionId": f"sub_{topic_idx:02d}",
                "sectionTitleEn": title_en,
                "sectionTitleHi": title_hi,
                "subtopicId": f"sub_{topic_idx:02d}",
                "subtopicTitleEn": title_en,
                "subtopicTitleHi": title_hi,
                "questionType": "MCQ",
                "positiveMarks": 2.0,
                "negativeMarks": 0.66,
                "pyqTag": item["exam_tag"],
                "examYear": item["exam_year"],
                "topicTag": f"Code of Civil Procedure, 1908: {title_en}",
                "difficulty": "MEDIUM",
                "questionTextEn": q_en,
                "questionTextHi": q_hi,
                "optionsEn": opts_en,
                "optionsHi": opts_hi,
                "correctOption": corr_letter,
                "correctOptionsList": None,
                "natMin": None,
                "natMax": None,
                "explanationEn": exp_en,
                "explanationHi": exp_hi,
                "q_id": 910000 + (topic_idx * 100) + q_num,
                "q_number": q_num,
                "section": title_en,
                "exam_year_tag": item["exam_tag"],
                "question_en": q_en,
                "question_hi": q_hi,
                "options_en": opts_en,
                "options_hi": opts_hi,
                "correct_index": corr_idx,
                "correct_indices": [corr_idx],
                "explanation_en": exp_en,
                "explanation_hi": exp_hi
            }
            formatted_questions.append(q_obj)

        total_q = len(formatted_questions)
        duration_mins = max(10, int(total_q * 1.0))

        test_data = {
            "testId": test_id,
            "titleEn": f"CPC Topic {topic_idx}: {title_en}",
            "titleHi": f"सीपीसी अध्याय {topic_idx}: {title_hi}",
            "subject": "Code of Civil Procedure, 1908",
            "subjectHi": "सिविल प्रक्रिया संहिता, 1908",
            "topicId": f"cpc_t{topic_idx:02d}",
            "totalQuestions": total_q,
            "durationMinutes": duration_mins,
            "marksPerQuestion": 2.0,
            "negativeMarks": 0.66,
            "source": "Youth Competition Times PCS (J) & Higher Judicial Services PYQ (1990-2024)",
            "questions": formatted_questions
        }

        out_path = os.path.join(OUTPUT_DIR, f"{test_id}.json")
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)

        print(f"  Successfully wrote {total_q} questions to {test_id}.json")
        total_built += 1
        total_questions += total_q

    print(f"\n=== Rebuild Complete: {total_built} topics, {total_questions} total questions ===")

if __name__ == '__main__':
    build_all()
