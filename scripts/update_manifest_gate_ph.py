import json
import os

manifest_path = "manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# 1. Update categories
for cat in manifest.get("categories", []):
    if cat.get("id") == "gate_ph":
        cat["subtitle"] = "Authentic Official Master PYQs (2024, 2023, 2022) + Full Mocks + Topic Tests"
        break

# 2. Define new gate_ph PYQ entries
pyq_2024 = {
    "test_id": "gate_ph_pyq_2024",
    "testId": "gate_ph_pyq_2024",
    "category_id": "gate_ph",
    "categoryId": "gate_ph",
    "test_type": "PYQ",
    "testType": "PYQ",
    "title": "GATE 2024 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
    "titleEn": "GATE 2024 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
    "titleHi": "GATE 2024 भौतिकी (PH) आधिकारिक हल प्रश्न पत्र",
    "exam_year_tag": "GATE PH • 2024 Official Paper",
    "examYearTag": "GATE PH • 2024 Official Paper",
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
    "path": "tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json",
    "json_url": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json",
    "cdnUrl": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json",
    "altCdnUrl": "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json"
}

pyq_2023 = {
    "test_id": "gate_ph_pyq_2023",
    "testId": "gate_ph_pyq_2023",
    "category_id": "gate_ph",
    "categoryId": "gate_ph",
    "test_type": "PYQ",
    "testType": "PYQ",
    "title": "GATE 2023 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
    "titleEn": "GATE 2023 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
    "titleHi": "GATE 2023 भौतिकी (PH) आधिकारिक हल प्रश्न पत्र",
    "exam_year_tag": "GATE PH • 2023 Official Paper",
    "examYearTag": "GATE PH • 2023 Official Paper",
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
    "path": "tests/gate/gate_ph/pyq/gate_ph_pyq_2023.json",
    "json_url": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2023.json",
    "cdnUrl": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2023.json",
    "altCdnUrl": "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2023.json"
}

pyq_2022 = {
    "test_id": "gate_ph_pyq_2022",
    "testId": "gate_ph_pyq_2022",
    "category_id": "gate_ph",
    "categoryId": "gate_ph",
    "test_type": "PYQ",
    "testType": "PYQ",
    "title": "GATE 2022 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
    "titleEn": "GATE 2022 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
    "titleHi": "GATE 2022 भौतिकी (PH) आधिकारिक हल प्रश्न पत्र",
    "exam_year_tag": "GATE PH • 2022 Official Paper",
    "examYearTag": "GATE PH • 2022 Official Paper",
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
    "path": "tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json",
    "json_url": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json",
    "cdnUrl": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json",
    "altCdnUrl": "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json"
}

# 3. Rebuild tests list
new_tests = []
gate_ph_pyqs_added = False

for t in manifest.get("tests", []):
    tid = t.get("test_id") or t.get("testId")
    if tid == "gate_ph_pyq_2025":
        # Skip fake paper
        continue
    if tid == "gate_ph_pyq_2024":
        # Add 2024, 2023, 2022 in order
        new_tests.append(pyq_2024)
        new_tests.append(pyq_2023)
        new_tests.append(pyq_2022)
        gate_ph_pyqs_added = True
        continue
    if tid in ("gate_ph_pyq_2023", "gate_ph_pyq_2022"):
        # Skip if already exists elsewhere to avoid duplicate
        continue
    new_tests.append(t)

if not gate_ph_pyqs_added:
    new_tests.extend([pyq_2024, pyq_2023, pyq_2022])

manifest["tests"] = new_tests

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print("SUCCESS: Updated manifest.json with authentic GATE PH PYQs (2024, 2023, 2022) and removed fake 2025.")
