import json
import os
import re

def create_gate_ph_2023():
    # Load raw text
    with open('temp_gate_pdfs/gate_ph_2023_text.txt', encoding='utf-8') as f:
        raw_text = f.read()

    # Pre-clean
    cleaned_lines = []
    for line in raw_text.split('\n'):
        l = line.strip()
        if not l:
            continue
        if any(drop in l for drop in [
            'GATE Physics Question Paper-2023',
            'Physics by fiziks',
            'Learn Physics in Right Way',
            'H.No. 40-D',
            'Phone: 011-',
            'Website: www.physicsbyfiziks.com',
            'Be Part of Disciplined Learning',
            '=== PAGE '
        ]):
            continue
        cleaned_lines.append(line)

    cleaned_text = '\n'.join(cleaned_lines)
    parts = re.split(r'\n(?=Q\d+\.)', cleaned_text)

    # We will build question items
    questions = []

    # Ground truth answer key table
    # (q_num, q_type, marks, neg, key, options_list, nat_min, nat_max, topic)
    meta = {
        1: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Verbal Aptitude", "Easy"),
        2: ("MCQ", 1.0, 0.33, "C", ["C"], None, None, "Verbal Aptitude", "Easy"),
        3: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Quantitative Aptitude", "Easy"),
        4: ("MCQ", 1.0, 0.33, "D", ["D"], None, None, "Verbal Aptitude", "Easy"),
        5: ("MCQ", 1.0, 0.33, "C", ["C"], None, None, "Spatial Aptitude", "Medium"),
        6: ("MCQ", 2.0, 0.66, "D", ["D"], None, None, "Analytical Aptitude", "Medium"),
        7: ("MCQ", 2.0, 0.66, "A", ["A"], None, None, "Quantitative Aptitude", "Easy"),
        8: ("MCQ", 2.0, 0.66, "C", ["C"], None, None, "Verbal Aptitude", "Medium"),
        9: ("MCQ", 2.0, 0.66, "A", ["A"], None, None, "Quantitative Aptitude", "Easy"),
        10: ("MCQ", 2.0, 0.66, "D", ["D"], None, None, "Spatial Aptitude", "Easy"),
        11: ("MCQ", 1.0, 0.0, "A", ["A", "B", "C", "D"], None, None, "Thermodynamics & Statistical Physics", "Medium"), # MTA
        12: ("MCQ", 1.0, 0.33, "D", ["D"], None, None, "Atomic & Molecular Physics", "Easy"),
        13: ("MCQ", 1.0, 0.33, "A", ["A"], None, None, "Electronics", "Easy"),
        14: ("MCQ", 1.0, 0.33, "A", ["A"], None, None, "Atomic & Molecular Physics", "Easy"),
        15: ("MCQ", 1.0, 0.0, "A", ["A", "B", "C", "D"], None, None, "Quantum Mechanics", "Medium"), # MTA
        16: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Solid State Physics", "Medium"),
        17: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Mathematical Physics", "Medium"),
        18: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Solid State Physics", "Easy"),
        19: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Solid State Physics", "Easy"),
        20: ("MCQ", 1.0, 0.33, "D", ["D"], None, None, "Solid State Physics", "Medium"),
        21: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Solid State Physics", "Easy"),
        22: ("MCQ", 1.0, 0.33, "A", ["A"], None, None, "Solid State Physics", "Easy"),
        23: ("MCQ", 1.0, 0.33, "C", ["C"], None, None, "Nuclear & Particle Physics", "Easy"),
        24: ("MCQ", 1.0, 0.33, "D", ["D"], None, None, "Electronics", "Easy"),
        25: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Atomic & Molecular Physics", "Easy"),
        26: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Mathematical Physics", "Medium"),
        27: ("MCQ", 1.0, 0.33, "B", ["B"], None, None, "Mathematical Physics", "Medium"),
        28: ("MSQ", 1.0, 0.0, None, ["B", "C"], None, None, "Thermodynamics & Statistical Physics", "Medium"),
        29: ("MSQ", 1.0, 0.0, None, ["A", "C"], None, None, "Nuclear & Particle Physics", "Medium"),
        30: ("MSQ", 1.0, 0.0, None, ["A", "B", "C"], None, None, "Nuclear & Particle Physics", "Medium"),
        31: ("MSQ", 1.0, 0.0, None, ["A", "B", "D"], None, None, "Electromagnetic Theory", "Medium"),
        32: ("MSQ", 1.0, 0.0, None, ["A", "B", "D"], None, None, "Mathematical Physics", "Medium"),
        33: ("NAT", 1.0, 0.0, None, [], 45.0, 45.0, "Atomic & Molecular Physics", "Medium"),
        34: ("NAT", 1.0, 0.0, None, [], 2.20, 2.36, "Electronics", "Medium"),
        35: ("NAT", 1.0, 0.0, None, [], 0.36, 0.40, "Electromagnetic Theory", "Medium"),
        36: ("MCQ", 2.0, 0.66, "C", ["C"], None, None, "Atomic & Molecular Physics", "Hard"),
        37: ("MCQ", 2.0, 0.66, "A", ["A"], None, None, "Electronics", "Medium"),
        38: ("MCQ", 2.0, 0.66, "A", ["A"], None, None, "Thermodynamics & Statistical Physics", "Hard"),
        39: ("MCQ", 2.0, 0.66, "A", ["A"], None, None, "Nuclear & Particle Physics", "Medium"),
        40: ("MCQ", 2.0, 0.66, "C", ["C"], None, None, "Classical Mechanics", "Medium"),
        41: ("MCQ", 2.0, 0.0, "A", ["A", "B", "C", "D"], None, None, "Classical Mechanics", "Hard"), # MTA
        42: ("MCQ", 2.0, 0.66, "D", ["D"], None, None, "Classical Mechanics", "Medium"),
        43: ("MCQ", 2.0, 0.66, "D", ["D"], None, None, "Mathematical Physics", "Medium"),
        44: ("MCQ", 2.0, 0.66, "D", ["D"], None, None, "Quantum Mechanics", "Medium"),
        45: ("MCQ", 2.0, 0.66, "B", ["B"], None, None, "Solid State Physics", "Hard"),
        46: ("MCQ", 2.0, 0.66, "C", ["C"], None, None, "Solid State Physics", "Medium"),
        47: ("MCQ", 2.0, 0.66, "B", ["B"], None, None, "Solid State Physics", "Medium"),
        48: ("MCQ", 2.0, 0.66, "A", ["A"], None, None, "Nuclear & Particle Physics", "Medium"),
        49: ("MCQ", 2.0, 0.66, "C", ["C"], None, None, "Quantum Mechanics", "Medium"),
        50: ("MCQ", 2.0, 0.66, "C", ["C"], None, None, "Quantum Mechanics", "Medium"),
        51: ("MCQ", 2.0, 0.66, "B", ["B"], None, None, "Quantum Mechanics", "Medium"),
        52: ("MCQ", 2.0, 0.66, "A", ["A"], None, None, "Quantum Mechanics", "Hard"),
        53: ("MCQ", 2.0, 0.66, "D", ["D"], None, None, "Quantum Mechanics", "Medium"),
        54: ("MCQ", 2.0, 0.66, "C", ["C"], None, None, "Atomic & Molecular Physics", "Medium"),
        55: ("MSQ", 2.0, 0.0, None, ["A"], None, None, "Electromagnetic Theory", "Hard"),
        56: ("MSQ", 2.0, 0.0, None, ["B"], None, None, "Mathematical Physics", "Hard"),
        57: ("MSQ", 2.0, 0.0, None, ["A", "C", "D"], None, None, "Classical Mechanics", "Hard"),
        58: ("MSQ", 2.0, 0.0, None, ["A", "C"], None, None, "Nuclear & Particle Physics", "Hard"),
        59: ("NAT", 2.0, 0.0, None, [], 2.0, 2.0, "Electromagnetic Theory", "Hard"), # MTA officially
        60: ("NAT", 2.0, 0.0, None, [], 326.9, 327.1, "Nuclear & Particle Physics", "Hard"),
        61: ("NAT", 2.0, 0.0, None, [], 11.0, 13.7, "Electromagnetic Theory", "Hard"),
        62: ("NAT", 2.0, 0.0, None, [], 4.90, 4.94, "Nuclear & Particle Physics", "Medium"),
        63: ("NAT", 2.0, 0.0, None, [], 15.0, 15.0, "Thermodynamics & Statistical Physics", "Hard"),
        64: ("NAT", 2.0, 0.0, None, [], 0.6, 0.6, "Thermodynamics & Statistical Physics", "Hard"),
        65: ("NAT", 2.0, 0.0, None, [], 200.0, 200.0, "Thermodynamics & Statistical Physics", "Hard")
    }

    # Now let's build the 65 question dictionaries
    for q_num in range(1, 66):
        q_type, pos_m, neg_m, c_opt, opt_list, n_min, n_max, topic, diff = meta[q_num]
        sec_id = "sec_ga" if q_num <= 10 else "sec_ph"
        sec_title = "General Aptitude" if q_num <= 10 else "Physics"

        # Determine indices
        opt_to_idx = {"A": 0, "B": 1, "C": 2, "D": 3}
        c_idx = opt_to_idx.get(c_opt) if c_opt in opt_to_idx else None
        c_indices = [opt_to_idx[o] for o in opt_list if o in opt_to_idx]

        questions.append({
            "questionId": f"gate_ph_2023_q{q_num:02d}",
            "questionNumber": q_num,
            "sectionId": sec_id,
            "sectionTitle": sec_title,
            "questionType": q_type,
            "positiveMarks": pos_m,
            "negativeMarks": neg_m,
            "pyqTag": "GATE Physics (PH) • 2023 Official Paper",
            "topicTag": topic,
            "difficulty": diff,
            "correctOption": c_opt,
            "correctOptionsList": opt_list,
            "correct_index": c_idx,
            "correct_indices": c_indices,
            "natMin": n_min,
            "natMax": n_max,
            # Placeholder text fields to be populated from questions data
            "questionTextEn": "",
            "optionsEn": [],
            "explanationEn": "",
            "questionTextHi": "",
            "optionsHi": [],
            "explanationHi": ""
        })

    print(f'Constructed meta skeleton for {len(questions)} questions.')
    return questions

if __name__ == '__main__':
    create_gate_ph_2023()
