import json

with open('manifest_tgt_pgt_history_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

with open('manifest.json', 'r', encoding='utf-8') as f:
    mf = json.load(f)

existing_tids = {t.get('testId') for t in mf.get('tests', [])}
mock01 = next((t for t in master.get('tests', []) if t.get('testId') == 'tgt_pgt_hist_mock01_full_length'), None)

if mock01 and mock01.get('testId') not in existing_tids:
    # Add right before or after history chapters
    idx = 0
    for i, t in enumerate(mf['tests']):
        if t.get('testId', '').startswith('tgt_pgt_hist_ch'):
            idx = i
            break
    mf['tests'].insert(idx, mock01)
    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(mf, f, ensure_ascii=False, indent=2)
    print("Added tgt_pgt_hist_mock01_full_length to manifest.json!")
else:
    print("mock01 already present or not found in master.")
