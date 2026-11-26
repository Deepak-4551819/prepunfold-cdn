# -*- coding: utf-8 -*-
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

# Test sample sentences from the PDF
samples = [
    "02. efmevOeg Ieešer meYÙelee keâer ØecegKe efJeMes<eleeSB",
    "1. efkeâme nÌ[hhee mLeue mes efvekeâeme veeefueÙeeW kesâ meeLe heâMe& peefÌ[le yeejn mveeveie=n keâe Skeâ (mesš) mecetn efceuee nw?",
    "2. efvecveefueefKele nÌ[hhee mLeueeW ceW mes efkeâme Skeâ mLeue mes iele&-DeeJeeme kesâ ØeceeCeeW keâer Øeeefhle ngF& nw?",
    "3. efvecveefueefKele mLeueeW ceW efkeâme Skeâ mes GòejJeleea nÌ[hhee keâeue, ceeueJee Deewj peesjJes mebmke=âefleÙeeB efceueer nQ?",
    "Ans. (c) : nÌ[hhee SJeb ceesnvepeesoÌ[eW kesâ Deefleefjòeâ ueesLeue Yeer meQOeJe meYÙelee keâe ØecegKe mLeue nw~ ueesLeue keâe šeruee Denceoeyeeo (iegpejele) efpeues ceW mejieJeue veecekeâ «eece kesâ meceerhe efmLele nw~",
    "70. ________ves efmeæ efkeâÙee efkeâ nÌ[hhee kesâ ueesieeW ceW Skeâ meeceevÙe oheâveeves keâer heæefle Leer~",
    "100. metÛeer-I keâes metÛeer-II mes megcesefuele keâerefpeS Deewj efoS ieS ketâš mes mener Gòej keâe ÛeÙeve keâerefpeS :",
    "209. efvecveebeEkeâle ceW mes Øeekeä-nÌ[hhee mebmke=âefle keâewve-meer nw?",
]

def decode_aps_clean(text):
    if not text:
        return ""
    s = text

    # Remove PDF watermarks / noise
    s = re.sub(r'JOIN\s*@APNAPDFS', '', s, flags=re.IGNORECASE)
    s = re.sub(r'@Apnapdfs', '', s, flags=re.IGNORECASE)
    s = re.sub(r'CLICK\s*HERE', '', s, flags=re.IGNORECASE)

    # Common words & compounds pre-substitution
    word_map = [
        ("nÌ[hhee", "हड़प्पा"), ("nÌ[hheerÙe", "हड़प्पीय"),
        ("ceesnvepeesoÌ[eW", "मोहनजोदड़ो"), ("ceesnvepeesoÌ[es", "मोहनजोदड़ो"),
        ("ueesLeue", "लोथल"), ("keâeueeryebiee", "कालीबंगा"),
        ("yeveeJeueer", "बनावली"), ("jeKeerieÌ{er", "राखीगढ़ी"),
        ("ÛevntoÌ[eW", "चन्हुदड़ो"), ("OeewueeJeerje", "धौलावीरा"),
        ("megjkeâesleoe", "सुरकोटदा"), ("meQOeJe", "सैंधव"),
        ("efvecveefueefKele", "निम्नलिखित"), ("efvecveebeEkeâle", "निम्नांकित"),
        ("efvecve", "निम्न"), ("mener", "सही"),
        ("megcesefuele", "सुमेलित"), ("metÛeer-I", "सूची-I"),
        ("metÛeer-II", "सूची-II"), ("metÛeer", "सूची"),
        ("ketâš", "कूट"), ("efJeMes<eleeSB", "विशेषताएँ"),
        ("efJeMes<elee", "विशेषता"), ("mebmke=âefle", "संस्कृति"),
        ("mebmke=âefleÙeeW", "संस्कृतियों"), ("mebmke=âefleÙeeB", "संस्कृतियाँ"),
        ("Deeueceieerjhegj", "आलमगीरपुर"), ("«eece", "ग्राम"),
        ("«eecerCe", "ग्रामीण"), ("šeruee", "टीला"),
        ("Denceoeyeeo", "अहमदाबाद"), ("DeJeMes<e", "अवशेष"),
        ("Ùeespevee", "योजना"), ("megefveÙeesefpele", "सुनियोजित"),
        ("megJÙeJeefmLele", "सुव्यवस्थित"), ("veeefueÙeeW", "नालियों"),
        ("mveeveie=n", "स्नानगृह"), ("heâMe&", "फर्श"),
        ("GòejJeleea", "उत्तरवर्ती"), ("Gòejer", "उत्तरी"),
        ("oef#eCeer", "दक्षिणी"), ("oef#eCe", "दक्षिण"),
        ("heeqMÛeceer", "पश्चिमी"), ("hetJeea", "पूर्वी"),
        ("Deefleefjòeâ", "अतिरिक्त"), ("DeeOeej", "आधार"),
        ("GheueyOe", "उपलब्ध"), ("meeceevÙe", "सामान्य"),
        ("oheâveeves", "दफनाने"), ("heæefle", "पद्धति"),
        ("efmeæ", "सिद्ध"), ("Ghejesòeâ", "उपर्युक्त"),
        ("oesveeW", "दोनों"), ("GlKeveve", "उत्खनन"),
        ("Gòej", "उत्तर"), ("Ans.", "Ans."),
        ("JÙeeKÙee", "व्याख्या"), ("kesâ", "के"),
        ("keâer", "की"), ("keâe", "का"),
        ("keâes", "को"), ("mes", "से"),
        ("ceW", "में"), ("nw~", "है।"),
        ("nQ~", "हैं।"), ("Lee~", "था।"),
        ("Les~", "थे।"), ("Leer~", "थी।"),
        ("SJeb", "एवं"), ("leLee", "तथा"),
        ("Deewj", "और"), ("veneR", "नहीं"),
        ("efkeâme", "किस"), ("Fme", "इस"),
        ("Gme", "उस"), ("efpemes", "जिस"),
        ("ÙeneB", "यहाँ"), ("JeneB", "वहाँ"),
        ("~", "।"), ("Ì[", "ड़"), ("Ì{", "ढ़"),
        ("ef›eâ", "क्रि"), ("›eâ", "क्र"),
        ("efMe", "शि"), ("efve", "नि"), ("efmLe", "स्थि"),
        ("efJe", "वि"), ("efce", "मि"), ("efpe", "जि"),
        ("efue", "लि"), ("efle", "ति"), ("efkeâ", "कि"),
        ("efye", "बि"), ("efOe", "धि"), ("efme", "सि"),
        ("efhe", "पि"), ("efYe", "भि"), ("efHe", "फि"),
        ("efo", "दि"), ("efo", "दि"), ("efLe", "थि"),
        ("efIe", "घि"), ("efKe", "खि"), ("efie", "गि"),
    ]
    for k, v in word_map:
        s = s.replace(k, v)

    # Let aps_decoder handle remainder
    from aps_decoder import decode_aps
    s = decode_aps(s)

    # Clean residual halants on standalone words
    s = re.sub(r'([क-ह])्(?=[\s\.,।\?!:;\)\]\"]|$)', r'\1', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

for idx, sample in enumerate(samples, 1):
    print(f"Sample {idx}:")
    print("  RAW:", sample)
    print("  DEC:", decode_aps_clean(sample))
