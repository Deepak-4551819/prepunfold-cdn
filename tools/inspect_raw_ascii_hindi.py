import json
import os
import re

TESTS_DIR = "tests/tgt_pgt_history"
# Detect KrutiDev / APS words (words with English letters mixed with symbols or common KrutiDev patterns)
KRUTI_WORD_RE = re.compile(r'\b[a-zA-Z]{2,}[@&âäåéèêëïîôöûü°§æ®\[\]<>\\]+[a-zA-Z0-9]*\b|\b[a-zA-Z]{3,}\b')

# Note that purely English words like 'A', 'B', 'C', 'D' or 'None' or known English words shouldn't trigger,
# but words in questionTextHi or optionsHi that are KrutiDev gibberish like 'kegâcnejieerjer', 'JesoeW', 'Yee<ee'
KRUTI_SAMPLES = []

def has_krutidev_in_hindi(text):
    if not text:
        return []
    words = re.findall(r'[a-zA-Z@âäåéèêëïîôöûü°§æ®\[\]<>\\&]+', text)
    suspicious = []
    for w in words:
        if len(w) >= 3 and any(c in w for c in '@âäåéèêëïîôöûü°§æ®[]<>\\&'):
            suspicious.append(w)
        elif len(w) >= 4 and any(c.isupper() for c in w) and any(c.islower() for c in w) and not w.startswith('http'):
            # Mixed case like 'JesoeW', 'Yee<ee', 'keäÙee'
            suspicious.append(w)
    return suspicious

for fname in sorted(os.listdir(TESTS_DIR)):
    if not fname.startswith('tgt_pgt_hist_ch') or not fname.endswith('.json'):
        continue
    fpath = os.path.join(TESTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        qn = q.get('questionNumber')
        q_hi = str(q.get('questionTextHi') or '')
        susp = has_krutidev_in_hindi(q_hi)
        for opt in q.get('optionsHi', []):
            susp.extend(has_krutidev_in_hindi(str(opt)))
        if susp:
            KRUTI_SAMPLES.append((fname, qn, susp[:5]))

print(f"Total questions with KrutiDev gibberish in Hindi text/options: {len(KRUTI_SAMPLES)}")
for fn, qn, words in KRUTI_SAMPLES[:25]:
    print(f"  {fn} Q{qn}: {words}")
