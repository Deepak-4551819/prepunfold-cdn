# -*- coding: utf-8 -*-
import json
import re

def check_2022():
    with open('tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    print("=== 2022 MCQs 2m negativeMarks ===")
    for q in d['questions']:
        if q['questionType'] == 'MCQ' and q.get('positiveMarks') == 2.0:
            if q.get('negativeMarks') != 0.67:
                print(f"Q{q['questionNumber']}: pos={q.get('positiveMarks')}, neg={q.get('negativeMarks')}")

    print("\n=== 2022 NATs Q29, 31-35, 59-64 ===")
    for q in d['questions']:
        qn = q['questionNumber']
        if qn in [29, 31, 32, 33, 34, 35, 59, 60, 61, 62, 63, 64]:
            print(f"Q{qn}: natMin={q.get('natMin')}, natMax={q.get('natMax')}, correctOption={q.get('correctOption')}")
            exp = q.get('explanationEn', '')
            print(f"  Exp: {exp[:150]}...")

    print("\n=== 2022 Options unwrapped LaTeX ===")
    for q in d['questions']:
        qn = q['questionNumber']
        for i, opt in enumerate(q.get('optionsEn', [])):
            if ('\\' in opt or '_' in opt or '^' in opt) and '$' not in opt:
                print(f"Q{qn} Opt {chr(65+i)}: {opt}")

def check_2023():
    with open('tests/gate/gate_ph/pyq/gate_ph_pyq_2023.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    print("\n=== 2023 Q43, Q44 options ===")
    for q in d['questions']:
        qn = q['questionNumber']
        if qn in [43, 44]:
            print(f"Q{qn} optionsEn: {q.get('optionsEn')}")
            print(f"Q{qn} correctOption: {q.get('correctOption')}, correctOptionsList: {q.get('correctOptionsList')}")
        if qn in [60, 63]:
            print(f"Q{qn} natMin={q.get('natMin')}, natMax={q.get('natMax')}, exp={q.get('explanationEn')[:150]}")
    print("\n=== 2023 2m MCQs negativeMarks ===")
    for q in d['questions']:
        if q['questionType'] == 'MCQ' and q.get('positiveMarks') == 2.0:
            if q.get('negativeMarks') != 0.67:
                print(f"Q{q['questionNumber']}: pos={q.get('positiveMarks')}, neg={q.get('negativeMarks')}")
    print("\n=== 2023 Options unwrapped LaTeX ===")
    for q in d['questions']:
        qn = q['questionNumber']
        for i, opt in enumerate(q.get('optionsEn', [])):
            if ('\\' in opt or '_' in opt or '^' in opt) and '$' not in opt:
                print(f"Q{qn} Opt {chr(65+i)}: {opt}")

def check_2024():
    with open('tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    print("\n=== 2024 Q47, Q61 ===")
    for q in d['questions']:
        qn = q['questionNumber']
        if qn in [47, 61]:
            print(f"Q{qn} type={q.get('questionType')}, correctOption={q.get('correctOption')}, correctOptionsList={q.get('correctOptionsList')}, natMin={q.get('natMin')}, natMax={q.get('natMax')}")
            print(f"Q{qn} exp: {q.get('explanationEn')[:200]}")
    print("\n=== 2024 questionIds ===")
    extra_zeros = [q['questionId'] for q in d['questions'] if re.match(r'gate_ph_2024_q0\d\d', q['questionId'])]
    print(f"Total questionIds with extra zero: {len(extra_zeros)} (sample: {extra_zeros[:5]})")

def check_2025():
    with open('tests/gate/gate_ph/pyq/gate_ph_pyq_2025.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    print("\n=== 2025 explanations ===")
    placeholders = [q['questionNumber'] for q in d['questions'] if 'Official GATE 2025 PH Answer Key' in q.get('explanationEn', '') or len(q.get('explanationEn', '')) < 80]
    print(f"Total placeholder explanations in 2025: {len(placeholders)}")
    print(f"Sample placeholder questions: {placeholders[:10]}")

def check_2026():
    with open('tests/gate/gate_ph/pyq/gate_ph_pyq_2026.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    print("\n=== 2026 explanations ===")
    placeholders = [q['questionNumber'] for q in d['questions'] if 'Official GATE' in q.get('explanationEn', '') or len(q.get('explanationEn', '')) < 80]
    print(f"Total placeholder explanations in 2026: {len(placeholders)}")
    print(f"Sample placeholder questions: {placeholders[:10]}")

if __name__ == '__main__':
    check_2022()
    check_2023()
    check_2024()
    check_2025()
    check_2026()
