import fitz

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

for i in range(min(15, len(doc))):
    text = doc[i].get_text()
    first_lines = "\n".join([line.strip() for line in text.split("\n") if line.strip()][:10])
    print(f"--- PAGE {i+1} ---")
    print(first_lines)
    print("="*40)
