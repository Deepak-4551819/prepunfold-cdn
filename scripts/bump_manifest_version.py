# -*- coding: utf-8 -*-
import sys
import json
from datetime import datetime, timezone

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('manifest.json', 'r', encoding='utf-8') as f:
    mf = json.load(f)

tests = mf.get('tests', [])
cats = mf.get('categories', [])

tot_tests = len(tests)
tot_questions = sum(t.get('totalQuestions', 0) for t in tests)
now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

new_version = 37

mf['manifest_version'] = new_version
mf['manifestVersion'] = new_version
mf['version'] = new_version
mf['schemaVersion'] = new_version
mf['totalTests'] = tot_tests
mf['total_tests'] = tot_tests
mf['totalQuestions'] = tot_questions
mf['updatedAt'] = now_iso
mf['lastUpdated'] = now_iso
mf['updated_at'] = now_iso

with open('manifest.json', 'w', encoding='utf-8') as f:
    json.dump(mf, f, ensure_ascii=False, indent=2)

print(f"Bumped manifest to v{new_version}: {tot_tests} tests, {tot_questions} questions, updated at {now_iso}")
