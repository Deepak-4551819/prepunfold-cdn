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

EXPECTED_TOP_24_TOPIC = [
    'testId', 'categoryId', 'test_id', 'category_id', 'title', 'titleEn',
    'testType', 'test_type', 'partId', 'part_id', 'partTitle',
    'isFree', 'is_free', 'durationMinutes', 'duration_minutes',
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
    print("=== 1. AUDITING MANIFEST.JSON FOR IIT JAM MA SUITE ===")
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1.1 Category metadata
    ma_cat = [c for c in manifest.get('categories', []) if c.get('id') == 'jam_ma']
    if not ma_cat:
        errors.append("jam_ma category missing in manifest.json")
    else:
        cat = ma_cat[0]
        if cat.get('totalTests') != 31:
            errors.append(f"Category totalTests != 31 ({cat.get('totalTests')})")
        if cat.get('totalQuestions') != 1220:
            errors.append(f"Category totalQuestions != 1220 ({cat.get('totalQuestions')})")
        parts = cat.get('parts', [])
        if len(parts) != 8:
            errors.append(f"Category parts len != 8 ({len(parts)})")
        else:
            for idx, p in enumerate(parts, 1):
                if p.get('order') != idx:
                    errors.append(f"Part order mismatch: expected {idx}, got {p.get('order')}")
                if p.get('topicCount') != 2:
                    errors.append(f"Part {p.get('partId')} topicCount != 2")
                if p.get('questionCount') != 40:
                    errors.append(f"Part {p.get('partId')} questionCount != 40")
        print(f"[OK] Category jam_ma metadata: {len(parts)} parts, {cat.get('totalTests')} tests, {cat.get('totalQuestions')} questions")

    # 1.2 Tests in manifest
    jam_tests = [t for t in manifest.get('tests', []) if t.get('categoryId') == 'jam_ma']
    if len(jam_tests) != 31:
        errors.append(f"Expected 31 jam_ma tests in manifest, found {len(jam_tests)}")
    else:
        print(f"[OK] Manifest contains exactly 31 jam_ma test entries")

    pyqs = [t for t in jam_tests if t.get('testType') == 'PYQ']
    mocks = [t for t in jam_tests if t.get('testType') == 'FULL_MOCK']
    topics = [t for t in jam_tests if t.get('testType') == 'TOPIC']

    if len(pyqs) != 5:
        errors.append(f"Expected 5 PYQs, got {len(pyqs)}")
    if len(mocks) != 10:
        errors.append(f"Expected 10 Full Mocks, got {len(mocks)}")
    if len(topics) != 16:
        errors.append(f"Expected 16 Topic Tests, got {len(topics)}")
    print(f"[OK] Test type breakdown: {len(pyqs)} PYQs, {len(mocks)} Full Mocks, {len(topics)} Topic Tests")

    # Order check
    expected_order = (
        [f"jam_ma_pyq_{y}" for y in [2026, 2025, 2024, 2023, 2022]] +
        [f"jam_ma_mock_{i:02d}" for i in range(1, 11)]
    )
    for i, exp_id in enumerate(expected_order):
        actual_id = jam_tests[i].get('testId')
        if actual_id != exp_id:
            errors.append(f"Test order mismatch at index {i}: expected {exp_id}, got {actual_id}")

    # Check all file paths in manifest exist
    all_paths = []
    for t in jam_tests:
        fp = t.get('filePath')
        if not fp or not os.path.exists(fp):
            errors.append(f"Manifest filePath does not exist: {fp}")
        else:
            all_paths.append(fp)

    print("=== 2. AUDITING ALL 31 IIT JAM MA TEST FILES ON DISK ===")
    total_q_scanned = 0
    for path in all_paths:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)

        tid = d.get('testId')
        ttype = d.get('testType')
        is_mock = (ttype == 'FULL_MOCK')
        is_pyq = (ttype == 'PYQ')
        is_topic = (ttype == 'TOPIC')

        # Check top-level keys
        actual_keys = list(d.keys())
        if is_topic:
            if actual_keys != EXPECTED_TOP_24_TOPIC:
                errors.append(f"{tid}: Topic test top keys mismatch: {actual_keys}")
        else:
            if actual_keys != EXPECTED_TOP_21:
                errors.append(f"{tid}: Top keys mismatch: {actual_keys}")

        qs = d.get('questions', [])
        expected_len = 60 if (is_mock or is_pyq) else 20
        expected_marks = 100.0 if (is_mock or is_pyq) else 30.0

        if len(qs) != expected_len:
            errors.append(f"{tid}: question count {len(qs)} != {expected_len}")
        if d.get('maxMarks') != expected_marks:
            errors.append(f"{tid}: maxMarks {d.get('maxMarks')} != {expected_marks}")

        total_q_scanned += len(qs)

        # Questions check
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
            if re.search(r'\b(wait|hold on|let me rethink|let me re-read)\b\s*[:\-,]', exp, re.I):
                errors.append(f"{tid} Q{qnum}: Self-talk in explanationEn")

            for fld, text in [('qtext', qtext), ('exp', exp)] + [(f'opt{k}', o) for k, o in enumerate(opts)]:
                unsec = text.replace(r'\$', '')
                if unsec.count('$') % 2 != 0:
                    errors.append(f"{tid} Q{qnum}: Odd dollar count in {fld}")

        if round(marks_sum, 2) != expected_marks:
            errors.append(f"{tid}: Positive marks sum != {expected_marks} ({marks_sum})")

    print(f"[OK] Scanned {len(all_paths)} files, total questions: {total_q_scanned}")

    print("=== 3. AUDITING SEEN_QUESTION_HASHES.JSON ===")
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)
    jam_ma_hashes = [k for k, v in hashes.items() if v.get('categoryId') == 'jam_ma']
    if len(jam_ma_hashes) != 1217:
        errors.append(f"Expected 1217 unique hashes for jam_ma, got {len(jam_ma_hashes)}")
    else:
        print(f"[OK] Exactly 1217 unique hashes indexed for jam_ma (1220 questions processed, 3 generic stems in PYQs)")

    print("=== SUMMARY ===")
    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for e in errors[:25]:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("ALL 31 IIT JAM MA AUDIT CHECKS PASSED PERFECTLY! 100% READY!")

if __name__ == '__main__':
    audit()
