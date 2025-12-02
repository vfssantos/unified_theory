# II.A — Projection Requirement

## Statement

> **THEOREM II.A.1 (Cut-and-Project Necessity)**:
> 
> Every quasicrystal is a **projection** from a higher-dimensional periodic lattice.

---

## The Cut-and-Project Method

### Definition

Let Λ be a lattice in ℝⁿ. The **cut-and-project** construction produces a quasicrystal in ℝᵈ (d < n):

1. **Decompose**: ℝⁿ = V_∥ ⊕ V_⊥ where dim(V_∥) = d
2. **Project**: P_∥: ℝⁿ → V_∥ (physical space)
3. **Window**: W ⊂ V_⊥ (acceptance domain)
4. **Select**: Q = {P_∥(p) : p ∈ Λ, P_⊥(p) ∈ W}

The resulting set Q is a **quasicrystal** if the projection direction is irrational with respect to the lattice.

### Key Properties

- **Discrete**: Q is a discrete point set
- **Aperiodic**: No translation symmetry (for irrational slopes)
- **Long-range order**: Sharp diffraction peaks
- **Deterministic**: Fully specified by (Λ, V_∥, W)

---

## Why Projection is Necessary

### LEMMA II.A.1a: Aperiodic order requires irrational structure

**Proof**: A periodic structure has rational relationships between all length scales. For aperiodicity, we need incommensurate (irrational) length ratios. These arise naturally from projecting a rational (integer) lattice along an irrational direction. ∎

### LEMMA II.A.1b: Higher dimension provides the irrationality

**Proof**: In 1D, a quasiperiodic sequence (e.g., Fibonacci) arises from projecting ℤ² along slope 1/φ (irrational). The golden ratio φ is "stored" in the 2D structure and "revealed" by projection. ∎

---

## Dimension Requirements

For an H₃ (icosahedral) quasicrystal in 3D:

| Target Symmetry | Minimum Source Dimension | Method |
|-----------------|-------------------------|--------|
| 5-fold (2D) | 4D or 5D | ℤ⁵ or Penrose |
| 8-fold (2D) | 4D | ℤ⁴ with specific window |
| **Icosahedral (3D)** | **6D minimum** | Standard cut-and-project |
| **Icosahedral (3D)** | **8D (E₈)** | **Optimal (maximal symmetry)** |

### Why E₈ over ℤ⁶?

Both ℤ⁶ and E₈ can produce icosahedral quasicrystals. However:

| Property | ℤ⁶ | E₈ |
|----------|-----|-----|
| Dimension | 6 | 8 |
| Symmetry | Low | Maximal exceptional |
| Root count | — | 240 |
| Self-dual? | No | Yes (even self-dual) |
| Uniqueness | Not unique | **Unique** in 8D |

E₈ provides **maximal structure** for the projection.

---

## The Superspace Formalism

### Physical vs. Perpendicular Space

For an icosahedral quasicrystal:

| Space | Dimension | Role |
|-------|-----------|------|
| Physical (E_∥) | 3D | Where atoms live |
| Perpendicular (E_⊥) | 3D | Controls aperiodicity |
| **Total** | **6D** | Minimum embedding |

The E₈ projection adds additional structure:
- 8D total
- 4D "parallel" (containing H₄)
- 4D "perpendicular"

---

## Implication

> Quasicrystals are not "random" or "accidental" — they are **shadows** of higher-dimensional periodic structures.

The specific choice of source lattice (E₈) and projection direction (golden eigenvalues) determines all properties of the resulting quasicrystal.

→ Section II.B asks: Why must the intermediate step be H₄?

---

## References

- de Bruijn, N.G. "Algebraic Theory of Penrose's Non-Periodic Tilings" (1981)
- Duneau, M. & Katz, A. "Quasiperiodic Patterns" (1985)
- Elser, V. "The Diffraction Pattern of Projected Structures" (1986)


