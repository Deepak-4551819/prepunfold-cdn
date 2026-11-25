import pymupdf, re, json
from test_regex_splits import extract_all_questions

k25 = {}
doc_k = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2025_k.pdf')
k_text = "\n".join([p.get_text() for p in doc_k])
lines = [l.strip() for l in k_text.splitlines() if l.strip()]
i = 0
while i < len(lines):
    line = lines[i]
    if line.isdigit() and 1 <= int(line) <= 65:
        qnum = int(line)
        if i + 5 < len(lines) and lines[i+2] in ['MCQ', 'MSQ', 'NAT']:
            k25[qnum] = {
                'qtype': lines[i+2],
                'sec': lines[i+3],
                'key': lines[i+4],
                'marks': float(lines[i+5])
            }
            i += 6
            continue
    i += 1

print(f"2025 Key loaded: {len(k25)} questions")
qs25 = extract_all_questions('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

for qnum in range(1, 66):
    chunk = qs25[qnum]
    kinfo = k25[qnum]
    # Check if question text has options
    print(f"Q{qnum:02d} [{kinfo['qtype']}, {kinfo['marks']}M, Key: {kinfo['key']}]: {chunk[:80].replace(chr(10), ' ')}")
