import pymupdf

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)

# Look at page 11 (doc[10])
page = doc[10]
blocks = page.get_text("blocks")
print(f"Page 11 blocks: {len(blocks)}")
for b in blocks:
    txt = b[4].strip()
    first_line = txt.split('\n')[0] if txt else ''
    last_line = txt.split('\n')[-1] if txt else ''
    print(f"({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}): '{first_line}' ... '{last_line}' (len {len(txt)})")
