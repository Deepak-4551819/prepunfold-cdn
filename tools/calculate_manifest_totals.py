import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

tests = m.get('tests', [])
total_tests = len(tests)
total_questions = sum(t.get('totalQuestions', 0) for t in tests)

print(f"Calculated total tests: {total_tests}")
print(f"Calculated total questions: {total_questions}")
print(f"Manifest totalTests: {m.get('totalTests')}")
print(f"Manifest totalQuestions: {m.get('totalQuestions')}")
