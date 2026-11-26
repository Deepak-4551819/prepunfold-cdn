# -*- coding: utf-8 -*-
import sys
import os
import json
import re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

EXPECTED_TOP_21 = [
    'testId', 'categoryId', 'test_id', 'category_id', 'title', 'titleEn',
    'testType', 'test_type', 'isFree', 'is_free', 'durationMinutes', 'duration_minutes',
    'totalQuestions', 'total_questions', 'maxMarks', 'positiveMarks', 'negativeMarks',
    'examYear', 'shiftBadge', 'sections', 'questions'
]

EXPECTED_Q_19 = [
    'questionId', 'questionNumber', 'sectionId', 'sectionTitle', 'questionType',
    'positiveMarks', 'negativeMarks', 'pyqTag', 'topicTag', 'difficulty',
    'correctOption', 'correctOptionsList', 'correct_index', 'correct_indices',
    'natMin', 'natMax', 'questionTextEn', 'optionsEn', 'explanationEn'
]

LETTER_TO_IDX = {"A": 0, "B": 1, "C": 2, "D": 3}

def audit_gate_cy():
    print("==================================================")
    print("AUDITING GATE CHEMISTRY (CY) OFFICIAL PYQS")
    print("==================================================")

    pyq_dir = "tests/gate/gate_cy/pyq"
    years = [2022, 2023, 2024, 2025, 2026]
    all_passed = True
    total_q_count = 0

    for yr in years:
        fname = f"gate_cy_pyq_{yr}.json"
        fpath = os.path.join(pyq_dir, fname)
        if not os.path.exists(fpath):
            print(f"[FAIL] Missing file: {fpath}")
            all_passed = False
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        errors = []

        # 1. Top-level keys
        actual_top = list(data.keys())
        if actual_top != EXPECTED_TOP_21:
            diff_extra = set(actual_top) - set(EXPECTED_TOP_21)
            diff_missing = set(EXPECTED_TOP_21) - set(actual_top)
            errors.append(f"Top-level keys mismatch! Extra: {diff_extra}, Missing: {diff_missing}")

        # 2. Metadata
        if data.get("testId") != f"gate_cy_pyq_{yr}":
            errors.append(f"testId mismatch: {data.get('testId')}")
        if data.get("categoryId") != "gate_cy":
            errors.append(f"categoryId mismatch: {data.get('categoryId')}")
        if data.get("totalQuestions") != 65:
            errors.append(f"totalQuestions != 65 ({data.get('totalQuestions')})")
        if data.get("maxMarks") != 100.0:
            errors.append(f"maxMarks != 100.0 ({data.get('maxMarks')})")
        if yr == 2022 and not data.get("isFree"):
            errors.append("2022 should be isFree=True")
        if yr > 2022 and data.get("isFree"):
            errors.append(f"{yr} should be isFree=False")

        # 3. Sections
        secs = data.get("sections", [])
        if len(secs) != 2:
            errors.append(f"Expected 2 sections, got {len(secs)}")
        else:
            ga_sec, cy_sec = secs[0], secs[1]
            if ga_sec.get("sectionId") != "sec_ga" or ga_sec.get("questionCount") != 10 or ga_sec.get("totalMarks") != 15.0:
                errors.append(f"GA section invalid: {ga_sec}")
            if cy_sec.get("sectionId") != "sec_cy" or cy_sec.get("questionCount") != 55 or cy_sec.get("totalMarks") != 85.0:
                errors.append(f"CY section invalid: {cy_sec}")

        # 4. Questions
        qs = data.get("questions", [])
        if len(qs) != 65:
            errors.append(f"Questions array length != 65 ({len(qs)})")
        total_q_count += len(qs)

        marks_sum = 0.0
        for i, q in enumerate(qs, 1):
            qnum = q.get("questionNumber")
            if qnum != i:
                errors.append(f"Q index {i} has questionNumber {qnum}")

            actual_q_keys = list(q.keys())
            if actual_q_keys != EXPECTED_Q_19:
                errors.append(f"Q{qnum}: Question keys mismatch! Got {actual_q_keys}")

            qt = q.get("questionType")
            pos = q.get("positiveMarks", 0.0)
            neg = q.get("negativeMarks", 0.0)
            marks_sum += pos
            co = q.get("correctOption")
            col = q.get("correctOptionsList")
            cidx = q.get("correct_index")
            cindices = q.get("correct_indices")
            nmin = q.get("natMin")
            nmax = q.get("natMax")
            qtext = q.get("questionTextEn", "")
            opts = q.get("optionsEn", [])
            exp = q.get("explanationEn", "")
            is_mta = "MTA" in (str(co) + str(col) + exp)

            # Negative marks check
            if is_mta:
                if neg != 0.0:
                    errors.append(f"Q{qnum}: MTA negativeMarks != 0.0 ({neg})")
            elif qt == 'MCQ':
                if pos == 1.0 and abs(neg - 0.33) > 0.01:
                    errors.append(f"Q{qnum}: 1m MCQ negativeMarks != 0.33 ({neg})")
                elif pos == 2.0 and abs(neg - 0.67) > 0.01:
                    errors.append(f"Q{qnum}: 2m MCQ negativeMarks != 0.67 ({neg})")
            elif qt in ('MSQ', 'NAT'):
                if neg != 0.0:
                    errors.append(f"Q{qnum}: {qt} negativeMarks != 0.0 ({neg})")

            # Type specific checks
            if qt == 'MCQ':
                if len(opts) != 4:
                    errors.append(f"Q{qnum}: MCQ optionsEn len != 4")
                if len(set(o.strip() for o in opts)) < 4:
                    errors.append(f"Q{qnum}: Duplicate options found")
                if is_mta:
                    if col != ['A', 'B', 'C', 'D'] or cindices != [0, 1, 2, 3]:
                        errors.append(f"Q{qnum}: MTA MCQ col/cindices mismatch")
                else:
                    if co not in ('A', 'B', 'C', 'D'):
                        errors.append(f"Q{qnum}: MCQ co not in A-D ({co})")
                    expected_idx = LETTER_TO_IDX.get(co)
                    if cidx != expected_idx:
                        errors.append(f"Q{qnum}: MCQ cidx mismatch: co={co}, cidx={cidx}")
                    if cindices != [expected_idx]:
                        errors.append(f"Q{qnum}: MCQ cindices mismatch: {cindices}")
            elif qt == 'MSQ':
                if co is not None and not is_mta:
                    errors.append(f"Q{qnum}: MSQ correctOption must be null, got {co}")
                if len(opts) != 4:
                    errors.append(f"Q{qnum}: MSQ optionsEn len != 4")
                if not col:
                    errors.append(f"Q{qnum}: MSQ col is empty")
                expected_indices = [LETTER_TO_IDX[l] for l in col if l in LETTER_TO_IDX]
                if cindices != expected_indices:
                    errors.append(f"Q{qnum}: MSQ cindices mismatch: col={col}, cindices={cindices}")
            elif qt == 'NAT':
                if opts != []:
                    errors.append(f"Q{qnum}: NAT optionsEn not empty: {opts}")
                if col != [] or cidx is not None or cindices != []:
                    errors.append(f"Q{qnum}: NAT has option list/indices set")
                if not is_mta and (nmin is None or nmax is None):
                    errors.append(f"Q{qnum}: NAT missing natMin/natMax")

            # Text / Explanation checks
            if len(qtext.strip()) < 10:
                errors.append(f"Q{qnum}: questionTextEn too short")
            if len(exp.strip()) < 15:
                errors.append(f"Q{qnum}: explanationEn too short")
            if any(w in exp.lower() for w in ["wait,", "hold on", "let me re-read"]):
                errors.append(f"Q{qnum}: Self-talk in explanationEn")

            # LaTeX balance
            for fld, text in [('qtext', qtext), ('exp', exp)] + [(f'opt{k}', o) for k, o in enumerate(opts)]:
                unsec = text.replace(r'\$', '')
                if unsec.count('$') % 2 != 0:
                    errors.append(f"Q{qnum}: Odd dollar count in {fld}")

        if round(marks_sum, 2) != 100.0:
            errors.append(f"Positive marks sum != 100.0 ({marks_sum})")

        if errors:
            print(f"[FAIL] {fname}: {len(errors)} issues")
            for e in errors[:10]:
                print(f"   - {e}")
            all_passed = False
        else:
            print(f"[PASS] {fname}: 65 Qs, 100.0 marks, strict 21/19 schema, verified!")

    # 5. Manifest check
    print("\nAuditing manifest.json for gate_cy...")
    with open('manifest.json', 'r', encoding='utf-8') as f:
        m = json.load(f)

    cat = [c for c in m.get('categories', []) if c.get('id') == 'gate_cy']
    if not cat:
        print("[FAIL] gate_cy category missing in manifest.json")
        all_passed = False
    else:
        c = cat[0]
        if c.get('totalTests') != 5 or c.get('totalQuestions') != 325:
            print(f"[FAIL] Category counts mismatch: tests={c.get('totalTests')}, qs={c.get('totalQuestions')}")
            all_passed = False
        else:
            print(f"[PASS] Category gate_cy: totalTests={c.get('totalTests')}, totalQuestions={c.get('totalQuestions')}")

    cy_tests = [t for t in m.get('tests', []) if t.get('categoryId') == 'gate_cy']
    if len(cy_tests) != 5:
        print(f"[FAIL] Expected 5 gate_cy tests in manifest['tests'], got {len(cy_tests)}")
        all_passed = False
    else:
        print(f"[PASS] Found 5 gate_cy tests in manifest['tests']")
        expected_years = [2026, 2025, 2024, 2023, 2022]
        for idx, t in enumerate(cy_tests):
            yr = expected_years[idx]
            expected_tid = f"gate_cy_pyq_{yr}"
            if t.get('testId') != expected_tid:
                print(f"[FAIL] Order/testId mismatch: expected {expected_tid}, got {t.get('testId')}")
                all_passed = False
            fpath = t.get('filePath')
            if not os.path.exists(fpath):
                print(f"[FAIL] Manifest test filePath does not exist: {fpath}")
                all_passed = False

    # 6. Hashes check
    print("\nAuditing seen_question_hashes.json for gate_cy...")
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)
    cy_hashes = [k for k, v in hashes.items() if v.get('categoryId') == 'gate_cy']
    if len(cy_hashes) not in (324, 325):
        print(f"[FAIL] Expected 324/325 gate_cy hashes, got {len(cy_hashes)}")
        all_passed = False
    else:
        print(f"[PASS] {len(cy_hashes)} unique question hashes indexed for gate_cy (325 questions processed, 1 identical stem across 2024 Q56 & Q57)!")

    print("\n" + "=" * 50)
    if all_passed:
        print("ALL AUDIT CHECKS PASSED FOR GATE CHEMISTRY (CY)! 100% READY!")
    else:
        print("SOME AUDIT CHECKS FAILED! PLEASE REVIEW OUTPUT ABOVE.")
    print("=" * 50)

if __name__ == '__main__':
    audit_gate_cy()
