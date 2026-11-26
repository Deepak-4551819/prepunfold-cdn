import pypdf
import json

reader = pypdf.PdfReader('HISTORY CHAPTER-WISE SOLVED PAPERS.pdf')

print("--- PAGE 803 ---")
p803 = reader.pages[802].extract_text()
print(p803[:600])

print("\n--- PAGE 804 ---")
p804 = reader.pages[803].extract_text()
print(p804[:800])

print("\n--- PAGE 805 ---")
p805 = reader.pages[804].extract_text()
print(p805[:400])

# Also check Chapter 24 JSON
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch24_post_independence.json', 'r', encoding='utf-8') as f:
    ch24 = json.load(f)

print(f"\nChapter 24 total questions: {len(ch24['questions'])}")
print(f"Ch 24 last 3 questions:")
for q in ch24['questions'][-3:]:
    print(f"Q{q['questionNumber']}: {q['pyqTag']} | {q['questionTextHi'][:60]}")
