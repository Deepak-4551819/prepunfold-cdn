import pymupdf, os

os.makedirs('raw_pdfs/gate_cs/extracted_imgs', exist_ok=True)
doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

pages = [5, 7, 21, 27, 40, 53, 55, 57, 60, 62, 64]
for pno in pages:
    page = doc[pno-1]
    imgs = page.get_images()
    for idx, img in enumerate(imgs):
        xref = img[0]
        base_img = doc.extract_image(xref)
        if base_img['width'] > 200 and base_img['height'] > 100:
            fname = f"p{pno}_img{idx}.{base_img['ext']}"
            with open(os.path.join('raw_pdfs/gate_cs/extracted_imgs', fname), 'wb') as f:
                f.write(base_img['image'])
            print(f"Saved {fname} ({base_img['width']}x{base_img['height']})")
