import json, os, glob, datetime

MANIFEST_PATH = "manifest.json"
CA_ROOT = "tests/current_affairs"

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 1. Update or Add category
categories = manifest.get("categories", [])
cat_id = "current_affairs"
cat_entry = None
for c in categories:
    if c.get("categoryId") == cat_id or c.get("category_id") == cat_id or c.get("id") == cat_id:
        cat_entry = c
        break

if not cat_entry:
    cat_entry = {
        "id": "current_affairs",
        "categoryId": "current_affairs",
        "category_id": "current_affairs",
        "categoryName": "Current Affairs 2024-25 (समसामयिकी)",
        "category_name": "Current Affairs 2024-25 (समसामयिकी)",
        "categoryNameHi": "करेंट अफेयर्स एवं समसामयिकी (2024-25)",
        "title": "Current Affairs 2024-25 (समसामयिकी)",
        "titleEn": "Current Affairs 2024-25 (UPSC, UPPCS, TGT/PGT, SSC, State PSC)",
        "titleHi": "करेंट अफेयर्स एवं समसामयिकी (UPSC, UPPCS, TGT/PGT, SSC, राज्य PSC)",
        "subtitle": "8 Subject/Topic Tests + 2 Full-Length Annual Grand Mocks (600 Solved Questions)",
        "descriptionEn": "Comprehensive National, International, Economy, Science, Environment, Sports, Awards & Annual Mocks with Detailed Explanations",
        "descriptionHi": "राष्ट्रीय, अंतर्राष्ट्रीय, अर्थव्यवस्था, विज्ञान, पर्यावरण, खेल, पुरस्कार एवं वार्षिक महाभ्यास मॉक टेस्ट विस्तृत व्याख्या सहित",
        "iconName": "public",
        "is_active": True,
        "pass_6m_product_id": "pass_current_affairs_6m_49",
        "pass_6m_price": "₹49",
        "pass_6m_strike_price": "₹149",
        "pass_6m_days": 180,
        "pass_1y_product_id": "pass_current_affairs_1y_89",
        "pass_1y_price": "₹89",
        "pass_1y_strike_price": "₹249",
        "pass_1y_days": 365,
        "totalTests": 10,
        "totalQuestions": 600,
        "order": len(categories) + 1
    }
    categories.append(cat_entry)
else:
    cat_entry["totalTests"] = 10
    cat_entry["totalQuestions"] = 600

manifest["categories"] = categories

# 2. Gather all 10 tests
existing_tests = [t for t in manifest.get("tests", []) if t.get("categoryId") != cat_id and t.get("category_id") != cat_id]

ca_files = glob.glob(f"{CA_ROOT}/*.json")
print(f"Found {len(ca_files)} Current Affairs test files to register...")

new_test_entries = []
for fp in sorted(ca_files):
    with open(fp, 'r', encoding='utf-8') as f:
        t_data = json.load(f)

    rel_path = os.path.relpath(fp, ".").replace("\\", "/")
    entry = {
        "testId": t_data["testId"],
        "categoryId": cat_id,
        "test_id": t_data["testId"],
        "category_id": cat_id,
        "title": t_data["title"],
        "titleEn": t_data["titleEn"],
        "titleHi": t_data["titleHi"],
        "testType": t_data["testType"],
        "test_type": t_data["testType"],
        "isFree": t_data["isFree"],
        "is_free": t_data["isFree"],
        "durationMinutes": t_data["durationMinutes"],
        "duration_minutes": t_data["durationMinutes"],
        "totalQuestions": t_data["totalQuestions"],
        "total_questions": t_data["totalQuestions"],
        "maxMarks": t_data["maxMarks"],
        "positiveMarks": t_data["positiveMarks"],
        "negativeMarks": t_data["negativeMarks"],
        "examYear": t_data.get("examYear", 2024),
        "shiftBadge": t_data.get("shiftBadge", "Current Affairs 2024"),
        "filePath": rel_path,
        "file_path": rel_path
    }
    new_test_entries.append(entry)

manifest["tests"] = existing_tests + new_test_entries
manifest["total_tests"] = len(manifest["tests"])
manifest["manifest_version"] = manifest.get("manifest_version", 22) + 1
manifest["updated_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Manifest successfully updated with {len(new_test_entries)} Current Affairs tests!")
print(f"New manifest_version: {manifest['manifest_version']}")
print(f"Total tests registered across all categories: {manifest['total_tests']}")
