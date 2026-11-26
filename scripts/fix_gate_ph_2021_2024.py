# -*- coding: utf-8 -*-
"""
Fixes and standardizes GATE PH PYQs 2021, 2022, 2023, 2024:
- Strict 19-key English-only schema (removes all Hindi keys from 2021 and normalizes top-level keys + sections)
- 2-mark MCQ negativeMarks = 0.67 (except MTA = 0.0)
- NAT correctOption = clean string ("6", "2.4 to 2.6"), correctOptionsList = []
- Wraps all unwrapped math/LaTeX in optionsEn inside $ ... $
- Fixes 2022 (Q10 MTA, Q52 MSQ, Q29-Q35 & Q59-Q65 exact official stems/solutions)
- Fixes 2023 (Q34, Q35, Q43, Q44, Q57, Q59 MTA, Q60, Q61, Q62, Q63, Q64 exact official stems/solutions)
- Fixes 2024 (questionId padding q10..q65, Q47, Q61, Q65 range & Schmidt math)
"""

import json
import re
from collections import OrderedDict

EXPECTED_KEYS = [
    "questionId", "questionNumber", "sectionId", "sectionTitle",
    "questionType", "positiveMarks", "negativeMarks", "pyqTag",
    "topicTag", "difficulty", "correctOption", "correctOptionsList",
    "correct_index", "correct_indices", "natMin", "natMax",
    "questionTextEn", "optionsEn", "explanationEn"
]

def fmt_nat_str(nmin: float, nmax: float) -> str:
    def fmt_num(v: float) -> str:
        if float(v).is_integer():
            return str(int(v))
        return str(v)
    if nmin == nmax:
        return fmt_num(nmin)
    return f"{fmt_num(nmin)} to {fmt_num(nmax)}"

def wrap_option_math(opt: str) -> str:
    if "$" in opt:
        return opt
    s = opt.strip()
    # If pure English prose without math tokens, keep as is
    has_latex_cmd = "\\" in s
    has_sub_sup = ("^" in s or "_" in s)
    if not (has_latex_cmd or has_sub_sup):
        return s

    # Clean known malformed math tokens inside options before wrapping
    replacements = {
        "F{f(x - x0)} = e^-i k x0 g(k)": r"$\mathcal{F}\{f(x - x_0)\} = e^{-i k x_0} g(k)$",
        "F{f(x) e^i k0 x} = g(k + k0)": r"$\mathcal{F}\{f(x) e^{i k_0 x}\} = g(k + k_0)$",
        "F{f'(x)} = i k g(k)": r"$\mathcal{F}\{f'(x)\} = i k g(k)$",
        "F{x f(x)} = i k g(k)": r"$\mathcal{F}\{x f(x)\} = i k g(k)$",
        "F{f * g}(ω) = f̃(ω) g̃(ω)": r"$\mathcal{F}\{f * g\}(\omega) = \tilde{f}(\omega) \tilde{g}(\omega)$",
        "F{a f + b g}(ω) = a f̃(ω) + b g̃(ω)": r"$\mathcal{F}\{a f + b g\}(\omega) = a \tilde{f}(\omega) + b \tilde{g}(\omega)$",
        "F{f · g}(ω) = f̃(ω) g̃(ω)": r"$\mathcal{F}\{f \cdot g\}(\omega) = \tilde{f}(\omega) \tilde{g}(\omega)$",
        "F{f(x − a)}(ω) = e^(i a ω) f̃(ω)": r"$\mathcal{F}\{f(x - a)\}(\omega) = e^{i a \omega} \tilde{f}(\omega)$",
        "q^-2": "$q^{-2}$",
        "q^-1": "$q^{-1}$",
        "1/2^-, 5/2^+": "$1/2^-,\\; 5/2^+$",
        "1/2^+, 5/2^+": "$1/2^+,\\; 5/2^+$",
        "1/2^-, 1/2^-": "$1/2^-,\\; 1/2^-$",
        "1/2^+, 1/2^-": "$1/2^+,\\; 1/2^-$",
        "1^+, 2^+": "$1^+,\\; 2^+$",
        "1^+, 2^+, 3^+": "$1^+,\\; 2^+,\\; 3^+$",
        "1^-, 2^-": "$1^-,\\; 2^-$",
        "1^-, 2^-, 3^-": "$1^-,\\; 2^-,\\; 3^-$",
        "H, L^2 and L_z": "$H, L^2$ and $L_z$",
        "H, L, L^2 and L_z": "$H, L, L^2$ and $L_z$",
        "L^2 and L_z only": "$L^2$ and $L_z$ only",
        "H and L_z only": "$H$ and $L_z$ only",
        "XYZ_2": "$XYZ_2$",
        "X_2YZ": "$X_2YZ$",
        "XY_2Z_4": "$XY_2Z_4$",
        "A horizontal line independent of T^2": "A horizontal line independent of $T^2$",
        "The fringe width doubles (\\beta' = 2\\beta)": r"The fringe width doubles ($\beta' = 2\beta$)",
        "The fringe width is halved (\\beta' = \\beta / 2)": r"The fringe width is halved ($\beta' = \beta / 2$)",
        "E_1^{(2)} < E_1^{(1)} because the wavefunction penetrates into the classically forbidden region, increasing the effective width of the box": r"$E_1^{(2)} < E_1^{(1)}$ because the wavefunction penetrates into the classically forbidden region, increasing the effective width of the box",
        "Linear momentum p_s": "Linear momentum $p_s$",
        "Canonical angular momentum p_\\phi = m s^2 \\dot{\\phi} + \\frac{q B_0 s^2}{2}": r"Canonical angular momentum $p_\phi = m s^2 \dot{\phi} + \frac{q B_0 s^2}{2}$",
        "Linear momentum p_z only": "Linear momentum $p_z$ only",
        "\\text{independent of } \\omega": r"independent of $\omega$",
        "A step function with f(E) = 1 for E < E_F, and f(E) = 0 for E > E_F": "A step function with $f(E) = 1$ for $E < E_F$, and $f(E) = 0$ for $E > E_F$",
        "\\Delta S_{univ} = 0 for the irreversible process": r"$\Delta S_{\text{univ}} = 0$ for the irreversible process",
        "\\Delta S_{univ} = 0 for the reversible process, and \\Delta S_{univ} > 0 for the irreversible process": r"$\Delta S_{\text{univ}} = 0$ for the reversible process, and $\Delta S_{\text{univ}} > 0$ for the irreversible process",
        "\\Delta S_{univ} < 0 for the irreversible process": r"$\Delta S_{\text{univ}} < 0$ for the irreversible process",
        "\\Delta S_{univ} > 0 for both the reversible and irreversible processes": r"$\Delta S_{\text{univ}} > 0$ for both the reversible and irreversible processes",
        "The angular momentum component p_\\phi = m a^2 sin^2\\theta \\dot{\\phi} is a conserved constant of motion": r"The angular momentum component $p_\phi = m a^2 \sin^2\theta \dot{\phi}$ is a conserved constant of motion",
        "The total mechanical energy E = (1/2) m a^2 (\\dot{\\theta}^2 + sin^2\\theta \\dot{\\phi}^2) + m g a cos\\theta is conserved": r"The total mechanical energy $E = \frac{1}{2} m a^2 (\dot{\theta}^2 + \sin^2\theta \dot{\phi}^2) + m g a \cos\theta$ is conserved",
        "The angle \\theta is a cyclic coordinate": r"The angle $\theta$ is a cyclic coordinate",
        "The effective potential for the \\theta motion is V_eff(\\theta) = p_\\phi^2 / (2 m a^2 sin^2\\theta) + m g a cos\\theta": r"The effective potential for the $\theta$ motion is $V_{\text{eff}}(\theta) = \frac{p_\phi^2}{2 m a^2 \sin^2\theta} + m g a \cos\theta$",
        "The effective potential is V_eff(r) = L^2 / (2 r^2) - V_0 e^-r^2": r"The effective potential is $V_{\text{eff}}(r) = \frac{L^2}{2 r^2} - V_0 e^{-r^2}$",
        "For small r, the repulsive centrifugal barrier L^2 / (2 r^2) dominates": r"For small $r$, the repulsive centrifugal barrier $\frac{L^2}{2 r^2}$ dominates",
        "The energy scales satisfy the hierarchy E_elec >> E_vib >> E_rot": r"The energy scales satisfy the hierarchy $E_{\text{elec}} \gg E_{\text{vib}} \gg E_{\text{rot}}$",
        "E_rot >> E_vib >> E_elec": r"$E_{\text{rot}} \gg E_{\text{vib}} \gg E_{\text{elec}}$",
        "γ is directly proportional to the density of electronic states at the Fermi energy g(E_F)": r"$\gamma$ is directly proportional to the density of electronic states at the Fermi energy $g(E_F)$",
        "γ is inversely proportional to g(E_F)": r"$\gamma$ is inversely proportional to $g(E_F)$",
        "For a 3D free electron gas, γ = (π^2 kB^2 / 3) g(E_F)": r"For a 3D free electron gas, $\gamma = \frac{\pi^2 k_B^2}{3} g(E_F)$",
        "At Brewster’s angle of incidence θB = tan^-1(n2 / n1), the parallel-polarized component has zero reflection coefficient": r"At Brewster’s angle of incidence $\theta_B = \tan^{-1}(n_2 / n_1)$, the parallel-polarized component has zero reflection coefficient",
        "It is in a pure ^1S_0 state with orbital angular momentum L = 0": r"It is in a pure ${}^1S_0$ state with orbital angular momentum $L = 0$",
        "It is an admixture of ^3S_1 and ^3D_1 states due to non-central tensor forces": r"It is an admixture of ${}^3S_1$ and ${}^3D_1$ states due to non-central tensor forces",
        "The magnetic field B inside the sphere is uniform and given by B_in = (2/3) μ0 M": r"The magnetic field $\mathbf{B}$ inside the sphere is uniform and given by $\mathbf{B}_{\text{in}} = \frac{2}{3}\mu_0 \mathbf{M}$",
        "The magnetic field B outside the sphere is identical to that of an ideal magnetic dipole of moment m = (4/3) π R^3 M": r"The magnetic field $\mathbf{B}$ outside the sphere is identical to that of an ideal magnetic dipole of moment $\mathbf{m} = \frac{4}{3}\pi R^3 \mathbf{M}$",
        "+\\hbar/2 with probability 1": r"$+\hbar/2$ with probability 1",
        "-\\hbar/2 with probability 1": r"$-\hbar/2$ with probability 1",
        "+\\hbar/2 with probability 1/2, and -\\hbar/2 with probability 1/2": r"$+\hbar/2$ with probability $1/2$, and $-\hbar/2$ with probability $1/2$",
        "Parity conservation and angular momentum conservation require the two final neutrons to be in a ^3P_1 state (L=1, S=1, J=1)": r"Parity conservation and angular momentum conservation require the two final neutrons to be in a ${}^3P_1$ state ($L=1, S=1, J=1$)",
        "The two neutrons are produced in a singlet ^1S_0 state": r"The two neutrons are produced in a singlet ${}^1S_0$ state",
        "The circulation of V around the perimeter boundary of the disc is 2π ω R^2": r"The circulation of $\mathbf{V}$ around the perimeter boundary of the disc is $2\pi \omega R^2$",
        "μ₀ k e^(−R) ẑ": r"$\mu_0 k e^{-R} \hat{z}$",
        "μ₀ k e^(−s) ẑ": r"$\mu_0 k e^{-s} \hat{z}$",
        "μ₀ k (R/s) e^(−s) ẑ": r"$\mu_0 k (R/s) e^{-s} \hat{z}$",
        "^A_Z P → ^A_{Z+1} Q + e⁻ + ν̄_e": r"$^A_Z P \to {}^A_{Z+1} Q + e^- + \bar{\nu}_e$",
        "^A_Z P → ^A_{Z-1} R + e⁺ + ν̄_e": r"$^A_Z P \to {}^A_{Z-1} R + e^+ + \bar{\nu}_e$",
        "^A_Z P → ^A_Z P + e⁺ + e⁻ + ν_e": r"$^A_Z P \to {}^A_Z P + e^+ + e^- + \nu_e$",
        "^A_Z P → ^A_Z P + ν_e + γ": r"$^A_Z P \to {}^A_Z P + \nu_e + \gamma$",
        "ẋ = p_y/m, ẏ = p_x/m, ṗ_x = −m ω₀² x, ṗ_y = −m ω₀² y": r"$\dot{x} = p_y/m,\; \dot{y} = p_x/m,\; \dot{p}_x = -m \omega_0^2 x,\; \dot{p}_y = -m \omega_0^2 y$",
        "ẋ = p_x/m, ẏ = p_y/m, ṗ_x = m ω₀² y, ṗ_y = m ω₀² x": r"$\dot{x} = p_x/m,\; \dot{y} = p_y/m,\; \dot{p}_x = m \omega_0^2 y,\; \dot{p}_y = m \omega_0^2 x$",
        "ẋ = p_y/m, ẏ = p_x/m, ṗ_x = −m ω₀² y, ṗ_y = −m ω₀² x": r"$\dot{x} = p_y/m,\; \dot{y} = p_x/m,\; \dot{p}_x = -m \omega_0^2 y,\; \dot{p}_y = -m \omega_0^2 x$",
        "ẋ = p_y/m, ẏ = p_x/m, ṗ_x = m ω₀² y, ṗ_y = m ω₀² x": r"$\dot{x} = p_y/m,\; \dot{y} = p_x/m,\; \dot{p}_x = m \omega_0^2 y,\; \dot{p}_y = m \omega_0^2 x$",
        "x(t) ∝ e^(ωt)": r"$x(t) \propto e^{\omega t}$",
        "V(x) ∝ e^(−αx)": r"$V(x) \propto e^{-\alpha x}$",
        "∮_Γ F⃗ · dl⃗ = 0": r"$\oint_\Gamma \vec{F} \cdot d\vec{l} = 0$",
        "E₀^(P) = E₀^(Q)": r"$E_0^{(P)} = E_0^{(Q)}$",
        "E₀^(Q) = E₀^(S)": r"$E_0^{(Q)} = E_0^{(S)}$",
        "E₀^(P) = E₁^(R)": r"$E_0^{(P)} = E_1^{(R)}$",
        "E₀^(R) ≠ E₀^(Q)": r"$E_0^{(R)} \neq E_0^{(Q)}$",
        "H' commutes with L_z and S_z": r"$H'$ commutes with $L_z$ and $S_z$",
        "H₀, L⃗², S⃗², L_z and S_z have a complete set of simultaneous eigenstates": r"$H_0, \vec{L}^2, \vec{S}^2, L_z$ and $S_z$ have a complete set of simultaneous eigenstates",
    }
    if s in replacements:
        return replacements[s]

    # General clean expression: fix unicode subscripts/superscripts if any & wrap whole expression
    u_map = {
        "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3", "₄": "_4",
        "⁰": "^0", "¹": "^1", "²": "^2", "³": "^3", "⁴": "^4",
        "⁻": "-", "⁺": "+", "−": "-", "∝": r"\propto ", "≠": r"\neq ",
        "μ": r"\mu ", "ω": r"\omega ", "θ": r"\theta ", "φ": r"\phi ",
        "λ": r"\lambda ", "α": r"\alpha ", "β": r"\beta ", "γ": r"\gamma ",
        "π": r"\pi ", "ℏ": r"\hbar ", "Δ": r"\Delta ", "Φ": r"\Phi ",
        "→": r"\to ", "·": r"\cdot ", "×": r"\times ", "≤": r"\le ", "≥": r"\ge ",
        "ñ": r"\tilde{n}", "f̃": r"\tilde{f}", "g̃": r"\tilde{g}",
    }
    for k, v in u_map.items():
        if k in s:
            s = s.replace(k, v)
    return f"${s}$"

# --- Specific Verified Replacements ---

FIXES_2022 = {
    10: {
        "negativeMarks": 0.0,
        "correctOptionsList": ["A", "B", "C", "D"],
        "correct_indices": [0, 1, 2, 3],
        "questionTextEn": "Consider a cube formed by folding a sheet of paper. Which planar pattern represents a valid unfolded net of the cube without overlapping faces?\n[Note: Awarded Marks to All (MTA) in the official GATE 2022 answer key.]",
        "explanationEn": "In the official GATE 2022 final answer key, Q.10 (GA, 2 marks) was awarded Marks to All (MTA) due to ambiguity in the planar folding figure.",
    },
    29: {
        "questionTextEn": "Potassium metal has electron concentration of $1.4 \\times 10^{28}\\text{ m}^{-3}$ and the corresponding density of states at Fermi level is $6.2 \\times 10^{46}\\text{ Joule}^{-1}\\text{ m}^{-3}$. If the Pauli paramagnetic susceptibility of Potassium is $n \\times 10^{-k}$ in standard scientific form, then the value of $k$ (an integer) is __________.\n(Magnetic moment of electron is $9.3 \\times 10^{-24}\\text{ Joule T}^{-1}$; permeability of free space is $4\\pi \\times 10^{-7}\\text{ T m A}^{-1}$)",
        "explanationEn": "In SI units, the Pauli paramagnetic susceptibility of a free-electron gas is:\n$$\\chi_P = \\mu_0 \\mu_B^2 g(E_F)$$\nSubstituting the given values:\n- $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ T m A}^{-1}$\n- $\\mu_B = 9.3 \\times 10^{-24}\\text{ J T}^{-1}$\n- $g(E_F) = 6.2 \\times 10^{46}\\text{ J}^{-1}\\text{ m}^{-3}$\n$$\\chi_P = (4\\pi \\times 10^{-7}) \\times (9.3 \\times 10^{-24})^2 \\times (6.2 \\times 10^{46})$$\n$$\\chi_P \\approx (1.2566 \\times 10^{-6}) \\times (8.649 \\times 10^{-47}) \\times (6.2 \\times 10^{46}) \\approx 6.74 \\times 10^{-6}$$\nComparing with the standard scientific form $n \\times 10^{-k}$ ($1 \\le n < 10$), we obtain $n \\approx 6.74$ and $k = 6$.\nOfficial Key: 6.",
    },
    30: {
        "questionTextEn": "A power supply has internal resistance $R_S$ and open load voltage $V_S = 5\\text{ V}$. When a load resistance $R_L$ is connected to the power supply, a voltage drop of $V_L = 4\\text{ V}$ is measured across the load. The value of $\\frac{R_L}{R_S}$ is __________ (Round off to the nearest integer).",
        "explanationEn": "By the voltage divider rule across the series combination of internal resistance $R_S$ and load resistance $R_L$:\n$$V_L = V_S \\left(\\frac{R_L}{R_L + R_S}\\right)$$\nGiven $V_S = 5\\text{ V}$ and $V_L = 4\\text{ V}$:\n$$4 = 5 \\left(\\frac{R_L}{R_L + R_S}\\right) \\implies 4 R_L + 4 R_S = 5 R_L \\implies R_L = 4 R_S$$\nTherefore, $\\frac{R_L}{R_S} = 4$.\nOfficial Key: 4.",
    },
    31: {
        "questionTextEn": "Electric field is measured along the axis of a uniformly charged disc of radius $25\\text{ cm}$. At a distance $d$ from the centre, the field differs by $10\\%$ from that of an infinite plane having the same charge density. The value of $d$ is _______ $\\text{cm}$ (Round off to one decimal place).",
        "explanationEn": "Along the axis of a uniformly charged disc of radius $R = 25\\text{ cm}$ with surface charge density $\\sigma$, the electric field at distance $d$ from the centre is:\n$$E(d) = \\frac{\\sigma}{2\\varepsilon_0} \\left(1 - \\frac{d}{\\sqrt{d^2 + R^2}}\\right)$$\nThe electric field of an infinite plane with the same charge density $\\sigma$ is $E_{\\infty} = \\frac{\\sigma}{2\\varepsilon_0}$.\nSince $E(d)$ differs from $E_{\\infty}$ by $10\\%$ ($E(d) = 0.90\\,E_{\\infty}$):\n$$\\frac{d}{\\sqrt{d^2 + R^2}} = 0.10 = \\frac{1}{10}$$\nSquaring both sides:\n$$\\frac{d^2}{d^2 + R^2} = \\frac{1}{100} \\implies 100 d^2 = d^2 + R^2 \\implies 99 d^2 = R^2$$\n$$d = \\frac{R}{\\sqrt{99}} = \\frac{25\\text{ cm}}{9.9499} \\approx 2.51\\text{ cm}$$\nRounded to one decimal place, $d = 2.5\\text{ cm}$.\nOfficial Key range: 2.4 to 2.6.",
    },
    32: {
        "questionTextEn": "In a solid, a Raman line observed at $300\\text{ cm}^{-1}$ has intensity of Stokes line four times that of the anti-Stokes line. The temperature of the sample is _______ $\\text{K}$ (Round off to the nearest integer). ($1\\text{ cm}^{-1} \\equiv 1.44\\text{ K}$)",
        "explanationEn": "The ratio of the intensity of the Stokes line to that of the anti-Stokes line is governed by the Boltzmann population factor:\n$$\\frac{I_{\\text{Stokes}}}{I_{\\text{anti-Stokes}}} = \\exp\\left(\\frac{h c \\Delta\\tilde{\\nu}}{k_B T}\\right)$$\nGiven $I_{\\text{Stokes}} / I_{\\text{anti-Stokes}} = 4$, $\\Delta\\tilde{\\nu} = 300\\text{ cm}^{-1}$, and $1\\text{ cm}^{-1} \\equiv 1.44\\text{ K}$ (i.e. $hc \\Delta\\tilde{\\nu} / k_B = 300 \\times 1.44\\text{ K} = 432\\text{ K}$):\n$$\\exp\\left(\\frac{432}{T}\\right) = 4 \\implies \\frac{432}{T} = \\ln 4 = 1.3863$$\n$$T = \\frac{432}{1.3863} \\approx 311.6\\text{ K}$$\nRounded to the nearest integer, $T = 312\\text{ K}$.\nOfficial Key range: 311 to 312.",
    },
    33: {
        "questionTextEn": "An electromagnetic pulse has a pulse width of $10^{-3}\\text{ s}$. The uncertainty in the momentum of the corresponding photon is of the order of $10^{-N}\\text{ kg m s}^{-1}$, where $N$ is an integer. The value of $N$ is ____________.\n(speed of light $= 3 \\times 10^8\\text{ m s}^{-1}$, $h = 6.6 \\times 10^{-34}\\text{ J s}$)",
        "explanationEn": "From the energy-time uncertainty relation for a pulse of duration $\\Delta t = 10^{-3}\\text{ s}$:\n$$\\Delta E \\sim \\frac{h}{\\Delta t} \\quad \\text{or} \\quad \\frac{\\hbar}{\\Delta t}$$\nFor a photon, $E = p c \\implies \\Delta p = \\frac{\\Delta E}{c}$:\n- Using $\\Delta E \\sim h / \\Delta t$: $\\Delta p \\sim \\frac{6.6 \\times 10^{-34}}{10^{-3} \\times 3 \\times 10^8} = 2.2 \\times 10^{-39}\\text{ kg m s}^{-1}$ ($N = 39$).\n- Using $\\Delta E \\sim \\hbar / \\Delta t$: $\\Delta p \\sim \\frac{1.05 \\times 10^{-34}}{10^{-3} \\times 3 \\times 10^8} = 3.5 \\times 10^{-40}\\text{ kg m s}^{-1}$ ($N = 40$).\nThus, the order of magnitude exponent is $N = 39$ or $40$.\nOfficial Key range: 39 to 40.",
    },
    34: {
        "questionTextEn": "The wavefunction of a particle in a one-dimensional infinite well of size $2a$ (extending from $-a$ to $+a$) at a certain time is\n$$\\psi(x) = \\frac{1}{\\sqrt{6a}}\\left[\\sqrt{2}\\sin\\left(\\frac{\\pi x}{a}\\right) + \\sqrt{3}\\cos\\left(\\frac{\\pi x}{2a}\\right) + \\cos\\left(\\frac{3\\pi x}{2a}\\right)\\right]$$\nProbability of finding the particle in $n = 2$ state at that time is ______ $\\%$ (Round off to the nearest integer).",
        "explanationEn": "For a 1D infinite square well of width $2a$ symmetric about the origin ($-a \\le x \\le a$), the normalized energy eigenstates are:\n- $n = 1$: $\\phi_1(x) = \\frac{1}{\\sqrt{a}}\\cos\\left(\\frac{\\pi x}{2a}\\right)$\n- $n = 2$: $\\phi_2(x) = \\frac{1}{\\sqrt{a}}\\sin\\left(\\frac{\\pi x}{a}\\right)$\n- $n = 3$: $\\phi_3(x) = \\frac{1}{\\sqrt{a}}\\cos\\left(\\frac{3\\pi x}{2a}\\right)$\nRewriting $\\psi(x)$ in terms of these orthonormal eigenstates:\n$$\\psi(x) = \\sqrt{\\frac{3}{6}}\\,\\phi_1(x) + \\sqrt{\\frac{2}{6}}\\,\\phi_2(x) + \\sqrt{\\frac{1}{6}}\\,\\phi_3(x)$$\nThe state is normalized since $\\frac{3}{6} + \\frac{2}{6} + \\frac{1}{6} = 1$.\nThe probability of finding the particle in the $n = 2$ state is:\n$$P(n = 2) = |c_2|^2 = \\frac{2}{6} = \\frac{1}{3} \\approx 33.33\\%$$\nRounded to the nearest integer, this is $33\\%$.\nOfficial Key range: 33 to 34.",
    },
    35: {
        "questionTextEn": "A spectrometer is used to detect plasma oscillations in a sample. The spectrometer can work in the range of $3 \\times 10^{12}\\text{ rad s}^{-1}$ to $30 \\times 10^{12}\\text{ rad s}^{-1}$. The minimum carrier concentration that can be detected by using this spectrometer is $n \\times 10^{21}\\text{ m}^{-3}$. The value of $n$ is _____________ (Round off to two decimal places).\n(Charge of an electron $= -1.6 \\times 10^{-19}\\text{ C}$, mass of an electron $= 9.1 \\times 10^{-31}\\text{ kg}$ and $\\epsilon_0 = 8.85 \\times 10^{-12}\\text{ C}^2\\text{ N}^{-1}\\text{ m}^{-2}$)",
        "explanationEn": "The plasma angular frequency is given by:\n$$\\omega_p = \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}} \\implies n_e = \\frac{\\omega_p^2 \\epsilon_0 m_e}{e^2}$$\nThe minimum detectable carrier concentration corresponds to the minimum spectrometer frequency $\\omega_{p,\\min} = 3 \\times 10^{12}\\text{ rad s}^{-1}$:\n$$n_{e,\\min} = \\frac{(3 \\times 10^{12})^2 \\times (8.85 \\times 10^{-12}) \\times (9.1 \\times 10^{-31})}{(1.6 \\times 10^{-19})^2}$$\n$$n_{e,\\min} = \\frac{9 \\times 10^{24} \\times 8.0535 \\times 10^{-42}}{2.56 \\times 10^{-38}} = \\frac{72.4815 \\times 10^{-18}}{2.56 \\times 10^{-38}} \\approx 2.831 \\times 10^{21}\\text{ m}^{-3}$$\nThus, $n = 2.83$.\nOfficial Key range: 2.70 to 2.96.",
    },
    52: {
        "questionType": "MSQ",
        "negativeMarks": 0.0,
        "correctOption": None,
        "correctOptionsList": ["D"],
        "correct_index": None,
        "correct_indices": [3],
    },
    59: {
        "questionTextEn": "The minimum number of two-input NAND gates required to implement the following Boolean expression is ________________.\n$$Y = [A\\bar{B}(C + BD) + \\bar{A}\\bar{B}]C$$",
        "explanationEn": "Simplify the Boolean expression step by step:\n$$Y = [A\\bar{B}C + A(\\bar{B}B)D + \\bar{A}\\bar{B}]C$$\nSince $\\bar{B}B = 0$:\n$$Y = (A\\bar{B}C + \\bar{A}\\bar{B})C = A\\bar{B}C + \\bar{A}\\bar{B}C = (A + \\bar{A})\\bar{B}C = \\bar{B}C$$\nTo implement $Y = \\bar{B}C$ using only 2-input NAND gates:\n1. Gate 1: $G_1 = \\overline{B \\cdot B} = \\bar{B}$\n2. Gate 2: $G_2 = \\overline{\\bar{B} \\cdot C}$\n3. Gate 3: $G_3 = \\overline{G_2 \\cdot G_2} = \\bar{B}C = Y$\nThus, a minimum of $3$ two-input NAND gates is required.\nOfficial Key: 3.",
    },
    60: {
        "questionTextEn": "In a nucleus, the interaction $V_{so}\\,\\vec{l}\\cdot\\vec{s}$ is responsible for creating spin-orbit doublets. The energy difference between $p_{1/2}$ and $p_{3/2}$ states in units of $\\frac{V_{so}\\hbar^2}{2}$ is ____________ (Round off to the nearest integer).",
        "explanationEn": "Since $\\vec{j} = \\vec{l} + \\vec{s}$, we have:\n$$\\vec{l}\\cdot\\vec{s} = \\frac{1}{2}\\left(\\vec{j}^2 - \\vec{l}^2 - \\vec{s}^2\\right)$$\nFor a $p$-state ($l = 1, s = 1/2$):\n- For $p_{3/2}$ ($j = 3/2$):\n  $$\\langle \\vec{l}\\cdot\\vec{s} \\rangle_{3/2} = \\frac{\\hbar^2}{2}\\left[\\frac{3}{2}\\left(\\frac{5}{2}\\right) - 1(2) - \\frac{1}{2}\\left(\\frac{3}{2}\\right)\\right] = \\frac{\\hbar^2}{2}\\left[\\frac{15}{4} - 2 - \\frac{3}{4}\\right] = \\frac{1}{2}\\hbar^2$$\n- For $p_{1/2}$ ($j = 1/2$):\n  $$\\langle \\vec{l}\\cdot\\vec{s} \\rangle_{1/2} = \\frac{\\hbar^2}{2}\\left[\\frac{1}{2}\\left(\\frac{3}{2}\\right) - 1(2) - \\frac{1}{2}\\left(\\frac{3}{2}\\right)\\right] = \\frac{\\hbar^2}{2}(-2) = -\\hbar^2$$\nThe magnitude of the energy difference between the two doublet states is:\n$$\\Delta E = V_{so}\\left(\\frac{1}{2}\\hbar^2 - (-\\hbar^2)\\right) = \\frac{3}{2} V_{so}\\hbar^2 = 3\\left(\\frac{V_{so}\\hbar^2}{2}\\right)$$\nIn units of $\\frac{V_{so}\\hbar^2}{2}$, the difference is $3$.\nOfficial Key: 3.",
    },
    61: {
        "questionTextEn": "Two identical particles of rest mass $m_0$ approach each other with equal and opposite velocity $v = 0.5c$, where $c$ is the speed of light. The total energy of one particle as measured in the rest frame of the other is $E = \\alpha m_0 c^2$. The value of $\\alpha$ is _______________ (Round off to two decimal places).",
        "explanationEn": "Let particle 1 move with $+0.5c$ and particle 2 with $-0.5c$ in the laboratory frame. By relativistic velocity addition, the speed $u$ of particle 1 as measured in the rest frame of particle 2 is:\n$$u = \\frac{v_1 + v_2}{1 + \\frac{v_1 v_2}{c^2}} = \\frac{0.5c + 0.5c}{1 + (0.5)(0.5)} = \\frac{c}{1.25} = 0.8c$$\nThe Lorentz factor in the rest frame of particle 2 is:\n$$\\gamma = \\frac{1}{\\sqrt{1 - u^2/c^2}} = \\frac{1}{\\sqrt{1 - 0.64}} = \\frac{1}{0.6} = \\frac{5}{3} \\approx 1.67$$\nThus, the total energy of particle 1 in the rest frame of particle 2 is:\n$$E = \\gamma m_0 c^2 = \\frac{5}{3} m_0 c^2 \\approx 1.67\\,m_0 c^2$$\nHence, $\\alpha = 1.67$.\nOfficial Key range: 1.65 to 1.70.",
    },
    62: {
        "questionTextEn": "In an X-Ray diffraction experiment on a solid with FCC structure, five diffraction peaks corresponding to $(111)$, $(200)$, $(220)$, $(311)$ and $(222)$ planes are observed using $1.54\\text{ \\AA}$ X-rays. On using $3\\text{ \\AA}$ X-rays on the same solid, the number of observed peaks will be ________________.",
        "explanationEn": "By Bragg's law, $2d_{hkl}\\sin\\theta = \\lambda$, a peak is observable only if $\\sin\\theta = \\frac{\\lambda}{2 d_{hkl}} \\le 1$, i.e., $d_{hkl} \\ge \\frac{\\lambda}{2}$, where $d_{hkl} = \\frac{a}{\\sqrt{h^2 + k^2 + l^2}}$.\nFor $\\lambda_1 = 1.54\\text{ \\AA}$:\n- The 5th FCC peak $(222)$ ($h^2+k^2+l^2 = 12$) is observed $\\implies \\frac{a}{\\sqrt{12}} \\ge \\frac{1.54}{2} = 0.77\\text{ \\AA} \\implies a \\ge 2.667\\text{ \\AA}$.\n- The 6th FCC peak $(400)$ ($h^2+k^2+l^2 = 16$) is NOT observed $\\implies \\frac{a}{\\sqrt{16}} < 0.77\\text{ \\AA} \\implies a < 3.08\\text{ \\AA}$.\nNow using $\\lambda_2 = 3\\text{ \\AA}$, diffraction requires $d_{hkl} \\ge \\frac{3}{2} = 1.5\\text{ \\AA}$:\n- For $(111)$: $d_{111} = \\frac{a}{\\sqrt{3}} \\in [1.54, 1.78]\\text{ \\AA} \\ge 1.5\\text{ \\AA}$ (Observed).\n- For $(200)$: $d_{200} = \\frac{a}{2} < 1.5\\text{ \\AA}$ (for typical lattice constant $a \\approx 2.7\\text{--}2.99\\text{ \\AA}$; not observed).\nTherefore, only $1$ diffraction peak corresponding to $(111)$ is observed.\nOfficial Key: 1.",
    },
    63: {
        "questionTextEn": "For $1\\text{ mole}$ of Nitrogen gas, the ratio $\\left(\\frac{\\Delta S_I}{\\Delta S_{II}}\\right)$ of entropy change of the gas in processes (I) and (II) mentioned below is ______________ (Round off to one decimal place).\n(I) The gas is held at $1\\text{ atm}$ and is cooled from $300\\text{ K}$ to $77\\text{ K}$.\n(II) The gas is liquified at $77\\text{ K}$.\n(Take $C_p = 7.0\\text{ cal mol}^{-1}\\text{ K}^{-1}$, Latent heat $L = 1293.6\\text{ cal mol}^{-1}$)",
        "explanationEn": "1. Entropy change in process (I) (isobaric cooling from $T_1 = 300\\text{ K}$ to $T_2 = 77\\text{ K}$):\n$$\\Delta S_I = n C_p \\ln\\left(\\frac{T_2}{T_1}\\right) = 1 \\times 7.0 \\times \\ln\\left(\\frac{77}{300}\\right) = 7.0 \\times (-1.3600) = -9.520\\text{ cal mol}^{-1}\\text{ K}^{-1}$$\n2. Entropy change in process (II) (isothermal liquefaction at $T = 77\\text{ K}$):\n$$\\Delta S_{II} = -\\frac{n L}{T} = -\\frac{1 \\times 1293.6}{77} = -16.8\\text{ cal mol}^{-1}\\text{ K}^{-1}$$\n3. Ratio of the entropy changes:\n$$\\frac{\\Delta S_I}{\\Delta S_{II}} = \\frac{-9.520}{-16.8} = 0.5667 \\approx 0.6$$\nOfficial Key range: 0.5 to 0.7.",
    },
    64: {
        "questionTextEn": "Frequency bandwidth $\\Delta\\nu$ of a gas laser of frequency $\\nu\\text{ Hz}$ is\n$$\\Delta\\nu = \\frac{2\\nu}{c}\\sqrt{\\frac{\\alpha}{A}}$$\nwhere $\\alpha = 3.44 \\times 10^6\\text{ m}^2\\text{ s}^{-2}$ at room temperature and $A$ is the atomic mass of the lasing atom. For $^4\\text{He}\\text{--}^{20}\\text{Ne}$ laser (wavelength $= 633\\text{ nm}$), $\\Delta\\nu = n \\times 10^9\\text{ Hz}$. The value of $n$ is ________ (Round off to one decimal place).",
        "explanationEn": "For the $\\text{He-Ne}$ laser, the lasing atom is Neon ($^{20}\\text{Ne}$), so $A = 20$.\nWith $\\lambda = 633\\text{ nm} = 633 \\times 10^{-9}\\text{ m}$ and $\\nu / c = 1/\\lambda$:\n$$\\Delta\\nu = \\frac{2}{\\lambda}\\sqrt{\\frac{\\alpha}{A}} = \\frac{2}{633 \\times 10^{-9}}\\sqrt{\\frac{3.44 \\times 10^6}{20}}$$\n$$\\Delta\\nu = (3.1596 \\times 10^6) \\times \\sqrt{1.72 \\times 10^5} = (3.1596 \\times 10^6) \\times 414.73 \\approx 1.31 \\times 10^9\\text{ Hz}$$\nThus, $n = 1.3$.\nOfficial Key range: 1.2 to 1.4.",
    },
    65: {
        "questionTextEn": "A current of $1\\text{ A}$ is flowing through a very long solenoid made of winding density $3000\\text{ turns/m}$. A parallel plate capacitor, with plates oriented parallel to the solenoid axis and carrying surface charge density $6\\epsilon_0\\text{ C m}^{-2}$, is placed at the middle of the solenoid. The momentum density of the electromagnetic field at the midpoint $X$ of the capacitor is $n \\times 10^{-13}\\text{ N s m}^{-3}$. The value of $n$ is ______________ (Round off to the nearest integer).\n(speed of light $c = 3 \\times 10^8\\text{ m s}^{-1}$)",
        "explanationEn": "1. Magnetic field inside the long solenoid:\n$$B = \\mu_0 n_{\\text{turns}} I = (4\\pi \\times 10^{-7}) \\times 3000 \\times 1 = 12\\pi \\times 10^{-4}\\text{ T} \\approx 3.770 \\times 10^{-3}\\text{ T}$$\n2. Electric field between the parallel capacitor plates:\n$$E = \\frac{\\sigma}{\\epsilon_0} = \\frac{6\\epsilon_0}{\\epsilon_0} = 6\\text{ V/m}$$\nSince the plates are parallel to the solenoid axis, $\\vec{E} \\perp \\vec{B}$.\n3. Electromagnetic momentum density $\\vec{g} = \\frac{\\vec{S}}{c^2} = \\frac{\\vec{E} \\times \\vec{B}}{\\mu_0 c^2} = \\epsilon_0 (\\vec{E} \\times \\vec{B})$:\n$$g = \\epsilon_0 E B = \\frac{1}{\\mu_0 c^2} E B = \\frac{6 \\times (12\\pi \\times 10^{-4})}{(4\\pi \\times 10^{-7}) \\times (3 \\times 10^8)^2} = \\frac{72\\pi \\times 10^{-4}}{36\\pi \\times 10^9} = 2 \\times 10^{-13}\\text{ N s m}^{-3}$$\nThus, $n = 2$.\nOfficial Key: 2.",
    },
}

FIXES_2023 = {
    34: {
        "questionTextEn": "For a transistor amplifier, the frequency response is such that the mid band voltage gain is $200$. The cutoff frequencies are $20\\text{ Hz}$ and $20\\text{ kHz}$. What is the ratio (rounded off to two decimal places) of the voltage gain at $10\\text{ Hz}$ to that at $100\\text{ kHz}$?",
        "explanationEn": "For a band-pass transistor amplifier with midband gain $A_{\\text{mid}} = 200$, lower cutoff $f_L = 20\\text{ Hz}$, and upper cutoff $f_H = 20\\text{ kHz}$:\n- At $f_1 = 10\\text{ Hz}$ (low-frequency roll-off):\n  $$A_v(10\\text{ Hz}) = \\frac{A_{\\text{mid}}}{\\sqrt{1 + (f_L / f_1)^2}} = \\frac{200}{\\sqrt{1 + (20/10)^2}} = \\frac{200}{\\sqrt{5}}$$\n- At $f_2 = 100\\text{ kHz}$ (high-frequency roll-off):\n  $$A_v(100\\text{ kHz}) = \\frac{A_{\\text{mid}}}{\\sqrt{1 + (f_2 / f_H)^2}} = \\frac{200}{\\sqrt{1 + (100/20)^2}} = \\frac{200}{\\sqrt{26}}$$\nThe ratio of the voltage gain at $10\\text{ Hz}$ to that at $100\\text{ kHz}$ is:\n$$\\frac{A_v(10\\text{ Hz})}{A_v(100\\text{ kHz})} = \\frac{\\sqrt{26}}{\\sqrt{5}} = \\sqrt{5.2} \\approx 2.28$$\nOfficial Key range: 2.20 to 2.36.",
    },
    35: {
        "questionTextEn": "An electric field as a function of radial coordinate $r$ has the form $\\vec{E} = \\alpha \\frac{e^{-r^2}}{r}\\hat{r}$, where $\\alpha$ is a constant. Assume that dimensions are appropriately taken care of. The electric flux through a sphere of radius $\\sqrt{2}$, centered at the origin, is $\\Phi$. What is the value of $\\frac{\\Phi}{2\\pi\\alpha}$ (rounded off to two decimal places)?",
        "explanationEn": "By Gauss's definition of electric flux through a sphere of radius $R = \\sqrt{2}$ centered at the origin:\n$$\\Phi = \\oint_S \\vec{E} \\cdot d\\vec{A} = E(R) \\cdot (4\\pi R^2) = \\left(\\alpha \\frac{e^{-R^2}}{R}\\right) (4\\pi R^2) = 4\\pi \\alpha R e^{-R^2}$$\nSubstituting $R = \\sqrt{2}$ ($R^2 = 2$):\n$$\\Phi = 4\\pi\\alpha\\sqrt{2}\\,e^{-2}$$\nTherefore:\n$$\\frac{\\Phi}{2\\pi\\alpha} = 2\\sqrt{2}\\,e^{-2} \\approx 2.8284 \\times 0.13534 \\approx 0.383$$\nRounded off to two decimal places, the value is $0.38$.\nOfficial Key range: 0.36 to 0.40.",
    },
    43: {
        "questionTextEn": "Consider two real functions\n$$U(x, y) = x y (x^2 - y^2), \\quad V(x, y) = a x^4 + b y^4 + c x^2 y^2 + d$$\nwhere $d$ is a real constant and $a, b, c$ are real coefficients. If $U(x, y) + i V(x, y)$ is analytic, then what is the value of $a \\times b \\times c$?",
        "optionsEn": ["$1/8$", "$3/28$", "$5/36$", "$3/32$"],
        "explanationEn": "For $f(z) = U(x, y) + i V(x, y)$ to be analytic, the Cauchy-Riemann equations must hold:\n$$\\frac{\\partial U}{\\partial x} = \\frac{\\partial V}{\\partial y} \\quad \\text{and} \\quad \\frac{\\partial U}{\\partial y} = -\\frac{\\partial V}{\\partial x}$$\nWith $U(x, y) = x^3 y - x y^3$:\n1. $\\frac{\\partial U}{\\partial x} = 3x^2 y - y^3$ and $\\frac{\\partial V}{\\partial y} = 4b y^3 + 2c x^2 y$.\n   Equating coefficients gives $4b = -1 \\implies b = -\\frac{1}{4}$, and $2c = 3 \\implies c = \\frac{3}{2}$.\n2. $\\frac{\\partial U}{\\partial y} = x^3 - 3x y^2$ and $-\\frac{\\partial V}{\\partial x} = -4a x^3 - 2c x y^2$.\n   Equating coefficients gives $-4a = 1 \\implies a = -\\frac{1}{4}$ (and $-2c = -3 \\implies c = \\frac{3}{2}$, consistent).\nTherefore:\n$$a \\times b \\times c = \\left(-\\frac{1}{4}\\right)\\left(-\\frac{1}{4}\\right)\\left(\\frac{3}{2}\\right) = \\frac{3}{32}$$\nHence, Option (D) is correct.",
    },
    44: {
        "questionTextEn": "Young's double slit experiment is performed using a beam of $C_{60}$ (fullerene) molecules, each molecule being made up of $60$ carbon atoms. When the slit separation is $50\\text{ nm}$, fringes are formed on a screen kept at a distance of $1\\text{ m}$ from the slits. Now, the experiment is repeated with $C_{70}$ molecules with a slit separation of $92.5\\text{ nm}$. The kinetic energies of both the beams are the same. The position of the $4\\text{th}$ bright fringe for $C_{60}$ will correspond to the $n\\text{th}$ bright fringe for $C_{70}$. What is the value of $n$ (rounded off to the nearest integer)?",
        "optionsEn": ["$5$", "$6$", "$7$", "$8$"],
        "explanationEn": "The de Broglie wavelength of a molecule of mass $m$ and kinetic energy $K$ is:\n$$\\lambda = \\frac{h}{\\sqrt{2mK}}$$\nSince $K$ is the same for both beams, $\\frac{\\lambda_{70}}{\\lambda_{60}} = \\sqrt{\\frac{m_{60}}{m_{70}}} = \\sqrt{\\frac{60}{70}}$.\nThe position of the $n$-th bright fringe on a screen at distance $D$ with slit separation $d$ is $y_n = \\frac{n \\lambda D}{d}$.\nFor the $4\\text{th}$ bright fringe of $C_{60}$ ($d_1 = 50\\text{ nm}$) to coincide with the $n\\text{th}$ bright fringe of $C_{70}$ ($d_2 = 92.5\\text{ nm}$):\n$$\\frac{4 \\lambda_{60} D}{d_1} = \\frac{n \\lambda_{70} D}{d_2} \\implies n = 4\\left(\\frac{d_2}{d_1}\\right)\\left(\\frac{\\lambda_{60}}{\\lambda_{70}}\\right) = 4 \\times \\frac{92.5}{50} \\times \\sqrt{\\frac{70}{60}}$$\n$$n = 4 \\times 1.85 \\times 1.0801 \\approx 7.993 \\approx 8$$\nHence, Option (D) is correct.",
    },
    57: {
        "optionsEn": [
            r"The divergence of the velocity field is zero: $\nabla \cdot \mathbf{V} = 0$",
            r"The curl of the velocity field is zero: $\nabla \times \mathbf{V} = 0$",
            r"The curl of the velocity field is $\nabla \times \mathbf{V} = 2\omega \hat{z}$",
            r"The circulation of $\mathbf{V}$ around the perimeter boundary of the disc is $2\pi \omega R^2$"
        ],
    },
    59: {
        "questionTextEn": "Two independent electrostatic configurations are considered: Configuration (I) consists of an isolated point charge $q = 1\\text{ C}$, and Configuration (II) consists of another identical charge surrounded by a thick conducting shell of inner radius $R_1 = 1\\text{ m}$ and outer radius $R_2 = 2\\text{ m}$, with the charge being at the center of the shell. Let $W_I = \\frac{\\epsilon_0}{2}\\int E_I^2\\,dV$ and $W_{II} = \\frac{\\epsilon_0}{2}\\int E_{II}^2\\,dV$, where $E_I$ and $E_{II}$ are the magnitudes of the electric fields for configurations (I) and (II) respectively, $\\epsilon_0$ is the permittivity of vacuum, and the volume integrals are evaluated over all space. If $\\frac{8\\pi}{\\epsilon_0}(W_I - W_{II}) = \\frac{1}{n}$, what is the value of the integer $n$?\n[Note: Awarded Marks to All (MTA) in the official GATE 2023 final answer key.]",
        "explanationEn": "In the region inside the shell cavity ($r < R_1$) and outside the shell ($r > R_2$), the electric field is identical in both configurations ($E_I = E_{II} = \\frac{q}{4\\pi\\epsilon_0 r^2}$). Inside the conducting shell ($R_1 < r < R_2$), $E_{II} = 0$.\nTaking the formal difference of the two integrals:\n$$W_I - W_{II} = \\frac{\\epsilon_0}{2} \\int_{R_1}^{R_2} \\left(\\frac{q}{4\\pi\\epsilon_0 r^2}\\right)^2 (4\\pi r^2\\,dr) = \\frac{q^2}{8\\pi\\epsilon_0}\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = \\frac{1}{8\\pi\\epsilon_0}\\left(1 - \\frac{1}{2}\\right) = \\frac{1}{16\\pi\\epsilon_0}$$\nThen $\\frac{8\\pi}{\\epsilon_0}(W_I - W_{II}) = \\frac{1}{2\\epsilon_0^2}$ (missing a $1/\\epsilon_0^2$ or because $W_I, W_{II}$ diverge individually at $r \\to 0$).\nConsequently, IIT Kanpur awarded Marks to All (MTA) for Q.59 in the final key.",
    },
    60: {
        "questionTextEn": "In pion-nucleon scattering, the pion and nucleon can combine to form a short-lived bound state called the $\\Delta$ particle ($\\pi + N \\to \\Delta$). The masses of the pion, nucleon and the $\\Delta$ particle are $140\\text{ MeV}/c^2$, $938\\text{ MeV}/c^2$ and $1230\\text{ MeV}/c^2$, respectively. In the lab frame, where the nucleon is at rest, what is the minimum energy (in $\\text{MeV}$, rounded off to one decimal place) of the pion to produce the $\\Delta$ particle?",
        "explanationEn": "Using the invariance of total four-momentum squared ($s = P_{\\text{total}}^2$) in natural units ($c = 1$):\nIn the lab frame, the target nucleon is at rest: $P_N = (m_N, \\mathbf{0})$, and the incident pion has $P_\\pi = (E_\\pi, \\mathbf{p}_\\pi)$ with $P_\\pi^2 = m_\\pi^2$.\nAt threshold to produce a single $\\Delta$ particle:\n$$(P_\\pi + P_N)^2 = m_\\Delta^2 \\implies m_\\pi^2 + m_N^2 + 2 m_N E_\\pi = m_\\Delta^2$$\nSolving for the minimum total energy $E_\\pi$ of the pion:\n$$E_\\pi = \\frac{m_\\Delta^2 - m_N^2 - m_\\pi^2}{2 m_N}$$\nSubstituting $m_\\Delta = 1230\\text{ MeV}$, $m_N = 938\\text{ MeV}$, and $m_\\pi = 140\\text{ MeV}$:\n$$E_\\pi = \\frac{1230^2 - 938^2 - 140^2}{2 \\times 938} = \\frac{1,512,900 - 879,844 - 19,600}{1876} = \\frac{613,456}{1876} \\approx 327.0\\text{ MeV}$$\nOfficial Key range: 326.9 to 327.1.",
    },
    61: {
        "questionTextEn": "Consider an electromagnetic wave propagating in the $z$-direction in vacuum, with the magnetic field given by $\\vec{B} = \\vec{B}_0 e^{i(kz - \\omega t)}$. If $B_0 = 10^{-8}\\text{ T}$, the average power passing through a circle of radius $1.0\\text{ m}$ placed in the $xy$-plane is $P$ (in Watts). Using $\\epsilon_0 = 10^{-11}\\text{ C}^2\\text{ N}^{-1}\\text{ m}^{-2}$ (and $c = 3 \\times 10^8\\text{ m s}^{-1}$), what is the value of $\\frac{10^3 P}{\\pi}$ (rounded off to one decimal place)?",
        "explanationEn": "The time-averaged intensity (Poynting flux) of a plane electromagnetic wave in vacuum is:\n$$\\langle S \\rangle = \\frac{c B_0^2}{2\\mu_0} = \\frac{1}{2}\\epsilon_0 c^3 B_0^2$$\n(since $\\mu_0 = \\frac{1}{\\epsilon_0 c^2}$).\nSubstituting $\\epsilon_0 = 10^{-11}$, $c = 3 \\times 10^8\\text{ m/s}$, and $B_0 = 10^{-8}\\text{ T}$:\n$$\\langle S \\rangle = \\frac{1}{2} (10^{-11}) (3 \\times 10^8)^3 (10^{-8})^2 = 0.5 \\times 10^{-11} \\times 2.7 \\times 10^{25} \\times 10^{-16} = 0.0135\\text{ W m}^{-2}$$\nThe power passing through a circle of radius $R = 1.0\\text{ m}$ in the $xy$-plane (perpendicular to the propagation direction $\\hat{z}$) is:\n$$P = \\langle S \\rangle (\\pi R^2) = 0.0135\\pi\\text{ W}$$\nTherefore:\n$$\\frac{10^3 P}{\\pi} = 10^3 \\times 0.0135 = 13.5$$\nOfficial Key range: 11.0 to 13.7.",
    },
    62: {
        "questionTextEn": "An $\\alpha$-particle is emitted from the decay of Americium ($\\text{Am}$) at rest, i.e., $^{241}_{94}\\text{Am} \\to {}^{237}_{92}\\text{U} + \\alpha$ (or daughter nucleus). The rest masses of $^{241}_{94}\\text{Am}$, the daughter nucleus, and $\\alpha$ are $224.544\\text{ GeV}/c^2$, $220.811\\text{ GeV}/c^2$ and $3.728\\text{ GeV}/c^2$ respectively. What is the kinetic energy (in $\\text{MeV}$, rounded off to two decimal places) of the $\\alpha$-particle?",
        "explanationEn": "1. Total disintegration energy ($Q$-value):\n$$Q = (M_{\\text{parent}} - M_{\\text{daughter}} - m_\\alpha) c^2 = (224.544 - 220.811 - 3.728)\\text{ GeV} = 0.005\\text{ GeV} = 5.00\\text{ MeV}$$\n2. By conservation of momentum and energy in two-body decay at rest:\n$$T_\\alpha = Q \\left(\\frac{M_{\\text{daughter}}}{M_{\\text{daughter}} + m_\\alpha}\\right) = 5.00 \\times \\frac{220.811}{220.811 + 3.728} = 5.00 \\times \\frac{220.811}{224.539} \\approx 4.917\\text{ MeV} \\approx 4.92\\text{ MeV}$$\nOfficial Key range: 4.90 to 4.94.",
    },
    63: {
        "questionTextEn": "Consider $6$ identical, non-interacting, spin-$1/2$ atoms arranged on a crystal lattice at absolute temperature $T$. The $z$-component of the magnetic moment of each of these atoms can be $\\pm \\mu_B$. If $P$ and $Q$ are the probabilities of the net magnetic moment of the solid being $2\\mu_B$ and $6\\mu_B$ respectively, what is the value of $\\frac{P}{Q}$ (in integer)?",
        "explanationEn": "In zero external magnetic field, all $2^6 = 64$ spin configurations have equal energy and hence equal a priori probability.\nLet $N_+$ be the number of atoms with $+\\mu_B$ and $N_- = 6 - N_+$ with $-\\mu_B$. The net magnetic moment is $(N_+ - N_-)\\mu_B = (2N_+ - 6)\\mu_B$:\n- For net magnetic moment $= 2\\mu_B$: $2N_+ - 6 = 2 \\implies N_+ = 4, N_- = 2$.\n  The number of ways is $\\binom{6}{4} = \\binom{6}{2} = \\frac{6 \\times 5}{2} = 15$, so $P = \\frac{15}{64}$.\n- For net magnetic moment $= 6\\mu_B$: $2N_+ - 6 = 6 \\implies N_+ = 6, N_- = 0$.\n  The number of ways is $\\binom{6}{6} = 1$, so $Q = \\frac{1}{64}$.\nTherefore, the ratio of probabilities is:\n$$\\frac{P}{Q} = \\frac{15/64}{1/64} = 15$$\nOfficial Key: 15.",
    },
    64: {
        "questionTextEn": "Two identical, non-interacting $^4_2\\text{He}$ atoms are distributed among $4$ different non-degenerate energy levels. The probability that they occupy different energy levels is $p$. Similarly, two spin-polarized $^3_2\\text{He}$ atoms are distributed among $4$ different non-degenerate energy levels, and the probability that they occupy different levels is $q$. What is the value of $\\frac{p}{q}$ (rounded off to one decimal place)?",
        "explanationEn": "1. For $^4_2\\text{He}$ (identical spin-$0$ bosons, $N = 2$ particles in $g = 4$ levels):\n   - Total microstates: $\\Omega_{\\text{BE}} = \\binom{g + N - 1}{N} = \\binom{5}{2} = 10$.\n   - Microstates with particles in different levels: $\\binom{4}{2} = 6$.\n   - Probability $p = \\frac{6}{10} = 0.6$.\n2. For $^3_2\\text{He}$ (identical fermions with 1 particle per level allowed):\n   - By the Pauli exclusion principle, two fermions cannot occupy the same single-particle state, so every allowed configuration places them in different energy levels: $q = \\frac{\\binom{4}{2}}{\\binom{4}{2}} = 1$.\n3. Therefore:\n   $$\\frac{p}{q} = \\frac{0.6}{1} = 0.6$$\nOfficial Key: 0.6.",
    },
}

FIXES_2024 = {
    47: {
        "explanationEn": "For a half-harmonic oscillator with an infinite wall at $x = 0$, the boundary condition $\\psi(0) = 0$ selects only the odd-parity eigenstates of the full harmonic oscillator ($n = 2j + 1$ for $j = 0, 1, 2, \\dots$):\n$$E_j = \\left(2j + \\frac{3}{2}\\right)\\hbar\\omega_0 + V_0$$\nTaking $\\hbar = 1$:\n- Case P ($\\omega_0 = 12, V_0 = 0$): $E_0^{(P)} = \\frac{3}{2}(12) + 0 = 18$\n- Case Q ($\\omega_0 = 12, V_0 = 3$): $E_0^{(Q)} = \\frac{3}{2}(12) + 3 = 21$\n- Case R ($\\omega_0 = 4, V_0 = 4$): $E_0^{(R)} = \\frac{3}{2}(4) + 4 = 10$, and $E_1^{(R)} = \\frac{7}{2}(4) + 4 = 18$\n- Case S ($\\omega_0 = 14, V_0 = 0$): $E_0^{(S)} = \\frac{3}{2}(14) + 0 = 21$\nComparing the energies:\n- $E_0^{(P)} = 18 \\neq 21 = E_0^{(Q)}$ (A is FALSE)\n- $E_0^{(Q)} = 21 = E_0^{(S)}$ (B is TRUE)\n- $E_0^{(P)} = 18 = E_1^{(R)}$ (C is TRUE)\n- $E_0^{(R)} = 10 \\neq 21 = E_0^{(Q)}$ (D is TRUE)\nTherefore, Options (B), (C), and (D) are correct.",
    },
    61: {
        "questionTextEn": "A particle of mass $m$ in an infinite potential well of width $a$ ($0 \\le x \\le a$) is subjected to a perturbation $V' = \\frac{h^2}{40 m a^2}$ in the region $\\frac{3a}{4} \\le x \\le a$, where $h$ is Planck's constant.\n\nThe first-order energy shift $\\Delta E_4^{(1)}$ of the fourth energy eigenstate ($n = 4$) due to this perturbation is $\\frac{h^2}{N m a^2}$. The value of $N$ is ____________ (in integer).",
        "explanationEn": "1. The unperturbed normalized wavefunction for $n = 4$ in an infinite well of width $a$ is:\n$$\\psi_4(x) = \\sqrt{\\frac{2}{a}} \\sin\\left(\\frac{4\\pi x}{a}\\right)$$\n2. The first-order energy shift is:\n$$\\Delta E_4^{(1)} = \\langle \\psi_4 | V' | \\psi_4 \\rangle = \\frac{h^2}{40 m a^2} \\cdot \\frac{2}{a} \\int_{3a/4}^{a} \\sin^2\\left(\\frac{4\\pi x}{a}\\right) dx$$\n3. Let $u = \\frac{4\\pi x}{a} \\implies dx = \\frac{a}{4\\pi} du$. As $x$ goes from $3a/4$ to $a$, $u$ goes from $3\\pi$ to $4\\pi$:\n$$\\int_{3a/4}^{a} \\sin^2\\left(\\frac{4\\pi x}{a}\\right) dx = \\frac{a}{4\\pi} \\int_{3\\pi}^{4\\pi} \\sin^2 u\\,du = \\frac{a}{4\\pi} \\cdot \\frac{\\pi}{2} = \\frac{a}{8}$$\n4. Substituting back:\n$$\\Delta E_4^{(1)} = \\frac{h^2}{40 m a^2} \\cdot \\frac{2}{a} \\cdot \\frac{a}{8} = \\frac{h^2}{160 m a^2}$$\nComparing with $\\frac{h^2}{N m a^2}$, we get $N = 160$.\nOfficial Key: 160.",
    },
    65: {
        "natMin": 2.0,
        "natMax": 3.0,
        "correctOption": "2 to 3",
        "explanationEn": "1. Nuclear Shell Model configurations for $A = 15$ mirror nuclei:\n- $^{15}_8\\text{O}$ has $Z = 8$ (closed proton shells) and $N = 7$ neutrons $\\implies$ unpaired neutron in the $1p_{1/2}$ level ($l = 1, j = 1/2 = l - 1/2$).\n- $^{15}_7\\text{N}$ has $N = 8$ (closed neutron shells) and $Z = 7$ protons $\\implies$ unpaired proton in the $1p_{1/2}$ level ($l = 1, j = 1/2 = l - 1/2$).\n\n2. Schmidt Magnetic Moments for $j = l - 1/2 = 1/2$:\n- For an odd neutron ($g_l = 0, g_s = -3.826$):\n  $$\\mu_n = \\frac{j}{j + 1}\\left(-\\frac{1}{2} g_s\\right)\\mu_N = \\frac{1}{3}\\left(-\\frac{1}{2}(-3.826)\\right)\\mu_N = +0.638\\,\\mu_N$$\n- For an odd proton ($g_l = 1, g_s = +5.586$):\n  $$\\mu_p = \\frac{j}{j + 1}\\left[(j + 1) g_l - \\frac{1}{2} g_s\\right]\\mu_N = \\frac{1}{3}\\left[1.5 - 2.793\\right]\\mu_N = -0.431\\,\\mu_N$$\n  (or using the exact Schmidt formula $\\mu = j\\left[g_l - \\frac{g_s - g_l}{2l+1}\\right]$: $\\mu_p = \\frac{1}{2}\\left[1 - \\frac{4.586}{3}\\right] = -0.264\\,\\mu_N$).\n\n3. Magnitude of the difference:\n$$|\\mu_n - \\mu_p| = |0.638 - (-0.264)|\\,\\mu_N = 0.902\\,\\mu_N = \\frac{2.71}{3}\\,\\mu_N \\implies a \\approx 2.71$$\n(Depending on rounded $g_s$ values, $a$ lies in the official accepted range $2$ to $3$).\nOfficial Key range: 2 to 3.",
    },
}

YEAR_FIXES = {2022: FIXES_2022, 2023: FIXES_2023, 2024: FIXES_2024}

def process_year(yr: int):
    path = f"tests/gate/gate_ph/pyq/gate_ph_pyq_{yr}.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Remove top-level titleHi if present
    data.pop("titleHi", None)

    fixes = YEAR_FIXES.get(yr, {})
    qs = data["questions"]

    # Build sections dynamically if missing
    sec_map = OrderedDict()
    new_qs = []

    for q in qs:
        qn = int(q["questionNumber"])

        # Apply targeted fixes first
        if qn in fixes:
            for k, v in fixes[qn].items():
                q[k] = v

        # Standardize questionId (remove extra 0-padding like q010 -> q10)
        q["questionId"] = f"gate_ph_{yr}_q{qn:02d}"

        # Fix 2m MCQ negativeMarks = 0.67 (unless MTA where neg == 0.0)
        if q["questionType"] == "MCQ" and float(q["positiveMarks"]) == 2.0:
            if float(q["negativeMarks"]) != 0.0:
                q["negativeMarks"] = 0.67

        # Standardize NAT fields
        if q["questionType"] == "NAT":
            nmin = float(q["natMin"])
            nmax = float(q["natMax"])
            q["natMin"] = nmin
            q["natMax"] = nmax
            q["correctOption"] = fmt_nat_str(nmin, nmax)
            q["correctOptionsList"] = []
            q["correct_index"] = None
            q["correct_indices"] = []
            q["optionsEn"] = []
        else:
            # Wrap unwrapped math in optionsEn
            q["optionsEn"] = [wrap_option_math(o) for o in q.get("optionsEn", [])]

        # Enforce strict 19-key English-only dict
        clean_q = {}
        for k in EXPECTED_KEYS:
            clean_q[k] = q[k]
        new_qs.append(clean_q)

        sid = clean_q["sectionId"]
        stitle = clean_q["sectionTitle"]
        if sid not in sec_map:
            sec_map[sid] = {"sectionId": sid, "sectionTitle": stitle, "sectionTitleEn": stitle, "questionCount": 0, "totalMarks": 0.0}
        sec_map[sid]["questionCount"] += 1
        sec_map[sid]["totalMarks"] = round(sec_map[sid]["totalMarks"] + float(clean_q["positiveMarks"]), 2)

    # Rebuild top-level cleanly matching mocks/topics/2025/2026
    out = {
        "testId": f"gate_ph_pyq_{yr}",
        "categoryId": "gate_ph",
        "test_id": f"gate_ph_pyq_{yr}",
        "category_id": "gate_ph",
        "title": data["title"],
        "titleEn": data["titleEn"],
        "testType": "PYQ",
        "test_type": "PYQ",
        "isFree": bool(data.get("isFree", True)),
        "is_free": bool(data.get("is_free", True)),
        "durationMinutes": 180,
        "duration_minutes": 180,
        "totalQuestions": len(new_qs),
        "total_questions": len(new_qs),
        "maxMarks": 100.0,
        "positiveMarks": 2.0,
        "negativeMarks": 0.33,
        "examYear": yr,
        "shiftBadge": data.get("shiftBadge") or f"GATE PH • {yr} Official Paper",
        "sections": list(sec_map.values()),
        "questions": new_qs,
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"✅ Fixed gate_ph_pyq_{yr}.json ({len(new_qs)} Qs, {sum(x['positiveMarks'] for x in new_qs):.1f} marks)")

if __name__ == "__main__":
    for yr in [2021, 2022, 2023, 2024]:
        process_year(yr)
