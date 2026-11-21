import json, os, re

MASTER_FILE = "scripts/extracted_tgt_pgt_economics_master.json"
OUT_DIR = "tests/teaching/tgt_pgt_economics/chapter_tests"
os.makedirs(OUT_DIR, exist_ok=True)

with open(MASTER_FILE, "r", encoding="utf-8") as f:
    master_qs = json.load(f)

print(f"Loaded {len(master_qs)} master Economics questions.")

CHAPTER_METADATA = [
    (1, "Definition and Nature of Economics", "अर्थशास्त्र की परिभाषा एवं प्रकृति", "definition_and_nature"),
    (2, "Demand Analysis & Elasticity", "मांग विश्लेषण एवं लोच", "demand_analysis_elasticity"),
    (3, "Theory of Consumer Behaviour & Indifference Curve", "उपभोक्ता व्यवहार का सिद्धान्त एवं तटस्थता वक्र", "consumer_behaviour_indifference_curve"),
    (4, "Production Function, Cost & Law of Production", "उत्पादन फलन, लागत एवं उत्पादन के नियम", "production_function_cost_laws"),
    (5, "Equilibrium of the Firm & Market Structures", "फर्म का साम्य एवं बाजार संरचनाएँ", "firm_equilibrium_market_structures"),
    (6, "Theory of Distribution, Profit & Interest", "वितरण का सिद्धान्त, लाभ एवं ब्याज", "distribution_profit_interest"),
    (7, "Theory of Employment, Multiplier & IS-LM", "रोजगार का सिद्धान्त, गुणक एवं IS-LM मॉडल", "employment_multiplier_islm"),
    (8, "Theory of Trade Cycle", "व्यापार चक्र का सिद्धान्त", "trade_cycle"),
    (9, "Theory of Public Finance", "लोक वित्त का सिद्धान्त", "public_finance"),
    (10, "Private and Public Goods", "निजी एवं सार्वजनिक वस्तुएँ", "private_public_goods"),
    (11, "Budget, Fiscal Policy & Economic Survey", "बजट, राजकोषीय नीति एवं आर्थिक सर्वेक्षण", "budget_fiscal_policy_economic_survey"),
    (12, "Theory of Taxation & Classification of Taxes", "करारोपण का सिद्धान्त एवं करों का वर्गीकरण", "taxation_tax_classification"),
    (13, "Public Debt & Finance Commission", "सार्वजनिक ऋण एवं वित्त आयोग", "public_debt_finance_commission"),
    (14, "Value of Money and Measurement", "मुद्रा का मूल्य एवं उसका मापन", "value_of_money_measurement"),
    (15, "Quantity Theory of Money", "मुद्रा का परिमाण सिद्धान्त", "quantity_theory_of_money"),
    (16, "Money Inflation & Phillips Curve", "मुद्रास्फीति एवं फिलिप्स वक्र", "inflation_phillips_curve"),
    (17, "Monetary Policy & Banking Institutions", "मौद्रिक नीति एवं बैंकिंग संस्थाएँ", "monetary_policy_banking"),
    (18, "Monetary Institutions", "मुद्रा बाजार एवं वित्तीय संस्थाएँ", "monetary_institutions"),
    (19, "Theory of International Trade & Terms of Trade", "अंतर्राष्ट्रीय व्यापार का सिद्धान्त एवं व्यापार की शर्तें", "international_trade_terms_of_trade"),
    (20, "Foreign Exchange Rate & Devaluation", "विदेशी विनिमय दर एवं अवमूल्यन", "exchange_rate_devaluation"),
    (21, "Balance of Payments", "भुगतान संतुलन", "balance_of_payments"),
    (22, "International Economic Institutions", "अंतर्राष्ट्रीय आर्थिक संस्थाएँ (IMF, WB, WTO)", "international_economic_institutions"),
    (23, "Economic Growth, Development & Five Year Plans", "आर्थिक संवृद्धि, विकास एवं पंचवर्षीय योजनाएँ", "growth_development_five_year_plans"),
    (24, "Theories of Economic Growth & Welfare Economics", "आर्थिक विकास के सिद्धान्त एवं कल्याणकारी अर्थशास्त्र", "growth_theories_welfare_economics"),
    (25, "Population Theory & Population Policy", "जनसंख्या सिद्धान्त एवं जनसंख्या नीति", "population_theory_policy"),
    (26, "National Income Accounting", "राष्ट्रीय आय लेखांकन", "national_income_accounting"),
    (27, "Poverty and Unemployment", "निर्धनता एवं बेरोजगारी", "poverty_unemployment"),
    (28, "Agriculture, Rural Development & Food Security", "कृषि, ग्रामीण विकास एवं खाद्य सुरक्षा", "agriculture_rural_development_food_security"),
    (29, "Industrial Policy & MSME", "औद्योगिक नीति एवं MSME", "industrial_policy_msme"),
    (30, "Statistics, Central Tendency & Correlation", "सांख्यिकी, केन्द्रीय प्रवृत्ति एवं सहसंबंध", "statistics_central_tendency_correlation"),
    (31, "Miscellaneous Applied Economics", "विविध अनुप्रयुक्त अर्थशास्त्र", "miscellaneous_applied_economics")
]

qs_by_chapter = {}
for q in master_qs:
    ch = q.get("chapter", "").strip()
    if ch not in qs_by_chapter:
        qs_by_chapter[ch] = []
    qs_by_chapter[ch].append(q)

built_tests = []

for ch_num, ch_en, ch_hi, slug in CHAPTER_METADATA:
    ch_qs = qs_by_chapter.get(ch_en, [])
    if not ch_qs:
        print(f"Warning: No questions found for chapter {ch_num}: {ch_en}")
        continue

    # Cap to max 100 questions per test for optimal loading and exam experience
    selected_qs = ch_qs[:100]
    total_q = len(selected_qs)
    test_id = f"tgt_pgt_econ_ch{ch_num:02d}_{slug}"

    questions_list = []
    for idx, q in enumerate(selected_qs, 1):
        corr_opt = q.get("correctOption", "A").strip().upper()
        if not corr_opt or corr_opt not in ("A", "B", "C", "D"):
            corr_opt = "A"
        corr_idx = ord(corr_opt) - ord('A')

        raw_opts = q.get("options", ["(A)", "(B)", "(C)", "(D)"])
        while len(raw_opts) < 4:
            raw_opts.append(f"Option {chr(ord('A') + len(raw_opts))}")

        q_item = {
            "questionId": f"{test_id}_q{idx:03d}",
            "questionNumber": idx,
            "sectionId": "sec_economics",
            "sectionTitle": f"Chapter {ch_num:02d}: {ch_en}",
            "questionType": "MCQ",
            "positiveMarks": 1.0,
            "negativeMarks": 0.0,
            "pyqTag": q.get("examTag", f"TGT/PGT Economics Ch {ch_num:02d}"),
            "topicTag": ch_hi,
            "difficulty": "Medium",
            "correctOption": corr_opt,
            "correctOptionsList": [corr_opt],
            "correct_index": corr_idx,
            "correct_indices": [corr_idx],
            "natMin": None,
            "natMax": None,
            "questionText": q.get("questionText", ""),
            "questionTextEn": q.get("questionText", ""),
            "questionTextHi": "",
            "options": raw_opts[:4],
            "optionsEn": raw_opts[:4],
            "optionsHi": [],
            "explanation": q.get("explanation", ""),
            "explanationEn": q.get("explanation", ""),
            "explanationHi": ""
        }
        questions_list.append(q_item)

    duration = 60 if total_q <= 50 else (90 if total_q <= 80 else 120)

    test_doc = {
        "testId": test_id,
        "categoryId": "tgt_pgt_economics",
        "test_id": test_id,
        "category_id": "tgt_pgt_economics",
        "title": f"Economics Chapter {ch_num:02d}: {ch_en}",
        "titleEn": f"Economics Chapter {ch_num:02d}: {ch_en}",
        "titleHi": f"अर्थशास्त्र अध्याय {ch_num:02d}: {ch_hi}",
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
        "path": f"tests/teaching/tgt_pgt_economics/chapter_tests/{test_id}.json",
        "questions": questions_list
    }

    out_path = os.path.join(OUT_DIR, f"{test_id}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(test_doc, f, ensure_ascii=False, indent=2)

    built_tests.append(test_doc)
    print(f"Created Chapter Test {ch_num:02d}: {ch_en} ({total_q} Qs)")

print(f"\nSuccessfully built {len(built_tests)} Economics Chapter Tests!")
