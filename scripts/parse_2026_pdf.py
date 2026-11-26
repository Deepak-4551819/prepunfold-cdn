# -*- coding: utf-8 -*-
import fitz
import re

doc = fitz.open('temp_gate_pdfs/gate_ph_2026.pdf')

full_text = ""
for page_num in range(len(doc)):
    page_text = doc[page_num].get_text()
    full_text += f"\n--- PAGE {page_num + 1} ---\n" + page_text

with open('temp_gate_pdfs/gate_ph_2026_mupdf.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f"Extracted {len(full_text)} chars from {len(doc)} pages.")

# Search for Q.<num> occurrences
q_matches = list(re.finditer(r'Q\.(\d+)', full_text))
print(f"Found {len(q_matches)} question headers.")
seen = set()
for m in q_matches:
    num = int(m.group(1))
    seen.add(num)
print("Unique Q numbers found:", sorted(list(seen)))
missing = [i for i in range(1, 66) if i not in seen]
print("Missing Q numbers:", missing)
