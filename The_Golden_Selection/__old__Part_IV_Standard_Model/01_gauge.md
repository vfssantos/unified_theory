# IV.1 — Gauge Groups: SU(3)×SU(2)×U(1) from D₆ Geometry

## Statement

> **THEOREM IV.1.1 (Gauge Group Embedding)** [VERIFIED]:
>
> The Standard Model gauge group **SU(3)×SU(2)×U(1)** embeds naturally in D₆ via the subalgebra chain:
> - **SU(3)**: A₂ subalgebra (color) — coordinates 1-3
> - **SU(2)**: A₁ subalgebra (weak isospin) — coordinates 4-5
> - **U(1)**: Cartan subalgebra (hypercharge)
>
> The commutation relations $[SU(3), SU(2)] = 0$ and $[SU(3), U(1)] = 0$ are **verified**.

---

## Intuition

> **In plain terms**: The D₆ lattice is like a 6-dimensional crystal with very specific symmetries. Hidden inside this crystal are smaller symmetry patterns — the A₂ triangle (which becomes SU(3) color), the A₁ line (which becomes SU(2) weak), and a single direction (which becomes U(1) hypercharge). These aren't put in by hand; they're already there in the D₆ structure. The key insight is that these subalgebras use **different coordinates** (1-3 vs 4-5), so they automatically commute.

---

## Prerequisites

- **[THEOREM II.C.1]**: D₆ is the minimal lattice for H₃ realization
- **[THEOREM III.1.1]**: D₆ shell structure (30+30)
- **[KNOWN]**: Lie algebra embedding theory

---

## D₆ Subalgebra Structure

### The D₆ Root System

The D₆ root system consists of 60 roots in ℝ⁶:
$$\Phi(D_6) = \{\pm e_i \pm e_j : 1 \le i < j \le 6\}$$

All roots have squared length $|\alpha|^2 = 2$.

### Simple Roots

A standard choice of simple roots:
- $\alpha_1 = e_1 - e_2$
- $\alpha_2 = e_2 - e_3$
- $\alpha_3 = e_3 - e_4$
- $\alpha_4 = e_4 - e_5$
- $\alpha_5 = e_5 - e_6$
- $\alpha_6 = e_5 + e_6$

The Dynkin diagram:

```
    α₁ — α₂ — α₃ — α₄ — α₅
                        |
                       α₆
```

---

## Standard Model Embedding

### SU(3) Color — The A₂ Subalgebra

The A₂ subalgebra (rank 2, 6 roots) embeds in D₆ using **coordinates 1-3**:

**Simple roots**:
$$\alpha_1^{SU3} = e_1 - e_2, \quad \alpha_2^{SU3} = e_2 - e_3$$

**All A₂ roots**:
$$\Phi(A_2) = \{\pm(e_1-e_2), \pm(e_2-e_3), \pm(e_1-e_3)\}$$

These 6 roots + 2 Cartan generators give the 8 gluons.

### SU(2) Weak — The A₁ Subalgebra

The A₁ subalgebra (rank 1, 2 roots) embeds using **coordinates 4-5**:

**Simple root**:
$$\alpha^{SU2} = e_4 - e_5$$

**All A₁ roots**:
$$\Phi(A_1) = \{\pm(e_4-e_5)\}$$

These 2 roots + 1 Cartan generator give $W^+$, $W^-$, and $W^3$.

### U(1) Hypercharge — Cartan Direction

The hypercharge generator is a direction in the Cartan subalgebra:

$$Y = \left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}, -\frac{1}{2}, -\frac{1}{2}, 0\right)$$

This is the standard SU(5) GUT normalization.

### Commutation Relations [VERIFIED]

**Delegation 22** verified:

| Check | Result | Status |
|-------|--------|--------|
| $\alpha_{SU3} \cdot \alpha_{SU2} = 0$ (all pairs) | Exactly 0 | ✅ **VERIFIED** |
| $\alpha_{SU3} \cdot Y = 0$ (all roots) | Exactly 0 | ✅ **VERIFIED** |

**Why they commute**: The A₂ roots use coordinates {1,2,3} while A₁ roots use coordinates {4,5}. These are **disjoint**, so all dot products vanish automatically.

---

## Projection to H₃: Shell Placement

### The Key Result [VERIFIED]

When the gauge generators are projected to 3D via the Koca–Al-Siyabi matrix:

| Generator | Shell | $|x_\parallel|^2$ | Physical Role |
|-----------|-------|-------------------|---------------|
| SU(3) roots (A₂) | **Outer** | $1 + \frac{\sqrt{5}}{5} \approx 1.447$ | Strong force |
| SU(2) roots (A₁) | **Inner** | $1 - \frac{\sqrt{5}}{5} \approx 0.553$ | Weak force |

**Note**: Earlier documentation had the shell labels inverted. Delegation 22 verified the correct assignment.

**Physical interpretation**: The strong force (SU(3)) projects to the **larger** shell, while the weak force (SU(2)) projects to the **smaller** shell. This has no effect on the Weinberg angle calculation, which depends only on the **ratio** of projected lengths.

### The 120° Twist [VERIFIED]

In 6D, the SU(2) and SU(3) roots are **orthogonal** (90°).

After projection to 3D:
$$\cos\theta = \frac{x_{SU2} \cdot x_{SU3}}{|x_{SU2}||x_{SU3}|} = -\frac{1}{2}$$

Therefore: $\theta = 120°$

**Delegation 22 verified**: $\cos\theta = -0.500000$ exactly.

**Physical interpretation**: The golden projection "twists" orthogonal 6D gauge directions into an A₂-like 120° configuration in 3D. This is the geometric origin of the non-trivial electroweak mixing.

---

## Comparison with GUT Embeddings

### SU(5) GUT

The Standard Model embeds in SU(5):
$$SU(5) \supset SU(3) \times SU(2) \times U(1)$$

**D₆ connection**: The SU(5) embedding uses the same A₂ + A₁ + U(1) structure that exists in D₆.

### SO(10) GUT

$$SO(10) \supset SU(5) \supset SU(3) \times SU(2) \times U(1)$$

**D₆ connection**: SO(10) = D₅, which is a subalgebra of D₆. So D₆ naturally contains the SO(10) GUT structure.

### E₆ and E₈ Approaches

| Approach | Lattice | SM Embedding | φ-Structure |
|----------|---------|--------------|-------------|
| E₈ (Lisi) | E₈ | Complex | Yes (600-cell) |
| E₆ GUT | E₆ | Standard | No known H₃ |
| **D₆** | D₆ | Standard | **Yes (H₃)** |

**D₆ advantage**: Minimal lattice with both SM embedding AND golden projection.

---

## Claim Status

| Claim | Status | Source |
|-------|--------|--------|
| A₂ ⊂ D₆ | **[KNOWN]** | Standard Lie theory |
| A₁ ⊂ D₆ | **[KNOWN]** | Standard Lie theory |
| U(1) from Cartan | **[KNOWN]** | Standard Lie theory |
| [SU(3), SU(2)] = 0 | **[VERIFIED]** | Delegation 22 |
| [SU(3), U(1)] = 0 | **[VERIFIED]** | Delegation 22 |
| SU(3) on outer shell | **[VERIFIED]** | Delegation 22 |
| SU(2) on inner shell | **[VERIFIED]** | Delegation 22 |
| 120° angle after projection | **[VERIFIED]** | Delegation 22 |

---

## Open Questions

| Question | Status | Priority |
|----------|--------|----------|
| ~~Commutation relations~~ | ✅ **VERIFIED** | — |
| ~~Shell placement~~ | ✅ **VERIFIED** | — |
| ~~120° twist~~ | ✅ **VERIFIED** | — |
| D₆ ⊃ D₅ = SO(10) explicitly | [TODO] | LOW |

---

## References

1. **Slansky, R.** (1981). "Group Theory for Unified Model Building." *Phys. Rep.* 79, 1.
2. **Delegation 22**: Gauge Commutator Verification — `Appendices/D_delegations/22_gauge_commutators/`
3. **Humphreys, J.E.** (1972). *Introduction to Lie Algebras and Representation Theory*. Springer.
4. **Koca, M. et al.** (2020). "Icosahedral Polyhedra from D₆ Lattice." *Symmetry* 12, 1983.
