import json, re, hashlib, subprocess

def normalize_stem(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'\d+(\.\d+)?', '<NUM>', text)
    text = re.sub(r'[^a-z<num>\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

seen_hashes = json.load(open('seen_question_hashes.json', encoding='utf-8'))

raw_bytes = subprocess.check_output(["git", "show", "06afdf8:tests/gate_cs_pyq_2024.json"])
old_data = json.loads(raw_bytes.decode('utf-8', errors='ignore'))
for q in old_data['questions'][:3]:
    en = q['question_en']
    norm = normalize_stem(en)
    h_norm = hashlib.md5(norm.encode('utf-8')).hexdigest()[:16]
    h_raw = hashlib.md5(en.encode('utf-8')).hexdigest()[:16]
    h_sha = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
    print("Q:", q['q_number'])
    print("  norm:", norm[:60])
    print("  md5(norm):", h_norm)
    print("  md5(raw):", h_raw)
    print("  sha256(norm):", h_sha)
    print("  in seen_hashes?", h_norm in seen_hashes, h_raw in seen_hashes, h_sha in seen_hashes)
