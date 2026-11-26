import pymupdf
import re
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from test_ch2_parse import parse_blocks

doc = pymupdf.open("HISTORY CHAPTER-WISE SOLVED PAPERS.pdf")
blocks = parse_blocks(doc, 33, 59)
full_text = "\n".join([b[4] for b in blocks])

ans_pattern = re.compile(r'(?:^|\n)\s*(?:Ans|Gòej|Ans\.)[\s\.:\-\u2013\u2500–—]*\(?([a-eA-E\*])\)?', re.MULTILINE)
matches = list(ans_pattern.finditer(full_text))

bad_opts = []
for i, m in enumerate(matches):
    prev_boundary = matches[i-1].end() if i > 0 else 0
    pre_text = full_text[prev_boundary:m.start()]
    found_nums = list(re.finditer(r'(?:^|\n)\s*(\d{1,4})\.\s*', pre_text))
    if not found_nums:
        continue
    candidates = [int(fn.group(1)) for fn in found_nums]
    q_num = min(candidates, key=lambda x: abs(x - (i+1)))

    # Body after question number
    # find the position of this q_num in pre_text
    match_pos = [fn for fn in found_nums if int(fn.group(1)) == q_num][-1]
    body = pre_text[match_pos.end():]

    # Find options (a), (b), (c), (d)
    opt_matches = list(re.finditer(r'(?:^|\n|\s)(?:\(([a-dA-D])\)|([a-dA-D])\))\s*', body))
    # Deduplicate by option letter
    seen_letters = set()
    valid_opts = []
    for om in opt_matches:
        l = (om.group(1) or om.group(2)).lower()
        if l not in seen_letters:
            seen_letters.add(l)
            valid_opts.append((l, om.start(), om.end()))

    if len(seen_letters) < 4:
        bad_opts.append((q_num, len(seen_letters), [v[0] for v in valid_opts]))

print(f"Total Qs: {len(matches)}")
print(f"Bad options count: {len(bad_opts)}")
if bad_opts:
    print(f"First 10 bad options: {bad_opts[:10]}")
