import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

CACHE_FILE = 'scripts/judiciary_translation_cache.json'
PDF_PATH = r'C:\Users\yedde\Downloads\Judicial\Indian Constitution Youth PYQ.pdf'
OUTPUT_DIR = r'tests\judiciary_pyq\constitution'
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

CONST_CONFIG = [
    (1, 'const_pyq_t01_historical_background', 'Historical Background of Constitution', 'संविधान की ऐतिहासिक पृष्ठभूमि', 4, 10),
    (2, 'const_pyq_t02_preamble', 'Preamble of the Constitution', 'संविधान की प्रस्तावना', 11, 19),
    (3, 'const_pyq_t03_union_territories_and_citizenship', 'The Union & Its Territory and Citizenship (Art 1-11)', 'संघ और उसका राज्यक्षेत्र एवं नागरिकता (अनुच्छेद 1-11)', 20, 23),
    (4, 'const_pyq_t04_fundamental_rights_state_and_laws', 'Fundamental Rights - State & Inconsistent Laws (Art 12-13)', 'मूल अधिकार - राज्य की परिभाषा एवं विधियां (अनुच्छेद 12-13)', 24, 33),
    (5, 'const_pyq_t05_right_to_equality', 'Right to Equality (Art 14-18)', 'समता का अधिकार (अनुच्छेद 14-18)', 34, 46),
    (6, 'const_pyq_t06_right_to_freedom_and_life', 'Right to Freedom, Life & Personal Liberty (Art 19-22)', 'स्वतंत्रता एवं प्राण व दैहिक स्वतंत्रता का अधिकार (अनुच्छेद 19-22)', 47, 66),
    (7, 'const_pyq_t07_exploitation_religion_cultural_rights', 'Right against Exploitation, Freedom of Religion & Minorities (Art 23-31)', 'शोषण के विरुद्ध, धर्म की स्वतंत्रता एवं संस्कृति व शिक्षा (अनुच्छेद 23-31)', 67, 72),
    (8, 'const_pyq_t08_constitutional_remedies', 'Right to Constitutional Remedies & Writs (Art 32-35)', 'संवैधानिक उपचारों का अधिकार एवं रिटें (अनुच्छेद 32-35)', 73, 82),
    (9, 'const_pyq_t09_directive_principles_of_state_policy', 'Directive Principles of State Policy (Art 36-51)', 'राज्य की नीति के निदेशक तत्व (अनुच्छेद 36-51)', 83, 94),
    (10, 'const_pyq_t10_fundamental_duties', 'Fundamental Duties (Art 51A)', 'मूल कर्तव्य (अनुच्छेद 51A)', 95, 99),
    (11, 'const_pyq_t11_president_and_vice_president', 'The Union Executive - President & Vice-President (Art 52-78)', 'संघीय कार्यपालिका - राष्ट्रपति एवं उपराष्ट्रपति (अनुच्छेद 52-78)', 100, 115),
    (12, 'const_pyq_t12_parliament', 'The Parliament (Art 79-123)', 'संसद (अनुच्छेद 79-123)', 116, 127),
    (13, 'const_pyq_t13_union_judiciary_supreme_court_cag', 'The Union Judiciary - Supreme Court & CAG (Art 124-151)', 'संघीय न्यायपालिका - उच्चतम न्यायालय एवं कैग (अनुच्छेद 124-151)', 128, 145),
    (14, 'const_pyq_t14_state_executive_and_legislature', 'The State Executive & Legislature (Art 152-213)', 'राज्य कार्यपालिका एवं विधानमंडल (अनुच्छेद 152-213)', 146, 152),
    (15, 'const_pyq_t15_high_courts_and_subordinate_courts', 'High Courts & Subordinate Courts (Art 214-237)', 'उच्च न्यायालय एवं अधीनस्थ न्यायालय (अनुच्छेद 214-237)', 153, 161),
    (16, 'const_pyq_t16_panchayats_municipalities_and_uts', 'Union Territories, Panchayats & Municipalities (Art 239-243ZT)', 'संघ राज्य क्षेत्र, पंचायतें एवं नगरपालिकाएं (अनुच्छेद 239-243ZT)', 162, 165),
    (17, 'const_pyq_t17_relations_between_union_and_states', 'Relations between Union & States (Art 245-263)', 'संघ और राज्यों के बीच संबंध (अनुच्छेद 245-263)', 166, 173),
    (18, 'const_pyq_t18_finance_property_contracts_trade', 'Finance, Property, Contracts, Suits & Trade (Art 264-307)', 'वित्त, संपत्ति, संविदाएं एवं व्यापार (अनुच्छेद 264-307)', 174, 178),
    (19, 'const_pyq_t19_services_tribunals_and_elections', 'Services, Tribunals & Elections (Art 308-329)', 'अधीनस्थ सेवाएं, अधिकरण एवं निर्वाचन (अनुच्छेद 308-329)', 179, 187),
    (20, 'const_pyq_t20_emergency_and_special_provisions', 'Special Provisions, Official Language & Emergency (Art 330-360)', 'विशेष उपबंध, राजभाषा एवं आपात उपबंध (अनुच्छेद 330-360)', 188, 199),
    (21, 'const_pyq_t21_amendment_and_miscellaneous', 'Amendment of Constitution & Miscellaneous (Art 361-395)', 'संविधान का संशोधन एवं प्रकीर्ण (अनुच्छेद 361-395)', 200, 210),
    (22, 'const_pyq_t22_schedules_of_constitution', 'Schedules of the Constitution', 'संविधान की अनुसूचियां', 211, 217),
    (23, 'const_pyq_t23_landmark_and_recent_cases', 'Landmark & Recent Constitutional Cases', 'महत्वपूर्ण एवं नवीनतम संविधान वाद', 218, 232),
    (24, 'const_pyq_t24_miscellaneous_and_revision_questions', 'Miscellaneous & Revision Practice Questions', 'विविध एवं अभ्यास प्रश्न (रिवीज़न)', 233, 240)
]

def parse_const_questions(doc, p_start, p_end):
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s.startswith('YeejleerÙe mebefJeOeeve') or re.match(r'^\d+$', s):
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

def build_const_all():
    doc = pymupdf.open(PDF_PATH)
    total_built_questions = 0
    opt_idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 0}

    for topic_idx, test_id, title_en, title_hi, p_start, p_end in CONST_CONFIG:
        raw_qs = parse_const_questions(doc, p_start, p_end)
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
                "topicTag": f"Constitution of India: {title_en.split('(')[0].strip()}",
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
                "q_id": 950000 + topic_idx * 1000 + q_num,
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
            "partId": "part5_constitution_of_india",
            "partTitleEn": "Part V: Constitution of India",
            "partTitleHi": "भाग V: भारत का संविधान",
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
            "titleEn": f"Constitution Topic {topic_idx}: {title_en} ({total_q} PYQs)",
            "titleHi": f"भारतीय संविधान अध्याय {topic_idx}: {title_hi} ({total_q} विगत वर्ष प्रश्न)",
            "subtitleEn": "Part V: Constitution of India",
            "testType": "TOPIC",
            "isFree": True,
            "durationMinutes": total_q,
            "totalQuestions": total_q,
            "maxMarks": total_q * 2.0,
            "positiveMarks": 2.0,
            "negativeMarks": 0.66,
            "examYear": 2024,
            "shiftBadge": "Judiciary PYQ (1990–2024) • Constitution",
            "questions": formatted_questions
        }

        out_path = os.path.join(OUTPUT_DIR, f"{test_id}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(test_json, f, ensure_ascii=False, indent=2)

        print(f"Generated {out_path} with {total_q} questions")
        total_built_questions += total_q

    print("=" * 75)
    print(f"Constitution Build Complete: {len(CONST_CONFIG)} Tests Built | Total Questions: {total_built_questions}")

if __name__ == '__main__':
    build_const_all()
