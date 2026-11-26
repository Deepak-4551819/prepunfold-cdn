# -*- coding: utf-8 -*-
import json
import zipfile
import re
from collections import Counter

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"

with zipfile.ZipFile(ZIP_PATH, "r") as z:
    for name in sorted(z.namelist()):
        if not name.endswith(".json"):
            continue
        print("\n" + "="*70)
        print("AUDITING ZIP FILE:", name)
        print("="*70)
        d = json.loads(z.read(name).decode("utf-8"))
        qs = d.get("questions", [])

        cid_hits = []
        header_hits = []
        pua_hits = []
        short_stem = []
        missing_opts = []

        for q in qs:
            qn = q.get("questionNumber")
            text = q.get("questionTextEn", "")
            exp = q.get("explanationEn", "")
            opts = q.get("optionsEn", [])
            qt = q.get("questionType")

            if "(cid:" in text or "(cid:" in exp:
                cid_hits.append((qn, text[:60]))
            if any(re.search(r'\b(carry\s+(?:one|two|1|2)\s+marks?|questions?\s+number|page\s+\d+)\b', text, re.I) for _ in [1]):
                header_hits.append((qn, text[:60]))
            if any("\uf000" <= ch <= "\uf8ff" for ch in text + exp):
                pua_hits.append(qn)
            if len(text.strip()) < 20:
                short_stem.append((qn, text))
            if qt in ("MCQ", "MSQ") and (len(opts) != 4 or any(len(o.strip()) == 0 for o in opts)):
                missing_opts.append((qn, len(opts), opts))

        print(f"Total questions: {len(qs)}")
        print(f"Cid codes (cid:xx) count: {len(cid_hits)}")
        for h in cid_hits[:5]:
            print(f"  Q{h[0]}: {ascii(h[1])}")
        print(f"Header artifacts count: {len(header_hits)}")
        for h in header_hits[:5]:
            print(f"  Q{h[0]}: {ascii(h[1])}")
        print(f"PUA Private-Use-Area glyphs: {len(pua_hits)} questions ({pua_hits[:10]})")
        print(f"Short stems (<20 chars): {len(short_stem)}")
        for h in short_stem[:5]:
            print(f"  Q{h[0]}: {ascii(h[1])}")
        print(f"Bad options (MCQ/MSQ != 4): {len(missing_opts)}")
        for h in missing_opts[:5]:
            print(f"  Q{h[0]}: count={h[1]}, opts={ascii(h[2])}")
