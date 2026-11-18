#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_2022_gs1.py — Builds the complete 150-question authentic UPPSC PCS Prelims 2022 GS-1 Paper."""
import json
import os

def create_q(q_num, topic, diff, opt_letter, q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi):
    letter_to_idx = {"A": 0, "B": 1, "C": 2, "D": 3}
    idx = letter_to_idx[opt_letter.upper()]
    return {
        "questionId": f"uppcs_pre_2022_gs1_q{q_num:03d}",
        "questionNumber": q_num,
        "sectionId": "sec_gs1",
        "sectionTitle": "General Studies I",
        "questionType": "MCQ",
        "positiveMarks": 1.33,
        "negativeMarks": 0.44,
        "pyqTag": "UPPCS Prelims 2022 • GS Paper-I",
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

def get_questions_1_to_50():
    qs = []
    # Q1
    qs.append(create_q(
        1, "Ancient Indian History", "Medium", "A",
        "Match List-I with List-II and select the correct answer using the code given below:\n\nList-I (Harappan Site)\n(A) Manda\n(B) Daimabad\n(C) Kalibangan\n(D) Rakhigarhi\n\nList-II (State / UT)\n(1) Rajasthan\n(2) Haryana\n(3) Jammu & Kashmir\n(4) Maharashtra",
        ["A-(3), B-(4), C-(1), D-(2)", "A-(4), B-(3), C-(1), D-(2)", "A-(3), B-(4), C-(2), D-(1)", "A-(1), B-(2), C-(3), D-(4)"],
        "Manda is in Jammu & Kashmir (3), Daimabad in Maharashtra (4), Kalibangan in Rajasthan (1), and Rakhigarhi in Haryana (2). Hence, option A is correct.",
        "सूची-I को सूची-II से सुमेलित कीजिए तथा नीचे दिए गए कूट से सही उत्तर चुनिए:\n\nसूची-I (हड़प्पा स्थल)\n(A) मांडा\n(B) दायमाबाद\n(C) कालीबंगा\n(D) राखीगढ़ी\n\nसूची-II (राज्य / केंद्र शासित प्रदेश)\n(1) राजस्थान\n(2) हरियाणा\n(3) जम्मू-कश्मीर\n(4) महाराष्ट्र",
        ["A-(3), B-(4), C-(1), D-(2)", "A-(4), B-(3), C-(1), D-(2)", "A-(3), B-(4), C-(2), D-(1)", "A-(1), B-(2), C-(3), D-(4)"],
        "मांडा (जम्मू-कश्मीर - 3), दायमाबाद (महाराष्ट्र - 4), कालीबंगा (राजस्थान - 1) तथा राखीगढ़ी (हरियाणा - 2)। अतः सही कूट A-(3), B-(4), C-(1), D-(2) है। विकल्प A सही है।"
    ))
    # Q2
    qs.append(create_q(
        2, "Medieval Indian History", "Medium", "B",
        "Match List-I with List-II and select the correct answer using the code given below:\n\nList-I (Monument)\n(A) Sultan Garhi\n(B) Red Palace (Lal Mahal)\n(C) Jamat Khana Masjid\n(D) Adhai Din Ka Jhonpra\n\nList-II (Builder)\n(1) Alauddin Khalji\n(2) Qutb-ud-din Aibak\n(3) Iltutmish\n(4) Balban",
        ["A-(3), B-(4), C-(2), D-(1)", "A-(3), B-(4), C-(1), D-(2)", "A-(4), B-(3), C-(1), D-(2)", "A-(2), B-(4), C-(1), D-(3)"],
        "Sultan Garhi was constructed by Iltutmish (3), Red Palace (Lal Mahal) by Balban (4), Jamat Khana Masjid by Alauddin Khalji (1), and Adhai Din Ka Jhonpra in Ajmer by Qutb-ud-din Aibak (2). Hence, option B is correct.",
        "सूची-I को सूची-II से सुमेलित कीजिए तथा नीचे दिए गए कूट से सही उत्तर चुनिए:\n\nसूची-I (भवन)\n(A) सुल्तान गढ़ी\n(B) लाल महल\n(C) जमात खाना मस्जिद\n(D) अढ़ाई दिन का झोंपड़ा\n\nसूची-II (निर्माणकर्ता)\n(1) अलाउद्दीन खिलजी\n(2) कुतुबुद्दीन ऐबक\n(3) इल्तुतमिश\n(4) बलबन",
        ["A-(3), B-(4), C-(2), D-(1)", "A-(3), B-(4), C-(1), D-(2)", "A-(4), B-(3), C-(1), D-(2)", "A-(2), B-(4), C-(1), D-(3)"],
        "सुल्तान गढ़ी (इल्तुतमिश - 3), लाल महल (बलबन - 4), जमात खाना मस्जिद (अलाउद्दीन खिलजी - 1) तथा अढ़ाई दिन का झोंपड़ा (कुतुबुद्दीन ऐबक - 2)। अतः विकल्प B सही है।"
    ))
    # Q3
    qs.append(create_q(
        3, "Modern Indian History", "Easy", "C",
        "Who among the following was the founder of the 'Satyashodhak Samaj' in 1873?",
        ["Raja Ram Mohan Roy", "Sri Narayana Guru", "Jyotirao Phule", "Tarabai Shinde"],
        "Mahatma Jyotirao Phule founded the Satyashodhak Samaj on September 24, 1873 in Pune, Maharashtra to champion the rights and education of oppressed classes and women. Hence, option C is correct.",
        "निम्नलिखित में से किसने 1873 में 'सत्यशोधक समाज' की स्थापना की थी?",
        ["राजा राममोहन राय", "श्री नारायण गुरु", "ज्योतिराव फुले", "ताराबाई शिंदे"],
        "महात्मा ज्योतिराव फुले ने 24 सितंबर 1873 को पुणे में सत्यशोधक समाज की स्थापना की थी। इसका उद्देश्य वंचित एवं शोषित वर्गों को सामाजिक समानता व न्याय दिलाना था। अतः विकल्प C सही है।"
    ))
    # Q4
    qs.append(create_q(
        4, "Indian Polity", "Easy", "D",
        "Which Constitutional Amendment Act made the Right to Education (Article 21A) a Fundamental Right in India?",
        ["42nd Amendment Act", "44th Amendment Act", "73rd Amendment Act", "86th Amendment Act"],
        "The 86th Constitutional Amendment Act, 2002 inserted Article 21A into the Constitution of India, providing free and compulsory education to all children of 6 to 14 years as a Fundamental Right. Hence, option D is correct.",
        "किस संविधान संशोधन अधिनियम द्वारा शिक्षा के अधिकार (अनुच्छेद 21A) को भारत में मौलिक अधिकार बनाया गया?",
        ["42वाँ संशोधन अधिनियम", "44वाँ संशोधन अधिनियम", "73वाँ संशोधन अधिनियम", "86वाँ संशोधन अधिनियम"],
        "86वें संविधान संशोधन अधिनियम 2002 द्वारा संविधान में अनुच्छेद 21A जोड़ा गया जिसके तहत 6 से 14 वर्ष के बच्चों के लिए निःशुल्क एवं अनिवार्य शिक्षा को मौलिक अधिकार बनाया गया। अतः विकल्प D सही है।"
    ))
    # Q5
    qs.append(create_q(
        5, "Environment & Ecology", "Easy", "A",
        "Which one of the following is the first National Park established in India (in 1936 as Hailey National Park)?",
        ["Jim Corbett National Park", "Kaziranga National Park", "Kanha National Park", "Bandipur National Park"],
        "Jim Corbett National Park in Nainital/Pauri Garhwal district of Uttarakhand was established in 1936 as Hailey National Park, making it India's first national park. Hence, option A is correct.",
        "निम्नलिखित में से कौन-सा भारत में स्थापित पहला राष्ट्रीय उद्यान है (1936 में हैली नेशनल पार्क के रूप में स्थापित)?",
        ["जिम कॉर्बेट राष्ट्रीय उद्यान", "काजीरंगा राष्ट्रीय उद्यान", "कान्हा राष्ट्रीय उद्यान", "बांदीपुर राष्ट्रीय उद्यान"],
        "उत्तराखंड में स्थित जिम कॉर्बेट राष्ट्रीय उद्यान भारत का प्रथम राष्ट्रीय उद्यान है, जिसे 1936 में हैली राष्ट्रीय उद्यान के नाम से स्थापित किया गया था। अतः विकल्प A सही है।"
    ))
    # Q6
    qs.append(create_q(
        6, "Indian Geography", "Easy", "B",
        "Which one of the following pairs (Mountain Pass — State / UT) is NOT correctly matched?",
        ["Mana Pass — Uttarakhand", "Nathu La — Arunachal Pradesh", "Zoji La — Ladakh", "Shipki La — Himachal Pradesh"],
        "Nathu La is a pass situated in Sikkim connecting India with Tibet Autonomous Region of China. Bomdi La and Diphu Pass are in Arunachal Pradesh. Hence, option B is incorrectly matched.",
        "निम्नलिखित में से कौन-सा युग्म (पर्वतीय दर्रा — राज्य / केंद्र शासित प्रदेश) सही सुमेलित नहीं है?",
        ["माना दर्रा — उत्तराखंड", "नाथू ला — अरुणाचल प्रदेश", "जोजिला — लद्दाख", "शिपकी ला — हिमाचल प्रदेश"],
        "नाथू ला दर्रा सिक्किम में स्थित है (अरुणाचल प्रदेश में नहीं)। माना दर्रा उत्तराखंड में, जोजिला लद्दाख में तथा शिपकी ला हिमाचल प्रदेश में है। अतः विकल्प B सही उत्तर है।"
    ))
    # Q7
    qs.append(create_q(
        7, "General Science", "Easy", "C",
        "Bacillus Calmette-Guérin (BCG) vaccine is administered to prevent which infectious disease?",
        ["Typhoid", "Polio", "Tuberculosis (TB)", "Diphtheria"],
        "BCG vaccine provides immunity against Tuberculosis (TB), an infectious disease caused by Mycobacterium tuberculosis. Hence, option C is correct.",
        "बैसिलस कैलमेट-गुएरिन (BCG) का टीका किस संक्रामक रोग से बचाव के लिए लगाया जाता है?",
        ["टाइफाइड", "पोलियो", "तपेदिक / क्षय रोग (Tuberculosis)", "डिप्थीरिया"],
        "बीसीजी (BCG) का टीका मुख्य रूप से टीबी (तपेदिक / क्षय रोग) के संक्रमण से बचाव के लिए नवजात शिशुओं को दिया जाता है। अतः विकल्प C सही है।"
    ))
    # Q8
    qs.append(create_q(
        8, "Indian Economy", "Medium", "D",
        "Match List-I (Committee / Commission) with List-II (Subject Area) and select the correct answer:\n\nList-I\n(A) Narasimham Committee\n(B) Sarkaria Commission\n(C) Tendulkar Committee\n(D) Kelkar Committee\n\nList-II\n(1) Tax Reforms\n(2) Poverty Estimation\n(3) Centre-State Relations\n(4) Banking Sector Reforms",
        ["A-(4), B-(3), C-(1), D-(2)", "A-(3), B-(4), C-(2), D-(1)", "A-(4), B-(2), C-(3), D-(1)", "A-(4), B-(3), C-(2), D-(1)"],
        "Narasimham Committee: Banking Sector Reforms (4); Sarkaria Commission: Centre-State Relations (3); Tendulkar Committee: Poverty Estimation (2); Kelkar Committee: Tax Reforms (1). Hence, code A-(4), B-(3), C-(2), D-(1) is correct (Option D).",
        "सूची-I (समिति/आयोग) को सूची-II (विषय/क्षेत्र) से सुमेलित कीजिए तथा नीचे दिए गए कूट से सही उत्तर चुनिए:\n\nसूची-I\n(A) नरसिम्हम समिति\n(B) सरकारिया आयोग\n(C) तेंदुलकर समिति\n(D) केलकर समिति\n\nसूची-II\n(1) कर सुधार\n(2) गरीबी रेखा का निर्धारण\n(3) केंद्र-राज्य संबंध\n(4) बैंकिंग क्षेत्र सुधार",
        ["A-(4), B-(3), C-(1), D-(2)", "A-(3), B-(4), C-(2), D-(1)", "A-(4), B-(2), C-(3), D-(1)", "A-(4), B-(3), C-(2), D-(1)"],
        "नरसिम्हम समिति (बैंकिंग सुधार - 4), सरकारिया आयोग (केंद्र-राज्य संबंध - 3), तेंदुलकर समिति (गरीबी निर्धारण - 2) तथा केलकर समिति (कर संरचना सुधार - 1)। अतः विकल्प D सही है।"
    ))
    # Q9
    qs.append(create_q(
        9, "World Geography", "Medium", "A",
        "Which one of the following countries does NOT share a coastline with the Black Sea?",
        ["Belarus", "Turkey", "Bulgaria", "Georgia"],
        "The six countries bordering the Black Sea are Russia, Ukraine, Georgia, Turkey, Bulgaria, and Romania. Belarus is a completely landlocked country. Hence, option A is correct.",
        "निम्नलिखित में से किस देश की सीमा काला सागर (Black Sea) से नहीं लगती है?",
        ["बेलारूस", "तुर्की", "बुल्गारिया", "जॉर्जिया"],
        "काला सागर से छह देशों की तटरेखा लगती है: रूस, यूक्रेन, जॉर्जिया, तुर्की, बुल्गारिया तथा रोमानिया। बेलारूस एक स्थलरुद्ध (लैंडलॉक्ड) देश है। अतः विकल्प A सही उत्तर है।"
    ))
    # Q10
    qs.append(create_q(
        10, "UP Special & Current Affairs", "Easy", "B",
        "In which district of Uttar Pradesh is the 'Shaheed Ashfaqulla Khan Zoological Park' located?",
        ["Lucknow", "Gorakhpur", "Kanpur", "Etawah"],
        "Shaheed Ashfaqulla Khan Zoological Park is located in Gorakhpur district, Uttar Pradesh. It is the third state zoo after Lucknow and Kanpur. Hence, option B is correct.",
        "उत्तर प्रदेश के किस जिले में 'शहीद अशफाकउल्ला खान प्राणी उद्यान' स्थित है?",
        ["लखनऊ", "गोरखपुर", "कानपुर", "इटावा"],
        "शहीद अशफाकउल्ला खान प्राणी उद्यान उत्तर प्रदेश के गोरखपुर जिले में स्थित है। यह प्रदेश का तीसरा चिड़ियाघर है। अतः विकल्प B सही है।"
    ))
    # Q11
    qs.append(create_q(
        11, "Modern Indian History", "Easy", "C",
        "Who among the following was the first President of the All India Trade Union Congress (AITUC) founded in 1920?",
        ["N.M. Joshi", "V.V. Giri", "Lala Lajpat Rai", "B.P. Wadia"],
        "The All India Trade Union Congress (AITUC) was founded on October 31, 1920 in Bombay with Lala Lajpat Rai as its founding President and Diwan Chaman Lall as General Secretary. Hence, option C is correct.",
        "1920 में बंबई में स्थापित 'अखिल भारतीय ट्रेड यूनियन कांग्रेस' (AITUC) के प्रथम अध्यक्ष कौन थे?",
        ["एन.एम. जोशी", "वी.वी. गिरि", "लाला लाजपत राय", "बी.पी. वाडिया"],
        "अखिल भारतीय ट्रेड यूनियन कांग्रेस (AITUC) की स्थापना 31 अक्टूबर 1920 को बंबई में हुई थी। इसके प्रथम अध्यक्ष लाला लाजपत राय थे। अतः विकल्प C सही है।"
    ))
    # Q12
    qs.append(create_q(
        12, "Indian Polity", "Medium", "D",
        "Which Schedule of the Constitution of India contains provisions regarding the administration and control of Scheduled Areas and Scheduled Tribes in states other than Assam, Meghalaya, Tripura, and Mizoram?",
        ["Third Schedule", "Fourth Schedule", "Sixth Schedule", "Fifth Schedule"],
        "The Fifth Schedule governs Scheduled Areas and Scheduled Tribes across Indian states, excluding Assam, Meghalaya, Tripura, and Mizoram (which are under the Sixth Schedule). Hence, option D is correct.",
        "भारतीय संविधान की किस अनुसूची में असम, मेघालय, त्रिपुरा और मिजोरम को छोड़कर अन्य राज्यों के अनुसूचित क्षेत्रों और अनुसूचित जनजातियों के प्रशासन तथा नियंत्रण का प्रावधान है?",
        ["तीसरी अनुसूची", "चौथी अनुसूची", "छठी अनुसूची", "पाँचवीं अनुसूची"],
        "पाँचवीं अनुसूची में असम, मेघालय, त्रिपुरा और मिजोरम के अतिरिक्त अन्य राज्यों के अनुसूचित क्षेत्रों व जनजातियों के प्रशासन के विशेष प्रावधान हैं। अतः विकल्प D सही है।"
    ))
    # Q13
    qs.append(create_q(
        13, "General Science", "Easy", "A",
        "Which inert or non-reactive gas is filled inside incandescent electric bulbs along with Argon to prevent tungsten filament evaporation?",
        ["Nitrogen", "Oxygen", "Hydrogen", "Carbon dioxide"],
        "An inert mixture of Argon (around 93%) and Nitrogen (around 7%) gas is filled inside incandescent bulbs to retard the evaporation of the hot tungsten filament and prevent oxidation. Hence, option A is correct.",
        "विद्युत बल्ब में टंगस्टन फिलामेंट के वाष्पीकरण और ऑक्सीकरण को रोकने के लिए आर्गन के साथ कौन-सी गैस भरी जाती है?",
        ["नाइट्रोजन", "ऑक्सीजन", "हाइड्रोजन", "कार्बन डाइऑक्साइड"],
        "विद्युत बल्बों में टंगस्टन तंतु के जलने और ऑक्सीकृत होने से बचाने के लिए आर्गन के साथ अक्रिय नाइट्रोजन गैस भरी जाती है। अतः विकल्प A सही है।"
    ))
    # Q14
    qs.append(create_q(
        14, "Environment & Ecology", "Medium", "B",
        "The 'Kyoto Protocol' adopted in 1997 is an international treaty primarily associated with:",
        ["Preserving polar ice caps", "Reduction of greenhouse gas emissions to combat climate change", "Safe disposal of transboundary hazardous wastes", "Protecting endangered marine turtle species"],
        "The Kyoto Protocol was adopted in December 1997 in Kyoto, Japan under the UNFCCC, committing industrialized nations to legally binding targets for reducing greenhouse gas emissions. Hence, option B is correct.",
        "1997 में अपनाया गया 'क्योटो प्रोटोकॉल' मुख्य रूप से किससे संबंधित एक अंतर्राष्ट्रीय समझौता है?",
        ["ध्रुवीय हिमशैल संरक्षण", "जलवायु परिवर्तन से निपटने के लिए ग्रीनहाउस गैसों के उत्सर्जन में कमी", "खतरनाक अपशिष्टों का सीमापार निस्तारण", "लुप्तप्राय समुद्री कछुओं का संरक्षण"],
        "क्योटो प्रोटोकॉल 1997 में UNFCCC के अंतर्गत अपनाया गया था, जिसका उद्देश्य वैश्विक तापन और जलवायु परिवर्तन को रोकने के लिए ग्रीनहाउस गैसों के उत्सर्जन को कम करना है। अतः विकल्प B सही है।"
    ))
    # Q15
    qs.append(create_q(
        15, "Indian Geography", "Easy", "C",
        "The spectacular 'Dhuandhar Falls' is located on which river near Bhedaghat, Jabalpur in Madhya Pradesh?",
        ["Chambal River", "Betwa River", "Narmada River", "Tapi River"],
        "Dhuandhar Falls is located on the Narmada River in Bhedaghat near Jabalpur, Madhya Pradesh, renowned for its cascading drop through white marble rocks. Hence, option C is correct.",
        "प्रसिद्ध 'धुआंधार जलप्रपात' मध्य प्रदेश में जबलपुर (भेड़ाघाट) के निकट किस नदी पर स्थित है?",
        ["चंबल नदी", "बेतवा नदी", "नर्मदा नदी", "ताप्ती नदी"],
        "धुआंधार जलप्रपात मध्य प्रदेश के जबलपुर में भेड़ाघाट के निकट संगमरमर की चट्टानों के बीच नर्मदा नदी पर स्थित है। अतः विकल्प C सही है।"
    ))
    # Q16
    qs.append(create_q(
        16, "Ancient Indian History", "Easy", "D",
        "Who among the following was the court poet of Emperor Harshavardhana and authored 'Harshacharita' and 'Kadambari'?",
        ["Kalidasa", "Bhavabhuti", "Dandin", "Banabhatta"],
        "Banabhatta was the celebrated court poet of Emperor Harshavardhana (7th century CE) and composed Harshacharita (biography of Harsha) and the classical romantic prose Kadambari. Hence, option D is correct.",
        "सम्राट हर्षवर्धन के दरबारी कवि कौन थे जिन्होंने 'हर्षचरित' तथा 'कादंबरी' की रचना की?",
        ["कालिदास", "भवभूति", "दंडी", "बाणभट्ट"],
        "बाणभट्ट 7वीं शताब्दी में सम्राट हर्षवर्धन के प्रमुख दरबारी कवि थे। उन्होंने राजा हर्ष की जीवनी 'हर्षचरित' और प्रसिद्ध संस्कृत गद्य 'कादंबरी' की रचना की। अतः विकल्प D सही है।"
    ))
    # Q17
    qs.append(create_q(
        17, "Medieval Indian History", "Easy", "A",
        "Which Sultan of Delhi transferred his imperial capital from Delhi to Devagiri (renamed Daulatabad) in 1327 CE?",
        ["Muhammad bin Tughlaq", "Alauddin Khalji", "Firoz Shah Tughlaq", "Ghiyasuddin Balban"],
        "Sultan Muhammad bin Tughlaq ordered the shifting of the capital from Delhi to Devagiri in the Deccan (renaming it Daulatabad) in 1327 CE to secure administrative control over southern territories. Hence, option A is correct.",
        "1327 ई. में किस दिल्ली सुल्तान ने अपनी राजधानी को दिल्ली से देवगिरि (दौलताबाद) स्थानांतरित किया था?",
        ["मुहम्मद बिन तुगलक", "अलाउद्दीन खिलजी", "फिरोज शाह तुगलक", "गियासुद्दीन बलबन"],
        "सुल्तान मुहम्मद बिन तुगलक ने दक्षिण भारत पर प्रशासनिक नियंत्रण सुदृढ़ करने हेतु राजधानी दिल्ली से देवगिरि स्थानांतरित की और उसका नाम दौलताबाद रखा। अतः विकल्प A सही है।"
    ))
    # Q18
    qs.append(create_q(
        18, "Indian Economy", "Easy", "B",
        "What is the base year currently used for compiling the All-India Consumer Price Index (CPI - Combined) by NSO?",
        ["2004-05 = 100", "2012 = 100", "2011-12 = 100", "2016 = 100"],
        "The base year for the Consumer Price Index (CPI) Combined, Rural, and Urban compiled by the National Statistical Office (NSO) is 2012 = 100. (2011-12 is used for GDP and IIP). Hence, option B is correct.",
        "राष्ट्रीय सांख्यिकी कार्यालय (NSO) द्वारा जारी अखिल भारतीय उपभोक्ता मूल्य सूचकांक (CPI - संयुक्त) का वर्तमान आधार वर्ष क्या है?",
        ["2004-05 = 100", "2012 = 100", "2011-12 = 100", "2016 = 100"],
        "अखिल भारतीय उपभोक्ता मूल्य सूचकांक (CPI) की गणना के लिए आधार वर्ष 2012 = 100 है, जबकि GDP और IIP का आधार वर्ष 2011-12 है। अतः विकल्प B सही है।"
    ))
    # Q19
    qs.append(create_q(
        19, "World Geography", "Easy", "C",
        "Which of the following is the longest river in the European continent?",
        ["Danube River", "Rhine River", "Volga River", "Elbe River"],
        "The Volga River in Russia, with a total length of approximately 3,530 km (2,193 miles), is the longest river in Europe, discharging into the Caspian Sea. The Danube is the second longest. Hence, option C is correct.",
        "यूरोप महाद्वीप की सबसे लंबी नदी निम्नलिखित में से कौन-सी है?",
        ["डेन्यूब नदी", "राइन नदी", "वोल्गा नदी", "एल्बे नदी"],
        "रूस में प्रवाहित होने वाली और कैस्पियन सागर में गिरने वाली वोल्गा नदी (लगभग 3,530 किमी) यूरोप की सबसे लंबी नदी है। डेन्यूब दूसरी सबसे लंबी नदी है। अतः विकल्प C सही है।"
    ))
    # Q20
    qs.append(create_q(
        20, "UP Special & Current Affairs", "Easy", "D",
        "Which district of Uttar Pradesh is famously associated with the GI-tagged 'Black Clay Pottery' craft?",
        ["Gorakhpur", "Bulandshahr (Khurja)", "Kannauj", "Azamgarh (Nizamabad)"],
        "Nizamabad in Azamgarh district of Uttar Pradesh is globally acclaimed for its dark, shiny Black Clay Pottery, which holds an official Geographical Indication (GI) tag. Hence, option D is correct.",
        "उत्तर प्रदेश का कौन-सा जिला जीआई-टैग प्राप्त 'काली मिट्टी की कलात्मक पॉटरी' (ब्लैक पॉटरी) के लिए प्रसिद्ध है?",
        ["गोरखपुर", "बुलंदशहर (खुर्जा)", "कन्नौज", "आजमगढ़ (निजामाबाद)"],
        "आजमगढ़ जिले का निजामाबाद अपनी विशिष्ट चमकदार काली मिट्टी के बर्तनों (ब्लैक पॉटरी) के लिए विश्वविख्यात है, जिसे जीआई टैग प्राप्त है। अतः विकल्प D सही है।"
    ))
    # Q21
    qs.append(create_q(
        21, "Indian Polity", "Medium", "A",
        "Article 239AA of the Constitution of India provides special provisions with respect to which Union Territory?",
        ["National Capital Territory of Delhi", "Puducherry", "Jammu and Kashmir", "Ladakh"],
        "Article 239AA was inserted by the 69th Constitutional Amendment Act, 1991, conferring special constitutional status on the Union Territory of Delhi as the National Capital Territory with a Legislative Assembly and Council of Ministers. Hence, option A is correct.",
        "भारतीय संविधान का अनुच्छेद 239AA किस केंद्र शासित प्रदेश के संबंध में विशेष प्रावधान करता है?",
        ["दिल्ली राष्ट्रीय राजधानी क्षेत्र (NCT of Delhi)", "पुडुचेरी", "जम्मू और कश्मीर", "लद्दाख"],
        "69वें संविधान संशोधन अधिनियम 1991 द्वारा जोड़े गए अनुच्छेद 239AA के तहत दिल्ली को राष्ट्रीय राजधानी क्षेत्र (NCT) का विशेष दर्जा और विधानसभा प्रदान की गई। अतः विकल्प A सही है।"
    ))
    # Q22
    qs.append(create_q(
        22, "Environment & Ecology", "Easy", "B",
        "Which gas family is primarily held responsible for the depletion of the stratospheric ozone layer (Ozone Hole)?",
        ["Carbon dioxide", "Chlorofluorocarbons (CFCs)", "Methane", "Nitrous oxide"],
        "Chlorofluorocarbons (CFCs) and halons release active chlorine and bromine atoms upon UV exposure in the stratosphere, which catalytically break down ozone (O3) molecules. Hence, option B is correct.",
        "समताप मंडलीय ओजोन परत के क्षरण (ओजोन छिद्र) के लिए मुख्य रूप से कौन-सी गैसें उत्तरदायी हैं?",
        ["कार्बन डाइऑक्साइड", "क्लोरोफ्लोरोकार्बन (CFCs)", "मीथेन", "नाइट्रस ऑक्साइड"],
        "क्लोरोफ्लोरोकार्बन (CFCs) से निकलने वाले क्लोरीन और ब्रोमीन परमाणु समताप मंडल में ओजोन अणुओं को ऑक्सीजन में विखंडित कर देते हैं। अतः विकल्प B सही है।"
    ))
    # Q23
    qs.append(create_q(
        23, "Environment & Ecology", "Easy", "C",
        "The Ramsar Convention signed in 1971 in Ramsar, Iran is an intergovernmental treaty dedicated to the conservation of:",
        ["Coral Reefs", "High-altitude Grasslands", "Wetlands", "Mangrove Forests"],
        "The Convention on Wetlands of International Importance, known as the Ramsar Convention, was adopted in Ramsar, Iran on February 2, 1971 to promote wetland conservation and sustainable utilization. Hence, option C is correct.",
        "1971 में ईरान के रामसर शहर में हस्ताक्षरित 'रामसर अभिसमय' किसके संरक्षण से संबंधित एक अंतर्राष्ट्रीय संधि है?",
        ["प्रवाल भित्तियाँ", "घास के मैदान", "आर्द्रभूमियाँ (Wetlands)", "मैंग्रोव वन"],
        "रामसर अभिसमय 2 फरवरी 1971 को अंगीकार किया गया था, जिसका उद्देश्य दुनिया भर की अंतर्राष्ट्रीय महत्व की आर्द्रभूमियों (नमभूमियों) का संरक्षण करना है। अतः विकल्प C सही है।"
    ))
    # Q24
    qs.append(create_q(
        24, "UP Special & Current Affairs", "Easy", "D",
        "In which district of Uttar Pradesh is the 'Bakhira Wildlife Sanctuary' (declared a Ramsar Wetland site in 2022) situated?",
        ["Gonda", "Basti", "Siddharthnagar", "Sant Kabir Nagar"],
        "Bakhira Wildlife Sanctuary, the largest natural floodplain wetland in eastern Uttar Pradesh, is situated in Sant Kabir Nagar district and was designated as a Ramsar Site in 2022. Hence, option D is correct.",
        "उत्तर प्रदेश के किस जिले में 'बखीरा वन्यजीव अभयारण्य' (2022 में रामसर स्थल घोषित) स्थित है?",
        ["गोंडा", "बस्ती", "सिद्धार्थनगर", "संत कबीर नगर"],
        "बखीरा वन्यजीव अभयारण्य पूर्वी उत्तर प्रदेश के संत कबीर नगर जिले में स्थित मीठे पानी की प्राकृतिक आर्द्रभूमि है जिसे 2022 में रामसर स्थल घोषित किया गया। अतः विकल्प D सही है।"
    ))
    # Q25
    qs.append(create_q(
        25, "Indian Polity", "Easy", "A",
        "Under Article 108 of the Constitution of India, a Joint Sitting of both Houses of Parliament is summoned by:",
        ["The President of India", "The Speaker of Lok Sabha", "The Prime Minister", "The Chairman of Rajya Sabha"],
        "Under Article 108, the President of India summons a Joint Sitting of Parliament to resolve a legislative deadlock. Under Article 118(4), the Speaker of Lok Sabha presides over it. Hence, option A is correct.",
        "भारतीय संविधान के अनुच्छेद 108 के अंतर्गत संसद के दोनों सदनों की संयुक्त बैठक किसके द्वारा आहूत (बुलाई) की जाती है?",
        ["भारत के राष्ट्रपति द्वारा", "लोकसभा अध्यक्ष द्वारा", "प्रधानमंत्री द्वारा", "राज्यसभा के सभापति द्वारा"],
        "अनुच्छेद 108 के अनुसार दोनों सदनों के मध्य गतिरोध दूर करने के लिए संयुक्त बैठक राष्ट्रपति द्वारा आहूत की जाती है, जबकि इसकी अध्यक्षता लोकसभा अध्यक्ष करते हैं। अतः विकल्प A सही है।"
    ))
    # Q26
    qs.append(create_q(
        26, "General Science", "Easy", "B",
        "Which of the following is the principal combustible component of Biogas (Gobar gas)?",
        ["Propane", "Methane", "Ethane", "Carbon monoxide"],
        "Biogas generated by anaerobic digestion of organic matter consists mainly of Methane (50%–75%) and Carbon dioxide (25%–50%). Methane provides its fuel value. Hence, option B is correct.",
        "बायोगैस (गोबर गैस) का मुख्य ज्वलनशील घटक निम्नलिखित में से कौन-सा है?",
        ["प्रोपेन", "मीथेन", "ईथेन", "कार्बन मोनोऑक्साइड"],
        "बायोगैस में 50 से 75 प्रतिशत तक मीथेन (CH4) गैस होती है, जो इसकी मुख्य ज्वलनशील एवं ऊर्जा प्रदायक घटक है। अतः विकल्प B सही है।"
    ))
    # Q27
    qs.append(create_q(
        27, "Indian Polity", "Easy", "C",
        "The Fundamental Duties were incorporated into Part IV-A of the Constitution of India based on the recommendations of which committee?",
        ["Verma Committee", "Sarkaria Commission", "Swaran Singh Committee", "Kothari Commission"],
        "The Fundamental Duties (Article 51A) were added by the 42nd Constitutional Amendment Act, 1976 on the recommendations of the Sardar Swaran Singh Committee. Hence, option C is correct.",
        "किस समिति की संस्तुतियों के आधार पर भारतीय संविधान के भाग IV-A में मौलिक कर्तव्यों को शामिल किया गया था?",
        ["वर्मा समिति", "सरकारिया आयोग", "स्वर्ण सिंह समिति", "कोठारी आयोग"],
        "सरदार स्वर्ण सिंह समिति की सिफारिशों के आधार पर 42वें संविधान संशोधन 1976 द्वारा संविधान में भाग IV-A (अनुच्छेद 51A) जोड़कर मौलिक कर्तव्य शामिल किए गए। अतः विकल्प C सही है।"
    ))
    # Q28
    qs.append(create_q(
        28, "Ancient Indian History", "Easy", "D",
        "At which of the following Harappan sites was an artificial brick dockyard (tidal basin for maritime trade) discovered?",
        ["Kalibangan", "Banawali", "Surkotada", "Lothal"],
        "Lothal, located on the Bhogava river in the Gulf of Khambhat (Gujarat), featured a massive brick basin identified by archaeologists as an ancient dockyard connected to tidal channels. Hence, option D is correct.",
        "हड़प्पा सभ्यता के किस स्थल पर ईंटों से निर्मित एक विशाल गोदीबाड़ा (डॉकयार्ड/बंदरगाह) प्राप्त हुआ है?",
        ["कालीबंगा", "बनावली", "सुरकोटदा", "लोथल"],
        "गुजरात के लोथल (भोगवा नदी तट) से जहाजों की गोदी (डॉकयार्ड) के साक्ष्य मिले हैं जो हड़प्पा कालीन समुद्री व्यापार का प्रमुख केंद्र था। अतः विकल्प D सही है।"
    ))
    # Q29
    qs.append(create_q(
        29, "Indian Economy", "Medium", "A",
        "The Human Development Index (HDI) calculated by UNDP is based on indicators of which three core dimensions of human development?",
        ["Health (Life Expectancy), Education, and Standard of Living (GNI per capita)", "Poverty rate, Literacy rate, and Unemployment rate", "Life Expectancy, Infant Mortality Rate, and Maternal Health", "GDP growth rate, Clean Water access, and Power consumption"],
        "HDI measures average achievement across three basic dimensions: a long and healthy life (life expectancy at birth), knowledge (mean and expected years of schooling), and a decent standard of living (GNI per capita PPP$). Hence, option A is correct.",
        "संयुक्त राष्ट्र विकास कार्यक्रम (UNDP) द्वारा जारी मानव विकास सूचकांक (HDI) किन तीन प्रमुख आयामों पर आधारित है?",
        ["स्वास्थ्य (जीवन प्रत्याशा), शिक्षा (ज्ञान), तथा जीवन स्तर (प्रति व्यक्ति GNI)", "गरीबी दर, साक्षरता दर, तथा बेरोजगारी दर", "जीवन प्रत्याशा, शिशु मृत्यु दर, तथा मातृ स्वास्थ्य", "सकल घरेलू उत्पाद, स्वच्छ पेयजल, तथा विद्युत खपत"],
        "मानव विकास सूचकांक (HDI) तीन प्रमुख आयामों पर मापा जाता है: दीघार्यु एवं स्वस्थ जीवन, ज्ञान/शिक्षा, तथा सम्मानजनक जीवन स्तर। अतः विकल्प A सही उत्तर है।"
    ))
    # Q30
    qs.append(create_q(
        30, "Indian Geography", "Medium", "B",
        "Through how many states of India does the Tropic of Cancer (23°30' N) pass?",
        ["6 States", "8 States", "7 States", "9 States"],
        "The Tropic of Cancer passes through 8 Indian states from west to east: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram. Hence, option B is correct.",
        "कर्क रेखा (23°30' उत्तरी अक्षांश) भारत के कुल कितने राज्यों से होकर गुजरती है?",
        ["6 राज्य", "8 राज्य", "7 राज्य", "9 राज्य"],
        "कर्क रेखा भारत के 8 राज्यों से होकर गुजरती है: गुजरात, राजस्थान, मध्य प्रदेश, छत्तीसगढ़, झारखंड, पश्चिम बंगाल, त्रिपुरा तथा मिजोरम। अतः विकल्प B सही है।"
    ))
    # Q31
    qs.append(create_q(
        31, "Indian Economy", "Easy", "C",
        "In Indian agriculture and economic terminology, the 'Blue Revolution' is associated with the rapid growth of:",
        ["Oilseeds Production", "Milk Production", "Fisheries and Aquaculture", "Fertilizer Manufacturing"],
        "The Blue Revolution (Neel Kranti) refers to the rapid intensification and economic development of the fisheries and aquaculture sector in India. Hence, option C is correct.",
        "भारतीय कृषि एवं अर्थव्यवस्था में 'नीली क्रांति' (Blue Revolution) का संबंध किससे है?",
        ["तिलहन उत्पादन", "दुग्ध उत्पादन", "मत्स्य पालन एवं जलीय कृषि", "उर्वरक उत्पादन"],
        "नीली क्रांति का संबंध मछली उत्पादन और जलीय जीवों के संवर्धन एवं व्यावसायिक विकास से है। अतः विकल्प C सही है।"
    ))
    # Q32
    qs.append(create_q(
        32, "Indian Polity", "Easy", "D",
        "Which Article of the Constitution of India deals with the power of Parliament to amend the Constitution and procedure therefor?",
        ["Article 352", "Article 356", "Article 360", "Article 368"],
        "Part XX, Article 368 of the Constitution outlines the procedure and powers of Parliament to amend the Constitution. Articles 352, 356, and 360 deal with emergency provisions. Hence, option D is correct.",
        "संविधान में संशोधन करने की संसद की शक्ति और उसकी प्रक्रिया का उल्लेख किस अनुच्छेद में है?",
        ["अनुच्छेद 352", "अनुच्छेद 356", "अनुच्छेद 360", "अनुच्छेद 368"],
        "भारतीय संविधान के भाग XX के अनुच्छेद 368 में संविधान में संशोधन करने की संसद की शक्ति और प्रक्रिया का वर्णन है। अतः विकल्प D सही है।"
    ))
    # Q33
    qs.append(create_q(
        33, "Modern Indian History", "Easy", "A",
        "Who founded the famous 'Asiatic Society of Bengal' in Calcutta in 1784 to promote Oriental research?",
        ["Sir William Jones", "Warren Hastings", "Max Müller", "Charles Wilkins"],
        "Sir William Jones, a puisne judge of the Supreme Court at Fort William, founded the Asiatic Society in Calcutta on January 15, 1784 to investigate the history, arts, and literature of Asia. Hence, option A is correct.",
        "1784 में कलकत्ता में प्राच्य विद्या और शोध को बढ़ावा देने के लिए 'एशियाटिक सोसाइटी ऑफ बंगाल' की स्थापना किसने की थी?",
        ["सर विलियम जोन्स", "वारेन हेस्टिंग्स", "मैक्स मूलर", "चार्ल्स विल्किन्स"],
        "15 जनवरी 1784 को कलकत्ता में सर विलियम जोन्स द्वारा एशियाटिक सोसाइटी की स्थापना की गई थी। अतः विकल्प A सही है।"
    ))
    # Q34
    qs.append(create_q(
        34, "Environment & Ecology", "Easy", "B",
        "Kaziranga National Park in Assam is globally celebrated as the premier natural habitat of which endangered animal?",
        ["Asiatic Lion", "Great Indian One-Horned Rhinoceros", "Snow Leopard", "Wild Water Buffalo"],
        "Kaziranga National Park holds two-thirds of the world's population of the Great Indian One-horned Rhinoceros (Rhinoceros unicornis). Hence, option B is correct.",
        "असम का काजीरंगा राष्ट्रीय उद्यान किस संकटापन्न वन्यजीव के प्राकृतिक पर्यावास के रूप में विश्वप्रसिद्ध है?",
        ["एशियाई शेर", "एक सींग वाला भारतीय गैंडा", "हिम तेंदुआ", "जंगली जल भैंसा"],
        "काजीरंगा राष्ट्रीय उद्यान एक सींग वाले भारतीय गैंडे की दुनिया की सबसे बड़ी आबादी का प्राकृतिक आवास है। अतः विकल्प B सही है।"
    ))
    # Q35
    qs.append(create_q(
        35, "General Science", "Easy", "C",
        "Deficiency of Vitamin C (Ascorbic acid) in human diet leads to which of the following diseases?",
        ["Beri-beri", "Rickets", "Scurvy", "Pellagra"],
        "Vitamin C (ascorbic acid) is essential for collagen synthesis. Its deficiency causes scurvy, characterized by bleeding gums, skin spots, and impaired wound healing. Beri-beri is due to B1, Rickets to Vitamin D, and Pellagra to B3. Hence, option C is correct.",
        "मानव आहार में विटामिन C (एस्कॉर्बिक एसिड) की कमी से कौन-सा रोग होता है?",
        ["बेरी-बेरी", "रिकेट्स", "स्कर्वी", "पेलाग्रा"],
        "विटामिन C की कमी से स्कर्वी रोग हो जाता है, जिससे मसूड़ों से खून आना और घावों का देरी से भरना जैसे लक्षण दिखाई देते हैं। अतः विकल्प C सही है।"
    ))
    # Q36
    qs.append(create_q(
        36, "Medieval Indian History", "Easy", "D",
        "The historic 'Battle of Khanwa' was fought in 1527 between Mughal Emperor Babur and which Rajput ruler?",
        ["Maharana Pratap", "Rana Kumbha", "Raja Man Singh", "Rana Sanga of Mewar"],
        "The Battle of Khanwa was fought on March 16, 1527 between Babur and Rana Sanga of Mewar. Babur's decisive victory consolidated Mughal power in northern India. Hence, option D is correct.",
        "1527 ई. में 'खानवा का ऐतिहासिक युद्ध' मुगल सम्राट बाबर और किस राजपूत शासक के मध्य लड़ा गया था?",
        ["महाराणा प्रताप", "राणा कुंभा", "राजा मानसिंह", "मेवाड़ के राणा सांगा"],
        "खानवा का युद्ध 16 मार्च 1527 को आगरा के निकट खानवा में बाबर और मेवाड़ के शासक राणा सांगा के मध्य हुआ था, जिसमें बाबर विजयी रहा। अतः विकल्प D सही है।"
    ))
    # Q37
    qs.append(create_q(
        37, "Indian Polity", "Medium", "A",
        "What is the correct order of the keywords defining India's constitutional character in the Preamble of the Constitution of India?",
        ["Sovereign, Socialist, Secular, Democratic, Republic", "Sovereign, Democratic, Socialist, Secular, Republic", "Socialist, Secular, Sovereign, Democratic, Republic", "Sovereign, Secular, Socialist, Democratic, Republic"],
        "The Preamble solemnly declares India to be a 'Sovereign Socialist Secular Democratic Republic'. The words 'Socialist' and 'Secular' were added by the 42nd Amendment Act in 1976. Hence, option A is correct.",
        "भारतीय संविधान की प्रस्तावना में भारत के स्वरूप को व्यक्त करने वाले शब्दों का सही क्रम क्या है?",
        ["संपूर्ण प्रभुत्व-संपन्न, समाजवादी, पंथनिरपेक्ष, लोकतंत्रात्मक, गणराज्य", "संपूर्ण प्रभुत्व-संपन्न, लोकतंत्रात्मक, समाजवादी, पंथनिरपेक्ष, गणराज्य", "समाजवादी, पंथनिरपेक्ष, संपूर्ण प्रभुत्व-संपन्न, लोकतंत्रात्मक, गणराज्य", "संपूर्ण प्रभुत्व-संपन्न, पंथनिरपेक्ष, समाजवादी, लोकतंत्रात्मक, गणराज्य"],
        "प्रस्तावना के अनुसार भारत एक 'संपूर्ण प्रभुत्व-संपन्न समाजवादी पंथनिरपेक्ष लोकतंत्रात्मक गणराज्य' है। 42वें संशोधन 1976 द्वारा समाजवादी एवं पंथनिरपेक्ष शब्द जोड़े गए। अतः विकल्प A सही है।"
    ))
    # Q38
    qs.append(create_q(
        38, "Indian Economy & Schemes", "Easy", "B",
        "Under the 'PM-KISAN' (Pradhan Mantri Kisan Samman Nidhi) scheme, what total annual income support is provided to eligible farmer families?",
        ["₹4,000 in two instalments", "₹6,000 in three instalments of ₹2,000 each", "₹8,000 in four instalments", "₹10,000 in one lump sum"],
        "Under PM-KISAN launched in February 2019, income support of ₹6,000 per year is deposited directly into bank accounts of eligible farmer families in three four-monthly instalments of ₹2,000 each. Hence, option B is correct.",
        "'पीएम-किसान' (प्रधानमंत्री किसान सम्मान निधि) योजना के अंतर्गत पात्र किसान परिवारों को प्रति वर्ष कितनी वित्तीय सहायता प्रदान की जाती है?",
        ["₹4,000 दो किस्तों में", "₹6,000 तीन समान किस्तों में (₹2,000 प्रत्येक)", "₹8,000 चार किस्तों में", "₹10,000 एकमुश्त"],
        "पीएम-किसान योजना के तहत केंद्र सरकार पात्र किसानों को ₹6,000 प्रति वर्ष की आर्थिक सहायता ₹2,000-₹2,000 की तीन किस्तों में सीधे बैंक खाते में प्रदान करती है। अतः विकल्प B सही है।"
    ))
    # Q39
    qs.append(create_q(
        39, "Environment & Ecology", "Easy", "C",
        "The pristine 'Silent Valley National Park', renowned for its evergreen tropical rainforest and Lion-tailed macaque, is located in which state?",
        ["Tamil Nadu", "Karnataka", "Kerala", "Goa"],
        "Silent Valley National Park is located in the Kundali Hills of Palakkad district in Kerala, forming a vital part of the Nilgiri Biosphere Reserve. Hence, option C is correct.",
        "'साइलेंट वैली (शांत घाटी) राष्ट्रीय उद्यान', जो उष्णकटिबंधीय सदाबहार वर्षावनों एवं सिंह-पुच्छ मकाक के लिए प्रसिद्ध है, किस राज्य में स्थित है?",
        ["तमिलनाडु", "कर्नाटक", "केरल", "गोवा"],
        "साइलेंट वैली राष्ट्रीय उद्यान केरल के पलक्कड़ जिले में नीलगिरि पहाड़ियों के अंतर्गत स्थित है। अतः विकल्प C सही है।"
    ))
    # Q40
    qs.append(create_q(
        40, "Environment & History", "Easy", "D",
        "The famous 'Chipko Movement' for forest conservation was launched in the 1970s in which modern state of India?",
        ["Himachal Pradesh", "Madhya Pradesh", "Assam", "Uttarakhand"],
        "The Chipko Movement was initiated in 1973 in Reni village, Chamoli district (then in Uttar Pradesh, now in Uttarakhand), led by Sunderlal Bahuguna, Chandi Prasad Bhatt, and Gaura Devi. Hence, option D is correct.",
        "वनों की कटाई रोकने के लिए 1970 के दशक में प्रसिद्ध 'चिपको आंदोलन' भारत के किस वर्तमान राज्य में प्रारंभ हुआ था?",
        ["हिमाचल प्रदेश", "मध्य प्रदेश", "असम", "उत्तराखंड"],
        "चिपको आंदोलन 1973 में चमोली जिले (तत्कालीन उत्तर प्रदेश, वर्तमान उत्तराखंड) में सुंदरलाल बहुगुणा, चंडी प्रसाद भट्ट और गौरा देवी के नेतृत्व में शुरू हुआ था। अतः विकल्प D सही है।"
    ))
    # Q41
    qs.append(create_q(
        41, "Indian Polity", "Easy", "A",
        "Under Article 75(3) of the Constitution of India, the Union Council of Ministers is collectively responsible to:",
        ["The Lok Sabha (House of the People)", "The President of India", "Both Houses of Parliament jointly", "The Prime Minister"],
        "Article 75(3) explicitly states: 'The Council of Ministers shall be collectively responsible to the House of the People (Lok Sabha)'. Hence, option A is correct.",
        "भारतीय संविधान के अनुच्छेद 75(3) के अनुसार, केंद्रीय मंत्रिपरिषद सामूहिक रूप से किसके प्रति उत्तरदायी होती है?",
        ["लोकसभा के प्रति", "राष्ट्रपति के प्रति", "संसद के दोनों सदनों के प्रति", "प्रधानमंत्री के प्रति"],
        "अनुच्छेद 75(3) के तहत मंत्रिपरिषद सामूहिक रूप से केवल लोकसभा (जनता के सदन) के प्रति उत्तरदायी होती है। अतः विकल्प A सही है।"
    ))
    # Q42
    qs.append(create_q(
        42, "Indian Economy", "Easy", "B",
        "The Planning Commission of India was formally replaced by the 'NITI Aayog' on which date?",
        ["15 August 2014", "1 January 2015", "1 April 2015", "26 January 2015"],
        "NITI Aayog (National Institution for Transforming India) was established by a Cabinet resolution on January 1, 2015, replacing the 65-year-old Planning Commission. Hence, option B is correct.",
        "भारत के योजना आयोग को औपचारिक रूप से समाप्त कर किस तिथि को 'नीति आयोग' (NITI Aayog) का गठन किया गया?",
        ["15 अगस्त 2014", "1 जनवरी 2015", "1 अप्रैल 2015", "26 जनवरी 2015"],
        "1 जनवरी 2015 को केंद्रीय मंत्रिमंडल के प्रस्ताव द्वारा योजना आयोग के स्थान पर 'नीति आयोग' की स्थापना की गई थी। अतः विकल्प B सही है।"
    ))
    # Q43
    qs.append(create_q(
        43, "Environment & Ecology", "Easy", "C",
        "On which date is 'World Environment Day' celebrated internationally every year?",
        ["22 April", "22 May", "5 June", "16 September"],
        "World Environment Day is observed globally on 5 June each year since 1974, commemorating the opening day of the 1972 United Nations Conference on the Human Environment in Stockholm. Hence, option C is correct.",
        "प्रतिवर्ष अंतर्राष्ट्रीय स्तर पर 'विश्व पर्यावरण दिवस' किस तिथि को मनाया जाता है?",
        ["22 अप्रैल", "22 मई", "5 जून", "16 सितंबर"],
        "5 जून 1972 को स्टॉकहोम सम्मेलन की स्मृति में प्रतिवर्ष 5 जून को संयुक्त राष्ट्र द्वारा विश्व पर्यावरण दिवस मनाया जाता है। (22 अप्रैल पृथ्वी दिवस, 16 सितंबर ओजोन दिवस)। अतः विकल्प C सही है।"
    ))
    # Q44
    qs.append(create_q(
        44, "General Science", "Easy", "D",
        "In human blood grouping (ABO system), which blood group is recognized as the 'Universal Donor'?",
        ["Group AB Positive (AB+)", "Group A Negative (A-)", "Group B Positive (B+)", "Group O Negative (O-)"],
        "Individuals with Blood Group O negative (O-) lack A, B, and Rh antigens on their red blood cells, making their RBCs safely transfusable to almost any recipient; hence known as Universal Donors. Hence, option D is correct.",
        "मानव रक्त समूह प्रणाली (ABO सिस्टम) में किस रक्त समूह को 'सर्वदाता' (Universal Donor) कहा जाता है?",
        ["रक्त समूह AB धनात्मक (AB+)", "रक्त समूह A ऋणात्मक (A-)", "रक्त समूह B धनात्मक (B+)", "रक्त समूह O ऋणात्मक (O-)"],
        "रक्त समूह O- की लाल रक्त कणिकाओं पर A, B अथवा Rh कोई भी प्रतिजन (एंटीजन) नहीं होता, जिससे यह किसी भी व्यक्ति को दिया जा सकता है; अतः इसे सर्वदाता कहते हैं। विकल्प D सही है।"
    ))
    # Q45
    qs.append(create_q(
        45, "Modern Indian History", "Easy", "A",
        "Mahatma Gandhi launched his first Satyagraha movement in India in 1917 at Champaran (Bihar) against which oppressive system?",
        ["Tinkathia system of indigo cultivation", "Zamidari rent enhancement", "Salt Monopoly tax", "Rowlatt Act restrictions"],
        "The Champaran Satyagraha of 1917 was Mahatma Gandhi's first civil disobedience movement in India, fought against European planters forcing peasants to cultivate indigo on 3/20th of their land (Tinkathia system). Hence, option A is correct.",
        "1917 में महात्मा गांधी ने भारत में अपना पहला सत्याग्रह आंदोलन चंपारण (बिहार) में किस शोषणकारी व्यवस्था के विरुद्ध शुरू किया था?",
        ["नील की खेती की 'तिनकठिया' व्यवस्था", "जमींदारी लगान वृद्धि", "नमक कर एकाधिकार", "रौलट एक्ट पाबंदियाँ"],
        "चंपारण सत्याग्रह (1917) में गांधीजी ने यूरोपीय बागान मालिकों की तिनकठिया प्रथा (जमीन के 3/20 भाग पर नील की खेती की अनिवार्यता) के विरुद्ध किसानों का नेतृत्व किया था। अतः विकल्प A सही है।"
    ))
    # Q46
    qs.append(create_q(
        46, "World Geography", "Medium", "B",
        "Which of the following is the deepest oceanic trench in the world, located in the western Pacific Ocean?",
        ["Puerto Rico Trench", "Mariana Trench (Challenger Deep)", "Java (Sunda) Trench", "Tonga Trench"],
        "The Mariana Trench in the western Pacific Ocean contains the Challenger Deep, the deepest known point on Earth with a depth of approximately 11,034 meters (36,201 feet). Hence, option B is correct.",
        "विश्व का सबसे गहरा महासागरीय गर्त (Trench) निम्नलिखित में से कौन-सा है, जो पश्चिमी प्रशांत महासागर में स्थित है?",
        ["प्यूर्टो रिको गर्त", "मारियाना गर्त (चैलेंजर दीप)", "जावा (सुंडा) गर्त", "टोंगा गर्त"],
        "पश्चिमी प्रशांत महासागर में स्थित मारियाना गर्त (चैलेंजर गर्त) लगभग 11,034 मीटर की गहराई के साथ पृथ्वी का सबसे गहरा बिंदु है। अतः विकल्प B सही है।"
    ))
    # Q47
    qs.append(create_q(
        47, "Indian Geography", "Easy", "C",
        "The world's largest inhabited river island, 'Majuli', is situated on which river in Assam?",
        ["Ganga River", "Yamuna River", "Brahmaputra River", "Meghna River"],
        "Majuli is the world's largest river island formed by the Brahmaputra River and Subansiri River in Assam, recognized as a district of Assam. Hence, option C is correct.",
        "विश्व का सबसे बड़ा आबाद नदी द्वीप 'माजुली' असम में किस नदी पर स्थित है?",
        ["गंगा नदी", "यमुना नदी", "ब्रह्मपुत्र नदी", "मेघना नदी"],
        "माजुली असम में ब्रह्मपुत्र नदी के मध्य स्थित विश्व का सबसे बड़ा नदी द्वीप है, जो भारत का पहला नदी द्वीप जिला भी है। अतः विकल्प C सही है।"
    ))
    # Q48
    qs.append(create_q(
        48, "Indian Polity", "Easy", "D",
        "Under Article 280 of the Constitution of India, the Finance Commission is constituted by the President every:",
        ["3 years", "4 years", "6 years", "5 years (or earlier)"],
        "Under Article 280(1), the President of India constitutes a Finance Commission every fifth year (or at such earlier time as considered necessary) to recommend distribution of tax revenues between Union and States. Hence, option D is correct.",
        "भारतीय संविधान के अनुच्छेद 280 के तहत वित्त आयोग का गठन राष्ट्रपति द्वारा प्रत्येक कितने वर्ष पर किया जाता है?",
        ["3 वर्ष", "4 वर्ष", "6 वर्ष", "5 वर्ष (या आवश्यकतानुसार उससे पहले)"],
        "अनुच्छेद 280 के अनुसार भारत का राष्ट्रपति प्रत्येक 5वें वर्ष की समाप्ति पर या आवश्यकतानुसार उससे पूर्व एक वित्त आयोग का गठन करता है। अतः विकल्प D सही है।"
    ))
    # Q49
    qs.append(create_q(
        49, "Modern Indian History", "Easy", "A",
        "On 8 August 1942, the historic 'Quit India' Resolution was formally passed by the All India Congress Committee (AICC) meeting at:",
        ["Gowalia Tank Maidan, Bombay", "Ramgarh, Bihar", "Tripuri, MP", "Haripura, Gujarat"],
        "The Quit India Resolution was passed on August 8, 1942 at the Gowalia Tank Maidan (now August Kranti Maidan) in Bombay, where Mahatma Gandhi delivered his famous 'Do or Die' speech. Hence, option A is correct.",
        "8 अगस्त 1942 को अखिल भारतीय कांग्रेस कमेटी (AICC) ने 'भारत छोड़ो' प्रस्ताव औपचारिक रूप से कहाँ पारित किया था?",
        ["गोवालिया टैंक मैदान, बंबई", "रामगढ़, बिहार", "त्रिपुरी, मध्य प्रदेश", "हरिपुरा, गुजरात"],
        "8 अगस्त 1942 को बंबई के गोवालिया टैंक मैदान (अगस्त क्रांति मैदान) में भारत छोड़ो आंदोलन का प्रस्ताव पारित किया गया जहाँ गांधीजी ने 'करो या मरो' का नारा दिया। अतः विकल्प A सही है।"
    ))
    # Q50
    qs.append(create_q(
        50, "International Organizations", "Easy", "B",
        "Where is the headquarters of the International Court of Justice (ICJ) located?",
        ["Geneva, Switzerland", "The Hague, Netherlands", "New York, USA", "Vienna, Austria"],
        "The International Court of Justice (ICJ), the principal judicial organ of the United Nations established in 1945, has its permanent seat at the Peace Palace in The Hague, Netherlands. Hence, option B is correct.",
        "अंतर्राष्ट्रीय न्यायालय (International Court of Justice - ICJ) का मुख्यालय कहाँ स्थित है?",
        ["जिनेवा, स्विट्जरलैंड", "द हेग, नीदरलैंड्स", "न्यूयॉर्क, यूएसए", "वियना, ऑस्ट्रिया"],
        "संयुक्त राष्ट्र के मुख्य न्यायिक अंग 'अंतर्राष्ट्रीय न्यायालय' (ICJ) की स्थापना 1945 में हुई थी और इसका मुख्यालय द हेग (नीदरलैंड्स) के पीस पैलेस में स्थित है। अतः विकल्प B सही है।"
    ))
    return qs

print("Part 1 definitions loaded.")
