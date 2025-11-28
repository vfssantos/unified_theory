# Notation and Conventions

This document establishes all notation used throughout the Golden Selection framework.

---

## Mathematical Constants

| Symbol | Definition | Numerical Value |
|--------|------------|-----------------|
| φ | Golden ratio = (1+√5)/2 | 1.6180339887498948... |
| φ⁻¹ | Inverse golden ratio = (√5-1)/2 | 0.6180339887498948... |
| φ² | φ + 1 | 2.6180339887498948... |
| φ³ | φ² + φ | 4.2360679774997896... |
| φ⁻² | 2 - φ | 0.3819660112501052... |
| φ⁻³ | 1/φ³ | 0.2360679774997896... |
| √5 | φ + φ⁻¹ | 2.2360679774997896... |

### Golden Ratio Identities

These identities are used frequently:

1. φ² = φ + 1
2. φ⁻¹ = φ - 1
3. φⁿ = φⁿ⁻¹ + φⁿ⁻² (Fibonacci recursion)
4. φ + φ⁻¹ = √5
5. φ × φ⁻¹ = 1
6. φ² + φ⁻² = 3
7. φ - φ⁻¹ = 1

---

## E₈ Lattice

### Basic Notation

| Symbol | Meaning |
|--------|---------|
| Λ_E₈ | The E₈ lattice in ℝ⁸ |
| α, β, γ | Generic E₈ root vectors |
| \|α\| | Euclidean norm of root α |
| ⟨α, β⟩ | Inner product (dot product) |
| 𝔢₈ | The E₈ Lie algebra |
| W(E₈) | The Weyl group of E₈ |

### Root Types

| Type | Description | Count |
|------|-------------|-------|
| D₈ | Vectors (±1, ±1, 0, 0, 0, 0, 0, 0) and permutations | 112 |
| S₈ | Vectors ½(±1, ±1, ±1, ±1, ±1, ±1, ±1, ±1) with even minus signs | 128 |

### Root Indexing

Throughout this document, roots are indexed 0-239 in a fixed order:
- Roots 0-111: D₈ type
- Roots 112-239: S₈ type

See [Appendix A](../Appendices/A_e8_root_tables.md) for the complete list.

---

## Projection

### 8D → 4D Projection

| Symbol | Meaning |
|--------|---------|
| P_φ | The golden projection matrix (4×8) |
| V_phys | Physical 4D subspace |
| V_int | Internal 4D subspace |
| x = P_φ · α | Physical projection of root α |
| ξ = π_int(α) | Internal projection of root α |

### Pythagorean Relation

For any E₈ root α with \|α\|² = 2:

$$|x|^2 + |\xi|^2 = 2$$

### Shell Classification

| Shell | Physical Radius | Internal Radius |
|-------|-----------------|-----------------|
| Inner | R_inner ≈ 0.7435 | R_int,outer ≈ 1.2030 |
| Outer | R_outer ≈ 1.2030 | R_int,inner ≈ 0.7435 |

Note: Inner/outer are **swapped** between physical and internal.

---

## 600-Cell Geometry

### Height (Latitude)

| Symbol | Meaning |
|--------|---------|
| h(α) | Height of root α in vertex-first slicing |
| v_⊥ | Perpendicular component (in H₃) |

Relation: \|v_⊥\|² = 4 - h²

### Height Spectrum (Inner 600-Cell)

| Height h | Count | 3D Polytope | Physical Role |
|----------|-------|-------------|---------------|
| ±2 | 1 | Pole | — |
| ±φ | 12 | Icosahedron | **Gauge** |
| ±1 | 20 | Dodecahedron | **Matter** |
| ±φ⁻¹ | 12 | Icosahedron | Intermediate |
| 0 | 30 | Icosidodecahedron | Equator |

### Symmetry Groups

| Symbol | Name | Order |
|--------|------|-------|
| H₄ | 4D icosahedral group | 14,400 |
| H₃ | 3D icosahedral group | 120 |
| T_h | Pyritohedral group | 24 |
| A₅ | Alternating group (icosahedral rotations) | 60 |

---

## Physics Quantities

### Electroweak

| Symbol | Meaning | Observed Value |
|--------|---------|----------------|
| θ_W | Weinberg (weak mixing) angle | ~28.7° |
| sin²θ_W | Weak mixing parameter | 0.23122 ± 0.00004 |
| m_W | W boson mass | 80.377 GeV |
| m_Z | Z boson mass | 91.188 GeV |
| m_H | Higgs mass | 125.10 GeV |
| v | Higgs VEV | 246 GeV |

### Fermion Masses

| Symbol | Meaning |
|--------|---------|
| m_e, m_μ, m_τ | Charged lepton masses |
| m_u, m_c, m_t | Up-type quark masses |
| m_d, m_s, m_b | Down-type quark masses |

### Koide Parameters

| Symbol | Meaning |
|--------|---------|
| Q | Koide ratio = Σm / (Σ√m)² |
| θ₀ | Koide phase (angle in mass plane) |
| M₀ | Koide scale parameter |

Koide formula:
$$\sqrt{m_i} = M_0 \left(1 + \sqrt{2}\cos(\theta_0 + \frac{2\pi i}{3})\right)$$

### Mixing Matrices

| Symbol | Meaning |
|--------|---------|
| V_CKM | Quark mixing (Cabibbo-Kobayashi-Maskawa) |
| U_PMNS | Lepton mixing (Pontecorvo-Maki-Nakagawa-Sakata) |
| θ₁₂, θ₂₃, θ₁₃ | Mixing angles |
| δ | CP-violating phase |

---

## Lie Algebra Notation

| Symbol | Meaning | Dimension |
|--------|---------|-----------|
| 𝔢₈ | E₈ Lie algebra | 248 |
| 𝔰𝔬(16) | SO(16) Lie algebra | 120 |
| 𝔰𝔬(10) | SO(10) = Spin(10) algebra | 45 |
| 𝔰𝔲(5) | SU(5) Lie algebra | 24 |
| 𝔰𝔲(4) | SU(4) = A₃ algebra | 15 |
| 𝔰𝔬(8) | SO(8) = D₄ algebra | 28 |
| 𝔰𝔲(3) | SU(3) color algebra | 8 |
| 𝔰𝔲(2) | SU(2) weak algebra | 3 |

### Standard Embeddings

$$E_8 \supset \text{Spin}(16) \supset \text{Spin}(10) \supset \text{SU}(5) \supset \text{SU}(3) \times \text{SU}(2) \times \text{U}(1)$$

---

## Document Conventions

### Equation Numbering

- Equations in Section X are numbered (X.1), (X.2), etc.
- Major results use boxed format: $\boxed{\text{result}}$

### Cross-References

- [THEOREM X.Y]: Reference to theorem
- [POSTULATE X]: Reference to postulate
- [DERIVATION X.Y]: Reference to derivation
- [Appendix A]: Reference to appendix
- [Section X]: Reference to section

### Code

- All verification code is in Python 3
- Uses NumPy for numerical work
- Full scripts in [Appendix D](../Appendices/D_verification_code.md)

