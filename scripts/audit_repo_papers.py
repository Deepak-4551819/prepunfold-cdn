#!/usr/bin/env python3
"""scripts/audit_repo_papers.py — Audits all question papers for QuestionDto compliance, duplicates, and bilingual integrity."""
import json, glob, os, re, sys
from collections import defaultdict

def normalize_stem(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'\d+(\.\d+)?', '<NUM>', text)
    text = re.sub(r'[^a-z<num>\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def audit_all_papers(root_dir="."):
    files = sorted(glob.glob(os.path.join(root_dir, "tests", "*.json")))
    if not files:
        files = sorted(glob.glob(os.path.join(root_dir, "tests", "**", "*.json"), recursive=True))

    global_exact_stems = defaultdict(list)
    print(f"{'Paper ID':<38} | {'Q Count':<9} | {'Exact Dups':<10} | {'Status'}")
    print("-" * 75)

    total_qs = 0
    total_papers = 0
    any_fail = False

    for path in files:
        fname = os.path.basename(path)
        if fname in ("manifest.json", "seen_question_hashes.json"):
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"{fname:<38} | ERROR: Invalid JSON: {e}")
            any_fail = True
            continue

        questions = data.get("questions", [])
        if not questions:
            continue

        total_papers += 1
        test_id = data.get("test_id") or data.get("testId") or fname
        expected = data.get("total_questions") or data.get("totalQuestions") or len(questions)

        exact_seen = set()
        exact_dups = 0
        missing_fields = 0

        for idx, q in enumerate(questions):
            total_qs += 1
            qid = q.get("q_id")
            en = (q.get("question_en") or q.get("questionTextEn") or "").strip()
            hi = (q.get("question_hi") or q.get("questionTextHi") or "").strip()
            corr = q.get("correct_index")
            if corr is None:
                corr = q.get("correctOption")

            if not isinstance(qid, int) or not en or not hi or corr is None:
                missing_fields += 1

            exact_key = re.sub(r'\s+', ' ', en.lower())
            if exact_key in exact_seen:
                exact_dups += 1
            exact_seen.add(exact_key)
            global_exact_stems[exact_key].append(test_id)

        status = "OK" if (len(questions) == expected and exact_dups == 0 and missing_fields == 0) else "NEEDS FIX"
        if status != "OK":
            any_fail = True
        print(f"{test_id:<38} | {len(questions):>3}/{expected:<5} | {exact_dups:<10} | {status} (missing={missing_fields})")

    print("-" * 75)
    print(f"Total Papers Audited: {total_papers} | Total Questions: {total_qs}")
    return not any_fail

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    ok = audit_all_papers(target)
    sys.exit(0 if ok else 1)
