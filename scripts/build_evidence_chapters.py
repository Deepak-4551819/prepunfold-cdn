import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

PDF_PATH = r'C:\Users\yedde\Downloads\Judicial\Evidence Youth PYQ(2)(1).pdf'
OUTPUT_DIR = r'D:\Android Project\prepunfold-cdn\tests\judiciary_pyq\evidence'
CACHE_FILE = r'D:\Android Project\prepunfold-cdn\scripts\judiciary_translation_cache.json'

os.makedirs(OUTPUT_DIR, exist_ok=True)

trans_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            trans_cache = json.load(f)
    except:
        trans_cache = {}

def is_hindi(text):
    if not text:
        return False
    return bool(re.search(r'[\u0900-\u097F]', text))

def translate_batch(texts, max_workers=14):
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

EVIDENCE_CONFIG = [
    (1, 'evidence_pyq_t01_preliminary', 'Preliminary (Sec 1-4)', 'प्रारंभिक (धारा 1-4)', 4, 20),
    (2, 'evidence_pyq_t02_relevancy_and_res_gestae', 'Relevancy of Facts & Res Gestae (Sec 5-16)', 'तथ्यों की सुसंगति एवं रेस जेस्टे (धारा 5-16)', 21, 43),
    (3, 'evidence_pyq_t03_admissions_and_confessions', 'Admissions and Confessions (Sec 17-31)', 'स्वीकृति एवं संस्वीकृति (धारा 17-31)', 44, 71),
    (4, 'evidence_pyq_t04_dying_declaration_and_statements', 'Dying Declaration & Statements (Sec 32-33)', 'मृत्युकालिक कथन एवं सुसंगत कथन (धारा 32-33)', 72, 88),
    (5, 'evidence_pyq_t05_statements_under_special_circumstances', 'Statements under Special Circumstances & Judgments (Sec 34-44)', 'विशेष परिस्थितियों में किए गए कथन एवं निर्णय (धारा 34-44)', 89, 97),
    (6, 'evidence_pyq_t06_expert_opinion_and_character', 'Opinions of Third Persons & Character (Sec 45-55)', 'अन्य व्यक्तियों की राय एवं शील (धारा 45-55)', 98, 111),
    (7, 'evidence_pyq_t07_facts_need_not_be_proved', 'Facts Which Need Not Be Proved (Sec 56-58)', 'तथ्य जिनका साबित किया जाना आवश्यक नहीं (धारा 56-58)', 112, 116),
    (8, 'evidence_pyq_t08_oral_and_documentary_evidence', 'Oral and Documentary Evidence (Sec 59-73A)', 'मौखिक एवं दस्तावेजी साक्ष्य (धारा 59-73A)', 117, 136),
    (9, 'evidence_pyq_t09_public_documents', 'Public Documents (Sec 74-78)', 'लोक दस्तावेज (धारा 74-78)', 137, 141),
    (10, 'evidence_pyq_t10_presumptions_as_to_documents', 'Presumptions as to Documents (Sec 79-90A)', 'दस्तावेजों के बारे में उपधारणाएं (धारा 79-90A)', 142, 148),
    (11, 'evidence_pyq_t11_exclusion_of_oral_by_documentary_evidence', 'Exclusion of Oral by Documentary Evidence (Sec 91-100)', 'दस्तावेजी साक्ष्य द्वारा मौखिक साक्ष्य का अपवर्जन (धारा 91-100)', 149, 154),
    (12, 'evidence_pyq_t12_burden_of_proof', 'Burden of Proof and Presumptions (Sec 101-114A)', 'सबूत का भार एवं उपधारणाएं (धारा 101-114A)', 155, 177),
    (13, 'evidence_pyq_t13_estoppel', 'Estoppel (Sec 115-117)', 'विबंध (धारा 115-117)', 178, 183),
    (14, 'evidence_pyq_t14_witnesses_competency_privilege', 'Witnesses, Competency and Privileges (Sec 118-134)', 'साक्षी, सक्षमता एवं विशेषाधिकार (धारा 118-134)', 184, 203),
    (15, 'evidence_pyq_t15_examination_of_witnesses', 'Examination of Witnesses (Sec 135-166)', 'साक्षियों की परीक्षा (धारा 135-166)', 204, 226),
    (16, 'evidence_pyq_t16_improper_admission_and_rejection', 'Improper Admission and Rejection of Evidence (Sec 167)', 'साक्ष्य के अनुचित ग्रहण और अग्रहण (धारा 167)', 227, 227),
    (17, 'evidence_pyq_t17_practice_and_revision_questions', 'Practice and Revision Questions (Miscellaneous)', 'विविध एवं अभ्यास प्रश्न (रिवीज़न)', 228, 240)
]

def parse_evidence_questions(doc, p_start, p_end):
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s.startswith('YeejleerÙe mee#Ùe DeefOeefveÙece') or re.match(r'^\d+$', s):
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

def build_evidence_all():
    doc = pymupdf.open(PDF_PATH)
    total_built = 0
    total_questions_all = 0
    opt_idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    print(f"=== Starting Build for Indian Evidence Act, 1872 (17 Topics) ===")

    for topic_idx, test_id, title_en, title_hi, p_start, p_end in EVIDENCE_CONFIG:
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

        raw_qs = parse_evidence_questions(doc, p_start, p_end)
        if not raw_qs:
            print(f"Warning: No questions parsed for {test_id} (pp. {p_start}-{p_end})")
            continue

        print(f"Translating & Building {test_id} ({len(raw_qs)} Qs)...")

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
                "topicTag": f"Indian Evidence Act, 1872: {title_en.split('(')[0].strip()}",
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
                "q_id": 930000 + topic_idx * 100 + q_num,
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
            "partId": "part3_evidence_1872",
            "partTitleEn": "Part III: Indian Evidence Act, 1872",
            "partTitleHi": "भाग III: भारतीय साक्ष्य अधिनियम, 1872",
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
            "titleEn": f"Evidence Act Topic {topic_idx}: {title_en} ({total_q} PYQs)",
            "titleHi": f"भारतीय साक्ष्य अधिनियम अध्याय {topic_idx}: {title_hi} ({total_q} विगत वर्ष प्रश्न)",
            "subtitleEn": "Part III: Indian Evidence Act, 1872",
            "testType": "TOPIC",
            "isFree": True,
            "durationMinutes": total_q,
            "totalQuestions": total_q,
            "maxMarks": total_q * 2.0,
            "positiveMarks": 2.0,
            "negativeMarks": 0.66,
            "examYear": 2024,
            "shiftBadge": "Judiciary PYQ (1990–2024) • Evidence",
            "questions": formatted_questions
        }

        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(test_json, f, ensure_ascii=False, indent=2)

        print(f"Generated {out_file} with {total_q} questions")
        total_built += 1
        total_questions_all += total_q

    print("="*75)
    print(f"Evidence Act Build Complete: {total_built} Tests Built | Total Questions: {total_questions_all}")

if __name__ == "__main__":
    build_evidence_all()
