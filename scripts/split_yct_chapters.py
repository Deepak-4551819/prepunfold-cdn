"""
Fast Chapter Splitter for YCT TGT/PGT History (928 Pages)
Run on Windows: python split_yct_chapters.py "HISTORY CHAPTER-WISE SOLVED PAPERS.pdf"
Requires: pip install pypdf
"""
import os, sys
from pypdf import PdfReader, PdfWriter

CHAPTERS = [
    ("ch01_prehistoric_cultures", 9, 32),
    ("ch02_indus_valley", 33, 59),
    ("ch03_vedic_period", 60, 90),
    ("ch04_jain_buddha_mahajanapada", 91, 134),
    ("ch05_mauryan_post_mauryan", 135, 182),
    ("ch06_gupta_post_gupta", 183, 212),
    ("ch07_chola_period", 213, 224),
    ("ch08_foreign_invasions", 225, 232),
    ("ch09_ancient_misc", 233, 284),
    ("ch10_delhi_sultanate", 285, 348),
    ("ch11_mughal_empire", 349, 419),
    ("ch12_bahmani_vijayanagara_maratha", 420, 449),
    ("ch13_medieval_culture_bhakti_sufi", 450, 521),
    ("ch14_medieval_society_economy", 522, 544),
    ("ch15_medieval_misc", 545, 562),
    ("ch16_east_india_company", 563, 593),
    ("ch17_modern_agriculture_trade", 594, 611),
    ("ch18_modern_education_constitution", 612, 636),
    ("ch19_revolt_1857", 637, 650),
    ("ch20_19th_century_renaissance", 651, 687),
    ("ch21_national_movement_mass", 688, 762),
    ("ch22_gandhi_tilak_gokhale_bose", 763, 780),
    ("ch23_independence_cripps_mountbatten", 781, 791),
    ("ch24_post_independence_1950", 792, 803),
    ("ch25_governors_viceroys", 804, 811),
    ("ch26_peasant_tribal_movements", 812, 818),
    ("ch27_revolutionary_movements", 819, 822),
    ("ch28_modern_misc", 823, 861),
    ("ch29_research_historiography", 862, 884),
    ("ch30_world_history", 885, 928),
]

def split_pdf(pdf_path, out_dir="yct_chapters_pdf"):
    os.makedirs(out_dir, exist_ok=True)
    reader = PdfReader(pdf_path)
    for name, start_p, end_p in CHAPTERS:
        writer = PdfWriter()
        for p in range(start_p - 1, min(end_p, len(reader.pages))):
            writer.add_page(reader.pages[p])
        out_file = os.path.join(out_dir, f"{name}_p{start_p}-{end_p}.pdf")
        with open(out_file, "wb") as f:
            writer.write(f)
        print(f"Created {out_file} ({end_p - start_p + 1} pages)")

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "HISTORY CHAPTER-WISE SOLVED PAPERS.pdf"
    split_pdf(src)
