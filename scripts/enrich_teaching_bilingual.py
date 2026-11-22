# -*- coding: utf-8 -*-
import os, sys, json, re, time, requests, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

CACHE_EN_HI_FILE = os.path.join(os.path.dirname(__file__), "cache_en_to_hi.json")
CACHE_HI_EN_FILE = os.path.join(os.path.dirname(__file__), "cache_hi_to_en.json")

cache_en_hi = {}
if os.path.exists(CACHE_EN_HI_FILE):
    try:
        with open(CACHE_EN_HI_FILE, 'r', encoding='utf-8') as f:
            cache_en_hi = json.load(f)
    except:
        cache_en_hi = {}

cache_hi_en = {}
if os.path.exists(CACHE_HI_EN_FILE):
    try:
        with open(CACHE_HI_EN_FILE, 'r', encoding='utf-8') as f:
            cache_hi_en = json.load(f)
    except:
        cache_hi_en = {}

print(f"Loaded caches: EN->HI has {len(cache_en_hi)} entries, HI->EN has {len(cache_hi_en)} entries.")

def save_caches():
    with open(CACHE_EN_HI_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache_en_hi, f, ensure_ascii=False)
    with open(CACHE_HI_EN_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache_hi_en, f, ensure_ascii=False)

def translate_single(text, sl, tl):
    if not text.strip():
        return text
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={sl}&tl={tl}&q={urllib.parse.quote(text)}"
    for _ in range(3):
        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=10)
            if r.status_code == 200:
                res = r.json()
                if isinstance(res, list) and len(res) > 0 and isinstance(res[0], str):
                    return res[0]
        except Exception:
            time.sleep(0.5)
    return text

def translate_batch(batch, sl, tl):
    if not batch:
        return {}
    cleaned = [b.replace("\n", " ").strip() for b in batch]
    joined = "\n".join(cleaned)
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={sl}&tl={tl}&q={urllib.parse.quote(joined)}"
    for _ in range(3):
        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=12)
            if r.status_code == 200:
                res = r.json()
                if isinstance(res, list) and len(res) > 0 and isinstance(res[0], str):
                    lines = res[0].split("\n")
                    if len(lines) == len(batch):
                        return dict(zip(batch, lines))
        except Exception:
            time.sleep(0.5)
    # Fallback to single translations
    res = {}
    for item in batch:
        res[item] = translate_single(item, sl, tl)
    return res

def batch_translate_missing(items_set, cache_dict, sl, tl, label=""):
    missing = [it for it in items_set if it and it.strip() and it not in cache_dict]
    print(f"[{label}] Total unique: {len(items_set)}, missing: {len(missing)}")
    if not missing:
        return

    BATCH_SIZE = 35
    chunks = [missing[i:i + BATCH_SIZE] for i in range(0, len(missing), BATCH_SIZE)]
    print(f"[{label}] Processing {len(chunks)} chunks using 8 workers...")

    done_chunks = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(translate_batch, chunk, sl, tl): chunk for chunk in chunks}
        for future in as_completed(futures):
            res_dict = future.result()
            if res_dict:
                cache_dict.update(res_dict)
            done_chunks += 1
            if done_chunks % 25 == 0 or done_chunks == len(chunks):
                print(f"[{label}] Progress: {done_chunks}/{len(chunks)} chunks completed ({len(cache_dict)} in cache).")
                save_caches()

    save_caches()
    print(f"[{label}] Finished batch translation. Cache size: {len(cache_dict)}")

def enrich_economics():
    print("\n=== Enriching Economics (EN -> HI) ===")
    econ_dir = "tests/teaching/tgt_pgt_economics"
    all_files = []
    unique_texts = set()

    for root, dirs, files in os.walk(econ_dir):
        for f in files:
            if f.endswith(".json"):
                all_files.append(os.path.join(root, f))

    for p in all_files:
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            for q in data.get('questions', []):
                q_en = q.get('questionTextEn', '').strip()
                if q_en:
                    unique_texts.add(q_en)
                for opt in q.get('optionsEn', []):
                    if opt and opt.strip():
                        unique_texts.add(opt.strip())

    batch_translate_missing(unique_texts, cache_en_hi, sl="en", tl="hi", label="Econ EN->HI")

    # Now apply to files
    for p in all_files:
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)

        modified = False
        for q in data.get('questions', []):
            q_en = q.get('questionTextEn', '').strip() or q.get('questionText', '').strip()
            opts_en = q.get('optionsEn', []) or q.get('options', [])
            corr_opt = q.get('correctOption', 'A')

            # Populate Hindi
            if not q.get('questionTextHi') or not q['questionTextHi'].strip():
                q['questionTextHi'] = cache_en_hi.get(q_en, q_en)
                modified = True

            if not q.get('optionsHi') or len(q['optionsHi']) < 4:
                q['optionsHi'] = [cache_en_hi.get(opt.strip(), opt) for opt in opts_en]
                modified = True

            if not q.get('explanationHi') or not q['explanationHi'].strip():
                orig_exp = q.get('explanationEn', '').strip() or q.get('explanation', '').strip()
                q['explanationHi'] = f"सही विकल्प ({corr_opt}) है।\n{orig_exp}"
                modified = True

            # Ensure English is populated
            if not q.get('questionTextEn'):
                q['questionTextEn'] = q_en
                modified = True
            if not q.get('optionsEn') or len(q['optionsEn']) < 4:
                q['optionsEn'] = opts_en
                modified = True
            if not q.get('explanationEn'):
                q['explanationEn'] = q.get('explanation', '') or f"Correct option is ({corr_opt})."
                modified = True

            # Fallbacks
            q['questionText'] = q['questionTextEn']
            q['options'] = q['optionsEn']
            q['explanation'] = q['explanationEn']

        if modified:
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(data, fp, ensure_ascii=False, indent=2)

    print(f"Updated {len(all_files)} Economics files with Hindi translations!")

def enrich_civics_history_geography():
    print("\n=== Enriching Civics, History, Geography (HI -> EN) ===")
    cats = ['tgt_pgt_civics', 'tgt_pgt_history', 'tgt_pgt_geography']
    all_files = []
    unique_texts = set()

    for cat in cats:
        cat_dir = os.path.join("tests/teaching", cat)
        if not os.path.exists(cat_dir):
            continue
        for root, dirs, files in os.walk(cat_dir):
            for f in files:
                if f.endswith(".json"):
                    all_files.append(os.path.join(root, f))

    for p in all_files:
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            for q in data.get('questions', []):
                q_hi = q.get('questionTextHi', '').strip()
                if q_hi:
                    unique_texts.add(q_hi)
                for opt in q.get('optionsHi', []):
                    if opt and opt.strip():
                        unique_texts.add(opt.strip())

    batch_translate_missing(unique_texts, cache_hi_en, sl="hi", tl="en", label="Civ/Hist/Geo HI->EN")

    # Now apply to files
    for p in all_files:
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)

        modified = False
        for q in data.get('questions', []):
            q_hi = q.get('questionTextHi', '').strip()
            opts_hi = q.get('optionsHi', [])
            corr_opt = q.get('correctOption', 'A')

            # Populate English
            translated_q_en = cache_hi_en.get(q_hi, "")
            if translated_q_en:
                q['questionTextEn'] = translated_q_en
                modified = True
            elif not q.get('questionTextEn') or q.get('questionTextEn') == q_hi:
                q['questionTextEn'] = translated_q_en or q_hi

            translated_opts_en = [cache_hi_en.get(opt.strip(), opt) for opt in opts_hi]
            if translated_opts_en:
                q['optionsEn'] = translated_opts_en
                modified = True

            orig_exp_hi = q.get('explanationHi', '').strip() or q.get('explanation', '').strip()
            if not q.get('explanationEn') or q.get('explanationEn') == orig_exp_hi:
                q['explanationEn'] = f"Correct option is ({corr_opt}).\n[Hindi solution: {orig_exp_hi}]"
                modified = True

            # Ensure Hindi fields are present
            if not q.get('questionTextHi'):
                q['questionTextHi'] = q_hi
                modified = True
            if not q.get('optionsHi'):
                q['optionsHi'] = opts_hi
                modified = True
            if not q.get('explanationHi'):
                q['explanationHi'] = orig_exp_hi
                modified = True

            # Fallbacks: for Hindi exam preference, default questionText/options
            q['questionText'] = q['questionTextHi']
            q['options'] = q['optionsHi']
            q['explanation'] = q['explanationHi']

        if modified:
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(data, fp, ensure_ascii=False, indent=2)

    print(f"Updated {len(all_files)} Civics, History, Geography files with English translations!")

if __name__ == '__main__':
    start_time = time.time()
    enrich_economics()
    enrich_civics_history_geography()
    print(f"\nAll done in {time.time() - start_time:.1f} seconds!")
