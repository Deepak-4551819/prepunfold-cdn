# -*- coding: utf-8 -*-
import json
import os

files = {
    'cpc': r'C:\Users\yedde\Downloads\cpc_pyq.json',
    'crpc': r'C:\Users\yedde\Downloads\crpc_pyq.json',
    'evidence': r'C:\Users\yedde\Downloads\evidence_pyq (1).json',
    'ipc': r'C:\Users\yedde\Downloads\ipc_pyq (1).json',
    'constitution': r'C:\Users\yedde\Downloads\indian_constitution_pyq (1).json',
    'up_9_minor_acts': r'C:\Users\yedde\Downloads\up_9_minor_acts_pyq.json',
    'tort_limitation_sra_trust_equity': r'C:\Users\yedde\Downloads\tort_limitation_sra_trust_equity_pyq.json',
    'tpa_contract': r'C:\Users\yedde\Downloads\tpa_contract_pyq.json',
    'jurisprudence_int_org': r'C:\Users\yedde\Downloads\jurisprudence_int_org_pyq.json'
}

for name, p in files.items():
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"=== {name} ({len(d.get('chapters', []))} chapters, {d.get('total_questions')} Qs) ===")
    for c in d.get('chapters', []):
        print(f"  Ch {c.get('chapter_id')}: Qs={len(c.get('questions', []))}, EN='{c.get('chapter_name_en')}', HI='{c.get('chapter_name_hi')}'")
