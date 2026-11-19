# -*- coding: utf-8 -*-
import pymupdf, re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\GEOGRAPHY CHAPTER-WISE SOLVED PAPERS.pdf')
page = doc[8] # page 9

# Let's extract sentences and print raw characters alongside their hex/ord values
text = doc[8].get_text()
for line in text.splitlines()[:20]:
    if line.strip():
        print(f"RAW: {line}")
