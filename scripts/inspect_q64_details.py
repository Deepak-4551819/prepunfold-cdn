from PIL import Image
import numpy as np

arr = np.array(Image.open('scripts/img_p64_2.png').convert('L'))
h, w = arr.shape
print(f"h={h}, w={w}")
# Let's inspect 4 corners and center:
# Top-left (node A/B), Top-right, Bottom-left, Bottom-right, Top-edge, Bottom-edge, Left-edge, Right-edge, Diagonals
regions = {
    'top_left': (0, 0, 70, 70),
    'top_right': (0, w-70, 70, w),
    'bottom_left': (h-70, 0, h, 70),
    'bottom_right': (h-70, w-70, h, w),
    'top_mid': (0, int(w*0.35), 50, int(w*0.65)),
    'bottom_mid': (h-50, int(w*0.35), h, int(w*0.65)),
    'left_mid': (int(h*0.35), 0, int(h*0.65), 50),
    'right_mid': (int(h*0.35), w-50, int(h*0.65), w),
    'center': (int(h*0.35), int(w*0.35), int(h*0.65), int(w*0.65)),
}

for name, (y1, x1, y2, x2) in regions.items():
    patch = arr[y1:y2, x1:x2]
    print(f"=== {name} ===")
    for r in patch[::2]:
        print("".join("#" if val < 160 else " " for val in r))
