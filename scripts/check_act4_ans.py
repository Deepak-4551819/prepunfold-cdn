import pymupdf
import re

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)
page_text = doc[41].get_text() # Page 42

ans_matches = re.findall(r'(\d+)\.\s*\(([a-d])\)', page_text)
found_nums = set(int(num) for num, ans in ans_matches)
for i in range(1, 129):
    if i not in found_nums:
        print(f"Missing num: {i}")

# Print around missing num
lines = [l.strip() for l in page_text.split('\n') if l.strip()]
print("\nSample lines from page 42:")
print("\n".join(lines[-30:]))
