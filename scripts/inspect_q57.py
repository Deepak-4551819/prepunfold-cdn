from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
res, _ = ocr('scripts/img_p57_2.png')
for b in sorted(res, key=lambda r: (r[0][0][0])):
    print(f"x={int(b[0][0][0])}, y={int(b[0][0][1])}: {b[1]}")
