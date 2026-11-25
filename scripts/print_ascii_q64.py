import numpy as np
from PIL import Image

arr = np.array(Image.open('scripts/img_p64_2.png').convert('L'))
# downsample to 80 cols
step_x = arr.shape[1] // 80
step_y = step_x * 2 # aspect ratio compensation
for y in range(0, arr.shape[0], step_y):
    row = arr[y, ::step_x]
    print("".join("#" if val < 180 else " " for val in row))
