import json, os

for path in ['scripts/history_translation_cache.json', 'scripts/cache_hi_to_en.json', 'scripts/cache_en_to_hi.json']:
    if os.path.exists(path):
        size = os.path.getsize(path)
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"{path}: {len(data)} entries ({size/1024:.1f} KB)")
        # Show 3 sample items
        sample = list(data.items())[:3]
        for k, v in sample:
            print(f"  '{k[:50]}' -> '{v[:50]}'")
