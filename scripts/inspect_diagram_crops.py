from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
# Page 62 diagram:
img62 = Image.open("scripts/rendered_p62.png")
# w=1654, h=2339 at 200 dpi
w, h = img62.size
crop62 = img62.crop((int(w * 0.1), int(h * 0.28), int(w * 0.9), int(h * 0.42)))
crop62.save("scripts/diag_p62.png")
res62, _ = ocr("scripts/diag_p62.png")
print("=== Q62 DIAGRAM OCR ===")
if res62:
    for r in res62:
        print(" ", r[1])

# Page 64 diagram:
img64 = Image.open("scripts/rendered_p64.png")
crop64 = img64.crop((int(w * 0.1), int(h * 0.13), int(w * 0.9), int(h * 0.35)))
crop64.save("scripts/diag_p64.png")
res64, _ = ocr("scripts/diag_p64.png")
print("=== Q64 DIAGRAM OCR ===")
if res64:
    for r in res64:
        print(" ", r[1])
