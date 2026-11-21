import pymupdf
import re
import json
import os
import requests
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

# Preload from existing caches if available
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

def translate_batch(texts, max_workers=12):
    to_fetch = [t for t in texts if t and (t not in trans_cache or not is_hindi(trans_cache.get(t, "")))]

    def fetch_one(text):
        if not text:
            return text, ""
        if len(text) > 1200:
            parts = re.split(r'(\.\s+)', text)
            translated_parts = []
            curr = ""
            for p in parts:
                if len(curr) + len(p) < 1000:
                    curr += p
                else:
                    if curr:
                        _, tr = fetch_one(curr)
                        translated_parts.append(tr)
                    curr = p
            if curr:
                _, tr = fetch_one(curr)
                translated_parts.append(tr)
            return text, " ".join(translated_parts)

        url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=hi&q={urllib.parse.quote(text)}"
        for _ in range(2):
            try:
                r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=7)
                if r.status_code == 200:
                    res = r.json()
                    if isinstance(res, list) and len(res) > 0 and isinstance(res[0], str):
                        return text, res[0]
            except:
                pass
        return text, text

    if to_fetch:
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

def split_en_hi(text_block):
    if '/' in text_block:
        return text_block.split('/')[0].strip()
    lines = [l.strip() for l in text_block.split('\n') if l.strip()]
    if not lines:
        return text_block.strip()
    en_lines = []
    for line in lines:
        has_akruti = any(ord(c) > 127 for c in line) or bool(re.search(r'(keâ|ef|me|ue|Je|Ce|Øe|›eâ|ne|le|Le|oe|Oe|ve|he|ye|Ye|ce|Ùe|Me|<e)', line))
        words = re.findall(r'[a-zA-Z]+', line)
        if len(words) > 0 and not has_akruti:
            en_lines.append(line)
        elif not en_lines:
            en_lines.append(line)
        else:
            break
    return ' '.join(en_lines).strip()

def find_4_options_sequential(s):
    m_a = re.search(r'(?:^|\n|\s)\(a\)\s*', s, re.I)
    if not m_a: return None
    m_b = re.search(r'(?:^|\n|\s)\(b\)\s*', s[m_a.end():], re.I)
    if not m_b: return None
    b_start = m_a.end() + m_b.start()
    b_end = m_a.end() + m_b.end()
    m_c = re.search(r'(?:^|\n|\s)\(c\)\s*', s[b_end:], re.I)
    if not m_c: return None
    c_start = b_end + m_c.start()
    c_end = b_end + m_c.end()
    m_d = re.search(r'(?:^|\n|\s)\(d\)\s*', s[c_end:], re.I)
    if not m_d: return None
    d_start = c_end + m_d.start()
    d_end = c_end + m_d.end()
    return [(m_a.start(), m_a.end()), (b_start, b_end), (c_start, c_end), (d_start, d_end)]

# Full 20 topic breakdown
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

def parse_questions_from_pages(doc, p_start, p_end):
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s == 'efmeefJeue Øeef›eâÙee mebefnlee, 1908' or re.match(r'^\d+$', s):
                continue
            lines.append(l)
    text = '\n'.join(lines)

    ans_matches = list(re.finditer(r'\nAns\.\s*\(([a-eA-E\*&, ]+)\)\s*:?', text))
    if not ans_matches:
        return []

    questions = []
    for i, ans_m in enumerate(ans_matches):
        ans_start = ans_m.start()
        ans_end = ans_m.end()
        ans_str = ans_m.group(1).upper()
        m_let = re.search(r'[A-E]', ans_str)
        corr_letter = m_let.group(0) if m_let else 'A'

        prev_ans_end = ans_matches[i-1].end() if i > 0 else 0
        window = text[prev_ans_end:ans_start]

        q_num_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*\.\s+', window))
        if q_num_matches:
            q_num = int(q_num_matches[0].group(1))
            q_start_idx = prev_ans_end + q_num_matches[0].start()
        else:
            q_num = i + 1
            q_start_idx = prev_ans_end

        pre_ans = text[q_start_idx:ans_start].strip()
        pre_ans = re.sub(r'^\n?\s*\d+\s*\.\s*', '', pre_ans).strip()

        if i + 1 < len(ans_matches):
            next_window = text[ans_end:ans_matches[i+1].start()]
            next_q_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*\.\s+', next_window))
            if next_q_matches:
                exp_end = ans_end + next_q_matches[0].start()
            else:
                exp_end = ans_matches[i+1].start()
        else:
            exp_end = len(text)

        explanation = text[ans_end:exp_end].strip()

        opt_ranges = find_4_options_sequential(pre_ans)
        if opt_ranges:
            raw_stem = pre_ans[:opt_ranges[0][0]].strip()
            raw_options = [
                pre_ans[opt_ranges[0][1]:opt_ranges[1][0]].strip(),
                pre_ans[opt_ranges[1][1]:opt_ranges[2][0]].strip(),
                pre_ans[opt_ranges[2][1]:opt_ranges[3][0]].strip(),
                pre_ans[opt_ranges[3][1]:].strip()
            ]

            d_lines = raw_options[3].split('\n')
            exam_tag = ""
            actual_d_lines = []
            for l in d_lines:
                ls = l.strip()
                if re.search(r'(P\.C\.S|I\.A\.S|U\.P|M\.P|R\.O|A\.R\.O|B\.P|R\.A\.S|Uttarakhand|Jharkhand|Chhattisgarh|Bihar|Rajasthan|Haryana|MPHC|UPPCS|BPSC|RJS|JS|CJ|Pre|Mains|\b\d{4}\b)', ls, re.I) and len(actual_d_lines) > 0:
                    exam_tag = (exam_tag + " " + ls).strip()
                else:
                    actual_d_lines.append(l)
            raw_options[3] = '\n'.join(actual_d_lines).strip()
        else:
            raw_stem = pre_ans
            raw_options = ["", "", "", ""]
            exam_tag = ""

        q_en = split_en_hi(raw_stem)
        opts_en = [split_en_hi(o) for o in raw_options]

        q_en = re.sub(r'\s+', ' ', q_en).strip()
        opts_en = [re.sub(r'\s+', ' ', o).strip() for o in opts_en]

        for idx_o in range(4):
            if not opts_en[idx_o]:
                opts_en[idx_o] = f"Option {chr(ord('A') + idx_o)}"

        m_yr = re.search(r'\b(19\d\d|20\d\d)\b', exam_tag)
        exam_year = int(m_yr.group(1)) if m_yr else 2024

        questions.append({
            "num": i + 1,
            "orig_num": q_num,
            "q_en": q_en if q_en else f"Question {i+1}",
            "opts_en": opts_en,
            "correct_opt": corr_letter,
            "exam_tag": exam_tag if exam_tag else "State Judiciary & PCS (J) PYQ",
            "exam_year": exam_year,
            "explanation": explanation
        })

    return questions

def build_all():
    doc = pymupdf.open(PDF_PATH)
    total_built = 0
    total_questions_all = 0
    opt_idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    print(f"=== Starting Build for Code of Civil Procedure, 1908 (20 Topics) ===")

    for topic_idx, test_id, title_en, title_hi, p_start, p_end in TESTS_CONFIG:
        out_file = os.path.join(OUTPUT_DIR, f"{test_id}.json")

        if os.path.exists(out_file):
            try:
                with open(out_file, 'r', encoding='utf-8') as f:
                    existing = json.load(f)
                qs = existing.get("questions", [])
                if len(qs) > 0 and any(is_hindi(q.get("questionTextHi", "")) for q in qs[:min(5, len(qs))]):
                    print(f"Skipping already generated test: {test_id} ({len(qs)} Qs)")
                    total_built += 1
                    total_questions_all += len(qs)
                    continue
            except:
                pass

        raw_qs = parse_questions_from_pages(doc, p_start, p_end)
        if not raw_qs:
            print(f"Warning: No questions parsed for {test_id} (pp. {p_start}-{p_end})")
            continue

        print(f"Translating & Building {test_id} ({len(raw_qs)} Qs)...")

        # Batch translation
        q_texts = [q["q_en"] for q in raw_qs]
        all_opts = []
        for q in raw_qs:
            all_opts.extend(q["opts_en"])

        trans_q_texts = translate_batch(q_texts)
        trans_opts = translate_batch(all_opts)

        formatted_questions = []
        subtopic_id = f"sub_{topic_idx:02d}_{test_id.split('_')[-1]}"
        subtopic_title_en = f"(i) {title_en}"
        subtopic_title_hi = f"(i) {title_hi}"

        for i, q in enumerate(raw_qs):
            q_num = q["num"]
            opts_en = q["opts_en"]
            opts_hi = trans_opts[i*4 : (i+1)*4]
            corr_letter = q["correct_opt"]
            corr_idx = opt_idx_map.get(corr_letter, 0)

            # Correct answer option text for clear explanation
            corr_text_en = opts_en[corr_idx] if corr_idx < len(opts_en) else ""
            corr_text_hi = opts_hi[corr_idx] if corr_idx < len(opts_hi) else ""

            exp_en = f"Correct Answer: ({corr_letter}). {corr_text_en}."
            exp_hi = f"सही उत्तर: ({corr_letter}) {corr_text_hi}।"

            q_obj = {
                "questionId": f"{test_id}_q{q_num:03d}",
                "questionNumber": q_num,
                "sectionId": subtopic_id,
                "sectionTitleEn": f"{title_en}",
                "sectionTitleHi": f"{title_hi}",
                "subtopicId": subtopic_id,
                "subtopicTitleEn": subtopic_title_en,
                "subtopicTitleHi": subtopic_title_hi,
                "questionType": "MCQ",
                "positiveMarks": 2.0,
                "negativeMarks": 0.66,
                "pyqTag": q["exam_tag"],
                "examYear": q["exam_year"],
                "topicTag": f"Code of Civil Procedure, 1908: {title_en.split('(')[0].strip()}",
                "difficulty": "MEDIUM",
                "questionTextEn": q["q_en"],
                "questionTextHi": trans_q_texts[i],
                "optionsEn": opts_en,
                "optionsHi": opts_hi,
                "correctOption": corr_letter,
                "correctOptionsList": None,
                "natMin": None,
                "natMax": None,
                "explanationEn": exp_en,
                "explanationHi": exp_hi,
                "q_id": 910000 + topic_idx * 100 + q_num,
                "q_number": q_num,
                "section": f"{title_en}",
                "exam_year_tag": q["exam_tag"],
                "question_en": q["q_en"],
                "question_hi": trans_q_texts[i],
                "options_en": opts_en,
                "options_hi": opts_hi,
                "correct_index": corr_idx,
                "correct_indices": [corr_idx],
                "explanation_en": exp_en,
                "explanation_hi": exp_hi
            }
            formatted_questions.append(q_obj)

        total_q = len(formatted_questions)
        test_json = {
            "testId": test_id,
            "categoryId": "judiciary_pyq",
            "partId": "part1_cpc_1908",
            "partTitleEn": "Part I: Code of Civil Procedure, 1908",
            "partTitleHi": "भाग I: सिविल प्रक्रिया संहिता, 1908",
            "topicNumber": topic_idx,
            "topicTitleEn": f"{topic_idx}. {title_en}",
            "topicTitleHi": f"{topic_idx}. {title_hi}",
            "subtopics": [
                {
                    "subtopicId": subtopic_id,
                    "subtopicTitleEn": subtopic_title_en,
                    "subtopicTitleHi": subtopic_title_hi,
                    "questionCount": total_q
                }
            ],
            "titleEn": f"CPC Topic {topic_idx}: {title_en} ({total_q} PYQs)",
            "titleHi": f"सिविल प्रक्रिया संहिता अध्याय {topic_idx}: {title_hi} ({total_q} विगत वर्ष प्रश्न)",
            "subtitleEn": "Part I: Code of Civil Procedure, 1908",
            "testType": "TOPIC",
            "isFree": True,
            "durationMinutes": total_q,
            "totalQuestions": total_q,
            "maxMarks": total_q * 2.0,
            "positiveMarks": 2.0,
            "negativeMarks": 0.66,
            "examYear": 2024,
            "shiftBadge": "Judiciary PYQ (1990–2024) • CPC",
            "questions": formatted_questions
        }

        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(test_json, f, ensure_ascii=False, indent=2)

        print(f"Generated {out_file} with {total_q} questions")
        total_built += 1
        total_questions_all += total_q

    print("="*75)
    print(f"CPC Build Complete: {total_built} Tests Built | Total Questions: {total_questions_all}")

if __name__ == "__main__":
    build_all()
