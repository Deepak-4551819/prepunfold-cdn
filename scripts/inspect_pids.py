from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
img = Image.open('scripts/img_p55_2.jpeg')
# crop pid column in player: x from 0 to 80
c1 = img.crop((0, 0, 80, 288))
c1.save('scripts/c1_pid.png')
res1, _ = ocr('scripts/c1_pid.png')
print("player pid:", [r[1] for r in res1] if res1 else "none")

# crop members pid column: x from 1070 to 1160
c2 = img.crop((1070, 0, 1160, 288))
c2.save('scripts/c2_mem_pid.png')
res2, _ = ocr('scripts/c2_mem_pid.png')
print("members pid:", [r[1] for r in res2] if res2 else "none")
