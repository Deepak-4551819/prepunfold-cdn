# -*- coding: utf-8 -*-
import unicodedata
import re

GREEK_MAP = {
    "MATHEMATICAL ITALIC SMALL ALPHA": r"\alpha",
    "MATHEMATICAL ITALIC SMALL BETA": r"\beta",
    "MATHEMATICAL ITALIC SMALL GAMMA": r"\gamma",
    "MATHEMATICAL ITALIC SMALL DELTA": r"\delta",
    "MATHEMATICAL ITALIC SMALL EPSILON": r"\epsilon",
    "MATHEMATICAL ITALIC SMALL ZETA": r"\zeta",
    "MATHEMATICAL ITALIC SMALL ETA": r"\eta",
    "MATHEMATICAL ITALIC SMALL THETA": r"\theta",
    "MATHEMATICAL ITALIC SMALL IOTA": r"\iota",
    "MATHEMATICAL ITALIC SMALL KAPPA": r"\kappa",
    "MATHEMATICAL ITALIC SMALL LAMBDA": r"\lambda",
    "MATHEMATICAL ITALIC SMALL MU": r"\mu",
    "MATHEMATICAL ITALIC SMALL NU": r"\nu",
    "MATHEMATICAL ITALIC SMALL XI": r"\xi",
    "MATHEMATICAL ITALIC SMALL PI": r"\pi",
    "MATHEMATICAL ITALIC SMALL RHO": r"\rho",
    "MATHEMATICAL ITALIC SMALL SIGMA": r"\sigma",
    "MATHEMATICAL ITALIC SMALL TAU": r"\tau",
    "MATHEMATICAL ITALIC SMALL UPSILON": r"\upsilon",
    "MATHEMATICAL ITALIC SMALL PHI": r"\phi",
    "MATHEMATICAL ITALIC SMALL CHI": r"\chi",
    "MATHEMATICAL ITALIC SMALL PSI": r"\psi",
    "MATHEMATICAL ITALIC SMALL OMEGA": r"\omega",
    "GREEK CAPITAL LETTER DELTA": r"\Delta",
    "GREEK CAPITAL LETTER OMEGA": r"\Omega",
    "GREEK CAPITAL LETTER SIGMA": r"\Sigma",
    "GREEK CAPITAL LETTER PI": r"\Pi",
    "GREEK CAPITAL LETTER LAMBDA": r"\Lambda",
    "GREEK CAPITAL LETTER XI": r"\Xi",
}

def clean_math_text(s: str) -> str:
    # 1. Handle combining vector arrow (char + \u20d7) and combining hat (char + \u0302)
    s = re.sub(r'([A-Za-z\u1d400-\u1d7ff\u0370-\u03ff])\u20d7', r'\\vec{\1}', s)
    s = re.sub(r'([A-Za-z\u1d400-\u1d7ff\u0370-\u03ff])\u0302', r'\\hat{\1}', s)
    s = re.sub(r'∇\u20d7+', r'\\vec{\\nabla}', s)

    out = []
    for c in s:
        code = ord(c)
        if 0x1d400 <= code <= 0x1d7ff:
            name = unicodedata.name(c, "")
            if name in GREEK_MAP:
                out.append(" " + GREEK_MAP[name] + " ")
            elif "CAPITAL" in name:
                # Last word is the letter
                out.append(name.split()[-1])
            elif "SMALL" in name:
                out.append(name.split()[-1].lower())
            else:
                out.append(c)
        elif code == 0x2212: # minus
            out.append("-")
        elif code == 0x210f: # hbar
            out.append(r"\hbar")
        elif code == 0x2207: # nabla
            out.append(r"\nabla")
        elif code == 0x221a: # sqrt
            out.append(r"\sqrt")
        elif code == 0xd7:   # times
            out.append(r"\times")
        elif code == 0x2260: # neq
            out.append(r"\neq")
        elif code == 0x27e8: # <
            out.append(r"\langle")
        elif code == 0x27e9: # >
            out.append(r"\rangle")
        elif code == 0x2192: # ->
            out.append(r"\to")
        elif code == 0x305:  # overline
            pass
        elif code == 0x2245: # approx equal
            out.append(r"\cong")
        elif code == 0x2264: # <=
            out.append(r"\le")
        elif code == 0x2265: # >=
            out.append(r"\ge")
        elif code == 0x221d: # proportional
            out.append(r"\propto")
        else:
            out.append(c)
    res = "".join(out)
    res = re.sub(r'\s+', ' ', res)
    return res

import json
blocks = json.load(open('temp_gate_pdfs/gate_ph_2026_raw_blocks.json', encoding='utf-8'))
for qn in [11, 14, 15, 18, 19, 21, 24, 27, 36, 37, 39, 41, 51]:
    print(f"=== Q{qn} cleaned ===")
    print(clean_math_text(blocks[str(qn)])[:250])
