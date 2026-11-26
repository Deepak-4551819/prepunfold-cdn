import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from kruti_converter import kruti_to_unicode

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
    out = kruti_to_unicode(w)
    print(f"{w:<20} -> {out}")
