# -*- coding: utf-8 -*-
import json
import os
from gate_ph_2021_part1 import get_questions_part1
from gate_ph_2021_part2 import get_questions_part2

def build_gate_ph_2021():
    q1 = get_questions_part1()
    q2 = get_questions_part2()
    all_questions = q1 + q2

    print(f"Total gathered 2021 questions: {len(all_questions)}")
    assert len(all_questions) == 65, f"Expected 65 questions, got {len(all_questions)}"

    total_marks = 0.0
    for idx, q in enumerate(all_questions, 1):
        assert q["questionNumber"] == idx, f"Question number mismatch at index {idx}: {q['questionNumber']}"
        pos = q.get("positiveMarks", 0.0)
        total_marks += pos
        assert "questionTextEn" in q and len(q["questionTextEn"]) > 0
        assert "questionTextHi" in q and len(q["questionTextHi"]) > 0
        assert "explanationEn" in q and len(q["explanationEn"]) > 0
        assert "explanationHi" in q and len(q["explanationHi"]) > 0
        if q["questionType"] in ("MCQ", "MSQ"):
            assert len(q["optionsEn"]) == 4, f"Q{idx} ({q['questionType']}) must have 4 options"
            assert len(q["optionsHi"]) == 4, f"Q{idx} ({q['questionType']}) must have 4 Hindi options"

    print(f"Total calculated marks: {total_marks}")
    assert abs(total_marks - 100.0) < 1e-4, f"Expected 100.0 marks, got {total_marks}"

    paper_data = {
        "testId": "gate_ph_pyq_2021",
        "categoryId": "gate_ph",
        "test_id": "gate_ph_2021",
        "category_id": "gate_ph",
        "title": "GATE 2021 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
        "titleEn": "GATE 2021 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
        "titleHi": "GATE 2021 भौतिकी (PH) आधिकारिक हल प्रश्न पत्र",
        "testType": "PYQ",
        "test_type": "PYQ",
        "isFree": True,
        "is_free": True,
        "durationMinutes": 180,
        "duration_minutes": 180,
        "totalQuestions": 65,
        "total_questions": 65,
        "maxMarks": 100.0,
        "positiveMarks": 2.0,
        "negativeMarks": 0.33,
        "examYear": 2021,
        "shiftBadge": "GATE PH • 2021 Official Paper",
        "questions": all_questions
    }

    out_dir = "tests/gate/gate_ph/pyq"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "gate_ph_pyq_2021.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(paper_data, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: Wrote {out_file} ({os.path.getsize(out_file)} bytes).")

if __name__ == "__main__":
    build_gate_ph_2021()
