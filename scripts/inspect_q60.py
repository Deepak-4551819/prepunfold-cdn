from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
res, _ = ocr('scripts/img_p60_2.png')
for b in sorted(res, key=lambda r: (r[0][0][1], r[0][0][0])):
    print(f"y={int(b[0][0][1])}, x={int(b[0][0][0])}: {b[1]}")
