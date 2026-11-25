import pymupdf

doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2024_q.pdf')
text = doc[0].get_text()
for char in text:
    if ord(char) > 127:
        print(f"char: {char!r}, ord: {ord(char)}, hex: {hex(ord(char))}")
