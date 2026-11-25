import pymupdf
import re

doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2024_q.pdf')

full_text = ""
for page in doc:
    full_text += page.get_text() + "\n---PAGE---\n"

# Search for Q.11, Q.12, Q.13, Q.14, Q.15
for qnum in range(11, 20):
    m = re.search(rf'Q\.{qnum}\s*\n(.*?)(?=Q\.{qnum+1}|\Z)', full_text, re.DOTALL)
    if m:
        print(f"=== OFFICIAL PDF Q.{qnum} ===")
        print(m.group(1)[:300].strip())
        print()
