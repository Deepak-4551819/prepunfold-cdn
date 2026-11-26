#!/usr/bin/env python3
"""
tools/split_for_agent.py
Splits 'HISTORY CHAPTER-WISE SOLVED PAPERS.pdf' (928 pages) into 5-page PDF chunks
inside '_tmp_chunks/' named 'ch{CC:02d}_p{start:03d}_{end:03d}.pdf'
according to the exact 30-chapter map.
"""

import os
import sys
from pypdf import PdfReader, PdfWriter

# Exact 30-chapter map (1-based page numbers in the PDF)
CHAPTER_MAP = [
    (1,  "part1_ancient_history", "tgt_pgt_hist_ch01_prehistoric_cultures.json", 9,   32),
    (2,  "part1_ancient_history", "tgt_pgt_hist_ch02_indus_valley.json",         33,  59),
    (3,  "part1_ancient_history", "tgt_pgt_hist_ch03_vedic_period.json",         60,  90),
    (4,  "part1_ancient_history", "tgt_pgt_hist_ch04_jain_buddha_mahajanapada.json", 91, 134),
    (5,  "part1_ancient_history", "tgt_pgt_hist_ch05_mauryan_post_mauryan.json", 135, 182),
    (6,  "part1_ancient_history", "tgt_pgt_hist_ch06_gupta_post_gupta.json",    183, 212),
    (7,  "part1_ancient_history", "tgt_pgt_hist_ch07_chola_period.json",         213, 224),
    (8,  "part1_ancient_history", "tgt_pgt_hist_ch08_foreign_invasions.json",    225, 232),
    (9,  "part1_ancient_history", "tgt_pgt_hist_ch09_ancient_misc.json",         233, 284),
    (10, "part2_medieval_history", "tgt_pgt_hist_ch10_delhi_sultanate.json",     285, 348),
    (11, "part2_medieval_history", "tgt_pgt_hist_ch11_mughal_empire.json",       349, 419),
    (12, "part2_medieval_history", "tgt_pgt_hist_ch12_bahmani_vijayanagara_maratha.json", 420, 449),
    (13, "part2_medieval_history", "tgt_pgt_hist_ch13_medieval_culture.json",    450, 521),
    (14, "part2_medieval_history", "tgt_pgt_hist_ch14_medieval_society_economy.json", 522, 544),
    (15, "part2_medieval_history", "tgt_pgt_hist_ch15_medieval_misc.json",       545, 562),
    (16, "part3_modern_history",   "tgt_pgt_hist_ch16_east_india_company.json", 563, 593),
    (17, "part3_modern_history",   "tgt_pgt_hist_ch17_modern_agriculture_trade.json", 594, 611),
    (18, "part3_modern_history",   "tgt_pgt_hist_ch18_modern_education_constitution.json", 612, 636),
    (19, "part3_modern_history",   "tgt_pgt_hist_ch19_revolt_1857.json",         637, 650),
    (20, "part3_modern_history",   "tgt_pgt_hist_ch20_19th_century_renaissance.json", 651, 687),
    (21, "part3_modern_history",   "tgt_pgt_hist_ch21_national_movement.json",   688, 762),
    (22, "part3_modern_history",   "tgt_pgt_hist_ch22_gandhi_tilak_gokhale_bose.json", 763, 780),
    (23, "part3_modern_history",   "tgt_pgt_hist_ch23_independence.json",        781, 791),
    (24, "part3_modern_history",   "tgt_pgt_hist_ch24_post_independence.json",   792, 803),
    (25, "part3_modern_history",   "tgt_pgt_hist_ch25_governors_viceroys.json",  804, 811),
    (26, "part3_modern_history",   "tgt_pgt_hist_ch26_peasant_tribal.json",      812, 818),
    (27, "part3_modern_history",   "tgt_pgt_hist_ch27_revolutionary.json",       819, 822),
    (28, "part3_modern_history",   "tgt_pgt_hist_ch28_modern_misc.json",         823, 861),
    (29, "part4_research_world",   "tgt_pgt_hist_ch29_research.json",            862, 884),
    (30, "part4_research_world",   "tgt_pgt_hist_ch30_world_history.json",       885, 928),
]

def find_pdf_file():
    candidates = [
        "HISTORY CHAPTER-WISE SOLVED PAPERS.pdf",
        os.path.join(os.path.dirname(__file__), "..", "HISTORY CHAPTER-WISE SOLVED PAPERS.pdf"),
        os.path.expanduser(r"~\Downloads\HISTORY CHAPTER-WISE SOLVED PAPERS.pdf"),
        r"C:\Users\yedde\Downloads\HISTORY CHAPTER-WISE SOLVED PAPERS.pdf",
    ]
    for p in candidates:
        norm = os.path.normpath(p)
        if os.path.isfile(norm):
            return norm
    raise FileNotFoundError("Could not locate 'HISTORY CHAPTER-WISE SOLVED PAPERS.pdf' in repo root or Downloads.")

def split_pdf_into_chunks(pdf_path, out_dir="_tmp_chunks", chunk_size=5):
    os.makedirs(out_dir, exist_ok=True)
    print(f"Reading source PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages in PDF: {total_pages}")

    total_chunks = 0
    for ch_num, part_id, json_name, start_p, end_p in CHAPTER_MAP:
        p = start_p
        ch_chunks = 0
        while p <= end_p:
            chunk_end = min(p + chunk_size - 1, end_p)
            chunk_name = f"ch{ch_num:02d}_p{p:03d}_{chunk_end:03d}.pdf"
            chunk_path = os.path.join(out_dir, chunk_name)

            writer = PdfWriter()
            for page_idx in range(p - 1, min(chunk_end, total_pages)):
                writer.add_page(reader.pages[page_idx])

            with open(chunk_path, "wb") as f_out:
                writer.write(f_out)

            ch_chunks += 1
            total_chunks += 1
            p = chunk_end + 1

        print(f"  [Ch {ch_num:02d}] pp. {start_p:03d}–{end_p:03d} -> {ch_chunks} chunks ({json_name})")

    print(f"\nAll done! Successfully generated {total_chunks} PDF chunks in '{out_dir}/'.")
    return total_chunks

if __name__ == "__main__":
    src_pdf = sys.argv[1] if len(sys.argv) > 1 else find_pdf_file()
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "_tmp_chunks"
    split_pdf_into_chunks(src_pdf, dest_dir)
