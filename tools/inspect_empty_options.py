import json, os

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

for fname in files:
    with open(os.path.join(CH_DIR, fname), 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data.get('questions', [])
    for q in qs:
        opts_hi = q.get('optionsHi', [])
        opts_en = q.get('optionsEn', [])
        if any(not opt or opt.strip() == "" for opt in opts_hi) or any(not opt or opt.strip() == "" for opt in opts_en):
            print(f"{fname} Q{q.get('questionNumber')}:")
            print(f"  PYQ: {q.get('pyqTag')}")
            print(f"  TextHi: {q.get('questionTextHi')[:80]}")
            print(f"  OptsHi: {opts_hi}")
            print(f"  OptsEn: {opts_en}")
