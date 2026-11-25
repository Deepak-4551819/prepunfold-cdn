import pymupdf

doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')
for p in [10, 11, 12]:
    print(f"=== PAGE {p} ===")
    print(doc[p-1].get_text())
    print()
