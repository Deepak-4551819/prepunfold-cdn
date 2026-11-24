import json

with open(r'C:\Users\yedde\Downloads\ctet_all_state_tet_hindi_chapterwise.json', 'r', encoding='utf-8') as f:
    ctet = json.load(f)

ch21 = ctet['chapters'][20]
print(f"Chapter 21: {ch21.get('chapter_name')} ({len(ch21.get('questions', []))} Qs)")
for i, q in enumerate(ch21['questions'][:5]):
    print(f"Q{i+1}: {q.get('question')[:100]} | Exam: {q.get('exam')}")
