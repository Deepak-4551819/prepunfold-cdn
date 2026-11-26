# -*- coding: utf-8 -*-
import os, sys, json, re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def audit_gate_ph():
    errors = []

    print("=== 1. AUDITING MANIFEST.JSON ===")
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    gate_ph_cat = None
    for c in manifest.get('categories', []):
        if c.get('id') == 'gate_ph':
            gate_ph_cat = c
            break

    if not gate_ph_cat:
        errors.append("Category gate_ph not found in manifest")
    else:
        if gate_ph_cat.get('totalTests') != 36:
            errors.append(f"gate_ph totalTests expected 36, got {gate_ph_cat.get('totalTests')}")
        if gate_ph_cat.get('totalQuestions') != 1440:
            errors.append(f"gate_ph totalQuestions expected 1440, got {gate_ph_cat.get('totalQuestions')}")
        if len(gate_ph_cat.get('parts', [])) != 10:
            errors.append(f"gate_ph parts count expected 10, got {len(gate_ph_cat.get('parts', []))}")
        print(f"[OK] Category gate_ph metadata valid: 10 parts, {gate_ph_cat.get('totalTests')} tests, {gate_ph_cat.get('totalQuestions')} questions")

    manifest_ph_tests = [t for t in manifest.get('tests', []) if t.get('categoryId') == 'gate_ph']
    if len(manifest_ph_tests) != 36:
        errors.append(f"Expected 36 gate_ph tests in manifest.tests, got {len(manifest_ph_tests)}")
    else:
        print("[OK] Manifest contains exactly 36 gate_ph test entries")

    for t in manifest_ph_tests:
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

    print("=== 2. AUDITING OFFICIAL PYQs (2021-2026) ===")
    EXPECTED_19_KEYS = {
        'questionId', 'questionNumber', 'sectionId', 'sectionTitle', 'questionType',
        'positiveMarks', 'negativeMarks', 'pyqTag', 'topicTag', 'difficulty',
        'correctOption', 'correctOptionsList', 'correct_index', 'correct_indices',
        'natMin', 'natMax', 'questionTextEn', 'optionsEn', 'explanationEn'
    }

    for y in [2021, 2022, 2023, 2024, 2025, 2026]:
        p = f'tests/gate/gate_ph/pyq/gate_ph_pyq_{y}.json'
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        qs = d.get('questions', [])
        if len(qs) != 65:
            errors.append(f"PYQ {y} has {len(qs)} questions (expected 65)")
        total_marks = sum(float(q.get('positiveMarks', 0)) for q in qs)
        if abs(total_marks - 100.0) > 0.01:
            errors.append(f"PYQ {y} total marks is {total_marks} (expected 100.0)")

        placeholders = 0
        bleed_count = 0
        for q in qs:
            qnum = q.get('questionNumber')
            qtype = q.get('questionType')
            pos = float(q.get('positiveMarks', 0))
            neg = float(q.get('negativeMarks', 0))

            extra_keys = set(q.keys()) - EXPECTED_19_KEYS
            missing_keys = EXPECTED_19_KEYS - set(q.keys())
            if extra_keys:
                errors.append(f"{y} Q{qnum} has extra keys: {extra_keys}")
            if missing_keys:
                errors.append(f"{y} Q{qnum} missing keys: {missing_keys}")

            if qtype == 'MCQ':
                if pos == 1.0 and abs(neg - 0.33) > 0.01 and neg != 0.0:
                    errors.append(f"{y} Q{qnum} 1m MCQ negativeMarks is {neg}")
                elif pos == 2.0 and abs(neg - 0.67) > 0.01 and neg != 0.0:
                    errors.append(f"{y} Q{qnum} 2m MCQ negativeMarks is {neg}")
            elif qtype in ('MSQ', 'NAT'):
                if neg != 0.0:
                    errors.append(f"{y} Q{qnum} {qtype} negativeMarks is not 0.0 ({neg})")

            if qtype == 'NAT':
                if q.get('correctOption') is None:
                    errors.append(f"{y} Q{qnum} NAT correctOption is None")
                if q.get('optionsEn') != []:
                    errors.append(f"{y} Q{qnum} NAT optionsEn not empty")

            if qtype == 'MSQ':
                if q.get('correctOption') is not None:
                    errors.append(f"{y} Q{qnum} MSQ correctOption should be None (got {q.get('correctOption')})")

            exp = q.get('explanationEn', '')
            if not exp or len(exp.strip()) < 15:
                errors.append(f"{y} Q{qnum} explanation is too short or empty")
            if 'Official GATE' in exp and 'Answer Key:' in exp and len(exp.splitlines()) <= 2:
                placeholders += 1

            qtext = q.get('questionTextEn', '')
            if re.search(r'Q\.\d+\s+[A-Z]', qtext):
                bleed_count += 1
            for opt in q.get('optionsEn', []):
                if re.search(r'Q\.\d+\s+[A-Z]', opt):
                    bleed_count += 1

        print(f"[OK] PYQ {y}: 65 Qs, {total_marks:.1f} marks, {placeholders} placeholders, {bleed_count} bleeds")
        if placeholders > 0:
            errors.append(f"PYQ {y} has {placeholders} placeholder explanations")
        if bleed_count > 0:
            errors.append(f"PYQ {y} has {bleed_count} question bleeds")

    print("=== 3. AUDITING FULL MOCKS (01-10) ===")
    for i in range(1, 11):
        p = f'tests/gate/gate_ph/full_mocks/gate_ph_mock_{i:02d}.json'
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        qs = d.get('questions', [])
        if len(qs) != 65:
            errors.append(f"Mock {i:02d} has {len(qs)} questions (expected 65)")
        total_marks = sum(float(q.get('positiveMarks', 0)) for q in qs)
        if abs(total_marks - 100.0) > 0.01:
            errors.append(f"Mock {i:02d} total marks is {total_marks} (expected 100.0)")

    print("[OK] All 10 Full Mocks verified: 65 Qs, 100.0 marks each")

    print("=== 4. AUDITING TOPIC TESTS (20 TESTS) ===")
    topic_count = 0
    for root, dirs, files in os.walk('tests/gate/gate_ph/topic_tests'):
        for f in files:
            if f.endswith('.json'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8') as jf:
                    d = json.load(jf)
                qs = d.get('questions', [])
                if len(qs) != 20:
                    errors.append(f"Topic test {f} has {len(qs)} questions (expected 20)")
                topic_count += 1
    print(f"[OK] All {topic_count} Topic Tests verified: 20 Qs each")

    print("=== SUMMARY ===")
    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for e in errors[:25]:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("ALL AUDIT CHECKS PASSED PERFECTLY!")

if __name__ == '__main__':
    audit_gate_ph()
