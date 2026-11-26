import json
import os
import re

TESTS_DIR = "tests/tgt_pgt_history"
HINDI_RE = re.compile(r'[\u0900-\u097F]')
ARTIFACT_RE = re.compile(r'uee@|kewâ|cesÙ|fह्|[™०åäø§°\^@æ®]')

files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

hindi_in_en = []
artifacts_in_en = []

for fname in files:
    fpath = os.path.join(TESTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        qn = q.get('questionNumber')
        q_en = str(q.get('questionTextEn') or '')
        opts_en = [str(o) for o in q.get('optionsEn', [])]
        exp_en = str(q.get('explanationEn') or '')

        all_en = [q_en, exp_en] + opts_en
        for t in all_en:
            if HINDI_RE.search(t):
                hindi_in_en.append((fname, qn, t[:60]))
                break
        for t in all_en:
            if ARTIFACT_RE.search(t):
                artifacts_in_en.append((fname, qn, t[:60]))
                break

print(f"Total questions with Hindi characters in English fields: {len(hindi_in_en)}")
print(f"Total questions with Artifacts in English fields: {len(artifacts_in_en)}")
for fn, qn, snip in artifacts_in_en[:15]:
    print(f"  {fn} Q{qn}: {snip}")
