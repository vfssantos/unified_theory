# Verification 05: Fermions and Generations

## Overview

This folder contains verification code for the fermion content of the Golden Selection framework:

1. **Fermion spectrum** — The ω₅ spinor orbit of D₆ gives exact SM quantum numbers
2. **Generation mechanism** — Three generations arise from occupation domains (to be verified)

---

## Verified Claims

### THEOREM IV.3.1 (Fermions from Spinors)

| Claim | Status | Verification |
|-------|--------|--------------|
| ω₅ has 32 spinor weights | ✅ **VERIFIED** | `spinor_charges.py` |
| SM charges from ω₅ | ✅ **VERIFIED** | `spinor_charges.py` |
| ×2 is basis conversion | ✅ **VERIFIED** | `spinor_charges.py` |
| One ω₅ = one generation | ✅ **VERIFIED** | `spinor_charges.py` |

### Generation Mechanism (IV.4)

| Claim | Status | Notes |
|-------|--------|-------|
| Three occupation domains exist | ⬜ Pending | From quasicrystal geometry |
| Domains have φ-related volumes | ⬜ Pending | Needs verification |
| Three generations from three domains | ⬜ Pending | Spectral mechanism |

---

## Verification Files

| File | Description | Run |
|------|-------------|-----|
| `spinor_charges.py` | Verifies THEOREM IV.3.1 | `python3 spinor_charges.py` |

---

## Running Verification

```bash
cd Appendices/C_verifications/05_generations/
python3 spinor_charges.py
```

**Expected output**: ALL VERIFICATIONS PASSED ✓

---

## Key Results

### Quantum Number Formulas

From the ω₅ spinor weights $w = (w_1, w_2, w_3, w_4, w_5, w_6)$ with $w_i \in \{\pm\frac{1}{2}\}$:

$$I_3 = \frac{w_4 - w_5}{2}$$

$$Y_{\text{SM}} = 2 \times \left(\frac{w_1 + w_2 + w_3}{3} - \frac{w_4 + w_5}{2}\right)$$

$$Q = I_3 + \frac{Y_{\text{SM}}}{2}$$

### Charge Spectrum

The 32 ω₅ weights produce exactly the SM charges (particles + antiparticles):

| Charge $Q$ | Multiplicity | Particles |
|------------|--------------|-----------|
| −1 | 2 | $e_L, e_R$ |
| −2/3 | 6 | $\bar{u}$ (3 colors × 2 chiralities) |
| −1/3 | 6 | $d$ (3 colors × 2 chiralities) |
| 0 | 4 | $\nu_L, \nu_R$ |
| +1/3 | 6 | $\bar{d}$ (3 colors × 2 chiralities) |
| +2/3 | 6 | $u$ (3 colors × 2 chiralities) |
| +1 | 2 | $\bar{e}_L, \bar{e}_R$ |
| **Total** | **32** | |

### The ×2 Factor

The factor of 2 in the hypercharge formula is **not a free parameter**:
- Without ×2: 15 distinct charges (non-SM)
- With ×2: exactly 7 SM charges

This is a basis conversion from spinor coordinates (±½) to SM convention (integers).

---

## References

- **Part IV.3**: `Part_IV_Standard_Model_v2/03_fermions.md`
- **Delegation 23**: `D_delegations/23_omega2_sm_charges/`
