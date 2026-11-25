import json, glob, hashlib, re

seen_hashes = json.load(open('seen_question_hashes.json', encoding='utf-8'))
print("Target keys in seen_hashes (first 5):", list(seen_hashes.keys())[:5])

# Check a few files to see which hash matches
files = glob.glob('tests/**/*.json', recursive=True)
found = 0
for f in files:
    try:
        d = json.load(open(f, encoding='utf-8'))
        qs = d.get('questions', [])
        for q in qs:
            for text_field in ['questionTextEn', 'question_en', 'questionText', 'question']:
                if text_field in q:
                    t = q[text_field]
                    for candidate in [
                        t,
                        t.strip(),
                        t.strip().lower(),
                        re.sub(r'\s+', ' ', t.strip().lower()),
                        re.sub(r'[^a-zA-Z0-9]', '', t.lower())
                    ]:
                        h1 = hashlib.md5(candidate.encode('utf-8')).hexdigest()[:16]
                        if h1 in seen_hashes:
                            print(f"Match found! File: {f}, Field: {text_field}, Hash: {h1}, Val: {seen_hashes[h1]}")
                            found += 1
                            if found >= 3:
                                break
                    if found >= 3: break
            if found >= 3: break
        if found >= 3: break
    except Exception:
        pass
if found == 0:
    print("No direct MD5 match found with tested normalizations.")
