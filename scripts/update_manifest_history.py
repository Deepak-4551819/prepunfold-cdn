import json
import os
import re

MANIFEST_PATH = r'D:\Android Project\prepunfold-cdn\manifest.json'
TESTS_DIR = r'D:\Android Project\prepunfold-cdn\tests\history_pyq_1990_2024'

def update_manifest():
    if not os.path.exists(MANIFEST_PATH):
        print(f"Error: {MANIFEST_PATH} not found.")
        return

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    files = [f for f in os.listdir(TESTS_DIR) if f.endswith('.json')]
    print(f"Found {len(files)} generated history test files in {TESTS_DIR}.")

    # Sort files: anc first, med second, mod third, then by topic number
    def sort_key(fname):
        part_order = 0 if '_anc_' in fname else 1 if '_med_' in fname else 2
        m_num = re.search(r'_t(\d+)_', fname)
        t_num = int(m_num.group(1)) if m_num else 999
        return (part_order, t_num)

    files.sort(key=sort_key)

    total_questions = 0
    part_counts = {
        "part1_ancient_history": {"tests": 0, "qs": 0},
        "part2_medieval_history": {"tests": 0, "qs": 0},
        "part3_modern_history": {"tests": 0, "qs": 0}
    }
    test_entries = []

    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        t_id = data.get("testId", os.path.splitext(fname)[0])
        p_id = data.get("partId", "part1_ancient_history")
        q_count = data.get("totalQuestions", len(data.get("questions", [])))
        dur = data.get("durationMinutes", q_count)
        total_questions += q_count

        if p_id in part_counts:
            part_counts[p_id]["tests"] += 1
            part_counts[p_id]["qs"] += q_count

        entry = {
            "test_id": t_id,
            "testId": t_id,
            "category_id": "history_pyq_1990_2024",
            "categoryId": "history_pyq_1990_2024",
            "test_type": "TOPIC_TEST",
            "testType": "TOPIC_TEST",
            "title": data.get("titleEn", t_id),
            "titleEn": data.get("titleEn", t_id),
            "titleHi": data.get("titleHi", t_id),
            "exam_year_tag": "State PSC & UPSC PYQ (1990–2023)",
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
            "path": f"tests/history_pyq_1990_2024/{fname}",
            "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/history_pyq_1990_2024/{fname}",
            "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/history_pyq_1990_2024/{fname}",
            "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/history_pyq_1990_2024/{fname}"
        }
        test_entries.append(entry)

    history_category = {
        "id": "history_pyq_1990_2024",
        "categoryId": "history_pyq_1990_2024",
        "title": "Indian History PYQ (1990-2024) — All State PSC / UPSC",
        "titleEn": "Indian History PYQ (1990-2024) — All State PSC / UPSC",
        "titleHi": "भारतीय इतिहास विगत वर्ष प्रश्न (1990-2024) — सभी राज्य पीएससी / यूपीएससी (Topic & Sub-Topic Wise)",
        "subtitle": f"{len(test_entries)} Topic-Wise Mock Tests • Ancient, Medieval & Modern • {total_questions} Real PYQs (1990–2023) with Detailed Solutions",
        "descriptionEn": f"{len(test_entries)} Topic-Wise Mock Tests • Ancient, Medieval & Modern • {total_questions} Real PYQs (1990–2023) with Detailed Solutions",
        "descriptionHi": f"{len(test_entries)} अध्यायवार मॉक टेस्ट • प्राचीन, मध्यकालीन एवं आधुनिक भारत • {total_questions} वास्तविक विगत वर्ष प्रश्न (1990-2023) विस्तृत व्याख्या सहित",
        "is_active": True,
        "pass_6m_product_id": "pass_hist_pyq_6m_99",
        "pass_6m_price": "₹99",
        "pass_6m_strike_price": "₹249",
        "pass_6m_days": 180,
        "pass_1y_product_id": "pass_hist_pyq_1y_179",
        "pass_1y_price": "₹179",
        "pass_1y_strike_price": "₹399",
        "pass_1y_days": 365,
        "totalTests": len(test_entries),
        "totalQuestions": total_questions,
        "parts": [
            {
                "partId": "part1_ancient_history",
                "partTitleEn": f"Part I: Ancient History of India ({part_counts['part1_ancient_history']['tests']} Topics • {part_counts['part1_ancient_history']['qs']} PYQs)",
                "partTitleHi": f"भाग I: प्राचीन भारत का इतिहास ({part_counts['part1_ancient_history']['tests']} अध्याय • {part_counts['part1_ancient_history']['qs']} प्रश्न)",
                "topicCount": part_counts['part1_ancient_history']['tests'],
                "questionCount": part_counts['part1_ancient_history']['qs']
            },
            {
                "partId": "part2_medieval_history",
                "partTitleEn": f"Part II: Medieval History of India ({part_counts['part2_medieval_history']['tests']} Topics • {part_counts['part2_medieval_history']['qs']} PYQs)",
                "partTitleHi": f"भाग II: मध्यकालीन भारत का इतिहास ({part_counts['part2_medieval_history']['tests']} अध्याय • {part_counts['part2_medieval_history']['qs']} प्रश्न)",
                "topicCount": part_counts['part2_medieval_history']['tests'],
                "questionCount": part_counts['part2_medieval_history']['qs']
            },
            {
                "partId": "part3_modern_history",
                "partTitleEn": f"Part III: Modern History of India ({part_counts['part3_modern_history']['tests']} Topics • {part_counts['part3_modern_history']['qs']} PYQs)",
                "partTitleHi": f"भाग III: आधुनिक भारत का इतिहास ({part_counts['part3_modern_history']['tests']} अध्याय • {part_counts['part3_modern_history']['qs']} प्रश्न)",
                "topicCount": part_counts['part3_modern_history']['tests'],
                "questionCount": part_counts['part3_modern_history']['qs']
            }
        ]
    }

    # Insert or update Category
    cat_exists = False
    for i, cat in enumerate(manifest.get("categories", [])):
        if cat.get("id") == "history_pyq_1990_2024" or cat.get("categoryId") == "history_pyq_1990_2024":
            manifest["categories"][i] = history_category
            cat_exists = True
            break
    if not cat_exists:
        manifest["categories"].append(history_category)

    # Insert or update tests
    existing_tests = manifest.get("tests", [])
    filtered_tests = [t for t in existing_tests if t.get("categoryId") != "history_pyq_1990_2024" and t.get("category_id") != "history_pyq_1990_2024"]
    filtered_tests.extend(test_entries)

    manifest["tests"] = filtered_tests
    manifest["manifest_version"] = manifest.get("manifest_version", 14) + 1

    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Updated manifest.json: Added History category and {len(test_entries)} tests ({total_questions} Qs).")

if __name__ == "__main__":
    update_manifest()
