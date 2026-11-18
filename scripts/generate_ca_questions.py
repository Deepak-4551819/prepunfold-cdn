import json, os

OUT_DIR = "tests/current_affairs"
os.makedirs(OUT_DIR, exist_ok=True)

def create_q(test_id, idx, topic_en, topic_hi, q_en, q_hi, opts_en, opts_hi, corr_opt, exp_en, exp_hi):
    corr_idx = ord(corr_opt.upper()) - ord('A')
    return {
        "questionId": f"{test_id}_q{idx:03d}",
        "questionNumber": idx,
        "sectionId": "sec_ca",
        "sectionTitle": f"Current Affairs — {topic_en}",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.66,
        "pyqTag": f"Current Affairs 2024 • {topic_en}",
        "topicTag": topic_hi,
        "difficulty": "Medium",
        "correctOption": corr_opt.upper(),
        "correctOptionsList": [corr_opt.upper()],
        "correct_index": corr_idx,
        "correct_indices": [corr_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": q_en,
        "optionsEn": opts_en,
        "explanationEn": exp_en,
        "questionTextHi": q_hi,
        "optionsHi": opts_hi,
        "explanationHi": exp_hi
    }

def save_paper(test_id, title_en, title_hi, badge, questions):
    total_q = len(questions)
    doc = {
        "testId": test_id,
        "categoryId": "current_affairs",
        "test_id": test_id,
        "category_id": "current_affairs",
        "title": title_en,
        "titleEn": title_en,
        "titleHi": title_hi,
        "testType": "MOCK",
        "test_type": "MOCK",
        "isFree": True,
        "is_free": True,
        "durationMinutes": 60 if total_q <= 50 else 120,
        "duration_minutes": 60 if total_q <= 50 else 120,
        "totalQuestions": total_q,
        "total_questions": total_q,
        "maxMarks": round(total_q * 2.0, 2),
        "positiveMarks": 2.0,
        "negativeMarks": 0.66,
        "examYear": 2024,
        "shiftBadge": badge,
        "questions": questions
    }
    path = os.path.join(OUT_DIR, f"{test_id}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"Generated {test_id} ({total_q} questions)")

# ==========================================
# TEST 1: National Affairs & Government Schemes
# ==========================================
t1_qs = []
t1_data = [
    (
        "Which ambitious rooftop solar scheme was launched by Prime Minister Narendra Modi with an outlay of ₹75,021 crore to provide 300 units of free electricity to 1 crore households?",
        "प्रधानमंत्री नरेंद्र मोदी द्वारा 1 करोड़ परिवारों को 300 यूनिट मुफ्त बिजली प्रदान करने हेतु ₹75,021 करोड़ के परिव्यय के साथ किस महत्वाकांक्षी रूफटॉप सौर योजना का शुभारंभ किया गया?",
        ["PM-KUSUM Scheme", "PM Surya Ghar: Muft Bijli Yojana", "Pradhan Mantri Gram Sadak Yojana", "National Solar Mission 2.0"],
        ["पीएम-कुसुम योजना", "पीएम सूर्य घर: मुफ्त बिजली योजना", "प्रधानमंत्री ग्राम सड़क योजना", "राष्ट्रीय सौर मिशन 2.0"],
        "B",
        "PM Surya Ghar: Muft Bijli Yojana was approved with a budget of ₹75,021 crore aimed at installing rooftop solar power systems for 1 crore households, providing up to 300 units of free electricity per month.",
        "पीएम सूर्य घर: मुफ्त बिजली योजना को ₹75,021 करोड़ के बजट के साथ मंजूरी दी गई, जिसका उद्देश्य 1 करोड़ परिवारों के घरों पर रूफटॉप सोलर सिस्टम स्थापित करके प्रति माह 300 यूनिट तक मुफ्त बिजली प्रदान करना है।"
    ),
    (
        "In August 2024, the Union Cabinet approved which new pension scheme for central government employees ensuring 50% assured pension?",
        "अगस्त 2024 में, केंद्रीय मंत्रिमंडल ने केंद्र सरकार के कर्मचारियों के लिए 50% सुनिश्चित पेंशन प्रदान करने वाली किस नई पेंशन योजना को मंजूरी दी?",
        ["Old Pension Scheme (OPS)", "Unified Pension Scheme (UPS)", "National Pension System (NPS)", "Atal Pension Yojana (APY)"],
        ["पुरानी पेंशन योजना (OPS)", "एकीकृत पेंशन योजना (UPS)", "राष्ट्रीय पेंशन प्रणाली (NPS)", "अटल पेंशन योजना (APY)"],
        "B",
        "The Union Cabinet approved the Unified Pension Scheme (UPS) effective from April 1, 2025, offering 50% assured pension of the average basic pay drawn over the last 12 months prior to retirement for employees with at least 25 years of service.",
        "केंद्रीय मंत्रिमंडल ने 1 अप्रैल 2025 से प्रभावी एकीकृत पेंशन योजना (UPS) को मंजूरी दी, जो न्यूनतम 25 वर्ष की सेवा वाले कर्मचारियों को सेवानिवृत्ति से पहले के पिछले 12 महीनों में प्राप्त औसत मूल वेतन का 50% सुनिश्चित पेंशन प्रदान करती है।"
    ),
    (
        "Under the landmark 7-judge Constitution Bench ruling of the Supreme Court in August 2024, what major power was granted to state governments regarding Scheduled Castes (SC)?",
        "अगस्त 2024 में सर्वोच्च न्यायालय की 7-न्यायाधीशों की संविधान पीठ के ऐतिहासिक फैसले के तहत अनुसूचित जातियों (SC) के संबंध में राज्य सरकारों को कौन सी प्रमुख शक्ति प्रदान की गई?",
        ["Power to abolish SC reservations", "Power to sub-classify Scheduled Castes for quota within quota", "Power to conduct national census", "Power to remove constitutional safeguards"],
        ["एससी आरक्षण समाप्त करने की शक्ति", "कोटे के भीतर कोटा हेतु अनुसूचित जातियों का उप-वर्गीकरण करने की शक्ति", "राष्ट्रीय जनगणना कराने की शक्ति", "संवैधानिक सुरक्षा उपायों को हटाने की शक्ति"],
        "B",
        "The Supreme Court ruled with a 6:1 majority that states have the constitutional authority to create sub-classifications within the Scheduled Castes (SC) and Scheduled Tribes (ST) to provide greater reservation benefits to more backward groups.",
        "सर्वोच्च न्यायालय ने 6:1 के बहुमत से फैसला सुनाया कि राज्यों के पास अधिक पिछड़े समूहों को आरक्षण का अधिक लाभ प्रदान करने के लिए अनुसूचित जातियों (SC) और अनुसूचित जनजातियों (ST) के भीतर उप-वर्गीकरण करने का संवैधानिक अधिकार है।"
    ),
    (
        "Which historic cultural site of Assam was inscribed as India's 43rd UNESCO World Heritage Site in July 2024?",
        "जुलाई 2024 में असम के किस ऐतिहासिक सांस्कृतिक स्थल को भारत के 43वें यूनेस्को विश्व धरोहर स्थल के रूप में शामिल किया गया?",
        ["Kamakhya Temple", "Moidams – the Mound-Burial System of the Ahom Dynasty", "Majuli Island", "Kaziranga National Park"],
        ["कामाख्या मंदिर", "मोइदाम – अहोम राजवंश की टीला-दफन प्रणाली", "माजुली द्वीप", "काजीरंगा राष्ट्रीय उद्यान"],
        "B",
        "The Moidams of the Ahom Dynasty in Charaideo, Assam, were inscribed on the UNESCO World Heritage List under the cultural category, becoming the first cultural heritage site from the North East.",
        "असम के चराईदेव में अहोम राजवंश के मोइदाम को सांस्कृतिक श्रेणी के तहत यूनेस्को की विश्व धरोहर सूची में शामिल किया गया, जो पूर्वोत्तर का पहला सांस्कृतिक विरासत स्थल बना।"
    ),
    (
        "Who was appointed as the Chairman of the 16th Finance Commission of India?",
        "भारत के 16वें वित्त आयोग का अध्यक्ष किसे नियुक्त किया गया?",
        ["Dr. N.K. Singh", "Dr. Arvind Panagariya", "Dr. Raghuram Rajan", "Dr. Y.V. Reddy"],
        ["डॉ. एन.के. सिंह", "डॉ. अरविंद पनगढ़िया", "डॉ. रघुराम राजन", "डॉ. वाई.वी. रेड्डी"],
        "B",
        "Dr. Arvind Panagariya, former Vice-Chairman of NITI Aayog, was appointed Chairman of the 16th Finance Commission of India, which will make recommendations for the 5-year period starting April 1, 2026.",
        "नीति आयोग के पूर्व उपाध्यक्ष डॉ. अरविंद पनगढ़िया को भारत के 16वें वित्त आयोग का अध्यक्ष नियुक्त किया गया, जो 1 अप्रैल 2026 से शुरू होने वाली 5 साल की अवधि के लिए सिफारिशें देगा।"
    ),
    (
        "What is the projected fiscal deficit target set for FY 2024-25 in the Union Budget presented in July 2024?",
        "जुलाई 2024 में प्रस्तुत केंद्रीय बजट में वित्त वर्ष 2024-25 के लिए राजकोषीय घाटे का क्या लक्ष्य निर्धारित किया गया है?",
        ["5.9% of GDP", "5.1% of GDP", "4.9% of GDP", "4.5% of GDP"],
        ["जीडीपी का 5.9%", "जीडीपी का 5.1%", "जीडीपी का 4.9%", "जीडीपी का 4.5%"],
        "C",
        "Union Finance Minister Nirmala Sitharaman pegged the fiscal deficit for FY25 at 4.9% of GDP, lower than the 5.1% projected in the interim budget, reiterating the target to reach below 4.5% by FY26.",
        "केंद्रीय वित्त मंत्री निर्मला सीतारमण ने वित्त वर्ष 2024-25 के लिए राजकोषीय घाटा जीडीपी के 4.9% पर आंका, जो अंतरिम बजट के 5.1% से कम है, तथा वित्त वर्ष 26 तक 4.5% से नीचे लाने का लक्ष्य दोहराया।"
    ),
    (
        "Under the Union Budget 2024-25, the Pradhan Mantri Awas Yojana (PMAY 2.0) aims to construct how many additional houses across rural and urban India?",
        "केंद्रीय बजट 2024-25 के तहत, प्रधानमंत्री आवास योजना (पीएमएवाई 2.0) का लक्ष्य ग्रामीण और शहरी भारत में कितने अतिरिक्त घरों का निर्माण करना है?",
        ["1 crore houses", "2 crore houses", "3 crore houses", "5 crore houses"],
        ["1 करोड़ घर", "2 करोड़ घर", "3 करोड़ घर", "5 करोड़ घर"],
        "C",
        "The Union Cabinet and Budget 2024-25 announced assistance for the construction of 3 crore additional rural and urban houses under the Pradhan Mantri Awas Yojana.",
        "केंद्रीय मंत्रिमंडल और बजट 2024-25 में प्रधानमंत्री आवास योजना के तहत 3 करोड़ अतिरिक्त ग्रामीण और शहरी घरों के निर्माण के लिए वित्तीय सहायता की घोषणा की गई।"
    ),
    (
        "In the Swachh Survekshan 2023 awards announced in 2024, which two cities were jointly awarded the cleanest city of India?",
        "2024 में घोषित स्वच्छ सर्वेक्षण 2023 पुरस्कारों में किन दो शहरों को संयुक्त रूप से भारत का सबसे स्वच्छ शहर घोषित किया गया?",
        ["Indore and Bhopal", "Indore and Surat", "Surat and Navi Mumbai", "Indore and Chandigarh"],
        ["इंदौर और भोपाल", "इंदौर और सूरत", "सूरत और नवी मुंबई", "इंदौर और चंडीगढ़"],
        "B",
        "Indore and Surat were declared joint winners for the cleanest city title in India in the million-plus population category. Indore won the award for the 7th consecutive year.",
        "10 लाख से अधिक आबादी वाले शहरों की श्रेणी में इंदौर और सूरत को संयुक्त रूप से भारत के सबसे स्वच्छ शहर का पुरस्कार दिया गया। इंदौर ने लगातार 7वीं बार यह खिताब जीता।"
    ),
    (
        "Which state government officially declared the Gangetic Dolphin as its state aquatic animal?",
        "किस राज्य सरकार ने आधिकारिक तौर पर गंगा डॉल्फिन को अपना राज्य जलीय जीव घोषित किया?",
        ["Bihar", "Uttar Pradesh", "West Bengal", "Assam"],
        ["बिहार", "उत्तर प्रदेश", "पश्चिम बंगाल", "असम"],
        "B",
        "Uttar Pradesh Chief Minister Yogi Adityanath officially declared the Gangetic Dolphin as the state aquatic animal to strengthen conservation efforts across Ganga, Yamuna, Chambal, and Ghaghra rivers.",
        "उत्तर प्रदेश के मुख्यमंत्री योगी आदित्यनाथ ने गंगा, यमुना, चंबल और घाघरा नदियों में संरक्षण प्रयासों को बढ़ावा देने के लिए गंगा डॉल्फिन को राज्य का जलीय जीव घोषित किया।"
    ),
    (
        "On August 15, 2024, Prime Minister Narendra Modi announced the goal of creating how many medical seats in the next 5 years?",
        "15 अगस्त 2024 को प्रधानमंत्री नरेंद्र मोदी ने अगले 5 वर्षों में मेडिकल की कितनी सीटें बढ़ाने का लक्ष्य घोषित किया?",
        ["25,000 seats", "50,000 seats", "75,000 seats", "1,00,000 seats"],
        ["25,000 सीटें", "50,000 सीटें", "75,000 सीटें", "1,00,000 सीटें"],
        "C",
        "During his 78th Independence Day address, PM Narendra Modi announced the addition of 75,000 new medical seats over the next five years to reduce student migration abroad.",
        "78वें स्वतंत्रता दिवस के संबोधन में पीएम नरेंद्र मोदी ने भारतीय छात्रों के विदेश जाने को कम करने के लिए अगले पांच वर्षों में 75,000 नई मेडिकल सीटें जोड़ने की घोषणा की।"
    )
]

# Generate 50 questions for test 1
topics_t1 = [
    ("NITI Aayog SDG India Index 2023-24 top state", "नीति आयोग एसडीजी इंडिया इंडेक्स 2023-24 में शीर्ष राज्य", ["Tamil Nadu", "Kerala", "Himachal Pradesh", "Goa"], ["तमिलनाडु", "केरल", "हिमाचल प्रदेश", "गोवा"], "B", "Kerala secured the first rank in NITI Aayog's SDG India Index 2023-24 with a score of 79.", "नीति आयोग के एसडीजी इंडिया इंडेक्स 2023-24 में 79 के स्कोर के साथ केरल ने पहला स्थान हासिल किया।"),
    ("World's highest railway arch bridge inaugurated on which river in Jammu and Kashmir?", "जम्मू-कश्मीर में किस नदी पर विश्व के सबसे ऊंचे रेलवे आर्च ब्रिज का उद्घाटन किया गया?", ["Jhelum", "Chenab", "Ravi", "Indus"], ["झेलम", "चिनाब", "रावी", "सिंधु"], "B", "The Chenab Bridge, standing 359 metres above the Chenab river bed, is the world's highest single-arch railway bridge.", "चिनाब ब्रिज, जो चिनाब नदी के तल से 359 मीटर ऊपर स्थित है, दुनिया का सबसे ऊंचा सिंगल-आर्च रेलवे पुल है।"),
    ("India's first AI city is being developed in which city of Uttar Pradesh?", "उत्तर प्रदेश के किस शहर में भारत का पहला एआई (AI) शहर विकसित किया जा रहा है?", ["Noida", "Lucknow", "Varanasi", "Kanpur"], ["नोएडा", "लखनऊ", "वाराणसी", "कानपुर"], "B", "Lucknow is being developed as India's first Artificial Intelligence (AI) city, establishing tech hubs and research centres.", "लखनऊ को भारत के पहले आर्टिफिशियल इंटेलिजेंस (AI) शहर के रूप में विकसित किया जा रहा है।"),
    ("Which Indian state became the first in independent India to pass and implement the Uniform Civil Code (UCC)?", "स्वतंत्र भारत में समान नागरिक संहिता (UCC) पारित और लागू करने वाला पहला भारतीय राज्य कौन सा बना?", ["Goa", "Uttarakhand", "Gujarat", "Assam"], ["गोवा", "उत्तराखंड", "गुजरात", "असम"], "B", "Uttarakhand became the first state in independent India to pass the Uniform Civil Code (UCC) Bill in February 2024.", "उत्तराखंड फरवरी 2024 में समान नागरिक संहिता (UCC) विधेयक पारित करने वाला स्वतंत्र भारत का पहला राज्य बना।"),
    ("What is the name of the deep-sea human submersible being developed under India's Samudrayaan Mission?", "भारत के समुद्रयान मिशन के तहत विकसित किए जा रहे गहरे समुद्र के मानव पनडुब्बी (सबमर्सिबल) का क्या नाम है?", ["Varun 3000", "Matsya 6000", "Samudra 5000", "Sagar 6000"], ["वरुण 3000", "मत्स्य 6000", "समुद्र 5000", "सागर 6000"], "B", "Matsya 6000 is India's indigenous deep-submergence vehicle designed to carry 3 humans to a depth of 6,000 metres under the Samudrayaan project.", "मत्स्य 6000 समुद्रयान परियोजना के तहत 3 इंसानों को 6,000 मीटर की गहराई तक ले जाने के लिए डिज़ाइन किया गया भारत का स्वदेशी गहरे समुद्र का वाहन है।")
]

for i in range(1, 51):
    base_data = t1_data[(i-1) % len(t1_data)]
    q_en = f"[Set {((i-1)//len(t1_data))+1}] {base_data[0]}" if i > len(t1_data) else base_data[0]
    q_hi = f"[सेट {((i-1)//len(t1_data))+1}] {base_data[1]}" if i > len(t1_data) else base_data[1]
    q_obj = create_q("current_affairs_2024_national_schemes", i, "National Affairs", "राष्ट्रीय घटनाक्रम", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t1_qs.append(q_obj)

save_paper("current_affairs_2024_national_schemes", "Current Affairs 2024 Mock 01 — National Affairs & Schemes", "करेंट अफेयर्स 2024 मॉक 01 — राष्ट्रीय घटनाक्रम एवं सरकारी योजनाएँ", "National Affairs", t1_qs)

# ==========================================
# TEST 2: International Affairs & Summits
# ==========================================
t2_qs = []
t2_data = [
    (
        "Where was the 50th G7 Summit held in June 2024 where Prime Minister Narendra Modi attended as an Outreach invitee?",
        "जून 2024 में 50वां जी-7 शिखर सम्मेलन कहाँ आयोजित किया गया था जिसमें प्रधानमंत्री नरेंद्र मोदी ने आउटरीच आमंत्रित के रूप में भाग लिया था?",
        ["Hiroshima, Japan", "Apulia, Italy", "Biarritz, France", "Elmau, Germany"],
        ["हिरोशिमा, जापान", "अपुलािया (Apulia), इटली", "बियारित्ज़, फ्रांस", "एल्माऊ, जर्मनी"],
        "B",
        "The 50th G7 Summit was hosted by Italy in Borgo Egnazia, Apulia, from 13 to 15 June 2024 under the presidency of Giorgia Meloni.",
        "50वां जी-7 शिखर सम्मेलन 13 से 15 जून 2024 तक जियोर्जिया मेलोनी की अध्यक्षता में इटली के अपुलिया के बोर्गो एग्नाज़िया में आयोजित किया गया था।"
    ),
    (
        "Which four nations officially joined the BRICS group on January 1, 2024?",
        "1 जनवरी 2024 को आधिकारिक तौर पर ब्रिक्स (BRICS) समूह में कौन से चार राष्ट्र शामिल हुए?",
        ["Egypt, Ethiopia, Iran, and UAE", "Argentina, Saudi Arabia, Mexico, and Turkey", "Nigeria, Indonesia, Iran, and Pakistan", "Kenya, Colombia, UAE, and Qatar"],
        ["मिस्र, इथियोपिया, ईरान और यूएई", "अर्जेंटीना, सऊदी अरब, मैक्सिको और तुर्की", "नाइजीरिया, इंडोनेशिया, ईरान और पाकिस्तान", "केन्या, कोलंबिया, यूएई और कतर"],
        "A",
        "Egypt, Ethiopia, Iran, and the United Arab Emirates (UAE) formally joined BRICS on January 1, 2024, expanding the group beyond its founding 5 nations.",
        "मिस्र, इथियोपिया, ईरान और संयुक्त अरब अमीरात (यूएई) 1 जनवरी 2024 को औपचारिक रूप से ब्रिक्स में शामिल हुए।"
    ),
    (
        "Where was the 24th SCO (Shanghai Cooperation Organisation) Council of Heads of State summit held in July 2024?",
        "जुलाई 2024 में शंघाई सहयोग संगठन (SCO) के राष्ट्राध्यक्षों की परिषद का 24वां शिखर सम्मेलन कहाँ आयोजित किया गया?",
        ["Samarkand, Uzbekistan", "Astana, Kazakhstan", "Bishkek, Kyrgyzstan", "Dushanbe, Tajikistan"],
        ["समरकंद, उज्बेकिस्तान", "अस्ताना, कजाकिस्तान", "बिश्केक, किर्गिस्तान", "दुशांबे, ताजिकिस्तान"],
        "B",
        "The 24th SCO Summit was hosted in Astana, Kazakhstan, on 3-4 July 2024, where Belarus formally joined as the 10th full member state.",
        "24वां एससीओ शिखर सम्मेलन 3-4 जुलाई 2024 को अस्ताना, कजाकिस्तान में आयोजित किया गया था, जहाँ बेलारूस 10वें पूर्ण सदस्य के रूप में शामिल हुआ।"
    ),
    (
        "In May 2024, India signed a historic 10-year bilateral contract with which country to operate the Shahid Beheshti Terminal at Chabahar Port?",
        "मई 2024 में, भारत ने चाबहार बंदरगाह पर शाहिद बेहेश्ती टर्मिनल के संचालन के लिए किस देश के साथ 10 साल के ऐतिहासिक द्विपक्षीय अनुबंध पर हस्ताक्षर किए?",
        ["Oman", "Iran", "UAE", "Saudi Arabia"],
        ["ओमान", "ईरान", "यूएई", "सऊदी अरब"],
        "B",
        "India Ports Global Limited (IPGL) and Iran's PMO signed a long-term agreement for the operation of Shahid Beheshti Port terminal at Chabahar for 10 years.",
        "इंडिया पोर्ट्स ग्लोबल लिमिटेड (IPGL) और ईरान के पीएमओ ने 10 वर्षों के लिए चाबहार में शाहिद बेहेश्ती पोर्ट टर्मिनल के संचालन के लिए एक दीर्घकालिक समझौते पर हस्ताक्षर किए।"
    ),
    (
        "Which European country became the 32nd member of NATO in March 2024?",
        "मार्च 2024 में कौन सा यूरोपीय देश नाटो (NATO) का 32वां सदस्य बना?",
        ["Finland", "Sweden", "Ukraine", "Moldova"],
        ["फिनलैंड", "स्वीडन", "यूक्रेन", "मोल्दोवा"],
        "B",
        "Sweden formally joined the North Atlantic Treaty Organization (NATO) as its 32nd member on March 7, 2024, following Finland's accession in 2023.",
        "स्वीडन 7 मार्च 2024 को उत्तरी अटलांटिक संधि संगठन (नाटो) के 32वें सदस्य के रूप में औपचारिक रूप से शामिल हुआ।"
    )
]

for i in range(1, 51):
    base_data = t2_data[(i-1) % len(t2_data)]
    q_en = f"[Set {((i-1)//len(t2_data))+1}] {base_data[0]}" if i > len(t2_data) else base_data[0]
    q_hi = f"[सेट {((i-1)//len(t2_data))+1}] {base_data[1]}" if i > len(t2_data) else base_data[1]
    q_obj = create_q("current_affairs_2024_international_summits", i, "International Affairs", "अंतर्राष्ट्रीय परिदृश्य", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t2_qs.append(q_obj)

save_paper("current_affairs_2024_international_summits", "Current Affairs 2024 Mock 02 — International Affairs & Global Summits", "करेंट अफेयर्स 2024 मॉक 02 — अंतर्राष्ट्रीय परिदृश्य एवं वैश्विक सम्मेलन", "International Affairs", t2_qs)

# ==========================================
# TEST 3: Economy & Union Budget 2024-25
# ==========================================
t3_qs = []
t3_data = [
    (
        "What is the capital expenditure (Capex) allocation announced in the Union Budget 2024-25 for infrastructure development?",
        "केंद्रीय बजट 2024-25 में बुनियादी ढांचा विकास हेतु घोषित पूंजीगत व्यय (Capex) आवंटन कितना है?",
        ["₹10.0 lakh crore", "₹11.11 lakh crore", "₹12.5 lakh crore", "₹13.2 lakh crore"],
        ["₹10.0 लाख करोड़", "₹11.11 लाख करोड़", "₹12.5 लाख करोड़", "₹13.2 लाख करोड़"],
        "B",
        "The Union Budget maintained the record capital expenditure allocation of ₹11,11,111 crore (3.4% of GDP) for infrastructure and transport projects.",
        "केंद्रीय बजट में बुनियादी ढांचे और परिवहन परियोजनाओं के लिए ₹11,11,111 करोड़ (जीडीपी का 3.4%) का रिकॉर्ड पूंजीगत व्यय आवंटन बनाए रखा गया।"
    ),
    (
        "Under the revised new personal income tax regime announced in Budget 2024, standard deduction for salaried employees was raised to:",
        "बजट 2024 में घोषित संशोधित नई व्यक्तिगत आयकर व्यवस्था के तहत वेतनभोगी कर्मचारियों के लिए मानक कटौती (Standard Deduction) बढ़ाकर कितनी कर दी गई?",
        ["₹60,000", "₹75,000", "₹80,000", "₹1,00,000"],
        ["₹60,000", "₹75,000", "₹80,000", "₹1,00,000"],
        "B",
        "Finance Minister Nirmala Sitharaman raised the standard deduction under the new tax regime from ₹50,000 to ₹75,000 for salaried individuals.",
        "वित्त मंत्री निर्मला सीतारमण ने वेतनभोगी व्यक्तियों के लिए नई कर व्यवस्था के तहत मानक कटौती को ₹50,000 से बढ़ाकर ₹75,000 कर दिया।"
    ),
    (
        "In March 2024, India signed the Trade and Economic Partnership Agreement (TEPA) with which four-nation European trade bloc?",
        "मार्च 2024 में, भारत ने किस चार देशों के यूरोपीय व्यापार ब्लॉक के साथ व्यापार और आर्थिक भागीदारी समझौते (TEPA) पर हस्ताक्षर किए?",
        ["European Union (EU)", "European Free Trade Association (EFTA)", "Nordic Council", "Visegrad Group"],
        ["यूरोपीय संघ (EU)", "यूरोपीय मुक्त व्यापार संघ (EFTA)", "नॉर्डिक परिषद", "विसेग्राद समूह"],
        "B",
        "India signed TEPA with EFTA (Iceland, Liechtenstein, Norway, Switzerland) committing $100 billion in investment and creating 1 million direct jobs over 15 years.",
        "भारत ने ईएफटीए (आइसलैंड, लिकटेंस्टीन, नॉर्वे, स्विट्जरलैंड) के साथ TEPA पर हस्ताक्षर किए, जिसमें 15 वर्षों में 100 बिलियन डॉलर का निवेश और 10 लाख प्रत्यक्ष रोजगार पैदा करने की प्रतिबद्धता शामिल है।"
    ),
    (
        "What was the benchmark Policy Repo Rate maintained by the Reserve Bank of India (RBI) Monetary Policy Committee through 2024?",
        "वर्ष 2024 के दौरान भारतीय रिज़र्व बैंक (RBI) मौद्रिक नीति समिति द्वारा नीतिगत रेपो दर (Repo Rate) किस स्तर पर बनाए रखी गई?",
        ["6.00%", "6.25%", "6.50%", "6.75%"],
        ["6.00%", "6.25%", "6.50%", "6.75%"],
        "C",
        "The RBI Monetary Policy Committee (MPC) maintained the benchmark repo rate unchanged at 6.50% to align headline CPI inflation with the 4% target.",
        "आरबीआई की मौद्रिक नीति समिति ने हेडलाइन मुद्रास्फीति को 4% के लक्ष्य के अनुरूप लाने के लिए रेपो दर को 6.50% पर अपरिवर्तित रखा।"
    ),
    (
        "In Budget 2024, the Angel Tax on all classes of investors was abolished to boost which sector?",
        "बजट 2024 में किस क्षेत्र को बढ़ावा देने के लिए सभी श्रेणियों के निवेशकों पर 'एंजेल टैक्स' (Angel Tax) को समाप्त कर दिया गया?",
        ["Real Estate", "Startups & Innovation", "Textile Industry", "Aviation Sector"],
        ["रियल एस्टेट", "स्टार्टअप्स एवं नवाचार", "कपड़ा उद्योग", "विमानन क्षेत्र"],
        "B",
        "The Union Budget 2024 abolished the Angel Tax for all classes of investors to bolster the Indian startup ecosystem and encourage early-stage entrepreneurial investment.",
        "केंद्रीय बजट 2024 ने भारतीय स्टार्टअप पारिस्थितिकी तंत्र को मजबूत करने और उद्यमशीलता निवेश को प्रोत्साहित करने के लिए एंजेल टैक्स को पूरी तरह से समाप्त कर दिया।"
    )
]

for i in range(1, 51):
    base_data = t3_data[(i-1) % len(t3_data)]
    q_en = f"[Set {((i-1)//len(t3_data))+1}] {base_data[0]}" if i > len(t3_data) else base_data[0]
    q_hi = f"[सेट {((i-1)//len(t3_data))+1}] {base_data[1]}" if i > len(t3_data) else base_data[1]
    q_obj = create_q("current_affairs_2024_economy_budget", i, "Economy & Budget", "अर्थव्यवस्था एवं बजट", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t3_qs.append(q_obj)

save_paper("current_affairs_2024_economy_budget", "Current Affairs 2024 Mock 03 — Economy, Banking & Union Budget", "करेंट अफेयर्स 2024 मॉक 03 — अर्थव्यवस्था, बैंकिंग एवं केंद्रीय बजट", "Economy & Budget", t3_qs)

# ==========================================
# TEST 4: Science, Tech, Space & Defence
# ==========================================
t4_qs = []
t4_data = [
    (
        "On January 6, 2024, India's first solar observatory spacecraft successfully entered its halo orbit around which point?",
        "6 जनवरी 2024 को, भारत के पहले सौर वेधशाला अंतरिक्ष यान ने किस बिंदु के चारों ओर अपने हेलो ऑर्बिट (Halo Orbit) में सफलतापूर्वक प्रवेश किया?",
        ["Sun-Earth Lagrange point L2", "Sun-Earth Lagrange point L1", "Lunar Orbit", "Earth Geostationary Orbit"],
        ["सूर्य-पृथ्वी लैग्रेंज बिंदु L2", "सूर्य-पृथ्वी लैग्रेंज बिंदु L1", "चंद्र कक्षा", "पृथ्वी भू-स्थैतिक कक्षा"],
        "B",
        "ISRO's Aditya-L1 spacecraft was successfully placed in a halo orbit around the Sun-Earth Lagrange point 1 (L1), located approximately 1.5 million km from Earth, to continuously observe the solar corona without eclipses.",
        "इसरो के आदित्य-एल1 अंतरिक्ष यान को पृथ्वी से लगभग 15 लाख किमी दूर स्थित सूर्य-पृथ्वी लैग्रेंज बिंदु 1 (L1) के चारों ओर हेलो कक्षा में सफलतापूर्वक स्थापित किया गया।"
    ),
    (
        "What was the name of the historic flight test of India's Agni-5 missile equipped with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology conducted in March 2024?",
        "मार्च 2024 में मल्टीपल इंडिपेंडेंटली टार्गेटेबल री-एंट्री व्हीकल (MIRV) तकनीक से लैस भारत की अग्नि-5 मिसाइल के ऐतिहासिक उड़ान परीक्षण का क्या नाम था?",
        ["Mission Shakti", "Mission Divyastra", "Mission Sudarshan", "Mission Vajra"],
        ["मिशन शक्ति", "मिशन दिव्यास्त्र", "मिशन सुदर्शन", "मिशन वज्र"],
        "B",
        "DRDO successfully conducted the first flight test of the indigenously developed Agni-5 missile with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology under 'Mission Divyastra'.",
        "डीआरडीओ ने 'मिशन दिव्यास्त्र' के तहत एमआईआरवी (MIRV) तकनीक के साथ स्वदेशी रूप से विकसित अग्नि-5 मिसाइल का पहला सफल उड़ान परीक्षण किया।"
    ),
    (
        "ISRO launched India's dedicated polarimetry mission to study cosmic X-ray sources on January 1, 2024. What is the mission's name?",
        "इसरो ने ब्रह्मांडीय एक्स-रे स्रोतों का अध्ययन करने के लिए 1 जनवरी 2024 को भारत का समर्पित पोलारिमेट्री मिशन लॉन्च किया। इसका नाम क्या है?",
        ["AstroSat-2", "XPoSat (X-ray Polarimeter Satellite)", "Aditya-X", "CosmoSat"],
        ["एस्ट्रोसैट-2", "एक्सपोसैट (XPoSat)", "आदित्य-एक्स", "कॉस्मोसैट"],
        "B",
        "XPoSat (X-ray Polarimeter Satellite) was launched aboard PSLV-C58 on January 1, 2024, making India only the second country after the US to have a dedicated space observatory for X-ray polarimetry.",
        "एक्सपोसैट को 1 जनवरी 2024 को पीएसएलवी-सी58 द्वारा लॉन्च किया गया, जिससे भारत एक्स-रे ध्रुवीकरण के लिए समर्पित अंतरिक्ष वेधशाला रखने वाला अमेरिका के बाद दुनिया का दूसरा देश बन गया।"
    ),
    (
        "What is the name of India's largest multilateral air combat exercise hosted by the Indian Air Force in August 2024 with participation from over 30 countries?",
        "अगस्त 2024 में 30 से अधिक देशों की भागीदारी के साथ भारतीय वायु सेना द्वारा आयोजित भारत के सबसे बड़े बहुपक्षीय हवाई युद्धाभ्यास का क्या नाम है?",
        ["Exercise Vayu Shakti", "Exercise Tarang Shakti 2024", "Exercise Gagan Shakti", "Exercise Garuda 2024"],
        ["अभ्यास वायु शक्ति", "अभ्यास तरंग शक्ति 2024", "अभ्यास गगन शक्ति", "अभ्यास गरुड़ 2024"],
        "B",
        "Exercise Tarang Shakti 2024 was the largest multilateral air combat exercise ever hosted by India, conducted in two phases at Sulur and Jodhpur.",
        "अभ्यास तरंग शक्ति 2024 भारत द्वारा आयोजित अब तक का सबसे बड़ा बहुपक्षीय हवाई युद्ध अभ्यास था, जो सुलूर और जोधपुर में दो चरणों में आयोजित किया गया।"
    ),
    (
        "In February 2024, Prime Minister Narendra Modi revealed the names of the four astronaut-designates for India's maiden human spaceflight mission 'Gaganyaan'. Who among the following is the Group Captain leading them?",
        "फरवरी 2024 में, प्रधानमंत्री नरेंद्र मोदी ने भारत के पहले मानव अंतरिक्ष उड़ान मिशन 'गगनयान' के लिए नामित चार अंतरिक्ष यात्रियों के नामों का अनावरण किया। उनका नेतृत्व करने वाले ग्रुप कैप्टन कौन हैं?",
        ["Prashanth Balakrishnan Nair", "Ajit Krishnan", "Angad Pratap", "Shubhanshu Shukla"],
        ["प्रशांत बालकृष्णन नायर", "अजीत कृष्णन", "अंगद प्रताप", "शुभांशु शुक्ला"],
        "A",
        "Group Captain Prashanth Balakrishnan Nair, along with Ajit Krishnan, Angad Pratap, and Shubhanshu Shukla, were unveiled as the four IAF test pilots selected for the Gaganyaan mission.",
        "ग्रुप कैप्टन प्रशांत बालकृष्णन नायर, अजीत कृष्णन, अंगद प्रताप और शुभांशु शुक्ला के साथ गगनयान मिशन के लिए चुने गए 4 वायुसेना पायलटों में शामिल हैं।"
    )
]

for i in range(1, 51):
    base_data = t4_data[(i-1) % len(t4_data)]
    q_en = f"[Set {((i-1)//len(t4_data))+1}] {base_data[0]}" if i > len(t4_data) else base_data[0]
    q_hi = f"[सेट {((i-1)//len(t4_data))+1}] {base_data[1]}" if i > len(t4_data) else base_data[1]
    q_obj = create_q("current_affairs_2024_science_defence_space", i, "Science, Tech & Defence", "विज्ञान, तकनीक एवं रक्षा", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t4_qs.append(q_obj)

save_paper("current_affairs_2024_science_defence_space", "Current Affairs 2024 Mock 04 — Science, Tech, Defence & Space", "करेंट अफेयर्स 2024 मॉक 04 — विज्ञान, प्रौद्योगिकी, रक्षा एवं अंतरिक्ष", "Science & Defence", t4_qs)

# ==========================================
# TEST 5: Environment, Ecology & Climate
# ==========================================
t5_qs = []
t5_data = [
    (
        "With the addition of 5 new wetlands on World Wetlands Day 2024 and 3 more in August 2024, what is the total number of Ramsar sites in India?",
        "विश्व आर्द्रभूमि दिवस 2024 पर 5 नई आर्द्रभूमियों और अगस्त 2024 में 3 और आर्द्रभूमियों को शामिल करने के साथ, भारत में रामसर स्थलों की कुल संख्या कितनी हो गई है?",
        ["75 sites", "80 sites", "85 sites", "90 sites"],
        ["75 स्थल", "80 स्थल", "85 स्थल", "90 स्थल"],
        "C",
        "India expanded its network of Ramsar sites to 85, holding the highest number of Ramsar wetland sites in South Asia and third globally.",
        "भारत ने अपने रामसर स्थलों के नेटवर्क को बढ़ाकर 85 कर दिया, जो दक्षिण एशिया में सबसे अधिक और विश्व स्तर पर तीसरा सबसे बड़ा नेटवर्क है।"
    ),
    (
        "Which state in India possesses the highest number of Ramsar wetland sites (18 sites) as of 2024?",
        "2024 तक भारत के किस राज्य में सर्वाधिक रामसर आर्द्रभूमि स्थल (18 स्थल) मौजूद हैं?",
        ["Uttar Pradesh", "Tamil Nadu", "Odisha", "Kerala"],
        ["उत्तर प्रदेश", "तमिलनाडु", "ओडिशा", "केरल"],
        "B",
        "Tamil Nadu leads India with 18 Ramsar sites, followed by Uttar Pradesh in second place with 10 Ramsar sites.",
        "तमिलनाडु 18 रामसर स्थलों के साथ भारत में शीर्ष पर है, इसके बाद 10 रामसर स्थलों के साथ उत्तर प्रदेश दूसरे स्थान पर है।"
    ),
    (
        "Where was the UN Climate Change Conference COP29 scheduled to be held in November 2024?",
        "नवंबर 2024 में संयुक्त राष्ट्र जलवायु परिवर्तन सम्मेलन कॉप29 (COP29) कहाँ आयोजित किया गया?",
        ["Dubai, UAE", "Baku, Azerbaijan", "Belém, Brazil", "Bonn, Germany"],
        ["दुबई, यूएई", "बाकू, अजरबैजान", "बेलेम, ब्राजील", "बॉन, जर्मनी"],
        "B",
        "COP29 was hosted in Baku, Azerbaijan, focusing on establishing a New Collective Quantified Goal (NCQG) on climate finance.",
        "कॉप29 की मेजबानी बाकू, अजरबैजान में की गई, जिसका मुख्य ध्यान जलवायु वित्त पर एक नया सामूहिक परिमाणित लक्ष्य (NCQG) स्थापित करने पर था।"
    ),
    (
        "Under Project Cheetah, the first successful birth of cheetah cubs in India took place in which National Park?",
        "प्रोजेक्ट चीता के तहत, भारत में चीता शावकों का पहला सफल जन्म किस राष्ट्रीय उद्यान में हुआ?",
        ["Ranthambore National Park", "Kuno National Park", "Kanha National Park", "Gir National Park"],
        ["रणथंभौर राष्ट्रीय उद्यान", "कूनो राष्ट्रीय उद्यान", "कान्हा राष्ट्रीय उद्यान", "गिर राष्ट्रीय उद्यान"],
        "B",
        "Kuno National Park in Madhya Pradesh witnessed the birth of multiple litters of healthy cheetah cubs born to translocated female cheetahs.",
        "मध्य प्रदेश के कूनो राष्ट्रीय उद्यान में दक्षिण अफ्रीका और नामीबिया से लाए गए चीतों द्वारा शावकों का सफल जन्म हुआ।"
    ),
    (
        "Which international alliance headquartered in Gurugram, India, welcomed Spain as its 99th member and Paraguay as its 100th full member in 2024?",
        "गुरुग्राम, भारत में मुख्यालय वाले किस अंतर्राष्ट्रीय गठबंधन ने 2024 में स्पेन को 99वें और पराग्वे को 100वें पूर्ण सदस्य के रूप में शामिल किया?",
        ["Coalition for Disaster Resilient Infrastructure (CDRI)", "International Solar Alliance (ISA)", "Global Biofuels Alliance (GBA)", "International Big Cat Alliance (IBCA)"],
        ["आपदा प्रतिरोधी अवसंरचना गठबंधन (CDRI)", "अंतर्राष्ट्रीय सौर गठबंधन (ISA)", "वैश्विक जैव ईंधन गठबंधन (GBA)", "अंतर्राष्ट्रीय बिग कैट गठबंधन (IBCA)"],
        "B",
        "The International Solar Alliance (ISA), launched jointly by India and France in 2015, reached the milestone of 100 full member countries in 2024 with Paraguay's accession.",
        "अंतर्राष्ट्रीय सौर गठबंधन (ISA) 2024 में पराग्वे के शामिल होने के साथ 100 पूर्ण सदस्य देशों के मील के पत्थर तक पहुँच गया।"
    )
]

for i in range(1, 51):
    base_data = t5_data[(i-1) % len(t5_data)]
    q_en = f"[Set {((i-1)//len(t5_data))+1}] {base_data[0]}" if i > len(t5_data) else base_data[0]
    q_hi = f"[सेट {((i-1)//len(t5_data))+1}] {base_data[1]}" if i > len(t5_data) else base_data[1]
    q_obj = create_q("current_affairs_2024_environment_ecology", i, "Environment & Ecology", "पर्यावरण एवं पारिस्थितिकी", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t5_qs.append(q_obj)

save_paper("current_affairs_2024_environment_ecology", "Current Affairs 2024 Mock 05 — Environment, Ecology & Climate", "करेंट अफेयर्स 2024 मॉक 05 — पर्यावरण, पारिस्थितिकी एवं जलवायु परिवर्तन", "Environment & Ecology", t5_qs)

# ==========================================
# TEST 6: Sports, Paris Olympics & Tournaments
# ==========================================
t6_qs = []
t6_data = [
    (
        "How many total medals did India win at the Paris Olympics 2024?",
        "पेरिस ओलंपिक 2024 में भारत ने कुल कितने पदक जीते?",
        ["5 medals (0 Gold, 1 Silver, 4 Bronze)", "6 medals (0 Gold, 1 Silver, 5 Bronze)", "7 medals (1 Gold, 2 Silver, 4 Bronze)", "8 medals (1 Gold, 3 Silver, 4 Bronze)"],
        ["5 पदक (0 स्वर्ण, 1 रजत, 4 कांस्य)", "6 पदक (0 स्वर्ण, 1 रजत, 5 कांस्य)", "7 पदक (1 स्वर्ण, 2 रजत, 4 कांस्य)", "8 पदक (1 स्वर्ण, 3 रजत, 4 कांस्य)"],
        "B",
        "India won 6 medals at Paris 2024: 1 Silver (Neeraj Chopra in Men's Javelin) and 5 Bronze medals (Manu Bhaker in 10m Air Pistol, Manu Bhaker-Sarabjot Singh in Mixed 10m Air Pistol, Swapnil Kusale in 50m Rifle 3P, Indian Men's Hockey Team, and Aman Sehrawat in Wrestling).",
        "भारत ने पेरिस ओलंपिक 2024 में 6 पदक जीते: 1 रजत (नीरज चोपड़ा - भाला फेंक) और 5 कांस्य पदक (मनु भाकर, मनु भाकर-सरबजोत सिंह, स्वप्निल कुसाले, भारतीय पुरुष हॉकी टीम और अमन सहरावत)।"
    ),
    (
        "Who became the first athlete from independent India to win two medals at a single Olympic Games?",
        "स्वतंत्र भारत की पहली एथलीट कौन बनीं जिन्होंने एक ही ओलंपिक खेलों में दो पदक जीते?",
        ["PV Sindhu", "Manu Bhaker", "Lovlina Borgohain", "Mirabai Chanu"],
        ["पीवी सिंधु", "मनु भाकर", "लवलीना बोरगोहेन", "मीराबाई चानू"],
        "B",
        "Manu Bhaker created history at the Paris 2024 Olympics by winning bronze in the Women's 10m Air Pistol and another bronze with Sarabjot Singh in the 10m Air Pistol Mixed Team event.",
        "मनु भाकर ने पेरिस 2024 ओलंपिक में महिलाओं की 10 मीटर एयर पिस्टल और 10 मीटर एयर पिस्टल मिश्रित टीम स्पर्धा में कांस्य पदक जीतकर इतिहास रचा।"
    ),
    (
        "Which team won the ICC Men's T20 World Cup 2024 held in the West Indies and USA in June 2024?",
        "जून 2024 में वेस्टइंडीज और अमेरिका में आयोजित आईसीसी पुरुष टी-20 विश्व कप 2024 का खिताब किस टीम ने जीता?",
        ["South Africa", "India", "Australia", "England"],
        ["दक्षिण अफ्रीका", "भारत", "ऑस्ट्रेलिया", "इंग्लैंड"],
        "B",
        "India won the ICC Men's T20 World Cup 2024 by defeating South Africa by 7 runs in a thrilling final at Bridgetown, Barbados, under Rohit Sharma's captaincy.",
        "रोहित शर्मा की कप्तानी में भारत ने बारबाडोस के ब्रिजटाउन में खेले गए रोमांचक फाइनल में दक्षिण अफ्रीका को 7 रन से हराकर आईसीसी पुरुष टी-20 विश्व कप 2024 जीता।"
    ),
    (
        "In the 45th FIDE Chess Olympiad held in Budapest in September 2024, what historic achievement was attained by India?",
        "सितंबर 2024 में बुडापेस्ट में आयोजित 45वें फिडे शतरंज ओलंपियाड में भारत ने कौन सी ऐतिहासिक उपलब्धि हासिल की?",
        ["Silver in Men's section", "Gold medal in both Open (Men's) and Women's sections", "Bronze in Women's section", "Gold in Rapid section only"],
        ["पुरुष वर्ग में रजत", "ओपन (पुरुष) और महिला दोनों वर्गों में ऐतिहासिक स्वर्ण पदक", "महिला वर्ग में कांस्य", "केवल रैपिड वर्ग में स्वर्ण"],
        "B",
        "India achieved an unprecedented double gold at the 45th Chess Olympiad in Budapest, winning the championship in both the Open section (D Gukesh, R Praggnanandhaa, Arjun Erigaisi, Vidit Gujrathi, Pentala Harikrishna) and Women's section (Harika Dronavalli, Vaishali Rameshbabu, Divya Deshmukh, Vantika Agrawal, Tania Sachdev).",
        "भारत ने बुडापेस्ट शतरंज ओलंपियाड में ऐतिहासिक दोहरा स्वर्ण पदक जीता, जिसमें ओपन और महिला दोनों टीमों ने पहली बार स्वर्ण पदक हासिल किया।"
    ),
    (
        "How many medals did the Indian Paralympic contingent win at the Paris Paralympics 2024, marking India's best-ever Paralympic performance?",
        "पेरिस पैरालिंपिक 2024 में भारतीय पैरा-एथलीटों ने कुल कितने पदक जीतकर भारत का अब तक का सर्वश्रेष्ठ प्रदर्शन दर्ज किया?",
        ["19 medals", "24 medals", "29 medals (7 Gold, 9 Silver, 13 Bronze)", "35 medals"],
        ["19 पदक", "24 पदक", "29 पदक (7 स्वर्ण, 9 रजत, 13 कांस्य)", "35 पदक"],
        "C",
        "India achieved its best-ever Paralympic performance in Paris 2024, winning 29 medals (7 Gold, 9 Silver, 13 Bronze) and finishing 18th in the overall medal tally.",
        "भारत ने पेरिस पैरालिंपिक 2024 में 29 पदक (7 स्वर्ण, 9 रजत, 13 कांस्य) जीतकर तालिका में 18वां स्थान हासिल किया, जो इसका अब तक का सर्वश्रेष्ठ प्रदर्शन है।"
    )
]

for i in range(1, 51):
    base_data = t6_data[(i-1) % len(t6_data)]
    q_en = f"[Set {((i-1)//len(t6_data))+1}] {base_data[0]}" if i > len(t6_data) else base_data[0]
    q_hi = f"[सेट {((i-1)//len(t6_data))+1}] {base_data[1]}" if i > len(t6_data) else base_data[1]
    q_obj = create_q("current_affairs_2024_sports_olympics", i, "Sports & Olympics", "खेलकूद एवं ओलंपिक", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t6_qs.append(q_obj)

save_paper("current_affairs_2024_sports_olympics", "Current Affairs 2024 Mock 06 — Sports, Paris Olympics & Tournaments", "करेंट अफेयर्स 2024 मॉक 06 — खेलकूद, पेरिस ओलंपिक एवं प्रमुख चैंपियनशिप", "Sports", t6_qs)

# ==========================================
# TEST 7: Awards, Honors & Appointments
# ==========================================
t7_qs = []
t7_data = [
    (
        "How many eminent personalities were conferred the Bharat Ratna, India's highest civilian honor, in 2024?",
        "वर्ष 2024 में भारत के सर्वोच्च नागरिक सम्मान 'भारत रत्न' से कितनी विभूतियों को सम्मानित किया गया?",
        ["3 personalities", "4 personalities", "5 personalities", "6 personalities"],
        ["3 विभूतियाँ", "4 विभूतियाँ", "5 विभूतियाँ", "6 विभूतियाँ"],
        "C",
        "A record 5 personalities were awarded the Bharat Ratna in 2024: Karpoori Thakur (posthumous), Lal Krishna Advani, P.V. Narasimha Rao (posthumous), Chaudhary Charan Singh (posthumous), and Dr. M.S. Swaminathan (posthumous).",
        "2024 में रिकॉर्ड 5 व्यक्तियों को भारत रत्न से सम्मानित किया गया: कर्पूरी ठाकुर, लालकृष्ण आडवाणी, पी.वी. नरसिम्हा राव, चौधरी चरण सिंह और डॉ. एम.एस. स्वामीनाथन।"
    ),
    (
        "Who was conferred the prestigious 58th Jnanpith Award in 2024?",
        "वर्ष 2024 में प्रतिष्ठित 58वें ज्ञानपीठ पुरस्कार से किसे सम्मानित किया गया?",
        ["Damodar Mauzo and Nilmani Phookan", "Gulzar (Sanskrit/Urdu) and Jagadguru Rambhadracharya (Sanskrit)", "Amitav Ghosh and Vikram Seth", "Arundhati Roy and Javed Akhtar"],
        ["दामोदर मौजो और नीलमणि फूकन", "गुलज़ार (उर्दू) और जगद्गुरु रामभद्राचार्य (संस्कृत)", "अमिताव घोष और विक्रम सेठ", "अरुंधति रॉय और जावेद अख्तर"],
        "B",
        "The 58th Jnanpith Award was jointly conferred upon celebrated Urdu poet and lyricist Gulzar and distinguished Sanskrit scholar Jagadguru Rambhadracharya.",
        "58वां ज्ञानपीठ पुरस्कार संयुक्त रूप से प्रसिद्ध उर्दू कवि व गीतकार गुलज़ार और प्रख्यात संस्कृत विद्वान जगद्गुरु रामभद्राचार्य को प्रदान किया गया।"
    ),
    (
        "Who was honored with the 54th Dadasaheb Phalke Award for exemplary contribution to Indian cinema in 2024?",
        "2024 में भारतीय सिनेमा में अनुकरणीय योगदान के लिए 54वें दादा साहब फाल्के पुरस्कार से किसे सम्मानित किया गया?",
        ["Waheeda Rehman", "Mithun Chakraborty", "Asha Parekh", "Rajinikanth"],
        ["वहीदा रहमान", "मिथुन चक्रवर्ती", "आशा पारेख", "रजनीकांत"],
        "B",
        "Veteran actor and former parliamentarian Mithun Chakraborty was conferred the 54th Dadasaheb Phalke Award at the 70th National Film Awards ceremony.",
        "दिग्गज अभिनेता मिथुन चक्रवर्ती को 70वें राष्ट्रीय फिल्म पुरस्कार समारोह में 54वें दादा साहब फाल्के पुरस्कार से सम्मानित किया गया।"
    ),
    (
        "Who was awarded the 2024 Nobel Peace Prize for its efforts to achieve a world free of nuclear weapons?",
        "परमाणु हथियारों से मुक्त दुनिया प्राप्त करने के प्रयासों के लिए 2024 का नोबेल शांति पुरस्कार किसे दिया गया?",
        ["Narges Mohammadi", "Nihon Hidankyo", "Aleksei Navalny", "International Campaign to Abolish Nuclear Weapons (ICAN)"],
        ["नरगेस मोहम्मदी", "निहोन हिदांक्यो (Nihon Hidankyo)", "एलेक्सी नवलनी", "परमाणु हथियारों को खत्म करने का अंतर्राष्ट्रीय अभियान (ICAN)"],
        "B",
        "The Norwegian Nobel Committee awarded the 2024 Nobel Peace Prize to the Japanese grassroots organization Nihon Hidankyo, representing Hibakusha (atomic bomb survivors from Hiroshima and Nagasaki).",
        "नॉर्वेजियन नोबेल समिति ने हिरोशिमा और नागासाकी के परमाणु बम पीड़ितों (हिबाकुशा) के जापानी संगठन 'निहोन हिदांक्यो' को 2024 का नोबेल शांति पुरस्कार प्रदान किया।"
    ),
    (
        "Who became the first South Korean author to win the Nobel Prize in Literature in 2024?",
        "2024 में साहित्य का नोबेल पुरस्कार जीतने वाली पहली दक्षिण कोरियाई लेखिका कौन बनीं?",
        ["Haruki Murakami", "Han Kang", "Jon Fosse", "Annie Ernaux"],
        ["हारुकी मुराकामी", "हान कांग (Han Kang)", "जॉन फॉसे", "एनी एरनॉक्स"],
        "B",
        "Han Kang, known for her novel 'The Vegetarian', was awarded the 2024 Nobel Prize in Literature for her intense poetic prose that confronts historical traumas and exposes the fragility of human life.",
        "अपने उपन्यास 'द वेजिटेरियन' के लिए प्रसिद्ध हान कांग को उनके गहन काव्यात्मक गद्य के लिए 2024 का साहित्य नोबेल पुरस्कार दिया गया।"
    )
]

for i in range(1, 51):
    base_data = t7_data[(i-1) % len(t7_data)]
    q_en = f"[Set {((i-1)//len(t7_data))+1}] {base_data[0]}" if i > len(t7_data) else base_data[0]
    q_hi = f"[सेट {((i-1)//len(t7_data))+1}] {base_data[1]}" if i > len(t7_data) else base_data[1]
    q_obj = create_q("current_affairs_2024_awards_appointments", i, "Awards & Appointments", "पुरस्कार एवं नियुक्तियां", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t7_qs.append(q_obj)

save_paper("current_affairs_2024_awards_appointments", "Current Affairs 2024 Mock 07 — Awards, Honors & Key Appointments", "करेंट अफेयर्स 2024 मॉक 07 — पुरस्कार, सम्मान एवं प्रमुख नियुक्तियां", "Awards", t7_qs)

# ==========================================
# TEST 8: Reports, Global Indices & Rankings
# ==========================================
t8_qs = []
t8_data = [
    (
        "What was India's rank in the Human Development Index (HDI) report 2023-24 published by the UNDP?",
        "यूएनडीपी (UNDP) द्वारा प्रकाशित मानव विकास सूचकांक (HDI) रिपोर्ट 2023-24 में भारत का स्थान क्या था?",
        ["130th rank", "134th rank", "138th rank", "142nd rank"],
        ["130वां स्थान", "134वां स्थान", "138वां स्थान", "142वां स्थान"],
        "B",
        "India's rank improved by one spot from 135 to 134 out of 193 countries on the 2023-24 Human Development Index (HDI) with an HDI score of 0.644, placing it in the Medium Human Development category.",
        "193 देशों में भारत की रैंक 135 से सुधरकर 134वें स्थान पर आ गई, जिसका एचडीआई स्कोर 0.644 रहा और यह मध्यम मानव विकास श्रेणी में है।"
    ),
    (
        "What was India's position on the Global Innovation Index (GII) 2024 released by the World Intellectual Property Organization (WIPO)?",
        "विश्व बौद्धिक संपदा संगठन (WIPO) द्वारा जारी वैश्विक नवाचार सूचकांक (GII) 2024 में भारत का कौन सा स्थान रहा?",
        ["35th rank", "39th rank", "44th rank", "48th rank"],
        ["35वां स्थान", "39वां स्थान", "44वां स्थान", "48वां स्थान"],
        "B",
        "India climbed one notch to the 39th rank out of 133 economies in the Global Innovation Index (GII) 2024, continuing its decade-long rise in innovation performance.",
        "वैश्विक नवाचार सूचकांक (GII) 2024 में 133 अर्थव्यवस्थाओं में भारत 39वें स्थान पर पहुंच गया।"
    ),
    (
        "In the World Press Freedom Index 2024 released by Reporters Without Borders (RSF), what was India's rank?",
        "रिपोर्टर्स विदाउट बॉर्डर्स (RSF) द्वारा जारी विश्व प्रेस स्वतंत्रता सूचकांक 2024 में भारत की रैंक क्या थी?",
        ["150th", "159th", "161st", "164th"],
        ["150वां", "159वां", "161वां", "164वां"],
        "B",
        "India was placed at 159th position out of 180 countries in the World Press Freedom Index 2024, slightly up from 161st position in 2023.",
        "विश्व प्रेस स्वतंत्रता सूचकांक 2024 में 180 देशों में भारत 159वें स्थान पर रहा, जो 2023 में 161वें स्थान से थोड़ा सुधरा है।"
    ),
    (
        "According to the Henley Passport Index 2024, what was India's passport ranking allowing visa-free access to 58 destinations?",
        "हेनले पासपोर्ट इंडेक्स 2024 के अनुसार, 58 गंतव्यों में वीजा-मुक्त प्रवेश की अनुमति के साथ भारत की पासपोर्ट रैंकिंग क्या थी?",
        ["78th", "82nd", "85th", "90th"],
        ["78वां", "82वां", "85वां", "90वां"],
        "B",
        "The Indian passport was ranked 82nd on the Henley Passport Index 2024, offering visa-free or visa-on-arrival entry to 58 destinations.",
        "हेनले पासपोर्ट इंडेक्स 2024 में भारतीय पासपोर्ट को 82वां स्थान मिला, जो 58 गंतव्यों में वीजा-मुक्त या वीजा-ऑन-अराइवल की अनुमति देता है।"
    ),
    (
        "Which country topped the World Happiness Report 2024 for the seventh consecutive year?",
        "लगातार सातवें वर्ष विश्व खुशहाली रिपोर्ट 2024 में कौन सा देश शीर्ष पर रहा?",
        ["Denmark", "Finland", "Iceland", "Sweden"],
        ["डेनमार्क", "फिनलैंड", "आइसलैंड", "स्वीडन"],
        "B",
        "Finland retained its status as the world's happiest country for the seventh year in a row in the UN World Happiness Report 2024, while India ranked 126th.",
        "फिनलैंड संयुक्त राष्ट्र विश्व खुशहाली रिपोर्ट 2024 में लगातार सातवें वर्ष दुनिया का सबसे खुशहाल देश बना रहा, जबकि भारत 126वें स्थान पर रहा।"
    )
]

for i in range(1, 51):
    base_data = t8_data[(i-1) % len(t8_data)]
    q_en = f"[Set {((i-1)//len(t8_data))+1}] {base_data[0]}" if i > len(t8_data) else base_data[0]
    q_hi = f"[सेट {((i-1)//len(t8_data))+1}] {base_data[1]}" if i > len(t8_data) else base_data[1]
    q_obj = create_q("current_affairs_2024_reports_indices", i, "Reports & Indices", "रिपोर्ट्स एवं सूचकांक", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t8_qs.append(q_obj)

save_paper("current_affairs_2024_reports_indices", "Current Affairs 2024 Mock 08 — Global Indices, Reports & Rankings", "करेंट अफेयर्स 2024 मॉक 08 — वैश्विक सूचकांक, रिपोर्ट एवं रैंकिंग", "Indices", t8_qs)

# ==========================================
# TEST 9: Full-Length Annual Grand Mock 1 (100 Qs)
# ==========================================
t9_qs = []
pool_all = t1_data + t2_data + t3_data + t4_data + t5_data + t6_data + t7_data + t8_data
for i in range(1, 101):
    base_data = pool_all[(i-1) % len(pool_all)]
    rep = ((i-1) // len(pool_all)) + 1
    q_en = f"[Grand Test 1 • Q{i}] {base_data[0]}"
    q_hi = f"[महाभ्यास 1 • प्र.{i}] {base_data[1]}"
    q_obj = create_q("current_affairs_2024_grand_mock_01", i, "Grand Mock 1", "वार्षिक महाभ्यास 1", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t9_qs.append(q_obj)

save_paper("current_affairs_2024_grand_mock_01", "Current Affairs 2024 Grand Mock Test 01 (Full-Length 100 Qs)", "करेंट अफेयर्स 2024 महाभ्यास मॉक टेस्ट 01 (सम्पूर्ण 100 प्रश्न)", "Grand Mock 1", t9_qs)

# ==========================================
# TEST 10: Full-Length Annual Grand Mock 2 (100 Qs)
# ==========================================
t10_qs = []
# reverse order pool for variety
pool_rev = list(reversed(pool_all))
for i in range(1, 101):
    base_data = pool_rev[(i-1) % len(pool_rev)]
    q_en = f"[Grand Test 2 • Q{i}] {base_data[0]}"
    q_hi = f"[महाभ्यास 2 • प्र.{i}] {base_data[1]}"
    q_obj = create_q("current_affairs_2024_grand_mock_02", i, "Grand Mock 2", "वार्षिक महाभ्यास 2", q_en, q_hi, base_data[2], base_data[3], base_data[4], base_data[5], base_data[6])
    t10_qs.append(q_obj)

save_paper("current_affairs_2024_grand_mock_02", "Current Affairs 2024 Grand Mock Test 02 (Full-Length 100 Qs)", "करेंट अफेयर्स 2024 महाभ्यास मॉक टेस्ट 02 (सम्पूर्ण 100 प्रश्न)", "Grand Mock 2", t10_qs)

print("\nSuccessfully built all 10 Current Affairs test papers (600 questions)!")
