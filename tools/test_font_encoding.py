import pypdf
try:
    import fitz # PyMuPDF
    print("fitz is available!")
except ImportError:
    fitz = None
    print("fitz is NOT available")

# Check page 804 in PDF using fitz if available
if fitz:
    doc = fitz.open('HISTORY CHAPTER-WISE SOLVED PAPERS.pdf')
    page = doc[803]
    text = page.get_text()
    print("=== PyMuPDF get_text() on p. 804 ===")
    print(text[:1000])
