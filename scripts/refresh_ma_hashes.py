# -*- coding: utf-8 -*-
import json, hashlib, re, os, sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def refresh():
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)

    # Purge gate_ma
    hashes = {k: v for k, v in hashes.items() if v.get('categoryId') != 'gate_ma'}

    added = 0
    # 5 PYQs
    for y in [2026, 2025, 2024, 2023, 2022]:
        p = f"tests/gate/gate_ma/pyq/gate_ma_pyq_{y}.json"
        with open(p, 'r', encoding='utf-8') as jf:
            d = json.load(jf)
        for q in d['questions']:
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': d['testId'],
                'categoryId': 'gate_ma',
                'topicTag': q.get('topicTag', 'Mathematics')
            }
            added += 1

    # 10 Full Mocks
    for i in range(1, 11):
        p = f"tests/gate/gate_ma/full_mocks/gate_ma_mock_{i:02d}.json"
        with open(p, 'r', encoding='utf-8') as jf:
            d = json.load(jf)
        for q in d['questions']:
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': d['testId'],
                'categoryId': 'gate_ma',
                'topicTag': q.get('topicTag', 'Mathematics')
            }
            added += 1

    # 24 Topic Tests
    topic_dir = "tests/gate/gate_ma/topic_tests"
    for root, dirs, files in os.walk(topic_dir):
        for f in sorted(files):
            if f.endswith('.json'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8') as jf:
                    d = json.load(jf)
                for q in d['questions']:
                    text = q.get('questionTextEn', '')
                    norm = re.sub(r'\s+', ' ', text.strip().lower())
                    h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
                    hashes[h] = {
                        'questionId': q['questionId'],
                        'testId': d['testId'],
                        'categoryId': 'gate_ma',
                        'topicTag': q.get('topicTag', 'Mathematics')
                    }
                    added += 1

    with open('seen_question_hashes.json', 'w', encoding='utf-8') as f:
        json.dump(hashes, f, ensure_ascii=False, indent=2)
    print(f"✓ Refreshed {added} gate_ma question hashes in seen_question_hashes.json (Total: {len(hashes)})")

if __name__ == '__main__':
    refresh()
