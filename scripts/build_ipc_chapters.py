import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

CACHE_FILE = 'scripts/judiciary_translation_cache.json'
PDF_PATH = r'C:\Users\yedde\Downloads\Judicial\IPC Youth PYQ-1.pdf'
OUTPUT_DIR = r'tests\judiciary_pyq\ipc'
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

IPC_CONFIG = [
    (1, 'ipc_pyq_t01_general_introduction', 'General Introduction (Nature & Elements of Crime)', 'सामान्य प्रस्तावना (अपराध की प्रकृति एवं तत्व)', 5, 12),
    (2, 'ipc_pyq_t02_preliminary_and_jurisdiction', 'Preliminary & Jurisdiction (Sec 1-5)', 'प्रारम्भिक एवं क्षेत्राधिकार (धारा 1-5)', 13, 15),
    (3, 'ipc_pyq_t03_general_explanations', 'General Explanations & Joint Liability (Sec 6-52A)', 'साधारण स्पष्टीकरण एवं संयुक्त दायित्व (धारा 6-52A)', 16, 39),
    (4, 'ipc_pyq_t04_punishments', 'Punishments (Sec 53-75)', 'दंडों के विषय में (धारा 53-75)', 40, 48),
    (5, 'ipc_pyq_t05_general_exceptions_excusable_acts', 'General Exceptions - Excusable Acts (Sec 76-95)', 'साधारण अपवाद (धारा 76-95)', 49, 77),
    (6, 'ipc_pyq_t06_right_of_private_defence', 'Right of Private Defence (Sec 96-106)', 'प्राइवेट प्रतिरक्षा का अधिकार (धारा 96-106)', 78, 92),
    (7, 'ipc_pyq_t07_abetment', 'Abetment (Sec 107-120)', 'दुष्प्रेरण (धारा 107-120)', 93, 104),
    (8, 'ipc_pyq_t08_criminal_conspiracy', 'Criminal Conspiracy (Sec 120A-120B)', 'आपराधिक षड्यंत्र (धारा 120A-120B)', 105, 109),
    (9, 'ipc_pyq_t09_offences_against_state_and_armed_forces', 'Offences Against State & Armed Forces (Sec 121-140)', 'राज्य एवं सेना के विरुद्ध अपराध (धारा 121-140)', 110, 115),
    (10, 'ipc_pyq_t10_offences_against_public_tranquillity', 'Offences Against Public Tranquillity (Sec 141-160)', 'लोक शांति के विरुद्ध अपराध (धारा 141-160)', 116, 125),
    (11, 'ipc_pyq_t11_offences_relating_to_public_servants_and_elections', 'Public Servants, Elections & Contempt (Sec 161-190)', 'लोक सेवकों, निर्वाचन एवं अवमानना सम्बन्धी अपराध (धारा 161-190)', 126, 131),
    (12, 'ipc_pyq_t12_false_evidence_and_public_justice', 'False Evidence & Offences Against Public Justice (Sec 191-229A)', 'मिथ्या साक्ष्य एवं लोक न्याय के विरुद्ध अपराध (धारा 191-229A)', 132, 139),
    (13, 'ipc_pyq_t13_coin_stamps_public_health_and_religion', 'Coin, Public Health, Safety & Religion (Sec 230-298)', 'सिक्का, लोक स्वास्थ्य, सुरक्षा एवं धर्म सम्बन्धी अपराध (धारा 230-298)', 140, 146),
    (14, 'ipc_pyq_t14_offences_affecting_life_homicide_murder', 'Offences Affecting Life - Homicide & Murder (Sec 299-311)', 'मानव जीवन पर प्रभाव डालने वाले अपराध (धारा 299-311)', 147, 174),
    (15, 'ipc_pyq_t15_miscarriage_hurt_and_grievous_hurt', 'Miscarriage, Hurt & Grievous Hurt (Sec 312-338)', 'गर्भपात, उपहति एवं घोर उपहति (धारा 312-338)', 175, 184),
    (16, 'ipc_pyq_t16_wrongful_restraint_and_confinement', 'Wrongful Restraint & Confinement (Sec 339-348)', 'सदोष अवरोध एवं सदोष परिरोध (धारा 339-348)', 185, 189),
    (17, 'ipc_pyq_t17_criminal_force_and_assault', 'Criminal Force & Assault (Sec 349-358)', 'आपराधिक बल एवं हमला (धारा 349-358)', 190, 196),
    (18, 'ipc_pyq_t18_kidnapping_abduction_slavery', 'Kidnapping, Abduction & Forced Labour (Sec 359-374)', 'व्यपहरण, अपहरण एवं बलात्श्रम (धारा 359-374)', 197, 206),
    (19, 'ipc_pyq_t19_sexual_offences', 'Sexual Offences & Unnatural Offences (Sec 375-377)', 'यौन अपराध एवं प्रकृति विरुद्ध अपराध (धारा 375-377)', 207, 219),
    (20, 'ipc_pyq_t20_theft_extortion_robbery_dacoity', 'Theft, Extortion, Robbery & Dacoity (Sec 378-402)', 'चोरी, उद्दापन, लूट एवं डकैती (धारा 378-402)', 220, 238),
    (21, 'ipc_pyq_t21_criminal_misappropriation_and_breach_of_trust', 'Misappropriation & Breach of Trust (Sec 403-409)', 'आपराधिक दुर्विनियोग एवं न्यासभंग (धारा 403-409)', 239, 248),
    (22, 'ipc_pyq_t22_cheating_mischief_criminal_trespass', 'Cheating, Mischief & Criminal Trespass (Sec 410-462)', 'छल, रिष्टि एवं आपराधिक अतिचार (धारा 410-462)', 249, 258),
    (23, 'ipc_pyq_t23_forgery_documents_property_marks', 'Offences Relating to Documents & Property Marks (Sec 463-489E)', 'दस्तावेजों एवं संपत्ति चिह्नों सम्बन्धी अपराध (धारा 463-489E)', 259, 265),
    (24, 'ipc_pyq_t24_marriage_cruelty_defamation', 'Marriage, Cruelty & Defamation (Sec 493-502)', 'विवाह सम्बन्धी अपराध, क्रूरता एवं मानहानि (धारा 493-502)', 266, 271),
    (25, 'ipc_pyq_t25_criminal_intimidation_insult_attempt', 'Criminal Intimidation, Insult & Attempt (Sec 503-511)', 'आपराधिक अभित्रास, अपमान एवं प्रयत्न (धारा 503-511)', 272, 280),
    (26, 'ipc_pyq_t26_important_cases_and_revision_questions', 'Landmark Cases & Revision Questions', 'महत्वपूर्ण वाद एवं अभ्यास प्रश्न (रिवीज़न)', 281, 304),
]

def parse_ipc_questions(doc, p_start, p_end):
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s.startswith('YeejleerÙe oC[ mebefnlee') or re.match(r'^\d+$', s):
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

def build_ipc_all():
    doc = pymupdf.open(PDF_PATH)
    total_built_questions = 0
    opt_idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 0}

    for topic_idx, test_id, title_en, title_hi, p_start, p_end in IPC_CONFIG:
        raw_qs = parse_ipc_questions(doc, p_start, p_end)
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
                "topicTag": f"Indian Penal Code, 1860: {title_en.split('(')[0].strip()}",
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
                "q_id": 940000 + topic_idx * 1000 + q_num,
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
            "partId": "part4_ipc_1860",
            "partTitleEn": "Part IV: Indian Penal Code, 1860",
            "partTitleHi": "भाग IV: भारतीय दंड संहिता, 1860",
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
            "titleEn": f"IPC Topic {topic_idx}: {title_en} ({total_q} PYQs)",
            "titleHi": f"भारतीय दंड संहिता अध्याय {topic_idx}: {title_hi} ({total_q} विगत वर्ष प्रश्न)",
            "subtitleEn": "Part IV: Indian Penal Code, 1860",
            "testType": "TOPIC",
            "isFree": True,
            "durationMinutes": total_q,
            "totalQuestions": total_q,
            "maxMarks": total_q * 2.0,
            "positiveMarks": 2.0,
            "negativeMarks": 0.66,
            "examYear": 2024,
            "shiftBadge": "Judiciary PYQ (1990–2024) • IPC",
            "questions": formatted_questions
        }

        out_path = os.path.join(OUTPUT_DIR, f"{test_id}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(test_json, f, ensure_ascii=False, indent=2)

        print(f"Generated {out_path} with {total_q} questions")
        total_built_questions += total_q

    print("=" * 75)
    print(f"IPC Build Complete: {len(IPC_CONFIG)} Tests Built | Total Questions: {total_built_questions}")

if __name__ == '__main__':
    build_ipc_all()
