# -*- coding: utf-8 -*-
import pymupdf, re

def aps_to_unicode(text):
    if not text:
        return ""

    s = text

    # Normalize punctuation
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = s.replace("~", "।").replace("0", "०")

    # 1. Step 1: Handle reph '&'
    # In APS, '&' is typed after a consonant to put 'र्' on top.
    # We replace C + '&' with 'र्' + C
    # But let's first handle 'ef' (short-i)
    # 'ef' is typed BEFORE the consonant(s)
    # Regex: 'ef' followed by:
    # (optional half consonants: [kKiIÛpPlLoOvhHyYcumJMn#$ß]) +
    # (full consonant or conjunct)

    # Half consonant list in APS:
    half_chars = "kKiIÛpPlLoOvhHyYcumJMn#$ß<"

    # Full consonants in APS:
    # keâ, Ke, ie, Ie, ³e, Ûe, Ú, pe, Pe, ×e, še, "e, [e, {e, Ce, le, Le, oe, Oe, ve, he, He, ye, Ye, ce, Ùe, j, ue, Je, Me, <e, me, ne, #e, $e, %e, ße, òe, É, Ü, Í, Î, Ï, Õe, Øe

    # Let's map full consonants to a temporary token or directly
    # Easier approach: replace character tokens systematically!

    # Step A: Pre-replace conjuncts
    subs_conjuncts = [
        ("òee", "tta_aa"), ("òe", "tta_full"), ("ò", "त्त्"),
        ("Ée", "dva_aa"), ("É", "द्व"),
        ("Üe", "ddha_aa"), ("Ü", "द्ध"),
        ("Íe", "dya_aa"), ("Í", "द्य"),
        ("Îe", "dma_aa"), ("Î", "द्म"),
        ("Ïe", "dra_aa"), ("Ï", "द्र"),
        ("Õe", "शवा"), ("Õ", "श्व"),
        ("Øe", "pra_full"), ("Ø", "प्र"),
        ("keä", "क्या"),
        ("k=â", "कृ"), ("i=â", "गृ"), ("le=â", "तृ"), ("=â", "्र"),
        ("šô", "ट्र"), ("[ô", "ड्र"), ("{ô", "ढ्र"),
    ]
    for k, v in subs_conjuncts:
        s = s.replace(k, v)

    # Vowels
    subs_vowels = [
        ("Dee", "आ"), ("Dees", "ओ"), ("Deew", "औ"), ("De", "अ"),
        ("F&", "ई"), ("F", "इ"), ("Gâ", "ऊ"), ("G", "उ"),
        ("Sâ", "ऐ"), ("S", "ए"), ("*e", "ऋ"),
    ]
    for k, v in subs_vowels:
        s = s.replace(k, v)

    # Full consonants (inherent 'a')
    subs_cons = [
        ("keâe", "का"), ("keâ", "क"),
        ("Kee", "खा"), ("Ke", "ख"),
        ("iee", "गा"), ("ie", "ग"),
        ("Iee", "घा"), ("Ie", "घ"),
        ("³ee", "ङा"), ("³e", "ङ"),
        ("Ûee", "चा"), ("Ûe", "च"),
        ("Úe", "छा"), ("Ú", "छ"),
        ("pee", "जा"), ("pe", "ज"),
        ("Pee", "झा"), ("Pe", "झ"),
        ("×ee", "ञा"), ("×e", "ञ"),
        ("šee", "टा"), ("še", "ट"),
        ('"ee', "ठा"), ('"e', "ठ"),
        ("[ee", "डा"), ("[e", "ड"),
        ("{ee", "ढा"), ("{e", "ढ"),
        ("Cee", "णा"), ("Ce", "ण"),
        ("lee", "ता"), ("le", "त"),
        ("Lee", "था"), ("Le", "थ"),
        ("oee", "दा"), ("oe", "द"),
        ("Oee", "धा"), ("Oe", "ध"),
        ("vee", "ना"), ("ve", "न"),
        ("hee", "पा"), ("he", "प"),
        ("Hee", "फा"), ("He", "फ"),
        ("yee", "बा"), ("ye", "ब"),
        ("Yee", "भा"), ("Ye", "भ"),
        ("cee", "मा"), ("ce", "म"),
        ("Ùee", "या"), ("Ùe", "य"),
        ("jee", "रा"), ("j", "र"),
        ("ueee", "ला"), ("ue", "ल"),
        ("Jee", "वा"), ("Je", "व"),
        ("Mee", "शा"), ("Me", "श"),
        ("<ee", "षा"), ("<e", "ष"),
        ("mee", "सा"), ("me", "स"),
        ("nee", "हा"), ("ne", "ह"),
        ("#ee", "क्षा"), ("#e", "क्ष"),
        ("$ee", "त्रा"), ("$e", "त्र"),
        ("%ee", "ज्ञा"), ("%e", "ज्ञ"),
        ("ßee", "श्रा"), ("ße", "श्र"),
        ("pra_full", "प्र"), ("tta_full", "त्त"), ("tta_aa", "त्ता"),
        ("dva_aa", "द्वा"), ("ddha_aa", "द्धा"), ("dya_aa", "द्या"),
    ]
    for k, v in subs_cons:
        s = s.replace(k, v)

    # Half consonants
    subs_half = [
        ("k", "क्"), ("K", "ख्"), ("i", "ग्"), ("I", "घ्"),
        ("Û", "च्"), ("p", "ज्"), ("P", "झ्"),
        ("l", "त्"), ("L", "थ्"), ("o", "द्"), ("O", "ध्"), ("v", "न्"),
        ("h", "प्"), ("H", "फ्"), ("y", "ब्"), ("Y", "भ्"), ("c", "म्"),
        ("u", "ल्"), ("J", "व्"), ("M", "श्"), ("<", "ष्"), ("m", "स्"),
        ("n", "ह्"), ("#", "क्ष्"), ("$", "त्र्"), ("%", "ज्ञ्"), ("ß", "श्र्"),
    ]
    for k, v in subs_half:
        s = s.replace(k, v)

    # Matras
    subs_matras = [
        ("ee", "ा"), ("er", "ी"), ("g", "ु"), ("t", "ू"),
        ("s", "े"), ("w", "ै"), ("es", "ो"), ("ew", "ौ"),
        ("W", "ें"), ("b", "ं"), ("B", "ँ"),
        ("=", "ृ"), ("@e", "ॉ"), ("@", "ॅ"),
        ("&", "ी"),
    ]
    for k, v in subs_matras:
        s = s.replace(k, v)

    # Fix short-i 'ef'
    # Pattern: 'ef' followed by half consonant(s) and full consonant
    # Example: 'ef' + 'क' -> 'कि', 'ef' + 'स्' + 'थ' -> 'स्थि'
    def fix_i(match):
        cluster = match.group(1)
        return cluster + "ि"

    s = re.sub(r'ef([क-ह]्[क-ह]|[क-ह])', fix_i, s)
    s = re.sub(r'e([क-ह]्[क-ह]|[क-ह])', fix_i, s)

    # Fix lingering 'e'
    s = s.replace("e", "")

    return s

doc = pymupdf.open(r'C:\Users\yedde\Downloads\GEOGRAPHY CHAPTER-WISE SOLVED PAPERS.pdf')
page = doc[8] # page 9
raw_text = page.get_text()

# We only convert lines that are NOT headers/footers/exam tags
lines = raw_text.splitlines()
converted_lines = []
for l in lines:
    ls = l.strip()
    if not ls:
        continue
    if ls in ("TGT/PGT Geography Planner", "YCT", "9") or ls.startswith("UP PGT") or ls.startswith("NTA UGC"):
        converted_lines.append(ls)
    elif ls.startswith("Ans."):
        # separate Ans. (x) : from Hindi text
        m = re.match(r'^(Ans\.\s*\([a-eA-E]\)\s*[:\.]?)(.*)$', ls)
        if m:
            converted_lines.append(m.group(1) + " " + aps_to_unicode(m.group(2)))
        else:
            converted_lines.append(aps_to_unicode(ls))
    elif re.match(r'^\([a-eA-E]\)', ls):
        # option letter
        m = re.match(r'^(\([a-eA-E]\)\s*)(.*)$', ls)
        converted_lines.append(m.group(1) + aps_to_unicode(m.group(2)))
    else:
        # question or text
        m = re.match(r'^(\d+\.\s*)(.*)$', ls)
        if m:
            converted_lines.append(m.group(1) + aps_to_unicode(m.group(2)))
        else:
            converted_lines.append(aps_to_unicode(ls))

print("=== CONVERTED PAGE 9 TEXT ===")
print("\n".join(converted_lines[:25]))
