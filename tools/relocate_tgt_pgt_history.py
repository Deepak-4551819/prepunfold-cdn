import os
import shutil
import json
import time

SRC_DIR = "tests/tgt_pgt_history"
DEST_DIR = "tests/teaching/tgt_pgt_history"
MANIFEST_FILE = "manifest.json"
MASTER_MANIFEST = "manifest_tgt_pgt_history_master.json"

CDN_PREFIX = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/teaching/tgt_pgt_history/"
ALT_CDN_PREFIX = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/teaching/tgt_pgt_history/"

def relocate():
    # 1. Remove old subdirs in tests/teaching/tgt_pgt_history
    if os.path.exists(DEST_DIR):
        print(f"Cleaning existing contents in {DEST_DIR}...")
        for item in os.listdir(DEST_DIR):
            p = os.path.join(DEST_DIR, item)
            if os.path.isdir(p):
                shutil.rmtree(p)
            else:
                os.remove(p)
    else:
        os.makedirs(DEST_DIR, exist_ok=True)

    # 2. Move all files from tests/tgt_pgt_history to tests/teaching/tgt_pgt_history
    if os.path.exists(SRC_DIR):
        files = os.listdir(SRC_DIR)
        print(f"Moving {len(files)} files from {SRC_DIR} to {DEST_DIR}...")
        for f in files:
            src_f = os.path.join(SRC_DIR, f)
            dest_f = os.path.join(DEST_DIR, f)
            shutil.copy2(src_f, dest_f)
            os.remove(src_f)
        os.rmdir(SRC_DIR)
        print(f"Removed source directory {SRC_DIR}.")
    else:
        print(f"Source dir {SRC_DIR} does not exist!")

    # 3. Update manifest.json
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    for t in manifest.get('tests', []):
        cat = t.get('categoryId') or t.get('category_id')
        if cat == 'tgt_pgt_history':
            fn = os.path.basename(t.get('jsonUrl') or t.get('cdnUrl') or t.get('path') or '')
            if not fn.endswith('.json'):
                fn = (t.get('testId') or t.get('test_id')) + '.json'
            rel_path = f"tests/teaching/tgt_pgt_history/{fn}"
            t['path'] = rel_path
            t['filePath'] = rel_path
            t['file_path'] = rel_path
            t['cdnUrl'] = CDN_PREFIX + fn
            t['json_url'] = CDN_PREFIX + fn
            t['altCdnUrl'] = ALT_CDN_PREFIX + fn

    cur_v = manifest.get('version', 39)
    new_v = cur_v + 1
    manifest['version'] = new_v
    manifest['manifest_version'] = new_v
    manifest['manifestVersion'] = new_v
    manifest['lastUpdated'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    manifest['updatedAt'] = manifest['lastUpdated']
    manifest['updated_at'] = manifest['lastUpdated']

    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Updated manifest.json: bumped to v{new_v}.")

    # 4. Update manifest_tgt_pgt_history_master.json
    with open(MASTER_MANIFEST, 'r', encoding='utf-8') as f:
        master = json.load(f)

    for t in master.get('tests', []):
        fn = os.path.basename(t.get('jsonUrl') or t.get('cdnUrl') or t.get('path') or '')
        if not fn.endswith('.json'):
            fn = (t.get('testId') or t.get('test_id')) + '.json'
        rel_path = f"tests/teaching/tgt_pgt_history/{fn}"
        t['path'] = rel_path
        t['filePath'] = rel_path
        t['file_path'] = rel_path
        t['cdnUrl'] = CDN_PREFIX + fn
        t['json_url'] = CDN_PREFIX + fn
        t['altCdnUrl'] = ALT_CDN_PREFIX + fn

    master['version'] = new_v
    master['manifest_version'] = new_v
    master['manifestVersion'] = new_v
    master['lastUpdated'] = manifest['lastUpdated']
    master['updatedAt'] = manifest['lastUpdated']
    master['updated_at'] = manifest['lastUpdated']

    with open(MASTER_MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(master, f, ensure_ascii=False, indent=2)
    print(f"Updated master manifest: bumped to v{new_v}.")

if __name__ == '__main__':
    relocate()
