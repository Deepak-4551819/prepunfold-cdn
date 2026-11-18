import json, os, re
from collections import defaultdict

MASTER_JSON = "scripts/extracted_tgt_pgt_economics_master.json"
PYQ_DIR = "tests/teaching/tgt_pgt_economics/pyq"
MOCK_DIR = "tests/teaching/tgt_pgt_economics/mock_tests"

os.makedirs(PYQ_DIR, exist_ok=True)
os.makedirs(MOCK_DIR, exist_ok=True)

with open(MASTER_JSON, "r", encoding="utf-8") as f:
    master_qs = json.load(f)

print(f"Loaded {len(master_qs)} master questions.")

# Track used question indices to prevent duplicate usage in mock tests
used_indices = set()

# Define the 20 Official PYQ definitions:
# (test_id, title_en, title_hi, exam_year, shift_badge, tag_regex, duration_min, pos_marks, neg_marks, max_qs)
PYQ_DEFS = [
    (
        "tgt_pgt_econ_pyq_up_pgt_2021",
        "UP PGT Economics 2021 — Official Solved Paper",
        "यूपी पीजीटी अर्थशास्त्र 2021 — आधिकारिक हल प्रश्न-पत्र",
        2021,
        "UP PGT 2021 • Economics Official",
        r"UP\s+PGT.*2021",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_econ_pyq_up_pgt_2016",
        "UP PGT Economics 2016 — Official Solved Paper",
        "यूपी पीजीटी अर्थशास्त्र 2016 — आधिकारिक हल प्रश्न-पत्र",
        2016,
        "UP PGT 2016 • Economics Official",
        r"UP\s+PGT.*2016",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_econ_pyq_up_pgt_2011",
        "UP PGT Economics 2011 — Official Solved Paper",
        "यूपी पीजीटी अर्थशास्त्र 2011 — आधिकारिक हल प्रश्न-पत्र",
        2011,
        "UP PGT 2011 • Economics Official",
        r"UP\s+PGT.*2011",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_econ_pyq_up_pgt_2009",
        "UP PGT Economics 2009 — Official Solved Paper",
        "यूपी पीजीटी अर्थशास्त्र 2009 — आधिकारिक हल प्रश्न-पत्र",
        2009,
        "UP PGT 2009 • Economics Official",
        r"UP\s+PGT.*2009",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_econ_pyq_up_pgt_2005",
        "UP PGT Economics 2005 — Official Solved Paper",
        "यूपी पीजीटी अर्थशास्त्र 2005 — आधिकारिक हल प्रश्न-पत्र",
        2005,
        "UP PGT 2005 • Economics Official",
        r"UP\s+PGT.*2005",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_econ_pyq_up_pgt_2004",
        "UP PGT Economics 2004 — Official Solved Paper",
        "यूपी पीजीटी अर्थशास्त्र 2004 — आधिकारिक हल प्रश्न-पत्र",
        2004,
        "UP PGT 2004 • Economics Official",
        r"UP\s+PGT.*2004",
        120, 3.4, 0.0, 125
    ),
    (
        "tgt_pgt_econ_pyq_up_tgt_2021",
        "UP TGT Economics 2021 — Official Solved Paper",
        "यूपी टीजीटी अर्थशास्त्र 2021 — आधिकारिक हल प्रश्न-पत्र",
        2021,
        "UP TGT 2021 • Economics Official",
        r"UP\s+TGT.*2021",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_econ_pyq_up_tgt_2016",
        "UP TGT Economics 2016 — Official Solved Paper",
        "यूपी टीजीटी अर्थशास्त्र 2016 — आधिकारिक हल प्रश्न-पत्र",
        2016,
        "UP TGT 2016 • Economics Official",
        r"UP\s+TGT.*2016",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_econ_pyq_up_tgt_2011",
        "UP TGT Economics 2011 — Official Solved Paper",
        "यूपी टीजीटी अर्थशास्त्र 2011 — आधिकारिक हल प्रश्न-पत्र",
        2011,
        "UP TGT 2011 • Economics Official",
        r"UP\s+TGT.*2011",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_econ_pyq_up_tgt_2009",
        "UP TGT Economics 2009 — Official Solved Paper",
        "यूपी टीजीटी अर्थशास्त्र 2009 — आधिकारिक हल प्रश्न-पत्र",
        2009,
        "UP TGT 2009 • Economics Official",
        r"UP\s+TGT.*2009",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_econ_pyq_up_tgt_2005",
        "UP TGT Economics 2005 — Official Solved Paper",
        "यूपी टीजीटी अर्थशास्त्र 2005 — आधिकारिक हल प्रश्न-पत्र",
        2005,
        "UP TGT 2005 • Economics Official",
        r"UP\s+TGT.*2005",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_econ_pyq_up_tgt_2004",
        "UP TGT Economics 2004 — Official Solved Paper",
        "यूपी टीजीटी अर्थशास्त्र 2004 — आधिकारिक हल प्रश्न-पत्र",
        2004,
        "UP TGT 2004 • Economics Official",
        r"UP\s+TGT.*2004",
        120, 4.0, 0.0, 63
    ),
    (
        "tgt_pgt_econ_pyq_dsssb_pgt_2021",
        "DSSSB PGT Economics 2021 — Official Solved Paper",
        "DSSSB पीजीटी अर्थशास्त्र 2021 — आधिकारिक हल प्रश्न-पत्र",
        2021,
        "DSSSB PGT 2021 • Economics Official",
        r"DSSSB\s+PGT",
        120, 1.0, 0.25, 200
    ),
    (
        "tgt_pgt_econ_pyq_rpsc_pgt_2022",
        "RPSC School Lecturer (PGT) Economics 2022 — Official Paper",
        "RPSC प्राध्यापक (PGT) अर्थशास्त्र 2022 — आधिकारिक हल प्रश्न-पत्र",
        2022,
        "RPSC PGT 2022 • Economics Official",
        r"RPSC\s+PGT",
        120, 2.0, 0.66, 150
    ),
    (
        "tgt_pgt_econ_pyq_kvs_pgt_2018",
        "KVS PGT Economics 2018 — Official Solved Paper",
        "केवीएस पीजीटी अर्थशास्त्र 2018 — आधिकारिक हल प्रश्न-पत्र",
        2018,
        "KVS PGT 2018 • Economics Official",
        r"KVS\s+PGT.*2018",
        120, 1.0, 0.0, 100
    ),
    (
        "tgt_pgt_econ_pyq_kvs_pgt_2017",
        "KVS PGT Economics 2017 — Official Solved Paper",
        "केवीएस पीजीटी अर्थशास्त्र 2017 — आधिकारिक हल प्रश्न-पत्र",
        2017,
        "KVS PGT 2017 • Economics Official",
        r"KVS\s+PGT.*2017",
        120, 1.0, 0.0, 100
    ),
    (
        "tgt_pgt_econ_pyq_nvs_pgt_2022",
        "NVS PGT Economics 2022 — Official Solved Paper",
        "एनवीएस पीजीटी अर्थशास्त्र 2022 — आधिकारिक हल प्रश्न-पत्र",
        2022,
        "NVS PGT 2022 • Economics Official",
        r"NVS\s+PGT",
        120, 1.0, 0.0, 100
    ),
    (
        "tgt_pgt_econ_pyq_jssc_pgt_2018",
        "JSSC PGT Economics 2018 — Official Solved Paper",
        "जेएसएससी पीजीटी अर्थशास्त्र 2018 — आधिकारिक हल प्रश्न-पत्र",
        2018,
        "JSSC PGT 2018 • Economics Official",
        r"JSSC\s+PGT",
        120, 2.0, 0.0, 150
    ),
    (
        "tgt_pgt_econ_pyq_ukpsc_lect_2020",
        "UKPSC Lecturer (Mains) Economics 2020 — Official Paper",
        "UKPSC प्रवक्ता (मुख्य परीक्षा) अर्थशास्त्र 2020 — आधिकारिक प्रश्न-पत्र",
        2020,
        "UKPSC Lecturer 2020 • Economics Official",
        r"UKPSC.*Lecturer",
        120, 1.0, 0.25, 150
    ),
    (
        "tgt_pgt_econ_pyq_uppsc_gic_2021",
        "UPPSC GIC / GDC Lecturer Economics 2021 — Official Paper",
        "यूपीपीएससी जीआईसी / जीडीसी प्रवक्ता अर्थशास्त्र 2021 — आधिकारिक हल प्रश्न-पत्र",
        2021,
        "UPPSC GIC/GDC 2021 • Economics Official",
        r"GDC.*2021|GIC.*2021",
        120, 2.5, 0.83, 100
    )
]

def format_question(q, q_num, test_id, pos_marks, neg_marks):
    corr = q["correctOption"]
    corr_idx = ord(corr) - ord("A") if corr in ["A", "B", "C", "D"] else 0
    return {
        "questionId": f"{test_id}_q{q_num:03d}",
        "questionNumber": q_num,
        "sectionId": "sec_economics",
        "sectionTitle": "Economics (अर्थशास्त्र)",
        "questionType": "MCQ",
        "positiveMarks": pos_marks,
        "negativeMarks": neg_marks,
        "pyqTag": q.get("examTag", "TGT/PGT Economics Solved Papers"),
        "topicTag": q.get("chapter", "Economics"),
        "difficulty": "Medium",
        "correctOption": corr,
        "correctOptionsList": [corr],
        "correct_index": corr_idx,
        "correct_indices": [corr_idx],
        "natMin": None,
        "natMax": None,
        "questionText": q["questionText"],
        "questionTextEn": q["questionText"],
        "questionTextHi": "",
        "options": q["options"],
        "optionsEn": q["options"],
        "optionsHi": [],
        "explanation": q["explanation"],
        "explanationEn": q["explanation"],
        "explanationHi": ""
    }

def build_test_json(test_id, title_en, title_hi, test_type, exam_year, shift_badge, duration_min, pos_marks, neg_marks, raw_qs):
    formatted_qs = []
    for i, q in enumerate(raw_qs, start=1):
        formatted_qs.append(format_question(q, i, test_id, pos_marks, neg_marks))

    return {
        "testId": test_id,
        "categoryId": "tgt_pgt_economics",
        "test_id": test_id,
        "category_id": "tgt_pgt_economics",
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

for item in PYQ_DEFS:
    test_id, title_en, title_hi, exam_year, shift_badge, tag_regex, duration_min, pos_marks, neg_marks, max_qs = item
    rgx = re.compile(tag_regex, re.IGNORECASE)

    matched = []
    for idx, q in enumerate(master_qs):
        if idx not in used_indices and rgx.search(q.get("examTag", "")):
            matched.append((idx, q))
            if len(matched) >= max_qs:
                break

    # Mark indices as used
    for idx, _ in matched:
        used_indices.add(idx)

    raw_qs = [q for _, q in matched]
    test_obj = build_test_json(test_id, title_en, title_hi, "PYQ", exam_year, shift_badge, duration_min, pos_marks, neg_marks, raw_qs)

    file_path = os.path.join(PYQ_DIR, f"{test_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_obj, f, ensure_ascii=False, indent=2)

    print(f"Created PYQ Paper: {test_id} ({len(raw_qs)} questions) -> {file_path}")
    created_pyqs.append(test_obj)

print(f"\nTotal questions used in 20 PYQ papers: {len(used_indices)}")
remaining_indices = [i for i in range(len(master_qs)) if i not in used_indices]
print(f"Remaining unused questions for Mock Tests: {len(remaining_indices)}")

# Now create 10 High-Yield Subject & Full-Length Mock Tests (100 Qs each) from remaining questions
MOCK_DEFS = [
    (
        "tgt_pgt_econ_mock_01_microeconomics",
        "TGT/PGT Economics Mock 1 — Microeconomics & Market Theory",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 1 — व्यष्टि अर्थशास्त्र एवं बाजार संतुलन",
        "Microeconomics • 100 Solved MCQs",
        ["Definition and Nature of Economics", "Demand Analysis & Elasticity", "Theory of Consumer Behaviour & Indifference Curve", "Production Function, Cost & Law of Production", "Equilibrium of the Firm & Market Structures"],
        100
    ),
    (
        "tgt_pgt_econ_mock_02_macroeconomics",
        "TGT/PGT Economics Mock 2 — Macroeconomics & Employment Theory",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 2 — समष्टि अर्थशास्त्र एवं रोजगार सिद्धांत",
        "Macroeconomics • 100 Solved MCQs",
        ["Theory of Employment, Multiplier & IS-LM", "Theory of Trade Cycle", "Theory of Distribution, Profit & Interest"],
        100
    ),
    (
        "tgt_pgt_econ_mock_03_money_banking",
        "TGT/PGT Economics Mock 3 — Money, Banking & Monetary Policy",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 3 — मुद्रा, बैंकिंग एवं मौद्रिक नीति",
        "Money & Banking • 100 Solved MCQs",
        ["Value of Money and Measurement", "Quantity Theory of Money", "Money Inflation & Phillips Curve", "Monetary Policy & Banking Institutions", "Monetary Institutions"],
        100
    ),
    (
        "tgt_pgt_econ_mock_04_public_finance",
        "TGT/PGT Economics Mock 4 — Public Finance, Budget & Taxation",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 4 — लोक वित्त, बजट एवं कराधान",
        "Public Finance • 100 Solved MCQs",
        ["Theory of Public Finance", "Private and Public Goods", "Budget, Fiscal Policy & Economic Survey", "Theory of Taxation & Classification of Taxes", "Public Debt & Finance Commission"],
        100
    ),
    (
        "tgt_pgt_econ_mock_05_international_trade",
        "TGT/PGT Economics Mock 5 — International Economics & Trade",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 5 — अंतर्राष्ट्रीय अर्थशास्त्र एवं व्यापार",
        "International Trade • 100 Solved MCQs",
        ["Theory of International Trade & Terms of Trade", "Foreign Exchange Rate & Devaluation", "Balance of Payments", "International Economic Institutions"],
        100
    ),
    (
        "tgt_pgt_econ_mock_06_growth_development",
        "TGT/PGT Economics Mock 6 — Growth, Development & Planning",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 6 — आर्थिक संवृद्धि, विकास एवं नियोजन",
        "Growth & Planning • 100 Solved MCQs",
        ["Economic Growth, Development & Five Year Plans", "Theories of Economic Growth & Welfare Economics", "Population Theory & Population Policy"],
        100
    ),
    (
        "tgt_pgt_econ_mock_07_indian_economy",
        "TGT/PGT Economics Mock 7 — Indian Economy, Agriculture & Industry",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 7 — भारतीय अर्थव्यवस्था, कृषि एवं उद्योग",
        "Indian Economy • 100 Solved MCQs",
        ["National Income Accounting", "Poverty and Unemployment", "Agriculture, Rural Development & Food Security", "Industrial Policy & MSME"],
        100
    ),
    (
        "tgt_pgt_econ_mock_08_statistics",
        "TGT/PGT Economics Mock 8 — Economic Statistics & Quantitative Analysis",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 8 — आर्थिक सांख्यिकी एवं परिमाणात्मक विश्लेषण",
        "Economic Statistics • 100 Solved MCQs",
        ["Statistics, Central Tendency & Correlation", "Miscellaneous Applied Economics"],
        100
    ),
    (
        "tgt_pgt_econ_mock_09_full_length_1",
        "TGT/PGT Economics Mock 9 — Full-Length Grand Test 1",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 9 — संपूर्ण पाठ्यक्रम ग्रैंड टेस्ट 1",
        "Full Length Mock • 100 Solved MCQs",
        None, # all chapters mixed
        100
    ),
    (
        "tgt_pgt_econ_mock_10_full_length_2",
        "TGT/PGT Economics Mock 10 — Full-Length Grand Test 2",
        "टीजीटी/पीजीटी अर्थशास्त्र मॉक 10 — संपूर्ण पाठ्यक्रम ग्रैंड टेस्ट 2",
        "Full Length Mock • 100 Solved MCQs",
        None, # all chapters mixed
        100
    )
]

created_mocks = []

for mock_item in MOCK_DEFS:
    test_id, title_en, title_hi, badge, target_chapters, q_count = mock_item

    selected = []
    for idx in remaining_indices:
        if idx not in used_indices:
            q = master_qs[idx]
            if target_chapters is None or q.get("chapter") in target_chapters:
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

    print(f"Created Mock Test: {test_id} ({len(raw_qs)} questions) -> {file_path}")
    created_mocks.append(test_obj)

print(f"\nALL DONE! Generated {len(created_pyqs)} PYQ papers and {len(created_mocks)} Mock Tests.")
