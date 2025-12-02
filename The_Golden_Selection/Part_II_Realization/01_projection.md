# II.A — The Cut-and-Project Method

## Statement

> **THEOREM II.A.1 (Cut-and-Project Description)** [KNOWN]:
>
> Under standard assumptions of finite local complexity and repetitivity, quasicrystals with sharp diffraction patterns (pure point spectrum) are accurately described as **model sets** constructed by the cut-and-project method from a higher-dimensional periodic lattice.

---

## Intuition

> **In plain terms**: You can't build a perfect quasicrystal by placing tiles one at a time in 3D — the non-local correlations would require infinite lookahead. But from 6D, the correlations are just "local" — you're slicing a periodic structure.

---

## Prerequisites

- **[KNOWN]**: De Bruijn (1981) — Penrose tilings as projections
- **[KNOWN]**: Meyer (1972) — Model sets and diffraction

---

## The Method

### Definition: Cut-and-Project Set

A **model set** (cut-and-project quasicrystal) is defined by:

1. **Superspace**: $\mathbb{R}^n = E_\parallel \oplus E_\perp$
   - $E_\parallel$: Physical space (dimension $d$)
   - $E_\perp$: Internal/perpendicular space (dimension $n-d$)

2. **Lattice**: $\mathcal{L} \subset \mathbb{R}^n$ (periodic)

3. **Acceptance Window**: $W \subset E_\perp$ (bounded region)

4. **Projection**: 
   $$\Lambda = \{ \pi_\parallel(x) : x \in \mathcal{L}, \, \pi_\perp(x) \in W \}$$

### Visualization

```
6D Superspace (periodic lattice)
        ↓ project onto E_∥
3D Physical Space (aperiodic slice)

The "acceptance window" W filters which points appear.
```

---

## Why This Works

### Property 1: Long-range order from periodicity

The lattice $\mathcal{L}$ is periodic → the projection inherits long-range correlations.

### Property 2: Aperiodicity from irrationality

If $E_\parallel$ and $E_\perp$ are **irrationally oriented** relative to $\mathcal{L}$, the projection is aperiodic.

### Property 3: Sharp diffraction

Model sets have **pure point diffraction spectra** — discrete Bragg peaks, not diffuse scattering.

---

## Application to H₃ Quasicrystals

For icosahedral (H₃) quasicrystals:
- **Superspace dimension**: $n = 6$
- **Physical space**: $d = 3$
- **Internal space**: $n - d = 3$
- **Lattice**: **D₆** (minimal root lattice with algebraic φ)
- **Projection**: Golden (H₃-invariant)

The **3+3 split** is natural:
- 3D physical space ($E_\parallel$)
- 3D phason space ($E_\perp$) — corresponds to internal degrees of freedom

---

## Connection to FEP

In the Geometric Free Energy Principle:
- **Environment**: The 6D lattice (hidden causes)
- **System**: The 3D slice (internal model)
- **Markov Blanket**: The acceptance window $W$

The window $W$ literally **filters** which lattice points become "real" in 3D — it IS the Markov blanket.

---

## Claim Status

| Claim | Status | Source |
|-------|--------|--------|
| Cut-and-project produces quasicrystals | [KNOWN] | De Bruijn (1981) |
| Pure point spectrum from model sets | [KNOWN] | Meyer (1972) |
| H₃ requires 6D superspace | [KNOWN] | Duneau-Katz (1985) |

---

## References

1. **de Bruijn, N.G.** (1981). "Algebraic theory of Penrose's non-periodic tilings." *Proc. Kon. Ned. Akad. Wet.* A84, 39-66.
2. **Meyer, Y.** (1972). *Algebraic Numbers and Harmonic Analysis*. North-Holland.
3. **Duneau, M. & Katz, A.** (1985). "Quasiperiodic patterns." *Phys. Rev. Lett.* 54, 2688.

