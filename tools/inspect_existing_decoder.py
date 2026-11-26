with open('tools/test_clean_decode.py', 'r', encoding='utf-8') as f:
    text = f.read()
print("=== test_clean_decode.py ===")
print('\n'.join(text.splitlines()[:80]))
