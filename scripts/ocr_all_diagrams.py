from rapidocr_onnxruntime import RapidOCR
import glob

ocr = RapidOCR()
files = sorted(glob.glob("scripts/img_p*_2.*"))
with open("scripts/ocr_diagrams_results.txt", "w", encoding="utf-8") as out:
    for f in files:
        result, _ = ocr(f)
        out.write(f"=== {f} ===\n")
        if result:
            for line in result:
                out.write(f"  {line[1]}\n")
        else:
            out.write("  (no text detected)\n")
        out.write("\n")
print("OCR completed for all diagram images!")
