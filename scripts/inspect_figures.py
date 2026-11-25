import pymupdf

doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

for qnum in [40, 53, 55, 57, 60, 62, 64]:
    # find page where Q.qnum is
    for pno in range(len(doc)):
        text = doc[pno].get_text()
        if f"Q.{qnum}" in text:
            print(f"=== Q.{qnum} (Page {pno+1}) ===")
            print(text.strip())
            print()
            break
