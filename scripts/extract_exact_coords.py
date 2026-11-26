# -*- coding: utf-8 -*-
import pymupdf

def dump_words(pdf_path, pages):
    doc = pymupdf.open(pdf_path)
    for pno in pages:
        page = doc[pno-1]
        print(f"\n=== {pdf_path} Page {pno} ===")
        words = page.get_text("words")
        # sort by y0 (rounded to 3pt) then x0
        words.sort(key=lambda w: (round(w[1]/4)*4, w[0]))
        lines = []
        cur_y = None
        cur_line = []
        for w in words:
            y = round(w[1]/4)*4
            if cur_y is None or abs(y - cur_y) > 4:
                if cur_line:
                    lines.append((cur_y, " ".join(cur_line)))
                cur_y = y
                cur_line = [f"{w[4]}"]
            else:
                cur_line.append(f"{w[4]}")
        if cur_line:
            lines.append((cur_y, " ".join(cur_line)))
        for y, l in lines:
            print(f"  [y={y:4d}] {l}")

dump_words("temp_gate_pdfs/gate_ph_2024_official.pdf", [31, 42])
dump_words("temp_gate_pdfs/gate_ph_2022_official.pdf", [21, 40, 41])
dump_words("temp_gate_pdfs/gate_ph_2023_official.pdf", [48])
