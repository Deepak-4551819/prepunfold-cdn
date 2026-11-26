# -*- coding: utf-8 -*-
import json, re

for y in [2025, 2026]:
    d = json.load(open(f"tests/gate/gate_ph/pyq/gate_ph_pyq_{y}.json", encoding="utf-8"))
    print(f"\n=== {y} Special Unicode / Garbled Math Check ===")
    non_ascii = set()
    for q in d["questions"]:
        s = (q.get("questionTextEn") or "") + " " + " ".join(q.get("optionsEn") or [])
        for ch in s:
            if ord(ch) > 127:
                non_ascii.add((ch, hex(ord(ch))))
    print(f"Non-ASCII chars in {y} ({len(non_ascii)}):", sorted(list(non_ascii), key=lambda x: x[1])[:40])
