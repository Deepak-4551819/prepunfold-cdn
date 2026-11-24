import json

with open('tests/judiciary_pyq/cpc/cpc_pyq_t01_preliminary.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Test metadata keys:", [k for k in d.keys() if k != 'questions'])
print("Total questions:", len(d.get('questions', [])))
if d.get('questions'):
    print("Q[0]:", json.dumps(d['questions'][0], ensure_ascii=False, indent=2))
