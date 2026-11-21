import pymupdf
import re

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)

# Let's inspect text of page 3, 20, 28, 68
for p in [2, 19, 27, 67]:
    print(f"=== PAGE {p+1} ===")
    t = doc[p].get_text()
    for q in [1, 2, 3]:
        m = re.search(rf'\n\s*{q}\.\s+(.*?)(?=\n\s*{q+1}\.|\Z)', t, re.DOTALL)
        if m:
            print(f"--- Q{q} ---")
            print(m.group(1)[:300])
