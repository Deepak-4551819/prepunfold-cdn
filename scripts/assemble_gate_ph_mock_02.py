# -*- coding: utf-8 -*-
"""
Assembles GATE PH Mock 02 from part 1 and part 2, validates, and writes out JSON.
"""
import os
import json
import sys

from build_gate_ph_mock_02_part1 import get_mock_02_part1
from build_gate_ph_mock_02_part2 import get_mock_02_part2

def assemble_mock_02():
    q_part1 = get_mock_02_part1()
    q_part2 = get_mock_02_part2()

    print(f"Part 1 questions: {len(q_part1)}")
    print(f"Part 2 questions: {len(q_part2)}")

    all_questions = q_part1 + q_part2
    assert len(all_questions) == 65, f"Expected 65 questions, got {len(all_questions)}"

    total_marks = 0.0
    for idx, q in enumerate(all_questions, 1):
        assert q["questionNumber"] == idx, f"Question number mismatch: {q['questionNumber']} != {idx}"
        assert q["questionTextEn"], f"Missing questionTextEn in Q{idx}"
        assert q["questionTextHi"], f"Missing questionTextHi in Q{idx}"
        assert q["explanationEn"], f"Missing explanationEn in Q{idx}"
        assert q["explanationHi"], f"Missing explanationHi in Q{idx}"
        total_marks += q["positiveMarks"]

    print(f"Total calculated positive marks: {total_marks}")
    assert abs(total_marks - 100.0) < 1e-4, f"Total marks must be 100.0, got {total_marks}"

    test_data = {
        "testId": "gate_ph_mock_02",
        "categoryId": "gate_ph",
        "test_id": "gate_ph_mock_02",
        "category_id": "gate_ph",
        "title": "GATE Physics (PH) Full Length Mock Test 02",
        "titleEn": "GATE Physics (PH) Full Length Mock Test 02",
        "titleHi": "GATE भौतिकी (PH) संपूर्ण मॉक टेस्ट 02",
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
        "shiftBadge": "GATE PH • Full Mock Test 02",
        "questions": all_questions
    }

    output_path = os.path.join("tests", "gate", "gate_ph", "mock_tests", "gate_ph_mock_02.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    assemble_mock_02()
