#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/package_uppcs_zip.py — Packages all 14 official UPPCS PYQ papers (2018-2024) into zip archives."""
import glob
import os
import zipfile

def package_zip():
    files = sorted(glob.glob("tests/state_psc/uppcs_pre/pyq/*.json"))
    print("Files found in pyq folder:", len(files))

    archives = [
        "uppcs_pre_pyq_14_papers_full_2018_2024.zip",
        "uppcs_pre_pyq_10_papers_full.zip"
    ]

    for zip_name in archives:
        with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in files:
                arcname = os.path.relpath(f, ".")
                zf.write(f, arcname)

        size_mb = os.path.getsize(zip_name) / (1024 * 1024)
        print(f"Archive '{zip_name}' created successfully with {len(files)} files ({size_mb:.2f} MB).")

if __name__ == "__main__":
    package_zip()
