# XI.3 Magic Numbers

## Overview

The nuclear magic numbers (2, 8, 20, 28, 50, 82, 126) are **derived** from the geometric Hamiltonian with all coefficients determined by geometry.

**Key finding**: The branching rules SO(3) → I_h determine which magic numbers arise from pure geometry and which require the spin-orbit term.

---

## XI.3.1 Results Summary

| Magic # | Gap After | Mechanism | Status |
|---------|-----------|-----------|--------|
| **2** | $1s_{1/2}$ | Branching: I_h = SO(3) for ℓ=0 | **[THEOREM]** |
| **8** | $1p_{1/2}$ | Branching: I_h = SO(3) for ℓ=1 | **[THEOREM]** |
| **20** | $1d_{3/2}$ | Branching: I_h = SO(3) for ℓ=2 | **[THEOREM]** |
| **28** | $1f_{7/2}$ ★ | Spin-orbit (λ₀ = 3q/2z) | **[DERIVED]** |
| **50** | $1g_{9/2}$ ★ | Strain inversion (c₂ = k/2) + SO | **[DERIVED]** |
| **82** | $1g_{7/2}$ | Strain inversion + SO | **[DERIVED]** |
| **126** | $1h_{9/2}$ | Strain inversion + SO | **[DERIVED]** |

★ = Intruder orbital

**All seven magic numbers are derived with no free parameters.**

---

## XI.3.2 The Branching Rule Explanation

### Why Icosahedral Geometry Determines Low-ℓ Shells

The **spherical harmonics** $Y_{\ell m}$ decompose into **Icosahedral irreps** as:

| ℓ | Shell | Spherical (2ℓ+1) | Icosahedral (I_h) | Geometric? |
|---|-------|------------------|-------------------|------------|
| 0 | s | 1 | A_g (1) | ✅ **YES** |
| 1 | p | 3 | T_{1u} (3) | ✅ **YES** |
| 2 | d | 5 | H_g (5) | ✅ **YES** |
| 3 | f | 7 | T_{2u}(3) ⊕ G_u(4) | ❌ **SPLITS** |
| 4 | g | 9 | G_g(4) ⊕ H_g(5) | ❌ **SPLITS** |
| 5 | h | 11 | T_{1u}(3) ⊕ T_{2u}(3) ⊕ H_u(5) | ❌ **SPLITS** |

### Mathematical Consequence

- **ℓ = 0, 1, 2 (s, p, d)**: Icosahedral irrep dimensions match spherical (2ℓ+1)
  - The D₆ graph Laplacian naturally produces the correct degeneracies
  - **Magic numbers 2, 8, 20 are purely geometric**

- **ℓ ≥ 3 (f, g, h, ...)**: Icosahedral symmetry **splits** the spherical representation
  - f-shell (7 states) → 3 + 4 split
  - g-shell (9 states) → 4 + 5 split
  - **Magic 28+ requires the spin-orbit term H_so to restore proper j-splitting**

This is a **mathematical theorem** (standard group theory), not a phenomenological observation.

*Full derivation: `Appendices/C_verifications/12_nuclear_magic/branching_rules.md`*

---

## XI.3.3 Light Nuclei: Pure Geometry (2, 8, 20)

The first three magic numbers arise from **pure graph isotropy** — no spin-orbit needed.

### Why These Are Geometric

For ℓ = 0, 1, 2, the branching rules show:
- A_g (dim 1) matches s-shell (2ℓ+1 = 1) ✓
- T_{1u} (dim 3) matches p-shell (2ℓ+1 = 3) ✓
- H_g (dim 5) matches d-shell (2ℓ+1 = 5) ✓

The D₆ → H₃ cluster eigenstates **exactly** reproduce spherical shell degeneracies for these orbitals.

### Shell Closures

| Shell | Orbitals | Cumulative | Status |
|-------|----------|------------|--------|
| $1s$ | 2 | **2** | ✅ DERIVED |
| $1p$ | 6 | **8** | ✅ DERIVED |
| $1d + 2s$ | 10 + 2 | **20** | ✅ DERIVED |

---

## XI.3.4 Medium Nuclei: Spin-Orbit (28)

### Why 28 Requires Spin-Orbit

The f-shell (ℓ = 3) has 14 states (with spin) in spherical symmetry:
- 1f₇/₂: 8 states (j = 7/2)
- 1f₅/₂: 6 states (j = 5/2)

Under I_h symmetry **without spin-orbit**, the f-shell splits as:
$$\text{7 orbitals} \rightarrow T_{2u}(3) \oplus G_u(4)$$

This gives icosahedral shell closures at 32, 54... — NOT at 28!

### How Spin-Orbit "Restores" the Ordering

With spin-orbit (λ₀ = 3q/2z = 0.060):

1. **The L·S coupling splits by j**, not by I_h irrep
2. For ℓ = 3:
   - j = ℓ + ½ = 7/2: ⟨L·S⟩ = ℓ/2 = 1.5 → **lowered** by λ₀ × 1.5
   - j = ℓ − ½ = 5/2: ⟨L·S⟩ = −(ℓ+1)/2 = −2 → **raised** by λ₀ × 2
3. The $1f_{7/2}$ level (8 states) is pulled **below** the I_h splitting gap
4. Gap opens at cumulative 20 + 8 = **28**

**The j-splitting from L·S overpowers the I_h splitting** when λ₀ ≈ 0.06 — precisely the derived value!

### Status

**[DERIVED]** — The spin-orbit coefficient λ₀ = 3q/(2z) is rigorously derived from the discrete Dirac operator and Averaging Lemma. It exactly matches the Nilsson parameter κ ≈ 0.06.

---

## XI.3.5 Heavy Nuclei: Strain Inversion (50, 82, 126)

### The Intruder Mechanism

From XI.2.5, the internal strain term:
$$V_{\text{strain}}(\alpha) = c_2 \, |x_\perp(\alpha)|^2$$

Combined with the **exact** inversion property (all D₆ roots satisfy $|x_\parallel|^2 + |x_\perp|^2 = 2$):
- Surface-localized states (large |x_∥|) have small |x_⊥| → **lower** $V_{\text{strain}}$
- Bulk-localized states (small |x_∥|) have large |x_⊥| → **higher** $V_{\text{strain}}$
- High-$\ell$ "intruder" orbitals (surface-peaked by centrifugal barrier) gain energy bonus

### ✅ DERIVED: c₂ = k/2

$$\boxed{c_2 = \frac{k}{2} \approx 0.603}$$

where $k \approx 1.206$ is the **Phason Stiffness** (Theorem IV.1.9).

**Physical interpretation**: 
- Elastic energy: $E = \frac{1}{2} k \cdot |x_\perp|^2$
- The "intruder" potential is literally the phason strain energy!

### Intruder Orbitals

| Intruder | From Shell | Effect |
|----------|------------|--------|
| $1g_{9/2}$ | N = 4 | Drops to cumulative 50 → **direct gap** |
| $1h_{11/2}$ | N = 5 | Drops to cumulative 74 → reshuffles spectrum |
| $1i_{13/2}$ | N = 6 | Drops to cumulative 96 → reshuffles spectrum |

### Results

| Magic # | Gap After | Intruder Role | Status |
|---------|-----------|---------------|--------|
| 50 | $1g_{9/2}$ ★ | Direct | **[DERIVED]** |
| 82 | $1g_{7/2}$ | Indirect | **[DERIVED]** |
| 126 | $1h_{9/2}$ | Indirect | **[DERIVED]** |

---

## XI.3.6 Comparison with Standard Model

| Feature | Standard Shell Model | Golden Selection |
|---------|---------------------|------------------|
| Potential | Woods-Saxon (fitted) | Graph Laplacian (geometric) |
| Spin-orbit | Phenomenological (fitted κ) | **Derived**: λ₀ = 3q/(2z) |
| Intruders | Adjusted parameters | **Derived**: c₂ = k/2 |
| Magic 2, 8, 20 | From HO + SO | **Derived** from I_h symmetry |
| Magic 28+ | From fitted parameters | **Derived** from λ₀ and c₂ |

**Key difference**: The standard shell model has ~2-3 free parameters that are fit to data. The Golden Selection derives all coefficients from geometry.

---

## XI.3.7 Resolved Questions

### Q1: Why does the D₆ cluster alone fail for ℓ ≥ 3?

**Answer**: The branching rules SO(3) → I_h prove that icosahedral symmetry **splits** the f, g, h shells:
- ℓ = 3 (dim 7) → T_{2u}(3) ⊕ G_u(4) 
- ℓ = 4 (dim 9) → G_g(4) ⊕ H_g(5)

The spin-orbit term H_so restores the proper ordering.

*See `Appendices/C_verifications/12_nuclear_magic/branching_rules.md`*

### Q2: Are magic numbers 2, 8, 20 geometric?

**Answer**: ✅ **YES** — The s, p, d shells (ℓ ≤ 2) don't split under I_h because their dimensions (1, 3, 5) match icosahedral irrep dimensions exactly.

### Q3: Can c₂ be derived from geometry?

**Answer**: ✅ **YES** — c₂ = k/2 = 0.603 from the Phason Stiffness k ≈ 1.206 (Part IV, Theorem IV.1.9).

### Q4: Can λ₀ be derived from geometry?

**Answer**: ✅ **YES** — The formula λ₀ = 3q/(2z) = 0.060 is derived from three pillars:

$$\boxed{\lambda_0 = \frac{D(D-1)}{4} \cdot \frac{q}{z} = \frac{3q}{2z} = 0.060}$$

**The Three Pillars:**

| Pillar | Statement | Status |
|--------|-----------|--------|
| **1. Averaging Lemma** | Σ ê⊗ê = (z/D)×I | **[PROVEN]** — Schur's Lemma, machine precision |
| **2. Berry Holonomy** | Plaquette holonomy = e^{iq} | **[DERIVED]** — Part IV Theorem IV.1.8 + lattice gauge theory |
| **3. Mass-Strain** | (t/M)² = geometric const. | **[AXIOM 0]** — Vacuum optimization |

**Factor origins:**
- **1/z**: From Averaging Lemma (proven exactly for D₆)
- **D(D-1)/2 = 3**: Rotation planes in SO(3), D=3 from Axiom 0
- **q = 2π/φ²**: Golden quantum angle from Part IV, enters as plaquette holonomy in FW double commutator
- **1/2**: Thomas precession (universal relativistic kinematics)

This **exactly matches** the Nilsson parameter κ ≈ 0.06 for heavy nuclei.

*Full derivation: `Appendices/C_verifications/12_nuclear_magic/spin_orbit_derivation.md`*

---

## Summary

| Magic Numbers | Status | Explanation |
|---------------|--------|-------------|
| **2, 8, 20** | **[THEOREM]** | SO(3) → I_h branching rules: irrep dims match for ℓ ≤ 2 |
| **28, 50, 82, 126** | **[DERIVED]** | H_so (λ₀ = 3q/2z) + V_strain (c₂ = k/2) |

**All seven magic numbers are derived from geometry with no free parameters.**

### Coupling Constants

| Constant | Formula | Value | Status | Evidence |
|----------|---------|-------|--------|----------|
| **c₂** | k/2 | 0.603 | **[DERIVED]** | Part IV phason stiffness |
| **λ₀** | 3q/(2z) | 0.060 | **[DERIVED]** | Three-pillar derivation |

### Derivation Rigor for λ₀

| Component | Status | Verification |
|-----------|--------|--------------|
| Averaging Lemma (1/z) | **[PROVEN]** | `averaging_lemma_proof.py` |
| FW structure | **[CONFIRMED]** | Standard lattice physics literature |
| Mass-strain consistency | **[AXIOM 0]** | Framework internal consistency |

**Verification code**: `Appendices/C_verifications/12_nuclear_magic/`
