# -*- coding: utf-8 -*-
import json
import re

blocks = json.load(open('temp_gate_pdfs/gate_ph_2026_raw_blocks.json', encoding='utf-8'))
keys_file = open('temp_gate_pdfs/gate_ph_2026_key.txt', encoding='utf-8').read().splitlines()

keys = {}
for line in keys_file:
    m = re.match(r'^(\d+)\s+2\s+(MCQ|MSQ|NAT)\s+(GA|PH)\s+(.+?)\s+(\d+)$', line.strip())
    if m:
        keys[int(m.group(1))] = {
            "type": m.group(2),
            "sec": m.group(3),
            "key": m.group(4).strip(),
            "marks": float(m.group(5))
        }

print(f"Loaded {len(keys)} official keys.")

for qn in range(1, 66):
    raw = blocks[str(qn)]
    k = keys[qn]
    print(f"\n==================== Q{qn} ({k['type']} {k['marks']}m Key: {k['key']}) ====================")
    lines = [l for l in raw.splitlines() if l.strip()]
    stem_lines = []
    opt_a, opt_b, opt_c, opt_d = None, None, None, None
    curr_opt = None
    curr_opt_lines = []

    # Simple option detector
    for line in lines:
        m_opt = re.match(r'^\(([A-D])\)\s*(.*)', line.strip())
        if m_opt:
            if curr_opt == 'A': opt_a = " ".join(curr_opt_lines).strip()
            elif curr_opt == 'B': opt_b = " ".join(curr_opt_lines).strip()
            elif curr_opt == 'C': opt_c = " ".join(curr_opt_lines).strip()
            elif curr_opt == 'D': opt_d = " ".join(curr_opt_lines).strip()
            curr_opt = m_opt.group(1)
            curr_opt_lines = [m_opt.group(2)]
        elif curr_opt is not None:
            curr_opt_lines.append(line.strip())
        else:
            stem_lines.append(line.strip())

    if curr_opt == 'A': opt_a = " ".join(curr_opt_lines).strip()
    elif curr_opt == 'B': opt_b = " ".join(curr_opt_lines).strip()
    elif curr_opt == 'C': opt_c = " ".join(curr_opt_lines).strip()
    elif curr_opt == 'D': opt_d = " ".join(curr_opt_lines).strip()

    stem = " ".join(stem_lines)
    print("STEM:", stem[:160])
    if k['type'] in ('MCQ', 'MSQ'):
        print("  A:", opt_a)
        print("  B:", opt_b)
        print("  C:", opt_c)
        print("  D:", opt_d)
