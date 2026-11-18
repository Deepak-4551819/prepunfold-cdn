import json, os, glob, datetime

MANIFEST_PATH = "manifest.json"
CIVICS_ROOT = "tests/teaching/tgt_pgt_civics"

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 1. Update or Add category
categories = manifest.get("categories", [])
cat_id = "tgt_pgt_civics"
cat_entry = None
for c in categories:
    if c.get("categoryId") == cat_id or c.get("category_id") == cat_id:
        cat_entry = c
        break

if not cat_entry:
    cat_entry = {
        "categoryId": cat_id,
        "category_id": cat_id,
        "categoryName": "TGT/PGT Civics & Political Science",
        "category_name": "TGT/PGT Civics & Political Science",
        "categoryNameHi": "टीजीटी/पीजीटी नागरिक शास्त्र एवं राजनीति विज्ञान",
        "iconName": "account_balance",
        "totalTests": 30,
        "order": len(categories) + 1
    }
    categories.append(cat_entry)
else:
    cat_entry["totalTests"] = 30
    cat_entry["categoryName"] = "TGT/PGT Civics & Political Science"
    cat_entry["categoryNameHi"] = "टीजीटी/पीजीटी नागरिक शास्त्र एवं राजनीति विज्ञान"

manifest["categories"] = categories

# 2. Gather all 30 tests
existing_tests = [t for t in manifest.get("tests", []) if t.get("categoryId") != cat_id and t.get("category_id") != cat_id]

civics_files = glob.glob(f"{CIVICS_ROOT}/**/*.json", recursive=True)
print(f"Found {len(civics_files)} test files to register...")

new_test_entries = []
for fp in sorted(civics_files):
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
        "examYear": t_data.get("examYear", 2021),
        "shiftBadge": t_data.get("shiftBadge", ""),
        "filePath": rel_path,
        "file_path": rel_path
    }
    new_test_entries.append(entry)

manifest["tests"] = existing_tests + new_test_entries
manifest["total_tests"] = len(manifest["tests"])
manifest["manifest_version"] = manifest.get("manifest_version", 19) + 1
manifest["updated_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Manifest successfully updated with {len(new_test_entries)} Civics tests!")
print(f"New manifest_version: {manifest['manifest_version']}")
print(f"Total tests registered across all categories: {manifest['total_tests']}")
