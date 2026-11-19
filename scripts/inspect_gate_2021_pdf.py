import pypdf

reader = pypdf.PdfReader("temp_gate_pdfs/ph_2021.pdf")
print("Total pages:", len(reader.pages))

for i in range(len(reader.pages)):
    txt = reader.pages[i].extract_text() or ""
    if len(txt.strip()) > 0:
        print(f"Page {i+1} has {len(txt)} chars. Sample: {txt[:100]!r}")
