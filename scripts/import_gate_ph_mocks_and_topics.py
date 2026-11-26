# -*- coding: utf-8 -*-
"""
Removes all previous GATE PH full mocks and topic tests, and imports/normalizes
the new 10 Full Mocks and 20 Topic Tests from gate_ph_mocks_and_topic_tests.zip.
"""

import os
import sys
import json
import shutil
import zipfile
from collections import OrderedDict

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ph_mocks_and_topic_tests.zip"
FULL_MOCKS_DIR = "tests/gate/gate_ph/full_mocks"
TOPIC_TESTS_DIR = "tests/gate/gate_ph/topic_tests"

DIFF_MAP = {
    "EASY": "Easy", "Easy": "Easy",
    "MODERATE": "Medium", "MEDIUM": "Medium", "Medium": "Medium",
    "HARD": "Hard", "Hard": "Hard",
}

def normalize_test(raw_data: dict, is_mock: bool) -> dict:
    tid = raw_data["testId"]
    ttype = "FULL_MOCK" if is_mock else "TOPIC"
    questions = raw_data["questions"]

    if is_mock:
        num = int(tid.split("_")[-1])
        pyq_tag = f"GATE PH Mock {num:02d}"
        shift_badge = raw_data.get("shiftBadge") or f"GATE PH • Full Mock {num:02d}"
    else:
        part_title = raw_data["partTitle"]
        set_num = int(tid.split("_")[-1])
        pyq_tag = f"GATE PH Topic • {part_title} (Set {set_num})"
        shift_badge = raw_data.get("shiftBadge") or f"GATE PH • {part_title} • Set {set_num}"

    # Build sections dynamically preserving first-seen order
    sec_map = OrderedDict()
    for q in questions:
        sid = q["sectionId"]
        stitle = q["sectionTitle"]
        if sid not in sec_map:
            sec_map[sid] = {"sectionId": sid, "sectionTitle": stitle, "sectionTitleEn": stitle, "questionCount": 0, "totalMarks": 0.0}
        sec_map[sid]["questionCount"] += 1
        sec_map[sid]["totalMarks"] = round(sec_map[sid]["totalMarks"] + float(q["positiveMarks"]), 2)
    sections = list(sec_map.values())

    norm_questions = []
    for q in questions:
        qt = q["questionType"]
        diff = DIFF_MAP.get(q.get("difficulty", "Medium"), "Medium")
        pos = float(q["positiveMarks"])
        neg = float(q["negativeMarks"])

        if qt == "MCQ":
            co = q["correctOption"]
            ci = int(q["correct_index"])
            col = [co]
            cis = [ci]
            nmin, nmax = None, None
            opts_en = list(q["optionsEn"])
            if pos == 2.0 and neg == 0.66:
                neg = 0.67
        elif qt == "MSQ":
            co = None
            ci = None
            col = list(q["correctOptionsList"])
            cis = list(q["correct_indices"])
            nmin, nmax = None, None
            opts_en = list(q["optionsEn"])
        elif qt == "NAT":
            nmin = float(q["natMin"])
            nmax = float(q["natMax"])
            co = q.get("correctOption")
            if co is None:
                if nmin == nmax:
                    co = str(int(nmin)) if nmin.is_integer() else str(nmin)
                else:
                    co = f"{nmin} to {nmax}"
            else:
                co = str(co)
            ci = None
            col = []
            cis = []
            opts_en = []
        else:
            raise ValueError(f"Unknown questionType {qt} in {tid}")

        nq = {
            "questionId": q["questionId"],
            "questionNumber": int(q["questionNumber"]),
            "sectionId": q["sectionId"],
            "sectionTitle": q["sectionTitle"],
            "questionType": qt,
            "positiveMarks": pos,
            "negativeMarks": neg,
            "pyqTag": pyq_tag,
            "topicTag": q["topicTag"],
            "difficulty": diff,
            "correctOption": co,
            "correctOptionsList": col,
            "correct_index": ci,
            "correct_indices": cis,
            "natMin": nmin,
            "natMax": nmax,
            "questionTextEn": q["questionTextEn"],
            "optionsEn": opts_en,
            "explanationEn": q["explanationEn"],
        }
        norm_questions.append(nq)

    out = {
        "testId": tid,
        "categoryId": "gate_ph",
        "test_id": tid,
        "category_id": "gate_ph",
        "title": raw_data["title"],
        "titleEn": raw_data["titleEn"],
        "testType": ttype,
        "test_type": ttype,
    }
    if not is_mock:
        out["partId"] = raw_data["partId"]
        out["part_id"] = raw_data["partId"]
        out["partTitle"] = raw_data["partTitle"]

    out.update({
        "isFree": bool(raw_data["isFree"]),
        "is_free": bool(raw_data["isFree"]),
        "durationMinutes": int(raw_data["durationMinutes"]),
        "duration_minutes": int(raw_data["durationMinutes"]),
        "totalQuestions": len(norm_questions),
        "total_questions": len(norm_questions),
        "maxMarks": float(raw_data["maxMarks"]),
        "positiveMarks": float(raw_data["positiveMarks"]),
        "negativeMarks": float(raw_data["negativeMarks"]),
        "examYear": 2027,
        "shiftBadge": shift_badge,
        "sections": sections,
        "questions": norm_questions,
    })
    return out

def main():
    # 1. Remove previous mocks & topic tests
    if os.path.exists(FULL_MOCKS_DIR):
        shutil.rmtree(FULL_MOCKS_DIR)
        print(f"🗑️ Removed old directory: {FULL_MOCKS_DIR}")
    if os.path.exists(TOPIC_TESTS_DIR):
        shutil.rmtree(TOPIC_TESTS_DIR)
        print(f"🗑️ Removed old directory: {TOPIC_TESTS_DIR}")

    os.makedirs(FULL_MOCKS_DIR, exist_ok=True)
    os.makedirs(TOPIC_TESTS_DIR, exist_ok=True)

    mock_count = 0
    topic_count = 0

    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        for name in sorted(z.namelist()):
            if not name.endswith(".json"):
                continue
            raw = json.loads(z.read(name).decode("utf-8"))
            is_mock = name.startswith("full_mocks/")
            norm = normalize_test(raw, is_mock=is_mock)
            tid = norm["testId"]

            if is_mock:
                out_path = os.path.join(FULL_MOCKS_DIR, f"{tid}.json")
                mock_count += 1
            else:
                part_dir = os.path.join(TOPIC_TESTS_DIR, norm["partId"])
                os.makedirs(part_dir, exist_ok=True)
                out_path = os.path.join(part_dir, f"{tid}.json")
                topic_count += 1

            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(norm, f, ensure_ascii=False, indent=2)

    print(f"✅ Imported {mock_count} full mocks and {topic_count} topic tests cleanly!")

if __name__ == "__main__":
    main()
