import json, os, glob

ROOT = "tests/teaching/tgt_pgt_history"
files = glob.glob(f"{ROOT}/**/*.json", recursive=True)

print(f"Verifying {len(files)} files in {ROOT}...")
assert len(files) == 30, f"Expected 30 files, found {len(files)}"

total_qs = 0
errors = []

for fp in sorted(files):
    rel = os.path.relpath(fp, ROOT)
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)

    req_keys = [
        "testId", "categoryId", "test_id", "category_id", "title", "titleEn", "titleHi",
        "testType", "test_type", "isFree", "is_free", "durationMinutes", "duration_minutes",
        "totalQuestions", "total_questions", "maxMarks", "positiveMarks", "negativeMarks",
        "shiftBadge", "questions"
    ]
    for k in req_keys:
        if k not in data:
            errors.append(f"{rel}: Missing top-level key {k}")

    qs = data.get("questions", [])
    if len(qs) == 0:
        errors.append(f"{rel}: Has 0 questions!")
    if len(qs) != data.get("totalQuestions"):
        errors.append(f"{rel}: totalQuestions ({data.get('totalQuestions')}) != len(questions) ({len(qs)})")

    q_ids = set()
    for q_idx, q in enumerate(qs, 1):
        total_qs += 1
        qid = q.get("questionId")
        if not qid:
            errors.append(f"{rel} Q{q_idx}: missing questionId")
        elif qid in q_ids:
            errors.append(f"{rel} Q{q_idx}: duplicate questionId {qid}")
        q_ids.add(qid)

        q_text = q.get("questionTextHi", "").strip()
        if not q_text:
            errors.append(f"{rel} Q{q_idx}: empty questionTextHi")

        opts = q.get("optionsHi", [])
        if len(opts) != 4:
            errors.append(f"{rel} Q{q_idx}: expected 4 options, found {len(opts)}")
        for o_idx, opt in enumerate(opts):
            if not str(opt).strip():
                errors.append(f"{rel} Q{q_idx}: empty option {o_idx}")

        corr = q.get("correctOption")
        if corr not in ['A', 'B', 'C', 'D']:
            errors.append(f"{rel} Q{q_idx}: invalid correctOption '{corr}'")
        else:
            exp_idx = ord(corr) - ord('A')
            if q.get("correct_index") != exp_idx:
                errors.append(f"{rel} Q{q_idx}: correct_index mismatch ({q.get('correct_index')} != {exp_idx})")

        exp = q.get("explanationHi", "").strip()
        if not exp:
            errors.append(f"{rel} Q{q_idx}: empty explanationHi")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors[:20]:
        print("  -", e)
    raise SystemExit(1)
else:
    print(f"SUCCESS: All {len(files)} test files verified perfectly!")
    print(f"Total verified authentic questions: {total_qs}")
