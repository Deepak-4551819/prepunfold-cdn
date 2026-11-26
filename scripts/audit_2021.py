# -*- coding: utf-8 -*-
import json
import re

d = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json', encoding='utf-8'))
qs = d.get('questions', [])
print(f"Total questions in 2021: {len(qs)}")
for q in qs:
    qn = q['questionNumber']
    t = q['questionTextEn']
    e = q['explanationEn']
    opts = q.get('optionsEn', [])
    qt = q['questionType']
    if 'placeholder' in t.lower() or 'placeholder' in e.lower() or 'step-by-step' in e.lower():
        print(f"Placeholder in Q{qn}: {t[:60]} | {e[:60]}")
    if qt in ('MCQ', 'MSQ') and len(opts) != 4:
        print(f"Options issue Q{qn}: {opts}")
    if any(ord(c) > 127 and c not in 'αβγδεζηθικλμνξπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΠΡΣΤΥΦΧΨΩℏ√∫∂∇±×÷≤≥≠≈∞°′″→←↑↓↔∈∉⊂⊆∪∩∧∨¬⇒⇔∑∏' for c in t):
        bad_chars = [c for c in t if ord(c) > 127 and c not in 'αβγδεζηθικλμνξπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΠΡΣΤΥΦΧΨΩℏ√∫∂∇±×÷≤≥≠≈∞°′″→←↑↓↔∈∉⊂⊆∪∩∧∨¬⇒⇔∑∏']
        if any(ord(c) >= 0x0500 for c in bad_chars):
            print(f"Special chars in Q{qn}: {bad_chars}")
