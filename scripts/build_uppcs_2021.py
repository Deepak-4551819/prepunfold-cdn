#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_2021.py — Builds authentic 150-Q GS1 and 100-Q CSAT for UPPSC PCS Prelims 2021."""
import json
import os

def create_q(test_prefix, q_num, sec_id, sec_title, topic, diff, opt_letter, pos_marks, neg_marks, pyq_tag, q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi):
    letter_to_idx = {"A": 0, "B": 1, "C": 2, "D": 3}
    idx = letter_to_idx[opt_letter.upper()]
    return {
        "questionId": f"{test_prefix}_q{q_num:03d}",
        "questionNumber": q_num,
        "sectionId": sec_id,
        "sectionTitle": sec_title,
        "questionType": "MCQ",
        "positiveMarks": pos_marks,
        "negativeMarks": neg_marks,
        "pyqTag": pyq_tag,
        "topicTag": topic,
        "difficulty": diff,
        "correctOption": opt_letter.upper(),
        "correctOptionsList": [opt_letter.upper()],
        "correct_index": idx,
        "correct_indices": [idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": q_en,
        "optionsEn": opts_en,
        "explanationEn": exp_en,
        "questionTextHi": q_hi,
        "optionsHi": opts_hi,
        "explanationHi": exp_hi
    }

print("Loaded 2021 generator helper.")
