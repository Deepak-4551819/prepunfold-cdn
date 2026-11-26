import json
import os
import re
import time
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

CACHE_HI_EN_FILE = os.path.join(os.path.dirname(__file__), "..", "scripts", "cache_hi_to_en.json")
HIST_CACHE_FILE = os.path.join(os.path.dirname(__file__), "..", "scripts", "history_translation_cache.json")

translation_cache = {}

if os.path.exists(CACHE_HI_EN_FILE):
    try:
        with open(CACHE_HI_EN_FILE, 'r', encoding='utf-8') as f:
            for k, v in json.load(f).items():
                if k and v:
                    translation_cache[k.strip()] = v.strip()
    except Exception as e:
        print("Warning loading CACHE_HI_EN_FILE:", e)

if os.path.exists(HIST_CACHE_FILE):
    try:
        with open(HIST_CACHE_FILE, 'r', encoding='utf-8') as f:
            for k, v in json.load(f).items():
                if k and v:
                    translation_cache[v.strip()] = k.strip()
    except Exception as e:
        print("Warning loading HIST_CACHE_FILE:", e)

print(f"Total translation cache entries loaded: {len(translation_cache)}")

def save_cache():
    try:
        with open(CACHE_HI_EN_FILE, 'w', encoding='utf-8') as f:
            json.dump(translation_cache, f, ensure_ascii=False)
    except Exception as e:
        print("Warning saving cache:", e)

def clean_hindi_text(text):
    if not text:
        return ""

    s = str(text)

    # Word-level replacements for legacy words
    word_subs = [
        ("Sce. åJeeruej", "एम. व्हीलर"),
        ("åJeeruej", "व्हीलर"),
        ("बैनजाa", "बनर्जी"),
        ("कानिËघम", "कनिंघम"),
        ("कनिËघम", "कनिंघम"),
        ("बQटिक", "बेंटिक"),
        ("नियुक्यत", "नियुक्त"),
        ("समüट", "सम्राट"),
        ("मõस", "मद्रास"),
        ("परवरी", "फरवरी"),
        ("किसन", "किसान"),
        ("इतिहस", "इतिहास"),
        ("सह्यता", "सहायता"),
        ("हेने", "होने"),
        ("हेकर", "होकर"),
        ("आथिक", "आर्थिक"),
        ("शŒाrकरण", "शस्त्रीकरण"),
        ("क्QबिÇज", "कैम्ब्रिज"),
        ("अक्यट्ूबर", "अक्टूबर"),
        ("फिक्यकी", "फिक्की"),
        ("टट आयरन", "टाटा आयरन"),
        ("क्ंपनी", "कम्पनी"),
        ("ueenewj", "लाहौर"),
        ("oeceesoj", "दामोदर"),
        ("MewJeOece", "शैवधर्म"),
        ("MesjMeen", "शेरशाह"),
        ("cegncceo", "मोहम्मद"),
        ("cenelcee", "महात्मा"),
        ("ieebOeer", "गाँधी"),
        ("ieeBOeer", "गाँधी"),
        ("uegF", "लुई"),
        ("iJeso", "ऋग्वेद"),
        ("uee@[&", "लॉर्ड"),
        ("la@rd", "लॉर्ड"),
        ("kewâefvebie", "कैनिंग"),
        ("kewâनिbie", "कैनिंग"),
        ("cesÙees", "मेयो"),
        ("[thues", "डूप्ले"),
        ("काGvš o uewueer", "काउंट डी लैली"),
        ("[uenewpeer", "डलहौजी"),
        ("Asharam Paddhati", "आश्रम पद्धति"),
        ("GDC ASST. PROF.", "UPPSC GDC"),
        ("RPSC Asst. Prof.", "RPSC"),
        ("UP Higher Asst. Prof.", "UP Higher"),
        ("meved", "सन"),
        ("F&.", "ई."),
        ("F&", "ई."),
        ("ceW", "में"),
        ("kesâ", "के"),
        ("keâes", "को"),
        ("keâe", "का"),
        ("keâer", "की"),
        ("nw", "है"),
        ("nQ", "हैं"),
        ("Lee", "था"),
        ("Leer", "थी"),
        ("Les", "थे"),
        ("Ske", "एक"),
        ("mes", "से"),
        ("hej", "पर"),
        ("yeer.Sce. keâewue", "बी.एम. कौल"),
        ("efieušer cewve Dee@Heâ 1962", "गिल्टी मैन ऑफ 1962"),
        ("oer Deyee@peeavesme ØeesšskeäMeve Skeäš", "द एबोरिजिनल्स प्रोटेक्शन एक्ट"),
        ("heesuewC[ kesâ meeLe Devee›eâceCe mecePeewlee", "पोलैंड के साथ अनाक्रमण समझौता"),
        ("Devpegme", "अंजुस"),
        ("petve", "जून"),
        ("pegueeF&", "जुलाई"),
        ("Deiemle", "अगस्त"),
        ("efmelecyej", "सितम्बर"),
        ("Dekeäštyej", "अक्टूबर"),
        ("veJecyej", "नवम्बर"),
        ("efomecyej", "दिसम्बर"),
        ("peveJejer", "जनवरी"),
        ("heâjJejer", "फरवरी"),
        ("ceeÛe&", "मार्च"),
        ("DeØewue", "अप्रैल"),
        ("ceF&", "मई"),
    ]
    for k, v in word_subs:
        s = s.replace(k, v)

    # Specific common legacy glyphs
    s = s.replace("ला@र्ड", "लॉर्ड")
    s = s.replace("ला@र्", "लॉर्ड")
    s = s.replace("लॉर्डज कर्जन", "लॉर्ड कर्जन")
    s = s.replace("का@लबर्ट", "कॉलबर्ट")
    s = s.replace("का@लेज", "कॉलेज")
    s = s.replace("ड@क्टर", "डॉक्टर")
    s = s.replace("मा@लx-मिंटे", "मार्ले-मिंटो")
    s = s.replace("मा@लx-मिन्टे", "मार्ले-मिंटो")
    s = s.replace("मा@लx", "मार्ले")
    s = s.replace("मिंटे", "मिंटो")
    s = s.replace("रा@लेट", "रौलेट")
    s = s.replace("आ@ल", "ऑल")
    s = s.replace("आ@]फ", "ऑफ")
    s = s.replace("आ@फ", "ऑफ")
    s = s.replace("पा@वटa", "पावर्टी")
    s = s.replace("अनबिÇfट्श", "अनब्रिटिश")
    s = s.replace("कां«ोस", "काँग्रेस")
    s = s.replace("कां«ेस", "काँग्रेस")
    s = s.replace("बिÇfट्श", "ब्रिटिश")
    s = s.replace("इfण्डया", "इण्डिया")
    s = s.replace("इqण्डया", "इण्डिया")
    s = s.replace("इfण्डयन", "इण्डियन")
    s = s.replace("इंfडयन", "इण्डियन")
    s = s.replace("काउंसिल", "काउंसिल")
    s = s.replace("fह्न्द्ू", "हिन्दू")
    s = s.replace("fह्ंद्ू", "हिन्दू")
    s = s.replace("fह्न्द्ुआें", "हिन्दुओं")
    s = s.replace("fह्स्ट्^ी", "हिस्ट्री")
    s = s.replace("fह्ट्लर", "हिटलर")
    s = s.replace("fह्", "हि")
    s = s.replace("वि®æ", "विरुद्ध")
    s = s.replace("øेंच", "फ्रेंच")
    s = s.replace("øंसिस", "फ्रांसिस")
    s = s.replace("øQक", "फ्रैंक")
    s = s.replace("øQ", "फ्रैं")
    s = s.replace("ø", "फ्र")
    s = s.replace("™प", "रूप")
    s = s.replace("™ल", "रूल")
    s = s.replace("™", "रू")
    s = s.replace("®]जवेल्ट", "रूजवेल्ट")
    s = s.replace("®æ", "द्ध")
    s = s.replace("®", "रु")
    s = s.replace("चन्õ", "चन्द्र")
    s = s.replace("रा°^ीय", "राष्ट्रीय")
    s = s.replace("रा°^", "राष्ट्र")
    s = s.replace("रा„^ीय", "राष्ट्रीय")
    s = s.replace("रा„^", "राष्ट्र")
    s = s.replace("केन्õीय", "केन्द्रीय")
    s = s.replace("मान्केकर", "मानकेकर")
    s = s.replace("अनटेल्ड", "अनटोल्ड")
    s = s.replace("स्टेरी", "स्टोरी")
    s = s.replace("अंगुली छ", "अंगुली छाप")
    s = s.replace("साfम्मलित", "सम्मिलित")
    s = s.replace("विघाfट्त", "विघटित")
    s = s.replace("माfह्लाआें", "महिलाओं")
    s = s.replace("पुनविवाह", "पुनर्विवाह")
    s = s.replace("समीfह्त", "समाहित")
    s = s.replace("मुत्ति वीfह्नी", "मुक्ति वाहिनी")
    s = s.replace("मुत्ति", "मुक्ति")
    s = s.replace("वीfह्नी", "वाहिनी")
    s = s.replace("अल्पन्सो डr अल्बुकक", "अल्फोंसो डी अल्बुकर्क")
    s = s.replace("øंसिस्काे डr अल्मेड", "फ्रांसिस्को डी अल्मेडा")
    s = s.replace("निनो द क्ुन्ह", "नीनो दा कुन्हा")
    s = s.replace("वास्काेfडगामा", "वास्कोडिगामा")
    s = s.replace("नेह्™", "नेहरू")
    s = s.replace("डइरेक्यट्र", "डायरेक्टर")
    s = s.replace("सिद्धन्त", "सिद्धान्त")
    s = s.replace("स्थपना", "स्थापना")
    s = s.replace("सद्स्याें", "सदस्यों")
    s = s.replace("प्रदन", "प्रदान")
    s = s.replace("प्रस्तव", "प्रस्ताव")
    s = s.replace("जमाRदरी", "जमींदारी")
    s = s.replace("जमाRदर", "जमींदार")
    s = s.replace("अंगीकृत", "अंगीकृत")
    s = s.replace("द्ेश", "देश")
    s = s.replace("हैद्राबाद", "हैदराबाद")
    s = s.replace("fह्", "हि")
    s = s.replace("आfर्डनेंस", "ऑर्डिनेंस")
    s = s.replace("आ@fस्ट्^या", "ऑस्ट्रिया")
    s = s.replace("आ@स्ट्^ेलियाई", "ऑस्ट्रेलियाई")
    s = s.replace("fट्क", "टिक")
    s = s.replace("fट्व", "टिव")
    s = s.replace("fठ्", "ठि")

    # Font glyphs
    s = s.replace("Ë", "ं")
    s = s.replace("ü", "्रा")
    s = s.replace("õ", "द्र")
    s = s.replace("Ç", "्र")
    s = s.replace("Œ", "स्त्र")
    s = s.replace("Q", "ै")
    s = s.replace("Š", " :")
    s = s.replace("्d", "्")
    s = s.replace("क्यत", "क्त")
    s = s.replace("ीि", "ी")
    s = s.replace("िी", "ी")
    s = s.replace("ाे", "ो")
    s = s.replace("ाै", "ौ")

    # Regex patterns
    s = re.sub(r'([क-ह])ा@', r'\1ॉ', s)
    s = re.sub(r'([क-ह])@', r'\1ॉ', s)
    s = re.sub(r'आ@', r'ऑ', s)

    # Devanagari letter followed by 'r'
    s = re.sub(r'([क-ह])r\b', r'\1ी', s)
    s = re.sub(r'([क-ह])r', r'\1ी', s)

    # 'f' followed by Devanagari letter
    s = re.sub(r'f([क-ह])', r'\1ि', s)

    # 'ह्' forms
    s = s.replace("ह्ुआ", "हुआ").replace("ह्ुई", "हुई").replace("ह्ुए", "हुए").replace("ह्ू", "हू").replace("ह्ु", "हु")

    # Embedded devanagari zero
    s = re.sub(r'(\d+)०(\d*)', r'\g<1>0\g<2>', s)
    s = re.sub(r'०(\d+)', r'0\g<1>', s)

    # Stray markers
    s = re.sub(r'[`~^§©\u2217\u00d7]', '', s)

    return s.strip()

def fix_empty_options(options, pyq_tag, q_text):
    opts = [clean_hindi_text(o) if o else "" for o in options]
    pyq = clean_hindi_text(pyq_tag) if pyq_tag else ""

    # 1. Clumped in any single option
    for idx in range(4):
        clump = opts[idx]
        if clump and '(a)' in clump and '(b)' in clump and '(c)' in clump and '(d)' in clump:
            m = re.search(r'\(a\)\s*(.*?)\s*\(b\)\s*(.*?)\s*\(c\)\s*(.*?)\s*\(d\)\s*(.*)$', clump, re.DOTALL)
            if m:
                opts[0] = clean_hindi_text(m.group(1).strip())
                opts[1] = clean_hindi_text(m.group(2).strip())
                opts[2] = clean_hindi_text(m.group(3).strip())
                opts[3] = clean_hindi_text(m.group(4).strip())
                break

    # 2. Clumped in question text
    if any(not opt for opt in opts):
        if '(a)' in q_text and '(b)' in q_text and '(c)' in q_text and '(d)' in q_text:
            m = re.search(r'\(a\)\s*(.*?)\s*\(b\)\s*(.*?)\s*\(c\)\s*(.*?)\s*\(d\)\s*([^:\n\r]+)', q_text, re.DOTALL)
            if m:
                opts[0] = clean_hindi_text(m.group(1).strip())
                opts[1] = clean_hindi_text(m.group(2).strip())
                opts[2] = clean_hindi_text(m.group(3).strip())
                opts[3] = clean_hindi_text(m.group(4).strip())

    # 3. Opt 3 empty and absorbed into pyqTag
    if not opts[3] and pyq:
        if '|' in pyq:
            parts = pyq.split('|')
            cand_opt = clean_hindi_text(parts[0].strip())
            rest_pyq = '|'.join(parts[1:]).strip()
            opts[3] = cand_opt
            pyq = rest_pyq
        else:
            if not any(exam in pyq for exam in ['UP', 'PGT', 'TGT', 'UGC', 'NET', 'JRF', 'RPSC', 'KVS', 'NVS', 'GIC', 'GDC', 'Lect', 'Asst', 'Paper']):
                opts[3] = pyq.strip()
                pyq = "UP TGT/PGT History"

    # Fallback default if still empty
    default_opts = ["(a)", "(b)", "(c)", "(d)"]
    for i in range(4):
        if not opts[i]:
            opts[i] = default_opts[i]

    return opts, pyq

def translate_batch_post(batch, cache_dict):
    if not batch:
        return {}

    res = {}
    missing = []
    for item in batch:
        cleaned = " ".join(item.split()).strip()
        if not cleaned:
            res[item] = ""
        elif cleaned in cache_dict:
            res[item] = cache_dict[cleaned]
        else:
            missing.append(cleaned)

    if not missing:
        return res

    CHUNK_SIZE = 25
    post_url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en"

    for i in range(0, len(missing), CHUNK_SIZE):
        sub = missing[i:i + CHUNK_SIZE]
        joined = "\n".join(sub)

        success = False
        for attempt in range(3):
            try:
                r = requests.post(post_url, data={'q': joined}, headers={'User-Agent': 'Mozilla/5.0'}, timeout=8)
                if r.status_code == 200:
                    d = r.json()
                    if isinstance(d, list) and d and isinstance(d[0], str):
                        lines = d[0].split("\n")
                        if len(lines) == len(sub):
                            for src, tr in zip(sub, lines):
                                tr_c = tr.strip()
                                cache_dict[src] = tr_c
                                res[src] = tr_c
                            success = True
                            break
            except Exception:
                time.sleep(0.3)

        if not success:
            for item in sub:
                for att in range(2):
                    try:
                        r = requests.post(post_url, data={'q': item}, headers={'User-Agent': 'Mozilla/5.0'}, timeout=6)
                        if r.status_code == 200:
                            d = r.json()
                            if isinstance(d, list) and d and isinstance(d[0], str):
                                tr_c = d[0].strip()
                                cache_dict[item] = tr_c
                                res[item] = tr_c
                                break
                    except Exception:
                        time.sleep(0.2)
                if item not in res:
                    res[item] = item

    return res

def process_single_chapter(file_path, is_ch25=False):
    print(f"\n==========================================")
    print(f"Processing: {os.path.basename(file_path)}")
    print(f"==========================================")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    qs = data.get('questions', [])
    orig_count = len(qs)

    # If Chapter 25, trim Q1 and Q2
    if is_ch25 and orig_count == 58:
        print("Trimming Questions 1 and 2 (Post-Independence spillover) from Chapter 25...")
        qs = qs[2:]
        print(f"Remaining questions for Chapter 25: {len(qs)}")

    total_q = len(qs)
    dur = max(60, total_q)
    data['totalQuestions'] = total_q
    data['total_questions'] = total_q
    data['maxMarks'] = float(total_q * 2.0)
    data['max_marks'] = float(total_q * 2.0)
    data['durationMinutes'] = dur
    data['duration_minutes'] = dur

    # Step 1: Clean Hindi fields and fix options
    for i, q in enumerate(qs, 1):
        q['questionNumber'] = i
        q['q_number'] = i
        q['positiveMarks'] = 2.0
        q['positive_marks'] = 2.0
        q['negativeMarks'] = 0.0
        q['negative_marks'] = 0.0
        q['q_marks'] = 2.0
        q['q_negative_marks'] = 0.0

        # Clean Hindi text
        q_hi = clean_hindi_text(q.get('questionTextHi', ''))
        q['questionTextHi'] = q_hi
        q['question_hi'] = q_hi

        exp_hi = clean_hindi_text(q.get('explanationHi', ''))
        q['explanationHi'] = exp_hi
        q['explanation_hi'] = exp_hi

        opts_hi = q.get('optionsHi', [])
        pyq = q.get('pyqTag', '')
        fixed_opts, fixed_pyq = fix_empty_options(opts_hi, pyq, q_hi)
        q['optionsHi'] = fixed_opts
        q['options_hi'] = fixed_opts
        q['pyqTag'] = fixed_pyq

    # Step 2: Gather all strings needing translation
    texts_to_translate = set()
    for q in qs:
        # Question text: if En is same as Hi or contains Hindi, translate
        q_en = q.get('questionTextEn', '').strip()
        q_hi = q.get('questionTextHi', '').strip()
        if not q_en or q_en == q_hi or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in q_en):
            if q_hi:
                texts_to_translate.add(" ".join(q_hi.split()))

        # Options: if En is same as Hi or contains Hindi, translate
        opts_en = q.get('optionsEn', [])
        opts_hi = q.get('optionsHi', [])
        for i in range(4):
            opt_hi = opts_hi[i] if i < len(opts_hi) else ""
            opt_en = opts_en[i] if i < len(opts_en) else ""
            if not opt_en or opt_en == opt_hi or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in opt_en):
                if opt_hi:
                    texts_to_translate.add(" ".join(opt_hi.split()))

        # Explanation: if En is same as Hi or contains Hindi, translate
        exp_en = q.get('explanationEn', '').strip()
        exp_hi = q.get('explanationHi', '').strip()
        if not exp_en or exp_en == exp_hi or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in exp_en):
            if exp_hi:
                core_exp = '. '.join([s.strip() for s in exp_hi.split('।')[:2] if s.strip()])
                if core_exp:
                    texts_to_translate.add(" ".join(core_exp.split()))

    missing = [t for t in texts_to_translate if t not in translation_cache]
    print(f"Total texts needing translation: {len(texts_to_translate)} (Missing from cache: {len(missing)})")

    if missing:
        t0 = time.time()
        translate_batch_post(missing, translation_cache)
        save_cache()
        print(f"Translated {len(missing)} items in {time.time() - t0:.2f}s, cache updated.")

    # Step 3: Populate English fields
    for q in qs:
        q_hi = " ".join(q.get('questionTextHi', '').split())
        q_en = q.get('questionTextEn', '').strip()
        if not q_en or q_en == q.get('questionTextHi', '') or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in q_en):
            q_en = translation_cache.get(q_hi, q.get('questionTextHi', ''))
        q['questionTextEn'] = q_en
        q['question_en'] = q_en

        opts_hi = q.get('optionsHi', [])
        opts_en = list(q.get('optionsEn', []))
        if len(opts_en) < 4:
            opts_en = ["", "", "", ""]
        for i in range(4):
            raw_opt_hi = opts_hi[i] if i < len(opts_hi) else ""
            opt_hi = " ".join(raw_opt_hi.split())
            opt_en = opts_en[i] if i < len(opts_en) else ""
            if not opt_en or opt_en == raw_opt_hi or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in opt_en):
                opt_en = translation_cache.get(opt_hi, raw_opt_hi)
            opts_en[i] = opt_en
        q['optionsEn'] = opts_en
        q['options_en'] = opts_en

        raw_exp_hi = q.get('explanationHi', '')
        exp_en = q.get('explanationEn', '').strip()
        if not exp_en or exp_en == raw_exp_hi or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in exp_en):
            core_exp = " ".join('. '.join([s.strip() for s in raw_exp_hi.split('।')[:2] if s.strip()]).split())
            exp_en = translation_cache.get(core_exp, raw_exp_hi[:120])
        q['explanationEn'] = exp_en
        q['explanation_en'] = exp_en

    data['questions'] = qs

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved {file_path}: {len(qs)} Qs, durationMinutes={dur}")
    return len(qs)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        chs = [int(x) for x in sys.argv[1:]]
        for ch in chs:
            fname = f"tgt_pgt_hist_ch{ch:02d}"
            matches = [f for f in os.listdir('tests/tgt_pgt_history') if f.startswith(fname) and f.endswith('.json')]
            if matches:
                p = os.path.join('tests/tgt_pgt_history', matches[0])
                process_single_chapter(p, is_ch25=(ch == 25))
    else:
        # Default test on Ch 25
        process_single_chapter('tests/tgt_pgt_history/tgt_pgt_hist_ch25_governors_viceroys.json', is_ch25=True)
