import pypdf

reader = pypdf.PdfReader('HISTORY CHAPTER-WISE SOLVED PAPERS.pdf')
print("=== PAGE 802 ===")
print(reader.pages[801].extract_text())
print("\n=== PAGE 803 ===")
print(reader.pages[802].extract_text())
