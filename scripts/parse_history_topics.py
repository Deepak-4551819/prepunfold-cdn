import pymupdf
import re
import json

pdf_path = r'C:\Users\yedde\Downloads\Ghatnachakra History 2024_ (1)(1).pdf'
doc = pymupdf.open(pdf_path)

txt = doc[2].get_text()

# Let's extract chapters from the index text
lines = txt.split('\n')

parts = [
    ("part1_ancient_history", "Part I: Ancient History of India", "भाग I: प्राचीन भारत का इतिहास", []),
    ("part2_medieval_history", "Part II: Medieval History of India", "भाग II: मध्यकालीन भारत का इतिहास", []),
    ("part3_modern_history", "Part III: Modern History of India", "भाग III: आधुनिक भारत का इतिहास", [])
]

# We know the chapter lists from page 3:
# Ancient History: Chapters 1 to 15
ancient_raw = [
    (1, "Stone Age", "पाषाण काल", 9, 16),
    (2, "Indus Valley Civilization", "सिंधु घाटी सभ्यता", 16, 31),
    (3, "Vedic Age", "वैदिक काल", 32, 47),
    (4, "Buddhism", "बौद्ध धर्म", 47, 68),
    (5, "Jain Religion", "जैन धर्म", 68, 78),
    (6, "Shaiva and Bhagavata Religion", "शैव एवं भागवत धर्म", 78, 84),
    (7, "Sixth Century B.C.E - Political Condition", "छठी शताब्दी ई.पू. - राजनीतिक दशा (महाजनपद काल)", 84, 94),
    (8, "Greek Invasion", "यूनानी आक्रमण", 94, 96),
    (9, "Maurya Empire", "मौर्य साम्राज्य", 96, 116),
    (10, "Post-Mauryan Period", "मौर्योत्तर काल", 116, 126),
    (11, "Gupta and Post-Gupta Period", "गुप्त एवं गुप्तोत्तर काल", 126, 151),
    (12, "Architecture in Ancient India", "प्राचीन भारत में स्थापत्य कला", 151, 165),
    (13, "South India (Chola, Chalukya, Pallava and Sangam Period)", "दक्षिण भारत (चोल, चालुक्य, पल्लव एवं संगम काल)", 165, 178),
    (14, "Ancient Literature and Litterateur", "प्राचीन साहित्य एवं साहित्यकार", 178, 189),
    (15, "Pre-Medieval Period", "पूर्व-मध्य काल", 189, 198)
]

# Medieval History: Chapters 1 to 25
medieval_raw = [
    (1, "Muslim Invasion of India", "भारत पर मुस्लिम आक्रमण", 199, 205),
    (2, "Delhi Sultanate: Slave Dynasty", "दिल्ली सल्तनत: गुलाम वंश", 205, 211),
    (3, "Delhi Sultanate: Khalji Dynasty", "दिल्ली सल्तनत: खिलजी वंश", 211, 217),
    (4, "Delhi Sultanate: Tughluq Dynasty", "दिल्ली सल्तनत: तुगलक वंश", 217, 224),
    (5, "Delhi Sultanate: Lodi Dynasty", "दिल्ली सल्तनत: लोदी वंश", 225, 226),
    (6, "Vijayanagara Empire", "विजयनगर साम्राज्य", 227, 233),
    (7, "Delhi Sultanate: Administration", "दिल्ली सल्तनत: प्रशासन", 233, 238),
    (8, "Delhi Sultanate: Art and Architecture", "दिल्ली सल्तनत: कला एवं स्थापत्य", 238, 240),
    (9, "Delhi Sultanate: Literature", "दिल्ली सल्तनत: साहित्य", 240, 246),
    (10, "Delhi Sultanate: Miscellaneous", "दिल्ली सल्तनत: विविध", 246, 251),
    (11, "Provincial Dynasty of North India and Deccan", "उत्तर भारत एवं दक्कन के प्रांतीय राजवंश", 251, 257),
    (12, "Bhakti and Sufi Movement", "भक्ति एवं सूफी आंदोलन", 257, 271),
    (13, "Mughal Dynasty: Babur", "मुगल वंश: बाबर", 271, 276),
    (14, "Mughal Dynasty: Humayun and Sher Shah", "हुमायूं एवं शेरशाह", 276, 280),
    (15, "Mughal Dynasty: Akbar", "मुगल वंश: अकबर", 280, 293),
    (16, "Mughal Dynasty: Jahangir", "मुगल वंश: जहांगीर", 293, 297),
    (17, "Mughal Dynasty: Shah Jahan", "मुगल वंश: शाहजहां", 298, 301),
    (18, "Mughal Dynasty: Aurangzeb", "मुगल वंश: औरंगजेब", 302, 306),
    (19, "Mughal Administration", "मुगल प्रशासन", 306, 311),
    (20, "Music and Paintings of Mughal Period", "मुगलकालीन संगीत एवं चित्रकला", 311, 315),
    (21, "Mughal Literature", "मुगलकालीन साहित्य", 315, 319),
    (22, "Mughal Period: Miscellaneous", "मुगल काल: विविध", 319, 326),
    (23, "Sikh Sect", "सिख संप्रदाय", 326, 329),
    (24, "Maratha State and Confederacy", "मराठा राज्य एवं संघ", 329, 335),
    (25, "Disintegration of the Mughal Empire", "मुगल साम्राज्य का विघटन", 336, 339)
]

# Modern History: Chapters 1 to 55
modern_raw = [
    (1, "Advent of European Companies", "यूरोपीय कंपनियों का आगमन", 340, 350),
    (2, "East India Company and Nawab of Bengal", "ईस्ट इंडिया कंपनी और बंगाल के नवाब", 350, 355),
    (3, "Regional States: Punjab and Mysore", "क्षेत्रीय राज्य: पंजाब एवं मैसूर", 355, 359),
    (4, "Governor, Governor-General and Viceroy", "गवर्नर, गवर्नर जनरल एवं वायसराय", 359, 379),
    (5, "Economic Impact of British Rule on India", "ब्रिटिश शासन का भारतीय अर्थव्यवस्था पर प्रभाव", 379, 387),
    (6, "Revolt of 1857", "1857 का विद्रोह", 387, 401),
    (7, "Other Civil and Tribal Uprisings", "अन्य जन आंदोलन एवं जनजातीय विद्रोह", 401, 415),
    (8, "Development of Education in Modern India", "आधुनिक भारत में शिक्षा का विकास", 415, 422),
    (9, "Development of Press in Modern India", "आधुनिक भारत में प्रेस का विकास", 422, 433),
    (10, "Social and Religious Reform Movements", "सामाजिक एवं धार्मिक सुधार आंदोलन", 433, 455),
    (11, "Political Organisations Established before Congress", "कांग्रेस से पूर्व स्थापित राजनीतिक संस्थाएं", 455, 460),
    (12, "Indian National Congress", "भारतीय राष्ट्रीय कांग्रेस", 460, 471),
    (13, "Moderates and Extremists in Congress", "कांग्रेस में नरम दल एवं गरम दल", 471, 477),
    (14, "Revolutionary Movement in India", "भारत में क्रांतिकारी आंदोलन", 477, 491),
    (15, "Revolutionary Activities Outside India", "भारत से बाहर क्रांतिकारी गतिविधियां", 491, 497),
    (16, "Partition of Bengal and Swadeshi Movement", "बंगाल विभाजन एवं स्वदेशी आंदोलन", 497, 502),
    (17, "Congress: Banaras, Calcutta and Surat Sessions", "कांग्रेस: बनारस, कलकत्ता एवं सूरत अधिवेशन", 503, 506),
    (18, "Formation of Muslim League (1906)", "मुस्लिम लीग का गठन (1906)", 506, 508),
    (19, "Morley-Minto Reforms", "मार्ले-मिंटो सुधार (1909)", 508, 509),
    (20, "Delhi Durbar and Change of Capital", "दिल्ली दरबार एवं राजधानी परिवर्तन", 509, 511),
    (21, "Lucknow Session of Congress (The Lucknow Pact)", "कांग्रेस का लखनऊ अधिवेशन (लखनऊ समझौता 1916)", 511, 512),
    (22, "Home Rule League Movement", "होम रूल लीग आंदोलन", 512, 515),
    (23, "Gandhi and His Early Movements", "गांधीजी एवं उनके प्रारंभिक आंदोलन", 515, 531),
    (24, "Peasant Movement and Kisan Sabha", "किसान आंदोलन एवं किसान सभा", 531, 536),
    (25, "Trade Union and Communist Party", "ट्रेड यूनियन एवं कम्युनिस्ट पार्टी", 537, 539),
    (26, "Rowlatt Act and Jallianwala Bagh Massacre (1919)", "रौलट एक्ट एवं जलियांवाला बाग हत्याकांड (1919)", 539, 545),
    (27, "Khilafat Movement", "खिलाफत आंदोलन", 545, 548),
    (28, "Non-Cooperation Movement", "असहयोग आंदोलन", 548, 556),
    (29, "Formation of Swaraj Party (1923)", "स्वराज पार्टी का गठन (1923)", 556, 559),
    (30, "Simon Commission (1927)", "साइमन कमीशन (1927)", 559, 563),
    (31, "Lahore Session of Congress and Complete Independence", "कांग्रेस का लाहौर अधिवेशन एवं पूर्ण स्वराज (1929)", 563, 566),
    (32, "Civil Disobedience Movement", "सविनय अवज्ञा आंदोलन", 567, 573),
    (33, "Gandhi-Irwin Pact", "गांधी-इरविन समझौता", 573, 574),
    (34, "Karachi Session of Congress (1931)", "कांग्रेस का कराची अधिवेशन (1931)", 575, 576),
    (35, "Round Table Conferences", "गोलमेज सम्मेलन", 576, 580),
    (36, "Communal Award and Poona Pact (1932)", "सांप्रदायिक पंचाट एवं पूना पैक्ट (1932)", 580, 583),
    (37, "Congress Socialist Party (1934)", "कांग्रेस समाजवादी पार्टी (1934)", 584, 586),
    (38, "Provincial Elections and Formation of Cabinet (1937)", "प्रांतीय चुनाव एवं मंत्रिमंडल का गठन (1937)", 586, 588),
    (39, "Tripuri Crisis of Congress (1939)", "कांग्रेस का त्रिपुरी संकट (1939)", 589, 590),
    (40, "Indian Princely States", "भारतीय देशी रियासतें", 590, 592),
    (41, "Second World War", "द्वितीय विश्व युद्ध", 592, 593),
    (42, "Demand for Pakistan", "पाकिस्तान की मांग", 593, 596),
    (43, "Individual Satyagraha (1940)", "व्यक्तिगत सत्याग्रह (1940)", 596, 597),
    (44, "Cripps Mission (1942)", "क्रिप्स मिशन (1942)", 597, 599),
    (45, "Quit India Movement", "भारत छोड़ो आंदोलन", 599, 609),
    (46, "Subhash Chandra Bose and Azad Hind Fauj", "सुभाष चंद्र बोस एवं आजाद हिंद फौज", 610, 615),
    (47, "Cabinet Mission Plan (1946)", "कैबिनेट मिशन योजना (1946)", 616, 619),
    (48, "Constituent Assembly (1946)", "संविधान सभा (1946)", 619, 621),
    (49, "Formation of Interim Government (1946)", "अंतरिम सरकार का गठन (1946)", 621, 623),
    (50, "Partition of India and Independence", "भारत का विभाजन एवं स्वतंत्रता", 623, 631),
    (51, "Constitutional Development of India", "भारत का संवैधानिक विकास", 631, 644),
    (52, "Modern History: Miscellaneous", "आधुनिक इतिहास: विविध", 644, 690),
    (53, "Magazines, Books and Their Authors", "पत्रिकाएं, पुस्तकें एवं उनके लेखक", 691, 718),
    (54, "Art and Culture", "कला एवं संस्कृति", 718, 740),
    (55, "Awards and Honours", "पुरस्कार एवं सम्मान", 740, 744)
]

print(f"Ancient: {len(ancient_raw)} topics")
print(f"Medieval: {len(medieval_raw)} topics")
print(f"Modern: {len(modern_raw)} topics")
print(f"Total History Topics: {len(ancient_raw) + len(medieval_raw) + len(modern_raw)}")

config = {
    "ancient": ancient_raw,
    "medieval": medieval_raw,
    "modern": modern_raw
}

with open(r'D:\Android Project\prepunfold-cdn\scripts\history_topics_config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
print("Saved history_topics_config.json successfully!")
