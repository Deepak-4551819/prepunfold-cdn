from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
for q, path in [(62, "scripts/diag_p62.png"), (64, "scripts/diag_p64.png")]:
    res, _ = ocr(path)
    print(f"=== Q{q} ===")
    if res:
        for r in sorted(res, key=lambda b: (b[0][0][1], b[0][0][0])):
            print(f"  y={int(r[0][0][1])}, x={int(r[0][0][0])}: {r[1]}")
