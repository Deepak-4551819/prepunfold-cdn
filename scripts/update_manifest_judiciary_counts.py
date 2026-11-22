# -*- coding: utf-8 -*-
import json
import glob
import os

MANIFEST_PATH = r'D:\Android Project\prepunfold-cdn\manifest.json'

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

old_version = manifest.get('manifest_version', 29)
new_version = old_version + 1
manifest['manifest_version'] = new_version
manifest['manifestVersion'] = new_version

print(f"Bumping manifest_version: {old_version} -> {new_version}")

# Map file path to actual question count
test_files = sorted(glob.glob(r'tests/judiciary_pyq/**/*.json', recursive=True))
file_counts = {}
for tf in test_files:
    rel = tf.replace('\\', '/')
    with open(tf, 'r', encoding='utf-8') as f:
        d = json.load(f)
    cnt = len(d.get('questions', []))
    tid = d.get('testId')
    file_counts[tid] = (cnt, rel)

updated_entries = 0
for test_entry in manifest.get('tests', []):
    tid = test_entry.get('testId') or test_entry.get('test_id')
    if tid in file_counts:
        cnt, rel = file_counts[tid]
        test_entry['totalQuestions'] = cnt
        test_entry['total_questions'] = cnt
        test_entry['durationMinutes'] = cnt
        test_entry['duration_minutes'] = cnt
        test_entry['path'] = rel
        test_entry['cdnUrl'] = f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel}"
        test_entry['json_url'] = f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel}"
        test_entry['version'] = new_version
        updated_entries += 1

print(f"Updated {updated_entries} test entries in manifest.json.")

# Also update categories / parts total questions if present
for cat in manifest.get('categories', []):
    if cat.get('categoryId') == 'judiciary_pyq' or cat.get('category_id') == 'judiciary_pyq':
        tot_q = sum(v[0] for v in file_counts.values())
        cat['totalQuestions'] = tot_q
        cat['total_questions'] = tot_q
        print(f"Updated category judiciary_pyq total questions to {tot_q}")

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print("Saved manifest.json successfully.")
