import json, os, re
from collections import defaultdict

MASTER_JSON = "scripts/extracted_tgt_pgt_geography_master.json"
PYQ_DIR = "tests/teaching/tgt_pgt_geography/pyq"
MOCK_DIR = "tests/teaching/tgt_pgt_geography/mock_tests"

os.makedirs(PYQ_DIR, exist_ok=True)
os.makedirs(MOCK_DIR, exist_ok=True)

with open(MASTER_JSON, "r", encoding="utf-8") as f:
    master_qs = json.load(f)

print(f"Loaded {len(master_qs)} Geography master questions.")

used_indices = set()

# 20 Official Geography PYQ Papers
GEO_PYQ_DEFS = [
    (
        "tgt_pgt_geo_pyq_up_pgt_2021",
        "UP PGT Geography 2021 — Official Solved Paper",
        "यूपी पीजीटी भूगोल 2021 — आधिकारिक हल प्रश्न-पत्र",
        2021,
        "UP PGT 2021 • Geography Official",
        r"UP\s+PGT.*2021",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_geo_pyq_up_pgt_2016",
        "UP PGT Geography 2016 — Official Solved Paper",
        "यूपी पीजीटी भूगोल 2016 — आधिकारिक हल प्रश्न-पत्र",
        2016,
        "UP PGT 2016 • Geography Official",
        r"UP\s+PGT.*2016",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_geo_pyq_up_pgt_2013",
        "UP PGT Geography 2013 — Official Solved Paper",
        "यूपी पीजीटी भूगोल 2013 — आधिकारिक हल प्रश्न-पत्र",
        2013,
        "UP PGT 2013 • Geography Official",
        r"UP\s+PGT.*2013",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_geo_pyq_up_pgt_2011",
        "UP PGT Geography 2011 — Official Solved Paper",
        "यूपी पीजीटी भूगोल 2011 — आधिकारिक हल प्रश्न-पत्र",
        2011,
        "UP PGT 2011 • Geography Official",
        r"UP\s+PGT.*2011",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_geo_pyq_up_pgt_2010",
        "UP PGT Geography 2010 — Official Solved Paper",
        "यूपी पीजीटी भूगोल 2010 — आधिकारिक हल प्रश्न-पत्र",
        2010,
        "UP PGT 2010 • Geography Official",
        r"UP\s+PGT.*2010",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_geo_pyq_up_pgt_2004",
        "UP PGT Geography 2004 — Official Solved Paper",
        "यूपी पीजीटी भूगोल 2004 — आधिकारिक हल प्रश्न-पत्र",
        2004,
        "UP PGT 2004 • Geography Official",
        r"UP\s+PGT.*2004",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_geo_pyq_up_tgt_2021",
        "UP TGT Geography 2021 — Official Solved Paper",
        "यूपी टीजीटी भूगोल 2021 — आधिकारिक हल प्रश्न-पत्र",
        2021,
        "UP TGT 2021 • Geography Official",
        r"UP\s+TGT.*2021",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_geo_pyq_up_tgt_2016",
        "UP TGT Geography 2016 — Official Solved Paper",
        "यूपी टीजीटी भूगोल 2016 — आधिकारिक हल प्रश्न-पत्र",
        2016,
        "UP TGT 2016 • Geography Official",
        r"UP\s+TGT.*2016",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_geo_pyq_up_tgt_2013",
        "UP TGT Geography 2013 — Official Solved Paper",
        "यूपी टीजीटी भूगोल 2013 — आधिकारिक हल प्रश्न-पत्र",
        2013,
        "UP TGT 2013 • Geography Official",
        r"UP\s+TGT.*2013",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_geo_pyq_up_tgt_2011",
        "UP TGT Geography 2011 — Official Solved Paper",
        "यूपी टीजीटी भूगोल 2011 — आधिकारिक हल प्रश्न-पत्र",
        2011,
        "UP TGT 2011 • Geography Official",
        r"UP\s+TGT.*2011",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_geo_pyq_up_tgt_2010",
        "UP TGT Geography 2010 — Official Solved Paper",
        "यूपी टीजीटी भूगोल 2010 — आधिकारिक हल प्रश्न-पत्र",
        2010,
        "UP TGT 2010 • Geography Official",
        r"UP\s+TGT.*2010",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_geo_pyq_up_tgt_2009",
        "UP TGT Geography 2009 — Official Solved Paper",
        "यूपी टीजीटी भूगोल 2009 — आधिकारिक हल प्रश्न-पत्र",
        2009,
        "UP TGT 2009 • Geography Official",
        r"UP\s+TGT.*2009",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_geo_pyq_up_tgt_2004",
        "UP TGT Geography 2004 — Official Solved Paper",
        "यूपी टीजीटी भूगोल 2004 — आधिकारिक हल प्रश्न-पत्र",
        2004,
        "UP TGT 2004 • Geography Official",
        r"UP\s+TGT.*2004",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_geo_pyq_up_lt_grade_2018",
        "UP LT Grade Assistant Teacher Geography 2018 — Official Paper",
        "यूपी एलटी ग्रेड सहायक अध्यापक भूगोल 2018 — आधिकारिक हल प्रश्न-पत्र",
        2018,
        "UP LT Grade 2018 • Geography Official",
        r"LT.*2018",
        120, 1.0, 0.33, 100
    ),
    (
        "tgt_pgt_geo_pyq_uppsc_gic_gdc_2021",
        "UPPSC GIC / GDC Lecturer Geography 2021 — Official Paper",
        "यूपीपीएससी जीआईसी / जीडीसी प्रवक्ता भूगोल 2021 — आधिकारिक हल प्रश्न-पत्र",
        2021,
        "UPPSC GIC/GDC 2021 • Geography Official",
        r"GIC.*2021|GDC.*2021",
        120, 2.5, 0.83, 100
    ),
    (
        "tgt_pgt_geo_pyq_dsssb_pgt_2021",
        "DSSSB PGT Geography 2021 — Official Solved Paper",
        "DSSSB पीजीटी भूगोल 2021 — आधिकारिक हल प्रश्न-पत्र",
        2021,
        "DSSSB PGT 2021 • Geography Official",
        r"DSSSB.*2021|DSSSB\s+PGT\s+11/07/2021",
        120, 1.0, 0.25, 150
    ),
    (
        "tgt_pgt_geo_pyq_dsssb_pgt_2018",
        "DSSSB PGT Geography 2018 — Official Solved Paper",
        "DSSSB पीजीटी भूगोल 2018 — आधिकारिक हल प्रश्न-पत्र",
        2018,
        "DSSSB PGT 2018 • Geography Official",
        r"DSSSB.*2018",
        120, 1.0, 0.25, 150
    ),
    (
        "tgt_pgt_geo_pyq_ukpsc_lect_2020",
        "UKPSC Lecturer (Mains) Geography 2020 — Official Paper",
        "UKPSC प्रवक्ता (मुख्य परीक्षा) भूगोल 2020 — आधिकारिक प्रश्न-पत्र",
        2020,
        "UKPSC Lecturer 2020 • Geography Official",
        r"UKPSC.*Lecturer",
        120, 1.0, 0.25, 150
    ),
    (
        "tgt_pgt_geo_pyq_rpsc_pgt_2020",
        "RPSC School Lecturer (PGT) / College Geography 2020 — Official Paper",
        "RPSC प्राध्यापक (PGT) / कॉलेज भूगोल 2020 — आधिकारिक हल प्रश्न-पत्र",
        2020,
        "RPSC PGT 2020 • Geography Official",
        r"RPSC.*2020|RPSC.*Asst",
        120, 2.0, 0.66, 150
    ),
    (
        "tgt_pgt_geo_pyq_jssc_pgt_2018",
        "JSSC PGT / Jharkhand TGT Geography 2018 — Official Solved Paper",
        "जेएसएससी पीजीटी / झारखण्ड टीजीटी भूगोल 2018 — आधिकारिक हल प्रश्न-पत्र",
        2018,
        "JSSC PGT 2018 • Geography Official",
        r"Jharkhand|JSSC",
        120, 2.0, 0.0, 150
    )
]

def format_geo_question(q, q_num, test_id, pos_marks, neg_marks):
    corr = q["correctOption"]
    corr_idx = ord(corr) - ord("A") if corr in ["A", "B", "C", "D"] else 0
    return {
        "questionId": f"{test_id}_q{q_num:03d}",
        "questionNumber": q_num,
        "sectionId": "sec_geography",
        "sectionTitle": "Geography (भूगोल)",
        "questionType": "MCQ",
        "positiveMarks": pos_marks,
        "negativeMarks": neg_marks,
        "pyqTag": q.get("examTag", "TGT/PGT Geography Solved Papers"),
        "topicTag": q.get("chapterHi", q.get("chapterEn", "Geography")),
        "difficulty": "Medium",
        "correctOption": corr,
        "correctOptionsList": [corr],
        "correct_index": corr_idx,
        "correct_indices": [corr_idx],
        "natMin": None,
        "natMax": None,
        "questionText": q["questionText"],
        "questionTextHi": q["questionTextHi"],
        "questionTextEn": "",
        "options": q["options"],
        "optionsHi": q["optionsHi"],
        "optionsEn": [],
        "explanation": q["explanation"],
        "explanationHi": q["explanationHi"],
        "explanationEn": ""
    }

def build_test_json(test_id, title_en, title_hi, test_type, exam_year, shift_badge, duration_min, pos_marks, neg_marks, raw_qs):
    formatted_qs = []
    for i, q in enumerate(raw_qs, start=1):
        formatted_qs.append(format_geo_question(q, i, test_id, pos_marks, neg_marks))

    return {
        "testId": test_id,
        "categoryId": "tgt_pgt_geography",
        "test_id": test_id,
        "category_id": "tgt_pgt_geography",
        "title": title_en,
        "titleEn": title_en,
        "titleHi": title_hi,
        "testType": test_type,
        "test_type": test_type,
        "isFree": True,
        "is_free": True,
        "durationMinutes": duration_min,
        "duration_minutes": duration_min,
        "totalQuestions": len(formatted_qs),
        "total_questions": len(formatted_qs),
        "maxMarks": round(len(formatted_qs) * pos_marks, 2),
        "positiveMarks": pos_marks,
        "negativeMarks": neg_marks,
        "examYear": exam_year,
        "shiftBadge": shift_badge,
        "questions": formatted_qs
    }

created_pyqs = []
for item in GEO_PYQ_DEFS:
    test_id, title_en, title_hi, exam_year, shift_badge, tag_regex, duration_min, pos_marks, neg_marks, max_qs = item
    rgx = re.compile(tag_regex, re.IGNORECASE)

    matched = []
    for idx, q in enumerate(master_qs):
        if idx not in used_indices and rgx.search(q.get("examTag", "")):
            matched.append((idx, q))
            if len(matched) >= max_qs:
                break

    for idx, _ in matched:
        used_indices.add(idx)

    raw_qs = [q for _, q in matched]
    test_obj = build_test_json(test_id, title_en, title_hi, "PYQ", exam_year, shift_badge, duration_min, pos_marks, neg_marks, raw_qs)

    file_path = os.path.join(PYQ_DIR, f"{test_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_obj, f, ensure_ascii=False, indent=2)

    print(f"Created Geography PYQ Paper: {test_id} ({len(raw_qs)} questions) -> {file_path}")
    created_pyqs.append(test_obj)

print(f"\nTotal questions used in 20 Geography PYQ papers: {len(used_indices)}")
remaining_indices = [i for i in range(len(master_qs)) if i not in used_indices]
print(f"Remaining unused questions for Geography Mock Tests: {len(remaining_indices)}")

# 10 High-Yield Subject & Full-Length Geography Mock Tests (100 Qs each)
GEO_MOCK_DEFS = [
    (
        "tgt_pgt_geo_mock_01_geomorphology",
        "TGT/PGT Geography Mock 1 — Geomorphology & Lithosphere",
        "टीजीटी/पीजीटी भूगोल मॉक 1 — स्थलमण्डल एवं भू-आकृति विज्ञान",
        "Geomorphology • 100 Solved MCQs",
        ["Geomorphology & Lithosphere", "Physical Geography & Solar System"],
        100
    ),
    (
        "tgt_pgt_geo_mock_02_climatology",
        "TGT/PGT Geography Mock 2 — Climatology & Atmosphere",
        "टीजीटी/पीजीटी भूगोल मॉक 2 — वायुमण्डल एवं जलवायु विज्ञान",
        "Climatology • 100 Solved MCQs",
        ["Climatology & Atmosphere"],
        100
    ),
    (
        "tgt_pgt_geo_mock_03_oceanography",
        "TGT/PGT Geography Mock 3 — Oceanography & Hydrosphere",
        "टीजीटी/पीजीटी भूगोल मॉक 3 — जलमण्डल एवं समुद्र विज्ञान",
        "Oceanography • 100 Solved MCQs",
        ["Oceanography & Hydrosphere"],
        100
    ),
    (
        "tgt_pgt_geo_mock_04_biogeography",
        "TGT/PGT Geography Mock 4 — Biogeography, Ecosystem & Environment",
        "टीजीटी/पीजीटी भूगोल मॉक 4 — जैवमण्डल एवं पारिस्थितिकी तंत्र",
        "Biogeography • 100 Solved MCQs",
        ["Biogeography & Ecosystem"],
        100
    ),
    (
        "tgt_pgt_geo_mock_05_human_geography",
        "TGT/PGT Geography Mock 5 — Human Geography, Population & Settlement",
        "टीजीटी/पीजीटी भूगोल मॉक 5 — मानव भूगोल, जनसंख्या एवं अधिवास",
        "Human Geography • 100 Solved MCQs",
        ["Human Geography, Population & Settlement"],
        100
    ),
    (
        "tgt_pgt_geo_mock_06_economic_geography",
        "TGT/PGT Geography Mock 6 — Economic Geography, Agriculture & Resources",
        "टीजीटी/पीजीटी भूगोल मॉक 6 — आर्थिक भूगोल, कृषि एवं संसाधन",
        "Economic Geography • 100 Solved MCQs",
        ["Economic Geography & Resources"],
        100
    ),
    (
        "tgt_pgt_geo_mock_07_india_physical",
        "TGT/PGT Geography Mock 7 — Geography of India (Physical & Drainage)",
        "टीजीटी/पीजीटी भूगोल मॉक 7 — भारत का भूगोल (प्राकृतिक संरचना एवं अपवाह)",
        "Geography of India • 100 Solved MCQs",
        ["Geography of India"],
        100
    ),
    (
        "tgt_pgt_geo_mock_08_india_economic",
        "TGT/PGT Geography Mock 8 — Geography of India (Economic & Minerals)",
        "टीजीटी/पीजीटी भूगोल मॉक 8 — भारत का भूगोल (आर्थिक, खनिज एवं उद्योग)",
        "Geography of India • 100 Solved MCQs",
        ["Geography of India"],
        100
    ),
    (
        "tgt_pgt_geo_mock_09_full_length_1",
        "TGT/PGT Geography Mock 9 — Full-Length Grand Test 1",
        "टीजीटी/पीजीटी भूगोल मॉक 9 — संपूर्ण पाठ्यक्रम ग्रैंड टेस्ट 1",
        "Full Length Mock • 100 Solved MCQs",
        None,
        100
    ),
    (
        "tgt_pgt_geo_mock_10_full_length_2",
        "TGT/PGT Geography Mock 10 — Full-Length Grand Test 2",
        "टीजीटी/पीजीटी भूगोल मॉक 10 — संपूर्ण पाठ्यक्रम ग्रैंड टेस्ट 2",
        "Full Length Mock • 100 Solved MCQs",
        None,
        100
    )
]

created_mocks = []
for mock_item in GEO_MOCK_DEFS:
    test_id, title_en, title_hi, badge, target_chapters, q_count = mock_item

    selected = []
    for idx in remaining_indices:
        if idx not in used_indices:
            q = master_qs[idx]
            if target_chapters is None or q.get("chapterEn") in target_chapters:
                selected.append((idx, q))
                if len(selected) >= q_count:
                    break

    for idx, _ in selected:
        used_indices.add(idx)

    raw_qs = [q for _, q in selected]
    test_obj = build_test_json(test_id, title_en, title_hi, "MOCK", 2024, badge, 120, 1.0, 0.0, raw_qs)

    file_path = os.path.join(MOCK_DIR, f"{test_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_obj, f, ensure_ascii=False, indent=2)

    print(f"Created Geography Mock Test: {test_id} ({len(raw_qs)} questions) -> {file_path}")
    created_mocks.append(test_obj)

print(f"\nALL GEOGRAPHY PAPERS CREATED: {len(created_pyqs)} PYQs + {len(created_mocks)} Mocks!")
