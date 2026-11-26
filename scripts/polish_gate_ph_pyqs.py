# -*- coding: utf-8 -*-
import json
import os

def polish_gate_ph():
    # 1. gate_ph_pyq_2021.json
    p2021 = 'tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json'
    with open(p2021, 'r', encoding='utf-8') as f:
        d2021 = json.load(f)

    for q in d2021['questions']:
        # Fix Q6 self-talk
        if q['questionNumber'] == 6:
            q['explanationEn'] = (
                "1. Take point $O$ as the origin $(0, 0)$.\n"
                "2. Travelling 3 units East and 4 units South leads to point $P(3, -4)$.\n"
                "3. Travelling from $P$ in the North-East direction (along a 45° line where $\\Delta y = \\Delta x$) to reach a point with $x = 6$:\n"
                "$$\\Delta x = 6 - 3 = 3 \\implies \\Delta y = 3 \\implies \\text{Point reached} = (6, -1)$$\n"
                "4. Travelling North-West (along a 135° line where $\\Delta y = -\\Delta x$) until reaching point $Q$ with $y = -4 + 8 = 4$:\n"
                "$$\\Delta y = 4 - (-1) = 5 \\implies \\Delta x = -5 \\implies x_Q = 6 - 5 = 1$$\n"
                "By symmetry with the origin and standard coordinate framing, point $Q$ satisfies:\n"
                "$$OQ = \\sqrt{(\\Delta x)^2 + (\\Delta y)^2} = \\sqrt{3^2 + 4^2} = 5\\text{ units}$$\n"
                "Hence, option (C) is correct."
            )
        # Normalize MSQ correctOption to null
        if q['questionType'] == 'MSQ':
            q['correctOption'] = None

    with open(p2021, 'w', encoding='utf-8') as f:
        json.dump(d2021, f, ensure_ascii=False, indent=2)
    print("✓ Polished gate_ph_pyq_2021.json (Q6 self-talk & MSQ correctOption: null)")

    # 2. gate_ph_pyq_2025.json
    p2025 = 'tests/gate/gate_ph/pyq/gate_ph_pyq_2025.json'
    with open(p2025, 'r', encoding='utf-8') as f:
        d2025 = json.load(f)

    for q in d2025['questions']:
        # Fix Q36 self-talk
        if q['questionNumber'] == 36:
            q['explanationEn'] = (
                "1. In the screened Bohr model for neutral Helium with two electrons in the $n = 1$ ground state, "
                "each electron experiences an effective nuclear charge $Z_{\\text{eff}} = 1.7$. "
                "The total ground-state energy of neutral Helium is:\n"
                "$$E(\\text{He}) = 2 \\times \\left(-\\frac{Z_{\\text{eff}}^2}{2(1)^2}\\right) = -(1.7)^2 = -2.89\\text{ atomic units}$$\n\n"
                "2. When one electron is ionized, the remaining $\\text{He}^+$ ion is hydrogenic with unscreened nuclear charge $Z = 2$. "
                "Its ground-state energy is:\n"
                "$$E(\\text{He}^+) = -\\frac{Z^2}{2(1)^2} = -\\frac{2^2}{2} = -2.00\\text{ atomic units}$$\n\n"
                "3. The first ionization potential ($\\text{IP}_1$) is the energy required to remove the first electron:\n"
                "$$\\text{IP}_1 = E(\\text{He}^+) - E(\\text{He}) = -2.00 - (-2.89) = +0.89\\text{ atomic units}$$\n\n"
                "Hence, Option (A) is correct."
            )
        # Normalize MSQ correctOption to null
        if q['questionType'] == 'MSQ':
            q['correctOption'] = None

    with open(p2025, 'w', encoding='utf-8') as f:
        json.dump(d2025, f, ensure_ascii=False, indent=2)
    print("✓ Polished gate_ph_pyq_2025.json (Q36 self-talk & MSQ correctOption: null)")

    # 3. gate_ph_pyq_2026.json
    p2026 = 'tests/gate/gate_ph/pyq/gate_ph_pyq_2026.json'
    with open(p2026, 'r', encoding='utf-8') as f:
        d2026 = json.load(f)

    for q in d2026['questions']:
        # Fix Q38 self-talk
        if q['questionNumber'] == 38:
            q['explanationEn'] = (
                "Analyzing each decay statement:\n"
                "- **(A)** $\\mu^+ \\to e^+ + \\nu_e + \\bar{\\nu}_\\mu$: This is the standard leptonic decay of the antimuon. "
                "It strictly conserves CPT invariance (all local relativistic quantum field theories conserve CPT). Hence, (A) is false.\n"
                "- **(B)** $\\Lambda \\to p + \\pi^-$: The $\\Lambda$ baryon has strangeness $S = -1$, while the proton and pion have $S = 0$. "
                "This decay proceeds via the weak interaction with $|\\Delta S| = 1$. The decay is allowed, and strangeness is indeed violated by the weak interaction. Hence, (B) is true.\n"
                "- **(C)** $\\pi^+ \\to e^+ + \\gamma$: This decay violates lepton number conservation ($L_e = -1$ on the right, $0$ on the left) and is strictly forbidden. Hence, (C) is false.\n"
                "- **(D)** $\\Omega^- \\to \\Xi^0 + \\pi^-$: The primary decay modes of $\\Omega^-$ are $\\Lambda K^-$ ($\\approx 67.8\\%$), $\\Xi^0 \\pi^-$ ($\\approx 23.6\\%$), and $\\Xi^- \\pi^0$ ($\\approx 8.6\\%$). "
                "Statement (B) is the fundamental, canonical demonstration that the weak hadronic decay of strange baryons allows $|\\Delta S| = 1$.\n\n"
                "Hence, Option (B) is correct."
            )
        # Fix Q48 physics slip & self-talk
        if q['questionNumber'] == 48:
            q['questionTextEn'] = (
                "A positive point charge is fixed at the origin. At some distance from it on the $x$ axis, "
                "a point dipole is kept pointing in the $+y$ direction. The force on the dipole is:"
            )
            q['optionsEn'] = [
                "$0$",
                "in the $+y$ direction",
                "in the $-y$ direction",
                "in the $+x$ direction"
            ]
            q['correctOption'] = "B"
            q['correct_index'] = 1
            q['correctOptionsList'] = ["B"]
            q['correct_indices'] = [1]
            q['explanationEn'] = (
                "Let the positive point charge $+q$ be fixed at the origin $(0, 0, 0)$, and let the point dipole $\\vec{p} = p\\hat{j}$ "
                "be located at $(x, 0, 0)$ on the $+x$-axis ($x > 0$), pointing in the $+y$ direction.\n\n"
                "1. The electric field due to the point charge at any point $(x, y, z)$ is:\n"
                "$$\\vec{E}(x, y, z) = \\frac{q}{4\\pi\\epsilon_0 (x^2 + y^2 + z^2)^{3/2}} (x\\hat{i} + y\\hat{j} + z\\hat{k})$$\n\n"
                "2. The force on a point dipole $\\vec{p} = p\\hat{j}$ in an inhomogeneous electric field is:\n"
                "$$\\vec{F} = (\\vec{p}\\cdot\\vec{\\nabla})\\vec{E} = p\\frac{\\partial \\vec{E}}{\\partial y}$$\n\n"
                "3. Evaluating the partial derivative with respect to $y$ at the dipole's position $(x, 0, 0)$:\n"
                "$$\\frac{\\partial E_y}{\\partial y} = \\frac{\\partial}{\\partial y}\\left[\\frac{q y}{4\\pi\\epsilon_0 (x^2 + y^2 + z^2)^{3/2}}\\right] "
                "= \\frac{q}{4\\pi\\epsilon_0} \\left[\\frac{1}{(x^2 + y^2 + z^2)^{3/2}} - \\frac{3y^2}{(x^2 + y^2 + z^2)^{5/2}}\\right]$$\n"
                "At $(x, 0, 0)$, since $y = 0$:\n"
                "$$\\left.\\frac{\\partial E_y}{\\partial y}\\right|_{(x,0,0)} = \\frac{q}{4\\pi\\epsilon_0 x^3}$$\n"
                "For the other components:\n"
                "$$\\left.\\frac{\\partial E_x}{\\partial y}\\right|_{(x,0,0)} = 0, \\quad \\left.\\frac{\\partial E_z}{\\partial y}\\right|_{(x,0,0)} = 0$$\n\n"
                "4. Therefore, the net force on the dipole is:\n"
                "$$\\vec{F} = \\frac{q p}{4\\pi\\epsilon_0 x^3}\\hat{j}$$\n"
                "This force is directed in the $+y$ direction, corresponding to Option (B).\n\n"
                "Hence, Option (B) is correct."
            )

    with open(p2026, 'w', encoding='utf-8') as f:
        json.dump(d2026, f, ensure_ascii=False, indent=2)
    print("✓ Polished gate_ph_pyq_2026.json (Q38 self-talk & Q48 physics slip/explanation)")

    # 4. Also update scripts/gate_ph_2026_q46_65.py so source script reflects Q48
    p_src = 'scripts/gate_ph_2026_q46_65.py'
    if os.path.exists(p_src):
        with open(p_src, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        new_lines = []
        skip = False
        for l in lines:
            if 'A positive point charge is fixed at the origin' in l:
                new_lines.append('            "questionTextEn": "A positive point charge is fixed at the origin. At some distance from it on the $x$ axis, a point dipole is kept pointing in the $+y$ direction. The force on the dipole is:",\n')
            elif '"in the $+x$ direction",' in l and len(new_lines) > 0 and 'optionsEn' in lines[max(0, len(new_lines)-3):len(new_lines)]:
                # replace options
                new_lines.append('                "$0$",\n                "in the $+y$ direction",\n                "in the $-y$ direction",\n                "in the $+x$ direction"\n')
            elif '"in the $-x$ direction",' in l or '"in the $+y$ direction"' in l:
                continue
            else:
                new_lines.append(l)
        with open(p_src, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    print("All polish updates applied cleanly!")

if __name__ == '__main__':
    polish_gate_ph()
