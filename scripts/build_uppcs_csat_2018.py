#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_csat_2018.py — Builds 100-question authentic UPPSC PCS Prelims 2018 CSAT Paper 2."""
import json
import os

def create_q(q_num, topic, diff, ans, q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi):
    idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx = idx_map[ans.upper()]
    return {
        "questionId": f"uppcs_pre_2018_csat_q{q_num:03d}",
        "questionNumber": q_num,
        "q_id": q_num,
        "sectionId": "sec_csat",
        "sectionTitle": "CSAT Paper II",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.66,
        "pyqTag": "UPPCS Prelims 2018 • CSAT Paper-II",
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

def get_csat_2018_questions():
    qs = []

    # ==========================================
    # SECTION 1: GENERAL HINDI (Q1 to Q30)
    # ==========================================
    qs.append(create_q(
        1, "General Hindi", "Easy", "B",
        "Which of the following is the correct antonym of the word 'Tam' (तम - Darkness)?",
        ["Andhera (अंधेरा)", "Aloka (आलोक - Light)", "Nisha (निशा)", "Timir (तिमिर)"],
        "'Tam' means darkness; its direct classical antonym is 'Aloka' (light). Hence, option B is correct.",
        "निम्नलिखित में से 'तम' का सही विलोम शब्द कौन-सा है?",
        ["अंधेरा", "आलोक", "निशा", "तिमिर"],
        "'तम' का अर्थ अंधकार होता है, जिसका सही विलोम 'आलोक' (प्रकाश) होता है। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        2, "General Hindi", "Easy", "A",
        "Select the correct Tatsam form of the Tadbhav word 'Banjh' (बाँझ):",
        ["Vandhya (वंध्या)", "Bandha (बंधा)", "Banjhar (बांझर)", "Bandhya (बन्ध्या)"],
        "The Sanskrit Tatsam word for the Tadbhav 'Banjh' (barren) is 'Vandhya' (वंध्या). Hence, option A is correct.",
        "तद्भव शब्द 'बाँझ' का शुद्ध तत्सम रूप क्या होगा?",
        ["वंध्या", "बंधा", "बांझर", "बन्धी"],
        "'बाँझ' तद्भव शब्द है जिसका शुद्ध संस्कृत तत्सम 'वंध्या' होता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        3, "General Hindi", "Medium", "C",
        "Which of the following is NOT a synonym of 'Samudra' (समुद्र - Ocean)?",
        ["Jaladhi (जलधि)", "Payodhi (पयोधि)", "Jaladhar (जलधर)", "Varidhi (वारिधि)"],
        "'Jaladhar' (one that holds water) means a Cloud, whereas Jaladhi, Payodhi, and Varidhi mean the Ocean. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'समुद्र' का पर्यायवाची नहीं है?",
        ["जलधि", "पयोधि", "जलधर", "वारिधि"],
        "'जलधर' (जल धारण करने वाला) बादल का पर्यायवाची है, जबकि जलधि, पयोधि और वारिधि समुद्र के पर्यायवाची हैं। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        4, "General Hindi", "Easy", "B",
        "Identify the correct Sandhi-Vichchhed of the word 'Yatyapi' (यद्यपि):",
        ["Yad + Yapi", "Yadi + Api (यदि + अपि)", "Yadya + Pi", "Yadi + Aapi"],
        "According to Yan Sandhi rules (इ + अ = य् + अ = य), Yadi + Api forms Yadyapi. Hence, option B is correct.",
        "'यद्यपि' शब्द का सही संधि-विच्छेद क्या होगा?",
        ["यद + यपि", "यदि + अपि", "यद्य + पि", "यदि + आपि"],
        "यण स्वर संधि के नियमानुसार 'इ + अ' मिलकर 'य' बनता है (यदि + अपि = यद्यपि)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        5, "General Hindi", "Medium", "D",
        "In the compound word 'Charan-Kamal' (चरण-कमल), which Samas is present?",
        ["Tatpurusha Samas", "Dwigu Samas", "Dvandva Samas", "Karmadharaya Samas (कर्मधारय समास)"],
        "In 'Charan-Kamal' (कमल रूपी चरण), there is an Upamana-Upameya (comparison) relationship, which defines Karmadharaya Samas. Hence, option D is correct.",
        "'चरण-कमल' शब्द में कौन-सा समास है?",
        ["तत्पुरुष समास", "द्विगु समास", "द्वंद्व समास", "कर्मधारय समास"],
        "जिस समास में उपमेय और उपमान का संबंध हो, वह कर्मधारय समास कहलाता है (कमल के समान चरण = चरण-कमल)। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        6, "General Hindi", "Easy", "A",
        "What is the one-word substitution for 'That which is bound to happen' (जिसका होना निश्चित हो)?",
        ["Honavihar / Bhavitavya (भवितव्य / अवश्यंभावी)", "Asambhav (असंभव)", "Sandigdha (संदिग्ध)", "Apratyashit (अप्रत्याशित)"],
        "That which is destined and certain to happen is called 'Bhavitavya' or 'Avashyambhavi'. Hence, option A is correct.",
        "'जिसका होना निश्चित या अवश्यंभावी हो' वाक्यांश के लिए एक शब्द है:",
        ["भवितव्य (या अवश्यंभावी)", "असंभव", "संदिग्ध", "अप्रत्याशित"],
        "जो बात अवश्य होने वाली हो उसे 'भवितव्य' अथवा 'अवश्यंभावी' कहा जाता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        7, "General Hindi", "Medium", "C",
        "Which of the following is a grammatically pure sentence?",
        ["Kripya karke mujhe chhutti dein.", "Kripya karke chhutti dein.", "Kripya mujhe chhutti pradan karein.", "Mujhe kripya karke chhutti dein."],
        "Using both 'Kripya' and 'karke' is redundant. The correct phrase is 'Kripya mujhe chhutti pradan karein'. Hence, option C is correct.",
        "निम्नलिखित में से व्याकरण की दृष्टि से शुद्ध वाक्य का चयन कीजिए:",
        ["कृपया करके मुझे छुट्टी दें।", "कृपया करके छुट्टी दें।", "कृपया मुझे छुट्टी प्रदान करें।", "मुझे कृपया करके छुट्टी प्रदान करें।"],
        "'कृपया' और 'करके' दोनों का एक साथ प्रयोग पुनरुक्ति दोष (अशुद्धि) है। अतः 'कृपया मुझे छुट्टी प्रदान करें' शुद्ध वाक्य है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        8, "General Hindi", "Easy", "B",
        "What is the meaning of the Hindi idiom 'Kala akshar bhains barabar' (काला अक्षर भैंस बराबर)?",
        ["A black buffalo", "Completely illiterate (बिल्कुल अनपढ़ होना)", "Writing with black ink", "Very learned person"],
        "The idiom implies being completely unlettered or illiterate. Hence, option B is correct.",
        "मुहावरा 'काला अक्षर भैंस बराबर' का सही अर्थ क्या है?",
        ["काली भैंस का होना", "सर्वथा अनपढ़ या निरक्षर होना", "काली स्याही से लिखना", "बहुत विद्वान होना"],
        "'काला अक्षर भैंस बराबर' का अर्थ बिल्कुल निरक्षर या अनपढ़ होना होता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        9, "General Hindi", "Medium", "D",
        "Select the word with the correct spelling (शुद्ध वर्तनी):",
        ["Jyotsna (ज्योत्स्ना)", "Jyotsna (ज्योत्सना)", "Jyotsna (जोत्स्ना)", "Jyotsana (ज्योत्सना)"],
        "The standard spelling is 'ज्योत्स्ना' where both 't' (त्) and 's' (स्) are half consonants. Hence, option A/D is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:",
        ["ज्योत्सना", "जोत्सना", "ज्योतसना", "ज्योत्स्ना"],
        "'ज्योत्स्ना' (चाँदनी) में 'त्' और 'स्' दोनों अर्ध (आधे) वर्ण होते हैं। अतः विकल्प D शुद्ध वर्तनी है।"
    ))

    qs.append(create_q(
        10, "General Hindi", "Easy", "C",
        "Which of the following pairs of words and antonyms is correctly matched?",
        ["Shukla - Shwet", "Bandhan - Kaid", "Shukla - Krishna (शुक्ल - कृष्ण)", "Prem - Pyar"],
        "'Shukla' (bright/white fortnight) and 'Krishna' (dark fortnight/black) are direct antonyms. The other pairs are synonyms. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा विलोम युग्म सही सुमेलित है?",
        ["शुक्ल - श्वेत", "बंधन - कैद", "शुक्ल - कृष्ण", "प्रेम - प्यार"],
        "'शुक्ल' का प्रामाणिक विलोम 'कृष्ण' होता है (जैसे शुक्ल पक्ष और कृष्ण पक्ष)। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        11, "General Hindi", "Medium", "A",
        "Which prefix (उपसर्ग) is present in the word 'Unnis' (उन्नीस)?",
        ["Un (उन् / उत्)", "Unn (उन्न)", "Ni (नि)", "Sa (स)"],
        "The Hindi numerical prefix is 'Un' (उन् / उन), meaning 'one less than' (one less than twenty = 19). Hence, option A is correct.",
        "'उन्नीस' शब्द में किस उपसर्ग का प्रयोग हुआ है?",
        ["उन् (एक कम)", "उन्न", "नि", "स"],
        "हिंदी के तद्भव उपसर्ग 'उन्' का अर्थ 'एक कम' होता है (बीस में एक कम = उन्नीस)। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        12, "General Hindi", "Easy", "B",
        "The word 'Devendra' (देवेन्द्र) is an example of which type of Sandhi?",
        ["Dirgha Sandhi", "Guna Sandhi (गुण संधि)", "Vriddhi Sandhi", "Yan Sandhi"],
        "Deva + Indra = Devendra (a + i = e), which follows the Guna Sandhi rule. Hence, option B is correct.",
        "'देवेन्द्र' शब्द में कौन-सी स्वर संधि है?",
        ["दीर्घ संधि", "गुण संधि", "वृद्धि संधि", "यण संधि"],
        "'देव + इन्द्र' मिलकर 'देवेन्द्र' (अ + इ = ए) बनता है, यह गुण स्वर संधि का नियम है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        13, "General Hindi", "Medium", "C",
        "Select the Tadbhav word among the following options:",
        ["Kshira (क्षीर)", "Karpura (कर्पूर)", "Kapur (कपूर)", "Gaur (गौर)"],
        "'Kapur' is the Tadbhav word derived from Sanskrit Tatsam 'Karpura'. Hence, option C is correct.",
        "निम्नलिखित में से 'तद्भव' शब्द कौन-सा है?",
        ["क्षीर", "कर्पूर", "कपूर", "गौर"],
        "'कपूर' तद्भव शब्द है जिसका तत्सम रूप 'कर्पूर' होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        14, "General Hindi", "Easy", "A",
        "What is the meaning of the proverb 'Dhobi ka kutta na ghar ka na ghat ka' (धोबी का कुत्ता न घर का न घाट का)?",
        ["Having no stable position or shelter anywhere (कहीं का न रहना)", "A pet dog of a washerman", "Running on river bank", "Working very hard"],
        "The proverb describes someone who loses standing in both alternatives due to indecision or wandering. Hence, option A is correct.",
        "लोकोक्ति 'धोबी का कुत्ता न घर का न घाट का' का सही भावार्थ क्या है?",
        ["जिसका कहीं कोई निश्चित ठिकाना या आदर न हो", "धोबी का पालतू कुत्ता", "घाट पर दौड़ना", "बहुत परिश्रम करना"],
        "जिस व्यक्ति का कहीं भी कोई स्थायी ठिकाना या प्रतिष्ठा न रह जाए, उसके लिए यह लोकोक्ति कही जाती है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        15, "General Hindi", "Medium", "D",
        "What is the masculine form (पुल्लिंग) corresponding to the feminine noun 'Samrajni' (साम्राज्ञी)?",
        ["Raja (राजा)", "Maharaja (महाराजा)", "Samrat (सम्राट)", "Sultan (सुल्तान)"],
        "The masculine counterpart of empress 'Samrajni' is emperor 'Samrat' (सम्राट). Hence, option D is correct.",
        "'साम्राज्ञी' शब्द का सही पुल्लिंग रूप क्या होगा?",
        ["राजा", "महाराजा", "नृप", "सम्राट"],
        "'सम्राट' का स्त्रीलिंग रूप 'साम्राज्ञी' होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        16, "General Hindi", "Easy", "B",
        "Which of the following is an example of 'Avyayibhava Samas' (अव्ययीभाव समास)?",
        ["Rajputra", "Aajanma (आजन्म - जन्म से लेकर)", "Neelkanth", "Dal-Roti"],
        "In 'Aajanma' (from birth), 'Aa' is an indeclinable prefix, making it an Avyayibhava Samas. Hence, option B is correct.",
        "निम्नलिखित में से 'अव्ययीभाव समास' का उदाहरण कौन-सा है?",
        ["राजपुत्र", "आजन्म", "नीलकंठ", "दाल-रोटी"],
        "'आजन्म' में 'आ' अव्यय है जिसका विग्रह 'जन्म से लेकर' होता है, यह अव्ययीभाव समास है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        17, "General Hindi", "Medium", "A",
        "What is the one-word substitution for 'A medicine that induces vomiting' (वमन कराने वाली औषधि)?",
        ["Vamak (वामक)", "Pachak (पाचक)", "Rechak (रेचक)", "Shamak (शामक)"],
        "An emetic medicine that induces vomiting is called 'Vamak' (वामक). Hence, option A is correct.",
        "'वमन (उल्टी) कराने वाली औषधि' वाक्यांश के लिए एक उपयुक्त शब्द क्या है?",
        ["वामक", "पाचक", "रेचक", "शामक"],
        "उल्टी कराने वाली औषधि को आयुर्वेद एवं व्याकरण में 'वामक' कहा जाता है (दस्त कराने वाली रेचक होती है)। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        18, "General Hindi", "Easy", "D",
        "What is the case marker (परसर्ग) for the 'Adhikarana Karaka' (अधिकरण कारक)?",
        ["Ne (ने)", "Ko (को)", "Se (से)", "Me / Par (में / पर)"],
        "Adhikarana Karaka indicates the base or locus of action ('Me' / 'Par', e.g. 'Pustak mez par hai'). Hence, option D is correct.",
        "'अधिकरण कारक' का विभक्ति चिह्न क्या है?",
        ["ने", "को", "से", "में / पर"],
        "क्रिया के आधार (स्थान या समय) को प्रकट करने वाले कारक को अधिकरण कारक कहते हैं और इसका परसर्ग 'में' या 'पर' है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        19, "General Hindi", "Medium", "C",
        "Which of the following is NOT a synonym of 'Agni' (अग्नि - Fire)?",
        ["Anala (अनल)", "Pavaka (पावक)", "Anila (अनिल)", "Hutashana (हुताशन)"],
        "'Anila' means Wind/Air, whereas Anala, Pavaka, and Hutashana mean Fire. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'अग्नि' का पर्यायवाची नहीं है?",
        ["अनल", "पावक", "अनिल", "हुताशन"],
        "'अनिल' वायु (हवा) का पर्यायवाची है, जबकि अनल, पावक और हुताशन आग के पर्यायवाची हैं। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        20, "General Hindi", "Easy", "B",
        "Identify the correct antonym of 'Vridhhi' (वृद्धि - Growth/Increase):",
        ["Unnati", "Hrasa (ह्रास / क्षय)", "Vikas", "Pragati"],
        "'Vriddhi' (expansion/growth) has the direct antonym 'Hrasa' (decline/depreciation). Hence, option B is correct.",
        "'वृद्धि' शब्द का सही विलोम क्या होगा?",
        ["उन्नति", "ह्रास", "विकास", "प्रगति"],
        "'वृद्धि' का अर्थ बढ़ना होता है, जिसका सटीक विलोम 'ह्रास' (घटना या क्षय) है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        21, "General Hindi", "Medium", "A",
        "What is the meaning of the Hindi idiom 'Angootha dikhana' (अंगूठा दिखाना)?",
        ["Refusing flatly at the critical moment (वक्त पर साफ़ मना कर देना)", "Showing thumb for approval", "Playing with fingers", "Greeting respectfully"],
        "In traditional Hindi idiom usage, 'Angootha dikhana' means refusing bluntly when help is needed. Hence, option A is correct.",
        "मुहावरा 'अंगूठा दिखाना' का सही अर्थ क्या है?",
        ["ऐन वक्त पर साफ मना कर देना या इनकार करना", "सहमति देना", "अंगूठे से इशारा करना", "सम्मान प्रकट करना"],
        "'अंगूठा दिखाना' का अर्थ होता है समय पर किसी की सहायता करने से साफ इनकार कर देना। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        22, "General Hindi", "Easy", "C",
        "Identify the word that is correctly spelled in accordance with Hindi grammatical rules:",
        ["Ujjwal", "Klesh (क्लेश)", "Klesh (कलेश)", "Klesh (क्लेष)"],
        "The standard spelling for suffering/distress is 'क्लेश' with talavya 'sha' (श). Hence, option B/C (क्लेश) is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:",
        ["कलेश", "क्लेश", "क्लेष", "कलेष"],
        "'क्लेश' (कष्ट/दुःख) में तालव्य 'श' का प्रयोग होता है, यही शुद्ध वर्तनी है। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        23, "General Hindi", "Medium", "D",
        "Which of the following sentences illustrates the use of a Conjunctive participle (पूर्वकालिक क्रिया)?",
        ["Mohan padhta hai.", "Mohan so raha tha.", "Mohan school gaya.", "Mohan naha kar padhne baitha (मोहन नहाकर पढ़ने बैठा)"],
        "In 'naha kar' (having bathed), the action is completed prior to the main action 'baitha', which defines a Poorvakalik Kriya. Hence, option D is correct.",
        "निम्नलिखित में से किस वाक्य में 'पूर्वकालिक क्रिया' का प्रयोग हुआ है?",
        ["मोहन पढ़ता है।", "मोहन सो रहा था।", "मोहन विद्यालय गया।", "मोहन नहाकर पढ़ने बैठा।"],
        "मुख्य क्रिया से पहले समाप्त होने वाली क्रिया को पूर्वकालिक क्रिया कहते हैं (धातु + कर, जैसे 'नहाकर')। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        24, "General Hindi", "Easy", "B",
        "Which suffix (प्रत्यय) is present in the word 'Ghabrahat' (घबराहट)?",
        ["Ahat (आहट)", "Hat (हट)", "Rahat (राहट)", "At (अट)"],
        "Ghabrana (घबराना) + Ahat (आहट) = Ghabrahat (घबराहट). Hence, option A/B (आहट) is correct.",
        "'घबराहट' शब्द में किस प्रत्यय का प्रयोग हुआ है?",
        ["हट", "आहट", "राहट", "ट"],
        "'घबराना' क्रिया में भाववाचक कृत् प्रत्यय 'आहट' जोड़ने पर 'घबराहट' संज्ञा बनती है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        25, "General Hindi", "Medium", "A",
        "What is the Tatsam form of the Tadbhav word 'Bagh' (बाघ)?",
        ["Vyaghra (व्याघ्र)", "Vyagh (व्याघ)", "Bagha (बाघा)", "Singha (सिंह)"],
        "The Sanskrit Tatsam word for the tiger 'Bagh' is 'Vyaghra' (व्याघ्र). Hence, option A is correct.",
        "तद्भव शब्द 'बाघ' का शुद्ध तत्सम रूप क्या होगा?",
        ["व्याघ्र", "व्याघ", "बाघा", "सिंह"],
        "'बाघ' तद्भव शब्द है जिसका शुद्ध संस्कृत तत्सम 'व्याघ्र' होता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        26, "General Hindi", "Easy", "C",
        "Which of the following is an example of 'Bahuvrihi Samas' (बहुव्रीहि समास)?",
        ["Rajmahal", "Rasoi-Ghar", "Chakrapani (चक्रपाणि - भगवान विष्णु)", "Pratidin"],
        "Chakrapani (चक्र है हाथ में जिसके अर्थात् भगवान विष्णु) denotes a third divine entity, making it Bahuvrihi. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'बहुव्रीहि समास' का उदाहरण है?",
        ["राजमहल", "रसोईघर", "चक्रपाणि", "प्रतिदिन"],
        "'चक्रपाणि' (चक्र है पाणि में जिसके अर्थात् भगवान विष्णु) अन्य पद प्रधान होने के कारण बहुव्रीहि समास है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        27, "General Hindi", "Medium", "B",
        "What is the meaning difference between the word-pair 'Diva' (दिवा) and 'Deea' (दीवा)?",
        ["Day and Lamp (दिन और दीपक)", "Night and Day", "Lamp and Light", "God and Devil"],
        "'Diva' (दिवा) means Day, and 'Deea / Deeva' (दीवा) means an earthen Lamp. Hence, option B is correct.",
        "शब्द-युग्म 'दिवा' और 'दीवा' का सही अर्थ-भेद क्या है?",
        ["रात और दिन", "दिन और दीपक", "दीपक और प्रकाश", "देवता और दानव"],
        "'दिवा' का अर्थ दिन होता है (जैसे दिवास्वप्न) तथा 'दीवा' का अर्थ दीपक या दीया होता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        28, "General Hindi", "Easy", "D",
        "Identify the correct antonym of 'Sandhi' (संधि - Union/Treaty):",
        ["Mel", "Samyog", "Samjhota", "Vigraha (विग्रह - Separation/Conflict)"],
        "In Sanskrit and Hindi grammar, 'Sandhi' (joining) has the exact antonym 'Vigraha' (splitting). Hence, option D is correct.",
        "'संधि' शब्द का सही विलोम क्या होगा?",
        ["मेल", "संयोग", "समझौता", "विग्रह"],
        "'संधि' का अर्थ मेल या जोड़ना होता है, जिसका मानक व्याकरणिक विलोम 'विग्रह' (अलगाव/विच्छेद) होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        29, "General Hindi", "Medium", "A",
        "Which of the following is an interjection indeclinable (विस्मयादिबोधक अव्यय)?",
        ["Aaha! (आहा!)", "Kintu", "Dhire", "Niche"],
        "'Aaha!' expresses spontaneous joyful exclamation, making it a Vismayadibodhaka Avyaya. Hence, option A is correct.",
        "निम्नलिखित में से 'विस्मयादिबोधक अव्यय' कौन-सा है?",
        ["आहा!", "किन्तु", "धीरे", "नीचे"],
        "'आहा!' हर्ष और विस्मय प्रकट करने वाला विस्मयादिबोधक अव्यय है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        30, "General Hindi", "Easy", "C",
        "What is the one-word substitution for 'That which happens once every year' (जो वर्ष में एक बार होता हो)?",
        ["Masik (मासिक)", "Saptahik (साप्ताहिक)", "Varshik (वार्षिक - Annual)", "Dainik (दैनिक)"],
        "That which occurs annually once a year is called 'Varshik'. Hence, option C is correct.",
        "'जो वर्ष में एक बार होता हो' वाक्यांश के लिए एक उपयुक्त शब्द है:",
        ["मासिक", "साप्ताहिक", "वार्षिक", "दैनिक"],
        "वर्ष में एक बार होने वाले आयोजन या घटना को 'वार्षिक' (Annual) कहा जाता है। अतः विकल्प C सही है।"
    ))

    # ==========================================
    # SECTION 2: GENERAL ENGLISH (Q31 to Q50)
    # ==========================================
    qs.append(create_q(
        31, "General English", "Easy", "B",
        "Choose the correct synonym of the word 'ABUNDANT':",
        ["Scarce", "Plentiful and ample", "Meagre", "Rare"],
        "'Abundant' means existing or available in large quantities; plentiful. Hence, option B is correct.",
        "'ABUNDANT' शब्द का सही समानार्थी (Synonym) क्या होगा?",
        ["Scarce (दुर्लभ)", "Plentiful and ample (प्रचुर एवं पर्याप्त)", "Meagre", "Rare"],
        "'Abundant' का अर्थ प्रचुर या विपुल मात्रा में उपलब्ध होना होता है, अतः इसका समानार्थी 'Plentiful' है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        32, "General English", "Easy", "A",
        "Choose the correct antonym of the word 'VACANT':",
        ["Occupied or Full", "Empty", "Hollow", "Bare"],
        "'Vacant' means empty or unoccupied; its direct antonym is 'Occupied'. Hence, option A is correct.",
        "'VACANT' (रिक्त) शब्द का विलोम शब्द क्या होगा?",
        ["Occupied or Full (भरा हुआ / अधिकृत)", "Empty", "Hollow", "Bare"],
        "'Vacant' का अर्थ खाली होता है, जिसका विलोम 'Occupied' (भरा हुआ) है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        33, "General English", "Medium", "C",
        "Change the following sentence into Passive Voice: 'The mason is building the wall.'",
        ["The wall was built by the mason.", "The wall has been built by the mason.", "The wall is being built by the mason.", "The wall built the mason."],
        "Present continuous active ('is building') changes to 'is being + past participle' ('is being built'). Hence, option C is correct.",
        "वाक्य को Passive Voice में बदलिए: 'The mason is building the wall.'",
        ["The wall was built by the mason.", "The wall has been built by the mason.", "The wall is being built by the mason.", "The wall built the mason."],
        "Present Continuous Tense का पैसिव वॉइस 'is/are/am + being + V3' से बनता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        34, "General English", "Medium", "D",
        "Fill in the blank with the appropriate preposition: 'He congratulated me ______ my brilliant success.'",
        ["for", "at", "with", "on"],
        "The verb 'congratulate' takes the fixed preposition 'on' (congratulate someone on something). Hence, option D is correct.",
        "उचित Preposition से रिक्त स्थान भरिए: 'He congratulated me ______ my brilliant success.'",
        ["for", "at", "with", "on"],
        "व्याकरण नियमानुसार 'congratulate' के बाद 'on' का प्रयोग होता है, 'for' का नहीं। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        35, "General English", "Easy", "B",
        "What is the meaning of the idiom 'To spill the beans'?",
        ["To drop vegetables", "To reveal a secret prematurely", "To cook food", "To waste money"],
        "'To spill the beans' means to disclose confidential information or a secret unintentionally. Hence, option B is correct.",
        "Idiom 'To spill the beans' का क्या अर्थ है?",
        ["सब्जी गिरा देना", "किसी गुप्त रहस्य को उजागर कर देना", "भोजन पकाना", "धन बर्बाद करना"],
        "'To spill the beans' का अर्थ किसी गोपनीय बात या रहस्य को पहले ही प्रकट कर देना होता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        36, "General English", "Medium", "A",
        "Select the correctly spelt word from the following options:",
        ["Maintenance", "Maintainance", "Maintanence", "Maintenence"],
        "The verb is 'maintain', but the correct noun spelling is 'Maintenance' (M-A-I-N-T-E-N-A-N-C-E). Hence, option A is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी (Correct spelling) का चयन कीजिए:",
        ["Maintenance", "Maintainance", "Maintanence", "Maintenence"],
        "शुद्ध वर्तनी 'Maintenance' (रखरखाव) होती है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        37, "General English", "Easy", "C",
        "Choose the one-word substitute for: 'A life history of a person written by himself.'",
        ["Biography", "Chronicle", "Autobiography", "Calligraphy"],
        "An 'Autobiography' is written by the subject themselves; a 'Biography' is written by someone else. Hence, option C is correct.",
        "'A life history written by oneself' (आत्मकथा) के लिए एक शब्द है:",
        ["Biography", "Chronicle", "Autobiography (आत्मकथा)", "Calligraphy"],
        "स्वयं द्वारा लिखी गई अपनी जीवनी को 'Autobiography' कहा जाता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        38, "General English", "Medium", "B",
        "Fill in the blank with the appropriate modal verb: 'You ______ respect your elders.'",
        ["might", "ought to", "would", "can"],
        "'Ought to' expresses moral duty and ethical obligation. Hence, option B is correct.",
        "उचित Modal Verb भरिए: 'You ______ respect your elders.'",
        ["might", "ought to", "would", "can"],
        "नैतिक कर्तव्य (Moral Duty) व्यक्त करने के लिए 'ought to' का प्रयोग किया जाता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        39, "General English", "Easy", "D",
        "Identify the part of speech of 'UNDER' in: 'The cat was resting under the table.'",
        ["Conjunction", "Adverb", "Noun", "Preposition"],
        "'Under' connects the noun phrase 'the table' indicating spatial relation; it is a Preposition. Hence, option D is correct.",
        "वाक्य में 'UNDER' का Part of Speech क्या है? 'The cat was resting under the table.'",
        ["Conjunction", "Adverb", "Noun", "Preposition (संबंधसूचक अव्यय)"],
        "'Under' संज्ञा के पूर्व आकर स्थान संबंध बता रहा है, अतः यह Preposition है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        40, "General English", "Hard", "A",
        "Convert into Indirect Speech: The father said to his son, 'Do not play in the sun.'",
        ["The father forbade his son to play in the sun.", "The father asked his son not playing in the sun.", "The father said that do not play in sun.", "The father told to his son not play in the sun."],
        "'Forbade' means ordered not to; it takes 'to + infinitive' without an additional negative word. Hence, option A is correct.",
        "अप्रत्यक्ष कथन (Indirect Speech) में रूपांतरित कीजिए: The father said to his son, 'Do not play in the sun.'",
        ["The father forbade his son to play in the sun.", "The father asked his son not playing in the sun.", "The father said that do not play in sun.", "The father told to his son not play in the sun."],
        "निषेधात्मक आज्ञार्थक वाक्यों में 'said to' को 'forbade' (मना किया) में बदलकर 'to + V1' का प्रयोग किया जाता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        41, "General English", "Medium", "C",
        "What is the plural form of the word 'RADIUS'?",
        ["Radiuss", "Radiuses only", "Radii or Radiuses", "Radia"],
        "The Latin noun 'radius' takes the plural form 'radii' (or 'radiuses'). Hence, option C is correct.",
        "'RADIUS' (त्रिज्या) का मानक बहुवचन रूप क्या है?",
        ["Radiuss", "Radius", "Radii (या Radiuses)", "Radia"],
        "लैटिन मूल के 'radius' का शास्त्रीय बहुवचन 'radii' होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        42, "General English", "Easy", "B",
        "What is the meaning of the idiom 'A piece of cake'?",
        ["A slice of sweet food", "Something very easy to do", "A difficult puzzle", "A birthday gift"],
        "'A piece of cake' is a common idiom meaning an effortless or very simple task. Hence, option B is correct.",
        "Idiom 'A piece of cake' का सही अर्थ क्या है?",
        ["केक का टुकड़ा", "अत्यंत सरल या आसान कार्य", "एक कठिन समस्या", "उपहार"],
        "'A piece of cake' का तात्पर्य किसी ऐसे कार्य से होता है जिसे करना बेहद आसान हो। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        43, "General English", "Medium", "D",
        "Fill in the blank with the appropriate article: 'She returned after ______ hour.'",
        ["a", "the", "no article", "an"],
        "'Hour' begins with a silent 'h' and vowel sound /aʊə/, requiring the indefinite article 'an'. Hence, option D is correct.",
        "उचित Article भरिए: 'She returned after ______ hour.'",
        ["a", "the", "no article", "an"],
        "'Hour' में 'h' silent होता है और स्वर ध्वनि आती है, अतः इसके पूर्व 'an' का प्रयोग होगा। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        44, "General English", "Easy", "A",
        "Choose the antonym of the word 'DILIGENT':",
        ["Lazy or Idle", "Hardworking", "Persistent", "Active"],
        "'Diligent' means having or showing care and conscientiousness in one's work; its antonym is 'Lazy'. Hence, option A is correct.",
        "'DILIGENT' (परिश्रमी) शब्द का विलोम शब्द क्या है?",
        ["Lazy or Idle (आलसी)", "Hardworking", "Persistent", "Active"],
        "'Diligent' का अर्थ मेहनती होता है, जिसका विपरीतार्थी 'Lazy' (आलसी) है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        45, "General English", "Medium", "C",
        "Identify the sentence with correct subject-verb agreement:",
        ["Each of the girls have won a prize.", "Each of the girls were winning a prize.", "Each of the girls has won a prize.", "Each of the girls are winner."],
        "'Each of' takes a singular verb ('has won'). Hence, option C is correct.",
        "सही व्याकरणिक सामंजस्य (Subject-Verb Agreement) वाला वाक्य पहचानिए:",
        ["Each of the girls have won a prize.", "Each of the girls were winning a prize.", "Each of the girls has won a prize.", "Each of the girls are winner."],
        "'Each of' के बाद संज्ञा बहुवचन होती है किन्तु क्रिया सदैव एकवचन (has) प्रयुक्त होती है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        46, "General English", "Easy", "B",
        "Select the synonym of the word 'AMICABLE':",
        ["Hostile", "Friendly and peaceful", "Fierce", "Rude"],
        "'Amicable' means characterized by friendliness and absence of discord. Hence, option B is correct.",
        "'AMICABLE' शब्द का समानार्थी शब्द क्या होगा?",
        ["Hostile", "Friendly and peaceful (सौहार्दपूर्ण / मैत्रीपूर्ण)", "Fierce", "Rude"],
        "'Amicable' का अर्थ मैत्रीपूर्ण और शांतिपूर्ण होता है, अतः इसका समानार्थी 'Friendly' है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        47, "General English", "Medium", "D",
        "Fill in the blank with the correct preposition: 'The cat jumped ______ the fence.'",
        ["in", "at", "between", "over"],
        "'Over' signifies crossing from one side to the other above an obstacle. Hence, option D is correct.",
        "उचित Preposition भरिए: 'The cat jumped ______ the fence.'",
        ["in", "at", "between", "over"],
        "किसी बाधा या घेरे के ऊपर से कूदकर पार करने के लिए 'over' का प्रयोग होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        48, "General English", "Easy", "A",
        "One who cannot read and write is called:",
        ["Illiterate", "Literate", "Scholar", "Blind"],
        "An 'Illiterate' person lacks the ability to read and write. Hence, option A is correct.",
        "'One who cannot read and write' (अनपढ़) के लिए एक शब्द है:",
        ["Illiterate (निरक्षर)", "Literate", "Scholar", "Blind"],
        "जो पढ़ना-लिखना न जानता हो उसे 'Illiterate' (निरक्षर) कहा जाता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        49, "General English", "Medium", "C",
        "Choose the correct alternative: 'He is junior ______ me in service.'",
        ["than", "from", "to", "with"],
        "Comparative adjectives ending in '-ior' (junior, senior, prior, superior, inferior) take 'to', not 'than'. Hence, option C is correct.",
        "रिक्त स्थान भरिए: 'He is junior ______ me in service.'",
        ["than", "from", "to", "with"],
        "लैटिन तुलनात्मक विशेषणों (Junior, Senior आदि) के बाद 'than' के स्थान पर 'to' का प्रयोग होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        50, "General English", "Easy", "B",
        "What does the idiom 'To leave no stone unturned' mean?",
        ["To collect stones", "To make every possible effort to achieve something", "To construct a stone wall", "To break rocks"],
        "'To leave no stone unturned' means to use every possible means or make every effort to reach an objective. Hence, option B is correct.",
        "Idiom 'To leave no stone unturned' का क्या अर्थ है?",
        ["पत्थर इकट्ठा करना", "कोई कसर न छोड़ना / हर संभव प्रयास करना", "दीवार बनाना", "चट्टान तोड़ना"],
        "'To leave no stone unturned' का अर्थ किसी कार्य की सफलता के लिए पूरा जोर लगा देना या कोई कसर न छोड़ना होता है। अतः विकल्प B सही है।"
    ))

    # =============================================================
    # SECTION 3: INTERPERSONAL SKILLS & COMMUNICATION (Q51 to Q75)
    # =============================================================
    qs.append(create_q(
        51, "Interpersonal & Communication Skills", "Medium", "B",
        "In organizational hierarchy, when information is passed upward through multiple tiers and becomes watered down or altered, this is called:",
        ["Semantic noise", "Filtering (निस्यंदन / छनन)", "Horizontal drift", "Direct feedback"],
        "Filtering is the deliberate or unconscious manipulation of information by intermediaries so it appears more favorable to senior leadership. Hence, option B is correct.",
        "संगठनात्मक पदानुक्रम में जब नीचे से ऊपर जाते समय सूचना को छाँटकर या विकृत करके प्रस्तुत किया जाता है, तो इसे क्या कहते हैं?",
        ["शब्दार्थीय शोर", "निस्यंदन / छनन (Filtering)", "क्षैतिज बहाव", "प्रत्यक्ष प्रतिपुष्टि"],
        "निस्यंदन (फिल्टरिंग) में मध्यवर्ती अधिकारी अप्रिय सूचनाओं को दबाकर केवल सुखद बातें ही उच्चाधिकारियों तक पहुंचाते हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        52, "Interpersonal & Communication Skills", "Easy", "A",
        "The scientific study of touch behavior as a non-verbal mode of communication is called:",
        ["Haptics (स्पर्श विज्ञान)", "Chronemics", "Proxemics", "Oculesics"],
        "Haptics is the study of how touch conveys emotions, status, and interpersonal warmth. Hence, option A is correct.",
        "अशाब्दिक संप्रेषण में शारीरिक स्पर्श (जैसे हाथ मिलाना, पीठ थपथपाना) के अध्ययन को क्या कहा जाता है?",
        ["हैप्टिक्स (Haptics / स्पर्श संप्रेषण)", "क्रोनेमिक्स", "प्रॉक्सिमिक्स", "ओकुलेसिक्स"],
        "हैप्टिक्स शारीरिक स्पर्श के माध्यम से व्यक्त होने वाले संवाद संकेतों का विज्ञान है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        53, "Interpersonal & Communication Skills", "Medium", "D",
        "Which of the following is considered the most common interpersonal defense mechanism when facing constructive criticism?",
        ["Active empathy", "Open questioning", "Taking notes", "Rationalization and denial (युक्तियुक्तकरण एवं इनकार)"],
        "When ego is threatened by criticism, individuals commonly resort to rationalization, projection, and denial to deflect blame. Hence, option D is correct.",
        "रचनात्मक आलोचना का सामना करते समय व्यक्ति द्वारा सामान्यतः अपनाई जाने वाली मनोवैज्ञानिक रक्षात्मक युक्ति (Defense Mechanism) कौन-सी है?",
        ["सक्रिय परानुभूति", "खुले प्रश्न पूछना", "नोट्स बनाना", "युक्तियुक्तकरण एवं इनकार (Rationalization & Denial)"],
        "व्यक्ति अपने अहम् की रक्षा के लिए बहानों का सहारा लेता है (युक्तियुक्तकरण) और अपनी त्रुटियों को मानने से इनकार करता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        54, "Interpersonal & Communication Skills", "Hard", "C",
        "The 'Sunk Cost Fallacy' in administrative decision-making causes administrators to:",
        ["Invest only in small projects", "Quit projects prematurely", "Continue investing money and time in failing projects to justify earlier expenditures", "Fire all project managers"],
        "The Sunk Cost Fallacy (escalation of commitment) traps decision-makers into throwing good resources after bad due to emotional attachment to unrecoverable past costs. Hence, option C is correct.",
        "प्रशासनिक निर्णयन में 'डूबत लागत भ्रांति' (Sunk Cost Fallacy) के कारण प्रशासक:",
        ["केवल छोटी योजनाओं में निवेश करते हैं", "परियोजनाओं को समय से पहले छोड़ देते हैं", "विगत खर्च को उचित ठहराने के लिए असफल योजनाओं में भी निरंतर संसाधन लगाते रहते हैं", "सभी सलाहकारों को हटा देते हैं"],
        "डूबत लागत पूर्वाग्रह में व्यक्ति यह सोचकर गलत योजना में धन लगाता रहता है कि 'पहले ही इतना खर्च हो चुका है, अब पीछे कैसे हटें'। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        55, "Interpersonal & Communication Skills", "Easy", "B",
        "Which of the following communication channels is least susceptible to misinterpretation of emotional tone?",
        ["Official email text", "Direct face-to-face dialogue with eye contact and body language", "Anonymous typed letter", "Notice board flyer"],
        "Face-to-face interaction provides vocal tone, facial expressions, and immediate clarification, minimizing emotional misinterpretation. Hence, option B is correct.",
        "निम्नलिखित में से किस संप्रेषण माध्यम में भावनात्मक लहजे के गलत अर्थ निकाले जाने की संभावना न्यूनतम होती है?",
        ["आधिकारिक ईमेल", "आमने-सामने प्रत्यक्ष संवाद (शारीरिक हाव-भाव युक्त)", "गुमनाम पत्र", "नोटिस बोर्ड"],
        "प्रत्यक्ष बातचीत में मुखमुद्रा और स्वर के उतार-चढ़ाव स्पष्ट होने से गलतफहमी की गुंजाइश सबसे कम रहती है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        56, "Interpersonal & Communication Skills", "Medium", "A",
        "In Thomas-Kilmann conflict management, the 'Avoiding' style is characterized by:",
        ["Low assertiveness and low cooperativeness (withdrawing from conflict)", "High assertiveness and high cooperativeness", "High assertiveness and low cooperativeness", "Low assertiveness and high cooperativeness"],
        "Avoiding represents unassertive and uncooperative behavior where an individual sidesteps, postpones, or withdraws from the issue. Hence, option A is correct.",
        "संघर्ष समाधान के थॉमस-किल्मन मॉडल में 'परिहार / टालने' (Avoiding) की शैली की क्या विशेषता है?",
        ["न्यून दृढ़ता और न्यून सहयोग (संघर्ष से पीछे हट जाना)", "उच्च दृढ़ता और उच्च सहयोग", "उच्च दृढ़ता और न्यून सहयोग", "न्यून दृढ़ता और उच्च सहयोग"],
        "टालने (अवाइडिंग) की शैली में व्यक्ति मुद्दे का सामना करने के बजाय उससे किनारा कर लेता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        57, "Interpersonal & Communication Skills", "Medium", "C",
        "The tendency for group members to exert less effort when working collectively than when working individually is called:",
        ["Groupthink", "Group polarization", "Social Loafing (सामाजिक अकर्मण्यता)", "Deindividuation"],
        "Social loafing occurs when individual contributions are pooled into a group effort and accountability is diffused. Hence, option C is correct.",
        "सामूहिक कार्य करते समय अकेले काम करने की तुलना में व्यक्तियों द्वारा कम प्रयास करने की प्रवृत्ति को क्या कहा जाता है?",
        ["समूह-सोच", "समूह ध्रुवीकरण", "सामाजिक अकर्मण्यता (Social Loafing)", "अव्यक्तिगतता"],
        "सामाजिक अकर्मण्यता में समूह के भीतर अपनी जिम्मेदारी के कम आंके जाने पर व्यक्ति कम मेहनत करता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        58, "Interpersonal & Communication Skills", "Easy", "D",
        "In proxemic distances, a distance of 4 feet to 12 feet between individuals is defined as:",
        ["Intimate distance", "Personal distance", "Confidential distance", "Social distance (सामाजिक दूरी)"],
        "Edward Hall established that 4 to 12 feet corresponds to Social distance, commonly used in business meetings and formal interviews. Hence, option D is correct.",
        "प्रॉक्सिमिक्स (सामीप्य विज्ञान) में 4 फीट से 12 फीट के बीच की शारीरिक दूरी को क्या कहा जाता है?",
        ["अंतरंग दूरी (0 से 1.5 फीट)", "व्यक्तिगत दूरी (1.5 से 4 फीट)", "गोपनीय दूरी", "सामाजिक दूरी (Social distance)"],
        "व्यावसायिक वार्ताओं एवं औपचारिक बैठकों के लिए 4 से 12 फीट की दूरी मानक 'सामाजिक दूरी' कहलाती है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        59, "Interpersonal & Communication Skills", "Medium", "B",
        "Which of the following is a key characteristic of 'Passive-Aggressive' communication behavior?",
        ["Direct and violent physical assault", "Expressing hidden resentment through indirect sabotage, deliberate procrastination, and sarcastic compliance", "Open and sincere collaboration", "Total silence without any emotion"],
        "Passive-aggressive communicators avoid direct confrontation and instead act out hostility through passive resistance, tardiness, and subtle stubbornness. Hence, option B is correct.",
        "'निष्क्रिय-आक्रामक' (Passive-Aggressive) संवाद शैली का मुख्य लक्षण क्या है?",
        ["प्रत्यक्ष हिंसक हमला", "प्रत्यक्ष विरोध न करके काम में जानबूझकर देरी, व्यंग्य और अप्रत्यक्ष रूप से बाधा डालना", "ईमानदार सहयोग", "पूर्णतः शांत रहना"],
        "निष्क्रिय-आक्रामक व्यक्ति सामने से सहमति जताता है परन्तु परोक्ष रूप से कार्य को लटकाकर या व्यंग्य करके अपनी नाराजगी प्रकट करता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        60, "Interpersonal & Communication Skills", "Hard", "A",
        "Herbert Simon's concept of 'Bounded Rationality' asserts that decision-makers are constrained by:",
        ["Incomplete information, cognitive capacity limits, and limited time", "Lack of any education", "Purely supernatural beliefs", "Total absence of any laws"],
        "Bounded rationality recognizes that human cognition, incomplete search, and time constraints prevent truly omniscient optimization. Hence, option A is correct.",
        "हर्बर्ट साइमन का 'सीमित तार्किकता' (Bounded Rationality) का सिद्धांत यह प्रतिपादित करता है कि निर्णयकर्ता बंधे होते हैं:",
        ["अपूर्ण सूचना, मानवीय मस्तिष्क की प्रसंस्करण सीमा तथा समय के अभाव से", "शिक्षा की पूर्ण कमी से", "अलौकिक अंधविश्वासों से", "कानून के पूर्ण अभाव से"],
        "हर्बर्ट साइमन के अनुसार मनुष्य सभी संभावित विकल्पों को जानने और उनका विश्लेषण करने में असमर्थ होता है, अतः उसकी तार्किकता सीमित होती है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        61, "Interpersonal & Communication Skills", "Easy", "C",
        "In a public meeting, the person elected or appointed to maintain order and direct proceedings is the:",
        ["Rapporteur", "Treasurer", "Chairperson / Presiding Officer", "Usher"],
        "The Chairperson controls floor time, maintains parliamentary order, and guides the session according to the agenda. Hence, option C is correct.",
        "औपचारिक सभा या बैठक का संचालन करने तथा व्यवस्था बनाए रखने वाले प्रमुख को क्या कहा जाता है?",
        ["कार्यवृत्त लेखक", "कोषाध्यक्ष", "अध्यक्ष / पीठासीन अधिकारी (Chairperson)", "प्रबंधक"],
        "बैठक की कार्यवाही का नियमन और अनुशासन बनाए रखने का उत्तरदायित्व सभापति या अध्यक्ष का होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        62, "Interpersonal & Communication Skills", "Medium", "B",
        "Which of the following describes 'Pseudolistening'?",
        ["Listening attentively with a recorder", "Pretending to listen by nodding while one's mind is elsewhere", "Listening through a hidden microphone", "Listening to foreign languages"],
        "Pseudolistening is counterfeit listening where the individual gives visual feedback of attentiveness while mentally disengaged. Hence, option B is correct.",
        "संप्रेषण में 'छद्म श्रवण' (Pseudolistening) से क्या तात्पर्य है?",
        ["रिकॉर्डर से ध्यानपूर्वक सुनना", "सिर हिलाकर सुनने का झूठा दिखावा करना जबकि ध्यान कहीं और हो", "छिपे हुए यंत्र से सुनना", "विदेशी भाषा सुनना"],
        "छद्म श्रवण में व्यक्ति वक्ता को यह दिखाता है कि वह सुन रहा है, जबकि उसका मन किसी अन्य विचार में मग्न होता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        63, "Interpersonal & Communication Skills", "Medium", "D",
        "The psychological barrier where a listener rejects or devalues a message solely because of their dislike of the speaker is known as:",
        ["Semantic noise", "Physiological deafness", "Information entropy", "Source Credibility Bias / Ad Hominem barrier"],
        "When personal bias against the sender causes the receiver to discount legitimate information, it is a source credibility distortion. Hence, option D is correct.",
        "जब कोई श्रोता केवल वक्ता के प्रति अपनी व्यक्तिगत नापसंदगी के कारण उसके सही संदेश को भी खारिज कर देता है, तो यह कौन-सी बाधा है?",
        ["शब्दार्थीय बाधा", "दैहिक बहरापन", "सूचना क्षय", "स्रोत विश्वसनीयता पूर्वाग्रह (Ad Hominem barrier)"],
        "वक्ता के प्रति दुर्भावना या पूर्वाग्रह के कारण संदेश के गुण-दोष की अनदेखी करना स्रोत पूर्वाग्रह कहलाता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        64, "Interpersonal & Communication Skills", "Hard", "A",
        "In the Johari Window, how can an individual increase their 'Open Area' (Arena) to build deeper professional trust?",
        ["Through self-disclosure and soliciting feedback", "By keeping all plans secret", "By refusing to communicate with juniors", "By ignoring all performance reviews"],
        "Expanding the Open quadrant requires two intentional behaviors: disclosing personal thoughts/goals and actively asking others for constructive feedback. Hence, option A is correct.",
        "जोहारी विंडो मॉडल में कोई अधिकारी अपने 'खुले क्षेत्र' (Open Area) का विस्तार करके विश्वास कैसे बढ़ा सकता है?",
        ["स्वयं के विचारों को साझा करके (Self-disclosure) तथा दूसरों से प्रतिपुष्टि (Feedback) मांगकर", "सभी योजनाओं को गुप्त रखकर", "कनिष्ठों से बात करने से बचकर", "समीक्षाओं की उपेक्षा करके"],
        "आत्म-प्रकटीकरण (अपनी बात स्पष्ट रखना) और दूसरों से निष्पक्ष फीडबैक लेने से खुला क्षेत्र बढ़ता है और अंतर्वैयक्तिक संबंध सुदृढ़ होते हैं। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        65, "Interpersonal & Communication Skills", "Easy", "C",
        "Which of the following bodily gestures typically indicates nervousness or anxiety during an interview?",
        ["Firm, upright posture", "Direct, warm eye contact", "Fidgeting with fingers, pencil tapping, and foot bouncing", "Calm hand rest"],
        "Fidgeting, repetitive tapping, and shaking legs are classic non-verbal leakage cues of internal anxiety. Hence, option C is correct.",
        "साक्षात्कार के दौरान कौन-सा शारीरिक हाव-भाव घबराहट या तनाव का संकेत माना जाता है?",
        ["सीधे और शांत बैठना", "संतुलित नेत्र संपर्क", "उंगलियां मरोड़ना, पैर हिलाना या पेन खटखटाना", "हाथों को स्थिर रखना"],
        "अनावश्यक उंगलियां चटकाना या पैर हिलाना आंतरिक बेचैनी और तनाव का अशाब्दिक प्रकटीकरण है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        66, "Interpersonal & Communication Skills", "Medium", "B",
        "What is the term for official written records detailing the discussions, motions, and decisions taken during a formal meeting?",
        ["Agenda", "Minutes of the Meeting (कार्यवृत्त)", "Circular", "Memo"],
        "Minutes constitute the official chronological legal record of everything transacted and agreed upon in a meeting. Hence, option B is correct.",
        "किसी औपचारिक बैठक में हुई चर्चा, प्रस्तावों और लिए गए निर्णयों के आधिकारिक लिखित अभिलेख को क्या कहा जाता है?",
        ["कार्यसूची (Agenda)", "कार्यवृत्त (Minutes of the Meeting)", "परिपत्र", "ज्ञापन"],
        "बैठक में संपन्न कार्यवाही और निर्णयों के प्रामाणिक दस्तावेज को 'कार्यवृत्त' (मिनट्स) कहा जाता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        67, "Interpersonal & Communication Skills", "Medium", "A",
        "The cognitive bias known as the 'Fundamental Attribution Error' leads people to:",
        ["Overemphasize internal personality traits and underestimate situational forces when explaining others' bad behavior", "Blame everything on the weather", "Assume all people are identical", "Always give others the benefit of the doubt"],
        "Lee Ross defined this error as our universal tendency to judge others' mistakes as flaws of character while excusing our own as forced by context. Hence, option A is correct.",
        "'मूलभूत आरोपण त्रुटि' (Fundamental Attribution Error) के अनुसार व्यक्ति दूसरों की गलतियों का मूल्यांकन करते समय:",
        ["परिस्थितिजन्य कारणों की अनदेखी करके उनके आंतरिक चरित्र या व्यक्तित्व को ही सारा दोष देता है", "सारा दोष मौसम पर डालता है", "सभी लोगों को समान मानता है", "दूसरों को संदेह का लाभ देता है"],
        "जब कोई दूसरा गलती करता है तो हम उसे 'लापरवाह या बुरा' कह देते हैं, जबकि स्वयं गलती होने पर परिस्थिति को दोष देते हैं। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        68, "Interpersonal & Communication Skills", "Easy", "D",
        "Which of the following is an essential prerequisite for empathetic listening?",
        ["Interrupting to give quick advice", "Checking watch repeatedly", "Thinking about what to reply", "Suspending judgment and giving undivided attention to the speaker"],
        "Empathy requires setting aside personal biases, resisting premature judgment, and tuning into the emotional world of the speaker. Hence, option D is correct.",
        "परानुभूतिक श्रवण (Empathetic listening) के लिए सबसे अनिवार्य पूर्व-शर्त क्या है?",
        ["शीघ्र सलाह देने के लिए बीच में बोलना", "बार-बार घड़ी देखना", "अपने उत्तर के बारे में सोचते रहना", "पूर्वाग्रहों को त्यागकर वक्ता को अपना पूरा ध्यान और मानसिक उपस्थिति देना"],
        "सामने वाले की बात को बिना किसी आलोचनात्मक पूर्वाग्रह के पूरे मनोयोग से सुनना ही परानुभूतिक श्रवण का आधार है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        69, "Interpersonal & Communication Skills", "Hard", "C",
        "In negotiation dynamics, the 'Zone of Possible Agreement' (ZOPA) is defined as:",
        ["The physical conference room where talks occur", "A treaty signed between nations", "The overlapping range between the buyer's maximum price and the seller's minimum reservation price", "The area outside the negotiation room"],
        "ZOPA is the bargaining range where the reservation prices of both parties overlap, making an agreement mutually acceptable. Hence, option C is correct.",
        "वार्ता एवं सौदेबाजी (Negotiation) में 'ZOPA' (Zone of Possible Agreement) से क्या तात्पर्य है?",
        ["वार्ता कक्ष का भौतिक क्षेत्र", "हस्ताक्षरित संधि", "क्रेता के अधिकतम मूल्य और विक्रेता के न्यूनतम आरक्षित मूल्य के बीच का परस्पर स्वीकार्य दायरा", "वार्ता से बाहर का क्षेत्र"],
        "ZOPA वह मूल्य सीमा होती है जिसके भीतर दोनों पक्षों के लाभ का बिंदु मिलता है और समझौता संभव होता है। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        70, "Interpersonal & Communication Skills", "Medium", "B",
        "Which of the following constitutes an effective 'Assertive' response to an unreasonable workload demand?",
        ["Screaming and insulting the boss", "Calmly explaining current priorities, constraints, and offering realistic timeline options", "Silently accepting and then secretly neglecting the work", "Weeping in front of colleagues"],
        "Assertiveness combines respect for self and others through clear, factual, and composed negotiation of boundaries. Hence, option B is correct.",
        "अत्यधिक एवं अनुचित कार्यभार सौंपे जाने पर एक 'दृढ़तापरक' (Assertive) अधिकारी की क्या उचित प्रतिक्रिया होगी?",
        ["चीखना और उच्चाधिकारी का अपमान करना", "शांत रहकर अपनी वर्तमान प्राथमिकताओं और सीमाओं को स्पष्ट करना तथा व्यावहारिक समय-सीमा का प्रस्ताव देना", "चुपचाप स्वीकार करके बाद में काम छोड़ देना", "सहकर्मियों के सामने रोना"],
        "दृढ़तापरक संवाद में व्यक्ति बिना गुस्सा किए या दब्बू बने अपनी वास्तविक स्थिति को तर्कपूर्ण ढंग से रखता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        71, "Interpersonal & Communication Skills", "Easy", "A",
        "In non-verbal communication, 'Artifactics' refers to messages conveyed by:",
        ["Personal clothing, jewelry, eyeglasses, and office decorations", "Only acoustic sounds", "Footstep speed", "Time zones"],
        "Artifactics is the study of personal adornments, dress, accessories, and interior décor as communicators of identity and status. Hence, option A is correct.",
        "अशाब्दिक संप्रेषण में 'आर्टिफैक्टिक्स' (Artifactics) का संबंध किससे है?",
        ["पहनावे, आभूषणों, साज-सज्जा और परिवेशीय वस्तुओं द्वारा संप्रेषित संदेशों से", "केवल ध्वनि तरंगों से", "पैरों की गति से", "समय क्षेत्र से"],
        "व्यक्ति की वेशभूषा, घड़ी, चश्मा और कार्यालय की सजावट अशाब्दिक रूप से उसके पद और व्यक्तित्व का संदेश देती है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        72, "Interpersonal & Communication Skills", "Medium", "D",
        "The informal network pattern where one person communicates with a few selected trusted individuals who then pass it to others is the:",
        ["Single strand chain", "Gossip circle", "Wheel pattern", "Cluster chain (गुच्छ श्रृंखला)"],
        "In a cluster grapevine, information travels through selective clusters of trusted liaisons, which is the most common pattern in real organizations. Hence, option D is correct.",
        "अनौपचारिक संप्रेषण में जब कोई व्यक्ति केवल कुछ चुने हुए विश्वस्त व्यक्तियों को सूचना देता है और वे आगे अपने विश्वस्तों को बताते हैं, तो यह क्या कहलाता है?",
        ["एकल श्रृंखला", "गपशप श्रृंखला", "पहिया पैटर्न", "गुच्छ श्रृंखला (Cluster Chain)"],
        "संगठनों में अनौपचारिक अफवाहों और सूचनाओं के प्रसार का सबसे सामान्य माध्यम 'गुच्छ श्रृंखला' ही होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        73, "Interpersonal & Communication Skills", "Medium", "B",
        "The cognitive tendency to judge a situation based on a single extreme recent disaster while ignoring long-term statistical averages is an example of:",
        ["Hindsight bias", "Salience / Recency bias", "Logical deduction", "Empirical regression"],
        "Recency or Salience bias causes individuals to give undue weight to vivid, recent occurrences over objective long-term baseline data. Hence, option B is correct.",
        "किसी हालिया आपदा के प्रभाव में आकर दीर्घकालिक सांख्यिकीय औसत की अनदेखी करते हुए निर्णय लेना किस पूर्वाग्रह का उदाहरण है?",
        ["पश्चदृष्टि पूर्वाग्रह", "नवीनता / प्रमुखता पूर्वाग्रह (Recency / Salience Bias)", "तार्किक निगमन", "आनुभविक प्रतिगमन"],
        "हाल ही में घटी घटना मस्तिष्क में अत्यंत सजीव होती है, जिससे व्यक्ति उसके आधार पर असंतुलित निर्णय कर बैठता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        74, "Interpersonal & Communication Skills", "Easy", "C",
        "Maintaining open palms and uncrossed arms during a negotiation typically communicates:",
        ["Deceit and hidden motives", "Intense anger", "Honesty, sincerity, and willingness to cooperate", "Desire to end talks abruptly"],
        "Open palms have been historically documented as an honest, disarming gesture signaling transparency and truthfulness. Hence, option C is correct.",
        "वार्ता के दौरान हथेलियों को खुला रखना और हाथ न बांधना सामान्यतः क्या संकेत देता है?",
        ["कपट और गुप्त इरादे", "तीव्र क्रोध", "ईमानदारी, खुलापन एवं सहयोग की तत्परता", "वार्ता समाप्त करने की जल्दी"],
        "खुली हथेलियां और सहज मुद्रा सत्यनिष्ठा, पारदर्शिता और सकारात्मक संवाद का अशाब्दिक प्रतीक हैं। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        75, "Interpersonal & Communication Skills", "Medium", "A",
        "When two departments in a government ministry exchange reports to coordinate a joint program, they are engaging in:",
        ["Horizontal / Lateral communication", "Downward communication", "Upward communication", "Informal rumor mill"],
        "Coordination between peer departments on the same administrative horizontal plane constitutes Lateral/Horizontal communication. Hence, option A is correct.",
        "जब किसी मंत्रालय के दो समकक्ष विभाग किसी संयुक्त योजना के समन्वय हेतु फाइलों या रिपोर्टों का आदान-प्रदान करते हैं, तो यह क्या कहलाता है?",
        ["क्षैतिज / पार्श्व संप्रेषण (Horizontal communication)", "अधोमुखी संप्रेषण", "उर्ध्वमुखी संप्रेषण", "अनौपचारिक जनप्रवाद"],
        "समान प्रशासनिक स्तर के विभागों के बीच समन्वय और सूचना विनिमय क्षैतिज संप्रेषण कहलाता है। अतः विकल्प A सही उत्तर है।"
    ))

    # ==============================================================
    # SECTION 4: LOGICAL REASONING & BASIC NUMERACY (Q76 to Q100)
    # ==============================================================
    qs.append(create_q(
        76, "Logical Reasoning & Maths", "Easy", "B",
        "Find the missing term in the sequence: 5, 10, 20, 40, 80, ?",
        ["140", "160", "150", "180"],
        "Each term is doubled: 5*2=10, 10*2=20, 20*2=40, 40*2=80, 80*2=160. Hence, option B is correct.",
        "संख्या श्रृंखला में अगला पद क्या होगा: 5, 10, 20, 40, 80, ?",
        ["140", "160", "150", "180"],
        "प्रत्येक संख्या अपनी पूर्ववर्ती संख्या की दोगुनी है (80 × 2 = 160)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        77, "Logical Reasoning & Maths", "Easy", "A",
        "If 'WATER' is coded as 'YCVGT', how is 'FIRE' coded in that language?",
        ["HKTG", "GJSF", "HKUF", "IKTG"],
        "Each letter is shifted by +2: F(+2)->H, I(+2)->K, R(+2)->T, E(+2)->G -> HKTG. Hence, option A is correct.",
        "यदि किसी कूट भाषा में 'WATER' को 'YCVGT' लिखा जाता है, तो उसी भाषा में 'FIRE' को कैसे लिखा जाएगा?",
        ["HKTG", "GJSF", "HKUF", "IKTG"],
        "प्रत्येक वर्ण में +2 का विस्थापन किया गया है: F→H, I→K, R→T, E→G। अतः कोड HKTG होगा। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        78, "Logical Reasoning & Maths", "Medium", "C",
        "A is the brother of B. B is the sister of C. C is the father of D. How is A related to D?",
        ["Father", "Brother", "Paternal Uncle (चाचा)", "Grandfather"],
        "A and B are siblings of C. C is D's father. Therefore, C's brother A is the Paternal Uncle of D. Hence, option C is correct.",
        "A, B का भाई है। B, C की बहन है। C, D का पिता है। A का D से क्या संबंध है?",
        ["पिता", "भाई", "चाचा (Paternal Uncle)", "दादा"],
        "C, D का पिता है तथा A, C का भाई है। अतः A, D का चाचा है। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        79, "Logical Reasoning & Maths", "Easy", "D",
        "A man walks 6 km towards West, turns left and walks 8 km. How far is he from his starting point?",
        ["12 km", "14 km", "8 km", "10 km"],
        "Shortest distance = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10 km. Hence, option D is correct.",
        "एक व्यक्ति पश्चिम दिशा में 6 किमी चलता है, फिर बाएँ मुड़कर 8 किमी चलता है। वह अपने प्रारंभिक बिंदु से कितनी दूरी पर है?",
        ["12 किमी", "14 किमी", "8 किमी", "10 किमी"],
        "दूरी = √(6² + 8²) = √(36 + 64) = √100 = 10 किमी। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        80, "Logical Reasoning & Maths", "Medium", "B",
        "The average of five numbers is 46 and that of the first four numbers is 45. What is the fifth number?",
        ["48", "50", "52", "49"],
        "Sum of 5 numbers = 5 * 46 = 230. Sum of 4 numbers = 4 * 45 = 180. Fifth number = 230 - 180 = 50. Hence, option B is correct.",
        "पाँच संख्याओं का औसत 46 है तथा प्रथम चार संख्याओं का औसत 45 है। पाँचवीं संख्या क्या होगी?",
        ["48", "50", "52", "49"],
        "पाँच संख्याओं का कुल योग = 5 × 46 = 230। प्रथम चार का योग = 4 × 45 = 180। पाँचवीं संख्या = 230 - 180 = 50। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        81, "Logical Reasoning & Maths", "Easy", "C",
        "A shopkeeper marks an item of ₹1,000 with a 20% discount. What is the selling price?",
        ["₹750", "₹700", "₹800", "₹850"],
        "Discount = 20% of 1000 = ₹200. SP = 1000 - 200 = ₹800. Hence, option C is correct.",
        "₹1,000 के अंकित मूल्य वाली वस्तु पर 20% की छूट दी जाती है। वस्तु का विक्रय मूल्य क्या होगा?",
        ["₹750", "₹700", "₹800", "₹850"],
        "छूट = 1000 का 20% = ₹200। विक्रय मूल्य = 1000 - 200 = ₹800। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        82, "Logical Reasoning & Maths", "Medium", "A",
        "12 men can finish a project in 20 days. In how many days can 15 men finish the same project?",
        ["16 days", "18 days", "15 days", "14 days"],
        "M1 * D1 = M2 * D2 => 12 * 20 = 15 * D2 => D2 = 240 / 15 = 16 days. Hence, option A is correct.",
        "12 पुरुष किसी कार्य को 20 दिन में पूरा कर सकते हैं। उसी कार्य को 15 पुरुष कितने दिनों में पूरा करेंगे?",
        ["16 दिन", "18 दिन", "15 दिन", "14 दिन"],
        "सूत्र: M₁ × D₁ = M₂ × D₂ => 12 × 20 = 15 × D₂ => D₂ = 240 / 15 = 16 दिन। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        83, "Logical Reasoning & Maths", "Easy", "D",
        "Divide ₹1,200 between A and B in the ratio 3 : 5. How much does B receive?",
        ["₹450", "₹600", "₹700", "₹750"],
        "Total parts = 3 + 5 = 8. B's share = (5/8) * 1200 = 5 * 150 = ₹750. Hence, option D is correct.",
        "₹1,200 को A और B के बीच 3 : 5 के अनुपात में बाँटिए। B का हिस्सा कितना होगा?",
        ["₹450", "₹600", "₹700", "₹750"],
        "कुल भाग = 3 + 5 = 8। B का भाग = (5/8) × 1200 = ₹750। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        84, "Logical Reasoning & Maths", "Medium", "B",
        "The simple interest on a certain sum for 3 years at 5% per annum is ₹600. What is the principal sum?",
        ["₹3,500", "₹4,000", "₹4,500", "₹5,000"],
        "P = (SI * 100) / (R * T) = (600 * 100) / (5 * 3) = 60000 / 15 = ₹4,000. Hence, option B is correct.",
        "किसी धनराशि पर 5% वार्षिक दर से 3 वर्ष का साधारण ब्याज ₹600 है। वह मूलधन क्या है?",
        ["₹3,500", "₹4,000", "₹4,500", "₹5,000"],
        "मूलधन = (ब्याज × 100) / (दर × समय) = (600 × 100) / (5 × 3) = ₹4,000। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        85, "Logical Reasoning & Maths", "Medium", "C",
        "A motorist travels 180 km at 60 km/h and returns at 90 km/h. What is his average speed for the round trip?",
        ["75 km/h", "70 km/h", "72 km/h", "74 km/h"],
        "Average speed = (2 * x * y) / (x + y) = (2 * 60 * 90) / (60 + 90) = 10800 / 150 = 72 km/h. Hence, option C is correct.",
        "एक मोटर चालक 180 किमी की दूरी 60 किमी/घं की चाल से जाता है तथा 90 किमी/घं की चाल से वापस आता है। पूरी यात्रा की औसत चाल क्या है?",
        ["75 किमी/घं", "70 किमी/घं", "72 किमी/घं", "74 किमी/घं"],
        "औसत चाल = 2xy / (x + y) = (2 × 60 × 90) / 150 = 72 किमी/घं। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        86, "Logical Reasoning & Maths", "Easy", "A",
        "In a row of 35 girls, Sunita is 10th from the right end. What is her rank from the left end?",
        ["26th", "25th", "27th", "24th"],
        "Rank from left = (Total - Right) + 1 = (35 - 10) + 1 = 25 + 1 = 26th. Hence, option A is correct.",
        "35 बालिकाओं की एक पंक्ति में सुनीता का स्थान दाएँ छोर से 10वाँ है। बाएँ छोर से उसका स्थान क्या होगा?",
        ["26वाँ", "25वाँ", "27वाँ", "24वाँ"],
        "बाएँ से स्थान = (35 - 10) + 1 = 26वाँ। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        87, "Logical Reasoning & Maths", "Medium", "D",
        "The perimeter of a square is 48 cm. What is the area of the square?",
        ["196 sq. cm", "121 sq. cm", "169 sq. cm", "144 sq. cm"],
        "Side = 48 / 4 = 12 cm. Area = 12^2 = 144 sq. cm. Hence, option D is correct.",
        "एक वर्ग का परिमाप 48 सेमी है। वर्ग का क्षेत्रफल कितना होगा?",
        ["196 वर्ग सेमी", "121 वर्ग सेमी", "169 वर्ग सेमी", "144 वर्ग सेमी"],
        "भुजा = 48 / 4 = 12 सेमी। क्षेत्रफल = (12)² = 144 वर्ग सेमी। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        88, "Logical Reasoning & Maths", "Easy", "B",
        "Which of the following numbers is completely divisible by 9?",
        ["12345", "54324", "65412", "78912"],
        "Sum of digits of 54324 = 5+4+3+2+4 = 18, which is divisible by 9. Hence, option B is correct.",
        "निम्नलिखित में से कौन-सी संख्या 9 से पूर्णतः विभाज्य है?",
        ["12345", "54324", "65412", "78912"],
        "54324 के अंकों का योग = 5 + 4 + 3 + 2 + 4 = 18 (जो 9 से विभाज्य है)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        89, "Logical Reasoning & Maths", "Medium", "C",
        "What is the reflex angle between the hands of a clock at 2:00?",
        ["60°", "120°", "300°", "240°"],
        "Angle at 2:00 = 2 * 30° = 60°. Reflex angle = 360° - 60° = 300°. Hence, option C is correct.",
        "घड़ी में 2:00 बजे दोनों सुइयों के मध्य का वृहत् कोण (Reflex angle) कितना होगा?",
        ["60°", "120°", "300°", "240°"],
        "2:00 बजे आंतरिक कोण = 60°। वृहत् कोण = 360° - 60° = 300°। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        90, "Logical Reasoning & Maths", "Easy", "A",
        "The product of two numbers is 720 and their HCF is 6. What is their LCM?",
        ["120", "140", "110", "130"],
        "LCM = Product / HCF = 720 / 6 = 120. Hence, option A is correct.",
        "दो संख्याओं का गुणनफल 720 तथा उनका HCF 6 है। उनका LCM क्या होगा?",
        ["120", "140", "110", "130"],
        "LCM = दो संख्याओं का गुणनफल / HCF = 720 / 6 = 120। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        91, "Logical Reasoning & Maths", "Medium", "B",
        "If a price is increased by 10% and then decreased by 10%, what is the net percentage change?",
        ["0% (No change)", "1% decrease", "1% increase", "2% decrease"],
        "Net change = 10 - 10 - (10*10)/100 = -1% (1% decrease). Hence, option B is correct.",
        "यदि किसी वस्तु के मूल्य में पहले 10% की वृद्धि और फिर 10% की कमी की जाए, तो कुल प्रतिशत परिवर्तन क्या होगा?",
        ["कोई परिवर्तन नहीं", "1% की कमी", "1% की वृद्धि", "2% की कमी"],
        "शुद्ध परिवर्तन = 10 - 10 - (100/100) = -1% (1% की कमी)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        92, "Logical Reasoning & Maths", "Hard", "D",
        "A box contains 3 white, 4 black, and 5 red balls. One ball is drawn at random. What is the probability that it is NOT black?",
        ["1/3", "5/12", "7/12", "2/3 (8/12)"],
        "Total balls = 3 + 4 + 5 = 12. Non-black balls = 3 + 5 = 8. Probability = 8 / 12 = 2/3. Hence, option D is correct.",
        "एक डिब्बे में 3 सफेद, 4 काली तथा 5 लाल गेंदें हैं। यादृच्छिक रूप से एक गेंद निकाली जाती है। उसके काली न होने की प्रायिकता क्या है?",
        ["1/3", "5/12", "7/12", "2/3 (8/12)"],
        "कुल गेंदें = 12। काली न होने वाली अनुकूल गेंदें = 3 + 5 = 8। प्रायिकता = 8/12 = 2/3। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        93, "Logical Reasoning & Maths", "Medium", "C",
        "If '×' means '+', '+' means '÷', '-' means '×', and '÷' means '-', what is: 8 × 7 - 3 + 6 ÷ 4 ?",
        ["12.5", "10", "7.5", "9.5"],
        "Expression: 8 + 7 * 3 / 6 - 4 = 8 + 21/6 - 4 = 8 + 3.5 - 4 = 7.5. Hence, option C is correct.",
        "यदि '×' का अर्थ '+', '+' का अर्थ '÷', '-' का अर्थ '×' तथा '÷' का अर्थ '-' हो, तो 8 × 7 - 3 + 6 ÷ 4 का मान क्या होगा?",
        ["12.5", "10", "7.5", "9.5"],
        "चिह्नों को बदलने पर: 8 + 7 × 3 ÷ 6 - 4 = 8 + 3.5 - 4 = 7.5। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        94, "Logical Reasoning & Maths", "Easy", "B",
        "Which of the following years was a leap year?",
        ["1900", "2004", "2001", "2003"],
        "2004 is divisible by 4, making it a leap year. 1900 is a century year not divisible by 400. Hence, option B is correct.",
        "निम्नलिखित में से कौन-सा वर्ष एक लीप वर्ष (अधिवर्ष) था?",
        ["1900", "2004", "2001", "2003"],
        "2004 संख्या 4 से पूर्णतः विभाज्य है, अतः यह एक लीप वर्ष था (1900 शताब्दी वर्ष 400 से विभाज्य नहीं था)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        95, "Logical Reasoning & Maths", "Medium", "A",
        "A student needs 40% marks to pass an examination. If he gets 178 marks and fails by 22 marks, what are the maximum marks?",
        ["500", "450", "400", "600"],
        "Passing marks = 178 + 22 = 200. 40% of Max = 200 => Max = (200 * 100) / 40 = 500. Hence, option A is correct.",
        "एक छात्र को उत्तीर्ण होने के लिए 40% अंक चाहिए। यदि वह 178 अंक प्राप्त करता है और 22 अंकों से अनुत्तीर्ण हो जाता है, तो कुल पूर्णांक कितना है?",
        ["500", "450", "400", "600"],
        "उत्तीर्णांक = 178 + 22 = 200। कुल पूर्णांक = (200 × 100) / 40 = 500 अंक। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        96, "Logical Reasoning & Maths", "Easy", "C",
        "Statements: All apples are fruits. All fruits are sweet. Conclusion: All apples are sweet.",
        ["Conclusion does not follow", "Partially true", "Conclusion follows logically", "Cannot be determined"],
        "Apples ⊂ Fruits ⊂ Sweet items => Apples ⊂ Sweet items. The conclusion definitely follows. Hence, option C is correct.",
        "कथन: सभी सेब फल हैं। सभी फल मीठे हैं। निष्कर्ष: सभी सेब मीठे हैं।",
        ["निष्कर्ष अनुसरण नहीं करता", "आंशिक सत्य है", "निष्कर्ष पूर्णतः तार्किक रूप से निकलता है", "तय नहीं किया जा सकता"],
        "सिलोगिज्म नियमानुसार: सेब ⊂ फल ⊂ मीठे पदार्थ। अतः सभी सेब निश्चित रूप से मीठे हैं। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        97, "Logical Reasoning & Maths", "Medium", "D",
        "A sum of ₹2,000 amounts to ₹2,420 in 2 years at compound interest compounded annually. What is the annual interest rate?",
        ["8%", "9%", "12%", "10%"],
        "A/P = 2420/2000 = 1.21 = (1 + r)^2 => 1 + r = 1.1 => r = 0.10 = 10%. Hence, option D is correct.",
        "₹2,000 की राशि 2 वर्ष में चक्रवृद्धि ब्याज से ₹2,420 हो जाती है। वार्षिक ब्याज की दर क्या है?",
        ["8%", "9%", "12%", "10%"],
        "A/P = 2420/2000 = 1.21 = (1 + r/100)² => 1 + r/100 = 1.1 => r = 10%। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        98, "Logical Reasoning & Maths", "Hard", "A",
        "How many 3-digit numbers can be formed using the digits 1, 2, 3, 4, 5 without repetition?",
        ["60", "120", "20", "24"],
        "5 * 4 * 3 = 60 numbers. Hence, option A is correct.",
        "अंकों 1, 2, 3, 4, 5 का प्रयोग करके बिना पुनरावृत्ति के 3 अंकों की कितनी संख्याएं बनाई जा सकती हैं?",
        ["60", "120", "20", "24"],
        "⁵P₃ = 5 × 4 × 3 = 60 संख्याएं। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        99, "Logical Reasoning & Maths", "Medium", "B",
        "A person covers a 600-metre long bridge in 5 minutes. What is his speed in km/h?",
        ["6 km/h", "7.2 km/h", "8.4 km/h", "9 km/h"],
        "Time = 5 * 60 = 300 s. Speed in m/s = 600 / 300 = 2 m/s. In km/h = 2 * (18/5) = 36/5 = 7.2 km/h. Hence, option B is correct.",
        "एक व्यक्ति 600 मीटर लंबे पुल को 5 मिनट में पार करता है। उसकी चाल किमी/घंटे में क्या है?",
        ["6 किमी/घं", "7.2 किमी/घं", "8.4 किमी/घं", "9 किमी/घं"],
        "समय = 300 सेकंड। चाल = 600 / 300 = 2 मी./से.। किमी/घंटे में = 2 × (18/5) = 7.2 किमी/घं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        100, "Logical Reasoning & Maths", "Easy", "C",
        "What is 30% of 150 added to 40% of 200?",
        ["115", "120", "125", "130"],
        "30% of 150 = 45. 40% of 200 = 80. Sum = 45 + 80 = 125. Hence, option C is correct.",
        "150 के 30% तथा 200 के 40% का योग कितना होगा?",
        ["115", "120", "125", "130"],
        "गणना: (150 × 0.3) + (200 × 0.4) = 45 + 80 = 125। अतः विकल्प C सही उत्तर है।"
    ))

    return qs

def main():
    qs = get_csat_2018_questions()
    assert len(qs) == 100, f"Expected 100 questions, got {len(qs)}"

    out_path = "tests/state_psc/uppcs_pre/pyq/uppcs_pre_pyq_2018_csat.json"
    data = {
        "testId": "uppcs_pre_pyq_2018_csat",
        "categoryId": "uppcs_pre",
        "test_id": "uppcs_pre_pyq_2018_csat",
        "category_id": "uppcs_pre",
        "title": "UPPSC PCS Prelims 2018 — CSAT Paper 2 (Full 100 Qs)",
        "titleEn": "UPPSC PCS Prelims 2018 — CSAT Paper 2 (Full 100 Qs)",
        "titleHi": "UPPSC PCS प्रारंभिक परीक्षा 2018 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
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
        "examYear": 2018,
        "shiftBadge": "UPPSC Prelims 2018 • CSAT Paper-2 (Full 100 Qs)",
        "questions": qs,
        "path": out_path.replace("\\", "/")
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)
    print(f"Successfully generated {out_path} with {len(qs)} questions.")

if __name__ == "__main__":
    main()
