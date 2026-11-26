import json
import os
import re

TESTS_DIR = "tests/tgt_pgt_history"
HINDI_CHAR_RE = re.compile(r'[\u0900-\u097F]')

files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
hindi_same_opts = []

for fname in files:
    fpath = os.path.join(TESTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        opts_hi = [str(o).strip() for o in q.get('optionsHi', [])]
        opts_en = [str(o).strip() for o in q.get('optionsEn', [])]
        if opts_hi and opts_en and opts_hi == opts_en:
            has_hindi = any(HINDI_CHAR_RE.search(o) for o in opts_hi)
            if has_hindi:
                hindi_same_opts.append((fname, q.get('questionNumber'), opts_hi))

print(f"Total questions where optsEn == optsHi AND contains Hindi characters: {len(hindi_same_opts)}")
for fn, qn, opts in hindi_same_opts[:20]:
    print(f"  {fn} Q{qn}: {opts}")
