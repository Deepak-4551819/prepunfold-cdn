import urllib.request

urls = [
    "https://purge.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/manifest.json",
    "https://purge.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/teaching/ctet_state_tet_hindi/ctet_tet_hindi_ch01_varnamala.json",
    "https://purge.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/teaching/emrs_general_hindi/emrs_hindi_ch01_varnamala.json"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"Purged [{resp.status}]: {u}")
    except Exception as e:
        print(f"Error purging {u}: {e}")
