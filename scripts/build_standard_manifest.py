import os
import json
import glob
import datetime

MANIFEST_PATH = "manifest.json"
BASE_CDN_URL = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main"
ALT_CDN_URL = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def determine_test_metadata(file_path):
    data = load_json(file_path)
    clean_path = file_path.replace("\\", "/")

    test_id = data.get("testId") or data.get("test_id")
    category_id = data.get("categoryId") or data.get("category_id")

    # Standardize category_id if missing or mismatch
    if not category_id:
        if "tgt_pgt_economics" in clean_path:
            category_id = "tgt_pgt_economics"
        elif "tgt_pgt_geography" in clean_path:
            category_id = "tgt_pgt_geography"
        elif "tgt_pgt_civics" in clean_path:
            category_id = "tgt_pgt_civics"
        elif "tgt_pgt_history" in clean_path:
            category_id = "tgt_pgt_history"
        elif "gate_ph" in clean_path:
            category_id = "gate_ph"
        elif "gate_cs" in clean_path:
            category_id = "gate_cs"
        elif "gate_ma" in clean_path:
            category_id = "gate_ma"
        elif "gate_cy" in clean_path:
            category_id = "gate_cy"
        elif "jam_ph" in clean_path:
            category_id = "jam_ph"
        elif "jam_ma" in clean_path:
            category_id = "jam_ma"
        elif "jam_cy" in clean_path:
            category_id = "jam_cy"
        elif "uppcs_pre" in clean_path:
            category_id = "uppcs_pre"
        elif "upsc_cse" in clean_path:
            category_id = "upsc_cse"
        elif "ssc_gd" in clean_path:
            category_id = "ssc_gd"
        elif "ssc_chsl" in clean_path:
            category_id = "ssc_chsl"
        elif "rrb_ntpc" in clean_path:
            category_id = "rrb_ntpc"
        elif "current_affairs" in clean_path:
            category_id = "current_affairs"
        elif "geography_pyq_1993_2026" in clean_path:
            category_id = "geography_pyq_1993_2026"
        elif "polity_pyq_1990_2022" in clean_path:
            category_id = "polity_pyq_1990_2022"
        elif "history_pyq_1990_2024" in clean_path:
            category_id = "history_pyq_1990_2024"
        elif "judiciary_pyq" in clean_path:
            category_id = "judiciary_pyq"

    # Determine test_type strictly in {"FULL_MOCK", "PYQ", "SECTIONAL", "TOPIC"}
    if "/full_mocks/" in clean_path:
        test_type = "FULL_MOCK"
    elif "/pyq/" in clean_path:
        test_type = "PYQ"
    elif "/sectional_tests/" in clean_path:
        test_type = "SECTIONAL"
    elif "/topic_tests/" in clean_path or "geography_pyq_1993_2026" in clean_path or "polity_pyq_1990_2022" in clean_path or "history_pyq_1990_2024" in clean_path or "judiciary_pyq" in clean_path:
        test_type = "TOPIC"
    else:
        # fallback based on data
        raw_type = data.get("testType") or data.get("test_type", "TOPIC")
        if raw_type in ("MOCK", "FULL_MOCK"):
            test_type = "FULL_MOCK"
        elif raw_type == "PYQ":
            test_type = "PYQ"
        elif raw_type == "SECTIONAL":
            test_type = "SECTIONAL"
        else:
            test_type = "TOPIC"

    # Determine part_id / partId if TOPIC
    part_id = data.get("partId") or data.get("part_id")
    if test_type == "TOPIC" and not part_id:
        if category_id == "tgt_pgt_economics":
            fname = os.path.basename(clean_path)
            ch_num = int(fname.split("_ch")[1][:2])
            if ch_num <= 6:
                part_id = "microeconomics"
            elif ch_num <= 8:
                part_id = "macroeconomics"
            elif ch_num <= 13:
                part_id = "public_finance"
            elif ch_num <= 18:
                part_id = "money_banking"
            elif ch_num <= 22:
                part_id = "international_trade"
            else:
                part_id = "indian_economy"
        elif category_id == "tgt_pgt_geography":
            fname = os.path.basename(clean_path)
            ch_num = int(fname.split("_ch")[1][:2])
            if ch_num == 1:
                part_id = "geographical_thought"
            elif ch_num <= 8:
                part_id = "physical_geography"
            elif ch_num <= 12:
                part_id = "human_economic_geography"
            elif ch_num <= 14:
                part_id = "indian_geography"
            else:
                part_id = "practical_cartography"
        elif category_id == "gate_ph":
            part_id = clean_path.split("/topic_tests/")[1].split("/")[0]
        elif category_id == "geography_pyq_1993_2026":
            part_id = "part1_indian_geography" if "geo_pyq_ind_" in clean_path else "part2_world_geography"
        elif category_id == "polity_pyq_1990_2022":
            part_id = "part1_indian_polity_and_governance"
        elif category_id == "history_pyq_1990_2024":
            fname = os.path.basename(clean_path)
            if "anc_" in fname:
                part_id = "part1_ancient_history"
            elif "med_" in fname:
                part_id = "part2_medieval_history"
            else:
                part_id = "part3_modern_history"
        elif category_id == "judiciary_pyq":
            sub = clean_path.split("/judiciary_pyq/")[1].split("/")[0]
            part_map_jud = {
                "cpc": "part1_cpc_1908",
                "crpc": "part2_crpc_1973",
                "evidence": "part3_evidence_1872",
                "ipc": "part4_ipc_1860",
                "constitution": "part5_constitution_of_india",
                "tpa": "part6_transfer_of_property_1882",
                "contract": "part7_indian_contract_act_1872",
                "tort": "part8_law_of_torts",
                "limitation": "part9_limitation_act_1963",
                "sra": "part10_specific_relief_act_1963",
                "trust_equity": "part11_law_of_trust_and_equity",
                "jurisprudence": "part12_jurisprudence",
                "international_org": "part13_international_organisations",
                "minor_acts": "part14_minor_acts"
            }
            part_id = part_map_jud.get(sub)
        elif category_id == "upsc_cse":
            part_id = "part1_indian_geography" if "ind_" in clean_path else "part2_world_geography"

    dur = data.get("durationMinutes") or data.get("duration_minutes", 120)
    total_q = data.get("totalQuestions") or data.get("total_questions", len(data.get("questions", [])))
    pos = data.get("positiveMarks") or data.get("positive_marks", 1.0)
    neg = data.get("negativeMarks") or data.get("negative_marks", 0.0)
    ey = data.get("examYearTag") or data.get("exam_year_tag") or str(data.get("examYear", 2024))
    sb = data.get("shiftBadge", "")

    title_en = data.get("titleEn") or data.get("title", "")
    title_hi = data.get("titleHi", "")
    title_main = data.get("title") or title_en

    entry = {
        "test_id": test_id,
        "testId": test_id,
        "category_id": category_id,
        "categoryId": category_id,
        "test_type": test_type,
        "testType": test_type,
        "title": title_main,
        "titleEn": title_en,
        "titleHi": title_hi,
        "exam_year_tag": ey,
        "examYearTag": ey,
        "shiftBadge": sb,
        "duration_minutes": dur,
        "durationMinutes": dur,
        "total_questions": total_q,
        "totalQuestions": total_q,
        "positive_marks": pos,
        "positiveMarks": pos,
        "negative_marks": neg,
        "negativeMarks": neg,
        "is_free": data.get("isFree", data.get("is_free", True)),
        "isFree": data.get("isFree", data.get("is_free", True)),
        "version": 1,
        "path": clean_path,
        "filePath": clean_path,
        "file_path": clean_path,
        "json_url": f"{BASE_CDN_URL}/{clean_path}",
        "cdnUrl": f"{BASE_CDN_URL}/{clean_path}",
        "altCdnUrl": f"{ALT_CDN_URL}/{clean_path}"
    }
    if part_id:
        entry["part_id"] = part_id
        entry["partId"] = part_id

    return entry

def build_categories(existing_categories):
    # Filter out legacy unused category
    cats = [c for c in existing_categories if (c.get("id") or c.get("categoryId")) != "tgt_pgt_econ_geo"]
    cat_by_id = {}
    for c in cats:
        cid = c.get("id") or c.get("categoryId")
        cat_by_id[cid] = c

    # 1. gate_ph parts
    gate_ph_parts = [
        {
            "partId": "01_measurements_error_analysis",
            "partTitleEn": "Section 1: Measurements & Error Analysis",
            "partTitleHi": "खंड 1: मापन एवं त्रुटि विश्लेषण",
            "order": 1,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "02_mathematical_physics",
            "partTitleEn": "Section 2: Mathematical Physics",
            "partTitleHi": "खंड 2: गणितीय भौतिकी",
            "order": 2,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "03_classical_mechanics",
            "partTitleEn": "Section 3: Classical Mechanics",
            "partTitleHi": "खंड 3: चिरसम्मत यांत्रिकी",
            "order": 3,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "04_electromagnetic_theory",
            "partTitleEn": "Section 4: Electromagnetic Theory",
            "partTitleHi": "खंड 4: विद्युतचुंबकीय सिद्धांत",
            "order": 4,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "05_quantum_mechanics",
            "partTitleEn": "Section 5: Quantum Mechanics",
            "partTitleHi": "खंड 5: क्वांटम यांत्रिकी",
            "order": 5,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "06_optical_physics",
            "partTitleEn": "Section 6: Optical Physics",
            "partTitleHi": "खंड 6: प्रकाशीय भौतिकी",
            "order": 6,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "07_thermodynamics_stat_physics",
            "partTitleEn": "Section 7: Thermodynamics & Statistical Physics",
            "partTitleHi": "खंड 7: ऊष्मागतिकी एवं सांख्यिकीय भौतिकी",
            "order": 7,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "08_atomic_molecular_physics",
            "partTitleEn": "Section 8: Atomic & Molecular Physics",
            "partTitleHi": "खंड 8: परमाण्विक एवं आणविक भौतिकी",
            "order": 8,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "09_solid_state_physics",
            "partTitleEn": "Section 9: Solid State Physics",
            "partTitleHi": "खंड 9: ठोस अवस्था भौतिकी",
            "order": 9,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "10_electronics",
            "partTitleEn": "Section 10: Electronics",
            "partTitleHi": "खंड 10: इलेक्ट्रॉनिकी",
            "order": 10,
            "topicCount": 2,
            "questionCount": 40
        },
        {
            "partId": "11_nuclear_particle_physics",
            "partTitleEn": "Section 11: Nuclear & Particle Physics",
            "partTitleHi": "खंड 11: नाभिकीय एवं कण भौतिकी",
            "order": 11,
            "topicCount": 2,
            "questionCount": 40
        }
    ]

    # 2. tgt_pgt_economics parts
    econ_parts = [
        {
            "partId": "microeconomics",
            "partTitleEn": "Unit 1: Microeconomics & Market Theory",
            "partTitleHi": "इकाई 1: व्यष्टि अर्थशास्त्र एवं बाजार सिद्धान्त",
            "order": 1,
            "topicCount": 6,
            "questionCount": 600
        },
        {
            "partId": "macroeconomics",
            "partTitleEn": "Unit 2: Macroeconomics & Trade Cycles",
            "partTitleHi": "इकाई 2: समष्टि अर्थशास्त्र एवं व्यापार चक्र",
            "order": 2,
            "topicCount": 2,
            "questionCount": 200
        },
        {
            "partId": "public_finance",
            "partTitleEn": "Unit 3: Public Finance, Budget & Taxation",
            "partTitleHi": "इकाई 3: लोक वित्त, बजट एवं कराधान",
            "order": 3,
            "topicCount": 5,
            "questionCount": 500
        },
        {
            "partId": "money_banking",
            "partTitleEn": "Unit 4: Money, Banking & Monetary Institutions",
            "partTitleHi": "इकाई 4: मुद्रा, बैंकिंग एवं मौद्रिक संस्थाएं",
            "order": 4,
            "topicCount": 5,
            "questionCount": 500
        },
        {
            "partId": "international_trade",
            "partTitleEn": "Unit 5: International Trade & Foreign Exchange",
            "partTitleHi": "इकाई 5: अंतर्राष्ट्रीय व्यापार एवं विदेशी विनिमय",
            "order": 5,
            "topicCount": 4,
            "questionCount": 400
        },
        {
            "partId": "indian_economy",
            "partTitleEn": "Unit 6: Indian Economy, Growth & Applied Statistics",
            "partTitleHi": "इकाई 6: भारतीय अर्थव्यवस्था, संवृद्धि एवं सांख्यिकी",
            "order": 6,
            "topicCount": 9,
            "questionCount": 900
        }
    ]

    # 3. tgt_pgt_geography parts
    geo_parts = [
        {
            "partId": "geographical_thought",
            "partTitleEn": "Unit 1: Geographical Thought & Concepts",
            "partTitleHi": "इकाई 1: भौगोलिक चिंतन एवं संकल्पनाएं",
            "order": 1,
            "topicCount": 1,
            "questionCount": 100
        },
        {
            "partId": "physical_geography",
            "partTitleEn": "Unit 2: Physical Geography, Geomorphology & Climatology",
            "partTitleHi": "इकाई 2: भौतिक भूगोल, भू-आकृति एवं जलवायु विज्ञान",
            "order": 2,
            "topicCount": 7,
            "questionCount": 700
        },
        {
            "partId": "human_economic_geography",
            "partTitleEn": "Unit 3: Human & Economic Geography",
            "partTitleHi": "इकाई 3: मानव एवं आर्थिक भूगोल",
            "order": 3,
            "topicCount": 4,
            "questionCount": 400
        },
        {
            "partId": "indian_geography",
            "partTitleEn": "Unit 4: Geography of India (Physical & Economic)",
            "partTitleHi": "इकाई 4: भारत का भूगोल (भौतिक एवं आर्थिक)",
            "order": 4,
            "topicCount": 2,
            "questionCount": 200
        },
        {
            "partId": "practical_cartography",
            "partTitleEn": "Unit 5: Cartography & Practical Geography",
            "partTitleHi": "इकाई 5: मानचित्रकला एवं प्रायोगिक भूगोल",
            "order": 5,
            "topicCount": 1,
            "questionCount": 100
        }
    ]

    # 4. upsc_cse parts
    upsc_parts = [
        {
            "partId": "part1_indian_geography",
            "partTitleEn": "Part I: Indian Geography (Topics 1–9)",
            "partTitleHi": "भाग I: भारत का भूगोल (अध्याय 1–9)",
            "order": 1,
            "topicCount": 9,
            "questionCount": 450
        },
        {
            "partId": "part2_world_geography",
            "partTitleEn": "Part II: World Geography (Topics 1–6)",
            "partTitleHi": "भाग II: विश्व का भूगोल (अध्याय 1–6)",
            "order": 2,
            "topicCount": 6,
            "questionCount": 300
        }
    ]

    # Category exam_group mapping
    group_map = {
        "tgt_pgt_economics": "teaching",
        "tgt_pgt_geography": "teaching",
        "tgt_pgt_civics": "teaching",
        "tgt_pgt_history": "teaching",
        "gate_ph": "gate",
        "gate_cs": "gate",
        "gate_ma": "gate",
        "gate_cy": "gate",
        "jam_ph": "jam",
        "jam_ma": "jam",
        "jam_cy": "jam",
        "uppcs_pre": "state_psc",
        "upsc_cse": "upsc",
        "ssc_gd": "ssc",
        "ssc_chsl": "ssc",
        "rrb_ntpc": "railway",
        "current_affairs": "general",
        "geography_pyq_1993_2026": "state_psc",
        "polity_pyq_1990_2022": "state_psc",
        "history_pyq_1990_2024": "state_psc",
        "judiciary_pyq": "judiciary"
    }

    sku_tiers = {
        "teaching": ("tier_49", "tier_89", "₹49", "₹89", "₹149", "₹249"),
        "ssc": ("tier_49", "tier_89", "₹49", "₹89", "₹149", "₹249"),
        "railway": ("tier_49", "tier_89", "₹49", "₹89", "₹149", "₹249"),
        "general": ("tier_49", "tier_89", "₹49", "₹89", "₹149", "₹249"),
        "gate": ("tier_99", "tier_179", "₹99", "₹179", "₹249", "₹399"),
        "jam": ("tier_99", "tier_179", "₹99", "₹179", "₹249", "₹399"),
        "state_psc": ("tier_99", "tier_179", "₹99", "₹179", "₹249", "₹399"),
        "upsc": ("tier_99", "tier_179", "₹99", "₹179", "₹249", "₹399"),
        "judiciary": ("tier_99", "tier_179", "₹99", "₹179", "₹249", "₹399")
    }

    for cid, cat in cat_by_id.items():
        grp = group_map.get(cid, "state_psc")
        cat["exam_group"] = grp
        cat["examGroup"] = grp
        cat["unlocks_categories"] = [cid]

        sku_6m, sku_1y, p_6m, p_1y, sp_6m, sp_1y = sku_tiers.get(grp, ("tier_49", "tier_89", "₹49", "₹89", "₹149", "₹249"))
        cat["pass_6m_sku"] = sku_6m
        cat["pass_1y_sku"] = sku_1y
        cat["pass_6m_price"] = p_6m
        cat["pass_1y_price"] = p_1y
        cat["pass_6m_strike_price"] = sp_6m
        cat["pass_1y_strike_price"] = sp_1y
        cat["pass_6m_days"] = 180
        cat["pass_1y_days"] = 365

        # Keep old pass product id for backward compat if present, or assign tier
        if "pass_6m_product_id" not in cat:
            cat["pass_6m_product_id"] = sku_6m
        if "pass_1y_product_id" not in cat:
            cat["pass_1y_product_id"] = sku_1y

        if cid == "gate_ph":
            cat["parts"] = gate_ph_parts
        elif cid == "tgt_pgt_economics":
            cat["parts"] = econ_parts
        elif cid == "tgt_pgt_geography":
            cat["parts"] = geo_parts
        elif cid == "upsc_cse":
            cat["parts"] = upsc_parts

    return list(cat_by_id.values())

def main():
    print("=== Step 2: Building Standard manifest.json ===")

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = load_json(MANIFEST_PATH)

    # 1. Categories
    categories = build_categories(manifest.get("categories", []))

    # Create quick part order lookup map for sorting
    # {cid: {partId: order_int}}
    part_order_map = {}
    for cat in categories:
        cid = cat.get("id") or cat.get("categoryId")
        part_order_map[cid] = {}
        for idx, p in enumerate(cat.get("parts", [])):
            pid = p.get("partId")
            order = p.get("order", idx + 1)
            part_order_map[cid][pid] = order

    # 2. Collect all valid test JSON files on disk
    all_json_files = glob.glob("tests/**/*.json", recursive=True)
    print(f"Total test JSON files found on disk: {len(all_json_files)}")

    manifest_tests = []
    seen_ids = set()
    duplicate_ids = []

    for fp in all_json_files:
        clean_p = fp.replace("\\", "/")
        entry = determine_test_metadata(clean_p)
        tid = entry["test_id"]
        if tid in seen_ids:
            duplicate_ids.append((tid, clean_p))
        else:
            seen_ids.add(tid)
        manifest_tests.append(entry)

    if duplicate_ids:
        print(f"WARNING: Found {len(duplicate_ids)} duplicate test IDs: {duplicate_ids}")

    # 3. Sort tests inside each category consistently:
    # FULL_MOCK -> PYQ -> SECTIONAL -> TOPIC (ordered by part order, then test order)
    type_priority = {
        "FULL_MOCK": 0,
        "PYQ": 1,
        "SECTIONAL": 2,
        "TOPIC": 3
    }

    def test_sort_key(t):
        cid = t.get("categoryId")
        ttype = t.get("testType", "TOPIC")
        prio = type_priority.get(ttype, 99)
        pid = t.get("partId", "")
        p_order = part_order_map.get(cid, {}).get(pid, 999)
        tid = t.get("testId", "")
        path = t.get("path", "")
        return (prio, p_order, tid, path)

    # Group tests by category
    tests_by_cat = {}
    for t in manifest_tests:
        cid = t.get("categoryId")
        tests_by_cat.setdefault(cid, []).append(t)

    sorted_all_tests = []
    # Preserve order of categories
    cat_order = [c.get("id") or c.get("categoryId") for c in categories]
    for cid in cat_order:
        c_tests = tests_by_cat.get(cid, [])
        c_tests.sort(key=test_sort_key)
        sorted_all_tests.extend(c_tests)

    # Update category totals
    for cat in categories:
        cid = cat.get("id") or cat.get("categoryId")
        c_tests = tests_by_cat.get(cid, [])
        cat["totalTests"] = len(c_tests)
        cat["totalQuestions"] = sum(t.get("totalQuestions", 0) for t in c_tests)

    # 4. Top-level Bundles
    bundles = [
        {
            "bundle_id": "bundle_tgt_pgt_sst",
            "bundleId": "bundle_tgt_pgt_sst",
            "title": "TGT/PGT Social Science Combo (सामाजिक विज्ञान कॉम्बो)",
            "titleEn": "TGT/PGT Social Science Combo (Economics, Geography, History, Civics)",
            "titleHi": "टीजीटी/पीजीटी सामाजिक विज्ञान कॉम्बो (अर्थशास्त्र, भूगोल, इतिहास, नागरिक शास्त्र)",
            "subtitle": "All 4 Teaching Subjects • Official PYQs + Sectional Tests + Full Mocks + Topic Tests",
            "exam_group": "teaching",
            "examGroup": "teaching",
            "unlocks_categories": [
                "tgt_pgt_geography",
                "tgt_pgt_economics",
                "tgt_pgt_history",
                "tgt_pgt_civics"
            ],
            "pass_6m_sku": "tier_99",
            "pass_6m_product_id": "tier_99",
            "pass_6m_price": "₹99",
            "pass_6m_strike_price": "₹249",
            "pass_6m_days": 180,
            "pass_1y_sku": "tier_179",
            "pass_1y_product_id": "tier_179",
            "pass_1y_price": "₹179",
            "pass_1y_strike_price": "₹399",
            "pass_1y_days": 365,
            "is_active": True
        },
        {
            "bundle_id": "bundle_all_access",
            "bundleId": "bundle_all_access",
            "title": "AbhyasDesk All-Access Pass (संपूर्ण एक्सेस पास)",
            "titleEn": "AbhyasDesk All-Access Pass (All Exams & Streams)",
            "titleHi": "अभ्यासडेस्क संपूर्ण एक्सेस पास (सभी परीक्षाएं एवं विषय)",
            "subtitle": "Unlock Everything: All Teaching, GATE, UPSC, State PSC, SSC, Railway & Compendiums",
            "exam_group": "all",
            "examGroup": "all",
            "unlocks_categories": ["*"],
            "pass_6m_sku": "tier_179",
            "pass_6m_product_id": "tier_179",
            "pass_6m_price": "₹179",
            "pass_6m_strike_price": "₹499",
            "pass_6m_days": 180,
            "pass_1y_sku": "tier_399",
            "pass_1y_product_id": "tier_399",
            "pass_1y_price": "₹399",
            "pass_1y_strike_price": "₹999",
            "pass_1y_days": 365,
            "is_active": True
        }
    ]

    # 5. Remote config
    remote_config = manifest.get("remote_config", {})
    remote_config.update({
        "active_play_product_id": "tier_179",
        "strike_through_price": "₹499",
        "promo_badge": "ALL-ACCESS PASS",
        "promo_title": "Unlock All Exams & Streams",
        "promo_subtitle": "Official PYQs + Pro Full Mocks + Sectional & Topic Tests • Detailed Explanations",
        "free_tests_unlocked_by_default": True
    })

    # 6. Master manifest
    manifest["manifest_version"] = manifest.get("manifest_version", 26) + 1
    manifest["version"] = manifest["manifest_version"]
    manifest["remote_config"] = remote_config
    manifest["categories"] = categories
    manifest["bundles"] = bundles
    manifest["tests"] = sorted_all_tests
    manifest["totalCategories"] = len(categories)
    manifest["totalTests"] = len(sorted_all_tests)
    manifest["total_tests"] = len(sorted_all_tests)
    manifest["totalQuestions"] = sum(t.get("totalQuestions", 0) for t in sorted_all_tests)
    manifest["updated_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest["lastUpdated"] = manifest["updated_at"]

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Manifest successfully updated!")
    print(f"New Manifest Version: v{manifest['manifest_version']}")
    print(f"Total Categories: {manifest['totalCategories']}")
    print(f"Total Bundles: {len(bundles)}")
    print(f"Total Tests: {manifest['totalTests']}")
    print(f"Total Questions: {manifest['totalQuestions']}")

if __name__ == "__main__":
    main()
