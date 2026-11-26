import json
import os
import re

TESTS_DIR = "tests/tgt_pgt_history"
MANIFEST_FILE = "manifest.json"
MASTER_MANIFEST = "manifest_tgt_pgt_history_master.json"

LEGACY_ARTIFACT_PATTERNS = [
    r'uee@', r'kewâ', r'cesÙ', r'fह्',
    r'[™०åäø§°\^@æ®]'
]
ARTIFACT_RE = re.compile('|'.join(LEGACY_ARTIFACT_PATTERNS))

def check_artifacts(text):
    if not text:
        return 0
    return len(ARTIFACT_RE.findall(str(text)))

def audit_all_chapters():
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
    results = []
    total_extracted_q = 0

    print("Auditing 30 chapter files in tests/tgt_pgt_history...")
    print("=" * 100)
    print(f"{'File':<52} | {'Qs':<4} | {'Dur':<4} | {'EmptyOpts':<9} | {'SameEnHi':<8} | {'Artifacts':<9} | {'Status'}")
    print("-" * 100)

    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        questions = data.get('questions', [])
        total_q = len(questions)
        total_extracted_q += total_q

        dur = data.get('durationMinutes') or data.get('duration_minutes', 0)
        expected_dur = min(420, max(60, total_q))

        empty_opts_count = 0
        same_en_hi_count = 0
        artifact_count = 0

        for q in questions:
            # Check options
            opts_hi = q.get('optionsHi', [])
            opts_en = q.get('optionsEn', [])
            if len(opts_hi) < 4 or any(not str(o).strip() for o in opts_hi) or len(opts_en) < 4 or any(not str(o).strip() for o in opts_en):
                empty_opts_count += 1

            # Check question and options identical
            q_hi = str(q.get('questionTextHi') or '').strip()
            q_en = str(q.get('questionTextEn') or '').strip()
            if (q_hi and q_en and q_hi == q_en) or ([str(o).strip() for o in opts_hi] == [str(o).strip() for o in opts_en]):
                same_en_hi_count += 1

            # Check artifacts
            texts = [q_hi, str(q.get('explanationHi') or '')] + [str(o) for o in opts_hi]
            for t in texts:
                artifact_count += check_artifacts(t)

        status = "PASS" if (empty_opts_count == 0 and same_en_hi_count == 0 and artifact_count == 0 and dur == expected_dur) else "FAIL"
        print(f"{fname:<52} | {total_q:<4} | {dur:<4} | {empty_opts_count:<9} | {same_en_hi_count:<8} | {artifact_count:<9} | {status}")
        results.append((fname, total_q, empty_opts_count, same_en_hi_count, artifact_count, status))

    print("=" * 100)
    print(f"Total Extracted Questions Across All 30 Chapters: {total_extracted_q}")
    all_pass = all(r[5] == "PASS" for r in results)
    if all_pass:
        print("[SUCCESS] ALL 30 CHAPTER FILES PASSED BILINGUAL QUALITY AND INTEGRITY CHECKS!")
    else:
        print("[WARNING] Some chapter files require post-processing.")

    # Audit Manifest
    print("\n" + "=" * 100)
    print("VERIFYING MANIFEST.JSON & OLD PAPERS...")
    print("=" * 100)
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    hist_tests = [t for t in manifest.get('tests', []) if (t.get('categoryId') or t.get('category_id')) == 'tgt_pgt_history']
    print(f"Total tgt_pgt_history tests in manifest.json: {len(hist_tests)}")

    old_papers = [t for t in hist_tests if 'teaching/tgt_pgt_history' in (t.get('jsonUrl') or t.get('filePath') or t.get('path') or '')]
    print(f"Old low-question paper references remaining: {len(old_papers)}")
    if len(old_papers) == 0:
        print("[PASS] 100% of old TGT/PGT History papers have been removed from manifest.json.")
    else:
        print("[FAIL] Some old papers still exist in manifest.json.")

    duration_mismatches = []
    for t in hist_tests:
        tid = t.get('testId') or t.get('test_id')
        dur = t.get('durationMinutes') or t.get('duration_minutes')
        tq = t.get('totalQuestions') or t.get('total_questions')
        expected = min(420, max(60, tq))
        if dur != expected:
            duration_mismatches.append((tid, dur, expected))

    if not duration_mismatches:
        print("[PASS] durationMinutes == min(420, max(60, totalQuestions)) for 100% of tests in manifest.json.")
    else:
        print(f"[FAIL] Duration mismatches in manifest.json: {duration_mismatches}")

    with open(MASTER_MANIFEST, 'r', encoding='utf-8') as f:
        master = json.load(f)
    print(f"\nTotal tests in manifest_tgt_pgt_history_master.json: {len(master.get('tests', []))}")
    master_mismatches = []
    for t in master.get('tests', []):
        tid = t.get('testId') or t.get('test_id')
        dur = t.get('durationMinutes') or t.get('duration_minutes')
        tq = t.get('totalQuestions') or t.get('total_questions')
        expected = min(420, max(60, tq))
        if dur != expected:
            master_mismatches.append((tid, dur, expected))
    if not master_mismatches:
        print("[PASS] durationMinutes == min(420, max(60, totalQuestions)) for 100% of tests in master manifest.")
    else:
        print(f"[FAIL] Duration mismatches in master manifest: {master_mismatches}")

if __name__ == '__main__':
    audit_all_chapters()
