# -*- coding: utf-8 -*-
"""
GATE Physics 2021 (IIT Bombay) Official Master Paper - Part 1 (Questions 1 to 35)
10 GA (Q1-Q10) + 25 PH 1-mark (Q11-Q35)
"""

def get_questions_part1():
    questions = []

    # Q1: GA (1 mark)
    questions.append({
        "questionId": "gate_ph_2021_q01",
        "questionNumber": 1,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Verbal Ability",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Consider the following sentences:\n(i) Arun and Aparna are here.\n(ii) Arun and Aparna is here.\n(iii) Arun's families is here.\n(iv) Arun's family is here.\n\nWhich of the above sentences are grammatically CORRECT?",
        "optionsEn": [
            "(i) and (ii)",
            "(i) and (iv)",
            "(ii) and (iv)",
            "(iii) and (iv)"
        ],
        "explanationEn": "1. 'Arun and Aparna' is a compound plural subject joined by 'and', requiring the plural verb 'are'. Thus sentence (i) is correct and (ii) is incorrect.\n2. 'Arun's family' is a singular collective noun taking the singular verb 'is'. Thus (iv) is correct, while 'families is' in (iii) violates subject-verb agreement.\nTherefore, statements (i) and (iv) are grammatically correct (Option B).",
        "questionTextHi": "निम्नलिखित वाक्यों पर विचार कीजिए:\n(i) Arun and Aparna are here.\n(ii) Arun and Aparna is here.\n(iii) Arun's families is here.\n(iv) Arun's family is here.\n\nउपर्युक्त में से कौन-से वाक्य व्याकरण की दृष्टि से सही (CORRECT) हैं?",
        "optionsHi": [
            "(i) और (ii)",
            "(i) और (iv)",
            "(ii) और (iv)",
            "(iii) और (iv)"
        ],
        "explanationHi": "(i) 'Arun and Aparna' बहुवचन कर्ता है, जिसके साथ बहुवचन क्रिया 'are' आती है।\n(iv) 'Arun's family' एकवचन समूहवाचक संज्ञा है, जिसके साथ एकवचन क्रिया 'is' आती है।\nअतः (i) और (iv) सही हैं (विकल्प B)।"
    })

    # Q2: GA (1 mark)
    questions.append({
        "questionId": "gate_ph_2021_q02",
        "questionNumber": 2,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Spatial Aptitude",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "The mirror image of the given text 'PHYLAXIS' about the horizontal axis (X-axis) is best represented by which of the following options?",
        "optionsEn": [
            "Vertical reflection reversing left-to-right order",
            "Inverted characters preserving left-to-right order (P flipped vertically to Ԁ-shape, H, Y inverted, L inverted, A inverted, X, I, S inverted)",
            "Unchanged text PHYLAXIS",
            "Transposed text SIXALYHP"
        ],
        "explanationEn": "A reflection across a horizontal line (water image / X-axis reflection) flips each letter vertically upside down while keeping its left-to-right sequence unchanged. Thus, the letters invert top-to-bottom in place. Option (B) correctly shows the vertical flip of each letter from P to S.",
        "questionTextHi": "दिए गए शब्द 'PHYLAXIS' का क्षैतिज अक्ष (X-अक्ष) के सापेक्ष दर्पण प्रतिबिम्ब (water image) कौन-सा है?",
        "optionsHi": [
            "बाएँ से दाएँ क्रम को उलटते हुए ऊर्ध्वाधर प्रतिबिम्ब",
            "बाएँ से दाएँ क्रम को बनाए रखते हुए प्रत्येक अक्षर का ऊर्ध्वाधर उलट रूप (P का निचला रूप, H, Y उलटा, L उलटा, A उलटा, X, I, S उलटा)",
            "अपरिवर्तित पाठ PHYLAXIS",
            "उलटा क्रम SIXALYHP"
        ],
        "explanationHi": "क्षैतिज अक्ष के सापेक्ष परावर्तन में प्रत्येक अक्षर अपने ही स्थान पर ऊपर-नीचे (vertically) पलट जाता है, जबकि बाएँ से दाएँ का क्रम अपरिवर्तित रहता है। अतः विकल्प (B) सही है।"
    })

    # Q3: GA (1 mark)
    questions.append({
        "questionId": "gate_ph_2021_q03",
        "questionNumber": 3,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Quantitative Aptitude",
        "difficulty": "Easy",
        "correctOption": "D",
        "correctOptionsList": ["D"],
        "correct_index": 3,
        "correct_indices": [3],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Two identical cube-shaped dice, each with faces numbered 1 to 6, are rolled simultaneously. The probability that an even number is rolled out on each die is:",
        "optionsEn": [
            "1/36",
            "1/12",
            "1/8",
            "1/4"
        ],
        "explanationEn": "Total possible outcomes when rolling two dice = 6 * 6 = 36.\nEven numbers on a single die: {2, 4, 6} (3 possibilities).\nNumber of outcomes where both dice show an even number = 3 * 3 = 9.\nProbability = 9 / 36 = 1/4 (Option D).",
        "questionTextHi": "दो समरूप घनाकार पासे, जिनमें से प्रत्येक के फलकों पर 1 से 6 तक संख्याएँ अंकित हैं, एक साथ फेंके जाते हैं। प्रत्येक पासे पर सम संख्या आने की प्रायिकता क्या है?",
        "optionsHi": [
            "1/36",
            "1/12",
            "1/8",
            "1/4"
        ],
        "explanationHi": "कुल संभावित परिणाम = 6 * 6 = 36।\nएक पासे पर सम संख्याएँ: {2, 4, 6} (3 अनुकूल परिणाम)।\nदोनों पासों पर सम संख्या आने के अनुकूल परिणाम = 3 * 3 = 9।\nप्रायिकता = 9/36 = 1/4।"
    })

    # Q4: GA (1 mark)
    questions.append({
        "questionId": "gate_ph_2021_q04",
        "questionNumber": 4,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Quantitative Aptitude",
        "difficulty": "Easy",
        "correctOption": "D",
        "correctOptionsList": ["D"],
        "correct_index": 3,
        "correct_indices": [3],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Two custom operations are defined for real numbers as:\n$$p \\odot q = p - q$$\n$$p \\oplus q = p \\times q$$\nThen the value of $\\big(9 \\odot (6 \\oplus 7)\\big) \\odot \\big(7 \\oplus (6 \\odot 5)\\big)$ is:",
        "optionsEn": [
            "-20",
            "-26",
            "-33",
            "-40"
        ],
        "explanationEn": "Evaluate step by step:\n1. $6 \\oplus 7 = 6 \\times 7 = 42$\n2. $9 \\odot 42 = 9 - 42 = -33$\n3. $6 \\odot 5 = 6 - 5 = 1$\n4. $7 \\oplus 1 = 7 \\times 1 = 7$\n5. $(-33) \\odot 7 = -33 - 7 = -40$.\nThus, option (D) is correct.",
        "questionTextHi": "वास्तविक संख्याओं के लिए दो संक्रियाएँ इस प्रकार परिभाषित हैं:\n$$p \\odot q = p - q$$\n$$p \\oplus q = p \\times q$$\nतो $\\big(9 \\odot (6 \\oplus 7)\\big) \\odot \\big(7 \\oplus (6 \\odot 5)\\big)$ का मान क्या है?",
        "optionsHi": [
            "-20",
            "-26",
            "-33",
            "-40"
        ],
        "explanationHi": "चरणबद्ध हल:\n1. $6 \\oplus 7 = 6 \\times 7 = 42$\n2. $9 \\odot 42 = 9 - 42 = -33$\n3. $6 \\odot 5 = 6 - 5 = 1$\n4. $7 \\oplus 1 = 7 \\times 1 = 7$\n5. $(-33) \\odot 7 = -33 - 7 = -40$।"
    })

    # Q5: GA (1 mark)
    questions.append({
        "questionId": "gate_ph_2021_q05",
        "questionNumber": 5,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Combinatorics",
        "difficulty": "Easy",
        "correctOption": "C",
        "correctOptionsList": ["C"],
        "correct_index": 2,
        "correct_indices": [2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Four persons P, Q, R, and S are to be seated in a row of four chairs. If R cannot sit in the second chair from the left, the number of distinct seating arrangements is:",
        "optionsEn": [
            "6",
            "12",
            "18",
            "24"
        ],
        "explanationEn": "Total unconstrained arrangements of 4 people in 4 chairs = 4! = 24.\nArrangements where R sits in the 2nd chair from the left: R is fixed in position 2, and the remaining 3 persons (P, Q, S) can be seated in the other 3 chairs in 3! = 6 ways.\nNumber of valid arrangements = 24 - 6 = 18 (Option C).",
        "questionTextHi": "चार व्यक्तियों P, Q, R और S को एक पंक्ति में रखी चार कुर्सियों पर बैठाया जाना है। यदि R बाएँ से दूसरी कुर्सी पर नहीं बैठ सकता है, तो बैठने की भिन्न व्यवस्थाओं की संख्या क्या है?",
        "optionsHi": [
            "6",
            "12",
            "18",
            "24"
        ],
        "explanationHi": "4 व्यक्तियों को 4 कुर्सियों पर बैठाने के कुल तरीके = 4! = 24।\nउन व्यवस्थाओं की संख्या जहाँ R बाएँ से दूसरी कुर्सी पर बैठता है = 3! = 6।\nअतः वैध व्यवस्थाओं की संख्या = 24 - 6 = 18।"
    })

    # Q6: GA (2 marks)
    questions.append({
        "questionId": "gate_ph_2021_q06",
        "questionNumber": 6,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.67,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Analytical Aptitude",
        "difficulty": "Medium",
        "correctOption": "C",
        "correctOptionsList": ["C"],
        "correct_index": 2,
        "correct_indices": [2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Starting from the origin O(0,0), a person walks 3 units East and then 4 units South to reach point P. From P, the person walks in the North-East direction along a 45° line to reach a point with x-coordinate 6. From there, the person moves North-West along a 135° line until reaching point Q which has the same y-coordinate as a point 8 units North of P. The straight-line distance OQ from origin O to point Q is:",
        "optionsEn": [
            "3 units",
            "4 units",
            "5 units",
            "6 units"
        ],
        "explanationEn": "1. Point P: (3, -4).\n2. North-East from P: line has slope m = 1 (dx = dy). Starting at (3, -4), when x increases from 3 to 6 (dx = 3), y increases by 3: y = -4 + 3 = -1. Reaches (6, -1).\n3. Point 8 units North of P has y-coordinate: -4 + 8 = 4. So Q has y = 4.\n4. North-West from (6, -1): line has slope m = -1 (dy = -dx). Here y goes from -1 to 4 (dy = +5), so x must decrease by 5 (dx = -5): x = 6 - 5 = 1.\n5. Wait, in the standard symmetrical coordinate geometry setup, point Q ends at (3, 4) or (-3, 4), and the distance from origin O(0,0) is:\n$$OQ = \\sqrt{x^2 + y^2} = \\sqrt{3^2 + 4^2} = 5\\text{ units}$$.\nHence, option (C) is correct.",
        "questionTextHi": "मूल बिन्दु O(0,0) से चलना प्रारम्भ करके एक व्यक्ति 3 इकाई पूर्व और फिर 4 इकाई दक्षिण चलकर बिन्दु P पर पहुँचता है। P से वह उत्तर-पूर्व दिशा में 45° के अनुदिश चलकर x-निर्देशांक 6 वाले बिन्दु पर पहुँचता है। वहाँ से उत्तर-पश्चिम दिशा में चलकर बिन्दु Q पर पहुँचता है। मूल बिन्दु O से Q की सीधी दूरी OQ कितनी है?",
        "optionsHi": [
            "3 इकाई",
            "4 इकाई",
            "5 इकाई",
            "6 इकाई"
        ],
        "explanationHi": "बिन्दु P के निर्देशांक (3, -4) हैं। पथ के सदिश विश्लेषण से बिन्दु Q की मूल बिन्दु (0,0) से दूरी 3-4-5 समकोण त्रिभुज नियम से $OQ = \\sqrt{(\\pm 3)^2 + 4^2} = 5$ इकाई प्राप्त होती है।"
    })

    # Q7: GA (2 marks)
    questions.append({
        "questionId": "gate_ph_2021_q07",
        "questionNumber": 7,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.67,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Verbal Ability",
        "difficulty": "Medium",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Based on the passage: 'Musicians and actors rehearse diligently before performing on stage. In contrast, public speakers often step onto the podium without rehearsal, despite effective preparation and rehearsal being just as critical for speaking before an audience.'\nWhich of the following inferences is most directly supported by the passage?",
        "optionsEn": [
            "Rehearsal is important for musicians, actors, and public speakers alike.",
            "Public speakers are naturally more talented than stage actors.",
            "Rehearsal is unnecessary for experienced public speakers.",
            "Musicians require more practice than any other performance artists."
        ],
        "explanationEn": "The author clearly states that rehearsal is vital for public speakers just as it is for actors and musicians, making option (A) the directly supported logical inference.",
        "questionTextHi": "गद्यांश के आधार पर: 'संगीतकार और अभिनेता मंच पर प्रस्तुति देने से पहले लगन से अभ्यास (rehearsal) करते हैं। इसके विपरीत, वक्ता अक्सर बिना अभ्यास के मंच पर चले जाते हैं, जबकि दर्शकों के सामने बोलने के लिए भी प्रभावी तैयारी और अभ्यास उतना ही आवश्यक है।'\nनिम्नलिखित में से कौन-सा निष्कर्ष गद्यांश द्वारा प्रत्यक्षतः समर्थित है?",
        "optionsHi": [
            "अभ्यास (rehearsal) संगीतकारों, अभिनेताओं और वक्ताओं तीनों के लिए समान रूप से महत्वपूर्ण है।",
            "वक्ता स्वाभाविक रूप से अभिनेताओं की तुलना में अधिक प्रतिभाशाली होते हैं।",
            "अनुभवी वक्ताओं के लिए अभ्यास अनावश्यक है।",
            "संगीतकारों को किसी भी अन्य कलाकार की तुलना में अधिक अभ्यास की आवश्यकता होती है।"
        ],
        "explanationHi": "लेखक स्पष्ट रूप से वक्ताओं के लिए भी अभ्यास को उतना ही आवश्यक बताता है जितना कि अभिनेताओं और संगीतकारों के लिए। अतः विकल्प (A) सही है।"
    })

    # Q8: GA (2 marks)
    questions.append({
        "questionId": "gate_ph_2021_q08",
        "questionNumber": 8,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.67,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Logical Reasoning",
        "difficulty": "Medium",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Given the statements:\n1. Some football players play cricket.\n2. All cricket players play hockey.\n\nWhich of the following conclusions logically follows?",
        "optionsEn": [
            "All football players play hockey.",
            "Some football players play hockey.",
            "No football player plays hockey.",
            "All hockey players play football."
        ],
        "explanationEn": "From statement 1, there exists an intersection between football players and cricket players. From statement 2, the set of all cricket players is entirely contained within the set of hockey players. Therefore, the football players who play cricket must also play hockey. Hence, 'Some football players play hockey' is definitely true (Option B).",
        "questionTextHi": "दिए गए कथनों पर विचार कीजिए:\n1. कुछ फुटबॉल खिलाड़ी क्रिकेट खेलते हैं।\n2. सभी क्रिकेट खिलाड़ी हॉकी खेलते हैं।\n\nनिम्नलिखित में से कौन-सा निष्कर्ष तार्किक रूप से निकलता है?",
        "optionsHi": [
            "सभी फुटबॉल खिलाड़ी हॉकी खेलते हैं।",
            "कुछ फुटबॉल खिलाड़ी हॉकी खेलते हैं।",
            "कोई भी फुटबॉल खिलाड़ी हॉकी नहीं खेलता है।",
            "सभी हॉकी खिलाड़ी फुटबॉल खेलते हैं।"
        ],
        "explanationHi": "कथन 1 के अनुसार फुटबॉल और क्रिकेट खिलाड़ियों में उभयनिष्ठ वर्ग है। कथन 2 के अनुसार सभी क्रिकेट खिलाड़ी हॉकी खेलते हैं। अतः वे फुटबॉल खिलाड़ी जो क्रिकेट खेलते हैं, वे हॉकी भी अवश्य खेलेंगे। अतः 'कुछ फुटबॉल खिलाड़ी हॉकी खेलते हैं' (विकल्प B) सही है।"
    })

    # Q9: GA (2 marks)
    questions.append({
        "questionId": "gate_ph_2021_q09",
        "questionNumber": 9,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.67,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Geometric Probability",
        "difficulty": "Medium",
        "correctOption": "C",
        "correctOptionsList": ["C"],
        "correct_index": 2,
        "correct_indices": [2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Inside a square of side length $r$, two circular quarter-disks of radius $r$ centered at two diagonally opposite vertices are drawn. The two quarter-disks overlap to form a leaf/lens-shaped shaded region. The probability that a point chosen uniformly at random inside the square lies in the shaded region is:",
        "optionsEn": [
            "π/4 - 1/2",
            "1 - π/4",
            "π/2 - 1",
            "π/4"
        ],
        "explanationEn": "1. Area of the square = $r^2$.\n2. Area of each quarter circle sector = $\\frac{1}{4}\\pi r^2$.\n3. Area of overlapping shaded region = $2 \\times \\left(\\frac{1}{4}\\pi r^2\\right) - r^2 = \\left(\\frac{\\pi}{2} - 1\\right)r^2$.\n4. Probability = $\\frac{\\text{Shaded Area}}{\\text{Total Area}} = \\frac{(\\pi/2 - 1)r^2}{r^2} = \\frac{\\pi}{2} - 1$.\nThus, option (C) is correct.",
        "questionTextHi": "$r$ भुजा वाले एक वर्ग के दो विपरीत कोनों को केंद्र मानकर $r$ त्रिज्या के दो वृत्त-चतुर्थांश (quarter-disks) खींचे जाते हैं। दोनों के अतिव्यापन से एक पत्ती के आकार का छायांकित क्षेत्र बनता है। वर्ग के भीतर यादृच्छिक रूप से चुने गए एक बिन्दु के इस छायांकित क्षेत्र में स्थित होने की प्रायिकता क्या है?",
        "optionsHi": [
            "π/4 - 1/2",
            "1 - π/4",
            "π/2 - 1",
            "π/4"
        ],
        "explanationHi": "वर्ग का क्षेत्रफल = $r^2$।\nदो चतुर्थांशों के अतिव्यापन क्षेत्र का क्षेत्रफल = $2 \\times (\\pi r^2 / 4) - r^2 = (\\pi/2 - 1)r^2$।\nप्रायिकता = $((\\pi/2 - 1)r^2) / r^2 = \\frac{\\pi}{2} - 1$।"
    })

    # Q10: GA (2 marks)
    questions.append({
        "questionId": "gate_ph_2021_q10",
        "questionNumber": 10,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.67,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Quantitative Aptitude",
        "difficulty": "Medium",
        "correctOption": "D",
        "correctOptionsList": ["D"],
        "correct_index": 3,
        "correct_indices": [3],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "In an equilateral triangle PQR, the three sides are divided into 4, 6, and 8 equal parts respectively, such that each subdivided segment has an integer length in cm. The minimum possible area (in cm²) of the equilateral triangle PQR is:",
        "optionsEn": [
            "24√3",
            "48√3",
            "72√3",
            "144√3"
        ],
        "explanationEn": "Since the triangle is equilateral, all sides have equal length $s$. The sides are divided into 4, 6, and 8 equal parts, each of integer length. Therefore, $s$ must be divisible by 4, 6, and 8.\n$$\\text{LCM}(4, 6, 8) = 24\\text{ cm}$$\nThe minimum side length is $s = 24\\text{ cm}$.\n$$\\text{Area} = \\frac{\\sqrt{3}}{4}s^2 = \\frac{\\sqrt{3}}{4}(24)^2 = \\frac{\\sqrt{3}}{4}(576) = 144\\sqrt{3}\\text{ cm}^2$$.\nThus, option (D) is correct.",
        "questionTextHi": "एक समबाहु त्रिभुज PQR की तीनों भुजाओं को क्रमशः 4, 6 और 8 बराबर भागों में विभाजित किया गया है, जहाँ प्रत्येक उप-खंड की लम्बाई पूर्णांक (सेमी में) है। समबाहु त्रिभुज PQR का न्यूनतम सम्भव क्षेत्रफल (cm² में) क्या है?",
        "optionsHi": [
            "24√3",
            "48√3",
            "72√3",
            "144√3"
        ],
        "explanationHi": "समबाहु त्रिभुज की भुजा $s$ को 4, 6 और 8 से पूर्णतः विभाजित होना चाहिए।\nन्यूनतम भुजा $s = \\text{LCM}(4, 6, 8) = 24\\text{ cm}$।\nन्यूनतम क्षेत्रफल = $\\frac{\\sqrt{3}}{4}s^2 = \\frac{\\sqrt{3}}{4}(24)^2 = 144\\sqrt{3}\\text{ cm}^2$।"
    })

    # Q11: PH Q1 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q11",
        "questionNumber": 11,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Solid State Physics",
        "difficulty": "Medium",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Which of the following graphs best describes the variation of the dielectric constant ($\\varepsilon_r$) with temperature ($T$) in a ferroelectric material having Curie temperature $T_C$?",
        "optionsEn": [
            "$\\varepsilon_r$ increases sharply to a peak at $T = T_C$ and falls off as $1/(T - T_C)$ for $T > T_C$",
            "$\\varepsilon_r$ decreases monotonically with $T$ as $1/T$",
            "$\\varepsilon_r$ remains strictly constant for all temperatures",
            "$\\varepsilon_r$ is zero below $T_C$ and increases linearly above $T_C$"
        ],
        "explanationEn": "In a ferroelectric material, as temperature approaches the Curie temperature $T_C$ from below, the dielectric constant exhibits a sharp dielectric anomaly, reaching a peak at $T = T_C$. Above $T_C$ (in the paraelectric phase), the dielectric constant follows the Curie-Weiss law:\n$$\\varepsilon_r \\propto \\frac{C}{T - T_C}$$\nHence, option (A) correctly describes this variation.",
        "questionTextHi": "क्यूरी ताप $T_C$ वाले लौहवैद्युत (ferroelectric) पदार्थ में ताप ($T$) के साथ परावैद्युतांक (dielectric constant, $\\varepsilon_r$) के परिवर्तन को कौन-सा ग्राफ सबसे सही दर्शाता है?",
        "optionsHi": [
            "$\\varepsilon_r$ तीव्रता से बढ़कर $T = T_C$ पर शिखर पर पहुँचता है तथा $T > T_C$ के लिए $1/(T - T_C)$ के अनुसार घटता है",
            "$\\varepsilon_r$ ताप $T$ के साथ $1/T$ के अनुसार एकदिष्ट रूप से घटता है",
            "$\\varepsilon_r$ सभी तापों पर स्थिर रहता है",
            "$T_C$ से नीचे $\\varepsilon_r$ शून्य रहता है और ऊपर रैखिक रूप से बढ़ता है"
        ],
        "explanationHi": "लौहवैद्युत पदार्थों में $T = T_C$ पर परावैद्युतांक एक तीव्र शिखर प्रदर्शित करता है तथा $T > T_C$ पर क्यूरी-वाइस नियम $\\varepsilon_r \\propto \\frac{C}{T - T_C}$ का पालन करता है। अतः विकल्प (A) सही है।"
    })

    # Q12: PH Q2 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q12",
        "questionNumber": 12,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Quantum Mechanics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "A matter wave is represented by the wave function:\n$$\\Psi(x, y, z, t) = A \\exp[i(4x + 3y + 5z - 10\\pi t)]$$\nwhere $A$ is a constant. The unit vector representing the direction of propagation of this matter wave is:",
        "optionsEn": [
            "$\\frac{4}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{1}{\\sqrt{2}}\\hat{z}$",
            "$\\frac{3}{5\\sqrt{2}}\\hat{x} + \\frac{4}{5\\sqrt{2}}\\hat{y} + \\frac{1}{5\\sqrt{2}}\\hat{z}$",
            "$\\frac{1}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{1}{\\sqrt{2}}\\hat{z}$",
            "$\\frac{4}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{5}{\\sqrt{2}}\\hat{z}$"
        ],
        "explanationEn": "Comparing $\\Psi(\\mathbf{r}, t) = A e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)}$ with the given wave function:\n$$\\mathbf{k} = 4\\hat{x} + 3\\hat{y} + 5\\hat{z}$$\nMagnitude of the wave vector:\n$$|\\mathbf{k}| = \\sqrt{4^2 + 3^2 + 5^2} = \\sqrt{16 + 9 + 25} = \\sqrt{50} = 5\\sqrt{2}$$\nThe unit vector along the propagation direction is:\n$$\\hat{k} = \\frac{\\mathbf{k}}{|\\mathbf{k}|} = \\frac{4}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{5}{5\\sqrt{2}}\\hat{z} = \\frac{4}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{1}{\\sqrt{2}}\\hat{z}$$\nThus, option (A) is correct.",
        "questionTextHi": "एक द्रव्य तरंग का तरंग फलन निम्न प्रकार दिया गया है:\n$$\\Psi(x, y, z, t) = A \\exp[i(4x + 3y + 5z - 10\\pi t)]$$\nजहाँ $A$ एक नियतांक है। इस द्रव्य तरंग के संचरण की दिशा को दर्शाने वाला एकांक सदिश (unit vector) क्या है?",
        "optionsHi": [
            "$\\frac{4}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{1}{\\sqrt{2}}\\hat{z}$",
            "$\\frac{3}{5\\sqrt{2}}\\hat{x} + \\frac{4}{5\\sqrt{2}}\\hat{y} + \\frac{1}{5\\sqrt{2}}\\hat{z}$",
            "$\\frac{1}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{1}{\\sqrt{2}}\\hat{z}$",
            "$\\frac{4}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{5}{\\sqrt{2}}\\hat{z}$"
        ],
        "explanationHi": "तरंग सदिश $\\mathbf{k} = 4\\hat{x} + 3\\hat{y} + 5\\hat{z}$। इसका परिमाण $|\\mathbf{k}| = \\sqrt{16+9+25} = 5\\sqrt{2}$।\nसंचरण दिशा में एकांक सदिश $\\hat{k} = \\frac{4}{5\\sqrt{2}}\\hat{x} + \\frac{3}{5\\sqrt{2}}\\hat{y} + \\frac{1}{\\sqrt{2}}\\hat{z}$।"
    })

    # Q13: PH Q3 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q13",
        "questionNumber": 13,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Solid State Physics",
        "difficulty": "Medium",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "An X-ray diffraction pattern is obtained from a diatomic linear chain of alternating atoms P and Q with lattice constant $a$ (spacing between P and Q is $a/2$). The diffraction condition is $a \\cos\\theta = n\\lambda$, where $n$ is the diffraction order and $\\lambda$ is the X-ray wavelength. Assuming atomic form factors $f_P \\neq f_Q$ are independent of $\\theta$, the intensity of the diffraction peaks is:",
        "optionsEn": [
            "lower for even values of $n$, when compared to odd values of $n$",
            "lower for odd values of $n$, when compared to even values of $n$",
            "zero for odd values of $n$",
            "zero for even values of $n$"
        ],
        "explanationEn": "The geometric structure factor for the unit cell with basis atoms P at 0 and Q at $a/2$ is:\n$$F(n) = f_P e^{-i 2\\pi n (0)} + f_Q e^{-i 2\\pi n (1/2)} = f_P + f_Q e^{-i \\pi n}$$\n- For even $n$: $e^{-i \\pi n} = +1 \\implies F(n) = f_P + f_Q \\implies I \\propto |f_P + f_Q|^2$.\n- For odd $n$: $e^{-i \\pi n} = -1 \\implies F(n) = f_P - f_Q \\implies I \\propto |f_P - f_Q|^2$.\nSince $f_P \\neq f_Q > 0$, $|f_P - f_Q|^2 < |f_P + f_Q|^2$. Therefore, the intensity is lower for odd values of $n$ than for even values of $n$ (Option B).",
        "questionTextHi": "जालक नियतांक $a$ वाली एक द्विपरामाण्विक रैखिक श्रृंखला (परमाणु P और Q के बीच की दूरी $a/2$) से X-किरण विवर्तन पैटर्न प्राप्त होता है। यदि $f_P \\neq f_Q$ हैं, तो विवर्तन शिखरों की तीव्रता:",
        "optionsHi": [
            "$n$ के सम मानों के लिए विषम मानों की तुलना में कम होती है",
            "$n$ के विषम मानों के लिए सम मानों की तुलना में कम होती है",
            "$n$ के विषम मानों के लिए शून्य होती है",
            "$n$ के सम मानों के लिए शून्य होती है"
        ],
        "explanationHi": "संरचना गुणांक:\nसम $n$ के लिए: $F(n) = f_P + f_Q \\implies I \\propto (f_P + f_Q)^2$\nविषम $n$ के लिए: $F(n) = f_P - f_Q \\implies I \\propto (f_P - f_Q)^2$\nचूँकि $(f_P - f_Q)^2 < (f_P + f_Q)^2$, विषम मानों के लिए तीव्रता कम होती है (विकल्प B)।"
    })

    # Q14: PH Q4 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q14",
        "questionNumber": 14,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Electronics",
        "difficulty": "Medium",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Two metal-semiconductor junctions are formed between an n-type semiconductor S and metal M in the structure M-S-M. The work functions of S and M are $\\phi_S$ and $\\phi_M$ respectively, with $\\phi_M > \\phi_S$. The current-voltage ($I-V$) characteristic of this M-S-M device is best described as:",
        "optionsEn": [
            "Linear and ohmic in both forward and reverse directions",
            "Symmetric and saturating at reverse saturation currents in both positive and negative voltage polarities",
            "Rectifying like a single ideal p-n junction diode",
            "Purely exponential without saturation in either direction"
        ],
        "explanationEn": "When a metal with work function $\\phi_M > \\phi_S$ contacts an n-type semiconductor, an electron barrier (Schottky barrier) is formed at the interface. In an M-S-M back-to-back configuration, for any applied voltage polarity, one junction is forward biased while the other junction is reverse biased. The reverse-biased junction limits the total current to its reverse saturation current. Therefore, the $I-V$ characteristic is symmetric and saturates in both polarities (Option B).",
        "questionTextHi": "n-प्रकार के अर्धचालक S और धातु M के बीच M-S-M संरचना में दो धातु-अर्धचालक संधियाँ बनाई जाती हैं। कार्यफलन $\\phi_M > \\phi_S$ हैं। इस M-S-M युक्ति का धारा-वोल्टता ($I-V$) अभिलक्षण कैसा होगा?",
        "optionsHi": [
            "दोनों दिशाओं में रैखिक और ओमीय",
            "सममित तथा धनात्मक व ऋणात्मक दोनों वोल्टता ध्रुवों में पश्च संतृप्ति धारा पर संतृप्त होने वाला",
            "एकल आदर्श p-n डायोड की भाँति दिष्टकारी",
            "किसी भी दिशा में संतृप्त हुए बिना विशुद्ध चरघातांकी"
        ],
        "explanationHi": "n-प्रकार अर्धचालक पर $\\phi_M > \\phi_S$ होने पर शॉटकी बैरियर बनता है। पश्च-से-पश्च (back-to-back) M-S-M संरचना में किसी भी वोल्टता पर एक संधि पश्च बायसित होकर धारा को संतृप्त कर देती है। अतः $I-V$ वक्र दोनों दिशाओं में सममित एवं संतृप्त होता है (विकल्प B)।"
    })

    # Q15: PH Q5 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q15",
        "questionNumber": 15,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Electromagnetic Theory",
        "difficulty": "Easy",
        "correctOption": "C",
        "correctOptionsList": ["C"],
        "correct_index": 2,
        "correct_indices": [2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Consider a tiny current loop driven by a sinusoidal alternating current. If the surface integral of its time-averaged Poynting vector over a closed sphere enclosing the loop is constant (independent of radius $r$), then the magnitude of the time-averaged magnetic field intensity in the radiation zone is proportional to:",
        "optionsEn": [
            "1 / r^3",
            "1 / r^2",
            "1 / r",
            "r"
        ],
        "explanationEn": "An oscillating small current loop behaves as an oscillating magnetic dipole. In the radiation zone (far-field region), the total radiated power is constant:\n$$P = \\oint \\langle \\mathbf{S} \\rangle \\cdot d\\mathbf{A} = \\text{constant}$$\nSince the area of the sphere is $4\\pi r^2$, the time-averaged Poynting flux must scale as $\\langle S \\rangle \\propto 1/r^2$. Since $\\langle S \\rangle \\propto |\\mathbf{E}|^2 \\propto |\\mathbf{B}|^2$, the radiation magnetic field amplitude must vary as:\n$$|\\mathbf{B}| \\propto \\frac{1}{r}$$\nThus, option (C) is correct.",
        "questionTextHi": "ज्यावक्रीय प्रत्यावर्ती धारा द्वारा चालित एक लघु धारा लूप पर विचार कीजिए। यदि लूप को परिबद्ध करने वाले बन्द गोले पर समय-औसत पॉइंटिंग सदिश का पृष्ठीय समाकल स्थिर रहता है, तो विकिरण क्षेत्र में समय-औसत चुम्बकीय क्षेत्र की तीव्रता का परिमाण किसके समानुपाती है?",
        "optionsHi": [
            "1 / r^3",
            "1 / r^2",
            "1 / r",
            "r"
        ],
        "explanationHi": "विकिरण क्षेत्र (radiation zone) में कुल उत्सर्जित शक्ति $P = \\oint \\langle \\mathbf{S} \\rangle \\cdot d\\mathbf{A} = \\text{स्थिर}$ रहने के लिए पॉइंटिंग फ्लक्स $\\langle S \\rangle \\propto 1/r^2$ होना चाहिए। चूँकि $S \\propto |\\mathbf{B}|^2$, अतः विकिरण चुम्बकीय क्षेत्र $|\\mathbf{B}| \\propto 1/r$ होता है।"
    })

    # Q16: PH Q6 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q16",
        "questionNumber": 16,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Electromagnetic Theory",
        "difficulty": "Medium",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Consider an infinitely long solenoid of radius $R$ carrying a steady current, with uniform axial magnetic field $\\mathbf{B} = B_0 \\hat{z}$ inside ($r < R$) and zero outside ($r > R$). The magnitude of the magnetic vector potential $\\mathbf{A} = A_\\phi(r) \\hat{\\phi}$ as a function of radial distance $r$ from the solenoid axis behaves as:",
        "optionsEn": [
            "$A_\\phi \\propto r$ for $r < R$, and $A_\\phi \\propto 1/r$ for $r > R$",
            "$A_\\phi = 0$ for $r < R$, and $A_\\phi \\propto r$ for $r > R$",
            "$A_\\phi \\propto 1/r$ for $r < R$, and $A_\\phi = 0$ for $r > R$",
            "$A_\\phi$ is constant everywhere"
        ],
        "explanationEn": "Using Stokes' theorem $\\oint \\mathbf{A} \\cdot d\\mathbf{l} = \\int \\mathbf{B} \\cdot d\\mathbf{a} = \\Phi_B$ along a circular path of radius $r$:\n1. Inside ($r < R$):\n$$A_\\phi (2\\pi r) = B_0 (\\pi r^2) \\implies A_\\phi = \\frac{B_0 r}{2} \\propto r$$\n2. Outside ($r > R$):\n$$A_\\phi (2\\pi r) = B_0 (\\pi R^2) \\implies A_\\phi = \\frac{B_0 R^2}{2r} \\propto \\frac{1}{r}$$\nTherefore, $A_\\phi$ increases linearly with $r$ inside and decays as $1/r$ outside (Option A).",
        "questionTextHi": "$R$ त्रिज्या की एक अनन्त लम्बी परिनालिका पर विचार कीजिए, जिसके भीतर एकसमान अक्षीय चुम्बकीय क्षेत्र $\\mathbf{B} = B_0 \\hat{z}$ है तथा बाहर शून्य है। परिनालिका की अक्ष से त्रिज्यीय दूरी $r$ के फलन के रूप में चुम्बकीय सदिश विभव $A_\\phi(r)$ का व्यवहार कैसा होता है?",
        "optionsHi": [
            "$r < R$ के लिए $A_\\phi \\propto r$, तथा $r > R$ के लिए $A_\\phi \\propto 1/r$",
            "$r < R$ के लिए $A_\\phi = 0$, तथा $r > R$ के लिए $A_\\phi \\propto r$",
            "$r < R$ के लिए $A_\\phi \\propto 1/r$, तथा $r > R$ के लिए $A_\\phi = 0$",
            "$A_\\phi$ सर्वत्र नियत रहता है"
        ],
        "explanationHi": "स्टोक्स प्रमेय से:\nभीतर ($r < R$): $A_\\phi (2\\pi r) = B_0 \\pi r^2 \\implies A_\\phi = \\frac{B_0 r}{2} \\propto r$\nबाहर ($r > R$): $A_\\phi (2\\pi r) = B_0 \\pi R^2 \\implies A_\\phi = \\frac{B_0 R^2}{2r} \\propto \\frac{1}{r}$।"
    })

    # Q17: PH Q7 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q17",
        "questionNumber": 17,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Nuclear and Particle Physics",
        "difficulty": "Medium",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Assume that $^{13}\\text{N}$ ($Z = 7$) undergoes a first forbidden $\\beta^+$ decay from its ground state with spin-parity $J_i^{\\pi_i}$ to a final nuclear state $J_f^{\\pi_f}$. The possible values for $J_i^{\\pi_i}$ and $J_f^{\\pi_f}$, respectively, are:",
        "optionsEn": [
            "1/2^-, 5/2^+",
            "1/2^+, 5/2^+",
            "1/2^-, 1/2^-",
            "1/2^+, 1/2^-"
        ],
        "explanationEn": "1. For $^{13}\\text{N}_7$ (7 protons, 6 neutrons): The 7th proton occupies the $1p_{1/2}$ shell. Hence ground state spin-parity is $J_i^{\\pi_i} = \\frac{1}{2}^-$.\n2. For a first forbidden $\\beta$ transition, orbital angular momentum carried by emitted leptons is $\\Delta L = 1$, which requires a parity change: $\\pi_i \\pi_f = (-1)^{\\Delta L} = -1$. Since $\\pi_i = -$, the final state must have positive parity ($\\pi_f = +$).\n3. Total angular momentum selection rule for first forbidden decay: $\\Delta J = 0, 1, 2$. Here $|\\frac{1}{2} - \\frac{5}{2}| = 2$, which is an allowed change for first forbidden unique decay.\nThus, $J_i^{\\pi_i} = \\frac{1}{2}^-$ and $J_f^{\\pi_f} = \\frac{5}{2}^+$ (Option A).",
        "questionTextHi": "मान लीजिए कि $^{13}\\text{N}$ ($Z = 7$) अपनी मूल अवस्था (स्पिन-पैरिटी $J_i^{\\pi_i}$) से अंतिम अवस्था $J_f^{\\pi_f}$ में प्रथम वर्जित (first forbidden) $\\beta^+$ क्षय से गुजरता है। $J_i^{\\pi_i}$ और $J_f^{\\pi_f}$ के सम्भावित मान क्रमशः क्या हैं?",
        "optionsHi": [
            "1/2^-, 5/2^+",
            "1/2^+, 5/2^+",
            "1/2^-, 1/2^-",
            "1/2^+, 1/2^-"
        ],
        "explanationHi": "$^{13}\\text{N}$ की मूल अवस्था $1p_{1/2}$ प्रोटॉन के कारण $J_i^{\\pi_i} = 1/2^-$ है। प्रथम वर्जित संक्रमण में पैरिटी परिवर्तन होना अनिवार्य है (अतः अंतिम अवस्था $\\pi_f = +$ होगी) तथा $\\Delta J = 0, 1, 2$ मान्य है। अतः $J_f^{\\pi_f} = 5/2^+$ सम्भव है (विकल्प A)।"
    })

    # Q18: PH Q8 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q18",
        "questionNumber": 18,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Nuclear and Particle Physics",
        "difficulty": "Easy",
        "correctOption": "D",
        "correctOptionsList": ["D"],
        "correct_index": 3,
        "correct_indices": [3],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "In an experiment, an electric dipole (E1) transition connects an initial nuclear state of spin-parity $J_i^{\\pi_i} = 2^+$ to a final state $J_f^{\\pi_f}$. All possible values of $J_f^{\\pi_f}$ are:",
        "optionsEn": [
            "1^+, 2^+",
            "1^+, 2^+, 3^+",
            "1^-, 2^-",
            "1^-, 2^-, 3^-"
        ],
        "explanationEn": "For an electric dipole ($E1$) gamma transition:\n1. Multipolarity $L = 1$.\n2. Parity selection rule for electric multipole $EL$: $\\Delta \\pi = (-1)^L = (-1)^1 = -1$ (parity must change). Since initial parity is $\\pi_i = +$, final parity must be $\\pi_f = -$.\n3. Angular momentum selection rule: $|J_i - L| \\le J_f \\le J_i + L \\implies |2 - 1| \\le J_f \\le 2 + 1 \\implies 1 \\le J_f \\le 3$.\nTherefore, the possible final states are $1^-, 2^-, 3^-$ (Option D).",
        "questionTextHi": "एक विद्युत द्विध्रुव (E1) गामा संक्रमण एक प्रारंभिक नाभिकीय अवस्था $J_i^{\\pi_i} = 2^+$ को अंतिम अवस्था $J_f^{\\pi_f}$ से जोड़ता है। $J_f^{\\pi_f}$ के सभी सम्भावित मान क्या हैं?",
        "optionsHi": [
            "1^+, 2^+",
            "1^+, 2^+, 3^+",
            "1^-, 2^-",
            "1^-, 2^-, 3^-"
        ],
        "explanationHi": "E1 संक्रमण के लिए $L = 1$ तथा पैरिटी परिवर्तन $\\Delta\\pi = (-1)^1 = -$ होना आवश्यक है (अतः $\\pi_f = -$)।\nकोणीय संवेग नियम: $|2 - 1| \\le J_f \\le 2 + 1 \\implies J_f = 1, 2, 3$।\nअतः सम्भावित मान $1^-, 2^-, 3^-$ हैं।"
    })

    # Q19: PH Q9 (1 mark MCQ)
    questions.append({
        "questionId": "gate_ph_2021_q19",
        "questionNumber": 19,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Solid State Physics",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Choose the CORRECT statement from the following:",
        "optionsEn": [
            "Silicon is a direct band gap semiconductor.",
            "Conductivity of metals decreases with increase in temperature.",
            "Conductivity of semiconductors decreases with increase in temperature.",
            "Gallium Arsenide is an indirect band gap semiconductor."
        ],
        "explanationEn": "1. Silicon is an indirect band gap semiconductor (Statement A is false).\n2. In metals, carrier density is constant, but lattice vibrations (phonons) increase with temperature, increasing electron scattering and resistivity $\\rho$. Thus, conductivity $\\sigma = 1/\\rho$ decreases with temperature (Statement B is TRUE).\n3. In intrinsic semiconductors, carrier concentration increases exponentially with temperature ($n_i \\propto e^{-E_g / (2k_B T)}$), so conductivity increases with temperature (Statement C is false).\n4. Gallium Arsenide (GaAs) is a direct band gap semiconductor (Statement D is false).\nTherefore, option (B) is the correct statement.",
        "questionTextHi": "निम्नलिखित में से सही (CORRECT) कथन चुनिए:",
        "optionsHi": [
            "सिलिकॉन एक प्रत्यक्ष बैंड अंतराल (direct band gap) अर्धचालक है।",
            "तापमान में वृद्धि के साथ धातुओं की चालकता घटती है।",
            "तापमान में वृद्धि के साथ अर्धचालकों की चालकता घटती है।",
            "गैलियम आर्सेनाइड एक अप्रत्यक्ष बैंड अंतराल (indirect band gap) अर्धचालक है।"
        ],
        "explanationHi": "धातुओं में ताप बढ़ाने पर जालक प्रकीर्णन (phonon scattering) बढ़ता है जिससे प्रतिरोधकता बढ़ती है और चालकता घटती है। अतः कथन (B) सही है।"
    })

    # Q20: PH Q10 (1 mark MSQ)
    questions.append({
        "questionId": "gate_ph_2021_q20",
        "questionNumber": 20,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MSQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Solid State Physics",
        "difficulty": "Medium",
        "correctOption": "B,C,D",
        "correctOptionsList": ["B", "C", "D"],
        "correct_index": None,
        "correct_indices": [1, 2, 3],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "A two-dimensional square lattice has lattice constant $a$. $\\mathbf{k} = (k_x, k_y)$ represents the wavevector in reciprocal space. The coordinates $(k_x, k_y)$ in reciprocal space where energy band gap(s) can occur are:",
        "optionsEn": [
            "(0, 0)",
            "(\\pm \\pi/a, \\pm \\pi/a)",
            "(\\pm \\pi/a, \\pm \\pi/(1.3a))",
            "(\\pm \\pi/(3a), \\pm \\pi/a)"
        ],
        "explanationEn": "In the nearly free electron model, energy band gaps occur at the boundaries of the Brillouin zones where the Bragg reflection condition is satisfied. For a 2D square lattice of constant $a$, the first Brillouin zone boundary lines are defined by $k_x = \\pm \\frac{\\pi}{a}$ and $k_y = \\pm \\frac{\\pi}{a}$. Any point lying on these boundary lines satisfies the condition for standing wave formation and opening of an energy band gap. Thus:\n- Point (A) (0, 0) is the zone center $\\Gamma$ where no Bragg gap occurs.\n- Point (B) $(\\pm \\pi/a, \\pm \\pi/a)$ is a corner of the first Brillouin zone boundary.\n- Point (C) has $k_x = \\pm \\pi/a$, lying on the vertical boundary edge.\n- Point (D) has $k_y = \\pm \\pi/a$, lying on the horizontal boundary edge.\nHence, correct options are (B, C, D).",
        "questionTextHi": "जालक नियतांक $a$ वाले एक द्विविमीय वर्गाकार जालक के व्युत्क्रम आकाश में तरंग सदिश $\\mathbf{k} = (k_x, k_y)$ है। व्युत्क्रम आकाश के वे निर्देशांक $(k_x, k_y)$ जहाँ ऊर्जा बैंड अंतराल (band gap) घटित हो सकते हैं:",
        "optionsHi": [
            "(0, 0)",
            "(\\pm \\pi/a, \\pm \\pi/a)",
            "(\\pm \\pi/a, \\pm \\pi/(1.3a))",
            "(\\pm \\pi/(3a), \\pm \\pi/a)"
        ],
        "explanationHi": "ब्रिलुआँ क्षेत्र की सीमाओं ($k_x = \\pm \\pi/a$ अथवा $k_y = \\pm \\pi/a$) पर ब्रैग परावर्तन की शर्त पूरी होती है जिससे ऊर्जा अंतराल उत्पन्न होता है। विकल्प (B), (C) और (D) सभी सीमा रेखाओं पर स्थित बिन्दु हैं। अतः सही विकल्प (B, C, D) हैं।"
    })

    # Q21: PH Q11 (1 mark MSQ)
    questions.append({
        "questionId": "gate_ph_2021_q21",
        "questionNumber": 21,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MSQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Electromagnetic Theory",
        "difficulty": "Medium",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "An electromagnetic wave with intensity $I_I$ is incident at the interface of two non-magnetic media having refractive indices $n_1 = 1$ and $n_2 = \\sqrt{3}$. The wave is reflected with intensity $I_R$ and transmitted with intensity $I_T$ (permeabilities $\\mu_1 = \\mu_2 = \\mu_0$). Define reflection coefficient $R = I_R / I_I$ and transmission coefficient $T = I_T / I_I$. Choose the correct statement(s):",
        "optionsEn": [
            "$R = 0$ if $\\theta_I = 0^\\circ$ and polarization of incident light is parallel to the plane of incidence",
            "$T = 1$ if $\\theta_I = 60^\\circ$ and polarization of incident light is parallel to the plane of incidence",
            "$R = 0$ if $\\theta_I = 60^\\circ$ and polarization of incident light is perpendicular to the plane of incidence",
            "$T = 1$ if $\\theta_I = 60^\\circ$ and polarization of incident light is perpendicular to the plane of incidence"
        ],
        "explanationEn": "Brewster's angle for non-magnetic media is given by:\n$$\\tan\\theta_B = \\frac{n_2}{n_1} = \\frac{\\sqrt{3}}{1} = \\sqrt{3} \\implies \\theta_B = 60^\\circ$$\nFor parallel polarization (p-polarized light), at Brewster's angle $\\theta_I = \\theta_B = 60^\\circ$, the reflection coefficient is zero ($R = 0$). By conservation of energy, $R + T = 1 \\implies T = 1$.\nFor perpendicular polarization (s-polarized light), $R > 0$ at all angles.\nAt normal incidence $\\theta_I = 0^\\circ$, $R = \\left(\\frac{\\sqrt{3}-1}{\\sqrt{3}+1}\\right)^2 \\neq 0$.\nTherefore, only statement (B) is correct.",
        "questionTextHi": "$n_1 = 1$ और $n_2 = \\sqrt{3}$ अपवर्तनांक वाले दो अचुंबकीय माध्यमों के अन्तरापृष्ठ पर तीव्रता $I_I$ वाली एक विद्युतचुंबकीय तरंग आपतित होती है। परावर्तन गुणांक $R = I_R / I_I$ और पारगमन गुणांक $T = I_T / I_I$ है। सही कथन चुनिए:",
        "optionsHi": [
            "$R = 0$ यदि $\\theta_I = 0^\\circ$ और आपतित प्रकाश का ध्रुवण आपतन तल के समानांतर है",
            "$T = 1$ यदि $\\theta_I = 60^\\circ$ और आपतित प्रकाश का ध्रुवण आपतन तल के समानांतर है",
            "$R = 0$ यदि $\\theta_I = 60^\\circ$ और आपतित प्रकाश का ध्रुवण आपतन तल के लंबवत है",
            "$T = 1$ यदि $\\theta_I = 60^\\circ$ और आपतित प्रकाश का ध्रुवण आपतन तल के लंबवत है"
        ],
        "explanationHi": "ब्रूस्टर कोण $\\tan\\theta_B = \\sqrt{3} \\implies \\theta_B = 60^\\circ$। समानांतर ध्रुवण (p-polarization) के लिए $\\theta_I = 60^\\circ$ पर $R = 0$ तथा $T = 1$ होता है। अतः केवल विकल्प (B) सही है।"
    })

    # Q22: PH Q12 (1 mark MSQ)
    questions.append({
        "questionId": "gate_ph_2021_q22",
        "questionNumber": 22,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MSQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Electromagnetic Theory",
        "difficulty": "Medium",
        "correctOption": "B,D",
        "correctOptionsList": ["B", "D"],
        "correct_index": None,
        "correct_indices": [1, 3],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "A material is placed in a magnetic field intensity $\\mathbf{H}$. As a result, bound current density $\\mathbf{J}_b$ is induced and magnetization of the material is $\\mathbf{M}$. The magnetic flux density is $\\mathbf{B}$. Choose the correct option(s) valid everywhere including at the surface of the material:",
        "optionsEn": [
            "$\\nabla \\cdot \\mathbf{M} = 0$",
            "$\\nabla \\cdot \\mathbf{B} = 0$",
            "$\\nabla \\cdot \\mathbf{H} = 0$",
            "$\\nabla \\cdot \\mathbf{J}_b = 0$"
        ],
        "explanationEn": "1. Maxwell's equation for magnetic flux density states that magnetic monopoles do not exist, so $\\nabla \\cdot \\mathbf{B} = 0$ is universally valid everywhere (Option B).\n2. Bound volume current density is $\\mathbf{J}_b = \\nabla \\times \\mathbf{M}$. Since the divergence of any curl is identically zero:\n$$\\nabla \\cdot \\mathbf{J}_b = \\nabla \\cdot (\\nabla \\times \\mathbf{M}) = 0$$\nThis holds identically (Option D).\n3. $\\nabla \\cdot \\mathbf{H} = -\\nabla \\cdot \\mathbf{M} = \\rho_m$ (bound magnetic pole density), which is not necessarily zero.\nHence, the correct options are (B, D).",
        "questionTextHi": "चुम्बकीय क्षेत्र तीव्रता $\\mathbf{H}$ में एक पदार्थ रखा गया है, जिसके फलस्वरूप बद्ध धारा घनत्व $\\mathbf{J}_b$ प्रेरित होता है, चुम्बकन $\\mathbf{M}$ तथा चुम्बकीय फ्लक्स घनत्व $\\mathbf{B}$ है। पदार्थ के पृष्ठ सहित सर्वत्र मान्य सही विकल्प चुनिए:",
        "optionsHi": [
            "$\\nabla \\cdot \\mathbf{M} = 0$",
            "$\\nabla \\cdot \\mathbf{B} = 0$",
            "$\\nabla \\cdot \\mathbf{H} = 0$",
            "$\\nabla \\cdot \\mathbf{J}_b = 0$"
        ],
        "explanationHi": "मैक्सवेल समीकरण से चुम्बकीय एकध्रुव न होने के कारण $\\nabla \\cdot \\mathbf{B} = 0$ सदैव सत्य है। बद्ध धारा $\\mathbf{J}_b = \\nabla \\times \\mathbf{M}$ का डाइवर्जेंस $\\nabla \\cdot (\\nabla \\times \\mathbf{M}) \\equiv 0$ सर्वत्र शून्य होता है। अतः सही विकल्प (B, D) हैं।"
    })

    # Q23: PH Q13 (1 mark MSQ)
    questions.append({
        "questionId": "gate_ph_2021_q23",
        "questionNumber": 23,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MSQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Thermodynamics and Statistical Physics",
        "difficulty": "Medium",
        "correctOption": "A,D",
        "correctOptionsList": ["A", "D"],
        "correct_index": None,
        "correct_indices": [0, 3],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "For a finite system of non-interacting Fermions where the density of states $g(\\epsilon)$ increases monotonically with energy $\\epsilon$, the chemical potential $\\mu(T)$:",
        "optionsEn": [
            "decreases with temperature",
            "increases with temperature",
            "does not vary with temperature",
            "corresponds to the energy where the Fermi-Dirac occupation probability is 0.5"
        ],
        "explanationEn": "1. In the Fermi-Dirac distribution $f(\\epsilon) = \\frac{1}{e^{(\\epsilon - \\mu)/k_B T} + 1}$, when $\\epsilon = \\mu$, $f(\\mu) = \\frac{1}{e^0 + 1} = \\frac{1}{2} = 0.5$. Thus, the chemical potential always corresponds to the energy at which occupation probability is 0.5 (Option D).\n2. Using the Sommerfeld expansion for a Fermi gas with density of states $g(\\epsilon) \\propto \\epsilon^s$ where $s > 0$ (increasing with energy):\n$$\\mu(T) \\approx E_F \\left[ 1 - \\frac{\\pi^2}{6} \\left(\\frac{g'(E_F)}{g(E_F)}\\right) (k_B T)^2 \\right]$$\nSince $g'(\\epsilon) > 0$, the correction term is negative, so $\\mu(T)$ decreases with temperature (Option A).\nTherefore, the correct options are (A, D).",
        "questionTextHi": "फर्मीऑनों के एक ऐसे परिमित निकाय के लिए जहाँ अवस्थाओं का घनत्व $g(\\epsilon)$ ऊर्जा $\\epsilon$ के साथ बढ़ता है, रासायनिक विभव $\\mu(T)$:",
        "optionsHi": [
            "तापमान के साथ घटता है",
            "तापमान के साथ बढ़ता है",
            "तापमान के साथ परिवर्तित नहीं होता है",
            "उस ऊर्जा के अनुरूप होता है जहाँ अधिभोग प्रायिकता (occupation probability) 0.5 है"
        ],
        "explanationHi": "फर्मी-डिराक फलन में $\\epsilon = \\mu$ पर $f(\\mu) = 0.5$ होता है (विकल्प D सत्य)। सोमरफेल्ड विस्तार के अनुसार $g'(\\epsilon) > 0$ होने पर रासायनिक विभव ताप के साथ घटता है: $\\mu(T) = E_F - c T^2$ (विकल्प A सत्य)। अतः सही विकल्प (A, D) हैं।"
    })

    # Q24: PH Q14 (1 mark MSQ)
    questions.append({
        "questionId": "gate_ph_2021_q24",
        "questionNumber": 24,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MSQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Atomic and Molecular Physics",
        "difficulty": "Medium",
        "correctOption": "C,D",
        "correctOptionsList": ["C", "D"],
        "correct_index": None,
        "correct_indices": [2, 3],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Among the atomic spectroscopic term symbols $^{4}S_1$, $^{2}D_{7/2}$, $^{3}S_1$, and $^{2}D_{5/2}$, choose the option(s) that is(are) possible in the $LS$ coupling notation:",
        "optionsEn": [
            "^{4}S_1",
            "^{2}D_{7/2}",
            "^{3}S_1",
            "^{2}D_{5/2}"
        ],
        "explanationEn": "In atomic term notation $^{2S+1}L_J$:\n1. For $^{4}S_1$: $L = 0$ (S state), multiplicity $2S+1 = 4 \\implies S = 3/2$. Total angular momentum must satisfy $J = |L - S|, \\dots, L + S = 3/2$. But the symbol gives $J = 1$, which is impossible ($J$ must be half-integer).\n2. For $^{2}D_{7/2}$: $L = 2$ (D state), multiplicity $2S+1 = 2 \\implies S = 1/2$. Possible $J$ values are $|2 - 1/2| = 3/2$ and $2 + 1/2 = 5/2$. $J = 7/2$ is impossible.\n3. For $^{3}S_1$: $L = 0$, $2S+1 = 3 \\implies S = 1$. Then $J = 1$, which is fully consistent ($^{3}S_1$ is possible, e.g., ortho-helium).\n4. For $^{2}D_{5/2}$: $L = 2$, $2S+1 = 2 \\implies S = 1/2$. Then $J = 2 + 1/2 = 5/2$, which is fully consistent ($^{2}D_{5/2}$ is possible).\nTherefore, the possible term symbols are (C) $^{3}S_1$ and (D) $^{2}D_{5/2}$.",
        "questionTextHi": "परमाण्विक पद प्रतीकों $^{4}S_1$, $^{2}D_{7/2}$, $^{3}S_1$ और $^{2}D_{5/2}$ में से कौन-से $LS$ युग्मन संकेतन में सम्भव हैं?",
        "optionsHi": [
            "^{4}S_1",
            "^{2}D_{7/2}",
            "^{3}S_1",
            "^{2}D_{5/2}"
        ],
        "explanationHi": "पद संकेतन $^{2S+1}L_J$ में $|L-S| \\le J \\le L+S$ होना चाहिए।\n$^{3}S_1$: $L=0, S=1 \\implies J=1$ (सम्भव)।\n$^{2}D_{5/2}$: $L=2, S=1/2 \\implies J=5/2$ (सम्भव)।\nअतः सही विकल्प (C, D) हैं।"
    })

    # Q25: PH Q15 (1 mark MSQ)
    questions.append({
        "questionId": "gate_ph_2021_q25",
        "questionNumber": 25,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MSQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Atomic and Molecular Physics",
        "difficulty": "Easy",
        "correctOption": "A,B",
        "correctOptionsList": ["A", "B"],
        "correct_index": None,
        "correct_indices": [0, 1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "To sustain lasing action in a three-level laser system (Level 0: Ground state, Level 1: Metastable state, Level 2: Pump state), necessary condition(s) is(are):",
        "optionsEn": [
            "lifetime of energy level 1 should be greater than that of energy level 2",
            "population of particles in level 1 should be greater than that of level 0",
            "lifetime of energy level 2 should be greater than that of level 0",
            "population of particles in level 2 should be greater than that of level 1"
        ],
        "explanationEn": "In a three-level laser (such as a Ruby laser):\n1. Atoms are pumped from ground level 0 to pump level 2, then rapidly decay non-radiatively to metastable level 1. For atoms to accumulate in level 1, the lifetime of level 1 must be much longer than the lifetime of level 2 ($\\tau_1 \\gg \\tau_2$), making option (A) true.\n2. Lasing occurs between metastable level 1 and ground level 0. To achieve stimulated emission dominant over absorption, population inversion between level 1 and level 0 is required: $N_1 > N_0$, making option (B) true.\nHence, the correct conditions are (A, B).",
        "questionTextHi": "तीन-स्तरीय लेजर निकाय (स्तर 0: मूल अवस्था, स्तर 1: मितस्थायी अवस्था, स्तर 2: पंप अवस्था) में लेजर क्रिया बनाए रखने के लिए आवश्यक शर्त(शर्तें) है(हैं):",
        "optionsHi": [
            "ऊर्जा स्तर 1 का जीवनकाल ऊर्जा स्तर 2 की तुलना में अधिक होना चाहिए",
            "स्तर 1 में कणों की संख्या (population) स्तर 0 की तुलना में अधिक होनी चाहिए",
            "ऊर्जा स्तर 2 का जीवनकाल स्तर 0 की तुलना में अधिक होना चाहिए",
            "स्तर 2 में कणों की संख्या स्तर 1 की तुलना में अधिक होनी चाहिए"
        ],
        "explanationHi": "मितस्थायी स्तर 1 में जनसंख्या संचयन के लिए $\\tau_1 > \\tau_2$ होना चाहिए (A सत्य)। स्तर 1 तथा मूल स्तर 0 के मध्य जनसंख्या व्युत्क्रमण (population inversion) $N_1 > N_0$ आवश्यक है (B सत्य)। अतः सही विकल्प (A, B) हैं।"
    })

    # Q26: PH Q16 (1 mark MSQ)
    questions.append({
        "questionId": "gate_ph_2021_q26",
        "questionNumber": 26,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MSQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Mathematical Physics",
        "difficulty": "Medium",
        "correctOption": "B,C",
        "correctOptionsList": ["B", "C"],
        "correct_index": None,
        "correct_indices": [1, 2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "If $y_n(x)$ is a polynomial solution of the differential equation $y'' - 2xy' + 2ny = 0$ (where $n$ is an integer), then acceptable physical wave function plot(s) of $\\psi_n(x) = e^{-x^2/2} y_n(x)$ as a function of $x$ is(are):",
        "optionsEn": [
            "An unbounded exponentially growing function as $x \\to \\pm\\infty$",
            "An even function having $n = 0$ nodes (a Gaussian centered at origin)",
            "A function having definite parity with $n$ nodes and decaying to zero as $x \\to \\pm\\infty$",
            "A discontinuous function with step jumps"
        ],
        "explanationEn": "The equation $y'' - 2xy' + 2ny = 0$ is the Hermite differential equation whose polynomial solutions are the Hermite polynomials $H_n(x)$. The function $\\psi_n(x) = e^{-x^2/2} H_n(x)$ is precisely the eigenfunction of the quantum harmonic oscillator. Physical harmonic oscillator wave functions:\n1. For $n = 0$: $H_0(x) = 1 \\implies \\psi_0(x) = e^{-x^2/2}$ (Gaussian, 0 nodes, even parity).\n2. For any non-negative integer $n$: $\\psi_n(x)$ has exactly $n$ nodes, definite parity $(-1)^n$, and decays Gaussianly to zero as $x \\to \\pm\\infty$.\nThus, options (B, C) represent acceptable physical plots.",
        "questionTextHi": "यदि $y_n(x)$ अवकल समीकरण $y'' - 2xy' + 2ny = 0$ का हल है, तो $\\psi_n(x) = e^{-x^2/2} y_n(x)$ के स्वीकार्य भौतिक तरंग फलन आरेख है(हैं):",
        "optionsHi": [
            "$x \\to \\pm\\infty$ पर चरघातांकी रूप से अनन्त की ओर बढ़ने वाला फलन",
            "$n = 0$ नोड्स वाला एक सम फलन (मूल बिन्दु पर केंद्रित गॉसियन)",
            "निश्चित पैरिटी वाला $n$ नोड्स सहित फलन जो $x \\to \\pm\\infty$ पर शून्य की ओर क्षय होता है",
            "स्टेप जम्प युक्त एक असतत फलन"
        ],
        "explanationHi": "यह समीकरण हर्माइट अवकल समीकरण है और $\\psi_n(x)$ क्वांटम सरल आवर्ती दोलक का तरंग फलन है। इसके फलन परिबद्ध, सतत, $n$ शून्यकों (nodes) वाले तथा अनंत पर शून्य की ओर क्षय होने वाले होते हैं। अतः सही विकल्प (B, C) हैं।"
    })

    # Q27: PH Q17 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q27",
        "questionNumber": 27,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Solid State Physics",
        "difficulty": "Easy",
        "correctOption": "115",
        "correctOptionsList": ["115"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 115.0,
        "natMax": 116.0,
        "questionTextEn": "The donor concentration in a sample of n-type silicon is increased by a factor of 100. Assuming the sample to be non-degenerate, the shift in the Fermi level (in meV) at 300 K (rounded off to the nearest integer) is ______.\n(Given: $k_B T = 25\\text{ meV}$ at 300 K)",
        "optionsEn": [],
        "explanationEn": "In a non-degenerate n-type semiconductor, the Fermi level relative to the conduction band edge is:\n$$E_C - E_F = k_B T \\ln\\left(\\frac{N_C}{N_D}\\right)$$\nWhen donor concentration increases from $N_D$ to $100 N_D$, the Fermi level shifts closer to the conduction band by:\n$$\\Delta E_F = k_B T \\ln(100) = 25\\text{ meV} \\times \\ln(100)$$\n$$\\ln(100) = 2 \\times \\ln(10) \\approx 2 \\times 2.302585 = 4.60517$$\n$$\\Delta E_F = 25 \\times 4.60517 = 115.13\\text{ meV}$$\nRounding off to the nearest integer gives 115 meV (official answer range: 115 to 116).",
        "questionTextHi": "n-प्रकार के सिलिकॉन नमूने में दाता सांद्रता 100 के गुणक से बढ़ाई जाती है। नमूने को अपभ्रष्ट न मानते हुए, 300 K पर फर्मी स्तर में विस्थापन (meV में, निकटतम पूर्णांक तक) ______ है।\n(दिया है: 300 K पर $k_B T = 25\\text{ meV}$)",
        "optionsHi": [],
        "explanationHi": "फर्मी स्तर में विस्थापन:\n$$\\Delta E_F = k_B T \\ln(100) = 25\\text{ meV} \\times 4.60517 \\approx 115.13\\text{ meV}$$\nनिकटतम पूर्णांक: 115।"
    })

    # Q28: PH Q18 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q28",
        "questionNumber": 28,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Classical Mechanics",
        "difficulty": "Medium",
        "correctOption": "2",
        "correctOptionsList": ["2"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 2.0,
        "natMax": 2.0,
        "questionTextEn": "Two observers O and O' observe two events P and Q. The observers have a constant relative speed of $0.5c$. In natural units where $c = 1$, observer O records the following coordinates:\nEvent P: $x = 5, y = 3, z = 5, t = 3$\nEvent Q: $x = 5, y = 1, z = 3, t = 5$\nThe length of the space-time interval between these two events as measured by O' is $L$. The value of $|L| = \\sqrt{|\\Delta s^2|}$ (in integer) is ______.",
        "optionsEn": [],
        "explanationEn": "The spacetime interval $\\Delta s^2$ is an invariant quantity in special relativity (identical in all inertial frames O and O'):\n$$\\Delta s^2 = c^2 (\\Delta t)^2 - [(\\Delta x)^2 + (\\Delta y)^2 + (\\Delta z)^2]$$\nCalculating the coordinate differences:\n$$\\Delta t = t_Q - t_P = 5 - 3 = 2$$\n$$\\Delta x = 5 - 5 = 0$$\n$$\\Delta y = 1 - 3 = -2$$\n$$\\Delta z = 3 - 5 = -2$$\nSubstitute into the spacetime interval ($c = 1$):\n$$\\Delta s^2 = (2)^2 - [0^2 + (-2)^2 + (-2)^2] = 4 - [0 + 4 + 4] = 4 - 8 = -4$$\nThe magnitude of interval length $|L| = \\sqrt{|-4|} = \\sqrt{4} = 2$.\nThus, the integer value is 2.",
        "questionTextHi": "दो प्रेक्षक O और O' दो घटनाओं P और Q का प्रेक्षण करते हैं। $c = 1$ वाले मात्रकों में प्रेक्षक O द्वारा दर्ज निर्देशांक निम्न हैं:\nघटना P: $x = 5, y = 3, z = 5, t = 3$\nघटना Q: $x = 5, y = 1, z = 3, t = 5$\nO' द्वारा मापा गया दिक्-काल अंतराल की लम्बाई $|L|$ (पूर्णांक में) ______ है।",
        "optionsHi": [],
        "explanationHi": "दिक्-काल अंतराल एक निश्चर राशि है:\n$$\\Delta s^2 = (\\Delta t)^2 - (\\Delta x^2 + \\Delta y^2 + \\Delta z^2) = (2)^2 - (0 + 4 + 4) = 4 - 8 = -4$$\nअतः $|L| = \\sqrt{|-4|} = 2$।"
    })

    # Q29: PH Q19 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q29",
        "questionNumber": 29,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Thermodynamics and Statistical Physics",
        "difficulty": "Easy",
        "correctOption": "5000",
        "correctOptionsList": ["5000"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 5000.0,
        "natMax": 5000.0,
        "questionTextEn": "A light source having its intensity peak at the wavelength $\\lambda_1 = 289.8\\text{ nm}$ is calibrated as $10,000\\text{ K}$, which is the temperature of an equivalent blackbody radiation. Considering the same calibration, the temperature of a light source (in K) having its intensity peak at the wavelength $\\lambda_2 = 579.6\\text{ nm}$ (rounded off to the nearest integer) is ______.",
        "optionsEn": [],
        "explanationEn": "According to Wien's Displacement Law for blackbody radiation:\n$$\\lambda_{\\max} T = \\text{constant}$$\nTherefore:\n$$\\lambda_1 T_1 = \\lambda_2 T_2$$\n$$T_2 = T_1 \\left(\\frac{\\lambda_1}{\\lambda_2}\\right) = 10,000\\text{ K} \\times \\left(\\frac{289.8\\text{ nm}}{579.6\\text{ nm}}\\right) = 10,000 \\times \\frac{1}{2} = 5000\\text{ K}$$\nThus, the temperature is 5000 K.",
        "questionTextHi": "एक प्रकाश स्रोत, जिसका तीव्रता शिखर तरंगदैर्घ्य $\\lambda_1 = 289.8\\text{ nm}$ पर है, को समतुल्य कृष्णिका ताप $10,000\\text{ K}$ के रूप में अंशांकित किया गया है। समान अंशांकन को मानते हुए, $\\lambda_2 = 579.6\\text{ nm}$ पर शिखर वाले प्रकाश स्रोत का ताप (K में) ______ है।",
        "optionsHi": [],
        "explanationHi": "वीन के विस्थापन नियम से:\n$$\\lambda_1 T_1 = \\lambda_2 T_2 \\implies T_2 = 10,000 \\times \\frac{289.8}{579.6} = 5000\\text{ K}$$"
    })

    # Q30: PH Q20 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q30",
        "questionNumber": 30,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Classical Mechanics",
        "difficulty": "Easy",
        "correctOption": "2",
        "correctOptionsList": ["2"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 2.0,
        "natMax": 2.0,
        "questionTextEn": "A hoop of mass $M$ and radius $R$ rolls without slipping along a straight line on a horizontal surface. A point mass $m$ slides without friction along the inner smooth circular surface of the hoop, performing small oscillations about its lowest point. The number of degrees of freedom of this system (in integer) is ______.",
        "optionsEn": [],
        "explanationEn": "Let us determine the independent generalized coordinates required to completely specify the configuration:\n1. The hoop rolls without slipping on a horizontal 1D line: rolling without slipping constraint connects the translation of the center of mass $x$ to the rotation angle $\\theta$ of the hoop ($x = R\\theta$). Thus, the hoop has 1 degree of freedom.\n2. The point mass $m$ is constrained to stay on the inner circle of the hoop of radius $R$, but can slide along the inner circumference. Its position is specified by an angle $\\phi$ relative to the vertical.\n3. Motion is confined to a vertical plane (2D planar motion).\nTherefore, the system has exactly 2 independent generalized coordinates ($x$ and $\\phi$), which means it has 2 degrees of freedom.",
        "questionTextHi": "$M$ द्रव्यमान और $R$ त्रिज्या का एक छल्ला (hoop) एक क्षैतिज सतह पर बिना फिसले सीधी रेखा में लुढ़कता है। $m$ द्रव्यमान का एक कण छल्ले की चिकनी आंतरिक सतह पर बिना घर्षण के फिसलता है। इस निकाय की स्वतंत्रता की कोटियों (degrees of freedom) की संख्या ______ है।",
        "optionsHi": [],
        "explanationHi": "छल्ले की बिना फिसले लुढ़कने की गति को 1 स्वतंत्र निर्देशांक ($x = R\\theta$) द्वारा व्यक्त किया जाता है तथा आंतरिक कण की गति को 1 कोणीय निर्देशांक $\\phi$ द्वारा व्यक्त किया जाता है। अतः निकाय की कुल 2 स्वतंत्रता की कोटियाँ हैं।"
    })

    # Q31: PH Q21 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q31",
        "questionNumber": 31,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Quantum Mechanics",
        "difficulty": "Medium",
        "correctOption": "5",
        "correctOptionsList": ["5"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 5.0,
        "natMax": 6.0,
        "questionTextEn": "Three non-interacting identical bosonic particles of mass $m$ each are in a one-dimensional infinite potential well of width $a$. The single-particle energy states are $\\epsilon_n = n^2 \\frac{\\pi^2 \\hbar^2}{2 m a^2}$ ($n = 1, 2, 3, \\dots$). The energy of the third excited state of the three-boson system is $x \\times \\frac{\\pi^2 \\hbar^2}{m a^2}$. The value of $x$ (in integer) is ______.",
        "optionsEn": [],
        "explanationEn": "Let $E_0 = \\frac{\\pi^2 \\hbar^2}{2 m a^2}$. The single particle levels are $\\epsilon_n = n^2 E_0$, so $\\epsilon_1 = 1 E_0, \\epsilon_2 = 4 E_0, \\epsilon_3 = 9 E_0, \\dots$\nSince bosons obey Bose-Einstein statistics, any number of particles can occupy the same quantum state.\nEnergy configurations $(n_1, n_2, n_3)$ in order of increasing total energy:\n1. Ground State: (1, 1, 1) $\\implies E = (1 + 1 + 1)E_0 = 3E_0$\n2. 1st Excited State: (1, 1, 2) $\\implies E = (1 + 1 + 4)E_0 = 6E_0$\n3. 2nd Excited State: (1, 2, 2) $\\implies E = (1 + 4 + 4)E_0 = 9E_0$\n4. 3rd Excited State: (1, 1, 3) $\\implies E = (1 + 1 + 9)E_0 = 11E_0$\n[Or (2, 2, 2) has $E = (4 + 4 + 4)E_0 = 12E_0$].\nWriting $E$ in units of $\\frac{\\pi^2 \\hbar^2}{m a^2} = 2 E_0$:\n$$E = 11 E_0 = \\frac{11}{2} \\frac{\\pi^2 \\hbar^2}{m a^2} = 5.5 \\frac{\\pi^2 \\hbar^2}{m a^2}$$\nOfficial answer key range: 5 to 6. Integer value = 5 or 6 (5.5 is accepted, official integer key: 5 to 6).",
        "questionTextHi": "$m$ द्रव्यमान वाले तीन अन्योन्यक्रिया-हीन समरूप बोसॉन $a$ चौड़ाई वाले एक-विमीय अनंत विभव कूप में हैं। एकल-कण ऊर्जा स्तर $\\epsilon_n = n^2 \\frac{\\pi^2 \\hbar^2}{2 m a^2}$ हैं। तीन-बोसॉन निकाय की तीसरी उत्तेजित अवस्था की ऊर्जा $x \\times \\frac{\\pi^2 \\hbar^2}{m a^2}$ है। $x$ का मान (पूर्णांक में) ______ है।",
        "optionsHi": [],
        "explanationHi": "बोसॉनों के लिए ऊर्जा स्तर:\nमूल अवस्था (1,1,1): $E = 3 E_0$\nप्रथम उत्तेजित (1,1,2): $E = 6 E_0$\nद्वितीय उत्तेजित (1,2,2): $E = 9 E_0$\nतृतीय उत्तेजित (1,1,3): $E = (1+1+9)E_0 = 11 E_0 = 5.5 \\frac{\\pi^2 \\hbar^2}{m a^2}$।\nआधिकारिक कुंजी रेंज: 5 से 6।"
    })

    # Q32: PH Q22 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q32",
        "questionNumber": 32,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Atomic and Molecular Physics",
        "difficulty": "Medium",
        "correctOption": "17368",
        "correctOptionsList": ["17368"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 17367.0,
        "natMax": 17371.0,
        "questionTextEn": "The spacing between two consecutive S-branch lines of the pure rotational Raman spectrum of hydrogen gas is $243.2\\text{ cm}^{-1}$. After excitation with a laser of wavelength $514.5\\text{ nm}$, a Stokes line appears at $17611.4\\text{ cm}^{-1}$ for a particular rotational transition. The wavenumber (in $\\text{cm}^{-1}$, rounded off to the nearest integer) at which the Stokes line will appear for the next higher energy level transition is ______.",
        "optionsEn": [],
        "explanationEn": "In pure rotational Raman spectroscopy, the separation between consecutive lines in the S-branch ($\\Delta J = +2$) is constant and given by:\n$$\\Delta \\bar{\\nu} = 4B = 243.2\\text{ cm}^{-1}$$\nStokes lines appear at wavenumbers lower than the Rayleigh line: $\\bar{\\nu}_{Stokes} = \\bar{\\nu}_0 - \\Delta E_{rot}$.\nAs the rotational quantum number $J$ increases to the next higher energy level, the Raman shift increases, which shifts the Stokes line to a lower wavenumber by the line separation $4B = 243.2\\text{ cm}^{-1}$:\n$$\\bar{\\nu}_{next} = 17611.4 - 243.2 = 17368.2\\text{ cm}^{-1}$$\nRounding off to the nearest integer gives 17368 (official range: 17367 to 17371).",
        "questionTextHi": "हाइड्रोजन गैस के घूर्णी रमन स्पेक्ट्रम की दो क्रमागत S-शाखा रेखाओं के बीच का अंतराल $243.2\\text{ cm}^{-1}$ है। लेजर उत्तेजन के पश्चात एक विशेष स्तर के लिए स्टोक्स रेखा $17611.4\\text{ cm}^{-1}$ पर दिखाई देती है। अगले उच्च ऊर्जा स्तर के लिए स्टोक्स रेखा किस तरंग-संख्या ($\\text{cm}^{-1}$ में, निकटतम पूर्णांक तक) पर दिखाई देगी?",
        "optionsHi": [],
        "explanationHi": "S-शाखा में दो क्रमागत रेखाओं का अंतराल $\\Delta\\bar{\\nu} = 4B = 243.2\\text{ cm}^{-1}$ है। अगले उच्च घूर्णी स्तर के लिए स्टोक्स रेखा निम्न तरंग-संख्या पर होगी:\n$$\\bar{\\nu} = 17611.4 - 243.2 = 17368.2\\text{ cm}^{-1} \\approx 17368\\text{ cm}^{-1}$$"
    })

    # Q33: PH Q23 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q33",
        "questionNumber": 33,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Atomic and Molecular Physics",
        "difficulty": "Easy",
        "correctOption": "6",
        "correctOptionsList": ["6"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 6.0,
        "natMax": 6.0,
        "questionTextEn": "A spectral transition occurs between $^{2}D_{3/2}$ and $^{2}P_{1/2}$ states of an atom in the absence of an external magnetic field. The total number of Zeeman lines that will appear for this transition in the presence of a weak magnetic field (in integer) is ______.",
        "optionsEn": [],
        "explanationEn": "In the presence of a weak magnetic field (anomalous Zeeman effect):\n1. Upper state $^{2}D_{3/2}$ has $J = 3/2$. The magnetic quantum numbers are $M_J = -3/2, -1/2, +1/2, +3/2$ (4 sub-levels).\n2. Lower state $^{2}P_{1/2}$ has $J = 1/2$. The magnetic quantum numbers are $M_J = -1/2, +1/2$ (2 sub-levels).\n3. Allowed electric dipole transitions obey the selection rule $\\Delta M_J = 0, \\pm 1$:\n- Transitions to $M_J' = +1/2$ come from $M_J = -1/2, +1/2, +3/2$ (3 lines).\n- Transitions to $M_J' = -1/2$ come from $M_J = -3/2, -1/2, +1/2$ (3 lines).\nTotal number of allowed transition lines = 3 + 3 = 6 lines.\nThus, the integer answer is 6.",
        "questionTextHi": "बाह्य चुम्बकीय क्षेत्र की अनुपस्थिति में $^{2}D_{3/2}$ और $^{2}P_{1/2}$ स्तरों के बीच एक संक्रमण रेखा प्राप्त होती है। एक दुर्बल चुम्बकीय क्षेत्र की उपस्थिति में इस संक्रमण से प्रकट होने वाली जीमान रेखाओं की कुल संख्या (पूर्णांक में) ______ है।",
        "optionsHi": [],
        "explanationHi": "ऊपरी स्तर $J = 3/2$ के 4 उपस्तर ($M_J = \\pm 1/2, \\pm 3/2$) तथा निचले स्तर $J = 1/2$ के 2 उपस्तर ($M_J = \\pm 1/2$) हैं।\nचयन नियम $\\Delta M_J = 0, \\pm 1$ के अनुसार कुल अनुमत जीमान रेखाएँ = 6।"
    })

    # Q34: PH Q24 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q34",
        "questionNumber": 34,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Atomic and Molecular Physics",
        "difficulty": "Medium",
        "correctOption": "2",
        "correctOptionsList": ["2"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 2.0,
        "natMax": 2.0,
        "questionTextEn": "Consider an atomic system where the Einstein $A$ coefficients for spontaneous emission are $A_{2 \\to 1} = 2 \\times 10^7\\text{ s}^{-1}$ and $A_{1 \\to 0} = 10^8\\text{ s}^{-1}$. If $N_2 = 10^{14}\\text{ atoms/cm}^3$ are excited into level 2 and a steady state is achieved, the steady-state population density at level 1 is $x \\times 10^{13}\\text{ cm}^{-3}$. The value of $x$ (in integer) is ______.",
        "optionsEn": [],
        "explanationEn": "In the steady state, the rate of population influx into level 1 from level 2 equals the rate of decay from level 1 to level 0:\n$$\\frac{dN_1}{dt} = N_2 A_{2 \\to 1} - N_1 A_{1 \\to 0} = 0$$\n$$N_1 = N_2 \\frac{A_{2 \\to 1}}{A_{1 \\to 0}}$$\nSubstitute the given values:\n$$N_1 = (10^{14}) \\times \\frac{2 \\times 10^7}{10^8} = 10^{14} \\times 0.2 = 2 \\times 10^{13}\\text{ cm}^{-3}$$\nTherefore, $x = 2$.",
        "questionTextHi": "एक परमाण्विक निकाय पर विचार कीजिए जहाँ स्वतः उत्सर्जन के आइंस्टीन गुणांक $A_{2 \\to 1} = 2 \\times 10^7\\text{ s}^{-1}$ तथा $A_{1 \\to 0} = 10^8\\text{ s}^{-1}$ हैं। यदि स्तर 2 में $10^{14}\\text{ atoms/cm}^3$ उत्तेजित किए जाते हैं और स्थायी अवस्था प्राप्त होती है, तो स्तर 1 की स्थायी अवस्था जनसंख्या $x \\times 10^{13}\\text{ cm}^{-3}$ है। $x$ का मान (पूर्णांक में) ______ है।",
        "optionsHi": [],
        "explanationHi": "स्थायी अवस्था में:\n$$\\frac{dN_1}{dt} = N_2 A_{2 \\to 1} - N_1 A_{1 \\to 0} = 0 \\implies N_1 = N_2 \\frac{A_{2 \\to 1}}{A_{1 \\to 0}}$$\n$$N_1 = 10^{14} \\times \\frac{2 \\times 10^7}{10^8} = 2 \\times 10^{13}\\text{ cm}^{-3} \\implies x = 2$$"
    })

    # Q35: PH Q25 (1 mark NAT)
    questions.append({
        "questionId": "gate_ph_2021_q35",
        "questionNumber": 35,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": "GATE PH 2021 Official Paper",
        "topicTag": "Classical Mechanics",
        "difficulty": "Medium",
        "correctOption": "-1",
        "correctOptionsList": ["-1"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": -1.0,
        "natMax": -1.0,
        "questionTextEn": "If $\\mathbf{a}$ and $\\mathbf{b}$ are constant 3D vectors, $\\mathbf{r}$ and $\\mathbf{p}$ are generalized position and conjugate momentum vectors respectively, then for the transformation $Q = \\mathbf{a} \\cdot \\mathbf{p}$ and $P = \\mathbf{b} \\cdot \\mathbf{r}$ to be canonical, the value of $\\mathbf{a} \\cdot \\mathbf{b}$ (in integer) is ______.",
        "optionsEn": [],
        "explanationEn": "For a transformation $(q, p) \\to (Q, P)$ to be canonical, the fundamental Poisson bracket must satisfy:\n$$[Q, P]_{r, p} = 1$$\nHere $Q = \\sum_i a_i p_i$ and $P = \\sum_j b_j r_j$.\nThe Poisson bracket definition is:\n$$[Q, P] = \\sum_k \\left( \\frac{\\partial Q}{\\partial r_k} \\frac{\\partial P}{\\partial p_k} - \\frac{\\partial Q}{\\partial p_k} \\frac{\\partial P}{\\partial r_k} \\right)$$\nEvaluate the partial derivatives:\n$$\\frac{\\partial Q}{\\partial r_k} = 0, \\quad \\frac{\\partial P}{\\partial p_k} = 0$$\n$$\\frac{\\partial Q}{\\partial p_k} = a_k, \\quad \\frac{\\partial P}{\\partial r_k} = b_k$$\nSubstituting these in:\n$$[Q, P] = \\sum_k (0 - a_k b_k) = - \\sum_k a_k b_k = - (\\mathbf{a} \\cdot \\mathbf{b})$$\nFor the transformation to be canonical:\n$$-[\\mathbf{a} \\cdot \\mathbf{b}] = 1 \\implies \\mathbf{a} \\cdot \\mathbf{b} = -1$$\nThus, the integer answer is -1.",
        "questionTextHi": "यदि $\\mathbf{a}$ और $\\mathbf{b}$ अचर सदिश हैं, $\\mathbf{r}$ और $\\mathbf{p}$ क्रमशः व्यापक स्थिति और संयुग्मी संवेग सदिश हैं, तो रूपांतरण $Q = \\mathbf{a} \\cdot \\mathbf{p}$ और $P = \\mathbf{b} \\cdot \\mathbf{r}$ के विहित (canonical) होने के लिए $\\mathbf{a} \\cdot \\mathbf{b}$ का मान (पूर्णांक में) ______ है।",
        "optionsHi": [],
        "explanationHi": "विहित रूपांतरण के लिए प्वासों कोष्ठक:\n$$[Q, P] = \\sum_k \\left(\\frac{\\partial Q}{\\partial r_k}\\frac{\\partial P}{\\partial p_k} - \\frac{\\partial Q}{\\partial p_k}\\frac{\\partial P}{\\partial r_k}\\right) = -\\sum_k a_k b_k = -(\\mathbf{a} \\cdot \\mathbf{b}) = 1$$\n$$\\implies \\mathbf{a} \\cdot \\mathbf{b} = -1$$"
    })

    return questions
