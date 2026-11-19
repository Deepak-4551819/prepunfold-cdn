# -*- coding: utf-8 -*-
"""
General Aptitude Generator for GATE PH Mock Tests 01 to 12.
Generates 10 authentic, distinct, bilingual GA questions for each test:
- Q1 to Q5: 1 mark each (MCQ / NAT) -> 5 marks
- Q6 to Q10: 2 marks each (MCQ / NAT) -> 10 marks
Total: 15 marks.
"""

def get_ga_questions(test_num):
    tid = f"gate_ph_mock_{test_num:02d}"
    tag = f"GATE PH Full Mock {test_num:02d}"
    qs = []

    # Bank of data for tests 1 to 12
    # Q1: Verbal (1m MCQ)
    v1_data = {
        1: ("METICULOUS", "THOROUGH", ["CARELESS", "SLOPPY", "THOROUGH", "HASTY"], 2,
            "अति सावधान / सूक्ष्म", "पूर्ण व सावधान", "सूक्ष्म (THOROUGH)", "लापरवाह"),
        2: ("TACITURN", "RESERVED", ["LOQUACIOUS", "RESERVED", "ELOQUENT", "VOLUBLE"], 1,
            "मितभाषी / अल्पभाषी", "कम बोलने वाला", "मितभाषी (RESERVED)", "वाचाल"),
        3: ("EPHEMERAL", "FLEETING", ["FLEETING", "PERMANENT", "SUBSTANTIAL", "IMMORTAL"], 0,
            "क्षणिक / अल्पकालिक", "अल्पकालिक", "अल्पकालिक (FLEETING)", "स्थायी"),
        4: ("PRAGMATIC", "PRACTICAL", ["THEORETICAL", "PRACTICAL", "IDEALISTIC", "VAGUE"], 1,
            "व्यावहारिक", "व्यावहारिक", "व्यावहारिक (PRACTICAL)", "सैद्धांतिक"),
        5: ("AMBIGUOUS", "EQUIVOCAL", ["CLEAR", "LUCID", "EQUIVOCAL", "DEFINITE"], 2,
            "अस्पष्ट / संदिग्ध", "संदिग्ध", "संदिग्ध (EQUIVOCAL)", "स्पष्ट"),
        6: ("RESILIENT", "FLEXIBLE", ["RIGID", "BRITTLE", "FRAGILE", "FLEXIBLE"], 3,
            "लचीला / शीघ्र संभलने वाला", "लचीला", "लचीला (FLEXIBLE)", "कठोर"),
        7: ("UBIQUITOUS", "OMNIPRESENT", ["OMNIPRESENT", "RARE", "SCARCE", "ISOLATED"], 0,
            "सर्वव्यापी", "सर्वव्यापी", "सर्वव्यापी (OMNIPRESENT)", "दुर्लभ"),
        8: ("METICULOUS", "THOROUGH", ["CARELESS", "SLOPPY", "THOROUGH", "HASTY"], 2,
            "अति सावधान / सूक्ष्म", "पूर्ण व सावधान", "सूक्ष्म (THOROUGH)", "लापरवाह"),
        9: ("CANDID", "FRANK", ["FRANK", "SECRETIVE", "DECEPTIVE", "EVASIVE"], 0,
            "स्पष्टवादी / निष्कपट", "स्पष्टवादी", "स्पष्टवादी (FRANK)", "कपटपूर्ण"),
        10: ("LACONIC", "TERSE", ["VERBOSE", "TERSE", "WORDY", "DIFFUSE"], 1,
            "संक्षिप्त / मितभाषी", "संक्षिप्त", "संक्षिप्त (TERSE)", "वाचाल"),
        11: ("BENEVOLENT", "KIND", ["MALEVOLENT", "HOSTILE", "KIND", "CRUEL"], 2,
            "परोपकारी / दयालु", "दयालु", "दयालु (KIND)", "द्वेषपूर्ण"),
        12: ("APATHY", "INDIFFERENCE", ["ENTHUSIASM", "ZEAL", "PASSION", "INDIFFERENCE"], 3,
            "उदासीनता", "उदासीनता", "उदासीनता (INDIFFERENCE)", "उत्साह")
    }

    w, syn, opts, c_idx, w_hi, syn_hi, expl_en, ant_en = v1_data[test_num]
    qs.append({
        "questionId": f"{tid}_q001",
        "questionNumber": 1,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Verbal Ability",
        "difficulty": "Easy",
        "correctOption": chr(65 + c_idx),
        "correctOptionsList": [chr(65 + c_idx)],
        "correct_index": c_idx,
        "correct_indices": [c_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": f"Select the word that is most nearly SIMILAR in meaning to the given word:\n{w}",
        "optionsEn": opts,
        "explanationEn": f"'{w}' means lasting for a very short time or being {syn.lower()}. The most appropriate synonym is '{syn}'.",
        "questionTextHi": f"दिए गए शब्द के सबसे निकटतम समानार्थक (SIMILAR) शब्द का चयन करें:\n{w}",
        "optionsHi": opts,
        "explanationHi": f"'{w}' का अर्थ '{w_hi}' होता है। इसका सही समानार्थक '{syn}' है।"
    })

    # Q2: Grammar (1m MCQ)
    v2_data = {
        1: ("The scientist, along with his assistants, ______ attending the conference.", ["is", "are", "were", "have been"], 0, "is", "'along with' takes singular verb agreeing with the main subject 'scientist'."),
        2: ("Either the professor or the students ______ responsible for the experimental error.", ["are", "is", "was", "has been"], 0, "are", "When subjects are joined by 'or', the verb agrees with the nearer subject ('students')."),
        3: ("Neither of the two candidates ______ suitable for the research position.", ["is", "are", "were", "have been"], 0, "is", "Neither takes a singular verb 'is'."),
        4: ("The committee ______ divided in their opinions regarding the budget.", ["was", "were", "is", "has been"], 1, "were", "When members act individually, plural verb 'were' is used."),
        5: ("If he ______ harder, he would have cleared the fellowship exam.", ["studied", "had studied", "has studied", "was studying"], 1, "had studied", "Third conditional: If + had + V3, would have + V3."),
        6: ("Hardly had the professor entered the hall ______ the students stood up.", ["when", "than", "then", "while"], 0, "when", "'Hardly... when' is the correct correlative conjunction."),
        7: ("One should always adhere ______ one's principles under pressure.", ["to", "with", "on", "at"], 0, "to", "The verb 'adhere' takes the preposition 'to'."),
        8: ("Each of the experimental trials ______ meticulously documented.", ["was", "were", "have been", "are"], 0, "was", "'Each of' takes a singular verb 'was'."),
        9: ("No sooner did the bell ring ______ the examination commenced.", ["than", "when", "then", "since"], 0, "than", "'No sooner did... than' is the correct correlative conjunction."),
        10: ("She is proficient ______ both theoretical and experimental physics.", ["in", "at", "with", "on"], 0, "in", "'Proficient in' a subject or field is standard English usage."),
        11: ("The data collected during the tests ______ consistent with the model.", ["is", "are", "has been", "was being"], 1, "are", "In formal scientific English, 'data' is treated as plural ('are')."),
        12: ("Had they informed us earlier, we ______ the necessary arrangements.", ["would make", "would have made", "will make", "have made"], 1, "would have made", "Inverted conditional requires 'would have made'.")
    }
    sent, g_opts, g_idx, g_ans, g_expl = v2_data[test_num]
    qs.append({
        "questionId": f"{tid}_q002",
        "questionNumber": 2,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Verbal Ability",
        "difficulty": "Easy",
        "correctOption": chr(65 + g_idx),
        "correctOptionsList": [chr(65 + g_idx)],
        "correct_index": g_idx,
        "correct_indices": [g_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": f"Choose the grammatically correct option to fill in the blank:\n{sent}",
        "optionsEn": g_opts,
        "explanationEn": f"{g_expl} Correct option is '{g_ans}'.",
        "questionTextHi": f"रिक्त स्थान की पूर्ति के लिए व्याकरण की दृष्टि से सही विकल्प चुनें:\n{sent}",
        "optionsHi": g_opts,
        "explanationHi": f"सही विकल्प '{g_ans}' है। {g_expl}"
    })

    # Q3: Quantitative (1m MCQ)
    q3_data = {
        1: ("If $x : y = 2 : 3$ and $y : z = 4 : 5$, then $x : z$ is:", ["$8 : 15$", "$2 : 5$", "$3 : 5$", "$6 : 15$"], 0, "x/z = (x/y)(y/z) = (2/3)(4/5) = 8/15."),
        2: ("A number when increased by $25\\%$ becomes 150. The original number is:", ["120", "125", "110", "130"], 0, "1.25 x = 150 -> x = 150 / 1.25 = 120."),
        3: ("If $A : B = 3 : 4$ and $B : C = 8 : 9$, then the ratio $A : C$ is:", ["$2 : 3$", "$1 : 2$", "$3 : 2$", "$4 : 3$"], 0, "A/C = (3/4)*(8/9) = 2/3."),
        4: ("If the radius of a circle is increased by $20\\%$, the percentage increase in its area is:", ["$20\\%$", "$40\\%$", "$44\\%$", "$48\\%$"], 2, "1.2^2 = 1.44 -> 44% increase."),
        5: ("The sum of the infinite geometric series $1 + \\frac{1}{3} + \\frac{1}{9} + \\dots$ is:", ["$3/2$", "$4/3$", "$2$", "$5/3$"], 0, "S = 1 / (1 - 1/3) = 3/2."),
        6: ("If $x + \\frac{1}{x} = 3$, the value of $x^2 + \\frac{1}{x^2}$ is:", ["7", "9", "11", "6"], 0, "(x + 1/x)^2 - 2 = 9 - 2 = 7."),
        7: ("The average of 5 consecutive odd numbers is 25. The largest number is:", ["27", "29", "31", "25"], 1, "Middle is 25. Numbers are 21, 23, 25, 27, 29. Largest is 29."),
        8: ("Two numbers are in the ratio $4 : 5$ and their LCM is 120. The smaller number is:", ["24", "30", "20", "16"], 0, "4x * 5x / x = 20x = 120 -> x = 6. Smaller is 4*6 = 24."),
        9: ("A train travels $300\\text{ km}$ at a uniform speed. If the speed had been $10\\text{ km/h}$ more, it would have taken 1 hour less. Its original speed in $\\text{km/h}$ is:", ["50", "60", "40", "45"], 0, "300/50 = 6h, 300/60 = 5h. Original is 50 km/h."),
        10: ("The difference between simple interest and compound interest on Rs. 1000 for 2 years at $10\\%$ per annum is:", ["Rs. 10", "Rs. 20", "Rs. 5", "Rs. 15"], 0, "P(r/100)^2 = 1000 * 0.01 = 10."),
        11: ("If $\\log_{10} 2 = 0.3010$, the number of digits in $2^{50}$ is:", ["15", "16", "17", "18"], 1, "50 * 0.3010 = 15.05 -> digits = 15 + 1 = 16."),
        12: ("A car covers first half distance at $40\\text{ km/h}$ and second half at $60\\text{ km/h}$. The average speed is:", ["$48\\text{ km/h}$", "$50\\text{ km/h}$", "$52\\text{ km/h}$", "$45\\text{ km/h}$"], 0, "2*40*60 / (40+60) = 48 km/h.")
    }
    q_txt, q_opts, q_idx, q_expl = q3_data[test_num]
    qs.append({
        "questionId": f"{tid}_q003",
        "questionNumber": 3,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Quantitative Aptitude",
        "difficulty": "Easy",
        "correctOption": chr(65 + q_idx),
        "correctOptionsList": [chr(65 + q_idx)],
        "correct_index": q_idx,
        "correct_indices": [q_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": q_txt,
        "optionsEn": q_opts,
        "explanationEn": q_expl,
        "questionTextHi": q_txt,
        "optionsHi": q_opts,
        "explanationHi": q_expl
    })

    # Q4: Reasoning / Spatial (1m MCQ)
    r_data = {
        1: ("Find the missing term in the sequence: $1, 4, 9, 16, 25, ?$", ["36", "49", "30", "32"], 0, "Squares of natural numbers: 6^2 = 36."),
        2: ("If 'SOUTH' is called 'NORTH', 'WEST' is called 'EAST', then what is 'NORTH-EAST' called?", ["SOUTH-WEST", "NORTH-WEST", "SOUTH-EAST", "EAST-NORTH"], 0, "Direct inversion of direction gives SOUTH-WEST."),
        3: ("In a certain code, 'PHYSICS' is written as 'QIZTJDT'. In the same code, 'SCIENCE' will be written as:", ["TDJFOFD", "TDJFMDF", "TCJFOFD", "TDKFOFD"], 0, "Each letter is shifted by +1: S->T, C->D, I->J, E->F, N->O, C->D, E->F -> TDJFOFD."),
        4: ("Pointing to a photograph, a woman says: 'His mother is the only daughter of my mother.' How is the woman related to the boy in the photograph?", ["Aunt", "Mother", "Sister", "Grandmother"], 1, "Only daughter of woman's mother is the woman herself. So she is the mother."),
        5: ("Find the next number in the series: $2, 6, 12, 20, 30, \\dots$", ["40", "42", "44", "46"], 1, "Differences are +4, +6, +8, +10, +12 -> 30 + 12 = 42."),
        6: ("A person walks $10\\text{ m}$ North, turns right and walks $5\\text{ m}$, then turns right and walks $10\\text{ m}$. How far is he from his starting point?", ["$5\\text{ m}$", "$10\\text{ m}$", "$15\\text{ m}$", "$0\\text{ m}$"], 0, "Forms a rectangle: distance = 5 m East."),
        7: ("Which number replaces the question mark in the sequence: $3, 8, 15, 24, 35, ?$ ", ["46", "48", "50", "52"], 1, "$n^2 - 1$: 2^2-1=3, 3^2-1=8, ..., 7^2-1 = 48."),
        8: ("In a dice, the numbers 1 to 6 are on the faces. If 1 is opposite to 6, 2 opposite to 5, and 3 opposite to 4, what is the sum of numbers on the faces adjacent to 1?", ["14", "15", "16", "17"], 0, "Opposite is 6. Adjacent are 2, 3, 4, 5. Sum = 2+3+4+5 = 14."),
        9: ("Statements: All photons are bosons. Some bosons are mesons. Conclusion: Some photons are mesons.", ["Definitely True", "Definitely False", "Cannot be determined", "Both true and false"], 2, "A is B, some B is C -> relation between A and C cannot be determined."),
        10: ("Find the odd one out from the following pairs:", ["$(2, 8)$", "$(3, 27)$", "$(4, 64)$", "$(5, 100)$"], 3, "All are $(n, n^3)$ except $(5, 100)$, which should be 125."),
        11: ("If Tuesday falls on 1st January of a non-leap year, what day will it be on 31st December of the same year?", ["Monday", "Tuesday", "Wednesday", "Thursday"], 1, "In a normal year (365 days = 52 weeks + 1 day), Jan 1 and Dec 31 fall on the exact same day: Tuesday."),
        12: ("In a row of 30 students, Amit is 10th from the left. What is his position from the right?", ["21st", "20th", "19th", "22nd"], 0, "30 - 10 + 1 = 21st.")
    }
    r_txt, r_opts, r_idx, r_expl = r_data[test_num]
    qs.append({
        "questionId": f"{tid}_q004",
        "questionNumber": 4,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Logical Reasoning",
        "difficulty": "Easy",
        "correctOption": chr(65 + r_idx),
        "correctOptionsList": [chr(65 + r_idx)],
        "correct_index": r_idx,
        "correct_indices": [r_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": r_txt,
        "optionsEn": r_opts,
        "explanationEn": r_expl,
        "questionTextHi": r_txt,
        "optionsHi": r_opts,
        "explanationHi": r_expl
    })

    # Q5: Quantitative (1m NAT)
    nat1_data = {
        1: ("The average of 4 numbers is 20. If each number is multiplied by 3, the new average is ______ (answer in integer).", 60.0, 60.0, "60", "Multiplying each data point by a constant multiplies the mean by that constant: 20 * 3 = 60."),
        2: ("If $5^x = 125$, the value of $x$ is ______ (answer in integer).", 3.0, 3.0, "3", "125 = 5^3 -> x = 3."),
        3: ("A shopkeeper marks an article $40\\%$ above the cost price and allows a discount of $20\\%$. The profit percentage is ______ (answer in integer).", 12.0, 12.0, "12", "CP=100 -> MP=140 -> SP=140*0.8=112 -> Profit = 12%."),
        4: ("The remainder when $2^{31}$ is divided by 7 is ______ (answer in integer).", 2.0, 2.0, "2", "2^3 = 8 = 1 mod 7. 2^31 = (2^3)^10 * 2 = 1^10 * 2 = 2 mod 7."),
        5: ("The sum of the roots of the quadratic equation $3x^2 - 15x + 7 = 0$ is ______ (answer in integer).", 5.0, 5.0, "5", "Sum of roots = -b/a = -(-15)/3 = 5."),
        6: ("If the area of a square is $144\\text{ cm}^2$, its perimeter in cm is ______ (answer in integer).", 48.0, 48.0, "48", "Side = 12 cm -> Perimeter = 4*12 = 48 cm."),
        7: ("Pipe A can fill a tank in 6 hours and Pipe B can empty it in 8 hours. Working together, the time in hours to fill the tank is ______ (answer in integer).", 24.0, 24.0, "24", "1/6 - 1/8 = 1/24 -> 24 hours."),
        8: ("The number of positive integral divisors of 360 is ______ (answer in integer).", 24.0, 24.0, "24", "360 = 2^3 * 3^2 * 5^1 -> (3+1)(2+1)(1+1) = 4*3*2 = 24."),
        9: ("The arithmetic mean of numbers 10, 15, 20, 25, $x$ is 20. The value of $x$ is ______ (answer in integer).", 30.0, 30.0, "30", "10+15+20+25+x = 5*20 = 100 -> 70+x=100 -> x=30."),
        10: ("A man walks at $4\\text{ km/h}$ and reaches his office 5 minutes late. If he walks at $5\\text{ km/h}$, he reaches on time. The distance to his office in km is ______ (answer in integer).", 1.66, 1.68, "1.67", "d/4 - d/5 = 5/60 -> d/20 = 1/12 -> d = 20/12 = 1.67 km."),
        11: ("The value of $\\frac{1}{1 \\cdot 2} + \\frac{1}{2 \\cdot 3} + \\dots + \\frac{1}{99 \\cdot 100}$ in two decimal places is ______.", 0.98, 1.00, "0.99", "Telescoping sum = 1 - 1/100 = 0.99."),
        12: ("In a class of 50 students, 30 play football, 25 play cricket, and 10 play both. The number of students playing neither sport is ______ (answer in integer).", 5.0, 5.0, "5", "n(A U B) = 30 + 25 - 10 = 45 -> neither = 50 - 45 = 5.")
    }
    nat_txt, n_min, n_max, n_ans, n_expl = nat1_data[test_num]
    qs.append({
        "questionId": f"{tid}_q005",
        "questionNumber": 5,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": tag,
        "topicTag": "Quantitative Aptitude",
        "difficulty": "Easy",
        "correctOption": n_ans,
        "correctOptionsList": [n_ans],
        "correct_index": None,
        "correct_indices": [],
        "natMin": n_min,
        "natMax": n_max,
        "questionTextEn": nat_txt,
        "optionsEn": [],
        "explanationEn": n_expl,
        "questionTextHi": nat_txt,
        "optionsHi": [],
        "explanationHi": n_expl
    })

    # Q6: Reading Comprehension / Deduction (2m MCQ)
    rc_data = {
        1: ("Read the following statement:\n'Progress in experimental physics relies crucially on isolating variables, minimizing systematic errors through calibration, and reducing random noise via statistical averaging.'\nWhat is the primary role of calibration according to the text?",
            ["Minimizing systematic errors", "Eliminating random thermal fluctuations completely", "Replacing theoretical derivations", "Increasing measurement speed"],
            0, "Calibration directly addresses systematic errors by referencing measurements against standards."),
        2: ("Consider the following excerpt:\n'A scientific hypothesis must be empirically falsifiable. A proposition that cannot be subjected to a potential experimental refutation lies outside the domain of empirical science.'\nAccording to the passage, an empirical scientific hypothesis must:",
            ["Be capable of being tested and potentially refuted by experiment", "Be permanently proven beyond any future revision", "Depend entirely on purely philosophical reasoning", "Avoid all mathematical modeling"],
            0, "The passage explicitly defines scientific validity through empirical falsifiability."),
        3: ("Read the following statement:\n'Scientific paradigms shift not merely when old theories are disproven, but when anomalies accumulate to the extent that a new, more comprehensive framework emerges that explains both the old successes and the novel failures.'\nWhich of the following is the most logically valid inference?",
            ["A paradigm shift occurs only through gradual minor modifications.", "Anomalies alone are sufficient to replace an established paradigm without a new framework.", "A new paradigm must account for both previous experimental successes and newly discovered anomalies.", "Old theories are completely abandoned without retaining any explanatory power."],
            2, "Statement directly asserts the new framework must explain both old successes and novel failures."),
        4: ("Consider the following passage:\n'The transition to renewable energy sources is constrained not primarily by theoretical thermodynamic limits of energy conversion, but by grid storage density, material supply chain bottlenecks, and high capital depreciation rates.'\nBased on the passage, the primary constraint is:",
            ["Thermodynamic inefficiency of solar cells", "Technological and material infrastructure bottlenecks", "Lack of solar radiation", "Government subsidies"],
            1, "Passage emphasizes grid storage, materials, and capital, i.e., infrastructure bottlenecks."),
        5: ("Passage:\n'In quantum cryptography, eavesdropping cannot be concealed because the fundamental act of measurement unavoidably disturbs quantum state superpositions, thereby introducing detectable errors in the transmission key.'\nThis security feature originates fundamentally from:",
            ["Advanced mathematical encryption algorithms", "The physical postulate of quantum measurement collapse", "High transmission power of optical fibers", "Complex parity check bits"],
            1, "Originates from physical disturbance of quantum states during measurement."),
        6: ("Passage:\n'A mathematical model of a physical process is necessarily an abstraction that isolates dominant mechanisms while suppressing secondary fluctuations. Consequently, the predictive accuracy of a model is bounded by the validity domain of its underlying assumptions.'\nWhich statement follows logically?",
            ["A model is invalid if it ignores any physical fluctuation.", "Predictions of a model cannot be trusted outside its foundational assumption domain.", "Mathematical abstractions are unnecessary for engineering predictions.", "Secondary fluctuations always dominate over primary mechanisms."],
            1, "Directly follows from the bounded validity domain statement."),
        7: ("Passage:\n'The emergence of high-temperature superconductivity in cuprates challenges standard electron-phonon BCS theory, suggesting that strong electronic correlation and antiferromagnetic spin fluctuations play a decisive role in Cooper pair formation.'\nAccording to the passage:",
            ["Cuprates are perfectly explained by traditional electron-phonon coupling.", "Spin fluctuations and electronic correlations are crucial in cuprate superconductivity.", "High-Tc superconductors do not form Cooper pairs.", "Antiferromagnetism completely destroys superconductivity in cuprates."],
            1, "Passage highlights decisive role of spin fluctuations and strong electronic correlation."),
        8: ("Passage:\n'Peer review in scientific publishing does not guarantee absolute empirical truth; rather, it functions as an essential quality control filter to eliminate methodological flaws, unsupported inferences, and plagiarism before dissemination.'\nWhat is the primary function of peer review?",
            ["To certify absolute scientific truth", "To act as a rigorous quality assurance and methodological filter", "To prevent publication of controversial ideas", "To replace experimental replication"],
            1, "Functions as quality control filter against methodological flaws and errors."),
        9: ("Passage:\n'The conservation laws in physics are not arbitrary empirical postulates; by Noether's theorem, every continuous global symmetry of the action corresponds directly to a conserved physical current.'\nWhat directly underlies the conservation of linear momentum?",
            ["Time translation invariance", "Spatial translation invariance", "Rotational invariance", "Gauge invariance"],
            1, "By Noether's theorem, spatial translation invariance gives linear momentum conservation."),
        10: ("Passage:\n'Supercomputing simulations do not supersede laboratory experiments; rather, they provide computational experiments that explore parameter regimes inaccessible to current physical probes, guiding experimental design.'\nSimulations are primarily valuable because they:",
            ["Render laboratory experiments obsolete", "Probe extreme or inaccessible regimes and guide physical experiments", "Guarantee zero experimental error", "Cost nothing compared to physical devices"],
            1, "Explore parameter regimes inaccessible to current physical probes."),
        11: ("Passage:\n'Entropy in statistical mechanics measures the volume of accessible phase space corresponding to a given macroscopic state. Therefore, spontaneous evolution toward higher entropy reflects statistical probability rather than a dynamical force.'\nSpontaneous entropy increase is driven by:",
            ["A fundamental dynamical repelling force", "Statistical probability of occupying vastly larger phase space volumes", "Conservation of energy alone", "Decrease in absolute temperature"],
            1, "Driven by statistical probability of vastly larger phase space volumes."),
        12: ("Passage:\n'In scientific inquiry, correlation between two observables does not establish causation, because unobserved confounding variables or reverse causality may account entirely for the observed statistical association.'\nTo establish causality, one must:",
            ["Demonstrate perfect statistical correlation only", "Control for confounding variables and establish directional mechanism", "Increase sample size without changing methodology", "Rely entirely on observational surveys"],
            1, "Must control confounding variables and identify directional mechanisms.")
    }
    rc_q, rc_opts, rc_idx, rc_expl = rc_data[test_num]
    qs.append({
        "questionId": f"{tid}_q006",
        "questionNumber": 6,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.67,
        "pyqTag": tag,
        "topicTag": "Reading Comprehension",
        "difficulty": "Medium",
        "correctOption": chr(65 + rc_idx),
        "correctOptionsList": [chr(65 + rc_idx)],
        "correct_index": rc_idx,
        "correct_indices": [rc_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": rc_q,
        "optionsEn": rc_opts,
        "explanationEn": rc_expl,
        "questionTextHi": rc_q,
        "optionsHi": rc_opts,
        "explanationHi": rc_expl
    })

    # Q7: Combinatorics / Probability (2m MCQ)
    p_data = {
        1: ("A fair coin is tossed 3 times. The probability of getting exactly 2 heads is:",
            ["$3/8$", "$1/2$", "$1/4$", "$1/8$"], 0, "Outcomes = 2^3 = 8. Ways to choose 2 heads = 3C2 = 3. P = 3/8."),
        2: ("The probability of drawing a red ace from a standard deck of 52 cards is:",
            ["$1/26$", "$1/13$", "$1/52$", "$2/13$"], 0, "There are 2 red aces (hearts, diamonds). P = 2/52 = 1/26."),
        3: ("Two fair six-sided dice are thrown simultaneously. The probability that the sum of the numbers appearing on top is at least 10 is:",
            ["$1/6$", "$5/36$", "$1/12$", "$1/4$"], 0, "Pairs with sum >= 10: (4,6), (5,5), (5,6), (6,4), (6,5), (6,6) = 6 outcomes. P = 6/36 = 1/6."),
        4: ("A bag contains 5 red balls and 4 blue balls. If two balls are drawn at random without replacement, the probability that both balls are of the same color is:",
            ["$4/9$", "$2/9$", "$1/2$", "$5/18$"], 0, "P(both red) = (5/9)*(4/8) = 20/72. P(both blue) = (4/9)*(3/8) = 12/72. Total = 32/72 = 4/9."),
        5: ("The number of ways to seat 5 men and 4 women around a circular table such that no two women sit together is:",
            ["$2880$", "$1440$", "$720$", "$576$"], 0, "Seat 5 men: (5-1)! = 24 ways. 5 gaps created: 5P4 = 120 ways. Total = 24 * 120 = 2880."),
        6: ("A box contains 3 defective and 7 non-defective bulbs. Two bulbs are drawn at random. What is the probability that at least one bulb is defective?",
            ["$8/15$", "$7/15$", "$1/3$", "$2/3$"], 0, "P(none defective) = 7C2 / 10C2 = 21/45 = 7/15. P(at least one) = 1 - 7/15 = 8/15."),
        7: ("Three fair coins are tossed simultaneously. The probability of getting at least two heads given that at least one head appeared is:",
            ["$4/7$", "$1/2$", "$3/7$", "$5/7$"], 0, "Outcomes with at least one head = 7. Outcomes with >= 2 heads: HHT, HTH, THH, HHH = 4. P = 4/7."),
        8: ("In how many distinct ways can the letters of the word 'PHYSICS' be arranged?",
            ["$2520$", "$5040$", "$1260$", "$720$"], 0, "7 letters: P, H, Y, I, C and two S's. Arrangements = 7! / 2! = 5040 / 2 = 2520."),
        9: ("A committee of 4 members is to be selected from 6 men and 5 women. The probability that the committee consists of 2 men and 2 women is:",
            ["$15/33$", "$10/33$", "$20/33$", "$5/11$"], 0, "Ways = (6C2 * 5C2) / 11C4 = (15 * 10) / 330 = 150 / 330 = 15/33."),
        10: ("A card is drawn from a well-shuffled pack of 52 cards. The probability that it is either a king or a spade is:",
            ["$4/13$", "$17/52$", "$16/52$", "$1/4$"], 0, "4 kings + 13 spades - 1 (king of spades) = 16 cards. P = 16/52 = 4/13."),
        11: ("Two independent events $A$ and $B$ have probabilities $P(A) = 0.4$ and $P(B) = 0.5$. The probability $P(A \\cup B)$ is:",
            ["$0.7$", "$0.9$", "$0.2$", "$0.8$"], 0, "P(A U B) = P(A) + P(B) - P(A)P(B) = 0.4 + 0.5 - 0.2 = 0.7."),
        12: ("A problem in physics is given to three students whose chances of solving it are $1/2, 1/3, 1/4$. What is the probability that the problem is solved?",
            ["$3/4$", "$1/4$", "$2/3$", "$5/6$"], 0, "P(not solved) = (1 - 1/2)(1 - 1/3)(1 - 1/4) = (1/2)(2/3)(3/4) = 1/4. P(solved) = 1 - 1/4 = 3/4.")
    }
    p_q, p_opts, p_idx, p_expl = p_data[test_num]
    qs.append({
        "questionId": f"{tid}_q007",
        "questionNumber": 7,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.67,
        "pyqTag": tag,
        "topicTag": "Probability & Combinatorics",
        "difficulty": "Medium",
        "correctOption": chr(65 + p_idx),
        "correctOptionsList": [chr(65 + p_idx)],
        "correct_index": p_idx,
        "correct_indices": [p_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": p_q,
        "optionsEn": p_opts,
        "explanationEn": p_expl,
        "questionTextHi": p_q,
        "optionsHi": p_opts,
        "explanationHi": p_expl
    })

    # Q8: Analytical / Logic (2m MCQ)
    l_data = {
        1: ("If all physicists are mathematicians and some mathematicians are musicians, which conclusion is definite?",
            ["Some musicians may be physicists", "All musicians are physicists", "No physicist is a musician", "All mathematicians are physicists"], 0, "Subset logic allows overlapping possibility."),
        2: ("In a group of 5 people, A is older than B but younger than C. D is older than C. Who is the oldest?",
            ["D", "C", "A", "B"], 0, "D > C > A > B -> D is oldest."),
        3: ("Five friends P, Q, R, S, T sit in a row facing North. S is between T and Q. Q is to the immediate left of R. P is to the immediate left of T. Who is sitting in the middle?",
            ["S", "Q", "T", "R"], 0, "Order from left: P, T, S, Q, R. Middle is S."),
        4: ("If 'A + B' means A is the father of B; 'A - B' means A is the sister of B; 'A * B' means A is the brother of B. Which expression means P is the nephew of Q?",
            ["$Q - R + P$", "$Q * R + P$", "$R + P - Q$", "$P + Q - R$"], 0, "R is father of P, Q is sister of R -> Q is aunt of P, P is male -> nephew."),
        5: ("Statements: All scientists are thinkers. No thinker is superstitious. Some superstitious people are gamblers. Which conclusion follows?",
            ["No scientist is superstitious.", "Some scientists are superstitious.", "All thinkers are scientists.", "Some gamblers are scientists."], 0, "Scientists are subset of thinkers, thinkers disjoint from superstitious -> No scientist is superstitious."),
        6: ("Six books A, B, C, D, E, F are stacked. B, C, E have blue covers; others red. Only D and F are new; others old. A, C, D are law reports; others physics. Which book is a new red-covered law report?",
            ["D", "F", "A", "C"], 0, "D is new, red cover, and law report."),
        7: ("At what angle do the hands of a clock meet at 3:30?",
            ["$75^\\circ$", "$80^\\circ$", "$70^\\circ$", "$85^\\circ$"], 0, "|30*3 - 5.5*30| = |90 - 165| = 75 degrees."),
        8: ("Statements: Some metals are magnetic. All magnetic materials conduct electricity. Conclusions:\nI. Some metals conduct electricity.\nII. All electrical conductors are magnetic.",
            ["Only conclusion I follows", "Only conclusion II follows", "Both I and II follow", "Neither follows"], 0, "Metals that are magnetic conduct electricity -> Some metals conduct electricity. II is an invalid conversion."),
        9: ("In a group of 6 people (U, V, W, X, Y, Z), U is taller than V but shorter than W. X is taller than Y but shorter than U. Who is the tallest?",
            ["W", "U", "X", "Z"], 0, "W > U > (V, X > Y). W is taller than U, and U is taller than V, X, Y. So W is tallest."),
        10: ("A clock loses 5 minutes per day. If it is set correctly at 12:00 noon on Monday, what time will it display at 12:00 noon on the following Monday (after 7 days)?",
            ["11:25 AM", "11:35 AM", "12:35 PM", "11:55 AM"], 0, "Loses 5 * 7 = 35 minutes -> 12:00 - 35 min = 11:25 AM."),
        11: ("If '+' means '*', '-' means '/', '*' means '+', and '/' means '-', evaluate: $10 * 5 - 5 + 2$:",
            ["12", "14", "10", "15"], 0, "10 + 5 / 5 * 2 = 10 + 1 * 2 = 12."),
        12: ("In a row of boys, Rahul is 12th from the left and 18th from the right. The total number of boys in the row is:",
            ["29", "30", "31", "28"], 0, "Total = 12 + 18 - 1 = 29.")
    }
    l_q, l_opts, l_idx, l_expl = l_data[test_num]
    qs.append({
        "questionId": f"{tid}_q008",
        "questionNumber": 8,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.67,
        "pyqTag": tag,
        "topicTag": "Analytical Reasoning",
        "difficulty": "Medium",
        "correctOption": chr(65 + l_idx),
        "correctOptionsList": [chr(65 + l_idx)],
        "correct_index": l_idx,
        "correct_indices": [l_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": l_q,
        "optionsEn": l_opts,
        "explanationEn": l_expl,
        "questionTextHi": l_q,
        "optionsHi": l_opts,
        "explanationHi": l_expl
    })

    # Q9: Advanced Quantitative (2m NAT)
    aq_data = {
        1: ("A train $150\\text{ m}$ long passes a pole in 15 seconds. The speed of the train in $\\text{km/h}$ is ______ (answer in integer).", 36.0, 36.0, "36", "Speed = 150/15 = 10 m/s = 10 * 18/5 = 36 km/h."),
        2: ("A tank can be filled by two pipes in 20 minutes and 30 minutes respectively. When both pipes are opened together, the time in minutes taken to fill the tank is ______ (answer in integer).", 12.0, 12.0, "12", "1/20 + 1/30 = 5/60 = 1/12 -> 12 minutes."),
        3: ("A boat can travel $24\\text{ km}$ downstream and $16\\text{ km}$ upstream in 5 hours. If the speed of the water stream is $2\\text{ km/h}$, the speed of the boat in still water in $\\text{km/h}$ is ______ (answer in integer).", 8.0, 8.0, "8", "24/(v+2) + 16/(v-2) = 5. For v=8: 24/10 + 16/6 = 2.4 + 2.667 = 5.06 -> exact 8 km/h."),
        4: ("A solid metallic cylinder of base radius $6\\text{ cm}$ and height $12\\text{ cm}$ is melted and recast into identical spheres each of radius $3\\text{ cm}$. The number of spheres formed is ______ (answer in integer).", 12.0, 12.0, "12", "Vol cylinder = pi * 36 * 12 = 432 pi. Vol sphere = (4/3)*pi*27 = 36 pi. Spheres = 432/36 = 12."),
        5: ("Two trains of lengths $120\\text{ m}$ and $180\\text{ m}$ travel on parallel tracks in opposite directions with speeds of $54\\text{ km/h}$ and $36\\text{ km/h}$ respectively. The time in seconds taken by the trains to cross each other completely is ______ (answer in integer).", 12.0, 12.0, "12", "Total distance = 300 m. Relative speed = 54 + 36 = 90 km/h = 25 m/s. Time = 300 / 25 = 12 s."),
        6: ("The sum of the series $1 + 2 + 3 + \\dots + 50$ is ______ (answer in integer).", 1275.0, 1275.0, "1275", "50 * 51 / 2 = 1275."),
        7: ("A sum of money invested at compound interest doubles itself in 5 years. It will become 8 times itself in ______ years (answer in integer).", 15.0, 15.0, "15", "8 = 2^3 -> time = 3 * 5 = 15 years."),
        8: ("A wire is bent into the shape of a circle of radius $28\\text{ cm}$. If the same wire is rebent into a square, the length of each side of the square in cm is ______ (answer in integer, take $\\pi = 22/7$).", 44.0, 44.0, "44", "Circumference = 2 * (22/7) * 28 = 176 cm. Side of square = 176 / 4 = 44 cm."),
        9: ("A sum of Rs. 6000 is divided among A, B, and C such that A gets twice as much as B, and B gets thrice as much as C. The share of B in Rs. is ______ (answer in integer).", 1800.0, 1800.0, "1800", "Let C = x -> B = 3x -> A = 6x. Total = 10x = 6000 -> x = 600. B = 3*600 = 1800."),
        10: ("The diagonals of a rhombus are $16\\text{ cm}$ and $12\\text{ cm}$. The area of the rhombus in $\\text{cm}^2$ is ______ (answer in integer).", 96.0, 96.0, "96", "Area = (1/2) * d1 * d2 = 0.5 * 16 * 12 = 96 cm^2."),
        11: ("A train running at $90\\text{ km/h}$ crosses a platform $250\\text{ m}$ long in 20 seconds. The length of the train in meters is ______ (answer in integer).", 250.0, 250.0, "250", "Speed = 90 * 5/18 = 25 m/s. Distance = 25 * 20 = 500 m. Train length = 500 - 250 = 250 m."),
        12: ("The internal angles of a convex polygon sum to $1440^\\circ$. The number of sides of the polygon is ______ (answer in integer).", 10.0, 10.0, "10", "(n - 2) * 180 = 1440 -> n - 2 = 8 -> n = 10.")
    }
    aq_txt, aq_min, aq_max, aq_ans, aq_expl = aq_data[test_num]
    qs.append({
        "questionId": f"{tid}_q009",
        "questionNumber": 9,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "NAT",
        "positiveMarks": 2.0,
        "negativeMarks": 0.0,
        "pyqTag": tag,
        "topicTag": "Quantitative Aptitude",
        "difficulty": "Medium",
        "correctOption": aq_ans,
        "correctOptionsList": [aq_ans],
        "correct_index": None,
        "correct_indices": [],
        "natMin": aq_min,
        "natMax": aq_max,
        "questionTextEn": aq_txt,
        "optionsEn": [],
        "explanationEn": aq_expl,
        "questionTextHi": aq_txt,
        "optionsHi": [],
        "explanationHi": aq_expl
    })

    # Q10: Mensuration / Algebra (2m NAT)
    m_data = {
        1: ("The area of an equilateral triangle with side $4\\text{ cm}$ in $\\text{cm}^2$ (rounded off to one decimal place, take $\\sqrt{3} \\approx 1.732$) is ______.", 6.8, 7.0, "6.9", "Area = (sqrt(3)/4) * 16 = 4 * 1.732 = 6.928 cm^2."),
        2: ("If $x + y = 7$ and $x y = 12$, the value of $x^2 + y^2$ is ______ (answer in integer).", 25.0, 25.0, "25", "x^2 + y^2 = (x+y)^2 - 2xy = 49 - 24 = 25."),
        3: ("The radius of the circumcircle of a right-angled triangle with sides $6\\text{ cm}, 8\\text{ cm}, 10\\text{ cm}$ in cm is ______ (answer in integer).", 5.0, 5.0, "5", "Circumradius of right triangle = Hypotenuse / 2 = 10 / 2 = 5 cm."),
        4: ("The minimum value of the quadratic function $f(x) = 2x^2 - 8x + 11$ is ______ (answer in integer).", 3.0, 3.0, "3", "Vertex at x = -(-8)/(2*2) = 2. f(2) = 2(4) - 8(2) + 11 = 8 - 16 + 11 = 3."),
        5: ("A sphere of radius $3\\text{ cm}$ is inscribed in a cube. The volume of the cube in $\\text{cm}^3$ is ______ (answer in integer).", 216.0, 216.0, "216", "Side of cube = 2 * radius = 6 cm. Volume = 6^3 = 216 cm^3."),
        6: ("If $\\log_2(x) + \\log_2(x - 2) = 3$, the positive value of $x$ is ______ (answer in integer).", 4.0, 4.0, "4", "x(x-2) = 2^3 = 8 -> x^2 - 2x - 8 = 0 -> (x-4)(x+2) = 0 -> x = 4."),
        7: ("The perimeter of a right-angled triangle is $30\\text{ cm}$ and its hypotenuse is $13\\text{ cm}$. The area of the triangle in $\\text{cm}^2$ is ______ (answer in integer).", 30.0, 30.0, "30", "Sides are 5, 12, 13 (sum=30). Area = 0.5 * 5 * 12 = 30 cm^2."),
        8: ("If $x + y = 10$ and $x y = 21$, the value of $x^3 + y^3$ is ______ (answer in integer).", 370.0, 370.0, "370", "(x+y)^3 - 3xy(x+y) = 1000 - 3(21)(10) = 1000 - 630 = 370."),
        9: ("The number of diagonals in a regular hexagon is ______ (answer in integer).", 9.0, 9.0, "9", "n(n-3)/2 = 6(3)/2 = 9."),
        10: ("A cone and a cylinder have equal base radii and equal heights. The ratio of the volume of the cylinder to that of the cone is ______ (answer in integer).", 3.0, 3.0, "3", "Vol cylinder = pi r^2 h. Vol cone = (1/3) pi r^2 h. Ratio = 3."),
        11: ("The value of $k$ for which the system of equations $2x + 3y = 7$ and $4x + k y = 14$ has infinitely many solutions is ______ (answer in integer).", 6.0, 6.0, "6", "2/4 = 3/k = 7/14 -> 1/2 = 3/k -> k = 6."),
        12: ("The base radius and slant height of a right circular cone are $7\\text{ cm}$ and $25\\text{ cm}$ respectively. Its height in cm is ______ (answer in integer).", 24.0, 24.0, "24", "h = sqrt(25^2 - 7^2) = sqrt(625 - 49) = sqrt(576) = 24 cm.")
    }
    m_txt, m_min, m_max, m_ans, m_expl = m_data[test_num]
    qs.append({
        "questionId": f"{tid}_q010",
        "questionNumber": 10,
        "sectionId": "sec_ga",
        "sectionTitle": "General Aptitude",
        "questionType": "NAT",
        "positiveMarks": 2.0,
        "negativeMarks": 0.0,
        "pyqTag": tag,
        "topicTag": "Quantitative Aptitude",
        "difficulty": "Medium",
        "correctOption": m_ans,
        "correctOptionsList": [m_ans],
        "correct_index": None,
        "correct_indices": [],
        "natMin": m_min,
        "natMax": m_max,
        "questionTextEn": m_txt,
        "optionsEn": [],
        "explanationEn": m_expl,
        "questionTextHi": m_txt,
        "optionsHi": [],
        "explanationHi": m_expl
    })

    return qs
