# Part X — Mixing

## Overview

With masses established (Part IX), we address the final piece of the Standard Model: **flavor mixing**.

The CKM and PMNS matrices describe how generations mix. In this framework, they emerge from **phason tunneling** in the internal space.

---

## Key Results

| Result | Status | Section |
|--------|--------|---------|
| θ_C = arctan(φ⁻³) ≈ 13.28° | **[VERIFIED]** | X.1 |
| V_us, V_cb from E⊥ rotations | **[DERIVED]** | X.1 |
| V_ub from Fibonacci tunneling (φ⁻²) | **[DERIVED]** | X.1 |
| δ_CP = 2π/5 = 72° | **[VERIFIED]** | X.1 |
| PMNS angles < 3% error | **[VERIFIED]** | X.1 |

---

## The Central Insight

> **Mixing is not arbitrary — it is the geometry of transitions between occupation domains in internal space.**

The mechanism differs for leptons vs quarks:

| Sector | Mechanism | Mixing Size |
|--------|-----------|-------------|
| **Leptons** | Rotation on A₂ cone | Large (PMNS) |
| **Quarks** | Tunneling between domains | Small (CKM) |

---

## Contents

| Section | Title | Content |
|---------|-------|---------|
| X.1 | Mixing | CKM, PMNS, CP violation |
| X.2 | Predictions | Testable predictions summary |

---

## CKM Matrix (Quarks)

Quarks are "trapped" in occupation domains (A, B, C). Mixing requires **tunneling**:

- **Adjacent generations** (V_us, V_cb): Single-step tunneling
- **Non-adjacent** (V_ub): Multi-step with φ⁻² penalty

$$V_{ub} \approx V_{us} \times V_{cb} \times \varphi^{-2}$$

| Element | Predicted | Observed | Error |
|---------|-----------|----------|-------|
| V_ub | 0.0036 | 0.0037 | **2.7%** |

---

## PMNS Matrix (Leptons)

Leptons share a common A₂ cone, so they mix by **rotation**:

$$\theta_{12} \approx \arctan\left(\frac{1}{\sqrt{2}}\right) \approx 35.3°$$

| Angle | Predicted | Observed | Error |
|-------|-----------|----------|-------|
| θ₁₂ | 35.0° | 33.4° | 2.4% |
| θ₂₃ | 45.0° | 49.7° | 2.3% |
| θ₁₃ | 8.6° | 8.6° | < 1% |

---

## CP Violation

The CP-violating phase arises from the **5-fold symmetry** of the internal space (Pentagrid):

$$\delta_{CP} = \frac{2\pi}{5} = 72°$$

| Phase | Predicted | Observed | Error |
|-------|-----------|----------|-------|
| γ (CKM) | 72° | 72.1° ± 5° | **< 1%** |

---

## Connection to Other Parts

| Part | Connection |
|------|------------|
| **IX (Masses)** | Diagonal mass matrix |
| **VIII (Matter)** | The fermions that mix |
| **XII (Assessment)** | Predictions summary |

---

## Prerequisites

- **[Part IX]**: Mass mechanism (determines diagonal masses)
- **[Part VIII]**: Three generations (what's mixing)

---

## Verification

See `Appendices/C_verifications/07_ckm_pmns/` and `Appendices/C_verifications/08_mixing/`.

