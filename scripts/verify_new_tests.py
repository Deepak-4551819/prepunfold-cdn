import os
import json
import glob

ctet_files = glob.glob("tests/teaching/ctet_state_tet_hindi/*.json")
emrs_files = glob.glob("tests/teaching/emrs_general_hindi/*.json")

print(f"CTET test files: {len(ctet_files)}")
total_ctet_q = 0
for f in sorted(ctet_files):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    total_ctet_q += len(d['questions'])
print(f"Total CTET questions: {total_ctet_q}")

print(f"\nEMRS test files: {len(emrs_files)}")
total_emrs_q = 0
for f in sorted(emrs_files):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    total_emrs_q += len(d['questions'])
print(f"Total EMRS questions: {total_emrs_q}")
