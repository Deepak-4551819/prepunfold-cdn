import urllib.request
import json

raw_url = "https://raw.githubusercontent.com/Deepak-4551819/prepunfold-cdn/main/manifest.json"
print("Checking Raw GitHub manifest...")
try:
    with urllib.request.urlopen(urllib.request.Request(raw_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        m = json.loads(resp.read().decode('utf-8'))
        print(f"  Version: {m.get('manifest_version')}")
        print(f"  Categories: {len(m.get('categories', []))}")
        print(f"  Tests: {len(m.get('tests', []))}")
        print(f"  Questions: {m.get('totalQuestions')}")

        cat_ids = [c['id'] for c in m.get('categories', [])]
        print(f"  'ctet_state_tet_hindi' in categories: {'ctet_state_tet_hindi' in cat_ids}")
        print(f"  'emrs_general_hindi' in categories: {'emrs_general_hindi' in cat_ids}")
except Exception as e:
    print("Error fetching raw:", e)

test_url = "https://raw.githubusercontent.com/Deepak-4551819/prepunfold-cdn/main/tests/teaching/ctet_state_tet_hindi/ctet_tet_hindi_ch01_varnamala.json"
print("\nChecking test paper on Raw GitHub...")
try:
    with urllib.request.urlopen(urllib.request.Request(test_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        t = json.loads(resp.read().decode('utf-8'))
        print(f"  Title: {t.get('title')}")
        print(f"  Questions: {len(t.get('questions', []))}")
        q1 = t['questions'][0]
        print(f"  Q1: {q1.get('questionTextHi')}")
        print(f"  Options: {q1.get('optionsHi')}")
        print(f"  Ans: {q1.get('correctOption')}")
        print(f"  Exam: {q1.get('pyqTag')}")
except Exception as e:
    print("Error fetching test:", e)
