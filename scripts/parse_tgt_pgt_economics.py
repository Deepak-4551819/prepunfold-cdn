import pymupdf, re, json, os
from collections import defaultdict, Counter

PDF_PATH = r"C:\Users\yedde\Downloads\Economics_Chapter-Wise_Solved_Papers_ENGLISH_MEDIUM.pdf"

CHAPTERS = [
    (7, 28, "Definition and Nature of Economics"),
    (29, 85, "Demand Analysis & Elasticity"),
    (86, 152, "Theory of Consumer Behaviour & Indifference Curve"),
    (153, 225, "Production Function, Cost & Law of Production"),
    (226, 315, "Equilibrium of the Firm & Market Structures"),
    (316, 352, "Theory of Distribution, Profit & Interest"),
    (353, 425, "Theory of Employment, Multiplier & IS-LM"),
    (426, 438, "Theory of Trade Cycle"),
    (439, 449, "Theory of Public Finance"),
    (450, 460, "Private and Public Goods"),
    (461, 515, "Budget, Fiscal Policy & Economic Survey"),
    (516, 566, "Theory of Taxation & Classification of Taxes"),
    (567, 585, "Public Debt & Finance Commission"),
    (586, 604, "Value of Money and Measurement"),
    (605, 632, "Quantity Theory of Money"),
    (633, 659, "Money Inflation & Phillips Curve"),
    (660, 718, "Monetary Policy & Banking Institutions"),
    (719, 731, "Monetary Institutions"),
    (732, 786, "Theory of International Trade & Terms of Trade"),
    (787, 815, "Foreign Exchange Rate & Devaluation"),
    (816, 837, "Balance of Payments"),
    (838, 874, "International Economic Institutions"),
    (875, 951, "Economic Growth, Development & Five Year Plans"),
    (952, 1031, "Theories of Economic Growth & Welfare Economics"),
    (1032, 1055, "Population Theory & Population Policy"),
    (1056, 1096, "National Income Accounting"),
    (1097, 1120, "Poverty and Unemployment"),
    (1121, 1160, "Agriculture, Rural Development & Food Security"),
    (1161, 1182, "Industrial Policy & MSME"),
    (1183, 1288, "Statistics, Central Tendency & Correlation"),
    (1289, 1328, "Miscellaneous Applied Economics")
]

def clean_page(text):
    lines = text.splitlines()
    cleaned = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        if s.isdigit() and len(s) <= 4:
            continue
        if s in ('TGT/PGT Economics Planner', 'YCT', 'Join @Yctbooks', 'CLICK HERE - JOIN @YCTBOOKS'):
            continue
        if 'CLICK HERE - JOIN' in s or '@YCTBOOKS' in s:
            continue
        cleaned.append(s)
    return '\n'.join(cleaned)

EXAM_INLINE_REGEX = re.compile(
    r'(\s+)(UP\s+PGT|UP\s+TGT|RPSC|KVS|NVS|DSSSB|TNPSC|Punjab\s+Lect|APPSC|UKPSC|MP\s+Assistant|JSSC|UPPSC\s+GDC|Uttarakhand\s+GIC|LT\s+Grade|NET|SET|TRB|SSB|WBPSC|WB\s+SET|UGC|UPPCS|BPSC|Kerala\s+Set|MH\s+SET|Haryana\s+PGT).*$',
    re.IGNORECASE
)

EXAM_LINE_REGEX = re.compile(
    r'^(UP\s+PGT|UP\s+TGT|RPSC|KVS|NVS|DSSSB|TNPSC|Punjab\s+Lect|APPSC|UKPSC|MP\s+Assistant|JSSC|UPPSC\s+GDC|Uttarakhand\s+GIC|LT\s+Grade|NET|SET|TRB|SSB|WBPSC|WB\s+SET|UGC|UPPCS|BPSC|Kerala\s+Set|MH\s+SET|Haryana\s+PGT|GDC|GIC).*$',
    re.IGNORECASE
)

def parse_options_and_tags(opt_block):
    pattern = re.compile(r'(?:^|\s)(?:\(([a-eA-E])\)|([a-eA-E])\))\s*')
    matches = list(pattern.finditer(opt_block))
    if not matches:
        return [], ''

    options = {}
    for i, m in enumerate(matches):
        letter = (m.group(1) or m.group(2)).upper()
        start = m.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(opt_block)
        val = opt_block[start:end].strip()
        options[letter] = val

    last_letter = list(options.keys())[-1]
    last_val = options[last_letter]
    last_lines = [l.strip() for l in last_val.splitlines() if l.strip()]

    opt_lines = []
    tag_lines = []

    for l in last_lines:
        inline_m = EXAM_INLINE_REGEX.search(l)
        if inline_m:
            prefix = l[:inline_m.start()].strip()
            suffix = l[inline_m.start():].strip()
            if prefix:
                opt_lines.append(prefix)
            if suffix:
                tag_lines.append(suffix)
        elif EXAM_LINE_REGEX.match(l) or (re.search(r'\b(19\d\d|20\d\d)\b', l) and any(kw in l.lower() for kw in ['paper', 'shift', 'exam', 'set', 'pre', 'mains', 'lect', 'pgt', 'tgt'])):
            tag_lines.append(l)
        else:
            opt_lines.append(l)

    options[last_letter] = ' '.join(opt_lines).strip()
    exam_tag = ' | '.join(tag_lines).strip()

    opt_list = []
    for l in ['A', 'B', 'C', 'D']:
        if l in options and len(options[l].strip()) > 0:
            opt_list.append(re.sub(r'\s+', ' ', options[l]).strip())

    return opt_list, exam_tag

def parse_chapter(doc, start_p, end_p, chapter_title):
    pages_text = []
    for p in range(start_p - 1, min(end_p, len(doc))):
        pages_text.append(clean_page(doc[p].get_text()))
    full_text = '\n'.join(pages_text)

    ans_pattern = re.compile(r'(?:^|\n)\s*Ans\s*[\.:-]*\s*(?:\n\s*)?\(?([a-eA-E\*])\)?\s*[:\.-]?', re.MULTILINE)
    matches = list(ans_pattern.finditer(full_text))

    questions = []
    for i, m in enumerate(matches):
        prev_boundary = matches[i-1].end() if i > 0 else 0
        between_prev_and_ans = full_text[prev_boundary:m.start()]

        q_matches = list(re.finditer(r'(?:^|\n)\s*(\d{1,4})\.\s+', between_prev_and_ans))
        if not q_matches:
            continue
        last_q = q_matches[-1]

        if questions:
            questions[-1]['explanation'] = re.sub(r'\s+', ' ', between_prev_and_ans[:last_q.start()].strip())

        q_and_opt = between_prev_and_ans[last_q.start():].strip()
        ans_letter = m.group(1).upper()

        opt_m = re.search(r'(?:^|\n)\s*(?:\([a-eA-E]\)|[a-eA-E]\))\s*', q_and_opt)
        if not opt_m:
            continue

        q_text = re.sub(r'^\d+\.\s*', '', q_and_opt[:opt_m.start()]).strip()
        q_text = re.sub(r'\s+', ' ', q_text)
        opt_part = q_and_opt[opt_m.start():].strip()

        opts, exam_tag = parse_options_and_tags(opt_part)
        if len(opts) != 4 or any(len(o) == 0 for o in opts):
            continue
        if ans_letter not in ['A', 'B', 'C', 'D']:
            continue
        if len(q_text) < 5:
            continue

        questions.append({
            'q_num_book': int(last_q.group(1)),
            'chapter': chapter_title,
            'questionText': q_text,
            'options': opts,
            'correctOption': ans_letter,
            'examTag': exam_tag if exam_tag else "TGT/PGT Economics Solved Papers",
            'explanation': ''
        })

    if questions and matches:
        last_exp = full_text[matches[-1].end():matches[-1].end()+1000].strip()
        next_q = re.search(r'(?:^|\n)\s*\d{1,4}\.\s+', last_exp)
        if next_q:
            last_exp = last_exp[:next_q.start()]
        questions[-1]['explanation'] = re.sub(r'\s+', ' ', last_exp.strip())

    # Filter out any questions with empty explanation
    final_questions = []
    for q in questions:
        if len(q['explanation'].strip()) >= 5:
            final_questions.append(q)

    return final_questions

def main():
    print(f"Opening {PDF_PATH}...")
    doc = pymupdf.open(PDF_PATH)
    all_questions = []

    for start_p, end_p, ch_name in CHAPTERS:
        ch_qs = parse_chapter(doc, start_p, end_p, ch_name)
        print(f"Chapter '{ch_name}' (pp. {start_p}-{end_p}): {len(ch_qs)} valid questions extracted.")
        all_questions.extend(ch_qs)

    print(f"\nTOTAL VALID QUESTIONS EXTRACTED: {len(all_questions)}")

    out_file = r"scripts/extracted_tgt_pgt_economics_master.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"Saved master questions cache to {out_file} ({os.path.getsize(out_file) / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    main()
