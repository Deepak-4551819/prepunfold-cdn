import numpy as np
from PIL import Image

arr = np.array(Image.open('scripts/img_p64_2.png').convert('L'))
# Crop around diagonals:
# diagonal A(35,35) to C(200, 230)
# diagonal B(35, 230) to D(200, 35)
crops = {
    'diag_AC_upper': arr[60:110, 80:130],
    'diag_BD_upper': arr[60:110, 135:185],
    'diag_AC_lower': arr[130:180, 135:185],
    'diag_BD_lower': arr[130:180, 80:130],
}

for name, patch in crops.items():
    print(f"=== {name} ===")
    for r in patch[::2]:
        print("".join("#" if val < 160 else " " for val in r))
