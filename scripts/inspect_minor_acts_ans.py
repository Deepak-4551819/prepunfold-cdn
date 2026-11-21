import pymupdf

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)

print("--- PAGE 11 (End of Act 1) ---")
print(doc[10].get_text())

print("--- PAGE 80 (End of Act 9) ---")
print(doc[79].get_text()[-1000:])
