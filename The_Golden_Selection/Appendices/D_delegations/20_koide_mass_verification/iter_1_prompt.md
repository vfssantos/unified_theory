# Delegation 20 - Iteration 1: Koide Mass Ratio Numerical Verification

## 1. BACKGROUND: The Koide Formula

### 1.1 The Original Koide Formula (1982)

Yoshio Koide discovered an empirical relation for charged lepton masses:

$$Q = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

This holds to **0.01% accuracy** — one of the most precise "coincidences" in particle physics.

**Reference**: Koide, Y. (1983). "A Fermion-Boson Composite Model of Quarks and Leptons." *Phys. Lett. B* 120, 161-165.

### 1.2 The Geometric Parameterization

The Koide formula is equivalent to masses lying on a circle in "mass space":

$$\sqrt{m_i} = M_0 \left(1 + \sqrt{2}\cos\left(\theta_0 + \frac{2\pi i}{3}\right)\right), \quad i = 0, 1, 2$$

where:
- **$M_0$** sets the overall mass scale
- **$\theta_0$** is the "Koide phase" (determines mass ratios)
- The **120° spacing** ($2\pi/3$) is what gives $Q = 2/3$

**Reference**: Brannen, C.A. (2006). "The Lepton Masses." *Preprint*. Available at: http://brannenworks.com/MASSES2.pdf

### 1.3 The Observed Koide Phase

From experimental masses (PDG 2024):
- $m_e = 0.51099895$ MeV
- $m_\mu = 105.6583755$ MeV  
- $m_\tau = 1776.86$ MeV

The empirically-fitted Koide phase is approximately:
$$\theta_0^{exp} \approx 0.2222 \text{ rad} \approx 12.73°$$

or equivalently $\theta_0 \approx 360° - 12.73° = 347.27°$ (depending on convention).

### 1.4 The Golden Selection Claim

The **Golden Selection theory** proposes that the Koide phase has a geometric origin:

$$\theta_0 = 360° - \arctan(\phi^{-3}) \approx 346.72°$$

where $\phi = (1+\sqrt{5})/2 \approx 1.618$ is the golden ratio.

Note: $\phi^{-3} \approx 0.2361$ and $\arctan(\phi^{-3}) \approx 13.28°$.

**The claim**: This geometric phase produces the correct lepton mass ratios.

---

## 2. THE CLAIM TO VERIFY

**Primary Claim**: The formula with $\theta_0 = 360° - \arctan(\phi^{-3})$ produces:
- $m_\tau / m_e \approx 3477$
- $m_\mu / m_e \approx 207$

**Secondary Claim (The "Singularity" Argument)**: The electron is light because its angle $\theta_e$ is close to a "singularity" where the mass term $1 + \sqrt{2}\cos\theta \to 0$.

---

## 3. EXPERIMENTAL DATA

### Charged Lepton Masses (PDG 2024)

| Particle | Mass (MeV) | Uncertainty |
|----------|------------|-------------|
| Electron | 0.51099895000 | ±0.00000000015 |
| Muon | 105.6583755 | ±0.0000023 |
| Tau | 1776.86 | ±0.12 |

**Reference**: Particle Data Group (2024). https://pdg.lbl.gov/

### Derived Ratios

| Ratio | Value |
|-------|-------|
| $m_\mu / m_e$ | 206.7682830 |
| $m_\tau / m_e$ | 3477.23 |
| $m_\tau / m_\mu$ | 16.8170 |

### Koide Q-Value Check

$$Q = \frac{0.511 + 105.66 + 1776.86}{(\sqrt{0.511} + \sqrt{105.66} + \sqrt{1776.86})^2} = \frac{1883.03}{(0.715 + 10.28 + 42.15)^2} = \frac{1883.03}{2825.8} = 0.6666...$$

**Confirmed**: $Q = 2/3$ to high precision.

---

## 4. TASKS

### Task A: Direct Calculation

Using the Golden Selection phase $\theta_0 = 360° - \arctan(\phi^{-3}) \approx 346.72°$:

1. Compute the three angles: $\theta_0$, $\theta_0 + 120°$, $\theta_0 + 240°$
2. Compute mass terms: $T_i = 1 + \sqrt{2}\cos(\theta_i)$
3. Compute mass ratios: $(T_{max}/T_{min})^2$

**Question**: Does this match $m_\tau/m_e = 3477$ and $m_\mu/m_e = 207$?

### Task B: Permutation Search

The assignment $(\tau, \mu, e) \leftrightarrow (i=0, 1, 2)$ is not fixed a priori.

Test all 6 permutations to find if ANY produces correct ratios.

### Task C: Optimal Phase Search

Scan $\theta_0 \in [0°, 360°]$ to find:
1. The $\theta_0$ that minimizes error in mass ratios
2. Compare this optimal phase to $\arctan(\phi^{-3})$

### Task D: Singularity Analysis

The singularity (where $T_i = 0$) occurs at:
$$\theta_{sing} = \arccos(-1/\sqrt{2}) = 135° \text{ or } 225°$$

For each generation:
1. How far is its angle from the nearest singularity?
2. Is the electron actually "near" a singularity?

---

## 5. VERIFICATION CODE

```python
import numpy as np
from itertools import permutations

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Observed masses (MeV) - PDG 2024
m_e = 0.51099895
m_mu = 105.6583755
m_tau = 1776.86

# Observed ratios
ratio_mu_e = m_mu / m_e   # 206.768
ratio_tau_e = m_tau / m_e  # 3477.23
ratio_tau_mu = m_tau / m_mu  # 16.817

print("=" * 60)
print("KOIDE MASS RATIO VERIFICATION")
print("=" * 60)

print(f"\n1. OBSERVED DATA (PDG 2024)")
print(f"   m_e  = {m_e:.8f} MeV")
print(f"   m_μ  = {m_mu:.7f} MeV")
print(f"   m_τ  = {m_tau:.2f} MeV")
print(f"\n   Ratios:")
print(f"   m_μ/m_e  = {ratio_mu_e:.3f}")
print(f"   m_τ/m_e  = {ratio_tau_e:.2f}")
print(f"   m_τ/m_μ  = {ratio_tau_mu:.4f}")

# Verify Koide Q = 2/3
Q = (m_e + m_mu + m_tau) / (np.sqrt(m_e) + np.sqrt(m_mu) + np.sqrt(m_tau))**2
print(f"\n   Koide Q = {Q:.6f} (target: 0.666667)")

# Golden Koide phase
theta_0_golden = 360 - np.degrees(np.arctan(phi**-3))
print(f"\n2. GOLDEN SELECTION PHASE")
print(f"   φ = {phi:.10f}")
print(f"   φ⁻³ = {phi**-3:.10f}")
print(f"   arctan(φ⁻³) = {np.degrees(np.arctan(phi**-3)):.4f}°")
print(f"   θ₀ = 360° - arctan(φ⁻³) = {theta_0_golden:.4f}°")

# Koide mass formula
def koide_terms(theta_0_deg):
    """Compute mass terms T_i = 1 + √2 cos(θ_i) for i=0,1,2."""
    theta_0 = np.radians(theta_0_deg)
    angles = [theta_0, theta_0 + 2*np.pi/3, theta_0 + 4*np.pi/3]
    terms = [1 + np.sqrt(2) * np.cos(a) for a in angles]
    return terms, [np.degrees(a) % 360 for a in angles]

# Task A: Direct calculation
print(f"\n3. TASK A: DIRECT CALCULATION (θ₀ = {theta_0_golden:.2f}°)")
terms, angles = koide_terms(theta_0_golden)
print(f"   Angles: θ₀={angles[0]:.2f}°, θ₁={angles[1]:.2f}°, θ₂={angles[2]:.2f}°")
print(f"   Terms:  T₀={terms[0]:.6f}, T₁={terms[1]:.6f}, T₂={terms[2]:.6f}")

if all(t > 0 for t in terms):
    # Sort by magnitude (τ > μ > e)
    sorted_terms = sorted(enumerate(terms), key=lambda x: x[1], reverse=True)
    T_tau, T_mu, T_e = [t[1] for t in sorted_terms]
    idx_tau, idx_mu, idx_e = [t[0] for t in sorted_terms]
    
    pred_tau_e = (T_tau / T_e)**2
    pred_mu_e = (T_mu / T_e)**2
    
    err_tau = abs(pred_tau_e - ratio_tau_e) / ratio_tau_e * 100
    err_mu = abs(pred_mu_e - ratio_mu_e) / ratio_mu_e * 100
    
    print(f"\n   Predicted (sorted by magnitude):")
    print(f"   m_τ/m_e = {pred_tau_e:.2f} (observed: {ratio_tau_e:.2f}, error: {err_tau:.1f}%)")
    print(f"   m_μ/m_e = {pred_mu_e:.2f} (observed: {ratio_mu_e:.2f}, error: {err_mu:.1f}%)")
else:
    print("   WARNING: Negative mass term!")

# Task B: All permutations
print(f"\n4. TASK B: ALL PERMUTATIONS")
print(f"   Testing all 6 assignments of (τ,μ,e) to (T₀,T₁,T₂):")
best_perm = None
best_err = float('inf')

for perm in permutations([0, 1, 2]):
    T_tau = terms[perm[0]]
    T_mu = terms[perm[1]]
    T_e = terms[perm[2]]
    
    if T_e > 0 and T_mu > 0 and T_tau > 0:
        r_tau_e = (T_tau / T_e)**2
        r_mu_e = (T_mu / T_e)**2
        err_tau = abs(r_tau_e - ratio_tau_e) / ratio_tau_e * 100
        err_mu = abs(r_mu_e - ratio_mu_e) / ratio_mu_e * 100
        total_err = err_tau + err_mu
        
        print(f"   Perm {perm}: τ/e={r_tau_e:8.1f} ({err_tau:5.1f}%), μ/e={r_mu_e:6.1f} ({err_mu:5.1f}%)")
        
        if total_err < best_err:
            best_err = total_err
            best_perm = perm

print(f"\n   Best permutation: {best_perm} with total error {best_err:.1f}%")

# Task C: Phase scan
print(f"\n5. TASK C: OPTIMAL PHASE SEARCH")
best_theta = None
best_scan_err = float('inf')

for theta_0_deg in np.linspace(0, 360, 36001):  # 0.01° resolution
    terms_scan, _ = koide_terms(theta_0_deg)
    if all(t > 0 for t in terms_scan):
        sorted_t = sorted(terms_scan, reverse=True)
        r_tau_e = (sorted_t[0] / sorted_t[2])**2
        r_mu_e = (sorted_t[1] / sorted_t[2])**2
        err = abs(r_tau_e - ratio_tau_e) / ratio_tau_e + abs(r_mu_e - ratio_mu_e) / ratio_mu_e
        if err < best_scan_err:
            best_scan_err = err
            best_theta = theta_0_deg
            best_ratios = (r_tau_e, r_mu_e)

print(f"   Optimal θ₀ = {best_theta:.2f}°")
print(f"   Predicted: τ/e = {best_ratios[0]:.2f}, μ/e = {best_ratios[1]:.2f}")
print(f"   Observed:  τ/e = {ratio_tau_e:.2f}, μ/e = {ratio_mu_e:.2f}")
print(f"\n   Golden θ₀ = {theta_0_golden:.2f}°")
print(f"   Difference from optimal = {abs(best_theta - theta_0_golden):.2f}°")

# Task D: Singularity analysis
print(f"\n6. TASK D: SINGULARITY ANALYSIS")
singularities = [135, 225]  # degrees where 1 + √2 cos θ = 0
print(f"   Singularities at: {singularities}° (where T = 0)")

_, angles = koide_terms(theta_0_golden)
for i, ang in enumerate(angles):
    min_dist = min(abs(ang - s) for s in singularities)
    min_dist = min(min_dist, 360 - min_dist)  # Handle wrap-around
    print(f"   θ_{i} = {ang:.2f}°, distance to singularity = {min_dist:.2f}°")

# Final verdict
print(f"\n" + "=" * 60)
print("VERDICT")
print("=" * 60)
if best_err < 10:
    print("CONFIRMED: Golden phase produces correct ratios (<5% error each)")
elif abs(best_theta - theta_0_golden) < 10:
    print("CLOSE: Golden phase is within 10° of optimal")
elif abs(best_theta - theta_0_golden) < 30:
    print("PARTIAL: Golden phase is within 30° of optimal")
else:
    print("FAILED: Golden phase is far from optimal (>30°)")
```

---

## 6. DELIVERABLES

### Required Output

1. **Task A**: Direct calculation results with $\theta_0 = 346.72°$
2. **Task B**: Best permutation and its error
3. **Task C**: Optimal $\theta_0$ from scan and comparison to golden value
4. **Task D**: Singularity distances for each generation

### Verdict Categories

| Verdict | Meaning |
|---------|---------|
| **CONFIRMED** | Golden $\theta_0$ produces correct ratios (<5% error each) |
| **CLOSE** | Golden $\theta_0$ is within 10° of optimal |
| **PARTIAL** | Golden $\theta_0$ is within 30° of optimal |
| **FAILED** | Golden $\theta_0$ is far from optimal (>30°) |
| **IMPOSSIBLE** | No $\theta_0$ can produce the observed ratios |

---

## 7. REFERENCES

1. **Koide, Y.** (1983). "A Fermion-Boson Composite Model of Quarks and Leptons." *Phys. Lett. B* 120, 161-165.

2. **Brannen, C.A.** (2006). "The Lepton Masses." Available at: http://brannenworks.com/MASSES2.pdf

3. **Particle Data Group** (2024). "Review of Particle Physics." *Phys. Rev. D* 110, 030001. https://pdg.lbl.gov/

4. **Rivero, A.** (2005). "The strange formula of Dr. Koide." arXiv:hep-ph/0505220.

5. **Foot, R.** (1994). "A note on Koide's lepton mass relation." arXiv:hep-ph/9402242.

---

## 8. CONTEXT

This is a **critical test** of the Golden Selection theory's mass mechanism. The theory claims:
- The Koide phase $\theta_0$ is geometrically determined by the golden ratio
- The electron is light because it sits near a "singularity" in the Koide formula

If the golden phase does NOT produce the correct mass ratios, the theory has no explanation for the lepton mass hierarchy.

**Be rigorous. Report exact numbers. Don't round favorably.**
