# -*- coding: utf-8 -*-
import os
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

zip_path = r"C:\Users\yedde\Downloads\jam_cy_mocks_and_topic_tests.zip"
print(f"Inspecting zip: {zip_path}")

if not os.path.exists(zip_path):
    print("Zip file does not exist!")
    sys.exit(1)

with zipfile.ZipFile(zip_path, 'r') as z:
    names = z.namelist()
    print(f"Total entries in zip: {len(names)}")
    mocks = [n for n in names if 'mock' in n.lower() and n.endswith('.json') and 'snippet' not in n.lower()]
    topics = [n for n in names if 'topic' in n.lower() and n.endswith('.json') and 'snippet' not in n.lower()]
    snippets = [n for n in names if 'snippet' in n.lower() or 'manifest' in n.lower()]
    others = [n for n in names if n not in mocks and n not in topics and n not in snippets]

    print(f"\nMocks count: {len(mocks)}")
    for m in sorted(mocks):
        print(f"  {m} ({z.getinfo(m).file_size} bytes)")

    print(f"\nTopics count: {len(topics)}")
    for t in sorted(topics):
        print(f"  {t} ({z.getinfo(t).file_size} bytes)")

    print(f"\nSnippets / Manifest: {snippets}")
    for s in snippets:
        print(f"  {s} ({z.getinfo(s).file_size} bytes)")

    if others:
        print(f"\nOthers: {others}")
