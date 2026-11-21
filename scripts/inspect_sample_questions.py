import os
import pymupdf

DIR_PATH = r"C:\Users\yedde\Downloads\Judicial"

for pdf_name in ['CPC Youth PYQ.pdf', 'Indian Constitution Youth PYQ.pdf', 'IPC Youth PYQ-1.pdf']:
    fpath = os.path.join(DIR_PATH, pdf_name)
    doc = pymupdf.open(fpath)
    print(f"\n{'='*70}\n{pdf_name} - Page 5 Text Preview:\n{'='*70}")
    print(doc[4].get_text()[:2000])
