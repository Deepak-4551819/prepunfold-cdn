import json, os, re

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

legacy_patterns = [
    r'uee@', r'kewâ', r'cesÙ', r'fह्', r'™', r'०', r'f°', r'f§', r'fV',
    r'la@rd', r'\[thues', r'uewueer', r'\[uenewpeer', r'MewJeOece', r'oeceesoj',
    r'ueenewj', r'MesjMeen', r'cegncceo', r'cenelcee', r'ieebOeer', r'ieeBOeer',
    r'uegF', r'iJeso', r'बQटिक', r'क्QबिÇज', r'आ@', r'का@', r'ला@', r'ड@', r'पा@',
    r'fट्क', r'fट्व', r'fठ्', r'ø', r'æ', r'®', r'Ë', r'ü', r'õ', r'Ç', r'Œ'
]

compiled = [re.compile(p) for p in legacy_patterns]

for fname in files:
    fpath = os.path.join(CH_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        fields = [
            ('q_hi', q.get('questionTextHi', '')),
            ('exp_hi', q.get('explanationHi', '')),
            ('q_en', q.get('questionTextEn', '')),
            ('exp_en', q.get('explanationEn', '')),
            ('opts_hi', " | ".join(q.get('optionsHi', []))),
            ('opts_en', " | ".join(q.get('optionsEn', [])))
        ]
        for fld_name, text in fields:
            for cp in compiled:
                m = cp.findall(text)
                if m:
                    print(f"{fname} Q{q.get('questionNumber')} [{fld_name}]: pattern '{cp.pattern}' matched: {m}")
                    # Show surrounding snippet
                    match_obj = cp.search(text)
                    start = max(0, match_obj.start() - 20)
                    end = min(len(text), match_obj.end() + 20)
                    print(f"   Snippet: ...{text[start:end]}...")
