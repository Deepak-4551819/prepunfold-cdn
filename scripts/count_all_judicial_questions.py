import os
import pymupdf
import re

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

grand_total = 0

for fname in files:
    fpath = os.path.join(DIR_PATH, fname)
    doc = pymupdf.open(fpath)

    # Collect text from page 4 onwards (after index & trend analysis)
    lines = []
    for p in range(3, len(doc)):
        lines.append(doc[p].get_text())
    full_text = '\n'.join(lines)

    # Count Ans. matches
    ans_matches = re.findall(r'\nAns\.\s*\(([a-eA-E\*])\)', full_text)

    # Also find question numbers
    q_matches = re.findall(r'\n\s*(\d+)\s*\.\s+', full_text)

    print(f"{fname:<50} | Pages: {len(doc):3d} | Ans Count: {len(ans_matches):4d}")
    grand_total += len(ans_matches)

print("="*70)
print(f"Grand Total Questions across all 9 Judicial PDFs: {grand_total}")
