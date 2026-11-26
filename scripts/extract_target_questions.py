import pdfplumber
import re

print("=== Extracting from gate_ph_2026.pdf ===")
with pdfplumber.open("temp_gate_pdfs/gate_ph_2026.pdf") as pdf:
    full_text = "\n---PAGE---\n".join([page.extract_text() or "" for page in pdf.pages])

    # Let's search for Q.17, Q.18, Q.45, Q.46, Q.2
    with open("temp_gate_pdfs/gate_ph_2026_extracted.txt", "w", encoding="utf-8") as out:
        out.write(full_text)

print("Saved 2026 extracted text.")

print("=== Extracting from gate_ph_2025.pdf ===")
with pdfplumber.open("temp_gate_pdfs/gate_ph_2025.pdf") as pdf:
    full_text = "\n---PAGE---\n".join([page.extract_text() or "" for page in pdf.pages])

    with open("temp_gate_pdfs/gate_ph_2025_extracted.txt", "w", encoding="utf-8") as out:
        out.write(full_text)

print("Saved 2025 extracted text.")
