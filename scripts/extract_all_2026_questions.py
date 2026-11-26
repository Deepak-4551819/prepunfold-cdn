# -*- coding: utf-8 -*-
import re
import json

with open('temp_gate_pdfs/gate_ph_2026_mupdf.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's clean headers/footers
# Organizing Institute: IIT Guwahati Page X of 40
cleaned = re.sub(r'Organizing Institute: IIT Guwahati\s+Page \d+ of 40', '', text)
cleaned = re.sub(r'--- PAGE \d+ ---\s+Physics \(PH\)', '', cleaned)
cleaned = re.sub(r'General Aptitude \(GA\)', '', cleaned)
cleaned = re.sub(r'Q\.\d+\s*–\s*Q\.\d+\s*Carry (ONE|TWO) marks? Each', '', cleaned)

# Find all Q.<num> blocks
q_blocks = {}
matches = list(re.finditer(r'(?:^|\n)Q\.(\d+)\s*\n', cleaned))
for i, m in enumerate(matches):
    qnum = int(m.group(1))
    start_pos = m.end()
    end_pos = matches[i+1].start() if i + 1 < len(matches) else len(cleaned)
    q_blocks[qnum] = cleaned[start_pos:end_pos].strip()

print(f"Extracted {len(q_blocks)} question blocks.")

with open('temp_gate_pdfs/gate_ph_2026_raw_blocks.json', 'w', encoding='utf-8') as f:
    json.dump(q_blocks, f, indent=2, ensure_ascii=False)

for qn in [1, 2, 10, 11, 28, 29, 36, 65]:
    print(f"\n--- Q{qn} raw block ---")
    print(q_blocks.get(qn, 'MISSING')[:300])
