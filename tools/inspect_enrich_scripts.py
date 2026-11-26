for path in ['scripts/polity_translator.py', 'scripts/enrich_teaching_bilingual.py', 'scripts/enrich_history_hindi.py']:
    print(f"=== {path} (first 40 lines) ===")
    with open(path, 'r', encoding='utf-8') as f:
        lines = [f.readline() for _ in range(40)]
        print("".join(lines))
