# -*- coding: utf-8 -*-
import pymupdf

def dump_pages(pdf_path, q_markers):
    doc = pymupdf.open(pdf_path)
    print(f"=== {pdf_path} ===")
    for i, page in enumerate(doc):
        txt = page.get_text()
        matched = [m for m in q_markers if m in txt]
        if matched:
            imgs = page.get_images()
            print(f"\nPage {i+1} (matches={matched}, raster_images={len(imgs)}):")
            words = page.get_text("words")
            words.sort(key=lambda w: (round(w[1]/4)*4, w[0]))
            cur_y = None
            line = []
            for w in words:
                y = round(w[1]/4)*4
                if cur_y is None or abs(y - cur_y) > 4:
                    if line:
                        print(f"  [y={cur_y:4d}] {' '.join(line)}")
                    cur_y = y
                    line = [w[4]]
                else:
                    line.append(w[4])
            if line:
                print(f"  [y={cur_y:4d}] {' '.join(line)}")

dump_pages("temp_gate_pdfs/gate_ph_2025.pdf", ["Q.19", "Q.26", "Q.28", "Q.37", "Q.38", "Q.39", "Q.48", "Q.60", "Q.64", "Q.65"])
dump_pages("temp_gate_pdfs/gate_ph_2026.pdf", ["Q.7", "Q.22", "Q.31", "Q.43", "Q.44", "Q.54", "Q.60", "Q.64"])
