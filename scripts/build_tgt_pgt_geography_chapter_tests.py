import json, os

MASTER_FILE = "scripts/extracted_tgt_pgt_geography_master.json"
OUT_DIR = "tests/teaching/tgt_pgt_geography/chapter_tests"
os.makedirs(OUT_DIR, exist_ok=True)

with open(MASTER_FILE, "r", encoding="utf-8") as f:
    master_qs = json.load(f)

print(f"Loaded {len(master_qs)} master Geography questions.")

CHAPTER_METADATA = [
    (1, "Geographical Thought & Nature of Geography", "भूगोल-अर्थ एवं विषय क्षेत्र", "geographical_thought", "Geographical Thought & Nature of Geography", 0, 100),
    (2, "Physical Geography & Solar System", "भौतिक भूगोल एवं सौर मण्डल", "physical_geography_solar_system", "Physical Geography & Solar System", 0, 100),
    (3, "Geomorphology & Lithosphere (Part 1)", "स्थलमण्डल एवं भू-आकृति विज्ञान (भाग 1)", "geomorphology_part1", "Geomorphology & Lithosphere", 0, 100),
    (4, "Geomorphology & Lithosphere (Part 2)", "स्थलमण्डल एवं भू-आकृति विज्ञान (भाग 2)", "geomorphology_part2", "Geomorphology & Lithosphere", 100, 200),
    (5, "Climatology & Atmosphere (Part 1)", "वायुमण्डल एवं जलवायु विज्ञान (भाग 1)", "climatology_part1", "Climatology & Atmosphere", 0, 100),
    (6, "Climatology & Atmosphere (Part 2)", "वायुमण्डल एवं जलवायु विज्ञान (भाग 2)", "climatology_part2", "Climatology & Atmosphere", 100, 200),
    (7, "Oceanography & Hydrosphere", "जलमण्डल एवं समुद्र विज्ञान", "oceanography_hydrosphere", "Oceanography & Hydrosphere", 0, 100),
    (8, "Biogeography & Ecosystem", "जैवमण्डल एवं पारिस्थितिकी", "biogeography_ecosystem", "Biogeography & Ecosystem", 0, 100),
    (9, "Human Geography & Settlement (Part 1)", "मानव भूगोल एवं अधिवास (भाग 1)", "human_geography_part1", "Human Geography, Population & Settlement", 0, 100),
    (10, "Human Geography & Population (Part 2)", "मानव भूगोल एवं जनसंख्या (भाग 2)", "human_geography_part2", "Human Geography, Population & Settlement", 100, 200),
    (11, "Economic Geography & Resources (Part 1)", "आर्थिक भूगोल एवं संसाधन (भाग 1)", "economic_geography_part1", "Economic Geography & Resources", 0, 100),
    (12, "Economic Geography & Trade (Part 2)", "आर्थिक भूगोल एवं व्यापार (भाग 2)", "economic_geography_part2", "Economic Geography & Resources", 100, 200),
    (13, "Geography of India — Physical", "भारत का भूगोल — भौतिक संरचना एवं अपवाह", "geography_india_physical", "Geography of India", 0, 100),
    (14, "Geography of India — Economic & Agriculture", "भारत का भूगोल — कृषि, खनिज एवं उद्योग", "geography_india_economic", "Geography of India", 100, 200),
    (15, "Miscellaneous Geography & Cartography", "विविध भूगोल एवं मानचित्रकला", "cartography_miscellaneous", "Miscellaneous Geography & Cartography", 0, 100),
]

qs_by_chapter = {
    "Geographical Thought & Nature of Geography": [],
    "Physical Geography & Solar System": [],
    "Geomorphology & Lithosphere": [],
    "Climatology & Atmosphere": [],
    "Oceanography & Hydrosphere": [],
    "Biogeography & Ecosystem": [],
    "Human Geography, Population & Settlement": [],
    "Economic Geography & Resources": [],
    "Geography of India": [],
    "Miscellaneous Geography & Cartography": []
}

for q in master_qs:
    ch = q.get("chapterEn", "").strip()
    if ch in qs_by_chapter:
        qs_by_chapter[ch].append(q)

built_tests = []

for ch_num, ch_en, ch_hi, slug, source_key, start_idx, end_idx in CHAPTER_METADATA:
    available_qs = qs_by_chapter.get(source_key, [])
    selected_qs = available_qs[start_idx:end_idx]
    if not selected_qs:
        selected_qs = available_qs[:100]

    total_q = len(selected_qs)
    test_id = f"tgt_pgt_geo_ch{ch_num:02d}_{slug}"

    questions_list = []
    for idx, q in enumerate(selected_qs, 1):
        corr_opt = q.get("correctOption", "A").strip().upper()
        if not corr_opt or corr_opt not in ("A", "B", "C", "D"):
            corr_opt = "A"
        corr_idx = ord(corr_opt) - ord('A')

        raw_opts = q.get("options", q.get("optionsHi", ["(A)", "(B)", "(C)", "(D)"]))
        while len(raw_opts) < 4:
            raw_opts.append(f"Option {chr(ord('A') + len(raw_opts))}")

        q_item = {
            "questionId": f"{test_id}_q{idx:03d}",
            "questionNumber": idx,
            "sectionId": "sec_geography",
            "sectionTitle": f"Chapter {ch_num:02d}: {ch_en}",
            "questionType": "MCQ",
            "positiveMarks": 1.0,
            "negativeMarks": 0.0,
            "pyqTag": q.get("examTag", f"TGT/PGT Geography Ch {ch_num:02d}"),
            "topicTag": ch_hi,
            "difficulty": "Medium",
            "correctOption": corr_opt,
            "correctOptionsList": [corr_opt],
            "correct_index": corr_idx,
            "correct_indices": [corr_idx],
            "natMin": None,
            "natMax": None,
            "questionText": q.get("questionText", q.get("questionTextHi", "")),
            "questionTextEn": q.get("questionTextEn", ""),
            "questionTextHi": q.get("questionTextHi", q.get("questionText", "")),
            "options": raw_opts[:4],
            "optionsEn": q.get("optionsEn", []),
            "optionsHi": raw_opts[:4],
            "explanation": q.get("explanation", q.get("explanationHi", "")),
            "explanationEn": q.get("explanationEn", ""),
            "explanationHi": q.get("explanationHi", q.get("explanation", ""))
        }
        questions_list.append(q_item)

    duration = 60 if total_q <= 50 else (90 if total_q <= 80 else 120)

    test_doc = {
        "testId": test_id,
        "categoryId": "tgt_pgt_geography",
        "test_id": test_id,
        "category_id": "tgt_pgt_geography",
        "title": f"Geography Chapter {ch_num:02d}: {ch_en}",
        "titleEn": f"Geography Chapter {ch_num:02d}: {ch_en}",
        "titleHi": f"भूगोल अध्याय {ch_num:02d}: {ch_hi}",
        "testType": "TOPIC",
        "test_type": "TOPIC",
        "isFree": True,
        "is_free": True,
        "durationMinutes": duration,
        "duration_minutes": duration,
        "totalQuestions": total_q,
        "total_questions": total_q,
        "maxMarks": float(total_q),
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "examYear": 2024,
        "shiftBadge": f"Chapter {ch_num:02d} • {total_q} Solved Qs",
        "path": f"tests/teaching/tgt_pgt_geography/chapter_tests/{test_id}.json",
        "questions": questions_list
    }

    out_path = os.path.join(OUT_DIR, f"{test_id}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(test_doc, f, ensure_ascii=False, indent=2)

    built_tests.append(test_doc)
    print(f"Created Geography Chapter Test {ch_num:02d}: {ch_en} ({total_q} Qs)")

print(f"\nSuccessfully built {len(built_tests)} Geography Chapter Tests!")
