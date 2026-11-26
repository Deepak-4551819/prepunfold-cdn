import os, json

print("Searching for files referencing tests/teaching/tgt_pgt_history...")
for root, dirs, files in os.walk('.'):
    if '.git' in root or '_tmp_chunks' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.json') or f.endswith('.py') or f.endswith('.md'):
            fpath = os.path.join(root, f)
            try:
                with open(fpath, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                    if 'tests/teaching/tgt_pgt_history' in content:
                        print(f"  Found in: {fpath}")
            except Exception:
                pass
