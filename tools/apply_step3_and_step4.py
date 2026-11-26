import os
import json

CDN_BASE = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/tgt_pgt_history/"
ALT_CDN_BASE = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/tgt_pgt_history/"
TESTS_DIR = "tests/tgt_pgt_history"
MASTER_MANIFEST = "manifest_tgt_pgt_history_master.json"
MAIN_MANIFEST = "manifest.json"

def calc_duration(total_q):
    return min(420, max(60, total_q))

def update_chapter_files():
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        q_count = len(data.get('questions', []))
        dur = calc_duration(q_count)

        data['durationMinutes'] = dur
        data['duration_minutes'] = dur
        data['totalQuestions'] = q_count
        data['total_questions'] = q_count

        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def update_manifest_list(manifest_path):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest_data = json.load(f)

    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
    ch_info = {}
    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        q_count = len(d.get('questions', []))
        dur = calc_duration(q_count)
        ch_info[fname] = {
            'totalQuestions': q_count,
            'durationMinutes': dur,
            'testId': d.get('testId') or fname.replace('.json', ''),
            'title': d.get('title') or d.get('testTitle') or fname.replace('.json', '')
        }

    tests = manifest_data.get('tests', [])
    updated_tests = []
    purged_count = 0

    for t in tests:
        cat = t.get('categoryId') or t.get('category_id')
        url = t.get('cdnUrl') or t.get('json_url') or t.get('filePath') or t.get('path') or ''

        if cat == 'tgt_pgt_history':
            # Purge any old references to teaching/tgt_pgt_history
            if 'teaching/tgt_pgt_history' in url:
                purged_count += 1
                continue

            fn = os.path.basename(url)
            if not fn.endswith('.json'):
                fn = (t.get('testId') or t.get('test_id')) + '.json'

            if fn in ch_info:
                info = ch_info[fn]
                t['totalQuestions'] = info['totalQuestions']
                t['total_questions'] = info['totalQuestions']
                t['durationMinutes'] = info['durationMinutes']
                t['duration_minutes'] = info['durationMinutes']
                t['cdnUrl'] = CDN_BASE + fn
                t['json_url'] = CDN_BASE + fn
                t['altCdnUrl'] = ALT_CDN_BASE + fn
                t['filePath'] = f"tests/tgt_pgt_history/{fn}"
                t['file_path'] = f"tests/tgt_pgt_history/{fn}"
                t['path'] = f"tests/tgt_pgt_history/{fn}"
            elif 'mock01' in fn or 'mock01' in t.get('testId', ''):
                mock_q = 63
                t['totalQuestions'] = mock_q
                t['total_questions'] = mock_q
                t['durationMinutes'] = calc_duration(mock_q)
                t['duration_minutes'] = calc_duration(mock_q)
                t['cdnUrl'] = CDN_BASE + "tgt_pgt_hist_mock01_full_length.json"
                t['json_url'] = CDN_BASE + "tgt_pgt_hist_mock01_full_length.json"
                t['altCdnUrl'] = ALT_CDN_BASE + "tgt_pgt_hist_mock01_full_length.json"
                t['filePath'] = "tests/tgt_pgt_history/tgt_pgt_hist_mock01_full_length.json"
                t['file_path'] = "tests/tgt_pgt_history/tgt_pgt_hist_mock01_full_length.json"
                t['path'] = "tests/tgt_pgt_history/tgt_pgt_hist_mock01_full_length.json"

        updated_tests.append(t)

    manifest_data['tests'] = updated_tests
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)
    print(f"Updated {manifest_path}: total tests = {len(updated_tests)}, purged = {purged_count}")

if __name__ == '__main__':
    update_chapter_files()
    update_manifest_list(MASTER_MANIFEST)
    update_manifest_list(MAIN_MANIFEST)
