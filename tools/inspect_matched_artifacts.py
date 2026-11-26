import json, os, re
from collections import Counter

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

legacy_patterns = [
    r'uee@', r'kewâ', r'cesÙ', r'fह्', r'™', r'०', r'f°', r'f§', r'fV',
    r'la@rd', r'\[thues', r'uewueer', r'\[uenewpeer', r'MewJeOece', r'oeceesoj',
    r'ueenewj', r'MesjMeen', r'cegncceo', r'cenelcee', r'ieebOeer', r'ieeBOeer',
    r'uegF', r'iJeso', r'बQटिक', r'क्QबिÇज', r'आ@', r'का@', r'ला@', r'ड@', r'पा@',
    r'fट्क', r'fट्व', r'fठ्', r'ø', r'æ', r'®', r'Ë', r'ü', r'õ', r'Ç', r'Œ'
]

pattern_counter = Counter()
sample_matches = {}

for fname in files:
    fpath = os.path.join(CH_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        fields = [
            q.get('questionTextHi', ''),
            q.get('explanationHi', ''),
            q.get('questionTextEn', ''),
            q.get('explanationEn', ''),
            " ".join(q.get('optionsHi', [])),
            " ".join(q.get('optionsEn', []))
        ]
        for text in fields:
            for p in legacy_patterns:
                m = re.findall(p, text)
                if m:
                    pattern_counter[p] += len(m)
                    if p not in sample_matches:
                        sample_matches[p] = (fname, q.get('questionNumber'), text[:100])

print("Matched artifact patterns count:")
for p, c in pattern_counter.most_common():
    print(f"  {p:<20}: {c}")
    fname, qnum, s = sample_matches[p]
    print(f"     Sample ({fname} Q{qnum}): {s}\n")
