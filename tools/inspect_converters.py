import os

for path in ['scripts/kruti_converter.py', 'scripts/aps_decoder.py', 'tools/test_clean_decode.py']:
    if os.path.exists(path):
        print(f"=== {path} (first 40 lines) ===")
        with open(path, 'r', encoding='utf-8') as f:
            lines = [f.readline() for _ in range(40)]
            print("".join(lines))
