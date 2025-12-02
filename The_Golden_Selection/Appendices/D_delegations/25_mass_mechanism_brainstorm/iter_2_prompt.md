# Delegation 25 - Iteration 2: Laplacian Eigenvalues on Occupation Domains

## 1. CONTEXT FROM ITERATION 1

### 1.1 What We Established

**Confirmed**:
- Q = 2/3 is **geometrically enforced** by the A₂ sublattice structure in D₆
- The Koide formula's 120° spacing comes from A₂ root geometry

**Falsified**:
- θ₀ = arctan(φ⁻³) exactly (off by 0.55°, fatal for electron mass)
- Direct volume scaling: √m ∝ 1/V (gives wrong ratios)

**New Hypothesis**:
Mass is proportional to the **first Laplacian eigenvalue** on the occupation domain:
$$m_n \propto \lambda_1(\text{Domain}_n)$$

### 1.2 Why This Makes Sense

In spectral geometry ("hearing the shape of a drum"):
- **Smaller domain** → **Higher fundamental frequency** → **Larger eigenvalue**
- **Larger domain** → **Lower fundamental frequency** → **Smaller eigenvalue**

This naturally gives:
- Core (smallest, C) → Highest eigenvalue → **τ** (heaviest)
- Shell (middle, B) → Middle eigenvalue → **μ** (middle)
- Skin (largest, A) → Lowest eigenvalue → **e** (lightest)

---

## 2. THE OCCUPATION DOMAINS

### 2.1 Definition

When the D₆ lattice is projected to 3D via the Koca–Al-Siyabi projection, the "acceptance window" in internal space (E⊥) is a **rhombic triacontahedron** (30-faced polyhedron with icosahedral symmetry).

This window stratifies into **three nested regions** called **occupation domains**:

| Domain | Name | Position in E⊥ | Physical Role |
|--------|------|----------------|---------------|
| **C** | Core | Center (deep) | τ, t, b (Gen 3) |
| **B** | Shell | Middle | μ, c, s (Gen 2) |
| **A** | Skin | Outer (boundary) | e, u, d (Gen 1) |

### 2.2 Window Volumes (from Baake & Grimm)

The volumes are given by explicit formulas involving τ = φ (golden ratio):

| Domain | Volume Formula | Numerical Value |
|--------|----------------|-----------------|
| **A** (Skin) | V_A = 20(4-τ) | ≈ 47.64 |
| **B** (Shell) | V_B = 4(τ+2) | ≈ 14.47 |
| **C** (Core) | V_C = 20(τ-1) | ≈ 12.36 |

Where τ = φ = (1+√5)/2 ≈ 1.618.

**Note**: These are the volumes of the **windows** in E⊥, not physical 3D volumes.

### 2.3 Domain Shapes

The three domains are **nested icosahedral shells** in E⊥:

- **Core (C)**: A small icosahedral region at the center
- **Shell (B)**: A middle layer surrounding the core
- **Skin (A)**: The outer layer extending to the boundary

The boundary of the full window is a **rhombic triacontahedron** (dual of icosidodecahedron).

---

## 3. THE LAPLACIAN EIGENVALUE PROBLEM

### 3.1 The Setup

For a bounded domain Ω in ℝ³ (or ℝⁿ), the **Dirichlet Laplacian eigenvalue problem** is:

$$-\nabla^2 \psi = \lambda \psi \quad \text{in } \Omega$$
$$\psi = 0 \quad \text{on } \partial\Omega$$

The **first (smallest) eigenvalue** λ₁ is called the **fundamental frequency**.

### 3.2 Weyl's Law

For large eigenvalues, Weyl's law gives:

$$\lambda_n \sim C_d \left(\frac{n}{V}\right)^{2/d}$$

Where:
- d = dimension
- V = volume of domain
- C_d = dimension-dependent constant

For the **first eigenvalue** specifically:

$$\lambda_1 \propto \frac{1}{V^{2/d}}$$

In 3D (d=3): λ₁ ∝ V^{-2/3}

### 3.3 Faber-Krahn Inequality

Among all domains of fixed volume, the **ball** has the smallest first eigenvalue. This gives a lower bound:

$$\lambda_1 \geq \frac{j_{d/2-1,1}^2}{R^2}$$

Where j is a Bessel function zero and R is the radius of a ball with the same volume.

### 3.4 Shape Dependence

The first eigenvalue depends on both **volume** and **shape**:
- More "elongated" shapes have higher λ₁
- More "spherical" shapes have lower λ₁

For icosahedral domains, the shape factor should be similar across all three domains (they're all icosahedral shells).

---

## 4. THE CALCULATION

### 4.1 Simple Estimate (Volume Scaling)

If we ignore shape effects and use λ₁ ∝ V^{-2/3}:

| Domain | Volume | V^{-2/3} | Normalized |
|--------|--------|----------|------------|
| **C** (Core) | 12.36 | 0.188 | 1.000 |
| **B** (Shell) | 14.47 | 0.168 | 0.894 |
| **A** (Skin) | 47.64 | 0.076 | 0.404 |

**Predicted ratios** (if m ∝ λ₁ ∝ V^{-2/3}):
- m_τ / m_μ ≈ 1.00 / 0.894 = 1.12
- m_μ / m_e ≈ 0.894 / 0.404 = 2.21
- m_τ / m_e ≈ 1.00 / 0.404 = 2.48

**Observed ratios**:
- m_τ / m_μ = 16.8
- m_μ / m_e = 206.8
- m_τ / m_e = 3477

**Result**: Simple V^{-2/3} scaling is **way off** (factor of 15-1400).

### 4.2 What's Missing?

The simple estimate fails because:

1. **The domains are not separate balls** — they're nested shells
2. **The eigenvalue problem should be on shells**, not solid regions
3. **The internal space E⊥ is 3D**, but the physics may involve different boundary conditions

### 4.3 Shell Eigenvalues

For a **spherical shell** (annulus in 3D) with inner radius r₁ and outer radius r₂, the first eigenvalue is approximately:

$$\lambda_1 \approx \frac{\pi^2}{(r_2 - r_1)^2}$$

The eigenvalue depends on the **thickness** of the shell, not just the volume.

---

## 5. TASKS

### Task 1: Compute Shell Radii

From the window volumes, estimate the radii of the three domains:

**Assuming icosahedral shape** (volume ∝ r³):

| Domain | Volume | Estimated Radius |
|--------|--------|------------------|
| **C** (Core) | 12.36 | r_C ≈ ? |
| **B** (Shell) | 14.47 | r_B ≈ ? |
| **A** (Skin) | 47.64 | r_A ≈ ? |

**Note**: The Shell and Skin are **annular regions**, so we need:
- Core: 0 < r < r_C
- Shell: r_C < r < r_B
- Skin: r_B < r < r_A

### Task 2: Compute Shell Eigenvalues

For each shell, compute the first Dirichlet eigenvalue:

1. **Core** (solid icosahedron): λ₁(Core)
2. **Shell** (icosahedral annulus): λ₁(Shell)
3. **Skin** (icosahedral annulus): λ₁(Skin)

### Task 3: Compare to Lepton Masses

Check if the eigenvalue ratios match:

| Ratio | Eigenvalue Prediction | Observed |
|-------|----------------------|----------|
| λ_C / λ_B | ? | m_τ/m_μ = 16.8 |
| λ_B / λ_A | ? | m_μ/m_e = 206.8 |
| λ_C / λ_A | ? | m_τ/m_e = 3477 |

### Task 4: Check Koide Q

If masses are proportional to eigenvalues, does the resulting distribution satisfy Q = 2/3?

$$Q = \frac{\lambda_A + \lambda_B + \lambda_C}{(\sqrt{\lambda_A} + \sqrt{\lambda_B} + \sqrt{\lambda_C})^2} \stackrel{?}{=} \frac{2}{3}$$

### Task 5: Alternative: Neumann Boundary Conditions

The Dirichlet condition (ψ = 0 on boundary) may not be physical. Try:

1. **Neumann** (∂ψ/∂n = 0): "Reflecting" boundary
2. **Periodic**: Wrap-around conditions
3. **Mixed**: Different conditions on inner/outer boundaries

---

## 6. VERIFICATION CODE

```python
import numpy as np
from scipy.special import jn_zeros

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Window volumes (from Baake & Grimm)
V_A = 20 * (4 - phi)  # Skin
V_B = 4 * (phi + 2)   # Shell
V_C = 20 * (phi - 1)  # Core

print("=" * 70)
print("LAPLACIAN EIGENVALUE ANALYSIS")
print("=" * 70)

print("\n1. WINDOW VOLUMES")
print(f"   V_A (Skin)  = {V_A:.4f}")
print(f"   V_B (Shell) = {V_B:.4f}")
print(f"   V_C (Core)  = {V_C:.4f}")
print(f"   Total = {V_A + V_B + V_C:.4f}")

# Observed lepton masses
m_e = 0.511
m_mu = 105.66
m_tau = 1776.86

print("\n2. OBSERVED MASS RATIOS")
print(f"   m_τ/m_μ = {m_tau/m_mu:.2f}")
print(f"   m_μ/m_e = {m_mu/m_e:.2f}")
print(f"   m_τ/m_e = {m_tau/m_e:.2f}")

# Simple volume scaling: λ ∝ V^{-2/3}
print("\n3. SIMPLE VOLUME SCALING (λ ∝ V^{-2/3})")
lambda_A = V_A**(-2/3)
lambda_B = V_B**(-2/3)
lambda_C = V_C**(-2/3)

# Normalize to Core
lambda_A_norm = lambda_A / lambda_C
lambda_B_norm = lambda_B / lambda_C
lambda_C_norm = 1.0

print(f"   λ_A (Skin)  = {lambda_A_norm:.4f}")
print(f"   λ_B (Shell) = {lambda_B_norm:.4f}")
print(f"   λ_C (Core)  = {lambda_C_norm:.4f}")

print("\n   Predicted ratios (if m ∝ λ):")
print(f"   m_τ/m_μ ≈ {lambda_C_norm/lambda_B_norm:.2f} (observed: {m_tau/m_mu:.2f})")
print(f"   m_μ/m_e ≈ {lambda_B_norm/lambda_A_norm:.2f} (observed: {m_mu/m_e:.2f})")
print(f"   m_τ/m_e ≈ {lambda_C_norm/lambda_A_norm:.2f} (observed: {m_tau/m_e:.2f})")

# Estimate radii (assuming icosahedral ≈ spherical for volume)
# V = (4/3)πr³ → r = (3V/4π)^{1/3}
def radius_from_volume(V):
    return (3 * V / (4 * np.pi))**(1/3)

r_total = radius_from_volume(V_A + V_B + V_C)
r_BC = radius_from_volume(V_B + V_C)  # Inner boundary of Skin
r_C = radius_from_volume(V_C)         # Inner boundary of Shell

print("\n4. ESTIMATED RADII (spherical approximation)")
print(f"   r_C (Core outer) = {r_C:.4f}")
print(f"   r_BC (Shell outer) = {r_BC:.4f}")
print(f"   r_total (Skin outer) = {r_total:.4f}")

# Shell thicknesses
t_C = r_C                    # Core: 0 to r_C
t_B = r_BC - r_C             # Shell: r_C to r_BC
t_A = r_total - r_BC         # Skin: r_BC to r_total

print(f"\n   Thicknesses:")
print(f"   t_C (Core)  = {t_C:.4f}")
print(f"   t_B (Shell) = {t_B:.4f}")
print(f"   t_A (Skin)  = {t_A:.4f}")

# Shell eigenvalue approximation: λ ∝ 1/t²
print("\n5. SHELL EIGENVALUE SCALING (λ ∝ 1/t²)")
lambda_A_shell = 1 / t_A**2
lambda_B_shell = 1 / t_B**2
lambda_C_shell = 1 / t_C**2

# Normalize
lambda_A_shell_norm = lambda_A_shell / lambda_C_shell
lambda_B_shell_norm = lambda_B_shell / lambda_C_shell
lambda_C_shell_norm = 1.0

print(f"   λ_A (Skin)  = {lambda_A_shell_norm:.4f}")
print(f"   λ_B (Shell) = {lambda_B_shell_norm:.4f}")
print(f"   λ_C (Core)  = {lambda_C_shell_norm:.4f}")

print("\n   Predicted ratios (if m ∝ 1/t²):")
print(f"   m_τ/m_μ ≈ {lambda_C_shell_norm/lambda_B_shell_norm:.2f} (observed: {m_tau/m_mu:.2f})")
print(f"   m_μ/m_e ≈ {lambda_B_shell_norm/lambda_A_shell_norm:.2f} (observed: {m_mu/m_e:.2f})")
print(f"   m_τ/m_e ≈ {lambda_C_shell_norm/lambda_A_shell_norm:.2f} (observed: {m_tau/m_e:.2f})")

# Check Koide Q for both scalings
print("\n6. KOIDE Q CHECK")

def koide_Q(m1, m2, m3):
    return (m1 + m2 + m3) / (np.sqrt(m1) + np.sqrt(m2) + np.sqrt(m3))**2

# Using volume scaling
Q_vol = koide_Q(lambda_A_norm, lambda_B_norm, lambda_C_norm)
print(f"   Q (volume scaling) = {Q_vol:.4f}")

# Using shell scaling
Q_shell = koide_Q(lambda_A_shell_norm, lambda_B_shell_norm, lambda_C_shell_norm)
print(f"   Q (shell scaling)  = {Q_shell:.4f}")

# Observed
Q_obs = koide_Q(m_e, m_mu, m_tau)
print(f"   Q (observed)       = {Q_obs:.4f}")
print(f"   Target Q           = 0.6667")

print("\n" + "=" * 70)
print("VERDICT")
print("=" * 70)
```

---

## 7. EXPECTED OUTCOMES

### Scenario A: Eigenvalues Match
If λ_C : λ_B : λ_A ≈ 3477 : 207 : 1, then:
- **Mass = Laplacian eigenvalue** is confirmed
- The mechanism is purely spectral geometry

### Scenario B: Eigenvalues Give Q = 2/3 but Wrong Ratios
If Q ≈ 2/3 but ratios are wrong:
- The Koide constraint is separate from the eigenvalue mechanism
- Need to combine eigenvalues with Koide phase

### Scenario C: Neither Works
If eigenvalues don't match masses or Q:
- The mass mechanism is more complex
- May need to consider eigenvector structure, not just eigenvalues

---

## 8. DELIVERABLES

1. **Shell radii** computed from window volumes
2. **Eigenvalue estimates** for each domain
3. **Comparison** to observed mass ratios
4. **Koide Q** for the eigenvalue distribution
5. **Assessment** of whether spectral geometry explains masses

---

## 9. REFERENCES

1. **Weyl, H.** (1911). "Über die asymptotische Verteilung der Eigenwerte." *Nachr. Königl. Ges. Wiss. Göttingen*.

2. **Faber, G.** (1923). "Beweis, dass unter allen homogenen Membranen von gleicher Fläche und gleicher Spannung die kreisförmige den tiefsten Grundton gibt."

3. **Baake, M. & Grimm, U.** (2013). "Aperiodic Order, Vol. 1." Cambridge University Press.

4. **Kac, M.** (1966). "Can One Hear the Shape of a Drum?" *American Mathematical Monthly* 73, 1-23.

