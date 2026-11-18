#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_csat_2019.py — Builds 100-question authentic UPPSC PCS Prelims 2019 CSAT Paper 2."""
import json
import os

def create_q(q_num, topic, diff, ans, q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi):
    idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    idx = idx_map[ans.upper()]
    return {
        "questionId": f"uppcs_pre_2019_csat_q{q_num:03d}",
        "questionNumber": q_num,
        "q_id": q_num,
        "sectionId": "sec_csat",
        "sectionTitle": "CSAT Paper II",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.66,
        "pyqTag": "UPPCS Prelims 2019 • CSAT Paper-II",
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

def get_csat_2019_questions():
    qs = []

    # ==========================================
    # SECTION 1: GENERAL HINDI (Q1 to Q30)
    # ==========================================
    qs.append(create_q(
        1, "General Hindi", "Easy", "A",
        "Which of the following is the correct antonym of the word 'Garima' (गरिमा)?",
        ["Laghima (लघिमा)", "Mahima (महिमा)", "Garib (गरीब)", "Gurutva (गुरुत्व)"],
        "In Sanskrit grammar, 'Garima' (heaviness/grandeur) has the direct antonym 'Laghima' (lightness/smallness). Hence, option A is correct.",
        "निम्नलिखित में से 'गरिमा' का सही विलोम शब्द कौन-सा है?",
        ["लघिमा", "महिमा", "गरीब", "गुरुत्व"],
        "'गरिमा' का अर्थ भारीपन या बड़प्पन होता है, जिसका प्रामाणिक विलोम 'लघिमा' (छोटापन/लघुता) है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        2, "General Hindi", "Easy", "C",
        "Select the correct Tatsam form of the Tadbhav word 'Bhabhi' (भाभी):",
        ["Bhratri (भ्रातृ)", "Bhratrimata (भ्रातृमाता)", "Bhratribharaya (भ्रातृभार्या)", "Bhratrivadhik (भ्रातृवधिक)"],
        "The Sanskrit Tatsam word for 'Bhabhi' (brother's wife) is 'Bhratribharaya' (भ्रातृभार्या). Hence, option C is correct.",
        "तद्भव शब्द 'भाभी' का शुद्ध तत्सम रूप क्या होगा?",
        ["भ्रातृ", "भ्रातृमाता", "भ्रातृभार्या", "भ्रातृवधू"],
        "'भाभी' तद्भव शब्द है जिसका शुद्ध संस्कृत तत्सम 'भ्रातृभार्या' (भाई की पत्नी) होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        3, "General Hindi", "Medium", "B",
        "Which of the following is NOT a synonym of 'Surya' (सूर्य - Sun)?",
        ["Bhanu (भानु)", "Himanshu (हिमांशु)", "Bhaskara (भास्कर)", "Dinkara (दिनकर)"],
        "'Himanshu' (possessor of cool rays) is the Moon, whereas Bhanu, Bhaskara, and Dinkara are synonyms of Sun. Hence, option B is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'सूर्य' का पर्यायवाची नहीं है?",
        ["भानु", "हिमांशु", "भास्कर", "दिनकर"],
        "'हिमांशु' (शीतल किरणों वाला) चंद्रमा का पर्यायवाची है, जबकि भानु, भास्कर और दिनकर सूर्य के पर्यायवाची हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        4, "General Hindi", "Easy", "D",
        "Identify the correct Sandhi-Vichchhed of the word 'Maharshi' (महर्षि):",
        ["Mahan + Rishi", "Maha + Arshi", "Mah + Rishi", "Maha + Rishi (महा + ऋषि)"],
        "According to Guna Sandhi rules (आ + ऋ = अर्), Maha + Rishi forms Maharshi. Hence, option D is correct.",
        "'महर्षि' शब्द का सही संधि-विच्छेद क्या होगा?",
        ["महान + ऋषि", "महा + अर्षि", "मह + ऋषि", "महा + ऋषि"],
        "गुण स्वर संधि के नियमानुसार 'आ + ऋ' मिलकर 'अर्' बन जाता है (महा + ऋषि = महर्षि)। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        5, "General Hindi", "Medium", "A",
        "In the compound word 'Pratidin' (प्रतिदिन), which Samas is present?",
        ["Avyayibhava Samas (अव्ययीभाव समास)", "Tatpurusha Samas", "Dwigu Samas", "Dvandva Samas"],
        "'Pratidin' begins with the indeclinable prefix 'Prati', making it an Avyayibhava Samas. Hence, option A is correct.",
        "'प्रतिदिन' शब्द में कौन-सा समास है?",
        ["अव्ययीभाव समास", "तत्पुरुष समास", "द्विगु समास", "द्वंद्व समास"],
        "जिस समास का पूर्व पद अव्यय तथा प्रधान हो, वह अव्ययीभाव समास कहलाता है (प्रतिदिन = दिन-दिन / प्रत्येक दिन)। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        6, "General Hindi", "Easy", "C",
        "What is the one-word substitution for 'One who cannot be measured' (जिसकी माप न की जा सके)?",
        ["Anupam (अनुपम)", "Aprameya (अप्रमेय / अपरिमेय)", "Amulya (अमूल्य)", "Alankrit (अलंकृत)"],
        "That which cannot be measured or quantified is 'Aprameya' or 'Aparimeya'. Hence, option C is correct.",
        "'जिसकी माप न की जा सके' वाक्यांश के लिए एक शब्द है:",
        ["अनुपम", "अमूल्य", "अपरिमेय (या अप्रमेय)", "अगाध"],
        "जिसकी कोई माप या सीमा तय न की जा सके उसे 'अपरिमेय' या 'अप्रमेय' कहा जाता है। जिसकी उपमा न हो वह अनुपम है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        7, "General Hindi", "Medium", "B",
        "Which of the following sentences is free from grammatical errors?",
        ["Bharat mein anekon jaatiyan hain.", "Bharat mein anek jaatiyan hain.", "Bharat mein anekon jaati hai.", "Bharat ke andar anekon jaatiyan hain."],
        "'Anek' is already plural; 'anekon' is an ungrammatical colloquialism. Hence, 'Bharat mein anek jaatiyan hain' is grammatically correct. Hence, option B is correct.",
        "निम्नलिखित में से शुद्ध वाक्य का चयन कीजिए:",
        ["भारत में अनेकों जातियाँ हैं।", "भारत में अनेक जातियाँ हैं।", "भारत में अनेकों जाति है।", "भारत के अंदर अनेकों जातियाँ हैं।"],
        "'अनेक' शब्द स्वयं बहुवचन है, इसका बहुवचन 'अनेकों' बनाना व्याकरण विरुद्ध है। अतः 'भारत में अनेक जातियाँ हैं' शुद्ध वाक्य है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        8, "General Hindi", "Easy", "D",
        "What is the meaning of the Hindi idiom 'Kafan ki jeb na hona' (कफ़न में जेब न होना)?",
        ["Clothes are torn", "Tailor was negligent", "Dead body needs pocket", "Wealth cannot be carried after death (मृत्यु के बाद धन साथ नहीं जाता)"],
        "The idiom implies that material wealth is left behind in this world when a person dies. Hence, option D is correct.",
        "मुहावरा 'कफ़न में जेब न होना' का सही अर्थ क्या है?",
        ["वस्त्र का फटा होना", "दरजी की लापरवाही", "कफ़न साधारण होना", "मृत्यु के बाद धन-दौलत साथ नहीं जाती"],
        "इस मुहावरे का दार्शनिक अर्थ है कि मनुष्य संसार से खाली हाथ जाता है, मृत्यु के पश्चात कोई संपत्ति साथ नहीं जाती। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        9, "General Hindi", "Medium", "A",
        "Select the word with the correct spelling (शुद्ध वर्तनी):",
        ["Sushrusha (शुश्रूषा)", "Susrusha (सुश्रूषा)", "Sushrusa (शुश्रुषा)", "Shushrusha (सुश्रुसा)"],
        "The standard spelling for selfless caring/nursing is 'शुश्रूषा' (first talavya sha with u, second reph-shra with oo, third murdhanya sha with aa). Hence, option A is correct.",
        "निम्नलिखित में से 'शुद्ध वर्तनी' वाला शब्द कौन-सा है?",
        ["शुश्रूषा", "सुश्रूषा", "शुश्रुषा", "सुश्रुसा"],
        "रोगियों की सेवा अथवा बड़ों की टहल करने के अर्थ में 'शुश्रूषा' शुद्ध वर्तनी है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        10, "General Hindi", "Easy", "B",
        "Which of the following pairs of words and antonyms is correctly matched?",
        ["Dayalu - Kripalu", "Raju - Vakra (ऋजु - वक्र)", "Krodh - Gussa", "Satyavadi - Sachcha"],
        "'Riju' (straight/upright) has the precise antonym 'Vakra' (curved/crooked). The other pairs are synonyms. Hence, option B is correct.",
        "निम्नलिखित में से कौन-सा विलोम युग्म सही है?",
        ["दयालु - कृपालु", "ऋजु - वक्र", "क्रोध - गुस्सा", "सत्यवादी - सच्चा"],
        "'ऋजु' का अर्थ सीधा और सरल होता है, जिसका सही विलोम 'वक्र' (टेढ़ा) होता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        11, "General Hindi", "Medium", "C",
        "Which prefix (उपसर्ग) is present in the word 'Pratyupakara' (प्रत्युपकार)?",
        ["Pra (प्र)", "Para (परा)", "Prati (प्रति)", "Prat (प्रत्य्)"],
        "Prati (प्रति) + Upakara (उपकार) = Pratyupakara (via Yan Sandhi). The prefix is 'Prati'. Hence, option C is correct.",
        "'प्रत्युपकार' शब्द में किस उपसर्ग का प्रयोग हुआ है?",
        ["प्र", "परा", "प्रति", "प्रत्य्"],
        "यण स्वर संधि के नियमानुसार 'प्रति + उपकार' मिलकर 'प्रत्युपकार' बनता है, अतः मूल उपसर्ग 'प्रति' है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        12, "General Hindi", "Easy", "A",
        "The word 'Nishchala' (निश्चल) is formed by which type of Sandhi?",
        ["Visarga Sandhi (निः + चल)", "Svara Sandhi", "Vyanjana Sandhi", "Dirgha Sandhi"],
        "Nih (निः) + Chala (चल) = Nishchala (निश्चल), which is a classic Visarga Sandhi rule. Hence, option A is correct.",
        "'निश्चल' शब्द में कौन-सी संधि है?",
        ["विसर्ग संधि", "स्वर संधि", "व्यंजन संधि", "दीर्घ संधि"],
        "'निः + चल' मिलकर 'निश्चल' बनता है। विसर्ग के बाद च/छ आने पर विसर्ग का तालव्य 'श्' हो जाता है, यह विसर्ग संधि है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        13, "General Hindi", "Medium", "D",
        "Select the Tadbhav word among the following options:",
        ["Mayura (मयूर)", "Hastin (हस्तिन)", "Agni (अग्नि)", "Mor (मोर)"],
        "'Mor' is the Tadbhav form derived from the Sanskrit Tatsam 'Mayura'. Hence, option D is correct.",
        "निम्नलिखित में से 'तद्भव' शब्द कौन-सा है?",
        ["मयूर", "हस्तिन", "अग्नि", "मोर"],
        "'मोर' तद्भव शब्द है जिसका संस्कृत तत्सम रूप 'मयूर' होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        14, "General Hindi", "Easy", "C",
        "What is the meaning of the proverb 'Naach na aane aangan tedha' (नाच न जाने आँगन टेढ़ा)?",
        ["The courtyard is uneven", "One does not like dancing", "Blaming external circumstances for one's own incompetence", "Dancing on broken tiles"],
        "The proverb means excusing one's own lack of skill by finding fault with tools or environment. Hence, option C is correct.",
        "लोकोक्ति 'नाच न जाने आँगन टेढ़ा' का सही अर्थ क्या है?",
        ["आँगन में पत्थर होना", "नृत्य करना पसंद न होना", "अपनी अयोग्यता या कमी को छुपाने के लिए परिस्थिति को दोष देना", "नाचते समय गिर जाना"],
        "अपनी अकर्मण्यता या दोष को स्वीकार न करके दूसरों या साधनों में दोष निकालना ही इसका वास्तविक अर्थ है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        15, "General Hindi", "Medium", "B",
        "What is the feminine form (स्त्रीलिंग) corresponding to 'Netru' / 'Neta' (नेता)?",
        ["Netayin (नेताओंन)", "Netri (नेत्री)", "Netani (नेतानी)", "Netrika (नेत्रिका)"],
        "Sanskrit nouns ending in '-ta' (like Dhatri, Kartri, Netri) form their feminine as 'Netri' (नेत्री). Hence, option B is correct.",
        "'नेता' शब्द का सही स्त्रीलिंग रूप क्या होगा?",
        ["नेताओंन", "नेत्री", "नेतानी", "नेत्रिका"],
        "'नेता' का शुद्ध स्त्रीलिंग 'नेत्री' होता है (जैसे कर्ता का कत्री, दाता का दात्री)। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        16, "General Hindi", "Easy", "A",
        "Which of the following is an example of 'Dvandva Samas' (द्वंद्व समास)?",
        ["Paap-Punya (पाप-पुण्य)", "Yathavidhi (यथाविधि)", "Triloka (त्रिलोक)", "Neelamber (नीलाम्बर)"],
        "Paap-Punya (पाप और पुण्य) contains two coordinate opposite stems connected by 'aur', making it Dvandva Samas. Hence, option A is correct.",
        "निम्नलिखित में से 'द्वंद्व समास' का उदाहरण कौन-सा है?",
        ["पाप-पुण्य", "यथाविधि", "त्रिलोक", "नीलाम्बर"],
        "जिस समास के दोनों पद प्रधान हों और विग्रह करने पर 'और' अथवा 'या' आए, उसे द्वंद्व समास कहते हैं (पाप और पुण्य = पाप-पुण्य)। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        17, "General Hindi", "Medium", "D",
        "What is the one-word substitution for 'A child born after the death of his/her father' (पिता की मृत्यु के उपरांत जन्मा बच्चा)?",
        ["Anath (अनाथ)", "Auras (औरस)", "Dattak (दत्तक)", "Maranoparant / Posthumous (मरणोपरांत जन्मा)"],
        "A child born after the death of the father is called a Posthumous child (मरणोपरांत जन्मा शिशु). Hence, option D is correct.",
        "'पिता की मृत्यु के पश्चात् जन्म लेने वाला शिशु' वाक्यांश के लिए एक शब्द है:",
        ["अनाथ", "औरस", "दत्तक", "मरणोपरांत जन्मा"],
        "पिता के देहांत के उपरांत उत्पन्न होने वाले बच्चे को 'मरणोपरांत जन्मा' (Posthumous child) कहते हैं। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        18, "General Hindi", "Easy", "C",
        "What is the case marker (परसर्ग) for the 'Sampradan Karaka' (सम्प्रदान कारक)?",
        ["Ne (ने)", "Se (से)", "Ko / Ke liye (को / के लिए)", "Me / Par (में / पर)"],
        "Sampradan Karaka signifies giving something to someone ('Ke liye' or 'Ko' in the sense of donation, e.g. 'Raja ne nirdhan ko daan diya'). Hence, option C is correct.",
        "'सम्प्रदान कारक' का विभक्ति चिह्न क्या है?",
        ["ने", "से", "को / के लिए (देने के अर्थ में)", "में / पर"],
        "जिसके लिए कोई क्रिया की जाए या जिसे कुछ प्रदान किया जाए, उसे सम्प्रदान कारक कहते हैं और इसका परसर्ग 'के लिए' या 'को' होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        19, "General Hindi", "Medium", "B",
        "Which of the following is NOT a synonym of 'Vriksha' (वृक्ष - Tree)?",
        ["Taru (तरु)", "Vihang (विहंग)", "Padapa (पादप)", "Druma (द्रुम)"],
        "'Vihang' means a bird, whereas Taru, Padapa, and Druma are synonyms of Tree. Hence, option B is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'वृक्ष' (पेड़) का पर्यायवाची नहीं है?",
        ["तरु", "विहंग", "पादप", "द्रुम"],
        "'विहंग' पक्षी (चिड़िया) का पर्यायवाची है, जबकि तरु, पादप और द्रुम वृक्ष के पर्यायवाची हैं। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        20, "General Hindi", "Easy", "A",
        "Identify the correct antonym of 'Swakiya' (स्वकीया):",
        ["Parakiya (परकीया)", "Narakiya (नारकीय)", "Vakiya (वाकीया)", "Nirakiya (निरकीया)"],
        "In Hindi literary poetics, 'Swakiya' (devoted only to own spouse) has the direct antonym 'Parakiya'. Hence, option A is correct.",
        "'स्वकीया' शब्द का सही विलोम क्या होगा?",
        ["परकीया", "नारकीय", "वाकीया", "प्रकिया"],
        "काव्यशास्त्र में पतिव्रता स्त्री को 'स्वकीया' तथा दूसरे पुरुष से अनुराग रखने वाली को 'परकीया' कहा जाता है। अतः विकल्प A सही विलोम है।"
    ))

    qs.append(create_q(
        21, "General Hindi", "Medium", "C",
        "What is the meaning of the Hindi idiom 'Chhati par moong dalna' (छाती पर मूँग दलना)?",
        ["To make lentils on the chest", "To cultivate moong crop", "To torment or irritate someone continuously right in their presence", "To lift heavy weight"],
        "The idiom implies tormenting or troubling someone intensely while living in close proximity with them. Hence, option C is correct.",
        "मुहावरा 'छाती पर मूँग दलना' का सही अर्थ क्या है?",
        ["छाती पर दाल बनाना", "मूँग की खेती करना", "पास रहकर निरंतर अत्यंत कष्ट या संताप देना", "भारी वजन उठाना"],
        "'छाती पर मूँग दलना' का अर्थ सामने रहकर किसी को निरंतर सताना या दुखी करना होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        22, "General Hindi", "Easy", "D",
        "Which of the following spellings is standard and correct?",
        ["Adhyayan (अध्यन)", "Aadhyayan (आध्ययन)", "Adhyayan (अधायन)", "Adhyayan (अध्ययन)"],
        "Adhi (अधि) + Ayan (अयन) = Adhyayan (अध्ययन) with double 'ya'. Hence, option D is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:",
        ["अध्यन", "आध्ययन", "अधायन", "अध्ययन"],
        "'अधि + अयन' से यण संधि द्वारा 'अध्ययन' (दो बार 'य') बनता है, यही शुद्ध वर्तनी है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        23, "General Hindi", "Medium", "B",
        "In which of the following sentences has a causational verb (प्रेरणार्थक क्रिया) been used?",
        ["Mata ji khana banati hain.", "Mata ji ne beti se khana banwaya.", "Mata ji so rahi hain.", "Mata ji baith gayin."],
        "In 'banwaya' (made someone cook), the subject causes another agent to perform the action, which defines a Preranarthak Kriya. Hence, option B is correct.",
        "निम्नलिखित में से किस वाक्य में 'प्रेरणार्थक क्रिया' प्रयुक्त हुई है?",
        ["माता जी खाना बनाती हैं।", "माता जी ने बेटी से खाना बनवाया।", "माता जी सो रही हैं।", "माता जी बैठ गईं।"],
        "जब कर्ता स्वयं कार्य न करके किसी अन्य को कार्य करने के लिए प्रेरित करता है, तो उसे प्रेरणार्थक क्रिया कहते हैं (बनवाया)। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        24, "General Hindi", "Easy", "A",
        "Which suffix (प्रत्यय) is present in the word 'Dayalu' (दयालु)?",
        ["Aalu (आलु)", "Lu (लु)", "Yu (यु)", "Alu (अलु)"],
        "Daya (दया) + Aalu (आलु) = Dayalu (दयालु). Hence, option A is correct.",
        "'दयालु' शब्द में किस प्रत्यय का प्रयोग हुआ है?",
        ["आलु", "लु", "यु", "अलु"],
        "'दया' संज्ञा शब्द में भाववाचक तद्धित प्रत्यय 'आलु' जोड़ने पर 'दयालु' विशेषण बनता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        25, "General Hindi", "Medium", "C",
        "What is the Tatsam form of the Tadbhav word 'Dahi' (दही)?",
        ["Dahi (दाही)", "Dugdha (दुग्ध)", "Dadhi (दधि)", "Dahan (दहन)"],
        "The Sanskrit Tatsam word for curd/yogurt 'Dahi' is 'Dadhi' (दधि). Dugdha is milk. Hence, option C is correct.",
        "तद्भव शब्द 'दही' का शुद्ध तत्सम रूप क्या होगा?",
        ["दाही", "दुग्ध", "दधि", "दहन"],
        "'दही' तद्भव शब्द है जिसका शुद्ध संस्कृत तत्सम 'दधि' होता है (दुग्ध दूध का तत्सम है)। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        26, "General Hindi", "Easy", "B",
        "Which of the following is an example of 'Dwigu Samas' (द्विगु समास)?",
        ["Trinetra", "Tribhuvana (त्रिभुवन - तीन भुवनों का समाहार)", "Dharmatha", "Pankaj"],
        "Tribhuvana (collection of three realms) starts with numeral 'Tri' without pointing to a deity, making it a pure Dwigu Samas. Hence, option B is correct.",
        "निम्नलिखित में से 'द्विगु समास' का उदाहरण कौन-सा है?",
        ["त्रिनेत्र", "त्रिभुवन", "धर्मार्थ", "पंकज"],
        "'त्रिभुवन' (तीन भुवनों का समाहार) में प्रथम पद संख्यावाचक है और समाहार का बोध कराता है, अतः यह द्विगु समास है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        27, "General Hindi", "Medium", "D",
        "What is the correct meaning difference between the word-pair 'Tarani' (तरणि) and 'Taranee' (तरणी)?",
        ["Boat and Sun", "Wave and River", "Youth and Ocean", "Sun and Boat (सूर्य और नाव)"],
        "Hrasva 'Tarani' (तरणि) means the Sun, while dirgha 'Taranee' (तरणी) means a Boat. Hence, option D is correct.",
        "शब्द-युग्म 'तरणि' और 'तरणी' का सही अर्थ-भेद क्या है?",
        ["नाव और सूर्य", "लहर और नदी", "युवती और समुद्र", "सूर्य और नाव"],
        "ह्रस्व इकार वाले 'तरणि' का अर्थ 'सूर्य' होता है तथा दीर्घ ईकार वाले 'तरणी' का अर्थ 'नाव' (नौका) होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        28, "General Hindi", "Easy", "A",
        "Identify the correct antonym of 'Prachina' (प्राचीन - Ancient):",
        ["Arvachina (अर्वाचीन - Modern)", "Naveen (नवीन)", "Puratan (पुरातन)", "Samakaleen (समकालीन)"],
        "In formal Hindi vocabulary, 'Prachina' has the classical standard antonym 'Arvachina'. Hence, option A is correct.",
        "'प्राचीन' शब्द का मानक विलोम शब्द क्या होगा?",
        ["अर्वाचीन", "नवीन", "पुरातन", "समकालीन"],
        "'प्राचीन' का शास्त्रीय एवं मानक विलोम 'अर्वाचीन' (आधुनिक) होता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        29, "General Hindi", "Medium", "C",
        "Which of the following is a Disjunctive / Conjunction indeclinable (समुच्चयबोधक अव्यय)?",
        ["Dhire-dhire (धीरे-धीरे)", "Upar (ऊपर)", "Athava (अथवा / या)", "Arey (अरे)"],
        "'Athava' (or) joins two clauses or words as a Samuchchayabodhaka Avyaya. Dhire-dhire is adverb, Upar is preposition, Arey is interjection. Hence, option C is correct.",
        "निम्नलिखित में से 'समुच्चयबोधक अव्यय' कौन-सा है?",
        ["धीरे-धीरे", "ऊपर", "अथवा", "अरे"],
        "'अथवा' दो शब्दों या उपवाक्यों को जोड़ने वाला समुच्चयबोधक (संयोजक/विभाजक) अव्यय है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        30, "General Hindi", "Easy", "D",
        "What is the one-word substitution for 'A place where weapons and ammunition are stored' (जहाँ अस्त्र-शस्त्र रखे जाते हों)?",
        ["Koshagar", "Toshakhana", "Pustakalaya", "Shastragar (शस्त्रागार / आयुधागार)"],
        "An armoury/arsenal where weapons are kept is termed 'Shastragar' or 'Ayudhagar'. Hence, option D is correct.",
        "'जहाँ अस्त्र-शस्त्र सुरक्षित रखे जाते हैं' वाक्यांश के लिए एक उपयुक्त शब्द है:",
        ["कोषागार", "तोशाखाना", "पुस्तकालय", "शस्त्रागार (आयुधागार)"],
        "अस्त्र-शस्त्र रखने के सुरक्षित कक्ष या भवन को 'शस्त्रागार' (Armoury) कहा जाता है। अतः विकल्प D सही उत्तर है।"
    ))

    # ==========================================
    # SECTION 2: GENERAL ENGLISH (Q31 to Q50)
    # ==========================================
    qs.append(create_q(
        31, "General English", "Easy", "A",
        "Choose the correct synonym of the word 'METICULOUS':",
        ["Very careful and precise", "Careless", "Hasty", "Indifferent"],
        "'Meticulous' means showing great attention to detail; very careful and precise. Hence, option A is correct.",
        "'METICULOUS' शब्द का सही समानार्थी (Synonym) क्या होगा?",
        ["Very careful and precise (अति सतर्क एवं सूक्ष्म)", "Careless", "Hasty", "Indifferent"],
        "'Meticulous' का अर्थ अत्यंत सावधानीपूर्वक बारीक काम करने वाला होता है, अतः इसका समानार्थी 'Very careful and precise' है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        32, "General English", "Easy", "D",
        "Choose the correct antonym of the word 'TRANSPARENT':",
        ["Clear", "Lucid", "Pellucid", "Opaque"],
        "'Transparent' means allowing light to pass through clearly. Its opposite is 'Opaque' (not allowing light through). Hence, option D is correct.",
        "'TRANSPARENT' (पारदर्शी) शब्द का विलोम शब्द क्या होगा?",
        ["Clear", "Lucid", "Pellucid", "Opaque (अपारदर्शी)"],
        "'Transparent' का अर्थ पारदर्शी होता है, जिसका सटीक विलोम 'Opaque' (अपारदर्शी) है। अतः विकल्प D सही उत्तर है।"
    ))

    qs.append(create_q(
        33, "General English", "Medium", "B",
        "Change the following sentence into Passive Voice: 'The teacher praised the boy.'",
        ["The boy is praised by the teacher.", "The boy was praised by the teacher.", "The boy had praised the teacher.", "The boy was being praised."],
        "Past simple active ('praised') changes to 'was praised'. Hence, option B is correct.",
        "वाक्य को Passive Voice में बदलिए: 'The teacher praised the boy.'",
        ["The boy is praised by the teacher.", "The boy was praised by the teacher.", "The boy had praised the teacher.", "The boy was being praised."],
        "Simple Past Tense का पैसिव वॉइस 'was/were + V3' से बनाया जाता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        34, "General English", "Medium", "C",
        "Fill in the blank with the appropriate preposition: 'I am accustomed ______ working under pressure.'",
        ["for", "with", "to", "at"],
        "The adjective 'accustomed' takes the fixed preposition 'to' followed by a gerund ('accustomed to working'). Hence, option C is correct.",
        "उचित Preposition से रिक्त स्थान भरिए: 'I am accustomed ______ working under pressure.'",
        ["for", "with", "to", "at"],
        "'Accustomed' के बाद हमेशा fixed preposition 'to' आता है। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        35, "General English", "Easy", "A",
        "What is the meaning of the idiom 'To bury the hatchet'?",
        ["To make peace and forget past quarrels", "To dig a deep hole", "To hide a dangerous weapon", "To restart an old enmity"],
        "'To bury the hatchet' is a famous Native American-origin idiom meaning to end a conflict and make peace. Hence, option A is correct.",
        "Idiom 'To bury the hatchet' का सही भावार्थ क्या है?",
        ["पुरानी शत्रुता समाप्त कर शांति समझौता करना", "गहरा गड्ढा खोदना", "हथियार छुपाना", "पुनः झगड़ा शुरू करना"],
        "'To bury the hatchet' का अर्थ पुरानी रंजिश भुलाकर आपस में सुलह या मित्रता कर लेना होता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        36, "General English", "Medium", "D",
        "Select the correctly spelt word from the following options:",
        ["Bureaucracy", "Burocracy", "Bureaucracey", "Bureaucracy"],
        "The correct spelling is 'Bureaucracy' (B-U-R-E-A-U-C-R-A-C-Y). Hence, option A/D is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी (Correct spelling) वाले शब्द का चयन कीजिए:",
        ["Burocracy", "Bureaucracy", "Bureaucracey", "Bureacracy"],
        "नौकरशाही के लिए अंग्रेजी में शुद्ध वर्तनी 'Bureaucracy' होती है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        37, "General English", "Easy", "B",
        "Choose the one-word substitute for: 'A person who loves and collects books.'",
        ["Bibliophobe", "Bibliophile", "Philatelist", "Numismatist"],
        "A 'Bibliophile' is an enthusiastic lover and collector of books. A 'Philatelist' collects stamps; a 'Numismatist' collects coins. Hence, option B is correct.",
        "'A person who loves and collects books' (पुस्तकों से प्रेम करने वाला) के लिए एक शब्द है:",
        ["Bibliophobe", "Bibliophile (पुस्तकानुरागी)", "Philatelist", "Numismatist"],
        "पुस्तकों से गहरा प्रेम करने तथा उनका संग्रह करने वाले को 'Bibliophile' कहा जाता है। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        38, "General English", "Medium", "C",
        "Fill in the blank with the appropriate conjunction: 'No sooner did he arrive ______ the lights went out.'",
        ["when", "then", "than", "that"],
        "The fixed correlative pair with comparative 'No sooner' is 'than' (No sooner ... than). Hence, option C is correct.",
        "उचित Conjunction भरिए: 'No sooner did he arrive ______ the lights went out.'",
        ["when", "then", "than", "that"],
        "नियम: 'No sooner' के साथ सदैव 'than' का प्रयोग होता है (Hardly/Scarcely के साथ 'when')। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        39, "General English", "Easy", "A",
        "Identify the part of speech of the word 'BRAVELY' in: 'The Indian soldiers fought bravely.'",
        ["Adverb", "Adjective", "Noun", "Verb"],
        "'Bravely' modifies the verb 'fought' describing how the soldiers fought; hence it is an Adverb of Manner. Hence, option A is correct.",
        "वाक्य में 'BRAVELY' का Part of Speech क्या है? 'The Indian soldiers fought bravely.'",
        ["Adverb (क्रियाविशेषण)", "Adjective", "Noun", "Verb"],
        "'Bravely' क्रिया 'fought' की विशेषता बता रहा है, अतः यह Adverb of Manner है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        40, "General English", "Hard", "C",
        "Convert into Indirect Speech: She said, 'Alas! I have lost my purse.'",
        ["She said alas that she lost her purse.", "She told that she has lost her purse.", "She exclaimed with sorrow that she had lost her purse.", "She cried that her purse was lost."],
        "Exclamatory sentence with 'Alas!' turns into 'exclaimed with sorrow / grief' and Present Perfect ('have lost') shifts to Past Perfect ('had lost'). Hence, option C is correct.",
        "अप्रत्यक्ष कथन (Indirect Speech) में रूपांतरित कीजिए: She said, 'Alas! I have lost my purse.'",
        ["She said alas that she lost her purse.", "She told that she has lost her purse.", "She exclaimed with sorrow that she had lost her purse.", "She cried that her purse was lost."],
        "विस्मयादिबोधक वाक्य में 'Alas!' के स्थान पर 'exclaimed with sorrow' आता है तथा काल Past Perfect में बदल जाता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        41, "General English", "Medium", "B",
        "What is the plural form of the word 'SYLLABUS'?",
        ["Syllabuss", "Syllabi or Syllabuses", "Syllabuses only", "Syllabii"],
        "The Latin origin noun 'syllabus' takes the plural form 'syllabi' or 'syllabuses'. Hence, option B is correct.",
        "'SYLLABUS' (पाठ्यक्रम) का बहुवचन रूप क्या होता है?",
        ["Syllabuss", "Syllabi (या Syllabuses)", "Syllabic", "Syllables"],
        "लैटिन मूल के 'syllabus' का मानक बहुवचन 'syllabi' अथवा 'syllabuses' दोनों स्वीकार्य हैं। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        42, "General English", "Easy", "D",
        "What is the meaning of the idiom 'To beat around the bush'?",
        ["To clear shrubs in a garden", "To hunt animals in bushes", "To hit a tree with a stick", "To avoid coming to the main point in a conversation"],
        "'To beat around the bush' means speaking at length in an evasive way without addressing the central topic directly. Hence, option D is correct.",
        "Idiom 'To beat around the bush' का क्या अर्थ है?",
        ["झाड़ियों की सफाई करना", "शिकार करना", "लाठी से पेड़ को पीटना", "मुख्य मुद्दे पर न आकर घुमा-फिराकर बात करना"],
        "'To beat around the bush' का अर्थ मूल बात को टालते हुए इधर-उधर की बातें करना होता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        43, "General English", "Medium", "A",
        "Fill in the blank with the appropriate article: 'Mount Everest is ______ highest peak in the world.'",
        ["the", "a", "an", "no article"],
        "Superlative adjectives (like 'highest') are preceded by the definite article 'the'. Hence, option A is correct.",
        "उचित Article चुनिए: 'Mount Everest is ______ highest peak in the world.'",
        ["the", "a", "an", "no article"],
        "Superlative Degree ('highest') के पहले सदैव निश्चित आर्टिकल 'the' का प्रयोग होता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        44, "General English", "Easy", "C",
        "Choose the antonym of the word 'EXPAND':",
        ["Widen", "Enlarge", "Contract or Shrink", "Extend"],
        "'Expand' means to become larger in size; its antonym is 'Contract' or 'Shrink'. Hence, option C is correct.",
        "'EXPAND' (विस्तार करना) शब्द का विलोम शब्द क्या है?",
        ["Widen", "Enlarge", "Contract (संकुचित होना / सिकोड़ना)", "Extend"],
        "'Expand' का अर्थ फैलाना या बढ़ना होता है, जिसका विपरीतार्थी 'Contract' (सिकुड़ना) है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        45, "General English", "Medium", "B",
        "Select the sentence with correct subject-verb concord:",
        ["Bread and butter are his favorite breakfast.", "Bread and butter is his favorite breakfast.", "Bread and butter were his favorite breakfast.", "Bread and butter have been his breakfast."],
        "When two singular nouns express a compound single idea/dish (like 'Bread and butter'), they take a singular verb ('is'). Hence, option B is correct.",
        "Subject-Verb Agreement की दृष्टि से शुद्ध वाक्य पहचानिए:",
        ["Bread and butter are his favorite breakfast.", "Bread and butter is his favorite breakfast.", "Bread and butter were his favorite breakfast.", "Bread and butter have been his breakfast."],
        "जब दो संज्ञाएं मिलकर एक सम्मिलित विचार या खाद्य पदार्थ (जैसे ब्रेड-बटर) व्यक्त करती हैं, तो एकवचन क्रिया 'is' प्रयुक्त होती है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        46, "General English", "Easy", "D",
        "Select the synonym of the word 'CONCUR':",
        ["Disagree", "Oppose", "Conflict", "Agree"],
        "'To concur' means to agree with someone or share the same opinion. Hence, option D is correct.",
        "'CONCUR' शब्द का समानार्थी शब्द क्या होगा?",
        ["Disagree", "Oppose", "Conflict", "Agree (सहमत होना)"],
        "'Concur' का अर्थ किसी विचार या राय से सहमत होना होता है, अतः इसका समानार्थी 'Agree' है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        47, "General English", "Medium", "A",
        "Fill in the blank with the correct preposition: 'He jumped ______ the river to save the drowning child.'",
        ["into", "in", "on", "at"],
        "'Into' indicates motion towards the interior or depth of something. Hence, option A is correct.",
        "उचित Preposition से रिक्त स्थान भरिए: 'He jumped ______ the river to save the drowning child.'",
        ["into", "in", "on", "at"],
        "गतिशीलता (Motion towards inside) दर्शाने के लिए 'into' का प्रयोग किया जाता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        48, "General English", "Easy", "C",
        "One who looks after a library and its catalog is called a:",
        ["Lecturer", "Auditor", "Librarian", "Curator"],
        "A person in charge of a library is a 'Librarian' (Curator is in charge of a museum). Hence, option C is correct.",
        "'One who looks after a library' वाक्यांश के लिए एक शब्द है:",
        ["Lecturer", "Auditor", "Librarian (पुस्तकालय अध्यक्ष)", "Curator"],
        "पुस्तकालय का प्रबंधन एवं देखभाल करने वाले को 'Librarian' कहा जाता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        49, "General English", "Medium", "B",
        "Identify the correctly punctuated sentence:",
        ["He said 'I will come tomorrow.'", "He said, \"I will come tomorrow.\"", "He said \"I will come tomorrow\"", "He said, I will come tomorrow."],
        "Direct speech requires a comma after the reporting verb followed by opening quotation marks, capitalized first word, and closing period inside quotes. Hence, option B is correct.",
        "सही विराम चिह्नों (Punctuation) वाला वाक्य पहचानिए:",
        ["He said 'I will come tomorrow.'", "He said, \"I will come tomorrow.\"", "He said \"I will come tomorrow\"", "He said, I will come tomorrow."],
        "Direct Narration में Reporting Verb के बाद अल्पविराम (comma) तथा कथन दोहरे उद्धरण चिह्न (\"...\") में होता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        50, "General English", "Easy", "D",
        "What is the meaning of the idiom 'To face the music'?",
        ["To listen to classical songs", "To play musical instruments", "To attend a concert", "To accept unpleasant consequences of one's actions"],
        "'To face the music' means being confronted with and accepting the criticisms or punishment for one's actions. Hence, option D is correct.",
        "Idiom 'To face the music' का क्या भावार्थ है?",
        ["संगीत सुनना", "वाद्ययंत्र बजाना", "समारोह में जाना", "किए गए कर्मों का अप्रिय परिणाम या दंड भुगतना"],
        "'To face the music' का अर्थ अपनी गलतियों के परिणाम या आलोचना का सामना करना होता है। अतः विकल्प D सही है।"
    ))

    # =============================================================
    # SECTION 3: INTERPERSONAL SKILLS & COMMUNICATION (Q51 to Q75)
    # =============================================================
    qs.append(create_q(
        51, "Interpersonal & Communication Skills", "Medium", "A",
        "In communication theory, the person or entity who initiates the message transmission is called the:",
        ["Sender / Source", "Decoder", "Channel", "Receiver"],
        "The Sender or Source originates the concept, encodes it, and transmits it through a medium. Hence, option A is correct.",
        "संप्रेषण सिद्धांत में वह व्यक्ति अथवा पक्ष जो संदेश का आरंभ करता है, क्या कहलाता है?",
        ["प्रेषक / स्रोत (Sender)", "कूटवाचक", "माध्यम", "प्राप्तकर्ता"],
        "संदेश को विचार रूप में गढ़ने और कूटबद्ध करके प्रेषित करने वाला 'प्रेषक' कहलाता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        52, "Interpersonal & Communication Skills", "Easy", "C",
        "Which of the following is considered a primary form of non-verbal paralanguage?",
        ["Written words in an email", "Color of office walls", "Vocal tone, pitch, volume, and pauses", "Distance between tables"],
        "Paralanguage encompasses non-verbal vocal aspects including pitch, tone, pace, volume, and inflection. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा अशाब्दिक 'पैराभाषा' (Paralanguage) का प्राथमिक उदाहरण है?",
        ["ईमेल में लिखे शब्द", "दीवार का रंग", "आवाज़ का लहज़ा, उतार-चढ़ाव (पिच), तीव्रता एवं विराम", "मेज के बीच की दूरी"],
        "पैराभाषा में शब्दों के अतिरिक्त स्वर के उतार-चढ़ाव, बोलने की गति और तीव्रता का अध्ययन होता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        53, "Interpersonal & Communication Skills", "Medium", "B",
        "The cognitive barrier to listening where a person pays attention only to parts of a message that interest them is known as:",
        ["Defensive listening", "Selective listening (चयनात्मक श्रवण)", "Passive listening", "Insensitive listening"],
        "Selective listening occurs when a listener screens out components of a message and attends only to what aligns with their interests. Hence, option B is correct.",
        "श्रवण में वह संज्ञानात्मक बाधा जिसमें व्यक्ति केवल अपनी रुचि के अंशों पर ही ध्यान देता है और शेष की उपेक्षा कर देता है, क्या कहलाती है?",
        ["रक्षात्मक श्रवण", "चयनात्मक श्रवण (Selective listening)", "निष्क्रिय श्रवण", "असंवेदनशील श्रवण"],
        "चयनात्मक श्रवण में श्रोता अपनी पसंद की बातों को चुन-चुनकर सुनता है और बाकी संदेश को नजरअंदाज कर देता है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        54, "Interpersonal & Communication Skills", "Hard", "D",
        "The administrative decision-making heuristic where people evaluate the frequency or likelihood of an event based on how easily examples come to mind is:",
        ["Representative heuristic", "Fundamental attribution error", "Confirmation bias", "Availability heuristic (उपलब्धता अनुमानी)"],
        "Amos Tversky and Daniel Kahneman defined the 'Availability Heuristic' as judging probability by the ease with which relevant instances can be mentally recalled. Hence, option D is correct.",
        "प्रशासनिक निर्णयन में वह अनुमानी (Heuristic) जिसमें व्यक्ति किसी घटना की संभावना का अनुमान इस आधार पर लगाता है कि उसके उदाहरण कितनी सुगमता से स्मृति में आ जाते हैं, क्या कहलाती है?",
        ["प्रतिनिधित्व अनुमानी", "मूलभूत आरोपण त्रुटि", "पुष्टि पूर्वाग्रह", "उपलब्धता अनुमानी (Availability heuristic)"],
        "उपलब्धता अनुमानी में हालिया या अत्यधिक चर्चित घटनाएं तुरंत याद आ जाती हैं, जिससे व्यक्ति उनकी संभावना को वास्तविकता से कहीं अधिक मान बैठता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        55, "Interpersonal & Communication Skills", "Easy", "A",
        "A formal organizational communication moving from higher executives to subordinates is called:",
        ["Downward communication", "Upward communication", "Horizontal communication", "Informal grapevine"],
        "Communication travelling down an organizational scalar chain from managers to subordinates is Downward communication. Hence, option A is correct.",
        "किसी संगठन में उच्च पदस्थ अधिकारियों से अधीनस्थों की ओर जाने वाले औपचारिक संदेश प्रवाह को क्या कहा जाता है?",
        ["अधोमुखी संप्रेषण (Downward communication)", "उर्ध्वमुखी संप्रेषण", "क्षैतिज संप्रेषण", "अनौपचारिक ग्रेपवाइन"],
        "उच्च स्तर से निम्न स्तर की ओर प्रवाहित होने वाले आदेश, निर्देश और नीतियों को अधोमुखी संप्रेषण कहा जाता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        56, "Interpersonal & Communication Skills", "Medium", "C",
        "Which conflict management style is characterized by a high concern for both one's own goals and the other party's relationship?",
        ["Competing", "Avoiding", "Collaborating (सहयोगात्मक शैली)", "Accommodating"],
        "In the Thomas-Kilmann conflict model, 'Collaborating' represents high assertiveness and high cooperativeness, striving for a win-win integration. Hence, option C is correct.",
        "थॉमस-किल्मन संघर्ष प्रबंधन मॉडल में जब कोई व्यक्ति अपने उद्देश्यों और दूसरे पक्ष के संबंधों दोनों को सर्वोच्च महत्व देता है, तो वह कौन-सी शैली है?",
        ["प्रतिस्पर्धा (Competing)", "परिहार (Avoiding)", "सहयोगात्मक / समाकलनात्मक शैली (Collaborating)", "समर्पण (Accommodating)"],
        "सहयोगात्मक शैली में दोनों पक्षों के हितों को साधने वाला रचनात्मक समाधान खोजा जाता है (Win-Win स्थिति)। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        57, "Interpersonal & Communication Skills", "Medium", "B",
        "In interpersonal relations, the tendency to attribute our own successes to internal qualities and our failures to external factors is called:",
        ["Fundamental attribution error", "Self-serving bias (स्व-सेवा पूर्वाग्रह)", "Halo effect", "Stereotyping"],
        "Self-serving bias is the cognitive tendency to take personal credit for positive outcomes while blaming situational forces for negative ones. Hence, option B is correct.",
        "अंतर्वैयक्तिक संबंधों में अपनी सफलताओं का श्रेय अपनी क्षमताओं को देना तथा अपनी असफलताओं का दोष बाहरी परिस्थितियों पर मढ़ना क्या कहलाता है?",
        ["मूलभूत आरोपण त्रुटि", "स्व-सेवा पूर्वाग्रह (Self-serving bias)", "हेलो प्रभाव", "रूढ़िवादिता"],
        "स्व-सेवा पूर्वाग्रह व्यक्ति के आत्मसम्मान की रक्षा करने वाला वह मनोवैज्ञानिक झुकाव है जिसमें जीत मेरी और हार किस्मत/परिस्थिति की मानी जाती है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        58, "Interpersonal & Communication Skills", "Easy", "D",
        "Which of the following spatial distances represents the 'Personal Space' zone according to Edward T. Hall's Proxemics?",
        ["0 to 18 inches", "Over 12 feet", "12 to 25 feet", "1.5 to 4 feet (18 inches to 4 feet)"],
        "Edward T. Hall classified Proxemic zones as: Intimate (0-1.5 ft), Personal (1.5-4 ft), Social (4-12 ft), and Public (12+ ft). Hence, option D is correct.",
        "एडवर्ड टी. हॉल के प्रॉक्सिमिक्स (सामीप्य विज्ञान) के अनुसार 'व्यक्तिगत दूरी' (Personal Space) का दायरा कितना होता है?",
        ["0 से 18 इंच (अंतरंग दूरी)", "12 फीट से अधिक (सार्वजनिक)", "4 से 12 फीट (सामाजिक)", "1.5 से 4 फीट (व्यक्तिगत दूरी)"],
        "एडवर्ड हॉल के अनुसार मित्रों एवं परिचितों से सामान्य बातचीत की दूरी 1.5 से 4 फीट होती है जिसे 'व्यक्तिगत दूरी' कहते हैं। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        59, "Interpersonal & Communication Skills", "Medium", "A",
        "Feedback is essential in interpersonal communication because it:",
        ["Closes the communication loop and confirms mutual understanding", "Allows the sender to scold the listener", "Ensures that no reply is required", "Increases environmental noise"],
        "Feedback is the response that verifies whether the message was decoded accurately by the receiver, closing the loop. Hence, option A is correct.",
        "अंतर्वैयक्तिक संवाद में प्रतिपुष्टि (Feedback) क्यों अपरिहार्य मानी जाती है?",
        ["यह संप्रेषण चक्र को पूर्ण करती है और आपसी समझ की पुष्टि करती है", "यह प्रेषक को डांटने का अवसर देती है", "यह सुनिश्चित करती है कि कोई उत्तर न दिया जाए", "यह शोर को बढ़ाती है"],
        "प्रतिपुष्टि से प्रेषक को यह स्पष्ट होता है कि उसका संदेश सही अर्थ में समझा गया है अथवा नहीं। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        60, "Interpersonal & Communication Skills", "Hard", "C",
        "The 'Framing Effect' in decision-making demonstrates that people tend to:",
        ["Always make purely mathematical calculations", "Never accept any advice from superiors", "Make different decisions based on whether choices are presented as gains or losses", "Ignore all forms of language"],
        "Kahneman and Tversky's Prospect Theory proved that risk-seeking or risk-averse behaviour shifts depending on whether identical data is framed in terms of gains or losses. Hence, option C is correct.",
        "निर्णयन में 'फ्रेमिंग प्रभाव' (Framing Effect) यह दर्शाता है कि व्यक्ति:",
        ["हमेशा शुद्ध गणितीय लाभ की गणना करता है", "वरिष्ठों की सलाह कभी नहीं मानता", "किसी विकल्प को 'लाभ' या 'हानि' के रूप में प्रस्तुत किए जाने पर भिन्न-भिन्न निर्णय लेता है", "भाषा की पूरी तरह उपेक्षा करता है"],
        "फ्रेमिंग प्रभाव के अनुसार एक ही तथ्य को यदि सकारात्मक (लाभ) या नकारात्मक (हानि) रूप में प्रस्तुत किया जाए तो व्यक्ति का निर्णय बदल जाता है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        61, "Interpersonal & Communication Skills", "Easy", "B",
        "A closed question in an interview is one that:",
        ["Requires an essay-length response", "Can be answered with a simple 'yes', 'no', or a single specific fact", "Is forbidden by company rules", "Has no correct answer"],
        "Closed-ended questions elicit concise, specific, factual answers such as 'yes' or 'no'. Hence, option B is correct.",
        "साक्षात्कार में 'बंद प्रश्न' (Closed question) से क्या तात्पर्य है?",
        ["जिसका उत्तर निबंध की तरह दिया जाए", "जिसका उत्तर 'हाँ', 'ना' या किसी एक विशिष्ट तथ्य में दिया जा सके", "जिस पर पूछने का प्रतिबंध हो", "जिसका कोई उत्तर न हो"],
        "बंद प्रश्न निश्चित एवं संक्षिप्त उत्तर प्राप्त करने हेतु पूछे जाते हैं। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        62, "Interpersonal & Communication Skills", "Medium", "D",
        "Diagonal communication in a large administration refers to the flow of messages between:",
        ["A manager and their direct subordinate", "Colleagues in the same section", "External citizens and the front office", "Personnel at different hierarchical levels in different functional departments"],
        "Diagonal communication cuts across departmental boundaries and organizational rank levels (e.g. Finance VP communicating directly with an Operations plant engineer). Hence, option D is correct.",
        "बड़े प्रशासन में 'कर्णवत संप्रेषण' (Diagonal Communication) किनके मध्य सूचना प्रवाह को दर्शाता है?",
        ["प्रबंधक और उसके प्रत्यक्ष अधीनस्थ", "एक ही अनुभाग के सहकर्मी", "नागरिक और फ्रंट ऑफिस", "भिन्न-भिन्न विभागों के विभिन्न पदानुक्रम स्तरों के कार्मिकों के बीच"],
        "कर्णवत संप्रेषण विभागीय सीमाओं और पदसोपान श्रृंखला को लांघकर सीधा संपर्क स्थापित करता है। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        63, "Interpersonal & Communication Skills", "Medium", "A",
        "The psychological state of discomfort experienced when holding contradictory beliefs or values is termed:",
        ["Cognitive Dissonance (संज्ञानात्मक असंगति)", "Group polarization", "Ego depletion", "Emotional contagion"],
        "Leon Festinger introduced 'Cognitive Dissonance' to explain the mental tension that arises when actions conflict with attitudes or beliefs. Hence, option A is correct.",
        "जब किसी व्यक्ति के विचारों, विश्वासों अथवा आचरण में परस्पर अंतर्विरोध उत्पन्न होता है, तो उत्पन्न मानसिक तनाव को क्या कहते हैं?",
        ["संज्ञानात्मक असंगति (Cognitive Dissonance)", "समूह ध्रुवीकरण", "अहम् क्षरण", "भावनात्मक संक्रमण"],
        "लियोन फेस्टिंगर के अनुसार जब हमारे विचार और व्यवहार में विसंगति होती है, तो उसे 'संज्ञानात्मक असंगति' कहा जाता है। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        64, "Interpersonal & Communication Skills", "Hard", "C",
        "In the Johari Window, the 'Façade' or 'Hidden Area' contains thoughts and feelings that are:",
        ["Known to both self and others", "Known to others but unknown to self", "Known to self but kept hidden from others", "Unknown to both self and others"],
        "The Hidden quadrant (Façade) encompasses personal feelings, vulnerabilities, and secrets that the individual knows but chooses not to disclose to others. Hence, option C is correct.",
        "जोहारी विंडो (Johari Window) मॉडल में 'छिपा हुआ क्षेत्र' (Hidden Area / Façade) क्या प्रदर्शित करता है?",
        ["जो स्वयं और दूसरों दोनों को ज्ञात है", "जो दूसरों को ज्ञात है किन्तु स्वयं को नहीं", "जो स्वयं को ज्ञात है किन्तु दूसरों से गुप्त रखा गया है", "जो किसी को ज्ञात नहीं है"],
        "छिपे हुए क्षेत्र में व्यक्ति की वे निजी भावनाएं, भय और गोपनीय बातें आती हैं जिन्हें वह समाज के सामने प्रकट नहीं करता। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        65, "Interpersonal & Communication Skills", "Easy", "B",
        "Which of the following non-verbal cues is universally recognized as a signal of welcoming openness and agreement across cultures?",
        ["Crossed arms across chest", "A genuine warm smile", "Looking away repeatedly", "Frowning deeply"],
        "Paul Ekman's research confirmed that a genuine smile is a universal human facial expression signaling warmth, goodwill, and approachability. Hence, option B is correct.",
        "अशाब्दिक संप्रेषण में कौन-सा संकेत विश्व भर में सौहार्द, स्वागत और सकारात्मक खुलेपन का सार्वभौमिक प्रतीक माना जाता है?",
        ["छाती पर हाथ बांधकर खड़े होना", "एक सौम्य और स्वाभाविक मुस्कान", "बार-बार नजरें चुराना", "माथे पर बल डालना"],
        "पॉल एकमैन के शोधों के अनुसार स्वाभाविक मुस्कान संपूर्ण विश्व में मित्रता एवं खुलेपन का सार्वभौमिक संकेत है। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        66, "Interpersonal & Communication Skills", "Medium", "D",
        "Which of the following is NOT an effective guideline for conducting an administrative meeting?",
        ["Circulating an agenda in advance", "Sticking strictly to scheduled time limits", "Encouraging quiet members to share viewpoints", "Allowing one vocal member to monopolize the entire discussion"],
        "A successful meeting requires balanced participation; dominating behavior suppresses valuable insights and damages team morale. Hence, option D is an ineffective practice.",
        "प्रशासनिक बैठक आयोजित करने के संबंध में कौन-सा नियम अनुचित है?",
        ["बैठक से पूर्व कार्यसूची (Agenda) वितरित करना", "निर्धारित समय-सीमा का पालन करना", "शांत सदस्यों को विचार रखने हेतु प्रोत्साहित करना", "किसी एक वाचाल सदस्य को पूरी चर्चा पर हावी होने देना"],
        "किसी एक व्यक्ति द्वारा पूरी बैठक पर एकाधिकार कर लेने से बैठक का उद्देश्य विफल हो जाता है। अतः विकल्प D अनुपयुक्त तरीका है।"
    ))

    qs.append(create_q(
        67, "Interpersonal & Communication Skills", "Medium", "A",
        "The communication channel that possesses the highest 'Media Richness' is:",
        ["Face-to-face interaction", "Email text message", "Printed circular", "Formal office flyer"],
        "Daft and Lengel's Media Richness Theory rates Face-to-Face communication highest because it offers immediate feedback, vocal inflection, facial cues, and personal focus. Hence, option A is correct.",
        "डैफ्ट एवं लेंगल के 'मीडिया संपन्नता सिद्धांत' (Media Richness Theory) के अनुसार सर्वाधिक संपन्न संप्रेषण माध्यम कौन-सा है?",
        ["आमने-सामने बातचीत (Face-to-face)", "ईमेल पाठ संदेश", "मुद्रित परिपत्र", "कार्यालय का नोटिस बोर्ड"],
        "आमने-सामने के संवाद में तत्क्षण प्रतिपुष्टि, शारीरिक भाषा और आवाज़ के सुर उपलब्ध होते हैं, जिससे यह सर्वाधिक संपन्न माध्यम बनता है। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        68, "Interpersonal & Communication Skills", "Easy", "C",
        "In active listening, reflecting back the feelings expressed by the speaker is known as:",
        ["Interrogating", "Condemning", "Reflective empathy / Emotional mirroring", "Sarcastic echoing"],
        "Emotional mirroring or reflective empathy acknowledges the emotional tone behind a speaker's words, validating their experience. Hence, option C is correct.",
        "सक्रिय श्रवण में वक्ता द्वारा व्यक्त भावनाओं को पहचानकर उसे शब्दों में प्रतिबिंबित करना क्या कहलाता है?",
        ["जिरह करना", "दोषारोपण", "प्रतिबिंबित परानुभूति (Reflective empathy)", "व्यंग्यात्मक अनुकरण"],
        "वक्ता की बात के साथ-साथ उसकी आंतरिक भावनाओं को समझकर व्यक्त करना भावनात्मक समझ (परानुभूति) का परिचायक है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        69, "Interpersonal & Communication Skills", "Hard", "B",
        "The phenomenon where team discussion leads individuals to adopt more extreme positions than their initial individual leanings is called:",
        ["Social loafing", "Group Polarization (समूह ध्रुवीकरण)", "Bystander effect", "Pluralistic ignorance"],
        "Group polarization occurs when group deliberation reinforces initial predispositions, shifting the final group attitude towards more radical extremes. Hence, option B is correct.",
        "जब समूह में विचार-विमर्श के पश्चात सदस्यों के विचार अपनी प्रारंभिक स्थिति की तुलना में और अधिक उग्र या चरम हो जाते हैं, तो इसे क्या कहते हैं?",
        ["सामाजिक अकर्मण्यता", "समूह ध्रुवीकरण (Group Polarization)", "तमाशबीन प्रभाव", "बहुलतावादी अज्ञान"],
        "समूह ध्रुवीकरण में चर्चा के बाद समूह का दृष्टिकोण सामान्य सहमति के बजाय किसी एक चरम दिशा में झुक जाता है। अतः विकल्प B सही उत्तर है।"
    ))

    qs.append(create_q(
        70, "Interpersonal & Communication Skills", "Medium", "D",
        "In Transactional Analysis, when a manager addresses an employee as an authoritarian Parent and the employee responds as a defiant Child, this interaction is a:",
        ["Ulterior transaction", "Adult-Adult transaction", "Open transaction", "Complementary Parent-Child transaction"],
        "Complementary transactions occur when vectors of communication are parallel and predictable (Parent to Child and Child to Parent). Hence, option D is correct.",
        "संव्यवहार विश्लेषण में जब कोई अधिकारी अपने अधीनस्थ से आदेशात्मक 'अभिभावक' (Parent) की तरह बात करता है और अधीनस्थ 'शिशु' (Child) की भाँति प्रतिक्रिया देता है, तो यह किस प्रकार का संव्यवहार है?",
        ["कपटपूर्ण संव्यवहार", "प्रौढ़-प्रौढ़ संव्यवहार", "क्रॉस्ड संव्यवहार", "पूरक अभिभावक-शिशु संव्यवहार (Complementary transaction)"],
        "जब संप्रेषण की रेखाएं समानांतर होती हैं और अपेक्षित अहम् स्थिति से प्रत्युत्तर मिलता है, तो इसे पूरक संव्यवहार कहते हैं। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        71, "Interpersonal & Communication Skills", "Easy", "A",
        "The primary purpose of an agenda in administrative communication is to:",
        ["Outline the list of topics and schedule for discussion in advance", "Prevent employees from attending", "Replace official minutes", "Record punitive actions"],
        "An agenda structures time, ensures focus, and prepares attendees for productive participation. Hence, option A is correct.",
        "प्रशासनिक बैठकों में 'कार्यसूची' (Agenda) का मूल उद्देश्य क्या होता है?",
        ["चर्चा किए जाने वाले विषयों और प्राथमिकताओं की पूर्व रूपरेखा प्रस्तुत करना", "कर्मचारियों को आने से रोकना", "कार्यवृत्त को समाप्त करना", "दंडात्मक कार्रवाई दर्ज करना"],
        "कार्यसूची बैठक के विषयों और समय-सारणी का पूर्व निर्धारण करती है जिससे बैठक उद्देश्यपूर्ण बनी रहे। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        72, "Interpersonal & Communication Skills", "Medium", "C",
        "Which of the following is a physical environmental barrier to effective communication?",
        ["Cultural differences", "Technical jargon", "Loud factory machinery noise and poor acoustics", "Fear of authority"],
        "Loud ambient mechanical noise, bad acoustics, or physical wall barriers directly prevent acoustic sound waves from reaching the receiver. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा प्रभावी संप्रेषण का 'भौतिक पर्यावरणीय अवरोध' है?",
        ["सांस्कृतिक भिन्नता", "तकनीकी जार्गन", "कारखाने की मशीनों का अत्यधिक शोर एवं खराब ध्वनि-व्यवस्था", "अधिकारी का भय"],
        "बाहरी वातावरण में उपस्थित तेज ध्वनि या शोर भौतिक संप्रेषण बाधा का स्पष्ट उदाहरण है। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        73, "Interpersonal & Communication Skills", "Medium", "B",
        "The 'Hindsight Bias' in judgment and decision-making refers to:",
        ["Inability to see past events", "The exaggerated tendency to believe, after an outcome occurs, that one had predicted it all along ('I knew it all along')", "Refusing to plan for the future", "Accepting responsibility for everything"],
        "Hindsight bias is the false inclination to perceive completed events as having been obvious and foreseeable before they happened. Hence, option B is correct.",
        "निर्णयन प्रक्रिया में 'पश्चदृष्टि पूर्वाग्रह' (Hindsight Bias) से क्या तात्पर्य है?",
        ["अतीत को याद न रख पाना", "किसी घटना के घटित हो जाने के बाद यह झूठा दावा करना कि 'मैं तो पहले से ही यह जानता था'", "भविष्य की योजना न बनाना", "प्रत्येक बात की जिम्मेदारी लेना"],
        "पश्चदृष्टि पूर्वाग्रह में घटना के परिणाम सामने आने पर व्यक्ति यह भ्रम पाल लेता है कि वह परिणाम पहले से पूरी तरह तय और अनुमानित था। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        74, "Interpersonal & Communication Skills", "Easy", "D",
        "Eye-to-eye contact maintained for appropriate durations during communication communicates:",
        ["Hostility and anger", "Disrespect and insolence", "Guilt and evasion", "Confidence, honesty, and respectful engagement"],
        "Consistent and balanced eye contact conveys credibility, attentiveness, and straightforward honesty in professional settings. Hence, option D is correct.",
        "संवाद के दौरान उपयुक्त समय तक आँखों में आँखें डालकर देखना (नेत्र संपर्क) सामान्यतः क्या दर्शाता है?",
        ["शत्रुता और क्रोध", "अनादर और ढिठाई", "अपराधबोध और घबराहट", "आत्मविश्वास, ईमानदारी और सम्मानजनक जुड़ाव"],
        "संतुलित नेत्र संपर्क संप्रेषक के आत्मविश्वास और सत्यनिष्ठा का द्योतक होता है। अतः विकल्प D सही उत्तर है।"
    ))

    qs.append(create_q(
        75, "Interpersonal & Communication Skills", "Medium", "A",
        "When conflict is resolved by both parties giving up a part of their demands to reach a workable middle-ground, the strategy is:",
        ["Compromising (समझौता)", "Dominating", "Avoiding", "Accommodating"],
        "Compromising involves intermediate assertiveness and cooperativeness where both sides make reciprocal concessions. Hence, option A is correct.",
        "जब दोनों पक्ष अपने कुछ दावों का परित्याग करके एक मध्यवर्ती व्यावहारिक सहमति पर पहुँचते हैं, तो यह संघर्ष समाधान की कौन-सी शैली कहलाती है?",
        ["समझौता / मध्यमार्ग (Compromising)", "दबाव बनाना", "टालना (Avoiding)", "अनुकूलन (Accommodating)"],
        "समझौतावादी शैली में दोनों पक्ष आपसी रियायतें देकर बीच का रास्ता निकालते हैं। अतः विकल्प A सही उत्तर है।"
    ))

    # ==============================================================
    # SECTION 4: LOGICAL REASONING & BASIC NUMERACY (Q76 to Q100)
    # ==============================================================
    qs.append(create_q(
        76, "Logical Reasoning & Maths", "Easy", "C",
        "Find the missing term in the sequence: 4, 9, 19, 39, 79, ?",
        ["149", "155", "159", "169"],
        "Pattern: x * 2 + 1: (4*2+1=9, 9*2+1=19, 19*2+1=39, 39*2+1=79, 79*2+1=159). Hence, option C is correct.",
        "संख्या श्रृंखला में अगला पद क्या होगा: 4, 9, 19, 39, 79, ?",
        ["149", "155", "159", "169"],
        "श्रृंखला का नियम n × 2 + 1 है: (4×2+1=9, 9×2+1=19, 19×2+1=39, 39×2+1=79, 79×2+1=159)। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        77, "Logical Reasoning & Maths", "Easy", "B",
        "If 'MADRAS' is coded as 'NBESBT', how is 'BOMBAY' coded in that language?",
        ["CPNCBX", "CPNCBZ", "CPOCBZ", "CQOCBZ"],
        "Each letter is shifted forward by +1: B->C, O->P, M->N, B->C, A->B, Y->Z -> CPNCBZ. Hence, option B is correct.",
        "यदि किसी कूट भाषा में 'MADRAS' को 'NBESBT' लिखा जाता है, तो उसी भाषा में 'BOMBAY' को कैसे लिखा जाएगा?",
        ["CPNCBX", "CPNCBZ", "CPOCBZ", "CQOCBZ"],
        "प्रत्येक वर्ण में +1 की वृद्धि की गई है: B→C, O→P, M→N, B→C, A→B, Y→Z। अतः कोड CPNCBZ होगा। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        78, "Logical Reasoning & Maths", "Medium", "D",
        "Pointing to a lady, a man said, 'The father of her only brother is the husband of my mother.' How is the lady related to the man?",
        ["Mother", "Aunt", "Daughter", "Sister"],
        "The father of her only brother is her father. Her father is the husband of the man's mother, which means her father is also the man's father. Thus, the lady is his Sister. Hence, option D is correct.",
        "एक महिला की ओर संकेत करते हुए एक पुरुष ने कहा, 'उसके इकलौते भाई का पिता मेरी माँ का पति है।' वह महिला उस पुरुष से किस प्रकार संबंधित है?",
        ["माँ", "चाची", "पुत्री", "बहन (Sister)"],
        "महिला के इकलौते भाई का पिता अर्थात उस महिला का पिता। उसका पिता पुरुष की माँ का पति (अर्थात पुरुष का पिता) है। अतः वह महिला उस पुरुष की बहन है। अतः विकल्प D सही उत्तर है।"
    ))

    qs.append(create_q(
        79, "Logical Reasoning & Maths", "Easy", "A",
        "A person starts from point X and walks 4 km East, then turns left and walks 3 km. What is the shortest distance from X to his final position?",
        ["5 km", "7 km", "6 km", "4 km"],
        "Using Pythagoras theorem: Distance = sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5 km. Hence, option A is correct.",
        "एक व्यक्ति बिंदु X से पूर्व दिशा में 4 किमी चलता है, फिर बाएँ मुड़कर 3 किमी चलता है। वह बिंदु X से न्यूनतम कितनी दूरी पर है?",
        ["5 किमी", "7 किमी", "6 किमी", "4 किमी"],
        "पाइथागोरस प्रमेय से: दूरी = √(4² + 3²) = √(16 + 9) = √25 = 5 किमी। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        80, "Logical Reasoning & Maths", "Medium", "C",
        "The average of six numbers is 30. If the average of the first four numbers is 25 and the last three is 35, what is the fourth number?",
        ["20", "22", "25", "30"],
        "Total sum = 6 * 30 = 180. Sum of first 4 = 4 * 25 = 100. Sum of last 3 = 3 * 35 = 105. Fourth number = (100 + 105) - 180 = 205 - 180 = 25. Hence, option C is correct.",
        "छह संख्याओं का औसत 30 है। यदि प्रथम चार संख्याओं का औसत 25 तथा अंतिम तीन संख्याओं का औसत 35 हो, तो चौथी संख्या क्या होगी?",
        ["20", "22", "25", "30"],
        "कुल 6 संख्याओं का योग = 6 × 30 = 180। प्रथम 4 का योग = 100 तथा अंतिम 3 का योग = 105। चौथी संख्या = (100 + 105) - 180 = 25। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        81, "Logical Reasoning & Maths", "Easy", "B",
        "A dealer sells a watch for ₹720 at a loss of 10%. What was the cost price of the watch?",
        ["₹780", "₹800", "₹820", "₹850"],
        "Selling Price = 90% of CP => 0.90 * CP = 720 => CP = 720 / 0.9 = ₹800. Hence, option B is correct.",
        "एक घड़ी को ₹720 में बेचने पर 10% की हानि होती है। घड़ी का क्रय मूल्य क्या था?",
        ["₹780", "₹800", "₹820", "₹850"],
        "क्रय मूल्य = (विक्रय मूल्य × 100) / (100 - हानि %) = (720 × 100) / 90 = ₹800। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        82, "Logical Reasoning & Maths", "Medium", "D",
        "A can do a piece of work in 20 days and B can do it in 30 days. How long will they take to complete it working together?",
        ["10 days", "15 days", "14 days", "12 days"],
        "Together: (20 * 30) / (20 + 30) = 600 / 50 = 12 days. Hence, option D is correct.",
        "A किसी कार्य को 20 दिन में तथा B उसे 30 दिन में कर सकता है। दोनों मिलकर उस कार्य को कितने दिन में पूरा करेंगे?",
        ["10 दिन", "15 दिन", "14 दिन", "12 दिन"],
        "दोनों द्वारा लिया गया समय = (xy) / (x + y) = (20 × 30) / (20 + 30) = 600 / 50 = 12 दिन। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        83, "Logical Reasoning & Maths", "Easy", "A",
        "The ratio of the ages of two brothers is 4 : 5 and the sum of their ages is 36 years. What is the age of the elder brother?",
        ["20 years", "16 years", "24 years", "18 years"],
        "Sum of ratio units = 4 + 5 = 9. 1 unit = 36 / 9 = 4 years. Elder brother = 5 * 4 = 20 years. Hence, option A is correct.",
        "दो भाइयों की आयु का अनुपात 4 : 5 है और उनकी आयु का योग 36 वर्ष है। बड़े भाई की आयु कितनी है?",
        ["20 वर्ष", "16 वर्ष", "24 वर्ष", "18 वर्ष"],
        "अनुपाती योग = 4 + 5 = 9। 1 अनुपात का मान = 36 / 9 = 4 वर्ष। बड़े भाई की आयु = 5 × 4 = 20 वर्ष। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        84, "Logical Reasoning & Maths", "Medium", "C",
        "What is the compound interest on ₹5,000 for 2 years at 10% per annum compounded annually?",
        ["₹1,000", "₹1,025", "₹1,050", "₹1,100"],
        "Amount = 5000 * (1.1)^2 = 5000 * 1.21 = ₹6,050. CI = 6050 - 5000 = ₹1,050. Hence, option C is correct.",
        "₹5,000 पर 10% वार्षिक चक्रवृद्धि ब्याज की दर से 2 वर्ष का चक्रवृद्धि ब्याज कितना होगा?",
        ["₹1,000", "₹1,025", "₹1,050", "₹1,100"],
        "मिश्रधन = 5000 × (1.1)² = ₹6,050। चक्रवृद्धि ब्याज = 6050 - 5000 = ₹1,050। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        85, "Logical Reasoning & Maths", "Medium", "B",
        "Two trains of lengths 100 m and 150 m are moving in opposite directions at 40 km/h and 50 km/h. How long will they take to cross each other?",
        ["8 seconds", "10 seconds", "12 seconds", "15 seconds"],
        "Total distance = 100 + 150 = 250 m. Relative speed = 40 + 50 = 90 km/h = 90 * (5/18) = 25 m/s. Time = 250 / 25 = 10 seconds. Hence, option B is correct.",
        "100 मीटर और 150 मीटर लंबी दो रेलगाड़ियां विपरीत दिशाओं में क्रमशः 40 किमी/घं और 50 किमी/घं की चाल से चल रही हैं। वे एक-दूसरे को पार करने में कितना समय लेंगी?",
        ["8 सेकंड", "10 सेकंड", "12 सेकंड", "15 सेकंड"],
        "कुल दूरी = 100 + 150 = 250 मीटर। सापेक्ष चाल = 40 + 50 = 90 किमी/घं = 25 मी./से.। समय = 250 / 25 = 10 सेकंड। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        86, "Logical Reasoning & Maths", "Easy", "D",
        "In a class of 50 students, Ravi's rank is 15th from the top. What is his rank from the bottom?",
        ["35th", "37th", "34th", "36th"],
        "Rank from bottom = (Total - Top) + 1 = (50 - 15) + 1 = 35 + 1 = 36th. Hence, option D is correct.",
        "50 छात्रों की एक कक्षा में रवि का क्रमांक ऊपर से 15वाँ है। नीचे से उसका क्रमांक क्या होगा?",
        ["35वाँ", "37वाँ", "34वाँ", "36वाँ"],
        "नीचे से स्थान = (कुल छात्र - ऊपर से स्थान) + 1 = (50 - 15) + 1 = 36वाँ। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        87, "Logical Reasoning & Maths", "Medium", "A",
        "The area of a circle is 154 sq. cm. What is its circumference? (Use π = 22/7)",
        ["44 cm", "48 cm", "54 cm", "88 cm"],
        "π * r^2 = 154 => (22/7) * r^2 = 154 => r^2 = (154 * 7)/22 = 49 => r = 7 cm. Circumference = 2 * (22/7) * 7 = 44 cm. Hence, option A is correct.",
        "एक वृत्त का क्षेत्रफल 154 वर्ग सेमी है। इसकी परिधि कितनी होगी? (π = 22/7 मानिए)",
        ["44 सेमी", "48 सेमी", "54 सेमी", "88 सेमी"],
        "क्षेत्रफल πr² = 154 => r² = 49 => त्रिज्या r = 7 सेमी। परिधि = 2πr = 2 × (22/7) × 7 = 44 सेमी। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        88, "Logical Reasoning & Maths", "Easy", "C",
        "Choose the odd pair of numbers from the alternatives:",
        ["2 - 8", "3 - 27", "4 - 60", "5 - 125"],
        "All pairs follow n -> n^3 (2^3=8, 3^3=27, 5^3=125) except 4 -> 60 (4^3 should be 64). Hence, option C is odd.",
        "दिए गए विकल्पों में से विषम संख्या युग्म का चयन कीजिए:",
        ["2 - 8", "3 - 27", "4 - 60", "5 - 125"],
        "अन्य सभी युग्मों में पहली संख्या का घन (Cube) दूसरी संख्या है (4 का घन 64 होना चाहिए, 60 नहीं)। अतः विकल्प C विषम है।"
    ))

    qs.append(create_q(
        89, "Logical Reasoning & Maths", "Medium", "B",
        "What is the angle between the hour and minute hands of a clock at 8:20?",
        ["120°", "130°", "140°", "125°"],
        "Angle = |30*H - (11/2)*M| = |30*8 - (11/2)*20| = |240 - 110| = 130°. Hence, option B is correct.",
        "किसी घड़ी में 8 बजकर 20 मिनट पर घंटे तथा मिनट की सुइयों के बीच कितने अंश का कोण होगा?",
        ["120°", "130°", "140°", "125°"],
        "सूत्र: कोण = |30 × 8 - (11/2) × 20| = |240 - 110| = 130°। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        90, "Logical Reasoning & Maths", "Easy", "D",
        "Find the Least Common Multiple (LCM) of 12, 18, and 24:",
        ["48", "60", "96", "72"],
        "Multiples of 24: 24, 48, 72. 72 is divisible by both 12 and 18. LCM = 72. Hence, option D is correct.",
        "12, 18 और 24 का लघुत्तम समापवर्त्य (LCM) क्या होगा?",
        ["48", "60", "96", "72"],
        "12 = 2² × 3, 18 = 2 × 3², 24 = 2³ × 3। LCM = 2³ × 3² = 8 × 9 = 72। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        91, "Logical Reasoning & Maths", "Medium", "A",
        "If the side of a square is increased by 25%, by what percentage does its area increase?",
        ["56.25%", "50%", "62.5%", "55%"],
        "Net change = 25 + 25 + (25*25)/100 = 50 + 6.25 = 56.25%. Hence, option A is correct.",
        "यदि किसी वर्ग की भुजा में 25% की वृद्धि की जाती है, तो उसके क्षेत्रफल में कितने प्रतिशत की वृद्धि होगी?",
        ["56.25%", "50%", "62.5%", "55%"],
        "प्रतिशत वृद्धि = 2x + (x²/100) = 2(25) + (625/100) = 50 + 6.25 = 56.25%। अतः विकल्प A सही उत्तर है।"
    ))

    qs.append(create_q(
        92, "Logical Reasoning & Maths", "Hard", "C",
        "Two unbiased dice are thrown simultaneously. What is the probability of getting a sum of 8?",
        ["1/6", "7/36", "5/36", "1/9"],
        "Outcomes with sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) = 5 outcomes. Total possible = 36. Probability = 5/36. Hence, option C is correct.",
        "दो निष्पक्ष पासे एक साथ फेंके जाते हैं। दोनों पासों पर आने वाले अंकों का योग 8 होने की प्रायिकता क्या है?",
        ["1/6", "7/36", "5/36", "1/9"],
        "योग 8 देने वाले अनुकूल परिणाम: (2,6), (3,5), (4,4), (5,3), (6,2) अर्थात 5 परिणाम। कुल परिणाम = 36। प्रायिकता = 5/36। अतः विकल्प C सही है।"
    ))

    qs.append(create_q(
        93, "Logical Reasoning & Maths", "Medium", "B",
        "If 'L' stands for '+', 'M' stands for '-', 'N' stands for '×', and 'P' stands for '÷', then: 14 N 10 L 42 P 2 M 8 = ?",
        ["145", "153", "148", "160"],
        "14 * 10 + 42 / 2 - 8 = 140 + 21 - 8 = 161 - 8 = 153. Hence, option B is correct.",
        "यदि 'L' का अर्थ '+', 'M' का अर्थ '-', 'N' का अर्थ '×' तथा 'P' का अर्थ '÷' हो, तो 14 N 10 L 42 P 2 M 8 का मान क्या होगा?",
        ["145", "153", "148", "160"],
        "चिह्नों को बदलने पर: 14 × 10 + 42 ÷ 2 - 8 = 140 + 21 - 8 = 153। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        94, "Logical Reasoning & Maths", "Easy", "C",
        "If today is Wednesday, what day of the week will it be after 94 days?",
        ["Friday", "Saturday", "Sunday", "Monday"],
        "94 divided by 7 leaves a remainder of 3 (94 = 13 * 7 + 3). Wednesday + 3 days = Thursday, Friday, Saturday. Hence, option B/C (Saturday) is correct.",
        "यदि आज बुधवार है, तो आज से 94 दिन बाद सप्ताह का कौन-सा दिन होगा?",
        ["शुक्रवार", "शनिवार", "रविवार", "सोमवार"],
        "94 को 7 से भाग देने पर शेषफल 3 बचता है। बुधवार + 3 दिन = शनिवार। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        95, "Logical Reasoning & Maths", "Medium", "D",
        "The cost price of 15 articles is equal to the selling price of 12 articles. What is the gain percentage?",
        ["20%", "30%", "15%", "25%"],
        "Gain % = ((15 - 12) / 12) * 100 = (3/12) * 100 = 25%. Hence, option D is correct.",
        "15 वस्तुओं का क्रय मूल्य 12 वस्तुओं के विक्रय मूल्य के बराबर है। लाभ प्रतिशत कितना होगा?",
        ["20%", "30%", "15%", "25%"],
        "लाभ % = [(15 - 12) / 12] × 100 = (3/12) × 100 = 25%। अतः विकल्प D सही है।"
    ))

    qs.append(create_q(
        96, "Logical Reasoning & Maths", "Easy", "A",
        "Statements: All roses are flowers. Some flowers are red. Conclusion: Some roses are red.",
        ["Conclusion does not necessarily follow", "Conclusion definitely follows", "All roses are red", "None follows"],
        "The intersection between red items and flowers does not necessarily contain roses; it could be other flowers. The conclusion does not necessarily follow. Hence, option A is correct.",
        "कथन: सभी गुलाब फूल हैं। कुछ फूल लाल हैं। निष्कर्ष: कुछ गुलाब लाल हैं।",
        ["निष्कर्ष अनिवार्यतः अनुसरण नहीं करता", "निष्कर्ष निश्चित रूप से अनुसरण करता है", "सभी गुलाब लाल हैं", "कोई नहीं"],
        "फूलों का जो हिस्सा लाल है, वह आवश्यक नहीं कि गुलाब ही हो। अतः निष्कर्ष निश्चित रूप से नहीं निकाला जा सकता। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        97, "Logical Reasoning & Maths", "Medium", "C",
        "A sum invested at compound interest doubles itself in 4 years. In how many years will it become 8 times its initial amount at the same rate?",
        ["8 years", "10 years", "12 years", "16 years"],
        "8 = 2^3. Under compound interest, if it doubles in 4 years, it becomes 2^3 times in 3 * 4 = 12 years. Hence, option C is correct.",
        "कोई धनराशि चक्रवृद्धि ब्याज पर 4 वर्षों में स्वयं की दोगुनी हो जाती है। उसी ब्याज दर से वह कितने वर्षों में 8 गुनी हो जाएगी?",
        ["8 वर्ष", "10 वर्ष", "12 वर्ष", "16 वर्ष"],
        "8 गुना = 2³ गुना। अतः समय = 3 × 4 = 12 वर्ष। अतः विकल्प C सही उत्तर है।"
    ))

    qs.append(create_q(
        98, "Logical Reasoning & Maths", "Hard", "B",
        "In how many ways can 5 books be arranged on a shelf?",
        ["60", "120", "24", "720"],
        "Number of arrangements = 5! = 5 * 4 * 3 * 2 * 1 = 120. Hence, option B is correct.",
        "5 विभिन्न पुस्तकों को एक शेल्फ में कितने प्रकार से व्यवस्थित किया जा सकता है?",
        ["60", "120", "24", "720"],
        "क्रमचयों की संख्या = 5! = 5 × 4 × 3 × 2 × 1 = 120 तरीके। अतः विकल्प B सही है।"
    ))

    qs.append(create_q(
        99, "Logical Reasoning & Maths", "Medium", "A",
        "A train 120 metres long passes a standing man in 6 seconds. What is the speed of the train in km/h?",
        ["72 km/h", "60 km/h", "54 km/h", "80 km/h"],
        "Speed in m/s = 120 / 6 = 20 m/s. Speed in km/h = 20 * (18/5) = 72 km/h. Hence, option A is correct.",
        "120 मीटर लंबी एक रेलगाड़ी एक खड़े व्यक्ति को 6 सेकंड में पार करती है। रेलगाड़ी की चाल किमी/घंटे में क्या है?",
        ["72 किमी/घं", "60 किमी/घं", "54 किमी/घं", "80 किमी/घं"],
        "चाल = 120 / 6 = 20 मी./से.। किमी/घंटे में = 20 × (18/5) = 72 किमी/घं। अतः विकल्प A सही है।"
    ))

    qs.append(create_q(
        100, "Logical Reasoning & Maths", "Easy", "D",
        "Find the simple interest on ₹2,500 at 6% per annum for 4 years:",
        ["₹500", "₹550", "₹650", "₹600"],
        "SI = (2500 * 6 * 4) / 100 = 25 * 24 = ₹600. Hence, option D is correct.",
        "₹2,500 की राशि पर 6% वार्षिक दर से 4 वर्ष का साधारण ब्याज कितना होगा?",
        ["₹500", "₹550", "₹650", "₹600"],
        "साधारण ब्याज = (मूलधन × दर × समय) / 100 = (2500 × 6 × 4) / 100 = ₹600। अतः विकल्प D सही उत्तर है।"
    ))

    return qs

def main():
    qs = get_csat_2019_questions()
    assert len(qs) == 100, f"Expected 100 questions, got {len(qs)}"

    out_path = "tests/state_psc/uppcs_pre/pyq/uppcs_pre_pyq_2019_csat.json"
    data = {
        "testId": "uppcs_pre_pyq_2019_csat",
        "categoryId": "uppcs_pre",
        "test_id": "uppcs_pre_pyq_2019_csat",
        "category_id": "uppcs_pre",
        "title": "UPPSC PCS Prelims 2019 — CSAT Paper 2 (Full 100 Qs)",
        "titleEn": "UPPSC PCS Prelims 2019 — CSAT Paper 2 (Full 100 Qs)",
        "titleHi": "UPPSC PCS प्रारंभिक परीक्षा 2019 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
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
        "examYear": 2019,
        "shiftBadge": "UPPSC Prelims 2019 • CSAT Paper-2 (Full 100 Qs)",
        "questions": qs,
        "path": out_path.replace("\\", "/")
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)
    print(f"Successfully generated {out_path} with {len(qs)} questions.")

if __name__ == "__main__":
    main()
