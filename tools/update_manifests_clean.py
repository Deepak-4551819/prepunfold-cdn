import json
import os

print("Updating manifests...")

# 1. Update manifest_tgt_pgt_history_master.json
with open('manifest_tgt_pgt_history_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

for t in master.get('tests', []):
    tid = t.get('testId', '')
    if tid == 'tgt_pgt_hist_ch25_governors_viceroys':
        t['totalQuestions'] = 56
        t['total_questions'] = 56
        t['maxMarks'] = 112.0
        t['max_marks'] = 112.0

    tq = t.get('totalQuestions', 0)
    dur = max(60, tq)
    t['durationMinutes'] = dur
    t['duration_minutes'] = dur

with open('manifest_tgt_pgt_history_master.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print(f"Updated manifest_tgt_pgt_history_master.json ({len(master.get('tests', []))} tests)")

# 2. Update manifest.json
with open('manifest.json', 'r', encoding='utf-8') as f:
    mf = json.load(f)

old_tests = mf.get('tests', [])
new_tests = []

removed_count = 0
for t in old_tests:
    tid = t.get('testId', '')
    cid = t.get('categoryId', '')
    fp = t.get('filePath', '') or t.get('path', '') or ''

    # Filter out old tgt_pgt_history tests:
    # They have categoryId == 'tgt_pgt_history' AND filePath under 'tests/teaching/tgt_pgt_history'
    if cid == 'tgt_pgt_history' and 'tests/teaching/tgt_pgt_history' in fp:
        removed_count += 1
        continue

    # If it is one of our 30 chapters, update totalQuestions and durationMinutes
    if tid.startswith('tgt_pgt_hist_ch'):
        if tid == 'tgt_pgt_hist_ch25_governors_viceroys':
            t['totalQuestions'] = 56
            t['total_questions'] = 56
            t['maxMarks'] = 112.0
            t['max_marks'] = 112.0
        tq = t.get('totalQuestions', 0)
        dur = max(60, tq)
        t['durationMinutes'] = dur
        t['duration_minutes'] = dur
    elif tid == 'tgt_pgt_hist_mock01_full_length':
        t['durationMinutes'] = 60
        t['duration_minutes'] = 60

    new_tests.append(t)

mf['tests'] = new_tests

with open('manifest.json', 'w', encoding='utf-8') as f:
    json.dump(mf, f, ensure_ascii=False, indent=2)

print(f"Updated manifest.json: removed {removed_count} old tests. Total tests now: {len(new_tests)}")

# Verify categoryId == 'tgt_pgt_history' in manifest.json
remaining_hist = [t for t in new_tests if t.get('categoryId') == 'tgt_pgt_history']
print(f"Remaining tgt_pgt_history tests in manifest.json: {len(remaining_hist)} (30 chapters + mock tests)")
for t in remaining_hist:
    print(f"  {t.get('testId')}: Qs={t.get('totalQuestions')}, Dur={t.get('durationMinutes')}, File={t.get('filePath')}")
