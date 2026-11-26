import json
import os
import re

TESTS_DIR = "tests/tgt_pgt_history"

def find_contexts(char, max_samples=10):
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
    samples = []
    pattern = re.compile(rf'.{{0,30}}{re.escape(char)}.{{0,30}}')
    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for q in data.get('questions', []):
            qn = q.get('questionNumber')
            for field in ['questionTextHi', 'explanationHi']:
                val = str(q.get(field) or '')
                for m in pattern.findall(val):
                    samples.append((fname, qn, field, m))
                    if len(samples) >= max_samples:
                        return samples
            for opt in q.get('optionsHi', []):
                for m in pattern.findall(str(opt)):
                    samples.append((fname, qn, 'opt', m))
                    if len(samples) >= max_samples:
                        return samples
    return samples

if __name__ == '__main__':
    for ch in ['ä', '°', '@', 'å']:
        print(f"=== CONTEXTS FOR {repr(ch)} ===")
        for fn, qn, fld, snippet in find_contexts(ch, 10):
            print(f"  [{fn} Q{qn} {fld}]: ...{snippet}...")
