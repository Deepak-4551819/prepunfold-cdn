# -*- coding: utf-8 -*-
import pymupdf, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from aps_decoder import decode_aps

doc = pymupdf.open(r'C:\Users\yedde\Downloads\GEOGRAPHY CHAPTER-WISE SOLVED PAPERS.pdf')

def clean_page(p_idx):
    lines = doc[p_idx].get_text().splitlines()
    cleaned = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        if s.isdigit() and len(s) <= 4:
            continue
        if 'TGT/PGT Geography Planner' in s or s == 'YCT':
            continue
        if '@Apnapdfs' in s or 'CLICK HERE' in s:
            continue
        cleaned.append(l.strip())
    return '\n'.join(cleaned)

sample_text = '\n'.join([clean_page(p) for p in range(8, 14)])

ans_pattern = re.compile(r'(?:^|\n)\s*Ans\s*[\.:-]*\s*(?:\n\s*)?\(?([a-eA-E\*])\)?\s*[:\.-]?', re.MULTILINE)
matches = list(ans_pattern.finditer(sample_text))

for i in range(min(5, len(matches))):
    m = matches[i]
    prev_boundary = matches[i-1].end() if i > 0 else 0
    text_before = sample_text[prev_boundary:m.start()].strip()

    q_matches = list(re.finditer(r'(?:^|\n)\s*(\d{1,4})\.\s+', text_before))
    if not q_matches:
        continue
    last_q = q_matches[-1]

    q_and_opt = text_before[last_q.start():].strip()
    ans_letter = m.group(1).upper()

    # Split by options (a), (b), (c), (d)
    opt_m = re.search(r'(?:^|\n)\s*(?:\([a-eA-E]\)|[a-eA-E]\))\s*', q_and_opt)
    if not opt_m:
        continue

    q_text_raw = re.sub(r'^\d+\.\s*', '', q_and_opt[:opt_m.start()]).strip()
    opt_part_raw = q_and_opt[opt_m.start():].strip()

    # Split options
    opt_matches = list(re.finditer(r'(?:^|\s)(?:\(([a-eA-E])\)|([a-eA-E])\))\s*', opt_part_raw))
    options_raw = {}
    for idx, om in enumerate(opt_matches):
        letter = (om.group(1) or om.group(2)).upper()
        start = om.end()
        end = opt_matches[idx+1].start() if idx + 1 < len(opt_matches) else len(opt_part_raw)
        options_raw[letter] = opt_part_raw[start:end].strip()

    # Exam tag is usually at the end of the last option or on its own line
    last_letter = list(options_raw.keys())[-1]
    last_val = options_raw[last_letter]
    last_lines = [l.strip() for l in last_val.splitlines() if l.strip()]

    opt_d_lines = []
    tag_lines = []
    exam_kw = ['PGT', 'TGT', 'GIC', 'GDC', 'LT', 'NET', 'JRF', 'SET', 'Asst', 'Prof', 'Lect', 'UPPCS', 'PSC', 'KVS', 'NVS', 'DSSSB', 'RPSC', 'JSSC', 'UKPSC', 'BPSC']
    for l in last_lines:
        if any(kw in l for kw in exam_kw) or re.search(r'\b(19\d\d|20\d\d)\b', l):
            tag_lines.append(l)
        else:
            opt_d_lines.append(l)

    options_raw[last_letter] = ' '.join(opt_d_lines).strip()
    exam_tag = ' | '.join(tag_lines).strip()

    # Explanation
    next_boundary = matches[i+1].start() if i + 1 < len(matches) else len(sample_text)
    next_q_m = re.search(r'(?:^|\n)\s*\d{1,4}\.\s+', sample_text[m.end():next_boundary])
    if next_q_m:
        exp_raw = sample_text[m.end():m.end() + next_q_m.start()].strip()
    else:
        exp_raw = sample_text[m.end():next_boundary].strip()

    print(f"=== QUESTION #{last_q.group(1)} ===")
    print("Q_HI:", decode_aps(q_text_raw).replace('\n', ' '))
    print("OPTIONS:")
    for l in ['A', 'B', 'C', 'D']:
        if l in options_raw:
            print(f"  ({l.lower()}) {decode_aps(options_raw[l]).replace(chr(10), ' ')}")
    print("ANS:", ans_letter)
    print("TAG:", exam_tag)
    print("EXP:", decode_aps(exp_raw)[:150].replace('\n', ' '))
    print()
