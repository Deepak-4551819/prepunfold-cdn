import json, os, re
from collections import Counter

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

artifact_counter = Counter()

# Exclude valid Latin terms in questions/explanations (like standard dates/names/tags)
EXCLUDE_TERMS = {
    'A', 'B', 'C', 'D', 'a', 'b', 'c', 'd', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
    'UP', 'PGT', 'TGT', 'UGC', 'NET', 'JRF', 'RPSC', 'KVS', 'NVS', 'GIC', 'GDC', 'BC', 'AD', 'UPPCS',
    'Pre', 'Mains', 'Spl', 'Shift', 'Dec', 'June', 'July', 'Nov', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
    'History', 'Planner', 'YCT', 'Click', 'Here', 'Publication', 'Books', 'Dr', 'Prof', 'ASI', 'GSI', 'IAS',
    'PCS', 'UKPSC', 'MPPSC', 'CGPSC', 'Lect', 'Asst', 'Exam'
}

for fname in files:
    with open(os.path.join(CH_DIR, fname), 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        for field in ['questionTextHi', 'explanationHi']:
            val = q.get(field, '')
            tokens = re.findall(r'[a-zA-Z0-9@â™®æ~^`§©\u2217\u00d7\u00f8\u00b0]+', val)
            for t in tokens:
                if t not in EXCLUDE_TERMS and not t.isdigit():
                    artifact_counter[t] += 1
        for opt in q.get('optionsHi', []):
            tokens = re.findall(r'[a-zA-Z0-9@â™®æ~^`§©\u2217\u00d7\u00f8\u00b0]+', opt)
            for t in tokens:
                if t not in EXCLUDE_TERMS and not t.isdigit():
                    artifact_counter[t] += 1

print(f"Total distinct legacy artifact tokens: {len(artifact_counter)}")
print("Top 100 most frequent artifact tokens:")
for t, count in artifact_counter.most_common(100):
    print(f"  {t:<25} : {count}")
