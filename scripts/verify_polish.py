# -*- coding: utf-8 -*-
import json
import sys

def verify():
    # 1. Check Q48
    d26 = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2026.json', 'r', encoding='utf-8'))
    for q in d26['questions']:
        if q['questionNumber'] == 48:
            print('--- 2026 Q48 ---')
            print('Text:', q['questionTextEn'])
            print('Options:', q['optionsEn'])
            print('Correct:', q['correctOption'])
            assert '$+y$ direction' in q['questionTextEn']
            assert q['optionsEn'][1] == 'in the $+y$ direction'
            assert q['correctOption'] == 'B'
            assert 'Wait' not in q['explanationEn']

    # 2. Check 2021 Q6
    d21 = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json', 'r', encoding='utf-8'))
    for q in d21['questions']:
        if q['questionNumber'] == 6:
            print('--- 2021 Q6 ---')
            print('Exp ends with:', q['explanationEn'][-150:])
            assert 'Wait' not in q['explanationEn']

    # 3. Check 2025 Q36
    d25 = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2025.json', 'r', encoding='utf-8'))
    for q in d25['questions']:
        if q['questionNumber'] == 36:
            print('--- 2025 Q36 ---')
            print('Exp starts with:', q['explanationEn'][:150])
            assert 'Hold on' not in q['explanationEn']
            assert 'wait' not in q['explanationEn'].lower()

    # 4. Check 2026 Q38
    for q in d26['questions']:
        if q['questionNumber'] == 38:
            print('--- 2026 Q38 ---')
            print('Exp ends with:', q['explanationEn'][-150:])
            assert 'wait' not in q['explanationEn'].lower()

    # 5. Check MSQ correctOption across all 6 PYQs
    print('--- MSQ correctOption check ---')
    for y in [2021, 2022, 2023, 2024, 2025, 2026]:
        d = json.load(open(f'tests/gate/gate_ph/pyq/gate_ph_pyq_{y}.json', 'r', encoding='utf-8'))
        msqs = [q for q in d['questions'] if q['questionType'] == 'MSQ']
        non_null_co = [q['questionNumber'] for q in msqs if q['correctOption'] is not None]
        print(f'{y}: {len(msqs)} MSQs, non-null correctOption count: {len(non_null_co)}')
        assert len(non_null_co) == 0, f'{y} has non-null MSQ correctOption: {non_null_co}'

    print('ALL POLISH CHECKS VERIFIED SUCCESSFULLY!')

if __name__ == '__main__':
    verify()
