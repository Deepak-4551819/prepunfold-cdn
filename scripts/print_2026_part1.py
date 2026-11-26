# -*- coding: utf-8 -*-
import json

blocks = json.load(open('temp_gate_pdfs/gate_ph_2026_raw_blocks.json', encoding='utf-8'))
for qn in range(1, 36):
    print(f"***** Q{qn} *****")
    print(blocks[str(qn)].strip())
    print()
