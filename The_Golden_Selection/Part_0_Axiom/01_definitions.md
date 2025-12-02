# Definitions and Notation

## Core Quantities

### Geometric Free Energy ($F$)

$$F[\mathcal{G}] = E_{\text{strain}}[\mathcal{G}] + \lambda \cdot \kappa_{\text{Schur}}[\mathcal{G}]$$

| Term | Symbol | Meaning |
|------|--------|---------|
| Strain Energy | $E_{\text{strain}}$ | Physical instability (phason elastic energy) |
| Schur Curvature | $\kappa_{\text{Schur}}$ | Information-geometric complexity/roughness |
| Coupling | $\lambda$ | Relative weight of information-geometric vs physical terms |

#### Strain Energy ($E_{\text{strain}}$)

In quasicrystal elasticity, this is the **phason elastic energy**:
$$E_{\text{strain}} = \frac{1}{2} \int K_{ijkl} \, w_{ij} w_{kl} \, dV$$

where $w_{ij}$ is the phason strain tensor. This is [KNOWN] — standard quasicrystal physics.

**Physical meaning**: Energy cost of deviating from the ideal aperiodic structure.

#### Schur-Convex Curvature ($\kappa_{\text{Schur}}$)

From Bruna (2025), arXiv:2510.20845:
$$\kappa_{\text{Schur}} = A \cdot I_1^2 + B \cdot (I_2 - I_1^2)$$

where $I_1, I_2$ are invariant moments under dihedral symmetry, and $A, B$ are coefficients determined by the projector geometry.

**Key property**: Has unique stationary point at $q^* = \phi^{-2}$ for D₁₂ symmetry.

#### Coupling Constant ($\lambda$)

The relative weight between physical and information-geometric terms. In practice:
- λ **does not determine the equilibrium** — Bruna proves κ_Schur has its unique minimum at φ⁻² independently of λ
- Any positive λ gives φ⁻² as the equilibrium; λ only affects **convergence speed**
- Can be absorbed into the normalization of $\kappa_{\text{Schur}}$

**Physical identification**: λ is the **inverse temperature (precision) of the collective mode**. It controls how strongly the system "cares about" pattern formation vs total intensity.

**Why this is not circular**: Both $\kappa_{\text{Schur}}$ and $D_{\text{KL}}$ are convex with a shared unique minimum at $\phi^{-2}$. By convex analysis, their gradient flows trace the same path to this equilibrium regardless of λ. The golden ratio is selected by the D₁₂ geometry (C₂ × C₃ interference), not by tuning λ.

### Golden Ratio (φ)

$$\phi = \frac{1 + \sqrt{5}}{2} \approx 1.6180339887...$$

**Key identities**:
- $\phi^2 = \phi + 1$
- $\phi^{-1} = \phi - 1 \approx 0.618$
- $\phi^{-2} = 2 - \phi \approx 0.382$
- $\phi + \phi^{-1} = \sqrt{5}$

### Statistical Complexity ($C_\mu$)

$$C_\mu = H[\mathcal{S}] = -\sum_{s \in \mathcal{S}} P(s) \log P(s)$$

Shannon entropy of **causal states** — the minimal ε-machine.

### Colin de Verdière Invariant ($\mu(G)$)

Spectral measure of graph embeddability:
- $\mu(G) \leq 3$: Planar (2D)
- $\mu(G) \leq 4$: Linkless in 3D
- $\mu(G) \geq 6$: Intrinsically knotted

---

## Geometric Objects

### D₆ Lattice

$$D_6 = \{ x \in \mathbb{Z}^6 : \sum_i x_i \equiv 0 \pmod{2} \}$$

- **Dimension**: 6
- **Roots**: 60 vectors of form $\pm e_i \pm e_j$
- **Subalgebras**: Contains A₂, D₄, A₃

### H₃ Group

The **icosahedral point group**:
- **Order**: 120 = 60 rotations × 2 (with inversions)
- **Generators**: 5-fold, 3-fold, 2-fold rotations
- **Non-crystallographic**: Contains 5-fold axes

### Projection Decomposition

$$\mathbb{R}^6 = E_\parallel \oplus E_\perp$$

| Space | Dimension | Physical Role |
|-------|-----------|---------------|
| $E_\parallel$ | 3 | Physical space |
| $E_\perp$ | 3 | Internal/phason space |

---

## Claim Status Tags

| Symbol | Type | Meaning |
|--------|------|---------|
| **[ASSUMPTION]** | Foundational | Posited, not derived |
| **[KNOWN]** | External | Established theorem with citation |
| **[DERIVED]** | Our contribution | Follows from axiom + known results |
| **[CONJECTURE]** | Speculative | Motivated but unproven |
| **[VERIFIED]** | Checked | Numerically or computationally confirmed |

---

## Physical Constants

| Symbol | Name | Value |
|--------|------|-------|
| $\theta_W$ | Weinberg angle | $\sin^2\theta_W \approx 0.231$ |
| $\theta_C$ | Cabibbo angle | $\approx 13°$ |
| $Q$ | Koide ratio | $2/3$ (leptons) |
| $m_Z$ | Z boson mass | 91.2 GeV |
| $m_H$ | Higgs mass | 125.1 GeV |

---

## Orbit Notation

**Warning**: The symbol ω₃ has different meanings in different contexts:

| Symbol | Context | Meaning | Count |
|--------|---------|---------|-------|
| ω₃(H₃) | H₃ weight orbit | Dodecahedron vertices | 20 |
| **ω₃(D₆)** | D₆ weight orbit | Third fundamental weight | **160** |
| ω₅(D₆) | D₆ spinor orbit | Half-integer coordinates | 32 |

In Part III (shell structure), ω₃ typically refers to the H₃ dodecahedron (20 vertices).

In Part IV (mass mechanism), ω₃ refers to the D₆ weight orbit (160 states) which decomposes into 4 shells (20+60+60+20).

When context is ambiguous, we write ω₃(H₃) or ω₃(D₆) explicitly.
