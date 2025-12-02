# 02_projections — Golden Projection Matrices

## Overview

This folder contains the implementation and verification of the D₆ → H₃ projection that realizes the Golden Selection theory's geometric foundation.

---

## Key Result

The D₆ → H₃ projection matrix (Koca–Al-Siyabi form):

$$P_{D_6 \to H_3} = \frac{1}{\sqrt{5+\sqrt{5}}} \begin{pmatrix} 1 & -1 & 0 & 0 & \tau & -\tau \\ \tau & \tau & 1 & 1 & 0 & 0 \\ 0 & 0 & \tau & -\tau & 1 & 1 \end{pmatrix}$$

where $\tau = \phi = \frac{1+\sqrt{5}}{2}$ (Golden Ratio).

---

## Verified Properties

| Property | Value | Status |
|----------|-------|--------|
| Matrix orthonormality | Rows orthonormal | ✅ |
| D₆ roots (60 total) | Project to 2 shells | ✅ |
| Shell structure | 30 inner + 30 outer | ✅ |
| Shell geometry | Both icosidodecahedra | ✅ |
| Radius ratio | $r_{out}/r_{in} = \phi$ | ✅ |
| φ as eigenvalue | Emerges from projection | ✅ |

---

## Weinberg Angle Derivation

Using the same SU(5) embedding as E₈ (truncated to 6D):

| Generator | 6D Vector | |x|² (projected) |
|-----------|-----------|------------------|
| SU(2)_L | (0,0,0,1,-1,0) | $1 + \frac{\sqrt{5}}{5}$ |
| SU(3)_c | (1,-1,0,0,0,0) | $1 - \frac{\sqrt{5}}{5}$ |
| U(1)_Y | normalized hypercharge | $1 - \frac{3\sqrt{5}}{25}$ |

**Result:**

$$\sin^2\theta_W = \frac{393 - 75\sqrt{5}}{968} \approx 0.2327$$

This is **identical** to the E₈ derivation. The formula comes from golden icosahedral geometry + SU(5) normalization, not from E₈'s exceptional status.

---

## Files

| File | Purpose | Status |
|------|---------|--------|
| `d6_to_h3_projection.py` | Main implementation | ✅ Complete |
| `README.md` | This documentation | ✅ Complete |

---

## Usage

```bash
cd Appendices/B_calculations/02_projections
python d6_to_h3_projection.py
```

Output includes verification of:
1. Projection matrix orthonormality
2. Shell structure (30 + 30 icosidodecahedra)
3. Golden ratio in radius ratio
4. Weinberg angle calculation
5. 120° angle between SU(2) and SU(3) in 3D (A₂ geometry)

---

## References

1. **Al-Siyabi, Koca, Koca** (2020). "Icosahedral Polyhedra from D₆ Lattice and Danzer's ABCK Tiling." *MDPI Symmetry* 12, 1983.

2. **King, R.B.** (2004). "Regular Polytopes, Root Lattices, and Quasicrystals." *Croat. Chem. Acta* 77, 447-462.

3. **Delegation 08**: E₆ Alternative — Proves D₆ and E₈ give identical Weinberg angle.

4. **Delegation 10**: D₆ Shell Structure — Detailed shell analysis.

---

## Key Insight

> **D₆ is sufficient.** The Weinberg angle prediction comes from the golden icosahedral geometry (H₃) and SU(5) hypercharge normalization, not from E₈'s 8 dimensions or exceptional status. D₆ is the **minimal** lattice that realizes this structure.

