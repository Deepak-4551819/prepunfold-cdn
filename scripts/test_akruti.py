# Test Akruti font decoding
import re

akruti_map = [
    # Multi-char conjuncts & vowels
    ("Fkeäkeâ", "इक्क"),
    ("DeeB", "आँ"), ("DeB", "अं"), ("Dees", "ओ"), ("Deew", "औ"),
    ("Dee", "आ"), ("De", "अ"),
    ("F&", "ई"), ("F", "इ"),
    ("G", "उ"), ("T", "ऊ"),
    ("_e", "ऋ"),
    ("Ss", "ऐ"), ("S", "ए"),

    ("›eâ", "क्र"), ("Øe", "प्र"),
    ("keä", "क्"), ("keâ", "क"),
    ("Ke", "ख"), ("K", "ख्"),
    ("ie", "ग"), ("i", "ग्"),
    ("Ie", "घ"), ("I", "घ्"),
    ("Ûe", "च"), ("Û", "च्"),
    ("Ú", "छ"),
    ("pe", "ज"), ("p", "ज्"),
    ("Pe", "झ"), ("P", "झ्"),
    ("še", "ट"), ("š", "ट्"),
    ("þe", "ठ"), ("þ", "ठ्"),
    ("[e", "ड"), ("[", "ड्"),
    ("ªe", "ढ"), ("ª", "ढ्"),
    ("Ce", "ण"), ("C", "ण्"),
    ("le", "त"), ("l", "त्"),
    ("Le", "थ"), ("L", "थ्"),
    ("oe", "द"), ("o", "द्"),
    ("Oe", "ध"), ("O", "ध्"),
    ("ve", "न"), ("v", "न्"),
    ("he", "प"), ("h", "प्"),
    ("Heâ", "फ़"), ("He", "फ"), ("H", "फ्"),
    ("ye", "ब"), ("y", "ब्"),
    ("Ye", "भ"), ("Y", "भ्"),
    ("ce", "म"), ("c", "म्"),
    ("Ùee", "या"), ("Ùe", "य"), ("Ù", "य्"),
    ("j", "र"),
    ("ue", "ल"), ("u", "ल्"),
    ("Je", "व"), ("J", "व्"),
    ("Me", "श"), ("M", "श्"),
    ("<e", "ष"), ("<", "ष्"),
    ("me", "स"), ("m", "स्"),
    ("ne", "ह"), ("n", "ह्"),

    # Matras
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
    ("òeâ", "क्त"), ("òe", "त्त"), ("ò", "त्त्"),
    ("õ", "द्"),
]

def decode_akruti(text):
    if not text:
        return ""

    # Handle pre-base 'ef' (chhoti-i matra)
    # In Akruti, 'ef' comes BEFORE the consonant (single or half+consonant)
    # e.g., efme -> सि, efJe -> वि, ef›eâ -> क्रि, efn -> हि
    # We can handle ef by matching ef followed by consonant/cluster and moving 'ि' after it!
    # Pattern: ef followed by 1 or 2 tokens

    # Sort mappings by length descending
    sorted_map = sorted(akruti_map, key=lambda x: len(x[0]), reverse=True)

    # Let's replace ef pattern:
    # First, let's identify consonants in raw form:
    # 'me', 'Je', '›eâ', 'n', 'o', 'oe', 'Ce', 'keâ', 've', etc.
    res = text
    # Let's test on Q1 explanation
    for k, v in sorted_map:
        # If ef is at start, let's see
        pass
    return text

raw_exp = "efmeefJeue Øeef›eâÙee mebefnlee, 1908 keâer Oeeje 1(2) kesâ Devegmeej, efmeefJeue Øeef›eâÙee mebefnlee, 1 peveJejer 1909 keâes ueeiet keâer ieF&~"
print("Raw:", raw_exp)
