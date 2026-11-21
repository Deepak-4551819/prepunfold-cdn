import pymupdf

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)

for page_num in [2, 3, 11, 12, 19, 20, 27, 28, 42, 43, 52, 53, 62, 63, 64, 65, 67, 68, 79]:
    page = doc[page_num]
    rect = page.rect
    # 2 columns? Let's check blocks
    blocks = page.get_text("blocks")
    print(f"=== PAGE {page_num+1} (Total blocks: {len(blocks)}) ===")
    for b in blocks[:5]:
        print(f"Block ({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}):")
        lines = b[4].strip().split("\n")
        print("   " + "\n   ".join(lines[:4]))
