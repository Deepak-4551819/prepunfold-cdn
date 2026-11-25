from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
res, _ = ocr('scripts/img_p55_2.jpeg')
for b in sorted(res, key=lambda r: (r[0][0][1], r[0][0][0])):
    x = int(b[0][0][0])
    y = int(b[0][0][1])
    print(f"y={y:3d}, x={x:4d}: {b[1]}")
