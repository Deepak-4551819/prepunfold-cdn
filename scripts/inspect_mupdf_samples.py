# -*- coding: utf-8 -*-
with open('temp_gate_pdfs/gate_ph_2026_mupdf.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for qn in [10, 11, 14, 16, 19, 21, 24, 25, 27, 28, 29, 30, 36, 38, 39, 40, 41]:
    pos = text.find(f"Q.{qn}\n")
    if pos == -1:
        pos = text.find(f"Q.{qn} ")
    if pos != -1:
        print(f"\n==================== Q.{qn} ====================")
        print(text[pos:pos+400])
