import pymupdf

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)
page_text = doc[41].get_text()

lines = page_text.split('\n')
for i, line in enumerate(lines):
    if '87.' in line or '89.' in line or '88' in line:
        print(f"Line {i}: {line}")
