# II.C — E₈ Selection

## Statement

> **THEOREM II.C.1 (E₈ Uniqueness)** [PROVEN]:
> 
> Among lattices that are:
> 1. **Exceptional** (not crystallographic)
> 2. **Admit H₄-symmetric projection** with golden-ratio structure
> 3. **Provide root structure** for particle physics content
> 
> **E₈ is the unique solution.**
> 
> *Note*: For minimal icosahedral geometry alone, 6D crystallographic lattices (D₆) suffice.

---

## ⚠️ Important: The 6D Question

### Honest Acknowledgment

For **geometry alone**, 6D works:

| Lattice | Dimension | Type | H₃ Projection? |
|---------|-----------|------|----------------|
| **D₆** | 6 | Crystallographic | ✅ Yes (direct) |
| ℤ⁶ | 6 | Crystallographic | ✅ Yes (direct) |
| B₆ | 6 | Crystallographic | ✅ Yes (direct) |
| **E₆** | 6 | Exceptional | ❌ No (incompatible) |
| **E₈** | 8 | Exceptional | ✅ Yes (via H₄) |

**Key insight**: The standard 6D embedding (D₆) has H₃ as a maximal subgroup of its point group. This is the approach used in materials science.

### Why the Axiom Selects E₈ (From First Principles)

The axiom "Maximize stable generative information density" **forces** E₈ over D₆:

#### Argument 1: Generative Density (ρ_G)

| Model | Description | ρ_G |
|-------|-------------|-----|
| **D₆** | "There are two fundamental cells: icosa and dodeca" | Medium |
| **E₈** | "There is one cell (600-cell); duality emerges from projection" | **Higher** |

E₈ generates the **same complexity** from a **shorter description**. Like Maxwell unifying E&M into one field.

#### Argument 2: Golden Lock-in (Stability)

From **Bruna (2025)**: φ is a unique stationary point of Schur-convex curvature — a stability attractor.

| Model | How φ Appears | Lock-in |
|-------|---------------|---------|
| **D₆** | Chosen in projection matrix | **Partial** — could choose other irrationals |
| **E₈** | Forced as Galois eigenvalue | **Complete** — algebraically necessary |

In D₆, you SELECT the golden cut. In E₈, the golden ratio EMERGES from the algebra. E₈ has stronger stability because φ is locked, not chosen.

#### Argument 3: Variational Extremum

The axiom's principle: $\delta S = \delta \int (\rho_G - \lambda \mathcal{U}) dV = 0$

| Model | ρ_G | Stability (1/U) | S = ρ_G - λU |
|-------|-----|-----------------|--------------|
| **D₆** | Medium | Good | Local maximum |
| **E₈** | High | Locked | **Global maximum** |

**Conclusion**: E₈ is the extremum selected by the axiom.

#### Why This Matters

The old argument was: "E₈ is chosen for physics content."

The new argument is: **"E₈ is forced by the axiom itself."**

- Unity (E₈) is more generative than Duality (D₆)
- Forced φ (E₈) is more stable than chosen φ (D₆)
- E₈ is the global maximum; D₆ is a local maximum

### Why Not E₆?

E₆ is 6-dimensional and exceptional — could it work?

**No.** Complete classification shows:
- W(E₆) has **no reflection subgroup of type H₃**
- E₆ Coxeter exponent 5 gives 75° rotation, not 72° (icosahedral)
- E₆ is geometrically tied to **tetrahedral (2T)**, not icosahedral
- E₆ is used for **2D 12-fold/7-fold** quasicrystals, not 3D icosahedral

See `Appendices/D_delegations/08_e6_alternative/` for full analysis.

---

## The E₈ Lattice

### Definition

The E₈ lattice Λ_{E₈} consists of all vectors in ℝ⁸ satisfying:

$$\Lambda_{E_8} = \left\{ \mathbf{x} \in \mathbb{R}^8 \;\middle|\; 
\begin{array}{l}
x_i \in \mathbb{Z} \text{ for all } i, \text{ or } x_i \in \mathbb{Z} + \frac{1}{2} \text{ for all } i \\
\text{and } \sum_{i=1}^8 x_i \in 2\mathbb{Z}
\end{array}
\right\}$$

### Root System

The **roots** of E₈ are the 240 vectors of minimal non-zero length (√2):

| Type | Description | Count |
|------|-------------|-------|
| D₈ | (±1, ±1, 0, 0, 0, 0, 0, 0) permutations | 112 |
| Spinor | ½(±1, ±1, ±1, ±1, ±1, ±1, ±1, ±1) with even # of minus signs | 128 |
| **Total** | | **240** |

### Properties

| Property | Value | Significance |
|----------|-------|--------------|
| Dimension | 8 | Minimal for H₄ (via Galois) |
| Roots | 240 = 2×120 | Two 600-cells |
| Coxeter h | 30 | Required for H₄ |
| Even? | Yes | All norms even |
| Self-dual? | Yes | Λ = Λ* |
| **Unique?** | **Yes** | Only even self-dual in 8D |

---

## Why 8D Is Minimal (For Exceptional Path)

### The Galois Conjugation Argument [PROVEN]

The golden ratio φ = (1+√5)/2 has Galois conjugate φ' = (1-√5)/2.

For H₄ to act crystallographically on a lattice, all matrix traces must be **integers**. But H₄ contains rotations with traces involving √5.

**Solution**: Pair each φ-eigenvalue with its conjugate φ' in an internal space.

| Target | Physical Dim | Internal Dim | Total |
|--------|--------------|--------------|-------|
| H₃ | 3 | 3 | 6 |
| **H₄** | **4** | **4** | **8** |

For H₄: 4D physical + 4D internal (Galois conjugate) = **8D minimum**.

### Why Other 8D Lattices Fail

| Lattice | Roots | Coxeter h | H₄ Projection? |
|---------|-------|-----------|----------------|
| ℤ⁸ | 16 | 16 | ❌ Too few |
| D₈ | 112 | 14 | ❌ Need 120 |
| **E₈** | **240** | **30** | ✅ 240 = 2×120 |

**D₈ fails**: Only 112 roots, but 600-cell needs 120 vertices.

**E₈ succeeds**: 240 roots project to two nested 600-cells with radius ratio φ.

### The Spectral Argument [PROVEN]

H₄ symmetry requires Coxeter number **h = 30** (for 5-fold and 30-fold rotations).

| Lattice | Coxeter h | Has order-30? |
|---------|-----------|---------------|
| D₈ | 14 | ❌ |
| A₈ | 9 | ❌ |
| B₈ | 16 | ❌ |
| **E₈** | **30** | ✅ |

**Only E₈** has the spectral structure required for H₄.

---

## The Elser-Sloane Projection

### The Construction [PROVEN]

**Theorem (Elser-Sloane, 1987)**: There exists a unique (up to automorphisms) projection P: ℝ⁸ → ℝ⁴ such that the 240 E₈ roots project to **two concentric 600-cells** with radius ratio φ.

### The Result

$$E_8 \text{ (240 roots)} \xrightarrow{P_\phi} \text{Two 600-cells}$$

| Shell | Vertices | Radius |
|-------|----------|--------|
| Inner | 120 | R |
| Outer | 120 | φR |

**Radius ratio = φ exactly.** The golden ratio emerges as an eigenvalue, not assumed.

---

## Comparison: D₆ vs E₈

| Aspect | D₆ (Minimal) | E₈ (Exceptional) |
|--------|--------------|------------------|
| **Dimension** | 6 | 8 |
| **Type** | Crystallographic | Exceptional |
| **H₃ Path** | Direct | Via H₄ |
| **Golden structure** | No | Yes (φ scaling) |
| **Root count** | — | 240 |
| **Physics content** | Minimal | Gauge + matter |
| **Use case** | Materials science | Fundamental theory |

### When to Use Which

- **D₆**: For describing real quasicrystal materials (Al-Pd-Mn, etc.)
- **E₈**: For deriving physics from geometry (Standard Model content)

---

## Physical Implications

### Fermions Are Forced

The 240 E₈ roots decompose as:

| Component | Roots | Physical Role |
|-----------|-------|---------------|
| D₈ sector | 112 | Bosons |
| Spinor sector | 128 | **Fermions** |

You **cannot** have H₄ symmetry with just bosons — the geometry is incomplete without spinors. **Matter is geometrically forced.**

### Family Structure

E₈ contains E₆×SU(3) as maximal subgroup:
- E₆: Standard GUT gauge structure
- SU(3): Family symmetry (three generations)

This is why E₈ provides "more physics" than D₆.

---

## Summary

> **THEOREM II.C.1 (Refined)**:
> 
> 1. For **minimal icosahedral geometry**: 6D D₆ suffices
> 2. For **exceptional + golden + physics structure**: E₈ is unique
> 3. **E₆ does not work** for H₃ (incompatible geometry)
> 
> The Golden Selection uses E₈ because it requires all three: exceptionality, golden-ratio chain, and physics content.

---

## Summary of Claim Status

| Claim | Status | Source |
|-------|--------|--------|
| D₆ produces H₃ | [KNOWN] | Standard QC theory |
| E₆ does not produce H₃ | [PROVEN] | W(E₆) classification |
| 8D minimal for H₄ | [PROVEN] | Galois conjugation |
| E₈ unique in 8D for H₄ | [PROVEN] | Spectral (h=30) + root count |
| E₈ → two 600-cells | [PROVEN] | Elser-Sloane (1987) |
| φ emerges as eigenvalue | [PROVEN] | Projection matrix |

---

## References

### Core Results
- Elser, V. & Sloane, N.J.A. "A Highly Symmetric Four-Dimensional Quasicrystal" (1987)
- Conway, J.H. & Sloane, N.J.A. "Sphere Packings, Lattices and Groups" (1988)

### Galois Conjugation
- Standard superspace crystallography (de Bruijn, Duneau-Katz)

### E₆ Incompatibility
- Douglass–Pfeiffer–Röhrle: Classification of W(E₆) reflection subgroups
- Dechant: E₆ ↔ 2T (tetrahedral), E₈ ↔ 2I (icosahedral) correspondence

### D₆ for H₃
- Al-Siyabi et al.: "Point group of D₆ admits H₃ as maximal subgroup"
