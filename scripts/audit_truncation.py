import glob
import json
import os

judiciary_dir = "tests/judiciary_pyq"
subdirs = sorted([d for d in os.listdir(judiciary_dir) if os.path.isdir(os.path.join(judiciary_dir, d))])

for sub in subdirs:
    sub_path = os.path.join(judiciary_dir, sub)
    json_files = sorted(glob.glob(os.path.join(sub_path, "*.json")))
    short_stems = 0
    total_q = 0
    sample_short = []

    for f in json_files:
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
        for q in data.get("questions", []):
            total_q += 1
            en = q.get("questionTextEn", "").strip()
            # check if short or ends with prepositions/articles
            words = en.split()
            if len(words) < 7 or en.endswith((" the", " of", " in", " on", " to", " with", " had", " a", " an", " by", " under", " at", " for")):
                short_stems += 1
                if len(sample_short) < 3:
                    sample_short.append((q.get("id"), en))

    print(f"[{sub:<18}] Total Qs: {total_q:>5} | Short/Truncated Stems: {short_stems:>4} ({short_stems/total_q*100:.1f}%)")
    for qid, s in sample_short:
        print(f"    {qid}: {s}")
