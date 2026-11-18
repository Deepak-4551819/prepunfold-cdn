import json, os, re, sys, random

MASTER_PATH = os.path.join(os.path.dirname(__file__), "extracted_tgt_pgt_civics_master.json")
PYQ_DIR = "tests/teaching/tgt_pgt_civics/pyq"
MOCK_DIR = "tests/teaching/tgt_pgt_civics/mock_tests"

os.makedirs(PYQ_DIR, exist_ok=True)
os.makedirs(MOCK_DIR, exist_ok=True)

with open(MASTER_PATH, 'r', encoding='utf-8') as f:
    master_qs = json.load(f)

print(f"Loaded {len(master_qs)} master questions.")

def build_paper_json(test_id, title_en, title_hi, test_type, exam_year, shift_badge, q_list):
    questions_formatted = []
    for idx, q in enumerate(q_list, 1):
        corr_opt = q.get("correctOption", "A").upper()
        if corr_opt not in ['A', 'B', 'C', 'D']:
            corr_opt = 'A'
        corr_idx = ord(corr_opt) - ord('A')

        q_id = f"{test_id}_q{idx:03d}"
        q_text = q["questionTextHi"]
        opts = q["optionsHi"]
        while len(opts) < 4:
            opts.append(f"इनमें से कोई नहीं ({len(opts)+1})")
        opts = opts[:4]

        exp = q.get("explanationHi", "") or f"सही विकल्प ({corr_opt}) है।"
        topic = q.get("chapterHi", "नागरिक शास्त्र")

        q_obj = {
            "questionId": q_id,
            "questionNumber": idx,
            "sectionId": "sec_civics",
            "sectionTitle": "नागरिक शास्त्र एवं राजनीति विज्ञान (Civics & Political Science)",
            "questionType": "MCQ",
            "positiveMarks": 1.33,
            "negativeMarks": 0.33,
            "pyqTag": q.get("examTag") or shift_badge,
            "topicTag": topic,
            "difficulty": "Medium",
            "correctOption": corr_opt,
            "correctOptionsList": [corr_opt],
            "correct_index": corr_idx,
            "correct_indices": [corr_idx],
            "natMin": None,
            "natMax": None,
            "questionTextEn": q_text,
            "optionsEn": opts,
            "explanationEn": exp,
            "questionTextHi": q_text,
            "optionsHi": opts,
            "explanationHi": exp
        }
        questions_formatted.append(q_obj)

    total_q = len(questions_formatted)
    max_m = round(total_q * 1.33, 2)

    doc = {
        "testId": test_id,
        "categoryId": "tgt_pgt_civics",
        "test_id": test_id,
        "category_id": "tgt_pgt_civics",
        "title": title_en,
        "titleEn": title_en,
        "titleHi": title_hi,
        "testType": test_type,
        "test_type": test_type,
        "isFree": True,
        "is_free": True,
        "durationMinutes": 120,
        "duration_minutes": 120,
        "totalQuestions": total_q,
        "total_questions": total_q,
        "maxMarks": max_m,
        "positiveMarks": 1.33,
        "negativeMarks": 0.33,
        "examYear": exam_year,
        "shiftBadge": shift_badge,
        "questions": questions_formatted
    }
    return doc

# --- 20 OFFICIAL PYQ PAPERS DEFINITIONS ---
pyq_specs = [
    ("tgt_pgt_civics_pyq_up_pgt_2021", "UP PGT Civics 2021 Official Paper", "यूपी पीजीटी नागरिक शास्त्र 2021 आधिकारिक प्रश्न-पत्र", 2021, "UP PGT 2021", r'UP\s*PGT.*2021', 125),
    ("tgt_pgt_civics_pyq_up_pgt_2016", "UP PGT Civics 2016 Official Paper", "यूपी पीजीटी नागरिक शास्त्र 2016 आधिकारिक प्रश्न-पत्र", 2016, "UP PGT 2016", r'UP\s*PGT.*2016|PGT.*2016', 125),
    ("tgt_pgt_civics_pyq_up_pgt_2010", "UP PGT Civics 2010 Official Paper", "यूपी पीजीटी नागरिक शास्त्र 2010 आधिकारिक प्रश्न-पत्र", 2010, "UP PGT 2010", r'PGT.*2010|झ्उT.*2०1०', 100),
    ("tgt_pgt_civics_pyq_up_pgt_2000_2004", "UP PGT Civics 2000-2004 Solved Paper", "यूपी पीजीटी नागरिक शास्त्र 2000-2004 हल प्रश्न-पत्र", 2004, "UP PGT 2000-04", r'PGT.*(200[0-5]|201[1-3])|झ्उT.*(2००[०-५]|2०1[१-३])|प्रवक्ता.*(200[0-5]|201[1-3])', 100),
    ("tgt_pgt_civics_pyq_up_tgt_2021", "UP TGT Civics 2021 Official Paper", "यूपी टीजीटी नागरिक शास्त्र 2021 आधिकारिक प्रश्न-पत्र", 2021, "UP TGT 2021", r'UP\s*TGT.*2021|TGT.*2021', 63),
    ("tgt_pgt_civics_pyq_up_tgt_2016", "UP TGT Civics 2016 Official Paper", "यूपी टीजीटी नागरिक शास्त्र 2016 आधिकारिक प्रश्न-पत्र", 2016, "UP TGT 2016", r'UP\s*TGT.*2016|TGT.*2016', 63),
    ("tgt_pgt_civics_pyq_up_tgt_2004_2010", "UP TGT Civics 2004-2010 Solved Paper", "यूपी टीजीटी नागरिक शास्त्र 2004-2010 हल प्रश्न-पत्र", 2010, "UP TGT 2004-10", r'TGT.*(200\d|201[0-5])|TउT.*(2००|2०1[०-५])', 63),
    ("tgt_pgt_civics_pyq_up_lt_grade_2018", "UP LT Grade Civics 2018 Official Paper", "यूपी एलटी ग्रेड नागरिक शास्त्र 2018 आधिकारिक प्रश्न-पत्र", 2018, "UP LT Grade 2018", r'LT\s*Grade|UP\s*LT', 60),
    ("tgt_pgt_civics_pyq_uppsc_gic_2021", "UPPSC GIC Lecturer Civics 2021 Official Paper", "यूपीपीएससी जीआईसी प्रवक्ता नागरिक शास्त्र 2021 आधिकारिक प्रश्न-पत्र", 2021, "UPPSC GIC 2021", r'UPPSC\s*GIC.*2021|GIC.*2021', 80),
    ("tgt_pgt_civics_pyq_uppsc_gdc_2021", "UPPSC GDC Assistant Professor Political Science 2021", "यूपीपीएससी जीडीसी असिस्टेंट प्रोफेसर राजनीति विज्ञान 2021", 2021, "UPPSC GDC 2021", r'GDC|G\.D\.C', 90),
    ("tgt_pgt_civics_pyq_dsssb_pgt_2021_s1", "DSSSB PGT Political Science 2021 (Shift 1)", "डीएसएसएसबी पीजीटी राजनीति विज्ञान 2021 (पारी 1)", 2021, "DSSSB PGT 2021", r'DSSSB.*22/07/2021', 120),
    ("tgt_pgt_civics_pyq_dsssb_pgt_2021_s2", "DSSSB PGT Political Science 2021 (Shift 2)", "डीएसएसएसबी पीजीटी राजनीति विज्ञान 2021 (पारी 2)", 2021, "DSSSB PGT 2021", r'DSSSB.*04/07/2021', 120),
    ("tgt_pgt_civics_pyq_ukpsc_lect_2020", "UKPSC Lecturer Civics Mains 2020 Official Paper", "यूकेपीएससी प्रवक्ता नागरिक शास्त्र मुख्य परीक्षा 2020", 2020, "UKPSC Lecturer 2020", r'UKPSC.*Lecturer.*2020|उत्तराखण्ड.*लेक्यचरर.*2020', 150),
    ("tgt_pgt_civics_pyq_uk_gic_asst_prof_2018", "UK GIC / Assistant Professor Civics 2017-2018", "उत्तराखण्ड जीआईसी / असिस्टेंट प्रोफेसर नागरिक शास्त्र 2018", 2018, "UK GIC 2018", r'UK\s*GIC|Uttarakhand.*2017|खण्ड असि', 100),
    ("tgt_pgt_civics_pyq_rpsc_lect_2020_p1", "RPSC Assistant Professor Political Science 2020 (Paper 1)", "आरपीएससी असिस्टेंट प्रोफेसर राजनीति विज्ञान 2020 (प्रश्न-पत्र 1)", 2020, "RPSC Asst Prof 2020", r'RPSC.*Asst.*Prof.*2020.*I\b|राज.*2016.*प्रथम', 120),
    ("tgt_pgt_civics_pyq_rpsc_lect_2020_p2", "RPSC Assistant Professor Political Science 2020 (Paper 2)", "आरपीएससी असिस्टेंट प्रोफेसर राजनीति विज्ञान 2020 (प्रश्न-पत्र 2)", 2020, "RPSC Asst Prof 2020", r'RPSC.*Asst.*Prof.*2020.*II\b|राज.*2016.*द्वितीय', 120),
    ("tgt_pgt_civics_pyq_haryana_pgt_asst_2020", "Haryana PGT / Assistant Professor Political Science 2020", "हरियाणा पीजीटी / असिस्टेंट प्रोफेसर राजनीति विज्ञान 2020", 2020, "Haryana PGT 2020", r'Haryana', 100),
    ("tgt_pgt_civics_pyq_mppsc_asst_prof_2018", "MPPSC Assistant Professor Political Science 2018", "एमपीपीएससी असिस्टेंट प्रोफेसर राजनीति विज्ञान 2018", 2018, "MPPSC Asst Prof 2018", r'M\.P\..*Assistant', 120),
    ("tgt_pgt_civics_pyq_cgpsc_asst_prof_2016", "CGPSC Assistant Professor Political Science 2014-2016", "सीजीपीएससी असिस्टेंट प्रोफेसर राजनीति विज्ञान 2016", 2016, "CGPSC Asst Prof 2016", r'CGPSC', 80),
    ("tgt_pgt_civics_pyq_ugc_net_pol_sci_2021", "UGC NET / JRF Political Science 2021 Official Paper", "यूजीसी नेट / जेआरएफ राजनीति विज्ञान 2021 आधिकारिक प्रश्न-पत्र", 2021, "UGC NET 2021", r'NTA UGC NET.*2020/June 2021', 120)
]

used_indices = set()
for test_id, t_en, t_hi, yr, badge, pat, limit in pyq_specs:
    matched = []
    for idx, q in enumerate(master_qs):
        t = q.get('examTag', '')
        if re.search(pat, t, re.IGNORECASE):
            matched.append((idx, q))

    # Pick up to limit
    selected_idx_q = matched[:limit]
    for idx, _ in selected_idx_q:
        used_indices.add(idx)

    selected_qs = [q for _, q in selected_idx_q]
    doc = build_paper_json(test_id, t_en, t_hi, "PYQ", yr, badge, selected_qs)
    out_file = os.path.join(PYQ_DIR, f"{test_id}.json")
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"Built PYQ: {test_id} -> {len(selected_qs)} questions")

# --- 10 SUBJECT & GRAND MOCK TESTS DEFINITIONS ---
mock_specs = [
    ("tgt_pgt_civics_mock_01_political_theory", "TGT/PGT Civics Mock Test 01 — Political Theory & Concepts", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 01 — राजनीतिक सिद्धान्त एवं अवधारणाएँ", 2024, "Mock Test 01", "Political Theory", 100),
    ("tgt_pgt_civics_mock_02_sovereignty_rights", "TGT/PGT Civics Mock Test 02 — Sovereignty, Rights, Liberty & Justice", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 02 — सम्प्रभुता, अधिकार, स्वतंत्रता एवं न्याय", 2024, "Mock Test 02", "Political Theory", 100),
    ("tgt_pgt_civics_mock_03_political_ideologies", "TGT/PGT Civics Mock Test 03 — Political Ideologies & Democracy", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 03 — प्रमुख राजनीतिक विचारधाराएँ एवं लोकतन्त्र", 2024, "Mock Test 03", "Political Theory", 100),
    ("tgt_pgt_civics_mock_04_comparative_politics", "TGT/PGT Civics Mock Test 04 — Comparative Politics & Government Forms", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 04 — तुलनात्मक शासन एवं राजनीति", 2024, "Mock Test 04", "Comparative Politics & Government", 100),
    ("tgt_pgt_civics_mock_05_western_thinkers", "TGT/PGT Civics Mock Test 05 — Western Political Thinkers", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 05 — पाश्चात्य राजनीतिक विचारक (प्लेटो, अरस्तू, मैकियावेली, मार्क्स)", 2024, "Mock Test 05", "Political Thinkers", 100),
    ("tgt_pgt_civics_mock_06_indian_thinkers", "TGT/PGT Civics Mock Test 06 — Indian Political Thinkers", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 06 — भारतीय राजनीतिक विचारक (मनु, कौटिल्य, गाँधी, अम्बेडकर)", 2024, "Mock Test 06", "Political Thinkers", 100),
    ("tgt_pgt_civics_mock_07_indian_constitution", "TGT/PGT Civics Mock Test 07 — Indian Constitution & Fundamental Rights", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 07 — भारतीय संविधान, मौलिक अधिकार एवं नीति निदेशक तत्व", 2024, "Mock Test 07", "Indian Government, Constitution & Politics", 100),
    ("tgt_pgt_civics_mock_08_union_state_govt", "TGT/PGT Civics Mock Test 08 — Union & State Government (Parliament, Executive & Judiciary)", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 08 — संघ एवं राज्य सरकार (संसद, कार्यपालिका एवं न्यायपालिका)", 2024, "Mock Test 08", "Indian Government, Constitution & Politics", 100),
    ("tgt_pgt_civics_mock_09_public_admin", "TGT/PGT Civics Mock Test 09 — Public Administration & Local Self Government", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 09 — लोक प्रशासन एवं स्थानीय स्वशासन", 2024, "Mock Test 09", "Public Administration", 100),
    ("tgt_pgt_civics_mock_10_international_relations", "TGT/PGT Civics Mock Test 10 — International Relations & Foreign Policy", "टीजीटी/पीजीटी नागरिक शास्त्र मॉक 10 — भारतीय विदेश नीति एवं अंतर्राष्ट्रीय सम्बन्ध", 2024, "Mock Test 10", "International Relations & Foreign Policy", 100)
]

# Build chapter question pools
ch_pools = {}
for idx, q in enumerate(master_qs):
    ch = q.get("chapterEn", "General")
    if ch not in ch_pools:
        ch_pools[ch] = []
    ch_pools[ch].append((idx, q))

mock_used = set()
for test_id, t_en, t_hi, yr, badge, target_ch, limit in mock_specs:
    pool = ch_pools.get(target_ch, [])
    # Filter available
    available = [q for idx, q in pool if idx not in mock_used]
    if len(available) < limit:
        # allow fallback from all available in that pool
        available = [q for _, q in pool]

    selected = available[:limit]
    for q in selected:
        mock_used.add(id(q))

    doc = build_paper_json(test_id, t_en, t_hi, "MOCK", yr, badge, selected)
    out_file = os.path.join(MOCK_DIR, f"{test_id}.json")
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"Built Mock: {test_id} -> {len(selected)} questions")

print("\nSuccessfully built all 30 TGT/PGT Civics test files!")
