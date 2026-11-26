import json, os, re

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

def fix_empty_options(options, pyq_tag, q_text):
    opts = [o.strip() if o else "" for o in options]
    pyq = pyq_tag.strip() if pyq_tag else ""

    # Clumped in any single option
    for idx in range(4):
        clump = opts[idx]
        if clump and '(a)' in clump and '(b)' in clump and '(c)' in clump and '(d)' in clump:
            m = re.search(r'\(a\)\s*(.*?)\s*\(b\)\s*(.*?)\s*\(c\)\s*(.*?)\s*\(d\)\s*(.*)$', clump, re.DOTALL)
            if m:
                opts[0] = m.group(1).strip()
                opts[1] = m.group(2).strip()
                opts[2] = m.group(3).strip()
                opts[3] = m.group(4).strip()
                break

    # Clumped in question text
    if any(not opt for opt in opts):
        if '(a)' in q_text and '(b)' in q_text and '(c)' in q_text and '(d)' in q_text:
            m = re.search(r'\(a\)\s*(.*?)\s*\(b\)\s*(.*?)\s*\(c\)\s*(.*?)\s*\(d\)\s*([^:\n\r]+)', q_text, re.DOTALL)
            if m:
                opts[0] = m.group(1).strip()
                opts[1] = m.group(2).strip()
                opts[2] = m.group(3).strip()
                opts[3] = m.group(4).strip()

    # Opt 3 empty and absorbed into pyqTag
    if not opts[3] and pyq:
        if '|' in pyq:
            parts = pyq.split('|')
            cand_opt = parts[0].strip()
            rest_pyq = '|'.join(parts[1:]).strip()
            opts[3] = cand_opt
            pyq = rest_pyq
        else:
            if not any(exam in pyq for exam in ['UP', 'PGT', 'TGT', 'UGC', 'NET', 'JRF', 'RPSC', 'KVS', 'NVS', 'GIC', 'GDC', 'Lect', 'Asst', 'Paper']):
                opts[3] = pyq.strip()
                pyq = "UP TGT/PGT History"

    # Opt 0, 1, 2 empty but present in q_text or pyq
    # If still empty options:
    return opts, pyq

unresolved = []
total_empty_orig = 0

for fname in files:
    with open(os.path.join(CH_DIR, fname), 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        opts_hi = q.get('optionsHi', [])
        if any(not o for o in opts_hi):
            total_empty_orig += 1
            fixed_opts, fixed_pyq = fix_empty_options(opts_hi, q.get('pyqTag', ''), q.get('questionTextHi', ''))
            if any(not o for o in fixed_opts):
                unresolved.append((fname, q.get('questionNumber'), q.get('pyqTag'), fixed_opts, q.get('questionTextHi')[:60]))

print(f"Total original questions with empty options: {total_empty_orig}")
print(f"Total unresolved after fix_empty_options: {len(unresolved)}")
for u in unresolved[:10]:
    print(" ", u)
