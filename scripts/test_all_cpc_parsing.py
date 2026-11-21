import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\CPC Youth PYQ.pdf')

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
    (15, "First Schedule (Orders 1-10)", 83, 114),
    (16, "First Schedule (Orders 11-20)", 115, 124),
    (17, "First Schedule (Order 21)", 125, 132),
    (18, "First Schedule (Orders 22-32)", 133, 142),
    (19, "First Schedule (Orders 33-51)", 143, 159),
    (20, "Miscellaneous & Practice Questions", 160, 168)
]

def split_en_hi(text_block):
    if '/' in text_block:
        return text_block.split('/')[0].strip()
    lines = [l.strip() for l in text_block.split('\n') if l.strip()]
    if not lines:
        return text_block.strip()
    en_lines = []
    for line in lines:
        has_akruti = any(ord(c) > 127 for c in line) or bool(re.search(r'(keâ|ef|me|ue|Je|Ce|Øe|›eâ|ne|le|Le|oe|Oe|ve|he|ye|Ye|ce|Ùe|Me|<e)', line))
        words = re.findall(r'[a-zA-Z]+', line)
        if len(words) > 0 and not has_akruti:
            en_lines.append(line)
        elif not en_lines:
            en_lines.append(line)
        else:
            break
    return ' '.join(en_lines).strip()

total_extracted = 0

for ch_num, title, p_start, p_end in chapters_info:
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s == 'efmeefJeue Øeef›eâÙee mebefnlee, 1908' or re.match(r'^\d+$', s):
                continue
            lines.append(l)
    text = '\n'.join(lines)

    # In each chapter / sub-range, find Ans. matches
    ans_matches = list(re.finditer(r'\nAns\.\s*\(([a-eA-E\*&, ]+)\)\s*:?', text))

    # Also find question numbers
    q_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*\.\s+', text))

    print(f"Test {ch_num:02d}: {title:<52} | Ans: {len(ans_matches):3d} | Q tags: {len(q_matches):3d}")
    total_extracted += len(ans_matches)

print("="*75)
print(f"Total extracted across all 20 tests: {total_extracted}")
