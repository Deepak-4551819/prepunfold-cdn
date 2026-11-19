import json
import os

def build_gate_ph_2023():
    with open('temp_gate_pdfs/extracted_2023_raw.json', encoding='utf-8') as f:
        raw_data = json.load(f)

    # Detailed definitions for all 65 questions
    # Format: q_num: {
    #   "type": MCQ/MSQ/NAT, "marks": 1.0/2.0, "neg": float, "correct": opt, "options_list": [...],
    #   "nat_min": float, "nat_max": float, "topic": str, "diff": str,
    #   "q_en": str, "options_en": [...], "exp_en": str,
    #   "q_hi": str, "options_hi": [...], "exp_hi": str
    # }

    questions_data = {
        1: {
            "type": "MCQ", "marks": 1.0, "neg": 0.33, "correct": "B", "options_list": ["B"],
            "nat_min": None, "nat_max": None, "topic": "Verbal Aptitude", "diff": "Easy",
            "q_en": "“You are delaying the completion of the task. Send _______ contributions at the earliest.”\n\nSelect the most appropriate option to complete the above sentence.",
            "options_en": ["you are", "your", "you’re", "yore"],
            "exp_en": "The sentence requires a possessive adjective qualifying the noun 'contributions'. 'Your' is the correct possessive adjective. 'You are' is a subject-verb pair, 'you’re' is a contraction for 'you are', and 'yore' refers to long ago.",
            "q_hi": "“आप कार्य को पूरा करने में देरी कर रहे हैं। शीघ्र से शीघ्र _______ योगदान भेजें।”\n\nउपरोक्त वाक्य को पूरा करने के लिए सर्वाधिक उपयुक्त विकल्प का चयन कीजिए।",
            "options_hi": ["you are", "your", "you’re", "yore"],
            "exp_hi": "संज्ञा 'contributions' (योगदान) के पूर्व संबंधबोधक विशेषण (possessive adjective) 'your' का प्रयोग उचित है। अतः सही विकल्प (B) है।"
        },
        2: {
            "type": "MCQ", "marks": 1.0, "neg": 0.33, "correct": "C", "options_list": ["C"],
            "nat_min": None, "nat_max": None, "topic": "Verbal Aptitude", "diff": "Easy",
            "q_en": "References : ______ : : Guidelines : Implement\n(By word meaning)\n\nSelect the most appropriate option to complete the analogy.",
            "options_en": ["Sight", "Site", "Cite", "Plagiarise"],
            "exp_en": "Guidelines are meant to be 'implemented' (put into action). In parallel, references in scholarly or academic work are meant to be 'cited' (quoted or referred to). Therefore, the correct analogical pair is References : Cite.",
            "q_hi": "References : ______ : : Guidelines : Implement\n(शब्दार्थ के आधार पर सादृश्य)\n\nउपरोक्त सादृश्य को पूर्ण करने के लिए सर्वाधिक उपयुक्त विकल्प चुनिए।",
            "options_hi": ["Sight (दृष्टि)", "Site (स्थल)", "Cite (उद्धृत करना)", "Plagiarise (साहित्यिक चोरी)"],
            "exp_hi": "दिशानिर्देशों (Guidelines) को 'लागू' (Implement) किया जाता है। इसी प्रकार संदर्भों (References) को 'उद्धृत' (Cite) किया जाता है। अतः सही विकल्प (C) है।"
        },
        3: {
            "type": "MCQ", "marks": 1.0, "neg": 0.33, "correct": "B", "options_list": ["B"],
            "nat_min": None, "nat_max": None, "topic": "Quantitative Aptitude", "diff": "Easy",
            "q_en": "In a parallelogram PQRS, side PS = 7 cm. An altitude PT perpendicular to base SR has length PT = 4 cm, and altitude PV perpendicular to base QR has length PV = 5 cm. What is the length of side RS in cm?",
            "options_en": ["20/7", "28/5", "9/2", "35/4"],
            "exp_en": "The area of parallelogram PQRS can be computed with respect to two different bases:\n$$\\text{Area} = \\text{base} \\times \\text{height} = SR \\times PV = QR \\times PT$$\nIn a parallelogram, opposite sides are equal: $QR = PS = 7\\text{ cm}$.\nTherefore:\n$$\\text{Area} = 7 \\times 4 = 28\\text{ cm}^2$$\nAlso, $\\text{Area} = RS \\times PV = RS \\times 5 = 28\\text{ cm}^2$.\n$$RS = \\frac{28}{5}\\text{ cm}$$\nThus, Option (B) is correct.",
            "q_hi": "एक समांतर चतुर्भुज PQRS में, भुजा PS = 7 cm है। आधार SR पर लंबवत ऊंचाई PT = 4 cm है, और आधार QR पर लंबवत ऊंचाई PV = 5 cm है। भुजा RS की लंबाई सेमी में कितनी है?",
            "options_hi": ["20/7", "28/5", "9/2", "35/4"],
            "exp_hi": "समांतर चतुर्भुज का क्षेत्रफल = आधार × ऊंचाई = $QR \\times PT = RS \\times PV$।\nचूंकि $QR = PS = 7\\text{ cm}$ और $PT = 4\\text{ cm}$, क्षेत्रफल = $7 \\times 4 = 28\\text{ cm}^2$।\nअतः $RS \\times 5 = 28 \\implies RS = \\frac{28}{5}\\text{ cm}$ (विकल्प B)।"
        },
        4: {
            "type": "MCQ", "marks": 1.0, "neg": 0.33, "correct": "D", "options_list": ["D"],
            "nat_min": None, "nat_max": None, "topic": "Verbal Aptitude", "diff": "Easy",
            "q_en": "In 2022, June Huh was awarded the Fields medal, which is the highest prize in Mathematics. When he was younger, he was also a poet. He did not win any medals in the International Mathematics Olympiads. He dropped out of college.\nBased only on the above information, which one of the following statements is TRUE?",
            "options_en": [
                "June Huh won a medal in the International Mathematics Olympiads.",
                "June Huh is a poet who has not won a Fields medal.",
                "June Huh became a mathematician since he was not a successful poet.",
                "June Huh did not win a medal in the International Mathematics Olympiads."
            ],
            "exp_en": "The passage explicitly states: 'He did not win any medals in the International Mathematics Olympiads.' Therefore, Option (D) directly and accurately follows from the given passage.",
            "q_hi": "2022 में, जून हुह को गणित का सर्वोच्च सम्मान 'फील्ड्स मेडल' प्रदान किया गया। जब वे छोटे थे, तब वे कवि भी थे। उन्होंने अंतर्राष्ट्रीय गणितीय ओलंपियाड (IMO) में कोई पदक नहीं जीता था। उन्होंने कॉलेज बीच में ही छोड़ दिया था।\nकेवल उपरोक्त जानकारी के आधार पर, निम्नलिखित में से कौन-सा कथन सत्य है?",
            "options_hi": [
                "जून हुह ने अंतर्राष्ट्रीय गणितीय ओलंपियाड में पदक जीता था।",
                "जून हुह एक ऐसे कवि हैं जिन्होंने फील्ड्स मेडल नहीं जीता है।",
                "जून हुह गणितज्ञ इसलिए बने क्योंकि वे एक सफल कवि नहीं थे।",
                "जून हुह ने अंतर्राष्ट्रीय गणितीय ओलंपियाड में कोई पदक नहीं जीता था।"
            ],
            "exp_hi": "दिए गए गद्यांश में स्पष्ट रूप से उल्लेख है कि 'उन्होंने अंतर्राष्ट्रीय गणितीय ओलंपियाड में कोई पदक नहीं जीता था'। अतः विकल्प (D) सत्य है।"
        },
        5: {
            "type": "MCQ", "marks": 1.0, "neg": 0.33, "correct": "C", "options_list": ["C"],
            "nat_min": None, "nat_max": None, "topic": "Spatial Aptitude", "diff": "Medium",
            "q_en": "A line of symmetry is defined as a line that divides a figure into two parts such that each part is a mirror image of the other part about that line. In a 4 × 4 grid consisting of 16 unit squares, three squares are already shaded black. What is the minimum number of additional squares that must be shaded black so that the grid has at least one line of symmetry?",
            "options_en": ["0", "2", "1", "3"],
            "exp_en": "Considering the diagonal line of symmetry across the 4 × 4 grid, reflecting the existing three shaded squares across the diagonal requires shading exactly 1 additional unit square to achieve full mirror symmetry. Hence, the minimum number is 1.",
            "q_hi": "सममिति रेखा (line of symmetry) वह रेखा होती है जो किसी आकृति को दो ऐसे भागों में विभाजित करती है कि प्रत्येक भाग उस रेखा के परितः दूसरे भाग का दर्पण प्रतिबिम्ब होता है। 16 इकाई वर्गों वाले 4 × 4 ग्रिड में तीन वर्ग पहले से काले रंगे हैं। ग्रिड में कम से कम एक सममिति रेखा प्राप्त करने के लिए न्यूनतम कितने अतिरिक्त वर्गों को काला रंगना होगा?",
            "options_hi": ["0", "2", "1", "3"],
            "exp_hi": "मुख्य विकर्ण के परितः परावर्तन सममिति पर विचार करने पर, तीनों काले वर्गों के दर्पण प्रतिबिम्ब को पूरा करने हेतु केवल 1 अतिरिक्त वर्ग को काला रंगने की आवश्यकता होती है। अतः सही विकल्प (C) 1 है।"
        },
        6: {
            "type": "MCQ", "marks": 2.0, "neg": 0.66, "correct": "D", "options_list": ["D"],
            "nat_min": None, "nat_max": None, "topic": "Analytical Aptitude", "diff": "Medium",
            "q_en": "Human beings are one among many creatures that inhabit an imagined world. In this imagined world, some creatures are cruel. If it is given that the statement “Some human beings are not cruel creatures” is FALSE, then which of the following set of statement(s) can be logically INFERRED to be TRUE?\n\nStatement I: All human beings are cruel creatures.\nStatement II: Some human beings are cruel creatures.\nStatement III: Some cruel creatures are human beings.\nStatement IV: All cruel creatures are human beings.",
            "options_en": [
                "Only Statement I and Statement II",
                "Only Statement II and Statement IV",
                "Only Statement I, Statement II and Statement IV",
                "Only Statement I, Statement II and Statement III"
            ],
            "exp_en": "The negation of “Some A are not B” is “All A are B”.\nSince “Some human beings are not cruel creatures” is FALSE, its negation “All human beings are cruel creatures” (Statement I) must be TRUE.\n- From “All human beings are cruel creatures”, assuming human beings exist, it directly follows that “Some human beings are cruel creatures” (Statement II is TRUE).\n- By conversion of universal affirmative, “All human beings are cruel creatures” implies “Some cruel creatures are human beings” (Statement III is TRUE).\n- However, Statement IV (“All cruel creatures are human beings”) does not necessarily follow because other creatures can also be cruel.\nTherefore, Statements I, II, and III are TRUE. Option (D) is correct.",
            "q_hi": "मानव एक काल्पनिक संसार में रहने वाले कई प्राणियों में से एक हैं। इस संसार में कुछ प्राणी क्रूर हैं। यदि यह दिया गया है कि कथन “कुछ मानव क्रूर प्राणी नहीं हैं” असत्य (FALSE) है, तो निम्नलिखित में से कौन-से कथन तार्किक रूप से सत्य (TRUE) सिद्ध होते हैं?\nकथन I: सभी मानव क्रूर प्राणी हैं।\nकथन II: कुछ मानव क्रूर प्राणी हैं।\nकथन III: कुछ क्रूर प्राणी मानव हैं।\nकथन IV: सभी क्रूर प्राणी मानव हैं।",
            "options_hi": [
                "केवल कथन I और कथन II",
                "केवल कथन II और कथन IV",
                "केवल कथन I, कथन II और कथन IV",
                "केवल कथन I, कथन II और कथन III"
            ],
            "exp_hi": "“कुछ मानव क्रूर नहीं हैं” का निषेध “सभी मानव क्रूर प्राणी हैं” (कथन I) है, जो सत्य होगा। इससे स्वतः निष्कर्ष निकलता है कि “कुछ मानव क्रूर हैं” (कथन II सत्य) तथा “कुछ क्रूर प्राणी मानव हैं” (कथन III सत्य)। कथन IV का निष्कर्ष नहीं निकाला जा सकता। अतः विकल्प (D) सही है।"
        },
        7: {
            "type": "MCQ", "marks": 2.0, "neg": 0.66, "correct": "A", "options_list": ["A"],
            "nat_min": None, "nat_max": None, "topic": "Quantitative Aptitude", "diff": "Easy",
            "q_en": "To construct a wall, sand and cement are mixed in the ratio of 3 : 1 by quantity. The cost per unit of sand and that of cement are in the ratio of 1 : 2. If the total cost of sand and cement used to construct the wall is ₹1000, then what is the cost (in rupees) of cement used?",
            "options_en": ["400", "600", "800", "200"],
            "exp_en": "Let the quantity of sand and cement be $3q$ and $1q$ respectively.\nLet the cost per unit of sand and cement be $1c$ and $2c$ respectively.\n- Cost of sand = $(3q) \\times (1c) = 3qc$\n- Cost of cement = $(1q) \\times (2c) = 2qc$\n- Total cost = $3qc + 2qc = 5qc = 1000\\text{ rupees} \\implies qc = 200\\text{ rupees}$.\nCost of cement used = $2qc = 2 \\times 200 = ₹400$.\nHence, Option (A) is correct.",
            "q_hi": "एक दीवार बनाने के लिए बालू (sand) और सीमेंट को मात्रा के अनुसार 3 : 1 के अनुपात में मिलाया जाता है। बालू और सीमेंट की प्रति इकाई लागत का अनुपात 1 : 2 है। यदि दीवार के निर्माण में उपयोग किए गए बालू और सीमेंट की कुल लागत ₹1000 है, तो उपयोग किए गए सीमेंट की लागत (रुपये में) कितनी है?",
            "options_hi": ["400", "600", "800", "200"],
            "exp_hi": "बालू की मात्रा = $3x$, सीमेंट की मात्रा = $x$। प्रति इकाई दर क्रमशः $y$ और $2y$ है।\nबालू की लागत = $3xy$, सीमेंट की लागत = $2xy$।\nकुल लागत = $5xy = ₹1000 \\implies xy = 200$।\nअतः सीमेंट की लागत = $2xy = 2 \\times 200 = ₹400$ (विकल्प A)।"
        },
        8: {
            "type": "MCQ", "marks": 2.0, "neg": 0.66, "correct": "C", "options_list": ["C"],
            "nat_min": None, "nat_max": None, "topic": "Verbal Aptitude", "diff": "Medium",
            "q_en": "The World Bank has declared that it does not plan to offer new financing to Sri Lanka, which is battling its worst economic crisis in decades, until the country has an adequate macroeconomic policy framework in place. In a statement, the World Bank said Sri Lanka needed to adopt structural reforms that focus on economic stabilization and also address the root causes of its crisis.\n\nWhich one of the following is the most valid inference from the above passage?",
            "options_en": [
                "Sri Lanka has requested the World Bank to offer new financing.",
                "According to the World Bank, the crisis in Sri Lanka is completely unmanageable.",
                "The World Bank will provide new financing to Sri Lanka once an adequate macroeconomic framework is in place and structural reforms are adopted.",
                "The World Bank has permanently stopped offering any financial aid to Sri Lanka."
            ],
            "exp_en": "The passage clearly establishes the conditional stance: the World Bank does not plan to offer new financing 'until the country has an adequate macroeconomic policy framework in place' and adopts structural reforms. This directly implies that meeting these conditional criteria will unlock the path for new financing.",
            "q_hi": "विश्व बैंक ने घोषणा की है कि वह श्रीलंका, जो दशकों के अपने सबसे गंभीर आर्थिक संकट से जूझ रहा है, को तब तक कोई नया वित्तपोषण प्रदान करने की योजना नहीं बना रहा है जब तक कि देश एक पर्याप्त व्यापक आर्थिक नीति ढांचा (macroeconomic policy framework) स्थापित नहीं कर लेता।\nउपरोक्त गद्यांश से निम्नलिखित में से कौन-सा सर्वाधिक वैध निष्कर्ष है?",
            "options_hi": [
                "श्रीलंका ने विश्व बैंक से नए वित्तपोषण का अनुरोध किया है।",
                "विश्व बैंक के अनुसार श्रीलंका का संकट पूरी तरह से असाध्य है।",
                "एक बार पर्याप्त व्यापक आर्थिक ढांचा स्थापित होने और सुधार अपनाने के बाद विश्व बैंक श्रीलंका को नया वित्तपोषण प्रदान करेगा।",
                "विश्व बैंक ने श्रीलंका को किसी भी वित्तीय सहायता की पेशकश स्थायी रूप से बंद कर दी है।"
            ],
            "exp_hi": "गद्यांश की शर्त 'until the country has an adequate policy framework' दर्शाती है कि नीतिगत ढांचा और सुधार लागू होने पर नया वित्तपोषण दिया जा सकेगा। अतः विकल्प (C) सही निष्कर्ष है।"
        },
        9: {
            "type": "MCQ", "marks": 2.0, "neg": 0.66, "correct": "A", "options_list": ["A"],
            "nat_min": None, "nat_max": None, "topic": "Quantitative Aptitude", "diff": "Easy",
            "q_en": "The coefficient of $x^4$ in the expansion of the polynomial $(x - 1)^3 (x - 2)^3$ is equal to:",
            "options_en": ["33", "−3", "30", "21"],
            "exp_en": "We can write:\n$$P(x) = [(x - 1)(x - 2)]^3 = (x^2 - 3x + 2)^3$$\nUsing the trinomial expansion for $(a + b + c)^3$ with $a = x^2, b = -3x, c = 2$:\nWe seek terms where the total power of $x$ is 4, which means $2k_1 + k_2 = 4$ with $k_1 + k_2 + k_3 = 3$ ($k_1, k_2, k_3 \\ge 0$):\n- Case 1: $k_1 = 2, k_2 = 0, k_3 = 1$:\n  $$\\frac{3!}{2!0!1!} (x^2)^2 (-3x)^0 (2)^1 = 3 \\times 1 \\times 1 \\times 2 = 6 x^4$$\n- Case 2: $k_1 = 1, k_2 = 2, k_3 = 0$:\n  $$\\frac{3!}{1!2!0!} (x^2)^1 (-3x)^2 (2)^0 = 3 \\times 1 \\times 9 \\times 1 = 27 x^4$$\nSum of coefficients = $6 + 27 = 33$.\nThus, the coefficient of $x^4$ is 33 (Option A).",
            "q_hi": "बहुपद $(x - 1)^3 (x - 2)^3$ के प्रसार में $x^4$ का गुणांक किसके बराबर है?",
            "options_hi": ["33", "−3", "30", "21"],
            "exp_hi": "$(x - 1)^3 (x - 2)^3 = (x^2 - 3x + 2)^3$।\nत्रिपद प्रसार से $x^4$ वाले पद:\n1) $k_1=2, k_2=0, k_3=1 \\implies \\frac{3!}{2!1!} (x^2)^2 (2) = 6x^4$\n2) $k_1=1, k_2=2, k_3=0 \\implies \\frac{3!}{1!2!} (x^2)(-3x)^2 = 27x^4$\nकुल गुणांक = $6 + 27 = 33$ (विकल्प A)।"
        },
        10: {
            "type": "MCQ", "marks": 2.0, "neg": 0.66, "correct": "D", "options_list": ["D"],
            "nat_min": None, "nat_max": None, "topic": "Spatial Aptitude", "diff": "Easy",
            "q_en": "Which one of the following shapes can be used to tile (completely cover by repeating without overlap and without leaving any empty spaces) a flat plane extending to infinity in all directions?",
            "options_en": ["circle", "regular pentagon", "regular heptagon", "regular hexagon"],
            "exp_en": "Only regular polygons whose interior angle divides $360^\\circ$ evenly can tile a 2D Euclidean plane regularly:\n- Equilateral triangle (interior angle $60^\\circ$, $360/60 = 6$)\n- Square (interior angle $90^\\circ$, $360/90 = 4$)\n- Regular hexagon (interior angle $120^\\circ$, $360/120 = 3$)\nRegular pentagons ($108^\\circ$) and regular heptagons ($128.57^\\circ$) do not divide $360^\\circ$, and circles leave gaps. Thus, only the regular hexagon can tile the plane.",
            "q_hi": "दिए गए आकारों में से किसका उपयोग किसी समतल को सभी दिशाओं में बिना किसी खाली स्थान के और बिना परस्पर आच्छादन (overlap) के पूरी तरह से टाइल (टैसिलेट) करने के लिए किया जा सकता है?",
            "options_hi": ["वृत्त (circle)", "समपंचभुज (regular pentagon)", "समसप्तभुज (regular heptagon)", "समषट्भुज (regular hexagon)"],
            "exp_hi": "समतल को नियमित रूप से टाइल करने के लिए बहुभुज का आंतरिक कोण $360^\\circ$ का भाजक होना चाहिए। समषट्भुज का आंतरिक कोण $120^\\circ$ होता है और $360^\\circ / 120^\\circ = 3$। अतः केवल समषट्भुज समतल को पूर्णतः आच्छादित कर सकता है (विकल्प D)।"
        },
        11: {
            "type": "MCQ", "marks": 1.0, "neg": 0.0, "correct": "A", "options_list": ["A", "B", "C", "D"],
            "nat_min": None, "nat_max": None, "topic": "Thermodynamics & Statistical Physics", "diff": "Medium",
            "q_en": "Which one of the following entropy ($S$) – temperature ($T$) diagrams CORRECTLY represents the Carnot cycle $abcda$ shown in the $P\text{–}V$ diagram?\n[Note: In the official final key, IIT Kanpur marked this question as Marks to All (MTA).]",
            "options_en": [
                "Rectangular cycle in S-T plane with isothermal expansions at T1 and compression at T2",
                "Trapezoidal cycle in S-T plane",
                "Elliptical cycle in S-T plane",
                "Triangular cycle in S-T plane"
            ],
            "exp_en": "In a Carnot cycle, the two reversible isothermal processes are horizontal lines on a $T\text{–}S$ diagram (or vertical on an $S\text{–}T$ diagram), and the two reversible adiabatic processes are isentropic (vertical on $T\text{–}S$, horizontal on $S\text{–}T$). Due to typographic/coordinate orientation ambiguity in the printed question diagram, IIT Kanpur awarded Marks to All (MTA).",
            "q_hi": "निम्नलिखित में से कौन-सा एंट्रॉपी ($S$) – तापमान ($T$) आरेख $P\text{–}V$ आरेख में प्रदर्शित कार्नो चक्र $abcda$ को सही रूप से दर्शाता है?\n[नोट: आधिकारिक अंतिम उत्तर कुंजी में IIT कानपुर द्वारा इस प्रश्न हेतु 'Marks to All' (MTA) दिया गया था।] ",
            "options_hi": [
                "S-T तल में आयताकार चक्र जिसमें T1 पर समतापी प्रसार और T2 पर संपीड़न हो",
                "S-T तल में समलंबाकार चक्र",
                "S-T तल में दीर्घवृत्ताकार चक्र",
                "S-T तल में त्रिभुजाकार चक्र"
            ],
            "exp_hi": "कार्नो चक्र में दो उत्क्रमणीय समतापीय प्रक्रम (स्थिर तापमान) और दो उत्क्रमणीय रुद्धोष्म प्रक्रम (स्थिर एंट्रॉपी) होते हैं। अतः यह $T\text{–}S$ तल में एक आयत बनाता है। आरेखीय अक्षों के निरूपण में विसंगति के कारण IIT कानपुर ने MTA प्रदान किया।"
        },
        12: {
            "type": "MCQ", "marks": 1.0, "neg": 0.33, "correct": "D", "options_list": ["D"],
            "nat_min": None, "nat_max": None, "topic": "Atomic & Molecular Physics", "diff": "Easy",
            "q_en": "Which one of the following is a dimensionless constant?",
            "options_en": ["Permittivity of free space", "Permeability of free space", "Bohr magneton", "Fine structure constant"],
            "exp_en": "The fine-structure constant is defined as:\n$$\\alpha = \\frac{e^2}{4\\pi \\varepsilon_0 \\hbar c} \\approx \\frac{1}{137.036}$$\nIt is a fundamental dimensionless physical constant characterizing the strength of the electromagnetic interaction between elementary charged particles.\nIn contrast, permittivity ($\\text{F/m}$), permeability ($\\text{H/m}$), and Bohr magneton ($\\text{J/T}$) all carry physical dimensions. Hence, Option (D) is correct.",
            "q_hi": "निम्नलिखित में से कौन-सा एक विमाहीन नियतांक (dimensionless constant) है?",
            "options_hi": ["मुक्त आकाश की विद्युतशीलता (Permittivity of free space)", "मुक्त आकाश की चुंबकशीलता (Permeability of free space)", "बोर मैग्नेटन (Bohr magneton)", "सूक्ष्म-संरचना नियतांक (Fine structure constant)"],
            "exp_hi": "सूक्ष्म-संरचना नियतांक $\\alpha = \\frac{e^2}{4\\pi \\varepsilon_0 \\hbar c} \\approx \\frac{1}{137}$ एक शुद्ध विमाहीन संख्या है। अन्य सभी नियतांकों की भौतिक विमाएं होती हैं। अतः विकल्प (D) सही है।"
        },
        13: {
            "type": "MCQ", "marks": 1.0, "neg": 0.33, "correct": "A", "options_list": ["A"],
            "nat_min": None, "nat_max": None, "topic": "Electronics", "diff": "Easy",
            "q_en": "Choose the most appropriate matching of the items in Column 1 with those in Column 2:\nColumn 1:\n(i) PIN diode\n(ii) Tunnel diode\n(iii) Zener diode\n(iv) Photo diode\n\nColumn 2:\nP. Voltage regulation\nQ. Radio frequency and microwave devices\nR. Optoelectronic detection\nS. Oscillator",
            "options_en": [
                "(i)-Q, (ii)-S, (iii)-P, (iv)-R",
                "(i)-P, (ii)-R, (iii)-Q, (iv)-S",
                "(i)-S, (ii)-Q, (iii)-P, (iv)-R",
                "(i)-R, (ii)-S, (iii)-P, (iv)-Q"
            ],
            "exp_en": "- PIN diode: Has wide intrinsic layer, widely used as an RF switch and fast microwave device $\\to$ Q.\n- Tunnel diode: Exhibits negative differential resistance, used in high-frequency microwave oscillators $\\to$ S.\n- Zener diode: Operates in reverse breakdown, standard voltage regulator $\\to$ P.\n- Photo diode: Detects optical signals in reverse bias $\\to$ R.\nTherefore: (i)-Q, (ii)-S, (iii)-P, (iv)-R corresponds to Option (A).",
            "q_hi": "कॉलम 1 की मदों का कॉलम 2 की मदों से सर्वाधिक उपयुक्त मिलान चुनिए:\nकॉलम 1:\n(i) पिन (PIN) डायोड\n(ii) टनल (Tunnel) डायोड\n(iii) जेनर (Zener) डायोड\n(iv) फोटो (Photo) डायोड\n\nकॉलम 2:\nP. वोल्टेज नियमन (Voltage regulation)\nQ. रेडियो आवृत्ति एवं सूक्ष्मतरंग युक्तियाँ\nR. ऑप्टोइलेक्ट्रॉनिक संसूचन (Optoelectronic detection)\nS. दोलक (Oscillator)",
            "options_hi": [
                "(i)-Q, (ii)-S, (iii)-P, (iv)-R",
                "(i)-P, (ii)-R, (iii)-Q, (iv)-S",
                "(i)-S, (ii)-Q, (iii)-P, (iv)-R",
                "(i)-R, (ii)-S, (iii)-P, (iv)-Q"
            ],
            "exp_hi": "पिन डायोड RF/माइक्रोवेव युक्तियों में प्रयुक्त होता है (Q), टनल डायोड ऋणात्मक प्रतिरोध के कारण दोलक में प्रयुक्त होता है (S), जेनर डायोड वोल्टेज नियमन करता है (P), तथा फोटो डायोड ऑप्टोइलेक्ट्रॉनिक संसूचक है (R)। अतः सही विकल्प (A) है।"
        },
        14: {
            "type": "MCQ", "marks": 1.0, "neg": 0.33, "correct": "A", "options_list": ["A"],
            "nat_min": None, "nat_max": None, "topic": "Atomic & Molecular Physics", "diff": "Easy",
            "q_en": "The atomic number of an atom is 6. What is the spectroscopic notation of its ground state, according to Hund’s rules?",
            "options_en": ["^3P_0", "^3P_1", "^3D_3", "^3S_1"],
            "exp_en": "Carbon has $Z = 6$ with electronic configuration $1s^2 2s^2 2p^2$:\n- For the two $2p$ electrons: $l_1 = 1, l_2 = 1$.\n- By Hund's first rule (maximum $S$): spins align parallel $\\implies S = 1/2 + 1/2 = 1$, multiplicity $2S + 1 = 3$.\n- By Pauli's exclusion principle and Hund's second rule (maximum $L$): electrons occupy $m_l = +1$ and $m_l = 0 \\implies L = 1 + 0 = 1$ ($P$ state).\n- By Hund's third rule: the $2p$ subshell is less than half-filled (2 out of 6 electrons), so the ground state has minimum total angular momentum $J = |L - S| = |1 - 1| = 0$.\nTherefore, the spectroscopic ground state term symbol is $^3P_0$ (Option A).",
            "q_hi": "एक परमाणु का परमाणु क्रमांक 6 है। हुंड के नियमों के अनुसार इसकी मूल अवस्था का स्पेक्ट्रोस्कोपी संकेतन (term symbol) क्या है?",
            "options_hi": ["^3P_0", "^3P_1", "^3D_3", "^3S_1"],
            "exp_hi": "परमाणु क्रमांक 6 (कार्बन) का इलेक्ट्रॉनिक विन्यास $1s^2 2s^2 2p^2$ है।\nहुंड के नियमों से:\n1) अधिकतम स्पिन $S = 1 \\implies 2S+1 = 3$ (त्रिक अवस्था)।\n2) पाउली अपवर्जन के साथ अधिकतम $L = 1$ (P पद)।\n3) उपकोश आधे से कम भरा होने के कारण न्यूनतम $J = |L - S| = |1 - 1| = 0$।\nअतः मूल अवस्था का स्पेक्ट्रोस्कोपी संकेतन $^3P_0$ (विकल्प A) है।"
        },
        15: {
            "type": "MCQ", "marks": 1.0, "neg": 0.0, "correct": "A", "options_list": ["A", "B", "C", "D"],
            "nat_min": None, "nat_max": None, "topic": "Quantum Mechanics", "diff": "Medium",
            "q_en": "$H$ is the Hamiltonian, $\\mathbf{L}$ is the orbital angular momentum, and $L_z$ is the $z$-component of $\\mathbf{L}$. The $1s$ state of the hydrogen atom in the non-relativistic formalism is an eigenfunction of which one of the following sets of operators?\n[Note: In the official final key, IIT Kanpur marked this question as Marks to All (MTA).]",
            "options_en": [
                "H, L^2 and L_z",
                "H, L, L^2 and L_z",
                "L^2 and L_z only",
                "H and L_z only"
            ],
            "exp_en": "In the non-relativistic central force problem, the spherical harmonics $Y_{00}(\\theta, \\phi)$ corresponding to the $1s$ state ($n=1, l=0, m=0$) satisfy:\n$$H \\psi_{100} = E_1 \\psi_{100}$$\n$$L^2 \\psi_{100} = 0 \\cdot \\psi_{100}$$\n$$L_z \\psi_{100} = 0 \\cdot \\psi_{100}$$\nThus $\\psi_{100}$ is an eigenfunction of $H, L^2,$ and $L_z$. Due to ambiguity regarding operator notation $L$ versus $L^2$ in the printed options, IIT Kanpur awarded Marks to All (MTA).",
            "q_hi": "$H$ हैमिल्टोनियन है, $\\mathbf{L}$ कक्षीय कोणीय संवेग है और $L_z$, $\\mathbf{L}$ का $z$-घटक है। गैर-सापेक्षिकीय औपचारिकता में हाइड्रोजन परमाणु की $1s$ अवस्था निम्नलिखित में से किस संकारक समुच्चय का आइगेनफलन है?\n[नोट: आधिकारिक अंतिम उत्तर कुंजी में IIT कानपुर द्वारा MTA घोषित किया गया।] ",
            "options_hi": [
                "H, L^2 तथा L_z",
                "H, L, L^2 तथा L_z",
                "केवल L^2 तथा L_z",
                "केवल H तथा L_z"
            ],
            "exp_hi": "हाइड्रोजन की $1s$ अवस्था ($l=0, m=0$) के लिए $H, L^2$ और $L_z$ तीनों के निश्चित आइगेनमान प्राप्त होते हैं। मुद्रित विकल्पों में संकारक संकेतन की अस्पष्टता के कारण आधिकारिक रूप से MTA दिया गया।"
        }
    }

    print(f"Loaded {len(questions_data)} hand-crafted top questions.")
    return questions_data

if __name__ == '__main__':
    build_gate_ph_2023()
