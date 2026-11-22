# -*- coding: utf-8 -*-
"""
Updates manifest.json with:
1. Category description and 11-section syllabus parts for gate_ph.
2. 4 Official Master PYQs (2024, 2023, 2022, 2021).
3. 12 Full-Length Mock Tests in full_mocks/ (gate_ph_mock_01 to gate_ph_mock_12).
4. 22 Topic-Wise Tests in topic_tests/ (2 tests per topic for all 11 sections).
"""

import json
import os
from build_all_topic_tests import TOPIC_CONFIGS

BASE_CDN_URL = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main"
ALT_CDN_URL = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main"

GATE_PH_PARTS = [
    {
        "partId": cfg["folder"],
        "partTitleEn": f"Section {cfg['index']}: {cfg['title_en']}",
        "partTitleHi": f"खंड {cfg['index']}: {cfg['title_hi']}",
        "order": cfg["index"],
        "topicCount": 2,
        "questionCount": 40
    }
    for cfg in TOPIC_CONFIGS
]

def update_manifest():
    manifest_path = "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # 1. Update Category metadata & parts
    for cat in manifest.get("categories", []):
        if cat.get("id") == "gate_ph" or cat.get("categoryId") == "gate_ph":
            cat["title"] = "GATE Physics (PH) — Revised 11-Section Syllabus"
            cat["titleEn"] = "GATE Physics (PH) — Revised 11-Section Syllabus"
            cat["titleHi"] = "गेट भौतिकी (PH) — संशोधित 11-खंड पाठ्यक्रम"
            cat["subtitle"] = "Official Master PYQs (2024–2021) + 12 Full Length Mocks + 22 Topic-Wise Tests"
            cat["subtitleEn"] = "Official Master PYQs (2024–2021) + 12 Full Length Mocks + 22 Topic-Wise Tests"
            cat["subtitleHi"] = "आधिकारिक मास्टर PYQs (2024–2021) + 12 संपूर्ण मॉक टेस्ट + 22 टॉपिक-वार टेस्ट"
            cat["parts"] = GATE_PH_PARTS
            cat["exam_group"] = "gate"
            cat["examGroup"] = "gate"
            cat["unlocks_categories"] = ["gate_ph"]
            cat["pass_6m_sku"] = "tier_99"
            cat["pass_1y_sku"] = "tier_179"
            break

    # 2. Filter out old gate_ph tests to rebuild cleanly
    tests = manifest.get("tests", [])
    non_gate_ph = [t for t in tests if (t.get("category_id") != "gate_ph" and t.get("categoryId") != "gate_ph")]

    # 3. Add 12 Full Mocks
    full_mocks = []
    for t in range(1, 13):
        tid = f"gate_ph_mock_{t:02d}"
        path = f"tests/gate/gate_ph/full_mocks/{tid}.json"
        assert os.path.exists(path), f"File {path} does not exist!"

        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "gate_ph",
            "categoryId": "gate_ph",
            "test_type": "FULL_MOCK",
            "testType": "FULL_MOCK",
            "title": f"GATE Physics (PH) Full Length Mock Test {t:02d} (11-Section Syllabus)",
            "titleEn": f"GATE Physics (PH) Full Length Mock Test {t:02d} (11-Section Syllabus)",
            "titleHi": f"GATE भौतिकी (PH) संपूर्ण मॉक टेस्ट {t:02d} (11-खंड पाठ्यक्रम)",
            "exam_year_tag": f"GATE PH • Full Mock Test {t:02d}",
            "examYearTag": f"GATE PH • Full Mock Test {t:02d}",
            "shiftBadge": f"Full Mock {t:02d}",
            "duration_minutes": 180,
            "durationMinutes": 180,
            "total_questions": 65,
            "totalQuestions": 65,
            "positive_marks": 2.0,
            "positiveMarks": 2.0,
            "negative_marks": 0.33,
            "negativeMarks": 0.33,
            "is_free": True,
            "isFree": True,
            "version": 1,
            "path": path,
            "filePath": path,
            "file_path": path,
            "json_url": f"{BASE_CDN_URL}/{path}",
            "cdnUrl": f"{BASE_CDN_URL}/{path}",
            "altCdnUrl": f"{ALT_CDN_URL}/{path}"
        }
        full_mocks.append(entry)

    # 4. Add 4 PYQs
    pyqs = []
    for yr in [2024, 2023, 2022, 2021]:
        tid = f"gate_ph_pyq_{yr}"
        path = f"tests/gate/gate_ph/pyq/{tid}.json"
        assert os.path.exists(path), f"File {path} does not exist!"

        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "gate_ph",
            "categoryId": "gate_ph",
            "test_type": "PYQ",
            "testType": "PYQ",
            "title": f"GATE {yr} Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
            "titleEn": f"GATE {yr} Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
            "titleHi": f"GATE {yr} भौतिकी (PH) आधिकारिक प्रश्न पत्र (सभी 9 विषय एवं सामान्य योग्यता)",
            "exam_year_tag": f"GATE PH {yr}",
            "examYearTag": f"GATE PH {yr}",
            "shiftBadge": f"GATE {yr}",
            "duration_minutes": 180,
            "durationMinutes": 180,
            "total_questions": 65,
            "totalQuestions": 65,
            "positive_marks": 2.0,
            "positiveMarks": 2.0,
            "negative_marks": 0.33,
            "negativeMarks": 0.33,
            "is_free": True,
            "isFree": True,
            "version": 1,
            "path": path,
            "filePath": path,
            "file_path": path,
            "json_url": f"{BASE_CDN_URL}/{path}",
            "cdnUrl": f"{BASE_CDN_URL}/{path}",
            "altCdnUrl": f"{ALT_CDN_URL}/{path}"
        }
        pyqs.append(entry)

    # 5. Add 22 Topic Tests
    topic_tests = []
    for cfg in TOPIC_CONFIGS:
        t_folder = cfg["folder"]
        for sub_cfg in [cfg["sub1"], cfg["sub2"]]:
            tid = sub_cfg["id"]
            fname = sub_cfg["file"]
            path = f"tests/gate/gate_ph/topic_tests/{t_folder}/{fname}"
            assert os.path.exists(path), f"File {path} does not exist!"

            entry = {
                "test_id": tid,
                "testId": tid,
                "category_id": "gate_ph",
                "categoryId": "gate_ph",
                "test_type": "TOPIC",
                "testType": "TOPIC",
                "part_id": t_folder,
                "partId": t_folder,
                "title": sub_cfg["title_en"],
                "titleEn": sub_cfg["title_en"],
                "titleHi": sub_cfg["title_hi"],
                "exam_year_tag": sub_cfg["badge"],
                "examYearTag": sub_cfg["badge"],
                "shiftBadge": sub_cfg["badge"],
                "duration_minutes": 60,
                "durationMinutes": 60,
                "total_questions": 20,
                "totalQuestions": 20,
                "positive_marks": 2.0,
                "positiveMarks": 2.0,
                "negative_marks": 0.33,
                "negativeMarks": 0.33,
                "is_free": True,
                "isFree": True,
                "version": 1,
                "path": path,
                "filePath": path,
                "file_path": path,
                "json_url": f"{BASE_CDN_URL}/{path}",
                "cdnUrl": f"{BASE_CDN_URL}/{path}",
                "altCdnUrl": f"{ALT_CDN_URL}/{path}"
            }
            topic_tests.append(entry)

    # Order: FULL_MOCK -> PYQ -> SECTIONAL -> TOPIC
    new_gate_ph_tests = full_mocks + pyqs + topic_tests
    print(f"Total gate_ph tests to insert: {len(new_gate_ph_tests)} (12 Full Mocks + 4 PYQs + 22 Topic Tests)")

    all_tests = non_gate_ph + new_gate_ph_tests
    manifest["tests"] = all_tests

    # Update category count
    for cat in manifest.get("categories", []):
        if cat.get("id") == "gate_ph" or cat.get("categoryId") == "gate_ph":
            cat["totalTests"] = len(new_gate_ph_tests)
            cat["totalQuestions"] = sum(t["totalQuestions"] for t in new_gate_ph_tests)

    manifest["totalTests"] = len(all_tests)
    manifest["total_tests"] = len(all_tests)

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Successfully updated {manifest_path} with {len(all_tests)} total tests!")

if __name__ == "__main__":
    update_manifest()
