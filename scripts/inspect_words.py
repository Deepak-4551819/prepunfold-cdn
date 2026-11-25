import fitz

doc = fitz.open("raw_pdfs/gate_cs/gate_cs_2025_q.pdf")
for p in [62, 64]:
    page = doc[p - 1]
    words = page.get_text("words")
    print(f"=== PAGE {p} WORDS ===")
    # sort by y, then x
    for w in sorted(words, key=lambda x: (x[1], x[0])):
        if 150 < w[1] < 400: # diagram region
            print(f"  y={int(w[1])}, x={int(w[0])}: {repr(w[4])}")
