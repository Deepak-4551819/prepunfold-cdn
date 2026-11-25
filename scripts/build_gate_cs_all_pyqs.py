# -*- coding: utf-8 -*-
"""
Official GATE Computer Science (CS) PYQ Extractor & Builder (2022 - 2026)
Downloads (if needed) official GATE CS Question Papers & Answer Keys from IIT Madras (gate2027.iitm.ac.in),
extracts all 65 questions per paper with geometric block sorting and math glyph normalization,
validates marks/types/keys/options, and writes AbhyasDesk-compatible JSON files under:
  tests/gate/gate_cs/pyq/
"""

import os
import sys
import re
import json
import unicodedata
import requests
import pdfplumber
import pymupdf

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

RAW_PDF_DIR = os.path.join("raw_pdfs", "gate_cs")
OUTPUT_DIR = os.path.join("tests", "gate", "gate_cs", "pyq")
HEADERS = {"User-Agent": "Mozilla/5.0"}

PAPERS = {
    "gate_cs_pyq_2026_set1": {
        "raw_prefix": "gate_cs_2026_s1",
        "year": 2026,
        "set_label": "Set 1",
        "shift_badge": "GATE CS • 2026 Set 1 Official Paper",
        "pyq_tag": "GATE Computer Science (CS) • 2026 Set 1 Official Paper",
        "title_en": "GATE 2026 Computer Science (CS) Set 1 Official Solved Paper",
        "qp_url": "https://gate2027.iitm.ac.in/static/doc/download/2026/QPs/CS1.pdf",
        "key_url": "https://gate2027.iitm.ac.in/static/doc/download/2026/Keys/CS1_Keys.pdf",
        "is_free": False,
    },
    "gate_cs_pyq_2026_set2": {
        "raw_prefix": "gate_cs_2026_s2",
        "year": 2026,
        "set_label": "Set 2",
        "shift_badge": "GATE CS • 2026 Set 2 Official Paper",
        "pyq_tag": "GATE Computer Science (CS) • 2026 Set 2 Official Paper",
        "title_en": "GATE 2026 Computer Science (CS) Set 2 Official Solved Paper",
        "qp_url": "https://gate2027.iitm.ac.in/static/doc/download/2026/QPs/CS2.pdf",
        "key_url": "https://gate2027.iitm.ac.in/static/doc/download/2026/Keys/CS2_Keys.pdf",
        "is_free": False,
    },
    "gate_cs_pyq_2025_set2": {
        "raw_prefix": "gate_cs_2025_s2",
        "year": 2025,
        "set_label": "Set 2",
        "shift_badge": "GATE CS • 2025 Set 2 Official Paper",
        "pyq_tag": "GATE Computer Science (CS) • 2025 Set 2 Official Paper",
        "title_en": "GATE 2025 Computer Science (CS) Set 2 Official Solved Paper",
        "qp_url": "https://gate2027.iitm.ac.in/static/doc/download/2025/CS22025.pdf",
        "key_url": "https://gate2027.iitm.ac.in/static/doc/download/2025_Key/CS2_Keys.pdf",
        "is_free": False,
    },
    "gate_cs_pyq_2024_set2": {
        "raw_prefix": "gate_cs_2024_s2",
        "year": 2024,
        "set_label": "Set 2",
        "shift_badge": "GATE CS • 2024 Set 2 Official Paper",
        "pyq_tag": "GATE Computer Science (CS) • 2024 Set 2 Official Paper",
        "title_en": "GATE 2024 Computer Science (CS) Set 2 Official Solved Paper",
        "qp_url": "https://gate2027.iitm.ac.in/static/doc/download/2024/CS224S6.pdf",
        "key_url": "https://gate2027.iitm.ac.in/static/doc/download/2024/CS2FinalAnswerKey.pdf",
        "is_free": False,
    },
    "gate_cs_pyq_2023": {
        "raw_prefix": "gate_cs_2023",
        "year": 2023,
        "set_label": "Official",
        "shift_badge": "GATE CS • 2023 Official Paper",
        "pyq_tag": "GATE Computer Science (CS) • 2023 Official Paper",
        "title_en": "GATE 2023 Computer Science (CS) Official Solved Paper",
        "qp_url": "https://gate2027.iitm.ac.in/static/doc/download/2023/cs_2023.pdf",
        "key_url": "https://gate2027.iitm.ac.in/static/doc/download/Answer_keys2023/CS_ANS_GATE2023.pdf",
        "is_free": False,
    },
    "gate_cs_pyq_2022": {
        "raw_prefix": "gate_cs_2022",
        "year": 2022,
        "set_label": "Official",
        "shift_badge": "GATE CS • 2022 Official Paper",
        "pyq_tag": "GATE Computer Science (CS) • 2022 Official Paper",
        "title_en": "GATE 2022 Computer Science (CS) Official Solved Paper",
        "qp_url": "https://gate2027.iitm.ac.in/static/doc/download/2022/cs_2022.pdf",
        "key_url": "https://gate2027.iitm.ac.in/static/doc/download/Answer_keys2022/cs_2022.pdf",
        "is_free": False,
    },
}

# Symbol font PUA (0xF0xx) -> Unicode
SYMBOL_PUA_MAP = {
    "\uf028": "(",
    "\uf029": ")",
    "\uf02b": "+",
    "\uf02d": "-",
    "\uf03d": "=",
    "\uf03e": ">",
    "\uf050": "Π",
    "\uf057": "Ω",
    "\uf066": "φ",
    "\uf071": "θ",
    "\uf0a2": "′",
    "\uf0ae": "→",
    "\uf0b3": "≥",
    "\uf0b4": "×",
    "\uf0b7": "•",
    "\uf0b8": "÷",
    "\uf0b9": "≠",
    "\uf0c7": "∩",
    "\uf0cd": "⊆",
    "\uf0ce": "∈",
    "\uf0d7": "⋅",
    "\uf0e6": "(",
    "\uf0e7": "|",
    "\uf0e8": "(",
    "\uf0ec": "{",
    "\uf0ed": "{",
    "\uf0ee": "{",
    "\uf0f6": ")",
    "\uf0f7": "|",
    "\uf0f8": ")",
}

# CMEX10 control char glyphs -> Unicode
CMEX10_MAP = {
    "\x02": "(",
    "\x03": ")",
    "\x0a": "[",
    "\x0b": "]",
    "\x0c": "∫",
    "\x0d": "(",
    "\x0e": ")",
    "\x0f": "(",
    "\x10": ")",
}

OPT_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}


def download_pdf(url, path):
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        return True
    os.makedirs(os.path.dirname(path), exist_ok=True)
    r = requests.get(url, headers=HEADERS, timeout=45)
    if r.status_code == 200 and r.content[:4] == b"%PDF":
        with open(path, "wb") as f:
            f.write(r.content)
        return True
    raise RuntimeError(f"Failed to download {url} (HTTP {r.status_code})")


def parse_answer_key(pdf_path):
    keys = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for line in (page.extract_text() or "").splitlines():
                line = line.strip()
                m = re.match(
                    r"^(\d{1,2})\s+\d+\s+(MCQ|MSQ|NAT)\s+(GA|CS(?:-\d)?)\s+(.+?)\s+([12])$",
                    line
                )
                if m:
                    qno = int(m.group(1))
                    qtype = m.group(2)
                    sec = m.group(3)
                    ans_raw = m.group(4).strip()
                    marks = float(m.group(5))
                    neg = round(marks / 3.0, 2) if qtype == "MCQ" else 0.0
                    # Match 0.33 / 0.66 convention in gate_cs_pyq_2024_set1.json
                    if qtype == "MCQ" and marks == 2.0:
                        neg = 0.66
                    keys[qno] = {
                        "qno": qno,
                        "type": qtype,
                        "section_id": "sec_ga" if sec == "GA" else "sec_cs",
                        "section_title": "General Aptitude" if sec == "GA" else "Computer Science and Information Technology",
                        "ans_raw": ans_raw,
                        "marks": marks,
                        "neg": neg,
                    }
    if len(keys) != 65:
        raise ValueError(f"Expected 65 keys in {pdf_path}, got {len(keys)}")
    return keys


def normalize_span_text(text, font_name):
    if font_name == "CMEX10":
        out = []
        for ch in text:
            out.append(CMEX10_MAP.get(ch, ch))
        text = "".join(out)
    for k, v in SYMBOL_PUA_MAP.items():
        if k in text:
            text = text.replace(k, v)
    # Remove invisible format chars like U+2061 FUNCTION APPLICATION
    text = text.replace("\u2061", "").replace("\u200b", "").replace("\ufeff", "")
    text = unicodedata.normalize("NFKC", text)
    return text


def is_header_footer(s):
    if re.match(r"^(Organiz|Organis)ing Institute:", s):
        return True
    if re.match(r"^Page \d+ of \d+", s):
        return True
    if re.match(r"^Computer Science (&|and) Information Technology", s):
        return True
    if re.match(r"^GATE \d{4} (General Aptitude|Computer Science)", s):
        return True
    if re.match(r"^Q\.\s*\d+\s*[–-]\s*Q\.\s*\d+", s):
        return True
    if re.match(r"^(Carry (ONE|TWO) mark|Multiple (Choice|Select)|Numerical Answer)", s, re.I):
        return True
    if s in [
        "CS", "GA", "General Aptitude (GA)", "General Aptitude",
        "Computer Science & Information Technology (CS1)",
        "Computer Science & Information Technology (CS2)",
    ]:
        return True
    return False


def block_to_clean_text(block):
    lines_out = []
    for line in block.get("lines", []):
        parts = []
        for span in line.get("spans", []):
            parts.append(normalize_span_text(span.get("text", ""), span.get("font", "")))
        joined_line = "".join(parts)
        s = joined_line.strip()
        if not s or is_header_footer(s):
            continue
        lines_out.append(joined_line.rstrip())
    return "\n".join(lines_out)


def extract_questions_text(qp_pdf):
    doc = pymupdf.open(qp_pdf)
    all_pages = []
    for page in doc:
        d = page.get_text("dict")
        raw_blocks = []
        for b in d.get("blocks", []):
            if b.get("type") != 0:
                continue
            txt = block_to_clean_text(b)
            if not txt.strip():
                continue
            x0, y0, x1, y1 = b["bbox"]
            raw_blocks.append([x0, y0, x1, y1, txt])

        # Skip split range headers like "Q.1" + "– Q.5 Carry ONE mark Each"
        skip_idx = set()
        for i, b in enumerate(raw_blocks):
            t = b[4].strip()
            if re.match(r"^Q\.\s*\d+$", t):
                for j, b2 in enumerate(raw_blocks):
                    if i != j and abs(b[1] - b2[1]) < 8 and b2[0] > b[0]:
                        if re.match(r"^[–-]\s*Q\.\s*\d+", b2[4].strip()):
                            skip_idx.add(i)
                            skip_idx.add(j)

        kept = [b for i, b in enumerate(raw_blocks) if i not in skip_idx]

        def is_margin_marker(blk):
            t = blk[4].strip()
            return blk[0] < 105 and (
                bool(re.match(r"^Q\.\s*\d{1,2}$", t))
                or bool(re.match(r"^\([A-D]\)(?:\s|$)", t))
            )

        main_blocks = [b for b in kept if not is_margin_marker(b)]
        markers = [b for b in kept if is_margin_marker(b)]

        # Assign each main_block to its closest directly-overlapping marker (if any)
        marker_direct_tops = {id(m): [] for m in markers}
        unclaimed = []
        for mb in main_blocks:
            best_m = None
            best_dist = 1e9
            for mk in markers:
                ymid = (mk[1] + mk[3]) / 2.0
                if mb[1] - 4 <= ymid <= mb[3] + 4:
                    dist = abs(ymid - (mb[1] + mb[3]) / 2.0)
                    if dist < best_dist:
                        best_dist = dist
                        best_m = mk
            if best_m is not None:
                marker_direct_tops[id(best_m)].append(mb[1])
            else:
                unclaimed.append(mb)

        # Any unclaimed block within 22pt of a marker (e.g. tall fraction numerator) snaps to closest marker
        for mb in unclaimed:
            best_m = None
            best_dist = 1e9
            for mk in markers:
                ymid = (mk[1] + mk[3]) / 2.0
                if mb[1] - 22 <= ymid <= mb[3] + 22:
                    dist = abs(ymid - (mb[1] + mb[3]) / 2.0)
                    if dist < best_dist:
                        best_dist = dist
                        best_m = mk
            if best_m is not None:
                marker_direct_tops[id(best_m)].append(mb[1])

        sort_items = []
        for b in kept:
            x0, y0, x1, y1, txt = b
            sort_y = y0
            if is_margin_marker(b):
                tops = marker_direct_tops.get(id(b), [])
                if tops:
                    sort_y = min(tops) - 0.5
            elif x0 < 105 and re.match(r"^Q\.\s*\d{1,2}\b", txt.strip()):
                same_line_tops = [
                    ob[1] for ob in kept
                    if ob is not b and ob[0] > x0 and abs(ob[1] - y0) < 6.0
                ]
                if same_line_tops:
                    sort_y = min([y0] + same_line_tops) - 0.5
            sort_items.append((sort_y, x0, txt))

        sort_items.sort(key=lambda it: (round(it[0], 1), it[1]))
        all_pages.append("\n".join(it[2] for it in sort_items))

    joined = "\n".join(all_pages)
    if "\nQ. No.\nSession\n" in joined:
        joined = joined.split("\nQ. No.\nSession\n")[0]
    parts = re.split(r"(?=(?:^|\n)\s*Q\.\s*\d{1,2}\b)", joined)
    q_texts = {}
    for part in parts:
        m = re.match(r"\s*Q\.\s*(\d{1,2})\b(.*)", part, re.S)
        if m:
            qno = int(m.group(1))
            if 1 <= qno <= 65 and qno not in q_texts:
                q_texts[qno] = m.group(2).strip()
    if len(q_texts) != 65:
        raise ValueError(f"Expected 65 questions in {qp_pdf}, got {len(q_texts)}")
    return q_texts


def clean_whitespace(text):
    # Collapse excessive blank lines and trailing spaces per line
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in text.splitlines()]
    out = []
    prev_blank = False
    for ln in lines:
        if not ln:
            if not prev_blank:
                out.append("")
            prev_blank = True
        else:
            out.append(ln)
            prev_blank = False
    return "\n".join(out).strip()


def split_options(qtype, block, paper_id, qno):
    if qtype == "NAT":
        return clean_whitespace(block), []
    block_norm = re.sub(r"\(\s*([A-D])\s*\)", r"(\1)", block)
    m = re.search(
        r"(?:^|\n)\s*\(A\)\s*(.*?)\s*\n\s*\(B\)\s*(.*?)\s*\n\s*\(C\)\s*(.*?)\s*\n\s*\(D\)\s*(.*)",
        block_norm,
        re.S
    )
    if not m:
        raise ValueError(f"{paper_id} Q.{qno}: Failed to split (A)-(D) options")
    stem = clean_whitespace(block_norm[:m.start()])
    opts = []
    for i in range(1, 5):
        opt = re.sub(r"\s+", " ", m.group(i)).strip()
        if not opt:
            letter = "ABCD"[i - 1]
            opt = f"Figure ({letter}) — (Refer to official question paper)"
        opts.append(opt)
    return stem, opts


def parse_answer_fields(meta):
    qtype = meta["type"]
    ans = meta["ans_raw"]
    if qtype == "MCQ":
        if ans == "MTA":
            return {
                "correctOption": "A",
                "correctOptionsList": ["A"],
                "correct_index": 0,
                "correct_indices": [0],
                "natMin": None,
                "natMax": None,
            }
        letter = ans.strip().upper()
        idx = OPT_INDEX[letter]
        return {
            "correctOption": letter,
            "correctOptionsList": [letter],
            "correct_index": idx,
            "correct_indices": [idx],
            "natMin": None,
            "natMax": None,
        }
    elif qtype == "MSQ":
        # Handle "A, C, D or C, D" by taking first valid option list
        primary = re.split(r"\bor\b", ans, flags=re.I)[0]
        letters = [x.strip().upper() for x in re.split(r"[;,]", primary) if x.strip().upper() in OPT_INDEX]
        if not letters:
            raise ValueError(f"Q.{meta['qno']}: Could not parse MSQ key '{ans}'")
        indices = [OPT_INDEX[l] for l in letters]
        return {
            "correctOption": None,
            "correctOptionsList": letters,
            "correct_index": None,
            "correct_indices": indices,
            "natMin": None,
            "natMax": None,
        }
    elif qtype == "NAT":
        # Handle "2 to 2 OR 4 to 4" or "4.24 to 4.26" or "-60.25 to -60.25"
        primary = re.split(r"\bor\b", ans, flags=re.I)[0].strip()
        m = re.match(r"^(-?\d+(?:\.\d+)?)\s+to\s+(-?\d+(?:\.\d+)?)$", primary, re.I)
        if not m:
            raise ValueError(f"Q.{meta['qno']}: Could not parse NAT key '{ans}'")
        nmin = float(m.group(1))
        nmax = float(m.group(2))
        return {
            "correctOption": None,
            "correctOptionsList": [],
            "correct_index": None,
            "correct_indices": [],
            "natMin": nmin,
            "natMax": nmax,
        }
    raise ValueError(f"Unknown type {qtype}")


# Embedded per-question (topicTag, difficulty, explanationEn) for all 390 questions across the 6 papers
QUESTION_DETAILS = {
    # --- GATE CS 2022 ---
    "gate_cs_2022_q01": ("Verbal Aptitude — Vocabulary", "Easy", "In English usage, 'fare' refers to the price charged for a journey or service, while 'fair' means reasonable or just. Therefore, 'The fare is too high for it to be considered fair' is the only grammatically and semantically correct option."),
    "gate_cs_2022_q02": ("Quantitative Aptitude — Mensuration & Area", "Easy", "The area under the piecewise constant curve over [0, 1] is the sum of rectangular areas: 2*(1/3 - 0) + 3*(3/4 - 1/3) + 1*(1 - 3/4) = 2/3 + 3*(5/12) + 1/4 = 2/3 + 5/4 + 1/4 = 2/3 + 3/2 = 13/6."),
    "gate_cs_2022_q03": ("Quantitative Aptitude — Algebra", "Medium", "Since r^2 + 2r + 6 = 0, completing the square gives (r + 1)^2 = -5. Letting u = r + 1, we have (r+2)(r+5) = (u+1)(u+4) = u^2 + 5u + 4 = 5u - 1 and (r+3)(r+4) = (u+2)(u+3) = u^2 + 5u + 6 = 5u + 1, so their product is (5u - 1)(5u + 1) = 25u^2 - 1 = 25(-5) - 1 = -126."),
    "gate_cs_2022_q04": ("Analytical Aptitude — Logical Deduction", "Easy", "Assuming at least one student exists in the class, Statement 1 ('All students are inquisitive') and Statement 3 ('No student is inquisitive') are logical contraries. They cannot both be true at the same time."),
    "gate_cs_2022_q05": ("Spatial Aptitude — Visual Reasoning", "Medium", "Rotating the given letter plates in their plane and combining them with the additional plates in Option (B) yields a five-letter sequence that reads the same forwards and backwards. Refer to the official question paper figures to verify the exact plate orientations."),
    "gate_cs_2022_q06": ("Verbal Aptitude — Reading Comprehension", "Easy", "The passage explicitly states that in organizations with good work culture, metrics help improve outcomes, while in those with poor work culture they are counterproductive. Thus, Option (B) follows directly from the passage."),
    "gate_cs_2022_q07": ("Quantitative Aptitude — Percentages", "Easy", "Out of the total qualified candidates, girls accounted for 60%, which implies boys accounted for the remaining 40%. Since 40% < 60%, the number of boys who qualified is strictly less than the number of girls who qualified."),
    "gate_cs_2022_q08": ("Quantitative Aptitude — Probability", "Medium", "Initially there are 3 green and 2 orange balls. By the law of total probability, P(2nd is orange) = P(1st is green)*P(2nd is orange | 1st green) + P(1st is orange)*P(2nd is orange | 1st orange) = (3/5)*(2/4) + (2/5)*(2/5) = 3/10 + 4/25 = 23/50."),
    "gate_cs_2022_q09": ("Spatial Aptitude — Geometry", "Hard", "By the midpoint theorem, PR being parallel to QS implies one pair consists of the midpoints of two sides and the other consists of the corners of the third side. Since P lies on the side opposite corner T and S and U cannot share a side, P and R must be the corners on that opposite side while Q and S are the midpoints of the other two sides, so S cannot be placed at a corner."),
    "gate_cs_2022_q10": ("Spatial Aptitude — Visual Reasoning", "Medium", "To partition the grid into four plots of similar shape with ropes R1 and R2 fixed, each straight rope can connect three collinear poles. Adding 3 more straight ropes completes the required four similar regions (refer to the official grid diagram)."),
    "gate_cs_2022_q11": ("Algorithms — Asymptotic Analysis", "Easy", "If f(n) is a polynomial of degree d, then f(n) = Theta(n^d), which implies f(n^2) = Theta((n^2)^d) = Theta(n^(2d)) and (f(n))^2 = Theta((n^d)^2) = Theta(n^(2d)). Hence f(n^2) = Theta(f(n)^2) whenever f(n) is a polynomial."),
    "gate_cs_2022_q12": ("Theory of Computation — Finite Automata", "Easy", "Tracing the transitions from the start state of the given finite automaton shows it accepts zero or more repetitions of blocks ba*a or ab*b followed by a suffix matching ab* or ba*. This matches the regular expression (ba*a + ab*b)*(ab* + ba*) (refer to the official state diagram)."),
    "gate_cs_2022_q13": ("Compiler Design — Parsing", "Easy", "Every deterministic context-free language (DCFL) has an LR(1) grammar, so LR(1) parsing is sufficient to parse all DCFLs. The other statements are false: LALR(1) can introduce reduce-reduce conflicts absent in LR(1), symbol tables are used across semantic/code-gen phases too, and data flow analysis is for compile-time optimization."),
    "gate_cs_2022_q14": ("Databases — Normalization", "Easy", "In a binary relation R(A, B), the only possible non-trivial functional dependencies are A -> B or B -> A. In either case, the left-hand side is a superkey of R, guaranteeing that every 2-attribute relation is always in BCNF."),
    "gate_cs_2022_q15": ("Data Structures — Linked Lists", "Easy", "Reversing a singly linked list of n nodes requires visiting every node at least once, giving an Omega(n) lower bound. The standard iterative three-pointer algorithm reverses the list in Theta(n) worst-case time using O(1) auxiliary space."),
    "gate_cs_2022_q16": ("Data Structures — Hashing", "Easy", "With simple uniform hashing, each key—whether hashed by h1 (odd) or h2 (even)—is mapped uniformly and independently to any of the m slots with probability 1/m. By linearity of expectation over n keys, the expected number of keys in any slot is n/m."),
    "gate_cs_2022_q17": ("Computer Organization — I/O & DMA", "Easy", "Direct Memory Access (DMA) allows the disk controller to transfer blocks of data directly to main memory without CPU intervention for each word. This minimizes CPU overhead and yields the highest data transfer throughput compared to polling, programmed I/O, or interrupt-driven I/O."),
    "gate_cs_2022_q18": ("Digital Logic — Number Representation", "Easy", "In 4-bit 2's complement representation, the valid range is [-8, +7]. For R1 = 1100 (-4) and R2 = 1010 (-6), their sum is -10, which falls outside [-8, +7] and causes arithmetic underflow/overflow (while the other pairs yield -7, +7, and -8, all within range)."),
    "gate_cs_2022_q19": ("Operating Systems — Synchronization", "Medium", "To print B first, T2 must proceed first (requiring S1 = 1), after which T2 signals S3 so T1 prints C, and T1 signals S2 so T3 prints A, which then signals S1 to repeat the cycle. Thus S1 = 1, S2 = 0, S3 = 0 produces BCABCABCA...."),
    "gate_cs_2022_q20": ("Engineering Mathematics — Linear Algebra", "Easy", "For any compatible matrices A (m x n) and B (n x m), tr(AB) = sum_i sum_j A_ij B_ji = sum_j sum_i B_ji A_ij = tr(BA). The same cyclic property holds for square matrices C and D, so both Statement 1 and Statement 2 are correct."),
    "gate_cs_2022_q21": ("Programming in C — Pointers & Arrays", "Easy", "p = &x; *p = 10; updates x from 1 to 10. Next, *(&z[0] + 1) += 3 modifies z[1] from 11 to 14 while z[0] remains 10, so printf outputs '10, 10, 14'."),
    "gate_cs_2022_q22": ("Computer Networks — IP Addressing & Subnets", "Medium", "Counting the isolated broadcast domains (each Ethernet segment, point-to-point router-to-router link, and server/firewall link separated by router interfaces) in the enterprise topology gives 6 distinct subnets (refer to the official network diagram)."),
    "gate_cs_2022_q23": ("Theory of Computation — Decidability & Closure", "Medium", "If both L and its complement are recursively enumerable, L is decidable/recursive (B). Context-free languages are recursive and recursive languages are closed under complement, so the complement of a CFL is recursive (C). Regular languages are closed under intersection and every regular language is deterministic context-free (D)."),
    "gate_cs_2022_q24": ("Computer Organization — Cache Memory", "Medium", "A write-through (WT) cache immediately propagates writes to memory and does not need a dirty bit (so A is false). In a write-back (WB) cache, write hits only update the cache block and set the dirty bit without writing to memory (B is false), and a read miss can evict a dirty block (D is false)."),
    "gate_cs_2022_q25": ("Databases — Relational Algebra", "Medium", "Relational division pi_{eId, bId}(Own) / pi_{bId}(Brand) directly returns the eIds associated with every brand (A). Option (B) expresses the exact same universal quantification using difference and Cartesian product: all owners minus owners missing at least one brand."),
    "gate_cs_2022_q26": ("Operating Systems — Deadlocks", "Medium", "Circular wait is one of the four necessary Coffman conditions for deadlock (A). If every edge in a resource-allocation graph is an assignment edge (no request edges), no process is waiting on any resource, so no deadlock exists (D). With multi-instance resources a cycle is necessary but not sufficient (B false), and an unsafe state does not guarantee deadlock (C false)."),
    "gate_cs_2022_q27": ("Discrete Mathematics — Group Theory", "Medium", "If (xy)^2 = x^2 y^2 for all x, y in G, cancelling x on the left and y on the right from xyxy = xxyy yields yx = xy (A). If x^2 = 1 for all x, then (xy)^2 = 1 implies xy = (xy)^(-1) = y^(-1) x^(-1) = yx (B). Every group of prime order 2 is cyclic and hence abelian/commutative (C)."),
    "gate_cs_2022_q28": ("Data Structures — Binary Search Trees", "Medium", "In a 0-indexed complete BST with 1000 nodes, levels 0–8 hold 511 nodes (indices 0–510) and level 9 holds 489 nodes (indices 511–999, whose last parent is index 499). Hence the rightmost nodes at level 8 are leaves at indices 500–510, making index 510 the largest element, its parent 254 the 2nd largest, and the left child of 254 (index 509) the 3rd largest."),
    "gate_cs_2022_q29": ("Compiler Design — LR Parsing", "Medium", "In I0 = {[S' -> .S], [S -> .S+R]}, shifting '+' on [S -> S.+R] gives the kernel item [S -> S+.R]. Taking the closure adds [R -> .R*P], [R -> .P], [P -> .(S)], and [P -> .id], giving a total of 5 LR(0) items."),
    "gate_cs_2022_q30": ("Discrete Mathematics — Graph Theory", "Easy", "To maximize edges in a disconnected simple undirected graph on n = 10 vertices, partition the vertices into a clique of size n - 1 = 9 and an isolated vertex of size 1. This yields C(9, 2) = 9*8/2 = 36 edges."),
    "gate_cs_2022_q31": ("Databases — Functional Dependencies & Keys", "Easy", "Attributes A and B do not appear on the right-hand side of any FD, and (AB)+ = {A, B, C, D, E}, so AB is the sole candidate key. Any subset containing AB is a superkey, and there are 2^3 = 8 choices for the remaining 3 attributes {C, D, E}, giving 8 superkeys."),
    "gate_cs_2022_q32": ("Discrete Mathematics — Combinatorics", "Medium", "Arranging 6 identical balls into 3 identical bins (where bins may be empty) corresponds to the integer partitions of 6 into at most 3 parts. The partitions are (6), (5,1), (4,2), (4,1,1), (3,3), (3,2,1), and (2,2,2), giving 7 arrangements."),
    "gate_cs_2022_q33": ("Computer Organization — Cache Memory", "Easy", "Initial AMAT = 10 + (1 - 0.8)*100 = 30 ns. After optimization with hit rate h', AMAT' = 15 + (1 - h')*100 <= 30, which gives (1 - h')*100 <= 15, so 1 - h' <= 0.15 and h' >= 0.85."),
    "gate_cs_2022_q34": ("Engineering Mathematics — Calculus", "Easy", "Evaluating lim_{x->0+} x / (1 - e^(2x)) has the 0/0 indeterminate form. Applying L'Hopital's rule gives lim_{x->0+} 1 / (-2e^(2x)) = -1/2 = -0.5."),
    "gate_cs_2022_q35": ("Computer Networks — Application Layer (DNS)", "Easy", "With an empty cache and iterative DNS resolution, the local resolver sends 1 query-response pair each to the Root server, the .in TLD server, the .org.in server, and finally the authoritative server for gate.org.in. Thus 4 DNS query-response pairs are required."),
    "gate_cs_2022_q36": ("Discrete Mathematics — Generating Functions", "Hard", "Writing a_n = 1 + b_n where b_n = n for odd n and 0 for even n, the constant 1 terms sum to 1/(1 - x). The odd-indexed terms give x + 3x^3 + 5x^5 + ... = x(1 + x^2)/(1 - x^2)^2, yielding the generating function in Option (A)."),
    "gate_cs_2022_q37": ("Discrete Mathematics — Graph Theory", "Medium", "In the adjacency matrix A of a simple undirected graph, the (i, i) diagonal entry of A^3 counts closed walks of length 3 starting and ending at vertex i. Each 3-cycle (triangle) has 3 vertices and 2 orientations per vertex, so it is counted 6 times in tr(A^3), giving tr(A^3)/6."),
    "gate_cs_2022_q38": ("Operating Systems — Virtual Memory", "Medium", "In an inverted page table, virtual addresses are typically looked up via hashing with chaining (or linear probing) rather than direct indexing, so collisions cause varying traversal lengths. Therefore, the claim that memory access time is always the same for all incoming virtual addresses (Option C) is false."),
    "gate_cs_2022_q39": ("Databases — Transactions & Concurrency", "Medium", "Tracing conflicting operations in S: R4(x) precedes W2(x) (T4 -> T2), W1(y) precedes W3(y) and R4(y) (T1 -> T3, T1 -> T4), and W3(y) precedes R4(y) (T3 -> T4). Together these precedence edges form the unique topological order T1 -> T3 -> T4 -> T2."),
    "gate_cs_2022_q40": ("Digital Logic — Combinational Circuits", "Medium", "To address 1024 = 2^10 words in memory S and 32 = 2^5 words in register file R, P must be a 10:2^10 decoder and Q must be a 5:2^5 decoder. T uses the 1-bit mode M to choose between the output from S and the output from R, making T a 2:1 multiplexer."),
    "gate_cs_2022_q41": ("Digital Logic — Floating Point Representation", "Medium", "Decoding IEEE-754 single precision: RA = 0xC1400000 gives -12.0, RB = 0x42100000 gives +36.0, and RC = 0x41400000 gives +12.0. Then A + C = 0, B = 3C, and B - C = 24 > 0 are true, whereas C = A + B (-12 + 36 = 24 != 12) is FALSE."),
    "gate_cs_2022_q42": ("Operating Systems — CPU Scheduling", "Hard", "With quantum q = 4 and arrival order P, Q, R, S at t = 0: P must finish in its first quantum (P <= 4) since there is no switch from S to P. For Option (D) (P=3, Q=7, R=7, S=3), the round-robin trace is P(3)->Q(4)->R(4)->S(3)->Q(3)->R(3), which has only one switch from Q to R (after S finishes, Q runs and switches to R once, then R finishes), violating the requirement of two switches from Q to R."),
    "gate_cs_2022_q43": ("Programming in C — Arrays", "Medium", "In a[3][3][3], each 2D slice a[i] has 9 elements (3 rows of 3). Because j stays 0 while i and k iterate from 0 to 2, a[i][0][k] prints the first row of each slice: 1 2 3, 10 11 12, and 19 20 21."),
    "gate_cs_2022_q44": ("Programming in C — Bitwise Operators", "Medium", "ASCII values are 'P'=80 (01010000), 'x'=120 (01111000), '*'=42, '-'=45, '+'=43. Computing bitwise ops: (80 & 120)+42 = 80+42 = 122 ('z'), (80 | 120)-45 = 120-45 = 75 ('K'), and (80 ^ 120)+43 = 40+43 = 83 ('S'), printing 'z K S'."),
    "gate_cs_2022_q45": ("Engineering Mathematics — Linear Algebra", "Medium", "Performing LU decomposition on [[1,1,-2],[1,3,-1],[2,1,-5]] (with L_ii = 1 or matching standard Doolittle factorization where L_11=L_22=L_33=1): U_11=1, U_12=1, U_13=-2; L_21=1, U_22=2, U_23=1; L_31=2, L_32=-1/2, and U_33 = -5 - 2*(-2) - (-1/2)*1 = -1/2. Back-substitution with [4,7,7]^T yields x_3 = 1, x_2 = 3, and x_1 = 0."),
    "gate_cs_2022_q46": ("Theory of Computation — Decidability", "Hard", "By Rice's theorem and reductions from the Halting Problem, equivalence of two TMs (A), whether L(M) is regular (B), and whether L(M) = Sigma* (C) are all undecidable. Option (D) is decidable because it suffices to simulate M for up to 1074 steps on all strings of length <= 1074 (since M can inspect at most 1074 tape cells in 1073 steps)."),
    "gate_cs_2022_q47": ("Theory of Computation — Formal Languages", "Medium", "For L1 = {a^n w a^n | w in {a,b}*}, taking n = 0 yields a^0 w a^0 = w for any w in {a,b}*, so L1 = {a,b}*, which is regular. Similarly, for L2 = {w x w^R | |w|, |x| > 0}, choosing |w| = 1 yields {a x a, b x b | |x| > 0}, which is also regular. Since every regular language is context-free, Options (A), (B), and (C) are all TRUE."),
    "gate_cs_2022_q48": ("Theory of Computation — Context-Free Languages", "Medium", "L1 = {ww} is well-known to be non-context-free, while L2 = {a^n b^n c^m} and L3 = {a^m b^n c^n} are both deterministic context-free (so A is true). Hence B ('Neither L1 nor L2 is CFL') is FALSE; C is FALSE because L2 intersect L3 = {a^n b^n c^n} is not CFL; and D is FALSE because the complement of {ww} IS context-free."),
    "gate_cs_2022_q49": ("Algorithms — Minimum Spanning Trees", "Hard", "Because all edge weights are distinct, G has a unique MST (so D is false). By the cut property (C), every minimum-weight edge crossing any non-trivial cut belongs to the MST. In Kruskal's algorithm, the smallest and second-smallest edges can never form a cycle, so both are in the MST (A), and among the 3rd and 4th smallest edges at most one can close a triangle with the first two, so at least one must be in the MST (B)."),
    "gate_cs_2022_q50": ("Discrete Mathematics — Graph Theory", "Hard", "The Petersen graph is 3-colorable (chromatic number 3, A), has a Hamiltonian path though no Hamiltonian cycle (B), and is isomorphic to the depicted 10-vertex cubic graph (C). Its maximum independent set size is 4 (not 3), making Option (D) false."),
    "gate_cs_2022_q51": ("Algorithms — Recurrence Relations", "Hard", "Computing small values from f(1) = 1, f(2n) = 2f(n) - 1, f(2n+1) = 2f(n) + 1 gives f(2^n) = 1 (B), f(2^n - 1) = 2^n - 1 (A), and f(5 * 2^n) = 2^(n+1) + 1 (C; e.g., f(5) = 3, f(10) = 5, f(20) = 9). Option (D) fails at n = 2 since f(5) = 3 != 5."),
    "gate_cs_2022_q52": ("Discrete Mathematics — Graph Theory", "Hard", "Entry (i, i) of A^2 counts walks of length 2 from vertex i back to i, which equals the degree of vertex i (A). Option (B) is false because (A + I_n)^(n-1) rather than A^(n-1) + I_n has all nonzero entries for connected graphs (e.g., for P3, A^2 + I_3 has zeros at (1, 2)); (C) fails when a graph has a cycle and an isolated vertex; and (D) fails for two disjoint edges."),
    "gate_cs_2022_q53": ("Engineering Mathematics — Linear Algebra", "Medium", "Multiplying the 4x4 matrix A by each vector: for v_A = [-1, 1, 0, 1]^T, Av_A = [-1, 1, 0, 1]^T = 1*v_A; for v_C = [-1, 0, 2, 2]^T, Av_C = [-3, 0, 6, 6]^T = 3*v_C; for v_D = [0, 1, -3, 0]^T, Av_D = [0, 3, -9, 0]^T = 3*v_D. Only Option (B) fails Av = lambda*v."),
    "gate_cs_2022_q54": ("Computer Organization — Cache Memory", "Hard", "With a 2 KB direct-mapped cache and 64-byte blocks, there are 32 blocks (5 index bits, 6 offset bits, 5 tag bits). P (0xA248) and S (0xA262) share the same block (bits [15:6] are identical: 0xA240..0xA27F), so every access to S hits after P loads the block (A) and P's block at index 9 is never evicted (B). Q (0xC28A) and R (0xCA8A) map to the same index 2 with different tags, so R evicts Q on every iteration (D)."),
    "gate_cs_2022_q55": ("Computer Networks — IP Addressing & Subnets", "Medium", "Look at the four subnet blocks: 12.20.164.0/22 covers 12.20.164.0–12.20.167.255 (which already includes 12.20.166.0/23), while 12.20.168.0/22 covers 12.20.168.0–12.20.171.255 (which includes both 12.20.168.0/23 and 12.20.170.0/23). Thus 12.20.164.0/22 and 12.20.168.0/22 collectively aggregate all listed subnets."),
    "gate_cs_2022_q56": ("Databases — SQL", "Hard", "This SQL query uses relational division via double negation (NOT EXISTS ... EXCEPT ...): it returns all students who have registered for EVERY course offered by department 'D01'. Evaluating against the table instances in the official paper yields 2 matching student rows."),
    "gate_cs_2022_q57": ("Computer Networks — Routing Protocols", "Hard", "After Q-R fails, Q knows its distance to R is infinity, while P still has distance 2 to R via Q. If P sends its update first (probability 1/2 since both send at the same average rate), Q adopts P's stale route to R with cost 3, forming a routing loop (count-to-infinity); if Q sends first, P updates to infinity and no loop forms. Hence the probability is 0.5."),
    "gate_cs_2022_q58": ("Discrete Mathematics — Graph Theory", "Hard", "From A[i][j] = 1 for 1 <= j <= i <= 5, vertex i has directed edges to every j < i (a transitive tournament DAG). Any spanning tree rooted at vertex 5 can choose each vertex k in {1, 2, 3, 4} to have its single incoming edge from any vertex in {k+1, ..., 5}, giving 4 * 3 * 2 * 1 = 24 directed spanning trees."),
    "gate_cs_2022_q59": ("Computer Networks — Data Link & Delays", "Medium", "Propagation delay = (2100 * 10^3 m) / (3 * 10^8 m/s) = 7 ms. Transmission time = (1000 * 8 bits) / (100 * 10^6 bps) = 0.08 ms. Total time for the receiver to completely receive the packet = 7 + 0.08 = 7.08 ms."),
    "gate_cs_2022_q60": ("Computer Networks — Transport Layer (TCP)", "Medium", "At 1 Gbps = 125 MB/s, over MSL = 60 s the sender can transmit 125 * 10^6 * 60 = 7.5 * 10^9 bytes. To assign unique byte sequence numbers without wrap-around, we need 2^n >= 7.5 * 10^9, which gives n = ceil(log2(7.5 * 10^9)) = 33 bits."),
    "gate_cs_2022_q61": ("Computer Organization — Pipelining", "Medium", "For X1, CPI = 1 + 0.30 * 2 = 1.60. For X2, only the 20% mispredicted branches incur the 2-cycle stall, so CPI_2 = 1 + 0.30 * 0.20 * 2 = 1.12. Since clock frequency is unchanged, speedup = 1.60 / 1.12 = 1.4286 (in range 1.42 to 1.45)."),
    "gate_cs_2022_q62": ("Data Structures — Queues", "Medium", "In the official figure for this question, the front/rear orientation of Q2 in the final state matches dequeuing directly from Q1 into Q2 without needing any Enqueue operation back onto Q1 (refer to the official question paper diagram). Thus 0 Enqueue operations on Q1 are required."),
    "gate_cs_2022_q63": ("Operating Systems — File Systems", "Hard", "In contiguous allocation (A), inserting between block 50 and 51 shifts blocks 51..100 right by 1 position (50 reads + 50 writes = 100 accesses) and writes the new block 51 (1 write), giving n_A = 101. In linked allocation (B), we traverse blocks 1..50 (50 reads), write the new block pointing to block 51 (1 write), and update block 50's next pointer (1 write), giving n_B = 52. Thus n_A + n_B = 101 + 52 = 153."),
    "gate_cs_2022_q64": ("Operating Systems — Virtual Memory", "Medium", "Simulating LRU with 4 frames on the 15-reference string 7,2,7,3,2,5,3,4,6,7,7,1,5,6,1 causes page faults at references 7, 2, 3, 5, 4, 6, 7, 1, 5 (9 faults in total). The page fault rate is 9 / 15 = 0.6."),
    "gate_cs_2022_q65": ("Compiler Design — Syntax Directed Translation", "Medium", "The grammar gives left-associative '#' (multiplication) lower precedence than left-associative '%' (integer division). Evaluating 20 # (10 % 5) # ((8 % 2) % 2) yields 20 * (10 / 5) * ((8 / 2) / 2) = 20 * 2 * (4 / 2) = 20 * 2 * 2 = 80."),

    # --- GATE CS 2023 ---
    "gate_cs_2023_q01": ("Verbal Aptitude — Grammar", "Easy", "In the context of 'reached the station late, and _______ missed the train', an adverb modifying the verb 'missed' is required. 'Nearly' means almost, fitting the sentence naturally, whereas 'near' is an adjective/preposition."),
    "gate_cs_2023_q02": ("Verbal Aptitude — Analogy", "Easy", "'Often' and 'Frequently' are synonyms. Among the options for 'Kind', 'Mean' (Option A) is the intended answer in the initial key, though IIT Kanpur awarded Marks to All (MTA) due to ambiguity between synonym ('Type') and antonym ('Mean'/'Cruel')."),
    "gate_cs_2023_q03": ("Quantitative Aptitude — Number Series", "Easy", "Working backwards from F7 = 60 and F6 = 37 using Fn-1 = Fn+1 - Fn: F5 = 60 - 37 = 23, F4 = 37 - 23 = 14, F3 = 23 - 14 = 9, F2 = 14 - 9 = 5, and F1 = 9 - 5 = 4."),
    "gate_cs_2023_q04": ("Quantitative Aptitude — Percentages", "Easy", "Of the 90% of pregnant women who received medical care at least once, 60% received care from doctors. That amounts to 0.60 * 0.90 = 54% of all pregnant women, which is strictly more than half."),
    "gate_cs_2023_q05": ("Spatial Aptitude — 3D Geometry", "Medium", "A smooth 3-dimensional object (such as a torus or a dumbbell) need not be everywhere convex or everywhere concave. Its surface can be concave in some regions and convex in other regions."),
    "gate_cs_2023_q06": ("Verbal Aptitude — Critical Reasoning", "Easy", "Since experts identified lack of physical exercise as a leading cause of health issues and the government responded by incentivizing riding bicycles to work, the government clearly assumes that riding bicycles is a form of physical exercise."),
    "gate_cs_2023_q07": ("Quantitative Aptitude — Functions & Inequalities", "Medium", "At t = 1, g(1) = 4 > f(1) = 0.01, so (i) holds. For t > 400, 0.01*t^2 > 4t (since 0.01*t > 4), so f(t) > g(t) for all t > T = 400, making (ii) true as well."),
    "gate_cs_2023_q08": ("Verbal Aptitude — Para Jumbles", "Medium", "Mina first carries heavy bags from the market (iii), climbs the stairs and begins to pant (ii), reaches the terrace and notices the man (i), who is then described leaning against the parapet (iv). This gives the coherent sequence (iii), (ii), (i), (iv)."),
    "gate_cs_2023_q09": ("Quantitative Aptitude — Functions", "Easy", "Since f(x) depends only on x and g(y) depends only on y, f(x) = g(y) can hold for all real x and y only if both functions equal the same constant value for every input."),
    "gate_cs_2023_q10": ("Spatial Aptitude — Transformations", "Medium", "Rotating figure P clockwise by 90 degrees in the plane produces figure Q, and reflecting figure Q across a horizontal axis produces figure R (refer to the official transformation diagram)."),
    "gate_cs_2023_q11": ("Compiler Design — Compiler Phases", "Easy", "A compiler's front-end (lexical, syntax, semantic analysis, IR generation) depends on the source language and is target-independent (S1 true), while the back-end (code generation, target optimization) depends on the target hardware (S2 true) and is source-language independent (S3 false)."),
    "gate_cs_2023_q12": ("Data Structures — Heaps", "Easy", "In a 1-indexed max-heap, every parent A[i] must satisfy A[i] >= A[2i] and A[i] >= A[2i+1]. Option (B) satisfies all parent-child constraints, whereas (A) fails at A[3]=10 < A[6]=14, (C) fails at A[5]=13 < A[10]=15, and (D) fails at A[4]=1 < A[8]=12."),
    "gate_cs_2023_q13": ("Data Structures — Linked Lists", "Easy", "Deleting a node given only its pointer in a singly-linked list requires finding its predecessor by traversing from head in O(n) worst-case time (unless it's not the tail and data-copy trick is disallowed/tail is deleted). In a doubly-linked list, the prev pointer is directly available, allowing O(1) deletion."),
    "gate_cs_2023_q14": ("Theory of Computation — Finite Automata", "Easy", "From start state s, reading '1' reaches the unique accepting state p (and '0' goes to trap state r). From p, reading '0' stays in p, while '1' moves to q from which another '1' returns to p (and '0' goes to r), giving the regular expression 1(0 + 11)*."),
    "gate_cs_2023_q15": ("Discrete Mathematics — Recurrence Relations", "Medium", "The characteristic equation of Ln = Ln-1 + Ln-2 is r^2 - r - 1 = 0, with roots phi = (1 + sqrt(5))/2 and psi = (1 - sqrt(5))/2. Matching L1 = 1 and L2 = 3 gives Ln = phi^n + psi^n = ((1 + sqrt(5))/2)^n + ((1 - sqrt(5))/2)^n."),
    "gate_cs_2023_q16": ("Databases — Relational Model", "Easy", "In the relational database model, the degree (or arity) of a relation is defined as the number of attributes (columns) in its relation schema. The number of tuples is its cardinality."),
    "gate_cs_2023_q17": ("Computer Networks — Data Link Layer", "Easy", "Stop-and-Wait utilization is U = 1 / (1 + 2a), where a = T_prop / T_trans = (length / speed) * (bandwidth / frame_size). Increasing link length and increasing transmission rate both maximize a, resulting in the lowest utilization."),
    "gate_cs_2023_q18": ("Engineering Mathematics — Linear Algebra", "Easy", "Observe that matrix B is obtained from matrix A by swapping Row 1 with Row 3 (1 row swap). Since swapping two rows of a matrix negates its determinant, det(B) = -det(A)."),
    "gate_cs_2023_q19": ("Theory of Computation — Regular Expressions", "Easy", "The regex letter(letter | digit)* requires at least one letter followed by zero or more letters or digits. The epsilon-NFA in Option (C) enforces an initial letter transition before entering an accepting loop over letter or digit (refer to the official NFA diagrams)."),
    "gate_cs_2023_q20": ("Algorithms — Hashing", "Medium", "When an adversary chooses keys specifically to cause collisions against a fixed deterministic hash function, universal hashing picks a hash function uniformly at random from a universal family at runtime. This prevents the adversary from forcing worst-case collisions and guarantees O(1) expected lookup/insertion."),
    "gate_cs_2023_q21": ("Digital Logic — Sequential Circuits", "Medium", "In the 2-to-1 MUX, select S chooses input 0 (fed back from output Q) when S = 0, holding Q, and chooses input 1 (D) when S = 1, passing D to Q. Because it is level-sensitive to S rather than edge-triggered, it behaves as a transparent D Latch."),
    "gate_cs_2023_q22": ("Operating Systems — Threads & Processes", "Easy", "Threads within the same process share the same virtual address space (hence the same page table base register), while each thread maintains its own execution context. Therefore, the stack pointer, program counter, and general purpose registers must be saved on a thread context switch."),
    "gate_cs_2023_q23": ("Operating Systems — OS Basics & Traps", "Medium", "A page fault is a hardware trap handled by the OS kernel, and a system call invokes a software trap to request an OS service; both force a transition from user mode to kernel mode. A normal function call stays in user mode, and malloc() may be served from user-space heap free lists without a system call."),
    "gate_cs_2023_q24": ("Theory of Computation — Closure Properties", "Easy", "Regular, recursive, and recursively enumerable languages are all closed under intersection (A, C, D). Context-free languages are NOT closed under intersection (e.g., {a^n b^n c^m} intersect {a^m b^n c^n} = {a^n b^n c^n} is not CFL), so (B) is false."),
    "gate_cs_2023_q25": ("Computer Networks — Routing Protocols", "Medium", "OSPF is an intra-domain (interior gateway) link-state routing protocol that uses Dijkstra's algorithm and supports hierarchical areas. Thus claiming it uses Bellman-Ford (A) or is an inter-domain protocol (C) is incorrect."),
    "gate_cs_2023_q26": ("Discrete Mathematics — Predicate Logic", "Medium", "Geetha's conjecture is forall x (P(x) => exists y Q(x, y)). If forall x forall y Q(x, y) holds, the consequent is always true for any y, implying the conjecture (B). Similarly, if exists y forall x (P(x) => Q(x, y)) holds, the same witness y works for every x, which is stronger than letting y depend on x (C)."),
    "gate_cs_2023_q27": ("Operating Systems — CPU Scheduling", "Medium", "Priority Scheduling and Shortest Job First can starve low-priority or long jobs indefinitely if higher-priority/shorter jobs keep arriving (C, D). Official IITK key also accepts (A, C, D) since FIFO can starve later processes if a process never yields or has infinite CPU burst."),
    "gate_cs_2023_q28": ("Engineering Mathematics — Calculus", "Medium", "Taking the derivative f'(x) = 3x^2 + 30x - 33 = 3(x + 11)(x - 1) gives critical points x = -11 and x = 1. Since f''(x) = 6x + 30, f''(-11) = -36 < 0 (local maximum) and f''(1) = 36 > 0 (local minimum), so both B and D are true."),
    "gate_cs_2023_q29": ("Algorithms — Asymptotic Analysis", "Easy", "Since f(n) = n and g(n) = n^2, lim_{n->inf} f(n)/g(n) = lim_{n->inf} 1/n = 0. Therefore f grows strictly slower than g, meaning f in o(g) and consequently f in O(g)."),
    "gate_cs_2023_q30": ("Engineering Mathematics — Linear Algebra", "Medium", "The sum of the eigenvalues of a matrix equals its trace (the sum of its diagonal entries, i.e., self-loops in the adjacency matrix). Counting the self-loops in the official graph diagram gives trace = 2 (or 4 depending on loop interpretation; official key accepts 2 or 4)."),
    "gate_cs_2023_q31": ("Engineering Mathematics — Calculus", "Easy", "Notice the integration limits for x, y, and z are symmetric around 0: [-3, 3], [-2, 2], and [-1, 1]. Because 4x^2 y is an odd function of y and -z^3 is an odd function of z, both integrals over symmetric intervals evaluate to 0."),
    "gate_cs_2023_q32": ("Digital Logic — Number Systems", "Easy", "Converting (132)_4 to decimal gives 1*16 + 3*4 + 2 = 30. Converting 30 to base 5: 30 = 1*25 + 1*5 + 0, which is 110 in radix-5."),
    "gate_cs_2023_q33": ("Computer Organization — Pipelining", "Easy", "The pipeline clock cycle time is max(10, 20, 14) = 20 ns. Executing n = 100 instructions in a k = 3 stage pipeline with no hazards takes (k + n - 1) * T_clk = (3 + 100 - 1) * 20 ns = 102 * 20 = 2040 ns."),
    "gate_cs_2023_q34": ("Computer Organization — I/O Organization", "Medium", "Polling every 10 ms yields 100 polls/sec, spending 100 * 100 us = 10,000 us = 10 ms, plus 200 us = 0.2 ms to process the single keystroke per second, giving T1 = 10.2 ms/s = 0.0102. Interrupt-driven I/O spends T2 = 1 ms/s = 0.001, so T1 / T2 = 10.2."),
    "gate_cs_2023_q35": ("Programming in C — Storage Classes", "Easy", "In funcp(), x is static and initialized once to 1. The first call increments it and returns 2 (main's x = 2); the second call increments it from 2 to 3 and returns 3, so y = 3 + 2 = 5 and printf prints x + y = 2 + 5 = 7."),
    "gate_cs_2023_q36": ("Programming in C — Recursion & Functions", "Medium", "main() calls f1(), which calls f2(2) and then f3(). f2(2) calls f3() and recursively calls f2(1) (which also calls f3() before returning 5), and finally f1()'s second direct call to f3() runs, matching the activation tree in Option (A)."),
    "gate_cs_2023_q37": ("Compiler Design — Data Flow Analysis", "Hard", "Tracing backwards from EXIT (where live variables or loop back-edges preserve {a, i, j}): B4 uses a and defines i, B3 defines a and branches back to B2/B4 (keeping j live along loop), and B1 initializes i, j, a before entering the loop. Matching the exact CFG edges in the diagram yields Option (D)."),
    "gate_cs_2023_q38": ("Operating Systems — Synchronization", "Hard", "With binary semaphore s = 1 (I-1), all increments and decrements are mutually exclusive, so X always ends at 10 + 5 - 3 = 12. With counting semaphore s = 2 (I-2), two threads can race simultaneously; the minimum final value occurs when 1 decr overlaps with 1 incr/other threads so all 5 increments are lost in overwrites while 3 decrements take effect: 10 - 3 = 7."),
    "gate_cs_2023_q39": ("Theory of Computation — Context-Free Grammars", "Medium", "From X -> aX | Xb | a | b, X generates all strings in a*(a + b)b* (every string has at least one a or b, with a's before and b's after). Wrapping X in S -> aSb | X still only adds matching a's on the left and b's on the right, so L(G) = a*(a + b)b*, which is regular."),
    "gate_cs_2023_q40": ("Theory of Computation — Pushdown Automata", "Hard", "Starting from s, the PDA pushes at least one 'A' onto the bottom marker while reading m >= 1 'a's, then either skips directly to q to pop all A's and bottom marker via epsilon transitions (n = 0 < m), or moves to p on 'b' to pop one A per 'b' and then transitions to q before the stack is empty (leaving at least one A to pop via epsilon in q, so n < m). Thus it accepts {a^m b^n | 1 <= m and n < m}."),
    "gate_cs_2023_q41": ("Computer Organization — Assembly & Addressing", "Medium", "To multiply b[i] by 8, we shift left by 3 bits (U1 = 3). Since ints are 32-bit (4 bytes) in byte-addressable memory, array pointers r3 and r4 must advance by 4 each iteration (U2 = 4, U3 = 4), and the loop jumps back to the condition check at L01 (U4 = L01)."),
    "gate_cs_2023_q42": ("Computer Organization — Memory Interfacing", "Hard", "The 10-bit address port uses IA11..IA5 and IA2..IA0, while IA4 and IA3 drive the 2:4 decoder for the four 1 KB blocks. Setting the 10-bit block address to 0 and varying (IA4, IA3) through 00, 01, 10, 11 gives 12-bit addresses 0, 8 (2^3), 16 (2^4), and 24 (2^4 + 2^3)."),
    "gate_cs_2023_q43": ("Digital Logic — Sequential Circuits", "Hard", "Initially (Q1, Q2, Q3) = (0, 1, 1). Inspecting the next-state transitions from (0, 1, 1) across clock cycles shows the state (0, 0, 1) is unreachable from the initial state (refer to the official flip-flop wiring diagram)."),
    "gate_cs_2023_q44": ("Digital Logic — Combinational Circuits", "Hard", "Expanding the Boolean function F(A, B, C) = A + A.C + A.B.C (with any complements shown in the printed PDF expression) into minterms and matching M1 (when B=0) and M2 (when B=1) with select lines (S1, S0) = (A, C) gives (X0..X7) = (1, 1, 0, 1, 1, 1, 0, 0)."),
    "gate_cs_2023_q45": ("Digital Logic — Floating Point Representation", "Medium", "P = 0xC1800000 has sign 1 (-), biased exponent 131 (unbiased +3), and mantissa 1.0, so P = -8.0 = -2^3. Multiplying by Q = 0x3F5C2EF4 (sign 0, biased exponent 126, unbiased -1) flips the sign to 1 and adds +3 to the exponent (126 + 3 = 129), keeping the mantissa unchanged and yielding 0xC15C2EF4."),
    "gate_cs_2023_q46": ("Data Structures — Heaps", "Easy", "In a binary max-heap with n elements, its height is O(log n). Extract-Max removes the root and sifts down in O(log n) worst-case time, and Insert appends at the end and sifts up in O(log n) worst-case time."),
    "gate_cs_2023_q47": ("Data Structures — Trees", "Medium", "foo() computes and prints the sum of values in each subtree in post-order (left, right, root). For the given tree: leaf 3 prints 3, leaf 8 prints 8, node 5 prints 5+3+8 = 16, leaf 13 prints 13, node 11 prints 11+13 = 24, and root 10 prints 10+16+24 = 50, giving '3 8 16 13 24 50'."),
    "gate_cs_2023_q48": ("Discrete Mathematics — Combinatorics", "Hard", "Choose 2k positions out of n for the elements of A union B in C(n, 2k) ways, and arrange the remaining n - 2k elements in (n - 2k)! ways. In those 2k positions, either all of A occupy the first k positions and B the last k, or vice versa (2 choices), with k! arrangements each, giving 2 * C(n, 2k) * (n - 2k)! * (k!)^2."),
    "gate_cs_2023_q49": ("Discrete Mathematics — Sets & Relations", "Medium", "If [x1] = [x2], then f(x1) = f(x2), so F([x]) = f(x) is well-defined (A false). Since f is onto B, F is onto (B); since F([x1]) = F([x2]) implies x1 ~ x2 and [x1] = [x2], F is one-to-one (C), and therefore F is a bijection (D)."),
    "gate_cs_2023_q50": ("Computer Networks — Transport Layer (TCP)", "Medium", "At 100 Mbps = 12.5 * 10^6 B/s over MSL = 120 s, up to 1.5 * 10^9 bytes can be transmitted before wrap-around. Since 2^30 = 1.07 * 10^9 < 1.5 * 10^9 <= 2^31, at least 31 bits are needed, making 32, 34, and 36 bits valid lengths."),
    "gate_cs_2023_q51": ("Discrete Mathematics — Group Theory", "Medium", "Symmetric difference Delta on the powerset 2^X is associative, commutative, has the empty set as identity, and satisfies A Delta A = empty set for every A in 2^X. Thus H is a group (A) and every element is its own inverse (D)."),
    "gate_cs_2023_q52": ("Computer Networks — Application Layer (HTTP/DNS)", "Hard", "Iterative lookup over the 3-tier DNS hierarchy takes 3 RTTs, and fetching the base HTML takes 1 RTT (TCP) + 1 RTT (GET) = 2 RTTs. With persistent HTTP and pipelining, all 10 objects arrive in 1 more RTT (total 6 RTTs, D); with non-persistent HTTP and 5 parallel TCP connections, 2 batches of 5 objects take 2 * 2 = 4 RTTs (total 9 RTTs, C)."),
    "gate_cs_2023_q53": ("Engineering Mathematics — Probability", "Medium", "The first and second coin tosses are independent, so B and C are independent (C) and consequently P(B|C) = P(B) (D). However, A = B intersect C has P(A) = 1/4 while P(A|B) = 1/2 != 1/4, so A is dependent on both B and C."),
    "gate_cs_2023_q54": ("Algorithms — Time Complexity", "Medium", "In Function 1, the inner loop runs n + floor(n/2) + floor(n/4) + ... <= 2n times, so f1(n) = Theta(n) and f1(n) in O(n) (D). Function 2 executes the statement exactly 100n = Theta(n) times, so f1(n) in Theta(f2(n)) (A)."),
    "gate_cs_2023_q55": ("Algorithms — Graph Algorithms", "Medium", "Greedy coloring assigns each vertex a color distinct from all already-colored neighbors, always yielding a proper vertex coloring (A). Because each vertex has at most Delta(G) neighbors, at least one color in {1, ..., Delta(G) + 1} is always available, bounding the colors used by Delta(G) + 1 (B)."),
    "gate_cs_2023_q56": ("Algorithms — Graph Traversal (BFS)", "Hard", "Because the empty set is a proper subset of every non-empty subset in 2^U, it is adjacent to all 7 other vertices in G. Therefore, a BFS starting at empty set discovers all 7 vertices at level 1 and can visit them in any of the 7! = 5040 permutations."),
    "gate_cs_2023_q57": ("Operating Systems — Virtual Memory", "Hard", "The 128 x 128 array has 16,384 integers, occupying 16,384 / 512 = 32 pages (each row of 128 ints is 1/4 of a page, so 4 rows fit per page). Since the loop accesses column-by-column across all 32 pages sequentially with only 30 frames under LRU, every access to a new page evicts the oldest page; each of the 128 columns touches all 32 pages, causing 128 * 32 = 4096 page faults."),
    "gate_cs_2023_q58": ("Operating Systems — Virtual Memory", "Medium", "With 4 KB = 2^12 byte pages, the page offset is 12 bits, leaving 57 - 12 = 45 bits for virtual page indexing. Each page holds 4096 / 8 = 512 = 2^9 PTEs (9 bits per level), so L = 45 / 9 = 5 levels are required."),
    "gate_cs_2023_q59": ("Data Structures — Stacks & Queues", "Medium", "After I & II: S (top->bottom) = [2,9,8,7,5,1], Q (front->rear) = [1,5,7,8,9,2]. After III–VI (2 pops from S, 2 dequeues from Q): S = [8,7,5,1], Q = [7,8,9,2]. Operations VII–VIII dequeue 7, 8, 9, 2 and push them onto S giving S = [2,9,8,7,8,7,5,1], and IX–X pop 2 and 9, leaving 8 at the top of S."),
    "gate_cs_2023_q60": ("Compiler Design — Syntax Directed Translation", "Medium", "The grammar evaluates binary numbers separated by '#': I evaluates the integer part (10)_2 = 2, and F evaluates the fractional part (.011)_2 = 0*2^(-1) + 1*2^(-2) + 1*2^(-3) = 0.25 + 0.125 = 0.375. Thus N.val = 2 + 0.375 = 2.375."),
    "gate_cs_2023_q61": ("Databases — SQL", "Easy", "Scanning the Student table for rows with gender = 'F' and marks > 65 matches rollNum 2 (Aliya, F, 70) and rollNum 3 (Aliya, F, 80), while rollNum 5 has marks = 65 (not strictly > 65). Hence 2 rows are returned."),
    "gate_cs_2023_q62": ("Databases — File Organization & Indexing", "Medium", "Each data block holds floor(1024 / 100) = 10 records, so 25,000 records span 25,000 / 10 = 2,500 data blocks, giving 2,500 primary index entries. Each index entry is 15 + 5 = 20 bytes, so each index block holds floor(1024 / 20) = 51 entries, requiring ceil(2500 / 51) = 50 index blocks. Binary search on 50 index blocks takes ceil(log2(50)) = 6 block accesses."),
    "gate_cs_2023_q63": ("Theory of Computation — Finite Automata", "Easy", "To reject strings with three or more consecutive 1's, the DFA needs to track the length of the current trailing run of 1's: 0 ones (q0), 1 one (q1), 2 ones (q2)—all accepting—plus a non-accepting trap state q3 for >= 3 consecutive 1's. Thus the minimal DFA has 4 states."),
    "gate_cs_2023_q64": ("Computer Organization — Cache Memory", "Medium", "In a 64 KB = 2^16 byte, 8-way set-associative cache, each way has size 64 KB / 8 = 8 KB = 2^13 bytes. Regardless of block size, the combined (INDEX + BLOCK OFFSET) bits equal log2(8 KB) = 13 bits, leaving 32 - 13 = 19 bits for the TAG field."),
    "gate_cs_2023_q65": ("Computer Networks — IP Addressing & Routing", "Medium", "Testing destination 200.150.68.118 against each entry: it matches 200.150.0.0/16 (Interface 1), 200.150.64.0/19 (64..95, Interface 2), and 200.150.68.0/24 (Interface 3), but NOT 200.150.68.64/27 (64..95, whereas 118 > 95). By longest prefix matching (/24 > /19 > /16), it is forwarded to Interface 3."),

    # --- GATE CS 2024 Set 2 ---
    "gate_cs_2024_s2_q01": ("Verbal Aptitude — Vocabulary", "Easy", "In '[walk -> jog -> sprint]', the words progress from mild to moderate to intense action. Similarly, 'bothered -> fazed -> daunted' shows increasing levels of disturbance, where 'fazed' means disturbed or disconcerted (whereas 'phased', 'phrased', and 'fused' do not fit the meaning)."),
    "gate_cs_2024_s2_q02": ("Quantitative Aptitude — Combinatorics", "Easy", "Mixing all 4 distinct elements in all possible orders corresponds to the number of permutations of 4 items, which is 4! = 4 * 3 * 2 * 1 = 24. Since the wizards work independently, each wizard makes 24 attempts."),
    "gate_cs_2024_s2_q03": ("Quantitative Aptitude — Set Theory", "Easy", "Out of 10,000 students, 10,000 - 1,500 = 8,500 like at least one branch. Let C and O be those liking core and other branches, with O = 4C and |C intersect O| = 500; by inclusion-exclusion, C + 4C - 500 = 8,500, giving 5C = 9,000 and C = 1,800."),
    "gate_cs_2024_s2_q04": ("Quantitative Aptitude — Logarithms & Algebra", "Easy", "Exponentiating ln((x + y)/2) = (1/2)(ln x + ln y) = ln(sqrt(xy)) gives (x + y)/2 = sqrt(xy). Squaring both sides gives x^2 + 2xy + y^2 = 4xy, so x^2 + y^2 = 2xy, and dividing by xy yields x/y + y/x = 2."),
    "gate_cs_2024_s2_q05": ("Quantitative Aptitude — Number Series", "Easy", "Look at consecutive differences: 9 - 6 = 3, 14 - 9 = 5, and 41 - 30 = 11. Following the consecutive odd integers pattern (+3, +5, +7, +9, +11), x = 14 + 7 = 21 (and 21 + 9 = 30)."),
    "gate_cs_2024_s2_q06": ("Verbal Aptitude — Para Jumbles", "Medium", "Sentence S introduces the geological collision, P ('This fortuitous geological event...') describes its immediate result, R ('The natural process of the cooling of this massive edifice...') describes the subsequent effect, and Q ('Thus...') draws the conclusion. This yields the coherent order SPRQ."),
    "gate_cs_2024_s2_q07": ("Quantitative Aptitude — Profit & Loss", "Easy", "When two items are sold at the same selling price S, one at p% profit and the other at p% loss, there is always an overall loss of (p/10)^2 %. With p = 10, the overall loss is (10/10)^2 = 1%."),
    "gate_cs_2024_s2_q08": ("Data Interpretation — Bar/Pie Chart", "Medium", "In 2007, renewables (Hydro 30% + Solar 5% + Wind 5%) accounted for 40% of total generation. In 2023, renewables (Hydro 35% + Solar 20% + Wind 10%) accounted for 65%, giving a percentage increase of ((65 - 40) / 40) * 100 = 62.5%."),
    "gate_cs_2024_s2_q09": ("Spatial Aptitude — 3D Geometry", "Easy", "Each straight planar cut along one of the three orthogonal axes (length, width, height) doubles the number of pieces. Making 1 cut along each of the 3 perpendicular mid-planes produces 2 * 2 * 2 = 8 equal smaller cubes, so 3 cuts suffice."),
    "gate_cs_2024_s2_q10": ("Analytical Aptitude — Grid Puzzle", "Hard", "Using the neighbor counts given in the first three rows of the 4 x 4 grid (refer to the official array figure), the positions of all crosses (X) in rows 1–3 are uniquely determined. Counting non-X immediate neighbors for each cell in the cross-free fourth row gives a sum of 11."),
    "gate_cs_2024_s2_q11": ("Computer Organization — I/O & DMA", "Easy", "At 4 MHz, 1% of cycles gives 0.01 * 4 * 10^6 = 40,000 DMA cycles per second. Transferring 8 bytes (64 bits) per cycle yields a transfer rate of 40,000 * 64 = 2,560,000 bits/sec."),
    "gate_cs_2024_s2_q12": ("Discrete Mathematics — Propositional Logic", "Easy", "'When q (student scores > 50% marks), not p (fail grade cannot be given)' translates directly to the implication q -> not p."),
    "gate_cs_2024_s2_q13": ("Programming in C — Functions & Evaluation", "Medium", "In main(), arguments to f(g(10), h(20)) are evaluated right-to-left: h(20) prints 20 and returns 20, then g(10) prints 10 and returns 10. Inside f(10, 20), g(10) prints 10 and h(20) prints 20, yielding '20101020'."),
    "gate_cs_2024_s2_q14": ("Digital Logic — Floating Point Representation", "Easy", "In IEEE 754 single precision, an all-1s exponent (1111 1111) represents Infinity or NaN rather than a finite floating-point number (ruling out C). Among finite positive numbers (sign bit 0), the largest biased exponent is 254 (1111 1110) with all 1s in the 23-bit mantissa, which is Option (B)."),
    "gate_cs_2024_s2_q15": ("Algorithms — Recurrence Relations", "Easy", "The characteristic equation r^2 - 5r + 6 = 0 has roots r = 2 and r = 3, so T(n) = c1 * 2^n + c2 * 3^n. Using T(0) = c1 + c2 = 1 and T(1) = 2*c1 + 3*c2 = 2 gives c1 = 1 and c2 = 0, so T(n) = 2^n = Theta(2^n)."),
    "gate_cs_2024_s2_q16": ("Engineering Mathematics — Calculus", "Medium", "Using the King's property of definite integrals, I = integral_0^2 f(x) dx = integral_0^2 f(2 - x) dx. Adding the two expressions gives 2I = integral_0^2 (f(x) + f(2 - x)) dx = integral_0^2 1 dx = 2, so I = 1."),
    "gate_cs_2024_s2_q17": ("Discrete Mathematics — Graph Theory", "Medium", "For an undirected simple graph, A is symmetric and has 0s on the diagonal. If A^(-1) = A, then A^2 = I, meaning every vertex i has degree (A^2)_ii = 1 and no two distinct vertices share a common neighbor; thus every vertex has degree 1, so G is a perfect matching (disjoint union of edges)."),
    "gate_cs_2024_s2_q18": ("Engineering Mathematics — Probability", "Easy", "There are 6^6 total outcomes and 6! outcomes with all distinct numbers. The probability is 6! / 6^6 = 720 / 46656 = 5 / 324."),
    "gate_cs_2024_s2_q19": ("Databases — Transactions", "Easy", "Durability in ACID guarantees that once a transaction has committed and been acknowledged to the user, its updates survive any subsequent system crash even if not yet flushed to disk."),
    "gate_cs_2024_s2_q20": ("Databases — ER Model", "Easy", "In an ER model, a weak entity depends on an identifying owner entity for its existence and primary key, so every weak entity instance must be associated with an owner entity—meaning the weak entity set MUST have total participation in the identifying relationship."),
    "gate_cs_2024_s2_q21": ("Compiler Design — Compiler Phases", "Easy", "A Lexical Analyzer outputs Tokens (P-2), a Syntax Analyzer builds a Parse Tree (Q-3), an Intermediate Code Generator commonly produces an Abstract Syntax Tree or three-address IR (R-1), and a Code Optimizer performs transformations like Constant Folding (S-4)."),
    "gate_cs_2024_s2_q22": ("Theory of Computation — Finite Automata", "Medium", "Following the transitions of the DFA in the diagram (refer to the official question paper), it accepts strings starting with 0*1 followed by zero or more loops returning to the accepting state via 0 or 10*1, matching 0*1(0 + 10*1)*."),
    "gate_cs_2024_s2_q23": ("Computer Networks — Data Link & Network Layer", "Medium", "As the IP packet leaves X toward Y via intermediate router R, the Layer-3 destination IP address is the final destination Y (B is true). Because Ethernet switch S is a transparent Layer-2 device, the Layer-2 destination MAC address on the frame is the MAC address of the next-hop router R (not S or Y), making only (B) true."),
    "gate_cs_2024_s2_q24": ("Operating Systems — Memory Management", "Medium", "The MMU performs hardware virtual-to-physical address translation using page tables/TLB (B) and raises page-fault traps on missing/invalid translations (C) or protection traps on permission violations like writing a read-only page (D). Allocating a page table for a new process is handled by the OS kernel, not the MMU."),
    "gate_cs_2024_s2_q25": ("Operating Systems — Process Management", "Medium", "A blocking disk I/O system call (A) and a page fault to swap space (B) both block process P until I/O completes, forcing the OS to switch P out of running state. A timer interrupt or disk completion interrupt for another process invokes an ISR, but the scheduler may resume P without moving P to a non-running state."),
    "gate_cs_2024_s2_q26": ("Databases — File Organization & Indexing", "Medium", "Scanning an entire relation reads pages sequentially in Sorted (A) or Heap (B) file organizations, minimizing random disk seeks. Unclustered tree or hash indexes store pointers to records scattered randomly across data pages, causing excessive random I/O during full scans."),
    "gate_cs_2024_s2_q27": ("Databases — Concurrency Control", "Medium", "Two-Phase Locking guarantees conflict serializability (A) because transactions follow a growing phase then a shrinking phase where no new locks can be acquired after releasing any lock (C), though deadlocks remain possible (D). Option (B) describes immediate acquire-release per operation rather than 2PL."),
    "gate_cs_2024_s2_q28": ("Computer Networks — Network Layer (IPv4)", "Medium", "In IPv4, any intermediate router (as well as the source) fragments a datagram if its size exceeds the outgoing link's MTU and DF=0 (B). Fragments are reassembled only at the final destination host (C), not at intermediate routers."),
    "gate_cs_2024_s2_q29": ("Compiler Design — Syntax Directed Translation", "Medium", "By definition, L-attributed SDDs can always be evaluated in a single depth-first (left-to-right) traversal (so B is FALSE). Moreover, not all L-attributed SDDs on LR(1) grammars can be evaluated during bottom-up LR parsing—only a restricted subclass (e.g., S-attributed or those convertible via marker non-terminals) can (so D is FALSE). Statements A and C are true."),
    "gate_cs_2024_s2_q30": ("Digital Logic — Boolean Algebra", "Easy", "In Boolean algebra, x + 1 = 1 (not x, so B is FALSE) and x . x = x (not 0, so C is FALSE). Identities x . 1 = x (A) and x + x' = 1 (D) are always true."),
    "gate_cs_2024_s2_q31": ("Computer Organization — Pipelining & Hazards", "Medium", "I1 writes R3 and I2 reads R3, creating a Read-After-Write (RAW) dependency on R3 between I1 and I2 (A). Between I1 and I3, both write R3 (WAW, not WAR); between I2 and I3, the RAW dependency is on R5 (not R3); and between I3 and I4, I3 writes R3 and I4 reads R3 (RAW, not WAW)."),
    "gate_cs_2024_s2_q32": ("Computer Networks — Network Layer (IPv4)", "Easy", "Every IP router decrements the Time to Live (TTL) field by 1 before forwarding (C), which changes the IP header and therefore requires recomputing the Header Checksum (D). Source IP and Protocol remain unchanged (unless NAT is used)."),
    "gate_cs_2024_s2_q33": ("Programming in C — Strings & Pointers", "Medium", "fX(a) computes string length using pointer arithmetic and does not modify the passed string, so passing a string literal fX(\"abcd\") (A), a local array char c[] = \"abcd\" (B), or a pointer char *c = \"abcd\" (D) all compile cleanly and return 4."),
    "gate_cs_2024_s2_q34": ("Discrete Mathematics — Posets & Lattices", "Medium", "A total order containing P corresponds to a topological sort of the poset with covering edges 1 -> 2, 3 -> 2, and 3 -> 4. Ordering {1, 2, 3} with 1 < 2 and 3 < 2 allows two orders: (1, 3, 2) and (3, 1, 2). In (1, 3, 2), 4 can go after 3 (2 positions: 1,3,4,2 or 1,3,2,4); in (3, 1, 2), 4 can go anywhere after 3 (3 positions: 3,4,1,2; 3,1,4,2; 3,1,2,4), giving 2 + 3 = 5 total orders."),
    "gate_cs_2024_s2_q35": ("Algorithms — Dynamic Programming (LIS)", "Medium", "Keeping the longest non-decreasing subsequence (LNDS) of A = [2, 5, 3, 1, 4, 2, 6] fixed and replacing all other elements minimizes replacements. An LNDS is [2, 3, 4, 6] of length 4 (out of 7 elements), so at least 7 - 4 = 3 elements must be replaced."),
    "gate_cs_2024_s2_q36": ("Programming in C — Pointers", "Easy", "Since q = p + 1 points one double past p, pointer subtraction (q - p) yields the element difference 1. Dereferencing gives *q - *p = 25.0 - 20.0 = 5.0, so printf outputs '1,5'."),
    "gate_cs_2024_s2_q37": ("Operating Systems — CPU Scheduling", "Medium", "Under SRTF: A runs 0–2 (rem 8), B runs 2–4 (rem 4), C runs 4–7 (finishes at 7, WT=0), B runs 7–11 (finishes at 11, WT=3), D runs 11–18 (finishes at 18, WT=5), A runs 18–26 (finishes at 26, WT=16), giving avg WT = (16+3+0+5)/4 = 6. Under NP-SJF: A runs 0–10 (WT=0), C runs 10–13 (WT=6), B runs 13–19 (WT=11), D runs 19–26 (WT=13), giving avg WT = (0+6+11+13)/4 = 7.5."),
    "gate_cs_2024_s2_q38": ("Computer Networks — IP Addressing & Subnets", "Easy", "The range 10.12.2.0 to 10.12.3.255 spans two consecutive /24 blocks (512 addresses), where the third octet is 2 (00000010) and 3 (00000011). These share the first 7 bits of the third octet (0000001x), giving the /23 prefix 10.12.2.0/23."),
    "gate_cs_2024_s2_q39": ("Data Structures — Binary Search Trees", "Easy", "The inorder traversal of any BST visits its keys in strictly sorted (ascending) order. Because the set V of distinct integers uniquely determines its sorted order, the inorder traversal is uniquely determined from V, whereas the root, preorder, and postorder depend on insertion order."),
    "gate_cs_2024_s2_q40": ("Compiler Design — LL(1) Parsing", "Hard", "From S -> AaAb | BbBa, FIRST(AaAb) = {c, a} and FIRST(BbBa) = {d, b}, so cell (1) (S, c) gets S -> AaAb and cell (2) (S, d) gets S -> BbBa. Because A precedes b in S -> AaAb and B precedes a in S -> BbBa, FOLLOW(A) = {a, b} and FOLLOW(B) = {b, a}, placing A -> eps in cell (3) (A, b) and B -> eps in cell (4) (B, a)."),
    "gate_cs_2024_s2_q41": ("Theory of Computation — Finite Automata", "Medium", "Tracing the 5-state epsilon-NFA in the figure shows that from the start state it either accepts 0* or enters the 1-cycle loop (1 + 0(00)*)(11)*, yielding 0* + (1 + 0(00)*)(11)*."),
    "gate_cs_2024_s2_q42": ("Algorithms — Sliding Window & Arrays", "Hard", "When X[i] == second, the subarray with at most two distinct values extends (len2++), while the trailing run of equal values resets to just X[i] (P = 1) and second becomes the previous first. When X[i] is a third distinct value, the new 2-distinct-value subarray keeps the previous trailing equal run plus X[i], so Q = len1 + 1."),
    "gate_cs_2024_s2_q43": ("Compiler Design — Intermediate Code Generation", "Medium", "Triple (1) loads array element s[i] via operator '=[]' with operands s and i. Triple (3) multiplies triple (0) (p + r) by triple (2) (-s[i]), giving '* (0) (2)'. Triple (6) addresses l-value x[i] via '[]=' with operands x and i, matching Option (A)."),
    "gate_cs_2024_s2_q44": ("Engineering Mathematics — Probability", "Medium", "Since x and y take values in [0, 1], we always have 0 <= y <= 1 and x >= 0, which implies xy <= x everywhere. Taking expectations on both sides gives E[z] = E[xy] <= E[x], i.e., z_bar <= x_bar."),
    "gate_cs_2024_s2_q45": ("Databases — Relational Algebra", "Medium", "To find cities with at least 3 distinct persons (p1, p2, p3 with the same city and distinct pids p1 != p2, p2 != p3, p1 != p3), we must join Person with itself three times (Person x Person x Person), which requires a minimum of 2 cross product operations."),
    "gate_cs_2024_s2_q46": ("Operating Systems — Synchronization", "Hard", "If T2 runs first, wait(s1) succeeds, x becomes 1, prints 1, signal(s2) sets s2=1, signal(s1) sets s1=1; then T1 acquires s1, increments x to 2, prints 2, consumes s2, and releases s1 (B). If T1 runs first, wait(s1) succeeds, x becomes 1, prints 1, and T1 blocks on wait(s2) while holding s1; T2 then blocks on wait(s1), causing deadlock (C)."),
    "gate_cs_2024_s2_q47": ("Engineering Mathematics — Linear Algebra", "Medium", "Swapping two rows of a square matrix negates its determinant (det(B) = -det(A), A), and since det(B) != 0 iff det(A) != 0, B is invertible whenever A is (B). Symmetry and zero trace are not preserved under arbitrary row swaps (C and D are false)."),
    "gate_cs_2024_s2_q48": ("Data Structures — Stacks", "Hard", "Because S2 holds at most 2 items, (B) 200, 300, 400, 100 succeeds by pushing 400 and 300 to S2, outputting 200, returning 300 then 400 to S1 to output them, and outputting 100. Similarly (C) and (D) require at most 1 item in S2 at a time, whereas (A) 100, 200, 400, 300 requires pushing 400, 300, and 200 (3 items) onto S2 before outputting 100, exceeding S2's capacity."),
    "gate_cs_2024_s2_q49": ("Digital Logic — Number Systems", "Easy", "Converting (224)_5 to decimal gives 2*25 + 2*5 + 4 = 64 (A). In radix-8, (100)_8 = 1*64 = 64 (B); in radix-7, (121)_7 = 1*49 + 2*7 + 1 = 64 (D); whereas (50)_16 = 80 != 64."),
    "gate_cs_2024_s2_q50": ("Digital Logic — Combinational Circuits", "Hard", "Evaluating the combinational logic circuit built from f1, f2, f3, f4 (refer to the official circuit diagram) yields minterms {0, 1, 2, 3, 4, 5, 6, 7}, which equals Sigma(0,1,2,3,4,5,6,7) (C) and equivalently maxterms Pi(8,9,10,11,12,13,14,15) (D)."),
    "gate_cs_2024_s2_q51": ("Algorithms — Minimum Spanning Trees", "Hard", "Swapping any two edges in the same cycle C preserves whether a subgraph is a spanning tree, so all edges in C must share the same weight parity for every spanning tree to have even weight. Thus in every cycle C, either all edges have even weight or all edges have odd weight (D); a triangle of three odd-weight edges shows A, B, and C need not hold."),
    "gate_cs_2024_s2_q52": ("Theory of Computation — Context-Free Grammars", "Hard", "Every production increases the count of c by 1 only at S -> c and b by 1 only at S -> aSbS (which adds one S), so by induction n_c(w) = n_b(w) + 1 (C). Also each S -> aSbS adds one 'a' and one extra 'c' (via the second S), while S -> c gives n_a=0, n_c=1, so n_a(w) >= n_c(w) - 1 > n_c(w) - 2 (B)."),
    "gate_cs_2024_s2_q53": ("Operating Systems — Disk Scheduling & I/O", "Medium", "At 6000 RPM (100 RPS), one rotation takes 10 ms, so average rotational latency is 5 ms and 1-sector transfer time is 10/500 = 0.02 ms. Each of the 3000 randomly placed sectors takes 5 ms (seek) + 5 ms (rotational latency) + 0.02 ms (transfer) = 10.02 ms, totaling 3000 * 10.02 ms = 30.06 seconds (in 29.50 to 30.50)."),
    "gate_cs_2024_s2_q54": ("Computer Networks — Transport Layer (TCP)", "Medium", "Upon timeout at cwnd = 12 MSS, ssthresh becomes 12/2 = 6 MSS and cwnd resets to 1 MSS (1st RTT after loss). After all segments in RTT 1 are ACKed, cwnd doubles to 2 MSS (2nd RTT), and after RTT 2 is ACKed, cwnd doubles to 4 MSS (3rd RTT)."),
    "gate_cs_2024_s2_q55": ("Computer Networks — Data Link Layer (CSMA/CD)", "Easy", "For CSMA/CD collision detection, transmission time must be at least 2 * T_prop. Here 2 * T_prop = 2 * (500 m) / (2 * 10^8 m/s) = 5 * 10^(-6) s, so minimum frame size = (10^8 bits/s) * (5 * 10^(-6) s) = 500 bits."),
    "gate_cs_2024_s2_q56": ("Databases — Functional Dependencies", "Hard", "For 4 attributes, each attribute can go into X, into Y, or into neither (3^4 = 81 total disjoint pairs). Subtracting pairs with X = empty (2^4 = 16) and pairs with Y = empty (2^4 = 16), and adding back X = Y = empty (counted twice, 1), gives 81 - 16 - 16 + 1 = 50 useful FDs."),
    "gate_cs_2024_s2_q57": ("Computer Organization — Instruction Formats", "Easy", "With 16 registers, each register field needs 4 bits (2 * 4 = 8 bits), 8 addressing modes need 3 bits, and the scalar field uses 16 bits. This leaves 32 - (8 + 3 + 16) = 5 bits for the opcode, supporting up to 2^5 = 32 unique opcodes."),
    "gate_cs_2024_s2_q58": ("Computer Organization — Pipelining", "Medium", "Both designs run at 2 GHz, so speedup = CPI_nonpipelined / CPI_pipelined. Here CPI_nonpipelined = 6, and CPI_pipelined = 1 + 0.20*2 + 0.20*3 = 1 + 0.4 + 0.6 = 2.0, giving speedup = 6 / 2.0 = 3.0 (in 2.9 to 3.1)."),
    "gate_cs_2024_s2_q59": ("Algorithms — Minimum Spanning Trees", "Medium", "Applying Kruskal's algorithm to the given 7-vertex graph: the four weight-1 edges form two disconnected components (paths/edges) of size 3/2 or 4 weight-1 edges with no cycles, leaving 2 more edges of weight 2 needed to connect the components. Counting ways to pick the 2 weight-2 edges without forming cycles in the official graph yields 9 distinct MSTs."),
    "gate_cs_2024_s2_q60": ("Discrete Mathematics — Graph Theory", "Medium", "Inspecting the graph in the official question paper shows it contains at least one edge and no odd cycles (it is bipartite). Hence its chromatic number is 2."),
    "gate_cs_2024_s2_q61": ("Computer Organization — Instruction Formats", "Hard", "There are 75 R-type and 75 I-type instructions; distinguishing R/I takes 1 bit and identifying 75 operations within a type needs ceil(log2(75)) = 7 bits, so Y = 1 + 7 = 8 bits. With 50 registers, each register field needs ceil(log2(50)) = 6 bits. In 32-bit R-type (OPCODE + UNUSED + 3 regs): X = 32 - (8 + 18) = 6; in I-type (OPCODE + 2 regs + imm): Z = 32 - (8 + 12) = 12, giving X + 2Y + Z = 6 + 16 + 12 = 34."),
    "gate_cs_2024_s2_q62": ("Theory of Computation — Regular Languages", "Medium", "L1 = b*ab*(ab*ab*)* is the set of all strings over {a, b} containing an ODD number of a's. Among strings in L2 of length <= 4: for length 1 (1 string), length 2 (2 strings), length 3 (4 strings), and length 4 (8 strings)—in general, half of the 2^k strings of length k >= 1 have an odd number of a's—so 1 + 2 + 4 + 8 = 15 strings."),
    "gate_cs_2024_s2_q63": ("Discrete Mathematics — Group Theory", "Medium", "An element (x, y, z) in Z2 x Z3 x Z4 is its own inverse iff 2x = 0 (mod 2), 2y = 0 (mod 3), and 2z = 0 (mod 4). That gives x in {0, 1} (2 choices), y in {0} (1 choice), and z in {0, 2} (2 choices), totaling 2 * 1 * 2 = 4 elements."),
    "gate_cs_2024_s2_q64": ("Operating Systems — Virtual Memory", "Hard", "Each 4 KB page holds 4096 / 4 = 1024 PTEs, so 1 outer page directory (always allocated) + inner page tables are used. Minimum pages X occurs when all 2000 PTEs are packed into ceil(2000 / 1024) = 2 inner pages, giving X = 1 + 2 = 3; maximum pages Y occurs when the 2000 accessed pages fall into 1024 distinct outer entries (since the outer directory has 1024 entries), using 1024 inner pages and Y = 1 + 1024 = 1025. Thus X + Y = 3 + 1025 = 1028."),
    "gate_cs_2024_s2_q65": ("Compiler Design — LR Parsing", "Hard", "Advancing the dot over S from I0 = CLOSURE({S' -> .S}) produces the 2 kernel items {S' -> S., S -> S.S}. Taking CLOSURE adds the 7 items {S -> .SS, S -> .Aa, S -> .bAc, S -> .Bc, S -> .bBa, A -> .d#, B -> .@}, yielding 2 + 7 = 9 LR(0) items."),

    # --- GATE CS 2025 Set 2 ---
    "gate_cs_2025_s2_q01": ("Verbal Aptitude — Vocabulary", "Easy", "After 'initial hesitation', 'never wavered' indicates strong determination. 'Resolve' means firm determination to do something, whereas 'ambivalence' means mixed feelings and 'revolve' is a verb."),
    "gate_cs_2025_s2_q02": ("Verbal Aptitude — Analogy", "Easy", "A nest is the shelter/home built by a bird; similarly, a hive is the home/dwelling of a bee."),
    "gate_cs_2025_s2_q03": ("Quantitative Aptitude — Algebra", "Easy", "If P*e^x = Q*e^(-x) holds for all real x, then multiplying by e^x gives P*e^(2x) = Q. Since e^(2x) varies with x while Q is constant, this can hold for all x only if P = Q = 0."),
    "gate_cs_2025_s2_q04": ("Spatial Aptitude — Cube Folding", "Medium", "Folding the 2D net in the question figure into a 3D cube fixes which faces are opposite and how adjacent face patterns orient relative to one another. Matching those adjacencies and orientations identifies Option (A) as the valid cube (refer to the official figures)."),
    "gate_cs_2025_s2_q05": ("Quantitative Aptitude — Number Theory", "Easy", "Since p1 and p2 are prime numbers, each is >= 2. Therefore their product p1 * p2 has p1 and p2 as non-trivial factors (> 1 and < p1*p2), so p1 * p2 is always composite (not prime)."),
    "gate_cs_2025_s2_q06": ("Verbal Aptitude — Logical Inference", "Medium", "The counterfactual conditional 'Even if I had known that you were in the hospital, I would not have gone there to see you' presupposes that Ramya did not know Josephine was in the hospital."),
    "gate_cs_2025_s2_q07": ("Analytical Aptitude — Coding-Decoding", "Easy", "Reversing the word IMAGE gives EGAMI, and shifting each letter forward by +1 yields FHBNJ; similarly reversing FIELD gives DLEIF and +1 gives EMFJG. Reversing BEACH gives HCAEB and shifting +1 gives IDBFC."),
    "gate_cs_2025_s2_q08": ("Analytical Aptitude — Sequences", "Medium", "Checking i = 1, 2, 3: X(1) = 20 + (-4) = 16, X(2) = 16 + 10 = 26, X(3) = 26 + 15 = 41, so X(i) = X(i-1) + I(i). Likewise, Y(1) = 20 * (-4) = -80, Y(2) = -80 * 10 = -800, Y(3) = -800 * 15 = -12000, so Y(i) = Y(i-1) * I(i)."),
    "gate_cs_2025_s2_q09": ("Quantitative Aptitude — Geometry", "Medium", "Triangles PQL and PSN share angles or notice Area(triangle PLS) = (1/2) * base PS * height PQ = (1/2) * 2 * 2 = 2 cm^2. Since triangle PLS has the same base PL and height equal to the width of rectangle PLMN, Area(PLMN) = 2 * Area(triangle PLS) = 4 cm^2."),
    "gate_cs_2025_s2_q10": ("Analytical Aptitude — Graph Puzzle", "Medium", "Connecting 5 land zones requires a spanning tree of at least 4 bridges, and bridges Q, R, T, and V connect all 5 zones Z1–Z5 without creating a cycle (refer to the official river map)."),
    "gate_cs_2025_s2_q11": ("Engineering Mathematics — Linear Algebra", "Easy", "Computing A^2 for A = [[1, 2], [2, -1]] gives [[5, 0], [0, 5]] = 5I. Therefore A^8 = (A^2)^4 = (5I)^4 = 625I = [[625, 0], [0, 625]]."),
    "gate_cs_2025_s2_q12": ("Engineering Mathematics — Calculus", "Medium", "Integrating by parts: integral_1^x t ln t dt = [(t^2/2) ln t - t^2/4]_1^x = (x^2/2) ln x - x^2/4 + 1/4 = 1/4. This simplifies to (x^2/4)(2 ln x - 1) = 0; since x > 1, 2 ln x = 1, so ln x = 1/2 and x = sqrt(e)."),
    "gate_cs_2025_s2_q13": ("Data Structures — Binary Trees", "Easy", "In a full binary tree with k internal nodes (each having 2 children), total edges = 2k, and total nodes n = 2k + 1. Solving for k gives k = (n - 1)/2."),
    "gate_cs_2025_s2_q14": ("Engineering Mathematics — Linear Algebra", "Easy", "From L^2 = L^(-1), multiplying by L gives L^3 = I. Hence M = L^8 = (L^3)^2 * L^2 = L^2 = N, so M - N = 0 (the zero matrix), whose determinant is 0."),
    "gate_cs_2025_s2_q15": ("Discrete Mathematics — Mathematical Logic", "Easy", "Option (A) is the exact axiom of mathematical induction over natural numbers {0, 1, 2, ...}: if P(0) holds and P(x) implies P(x + 1) for all x, then P(x) holds for all natural numbers x."),
    "gate_cs_2025_s2_q16": ("Computer Networks — Network & Transport Layers", "Easy", "ARP resolves a known IPv4 address to its link-layer MAC address, so (i) is TRUE. TCP supports piggybacking, allowing a single segment from S to R to carry both application data and an ACK for data from R to S, so (ii) is FALSE."),
    "gate_cs_2025_s2_q17": ("Computer Networks — Routing Protocols", "Easy", "Distance vector routing protocols (like RIP) compute shortest paths iteratively using the Bellman-Ford algorithm, whereas link state routing protocols (like OSPF) flood topology maps and run Dijkstra's algorithm."),
    "gate_cs_2025_s2_q18": ("Computer Networks — Network Layer (IPv4)", "Easy", "ICMP (protocol 1), IGMP (protocol 2), and OSPF (protocol 89) are encapsulated directly inside IPv4 datagrams and have IPv4 protocol numbers. RIP runs over UDP (port 520), so its IPv4 protocol field is UDP (17), not RIP."),
    "gate_cs_2025_s2_q19": ("Programming in C — Strings & Pointers", "Medium", "stringcopy(a, a + 2) copies from a+2 ('Hello World!') back into a[0..], overwriting '@#Hello Worl' and stopping when *t reaches the null byte '\\0' WITHOUT copying '\\0' into s! Thus the last two characters 'd!' of the original string remain after 'Hello World!', printing 'Hello World!d!'."),
    "gate_cs_2025_s2_q20": ("Algorithms — Comparison Models", "Easy", "Compare any two distinct elements in the list (1 comparison). The smaller of the two cannot be the largest element in the list, so only 1 comparison is needed."),
    "gate_cs_2025_s2_q21": ("Compiler Design — Intermediate Code Generation", "Easy", "Backpatching maintains lists of jump instructions whose target labels are unknown and fills them once targets are determined, enabling single-pass intermediate code generation for both Boolean expressions (short-circuit evaluation) and flow-of-control statements (if/while)."),
    "gate_cs_2025_s2_q22": ("Compiler Design — Syntax Directed Translation", "Medium", "Rule 1 computes inherited attribute B.i from R.i, then A.i from B.i (right-to-left dependency), violating L-attributed (and S-attributed) rules. Rule 2 computes D.i from C.i (left-to-right, L-attributed but not S-attributed since D.i is inherited). Rule 3 only computes synthesized attribute Q.i, so it is both S-attributed and L-attributed."),
    "gate_cs_2025_s2_q23": ("Computer Networks — Network Layer (IPv4)", "Medium", "Total IPv4 payload = 8 (UDP header) + 7488 = 7496 bytes. With MTU 1500 and a 20-byte IPv4 header, max IP payload per fragment (multiple of 8) is floor(1480/8)*8 = 1480 bytes. Dividing 7496 / 1480 gives 5 full fragments (5 * 1480 = 7400 bytes) plus a 6th fragment carrying 96 data bytes + 20 header bytes = 116 bytes."),
    "gate_cs_2025_s2_q24": ("Theory of Computation — Pushdown Automata", "Easy", "Every regular language is accepted by a DFA, which is a special case of a deterministic pushdown automaton (DPDA) that ignores its stack (A). DPDAs cannot accept all CFLs (such as palindromes) or all decidable languages."),
    "gate_cs_2025_s2_q25": ("Theory of Computation — Decidability", "Easy", "Emptiness of a CFG ('Is L(G1) = empty?') is decidable by marking generating non-terminals in O(|G|) time (D). Equivalence of two CFGs (A), disjointness of two CFGs (B), and whether a CFG equals a regular language (C) are all undecidable."),
    "gate_cs_2025_s2_q26": ("Operating Systems — CPU Scheduling", "Medium", "Under SRTF: P1 runs 0–1 (rem 9), P1 runs 1–2 (rem 8 < 13), P3 arrives at 2 (rem 6 < 8) and runs 2–8 (finishes at 8, TAT=6). At 8, P4 arrives (rem 9) while P1 has rem 8, so P1 runs 8–16 (finishes at 16, TAT=16), P4 runs 16–25 (finishes at 25, TAT=17), and P2 runs 25–38 (finishes at 38, TAT=37). Average TAT = (16 + 37 + 6 + 17) / 4 = 76 / 4 = 19 ms."),
    "gate_cs_2025_s2_q27": ("Databases — Transactions", "Medium", "Both concurrent transactions read the stale balance Rs. 11000 (lost update / lack of Isolation, C), which caused A to lose only one Rs. 10000 while B gained Rs. 20000, violating Consistency (money conservation, B). Atomicity and Durability were not necessarily violated since both committed."),
    "gate_cs_2025_s2_q28": ("Computer Organization — ISA Basics", "Easy", "The Instruction Set Architecture (ISA) defines programmer-visible hardware specifications such as the number and types of architectural registers (D), instructions, and addressing modes. Cache sizes, cache levels, and clock frequency are microarchitectural/implementation details."),
    "gate_cs_2025_s2_q29": ("Algorithms — Graph Traversal (BFS/DFS)", "Medium", "A DFS tree is not necessarily a shortest-path tree (A false). In an undirected graph, DFS has only tree edges and back/forward edges (no cross edges, B), BFS non-tree edges only connect vertices at levels differing by at most 1 (C), and both traversals discover all connected components (D)."),
    "gate_cs_2025_s2_q30": ("Theory of Computation — Closure Properties", "Medium", "Context-free languages are not closed under complementation ((i)-(b)), recursive languages are closed under both union ((ii)-(a)) and intersection ((ii)-(c)), and regular languages are closed under both intersection ((iii)-(c)) and union ((iii)-(a)). Hence both B and C are valid matchings."),
    "gate_cs_2025_s2_q31": ("Digital Logic — Logic Gates", "Medium", "Evaluating the logic gates in the circuit diagram (refer to the official question paper) yields F = (XY')' = X' + Y (or equivalent forms shown in A, B, and C after applying De Morgan's and absorption laws, whereas X + Y' in D is inequivalent)."),
    "gate_cs_2025_s2_q32": ("Computer Organization — Computer Arithmetic", "Medium", "Booth's algorithm performs an addition or subtraction whenever adjacent bits (Q_i, Q_{i-1}) differ (01 -> add, 10 -> sub), appending an implicit Q_{-1} = 0 at the LSB of Q = 1010 0100 1010 1010. Counting bit transitions across the 17-bit sequence 10100100101010100 gives 13 transitions (1->0, 0->1, ...), so 13 addition/subtraction operations are performed."),
    "gate_cs_2025_s2_q33": ("Programming in C — Loops & Control Flow", "Easy", "The do-while loop computes GCD(126, 105) using Euclid's subtraction method: (126,105) -> (21,105) -> (21,84) -> (21,63) -> (21,42) -> (21,21), terminating when x == y = 21."),
    "gate_cs_2025_s2_q34": ("Digital Logic — Sequential Circuits", "Medium", "A 4-bit ripple counter divides the input clock frequency by 2^4 = 16, so the last flip-flop's period (64 us) is 16 times the clock period. Thus T_clk = 64 / 16 = 4 us, and the counter frequency is 1 / (4 * 10^(-6) s) = 250,000 Hz = 250 kHz."),
    "gate_cs_2025_s2_q35": ("Data Structures — Binary Search Trees", "Easy", "Inserting into the BST: 10 (root), -4 (left of 10), 15 (right of 10), 30 (right of 15), 20 (left of 30), 5 (right of -4), 60 (right of 30), 19 (left of 20). The path from 19 to root 10 is 19 -> 20 -> 30 -> 15 -> 10, which has 4 edges."),
    "gate_cs_2025_s2_q36": ("Computer Networks — Data Link Layer", "Medium", "Transmission time T_t = 3000 / 2000 = 1.5 s = 1500 ms, and propagation delay T_p = 100 ms. In Stop-and-Wait, channel utilization is T_t / (T_t + 2*T_p) = 1500 / (1500 + 200) = 1500 / 1700 = 88.235% (88.23%)."),
    "gate_cs_2025_s2_q37": ("Algorithms — Graph Algorithms", "Medium", "Every spanning tree has exactly |V| - 1 edges, so adding alpha to every edge increases every spanning tree's weight by the same constant (|V| - 1)*alpha, preserving all MSTs. However, paths have differing numbers of edges, so adding alpha penalizes paths with more edges more heavily and can change shortest paths."),
    "gate_cs_2025_s2_q38": ("Data Structures — Trees & Heaps", "Hard", "Doubly linked lists with head and tail pointers meld in Theta(1) time by relinking pointers. Two array-based min-heaps of size n can be concatenated into an array of size 2n and heapified via Floyd's build-heap in Theta(n) time. Two BSTs of size n can be flattened in-order, merged, and converted back to a balanced BST in Theta(n) time."),
    "gate_cs_2025_s2_q39": ("Computer Organization — Cache Memory", "Easy", "With 1-byte blocks (offset = 0 bits), 12 index bits give 2^12 = 4096 blocks = 4 KB cache size. Total physical address length is 4 (tag) + 12 (index) + 0 (offset) = 16 bits, giving 2^16 = 64 KB main memory."),
    "gate_cs_2025_s2_q40": ("Compiler Design — LR Parsing", "Hard", "Because FOLLOW(A) = {a, c}, in the state reached on 'b', 'd' containing [S -> bd.a] and [A -> d.], SLR(1) reduces A -> d on lookahead 'a', creating a shift-reduce conflict. LALR(1) tracks exact lookahead {c} for [A -> d.] in that state and resolves the conflict, so G is LALR(1) but not SLR(1)."),
    "gate_cs_2025_s2_q41": ("Algorithms — Divide & Conquer", "Medium", "Using binary search, we can find the peak index i (maximum element) of the bitonic array in Theta(log n) comparisons, and then run binary search on the ascending prefix A[1..i] and the descending suffix A[i+1..n], taking Theta(log n) comparisons in total."),
    "gate_cs_2025_s2_q42": ("Discrete Mathematics — Posets & Lattices", "Hard", "Pointwise <= on Boolean functions {1..n} -> {0, 1} is reflexive, antisymmetric, and transitive, forming a partial order (B) isomorphic to the Boolean lattice of subsets of {1..n} with pointwise min (meet) and max (join) (C). It is not symmetric or an equivalence relation."),
    "gate_cs_2025_s2_q43": ("Digital Logic — K-Map Minimization", "Medium", "Grouping the 1s in the given Karnaugh map (refer to the official K-map figure) yields the two prime implicants x'z' and xz (D), and x'z' expands into the four minterms in Option (A)."),
    "gate_cs_2025_s2_q44": ("Engineering Mathematics — Linear Algebra", "Medium", "Since P = LU, PX = LUX = Q is solved by forward substitution LY = Q followed by backward substitution UX = Y (A). Also det(P) = det(L)*det(U) = 1 * u11*u22*u33: if P is invertible then det(L) != 0 and det(U) != 0 so both are invertible (B), and if P is singular then at least one diagonal element of U must be 0 (C). Symmetric P does not make L and U symmetric (D false)."),
    "gate_cs_2025_s2_q45": ("Data Structures — Stacks", "Medium", "Storing with each node a pointer to the minimum record at or below it (A) maintains O(1) PUSH (compare new key with previous top's min pointer), O(1) POP, and O(1) MIN (read top's min pointer). Maintaining a single min pointer (B) fails on POP in O(1), and sorted array (C) or min-heap (D) make PUSH/POP O(log n) or O(n)."),
    "gate_cs_2025_s2_q46": ("Databases — Normalization", "Medium", "In R1(A,B,C,D,E), AD is the only candidate key, making B, C, E non-prime; thus D -> E violates 3NF (C). In R2(A,B,C,D), C+ = {C, A, B, D} while A+ = {A, B, D}, so C is the sole candidate key and A, B, D are non-prime; thus A -> D and A -> B violate 3NF (D)."),
    "gate_cs_2025_s2_q47": ("Operating Systems — Virtual Memory", "Hard", "At reference 4 (position 3), page 2 is evicted while page 1 (older and equal frequency) stays, ruling out LRU and LFU/MFU ties, and at reference 6 (position 7), page 1 (frequency 2) is evicted while pages 4 and 5 remain because page 1 has the farthest next use (position 11 vs 9 and 10). Only Optimal page replacement matches all replacements (D)."),
    "gate_cs_2025_s2_q48": ("Operating Systems — Deadlocks", "Medium", "Wait-for graph edges: P1 -> P2 (via R2), P2 -> P3 (via R3), P3 -> P1 (via R1) forms cycle P1->P2->P3->P1; and P2 -> P4 (via R4), P4 -> P2 (via R2) forms cycle P2->P4->P2! Aborting P2 breaks BOTH cycles simultaneously (C), and aborting both P1 and P4 also breaks both cycles (D), whereas aborting only P1 or only P3 leaves P2<->P4 alive."),
    "gate_cs_2025_s2_q49": ("Digital Logic — Floating Point Representation", "Medium", "Decoding IEEE 754 single precision: RX = 0xC1100000 = -1.001_2 * 2^3 = -9.0; RY = 0x40C00000 = +1.1_2 * 2^2 = +6.0; RZ = 0x41400000 = +1.1_2 * 2^3 = +12.0. Checking equations: 4(-9 + 6) + 12 = 0 (A), 2(6) - 12 = 0 (B), and 4(-9) + 3(12) = 0 (C), while X + Y + Z = 9 != 0."),
    "gate_cs_2025_s2_q50": ("Digital Logic — Boolean Algebra", "Hard", "By the consensus theorem, AB + A'C + BC = AB + A'C (B). Expanding (A + C)(A' + B) = AA' + AB + A'C + BC = AB + A'C + BC = AB + A'C (C). Applying De Morgan's law and simplifying the complemented product-of-sums in (D) yields A'D + C'D' (D). Option (A) misses the term AC (since A'BC + ABC = BC, A'B'C' + AB'C' = B'C', leaving AB'C which combines to AC, not A'B')."),
    "gate_cs_2025_s2_q51": ("Compiler Design — Grammars & Parsing", "Hard", "Neither G1 nor G2 is left-factored (both have the common prefix 'if E then' across alternatives, causing LL(1) prediction conflicts, C). Furthermore, per the official key, both G1 and G2 are ambiguous (D)."),
    "gate_cs_2025_s2_q52": ("Theory of Computation — Regular & Context-Free Languages", "Hard", "{a^m b^n | m, n >= 0} = a*b* is regular (A). Option (C) tracks #a mod 7 (7 states) and #b mod 9 (9 states) in a finite 63-state DFA, so it is regular (C). Option (B) {a,b}* intersect {a^m b^n c^(m-n)} forces m - n = 0 so m = n, giving {a^n b^n} (non-regular CFL); Option (D) requires #a = #b (non-regular CFL)."),
    "gate_cs_2025_s2_q53": ("Databases — Transactions & Concurrency", "Medium", "Checking conflict graphs for each schedule: in (A), R1(X)->W2(X) (T1->T2) and W2(Y)->W1(Y) (T2->T1) create a cycle; in (C), W1(Y)->W2(Y) (T1->T2) and W2(X)->R1(X) (T2->T1) create a cycle; in (D), W2(X)->R1(X) (T2->T1) and W1(Y)->W2(Y) (T1->T2) create a cycle. Only schedule (B) has all conflict edges in one direction (T2 -> T1), making it conflict serializable."),
    "gate_cs_2025_s2_q54": ("Databases — SQL", "Medium", "EXISTS with correlated subquery (A), 0 < COUNT(*) (C), and NATURAL JOIN on rollno (D) are all valid SQL queries returning names of students enrolled in courseno 1470. SIZEOF(...) in (B) is not a valid SQL function."),
    "gate_cs_2025_s2_q55": ("Computer Organization — Cache Memory", "Easy", "AMAT = L1_hit_time + L1_miss_rate * (L2_miss_penalty_to_L1 + L2_miss_rate * Mem_miss_penalty_to_L2) = 1 + 0.10 * (10 + 0.20 * 100) = 1 + 0.10 * (10 + 20) = 1 + 3 = 4 ns."),
    "gate_cs_2025_s2_q56": ("Computer Organization — Pipelining", "Medium", "Max stage delay = 250 ns; adding the 10 ns latch delay gives clock cycle T_clk = 250 + 10 = 260 ns. Processing n = 1000 instructions in a k = 5 stage pipeline takes (k + n - 1) * T_clk = 1004 * 260 ns = 261,040 ns = 261.04 microseconds (in 260.20 to 261.20)."),
    "gate_cs_2025_s2_q57": ("Databases — B+ Trees", "Hard", "Leaf C = (20*, 22*, 25*, 26*) is full (4 keys). Inserting 23* splits C into two leaves: (20*, 22*, 23*) and (25*, 26*), copying 25 up into parent B = (7, 19, 33, 44). Since B is also full, inserting 25 splits B into (7, 19) and (33, 44) (with 25 pushed up to root A), making 33 the smallest key in the parent of the leaf containing 25*."),
    "gate_cs_2025_s2_q58": ("Operating Systems — Virtual Memory", "Medium", "Page size = 4096 = 2^12 bytes, so page offset = 12 bits. Each 4096-byte inner page table holds 4096 / 8 = 512 = 2^9 entries, using 9 bits for the inner page table index. Thus the outer page table index uses b = 32 - 12 - 9 = 11 bits."),
    "gate_cs_2025_s2_q59": ("Algorithms — Graph Traversal (BFS)", "Medium", "Two-pass BFS on a tree finds the tree's diameter (longest simple path between any two vertices): the first BFS from v finds an endpoint u of a diameter, and the second BFS from u finds the farthest vertex z. Measuring the longest path in the given tree diagram yields diameter 6."),
    "gate_cs_2025_s2_q60": ("Theory of Computation — Finite Automata", "Hard", "The product modulo 7 can take 7 values {0, 1, 2, 3, 4, 5, 6}, wait—since alphabet Sigma = {1, 2, 3, 4} contains no 0 or 7, the product modulo 7 can never be 0! Thus only the 6 nonzero residues {1, 2, 3, 4, 5, 6} mod 7 are reachable (and all 6 are pairwise distinguishable since multiplying by 1..4 keeps transitions distinct), giving 6 states."),
    "gate_cs_2025_s2_q61": ("Computer Organization — Performance & CPI", "Easy", "Total clock cycles = (2.25*2 + 1.20*5 + 1.65*4 + 1.30*3) * 10^8 = (4.5 + 6.0 + 6.6 + 3.9) * 10^8 = 21.0 * 10^8 cycles. Dividing total time 6.3 s by 21.0 * 10^8 cycles gives 3.0 * 10^(-9) s = 3 ns per clock cycle."),
    "gate_cs_2025_s2_q62": ("Programming in C — Pointers & Arrays", "Medium", "arr is {30, 50, 10, 0, 0}. ptr points to arr[1] (50), so a = 50. (*ptr)++ increments arr[1] to 51, then ptr++ moves ptr to arr[2] (10). Thus a + (*ptr) + arr[1] = 50 + 10 + 51 = 111."),
    "gate_cs_2025_s2_q63": ("Programming in C — Functions", "Easy", "g(n) = n + 10 and f(n) = g(2n) = 2n + 10, so g(f(n)) = 2n + 20. For n = 1, g(f(1)) = 22; for n = 2, g(f(2)) = 24. The loop terminates at n = 3 and prints sum = 22 + 24 = 46."),
    "gate_cs_2025_s2_q64": ("Discrete Mathematics — Combinatorics & Algebra", "Hard", "Square invariance {(alpha, beta)} = {(alpha^2, beta^2)} requires either alpha, beta in {0, 1} (yielding three polynomials: x^2, (x-1)^2, x(x-1)) or alpha = beta^2 and beta = alpha^2 with alpha != beta (giving primitive cube roots of unity omega, omega^2 and polynomial x^2 + x + 1). Out of these 4 square-invariant polynomials, 2 have equal roots (x^2 and (x-1)^2), so the probability is 2/4 = 0.5."),
    "gate_cs_2025_s2_q65": ("Engineering Mathematics — Probability", "Hard", "Let X ~ Uniform(0, 1) be the cut point. If X < 0.4, the subinterval containing 0.4 is (X, 1) with length 1 - X; if X > 0.4, it is (0, X) with length X. Thus E[L] = integral_0^0.4 (1 - x) dx + integral_0.4^1 x dx = (0.4 - 0.08) + (0.5 - 0.08) = 0.74 (within 0.70 to 0.80)."),

    # --- GATE CS 2026 Set 1 ---
    "gate_cs_2026_s1_q01": ("Verbal Aptitude — Vocabulary", "Easy", "A 'protagonist' is the leading or main character in a story or cause, whereas an 'antagonist' is the principal opponent or adversary. Thus 'antagonist' is the exact antonym."),
    "gate_cs_2026_s1_q02": ("Spatial Aptitude — Visual Reasoning", "Medium", "Counting or matching the parity, color/shape adjacencies, and orientations of the two given 4-tile building blocks shows that Option (C) cannot be tiled without overlapping or altering the two 4-tile patterns (refer to the official figure)."),
    "gate_cs_2026_s1_q03": ("Quantitative Aptitude — Combinatorics", "Easy", "In a single-elimination knock-out tournament with 64 players and no ties, each game eliminates exactly one player. To leave 1 undefeated winner, 64 - 1 = 63 players must be eliminated, requiring exactly 63 games."),
    "gate_cs_2026_s1_q04": ("Quantitative Aptitude — Arithmetic", "Easy", "The total credit cap is 70. Mandatory credits are 15 (core) + 20 (project) + at least 10 (specialization) = 45 credits minimum, leaving at most 70 - 45 = 25 credits for elective courses."),
    "gate_cs_2026_s1_q05": ("Analytical Aptitude — Logical Deduction", "Easy", "The given statement is T -> (S and Q) ('teacher in room -> all students stand silently'). Option (A) is its contrapositive, while (B) and (D) weaken the consequent. Option (C) asserts the converse (standing -> teacher in room), which does not necessarily follow."),
    "gate_cs_2026_s1_q06": ("Verbal Aptitude — Reading Comprehension", "Medium", "The passage says combinatorics is 'sometimes' used in modeling physical phenomena, making P ('always invoked') False. The passage explicitly states that assigning probabilities to combinatorial possibilities enables computing average values of physical quantities, making Q True."),
    "gate_cs_2026_s1_q07": ("Spatial Aptitude — 3D Views", "Medium", "Comparing the heights, widths, and recessed/protruding block positions in the front view and top view of Panel I against the four 3D candidates in Panel II matches structure (iv) (Option D; refer to the official figure)."),
    "gate_cs_2026_s1_q08": ("Data Interpretation — Line Graphs", "Medium", "For S <= 10, H10(S) - H20(S) = 0 - 0 = 0; for 10 < S <= 20, it equals S - 10 (linear slope +1); and for S > 20, it equals (S - 10) - (S - 20) = 10 (constant). This matches the capped ramp plot of N(S) in the figure."),
    "gate_cs_2026_s1_q09": ("Analytical Aptitude — Logical Puzzle", "Hard", "Vadlejch won silver (best overall after Chopra) and his best throw was not in rounds 1–2 (i) or round 6 (ii), while his round 4 throw was the best of round 4 (iv). Meanwhile, Vesely was 2nd after round 4 and never improved in rounds 5–6 (iii), and did not have a medal-winning throw in rounds 1–2 (i), so Vesely's best throw must have occurred in the Third round."),
    "gate_cs_2026_s1_q10": ("Quantitative Aptitude — Probability", "Medium", "Counting pairs (d1, d2) where d2 is an integer multiple of d1: for d1=1 (6 pairs: 1..6), d1=2 (3 pairs: 2,4,6), d1=3 (2 pairs: 3,6), d1=4 (1 pair: 4), d1=5 (1 pair: 5), d1=6 (1 pair: 6). Total favorable outcomes = 6 + 3 + 2 + 1 + 1 + 1 = 14 out of 36, giving probability 14/36 = 7/18."),
    "gate_cs_2026_s1_q11": ("Engineering Mathematics — Probability", "Easy", "Initially the urn has 1 Red and 1 Blue ball. In step 1, whichever color is picked (probability 1/2 each), the urn ends up with 2 balls of that color and 1 of the other (3 balls total). To equalize the counts after step 2, step 2 must pick the minority color, which has probability 1/3 regardless of step 1, giving total probability 1/3."),
    "gate_cs_2026_s1_q12": ("Discrete Mathematics — Combinatorics", "Medium", "The top-left 3 x 3 entries in {0, 1} can be chosen freely in 2^9 = 512 ways. Each row's 4th entry and each column's 4th entry are then uniquely fixed to make the parity even (and the bottom-right entry automatically satisfies both row 4 and column 4 parity since total 1s in the 3x3 block fixes both), yielding 512 matrices."),
    "gate_cs_2026_s1_q13": ("Engineering Mathematics — Linear Algebra", "Easy", "An n x n real matrix has a characteristic polynomial of degree n, so the algebraic (and geometric) multiplicity of any eigenvalue can be at most n. For example, the n x n identity matrix I_n has eigenvalue 1 with multiplicity n."),
    "gate_cs_2026_s1_q14": ("Computer Organization — Addressing Modes", "Easy", "Immediate addressing encodes a Constant directly in the instruction (P-4), Indirect addressing dereferences a Pointer (Q-2), Base with index accesses an Array element A[i] (R-1), and Base with offset/displacement accesses a field of a Record/struct (S-3)."),
    "gate_cs_2026_s1_q15": ("Computer Organization — ISA Basics", "Easy", "In a load-store architecture, ALU instructions operate only on registers while memory is accessed exclusively via LOAD and STORE instructions. Thus X and Y must first be loaded into R0 and R1, added into R2, and stored back to Z (Option D)."),
    "gate_cs_2026_s1_q16": ("Computer Organization — Pipelining & Hazards", "Easy", "A Read-After-Write (RAW, true dependency) hazard occurs when a later instruction needs a value written by an earlier instruction before it is ready in the pipeline. WAR and WAW are name (anti/output) dependencies in out-of-order execution, and Read-After-Read is never a hazard."),
    "gate_cs_2026_s1_q17": ("Algorithms — Recurrence Relations", "Medium", "For T2(n) = 5*T2(n/4) + Theta(log^2 n), n^(log_4 5) dominates log^2 n, so by Master Theorem Case 1, T2(n) = Theta(n^(log_4 5)) (~ n^1.161). Substituting into T1(n) = 4*T1(n/2) + T2(n), n^(log_2 4) = n^2 dominates n^(log_4 5), so again by Master Theorem Case 1, T1(n) = Theta(n^2)."),
    "gate_cs_2026_s1_q18": ("Computer Networks — Transport Layer (TCP)", "Medium", "TCP is full-duplex (C false), uses a three-way handshake (A false), and allows either endpoint to initiate teardown (B false). Both client and server can send FIN segments simultaneously (simultaneous close), so Option (D) is true."),
    "gate_cs_2026_s1_q19": ("Computer Networks — Application Layer (HTTP)", "Easy", "HTTP/1.1 uses persistent TCP connections by default, allowing multiple objects of the same webpage (A) or multiple webpages on the same server (D) to reuse one TCP connection, and supports pipelining requests without waiting for earlier responses (C). A single TCP connection cannot span different origin servers (B false)."),
    "gate_cs_2026_s1_q20": ("Engineering Mathematics — Linear Algebra", "Medium", "Because M has a non-zero vector v = (0, 1, 0, ..., 0) in its null space, M is singular, so det(M) = 0 (B). Since the null space is a vector subspace, every scalar multiple c*v (for all nonzero real c) is also in the null space, guaranteeing infinitely many (at least two) non-zero vectors (D)."),
    "gate_cs_2026_s1_q21": ("Digital Logic — Boolean Algebra", "Easy", "Evaluating F(P, Q) = (P' + Q) XOR (P'Q): for (P,Q) = (0,0), 1 XOR 0 = 1; for (0,1), 1 XOR 1 = 0; for (1,0), 0 XOR 0 = 0; for (1,1), 1 XOR 0 = 1. This is the XNOR truth table, which equals (P XOR Q)' (A) and equivalently P' XOR Q (C)."),
    "gate_cs_2026_s1_q22": ("Digital Logic — Number Representation", "Medium", "In 8-bit sign-magnitude form, valid values span [-127, +127]. Here X = -0110100_2 = -52 and Y = +1001100_2 = +76. Computing Z = X - Y = -128 (B) and Z = -X + Y = +128 (C) both fall outside [-127, +127], causing arithmetic overflow, while X + Y = +24 and -X - Y = -24 fit in range."),
    "gate_cs_2026_s1_q23": ("Data Structures — Heaps", "Easy", "In a 1-indexed binary heap of n elements, the internal (non-leaf) nodes are indices 1 through floor(n/2), and the leaves are floor(n/2) + 1 through n. Since n is odd, floor(n/2) = (n - 1)/2, so (n + 1)/2 and n are leaves while (n - 1)/2 (B) and (n - 3)/2 (C) are internal nodes (not leaves)."),
    "gate_cs_2026_s1_q24": ("Data Structures — Hashing", "Easy", "Inserting with h(x) = (x + 7) mod 11 and linear probing: 1 -> 8, 13 -> 9, 22 -> 7, 15 -> 0, 11 -> 7 (occupied at 7,8,9 -> placed at 10), and 24 -> 9 (occupied at 9,10,0 -> placed at 1). Among {0, 10, 2, 1}, only position 2 remains empty."),
    "gate_cs_2026_s1_q25": ("Theory of Computation — Context-Free Grammars", "Hard", "Because S -> aSbS | bS | eps allows deriving 'b' via S -> bS -> b and also allows multiple parses when 'b' can be matched inside S or outside (e.g., 'abb' can be derived as a(b)bS -> abb or aS(bS) -> a(b)b -> ab? Specifically 'abb' has S -> aSbS -> abS -> abbS -> abb and S -> aSbS -> a(bS)bS -> abb, so A and B are true). For 'abab', the first 'a' must match the first 'b' via S -> aSbS and the second 'a' must match the second 'b', forcing a unique rightmost derivation (C)."),
    "gate_cs_2026_s1_q26": ("Theory of Computation — Finite Automata", "Easy", "By subset construction, an NFA with 6 states has at most 2^6 = 64 subsets, so any equivalent minimal DFA can have at most 64 states. Therefore 65 (B) and 128 (D) states are impossible, while 32 and 1 are possible."),
    "gate_cs_2026_s1_q27": ("Compiler Design — Compiler Phases", "Easy", "In S1, the string literal \"Hello; lacks a closing double quote, causing an unterminated string token (lexical error). In S3, assigning a char* string literal \"Hello\" to an int* variable causes a type mismatch (semantic error). S2 is valid C."),
    "gate_cs_2026_s1_q28": ("Compiler Design — LL(1) Parsing", "Easy", "An LL(1) grammar must be free of left recursion and must be left-factored so that FIRST sets of alternative productions for the same non-terminal are disjoint (C). LL(1) is predictive without backtracking (A false), cannot be left-recursive (B false), and is strictly less powerful than SLR(1)/LR(1) on grammars (D false)."),
    "gate_cs_2026_s1_q29": ("Operating Systems — Deadlocks", "Easy", "Banker's algorithm is used for deadlock AVOIDANCE rather than deadlock prevention (so A is FALSE). In a resource allocation graph, an assignment edge points from a resource to the process holding it (process-to-resource is a request edge, so C is FALSE). Statements B and D are true."),
    "gate_cs_2026_s1_q30": ("Databases — Functional Dependencies", "Easy", "If P -> R and Q -> S, then by augmentation and union (Armstrong's axioms), PQ -> RS holds (C). If P -> R, then by augmentation PQ -> R holds (D). Options (A) and (B) are invalid FD inferences (e.g., if P -> R holds, Q need not determine R)."),
    "gate_cs_2026_s1_q31": ("Databases — Normalization", "Medium", "A dependency-preserving 3NF decomposition always exists via Bernstein's synthesis algorithm (A), and every relation with atomic domains is already in 1NF (B). However, BCNF decompositions cannot always preserve all functional dependencies (C; e.g., R(A,B,C) with AB -> C, C -> B), whereas 2NF decompositions can always be made dependency-preserving (D false)."),
    "gate_cs_2026_s1_q32": ("Engineering Mathematics — Calculus", "Easy", "As x -> 0+, log_e(1/x) -> +infinity while c1*e^x -> c1. For the right-hand limit lim_{x->0+} f(x) to be finite and equal f(0) = 3, the coefficient c2 must be 0; then c1*e^0 = c1 = 3, giving c1 + c2 = 3."),
    "gate_cs_2026_s1_q33": ("Data Structures — Binary Trees", "Easy", "In a full binary tree (every internal node has 2 children) with n = 23 nodes, total internal nodes = (23 - 1)/2 = 11. Maximum height is achieved by a skewed full tree where each level adds 1 internal node and 1 leaf, giving height equal to the number of internal nodes = 11 edges."),
    "gate_cs_2026_s1_q34": ("Programming in C — Scope & Variables", "Easy", "Inside the if (i < j) block, 'int i = 0;' declares a new local variable that shadows the parameter i. The parameter i remains 9 when printf(\"%d\", i) runs outside the if block, so the output is 9."),
    "gate_cs_2026_s1_q35": ("Operating Systems — Deadlocks", "Easy", "Each of the 5 processes needs at most 2 instances of R. Deadlock occurs if every process holds 1 instance and waits for 1 more (5 instances). With k = 5 + 1 = 6 instances, by the pigeonhole principle at least one process can obtain its 2nd instance, finish, and release both, guaranteeing deadlock freedom."),
    "gate_cs_2026_s1_q36": ("Digital Logic — Floating Point Representation", "Medium", "Decoding IEEE 754 single precision: X = 0x35C00000 has biased exp 107 (2^(-20)) and significand 1.5, so X = 1.5 * 2^(-20). Y = 0x34A00000 has biased exp 105 (2^(-22)) and significand 1.25, so Y = 1.25 * 2^(-22) = 0.3125 * 2^(-20). Adding gives Z = 1.8125 * 2^(-20) = 1.1101_2 * 2^(-20), which encodes as 0x35E80000."),
    "gate_cs_2026_s1_q37": ("Digital Logic — Sequential Circuits", "Medium", "Since D flip-flops satisfy D1 = Q1+ and D0 = Q0+, building the 3-variable Karnaugh maps for Q1+ and Q0+ from the 8-row next-state table directly yields the minimal SOP expressions in Option (B): D1 = P'Q1 + P'Q0 + Q1Q0 and D0 = P'Q0' + P'Q1 + Q1Q0'."),
    "gate_cs_2026_s1_q38": ("Computer Organization — Cache Memory", "Medium", "The cache size (2^23 bytes) and block size (128 = 2^7 bytes) are fixed, giving 2^16 total blocks. In direct-mapped cache, all 16 bits form the index, so M = 32 - 16 - 7 = 9 tag bits. In K-way set-associative cache (K = 2^L), the number of sets drops by a factor of 2^L, reducing index bits by L and increasing tag bits by L, so N = M + L."),
    "gate_cs_2026_s1_q39": ("Data Structures — Linked Lists", "Easy", "Since the list is guaranteed to be non-empty, the base case is a single-node list where head->next == NULL (returning 1), and the recursive step returns 1 + getListSize(head->next). Using head == NULL as base case would return 1 instead of 0 for the empty tail."),
    "gate_cs_2026_s1_q40": ("Data Structures — Binary Search Trees", "Medium", "A complete binary search tree on {1..15} is a perfect binary tree of height 3, so its root must be the median 8, and its root's left and right children must be 4 and 12 (the medians of 1..7 and 9..15). The third inserted element can be 12 (if 4 was 2nd), or a child of 4 (2 or 6) or a child of 12 (10 or 14) if inserted after 4 or 12, but 5 is at depth 3 (child of 6) and cannot be inserted as the 3rd element."),
    "gate_cs_2026_s1_q41": ("Algorithms — Shortest Paths", "Medium", "Every path of length at most k is also a path of length at most k + 1, so the minimum weight over the larger set cannot exceed the previous minimum, making S1 true. However, edge weights can be negative, so along a shortest path from s to v using (u, v) with w(u, v) < 0, we can have dk(u) > dk(v), making S2 false."),
    "gate_cs_2026_s1_q42": ("Compiler Design — Data Flow Analysis", "Hard", "Performing available-expressions data-flow analysis across the edges of the control flow graph in the official figure shows that g*k is available along all incoming paths to B4 (while b+i is not available or killed on one path), and no expression is available on all incoming paths to B5, giving B4: {g*k}, B5: {}."),
    "gate_cs_2026_s1_q43": ("Databases — Relational Algebra & Calculus", "Medium", "In E = {<u> | exists v, exists w (<u, v> in R and <v, w> in S)}, the second attribute of R (R.Q) equals the first attribute of S (S.X), and the first attribute of R (R.P) is projected out. Joining S and R on S.X = R.Q and projecting P yields Option (B)."),
    "gate_cs_2026_s1_q44": ("Computer Networks — Transport Layer (TCP)", "Hard", "During TCP slow start (ssthresh = 10000), the sender transmits 2^k segments in round k (at t = k ms): 1 segment in round 0 (t=0), 2 in round 1 (t=1), ..., cumulatively 2^(k+1) - 1 segments through round k. After round 9 (t = 9 ms), 2^10 - 1 = 1023 segments have been sent, and segment 2000 falls in round 10 (1024 to 2047), so transmission starts at 10 <= t < 11 ms."),
    "gate_cs_2026_s1_q45": ("Computer Networks — Data Link Layer", "Medium", "Transmission time per frame T_t = 1000 bits / 100 kbps = 10 ms, and one-way propagation delay T_p = 100 ms (RTT = 200 ms). For 100% link utilization, W >= 1 + 2*(T_p / T_t) = 1 + 2*(100 / 10) = 21 frames."),
    "gate_cs_2026_s1_q46": ("Engineering Mathematics — Calculus", "Hard", "For x >= 0, |x|/2 - x = -x/2 and x - |x|/2 = x/2, so f(x) = -x^2 / 4. For x < 0, |x|/2 - x = -3x/2 and x - |x|/2 = 3x/2, so f(x) = -9x^2 / 4. Thus f(x) <= 0 everywhere with global/local maximum 0 at x = 0 (A, no local minimum so B false); f'(x) = -x/2 (x >= 0) and -9x/2 (x < 0) matches 0 at x = 0 so f' is continuous over R (C), but its left and right slopes at 0 are -9/2 != -1/2 so f' is not differentiable at 0 (D)."),
    "gate_cs_2026_s1_q47": ("Algorithms — Graph Algorithms", "Hard", "If deg(v) >= k + 1 and v were NOT in S, then S would have to include all >= k + 1 neighbors of v to cover its incident edges, contradicting |S| = k; hence deg(v) >= k + 1 guarantees v in S (A). Being on a path/cycle of length k+1 or a clique of size k does not force v into every minimum vertex cover (e.g., K_k has a cover of size k-1)."),
    "gate_cs_2026_s1_q48": ("Digital Logic — K-Map Minimization", "Medium", "Plotting the 10 minterms {1,2,3,4,5,7,10,12,13,14} on a 4-variable K-map gives essential prime implicants P'S (covering 1,3,5,7) and QR' (covering 4,5,12,13). The remaining minterms 2, 10, 14 are minimally covered by either {P'Q'R, PRS'} (Option B) or {PQS', Q'RS'} (Option D)."),
    "gate_cs_2026_s1_q49": ("Algorithms — Minimum Spanning Trees", "Medium", "By the cycle property of MSTs with distinct weights, the heaviest edge in any cycle C can never belong to the MST (A). By the cut property applied to the cut ({v}, V\\{v}), the lightest edge incident on any vertex v must belong to every MST (D). Counterexamples exist for (B) (lightest edge of a cycle may not be in MST if lighter paths exist) and (C)."),
    "gate_cs_2026_s1_q50": ("Algorithms — Graph Traversal (DFS)", "Medium", "In a DAG, there are no back edges, so for any edge (u, v) we can have a tree/forward edge where u discovers and finishes around v (d[u] < d[v] < f[v] < f[u], A) or a cross edge where v is completely finished before u is discovered (d[v] < f[v] < d[u] < f[u], C). Option (B) corresponds to a back edge (impossible in a DAG), and Option (D) violates the parenthesis theorem of DFS timestamps."),
    "gate_cs_2026_s1_q51": ("Theory of Computation — Formal Languages", "Medium", "Every regular language is context-free, so L2 being regular guarantees L2 is context-free (C). L1 itself can be any arbitrary non-regular or even undecidable language (for example, if L2 = empty set, L1 intersect L2 = empty set is regular regardless of L1), making A, B, and D false in general."),
    "gate_cs_2026_s1_q52": ("Theory of Computation — Context-Free Grammars", "Hard", "In B -> aBb | ab, every step adds 1 'a' and 1 'b' (n_a = n_b). Accounting for the terminals in S -> abaABAbba and A -> aaBBAb | bBabaa, every derived string satisfies n1(s) >= n2(s) (B) and n1(s) <= 2*n2(s) (D)."),
    "gate_cs_2026_s1_q53": ("Compiler Design — Syntax Directed Translation", "Hard", "Both grammars generate '(int | float) id+' (so P = Q, A is true) and populate identical symbol table entries (D). SDD2 (D -> D1 id | T id) uses only bottom-up synthesized attributes and is S-attributed (B), whereas SDD1 passes inherited V.type down."),
    "gate_cs_2026_s1_q54": ("Operating Systems — Virtual Memory", "Medium", "A TLB caches page-table translations for pages present in main memory, and evicting a page invalidates its TLB/cache entries. Thus if a page table miss occurs (page fault, page not in main memory), neither a TLB hit (B) nor a physical-address cache hit (C) is possible."),
    "gate_cs_2026_s1_q55": ("Discrete Mathematics — Graph Theory", "Medium", "A graph is 2-colorable if and only if it is bipartite, which is equivalent to containing NO odd-length cycles (so it may contain even cycles, B, while A is false). Bipartiteness is tested via BFS/DFS 2-coloring in Theta(|V| + |E|) time using adjacency lists (C)."),
    "gate_cs_2026_s1_q56": ("Computer Networks — IP Addressing & Subnets", "Medium", "To assign at least 6000 IP addresses using CIDR, we need 2^13 = 8192 addresses, corresponding to a /19 prefix (32 - 13 = 19). A valid /19 block inside 202.16.0.0/15 must have its 3rd octet divisible by 2^5 = 32 (i.e., 0, 32, 64, 96, ...). Thus 202.16.0.0/19 (A), 202.17.64.0/19 (B), and 202.16.32.0/19 (C) are valid, while 202.17.24.0/19 (24 not divisible by 32) is invalid."),
    "gate_cs_2026_s1_q57": ("Discrete Mathematics — Combinatorics", "Hard", "Let M(n) be the number of matchings (including the empty matching) in a path P_n on n vertices. Either vertex n is unmatched (M(n-1) ways) or matched with vertex n-1 (M(n-2) ways), giving the Fibonacci recurrence M(n) = M(n-1) + M(n-2) with M(1) = 1, M(2) = 2: M(3)=3, M(4)=5, M(5)=8, M(6)=13, M(7)=21, and M(8)=34."),
    "gate_cs_2026_s1_q58": ("Engineering Mathematics — Probability", "Easy", "E[X] = (1/6)*(1 + 2 + 5 + 7) + (1/12)*(3 + 4 + 6 + 8) = 15/6 + 21/12 = 5/2 + 7/4 = 17/4 = 4.25 (within 4.24 to 4.26)."),
    "gate_cs_2026_s1_q59": ("Operating Systems — Disk Scheduling & I/O", "Medium", "At 15000 rpm (250 rps), 1 rotation = 4 ms, average rotational latency = 2 ms, and 1-sector transfer time = 4/400 = 0.01 ms. Head movement across tracks 0 -> 5 -> 12 -> 7 takes 5 + 7 + 5 = 17 ms. Reading 30 random sectors (10 per track) takes 30 * (2 + 0.01) = 60.3 ms, for a total of 17 + 60.3 = 77.3 ms."),
    "gate_cs_2026_s1_q60": ("Computer Organization — Pipelining", "Hard", "With a 1 ns clock cycle, an instruction needing t_EX ns occupies the EX stage for ceil(t_EX) cycles, stalling subsequent instructions by ceil(t_EX) - 1 cycles. Summing stalls: LOAD (1*15) + IMUL (1*10) + IDIV (2*5) + FADD (1*10) + FSUB (1*5) + FMUL (2*15) + FDIV (3*5) + Others (0*35) = 15 + 10 + 10 + 10 + 5 + 30 + 15 = 95 cycles."),
    "gate_cs_2026_s1_q61": ("Programming in C — Recursion", "Medium", "bar(n) computes floor(log2(n)) for n >= 1. foo(n) counts repeated applications of floor(log2) until reaching 1 plus 1: foo(1)=1, foo(2)=2 (bar(2)=1), foo(4)=3 (bar(4)=2), foo(16)=4 (bar(16)=4), and foo(65536)=5 (bar(65536)=16). Thus the smallest such n is 2^16 = 65536."),
    "gate_cs_2026_s1_q62": ("Data Structures — Binary Search Trees", "Medium", "Reconstructing the BST from preorder [50, 25, 13, 40, 30, 47, 75, 60, 70, 80, 77]: left subtree of 50 has [25, 13, 40, 30, 47] (5 nodes, postorder: 13, 30, 47, 40, 25); right subtree of 50 has root 75, whose left subtree is 60 with right child 70. Postorder of the right subtree starts with 70 (position 6) followed by 60 (position 7)."),
    "gate_cs_2026_s1_q63": ("Operating Systems — Process Management", "Medium", "In each iteration i = 0, 1, 2, the parent breaks out of the loop and calls printf, while the newly forked child continues to the next iteration. After 3 iterations, the original process plus 2 intermediate children and 1 final child (when i reaches 3) reach printf, executing printf 4 times in total."),
    "gate_cs_2026_s1_q64": ("Operating Systems — CPU Scheduling", "Medium", "Simulating FCFS (A takes 6s, C takes 8s): A1(10->10..16, WT=0), C1(11->16..24, WT=5), A2(20->24..30, WT=4), C2(22->30..38, WT=8), A3(30->38..44, WT=8), C3(33->44..52, WT=11), A4(40->52..58, WT=12), C4(44->58..66, WT=14), A5(50->66..72, WT=16), C5(55->72..80, WT=17). Total WT = 0+5+4+8+8+11+12+14+16+17 = 95 s, so average WT = 95 / 10 = 9.5 s."),
    "gate_cs_2026_s1_q65": ("Databases — Functional Dependencies & Keys", "Easy", "The candidate keys are AB and AC. Using inclusion-exclusion on subsets of {A, B, C, D}: superkeys containing AB = 2^2 = 4, superkeys containing AC = 2^2 = 4, and superkeys containing ABC = 2^1 = 2. Total superkeys = 4 + 4 - 2 = 6."),

    # --- GATE CS 2026 Set 2 ---
    "gate_cs_2026_s2_q01": ("Verbal Aptitude — Vocabulary", "Easy", "'Expedite', 'Hasten', and 'Hurry' are all synonyms meaning to speed up or cause something to happen sooner. 'Accelerate' shares this exact meaning, whereas 'Retard', 'Provide', and 'Disable' do not."),
    "gate_cs_2026_s2_q02": ("Spatial Aptitude — Visual Reasoning", "Easy", "Matching the complementary edge profile and corner geometry needed to complete square PQRS from the piece in Panel I identifies shape (iii) in Panel II (Option C; refer to the official figures)."),
    "gate_cs_2026_s2_q03": ("Quantitative Aptitude — Probability", "Easy", "Each day is independently cloudy with p = 0.5. By the binomial distribution, the probability of 3 cloudy days and 1 sunny day in 4 days is C(4, 3) * (0.5)^3 * (0.5)^1 = 4 / 16 = 1/4."),
    "gate_cs_2026_s2_q04": ("Quantitative Aptitude — Profit & Loss", "Easy", "The investor buys 100/50 = 2 shares of Stock A and 80/80 = 1 share of Stock B (total investment Rs. 180). The next day, selling them yields 2*55 + 1*70 = 110 + 70 = Rs. 180, so the profit is 180 - 180 = Rs. 0."),
    "gate_cs_2026_s2_q05": ("Analytical Aptitude — Logical Deduction", "Easy", "The statement 'When it is raining (R), peacocks dance (D)' is the implication R -> D. Its logically equivalent contrapositive is not D -> not R: 'When peacocks are not dancing, it is not raining' (Option C)."),
    "gate_cs_2026_s2_q06": ("Verbal Aptitude — Analogy", "Easy", "Water satisfies/relieves thirst, just as food satisfies/relieves hunger. Thus P = Thirst and Q = Hunger completes the analogy."),
    "gate_cs_2026_s2_q07": ("Spatial Aptitude — Visual Reasoning", "Medium", "Continuity of lines, shading, and rotational symmetry across the pattern in Panel I uniquely determines the two missing tiles as option (i) in Panel II (Option A; refer to the official figure)."),
    "gate_cs_2026_s2_q08": ("Analytical Aptitude — Graph Puzzle", "Medium", "The required trip is a Hamiltonian cycle (visiting every vertex once and returning to start). Inspecting the two highway graphs shows graph (i) contains a Hamiltonian cycle while graph (ii) has a cut vertex/degree-1 bottleneck preventing one (Option A; refer to the official diagram)."),
    "gate_cs_2026_s2_q09": ("Analytical Aptitude — Grid Puzzle", "Medium", "Checking the row sums and column sums specified along the left and top edges of Panel I against the shaded 4 x 4 grids in Panel II uniquely matches grid (ii) (Option B; refer to the official figure)."),
    "gate_cs_2026_s2_q10": ("Quantitative Aptitude — Probability", "Easy", "Two dice give 36 equally likely sums from 2 to 12. The prime sums are 2 (1 way), 3 (2 ways), 5 (4 ways), 7 (6 ways), and 11 (2 ways), totaling 1 + 2 + 4 + 6 + 2 = 15 favorable outcomes, so probability = 15/36."),
    "gate_cs_2026_s2_q11": ("Discrete Mathematics — Predicate Logic", "Easy", "'There is a person y' uses (exists y), and 'every other person x (x != y) knows y and y does not know x' translates to (forall x)((x != y) -> (M(x, y) and not M(y, x))), matching Option (A)."),
    "gate_cs_2026_s2_q12": ("Data Structures — Binary Trees", "Easy", "Inorder visits left subtree, node, right subtree (I-L); Preorder visits node, left subtree, right subtree (II-M); Postorder visits left subtree, right subtree, node (III-N)."),
    "gate_cs_2026_s2_q13": ("Theory of Computation — Turing Machines", "Easy", "By definition, a Turing machine M decides a language L if it halts on every input string in {0,1}*, accepting all strings in L and rejecting all strings in {0,1}* - L (Option D)."),
    "gate_cs_2026_s2_q14": ("Engineering Mathematics — Probability", "Easy", "The given PDF f(x) = (1 / (3 * sqrt(2*pi))) * exp(-x^2 / (2 * 3^2)) over (-inf, +inf) matches the standard normal distribution N(mu, sigma^2) with mean mu = 0 and standard deviation sigma = 3."),
    "gate_cs_2026_s2_q15": ("Databases — DBMS Architecture", "Easy", "In the three-schema DBMS architecture, the Logical (conceptual) schema defines Relations and constraints (I-N), the Physical (internal) schema specifies File organization and indexes (II-M), and the External schema defines user Views (III-L)."),
    "gate_cs_2026_s2_q16": ("Digital Logic — Boolean Algebra", "Easy", "In Boolean algebra, the complement law for AND states that a . a' = 0 (not 1), so Option (B) is not a property of Boolean algebra. Commutativity (A, D) and a + a' = 1 (C) are standard axioms."),
    "gate_cs_2026_s2_q17": ("Programming in C — Memory Management", "Easy", "In a C runtime environment, dynamically allocated memory via malloc()/calloc() resides on the heap (C). Static variables live in the data/BSS segment, and local arrays and return addresses live on the call stack."),
    "gate_cs_2026_s2_q18": ("Computer Organization — I/O & Interrupts", "Medium", "In non-vectored interrupts, the CPU jumps to a fixed handler and polls devices to identify the interrupter, taking longer to start the specific ISR than vectored interrupts (S1 true). In daisy-chain interrupts, the interrupt acknowledge signal propagates down the hardware chain so the CPU does NOT poll every device individually (S2 false)."),
    "gate_cs_2026_s2_q19": ("Programming in C — Scope & Variables", "Easy", "In P1, the local 'int a = 7;' inside main() validly shadows the global 'int a = 5;'. In P2 and P3, redeclaring the variable 'a' in the exact same block scope causes a compilation error, so only P1 compiles cleanly."),
    "gate_cs_2026_s2_q20": ("Databases — Transactions & Concurrency", "Easy", "Two operations on the same data item A conflict if at least one of them is a write (RW, WR, or WW). Therefore, T1 and T2 do not conflict on A only if both transactions only read A (Option A)."),
    "gate_cs_2026_s2_q21": ("Computer Networks — Data Link & Delays", "Easy", "The bottleneck link bandwidth along the path is min(2 Mbps, 500 kbps, 1 Mbps) = 500 kbps = 500 * 10^3 bits/sec. File size = 4 * 10^6 bytes = 32 * 10^6 bits. With negligible propagation/processing delays, transfer time = (32 * 10^6) / (500 * 10^3) = 64 seconds."),
    "gate_cs_2026_s2_q22": ("Computer Networks — Application Layer (DHCP)", "Easy", "DHCP clients do not initially have an IP address or know the DHCP server's address, so they broadcast DHCPDISCOVER (and DHCPREQUEST) packets across the local subnet. SMTP, FTP, and HTTP operate over unicast TCP connections."),
    "gate_cs_2026_s2_q23": ("Operating Systems — CPU Scheduling", "Easy", "First Come First Serve (FCFS) strictly runs processes in arrival order to completion (or I/O block) and is inherently non-preemptive. SRTF and Round Robin are preemptive by definition, and Priority Scheduling can be preemptive."),
    "gate_cs_2026_s2_q24": ("Algorithms — Asymptotic Analysis", "Easy", "Notice 2^(log2 n) = n, and by Stirling's approximation log(n!) = Theta(n log n). Comparing asymptotic growth: log(n) << n^(1/3) << n = 2^(log n) << n log n = Theta(log(n!)), which matches Option (A)."),
    "gate_cs_2026_s2_q25": ("Algorithms — Recurrence Relations", "Easy", "Solving T(n) = T(n-1) + 1 gives T(n) = n = Theta(n) (A). For T(n) = 2T(n/2) + 1, Master Theorem Case 1 gives Theta(n^(log_2 2)) = Theta(n) (B). Options (C) and (D) solve to Theta(n log n) and Theta(n^2), respectively."),
    "gate_cs_2026_s2_q26": ("Discrete Mathematics — Sets & Relations", "Medium", "(x, y) in R iff xy is a perfect square. x*x = x^2 is always a square (Reflexive, A); xy = yx (Symmetric, B); if xy = a^2 and yz = b^2, then xz = (ab/y)^2 is a rational square of integers hence a perfect square (Transitive, C). Since (1, 4) and (4, 1) are both in R with 1 != 4, R is not antisymmetric."),
    "gate_cs_2026_s2_q27": ("Engineering Mathematics — Calculus", "Easy", "Evaluating I(a) = integral_{-1}^1 (3x^2 - ax + 1) dx: the odd term -ax integrates to 0 over [-1, 1], leaving [x^3 + x]_{-1}^1 = 2 + 2 = 4. Thus I(a) = 4 is independent of a (A) and is always positive (C), never negative."),
    "gate_cs_2026_s2_q28": ("Digital Logic — Number Representation", "Easy", "In 4-bit 2's complement, the representable range is [-8, +7]. Here N1 = -5, N2 = -3, N3 = -6, N4 = -7. Checking operations: N1 + N2 = -8 (fits), N2 + N3 = -9 (overflow, B), N3 - N4 = +1 (fits), and N1 + N4 = -12 (overflow, D)."),
    "gate_cs_2026_s2_q29": ("Compiler Design — Grammars & Parsing", "Medium", "E -> E + E | E * E | id is ambiguous due to lacking precedence/associativity (e.g., two parse trees for id + id * id, B). S -> aS | Sa | eps is ambiguous because 'a' can be generated as a(S) or (S)a (C). Grammars (A) and (D) are unambiguous."),
    "gate_cs_2026_s2_q30": ("Data Structures — Hashing", "Easy", "Hashing with h(k) = k mod 9: 5->5, 28->1, 19->1, 15->6, 26->8, 33->6, 12->3, 17->8, 10->1. Bucket 1 holds {28, 19, 10} (length 3), bucket 6 holds {15, 33} (length 2), and bucket 8 holds {26, 17} (length 2), so the longest chain has length 3."),
    "gate_cs_2026_s2_q31": ("Engineering Mathematics — Linear Algebra", "Easy", "For ax + y = b and 16x + ay = 24 to have infinitely many (multiple) solutions, the coefficients must be proportional: a/16 = 1/a = b/24. From a^2 = 16 we get a = +/- 4, and from b = 24/a we get b = +/- 6 (with matching signs), so in both cases a*b = 24."),
    "gate_cs_2026_s2_q32": ("Algorithms — Sorting & Divide-and-Conquer", "Medium", "Tracing the 7 merges on A = [10, 7, 8, 19, 41, 35, 25, 31]: leaf pairs give [10],[7]->[7,10] (not void), [8],[19]->[8,19] (VOID), [41],[35]->[35,41] (not void), [25],[31]->[25,31] (VOID); next level gives [7,10],[8,19]->[7,8,10,19] (not void) and [35,41],[25,31]->[25,31,35,41] (not void); final merge [7,8,10,19],[25,31,35,41] appends R after L (VOID). Thus 3 merges are void."),
    "gate_cs_2026_s2_q33": ("Computer Networks — IP Addressing & Subnets", "Easy", "Subnet mask 255.255.240.0 has 12 host bits (32 - 20 = 12, since 240 = 11110000_2 leaves 4 bits in the 3rd octet + 8 bits in the 4th). Excluding the all-0s network address and all-1s broadcast address leaves 2^12 - 2 = 4096 - 2 = 4094 assignable IP addresses."),
    "gate_cs_2026_s2_q34": ("Digital Logic — Floating Point Representation", "Medium", "0xC2710000 in binary is 1 10000100 1110001000... Sign bit 1 gives negative; biased exponent 10000100_2 = 132 gives 2^(132-127) = 2^5; mantissa 1.1110001_2 = 1 + 1/2 + 1/4 + 1/8 + 1/128 = 1.8828125. Multiplying -1.8828125 * 32 = -60.25."),
    "gate_cs_2026_s2_q35": ("Compiler Design — Lexical Analysis", "Medium", "Applying longest-match tokenization (id starts with letter, number is digits+): 'x1' (id), '23' (num), 'mm' (id), '78' (num), 'y' (id), '7' (num), 'z' (id), 'zz5' (id), '14' (num), 'A' (id), '8' (num), 'H' (id), 'AaYcD' (id). Counting all tokens excluding whitespace gives 13 tokens."),
    "gate_cs_2026_s2_q36": ("Discrete Mathematics — Graph Theory", "Hard", "In K_n for n > 4, the maximum number of edge-disjoint spanning trees is floor(n/2) >= 2 (each using n - 1 edges, since C(n, 2) >= 2(n - 1) for n >= 4). Picking two edge-disjoint spanning trees T1 and T2 gives |T1 intersect T2| = 0, making the Jaccard coefficient 0."),
    "gate_cs_2026_s2_q37": ("Algorithms — Shortest Paths", "Medium", "In a weighted DAG, single-source shortest paths can be computed in Theta(m + n) worst-case time by topologically sorting the vertices in Theta(m + n) and relaxing outgoing edges once in topological order."),
    "gate_cs_2026_s2_q38": ("Algorithms — Time Complexity", "Medium", "The condition states that consecutive differences d[i] = A[i+1] - A[i] are strictly increasing (d[1] < d[2] < ... < d[n-1]). Checking d[i] < d[i+1] in a single linear scan takes Theta(n) time, and reading all n elements is necessary in the worst case, so Theta(n) is optimal."),
    "gate_cs_2026_s2_q39": ("Algorithms — Dynamic Programming", "Medium", "T[i][j] depends only on T[i-1][j] (top neighbor) and T[i][j-1] (left neighbor). Algorithm B1 iterates row-by-row (top-to-bottom, left-to-right), and Algorithm B2 iterates along anti-diagonals i + j = s in increasing order; in both orders both dependencies are already computed, so both B1 and B2 are correct."),
    "gate_cs_2026_s2_q40": ("Digital Logic — K-Map Minimization", "Easy", "Minterms {0,1,2,3,8,9,10,11} correspond to all combinations where bit B = 0 (since 0..3 have AB=00 and 8..11 have AB=10, while C and D vary over all 4 combinations). Thus all 8 minterms combine into the single prime implicant B'."),
    "gate_cs_2026_s2_q41": ("Compiler Design — LR Parsing", "Hard", "Building the canonical LR(0) automaton for S' -> .S, S -> .ACB, A -> .aA | .eps, C -> .cC | .eps, B -> .bB | .b: any state containing a completed epsilon-reduction item [A -> .] or [C -> .] alongside shift items (e.g., shift 'a' vs reduce A -> eps in I0 and after 'a'; shift 'c' vs reduce C -> eps after A and after 'c'; plus shift 'b' vs reduce B -> b. in the state after 'b' where [B -> b.] and [B -> b.B] coexist) produces 5 states/actions with shift-reduce conflicts in the LR(0) table."),
    "gate_cs_2026_s2_q42": ("Databases — Functional Dependencies", "Medium", "To prove Union (from X -> Y and X -> Z, derive X -> YZ): apply Augmentation to X -> Y using X to get X -> XY; apply Augmentation to X -> Z using Y to get XY -> YZ; then apply Transitivity to X -> XY and XY -> YZ to get X -> YZ. Reflexivity is not needed, so Augmentation and Transitivity are both necessary and sufficient."),
    "gate_cs_2026_s2_q43": ("Computer Networks — Data Link Layer (CRC)", "Medium", "Generator 1001 has degree 3, so append three 0s to data 110001011 -> 110001011000. Performing modulo-2 polynomial division (XOR) by 1001 leaves the 3-bit remainder 100."),
    "gate_cs_2026_s2_q44": ("Computer Organization — Instruction Formats", "Hard", "Each instruction is 16 bits and registers need 4 bits. M-type uses 2 regs + 6-bit imm = 14 bits (leaving 2-bit opcode prefixes: 2 out of 4 prefixes used, leaving 2 free 2-bit prefixes, i.e., 2 * 4 = 8 four-bit slots). R-type uses 3 regs = 12 bits (4-bit opcode: 7 out of those 8 slots used, leaving 1 four-bit prefix free). C-type uses 1 reg + 6-bit offset = 10 bits (6-bit opcode), and extending the remaining 1 four-bit prefix by 2 more bits yields 2^2 = 4 C-type opcodes."),
    "gate_cs_2026_s2_q45": ("Compiler Design — Data Flow Analysis", "Hard", "Performing backward live-variable analysis across the basic blocks in the official CFG figure (computing OUT[B] = union of IN[succ] and IN[B] = USE[B] union (OUT[B] - DEF[B])) yields live-out sets B1:{a,b,c,e,f}, B2:{d,e}, B3:{b,c,e,f}, B4: empty (Option A)."),
    "gate_cs_2026_s2_q46": ("Databases — Indexing & B+ Trees", "Medium", "A hash index hashes every search-key value to a bucket containing pointers to records, so it must have an entry for every search-key value (always dense, S1 true). In a B+ tree built on a sequentially ordered file, leaf entries can point only to the first record of each block (sparse index, S2 true)."),
    "gate_cs_2026_s2_q47": ("Theory of Computation — Finite Automata", "Hard", "Inspecting automata D1 and D2 in the official figure shows their languages share only the empty string epsilon (L(D1) intersect L(D2) = {eps}, C), and taking (L(D1) union L(D2))* accepts exactly all strings over {0, 1}* whose length is a multiple of 3 (D)."),
    "gate_cs_2026_s2_q48": ("Theory of Computation — Context-Free Languages", "Hard", "A PDA can push 'a's, match or adjust against 'b's, push 'c's, and pop against 'd's whenever the constraints pair adjacent or nested counters: i+k = j+l (A: push for a, pop for b, push/pop balance for c and d), i = l and j = k (C: push a's, push b's, pop b's with c's, pop a's with d's), and i+j = k+l (D: push for a and b, pop for c and d). Option (B) i=k and j=l is crossing-dependent (non-CFL)."),
    "gate_cs_2026_s2_q49": ("Data Structures — Binary Search Trees", "Hard", "Because Suc(Li) values are strictly increasing across leaves, the intervals (Val(Li), Val(Suc(Li))) are pairwise disjoint, so K has no duplicates (A). Each new key ki falls strictly between leaf Li and its inorder successor, so it is inserted either as the right child of Li or the leftmost child of Suc(Li) (only adding depth 1 below existing nodes without cascading), increasing the BST height by at most 1 (C). If n=1 (single root leaf), Suc is NULL so K can be empty (B false), and not all nodes are leaves (D false)."),
    "gate_cs_2026_s2_q50": ("Data Structures — Stacks & Queues", "Hard", "Since S is emptied completely before Q, any prefix popped from S must be strictly decreasing in arrival order? No, wait: the output 4 3 1 2 5 has 4 3 decreasing (from S) followed by 1 2 5 increasing (from Q), OR 4 3 1 decreasing (from S) followed by 2 5 increasing (from Q). Note 1 cannot come from S after 3 unless 1 was pushed BEFORE 3 and 4, which gives 4, 3, 1 from S and 2, 5 from Q (Option A: 1S, 2Q, 3S, 4S, 5Q)! And if 1, 2, 5 were enqueued in Q and 3, 4 pushed to S, popping S gives 4, 3 and dequeuing Q gives 1, 2, 5 (Option B: 1Q, 2Q, 3S, 4S, 5Q). Options (C) and (D) cannot produce 4 3 1 2 5."),
    "gate_cs_2026_s2_q51": ("Operating Systems — Synchronization", "Medium", "Wait(A) and Signal(A) enforce mutual exclusion around Print(*), X = X+1, and Print($) (when X == 2). Thus the 2nd process prints '$' before releasing A, so the 3rd process can only print its '*' AFTER '$' (allowing A, B, and C), whereas '***$###' (D) is impossible."),
    "gate_cs_2026_s2_q52": ("Computer Organization — Cache Memory", "Hard", "With a 4 KB direct-mapped cache and 16-byte blocks, there are 256 blocks: bits [3:0] = offset (1 hex digit), bits [11:4] = index (2 hex digits), bits [23:12] = tag. Addresses: P=0x845B32 (tag 845, idx B3), Q=0x845B26 (tag 845, idx B2), R=0x845B36 (tag 845, idx B3), S=0x846B32 (tag 846, idx B3). P, R, and S all map to index B3: P (tag 845) misses every time because S (tag 846) evicts it at the end of every cycle (A), while R shares the exact same block (845, B3) loaded by P just before it and hits on every access (B)."),
    "gate_cs_2026_s2_q53": ("Operating Systems — File Systems", "Medium", "Total disk blocks = 16 GB / 2 KB = 2^34 / 2^11 = 2^23 = 8,388,608 blocks. Each 2 KB (2048-byte) list block uses 4 bytes for the next-block pointer, leaving 2044 bytes to store 2044 / 4 = 511 block numbers. Thus ceil(8,388,608 / 511) = ceil(16416.0626) = 16417 blocks are required."),
    "gate_cs_2026_s2_q54": ("Operating Systems — Virtual Memory", "Medium", "With 4 KB pages and 1 MB TLB reach, the TLB has 1 MB / 4 KB = 256 entries. For 64 GB (2^36 B) virtual and 1 GB (2^30 B) physical memory with 12-bit page offset, VPN = 24 bits and PFN = 18 bits. Each entry holds 4 (pid) + 24 (VPN) + 18 (PFN) + 2 (control) = 48 bits = 6 bytes, so TLB size = 256 * 6 = 1536 bytes."),
    "gate_cs_2026_s2_q55": ("Operating Systems — Memory Management", "Medium", "Initial holes: {20, 4, 25, 18, 7, 9, 15, 12}. P1 (16 KB) uses best-fit hole 18 KB, leaving a 2 KB hole: {20, 4, 25, 2, 7, 9, 15, 12}. P2 (9 KB) uses exact best-fit hole 9 KB, leaving 0 KB: {20, 4, 25, 2, 7, 15, 12}. The holes strictly smaller than 8 KB are 4 KB, 2 KB, and 7 KB—giving 3 holes."),
    "gate_cs_2026_s2_q56": ("Computer Organization — Cache Memory", "Hard", "Write 0xA2C28 in 20-bit binary: 1010 0010 1100 0010 1000. The cache block index 176_10 in binary is 10110000_2, which matches bits [13:6] of the address, with bits [16:14] = 000 above it (while bit 17 = 1). Extending the index up to bit 16 gives 11 index bits ([16:6]) and 6 block-offset bits ([5:0]), yielding maximum cache size 2^(11 + 6) = 2^17 bytes = 128 KB."),
    "gate_cs_2026_s2_q57": ("Computer Organization — Pipelining", "Medium", "Non-pipelined time per instruction = 5 / 1.6 ns = 3.125 ns. Pipelined CPI = 1 + 0.30 * 2 = 1.6, so pipelined time per instruction = 1.6 / 1.2 ns = 1.3333 ns. Speedup = 3.125 / (1.6 / 1.2) = (5 * 1.2) / (1.6 * 1.6) = 6 / 2.56 = 2.34375 (within 2.30 to 2.40)."),
    "gate_cs_2026_s2_q58": ("Computer Networks — Transport Layer (TCP)", "Medium", "With MSS = 2 KB and ssthresh = 16 KB = 8 MSS, slow start begins at cwnd = 1 MSS (Round 1 sends 1 MSS, cwnd becomes 2), Round 2 sends 2 MSS (cwnd becomes 4), Round 3 sends 4 MSS (cwnd becomes 8 = ssthresh), and the connection enters congestion avoidance on the 4th round of transmission."),
    "gate_cs_2026_s2_q59": ("Digital Logic — Combinational Circuits", "Hard", "In the 2:4 decoder (Q) feeding the 4:1 MUX (M), each combination of (A, B) activates exactly one decoder output line and each combination of (S1, S0) selects one MUX input line (refer to the official circuit wiring). Counting how many of the 16 input combinations [A B S1 S0] route a high (1) signal to Y gives 6 combinations."),
    "gate_cs_2026_s2_q60": ("Programming in C — Pointers", "Medium", "Initially a=5, b=11, c=20. ptr=&a; *ptr=c; sets a=20. Then ptr=&c; a=*(&b); sets a=11, while *ptr still reads c=20. Finally c=*ptr-a sets c=20-11=9, which is printed."),
    "gate_cs_2026_s2_q61": ("Programming in C — Recursion", "Hard", "Let L = end + 1 - start. If L % 3 == 1 (L >= 1), func returns 1 + func(start, end-1) where the new length L-1 satisfies (L-1) % 3 == 0. From any L % 3 == 0, it transitions to L-1 (mod 3 == 2), and from L % 3 == 2 it transitions to L-2 (mod 3 == 0), alternating between 0 and 2 until L < 1 without ever hitting 1 mod 3 again. Thus 1 can be added at most once, making the maximum return value 1."),
    "gate_cs_2026_s2_q62": ("Engineering Mathematics — Linear Algebra", "Easy", "For any n x n matrix A and scalar k, det(kA) = k^n * det(A). Here n = 4, k = 2, and det(A) = 3, so det(2A) = 2^4 * 3 = 16 * 3 = 48."),
    "gate_cs_2026_s2_q63": ("Engineering Mathematics — Probability", "Hard", "Event E1 depends on tosses {2, 4, 6}, while E2 depends on tosses {1, 2, 3, 5}. Note that among tosses {1, 2, 3, 5}, by symmetry P(toss 2 = H | E2) = 1/2 (exactly half of the C(4, 2) = 6 outcomes of E2 have toss 2 = H), and tosses {4, 6} are completely independent of E2! Thus conditional on E2, tosses {2, 4, 6} are still independent fair coins, so P(E1 | E2) = P(at least 2 heads in 3 fair tosses) = (C(3,2) + C(3,3)) / 8 = 4 / 8 = 0.5."),
    "gate_cs_2026_s2_q64": ("Engineering Mathematics — Calculus", "Hard", "In (0, 1), r = 0.d1 d2 ... has f(r) = 1 iff d2 in {2, 3, 6, 7}. For each of the 10 choices of the first digit d1 in {0..9}, f(r) equals 1 on the two intervals [0.d1 2, 0.d1 4) and [0.d1 6, 0.d1 8) (using standard non-terminating/terminating boundary transitions at 0.d1 2, 0.d1 4, 0.d1 6, and 0.d1 8). Each of these 4 points per d1 is a jump discontinuity of f, giving 10 * 4 = 40 discontinuities."),
    "gate_cs_2026_s2_q65": ("Computer Networks — Transport Layer (TCP)", "Medium", "At 10^8 bps = 1.25 * 10^7 bytes/sec over 60 seconds, 60 * 1.25 * 10^7 = 7.5 * 10^8 bytes are transmitted, requiring ceil(log2(7.5 * 10^8)) = 30 bits to avoid sequence number wrap-around before 60 s. Meanwhile, RTT = 2 * 3 * 10^6 m * 5 ns/m = 30 ms, so bandwidth-delay product is 0.03 * 1.25 * 10^7 = 3.75 * 10^5 bytes (~19–20 bits), leaving N = 30 bits."),
}


def build_paper(test_id, cfg):
    qp_path = os.path.join(RAW_PDF_DIR, f"{cfg['raw_prefix']}_qp.pdf")
    key_path = os.path.join(RAW_PDF_DIR, f"{cfg['raw_prefix']}_key.pdf")
    download_pdf(cfg["qp_url"], qp_path)
    download_pdf(cfg["key_url"], key_path)

    keys = parse_answer_key(key_path)
    q_texts = extract_questions_text(qp_path)

    questions = []
    total_marks = 0.0
    ga_marks = 0.0
    cs_marks = 0.0

    for qno in range(1, 66):
        meta = keys[qno]
        total_marks += meta["marks"]
        if qno <= 10:
            ga_marks += meta["marks"]
        else:
            cs_marks += meta["marks"]

        stem, opts = split_options(meta["type"], q_texts[qno], test_id, qno)
        ans_fields = parse_answer_fields(meta)

        if not stem:
            raise ValueError(f"{test_id} Q.{qno}: Empty stem")

        # Sanity check for leftover PUA or control chars
        for txt_check in [stem] + opts:
            for ch in txt_check:
                cp = ord(ch)
                if 0xE000 <= cp <= 0xF8FF or cp == 0xFFFD or (cp < 32 and ch not in "\n\t"):
                    raise ValueError(f"{test_id} Q.{qno}: Unhandled char {hex(cp)} in {txt_check!r}")

        qid = f"{cfg['raw_prefix']}_q{qno:02d}"
        if qid not in QUESTION_DETAILS:
            raise ValueError(f"Missing QUESTION_DETAILS entry for {qid}")
        topic_tag, difficulty, exp_text = QUESTION_DETAILS[qid]
        if not topic_tag or topic_tag in ("General Aptitude", "Computer Science & IT"):
            raise ValueError(f"{qid}: Invalid or generic topicTag '{topic_tag}'")
        if difficulty not in ("Easy", "Medium", "Hard"):
            raise ValueError(f"{qid}: Invalid difficulty '{difficulty}'")
        if not exp_text or exp_text.startswith("Official Answer Key:"):
            raise ValueError(f"{qid}: Missing or placeholder explanation")

        q_obj = {
            "questionId": qid,
            "questionNumber": qno,
            "sectionId": meta["section_id"],
            "sectionTitle": meta["section_title"],
            "questionType": meta["type"],
            "positiveMarks": meta["marks"],
            "negativeMarks": meta["neg"],
            "pyqTag": cfg["pyq_tag"],
            "topicTag": topic_tag,
            "difficulty": difficulty,
            "correctOption": ans_fields["correctOption"],
            "correctOptionsList": ans_fields["correctOptionsList"],
            "correct_index": ans_fields["correct_index"],
            "correct_indices": ans_fields["correct_indices"],
            "natMin": ans_fields["natMin"],
            "natMax": ans_fields["natMax"],
            "questionTextEn": stem,
            "optionsEn": opts,
            "explanationEn": exp_text,
        }
        questions.append(q_obj)

    if abs(total_marks - 100.0) > 0.01 or abs(ga_marks - 15.0) > 0.01 or abs(cs_marks - 85.0) > 0.01:
        raise ValueError(f"{test_id}: Invalid marks total={total_marks}, ga={ga_marks}, cs={cs_marks}")

    test_json = {
        "testId": test_id,
        "categoryId": "gate_cs",
        "test_id": test_id,
        "category_id": "gate_cs",
        "title": cfg["title_en"],
        "titleEn": cfg["title_en"],
        "testType": "PYQ",
        "test_type": "PYQ",
        "isFree": cfg["is_free"],
        "is_free": cfg["is_free"],
        "durationMinutes": 180,
        "duration_minutes": 180,
        "totalQuestions": 65,
        "total_questions": 65,
        "maxMarks": 100.0,
        "positiveMarks": 2.0,
        "negativeMarks": 0.33,
        "examYear": cfg["year"],
        "shiftBadge": cfg["shift_badge"],
        "questions": questions,
    }
    return test_json


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for test_id, cfg in PAPERS.items():
        print(f"Building {test_id}...")
        data = build_paper(test_id, cfg)
        out_path = os.path.join(OUTPUT_DIR, f"{test_id}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        mcq = sum(1 for q in data["questions"] if q["questionType"] == "MCQ")
        msq = sum(1 for q in data["questions"] if q["questionType"] == "MSQ")
        nat = sum(1 for q in data["questions"] if q["questionType"] == "NAT")
        print(f"  [OK] {out_path} -> 65 Qs (MCQ={mcq}, MSQ={msq}, NAT={nat}), 100.0 Marks")


if __name__ == "__main__":
    main()
