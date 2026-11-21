import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

CACHE_FILE = 'scripts/judiciary_translation_cache.json'
PDF_PATH = r'C:\Users\yedde\Downloads\Judicial\Tort, Limitation, SRA, Trust and Equity Youth PYQ.pdf'

TORT_DIR = r'tests\judiciary_pyq\tort'
LIMITATION_DIR = r'tests\judiciary_pyq\limitation'
SRA_DIR = r'tests\judiciary_pyq\sra'
TRUST_DIR = r'tests\judiciary_pyq\trust_equity'

os.makedirs(TORT_DIR, exist_ok=True)
os.makedirs(LIMITATION_DIR, exist_ok=True)
os.makedirs(SRA_DIR, exist_ok=True)
os.makedirs(TRUST_DIR, exist_ok=True)

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

TORT_SRA_CONFIG = [
    # Law of Tort (Part 8)
    (1, 'tort_pyq_t01_definition_and_nature', 'Tort: Definition, Nature & Capacity', 'अपकृत्य: परिभाषा, प्रकृति एवं सक्षमता', 5, 21, 'tort'),
    (2, 'tort_pyq_t02_vicarious_state_liability_and_joint', 'Tort: Vicarious Liability, State Liability & Joint Tortfeasors', 'अपकृत्य: प्रतिनिधिक दायित्व, राज्य का दायित्व एवं संयुक्त अपकृत्यकर्ता', 22, 34, 'tort'),
    (3, 'tort_pyq_t03_general_defences', 'Tort: General Defences & Justification', 'अपकृत्य: सामान्य अपवाद एवं न्यायोचितता', 35, 42, 'tort'),
    (4, 'tort_pyq_t04_negligence_nuisance_and_trespass', 'Tort: Negligence, Nuisance & Trespass', 'अपकृत्य: उपेक्षा, उपताप एवं अतिचार', 43, 56, 'tort'),
    (5, 'tort_pyq_t05_defamation', 'Tort: Defamation', 'अपकृत्य: मानहानि', 57, 64, 'tort'),
    (6, 'tort_pyq_t06_strict_liability_malicious_prosecution_remedies', 'Tort: Strict Liability, Malicious Prosecution & Remedies', 'अपकृत्य: कठोर दायित्व, विद्वेषपूर्ण अभियोजन एवं उपचार', 65, 81, 'tort'),
    (7, 'tort_pyq_t07_miscellaneous_and_landmark_cases', 'Tort: Miscellaneous Cases & Practice Questions', 'अपकृत्य: विविध वाद एवं अभ्यास प्रश्न', 82, 96, 'tort'),

    # Limitation Act, 1963 (Part 9)
    (1, 'limitation_pyq_t01_limitation_of_suits_and_appeals', 'Limitation Act: Limitation of Suits, Appeals & Applications (Sec 1-11)', 'परिसीमा अधिनियम: वादों, अपीलों एवं आवेदनों की परिसीमा (धारा 1-11)', 97, 109, 'limitation'),
    (2, 'limitation_pyq_t02_computation_acknowledgment_and_schedule', 'Limitation Act: Computation, Acknowledgment & Schedule (Sec 12-32)', 'परिसीमा अधिनियम: संगणना, अभिस्वीकृति एवं अनुसूची (धारा 12-32)', 110, 123, 'limitation'),

    # Specific Relief Act, 1963 (Part 10)
    (1, 'sra_pyq_t01_possession_and_specific_performance', 'Specific Relief Act: Possession & Specific Performance (Sec 1-25)', 'विनिर्दिष्ट अनुतोष: कब्जा प्राप्त करना एवं विनिर्दिष्ट पालन (धारा 1-25)', 124, 138, 'sra'),
    (2, 'sra_pyq_t02_rectification_declaratory_injunctions', 'Specific Relief Act: Declaratory Decrees & Injunctions (Sec 26-44)', 'विनिर्दिष्ट अनुतोष: घोषणात्मक डिक्री एवं व्यादेश (धारा 26-44)', 139, 153, 'sra'),

    # Law of Trust & Equity (Part 11)
    (1, 'trust_equity_pyq_t01_equity_and_trusts', 'Law of Trust & Equity: Maxims of Equity & Indian Trusts Act', 'साम्य एवं न्यास विधि: साम्य के सूत्र एवं भारतीय न्यास अधिनियम', 154, 160, 'trust'),
]

def parse_tort_sra_questions(doc, p_start, p_end):
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s.startswith('Deheke=âlÙe efJeefOe') or s.startswith('heefjmeercee DeefOeefveÙece') or s.startswith('efJeefveefo&° Deveglees<e') or s.startswith('meecÙe SJeb vÙeeme') or re.match(r'^\d+$', s):
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

def build_tort_sra_all():
    doc = pymupdf.open(PDF_PATH)
    total_built_questions = 0
    opt_idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 0}

    for topic_idx, test_id, title_en, title_hi, p_start, p_end, act in TORT_SRA_CONFIG:
        raw_qs = parse_tort_sra_questions(doc, p_start, p_end)
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

        if act == 'tort':
            part_id = "part8_law_of_torts"
            part_title_en = "Part VIII: Law of Torts"
            part_title_hi = "भाग VIII: अपकृत्य विधि"
            topic_tag_prefix = "Law of Torts"
            shift_badge = "Judiciary PYQ (1990–2024) • Tort"
            base_qid = 980000
            out_dir = TORT_DIR
        elif act == 'limitation':
            part_id = "part9_limitation_act_1963"
            part_title_en = "Part IX: Limitation Act, 1963"
            part_title_hi = "भाग IX: परिसीमा अधिनियम, 1963"
            topic_tag_prefix = "Limitation Act, 1963"
            shift_badge = "Judiciary PYQ (1990–2024) • Limitation"
            base_qid = 985000
            out_dir = LIMITATION_DIR
        elif act == 'sra':
            part_id = "part10_specific_relief_act_1963"
            part_title_en = "Part X: Specific Relief Act, 1963"
            part_title_hi = "भाग X: विनिर्दिष्ट अनुतोष अधिनियम, 1963"
            topic_tag_prefix = "Specific Relief Act, 1963"
            shift_badge = "Judiciary PYQ (1990–2024) • SRA"
            base_qid = 990000
            out_dir = SRA_DIR
        else:
            part_id = "part11_law_of_trust_and_equity"
            part_title_en = "Part XI: Law of Trust & Equity"
            part_title_hi = "भाग XI: साम्य एवं न्यास विधि"
            topic_tag_prefix = "Law of Trust & Equity"
            shift_badge = "Judiciary PYQ (1990–2024) • Trust & Equity"
            base_qid = 995000
            out_dir = TRUST_DIR

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
    print(f"Tort, Limitation, SRA, Trust & Equity Build Complete: {len(TORT_SRA_CONFIG)} Tests Built | Total Questions: {total_built_questions}")

if __name__ == '__main__':
    build_tort_sra_all()
