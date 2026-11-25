import fitz

doc = fitz.open("raw_pdfs/gate_cs/gate_cs_2025_q.pdf")
pages_to_check = [40, 50, 53, 55, 57, 60, 62, 64] # 1-indexed

for p in pages_to_check:
    page = doc[p - 1]
    images = page.get_images()
    print(f"Page {p} has {len(images)} images")
    for img_idx, img in enumerate(images):
        xref = img[0]
        base_img = doc.extract_image(xref)
        img_bytes = base_img["image"]
        ext = base_img["ext"]
        filename = f"scripts/img_p{p}_{img_idx}.{ext}"
        with open(filename, "wb") as f_img:
            f_img.write(img_bytes)
        print(f"  Extracted {filename} ({base_img['width']}x{base_img['height']})")
