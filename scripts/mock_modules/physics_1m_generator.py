# -*- coding: utf-8 -*-
"""
Revised GATE PH 1-mark Physics Generator (Q11 to Q35) for GATE 2026/2027 (11 Sections).
Sections:
1. Measurements and Error Analysis (NEW)
2. Mathematical Physics
3. Classical Mechanics
4. Electromagnetic Theory
5. Quantum Mechanics
6. Optical Physics (NEW)
7. Thermodynamics and Statistical Physics
8. Atomic and Molecular Physics
9. Solid State Physics
10. Electronics
11. Nuclear and Particle Physics

Strictly eliminates removed topics:
- No Hamilton-Jacobi, no action-angle, no Liouville's theorem
- No Laplace transforms, no WKB approximation
- No radiation from a moving charge, no tight-binding model, no Kramers-Kronig, no EPR
"""

def get_physics_1m_questions(test_num):
    tid = f"gate_ph_mock_{test_num:02d}"
    tag = f"GATE PH Full Mock {test_num:02d}"
    qs = []

    # Q11: Section 1 - Measurements and Error Analysis (1m MCQ)
    m_data = {
        1: ("In a resistance measurement, the four-probe method is preferred over the conventional two-probe method primarily because:",
            ["It eliminates the effect of lead resistance and contact resistance", "It requires smaller current", "It works only for superconductors", "It measures AC impedance directly"], 0,
            "In the four-probe method, current is passed through two outer probes and voltage is measured across two inner probes using a high-impedance voltmeter, drawing almost zero current and eliminating lead/contact resistance."),
        2: ("The length of a cylinder is measured as $L = (5.00 \\pm 0.05)\\text{ cm}$ and its radius as $R = (2.00 \\pm 0.02)\\text{ cm}$. The percentage error in the calculated volume $V = \\pi R^2 L$ is:",
            ["$3.0\\%$", "$2.0\\%$", "$1.0\\%$", "$5.0\\%$"], 0,
            "Relative error: $\\frac{\\Delta V}{V} = 2 \\frac{\\Delta R}{R} + \\frac{\\Delta L}{L} = 2\\left(\\frac{0.02}{2.00}\\right) + \\frac{0.05}{5.00} = 2(0.01) + 0.01 = 0.03 = 3.0\\%$."),
        3: ("In a lock-in amplifier, the phase-sensitive detector (PSD) multiplies the input signal with a reference signal. The primary purpose of the subsequent low-pass filter is to:",
            ["Extract the DC component proportional to the signal amplitude and eliminate noise at other frequencies", "Amplify high-frequency harmonics", "Shift the phase by $90^\\circ$", "Convert AC signal to digital pulses"], 0,
            "Multiplying with $\\cos(\\omega_r t)$ shifts the signal at frequency $\\omega_r$ to DC ($\\omega = 0$), while uncorrelated noise is shifted to non-zero frequencies which are rejected by the low-pass filter."),
        4: ("A ground loop in an experimental measurement circuit typically causes unwanted interference because:",
            ["Different ground points are at slightly different potentials, causing circulating noise currents through shield conductors", "The circuit has infinite resistance", "Magnetic field lines cancel out completely", "Current cannot return to the source"], 0,
            "Ground loops occur when multiple grounding paths exist, and stray magnetic flux induces circulating currents through the ground loop, creating noise voltages across common impedances."),
        5: ("In a full-wave rectifier circuit with a capacitor filter, if the load resistance is $R_L$ and filter capacitance is $C$, the ripple factor is inversely proportional to:",
            ["$R_L C$", "$R_L / C$", "$\\sqrt{R_L C}$", "Independent of $R_L C$"], 0,
            "For a full-wave rectifier with capacitor filter, the ripple factor is $r = \\frac{1}{4\\sqrt{3} f R_L C} \\propto \\frac{1}{R_L C}$."),
        6: ("The least count of a vernier caliper with main scale division of $1\\text{ mm}$ and 10 vernier divisions matching 9 main scale divisions is:",
            ["$0.1\\text{ mm}$", "$0.01\\text{ mm}$", "$0.05\\text{ mm}$", "$0.2\\text{ mm}$"], 0,
            "$\\text{Least count} = 1\\text{ MSD} - 1\\text{ VSD} = 1\\text{ mm} - 0.9\\text{ mm} = 0.1\\text{ mm}$."),
        7: ("When two independent quantities $x = (10.0 \\pm 0.3)$ and $y = (5.0 \\pm 0.4)$ are subtracted ($z = x - y$), the absolute standard uncertainty in $z$ is:",
            ["$0.5$", "$0.7$", "$0.1$", "$0.35$"], 0,
            "For addition or subtraction of independent quantities, variances add in quadrature: $\\sigma_z = \\sqrt{\\sigma_x^2 + \\sigma_y^2} = \\sqrt{0.3^2 + 0.4^2} = \\sqrt{0.09 + 0.16} = 0.5$."),
        8: ("Which of the following grounding techniques is most effective in preventing ground loops in sensitive low-frequency experimental setups?",
            ["Single-point star grounding", "Multipoint grounding at every chassis", "Floating ground without any earth connection", "Connecting shields at both ends to ground"], 0,
            "Single-point (star) grounding ensures that all ground leads return to a single reference point, eliminating closed ground loops that pick up induced noise currents."),
        9: ("In a screw gauge, zero error is said to be negative when:",
            ["The zero of the circular scale lies above the reference line of the main scale", "The zero of the circular scale lies below the reference line", "The zero coincides with the reference line", "The screw rotates backwards"], 0,
            "Negative zero error occurs when the zero mark of the circular scale has not yet reached the reference datum line when jaws are closed, meaning it lies above the reference line."),
        10: ("A lock-in amplifier operating at reference frequency $f_0 = 1\\text{ kHz}$ with low-pass filter time constant $\\tau = 1\\text{ s}$ has an effective noise bandwidth of approximately:",
            ["$0.25\\text{ Hz}$", "$1\\text{ kHz}$", "$100\\text{ Hz}$", "$10\\text{ kHz}$"], 0,
            "For an RC low-pass filter, the equivalent noise bandwidth is $B_n = \\frac{1}{4\\tau} = \\frac{1}{4(1)} = 0.25\\text{ Hz}$, allowing extreme noise rejection."),
        11: ("The resistance of a thin film superconductor is measured using a 4-probe geometry. If probe spacing is $s$ on a semi-infinite sample, the sheet resistivity $\\rho$ is related to $V/I$ by:",
            ["$\\rho = \\frac{\\pi}{\\ln 2} \\frac{V}{I} \\approx 4.532 \\frac{V}{I}$", "$\\rho = \\frac{V}{I}$", "$\\rho = 2\\pi s \\frac{V}{I}$", "$\\rho = \\frac{1}{2\\pi s} \\frac{V}{I}$"], 0,
            "For a thin layer of thickness $w \\ll s$, the sheet resistance is $R_s = \\frac{\\pi}{\\ln 2} \\frac{V}{I} \\approx 4.532 \\frac{V}{I}$."),
        12: ("In a DC regulated power supply, the voltage regulation percentage is defined as:",
            ["$\\frac{V_{\\text{NL}} - V_{\\text{FL}}}{V_{\\text{FL}}} \\times 100\\%$", "$\\frac{V_{\\text{FL}}}{V_{\\text{NL}}} \\times 100\\%$", "$\\frac{V_{\\text{NL}} + V_{\\text{FL}}}{2} \\times 100\\%$", "$\\frac{V_{\\text{ripple}}}{V_{\\text{DC}}} \\times 100\\%$"], 0,
            "Voltage regulation measures stability under load: $\\%\\text{VR} = \\frac{V_{\\text{NL}} - V_{\\text{FL}}}{V_{\\text{FL}}} \\times 100\\%$.")
    }
    q11_txt, q11_opts, q11_idx, q11_expl = m_data[test_num]
    qs.append({
        "questionId": "{tid}_q011",
        "questionNumber": 11,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Measurements and Error Analysis",
        "difficulty": "Easy",
        "correctOption": chr(65 + q11_idx),
        "correctOptionsList": [chr(65 + q11_idx)],
        "correct_index": q11_idx,
        "correct_indices": [q11_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": q11_txt,
        "optionsEn": q11_opts,
        "explanationEn": q11_expl,
        "questionTextHi": q11_txt,
        "optionsHi": q11_opts,
        "explanationHi": q11_expl
    })

    # Q12 & Q13: Section 2 - Mathematical Physics (Matrices, Residues, Tensors, Differential Eqns)
    # (Notice: NO Laplace transforms!)
    qs.append({
        "questionId": "{tid}_q012",
        "questionNumber": 12,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Mathematical Physics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "Under a coordinate transformation $x'^i = a^i_j x^j$, a rank-2 covariant tensor $T_{ij}$ transforms as:",
        "optionsEn": ["$T'_{ij} = \\frac{\\partial x^k}{\\partial x'^i} \\frac{\\partial x^l}{\\partial x'^j} T_{kl}$", "$T'_{ij} = \\frac{\\partial x'^i}{\\partial x^k} \\frac{\\partial x'^j}{\\partial x^l} T_{kl}$", "$T'_{ij} = \\frac{\\partial x^k}{\\partial x'^i} T_{kj}$", "$T'_{ij} = a^i_j T_{ij}$"],
        "explanationEn": "Covariant tensor indices transform with inverse partial derivatives: $T'_{ij} = \\frac{\\partial x^k}{\\partial x'^i} \\frac{\\partial x^l}{\\partial x'^j} T_{kl}$.",
        "questionTextHi": "निर्देशांक रूपांतरण के अंतर्गत कोटि-2 सहपरिवर्ती (कोवेरिएंट) टेंसर $T_{ij}$ का रूपांतरण नियम क्या है?",
        "optionsHi": ["$T'_{ij} = \\frac{\\partial x^k}{\\partial x'^i} \\frac{\\partial x^l}{\\partial x'^j} T_{kl}$", "$T'_{ij} = \\frac{\\partial x'^i}{\\partial x^k} \\frac{\\partial x'^j}{\\partial x^l} T_{kl}$", "$T'_{ij} = \\frac{\\partial x^k}{\\partial x'^i} T_{kj}$", "$T'_{ij} = a^i_j T_{ij}$"],
        "explanationHi": "सहपरिवर्ती टेंसर सूचकांक आंशिक अवकलजों के व्युत्क्रम से रूपांतरित होते हैं: $T'_{ij} = \\frac{\\partial x^k}{\\partial x'^i} \\frac{\\partial x^l}{\\partial x'^j} T_{kl}$।"
    })

    qs.append({
        "questionId": "{tid}_q013",
        "questionNumber": 13,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Mathematical Physics",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "The residue of the function $f(z) = \\frac{\\cos z}{z^3}$ at the pole $z = 0$ is:",
        "optionsEn": ["$0$", "$-\\frac{1}{2}$", "$\\frac{1}{2}$", "$1$"],
        "explanationEn": "Expanding $\\cos z = 1 - \\frac{z^2}{2!} + \\frac{z^4}{4!} - \\dots$, we have $f(z) = \\frac{1}{z^3} - \\frac{1}{2z} + \\frac{z}{24} - \\dots$. The coefficient of $1/z$ is $-1/2$.",
        "questionTextHi": "ध्रुव $z = 0$ पर फलन $f(z) = \\frac{\\cos z}{z^3}$ का अवशेष क्या है?",
        "optionsHi": ["$0$", "$-\\frac{1}{2}$", "$\\frac{1}{2}$", "$1$"],
        "explanationHi": "लॉरेंट श्रेणी में $1/z$ का गुणांक $-1/2$ है।"
    })

    # Q14 & Q15: Section 3 - Classical Mechanics (No Liouville, No Hamilton-Jacobi, No Action-Angle)
    qs.append({
        "questionId": "{tid}_q014",
        "questionNumber": 14,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Classical Mechanics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "A particle moves in a circular orbit under an attractive central force $F(r) = -k/r^2$. The ratio of its kinetic energy $T$ to its potential energy $V(r) = -k/r$ is:",
        "optionsEn": ["$-1/2$", "$+1/2$", "$-1$", "$+2$"],
        "explanationEn": "By the Virial theorem for $V(r) \\propto r^n$ with $n = -1$: $2\\langle T \\rangle = n \\langle V \\rangle = -\\langle V \\rangle \\implies T = -\\frac{1}{2} V$. Hence $T/V = -1/2$.",
        "questionTextHi": "केंद्रीय बल $F(r) = -k/r^2$ में वृत्ताकार कक्षा में गतिमान कण के लिए गतिज ऊर्जा $T$ और स्थितिज ऊर्जा $V$ का अनुपात क्या है?",
        "optionsHi": ["$-1/2$", "$+1/2$", "$-1$", "$+2$"],
        "explanationHi": "विरियल प्रमेय से $2T = -V \\implies T/V = -1/2$।"
    })

    qs.append({
        "questionId": "{tid}_q015",
        "questionNumber": 15,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Classical Mechanics",
        "difficulty": "Easy",
        "correctOption": "C",
        "correctOptionsList": ["C"],
        "correct_index": 2,
        "correct_indices": [2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "The Poisson bracket between angular momentum component $L_x$ and linear momentum component $p_y$ is:",
        "optionsEn": ["$0$", "$-p_z$", "$p_z$", "$L_z$"],
        "explanationEn": "$\\{L_x, p_y\\} = \\{y p_z - z p_y, p_y\\} = \\{y, p_y\\} p_z = (1) p_z = p_z$.",
        "questionTextHi": "कोणीय संवेग घटक $L_x$ और रेखीय संवेग घटक $p_y$ के बीच प्वासों कोष्ठक का मान क्या है?",
        "optionsHi": ["$0$", "$-p_z$", "$p_z$", "$L_z$"],
        "explanationHi": "$\\{L_x, p_y\\} = p_z$।"
    })

    # Q16 & Q17: Section 4 - Electromagnetic Theory (No radiation from moving charge)
    qs.append({
        "questionId": "{tid}_q016",
        "questionNumber": 16,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Electromagnetic Theory",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "The electromagnetic wave equation in terms of the magnetic vector potential $\\mathbf{A}$ in Lorenz gauge $\\nabla \\cdot \\mathbf{A} + \\frac{1}{c^2} \\frac{\\partial V}{\\partial t} = 0$ in vacuum with current density $\\mathbf{J}$ is:",
        "optionsEn": ["$\\nabla^2 \\mathbf{A} - \\frac{1}{c^2} \\frac{\\partial^2 \\mathbf{A}}{\\partial t^2} = -\\mu_0 \\mathbf{J}$", "$\\nabla^2 \\mathbf{A} = -\\mu_0 \\mathbf{J}$", "$\\nabla \\times \\mathbf{A} = \\mathbf{B}$", "$\\nabla^2 \\mathbf{A} + \\mu_0 \\epsilon_0 \\mathbf{A} = 0$"],
        "explanationEn": "In Lorenz gauge, Maxwell's curl equations decouple into the inhomogeneous wave equation $\\nabla^2 \\mathbf{A} - \\frac{1}{c^2} \\frac{\\partial^2 \\mathbf{A}}{\\partial t^2} = -\\mu_0 \\mathbf{J}$.",
        "questionTextHi": "लॉरेंज गेज में चुंबकीय सदिश विभव $\\mathbf{A}$ के लिए तरंग समीकरण क्या है?",
        "optionsHi": ["$\\nabla^2 \\mathbf{A} - \\frac{1}{c^2} \\frac{\\partial^2 \\mathbf{A}}{\\partial t^2} = -\\mu_0 \\mathbf{J}$", "$\\nabla^2 \\mathbf{A} = -\\mu_0 \\mathbf{J}$", "$\\nabla \\times \\mathbf{A} = \\mathbf{B}$", "$\\nabla^2 \\mathbf{A} + \\mu_0 \\epsilon_0 \\mathbf{A} = 0$"],
        "explanationHi": "लॉरेंज गेज में $\\nabla^2 \\mathbf{A} - \\frac{1}{c^2} \\frac{\\partial^2 \\mathbf{A}}{\\partial t^2} = -\\mu_0 \\mathbf{J}$।"
    })

    qs.append({
        "questionId": "{tid}_q017",
        "questionNumber": 17,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Electromagnetic Theory",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "For an electromagnetic wave propagating inside a hollow rectangular waveguide of width $a$, the phase velocity $v_p$ and group velocity $v_g$ satisfy:",
        "optionsEn": ["$v_p v_g = c$", "$v_p v_g = c^2$", "$v_p = v_g = c$", "$v_p / v_g = c^2$"],
        "explanationEn": "In waveguides with dispersion $\\omega^2 = c^2 k^2 + \\omega_c^2$, $v_p = \\omega/k$ and $v_g = d\\omega/dk$, leading directly to $v_p v_g = c^2$.",
        "questionTextHi": "आयताकार वेवगाइड में कला वेग $v_p$ तथा समूह वेग $v_g$ में क्या संबंध है?",
        "optionsHi": ["$v_p v_g = c$", "$v_p v_g = c^2$", "$v_p = v_g = c$", "$v_p / v_g = c^2$"],
        "explanationHi": "$v_p v_g = c^2$।"
    })

    # Q18 & Q19: Section 5 - Quantum Mechanics (No WKB, No Dirac notation dependence)
    qs.append({
        "questionId": "{tid}_q018",
        "questionNumber": 18,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Quantum Mechanics",
        "difficulty": "Easy",
        "correctOption": "C",
        "correctOptionsList": ["C"],
        "correct_index": 2,
        "correct_indices": [2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "For a quantum particle in a one-dimensional delta-function potential well $V(x) = -\\alpha \\delta(x)$ with $\\alpha > 0$, the bound-state energy is:",
        "optionsEn": ["$-\\frac{m\\alpha}{2\\hbar^2}$", "$-\\frac{m^2\\alpha^2}{\\hbar^2}$", "$-\\frac{m\\alpha^2}{2\\hbar^2}$", "$-\\frac{2m\\alpha^2}{\\hbar^2}$"],
        "explanationEn": "Integrating the Schrödinger equation across $x = 0$ gives discontinuity $\\Delta\\psi' = -\\frac{2m\\alpha}{\\hbar^2} \\psi(0) \\implies \\kappa = \\frac{m\\alpha}{\\hbar^2}$. Then $E = -\\frac{\\hbar^2 \\kappa^2}{2m} = -\\frac{m\\alpha^2}{2\\hbar^2}$.",
        "questionTextHi": "एक-विमीय डेल्टा-फलन विभव $V(x) = -\\alpha \\delta(x)$ ($\\alpha > 0$) में बद्ध अवस्था की ऊर्जा क्या है?",
        "optionsHi": ["$-\\frac{m\\alpha}{2\\hbar^2}$", "$-\\frac{m^2\\alpha^2}{\\hbar^2}$", "$-\\frac{m\\alpha^2}{2\\hbar^2}$", "$-\\frac{2m\\alpha^2}{\\hbar^2}$"],
        "explanationHi": "$E = -\\frac{m\\alpha^2}{2\\hbar^2}$।"
    })

    qs.append({
        "questionId": "{tid}_q019",
        "questionNumber": 19,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Quantum Mechanics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "For a particle confined in a two-dimensional symmetric square box of side $L$ with infinite walls, the energy of state $(n_x, n_y)$ is $E = \\frac{\\pi^2 \\hbar^2}{2m L^2} (n_x^2 + n_y^2)$. The degeneracy of the first excited energy level is:",
        "optionsEn": ["2", "1", "3", "4"],
        "explanationEn": "The ground state is $(1, 1)$ (non-degenerate). The first excited level has $n_x^2 + n_y^2 = 1^2 + 2^2 = 5$, achieved by two states: $(1, 2)$ and $(2, 1)$, giving a degeneracy of 2.",
        "questionTextHi": "द्वि-विमीय सममित वर्गाकार बॉक्स में प्रथम उत्तेजित ऊर्जा स्तर की अपभ्रष्टता (डीजेनेरेसी) क्या है?",
        "optionsHi": ["2", "1", "3", "4"],
        "explanationHi": "अवस्थाएँ $(1, 2)$ तथा $(2, 1)$ समान ऊर्जा $5 \\frac{\\pi^2 \\hbar^2}{2mL^2}$ रखती हैं, अतः अपभ्रष्टता 2 है।"
    })

    # Q20 & Q21: Section 6 - Optical Physics (NEW SECTION)
    opt_data = {
        1: ("The Jones vector for right-handed circularly polarized light propagating along the $+z$ direction is proportional to:",
            ["$\\begin{pmatrix} 1 \\\\ -i \\end{pmatrix}$", "$\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$", "$\\begin{pmatrix} 1 \\\\ i \\end{pmatrix}$", "$\\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}$"], 0,
            "By convention in modern optics, right-handed circular polarization has a $-\\pi/2$ phase shift in the y-component: $\\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ -i \\end{pmatrix}$."),
        2: ("In a Fabry-Pérot interferometer with mirror separation $d$ in a medium of refractive index $n$, the Free Spectral Range (FSR) in frequency is given by:",
            ["$\\Delta \\nu_{\\text{FSR}} = \\frac{c}{2 n d}$", "$\\Delta \\nu_{\\text{FSR}} = \\frac{c}{n d}$", "$\\Delta \\nu_{\\text{FSR}} = \\frac{2 c}{n d}$", "$\\Delta \\nu_{\\text{FSR}} = \\frac{c}{4 n d}$"], 0,
            "The round-trip optical path length is $2nd$. The frequency spacing between adjacent transmission peaks is $\\Delta \\nu_{\\text{FSR}} = \\frac{c}{2nd}$."),
        3: ("In a Michelson interferometer, when one mirror is moved through a distance of $0.15\\text{ mm}$, 500 fringes cross the field of view. The wavelength of the light is:",
            ["$600\\text{ nm}$", "$300\\text{ nm}$", "$500\\text{ nm}$", "$750\\text{ nm}$"], 0,
            "$2 \\Delta d = N \\lambda \\implies \\lambda = \\frac{2 \\Delta d}{N} = \\frac{2(0.15 \\times 10^{-3}\\text{ m})}{500} = \\frac{0.3 \\times 10^{-3}}{500} = 600\\text{ nm}$."),
        4: ("According to the Rayleigh criterion of resolution for a circular aperture of diameter $D$ illuminated with wavelength $\\lambda$, the minimum angular resolution $\\theta_{\\text{min}}$ is:",
            ["$1.22 \\frac{\\lambda}{D}$", "$0.61 \\frac{\\lambda}{D}$", "$\\frac{\\lambda}{D}$", "$2.44 \\frac{\\lambda}{D}$"], 0,
            "The first diffraction minimum of the Airy disk occurs at angular radius $\\theta = 1.22 \\lambda / D$."),
        5: ("A quarter-wave plate introduces a phase difference between the ordinary and extraordinary waves equal to:",
            ["$\\frac{\\pi}{2}$", "$\\pi$", "$2\\pi$", "$\\frac{\\pi}{4}$"], 0,
            "A quarter-wave plate introduces a path difference of $\\lambda/4$, which corresponds to a phase difference of $\\Delta \\phi = \\frac{2\\pi}{\\lambda} \\frac{\\lambda}{4} = \\frac{\\pi}{2}$."),
        6: ("In an optical medium with normal dispersion, the refractive index $n$ increases with frequency $\\omega$. Consequently, the phase velocity $v_p$ and group velocity $v_g$ satisfy:",
            ["$v_g < v_p$", "$v_g > v_p$", "$v_g = v_p$", "$v_g v_p = c^2$"], 0,
            "Using $v_g = \\frac{v_p}{1 + \\frac{\\omega}{n} \\frac{dn}{d\\omega}}$, in normal dispersion $\\frac{dn}{d\\omega} > 0$, so $v_g < v_p$."),
        7: ("In a laser system, if $A_{21}$ and $B_{21}$ are the Einstein coefficients for spontaneous and stimulated emission, the ratio $A_{21} / B_{21}$ is proportional to:",
            ["$\\nu^3$", "$\\nu^2$", "$\\nu$", "$1/\\nu$"], 0,
            "By Planck's radiation law matching, $\\frac{A_{21}}{B_{21}} = \\frac{8\\pi h \\nu^3}{c^3} \\propto \\nu^3$."),
        8: ("In a Fabry-Pérot etalon with mirror reflectivity $R = 0.95$, the coefficient of finesse $F = \\frac{4R}{(1-R)^2}$ is closest to:",
            ["$1520$", "$380$", "$760$", "$95$"], 0,
            "$F = \\frac{4(0.95)}{(0.05)^2} = \\frac{3.8}{0.0025} = 1520$."),
        9: ("When unpolarized light passes through a linear polarizer followed by a quarter-wave plate with its fast axis at $45^\\circ$ to the polarizer axis, the emergent light is:",
            ["Circularly polarized", "Linearly polarized", "Unpolarized", "Elliptically polarized with major axis at $45^\\circ$"], 0,
            "Equal amplitude orthogonal components with $\\pi/2$ phase shift produce pure circular polarization."),
        10: ("In a diffraction grating with grating element $(a + b)$ and $N$ total rulings, the chromatic resolving power $\\lambda / \\Delta \\lambda$ in the $m$-th diffraction order is:",
            ["$m N$", "$N / m$", "$m (a + b)$", "$N / (a + b)$"], 0,
            "The chromatic resolving power of a diffraction grating is given by $R = \\frac{\\lambda}{\\Delta \\lambda} = m N$."),
        11: ("The Jones matrix for an ideal linear horizontal polarizer (passing x-polarization) is:",
            ["$\\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix}$", "$\\begin{pmatrix} 0 & 0 \\\\ 0 & 1 \\end{pmatrix}$", "$\\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}$", "$\\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}$"], 0,
            "Horizontal polarizer passes $E_x$ unchanged and attenuates $E_y$ to zero: $\\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix}$."),
        12: ("In a He-Ne laser, population inversion is established between energy levels of:",
            ["Neon atoms, assisted by resonant energy transfer from excited Helium atoms", "Helium atoms directly", "Both Helium and Neon equally", "The optical cavity mirrors"], 0,
            "Electrical discharge excites Helium to metastable $2^1S_0$ and $2^3S_1$ states, which transfer energy by resonant collisions to Neon $3s$ and $2s$ levels, creating population inversion in Neon.")
    }
    q20_txt, q20_opts, q20_idx, q20_expl = opt_data[test_num]
    qs.append({
        "questionId": "{tid}_q020",
        "questionNumber": 20,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Optical Physics",
        "difficulty": "Easy",
        "correctOption": chr(65 + q20_idx),
        "correctOptionsList": [chr(65 + q20_idx)],
        "correct_index": q20_idx,
        "correct_indices": [q20_idx],
        "natMin": None,
        "natMax": None,
        "questionTextEn": q20_txt,
        "optionsEn": q20_opts,
        "explanationEn": q20_expl,
        "questionTextHi": q20_txt,
        "optionsHi": q20_opts,
        "explanationHi": q20_expl
    })

    qs.append({
        "questionId": "{tid}_q021",
        "questionNumber": 21,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Optical Physics",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "In a double-slit Fraunhofer diffraction pattern, if the slit width is $a$ and slit separation is $d$, the condition for missing orders (absent spectra) is:",
        "optionsEn": ["$\\frac{d}{a} = \\text{fraction}$", "$\\frac{d}{a} = \\text{integer}$", "$d = a$", "$d = 2a$ only"],
        "explanationEn": "Missing orders occur when an interference maximum coincides with a diffraction minimum: $d \\sin \\theta = m \\lambda$ and $a \\sin \\theta = p \\lambda \\implies m = p (d/a)$. For this to occur, $d/a$ must be an integer ratio.",
        "questionTextHi": "द्वि-स्लिट विवर्तन में लुप्त कोटियों (मिसिंग ऑर्डर्स) के लिए शर्त क्या है?",
        "optionsHi": ["$\\frac{d}{a} = \\text{भिन्न}$", "$\\frac{d}{a} = \\text{पूर्णांक}$", "$d = a$", "$d = 2a$ केवल"],
        "explanationHi": "$d/a$ का मान एक पूर्णांक होना चाहिए।"
    })

    # Q22 & Q23: Section 7 - Thermodynamics and Statistical Physics
    qs.append({
        "questionId": "{tid}_q022",
        "questionNumber": 22,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Thermodynamics and Statistical Physics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "For an ideal Fermi gas at temperature $T \\ll T_F$, the electronic specific heat $C_V$ is proportional to:",
        "optionsEn": ["$T$", "$T^3$", "$T^{3/2}$", "$T^2$"],
        "explanationEn": "Only electrons within $k_B T$ of the Fermi level are thermally excited, so $C_V = \\frac{\\pi^2}{2} N k_B \\left(\\frac{T}{T_F}\\right) \\propto T$.",
        "questionTextHi": "$T \\ll T_F$ पर आदर्श फर्मी गैस की इलेक्ट्रॉनिक विशिष्ट ऊष्मा $C_V$ किसके समानुपाती होती है?",
        "optionsHi": ["$T$", "$T^3$", "$T^{3/2}$", "$T^2$"],
        "explanationHi": "$C_V \\propto T$।"
    })

    qs.append({
        "questionId": "{tid}_q023",
        "questionNumber": 23,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Thermodynamics and Statistical Physics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "In a 3D ideal Bose gas below the condensation temperature ($T < T_c$), the chemical potential $\\mu$ is identically:",
        "optionsEn": ["$0$", "$k_B T$", "$E_F$", "$-\\infty$"],
        "explanationEn": "Macroscopic occupation of the single-particle ground state ($E = 0$) in the thermodynamic limit forces $\\mu = 0$ for $T < T_c$.",
        "questionTextHi": "3D आदर्श बोस गैस में $T < T_c$ पर रासायनिक विभव $\\mu$ क्या होता है?",
        "optionsHi": ["$0$", "$k_B T$", "$E_F$", "$-\\infty$"],
        "explanationHi": "संक्रमण ताप से नीचे रासायनिक विभव $\\mu = 0$ होता है।"
    })

    # Q24 & Q25: Section 8 - Atomic and Molecular Physics (Includes Mössbauer & Paschen-Back, No EPR, Lasers moved)
    qs.append({
        "questionId": "{tid}_q024",
        "questionNumber": 24,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Atomic and Molecular Physics",
        "difficulty": "Easy",
        "correctOption": "C",
        "correctOptionsList": ["C"],
        "correct_index": 2,
        "correct_indices": [2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "In Mössbauer spectroscopy, recoil-free emission and absorption of $\\gamma$-rays is made possible because:",
        "optionsEn": ["The nucleus is isolated in free space", "The gamma-ray energy is completely zero", "The recoil momentum is absorbed by the crystal lattice as a whole, making recoil energy negligibly small", "Temperature is maintained at absolute zero"],
        "explanationEn": "When bound in a crystal lattice, the entire macroscopic crystal ($M \\gg m_{\\text{nucleus}}$) absorbs the recoil momentum, making the recoil kinetic energy $E_R = \\frac{p^2}{2M_{\\text{crystal}}} \\approx 0$.",
        "questionTextHi": "मेसबॉअर स्पेक्ट्रोस्कोपी में $\\gamma$-किरणों का प्रतिक्षेप-मुक्त (रिकॉइल-फ्री) उत्सर्जन कैसे संभव होता है?",
        "optionsHi": ["नाभिक मुक्त आकाश में स्थित होता है", "गामा किरण ऊर्जा शून्य होती है", "प्रतिक्षेप संवेग पूरे क्रिस्टल जालक द्वारा अवशोषित होता है जिससे प्रतिक्षेप ऊर्जा नगण्य हो जाती है", "तापमान शून्य होता है"],
        "explanationHi": "प्रतिक्षेप ऊर्जा पूरे क्रिस्टल जालक द्वारा वहन की जाती है, जिससे $E_R \\approx 0$ होता है।"
    })

    qs.append({
        "questionId": "{tid}_q025",
        "questionNumber": 25,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Atomic and Molecular Physics",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "The Paschen-Back effect occurs when the external magnetic field is so strong that:",
        "optionsEn": ["Spin-orbit coupling is stronger than the magnetic interaction", "The magnetic interaction dominates over the spin-orbit coupling, uncoupling $\\mathbf{L}$ and $\\mathbf{S}$", "Hyperfine structure dominates", "Nuclear spin flips completely"],
        "explanationEn": "In the Paschen-Back effect, the strong magnetic field uncouples $\\mathbf{L}$ and $\\mathbf{S}$, so $m_l$ and $m_s$ become good quantum numbers instead of $j$ and $m_j$.",
        "questionTextHi": "पाशन-बैक प्रभाव कब उत्पन्न होता है?",
        "optionsHi": ["चक्रण-कक्षा युग्मन बहुत प्रबल हो", "बाह्य चुंबकीय क्षेत्र इतना प्रबल हो कि $\\mathbf{L}$ और $\\mathbf{S}$ का युग्मन टूट जाता है", "अतिसूक्ष्म संरचना हावी हो", "नाभिकीय चक्रण पलट जाए"],
        "explanationHi": "प्रबल चुंबकीय क्षेत्र में $\\mathbf{L}$ और $\\mathbf{S}$ अलग-अलग $B$ के परितः पुरःसरण करते हैं।"
    })

    # Q26 & Q27: Section 9 - Solid State Physics (Includes semiconductor statistics & metal-semiconductor junctions; No tight-binding, no Kramers-Kronig)
    qs.append({
        "questionId": "{tid}_q026",
        "questionNumber": 26,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Solid State Physics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "In an ideal metal-semiconductor contact (n-type semiconductor with work function $\\Phi_s$ and metal with work function $\\Phi_m$), a rectifying Schottky barrier is formed when:",
        "optionsEn": ["$\\Phi_m > \\Phi_s$", "$\\Phi_m < \\Phi_s$", "$\\Phi_m = \\Phi_s$", "Independent of work functions"],
        "explanationEn": "For an n-type semiconductor, a rectifying Schottky barrier requires $\\Phi_m > \\Phi_s$ so that electrons flow from semiconductor to metal until equilibrium band bending creates a barrier $\\Phi_B = \\Phi_m - \\chi$.",
        "questionTextHi": "धातु-अर्धचालक संपर्क (n-प्रकार) में दिष्टकारी शोट्की रोधिका कब बनती है?",
        "optionsHi": ["$\\Phi_m > \\Phi_s$", "$\\Phi_m < \\Phi_s$", "$\\Phi_m = \\Phi_s$", "कार्यफलनों से स्वतंत्र"],
        "explanationHi": "n-प्रकार अर्धचालक के लिए शोट्की रोधिका हेतु $\\Phi_m > \\Phi_s$ आवश्यक है।"
    })

    qs.append({
        "questionId": "{tid}_q027",
        "questionNumber": 27,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Solid State Physics",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "In an intrinsic semiconductor, the Fermi level $E_F$ is located at:",
        "optionsEn": ["The top of the valence band", "Approximately in the middle of the bandgap: $E_F = \\frac{E_c + E_v}{2} + \\frac{3}{4} k_B T \\ln(m_h^* / m_e^*)$", "The bottom of the conduction band", "Directly at the donor energy level"],
        "explanationEn": "From carrier statistics $n = p$, $E_F = \\frac{E_c + E_v}{2} + \\frac{3}{4} k_B T \\ln(m_h^* / m_e^*)$, which lies very close to the center of the bandgap.",
        "questionTextHi": "नैज अर्धचालक में फर्मी स्तर $E_F$ कहाँ स्थित होता है?",
        "optionsHi": ["संयोजी बैंड के शीर्ष पर", "लगभग बैंड अंतराल के मध्य में", "चालन बैंड के तल पर", "दाता ऊर्जा स्तर पर"],
        "explanationHi": "नैज अर्धचालक में $E_F$ बैंड अंतराल के ठीक मध्य के समीप होता है।"
    })

    # Q28 & Q29: Section 10 - Electronics (Includes Op-amp waveform generators)
    qs.append({
        "questionId": "{tid}_q028",
        "questionNumber": 28,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Electronics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "An astable multivibrator constructed using an operational amplifier with positive feedback operates as:",
        "optionsEn": ["A free-running relaxation oscillator producing a square waveform", "A linear audio amplifier", "A digital counter", "A high-pass filter"],
        "explanationEn": "An op-amp astable multivibrator switches between positive and negative saturation voltages as a timing capacitor charges and discharges through a resistor, producing a continuous square wave.",
        "questionTextHi": "ऑप-एम्प द्वारा निर्मित अस्टेबल मल्टीवाइब्रेटर किस रूप में कार्य करता है?",
        "optionsHi": ["वर्गाकार तरंग उत्पन्न करने वाले मुक्त दोलक के रूप में", "रैखिक प्रवर्धक", "डिजिटल काउंटर", "हाई-पास फिल्टर"],
        "explanationHi": "यह निरंतर वर्गाकार तरंग उत्पन्न करने वाला रिलैक्सेशन दोलक है।"
    })

    qs.append({
        "questionId": "{tid}_q029",
        "questionNumber": 29,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Electronics",
        "difficulty": "Easy",
        "correctOption": "C",
        "correctOptionsList": ["C"],
        "correct_index": 2,
        "correct_indices": [2],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "A Schmitt trigger circuit uses which type of feedback to create hysteresis?",
        "optionsEn": ["Negative feedback only", "No feedback", "Positive feedback", "Both negative and capacitive feedback"],
        "explanationEn": "Positive feedback applied to the non-inverting terminal creates two distinct threshold voltages ($V_{UT}$ and $V_{LT}$), producing hysteresis.",
        "questionTextHi": "श्मिट ट्रिगर परिपथ में हिस्टैरिसीस उत्पन्न करने के लिए किस प्रकार का पुनर्निवेश उपयोग किया जाता है?",
        "optionsHi": ["केवल ऋणात्मक पुनर्निवेश", "कोई पुनर्निवेश नहीं", "धनात्मक पुनर्निवेश", "दोनों"],
        "explanationHi": "अ-प्रतिलोमी टर्मिनल पर धनात्मक पुनर्निवेश से हिस्टैरिसीस उत्पन्न होता है।"
    })

    # Q30 & Q31: Section 11 - Nuclear and Particle Physics
    qs.append({
        "questionId": "{tid}_q030",
        "questionNumber": 30,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Nuclear and Particle Physics",
        "difficulty": "Easy",
        "correctOption": "B",
        "correctOptionsList": ["B"],
        "correct_index": 1,
        "correct_indices": [1],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "In the Weizsäcker semi-empirical mass formula, the asymmetry energy term proportional to $(A - 2Z)^2 / A$ arises due to:",
        "optionsEn": ["Electrostatic Coulomb repulsion", "The Pauli exclusion principle acting differently when proton and neutron numbers differ", "Nuclear surface tension", "Pairing interaction between like nucleons"],
        "explanationEn": "Protons and neutrons occupy separate Fermi levels. Any difference $(N - Z) = A - 2Z$ forces nucleons to occupy higher kinetic energy states, reducing binding energy.",
        "questionTextHi": "अर्ध-आनुभविक द्रव्यमान सूत्र में असममिति ऊर्जा पद $(A - 2Z)^2/A$ का मूल कारण क्या है?",
        "optionsHi": ["कूलॉम प्रतिकर्षण", "पाउली अपवर्जन सिद्धांत", "पृष्ठ तनाव", "युग्मन बल"],
        "explanationHi": "प्रोटॉन और न्यूट्रॉन के अलग-अलग फर्मी स्तरों में भरने पर पाउली सिद्धांत के कारण ऊर्जा में वृद्धि होती है।"
    })

    qs.append({
        "questionId": "{tid}_q031",
        "questionNumber": 31,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "MCQ",
        "positiveMarks": 1.0,
        "negativeMarks": 0.33,
        "pyqTag": tag,
        "topicTag": "Nuclear and Particle Physics",
        "difficulty": "Easy",
        "correctOption": "A",
        "correctOptionsList": ["A"],
        "correct_index": 0,
        "correct_indices": [0],
        "natMin": None,
        "natMax": None,
        "questionTextEn": "The quark structure of the neutral pion $\\pi^0$ is represented by the superposition:",
        "optionsEn": ["$\\frac{1}{\\sqrt{2}} (u \\bar{u} - d \\bar{d})$", "$u \\bar{d}$", "$d \\bar{u}$", "$s \\bar{s}$"],
        "explanationEn": "The neutral pion is the $I = 1, I_3 = 0$ member of the pseudoscalar meson octet, described by $\\frac{1}{\\sqrt{2}} (u \\bar{u} - d \\bar{d})$.",
        "questionTextHi": "उदासीन पायन $\\pi^0$ की क्वार्क संरचना क्या है?",
        "optionsHi": ["$\\frac{1}{\\sqrt{2}} (u \\bar{u} - d \\bar{d})$", "$u \\bar{d}$", "$d \\bar{u}$", "$s \\bar{s}$"],
        "explanationHi": "$\\pi^0 = \\frac{1}{\\sqrt{2}} (u \\bar{u} - d \\bar{d})$।"
    })

    # Q32 to Q35: 4 NAT questions (1-mark each) covering Section 1, 2, 6, 10
    qs.append({
        "questionId": "{tid}_q032",
        "questionNumber": 32,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": tag,
        "topicTag": "Measurements and Error Analysis",
        "difficulty": "Easy",
        "correctOption": "4",
        "correctOptionsList": ["4"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 4.0,
        "natMax": 4.0,
        "questionTextEn": "A quantity $Z = X^2 Y^{1/2}$ is calculated from measured values. If the relative standard uncertainty in $X$ is $1.5\\%$ and in $Y$ is $4.0\\%$, the percentage standard uncertainty in $Z$ is ______\\% (answer in integer).",
        "optionsEn": [],
        "explanationEn": "Relative uncertainty: $(\\Delta Z / Z)^2 = (2 \\Delta X / X)^2 + (0.5 \\Delta Y / Y)^2 = (2 \\times 1.5)^2 + (0.5 \\times 4.0)^2 = 3.0^2 + 2.0^2 = 9 + 4 = 13 \\implies \\Delta Z/Z = \\sqrt{13} \\approx 3.61\\%$. Wait, if $\\Delta X / X = 1.5\\%$ and $\\Delta Y / Y = 4\\%$, let's set $\\Delta X / X = 1.5\\%, \\Delta Y / Y = 4\\%$ -> $3^2 + 2^2 = 13$. For integer: if $\\Delta X/X = 1.5\\%$ and $\\Delta Y/Y = 4.0\\%$, $\\sqrt{13} \\approx 3.6$. If $\\Delta X / X = 1.5\\%$ and $\\Delta Y/Y = 4.0\\%$, let's set $\\Delta X/X = 1.5\\%$ with $(2 \\times 1.5) = 3$ and $0.5 \\times 4 = 2$. What if $\\Delta X/X = 1.5\\%$ and $\\Delta Y/Y = 4\\%$? What if $(\\Delta Z/Z) = \\sqrt{3^2 + 4^2} = 5\\%$ with $\\Delta Y/Y = 8\\%$? Let $\\Delta X/X = 2\\%$ and $\\Delta Y/Y = 6\\%$: $(2 \\times 2)^2 + (0.5 \\times 6)^2 = 4^2 + 3^2 = 25 \\implies 5\\%$! Let's use $5\\%$.",
        "questionTextHi": "राशि $Z = X^2 Y^{1/2}$ में यदि $X$ में त्रुटि $2.0\\%$ तथा $Y$ में $6.0\\%$ है, तो $Z$ में प्रतिशत अनिश्चितता ______\\% है।",
        "optionsHi": [],
        "explanationHi": "$\\Delta Z/Z = \\sqrt{(2 \\times 2.0)^2 + (0.5 \\times 6.0)^2} = \\sqrt{16 + 9} = \\sqrt{25} = 5\\%$।"
    })
    # Update Q32 text and answer to clean 5%
    qs[-1]["questionTextEn"] = "A quantity $Z = X^2 Y^{1/2}$ is calculated from independent measurements. If the percentage uncertainty in $X$ is $2.0\\%$ and in $Y$ is $6.0\\%$, the percentage standard uncertainty in $Z$ is ______\\% (answer in integer)."
    qs[-1]["correctOption"] = "5"
    qs[-1]["correctOptionsList"] = ["5"]
    qs[-1]["natMin"] = 5.0
    qs[-1]["natMax"] = 5.0

    qs.append({
        "questionId": "{tid}_q033",
        "questionNumber": 33,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": tag,
        "topicTag": "Optical Physics",
        "difficulty": "Easy",
        "correctOption": "4",
        "correctOptionsList": ["4"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 4.0,
        "natMax": 4.0,
        "questionTextEn": "In a double-slit interference experiment, the distance between the two slits is $d = 0.8\\text{ mm}$ and the width of each slit is $a = 0.2\\text{ mm}$. The ratio $d/a$ which determines the missing order of interference is ______ (answer in integer).",
        "optionsEn": [],
        "explanationEn": "$d/a = 0.8 / 0.2 = 4$. Thus, the 4th, 8th, 12th ... interference maxima are missing.",
        "questionTextHi": "द्वि-स्लिट प्रयोग में $d = 0.8\\text{ mm}$ तथा $a = 0.2\\text{ mm}$ के लिए अनुपात $d/a$ ______ है।",
        "optionsHi": [],
        "explanationHi": "$d/a = 0.8 / 0.2 = 4$।"
    })

    qs.append({
        "questionId": "{tid}_q034",
        "questionNumber": 34,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": tag,
        "topicTag": "Quantum Mechanics",
        "difficulty": "Easy",
        "correctOption": "9",
        "correctOptionsList": ["9"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 9.0,
        "natMax": 9.0,
        "questionTextEn": "For an electron in a hydrogen atom in the state with principal quantum number $n = 3$, the total orbital spatial degeneracy (summing over all allowed orbital states $\\sum_{l=0}^{n-1} (2l+1)$, excluding spin) is ______ (answer in integer).",
        "optionsEn": [],
        "explanationEn": "Degeneracy without spin is $n^2 = 3^2 = 9$.",
        "questionTextHi": "हाइड्रोजन परमाणु में $n = 3$ स्तर के लिए कुल कक्षीय अपभ्रष्टता (चक्रण रहित) ______ है।",
        "optionsHi": [],
        "explanationHi": "$n^2 = 3^2 = 9$।"
    })

    qs.append({
        "questionId": "{tid}_q035",
        "questionNumber": 35,
        "sectionId": "sec_ph",
        "sectionTitle": "Physics",
        "questionType": "NAT",
        "positiveMarks": 1.0,
        "negativeMarks": 0.0,
        "pyqTag": tag,
        "topicTag": "Electronics",
        "difficulty": "Easy",
        "correctOption": "10",
        "correctOptionsList": ["10"],
        "correct_index": None,
        "correct_indices": [],
        "natMin": 10.0,
        "natMax": 10.0,
        "questionTextEn": "In a full-wave bridge rectifier operating from a $50\\text{ Hz}$ AC power line, the fundamental ripple frequency in the rectified DC output in Hz is ______ (answer in integer).",
        "optionsEn": [],
        "explanationEn": "For full-wave rectification, the ripple frequency is twice the input AC line frequency: $f_{\\text{ripple}} = 2 f_{\\text{line}} = 2 \\times 50\\text{ Hz} = 100\\text{ Hz}$. Wait, let's make the answer 100 Hz or adjust text: ripple frequency is 100 Hz.",
        "questionTextHi": "$50\\text{ Hz}$ प्रत्यावर्ती लाइन से संचालित पूर्ण-तरंग दिष्टकारी के निर्गत में रिपल आवृत्ति ______ Hz होती है।",
        "optionsHi": [],
        "explanationHi": "$f_{\\text{ripple}} = 2 \\times 50 = 100\\text{ Hz}$।"
    })
    qs[-1]["correctOption"] = "100"
    qs[-1]["correctOptionsList"] = ["100"]
    qs[-1]["natMin"] = 100.0
    qs[-1]["natMax"] = 100.0

    return qs
