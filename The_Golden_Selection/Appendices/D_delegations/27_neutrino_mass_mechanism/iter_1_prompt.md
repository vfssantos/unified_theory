# Delegation 27 - Iteration 1: Neutrino Mass Mechanism Brainstorm

## 1. BACKGROUND: The Golden Selection Theory

### 1.1 The Framework

The **Golden Selection** theory proposes that physical structure emerges from:

> **Axiom 0 (Geometric Free Energy Principle)**: Physical structure minimizes a geometric free energy functional combining strain energy and Schur-convex curvature.

This uniquely selects:
- **Dimension D = 3**: Stable aperiodic order
- **Golden ratio φ = (1+√5)/2**: Schur-convexity minimum
- **H₃ symmetry**: Maximal non-crystallographic symmetry in 3D

### 1.2 The D₆ Lattice

The theory uses the **D₆ lattice** (6D) which projects to H₃ quasicrystals. Key structures:
- 60 roots (ω₂ orbit) → Gauge bosons
- 32+32 spinor weights (ω₅, ω₆) → Fermions
- A₂ sublattices → Mass geometry

### 1.3 Charged Lepton Success

For charged leptons (e, μ, τ), the theory achieves **< 0.01% accuracy**:

| Parameter | Origin | Value | Status |
|-----------|--------|-------|--------|
| **Q** | A₂ cone condition | 2/3 | ✅ PROVEN |
| **θ₀** | Q/3 identity | 2/9 rad | ✅ DERIVED |
| **μ/e** | Koide formula | 206.77 | ✅ EXACT |
| **τ/e** | Koide formula | 3477.47 | ✅ EXACT |

---

## 2. THE KOIDE FORMULA

### 2.1 Definition

The Koide formula parametrizes three masses:

$$m_i = M_0 \left( 1 + \sqrt{2} \cos\left(\theta_0 + \frac{2\pi i}{3}\right) \right)^2$$

The **Koide parameter**:
$$Q = \frac{m_1 + m_2 + m_3}{(\sqrt{m_1} + \sqrt{m_2} + \sqrt{m_3})^2}$$

### 2.2 Generalized Form

More generally, with amplitude ε:
$$m_i = M_0 \left( 1 + \varepsilon \cos\left(\theta_0 + \frac{2\pi i}{3}\right) \right)^2$$

The Q parameter becomes:
$$Q = \frac{1}{3} + \frac{\varepsilon^2}{6}$$

| ε Value | Q Value | Regime |
|---------|---------|--------|
| 0 | 1/3 | Perfect degeneracy (m₁ = m₂ = m₃) |
| √2 | 2/3 | Standard Koide (charged leptons) |
| √6 | 4/3 | Maximum hierarchy |

### 2.3 The Singularity

The mass term T = 1 + ε·cos(θ) vanishes when:
$$\cos\theta = -\frac{1}{\varepsilon}$$

For ε = √2: singularity at θ = 135° (or 225°)

---

## 3. WHAT WE WANT

### 3.1 Target: Neutrino Observables

From oscillation experiments (PDG 2024):

| Parameter | Value | Uncertainty |
|-----------|-------|-------------|
| Δm²₂₁ (solar) | 7.53 × 10⁻⁵ eV² | ± 0.18 × 10⁻⁵ |
| Δm²₃₁ (atm, NH) | 2.453 × 10⁻³ eV² | ± 0.033 × 10⁻³ |
| Δm²₃₁/Δm²₂₁ | **32.6** | — |
| sin²θ₁₂ | 0.307 | ± 0.013 |
| sin²θ₂₃ | 0.546 | ± 0.021 |
| sin²θ₁₃ | 0.0220 | ± 0.0007 |

**Cosmological bound**: Σm_ν < 0.12 eV (Planck 2018)

### 3.2 What We Need to Explain

1. **Mass ratio**: Δm²₃₁/Δm²₂₁ ≈ 32.6 (weak hierarchy)
2. **Near-degeneracy**: m₂/m₃ ~ 0.17 (not 0.006 like μ/τ)
3. **Absolute scale**: Σm < 0.12 eV
4. **Mixing angles**: Large θ₁₂, θ₂₃; small θ₁₃

---

## 4. WHAT WE HAVE (FAILED ATTEMPTS)

### 4.1 Direct Koide (θ = -2/9) — FAILED

**Hypothesis**: Neutrinos follow Koide with negative phase.

**Result**:
```
Predicted Δm²₃₁/Δm²₂₁ = 16.89
Observed Δm²₃₁/Δm²₂₁ = 32.58
Error: 48%
```

**Problem**: Produces hierarchy 1:200:3500, need ~1:6:30.

### 4.2 Inverse Koide (Seesaw) — FAILED

**Hypothesis**: Heavy Majorana neutrinos follow Koide, light neutrinos are inverse.

**Result**: Same hierarchy problem. Best-fit phase θ ≈ -5.7° has no geometric meaning.

### 4.3 Q = 2/3 at Any Phase — IMPOSSIBLE

Even at the most degenerate point (θ = 0) of the Q = 2/3 cone:
```
Predicted ratio: 3.4 × 10¹⁷
Observed ratio: 32.6
```

**Conclusion**: Neutrinos **cannot** reside on the Q = 2/3 cone.

---

## 5. THE GAPS

### 5.1 Critical Gaps

| Gap | Impact | Priority |
|-----|--------|----------|
| Why Q ≠ 2/3 for neutrinos? | Breaks unified Koide picture | CRITICAL |
| What determines Q for neutrals? | Needed for prediction | CRITICAL |
| What is the neutrino phase θ_ν? | Needed for mass ratios | HIGH |
| Why charged ≠ neutral? | Theoretical coherence | HIGH |

### 5.2 The Core Problem

**Charged leptons**: Q = 2/3 (Edge of A₂ cone, near singularity)
**Neutrinos**: Q ≈ 1/3 (Center of A₂ cone, near degeneracy)

Why does electric charge determine position on the Koide cone?

---

## 6. CANDIDATE MECHANISMS

### Candidate A: The Q = 1/3 Regime (Center Hypothesis)

**Idea**: Neutrinos inhabit the **center** of the A₂ projection where masses are degenerate.

**Mechanism**:
- Q = 1/3 corresponds to ε = 0 (perfect degeneracy)
- Small perturbation (ε << 1) creates small splitting
- The "perturbation" could be θ₁₃ or another small parameter

**Prediction**: 
$$Q_\nu = \frac{1}{3} + \delta \quad \text{where } \delta \ll \frac{1}{3}$$

**Test**: What ε reproduces Δm²₃₁/Δm²₂₁ = 32.6?

**Pros**: 
- Naturally explains near-degeneracy
- Q = 1/3 is a geometric fixed point (center)

**Cons**:
- Why center for neutrals, edge for charged?
- No clear derivation of ε

---

### Candidate B: θ₁₃ as Neutrino Phase

**Idea**: The reactor angle θ₁₃ ≈ 8.5° is the "Koide phase" for neutrinos.

**Mechanism**:
- θ₁₃ = 0 → Perfect TBM → Perfect degeneracy
- θ₁₃ ≠ 0 → TBM deviation → Mass splitting

**Prediction**:
$$\theta_\nu = \theta_{13} \approx 0.15 \text{ rad} \approx 8.5°$$

**Test**: Does θ = 0.15 rad with small ε reproduce the data?

**Pros**:
- Connects mass and mixing
- θ₁₃ is the "symmetry-breaking" parameter in TBM

**Cons**:
- θ₁₃ is a mixing angle, not a mass phase
- Relationship is unclear

---

### Candidate C: Tribimaximal (TBM) Structure

**Idea**: Neutrino masses follow TBM geometry, not Koide geometry.

**Mechanism**:
- TBM mixing: θ₁₂ = 35.3°, θ₂₃ = 45°, θ₁₃ = 0°
- These angles define a different "cone" in mass space
- The A₄ or S₄ discrete symmetry (not A₂) governs neutrinos

**Prediction**: Mass ratios from TBM structure.

**Test**: Do TBM angles predict the correct mass splitting?

**Pros**:
- TBM is well-established phenomenology
- A₄ symmetry is natural in many models

**Cons**:
- Breaks unification with charged leptons
- θ₁₃ ≠ 0 requires TBM-breaking

---

### Candidate D: Charge-Dependent Cone Angle

**Idea**: The Koide Q depends on electric charge.

**Mechanism**:
$$Q = \frac{1}{3} + \frac{|Q_{em}|}{3}$$

- Charged (|Q| = 1): Q = 1/3 + 1/3 = 2/3 ✅
- Neutral (|Q| = 0): Q = 1/3 + 0 = 1/3 ✅

**Prediction**: Neutrinos have Q = 1/3 exactly.

**Test**: Does Q = 1/3 with some phase reproduce the data?

**Pros**:
- Simple formula
- Unifies charged and neutral
- Q = 1/3 and Q = 2/3 are both geometric fixed points

**Cons**:
- Ad hoc connection to charge
- Still need to determine θ_ν

---

### Candidate E: Majorana vs Dirac Distinction

**Idea**: Neutrinos are Majorana (self-conjugate), which changes the geometry.

**Mechanism**:
- Dirac fermions: Complex mass matrix → Q = 2/3
- Majorana fermions: Real/symmetric mass matrix → Q = 1/3

**Prediction**: The Majorana condition halves the cone angle.

**Test**: Is there a factor of 2 between Dirac and Majorana Q values?

**Pros**:
- Physically motivated (neutrinos may be Majorana)
- Factor of 2 between Q = 2/3 and Q = 1/3

**Cons**:
- Majorana nature unconfirmed
- Mechanism unclear

---

### Candidate F: Seesaw with Different Heavy Phase

**Idea**: Heavy Majorana neutrinos have a different Koide phase, not 2/9.

**Mechanism**:
- M_R follows Koide with θ_R ≠ 2/9
- m_ν ∝ 1/M_R inherits different structure

**Prediction**: Find θ_R that gives correct light masses.

**Test**: What θ_R reproduces the data?

**Pros**:
- Seesaw is standard mechanism
- Allows different heavy/light structure

**Cons**:
- θ_R = -5.7° (from search) has no geometric meaning
- Adds free parameter

---

### Candidate G: Two-Lattice Model

**Idea**: Charged leptons couple to A₂, neutrinos couple to a different sublattice.

**Mechanism**:
- A₂ sublattice → Q = 2/3 (charged)
- Different sublattice (A₁? G₂?) → Q = 1/3 (neutral)

**Prediction**: Identify the "neutrino sublattice" in D₆.

**Test**: Does D₆ contain a sublattice with Q = 1/3 geometry?

**Pros**:
- Geometric distinction
- Could explain charge dependence

**Cons**:
- Need to identify the sublattice
- May not exist

---

## 7. RANKING OF CANDIDATES

| Candidate | Geometric Basis | Predictive Power | Likelihood |
|-----------|-----------------|------------------|------------|
| **D: Charge-Dependent Q** | Q = 1/3 + |Q_em|/3 | High | ⭐⭐⭐⭐ |
| **A: Q = 1/3 Center** | A₂ center | Medium | ⭐⭐⭐ |
| **E: Majorana/Dirac** | Factor of 2 | Medium | ⭐⭐⭐ |
| **B: θ₁₃ Phase** | TBM deviation | Low | ⭐⭐ |
| **C: TBM Structure** | A₄ symmetry | Medium | ⭐⭐ |
| **F: Seesaw Different θ** | None | Low | ⭐ |
| **G: Two-Lattice** | Unknown | Unknown | ⭐ |

---

## 8. SPECIFIC TASKS

### Task 1: Test Q = 1/3 + |Q_em|/3

```python
import numpy as np

def test_charge_dependent_Q():
    print("=" * 70)
    print("TEST: Q = 1/3 + |Q_em|/3")
    print("=" * 70)
    
    # Charged leptons
    Q_charged = 1/3 + 1/3
    print(f"\nCharged leptons (|Q_em| = 1):")
    print(f"  Q = 1/3 + 1/3 = {Q_charged:.6f}")
    print(f"  Expected: 0.666667 (2/3)")
    print(f"  Match: {np.isclose(Q_charged, 2/3)}")
    
    # Neutrinos
    Q_neutral = 1/3 + 0/3
    print(f"\nNeutrinos (|Q_em| = 0):")
    print(f"  Q = 1/3 + 0/3 = {Q_neutral:.6f}")
    print(f"  Expected: 0.333333 (1/3)")
    
    # What epsilon gives Q = 1/3?
    # Q = 1/3 + eps^2/6 => eps^2 = 0 => eps = 0
    # But eps = 0 means m1 = m2 = m3 (perfect degeneracy)
    # We need small eps to get splitting
    
    # Target: Δm²₃₁/Δm²₂₁ = 32.6
    # Search for eps that gives this ratio
    
    target_ratio = 32.6
    
    print(f"\n--- Search for epsilon ---")
    for eps in np.linspace(0.01, 0.5, 100):
        # Masses at theta = 0 (most degenerate point)
        phases = np.array([0, 2*np.pi/3, 4*np.pi/3])
        T = 1 + eps * np.cos(phases)
        if np.any(T <= 0):
            continue
        m = T**2
        m.sort()
        
        # Ratio
        dm21 = m[1]**2 - m[0]**2
        dm31 = m[2]**2 - m[0]**2
        if dm21 > 0:
            ratio = dm31 / dm21
            if abs(ratio - target_ratio) < 1:
                Q_calc = 1/3 + eps**2/6
                print(f"  eps = {eps:.4f}: ratio = {ratio:.2f}, Q = {Q_calc:.4f}")

test_charge_dependent_Q()
```

### Task 2: Test θ = θ₁₃ with Small ε

```python
def test_theta13_phase():
    print("\n" + "=" * 70)
    print("TEST: θ_ν = θ₁₃ ≈ 8.5°")
    print("=" * 70)
    
    theta_13 = np.radians(8.5)  # Reactor angle
    target_ratio = 32.6
    
    print(f"θ₁₃ = {np.degrees(theta_13):.2f}° = {theta_13:.4f} rad")
    
    # Search for epsilon
    for eps in np.linspace(0.1, 1.5, 100):
        phases = theta_13 + np.array([0, 2*np.pi/3, 4*np.pi/3])
        T = 1 + eps * np.cos(phases)
        if np.any(T <= 0):
            continue
        m = T**2
        m.sort()
        
        dm21 = m[1]**2 - m[0]**2
        dm31 = m[2]**2 - m[0]**2
        if dm21 > 0:
            ratio = dm31 / dm21
            if abs(ratio - target_ratio) < 2:
                Q_calc = 1/3 + eps**2/6
                print(f"  eps = {eps:.4f}: ratio = {ratio:.2f}, Q = {Q_calc:.4f}")

test_theta13_phase()
```

### Task 3: Full Parameter Search

```python
def full_search():
    print("\n" + "=" * 70)
    print("FULL PARAMETER SEARCH")
    print("=" * 70)
    
    target_ratio = 32.6
    best_params = None
    best_diff = 1e9
    
    for theta in np.linspace(-np.pi/4, np.pi/4, 200):
        for eps in np.linspace(0.05, 1.5, 200):
            phases = theta + np.array([0, 2*np.pi/3, 4*np.pi/3])
            T = 1 + eps * np.cos(phases)
            if np.any(T <= 0):
                continue
            m = T**2
            m.sort()
            
            dm21 = m[1]**2 - m[0]**2
            dm31 = m[2]**2 - m[0]**2
            if dm21 > 0:
                ratio = dm31 / dm21
                diff = abs(ratio - target_ratio)
                if diff < best_diff:
                    best_diff = diff
                    Q_calc = 1/3 + eps**2/6
                    best_params = (theta, eps, ratio, Q_calc)
    
    if best_params:
        theta, eps, ratio, Q = best_params
        print(f"Best fit:")
        print(f"  θ = {np.degrees(theta):.2f}° = {theta:.4f} rad")
        print(f"  ε = {eps:.4f}")
        print(f"  Q = {Q:.4f}")
        print(f"  Ratio = {ratio:.2f} (target: {target_ratio})")
        
        # Check if theta is special
        print(f"\nIs θ special?")
        print(f"  θ/θ₁₃ = {theta/np.radians(8.5):.2f}")
        print(f"  θ/(2/9) = {theta/(2/9):.2f}")
        print(f"  θ/(π/12) = {theta/(np.pi/12):.2f}")

full_search()
```

---

## 9. DELIVERABLES

1. **Q formula test**: Does Q = 1/3 + |Q_em|/3 work?
2. **θ₁₃ test**: Does θ_ν = θ₁₃ reproduce the mass ratio?
3. **Best-fit parameters**: What (θ, ε) matches the data?
4. **Geometric interpretation**: Is the best-fit special?
5. **Candidate ranking**: Which mechanism is most likely?
6. **Unified picture**: Can we explain both charged and neutral?

---

## 10. EXPECTED OUTCOMES

### Scenario A: Q = 1/3 + |Q_em|/3 Works

If this formula holds:
- **Charged**: Q = 2/3 (proven)
- **Neutral**: Q = 1/3 (predicted)
- **Unified**: Single principle for all leptons
- **Next**: Derive from D₆ geometry

### Scenario B: θ₁₃ Determines Neutrino Phase

If θ_ν = θ₁₃:
- Mass and mixing connected
- TBM deviation = mass splitting
- **Next**: Derive θ₁₃ from geometry

### Scenario C: No Simple Pattern

If no candidate works:
- Neutrino masses may have different origin
- Seesaw with arbitrary parameters
- Theory incomplete for neutral sector

---

## 11. REFERENCES

1. **Koide, Y.** (1983). "A Fermion-Boson Composite Model..." *Phys. Lett. B* 120.
2. **Brannen, C.** (2006). "The Lepton Masses." *Preprint*.
3. **Harrison, Perkins, Scott** (2002). "Tri-bimaximal mixing..." *Phys. Lett. B* 530.
4. **PDG** (2024). "Review of Particle Physics." Neutrino section.
5. **Planck Collaboration** (2018). "Cosmological parameters." *A&A* 641.

