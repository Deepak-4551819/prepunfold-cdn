import os, shutil, math

print("tesseract in PATH:", shutil.which("tesseract"))
for p in [r"C:\Program Files\Tesseract-OCR\tesseract.exe", r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"]:
    if os.path.exists(p):
        print("Found tesseract:", p)

# Verify 2025 Q60 (transistor circuit): V_BE = 0.7V, beta_DC = 400, I_B = 18 to 19 uA
# Standard voltage-divider or fixed-bias or collector-feedback? Let's check common R values
print("\n2025 Q60: beta=400, V_BE=0.7V, I_B ~ 18.5 uA => I_C = 400*18.5uA = 7.4 mA")

# Verify 2025 Q65 (opamp with 5.1V Zener in feedback loop, +-15V, Vin = +1V, Vout = 7.0 to 7.2V)
# Notice 5.1 + 0.7 = 5.8V? Wait: Vout = 7.1V!
# If non-inverting with Vz=5.1V + drop, or inverting/non-inverting summing?
# Wait: 5.1 + 2*1 = 7.1! Or 1 + 5.1 + ... = 7.1!
print("2025 Q65: Vout = 7.0 to 7.2 V (note 5.1V + 2.0V = 7.1V, or Vz + Vin*(1+Rf/R1)?)")

# Verify 2026 Q60 (photodiode + TIA + 10-bit ADC, Vref = 5V, smallest I_d = 47.5 to 50.0 nA)
# 1 LSB = 5 V / 1024 = 4.8828 mV (or 5/1023 = 4.8876 mV)
# If R_f = 100 kOhm: I_min = 4.8828 mV / 100 kOhm = 48.83 nA!!
print("2026 Q60: 5V / 1024 / 100kOhm =", (5.0 / 1024 / 100e3) * 1e9, "nA (in 47.5 to 50.0!)")

# Verify 2026 Q31 (metal-superconductor I-V curve, energy gap = 2.0 meV)
# Note: in NIS (normal metal-insulator-superconductor) tunneling, current starts flowing sharply at eV = \Delta (energy gap \Delta = 2.0 meV -> V = 2.0 mV, or if 2\Delta -> V = 4.0 mV)
print("2026 Q31: D = 2.0 meV")
