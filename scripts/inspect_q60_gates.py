from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
img = Image.open('scripts/img_p60_2.png')
# let's crop the bottom and feedback lines
w, h = img.size
crops = {
    'd0_input': img.crop((0, 0, int(w*0.35), h)),
    'feedback': img.crop((0, int(h*0.5), w, h))
}
for name, c in crops.items():
    c.save(f"scripts/q60_{name}.png")
    res, _ = ocr(f"scripts/q60_{name}.png")
    print(f"=== {name} ===")
    if res:
        for r in res:
            print(" ", r[1])
