# -*- coding: utf-8 -*-
import json
import re
from collections import OrderedDict
from gate_ph_2026_q01_20 import get_q01_20
from gate_ph_2026_q21_45 import get_q21_45
from gate_ph_2026_q46_65 import get_q46_65

STANDARD_Q_KEYS = [
    "questionId", "questionNumber", "sectionId", "sectionTitle",
    "questionType", "positiveMarks", "negativeMarks", "pyqTag",
    "topicTag", "difficulty", "correctOption", "correctOptionsList",
    "correct_index", "correct_indices", "natMin", "natMax",
    "questionTextEn", "optionsEn", "explanationEn"
]

def load_official_keys():
    txt = open("temp_gate_pdfs/gate_ph_2026_key.txt", encoding="utf-8").read()
    keys = {}
    for line in txt.splitlines():
        m = re.match(r'^(\d+)\s+2\s+(MCQ|MSQ|NAT)\s+(?:GA|PH)\s+(.+?)\s+(\d+)\s*$', line.strip())
        if m:
            keys[int(m.group(1))] = {
                "type": m.group(2),
                "key": m.group(3).strip(),
                "marks": float(m.group(4))
            }
    return keys

def build_paper():
    q_map = {}
    q_map.update(get_q01_20())
    q_map.update(get_q21_45())
    q_map.update(get_q46_65())

    assert len(q_map) == 65, f"Expected 65 questions, got {len(q_map)}"
    official_keys = load_official_keys()
    assert len(official_keys) == 65, f"Expected 65 official keys, got {len(official_keys)}"

    sec_map = OrderedDict()
    all_questions = []

    for qn in range(1, 66):
        q = q_map[qn]
        k = official_keys[qn]

        assert q["questionType"] == k["type"], f"Q{qn} type mismatch: {q['questionType']} vs {k['type']}"
        assert q["positiveMarks"] == k["marks"], f"Q{qn} marks mismatch: {q['positiveMarks']} vs {k['marks']}"

        # Key verification
        if k["type"] == "MCQ":
            assert q["correctOption"] == k["key"], f"Q{qn} MCQ key mismatch: {q['correctOption']} vs {k['key']}"
            assert q["correctOptionsList"] == [k["key"]]
            assert len(q["optionsEn"]) == 4
        elif k["type"] == "MSQ":
            exp_keys = [x.strip() for x in k["key"].split(";")]
            assert q["correctOptionsList"] == exp_keys, f"Q{qn} MSQ key mismatch: {q['correctOptionsList']} vs {exp_keys}"
            assert len(q["optionsEn"]) == 4
        elif k["type"] == "NAT":
            p = k["key"].split(" to ")
            nmin, nmax = float(p[0]), float(p[1])
            assert abs(q["natMin"] - nmin) < 1e-4, f"Q{qn} NAT min mismatch: {q['natMin']} vs {nmin}"
            assert abs(q["natMax"] - nmax) < 1e-4, f"Q{qn} NAT max mismatch: {q['natMax']} vs {nmax}"
            assert q["correctOptionsList"] == []
            assert q["optionsEn"] == []

        # Standardize questionId and pyqTag
        q["questionId"] = f"gate_ph_2026_q{qn:02d}"
        q["pyqTag"] = "GATE PH 2026 Official Paper"

        # Check explanation
        exp = q["explanationEn"]
        assert len(exp.strip()) > 50, f"Q{qn} explanation too short or missing!"
        assert "Official GATE" not in exp or "range:" in exp or "Key:" in exp

        # Strict 19-key dict
        clean_q = OrderedDict((k, q[k]) for k in STANDARD_Q_KEYS)
        all_questions.append(clean_q)

        sid = clean_q["sectionId"]
        stitle = clean_q["sectionTitle"]
        if sid not in sec_map:
            sec_map[sid] = {
                "sectionId": sid,
                "sectionTitle": stitle,
                "sectionTitleEn": stitle,
                "questionCount": 0,
                "totalMarks": 0.0
            }
        sec_map[sid]["questionCount"] += 1
        sec_map[sid]["totalMarks"] = round(sec_map[sid]["totalMarks"] + float(clean_q["positiveMarks"]), 2)

    total_marks = sum(q["positiveMarks"] for q in all_questions)
    assert abs(total_marks - 100.0) < 1e-4, f"Total marks must be 100.0, got {total_marks}"

    paper = {
        "testId": "gate_ph_pyq_2026",
        "categoryId": "gate_ph",
        "test_id": "gate_ph_pyq_2026",
        "category_id": "gate_ph",
        "title": "GATE 2026 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
        "titleEn": "GATE 2026 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
        "testType": "PYQ",
        "test_type": "PYQ",
        "isFree": False,
        "is_free": False,
        "durationMinutes": 180,
        "duration_minutes": 180,
        "totalQuestions": 65,
        "total_questions": 65,
        "maxMarks": 100.0,
        "positiveMarks": 2.0,
        "negativeMarks": 0.33,
        "examYear": 2026,
        "shiftBadge": "GATE PH • 2026 Official Paper",
        "sections": list(sec_map.values()),
        "questions": all_questions
    }

    out_path = "tests/gate/gate_ph/pyq/gate_ph_pyq_2026.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(paper, f, indent=2, ensure_ascii=False)

    print(f"✅ Successfully wrote {out_path} ({len(all_questions)} Qs, {total_marks} marks)")

if __name__ == "__main__":
    build_paper()
