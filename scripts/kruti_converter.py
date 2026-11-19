# -*- coding: utf-8 -*-
import re

def kruti_to_unicode(text):
    if not text:
        return ""

    s = text

    # 1. Multi-character glyphs and conjuncts
    subs_1 = [
        ("òe", "त्त"), ("ò", "त्त्"), ("=â", "्र"), ("^", "्र"),
        ("Øe", "प्र"), ("Ø", "प्र"), ("Ùe", "य"), ("Ù", "य्"),
        ("keä", "क्य"), ("keâ", "क"), ("Ke", "ख"), ("ie", "ग"), ("Ie", "घ"), ("³e", "ङ"),
        ("Ûe", "च"), ("Ú", "छ"), ("pe", "ज"), ("Pe", "झ"), ("×e", "ञ"),
        ("še", "ट"), ('"e', "ठ"), ("[e", "ड"), ("{e", "ढ"), ("Ce", "ण"),
        ("le", "त"), ("Le", "थ"), ("oe", "द"), ("Oe", "ध"), ("ve", "न"),
        ("he", "प"), ("He", "फ"), ("ye", "ब"), ("Ye", "भ"), ("ce", "म"),
        ("Je", "व"), ("Me", "श"), ("<e", "ष"), ("me", "स"), ("ne", "ह"),
        ("#e", "क्ष"), ("$e", "त्र"), ("%e", "ज्ञ"), ("ße", "श्र"),

        # Vowels
        ("Dee", "आ"), ("Dees", "ओ"), ("Deew", "औ"), ("De", "अ"),
        ("F&", "ई"), ("F", "इ"), ("Gâ", "ऊ"), ("G", "उ"),
        ("Sâ", "ऐ"), ("S", "ए"), ("*e", "ऋ"),

        # Half letters
        ("k", "क्"), ("K", "ख्"), ("i", "ग्"), ("I", "घ्"),
        ("Û", "च्"), ("Ú", "छ्"), ("p", "ज्"), ("P", "झ्"),
        ("l", "त्"), ("L", "थ्"), ("o", "द्"), ("O", "ध्"), ("v", "न्"),
        ("h", "प्"), ("H", "फ्"), ("y", "ब्"), ("Y", "भ्"), ("c", "म्"),
        ("u", "ल्"), ("J", "व्"), ("M", "श्"), ("<", "ष्"), ("m", "स्"),
        ("n", "ह्"), ("#", "क्ष्"), ("$", "त्र्"), ("%", "ज्ञ्"), ("ß", "श्र्"),

        # Special consonants
        ("j", "र"), ("ue", "ल"),

        # Matras
        ("eâ", "ा"), ("ee", "ा"), ("er", "ी"), ("g", "ु"), ("t", "ू"),
        ("s", "े"), ("w", "ै"), ("es", "ो"), ("ew", "ौ"),
        ("b", "ं"), ("B", "ँ"), ("~", "।"), ("&", "ी"), ("@", "ॅ"),
        ("=", "ृ"), (":", ":"),
    ]

    # 2. In KrutiDev, short-i ('e') precedes the consonant.
    # We first fix 'e' repositioning:
    # Pattern: 'e' followed by half-consonant(s) and full consonant
    # Example: 'efJe' -> 'व' + 'ि' = 'वि', 'efve' -> 'नि', 'efie' -> 'गि'
    def fix_short_i(txt):
        # In Kruti, 'e' is followed by a consonant or conjunct
        # Let's handle 'e' + single or multi-char consonant before substitutions or after?
        # If we do it at Kruti character level:
        # 'e' + (consonant) -> consonant + 'ि'
        # In Kruti:
        # e + [consonant token]
        pass

    # Let's use the well-established JavaScript/Python Kruti-to-Unicode mapping
    return s
