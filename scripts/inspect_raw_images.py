from PIL import Image
import numpy as np

for name in ['p62_2.png', 'p64_2.png']:
    img = Image.open(f"scripts/img_{name}")
    print(f"=== {name} ===")
    print(f"mode: {img.mode}, size: {img.size}")
    arr = np.array(img)
    print("arr shape:", arr.shape)
    if img.mode == 'RGBA':
        alpha = arr[:, :, 3]
        print(f"alpha min: {alpha.min()}, max: {alpha.max()}, non-zero: {(alpha > 0).sum()} / {alpha.size}")
        rgb = arr[:, :, :3]
        print(f"rgb min: {rgb.min()}, max: {rgb.max()}")
    elif img.mode == 'P':
        print("palette image")
    else:
        print(f"min: {arr.min()}, max: {arr.max()}, mean: {arr.mean():.1f}")
