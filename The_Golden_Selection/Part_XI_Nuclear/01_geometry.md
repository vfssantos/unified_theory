# XI.1 Geometry: The Nuclear Cluster

## Overview

A nucleus of mass number $A$ corresponds to filling the $A$ lowest-energy single-particle states on a finite subset of the D₆ lattice.

---

## XI.1.1 Cluster Definition

The cluster nodes are defined by two cuts in 6D space:

$$C_K = \{ \alpha \in D_6 \mid P_\perp(\alpha) \in W_{\text{RT}} \land \|P_\parallel(\alpha)\| \le R(A) \}$$

| Cut | Condition | Physical Meaning |
|-----|-----------|------------------|
| **Internal** | $P_\perp \in W_{\text{RT}}$ | Node lies within Rhombic Triacontahedron acceptance window |
| **Physical** | $\|P_\parallel\| \le R(A)$ | Node lies within radius $R(A) = r_0 A^{1/3}$ |

**Interpretation**:
1. The **internal cut** ensures the cluster is a valid patch of the H₃ quasicrystal
2. The **physical cut** truncates the infinite lattice to a finite droplet

---

## XI.1.2 Shell Structure

The cluster grows in discrete geometric shells defined by the golden ratio $\varphi$:

| Shell | Geometry | Radius | Vertices |
|-------|----------|--------|----------|
| **1** | Icosidodecahedron | $r \approx 0.74$ | 30 |
| **2** | Icosidodecahedron | $r \approx 1.20$ | 30 |
| **3** | Rhombic Hexecontahedron-like | $r \approx 1.90$ | 60 |

*Note*: These shells are the finite analogs of the H₃ shell structure described in Part III. Radii are in units of D₆ root length $/\sqrt{2}$.

**Key property**: The radius ratio between successive shells is $\varphi$:

$$\frac{R_2}{R_1} = \frac{1.20}{0.74} \approx \varphi$$

---

## XI.1.3 Connection to Part III

The nuclear cluster $C_K$ is a **finite truncation** of the infinite H₃ quasicrystal:

| Part III (Infinite) | Part XI (Finite) |
|---------------------|------------------|
| Infinite D₆ → H₃ projection | Finite cluster $C_K$ |
| Shell structure continues indefinitely | Truncated at radius $R(A)$ |
| Translation symmetry (quasiperiodic) | Only point group symmetry |
| Bulk-dominated | Boundary effects important |

The boundary effects — coordination deficit, strain gradients — become the **physical mechanisms** for magic numbers beyond 20.

---

## XI.1.4 Cluster Size Examples

| Nucleus | A | Approximate $N$ (nodes) | Orbital Shells Filled |
|---------|---|-------------------------|------------------------|
| ⁴He | 4 | ~6 | Partial (1s) |
| ¹⁶O | 16 | ~20 | 1s + 1p (magic 8×2) |
| ⁴⁰Ca | 40 | ~50 | Through 1d/2s (magic 20×2) |
| ²⁰⁸Pb | 208 | ~120 | Through major shells |

*Note*: "Orbital shells" (s, p, d, f...) refer to quantum eigenstates of the Hamiltonian, not the geometric coordination shells defined in XI.1.2. The geometric shells provide the *arena*; the orbital shells are the *eigenmodes*.

---

## Summary

The nuclear cluster $C_K$ is defined by:
1. **Internal acceptance**: $P_\perp(\alpha) \in W_{\text{RT}}$ (valid quasicrystal patch)
2. **Physical truncation**: $\|P_\parallel(\alpha)\| \le R(A)$ (finite droplet)
3. **Shell structure**: Icosahedral shells at radii scaling by $\varphi$

This geometry provides the arena for the effective Hamiltonian in XI.2.
