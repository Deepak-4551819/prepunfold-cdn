# -*- coding: utf-8 -*-
import json

files = {
    'cpc': r'C:\Users\yedde\Downloads\cpc_pyq.json',
    'crpc': r'C:\Users\yedde\Downloads\crpc_pyq.json',
    'evidence': r'C:\Users\yedde\Downloads\evidence_pyq (1).json',
    'ipc': r'C:\Users\yedde\Downloads\ipc_pyq (1).json',
    'constitution': r'C:\Users\yedde\Downloads\indian_constitution_pyq (1).json',
    'minor_acts': r'C:\Users\yedde\Downloads\up_9_minor_acts_pyq.json',
    'tort_lim_sra_trust': r'C:\Users\yedde\Downloads\tort_limitation_sra_trust_equity_pyq.json',
    'tpa_contract': r'C:\Users\yedde\Downloads\tpa_contract_pyq.json',
    'juris_int_org': r'C:\Users\yedde\Downloads\jurisprudence_int_org_pyq.json'
}

for name, p in files.items():
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    tot = 0
    missing_q_en = 0
    missing_q_hi = 0
    missing_opt_en = 0
    missing_opt_hi = 0
    missing_exp_en = 0
    for ch in d['chapters']:
        for q in ch['questions']:
            tot += 1
            if not (q.get('question_en') or '').strip():
                missing_q_en += 1
            if not (q.get('question_hi') or '').strip():
                missing_q_hi += 1
            opts_en = q.get('options_en') or {}
            opts_hi = q.get('options_hi') or {}
            if not any((v or '').strip() for v in opts_en.values()):
                missing_opt_en += 1
            if not any((v or '').strip() for v in opts_hi.values()):
                missing_opt_hi += 1
            if not (q.get('explanation_en') or '').strip():
                missing_exp_en += 1
    print(f"{name:20s}: Total={tot} | Missing Q_EN={missing_q_en}, Q_HI={missing_q_hi}, Opt_EN={missing_opt_en}, Opt_HI={missing_opt_hi}, Exp_EN={missing_exp_en}")
