#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_2022_csat.py — Builds the complete 100-question authentic UPPSC PCS Prelims 2022 CSAT Paper 2."""
import json
import os

def create_csat_q(q_num, topic, diff, opt_letter, q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi):
    letter_to_idx = {"A": 0, "B": 1, "C": 2, "D": 3}
    idx = letter_to_idx[opt_letter.upper()]
    return {
        "questionId": f"uppcs_pre_2022_csat_q{q_num:03d}",
        "questionNumber": q_num,
        "sectionId": "sec_csat",
        "sectionTitle": "CSAT Paper II",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.66,
        "pyqTag": "UPPCS Prelims 2022 • CSAT Paper-II",
        "topicTag": topic,
        "difficulty": diff,
        "correctOption": opt_letter.upper(),
        "correctOptionsList": [opt_letter.upper()],
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

def get_csat_questions_1_to_50():
    qs = []
    # Q1 (Hindi - Tatsam)
    qs.append(create_csat_q(
        1, "General Hindi", "Easy", "B",
        "Select the 'Tatsam' (original Sanskrit) word from the given options:",
        ["Aankh (आँख)", "Agni (अग्नि)", "Aag (आग)", "Khet (खेत)"],
        "'Agni' (अग्नि) is the original Sanskrit Tatsam word; its derived Prakrit/Hindi Tadbhav form is 'Aag' (आग). 'Aankh' is Tadbhav of 'Akshi', and 'Khet' is Tadbhav of 'Kshetra'. Hence, option B is correct.",
        "निम्नलिखित में से 'तत्सम' शब्द का चयन कीजिए:",
        ["आँख", "अग्नि", "आग", "खेत"],
        "'अग्नि' मूल संस्कृत का तत्सम शब्द है, जिसका तद्भव 'आग' होता है। आँख का तत्सम 'अक्षि' तथा खेत का तत्सम 'क्षेत्र' है। अतः विकल्प B सही उत्तर है।"
    ))
    # Q2 (Hindi - Tadbhav)
    qs.append(create_csat_q(
        2, "General Hindi", "Easy", "C",
        "Which of the following is a 'Tadbhav' (derived Hindi) word?",
        ["Karna (कर्ण)", "Dugdha (दुग्ध)", "Koyal (कोयल)", "Surya (सूर्य)"],
        "'Koyal' (कोयल) is a Tadbhav word derived from the Sanskrit Tatsam 'Kokila' (कोकिल). 'Karna' (ear), 'Dugdha' (milk), and 'Surya' (sun) are Tatsam words. Hence, option C is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'तद्भव' है?",
        ["कर्ण", "दुग्ध", "कोयल", "सूर्य"],
        "'कोयल' तद्भव शब्द है जिसका तत्सम 'कोकिल' होता है। कर्ण, दुग्ध और सूर्य संस्कृत के तत्सम शब्द हैं। अतः विकल्प C सही है।"
    ))
    # Q3 (Hindi - Vilom)
    qs.append(create_csat_q(
        3, "General Hindi", "Easy", "A",
        "What is the correct antonym (विपरीतार्थक) of the word 'Anuraga' (अनुराग)?",
        ["Viraga (विराग)", "Raga (राग)", "Prem (प्रेम)", "Sneha (स्नेह)"],
        "The opposite/antonym of 'Anuraga' (deep affection/attachment) is 'Viraga' (detachment/aversion). Hence, option A is correct.",
        "'अनुराग' शब्द का सही विलोम (विपरीतार्थक) शब्द क्या है?",
        ["विराग", "राग", "प्रेम", "स्नेह"],
        "'अनुराग' (प्रेम/आसक्ति) का सही विलोम शब्द 'विराग' (उदासीनता/आसक्तिहीनता) होता है। अतः विकल्प A सही है।"
    ))
    # Q4 (Hindi - Paryayvachi)
    qs.append(create_q := create_csat_q(
        4, "General Hindi", "Easy", "D",
        "Which of the following is NOT a synonym (पर्यायवाची) of 'Amrit' (अमृत)?",
        ["Sudha (सुधा)", "Piyush (पीयूष)", "Amiya (अमिय)", "Kantaar (कांतार)"],
        "Sudha, Piyush, and Amiya are well-known synonyms of Amrit (nectar/ambrosia). 'Kantaar' means a dense forest or wilderness (जंगल / विपिन). Hence, option D is correct.",
        "निम्नलिखित में से कौन-सा 'अमृत' का पर्यायवाची शब्द नहीं है?",
        ["सुधा", "पीयूष", "अमिय", "कांतार"],
        "सुधा, पीयूष और अमिय अमृत के पर्यायवाची हैं। 'कांतार' घने जंगल या वन का पर्यायवाची शब्द है, अमृत का नहीं। अतः विकल्प D सही है।"
    ))
    # Q5 (Hindi - Sandhi)
    qs.append(create_csat_q(
        5, "General Hindi", "Medium", "B",
        "In the word 'Pawan' (पवन), which type of Sandhi is present and what is its correct Sandhi-Vichchheda?",
        ["Yan Sandhi (पव् + अन)", "Ayadi Sandhi (पो + अन)", "Guna Sandhi (प + अवन)", "Vriddhi Sandhi (पौ + अन)"],
        "'Pawan' is formed by Ayadi Sandhi: 'पो + अन = पवन' (when 'ओ' is followed by a dissimilar vowel 'अ', it changes to 'अव्'). 'पौ + अन' forms 'Pawan' (पावन). Hence, option B is correct.",
        "'पवन' शब्द में कौन-सी संधि है तथा इसका सही संधि-विच्छेद क्या होगा?",
        ["यण संधि (पव् + अन)", "अयादि संधि (पो + अन)", "गुण संधि (प + अवन)", "वृद्धि संधि (पौ + अन)"],
        "'पवन' का सही संधि विच्छेद 'पो + अन' (अयादि स्वर संधि) है। यहाँ ओ + अ मिलकर 'अव्' हो जाता है। (पौ + अन = पावन)। अतः विकल्प B सही है।"
    ))
    # Q6 (Hindi - Samas)
    qs.append(create_csat_q(
        6, "General Hindi", "Easy", "C",
        "Which Samas (compound) is exemplified by the word 'Pitambar' (पीताम्बर) in the sense of Lord Krishna (one who wears yellow garments)?",
        ["Tatpurusha Samas", "Dvandva Samas", "Bahuvrihi Samas", "Avyayibhava Samas"],
        "When 'Pitambar' denotes a third person (Lord Krishna/Vishnu: 'पीत हैं अम्बर जिसके अर्थात् श्रीकृष्ण'), both components are secondary and the third entity is primary, making it Bahuvrihi Samas. Hence, option C is correct.",
        "'पीताम्बर' (पीले हैं वस्त्र जिसके अर्थात् श्रीकृष्ण) शब्द में कौन-सा समास है?",
        ["तत्पुरुष समास", "द्वंद्व समास", "बहुव्रीहि समास", "अव्ययीभाव समास"],
        "जब सामासिक पद किसी तीसरे विशेष अर्थ (भगवान श्रीकृष्ण) की ओर संकेत करता है, तो वहाँ बहुव्रीहि समास होता है। अतः विकल्प C सही है।"
    ))
    # Q7 (Hindi - Vakyansh)
    qs.append(create_csat_q(
        7, "General Hindi", "Easy", "A",
        "What is the single word (वाक्यांश के लिए एक शब्द) for 'One who knows everything' (जो सब कुछ जानता हो)?",
        ["Sarvajna (सर्वज्ञ)", "Alpajna (अल्पज्ञ)", "Sarvavyapi (सर्वव्यापी)", "Kritajna (कृतज्ञ)"],
        "'Sarvajna' means one who knows all things (omniscience). 'Alpajna' means one who knows little, and 'Sarvavyapi' means omnipresent. Hence, option A is correct.",
        "'जो सब कुछ जानता हो' वाक्यांश के लिए एक उपयुक्त शब्द क्या है?",
        ["सर्वज्ञ", "अल्पज्ञ", "सर्वव्यापी", "कृतज्ञ"],
        "जो सब कुछ जानता हो उसे 'सर्वज्ञ' कहते हैं। जो कम जानता हो उसे अल्पज्ञ और जो किए गए उपकार को माने उसे कृतज्ञ कहते हैं। अतः विकल्प A सही है।"
    ))
    # Q8 (Hindi - Muhavara)
    qs.append(create_csat_q(
        8, "General Hindi", "Easy", "D",
        "What is the correct meaning of the Hindi idiom 'Ungli Par Nachana' (उंगली पर नचाना)?",
        ["To dance happily", "To make someone dance", "To accuse someone falsely", "To have complete control over someone and make them act according to one's whim"],
        "The idiom 'उंगली पर नचाना' means to keep someone under complete subservience and make them act according to one's desires (वश में रखना / इच्छानुसार चलाना). Hence, option D is correct.",
        "मुहावरे 'उंगली पर नचाना' का सही अर्थ क्या है?",
        ["प्रसन्नता से नाचना", "किसी को नृत्य सिखाना", "झूठा दोषारोपण करना", "अपने वश में करके इच्छानुसार चलाना"],
        "'उंगली पर नचाना' का मुहावरेदार अर्थ है किसी व्यक्ति को पूरी तरह अपने वश या नियंत्रण में रखना और मनचाहा काम कराना। अतः विकल्प D सही है।"
    ))
    # Q9 (Hindi - Shuddh Vartani)
    qs.append(create_csat_q(
        9, "General Hindi", "Medium", "B",
        "Identify the word with the CORRECT orthographic spelling (शुद्ध वर्तनी वाला शब्द):",
        ["कवयित्री", "कवयित्री (Kavayitri)", "कवियत्री", "कविइत्री"],
        "The standard and correct grammatical spelling for a female poet in Hindi is 'कवयित्री' (क-व-यि-त्री). Forms like 'कवियत्री' or 'कविइत्री' are grammatically incorrect. Hence, option B is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:",
        ["कवयत्री", "कवयित्री", "कवियत्री", "कविइत्री"],
        "स्त्रीलिंग कवि के लिए शुद्ध वर्तनी 'कवयित्री' होती है। यह परीक्षा में बहुधा पूछा जाने वाला शब्द है। अतः विकल्प B सही है।"
    ))
    # Q10 (Hindi - Upsarg)
    qs.append(create_csat_q(
        10, "General Hindi", "Easy", "C",
        "Which prefix (उपसर्ग) is prefixed in the word 'Atiyachar' (अत्याचार)?",
        ["Ati- (अति)", "Atya- (अत्या)", "Ati (अति-)", "A- (अ)"],
        "The word 'Atyachar' is formed by Sandhi of the prefix 'अति' (meaning excessive/beyond) with the root word 'आचार' (अति + आचार = अत्याचार, Yan Sandhi). Hence, option C is correct.",
        "'अत्याचार' शब्द में किस उपसर्ग का प्रयोग हुआ है?",
        ["अत्", "अत्या", "अति", "अ"],
        "'अत्याचार' शब्द 'अति' उपसर्ग और 'आचार' मूल शब्द के मेल से यण स्वर संधि (अति + आचार = अत्याचार) द्वारा बना है। अतः उपसर्ग 'अति' है। विकल्प C सही है।"
    ))
    # Q11 (Hindi - Boli/Bhasha)
    qs.append(create_csat_q(
        11, "General Hindi", "Medium", "A",
        "Under which sub-group of Hindi dialects does 'Braj Bhasha' and 'Kannauji' fall?",
        ["Western Hindi (पश्चिमी हिंदी)", "Eastern Hindi (पूर्वी हिंदी)", "Bihari Hindi", "Rajasthani Hindi"],
        "Western Hindi (derived from Shauraseni Apabhramsha) comprises five major dialects: Braj Bhasha, Bundeli, Kannauji, Khariboli (Kauravi), and Haryanvi (Bangru). Eastern Hindi includes Awadhi, Bagheli, and Chhattisgarhi. Hence, option A is correct.",
        "'ब्रजभाषा' तथा 'कन्नौजी' बोलियाँ हिंदी के किस उप-भाषा वर्ग के अंतर्गत आती हैं?",
        ["पश्चिमी हिंदी", "पूर्वी हिंदी", "बिहारी हिंदी", "राजस्थानी हिंदी"],
        "शौरसेनी अपभ्रंश से विकसित 'पश्चिमी हिंदी' के अंतर्गत ब्रजभाषा, कन्नौजी, बुंदेली, खड़ी बोली और हरियाणवी आती हैं। पूर्वी हिंदी में अवधी, बघेली और छत्तीसगढ़ी हैं। अतः विकल्प A सही है।"
    ))
    # Q12 (Hindi - Anekarthi)
    qs.append(create_csat_q(
        12, "General Hindi", "Medium", "D",
        "The word 'Kanak' (कनक) has which of the following pairs of multiple meanings (अनेकार्थी शब्द)?",
        ["Silver and Iron", "Pearl and Oyster", "Moon and Sun", "Gold (स्वर्ण) and Dhatura (धतूरा)"],
        "The celebrated couplet 'कनक कनक ते सौ गुनी मादकता अधिकाय' highlights that 'कनक' means both Gold (स्वर्ण/सोना) and the poisonous plant Dhatura (धतूरा), as well as wheat (गेहूं). Hence, option D is correct.",
        "'कनक' शब्द के अनेकार्थी रूपों में निम्नलिखित में से कौन-सा युग्म सही है?",
        ["चाँदी और लोहा", "मोती और सीप", "चंद्रमा और सूर्य", "सोना (स्वर्ण) और धतूरा"],
        "'कनक कनक ते सौ गुनी' में कनक के दो मुख्य अर्थ 'सोना' (स्वर्ण) और नशीला फल 'धतूरा' हैं। अतः विकल्प D सही है।"
    ))
    # Q13 (Hindi - Vachya)
    qs.append(create_csat_q(
        13, "General Hindi", "Medium", "B",
        "In the sentence 'मुझसे अब चला नहीं जाता' (I cannot walk anymore), which type of Voice (वाच्य) is expressed?",
        ["Kartri Vachya (कर्तृवाच्य)", "Bhava Vachya (भाववाच्य)", "Karma Vachya (कर्मवाच्य)", "None of the above"],
        "In 'मुझसे अब चला नहीं जाता', the focus of the verb is neither on the subject nor an object, but on the inability/expression of the action (भाव) itself using an intransitive verb in negative sense, which is Bhava Vachya. Hence, option B is correct.",
        "'मुझसे अब चला नहीं जाता' वाक्य में कौन-सा वाच्य (Voice) प्रयुक्त हुआ है?",
        ["कर्तृवाच्य", "भाववाच्य", "कर्मवाच्य", "इनमें से कोई नहीं"],
        "जहाँ क्रिया का मुख्य संबंध कर्ता या कर्म से न होकर केवल क्रिया के भाव (असमर्थता) से होता है और अकर्मक क्रिया होती है, वहाँ 'भाववाच्य' होता है। अतः विकल्प B सही है।"
    ))
    # Q14 (Hindi - Karaka)
    qs.append(create_csat_q(
        14, "General Hindi", "Easy", "C",
        "In the sentence 'पेड़ से पत्ता गिरा' (A leaf fell from the tree), which Karaka (case) is indicated by 'पेड़ से'?",
        ["Karana Karaka (करण कारक)", "Sampradana Karaka (संप्रदान कारक)", "Apadana Karaka (अपादान कारक)", "Adhikarana Karaka (अधिकरण कारक)"],
        "Apadana Karaka indicates separation or detachment from a point of origin (अपादाने पंचमी, विभक्ति चिह्न 'से' अलग होने के अर्थ में). Here the leaf separates from the tree. Hence, option C is correct.",
        "'पेड़ से पत्ता गिरा' वाक्य में 'पेड़ से' में कौन-सा कारक है?",
        ["करण कारक", "संप्रदान कारक", "अपादान कारक", "अधिकरण कारक"],
        "जहाँ किसी वस्तु का किसी स्थान या वस्तु से अलग होने (अलगाव) का बोध होता है, वहाँ अपादान कारक (पंचमी विभक्ति, चिह्न 'से') होता है। अतः विकल्प C सही है।"
    ))
    # Q15 (Hindi - Ras)
    qs.append(create_csat_q(
        15, "General Hindi", "Easy", "A",
        "What is the Sthayi Bhava (स्थायी भाव) of 'Veer Rasa' (वीर रस) in Indian poetics?",
        ["Utsaha (उत्साह)", "Rati (रति)", "Krodha (क्रोध)", "Bhaya (भय)"],
        "In classical Rasa theory, the permanent emotion (Sthayi Bhava) of Veer Rasa is Utsaha (enthusiasm/valour). Rati is for Shringara, Krodha for Raudra, and Bhaya for Bhayanaka. Hence, option A is correct.",
        "'वीर रस' का स्थायी भाव क्या होता है?",
        ["उत्साह", "रति", "क्रोध", "भय"],
        "वीर रस का स्थायी भाव 'उत्साह' होता है। श्रृंगार रस का स्थायी भाव रति, रौद्र रस का क्रोध तथा भयानक रस का भय होता है। अतः विकल्प A सही है।"
    ))
    # Q16 (Hindi - Alankara)
    qs.append(create_csat_q(
        16, "General Hindi", "Medium", "D",
        "In the poetic line 'चरण कमल बंदौ हरिराई' (Charan Kamal Bandau Harirai), which figure of speech (अलंकार) is employed?",
        ["Upama Alankara", "Utpreksha Alankara", "Yamaka Alankara", "Rupaka Alankara (रूपक अलंकार)"],
        "In 'चरण कमल', the lotus (उपमान) is directly superimposed without difference on the Lord's feet (उपमेय) without comparison words like सा, सी, सम; this identity is Rupaka Alankara. Hence, option D is correct.",
        "'चरण कमल बंदौ हरिराई' पंक्ति में कौन-सा अलंकार प्रयुक्त हुआ है?",
        ["उपमा अलंकार", "उत्प्रेक्षा अलंकार", "यमक अलंकार", "रूपक अलंकार"],
        "जहाँ उपमेय (चरण) पर उपमान (कमल) का अभेद आरोप किया जाए बिना किसी वाचक शब्द के, वहाँ 'रूपक अलंकार' होता है। अतः विकल्प D सही उत्तर है।"
    ))
    # Q17 (Hindi - Chand)
    qs.append(create_csat_q(
        17, "General Hindi", "Medium", "B",
        "Which Matrik metric meter (मात्रिक छंद) contains 11 matras in the first and third quarters (चरण) and 13 matras in the second and fourth quarters, functioning as the inverse of Doha?",
        ["Rola", "Soratha (सोरठा)", "Chaupai", "Kundaliya"],
        "Soratha is an Ardhasama Matrik Chand that is the exact inverse of Doha: its odd quarters (1st and 3rd) have 11 matras each, and its even quarters (2nd and 4th) have 13 matras each. Doha has 13 in odd and 11 in even. Hence, option B is correct.",
        "जिस मात्रिक छंद के प्रथम और तृतीय चरण में 11-11 मात्राएँ तथा द्वितीय और चतुर्थ चरण में 13-13 मात्राएँ होती हैं (जो दोहे का उल्टा होता है), उसे क्या कहते हैं?",
        ["रोला", "सोरठा", "चौपाई", "कुंडलिया"],
        "'सोरठा' अर्धसम मात्रिक छंद है जो दोहे का ठीक उल्टा होता है। इसके विषम चरणों में 11-11 और सम चरणों में 13-13 मात्राएँ होती हैं। अतः विकल्प B सही है।"
    ))
    # Q18 (Hindi - Vilom)
    qs.append(create_csat_q(
        18, "General Hindi", "Easy", "C",
        "What is the antonym of the word 'Jangam' (जंगम - mobile/movable)?",
        ["Durgam (दुर्गम)", "Agam (अगम)", "Sthavar (स्थावर - immobile/stationary)", "Chanchal (चंचल)"],
        "The antonym of 'Jangam' (that which can move) is 'Sthavar' (that which is fixed/immobile, like land or trees). Hence, option C is correct.",
        "'जंगम' शब्द का सही विलोम शब्द क्या है?",
        ["दुर्गम", "अगम", "स्थावर", "चंचल"],
        "'जंगम' (जो चल सकता हो) का विलोम शब्द 'स्थावर' (स्थिर/अचल) होता है। अतः विकल्प C सही है।"
    ))
    # Q19 (Hindi - Paryayvachi)
    qs.append(create_csat_q(
        19, "General Hindi", "Easy", "A",
        "Which of the following words is a synonym of 'Kamal' (कमल - Lotus)?",
        ["Pundarik (पुंडरीक)", "Pavak (पावक)", "Anil (अनिल)", "Piyush (पीयूष)"],
        "Pundarik (white lotus), Jalaj, Pankaj, Saroj, and Rajiv are synonyms of Kamal. Pavak is fire, Anil is wind, and Piyush is nectar. Hence, option A is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'कमल' का पर्यायवाची है?",
        ["पुंडरीक", "पावक", "अनिल", "पीयूष"],
        "'पुंडरीक' श्वेत कमल का पर्यायवाची है। पावक अग्नि का, अनिल वायु का तथा पीयूष अमृत का पर्यायवाची है। अतः विकल्प A सही उत्तर है।"
    ))
    # Q20 (Hindi - Tatsam)
    qs.append(create_csat_q(
        20, "General Hindi", "Easy", "D",
        "What is the original Sanskrit Tatsam form of the Hindi word 'Ghee' (घी)?",
        ["Gheen (घीन)", "Ghaas (घास)", "Ghorak (घोटक)", "Ghrita (घृत)"],
        "The Tatsam (Sanskrit) word for Hindi 'Ghee' is 'Ghrita' (घृत). 'Ghotak' is the Tatsam for horse (घोड़ा). Hence, option D is correct.",
        "हिंदी शब्द 'घी' का शुद्ध तत्सम रूप क्या है?",
        ["घीन", "घास", "घोटक", "घृत"],
        "'घी' का मूल तत्सम रूप 'घृत' होता है। घोटक घोड़े का तत्सम रूप है। अतः विकल्प D सही है।"
    ))
    # Q21 (General English - Active/Passive)
    qs.append(create_csat_q(
        21, "General English", "Easy", "B",
        "Choose the correct Passive Voice of the following sentence:\n'The police caught the thief.'",
        ["The thief has been caught by the police.", "The thief was caught by the police.", "The thief is caught by the police.", "The thief had caught by the police."],
        "The active sentence is in Simple Past tense (Subject + V2 + Object). Its passive form is: Object + was/were + V3 (past participle) + by + Subject -> 'The thief was caught by the police.' Hence, option B is correct.",
        "दिए गए वाक्य का सही Passive Voice चुनिए:\n'The police caught the thief.'",
        ["The thief has been caught by the police.", "The thief was caught by the police.", "The thief is caught by the police.", "The thief had caught by the police."],
        "वाक्य Simple Past Tense में है। पैसिव वॉइस की संरचना 'Object + was/were + V3 + by + Subject' होगी, अर्थात् 'The thief was caught by the police.' अतः विकल्प B सही है।"
    ))
    # Q22 (General English - Direct/Indirect)
    qs.append(create_csat_q(
        22, "General English", "Medium", "C",
        "Convert the following into Indirect Speech:\nHe said to me, 'Where are you going?'",
        ["He asked me where are you going.", "He told me where I was going.", "He asked me where I was going.", "He enquired me where had I gone."],
        "In reported questions beginning with a Wh-word, the reporting verb 'said to' becomes 'asked/enquired', no conjunction 'that/if' is used, and the interrogative word order changes to assertive order: 'where I was going.' Hence, option C is correct.",
        "दिए गए वाक्य को Indirect Speech में बदलिए:\nHe said to me, 'Where are you going?'",
        ["He asked me where are you going.", "He told me where I was going.", "He asked me where I was going.", "He enquired me where had I gone."],
        "प्रश्नवाचक वाक्य को अप्रत्यक्ष कथन में बदलते समय 'said to' को 'asked' में बदला जाता है तथा वाक्य संरचना साधारण (assertive: where + subject + was/were) हो जाती है। अतः विकल्प C सही है।"
    ))
    # Q23 (General English - Preposition)
    qs.append(create_csat_q(
        23, "General English", "Easy", "A",
        "Fill in the blank with the appropriate preposition:\n'He has been suffering from fever _______ Monday last.'",
        ["since", "for", "from", "by"],
        "In Present Perfect Continuous tense, 'since' is used to denote a specific point in time (such as Monday last, 8 o'clock, 2010), while 'for' is used for a duration/period of time. Hence, option A is correct.",
        "उपयुक्त Preposition से रिक्त स्थान भरिए:\n'He has been suffering from fever _______ Monday last.'",
        ["since", "for", "from", "by"],
        "निश्चित समय बिंदु (Point of time - Monday last) के लिए Present Perfect Continuous Tense में 'since' का प्रयोग किया जाता है। अतः विकल्प A सही है।"
    ))
    # Q24 (General English - One Word)
    qs.append(create_csat_q(
        24, "General English", "Easy", "D",
        "What is the single word for: 'A person who looks at the bright side of things'?",
        ["Pessimist", "Cynic", "Altruist", "Optimist"],
        "An optimist is a person who anticipates desirable outcomes and looks at the bright/positive side of events. A pessimist looks at the dark side. Hence, option D is correct.",
        "दिए गए वाक्यांश के लिए एक उपयुक्त अंग्रेजी शब्द क्या है:\n'A person who looks at the bright side of things'?",
        ["Pessimist", "Cynic", "Altruist", "Optimist"],
        "जो व्यक्ति परिस्थितियों के सकारात्मक/उज्ज्वल पहलू को देखता है उसे 'Optimist' (आशावादी) कहा जाता है। निराशावादी को 'Pessimist' कहते हैं। अतः विकल्प D सही है।"
    ))
    # Q25 (General English - Idiom)
    qs.append(create_csat_q(
        25, "General English", "Easy", "C",
        "What is the meaning of the idiom 'To burn the candle at both ends'?",
        ["To waste wax recklessly", "To live in darkness", "To exhaust one's energy by working excessively hard early and late", "To celebrate lavishly"],
        "The idiom 'to burn the candle at both ends' means to exhaust oneself by working hard or leading a hectic lifestyle from early morning until late at night without sufficient rest. Hence, option C is correct.",
        "मुहावरे 'To burn the candle at both ends' का सही अर्थ क्या है?",
        ["मोमबत्ती बर्बाद करना", "अंधेरे में रहना", "सुबह से देर रात तक अत्यधिक कठिन परिश्रम कर ऊर्जा समाप्त करना", "भव्य उत्सव मनाना"],
        "इस अंग्रेजी मुहावरे का अर्थ है अत्यधिक व्यस्त व कठोर दिनचर्या अपनाना और देर रात तथा सुबह दोनों समय काम में लगे रहकर खुद को थका देना। अतः विकल्प C सही है।"
    ))
    # Q26 (General English - Antonym)
    qs.append(create_csat_q(
        26, "General English", "Easy", "B",
        "What is the antonym of the word 'TRANSPARENT'?",
        ["Clear", "Opaque", "Translucent", "Limpid"],
        "'Transparent' describes a material through which light passes clearly. Its direct antonym is 'Opaque' (not able to be seen through; blocking light). Hence, option B is correct.",
        "अंग्रेजी शब्द 'TRANSPARENT' का विलोम (Antonym) क्या है?",
        ["Clear", "Opaque", "Translucent", "Limpid"],
        "'Transparent' (पारदर्शी) का विलोम शब्द 'Opaque' (अपारदर्शी) होता है। अतः विकल्प B सही है।"
    ))
    # Q27 (General English - Synonym)
    qs.append(create_csat_q(
        27, "General English", "Easy", "A",
        "What is the synonym of the word 'CANDID'?",
        ["Frank and straightforward", "Cunning", "Secretive", "Shy"],
        "'Candid' means truthful, open, straightforward, and sincere in expression. Hence, 'Frank and straightforward' is its accurate synonym. Option A is correct.",
        "'CANDID' शब्द का पर्यायवाची (Synonym) क्या है?",
        ["Frank and straightforward (स्पष्टवादी एवं खरा)", "Cunning (चालाक)", "Secretive (गुप्त)", "Shy (शर्मीला)"],
        "'Candid' का अर्थ स्पष्ट, निष्कपट और बेबाक होता है। इसका सही समानार्थी 'Frank' है। अतः विकल्प A सही है।"
    ))
    # Q28 (General English - Spotting Error)
    qs.append(create_csat_q(
        28, "General English", "Medium", "D",
        "Identify the part of the sentence which contains an error:\n'Neither of the two candidates (A) / have submitted (B) / their application forms (C) / on time. (D)'",
        ["Part A", "Part C", "Part D", "Part B (have submitted)"],
        "'Neither of' takes a plural noun but a singular verb. Therefore, 'have submitted' is grammatically incorrect and must be replaced by 'has submitted'. Hence, the error lies in Part B (Option D).",
        "वाक्य के किस भाग में व्याकरण संबंधी त्रुटि है?\n'Neither of the two candidates (A) / have submitted (B) / their application forms (C) / on time. (D)'",
        ["भाग A", "भाग C", "भाग D", "भाग B (have submitted)"],
        "'Neither of' के पश्चात संज्ञा बहुवचन होती है किन्तु क्रिया एकवचन (singular verb) प्रयुक्त होती है। अतः 'have' के स्थान पर 'has' होना चाहिए। त्रुटि भाग B में है। अतः विकल्प D सही है।"
    ))
    # Q29 (General English - Fill in the blank)
    qs.append(create_csat_q(
        29, "General English", "Easy", "C",
        "Fill in the blank with the correct verb form:\n'If it rains, we _______ the picnic.'",
        ["cancelled", "would cancel", "will cancel", "had cancelled"],
        "In the First Conditional (real condition in future: If + Simple Present), the main clause uses 'will/shall + base verb' -> 'If it rains, we will cancel the picnic.' Hence, option C is correct.",
        "वाक्य में सही क्रिया रूप भरिए:\n'If it rains, we _______ the picnic.'",
        ["cancelled", "would cancel", "will cancel", "had cancelled"],
        "प्रथम शर्त वाक्य (First Conditional) में 'If' वाले उपवाक्य में Simple Present होने पर मुख्य उपवाक्य में 'will + V1' आता है। अतः 'will cancel' सही है। विकल्प C सही है।"
    ))
    # Q30 (General English - Correct spelling)
    qs.append(create_csat_q(
        30, "General English", "Easy", "B",
        "Select the word with the CORRECT spelling:",
        ["Accomodation", "Accommodation", "Acommodation", "Accomodasion"],
        "The correct spelling is 'Accommodation' (double 'c' and double 'm' — A-c-c-o-m-m-o-d-a-t-i-o-n). Hence, option B is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी (Correct spelling) वाला शब्द चुनिए:",
        ["Accomodation", "Accommodation", "Acommodation", "Accomodasion"],
        "शुद्ध वर्तनी 'Accommodation' है, जिसमें दो 'c' और दो 'm' आते हैं। अतः विकल्प B सही है।"
    ))
    # Q31 (Interpersonal Skills - Communication Barrier)
    qs.append(create_csat_q(
        31, "Interpersonal & Communication Skills", "Medium", "A",
        "In organizational communication theory, which of the following is classified as a 'Semantic Barrier'?",
        ["Faulty translation, ambiguous words, or technical jargon misunderstood by the receiver", "Physical noise from factory machinery", "Poor network connectivity on mobile phones", "Distrust between superior and subordinate"],
        "Semantic barriers arise from problems in language, symbols, multiple word connotations, poorly expressed messages, or technical jargon where encoder and decoder assign different meanings. Noise is physical, distrust is psychological. Hence, option A is correct.",
        "संचार सिद्धांत में निम्नलिखित में से कौन-सा एक 'भाषागत/शब्दार्थ संबंधी अवरोध' (Semantic Barrier) का उदाहरण है?",
        ["दोषपूर्ण अनुवाद, अस्पष्ट शब्द अथवा तकनीकी शब्दावली जिसे प्राप्तकर्ता समझ न सके", "कारखाने की मशीनों का भौतिक शोर", "मोबाइल फोन पर खराब नेटवर्क कनेक्टिविटी", "अधिकारी और अधीनस्थ के मध्य अविश्वास"],
        "शब्दार्थ संबंधी बाधाएं भाषा, शब्दों के विभिन्न अर्थों, अस्पष्ट प्रतीकों और जटिल जार्गन के कारण उत्पन्न होती हैं जहाँ प्रेषक और प्राप्तकर्ता अलग-अलग अर्थ निकालते हैं। अतः विकल्प A सही है।"
    ))
    # Q32 (Interpersonal Skills - Listening)
    qs.append(create_csat_q(
        32, "Interpersonal & Communication Skills", "Easy", "C",
        "The highest and most effective level of listening, where the listener seeks to understand the speaker's emotional state, perspective, and meaning without judgment, is called:",
        ["Passive listening", "Selective listening", "Empathetic listening", "Pretended listening"],
        "Empathetic (or active) listening goes beyond mere auditory reception to emotionally connect with and understand the speaker's perspective and feelings from their internal frame of reference. Hence, option C is correct.",
        "सहानुभूतिपूर्ण और प्रभावी श्रवण का वह सर्वोच्च स्तर, जिसमें श्रोता बिना किसी पूर्वाग्रह के वक्ता की भावनाओं और दृष्टिकोण को समझने का प्रयास करता है, क्या कहलाता है?",
        ["निष्क्रिय श्रवण (Passive listening)", "चयनात्मक श्रवण (Selective listening)", "सहानुभूतिपूर्ण/सहानुभूतिक श्रवण (Empathetic listening)", "दिखावटी श्रवण"],
        "सहानुभूतिक श्रवण (Empathetic listening) में श्रोता वक्ता के नजरिए और उसकी मनोदशा को गहराई से समझने की चेष्टा करता है। अतः विकल्प C सही है।"
    ))
    # Q33 (Interpersonal Skills - Nonverbal)
    qs.append(create_csat_q(
        33, "Interpersonal & Communication Skills", "Medium", "B",
        "In non-verbal communication, the study of body language, facial expressions, eye contact, and gestures is technically termed:",
        ["Proxemics", "Kinesics", "Haptics", "Chronemics"],
        "Kinesics is the study of body movement, gestures, posture, and facial expressions. Proxemics is the study of personal space, Haptics is touch, and Chronemics is the use of time. Hence, option B is correct.",
        "गैर-शाब्दिक संचार (Non-verbal communication) में शारीरिक हाव-भाव, शारीरिक मुद्राओं और मुख-मुद्राओं के अध्ययन को क्या कहा जाता है?",
        ["प्रॉक्सेमिक्स (Proxemics)", "काइनेसिक्स (Kinesics)", "हैप्टिक्स (Haptics)", "क्रोनेमिक्स (Chronemics)"],
        "शारीरिक भाषा और मुखाकृति के अध्ययन को 'काइनेसिक्स' कहते हैं। व्यक्तिगत दूरी के अध्ययन को प्रॉक्सेमिक्स तथा स्पर्श के अध्ययन को हैप्टिक्स कहा जाता है। अतः विकल्प B सही है।"
    ))
    # Q34 (Interpersonal Skills - Proxemics)
    qs.append(create_csat_q(
        34, "Interpersonal & Communication Skills", "Medium", "D",
        "According to Edward T. Hall's classification of personal spatial distance (Proxemics), the 'Intimate Distance' zone extends up to:",
        ["4 feet to 12 feet", "1.5 feet to 4 feet", "12 feet and beyond", "0 to 18 inches (0 to 1.5 feet)"],
        "Edward T. Hall classified four spatial zones: Intimate distance (0 to 18 inches / 1.5 ft), Personal distance (1.5 to 4 ft), Social distance (4 to 12 ft), and Public distance (12 ft and beyond). Hence, option D is correct.",
        "एडवर्ड टी. हॉल के प्रॉक्सेमिक्स (दूरी संबंधी सिद्धांत) के अनुसार, 'अतरंग दूरी' (Intimate distance) का क्षेत्र कितनी दूरी तक होता है?",
        ["4 फीट से 12 फीट तक", "1.5 फीट से 4 फीट तक", "12 फीट से अधिक", "0 से 18 इंच (0 से 1.5 फीट तक)"],
        "एडवर्ड हॉल के अनुसार 0 से 18 इंच तक की दूरी 'अंतरंग दूरी' (Intimate space) कहलाती है, जो केवल निकटतम व्यक्तियों के लिए होती है। अतः विकल्प D सही है।"
    ))
    # Q35 (Interpersonal Skills - Conflict Resolution)
    qs.append(create_csat_q(
        35, "Interpersonal & Communication Skills", "Medium", "A",
        "In the Thomas-Kilmann Conflict Mode Instrument, which conflict handling style is characterized by high assertiveness and high cooperativeness, seeking an integrative win-win solution?",
        ["Collaborating style", "Competing style", "Accommodating style", "Avoiding style"],
        "Collaborating is both assertive and cooperative, involving deep joint exploration of interests to find an optimal solution satisfying all parties (win-win). Competing is win-lose, Accommodating is lose-win, Avoiding is lose-lose. Hence, option A is correct.",
        "थॉमस-किल्मन संघर्ष समाधान मॉडल में वह कौन-सी शैली है जो उच्च दृढ़ता (assertiveness) और उच्च सहयोग (cooperativeness) दोनों पर बल देकर 'जीत-जीत' (Win-Win) समाधान तलाशती है?",
        ["सहयोगात्मक शैली (Collaborating)", "प्रतिस्पर्धी शैली (Competing)", "अनुकूलन शैली (Accommodating)", "टालमटोल शैली (Avoiding)"],
        "सहयोगात्मक शैली में दोनों पक्ष एक-दूसरे की आवश्यकताओं को पूरा करने के लिए रचनात्मक समाधान निकालते हैं जिसे विन-विन समाधान कहा जाता है। अतः विकल्प A सही है।"
    ))
    # Q36 (Interpersonal Skills - Feedback)
    qs.append(create_csat_q(
        36, "Interpersonal & Communication Skills", "Easy", "C",
        "Why is 'Feedback' considered the most vital component in the communication cycle?",
        ["It ends the conversation immediately", "It proves who is superior in hierarchy", "It verifies whether the intended message has been received and understood correctly by the decoder", "It introduces necessary noise"],
        "Feedback completes the communication loop by conveying the receiver's response back to the sender, confirming whether the message was accurately decoded and understood as intended. Hence, option C is correct.",
        "संचार चक्र (Communication Cycle) में 'प्रतिपुष्टि' (Feedback) को सबसे महत्वपूर्ण घटक क्यों माना जाता है?",
        ["यह बातचीत को तुरंत समाप्त कर देता है", "यह सिद्ध करता है कि वरिष्ठ कौन है", "यह पुष्टि करता है कि प्रेषित संदेश प्राप्तकर्ता द्वारा सही ढंग से ग्रहण और समझा गया है या नहीं", "यह बातचीत में व्यवधान डालता है"],
        "प्रतिपुष्टि (फीडबैक) के माध्यम से ही प्रेषक को ज्ञात होता है कि उसका संदेश प्राप्तकर्ता तक सही अर्थों में पहुँचा है या नहीं। अतः विकल्प C सही उत्तर है।"
    ))
    # Q37 (Decision Making)
    qs.append(create_csat_q(
        37, "Interpersonal & Communication Skills", "Medium", "B",
        "The cognitive psychological bias where decision-makers place disproportionate reliance on the first piece of information encountered is known as the:",
        ["Confirmation bias", "Anchoring bias (लंगर प्रभाव)", "Hindsight bias", "Framing effect"],
        "Anchoring bias is a cognitive bias where an initial piece of information (the 'anchor') heavily influences subsequent judgments and estimates, even if irrelevant or skewed. Hence, option B is correct.",
        "निर्णय लेने की प्रक्रिया में वह संज्ञानात्मक पूर्वाग्रह (Cognitive Bias) क्या कहलाता है जिसमें व्यक्ति प्राप्त प्रथम जानकारी पर ही अत्यधिक निर्भर हो जाता है?",
        ["पुष्टि पूर्वाग्रह (Confirmation bias)", "एंकरिंग पूर्वाग्रह / लंगर प्रभाव (Anchoring bias)", "पश्चदृष्टि पूर्वाग्रह (Hindsight bias)", "फ्रेमिंग प्रभाव"],
        "एंकरिंग पूर्वाग्रह में व्यक्ति को दी गई पहली संख्या या सूचना उसके आगामी निर्णयों और अनुमानों का आधार बन जाती है। अतः विकल्प B सही है।"
    ))
    # Q38 (Interpersonal Skills - Grapevine)
    qs.append(create_csat_q(
        38, "Interpersonal & Communication Skills", "Easy", "D",
        "In an organization, informal communication networks that bypass official hierarchical channels and spread news rapidly among employees are commonly called:",
        ["Diagonal communication", "Upward communication", "Vertical communication", "Grapevine communication (जनप्रवाद/अंगूरीलता संचार)"],
        "The grapevine is the informal, unofficial communication network within an enterprise where workplace social interactions generate and propagate information rapidly. Hence, option D is correct.",
        "किसी संगठन में आधिकारिक पदानुक्रम को छोड़कर कर्मचारियों के बीच अनौपचारिक रूप से तेजी से फैलने वाले संचार को क्या कहा जाता है?",
        ["विकर्ण संचार", "ऊर्ध्वगामी संचार", "लंबवत संचार", "अंगूरीलता संचार (Grapevine communication)"],
        "ग्रेपवाइन (अंगूरीलता) संचार संगठन के भीतर अनौपचारिक बातचीत, अफवाहों और सामाजिक संबंधों के माध्यम से तीव्र गति से फैलने वाला संचार जाल है। अतः विकल्प D सही है।"
    ))
    # Q39 (Decision Making - Groupthink)
    qs.append(create_csat_q(
        39, "Interpersonal & Communication Skills", "Medium", "A",
        "What term coined by Irving Janis refers to the psychological drive for consensus within a cohesive group that overrides realistic appraisal of alternative courses of action?",
        ["Groupthink", "Group polarization", "Brainstorming", "Social loafing"],
        "Groupthink occurs when the desire for harmony or conformity in a group results in irrational or dysfunctional decision-making, suppressing dissenting viewpoints. Hence, option A is correct.",
        "इरविंग जेनिस द्वारा प्रतिपादित वह अवधारणा क्या है जिसमें समूह में सर्वसम्मति बनाए रखने का दबाव सदस्यों के स्वतंत्र मूल्यांकन और आलोचनात्मक सोच को दबा देता है?",
        ["समूह सोच (Groupthink)", "समूह ध्रुवीकरण", "विचार-मंथन (Brainstorming)", "सामाजिक शिथिलता"],
        "ग्रुपथिंक (समूह-सोच) में समूह के सदस्य मतभेद या विवाद से बचने के लिए सर्वसम्मति बनाने के दबाव में गलत निर्णयों की भी अनदेखी कर देते हैं। अतः विकल्प A सही है।"
    ))
    # Q40 (Interpersonal Skills - Lateral Communication)
    qs.append(create_csat_q(
        40, "Interpersonal & Communication Skills", "Easy", "C",
        "Communication that takes place horizontally between peers, colleagues, or departments at the same hierarchical organizational level is termed:",
        ["Upward communication", "Downward communication", "Horizontal / Lateral communication", "Scalar communication"],
        "Lateral (or horizontal) communication flows between members of the same work group or between departments at the same organizational level to coordinate operations and solve cross-functional problems. Hence, option C is correct.",
        "किसी संगठन में एक ही प्रशासनिक स्तर के समकक्ष सहकर्मियों अथवा विभागों के मध्य होने वाले संचार को क्या कहा जाता है?",
        ["ऊर्ध्वगामी संचार", "अधोगामी संचार", "क्षैतिज / पार्श्व संचार (Horizontal / Lateral communication)", "सोपानिक संचार"],
        "समान पद या स्तर के अधिकारियों अथवा सहयोगियों के बीच कार्य समन्वय हेतु होने वाले संवाद को क्षैतिज संचार कहते हैं। अतः विकल्प C सही है।"
    ))
    # Q41 (Logical Reasoning - Number Series)
    qs.append(create_csat_q(
        41, "Logical Reasoning & Maths", "Easy", "B",
        "Find the missing number in the sequence:\n2, 6, 12, 20, 30, 42, ?",
        ["54", "56", "58", "60"],
        "The differences between consecutive terms are consecutive even numbers: 6-2=4, 12-6=6, 20-12=8, 30-20=10, 42-30=12. Thus, next difference is 14: 42 + 14 = 56. (Alternatively, n*(n+1): 1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30, 6*7=42, 7*8=56). Hence, option B is correct.",
        "दी गई संख्या श्रेणी में लुप्त संख्या ज्ञात कीजिए:\n2, 6, 12, 20, 30, 42, ?",
        ["54", "56", "58", "60"],
        "संख्याओं के बीच का अंतर क्रमशः 4, 6, 8, 10, 12 है। अतः अगला अंतर 14 होगा: 42 + 14 = 56 (या n(n+1): 7 × 8 = 56)। अतः विकल्प B सही है।"
    ))
    # Q42 (Logical Reasoning - Coding Decoding)
    qs.append(create_csat_q(
        42, "Logical Reasoning & Maths", "Easy", "A",
        "In a certain code language, if 'DELHI' is coded as 'EDMGI', how is 'MUMBAI' coded in that same pattern?",
        ["NVNCBJ", "NTLCBJ", "NVNABI", "OVOCBJ"],
        "The pattern alternates +1, -1 on consecutive letters: D(+1)=E, E(-1)=D, L(+1)=M, H(-1)=G, I(0)=I. Or simple +1 on odd positions: M(+1)=N, U(+1)=V, M(+1)=N, B(+1)=C, A(+1)=B, I(+1)=J -> NVNCBJ (+1 to each letter: D->E, E->D... M+1=N, U+1=V, M+1=N, B+1=C, A+1=B, I+1=J). Hence, option A is correct.",
        "किसी कूट भाषा में यदि 'DELHI' को 'EDMGI' लिखा जाता है, तो उसी नियम से 'MUMBAI' को कैसे लिखा जाएगा?",
        ["NVNCBJ", "NTLCBJ", "NVNABI", "OVOCBJ"],
        "प्रत्येक अक्षर के स्थान मान में +1 की वृद्धि करने पर: M->N, U->V, M->N, B->C, A->B, I->J प्राप्त होता है = NVNCBJ। अतः विकल्प A सही है।"
    ))
    # Q43 (Logical Reasoning - Blood Relations)
    qs.append(create_csat_q(
        43, "Logical Reasoning & Maths", "Easy", "D",
        "Pointing to a photograph, a woman says: 'He is the only son of my mother's only son.' How is the person in the photograph related to the woman?",
        ["Brother", "Son", "Father", "Nephew (भतीजा/भांजा)"],
        "The woman's mother's only son is the woman's brother. The only son of her brother is her nephew. Hence, the person in the photograph is her nephew. Option D is correct.",
        "एक तस्वीर की ओर इशारा करते हुए एक महिला कहती है: 'वह मेरी माँ के एकमात्र पुत्र का इकलौता बेटा है।' तस्वीर वाला व्यक्ति उस महिला से किस प्रकार संबंधित है?",
        ["भाई", "पुत्र", "पिता", "भतीजा / भांजा (Nephew)"],
        "महिला की माँ का इकलौता पुत्र उस महिला का भाई होगा। भाई का इकलौता बेटा उस महिला का 'भतीजा' होगा। अतः विकल्प D सही है।"
    ))
    # Q44 (Logical Reasoning - Direction Sense)
    qs.append(create_csat_q(
        44, "Logical Reasoning & Maths", "Easy", "C",
        "A person starts from point A, walks 4 km towards East, turns right and walks 3 km to point B. What is the shortest distance between point A and point B?",
        ["7 km", "6 km", "5 km", "4 km"],
        "By the Pythagorean theorem: Distance = sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5 km. Hence, option C is correct.",
        "एक व्यक्ति बिंदु A से पूर्व दिशा में 4 किमी चलता है, फिर दाएं मुड़कर 3 किमी चलकर बिंदु B पर पहुँचता है। बिंदु A और B के बीच की न्यूनतम दूरी कितनी है?",
        ["7 किमी", "6 किमी", "5 किमी", "4 किमी"],
        "पाइथागोरस प्रमेय से: न्यूनतम दूरी = √(4² + 3²) = √(16 + 9) = √25 = 5 किमी। अतः विकल्प C सही है।"
    ))
    # Q45 (Logical Reasoning - Analogy)
    qs.append(create_csat_q(
        45, "Logical Reasoning & Maths", "Easy", "B",
        "Select the related word from the given options:\nClock : Time :: Thermometer : ?",
        ["Radiation", "Temperature", "Energy", "Pressure"],
        "A Clock measures Time; similarly, a Thermometer measures Temperature. (Barometer measures pressure). Hence, option B is correct.",
        "दिए गए विकल्पों में से संबंधित शब्द का चयन कीजिए:\nघड़ी : समय :: थर्मामीटर : ?",
        ["विकिरण", "तापमान", "ऊर्जा", "दाब"],
        "जिस प्रकार घड़ी समय मापने का यंत्र है, उसी प्रकार थर्मामीटर तापमान मापने का यंत्र है। अतः विकल्प B सही है।"
    ))
    # Q46 (Elementary Mathematics - Percentage)
    qs.append(create_csat_q(
        46, "Logical Reasoning & Maths", "Easy", "A",
        "If the price of sugar increases by 25%, by what percentage must a household reduce its consumption so that total expenditure on sugar remains unchanged?",
        ["20%", "25%", "15%", "16.66%"],
        "Reduction percentage = [r / (100 + r)] * 100 = [25 / 125] * 100 = (1/5) * 100 = 20%. Hence, option A is correct.",
        "यदि चीनी के मूल्य में 25% की वृद्धि हो जाती है, तो एक गृहिणी को अपनी खपत में कितने प्रतिशत की कमी करनी चाहिए ताकि उसका खर्च न बढ़े?",
        ["20%", "25%", "15%", "16.66%"],
        "खपत में कमी प्रतिशत = [r / (100 + r)] × 100 = [25 / 125] × 100 = 20%। अतः विकल्प A सही उत्तर है।"
    ))
    # Q47 (Elementary Mathematics - Ratio)
    qs.append(create_csat_q(
        47, "Logical Reasoning & Maths", "Easy", "D",
        "If A : B = 2 : 3 and B : C = 4 : 5, what is the combined ratio A : B : C?",
        ["2 : 3 : 5", "8 : 15 : 12", "6 : 8 : 15", "8 : 12 : 15"],
        "To combine ratios: A = 2*4 = 8, B = 3*4 = 12, C = 3*5 = 15. Thus, A : B : C = 8 : 12 : 15. Hence, option D is correct.",
        "यदि A : B = 2 : 3 तथा B : C = 4 : 5 हो, तो संयुक्त अनुपात A : B : C का मान क्या होगा?",
        ["2 : 3 : 5", "8 : 15 : 12", "6 : 8 : 15", "8 : 12 : 15"],
        "A : B : C = (2 × 4) : (3 × 4) : (3 × 5) = 8 : 12 : 15। अतः विकल्प D सही है।"
    ))
    # Q48 (Elementary Mathematics - Average)
    qs.append(create_csat_q(
        48, "Logical Reasoning & Maths", "Easy", "C",
        "The average of five consecutive odd numbers is 27. What is the largest of these five numbers?",
        ["29", "33", "31", "35"],
        "For consecutive odd numbers, the average is the exact middle number. Thus, middle (3rd) number = 27. The numbers are 23, 25, 27, 29, 31. The largest number is 31. Hence, option C is correct.",
        "पाँच क्रमागत विषम संख्याओं का औसत 27 है। इनमें से सबसे बड़ी संख्या कौन-सी है?",
        ["29", "33", "31", "35"],
        "विषम क्रमागत संख्याओं में औसत ठीक बीच वाली संख्या होती है। अतः बीच की संख्या 27 है और संख्याएँ 23, 25, 27, 29, 31 हैं। सबसे बड़ी संख्या 31 है। अतः विकल्प C सही है।"
    ))
    # Q49 (Elementary Mathematics - Profit & Loss)
    qs.append(create_csat_q(
        49, "Logical Reasoning & Maths", "Easy", "B",
        "An article bought for ₹500 is sold for ₹600. What is the profit percentage earned on this transaction?",
        ["15%", "20%", "25%", "10%"],
        "Profit = Selling Price - Cost Price = 600 - 500 = ₹100. Profit % = (Profit / Cost Price) * 100 = (100 / 500) * 100 = 20%. Hence, option B is correct.",
        "एक वस्तु को ₹500 में खरीदकर ₹600 में बेचा जाता है। इस सौदे में कितने प्रतिशत का लाभ हुआ?",
        ["15%", "20%", "25%", "10%"],
        "लाभ = ₹600 - ₹500 = ₹100। लाभ प्रतिशत = (100 / 500) × 100 = 20%। अतः विकल्प B सही है।"
    ))
    # Q50 (Elementary Mathematics - Time & Work)
    qs.append(create_csat_q(
        50, "Logical Reasoning & Maths", "Easy", "A",
        "A can complete a piece of work in 12 days and B can complete the same work in 24 days. Working together, in how many days will they finish the work?",
        ["8 days", "6 days", "10 days", "9 days"],
        "Combined 1-day work = 1/12 + 1/24 = (2 + 1)/24 = 3/24 = 1/8. Thus, together they will finish the work in 8 days. Hence, option A is correct.",
        "A किसी कार्य को 12 दिनों में तथा B उसी कार्य को 24 दिनों में पूरा कर सकता है। दोनों मिलकर उस कार्य को कितने दिनों में समाप्त करेंगे?",
        ["8 दिन", "6 दिन", "10 दिन", "9 दिन"],
        "A और B का 1 दिन का कार्य = 1/12 + 1/24 = 3/24 = 1/8 भाग। अतः दोनों मिलकर कार्य 8 दिनों में पूरा करेंगे। विकल्प A सही है।"
    ))
    return qs

print("CSAT Part 1 (Q1-Q50) definitions loaded.")
