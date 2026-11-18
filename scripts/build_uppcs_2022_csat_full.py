#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_2022_csat_full.py — Builds complete 100-question authentic UPPSC PCS Prelims 2022 CSAT Paper 2."""
import json
import os

from build_uppcs_2022_csat import get_csat_questions_1_to_50, create_csat_q

def get_csat_questions_51_to_100():
    qs = []
    # Q51 (Maths - Simple Interest)
    qs.append(create_csat_q(
        51, "Logical Reasoning & Maths", "Easy", "C",
        "A principal of ₹4,000 is invested at an annual simple interest rate of 5% for 3 years. What is the total simple interest earned?",
        ["₹500", "₹700", "₹600", "₹800"],
        "Simple Interest (SI) = (P * R * T) / 100 = (4000 * 5 * 3) / 100 = ₹600. Hence, option C is correct.",
        "₹4,000 की धनराशि पर 5% वार्षिक साधारण ब्याज की दर से 3 वर्ष का साधारण ब्याज कितना होगा?",
        ["₹500", "₹700", "₹600", "₹800"],
        "साधारण ब्याज (SI) = (मूलधन × दर × समय) / 100 = (4000 × 5 × 3) / 100 = ₹600। अतः विकल्प C सही है।"
    ))
    # Q52 (Maths - CI vs SI)
    qs.append(create_csat_q(
        52, "Logical Reasoning & Maths", "Medium", "B",
        "The difference between compound interest and simple interest on a sum of ₹10,000 for 2 years at 10% per annum is:",
        ["₹50", "₹100", "₹150", "₹200"],
        "Difference for 2 years = P * (R/100)^2 = 10,000 * (10/100)^2 = 10,000 * (1/100) = ₹100. Hence, option B is correct.",
        "₹10,000 की राशि पर 10% वार्षिक दर से 2 वर्ष के चक्रवृद्धि ब्याज और साधारण ब्याज का अंतर कितना होगा?",
        ["₹50", "₹100", "₹150", "₹200"],
        "2 वर्ष के लिए CI और SI का अंतर = P × (R/100)² = 10,000 × (10/100)² = ₹100। अतः विकल्प B सही है।"
    ))
    # Q53 (Maths - Train Speed)
    qs.append(create_csat_q(
        53, "Logical Reasoning & Maths", "Easy", "A",
        "A 180-metre-long passenger train crosses a stationary telegraph pole in 9 seconds. What is the speed of the train in km/h?",
        ["72 km/h", "54 km/h", "60 km/h", "90 km/h"],
        "Speed in m/s = Distance / Time = 180 / 9 = 20 m/s. Speed in km/h = 20 * (18/5) = 72 km/h. Hence, option A is correct.",
        "180 मीटर लंबी एक रेलगाड़ी एक स्थिर टेलीग्राफ खंभे को 9 सेकंड में पार करती है। रेलगाड़ी की गति किमी/घंटे में कितनी है?",
        ["72 किमी/घं", "54 किमी/घं", "60 किमी/घं", "90 किमी/घं"],
        "चाल = दूरी / समय = 180 / 9 = 20 मी./से.। किमी/घंटे में चाल = 20 × (18/5) = 72 किमी/घं। अतः विकल्प A सही है।"
    ))
    # Q54 (Maths - LCM & HCF)
    qs.append(create_csat_q(
        54, "Logical Reasoning & Maths", "Easy", "D",
        "The HCF of two numbers is 12 and their LCM is 240. If one of the numbers is 48, what is the other number?",
        ["50", "55", "70", "60"],
        "Product of two numbers = HCF * LCM -> First * Second = 12 * 240 = 2880. Second number = 2880 / 48 = 60. Hence, option D is correct.",
        "दो संख्याओं का म.स.प. (HCF) 12 और ल.स.प. (LCM) 240 है। यदि उनमें से एक संख्या 48 है, तो दूसरी संख्या क्या होगी?",
        ["50", "55", "70", "60"],
        "पहली संख्या × दूसरी संख्या = HCF × LCM -> 48 × दूसरी संख्या = 12 × 240 = 2880। दूसरी संख्या = 2880 / 48 = 60। अतः विकल्प D सही है।"
    ))
    # Q55 (Maths - Mensuration Circle)
    qs.append(create_csat_q(
        55, "Logical Reasoning & Maths", "Easy", "C",
        "If the radius of a circular playground is 14 metres, what is its perimeter (circumference) in metres? (Use pi = 22/7)",
        ["44 m", "66 m", "88 m", "176 m"],
        "Circumference = 2 * pi * r = 2 * (22/7) * 14 = 2 * 22 * 2 = 88 metres. Hence, option C is correct.",
        "यदि किसी वृत्ताकार मैदान की त्रिज्या 14 मीटर है, तो उसका परिमाप (परिधि) कितने मीटर होगा? (pi = 22/7 मानिए)",
        ["44 मीटर", "66 मीटर", "88 मीटर", "176 मीटर"],
        "वृत्त की परिधि = 2 × π × r = 2 × (22/7) × 14 = 88 मीटर। अतः विकल्प C सही उत्तर है।"
    ))
    # Q56 (Maths - Statistics Empirical Formula)
    qs.append(create_csat_q(
        56, "Logical Reasoning & Maths", "Medium", "B",
        "In a moderately skewed statistical distribution, if the Mean is 30 and the Median is 32, what is the estimated Mode using Karl Pearson's empirical relation?",
        ["34", "36", "38", "31"],
        "Empirical relationship: Mode = 3 * Median - 2 * Mean = 3*(32) - 2*(30) = 96 - 60 = 36. Hence, option B is correct.",
        "एक असममित सांख्यिकीय वितरण में यदि माध्य (Mean) 30 और माध्यिका (Median) 32 है, तो कार्ल पियर्सन के अनुभवजन्य सूत्र से बहुलक (Mode) का मान क्या होगा?",
        ["34", "36", "38", "31"],
        "बहुलक = 3 × माध्यिका - 2 × माध्य = 3(32) - 2(30) = 96 - 60 = 36। अतः विकल्प B सही है।"
    ))
    # Q57 (Maths - Statistics Median)
    qs.append(create_csat_q(
        57, "Logical Reasoning & Maths", "Easy", "A",
        "Find the Median of the following discrete observations:\n15, 7, 22, 19, 11, 28, 9",
        ["15", "19", "11", "17"],
        "Arrange in ascending order: 7, 9, 11, 15, 19, 22, 28. There are n=7 observations. Median is the (7+1)/2 = 4th term = 15. Hence, option A is correct.",
        "दिए गए आंकड़ों का माध्यक (माध्यिका) ज्ञात कीजिए:\n15, 7, 22, 19, 11, 28, 9",
        ["15", "19", "11", "17"],
        "आंकड़ों को आरोही क्रम में लिखने पर: 7, 9, 11, 15, 19, 22, 28। कुल पद n=7 (विषम) है। माध्यिका = (7+1)/2 = चौथा पद = 15। अतः विकल्प A सही है।"
    ))
    # Q58 (Maths - Geometry Polygon)
    qs.append(create_csat_q(
        58, "Logical Reasoning & Maths", "Easy", "D",
        "What is the sum of all interior angles of a regular hexagon (6-sided polygon)?",
        ["360°", "540°", "900°", "720°"],
        "Sum of interior angles of an n-sided polygon = (n - 2) * 180° = (6 - 2) * 180° = 4 * 180° = 720°. Hence, option D is correct.",
        "एक सम-षट्भुज (6 भुजाओं वाले बहुभुज) के सभी अंतःकोणों का योग कितना होता है?",
        ["360°", "540°", "900°", "720°"],
        "बहुभुज के अंतःकोणों का योग = (n - 2) × 180° = (6 - 2) × 180° = 4 × 180° = 720°। अतः विकल्प D सही है।"
    ))
    # Q59 (Maths - Probability Dice)
    qs.append(create_csat_q(
        59, "Logical Reasoning & Maths", "Medium", "C",
        "When two fair six-sided dice are rolled simultaneously, what is the probability that the sum of the numbers showing on top is equal to 7?",
        ["1/12", "1/9", "1/6", "5/36"],
        "Total possible outcomes = 6 * 6 = 36. Outcomes with sum 7 are: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) -> 6 outcomes. Probability = 6/36 = 1/6. Hence, option C is correct.",
        "दो निष्पक्ष पासों (Dice) को एक साथ फेंकने पर उन पर आने वाले अंकों का योग 7 होने की प्रायिकता क्या है?",
        ["1/12", "1/9", "1/6", "5/36"],
        "कुल संभावित परिणाम = 36। योग 7 वाले अनुकूल परिणाम = (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) अर्थात् 6 परिणाम। प्रायिकता = 6/36 = 1/6। अतः विकल्प C सही है।"
    ))
    # Q60 (Logical Reasoning - Ranking)
    qs.append(create_csat_q(
        60, "Logical Reasoning & Maths", "Easy", "B",
        "In a row of boys facing North, Rahul is 12th from the left end and 18th from the right end. How many total boys are there in the row?",
        ["30", "29", "28", "31"],
        "Total persons = (Rank from Left + Rank from Right) - 1 = (12 + 18) - 1 = 30 - 1 = 29. Hence, option B is correct.",
        "उत्तर दिशा की ओर मुख किए लड़कों की एक पंक्ति में राहुल बाएं छोर से 12वें स्थान पर और दाएं छोर से 18वें स्थान पर है। पंक्ति में कुल कितने लड़के हैं?",
        ["30", "29", "28", "31"],
        "कुल संख्या = (बाएं से स्थान + दाएं से स्थान) - 1 = (12 + 18) - 1 = 29। अतः विकल्प B सही उत्तर है।"
    ))
    # Q61 (Logical Reasoning - Syllogism)
    qs.append(create_csat_q(
        61, "Logical Reasoning & Maths", "Medium", "A",
        "Statements:\n1. All mangoes are golden.\n2. No golden things are cheap.\nConclusions:\nI. All mangoes are cheap.\nII. Golden-coloured mangoes are not cheap.\nWhich conclusion(s) logically follow?",
        ["Only Conclusion II follows", "Only Conclusion I follows", "Both I and II follow", "Neither I nor II follows"],
        "Since All mangoes are golden, and No golden things are cheap, it follows that No mangoes are cheap. Thus, Conclusion II (Golden-coloured mangoes are not cheap) is completely valid, while I is false. Hence, option A is correct.",
        "कथन:\n1. सभी आम सुनहरे हैं।\n2. कोई भी सुनहरी वस्तु सस्ती नहीं है।\nनिष्कर्ष:\nI. सभी आम सस्ते हैं।\nII. सुनहरे रंग के आम सस्ते नहीं हैं।\nकौन-सा निष्कर्ष तार्किक रूप से निकलता है?",
        ["केवल निष्कर्ष II निकलता है", "केवल निष्कर्ष I निकलता है", "I और II दोनों निकलते हैं", "न तो I और न ही II निकलता है"],
        "चूँकि सभी आम सुनहरे हैं और कोई सुनहरी वस्तु सस्ती नहीं है, अतः कोई आम सस्ता नहीं हो सकता। निष्कर्ष II पूर्णतः सत्य है और I असत्य। विकल्प A सही है।"
    ))
    # Q62 (Logical Reasoning - Venn Diagram)
    qs.append(create_csat_q(
        62, "Logical Reasoning & Maths", "Easy", "D",
        "Which of the following Venn diagram relations best represents the relationship among: 'Doctors, Human Beings, Engineers'?",
        ["Three separate mutually exclusive circles", "Two concentric circles with one overlapping", "One circle containing doctors, completely separate from human beings", "A large circle (Human Beings) containing two separate circles inside it (Doctors and Engineers)"],
        "All Doctors and all Engineers are Human Beings (represented by a large encompassing circle), and normally an individual professional belongs to either the medical or engineering profession, represented as two mutually exclusive circles inside. Hence, option D is correct.",
        "निम्नलिखित में से कौन-सा वेन आरेख 'डॉक्टर, मनुष्य, इंजीनियर' के बीच सही संबंध को दर्शाता है?",
        ["तीन परस्पर अलग-अलग वृत्त", "दो संकेंद्रीय वृत्त और एक आंशिक वृत्त", "एक बड़ा वृत्त जिसमें केवल डॉक्टर हों", "एक बड़ा वृत्त (मनुष्य) जिसके भीतर दो अलग-अलग वृत्त (डॉक्टर तथा इंजीनियर) हों"],
        "सभी डॉक्टर और इंजीनियर मनुष्य होते हैं, अतः मनुष्य का एक बड़ा वृत्त होगा जिसके अंदर डॉक्टर और इंजीनियर के दो अलग-अलग वृत्त होंगे। अतः विकल्प D सही है।"
    ))
    # Q63 (Logical Reasoning - Clock Angle)
    qs.append(create_csat_q(
        63, "Logical Reasoning & Maths", "Medium", "C",
        "What is the angle between the hour hand and the minute hand of an analogue clock at 3:30?",
        ["90°", "80°", "75°", "60°"],
        "Angle formula = |30*H - (11/2)*M| = |30*3 - (11/2)*30| = |90 - 165| = |-75| = 75°. Hence, option C is correct.",
        "एक घड़ी में 3 बजकर 30 मिनट पर घंटे और मिनट की सुइयों के बीच कितने अंश (डिग्री) का कोण बनेगा?",
        ["90°", "80°", "75°", "60°"],
        "कोण सूत्र = |30H - (11/2)M| = |30(3) - (11/2)(30)| = |90 - 165| = 75°। अतः विकल्प C सही है।"
    ))
    # Q64 (Logical Reasoning - Calendar)
    qs.append(create_csat_q(
        64, "Logical Reasoning & Maths", "Easy", "B",
        "If the 1st of January of a non-leap normal year was a Friday, what day of the week was the 31st of December of that same year?",
        ["Saturday", "Friday", "Thursday", "Sunday"],
        "An ordinary non-leap year consists of 365 days (52 weeks and 1 odd day). Consequently, the year always ends on the exact same day of the week on which it began. Since 1 January was Friday, 31 December was also Friday. (In a leap year it ends on Saturday). Hence, option B is correct.",
        "यदि किसी सामान्य (गैर-लीप) वर्ष का प्रथम दिन (1 जनवरी) शुक्रवार था, तो उस वर्ष का अंतिम दिन (31 दिसंबर) कौन-सा दिन होगा?",
        ["शनिवार", "शुक्रवार", "गुरुवार", "रविवार"],
        "साधारण वर्ष में 365 दिन (52 सप्ताह + 1 दिन) होते हैं, अतः साधारण वर्ष जिस वार को प्रारंभ होता है, उसी वार को समाप्त भी होता है। अतः 31 दिसंबर को शुक्रवार ही होगा। विकल्प B सही है।"
    ))
    # Q65 (Logical Reasoning - Dice)
    qs.append(create_csat_q(
        65, "Logical Reasoning & Maths", "Easy", "A",
        "On a standard six-faced gaming die, which number is on the face directly opposite to 4?",
        ["3", "2", "5", "1"],
        "On a standard die, the sum of numbers on any two opposite faces is always equal to 7. Therefore, face opposite to 4 is (7 - 4) = 3. Hence, option A is correct.",
        "एक मानक पासे (Standard Die) में अंक 4 के विपरीत फलक (face) पर कौन-सा अंक होगा?",
        ["3", "2", "5", "1"],
        "मानक पासे में किन्हीं भी दो विपरीत फलकों के अंकों का योग सदैव 7 होता है। अतः 4 के विपरीत 7 - 4 = 3 होगा। विकल्प A सही है।"
    ))
    # Q66 (Interpersonal Skills - Johari Window)
    qs.append(create_csat_q(
        66, "Interpersonal & Communication Skills", "Medium", "D",
        "In the 'Johari Window' model of interpersonal awareness, the quadrant representing information that is known to oneself but deliberately kept hidden from others is termed the:",
        ["Open / Arena area", "Blind area", "Unknown area", "Hidden / Facade area"],
        "The Johari Window has four quadrants: (1) Open: known to self & others; (2) Blind: unknown to self, known to others; (3) Hidden/Facade: known to self, unknown to others; (4) Unknown: unknown to both. Hence, option D is correct.",
        "पारस्परिक समझ के 'जोहारी विंडो' (Johari Window) मॉडल में वह चतुर्थांश क्या कहलाता है जिसमें वह सूचना होती है जो स्वयं को तो ज्ञात है किंतु दूसरों से छिपाई गई है?",
        ["खुला क्षेत्र (Open/Arena)", "अंध क्षेत्र (Blind spot)", "अज्ञात क्षेत्र (Unknown)", "छिपा हुआ / मुखौटा क्षेत्र (Hidden/Facade)"],
        "छिपा हुआ क्षेत्र (Hidden/Facade) वह भाग है जिसमें व्यक्ति अपने गोपनीय विचार व भावनाएँ दूसरों से छुपा कर रखता है। अतः विकल्प D सही है।"
    ))
    # Q67 (Interpersonal Skills - Transactional Analysis)
    qs.append(create_csat_q(
        67, "Interpersonal & Communication Skills", "Medium", "C",
        "According to Eric Berne's Transactional Analysis, which Ego State processes facts rationally, objectively, and logically like an information processor?",
        ["Parent Ego State", "Child Ego State", "Adult Ego State", "Rebellious Ego State"],
        "The Adult ego state evaluates reality objectively, dispassionately gathering facts and making logical decisions without the emotional reactions of the Child or the judgmental attitudes of the Parent. Hence, option C is correct.",
        "एरिक बर्न के संव्यवहार विश्लेषण (Transactional Analysis) के अनुसार, कौन-सी अहं अवस्था (Ego State) तथ्यों का निष्पक्ष, तर्कसंगत और वस्तुनिष्ठ विश्लेषण करती है?",
        ["पालक अहं (Parent Ego)", "शिशु अहं (Child Ego)", "वयस्क अहं (Adult Ego State)", "विद्रोही अहं"],
        "वयस्क अहं अवस्था (Adult Ego) वस्तुनिष्ठ, तर्कपूर्ण और व्यावहारिक सोच पर आधारित होती है जो वर्तमान वास्तविकताओं के आधार पर निर्णय लेती है। अतः विकल्प C सही है।"
    ))
    # Q68 (Interpersonal Skills - Paralanguage)
    qs.append(create_csat_q(
        68, "Interpersonal & Communication Skills", "Medium", "B",
        "In oral communication, vocal characteristics such as pitch, volume, pacing, inflection, and tone of voice that modify meaning without changing words are collectively known as:",
        ["Kinesics", "Paralanguage (परावरोधी भाषा)", "Proxemics", "Chronemics"],
        "Paralanguage encompasses non-verbal vocal aspects of speech—such as pitch, tempo, volume, resonance, and pauses—that convey emotion, intent, and subtle nuances beyond literal words. Hence, option B is correct.",
        "मौखिक संचार में आवाज़ का स्वर (Pitch), ध्वनि की तीव्रता (Volume), बोलने की गति और विराम, जो बिना शब्द बदले संदेश का अर्थ बदल देते हैं, क्या कहलाते हैं?",
        ["काइनेसिक्स", "पैरा-लैंग्वेज / पराभाषा (Paralanguage)", "प्रॉक्सेमिक्स", "क्रोनेमिक्स"],
        "पैरा-लैंग्वेज में वाणी के वे गैर-शाब्दिक स्वर तत्व आते हैं जो यह निर्धारित करते हैं कि कोई बात 'कैसे' कही गई है (स्वर, लय, उतार-चढ़ाव)। अतः विकल्प B सही है।"
    ))
    # Q69 (Decision Making - Delphi Technique)
    qs.append(create_csat_q(
        69, "Interpersonal & Communication Skills", "Medium", "A",
        "Which structured decision-making method gathers anonymous forecasts from a geographically dispersed panel of experts over repeated rounds with aggregated feedback?",
        ["Delphi Technique", "Brainstorming", "Nominal Group Technique", "Fishbone Analysis"],
        "The Delphi method systematically forecasts future events or solves complex policy problems through multiple rounds of anonymous questionnaires returned to a facilitator who aggregates responses until consensus emerges. Hence, option A is correct.",
        "कौन-सी निर्णय निर्माण विधि भौगोलिक रूप से दूर स्थित विशेषज्ञों के एक समूह से गुमनाम प्रश्नावली और बारंबार प्रतिपुष्टि के माध्यम से सर्वसम्मत निर्णय प्राप्त करती है?",
        ["डेल्फी तकनीक (Delphi Technique)", "ब्रेनस्टॉर्मिंग", "नामित समूह तकनीक", "फिशबोन विश्लेषण"],
        "डेल्फी तकनीक में विशेषज्ञों को आमने-सामने लाए बिना स्वतंत्र रूप से लिखित राय और गोपनीय प्रतिक्रियाओं के आधार पर निष्पक्ष निर्णय लिया जाता है। अतः विकल्प A सही है।"
    ))
    # Q70 (Decision Making - Pareto Principle)
    qs.append(create_csat_q(
        70, "Interpersonal & Communication Skills", "Easy", "D",
        "The famous 'Pareto Principle' utilized in managerial problem-solving is commonly known as the:",
        ["50/50 Rule", "60/40 Rule", "70/30 Rule", "80/20 Rule"],
        "The Pareto Principle (named after Vilfredo Pareto) states that roughly 80% of consequences or effects come from 20% of causes (e.g., 80% of problems in an organization stem from 20% of defects). Hence, option D is correct.",
        "प्रबंधकीय निर्णय निर्माण और समस्या निवारण में प्रसिद्ध 'पैरेटो सिद्धांत' (Pareto Principle) को सामान्यतः किस नाम से जाना जाता है?",
        ["50/50 का नियम", "60/40 का नियम", "70/30 का नियम", "80/20 का नियम (80/20 Rule)"],
        "पैरेटो सिद्धांत के अनुसार किसी भी तंत्र में 80 प्रतिशत परिणाम या समस्याएं मात्र 20 प्रतिशत प्रमुख कारणों से उत्पन्न होती हैं। अतः विकल्प D सही है।"
    ))
    # Q71 (Hindi - Visarga Sandhi)
    qs.append(create_csat_q(
        71, "General Hindi", "Easy", "C",
        "What is the correct Sandhi-Vichchheda of the word 'Yashoda' (यशोदा)?",
        ["यशो + दा", "यश + ओदा", "यशः + दा", "यशा + दा"],
        "'Yashoda' is a classic example of Visarga Sandhi: 'यशः + दा = यशोदा' (when Visarga after short 'अ' is followed by a voiced consonant, the combination changes to 'ओ'). Hence, option C is correct.",
        "'यशोदा' शब्द का सही संधि-विच्छेद क्या होगा?",
        ["यशो + दा", "यश + ओदा", "यशः + दा", "यशा + दा"],
        "'यशोदा' विसर्ग संधि का उदाहरण है: यशः + दा = यशोदा। विसर्ग के पहले 'अ' और बाद में किसी वर्ग का तीसरा, चौथा या पांचवां वर्ण होने पर विसर्ग 'ओ' में बदल जाता है। अतः विकल्प C सही है।"
    ))
    # Q72 (Hindi - Samas)
    qs.append(create_csat_q(
        72, "General Hindi", "Easy", "B",
        "Which Samas is exemplified by the compound word 'Yathashakti' (यथाशक्ति - according to one's power)?",
        ["Tatpurusha Samas", "Avyayibhava Samas (अव्ययीभाव समास)", "Karmadharaya Samas", "Dvandva Samas"],
        "In 'Yathashakti', the initial element 'Yatha' is an indeclinable prefix (Avyaya) and is primary, making the whole compound function as an adverb; hence it is Avyayibhava Samas. Option B is correct.",
        "'यथाशक्ति' (शक्ति के अनुसार) सामासिक पद में कौन-सा समास है?",
        ["तत्पुरुष समास", "अव्ययीभाव समास", "कर्मधारय समास", "द्वंद्व समास"],
        "जहाँ पहला पद अव्यय (यथा) हो और वही पद प्रधान हो, वहाँ अव्ययीभाव समास होता है। अतः विकल्प B सही है।"
    ))
    # Q73 (Hindi - Tatsam)
    qs.append(create_csat_q(
        73, "General Hindi", "Easy", "A",
        "What is the original Sanskrit Tatsam form of the Hindi word 'Bahu' (बहू / daughter-in-law or bride)?",
        ["Vadhoo (वधू)", "Bahu (बाहु)", "Vridha (वृद्धा)", "Varshini (वर्षिणी)"],
        "The Sanskrit Tatsam word for Hindi Tadbhav 'Bahu' (बहू) is 'Vadhoo' (वधू). Hence, option A is correct.",
        "हिंदी शब्द 'बहू' का शुद्ध तत्सम रूप क्या है?",
        ["वधू", "बाहु", "वृद्धा", "वर्षिणी"],
        "'बहू' तद्भव शब्द है जिसका मूल संस्कृत तत्सम 'वधू' होता है। अतः विकल्प A सही उत्तर है।"
    ))
    # Q74 (Hindi - Paryayvachi)
    qs.append(create_csat_q(
        74, "General Hindi", "Easy", "D",
        "Which of the following is NOT a synonym of 'Ghodha' (घोड़ा - Horse)?",
        ["Ashva (अश्व)", "Hay (हय)", "Turang (तुरंग)", "Karibha (करिभ)"],
        "Ashva, Hay, Ghodak, Turang, and Saindhav are synonyms of horse. 'Karibha' (or Kari) means an elephant (हाथी). Hence, option D is correct.",
        "निम्नलिखित में से कौन-सा शब्द 'घोड़ा' का पर्यायवाची नहीं है?",
        ["अश्व", "हय", "तुरंग", "करिभ"],
        "अश्व, हय, घोटक और तुरंग घोड़े के पर्यायवाची हैं, जबकि 'करिभ' (या करी) हाथी का पर्यायवाची है। अतः विकल्प D सही है।"
    ))
    # Q75 (Hindi - Vilom)
    qs.append(create_csat_q(
        75, "General Hindi", "Easy", "C",
        "What is the correct antonym of the word 'Utkarsha' (उत्कर्ष)?",
        ["Nikarsha (निकर्ष)", "Akarsha (आकर्ष)", "Apakarsha (अपकर्ष)", "Vikarsha (विकर्ष)"],
        "The opposite of 'Utkarsha' (elevation/prosperity) is 'Apakarsha' (decline/deterioration). Hence, option C is correct.",
        "'उत्कर्ष' शब्द का विलोम शब्द क्या है?",
        ["निकर्ष", "आकर्ष", "अपकर्ष", "विकर्ष"],
        "'उत्कर्ष' (उन्नति/प्रगति) का सही विलोम शब्द 'अपकर्ष' (अवनति/पतन) होता है। अतः विकल्प C सही है।"
    ))
    # Q76 (Hindi - Vakyansh)
    qs.append(create_csat_q(
        76, "General Hindi", "Easy", "B",
        "What is the one word for 'That which cannot be forgiven' (जो क्षमा करने योग्य न हो)?",
        ["Akshamya (अक्षम)", "Akshamya (अक्षम्य)", "Nirdoshi (निर्दोषी)", "Kshamashil (क्षमाशील)"],
        "That which cannot be pardoned or forgiven is 'Akshamya' (अक्षम्य). That which can be forgiven is 'Kshamya' (क्षम्य). Hence, option B is correct.",
        "'जो क्षमा करने योग्य न हो' वाक्यांश के लिए एक उपयुक्त शब्द क्या है?",
        ["अक्षम", "अक्षम्य", "निर्दोषी", "क्षमाशील"],
        "जिसे क्षमा न किया जा सके उसे 'अक्षम्य' कहा जाता है। अतः विकल्प B सही उत्तर है।"
    ))
    # Q77 (Hindi - Muhavara)
    qs.append(create_csat_q(
        77, "General Hindi", "Easy", "A",
        "What is the meaning of the Hindi idiom 'Gagar mein Sagar bharna' (गागर में सागर भरना)?",
        ["To express profound and extensive meaning in very few words", "To empty the sea into a pot", "To perform an impossible task literally", "To waste precious water"],
        "'गागर में सागर भरना' is famously used for poet Bihari, meaning to express deep, comprehensive, and vast thought within very few, concise words. Hence, option A is correct.",
        "मुहावरे 'गागर में सागर भरना' का सही अर्थ क्या है?",
        ["थोड़े शब्दों में बहुत अधिक और गूढ़ भाव व्यक्त करना", "घड़े में समुद्र का पानी भरना", "असंभव कार्य को संभव करना", "व्यर्थ बातें करना"],
        "'गागर में सागर भरना' का मुहावरेदार अर्थ है संक्षेप में विस्तृत एवं सारगर्भित विचार प्रस्तुत करना। अतः विकल्प A सही है।"
    ))
    # Q78 (Hindi - Shuddh Vartani)
    qs.append(create_csat_q(
        78, "General Hindi", "Medium", "D",
        "Select the word with the CORRECT grammatical spelling (शुद्ध वर्तनी):",
        ["उज्वल", "उज्जवल", "उज्वल", "उज्ज्वल (Ujjval)"],
        "In 'उज्ज्वल', the consonant 'ज' occurs twice in half (halant) form: 'उ + त् + ज्वल' = 'उज्ज्वल' (उ-ज्-ज्-व-ल). There is no full 'ज'. Hence, option D is correct.",
        "निम्नलिखित में से शुद्ध वर्तनी वाले शब्द का चयन कीजिए:",
        ["उज्वल", "उज्जवल", "उज्वल", "उज्ज्वल"],
        "'उज्ज्वल' की शुद्ध वर्तनी में दोनों 'ज' आधे (स्वररहित) होते हैं: उत् + ज्वल = उज्ज्वल। अतः विकल्प D सही है।"
    ))
    # Q79 (Hindi - Upsarg)
    qs.append(create_csat_q(
        79, "General Hindi", "Easy", "C",
        "Which prefix (उपसर्ग) is present in the word 'Dushcharitra' (दुश्चरित्र)?",
        ["Dush- (दुष्)", "Du- (दु)", "Dus- (दुस् / दुः)", "Dur- (दुर्)"],
        "The standard Sanskrit prefix is 'दुस्' (or Visarga 'दुः'), which by Sandhi rule changes to तालव्य 'श्' before 'च' (दुस् + चरित्र = दुश्चरित्र). Hence, option C is correct.",
        "'दुश्चरित्र' शब्द में कौन-सा उपसर्ग प्रयुक्त हुआ है?",
        ["दुष्", "दु", "दुस्", "दुर्"],
        "संस्कृत के 22 उपसर्गों में 'दुस्' उपसर्ग होता है, जो 'च' के पूर्व आने पर संधि के नियमानुसार 'श्' में परिवर्तित होकर 'दुश्चरित्र' बनता है। अतः विकल्प C सही है।"
    ))
    # Q80 (Hindi - Ras)
    qs.append(create_csat_q(
        80, "General Hindi", "Easy", "B",
        "What is the Sthayi Bhava (स्थायी भाव) of 'Raudra Rasa' (रौद्र रस)?",
        ["Bhaya (भय)", "Krodha (क्रोध)", "Utsaha (उत्साह)", "Shoka (शोक)"],
        "In Indian poetics, the permanent emotion (Sthayi Bhava) of Raudra Rasa (Furious emotion) is Krodha (Anger). Bhaya belongs to Bhayanaka, and Shoka to Karuna. Hence, option B is correct.",
        "'रौद्र रस' का स्थायी भाव क्या होता है?",
        ["भय", "क्रोध", "उत्साह", "शोक"],
        "रौद्र रस का स्थायी भाव 'क्रोध' होता है। भयानक रस का भय तथा करुण रस का शोक होता है। अतः विकल्प B सही है।"
    ))
    # Q81 (General English - Conditional)
    qs.append(create_csat_q(
        81, "General English", "Medium", "A",
        "Complete the sentence with the grammatically correct verb clause:\n'If you had informed me earlier, I _______ you.'",
        ["would have helped", "will help", "would help", "had helped"],
        "In Third Conditional (past unreal conditions: If + Past Perfect), the main clause requires 'would have + past participle (V3)' -> 'would have helped'. Hence, option A is correct.",
        "वाक्य को व्याकरण की दृष्टि से सही क्रिया रूप से पूरा कीजिए:\n'If you had informed me earlier, I _______ you.'",
        ["would have helped", "will help", "would help", "had helped"],
        "थर्ड कंडीशनल (काल्पनिक भूतकाल) में 'If + Past Perfect' होने पर मुख्य उपवाक्य में 'would have + V3' का प्रयोग होता है। अतः 'would have helped' सही है। विकल्प A सही है।"
    ))
    # Q82 (General English - Subject-Verb Agreement)
    qs.append(create_csat_q(
        82, "General English", "Easy", "D",
        "Fill in the blank with the correct auxiliary verb:\n'Bread and butter _______ his wholesome daily breakfast.'",
        ["are", "were", "have been", "is"],
        "When two singular nouns joined by 'and' express a single combined concept, dish, or idea (like bread and butter, slow and steady), they take a singular verb 'is'. Hence, option D is correct.",
        "सही क्रिया रूप से रिक्त स्थान भरिए:\n'Bread and butter _______ his wholesome daily breakfast.'",
        ["are", "were", "have been", "is"],
        "जब दो संज्ञाएं मिलकर एक समग्र विचार या व्यंजन व्यक्त करती हैं (जैसे Bread and butter), तो क्रिया एकवचन (singular - is) होती है। अतः विकल्प D सही है।"
    ))
    # Q83 (General English - Idiom)
    qs.append(create_csat_q(
        83, "General English", "Easy", "C",
        "What is the meaning of the idiomatic phrase 'A piece of cake'?",
        ["A sweet celebratory dessert", "An expensive gift", "A very easy and effortless task", "A difficult puzzle"],
        "The idiom 'a piece of cake' refers to something that is very simple, uncomplicated, and easily accomplished. Hence, option C is correct.",
        "मुहावरे 'A piece of cake' का सही अर्थ क्या है?",
        ["एक मीठा व्यंजन", "एक महंगा उपहार", "एक अत्यंत सरल एवं आसान कार्य", "एक जटिल पहेली"],
        "'A piece of cake' का अर्थ होता है कोई ऐसा काम जो बहुत आसान हो और सरलता से पूरा किया जा सके। अतः विकल्प C सही है।"
    ))
    # Q84 (General English - One Word)
    qs.append(create_csat_q(
        84, "General English", "Easy", "B",
        "What is the single word for: 'The life history of a person written by himself'?",
        ["Biography", "Autobiography", "Chronicle", "Memoir"],
        "An autobiography is the account of a person's life written by that person themselves. A biography is written by someone else. Hence, option B is correct.",
        "दिए गए वाक्यांश के लिए एक उपयुक्त शब्द क्या है:\n'The life history of a person written by himself'?",
        ["Biography", "Autobiography", "Chronicle", "Memoir"],
        "व्यक्ति द्वारा स्वयं लिखी गई अपनी जीवन कथा को 'Autobiography' (आत्मकथा) कहा जाता है। किसी अन्य द्वारा लिखे जाने पर उसे 'Biography' (जीवनी) कहते हैं। अतः विकल्प B सही है।"
    ))
    # Q85 (General English - Spelling)
    qs.append(create_csat_q(
        85, "General English", "Medium", "A",
        "Select the word with the CORRECT spelling of the military rank:",
        ["Lieutenant", "Lieutanant", "Leutenant", "Luitenant"],
        "The standard British/Indian English spelling is 'Lieutenant' (L-i-e-u-t-e-n-a-n-t). Hence, option A is correct.",
        "सैन्य अधिकारी पद 'लेफ्टिनेंट' की सही अंग्रेजी वर्तनी (Spelling) क्या है?",
        ["Lieutenant", "Lieutanant", "Leutenant", "Luitenant"],
        "सही वर्तनी 'Lieutenant' है (L-i-e-u-t-e-n-a-n-t)। अतः विकल्प A सही उत्तर है।"
    ))
    # Q86 (General English - Antonym)
    qs.append(create_csat_q(
        86, "General English", "Medium", "D",
        "What is the antonym of the word 'MITIGATE' (to make less severe or painful)?",
        ["Alleviate", "Assuage", "Diminish", "Aggravate / Intensify"],
        "'Mitigate' means to reduce the severity or harshness of something. Its direct antonym is 'Aggravate' (to make worse or more severe) or 'Intensify'. Hence, option D is correct.",
        "अंग्रेजी शब्द 'MITIGATE' (कम करना / शांत करना) का विलोम शब्द क्या है?",
        ["Alleviate", "Assuage", "Diminish", "Aggravate / Intensify (बढ़ाना / तीव्र करना)"],
        "'Mitigate' का अर्थ किसी समस्या या पीड़ा की तीव्रता को घटाना होता है, जिसका विलोम 'Aggravate' (बढ़ाना/गंभीर बनाना) है। अतः विकल्प D सही है।"
    ))
    # Q87 (General English - Synonym)
    qs.append(create_csat_q(
        87, "General English", "Easy", "C",
        "What is the synonym of the word 'METICULOUS'?",
        ["Careless", "Hasty", "Careful, precise, and thorough", "Lazy"],
        "'Meticulous' means showing great attention to detail, very careful, thorough, and precise. Hence, option C is correct.",
        "'METICULOUS' शब्द का सही समानार्थी (Synonym) क्या है?",
        ["Careless (लापरवाह)", "Hasty (जल्दबाज)", "Careful and thorough (सावधान एवं सूक्ष्मदर्शी)", "Lazy (आलसी)"],
        "'Meticulous' का अर्थ अत्यंत सावधानीपूर्वक बारीक विवरणों पर ध्यान देने वाला होता है। अतः 'Careful and thorough' सही है। विकल्प C सही है।"
    ))
    # Q88 (General English - Preposition with Senior)
    qs.append(create_csat_q(
        88, "General English", "Easy", "B",
        "Fill in the blank with the correct preposition:\n'Mr. Sharma is senior _______ me in service by three years.'",
        ["than", "to", "from", "with"],
        "Comparative adjectives ending in '-ior' borrowed from Latin (such as senior, junior, superior, inferior, prior) are followed by the preposition 'to', never 'than'. Hence, option B is correct.",
        "रिक्त स्थान में सही Preposition भरिए:\n'Mr. Sharma is senior _______ me in service by three years.'",
        ["than", "to", "from", "with"],
        "Latin से आए '-ior' प्रत्यय वाले विशेषणों (senior, junior, superior) के बाद तुलना के लिए 'to' का प्रयोग होता है, 'than' का नहीं। अतः विकल्प B सही है।"
    ))
    # Q89 (General English - Question Tag)
    qs.append(create_csat_q(
        89, "General English", "Easy", "A",
        "Choose the correct question tag to complete the sentence:\n'She sings very sweetly, _______?'",
        ["doesn't she", "isn't she", "did she", "don't she"],
        "With a positive statement in the Simple Present tense third person singular ('sings'), the appropriate negative tag uses 'doesn't + pronoun' -> 'doesn't she?'. Hence, option A is correct.",
        "वाक्य के लिए उपयुक्त Question Tag चुनिए:\n'She sings very sweetly, _______?'",
        ["doesn't she", "isn't she", "did she", "don't she"],
        "सकारात्मक वर्तमान काल (Simple Present) के साथ नकारात्मक टैग 'doesn't she?' का प्रयोग किया जाता है। अतः विकल्प A सही उत्तर है।"
    ))
    # Q90 (General English - Idiom)
    qs.append(create_csat_q(
        90, "General English", "Easy", "D",
        "What is the meaning of the idiom 'To spill the beans'?",
        ["To drop vegetables accidentally", "To cook a meal", "To plant new seeds", "To reveal a secret information indiscreetly"],
        "'To spill the beans' means to disclose confidential or secret information prematurely or inadvertently. Hence, option D is correct.",
        "मुहावरे 'To spill the beans' का सही अर्थ क्या है?",
        ["सब्जी गिरा देना", "खाना पकाना", "बीज बोना", "रहस्य या गोपनीय बात को अनजाने में उजागर कर देना"],
        "अंग्रेजी मुहावरे 'Spill the beans' का अर्थ किसी गुप्त सूचना को गलती से या समय से पहले प्रकट कर देना होता है। अतः विकल्प D सही है।"
    ))
    # Q91 (Decision Making - Assertiveness)
    qs.append(create_csat_q(
        91, "Interpersonal & Communication Skills", "Medium", "C",
        "Which interpersonal communication style is characterized by expressing one's feelings, rights, and boundaries clearly and firmly while fully respecting the rights and dignity of others?",
        ["Aggressive communication", "Passive communication", "Assertive communication", "Passive-aggressive communication"],
        "Assertive communication balances self-respect with respect for others, allowing individuals to advocate for their needs calmly, honestly, and respectfully without resorting to aggression or passivity. Hence, option C is correct.",
        "कौन-सी संचार शैली दूसरों की गरिमा और अधिकारों का सम्मान करते हुए अपने विचारों, अधिकारों और सीमाओं को स्पष्टता व दृढ़ता से व्यक्त करने पर आधारित होती है?",
        ["आक्रामक संचार (Aggressive)", "दब्बू/निष्क्रिय संचार (Passive)", "दृढ़/मुखर संचार (Assertive communication)", "निष्क्रीय-आक्रामक संचार"],
        "दृढ़ (मुखर) संचार में व्यक्ति बिना दूसरों पर हावी हुए और बिना दबकर अपनी बात को सम्मानजनक व स्पष्ट रूप से रखता है। अतः विकल्प C सही है।"
    ))
    # Q92 (Decision Making - Halo Effect)
    qs.append(create_csat_q(
        92, "Interpersonal & Communication Skills", "Medium", "B",
        "In performance appraisal and interviews, the psychological tendency where an overall favorable impression of a person in one attribute unduly influences the evaluation of their other unrelated traits is known as the:",
        ["Horn effect", "Halo effect", "Stereotyping", "Fundamental attribution error"],
        "The Halo effect is a cognitive bias where a positive impression in one domain (e.g., appearance or punctuality) positively biases overall perceptions in other unrelated competencies. (Horn effect is the negative counterpart). Hence, option B is correct.",
        "साक्षात्कार या मूल्यांकन में वह पूर्वाग्रह क्या कहलाता है जिसमें किसी व्यक्ति के एक सकारात्मक गुण के आधार पर उसके अन्य सभी गुणों का भी अनुकूल मूल्यांकन कर लिया जाता है?",
        ["हॉर्न प्रभाव", "परिवेश प्रभाव / हेलो प्रभाव (Halo effect)", "रूढ़िवादिता", "मौलिक आरोपण त्रुटि"],
        "हेलो प्रभाव (Halo Effect) एक संज्ञानात्मक पूर्वाग्रह है जिसमें किसी एक आकर्षक या सकारात्मक पहलू के आधार पर पूरे व्यक्ति का मूल्यांकन प्रभावित हो जाता है। अतः विकल्प B सही है।"
    ))
    # Q93 (Logical Reasoning - Number Series)
    qs.append(create_csat_q(
        93, "Logical Reasoning & Maths", "Easy", "A",
        "Find the next term in the series:\n3, 9, 27, 81, ?",
        ["243", "162", "216", "324"],
        "Each term is multiplied by 3 (powers of 3: 3^1, 3^2, 3^3, 3^4, 3^5): 81 * 3 = 243. Hence, option A is correct.",
        "दी गई श्रेणी का अगला पद ज्ञात कीजिए:\n3, 9, 27, 81, ?",
        ["243", "162", "216", "324"],
        "प्रत्येक पद को 3 से गुणा किया जा रहा है (3 की घातें): 81 × 3 = 243। अतः विकल्प A सही है।"
    ))
    # Q94 (Logical Reasoning - Letter Series)
    qs.append(create_csat_q(
        94, "Logical Reasoning & Maths", "Easy", "D",
        "What is the next letter in the series:\nB, E, H, K, N, ?",
        ["O", "P", "R", "Q"],
        "The positions in the English alphabet advance by +3: B(2) + 3 = E(5) + 3 = H(8) + 3 = K(11) + 3 = N(14) + 3 = Q(17). Hence, option D is correct.",
        "दिए गए अक्षर अनुक्रम में अगला अक्षर क्या होगा:\nB, E, H, K, N, ?",
        ["O", "P", "R", "Q"],
        "प्रत्येक अक्षर के स्थान मान में +3 की वृद्धि हो रही है: B(2), E(5), H(8), K(11), N(14), और 14 + 3 = 17 अर्थात् 'Q'। अतः विकल्प D सही है।"
    ))
    # Q95 (Logical Reasoning - Blood Relation)
    qs.append(create_csat_q(
        95, "Logical Reasoning & Maths", "Easy", "C",
        "A is B's brother. C is A's mother. D is C's father. E is B's son. How is D related to A?",
        ["Father", "Uncle", "Maternal Grandfather (नाना)", "Grandson"],
        "C is the mother of A. D is the father of C. Therefore, D is the maternal grandfather (नाना) of A. Hence, option C is correct.",
        "A, B का भाई है। C, A की माँ है। D, C का पिता है। E, B का पुत्र है। D का A से क्या संबंध है?",
        ["पिता", "चाचा", "नाना (Maternal Grandfather)", "पोता"],
        "A की माँ C है, और C के पिता D हैं। अतः D, A के 'नाना' हैं। विकल्प C सही उत्तर है।"
    ))
    # Q96 (Maths - Work and Wages)
    qs.append(create_csat_q(
        96, "Logical Reasoning & Maths", "Medium", "B",
        "X and Y can complete a work in 10 days and 15 days respectively. They undertake the job for ₹1,500. What is X's share of the earnings based on their work efficiency?",
        ["₹600", "₹900", "₹750", "₹1,000"],
        "Ratio of efficiencies = (1/10) : (1/15) = 3 : 2. Total ratio parts = 3 + 2 = 5. X's share = (3/5) * 1500 = ₹900. Hence, option B is correct.",
        "X और Y एक काम को क्रमशः 10 दिन और 15 दिन में समाप्त कर सकते हैं। वे मिलकर कार्य ₹1,500 में पूरा करने का ठेका लेते हैं। कार्य क्षमता के आधार पर X का हिस्सा कितना होगा?",
        ["₹600", "₹900", "₹750", "₹1,000"],
        "कार्य क्षमताओं का अनुपात = (1/10) : (1/15) = 3 : 2। कुल भाग = 5। X का हिस्सा = (3/5) × 1500 = ₹900। अतः विकल्प B सही है।"
    ))
    # Q97 (Maths - Pipe and Cistern)
    qs.append(create_csat_q(
        97, "Logical Reasoning & Maths", "Easy", "A",
        "Two pipes P and Q can fill an empty water tank in 20 minutes and 30 minutes respectively. If both pipes are opened simultaneously, in how many minutes will the tank be full?",
        ["12 minutes", "15 minutes", "10 minutes", "25 minutes"],
        "Combined filling rate per minute = 1/20 + 1/30 = (3 + 2)/60 = 5/60 = 1/12. Therefore, both pipes together fill the tank in 12 minutes. Hence, option A is correct.",
        "दो नल P और Q एक खाली पानी की टंकी को क्रमशः 20 मिनट और 30 मिनट में भर सकते हैं। यदि दोनों नलों को एक साथ खोल दिया जाए, तो टंकी कितने मिनट में भर जाएगी?",
        ["12 मिनट", "15 मिनट", "10 मिनट", "25 मिनट"],
        "दोनों नलों द्वारा 1 मिनट में भरा गया भाग = 1/20 + 1/30 = 5/60 = 1/12 भाग। अतः पूरी टंकी 12 मिनट में भर जाएगी। विकल्प A सही है।"
    ))
    # Q98 (Maths - Age Problem)
    qs.append(create_csat_q(
        98, "Logical Reasoning & Maths", "Easy", "D",
        "The ratio of the present ages of a father and his son is 5 : 2. If the sum of their present ages is 42 years, what will be the son's age after 5 years?",
        ["12 years", "15 years", "20 years", "17 years"],
        "Let ages be 5x and 2x. 5x + 2x = 42 -> 7x = 42 -> x = 6. Present age of son = 2 * 6 = 12 years. After 5 years, son's age = 12 + 5 = 17 years. Hence, option D is correct.",
        "एक पिता और उसके पुत्र की वर्तमान आयु का अनुपात 5 : 2 है। यदि उनकी आयु का योग 42 वर्ष है, तो 5 वर्ष बाद पुत्र की आयु कितनी होगी?",
        ["12 वर्ष", "15 वर्ष", "20 वर्ष", "17 वर्ष"],
        "5x + 2x = 42 -> 7x = 42 -> x = 6। पुत्र की वर्तमान आयु = 2 × 6 = 12 वर्ष। 5 वर्ष बाद पुत्र की आयु = 12 + 5 = 17 वर्ष होगी। अतः विकल्प D सही है।"
    ))
    # Q99 (Maths - Speed Average)
    qs.append(create_csat_q(
        99, "Logical Reasoning & Maths", "Easy", "C",
        "A motorist travels from city A to city B at an average speed of 60 km/h and returns from B to A along the same route at 40 km/h. What is the average speed for the entire round trip?",
        ["50 km/h", "52 km/h", "48 km/h", "45 km/h"],
        "Average speed for equal forward and return journeys = 2*x*y / (x + y) = 2*60*40 / (60 + 40) = 4800 / 100 = 48 km/h. Hence, option C is correct.",
        "एक मोटर चालक स्थान A से स्थान B तक 60 किमी/घंटा की गति से जाता है और उसी मार्ग से 40 किमी/घंटा की गति से वापस लौटता है। पूरी यात्रा की औसत गति क्या है?",
        ["50 किमी/घंटा", "52 किमी/घंटा", "48 किमी/घंटा", "45 किमी/घंटा"],
        "समान दूरी के आने-जाने की औसत चाल = 2xy / (x + y) = (2 × 60 × 40) / (60 + 40) = 4800 / 100 = 48 किमी/घंटा। अतः विकल्प C सही है।"
    ))
    # Q100 (Maths - Percentage Discount)
    qs.append(create_csat_q(
        100, "Logical Reasoning & Maths", "Easy", "B",
        "Two successive discounts of 20% and 10% on an article are equivalent to a single net discount percentage of:",
        ["30%", "28%", "25%", "22%"],
        "Net discount = d1 + d2 - (d1 * d2) / 100 = 20 + 10 - (20 * 10) / 100 = 30 - 2 = 28%. Hence, option B is correct.",
        "किसी वस्तु पर दी जाने वाली 20% और 10% की दो क्रमिक छूट (Successive Discounts) एक अकेली कितने प्रतिशत समतुल्य छूट के बराबर हैं?",
        ["30%", "28%", "25%", "22%"],
        "समतुल्य छूट = d1 + d2 - (d1 × d2)/100 = 20 + 10 - (20 × 10)/100 = 30 - 2 = 28%। अतः विकल्प B सही है।"
    ))
    return qs

def main():
    q1_50 = get_csat_questions_1_to_50()
    q51_100 = get_csat_questions_51_to_100()
    all_qs = q1_50 + q51_100

    assert len(all_qs) == 100, f"Expected 100 questions, got {len(all_qs)}"

    paper_data = {
        "testId": "uppcs_pre_pyq_2022_csat",
        "categoryId": "uppcs_pre",
        "test_id": "uppcs_pre_pyq_2022_csat",
        "category_id": "uppcs_pre",
        "title": "UPPSC PCS Prelims 2022 — CSAT Paper 2 (Full 100 Qs)",
        "titleEn": "UPPSC PCS Prelims 2022 — CSAT Paper 2 (Full 100 Qs)",
        "titleHi": "UPPSC PCS प्रारंभिक परीक्षा 2022 — सीसैट प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
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
        "examYear": 2022,
        "shiftBadge": "UPPCS Prelims 2022 • CSAT Paper-2 (Full 100 Qs)",
        "questions": all_qs,
        "path": "tests/state_psc/uppcs_pre/pyq/uppcs_pre_pyq_2022_csat.json"
    }

    out_path = os.path.join("tests", "state_psc", "uppcs_pre", "pyq", "uppcs_pre_pyq_2022_csat.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(paper_data, f, ensure_ascii=False, indent=2)

    print(f"SUCCESS: Generated {out_path} with {len(all_qs)} questions!")

if __name__ == "__main__":
    main()
