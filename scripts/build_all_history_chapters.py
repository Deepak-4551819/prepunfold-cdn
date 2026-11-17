import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

PDF_PATH = r'C:\Users\yedde\Downloads\Ghatnachakra History 2024_ (1)(1).pdf'
OUTPUT_DIR = r'D:\Android Project\prepunfold-cdn\tests\history_pyq_1990_2024'
CACHE_FILE = r'D:\Android Project\prepunfold-cdn\scripts\history_translation_cache.json'
CONFIG_PATH = r'D:\Android Project\prepunfold-cdn\scripts\history_topics_config.json'

os.makedirs(OUTPUT_DIR, exist_ok=True)

trans_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            trans_cache = json.load(f)
    except:
        trans_cache = {}

# Also load existing entries from polity cache if available
POLITY_CACHE = r'D:\Android Project\prepunfold-cdn\scripts\translation_cache.json'
if os.path.exists(POLITY_CACHE):
    try:
        with open(POLITY_CACHE, 'r', encoding='utf-8') as f:
            p_cache = json.load(f)
            for k, v in p_cache.items():
                if k not in trans_cache:
                    trans_cache[k] = v
    except:
        pass

def is_hindi(text):
    if not text:
        return False
    return bool(re.search(r'[\u0900-\u097F]', text))

def translate_batch(texts, max_workers=8):
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

def slugify(text):
    s = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    s = re.sub(r'\s+', '_', s).strip('_')
    return s[:40]

def process_history():
    doc = pymupdf.open(PDF_PATH)
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)

    part_meta = [
        ("ancient", "part1_ancient_history", "Part I: Ancient History of India", "भाग I: प्राचीन भारत का इतिहास", "anc"),
        ("medieval", "part2_medieval_history", "Part II: Medieval History of India", "भाग II: मध्यकालीन भारत का इतिहास", "med"),
        ("modern", "part3_modern_history", "Part III: Modern History of India", "भाग III: आधुनिक भारत का इतिहास", "mod")
    ]

    total_generated = 0

    for key, part_id, part_title_en, part_title_hi, part_code in part_meta:
        chapters = config[key]
        print(f"\n=== Processing {part_title_en} ({len(chapters)} chapters) ===")

        for ch_num, title_en, title_hi, start_p, end_p in chapters:
            slug = f"hist_pyq_{part_code}_t{ch_num:02d}_{slugify(title_en)}"
            out_file = os.path.join(OUTPUT_DIR, f"{slug}.json")

            if os.path.exists(out_file):
                try:
                    with open(out_file, 'r', encoding='utf-8') as f:
                        existing = json.load(f)
                    qs = existing.get("questions", [])
                    if len(qs) > 0 and any(is_hindi(q.get("questionTextHi", "")) for q in qs[:min(5, len(qs))]):
                        print(f"Skipping already generated with Hindi: {slug} ({len(qs)} Qs)")
                        total_generated += 1
                        continue
                except:
                    pass

            p_start = max(0, start_p - 1)
            p_end = min(len(doc), end_p)

            lines = []
            for p in range(p_start, p_end):
                for line in doc[p].get_text().split('\n'):
                    s = line.strip()
                    if s.startswith('https://t.me') or s.startswith('B–') or s == 'General Studies' or s == 'Indian History':
                        continue
                    lines.append(line)
            full_text = '\n'.join(lines)

            # Find sequential questions
            expected = 1
            pos = 0
            found_qs = []
            while True:
                m = re.search(r'\n\s*' + str(expected) + r'\s*\.\s+', full_text[pos:])
                if not m:
                    break
                q_start = pos + m.start()
                found_qs.append((expected, q_start))
                pos = q_start + len(m.group())
                expected += 1

            raw_questions = []
            for i in range(len(found_qs)):
                num, start = found_qs[i]
                end = found_qs[i+1][1] if i + 1 < len(found_qs) else len(full_text)
                block = full_text[start:end]
                clean = re.sub(r'^\n?\s*' + str(num) + r'\s*\.\s*', '', block).strip()

                m_ans = re.search(r'\nAns\.\s*\(([a-eA-E\*&, ]+)\)', clean)
                if not m_ans:
                    continue
                ans_str = m_ans.group(1).upper()
                m_first_letter = re.search(r'[A-E]', ans_str)
                correct_opt = m_first_letter.group(0) if m_first_letter else 'A'

                pre_ans = clean[:m_ans.start()].strip()
                explanation = clean[m_ans.end():].strip()

                # Match lowercase options (a), (b), (c), (d)
                opt_matches = list(re.finditer(r'(?:^|\n|\s)\(([a-d])\)\s*', pre_ans))
                filtered_opts = []
                expected_letter = 'a'
                for m in opt_matches:
                    if m.group(1).lower() == expected_letter:
                        filtered_opts.append(m)
                        expected_letter = chr(ord(expected_letter) + 1)
                        if expected_letter > 'd':
                            break

                if len(filtered_opts) == 4:
                    q_text = pre_ans[:filtered_opts[0].start()].strip()
                    options = []
                    for j in range(4):
                        opt_s = filtered_opts[j].end()
                        opt_e = filtered_opts[j+1].start() if j + 1 < 4 else len(pre_ans)
                        options.append(pre_ans[opt_s:opt_e].strip())

                    d_lines = options[3].split('\n')
                    exam_tag = ""
                    actual_d_lines = []
                    for l in d_lines:
                        ls = l.strip()
                        if re.search(r'(P\.C\.S|I\.A\.S|U\.P|M\.P|R\.O|A\.R\.O|B\.P|R\.A\.S|Uttarakhand|Jharkhand|Chhattisgarh|PSC|Pre|Mains|\b\d{4}\b)', ls) and len(actual_d_lines) > 0:
                            exam_tag = (exam_tag + " " + ls).strip()
                        else:
                            actual_d_lines.append(l)
                    options[3] = '\n'.join(actual_d_lines).strip()
                    options = [re.sub(r'\s+', ' ', o).strip() for o in options]
                else:
                    q_text = pre_ans
                    options = ["Option A", "Option B", "Option C", "Option D"]
                    exam_tag = ""

                q_text = re.sub(r'\s+', ' ', q_text).strip()
                explanation = re.sub(r'\s+', ' ', explanation).strip()
                m_yr = re.search(r'\b(19\d\d|20\d\d)\b', exam_tag)
                exam_year = int(m_yr.group(1)) if m_yr else 2024

                raw_questions.append({
                    "num": num,
                    "q_text": q_text,
                    "options": options,
                    "correct_opt": correct_opt,
                    "exam_tag": exam_tag if exam_tag else "State PSC & UPSC PYQ",
                    "exam_year": exam_year,
                    "explanation": explanation
                })

            print(f"Extracted {len(raw_questions)} questions for {slug}")

            # Batch translate
            all_q_texts = [q["q_text"] for q in raw_questions]
            all_explanations = [q["explanation"] for q in raw_questions]
            all_opt_texts = []
            for q in raw_questions:
                all_opt_texts.extend(q["options"])

            trans_q_texts = translate_batch(all_q_texts)
            trans_explanations = translate_batch(all_explanations)
            trans_opt_texts = translate_batch(all_opt_texts)

            subtopic_id = f"sub_01_{slugify(title_en)}"
            subtopic_title_en = f"(i) {title_en}"
            subtopic_title_hi = f"(i) {title_hi}"

            formatted_questions = []
            opt_idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}

            for i, q in enumerate(raw_questions):
                q_num = q["num"]
                opts_en = q["options"]
                opts_hi = trans_opt_texts[i*4 : (i+1)*4]
                corr_letter = q["correct_opt"]
                corr_idx = opt_idx_map.get(corr_letter, 0)

                q_obj = {
                    "questionId": f"{slug}_q{q_num:03d}",
                    "questionNumber": q_num,
                    "sectionId": subtopic_id,
                    "sectionTitleEn": f"{title_en} — {subtopic_title_en}",
                    "sectionTitleHi": f"{title_hi} — {subtopic_title_hi}",
                    "subtopicId": subtopic_id,
                    "subtopicTitleEn": subtopic_title_en,
                    "subtopicTitleHi": subtopic_title_hi,
                    "questionType": "MCQ",
                    "positiveMarks": 2.0,
                    "negativeMarks": 0.66,
                    "pyqTag": q["exam_tag"],
                    "examYear": q["exam_year"],
                    "topicTag": f"Indian History: {title_en}",
                    "difficulty": "MEDIUM",
                    "questionTextEn": q["q_text"],
                    "questionTextHi": trans_q_texts[i],
                    "optionsEn": opts_en,
                    "optionsHi": opts_hi,
                    "correctOption": corr_letter,
                    "correctOptionsList": None,
                    "natMin": None,
                    "natMax": None,
                    "explanationEn": f"Correct Answer: ({corr_letter}). {q['explanation']}",
                    "explanationHi": f"सही उत्तर: ({corr_letter}) {trans_explanations[i]}",
                    "q_id": 900000 + (1 if part_code=='anc' else 2 if part_code=='med' else 3) * 10000 + ch_num * 100 + q_num,
                    "q_number": q_num,
                    "section": f"{title_en} — {subtopic_title_en}",
                    "exam_year_tag": q["exam_tag"],
                    "question_en": q["q_text"],
                    "question_hi": trans_q_texts[i],
                    "options_en": opts_en,
                    "options_hi": opts_hi,
                    "correct_index": corr_idx,
                    "correct_indices": [corr_idx],
                    "explanation_en": f"Correct Answer: ({corr_letter}). {q['explanation']}",
                    "explanation_hi": f"सही उत्तर: ({corr_letter}) {trans_explanations[i]}"
                }
                formatted_questions.append(q_obj)

            total_q = len(formatted_questions)
            doc_json = {
                "testId": slug,
                "categoryId": "history_pyq_1990_2024",
                "partId": part_id,
                "partTitleEn": part_title_en,
                "partTitleHi": part_title_hi,
                "topicNumber": ch_num,
                "topicTitleEn": f"{ch_num}. {title_en}",
                "topicTitleHi": f"{ch_num}. {title_hi}",
                "subtopics": [
                    {
                        "subtopicId": subtopic_id,
                        "subtopicTitleEn": subtopic_title_en,
                        "subtopicTitleHi": subtopic_title_hi,
                        "questionCount": total_q
                    }
                ],
                "titleEn": f"Indian History Topic {ch_num}: {title_en} ({total_q} PYQs)",
                "titleHi": f"भारतीय इतिहास अध्याय {ch_num}: {title_hi} ({total_q} विगत वर्ष प्रश्न)",
                "subtitleEn": f"Part: {part_title_en}",
                "testType": "TOPIC",
                "isFree": True,
                "durationMinutes": total_q,
                "totalQuestions": total_q,
                "maxMarks": total_q * 2.0,
                "positiveMarks": 2.0,
                "negativeMarks": 0.66,
                "examYear": 2024,
                "shiftBadge": f"PYQ (1990–2023) • {part_title_en.split(':')[0]}",
                "questions": formatted_questions
            }

            with open(out_file, 'w', encoding='utf-8') as f:
                json.dump(doc_json, f, ensure_ascii=False, indent=2)

            total_generated += 1
            print(f"Generated {slug}: {total_q} Qs ({os.path.getsize(out_file)} bytes)")

    print(f"\n=== Completed History processing! Generated {total_generated} test files ===")

if __name__ == "__main__":
    process_history()
