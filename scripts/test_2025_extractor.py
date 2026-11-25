import pymupdf, re, json
from test_regex_splits import extract_all_questions

# Load answer key
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

qs25 = extract_all_questions('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

def clean_math_unicode(text):
    # Mathematical italic letters
    res = []
    for c in text:
        cp = ord(c)
        if 0x1d434 <= cp <= 0x1d44d: # Cap A-Z
            res.append(chr(ord('A') + cp - 0x1d434))
        elif 0x1d44e <= cp <= 0x1d467: # Small a-z
            res.append(chr(ord('a') + cp - 0x1d44e))
        elif 0x1d468 <= cp <= 0x1d481: # Bold italic A-Z
            res.append(chr(ord('A') + cp - 0x1d468))
        elif cp == 0x210e: # h
            res.append('h')
        elif cp == 0x2212: # minus
            res.append('-')
        elif cp == 0x2018 or cp == 0x2019:
            res.append("'")
        elif cp == 0x201c or cp == 0x201d:
            res.append('"')
        elif cp == 0x2013 or cp == 0x2014:
            res.append('-')
        elif cp == 0x2192:
            res.append('->')
        elif cp == 0x2227:
            res.append(' AND ')
        elif cp == 0x2208:
            res.append(' in ')
        elif cp == 0x2264:
            res.append('<=')
        elif cp == 0x2265:
            res.append('>=')
        elif cp == 0x2260:
            res.append('!=')
        elif cp == 0x222a:
            res.append(' U ')
        elif cp == 0x2229:
            res.append(' cap ')
        elif cp == 0x3dc: # Digamma / F
            res.append('F')
        elif cp == 0x1d6fc: # alpha
            res.append('alpha')
        elif cp == 0x1d6fd: # beta
            res.append('beta')
        elif cp == 0x1d716: # epsilon
            res.append('epsilon')
        elif cp == 0xac: # not
            res.append('NOT ')
        else:
            res.append(c)
    return "".join(res)

print("Testing extraction on all 65 questions of 2025:")
for qnum in range(1, 66):
    raw_chunk = qs25[qnum]
    meta = k25[qnum]
    qtype = meta['qtype']

    # Check options
    if qtype in ['MCQ', 'MSQ']:
        opt_matches = list(re.finditer(r'(?:^|\n)\s*\(([A-D])\)\s*', raw_chunk))
        if len(opt_matches) == 4:
            q_text = raw_chunk[:opt_matches[0].start()].strip()
            opts = []
            for j in range(4):
                start = opt_matches[j].end()
                end = opt_matches[j+1].start() if j < 3 else len(raw_chunk)
                opts.append(raw_chunk[start:end].strip())
            # print success summary
        else:
            print(f"Q{qnum} {qtype} options count mismatch: {len(opt_matches)} (matches: {[m.group(1) for m in opt_matches]})")
    else:
        # NAT
        q_text = raw_chunk.strip()

print("Extraction check complete.")
