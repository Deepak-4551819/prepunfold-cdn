import os
import zipfile
import json
import hashlib
import re
from datetime import datetime, timezone

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_da_official_pyqs_2024_2026.zip"
TARGET_DIR = r"tests/gate/gate_da/pyq"
FULL_MOCKS_DIR = r"tests/gate/gate_da/full_mocks"
TOPIC_TESTS_DIR = r"tests/gate/gate_da/topic_tests"
SHORT_NOTES_DIR = r"tests/gate/gate_da/short_notes"
VIDEOS_DIR = r"tests/gate/gate_da/videos"

for d in [TARGET_DIR, FULL_MOCKS_DIR, TOPIC_TESTS_DIR, SHORT_NOTES_DIR, VIDEOS_DIR]:
    os.makedirs(d, exist_ok=True)

print("Extracting and writing JSON files from zip...")
extracted_tests = {}
with zipfile.ZipFile(ZIP_PATH, "r") as z:
    for year in [2024, 2025, 2026]:
        fname = f"gate_da_pyq_{year}.json"
        data = json.loads(z.read(fname).decode("utf-8"))
        dest_path = os.path.join(TARGET_DIR, fname)
        with open(dest_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        extracted_tests[year] = data
        print(f"  Extracted {fname} -> {dest_path} ({len(data['questions'])} questions)")

print("\nUpdating manifest.json...")
with open("manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

# 1. Category setup
gate_da_category = {
    "id": "gate_da",
    "categoryId": "gate_da",
    "title": "GATE Data Science & Artificial Intelligence (DA)",
    "titleEn": "GATE Data Science & Artificial Intelligence (DA)",
    "titleHi": "गेट डेटा साइंस एवं आर्टिफिशियल इंटेलिजेंस (DA)",
    "subtitle": "Official Master PYQs (2024–2026) with Detailed Solutions & Explanations",
    "descriptionEn": "Official Master PYQs (2024–2026) with Detailed Solutions & Explanations",
    "descriptionHi": "आधिकारिक मास्टर PYQs (2024–2026) विस्तृत समाधान एवं व्याख्या सहित",
    "is_active": True,
    "isActive": True,
    "pass_6m_product_id": "pass_gate_da_6m_49",
    "pass_6m_price": "₹99",
    "pass_6m_strike_price": "₹249",
    "pass_6m_days": 180,
    "pass_1y_product_id": "pass_gate_da_1y_89",
    "pass_1y_price": "₹179",
    "pass_1y_strike_price": "₹399",
    "pass_1y_days": 365,
    "totalTests": 3,
    "totalQuestions": 195,
    "exam_group": "gate",
    "examGroup": "gate",
    "unlocks_categories": [
        "gate_da"
    ],
    "pass_6m_sku": "tier_99",
    "pass_1y_sku": "tier_179",
    "subtitleEn": "Official Master PYQs (2024–2026) with Detailed Solutions & Explanations",
    "subtitleHi": "आधिकारिक मास्टर PYQs (2024–2026) विस्तृत समाधान एवं व्याख्या सहित",
    "parts": [
        {
            "partId": "part_01_ga",
            "partTitleEn": "Section 1: General Aptitude",
            "partTitleHi": "खंड 1: सामान्य योग्यता",
            "order": 1,
            "topicCount": 0,
            "questionCount": 0
        },
        {
            "partId": "part_02_prob_stat",
            "partTitleEn": "Section 2: Probability & Statistics",
            "partTitleHi": "खंड 2: प्रायिकता एवं सांख्यिकी",
            "order": 2,
            "topicCount": 0,
            "questionCount": 0
        },
        {
            "partId": "part_03_la",
            "partTitleEn": "Section 3: Linear Algebra",
            "partTitleHi": "खंड 3: रैखिक बीजगणित",
            "order": 3,
            "topicCount": 0,
            "questionCount": 0
        },
        {
            "partId": "part_04_calc_opt",
            "partTitleEn": "Section 4: Calculus & Optimization",
            "partTitleHi": "खंड 4: कलन एवं इष्टतमीकरण",
            "order": 4,
            "topicCount": 0,
            "questionCount": 0
        },
        {
            "partId": "part_05_pdsa",
            "partTitleEn": "Section 5: Programming, Data Structures & Algorithms",
            "partTitleHi": "खंड 5: प्रोग्रामिंग, डेटा संरचनाएं एवं एल्गोरिदम",
            "order": 5,
            "topicCount": 0,
            "questionCount": 0
        },
        {
            "partId": "part_06_dbms_dw",
            "partTitleEn": "Section 6: Database Management & Warehousing",
            "partTitleHi": "खंड 6: डेटाबेस प्रबंधन एवं डेटा वेयरहाउसिंग",
            "order": 6,
            "topicCount": 0,
            "questionCount": 0
        },
        {
            "partId": "part_07_ml",
            "partTitleEn": "Section 7: Machine Learning",
            "partTitleHi": "खंड 7: मशीन लर्निंग",
            "order": 7,
            "topicCount": 0,
            "questionCount": 0
        },
        {
            "partId": "part_08_ai",
            "partTitleEn": "Section 8: Artificial Intelligence",
            "partTitleHi": "खंड 8: आर्टिफिशियल इंटेलिजेंस",
            "order": 8,
            "topicCount": 0,
            "questionCount": 0
        }
    ]
}

# Update or insert category
categories = manifest.get("categories", [])
existing_cat_idx = None
for i, c in enumerate(categories):
    if c.get("id") == "gate_da":
        existing_cat_idx = i
        break

if existing_cat_idx is not None:
    categories[existing_cat_idx] = gate_da_category
    print("  Updated existing gate_da category entry.")
else:
    # Insert right after gate_cy
    gate_cy_idx = None
    for i, c in enumerate(categories):
        if c.get("id") == "gate_cy":
            gate_cy_idx = i
            break
    if gate_cy_idx is not None:
        categories.insert(gate_cy_idx + 1, gate_da_category)
        print(f"  Inserted gate_da category after gate_cy at index {gate_cy_idx + 1}.")
    else:
        categories.append(gate_da_category)
        print("  Appended gate_da category.")

manifest["categories"] = categories

# 2. Test items
new_test_items = []
for yr in [2026, 2025, 2024]:
    rel_path = f"tests/gate/gate_da/pyq/gate_da_pyq_{yr}.json"
    new_test_items.append({
        "test_id": f"gate_da_pyq_{yr}",
        "testId": f"gate_da_pyq_{yr}",
        "category_id": "gate_da",
        "categoryId": "gate_da",
        "test_type": "PYQ",
        "testType": "PYQ",
        "title": f"GATE {yr} Data Science & Artificial Intelligence (DA) Official Solved Paper",
        "titleEn": f"GATE {yr} Data Science & Artificial Intelligence (DA) Official Solved Paper",
        "titleHi": f"GATE {yr} डेटा साइंस एवं आर्टिफिशियल इंटेलिजेंस (DA) आधिकारिक हल प्रश्न पत्र",
        "exam_year_tag": str(yr),
        "examYearTag": str(yr),
        "shiftBadge": f"GATE DA • {yr} Official Paper",
        "duration_minutes": 180,
        "durationMinutes": 180,
        "total_questions": 65,
        "totalQuestions": 65,
        "positive_marks": 2.0,
        "positiveMarks": 2.0,
        "negative_marks": 0.33,
        "negativeMarks": 0.33,
        "is_free": (yr == 2024),
        "isFree": (yr == 2024),
        "version": 1,
        "path": rel_path,
        "filePath": rel_path,
        "file_path": rel_path,
        "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
        "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
        "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/{rel_path}"
    })

# Remove existing gate_da tests if any
tests = [t for t in manifest.get("tests", []) if t.get("categoryId") != "gate_da"]

# Find where gate_cy tests end in manifest["tests"] to place gate_da tests adjacent
gate_cy_last_idx = -1
for i, t in enumerate(tests):
    if t.get("categoryId") == "gate_cy":
        gate_cy_last_idx = i

if gate_cy_last_idx != -1:
    tests = tests[:gate_cy_last_idx + 1] + new_test_items + tests[gate_cy_last_idx + 1:]
    print(f"  Inserted 3 gate_da test items right after gate_cy tests at index {gate_cy_last_idx + 1}.")
else:
    tests.extend(new_test_items)
    print("  Appended 3 gate_da test items to manifest tests.")

manifest["tests"] = tests

# Recalculate totals
total_tests = len(manifest["tests"])
total_questions = sum(t.get("totalQuestions", t.get("total_questions", 0)) for t in manifest["tests"])
total_cats = len(manifest["categories"])

current_ver = manifest.get("manifest_version", 37)
new_ver = current_ver + 1
manifest["manifest_version"] = new_ver
manifest["manifestVersion"] = new_ver
manifest["version"] = new_ver
manifest["totalCategories"] = total_cats
manifest["totalTests"] = total_tests
manifest["total_tests"] = total_tests
manifest["totalQuestions"] = total_questions

now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
manifest["updatedAt"] = now_iso
manifest["lastUpdated"] = now_iso
manifest["updated_at"] = now_iso

with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print(f"✓ manifest.json updated: manifest_version={new_ver}, totalCategories={total_cats}, totalTests={total_tests}, totalQuestions={total_questions}")

# 3. Update seen_question_hashes.json
print("\nUpdating seen_question_hashes.json...")
with open("seen_question_hashes.json", "r", encoding="utf-8") as f:
    hashes = json.load(f)

# Purge any existing gate_da hashes
hashes = {k: v for k, v in hashes.items() if v.get("categoryId") != "gate_da"}

added = 0
for yr in [2026, 2025, 2024]:
    t = extracted_tests[yr]
    tid = t["testId"]
    for q in t["questions"]:
        text = q.get("questionTextEn", "")
        norm = re.sub(r"\s+", " ", text.strip().lower())
        h = hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]
        hashes[h] = {
            "questionId": q["questionId"],
            "testId": tid,
            "categoryId": "gate_da",
            "topicTag": q.get("topicTag", "Data Science & AI")
        }
        added += 1

with open("seen_question_hashes.json", "w", encoding="utf-8") as f:
    json.dump(hashes, f, ensure_ascii=False, indent=2)

print(f"✓ Added {added} fresh gate_da question hashes to seen_question_hashes.json (Total: {len(hashes)})")
