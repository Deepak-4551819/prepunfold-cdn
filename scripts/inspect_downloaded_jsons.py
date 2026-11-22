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
    if not os.path.exists(p):
        print(f"Missing: {p}")
        continue
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    title = d.get('title')
    total_q = d.get('total_questions')
    chapters = d.get('chapters', [])
    print(f"=== {name.upper()} ===")
    print(f"  Title: {title}")
    print(f"  Total Qs in root: {total_q}, Chapters count: {len(chapters)}")
    for i, ch in enumerate(chapters):
        ch_id = ch.get('chapter_id')
        en_name = ch.get('chapter_name_en')
        hi_name = ch.get('chapter_name_hi')
        q_count = len(ch.get('questions', []))
        print(f"    Ch {i+1:02d}: id={ch_id}, Qs={q_count}, EN={en_name}, HI={hi_name}")
    print()
