import json

with open('tests/teaching/tgt_pgt_economics/topic_tests/tgt_pgt_econ_ch01_definition_and_nature.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Test metadata keys:", [k for k in d.keys() if k != 'questions'])
print("Total questions:", len(d.get('questions', [])))
if d.get('questions'):
    print("Q[0] keys:", list(d['questions'][0].keys()))
    print("Q[0]:", json.dumps(d['questions'][0], ensure_ascii=False, indent=2))
