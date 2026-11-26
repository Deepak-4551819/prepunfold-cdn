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

zip_path = r"C:\Users\yedde\Downloads\jam_cy_mocks_and_topic_tests.zip"

SELF_TALK_PATTERNS = [
    r"\bwait\b", r"\bhold on\b", r"\blet me check\b", r"\bofficial key confirms\b",
    r"\boh wait\b", r"\bscratch that\b", r"\bactually wait\b", r"\bwait,\b", r"\bhold on,\b"
]

EXPECTED_19_KEYS = [
    'questionId', 'questionNumber', 'sectionId', 'sectionTitle', 'questionType',
    'positiveMarks', 'negativeMarks', 'pyqTag', 'topicTag', 'difficulty',
    'correctOption', 'correctOptionsList', 'correct_index', 'correct_indices',
    'natMin', 'natMax', 'questionTextEn', 'optionsEn', 'explanationEn'
]

with zipfile.ZipFile(zip_path, 'r') as z:
    all_files = [n for n in z.namelist() if n.endswith('.json') and 'snippet' not in n.lower()]
    print(f"Total test files in zip: {len(all_files)}")

    total_questions = 0
    total_issues = 0

    for fname in sorted(all_files):
        data = json.loads(z.read(fname).decode('utf-8'))
        qs = data.get('questions', [])
        total_questions += len(qs)
        is_mock = 'mock' in fname.lower()
        expected_qc = 60 if is_mock else 20
        expected_marks = 100.0 if is_mock else 30.0

        file_issues = []
        calc_marks = 0.0

        if len(qs) != expected_qc:
            file_issues.append(f"Question count {len(qs)} != {expected_qc}")

        for q in qs:
            qnum = q.get('questionNumber')
            qt = q.get('questionType')
            pos = float(q.get('positiveMarks', 0.0))
            neg = float(q.get('negativeMarks', 0.0))
            calc_marks += pos
            qtext = q.get('questionTextEn', '')
            opts = q.get('optionsEn', [])
            exp = q.get('explanationEn', '')

            # Check keys
            if set(q.keys()) != set(EXPECTED_19_KEYS):
                file_issues.append(f"Q{qnum}: Key mismatch: {set(q.keys()) ^ set(EXPECTED_19_KEYS)}")

            # Check options
            if qt in ('MCQ', 'MSQ'):
                if len(opts) != 4:
                    file_issues.append(f"Q{qnum}: {qt} options count {len(opts)} != 4")
                if len(set(opts)) != len(opts) and len(opts) > 0:
                    file_issues.append(f"Q{qnum}: Duplicate options: {opts}")
            elif qt == 'NAT':
                if len(opts) != 0:
                    file_issues.append(f"Q{qnum}: NAT has options: {opts}")
                if q.get('natMin') is None or q.get('natMax') is None:
                    file_issues.append(f"Q{qnum}: NAT missing natMin/natMax")

            # Check LaTeX balance
            for text_f, fld in [(qtext, 'questionTextEn'), (exp, 'explanationEn')] + [(opt, f'opt_{i}') for i, opt in enumerate(opts)]:
                if text_f and text_f.count('$') % 2 != 0:
                    file_issues.append(f"Q{qnum} {fld}: Unbalanced $ ({text_f.count('$')})")

            # Check self-talk
            for pat in SELF_TALK_PATTERNS:
                if re.search(pat, exp, re.IGNORECASE):
                    file_issues.append(f"Q{qnum}: Self-talk match '{pat}': {exp[:80]}...")

        if abs(calc_marks - expected_marks) > 0.01:
            file_issues.append(f"Calculated marks {calc_marks} != expected {expected_marks}")

        if file_issues:
            print(f"[{fname}] {len(file_issues)} issues:")
            for iss in file_issues[:5]:
                print(f"  - {iss}")
            if len(file_issues) > 5:
                print(f"  ... and {len(file_issues) - 5} more")
            total_issues += len(file_issues)
        else:
            print(f"[{fname}] OK (qc={len(qs)}, marks={calc_marks})")

print(f"\n==========================================")
print(f"Total questions audited: {total_questions}")
print(f"Total issues found: {total_issues}")
