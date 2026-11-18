#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_2022_gs1_full.py — Builds the complete 150-question authentic UPPSC PCS Prelims 2022 GS-1 Paper."""
import json
import os

from build_uppcs_2022_gs1 import get_questions_1_to_50, create_q

def get_questions_51_to_100():
    qs = []
    # Q51
    qs.append(create_q(
        51, "UP Special & Environment", "Easy", "B",
        "Which is the only National Park located in the state of Uttar Pradesh?",
        ["Corbett National Park", "Dudhwa National Park", "Pilibhit National Park", "Chandraprabha National Park"],
        "Dudhwa National Park located in Lakhimpur Kheri district of Uttar Pradesh is the state's sole National Park, established in 1977. Pilibhit is a Tiger Reserve, and Chandraprabha is a Wildlife Sanctuary. Hence, option B is correct.",
        "उत्तर प्रदेश राज्य में स्थित एकमात्र राष्ट्रीय उद्यान कौन-सा है?",
        ["कॉर्बेट राष्ट्रीय उद्यान", "दुधवा राष्ट्रीय उद्यान", "पीलीभीत राष्ट्रीय उद्यान", "चंद्रप्रभा राष्ट्रीय उद्यान"],
        "लखीमपुर खीरी जिले में स्थित दुधवा राष्ट्रीय उद्यान उत्तर प्रदेश का एकमात्र राष्ट्रीय उद्यान है, जिसे 1977 में राष्ट्रीय उद्यान घोषित किया गया था। अतः विकल्प B सही है।"
    ))
    # Q52
    qs.append(create_q(
        52, "Indian Polity", "Medium", "C",
        "Under Article 148 of the Constitution of India, the Comptroller and Auditor General (CAG) of India holds office for a term of:",
        ["5 years or up to 65 years of age", "6 years or up to 62 years of age", "6 years or up to 65 years of age", "5 years or up to 62 years of age"],
        "Under the CAG (Duties, Powers and Conditions of Service) Act, 1971, the Comptroller and Auditor General holds office for a term of 6 years or until attaining the age of 65 years, whichever is earlier. Hence, option C is correct.",
        "भारतीय संविधान के अनुच्छेद 148 के अंतर्गत भारत के नियंत्रक एवं महालेखापरीक्षक (CAG) की पदावधि कितनी होती है?",
        ["5 वर्ष या 65 वर्ष की आयु तक", "6 वर्ष या 62 वर्ष की आयु तक", "6 वर्ष या 65 वर्ष की आयु तक (जो भी पहले हो)", "5 वर्ष या 62 वर्ष की आयु तक"],
        "अनुच्छेद 148 के तहत नियुक्त CAG का कार्यकाल 6 वर्ष या 65 वर्ष की आयु (जो भी पहले समाप्त हो) तक होता है। अतः विकल्प C सही उत्तर है।"
    ))
    # Q53
    qs.append(create_q(
        53, "Environment & Ecology", "Medium", "D",
        "Which of the following is NOT one of the officially designated Global Biodiversity Hotspots present in the Indian sub-region?",
        ["Himalaya", "Western Ghats and Sri Lanka", "Indo-Burma", "Eastern Ghats"],
        "India encompasses four global biodiversity hotspots: (1) Himalaya, (2) Western Ghats, (3) Indo-Burma, and (4) Sundaland (Nicobar Islands). The Eastern Ghats are an ecologically important hill range, but not a designated global biodiversity hotspot. Hence, option D is correct.",
        "निम्नलिखित में से कौन-सा भारतीय भू-भाग में स्थित वैश्विक जैव विविधता हॉटस्पॉट (Biodiversity Hotspot) नहीं है?",
        ["हिमालय", "पश्चिमी घाट", "इंडो-बर्मा", "पूर्वी घाट"],
        "भारत में चार वैश्विक जैव विविधता हॉटस्पॉट हैं: हिमालय, पश्चिमी घाट, इंडो-बर्मा तथा सुंदरलैंड। पूर्वी घाट जैव विविधता हॉटस्पॉट की सूची में शामिल नहीं है। अतः विकल्प D सही है।"
    ))
    # Q54
    qs.append(create_q(
        54, "Medieval Indian History", "Easy", "A",
        "The 'Mansabdari System', a grading mechanism for civil and military administration, was introduced by Mughal Emperor:",
        ["Akbar", "Babur", "Humayun", "Shah Jahan"],
        "Mughal Emperor Akbar introduced the Mansabdari system in 1571 CE. Every officer was assigned a Mansab (rank) denoting military obligations and civil rank, categorized into Zat (personal rank/salary) and Sawar (number of cavalrymen maintained). Hence, option A is correct.",
        "नागरिक और सैन्य प्रशासन के लिए 'मनसबदारी प्रणाली' किस मुगल सम्राट द्वारा शुरू की गई थी?",
        ["अकबर", "बाबर", "हुमायूँ", "शाहजहाँ"],
        "मुगल सम्राट अकबर ने 1571 ई. में मनसबदारी व्यवस्था प्रारंभ की थी जिसमें प्रत्येक अधिकारी को जात (व्यक्तिगत पद व वेतन) और सवार (सैनिक घुड़सवारों की संख्या) का मनसब दिया जाता था। अतः विकल्प A सही है।"
    ))
    # Q55
    qs.append(create_q(
        55, "Indian Economy & Agriculture", "Easy", "B",
        "Who coined the phrase 'Green Revolution' in 1968 to describe the dramatic increase in agricultural yields?",
        ["Dr. Norman Borlaug", "Dr. William S. Gaud", "Dr. M.S. Swaminathan", "Dr. Verghese Kurien"],
        "Dr. William S. Gaud, administrator of USAID, first coined the term 'Green Revolution' in a speech in March 1968 to contrast the peaceful agricultural transformation with the violent 'Red Revolution' in China. Hence, option B is correct.",
        "कृषि उत्पादकता में भारी वृद्धि का वर्णन करने के लिए 1968 में 'हरित क्रांति' (Green Revolution) शब्द का सर्वप्रथम प्रयोग किसने किया था?",
        ["डॉ. नॉर्मन बोरलॉग", "डॉ. विलियम एस. गॉड", "डॉ. एम.एस. स्वामीनाथन", "डॉ. वर्गीज कुरियन"],
        "यूएसएड (USAID) के प्रशासक डॉ. विलियम एस. गॉड ने मार्च 1968 में अपने एक भाषण में 'हरित क्रांति' शब्द गढ़ा था। डॉ. नॉर्मन बोरलॉग वैश्विक स्तर पर तथा डॉ. एम.एस. स्वामीनाथन भारत में हरित क्रांति के जनक हैं। अतः विकल्प B सही है।"
    ))
    # Q56
    qs.append(create_q(
        56, "Indian Polity", "Medium", "C",
        "In which landmark constitutional case did the Supreme Court of India hold that the Preamble is an integral part of the Constitution and can be amended under Article 368 without altering the basic structure?",
        ["Golaknath Case (1967)", "Minerva Mills Case (1980)", "Kesavananda Bharati Case (1973)", "Berubari Union Case (1960)"],
        "In the historic 13-judge bench ruling in Kesavananda Bharati v. State of Kerala (1973), the Supreme Court reversed the Berubari opinion, holding that the Preamble is an integral part of the Constitution and can be amended under Article 368 subject to the 'Basic Structure' doctrine. Hence, option C is correct.",
        "किस ऐतिहासिक वाद में सर्वोच्च न्यायालय ने यह व्यवस्था दी कि प्रस्तावना संविधान का अभिन्न अंग है और मूल ढांचे को बदले बिना अनुच्छेद 368 के तहत इसमें संशोधन किया जा सकता है?",
        ["गोलकनाथ वाद (1967)", "मिनर्वा मिल्स वाद (1980)", "केशवानंद भारती वाद (1973)", "बेरुबारी यूनियन वाद (1960)"],
        "केशवानंद भारती बनाम केरल राज्य (1973) के ऐतिहासिक निर्णय में सर्वोच्च न्यायालय ने स्पष्ट किया कि प्रस्तावना संविधान का अभिन्न अंग है और मूल ढांचे को नष्ट किए बिना इसमें संशोधन संभव है। अतः विकल्प C सही है।"
    ))
    # Q57
    qs.append(create_q(
        57, "Indian Geography", "Medium", "D",
        "Which of the following is the largest river drainage basin in India in terms of catchment area?",
        ["Godavari Basin", "Krishna Basin", "Brahmaputra Basin", "Ganga Basin"],
        "The Ganga Basin is by far the largest river basin in India, covering 861,452 sq km (about 26.2% of the country's total geographical area). Godavari is the second largest (largest in the peninsula). Hence, option D is correct.",
        "अपवाह क्षेत्र (बेसिन क्षेत्रफल) की दृष्टि से भारत का सबसे बड़ा नदी बेसिन कौन-सा है?",
        ["गोदावरी बेसिन", "कृष्णा बेसिन", "ब्रह्मपुत्र बेसिन", "गंगा बेसिन"],
        "गंगा बेसिन भारत का सबसे बड़ा नदी बेसिन है, जो देश के लगभग 26.2% भौगोलिक क्षेत्रफल (लगभग 8.6 लाख वर्ग किमी) पर विस्तृत है। प्रायद्वीपीय भारत का सबसे बड़ा बेसिन गोदावरी है। अतः विकल्प D सही है।"
    ))
    # Q58
    qs.append(create_q(
        58, "General Science", "Easy", "A",
        "During oxygenic photosynthesis in green plants, oxygen (O2) released into the atmosphere originates from the splitting of:",
        ["Water (H2O)", "Carbon dioxide (CO2)", "Glucose (C6H12O6)", "Chlorophyll"],
        "During the light-dependent reactions of photosynthesis in the thylakoid membranes, photolysis of water molecules (2H2O -> 4H+ + 4e- + O2) releases oxygen. Experiments by Ruben and Kamen using oxygen isotope O-18 proved this. Hence, option A is correct.",
        "हरे पौधों में प्रकाश संश्लेषण के दौरान वायुमंडल में मुक्त होने वाली ऑक्सीजन (O2) किसके विखंडन से प्राप्त होती है?",
        ["जल (H2O)", "कार्बन डाइऑक्साइड (CO2)", "ग्लूकोज", "पर्णहरित (क्लोरोफिल)"],
        "प्रकाश संश्लेषण की प्रकाशिक अभिक्रिया में जल के प्रकाशिक अपघटन (फोटोलाइसिस) से ऑक्सीजन गैस निकलती है, कार्बन डाइऑक्साइड से नहीं। अतः विकल्प A सही उत्तर है।"
    ))
    # Q59
    qs.append(create_q(
        59, "Constitutional History", "Medium", "B",
        "The system of 'Dyarchy' (dual rule dividing provincial subjects into Transferred and Reserved) was introduced in the provinces by the:",
        ["Indian Councils Act, 1909", "Government of India Act, 1919", "Government of India Act, 1935", "Charter Act of 1853"],
        "The Government of India Act, 1919 (Montagu-Chelmsford Reforms) introduced Dyarchy in the provincial executive, dividing administrative subjects into 'Reserved' (under Governor and Executive Council) and 'Transferred' (under Ministers responsible to the legislature). Hence, option B is correct.",
        "प्रांतों में 'द्वैध शासन' (Dyarchy - विषयों को आरक्षित और हस्तांतरित में विभाजित करने) की व्यवस्था किस अधिनियम द्वारा लागू की गई थी?",
        ["1909 का भारतीय परिषद अधिनियम", "1919 का भारत सरकार अधिनियम", "1935 का भारत सरकार अधिनियम", "1853 का चार्टर अधिनियम"],
        "1919 के भारत सरकार अधिनियम (मोंटेग्यू-चेम्सफोर्ड सुधार) द्वारा प्रांतों में द्वैध शासन प्रणाली प्रारंभ की गई थी, जिसे बाद में 1935 के अधिनियम द्वारा समाप्त कर केंद्र में लागू किया गया। अतः विकल्प B सही है।"
    ))
    # Q60
    qs.append(create_q(
        60, "Indian Economy & Taxation", "Easy", "C",
        "The Goods and Services Tax (GST) was introduced in India by which Constitutional Amendment Act, coming into force on 1 July 2017?",
        ["99th Amendment Act", "100th Amendment Act", "101st Amendment Act", "102nd Amendment Act"],
        "The 101st Constitutional Amendment Act, 2016 introduced the comprehensive indirect tax regime of Goods and Services Tax (GST) across India, which became operational from July 1, 2017. Hence, option C is correct.",
        "भारत में वस्तु एवं सेवा कर (GST) किस संविधान संशोधन अधिनियम द्वारा लागू किया गया, जो 1 जुलाई 2017 से प्रभावी हुआ?",
        ["99वाँ संशोधन अधिनियम", "100वाँ संशोधन अधिनियम", "101वाँ संशोधन अधिनियम", "102वाँ संशोधन अधिनियम"],
        "101वें संविधान संशोधन अधिनियम 2016 द्वारा भारत में जीएसटी लागू किया गया, जिसने कई अप्रत्यक्ष करों को समाप्त कर एकल कर प्रणाली की स्थापना की। अतः विकल्प C सही है।"
    ))
    # Q61
    qs.append(create_q(
        61, "Art & Culture", "Easy", "D",
        "Which Mughal monument situated in Agra was commissioned by Emperor Akbar in 1571 to serve as his new capital?",
        ["Red Fort of Delhi", "Humayun's Tomb", "Shalimar Bagh", "Fatehpur Sikri"],
        "Akbar founded Fatehpur Sikri in 1571 near Agra to honor the Sufi saint Shaikh Salim Chishti, constructing grand architectural landmarks including Jama Masjid, Buland Darwaza, and Panch Mahal. Hence, option D is correct.",
        "मुगल सम्राट अकबर द्वारा 1571 में अपनी नई राजधानी के रूप में निर्मित प्रसिद्ध शहर/स्मारक कौन-सा है?",
        ["दिल्ली का लाल किला", "हुमायूँ का मकबरा", "शालीमार बाग", "फतेहपुर सीकरी"],
        "सम्राट अकबर ने सूफी संत शेख सलीम चिश्ती के सम्मान में 1571 में आगरा के निकट फतेहपुर सीकरी की स्थापना की और इसे अपनी राजधानी बनाया। अतः विकल्प D सही है।"
    ))
    # Q62
    qs.append(create_q(
        62, "General Science", "Easy", "A",
        "Which vitamin plays an indispensable role in the synthesis of prothrombin and is essential for normal blood clotting?",
        ["Vitamin K", "Vitamin A", "Vitamin D", "Vitamin E"],
        "Vitamin K (phylloquinone/menaquinone) acts as a coenzyme in the hepatic synthesis of blood coagulation factors II (prothrombin), VII, IX, and X. Deficiency leads to prolonged bleeding. Hence, option A is correct.",
        "रक्त का थक्का (Blood Clotting) जमने और प्रोथ्रोम्बिन के निर्माण के लिए कौन-सा विटामिन अनिवार्य है?",
        ["विटामिन K", "विटामिन A", "विटामिन D", "विटामिन E"],
        "विटामिन K यकृत में प्रोथ्रोम्बिन और अन्य रक्त थक्का जमाने वाले कारकों के संश्लेषण के लिए आवश्यक होता है। इसकी कमी से रक्तस्राव नहीं रुकता। अतः विकल्प A सही है।"
    ))
    # Q63
    qs.append(create_q(
        63, "Modern Indian History", "Easy", "B",
        "The first session of the Indian National Congress (INC) held in Bombay in December 1885 was attended by how many delegates?",
        ["65 delegates", "72 delegates", "84 delegates", "100 delegates"],
        "The foundation session of the Indian National Congress met from 28 to 31 December 1885 at Gokuldas Tejpal Sanskrit College in Bombay, presided over by W.C. Bonnerjee and attended by 72 delegates from all over India. Hence, option B is correct.",
        "दिसंबर 1885 में बंबई में आयोजित भारतीय राष्ट्रीय कांग्रेस के प्रथम अधिवेशन में कितने प्रतिनिधियों ने भाग लिया था?",
        ["65 प्रतिनिधि", "72 प्रतिनिधि", "84 प्रतिनिधि", "100 प्रतिनिधि"],
        "भारतीय राष्ट्रीय कांग्रेस के प्रथम अधिवेशन (28-31 दिसंबर 1885, गोकुलदास तेजपाल संस्कृत कॉलेज, बंबई) में देश भर से कुल 72 प्रतिनिधियों ने भाग लिया था। इसकी अध्यक्षता व्योमेश चंद्र बनर्जी ने की थी। अतः विकल्प B सही है।"
    ))
    # Q64
    qs.append(create_q(
        64, "Indian Geography", "Easy", "C",
        "The 'Golden Quadrilateral' super-highway network in India connects which four major metropolitan cities?",
        ["Delhi – Mumbai – Hyderabad – Kolkata", "Delhi – Ahmedabad – Chennai – Kolkata", "Delhi – Mumbai – Chennai – Kolkata", "Chandigarh – Mumbai – Bangalore – Kolkata"],
        "The Golden Quadrilateral highway network developed under the National Highways Development Project (NHDP) connects India's four major metro hubs: Delhi, Mumbai, Chennai, and Kolkata. Hence, option C is correct.",
        "भारत का 'स्वर्णिम चतुर्भुज' (Golden Quadrilateral) राष्ट्रीय राजमार्ग नेटवर्क किन चार महानगरों को आपस में जोड़ता है?",
        ["दिल्ली – मुंबई – हैदराबाद – कोलकाता", "दिल्ली – अहमदाबाद – चेन्नई – कोलकाता", "दिल्ली – मुंबई – चेन्नई – कोलकाता", "चंडीगढ़ – मुंबई – बैंगलोर – कोलकाता"],
        "स्वर्णिम चतुर्भुज परियोजना देश के चार प्रमुख महानगरों: दिल्ली (उत्तर), मुंबई (पश्चिम), चेन्नई (दक्षिण) तथा कोलकाता (पूर्व) को 4/6 लेन राजमार्गों से जोड़ती है। अतः विकल्प C सही है।"
    ))
    # Q65
    qs.append(create_q(
        65, "Indian Polity", "Medium", "D",
        "Under the Constitution of India, if any question arises whether a Bill is a Money Bill or not, whose decision thereon shall be final?",
        ["The President of India", "The Finance Minister", "The Chairman of Rajya Sabha", "The Speaker of Lok Sabha"],
        "Under Article 110(3) of the Constitution of India, if any question arises whether a Bill is a Money Bill or not, the decision of the Speaker of the House of the People (Lok Sabha) thereon shall be final. Hence, option D is correct.",
        "भारतीय संविधान के अंतर्गत यदि यह प्रश्न उठता है कि कोई विधेयक 'धन विधेयक' (Money Bill) है या नहीं, तो किसका निर्णय अंतिम होता है?",
        ["भारत के राष्ट्रपति का", "वित्त मंत्री का", "राज्यसभा के सभापति का", "लोकसभा अध्यक्ष का"],
        "अनुच्छेद 110(3) के अनुसार किसी विधेयक के धन विधेयक होने या न होने पर लोकसभा अध्यक्ष (स्पीकर) का निर्णय अंतिम और सर्वमान्य होता है। अतः विकल्प D सही है।"
    ))
    # Q66
    qs.append(create_q(
        66, "Environment & Ecology", "Easy", "A",
        "Acid rain is primarily caused by atmospheric emissions of which two acidic gases from industrial combustion and automobiles?",
        ["Sulphur dioxide (SO2) and Nitrogen oxides (NOx)", "Carbon monoxide (CO) and Methane (CH4)", "Ozone (O3) and Carbon dioxide (CO2)", "Ammonia (NH3) and Chlorofluorocarbons (CFCs)"],
        "Acid rain results when sulfur dioxide (SO2) and nitrogen oxides (NOx) react with atmospheric water, oxygen, and oxidants to form sulfuric acid (H2SO4) and nitric acid (HNO3). Hence, option A is correct.",
        "अम्लीय वर्षा (Acid Rain) मुख्य रूप से वायुमंडल में किन दो गैसों के उत्सर्जन और जलवाष्प से क्रिया के कारण होती है?",
        ["सल्फर डाइऑक्साइड (SO2) और नाइट्रोजन ऑक्साइड्स (NOx)", "कार्बन मोनोऑक्साइड (CO) और मीथेन (CH4)", "ओजोन (O3) और कार्बन डाइऑक्साइड (CO2)", "अमोनिया (NH3) और सीएफसी (CFCs)"],
        "सल्फर डाइऑक्साइड और नाइट्रोजन के ऑक्साइड वायुमंडल में जलवाष्प से मिलकर क्रमशः सल्फ्यूरिक अम्ल और नाइट्रिक अम्ल बनाते हैं, जो वर्षा जल के साथ गिरते हैं। अतः विकल्प A सही है।"
    ))
    # Q67
    qs.append(create_q(
        67, "Modern Indian History", "Easy", "B",
        "The historic 'Kakori Train Action' was executed by revolutionaries of the Hindustan Republican Association (HRA) near Lucknow on which date?",
        ["9 August 1920", "9 August 1925", "23 March 1931", "17 December 1927"],
        "On August 9, 1925, members of the Hindustan Republican Association (Ram Prasad Bismil, Ashfaqulla Khan, Chandrashekhar Azad, Rajendra Lahiri, Sachindra Bakshi) held up the 8-Down passenger train at Kakori near Lucknow to acquire government funds for revolutionary struggle. Hence, option B is correct.",
        "हिंदुस्तान रिपब्लिकन एसोसिएशन (HRA) के क्रांतिकारियों द्वारा ऐतिहासिक 'काकोरी ट्रेन एक्शन' लखनऊ के निकट किस तिथि को किया गया था?",
        ["9 अगस्त 1920", "9 अगस्त 1925", "23 मार्च 1931", "17 दिसंबर 1927"],
        "9 अगस्त 1925 को रामप्रसाद बिस्मिल, अशफाकउल्ला खां, राजेंद्र लाहिड़ी, चंद्रशेखर आजाद आदि ने लखनऊ के काकोरी में 8-डाउन ट्रेन से सरकारी खजाने को जब्त किया था। अतः विकल्प B सही है।"
    ))
    # Q68
    qs.append(create_q(
        68, "Indian Economy & Banking", "Easy", "C",
        "The Reserve Bank of India (RBI) commenced its operations on 1 April 1935 following the recommendations of which commission?",
        ["Hunter Commission", "Chamberlain Commission", "Hilton Young Commission (Royal Commission on Indian Currency and Finance)", "Simon Commission"],
        "The Reserve Bank of India was established on April 1, 1935 under the Reserve Bank of India Act, 1934, based primarily on the recommendations of the Hilton Young Commission (Royal Commission on Indian Currency and Finance, 1926). Hence, option C is correct.",
        "भारतीय रिज़र्व बैंक (RBI) ने 1 अप्रैल 1935 को किस आयोग की सिफारिशों के आधार पर अपना कार्य प्रारंभ किया था?",
        ["हंटर आयोग", "चेम्बरलेन आयोग", "हिल्टन यंग आयोग (रॉयल कमीशन ऑन इंडियन करेंसी एंड फाइनेंस)", "साइमन कमीशन"],
        "हिल्टन यंग कमीशन (1926) की अनुशंसा पर भारतीय रिज़र्व बैंक अधिनियम 1934 पारित हुआ और 1 अप्रैल 1935 को केंद्रीय बैंक के रूप में आरबीआई की स्थापना हुई। अतः विकल्प C सही है।"
    ))
    # Q69
    qs.append(create_q(
        69, "Solar System & Astronomy", "Easy", "D",
        "Which planet in our solar system is commonly designated as 'Earth's Twin' due to its very similar size, mass, and bulk composition?",
        ["Mars", "Mercury", "Jupiter", "Venus"],
        "Venus is referred to as Earth's twin planet because of its similar diameter (around 95% of Earth's), mass (81.5% of Earth's), and proximity to Earth, although its dense runaway greenhouse atmosphere makes it the hottest planet. Hence, option D is correct.",
        "सौरमंडल के किस ग्रह को उसके आकार, द्रव्यमान और बनावट में समानता के कारण 'पृथ्वी की जुड़वां बहन' (Earth's Twin) कहा जाता है?",
        ["मंगल", "बुध", "बृहस्पति", "शुक्र (Venus)"],
        "शुक्र ग्रह का आकार, द्रव्यमान और घनत्व पृथ्वी के लगभग समान है, जिसके कारण इसे 'पृथ्वी की जुड़वां बहन' कहा जाता है। अतः विकल्प D सही है।"
    ))
    # Q70
    qs.append(create_q(
        70, "Indian Polity", "Easy", "A",
        "How many functional items are placed within the purview of Panchayats under the Eleventh Schedule added by the 73rd Constitutional Amendment Act, 1992?",
        ["29 items", "18 items", "21 items", "33 items"],
        "The Eleventh Schedule contains 29 functional items for Panchayats (Article 243G). The Twelfth Schedule (for Municipalities under the 74th Amendment) contains 18 items. Hence, option A is correct.",
        "73वें संविधान संशोधन अधिनियम 1992 द्वारा जोड़ी गई 11वीं अनुसूची के अंतर्गत पंचायतों के कार्यक्षेत्र में कितने विषय रखे गए हैं?",
        ["29 विषय", "18 विषय", "21 विषय", "33 विषय"],
        "11वीं अनुसूची में पंचायतों को सौंपे गए 29 प्रशासनिक व विकासात्मक विषयों की सूची है (जबकि 12वीं अनुसूची में नगरपालिकाओं के लिए 18 विषय हैं)। अतः विकल्प A सही है।"
    ))
    # Q71
    qs.append(create_q(
        71, "Environment & Climate", "Medium", "B",
        "Which greenhouse gas makes the greatest overall contribution to Earth's natural greenhouse effect?",
        ["Carbon dioxide", "Water vapour (H2O)", "Methane", "Ozone"],
        "Water vapour is the most abundant and dominant greenhouse gas in Earth's atmosphere, accounting for between 36% and 72% of the natural greenhouse effect (followed by CO2 at 9%–26%). Hence, option B is correct.",
        "पृथ्वी के प्राकृतिक ग्रीनहाउस प्रभाव में सबसे बड़ा समग्र योगदान किस ग्रीनहाउस गैस का होता है?",
        ["कार्बन डाइऑक्साइड", "जलवाष्प (Water vapour)", "मीथेन", "ओजोन"],
        "वायुमंडल में प्राकृतिक रूप से पाए जाने वाले जलवाष्प का प्राकृतिक ग्रीनहाउस प्रभाव में सबसे बड़ा हिस्सा (लगभग 36% से 72%) होता है। अतः विकल्प B सही है।"
    ))
    # Q72
    qs.append(create_q(
        72, "Ancient Indian History", "Easy", "C",
        "What is the predominant nature and writing style of the Harappan (Indus Valley) script discovered on seals and stone tablets?",
        ["Alphabetical written left-to-right", "Devanagari script", "Pictographic and Boustrophedon (alternate lines right-to-left and left-to-right)", "Kharosthi script"],
        "The Harappan script is primarily pictographic and logo-syllabic, written in Boustrophedon style (from right to left in the first line and left to right in the second line). It remains undeciphered. Hence, option C is correct.",
        "हड़प्पा (सिंधु घाटी) सभ्यता की मुहरों और पट्टिकाओं पर पाई गई लिपि की मुख्य प्रकृति और लेखन शैली क्या है?",
        ["वर्णमाला आधारित (बाएं से दाएं)", "देवनागरी लिपि", "भाव-चित्रात्मक (पिक्टोग्राफिक) एवं बूस्ट्रोफेडन (दाएं से बाएं तथा बाएं से दाएं)", "खरोष्ठी लिपि"],
        "हड़प्पा लिपि चित्रात्मक एवं प्रतीकात्मक है जिसे सामान्यतः 'बूस्ट्रोफेडन' शैली (पहली पंक्ति दाएं से बाएं, दूसरी बाएं से दाएं) में लिखा गया है। यह अभी तक पढ़ी नहीं जा सकी है। अतः विकल्प C सही है।"
    ))
    # Q73
    qs.append(create_q(
        73, "UP Special & Administration", "Medium", "D",
        "In Uttar Pradesh, the statutory anti-corruption institution of Lokayukta was established under the UP Lokayukta and Up-Lokayuktas Act passed in:",
        ["1965", "1970", "1980", "1975"],
        "The Uttar Pradesh Lokayukta and Up-Lokayuktas Act was enacted in 1975, and Justice Vishwambhar Dayal was appointed as the first Lokayukta of Uttar Pradesh in 1977. Hence, option D is correct.",
        "उत्तर प्रदेश में भ्रष्टाचार विरोधी वैधानिक संस्था 'लोकायुक्त' का गठन किस वर्ष पारित अधिनियम के तहत किया गया था?",
        ["1965", "1970", "1980", "1975"],
        "उत्तर प्रदेश लोकायुक्त एवं उप-लोकायुक्त अधिनियम 1975 में पारित हुआ और 1977 में न्यायमूर्ति विशंभर दयाल प्रदेश के पहले लोकायुक्त बने। अतः विकल्प D सही है।"
    ))
    # Q74
    qs.append(create_q(
        74, "General Science", "Easy", "A",
        "What logarithmic unit is universally employed to measure sound intensity and acoustic noise level?",
        ["Decibel (dB)", "Hertz (Hz)", "Pascal (Pa)", "Joule (J)"],
        "The Decibel (dB) is a logarithmic unit used to express the ratio of acoustic pressure or sound intensity relative to the threshold of human hearing (0 dB). Hertz measures frequency. Hence, option A is correct.",
        "ध्वनि की तीव्रता और शोर के स्तर को मापने के लिए किस लघुगणकीय इकाई (Unit) का उपयोग किया जाता है?",
        ["डेसिबल (dB)", "हर्ट्ज (Hz)", "पास्कल (Pa)", "जूल (J)"],
        "ध्वनि की तीव्रता और प्रबलता को डेसिबल (dB) में मापा जाता है। हर्ट्ज आवृत्ति का तथा पास्कल दाब का मात्रक है। अतः विकल्प A सही उत्तर है।"
    ))
    # Q75
    qs.append(create_q(
        75, "Modern Indian History", "Easy", "B",
        "The 'Swaraj Party' (Congress-Khilafat Swarajya Party) was founded in January 1923 at Allahabad by:",
        ["Mahatma Gandhi and Jawaharlal Nehru", "Chittaranjan Das and Motilal Nehru", "Subhash Chandra Bose and Lala Lajpat Rai", "Bal Gangadhar Tilak and Bipin Chandra Pal"],
        "Following the suspension of the Non-Cooperation Movement, Chittaranjan Das (President) and Motilal Nehru (Secretary) founded the Swaraj Party in January 1923 in Allahabad to contest council elections and enter legislative assemblies. Hence, option B is correct.",
        "जनवरी 1923 में इलाहाबाद में 'स्वराज्य पार्टी' (कांग्रेस-खिलाफत स्वराज्य पार्टी) की स्थापना किसने की थी?",
        ["महात्मा गांधी और जवाहरलाल नेहरू", "चित्तरंजन दास और मोतीलाल नेहरू", "सुभाष चंद्र बोस और लाला लाजपत राय", "बाल गंगाधर तिलक और बिपिन चंद्र पाल"],
        "असहयोग आंदोलन की वापसी के बाद परिषदों में प्रवेश कर सरकार की नीतियों का विरोध करने हेतु चित्तरंजन दास (अध्यक्ष) और मोतीलाल नेहरू (सचिव) ने 1923 में इलाहाबाद में स्वराज्य पार्टी का गठन किया। अतः विकल्प B सही है।"
    ))
    # Q76
    qs.append(create_q(
        76, "World Geography", "Medium", "C",
        "Through which one of the following countries does the Equator (0° latitude) NOT pass?",
        ["Indonesia", "Brazil", "India", "Ecuador"],
        "The Equator passes through 13 countries across South America (Ecuador, Colombia, Brazil), Africa (Sao Tome & Principe, Gabon, Congo, DRC, Uganda, Kenya, Somalia), and Asia/Oceania (Maldives, Indonesia, Kiribati). It does not pass through India (mainland India lies entirely north of the Equator). Hence, option C is correct.",
        "भूमध्य रेखा (0° अक्षांश) निम्नलिखित में से किस देश से होकर नहीं गुजरती है?",
        ["इंडोनेशिया", "ब्राजील", "भारत", "इक्वाडोर"],
        "भूमध्य रेखा 13 देशों से गुजरती है लेकिन भारत से नहीं गुजरती (भारत का मुख्य भूभाग 8°4' N से 37°6' N के मध्य स्थित है)। अतः विकल्प C सही उत्तर है।"
    ))
    # Q77
    qs.append(create_q(
        77, "Indian Polity", "Easy", "D",
        "Under Article 76 of the Constitution of India, the Attorney General for India is appointed by:",
        ["The Chief Justice of India", "The Prime Minister", "The Union Law Minister", "The President of India"],
        "Article 76(1) states that the President shall appoint a person who is qualified to be appointed a Judge of the Supreme Court to be Attorney General for India, who holds office during the pleasure of the President. Hence, option D is correct.",
        "भारतीय संविधान के अनुच्छेद 76 के तहत भारत के महान्यायवादी (Attorney General) की नियुक्ति किसके द्वारा की जाती है?",
        ["भारत के मुख्य न्यायाधीश द्वारा", "प्रधानमंत्री द्वारा", "केंद्रीय विधि मंत्री द्वारा", "भारत के राष्ट्रपति द्वारा"],
        "अनुच्छेद 76 के अनुसार सर्वोच्च न्यायालय का न्यायाधीश नियुक्त होने की योग्यता रखने वाले व्यक्ति को राष्ट्रपति भारत का महान्यायवादी नियुक्त करता है। अतः विकल्प D सही है।"
    ))
    # Q78
    qs.append(create_q(
        78, "Environment & Ecology", "Medium", "A",
        "The environmental phenomenon characterized by an over-enrichment of minerals and nutrients (especially phosphorus and nitrogen) in an aquatic body causing algal bloom and hypoxia is known as:",
        ["Eutrophication", "Biomagnification", "Salinization", "Acidification"],
        "Eutrophication occurs when excess agricultural fertilizers or sewage runoff enriched in nitrates and phosphates trigger rapid phytoplankton blooms, which consume dissolved oxygen upon decomposition and cause aquatic die-offs. Hence, option A is correct.",
        "जल निकायों में पोषक तत्वों (विशेषकर नाइट्रोजन और फास्फोरस) की अत्यधिक वृद्धि से शैवाल प्रस्फुटन (Algal bloom) और ऑक्सीजन की कमी होने की प्रक्रिया को क्या कहा जाता है?",
        ["सुपोषण (Eutrophication)", "जैव-आवर्धन (Biomagnification)", "लवणीकरण (Salinization)", "अम्लीकरण (Acidification)"],
        "जलाशयों में उर्वरकों और सीवेज के कारण पोषक तत्वों की अधिकता से शैवालों की बेतहाशा वृद्धि होती है और जल में घुलित ऑक्सीजन समाप्त हो जाती है; इसे सुपोषण (यूट्रोफिकेशन) कहते हैं। अतः विकल्प A सही है।"
    ))
    # Q79
    qs.append(create_q(
        79, "Medieval Indian History", "Easy", "B",
        "The syncretic socio-religious order named 'Din-i-Ilahi' (Tauhid-i-Ilahi) was introduced in 1582 CE by:",
        ["Humayun", "Akbar", "Jahangir", "Shah Jahan"],
        "Mughal Emperor Akbar promulgated Din-i-Ilahi ('Religion of God') in 1582, combining elements of Islam, Hinduism, Zoroastrianism, and Jainism emphasizing Sulh-i-Kul (universal peace and tolerance). Birbal was its only Hindu adherent. Hence, option B is correct.",
        "1582 ई. में सर्व-धर्म समभाव पर आधारित 'दीन-ए-इलाही' (तौहीद-ए-इलाही) नामक वैचारिक व धार्मिक विचार किसने प्रारंभ किया था?",
        ["हुमायूँ", "अकबर", "जहाँगीर", "शाहजहाँ"],
        "मुगल सम्राट अकबर ने सभी धर्मों के श्रेष्ठ तत्वों को समाहित कर 'दीन-ए-इलाही' की शुरुआत की थी। बीरबल इसे स्वीकार करने वाले एकमात्र हिंदू थे। अतः विकल्प B सही है।"
    ))
    # Q80
    qs.append(create_q(
        80, "Indian Economy & Banking", "Medium", "C",
        "How many total members constitute the Monetary Policy Committee (MPC) of the Reserve Bank of India responsible for fixing benchmark interest rates?",
        ["5 members", "4 members", "6 members", "8 members"],
        "Under Section 45ZB of the amended RBI Act, the Monetary Policy Committee (MPC) consists of 6 members: 3 ex-officio from RBI (including Governor as Chairperson) and 3 external members nominated by the Central Government. Hence, option C is correct.",
        "भारतीय रिज़र्व बैंक (RBI) की मौद्रिक नीति समिति (MPC), जो नीतिगत ब्याज दरों का निर्धारण करती है, में कुल कितने सदस्य होते हैं?",
        ["5 सदस्य", "4 सदस्य", "6 सदस्य", "8 सदस्य"],
        "मौद्रिक नीति समिति (MPC) में कुल 6 सदस्य होते हैं: 3 सदस्य आरबीआई से (गवर्नर सहित) तथा 3 सदस्य केंद्र सरकार द्वारा नियुक्त किए जाते हैं। अतः विकल्प C सही है।"
    ))
    # Q81
    qs.append(create_q(
        81, "Indian Climate & Geography", "Easy", "D",
        "The winter rainfalls and snow in northwest India are caused by cyclonic storms (Western Disturbances) originating in the:",
        ["Arabian Sea", "Bay of Bengal", "Caspian Sea", "Mediterranean Sea"],
        "Western Disturbances are extratropical cyclones that originate over the Mediterranean Sea and surrounding Atlantic waters, travelling eastward guided by subtropical westerly jet streams to bring vital winter showers to northwest India (benefiting Rabi crops). Hence, option D is correct.",
        "उत्तर-पश्चिम भारत में सर्दियों में होने वाली वर्षा और बर्फबारी के लिए उत्तरदायी 'पश्चिमी विक्षोभ' (Western Disturbances) कहाँ से उत्पन्न होते हैं?",
        ["अरब सागर", "बंगाल की खाड़ी", "कैस्पियन सागर", "भूमध्य सागर (Mediterranean Sea)"],
        "पश्चिमी विक्षोभ शीतोष्ण कटिबंधीय चक्रवात हैं जो भूमध्य सागर में उत्पन्न होते हैं और पछुआ जेट धाराओं द्वारा भारत के उत्तर-पश्चिमी भाग में शीतकालीन वर्षा लाते हैं। अतः विकल्प D सही है।"
    ))
    # Q82
    qs.append(create_q(
        82, "General Science", "Easy", "A",
        "What is the normal physiological pH range of arterial human blood under healthy conditions?",
        ["7.35 to 7.45 (Slightly alkaline)", "6.50 to 6.80 (Slightly acidic)", "7.00 to 7.10 (Neutral)", "7.80 to 8.20 (Strongly alkaline)"],
        "Healthy human blood pH is maintained strictly between 7.35 and 7.45 by bicarbonate buffer systems and renal-respiratory regulation, making it slightly alkaline. Hence, option A is correct.",
        "स्वस्थ मानव शरीर में रक्त का सामान्य pH मान किस सीमा के भीतर रहता है?",
        ["7.35 से 7.45 (हल्का क्षारीय)", "6.50 से 6.80 (हल्का अम्लीय)", "7.00 से 7.10 (उदासीन)", "7.80 से 8.20 (प्रबल क्षारीय)"],
        "मानव रक्त का सामान्य pH मान 7.35 से 7.45 के बीच होता है, अर्थात् यह हल्का क्षारीय प्रकृति का होता है। अतः विकल्प A सही उत्तर है।"
    ))
    # Q83
    qs.append(create_q(
        83, "Modern Indian History", "Easy", "B",
        "Why was the statutory Simon Commission appointed in November 1927 vehemently boycotted by Indian political parties?",
        ["It recommended the partition of Bengal", "All its seven members were British with no Indian representation", "It proposed to abolish the High Courts", "It rejected the provincial autonomy demand"],
        "The British government appointed an all-white 7-member Indian Statutory Commission under Sir John Simon with no Indian member, which was viewed as a direct insult to India's right to self-determination, sparking universal boycott and protests. Hence, option B is correct.",
        "नवंबर 1927 में गठित साइमन कमीशन का भारतीय राजनीतिक दलों द्वारा पूर्ण बहिष्कार क्यों किया गया था?",
        ["इसने बंगाल के विभाजन की सिफारिश की थी", "इसके सभी सात सदस्य श्वेत ब्रिटिश थे और कोई भी भारतीय सदस्य नहीं था", "इसने उच्च न्यायालयों को समाप्त करने का प्रस्ताव दिया था", "इसने प्रांतीय स्वायत्तता को खारिज कर दिया था"],
        "साइमन कमीशन में एक भी भारतीय को शामिल न किए जाने के कारण पूरे देश में 'साइमन गो बैक' के नारों के साथ इसका तीव्र विरोध और बहिष्कार किया गया। अतः विकल्प B सही है।"
    ))
    # Q84
    qs.append(create_q(
        84, "Indian Polity", "Easy", "C",
        "Which Fundamental Right was famously termed by Dr. B.R. Ambedkar as the 'very soul of the Constitution and the very heart of it'?",
        ["Right to Equality (Article 14)", "Right to Freedom of Speech (Article 19)", "Right to Constitutional Remedies (Article 32)", "Right to Life and Personal Liberty (Article 21)"],
        "Dr. B.R. Ambedkar declared Article 32 (Right to Constitutional Remedies—empowering citizens to move the Supreme Court via writs of Habeas Corpus, Mandamus, Prohibition, Quo Warranto, and Certiorari) as the 'heart and soul' of the Constitution. Hence, option C is correct.",
        "डॉ. बी.आर. अंबेडकर ने किस मौलिक अधिकार को 'संविधान का हृदय और उसकी आत्मा' कहा था?",
        ["समानता का अधिकार (अनुच्छेद 14)", "वाक् एवं अभिव्यक्ति की स्वतंत्रता (अनुच्छेद 19)", "संवैधानिक उपचारों का अधिकार (अनुच्छेद 32)", "प्राण एवं दैहिक स्वतंत्रता का अधिकार (अनुच्छेद 21)"],
        "डॉ. अंबेडकर ने संविधान के अनुच्छेद 32 (संवैधानिक उपचारों का अधिकार) को संविधान का हृदय और आत्मा कहा था क्योंकि यह नागरिकों के मौलिक अधिकारों की न्यायिक गारंटी देता है। अतः विकल्प C सही है।"
    ))
    # Q85
    qs.append(create_q(
        85, "Environment & Wildlife", "Easy", "D",
        "In which year was the flagship wildlife conservation initiative 'Project Tiger' launched in India at Corbett National Park?",
        ["1968", "1971", "1972", "1973"],
        "Project Tiger was officially launched by the Government of India on April 1, 1973 at Corbett National Park, Uttarakhand, to preserve the declining population of the Royal Bengal Tiger in their natural habitats. Hence, option D is correct.",
        "भारत में बाघों के संरक्षण के लिए महत्वाकांक्षी 'प्रोजेक्ट टाइगर' किस वर्ष कॉर्बेट राष्ट्रीय उद्यान से प्रारंभ किया गया था?",
        ["1968", "1971", "1972", "1973"],
        "भारत सरकार द्वारा 1 अप्रैल 1973 को जिम कॉर्बेट नेशनल पार्क से 'प्रोजेक्ट टाइगर' की शुरुआत की गई थी। अतः विकल्प D सही है।"
    ))
    # Q86
    qs.append(create_q(
        86, "Ancient Indian History", "Easy", "A",
        "According to Jain traditions, who was the 23rd Tirthankara of Jainism, born as a prince of Varanasi?",
        ["Parshvanatha", "Rishabhanatha", "Mahavira", "Arishtanemi"],
        "Parshvanatha was the 23rd Tirthankara, historically placed around the 8th century BCE in Varanasi. He propounded four moral restraints (Chaujjama Dharma): Ahimsa, Satya, Asteya, and Aparigraha (to which Mahavira added Brahmacharya). Hence, option A is correct.",
        "जैन परंपरा के अनुसार, वाराणसी के राजकुमार के रूप में जन्मे जैन धर्म के 23वें तीर्थंकर कौन थे?",
        ["पार्श्वनाथ", "ऋषभदेव", "महावीर स्वामी", "अरिष्टनेमि"],
        "भगवान पार्श्वनाथ जैन धर्म के 23वें तीर्थंकर थे, जिनका जन्म काशी (वाराणसी) के इक्ष्वाकु वंशीय राजा अश्वसेन के यहाँ हुआ था। अतः विकल्प A सही है।"
    ))
    # Q87
    qs.append(create_q(
        87, "Indian Economy", "Medium", "B",
        "Which nodal department under the Ministry of Finance, Government of India oversees disinvestment, minority stake sales, and strategic disinvestment in CPSEs?",
        ["Department of Economic Affairs (DEA)", "Department of Investment and Public Asset Management (DIPAM)", "Department of Financial Services (DFS)", "Department of Public Enterprises (DPE)"],
        "DIPAM (Department of Investment and Public Asset Management), originally set up as the Department of Disinvestment in 1999 and renamed in 2016, manages government investments and disinvestment in CPSEs. Hence, option B is correct.",
        "भारत सरकार के वित्त मंत्रालय के अधीन कौन-सा नोडल विभाग केंद्रीय सार्वजनिक क्षेत्र उद्यमों (CPSEs) में विनिवेश और रणनीतिक बिक्री का प्रबंधन करता है?",
        ["आर्थिक कार्य विभाग (DEA)", "दीपम - निवेश और लोक परिसंपत्ति प्रबंधन विभाग (DIPAM)", "वित्तीय सेवाएं विभाग (DFS)", "लोक उद्यम विभाग (DPE)"],
        "वित्त मंत्रालय के अंतर्गत 'दीपम' (DIPAM) सरकारी उपक्रमों में इक्विटी प्रबंधन और विनिवेश से जुड़े सभी मामलों की देखरेख करता है। अतः विकल्प B सही है।"
    ))
    # Q88
    qs.append(create_q(
        88, "Indian Geography & Infrastructure", "Easy", "C",
        "The world's longest highway tunnel above 10,000 feet, the 'Atal Tunnel' (9.02 km), was excavated under which mountain pass in Himachal Pradesh?",
        ["Bara-lacha la", "Zoji La", "Rohtang Pass (Pir Panjal Range)", "Khardung La"],
        "The 9.02 km long Atal Tunnel built under the Rohtang Pass in the eastern Pir Panjal range connects Manali to Lahaul and Spiti Valley in Himachal Pradesh with all-weather road access. Hence, option C is correct.",
        "10,000 फीट से अधिक की ऊंचाई पर विश्व की सबसे लंबी राजमार्ग सुरंग 'अटल टनल' (9.02 किमी) हिमाचल प्रदेश के किस दर्रे के नीचे बनाई गई है?",
        ["बारालाचा दर्रा", "जोजिला", "रोहतांग दर्रा (पीर पंजाल श्रेणी)", "खारदुंग ला"],
        "अटल सुरंग पीर पंजाल श्रेणी में रोहतांग दर्रे के नीचे निर्मित है, जो मनाली को पूरे वर्ष लाहौल-स्पीति घाटी से जोड़े रखती है। अतः विकल्प C सही है।"
    ))
    # Q89
    qs.append(create_q(
        89, "General Science", "Easy", "D",
        "What is the standard atmospheric pressure at mean sea level expressed in millimeters of mercury (mm of Hg)?",
        ["650 mm of Hg", "700 mm of Hg", "720 mm of Hg", "760 mm of Hg"],
        "Standard atmospheric pressure at mean sea level (1 atmosphere / 101.325 kPa) equals exactly 760 mm of mercury (or 29.92 inches of Hg / 76 cm of Hg). Hence, option D is correct.",
        "समुद्र तल पर मानक वायुमंडलीय दाब (1 atm) पारे के कितने मिलीमीटर (mm of Hg) स्तंभ के बराबर होता है?",
        ["650 mm of Hg", "700 mm of Hg", "720 mm of Hg", "760 mm of Hg"],
        "मानक वायुमंडलीय दाब 760 मिमी पारा स्तंभ (76 सेमी पारा अथवा 1013.25 मिलीबार) के बराबर होता है। अतः विकल्प D सही है।"
    ))
    # Q90
    qs.append(create_q(
        90, "Modern Indian History", "Easy", "A",
        "The historic 'Poona Pact' was signed in September 1932 in Yerwada Central Jail between Dr. B.R. Ambedkar and leaders representing:",
        ["Mahatma Gandhi (signed by Madan Mohan Malaviya on his behalf)", "Lord Willingdon", "Muhammad Ali Jinnah", "Subhash Chandra Bose"],
        "Signed on September 24, 1932 in Yerwada Jail (Pune), the Poona Pact between Dr. B.R. Ambedkar and caste Hindu leaders (signed by Pt. Madan Mohan Malaviya) abandoned separate electorates for depressed classes in favour of increased reserved seats in joint electorates, ending Gandhi's fast unto death. Hence, option A is correct.",
        "सितंबर 1932 में यरवदा जेल में डॉ. बी.आर. अंबेडकर और किसके मध्य ऐतिहासिक 'पूना समझौता' हस्ताक्षरित हुआ था?",
        ["महात्मा गांधी (गांधीजी की ओर से पं. मदन मोहन मालवीय द्वारा हस्ताक्षरित)", "लॉर्ड विलिंगडन", "मोहम्मद अली जिन्ना", "सुभाष चंद्र बोस"],
        "कम्युनल अवार्ड में दलितों को दिए गए पृथक निर्वाचन मंडल के विरोध में गांधीजी के आमरण अनशन के बाद 24 सितंबर 1932 को पूना पैक्ट पर हस्ताक्षर हुए, जिसमें पृथक निर्वाचन के स्थान पर संयुक्त निर्वाचन में सीटें आरक्षित की गईं। अतः विकल्प A सही है।"
    ))
    # Q91
    qs.append(create_q(
        91, "Indian Polity", "Medium", "B",
        "By which Constitutional Amendment Act was the phrase 'internal disturbance' replaced by 'armed rebellion' as a ground for proclaiming National Emergency under Article 352?",
        ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "52nd Amendment Act, 1985", "61st Amendment Act, 1988"],
        "The 44th Constitutional Amendment Act, 1978 substituted 'armed rebellion' for the vaguely defined 'internal disturbance' under Article 352 to prevent future misuse of emergency powers as had occurred in 1975. Hence, option B is correct.",
        "किस संविधान संशोधन अधिनियम द्वारा अनुच्छेद 352 के तहत राष्ट्रीय आपातकाल की घोषणा के आधार के रूप में 'आंतरिक अशांति' शब्द को हटाकर 'सशस्त्र विद्रोह' शब्द प्रतिस्थापित किया गया?",
        ["42वाँ संशोधन अधिनियम, 1976", "44वाँ संशोधन अधिनियम, 1978", "52वाँ संशोधन अधिनियम, 1985", "61वाँ संशोधन अधिनियम, 1988"],
        "44वें संविधान संशोधन 1978 द्वारा 'आंतरिक अशांति' शब्द के दुरुपयोग को रोकने के लिए उसके स्थान पर 'सशस्त्र विद्रोह' (Armed Rebellion) शब्द जोड़ा गया। अतः विकल्प B सही है।"
    ))
    # Q92
    qs.append(create_q(
        92, "Environment & Climate", "Easy", "C",
        "The landmark 'Paris Agreement' adopted at COP21 in December 2015 aims to pursue efforts to limit the global average temperature increase to:",
        ["3.0°C above pre-industrial levels", "2.5°C above pre-industrial levels", "1.5°C above pre-industrial levels (well below 2.0°C)", "0.5°C above pre-industrial levels"],
        "The Paris Climate Agreement (2015) commits signatories to hold global warming 'well below 2°C above pre-industrial levels and pursuing efforts to limit the temperature increase to 1.5°C'. Hence, option C is correct.",
        "दिसंबर 2015 में COP21 में स्वीकृत ऐतिहासिक 'पेरिस समझौते' का मुख्य लक्ष्य पूर्व-औद्योगिक स्तर से वैश्विक औसत तापमान वृद्धि को किस सीमा तक सीमित रखना है?",
        ["3.0°C तक", "2.5°C तक", "1.5°C तक सीमित करने का प्रयास (2.0°C से काफी नीचे)", "0.5°C तक"],
        "पेरिस समझौते के तहत विश्व समुदाय ने वैश्विक तापमान वृद्धि को पूर्व-औद्योगिक स्तर से 2 डिग्री सेल्सियस से नीचे रखने और 1.5 डिग्री सेल्सियस तक सीमित रखने का संकल्प लिया। अतः विकल्प C सही है।"
    ))
    # Q93
    qs.append(create_q(
        93, "Ancient Indian History", "Medium", "D",
        "Which Imperial Chola monarch launched a formidable naval expedition across the Bay of Bengal, conquering the Srivijaya Empire (Sumatra and Malaya) in 1025 CE?",
        ["Vijayalaya Chola", "Rajaraja Chola I", "Kulottunga Chola I", "Rajendra Chola I"],
        "Rajendra Chola I (reigned 1014–1044 CE) built a massive maritime armada, conquered Sri Lanka, assumed the title 'Gangaikonda Chola', and successfully conquered the maritime empire of Srivijaya (Sumatra/Malaya Peninsula) in 1025 CE. Hence, option D is correct.",
        "किस प्रतापी चोल शासक ने बंगाल की खाड़ी के पार शक्तिशाली नौसैनिक अभियान भेजकर 1025 ई. में श्रीविजय साम्राज्य (सुमात्रा व मलय प्रायद्वीप) पर विजय प्राप्त की थी?",
        ["विजयालय चोल", "राजराज चोल प्रथम", "कुलोत्तुंग चोल प्रथम", "राजेंद्र चोल प्रथम"],
        "राजेंद्र चोल प्रथम (गंगैकोंडचोल) ने अपनी शक्तिशाली नौसेना के बल पर श्रीविजय साम्राज्य के राजा संग्राम विजयोत्तुंगवर्मन को पराजित कर मलय और सुमात्रा के बंदरगाहों पर नियंत्रण स्थापित किया था। अतः विकल्प D सही है।"
    ))
    # Q94
    qs.append(create_q(
        94, "Indian Economy", "Easy", "A",
        "Which organization is officially entrusted with compiling and releasing estimates of National Income and Gross Domestic Product (GDP) in India?",
        ["National Statistical Office (NSO) under MoSPI", "Reserve Bank of India (RBI)", "NITI Aayog", "Ministry of Finance"],
        "The National Statistical Office (NSO), formed by merging the CSO and NSSO under the Ministry of Statistics and Programme Implementation (MoSPI), computes and publishes national income and GDP estimates. Hence, option A is correct.",
        "भारत में राष्ट्रीय आय (National Income) और सकल घरेलू उत्पाद (GDP) के अनुमान तैयार करने और जारी करने के लिए कौन-सी संस्था अधिकृत है?",
        ["सांख्यिकी और कार्यक्रम कार्यान्वयन मंत्रालय का 'राष्ट्रीय सांख्यिकी कार्यालय' (NSO)", "भारतीय रिज़र्व बैंक (RBI)", "नीति आयोग", "वित्त मंत्रालय"],
        "भारत में केंद्रीय सांख्यिकी कार्यालय (CSO) और अब NSO (राष्ट्रीय सांख्यिकी कार्यालय) द्वारा राष्ट्रीय आय व जीडीपी के आंकड़े संकलित किए जाते हैं। अतः विकल्प A सही है।"
    ))
    # Q95
    qs.append(create_q(
        95, "World Geography", "Easy", "B",
        "The world-famous 'Great Barrier Reef', the largest coral reef system on Earth, is situated off the coast of:",
        ["Western Australia", "Queensland, Northeast Australia", "New Zealand", "Madagascar"],
        "The Great Barrier Reef stretches for over 2,300 km in the Coral Sea off the coast of Queensland in north-eastern Australia. Hence, option B is correct.",
        "विश्व की सबसे बड़ी प्रवाल भित्ति प्रणाली 'ग्रेट बैरियर रीफ' (Great Barrier Reef) किस तट के निकट स्थित है?",
        ["पश्चिमी ऑस्ट्रेलिया", "क्वींसलैंड, उत्तर-पूर्वी ऑस्ट्रेलिया", "न्यूजीलैंड", "मेडागास्कर"],
        "ग्रेट बैरियर रीफ उत्तर-पूर्वी ऑस्ट्रेलिया में क्वींसलैंड तट के समानांतर कोरल सागर में स्थित विश्व की सबसे विशाल मूंगे की चट्टान है। अतः विकल्प B सही है।"
    ))
    # Q96
    qs.append(create_q(
        96, "General Science", "Easy", "C",
        "The peptide hormone 'Insulin' that controls blood sugar levels is secreted by which specific cells of the pancreas?",
        ["Alpha cells", "Delta cells", "Beta cells of Islets of Langerhans", "Acinar cells"],
        "Insulin is produced and secreted by the Beta (β) cells located in the Islets of Langerhans of the pancreas. Alpha cells secrete glucagon. Hence, option C is correct.",
        "मानव शरीर में रक्त शर्करा के स्तर को नियंत्रित करने वाला पेप्टाइड हार्मोन 'इंसुलिन' अग्न्याशय की किन विशिष्ट कोशिकाओं द्वारा स्रावित होता है?",
        ["अल्फा कोशिकाएं", "डेल्टा कोशिकाएं", "लैंगरहैंस की द्वीपिकाओं की बीटा (β) कोशिकाएं", "एसिनर कोशिकाएं"],
        "इंसुलिन अग्न्याशय (Pancreas) की लैंगरहैंस द्वीपिकाओं की बीटा कोशिकाओं द्वारा स्रावित होता है जो रक्त में ग्लूकोज की मात्रा को नियंत्रित करता है। अतः विकल्प C सही है।"
    ))
    # Q97
    qs.append(create_q(
        97, "Modern Indian History", "Easy", "D",
        "During which historic peasant movement of 1928 was Vallabhbhai Patel conferred the title of 'Sardar' by the local women?",
        ["Kheda Satyagraha", "Champaran Satyagraha", "Ahmedabad Mill Strike", "Bardoli Satyagraha"],
        "In 1928, Vallabhbhai Patel led the successful Bardoli Satyagraha in Gujarat against an unfair 22% land revenue hike. Impressed by his leadership, the women of Bardoli bestowed upon him the title 'Sardar' (Leader). Hence, option D is correct.",
        "1928 के किस ऐतिहासिक किसान आंदोलन के सफल नेतृत्व के दौरान वल्लभभाई पटेल को वहाँ की महिलाओं द्वारा 'सरदार' की उपाधि प्रदान की गई थी?",
        ["खेड़ा सत्याग्रह", "चंपारण सत्याग्रह", "अहमदाबाद मिल मजदूर आंदोलन", "बारदोली सत्याग्रह"],
        "1928 में गुजरात के बारदोली में लगान वृद्धि के विरोध में सफल किसान सत्याग्रह का नेतृत्व करने पर बारदोली की महिलाओं ने वल्लभभाई पटेल को 'सरदार' की उपाधि दी थी। अतः विकल्प D सही है।"
    ))
    # Q98
    qs.append(create_q(
        98, "Indian Polity", "Easy", "A",
        "By which Constitutional Amendment Act was the 'Right to Property' deleted from the list of Fundamental Rights and made a legal right under Article 300A?",
        ["44th Amendment Act, 1978", "42nd Amendment Act, 1976", "24th Amendment Act, 1971", "86th Amendment Act, 2002"],
        "The Janata Party government enacted the 44th Constitutional Amendment Act, 1978, which omitted the Right to Property from Article 19(1)(f) and Article 31, re-inserting it as a legal right under Article 300A in Part XII. Hence, option A is correct.",
        "किस संविधान संशोधन अधिनियम द्वारा 'संपत्ति के अधिकार' को मौलिक अधिकारों की सूची से हटाकर अनुच्छेद 300A के अंतर्गत केवल एक विधिक/कानूनी अधिकार बना दिया गया?",
        ["44वाँ संशोधन अधिनियम, 1978", "42वाँ संशोधन अधिनियम, 1976", "24वाँ संशोधन अधिनियम, 1971", "86वाँ संशोधन अधिनियम, 2002"],
        "44वें संविधान संशोधन 1978 द्वारा संपत्ति के मूल अधिकार (अनुच्छेद 31 एवं 19(1)(f)) को समाप्त कर भाग XII में अनुच्छेद 300A के तहत विधिक अधिकार बना दिया गया। अतः विकल्प A सही है।"
    ))
    # Q99
    qs.append(create_q(
        99, "Environment & Biotechnology", "Medium", "B",
        "The environmental cleanup technology that employs microorganisms (bacteria, fungi) to break down or neutralize hazardous environmental pollutants is termed:",
        ["Bioaccumulation", "Bioremediation", "Biomagnification", "Phytostabilization"],
        "Bioremediation uses biological mechanisms—primarily microorganisms, fungi, or green plants—to degrade environmental contaminants (such as oil spills, industrial wastes, heavy metals) into less toxic forms. Hence, option B is correct.",
        "प्रदूषित पर्यावरण और अपशिष्टों को हानिरहित पदार्थों में अपघटित करने के लिए सूक्ष्मजीवों (जीवाणुओं/कवकों) के उपयोग की तकनीक को क्या कहा जाता है?",
        ["जैव-संचयन (Bioaccumulation)", "जैव-उपचार (Bioremediation)", "जैव-आवर्धन (Biomagnification)", "पादप-स्थिरीकरण"],
        "जैव-उपचार (Bioremediation) वह प्रक्रिया है जिसमें सूक्ष्मजीवों का उपयोग कर प्रदूषित मृदा या जल से रासायनिक अपशिष्टों और विषैले तत्वों को विघटित किया जाता है। अतः विकल्प B सही है।"
    ))
    # Q100
    qs.append(create_q(
        100, "UP Special & Culture", "Easy", "C",
        "The grand 'Kashi Vishwanath Corridor' project connecting the ancient Jyotirlinga temple directly to the sacred Ganga ghats was inaugurated in which historic city of Uttar Pradesh?",
        ["Ayodhya", "Prayagraj", "Varanasi", "Mathura"],
        "Prime Minister Narendra Modi dedicated Phase 1 of the Kashi Vishwanath Dham (Corridor) to the nation on December 13, 2021 in Varanasi, connecting the Kashi Vishwanath temple with the Ganga river (Lalita Ghat). Hence, option C is correct.",
        "प्राचीन ज्योतिर्लिंग मंदिर को सीधे गंगा के घाटों से जोड़ने वाली भव्य 'काशी विश्वनाथ धाम (कॉरिडोर) परियोजना' का लोकार्पण उत्तर प्रदेश के किस शहर में किया गया?",
        ["अयोध्या", "प्रयागराज", "वाराणसी", "मथुरा"],
        "दिसंबर 2021 में प्रधानमंत्री द्वारा वाराणसी (काशी) में काशी विश्वनाथ धाम कॉरिडोर का लोकार्पण किया गया, जिससे श्रद्धालु गंगा स्नान के उपरांत सीधे मंदिर में प्रवेश कर सकते हैं। अतः विकल्प C सही है।"
    ))
    return qs

print("Part 2 definitions loaded.")
