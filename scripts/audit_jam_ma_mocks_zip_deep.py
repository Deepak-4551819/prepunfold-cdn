# -*- coding: utf-8 -*-
import sys
import json
import zipfile
import re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\jam_ma_mocks_and_topic_tests.zip"

print(f"Deep auditing {ZIP_PATH}...")
with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    for name in sorted(z.namelist()):
        if not name.endswith('.json') or 'snippet' in name:
            continue
        data = json.loads(z.read(name).decode('utf-8'))
        tid = data.get('testId')
        is_mock = 'mock' in name.lower()
        expected_qs = 60 if is_mock else 20
        expected_marks = 100.0 if is_mock else 30.0

        qs = data.get('questions', [])
        issues = []

        if len(qs) != expected_qs:
            issues.append(f"Question count mismatch: {len(qs)} vs expected {expected_qs}")
        if data.get('maxMarks') != expected_marks:
            issues.append(f"maxMarks mismatch: {data.get('maxMarks')} vs expected {expected_marks}")

        marks_sum = 0.0
        for i, q in enumerate(qs, 1):
            qnum = q.get('questionNumber')
            if qnum != i:
                issues.append(f"Q index {i} has qnum {qnum}")

            qt = q.get('questionType')
            pos = float(q.get('positiveMarks', 0.0))
            neg = float(q.get('negativeMarks', 0.0))
            marks_sum += pos
            co = q.get('correctOption')
            col = q.get('correctOptionsList')
            cidx = q.get('correct_index')
            cindices = q.get('correct_indices')
            nmin = q.get('natMin')
            nmax = q.get('natMax')
            qtext = q.get('questionTextEn', '')
            opts = q.get('optionsEn', [])
            exp = q.get('explanationEn', '')
            is_mta = "MTA" in (str(co) + str(col) + exp)

            # Check negative marks sign
            if neg < 0:
                issues.append(f"Q{qnum}: negativeMarks is negative: {neg}")

            # Option checks
            if qt in ('MCQ', 'MSQ'):
                if len(opts) != 4:
                    issues.append(f"Q{qnum}: {qt} options len != 4 ({len(opts)})")
                if len(set(o.strip() for o in opts)) < 4:
                    issues.append(f"Q{qnum}: Duplicate options found: {opts}")
            elif qt == 'NAT':
                if opts != []:
                    issues.append(f"Q{qnum}: NAT optionsEn not empty: {len(opts)}")

            # Keys consistency
            if qt == 'MCQ':
                if not is_mta:
                    if co not in ('A', 'B', 'C', 'D'):
                        issues.append(f"Q{qnum}: MCQ co not in A-D ({co})")
                    expected_idx = ord(co) - 65 if co in ('A', 'B', 'C', 'D') else None
                    if cidx != expected_idx:
                        issues.append(f"Q{qnum}: MCQ cidx mismatch: co={co}, cidx={cidx}")
            elif qt == 'MSQ':
                if co is not None and not is_mta:
                    issues.append(f"Q{qnum}: MSQ co must be null, got {co}")
                if not col:
                    issues.append(f"Q{qnum}: MSQ col empty")
            elif qt == 'NAT':
                if not is_mta and (nmin is None or nmax is None):
                    issues.append(f"Q{qnum}: NAT missing natMin/natMax")

            # Length / Bleed / Self-talk
            if len(qtext.strip()) < 10:
                issues.append(f"Q{qnum}: questionTextEn too short")
            if len(exp.strip()) < 10:
                issues.append(f"Q{qnum}: explanationEn too short")
            if any(w in exp.lower() for w in ["wait,", "hold on", "let me re-read"]):
                issues.append(f"Q{qnum}: Self-talk in explanationEn")

            # LaTeX balance
            for fld, text in [('qtext', qtext), ('exp', exp)] + [(f'opt{k}', o) for k, o in enumerate(opts)]:
                unsec = text.replace(r'\$', '')
                if unsec.count('$') % 2 != 0:
                    issues.append(f"Q{qnum}: Odd dollar count in {fld}")

        if round(marks_sum, 2) != expected_marks:
            issues.append(f"Positive marks sum != {expected_marks} ({marks_sum})")

        print(f"\n{name} ({len(qs)} Qs, {marks_sum} marks):")
        if issues:
            print(f"  FAILED with {len(issues)} issues:")
            for iss in issues[:5]:
                print(f"    - {iss}")
        else:
            print("  PASSED: 100% clean!")
