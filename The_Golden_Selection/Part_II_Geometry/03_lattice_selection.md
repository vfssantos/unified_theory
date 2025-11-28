# II.C Lattice Selection: The Case for D₆ (6D)

## Overview

The selection of the fundamental lattice follows from the **Topological Complexity Axiom** and the requirement of **minimality**. We do not select D₆ because it "explains physics" — that would be circular. We select D₆ because it is the **minimal structure** that satisfies the geometric requirements established in Parts I and II.

### Key Results

- **[THEOREM II.C.1]**: D₆ is the minimal crystallographic lattice admitting H₃-symmetric golden projection.
- **[THEOREM II.C.2]**: The 3+3 dimensional split of D₆ is forced by the cut-and-project requirement for non-crystallographic H₃ symmetry.

### Prerequisites

- [Section I.B]: D = 3 (Golden Lock)
- [Section I.C]: H₃ symmetry selection
- [Section II.A]: Cut-and-Project necessity
- [Section II.B]: H₃ projection geometry

---

## II.C.1 The Minimality Argument

### The Constraint Chain

From Part I and Part II.A-B, we have established:

1. **D = 3**: The Golden Lock (Zeeman + μ ≥ 6) forces exactly 3 spatial dimensions.
2. **H₃ Symmetry**: Topological complexity in 3D selects icosahedral symmetry.
3. **Cut-and-Project**: H₃ quasicrystals require projection from a higher-dimensional periodic lattice.

### The Dimensional Requirement

H₃ is a **non-crystallographic** point group in 3D — it cannot be the symmetry of any periodic lattice in 3 dimensions.

**Theorem (Embedding Dimension)** [Duneau & Katz 1985; Elser 1986]:

> To realize a non-crystallographic point group $G$ acting on $\mathbb{R}^n$ via cut-and-project from a periodic lattice, the minimal embedding dimension is $2n$.

**Proof sketch**: The group $G$ must act crystallographically in the embedding space. For icosahedral symmetry, the minimal faithful representation decomposes as $\mathbb{R}^6 = E_{\parallel} \oplus E_{\perp}$, where both subspaces carry inequivalent 3D representations of H₃.

For H₃ acting on $\mathbb{R}^3$:
$$\dim(\Lambda_{\min}) = 2 \times 3 = 6$$

This is not a choice — it is a **mathematical necessity**.

**References**:
- Duneau, M. & Katz, A. "Quasiperiodic Patterns" *Phys. Rev. Lett.* **54**, 2688 (1985)
- Elser, V. "The Diffraction Pattern of Projected Structures" *Acta Cryst. A* **42**, 36 (1986)

### The Lattice Candidates in 6D

Given the 6D requirement, which lattice?

| Lattice | Dimension | Type | H₃ Projection? |
|---------|-----------|------|----------------|
| $\mathbb{Z}^6$ | 6 | Primitive cubic | ✅ Yes |
| **D₆** | 6 | Root lattice | ✅ Yes (golden) |
| A₆ | 6 | Root lattice | ❌ No (wrong symmetry) |

Both $\mathbb{Z}^6$ and D₆ admit H₃ projections. However:

- **$\mathbb{Z}^6$**: Admits H₃ projection, but φ must be inserted by hand.
- **D₆**: The golden ratio φ emerges as an **eigenvalue** of the projection matrix (Koca et al. 2015).

### Selection Criterion: Algebraic Closure

The Golden Selection Axiom, via Bruna (2025), establishes that φ is the unique Schur-convex curvature minimum — it is **derived**, not assumed.

To preserve this derivation chain:
- The embedding lattice must produce φ **algebraically**, not as a free parameter.
- D₆ satisfies this: the Koca projection matrix has eigenvalues involving φ.
- $\mathbb{Z}^6$ does not: φ must be chosen arbitrarily.

> **[THEOREM II.C.1]**: D₆ is the minimal crystallographic lattice that:
> 1. Embeds H₃ (requires dim ≥ 6), and
> 2. Produces φ as an algebraic eigenvalue of the projection.

---

## II.C.2 The 3+3 Dimensional Split

The cut-and-project method decomposes the embedding space:

$$\mathbb{R}^6 = E_{\parallel} \oplus E_{\perp}$$

where:
- $E_{\parallel} \cong \mathbb{R}^3$: The **physical subspace** (projection target)
- $E_{\perp} \cong \mathbb{R}^3$: The **internal subspace** (perpendicular complement)

This is not a choice — it is forced by the projection geometry.

### The Physical Interpretation

The internal space $E_{\perp}$ has physical meaning in quasicrystal physics:

1. **Phason Modes**: Degrees of freedom in $E_{\perp}$ correspond to collective excitations called **phasons**.
2. **Measurable Effects**: Phasons cause diffuse scattering, heat transport, and peak shifts in diffraction.
3. **Energy Cost**: Phason strain has a well-defined elastic energy.

The 3+3 split is therefore **physically grounded** — it is not an abstract mathematical convenience.

---

## II.C.3 Why Not E₈?

E₈ (8D) also admits H₃ projection (via H₄ intermediate). Why not use it?

**Answer**: E₈ violates minimality.

| Criterion | D₆ (6D) | E₈ (8D) |
|-----------|---------|---------|
| Minimal dimension for H₃? | ✅ Yes (2×3=6) | ❌ No (+2 extra) |
| Golden ratio derived? | ✅ Yes (Koca eigenvalue) | ✅ Yes (Elser-Sloane) |
| Physical grounding? | ✅ Real quasicrystals | ❌ Theoretical only |

Both lattices produce the golden ratio algebraically. But D₆ does so in the **minimal** dimension.

The axiom of Topological Complexity does not favor "more structure" — it favors **maximal complexity per degree of freedom**. Adding unnecessary dimensions dilutes complexity.

> **Selection**: D₆ is selected over E₈ by the principle of **minimal sufficiency**.

---

## II.C.4 Summary

| Property | Value | Source |
|----------|-------|--------|
| Embedding dimension | 6 | Forced by H₃ non-crystallographic |
| Lattice | D₆ | Minimal with algebraic φ |
| Physical space | $E_{\parallel} \cong \mathbb{R}^3$ | Cut-and-project |
| Internal space | $E_{\perp} \cong \mathbb{R}^3$ | Cut-and-project |
| Golden ratio | φ = (1+√5)/2 | Projection eigenvalue |

The theory proceeds on the **D₆ → H₃ quasicrystal**.

---

## Note on Physics Predictions

The fact that D₆ contains subalgebras (A₂, D₄, A₃) relevant for Standard Model physics is a **consequence**, not a motivation. These structures are discovered *after* selecting D₆ on geometric grounds.

See **Part III** for the physics that emerges from this geometry.
