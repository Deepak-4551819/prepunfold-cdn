import json, os, glob, datetime

MANIFEST_PATH = "manifest.json"
CA_ROOT = "tests/current_affairs"
BASE_CDN_URL = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main"
ALT_CDN_URL = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main"

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

cat_id = "current_affairs"

existing_tests = [t for t in manifest.get("tests", []) if t.get("categoryId") != cat_id and t.get("category_id") != cat_id]

ca_files = glob.glob(f"{CA_ROOT}/**/*.json", recursive=True)
print(f"Found {len(ca_files)} Current Affairs test files to register...")

new_test_entries = []
for fp in sorted(ca_files):
    with open(fp, 'r', encoding='utf-8') as f:
        t_data = json.load(f)

    rel_path = os.path.relpath(fp, ".").replace("\\", "/")
    test_type = "FULL_MOCK" if "/full_mocks/" in rel_path else "SECTIONAL"

    entry = {
        "testId": t_data["testId"],
        "categoryId": cat_id,
        "test_id": t_data["testId"],
        "category_id": cat_id,
        "title": t_data["title"],
        "titleEn": t_data.get("titleEn", t_data["title"]),
        "titleHi": t_data.get("titleHi", ""),
        "testType": test_type,
        "test_type": test_type,
        "isFree": t_data.get("isFree", True),
        "is_free": t_data.get("isFree", True),
        "durationMinutes": t_data.get("durationMinutes", 60),
        "duration_minutes": t_data.get("durationMinutes", 60),
        "totalQuestions": t_data.get("totalQuestions", 50),
        "total_questions": t_data.get("totalQuestions", 50),
        "positiveMarks": t_data.get("positiveMarks", 2.0),
        "negativeMarks": t_data.get("negativeMarks", 0.66),
        "exam_year_tag": str(t_data.get("examYear", 2024)),
        "examYearTag": str(t_data.get("examYear", 2024)),
        "shiftBadge": t_data.get("shiftBadge", "Current Affairs 2024"),
        "version": 1,
        "path": rel_path,
        "filePath": rel_path,
        "file_path": rel_path,
        "json_url": f"{BASE_CDN_URL}/{rel_path}",
        "cdnUrl": f"{BASE_CDN_URL}/{rel_path}",
        "altCdnUrl": f"{ALT_CDN_URL}/{rel_path}"
    }
    new_test_entries.append(entry)

type_prio = {"FULL_MOCK": 0, "PYQ": 1, "SECTIONAL": 2, "TOPIC": 3}
new_test_entries.sort(key=lambda t: (type_prio.get(t["testType"], 99), t["testId"]))

manifest["tests"] = existing_tests + new_test_entries
manifest["total_tests"] = len(manifest["tests"])
manifest["totalTests"] = len(manifest["tests"])

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Manifest successfully updated with {len(new_test_entries)} Current Affairs tests!")
