from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
for name in ['p50_2.jpeg', 'p62_2.png', 'p64_2.png']:
    path = f"scripts/img_{name}"
    img = Image.open(path)
    # composite onto white
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        bg = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        bg.paste(img, mask=img.split()[3])
        img = bg
    else:
        img = img.convert('RGB')
    out_path = f"scripts/white_{name}.png"
    img.save(out_path)
    res, _ = ocr(out_path)
    print(f"=== {name} ===")
    if res:
        for r in res:
            print(" ", r[1])
    else:
        print("  (still no text)")
