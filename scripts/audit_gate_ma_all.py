# -*- coding: utf-8 -*-
import os, sys, json, re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def audit():
    errors = []

    print("=== 1. AUDITING MANIFEST.JSON FOR GATE MA ===")
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    gate_ma_cat = None
    for c in manifest.get('categories', []):
        if c.get('id') == 'gate_ma':
            gate_ma_cat = c
            break

    if not gate_ma_cat:
        errors.append("Category gate_ma not found in manifest")
    else:
        if gate_ma_cat.get('totalTests') != 39:
            errors.append(f"gate_ma totalTests expected 39, got {gate_ma_cat.get('totalTests')}")
        if gate_ma_cat.get('totalQuestions') != 1455:
            errors.append(f"gate_ma totalQuestions expected 1455, got {gate_ma_cat.get('totalQuestions')}")
        if len(gate_ma_cat.get('parts', [])) != 12:
            errors.append(f"gate_ma parts count expected 12, got {len(gate_ma_cat.get('parts', []))}")
        print(f"[OK] Category gate_ma metadata: 12 parts, {gate_ma_cat.get('totalTests')} tests, {gate_ma_cat.get('totalQuestions')} questions")

    manifest_ma_tests = [t for t in manifest.get('tests', []) if t.get('categoryId') == 'gate_ma']
    if len(manifest_ma_tests) != 39:
        errors.append(f"Expected 39 gate_ma tests in manifest.tests, got {len(manifest_ma_tests)}")
    else:
        print("[OK] Manifest contains exactly 39 gate_ma test entries")

    pyq_count = sum(1 for t in manifest_ma_tests if t.get('testType') == 'PYQ')
    mock_count = sum(1 for t in manifest_ma_tests if t.get('testType') == 'FULL_MOCK')
    topic_count = sum(1 for t in manifest_ma_tests if t.get('testType') == 'TOPIC')
    print(f"[OK] Test type breakdown: {pyq_count} PYQs, {mock_count} Full Mocks, {topic_count} Topic Tests")
    if pyq_count != 5: errors.append(f"Expected 5 PYQs, got {pyq_count}")
    if mock_count != 10: errors.append(f"Expected 10 Full Mocks, got {mock_count}")
    if topic_count != 24: errors.append(f"Expected 24 Topic Tests, got {topic_count}")

    for t in manifest_ma_tests:
        tid = t['testId']
        path = t.get('path') or t.get('filePath')
        if not path or not os.path.exists(path):
            errors.append(f"Manifest test {tid} path does not exist: {path}")
            continue
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        if d.get('testId') != tid:
            errors.append(f"TestId mismatch in {path}: manifest={tid}, file={d.get('testId')}")
        if len(d.get('questions', [])) != t.get('totalQuestions'):
            errors.append(f"Question count mismatch in {tid}: manifest={t.get('totalQuestions')}, file={len(d.get('questions', []))}")
        if bool(d.get('isFree', False)) != bool(t.get('isFree', False)):
            errors.append(f"isFree mismatch in {tid}: manifest={t.get('isFree')}, file={d.get('isFree')}")

    print("=== 2. AUDITING ALL 39 GATE MA TEST FILES ON DISK ===")
    EXPECTED_19_KEYS = {
        'questionId', 'questionNumber', 'sectionId', 'sectionTitle', 'questionType',
        'positiveMarks', 'negativeMarks', 'pyqTag', 'topicTag', 'difficulty',
        'correctOption', 'correctOptionsList', 'correct_index', 'correct_indices',
        'natMin', 'natMax', 'questionTextEn', 'optionsEn', 'explanationEn'
    }

    all_paths = [t.get('path') for t in manifest_ma_tests]
    total_q_scanned = 0

    for path in all_paths:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        tid = d.get('testId')
        ttype = d.get('testType')
        qs = d.get('questions', [])
        total_q_scanned += len(qs)

        expected_q_count = 65 if ttype in ('PYQ', 'FULL_MOCK') else 20
        expected_total_marks = 100.0 if ttype in ('PYQ', 'FULL_MOCK') else 30.0

        if len(qs) != expected_q_count:
            errors.append(f"{tid} has {len(qs)} questions (expected {expected_q_count})")
        tot_marks = sum(float(q.get('positiveMarks', 0)) for q in qs)
        if abs(tot_marks - expected_total_marks) > 0.01:
            errors.append(f"{tid} total marks is {tot_marks} (expected {expected_total_marks})")

        secs = d.get('sections', [])
        if not secs:
            errors.append(f"{tid} sections array is empty or missing")

        for q in qs:
            qnum = q.get('questionNumber')
            qt = q.get('questionType')
            pos = float(q.get('positiveMarks', 0))
            neg = float(q.get('negativeMarks', 0))

            extra = set(q.keys()) - EXPECTED_19_KEYS
            missing = EXPECTED_19_KEYS - set(q.keys())
            if extra: errors.append(f"{tid} Q{qnum} extra keys: {extra}")
            if missing: errors.append(f"{tid} Q{qnum} missing keys: {missing}")

            if qt == 'MCQ':
                if pos == 1.0 and abs(neg - 0.33) > 0.01 and neg != 0.0:
                    errors.append(f"{tid} Q{qnum} 1m MCQ negativeMarks is {neg}")
                elif pos == 2.0 and abs(neg - 0.67) > 0.01 and neg != 0.0:
                    errors.append(f"{tid} Q{qnum} 2m MCQ negativeMarks is {neg}")
            elif qt in ('MSQ', 'NAT'):
                if neg != 0.0:
                    errors.append(f"{tid} Q{qnum} {qt} negativeMarks is not 0.0 ({neg})")

            if qt == 'NAT':
                if q.get('correctOption') is None:
                    errors.append(f"{tid} Q{qnum} NAT correctOption is None")
                if q.get('optionsEn') != []:
                    errors.append(f"{tid} Q{qnum} NAT optionsEn not empty")
                if q.get('natMin') is None or q.get('natMax') is None:
                    errors.append(f"{tid} Q{qnum} NAT missing natMin/natMax")

            if qt == 'MSQ':
                if q.get('correctOption') is not None:
                    errors.append(f"{tid} Q{qnum} MSQ correctOption should be None (got {q.get('correctOption')})")
                if not q.get('correctOptionsList'):
                    errors.append(f"{tid} Q{qnum} MSQ correctOptionsList is empty")

            exp = q.get('explanationEn', '')
            if not exp or len(exp.strip()) < 10:
                errors.append(f"{tid} Q{qnum} explanation is too short or empty")

            qtext = q.get('questionTextEn', '')
            if re.search(r'Q\.\d+\s+[A-Z]', qtext):
                errors.append(f"{tid} Q{qnum} questionText has bleed")
            for opt in q.get('optionsEn', []):
                if re.search(r'Q\.\d+\s+[A-Z]', opt):
                    errors.append(f"{tid} Q{qnum} option has bleed")

    print(f"[OK] Scanned {len(all_paths)} files, total questions: {total_q_scanned}")

    print("=== SUMMARY ===")
    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for e in errors[:25]:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("ALL 39 GATE MA AUDIT CHECKS PASSED PERFECTLY!")

if __name__ == '__main__':
    audit()
