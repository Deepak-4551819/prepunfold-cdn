# -*- coding: utf-8 -*-
"""
Imports and normalizes GATE CS Full Mocks (10) and Topic Tests (22) from
gate_cs_mocks_and_topic_tests.zip to match the repository's English-only
GATE CS / GATE PH JSON schema, balances MCQ/MSQ option positions safely,
updates manifest.json (including gate_cs parts[]), and updates seen_question_hashes.json.
"""

import os
import re
import sys
import json
import random
import hashlib
import zipfile
from collections import Counter

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_cs_mocks_and_topic_tests.zip"
MANIFEST_PATH = "manifest.json"
SEEN_HASHES_PATH = "seen_question_hashes.json"
BASE_CDN_URL = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main"
ALT_CDN_URL = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main"

DIFF_MAP = {
    "EASY": "Easy",
    "Easy": "Easy",
    "MODERATE": "Medium",
    "MEDIUM": "Medium",
    "Medium": "Medium",
    "HARD": "Hard",
    "Hard": "Hard",
}

GATE_CS_PARTS = [
    {"partId": "part_01_ga", "partTitleEn": "Section 1: General Aptitude", "order": 1, "topicCount": 2, "questionCount": 40},
    {"partId": "part_02_em", "partTitleEn": "Section 2: Engineering & Discrete Mathematics", "order": 2, "topicCount": 2, "questionCount": 40},
    {"partId": "part_03_dl", "partTitleEn": "Section 3: Digital Logic", "order": 3, "topicCount": 2, "questionCount": 40},
    {"partId": "part_04_coa", "partTitleEn": "Section 4: Computer Organization & Architecture", "order": 4, "topicCount": 2, "questionCount": 40},
    {"partId": "part_05_pds", "partTitleEn": "Section 5: Programming & Data Structures", "order": 5, "topicCount": 2, "questionCount": 40},
    {"partId": "part_06_algo", "partTitleEn": "Section 6: Algorithms", "order": 6, "topicCount": 2, "questionCount": 40},
    {"partId": "part_07_toc", "partTitleEn": "Section 7: Theory of Computation", "order": 7, "topicCount": 2, "questionCount": 40},
    {"partId": "part_08_cd", "partTitleEn": "Section 8: Compiler Design", "order": 8, "topicCount": 2, "questionCount": 40},
    {"partId": "part_09_os", "partTitleEn": "Section 9: Operating Systems", "order": 9, "topicCount": 2, "questionCount": 40},
    {"partId": "part_10_dbms", "partTitleEn": "Section 10: Databases (DBMS)", "order": 10, "topicCount": 2, "questionCount": 40},
    {"partId": "part_11_cn", "partTitleEn": "Section 11: Computer Networks", "order": 11, "topicCount": 2, "questionCount": 40},
]

POS_OPT_PAT = re.compile(
    r"\b(above|below|neither|both\s*\(|all of these|all of the|none of the|none of these|option\s+[abcd])\b",
    re.IGNORECASE,
)
EXP_LETTER_PAT = re.compile(
    r"(\bOption\s+[ABCD]\b|\([ABCD]\)|\b[ABCD]\s+(?:is|are)\s+(?:true|false|correct|incorrect|valid|invalid)|"
    r"\b[ABCD],\s*[ABCD]|\b[ABCD]\s+and\s+[ABCD]\b|(?:options?|choices?|statements?)\s+[ABCD]\b)",
    re.IGNORECASE,
)


def compute_hash(text: str) -> str:
    norm = re.sub(r"\s+", " ", text.strip().lower())
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]


def can_shuffle_options(q: dict) -> bool:
    qt = q.get("questionType")
    opts = q.get("optionsEn") or []
    if qt not in ("MCQ", "MSQ") or len(opts) != 4:
        return False
    joined_opts = " | ".join(opts)
    if POS_OPT_PAT.search(joined_opts):
        return False
    exp = q.get("explanationEn") or ""
    if EXP_LETTER_PAT.search(exp):
        return False
    return True


def shuffle_question_options(q: dict, rng: random.Random) -> dict:
    opts = list(q["optionsEn"])
    perm = [0, 1, 2, 3]
    rng.shuffle(perm)
    new_opts = [opts[i] for i in perm]
    inv = {old_idx: new_idx for new_idx, old_idx in enumerate(perm)}
    letters = ["A", "B", "C", "D"]

    q["optionsEn"] = new_opts
    if q["questionType"] == "MCQ":
        old_idx = q["correct_index"]
        new_idx = inv[old_idx]
        q["correct_index"] = new_idx
        q["correct_indices"] = [new_idx]
        q["correctOption"] = letters[new_idx]
        q["correctOptionsList"] = [letters[new_idx]]
    else:  # MSQ
        new_idxs = sorted(inv[i] for i in q["correct_indices"])
        q["correct_indices"] = new_idxs
        q["correctOptionsList"] = [letters[i] for i in new_idxs]
        q["correctOption"] = None
        q["correct_index"] = None
    return q


def normalize_test(raw_data: dict, is_mock: bool) -> dict:
    tid = raw_data["testId"]
    ttype = "FULL_MOCK" if is_mock else "TOPIC"
    questions = raw_data.get("questions", [])

    if is_mock:
        mock_num = int(tid.split("_")[-1])
        pyq_tag = f"GATE CS • Full Mock {mock_num:02d}"
        shift_badge = f"GATE CS • Full Mock Test {mock_num:02d}"
        ga_qs = [q for q in questions if q.get("sectionId") == "sec_ga"]
        cs_qs = [q for q in questions if q.get("sectionId") != "sec_ga"]
        sections = [
            {
                "sectionId": "sec_ga",
                "sectionTitle": "General Aptitude",
                "sectionTitleEn": "General Aptitude",
                "questionCount": len(ga_qs),
                "totalMarks": round(sum(float(q["positiveMarks"]) for q in ga_qs), 2),
            },
            {
                "sectionId": "sec_cs",
                "sectionTitle": "Computer Science and Information Technology",
                "sectionTitleEn": "Computer Science and Information Technology",
                "questionCount": len(cs_qs),
                "totalMarks": round(sum(float(q["positiveMarks"]) for q in cs_qs), 2),
            },
        ]
    else:
        part_title = raw_data["partTitle"]
        set_num = int(tid.split("_")[-1])
        pyq_tag = f"GATE CS Topic • {part_title} (Set {set_num})"
        shift_badge = raw_data.get("shiftBadge") or f"Topic Set {set_num}"
        sec_id = questions[0]["sectionId"] if questions else f"sec_{raw_data['partId']}"
        sections = [
            {
                "sectionId": sec_id,
                "sectionTitle": part_title,
                "sectionTitleEn": part_title,
                "questionCount": len(questions),
                "totalMarks": round(sum(float(q["positiveMarks"]) for q in questions), 2),
            }
        ]

    norm_questions = []
    for q in questions:
        qt = q["questionType"]
        diff = DIFF_MAP.get(q.get("difficulty", "Medium"), "Medium")
        if qt == "MCQ":
            co = q["correctOption"]
            ci = int(q["correct_index"])
            col = [co]
            cis = [ci]
            nmin, nmax = None, None
            opts_en = list(q["optionsEn"])
        elif qt == "MSQ":
            co = None
            ci = None
            col = list(q["correctOptionsList"])
            cis = list(q["correct_indices"])
            nmin, nmax = None, None
            opts_en = list(q["optionsEn"])
        elif qt == "NAT":
            co = None
            ci = None
            col = []
            cis = []
            nmin = float(q["natMin"])
            nmax = float(q["natMax"])
            opts_en = []
        else:
            raise ValueError(f"Unknown questionType {qt} in {tid}")

        nq = {
            "questionId": q["questionId"],
            "questionNumber": int(q["questionNumber"]),
            "sectionId": q["sectionId"],
            "sectionTitle": q["sectionTitle"],
            "questionType": qt,
            "positiveMarks": float(q["positiveMarks"]),
            "negativeMarks": float(q["negativeMarks"]),
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

        if can_shuffle_options(nq):
            rng = random.Random(nq["questionId"])
            nq = shuffle_question_options(nq, rng)

        norm_questions.append(nq)

    out = {
        "testId": tid,
        "categoryId": "gate_cs",
        "test_id": tid,
        "category_id": "gate_cs",
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


def remove_empty_legacy_dirs():
    legacy_dirs = [
        "tests/gate/gate_cs/mock_tests",
        "tests/gate/gate_cs/topic_tests/01_engineering_and_discrete_maths",
        "tests/gate/gate_cs/topic_tests/02_digital_logic_and_coa",
        "tests/gate/gate_cs/topic_tests/03_programming_ds_and_algorithms",
        "tests/gate/gate_cs/topic_tests/04_toc_and_compiler_design",
        "tests/gate/gate_cs/topic_tests/05_os_dbms_and_computer_networks",
    ]
    for d in legacy_dirs:
        if os.path.isdir(d) and not os.listdir(d):
            os.rmdir(d)
            print(f"[CLEANUP] Removed empty legacy dir: {d}")


def main():
    os.makedirs("tests/gate/gate_cs/full_mocks", exist_ok=True)
    for part in GATE_CS_PARTS:
        os.makedirs(f"tests/gate/gate_cs/topic_tests/{part['partId']}", exist_ok=True)

    remove_empty_legacy_dirs()

    with open(SEEN_HASHES_PATH, "r", encoding="utf-8") as f:
        seen_hashes = json.load(f)

    # Remove any prior mock/topic hashes if re-running
    seen_hashes = {
        k: v for k, v in seen_hashes.items()
        if not (isinstance(v, dict) and v.get("categoryId") == "gate_cs" and (
            v.get("testId", "").startswith("gate_cs_mock_") or v.get("testId", "").startswith("gate_cs_topic_")
        ))
    }

    mcq_dist = Counter()
    msq_dist = Counter()
    mock_entries = []
    topic_entries = []
    new_hash_count = 0

    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        names = sorted([n for n in z.namelist() if n.endswith(".json")])
        for name in names:
            raw_data = json.loads(z.read(name).decode("utf-8"))
            is_mock = name.startswith("full_mocks/")
            norm_data = normalize_test(raw_data, is_mock=is_mock)
            tid = norm_data["testId"]

            if is_mock:
                rel_path = f"tests/gate/gate_cs/full_mocks/{tid}.json"
            else:
                part_id = norm_data["partId"]
                rel_path = f"tests/gate/gate_cs/topic_tests/{part_id}/{tid}.json"

            with open(rel_path, "w", encoding="utf-8") as f:
                json.dump(norm_data, f, ensure_ascii=False, indent=2)

            for q in norm_data["questions"]:
                if q["questionType"] == "MCQ":
                    mcq_dist[q["correctOption"]] += 1
                elif q["questionType"] == "MSQ":
                    msq_dist[tuple(q["correctOptionsList"])] += 1
                h = compute_hash(q["questionTextEn"])
                if h not in seen_hashes:
                    seen_hashes[h] = {
                        "questionId": q["questionId"],
                        "testId": tid,
                        "categoryId": "gate_cs",
                        "topicTag": q["topicTag"],
                    }
                    new_hash_count += 1

            entry = {
                "test_id": tid,
                "testId": tid,
                "category_id": "gate_cs",
                "categoryId": "gate_cs",
                "test_type": norm_data["testType"],
                "testType": norm_data["testType"],
                "title": norm_data["title"],
                "titleEn": norm_data["titleEn"],
                "exam_year_tag": "2027",
                "examYearTag": "2027",
                "shiftBadge": norm_data["shiftBadge"],
                "duration_minutes": norm_data["durationMinutes"],
                "durationMinutes": norm_data["durationMinutes"],
                "total_questions": norm_data["totalQuestions"],
                "totalQuestions": norm_data["totalQuestions"],
                "positive_marks": norm_data["positiveMarks"],
                "positiveMarks": norm_data["positiveMarks"],
                "negative_marks": norm_data["negativeMarks"],
                "negativeMarks": norm_data["negativeMarks"],
                "is_free": norm_data["isFree"],
                "isFree": norm_data["isFree"],
                "version": 1,
                "path": rel_path,
                "filePath": rel_path,
                "file_path": rel_path,
                "json_url": f"{BASE_CDN_URL}/{rel_path}",
                "cdnUrl": f"{BASE_CDN_URL}/{rel_path}",
                "altCdnUrl": f"{ALT_CDN_URL}/{rel_path}",
            }
            if not is_mock:
                entry["part_id"] = norm_data["partId"]
                entry["partId"] = norm_data["partId"]
                topic_entries.append(entry)
            else:
                mock_entries.append(entry)

    # Sort topic_entries by part order then test_id
    part_order = {p["partId"]: p["order"] for p in GATE_CS_PARTS}
    topic_entries.sort(key=lambda e: (part_order.get(e["partId"], 99), e["testId"]))

    # Update manifest.json
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    manifest["manifest_version"] = int(manifest.get("manifest_version", 34)) + 1

    for cat in manifest.get("categories", []):
        if cat.get("id") == "gate_cs" or cat.get("categoryId") == "gate_cs":
            cat["subtitle"] = "8 Official PYQs (2022–2026) + 10 Full Length Mocks + 22 Topic-Wise Tests"
            cat["descriptionEn"] = cat["subtitle"]
            cat["descriptionHi"] = cat["subtitle"]
            cat["parts"] = GATE_CS_PARTS
            cat["totalTests"] = 40
            cat["totalQuestions"] = 1610
            break

    tests = manifest.get("tests", [])
    existing_cs_pyqs = [
        t for t in tests
        if (t.get("category_id") == "gate_cs" or t.get("categoryId") == "gate_cs")
        and (t.get("test_type") == "PYQ" or t.get("testType") == "PYQ")
    ]
    first_cs_idx = next(
        (i for i, t in enumerate(tests) if (t.get("category_id") == "gate_cs" or t.get("categoryId") == "gate_cs")),
        len(tests),
    )
    non_cs_before = [
        t for t in tests[:first_cs_idx]
        if (t.get("category_id") != "gate_cs" and t.get("categoryId") != "gate_cs")
    ]
    non_cs_after = [
        t for t in tests[first_cs_idx:]
        if (t.get("category_id") != "gate_cs" and t.get("categoryId") != "gate_cs")
    ]
    manifest["tests"] = non_cs_before + mock_entries + existing_cs_pyqs + topic_entries + non_cs_after

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    with open(SEEN_HASHES_PATH, "w", encoding="utf-8") as f:
        json.dump(seen_hashes, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(mock_entries)} mocks + {len(topic_entries)} topic tests.")
    print(f"Post-balance MCQ correctOption distribution: {dict(mcq_dist)}")
    print(f"Post-balance MSQ combos: {dict(msq_dist)}")
    print(f"Updated manifest.json (version={manifest['manifest_version']}, totalTests={len(manifest['tests'])})")
    print(f"Updated seen_question_hashes.json (+{new_hash_count} hashes, total={len(seen_hashes)})")


if __name__ == "__main__":
    main()
