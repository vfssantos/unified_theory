# Delegation 20 - Iteration 2: Exponential Mass Model Verification

## 1. BACKGROUND: The New Mechanism

### 1.1 What We've Established (Delegation 24)

The "3 generations" problem has been solved geometrically:

1. **Source of "3"**: Danzer node types (A, B, C) in the D₆ → H₃ quasicrystal
2. **Node frequencies**: f_A : f_B : f_C = φ² : φ : 1 (approximately)
3. **Internal depths**: r_A : r_B : r_C ≈ φ² : φ : 1

Where φ = (1+√5)/2 ≈ 1.618 is the golden ratio.

### 1.2 The Exponential Coupling Hypothesis

Linear mapping of depths to masses fails (gives only 4:1 ratio, not 3477:1).

The correct mechanism is **exponential coupling**:

$$m_n = m_0 \exp(\alpha \cdot \phi^n), \quad n = 0, 1, 2$$

Where:
- **n = 0** (Gen 1, A-type, Skin): Electron
- **n = 1** (Gen 2, B-type, Shell): Muon  
- **n = 2** (Gen 3, C-type, Core): Tau

This explains why geometric φ-powers become **logarithms** of masses:
$$\ln(m_\tau) - \ln(m_\mu) \approx \alpha \cdot (\phi^2 - \phi) = \alpha \cdot 1$$
$$\ln(m_\mu) - \ln(m_e) \approx \alpha \cdot (\phi - 1) = \alpha \cdot \phi^{-1}$$

### 1.3 The Koide Constraint

The Koide formula is an empirical observation:

$$Q = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

This holds to **0.01% accuracy** for charged leptons.

**The Key Question**: Does the exponential model m = m₀ exp(α·φⁿ) **automatically satisfy** Q = 2/3?

---

## 2. THE CLAIMS TO VERIFY

### Primary Claim
The exponential model with φ-scaling:
$$m_n = m_0 \exp(\alpha \cdot \phi^n)$$
can reproduce the observed lepton mass ratios.

### Secondary Claim
This model **automatically satisfies** (or nearly satisfies) the Koide relation Q = 2/3.

### Tertiary Claim
The parameter α has a geometric interpretation related to the node-type structure.

---

## 3. EXPERIMENTAL DATA

### Charged Lepton Masses (PDG 2024)

| Particle | Mass (MeV) | Generation | Node Type |
|----------|------------|------------|-----------|
| Electron | 0.51099895 | 1 | A (Skin) |
| Muon | 105.6583755 | 2 | B (Shell) |
| Tau | 1776.86 | 3 | C (Core) |

### Derived Quantities

| Quantity | Value |
|----------|-------|
| m_μ / m_e | 206.768 |
| m_τ / m_e | 3477.23 |
| m_τ / m_μ | 16.817 |
| ln(m_τ/m_e) | 8.154 |
| ln(m_μ/m_e) | 5.334 |
| Koide Q | 0.666661 |

### φ-Related Values

| Quantity | Value |
|----------|-------|
| φ | 1.6180339887 |
| φ² | 2.6180339887 |
| φ - 1 = φ⁻¹ | 0.6180339887 |
| φ² - φ = 1 | 1.0000000000 |

---

## 4. TASKS

### Task A: Fit the Exponential Model

Given m_n = m₀ exp(α·φⁿ) for n = 0, 1, 2:

1. Find α that best fits the observed mass ratios
2. Compute the predicted masses
3. Compare to observed values

**Key equations:**
$$\frac{m_\tau}{m_e} = \exp(\alpha \cdot (\phi^2 - 1)) = \exp(\alpha \cdot \phi)$$

Wait, let me reconsider. If n = 0, 1, 2:
$$m_0 = m_0 \cdot e^{\alpha \cdot \phi^0} = m_0 \cdot e^{\alpha}$$
$$m_1 = m_0 \cdot e^{\alpha \cdot \phi}$$
$$m_2 = m_0 \cdot e^{\alpha \cdot \phi^2}$$

So:
$$\frac{m_2}{m_0} = e^{\alpha(\phi^2 - 1)} = e^{\alpha \cdot \phi}$$

From observed τ/e ratio:
$$\alpha = \frac{\ln(3477.23)}{\phi} = \frac{8.154}{1.618} \approx 5.04$$

### Task B: Check Koide Q

With the fitted α and m₀, compute:
$$Q = \frac{m_0 + m_1 + m_2}{(\sqrt{m_0} + \sqrt{m_1} + \sqrt{m_2})^2}$$

**Question**: Is Q close to 2/3?

### Task C: Explore Alternative Parameterizations

Try different forms:
1. **Form 1**: m_n = m₀ exp(α·φⁿ) with n = 0, 1, 2
2. **Form 2**: m_n = m₀ exp(α·n·φ) (linear in n, scaled by φ)
3. **Form 3**: m_n = m₀ · φ^(β·n²) (quadratic scaling)

Which form best matches both mass ratios AND Koide Q?

### Task D: Derive α from Geometry

If α has a geometric origin, it might be:
- Related to the window volumes (V_A, V_B, V_C)
- Related to the internal depths (r_A, r_B, r_C)
- A simple function of φ

**Check**: Is α ≈ φ³ ≈ 4.236? Or α ≈ 5 = φ² + φ?

### Task E: Connection to Koide Phase

The traditional Koide parameterization uses:
$$\sqrt{m_i} = M_0 (1 + \sqrt{2}\cos(\theta_0 + 2\pi i/3))$$

**Question**: Can we derive θ₀ from the exponential model?

If the exponential model works, what value of θ₀ does it correspond to?

---

## 5. VERIFICATION CODE

```python
import numpy as np
from scipy.optimize import minimize_scalar, minimize

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Observed masses (MeV) - PDG 2024
m_e = 0.51099895
m_mu = 105.6583755
m_tau = 1776.86
masses_obs = np.array([m_e, m_mu, m_tau])

print("=" * 70)
print("EXPONENTIAL MASS MODEL VERIFICATION")
print("=" * 70)

print("\n1. OBSERVED DATA")
print(f"   m_e  = {m_e:.8f} MeV")
print(f"   m_μ  = {m_mu:.7f} MeV")
print(f"   m_τ  = {m_tau:.2f} MeV")
print(f"   m_τ/m_e = {m_tau/m_e:.2f}")
print(f"   m_μ/m_e = {m_mu/m_e:.3f}")
print(f"   ln(m_τ/m_e) = {np.log(m_tau/m_e):.4f}")

# Observed Koide Q
Q_obs = (m_e + m_mu + m_tau) / (np.sqrt(m_e) + np.sqrt(m_mu) + np.sqrt(m_tau))**2
print(f"   Koide Q = {Q_obs:.6f}")

print("\n2. EXPONENTIAL MODEL: m_n = m_0 * exp(α * φ^n)")
print(f"   φ = {phi:.10f}")
print(f"   φ² = {phi**2:.10f}")

# Task A: Fit α from τ/e ratio
# m_2/m_0 = exp(α(φ² - 1)) = exp(α·φ)
alpha_fit = np.log(m_tau / m_e) / phi
print(f"\n   Fitted α (from τ/e ratio) = {alpha_fit:.6f}")

# Predict masses
def exp_model(m0, alpha, n):
    return m0 * np.exp(alpha * phi**n)

# Find m0 that gives correct electron mass
# m_e = m0 * exp(α * φ^0) = m0 * exp(α)
m0_fit = m_e / np.exp(alpha_fit)
print(f"   Fitted m₀ = {m0_fit:.8f} MeV")

# Predicted masses
m_pred = [exp_model(m0_fit, alpha_fit, n) for n in range(3)]
print(f"\n   Predicted masses:")
print(f"   m_e  = {m_pred[0]:.8f} MeV (obs: {m_e:.8f})")
print(f"   m_μ  = {m_pred[1]:.4f} MeV (obs: {m_mu:.4f})")
print(f"   m_τ  = {m_pred[2]:.2f} MeV (obs: {m_tau:.2f})")

err_mu = abs(m_pred[1] - m_mu) / m_mu * 100
err_tau = abs(m_pred[2] - m_tau) / m_tau * 100
print(f"\n   Errors: μ = {err_mu:.2f}%, τ = {err_tau:.2f}%")

# Task B: Check Koide Q
Q_pred = sum(m_pred) / sum(np.sqrt(m) for m in m_pred)**2
print(f"\n3. KOIDE Q CHECK")
print(f"   Predicted Q = {Q_pred:.6f}")
print(f"   Observed Q  = {Q_obs:.6f}")
print(f"   Target Q    = 0.666667")
print(f"   Error from 2/3 = {abs(Q_pred - 2/3) / (2/3) * 100:.2f}%")

# Task C: Alternative parameterizations
print("\n4. ALTERNATIVE PARAMETERIZATIONS")

# Form 2: m_n = m0 * exp(α * n * φ)
def form2_masses(m0, alpha):
    return [m0 * np.exp(alpha * n * phi) for n in range(3)]

def form2_error(params):
    m0, alpha = params
    m_pred = form2_masses(m0, alpha)
    if any(m <= 0 for m in m_pred):
        return 1e10
    err_tau = (m_pred[2] - m_tau)**2 / m_tau**2
    err_mu = (m_pred[1] - m_mu)**2 / m_mu**2
    return err_tau + err_mu

result2 = minimize(form2_error, [0.1, 2], method='Nelder-Mead')
m0_2, alpha_2 = result2.x
m_pred_2 = form2_masses(m0_2, alpha_2)
Q_2 = sum(m_pred_2) / sum(np.sqrt(m) for m in m_pred_2)**2
print(f"   Form 2 (m = m0·exp(α·n·φ)): α = {alpha_2:.4f}, Q = {Q_2:.6f}")

# Form 3: m_n = m0 * φ^(β*n²)
def form3_masses(m0, beta):
    return [m0 * phi**(beta * n**2) for n in range(3)]

def form3_error(params):
    m0, beta = params
    m_pred = form3_masses(m0, beta)
    if any(m <= 0 for m in m_pred):
        return 1e10
    err_tau = (m_pred[2] - m_tau)**2 / m_tau**2
    err_mu = (m_pred[1] - m_mu)**2 / m_mu**2
    return err_tau + err_mu

result3 = minimize(form3_error, [0.5, 5], method='Nelder-Mead')
m0_3, beta_3 = result3.x
m_pred_3 = form3_masses(m0_3, beta_3)
Q_3 = sum(m_pred_3) / sum(np.sqrt(m) for m in m_pred_3)**2
print(f"   Form 3 (m = m0·φ^(β·n²)): β = {beta_3:.4f}, Q = {Q_3:.6f}")

# Task D: Check if α has simple φ-expression
print("\n5. GEOMETRIC INTERPRETATION OF α")
print(f"   Fitted α = {alpha_fit:.6f}")
print(f"   φ³ = {phi**3:.6f}")
print(f"   φ² + φ = {phi**2 + phi:.6f}")
print(f"   2φ² = {2*phi**2:.6f}")
print(f"   π = {np.pi:.6f}")
print(f"   φ·π = {phi*np.pi:.6f}")

# Check ratios
print(f"\n   α/φ³ = {alpha_fit/phi**3:.6f}")
print(f"   α/π = {alpha_fit/np.pi:.6f}")

# Task E: Convert to Koide phase
print("\n6. CONNECTION TO KOIDE PHASE")

# The Koide parameterization: sqrt(m_i) = M0 * (1 + sqrt(2)*cos(θ0 + 2πi/3))
# We can find θ0 by fitting to our predicted masses

def koide_masses(M0, theta0):
    return [(M0 * (1 + np.sqrt(2) * np.cos(theta0 + 2*np.pi*i/3)))**2 for i in range(3)]

def koide_error(params):
    M0, theta0 = params
    m_k = koide_masses(M0, theta0)
    if any(m <= 0 for m in m_k):
        return 1e10
    # Match to observed masses
    err = sum((m_k[i] - masses_obs[i])**2 / masses_obs[i]**2 for i in range(3))
    return err

result_k = minimize(koide_error, [10, 0.2], method='Nelder-Mead')
M0_k, theta0_k = result_k.x
theta0_deg = np.degrees(theta0_k) % 360
print(f"   Fitted Koide parameters:")
print(f"   M₀ = {M0_k:.4f}")
print(f"   θ₀ = {theta0_k:.6f} rad = {theta0_deg:.2f}°")

# Compare to golden prediction
theta0_golden = np.radians(360 - np.degrees(np.arctan(phi**-3)))
print(f"\n   Golden prediction: θ₀ = {np.degrees(theta0_golden):.2f}°")
print(f"   arctan(φ⁻³) = {np.degrees(np.arctan(phi**-3)):.2f}°")
print(f"   Difference = {abs(theta0_deg - np.degrees(theta0_golden)):.2f}°")

# Final verdict
print("\n" + "=" * 70)
print("VERDICT")
print("=" * 70)

if err_mu < 5 and err_tau < 5:
    print("✅ MASS RATIOS: Exponential model fits well (<5% error)")
else:
    print(f"⚠️ MASS RATIOS: Errors are μ={err_mu:.1f}%, τ={err_tau:.1f}%")

if abs(Q_pred - 2/3) < 0.01:
    print("✅ KOIDE Q: Model satisfies Q ≈ 2/3 (<1% error)")
elif abs(Q_pred - 2/3) < 0.05:
    print("⚠️ KOIDE Q: Model gives Q close to 2/3 (<5% error)")
else:
    print(f"❌ KOIDE Q: Model gives Q = {Q_pred:.4f}, far from 2/3")

if abs(alpha_fit - phi**3) < 0.5:
    print(f"✅ α ≈ φ³: Geometric interpretation found")
elif abs(alpha_fit - np.pi) < 0.5:
    print(f"✅ α ≈ π: Geometric interpretation found")
else:
    print(f"⚠️ α = {alpha_fit:.3f}: No simple φ-expression found")
```

---

## 6. DELIVERABLES

### Required Output

1. **Task A**: Fitted α and predicted masses
2. **Task B**: Koide Q from exponential model
3. **Task C**: Comparison of alternative forms
4. **Task D**: Geometric interpretation of α
5. **Task E**: Equivalent Koide phase θ₀

### Verdict Categories

| Verdict | Meaning |
|---------|---------|
| **CONFIRMED** | Exponential model fits masses AND gives Q ≈ 2/3 |
| **PARTIAL** | Model fits masses but Q ≠ 2/3 (or vice versa) |
| **FAILED** | Model doesn't fit masses |

---

## 7. CONTEXT

This is a test of the **new mass mechanism** discovered in Delegation 24:

1. **3 generations** come from Danzer node types (A, B, C)
2. **Mass hierarchy** comes from exponential coupling to node depth
3. **The question**: Does this mechanism naturally produce Koide Q = 2/3?

If YES: The Koide formula is a **consequence** of the node-type geometry.
If NO: Koide requires an additional constraint beyond the exponential model.

**Be rigorous. Report exact numbers. Don't round favorably.**

---

## 8. REFERENCES

1. **Delegation 24**: Generation sources — `Appendices/D_delegations/24_generation_sources/`
2. **Koide, Y.** (1983). "A Fermion-Boson Composite Model." *Phys. Lett. B* 120.
3. **PDG 2024**: Particle masses. https://pdg.lbl.gov/

