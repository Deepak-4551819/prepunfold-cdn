import fitz

doc = fitz.open("raw_pdfs/gate_cs/gate_cs_2025_q.pdf")
for p in [50, 62, 64]:
    page = doc[p - 1]
    blocks = page.get_text("blocks")
    print(f"=== PAGE {p} BLOCKS ===")
    for b in blocks:
        # text is b[4]
        print(f"  ({int(b[0])},{int(b[1])})-({int(b[2])},{int(b[3])}): {repr(b[4][:80])}")
