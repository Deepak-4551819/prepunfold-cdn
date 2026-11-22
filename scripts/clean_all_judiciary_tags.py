# -*- coding: utf-8 -*-
import os
import json
import re

exam_chunk_pattern = re.compile(
    r'((?:\d+(?:st|nd|rd|th)\s+)?(?:UP|MP|MPHC|BPSC|UK|Uttarakhand|Uttaranchal|Rajasthan|Haryana|Delhi|DJS|Jharkhand|JS|Chhattisgarh|Chhattishgarh|CG|Bihar|Himachal|HP|Odisha|OPSC|West\s+Bengal|WB|Punjab|HJS|CJ|PCS|APO|ADPO|UGC(?:\s*\(?NET\)?)?|UPHESC|Civil\s+Judge|JLS|APP|CBI|CLAT)[A-Za-z0-9\s\(\)\-\,\.\/]*?\b(?:19\d\d|20\d\d)\b(?:\s*(?:Paper-I{1,3}|Part-I{1,3}|Paper\s*\d+|Part\s*\d+))?)',
    re.IGNORECASE
)

def clean_tag_val(v):
    if not v or not isinstance(v, str):
        return None

    # Check if string contains high-ascii font artifacts or corrupt keywords
    akruti_found = any(ord(c) > 127 and not (0x0900 <= ord(c) <= 0x097F) for c in v)
    is_corrupt = akruti_found or 'prepared/' in v or 'JÙeeKÙee' in v or 'efveCe' in v or 'ceW' in v or 'kesâ' in v

    if is_corrupt:
        matches = [m.group(1).strip() for m in exam_chunk_pattern.finditer(v)]
        if matches:
            unique = list(dict.fromkeys(matches))
            return ' | '.join(unique)
        else:
            return None
    return v

def main():
    base_dir = 'tests/judiciary_pyq'
    total_tags_cleaned = 0
    files_modified = 0

    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if not f.endswith('.json'):
                continue
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                data = json.load(fp)

            file_changed = False
            for q in data.get('questions', []):
                for k in ['pyqTag', 'exam_year_tag', 'tags']:
                    if k in q:
                        old_v = q[k]
                        new_v = clean_tag_val(old_v)
                        if old_v != new_v:
                            q[k] = new_v
                            file_changed = True
                            total_tags_cleaned += 1

            if file_changed:
                with open(path, 'w', encoding='utf-8') as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=2)
                files_modified += 1

    print(f"Done! Cleaned {total_tags_cleaned} tags across {files_modified} files.")

if __name__ == '__main__':
    main()
