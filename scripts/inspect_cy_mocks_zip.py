# -*- coding: utf-8 -*-
import sys
import os
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_cy_mocks_and_topic_tests.zip"

print(f"Inspecting zip: {ZIP_PATH}")
with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    names = sorted(z.namelist())
    print(f"Total entries in zip: {len(names)}")
    mocks = [n for n in names if 'mock' in n.lower() and n.endswith('.json')]
    topics = [n for n in names if 'topic' in n.lower() and n.endswith('.json')]
    others = [n for n in names if n not in mocks and n not in topics]
    print(f"Mock test files: {len(mocks)}")
    for m in mocks:
        print(f"  {m} ({z.getinfo(m).file_size} bytes)")
    print(f"\nTopic test files: {len(topics)}")
    for t in topics:
        print(f"  {t} ({z.getinfo(t).file_size} bytes)")
    if others:
        print(f"\nOther files: {len(others)}")
        for o in others:
            print(f"  {o} ({z.getinfo(o).file_size} bytes)")
