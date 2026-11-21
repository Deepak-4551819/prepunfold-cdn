import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\CPC Youth PYQ.pdf')

# Extract pages 4 to 15 (Chapter 1)
lines = []
for p in range(3, 15):
    for l in doc[p].get_text().split('\n'):
        s = l.strip()
        if not s or s.startswith('YCT') or s == 'efmeefJeue Øeef›eâÙee mebefnlee, 1908' or re.match(r'^\d+$', s):
            continue
        lines.append(l)

text = '\n'.join(lines)

# Split by sequential questions
# Each question starts with: \n\s*\d+\.\s+
# But wait! In each chapter, question numbers are sequential: 1, 2, 3...
# Let's verify sequential finding

expected = 1
pos = 0
found_qs = []
while True:
    m = re.search(r'(?:^|\n)\s*' + str(expected) + r'\s*\.\s+', text[pos:])
    if not m:
        break
    q_start = pos + m.start()
    found_qs.append((expected, q_start))
    pos = q_start + len(m.group())
    expected += 1

print(f"Total sequential questions found in Chapter 1: {len(found_qs)}")

for i in range(min(5, len(found_qs))):
    num, start = found_qs[i]
    end = found_qs[i+1][1] if i + 1 < len(found_qs) else len(text)
    block = text[start:end]
    print(f"\n{'='*60}\n--- RAW QUESTION {num} ---\n{block}")
