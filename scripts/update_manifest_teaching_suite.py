import json, os, glob

MANIFEST_PATH = "manifest.json"
BASE_URL = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main"
ALT_BASE_URL = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main"

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
    clean_path = file_path.replace("\\", "/")

    # Standardize test_type
    if "/full_mocks/" in clean_path:
        test_type = "FULL_MOCK"
    elif "/pyq/" in clean_path:
        test_type = "PYQ"
    elif "/sectional_tests/" in clean_path:
        test_type = "SECTIONAL"
    else:
        test_type = "TOPIC"

    # Part ID for TOPIC tests
    part_id = data.get("partId") or data.get("part_id")
    if test_type == "TOPIC" and not part_id:
        fname = os.path.basename(clean_path)
        ch_num = int(fname.split("_ch")[1][:2])
        if cat_id == "tgt_pgt_economics":
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
        elif cat_id == "tgt_pgt_geography":
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

    total_q = data.get("totalQuestions") or data.get("total_questions", len(data.get("questions", [])))
    dur = data.get("durationMinutes") or data.get("duration_minutes", 120)
    pos = data.get("positiveMarks") or data.get("positive_marks", 1.0)
    neg = data.get("negativeMarks") or data.get("negative_marks", 0.0)

    entry = {
        "test_id": test_id,
        "testId": test_id,
        "category_id": cat_id,
        "categoryId": cat_id,
        "test_type": test_type,
        "testType": test_type,
        "title": data.get("title", ""),
        "titleEn": data.get("titleEn", data.get("title", "")),
        "titleHi": data.get("titleHi", ""),
        "exam_year_tag": str(data.get("examYearTag") or data.get("exam_year_tag") or data.get("examYear", 2024)),
        "examYearTag": str(data.get("examYearTag") or data.get("exam_year_tag") or data.get("examYear", 2024)),
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
        "filePath": clean_path,
        "file_path": clean_path,
        "json_url": f"{BASE_URL}/{clean_path}",
        "cdnUrl": f"{BASE_URL}/{clean_path}",
        "altCdnUrl": f"{ALT_BASE_URL}/{clean_path}"
    }
    if part_id:
        entry["part_id"] = part_id
        entry["partId"] = part_id

    return entry

new_econ_entries = [build_manifest_entry(f) for f in econ_files]
new_geo_entries = [build_manifest_entry(f) for f in geo_files]

# Filter out old econ & geo tests from manifest['tests']
remaining_tests = [
    t for t in manifest.get("tests", [])
    if (t.get("categoryId") or t.get("category_id")) not in ("tgt_pgt_economics", "tgt_pgt_geography", "tgt_pgt_econ_geo")
]

# Lookup part order
cat_parts = {}
for cat in manifest.get("categories", []):
    cid = cat.get("id") or cat.get("categoryId")
    cat_parts[cid] = {p.get("partId"): p.get("order", idx + 1) for idx, p in enumerate(cat.get("parts", []))}

type_prio = {"FULL_MOCK": 0, "PYQ": 1, "SECTIONAL": 2, "TOPIC": 3}

def sort_key(item):
    cid = item.get("categoryId")
    ttype = item.get("testType", "TOPIC")
    prio = type_prio.get(ttype, 99)
    pid = item.get("partId", "")
    p_order = cat_parts.get(cid, {}).get(pid, 999)
    tid = item.get("testId", "")
    return (prio, p_order, tid)

new_econ_entries.sort(key=sort_key)
new_geo_entries.sort(key=sort_key)

all_new_tests = remaining_tests + new_econ_entries + new_geo_entries
manifest["tests"] = all_new_tests

# Update Categories metadata in manifest['categories']
total_econ_qs = sum(t["totalQuestions"] for t in new_econ_entries)
total_geo_qs = sum(t["totalQuestions"] for t in new_geo_entries)

manifest["categories"] = [c for c in manifest["categories"] if (c.get("id") or c.get("categoryId")) != "tgt_pgt_econ_geo"]

for cat in manifest["categories"]:
    cid = cat.get("id") or cat.get("categoryId")
    if cid == "tgt_pgt_economics":
        cat["totalTests"] = len(new_econ_entries)
        cat["totalQuestions"] = total_econ_qs
        cat["subtitle"] = f"31 Topic Tests + 20 Official PYQ Papers + 8 Sectional Tests + 2 Full Mocks ({total_econ_qs} Solved Qs)"
        cat["descriptionEn"] = f"Complete TGT/PGT Economics: 31 Topic Tests + 20 Official Shift Papers + 8 Sectional Tests + 2 Full Mocks • {total_econ_qs} Solved Questions"
        cat["descriptionHi"] = f"टीजीटी/पीजीटी अर्थशास्त्र: 31 टॉपिक टेस्ट + 20 आधिकारिक प्रश्न-पत्र + 8 सेक्शनल टेस्ट + 2 फुल मॉक • {total_econ_qs} हल प्रश्न"
    elif cid == "tgt_pgt_geography":
        cat["totalTests"] = len(new_geo_entries)
        cat["totalQuestions"] = total_geo_qs
        cat["subtitle"] = f"15 Topic Tests + 20 Official PYQ Papers + 8 Sectional Tests + 2 Full Mocks ({total_geo_qs} Solved Qs)"
        cat["descriptionEn"] = f"Complete TGT/PGT Geography: 15 Topic Tests + 20 Official Shift Papers + 8 Sectional Tests + 2 Full Mocks • {total_geo_qs} Solved Questions"
        cat["descriptionHi"] = f"टीजीटी/पीजीटी भूगोल: 15 टॉपिक टेस्ट + 20 आधिकारिक प्रश्न-पत्र + 8 सेक्शनल टेस्ट + 2 फुल मॉक • {total_geo_qs} हल प्रश्न"

manifest["totalCategories"] = len(manifest["categories"])
manifest["totalTests"] = len(manifest["tests"])
manifest["total_tests"] = len(manifest["tests"])

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\nManifest successfully updated!")
print(f"Registered {len(new_econ_entries)} Economics tests (Total Qs: {total_econ_qs})")
print(f"Registered {len(new_geo_entries)} Geography tests (Total Qs: {total_geo_qs})")
