# Delegation 25 - Iteration 3: Neutrino Mass Test with Brannen Phase

## 1. BACKGROUND: The Golden Selection Theory

### 1.1 The Framework

The **Golden Selection** theory proposes that the fundamental structure of physics emerges from a single principle:

> **Axiom 0 (Geometric Free Energy Principle)**: Physical structure minimizes a geometric free energy functional combining strain energy and Schur-convex curvature.

This axiom uniquely selects:
- **Dimension D = 3**: The only dimension supporting stable aperiodic order
- **Golden ratio φ = (1+√5)/2**: The unique irrational minimizing Schur-convex curvature
- **H₃ symmetry**: The maximal non-crystallographic symmetry in 3D (icosahedral)

### 1.2 The D₆ Lattice

The theory uses the **D₆ lattice** in 6 dimensions as the "parent" structure. When projected to 3D, it produces H₃ quasicrystals with golden ratio appearing throughout.

---

## 2. THE KOIDE FORMULA

### 2.1 Definition

The **Koide formula** (1983) is an empirical relation for charged lepton masses:

$$Q = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

This holds to remarkable precision (< 0.01% error).

### 2.2 Parametric Form

The Koide formula can be written as:

$$m_i = M_0 \left( 1 + \sqrt{2} \cos\left(\theta_0 + \frac{2\pi i}{3}\right) \right)^2$$

Where:
- $M_0$ = overall mass scale (determines absolute masses)
- $\theta_0$ = **Koide phase** (determines mass ratios)
- $i = 0, 1, 2$ for the three generations

### 2.3 The Singularity

The mass term $T = 1 + \sqrt{2}\cos\theta$ vanishes when:
$$\cos\theta = -\frac{1}{\sqrt{2}} \implies \theta = 135° \text{ or } 225°$$

Masses near this angle are **exponentially suppressed**.

---

## 3. THE BRANNEN PHASE BREAKTHROUGH

### 3.1 Charged Leptons: θ₀ = +2/9 rad

Carl Brannen (2006) discovered that the phase:

$$\boxed{\theta_0 = \frac{2}{9} \text{ radians} \approx 12.732°}$$

reproduces charged lepton masses **exactly**:

| Particle | Mass (MeV) | Predicted | Observed | Source |
|----------|------------|-----------|----------|--------|
| Electron | 0.511 | — | 0.51099895 | PDG 2024 |
| Muon | 105.66 | — | 105.6583755 | PDG 2024 |
| Tau | 1776.86 | — | 1776.86 | PDG 2024 |

**Mass ratios**:
| Ratio | Predicted | Observed | Error |
|-------|-----------|----------|-------|
| μ/e | 206.7703 | 206.7683 | **0.001%** |
| τ/e | 3477.4728 | 3477.2283 | **0.007%** |

### 3.2 Why Q = 2/3 (Proven)

The Koide parameter Q = 2/3 arises from the **A₂ lattice cone condition**:

1. In mass space $(\sqrt{m_e}, \sqrt{m_\mu}, \sqrt{m_\tau})$, the A₂ symmetry defines a cone around $(1,1,1)$
2. The cone angle is exactly **45°**
3. $Q = \frac{1}{3\cos^2(45°)} = \frac{1}{3 \times 1/2} = \frac{2}{3}$

### 3.3 Phase Assignment for Charged Leptons

For θ₀ = +2/9 rad ≈ +12.73°:

| Particle | Phase | Distance from 135° | T value | Result |
|----------|-------|-------------------|---------|--------|
| **τ** | 12.7° | 122.3° | 2.38 | **Large mass** |
| **μ** | 252.7° | 117.3° | 0.60 | **Medium mass** |
| **e** | 132.7° | **2.3°** | 0.003 | **Tiny mass** |

The electron is only **2.3° from the singularity**, explaining why it's so light.

---

## 4. BRANNEN'S NEUTRINO HYPOTHESIS

### 4.1 The Proposal

Brannen proposed that **neutrinos follow the same Koide formula** but with:

$$\boxed{\theta_0(\nu) = -\frac{2}{9} \text{ radians} \approx -12.732°}$$

Key differences from charged leptons:
- **Negative phase**: Sign flip (−2/9 instead of +2/9)
- **Different mass scale**: $M_0(\nu) \ll M_0(e)$
- **Same Q = 2/3**: The sum rule is preserved

### 4.2 Physical Motivation

The sign flip has geometric meaning:
- Charged leptons and neutrinos are "mirror images" on the Koide circle
- The negative phase places the **heaviest** neutrino near the singularity (opposite to charged leptons where the **lightest** is near singularity)
- This could explain the inverted hierarchy structure

### 4.3 Expected Hierarchy

For θ₀ = −2/9 rad:

| Particle | Phase | Distance from 135° | Expected |
|----------|-------|-------------------|----------|
| **ν₃** | −12.7° | 147.7° | **Heaviest** |
| **ν₂** | 107.3° | 27.7° | **Medium** |
| **ν₁** | 227.3° | 2.3° | **Lightest** (near singularity) |

---

## 5. NEUTRINO MASS DATA

### 5.1 What We Know

Neutrino oscillation experiments measure **mass-squared differences**, not absolute masses:

| Parameter | Value | Uncertainty | Source |
|-----------|-------|-------------|--------|
| Δm²₂₁ (solar) | 7.53 × 10⁻⁵ eV² | ± 0.18 × 10⁻⁵ | PDG 2024 |
| Δm²₃₁ (atm, NH) | 2.453 × 10⁻³ eV² | ± 0.033 × 10⁻³ | PDG 2024 |
| Δm²₃₂ (atm, IH) | −2.536 × 10⁻³ eV² | ± 0.034 × 10⁻³ | PDG 2024 |

Where:
- **NH** = Normal Hierarchy: m₁ < m₂ < m₃
- **IH** = Inverted Hierarchy: m₃ < m₁ < m₂

### 5.2 Cosmological Bound

$$\sum m_\nu < 0.12 \text{ eV} \quad \text{(Planck 2018, 95% CL)}$$

### 5.3 Derived Mass Ranges

**Normal Hierarchy** (assuming m₁ ≈ 0):
- m₁ ≈ 0 eV
- m₂ ≈ √(Δm²₂₁) ≈ 0.0087 eV = 8.7 meV
- m₃ ≈ √(Δm²₃₁) ≈ 0.0495 eV = 49.5 meV

**Key ratio** (from oscillation data):
$$\frac{\Delta m^2_{31}}{\Delta m^2_{21}} = \frac{2.453 \times 10^{-3}}{7.53 \times 10^{-5}} \approx 32.6$$

---

## 6. THE TEST

### Task 1: Calculate Koide Terms for θ₀ = −2/9

```python
import numpy as np

print("=" * 70)
print("NEUTRINO MASS TEST: Brannen Phase θ₀ = -2/9 rad")
print("=" * 70)

# Constants
theta_charged = 2/9  # radians (positive for charged leptons)
theta_nu = -2/9      # radians (negative for neutrinos)

print(f"\n1. PHASE PARAMETERS")
print(f"   θ₀(charged leptons) = +2/9 rad = +{np.degrees(theta_charged):.4f}°")
print(f"   θ₀(neutrinos)       = -2/9 rad = {np.degrees(theta_nu):.4f}°")

# Calculate Koide terms
def koide_terms(theta0):
    """Calculate T_i = 1 + √2·cos(θ₀ + 2πi/3) for i=0,1,2"""
    terms = []
    for i in range(3):
        phase = theta0 + 2*np.pi*i/3
        T = 1 + np.sqrt(2)*np.cos(phase)
        terms.append(T)
    return terms

T_nu = koide_terms(theta_nu)
print(f"\n2. KOIDE TERMS T = 1 + √2·cos(θ)")
for i, t in enumerate(T_nu):
    phase_deg = np.degrees(theta_nu + 2*np.pi*i/3)
    print(f"   T_{i} = {t:.6f}  (phase = {phase_deg:.2f}°)")
```

### Task 2: Calculate Mass Ratios

```python
# Mass ratios (m ~ T²)
m_ratios = [t**2 for t in T_nu]

# Sort to identify hierarchy
sorted_pairs = sorted(enumerate(m_ratios), key=lambda x: x[1])
print(f"\n3. MASS RATIOS (m ∝ T²)")
print(f"   Sorted by mass:")
for rank, (idx, m) in enumerate(sorted_pairs):
    label = ["Lightest (ν₁)", "Middle (ν₂)", "Heaviest (ν₃)"][rank]
    print(f"   {label}: T²_{idx} = {m:.6f}")

# Normalize to lightest
m_sorted = [m_ratios[i] for i, _ in sorted_pairs]
m1, m2, m3 = m_sorted

print(f"\n   Predicted ratios:")
print(f"   m₂/m₁ = {np.sqrt(m2/m1):.4f}")
print(f"   m₃/m₁ = {np.sqrt(m3/m1):.4f}")
print(f"   m₃/m₂ = {np.sqrt(m3/m2):.4f}")
```

### Task 3: Compare to Oscillation Data

```python
print(f"\n4. COMPARISON WITH OSCILLATION DATA")

# Observed mass-squared differences
dm21_sq = 7.53e-5  # eV²
dm31_sq = 2.453e-3  # eV² (Normal Hierarchy)

print(f"   Observed:")
print(f"   Δm²₂₁ = {dm21_sq:.2e} eV²")
print(f"   Δm²₃₁ = {dm31_sq:.2e} eV²")
print(f"   Δm²₃₁/Δm²₂₁ = {dm31_sq/dm21_sq:.2f}")

# From Koide: m₂²/m₁² = r₂₁, m₃²/m₁² = r₃₁
# Δm²₂₁ = m₂² - m₁² = m₁²(r₂₁ - 1)
# Δm²₃₁ = m₃² - m₁² = m₁²(r₃₁ - 1)
# Ratio: Δm²₃₁/Δm²₂₁ = (r₃₁ - 1)/(r₂₁ - 1)

r21 = m2/m1  # m₂²/m₁²
r31 = m3/m1  # m₃²/m₁²

pred_dm_ratio = (r31 - 1) / (r21 - 1)
obs_dm_ratio = dm31_sq / dm21_sq

print(f"\n   Predicted (from θ₀ = -2/9):")
print(f"   Δm²₃₁/Δm²₂₁ = {pred_dm_ratio:.2f}")
print(f"\n   Comparison:")
print(f"   Predicted: {pred_dm_ratio:.2f}")
print(f"   Observed:  {obs_dm_ratio:.2f}")
print(f"   Error: {100*abs(pred_dm_ratio - obs_dm_ratio)/obs_dm_ratio:.1f}%")
```

### Task 4: Determine Absolute Masses

```python
print(f"\n5. ABSOLUTE NEUTRINO MASSES")

# Solve for m₁ from Δm²₂₁ = m₁²(r₂₁ - 1)
if r21 > 1:
    m1_sq = dm21_sq / (r21 - 1)
    m1 = np.sqrt(m1_sq)
    m2_val = m1 * np.sqrt(r21)
    m3_val = m1 * np.sqrt(r31)
    
    print(f"   m₁ = {m1*1000:.4f} meV")
    print(f"   m₂ = {m2_val*1000:.4f} meV")
    print(f"   m₃ = {m3_val*1000:.4f} meV")
    print(f"   Σmᵢ = {(m1+m2_val+m3_val)*1000:.4f} meV = {m1+m2_val+m3_val:.4f} eV")
else:
    print("   ERROR: r₂₁ < 1, cannot solve for positive m₁²")
```

### Task 5: Check Cosmological Bound

```python
print(f"\n6. COSMOLOGICAL CHECK")
cosmo_bound = 0.12  # eV (Planck 2018)

if r21 > 1:
    sum_m = m1 + m2_val + m3_val
    print(f"   Σmᵢ = {sum_m:.4f} eV")
    print(f"   Bound: < {cosmo_bound} eV")
    print(f"   Status: {'✅ PASSES' if sum_m < cosmo_bound else '❌ FAILS'}")
```

### Task 6: Check Koide Q for Neutrinos

```python
print(f"\n7. KOIDE Q CHECK")

if r21 > 1:
    # Q = (m₁ + m₂ + m₃) / (√m₁ + √m₂ + √m₃)²
    Q = (m1 + m2_val + m3_val) / (np.sqrt(m1) + np.sqrt(m2_val) + np.sqrt(m3_val))**2
    print(f"   Q(neutrinos) = {Q:.6f}")
    print(f"   Target Q     = 0.666667")
    print(f"   Error: {100*abs(Q - 2/3)/(2/3):.4f}%")
```

### Task 7: Full Verification Code

```python
print("\n" + "=" * 70)
print("FULL VERIFICATION")
print("=" * 70)

import numpy as np

def full_neutrino_test():
    phi = (1 + np.sqrt(5)) / 2
    
    # Brannen phases
    theta_e = 2/9   # charged leptons
    theta_nu = -2/9  # neutrinos (hypothesis)
    
    # Koide formula
    def koide_masses(theta0):
        masses = []
        for i in range(3):
            T = 1 + np.sqrt(2) * np.cos(theta0 + 2*np.pi*i/3)
            masses.append(T**2)
        return sorted(masses)
    
    # Charged lepton test (known to work)
    m_e_obs = 0.51099895
    m_mu_obs = 105.6583755
    m_tau_obs = 1776.86
    
    m_charged = koide_masses(theta_e)
    scale_e = m_e_obs / m_charged[0]
    
    print("CHARGED LEPTONS (θ₀ = +2/9):")
    print(f"  Predicted μ/e = {m_charged[1]/m_charged[0]:.4f}")
    print(f"  Observed  μ/e = {m_mu_obs/m_e_obs:.4f}")
    print(f"  Predicted τ/e = {m_charged[2]/m_charged[0]:.4f}")
    print(f"  Observed  τ/e = {m_tau_obs/m_e_obs:.4f}")
    
    # Neutrino test
    m_nu = koide_masses(theta_nu)
    
    print("\nNEUTRINOS (θ₀ = -2/9):")
    print(f"  m₂/m₁ predicted = {np.sqrt(m_nu[1]/m_nu[0]):.4f}")
    print(f"  m₃/m₁ predicted = {np.sqrt(m_nu[2]/m_nu[0]):.4f}")
    
    # Compare to oscillation data
    dm21 = 7.53e-5
    dm31 = 2.453e-3
    
    r21 = m_nu[1]/m_nu[0]
    r31 = m_nu[2]/m_nu[0]
    
    pred_ratio = (r31 - 1)/(r21 - 1)
    obs_ratio = dm31/dm21
    
    print(f"\n  Δm²₃₁/Δm²₂₁:")
    print(f"    Predicted = {pred_ratio:.2f}")
    print(f"    Observed  = {obs_ratio:.2f}")
    print(f"    Error     = {100*abs(pred_ratio-obs_ratio)/obs_ratio:.1f}%")
    
    # Absolute masses
    if r21 > 1:
        m1 = np.sqrt(dm21/(r21-1))
        m2 = m1 * np.sqrt(r21)
        m3 = m1 * np.sqrt(r31)
        
        print(f"\n  Absolute masses:")
        print(f"    m₁ = {m1*1000:.2f} meV")
        print(f"    m₂ = {m2*1000:.2f} meV")
        print(f"    m₃ = {m3*1000:.2f} meV")
        print(f"    Σm = {(m1+m2+m3)*1000:.2f} meV")
        
        # Koide Q
        Q = (m1+m2+m3)/(np.sqrt(m1)+np.sqrt(m2)+np.sqrt(m3))**2
        print(f"\n  Koide Q = {Q:.6f} (target: 0.666667)")

full_neutrino_test()
```

---

## 7. EXPECTED OUTCOMES

### Scenario A: Perfect Match

If Δm²₃₁/Δm²₂₁ ≈ 32.6 is reproduced:
- **Neutrinos follow the same Koide geometry as charged leptons**
- The sign flip (±2/9) distinguishes charged/neutral leptons
- The theory predicts absolute neutrino masses
- **Major confirmation of the Brannen hypothesis**

### Scenario B: Wrong Ratio but Q = 2/3

If Q = 2/3 holds but the mass-squared ratio is wrong:
- Neutrinos are on the Koide circle but at a **different phase**
- Need to find θ₀(ν) that fits oscillation data
- The ±2/9 symmetry is broken

### Scenario C: Neither Works

If neither Q = 2/3 nor the ratios match:
- Neutrino masses have a **different origin**
- May require Majorana mass terms
- May require seesaw mechanism
- The Koide formula may not apply to neutrinos

---

## 8. DELIVERABLES

1. **Koide terms** T₀, T₁, T₂ for θ₀ = −2/9 rad
2. **Predicted mass ratios** m₃/m₂, m₂/m₁
3. **Comparison** to oscillation data Δm²₃₁/Δm²₂₁
4. **Absolute masses** m₁, m₂, m₃ (if consistent)
5. **Koide Q** for neutrinos
6. **Cosmological bound** check (Σm < 0.12 eV)
7. **Verdict**: Does θ₀(ν) = −2/9 work for neutrinos?

---

## 9. REFERENCES

1. **Koide, Y.** (1983). "A Fermion-Boson Composite Model of Quarks and Leptons." *Phys. Lett. B* 120, 161-165.

2. **Brannen, C.** (2006). "The Lepton Masses." *Preprint*. [First identification of θ₀ = 2/9]

3. **PDG** (2024). "Review of Particle Physics." *Phys. Rev. D* 110, 030001. [Neutrino oscillation parameters]

4. **Planck Collaboration** (2018). "Planck 2018 results. VI. Cosmological parameters." *A&A* 641, A6. [Cosmological neutrino mass bound]

5. **Foot, R.** (1994). "A note on Koide's lepton mass relation." *arXiv:hep-ph/9402242*.
