import json
import os

MANIFEST_PATH = r'D:\Android Project\prepunfold-cdn\manifest.json'
ENTRIES_PATH = r'D:\Android Project\prepunfold-cdn\scripts\polity_manifest_entries.json'
TESTS_DIR = r'D:\Android Project\prepunfold-cdn\tests\polity_pyq_1990_2022'

def update_manifest():
    if not os.path.exists(MANIFEST_PATH):
        print(f"Error: {MANIFEST_PATH} not found.")
        return

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1. Check generated files
    files = [f for f in os.listdir(TESTS_DIR) if f.endswith('.json')]
    print(f"Found {len(files)} generated test files in {TESTS_DIR}.")

    total_questions = 0
    test_entries = []

    # Sort files by topic number
    def get_topic_num(fname):
        m = os.path.basename(fname)
        # e.g. polity_pyq_t01_...
        import re
        m_num = re.search(r'_t(\d+)_', m)
        return int(m_num.group(1)) if m_num else 999

    files.sort(key=get_topic_num)

    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        t_id = data.get("testId", os.path.splitext(fname)[0])
        q_count = data.get("totalQuestions", len(data.get("questions", [])))
        dur = data.get("durationMinutes", q_count)
        total_questions += q_count

        entry = {
            "test_id": t_id,
            "testId": t_id,
            "category_id": "polity_pyq_1990_2022",
            "categoryId": "polity_pyq_1990_2022",
            "test_type": "TOPIC_TEST",
            "testType": "TOPIC_TEST",
            "title": data.get("titleEn", t_id),
            "titleEn": data.get("titleEn", t_id),
            "titleHi": data.get("titleHi", t_id),
            "exam_year_tag": "State PSC & UPSC PYQ (1990–2021)",
            "duration_minutes": dur,
            "durationMinutes": dur,
            "total_questions": q_count,
            "totalQuestions": q_count,
            "positive_marks": 2.0,
            "positiveMarks": 2.0,
            "negative_marks": 0.66,
            "negativeMarks": 0.66,
            "is_free": True,
            "isFree": True,
            "version": 1,
            "path": f"tests/polity_pyq_1990_2022/{fname}",
            "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{fname}",
            "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{fname}",
            "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{fname}"
        }
        test_entries.append(entry)

    # 2. Add or update Category in manifest["categories"]
    polity_category = {
        "id": "polity_pyq_1990_2022",
        "categoryId": "polity_pyq_1990_2022",
        "title": "Indian Polity & Governance PYQ (1990-2022) — All State PSC / UPSC",
        "titleEn": "Indian Polity & Governance PYQ (1990-2022) — All State PSC / UPSC",
        "titleHi": "भारतीय राजव्यवस्था एवं शासन विगत वर्ष प्रश्न (1990-2022) — सभी राज्य पीएससी / यूपीएससी (Topic & Sub-Topic Wise)",
        "subtitle": f"{len(test_entries)} Topic-Wise Mock Tests • 62 Sub-Topics • {total_questions} Real PYQs (1990–2021) with Detailed Solutions",
        "descriptionEn": f"{len(test_entries)} Topic-Wise Mock Tests • 62 Sub-Topics • {total_questions} Real PYQs (1990–2021) with Detailed Solutions",
        "descriptionHi": f"{len(test_entries)} अध्यायवार मॉक टेस्ट • 62 उप-विषय • {total_questions} वास्तविक विगत वर्ष प्रश्न (1990-2021) विस्तृत व्याख्या सहित",
        "is_active": True,
        "pass_6m_product_id": "pass_polity_pyq_6m_99",
        "pass_6m_price": "₹99",
        "pass_6m_strike_price": "₹249",
        "pass_6m_days": 180,
        "pass_1y_product_id": "pass_polity_pyq_1y_179",
        "pass_1y_price": "₹179",
        "pass_1y_strike_price": "₹399",
        "pass_1y_days": 365,
        "totalTests": len(test_entries),
        "totalQuestions": total_questions,
        "parts": [
            {
                "partId": "part1_indian_polity_and_governance",
                "partTitleEn": f"Part I: Indian Polity & Governance (Topics 1–{len(test_entries)} • {total_questions} PYQs)",
                "partTitleHi": f"भाग I: भारतीय राजव्यवस्था एवं शासन (अध्याय 1–{len(test_entries)} • {total_questions} प्रश्न)",
                "topicCount": len(test_entries),
                "questionCount": total_questions
            }
        ]
    }

    # Replace or insert category
    cat_exists = False
    for i, cat in enumerate(manifest.get("categories", [])):
        if cat.get("id") == "polity_pyq_1990_2022" or cat.get("categoryId") == "polity_pyq_1990_2022":
            manifest["categories"][i] = polity_category
            cat_exists = True
            break
    if not cat_exists:
        # Insert after geography
        geo_idx = -1
        for i, cat in enumerate(manifest.get("categories", [])):
            if "geography" in cat.get("id", ""):
                geo_idx = i
                break
        if geo_idx != -1:
            manifest["categories"].insert(geo_idx + 1, polity_category)
        else:
            manifest["categories"].append(polity_category)

    # 3. Add or update tests in manifest["tests"]
    existing_tests = manifest.get("tests", [])
    # Remove old polity entries if any
    filtered_tests = [t for t in existing_tests if t.get("categoryId") != "polity_pyq_1990_2022" and t.get("category_id") != "polity_pyq_1990_2022"]

    # Insert new test entries
    # Find position after geography tests
    insert_idx = len(filtered_tests)
    for i in range(len(filtered_tests) - 1, -1, -1):
        if "geo_pyq" in filtered_tests[i].get("testId", ""):
            insert_idx = i + 1
            break

    for entry in reversed(test_entries):
        filtered_tests.insert(insert_idx, entry)

    manifest["tests"] = filtered_tests
    manifest["manifest_version"] = manifest.get("manifest_version", 14) + 1

    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Updated manifest.json: Added category and {len(test_entries)} tests ({total_questions} Qs). Manifest version is now {manifest['manifest_version']}.")

if __name__ == "__main__":
    update_manifest()
