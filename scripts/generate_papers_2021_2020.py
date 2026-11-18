#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/generate_papers_2021_2020.py — Generates complete authentic 2021 and 2020 UPPCS papers."""
import json, os

def make_mcq(q_id, q_num, sec_id, sec_title, pos, neg, tag, topic, diff, ans, en_stem, en_opts, en_exp, hi_stem, hi_opts, hi_exp):
    idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx = idx_map[ans.upper()]
    return {
        "questionId": q_id,
        "questionNumber": q_num,
        "sectionId": sec_id,
        "sectionTitle": sec_title,
        "questionType": "MCQ",
        "positiveMarks": pos,
        "negativeMarks": neg,
        "pyqTag": tag,
        "topicTag": topic,
        "difficulty": diff,
        "correctOption": ans.upper(),
        "correctOptionsList": [ans.upper()],
        "correct_index": idx,
        "correct_indices": [idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": en_stem,
        "optionsEn": en_opts,
        "explanationEn": en_exp,
        "questionTextHi": hi_stem,
        "optionsHi": hi_opts,
        "explanationHi": hi_exp
    }

def save_paper(test_id, title_en, title_hi, year, is_gs, qs, out_path):
    tot = len(qs)
    pos = 1.33 if is_gs else 2.0
    neg = 0.44 if is_gs else 0.66
    paper_type = "GS-1" if is_gs else "CSAT Paper-2"
    data = {
        "testId": test_id,
        "categoryId": "uppcs_pre",
        "test_id": test_id,
        "category_id": "uppcs_pre",
        "title": f"{title_en} (Full {tot} Qs)",
        "titleEn": f"{title_en} (Full {tot} Qs)",
        "titleHi": f"{title_hi} (पूर्ण {tot} प्रश्न)",
        "testType": "PYQ",
        "test_type": "PYQ",
        "isFree": True,
        "is_free": True,
        "durationMinutes": 120,
        "duration_minutes": 120,
        "totalQuestions": tot,
        "total_questions": tot,
        "maxMarks": 200.0,
        "positiveMarks": pos,
        "negativeMarks": neg,
        "examYear": year,
        "shiftBadge": f"UPPCS Prelims {year} • {paper_type} (Full {tot} Qs)",
        "questions": qs,
        "path": out_path.replace("\\", "/")
    }
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {test_id} ({tot} Qs) to {out_path}")

print("Helper functions ready.")
