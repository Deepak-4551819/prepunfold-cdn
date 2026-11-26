import os
import re

pat = re.compile(r'tests/tgt_pgt_history')
for root, dirs, files in os.walk('tools'):
    for f in files:
        if f.endswith('.py'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                c = fl.read()
                if pat.search(c):
                    print(f"Ref in {p}")
