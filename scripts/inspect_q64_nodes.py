from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
img = Image.open('scripts/img_p64_2.png')
# resize 3x
img_large = img.resize((img.width * 3, img.height * 3))
img_large.save('scripts/q64_large.png')
res, _ = ocr('scripts/q64_large.png')
print("Q64 OCR:")
if res:
    for r in res:
        print(" ", r[1])
