# -*- coding: utf-8 -*-
import json
import glob
import os

base_tests = r'D:\Android Project\prepunfold-cdn\tests\judiciary_pyq'

files = {
    'cpc': r'C:\Users\yedde\Downloads\cpc_pyq.json',
    'crpc': r'C:\Users\yedde\Downloads\crpc_pyq.json',
    'evidence': r'C:\Users\yedde\Downloads\evidence_pyq (1).json',
    'ipc': r'C:\Users\yedde\Downloads\ipc_pyq (1).json',
    'constitution': r'C:\Users\yedde\Downloads\indian_constitution_pyq (1).json',
    'minor_acts': r'C:\Users\yedde\Downloads\up_9_minor_acts_pyq.json',
    'tort_limitation_sra_trust_equity': r'C:\Users\yedde\Downloads\tort_limitation_sra_trust_equity_pyq.json',
    'tpa_contract': r'C:\Users\yedde\Downloads\tpa_contract_pyq.json',
    'jurisprudence_int_org': r'C:\Users\yedde\Downloads\jurisprudence_int_org_pyq.json'
}

for sub in sorted(os.listdir(base_tests)):
    sub_dir = os.path.join(base_tests, sub)
    if not os.path.isdir(sub_dir):
        continue
    tests = sorted(glob.glob(os.path.join(sub_dir, '*.json')))
    total_q = 0
    print(f"Subject: {sub} ({len(tests)} tests)")
    for t in tests:
        with open(t, 'r', encoding='utf-8') as f:
            d = json.load(f)
        q_count = len(d.get('questions', []))
        total_q += q_count
        first_q = d['questions'][0]['questionTextEn'][:40] if d.get('questions') else 'EMPTY'
        print(f"  {os.path.basename(t)}: {q_count} Qs | Q1: {first_q}")
    print(f"Total {sub} Qs: {total_q}\n")
