from rapidocr_onnxruntime import RapidOCR
from PIL import Image

ocr = RapidOCR()
img = Image.open('scripts/img_p62_2.png')
# let's upscale by 2x for better OCR
img_up = img.resize((img.width * 2, img.height * 2))
img_up.save('scripts/q62_up.png')
res, _ = ocr('scripts/q62_up.png')
print("Q62 nodes:")
for r in res:
    print(" ", r[1])
