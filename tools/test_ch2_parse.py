import pymupdf
import re
import json

def parse_blocks(doc, start_page, end_page):
    blocks_all = []
    for p in range(start_page - 1, end_page):
        page = doc[p]
        blocks = page.get_text("blocks")
        # filter header and footer
        content = [b for b in blocks if b[1] > 35 and b[3] < 805 and b[4].strip()]
        # separate columns
        col1 = sorted([b for b in content if b[0] < 290], key=lambda b: b[1])
        col2 = sorted([b for b in content if b[0] >= 290], key=lambda b: b[1])
        blocks_all.extend(col1)
        blocks_all.extend(col2)
    return blocks_all

doc = pymupdf.open("HISTORY CHAPTER-WISE SOLVED PAPERS.pdf")
blocks = parse_blocks(doc, 33, 59)
print(f"Total blocks in Ch 2: {len(blocks)}")
full_text = "\n".join([b[4] for b in blocks])

ans_pattern = re.compile(r'(?:^|\n)\s*(?:Ans|Gòej|Ans\.)[\s\.:\-\u2013\u2500–—]*\(?([a-eA-E\*])\)?', re.MULTILINE)
matches = list(ans_pattern.finditer(full_text))
print(f"Total Ans matches: {len(matches)}")

q_list = []
for i, m in enumerate(matches):
    prev_boundary = matches[i-1].end() if i > 0 else 0
    pre_text = full_text[prev_boundary:m.start()]
    # look for question number
    found_nums = list(re.finditer(r'(?:^|\n)\s*(\d{1,4})\.\s*', pre_text))
    if found_nums:
        candidates = [int(fn.group(1)) for fn in found_nums]
        # pick closest to i+1
        best_num = min(candidates, key=lambda x: abs(x - (i+1)))
        q_list.append((best_num, m.group(1).upper()))

print(f"Total parsed Qs: {len(q_list)}")
nums = [q[0] for q in q_list]
print(f"Unique Q numbers: {len(set(nums))}")
missing = [n for n in range(1, 210) if n not in nums]
print(f"Missing Q numbers: {missing}")
