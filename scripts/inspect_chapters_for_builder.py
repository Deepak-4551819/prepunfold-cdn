import json

with open(r'C:\Users\yedde\Downloads\ctet_all_state_tet_hindi_chapterwise.json', 'r', encoding='utf-8') as f:
    ctet = json.load(f)

print("=== CTET & STATE TET CHAPTERS ===")
for ch in ctet['chapters']:
    print(f"Ch {ch['chapter_id']}: {ch['chapter_name']} ({len(ch['questions'])} Qs)")

with open(r'C:\Users\yedde\Downloads\emrs_special_general_hindi_chapterwise.json', 'r', encoding='utf-8') as f:
    emrs = json.load(f)

print("\n=== EMRS GENERAL HINDI CHAPTERS ===")
for ch in emrs['chapters']:
    print(f"Ch {ch['chapter_id']}: {ch['chapter_name']} ({len(ch['questions'])} Qs)")
