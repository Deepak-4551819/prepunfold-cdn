import os
import json
import re
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

CACHE_FILE = r'D:\Android Project\prepunfold-cdn\scripts\history_translation_cache.json'
TESTS_DIR = r'D:\Android Project\prepunfold-cdn\tests\history_pyq_1990_2024'

cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            cache = json.load(f)
    except:
        cache = {}

def is_hindi(text):
    if not text:
        return False
    return bool(re.search(r'[\u0900-\u097F]', text))

def fetch_one(text):
    if not text or is_hindi(text):
        return text, text
    if text in cache and is_hindi(cache[text]):
        return text, cache[text]

    # If text is too long for GET query param, chunk it
    if len(text) > 1200:
        parts = re.split(r'(\.\s+)', text)
        translated_parts = []
        curr = ""
        for p in parts:
            if len(curr) + len(p) < 1000:
                curr += p
            else:
                if curr:
                    _, tr = fetch_one(curr)
                    translated_parts.append(tr)
                curr = p
        if curr:
            _, tr = fetch_one(curr)
            translated_parts.append(tr)
        return text, " ".join(translated_parts)

    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=hi&q={urllib.parse.quote(text)}"
    for _ in range(3):
        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=8)
            if r.status_code == 200:
                res = r.json()
                if isinstance(res, list) and len(res) > 0 and isinstance(res[0], str):
                    return text, res[0]
        except:
            pass
    return text, text

def enrich_history():
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.endswith('.json')])
    print(f"Checking {len(files)} History files for any missing Hindi...")

    total_translated = 0

    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        questions = data.get("questions", [])
        to_fetch = set()

        for q in questions:
            if not is_hindi(q.get("questionTextHi", "")):
                to_fetch.add(q.get("questionTextEn", ""))

            opts_en = q.get("optionsEn", [])
            opts_hi = q.get("optionsHi", [])
            for idx in range(len(opts_en)):
                hi_val = opts_hi[idx] if idx < len(opts_hi) else ""
                if not is_hindi(hi_val):
                    to_fetch.add(opts_en[idx])

            exp_hi = q.get("explanationHi", "")
            if not is_hindi(exp_hi):
                clean_exp = re.sub(r'^Correct Answer:\s*\([A-D]\)\.\s*', '', q.get("explanationEn", "")).strip()
                to_fetch.add(clean_exp)

        untranslated = [t for t in to_fetch if t and (t not in cache or not is_hindi(cache[t]))]

        if untranslated:
            print(f"Translating {len(untranslated)} strings for {fname}...")
            with ThreadPoolExecutor(max_workers=8) as executor:
                for orig, trans in executor.map(fetch_one, untranslated):
                    if is_hindi(trans):
                        cache[orig] = trans
                        total_translated += 1

            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache, f, ensure_ascii=False)

        # Apply translations to questions
        modified = False
        for q in questions:
            en_q = q.get("questionTextEn", "")
            if not is_hindi(q.get("questionTextHi", "")) and en_q in cache and is_hindi(cache[en_q]):
                q["questionTextHi"] = cache[en_q]
                q["question_hi"] = cache[en_q]
                modified = True

            opts_en = q.get("optionsEn", [])
            opts_hi = list(q.get("optionsHi", []))
            for idx in range(len(opts_en)):
                en_opt = opts_en[idx]
                hi_opt = opts_hi[idx] if idx < len(opts_hi) else ""
                if not is_hindi(hi_opt) and en_opt in cache and is_hindi(cache[en_opt]):
                    opts_hi[idx] = cache[en_opt]
                    modified = True
            q["optionsHi"] = opts_hi
            q["options_hi"] = opts_hi

            exp_en = q.get("explanationEn", "")
            clean_exp = re.sub(r'^Correct Answer:\s*\([A-D]\)\.\s*', '', exp_en).strip()
            corr_opt = q.get("correctOption", "A")
            if not is_hindi(q.get("explanationHi", "")) and clean_exp in cache and is_hindi(cache[clean_exp]):
                new_hi_exp = f"सही उत्तर: ({corr_opt}) {cache[clean_exp]}"
                q["explanationHi"] = new_hi_exp
                q["explanation_hi"] = new_hi_exp
                modified = True

        if modified:
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Updated {fname} with Hindi translations.")

    print(f"Done enriching History! Total newly translated: {total_translated}")

if __name__ == "__main__":
    enrich_history()
