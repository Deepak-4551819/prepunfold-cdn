# -*- coding: utf-8 -*-
import os
import json
import re

chars = ['¤', 'Ÿ', 'ù', 'Ö', '£', 'ª', 'ú', 'å', 'ÿ', 'ñ', 'Ü', 'Ò']
samples = {c: set() for c in chars}

for root, dirs, files in os.walk('tests/judiciary_pyq'):
    for f in files:
        if f.endswith('.json'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            for q in d.get('questions', []):
                for k in ['questionTextHi', 'optionsHi', 'explanationHi']:
                    val = str(q.get(k, ''))
                    for c in chars:
                        if c in val:
                            words = val.split()
                            for w in words:
                                if c in w:
                                    samples[c].add(w.strip('.,;:\'\"()[]{}'))

for c in chars:
    print(f"{c} (U+{ord(c):04X}): {list(samples[c])[:8]}")
