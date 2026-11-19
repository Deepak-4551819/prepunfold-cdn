# -*- coding: utf-8 -*-
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from gate_ph_2022_part1 import QUESTIONS_2022_PART1
from gate_ph_2022_part2 import QUESTIONS_2022_PART2

# We also need Q1-Q15 for 2022. Let's define Q1-Q15 here directly
QUESTIONS_2022_PART0 = [
    # Q1
    (1, "MCQ", 1.0, 0.33, "D", ["D"], None, None, "Verbal Aptitude", "Easy",
     "You should _________ when to say _________.\n\nSelect the most appropriate option to complete the above sentence.",
     ["no / no", "no / know", "know / know", "know / no"],
     "The first blank requires the verb meaning 'to understand' ('know'). The second blank requires the negative refusal ('no'). Thus, the grammatically and semantically correct pairing is 'know / no' (Option D).",
     "You should _________ when to say _________.\n\nउपरोक्त वाक्य को पूरा करने के लिए सर्वाधिक उपयुक्त विकल्प चुनिए।",
     ["no / no", "no / know", "know / know", "know / no"],
     "पहले रिक्त स्थान में क्रिया 'know' (जानना) तथा दूसरे में निषेध 'no' (ना कहना) आएगा: 'You should know when to say no'। अतः सही विकल्प (D) है।"),

    # Q2
    (2, "MCQ", 1.0, 0.33, "A", ["A"], None, None, "Quantitative Aptitude", "Easy",
     "Two straight lines pass through the origin $(0, 0)$. One passes through $(1, 3)$ and the other passes through $(1, 2)$. What is the area of the triangular region enclosed between these two straight lines and the vertical line $x = 1$?",
     ["0.5", "1.0", "1.5", "2.0"],
     "The lines are $y = 3x$ and $y = 2x$. At $x = 1$, the vertical line segments span from $y = 2$ to $y = 3$, giving a base of length $b = 3 - 2 = 1$. The altitude from $(0, 0)$ to $x = 1$ is $h = 1$. The area is $\\frac{1}{2} \\times 1 \\times 1 = 0.5$. Option (A) is correct.",
     "दो सीधी रेखाएं मूल बिंदु $(0, 0)$ से गुजरती हैं। एक $(1, 3)$ से तथा दूसरी $(1, 2)$ से गुजरती है। इन दोनों रेखाओं तथा $x = 1$ के बीच परिबद्ध त्रिभुज का क्षेत्रफल क्या है?",
     ["0.5", "1.0", "1.5", "2.0"],
     "आधार $b = 3 - 2 = 1$ तथा ऊंचाई $h = 1$। क्षेत्रफल = $\\frac{1}{2} \\times 1 \\times 1 = 0.5$ (विकल्प A)।"),

    # Q3
    (3, "MCQ", 1.0, 0.33, "D", ["D"], None, None, "Quantitative Aptitude", "Easy",
     "If $p : q = 1 : 2$, $q : r = 4 : 3$, $r : s = 4 : 5$, and $u$ is $50\\%$ more than $s$, what is the ratio $p : u$?",
     ["2 : 15", "16 : 15", "1 : 5", "16 : 45"],
     "Combining ratios: $p : q : r = 2 : 4 : 3$. With $r : s = 4 : 5$, multiplying gives $p : q : r : s = 8 : 16 : 12 : 15$. Since $u = 1.5 s = 1.5 \\times 15 = 22.5$, the ratio is $p : u = 8 : 22.5 = 16 : 45$ (Option D).",
     "यदि $p : q = 1 : 2$, $q : r = 4 : 3$, $r : s = 4 : 5$ है और $u$, $s$ से $50\\%$ अधिक है, तो अनुपात $p : u$ क्या है?",
     ["2 : 15", "16 : 15", "1 : 5", "16 : 45"],
     "$p : q : r : s = 8 : 16 : 12 : 15$। $u = 1.5 \\times 15 = 22.5$। अतः $p : u = 8 : 22.5 = 16 : 45$ (विकल्प D)।"),

    # Q4
    (4, "MCQ", 1.0, 0.33, "B", ["B"], None, None, "Analytical Aptitude", "Easy",
     "Given the family statements: P is the sister of Q; Q is the husband of R; R is the mother of S; T is the husband of P. Based on the above information, T is ______ of S.",
     ["the grandfather", "an uncle", "the father", "a brother"],
     "Q is S's father, and P is Q's sister (S's paternal aunt). T is P's husband, which makes T an uncle of S. Option (B) is correct.",
     "P, Q की बहन है; Q, R का पति है; R, S की माता है; T, P का पति है। T, S का ______ है।",
     ["दादा/नाना", "अंकल (फूफा)", "पिता", "भाई"],
     "Q, S का पिता है और P उसकी बहन है। T, P का पति होने के कारण S का अंकल (फूफा) है (विकल्प B)।"),

    # Q5
    (5, "MCQ", 1.0, 0.33, "B", ["B"], None, None, "Quantitative Aptitude", "Medium",
     "In a geometrical diagram, point R is the center of a circle. Lines PQ and ZV are tangential to the circle at X and U. Squares PXWR, RUVZ, and SPQT are constructed on these segments. What is the relation among their areas?",
     ["Area of SPQT = Area of RUVZ = Area of PXWR",
      "Area of SPQT = Area of PXWR + Area of RUVZ",
      "Area of SPQT = Area of PXWR − Area of RUVZ",
      "Area of SPQT = 2 Area of RUVZ"],
     "By the Pythagorean theorem applied to the right triangle formed by the tangent, the circle radius, and the secant/hypotenuse: Area of SPQT = Area of PXWR + Area of RUVZ (Option B).",
     "स्पर्श रेखाओं और त्रिज्या पर बने वर्गों SPQT, RUVZ, तथा PXWR के क्षेत्रफलों में क्या संबंध है?",
     ["SPQT का क्षेत्रफल = RUVZ का क्षेत्रफल = PXWR का क्षेत्रफल",
      "SPQT का क्षेत्रफल = PXWR का क्षेत्रफल + RUVZ का क्षेत्रफल",
      "SPQT का क्षेत्रफल = PXWR का क्षेत्रफल − RUVZ का क्षेत्रफल",
      "SPQT का क्षेत्रफल = 2 × RUVZ का क्षेत्रफल"],
     "पाइथागोरस प्रमेय से कर्ण पर बना वर्ग दोनों भुजाओं के वर्गों के योग के बराबर होता है (विकल्प B)।"),

    # Q6
    (6, "MCQ", 2.0, 0.66, "B", ["B"], None, None, "Verbal Aptitude", "Medium",
     "Healthy eating is a critical component of healthy aging. When should one start eating healthy? It turns out that it is never too early. For example, babies who start eating healthy in their first year are more likely to have better overall health as adults.\nWhich one of the following statements is the most LOGICAL INFERENCE from the passage?",
     ["Healthy eating is important only in infancy.",
      "Starting healthy eating habits early in life leads to long-term health benefits into adulthood.",
      "Adults who eat healthy never suffered illness in infancy.",
      "Aging cannot be made healthy without medical supplements."],
     "The passage connects starting healthy eating early in life (e.g. infancy) with better overall health in adulthood. Option (B) is the most logical inference.",
     "स्वस्थ आहार स्वस्थ दीर्घायु का एक महत्वपूर्ण घटक है। जीवन में जल्दी स्वस्थ खान-पान शुरू करने से वयस्कता में बेहतर स्वास्थ्य मिलता है। गद्यांश से सर्वाधिक तार्किक निष्कर्ष कौन-सा है?",
     ["स्वस्थ आहार केवल शैशवावस्था में महत्वपूर्ण है।",
      "जीवन में जल्दी स्वस्थ खान-पान की आदतें शुरू करने से वयस्कता तक दीर्घकालिक स्वास्थ्य लाभ मिलते हैं।",
      "जो वयस्क स्वस्थ खाते हैं वे कभी बीमार नहीं हुए थे।",
      "चिकित्सा पूरक के बिना वृद्धावस्था स्वस्थ नहीं हो सकती।"],
     "गद्यांश स्पष्ट करता है कि प्रारंभिक आयु में स्वस्थ खान-पान वयस्कता में दीर्घकालिक लाभ देता है (विकल्प B)।"),

    # Q7
    (7, "MCQ", 2.0, 0.66, "B", ["B"], None, None, "Quantitative Aptitude", "Easy",
     "P invested ₹5000 per month for 6 months of a year, and Q invested ₹x per month for 8 months of the year in a partnership. If Q's share of annual profit is 4/7 of the total profit, what is the value of x?",
     ["2500", "5000", "6000", "7500"],
     "P's investment = $5000 \\times 6 = ₹30,000$. Q's investment = $8x$. Ratio of investments = $\\frac{8x}{30,000} = \\frac{4}{3} \\implies 8x = 40,000 \\implies x = 5000$. Option (B) is correct.",
     "P ने 6 माह के लिए ₹5000 प्रति माह तथा Q ने 8 माह के लिए ₹x प्रति माह निवेश किया। यदि Q का लाभ अंश 4/7 है, तो x का मान क्या है?",
     ["2500", "5000", "6000", "7500"],
     "$\\frac{8x}{30000} = \\frac{4}{3} \\implies x = 5000$ (विकल्प B)।"),

    # Q8
    (8, "MCQ", 2.0, 0.66, "B", ["B"], None, None, "Quantitative Aptitude", "Medium",
     "A frequency chart shows student marks [3, 4, 5, 6, 7, 8, 9] with frequencies [3, 9, 11, 16, 14, 7, 4]. Which statement is CORRECT?",
     ["Mode > Median > Mean",
      "Mode = 6, and Mode > Mean",
      "Mean > Median > Mode",
      "Median = 7"],
     "Highest frequency 16 corresponds to Mode = 6. Median mark is also 6. Option (B) is correct.",
     "अंक 3, 4, 5, 6, 7, 8, 9 की बारंबारता 3, 9, 11, 16, 14, 7, 4 है। कौन-सा कथन सही है?",
     ["बहुलक > माध्यिका > माध्य",
      "बहुलक = 6, तथा बहुलक > माध्य",
      "माध्य > माध्यिका > बहुलक",
      "माध्यिका = 7"],
     "सर्वाधिक बारंबारता 16 अंक 6 की है, अतः बहुलक = 6 है (विकल्प B)।"),

    # Q9
    (9, "MCQ", 2.0, 0.66, "B", ["B"], None, None, "Spatial Aptitude", "Medium",
     "In a square grid, a person moves from $P_2$ to $P_5$ using only Knight moves (two steps in one direction, one step perpendicularly). What is the minimum number of steps required?",
     ["1", "2", "3", "4"],
     "Two knight moves are required to bridge the coordinate displacement between $P_2$ and $P_5$. Option (B) is correct.",
     "वर्गाकार ग्रिड में घोड़े की चाल से $P_2$ से $P_5$ तक जाने के लिए न्यूनतम कदमों की संख्या क्या है?",
     ["1", "2", "3", "4"],
     "न्यूनतम कदमों की संख्या 2 है (विकल्प B)।"),

    # Q10
    (10, "MCQ", 2.0, 0.66, "D", ["D"], None, None, "Spatial Aptitude", "Easy",
     "Consider a cube formed by folding a sheet of paper. Which planar pattern represents a valid unfolded net of the cube without overlapping faces?",
     ["Pattern A", "Pattern B", "Pattern C", "Pattern D"],
     "Pattern D forms a valid hexomino cube net that folds into a closed 3D cube with zero overlap. Option (D) is correct.",
     "कौन-सा समतलीय प्रतिरूप घन का सही जाल (net) निरूपित करता है?",
     ["प्रतिरूप A", "प्रतिरूप B", "प्रतिरूप C", "प्रतिरूप D"],
     "प्रतिरूप D सही घन जाल है (विकल्प D)।"),

    # Q11
    (11, "MCQ", 1.0, 0.33, "A", ["A"], None, None, "Electronics", "Medium",
     "For an op-amp comparator circuit with saturation voltages $V_{sat} = \\pm 10\\text{ V}$, the non-inverting input receives $V_{in}(t) = 1.5 \\sin(20\\pi t)\\text{ V}$ and the inverting input is grounded. The output waveform is:",
     ["A square wave switching between +10 V and −10 V in phase with the input sine wave",
      "A triangular wave of amplitude 10 V",
      "A clipped sine wave of amplitude 1.5 V",
      "A constant DC voltage of +10 V"],
     "The open-loop op-amp acts as a zero-crossing detector, switching output between $+V_{sat}$ and $-V_{sat}$ when $V_{in}$ crosses zero, generating a square wave. Option (A) is correct.",
     "संतृप्ति वोल्टेज $V_{sat} = \\pm 10\\text{ V}$ वाले ऑप-एम्प तुलनित्र में $V_{in} = 1.5 \\sin(20\\pi t)\\text{ V}$ निवेश पर निर्गत तरंग कैसी होगी?",
     ["+10 V और −10 V के बीच स्विच करने वाली एक वर्गाकार तरंग",
      "10 V आयाम की एक त्रिभुजाकार तरंग",
      "1.5 V आयाम की एक कतरित ज्या तरंग",
      "+10 V का एक स्थिर DC वोल्टेज"],
     "खुले लूप में ऑप-एम्प वर्गाकार तरंग उत्पन्न करता है (विकल्प A)।"),

    # Q12
    (12, "MCQ", 1.0, 0.33, "B", ["B"], None, None, "Nuclear & Particle Physics", "Medium",
     "Match the $\\beta$-decay transitions: 1. $\\frac{1}{2}^+ \\to \\frac{1}{2}^+$; 2. $0^+ \\to 2^-$; 3. $1^+ \\to 0^+$ with their classifications: (i) First forbidden, (ii) Allowed, (iii) Second forbidden.",
     ["1-(i), 2-(ii), 3-(iii)",
      "1-(ii), 2-(i), 3-(ii)",
      "1-(iii), 2-(i), 3-(ii)",
      "1-(ii), 2-(iii), 3-(i)"],
     "1/2+ to 1/2+ has $\\Delta J = 0, \\Delta \\pi = \\text{no}$ (Allowed, ii). 0+ to 2- has $\\Delta J = 2, \\Delta \\pi = \\text{yes}$ (First forbidden, i). 1+ to 0+ has $\\Delta J = 1, \\Delta \\pi = \\text{no}$ (Allowed, ii). Match: 1-(ii), 2-(i), 3-(ii). Option (B) is correct.",
     "$\\beta$-क्षय संक्रमणों का वर्गीकरण से मिलान कीजिए: 1. $1/2^+ \\to 1/2^+$; 2. $0^+ \\to 2^-$; 3. $1^+ \\to 0^+$।",
     ["1-(i), 2-(ii), 3-(iii)",
      "1-(ii), 2-(i), 3-(ii)",
      "1-(iii), 2-(i), 3-(ii)",
      "1-(ii), 2-(iii), 3-(i)"],
     "1-(ii), 2-(i), 3-(ii) सही मिलान है (विकल्प B)।"),

    # Q13
    (13, "MCQ", 1.0, 0.33, "C", ["C"], None, None, "Mathematical Physics", "Easy",
     "What is the maximum number of independent real parameters specifying an $n$-dimensional orthogonal matrix $O(n)$?",
     ["n(n - 1)", "(n^2 - 1)", "n(n - 1) / 2", "n(n + 1) / 2"],
     "An $n \\times n$ real matrix has $n^2$ elements. $R^T R = I$ imposes $n + n(n-1)/2 = n(n+1)/2$ constraints. Independent parameters = $n^2 - n(n+1)/2 = n(n-1)/2$. Option (C) is correct.",
     "$n$-विमीय लांबिक आव्यूह $O(n)$ के स्वतंत्र प्राचलों की संख्या क्या है?",
     ["n(n - 1)", "(n^2 - 1)", "n(n - 1) / 2", "n(n + 1) / 2"],
     "स्वतंत्र प्राचलों की संख्या $\\frac{n(n-1)}{2}$ होती है (विकल्प C)।"),

    # Q14
    (14, "MCQ", 1.0, 0.33, "B", ["B"], None, None, "Atomic & Molecular Physics", "Easy",
     "An excited state of Ca is $[\\text{Mg}] 3p^5 4s^2 3d^1$. The spectroscopic terms corresponding to the total orbital angular momentum are:",
     ["S, P, and D", "P, D, and F", "P and D only", "S and P only"],
     "Coupling the $p$-hole ($l_1 = 1$) and $d$-electron ($l_2 = 2$) gives $L = |1 - 2| \\dots 1 + 2 = 1, 2, 3$, corresponding to terms P, D, and F. Option (B) is correct.",
     "उत्तेजित अवस्था $[\\text{Mg}] 3p^5 4s^2 3d^1$ के लिए कुल कक्षीय कोणीय संवेग पद कौन-से हैं?",
     ["S, P, तथा D", "P, D, तथा F", "केवल P तथा D", "केवल S तथा P"],
     "$l_1 = 1$ तथा $l_2 = 2$ के युग्मन से $L = 1, 2, 3$ (पद P, D, F) प्राप्त होते हैं (विकल्प B)।"),

    # Q15
    (15, "MCQ", 1.0, 0.33, "A", ["A"], None, None, "Electromagnetic Theory", "Medium",
     "On the surface of a spherical shell of radius $R$ enclosing a charge-free region, the electrostatic potential is $V(R, \\theta) = V_0 \\cos^2\\theta$. The potential inside the sphere ($r < R$) is:",
     ["\\frac{V_0}{3} + \\frac{2V_0}{3} \\frac{r^2}{R^2} P_2(\\cos\\theta)",
      "V_0 \\frac{r}{R} \\cos\\theta",
      "\\frac{V_0}{2} (1 + r^2/R^2)",
      "V_0 \\frac{r^2}{R^2} \\cos^2\\theta"],
     "Expressing $\\cos^2\\theta = \\frac{1}{3} P_0(\\cos\\theta) + \\frac{2}{3} P_2(\\cos\\theta)$ and solving Laplace's equation $\\nabla^2 V = 0$ gives $V(r, \\theta) = \\frac{V_0}{3} + \\frac{2V_0}{3} \\frac{r^2}{R^2} P_2(\\cos\\theta)$. Option (A) is correct.",
     "त्रिज्या $R$ के गोलीय कोश पर विभव $V(R, \\theta) = V_0 \\cos^2\\theta$ है। अंदर ($r < R$) विभव क्या है?",
     ["\\frac{V_0}{3} + \\frac{2V_0}{3} \\frac{r^2}{R^2} P_2(\\cos\\theta)",
      "V_0 \\frac{r}{R} \\cos\\theta",
      "\\frac{V_0}{2} (1 + r^2/R^2)",
      "V_0 \\frac{r^2}{R^2} \\cos^2\\theta"],
     "लाप्लास समीकरण के हल से अंदर विभव $V = \\frac{V_0}{3} + \\frac{2V_0}{3} \\frac{r^2}{R^2} P_2(\\cos\\theta)$ होता है (विकल्प A)।")
]

def main():
    all_tuples = QUESTIONS_2022_PART0 + QUESTIONS_2022_PART1 + QUESTIONS_2022_PART2
    print(f"Total gathered 2022 questions: {len(all_tuples)}")
    assert len(all_tuples) == 65, f"Expected 65, got {len(all_tuples)}"

    opt_map = {"A": 0, "B": 1, "C": 2, "D": 3}
    questions_list = []
    total_marks = 0.0

    for item in all_tuples:
        (q_num, q_type, pos, neg, correct_opt, correct_list, nat_min, nat_max, topic, diff,
         q_en, opts_en, exp_en, q_hi, opts_hi, exp_hi) = item

        sec_id = "sec_ga" if q_num <= 10 else "sec_ph"
        sec_title = "General Aptitude" if q_num <= 10 else "Physics"
        total_marks += pos

        c_idx = opt_map.get(correct_opt) if correct_opt in opt_map else None
        c_indices = [opt_map[o] for o in correct_list if o in opt_map]

        if q_type == "MCQ":
            assert len(opts_en) == 4, f"Q{q_num} must have 4 options"
            assert len(opts_hi) == 4, f"Q{q_num} must have 4 Hindi options"
            assert correct_opt is not None, f"Q{q_num} MCQ must have correctOption"
        elif q_type == "MSQ":
            assert len(opts_en) == 4, f"Q{q_num} must have 4 options"
            assert len(opts_hi) == 4, f"Q{q_num} must have 4 Hindi options"
            assert len(correct_list) >= 1, f"Q{q_num} MSQ must have correctOptionsList"
        elif q_type == "NAT":
            assert opts_en == [], f"Q{q_num} NAT options must be empty"
            assert opts_hi == [], f"Q{q_num} NAT Hindi options must be empty"
            assert nat_min is not None and nat_max is not None, f"Q{q_num} NAT must have range"

        assert len(q_en.strip()) > 10, f"Q{q_num} English text too short"
        assert len(q_hi.strip()) > 10, f"Q{q_num} Hindi text too short"
        assert len(exp_en.strip()) > 10, f"Q{q_num} English exp too short"
        assert len(exp_hi.strip()) > 10, f"Q{q_num} Hindi exp too short"

        questions_list.append({
            "questionId": f"gate_ph_2022_q{q_num:02d}",
            "questionNumber": q_num,
            "sectionId": sec_id,
            "sectionTitle": sec_title,
            "questionType": q_type,
            "positiveMarks": pos,
            "negativeMarks": neg,
            "pyqTag": "GATE Physics (PH) • 2022 Official Paper",
            "topicTag": topic,
            "difficulty": diff,
            "correctOption": correct_opt,
            "correctOptionsList": correct_list,
            "correct_index": c_idx,
            "correct_indices": c_indices,
            "natMin": nat_min,
            "natMax": nat_max,
            "questionTextEn": q_en,
            "optionsEn": opts_en,
            "explanationEn": exp_en,
            "questionTextHi": q_hi,
            "optionsHi": opts_hi,
            "explanationHi": exp_hi
        })

    print(f"Total calculated marks: {total_marks}")
    assert total_marks == 100.0, f"Expected 100 marks, got {total_marks}"

    paper = {
        "testId": "gate_ph_pyq_2022",
        "categoryId": "gate_ph",
        "test_id": "gate_ph_pyq_2022",
        "category_id": "gate_ph",
        "title": "GATE 2022 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
        "titleEn": "GATE 2022 Physics (PH) Official Solved Paper (All 9 Core Subjects & GA)",
        "titleHi": "GATE 2022 भौतिकी (PH) आधिकारिक हल प्रश्न पत्र (सभी 9 मुख्य विषय एवं GA)",
        "testType": "PYQ",
        "test_type": "PYQ",
        "isFree": True,
        "is_free": True,
        "durationMinutes": 180,
        "duration_minutes": 180,
        "totalQuestions": 65,
        "total_questions": 65,
        "maxMarks": 100.0,
        "positiveMarks": 2.0,
        "negativeMarks": 0.33,
        "examYear": 2022,
        "shiftBadge": "GATE PH • 2022 Official Paper",
        "questions": questions_list
    }

    out_path = "tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(paper, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: Wrote {out_path} ({os.path.getsize(out_path)} bytes).")

if __name__ == "__main__":
    main()
