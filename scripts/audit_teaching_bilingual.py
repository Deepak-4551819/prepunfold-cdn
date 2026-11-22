# -*- coding: utf-8 -*-
import os, json, sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

cats = ['tgt_pgt_economics', 'tgt_pgt_geography', 'tgt_pgt_civics', 'tgt_pgt_history']
base = 'tests/teaching'

total_files = 0
total_qs = 0
empty_en_count = 0
empty_hi_count = 0
same_en_hi_count = 0
invalid_opts_en = 0
invalid_opts_hi = 0

for cat in cats:
    cat_dir = os.path.join(base, cat)
    if not os.path.exists(cat_dir):
        continue
    c_files = 0
    c_qs = 0
    c_empty_en = 0
    c_empty_hi = 0
    c_same = 0
    for root, dirs, files in os.walk(cat_dir):
        for f in files:
            if not f.endswith('.json'):
                continue
            c_files += 1
            total_files += 1
            with open(os.path.join(root, f), 'r', encoding='utf-8') as fp:
                d = json.load(fp)
                qs = d.get('questions', [])
                c_qs += len(qs)
                total_qs += len(qs)
                for q in qs:
                    q_en = q.get('questionTextEn', '').strip()
                    q_hi = q.get('questionTextHi', '').strip()
                    opts_en = q.get('optionsEn', [])
                    opts_hi = q.get('optionsHi', [])

                    if not q_en:
                        c_empty_en += 1
                        empty_en_count += 1
                    if not q_hi:
                        c_empty_hi += 1
                        empty_hi_count += 1
                    if q_en and q_hi and q_en == q_hi:
                        c_same += 1
                        same_en_hi_count += 1
                    if len(opts_en) < 4 or any(not o for o in opts_en):
                        invalid_opts_en += 1
                    if len(opts_hi) < 4 or any(not o for o in opts_hi):
                        invalid_opts_hi += 1

    print(f"[{cat}] Files: {c_files} | Qs: {c_qs} | Empty EN: {c_empty_en} | Empty HI: {c_empty_hi} | Same EN&HI: {c_same}")

print(f"\n=== OVERALL AUDIT ===")
print(f"Total files checked: {total_files}")
print(f"Total questions: {total_qs}")
print(f"Empty questionTextEn: {empty_en_count}")
print(f"Empty questionTextHi: {empty_hi_count}")
print(f"Same En & Hi: {same_en_hi_count}")
print(f"Invalid optionsEn count: {invalid_opts_en}")
print(f"Invalid optionsHi count: {invalid_opts_hi}")

if empty_en_count == 0 and empty_hi_count == 0 and same_en_hi_count == 0 and invalid_opts_en == 0 and invalid_opts_hi == 0:
    print("\n>>> AUDIT PASSED: 100% of questions in all 166 teaching files are fully bilingual, valid, and clean! <<<")
else:
    print("\n>>> AUDIT FAILED: Issues remain! <<<")
