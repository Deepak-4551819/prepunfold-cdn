import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

CACHE_FILE = 'scripts/judiciary_translation_cache.json'
PDF_PATH = r'C:\Users\yedde\Downloads\Judicial\Juris. & Int. Organization Youth PYQ.pdf'

JURIS_DIR = r'tests\judiciary_pyq\jurisprudence'
INT_ORG_DIR = r'tests\judiciary_pyq\international_org'

os.makedirs(JURIS_DIR, exist_ok=True)
os.makedirs(INT_ORG_DIR, exist_ok=True)

# Load existing translation cache
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            trans_cache = json.load(f)
    except:
        trans_cache = {}
else:
    trans_cache = {}

def is_hindi(text):
    if not text:
        return False
    devanagari_chars = len(re.findall(r'[\u0900-\u097F]', text))
    return devanagari_chars >= 2

def translate_batch(texts, max_workers=20):
    to_fetch = []
    for t in texts:
        t_clean = t.strip()
        if not t_clean:
            continue
        if is_hindi(t_clean):
            continue
        if t_clean not in trans_cache:
            to_fetch.append(t_clean)

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

JURIS_INT_CONFIG = [
    # Part 12: Jurisprudence (8 topics)
    (1, 'juris_pyq_t01_definition_and_scope', 'Jurisprudence: Definition & Scope', 'विधिशास्त्र: परिभाषा एवं क्षेत्र विस्तार', 5, 11, 'juris'),
    (2, 'juris_pyq_t02_natural_law_and_analytical_school', 'Jurisprudence: Natural Law & Analytical School', 'विधिशास्त्र: प्राकृतिक विधि एवं विश्लेषणात्मक विचारधारा', 12, 31, 'juris'),
    (3, 'juris_pyq_t03_historical_sociological_realist_schools', 'Jurisprudence: Historical, Sociological & Realist Schools', 'विधिशास्त्र: ऐतिहासिक, समाजशास्त्रीय एवं यथार्थवादी विचारधारा', 32, 42, 'juris'),
    (4, 'juris_pyq_t04_sources_of_law_custom_precedent_legislation', 'Jurisprudence: Sources of Law (Custom, Legislation, Precedent)', 'विधिशास्त्र: विधि के स्रोत (रूढ़ि, विधान, न्यायिक पूर्व निर्णय)', 43, 53, 'juris'),
    (5, 'juris_pyq_t05_jural_concepts_rights_and_duties', 'Jurisprudence: Jural Concepts, Legal Rights & Duties', 'विधिशास्त्र: विधिक संकल्पनाएं, अधिकार एवं कर्तव्य', 54, 66, 'juris'),
    (6, 'juris_pyq_t06_possession_and_ownership', 'Jurisprudence: Possession and Ownership', 'विधिशास्त्र: कब्जा एवं स्वामित्व', 67, 77, 'juris'),
    (7, 'juris_pyq_t07_person_property_and_liability', 'Jurisprudence: Juristic Persons, Property & Liability', 'विधिशास्त्र: विधिक व्यक्ति, संपत्ति एवं दायित्व', 78, 86, 'juris'),
    (8, 'juris_pyq_t08_miscellaneous_and_practice_questions', 'Jurisprudence: Landmark Jurists & Revision Questions', 'विधिशास्त्र: विविध एवं अभ्यास प्रश्न', 87, 101, 'juris'),

    # Part 13: International Organisations & Current International Affairs (7 topics)
    (1, 'int_org_pyq_t01_un_charter_and_principles', 'International Org: UN Charter, Purposes & Principles', 'अंतर्राष्ट्रीय संगठन: संयुक्त राष्ट्र संघ, उद्देश्य एवं सिद्धांत', 102, 116, 'int_org'),
    (2, 'int_org_pyq_t02_general_assembly', 'International Org: General Assembly', 'अंतर्राष्ट्रीय संगठन: महासभा', 117, 125, 'int_org'),
    (3, 'int_org_pyq_t03_security_council', 'International Org: Security Council', 'अंतर्राष्ट्रीय संगठन: सुरक्षा परिषद', 126, 134, 'int_org'),
    (4, 'int_org_pyq_t04_ecosoc_trusteeship_secretariat', 'International Org: ECOSOC, Trusteeship & Secretariat', 'अंतर्राष्ट्रीय संगठन: आर्थिक व सामाजिक परिषद, न्यासिता एवं सचिवालय', 135, 140, 'int_org'),
    (5, 'int_org_pyq_t05_international_court_of_justice', 'International Org: International Court of Justice (ICJ)', 'अंतर्राष्ट्रीय संगठन: अंतर्राष्ट्रीय न्यायालय', 141, 176, 'int_org'),
    (6, 'int_org_pyq_t06_secretariat_and_specialized_agencies', 'International Org: Secretariat, Specialized Agencies & Treaties', 'अंतर्राष्ट्रीय संगठन: सचिवालय, विशिष्ट अभिकरण एवं विविध', 177, 192, 'int_org'),
    (7, 'int_org_pyq_t07_current_international_affairs', 'Current International Affairs & Conventions', 'वर्तमान अंतर्राष्ट्रीय प्रकरण एवं अभिसमय', 193, 208, 'int_org'),
]

def parse_juris_int_questions(doc, p_start, p_end):
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s.startswith('efJeefOeMeem$e') or s.startswith('Devleje&°^erÙe mebie\"ve') or re.match(r'^\d+$', s):
                continue
            lines.append(l)
    text = '\n'.join(lines)

    ans_matches = list(re.finditer(r'\nAns\s*[\.:]\s*\(([a-eA-E\*&, ]+)\)', text))
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
                if re.search(r'(P\.C\.S|I\.A\.S|U\.P|M\.P|R\.O|A\.R\.O|B\.P|R\.A\.S|Uttarakhand|Jharkhand|Chhattisgarh|Bihar|Rajasthan|Haryana|MPHC|UPPCS|BPSC|RJS|JS|CJ|APO|ADPO|APP|Pre|Mains|\b\d{4}\b)', ls, re.I) and len(actual_d_lines) > 0:
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

def build_juris_int_all():
    doc = pymupdf.open(PDF_PATH)
    total_built_questions = 0
    opt_idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 0}

    for topic_idx, test_id, title_en, title_hi, p_start, p_end, act in JURIS_INT_CONFIG:
        raw_qs = parse_juris_int_questions(doc, p_start, p_end)
        print(f"Translating & Building {test_id} ({len(raw_qs)} Qs)...")

        texts_to_trans = []
        for q in raw_qs:
            texts_to_trans.append(q["q_en"])
            for opt in q["opts_en"]:
                texts_to_trans.append(opt)

        trans_results = translate_batch(texts_to_trans)

        trans_q_texts = []
        trans_opts = []
        cursor = 0
        for q in raw_qs:
            trans_q_texts.append(trans_results[cursor])
            cursor += 1
            for _ in range(4):
                trans_opts.append(trans_results[cursor])
                cursor += 1

        formatted_questions = []
        subtopic_id = f"sub_{test_id}"
        subtopic_title_en = f"(i) {title_en}"
        subtopic_title_hi = f"(i) {title_hi}"

        if act == 'juris':
            part_id = "part12_jurisprudence"
            part_title_en = "Part XII: Jurisprudence"
            part_title_hi = "भाग XII: विधिशास्त्र"
            topic_tag_prefix = "Jurisprudence"
            shift_badge = "Judiciary PYQ (1990–2024) • Jurisprudence"
            base_qid = 996000
            out_dir = JURIS_DIR
        else:
            part_id = "part13_international_organisations"
            part_title_en = "Part XIII: International Organisations & Current International Affairs"
            part_title_hi = "भाग XIII: अंतर्राष्ट्रीय संगठन एवं वर्तमान अंतर्राष्ट्रीय प्रकरण"
            topic_tag_prefix = "International Organisations"
            shift_badge = "Judiciary PYQ (1990–2024) • Int Org"
            base_qid = 998000
            out_dir = INT_ORG_DIR

        for i, q in enumerate(raw_qs):
            q_num = q["num"]
            opts_en = q["opts_en"]
            opts_hi = trans_opts[i*4 : (i+1)*4]
            corr_letter = q["correct_opt"]
            corr_idx = opt_idx_map.get(corr_letter, 0)

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
                "topicTag": f"{topic_tag_prefix}: {title_en.split('(')[0].strip()}",
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
                "q_id": base_qid + topic_idx * 1000 + q_num,
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
            "partId": part_id,
            "partTitleEn": part_title_en,
            "partTitleHi": part_title_hi,
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
            "titleEn": f"{title_en} ({total_q} PYQs)",
            "titleHi": f"{title_hi} ({total_q} विगत वर्ष प्रश्न)",
            "subtitleEn": part_title_en,
            "testType": "TOPIC",
            "isFree": True,
            "durationMinutes": total_q,
            "totalQuestions": total_q,
            "maxMarks": total_q * 2.0,
            "positiveMarks": 2.0,
            "negativeMarks": 0.66,
            "examYear": 2024,
            "shiftBadge": shift_badge,
            "questions": formatted_questions
        }

        out_path = os.path.join(out_dir, f"{test_id}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(test_json, f, ensure_ascii=False, indent=2)

        print(f"Generated {out_path} with {total_q} questions")
        total_built_questions += total_q

    print("=" * 75)
    print(f"Jurisprudence & International Organisations Build Complete: {len(JURIS_INT_CONFIG)} Tests Built | Total Questions: {total_built_questions}")

if __name__ == '__main__':
    build_juris_int_all()
