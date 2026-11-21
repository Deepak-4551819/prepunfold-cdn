import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\CPC Youth PYQ.pdf')

lines = []
for p in range(3, 15):
    for l in doc[p].get_text().split('\n'):
        s = l.strip()
        if not s or s.startswith('YCT') or s == 'efmeefJeue Øeef›eâÙee mebefnlee, 1908' or re.match(r'^\d+$', s):
            continue
        lines.append(l)

text = '\n'.join(lines)

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

def clean_q_block(block, num):
    # Strip leading question number
    clean = re.sub(r'^\n?\s*' + str(num) + r'\s*\.\s*', '', block).strip()

    # Find Ans
    m_ans = re.search(r'\nAns\.\s*\(([a-eA-E\*&, ]+)\)\s*:?', clean)
    if not m_ans:
        return None
    ans_str = m_ans.group(1).upper()
    m_first = re.search(r'[A-E]', ans_str)
    correct_opt = m_first.group(0) if m_first else 'A'

    pre_ans = clean[:m_ans.start()].strip()
    explanation = clean[m_ans.end():].strip()

    # Options (a), (b), (c), (d)
    opt_matches = list(re.finditer(r'(?:^|\n|\s)\(([a-d])\)\s*', pre_ans))
    filtered_opts = []
    expected_letter = 'a'
    for m in opt_matches:
        if m.group(1).lower() == expected_letter:
            filtered_opts.append(m)
            expected_letter = chr(ord(expected_letter) + 1)
            if expected_letter > 'd':
                break

    if len(filtered_opts) == 4:
        raw_stem = pre_ans[:filtered_opts[0].start()].strip()
        raw_options = []
        for j in range(4):
            opt_s = filtered_opts[j].end()
            opt_e = filtered_opts[j+1].start() if j + 1 < 4 else len(pre_ans)
            raw_options.append(pre_ans[opt_s:opt_e].strip())

        # Last option might contain exam tag
        d_lines = raw_options[3].split('\n')
        exam_tag = ""
        actual_d_lines = []
        for l in d_lines:
            ls = l.strip()
            if re.search(r'(P\.C\.S|I\.A\.S|U\.P|M\.P|R\.O|A\.R\.O|B\.P|R\.A\.S|Uttarakhand|Jharkhand|Chhattisgarh|Bihar|Rajasthan|Haryana|MPHC|UPPCS|BPSC|RJS|JS|CJ|Pre|Mains|\b\d{4}\b)', ls, re.I) and len(actual_d_lines) > 0:
                exam_tag = (exam_tag + " " + ls).strip()
            else:
                actual_d_lines.append(l)
        raw_options[3] = '\n'.join(actual_d_lines).strip()
    else:
        raw_stem = pre_ans
        raw_options = ["", "", "", ""]
        exam_tag = ""

    # Clean options: keep English part before '/'
    options_en = []
    for opt in raw_options:
        opt_single = re.sub(r'\s+', ' ', opt).strip()
        if '/' in opt_single:
            parts = opt_single.split('/')
            opt_en = parts[0].strip()
        else:
            # maybe on separate lines
            lines_opt = opt.split('\n')
            opt_en = lines_opt[0].strip()
        options_en.append(opt_en)

    # Question stem: English part before '/' or before first line with high non-ASCII / Akruti
    stem_single = re.sub(r'\s+', ' ', raw_stem).strip()
    if '/' in raw_stem:
        q_en = raw_stem.split('/')[0].strip()
    else:
        # Check lines
        lines_stem = raw_stem.split('\n')
        en_lines = []
        for l in lines_stem:
            ls = l.strip()
            # If line is predominantly English ASCII words
            words = re.findall(r'[a-zA-Z]+', ls)
            # Check if this line looks like English
            if len(words) > 0 and not any(ord(c) > 127 for c in ls):
                # But wait, Akruti also uses ASCII like 'keâewve meer'
                # Let's see if words are English dictionary words or contain 'keâ'
                if any(w.lower() in ['the', 'is', 'of', 'in', 'and', 'to', 'which', 'from', 'date', 'code', 'civil', 'procedure', 'extends', 'act', 'court', 'suit', 'decree', 'order', 'section', 'judgment'] for w in words):
                    en_lines.append(ls)
                elif not en_lines:
                    en_lines.append(ls)
            elif not en_lines:
                en_lines.append(ls)
        q_en = ' '.join(en_lines).strip()

    q_en = re.sub(r'\s+', ' ', q_en).strip()

    return {
        "num": num,
        "q_en": q_en,
        "options_en": options_en,
        "correct_opt": correct_opt,
        "exam_tag": exam_tag,
        "explanation": explanation
    }

for i in range(len(found_qs)):
    num, start = found_qs[i]
    end = found_qs[i+1][1] if i + 1 < len(found_qs) else len(text)
    block = text[start:end]
    res = clean_q_block(block, num)
    if res:
        print(f"Q{res['num']:02d} [{res['correct_opt']}]: {res['q_en'][:70]}... | Opts: {res['options_en']} | Tag: {res['exam_tag']}")
