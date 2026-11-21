import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\CPC Youth PYQ.pdf')

# Table of contents from Page 2
chapters_info = [
    (1, "Preliminary (Sec 1-8)", 4, 15),
    (2, "Jurisdiction and Res Judicata (Sec 9-14)", 16, 29),
    (3, "Place of Suing and Institution of Suits (Sec 15-26)", 30, 38),
    (4, "Summons and Discovery (Sec 27-32)", 39, 40),
    (5, "Judgment, Decree and Costs (Sec 33-35B)", 41, 42),
    (6, "Execution (Sec 36-74)", 43, 53),
    (7, "Incidental Proceedings (Sec 75-78)", 54, 54),
    (8, "Suits in Particular Cases (Sec 79-88)", 55, 59),
    (9, "Special Proceedings (Sec 89-93)", 60, 64),
    (10, "Supplemental Proceedings (Sec 94-95)", 65, 65),
    (11, "Appeals (Sec 96-112)", 66, 71),
    (12, "Reference, Review and Revision (Sec 113-115)", 72, 75),
    (13, "High Court Rules and Special Provisions (Sec 116-131)", 76, 76),
    (14, "Miscellaneous (Sec 132-158)", 76, 82),
    (15, "First Schedule (Orders 1-51)", 83, 159),
    (16, "Miscellaneous & Practice Questions", 160, 168)
]

total_qs = 0
for ch_num, title, p_start, p_end in chapters_info:
    # gather text
    lines = []
    for p in range(p_start - 1, p_end):
        lines.append(doc[p].get_text())
    text = '\n'.join(lines)

    # count answers
    ans_matches = re.findall(r'\nAns\.\s*\(([a-eA-E\*])\)', text)
    print(f"Ch {ch_num:02d}: {title:<55} | Pages {p_start:3d}-{p_end:3d} | Ans Count: {len(ans_matches):3d}")
    total_qs += len(ans_matches)

print("="*80)
print(f"Total counted across chapters: {total_qs}")
