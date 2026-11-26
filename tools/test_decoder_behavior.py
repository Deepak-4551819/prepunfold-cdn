import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from aps_decoder import decode_aps

test_words = [
    "ueenewj",
    "oeceesoj",
    "MewJeOece",
    "uegF",
    "iebiee",
    "kewâefvebie",
    "la@rd",
    "uee@[&",
    "cesÙees",
    "™प",
    "[thues",
    "काGvš o uewueer",
    "[uenewpeer"
]

for w in test_words:
    out = decode_aps(w)
    print(f"{w:<20} -> {out}")
