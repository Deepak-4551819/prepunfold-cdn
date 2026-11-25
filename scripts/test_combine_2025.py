# -*- coding: utf-8 -*-
from build_2025_part1 import QUESTIONS_2025_PART1
from gate_cs_2025_part2 import QUESTIONS_2025_PART2

all_2025 = QUESTIONS_2025_PART1 + QUESTIONS_2025_PART2
print("Total 2025 questions:", len(all_2025))
assert len(all_2025) == 65, f"Expected 65, got {len(all_2025)}"

total_marks = 0
for idx, q in enumerate(all_2025, 1):
    q_num, q_type, marks, neg, key, opt_keys, n_min, n_max, topic, diff, text_en, opts_en, exp_en, text_hi, opts_hi, exp_hi = q
    assert q_num == idx, f"Mismatch q_num {q_num} != {idx}"
    total_marks += marks
    assert q_type in ["MCQ", "MSQ", "NAT"], f"Invalid q_type {q_type} in Q{q_num}"
    if q_type == "MCQ":
        assert len(opts_en) == 4, f"MCQ Q{q_num} must have 4 opts, got {len(opts_en)}"
        assert len(opts_hi) == 4, f"MCQ Q{q_num} must have 4 hi opts, got {len(opts_hi)}"
        assert key in ["A", "B", "C", "D"], f"Invalid MCQ key {key} in Q{q_num}"
    elif q_type == "MSQ":
        assert len(opts_en) == 4, f"MSQ Q{q_num} must have 4 opts, got {len(opts_en)}"
        assert len(opts_hi) == 4, f"MSQ Q{q_num} must have 4 hi opts, got {len(opts_hi)}"
        assert len(opt_keys) >= 1, f"Empty opt_keys in MSQ Q{q_num}"
    elif q_type == "NAT":
        assert n_min is not None and n_max is not None, f"NAT Q{q_num} missing range"

    assert len(text_en.strip()) > 0, f"Empty text_en in Q{q_num}"
    assert len(text_hi.strip()) > 0, f"Empty text_hi in Q{q_num}"
    assert len(exp_en.strip()) > 0, f"Empty exp_en in Q{q_num}"
    assert len(exp_hi.strip()) > 0, f"Empty exp_hi in Q{q_num}"

print("Total 2025 marks:", total_marks)
assert total_marks == 100.0, f"Expected 100.0 marks, got {total_marks}"
print("All 2025 validations passed successfully!")
