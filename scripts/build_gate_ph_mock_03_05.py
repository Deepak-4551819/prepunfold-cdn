# -*- coding: utf-8 -*-
"""
Builder for GATE PH Mock Tests 03, 04, and 05.
Each mock test contains 65 authentic, non-repetitive graduate-level GATE questions:
- Q1 to Q10: General Aptitude (15 marks)
- Q11 to Q35: Physics 1-mark (25 marks)
- Q36 to Q65: Physics 2-mark (60 marks: 15 MCQ, 5 MSQ, 10 NAT)
Total: 65 questions, 100.0 marks.
"""

import json
import os

def create_mock(test_num, title_en, title_hi, questions):
    assert len(questions) == 65, f"Mock {test_num} must have 65 questions, got {len(questions)}"
    total_marks = 0.0
    for idx, q in enumerate(questions, 1):
        assert q["questionNumber"] == idx, f"Mock {test_num} Q{idx} number mismatch"
        total_marks += q["positiveMarks"]
    assert abs(total_marks - 100.0) < 1e-4, f"Mock {test_num} total marks must be 100.0, got {total_marks}"

    test_id = f"gate_ph_mock_{test_num:02d}"
    data = {
        "testId": test_id,
        "categoryId": "gate_ph",
        "test_id": test_id,
        "category_id": "gate_ph",
        "title": title_en,
        "titleEn": title_en,
        "titleHi": title_hi,
        "testType": "MOCK",
        "test_type": "MOCK",
        "isFree": True,
        "is_free": True,
        "durationMinutes": 180,
        "duration_minutes": 180,
        "totalQuestions": 65,
        "total_questions": 65,
        "maxMarks": 100.0,
        "positiveMarks": 2.0,
        "negativeMarks": 0.33,
        "examYear": 2025,
        "shiftBadge": f"GATE PH • Full Mock Test {test_num:02d}",
        "questions": questions
    }
    out_dir = os.path.join("tests", "gate", "gate_ph", "mock_tests")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{test_id}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Generated {out_path} ({os.path.getsize(out_path)} bytes)")

print("Helper module loaded.")
