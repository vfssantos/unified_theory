# B. Calculations

Numerical and symbolic calculations supporting the theory. Each subfolder contains code and results for a specific calculation domain.

---

## Folder Structure

```
B_calculations/
├── 01_e8_roots/          # E₈ lattice fundamentals
├── 02_projections/       # Golden projection matrices
├── 03_gauge_couplings/   # Weinberg angle, coupling ratios
├── 04_mass_formulas/     # Koide, Higgs mass, etc.
└── 05_mixing_angles/     # CKM, PMNS matrix elements
```

---

## 01_e8_roots/

**Purpose**: Generate and verify E₈ root system properties

**Key Calculations**:
- [ ] Generate all 240 E₈ roots (112 D₈-type + 128 S₈-type)
- [ ] Verify root lengths (all √2)
- [ ] Compute inner products and angle spectrum
- [ ] Identify simple roots and Cartan matrix
- [ ] Map roots to Standard Model representations

**Files**:
- `e8_roots.py` — Root generation script
- `e8_roots_table.csv` — Complete list of 240 roots
- `e8_cartan.md` — Cartan matrix and Dynkin diagram

---

## 02_projections/

**Purpose**: Implement and verify the D₆ → H₃ golden projection (Koca–Al-Siyabi)

**Key Calculations**:
- [x] Construct the 3×6 projection matrix P_{D₆→H₃}
- [x] Project all 60 D₆ roots to 3D
- [x] Verify two icosidodecahedra emerge (30 + 30 vertices)
- [x] Compute radii ratio (verified: φ)
- [x] Compute Weinberg angle from SM generator projections
- [x] Verify 120° angle between SU(2) and SU(3) (A₂ geometry)

**Files**:
- `d6_to_h3_projection.py` — Complete implementation with verification
- `README.md` — Documentation and key results

**Key Result**: D₆ gives **identical** Weinberg angle formula to E₈:
$$\sin^2\theta_W = \frac{393 - 75\sqrt{5}}{968} \approx 0.2327$$

---

## 03_gauge_couplings/

**Purpose**: Calculate gauge coupling ratios from projection geometry

**Key Calculations**:
- [ ] Identify SU(3), SU(2), U(1) generators in E₈
- [ ] Project each generator type
- [ ] Compute |x|² for each gauge sector
- [ ] Calculate g₂²/g₁² ratio
- [ ] Derive sin²θ_W from projection

**Files**:
- `gauge_generators.py` — SM embedding in E₈
- `projection_ratios.py` — Coupling ratio calculation
- `weinberg_derivation.md` — Step-by-step derivation

---

## 04_mass_formulas/

**Purpose**: Verify mass predictions

**Key Calculations**:
- [ ] Koide ratio for leptons (verify Q = 2/3)
- [ ] Koide phase θ₀ (compare to arctan(φ⁻³))
- [ ] Quark Koide ratios
- [ ] Higgs mass m_H = m_Z × (15/11)
- [ ] Mirror mass scale predictions

**Files**:
- `koide_check.py` — Koide formula verification
- `higgs_mass.py` — Higgs mass prediction
- `mass_tables.md` — Comparison tables

---

## 05_mixing_angles/

**Purpose**: Calculate CKM and PMNS matrix predictions

**Key Calculations**:
- [ ] Cabibbo angle θ_C = arctan(φ⁻³)
- [ ] Full CKM matrix elements
- [ ] CP phase δ = arctan(φ²)
- [ ] PMNS angles from golden geometry
- [ ] Neutrino mass sum prediction

**Files**:
- `ckm_calculation.py` — CKM predictions
- `pmns_calculation.py` — PMNS predictions
- `mixing_comparison.md` — Theory vs. PDG values

---

## Calculation Standards

Each calculation file should include:

```python
"""
[Title]

Purpose: [What this calculates]
Supports: [Which theorem/claim]
Status: [Complete/Partial/Draft]

Dependencies:
- numpy
- [other packages]

References:
- [Relevant papers]
"""

import numpy as np

# Constants
PHI = (1 + np.sqrt(5)) / 2
PHI_INV = PHI - 1

# [Calculation code]

# Verification
def verify():
    """Run all verification checks."""
    pass

if __name__ == "__main__":
    verify()
```

---

## Status Summary

| Folder | Status | Priority |
|--------|--------|----------|
| 01_e8_roots | ⬜ Not Started | HIGH |
| 02_projections | ⬜ Not Started | HIGH |
| 03_gauge_couplings | ⬜ Not Started | HIGH |
| 04_mass_formulas | ⬜ Not Started | MEDIUM |
| 05_mixing_angles | ⬜ Not Started | MEDIUM |

