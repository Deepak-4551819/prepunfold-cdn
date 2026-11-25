import pymupdf, re

def check_extraction(pdf_path, key_path):
    doc = pymupdf.open(pdf_path)
    print(f"=== {pdf_path} ({len(doc)} pages) ===")

    # Concatenate all page texts
    pages_text = []
    for pno, page in enumerate(doc):
        t = page.get_text()
        pages_text.append(t)
    full = "\n".join(pages_text)

    # Count Q.1 to Q.65
    found_qs = {}
    for q in range(1, 66):
        # Match Q.1 or Q. 1
        matches = list(re.finditer(rf'(?:^|\n)\s*Q\s*\.\s*{q}\b', full))
        if matches:
            found_qs[q] = len(matches)
        else:
            found_qs[q] = 0

    missing = [q for q, count in found_qs.items() if count == 0]
    multi = [q for q, count in found_qs.items() if count > 1]
    print(f"Found: {len([q for q, c in found_qs.items() if c > 0])}/65")
    if missing:
        print("Missing questions:", missing)
    if multi:
        print("Multiple matches for questions:", multi)

check_extraction('raw_pdfs/gate_cs/gate_cs_2024_q.pdf', 'raw_pdfs/gate_cs/gate_cs_2024_k.pdf')
check_extraction('raw_pdfs/gate_cs/gate_cs_2025_q.pdf', 'raw_pdfs/gate_cs/gate_cs_2025_k.pdf')
