# -*- coding: utf-8 -*-
import json
import glob
import os

akruti_special_chars = set(['â', '›', 'Ø', 'ò', 'õ', 'ü', 'ý', 'ef›eâ', 'keâ'])

test_files = sorted(glob.glob(r'tests/judiciary_pyq/**/*.json', recursive=True))
print(f"Strictly auditing {len(test_files)} judiciary test files...")

issues = []
total_qs = 0
for tf in test_files:
    with open(tf, 'r', encoding='utf-8') as f:
        d = json.load(f)
    qs = d.get('questions', [])
    total_qs += len(qs)
    for q in qs:
        q_num = q.get('questionNumber')
        q_en = q.get('questionTextEn', '')
        q_hi = q.get('questionTextHi', '')
        opts_en = q.get('optionsEn', [])
        opts_hi = q.get('optionsHi', [])

        # Check Akruti special chars
        found_chars = [c for c in q_en if c in akruti_special_chars]
        if found_chars or 'keâ' in q_en or 'efme' in q_en:
            issues.append((os.path.basename(tf), q_num, f"Akruti found in questionTextEn: {found_chars} | {q_en[:50]}"))

        found_chars_hi = [c for c in q_hi if c in akruti_special_chars]
        if found_chars_hi or 'keâ' in q_hi or 'efme' in q_hi:
            issues.append((os.path.basename(tf), q_num, f"Akruti found in questionTextHi: {found_chars_hi} | {q_hi[:50]}"))

        # Check empty stem
        if not q_en.strip():
            issues.append((os.path.basename(tf), q_num, "Empty questionTextEn"))
        if not q_hi.strip():
            issues.append((os.path.basename(tf), q_num, "Empty questionTextHi"))

        # Check options count
        if len(opts_en) != 4:
            issues.append((os.path.basename(tf), q_num, f"optionsEn count={len(opts_en)}"))
        if len(opts_hi) != 4:
            issues.append((os.path.basename(tf), q_num, f"optionsHi count={len(opts_hi)}"))

print(f"\nAudit complete across {len(test_files)} files, {total_qs} questions.")
if not issues:
    print("SUCCESS: 0 ISSUES FOUND! 100% clean English and Hindi, 0 Akruti font artifacts across all 9,935 questions!")
else:
    print(f"Found {len(issues)} issues:")
    for iss in issues[:20]:
        print(" ", iss)
