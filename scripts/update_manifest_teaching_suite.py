import json, os, glob

MANIFEST_PATH = "manifest.json"
BASE_URL = "https://raw.githubusercontent.com/Deepak-4551819/prepunfold-cdn/main"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# 1. Gather all Economics tests:
econ_dir = "tests/teaching/tgt_pgt_economics"
econ_files = glob.glob(f"{econ_dir}/**/*.json", recursive=True)
print(f"Found {len(econ_files)} Economics test files.")

# 2. Gather all Geography tests:
geo_dir = "tests/teaching/tgt_pgt_geography"
geo_files = glob.glob(f"{geo_dir}/**/*.json", recursive=True)
print(f"Found {len(geo_files)} Geography test files.")

def build_manifest_entry(file_path):
    with open(file_path, "r", encoding="utf-8") as tf:
        data = json.load(tf)

    test_id = data.get("testId") or data.get("test_id")
    cat_id = data.get("categoryId") or data.get("category_id")
    test_type = data.get("testType") or data.get("test_type", "MOCK")
    total_q = data.get("totalQuestions") or data.get("total_questions", len(data.get("questions", [])))
    dur = data.get("durationMinutes") or data.get("duration_minutes", 120)
    pos = data.get("positiveMarks") or data.get("positive_marks", 1.0)
    neg = data.get("negativeMarks") or data.get("negative_marks", 0.0)

    clean_path = file_path.replace("\\", "/")

    return {
        "test_id": test_id,
        "testId": test_id,
        "category_id": cat_id,
        "categoryId": cat_id,
        "test_type": test_type,
        "testType": test_type,
        "title": data.get("title", ""),
        "titleEn": data.get("titleEn", data.get("title", "")),
        "titleHi": data.get("titleHi", ""),
        "exam_year_tag": str(data.get("examYear", 2024)),
        "examYearTag": str(data.get("examYear", 2024)),
        "shiftBadge": data.get("shiftBadge", ""),
        "duration_minutes": dur,
        "durationMinutes": dur,
        "total_questions": total_q,
        "totalQuestions": total_q,
        "positive_marks": pos,
        "positiveMarks": pos,
        "negative_marks": neg,
        "negativeMarks": neg,
        "is_free": data.get("isFree", True),
        "isFree": data.get("isFree", True),
        "version": 1,
        "path": clean_path,
        "json_url": f"{BASE_URL}/{clean_path}",
        "cdnUrl": f"{BASE_URL}/{clean_path}",
        "altCdnUrl": f"{BASE_URL}/{clean_path}"
    }

new_econ_entries = [build_manifest_entry(f) for f in econ_files]
new_geo_entries = [build_manifest_entry(f) for f in geo_files]

# Filter out old econ & geo tests from manifest['tests']
remaining_tests = [
    t for t in manifest.get("tests", [])
    if (t.get("categoryId") or t.get("category_id")) not in ("tgt_pgt_economics", "tgt_pgt_geography", "tgt_pgt_econ_geo")
]

# Sort tests so Chapter/Topic tests come first in order, followed by Mock tests and PYQs
def sort_key(item):
    ttype = item.get("testType", "")
    type_order = 0 if ttype == "TOPIC" else (1 if ttype == "MOCK" else 2)
    return (type_order, item.get("testId", ""))

new_econ_entries.sort(key=sort_key)
new_geo_entries.sort(key=sort_key)

all_new_tests = remaining_tests + new_econ_entries + new_geo_entries
manifest["tests"] = all_new_tests

# Update Categories metadata in manifest['categories']
total_econ_qs = sum(t["totalQuestions"] for t in new_econ_entries)
total_geo_qs = sum(t["totalQuestions"] for t in new_geo_entries)

# Remove legacy tgt_pgt_econ_geo category
manifest["categories"] = [c for c in manifest["categories"] if (c.get("id") or c.get("categoryId")) != "tgt_pgt_econ_geo"]

for cat in manifest["categories"]:
    cid = cat.get("id") or cat.get("categoryId")
    if cid == "tgt_pgt_economics":
        cat["totalTests"] = len(new_econ_entries)
        cat["totalQuestions"] = total_econ_qs
        cat["subtitle"] = f"31 Chapter Topic Tests + 20 Official PYQ Papers + 10 Full Mocks ({total_econ_qs} Solved Qs)"
        cat["descriptionEn"] = f"Complete TGT/PGT Economics: 31 Chapter Topic Tests + 20 Official Shift Papers (UP PGT/TGT, KVS, NVS, DSSSB) + 10 Full Mocks • {total_econ_qs} Solved Questions"
        cat["descriptionHi"] = f"टीजीटी/पीजीटी अर्थशास्त्र: 31 अध्यायवार टॉपिक टेस्ट + 20 आधिकारिक प्रश्न-पत्र + 10 फुल मॉक • {total_econ_qs} हल प्रश्न"
    elif cid == "tgt_pgt_geography":
        cat["totalTests"] = len(new_geo_entries)
        cat["totalQuestions"] = total_geo_qs
        cat["subtitle"] = f"15 Chapter Topic Tests + 20 Official PYQ Papers + 10 Full Mocks ({total_geo_qs} Solved Qs)"
        cat["descriptionEn"] = f"Complete TGT/PGT Geography: 15 Chapter Topic Tests + 20 Official Shift Papers (UP PGT/TGT, KVS, NVS, DSSSB) + 10 Full Mocks • {total_geo_qs} Solved Questions"
        cat["descriptionHi"] = f"टीजीटी/पीजीटी भूगोल: 15 अध्यायवार टॉपिक टेस्ट + 20 आधिकारिक प्रश्न-पत्र + 10 फुल मॉक • {total_geo_qs} हल प्रश्न"

manifest["manifest_version"] = manifest.get("manifest_version", 23) + 1
manifest["version"] = manifest["manifest_version"]
manifest["totalCategories"] = len(manifest["categories"])
manifest["totalTests"] = len(manifest["tests"])

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\nManifest successfully updated!")
print(f"Registered {len(new_econ_entries)} Economics tests (Total Qs: {total_econ_qs})")
print(f"Registered {len(new_geo_entries)} Geography tests (Total Qs: {total_geo_qs})")
print(f"New Manifest Version: v{manifest['manifest_version']}, Total Tests in CDN: {manifest['totalTests']}")
