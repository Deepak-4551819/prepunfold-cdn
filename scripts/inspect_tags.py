# -*- coding: utf-8 -*-
import json
import re

for fname in [
    r'C:\Users\yedde\Downloads\cpc_pyq.json',
    r'C:\Users\yedde\Downloads\crpc_pyq.json',
    r'C:\Users\yedde\Downloads\evidence_pyq (1).json',
    r'C:\Users\yedde\Downloads\ipc_pyq (1).json',
    r'C:\Users\yedde\Downloads\indian_constitution_pyq (1).json',
    r'C:\Users\yedde\Downloads\up_9_minor_acts_pyq.json',
    r'C:\Users\yedde\Downloads\tort_limitation_sra_trust_equity_pyq.json',
    r'C:\Users\yedde\Downloads\tpa_contract_pyq.json',
    r'C:\Users\yedde\Downloads\jurisprudence_int_org_pyq.json'
]:
    with open(fname, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"=== {d.get('title')} ===")
    sample_q = d['chapters'][0]['questions'][0]
    print("Keys in question:", list(sample_q.keys()))
    print("Sample Q:", sample_q.get('question_number'), sample_q.get('question_en')[:50] if sample_q.get('question_en') else sample_q.get('question_hi')[:50])
