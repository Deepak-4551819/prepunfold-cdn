import os
import pymupdf

DIR_PATH = r"C:\Users\yedde\Downloads\Judicial"
files = [
    'CPC Youth PYQ.pdf',
    'Cr.PC Youth PYQ.pdf',
    'Evidence Youth PYQ(2)(1).pdf',
    'IPC Youth PYQ-1.pdf',
    'Indian Constitution Youth PYQ.pdf',
    'TPA and Contract Act Youth PYQ(1).pdf',
    'Tort, Limitation, SRA, Trust and Equity Youth PYQ.pdf',
    'Juris. & Int. Organization Youth PYQ.pdf',
    'UP (GS) 9 miner Act Youth PYQ(3).pdf'
]

for fname in files:
    fpath = os.path.join(DIR_PATH, fname)
    doc = pymupdf.open(fpath)
    print(f"\n{'='*70}\nFILE: {fname} (Total Pages: {len(doc)})\n{'='*70}")
    # Inspect pages 1, 2, 3, 4
    for p in range(1, min(4, len(doc))):
        print(f"--- Page {p+1} ---")
        text = doc[p].get_text()
        print(text[:1500])
