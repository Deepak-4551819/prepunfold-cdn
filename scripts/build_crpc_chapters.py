import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

PDF_PATH = r'C:\Users\yedde\Downloads\Judicial\Cr.PC Youth PYQ.pdf'
OUTPUT_DIR = r'D:\Android Project\prepunfold-cdn\tests\judiciary_pyq\crpc'
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

CRPC_TESTS_CONFIG = [
    (1, "crpc_pyq_t01_preliminary", "Preliminary (Sec 1-5)", "प्रारंभिक (धारा 1-5)", 4, 17),
    (2, "crpc_pyq_t02_constitution_of_criminal_courts", "Constitution of Criminal Courts and Offices (Sec 6-25A)", "दंड न्यायालयों और कार्यालयों का गठन (धारा 6-25A)", 18, 25),
    (3, "crpc_pyq_t03_power_of_courts", "Power of Courts (Sec 26-35)", "न्यायालयों की शक्ति (धारा 26-35)", 26, 31),
    (4, "crpc_pyq_t04_aid_to_magistrates_and_police", "Powers of Superior Police Officers & Aid to Magistrates (Sec 36-40)", "वरिष्ठ पुलिस अधिकारियों की शक्तियां एवं मजिस्ट्रेटों और पुलिस को सहायता (धारा 36-40)", 32, 33),
    (5, "crpc_pyq_t05_arrest_of_persons", "Arrest of Persons (Sec 41-60A)", "व्यक्तियों की गिरफ्तारी (धारा 41-60A)", 34, 45),
    (6, "crpc_pyq_t06_process_to_compel_appearance", "Process to Compel Appearance (Sec 61-90)", "हाजिर होने को विवश करने के लिए आदेशिकाएं (धारा 61-90)", 46, 51),
    (7, "crpc_pyq_t07_process_to_compel_production_of_things", "Process to Compel Production of Things (Sec 91-105)", "चीजें पेश करने को विवश करने के लिए आदेशिकाएं (धारा 91-105)", 52, 55),
    (8, "crpc_pyq_t08_reciprocal_arrangements", "Reciprocal Arrangements (Sec 105A-105L)", "व्यतिकारी व्यवस्था (धारा 105A-105L)", 56, 56),
    (9, "crpc_pyq_t09_security_for_keeping_peace", "Security for Keeping the Peace and Good Behaviour (Sec 106-124)", "परिशांति कायम रखने के लिए और सदाचार के लिए प्रतिभूति (धारा 106-124)", 57, 61),
    (10, "crpc_pyq_t10_maintenance_of_wives_children_parents", "Maintenance of Wives, Children and Parents (Sec 125-128)", "भरण-पोषण (धारा 125-128)", 62, 73),
    (11, "crpc_pyq_t11_public_order_and_tranquillity", "Maintenance of Public Order and Tranquillity (Sec 129-148)", "लोक व्यवस्था और प्रशांति बनाए रखना (धारा 129-148)", 74, 81),
    (12, "crpc_pyq_t12_preventive_action_of_police", "Preventive Action of the Police (Sec 149-153)", "निवारक कार्य (धारा 149-153)", 82, 82),
    (13, "crpc_pyq_t13_information_to_police_and_investigation", "Information to Police and Powers to Investigate (Sec 154-176)", "पुलिस को इत्तिला और अन्वेषण की शक्तियां (धारा 154-176)", 83, 112),
    (14, "crpc_pyq_t14_jurisdiction_in_inquiries_and_trials", "Jurisdiction of Criminal Courts in Inquiries and Trials (Sec 177-189)", "जांचों और विचारणों में दंड न्यायालयों की अधिकारिता (धारा 177-189)", 113, 118),
    (15, "crpc_pyq_t15_initiation_of_proceedings", "Conditions Requisite for Initiation of Proceedings (Sec 190-199)", "कार्यवाहियां शुरू करने के लिए अपेक्षित शर्तें (धारा 190-199)", 119, 125),
    (16, "crpc_pyq_t16_complaints_to_magistrates", "Complaints to Magistrates & Commencement of Proceedings (Sec 200-210)", "मजिस्ट्रेटों से परिवाद और कार्यवाही का प्रारंभ (धारा 200-210)", 126, 131),
    (17, "crpc_pyq_t17_the_charge", "The Charge (Sec 211-224)", "आरोप (धारा 211-224)", 132, 140),
    (18, "crpc_pyq_t18_trial_before_court_of_session", "Trial before a Court of Session (Sec 225-237)", "सत्र न्यायालय के समक्ष विचारण (धारा 225-237)", 141, 144),
    (19, "crpc_pyq_t19_trial_of_warrant_cases", "Trial of Warrant-Cases by Magistrates (Sec 238-250)", "मजिस्ट्रेट द्वारा वारंट मामलों का विचारण (धारा 238-250)", 145, 148),
    (20, "crpc_pyq_t20_trial_of_summons_cases", "Trial of Summons-Cases by Magistrates (Sec 251-259)", "मजिस्ट्रेट द्वारा समन मामलों का विचारण (धारा 251-259)", 149, 151),
    (21, "crpc_pyq_t21_summary_trials", "Summary Trials (Sec 260-265)", "संक्षिप्त विचारण (धारा 260-265)", 152, 155),
    (22, "crpc_pyq_t22_plea_bargaining", "Plea Bargaining (Sec 265A-265L)", "अभिवचन का सौदा (धारा 265A-265L)", 156, 159),
    (23, "crpc_pyq_t23_attendance_of_confined_persons", "Attendance of Persons Confined in Prisons (Sec 266-271)", "कारागारों में परिरुद्ध या निरूद्ध व्यक्तियों की हाजिरी (धारा 266-271)", 160, 160),
    (24, "crpc_pyq_t24_evidence_in_inquiries_and_trials", "Evidence in Inquiries and Trials (Sec 272-299)", "जांचों और विचारणों में साक्ष्य (धारा 272-299)", 161, 163),
    (25, "crpc_pyq_t25_general_provisions_inquiries_trials", "General Provisions as to Inquiries and Trials (Sec 300-327)", "जांचों और विचारणों के बारे में साधारण उपबंध (धारा 300-327)", 164, 187),
    (26, "crpc_pyq_t26_unsound_mind_accused", "Provisions as to Accused Persons of Unsound Mind (Sec 328-352)", "विकृतचित्त अभियुक्त व्यक्तियों के बारे में उपबंध (धारा 328-352)", 188, 188),
    (27, "crpc_pyq_t27_the_judgment", "The Judgment (Sec 353-365)", "निर्णय (धारा 353-365)", 189, 197),
    (28, "crpc_pyq_t28_death_sentences_confirmation", "Submission of Death Sentences for Confirmation (Sec 366-371)", "मृत्यु दंडादेशों की पुष्टि (धारा 366-371)", 198, 199),
    (29, "crpc_pyq_t29_appeals", "Appeals (Sec 372-394)", "अपील (धारा 372-394)", 200, 209),
    (30, "crpc_pyq_t30_reference_and_revision", "Reference and Revision (Sec 395-405)", "निर्देश और पुनरीक्षण (धारा 395-405)", 210, 212),
    (31, "crpc_pyq_t31_transfer_of_criminal_cases", "Transfer of Criminal Cases (Sec 406-412)", "आपराधिक मामलों का अंतरण (धारा 406-412)", 213, 214),
    (32, "crpc_pyq_t32_execution_suspension_remission_sentences", "Execution, Suspension & Remission of Sentences (Sec 413-435)", "दंडादेशों का निष्पादन, निलंबन और परिहार (धारा 413-435)", 215, 218),
    (33, "crpc_pyq_t33_provisions_as_to_bail_and_bonds", "Provisions as to Bail and Bonds (Sec 436-450)", "जमानत और बंधपत्र (धारा 436-450)", 219, 228),
    (34, "crpc_pyq_t34_disposal_of_property", "Disposal of Property (Sec 451-459)", "संपत्ति का व्ययन (धारा 451-459)", 229, 229),
    (35, "crpc_pyq_t35_irregular_proceedings", "Irregular Proceedings (Sec 460-466)", "अनियमित कार्यवाहियां (धारा 460-466)", 230, 235),
    (36, "crpc_pyq_t36_limitation_for_cognizance", "Limitation for Taking Cognizance of Certain Offences (Sec 467-473)", "अपराधों का संज्ञान करने के लिए परिसीमा (धारा 467-473)", 236, 240),
    (37, "crpc_pyq_t37_miscellaneous_provisions", "Miscellaneous Provisions (Sec 474-484)", "प्रकीर्ण (धारा 474-484)", 241, 243),
    (38, "crpc_pyq_t38_schedules_classification_of_offences", "First and Second Schedules (Classification of Offences)", "प्रथम एवं द्वितीय अनुसूची (अपराधों का वर्गीकरण)", 244, 246),
    (39, "crpc_pyq_t39_practice_and_revision_questions", "Practice and Revision Questions (Miscellaneous)", "विविध एवं अभ्यास प्रश्न (रिवीज़न)", 247, 256)
]

def parse_crpc_questions(doc, p_start, p_end):
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s.startswith('oC[ Øeef›eâÙee mebefnlee') or re.match(r'^\d+$', s):
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

def build_crpc_all():
    doc = pymupdf.open(PDF_PATH)
    total_built = 0
    total_questions_all = 0
    opt_idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    print(f"=== Starting Build for Code of Criminal Procedure, 1973 (39 Topics) ===")

    for topic_idx, test_id, title_en, title_hi, p_start, p_end in CRPC_TESTS_CONFIG:
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

        raw_qs = parse_crpc_questions(doc, p_start, p_end)
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
                "topicTag": f"Code of Criminal Procedure, 1973: {title_en.split('(')[0].strip()}",
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
                "q_id": 920000 + topic_idx * 100 + q_num,
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
            "partId": "part2_crpc_1973",
            "partTitleEn": "Part II: Code of Criminal Procedure, 1973",
            "partTitleHi": "भाग II: दंड प्रक्रिया संहिता, 1973",
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
            "titleEn": f"CrPC Topic {topic_idx}: {title_en} ({total_q} PYQs)",
            "titleHi": f"दंड प्रक्रिया संहिता अध्याय {topic_idx}: {title_hi} ({total_q} विगत वर्ष प्रश्न)",
            "subtitleEn": "Part II: Code of Criminal Procedure, 1973",
            "testType": "TOPIC",
            "isFree": True,
            "durationMinutes": total_q,
            "totalQuestions": total_q,
            "maxMarks": total_q * 2.0,
            "positiveMarks": 2.0,
            "negativeMarks": 0.66,
            "examYear": 2024,
            "shiftBadge": "Judiciary PYQ (1990–2024) • CrPC",
            "questions": formatted_questions
        }

        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(test_json, f, ensure_ascii=False, indent=2)

        print(f"Generated {out_file} with {total_q} questions")
        total_built += 1
        total_questions_all += total_q

    print("="*75)
    print(f"CrPC Build Complete: {total_built} Tests Built | Total Questions: {total_questions_all}")

if __name__ == "__main__":
    build_crpc_all()
