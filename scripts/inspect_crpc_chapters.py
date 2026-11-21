import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\Cr.PC Youth PYQ.pdf')

# Table of contents from Page 2 and 3
# Let's inspect page 2 and page 3 completely to extract all chapters and page numbers
p2 = doc[1].get_text()
p3 = doc[2].get_text()
full_toc = p2 + '\n' + p3

print("=== FULL TABLE OF CONTENTS ===")
for line in full_toc.split('\n'):
    line_s = line.strip()
    if '■' in line_s or '....' in line_s or re.search(r'\d+\s*[-–]\s*\d+', line_s):
        print(line_s)
