import pymupdf, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from aps_decoder import decode_aps

PDF_PATH = r"C:\Users\yedde\Downloads\CIVICS_CHAPTER-WISE_SOLVED_PAPERS.pdf"

def clean_page(doc, p_idx):
    lines = doc[p_idx].get_text().splitlines()
    cleaned = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        if s.isdigit() and len(s) <= 4:
            continue
        if 'TGT PGT Civics Planner' in s or s == 'YCT':
            continue
        if '@Apnapdfs' in s or 'CLICK HERE' in s:
            continue
        cleaned.append(s)
    return '\n'.join(cleaned)

def parse_options_and_tags(opt_part_raw):
    opt_matches = list(re.finditer(r'(?:^|\s)(?:\(([a-eA-E])\)|([a-eA-E])\))\s*', opt_part_raw))
    if not opt_matches:
        return [], ""

    options_raw = {}
    for idx, om in enumerate(opt_matches):
        letter = (om.group(1) or om.group(2)).upper()
        start = om.end()
        end = opt_matches[idx+1].start() if idx + 1 < len(opt_matches) else len(opt_part_raw)
        options_raw[letter] = opt_part_raw[start:end].strip()

    last_letter = list(options_raw.keys())[-1]
    last_val = options_raw[last_letter]
    last_lines = [l.strip() for l in last_val.splitlines() if l.strip()]

    opt_d_lines = []
    tag_lines = []
    exam_kw = [
        'PGT', 'TGT', 'GIC', 'GDC', 'LT', 'NET', 'JRF', 'SET', 'Asst', 'Prof',
        'Lect', 'UPPCS', 'PSC', 'KVS', 'NVS', 'DSSSB', 'RPSC', 'JSSC', 'UKPSC',
        'BPSC', 'Exam', 'Shift', 'Paper', 'HPSC', 'MPPSC', 'CGPSC'
    ]

    is_tag = True
    for l in reversed(last_lines):
        if is_tag and (any(kw in l for kw in exam_kw) or re.search(r'\b(19\d\d|20\d\d)\b', l)):
            tag_lines.insert(0, l)
        else:
            is_tag = False
            opt_d_lines.insert(0, l)

    options_raw[last_letter] = ' '.join(opt_d_lines).strip()
    exam_tag = ' | '.join(tag_lines).strip()

    opt_list = []
    for l in ['A', 'B', 'C', 'D']:
        if l in options_raw and len(options_raw[l].strip()) > 0:
            decoded_opt = decode_aps(options_raw[l])
            decoded_opt = re.sub(r'\s+', ' ', decoded_opt).strip()
            if decoded_opt:
                opt_list.append(decoded_opt)

    return opt_list, exam_tag

doc = pymupdf.open(PDF_PATH)
sample_text = '\n'.join([clean_page(doc, p) for p in range(8, 25)])

ans_pattern = re.compile(r'(?:^|\n)\s*(Ans|Gòej)\s*[\.:-]*\s*(?:\n\s*)?\(?([a-eA-E\*])\)?\s*[:\.-]?', re.MULTILINE)
matches = list(ans_pattern.finditer(sample_text))
print(f"Found {len(matches)} Ans/Gòej matches in pages 9-25")

parsed_count = 0
for i, ans_m in enumerate(matches):
    marker_type = ans_m.group(1)
    correct_opt = ans_m.group(2).upper()
    if correct_opt == '*':
        correct_opt = 'A'

    next_boundary = matches[i+1].start() if i + 1 < len(matches) else len(sample_text)
    post_ans = sample_text[ans_m.end():next_boundary]

    extra_tag = ""
    if marker_type.lower() == 'gòej':
        vyakhya_m = re.search(r'JÙeeKÙee\s*[:–-]*\s*', post_ans)
        if vyakhya_m:
            extra_tag = post_ans[:vyakhya_m.start()].strip()
            explanation_raw = post_ans[vyakhya_m.end():]
        else:
            explanation_raw = post_ans
    else:
        explanation_raw = post_ans

    prev_boundary = matches[i-1].end() if i > 0 else 0
    pre_text = sample_text[prev_boundary:ans_m.start()]

    q_num_match = list(re.finditer(r'(?:^|\n)\s*(\d{1,4})\.\s*', pre_text))
    if not q_num_match:
        continue

    last_q = q_num_match[-1]
    book_q_num = int(last_q.group(1))
    q_body = pre_text[last_q.end():]

    first_opt = re.search(r'(?:^|\s)(?:\([aA]\)|[aA]\))\s*', q_body)
    if not first_opt:
        continue

    q_text_raw = q_body[:first_opt.start()]
    opt_part_raw = q_body[first_opt.start():]

    options, exam_tag = parse_options_and_tags(opt_part_raw)
    if extra_tag:
        clean_extra = decode_aps(extra_tag).strip()
        exam_tag = f"{exam_tag} | {clean_extra}".strip(" |")

    if len(options) >= 2:
        parsed_count += 1
        if parsed_count <= 8:
            print(f"Q{book_q_num} [{correct_opt}] Tag: {exam_tag}")
            print(f"  Q: {decode_aps(q_text_raw)[:80]}...")
            print(f"  Opts: {options[:2]}...")

print(f"\nTotal successfully parsed from sample: {parsed_count} / {len(matches)}")
