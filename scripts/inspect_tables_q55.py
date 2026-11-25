from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
img = Image.open('scripts/img_p55_2.jpeg')
w, h = img.size
# 4 tables side by side: player, coach, team, members
# player roughly 0 to w*0.28, coach roughly 0.28 to 0.50, team 0.50 to 0.78, members 0.78 to 1.0
crops = {
    'player': img.crop((0, 0, int(w * 0.28), h)),
    'coach': img.crop((int(w * 0.28), 0, int(w * 0.50), h)),
    'team': img.crop((int(w * 0.50), 0, int(w * 0.78), h)),
    'members': img.crop((int(w * 0.78), 0, w, h)),
}

for name, cimg in crops.items():
    cimg.save(f"scripts/q55_{name}.png")
    res, _ = ocr(f"scripts/q55_{name}.png")
    print(f"=== Table: {name} ===")
    if res:
        for r in res:
            print(" ", r[1])
