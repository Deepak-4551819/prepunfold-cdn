#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_2022_gs1_part3.py — Questions 101 to 150 of UPPSC PCS Prelims 2022 GS-1."""
import json
import os

from build_uppcs_2022_gs1 import create_q, get_questions_1_to_50
from build_uppcs_2022_gs1_full import get_questions_51_to_100

def get_questions_101_to_150():
    qs = []
    # Q101
    qs.append(create_q(
        101, "Ancient Indian History", "Easy", "C",
        "Which Major Rock Edict of Mauryan Emperor Ashoka gives a detailed account of the Kalinga War and Ashoka's remorse and conversion to Dhamma?",
        ["Major Rock Edict I", "Major Rock Edict V", "Major Rock Edict XIII", "Major Rock Edict X"],
        "Major Rock Edict XIII (the largest of all edicts) provides a poignant description of the conquest of Kalinga (261 BCE), the tremendous loss of human life, and Ashoka's profound grief, resulting in his renunciation of military conquest (Bherighosha) in favour of spiritual conquest (Dhammaghosha). Hence, option C is correct.",
        "मौर्य सम्राट अशोक का कौन-सा प्रमुख शिलालेख कलिंग युद्ध के विनाश और अशोक के हृदय परिवर्तन तथा धम्म-विजय का विस्तृत विवरण देता है?",
        ["प्रथम शिलालेख", "पाँचवाँ शिलालेख", "तेरहवाँ शिलालेख (Rock Edict XIII)", "दसवाँ शिलालेख"],
        "अशोक के 13वें शिलालेख में कलिंग युद्ध (261 ईसा पूर्व) का हृदयविदारक वर्णन और उसके बाद युद्ध त्याग कर 'धम्मघोष' अपनाने का उल्लेख मिलता है। अतः विकल्प C सही है।"
    ))
    # Q102
    qs.append(create_q(
        102, "Indian Polity", "Easy", "B",
        "Which Article of the Constitution of India guarantees 'Equality before the law and equal protection of the laws' within the territory of India?",
        ["Article 19", "Article 14", "Article 21", "Article 25"],
        "Article 14 guarantees that 'The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India'. Equality before law is borrowed from British common law, and equal protection of laws from the US Constitution. Hence, option B is correct.",
        "भारतीय संविधान का कौन-सा अनुच्छेद भारत के राज्यक्षेत्र में 'विधि के समक्ष समता और विधियों के समान संरक्षण' की गारंटी देता है?",
        ["अनुच्छेद 19", "अनुच्छेद 14", "अनुच्छेद 21", "अनुच्छेद 25"],
        "संविधान के भाग III में अनुच्छेद 14 यह घोषित करता है कि राज्य किसी भी व्यक्ति को विधि के समक्ष समता या विधियों के समान संरक्षण से वंचित नहीं करेगा। अतः विकल्प B सही है।"
    ))
    # Q103
    qs.append(create_q(
        103, "General Science & Environment", "Easy", "A",
        "Eco-friendly 'Green Crackers' emitting 30% less particulate pollution (SWAS, STAR, SAFAL) were developed in India by which scientific research institution?",
        ["CSIR-NEERI (National Environmental Engineering Research Institute)", "ISRO", "DRDO", "BARC"],
        "Green Crackers with reduced emission formulations (SWAS - Safe Water Releaser, STAR - Safe Thermite Cracker, SAFAL - Safe Minimal Aluminium) were formulated by CSIR-NEERI (Nagpur). Hence, option A is correct.",
        "30% कम प्रदूषणकारी पर्यावरण-अनुकूल 'ग्रीन पटाखे' (SWAS, STAR, SAFAL) भारत के किस वैज्ञानिक अनुसंधान संस्थान द्वारा विकसित किए गए?",
        ["CSIR-नीरी (राष्ट्रीय पर्यावरण अभियांत्रिकी अनुसंधान संस्थान, नागपुर)", "इसरो (ISRO)", "डीआरडीओ (DRDO)", "भाभा परमाणु अनुसंधान केंद्र (BARC)"],
        "काउंसिल ऑफ साइंटिफिक एंड इंडस्ट्रियल रिसर्च - नीरी (CSIR-NEERI) ने प्रदूषण को 30% तक कम करने वाले ग्रीन पटाखों का विकास किया। अतः विकल्प A सही है।"
    ))
    # Q104
    qs.append(create_q(
        104, "Modern Indian History", "Easy", "D",
        "The 'Permanent Settlement' (Zamindari Bandobast) system of land revenue was introduced in Bengal and Bihar in 1793 by Governor-General:",
        ["Lord Warren Hastings", "Lord Wellesley", "Lord William Bentinck", "Lord Cornwallis"],
        "Lord Cornwallis introduced the Permanent Settlement in Bengal, Bihar, and Odisha in 1793, fixing the land revenue demand perpetually with Zamindars recognized as owners of the land (yielding 10/11th to Company and 1/11th to Zamindar). Hence, option D is correct.",
        "1793 में बंगाल और बिहार में भू-राजस्व की 'स्थाई बंदोबस्त' (इस्तमरारी प्रथा) किस गवर्नर-जनरल द्वारा लागू की गई थी?",
        ["लॉर्ड वारेन हेस्टिंग्स", "लॉर्ड वेलेजली", "लॉर्ड विलियम बेंटिंक", "लॉर्ड कॉर्नवालिस"],
        "लॉर्ड कॉर्नवालिस ने 1793 में जमींदारों के साथ भू-राजस्व का स्थाई बंदोबस्त लागू किया, जिसके तहत कंपनी का हिस्सा 10/11 और जमींदार का हिस्सा 1/11 निर्धारित किया गया। अतः विकल्प D सही है।"
    ))
    # Q105
    qs.append(create_q(
        105, "Indian Economy & Public Finance", "Medium", "C",
        "In government budgetary terminology, 'Fiscal Deficit' is precisely defined as:",
        ["Total Revenue Receipts minus Total Revenue Expenditure", "Total Expenditure minus Total Revenue Receipts", "Total Expenditure minus Total Receipts (excluding Borrowings)", "Fiscal Deficit minus Interest Payments"],
        "Fiscal Deficit represents the total borrowing requirements of the government from all sources: Total Expenditure - (Revenue Receipts + Non-debt Capital Receipts). Fiscal Deficit minus interest payments is Primary Deficit. Hence, option C is correct.",
        "सरकारी बजट में 'राजकोषीय घाटा' (Fiscal Deficit) की सही परिभाषा क्या है?",
        ["कुल राजस्व प्राप्तियाँ घटाव कुल राजस्व व्यय", "कुल व्यय घटाव कुल राजस्व प्राप्तियाँ", "कुल व्यय घटाव कुल प्राप्तियाँ (उधारियों/ऋणों को छोड़कर)", "राजकोषीय घाटा घटाव ब्याज भुगतान"],
        "राजकोषीय घाटा सरकार के कुल व्यय और उधारियों को छोड़कर कुल प्राप्तियों का अंतर होता है, जो सरकार की कुल ऋण आवश्यकता को दर्शाता है। अतः विकल्प C सही है।"
    ))
    # Q106
    qs.append(create_q(
        106, "Indian Geography", "Easy", "B",
        "In the Panch Prayag sequence of Uttarakhand, the holy confluence of River Alaknanda and River Mandakini takes place at:",
        ["Karnaprayag", "Rudraprayag", "Devprayag", "Nandaprayag"],
        "At Rudraprayag, the Alaknanda River meets the Mandakini River (flowing from Kedarnath). At Karnaprayag, it meets Pindar; at Nandaprayag, Nandakini; and at Devprayag, Bhagirathi. Hence, option B is correct.",
        "उत्तराखंड के पंच प्रयागों में अलकनंदा और मंदाकिनी नदी का संगम किस स्थल पर होता है?",
        ["कर्णप्रयाग", "रुद्रप्रयाग", "देवप्रयाग", "नंदप्रयाग"],
        "रुद्रप्रयाग में अलकनंदा और केदारनाथ से आने वाली मंदाकिनी नदी का पवित्र संगम होता है। अतः विकल्प B सही है।"
    ))
    # Q107
    qs.append(create_q(
        107, "General Science", "Easy", "A",
        "Deficiency of Vitamin A (Retinol) in the human body causes which of the following ocular disorders?",
        ["Night Blindness (Nyctalopia) and Xerophthalmia", "Glaucoma", "Myopia", "Cataract"],
        "Vitamin A is necessary for rhodopsin synthesis in rod cells of the retina. Its deficiency leads to night blindness (nyctalopia) and severe drying of cornea/conjunctiva (xerophthalmia). Hence, option A is correct.",
        "मानव शरीर में विटामिन A (रेटिनॉल) की कमी से निम्नलिखित में से कौन-सा नेत्र रोग होता है?",
        ["रतौंधी (Night Blindness) और जेरोफथाल्मिया", "मोतियाबिंद", "निकट दृष्टि दोष", "ग्लूकोमा"],
        "विटामिन A की कमी से आँखों में रतौंधी (कम रोशनी में न दिखाई देना) तथा आँखों के सूखने का रोग (जेरोफथाल्मिया) हो जाता है। अतः विकल्प A सही है।"
    ))
    # Q108
    qs.append(create_q(
        108, "Modern Indian History", "Easy", "D",
        "The notorious 'Rowlatt Act' passed by the Imperial Legislative Council in March 1919 was officially titled the:",
        ["Defence of India Regulations Act", "Indian Arms and Ammunition Act", "Prevention of Seditious Meetings Act", "Anarchical and Revolutionary Crimes Act"],
        "The Rowlatt Act was officially named the 'Anarchical and Revolutionary Crimes Act of 1919'. It empowered the British government to arrest and detain any person suspected of sedition without warrant or trial for up to two years. Hence, option D is correct.",
        "मार्च 1919 में ब्रिटिश सरकार द्वारा पारित कुख्यात 'रौलट एक्ट' (Rowlatt Act) का आधिकारिक नाम क्या था?",
        ["भारत रक्षा नियमन अधिनियम", "भारतीय शस्त्र अधिनियम", "देशद्रोही सभा निवारण अधिनियम", "अराजक और क्रांतिकारी अपराध अधिनियम (Anarchical and Revolutionary Crimes Act)"],
        "रौलट एक्ट का आधिकारिक नाम 'अनार्किक एंड रिवोल्यूशनरी क्राइम्स एक्ट, 1919' था। इसे 'बिना वकील, बिना अपील, बिना दलील' का कानून भी कहा जाता था। अतः विकल्प D सही है।"
    ))
    # Q109
    qs.append(create_q(
        109, "Indian Polity", "Easy", "C",
        "The Directive Principles of State Policy (DPSP) contained in Part IV of the Indian Constitution were inspired by the Constitution of which country?",
        ["USA", "USSR", "Ireland (Irish Republic)", "Australia"],
        "The makers of the Indian Constitution borrowed the Directive Principles of State Policy (Articles 36 to 51) from the Constitution of Ireland (1937), which in turn had copied them from the Spanish Constitution. Hence, option C is correct.",
        "भारतीय संविधान के भाग IV में वर्णित 'राज्य के नीति निर्देशक तत्व' (DPSP) किस देश के संविधान से प्रेरित होकर ग्रहण किए गए हैं?",
        ["संयुक्त राज्य अमेरिका", "सोवियत संघ", "आयरलैंड", "ऑस्ट्रेलिया"],
        "भारतीय संविधान में राज्य के नीति निर्देशक तत्व आयरलैंड के 1937 के संविधान से प्रेरित होकर शामिल किए गए हैं। अतः विकल्प C सही है।"
    ))
    # Q110
    qs.append(create_q(
        110, "Environment & Ecology", "Easy", "B",
        "The 'Montreal Protocol' signed on 16 September 1987 is an international environmental treaty designed to phase out the production of:",
        ["Greenhouse gases causing global warming", "Substances that Deplete the Ozone Layer (ODS such as CFCs and Halons)", "Hazardous industrial nuclear waste", "Single-use synthetic plastics"],
        "The Montreal Protocol on Substances that Deplete the Ozone Layer was signed on 16 September 1987 (celebrated as World Ozone Day) to progressively eliminate chlorofluorocarbons (CFCs), halons, and carbon tetrachloride. Hence, option B is correct.",
        "16 सितंबर 1987 को हस्ताक्षरित 'मॉन्ट्रियल प्रोटोकॉल' किस पर्यावरण समस्या से निपटने के लिए ओजोन क्षयकारी पदार्थों के उत्पादन को समाप्त करने से संबंधित है?",
        ["ग्लोबल वार्मिंग गैसें", "ओजोन परत को नुकसान पहुँचाने वाले पदार्थ (CFCs और हैलोन)", "परमाणु अपशिष्ट", "एकल-उपयोग प्लास्टिक"],
        "मॉन्ट्रियल प्रोटोकॉल ओजोन परत के क्षरण को रोकने के लिए क्लोरोफ्लोरोकार्बन (CFCs) जैसे ओजोन क्षयकारी पदार्थों पर रोक लगाने वाली ऐतिहासिक अंतर्राष्ट्रीय संधि है। अतः विकल्प B सही है।"
    ))
    # Q111
    qs.append(create_q(
        111, "Medieval Indian History", "Easy", "A",
        "In which language did the first Mughal Emperor Babur compose his famous authentic autobiography 'Tuzuk-i-Baburi' (Baburnama)?",
        ["Chagatai Turkish", "Persian", "Arabic", "Urdu"],
        "Babur wrote his memoirs titled 'Tuzuk-i-Baburi' (Baburnama) in his native Chagatai Turkish language. It was later translated into Persian by Abdur Rahim Khan-i-Khana during Akbar's reign. Hence, option A is correct.",
        "प्रथम मुगल सम्राट बाबर ने अपनी प्रसिद्ध आत्मकथा 'तुजुक-ए-बाबरी' (बाबरनामा) किस भाषा में लिखी थी?",
        ["चगताई तुर्की", "फारसी", "अरबी", "उर्दू"],
        "बाबर ने अपनी आत्मकथा अपनी मातृभाषा 'चगताई तुर्की' में लिखी थी, जिसका बाद में अकबर के समय अब्दुर्रहीम खान-ए-खाना ने फारसी में अनुवाद किया था। अतः विकल्प A सही है।"
    ))
    # Q112
    qs.append(create_q(
        112, "Indian Economy & Banking", "Medium", "D",
        "What is the definition of 'Repo Rate' in Indian monetary policy operations?",
        ["The interest rate at which commercial banks park excess reserves with RBI", "The rate at which RBI lends long-term funds to government", "The statutory cash reserve ratio", "The interest rate at which the Reserve Bank of India lends short-term liquidity to commercial banks against government securities"],
        "Repo (Repurchase Option) Rate is the benchmark policy interest rate at which the central bank (RBI) provides short-term liquidity to commercial banks against the collateral of government and approved securities. Hence, option D is correct.",
        "भारतीय मौद्रिक नीति में 'रेपो दर' (Repo Rate) की सही परिभाषा क्या है?",
        ["वह दर जिस पर वाणिज्यिक बैंक अपनी अतिरिक्त जमा राशि आरबीआई के पास रखते हैं", "वह दर जिस पर आरबीआई सरकार को दीर्घकालिक ऋण देता है", "नकद आरक्षित अनुपात दर", "वह ब्याज दर जिस पर भारतीय रिज़र्व बैंक वाणिज्यिक बैंकों को सरकारी प्रतिभूतियों की जमानत पर अल्पकालिक ऋण प्रदान करता है"],
        "रेपो दर वह अल्पकालिक ब्याज दर है जिस पर आरबीआई वाणिज्यिक बैंकों को तरलता की कमी होने पर अल्पकाल के लिए ऋण देता है। अतः विकल्प D सही है।"
    ))
    # Q113
    qs.append(create_q(
        113, "Indian Geography", "Easy", "C",
        "Which is the largest brackish water coastal lagoon in India (and designated India's first Ramsar wetland in 1981)?",
        ["Pulicat Lake", "Vembanad Lake", "Chilika Lake", "Kolleru Lake"],
        "Chilika Lake in Odisha, situated at the mouth of the Daya River flowing into the Bay of Bengal, is the largest brackish water coastal lagoon in India and was designated India's first Ramsar site in 1981. Hence, option C is correct.",
        "भारत में खारे पानी की सबसे बड़ी तटीय लैगून झील कौन-सी है (जिसे 1981 में भारत का प्रथम रामसर स्थल घोषित किया गया था)?",
        ["पुलिकट झील", "वेम्बनाड झील", "चिल्का झील", "कोल्लेरू झील"],
        "ओडिशा में स्थित चिल्का झील भारत की सबसे बड़ी खारे पानी की लैगून झील है, जो विशाल जैव विविधता और प्रवासी पक्षियों का प्रमुख केंद्र है। अतः विकल्प C सही है।"
    ))
    # Q114
    qs.append(create_q(
        114, "General Science & Physics", "Easy", "B",
        "A 'Light Year' is an astronomical physical unit used to quantify:",
        ["Cosmic Time", "Astronomical Distance", "Luminous Intensity", "Stellar Mass"],
        "A light year is the total distance that light travels in a vacuum in one Julian year (approx. 9.46 trillion kilometres or 5.88 trillion miles), which is a unit of astronomical distance. Hence, option B is correct.",
        "खगोल विज्ञान में 'प्रकाश वर्ष' (Light Year) निम्नलिखित में से किसका मात्रक है?",
        ["समय", "खगोलीय दूरी", "प्रकाश की तीव्रता", "तारों का द्रव्यमान"],
        "प्रकाश वर्ष दूरी का मात्रक है। यह वह दूरी है जो प्रकाश निर्वात में एक वर्ष में तय करता है (लगभग 9.46 × 10^12 किमी)। अतः विकल्प B सही है।"
    ))
    # Q115
    qs.append(create_q(
        115, "Modern Indian History", "Easy", "A",
        "Which Indian princely state was the very first to accept and sign the 'Subsidiary Alliance System' introduced by Lord Wellesley in 1798?",
        ["Nizam of Hyderabad", "Nawab of Awadh", "Peshwa Baji Rao II", "Scindias of Gwalior"],
        "The Nizam of Hyderabad was the first Indian ruler to enter into Lord Wellesley's Subsidiary Alliance system in 1798, agreeing to disband his French-trained battalions and maintain a British subsidiary force. Hence, option A is correct.",
        "लॉर्ड वेलेजली द्वारा 1798 में लागू की गई 'सहायक संधि प्रणाली' (Subsidiary Alliance) को स्वीकार करने वाली पहली भारतीय रियासत कौन-सी थी?",
        ["हैदराबाद के निज़ाम", "अवध के नवाब", "पेशवा बाजीराव द्वितीय", "ग्वालियर के सिंधिया"],
        "1798 में हैदराबाद के निज़ाम ने सबसे पहले वेलेजली की सहायक संधि को स्वीकार किया था और ब्रिटिश सेना को अपने राज्य में तैनात करने की सहमति दी थी। अतः विकल्प A सही है।"
    ))
    # Q116
    qs.append(create_q(
        116, "Indian Polity", "Medium", "D",
        "Under Article 131 of the Constitution of India, inter-governmental disputes between the Government of India and one or more States fall under the Supreme Court's:",
        ["Appellate Jurisdiction", "Advisory Jurisdiction", "Writ Jurisdiction", "Original Exclusive Jurisdiction"],
        "Article 131 confers exclusive Original Jurisdiction on the Supreme Court to adjudicate federal disputes: between the Government of India and one or more States, or between two or more States. Hence, option D is correct.",
        "भारतीय संविधान के अनुच्छेद 131 के अंतर्गत भारत सरकार और एक या अधिक राज्यों के बीच होने वाले विवाद सर्वोच्च न्यायालय के किस क्षेत्राधिकार में आते हैं?",
        ["अपीलीय क्षेत्राधिकार", "परामर्शदात्री क्षेत्राधिकार", "रिट क्षेत्राधिकार", "आरंभिक/मूल अनन्य क्षेत्राधिकार (Original Jurisdiction)"],
        "अनुच्छेद 131 के तहत केंद्र और राज्यों के बीच अथवा दो या दो से अधिक राज्यों के मध्य संवैधानिक व विधिक विवादों का निपटारा सर्वोच्च न्यायालय के आरंभिक क्षेत्राधिकार के अधीन आता है। अतः विकल्प D सही है।"
    ))
    # Q117
    qs.append(create_q(
        117, "Environment & Ecology", "Easy", "C",
        "According to Raymond Lindeman's 10% Law of ecological efficiency, how much food energy is transferred from one trophic level to the next higher level in an ecosystem?",
        ["50%", "25%", "10%", "1%"],
        "According to Lindeman's Ten Percent Law (1942), only about 10% of the energy entering a trophic level is stored as biomass and available to the next higher trophic level; 90% is lost through respiration, metabolic work, and heat. Hence, option C is correct.",
        "रेमंड लिंडेमैन के 10 प्रतिशत के पारिस्थितिक नियम के अनुसार, एक पोषण स्तर से अगले उच्च पोषण स्तर तक कितनी ऊर्जा का स्थानांतरण होता है?",
        ["50 प्रतिशत", "25 प्रतिशत", "10 प्रतिशत", "1 प्रतिशत"],
        "पारिस्थितिक तंत्र में ऊर्जा प्रवाह के 10% नियम के अनुसार प्रत्येक पोषण स्तर पर केवल 10% ऊर्जा ही अगले स्तर को स्थानांतरित होती है, शेष 90% ऊर्जा उपापचय एवं ऊष्मा के रूप में नष्ट हो जाती है। अतः विकल्प C सही है।"
    ))
    # Q118
    qs.append(create_q(
        118, "Ancient Indian History & Art", "Medium", "B",
        "The celebrated 'Gandhara School of Art', characterized by Greco-Roman artistic motifs blending with Buddhist iconography, flourished mainly under the patronage of:",
        ["Guptas", "Kushanas (notably Emperor Kanishka)", "Mauryas", "Satavahanas"],
        "The Gandhara school of Buddhist sculpture flourished in northwestern India during the Kushana period (1st to 3rd centuries CE), particularly under the royal patronage of Emperor Kanishka I. Hence, option B is correct.",
        "यूनानी-रोमन कला शैली और बौद्ध विषयवस्तु के मिश्रण वाली 'गांधार कला शैली' का सर्वाधिक विकास किस राजवंश के संरक्षण में हुआ था?",
        ["गुप्त वंश", "कुषाण वंश (विशेषकर सम्राट कनिष्क)", "मौर्य वंश", "सातवाहन वंश"],
        "गांधार कला का चरमोत्कर्ष कुषाण सम्राट कनिष्क और उसके उत्तराधिकारियों के शासनकाल में हुआ, जिसमें बुद्ध की मूर्तियों को यूनानी देवता अपोलो के समान सुगठित शरीर व वस्त्रों के साथ उकेरा गया। अतः विकल्प B सही है।"
    ))
    # Q119
    qs.append(create_q(
        119, "Indian Economy & Financial Inclusion", "Easy", "A",
        "The flagship financial inclusion scheme 'Pradhan Mantri Jan Dhan Yojana' (PMJDY) was officially launched across India on:",
        ["28 August 2014", "15 August 2015", "2 October 2014", "26 January 2015"],
        "Prime Minister Narendra Modi formally launched the National Mission for Financial Inclusion—Pradhan Mantri Jan Dhan Yojana (PMJDY)—on 28 August 2014 with the slogan 'Mera Khata, Bhagya Vidhata'. Hence, option A is correct.",
        "वित्तीय समावेशन की राष्ट्रीय योजना 'प्रधानमंत्री जन-धन योजना' (PMJDY) का देशव्यापी शुभारंभ किस तिथि को किया गया था?",
        ["28 अगस्त 2014", "15 अगस्त 2015", "2 अक्टूबर 2014", "26 जनवरी 2015"],
        "प्रधानमंत्री नरेंद्र मोदी ने 28 अगस्त 2014 को 'मेरा खाता, भाग्य विधाता' के नारे के साथ देश के हर परिवार को बैंकिंग सेवाओं से जोड़ने हेतु जन-धन योजना का शुभारंभ किया था। अतः विकल्प A सही है।"
    ))
    # Q120
    qs.append(create_q(
        120, "World Geography", "Easy", "D",
        "The artificial sea-level waterway that connects the Mediterranean Sea directly with the Red Sea is the:",
        ["Panama Canal", "Kiel Canal", "Corinth Canal", "Suez Canal"],
        "The Suez Canal, constructed across the Isthmus of Suez in Egypt and opened in November 1869, provides a direct maritime shipping shortcut between the Mediterranean Sea and the Red Sea. Hence, option D is correct.",
        "भूमध्य सागर को लाल सागर से सीधे जोड़ने वाली प्रसिद्ध मानव निर्मित जल नहर कौन-सी है?",
        ["पनामा नहर", "कील नहर", "कोरिंथ नहर", "स्वेज नहर (Suez Canal)"],
        "1869 में खोली गई मिस्र की स्वेज नहर भूमध्य सागर को लाल सागर से जोड़ती है, जिससे यूरोप और एशिया के बीच की समुद्री दूरी हजारों किलोमीटर कम हो गई। अतः विकल्प D सही है।"
    ))
    # Q121
    qs.append(create_q(
        121, "General Science & Chemistry", "Easy", "C",
        "What is the chemical formula of 'Washing Soda' commonly used as a laundry detergent and water softening agent?",
        ["NaHCO3", "NaOH", "Na2CO3·10H2O", "CaSO4·2H2O"],
        "Washing soda is Sodium carbonate decahydrate (Na2CO3·10H2O). Sodium bicarbonate (NaHCO3) is baking soda, and Sodium hydroxide (NaOH) is caustic soda. Hence, option C is correct.",
        "कपड़े धोने के सोडे ('धावन सोडा' - Washing Soda) का रासायनिक सूत्र निम्नलिखित में से क्या है?",
        ["NaHCO3", "NaOH", "Na2CO3·10H2O", "CaSO4·2H2O"],
        "धावन सोडा सोडियम कार्बोनेट डेकाहाइड्रेट (Na2CO3·10H2O) होता है, जबकि NaHCO3 बेकिंग सोडा (मीठा सोडा) है। अतः विकल्प C सही उत्तर है।"
    ))
    # Q122
    qs.append(create_q(
        122, "Modern Indian History", "Easy", "B",
        "Which British Viceroy enacted the oppressive 'Vernacular Press Act' in 1878 to silence Indian-language newspapers?",
        ["Lord Ripon", "Lord Lytton", "Lord Curzon", "Lord Dufferin"],
        "Lord Lytton enacted the Vernacular Press Act in 1878 (derisively dubbed the 'Gagging Act') targeted specifically at vernacular newspapers like the Amrita Bazar Patrika. Lord Ripon repealed it in 1882. Hence, option B is correct.",
        "1878 में भारतीय भाषाओं के समाचार पत्रों पर कड़े प्रतिबंध लगाने वाला 'वर्नाक्युलर प्रेस एक्ट' किस ब्रिटिश वायसराय द्वारा पारित किया गया था?",
        ["लॉर्ड रिपन", "लॉर्ड लिटन", "लॉर्ड कर्जन", "लॉर्ड डफरिन"],
        "लॉर्ड लिटन ने 1878 में वर्नाक्युलर प्रेस एक्ट पारित किया, जिसे 'मुंह बंद करने वाला कानून' कहा गया। 1882 में लॉर्ड रिपन ने इसे निरस्त किया था। अतः विकल्प B सही है।"
    ))
    # Q123
    qs.append(create_q(
        123, "Indian Polity", "Easy", "A",
        "The 'Anti-Defection Law' was added to the Tenth Schedule of the Constitution of India by which Constitutional Amendment Act?",
        ["52nd Amendment Act, 1985", "42nd Amendment Act, 1976", "61st Amendment Act, 1988", "91st Amendment Act, 2003"],
        "The 52nd Constitutional Amendment Act, 1985 added the Tenth Schedule to prevent political defection by legislators ('Aaya Ram Gaya Ram' culture). The 91st Amendment Act (2003) strengthened it by removing the split exception. Hence, option A is correct.",
        "किस संविधान संशोधन अधिनियम द्वारा भारतीय संविधान में 10वीं अनुसूची जोड़कर 'दल-बदल विरोधी कानून' (Anti-Defection Law) बनाया गया था?",
        ["52वाँ संशोधन अधिनियम, 1985", "42वाँ संशोधन अधिनियम, 1976", "61वाँ संशोधन अधिनियम, 1988", "91वाँ संशोधन अधिनियम, 2003"],
        "52वें संविधान संशोधन 1985 द्वारा राजीव गांधी सरकार के समय संविधान में 10वीं अनुसूची जोड़ी गई जिसमें संसद और विधानसभाओं में दल-बदल के आधार पर अयोग्यता के नियम तय किए गए। अतः विकल्प A सही है।"
    ))
    # Q124
    qs.append(create_q(
        124, "Environment & Ecology", "Medium", "D",
        "Which of the following atmospheric pollutants is classified as a 'Secondary Pollutant' formed by photochemical reactions?",
        ["Carbon monoxide (CO)", "Sulphur dioxide (SO2)", "Lead particles", "Ground-level Ozone (O3) and PAN"],
        "Primary pollutants (CO, SO2, NO, particulate matter) are emitted directly from sources. Secondary pollutants like Ground-level Ozone and Peroxyacyl nitrates (PAN) form via photochemical interactions of NOx and VOCs in sunlight. Hence, option D is correct.",
        "निम्नलिखित में से कौन-सा वायु प्रदूषक एक 'द्वितीयक प्रदूषक' (Secondary Pollutant) है जो प्रकाश-रासायनिक अभिक्रियाओं द्वारा बनता है?",
        ["कार्बन मोनोऑक्साइड (CO)", "सल्फर डाइऑक्साइड (SO2)", "सीसा (Lead) के कण", "धरातलीय ओजोन (O3) तथा पैन (PAN)"],
        "प्राथमिक प्रदूषक सीधे स्रोतों से निकलते हैं (जैसे CO, SO2), जबकि द्वितीयक प्रदूषक सूर्य के प्रकाश में रासायनिक अभिक्रियाओं से बनते हैं (जैसे धरातलीय ओजोन और फोटोकेमिकल स्मॉग के घटक PAN)। अतः विकल्प D सही है।"
    ))
    # Q125
    qs.append(create_q(
        125, "Modern Indian History", "Easy", "C",
        "The tragic 'Chauri Chaura' incident, which prompted Mahatma Gandhi to abruptly suspend the Non-Cooperation Movement, took place in Gorakhpur district on:",
        ["13 April 1919", "1 August 1920", "4 February 1922", "12 March 1930"],
        "On 4 February 1922, a crowd of protesters clashed with police and set fire to the Chauri Chaura police station in Gorakhpur district (United Provinces), killing 22 policemen. Distressed by the violence, Gandhi withdrew the Non-Cooperation Movement on 12 February 1922. Hence, option C is correct.",
        "किस तिथि को गोरखपुर जिले में 'चौरी-चौरा' की ऐतिहासिक हिंसक घटना घटित हुई थी, जिसके कारण महात्मा गांधी ने असहयोग आंदोलन वापस ले लिया था?",
        ["13 अप्रैल 1919", "1 अगस्त 1920", "4 फरवरी 1922", "12 मार्च 1930"],
        "4 फरवरी 1922 को चौरी-चौरा में प्रदर्शनकारियों की भीड़ ने पुलिस चौकी में आग लगा दी थी जिसमें 22 पुलिसकर्मी मारे गए थे। अहिंसा के उल्लंघन से आहत होकर गांधीजी ने असहयोग आंदोलन स्थगित कर दिया। अतः विकल्प C सही है।"
    ))
    # Q126
    qs.append(create_q(
        126, "Indian Economy", "Medium", "B",
        "The 'Gini Coefficient' is an economic statistical metric universally utilized to measure:",
        ["Inflation rate in consumer goods", "Income or wealth inequality within a population", "Poverty headcount ratio", "Unemployment rate among youth"],
        "The Gini Coefficient (derived from the Lorenz Curve) measures the distribution of income or wealth across a nation, ranging from 0 (perfect equality) to 1 (perfect inequality). Hence, option B is correct.",
        "अर्थशास्त्र में 'गिनी गुणांक' (Gini Coefficient) का प्रयोग मुख्य रूप से किसका मापन करने के लिए किया जाता है?",
        ["मुद्रास्फीति की दर", "आय अथवा संपत्ति के वितरण में असमानता (Inequality)", "गरीबी रेखा का अनुपात", "श्रम बल में बेरोजगारी दर"],
        "लॉरेंज वक्र पर आधारित गिनी गुणांक 0 से 1 के बीच आय या धन के वितरण में पाई जाने वाली गैर-बराबरी (असमानता) को दर्शाता है (0 पूर्ण समानता, 1 पूर्ण असमानता)। अतः विकल्प B सही है।"
    ))
    # Q127
    qs.append(create_q(
        127, "Indian Geography", "Easy", "A",
        "Which is the highest mountain peak in Peninsular India (Western Ghats)?",
        ["Anamudi (2,695 m)", "Doddabetta (2,637 m)", "Guru Shikhar (1,722 m)", "Mahendragiri (1,501 m)"],
        "Anamudi (elevation 2,695 metres / 8,842 feet) in the Anaimalai Hills of Ernakulam/Idukki districts, Kerala, is the highest peak in Peninsular India. Doddabetta is the highest peak in the Nilgiri Hills. Hence, option A is correct.",
        "प्रायद्वीपीय भारत (तथा पश्चिमी घाट) की सबसे ऊंची पर्वत चोटी कौन-सी है?",
        ["अनाईमुडी (2,695 मीटर)", "दोड्डाबेट्टा (2,637 मीटर)", "गुरु शिखर (1,722 मीटर)", "महेंद्रगिरि (1,501 मीटर)"],
        "केरल की अनामलाई पहाड़ियों में स्थित 'अनाईमुडी' (2,695 मी.) प्रायद्वीपीय भारत तथा दक्षिण भारत की सर्वोच्च चोटी है। दोड्डाबेट्टा नीलगिरि की सबसे ऊंची चोटी है। अतः विकल्प A सही है।"
    ))
    # Q128
    qs.append(create_q(
        128, "General Science & Biology", "Easy", "D",
        "The double-helix molecular structure of Deoxyribonucleic Acid (DNA) was famously elucidated in 1953 by:",
        ["Gregor Mendel and Charles Darwin", "Louis Pasteur and Robert Koch", "Alexander Fleming and Howard Florey", "James Watson and Francis Crick"],
        "In 1953, James Watson and Francis Crick proposed the double-helix model of DNA, utilizing X-ray diffraction images taken by Rosalind Franklin and Maurice Wilkins. Watson, Crick, and Wilkins shared the Nobel Prize in 1962. Hence, option D is correct.",
        "1953 में डीएनए (DNA) की द्विकुंडलिनी (Double Helix) आणविक संरचना की खोज किसने की थी?",
        ["ग्रेगर मेंडल और चार्ल्स डार्विन", "लुई पाश्चर और रॉबर्ट कोच", "अलेक्जेंडर फ्लेमिंग और हॉवर्ड फ्लोरी", "जेम्स वाटसन और फ्रांसिस क्रिक"],
        "जेम्स वाटसन और फ्रांसिस क्रिक ने 1953 में डीएनए की डबल हेलिक्स संरचना का मॉडल प्रस्तुत किया था, जिसके लिए उन्हें 1962 में नोबेल पुरस्कार प्रदान किया गया। अतः विकल्प D सही है।"
    ))
    # Q129
    qs.append(create_q(
        129, "Modern Indian History", "Easy", "C",
        "The British East India Company under Major Hector Munro decisively defeated the joint armies of Mir Qasim, Shuja-ud-Daula, and Mughal Emperor Shah Alam II at the Battle of:",
        ["Plassey (1757)", "Wandiwash (1760)", "Buxar (22 October 1764)", "Panipat (1761)"],
        "On 22 October 1764, the Battle of Buxar was fought between the British army led by Hector Munro and the combined forces of Mir Qasim (deposed Nawab of Bengal), Shuja-ud-Daula (Nawab of Awadh), and Shah Alam II. British victory led to the Treaty of Allahabad (1765) granting Diwani rights of Bengal, Bihar, and Orissa. Hence, option C is correct.",
        "22 अक्टूबर 1764 को मेजर हेक्टर मुनरो के नेतृत्व में ब्रिटिश सेना ने मीर कासिम, शुजाउद्दौला और मुगल सम्राट शाहआलम द्वितीय की संयुक्त सेना को किस ऐतिहासिक युद्ध में निर्णायक रूप से पराजित किया था?",
        ["प्लासी का युद्ध (1757)", "वांडीवाश का युद्ध (1760)", "बक्सर का युद्ध (1764)", "पानीपत का तीसरा युद्ध (1761)"],
        "बक्सर के युद्ध (1764) में अंग्रेजों की जीत ने भारत में ब्रिटिश औपनिवेशिक सत्ता की वास्तविक नींव रखी, जिसके परिणामस्वरूप 1765 की इलाहाबाद संधि द्वारा अंग्रेजों को बंगाल, बिहार और उड़ीसा की दीवानी मिली। अतः विकल्प C सही है।"
    ))
    # Q130
    qs.append(create_q(
        130, "Indian Polity", "Medium", "B",
        "Under Article 263 of the Constitution of India, who is empowered to establish an Inter-State Council to coordinate policy between the Union and the States?",
        ["The Parliament by law", "The President of India", "The Chief Justice of India", "The NITI Aayog Governing Council"],
        "Under Article 263, if it appears to the President that public interests would be served by establishing an Inter-State Council, the President may by order establish such a council. It was first set up in 1990 on the recommendation of the Sarkaria Commission. Hence, option B is correct.",
        "भारतीय संविधान के अनुच्छेद 263 के तहत केंद्र और राज्यों के बीच समन्वय स्थापित करने हेतु 'अंतर-राज्यीय परिषद' (Inter-State Council) का गठन किसके द्वारा किया जाता है?",
        ["संसद द्वारा विधि बनाकर", "भारत के राष्ट्रपति द्वारा", "सर्वोच्च न्यायालय के मुख्य न्यायाधीश द्वारा", "नीति आयोग द्वारा"],
        "अनुच्छेद 263 के अंतर्गत राष्ट्रपति को लोकहित में अंतर-राज्यीय परिषद का गठन करने का अधिकार है। सरकारिया आयोग की सिफारिश पर 1990 में राष्ट्रपति के आदेश द्वारा इसका प्रथम बार गठन किया गया था। अतः विकल्प B सही है।"
    ))
    # Q131
    qs.append(create_q(
        131, "Environment & Ecology", "Easy", "A",
        "The United Nations Convention on Biological Diversity (CBD) was opened for signature in 1992 at the:",
        ["Rio Earth Summit (UNCED, Rio de Janeiro)", "Stockholm Conference (1972)", "Kyoto Conference (1997)", "Johannesburg Summit (2002)"],
        "The Convention on Biological Diversity (CBD) was opened for signature at the UN Conference on Environment and Development (Earth Summit) in Rio de Janeiro, Brazil in June 1992, entering into force in December 1993. Hence, option A is correct.",
        "संयुक्त राष्ट्र 'जैव विविधता अभिसमय' (CBD) पर किस ऐतिहासिक पर्यावरण सम्मेलन में हस्ताक्षर किए गए थे?",
        ["रियो पृथ्वी शिखर सम्मेलन 1992 (रियो डी जेनेरियो, ब्राजील)", "स्टॉकहोम सम्मेलन 1972", "क्योटो सम्मेलन 1997", "जोहान्सबर्ग सम्मेलन 2002"],
        "1992 में ब्राजील के रियो डी जेनेरियो में आयोजित ऐतिहासिक पृथ्वी शिखर सम्मेलन (Earth Summit) में जैव विविधता सम्मेलन (CBD) को अंगीकार किया गया था। अतः विकल्प A सही है।"
    ))
    # Q132
    qs.append(create_q(
        132, "Ancient Indian History", "Easy", "D",
        "The celebrated astronomer-mathematician Varahamihira and the great poet Kalidasa adorned the royal court (Navratnas) of which Gupta ruler?",
        ["Samudragupta", "Kumaragupta I", "Skandagupta", "Chandragupta II 'Vikramaditya'"],
        "Chandragupta II Vikramaditya (reigned c. 375–415 CE) patronized the famous 'Navratnas' (Nine Gems) in his court at Ujjain, which included Kalidasa, Varahamihira, Amarasimha, Dhanvantari, and Sanku. Hence, option D is correct.",
        "प्रसिद्ध खगोलविद् वराहमिहिर और महाकवि कालिदास किस गुप्त सम्राट के नवरत्नों (दरबारी विद्वानों) में शामिल थे?",
        ["समुद्रगुप्त", "कुमारगुप्त प्रथम", "स्कंदगुप्त", "चंद्रगुप्त द्वितीय 'विक्रमादित्य'"],
        "चंद्रगुप्त द्वितीय 'विक्रमादित्य' के उज्जैन स्थित दरबार में नवरत्न सुशोभित थे जिनमें कालिदास, वराहमिहिर, अमरसिंह, धन्वंतरि आदि महान विद्वान शामिल थे। अतः विकल्प D सही है।"
    ))
    # Q133
    qs.append(create_q(
        133, "Indian Economy & Rural Development", "Easy", "C",
        "The National Bank for Agriculture and Rural Development (NABARD) was established on 12 July 1982 on the recommendations of which committee?",
        ["Narasimham Committee", "Rangarajan Committee", "B. Sivaraman Committee (CRAFICARD)", "Gadgil Committee"],
        "NABARD was established on July 12, 1982 under Act 61 of 1981 based on the recommendations of the Committee to Review Arrangements for Institutional Credit for Agriculture and Rural Development (CRAFICARD) headed by B. Sivaraman. Hence, option C is correct.",
        "राष्ट्रीय कृषि और ग्रामीण विकास बैंक (NABARD) की स्थापना 12 जुलाई 1982 को किस समिति की संस्तुतियों पर की गई थी?",
        ["नरसिम्हम समिति", "रंगराजन समिति", "बी. शिवरामन समिति (CRAFICARD)", "गाडगिल समिति"],
        "बी. शिवरामन की अध्यक्षता वाली समिति (CRAFICARD) की सिफारिशों पर 12 जुलाई 1982 को ग्रामीण ऋण और कृषि विकास की शीर्ष संस्था नाबार्ड (NABARD) की स्थापना की गई थी। अतः विकल्प C सही है।"
    ))
    # Q134
    qs.append(create_q(
        134, "World Geography", "Easy", "B",
        "Which high-altitude mountain junction in Central Asia is globally renowned as the 'Roof of the World' (Bam-i-Dunya)?",
        ["Tibetan Plateau", "Pamir Knot (Pamir Mountains)", "Altai Mountains", "Zagros Mountains"],
        "The Pamir Knot is a major orographic knot where the Himalayas, Tian Shan, Karakoram, Kunlun, and Hindu Kush ranges converge, traditionally called the 'Roof of the World'. Hence, option B is correct.",
        "मध्य एशिया में स्थित किस उच्च पर्वतीय ग्रंथि को 'विश्व की छत' (Roof of the World) कहा जाता है?",
        ["तिब्बत का पठार", "पामीर की गांठ (पामीर पर्वतमाला)", "अल्ताई पर्वत", "जाग्रोस पर्वत"],
        "पामीर की गांठ (Pamir Knot) जहाँ से हिमालय, काराकोरम, कुनलुन, हिंदूकुश और तियान शान पर्वत श्रेणियां निकलती हैं, को 'विश्व की छत' कहा जाता है। अतः विकल्प B सही है।"
    ))
    # Q135
    qs.append(create_q(
        135, "General Science & Nuclear Physics", "Easy", "A",
        "What is 'Heavy Water' used as a neutron moderator and coolant in pressurized heavy-water nuclear reactors (PHWR)?",
        ["Deuterium oxide (D2O)", "Hydrogen peroxide (H2O2)", "Tritium oxide (T2O)", "Hard water with calcium bicarbonates"],
        "Heavy water is water enriched in the hydrogen isotope deuterium (2H or D), giving the chemical formula D2O. Its low neutron absorption cross-section makes it an ideal moderator for natural uranium reactors. Hence, option A is correct.",
        "परमाणु रिएक्टरों में न्यूट्रॉन मंदक और शीतलक के रूप में प्रयुक्त होने वाला 'भारी जल' (Heavy Water) रासायनिक रूप से क्या है?",
        ["ड्यूटेरियम ऑक्साइड (D2O)", "हाइड्रोजन पेरोक्साइड (H2O2)", "ट्रिटियम ऑक्साइड (T2O)", "कैल्शियम युक्त कठोर जल"],
        "भारी जल हाइड्रोजन के समस्थानिक ड्यूटेरियम का ऑक्साइड (D2O) होता है, जिसका उपयोग परमाणु भट्टियों में न्यूट्रॉनों की गति को धीमा (मंदक) करने के लिए किया जाता है। अतः विकल्प A सही है।"
    ))
    # Q136
    qs.append(create_q(
        136, "Modern Indian History", "Easy", "D",
        "The 'Morley-Minto Reforms' embodied in the Indian Councils Act of 1909 are infamous in Indian constitutional history for introducing:",
        ["Dyarchy in the provinces", "Federal court in Delhi", "Bicameral legislature at Centre", "Separate communal electorates for Muslims"],
        "The Indian Councils Act, 1909 (Morley-Minto Reforms) introduced communal representation by granting separate electorates for Muslims, where Muslim members were elected exclusively by Muslim voters, seeding communal division. Hence, option D is correct.",
        "1909 के भारतीय परिषद अधिनियम ('मार्ले-मिंटो सुधार') ने भारतीय शासन व्यवस्था में किस विवादास्पद प्रणाली की शुरुआत की थी?",
        ["प्रांतों में द्वैध शासन", "संघीय न्यायालय की स्थापना", "केंद्र में द्विसदनीय विधायिका", "मुसलमानों के लिए पृथक सांप्रदायिक निर्वाचन प्रणाली"],
        "मार्ले-मिंटो सुधार 1909 द्वारा भारत में पहली बार धर्म के आधार पर पृथक निर्वाचन क्षेत्र (सांप्रदायिक प्रतिनिधित्व) की व्यवस्था की गई। लॉर्ड मिंटो को 'सांप्रदायिक निर्वाचन का जनक' कहा जाता है। अतः विकल्प D सही है।"
    ))
    # Q137
    qs.append(create_q(
        137, "Indian Polity", "Easy", "C",
        "Under Article 360 of the Constitution of India, how many times has a 'Financial Emergency' been declared in India since independence?",
        ["Twice (1962 and 1971)", "Once (during the 1991 Balance of Payments crisis)", "Never (Zero times)", "Three times"],
        "Article 360 empowers the President to proclaim a Financial Emergency if the financial stability or credit of India is threatened. Thankfully, a Financial Emergency has never been declared in India so far. Hence, option C is correct.",
        "भारतीय संविधान के अनुच्छेद 360 के अंतर्गत स्वतंत्रता के बाद से अब तक भारत में कितनी बार 'वित्तीय आपातकाल' की घोषणा की गई है?",
        ["दो बार (1962 और 1971 में)", "एक बार (1991 के आर्थिक संकट में)", "कभी नहीं (एक बार भी नहीं)", "तीन बार"],
        "अनुच्छेद 360 के तहत वित्तीय आपातकाल की घोषणा भारत में आज तक कभी नहीं की गई है। अतः विकल्प C सही उत्तर है।"
    ))
    # Q138
    qs.append(create_q(
        138, "Environment & Ecology", "Medium", "B",
        "The 'Basel Convention' (adopted in 1989 and effective in 1992) is an international treaty primarily aimed at controlling the:",
        ["Emissions of greenhouse gases", "Transboundary movements and disposal of hazardous wastes", "Poaching of endangered species", "Oceanic radioactive contamination"],
        "The Basel Convention on the Control of Transboundary Movements of Hazardous Wastes and Their Disposal aims to protect human health and the environment against the adverse effects of hazardous wastes, preventing the dumping of toxic wastes by rich countries in developing nations. Hence, option B is correct.",
        "1989 में अंगीकार किया गया 'बेसल अभिसमय' (Basel Convention) मुख्य रूप से किससे संबंधित एक अंतर्राष्ट्रीय समझौता है?",
        ["ग्रीनहाउस गैसों का उत्सर्जन नियंत्रण", "खतरनाक अपशिष्टों के सीमा-पार आवागमन और उनके सुरक्षित निपटान पर नियंत्रण", "लुप्तप्राय प्रजातियों का अवैध शिकार", "समुद्री रेडियोधर्मी प्रदूषण"],
        "बेसल कन्वेंशन का मुख्य उद्देश्य विकसित देशों द्वारा विकासशील देशों में खतरनाक व विषैले अपशिष्टों के डंपिंग और सीमा-पार अवैध व्यापार को रोकना तथा विनियमित करना है। अतः विकल्प B सही है।"
    ))
    # Q139
    qs.append(create_q(
        139, "Medieval Indian History & Architecture", "Easy", "A",
        "The colossal gateway 'Buland Darwaza' (Door of Victory) at Fatehpur Sikri was constructed by Emperor Akbar in 1601 to commemorate his victory over:",
        ["Gujarat", "Kashmir", "Bengal", "Deccan (Ahmednagar)"],
        "Emperor Akbar built the 54-meter-high Buland Darwaza (the highest gateway in the world) at Fatehpur Sikri in 1601 CE to celebrate and commemorate his conquest of Gujarat in 1573. Hence, option A is correct.",
        "फतेहपुर सीकरी में स्थित भव्य 'बुलंद दरवाजा' का निर्माण मुगल सम्राट अकबर ने 1601 में किस विजय की स्मृति में करवाया था?",
        ["गुजरात विजय", "कश्मीर विजय", "बंगाल विजय", "दक्कन विजय"],
        "अकबर ने गुजरात विजय की ऐतिहासिक स्मृति को चिरस्थायी बनाने के लिए फतेहपुर सीकरी में जामा मस्जिद के दक्षिणी प्रवेश द्वार पर विशाल 'बुलंद दरवाजा' बनवाया था। अतः विकल्प A सही है।"
    ))
    # Q140
    qs.append(create_q(
        140, "Indian Economy & Schemes", "Easy", "D",
        "The flagship scheme 'Pradhan Mantri Awas Yojana' (PMAY - Urban and Gramin) was launched with the primary mission of:",
        ["Free electricity connections to all rural homes", "Clean LPG connections to women below poverty line", "Tap water connection to every household", "Housing for All (pucca houses with basic amenities)"],
        "PMAY was launched in June 2015 with the objective of providing 'Housing for All' by constructing pucca houses with water, sanitation, and electricity for eligible urban and rural poor families. Hence, option D is correct.",
        "केंद्र सरकार की 'प्रधानमंत्री आवास योजना' (PMAY) का प्राथमिक उद्देश्य क्या है?",
        ["सभी ग्रामीण घरों को मुफ्त बिजली कनेक्शन", "गरीबी रेखा से नीचे की महिलाओं को मुफ्त रसोई गैस", "प्रत्येक घर में नल से स्वच्छ जल", "'सबके लिए आवास' (पात्र परिवारों को पक्के मकान उपलब्ध कराना)"],
        "प्रधानमंत्री आवास योजना का मुख्य उद्देश्य देश के बेघर और कच्चे/जीर्ण-शीर्ण मकानों में रहने वाले पात्र परिवारों को सभी बुनियादी सुविधाओं से युक्त पक्के आवास उपलब्ध कराना है। अतः विकल्प D सही है।"
    ))
    # Q141
    qs.append(create_q(
        141, "World Geography", "Easy", "C",
        "Which of the following is the world's deepest and oldest freshwater lake, containing roughly 20% of the world's unfrozen surface freshwater, located in Russia?",
        ["Lake Superior", "Lake Victoria", "Lake Baikal", "Lake Tanganyika"],
        "Lake Baikal in southern Siberia, Russia, has a maximum depth of 1,642 meters (5,387 ft), making it the world's deepest and most voluminous freshwater lake. Hence, option C is correct.",
        "विश्व की सबसे गहरी और सबसे प्राचीन मीठे पानी की झील कौन-सी है जो रूस के साइबेरिया में स्थित है?",
        ["सुपीरियर झील", "विक्टोरिया झील", "बैकाल झील (Lake Baikal)", "तांगानिका झील"],
        "रूस में स्थित बैकाल झील विश्व की सबसे गहरी (लगभग 1,642 मीटर) और आयतन की दृष्टि से सबसे विशाल मीठे पानी की झील है। अतः विकल्प C सही है।"
    ))
    # Q142
    qs.append(create_q(
        142, "General Science & Physics", "Easy", "B",
        "Through which of the following media is the propagation speed of sound waves MAXIMUM?",
        ["Air (gaseous state)", "Steel / Iron (solid state)", "Water (liquid state)", "Vacuum"],
        "Sound waves are mechanical longitudinal waves requiring an elastic medium. Speed of sound depends directly on the elasticity and density of the medium: Solids > Liquids > Gases (and 0 in vacuum). In steel, speed of sound is ~5,100 m/s compared to ~1,500 m/s in water and ~343 m/s in air. Hence, option B is correct.",
        "निम्नलिखित में से किस माध्यम में ध्वनि की चाल (गति) सर्वाधिक होती है?",
        ["वायु में (गैसीय अवस्था)", "स्टील / लोहा में (ठोस अवस्था)", "जल में (द्रव अवस्था)", "निर्वात में"],
        "ध्वनि एक यांत्रिक तरंग है जिसकी चाल माध्यम की प्रत्यास्थता पर निर्भर करती है। ध्वनि की चाल ठोस में सर्वाधिक (स्टील में लगभग 5100 मी./से.), फिर द्रव में और सबसे कम गैस में होती है (निर्वात में शून्य)। अतः विकल्प B सही है।"
    ))
    # Q143
    qs.append(create_q(
        143, "Modern Indian History", "Easy", "A",
        "Who among the following was NOT a member of the three-man British 'Cabinet Mission' that arrived in India in March 1946?",
        ["Lord Mountbatten", "Lord Pethick-Lawrence", "Sir Stafford Cripps", "A.V. Alexander"],
        "The Cabinet Mission sent by Prime Minister Clement Attlee in 1946 consisted of three British cabinet ministers: Lord Pethick-Lawrence (Secretary of State for India), Sir Stafford Cripps (President of Board of Trade), and A.V. Alexander (First Lord of Admiralty). Lord Mountbatten arrived later in 1947 as Viceroy. Hence, option A is correct.",
        "मार्च 1946 में भारत आए तीन सदस्यीय ब्रिटिश 'कैबिनेट मिशन' के सदस्यों में निम्नलिखित में से कौन शामिल नहीं था?",
        ["लॉर्ड माउंटबेटन", "लॉर्ड पैथिक-लॉरेंस", "सर स्टेफोर्ड क्रिप्स", "ए.वी. अलेक्जेंडर"],
        "कैबिनेट मिशन 1946 में तीन कैबिनेट मंत्री शामिल थे: पैथिक-लॉरेंस (भारत सचिव), स्टेफोर्ड क्रिप्स तथा ए.वी. अलेक्जेंडर। लॉर्ड माउंटबेटन 1947 में अंतिम वायसराय बनकर आए थे। अतः विकल्प A सही है।"
    ))
    # Q144
    qs.append(create_q(
        144, "Indian Polity", "Medium", "D",
        "Under Article 226 of the Constitution of India, High Courts are empowered to issue prerogative writs for the enforcement of:",
        ["Fundamental Rights only", "Directive Principles of State Policy", "Statutory rules only", "Fundamental Rights as well as any other legal rights"],
        "While the Supreme Court's writ jurisdiction under Article 32 is restricted solely to the enforcement of Fundamental Rights, the High Court's writ jurisdiction under Article 226 extends to Fundamental Rights as well as 'for any other purpose' (legal rights), giving High Courts wider writ powers. Hence, option D is correct.",
        "भारतीय संविधान के अनुच्छेद 226 के अंतर्गत उच्च न्यायालय (High Court) किसके प्रवर्तन के लिए रिट (Writs) जारी करने की शक्ति रखते हैं?",
        ["केवल मौलिक अधिकारों के लिए", "राज्य के नीति निर्देशक तत्वों के लिए", "केवल वैधानिक नियमों के लिए", "मौलिक अधिकारों के साथ-साथ अन्य कानूनी/विधिक अधिकारों के लिए भी"],
        "सर्वोच्च न्यायालय अनुच्छेद 32 के तहत केवल मूल अधिकारों के उल्लंघन पर रिट जारी कर सकता है, जबकि उच्च न्यायालय अनुच्छेद 226 के तहत मूल अधिकारों के साथ-साथ अन्य विधिक अधिकारों के संरक्षण के लिए भी रिट जारी कर सकता है। अतः विकल्प D सही है।"
    ))
    # Q145
    qs.append(create_q(
        145, "Environment & Law", "Easy", "C",
        "In which year was the comprehensive 'Wildlife (Protection) Act' enacted by the Parliament of India to protect wild animals, birds, and plants?",
        ["1968", "1970", "1972", "1980"],
        "The Wildlife (Protection) Act, 1972 is the foundational environmental statute providing legal protection to wild fauna and flora, establishing National Parks and Sanctuaries, and regulating trade in wildlife derivatives. Hence, option C is correct.",
        "भारत की संसद द्वारा वन्यजीवों, पक्षियों और वनस्पतियों के संरक्षण के लिए व्यापक 'वन्यजीव (संरक्षण) अधिनियम' किस वर्ष पारित किया गया था?",
        ["1968", "1970", "1972", "1980"],
        "वन्यजीवों के अवैध शिकार, व्यापार और प्राकृतिक पर्यावासों के संरक्षण हेतु भारत में 'वन्यजीव संरक्षण अधिनियम' 1972 में लागू किया गया था। अतः विकल्प C सही है।"
    ))
    # Q146
    qs.append(create_q(
        146, "Ancient Indian History", "Easy", "B",
        "Megasthenes, the author of the classical account 'Indica', was sent as an ambassador to the court of Chandragupta Maurya by which Hellenistic ruler?",
        ["Alexander the Great", "Seleucus I Nicator", "Antiochus I", "Ptolemy II Philadelphus"],
        "Following the treaty between Chandragupta Maurya and Seleucus I Nicator (c. 303 BCE), Seleucus dispatched Megasthenes as his official envoy to the Mauryan imperial capital Pataliputra, where Megasthenes wrote 'Indica'. Hence, option B is correct.",
        "मौर्य साम्राज्य के विवरण पर आधारित प्रसिद्ध पुस्तक 'इण्डिका' के लेखक मेगस्थनीज को किस यूनानी शासक ने चंद्रगुप्त मौर्य के दरबार में राजदूत बनाकर भेजा था?",
        ["सिकंदर महान", "सेल्युकस प्रथम निकेटर", "एंटीओकस प्रथम", "टॉलमी द्वितीय फिलाडेल्फस"],
        "सेल्युकस निकेटर ने चंद्रगुप्त मौर्य के साथ हुई संधि के उपरांत मेगस्थनीज को पाटलिपुत्र में अपना राजदूत बनाकर भेजा था, जिसने अपनी पुस्तक 'इण्डिका' में मौर्यकालीन समाज और प्रशासन का वर्णन किया। अतः विकल्प B सही है।"
    ))
    # Q147
    qs.append(create_q(
        147, "Indian Economy & Infrastructure", "Easy", "A",
        "The Government of India launched the 'PM Gati Shakti National Master Plan' in October 2021 with the primary objective of:",
        ["Institutional multimodal connectivity infrastructure and seamless logistics across India", "Free skill development training for rural youth", "Direct cash transfer to small scale industries", "Affordable broadband internet to all gram panchayats"],
        "PM Gati Shakti National Master Plan is a ₹100-lakh-crore digital GIS platform synchronizing 16 ministries to plan and execute multi-modal infrastructure connectivity projects, breaking ministerial silos and reducing logistics costs. Hence, option A is correct.",
        "भारत सरकार द्वारा अक्टूबर 2021 में शुरू की गई 'पीएम गति शक्ति राष्ट्रीय मास्टर प्लान' का प्राथमिक उद्देश्य क्या है?",
        ["देश में मल्टी-मॉडल कनेक्टिविटी अवसंरचना और निर्बाध लॉजिस्टिक्स नेटवर्क का एकीकृत विकास", "ग्रामीण युवाओं के लिए निःशुल्क कौशल प्रशिक्षण", "लघु उद्योगों को प्रत्यक्ष नकद अनुदान", "सभी ग्राम पंचायतों को ब्रॉडबैंड इंटरनेट"],
        "पीएम गति शक्ति योजना विभिन्न मंत्रालयों (रेलवे, सड़क, जलमार्ग आदि) को एक डिजिटल प्लेटफॉर्म पर लाकर देश में मल्टी-मॉडल लॉजिस्टिक्स और बुनियादी ढांचे के त्वरित समन्वय का राष्ट्रीय मास्टर प्लान है। अतः विकल्प A सही है।"
    ))
    # Q148
    qs.append(create_q(
        148, "Indian Geography", "Easy", "D",
        "The famous 'Loktak Lake', renowned for its unique floating circular islands of decomposed vegetation called 'Phumdis' and Keibul Lamjao National Park, is situated in:",
        ["Meghalaya", "Mizoram", "Assam", "Manipur"],
        "Loktak Lake in Manipur is the largest freshwater lake in Northeast India, famous for its floating phumdis and the world's only floating national park—Keibul Lamjao, the last refuge of the endangered brow-antlered deer (Sangai). Hence, option D is correct.",
        "तैरते हुए द्वीपों ('फुमडी') और विश्व के एकमात्र तैरते हुए राष्ट्रीय उद्यान (केइबुल लामजाओ) के लिए विख्यात 'लोकटक झील' किस पूर्वोत्तर राज्य में स्थित है?",
        ["मेघालय", "मिजोरम", "असम", "मणिपुर"],
        "लोकटक झील मणिपुर में स्थित पूर्वोत्तर की सबसे बड़ी मीठे पानी की झील है। इसी पर विश्व का एकमात्र तैरता हुआ राष्ट्रीय उद्यान 'केइबुल लामजाओ' स्थित है जो शंघाई हिरण का घर है। अतः विकल्प D सही है।"
    ))
    # Q149
    qs.append(create_q(
        149, "General Science & Chemistry", "Easy", "C",
        "What is 'Dry Ice' commonly used as a commercial cooling refrigerant and special effect fog generator?",
        ["Solid Water Ice at -100°C", "Solid Nitrogen", "Solid Carbon Dioxide (CO2)", "Solid Methane"],
        "Dry ice is the solid state of carbon dioxide (CO2). At atmospheric pressure, it sublimes directly from solid to gaseous carbon dioxide at -78.5°C (-109.3°F) without leaving any liquid residue; hence termed 'dry'. Hence, option C is correct.",
        "शीतलन (रेफ्रिजरेशन) और कृत्रिम धुआं उत्पन्न करने के लिए प्रयुक्त होने वाली 'शुष्क बर्फ' (Dry Ice) रासायनिक रूप से क्या है?",
        ["-100°C पर जमी हुई ठोस बर्फ", "ठोस नाइट्रोजन", "ठोस कार्बन डाइऑक्साइड (Solid CO2)", "ठोस मीथेन"],
        "ठोस कार्बन डाइऑक्साइड को शुष्क बर्फ (Dry Ice) कहा जाता है। यह वायुमंडलीय दाब पर बिना पिघले सीधे गैस में परिवर्तित (उर्ध्वपातन) हो जाती है। अतः विकल्प C सही है।"
    ))
    # Q150
    qs.append(create_q(
        150, "UP Special & Economy", "Easy", "B",
        "The Government of Uttar Pradesh launched the flagship 'One District One Product' (ODOP) scheme in January 2018 with the objective of:",
        ["Promoting crop diversification across UP districts", "Reviving and promoting traditional specialized industrial and artisanal crafts unique to each district", "Providing free solar pumps in every district", "Establishing special economic export processing zones"],
        "The ODOP scheme was pioneered by the Uttar Pradesh government on UP Diwas (24 January 2018) to preserve and promote unique indigenous products, arts, and crafts native to each of the 75 districts of UP (such as Chikankari of Lucknow, Brassware of Moradabad, Perfume of Kannauj, Black Pottery of Azamgarh), later adopted nationwide by the Central Government. Hence, option B is correct.",
        "उत्तर प्रदेश सरकार द्वारा जनवरी 2018 में शुरू की गई 'एक जिला एक उत्पाद' (ODOP) योजना का मुख्य उद्देश्य क्या है?",
        ["जिलेवार फसल विविधीकरण को बढ़ावा देना", "प्रत्येक जिले के विशिष्ट पारंपरिक हस्तशिल्प और देशज कुटीर उद्योगों को पुनर्जीवित एवं प्रोत्साहित करना", "प्रत्येक जिले में मुफ्त सौर पंप उपलब्ध कराना", "विशेष आर्थिक निर्यात प्रसंस्करण क्षेत्र स्थापित करना"],
        "उत्तर प्रदेश दिवस (24 जनवरी 2018) को प्रदेश सरकार द्वारा 'एक जिला एक उत्पाद' (ODOP) योजना शुरू की गई थी, ताकि राज्य के सभी 75 जिलों के विशिष्ट पारंपरिक शिल्पों (जैसे मुरादाबाद का पीतल, कन्नौज का इत्र, आजमगढ़ की काली मिट्टी आदि) को वैश्विक पहचान मिल सके। अतः विकल्प B सही है।"
    ))
    return qs

def main():
    q1_50 = get_questions_1_to_50()
    q51_100 = get_questions_51_to_100()
    q101_150 = get_questions_101_to_150()
    all_qs = q1_50 + q51_100 + q101_150

    assert len(all_qs) == 150, f"Expected 150 questions, got {len(all_qs)}"

    paper_data = {
        "testId": "uppcs_pre_pyq_2022_gs1",
        "categoryId": "uppcs_pre",
        "test_id": "uppcs_pre_pyq_2022_gs1",
        "category_id": "uppcs_pre",
        "title": "UPPSC PCS Prelims 2022 — General Studies Paper 1 (Full 150 Qs)",
        "titleEn": "UPPSC PCS Prelims 2022 — General Studies Paper 1 (Full 150 Qs)",
        "titleHi": "UPPSC PCS प्रारंभिक परीक्षा 2022 — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
        "testType": "PYQ",
        "test_type": "PYQ",
        "isFree": True,
        "is_free": True,
        "durationMinutes": 120,
        "duration_minutes": 120,
        "totalQuestions": 150,
        "total_questions": 150,
        "maxMarks": 200.0,
        "positiveMarks": 1.33,
        "negativeMarks": 0.44,
        "examYear": 2022,
        "shiftBadge": "UPPCS Prelims 2022 • GS-1 (Full 150 Qs)",
        "questions": all_qs,
        "path": "tests/state_psc/uppcs_pre/pyq/uppcs_pre_pyq_2022_gs1.json"
    }

    out_path = os.path.join("tests", "state_psc", "uppcs_pre", "pyq", "uppcs_pre_pyq_2022_gs1.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(paper_data, f, ensure_ascii=False, indent=2)

    print(f"SUCCESS: Generated {out_path} with {len(all_qs)} questions!")

if __name__ == "__main__":
    main()
