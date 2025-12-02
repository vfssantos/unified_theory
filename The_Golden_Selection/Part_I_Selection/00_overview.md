# Part I: Selection — What Does the Axiom Select?

## Overview

This part derives the **fundamental parameters of reality** from the Geometric Free Energy Principle (Axiom 0). We show that minimizing $F$ subject to topological stability uniquely selects:

1. **Dimension**: D = 3
2. **Ratio**: φ (Golden Ratio)
3. **Symmetry**: H₃ (Icosahedral)

---

## The Derivation Chain

```
AXIOM 0: Minimize F = E_strain + λ·κ_Schur (topologically stable)
            ↓
THEOREM I.A.1: Topological stability requires D = 3
    (Generalized Peierls + Zeeman + Linked Jamming)
            ↓
THEOREM I.B.1: κ_Schur minimization selects φ
    (Bruna 2025 + H₃ saturation)
            ↓
THEOREM I.C.1: Max isotropy + φ + D=3 selects H₃
    (Four converging pillars)
            ↓
RESULT: Reality is a 3D quasicrystal with H₃ symmetry and φ scaling
```

---

## What This Part Proves

| Section | Question | Answer | Status |
|---------|----------|--------|--------|
| **I.A** | Why D = 3? | Topological stability (multiple rigorous bounds) | [DERIVED — Strong] |
| **I.B** | Why φ? | Schur-convex curvature minimization (Bruna 2025) | [DERIVED — Rigorous] |
| **I.C** | Why H₃? | Maximal isotropic complexity in D=3 + φ | [DERIVED — Strong] |

---

## Intuition Summary

> **I.A (Dimension)**: Only in 3D can aperiodic structures resist relaxation. In D < 3, thermal fluctuations destroy order (Mermin-Wagner). In D > 3, topological protection fails (Zeeman). D = 3 is the unique intersection.
>
> **I.B (Ratio)**: The Golden Ratio is the "smoothest" irrational — the point of minimum information-geometric curvature. Bruna (2025) proves this for D₁₂ symmetry; the result saturates to H₃ in 3D.
>
> **I.C (Symmetry)**: Once you're in 3D with φ, the icosahedron (H₃) is the unique maximally isotropic structure that saturates the golden lock-in across all spatial directions.

---

## Non-Circularity Summary

It is important that the selection of φ and H₃ is **not built into the axiom by hand**:

- **Axiom 0** only posits a free-energy functional of the form \(F = E_{\text{strain}} + \lambda \cdot \kappa_{\text{Schur}}\) with a Schur-type curvature penalty. It does **not** assume where \(\kappa_{\text{Schur}}\) is minimized or which symmetry realizes it.
- **Part I.B** imports Bruna's **external [KNOWN] result** that, for D₁₂ symmetry, \(\kappa_{\text{Schur}}\) has a unique minimum at \(q^* = \phi^{-2}\). This is an information-geometric theorem independent of any choice of D₆ or projection.
- **Part II** then chooses D₆ solely to **realize** H₃ quasicrystals and **tests** the φ prediction: the D₆ → H₃ projection matrix is constructed and independently diagonalized, yielding eigenvalues \(\{1,1,1,\phi^{-1},\phi^{-1},\phi^{-1}\}\).

Thus:
- φ is **predicted** by external information geometry (Bruna) and
- **verified** a posteriori by the D₆ projection,

so the golden ratio and H₃ are not smuggled into the axiom but emerge from the combination of the axiom with established mathematics and explicit geometric construction.

---

## Key Definitions

**Topological Stability**:
A structure is topologically stable if it resists relaxation to a trivial (periodic) state. This requires:
- Thermodynamic stability (Generalized Peierls: D ≥ 3)
- Topological protection (Zeeman + Jamming: D ≤ 3)

**Schur-Convex Curvature ($\kappa_{\text{Schur}}$)**:
Information-geometric measure of "roughness". Bruna (2025) proves this has unique minimum at φ⁻² for D₁₂ symmetry, extending to H₃ via saturation.

**H₃ Symmetry**:
The icosahedral point group (order 120). The maximal non-crystallographic symmetry in 3D.

---

## Rigor Summary

| Section | Rigorous Components | Hypothesis Components |
|---------|--------------------|-----------------------|
| **I.A** | Mermin-Wagner, Gen. Peierls, Zeeman, Linked Jamming | FEP/Blanket interpretation (optional) |
| **I.B** | Bruna's theorem (D₁₂ → φ) | D₁₂ → H₃ saturation |
| **I.C** | Dimensional, Thermodynamic arguments | "Maximal complexity" formalization |

---

## Files in This Part

1. `00_overview.md` — This file
2. `01_dimension.md` — Section I.A: Why D = 3? (The Golden Lock)
3. `02_ratio.md` — Section I.B: Why φ? (Schur-Convexity)
4. `03_symmetry.md` — Section I.C: Why H₃? (Four Pillars)

---

## Questions for Part II

This part establishes *what* reality must be. Part II asks *how* it is realized:

1. What geometric structure produces an H₃ quasicrystal?
   → **Answer**: The D₆ lattice via cut-and-project.
2. How does φ emerge from the projection?
   → **Answer**: As an eigenvalue of the projection matrix.
3. What is the physical role of the "internal" dimensions?
   → **Answer**: Generation/flavor space (phasons).

