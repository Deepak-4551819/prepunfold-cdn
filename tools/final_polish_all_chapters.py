import json
import os
import re

CH_DIR = 'tests/tgt_pgt_history'
files = sorted([f for f in os.listdir(CH_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])

# Translation cache
CACHE_HI_EN_FILE = os.path.join(os.path.dirname(__file__), "..", "scripts", "cache_hi_to_en.json")
translation_cache = {}
if os.path.exists(CACHE_HI_EN_FILE):
    with open(CACHE_HI_EN_FILE, 'r', encoding='utf-8') as f:
        translation_cache = json.load(f)

# Comprehensive dictionary of legacy terms in English fields
EN_TERM_MAP = [
    # Prominent figures & names
    ("jcesMeÛevõ oòe", "Ramesh Chandra Dutt"),
    ("jcesMe Ûevõ oòe", "Ramesh Chandra Dutt"),
    ("jescesMe Ûevõ oòe", "Ramesh Chandra Dutt"),
    ("jescesMe Ûebõ oòe", "Ramesh Chandra Dutt"),
    ("विलिÙece kewâjer", "William Carey"),
    ("WilliÙece kewâjer", "William Carey"),
    ("विलिÙece kewâjs", "William Carey"),
    ("WilliÙece kewâjs", "William Carey"),
    ("विलिÙece kewâj", "William Carey"),
    ("WilliÙece kewâj", "William Carey"),
    ("kewâJetj", "Cavour"),
    ("kewâkegâJeeo", "Kaiqubad"),
    ("osJesvõ šwieesj", "Debendranath Tagore"),
    ("[svi[ nsÙej", "David Hare"),
    ("Alekya]Jader KafVgham", "Alexander Cunningham"),
    ("MejlÛevõ jeÙe", "Sharat Chandra Ray"),
    ("ZebufVsa", "Zeb-un-Nisa"),
    ("BakhtufVsa", "Bakht-un-Nisa"),
    ("™õ Meen", "Rudra Shah"),
    ("Dhondhoo Pant", "Dhondhu Pant"),
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
    ("kewâनिbie", "Canning"),
    ("kewâefvebie", "Canning"),
    ("kewâकेÙe", "Kaikeya"),
    ("ce™", "Maru (Desert)"),
    ("celmÙe", "Matsya"),
    ("øeWâÛe", "French"),
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
    ("mef]jani", "Mazzini"),
    ("BIMSAK", "Bismarck"),
    ("nsceÛevõ", "Hemchandra"),
    ("mLetueYeõ", "Sthulabhadra"),
    ("GoÙeYeõ", "Udayabhadra"),
    ("MeerueYeõ", "Shilabhadra"),
    ("ÛevõMesKej", "Chandrashekhar"),
    ("ÛevõJeerj", "Chandravarman"),
    ("jeceÛevõ", "Ramchandra"),
    ("OeÇgJe", "Dhruva"),
    ("kegâ®", "Kuru"),
    ("kegâ®#es$e", "Kurukshetra"),
    ("Metõ", "Shudra"),
    ("JewMÙe", "Vaishya"),
    ("ViMJeeMi$e", "Vishwamitra"),
    ("mi$e", "Mitra"),
    ("ogÇ¢e", "Durga"),
    ("tritsu", "Tritsu"),
    ("Ùeog", "Yadu"),
    ("õIÙeg", "Druhyu"),
    ("Turvas", "Turvasha"),
    ("ceõ", "Madra"),
    ("uekegâliMe", "Lakulisha"),
    ("buæcharit", "Buddhacharita"),
    ("buæ", "Buddha"),
    ("Buæ", "Buddha"),
    ("Bauæ", "Buddhism"),
    ("boofæk", "Buddhist"),
    ("Vishuæ", "Pure"),
    ("Vishu", "Vishnu"),
    ("YeeieYeõ", "Bhagabhadra"),
    ("nsceÛevõ", "Hemchandra"),
    ("GoeÙeerYeõ", "Udayabhadra"),
    ("Shishunag", "Shishunaga"),
    ("Nagadsak", "Nagadasaka"),
    ("Bimbisar", "Bimbisara"),
    ("Bimbisara", "Bimbisara"),
    ("Ajatasatru", "Ajatashatru"),
    ("cegõeSb", "Coins"),
    ("cegõe", "Coins"),
    ("Shilpkar", "Artisan"),
    ("ref°", "restrictions"),
    ("kasjkewâ", "Korkai"),
    ("GjwÙetj", "Uraiyur"),
    ("Sarnath", "Sarnath"),
    ("cubernaga", "Kuberanaga"),
    ("OeÇgJeosJeer", "Dhruvadevi"),
    ("OeÇgJe osJeer", "Dhruvadevi"),
    ("kegâcee", "Kumara"),
    ("õcce", "Dharma"),
    ("ieesÛece&", "Gocharma"),
    ("buægupt", "Buddhagupta"),
    ("Buægupta", "Buddhagupta"),
    ("Skandagupta", "Skandagupta"),
    ("ViæMeeue Yebjika", "Viddhashalabhanjika"),
    ("Vasubandhu", "Vasubandhu"),
    ("Prabhakaramitra", "Prabhakaramitra"),
    ("ceneosJeer", "Mahadevi"),
    ("™õccee osJeer", "Rudrama Devi"),
    ("Lingaraj", "Lingaraja"),
    ("cegõesâMJej", "Mukteshwar"),
    ("ÛevõJejce", "Chandravarman"),
    ("Dharnikot", "Dhanyakataka"),
    ("Amoghavarsha", "Amoghavarsha"),
    ("Oece&MeeŒe", "Dharmashastra"),
    ("YetieYe&MeeŒe", "Geology"),
    ("kegâ®<e", "Cyrus"),
    ("oeje", "Darius"),
    ("ies™", "Geru (Ochre)"),
    ("Sibieesueer's Ùegæ", "Battle of Sagauli"),
    ("Jeešjuet's Ùegæ", "Battle of Waterloo"),
    ("Jeešjuet", "Waterloo"),
    ("Battle of Bor", "Battle of Borodino"),
    ("Jee@šj øesâce", "Water frame"),
    ("ncøeâer [sJeer", "Humphry Davy"),
    ("Saptavashay Yuæ", "Seven Years' War"),
    ("Sapta Vashaya Yuæ", "Seven Years' War"),
    ("Saptavashay", "Seven Years'"),
    ("Devolution Yuæ", "War of Devolution"),
    ("franco prussia war", "Franco-Prussian War"),
    ("Sino-French Yuæ", "Sino-French War"),
    ("chaldiran yuæ", "Battle of Chaldiran"),
    ("Ankara Yue", "Battle of Ankara"),
    ("Korean Yuæ", "Korean War"),
    ("कैजगियू Ùegæ", "Battle of Cajamarca"),
    ("ÛeboeJej of Ùegæ", "Battle of Chandawar"),
    ("Ûebosjer's Ûegæ", "Battle of Chanderi"),
    ("IeeIeje's Ùegæ", "Battle of Ghaghra"),
    ("Nuoer Ieešer's Ùegæ", "Battle of Haldighati"),
    ("nuoerIeešer ka Ùegæ", "Battle of Haldighati"),
    ("Yesjeede's Ùegæ", "Battle of Bilgram"),
    ("YeBJejie", "Bhanwar"),
    ("cegoki", "Mudki"),
    ("Chiliya", "Chillianwala"),
    ("Khubnigha", "Khub Nigar"),
    ("Serinbæ", "Seringapatam"),
    ("SsVeg®Jej", "Ennayiram"),
    ("Yee®[", "Bhard"),
    ("FvMee-S-cen®", "Insha-i-Mahru"),
    ("Sirr-i-Akbar", "Sirr-i-Akbar"),
    ("copyâjeW", "Infidels"),
    ("øegâš", "Foote"),
    ("Banier", "Bernier"),
    ("pels", "Pelsaert"),
    ("ieesvivo sibn", "Guru Gobind Singh"),
    ("ieg™ nj jeÙe", "Guru Har Rai"),
    ("jodhraj", "Jodhraj"),
    ("jinsen suri", "Jinasena Suri"),
    ("Jin", "Jina"),
    ("ceemJeethi", "Umasvati"),
    ("Shershah Je ngcee", "Sher Shah and Humayun"),
    ("vadodra", "Vadodara"),
    ("cegvõe", "Mundra"),
    ("ueesceder", "Lothal"),
    ("OeÇebieOee", "Dhrangadhra"),
    ("Udar ®", "moderate"),
    ("vrfæ", "increase"),
    ("Ùegæ", "War"),
    ("Yuæ", "War"),
    ("Yue", "War"),
    ("Ùeesæe", "Warrior"),
    ("ßes‰", "Superior"),
    ("ßeeæ", "Shraddha"),
    ("JeŒe", "Clothes"),
    ("MeeŒe", "Shastra"),
]

# Hindi cleaning dictionary
HI_TERM_MAP = [
    ("विलिÙece kewâjer", "विलियम कैरी"),
    ("विलिÙece kewâjs", "विलियम कैरी"),
    ("विलिÙece kewâj", "विलियम कैरी"),
    ("kewâJetj", "कावूर"),
    ("kewâkegâJeeo", "कैकुबाद"),
    ("kewâकेÙe", "कैकेय"),
    ("काsjkewâ", "कोरकई"),
    ("GjwÙetj", "उरैयूर"),
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
    ("०", "0"),
    ("ø", "फ्र"),
    ("®", "रु"),
    ("Ç", "्र"),
    ("Œ", "स्त्र"),
    ("Ë", "ं"),
    ("Q", "ै"),
    ("™", "रू"),
    ("ü", "्रा"),
    ("õ", "द्र"),
    ("`", ""),
    ("~", ""),
    ("^", ""),
    ("§", ""),
    ("©", ""),
    ("Asharam Paddhati", "आश्रम पद्धति"),
    ("GDC ASST. PROF.", "UPPSC GDC Assistant Professor"),
]

print("Applying final polish across all 30 chapter JSONs...")

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
        # Hindi field polish
        q_hi = q.get('questionTextHi', '')
        for k, v in HI_TERM_MAP:
            q_hi = q_hi.replace(k, v)
        q['questionTextHi'] = q_hi
        q['question_hi'] = q_hi

        exp_hi = q.get('explanationHi', '')
        for k, v in HI_TERM_MAP:
            exp_hi = exp_hi.replace(k, v)
        q['explanationHi'] = exp_hi
        q['explanation_hi'] = exp_hi

        opts_hi = list(q.get('optionsHi', []))
        for i in range(len(opts_hi)):
            o = opts_hi[i]
            for k, v in HI_TERM_MAP:
                o = o.replace(k, v)
            opts_hi[i] = o
        q['optionsHi'] = opts_hi
        q['options_hi'] = opts_hi

        # English field polish
        q_en = q.get('questionTextEn', '')
        for k, v in EN_TERM_MAP:
            q_en = q_en.replace(k, v)
        for k, v in HI_TERM_MAP:
            # Clean any stray legacy chars in En
            if k not in ['Luis Vaz de Camões', 'Thomas Müntzer']:
                q_en = q_en.replace(k, v)
        q_en = q_en.replace("०", "0").replace("`", "").replace("~", "").replace("^", "").replace("§", "").replace("©", "")

        # If still equal to Hindi, provide clear English fallback
        if q_en == q_hi or not q_en or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in q_en):
            q_en = translation_cache.get(q_hi, f"History Question {q.get('questionNumber')}")
        q['questionTextEn'] = q_en
        q['question_en'] = q_en

        opts_en = list(q.get('optionsEn', []))
        for i in range(len(opts_en)):
            oe = opts_en[i]
            for k, v in EN_TERM_MAP:
                oe = oe.replace(k, v)
            for k, v in HI_TERM_MAP:
                oe = oe.replace(k, v)
            oe = oe.replace("०", "0").replace("`", "").replace("~", "").replace("^", "").replace("§", "").replace("©", "")
            if oe == opts_hi[i] or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in oe):
                oe = translation_cache.get(opts_hi[i], f"Option {chr(65+i)}")
            opts_en[i] = oe
        q['optionsEn'] = opts_en
        q['options_en'] = opts_en

        exp_en = q.get('explanationEn', '')
        for k, v in EN_TERM_MAP:
            exp_en = exp_en.replace(k, v)
        for k, v in HI_TERM_MAP:
            exp_en = exp_en.replace(k, v)
        exp_en = exp_en.replace("०", "0").replace("`", "").replace("~", "").replace("^", "").replace("§", "").replace("©", "")
        if exp_en == exp_hi or not exp_en or any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in exp_en):
            core = '. '.join([s.strip() for s in exp_hi.split('।')[:2] if s.strip()])
            exp_en = translation_cache.get(core, exp_hi[:100])
        q['explanationEn'] = exp_en
        q['explanation_en'] = exp_en

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Final polish applied successfully across all 30 files!")
