# -*- coding: utf-8 -*-
import re

# Comprehensive Akruti / Devlys layout to Unicode Devanagari converter
# In Akruti, 'ef' is pre-base chhoti-i (ि)
# 'eâ' = क
# 'ee' = ा (aa matra)

def akruti_to_unicode(text):
    if not text:
        return ""

    # Reorder chhoti-i matra 'ef'
    # 'ef' precedes consonant or consonant conjunct
    # Matches: ef followed by halant consonant or full consonant
    # In Akruti:
    # 'ef' + '›eâ' -> क्रि
    # 'ef' + 'me' -> सि
    # 'ef' + 'Je' -> वि
    # 'ef' + 'oe' -> दि
    # 'ef' + 've' -> नि
    # 'ef' + 'he' -> पि
    # 'ef' + 'keâ' -> कि
    # 'ef' + 'ue' -> लि
    # 'ef' + 'Me' -> शि
    # 'ef' + 'le' -> ति
    # 'ef' + 'ie' -> गि
    # 'ef' + 'pe' -> जि
    # 'ef' + 'n' -> हि
    # 'ef' + 'õ' -> द्वि

    # First handle special conjuncts with 'ef'
    text = text.replace("ef›eâ", "›eâ_i_")
    text = text.replace("efõ", "õ_i_")

    # General regex for ef followed by consonant:
    # matches ef followed by (optional half-consonant) + full consonant
    text = re.sub(r'ef([A-Za-z«¬©®™±²³´µ¶·¸¹º»¼½¾¿À-ÿ]+)', r'\1_i_', text)

    # Replacements list: ordered longest-first
    replacements = [
        # Full vowels
        ("DeeB", "आँ"), ("DeB", "अं"), ("Dees", "ओ"), ("Deew", "औ"),
        ("Dee", "आ"), ("De", "अ"),
        ("Fkeäkeâ", "इक्क"), ("F&", "ई"), ("F", "इ"),
        ("G", "उ"), ("T", "ऊ"),
        ("_e", "ऋ"),
        ("Ss", "ऐ"), ("S", "ए"),

        # Complex conjuncts
        ("òeâ", "क्त"), ("òe", "त्त"), ("ò", "त्त्"),
        ("›eâ", "क्र"), ("›", "क्र"),
        ("Øe", "प्र"), ("Ø", "प्र"),
        ("õ", "द्व"),
        ("keäkeâ", "क्क"), ("keä", "क्"), ("keâ", "क"),
        ("Kee", "खा"), ("Ke", "ख"), ("K", "ख्"),
        ("iee", "गा"), ("ie", "ग"), ("i", "ग्"),
        ("Iee", "घा"), ("Ie", "घ"), ("I", "घ्"),
        ("Ûee", "चा"), ("Ûe", "च"), ("Û", "च्"),
        ("Ú", "छ"),
        ("pee", "जा"), ("pe", "ज"), ("p", "ज्"),
        ("Pee", "झा"), ("Pe", "झ"), ("P", "झ्"),
        ("¥", "ञ"),
        ("šee", "टा"), ("še", "ट"), ("š", "ट्"),
        ("þee", "ठा"), ("þe", "ठ"), ("þ", "ठ्"),
        ("[ee", "डा"), ("[e", "ड"), ("[", "ड्"),
        ("ªee", "ढा"), ("ªe", "ढ"), ("ª", "ढ्"),
        ("Cee", "णा"), ("Ce", "ण"), ("C", "ण्"),
        ("lee", "ता"), ("le", "त"), ("l", "त्"),
        ("Lee", "था"), ("Le", "थ"), ("L", "थ्"),
        ("oee", "दा"), ("oe", "द"), ("o", "द्"),
        ("Oee", "धा"), ("Oe", "ध"), ("O", "ध्"),
        ("vee", "ना"), ("ve", "न"), ("v", "न्"),
        ("hee", "पा"), ("he", "प"), ("h", "प्"),
        ("Heâ", "फ़"), ("He", "फ"), ("H", "फ्"),
        ("yee", "बा"), ("ye", "ब"), ("y", "ब्"),
        ("Yee", "भा"), ("Ye", "भ"), ("Y", "भ्"),
        ("cee", "मा"), ("ce", "म"), ("c", "म्"),
        ("Ùee", "या"), ("Ùe", "य"), ("Ù", "य्"),
        ("jee", "रा"), ("j", "र"),
        ("uee", "ला"), ("ue", "ल"), ("u", "ल्"),
        ("Jee", "वा"), ("Je", "व"), ("J", "व्"),
        ("Mee", "शा"), ("Me", "श"), ("M", "श्"),
        ("|<ee", "षा"), ("|<e", "ष"), ("<e", "ष"), ("<", "ष्"),
        ("mee", "सा"), ("me", "स"), ("m", "स्"),
        ("nee", "हा"), ("ne", "ह"), ("n", "ह्"),
        ("ü", "ह्न"), ("ý", "ह्य"),

        # Matras & signs
        ("eâ", "क"),
        ("ee", "ा"),
        ("er", "ी"),
        ("g", "ु"),
        ("t", "ू"),
        ("s", "े"),
        ("w", "ै"),
        ("es", "ो"),
        ("ew", "ौ"),
        ("b", "ं"),
        ("B", "ँ"),
        ("~", "।"),
        ("®", "रू"),
        ("™", "रु"),
        ("&", "र्"),
        ("§", "्र"),
        ("`", "'"),
        ("´", "'"),
        ("“", '"'),
        ("”", '"'),
        ("‘", "'"),
        ("’", "'"),
    ]

    for k, v in replacements:
        text = text.replace(k, v)

    # Put back chhoti-i
    text = text.replace("_i_", "ि")

    # Fix reph '&' (र्) - often appears after consonant
    # e.g., 'ieF&' -> गई + र् -> गई
    text = re.sub(r'([क-ह]ा?ी?ु?ू?े?ै?ो?ौ?)र्', r'र्\1', text)

    return text

if __name__ == "__main__":
    samples = [
        "efmeefJeue Øeef›eâÙee mebefnlee, 1908",
        "keâewve meer efoveebkeâ mes oerJeeveer Øeef›eâÙee mebefnlee, 1908 ueeiet keâer ieF&~",
        "ØeLece peveJejer, 1909",
        "efmeefJeue Øeef›eâÙee mebefnlee, 1908 keâer Oeeje 1(2) kesâ Devegmeej, efmeefJeue Øeef›eâÙee mebefnlee, 1 peveJejer 1909 keâes ueeiet keâer ieF&~"
    ]
    for s in samples:
        print("Raw :", s)
        print("Dec :", akruti_to_unicode(s))
        print()
