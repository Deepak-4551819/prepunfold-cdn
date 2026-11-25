import pymupdf, unicodedata
from collections import Counter

def inspect_chars(pdf_path):
    doc = pymupdf.open(pdf_path)
    chars = Counter()
    for page in doc:
        for c in page.get_text():
            if ord(c) > 127:
                chars[c] += 1
    print(f"=== {pdf_path} ===")
    for c, count in chars.most_common():
        name = unicodedata.name(c, 'UNKNOWN')
        print(f"  {c!r} ({hex(ord(c))}, {count:3d}x): {name}")

inspect_chars('raw_pdfs/gate_cs/gate_cs_2024_q.pdf')
inspect_chars('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')
