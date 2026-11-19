import urllib.request
import ssl

ctx = ssl._create_unverified_context()

years = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017]
base_urls = [
    'https://www.physicsbyfiziks.com/freedownload/previous_year_question_paper/gate/GATE%20Physics-{year}_Question%20Paper.pdf',
    'https://www.physicsbyfiziks.com/freedownload/previous_year_question_paper/gate/GATE%20{year}.pdf',
    'https://www.physicsbyfiziks.com/freedownload/previous_year_question_paper/gate/GATE%20Physics%20{year}.pdf',
    'https://www.physicsbyfiziks.com/freedownload/previous_year_question_paper/gate/gate-physics-{year}.pdf',
    'https://www.physicsbyfiziks.com/wp-content/uploads/2024/06/{year}-GATE-Physics.pdf',
    'https://www.physicsbyfiziks.com/freedownload/previous-solution/gate/{year}_Physics.pdf',
]

for y in years:
    found = False
    for b in base_urls:
        u = b.format(year=y)
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
            with urllib.request.urlopen(req, context=ctx, timeout=4) as resp:
                if resp.status == 200:
                    print(f'FOUND {y}: {u} (size: {resp.headers.get("Content-Length")})')
                    found = True
                    break
        except Exception:
            pass
    if not found:
        print(f'Not found yet for {y}')
