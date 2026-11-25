import pymupdf

doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

for pno in [40, 53, 55, 57, 60, 62, 64]:
    page = doc[pno-1]
    print(f"=== PAGE {pno} WORDS ===")
    words = page.get_text("words")
    # print words that are not in the main question text
    for w in words:
        # w is (x0, y0, x1, y1, word, block_no, line_no, word_no)
        print(f"{w[4]}", end=" ")
    print("\n")
