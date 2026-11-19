# -*- coding: utf-8 -*-
"""
Updates manifest.json with:
1. Category description update for gate_ph (11-section syllabus).
2. 4 Official Master PYQs (2024, 2023, 2022, 2021).
3. 12 Full-Length Mock Tests (gate_ph_mock_01 to gate_ph_mock_12).
4. 22 Topic-Wise Tests (2 tests per topic for all 11 sections).
"""

import json
import os
from build_all_topic_tests import TOPIC_CONFIGS

def update_manifest():
    manifest_path = "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # 1. Update Category metadata
    for cat in manifest.get("categories", []):
        if cat.get("id") == "gate_ph":
            cat["title"] = "GATE Physics (PH) — Revised 11-Section Syllabus"
            cat["titleEn"] = "GATE Physics (PH) — Revised 11-Section Syllabus"
            cat["titleHi"] = "गेट भौतिकी (PH) — संशोधित 11-खंड पाठ्यक्रम"
            cat["subtitle"] = "Official Master PYQs (2024–2021) + 12 Full Length Mocks + 22 Topic-Wise Tests"
            cat["subtitleEn"] = "Official Master PYQs (2024–2021) + 12 Full Length Mocks + 22 Topic-Wise Tests"
            cat["subtitleHi"] = "आधिकारिक मास्टर PYQs (2024–2021) + 12 संपूर्ण मॉक टेस्ट + 22 टॉपिक-वार टेस्ट"
            break

    # 2. Filter out old gate_ph topic tests and mocks to rebuild cleanly
    tests = manifest.get("tests", [])
    non_gate_ph = [t for t in tests if (t.get("category_id") != "gate_ph" and t.get("categoryId") != "gate_ph")]
    pyqs = [t for t in tests if (t.get("category_id") == "gate_ph" or t.get("categoryId") == "gate_ph") and "pyq" in (t.get("test_id") or t.get("testId", ""))]

    print(f"Retained {len(pyqs)} PYQs:")
    for p in pyqs:
        print("  PYQ:", p.get("test_id") or p.get("testId"))

    new_gate_ph_tests = []
    # Add PYQs first
    new_gate_ph_tests.extend(pyqs)

    # Add 12 Full Mocks
    for t in range(1, 13):
        tid = f"gate_ph_mock_{t:02d}"
        path = f"tests/gate/gate_ph/mock_tests/{tid}.json"
        assert os.path.exists(path), f"File {path} does not exist!"

        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "gate_ph",
            "categoryId": "gate_ph",
            "test_type": "MOCK",
            "testType": "MOCK",
            "title": f"GATE Physics (PH) Full Length Mock Test {t:02d} (11-Section Syllabus)",
            "titleEn": f"GATE Physics (PH) Full Length Mock Test {t:02d} (11-Section Syllabus)",
            "titleHi": f"GATE भौतिकी (PH) संपूर्ण मॉक टेस्ट {t:02d} (11-खंड पाठ्यक्रम)",
            "exam_year_tag": f"GATE PH • Full Mock Test {t:02d}",
            "examYearTag": f"GATE PH • Full Mock Test {t:02d}",
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
            "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{path}",
            "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{path}",
            "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/{path}"
        }
        new_gate_ph_tests.append(entry)

    # Add 22 Topic Tests
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
                "title": sub_cfg["title_en"],
                "titleEn": sub_cfg["title_en"],
                "titleHi": sub_cfg["title_hi"],
                "exam_year_tag": sub_cfg["badge"],
                "examYearTag": sub_cfg["badge"],
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
                "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{path}",
                "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{path}",
                "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/{path}"
            }
            new_gate_ph_tests.append(entry)

    print(f"Total gate_ph tests to insert: {len(new_gate_ph_tests)} (4 PYQs + 12 Mocks + 22 Topic Tests)")

    # Find where gate_ph was placed previously or place after previous categories
    # Combine back
    all_tests = non_gate_ph + new_gate_ph_tests
    manifest["tests"] = all_tests

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Successfully updated {manifest_path} with {len(all_tests)} total tests across the entire repository!")

if __name__ == "__main__":
    update_manifest()
