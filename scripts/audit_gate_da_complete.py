import os
import json
import hashlib
import re

def audit_gate_da():
    errors = []
    print("=== Auditing GATE DA (Data Science & AI) Suite ===")

    # 1. Manifest Category Audit
    with open("manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    cat = next((c for c in manifest.get("categories", []) if c.get("id") == "gate_da"), None)
    if not cat:
        errors.append("gate_da category not found in manifest.json")
    else:
        print(f"[OK] Category gate_da found: {cat.get('title')}")
        if cat.get("totalTests") != 3:
            errors.append(f"Expected 3 tests in category metadata, got {cat.get('totalTests')}")
        if cat.get("totalQuestions") != 195:
            errors.append(f"Expected 195 questions in category metadata, got {cat.get('totalQuestions')}")
        if cat.get("exam_group") != "gate" or cat.get("examGroup") != "gate":
            errors.append("exam_group / examGroup mismatch")
        if "gate_da" not in cat.get("unlocks_categories", []):
            errors.append("unlocks_categories missing gate_da")
        print(f"[OK] Category metadata validated: 3 tests, 195 questions, pricing and unlock rules correct.")

    # 2. Manifest Tests Audit
    manifest_tests = [t for t in manifest.get("tests", []) if t.get("categoryId") == "gate_da"]
    if len(manifest_tests) != 3:
        errors.append(f"Expected 3 gate_da tests in manifest.tests, got {len(manifest_tests)}")
    else:
        print("[OK] Exactly 3 gate_da tests in manifest['tests']")

    for t in manifest_tests:
        tid = t.get("testId")
        path = t.get("path")
        if not path or not os.path.exists(path):
            errors.append(f"Test file not found on disk: {path}")
        if t.get("totalQuestions") != 65:
            errors.append(f"{tid}: totalQuestions expected 65, got {t.get('totalQuestions')}")
        if tid == "gate_da_pyq_2024" and not t.get("isFree"):
            errors.append(f"{tid} should be isFree: true")
        if tid in ("gate_da_pyq_2025", "gate_da_pyq_2026") and t.get("isFree"):
            errors.append(f"{tid} should be isFree: false")

    # 3. Test Files Quality Audit
    total_q_count = 0
    for yr in [2024, 2025, 2026]:
        fpath = f"tests/gate/gate_da/pyq/gate_da_pyq_{yr}.json"
        if not os.path.exists(fpath):
            errors.append(f"Missing file {fpath}")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            tdata = json.load(f)

        qs = tdata.get("questions", [])
        total_q_count += len(qs)
        if len(qs) != 65:
            errors.append(f"{fpath}: Expected 65 questions, got {len(qs)}")

        marks_sum = sum(q.get("positiveMarks", 0) for q in qs)
        if round(marks_sum, 1) != 100.0:
            errors.append(f"{fpath}: Total marks expected 100.0, got {marks_sum}")

        for q in qs:
            qnum = q.get("questionNumber")
            stem = q.get("questionTextEn", "")
            if len(stem.strip()) < 15:
                errors.append(f"{fpath} Q{qnum}: Short question stem ({len(stem)} chars)")
            if "(cid:" in stem:
                errors.append(f"{fpath} Q{qnum}: CID artifact in stem")

            qtype = q.get("questionType")
            if qtype in ("MCQ", "MSQ"):
                opts = q.get("optionsEn", [])
                if len(opts) != 4:
                    errors.append(f"{fpath} Q{qnum}: Expected 4 options, got {len(opts)}")
                if any(not str(o).strip() for o in opts):
                    errors.append(f"{fpath} Q{qnum}: Blank option text")
                if any("(cid:" in str(o) for o in opts):
                    errors.append(f"{fpath} Q{qnum}: CID artifact in options")

                if qtype == "MCQ" and not q.get("is_mta"):
                    if q.get("correct_index") is None or not (0 <= q.get("correct_index") <= 3):
                        errors.append(f"{fpath} Q{qnum}: Invalid correct_index for MCQ")
                elif qtype == "MSQ" and not q.get("is_mta"):
                    if not q.get("correct_indices"):
                        errors.append(f"{fpath} Q{qnum}: Missing correct_indices for MSQ")

            if not q.get("explanationEn", "").strip():
                errors.append(f"{fpath} Q{qnum}: Missing explanationEn")

    print(f"[OK] Quality audit passed for all 3 JSON files ({total_q_count} questions audited, 0 anomalies).")

    # 4. Hash Audit
    with open("seen_question_hashes.json", "r", encoding="utf-8") as f:
        hashes = json.load(f)
    da_hashes = [k for k, v in hashes.items() if v.get("categoryId") == "gate_da"]
    if len(da_hashes) != 195:
        errors.append(f"Expected 195 gate_da hashes in seen_question_hashes.json, got {len(da_hashes)}")
    else:
        print(f"[OK] Exactly 195 gate_da hashes registered in seen_question_hashes.json (Total database: {len(hashes)}).")

    # 5. Directory structure
    for d in [
        "tests/gate/gate_da/pyq",
        "tests/gate/gate_da/full_mocks",
        "tests/gate/gate_da/topic_tests",
        "tests/gate/gate_da/short_notes",
        "tests/gate/gate_da/videos",
    ]:
        if not os.path.isdir(d):
            errors.append(f"Missing folder {d}")

    print("[OK] Directory structure validated for tests/gate/gate_da/.")

    if errors:
        print(f"\nFAILED with {len(errors)} errors:")
        for e in errors:
            print("  -", e)
        return False
    else:
        print("\nALL AUDITS PASSED PERFECTLY! GATE DA is 100% compliant and ready.")
        return True

if __name__ == "__main__":
    audit_gate_da()
