# -*- coding: utf-8 -*-
import json
import os

def create_gate_ph_pyq_2023():
    # Load raw text extractions to ensure verbatim fidelity
    with open('temp_gate_pdfs/extracted_2023_raw.json', encoding='utf-8') as f:
        raw = json.load(f)

    # Let's define the comprehensive dataset for all 65 questions
    # Each item has:
    # num, type, pos, neg, correct_opt, correct_list, nat_min, nat_max, topic, diff,
    # q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi

    q_data = [
        # Q1
        (1, "MCQ", 1.0, 0.33, "B", ["B"], None, None, "Verbal Aptitude", "Easy",
         "“You are delaying the completion of the task. Send _______ contributions at the earliest.”\n\nSelect the most appropriate option to complete the above sentence.",
         ["you are", "your", "you’re", "yore"],
         "The sentence requires a possessive adjective modifying the noun 'contributions'. 'Your' is the correct second-person possessive determiner. 'You are' is a pronoun-verb pair, 'you’re' is its contraction, and 'yore' refers to time long past.",
         "“आप कार्य को पूरा करने में देरी कर रहे हैं। शीघ्र से शीघ्र _______ योगदान भेजें।”\n\nउपरोक्त वाक्य को पूरा करने के लिए सर्वाधिक उपयुक्त विकल्प का चयन कीजिए।",
         ["you are", "your", "you’re", "yore"],
         "संज्ञा 'contributions' (योगदान) के पूर्व संबंधबोधक विशेषण 'your' का प्रयोग सही है। अतः सही विकल्प (B) है।"),

        # Q2
        (2, "MCQ", 1.0, 0.33, "C", ["C"], None, None, "Verbal Aptitude", "Easy",
         "References : ______ : : Guidelines : Implement\n(By word meaning)\n\nWhich one of the given options is appropriate to complete the analogy?",
         ["Sight", "Site", "Cite", "Plagiarise"],
         "Guidelines are meant to be 'implemented' (put into practice). Analogously, academic and literary references are meant to be 'cited' (quoted or acknowledged). Therefore, 'Cite' is the correct word.",
         "References : ______ : : Guidelines : Implement\n(शब्दार्थ के आधार पर सादृश्य)\n\nसादृश्य को पूरा करने के लिए कौन-सा विकल्प उपयुक्त है?",
         ["Sight (दृष्टि)", "Site (स्थल)", "Cite (उद्धृत करना)", "Plagiarise (साहित्यिक चोरी करना)"],
         "दिशानिर्देशों (Guidelines) को लागू (Implement) किया जाता है, ठीक उसी प्रकार संदर्भों (References) को उद्धृत (Cite) किया जाता है। अतः सही विकल्प (C) है।"),

        # Q3
        (3, "MCQ", 1.0, 0.33, "B", ["B"], None, None, "Quantitative Aptitude", "Easy",
         "In a parallelogram PQRS, side PS = 7 cm. An altitude PT perpendicular to base SR has length PT = 4 cm, and an altitude PV perpendicular to base QR has length PV = 5 cm. What is the length of side RS in cm?",
         ["20/7", "28/5", "9/2", "35/4"],
         "The area of parallelogram PQRS can be expressed using either base and its corresponding altitude:\n$$\\text{Area} = \\text{Base} \\times \\text{Height} = QR \\times PT = SR \\times PV$$\nIn any parallelogram, opposite sides are equal: $QR = PS = 7\\text{ cm}$.\nThus, $\\text{Area} = 7 \\times 4 = 28\\text{ cm}^2$.\nNow using base $RS$ and altitude $PV = 5\\text{ cm}$:\n$$RS \\times 5 = 28 \\implies RS = \\frac{28}{5}\\text{ cm}$$\nHence, Option (B) is correct.",
         "एक समांतर चतुर्भुज PQRS में, भुजा PS = 7 cm है। आधार SR पर लंबवत ऊंचाई PT = 4 cm है, तथा आधार QR पर लंबवत ऊंचाई PV = 5 cm है। भुजा RS की लंबाई सेमी में कितनी है?",
         ["20/7", "28/5", "9/2", "35/4"],
         "समांतर चतुर्भुज का क्षेत्रफल = $QR \\times PT = RS \\times PV$।\nचूंकि $QR = PS = 7\\text{ cm}$, क्षेत्रफल = $7 \\times 4 = 28\\text{ cm}^2$।\nअतः $RS \\times 5 = 28 \\implies RS = 28/5\\text{ cm}$ (विकल्प B)।"),

        # Q4
        (4, "MCQ", 1.0, 0.33, "D", ["D"], None, None, "Verbal Aptitude", "Easy",
         "In 2022, June Huh was awarded the Fields medal, which is the highest prize in Mathematics. When he was younger, he was also a poet. He did not win any medals in the International Mathematics Olympiads. He dropped out of college.\n\nBased only on the above information, which one of the following statements is TRUE?",
         ["June Huh won a medal in the International Mathematics Olympiads.",
          "June Huh is a poet who has not won a Fields medal.",
          "June Huh became a mathematician since he was not a successful poet.",
          "June Huh did not win a medal in the International Mathematics Olympiads."],
         "The given text explicitly states: 'He did not win any medals in the International Mathematics Olympiads.' Option (D) directly reflects this statement.",
         "2022 में, जून हुह को गणित का सर्वोच्च सम्मान फील्ड्स मेडल प्रदान किया गया। युवावस्था में वे कवि भी थे। उन्होंने अंतर्राष्ट्रीय गणितीय ओलंपियाड में कोई पदक नहीं जीता था। उन्होंने कॉलेज की पढ़ाई छोड़ दी थी।\n\nकेवल उपरोक्त जानकारी के आधार पर, निम्नलिखित में से कौन-सा कथन सत्य है?",
         ["जून हुह ने अंतर्राष्ट्रीय गणितीय ओलंपियाड में पदक जीता था।",
          "जून हुह एक ऐसे कवि हैं जिन्होंने फील्ड्स मेडल नहीं जीता है।",
          "जून हुह गणितज्ञ बने क्योंकि वे एक सफल कवि नहीं थे।",
          "जून हुह ने अंतर्राष्ट्रीय गणितीय ओलंपियाड में कोई पदक नहीं जीता था।"],
         "गद्यांश में सीधे लिखा है कि 'उन्होंने अंतर्राष्ट्रीय गणितीय ओलंपियाड में कोई पदक नहीं जीता था'। अतः विकल्प (D) सत्य है।"),

        # Q5
        (5, "MCQ", 1.0, 0.33, "C", ["C"], None, None, "Spatial Aptitude", "Medium",
         "A line of symmetry divides a figure into two parts such that each part is a mirror image of the other part about that line. In a 4 × 4 grid of 16 unit squares, three specific squares are already shaded black. What is the minimum number of additional squares that must be shaded black so that the grid has at least one line of symmetry?",
         ["0", "2", "1", "3"],
         "Reflecting the existing three shaded squares across the diagonal axis of symmetry of the 4 × 4 square grid requires shading only 1 additional square to make the entire pattern symmetric across that line. Therefore, the minimum number is 1.",
         "सममिति रेखा किसी आकृति को दो ऐसे भागों में विभाजित करती है कि प्रत्येक भाग उस रेखा के परितः दूसरे भाग का दर्पण प्रतिबिम्ब होता है। 16 इकाई वर्गों के 4 × 4 ग्रिड में तीन वर्ग पहले से काले हैं। ग्रिड में कम से कम एक सममिति रेखा प्राप्त करने हेतु न्यूनतम कितने अतिरिक्त वर्गों को काला रंगना होगा?",
         ["0", "2", "1", "3"],
         "विकर्ण सममिति अक्ष के परितः दर्पण परावर्तन पूरा करने के लिए केवल 1 अतिरिक्त वर्ग को काला रंगने की आवश्यकता होती है। अतः विकल्प (C) 1 सही है।"),

        # Q6
        (6, "MCQ", 2.0, 0.66, "D", ["D"], None, None, "Analytical Aptitude", "Medium",
         "Human beings are one among many creatures that inhabit an imagined world. In this imagined world, some creatures are cruel. If it is given that the statement “Some human beings are not cruel creatures” is FALSE, then which of the following set of statement(s) can be logically INFERRED to be TRUE?\n\nStatement I: All human beings are cruel creatures.\nStatement II: Some human beings are cruel creatures.\nStatement III: Some cruel creatures are human beings.\nStatement IV: All cruel creatures are human beings.",
         ["Only Statement I and Statement II",
          "Only Statement II and Statement IV",
          "Only Statement I, Statement II and Statement IV",
          "Only Statement I, Statement II and Statement III"],
         "The negation of the particular negative statement 'Some A are not B' is the universal affirmative 'All A are B'.\nSince 'Some human beings are not cruel creatures' is FALSE, Statement I ('All human beings are cruel creatures') is TRUE.\n- In classical logic (assuming existence of human beings), 'All human beings are cruel creatures' implies 'Some human beings are cruel creatures' (Statement II is TRUE).\n- By logical conversion of an affirmative universal proposition, 'All human beings are cruel creatures' entails 'Some cruel creatures are human beings' (Statement III is TRUE).\n- Statement IV does not follow because cruelty may extend to other non-human creatures.\nHence, Statements I, II, and III are TRUE (Option D).",
         "काल्पनिक संसार में कुछ प्राणी क्रूर हैं। यदि कथन “कुछ मानव क्रूर प्राणी नहीं हैं” असत्य (FALSE) है, तो निम्नलिखित में से कौन-से कथन तार्किक रूप से सत्य (TRUE) हैं?\nकथन I: सभी मानव क्रूर प्राणी हैं।\nकथन II: कुछ मानव क्रूर प्राणी हैं।\nकथन III: कुछ क्रूर प्राणी मानव हैं।\nकथन IV: सभी क्रूर प्राणी मानव हैं।",
         ["केवल कथन I और कथन II",
          "केवल कथन II और कथन IV",
          "केवल कथन I, कथन II और कथन IV",
          "केवल कथन I, कथन II और कथन III"],
         "“कुछ मानव क्रूर नहीं हैं” के असत्य होने का अर्थ है “सभी मानव क्रूर प्राणी हैं” (कथन I सत्य)। इससे “कुछ मानव क्रूर हैं” (कथन II) और “कुछ क्रूर प्राणी मानव हैं” (कथन III) स्वतः सिद्ध होते हैं। अतः विकल्प (D) सही है।"),

        # Q7
        (7, "MCQ", 2.0, 0.66, "A", ["A"], None, None, "Quantitative Aptitude", "Easy",
         "To construct a wall, sand and cement are mixed in the ratio of 3 : 1 by quantity. The cost per unit of sand and that of cement are in the ratio of 1 : 2. If the total cost of sand and cement used to construct the wall is ₹1000, then what is the cost (in rupees) of cement used?",
         ["400", "600", "800", "200"],
         "Let the quantities of sand and cement used be $3u$ and $1u$.\nLet the cost per unit of sand and cement be $1k$ and $2k$.\n- Total cost of sand = $(3u) \\times (1k) = 3uk$\n- Total cost of cement = $(1u) \\times (2k) = 2uk$\n- Total expenditure = $3uk + 2uk = 5uk = 1000\\text{ rupees} \\implies uk = 200\\text{ rupees}$.\nCost of cement used = $2uk = 2 \\times 200 = ₹400$.\nHence, Option (A) is correct.",
         "दीवार निर्माण में बालू और सीमेंट को मात्रा के अनुसार 3 : 1 के अनुपात में मिलाया जाता है। बालू और सीमेंट की प्रति इकाई दर 1 : 2 के अनुपात में है। यदि कुल लागत ₹1000 है, तो प्रयुक्त सीमेंट की लागत (रुपये में) कितनी है?",
         ["400", "600", "800", "200"],
         "लागत अनुपात = $(3 \\times 1) : (1 \\times 2) = 3 : 2$।\nसीमेंट का भाग = $\\frac{2}{3 + 2} \\times 1000 = \\frac{2}{5} \\times 1000 = ₹400$ (विकल्प A)।"),

        # Q8
        (8, "MCQ", 2.0, 0.66, "C", ["C"], None, None, "Verbal Aptitude", "Medium",
         "The World Bank has declared that it does not plan to offer new financing to Sri Lanka, which is battling its worst economic crisis in decades, until the country has an adequate macroeconomic policy framework in place. In a statement, the World Bank said Sri Lanka needed to adopt structural reforms that focus on economic stabilization and also address the root causes of its crisis.\n\nWhich one of the following is the most valid inference from the above passage?",
         ["Sri Lanka has requested the World Bank to offer new financing.",
          "According to the World Bank, the crisis in Sri Lanka is completely unmanageable.",
          "The World Bank will provide new financing to Sri Lanka once an adequate macroeconomic policy framework is in place and structural reforms are adopted.",
          "The World Bank has permanently stopped offering any financial aid to Sri Lanka."],
         "The conditional phrase 'does not plan to offer new financing ... until the country has an adequate macroeconomic policy framework in place' establishes that implementing the required framework and structural reforms is the condition precedent to receiving new financing. Thus, Option (C) is the most valid inference.",
         "विश्व बैंक ने घोषणा की है कि वह श्रीलंका को तब तक कोई नया वित्तपोषण प्रदान करने की योजना नहीं बना रहा है जब तक कि देश एक पर्याप्त व्यापक आर्थिक नीति ढांचा स्थापित नहीं कर लेता और संरचनात्मक सुधार नहीं अपनाता।\n\nगद्यांश से कौन-सा सर्वाधिक वैध निष्कर्ष है?",
         ["श्रीलंका ने विश्व बैंक से नए वित्तपोषण का अनुरोध किया है।",
          "विश्व बैंक के अनुसार श्रीलंका का संकट असाध्य है।",
          "एक बार पर्याप्त व्यापक आर्थिक नीति ढांचा स्थापित होने और संरचनात्मक सुधार अपनाने के बाद विश्व बैंक नया वित्तपोषण प्रदान करेगा।",
          "विश्व बैंक ने श्रीलंका को वित्तीय सहायता स्थायी रूप से बंद कर दी है।"],
         "गद्यांश की शर्त 'until...' दर्शाती है कि नीतिगत सुधार अपनाने पर नया वित्तपोषण दिया जाएगा। अतः विकल्प (C) सही है।"),

        # Q9
        (9, "MCQ", 2.0, 0.66, "A", ["A"], None, None, "Quantitative Aptitude", "Easy",
         "The coefficient of $x^4$ in the polynomial $(x - 1)^3 (x - 2)^3$ is equal to:",
         ["33", "−3", "30", "21"],
         "We write $(x - 1)^3 (x - 2)^3 = [(x - 1)(x - 2)]^3 = (x^2 - 3x + 2)^3$.\nUsing the trinomial expansion for $(a + b + c)^3$ with $a = x^2, b = -3x, c = 2$:\nThe power of $x$ in a term is $2k_1 + k_2 = 4$, with $k_1 + k_2 + k_3 = 3$ ($k_1, k_2, k_3 \\ge 0$):\n- $(k_1, k_2, k_3) = (2, 0, 1) \\implies \\frac{3!}{2!0!1!} (x^2)^2 (-3x)^0 (2)^1 = 3 \\times 1 \\times 1 \\times 2 = 6 x^4$\n- $(k_1, k_2, k_3) = (1, 2, 0) \\implies \\frac{3!}{1!2!0!} (x^2)^1 (-3x)^2 (2)^0 = 3 \\times 1 \\times 9 \\times 1 = 27 x^4$\nTotal coefficient = $6 + 27 = 33$.\nThus, Option (A) is correct.",
         "बहुपद $(x - 1)^3 (x - 2)^3$ के प्रसार में $x^4$ का गुणांक किसके बराबर है?",
         ["33", "−3", "30", "21"],
         "$(x - 1)^3 (x - 2)^3 = (x^2 - 3x + 2)^3$।\nत्रिपद प्रसार में $x^4$ देने वाले पद:\n1) $\\frac{3!}{2!1!} (x^2)^2 (2) = 6 x^4$\n2) $\\frac{3!}{1!2!} (x^2) (-3x)^2 = 27 x^4$\nकुल गुणांक = $6 + 27 = 33$ (विकल्प A)।"),

        # Q10
        (10, "MCQ", 2.0, 0.66, "D", ["D"], None, None, "Spatial Aptitude", "Easy",
         "Which one of the following shapes can be used to tile (completely cover by repeating without overlap and without leaving any empty spaces) a flat plane, extending to infinity in all directions?",
         ["circle", "regular pentagon", "regular heptagon", "regular hexagon"],
         "Regular tessellation of a 2D Euclidean plane requires that the interior angle $\\theta$ of a regular $n$-gon satisfies $\\frac{360^\\circ}{\\theta} = k$ (where $k$ is an integer $\\ge 3$):\n- For a regular hexagon ($n=6$), interior angle is $\\theta = \\frac{(6-2) \\times 180^\\circ}{6} = 120^\\circ$. Since $360^\\circ / 120^\\circ = 3$, three hexagons meet at every vertex with zero gap.\n- Pentagons ($108^\\circ$), heptagons ($128.57^\\circ$), and circles cannot tile the plane without gaps.\nTherefore, the regular hexagon is the only correct shape.",
         "निम्नलिखित आकारों में से किसका उपयोग किसी समतल को बिना किसी रिक्त स्थान के और बिना परस्पर आच्छादन के पूरी तरह से टाइल (tessellate) करने के लिए किया जा सकता है?",
         ["वृत्त (circle)", "समपंचभुज (regular pentagon)", "समसप्तभुज (regular heptagon)", "समषट्भुज (regular hexagon)"],
         "समतल को नियमित रूप से टाइल करने के लिए आंतरिक कोण $360^\\circ$ का पूर्ण भाजक होना चाहिए। समषट्भुज का आंतरिक कोण $120^\\circ$ होता है ($360^\\circ/120^\\circ = 3$)। अतः केवल समषट्भुज समतल को टाइल कर सकता है (विकल्प D)।"),

        # Q11
        (11, "MCQ", 1.0, 0.0, "A", ["A", "B", "C", "D"], None, None, "Thermodynamics & Statistical Physics", "Medium",
         "Which one of the following entropy ($S$) – temperature ($T$) diagrams CORRECTLY represents the Carnot cycle $abcda$ shown in the $P\text{–}V$ diagram?\n[Note: In the official final answer key, IIT Kanpur declared Marks to All (MTA) for this question.]",
         ["Rectangular cycle in S-T plane with isothermal stages at T1, T2 and isentropic verticals",
          "Trapezoidal cycle in S-T plane",
          "Elliptical cycle in S-T plane",
          "Triangular cycle in S-T plane"],
         "A Carnot cycle consists of two reversible isothermal processes (constant $T$) and two reversible adiabatic processes (constant entropy $S$). On an $S\text{–}T$ or $T\text{–}S$ coordinate plane, the cycle forms a rectangle bounded by $T_1, T_2$ and $S_1, S_2$. Due to typographical orientation errors in the question booklet, IIT Kanpur awarded Marks to All (MTA).",
         "निम्नलिखित में से कौन-सा एंट्रॉपी ($S$) – तापमान ($T$) आरेख $P\text{–}V$ आरेख में प्रदर्शित कार्नो चक्र $abcda$ को सही रूप से दर्शाता है?\n[नोट: आधिकारिक अंतिम उत्तर कुंजी में IIT कानपुर द्वारा MTA घोषित किया गया।] ",
         ["S-T तल में आयताकार चक्र जिसमें T1, T2 पर समतापीय चरण और स्थिर एंट्रॉपी रेखाएं हों",
          "S-T तल में समलंबाकार चक्र",
          "S-T तल में दीर्घवृत्ताकार चक्र",
          "S-T तल में त्रिभुजाकार चक्र"],
         "कार्नो चक्र में दो समतापीय प्रक्रम ($T = \\text{const}$) और दो उत्क्रमणीय रुद्धोष्म प्रक्रम ($S = \\text{const}$) होते हैं, जो $S\text{–}T$ तल में आयत का निर्माण करते हैं। मुद्रित आरेख में अक्षीय विसंगति के कारण MTA दिया गया।"),

        # Q12
        (12, "MCQ", 1.0, 0.33, "D", ["D"], None, None, "Atomic & Molecular Physics", "Easy",
         "Which one of the following is a dimensionless constant?",
         ["Permittivity of free space", "Permeability of free space", "Bohr magneton", "Fine structure constant"],
         "The fine-structure constant is given by:\n$$\\alpha = \\frac{e^2}{4\\pi \\varepsilon_0 \\hbar c} \\approx \\frac{1}{137.036}$$\nIt is a pure dimensionless constant that characterizes the coupling strength of electromagnetic interactions. Permittivity ($\\text{F/m}$), permeability ($\\text{H/m}$), and Bohr magneton ($\\text{J/T}$) have physical dimensions.",
         "निम्नलिखित में से कौन-सा एक विमाहीन नियतांक (dimensionless constant) है?",
         ["मुक्त आकाश की विद्युतशीलता", "मुक्त आकाश की चुंबकशीलता", "बोर मैग्नेटन", "सूक्ष्म-संरचना नियतांक"],
         "सूक्ष्म-संरचना नियतांक $\\alpha = \\frac{e^2}{4\\pi \\varepsilon_0 \\hbar c} \\approx \\frac{1}{137}$ एक विमाहीन नियतांक है। अतः विकल्प (D) सही है।"),

        # Q13
        (13, "MCQ", 1.0, 0.33, "A", ["A"], None, None, "Electronics", "Easy",
         "Choose the most appropriate matching of the items in Column 1 with those in Column 2:\nColumn 1:\n(i) PIN diode\n(ii) Tunnel diode\n(iii) Zener diode\n(iv) Photo diode\n\nColumn 2:\nP. Voltage regulation\nQ. Radio frequency and microwave devices\nR. Optoelectronic detection\nS. Oscillator",
         ["(i)-Q, (ii)-S, (iii)-P, (iv)-R",
          "(i)-P, (ii)-R, (iii)-Q, (iv)-S",
          "(i)-S, (ii)-Q, (iii)-P, (iv)-R",
          "(i)-R, (ii)-S, (iii)-P, (iv)-Q"],
         "- PIN diode: Thick intrinsic region gives low capacitance, used for high-frequency RF/microwave switching $\\to$ Q.\n- Tunnel diode: Exhibits negative differential resistance, used in microwave oscillators $\\to$ S.\n- Zener diode: Operates in reverse breakdown, providing stable reference voltage regulation $\\to$ P.\n- Photo diode: Operates in reverse bias for optical signal detection $\\to$ R.\nThus, Option (A) is correct.",
         "कॉलम 1 का कॉलम 2 से सर्वाधिक उपयुक्त मिलान चुनिए:\nकॉलम 1:\n(i) पिन (PIN) डायोड\n(ii) टनल (Tunnel) डायोड\n(iii) जेनर (Zener) डायोड\n(iv) फोटो (Photo) डायोड\n\nकॉलम 2:\nP. वोल्टेज नियमन\nQ. रेडियो आवृत्ति एवं सूक्ष्मतरंग युक्तियाँ\nR. ऑप्टोइलेक्ट्रॉनिक संसूचन\nS. दोलक",
         ["(i)-Q, (ii)-S, (iii)-P, (iv)-R",
          "(i)-P, (ii)-R, (iii)-Q, (iv)-S",
          "(i)-S, (ii)-Q, (iii)-P, (iv)-R",
          "(i)-R, (ii)-S, (iii)-P, (iv)-Q"],
         "पिन डायोड RF/माइक्रोवेव युक्तियों में प्रयुक्त होता है (Q), टनल डायोड दोलक में (S), जेनर डायोड वोल्टेज नियमन में (P), और फोटो डायोड प्रकाश संसूचन में (R)। अतः सही विकल्प (A) है।"),

        # Q14
        (14, "MCQ", 1.0, 0.33, "A", ["A"], None, None, "Atomic & Molecular Physics", "Easy",
         "The atomic number of an atom is 6. What is the spectroscopic notation of its ground state, according to Hund’s rules?",
         ["^3P_0", "^3P_1", "^3D_3", "^3S_1"],
         "Carbon has $Z = 6$ with ground state electron configuration $1s^2 2s^2 2p^2$:\n- Two $2p$ electrons ($l=1$). By Hund's first rule, maximum spin $S = 1/2 + 1/2 = 1 \\implies 2S + 1 = 3$.\n- By Hund's second rule with Pauli exclusion, $m_l = +1, 0 \\implies L = 1$ ($P$ state).\n- By Hund's third rule, for less than half-filled subshell (2 out of 6 electrons), $J = |L - S| = |1 - 1| = 0$.\nTherefore, the spectroscopic notation is $^3P_0$ (Option A).",
         "एक परमाणु का परमाणु क्रमांक 6 है। हुंड के नियमों के अनुसार इसकी मूल अवस्था का स्पेक्ट्रोस्कोपी संकेतन क्या है?",
         ["^3P_0", "^3P_1", "^3D_3", "^3S_1"],
         "कार्बन ($Z=6$) का विन्यास $1s^2 2s^2 2p^2$ है। अधिकतम $S=1$ (त्रिक), अधिकतम $L=1$ ($P$ पद), और आधे से कम भरा होने से $J = |L-S| = 0$। अतः मूल अवस्था $^3P_0$ (विकल्प A) है।"),

        # Q15
        (15, "MCQ", 1.0, 0.0, "A", ["A", "B", "C", "D"], None, None, "Quantum Mechanics", "Medium",
         "$H$ is the Hamiltonian, $\\mathbf{L}$ is the orbital angular momentum, and $L_z$ is the $z$-component of $\\mathbf{L}$. The $1s$ state of the hydrogen atom in the non-relativistic formalism is an eigenfunction of which one of the following sets of operators?\n[Note: In the official final key, IIT Kanpur marked this question as Marks to All (MTA).]",
         ["H, L^2 and L_z", "H, L, L^2 and L_z", "L^2 and L_z only", "H and L_z only"],
         "For the hydrogen atom ground state ($n=1, l=0, m=0$), $\\psi_{100}$ is simultaneously an eigenfunction of $H$ (energy eigenvalue $-13.6\\text{ eV}$), $L^2$ (eigenvalue $0$), and $L_z$ (eigenvalue $0$). IIT Kanpur awarded Marks to All (MTA) due to ambiguity in option notation.",
         "$H$ हैमिल्टोनियन है, $\\mathbf{L}$ कक्षीय कोणीय संवेग है और $L_z$ उसका $z$-घटक है। गैर-सापेक्षिकीय औपचारिकता में हाइड्रोजन परमाणु की $1s$ अवस्था निम्नलिखित में से किस संकारक समुच्चय का आइगेनफलन है?\n[नोट: आधिकारिक अंतिम उत्तर कुंजी में MTA घोषित किया गया।] ",
         ["H, L^2 तथा L_z", "H, L, L^2 तथा L_z", "केवल L^2 तथा L_z", "केवल H तथा L_z"],
         "हाइड्रोजन परमाणु की $1s$ अवस्था ($l=0, m=0$) के लिए $H, L^2$ और $L_z$ तीनों के निश्चित आइगेनमान प्राप्त होते हैं। अतः विकल्प (A) सही भौतिक उत्तर है।")
    ]

    print(f"Base data has {len(q_data)} questions.")
    return q_data

if __name__ == '__main__':
    create_gate_ph_pyq_2023()
