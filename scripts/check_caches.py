import os, json
for f in ['scripts/cache_en_to_hi.json', 'scripts/cache_hi_to_en.json']:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            print(f, 'size:', len(d))
    else:
        print(f, 'does not exist yet')
