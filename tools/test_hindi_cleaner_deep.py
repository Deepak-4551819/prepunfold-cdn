import re

def clean_hindi_text(text):
    if not text:
        return ""

    s = text

    # Direct word-level replacements for common legacy words
    word_subs = [
        ("ueenewj", "लाहौर"),
        ("oeceesoj", "दामोदर"),
        ("MewJeOece", "शैवधर्म"),
        ("MesjMeen", "शेरशाह"),
        ("cegncceo", "मोहम्मद"),
        ("cenelcee", "महात्मा"),
        ("ieebOeer", "गाँधी"),
        ("ieeBOeer", "गाँधी"),
        ("uegF", "लुई"),
        ("iJeso", "ऋग्वेद"),
        ("uee@[&", "लॉर्ड"),
        ("la@rd", "लॉर्ड"),
        ("kewâefvebie", "कैनिंग"),
        ("kewâनिbie", "कैनिंग"),
        ("cesÙees", "मेयो"),
        ("[thues", "डूप्ले"),
        ("काGvš o uewueer", "काउंट डी लैली"),
        ("[uenewpeer", "डलहौजी"),
        ("Asharam Paddhati", "आश्रम पद्धति"),
        ("GDC ASST. PROF.", "UPPSC GDC Assistant Professor"),
        ("RPSC Asst. Prof.", "RPSC Assistant Professor"),
        ("UP Higher Asst. Prof.", "UP Higher Education Assistant Professor"),
    ]
    for k, v in word_subs:
        s = s.replace(k, v)

    # Specific common legacy glyphs
    s = s.replace("ला@र्ड", "लॉर्ड")
    s = s.replace("का@लबर्ट", "कॉलबर्ट")
    s = s.replace("का@लेज", "कॉलेज")
    s = s.replace("ड@क्टर", "डॉक्टर")
    s = s.replace("मा@लx-मिंटे", "मार्ले-मिंटो")
    s = s.replace("मा@लx", "मार्ले")
    s = s.replace("मिंटे", "मिंटो")
    s = s.replace("रा@लेट", "रौलेट")
    s = s.replace("आ@ल", "ऑल")
    s = s.replace("आ@]फ", "ऑफ")
    s = s.replace("आ@फ", "ऑफ")
    s = s.replace("पा@वटa", "पावर्टी")
    s = s.replace("अनबिÇfट्श", "अनब्रिटिश")
    s = s.replace("कां«ोस", "काँग्रेस")
    s = s.replace("कां«ेस", "काँग्रेस")
    s = s.replace("बिÇfट्श", "ब्रिटिश")
    s = s.replace("इfण्डया", "इण्डिया")
    s = s.replace("इqण्डया", "इण्डिया")
    s = s.replace("इfण्डयन", "इण्डियन")
    s = s.replace("इंfडयन", "इण्डियन")
    s = s.replace("काउंसिल", "काउंसिल")
    s = s.replace("fह्न्द्ू", "हिन्दू")
    s = s.replace("fह्ंद्ू", "हिन्दू")
    s = s.replace("fह्न्द्ुआें", "हिन्दुओं")
    s = s.replace("fह्स्ट्^ी", "हिस्ट्री")
    s = s.replace("fह्ट्लर", "हिटलर")
    s = s.replace("fह्", "हि")
    s = s.replace("वि®æ", "विरुद्ध")
    s = s.replace("øेंच", "फ्रेंच")
    s = s.replace("øंसिस", "फ्रांसिस")
    s = s.replace("øQक", "फ्रैंक")
    s = s.replace("øQ", "फ्रैं")
    s = s.replace("ø", "फ्र")
    s = s.replace("™प", "रूप")
    s = s.replace("™ल", "रूल")
    s = s.replace("™", "रू")
    s = s.replace("®]जवेल्ट", "रूजवेल्ट")
    s = s.replace("®æ", "द्ध")
    s = s.replace("®", "रु")
    s = s.replace("चन्õ", "चन्द्र")
    s = s.replace("रा°^ीय", "राष्ट्रीय")
    s = s.replace("रा°^", "राष्ट्र")
    s = s.replace("रा„^ीय", "राष्ट्रीय")
    s = s.replace("रा„^", "राष्ट्र")
    s = s.replace("केन्õीय", "केन्द्रीय")
    s = s.replace("मान्केकर", "मानकेकर")
    s = s.replace("अनटेल्ड", "अनटोल्ड")
    s = s.replace("स्टेरी", "स्टोरी")
    s = s.replace("अंगुली छ", "अंगुली छाप")
    s = s.replace("साfम्मलित", "सम्मिलित")
    s = s.replace("विघाfट्त", "विघटित")
    s = s.replace("माfह्लाआें", "महिलाओं")
    s = s.replace("पुनविवाह", "पुनर्विवाह")
    s = s.replace("समीfह्त", "समाहित")
    s = s.replace("मुत्ति वीfह्नी", "मुक्ति वाहिनी")
    s = s.replace("मुत्ति", "मुक्ति")
    s = s.replace("वीfह्नी", "वाहिनी")
    s = s.replace("अल्पन्सो डr अल्बुकक", "अल्फोंसो डी अल्बुकर्क")
    s = s.replace("øंसिस्काे डr अल्मेड", "फ्रांसिस्को डी अल्मेडा")
    s = s.replace("निनो द क्ुन्ह", "नीनो दा कुन्हा")
    s = s.replace("वास्काेfडगामा", "वास्कोडिगामा")

    # Regex fixes for lingering patterns
    # 1. 'ा@' -> 'ॉ'
    s = re.sub(r'([क-ह])ा@', r'\1ॉ', s)
    s = re.sub(r'([क-ह])@', r'\1ॉ', s)
    s = re.sub(r'आ@', r'ऑ', s)

    # 2. Devanagari letter followed by 'r' -> replace 'r' with 'ी'
    s = re.sub(r'([क-ह])r\b', r'\1ी', s)
    s = re.sub(r'([क-ह])r', r'\1ी', s)

    # 3. 'f' followed by Devanagari letter -> letter with chhoti-i 'ि'
    s = re.sub(r'f([क-ह])', r'\1ि', s)

    # 4. 'द्ेश' -> 'देश'
    s = s.replace("द्ेश", "देश")
    s = s.replace("प्रदन", "प्रदान")
    s = s.replace("प्रस्तव", "प्रस्ताव")
    s = s.replace("जमाRदरी", "जमींदारी")
    s = s.replace("जमाRदर", "जमींदार")
    s = s.replace("अंगीकृत", "अंगीकृत")
    s = s.replace("ह्ुआ", "हुआ")
    s = s.replace("ह्ुई", "हुई")
    s = s.replace("ह्ुए", "हुए")
    s = s.replace("ह्ू", "हू")
    s = s.replace("ह्ु", "हु")
    s = s.replace("हैद्राबाद", "हैदराबाद")
    s = s.replace("नेह्™", "नेहरू")

    # 5. Clean up numbers with embedded devanagari zero (19०1 -> 1901)
    s = re.sub(r'(\d+)०(\d*)', r'\g<1>0\g<2>', s)
    s = re.sub(r'०(\d+)', r'0\g<1>', s)

    # 6. 'F&.' -> 'ई.'
    s = s.replace("F&.", "ई.")
    s = s.replace("F&", "ई.")

    # 7. Stray characters
    s = re.sub(r'[`~^§©\u2217]', '', s)

    return s.strip()

# Test on problematic samples
test_cases = [
    "किसने व्यपगत के सिद्धन्त की रचना की?",
    "uee@[& kewâनिbie",
    "काGvš o uewueer",
    "किसे लार्ड कर्जन ने 19०1 में पुरातत्व विभाग का डइरेक्यट्र जनरल नियुक्त किया था?",
    "fह्न्द्ू विवाह अधिनियम",
    "अल्पन्सो डr अल्बुकक",
    "चोटr",
    "1903 F&.",
    "जमाRदरी उन्मूलन",
    "नेह्™ द्वारा"
]

for tc in test_cases:
    print(f"{tc:<50} -> {clean_hindi_text(tc)}")
