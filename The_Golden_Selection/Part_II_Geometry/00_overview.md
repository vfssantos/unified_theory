# Part II: Geometry — Why E₈?

## Overview

Part I established that reality is a **3D quasicrystal with H₃ symmetry**.

Part II asks: **Where does this structure come from geometrically?**

The answer: It is a **projection from the E₈ lattice** in 8 dimensions.

---

## The Question

Quasicrystals cannot be "built" directly in 3D — they are mathematically defined as **projections from higher-dimensional periodic lattices**.

**Question**: What higher-dimensional lattice produces an H₃ quasicrystal with the structure needed for physics?

---

## ⚠️ Important Clarification: 6D vs 8D

### The Minimal Option (6D)

For **geometry alone**, 6D crystallographic lattices suffice:

| Lattice | Dimension | Type | H₃ Path | Physics Content |
|---------|-----------|------|---------|-----------------|
| **D₆** | 6 | Crystallographic | Direct | Minimal |
| ℤ⁶ | 6 | Crystallographic | Direct | Minimal |

This is the **standard approach** in materials science for icosahedral quasicrystals.

### The Exceptional Option (8D)

The Golden Selection uses E₈ because it requires **additional structure**:

| Lattice | Dimension | Type | H₃ Path | Physics Content |
|---------|-----------|------|---------|-----------------|
| **E₈** | 8 | Exceptional | Via H₄ | Rich (golden + families) |

### Why Not E₆?

One might ask: "Why not use the exceptional E₆ (6D) instead?"

**Answer**: E₆ does **not** produce H₃ geometry.
- W(E₆) has no reflection subgroup of type H₃
- E₆ is tied to tetrahedral (2T) geometry, not icosahedral
- E₆ is used for 2D 12-fold/7-fold quasicrystals, not 3D icosahedral

See `Appendices/D_delegations/08_e6_alternative/` for full analysis.

### The Choice

```
MINIMAL PATH:      D₆ (6D, crystallographic) → H₃ directly
EXCEPTIONAL PATH:  E₈ (8D, exceptional) → H₄ → H₃ with golden structure
DEAD END:          E₆ → H₃  ✗ (incompatible)
```

The Golden Selection uses the **exceptional path** because the axiom demands not just geometry, but structure for deriving physics.

---

## The Logic Chain

```
THEOREM II.A.1: Quasicrystals require projection from higher-D lattices
            ↓
THEOREM II.B.1: For exceptional + golden structure, H₃ requires H₄ parent
            ↓
THEOREM II.C.1: H₄ requires 8D embedding (Galois conjugation of φ)
            ↓
THEOREM II.C.2: E₈ is the unique exceptional lattice in 8D for H₄
            ↓
THEOREM II.D.1: The projection has eigenvalue φ (golden ratio)
            ↓
RESULT: E₈ → H₄ → H₃ is the unique exceptional completion
```

---

## Why the Axiom Selects E₈ Over D₆

Both D₆ and E₈ produce H₃ geometry. But the axiom **selects E₈** from first principles:

### Criterion 1: Algebraic Closure

| Model | Golden Ratio φ | Status |
|-------|----------------|--------|
| **D₆** | Appears in projection (chosen) | Free parameter — can be perturbed |
| **E₈** | Appears as eigenvalue (forced by Galois) | **Locked** — algebraically necessary |

In E₈, φ is derived from the projection matrix eigenvalues. In D₆, φ must be re-assumed.

### Criterion 2: Preservation of Derivation

The axiom derives φ from H₃ geometry (Bruna 2025: Schur curvature minimum).

| Model | φ in H₃ | φ in Embedding | Derivation Preserved? |
|-------|---------|----------------|----------------------|
| **D₆** | Derived ✅ | Re-assumed ❌ | **No** — chain broken |
| **E₈** | Derived ✅ | Still derived ✅ | **Yes** — chain intact |

E₈ maintains the logical chain; D₆ breaks it by re-introducing φ as a parameter.

### Criterion 3: Topological Complexity

| Model | $C_\mu$ | Stability | Selected? |
|-------|---------|-----------|-----------|
| **D₆** | High | Good but φ arbitrary | Local max |
| **E₈** | High | Locked (φ eigenvalue) | **Global max** |

**Conclusion**: E₈ is selected because it preserves the algebraic closure of the derivation chain.

---

## Summary Table

| Section | Question | Answer | Status |
|---------|----------|--------|--------|
| **II.A** | Why projection? | Quasicrystals are cut-and-project | [KNOWN] |
| **II.B** | Why H₄? | Exceptional + golden requires H₄ parent | [DERIVED] |
| **II.C** | Why E₈? | Unique exceptional lattice for H₄ | [PROVEN] |
| **II.D** | Why φ? | Eigenvalue of Elser-Sloane projection | [PROVEN] |

---

## Files in This Part

1. `01_projection.md` — Section II.A: Cut-and-project necessity
2. `02_h4_parent.md` — Section II.B: H₄ as intermediate
3. `03_e8_selection.md` — Section II.C: E₈ uniqueness (includes D₆ discussion)
4. `04_golden_ratio.md` — Section II.D: φ emergence
