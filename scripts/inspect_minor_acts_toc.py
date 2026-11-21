import pymupdf

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)
print("--- TOC (Page 2) ---")
print(doc[1].get_text())
