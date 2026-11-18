# -*- coding: utf-8 -*-
import re

def decode_aps(text):
    if not text:
        return ""

    s = text

    # Normalize punctuation and quotes
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = s.replace("~", "।").replace("0", "०")

    # 1. Reposition 'ef' (short-i) at ASCII level FIRST
    i_targets = [
        "mLe", "mle", "mhe", "mye", "mve", "mkeâ", "mHe", "mOe", "mle=â",
        "›eâ", "òe", "É", "Ü", "Í", "Î", "Ï", "Õe", "Øe",
        "keâer", "keâe", "keâ", "Ke", "ie", "Ie", "³e",
        "Ûe", "Ú", "pe", "Pe", "×e",
        "še", '"e', "[e", "{e", "Ce",
        "le", "Le", "oe", "Oe", "ve",
        "he", "He", "ye", "Ye", "ce",
        "Ùe", "j", "ue", "Je",
        "Me", "<e", "me", "ne",
        "#e", "$e", "%e", "ße",
    ]
    for target in i_targets:
        s = s.replace("ef" + target, target + "ि")

    # 2. Reposition '&' (reph) at ASCII level
    reph_targets = [
        "mLe", "›eâ", "òe", "É", "Ü", "Í", "Î", "Ï", "Õe", "Øe",
        "keâer", "keâe", "keâ", "Ke", "ie", "Ie", "³e",
        "Ûe", "Ú", "pe", "Pe", "×e",
        "še", '"e', "[e", "{e", "Ce",
        "leer", "lee", "le", "Leer", "Lee", "Le", "oe", "Oe", "ve",
        "he", "He", "ye", "Ye", "ceer", "cee", "ce",
        "Ùe", "j", "ue", "Jeer", "Jee", "Je",
        "Me", "<e", "me", "ne",
        "#e", "$e", "%e", "ße",
        "š", '"', "[", "{",
    ]
    for target in reph_targets:
        s = s.replace(target + "&", "र्" + target)

    # Specific pre-substitutions
    pre_subs = [
        ("òee", "त्ता"), ("òe", "त्त"), ("ò", "त्त्"),
        ("Éee", "द्वा"), ("Ée", "द्वा"), ("É", "द्व"),
        ("Üee", "द्धा"), ("Üe", "द्ध"), ("Ü", "द्ध"),
        ("Íee", "द्या"), ("Íe", "द्या"), ("Í", "द्य"),
        ("Îee", "द्मा"), ("Îe", "द्म"), ("Î", "द्म"),
        ("Ïee", "द्रा"), ("Ïe", "द्र"), ("Ï", "द्र"),
        ("Õee", "श्वा"), ("Õe", "श्व"), ("Õ", "श्व्"),
        ("Øee", "प्रा"), ("Øe", "प्र"), ("Ø", "प्र"),
        ("óee", "ट्टा"), ("óe", "ट्टा"), ("ó", "ट्ट"),
        ("keä", "क्य"),
        ("k=â", "कृ"), ("i=â", "गृ"), ("le=â", "तृ"), ("=â", "्र"),
        ("šô", "ट्र"), ("[ô", "ड्र"), ("{ô", "ढ्र"),
        ("mLe", "स्थ"), ("mle", "स्त"),
        ("nQ", "हैं"), ("nw", "है"),
        ("keâ@e", "कॉ"), ("he@e", "पॉ"), ("še@e", "टॉ"), ("še@", "टॉ"),
        ("kesâ", "के"), ("kewâ", "कै"), ("keâes", "को"), ("keâew", "कौ"),
        ("keâer", "की"), ("keâW", "कें"), ("keât", "कू"), ("keâg", "कु"),
        ("keâe", "का"), ("keâ", "क"),
    ]
    for k, v in pre_subs:
        s = s.replace(k, v)

    # Vowels
    vowels = [
        ("Deew", "औ"), ("Dees", "ओ"), ("Dee", "आ"), ("De", "अ"),
        ("F&", "ई"), ("F", "इ"),
        ("Gâ", "ऊ"), ("G", "उ"),
        ("Sâ", "ऐ"), ("S", "ए"),
        ("*e", "ऋ"),
    ]
    for k, v in vowels:
        s = s.replace(k, v)

    # Consonants with matras
    cons_map = [
        ("Ke", "ख"), ("ie", "ग"), ("Ie", "घ"), ("³e", "ङ"),
        ("Ûe", "च"), ("Ú", "छ"), ("pe", "ज"), ("Pe", "झ"), ("×e", "ञ"),
        ("še", "ट"), ('"e', "ठ"), ("[e", "ड"), ("{e", "ढ"), ("Ce", "ण"),
        ("le", "त"), ("Le", "थ"), ("oe", "द"), ("Oe", "ध"), ("ve", "न"),
        ("he", "प"), ("He", "फ"), ("ye", "ब"), ("Ye", "भ"), ("ce", "म"),
        ("Ùe", "य"), ("ue", "ल"), ("Je", "व"),
        ("Me", "श"), ("<e", "ष"), ("me", "स"), ("ne", "ह"),
        ("#e", "क्ष"), ("$e", "त्र"), ("%e", "ज्ञ"), ("ße", "श्र"),
        ("{", "ढ"), ('"', "ठ"), ("[", "ड"), ("j", "र"),
    ]
    for c_raw, c_uni in cons_map:
        s = s.replace(c_raw + "es", c_uni + "ो")
        s = s.replace(c_raw + "ew", c_uni + "ौ")
        s = s.replace(c_raw + "er", c_uni + "ी")
        s = s.replace(c_raw + "ee", c_uni + "ी")
        s = s.replace(c_raw + "s", c_uni + "े")
        s = s.replace(c_raw + "w", c_uni + "ै")
        s = s.replace(c_raw + "W", c_uni + "ें")
        s = s.replace(c_raw + "t", c_uni + "ू")
        s = s.replace(c_raw + "g", c_uni + "ु")
        s = s.replace(c_raw + "b", c_uni + "ं")
        s = s.replace(c_raw + "B", c_uni + "ँ")
        s = s.replace(c_raw + "=", c_uni + "ृ")
        s = s.replace(c_raw + "e", c_uni + "ा")
        s = s.replace(c_raw, c_uni)

    # Half consonants
    half_map = [
        ("k", "क्"), ("K", "ख्"), ("i", "ग्"), ("I", "घ्"),
        ("Û", "च्"), ("Ú", "छ्"), ("p", "ज्"), ("P", "झ्"),
        ("š", "ट्"), ("C", "ण्"),
        ("l", "त्"), ("L", "थ्"), ("o", "द्"), ("O", "ध्"), ("v", "न्"),
        ("h", "प्"), ("H", "फ्"), ("y", "ब्"), ("Y", "भ्"), ("c", "म्"),
        ("u", "ल्"), ("J", "व्"), ("M", "श्"), ("<", "ष्"), ("m", "स्"),
        ("n", "ह्"), ("#", "क्ष्"), ("$", "त्र्"), ("%", "ज्ञ्"), ("ß", "श्र्"),
    ]
    for k, v in half_map:
        s = s.replace(k, v)

    # Standalone matras
    matras = [
        ("es", "ो"), ("ew", "ौ"), ("ee", "ा"), ("er", "ी"),
        ("W", "ें"), ("w", "ै"), ("s", "े"), ("b", "ं"), ("B", "ँ"),
        ("t", "ू"), ("g", "ु"), ("=", "ृ"),
    ]
    for k, v in matras:
        s = s.replace(k, v)

    # Clean up
    s = s.replace("&", "").replace("â", "").replace("e", "")

    return s

def decode_line(line):
    ls = line.strip()
    if not ls:
        return ""
    if ls.startswith("TGT/PGT") or ls.startswith("UP PGT") or ls.startswith("UP TGT") or ls.startswith("NTA UGC") or ls.startswith("RPSC") or ls.startswith("KVS") or ls.startswith("NVS") or ls.startswith("DSSSB") or ls.startswith("GIC") or ls.startswith("GDC") or ls in ("YCT", "Ans."):
        return line
    if re.match(r'^(Ans\.\s*\([a-eA-E]\)\s*[:\.]?)(.*)$', ls):
        m = re.match(r'^(Ans\.\s*\([a-eA-E]\)\s*[:\.]?)(.*)$', ls)
        return m.group(1) + " " + decode_aps(m.group(2))
    if re.match(r'^(\([a-eA-E]\)\s*)(.*)$', ls):
        m = re.match(r'^(\([a-eA-E]\)\s*)(.*)$', ls)
        return m.group(1) + decode_aps(m.group(2))
    if re.match(r'^(\d+\.\s*)(.*)$', ls):
        m = re.match(r'^(\d+\.\s*)(.*)$', ls)
        return m.group(1) + decode_aps(m.group(2))
    return decode_aps(line)
