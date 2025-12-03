# Part VII — Gauge Sector

## Overview

With the foundational physics established (spacetime, quantum, gravity), we now turn to the **Standard Model**. This part addresses the gauge structure: the forces of nature.

The key result: the Standard Model gauge group **SU(3) × SU(2) × U(1)** emerges from the subalgebra structure of D₆.

---

## Key Results

| Result | Status | Section |
|--------|--------|---------|
| SM gauge group from D₆ subalgebras | **[DERIVED]** | VII.1 |
| sin²θ_W = (393-75√5)/968 ≈ 0.2327 | **[VERIFIED]** | VII.2 |
| Scale paradox resolved (CSDR) | **[RESOLVED]** | VII.2 |
| m_H = m_Z × φ^(2/3) = 125.68 GeV | **[VERIFIED]** | VII.3 |

---

## The Central Insight

> **The Standard Model gauge group is not assumed — it is the maximal commuting subalgebra structure of D₆.**

The D₆ root system contains:
- **A₂** ⊂ D₆ → SU(3) color
- **D₄** ⊂ D₆ → SO(8) → contains SU(2)_L
- **A₃** ⊂ D₆ → SU(4) → contains U(1)_Y

The projection to H₃ breaks these symmetries in a specific pattern, yielding the observed gauge structure.

---

## Contents

| Section | Title | Content |
|---------|-------|---------|
| VII.1 | Gauge Structure | SM group from D₆ subalgebras |
| VII.2 | Electroweak | Weinberg angle, CSDR |
| VII.3 | Higgs | Mass prediction, symmetry breaking |

---

## The Weinberg Angle

The most precise prediction of the theory:

$$\sin^2\theta_W = \frac{393 - 75\sqrt{5}}{968} \approx 0.2327$$

| Quantity | Predicted | Observed | Error |
|----------|-----------|----------|-------|
| sin²θ_W | 0.2327 | 0.2312 | **0.67%** |

This is derived from **pure geometry** — no free parameters.

---

## The Scale Paradox

**Problem**: Why does the geometric prediction match the Z-pole value (0.2312) rather than the GUT value (0.375)?

**Resolution**: Coset Space Dimensional Reduction (CSDR). The D₆ → H₃ projection **IS** electroweak symmetry breaking. The geometry defines the IR vacuum, not UV physics.

Evidence: The same Q = 2/3 appears in:
- Weinberg angle (via A₂ structure)
- Koide formula (via A₂ cone)
- Higgs mass (via A₂ triplet of Goldstones)

---

## Connection to Other Parts

| Part | Connection |
|------|------------|
| **VI (Gravity)** | Gauge fields interact with metric |
| **VIII (Matter)** | Fermions couple to gauge fields |
| **IX (Masses)** | Higgs mechanism gives mass |

---

## Prerequisites

- **[Part VI]**: Gravity (spacetime is curved)
- **[Part III]**: D₆ root structure

---

## Verification

See `Appendices/C_verifications/01_weinberg_angle/` and `Appendices/C_verifications/10_scale_paradox/`.

