import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\Cr.PC Youth PYQ.pdf')

def split_en_hi(text_block):
    if '/' in text_block:
        return text_block.split('/')[0].strip()
    lines = [l.strip() for l in text_block.split('\n') if l.strip()]
    if not lines:
        return text_block.strip()
    en_lines = []
    for line in lines:
        has_akruti = any(ord(c) > 127 for c in line) or bool(re.search(r'(keâ|ef|me|ue|Je|Ce|Øe|›eâ|ne|le|Le|oe|Oe|ve|he|ye|Ye|ce|Ùe|Me|<e)', line))
        words = re.findall(r'[a-zA-Z]+', line)
        if len(words) > 0 and not has_akruti:
            en_lines.append(line)
        elif not en_lines:
            en_lines.append(line)
        else:
            break
    return ' '.join(en_lines).strip()

def find_4_options_sequential(s):
    m_a = re.search(r'(?:^|\n|\s)\(a\)\s*', s, re.I)
    if not m_a: return None
    m_b = re.search(r'(?:^|\n|\s)\(b\)\s*', s[m_a.end():], re.I)
    if not m_b: return None
    b_start = m_a.end() + m_b.start()
    b_end = m_a.end() + m_b.end()
    m_c = re.search(r'(?:^|\n|\s)\(c\)\s*', s[b_end:], re.I)
    if not m_c: return None
    c_start = b_end + m_c.start()
    c_end = b_end + m_c.end()
    m_d = re.search(r'(?:^|\n|\s)\(d\)\s*', s[c_end:], re.I)
    if not m_d: return None
    d_start = c_end + m_d.start()
    d_end = c_end + m_d.end()
    return [(m_a.start(), m_a.end()), (b_start, b_end), (c_start, c_end), (d_start, d_end)]

from test_crpc_questions import crpc_chapters

total_q = 0
total_full = 0
for ch_num, title, p_s, p_e in crpc_chapters:
    lines = []
    for p in range(p_s - 1, p_e):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s.startswith('oC[ Øeef›eâÙee mebefnlee') or re.match(r'^\d+$', s):
                continue
            lines.append(l)
    text = '\n'.join(lines)

    ans_matches = list(re.finditer(r'\nAns\s*[\.:]\s*\(([a-eA-E\*&, ]+)\)', text))
    ch_q = len(ans_matches)
    ch_full = 0
    for i, ans_m in enumerate(ans_matches):
        ans_start = ans_m.start()
        prev_ans_end = ans_matches[i-1].end() if i > 0 else 0
        window = text[prev_ans_end:ans_start]
        q_num_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*\.\s+', window))
        if q_num_matches:
            q_start_idx = prev_ans_end + q_num_matches[0].start()
        else:
            q_start_idx = prev_ans_end
        pre_ans = text[q_start_idx:ans_start].strip()
        pre_ans = re.sub(r'^\n?\s*\d+\s*\.\s*', '', pre_ans).strip()

        opt_ranges = find_4_options_sequential(pre_ans)
        if opt_ranges:
            ch_full += 1

    total_q += ch_q
    total_full += ch_full
    if ch_full < ch_q:
        print(f"Ch {ch_num:02d}: {title[:35]:<35} | {ch_full}/{ch_q} full options")

print("="*65)
print(f"CrPC Parsing Accuracy: {total_full}/{total_q} ({total_full/total_q*100:.1f}%)")
