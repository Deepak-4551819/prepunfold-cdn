import pymupdf

doc = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

for pno in [5, 7, 9, 21, 27, 40, 53, 55, 57, 60, 62, 64]:
    page = doc[pno-1]
    imgs = page.get_images()
    print(f"Page {pno}: {len(imgs)} images")
    for img_idx, img in enumerate(imgs):
        xref = img[0]
        base_img = doc.extract_image(xref)
        print(f"  img {img_idx}: format={base_img['ext']}, size={base_img['width']}x{base_img['height']}, bytes={len(base_img['image'])}")
