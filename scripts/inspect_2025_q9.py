import pymupdf
doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')
print("Page 9 text:")
print(doc[8].get_text())
