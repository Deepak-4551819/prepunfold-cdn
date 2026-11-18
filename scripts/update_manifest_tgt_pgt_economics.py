import json, os, glob

MANIFEST_PATH = "manifest.json"
PYQ_DIR = "tests/teaching/tgt_pgt_economics/pyq"
MOCK_DIR = "tests/teaching/tgt_pgt_economics/mock_tests"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# 1. Add or update tgt_pgt_economics category
categories = manifest.get("categories", [])
cat_exists = False
for cat in categories:
    if cat.get("id") == "tgt_pgt_economics":
        cat_exists = True
        cat.update({
            "title": "TGT / PGT Economics (अर्थशास्त्र)",
            "titleEn": "TGT / PGT Economics (UPSESSB, KVS, NVS, DSSSB, RPSC)",
            "titleHi": "टीजीटी / पीजीटी अर्थशास्त्र (UPSESSB, KVS, NVS, DSSSB, RPSC)",
            "subtitle": "20 Official Full PYQ Papers + 10 Subject Mock Tests (2,992 Solved Questions)",
            "descriptionEn": "20 Official Full PYQ Papers (UP PGT/TGT, KVS, NVS, DSSSB, RPSC) + 10 Subject Mock Tests • 2,992 Solved Questions with Detailed Explanations",
            "descriptionHi": "20 आधिकारिक विगत वर्ष प्रश्न-पत्र (UP PGT/TGT, KVS, NVS, DSSSB, RPSC) + 10 विषयवार मॉक टेस्ट • 2,992 हल प्रश्न विस्तृत व्याख्या सहित",
            "is_active": True,
            "pass_6m_product_id": "pass_tgt_pgt_econ_6m_49",
            "pass_6m_price": "₹49",
            "pass_6m_strike_price": "₹149",
            "pass_6m_days": 180,
            "pass_1y_product_id": "pass_tgt_pgt_econ_1y_89",
            "pass_1y_price": "₹89",
            "pass_1y_strike_price": "₹249",
            "pass_1y_days": 365,
            "totalTests": 30,
            "totalQuestions": 2992
        })
        break

if not cat_exists:
    # Insert right next to tgt_pgt_econ_geo
    new_cat = {
        "id": "tgt_pgt_economics",
        "categoryId": "tgt_pgt_economics",
        "title": "TGT / PGT Economics (अर्थशास्त्र)",
        "titleEn": "TGT / PGT Economics (UPSESSB, KVS, NVS, DSSSB, RPSC)",
        "titleHi": "टीजीटी / पीजीटी अर्थशास्त्र (UPSESSB, KVS, NVS, DSSSB, RPSC)",
        "subtitle": "20 Official Full PYQ Papers + 10 Subject Mock Tests (2,992 Solved Questions)",
        "descriptionEn": "20 Official Full PYQ Papers (UP PGT/TGT, KVS, NVS, DSSSB, RPSC) + 10 Subject Mock Tests • 2,992 Solved Questions with Detailed Explanations",
        "descriptionHi": "20 आधिकारिक विगत वर्ष प्रश्न-पत्र (UP PGT/TGT, KVS, NVS, DSSSB, RPSC) + 10 विषयवार मॉक टेस्ट • 2,992 हल प्रश्न विस्तृत व्याख्या सहित",
        "is_active": True,
        "pass_6m_product_id": "pass_tgt_pgt_econ_6m_49",
        "pass_6m_price": "₹49",
        "pass_6m_strike_price": "₹149",
        "pass_6m_days": 180,
        "pass_1y_product_id": "pass_tgt_pgt_econ_1y_89",
        "pass_1y_price": "₹89",
        "pass_1y_strike_price": "₹249",
        "pass_1y_days": 365,
        "totalTests": 30,
        "totalQuestions": 2992
    }
    insert_idx = len(categories)
    for idx, c in enumerate(categories):
        if c.get("id") == "tgt_pgt_econ_geo":
            insert_idx = idx + 1
            break
    categories.insert(insert_idx, new_cat)

manifest["categories"] = categories

# Fix empty titles in tgt_pgt_econ_geo existing tests if any
for t in manifest.get("tests", []):
    if t.get("test_id") == "tgt_pgt_econ_geo_models_mock_1" and not t.get("title"):
        t["title"] = "TGT/PGT Economic Geography Mock 1 — Theories & Models"
        t["titleEn"] = "TGT/PGT Economic Geography Mock 1 — Theories & Models"
        t["titleHi"] = "टीजीटी/पीजीटी आर्थिक भूगोल मॉक 1 — सिद्धांत एवं मॉडल"
    elif t.get("test_id") == "tgt_pgt_econ_geo_pyq_compendium" and not t.get("title"):
        t["title"] = "TGT/PGT Economic Geography — Real PYQ Compendium"
        t["titleEn"] = "TGT/PGT Economic Geography — Real PYQ Compendium"
        t["titleHi"] = "टीजीटी/पीजीटी आर्थिक भूगोल — वास्तविक विगत वर्ष प्रश्न संग्रह"
    elif t.get("test_id") == "tgt_pgt_geo_pyq_01" and not t.get("title"):
        t["title"] = "UP PGT Geography 2021 — Official PYQ Paper"
        t["titleEn"] = "UP PGT Geography 2021 — Official PYQ Paper"
        t["titleHi"] = "यूपी पीजीटी भूगोल 2021 — आधिकारिक हल प्रश्न-पत्र"

# 2. Filter out any existing tgt_pgt_economics tests
existing_tests = [t for t in manifest.get("tests", []) if t.get("category_id") != "tgt_pgt_economics" and t.get("categoryId") != "tgt_pgt_economics"]

# 3. Read and format all 30 tests
new_test_entries = []

# Process PYQs first
pyq_files = sorted(glob.glob(os.path.join(PYQ_DIR, "*.json")))
for fp in pyq_files:
    with open(fp, "r", encoding="utf-8") as f:
        d = json.load(f)
    rel_path = fp.replace("\\", "/")
    test_entry = {
        "test_id": d["testId"],
        "testId": d["testId"],
        "category_id": "tgt_pgt_economics",
        "categoryId": "tgt_pgt_economics",
        "test_type": "PYQ",
        "testType": "PYQ",
        "title": d["title"],
        "titleEn": d["titleEn"],
        "titleHi": d["titleHi"],
        "exam_year_tag": d["shiftBadge"],
        "examYearTag": d["shiftBadge"],
        "duration_minutes": d["durationMinutes"],
        "durationMinutes": d["durationMinutes"],
        "total_questions": d["totalQuestions"],
        "totalQuestions": d["totalQuestions"],
        "positive_marks": d["positiveMarks"],
        "positiveMarks": d["positiveMarks"],
        "negative_marks": d["negativeMarks"],
        "negativeMarks": d["negativeMarks"],
        "is_free": True,
        "isFree": True,
        "version": 1,
        "path": rel_path,
        "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
        "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
        "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/{rel_path}"
    }
    new_test_entries.append(test_entry)

# Process Mock Tests next
mock_files = sorted(glob.glob(os.path.join(MOCK_DIR, "*.json")))
for fp in mock_files:
    with open(fp, "r", encoding="utf-8") as f:
        d = json.load(f)
    rel_path = fp.replace("\\", "/")
    test_entry = {
        "test_id": d["testId"],
        "testId": d["testId"],
        "category_id": "tgt_pgt_economics",
        "categoryId": "tgt_pgt_economics",
        "test_type": "MOCK",
        "testType": "MOCK",
        "title": d["title"],
        "titleEn": d["titleEn"],
        "titleHi": d["titleHi"],
        "exam_year_tag": d["shiftBadge"],
        "examYearTag": d["shiftBadge"],
        "duration_minutes": d["durationMinutes"],
        "durationMinutes": d["durationMinutes"],
        "total_questions": d["totalQuestions"],
        "totalQuestions": d["totalQuestions"],
        "positive_marks": d["positiveMarks"],
        "positiveMarks": d["positiveMarks"],
        "negative_marks": d["negativeMarks"],
        "negativeMarks": d["negativeMarks"],
        "is_free": True,
        "isFree": True,
        "version": 1,
        "path": rel_path,
        "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
        "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
        "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/{rel_path}"
    }
    new_test_entries.append(test_entry)

manifest["tests"] = existing_tests + new_test_entries
manifest["manifest_version"] = manifest.get("manifest_version", 17) + 1

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Manifest successfully updated with {len(new_test_entries)} tests (20 PYQs + 10 Mocks)!")
print(f"New manifest_version: {manifest['manifest_version']}")
