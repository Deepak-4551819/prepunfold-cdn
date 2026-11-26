import pypdf

reader = pypdf.PdfReader('HISTORY CHAPTER-WISE SOLVED PAPERS.pdf')
p804 = reader.pages[803].extract_text()
print(p804)
