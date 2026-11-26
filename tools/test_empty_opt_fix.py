import re

def fix_empty_options(options, pyq_tag):
    opts = list(options)
    pyq = pyq_tag

    # Case 2: all options clumped in opts[3] or opts[0]
    for idx in [3, 0]:
        clump = opts[idx]
        if clump and '(a)' in clump and '(b)' in clump and '(c)' in clump and '(d)' in clump:
            m = re.search(r'\(a\)\s*(.*?)\s*\(b\)\s*(.*?)\s*\(c\)\s*(.*?)\s*\(d\)\s*(.*)$', clump, re.DOTALL)
            if m:
                opts[0] = m.group(1).strip()
                opts[1] = m.group(2).strip()
                opts[2] = m.group(3).strip()
                opts[3] = m.group(4).strip()
                return opts, pyq

    # Case 1: opts[3] is empty and option D was swallowed into pyqTag
    if not opts[3] or opts[3].strip() == "":
        if pyq:
            # Check if pyq has a separator '|'
            if '|' in pyq:
                parts = pyq.split('|')
                cand_opt = parts[0].strip()
                rest_pyq = '|'.join(parts[1:]).strip()
                opts[3] = cand_opt
                pyq = rest_pyq
            else:
                # If pyq is just option text (e.g. '1934' or '1943')
                # and doesn't look like an exam name
                if not any(exam in pyq for exam in ['UP', 'PGT', 'TGT', 'UGC', 'NET', 'JRF', 'RPSC', 'KVS', 'NVS', 'GIC', 'GDC', 'Lect', 'Asst']):
                    opts[3] = pyq.strip()
                    pyq = "UP TGT/PGT History"

    return opts, pyq

# Test on samples
samples = [
    (['', '', '', '(a) iv ii iii i (b) ii iii i iv (c) ii iv iii i (d) iv i ii iii'], 'RPSC Asst. Prof. 2020 (I)'),
    (['1911', '1919', '1923', ''], '1934'),
    (['1900 F&.', '1901 F&.', '1902 F&.', ''], '1903 F&. | UKPSC Lecutrer Mains 2020'),
    (['1896 में', '1902 में', '1906 में', ''], '1935 ceW'),
]

for opts, pyq in samples:
    new_opts, new_pyq = fix_empty_options(opts, pyq)
    print("Orig Opts:", opts)
    print("Orig PYQ :", pyq)
    print("Fixed Opts:", new_opts)
    print("Fixed PYQ :", new_pyq)
    print()
