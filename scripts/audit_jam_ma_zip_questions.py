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

ZIP_PATH = r"C:\Users\yedde\Downloads\jam_ma_official_pyqs_2022_2026.zip"

LETTER_TO_IDX = {"A": 0, "B": 1, "C": 2, "D": 3}

print(f"Auditing questions inside {ZIP_PATH}...")
with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    for name in sorted(z.namelist()):
        if not name.endswith('.json') or 'snippet' in name:
            continue
        data = json.loads(z.read(name).decode('utf-8'))
        qs = data['questions']
        issues = []
        for q in qs:
            qnum = q['questionNumber']
            qt = q['questionType']
            qtext = q['questionTextEn']
            opts = q['optionsEn']
            exp = q['explanationEn']
            co = q['correctOption']
            col = q['correctOptionsList']
            cidx = q['correct_index']
            cindices = q['correct_indices']
            nmin = q['natMin']
            nmax = q['natMax']
            pos = q['positiveMarks']
            neg = q['negativeMarks']
            is_mta = "MTA" in (str(co) + str(col) + exp)

            # 1. Non-empty text
            if len(qtext.strip()) < 10:
                issues.append(f"Q{qnum}: questionTextEn too short ({len(qtext)})")

            # 2. Options check
            if qt in ('MCQ', 'MSQ'):
                if len(opts) != 4:
                    issues.append(f"Q{qnum}: {qt} does not have 4 options ({len(opts)})")
                else:
                    for i, o in enumerate(opts):
                        if not o.strip():
                            issues.append(f"Q{qnum}: option {chr(65+i)} is empty")
                    # Duplicate options check
                    opt_stripped = [o.strip() for o in opts]
                    if len(set(opt_stripped)) < 4:
                        issues.append(f"Q{qnum}: duplicate options found: {opts}")
            elif qt == 'NAT':
                if len(opts) != 0:
                    issues.append(f"Q{qnum}: NAT has options ({len(opts)})")

            # 3. Keys / indices consistency
            if qt == 'MCQ':
                if is_mta:
                    if col != ['A', 'B', 'C', 'D'] or cindices != [0, 1, 2, 3]:
                        issues.append(f"Q{qnum}: MTA MCQ col/cindices mismatch")
                else:
                    if co not in ('A', 'B', 'C', 'D'):
                        issues.append(f"Q{qnum}: MCQ correctOption invalid ({co})")
                    expected_idx = ord(co) - 65
                    if cidx != expected_idx:
                        issues.append(f"Q{qnum}: MCQ cidx mismatch: co={co}, cidx={cidx}")
                    if cindices != [expected_idx]:
                        issues.append(f"Q{qnum}: MCQ cindices mismatch: co={co}, cindices={cindices}")
            elif qt == 'MSQ':
                if co is not None and not is_mta:
                    issues.append(f"Q{qnum}: MSQ correctOption should be null, got ({co})")
                if not col:
                    issues.append(f"Q{qnum}: MSQ correctOptionsList empty")
                expected_indices = [ord(x) - 65 for x in col]
                if cindices != expected_indices:
                    issues.append(f"Q{qnum}: MSQ cindices mismatch: col={col}, cindices={cindices}")
            elif qt == 'NAT':
                if cidx is not None or cindices != []:
                    issues.append(f"Q{qnum}: NAT has index set ({cidx}, {cindices})")
                if col != []:
                    issues.append(f"Q{qnum}: NAT has correctOptionsList set")
                if not is_mta and (nmin is None or nmax is None):
                    issues.append(f"Q{qnum}: NAT missing natMin/natMax")

            # 4. LaTeX $ balance
            for field_name, val in [("qtext", qtext), ("exp", exp)] + [(f"opt{i}", o) for i, o in enumerate(opts)]:
                unsec = val.replace(r'\$', '')
                dollars = unsec.count('$')
                if dollars % 2 != 0:
                    issues.append(f"Q{qnum}: odd number of $ in {field_name}: {dollars}")

        print(f"\n{name}:")
        if issues:
            print(f"  FAILED with {len(issues)} issues:")
            for iss in issues[:15]:
                print(f"    - {iss}")
        else:
            print("  PASSED: 100% clean (zero duplicate options, balanced LaTeX, valid indices, clean options/keys)!")
