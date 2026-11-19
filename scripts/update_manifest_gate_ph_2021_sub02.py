import json

manifest_path = "manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# 1. Update category gate_ph
for cat in manifest.get("categories", []):
    if cat.get("id") == "gate_ph":
        cat["subtitle"] = "Official Master PYQs (2024–2021) + 12 Full Mocks + Topic Tests"
        break

# 2. Entries to add
pyq_2021 = {
    "test_id": "gate_ph_pyq_2021",
    "testId": "gate_ph_pyq_2021",
    "category_id": "gate_ph",
    "categoryId": "gate_ph",
    "test_type": "PYQ",
    "testType": "PYQ",
    "title": "GATE 2021 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
    "titleEn": "GATE 2021 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
    "titleHi": "GATE 2021 भौतिकी (PH) आधिकारिक हल प्रश्न पत्र",
    "exam_year_tag": "GATE PH • 2021 Official Paper",
    "examYearTag": "GATE PH • 2021 Official Paper",
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
    "path": "tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json",
    "json_url": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json",
    "cdnUrl": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json",
    "altCdnUrl": "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json"
}

sub_02 = {
    "test_id": "gate_ph_sub_02",
    "testId": "gate_ph_sub_02",
    "category_id": "gate_ph",
    "categoryId": "gate_ph",
    "test_type": "TOPIC_TEST",
    "testType": "TOPIC_TEST",
    "title": "GATE PH Subtopic Test: Classical Mechanics — Lagrangian, Hamiltonian & Rigid Body Dynamics",
    "titleEn": "GATE PH Subtopic Test: Classical Mechanics — Lagrangian, Hamiltonian & Rigid Body Dynamics",
    "titleHi": "GATE PH उप-विषय टेस्ट: चिरसम्मत यांत्रिकी — लैग्रेंजियन, हैमिल्टोनियन एवं दृढ़ पिण्ड गतिविज्ञान",
    "exam_year_tag": "Classical Mechanics 1",
    "examYearTag": "Classical Mechanics 1",
    "duration_minutes": 90,
    "durationMinutes": 90,
    "total_questions": 30,
    "totalQuestions": 30,
    "positive_marks": 2.0,
    "positiveMarks": 2.0,
    "negative_marks": 0.33,
    "negativeMarks": 0.33,
    "is_free": True,
    "isFree": True,
    "version": 1,
    "path": "tests/gate/gate_ph/topic_tests/02_classical_mechanics/sub_02_lagrangian_hamiltonian_rigid_body.json",
    "json_url": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/topic_tests/02_classical_mechanics/sub_02_lagrangian_hamiltonian_rigid_body.json",
    "cdnUrl": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/gate/gate_ph/topic_tests/02_classical_mechanics/sub_02_lagrangian_hamiltonian_rigid_body.json",
    "altCdnUrl": "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/gate/gate_ph/topic_tests/02_classical_mechanics/sub_02_lagrangian_hamiltonian_rigid_body.json"
}

# 3. Update tests list
new_tests = []
for t in manifest.get("tests", []):
    tid = t.get("test_id") or t.get("testId")
    if tid == "gate_ph_pyq_2021" or tid == "gate_ph_sub_02":
        continue
    new_tests.append(t)
    if tid == "gate_ph_pyq_2022":
        # Insert 2021 right after 2022
        new_tests.append(pyq_2021)
    elif tid == "gate_ph_sub_01":
        # Insert sub_02 right after sub_01
        new_tests.append(sub_02)

manifest["tests"] = new_tests

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print("SUCCESS: Updated manifest.json with gate_ph_pyq_2021 and gate_ph_sub_02.")
