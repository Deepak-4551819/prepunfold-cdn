import json, os, re, sys, random

MASTER_PATH = os.path.join(os.path.dirname(__file__), "extracted_tgt_pgt_history_master.json")
PYQ_DIR = "tests/teaching/tgt_pgt_history/pyq"
MOCK_DIR = "tests/teaching/tgt_pgt_history/mock_tests"

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
        topic = q.get("chapterHi", "इतिहास")

        q_obj = {
            "questionId": q_id,
            "questionNumber": idx,
            "sectionId": "sec_history",
            "sectionTitle": "इतिहास (History)",
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
        "categoryId": "tgt_pgt_history",
        "test_id": test_id,
        "category_id": "tgt_pgt_history",
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
    ("tgt_pgt_history_pyq_up_pgt_2021", "UP PGT History 2021 Official Paper", "यूपी पीजीटी इतिहास 2021 आधिकारिक प्रश्न-पत्र", 2021, "UP PGT 2021", r'UP\s*PGT.*2021', 125),
    ("tgt_pgt_history_pyq_up_pgt_2016", "UP PGT History 2016 Official Paper", "यूपी पीजीटी इतिहास 2016 आधिकारिक प्रश्न-पत्र", 2016, "UP PGT 2016", r'UP\s*PGT.*2016|PGT.*2016', 125),
    ("tgt_pgt_history_pyq_up_pgt_2000_2010", "UP PGT History 2000-2010 Solved Paper", "यूपी पीजीटी इतिहास 2000-2010 हल प्रश्न-पत्र", 2010, "UP PGT 2000-10", r'PGT.*(200\d|201[0-5])|झ्उT.*(2००|2०1)|प्रवक्ता.*(200|201)', 100),
    ("tgt_pgt_history_pyq_up_tgt_2021", "UP TGT History 2021 Official Paper", "यूपी टीजीटी इतिहास 2021 आधिकारिक प्रश्न-पत्र", 2021, "UP TGT 2021", r'UP\s*TGT.*2021|TGT.*2021', 63),
    ("tgt_pgt_history_pyq_up_tgt_2016", "UP TGT History 2016 Official Paper", "यूपी टीजीटी इतिहास 2016 आधिकारिक प्रश्न-पत्र", 2016, "UP TGT 2016", r'UP\s*TGT.*2016|TGT.*2016', 63),
    ("tgt_pgt_history_pyq_up_tgt_2004_2011", "UP TGT History 2004-2011 Solved Paper", "यूपी टीजीटी इतिहास 2004-2011 हल प्रश्न-पत्र", 2011, "UP TGT 2004-11", r'TGT.*(200\d|201[0-5])|TउT.*(2००|2०1)', 63),
    ("tgt_pgt_history_pyq_uppsc_gic_2021", "UPPSC GIC Lecturer History 2021 Official Paper", "यूपीपीएससी जीआईसी प्रवक्ता इतिहास 2021 आधिकारिक प्रश्न-पत्र", 2021, "UPPSC GIC 2021", r'UPPSC\s*GIC.*2021|GIC.*2021', 80),
    ("tgt_pgt_history_pyq_uppsc_gic_2018", "UPPSC GIC Lecturer History 2018 Official Paper", "यूपीपीएससी जीआईसी प्रवक्ता इतिहास 2018 आधिकारिक प्रश्न-पत्र", 2018, "UPPSC GIC 2018", r'GIC.*2018', 85),
    ("tgt_pgt_history_pyq_uppsc_gdc_2021", "UPPSC GDC Assistant Professor History 2021", "यूपीपीएससी जीडीसी असिस्टेंट प्रोफेसर इतिहास 2021", 2021, "UPPSC GDC 2021", r'UPPSC\s*GDC.*2021', 80),
    ("tgt_pgt_history_pyq_uppsc_gdc_2017", "UPPSC GDC Assistant Professor History 2017", "यूपीपीएससी जीडीसी असिस्टेंट प्रोफेसर इतिहास 2017", 2017, "UPPSC GDC 2017", r'GDC.*2017', 80),
    ("tgt_pgt_history_pyq_dsssb_pgt_2021_s1", "DSSSB PGT History 2021 (Shift 28/06/2021)", "डीएसएसएसबी पीजीटी इतिहास 2021 (पारी 28 जून)", 2021, "DSSSB PGT 2021", r'DSSSB.*28/06/2021', 120),
    ("tgt_pgt_history_pyq_dsssb_pgt_2021_s2", "DSSSB PGT History 2021 (Shift 10/07/2021)", "डीएसएसएसबी पीजीटी इतिहास 2021 (पारी 10 जुलाई)", 2021, "DSSSB PGT 2021", r'DSSSB.*10/07/2021', 120),
    ("tgt_pgt_history_pyq_dsssb_pgt_2019", "DSSSB PGT History 2019 Official Paper", "डीएसएसएसबी पीजीटी इतिहास 2019 आधिकारिक प्रश्न-पत्र", 2019, "DSSSB PGT 2019", r'DSSSB.*2019', 120),
    ("tgt_pgt_history_pyq_ukpsc_lect_2020", "UKPSC Lecturer History Mains 2020 Official Paper", "यूकेपीएससी प्रवक्ता इतिहास मुख्य परीक्षा 2020", 2020, "UKPSC Lecturer 2020", r'UKPSC.*2020', 150),
    ("tgt_pgt_history_pyq_rpsc_asst_prof_2020_p1", "RPSC Assistant Professor History 2020 (Paper 1)", "आरपीएससी असिस्टेंट प्रोफेसर इतिहास 2020 (प्रश्न-पत्र 1)", 2020, "RPSC Asst Prof 2020", r'RPSC.*Asst.*Prof.*2020.*I\b', 120),
    ("tgt_pgt_history_pyq_rpsc_asst_prof_2020_p2", "RPSC Assistant Professor History 2020 (Paper 2)", "आरपीएससी असिस्टेंट प्रोफेसर इतिहास 2020 (प्रश्न-पत्र 2)", 2020, "RPSC Asst Prof 2020", r'RPSC.*Asst.*Prof.*2020.*II\b', 120),
    ("tgt_pgt_history_pyq_rpsc_lect_2016", "RPSC School Lecturer History 2016 Official Paper", "आरपीएससी प्राध्यापक (स्कूल व्याख्याता) इतिहास 2016", 2016, "RPSC Lecturer 2016", r'RPSC.*2016', 110),
    ("tgt_pgt_history_pyq_mppsc_asst_prof_2017", "MPPSC Assistant Professor History 2017 Official Paper", "एमपीपीएससी असिस्टेंट प्रोफेसर इतिहास 2017", 2017, "MPPSC Asst Prof 2017", r'MP.*Asst.*Prof.*2017|M\.P\..*2017', 120),
    ("tgt_pgt_history_pyq_kvs_tgt_history_2018", "KVS TGT Social Science (History) 2018 Official Paper", "केवीएस टीजीटी सामाजिक विज्ञान (इतिहास) 2018", 2018, "KVS TGT 2018", r'KVS.*2018', 63),
    ("tgt_pgt_history_pyq_ugc_net_history_2021", "UGC NET / JRF History 2021 Official Paper", "यूजीसी नेट / जेआरएफ इतिहास 2021 आधिकारिक प्रश्न-पत्र", 2021, "UGC NET 2021", r'NTA UGC NET.*2020/June 2021', 120)
]

used_indices = set()
for test_id, t_en, t_hi, yr, badge, pat, limit in pyq_specs:
    matched = []
    for idx, q in enumerate(master_qs):
        t = q.get('examTag', '')
        if re.search(pat, t, re.IGNORECASE):
            matched.append((idx, q))

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
    ("tgt_pgt_history_mock_01_prehistoric_indus", "TGT/PGT History Mock 01 — Prehistoric Cultures & Indus Valley", "टीजीटी/पीजीटी इतिहास मॉक 01 — प्रागैतिहासिक संस्कृतियाँ एवं सिन्धु सभ्यता", 2024, "Mock Test 01", ["Prehistoric Cultures of India", "Indus Valley Civilization"], 100),
    ("tgt_pgt_history_mock_02_vedic_religions", "TGT/PGT History Mock 02 — Vedic Period, Jainism & Buddhism", "टीजीटी/पीजीटी इतिहास मॉक 02 — वैदिक काल, जैन एवं बौद्ध धर्म, महाजनपद", 2024, "Mock Test 02", ["Vedic Period", "Jainism, Buddhism & Mahajanapadas"], 100),
    ("tgt_pgt_history_mock_03_mauryan_gupta_chola", "TGT/PGT History Mock 03 — Mauryan, Gupta & Chola Empires", "टीजीटी/पीजीटी इतिहास मॉक 03 — मौर्य, गुप्त एवं चोल साम्राज्य व दक्षिण भारत", 2024, "Mock Test 03", ["Mauryan & Post-Mauryan Empire", "Gupta & Post-Gupta Era", "Chola Dynasty & South India"], 100),
    ("tgt_pgt_history_mock_04_delhi_sultanate", "TGT/PGT History Mock 04 — Delhi Sultanate (Admin, Art & Economy)", "टीजीटी/पीजीटी इतिहास मॉक 04 — दिल्ली सल्तनत (राजनीतिक, प्रशासनिक व सांस्कृतिक)", 2024, "Mock Test 04", ["Delhi Sultanate"], 100),
    ("tgt_pgt_history_mock_05_mughal_maratha", "TGT/PGT History Mock 05 — Mughal Empire, Bahmani & Marathas", "टीजीटी/पीजीटी इतिहास मॉक 05 — मुगल साम्राज्य, बहमनी एवं मराठा साम्राज्य", 2024, "Mock Test 05", ["Mughal Empire", "Vijayanagara, Bahmani & Marathas"], 100),
    ("tgt_pgt_history_mock_06_medieval_culture", "TGT/PGT History Mock 06 — Bhakti, Sufism & Medieval Society", "टीजीटी/पीजीटी इतिहास मॉक 06 — मध्यकालीन संस्कृति, भक्ति एवं सूफी आन्दोलन", 2024, "Mock Test 06", ["Medieval Culture, Bhakti & Sufism", "Medieval Economy & Society"], 100),
    ("tgt_pgt_history_mock_07_british_rule_1857", "TGT/PGT History Mock 07 — British Expansion, Revolt of 1857 & Reforms", "टीजीटी/पीजीटी इतिहास मॉक 07 — ब्रिटिश विस्तार, 1857 विद्रोह एवं सामाजिक सुधार", 2024, "Mock Test 07", ["British Expansion & East India Company", "Revolt of 1857", "Socio-Religious Reform Movements"], 100),
    ("tgt_pgt_history_mock_08_national_movement", "TGT/PGT History Mock 08 — Indian National Movement & Gandhi Era", "टीजीटी/पीजीटी इतिहास मॉक 08 — भारतीय राष्ट्रीय आन्दोलन एवं गाँधी युग", 2024, "Mock Test 08", ["Indian National Movement & Freedom Struggle", "Prominent Leaders in National Movement", "Independence & Partition of India"], 100),
    ("tgt_pgt_history_mock_09_historiography", "TGT/PGT History Mock 09 — Historical Methodology & Historiography", "टीजीटी/पीजीटी इतिहास मॉक 09 — इतिहास दर्शन, शोध प्रविधि एवं स्रोत", 2024, "Mock Test 09", ["Historical Methodology & Historiography"], 100),
    ("tgt_pgt_history_mock_10_world_history", "TGT/PGT History Mock 10 — World History (Renaissance, Revolutions & World Wars)", "टीजीटी/पीजीटी इतिहास मॉक 10 — विश्व इतिहास (पुनर्जागरण, क्रांतियाँ, विश्व युद्ध)", 2024, "Mock Test 10", ["World History"], 100)
]

ch_pools = {}
for idx, q in enumerate(master_qs):
    ch = q.get("chapterEn", "General")
    if ch not in ch_pools:
        ch_pools[ch] = []
    ch_pools[ch].append((idx, q))

mock_used = set()
for test_id, t_en, t_hi, yr, badge, target_chs, limit in mock_specs:
    pool = []
    for ch in target_chs:
        pool.extend(ch_pools.get(ch, []))

    available = [q for idx, q in pool if idx not in mock_used]
    if len(available) < limit:
        available = [q for _, q in pool]

    selected = available[:limit]
    for q in selected:
        mock_used.add(id(q))

    doc = build_paper_json(test_id, t_en, t_hi, "MOCK", yr, badge, selected)
    out_file = os.path.join(MOCK_DIR, f"{test_id}.json")
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"Built Mock: {test_id} -> {len(selected)} questions")

print("\nSuccessfully built all 30 TGT/PGT History test files!")
