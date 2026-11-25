import numpy as np
from PIL import Image

img = Image.open('scripts/img_p55_2.jpeg').convert('L')
arr = np.array(img)
# Let's inspect rows around y=72, y=126, y=180, y=234 for x between 0 and 80
for y in [72, 126, 180, 234]:
    # crop a 30x40 patch around each number
    patch = arr[y-15:y+15, 10:50]
    print(f"y={y}: min={patch.min()}, max={patch.max()}, mean={patch.mean():.1f}")
