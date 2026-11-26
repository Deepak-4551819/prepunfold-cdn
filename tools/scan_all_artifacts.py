import json
import os
import re

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

# Regex to find non-Devanagari, non-standard ASCII punctuation/digits in Hindi fields
hindi_fields = ['questionTextHi', 'optionsHi', 'explanationHi', 'question_hi', 'options_hi', 'explanation_hi']

all_artifacts = {}
empty_options_count = 0
untranslated_en_count = 0

for fname in files:
    with open(os.path.join(CH_DIR, fname), 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data.get('questions', [])

    file_artifacts = set()
    file_empty_opts = 0
    file_same_en_hi = 0

    for q in qs:
        # Check empty options
        opts_hi = q.get('optionsHi', [])
        opts_en = q.get('optionsEn', [])
        for i, opt in enumerate(opts_hi):
            if not opt or opt.strip() == "":
                file_empty_opts += 1
        for i, opt in enumerate(opts_en):
            if not opt or opt.strip() == "":
                file_empty_opts += 1

        # Check same en/hi
        q_en = q.get('questionTextEn', '').strip()
        q_hi = q.get('questionTextHi', '').strip()
        if q_en == q_hi and len(q_en) > 0:
            file_same_en_hi += 1

        # Scan for legacy artifacts in Hindi fields
        for field in ['questionTextHi', 'explanationHi']:
            val = q.get(field, '')
            # Look for legacy font patterns: e.g. latin letters mixed into hindi words, or symbols like @, â, ™, etc.
            matches = re.findall(r'[a-zA-Z@â™®æ~^`§©\u2217]+', val)
            for m in matches:
                # Exclude standard English abbreviations if any
                if m not in ('A', 'B', 'C', 'D', 'a', 'b', 'c', 'd', 'I', 'II', 'III', 'IV', 'UP', 'PGT', 'TGT', 'UGC', 'NET', 'JRF', 'RPSC', 'KVS', 'NVS', 'GIC', 'GDC', 'BC', 'AD'):
                    file_artifacts.add(m)

        for opt in opts_hi:
            matches = re.findall(r'[a-zA-Z@â™®æ~^`§©\u2217]+', opt)
            for m in matches:
                if m not in ('A', 'B', 'C', 'D', 'a', 'b', 'c', 'd', 'I', 'II', 'III', 'IV'):
                    file_artifacts.add(m)

    empty_options_count += file_empty_opts
    untranslated_en_count += file_same_en_hi
    print(f"{fname:<52} | Qs: {len(qs):<4} | Same En/Hi: {file_same_en_hi:<4} | Empty Opts: {file_empty_opts:<2} | Artifacts: {len(file_artifacts)}")
    if file_artifacts:
        sample = list(file_artifacts)[:8]
        print(f"    Sample artifacts: {sample}")

print("=" * 80)
print(f"Total Untranslated (Same En/Hi) Questions: {untranslated_en_count}")
print(f"Total Empty Options: {empty_options_count}")
