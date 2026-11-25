import pymupdf, re

doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')
print("Total pages:", len(doc))
for pno in range(len(doc)):
    text = doc[pno].get_text()
    m = re.findall(r'Q\s*\.\s*(\d+)\b', text)
    # filter out range like Q.1 - Q.5
    valid = []
    for num in m:
        # Check if preceded or followed by - or –
        if not re.search(rf'Q\s*\.\s*{num}\s*[-–]', text):
            valid.append(num)
    print(f"Page {pno+1}: Qs={valid}")
