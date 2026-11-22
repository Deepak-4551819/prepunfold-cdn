# -*- coding: utf-8 -*-
import os
import glob
import json

base_dir = r'D:\Android Project\prepunfold-cdn\tests\judiciary_pyq'

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

for sub in sorted(os.listdir(base_dir)):
    sub_path = os.path.join(base_dir, sub)
    if not os.path.isdir(sub_path):
        continue
    tests = sorted(glob.glob(os.path.join(sub_path, '*.json')))
    print(f"=== {sub.upper()} ({len(tests)} tests in repo) ===")
    for tf in tests:
        fname = os.path.basename(tf)
        with open(tf, 'r', encoding='utf-8') as f:
            d = json.load(f)
        print(f"  {fname} -> titleEn='{d.get('titleEn')}' ({len(d.get('questions', []))} Qs)")
