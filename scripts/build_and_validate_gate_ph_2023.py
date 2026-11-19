# -*- coding: utf-8 -*-
import json
import os
import sys

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from generate_full_gate_ph_2023 import create_gate_ph_pyq_2023
from gate_ph_2023_part1 import QUESTIONS_PART1
from gate_ph_2023_part2 import QUESTIONS_PART2

def main():
    part0_tuples = create_gate_ph_pyq_2023()

    all_questions_tuples = part0_tuples + QUESTIONS_PART1 + QUESTIONS_PART2
    print(f"Total question tuples gathered: {len(all_questions_tuples)}")

    if len(all_questions_tuples) != 65:
        print(f"ERROR: Expected 65 questions, got {len(all_questions_tuples)}")
        return

    # Verify numbers 1 to 65
    nums = [t[0] for t in all_questions_tuples]
    if nums != list(range(1, 66)):
        print(f"ERROR: Question numbers mismatch: {nums}")
        return

    opt_map = {"A": 0, "B": 1, "C": 2, "D": 3}
    questions_list = []
    total_marks = 0.0

    for item in all_questions_tuples:
        (q_num, q_type, pos, neg, correct_opt, correct_list, nat_min, nat_max, topic, diff,
         q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi) = item

        sec_id = "sec_ga" if q_num <= 10 else "sec_ph"
        sec_title = "General Aptitude" if q_num <= 10 else "Physics"
        total_marks += pos

        c_idx = opt_map.get(correct_opt) if correct_opt in opt_map else None
        c_indices = [opt_map[o] for o in correct_list if o in opt_map]

        # Validation
        if q_type == "MCQ":
            assert len(opts_en) == 4, f"Q{q_num} must have 4 options"
            assert len(opts_hi) == 4, f"Q{q_num} must have 4 Hindi options"
            assert correct_opt is not None, f"Q{q_num} MCQ must have correctOption"
        elif q_type == "MSQ":
            assert len(opts_en) == 4, f"Q{q_num} must have 4 options"
            assert len(opts_hi) == 4, f"Q{q_num} must have 4 Hindi options"
            assert len(correct_list) >= 1, f"Q{q_num} MSQ must have correctOptionsList"
        elif q_type == "NAT":
            assert opts_en == [], f"Q{q_num} NAT options must be empty"
            assert opts_hi == [], f"Q{q_num} NAT Hindi options must be empty"
            assert nat_min is not None and nat_max is not None, f"Q{q_num} NAT must have range"

        assert len(q_en.strip()) > 10, f"Q{q_num} English text too short"
        assert len(q_hi.strip()) > 10, f"Q{q_num} Hindi text too short"
        assert len(exp_en.strip()) > 10, f"Q{q_num} English exp too short"
        assert len(exp_hi.strip()) > 10, f"Q{q_num} Hindi exp too short"

        questions_list.append({
            "questionId": f"gate_ph_2023_q{q_num:02d}",
            "questionNumber": q_num,
            "sectionId": sec_id,
            "sectionTitle": sec_title,
            "questionType": q_type,
            "positiveMarks": pos,
            "negativeMarks": neg,
            "pyqTag": "GATE Physics (PH) • 2023 Official Paper",
            "topicTag": topic,
            "difficulty": diff,
            "correctOption": correct_opt,
            "correctOptionsList": correct_list,
            "correct_index": c_idx,
            "correct_indices": c_indices,
            "natMin": nat_min,
            "natMax": nat_max,
            "questionTextEn": q_en,
            "optionsEn": opts_en,
            "explanationEn": exp_en,
            "questionTextHi": q_hi,
            "optionsHi": opts_hi,
            "explanationHi": exp_hi
        })

    print(f"Total calculated marks: {total_marks}")
    assert total_marks == 100.0, f"Expected 100 marks, got {total_marks}"

    paper = {
        "testId": "gate_ph_pyq_2023",
        "categoryId": "gate_ph",
        "test_id": "gate_ph_pyq_2023",
        "category_id": "gate_ph",
        "title": "GATE 2023 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
        "titleEn": "GATE 2023 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
        "titleHi": "GATE 2023 भौतिकी (PH) आधिकारिक हल प्रश्न पत्र (सभी 9 मुख्य विषय एवं GA)",
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
        "examYear": 2023,
        "shiftBadge": "GATE PH • 2023 Official Paper",
        "questions": questions_list
    }

    out_path = "tests/gate/gate_ph/pyq/gate_ph_pyq_2023.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(paper, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: Wrote {out_path} ({os.path.getsize(out_path)} bytes).")

if __name__ == "__main__":
    main()
