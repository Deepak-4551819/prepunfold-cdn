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

def split_en_hi(text_block):
    # If '/' in text
    if '/' in text_block:
        parts = text_block.split('/')
        return parts[0].strip()

    # Otherwise, split by lines
    lines = [l.strip() for l in text_block.split('\n') if l.strip()]
    if not lines:
        return text_block.strip()

    # Check if first line or lines are English
    # Characters in Akruti include lots of non-ascii or specific accented letters:
    # like 'keâ', 'ef', 'me', 'ue', 'Je', 'Ce', 'Øe', '›eâ'
    en_lines = []
    for line in lines:
        # Check if line contains common Akruti markers
        has_akruti = any(ord(c) > 127 for c in line) or bool(re.search(r'(keâ|ef|me|ue|Je|Ce|Øe|›eâ|ne|le|Le|oe|Oe|ve|he|ye|Ye|ce|Ùe|Me|<e)', line))
        words = re.findall(r'[a-zA-Z]+', line)
        # If words contain common english words
        has_eng_words = any(w.lower() in [
            'the', 'is', 'of', 'in', 'and', 'to', 'which', 'from', 'date', 'code', 'civil',
            'procedure', 'extends', 'act', 'court', 'suit', 'decree', 'order', 'section',
            'judgment', 'not', 'a', 'an', 'under', 'following', 'has', 'been', 'defined',
            'its', 'essential', 'element', 'plaint', 'rejection', 'holder', 'means', 'person',
            'favour', 'passed', 'capable', 'execution', 'made', 'foreign', 'judge', 'profit',
            'mesne', 'substantive', 'law', 'combination', 'prescriptive', 'apply', 'writ',
            'petitions', 'specifically', 'always', 'never', 'wrongful', 'possession', 'property',
            'pleader', 'prescribed', 'public', 'officer', 'jurisdiction', 'pecuniary', 'original',
            'value', 'instituted', 'district', 'high', 'senior', 'division', 'junior', 'statement',
            'only', 'both', 'neither', 'nor', 'all', 'above', 'none', 'preliminary', 'final',
            'partly', 'dismissal', 'default', 'conclusive', 'determination', 'rights', 'parties',
            'adjudication', 'formal', 'expression'
        ] for w in words)

        if has_eng_words:
            en_lines.append(line)
        elif not has_akruti:
            en_lines.append(line)
        elif not en_lines:
            en_lines.append(line)
        else:
            break

    return ' '.join(en_lines).strip()

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

parsed = []
for i in range(len(found_qs)):
    num, start = found_qs[i]
    end = found_qs[i+1][1] if i + 1 < len(found_qs) else len(text)
    clean = re.sub(r'^\n?\s*' + str(num) + r'\s*\.\s*', '', text[start:end]).strip()

    m_ans = re.search(r'\nAns\.\s*\(([a-eA-E\*&, ]+)\)\s*:?', clean)
    if not m_ans:
        continue
    ans_str = m_ans.group(1).upper()
    m_first = re.search(r'[A-E]', ans_str)
    correct_opt = m_first.group(0) if m_first else 'A'

    pre_ans = clean[:m_ans.start()].strip()
    explanation = clean[m_ans.end():].strip()

    opt_matches = list(re.finditer(r'(?:^|\n)\s*\(([a-d])\)\s*', pre_ans))
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

    q_en = split_en_hi(raw_stem)
    opts_en = [split_en_hi(o) for o in raw_options]

    # clean extra spaces
    q_en = re.sub(r'\s+', ' ', q_en).strip()
    opts_en = [re.sub(r'\s+', ' ', o).strip() for o in opts_en]

    parsed.append((num, q_en, opts_en, correct_opt, exam_tag))

print(f"Successfully parsed {len(parsed)} questions in Chapter 1")
for p in parsed[:10]:
    print(f"Q{p[0]:02d} [{p[3]}]: {p[1][:60]}... | Opts: {p[2]}")
