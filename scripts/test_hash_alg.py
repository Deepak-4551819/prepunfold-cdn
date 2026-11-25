import json, subprocess, hashlib, re

raw = subprocess.check_output(["git", "show", "06afdf8:tests/gate_ph_pyq_2024.json"])
d = json.loads(raw.decode('utf-8', errors='ignore'))
seen_hashes = json.load(open('seen_question_hashes.json', encoding='utf-8'))

for i, q in enumerate(d['questions'][:5]):
    text = q.get('question_en', '')
    norm = re.sub(r'\s+', ' ', text.strip().lower())
    h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
    print(f"Q{i+1}: computed={h}, in seen_hashes={h in seen_hashes}")
    if h in seen_hashes:
        print("  found:", seen_hashes[h])
