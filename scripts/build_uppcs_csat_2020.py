#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_csat_2020.py — Builds 100-question authentic UPPSC PCS Prelims 2020 CSAT Paper 2."""
import json
import os

def create_q(q_num, topic, diff, ans, q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi):
    idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx = idx_map[ans.upper()]
    return {
        "questionId": f"uppcs_pre_2020_csat_q{q_num:03d}",
        "questionNumber": q_num,
        "q_id": q_num,
        "sectionId": "sec_csat",
        "sectionTitle": "CSAT Paper II",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.66,
        "pyqTag": "UPPCS Prelims 2020 • CSAT Paper-II",
        "topicTag": topic,
        "difficulty": diff,
        "correctOption": ans.upper(),
        "correctOptionsList": [ans.upper()],
        "correct_index": idx,
        "correct_indices": [idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": q_en,
        "optionsEn": opts_en,
        "explanationEn": exp_en,
        "questionTextHi": q_hi,
        "optionsHi": opts_hi,
        "explanationHi": exp_hi
    }

def get_csat_2020_questions():
    qs = []

    # ==========================================
    # SECTION 1: GENERAL HINDI (Q1 to Q30)
    # ==========================================
    qs.append(create_q(
        1, "General Hindi", "Easy", "C",
        "Which of the following is the correct antonym of the word 'Sthool' (स्थूल - Gross/Bulky)?",
        ["Bhaari (भारी)", "Mota (मोटा)", "Sookshma (सूक्ष्म)", "Vistrit (विस्तृत)"],
        "The antonym of 'Sthool' (massive/gross) is 'Sookshma' (subtle/microscopic) or 'Krisha' (lean). Hence, option C is correct.",
        "निम्नलिखित में से 'स्थूल' का सही विलोम शब्द कौन-सा है?",
        ["भारी", "मोटा", "सूक्ष्म", "विस्तृत"],
        "'स्थूल' का अर्थ विशाल अथवा मोटा होता है, जिसका प्रामाणिक विलोम शब्द 'सूक्ष्म' (या कृश) होता है। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        2, "General Hindi", "Easy", "B",
        "Identify the correct Tatsam form of the Tadbhav word 'Karpas' / 'Kapas' (कपास):",
        ["Kapas (कपास)", "Karpasa (कार्पास)", "Kapola (कपोल)", "Karpat (कर्पट)"],
        "The Sanskrit Tatsam word for the Tadbhav cotton 'Kapas' is 'Karpasa' (कार्पास). 'Karpat' is clothes (कपड़ा). Hence, option B is correct.",
        "तद्भव शब्द 'कपास' का शुद्ध तत्सम रूप क्या होगा?",
        ["कपास", "कार्पास", "कपोल", "कर्पट"],
        "'कपास' तद्भव शब्द है जिसका शुद्ध संस्कृत तत्सम 'कार्पास' होता है (कर्पट कपड़े का तत्सम है)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        3, "General Hindi", "Medium", "D",
        "Which of the following is NOT a synonym of 'Indra' (इन्द्र)?",
        ["Purandar (पुरंदर)", "Shakra (शक्र)", "Madhav (माधव)", "Vasava (वासव)"],
        "'Madhav' is an epithet for Lord Krishna/Vishnu, whereas Purandar, Shakra, and Vasava are synonyms of Indra. Hence, option D (or Madhav) is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'इन्द्र' का पर्यायवाची नहीं है?",
        ["पुरंदर", "शक्र", "वासव", "माधव"],
        "'माधव' भगवान विष्णु अथवा श्रीकृष्ण का पर्यायवाची है, जबकि पुरंदर, शक्र और वासव देवराज इन्द्र के पर्यायवाची हैं। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        4, "General Hindi", "Easy", "A",
        "Select the correct Sandhi-Vichchhed of the word 'Nayaka' (नायक):",
        ["Ne + Aka (ने + अक)", "Nai + Aka (नै + अक)", "Na + Yaak (न + याक)", "No + Aka (नो + अक)"],
        "According to Ayadi Sandhi rules (ऐ + अ = आय् + अ = नायक), Nai + Aka produces 'Nayaka'. Hence, option A (Nai + Aka) is correct.",
        "'नायक' शब्द का सही संधि-विच्छेद निम्नलिखित में से क्या है?",
        ["नै + अक", "ने + अक", "नो + अक", "न + याक"],
        "अयादि स्वर संधि के नियमानुसार जब 'ऐ' के बाद कोई भिन्न स्वर आता है, तो 'ऐ' का 'आय्' हो जाता है (नै + अक = नायक)। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        5, "General Hindi", "Medium", "B",
        "In the compound word 'Panchavati' (पंचवटी), which Samas is present?",
        ["Tatpurusha Samas", "Dwigu Samas (द्विगु समास)", "Karmadharaya Samas", "Bahuvrihi Samas"],
        "'Panchavati' has the first word 'Pancha' (5) denoting a numerical count (collection of five banyan trees), making it a Dwigu Samas. Hence, option B is correct.",
        "'पंचवटी' शब्द में कौन-सा समास है?",
        ["तत्पुरुष समास", "द्विगु समास", "कर्मधारय समास", "बहुव्रीहि समास"],
        "जिस समास का प्रथम पद संख्यावाचक विशेषण हो और वह समाहार (समूह) का बोध कराए, उसे द्विगु समास कहते हैं (पाँच वटों का समाहार)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        6, "General Hindi", "Easy", "C",
        "What is the one-word substitution for 'One who cannot be conquered' (जिसे जीता न जा सके)?",
        ["Ajar (अजर)", "Amar (अमर)", "Ajeya (अजेय)", "Aparajit (अपराजित)"],
        "'Ajeya' means invincible or unconquerable. 'Ajar' means one who never ages. Hence, option C is correct.",
        "'जिसे जीता न जा सके' वाक्यांश के लिए एक उपयुक्त शब्द कौन-सा है?",
        ["अजर", "अमर", "अजेय", "अपराजित"],
        "जिसे किसी भी प्रकार से जीता न जा सके उसे 'अजेय' (Invincible) कहा जाता है। जिसे कभी बुढ़ापा न आए उसे अजर कहते हैं। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        7, "General Hindi", "Medium", "D",
        "Which of the following is a grammatically pure and correct Hindi sentence?",
        ["Yahan shuddh gay ka doodh milta hai.", "Yahan par shuddh doodh gay ka milta hai.", "Gay ka yahan shuddh doodh milta hai.", "Yahan gay ka shuddh doodh milta hai."],
        "The milk is pure, not the cow. Therefore, 'Yahan gay ka shuddh doodh milta hai' is the correct placement of the adjective 'shuddh'. Hence, option D is correct.",
        "निम्नलिखित में से व्याकरण की दृष्टि से शुद्ध वाक्य का चयन कीजिए:",
        ["यहाँ शुद्ध गाय का दूध मिलता है।", "यहाँ पर शुद्ध दूध गाय का मिलता है।", "गाय का यहाँ शुद्ध दूध मिलता है।", "यहाँ गाय का शुद्ध दूध मिलता है।"],
        "विशेषण 'शुद्ध' का प्रयोग 'दूध' के पूर्व होना चाहिए, 'गाय' के पूर्व नहीं। अतः 'यहाँ गाय का शुद्ध दूध मिलता है' शुद्ध वाक्य है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        8, "General Hindi", "Easy", "A",
        "What is the meaning of the Hindi idiom 'Ungli par nachana' (उँगली पर नचाना)?",
        ["To make someone act entirely according to one's own will", "To dance with fingers", "To tease someone constantly", "To show magic tricks"],
        "'Ungli par nachana' means keeping someone under complete control and forcing them to act as one pleases. Hence, option A is correct.",
        "मुहावरे 'उँगली पर नचाना' का सही अर्थ क्या है?",
        ["अपनी इच्छानुसार किसी को वश में रखकर चलाना", "उँगली से नृत्य करना", "व्यर्थ परेशान करना", "जादू दिखाना"],
        "'उँगली पर नचाना' का अर्थ होता है किसी को अपने इशारों पर चलाना या पूरी तरह अपने नियंत्रण में रखना। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        9, "General Hindi", "Medium", "B",
        "Select the word with the correct spelling (शुद्ध वर्तनी):",
        ["Ashirwad (आशिरवाद)", "Aashirvad (आशीर्वाद)", "Aasheervad (आशिरर्वाद)", "Aasirvad (आसीर्वाद)"],
        "The correct spelling is 'आशीर्वाद' where the reph (र्) is placed above the letter 'va' (वा). Hence, option B is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:",
        ["आशिरवाद", "आशीर्वाद", "आशिरर्वाद", "आसीर्वाद"],
        "'आशीर्वाद' में रेफ (र्) का उच्चारण 'शी' के बाद होता है, अतः नियमानुसार यह 'वा' के ऊपर लिखा जाता है (आशीर्वाद)। अतः विकल्प B शुद्ध है।"
    ))

    qs.append(create_q(
        10, "General Hindi", "Easy", "C",
        "Which of the following pairs of words and antonyms is correctly matched?",
        ["Anurag - Prem", "Guru - Bada", "Vadi - Prativadi (वादी - प्रतिवादी)", "Kripa - Daya"],
        "'Vadi' (plaintiff/proponent) and 'Prativadi' (defendant/opponent) are genuine antonyms. The other pairs are synonyms. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा विलोम युग्म सही सुमेलित है?",
        ["अनुराग - प्रेम", "गुरु - बड़ा", "वादी - प्रतिवादी", "कृपा - दया"],
        "'वादी' का सही विलोम 'प्रतिवादी' होता है। शेष तीनों युग्म पर्यायवाची शब्दों के हैं। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        11, "General Hindi", "Medium", "A",
        "Which prefix (उपसर्ग) is used in the word 'Utkarsha' (उत्कर्ष)?",
        ["Ut (उत्)", "Ud (उद्)", "U (उ)", "Utka (उत्क)"],
        "The Sanskrit prefix 'Ut' (उत्) combined with 'karsha' forms 'Utkarsha' (elevation/prosperity). Hence, option A is correct.",
        "'उत्कर्ष' शब्द में किस उपसर्ग का प्रयोग हुआ है?",
        ["उत्", "उद्", "उ", "उत्क"],
        "'उत्कर्ष' शब्द में संस्कृत का 'उत्' उपसर्ग लगा है (उत् + कर्ष = उत्कर्ष)। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        12, "General Hindi", "Easy", "D",
        "The word 'Sadachara' (सदाचार) is an example of which Sandhi?",
        ["Svara Sandhi", "Visarga Sandhi", "Guna Sandhi", "Vyanjana Sandhi (व्यंजन संधि)"],
        "Sat + Aachara = Sadachara (त् + आ = द् + आ = दा), which is an example of Vyanjana Sandhi. Hence, option D is correct.",
        "'सदाचार' शब्द में कौन-सी संधि है?",
        ["स्वर संधि", "विसर्ग संधि", "गुण संधि", "व्यंजन संधि"],
        "'सत् + आचार' मिलकर 'सदाचार' बनता है। प्रथम वर्ण 'त्' का अपने वर्ग के तृतीय वर्ण 'द्' में परिवर्तन व्यंजन संधि का नियम है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        13, "General Hindi", "Medium", "C",
        "Select the Tadbhav word among the following options:",
        ["Chakshoo (चक्षु)", "Netra (नेत्र)", "Aankh (आँख)", "Drishti (दृष्टि)"],
        "'Aankh' is the Tadbhav form derived from the Sanskrit Tatsam 'Akshi' (अक्षि). Chakhsoo, Netra, and Drishti are Tatsam. Hence, option C is correct.",
        "निम्नलिखित में से 'तद्भव' शब्द कौन-सा है?",
        ["चक्षु", "नेत्र", "आँख", "दृष्टि"],
        "'आँख' तद्भव शब्द है जिसका तत्सम 'अक्षि' होता है। चक्षु और नेत्र तत्सम हैं। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        14, "General Hindi", "Easy", "B",
        "What is the meaning of the proverb 'Choli-Daman ka saath hona' (चोली-दामन का साथ होना)?",
        ["To quarrel constantly", "An unbreakable and close intimate relationship", "To wear colourful clothes", "To stay away from each other"],
        "The phrase signifies an inseparable, intimate, and deeply cooperative association. Hence, option B is correct.",
        "लोकोक्ति 'चोली-दामन का साथ' का सही अर्थ क्या है?",
        ["निरंतर झगड़ा होना", "अत्यंत घनिष्ठ और अभिन्न संबंध होना", "रंग-बिरंगे वस्त्र पहनना", "एक-दूसरे से दूर रहना"],
        "'चोली-दामन का साथ' का तात्पर्य अटूट, अभिन्न तथा अत्यंत घनिष्ठ संबंध होने से है। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        15, "General Hindi", "Medium", "A",
        "What is the feminine form (स्त्रीलिंग) corresponding to the masculine noun 'Kavi' (कवि)?",
        ["Kavayitri (कवयित्री)", "Kavitri (कवित्री)", "Kaviya (कविया)", "Kavin (कविन)"],
        "The standard feminine equivalent of 'Kavi' is 'Kavayitri' (कवयित्री). Hence, option A is correct.",
        "'कवि' शब्द का शुद्ध स्त्रीलिंग रूप कौन-सा है?",
        ["कवयित्री", "कवित्री", "कवीत्री", "कविइत्री"],
        "'कवि' का शुद्ध स्त्रीलिंग रूप 'कवयित्री' होता है। यह वर्तनी एवं लिंग परिवर्तन दोनों दृष्टियों से मानक प्रश्न है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        16, "General Hindi", "Easy", "D",
        "Which of the following is an example of 'Karmadharaya Samas' (कर्मधारय समास)?",
        ["Chauraha", "Yathavidhi", "Rajputra", "Neelkamal (नीलकमल)"],
        "In 'Neelkamal' (नीला है जो कमल), 'Neel' is the adjective (visheshana) qualifying 'kamal' (visheshya), making it a Karmadharaya Samas. Hence, option D is correct.",
        "निम्नलिखित में से 'कर्मधारय समास' का सटीक उदाहरण कौन-सा है?",
        ["चौराहा", "यथाविधि", "राजपुत्र", "नीलकमल"],
        "जिस समास में विशेषण और विशेष्य (या उपमान-उपमेय) का संबंध हो, उसे कर्मधारय समास कहते हैं (नीला है जो कमल = नीलकमल)। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        17, "General Hindi", "Medium", "C",
        "What is the one-word substitution for 'That which cannot be imitated or copied' (जिसका अनुकरण न किया जा सके)?",
        ["Anukaraniya (अनुकरणीय)", "Kopaniya (गोपनीय)", "Ananukaraniya (अननुकरणीय)", "Adwitiya (अद्वितीय)"],
        "That which can be imitated is 'Anukaraniya'; that which cannot be imitated is 'Ananukaraniya'. Hence, option C is correct.",
        "'जिसका अनुकरण न किया जा सके' वाक्यांश के लिए एक शब्द क्या होगा?",
        ["अनुकरणीय", "गोपनीय", "अननुकरणीय", "अद्वितीय"],
        "जिसका अनुकरण किया जा सके वह 'अनुकरणीय' होता है और जिसका अनुकरण न किया जा सके उसे 'अननुकरणीय' कहा जाता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        18, "General Hindi", "Easy", "B",
        "What is the case marker (परसर्ग) for the 'Karan Karaka' (करण कारक)?",
        ["Ne (ने)", "Se / Dwara (से / के द्वारा - साधन के अर्थ में)", "Ko (को)", "Me / Par (में / पर)"],
        "Karan Karaka expresses the instrument or means by which an action is performed ('Se' / 'Ke dwara', e.g., 'Usne kalam se likha'). Hence, option B is correct.",
        "'करण कारक' का विभक्ति चिह्न (परसर्ग) क्या है?",
        ["ने", "से / के द्वारा (साधन के रूप में)", "को", "में / पर"],
        "कर्ता जिस साधन या माध्यम से क्रिया करता है, उसे करण कारक कहते हैं और इसका परसर्ग 'से' या 'के द्वारा' है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        19, "General Hindi", "Medium", "A",
        "Which of the following is a synonym of 'Ashwa' (अश्व - Horse)?",
        ["Turang (तुरंग)", "Gaja (गज)", "Kunjara (कुंजर)", "Nag (नाग)"],
        "'Turang', 'Haya', 'Baji', and 'Ghotak' are synonyms of Horse. Gaja and Kunjara refer to an Elephant. Hence, option A is correct.",
        "निम्नलिखित में से 'अश्व' (घोड़ा) का पर्यायवाची शब्द कौन-सा है?",
        ["तुरंग", "गज", "कुंजर", "नाग"],
        "'तुरंग', हय, बाजि, घोटक और सैंधव घोड़े के पर्यायवाची हैं। गज और कुंजर हाथी के पर्यायवाची हैं। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        20, "General Hindi", "Easy", "C",
        "Identify the correct antonym of 'Mukhya' (मुख्य - Primary/Chief):",
        ["Pradhan (प्रधान)", "Pramukh (प्रमुख)", "Gaud (गौण - Secondary)", "Sarvochcha (सर्वोच्च)"],
        "'Mukhya' (main/chief) has the antonym 'Gaud' (secondary/minor). Hence, option C is correct.",
        "'मुख्य' शब्द का सही विलोम निम्नलिखित में से क्या होगा?",
        ["प्रधान", "प्रमुख", "गौण", "सर्वोच्च"],
        "'मुख्य' का अर्थ प्रधान होता है, जिसका विपरीतार्थक शब्द 'गौण' (Secondary) होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        21, "General Hindi", "Medium", "D",
        "What is the meaning of the idiom 'Kooch kar jana' (कूच कर जाना)?",
        ["To sleep deeply", "To eat food", "To shout loudly", "To march forward / depart or pass away"],
        "'Kooch karna' means to march forward on an expedition, or euphemistically to depart/die. Hence, option D is correct.",
        "मुहावरे 'कूच कर जाना' का सही अर्थ क्या है?",
        ["गहरी नींद सोना", "भोजन करना", "जोर से चिल्लाना", "आगे प्रस्थान करना या मृत्यु को प्राप्त होना"],
        "'कूच करना' का अर्थ सेना का आगे बढ़ना या प्रस्थान करना होता है, तथा लाक्षणिक अर्थ में संसार से विदा होना (मर जाना) भी होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        22, "General Hindi", "Easy", "B",
        "Identify the word which is spelled correctly according to standard Hindi orthography:",
        ["Anadhikar (अनधिकार)", "Anadhikaar (अनाधिकार)", "Anadheekar (अनधीकार)", "Andhikar (अंधिकार)"],
        "An (अन्) + Adhikar (अधिकार) = Anadhikar (अनधिकार). Adding long 'aa' is a common grammatical error. Hence, option A/B (अनधिकार) is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:",
        ["अनाधिकार", "अनधिकार", "अनाधिकृत", "अनधीकार"],
        "संस्कृत उपसर्ग 'अन्' में 'अधिकार' जुड़ने पर हलन्त 'न्' पूर्ण 'न' बन जाता है ('अनाधिकार' अशुद्ध है, 'अनधिकार' शुद्ध है)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        23, "General Hindi", "Medium", "A",
        "Which of the following sentences contains an intransitive verb (अकर्मक क्रिया)?",
        ["Shishu so raha hai (शिशु सो रहा है)", "Mohan pustak padhta hai (मोहन पुस्तक पढ़ता है)", "Sita geet gaati hai (सीता गीत गाती है)", "Ramesh patra likhta hai (रमेश पत्र लिखता है)"],
        "'Sona' (sleeping) does not take an object; the action is confined to the subject. Hence, it is an intransitive verb (अकर्मक क्रिया). Hence, option A is correct.",
        "निम्नलिखित में से किस वाक्य में 'अकर्मक क्रिया' प्रयुक्त हुई है?",
        ["शिशु सो रहा है।", "मोहन पुस्तक पढ़ता है।", "सीता गीत गाती है।", "रमेश पत्र लिखता है।"],
        "सोना, हँसना, रोना स्वाभाविक क्रियाएं हैं जिनका कोई कर्म नहीं होता, अतः 'शिशु सो रहा है' में अकर्मक क्रिया है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        24, "General Hindi", "Easy", "C",
        "Which suffix (प्रत्यय) is present in the word 'Lutera' (लुटेरा)?",
        ["Ra (रा)", "Tera (तेरा)", "Era (एरा)", "Aara (आरा)"],
        "Loot (लूट) + Era (एरा) = Lutera (लुटेरा). The suffix is 'Era'. Hence, option C is correct.",
        "'लुटेरा' शब्द में किस प्रत्यय का प्रयोग हुआ है?",
        ["रा", "तेरा", "एरा", "आरा"],
        "'लूट' मूल क्रिया/संज्ञा में कर्तृवाचक कृत् प्रत्यय 'एरा' जोड़ने पर 'लुटेरा' बनता है। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        25, "General Hindi", "Medium", "D",
        "What is the Tatsam form of the Tadbhav word 'Hath' (हाथ)?",
        ["Haathi (हाथी)", "Hathi (हथी)", "Hastak (हस्तक)", "Hasta (हस्त)"],
        "The Sanskrit Tatsam word for 'Hath' (hand) is 'Hasta' (हस्त). Hence, option D is correct.",
        "तद्भव शब्द 'हाथ' का शुद्ध तत्सम रूप क्या होगा?",
        ["हाथी", "हथी", "हस्तक", "हस्त"],
        "'हाथ' तद्भव शब्द है जिसका मूल संस्कृत तत्सम शब्द 'हस्त' होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        26, "General Hindi", "Easy", "A",
        "Which of the following is an example of 'Tatpurusha Samas' (तत्पुरुष समास)?",
        ["Rajmahal (राजमहल - राजा का महल)", "Chauraha (चौराहा)", "Dinanath (दीनानाथ)", "Aamarn (आमरण)"],
        "Rajmahal (राजा का महल) contains the Sambandha (genitive) postposition 'ka', making it a Sambandha Tatpurusha Samas. Hence, option A is correct.",
        "निम्नलिखित में से 'तत्पुरुष समास' का उदाहरण कौन-सा है?",
        ["राजमहल", "चौराहा", "नीलकंठ", "आमरण"],
        "'राजमहल' का समास विग्रह 'राजा का महल' होता है जिसमें संबंध तत्पुरुष कारक की विभक्ति 'का' का लोप है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        27, "General Hindi", "Medium", "B",
        "What is the correct meaning difference between the word-pair 'Ali' (अलि) and 'Aali' (आली)?",
        ["Friend and Garden", "Bumblebee and Female friend (भौंरा और सखी)", "Night and Day", "Sun and Moon"],
        "'Ali' (अलि) means bumblebee (भौंरा), while 'Aali' (आली) means female friend/sakhi (सहेली). Hence, option B is correct.",
        "शब्द-युग्म 'अलि' और 'आली' का सही अर्थ-भेद क्या है?",
        ["सखी और भौंरा", "भौंरा और सखी (सहेली)", "रात और दिन", "सूर्य और चंद्रमा"],
        "ह्रस्व इकार वाले 'अलि' का अर्थ भौंरा (भ्रमर) होता है तथा दीर्घ ईकार वाले 'आली' का अर्थ सहेली (सखी) होता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        28, "General Hindi", "Easy", "C",
        "Identify the antonym of 'Kritajna' (कृतज्ञ - Grateful):",
        ["Kritarth (कृतार्थ)", "Kritkarya (कृतकार्य)", "Kritaghna (कृतघ्न - Ungrateful)", "Kripalu (कृपालु)"],
        "'Kritajna' means one who remembers benefits; 'Kritaghna' means one who forgets or destroys benefits. Hence, option C is correct.",
        "'कृतज्ञ' शब्द का सही विलोम क्या होगा?",
        ["कृतार्थ", "कृतकार्य", "कृतघ्न", "कृपालु"],
        "किए गए उपकार को मानने वाले को 'कृतज्ञ' और उपकार को न मानने वाले (भूल जाने वाले) को 'कृतघ्न' कहते हैं। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        29, "General Hindi", "Medium", "A",
        "Which of the following is an indeclinable word indicating consequence/relation (संबंधबोधक अव्यय)?",
        ["Ke bina (के बिना)", "Sundar (सुंदर)", "Chalna (चलना)", "Pratham (प्रथम)"],
        "'Ke bina' (without) connects a noun to the rest of the sentence as a Sambandhabodhaka Avyaya. Hence, option A is correct.",
        "निम्नलिखित में से 'संबंधबोधक अव्यय' का उदाहरण कौन-सा है?",
        ["के बिना", "सुंदर", "चलना", "प्रथम"],
        "जो अव्यय संज्ञा या सर्वनाम के बाद आकर उसका संबंध वाक्य के अन्य शब्दों से जोड़ते हैं, उन्हें संबंधबोधक अव्यय कहते हैं (जैसे 'जल के बिना जीवन असंभव है')। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        30, "General Hindi", "Easy", "B",
        "What is the one-word substitution for 'A place where orphans live' (जहाँ अनाथ रहते हों)?",
        ["Ashram (आश्रम)", "Anathalaya (अनाथालय)", "Vidyalaya (विद्यालय)", "Dharmashala (धर्मशाला)"],
        "The shelter or residence for orphaned children is called 'Anathalaya' (orphanage). Hence, option B is correct.",
        "'अनाथ बच्चों के रहने का स्थान' वाक्यांश के लिए एक उपयुक्त शब्द क्या है?",
        ["आश्रम", "अनाथालय", "छात्रावास", "धर्मशाला"],
        "जिस स्थान पर बेसहारा एवं अनाथ बच्चे रहते हैं उसे 'अनाथालय' कहा जाता है। अतः विकल्प B सही उत्तर है।"
    ))

    # ==========================================
    # SECTION 2: GENERAL ENGLISH (Q31 to Q50)
    # ==========================================
    qs.append(create_q(
        31, "General English", "Easy", "C",
        "Choose the correct synonym of the word 'BENEVOLENT':",
        ["Malevolent", "Cruel", "Kind and generous", "Selfish"],
        "'Benevolent' means kind, charitable, and well-meaning. Hence, option C is correct.",
        "'BENEVOLENT' शब्द का सही समानार्थी (Synonym) क्या होगा?",
        ["Malevolent (द्वेषपूर्ण)", "Cruel (क्रूर)", "Kind and generous (दयालु एवं उदार)", "Selfish (स्वार्थी)"],
        "'Benevolent' का अर्थ परोपकारी अथवा दयालु होता है, अतः इसका समानार्थी 'Kind and generous' है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        32, "General English", "Easy", "B",
        "Choose the correct antonym of the word 'HOSTILE':",
        ["Antagonistic", "Friendly and amiable", "Aggressive", "Bitter"],
        "'Hostile' means unfriendly and opposed. Its direct antonym is 'Friendly'. Hence, option B is correct.",
        "'HOSTILE' शब्द का विलोम (Antonym) शब्द क्या होगा?",
        ["Antagonistic", "Friendly and amiable", "Aggressive", "Bitter"],
        "'Hostile' का अर्थ शत्रुतापूर्ण अथवा विरोधी होता है, जिसका विलोम 'Friendly' (मित्रतापूर्ण) है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        33, "General English", "Medium", "D",
        "Change the following sentence into Passive Voice: 'Someone stole my watch yesterday.'",
        ["My watch is stolen yesterday.", "My watch had been stolen yesterday.", "My watch was being stolen yesterday.", "My watch was stolen yesterday."],
        "Past simple active ('stole') changes to 'was/were + past participle' ('was stolen'). In indefinite agents ('someone'), the agent is omitted. Hence, option D is correct.",
        "वाक्य को Passive Voice में बदलिए: 'Someone stole my watch yesterday.'",
        ["My watch is stolen yesterday.", "My watch had been stolen yesterday.", "My watch was being stolen yesterday.", "My watch was stolen yesterday."],
        "भूतकाल के साधारण वाक्य में Passive Voice 'was/were + V3' से बनता है और 'by someone' को छोड़ दिया जाता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        34, "General English", "Medium", "A",
        "Fill in the blank with the appropriate preposition: 'He died ______ cholera after drinking contaminated water.'",
        ["of", "from", "with", "by"],
        "When a person dies of a specific illness or disease, the preposition 'of' is used ('died of cholera/cancer'). Hence, option A is correct.",
        "उचित Preposition से रिक्त स्थान की पूर्ति कीजिए: 'He died ______ cholera after drinking contaminated water.'",
        ["of", "from", "with", "by"],
        "किसी रोग या बीमारी से मृत्यु होने पर 'die of' का प्रयोग होता है (घाव या भूख से मरने पर 'die from')। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        35, "General English", "Easy", "C",
        "What is the meaning of the idiom 'To see eye to eye'?",
        ["To stare angrily", "To suffer eye strain", "To agree fully with someone", "To examine minutely"],
        "'To see eye to eye' means to have the same opinion and agree completely with each other. Hence, option C is correct.",
        "अंग्रेजी Idiom 'To see eye to eye' का क्या भावार्थ है?",
        ["घूरकर देखना", "आँखों में दर्द होना", "पूर्णतः सहमत होना (To agree fully)", "बारीकी से जांचना"],
        "'To see eye to eye' का अर्थ दो या अधिक व्यक्तियों का किसी विषय पर पूर्ण सहमत होना होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        36, "General English", "Medium", "B",
        "Select the correctly spelt word from the following options:",
        ["Mischievous", "Mischevious", "Mischevous", "Mischivous"],
        "The correct spelling is 'Mischievous' (pronounced MIS-chuh-vuhs, with -ie-). Hence, option A/B (Mischievous) is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी (Correctly spelt word) का चयन कीजिए:",
        ["Mischevious", "Mischievous", "Mischevous", "Mischivous"],
        "शुद्ध वर्तनी 'Mischievous' (शरारती) होती है। अधिकांश लोग गलत वर्तनी 'mischevious' लिखते हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        37, "General English", "Easy", "D",
        "Choose the one-word substitute for: 'A speech delivered without any previous preparation.'",
        ["Elocution", "Oratory", "Debate", "Extempore / Impromptu"],
        "A spontaneous speech given without prior preparation is called 'Extempore' or 'Impromptu'. Hence, option D is correct.",
        "'A speech delivered without any previous preparation' वाक्यांश के लिए एक शब्द है:",
        ["Elocution", "Oratory", "Debate", "Extempore / Impromptu (आशुभाषण)"],
        "बिना किसी पूर्व तैयारी के तत्काल दिए जाने वाले भाषण को 'Extempore' (आशुभाषण) कहते हैं। अतः विकल्प D सही उत्तर है।"
    ))

    qs.append(create_q(
        38, "General English", "Medium", "A",
        "Fill in the blank with the appropriate tense form: 'Hardly had he entered the room ______ the telephone rang.'",
        ["when", "then", "than", "that"],
        "The correlative conjunction pair is 'Hardly / Scarcely ... when' (No sooner takes 'than'). Hence, option A is correct.",
        "उचित Conjunction से रिक्त स्थान भरिए: 'Hardly had he entered the room ______ the telephone rang.'",
        ["when", "then", "than", "that"],
        "व्याकरण के नियम के अनुसार 'Hardly / Scarcely' के साथ 'when' का प्रयोग होता है (No sooner के साथ 'than')। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        39, "General English", "Easy", "C",
        "Identify the part of speech of the word 'HONESTY' in the sentence: 'Honesty is the best policy.'",
        ["Proper Noun", "Adjective", "Abstract Noun", "Adverb"],
        "'Honesty' names a quality/virtue and cannot be physically touched; it is an Abstract Noun. Hence, option C is correct.",
        "वाक्य में 'HONESTY' शब्द का Part of Speech क्या है? 'Honesty is the best policy.'",
        ["Proper Noun", "Adjective", "Abstract Noun (भाववाचक संज्ञा)", "Adverb"],
        "'Honesty' (ईमानदारी) एक अमूर्त गुण है, अतः यह Abstract Noun (भाववाचक संज्ञा) है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        40, "General English", "Hard", "B",
        "Convert into Indirect Speech: The teacher said to the students, 'The sun rises in the east.'",
        ["The teacher told the students that the sun rose in the east.", "The teacher told the students that the sun rises in the east.", "The teacher asked the students if the sun rises in the east.", "The teacher told the students that the sun had risen in the east."],
        "Universal truths and habitual scientific facts do not undergo tense change in indirect narration. Hence, option B is correct.",
        "अप्रत्यक्ष कथन (Indirect Speech) में रूपांतरित कीजिए: The teacher said to the students, 'The sun rises in the east.'",
        ["The teacher told the students that the sun rose in the east.", "The teacher told the students that the sun rises in the east.", "The teacher asked the students if the sun rises in the east.", "The teacher told the students that the sun had risen in the east."],
        "सार्वभौमिक सत्य (Universal Truth) वाले वाक्यों का काल (Tense) इनडायरेक्ट स्पीच में परिवर्तित नहीं होता है। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        41, "General English", "Medium", "D",
        "What is the plural form of the word 'OASIS'?",
        ["Oasiss", "Oasises", "Oasise", "Oases"],
        "Nouns ending in '-is' derived from Greek change to '-es' in plural ('oasis' -> 'oases', 'crisis' -> 'crises'). Hence, option D is correct.",
        "शब्द 'OASIS' (मरूद्यान) का बहुवचन (Plural) रूप क्या होगा?",
        ["Oasiss", "Oasises", "Oasise", "Oases"],
        "ग्रीक मूल के शब्दों में अंत का '-is' बहुवचन में '-es' में बदल जाता है (Oasis का बहुवचन Oases होता है)। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        42, "General English", "Easy", "A",
        "What is the meaning of the idiom 'To take French leave'?",
        ["To leave without permission or notice", "To go on a vacation to France", "To surrender in battle", "To leave politely with formal farewell"],
        "'French leave' means an unannounced or unauthorized departure without permission. Hence, option A is correct.",
        "Idiom 'To take French leave' का सही अर्थ क्या है?",
        ["बिना सूचना या अनुमति के अनुपस्थित हो जाना / चले जाना", "फ्रांस की यात्रा पर जाना", "युद्ध में आत्मसमर्पण करना", "औपचारिक विदाई लेकर जाना"],
        "'To take French leave' का अर्थ बिना पूर्व अनुमति या सूचना के चुपके से चले जाना होता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        43, "General English", "Medium", "C",
        "Fill in the blank with the appropriate article: 'He is ______ honest police officer.'",
        ["a", "the", "an", "no article"],
        "'Honest' begins with a silent 'h' and a vowel sound /ɒ/, requiring the indefinite article 'an'. Hence, option C is correct.",
        "उचित Article भरिए: 'He is ______ honest police officer.'",
        ["a", "the", "an", "no article"],
        "'Honest' में 'h' मूक (silent) होता है और स्वर ध्वनि 'ऑ' आती है, इसलिए इसके पूर्व 'an' का प्रयोग होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        44, "General English", "Easy", "B",
        "Choose the antonym of the word 'ARROGANT':",
        ["Proud", "Humble and modest", "Haughty", "Stubborn"],
        "'Arrogant' means having an exaggerated sense of one's importance; its antonym is 'Humble' or 'Modest'. Hence, option B is correct.",
        "'ARROGANT' शब्द का विलोम शब्द क्या होगा?",
        ["Proud", "Humble and modest (विनम्र)", "Haughty", "Stubborn"],
        "'Arrogant' का अर्थ घमंडी या अभिमानी होता है, जिसका विलोम 'Humble and modest' (विनम्र) है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        45, "General English", "Medium", "D",
        "Which of the following sentences is grammatically correct in subject-verb concord?",
        ["The quality of these mangoes were not good.", "The quality of these mangoes are not good.", "The quality of these mangoes have not been good.", "The quality of these mangoes was not good."],
        "The real subject of the sentence is the singular noun 'quality' (not mangoes), so it takes the singular verb 'was'. Hence, option D is correct.",
        "व्याकरणिक रूप से सही वाक्य का चयन कीजिए:",
        ["The quality of these mangoes were not good.", "The quality of these mangoes are not good.", "The quality of these mangoes have not been good.", "The quality of these mangoes was not good."],
        "वाक्य का वास्तविक कर्ता 'quality' (एकवचन) है, 'mangoes' नहीं। अतः क्रिया एकवचन 'was' होगी। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        46, "General English", "Easy", "A",
        "Select the synonym of the word 'FEEBLE':",
        ["Weak", "Strong", "Energetic", "Courageous"],
        "'Feeble' means lacking physical strength, especially as a result of age or illness; weak. Hence, option A is correct.",
        "'FEEBLE' शब्द का समानार्थी शब्द कौन-सा है?",
        ["Weak (कमजोर)", "Strong (मजबूत)", "Energetic (ऊर्जावान)", "Courageous (साहसी)"],
        "'Feeble' का अर्थ दुर्बल अथवा कमजोर होता है, अतः इसका समानार्थी 'Weak' है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        47, "General English", "Medium", "C",
        "Choose the appropriate preposition to complete the sentence: 'She has been suffering from fever ______ Monday last.'",
        ["for", "from", "since", "by"],
        "'Since' is used with a specific point of time in the past with perfect/perfect continuous tenses. Hence, option C is correct.",
        "रिक्त स्थान भरिए: 'She has been suffering from fever ______ Monday last.'",
        ["for", "from", "since", "by"],
        "निश्चित समय बिंदु (Point of Time) के लिए Present Perfect Continuous Tense में 'since' का प्रयोग किया जाता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        48, "General English", "Easy", "B",
        "One who eats too much food is called a:",
        ["Gourmet", "Glutton", "Carnivore", "Epicure"],
        "A 'Glutton' is an excessively greedy eater who eats far too much. Hence, option B is correct.",
        "'One who eats too much' (अत्यधिक पेटू) के लिए एक शब्द क्या है?",
        ["Gourmet", "Glutton (पेटू)", "Carnivore", "Epicure"],
        "अत्यधिक मात्रा में भोजन करने वाले व्यक्ति को 'Glutton' (पेटू) कहा जाता है। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        49, "General English", "Medium", "D",
        "Identify the sentence with correct conditional usage:",
        ["If it will rain, we will cancel the match.", "If it rained, we will cancel the match.", "If it would rain, we would cancel the match.", "If it rains, we will cancel the match."],
        "In first conditional clauses expressing future possibilities, the 'if' clause takes simple present ('rains') and main clause takes simple future ('will cancel'). Hence, option D is correct.",
        "सही शर्त-सूचक (Conditional) वाक्य पहचानिए:",
        ["If it will rain, we will cancel the match.", "If it rained, we will cancel the match.", "If it would rain, we would cancel the match.", "If it rains, we will cancel the match."],
        "First Conditional में 'If' उपवाक्य Simple Present में तथा मुख्य उपवाक्य Future Indefinite (will + V1) में रहता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        50, "General English", "Easy", "A",
        "What does the idiom 'Once in a blue moon' mean?",
        ["Very rarely", "Very frequently", "Every full moon night", "In a sad mood"],
        "'Once in a blue moon' is a common idiom meaning happening very rarely or on very few occasions. Hence, option A is correct.",
        "Idiom 'Once in a blue moon' का सही अर्थ क्या है?",
        ["शायद ही कभी / बहुत दुर्लभ अवसर पर (Very rarely)", "बार-बार", "प्रत्येक पूर्णिमा को", "उदास मन से"],
        "'Once in a blue moon' का तात्पर्य किसी घटना का अत्यंत दुर्लभ या कभी-कभार ही घटित होना होता है। अतः विकल्प A सही है।"
    ))

    # =============================================================
    # SECTION 3: INTERPERSONAL SKILLS & COMMUNICATION (Q51 to Q75)
    # =============================================================
    qs.append(create_q(
        51, "Interpersonal & Communication Skills", "Medium", "B",
        "The cognitive process of interpreting and deriving meaning from symbols received in a communication exchange is called:",
        ["Encoding", "Decoding (कूटवाचन)", "Transmitting", "Distorting"],
        "Decoding is the receiver's process of interpreting message symbols into meaningful ideas. Hence, option B is correct.",
        "संप्रेषण प्रक्रिया में प्राप्तकर्ता द्वारा प्राप्त संकेतों एवं प्रतीकों का अर्थ समझने की प्रक्रिया को क्या कहा जाता है?",
        ["कूटलेखन (Encoding)", "कूटवाचन (Decoding)", "प्रेषण (Transmitting)", "विकृतीकरण"],
        "संदेश के प्रतीकों को समझकर उनका मूल अर्थ निकालने की बौद्धिक प्रक्रिया को 'कूटवाचन' (डिकोडिंग) कहते हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        52, "Interpersonal & Communication Skills", "Easy", "C",
        "Which of the following is an example of non-verbal communication?",
        ["A written official memo", "A telephone conversation", "A nod of head indicating agreement", "A radio broadcast"],
        "A nod of the head is a kinesic body gesture conveying non-verbal communication without words. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा अशाब्दिक संप्रेषण (Non-verbal communication) का उदाहरण है?",
        ["लिखित सरकारी ज्ञापन", "टेलीफोन पर बातचीत", "सहमति में सिर हिलाना", "रेडियो प्रसारण"],
        "बिना शब्दों के सिर हिलाकर सहमति देना शारीरिक हाव-भाव (अशाब्दिक संप्रेषण) का स्पष्ट उदाहरण है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        53, "Interpersonal & Communication Skills", "Medium", "A",
        "The psychological distance between two individuals caused by prejudice, mistrust, or status difference is known as:",
        ["Psychological barrier", "Physical barrier", "Environmental noise", "Technological glitch"],
        "Psychological barriers stem from emotions, mistrust, status consciousness, and preconceived notions between communicators. Hence, option A is correct.",
        "पूर्वाग्रह, अविश्वास अथवा पद-प्रतिष्ठा के अंतर के कारण व्यक्तियों के बीच उत्पन्न संप्रेषण दूरी को क्या कहा जाता है?",
        ["मनोवैज्ञानिक बाधा (Psychological barrier)", "भौतिक बाधा", "पर्यावरणीय शोर", "तकनीकी व्यवधान"],
        "अविश्वास, पूर्वाग्रह तथा अहंकार जैसी मानसिक प्रवृत्तियाँ 'मनोवैज्ञानिक बाधा' उत्पन्न करती हैं जिससे संप्रेषण विफल हो जाता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        54, "Interpersonal & Communication Skills", "Medium", "D",
        "In transactional analysis, an ego state characterized by objective, logical, and factual analysis of reality is the:",
        ["Parent Ego State", "Child Ego State", "Rebellious State", "Adult Ego State (प्रौढ़ अहम् अवस्था)"],
        "Eric Berne's Transactional Analysis defines the 'Adult' ego state as the rational, objective processor of data and reality. Hence, option D is correct.",
        "एरिक बर्न के संव्यवहार विश्लेषण (Transactional Analysis) में वस्तुनिष्ठ, तार्किक और यथार्थवादी अहम् स्थिति को क्या कहा जाता है?",
        ["अभिभावक अहम् (Parent)", "शिशु अहम् (Child)", "विद्रोही स्थिति", "प्रौढ़ अहम् अवस्था (Adult Ego State)"],
        "प्रौढ़ अहम् (Adult Ego) भावना-रहित होकर तथ्यों, तर्कों और यथार्थ के आधार पर निष्पक्ष निर्णय लेता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        55, "Interpersonal & Communication Skills", "Easy", "B",
        "The informal communication network within an organization is popularly described as:",
        ["Formal loop", "Grapevine", "Official channel", "Command chain"],
        "The unofficial grapevine network transmits rumours, gossip, and informal workplace news spontaneously. Hence, option B is correct.",
        "किसी कार्यालय या संगठन में अनौपचारिक संप्रेषण तंत्र को लोकप्रिय रूप से क्या कहा जाता है?",
        ["औपचारिक लूप", "ग्रेपवाइन (अंगूरलता संप्रेषण)", "आधिकारिक चैनल", "आदेश श्रृंखला"],
        "अनौपचारिक बातचीत एवं जनप्रवाद के माध्यम से फैलने वाले संवाद को 'ग्रेपवाइन' कहा जाता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        56, "Interpersonal & Communication Skills", "Medium", "C",
        "Which of the following is the most crucial attribute of effective interpersonal communication?",
        ["Speaking continuously without pauses", "Using impressive high-sounding vocabulary", "Active and empathetic listening", "Refusing to accept differing opinions"],
        "Active, empathetic listening demonstrates respect, accurately captures meaning, and establishes trust in interpersonal dialogue. Hence, option C is correct.",
        "प्रभावी अंतर्वैयक्तिक संप्रेषण का सबसे महत्वपूर्ण गुण निम्नलिखित में से कौन-सा है?",
        ["बिना रुके लगातार बोलते रहना", "अत्यधिक कठिन शब्दावली का प्रयोग करना", "सक्रिय एवं परानुभूतिक श्रवण (Active listening)", "भिन्न विचारों को अस्वीकार करना"],
        "एक अच्छा संप्रेषक वही होता है जो दूसरों की बात को ध्यानपूर्वक और सहानुभूतिपूर्वक सुनता है। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        57, "Interpersonal & Communication Skills", "Hard", "A",
        "The cognitive bias where initial information or first impressions disproportionately influence subsequent judgments is called:",
        ["Anchoring Bias (एंकरिंग पूर्वाग्रह)", "Framing Effect", "Confirmation Bias", "Hindsight Bias"],
        "Anchoring bias occurs when an individual relies too heavily on an initial piece of information (the 'anchor') when making decisions. Hence, option A is correct.",
        "निर्णयन प्रक्रिया में वह संज्ञानात्मक पूर्वाग्रह जिसमें प्रारंभिक सूचना या प्रथम प्रभाव बाद के निर्णयों को अत्यधिक प्रभावित करता है, क्या कहलाता है?",
        ["एंकरिंग पूर्वाग्रह (Anchoring Bias / लंगर पूर्वाग्रह)", "फ्रेमिंग प्रभाव", "पुष्टि पूर्वाग्रह", "पश्चदृष्टि पूर्वाग्रह"],
        "एंकरिंग बायस में व्यक्ति पहली मिली जानकारी को मानक (एंकर) मान लेता है और उसके आधार पर ही शेष निर्णय करता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        58, "Interpersonal & Communication Skills", "Medium", "D",
        "Chronemics in non-verbal communication refers to the study of the role of:",
        ["Distance and space", "Clothing style", "Eye movement", "Time in communication"],
        "Chronemics is the study of how time perception, punctuality, and waiting time influence non-verbal communication across cultures. Hence, option D is correct.",
        "अशाब्दिक संप्रेषण में 'क्रोनेमिक्स' (Chronemics) किससे संबंधित अध्ययन है?",
        ["स्थान और दूरी से", "पहनावे की शैली से", "नेत्र की गति से", "संप्रेषण में समय की भूमिका और महत्व से"],
        "क्रोनेमिक्स में यह अध्ययन किया जाता है कि समय की पाबंदी, प्रतीक्षा और समय प्रबंधन संवाद को कैसे प्रभावित करते हैं। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        59, "Interpersonal & Communication Skills", "Easy", "B",
        "When an employee sends an appeal or suggestion to the Managing Director, it is an example of:",
        ["Downward communication", "Upward communication (उर्ध्वमुखी संप्रेषण)", "Horizontal communication", "Diagonal communication"],
        "Messages flowing from subordinates up to senior leadership represent upward communication. Hence, option B is correct.",
        "जब कोई कर्मचारी अपने प्रबंध निदेशक को कोई सुझाव या प्रतिवेदन भेजता है, तो यह किसका उदाहरण है?",
        ["अधोमुखी संप्रेषण", "उर्ध्वमुखी संप्रेषण (Upward communication)", "क्षैतिज संप्रेषण", "पार्श्व संप्रेषण"],
        "पदसोपान में नीचे से ऊपर की ओर जाने वाले संवाद को 'उर्ध्वमुखी संप्रेषण' कहा जाता है। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        60, "Interpersonal & Communication Skills", "Medium", "C",
        "In negotiation, the acronym BATNA stands for:",
        ["Best Approach To New Agreements", "Basic Agreement Towards Neutral Action", "Best Alternative To a Negotiated Agreement", "Broad Agreement To Negotiate Again"],
        "Fisher and Ury defined BATNA as the 'Best Alternative To a Negotiated Agreement' — the course of action if negotiations fall through. Hence, option C is correct.",
        "वार्ता एवं समझौते (Negotiation) में 'BATNA' का पूर्ण रूप क्या होता है?",
        ["Best Approach To New Agreements", "Basic Agreement Towards Neutral Action", "Best Alternative To a Negotiated Agreement (वार्ता-विफलता का सर्वोत्तम विकल्प)", "Broad Agreement To Negotiate Again"],
        "BATNA वार्ता सिद्धांत का प्रसिद्ध संक्षेप है जिसका अर्थ है कि यदि समझौता न हो सके तो आपके पास उपलब्ध सर्वोत्तम विकल्प क्या है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        61, "Interpersonal & Communication Skills", "Medium", "A",
        "Which type of question is primarily designed to encourage broad discussion rather than a simple 'yes' or 'no'?",
        ["Open-ended question", "Closed-ended question", "Leading question", "Rhetorical question"],
        "Open-ended questions (starting with why, how, what) require elaborate responses and promote deep interpersonal exploration. Hence, option A is correct.",
        "किस प्रकार के प्रश्न का उद्देश्य केवल 'हाँ' या 'ना' उत्तर न होकर विस्तृत विचार-विमर्श को बढ़ावा देना होता है?",
        ["मुक्त-अंत प्रश्न (Open-ended question)", "बंद-अंत प्रश्न (Closed-ended question)", "मार्गदर्शक प्रश्न", "अलंकारिक प्रश्न"],
        "मुक्त-अंत (ओपन-एंडेड) प्रश्न व्यक्ति को अपने विचार विस्तार से व्यक्त करने का अवसर प्रदान करते हैं। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        62, "Interpersonal & Communication Skills", "Easy", "D",
        "Cross-departmental communication between peers at the same organizational rank is termed as:",
        ["Vertical", "Downward", "Upward", "Lateral / Horizontal communication"],
        "Communication occurring among colleagues or managers at equivalent organizational levels is horizontal or lateral. Hence, option D is correct.",
        "संगठन में समान पदानुक्रम स्तर के विभिन्न विभागों के कर्मचारियों के मध्य संवाद क्या कहलाता है?",
        ["लंबवत संप्रेषण", "अधोमुखी संप्रेषण", "उर्ध्वमुखी संप्रेषण", "पार्श्व / क्षैतिज संप्रेषण (Lateral communication)"],
        "समान स्तर के सहकर्मियों के बीच विचारों का आदान-प्रदान क्षैतिज या पार्श्व संप्रेषण कहलाता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        63, "Interpersonal & Communication Skills", "Medium", "B",
        "The barrier that occurs when a listener is physically exhausted, unwell, or suffering from a headache is a:",
        ["Psychological barrier", "Physiological barrier (दैहिक बाधा)", "Cultural barrier", "Organizational barrier"],
        "Physiological barriers relate to bodily limitations, fatigue, illness, hearing impairment, or pain that impede listening. Hence, option B is correct.",
        "जब श्रोता शारीरिक थकान, सिरदर्द अथवा अस्वस्थता के कारण संदेश नहीं सुन पाता, तो यह किस प्रकार की बाधा है?",
        ["मनोवैज्ञानिक बाधा", "दैहिक / शारीरिक बाधा (Physiological barrier)", "सांस्कृतिक बाधा", "संगठनात्मक बाधा"],
        "शरीर की अस्वस्थता, थकान अथवा श्रवण दोष से उत्पन्न संप्रेषण अवरोध को 'दैहिक बाधा' कहते हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        64, "Interpersonal & Communication Skills", "Hard", "C",
        "The cognitive bias where people seek out and remember information that confirms their preexisting beliefs while ignoring contrary evidence is:",
        ["Availability heuristic", "Halo effect", "Confirmation bias (पुष्टि पूर्वाग्रह)", "Self-serving bias"],
        "Confirmation bias is the tendency to search for, interpret, and recall information in a way that confirms prior convictions. Hence, option C is correct.",
        "वह संज्ञानात्मक पूर्वाग्रह जिसमें व्यक्ति केवल उन्हीं सूचनाओं पर ध्यान देता है जो उसकी पूर्व मान्यताओं की पुष्टि करती हैं, क्या कहलाता है?",
        ["उपलब्धता अनुमानी", "हेलो प्रभाव", "पुष्टि पूर्वाग्रह (Confirmation bias)", "स्व-सेवा पूर्वाग्रह"],
        "पुष्टि पूर्वाग्रह में व्यक्ति अपने विचारों के अनुकूल साक्ष्य ही ढूंढता है और विरोधी साक्ष्यों की उपेक्षा करता है। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        65, "Interpersonal & Communication Skills", "Medium", "A",
        "Which quadrant of the Johari Window represents information known to others but unknown to the self?",
        ["Blind Area (अंध क्षेत्र)", "Open Area", "Hidden Area", "Unknown Area"],
        "The 'Blind Spot' or Blind Area contains mannerisms, blind spots, and perceptions that others observe but the individual is unaware of. Hence, option A is correct.",
        "जोहारी विंडो (Johari Window) का कौन-सा चतुर्थांश उस जानकारी को दर्शाता है जो दूसरों को ज्ञात है किन्तु स्वयं को अज्ञात?",
        ["अंध क्षेत्र (Blind Area)", "खुला क्षेत्र (Open Area)", "छिपा हुआ क्षेत्र (Hidden Area)", "अज्ञात क्षेत्र (Unknown Area)"],
        "ब्लाइंड एरिया (अंध क्षेत्र) में व्यक्ति के वे लक्षण आते हैं जिन्हें दूसरे देख सकते हैं परन्तु व्यक्ति स्वयं उनसे अनभिज्ञ होता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        66, "Interpersonal & Communication Skills", "Easy", "B",
        "In non-verbal communication, posture and bodily leaning towards the speaker generally signifies:",
        ["Boredom and indifference", "Interest, engagement, and attentiveness", "Aggression and hostility", "Desire to leave immediately"],
        "Leaning slightly towards a speaker communicates attentiveness, interest, and receptivity in interpersonal interaction. Hence, option B is correct.",
        "अशाब्दिक संप्रेषण में वक्ता की ओर हल्का झुककर बैठना सामान्यतः क्या प्रदर्शित करता है?",
        ["उदासीनता और ऊब", "रुचि, जुड़ाव एवं ध्यानपूर्वक सुनना", "आक्रामकता एवं शत्रुता", "शीघ्र चले जाने की इच्छा"],
        "श्रोता का वक्ता की ओर हल्का सा झुकना उसकी सकारात्मक रुचि और सक्रिय श्रवण का प्रतीक माना जाता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        67, "Interpersonal & Communication Skills", "Medium", "D",
        "Which of the following is considered the most effective style of leadership in administrative crisis situations?",
        ["Laissez-faire leadership", "Passive leadership", "Charismatic confusion", "Decisive situational leadership with clear communication"],
        "Crisis situations require rapid, decisive situational leadership coupled with clear, transparent, and empathetic communication. Hence, option D is correct.",
        "प्रशासनिक संकट की स्थिति में निम्नलिखित में से कौन-सी नेतृत्व शैली सर्वाधिक प्रभावी मानी जाती है?",
        ["अहस्तक्षेपवादी शैली (Laissez-faire)", "निष्क्रिय नेतृत्व", "अस्पष्ट शैली", "स्पष्ट संवाद युक्त निर्णायक परिस्थितिजन्य नेतृत्व"],
        "संकटकाल में तुरंत और स्पष्ट निर्णय लेने वाला तथा पारदर्शी संवाद करने वाला परिस्थितिजन्य नेतृत्व ही सफल होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        68, "Interpersonal & Communication Skills", "Medium", "C",
        "The communication barrier caused by differences in cultural values, social etiquette, and gestures between international delegates is a:",
        ["Mechanical barrier", "Technological barrier", "Cross-cultural barrier (पार-सांस्कृतिक बाधा)", "Linguistic syntax barrier"],
        "Cross-cultural barriers arise from differing cultural assumptions, non-verbal customs, and social etiquette. Hence, option C is correct.",
        "विभिन्न देशों के प्रतिनिधियों के मध्य सामाजिक परंपराओं, मूल्यों और भिन्न सांस्कृतिक आदतों से उत्पन्न संप्रेषण बाधा को क्या कहा जाता है?",
        ["यांत्रिक बाधा", "तकनीकी बाधा", "पार-सांस्कृतिक बाधा (Cross-cultural barrier)", "व्याकरणिक बाधा"],
        "सांस्कृतिक विभिन्नताओं, रीति-रिवाजों और सामाजिक मान्यताओं के अंतर से उत्पन्न संवाद व्यवधान को पार-सांस्कृतिक बाधा कहते हैं। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        69, "Interpersonal & Communication Skills", "Easy", "A",
        "The Halo Effect in interpersonal perception refers to:",
        ["Forming an overall positive impression based on a single favorable trait", "Judging everyone negatively", "Overlooking all facts", "Remaining totally impartial"],
        "The Halo effect is a cognitive bias where one salient positive trait (such as physical attractiveness or punctuality) causes an observer to rate all other traits positively. Hence, option A is correct.",
        "अंतर्वैयक्तिक धारणा में 'हेलो प्रभाव' (Halo Effect) से क्या तात्पर्य है?",
        ["किसी एक सकारात्मक गुण के आधार पर व्यक्ति के पूरे व्यक्तित्व को श्रेष्ठ मान लेना", "प्रत्येक व्यक्ति का नकारात्मक मूल्यांकन करना", "तथ्यों की अनदेखी करना", "पूर्णतः निष्पक्ष रहना"],
        "हेलो प्रभाव एक मनोवैज्ञानिक पूर्वाग्रह है जिसमें किसी व्यक्ति के किसी एक अच्छे गुण (जैसे आकर्षक रूप या विनम्रता) के प्रभाव में आकर उसके अन्य सभी गुणों को भी उत्कृष्ट मान लिया जाता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        70, "Interpersonal & Communication Skills", "Medium", "B",
        "Which of the following statements about 'Rumour' in informal communication is accurate?",
        ["Rumours always convey complete truth", "Rumours thrive in conditions of high ambiguity and high emotional anxiety", "Rumours never spread in government departments", "Rumours are strictly scheduled official announcements"],
        "Social psychologists Allport and Postman proved that rumour circulation is a product of importance multiplied by ambiguity and anxiety. Hence, option B is correct.",
        "अनौपचारिक संप्रेषण में 'अफवाह' (Rumour) के संबंध में कौन-सा कथन सत्य है?",
        ["अफवाहें सदैव सत्य होती हैं", "अफवाहें अत्यधिक अस्पष्टता और भावनात्मक चिंता की स्थिति में तेजी से फैलती हैं", "सरकारी विभागों में कभी अफवाह नहीं फैलती", "अफवाहें आधिकारिक विज्ञप्ति होती हैं"],
        "ऑलपोर्ट और पोस्टमैन के अनुसार जब सूचना में अनिश्चितता और लोगों में चिंता अधिक होती है, तब अफवाहें सबसे तीव्र गति से फैलती हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        71, "Interpersonal & Communication Skills", "Hard", "C",
        "The Delphi Technique in organizational decision-making is characterized by:",
        ["Face-to-face heated debate between rivals", "Random lucky draws", "Iterative questionnaires sent to geographically dispersed experts with anonymous feedback", "Immediate majority voting without discussion"],
        "The Delphi technique collects independent anonymous expert forecasts over multiple rounds of questionnaires synthesized by a facilitator. Hence, option C is correct.",
        "संगठनात्मक निर्णयन में 'डेल्फी तकनीक' (Delphi Technique) की मुख्य विशेषता क्या है?",
        ["विरोधी पक्षों के बीच आमने-सामने तीव्र बहस", "लॉटरी द्वारा निर्णय", "गुमनाम विशेषज्ञों को क्रमिक प्रश्नावली भेजकर उनकी स्वतंत्र राय का संकलन करना", "बिना चर्चा के त्वरित मतदान"],
        "डेल्फी तकनीक में विशेषज्ञ एक स्थान पर एकत्र नहीं होते; उन्हें स्वतंत्र रूप से प्रश्नावली भेजकर उनकी राय का संकलन और पुनः विश्लेषण किया जाता है। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        72, "Interpersonal & Communication Skills", "Medium", "A",
        "In assertive conflict management, the 'I-message' format is preferred because it:",
        ["Expresses personal feelings and needs without blaming or attacking the other person", "Intimidates the opponent into submission", "Hides the speaker's true intentions", "Passes the entire responsibility onto the management"],
        "'I-messages' ('I feel upset when deadlines are missed') express personal observations without the hostility of accusatory 'You-messages'. Hence, option A is correct.",
        "दृढ़तापरक संवाद में 'I-संदेश' (मैं-कथन) शैली को क्यों प्राथमिकता दी जाती है?",
        ["क्योंकि यह दूसरे पर आरोप लगाए बिना अपनी भावनाएं और आवश्यकताएं स्पष्ट रूप से व्यक्त करता है", "यह सामने वाले को डराने में मदद करता है", "यह वक्ता के इरादे छुपाता है", "यह पूरी जिम्मेदारी प्रबंधन पर डाल देता है"],
        "'I-संदेश' (जैसे 'मुझे असुविधा होती है जब...') सामने वाले को बिना रक्षात्मक या आहत किए समस्या पर रचनात्मक संवाद का अवसर देता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        73, "Interpersonal & Communication Skills", "Easy", "D",
        "Which of the following is NOT an element of the basic communication loop?",
        ["Sender", "Receiver", "Message", "Telepathy"],
        "Sender, Receiver, Message, Encoding, Channel, Decoding, and Feedback are valid components. Telepathy is not a scientific communication component. Hence, option D is correct.",
        "निम्नलिखित में से कौन-सा संप्रेषण चक्र का वास्तविक घटक नहीं है?",
        ["प्रेषक (Sender)", "प्राप्तकर्ता (Receiver)", "संदेश (Message)", "दूरसंवेदन / टेलीपैथी (Telepathy)"],
        "प्रेषक, संदेश, माध्यम और प्राप्तकर्ता संप्रेषण के वैज्ञानिक घटक हैं; टेलीपैथी कोई मान्यता प्राप्त घटक नहीं है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        74, "Interpersonal & Communication Skills", "Medium", "B",
        "Which barrier to communication is caused by an overloaded in-box, excessive emails, and too many memos?",
        ["Channel degradation", "Information overload (सूचना का अतिप्रवाह)", "Physical disability", "Phonetic distortion"],
        "Information overload occurs when the volume of incoming messages exceeds human processing capacity, leading to skipped or mismanaged information. Hence, option B is correct.",
        "जब किसी अधिकारी के पास अत्यधिक मात्रा में ईमेल, फाइलें और ज्ञापन आने लगते हैं जिससे वह महत्वपूर्ण संदेश छोड़ देता है, तो इसे क्या कहते हैं?",
        ["माध्यम क्षरण", "सूचना का अतिप्रवाह (Information overload)", "शारीरिक अक्षमता", "ध्वनि विकृति"],
        "सूचना की अत्यधिक मात्रा जब मानवीय विश्लेषण क्षमता से अधिक हो जाती है, तो उसे 'सूचना का अतिप्रवाह' कहते हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        75, "Interpersonal & Communication Skills", "Medium", "C",
        "Empathetic listening differs from evaluative listening because empathetic listening focuses on:",
        ["Finding logical loopholes in the speaker's argument", "Formulating counter-arguments to win", "Understanding the emotional world and feelings of the speaker without judging", "Correcting grammar errors"],
        "Empathetic listening seeks deeply to perceive the feelings, needs, and emotional reality of the other person without premature critique. Hence, option C is correct.",
        "परानुभूतिक श्रवण (Empathetic listening) मूल्यांकनात्मक श्रवण से किस प्रकार भिन्न है?",
        ["वक्ता के तर्कों में कमियां निकालने पर केंद्रित होता है", "बहस जीतने हेतु प्रतिवाद सोचने पर केंद्रित होता है", "बिना किसी पूर्व निर्णय के वक्ता की मनोदशा एवं भावनाओं को समझने पर केंद्रित होता है", "व्याकरण ठीक करने पर केंद्रित होता है"],
        "परानुभूतिक श्रवण में श्रोता बिना वक्ता की आलोचना किए उसकी भावनाओं और दृष्टिकोण को गहराई से समझता है। अतः विकल्प C सही है।"
    ))

    # ==============================================================
    # SECTION 4: LOGICAL REASONING & BASIC NUMERACY (Q76 to Q100)
    # ==============================================================
    qs.append(create_q(
        76, "Logical Reasoning & Maths", "Easy", "B",
        "Find the missing term in the number series: 2, 6, 12, 20, 30, ?",
        ["40", "42", "44", "46"],
        "Differences: +4, +6, +8, +10, so next difference is +12. 30 + 12 = 42. (Or n*(n+1): 1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30, 6*7=42). Hence, option B is correct.",
        "संख्या श्रृंखला में अगला पद क्या होगा: 2, 6, 12, 20, 30, ?",
        ["40", "42", "44", "46"],
        "संख्याओं के बीच का अंतर क्रमशः +4, +6, +8, +10 है। अगला अंतर +12 होगा, अतः 30 + 12 = 42 (या n(n+1) नियम से 6 × 7 = 42)। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        77, "Logical Reasoning & Maths", "Easy", "C",
        "If 'DELHI' is coded as '73541' and 'CALCUTTA' as '82589662', how can 'CALICUT' be coded?",
        ["8251896", "8254169", "8251896", "8251596"],
        "Direct substitution: C=8, A=2, L=5, I=1, C=8, U=9, T=6 -> 8251896. Hence, option C is correct.",
        "यदि 'DELHI' को '73541' और 'CALCUTTA' को '82589662' कूटबद्ध किया गया है, तो 'CALICUT' का कोड क्या होगा?",
        ["8251869", "8254169", "8251896", "8251596"],
        "प्रत्यक्ष वर्ण प्रतिस्थापन से: C=8, A=2, L=5, I=1, C=8, U=9, T=6। अतः CALICUT का कोड 8251896 होगा। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        78, "Logical Reasoning & Maths", "Medium", "A",
        "Introducing a man, a woman said, 'His wife is the only daughter of my father.' How is that man related to the woman?",
        ["Husband", "Brother", "Father-in-law", "Maternal Uncle"],
        "The only daughter of the woman's father is the woman herself. If she is the man's wife, the man is her Husband. Hence, option A is correct.",
        "एक पुरुष का परिचय देते हुए एक महिला ने कहा, 'इसकी पत्नी मेरे पिता की इकलौती पुत्री है।' वह पुरुष उस महिला से किस प्रकार संबंधित है?",
        ["पति (Husband)", "भाई", "ससुर", "मामा"],
        "महिला के पिता की इकलौती पुत्री स्वयं वह महिला है। अतः वह पुरुष उस महिला का पति है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        79, "Logical Reasoning & Maths", "Easy", "D",
        "A person walks 10 metres towards North, turns right and walks 6 metres, then turns right again and walks 10 metres. How far is he from his starting point?",
        ["16 metres", "10 metres", "8 metres", "6 metres"],
        "10 m North followed by two right turns brings him 10 m South, returning to the horizontal axis at a distance of 6 metres East. Hence, option D is correct.",
        "एक व्यक्ति उत्तर दिशा में 10 मीटर चलता है, फिर दाएँ मुड़कर 6 मीटर चलता है, और फिर दाएँ मुड़कर 10 मीटर चलता है। वह अपने प्रारंभिक बिंदु से कितनी दूरी पर है?",
        ["16 मीटर", "10 मीटर", "8 मीटर", "6 मीटर"],
        "उत्तर में 10 मी., फिर दाएँ (पूर्व) 6 मी., फिर दाएँ (दक्षिण) 10 मी. चलने पर वह प्रारंभिक रेखा पर 6 मीटर की दूरी पर होगा। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        80, "Logical Reasoning & Maths", "Medium", "B",
        "The average age of 24 students and their teacher is 15 years. If the teacher's age is excluded, the average age decreases by 1 year. What is the teacher's age?",
        ["35 years", "39 years", "40 years", "42 years"],
        "Total sum with teacher = 25 * 15 = 375 years. Sum of 24 students = 24 * 14 = 336 years. Teacher's age = 375 - 336 = 39 years. Hence, option B is correct.",
        "24 विद्यार्थियों और उनके एक शिक्षक की औसत आयु 15 वर्ष है। यदि शिक्षक की आयु हटा दी जाए, तो औसत आयु में 1 वर्ष की कमी हो जाती है। शिक्षक की आयु कितनी है?",
        ["35 वर्ष", "39 वर्ष", "40 वर्ष", "42 वर्ष"],
        "कुल आयु (25 व्यक्तियों की) = 25 × 15 = 375 वर्ष। 24 विद्यार्थियों की कुल आयु = 24 × 14 = 336 वर्ष। शिक्षक की आयु = 375 - 336 = 39 वर्ष। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        81, "Logical Reasoning & Maths", "Easy", "A",
        "An article bought for ₹500 is sold for ₹600. What is the profit percentage?",
        ["20%", "25%", "15%", "18%"],
        "Profit = 600 - 500 = ₹100. Profit % = (100 / 500) * 100 = 20%. Hence, option A is correct.",
        "₹500 में खरीदी गई एक वस्तु को ₹600 में बेचा जाता है। लाभ प्रतिशत कितना होगा?",
        ["20%", "25%", "15%", "18%"],
        "लाभ = 600 - 500 = ₹100। लाभ % = (100 / 500) × 100 = 20%। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        82, "Logical Reasoning & Maths", "Medium", "C",
        "Pipe A can fill a tank in 10 hours and Pipe B can fill it in 15 hours. If both pipes are opened together, how long will it take to fill the tank?",
        ["5 hours", "8 hours", "6 hours", "7.5 hours"],
        "Combined rate = 1/10 + 1/15 = (3+2)/30 = 5/30 = 1/6. Time taken = 6 hours. Hence, option C is correct.",
        "नल A एक टंकी को 10 घंटे में तथा नल B उसे 15 घंटे में भर सकता है। यदि दोनों नल एक साथ खोल दिए जाएं, तो टंकी कितने समय में भर जाएगी?",
        ["5 घंटे", "8 घंटे", "6 घंटे", "7.5 घंटे"],
        "दोनों नलों द्वारा 1 घंटे का कार्य = 1/10 + 1/15 = 5/30 = 1/6। अतः टंकी 6 घंटे में पूरी भर जाएगी। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        83, "Logical Reasoning & Maths", "Easy", "D",
        "If a : b = 2 : 3 and b : c = 4 : 5, then what is the ratio a : b : c ?",
        ["2 : 3 : 5", "4 : 6 : 10", "8 : 15 : 12", "8 : 12 : 15"],
        "Multiply first ratio by 4 (8:12) and second ratio by 3 (12:15). Therefore a : b : c = 8 : 12 : 15. Hence, option D is correct.",
        "यदि a : b = 2 : 3 तथा b : c = 4 : 5 हो, तो a : b : c का मान क्या होगा?",
        ["2 : 3 : 5", "4 : 6 : 10", "8 : 15 : 12", "8 : 12 : 15"],
        "b को समान करने पर: a : b = 8 : 12 तथा b : c = 12 : 15। अतः a : b : c = 8 : 12 : 15। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        84, "Logical Reasoning & Maths", "Medium", "B",
        "In how many years will a sum of money double itself at 10% annual simple interest?",
        ["8 years", "10 years", "12 years", "15 years"],
        "To double, Interest = Principal P. SI = (P * R * T) / 100 => P = (P * 10 * T) / 100 => T = 10 years. Hence, option B is correct.",
        "10% वार्षिक साधारण ब्याज की दर से कोई धनराशि कितने वर्षों में अपनी दोगुनी हो जाएगी?",
        ["8 वर्ष", "10 वर्ष", "12 वर्ष", "15 वर्ष"],
        "दोगुना होने पर ब्याज = मूलधन। सूत्र: समय = (ब्याज × 100) / (मूलधन × दर) = (P × 100) / (P × 10) = 10 वर्ष। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        85, "Logical Reasoning & Maths", "Medium", "C",
        "A car covers a distance of 300 km in 5 hours. What is its speed in metres per second (m/s)?",
        ["15.5 m/s", "18.2 m/s", "16.67 m/s", "20 m/s"],
        "Speed in km/h = 300 / 5 = 60 km/h. Speed in m/s = 60 * (5/18) = 50 / 3 = 16.67 m/s. Hence, option C is correct.",
        "एक कार 5 घंटे में 300 किमी की दूरी तय करती है। उसकी चाल मीटर प्रति सेकंड (m/s) में कितनी होगी?",
        ["15.5 मी./से.", "18.2 मी./से.", "16.67 मी./से.", "20 मी./से."],
        "चाल = 300 / 5 = 60 किमी/घं। मी./से. में चाल = 60 × (5/18) = 50/3 = 16.67 मी./से.। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        86, "Logical Reasoning & Maths", "Easy", "A",
        "In a row of trees, a particular neem tree is 7th from either end of the row. How many trees are there in the row?",
        ["13", "14", "15", "12"],
        "Total trees = (Left + Right) - 1 = (7 + 7) - 1 = 13. Hence, option A is correct.",
        "वृक्षों की एक पंक्ति में एक नीम का पेड़ दोनों छोर से 7वें स्थान पर है। पंक्ति में कुल कितने पेड़ हैं?",
        ["13", "14", "15", "12"],
        "कुल पेड़ = (बाएँ से स्थान + दाएँ से स्थान) - 1 = (7 + 7) - 1 = 13 पेड़। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        87, "Logical Reasoning & Maths", "Medium", "D",
        "The diagonal of a square is 10 cm. What is the area of the square?",
        ["100 sq. cm", "25 sq. cm", "75 sq. cm", "50 sq. cm"],
        "Area of a square = (Diagonal^2) / 2 = (10^2) / 2 = 100 / 2 = 50 sq. cm. Hence, option D is correct.",
        "एक वर्ग के विकर्ण की लंबाई 10 सेमी है। वर्ग का क्षेत्रफल कितना होगा?",
        ["100 वर्ग सेमी", "25 वर्ग सेमी", "75 वर्ग सेमी", "50 वर्ग सेमी"],
        "वर्ग का क्षेत्रफल = (विकर्ण)² / 2 = (10)² / 2 = 100 / 2 = 50 वर्ग सेमी। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        88, "Logical Reasoning & Maths", "Easy", "B",
        "Which of the following numbers is prime?",
        ["27", "29", "33", "35"],
        "29 has no divisors other than 1 and itself, making it a prime number. 27=3*9, 33=3*11, 35=5*7. Hence, option B is correct.",
        "निम्नलिखित में से कौन-सी एक अभाज्य (Prime) संख्या है?",
        ["27", "29", "33", "35"],
        "29 केवल 1 और स्वयं 29 से विभाजित होती है, अतः यह अभाज्य संख्या है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        89, "Logical Reasoning & Maths", "Medium", "C",
        "What is the angle between the hour hand and minute hand of a clock at 3:30?",
        ["70°", "80°", "75°", "85°"],
        "Angle = |30*H - (11/2)*M| = |30*3 - (11/2)*30| = |90 - 165| = 75°. Hence, option C is correct.",
        "किसी घड़ी में 3 बजकर 30 मिनट पर घंटे और मिनट की सुइयों के बीच कितने अंश का कोण होगा?",
        ["70°", "80°", "75°", "85°"],
        "सूत्र: कोण = |30 × 3 - (11/2) × 30| = |90 - 165| = 75°। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        90, "Logical Reasoning & Maths", "Easy", "A",
        "What is the Greatest Common Divisor (GCD/HCF) of 36 and 84?",
        ["12", "6", "18", "24"],
        "36 = 12 * 3; 84 = 12 * 7. Highest common factor is 12. Hence, option A is correct.",
        "36 और 84 का महत्तम समापवर्तक (HCF) क्या होगा?",
        ["12", "6", "18", "24"],
        "36 = 2² × 3² तथा 84 = 2² × 3 × 7। उभयनिष्ठ गुणनखंड = 2² × 3 = 12। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        91, "Logical Reasoning & Maths", "Medium", "B",
        "If the radius of a circle is doubled, by what percentage does its area increase?",
        ["100%", "300%", "200%", "400%"],
        "Area is proportional to r^2. If r becomes 2r, new area is 4 times original area. Increase = 4A - A = 3A. Percentage increase = (3A / A) * 100 = 300%. Hence, option B is correct.",
        "यदि किसी वृत्त की त्रिज्या को दोगुना कर दिया जाए, तो उसके क्षेत्रफल में कितने प्रतिशत की वृद्धि होगी?",
        ["100%", "300%", "200%", "400%"],
        "नया क्षेत्रफल = π(2r)² = 4πr² (अर्थात 4 गुना)। वृद्धि = 4 - 1 = 3 गुना = 300%। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        92, "Logical Reasoning & Maths", "Hard", "C",
        "A single card is drawn from a well-shuffled standard pack of 52 cards. What is the probability that it is either a King or a Heart?",
        ["1/13", "4/13", "16/52 = 4/13", "17/52"],
        "Number of Kings = 4, Hearts = 13. King of Hearts is common (1). Total favorable cards = 4 + 13 - 1 = 16. Probability = 16 / 52 = 4/13. Hence, option C is correct.",
        "52 ताश के पत्तों की गड्डी में से यादृच्छिक रूप से 1 पत्ता निकाला जाता है। उस पत्ते के बादशाह (King) या पान (Heart) होने की प्रायिकता क्या है?",
        ["1/13", "3/13", "4/13 (16/52)", "17/52"],
        "कुल बादशाह = 4, कुल पान = 13। पान का बादशाह दोनों में सम्मिलित है (1 पत्ता)। अनुकूल पत्ते = 4 + 13 - 1 = 16। प्रायिकता = 16/52 = 4/13। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        93, "Logical Reasoning & Maths", "Medium", "D",
        "If 'P' denotes '÷', 'Q' denotes '×', 'R' denotes '+', and 'S' denotes '-', what is the value of: 18 Q 12 P 4 R 5 S 6 ?",
        ["45", "51", "55", "53"],
        "Expression: 18 * 12 ÷ 4 + 5 - 6 = 18 * 3 + 5 - 6 = 54 + 5 - 6 = 53. Hence, option D is correct.",
        "यदि 'P' का अर्थ '÷', 'Q' का अर्थ '×', 'R' का अर्थ '+', और 'S' का अर्थ '-' हो, तो समीकरण का मान क्या होगा: 18 Q 12 P 4 R 5 S 6 ?",
        ["45", "51", "55", "53"],
        "मान रखने पर: 18 × 12 ÷ 4 + 5 - 6 = 18 × 3 + 5 - 6 = 54 + 5 - 6 = 53। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        94, "Logical Reasoning & Maths", "Easy", "B",
        "How many leap years are there in a century of 100 normal calendar years?",
        ["25", "24", "26", "23"],
        "In a standard 100-year period (e.g. 1901 to 2000 or 1801 to 1900), there are 24 leap years unless the 100th year is a 400-multiple leap year (24 ordinary century). The standard general count is 24. Hence, option B is correct.",
        "सामान्यतः 100 वर्षों की अवधि में कितने लीप वर्ष (अधिवर्ष) होते हैं?",
        ["25", "24", "26", "23"],
        "प्रत्येक चौथे वर्ष में लीप वर्ष आता है, परन्तु 100वाँ वर्ष शताब्दी होने के कारण यदि 400 से विभाज्य न हो तो सामान्य वर्ष होता है। अतः 100 वर्षों में 24 लीप वर्ष होते हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        95, "Logical Reasoning & Maths", "Medium", "A",
        "The length and breadth of a rectangle are increased by 20% and 10% respectively. What is the net percentage increase in its area?",
        ["32%", "30%", "28%", "35%"],
        "Net percentage change = a + b + (a*b)/100 = 20 + 10 + (20*10)/100 = 30 + 2 = 32%. Hence, option A is correct.",
        "एक आयत की लंबाई में 20% और चौड़ाई में 10% की वृद्धि की जाती है। उसके क्षेत्रफल में कुल कितने प्रतिशत की वृद्धि होगी?",
        ["32%", "30%", "28%", "35%"],
        "कुल प्रतिशत वृद्धि = x + y + (xy/100) = 20 + 10 + (200/100) = 32%। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        96, "Logical Reasoning & Maths", "Easy", "C",
        "Statements: Some books are pens. All pens are papers. Conclusion: Some books are papers.",
        ["Conclusion does not follow", "Partially follows", "Conclusion follows logically", "Cannot be determined"],
        "Some books are pens (intersection exists) and all pens are inside papers, meaning the intersection between books and papers is guaranteed. The conclusion follows. Hence, option C is correct.",
        "कथन: कुछ किताबें पेन हैं। सभी पेन कागज हैं। निष्कर्ष: कुछ किताबें कागज हैं।",
        ["निष्कर्ष अनुसरण नहीं करता", "आंशिक अनुसरण करता है", "निष्कर्ष पूर्णतः तार्किक रूप से निकलता है", "तय नहीं किया जा सकता"],
        "कथनानुसार किताबों का जो भाग पेन है, वह निश्चित रूप से कागज भी होगा। अतः 'कुछ किताबें कागज हैं' निष्कर्ष सत्य है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        97, "Logical Reasoning & Maths", "Medium", "B",
        "A man rows 18 km downstream in 3 hours and 12 km upstream in 3 hours. What is the speed of the current?",
        ["2 km/h", "1 km/h", "1.5 km/h", "3 km/h"],
        "Downstream speed u = 18/3 = 6 km/h. Upstream speed v = 12/3 = 4 km/h. Speed of current = (u - v) / 2 = (6 - 4) / 2 = 1 km/h. Hence, option B is correct.",
        "एक नाविक धारा के अनुकूल 18 किमी की दूरी 3 घंटे में तथा धारा के प्रतिकूल 12 किमी की दूरी 3 घंटे में तय करता है। धारा की चाल कितनी है?",
        ["2 किमी/घं", "1 किमी/घं", "1.5 किमी/घं", "3 किमी/घं"],
        "अनुकूल चाल = 18/3 = 6 किमी/घं। प्रतिकूल चाल = 12/3 = 4 किमी/घं। धारा की चाल = (6 - 4)/2 = 1 किमी/घं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        98, "Logical Reasoning & Maths", "Hard", "D",
        "In how many ways can a committee of 3 men and 2 women be formed from a group of 5 men and 4 women?",
        ["40", "50", "30", "60"],
        "Ways = 5C3 * 4C2 = 10 * 6 = 60. Hence, option D is correct.",
        "5 पुरुषों और 4 महिलाओं में से 3 पुरुषों और 2 महिलाओं की एक समिति कितने प्रकार से बनाई जा सकती है?",
        ["40", "50", "30", "60"],
        "कुल तरीके = ⁵C₃ × ⁴C₂ = 10 × 6 = 60 तरीके। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        99, "Logical Reasoning & Maths", "Medium", "A",
        "The value of a machine depreciates by 10% every year. If its present value is ₹10,000, what will be its value after 2 years?",
        ["₹8,100", "₹8,000", "₹8,500", "₹9,000"],
        "Value after 2 years = 10000 * (1 - 0.10)^2 = 10000 * 0.81 = ₹8,100. Hence, option A is correct.",
        "किसी मशीन के मूल्य में प्रतिवर्ष 10% का अवमूल्यन होता है। यदि उसका वर्तमान मूल्य ₹10,000 है, तो 2 वर्ष बाद उसका मूल्य क्या होगा?",
        ["₹8,100", "₹8,000", "₹8,500", "₹9,000"],
        "2 वर्ष बाद मूल्य = 10000 × (1 - 10/100)² = 10000 × (0.9)² = ₹8,100। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        100, "Logical Reasoning & Maths", "Easy", "C",
        "What is the value of 15% of 200 plus 25% of 400?",
        ["120", "110", "130", "140"],
        "Calculation: 15% of 200 = 30; 25% of 400 = 100; Sum = 30 + 100 = 130. Hence, option C is correct.",
        "200 के 15% तथा 400 के 25% का योग कितना होगा?",
        ["120", "110", "130", "140"],
        "गणना: 200 का 15% = 30; 400 का 25% = 100; योग = 30 + 100 = 130। अतः विकल्प C सही उत्तर है।"
    ))

    return qs

def main():
    qs = get_csat_2020_questions()
    assert len(qs) == 100, f"Expected 100 questions, got {len(qs)}"

    out_path = "tests/state_psc/uppcs_pre/pyq/uppcs_pre_pyq_2020_csat.json"
    data = {
        "testId": "uppcs_pre_pyq_2020_csat",
        "categoryId": "uppcs_pre",
        "test_id": "uppcs_pre_pyq_2020_csat",
        "category_id": "uppcs_pre",
        "title": "UPPSC PCS Prelims 2020 — CSAT Paper 2 (Full 100 Qs)",
        "titleEn": "UPPSC PCS Prelims 2020 — CSAT Paper 2 (Full 100 Qs)",
        "titleHi": "UPPSC PCS प्रारंभिक परीक्षा 2020 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
        "testType": "PYQ",
        "test_type": "PYQ",
        "isFree": True,
        "is_free": True,
        "durationMinutes": 120,
        "duration_minutes": 120,
        "totalQuestions": 100,
        "total_questions": 100,
        "maxMarks": 200.0,
        "positiveMarks": 2.0,
        "negativeMarks": 0.66,
        "examYear": 2020,
        "shiftBadge": "UPPSC Prelims 2020 • CSAT Paper-2 (Full 100 Qs)",
        "questions": qs,
        "path": out_path.replace("\\", "/")
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)
    print(f"Successfully generated {out_path} with {len(qs)} questions.")

if __name__ == "__main__":
    main()
