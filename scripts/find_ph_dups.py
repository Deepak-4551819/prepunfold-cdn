# -*- coding: utf-8 -*-
import json
import glob
import re
from collections import defaultdict

def norm(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]', '', text)
    return text[:60]

all_qs = defaultdict(list)
files = sorted(glob.glob('tests/gate/gate_ph/**/*.json', recursive=True))
print(f"Scanning {len(files)} gate_ph files...")

for f in files:
    d = json.load(open(f, encoding='utf-8'))
    for q in d.get('questions', []):
        t = norm(q.get('questionTextEn', ''))
        if t:
            all_qs[t].append((f.replace('\\', '/'), q.get('questionNumber')))

dups = {k: v for k, v in all_qs.items() if len(v) > 1}
print(f"Total duplicate question clusters in tests/gate/gate_ph: {len(dups)}")
for k, v in list(dups.items())[:20]:
    fnames = [x[0] for x in v]
    print(f"\nCluster ({len(v)} occurrences):")
    for fname, qn in v:
        print(f"  {fname} #Q{qn}")
