# -*- coding: utf-8 -*-
import json
import re

d21 = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json', encoding='utf-8'))
qs21 = d21.get('questions', [])

# Check other PYQs
for yr in [2022, 2023, 2024]:
    dyr = json.load(open(f'tests/gate/gate_ph/pyq/gate_ph_pyq_{yr}.json', encoding='utf-8'))
    qs_yr = dyr.get('questions', [])
    t21 = set(q['questionTextEn'].strip().lower() for q in qs21)
    tyr = set(q['questionTextEn'].strip().lower() for q in qs_yr)
    overlap = t21.intersection(tyr)
    print(f"2021 vs {yr} overlap: {len(overlap)}")

# Check if 2021 has duplicate questions with topic_tests or full_mocks
for f in ['tests/gate/gate_ph/full_mocks/gate_ph_mock_01.json']:
    dm = json.load(open(f, encoding='utf-8'))
    tm = set(q['questionTextEn'].strip().lower() for q in dm['questions'])
    overlap = t21.intersection(tm)
    print(f"2021 vs Mock 01 overlap: {len(overlap)}")
    if overlap:
        for x in list(overlap)[:3]:
            print("  Overlap:", x[:80])
