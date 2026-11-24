import json

for path in [r'C:\Users\yedde\Downloads\ctet_all_state_tet_hindi_chapterwise.json', r'C:\Users\yedde\Downloads\emrs_special_general_hindi_chapterwise.json']:
    print("=" * 60)
    print("FILE:", path)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("Title:", data.get('title'))
    print("Total chapters:", len(data.get('chapters', [])))
    print("Total questions field:", data.get('total_questions'))

    # check first 3 questions of chapter 1
    ch1 = data['chapters'][0]
    print(f"Chapter 1: {ch1.get('chapter_name')} ({len(ch1.get('questions', []))} qs)")
    for i, q in enumerate(ch1['questions'][:3]):
        print(f"--- Q{i+1} ---")
        print("Keys:", list(q.keys()))
        print("question:", repr(q.get('question')))
        print("options:", q.get('options'))
        print("answer:", repr(q.get('answer')))
        print("explanation:", repr(q.get('explanation')[:150] if q.get('explanation') else None))
        print("exam:", repr(q.get('exam')))
        print("page:", q.get('page'))
