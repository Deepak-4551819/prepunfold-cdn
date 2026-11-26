import json
import os

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

total_qs = 0
print(f"Found {len(files)} chapter files in {CH_DIR}:")
print("-" * 92)
print(f"{'File':<52} | {'Qs':<5} | {'Keys':<5} | {'Opts':<5} | {'Marks':<5} | Range")
print("-" * 92)

errors = []
chapter_counts = {}

for fname in files:
    path = os.path.join(CH_DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data.get('questions', [])
    q_count = len(qs)
    total_qs += q_count
    chapter_counts[fname] = q_count

    # Check keys & options
    keys_ok = all(len(q.keys()) >= 40 for q in qs)
    opts_ok = all(len(q.get('optionsEn', [])) == 4 and len(q.get('optionsHi', [])) == 4 for q in qs)
    marks_ok = all(q.get('positiveMarks') == 2.0 and q.get('negativeMarks') == 0.0 for q in qs)

    q_nums = [q.get('questionNumber') for q in qs]
    expected_nums = list(range(1, q_count + 1))
    seq_ok = (q_nums == expected_nums)

    if not (keys_ok and opts_ok and marks_ok and seq_ok):
        errors.append((fname, keys_ok, opts_ok, marks_ok, seq_ok))

    min_q = min(q_nums) if q_nums else 0
    max_q = max(q_nums) if q_nums else 0
    print(f"{fname:<52} | {q_count:<5} | {'OK' if keys_ok else 'FAIL':<5} | {'OK' if opts_ok else 'FAIL':<5} | {'OK' if marks_ok else 'FAIL':<5} | Q{min_q}-Q{max_q}")

print("-" * 92)
print(f"TOTAL EXTRACTED QUESTIONS ACROSS ALL 30 CHAPTERS: {total_qs}")

if errors:
    print(f"\n[ERROR] Issues detected in {len(errors)} files:")
    for err in errors:
        print(" ", err)
else:
    print("\n[SUCCESS] ALL 30 CHAPTERS PASSED INTEGRITY VALIDATION!")

# Audit Manifests
print("\n" + "=" * 92)
print("AUDITING MANIFESTS...")
print("=" * 92)

# 1. manifest_tgt_pgt_history_master.json
with open('manifest_tgt_pgt_history_master.json', 'r', encoding='utf-8') as f:
    master_manifest = json.load(f)

tests = master_manifest.get('tests', [])
print(f"manifest_tgt_pgt_history_master.json contains {len(tests)} tests.")
manifest_ch_files = {}
manifest_total_qs = 0
for t in tests:
    fpath = t.get('filePath') or t.get('path') or ''
    fname = os.path.basename(fpath)
    tc = t.get('totalQuestions', 0)
    manifest_total_qs += tc
    if fname.startswith('tgt_pgt_hist_ch'):
        manifest_ch_files[fname] = tc
        expected_c = chapter_counts.get(fname)
        if expected_c != tc:
            print(f"[MISMATCH] {fname}: master manifest says {tc}, file has {expected_c}")

missing_in_master = set(chapter_counts.keys()) - set(manifest_ch_files.keys())
if missing_in_master:
    print(f"[ERROR] Chapters missing in master manifest: {missing_in_master}")
else:
    print(f"[SUCCESS] All 30 chapters registered in master manifest! (Total manifest Qs: {manifest_total_qs})")

# 2. manifest.json
with open('manifest.json', 'r', encoding='utf-8') as f:
    main_manifest = json.load(f)

main_tests = main_manifest.get('tests', [])
main_ch_files = {}
for t in main_tests:
    fpath = t.get('filePath') or t.get('path') or ''
    fname = os.path.basename(fpath)
    if fname.startswith('tgt_pgt_hist_ch'):
        main_ch_files[fname] = t.get('totalQuestions', 0)

print(f"\nmanifest.json contains {len(main_tests)} total tests, {len(main_ch_files)} are TGT/PGT History chapters.")

missing_in_main = set(chapter_counts.keys()) - set(main_ch_files.keys())
if missing_in_main:
    print(f"[ERROR] Chapters missing in main manifest: {missing_in_main}")
else:
    # check question counts match
    mismatches = []
    for fname, cnt in chapter_counts.items():
        if main_ch_files.get(fname) != cnt:
            mismatches.append((fname, cnt, main_ch_files.get(fname)))
    if mismatches:
        print(f"[ERROR] Question count mismatches in main manifest: {mismatches}")
    else:
        print(f"[SUCCESS] All 30 chapters registered in main manifest.json with 100% matching question counts!")
