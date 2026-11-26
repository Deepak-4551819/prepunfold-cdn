import json
import os
import re

TESTS_DIR = "tests/tgt_pgt_history"
ARTIFACT_PATTERNS = [
    r'uee@', r'kewâ', r'cesÙ', r'fह्',
    r'[™०åäø§°\^@æ®]'
]
ARTIFACT_REGEX = re.compile('|'.join(ARTIFACT_PATTERNS))

def inspect():
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
    artifact_occurrences = {}
    sample_same_opts = []

    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for q in data.get('questions', []):
            q_num = q.get('questionNumber')
            # Check Hindi text
            for field in ['questionTextHi', 'explanationHi']:
                val = str(q.get(field) or '')
                for m in ARTIFACT_REGEX.findall(val):
                    artifact_occurrences[m] = artifact_occurrences.get(m, 0) + 1
            for opt in q.get('optionsHi', []):
                for m in ARTIFACT_REGEX.findall(str(opt)):
                    artifact_occurrences[m] = artifact_occurrences.get(m, 0) + 1

            # Check same options
            opts_hi = [str(o).strip() for o in q.get('optionsHi', [])]
            opts_en = [str(o).strip() for o in q.get('optionsEn', [])]
            if opts_hi and opts_en and opts_hi == opts_en:
                if len(sample_same_opts) < 15:
                    sample_same_opts.append((fname, q_num, opts_hi))

    print("Artifact frequencies in Hindi fields:")
    for k, v in sorted(artifact_occurrences.items(), key=lambda x: -x[1]):
        print(f"  {repr(k)}: {v} occurrences")

    print("\nSample 'optsEn == optsHi' occurrences:")
    for fn, qn, opts in sample_same_opts:
        print(f"  {fn} Q{qn}: {opts}")

if __name__ == '__main__':
    inspect()
