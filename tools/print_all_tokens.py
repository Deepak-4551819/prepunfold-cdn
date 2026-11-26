import json

with open('tools/all_artifact_tokens.json', 'r', encoding='utf-8') as f:
    tokens = json.load(f)

for idx, (tok, count) in enumerate(tokens):
    print(f"{idx+1:03d}: {tok!r:<25} ({count})")
