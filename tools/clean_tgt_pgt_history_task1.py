import glob
import json
import os
import re

DIR = "tests/teaching/tgt_pgt_history"

# 1. Exact 12 split/both-placeholder questions
FIX_12_QUESTIONS = {
    ("tgt_pgt_hist_ch06_gupta_post_gupta.json", 217): {
        "questionTextHi": "निम्नलिखित में से किस प्राचीन स्मृतिकार ने उत्तराधिकार के सम्बन्ध में विधवाओं को पुत्र के बाद स्थान दिया है?",
        "questionTextEn": "Which of the following ancient lawgivers gave widows a place after sons in matters of inheritance?",
        "optionsHi": ["याज्ञवल्क्य", "मनु", "बृहस्पति", "कात्यायन"],
        "optionsEn": ["Yajnavalkya", "Manu", "Brihaspati", "Katyayana"],
        "correctOption": "A",
        "explanationHi": "प्राचीन स्मृतिकार याज्ञवल्क्य ने स्त्री उत्तराधिकार का वर्णन किया है। उन्होंने सम्पत्ति में स्त्री के अधिकार को स्पष्ट किया है तथा विधवा स्त्री को पुत्र के बाद उत्तराधिकारी माना है।",
        "explanationEn": "Ancient lawgiver Yajnavalkya described female inheritance. He clarified women's rights in property and recognized widows as heirs right after sons."
    },
    ("tgt_pgt_hist_ch07_chola_period.json", 45): {
        "questionTextHi": "चोलों के स्थानीय स्वायत्तशाली ग्राम प्रशासन की जानकारी उत्तरमेरूर अभिलेख से होती है। इस अभिलेख का संबंध किस चोल शासक से है?",
        "questionTextEn": "Information about the local autonomous village administration of the Cholas is known from the Uttaramerur inscription. This inscription is associated with which Chola ruler?",
        "optionsHi": ["राजराज प्रथम", "विजयालय", "सुन्दर चोल", "परान्तक I"],
        "optionsEn": ["Rajaraja I", "Vijayalaya", "Sundara Chola", "Parantaka I"],
        "correctOption": "D",
        "explanationHi": "परान्तक प्रथम (907-955 ई.) के उत्तरमेरूर अभिलेख से चोलों के स्वायत्त ग्रामीण प्रशासन और सभा की कार्यप्रणाली की विस्तृत जानकारी मिलती है।",
        "explanationEn": "The Uttaramerur inscription of Parantaka I (907–955 AD) provides detailed information on the autonomous village administration and Sabha functioning of the Cholas."
    },
    ("tgt_pgt_hist_ch10_delhi_sultanate.json", 50): {
        "questionTextHi": "अपनी मृत्यु के पूर्व बलबन ने किसको अपना उत्तराधिकारी मनोनीत किया था?",
        "questionTextEn": "Whom did Balban nominate as his successor before his death?",
        "optionsHi": ["मुहम्मद (कैखुसरो)", "फखरुद्दीन", "बुगरा खान", "कैकुबाद"],
        "optionsEn": ["Muhammad (Kaikhusrau)", "Fakhruddin", "Bughra Khan", "Kaikubad"],
        "correctOption": "A",
        "explanationHi": "अपनी मृत्यु से पूर्व बलबन ने अपने पौत्र कैखुसरो (शहीद शहजादा मुहम्मद के पुत्र) को अपना उत्तराधिकारी नियुक्त किया था। किन्तु बलबन की मृत्यु के बाद दिल्ली के कोतवाल फखरुद्दीन मुहम्मद ने षड्यंत्र रचकर कैकुबाद को गद्दी पर बैठाया।",
        "explanationEn": "Before his death, Balban had nominated his grandson Kaikhusrau (son of Prince Muhammad) as his successor. However, after Balban's death, Kotwal Fakhruddin enthroned Kaikubad."
    },
    ("tgt_pgt_hist_ch10_delhi_sultanate.json", 229): {
        "questionTextHi": "निम्नलिखित कथनों पर विचार कीजिए–\nअभिकथन (A) : बलबन के राजत्व का सिद्धान्त 'रक्त और लौह' की नीति पर आधारित था।\nकारण (R) : ताज की प्रतिष्ठा इल्तुतमिश के उत्तराधिकारियों के अधीन घटी थी।\nनिम्नलिखित कूट से इस प्रश्न का सही उत्तर दीजिए :",
        "questionTextEn": "Consider the following statements:\nAssertion (A): Balban's theory of kingship was based on the policy of 'Blood and Iron'.\nReason (R): The prestige of the Crown had declined under the successors of Iltutmish.\nSelect the correct answer from the code below:",
        "optionsHi": [
            "(A) सही है, (R) गलत है।",
            "(A) और (R) दोनों सही हैं, और (R), (A) का सही स्पष्टीकरण है।",
            "(A) सही है, परन्तु (R) गलत है।",
            "(A) गलत है, परन्तु (R) सही है।"
        ],
        "optionsEn": [
            "(A) is true, but (R) is false.",
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "(A) is true, but (R) is false and not the explanation.",
            "(A) is false, but (R) is true."
        ],
        "correctOption": "B",
        "explanationHi": "बलबन का राजत्व सिद्धान्त 'रक्त और लौह' की नीति पर आधारित था। इल्तुतमिश के कमजोर उत्तराधिकारियों के काल में ताज की प्रतिष्ठा नष्ट हो गई थी, जिसे बलबन ने कठोर नियमों और आतंक से पुनर्स्थापित किया। अतः (A) और (R) दोनों सही हैं तथा (R), (A) का सही स्पष्टीकरण है।",
        "explanationEn": "Balban's theory of kingship rested on 'Blood and Iron'. The prestige of the crown had severely degraded under Iltutmish's weak successors, which Balban restored through strict court etiquette and absolute authority. Thus both are true and (R) correctly explains (A)."
    },
    ("tgt_pgt_hist_ch11_mughal_empire.json", 60): {
        "questionTextHi": "निम्न में से किसे शाहजहाँ ने सितम्बर 1657 में अपनी बीमारी के कारण औपचारिक रूप से अपना उत्तराधिकारी मनोनीत किया?",
        "questionTextEn": "Whom among the following did Shah Jahan formally nominate as his successor in September 1657 due to his illness?",
        "optionsHi": ["दारा शिकोह", "शुजा", "औरंगजेब", "मुराद"],
        "optionsEn": ["Dara Shikoh", "Shuja", "Aurangzeb", "Murad"],
        "correctOption": "A",
        "explanationHi": "शाहजहाँ के बीमार होने पर उसने सितम्बर 1657 में अपने ज्येष्ठ पुत्र दारा शिकोह को अपना औपचारिक उत्तराधिकारी घोषित किया था, जिसके फलस्वरूप उत्तराधिकार का युद्ध छिड़ गया।",
        "explanationEn": "When Shah Jahan fell critically ill in September 1657, he formally nominated his eldest son Dara Shikoh as his successor, which triggered the war of succession among his sons."
    },
    ("tgt_pgt_hist_ch11_mughal_empire.json", 216): {
        "questionTextHi": "ईरान से आया रफीउद्दीन शिराजी लिखता है कि, ''मैं (आगरा में) भीड़ के बीच तम्बू के बने घेरे में खड़ा था, तभी अचानक आवाज गूँजी 'खुदा राजा की रक्षा करे।' मैंने समझा कि राजा आ गया है... उन्होंने उत्तर दिया कि दरबारियों के लिए शिष्टाचार बहुत ज्यादा हैं, परन्तु राजा स्वयं सबसे ज्यादा अनौपचारिक है।'' निम्नलिखित में से किस शासक के बारे में शिराजी ने यह लिखा है?",
        "questionTextEn": "Rafiuddin Shirazi from Iran writes: 'I was standing in Agra amidst the crowd... They replied that court etiquette is strict for courtiers, but the King himself is the most informal.' Regarding which ruler did Shirazi write this?",
        "optionsHi": ["अकबर", "जहाँगीर", "जहांदार शाह", "मोहम्मद शाह रंगीला"],
        "optionsEn": ["Akbar", "Jahangir", "Jahandar Shah", "Muhammad Shah Rangeela"],
        "correctOption": "A",
        "explanationHi": "रफीउद्दीन शिराजी ने अकबर के बारे में लिखा कि वह अपने साथियों और अजनबियों के बीच कोई भेद नहीं करता था तथा अत्यधिक अनौपचारिक स्वभाव का था।",
        "explanationEn": "Rafiuddin Shirazi recorded this description of Akbar, remarking on Akbar's unusually accessible and informal demeanor with common people."
    },
    ("tgt_pgt_hist_ch11_mughal_empire.json", 220): {
        "questionTextHi": "''इस बादशाह ने स्थानीय और अन्य अधिकारियों से यात्रियों तथा व्यापारियों को क्षति नहीं पहुँचाने और यदि कोई व्यापारी दुर्घटना में बिना उत्तराधिकारी के मर जाता है तो उसकी संपत्ति नहीं हड़पने का आदेश दिया।'' यह कथन किस शासक से संबंधित है?",
        "questionTextEn": "'This emperor ordered local officers not to harm travellers and merchants, and if any merchant died in an accident without an heir, not to seize his property.' Which ruler does this refer to?",
        "optionsHi": ["शेरशाह", "अकबर", "जहाँगीर", "शाहजहाँ"],
        "optionsEn": ["Sher Shah", "Akbar", "Jahangir", "Shah Jahan"],
        "correctOption": "A",
        "explanationHi": "शेरशाह सूरी ने व्यापारियों एवं यात्रियों की सुरक्षा हेतु कड़े नियम बनाए थे। बिना वारिस लावारिस मृतक की संपत्ति हड़पने पर पाबंदी थी और स्थानीय अधिकारियों को उनकी सुरक्षा के लिए जिम्मेदार बनाया गया था।",
        "explanationEn": "Sher Shah Suri enacted strict regulations for the protection of merchants and travelers, forbidding confiscation of heirless property and holding local officials accountable."
    },
    ("tgt_pgt_hist_ch11_mughal_empire.json", 401): {
        "questionTextHi": "विदेशी यात्री जिसने दारा शिकोह एवं औरंगजेब के मध्य हुए उत्तराधिकार-युद्ध को देखा था, वह कौन था?",
        "questionTextEn": "Who was the foreign traveller who witnessed the war of succession between Dara Shikoh and Aurangzeb?",
        "optionsHi": ["फ्रांस्वा बर्नियर", "निकोलो मनूची", "ट्रैवर्नियर", "थॉमस रो"],
        "optionsEn": ["François Bernier", "Niccolao Manucci", "Tavernier", "Thomas Roe"],
        "correctOption": "A",
        "explanationHi": "फ्रांसीसी चिकित्सक और यात्री फ्रांस्वा बर्नियर (François Bernier) ने 1658 में दारा शिकोह और औरंगजेब के मध्य उत्तराधिकार के युद्ध को प्रत्यक्ष रूप से देखा था। वह कुछ समय तक दारा शिकोह का चिकित्सक भी रहा।",
        "explanationEn": "French physician and traveller François Bernier directly witnessed the Mughal war of succession between Dara Shikoh and Aurangzeb, and served briefly as Dara's physician."
    },
    ("tgt_pgt_hist_ch11_mughal_empire.json", 499): {
        "questionTextHi": "निम्नलिखित में से कौन एक हुमायूँ के स्थान पर बाबर के उत्तराधिकारी के रूप में प्रधानमंत्री मीर खलीफा की पसंद था?",
        "questionTextEn": "Who among the following was the choice of Prime Minister Mir Khalifa as Babur's successor in place of Humayun?",
        "optionsHi": ["मिर्जा कामरान", "मेहदी ख्वाजा", "मिर्जा अस्करी", "मिर्जा हिंदाल"],
        "optionsEn": ["Mirza Kamran", "Mehdi Khwaja", "Mirza Askari", "Mirza Hindal"],
        "correctOption": "B",
        "explanationHi": "बाबर के प्रधानमंत्री मीर खलीफा हुमायूँ को अयोग्य मानते थे और उसकी जगह बाबर के बहनोई मेहदी ख्वाजा को गद्दी पर बैठाना चाहते थे, किन्तु बाद में यह योजना विफल हो गई।",
        "explanationEn": "Babur's prime minister, Mir Nizamuddin Khalifa, initially favored Babur's brother-in-law Mehdi Khwaja to succeed him over Humayun, though the conspiracy later collapsed."
    },
    ("tgt_pgt_hist_ch16_east_india_company.json", 5): {
        "questionTextHi": "उत्तर अठारहवीं सदी के हैदराबादी शासन प्रणाली को 'संरक्षक-आश्रित संबंध' के रूप में देखा जा सकता है, क्योंकि–",
        "questionTextEn": "The 18th-century Hyderabadi administrative system can be viewed as a 'patron-client relationship' because:",
        "optionsHi": [
            "निजाम ने अपनी निष्ठा मुगल बादशाह के प्रति दर्शाई और उसे लगातार नजराना देता रहा।",
            "स्थानीय हिन्दू जमींदारों को निजाम द्वारा दबा कर रखा जाता था और उन्हें नजराना देने के लिए बाध्य किया जाता था।",
            "हैदराबाद राज्य के अर्ध-स्वायत्त शासकों को अपनी मर्जी से शासन चलाने की स्वतंत्रता थी और बदले में उन्हें निजाम को वार्षिक नजराना देना होता था।",
            "स्थानीय कुलीन मुस्लिम लोग निजाम और मुगलों के प्रति अपनी निष्ठा का प्रदर्शन करते थे।"
        ],
        "optionsEn": [
            "The Nizam pledged loyalty to the Mughal emperor and consistently paid tribute.",
            "Local Hindu zamindars were suppressed by the Nizam and coerced into paying peshkash.",
            "Semi-autonomous rulers within Hyderabad had autonomy to govern in exchange for regular tribute to the Nizam.",
            "Local Muslim elites demonstrated allegiance to both the Nizam and Mughal rulers."
        ],
        "correctOption": "C",
        "explanationHi": "हैदराबाद में निजाम-उल-मुल्क आसफजाह और उनके उत्तराधिकारियों ने स्थानीय समस्थनों व सरदारों को आंतरिक स्वायत्तता दी और बदले में वार्षिक नजराना (पेशकश) लिया, जो संरक्षक-आश्रित संबंध का प्रारूप था।",
        "explanationEn": "The Nizams of Hyderabad allowed subordinate chieftains internal autonomy in exchange for annual tribute (peshkash), epitomizing a classic patron-client relationship."
    },
    ("tgt_pgt_hist_ch20_19th_century_renaissance.json", 245): {
        "questionTextHi": "ईसाई धर्म में धर्मान्तरित हिन्दुओं को पैतृक सम्पत्ति में उत्तराधिकार प्राप्त करने में सक्षम बनाने वाला अधिनियम कौन-सा था?",
        "questionTextEn": "Which act enabled Hindu converts to Christianity to inherit their ancestral property?",
        "optionsHi": ["एक्ट XXI, 1850 (लेक्स लोकी अधिनियम)", "एक्ट XXII, 1850", "एक्ट XXIII, 1850", "एक्ट XXIV, 1850"],
        "optionsEn": ["Act XXI of 1850 (Caste Disabilities Removal / Lex Loci Act)", "Act XXII of 1850", "Act XXIII of 1850", "Act XXIV of 1850"],
        "correctOption": "A",
        "explanationHi": "धार्मिक अयोग्यता निवारण अधिनियम (एक्ट XXI, 1850 / Lex Loci Act) द्वारा यह प्रावधान किया गया कि धर्म परिवर्तन करने पर भी व्यक्ति को पैतृक सम्पत्ति के उत्तराधिकार से वंचित नहीं किया जा सकता।",
        "explanationEn": "The Caste Disabilities Removal Act (Act XXI of 1850 / Lex Loci Act) ensured that conversion to Christianity did not deprive an individual of rights to ancestral property inheritance."
    },
    ("tgt_pgt_hist_ch24_post_independence.json", 22): {
        "questionTextHi": "इनमें से किस मामले पर सर्वोच्च न्यायालय द्वारा दिया गया निर्णय, लिंग की परवाह किए बिना संपत्ति के उत्तराधिकार के समान अधिकारों से संबंधित है?",
        "questionTextEn": "Which Supreme Court judgment established equal inheritance rights to property regardless of gender?",
        "optionsHi": ["मेरी रॉय बनाम केरल राज्य", "श्रेया सिंघल बनाम भारत संघ", "विशाखा बनाम राजस्थान राज्य", "लिली थॉमस बनाम भारत संघ"],
        "optionsEn": ["Mary Roy v. State of Kerala", "Shreya Singhal v. Union of India", "Vishaka v. State of Rajasthan", "Lily Thomas v. Union of India"],
        "correctOption": "A",
        "explanationHi": "1986 में मेरी रॉय बनाम केरल राज्य मामले में सर्वोच्च न्यायालय ने ऐतिहासिक निर्णय देते हुए त्रावणकोर क्रिश्चियन सक्सेशन एक्ट को निरस्त किया और सीरियन क्रिश्चियन महिलाओं को पैतृक संपत्ति में भाइयों के बराबर अधिकार प्रदान किया।",
        "explanationEn": "In Mary Roy v. State of Kerala (1986), the Supreme Court struck down provisions of the Travancore Christian Succession Act, granting Syrian Christian women equal rights in ancestral property."
    }
}

# 2. Specific fixes for the 38 En-only placeholder questions
FIX_38_QUESTIONS = {
    ("tgt_pgt_hist_ch01_prehistoric_cultures.json", 55): {
        "optionsHi": ["ऑस्ट्रेलिया की मुंगो झील", "बोरनेओ की नियाह गुफा", "इजराइल में कफजेह का कपाल", "मोरक्को में डर-एस-सोल्टन"],
        "optionsEn": ["Lake Mungo in Australia", "Niah Cave in Borneo", "Skull of Qafzeh in Israel", "Dar es-Soltan in Morocco"]
    },
    ("tgt_pgt_hist_ch02_indus_valley.json", 71): {
        "optionsHi": ["हाथी", "गैंडा", "बाघ", "बैल"],
        "optionsEn": ["Elephant", "Rhinoceros", "Tiger", "Bull"]
    },
    ("tgt_pgt_hist_ch02_indus_valley.json", 155): {
        "optionsHi": ["महाराष्ट्र", "गुजरात", "आंध्र प्रदेश", "उत्तर प्रदेश"],
        "optionsEn": ["Maharashtra", "Gujarat", "Andhra Pradesh", "Uttar Pradesh"]
    },
    ("tgt_pgt_hist_ch02_indus_valley.json", 193): {
        "optionsHi": ["एकशृंगी", "वृषभ", "गैंडा", "गज"],
        "optionsEn": ["Unicorn", "Bull", "Rhinoceros", "Elephant"]
    },
    ("tgt_pgt_hist_ch03_vedic_period.json", 92): {
        "optionsHi": ["रुद्र", "मारुत", "अग्नि", "इन्द्र"],
        "optionsEn": ["Rudra", "Marut", "Agni", "Indra"]
    },
    ("tgt_pgt_hist_ch03_vedic_period.json", 101): {
        "optionsHi": ["अग्नि", "वरुण", "मित्र", "इन्द्र"],
        "optionsEn": ["Agni", "Varuna", "Mitra", "Indra"]
    },
    ("tgt_pgt_hist_ch03_vedic_period.json", 155): {
        "optionsHi": ["विष्णु", "कृष्ण", "इन्द्र", "ब्रह्मा"],
        "optionsEn": ["Vishnu", "Krishna", "Indra", "Brahma"]
    },
    ("tgt_pgt_hist_ch04_jain_buddha_mahajanapada.json", 6): {
        "questionTextHi": "सूची-I के साथ सूची-II का मिलान कीजिए:\nसूची-I (ध्यानी बुद्ध): (A) अमिताभ (B) अक्षोभ्य (C) वैरोचन (D) अमोघसिद्धि\nसूची-II (उनके बोधिसत्व): (I) वज्रपाणि (II) पद्मपाणि (III) विश्वपाणि (IV) समन्तभद्र",
        "questionTextEn": "Match List-I with List-II:\nList-I (Dhyani Buddha): (A) Amitabha (B) Akshobhya (C) Vairochana (D) Amoghasiddhi\nList-II (Their Bodhisattvas): (I) Vajrapani (II) Padmapani (III) Vishvapani (IV) Samantabhadra",
        "optionsHi": [
            "(A)-(I), (B)-(II), (C)-(III), (D)-(IV)",
            "(A)-(II), (B)-(I), (C)-(IV), (D)-(III)",
            "(A)-(III), (B)-(II), (C)-(I), (D)-(IV)",
            "(A)-(IV), (B)-(III), (C)-(II), (D)-(I)"
        ],
        "optionsEn": [
            "(A)-(I), (B)-(II), (C)-(III), (D)-(IV)",
            "(A)-(II), (B)-(I), (C)-(IV), (D)-(III)",
            "(A)-(III), (B)-(II), (C)-(I), (D)-(IV)",
            "(A)-(IV), (B)-(III), (C)-(II), (D)-(I)"
        ]
    },
    ("tgt_pgt_hist_ch04_jain_buddha_mahajanapada.json", 81): {
        "optionsHi": ["भद्रबाहु", "कुन्दकुन्द", "स्थूलभद्र", "यशोभद्र"],
        "optionsEn": ["Bhadrabahu", "Kundakunda", "Sthulabhadra", "Yashobhadra"]
    },
    ("tgt_pgt_hist_ch04_jain_buddha_mahajanapada.json", 252): {
        "optionsHi": ["हरिहर", "महेश्वर", "अर्द्धनारीश्वर", "विष्णुलोकेश्वर"],
        "optionsEn": ["Harihara", "Maheshwara", "Ardhanarishvara", "Vishnulokeshwara"]
    },
    ("tgt_pgt_hist_ch05_mauryan_post_mauryan.json", 211): {
        "optionsHi": ["तमिलनाडु", "कर्नाटक", "महाराष्ट्र", "आन्ध्र"],
        "optionsEn": ["Tamil Nadu", "Karnataka", "Maharashtra", "Andhra"]
    },
    ("tgt_pgt_hist_ch06_gupta_post_gupta.json", 30): {
        "optionsHi": ["क्षेमेन्द्र", "कालिदास", "अमर सिंह", "लक्ष्मीधर"],
        "optionsEn": ["Kshemendra", "Kalidasa", "Amar Singh", "Lakshmidhara"]
    },
    ("tgt_pgt_hist_ch06_gupta_post_gupta.json", 45): {
        "questionTextHi": "सूची-I (शासक) को सूची-II (शिलालेख) से सुमेलित कीजिए तथा दिये गये कूट में से सही उत्तर दीजिए –\nसूची-I (शासक): (A) कुमारगुप्त I (B) कुमारगुप्त II (C) बुद्धगुप्त (D) परान्तक II\nसूची-II (शिलालेख): (i) उत्तरमेरूर शिलालेख (ii) बिलसद शिलालेख (iii) सारनाथ शिलालेख (iv) एरण शिलालेख",
        "questionTextEn": "Match List-I (Ruler) with List-II (Inscription) and select the correct answer from the code below:\nList-I (Ruler): (A) Kumaragupta I (B) Kumaragupta II (C) Buddhagupta (D) Parantaka II\nList-II (Inscription): (i) Uttaramerur Inscription (ii) Bilsad Inscription (iii) Sarnath Inscription (iv) Eran Inscription",
        "optionsHi": [
            "(A)-(ii), (B)-(iii), (C)-(iv), (D)-(i)",
            "(A)-(iii), (B)-(iv), (C)-(ii), (D)-(i)",
            "(A)-(iv), (B)-(iii), (C)-(ii), (D)-(i)",
            "(A)-(i), (B)-(ii), (C)-(iii), (D)-(iv)"
        ],
        "optionsEn": [
            "(A)-(ii), (B)-(iii), (C)-(iv), (D)-(i)",
            "(A)-(iii), (B)-(iv), (C)-(ii), (D)-(i)",
            "(A)-(iv), (B)-(iii), (C)-(ii), (D)-(i)",
            "(A)-(i), (B)-(ii), (C)-(iii), (D)-(iv)"
        ]
    },
    ("tgt_pgt_hist_ch06_gupta_post_gupta.json", 66): {
        "optionsHi": ["चन्द्रवर्मा", "विजय बाहु", "महेन्द्र", "मेघवर्ण"],
        "optionsEn": ["Chandravarman", "Vijayabahu", "Mahendra", "Meghavarna"]
    },
    ("tgt_pgt_hist_ch08_foreign_invasions.json", 53): {
        "optionsHi": ["नायकी देवी", "विनयावती", "महादेवी", "रुद्रमा देवी"],
        "optionsEn": ["Nayaki Devi", "Vinayavati", "Mahadevi", "Rudrama Devi"]
    },
    ("tgt_pgt_hist_ch09_ancient_misc.json", 40): {
        "optionsHi": ["दामोदरगुप्त", "लक्ष्मीधर", "महेन्द्रवर्मा", "देवगण"],
        "optionsEn": ["Damodaragupta", "Lakshmidhara", "Mahendravarman", "Devagana"]
    },
    ("tgt_pgt_hist_ch09_ancient_misc.json", 107): {
        "optionsHi": ["राष्ट्र", "महाद्वीप", "संस्कृति", "सभ्यता"],
        "optionsEn": ["Nation", "Continent", "Culture", "Civilization"]
    },
    ("tgt_pgt_hist_ch09_ancient_misc.json", 360): {
        "optionsHi": ["सिद्धों का एक मठ", "एक बौद्ध ग्रन्थ", "एक जैन देवी", "एक प्रकार की भारतीय वर्णमाला"],
        "optionsEn": ["A monastery of Siddhas", "A Buddhist text", "A Jain goddess", "A type of Indian alphabet"]
    },
    ("tgt_pgt_hist_ch10_delhi_sultanate.json", 108): {
        "optionsHi": ["इल्तुतमिश", "बलबन", "अलाउद्दीन खिलजी", "फिरोज शाह तुगलक"],
        "optionsEn": ["Iltutmish", "Balban", "Alauddin Khilji", "Firoz Shah Tughlaq"]
    },
    ("tgt_pgt_hist_ch10_delhi_sultanate.json", 302): {
        "optionsHi": ["कन्नौज का युद्ध", "तराइन का द्वितीय युद्ध", "पानीपत का युद्ध", "खानवा का युद्ध"],
        "optionsEn": ["Battle of Kannauj", "Second Battle of Tarain", "Battle of Panipat", "Battle of Khanwa"]
    },
    ("tgt_pgt_hist_ch11_mughal_empire.json", 131): {
        "optionsHi": ["यशोभद्रा", "हरिविजय सूरी", "चन्द्रप्रभा सूरी", "पुष्पदन्त"],
        "optionsEn": ["Yashobhadra", "Harivijaya Suri", "Chandraprabha Suri", "Pushpadanta"]
    },
    ("tgt_pgt_hist_ch11_mughal_empire.json", 177): {
        "optionsHi": ["रुद्र चन्द", "बाजबहादुर चंद", "ज्ञान चंद", "कीर्ति चंद"],
        "optionsEn": ["Rudra Chand", "Baz Bahadur Chand", "Gyan Chand", "Kirti Chand"]
    },
    ("tgt_pgt_hist_ch12_bahmani_vijayanagara_maratha.json", 93): {
        "questionTextHi": "सूची-I को सूची-II से सुमेलित करें तथा अधोलिखित कूट से अपना उत्तर चुनिये–\nसूची-I: (A) सदाशिव (B) संगम वंश (C) राम राय (D) अमुक्तमाल्यद\nसूची-II: (W) अरविदु वंश (X) देव राय I (Y) कृष्ण देव राय (Z) तालीकोट का युद्ध",
        "questionTextEn": "Match List-I with List-II and select the correct answer from the code below:\nList-I: (A) Sadashiva (B) Sangama Dynasty (C) Rama Raya (D) Amuktamalyada\nList-II: (W) Aravidu Dynasty (X) Deva Raya I (Y) Krishna Deva Raya (Z) Battle of Talikota",
        "optionsHi": [
            "(A)-Z, (B)-X, (C)-W, (D)-Y",
            "(A)-X, (B)-Z, (C)-W, (D)-Y",
            "(A)-Y, (B)-Z, (C)-Z, (D)-W",
            "(A)-W, (B)-X, (C)-Y, (D)-Z"
        ],
        "optionsEn": [
            "(A)-Z, (B)-X, (C)-W, (D)-Y",
            "(A)-X, (B)-Z, (C)-W, (D)-Y",
            "(A)-Y, (B)-Z, (C)-Z, (D)-W",
            "(A)-W, (B)-X, (C)-Y, (D)-Z"
        ]
    },
    ("tgt_pgt_hist_ch13_medieval_culture.json", 251): {
        "optionsHi": ["कर्नाटक", "महाराष्ट्र", "केरल", "दिल्ली"],
        "optionsEn": ["Karnataka", "Maharashtra", "Kerala", "Delhi"]
    },
    ("tgt_pgt_hist_ch16_east_india_company.json", 104): {
        "optionsHi": ["फॉक्स क्राफ्ट", "स्ट्रेन्शम मास्टर", "गेराल्ड औंगीर", "चार्ल्स बून"],
        "optionsEn": ["Foxcroft", "Streynsham Master", "Gerald Aungier", "Charles Boone"]
    },
    ("tgt_pgt_hist_ch18_modern_education_constitution.json", 57): {
        "optionsHi": ["सर जॉन क्लेवरिंग", "कर्नल मानसन", "लेमेस्टर", "रिचर्ड बारवेल"],
        "optionsEn": ["Sir John Clavering", "Colonel Monson", "Mons. Lemaitre", "Richard Barwell"]
    },
    ("tgt_pgt_hist_ch19_revolt_1857.json", 80): {
        "questionTextHi": "सूची I को सूची II से सुमेलित कीजिए तथा नीचे दिये गये कूट से सही उत्तर का चयन कीजिए:\nसूची I: (A) लक्ष्मीबाई (B) तात्यां टोपे (C) नाना साहब (D) बहादुर शाह\nसूची II: 1. रंगून निर्वासित 2. नेपाल निर्वासित 3. गिरफ्तार हुए और फांसी पर लटकाये गये 4. युद्ध में मारी गयीं",
        "questionTextEn": "Match List I with List II and select the correct answer from the code below:\nList I: (A) Lakshmibai (B) Tatya Tope (C) Nana Saheb (D) Bahadur Shah\nList II: 1. Exiled to Rangoon 2. Exiled to Nepal 3. Arrested and hanged 4. Killed in battle",
        "optionsHi": [
            "(A)-1, (B)-2, (C)-3, (D)-4",
            "(A)-2, (B)-3, (C)-1, (D)-4",
            "(A)-4, (B)-3, (C)-2, (D)-1",
            "(A)-4, (B)-2, (C)-3, (D)-1"
        ],
        "optionsEn": [
            "(A)-1, (B)-2, (C)-3, (D)-4",
            "(A)-2, (B)-3, (C)-1, (D)-4",
            "(A)-4, (B)-3, (C)-2, (D)-1",
            "(A)-4, (B)-2, (C)-3, (D)-1"
        ]
    },
    ("tgt_pgt_hist_ch20_19th_century_renaissance.json", 128): {
        "optionsHi": ["राजस्थान", "महाराष्ट्र", "गुजरात", "पंजाब"],
        "optionsEn": ["Rajasthan", "Maharashtra", "Gujarat", "Punjab"]
    },
    ("tgt_pgt_hist_ch21_national_movement.json", 379): {
        "optionsHi": ["गुजरात", "मध्य प्रदेश", "महाराष्ट्र", "उड़ीसा"],
        "optionsEn": ["Gujarat", "Madhya Pradesh", "Maharashtra", "Orissa"]
    },
    ("tgt_pgt_hist_ch25_governors_viceroys.json", 40): {
        "optionsHi": ["द कलकत्ता म्युनिसिपल अमेंडमेंट एक्ट", "इण्डियन यूनिवर्सिटीज एक्ट", "इण्डियन ऑफिशियल सीक्रेट्स अमेंडमेंट एक्ट", "वर्नाक्युलर प्रेस एक्ट"],
        "optionsEn": ["The Calcutta Municipal Amendment Act", "Indian Universities Act", "Indian Official Secrets Amendment Act", "Vernacular Press Act"]
    },
    ("tgt_pgt_hist_ch28_modern_misc.json", 166): {
        "optionsHi": ["तमिलनाडु", "पश्चिम बंगाल", "महाराष्ट्र", "केरल"],
        "optionsEn": ["Tamil Nadu", "West Bengal", "Maharashtra", "Kerala"]
    },
    ("tgt_pgt_hist_ch29_research.json", 65): {
        "optionsHi": ["उपयोगितावादी", "साम्राज्यवादी", "उपाश्रयी", "राष्ट्रवादी"],
        "optionsEn": ["Utilitarians", "Imperialists", "Subaltern", "Nationalists"]
    },
    ("tgt_pgt_hist_ch30_world_history.json", 13): {
        "optionsHi": ["अमरीका", "इंग्लैण्ड", "फ्रांस", "इटली"],
        "optionsEn": ["America", "England", "France", "Italy"]
    },
    ("tgt_pgt_hist_ch30_world_history.json", 51): {
        "optionsHi": ["निचिरेन", "हायाशी रजान", "एन्निन", "फुजिवारा सीका"],
        "optionsEn": ["Nichiren", "Hayashi Razan", "Ennin", "Fujiwara Seika"]
    },
    ("tgt_pgt_hist_ch30_world_history.json", 154): {
        "optionsHi": ["वियना का युद्ध", "कॉन्स्टेंटिनोपल का घेरा", "चालदिरान का युद्ध", "अंकारा का युद्ध"],
        "optionsEn": ["Battle of Vienna", "Siege of Constantinople", "Battle of Chaldiran", "Battle of Ankara"]
    },
    ("tgt_pgt_hist_ch30_world_history.json", 185): {
        "optionsHi": ["कोरियाई युद्ध", "काजामार्का का युद्ध", "वियतनाम युद्ध", "अफगान गृहयुद्ध"],
        "optionsEn": ["Korean War", "Battle of Cajamarca", "Vietnam War", "Afghan Civil War"]
    },
    ("tgt_pgt_hist_ch30_world_history.json", 240): {
        "optionsHi": ["साम्प्रदायिकतावाद", "रंगभेद", "राष्ट्रवाद", "फासीवाद"],
        "optionsEn": ["Communalism", "Apartheid", "Nationalism", "Fascism"]
    },
    ("tgt_pgt_hist_ch30_world_history.json", 257): {
        "optionsHi": ["वर्जीनिया", "मैरीलैंड", "जॉर्जिया", "कनेक्टिकट"],
        "optionsEn": ["Virginia", "Maryland", "Georgia", "Connecticut"]
    }
}

# 3. Global Text Replacements (Hindi)
HINDI_REPLACEMENTS = [
    # Typos & OCR artifacts
    ("किसाने", "किसने"),
    ("तिरुkegâjue", "तिरुक्कुरल"),
    ("तिरुkjue", "तिरुक्कुरल"),
    ("kegâjue", "तिरुक्कुरल"),
    ("vÙetÙeeke&â", "न्यूयॉर्क"),
    ("vÙet", "न्यू"),
    ("Sce.के.", "एम.के."),
    ("Sce.", "एम."),
    ("KeejJesue", "खारवेल"),
    ("nwJesue", "हैवेल"),
    ("हैJesue", "हैवेल"),
    ("Jesue", "वेल"),
    ("ceneje<š", "महाराष्ट्र"),
    ("ceneje„", "महाराष्ट्र"),
    ("Fbiueै[", "इंग्लैण्ड"),
    ("Fšueer", "इटली"),
    ("ieै[e", "गैंडा"),
    ("neथाr", "हाथी"),
    ("Fbद्र", "इन्द्र"),
    ("jbieYeso", "रंगभेद"),
    ("cewjerueै[", "मैरीलैंड"),
    ("je<šJeeoer", "राष्ट्रवादी"),
    ("mšsÙeMeece", "स्ट्रेन्शम"),
    ("uesceemšs", "लेमेस्टर"),
    ("कVौज", "कन्नौज"),
    ("ÙeMeesYeद्रe", "यशोभद्रा"),
    ("ÙeMeesYeद्र", "यशोभद्र"),
    ("censvद्रJecee&", "महेन्द्रवर्मा"),
    ("censvद्र", "महेन्द्र"),
    ("रूद्र Ûebद्र", "रुद्र चन्द"),
    ("रूद्रccee osJeer", "रुद्रमा देवी"),
    ("शिकाiees", "शिकागो"),
    ("अं«ोजों", "अंग्रेजों"),
    ("अं«ोज", "अंग्रेज"),
    ("«न्थों", "ग्रन्थों"),
    ("«न्थ", "ग्रन्थ"),
    ("«ंथों", "ग्रंथों"),
    ("«ंथ", "ग्रंथ"),
    ("वि«ह", "विग्रह"),
    ("आqग्न", "अग्नि"),
    ("qस्थत", "स्थित"),
    ("शहबुöीन", "शहाबुद्दीन"),
    ("पखरुöीन", "फखरुद्दीन"),
    ("कैक्ुबाद", "कैकुबाद"),
    ("रपीउöीन", "रफीउद्दीन"),
    ("शिरा]जी", "शिराजी"),
    ("बा|नयर", "बर्नियर"),
    ("ह्त्या", "हत्या"),
    ("मह्त्व", "महत्व"),
    ("मह्म्मद", "मोहम्मद"),
    ("दराशिकोह", "दारा शिकोह"),
    ("बहद्ुर", "बहादुर"),
    ("महत्मा", "महात्मा"),
    ("ह्र्ष", "हर्ष"),
    ("क््रष्ण", "कृष्ण"),
    ("त्र+ग्वेद", "ऋग्वेद"),
    ("त्र+चाएं", "ऋचाएं"),
    ("त्र+चाआें", "ऋचाओं"),
    ("विÅालय", "विद्यालय"),
    ("बुfद्ध", "बुद्धि"),
    ("बुfद्धमान", "बुद्धिमान"),
    ("अपùत", "अपहृत"),
    ("सवाxच्च", "सर्वोच्च"),
    ("परि्डनेण्ड", "फर्डिनेंड"),
]

# 4. Global Text Replacements (English)
ENGLISH_REPLACEMENTS = [
    # Residual Kruti strings in English fields
    ("tirukegâjue", "Tirukkural"),
    ("kegâjue", "Tirukkural"),
    ("vÙetÙeeke&â", "New York"),
    ("vÙet", "New"),
    ("Sce.के.", "M.K."),
    ("Sce.", "M."),
    ("KeejJesue", "Kharavela"),
    ("nwJesue", "Havell"),
    ("Lord Jesuespueer", "Lord Wellesley"),
    ("neueJesue", "Holwell"),
    ("[sवि[ nJesue", "David Hare"),
    ("JewJesue योजना", "Wavell Plan"),
    ("Lord JesJesue", "Lord Wavell"),
    ("SÛe.SÛe. [es[Jesue", "H.H. Dodwell"),
    ("Nikasuees cewkiÙeeJesueer", "Niccolo Machiavelli"),
    ("निकाsuees cewकिÙeeJesueer", "Niccolo Machiavelli"),
    ("Jesue", "Well"),
    ("ceneje<š", "Maharashtra"),
    ("ceneje„", "Maharashtra"),
    ("Fbiueै[", "England"),
    ("Fšueer", "Italy"),
    ("jbieyeso", "Apartheid"),
    ("cewjerueै[", "Maryland"),
    ("je<šJeeoer", "Nationalist"),
    ("mšsÙeMeece", "Streynsham"),
    ("uesceemšs", "Lemaitre"),
    ("ÙeMeesYeद्रe", "Yashobhadra"),
    ("ÙeMeesYeद्र", "Yashobhadra"),
    ("censvद्रJecee&", "Mahendravarman"),
    ("censvद्र", "Mahendra"),
    ("रूद्र Ûebद्र", "Rudra Chand"),
    ("रूद्रccee osJeer", "Rudrama Devi"),
    ("शिकाiees", "Chicago"),
    # Bogus eggs -> British
    ("asked eggs to leave", "asked the British to leave"),
    ("against eggs", "against the British"),
    ("sold eggs to the Nawab", "sold Bengal to the British"),
    ("sell eggs in 1790", "sell Penang Island to the British in 1790"),
    ("help the eggs", "help the British"),
]

def clean_hindi_text(text):
    if not isinstance(text, str):
        return text
    for old, new in HINDI_REPLACEMENTS:
        text = text.replace(old, new)
    return text

def clean_english_text(text, is_question_stem=False, is_farmer_related=False):
    if not isinstance(text, str):
        return text
    for old, new in ENGLISH_REPLACEMENTS:
        text = text.replace(old, new)

    # Fix bogus farmer in question stems
    if is_question_stem and not is_farmer_related:
        text = re.sub(r'\bWhich of the following farmers\b', 'Who among the following', text, flags=re.I)
        text = re.sub(r'\bWho among the following farmers\b', 'Who among the following', text, flags=re.I)
        text = re.sub(r'\bWhich farmers\b', 'Who', text, flags=re.I)
        text = re.sub(r'\bWhich farmer\b', 'Who', text, flags=re.I)
        text = re.sub(r'\bThe farmer had given\b', 'Who gave', text, flags=re.I)
        text = re.sub(r'\bThe farmers had said\b', 'Who had said', text, flags=re.I)
        text = re.sub(r'\bThe farmers said\b', 'Who said', text, flags=re.I)
        text = re.sub(r'\bThe farmer said\b', 'Who said', text, flags=re.I)
        text = re.sub(r'\bFarmer wrote\b', 'Who wrote', text, flags=re.I)
        text = re.sub(r'\bFarmer published\b', 'Who published', text, flags=re.I)
        text = re.sub(r'\bFarmer had made\b', 'Who made', text, flags=re.I)
        text = re.sub(r'\bFarmers had made\b', 'Who made', text, flags=re.I)
        text = re.sub(r'\bFarmers call\b', 'Who called', text, flags=re.I)
        text = re.sub(r'\bFarmers coined\b', 'Who coined', text, flags=re.I)
        text = re.sub(r'\bFarmers stopped\b', 'Who stopped', text, flags=re.I)
        text = re.sub(r'\bFarmer had issued\b', 'Who had issued', text, flags=re.I)
        text = re.sub(r'\bFarmer established\b', 'Who established', text, flags=re.I)
        text = re.sub(r'\bFarmer founded\b', 'Who founded', text, flags=re.I)
        text = re.sub(r'\bDid the farmers get\b', 'Who got', text, flags=re.I)
        text = re.sub(r'\bDid the farmers help\b', 'Who helped', text, flags=re.I)
        text = re.sub(r'\bDid farmers recognize\b', 'Who recognized', text, flags=re.I)
        text = re.sub(r'\bDid farmers reject\b', 'Who rejected', text, flags=re.I)
        text = re.sub(r'\bAmong these, farmers wrote\b', 'Among these, who wrote', text, flags=re.I)
        text = re.sub(r'\bThese farmers had said\b', 'Who had said', text, flags=re.I)
        text = re.sub(r'\bShould these farmers say\b', 'Who said', text, flags=re.I)
        text = re.sub(r'\bHave farmers referred\b', 'Who referred', text, flags=re.I)
        text = re.sub(r'\bFor the first time, farmers got\b', 'Who for the first time got', text, flags=re.I)
        text = re.sub(r'\bby which farmer\b', 'by whom', text, flags=re.I)
        text = re.sub(r'\bto which farmer\b', 'to whom', text, flags=re.I)
        text = re.sub(r'\bWhere did Penang Dwarp farmers sell eggs in 1790\b', 'Who sold Penang Island to the British in 1790', text, flags=re.I)

    return text

def is_peasant_movement_question(qhi):
    # Check if this question is legitimately about farmers/peasants
    keywords = ['किसान आन्दोलन', 'किसान आंदोलन', 'कृषक', 'किसानों', 'किसान सभा', 'चम्पारण', 'बारदोली', 'बटाईदार', 'नील आन्दोलन', 'रैयत', 'बिजोलिया']
    return any(k in qhi for k in keywords)

def run():
    files = sorted(glob.glob(f"{DIR}/tgt_pgt_hist_ch*.json"))
    print(f"Processing {len(files)} files...")

    total_questions = 0
    total_12_fixed = 0
    total_38_fixed = 0

    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as fp:
            data = json.load(fp)

        questions = data.get("questions", [])
        total_questions += len(questions)

        for q in questions:
            qnum = q.get("questionNumber")
            key = (fname, qnum)

            # 1. Check if it's one of the 12 split questions
            if key in FIX_12_QUESTIONS:
                fix = FIX_12_QUESTIONS[key]
                q["questionTextHi"] = fix["questionTextHi"]
                q["questionTextEn"] = fix["questionTextEn"]
                q["optionsHi"] = fix["optionsHi"]
                q["optionsEn"] = fix["optionsEn"]
                q["correctOption"] = fix["correctOption"]
                q["explanationHi"] = fix["explanationHi"]
                q["explanationEn"] = fix["explanationEn"]
                total_12_fixed += 1

            # 2. Check if it's one of the 38 En-only questions
            elif key in FIX_38_QUESTIONS:
                fix = FIX_38_QUESTIONS[key]
                if "questionTextHi" in fix:
                    q["questionTextHi"] = fix["questionTextHi"]
                if "questionTextEn" in fix:
                    q["questionTextEn"] = fix["questionTextEn"]
                q["optionsHi"] = fix["optionsHi"]
                q["optionsEn"] = fix["optionsEn"]
                total_38_fixed += 1

            # 3. Clean Hindi fields
            q["questionTextHi"] = clean_hindi_text(q.get("questionTextHi", ""))
            q["optionsHi"] = [clean_hindi_text(opt) for opt in q.get("optionsHi", [])]
            q["explanationHi"] = clean_hindi_text(q.get("explanationHi", ""))

            # 4. Clean English fields
            is_peasant = is_peasant_movement_question(q.get("questionTextHi", ""))
            q["questionTextEn"] = clean_english_text(q.get("questionTextEn", ""), is_question_stem=True, is_farmer_related=is_peasant)
            q["optionsEn"] = [clean_english_text(opt) for opt in q.get("optionsEn", [])]
            q["explanationEn"] = clean_english_text(q.get("explanationEn", ""), is_question_stem=False, is_farmer_related=is_peasant)

            # 5. Synchronize dual camelCase & snake_case schema
            opt_map = {"A": 0, "B": 1, "C": 2, "D": 3}
            ans_str = q.get("correctOption", "A")
            corr_idx = opt_map.get(ans_str, 0)

            q["correct_index"] = corr_idx
            q["correct_indices"] = [corr_idx]
            q["q_number"] = qnum
            q["question_en"] = q["questionTextEn"]
            q["question_hi"] = q["questionTextHi"]
            q["options_en"] = q["optionsEn"]
            q["options_hi"] = q["optionsHi"]
            q["explanation_en"] = q["explanationEn"]
            q["explanation_hi"] = q["explanationHi"]

        with open(fpath, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)

    print(f"Task 1 completed successfully!")
    print(f"Total questions processed: {total_questions}")
    print(f"12 both-placeholder questions fixed: {total_12_fixed}")
    print(f"38 En-placeholder questions fixed: {total_38_fixed}")

if __name__ == "__main__":
    run()
