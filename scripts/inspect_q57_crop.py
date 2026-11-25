from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
img = Image.open('scripts/img_p57_2.png')
w, h = img.size
# 3 segments
c1 = img.crop((0, 0, int(w*0.4), h))
c2 = img.crop((int(w*0.3), 0, int(w*0.7), h))
c3 = img.crop((int(w*0.6), 0, w, h))

for idx, c in enumerate([c1, c2, c3], 1):
    c.save(f"scripts/q57_link{idx}.png")
    res, _ = ocr(f"scripts/q57_link{idx}.png")
    print(f"=== Link {idx} ===")
    if res:
        for r in res:
            print(" ", r[1])
