# -*- coding: utf-8 -*-
import re

def convert_aps_to_unicode(text):
    if not text:
        return ""

    s = text

    # 0. Normalize quotes and symbols
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')

    # 1. Handle reph / rakar
    # In APS, 'ef' is short-i, typed before consonant
    # We will do a multi-stage replacement

    # Pre-substitutions for complex glyphs
    complex_map = [
        ("òee", "त्ता"), ("òe", "त्त"), ("ò", "त्त्"),
        ("Ée", "द्वा"), ("É", "द्व"),
        ("Üe", "द्धा"), ("Ü", "द्ध"),
        ("Íe", "द्या"), ("Í", "द्य"),
        ("Îe", "द्मा"), ("Î", "द्म"),
        ("Ïe", "द्रा"), ("Ï", "द्र"),
        ("Õe", "श्व"), ("Õ", "श्व्"),
        ("Øe", "प्र"), ("Ø", "प्र"),
        ("keä", "क्य"),
        ("=â", "्र"), ("k=â", "क्र"), ("i=â", "ग्र"), ("le=â", "त्र"),
        ("šô", "ट्र"), ("[ô", "ड्र"), ("{ô", "ढ्र"),
    ]
    for k, v in complex_map:
        s = s.replace(k, v)

    # Vowels
    vowels = [
        ("Dee", "आ"), ("Dees", "ओ"), ("Deew", "औ"), ("De", "अ"),
        ("F&", "ई"), ("F", "इ"), ("Gâ", "ऊ"), ("G", "उ"),
        ("Sâ", "ऐ"), ("S", "ए"), ("*e", "ऋ"),
    ]
    for k, v in vowels:
        s = s.replace(k, v)

    # Consonants with inherent 'a'
    consonants_full = [
        ("keâ", "क"), ("Ke", "ख"), ("ie", "ग"), ("Ie", "घ"), ("³e", "ङ"),
        ("Ûe", "च"), ("Ú", "छ"), ("pe", "ज"), ("Pe", "झ"), ("×e", "ञ"),
        ("še", "ट"), ('"e', "ठ"), ("[e", "ड"), ("{e", "ढ"), ("Ce", "ण"),
        ("le", "त"), ("Le", "थ"), ("oe", "द"), ("Oe", "ध"), ("ve", "न"),
        ("he", "प"), ("He", "फ"), ("ye", "ब"), ("Ye", "भ"), ("ce", "म"),
        ("Ùe", "य"), ("j", "र"), ("ue", "ल"), ("Je", "व"),
        ("Me", "श"), ("<e", "ष"), ("me", "स"), ("ne", "ह"),
        ("#e", "क्ष"), ("$e", "त्र"), ("%e", "ज्ञ"), ("ße", "श्र"),
    ]
    for k, v in consonants_full:
        s = s.replace(k, v)

    # Half consonants
    consonants_half = [
        ("k", "क्"), ("K", "ख्"), ("i", "ग्"), ("I", "घ्"),
        ("Û", "च्"), ("p", "ज्"), ("P", "झ्"),
        ("l", "त्"), ("L", "थ्"), ("o", "द्"), ("O", "ध्"), ("v", "न्"),
        ("h", "प्"), ("H", "फ्"), ("y", "ब्"), ("Y", "भ्"), ("c", "म्"),
        ("u", "ल्"), ("J", "व्"), ("M", "श्"), ("<", "ष्"), ("m", "स्"),
        ("n", "ह्"), ("#", "क्ष्"), ("$", "त्र्"), ("%", "ज्ञ्"), ("ß", "श्र्"),
    ]
    for k, v in consonants_half:
        s = s.replace(k, v)

    # Matras and signs
    matras = [
        ("ee", "ा"), ("er", "ी"), ("g", "ु"), ("t", "ू"),
        ("s", "े"), ("w", "ै"), ("es", "ो"), ("ew", "ौ"),
        ("W", "ें"), ("b", "ं"), ("B", "ँ"), ("~", "।"),
        ("=", "ृ"), ("@", "ॅ"), ("^", "्र"), ("ô", "्र"),
        (":", ":"), ("&", "ी"),
    ]
    for k, v in matras:
        s = s.replace(k, v)

    # Now handle short-i ('ef' or 'e')
    # In APS, 'ef' stands for short-i preceding a consonant/conjunct
    # Let's fix occurrences like 'efक' -> 'कि', 'efग्' -> 'गि', etc.
    # Pattern: 'ef' followed by [optional half-consonants] + [full consonant]
    # In unicode: consonant + 'ि'
    def replace_short_i(match):
        cons = match.group(1)
        return cons + "ि"

    # Regex: ef followed by (consonant sequence)
    # Devanagari consonants: [क-ह](्[क-ह])*
    s = re.sub(r'ef([क-ह](?:्[क-ह])*)', replace_short_i, s)
    s = re.sub(r'e([क-ह](?:्[क-ह])*)', replace_short_i, s)

    # Fix nukta and danda
    s = s.replace("0", "०").replace("~", "।")

    return s

# Test on page 9 sample text
sample = """Gòejer Decesefjkeâe ceW ØeLece JeemleefJekeâ Yet-Deeke=âefle efJe%eeve Jesòee efkeâmes keâne peelee nw?
(a) peer.kesâ. efieuyeš&
(b) pes. [yuÙet. he@eJesue
(c) [yuÙet. Sce. [sefJeme
(d) meer.F&. [šve
UP PGT 2021
Ans. (a) : Gòejer Decesefjkeâe ceW ØeLece Yet-Deeke=âefle efJe%eeveJesòee peer.kesâ. efieuyeš& keâes ceevee peelee nw~"""

converted = convert_aps_to_unicode(sample)
print("--- CONVERTED OUTPUT ---")
print(converted)
