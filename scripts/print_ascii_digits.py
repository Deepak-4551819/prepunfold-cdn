import numpy as np
from PIL import Image

arr = np.array(Image.open('scripts/img_p55_2.jpeg').convert('L'))

print("=== PLAYER PIDS ===")
for y in [72, 126, 180, 234]:
    patch = arr[y-12:y+15, 10:45]
    print(f"--- y={y} ---")
    for r in patch[::2]: # skip every other row for aspect ratio
        line = "".join("#" if val < 150 else " " for val in r)
        print(line)

print("=== MEMBERS PIDS ===")
for y in [72, 126, 180, 234]:
    patch = arr[y-12:y+15, 1090:1135]
    print(f"--- y={y} ---")
    for r in patch[::2]:
        line = "".join("#" if val < 150 else " " for val in r)
        print(line)
