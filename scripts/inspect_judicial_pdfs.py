import os
import pymupdf

DIR_PATH = r"C:\Users\yedde\Downloads\Judicial"
files = sorted([f for f in os.listdir(DIR_PATH) if f.endswith('.pdf')])

print(f"Found {len(files)} PDFs in {DIR_PATH}:")
for f in files:
    fpath = os.path.join(DIR_PATH, f)
    try:
        doc = pymupdf.open(fpath)
        print(f"\n{'='*60}")
        print(f"File: {f} | Pages: {len(doc)} | Size: {os.path.getsize(fpath)/(1024*1024):.1f} MB")

        # Sample text from first few pages
        sample_pages = min(5, len(doc))
        for p in range(sample_pages):
            text = doc[p].get_text()
            first_lines = [line.strip() for line in text.split('\n') if line.strip()][:5]
            print(f"  Page {p+1}: {first_lines}")
    except Exception as e:
        print(f"Error reading {f}: {e}")
