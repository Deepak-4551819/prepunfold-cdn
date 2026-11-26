# -*- coding: utf-8 -*-
import json, hashlib, re

def refresh():
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)

    hashes = {k: v for k, v in hashes.items() if v.get('categoryId') != 'gate_ph'}

    test_files = []
    for y in [2026, 2025, 2024, 2023, 2022, 2021]:
        test_files.append(f'tests/gate/gate_ph/pyq/gate_ph_pyq_{y}.json')
    for i in range(1, 11):
        test_files.append(f'tests/gate/gate_ph/full_mocks/gate_ph_mock_{i:02d}.json')
    parts = ['part_01_ga', 'part_02_mp', 'part_03_cm', 'part_04_emt', 'part_05_qm', 'part_06_tsp', 'part_07_amp', 'part_08_ssp', 'part_09_elec', 'part_10_npp']
    sub_prefixes = ['ga', 'mp', 'cm', 'emt', 'qm', 'tsp', 'amp', 'ssp', 'elec', 'npp']
    for part, pref in zip(parts, sub_prefixes):
        for set_num in [1, 2]:
            test_files.append(f'tests/gate/gate_ph/topic_tests/{part}/gate_ph_topic_{pref}_{set_num:02d}.json')

    added = 0
    for fp in test_files:
        with open(fp, 'r', encoding='utf-8') as jf:
            d = json.load(jf)
        for q in d.get('questions', []):
            text = q.get('questionTextEn') or ''
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': d['testId'],
                'categoryId': d['categoryId'],
                'topicTag': q.get('topicTag', '')
            }
            added += 1

    with open('seen_question_hashes.json', 'w', encoding='utf-8') as f:
        json.dump(hashes, f, ensure_ascii=False, indent=2)
    print(f'Refreshed {added} gate_ph question hashes! Total: {len(hashes)}')

if __name__ == '__main__':
    refresh()
