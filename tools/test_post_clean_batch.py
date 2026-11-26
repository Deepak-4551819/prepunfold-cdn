import requests, time

def translate_batch_post(batch, cache_dict):
    if not batch:
        return {}

    res = {}
    missing = []
    for item in batch:
        cleaned = " ".join(item.split()).strip()
        if not cleaned:
            res[item] = ""
        elif cleaned in cache_dict:
            res[item] = cache_dict[cleaned]
        else:
            missing.append(cleaned)

    if not missing:
        return res

    # Chunk missing into max 25 items per POST
    CHUNK_SIZE = 25
    post_url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en"

    for i in range(0, len(missing), CHUNK_SIZE):
        sub = missing[i:i + CHUNK_SIZE]
        joined = "\n".join(sub)

        success = False
        for attempt in range(3):
            try:
                r = requests.post(post_url, data={'q': joined}, headers={'User-Agent': 'Mozilla/5.0'}, timeout=8)
                if r.status_code == 200:
                    d = r.json()
                    if isinstance(d, list) and d and isinstance(d[0], str):
                        lines = d[0].split("\n")
                        if len(lines) == len(sub):
                            for src, tr in zip(sub, lines):
                                tr_c = tr.strip()
                                cache_dict[src] = tr_c
                                res[src] = tr_c
                            success = True
                            break
            except Exception:
                time.sleep(0.3)

        if not success:
            # Item-by-item fallback
            for item in sub:
                for att in range(2):
                    try:
                        r = requests.post(post_url, data={'q': item}, headers={'User-Agent': 'Mozilla/5.0'}, timeout=6)
                        if r.status_code == 200:
                            d = r.json()
                            if isinstance(d, list) and d and isinstance(d[0], str):
                                tr_c = d[0].strip()
                                cache_dict[item] = tr_c
                                res[item] = tr_c
                                break
                    except Exception:
                        time.sleep(0.2)
                if item not in res:
                    res[item] = item

    return res

# Test with 50 items
test_50 = [f"सिंधु घाटी सभ्यता प्रश्न संख्या {i} का विवरण।" for i in range(50)]
c = {}
t0 = time.time()
r = translate_batch_post(test_50, c)
print(f"Translated {len(r)} items in {time.time() - t0:.2f}s:")
print("Sample:", list(r.items())[:3])
