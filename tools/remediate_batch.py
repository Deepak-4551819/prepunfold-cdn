# -*- coding: utf-8 -*-
import json
import os
import re
import sys
import time
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(__file__))
from artifact_hindi_map import clean_hindi_text
from artifact_english_map import clean_english_text

TESTS_DIR = "tests/tgt_pgt_history"
CACHE_FILE = os.path.join(os.path.dirname(__file__), "..", "scripts", "cache_hi_to_en.json")
HINDI_RE = re.compile(r'[\u0900-\u097F]')

translation_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            translation_cache = json.load(f)
    except Exception as e:
        print("Warning loading cache:", e)

def save_cache():
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(translation_cache, f, ensure_ascii=False)
    except Exception as e:
        print("Warning saving cache:", e)

def translate_text(text):
    if not text or not str(text).strip():
        return ""
    s = str(text).strip()
    if s in translation_cache:
        return translation_cache[s]
    # Check if text actually has Hindi
    if not HINDI_RE.search(s):
        return s

    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en&q={urllib.parse.quote(s)}"
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if r.status_code == 200:
            res = r.json()
            if isinstance(res, list) and res and isinstance(res[0], str):
                tr = res[0].strip()
                translation_cache[s] = tr
                return tr
    except Exception:
        pass
    return s

def remediate_chapter(chapter_num):
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith(f"tgt_pgt_hist_ch{chapter_num:02d}_") and f.endswith('.json')])
    if not files:
        print(f"No file found for chapter {chapter_num}")
        return

    fname = files[0]
    fpath = os.path.join(TESTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data.get('questions', [])
    modified_q_count = 0

    texts_to_translate = []

    for q in questions:
        # 1. Clean Hindi fields
        q_hi = clean_hindi_text(q.get('questionTextHi') or q.get('question_hi') or '')
        opts_hi = [clean_hindi_text(o) for o in (q.get('optionsHi') or q.get('options_hi') or [])]
        exp_hi = clean_hindi_text(q.get('explanationHi') or q.get('explanation_hi') or '')

        q['questionTextHi'] = q_hi
        q['question_hi'] = q_hi
        q['optionsHi'] = opts_hi
        q['options_hi'] = opts_hi
        q['explanationHi'] = exp_hi
        q['explanation_hi'] = exp_hi

        # 2. Clean English fields
        q_en = clean_english_text(q.get('questionTextEn') or q.get('question_en') or '')
        opts_en = [clean_english_text(o) for o in (q.get('optionsEn') or q.get('options_en') or [])]
        exp_en = clean_english_text(q.get('explanationEn') or q.get('explanation_en') or '')

        # Check if q_en needs translation (if identical to q_hi or contains Devanagari)
        if (not q_en) or (q_en.strip() == q_hi.strip()) or HINDI_RE.search(q_en):
            if q_hi.strip() in translation_cache:
                q_en = translation_cache[q_hi.strip()]
            else:
                texts_to_translate.append(q_hi.strip())

        # Check if exp_en needs translation (if contains Devanagari or starts with Hindi)
        if HINDI_RE.search(exp_en):
            # Translate from clean Hindi explanation
            if exp_hi.strip() in translation_cache:
                exp_en = translation_cache[exp_hi.strip()]
            else:
                texts_to_translate.append(exp_hi.strip())

        # Check options
        for o_idx, opt_en in enumerate(opts_en):
            if HINDI_RE.search(opt_en):
                clean_opt_hi = opts_hi[o_idx].strip()
                if clean_opt_hi in translation_cache:
                    opts_en[o_idx] = translation_cache[clean_opt_hi]
                else:
                    texts_to_translate.append(clean_opt_hi)

    # Batch translate texts not in cache
    unique_to_translate = list(set(t for t in texts_to_translate if t and t not in translation_cache))
    if unique_to_translate:
        print(f"  Translating {len(unique_to_translate)} items for Ch {chapter_num}...")
        with ThreadPoolExecutor(max_workers=8) as ex:
            results = list(ex.map(translate_text, unique_to_translate))
        save_cache()

    # Now apply the translations and handle identical options
    for q in questions:
        q_hi = q['questionTextHi']
        opts_hi = q['optionsHi']
        exp_hi = q['explanationHi']

        q_en = clean_english_text(q.get('questionTextEn') or q.get('question_en') or '')
        opts_en = [clean_english_text(o) for o in (q.get('optionsEn') or q.get('options_en') or [])]
        exp_en = clean_english_text(q.get('explanationEn') or q.get('explanation_en') or '')

        if (not q_en) or (q_en.strip() == q_hi.strip()) or HINDI_RE.search(q_en):
            q_en = translation_cache.get(q_hi.strip(), q_en)
            q_en = clean_english_text(q_en)

        if HINDI_RE.search(exp_en):
            exp_en = translation_cache.get(exp_hi.strip(), exp_en)
            exp_en = clean_english_text(exp_en)

        for o_idx, opt_en in enumerate(opts_en):
            if HINDI_RE.search(opt_en):
                clean_opt_hi = opts_hi[o_idx].strip()
                opts_en[o_idx] = translation_cache.get(clean_opt_hi, opt_en)
                opts_en[o_idx] = clean_english_text(opts_en[o_idx])

        # If opts_en is still identical to opts_hi (e.g. '1900' or '(II), (IV)'), differentiate with (A), (B), (C), (D)
        if [str(o).strip() for o in opts_en] == [str(o).strip() for o in opts_hi]:
            labels = ['(A)', '(B)', '(C)', '(D)']
            opts_en = [f"{labels[i]} {str(o).strip()}" for i, o in enumerate(opts_en)]

        # Ensure camelCase and snake_case sync
        q['questionTextEn'] = q_en
        q['question_en'] = q_en
        q['optionsEn'] = opts_en
        q['options_en'] = opts_en
        q['explanationEn'] = exp_en
        q['explanation_en'] = exp_en

    # Save chapter file
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Finished Ch {chapter_num:02d} ({fname}): {len(questions)} Qs.")

if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        ch_list = [int(x) for x in args]
    else:
        ch_list = [1, 2, 3, 4, 5]
    for ch in ch_list:
        remediate_chapter(ch)
    save_cache()
