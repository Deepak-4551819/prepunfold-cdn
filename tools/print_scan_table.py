from scan_corrupted_questions import scan_all_30_chapters

results = scan_all_30_chapters()
for idx, r in enumerate(results, 1):
    print(f"{idx:02d}: {r['file']} -> Total: {r['total']}, Clean: {r['clean']}, Flagged: {r['flagged']}")
