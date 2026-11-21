import pymupdf

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)

for p in range(27, 42):
    t = doc[p].get_text()
    if "88." in t:
        print(f"Page {p+1}:")
        idx = t.find("88.")
        print(t[idx:idx+500])
