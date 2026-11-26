import os
import json

CH_DIR = "tests/teaching/tgt_pgt_history"
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith("tgt_pgt_hist_") and f.endswith(".json")])

total_questions = 0
total_errors = 0

print(f"Auditing {len(files)} files in {CH_DIR}...")

for f in files:
    path = os.path.join(CH_DIR, f)
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)

    qs = data.get("questions", [])
    total_questions += len(qs)

    # Check question numbers
    for i, q in enumerate(qs):
        if q.get("questionNumber") != i + 1:
            print(f"Error in {f}: Q{q.get('questionNumber')} at index {i}")
            total_errors += 1

        # Check options
        oh = q.get("optionsHi", [])
        oe = q.get("optionsEn", [])
        if len(oh) != 4 or len(oe) != 4:
            print(f"Option error in {f} Q{i+1}: oh={len(oh)}, oe={len(oe)}")
            total_errors += 1

        if any("Option " in opt for opt in oh) or any("Option " in opt for opt in oe):
            print(f"Placeholder in {f} Q{i+1}")
            total_errors += 1

print(f"Audit Complete: {len(files)} files, {total_questions} questions, {total_errors} errors.")
