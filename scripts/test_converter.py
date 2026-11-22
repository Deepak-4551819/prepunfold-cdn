# -*- coding: utf-8 -*-
import re

AKRUTI_MAP = {
    # Special conjuncts with chhoti-i 'ef'
    'ef›eâ': 'क्रि', 'efõ': 'द्वि', 'efo': 'दि', 'efme': 'सि', 'efJe': 'वि',
    'efve': 'नि', 'efhe': 'पि', 'efkeâ': 'कि', 'efue': 'लि', 'efMe': 'शि',
    'efle': 'ति', 'efie': 'गि', 'efpe': 'जि', 'efn': 'हि', 'efne': 'हि',
    'efYe': 'भि', 'efye': 'बि', 'efLe': 'थि', 'efOe': 'धि', 'efIe': 'घि',
    'efÛe': 'चि', 'efÚ': 'छि', 'efše': 'टि', 'efþe': 'ठि', 'ef[e': 'डि',
    'ef[': 'डि', 'efªe': 'ढि', 'efCe': 'णि', 'efKe': 'खि', 'efPe': 'झि',
    'ef<e': 'षि', 'efj': 'रि', 'efje': 'रि', 'efòe': 'त्ति', 'efkeä': 'क्कि',
    'efmle': 'स्ति', 'efmLe': 'स्थि', 'efmJe': 'स्वि', 'efõ': 'द्वि',

    # Words / syllables with 'aa' matra
    'keâe': 'का', 'Kee': 'खा', 'iee': 'गा', 'Iee': 'घा',
    'Ûee': 'चा', 'Úee': 'छा', 'pee': 'जा', 'Pee': 'झा',
    'šee': 'टा', 'þee': 'ठा', '[ee': 'डा', 'ªee': 'ढा', 'Cee': 'णा',
    'lee': 'ता', 'Lee': 'था', 'oee': 'दा', 'Oee': 'धा', 'vee': 'ना',
    'hee': 'पा', 'Heâe': 'फ़ा', 'Hee': 'फा', 'yee': 'बा', 'Yee': 'भा',
    'cee': 'मा', 'Ùee': 'या', 'jee': 'रा', 'uee': 'ला', 'Jee': 'वा',
    'Mee': 'शा', '<ee': 'षा', 'mee': 'सा', 'nee': 'हा',

    # Single consonants (full)
    'keâ': 'क', 'Ke': 'ख', 'ie': 'ग', 'Ie': 'घ',
    'Ûe': 'च', 'Ú': 'छ', 'pe': 'ज', 'Pe': 'झ', '¥': 'ञ',
    'še': 'ट', 'þe': 'ठ', '[e': 'ड', '[': 'ड', 'ªe': 'ढ', 'Ce': 'ण',
    'le': 'त', 'Le': 'थ', 'oe': 'द', 'Oe': 'ध', 've': 'न',
    'he': 'प', 'Heâ': 'फ़', 'He': 'फ', 'ye': 'ब', 'Ye': 'भ',
    'ce': 'म', 'Ùe': 'य', 'je': 'र', 'ue': 'ल', 'Je': 'व',
    'Me': 'श', '<e': 'ष', 'me': 'स', 'ne': 'ह',

    # Half consonants
    'keä': 'क्', 'K': 'ख्', 'i': 'ग्', 'I': 'घ्',
    'Û': 'च्', 'p': 'ज्', 'P': 'झ्',
    'š': 'ट्', 'þ': 'ठ्', 'ª': 'ढ्', 'C': 'ण्',
    'l': 'त्', 'L': 'थ्', 'o': 'द्', 'O': 'ध्', 'v': 'न्',
    'h': 'प्', 'H': 'फ्', 'y': 'ब्', 'Y': 'भ्',
    'c': 'म्', 'Ù': 'य्', 'j': 'र', 'u': 'ल्', 'J': 'व्',
    'M': 'श्', '<': 'ष्', 'm': 'स्', 'n': 'ह्',

    # Conjuncts
    'òeâ': 'क्त', 'òe': 'त्त', 'ò': 'त्त्',
    'Øe': 'प्र', 'Ø': 'प्र', '›eâ': 'क्र', '›': 'क्र',
    'õ': 'द्व', 'ü': 'ह्न', 'ý': 'ह्य',
    '#': 'क्ष', '$': 'त्र',

    # Vowels
    'DeeB': 'आँ', 'DeB': 'अं', 'Dees': 'ओ', 'Deew': 'औ', 'Dee': 'आ', 'De': 'अ',
    'Fkeäkeâ': 'इक्क', 'F&': 'ई', 'F': 'इ', 'G': 'उ', 'T': 'ऊ', '_e': 'ऋ', 'Ss': 'ऐ', 'S': 'ए',

    # Common combinations
    'kesâ': 'के', 'ceW': 'में', 'nw': 'है', 'nQ': 'हैं', 'mes': 'से',
    'keâes': 'को', 'keâeR': 'कीं', 'keâer': 'की',

    # Matras & symbols
    'ee': 'ा', 'er': 'ी', 'g': 'ु', 't': 'ू',
    's': 'े', 'w': 'ै', 'es': 'ो', 'ew': 'ौ',
    'b': 'ं', 'B': 'ँ', '~': '।',
    '®': 'रू', '™': 'रु',
    '&': 'र्', '§': '्र',
    '‘': "'", '’': "'", '“': '"', '”': '"',
    '`': "'", '´': "'",
    'eâ': 'क', 'e': 'ा', 'W': 'ं',
}

keys_sorted = sorted(AKRUTI_MAP.keys(), key=lambda x: -len(x))
pattern = re.compile('|'.join(re.escape(k) for k in keys_sorted))

def convert(text):
    res = pattern.sub(lambda m: AKRUTI_MAP[m.group(0)], text)
    # Reph & (र्) - in Akruti, & comes after the syllable
    # e.g. ieF& -> गई + र् -> गई or efveCe&Ùe -> निर्णय
    res = re.sub(r'([क-ह][ािीुूेैोौंँ]*)र्', r'र्\1', res)
    # Clean up double aa matra if any
    res = res.replace('ाा', 'ा')
    return res

samples = [
    'efmeefJeue Øeef›eâÙee mebefnlee, 1908',
    'keâewve meer efoveebkeâ mes oerJeeveer Øeef›eâÙee mebefnlee, 1908 ueeiet keâer ieF&~',
    'ØeLece peveJejer, 1909',
    'efmeefJeue Øeef›eâÙee mebefnlee keâer efkeâme Oeeje ceW ‘ef[›eâer heeefjle keâjves Jeeuee vÙeeÙeeueÙe’ heo heefjYeeef<ele nw–',
    'DeeefOehelÙe SJeb ceOÙeJeleea ueeYe kesâ Jeeo ceW–DeeosMe 20 efveÙece 12',
    'Jeeohe$e keâe veecebpetj efkeâÙee peevee Deewj'
]
for s in samples:
    print('Raw:', s)
    print('Uni:', convert(s))
    print()
