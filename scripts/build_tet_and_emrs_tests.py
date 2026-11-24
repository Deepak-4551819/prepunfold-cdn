# -*- coding: utf-8 -*-
import os
import json

CTET_SOURCE = r"C:\Users\yedde\Downloads\ctet_all_state_tet_hindi_chapterwise.json"
EMRS_SOURCE = r"C:\Users\yedde\Downloads\emrs_special_general_hindi_chapterwise.json"

CTET_DIR = "tests/teaching/ctet_state_tet_hindi"
EMRS_DIR = "tests/teaching/emrs_general_hindi"

CTET_CHAPTER_CONFIG = [
    {
        "ch_id": 1,
        "slug": "ch01_varnamala",
        "name_hi": "हिन्दी वर्णमाला",
        "name_en": "Hindi Alphabet & Phonetics (वर्णमाला)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 2,
        "slug": "ch02_vakya_rachana_shuddhi",
        "name_hi": "वाक्य रचना, विराम चिह्न एवं वर्तनी शुद्धि",
        "name_en": "Sentence Syntax, Punctuation & Spellings (वाक्य रचना एवं वर्तनी शुद्धि)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 3,
        "slug": "ch03_shabd_bhed_vilom_paryay",
        "name_hi": "विलोम, पर्यायवाची, एकार्थक-अनेकार्थक, तद्भव-तत्सम, देशज-विदेशज, वाक्यांश के लिए एक शब्द",
        "name_en": "Vocabulary, Antonyms, Synonyms & Word Etymology (शब्द संपदा)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 4,
        "slug": "ch04_sangya_sarvanam_kriya_visheshana",
        "name_hi": "संज्ञा, सर्वनाम, क्रिया, विशेषण तथा उनके भेद, अव्यय",
        "name_en": "Parts of Speech: Noun, Pronoun, Verb, Adjective & Indeclinable",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 5,
        "slug": "ch05_ling_vachan_karak_kaal_vachya",
        "name_hi": "लिंग, वचन, कारक, काल, वाच्य",
        "name_en": "Gender, Number, Case, Tense & Voice (लिंग, वचन, कारक, काल, वाच्य)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 6,
        "slug": "ch06_upsarg_pratyay",
        "name_hi": "उपसर्ग-प्रत्यय",
        "name_en": "Prefixes & Suffixes (उपसर्ग एवं प्रत्यय)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 7,
        "slug": "ch07_sandhi_samas",
        "name_hi": "संधि-समास",
        "name_en": "Sandhi & Compound Words (संधि एवं समास)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 8,
        "slug": "ch08_lokokti_muhavare",
        "name_hi": "लोकोक्ति एवं मुहावरे",
        "name_en": "Idioms & Proverbs (लोकोक्ति एवं मुहावरे)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 9,
        "slug": "ch09_ras_chhand_alankar",
        "name_hi": "रस, छन्द, अलंकार तथा उसके भेद",
        "name_en": "Poetics: Ras, Chhand & Alankar (रस, छन्द एवं अलंकार)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 10,
        "slug": "ch10_kavi_lekhak_rachnaye",
        "name_hi": "कवियों एवं लेखकों की रचनाएँ",
        "name_en": "Poets, Writers & Literary Works (कवि एवं रचनाएं)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 11,
        "slug": "ch11_hindi_vividh",
        "name_hi": "हिन्दी विविध प्रश्न",
        "name_en": "Miscellaneous Hindi Questions (हिन्दी विविध)",
        "part_id": "hindi_grammar_literature"
    },
    {
        "ch_id": 12,
        "slug": "ch12_bhasha_adhigam_arjan",
        "name_hi": "भाषा अधिगम और अर्जन",
        "name_en": "Language Learning & Acquisition (भाषा अधिगम और अर्जन)",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 13,
        "slug": "ch13_bhasha_adhyapan_siddhant",
        "name_hi": "भाषा अध्यापन के सिद्धान्त",
        "name_en": "Principles of Language Teaching (भाषा शिक्षण के सिद्धान्त)",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 14,
        "slug": "ch14_bhasha_karya_sunna_bolna",
        "name_hi": "भाषा का कार्य (सुनने और बोलने की भूमिका)",
        "name_en": "Role of Listening & Speaking in Language Functions",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 15,
        "slug": "ch15_vichar_sampreshan",
        "name_hi": "विचारों का सम्प्रेषण (मौखिक और लिखित)",
        "name_en": "Communication of Ideas: Oral & Written (विचार सम्प्रेषण)",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 16,
        "slug": "ch16_bhasha_kaushal",
        "name_hi": "भाषा कौशल (बोलना, सुनना, पढ़ना और लिखना)",
        "name_en": "Language Skills: LSRW (सुनना, बोलना, पढ़ना, लिखना)",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 17,
        "slug": "ch17_bodhgamayata_mulyankan",
        "name_hi": "भाषा बोधगम्यता एवं मूल्यांकन",
        "name_en": "Language Comprehension & Evaluation (बोधगम्यता एवं मूल्यांकन)",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 18,
        "slug": "ch18_adhyapan_adhigam_samagri",
        "name_hi": "अध्यापन अधिगम सामग्रियां",
        "name_en": "Teaching-Learning Materials & TLM (अध्यापन अधिगम सामग्री)",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 19,
        "slug": "ch19_upcharatmak_adhyapan",
        "name_hi": "उपचारात्मक अध्यापन",
        "name_en": "Remedial Teaching (उपचारात्मक शिक्षण)",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 20,
        "slug": "ch20_bhasha_shikshan_vividh",
        "name_hi": "भाषा शिक्षण के विविध प्रश्न",
        "name_en": "Miscellaneous Pedagogy & Teaching Practice (शिक्षण विविध)",
        "part_id": "hindi_pedagogy"
    },
    {
        "ch_id": 21,
        "slug": "ch21_apatith_anuchhed",
        "name_hi": "अपठित अनुच्छेद",
        "name_en": "Unseen Passages & Reading Comprehension (अपठित अनुच्छेद)",
        "part_id": "reading_comprehension"
    }
]

EMRS_CHAPTER_CONFIG = [
    {"ch_id": 1, "slug": "ch01_varnamala", "name_hi": "वर्णमाला", "name_en": "Varnamala & Phonetics (वर्णमाला)", "part_id": "emrs_grammar"},
    {"ch_id": 2, "slug": "ch02_vartani_vakya_shuddhi", "name_hi": "वर्तनी एवं वाक्य शुद्धि", "name_en": "Spelling & Sentence Correction (वर्तनी एवं वाक्य शुद्धि)", "part_id": "emrs_grammar"},
    {"ch_id": 3, "slug": "ch03_sangya", "name_hi": "संज्ञा", "name_en": "Noun (संज्ञा)", "part_id": "emrs_grammar"},
    {"ch_id": 4, "slug": "ch04_sarvanam", "name_hi": "सर्वनाम", "name_en": "Pronoun (सर्वनाम)", "part_id": "emrs_grammar"},
    {"ch_id": 5, "slug": "ch05_visheshana", "name_hi": "विशेषण", "name_en": "Adjective (विशेषण)", "part_id": "emrs_grammar"},
    {"ch_id": 6, "slug": "ch06_kriya", "name_hi": "क्रिया", "name_en": "Verb (क्रिया)", "part_id": "emrs_grammar"},
    {"ch_id": 7, "slug": "ch07_ling_vachan", "name_hi": "लिंग तथा वचन", "name_en": "Gender & Number (लिंग तथा वचन)", "part_id": "emrs_grammar"},
    {"ch_id": 8, "slug": "ch08_kaal_vachya", "name_hi": "काल एवं वाच्य", "name_en": "Tense & Voice (काल एवं वाच्य)", "part_id": "emrs_grammar"},
    {"ch_id": 9, "slug": "ch09_karak", "name_hi": "कारक", "name_en": "Case & Prepositions (कारक)", "part_id": "emrs_grammar"},
    {"ch_id": 10, "slug": "ch10_tadbhava_tatsam_utpatti", "name_hi": "तद्भव एवं तत्सम शब्द तथा शब्दों की उत्पत्ति", "name_en": "Tatsam, Tadbhava & Word Origins", "part_id": "emrs_vocab"},
    {"ch_id": 11, "slug": "ch11_upsarg_pratyay", "name_hi": "उपसर्ग तथा प्रत्यय", "name_en": "Prefix & Suffix (उपसर्ग तथा प्रत्यय)", "part_id": "emrs_vocab"},
    {"ch_id": 12, "slug": "ch12_vilom_shabd", "name_hi": "विलोम शब्द", "name_en": "Antonyms (विलोम शब्द)", "part_id": "emrs_vocab"},
    {"ch_id": 13, "slug": "ch13_paryayvachi_samanarthi", "name_hi": "पर्यायवाची शब्द/समानार्थी", "name_en": "Synonyms (पर्यायवाची शब्द)", "part_id": "emrs_vocab"},
    {"ch_id": 14, "slug": "ch14_vakyansh_ek_shabd", "name_hi": "वाक्यांश के लिए एक शब्द", "name_en": "One Word Substitution (वाक्यांश के लिए एक शब्द)", "part_id": "emrs_vocab"},
    {"ch_id": 15, "slug": "ch15_rikt_sthan", "name_hi": "रिक्त स्थान", "name_en": "Fill in the Blanks (रिक्त स्थान पूर्ति)", "part_id": "emrs_vocab"},
    {"ch_id": 16, "slug": "ch16_vakya_rachana_bhed", "name_hi": "वाक्य रचना एवं वाक्य भेद", "name_en": "Sentence Structure & Types (वाक्य रचना)", "part_id": "emrs_grammar"},
    {"ch_id": 17, "slug": "ch17_sandhi", "name_hi": "संधि", "name_en": "Sandhi (संधि)", "part_id": "emrs_grammar"},
    {"ch_id": 18, "slug": "ch18_samas", "name_hi": "समास", "name_en": "Samas / Compound Words (समास)", "part_id": "emrs_grammar"},
    {"ch_id": 19, "slug": "ch19_vyavasthit_vakya_kram", "name_hi": "व्यवस्थित वाक्य क्रम", "name_en": "Sentence Para Jumbles (वाक्य क्रम व्यवस्था)", "part_id": "emrs_grammar"},
    {"ch_id": 20, "slug": "ch20_ras_chhand_alankar", "name_hi": "रस, छन्द एवं अलंकार", "name_en": "Poetics: Ras, Chhand & Alankar (रस, छन्द, अलंकार)", "part_id": "emrs_literature_comprehension"},
    {"ch_id": 21, "slug": "ch21_muhavare_lokoktiya", "name_hi": "मुहावरें एवं लोकोक्तियां", "name_en": "Idioms & Proverbs (मुहावरे एवं लोकोक्तियां)", "part_id": "emrs_vocab"},
    {"ch_id": 22, "slug": "ch22_apatith_gadyansh", "name_hi": "अपठित गद्यांश और प्रश्नोत्तर", "name_en": "Unseen Passage & Comprehension (अपठित गद्यांश)", "part_id": "emrs_literature_comprehension"},
    {"ch_id": 23, "slug": "ch23_hindi_bhasha_sahitya", "name_hi": "हिन्दी भाषा व साहित्य", "name_en": "Hindi Language & Literature (भाषा व साहित्य)", "part_id": "emrs_literature_comprehension"},
    {"ch_id": 24, "slug": "ch24_rachna_rachnakar", "name_hi": "रचना एवं रचनाकार", "name_en": "Authors & Literary Works (रचना एवं रचनाकार)", "part_id": "emrs_literature_comprehension"},
    {"ch_id": 25, "slug": "ch25_vividh", "name_hi": "विविध", "name_en": "Miscellaneous Solved Questions (विविध)", "part_id": "emrs_literature_comprehension"}
]

def build_test_papers():
    os.makedirs(CTET_DIR, exist_ok=True)
    os.makedirs(EMRS_DIR, exist_ok=True)

    # 1. Process CTET & All State TET
    print("Loading CTET source JSON...")
    with open(CTET_SOURCE, 'r', encoding='utf-8') as f:
        ctet_data = json.load(f)

    ctet_tests_meta = []
    ctet_ch_dict = {ch['chapter_id']: ch for ch in ctet_data.get('chapters', [])}
    q_id_counter = 800000

    for cfg in CTET_CHAPTER_CONFIG:
        ch_id = cfg['ch_id']
        ch = ctet_ch_dict.get(ch_id)
        if not ch:
            print(f"Warning: CTET Chapter {ch_id} not found!")
            continue

        raw_qs = ch.get('questions', [])
        total_q = len(raw_qs)
        test_id = f"ctet_tet_hindi_{cfg['slug']}"
        file_name = f"{test_id}.json"
        rel_path = f"{CTET_DIR}/{file_name}".replace("\\", "/")
        is_free = (ch_id == 1)

        questions = []
        for q_num, q in enumerate(raw_qs, 1):
            q_id_counter += 1
            correct_opt = (q.get('answer') or 'A').strip().upper()
            if correct_opt not in ['A', 'B', 'C', 'D']:
                correct_opt = 'A'
            correct_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[correct_opt]

            opts_dict = q.get('options', {})
            opts_list = [
                str(opts_dict.get('a', '')).strip(),
                str(opts_dict.get('b', '')).strip(),
                str(opts_dict.get('c', '')).strip(),
                str(opts_dict.get('d', '')).strip()
            ]

            q_text = str(q.get('question', '')).strip()
            exp_text = str(q.get('explanation', '')).strip()
            exam_tag = str(q.get('exam', '')).strip() if q.get('exam') else "CTET / All State TET"

            q_obj = {
                "questionId": f"{test_id}_q{q_num:03d}",
                "questionNumber": q_num,
                "sectionId": cfg['part_id'],
                "sectionTitle": cfg['name_hi'],
                "sectionTitleEn": cfg['name_en'],
                "sectionTitleHi": cfg['name_hi'],
                "subtopicId": f"sub_{ch_id:02d}",
                "subtopicTitleEn": cfg['name_en'],
                "subtopicTitleHi": cfg['name_hi'],
                "questionType": "MCQ",
                "positiveMarks": 1.0,
                "negativeMarks": 0.0,
                "pyqTag": exam_tag,
                "examYear": 2024,
                "topicTag": f"CTET & State TET Hindi: {cfg['name_hi']}",
                "difficulty": "MEDIUM",
                "correctOption": correct_opt,
                "correctOptionsList": [correct_opt],
                "correct_index": correct_idx,
                "correct_indices": [correct_idx],
                "natMin": None,
                "natMax": None,
                "questionText": q_text,
                "questionTextEn": q_text,
                "questionTextHi": q_text,
                "options": opts_list,
                "optionsEn": opts_list,
                "optionsHi": opts_list,
                "explanation": exp_text,
                "explanationEn": exp_text,
                "explanationHi": exp_text,
                # snake_case fields
                "q_id": q_id_counter,
                "q_number": q_num,
                "section": cfg['name_hi'],
                "exam_year_tag": exam_tag,
                "question_en": q_text,
                "question_hi": q_text,
                "options_en": opts_list,
                "options_hi": opts_list,
                "answer": correct_opt.lower(),
                "explanation_en": exp_text,
                "explanation_hi": exp_text
            }
            questions.append(q_obj)

        duration = min(180, max(30, total_q))

        paper_data = {
            "testId": test_id,
            "categoryId": "ctet_state_tet_hindi",
            "test_id": test_id,
            "category_id": "ctet_state_tet_hindi",
            "title": f"CTET & State TET Hindi — Ch {ch_id:02d}: {cfg['name_en']}",
            "titleEn": f"CTET & State TET Hindi — Ch {ch_id:02d}: {cfg['name_en']}",
            "titleHi": f"सीटीईटी एवं राज्य टीईटी हिन्दी — अध्याय {ch_id:02d}: {cfg['name_hi']}",
            "testType": "TOPIC",
            "test_type": "TOPIC",
            "isFree": is_free,
            "is_free": is_free,
            "durationMinutes": duration,
            "duration_minutes": duration,
            "totalQuestions": total_q,
            "total_questions": total_q,
            "maxMarks": float(total_q),
            "positiveMarks": 1.0,
            "negativeMarks": 0.0,
            "examYear": 2024,
            "shiftBadge": f"Chapter Test • {total_q} Solved MCQs",
            "path": rel_path,
            "filePath": rel_path,
            "file_path": rel_path,
            "part_id": cfg['part_id'],
            "partId": cfg['part_id'],
            "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
            "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
            "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/{rel_path}",
            "questions": questions
        }

        with open(rel_path, 'w', encoding='utf-8') as out_f:
            json.dump(paper_data, out_f, ensure_ascii=False, indent=2)

        # Meta for manifest
        meta = {k: v for k, v in paper_data.items() if k != 'questions'}
        ctet_tests_meta.append(meta)

    print(f"Generated {len(ctet_tests_meta)} tests for CTET & State TET Hindi.")

    # 2. Process EMRS Special General Hindi
    print("Loading EMRS source JSON...")
    with open(EMRS_SOURCE, 'r', encoding='utf-8') as f:
        emrs_data = json.load(f)

    emrs_tests_meta = []
    emrs_ch_dict = {ch['chapter_id']: ch for ch in emrs_data.get('chapters', [])}

    for cfg in EMRS_CHAPTER_CONFIG:
        ch_id = cfg['ch_id']
        ch = emrs_ch_dict.get(ch_id)
        if not ch:
            print(f"Warning: EMRS Chapter {ch_id} not found!")
            continue

        raw_qs = ch.get('questions', [])
        total_q = len(raw_qs)
        test_id = f"emrs_hindi_{cfg['slug']}"
        file_name = f"{test_id}.json"
        rel_path = f"{EMRS_DIR}/{file_name}".replace("\\", "/")
        is_free = (ch_id == 1)

        questions = []
        for q_num, q in enumerate(raw_qs, 1):
            q_id_counter += 1
            correct_opt = (q.get('answer') or 'A').strip().upper()
            if correct_opt not in ['A', 'B', 'C', 'D']:
                correct_opt = 'A'
            correct_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[correct_opt]

            opts_dict = q.get('options', {})
            opts_list = [
                str(opts_dict.get('a', '')).strip(),
                str(opts_dict.get('b', '')).strip(),
                str(opts_dict.get('c', '')).strip(),
                str(opts_dict.get('d', '')).strip()
            ]

            q_text = str(q.get('question', '')).strip()
            exp_text = str(q.get('explanation', '')).strip()
            exam_tag = str(q.get('exam', '')).strip() if q.get('exam') else "EMRS / Central Schools"

            q_obj = {
                "questionId": f"{test_id}_q{q_num:03d}",
                "questionNumber": q_num,
                "sectionId": cfg['part_id'],
                "sectionTitle": cfg['name_hi'],
                "sectionTitleEn": cfg['name_en'],
                "sectionTitleHi": cfg['name_hi'],
                "subtopicId": f"sub_{ch_id:02d}",
                "subtopicTitleEn": cfg['name_en'],
                "subtopicTitleHi": cfg['name_hi'],
                "questionType": "MCQ",
                "positiveMarks": 1.0,
                "negativeMarks": 0.0,
                "pyqTag": exam_tag,
                "examYear": 2024,
                "topicTag": f"EMRS General Hindi: {cfg['name_hi']}",
                "difficulty": "MEDIUM",
                "correctOption": correct_opt,
                "correctOptionsList": [correct_opt],
                "correct_index": correct_idx,
                "correct_indices": [correct_idx],
                "natMin": None,
                "natMax": None,
                "questionText": q_text,
                "questionTextEn": q_text,
                "questionTextHi": q_text,
                "options": opts_list,
                "optionsEn": opts_list,
                "optionsHi": opts_list,
                "explanation": exp_text,
                "explanationEn": exp_text,
                "explanationHi": exp_text,
                # snake_case fields
                "q_id": q_id_counter,
                "q_number": q_num,
                "section": cfg['name_hi'],
                "exam_year_tag": exam_tag,
                "question_en": q_text,
                "question_hi": q_text,
                "options_en": opts_list,
                "options_hi": opts_list,
                "answer": correct_opt.lower(),
                "explanation_en": exp_text,
                "explanation_hi": exp_text
            }
            questions.append(q_obj)

        duration = min(180, max(30, total_q))

        paper_data = {
            "testId": test_id,
            "categoryId": "emrs_general_hindi",
            "test_id": test_id,
            "category_id": "emrs_general_hindi",
            "title": f"EMRS General Hindi — Ch {ch_id:02d}: {cfg['name_en']}",
            "titleEn": f"EMRS General Hindi — Ch {ch_id:02d}: {cfg['name_en']}",
            "titleHi": f"ईएमआरएस सामान्य हिन्दी — अध्याय {ch_id:02d}: {cfg['name_hi']}",
            "testType": "TOPIC",
            "test_type": "TOPIC",
            "isFree": is_free,
            "is_free": is_free,
            "durationMinutes": duration,
            "duration_minutes": duration,
            "totalQuestions": total_q,
            "total_questions": total_q,
            "maxMarks": float(total_q),
            "positiveMarks": 1.0,
            "negativeMarks": 0.0,
            "examYear": 2024,
            "shiftBadge": f"Chapter Test • {total_q} Solved MCQs",
            "path": rel_path,
            "filePath": rel_path,
            "file_path": rel_path,
            "part_id": cfg['part_id'],
            "partId": cfg['part_id'],
            "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
            "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
            "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/{rel_path}",
            "questions": questions
        }

        with open(rel_path, 'w', encoding='utf-8') as out_f:
            json.dump(paper_data, out_f, ensure_ascii=False, indent=2)

        meta = {k: v for k, v in paper_data.items() if k != 'questions'}
        emrs_tests_meta.append(meta)

    print(f"Generated {len(emrs_tests_meta)} tests for EMRS Special General Hindi.")

    # Save metadata lists for manifest updater
    with open("scripts/ctet_tests_meta.json", "w", encoding="utf-8") as f:
        json.dump(ctet_tests_meta, f, ensure_ascii=False, indent=2)
    with open("scripts/emrs_tests_meta.json", "w", encoding="utf-8") as f:
        json.dump(emrs_tests_meta, f, ensure_ascii=False, indent=2)

    print("All test files generated successfully!")

if __name__ == "__main__":
    build_test_papers()
