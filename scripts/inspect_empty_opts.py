# -*- coding: utf-8 -*-
import json
import zipfile

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"

with zipfile.ZipFile(ZIP_PATH, "r") as z:
    for name in sorted(z.namelist()):
        if not name.endswith(".json"):
            continue
        d = json.loads(z.read(name).decode("utf-8"))
        for q in d.get("questions", []):
            opts = q.get("optionsEn", [])
            qt = q.get("questionType")
            if qt in ("MCQ", "MSQ") and (len(opts) != 4 or any(len(o.strip()) == 0 for o in opts)):
                print(f"[{name}] Q{q.get('questionNumber')} ({qt}, key={q.get('correctOption') or q.get('correctOptionsList')}):")
                print(f"  Stem: {ascii(q.get('questionTextEn', '')[:100])}")
                print(f"  Opts: {ascii(opts)}")
                print(f"  Exp:  {ascii(q.get('explanationEn', '')[:100])}")
