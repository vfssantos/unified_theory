# Deep Research Request: Koide A₂ Triples in D₆ Roots

## 1. BACKGROUND: The Golden Selection Theory

### The Axiom (Axiom 0)

The universe minimizes a **Schur-convex curvature functional** κ_Schur subject to topological stability constraints. This uniquely selects:
- **D = 3** spatial dimensions
- **φ = (1+√5)/2** as the optimal ratio
- **H₃ (icosahedral) symmetry** as the maximal 3D point group with φ-eigenvalue

### The Realization

The unique lattice realizing H₃ symmetry via cut-and-project is **D₆**. The D₆ → H₃ projection produces:
- **Physical space E∥** (3D)
- **Internal space E⊥** (3D)

### What We've Established

- **L⊥ operator** gives φ², φ⁴, φ⁶ cross-band ratios (Delegation 16-17)
- **15/11 in S₂** corresponds to A₃ subalgebra (Q_down = 11/15)
- **Shell centroids vanish** due to Weyl symmetry (Delegation 18)
- **Koide Q = 2/3 NOT found** in L⊥ eigenvalues or shell centroids

---

## 2. THE KOIDE MECHANISM (from E₈ Theory)

### What Worked in E₈

The `E_appendix_calculations.md` reveals the **actual Koide mechanism**:

#### 2.1 A₂ Triples Exist

**Theorem E.4**: The inner 600-cell contains exactly **400 distinct A₂ (equilateral) triples** with:
$$|\alpha_i|^2 = 2, \quad \alpha_i \cdot \alpha_j = -1 \quad (i \neq j)$$

These form perfect 120° triangles in 2-planes within E₈.

#### 2.2 Explicit Lepton Triple

The simplest A₂ triple (living in first 3 coordinates of E₈):

| Label | Root # | Type | 8D Coordinates | h | θ in plane |
|-------|--------|------|----------------|---|------------|
| τ | 2 | D₈ | (1, -1, 0, 0, 0, 0, 0, 0) | −2 | 0° |
| μ | 7 | D₈ | (-1, 0, 1, 0, 0, 0, 0, 0) | +1 | 120° |
| e | 30 | D₈ | (0, 1, -1, 0, 0, 0, 0, 0) | +1 | 240° |

**Verification**:
- α_τ · α_μ = α_μ · α_e = α_e · α_τ = **-1** ✓
- α_τ + α_μ + α_e = **0** ✓
- Heights: (-2, +1, +1) — τ heaviest

#### 2.3 The Koide 2-Plane

Orthonormal basis for the plane spanned by these roots:
$$e_1 = \frac{1}{\sqrt{2}}(1, -1, 0, 0, 0, 0, 0, 0)$$
$$e_2 = \frac{1}{\sqrt{6}}(1, 1, -2, 0, 0, 0, 0, 0)$$

Projections give angles: 0°, 120°, 240° — **perfect A₂ geometry**.

#### 2.4 The Mass Formula

$$\sqrt{m_i} = M_0 \left(1 + \sqrt{2}\cos\left(\theta_0 + \frac{2\pi i}{3}\right)\right)$$

where:
- **θ₀ ≈ 347°** = 360° - arctan(φ⁻³)
- The **120° spacing** (2πi/3) gives Q = 2/3 automatically

#### 2.5 Only Leptons Satisfy Koide

| Sector | Q value | Koide? |
|--------|---------|--------|
| **Leptons** | 0.6667 | ✅ Exact |
| Up quarks | 0.849 | ❌ Uses Q = 6/7 (D₄) |
| Down quarks | 0.731 | ❌ Uses Q = 11/15 (A₃) |

---

## 3. THE D₆ ANALOG

### 3.1 D₆ Root System

The D₆ root system has **60 roots** of the form:
$$\pm e_i \pm e_j \quad \text{for } 1 \leq i < j \leq 6$$

where e_i are standard basis vectors in ℝ⁶.

All roots have |α|² = 2.

### 3.2 A₂ Condition in D₆

An **A₂ triple** (α, β, γ) must satisfy:
1. **Equal lengths**: |α|² = |β|² = |γ|² = 2
2. **Equal angles**: α · β = β · γ = γ · α = **-1**
3. **Closure**: α + β + γ = 0

### 3.3 Expected Structure

In D₆, the A₂ subalgebra can be embedded as:
- α₁ = e₁ - e₂
- α₂ = e₂ - e₃
- α₃ = -(α₁ + α₂) = e₃ - e₁

This is the **standard A₂ embedding** in the first 3 coordinates.

---

## 4. COMPUTATION GOALS

### Goal A: Enumerate All A₂ Triples

Search all $\binom{60}{3} = 34,220$ triplets of D₆ roots for A₂ condition:

```python
import numpy as np
from itertools import combinations

# Generate D₆ roots
def generate_d6_roots():
    roots = []
    for i in range(6):
        for j in range(i+1, 6):
            for si in [1, -1]:
                for sj in [1, -1]:
                    root = np.zeros(6)
                    root[i] = si
                    root[j] = sj
                    roots.append(root)
    return np.array(roots)

roots = generate_d6_roots()
print(f"D₆ has {len(roots)} roots")  # Should be 60

# Find A₂ triples
a2_triples = []
for i, j, k in combinations(range(len(roots)), 3):
    α, β, γ = roots[i], roots[j], roots[k]
    
    # Check A₂ condition
    dot_ab = np.dot(α, β)
    dot_bc = np.dot(β, γ)
    dot_ca = np.dot(γ, α)
    
    if np.isclose(dot_ab, -1) and np.isclose(dot_bc, -1) and np.isclose(dot_ca, -1):
        # Verify closure
        if np.allclose(α + β + γ, 0):
            a2_triples.append((i, j, k))

print(f"Found {len(a2_triples)} A₂ triples")
```

**Deliverable**: Count of A₂ triples and list of all (i, j, k) indices.

### Goal B: Project to E⊥ and Check Angles

For each A₂ triple, project to E⊥ using Koca–Al-Siyabi matrix and verify 120° angles:

```python
# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Koca–Al-Siyabi projection to E_perp (3x6)
P_perp = (1/np.sqrt(2 * (1 + phi**2))) * np.array([
    [1, -1, 0, 0, phi, -phi],
    [0, 0, 1, -1, -phi, phi],
    [-phi, -phi, -phi, -phi, -1, -1]
]).T  # 6x3, then transpose for v @ P_perp

def angle_between(v1, v2):
    cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))

# For each A₂ triple
for (i, j, k) in a2_triples:
    α_perp = roots[i] @ P_perp
    β_perp = roots[j] @ P_perp
    γ_perp = roots[k] @ P_perp
    
    angle_ab = angle_between(α_perp, β_perp)
    angle_bc = angle_between(β_perp, γ_perp)
    angle_ca = angle_between(γ_perp, α_perp)
    
    # Check if angles are 120°
    if all(abs(a - 120) < 5 for a in [angle_ab, angle_bc, angle_ca]):
        print(f"Triple ({i},{j},{k}): angles = {angle_ab:.1f}°, {angle_bc:.1f}°, {angle_ca:.1f}°")
```

**Deliverable**: Which triples have 120° angles in E⊥?

### Goal C: Classify by Shell Structure

For each A₂ triple, compute |α_⊥|² for each root and classify:

```python
for (i, j, k) in a2_triples:
    xi_sq = [np.sum((roots[idx] @ P_perp)**2) for idx in [i, j, k]]
    print(f"Triple ({i},{j},{k}): |α_⊥|² = {xi_sq}")
```

**Deliverable**: Distribution of triples by internal shell structure.

### Goal D: Find Lepton-Like Triple

Look for a triple with structure similar to E₈ leptons:
- One root with different |α_⊥|² (τ — heaviest)
- Two roots with same |α_⊥|² (μ, e — lighter)

This mirrors the E₈ pattern: heights (-2, +1, +1).

### Goal E: Compute Koide Phase

For promising triples, compute the "phase" in the Koide 2-plane:

1. Find the 2-plane spanned by the triple in E⊥
2. Project each root onto this plane
3. Compute angles from a reference direction
4. Check if phases are 0°, 120°, 240°

### Goal F: Test Mass Predictions

If a lepton-like triple is found, test:

$$\sqrt{m_i} = M_0 \left(1 + \sqrt{2}\cos\left(\theta_0 + \frac{2\pi i}{3}\right)\right)$$

with θ₀ = 360° - arctan(φ⁻³) ≈ 347°.

**Compare**:
- Predicted m_e : m_μ : m_τ ratios
- Observed: 1 : 207 : 3477

---

## 5. SPECIFIC QUESTIONS

### Critical Questions

1. **How many A₂ triples exist in D₆?**
   - E₈ has 400 in the 600-cell
   - D₆ has 60 roots → expect fewer triples

2. **Do any triples have 120° angles in E⊥?**
   - The Koca–Al-Siyabi projection might distort angles
   - Need to check explicitly

3. **Is there a "lepton-like" triple?**
   - One root at different |α_⊥|² than the other two
   - Mirrors the E₈ height pattern (-2, +1, +1)

4. **Does θ₀ = 360° - arctan(φ⁻³) emerge?**
   - This is the key prediction from E₈
   - Would be strong validation if it appears in D₆

### Secondary Questions

5. **How do A₂ triples relate to L⊥ eigenvectors?**
   - Do the roots in a triple correspond to specific L⊥ modes?

6. **Can we identify "quark-like" triples?**
   - With Q = 6/7 (up) or Q = 11/15 (down) instead of Q = 2/3

---

## 6. EXPECTED RESULTS

### Best Case

- Multiple A₂ triples exist with 120° angles in E⊥
- One "lepton-like" triple with asymmetric |α_⊥|² pattern
- θ₀ ≈ 347° emerges from geometry
- Mass ratios match leptons to <1%

### Worst Case

- A₂ triples exist but angles are distorted (not 120° in E⊥)
- No clear lepton-like pattern
- θ₀ doesn't match arctan(φ⁻³)

### Either Way

- We learn whether the E₈ Koide mechanism ports to D₆
- If not, we understand what's missing

---

## 7. DELIVERABLES

### 7.1 A₂ Triple Census

| Count | Description |
|-------|-------------|
| Total A₂ triples | ??? |
| With 120° in E⊥ | ??? |
| With asymmetric |α_⊥|² | ??? |
| Lepton-like candidates | ??? |

### 7.2 Best Lepton Candidate

| Property | Value |
|----------|-------|
| Root indices | (?, ?, ?) |
| 6D coordinates | ... |
| |α_⊥|² values | ... |
| Angles in E⊥ | ... |
| Koide phase θ₀ | ... |

### 7.3 Mass Prediction Test

| Particle | Predicted (MeV) | Observed (MeV) | Error |
|----------|-----------------|----------------|-------|
| e | ... | 0.511 | ... |
| μ | ... | 105.66 | ... |
| τ | ... | 1776.86 | ... |

### 7.4 Verdict Table

| Finding | Status | Confidence |
|---------|--------|------------|
| A₂ triples exist in D₆ | FOUND/NOT FOUND | HIGH/MEDIUM/LOW |
| 120° angles in E⊥ | FOUND/NOT FOUND | ... |
| Lepton-like triple | FOUND/NOT FOUND | ... |
| θ₀ = 360° - arctan(φ⁻³) | MATCHES/DOESN'T MATCH | ... |
| Mass predictions accurate | YES/NO | ... |

---

## 8. CONTEXT NOTES

- **This is the key test** for porting E₈ Koide to D₆
- **The E₈ mechanism is well-understood** — we're checking if D₆ has the same structure
- **Only leptons satisfy Koide** (Q = 2/3) — quarks use different Q values
- **Be thorough** — enumerate ALL A₂ triples, not just obvious ones
- **Negative results are valuable** — if D₆ doesn't have Koide structure, that's important

---

## 9. REFERENCE: E₈ LEPTON TRIPLE

For comparison, the E₈ lepton triple:

| Label | E₈ Coordinates | h | |ξ₅| |
|-------|----------------|---|-----|
| τ | (1, -1, 0, 0, 0, 0, 0, 0) | -2 | 1.050 |
| μ | (-1, 0, 1, 0, 0, 0, 0, 0) | +1 | 1.272 |
| e | (0, 1, -1, 0, 0, 0, 0, 0) | +1 | 1.044 |

**Properties**:
- All pairwise dots = -1 ✓
- Sum = 0 ✓
- Heights: τ at pole, μ and e in matter band
- Mass formula with θ₀ ≈ 347° gives <1% accuracy

**The D₆ analog should have similar structure** — one "heavy" root and two "light" roots forming a perfect A₂ triangle.

