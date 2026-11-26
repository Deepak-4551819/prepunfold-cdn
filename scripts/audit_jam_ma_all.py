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

def audit():
    errors = []
    print("=== 1. AUDITING MANIFEST.JSON FOR IIT JAM MA ===")
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1.1 Category metadata
    jam_ma_cat = [c for c in manifest.get('categories', []) if c.get('id') == 'jam_ma']
    if not jam_ma_cat:
        errors.append("jam_ma category missing in manifest.json")
    else:
        cat = jam_ma_cat[0]
        if cat.get('totalTests') != 5:
            errors.append(f"Category totalTests != 5 ({cat.get('totalTests')})")
        if cat.get('totalQuestions') != 300:
            errors.append(f"Category totalQuestions != 300 ({cat.get('totalQuestions')})")
        print(f"[OK] Category jam_ma metadata: totalTests={cat.get('totalTests')}, totalQuestions={cat.get('totalQuestions')}")

    # 1.2 Tests in manifest
    jam_ma_tests = [t for t in manifest.get('tests', []) if t.get('categoryId') == 'jam_ma']
    if len(jam_ma_tests) != 5:
        errors.append(f"Expected 5 jam_ma tests in manifest, found {len(jam_ma_tests)}")
    else:
        print(f"[OK] Manifest contains exactly 5 jam_ma test entries")

    expected_years = [2026, 2025, 2024, 2023, 2022]
    all_paths = []
    for idx, yr in enumerate(expected_years):
        t = jam_ma_tests[idx]
        exp_id = f"jam_ma_pyq_{yr}"
        if t.get('testId') != exp_id:
            errors.append(f"Test order mismatch at index {idx}: expected {exp_id}, got {t.get('testId')}")
        fp = t.get('filePath')
        if not fp or not os.path.exists(fp):
            errors.append(f"Manifest filePath does not exist: {fp}")
        else:
            all_paths.append(fp)

    print("=== 2. AUDITING ALL 5 IIT JAM MA TEST FILES ON DISK ===")
    total_q_scanned = 0
    for path in all_paths:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)

        tid = d.get('testId')
        actual_keys = list(d.keys())
        if actual_keys != EXPECTED_TOP_21:
            diff_extra = set(actual_keys) - set(EXPECTED_TOP_21)
            diff_missing = set(EXPECTED_TOP_21) - set(actual_keys)
            errors.append(f"{tid}: Top keys mismatch! Extra: {diff_extra}, Missing: {diff_missing}")

        qs = d.get('questions', [])
        if len(qs) != 60:
            errors.append(f"{tid}: question count {len(qs)} != 60")
        if d.get('maxMarks') != 100.0:
            errors.append(f"{tid}: maxMarks {d.get('maxMarks')} != 100.0")

        total_q_scanned += len(qs)

        # Check sections
        secs = d.get('sections', [])
        if len(secs) != 3:
            errors.append(f"{tid}: Expected 3 sections, got {len(secs)}")
        else:
            sa, sb, sc = secs[0], secs[1], secs[2]
            if sa.get('sectionId') != 'sec_a' or sa.get('questionCount') != 30 or sa.get('totalMarks') != 50.0:
                errors.append(f"{tid}: Section A invalid: {sa}")
            if sb.get('sectionId') != 'sec_b' or sb.get('questionCount') != 10 or sb.get('totalMarks') != 20.0:
                errors.append(f"{tid}: Section B invalid: {sb}")
            if sc.get('sectionId') != 'sec_c' or sc.get('questionCount') != 20 or sc.get('totalMarks') != 30.0:
                errors.append(f"{tid}: Section C invalid: {sc}")

        marks_sum = 0.0
        for i, q in enumerate(qs, 1):
            qnum = q.get('questionNumber')
            if qnum != i:
                errors.append(f"{tid} Q index {i} has qnum {qnum}")

            actual_q_keys = list(q.keys())
            if actual_q_keys != EXPECTED_Q_19:
                errors.append(f"{tid} Q{qnum}: Question keys mismatch: {actual_q_keys}")

            qt = q.get('questionType')
            pos = float(q.get('positiveMarks', 0.0))
            neg = float(q.get('negativeMarks', 0.0))
            marks_sum += pos
            co = q.get('correctOption')
            col = q.get('correctOptionsList')
            cidx = q.get('correct_index')
            cindices = q.get('correct_indices')
            opts = q.get('optionsEn', [])
            qtext = q.get('questionTextEn', '')
            exp = q.get('explanationEn', '')
            is_mta = "MTA" in (str(co) + str(col) + exp)

            # Negative marks check
            if is_mta:
                if neg != 0.0:
                    errors.append(f"{tid} Q{qnum}: MTA negativeMarks != 0.0 ({neg})")
            elif qt == 'MCQ':
                if pos == 1.0 and abs(neg - 0.33) > 0.01:
                    errors.append(f"{tid} Q{qnum}: 1m MCQ negativeMarks != 0.33 ({neg})")
                elif pos == 2.0 and abs(neg - 0.67) > 0.01:
                    errors.append(f"{tid} Q{qnum}: 2m MCQ negativeMarks != 0.67 ({neg})")
            elif qt in ('MSQ', 'NAT'):
                if neg != 0.0:
                    errors.append(f"{tid} Q{qnum}: {qt} negativeMarks != 0.0 ({neg})")

            # Option checks
            if qt == 'MCQ':
                if len(opts) != 4:
                    errors.append(f"{tid} Q{qnum}: MCQ options count != 4")
                if len(set(o.strip() for o in opts)) < 4:
                    errors.append(f"{tid} Q{qnum}: Duplicate options found")
                if is_mta:
                    if col != ['A', 'B', 'C', 'D'] or cindices != [0, 1, 2, 3]:
                        errors.append(f"{tid} Q{qnum}: MTA col/cindices mismatch")
                else:
                    if co not in ('A', 'B', 'C', 'D'):
                        errors.append(f"{tid} Q{qnum}: MCQ correctOption not in A-D ({co})")
                    expected_idx = LETTER_TO_IDX.get(co)
                    if cidx != expected_idx:
                        errors.append(f"{tid} Q{qnum}: MCQ cidx mismatch: co={co}, cidx={cidx}")
                    if cindices != [expected_idx]:
                        errors.append(f"{tid} Q{qnum}: MCQ cindices mismatch: {cindices}")

            elif qt == 'MSQ':
                if co is not None and not is_mta:
                    errors.append(f"{tid} Q{qnum}: MSQ correctOption must be null, got {co}")
                if len(opts) != 4:
                    errors.append(f"{tid} Q{qnum}: MSQ options count != 4")
                if not col:
                    errors.append(f"{tid} Q{qnum}: MSQ correctOptionsList is empty")
                expected_indices = [LETTER_TO_IDX[l] for l in col if l in LETTER_TO_IDX]
                if cindices != expected_indices:
                    errors.append(f"{tid} Q{qnum}: MSQ cindices mismatch: col={col}, cindices={cindices}")

            elif qt == 'NAT':
                if opts != []:
                    errors.append(f"{tid} Q{qnum}: NAT optionsEn not empty")
                if col != [] or cidx is not None or cindices != []:
                    errors.append(f"{tid} Q{qnum}: NAT has optionsList/indices set")
                if not is_mta and (q.get('natMin') is None or q.get('natMax') is None):
                    errors.append(f"{tid} Q{qnum}: NAT missing natMin/natMax")

            # Text / Explanation / Bleed / LaTeX
            if len(qtext.strip()) < 10:
                errors.append(f"{tid} Q{qnum}: questionTextEn too short")
            if len(exp.strip()) < 10:
                errors.append(f"{tid} Q{qnum}: explanationEn too short")
            if any(w in exp.lower() for w in ["wait,", "hold on", "let me re-read"]):
                errors.append(f"{tid} Q{qnum}: Self-talk in explanationEn")

            for fld, text in [('qtext', qtext), ('exp', exp)] + [(f'opt{k}', o) for k, o in enumerate(opts)]:
                unsec = text.replace(r'\$', '')
                if unsec.count('$') % 2 != 0:
                    errors.append(f"{tid} Q{qnum}: Odd dollar count in {fld}")

        if round(marks_sum, 2) != 100.0:
            errors.append(f"{tid}: Positive marks sum != 100.0 ({marks_sum})")

    print(f"[OK] Scanned {len(all_paths)} files, total questions: {total_q_scanned}")

    print("=== 3. AUDITING SEEN_QUESTION_HASHES.JSON ===")
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)
    jam_ma_hashes = [k for k, v in hashes.items() if v.get('categoryId') == 'jam_ma']
    if len(jam_ma_hashes) != 297:
        errors.append(f"Expected 297 unique hashes for jam_ma, got {len(jam_ma_hashes)}")
    else:
        print(f"[OK] Exactly 297 unique hashes indexed for jam_ma (300 questions processed, 3 generic stems)")

    print("=== SUMMARY ===")
    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for e in errors[:25]:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("ALL 5 IIT JAM MA AUDIT CHECKS PASSED PERFECTLY! 100% READY!")

if __name__ == '__main__':
    audit()
