# -*- coding: utf-8 -*-
import os
import json
import re

replacements = [
    # ¤ -> रू or रु
    (r'¤पये', 'रुपये'),
    (r'¤प', 'रूप'),
    (r'¤ढ', 'रूढ़'),
    (r'¤सो', 'रूसो'),
    (r'¤मल', 'रूमाल'),
    (r'¤', 'रू'),

    # Ÿ combinations
    (r'डŸाूनण्ट', 'डिपोनेंट'),
    (r'डŸाूगी', 'ड्यूपी'),
    (r'डŸाूगिट', 'ड्यूपिट'),
    (r'Ÿाू', '्यू'),
    (r'Ÿा', '्य'),
    (r'Ÿ', '्य'),

    # ù combinations (hri / hrit)
    (r'“ùदय', '“हृदय'),
    (r'ùदय', 'हृदय'),
    (r'व्यपùत', 'व्यपहृत'),
    (r'अपùत', 'अपहृत'),
    (r'अधिùत', 'अधिहृत'),
    (r'व्यवùत', 'व्यवहृत'),
    (r'ùास', 'श्वास'),
    (r'आùान', 'आह्वान'),
    (r'ù', 'हृ'),

    # Ö combinations (chihna / aahwaan)
    (r'चिÖों', 'चिह्नों'),
    (r'पहचान-चिÖ', 'पहचान-चिह्न'),
    (r'चिÖक', 'चिह्नक'),
    (r'चिÖ', 'चिह्न'),
    (r'आÖान', 'आह्वान'),
    (r'Ö', 'ह्न'),

    # £ combinations
    (r'ि£यर', 'क्लियर'),
    (r'£ीयरे', 'क्लियर'),
    (r'ि£ट्बी', 'व्हाइटबी'),
    (r'£ाइटबी', 'व्हाइटबी'),
    (r'£ाइट', 'व्हाइट'),
    (r'£ीटबी', 'व्हाइटबी'),
    (r'आ£ान', 'आह्वान'),
    (r'चि£', 'चिह्न'),
    (r'£', 'क्ल'),

    # ª & ú combinations (tth / tt)
    (r'इकªा', 'इकट्ठा'),
    (r'इकªे', 'इकट्ठे'),
    (r'इकª', 'इकट्ठ'),
    (r'अªारह', 'अट्ठारह'),
    (r'अúारहवी', 'अट्ठारहवीं'),
    (r'अúारह', 'अट्ठारह'),
    (r'चिªी', 'चिट्ठी'),
    (r'मिªÒ', 'मिट्टी'),
    (r'मिúÒ', 'मिट्टी'),
    (r'विªल', 'विट्ठल'),
    (r'पट्टÒ', 'पट्टा'),
    (r'ª', 'ट्ठ'),
    (r'ú', 'ट्ट'),
    (r'Ò', 'ी'),

    # å combinations
    (r'आåवान', 'आह्वान'),
    (r'å', 'ह्व'),

    # ÿ combinations (hma / hya)
    (r'ब्रÿानन्दम', 'ब्रह्मानन्दम'),
    (r'ब्रÿा', 'ब्रह्मा'),
    (r'सुब्रÿाण्यम', 'सुब्रह्मण्यम'),
    (r'अग्राÿा', 'अग्राह्य'),
    (r'ग्राÿा', 'ग्राह्य'),
    (r'ÿा', 'ह्म'),
    (r'ÿ', 'ह्म'),

    # ñ combinations (dd)
    (r'चिन्नापरेñी', 'चिन्नापरेड्डी'),
    (r'म्हारीरेñी', 'म्हारीरेड्डी'),
    (r'नागीरेñी', 'नागीरेड्डी'),
    (r'रेñी', 'रेड्डी'),
    (r'हñी', 'हड्डी'),
    (r'अñे', 'अड्डे'),
    (r'ñ', 'ड्ड'),

    # Ü combinations
    (r'Üास', 'श्वास'),
    (r'एÜरलिच', 'एहर्लिच'),
    (r'Ü', 'श्व'),
]

def fix_text(text):
    if not text or not isinstance(text, str):
        return text
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    return text

def fix_obj(obj):
    if isinstance(obj, str):
        return fix_text(obj)
    elif isinstance(obj, list):
        return [fix_obj(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: fix_obj(v) for k, v in obj.items()}
    return obj

def main():
    base_dir = 'tests/judiciary_pyq'
    total_files = 0
    modified = 0

    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if not f.endswith('.json'):
                continue
            total_files += 1
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                content = fp.read()

            fixed = fix_text(content)
            if fixed != content:
                # parse and save formatted
                data = json.loads(fixed)
                with open(p, 'w', encoding='utf-8') as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=2)
                modified += 1

    print(f"Fixed Hindi glyphs in {modified} / {total_files} files.")

if __name__ == '__main__':
    main()
