from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
for name in ['player', 'coach', 'team', 'members']:
    res, _ = ocr(f"scripts/q55_{name}.png")
    print(f"*** {name} ***")
    # sort by y then x
    boxes = sorted(res, key=lambda r: (r[0][0][1], r[0][0][0]))
    for b in boxes:
        print(f"  y={int(b[0][0][1])}, x={int(b[0][0][0])}: {b[1]}")
