import json
import os
import re
import requests
import urllib.parse

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

# Translation cache
CACHE_HI_EN_FILE = os.path.join(os.path.dirname(__file__), "..", "scripts", "cache_hi_to_en.json")
translation_cache = {}
if os.path.exists(CACHE_HI_EN_FILE):
    with open(CACHE_HI_EN_FILE, 'r', encoding='utf-8') as f:
        translation_cache = json.load(f)

def clean_text_all(s):
    if not s:
        return ""

    # 1. Hindi legacy words & glyphs
    replacements = [
        ("cenelcee ieebOeer", "महात्मा गाँधी"),
        ("cenelcee ieeBOeer", "महात्मा गाँधी"),
        ("cenelcee", "महात्मा"),
        ("ieeBOeer", "गाँधी"),
        ("ieebOeer", "गाँधी"),
        ("cegncceo ieesjer", "मोहम्मद गोरी"),
        ("cegncceo", "मोहम्मद"),
        ("MesjMeen", "शेरशाह"),
        ("iJeso", "ऋग्वेद"),
        ("ueenewj", "लाहौर"),
        ("oeceesoj", "दामोदर"),
        ("MewJeOece", "शैवधर्म"),
        ("uegF", "लुई"),
        ("[thues", "डूप्ले"),
        ("uee@[& keäueeFJe", "लॉर्ड क्लाइव"),
        ("uee@[&", "लॉर्ड"),
        ("la@rd", "लॉर्ड"),
        ("uee[& cesÙees", "लॉर्ड मेयो"),
        ("cesÙees", "मेयो"),
        ("kewâनिbie", "कैनिंग"),
        ("kewâefvebie", "कैनिंग"),
        ("kewâकेÙe", "कैकेय"),
        ("JeŒe", "वस्त्र"),
        ("ce™", "मरु"),
        ("celmÙe", "मत्स्य"),
        ("øeWâÛe", "फ्रेंच"),
        ("vadodra cegvõe ueesceder OeÇebieOee", "वडोदरा मुंद्रा लोथल ध्रांगध्रा"),
        ("Fvõ ®õ", "इन्द्र रुद्र"),
        ("Fvõ", "इन्द्र"),
        ("®õ", "रुद्र"),
        ("$e+iJeso", "ऋग्वेद"),
        ("Yajuvxad", "यजुर्वेद"),
        ("Asharam Paddhati", "आश्रम पद्धति"),
        ("Shri Shri", "श्री श्री"),
        ("shudder", "सिंध"),
        ("cee@všieessejer", "मोंटगोमरी"),
        ("Lyallpur", "लायलपुर"),
    ]
    for k, v in replacements:
        s = s.replace(k, v)

    # Specific Devanagari conjuncts & glyphs
    dev_subs = [
        ("सम्बæ", "सम्बद्ध"),
        ("बौæ", "बौद्ध"),
        ("वि®æ", "विरुद्ध"),
        ("शुæ", "शुद्ध"),
        ("प्रसिæ", "प्रसिद्ध"),
        ("युæ", "युद्ध"),
        ("वृæ", "वृद्ध"),
        ("बुæ", "बुद्ध"),
        ("सिæ", "सिद्ध"),
        ("आबæ", "आबद्ध"),
        ("æ", "द्ध"),
        ("f°eLe", "स्थित"),
        ("f°", "स्थि"),
        ("पाfमी", "पश्चिमी"),
        ("fV", "वि"),
        ("परिपक्यव", "परिपक्व"),
        ("हड़प्पाrय", "हड़प्पीय"),
        ("पुरातीति्वक", "पुरातात्विक"),
        ("पाकिस्तन", "पाकिस्तान"),
        ("अगन", "अग्नि"),
        ("उझ", "उषा"),
        ("ceद्र", "मद्र"),
        ("उशीनर", "उशीनर"),
        ("पांचाल", "पांचाल"),
        ("Lord Kang", "Lord Canning"),
        ("john lawrence", "John Lawrence"),
        ("warren hasting", "Warren Hastings"),
        ("Jesus Vansittart", "Henry Vansittart"),
        ("henry dv", "Henry IV"),
        ("uegF& XIV", "Louis XIV"),
        ("uegF& XV", "Louis XV"),
        ("uegF& XIII", "Louis XIII"),
        ("ieebieeOej", "गंगाधर"),
        ("Dhondhoo Pant", "धोंधू पंत"),
        ("jecesibn", "राजेन्द्र"),
        ("Shashank", "शशांक"),
        ("Kharavela", "खारवेल"),
        ("Gautamiputra", "गौतमीपुत्र"),
        ("Pulakeshin", "पुलकेशी"),
    ]
    for k, v in dev_subs:
        s = s.replace(k, v)

    # Numbers: Devanagari zero '०' -> '0'
    s = re.sub(r'०', '0', s)

    # Miscellaneous artifact characters
    s = s.replace("ø", "फ्र")
    s = s.replace("®", "रु")
    s = s.replace("Ç", "्र")
    s = s.replace("Œ", "स्त्र")
    s = s.replace("Ë", "ं")
    s = s.replace("Q", "ै")
    s = s.replace("™", "रू")
    s = s.replace("`", "")
    s = s.replace("~", "")
    s = s.replace("^", "")
    s = s.replace("§", "")
    s = s.replace("©", "")

    return s.strip()

def clean_en_options(opts_en):
    res = []
    en_subs = [
        ("cenelcee ieebOeer", "Mahatma Gandhi"),
        ("cenelcee ieeBOeer", "Mahatma Gandhi"),
        ("cenelcee", "Mahatma"),
        ("ieeBOeer", "Gandhi"),
        ("ieebOeer", "Gandhi"),
        ("cegncceo ieesjer", "Muhammad Ghori"),
        ("cegncceo", "Muhammad"),
        ("MesjMeen", "Sher Shah"),
        ("iJeso", "Rigveda"),
        ("$e+iJeso", "Rigveda"),
        ("Yajuvxad", "Yajurveda"),
        ("ueenewj", "Lahore"),
        ("oeceesoj", "Damodar"),
        ("MewJeOece", "Shaivism"),
        ("uegF", "Louis"),
        ("[thues", "Dupleix"),
        ("uee@[& keäueeFJe", "Lord Clive"),
        ("uee@[&", "Lord"),
        ("la@rd", "Lord"),
        ("uee[& cesÙees", "Lord Mayo"),
        ("cesÙees", "Mayo"),
        ("kewâनिbie", "Canning"),
        ("kewâefvebie", "Canning"),
        ("kewâकेÙe", "Kaikeya"),
        ("JeŒe", "Clothes"),
        ("ce™", "Maru (Desert)"),
        ("celmÙe", "Matsya"),
        ("øeWâÛe", "French"),
        ("vadodra cegvõe ueesceder OeÇebieOee", "Vadodara, Mundra, Lothal, Dhrangadhra"),
        ("Fvõ ®õ", "Indra, Rudra"),
        ("Fvõ", "Indra"),
        ("®õ", "Rudra"),
        ("cee@všieessejer", "Montgomery"),
        ("shudder", "Sindh"),
        ("Lord Kang", "Lord Canning"),
        ("john lawrence", "John Lawrence"),
        ("warren hasting", "Warren Hastings"),
        ("Jesus Vansittart", "Henry Vansittart"),
        ("henry dv", "Henry IV"),
        ("uegF& XIV", "Louis XIV"),
        ("uegF& XV", "Louis XV"),
        ("uegF& XIII", "Louis XIII"),
        ("ieebieeOej", "Gangadhar"),
        ("Dhondhoo Pant", "Dhondhu Pant"),
        ("jecesibn", "Rajendra"),
        ("francis merton", "Francois Martin"),
        ("lord batik", "Lord Bentinck"),
        ("lord dalhasy", "Lord Dalhousie"),
        ("lord akyton", "Lord Acton"),
        ("A. Kanigham", "A. Cunningham"),
        ("Sc. åJeeruej", "M. Wheeler"),
        ("R.D. Banjaa", "R.D. Banerjee"),
        ("francisco de almed", "Francisco de Almeida"),
        ("Lord Northubach", "Lord Northbrook"),
    ]
    for opt in opts_en:
        o = str(opt)
        for k, v in en_subs:
            o = o.replace(k, v)
        res.append(o.strip())
    return res

print("Executing comprehensive sweep across all 30 chapter files...")
for fname in files:
    fpath = os.path.join(CH_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    qs = data.get('questions', [])
    tq = len(qs)
    dur = max(60, tq)
    data['durationMinutes'] = dur
    data['duration_minutes'] = dur
    data['totalQuestions'] = tq
    data['total_questions'] = tq
    data['maxMarks'] = float(tq * 2.0)
    data['max_marks'] = float(tq * 2.0)

    for q in qs:
        # Hindi cleaning
        q['questionTextHi'] = clean_text_all(q.get('questionTextHi', ''))
        q['question_hi'] = q['questionTextHi']
        q['explanationHi'] = clean_text_all(q.get('explanationHi', ''))
        q['explanation_hi'] = q['explanationHi']

        opts_hi = [clean_text_all(o) for o in q.get('optionsHi', [])]
        q['optionsHi'] = opts_hi
        q['options_hi'] = opts_hi

        # English cleaning
        q_en = clean_text_all(q.get('questionTextEn', ''))
        # If En is still equal to Hi, translate
        if q_en == q['questionTextHi'] or not q_en or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in q_en):
            q_en = translation_cache.get(q['questionTextHi'], q_en)
            if q_en == q['questionTextHi']:
                # Call remote translate
                try:
                    u = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en&q={urllib.parse.quote(q['questionTextHi'])}"
                    r = requests.get(u, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
                    if r.status_code == 200:
                        d = r.json()
                        if isinstance(d, list) and d and isinstance(d[0], str):
                            q_en = d[0].strip()
                            translation_cache[q['questionTextHi']] = q_en
                except Exception:
                    pass
        q['questionTextEn'] = q_en
        q['question_en'] = q_en

        opts_en = clean_en_options(q.get('optionsEn', []))
        # Ensure opts_en != opts_hi
        for i in range(4):
            if opts_en[i] == opts_hi[i] or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in opts_en[i]):
                opts_en[i] = translation_cache.get(opts_hi[i], opts_en[i])
        q['optionsEn'] = opts_en
        q['options_en'] = opts_en

        exp_en = clean_text_all(q.get('explanationEn', ''))
        if not exp_en or exp_en == q['explanationHi'] or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in exp_en):
            core_exp = '. '.join([s.strip() for s in q['explanationHi'].split('।')[:2] if s.strip()])
            exp_en = translation_cache.get(core_exp, exp_en)
        q['explanationEn'] = exp_en
        q['explanation_en'] = exp_en

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Sweep completed successfully across all 30 files!")
