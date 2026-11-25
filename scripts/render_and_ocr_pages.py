import fitz
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = fitz.open("raw_pdfs/gate_cs/gate_cs_2025_q.pdf")

for p in [50, 60, 62, 64]:
    page = doc[p - 1]
    pix = page.get_pixmap(dpi=200)
    pix_path = f"scripts/rendered_p{p}.png"
    pix.save(pix_path)
    res, _ = ocr(pix_path)
    print(f"=== PAGE {p} RENDERED OCR ===")
    if res:
        for r in res:
            # print lines that look like diagram content
            print(" ", r[1])
