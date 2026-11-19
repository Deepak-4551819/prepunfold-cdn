# -*- coding: utf-8 -*-
"""
Updates manifest.json with all 12 GATE PH Mock Tests (gate_ph_mock_01 to gate_ph_mock_12).
"""
import json
import os

def update_manifest():
    manifest_path = "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    tests_list = manifest.get("tests", [])

    # Create entries for Mock 02 to Mock 12
    for t in range(2, 13):
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
            "title": f"GATE Physics (PH) Full Length Mock Test {t:02d}",
            "titleEn": f"GATE Physics (PH) Full Length Mock Test {t:02d}",
            "titleHi": f"GATE भौतिकी (PH) संपूर्ण मॉक टेस्ट {t:02d}",
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

        # Check if already exists in tests_list
        existing_idx = None
        for i, existing in enumerate(tests_list):
            if existing.get("test_id") == tid or existing.get("testId") == tid:
                existing_idx = i
                break

        if existing_idx is not None:
            tests_list[existing_idx] = entry
            print(f"Updated {tid} in manifest.")
        else:
            # Insert after previous mock if possible
            prev_tid = f"gate_ph_mock_{t-1:02d}"
            prev_idx = None
            for i, existing in enumerate(tests_list):
                if existing.get("test_id") == prev_tid or existing.get("testId") == prev_tid:
                    prev_idx = i
                    break
            if prev_idx is not None:
                tests_list.insert(prev_idx + 1, entry)
            else:
                tests_list.append(entry)
            print(f"Added {tid} to manifest.")

    manifest["tests"] = tests_list

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Successfully updated {manifest_path} with all 12 GATE PH Mock Tests.")

if __name__ == "__main__":
    update_manifest()
