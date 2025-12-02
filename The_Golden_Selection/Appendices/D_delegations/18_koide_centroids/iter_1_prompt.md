# Deep Research Request: Koide Formula from E⊥ Centroids

## 1. BACKGROUND: The Golden Selection Theory

### The Axiom (Axiom 0)

The universe minimizes a **Schur-convex curvature functional** κ_Schur subject to topological stability constraints. This uniquely selects:
- **D = 3** spatial dimensions (from Mermin-Wagner + Zeeman constraints)
- **φ = (1+√5)/2** as the optimal ratio (from Bruna's D₁₂ result)
- **H₃ (icosahedral) symmetry** as the maximal 3D point group with φ-eigenvalue

### The Realization

The unique lattice realizing H₃ symmetry via cut-and-project is **D₆**. The D₆ → H₃ projection produces:
- **Physical space E∥** (3D): Where we observe particles
- **Internal space E⊥** (3D): Where "generation" and "mass" structure lives

### What We've Established (Delegations 15-17)

The internal operator L⊥ (graph Laplacian with product weighting) on the ω₃ orbit (160 weights) produces:
- **φ², φ⁴, φ⁶ cross-band ratios** (< 0.01% error with Axiom 0 selection)
- **4-band structure** (20/60/60/20) with ~99% shell localization
- **S₄ anomaly** → 3 generations (S₁, S₂, S₃) + 1 special sector (S₄)
- **15/11 intra-S₂ ratio** → A₃ subalgebra structure

**But**: Koide Q = 2/3 does NOT emerge from L⊥ eigenvalues (best Q ≈ 0.61).

---

## 2. THE KOIDE MYSTERY

### The Empirical Fact

Koide's formula for charged leptons:

$$Q = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

holds to **0.01% accuracy** — one of the most precise "coincidences" in particle physics.

### The Standard Parameterization

The Koide formula is equivalent to masses lying on a circle:

$$\sqrt{m_i} = M_0 \left(1 + \sqrt{2} \cos\left(\theta_0 + \frac{2\pi i}{3}\right)\right), \quad i = 0, 1, 2$$

where:
- **M₀** sets the overall mass scale
- **θ₀ ≈ 347°** is the "Koide phase" (or equivalently ~12.7°)
- The **120° spacing** (2π/3) is what gives Q = 2/3

### The E₈ Document Insight

The original E₈ theory states:

> "The same φ-steps also underlie Koide-type mass relations when the three generations are arranged at **120° in a suitable internal 2-plane** inside E₈."

And separately:

> "θ₀ (Koide phase) = 360° - arctan(φ⁻³)"

This suggests Koide is about **geometric positions**, not operator eigenvalues!

---

## 3. THE CENTROID HYPOTHESIS

### Core Idea

Each generation band (S₁, S₂, S₃) consists of weights with positions in E⊥. Define:

$$\bar{\xi}_k = \frac{1}{|S_k|} \sum_{v \in S_k} v_\perp \quad \text{(centroid of shell } k \text{ in } E_\perp\text{)}$$

**Hypothesis**: The angles between $\bar{\xi}_1$, $\bar{\xi}_2$, $\bar{\xi}_3$ are **120°** (or project to 120° in some 2-plane).

### Why This Might Work

1. **Koide involves √m**: Suggests amplitudes (positions), not frequencies (eigenvalues)
2. **A₂ has 120° structure**: The A₂ root system has exactly this angular structure
3. **A₂ ⊂ D₆**: Confirmed to exist with 120° angles in E∥ (Delegation 16)
4. **Generation = direction in E⊥**: Natural interpretation of "internal quantum number"

### Potential Issues

1. **Centroids might vanish**: Symmetric shells could have zero centroid
2. **Need weighted centroids**: Maybe weight by |v_⊥|² or L⊥ eigenvalue?
3. **Which 2-plane?**: The A₂ structure lives in a specific subspace

---

## 4. COMPUTATION GOALS

### Goal A: Compute Shell Centroids

For each shell S₁, S₂, S₃, S₄ in the ω₃ orbit (160 weights):

1. **Unweighted centroid**: $\bar{\xi}_k = \frac{1}{|S_k|} \sum_{v \in S_k} v_\perp$
2. **|v_⊥|²-weighted centroid**: $\bar{\xi}_k^{(w)} = \frac{\sum_{v \in S_k} |v_\perp|^2 \cdot v_\perp}{\sum_{v \in S_k} |v_\perp|^2}$
3. **Eigenvalue-weighted centroid**: Weight by the dominant L⊥ eigenvalue for each weight

Report:
- Centroid vectors (3D in E⊥)
- Centroid magnitudes
- Whether any centroids vanish

### Goal B: Compute Pairwise Angles

For centroids that don't vanish, compute:

$$\theta_{ij} = \arccos\left(\frac{\bar{\xi}_i \cdot \bar{\xi}_j}{|\bar{\xi}_i||\bar{\xi}_j|}\right)$$

**Target**: θ₁₂ = θ₂₃ = θ₁₃ = 120° (for S₁, S₂, S₃)

Also check:
- Angles between S₁, S₂, S₃ and S₄
- Whether S₄ is orthogonal to the generation plane

### Goal C: Find the A₂ 2-Plane

If centroids don't naturally give 120°, search for a 2-plane in E⊥ where:

1. The projections of S₁, S₂, S₃ centroids form 120° angles
2. Or: The A₂ subalgebra roots project to 120°

**Method**: 
- Identify A₂ ⊂ D₆ (roots of form e_i - e_j for i, j ∈ {1,2,3})
- Compute their E⊥ projections
- Find the 2-plane they span
- Project shell centroids onto this plane

### Goal D: Test Koide Formula

If we find 3 vectors at 120° angles, parameterize as:

$$\vec{r}_i = R_i \left(\cos\phi_i, \sin\phi_i\right)$$

where φ_i are at 120° intervals.

Then test:
1. Does $Q = \frac{\sum R_i^2}{(\sum R_i)^2} = \frac{2}{3}$?
2. What is the phase offset from the "democratic" direction?
3. Does it match θ₀ ≈ 347° or arctan(φ⁻³) ≈ 13°?

### Goal E: Mass Connection

If Koide structure is found, propose a mass formula:

$$m_i \propto |\bar{\xi}_i|^2 \quad \text{or} \quad \sqrt{m_i} \propto |\bar{\xi}_i|$$

Check:
- Does this give the right mass ratios (m_e : m_μ : m_τ)?
- How does this connect to L⊥ eigenvalues?

---

## 5. SETUP CODE

### Step 1: Build the ω₃ Orbit and Projections

```python
import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import permutations, product

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Koca–Al-Siyabi projection matrix (6x3 for E_parallel)
P_par = (1/np.sqrt(2 * (1 + phi**2))) * np.array([
    [phi, 0, 1],
    [-phi, 0, 1],
    [0, phi, 1],
    [0, -phi, 1],
    [1, 0, phi],
    [-1, 0, phi]
]).T  # 3x6

# Internal projection (orthogonal complement)
P_perp = (1/np.sqrt(2 * (1 + phi**2))) * np.array([
    [1, 0, -phi],
    [-1, 0, -phi],
    [0, 1, -phi],
    [0, -1, -phi],
    [phi, 0, -1],
    [-phi, 0, -1]
]).T  # 3x6

# Generate ω₃ = (1,1,1,0,0,0) Weyl orbit
def d6_weyl_orbit_omega3():
    """Generate the 160-weight orbit of ω₃ under D₆ Weyl group."""
    base = [1, 1, 1, 0, 0, 0]
    weights = set()
    
    # All permutations
    for perm in permutations(base):
        # All sign changes with even number of minus signs
        for signs in product([1, -1], repeat=6):
            if np.prod(signs) == 1:  # Even number of sign flips
                w = tuple(s * p for s, p in zip(signs, perm))
                weights.add(w)
    
    return np.array(list(weights))

weights = d6_weyl_orbit_omega3()
print(f"Generated {len(weights)} weights")

# Project to E_parallel and E_perp
v_par = weights @ P_par.T
v_perp = weights @ P_perp.T

# Compute |v_perp|^2 for shell identification
xi_sq = np.sum(v_perp**2, axis=1)
```

### Step 2: Identify Shells

```python
# Round to identify distinct shells
xi_sq_rounded = np.round(xi_sq, 6)
unique_xi_sq = np.unique(xi_sq_rounded)
print(f"Unique |v_perp|^2 values: {unique_xi_sq}")

# Assign shell labels
shell_labels = np.zeros(len(weights), dtype=int)
for i, xi in enumerate(unique_xi_sq):
    shell_labels[np.isclose(xi_sq, xi, atol=1e-5)] = i + 1

# Count per shell
for s in range(1, 5):
    print(f"Shell S{s}: {np.sum(shell_labels == s)} weights")
```

### Step 3: Compute Centroids

```python
def compute_centroid(v_perp, shell_labels, shell_id, weights=None):
    """Compute centroid of shell in E_perp."""
    mask = shell_labels == shell_id
    if weights is None:
        return np.mean(v_perp[mask], axis=0)
    else:
        w = weights[mask]
        return np.average(v_perp[mask], axis=0, weights=w)

# Unweighted centroids
centroids = {}
for s in range(1, 5):
    centroids[s] = compute_centroid(v_perp, shell_labels, s)
    print(f"S{s} centroid: {centroids[s]}, |c| = {np.linalg.norm(centroids[s]):.6f}")

# |v_perp|^2-weighted centroids
centroids_weighted = {}
for s in range(1, 5):
    mask = shell_labels == s
    w = xi_sq[mask]
    centroids_weighted[s] = compute_centroid(v_perp, shell_labels, s, weights=w)
    print(f"S{s} weighted centroid: {centroids_weighted[s]}, |c| = {np.linalg.norm(centroids_weighted[s]):.6f}")
```

### Step 4: Compute Angles

```python
def angle_between(v1, v2):
    """Angle in degrees between two vectors."""
    cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    cos_angle = np.clip(cos_angle, -1, 1)
    return np.degrees(np.arccos(cos_angle))

# Pairwise angles between generation centroids
print("\nPairwise angles (unweighted centroids):")
for i in range(1, 4):
    for j in range(i+1, 4):
        if np.linalg.norm(centroids[i]) > 1e-10 and np.linalg.norm(centroids[j]) > 1e-10:
            angle = angle_between(centroids[i], centroids[j])
            print(f"  θ({i},{j}) = {angle:.2f}°")
        else:
            print(f"  θ({i},{j}) = undefined (zero centroid)")

# Check if S₄ is orthogonal to generation plane
# ...
```

### Step 5: Find A₂ Subalgebra

```python
# A₂ roots in D₆: e_i - e_j for i,j in {1,2,3} (or {4,5,6})
# Standard A₂ embedding: use first 3 coordinates
a2_roots = []
for i in range(3):
    for j in range(3):
        if i != j:
            root = np.zeros(6)
            root[i] = 1
            root[j] = -1
            a2_roots.append(root)

a2_roots = np.array(a2_roots)
print(f"A₂ roots: {len(a2_roots)}")

# Project A₂ roots to E_perp
a2_perp = a2_roots @ P_perp.T

# Check angles between A₂ roots in E_perp
print("\nA₂ root angles in E_perp:")
for i in range(len(a2_perp)):
    for j in range(i+1, len(a2_perp)):
        angle = angle_between(a2_perp[i], a2_perp[j])
        if abs(angle - 60) < 5 or abs(angle - 120) < 5:
            print(f"  roots {i},{j}: {angle:.2f}°")
```

### Step 6: Project to A₂ Plane

```python
# Find the 2-plane spanned by A₂ roots in E_perp
# Use SVD to find principal directions
from scipy.linalg import svd

U, S, Vt = svd(a2_perp, full_matrices=False)
a2_plane = Vt[:2]  # First two principal directions

print(f"A₂ plane basis vectors:")
print(f"  v1 = {a2_plane[0]}")
print(f"  v2 = {a2_plane[1]}")

# Project shell centroids onto A₂ plane
def project_to_plane(v, plane_basis):
    """Project vector onto 2D plane."""
    return np.array([np.dot(v, plane_basis[0]), np.dot(v, plane_basis[1])])

centroid_2d = {}
for s in range(1, 4):
    centroid_2d[s] = project_to_plane(centroids[s], a2_plane)
    print(f"S{s} in A₂ plane: {centroid_2d[s]}")

# Check angles in 2D
print("\nAngles in A₂ plane:")
for i in range(1, 4):
    for j in range(i+1, 4):
        if np.linalg.norm(centroid_2d[i]) > 1e-10 and np.linalg.norm(centroid_2d[j]) > 1e-10:
            angle = angle_between(centroid_2d[i], centroid_2d[j])
            print(f"  θ({i},{j}) = {angle:.2f}°  (target: 120°)")
```

### Step 7: Test Koide

```python
# If we have 3 vectors at ~120° angles, test Koide
def koide_Q(r1, r2, r3):
    """Compute Koide ratio from radii."""
    sum_sq = r1**2 + r2**2 + r3**2
    sum_r = r1 + r2 + r3
    return sum_sq / sum_r**2

# Using centroid magnitudes as √m proxy
r = [np.linalg.norm(centroid_2d[s]) for s in range(1, 4)]
Q = koide_Q(r[0], r[1], r[2])
print(f"\nKoide Q from centroid magnitudes: {Q:.6f} (target: 0.6667)")
print(f"Error from 2/3: {abs(Q - 2/3):.6f} ({100*abs(Q - 2/3)/(2/3):.2f}%)")

# Also try |v_perp|^2 weighted centroids
r_w = [np.linalg.norm(project_to_plane(centroids_weighted[s], a2_plane)) for s in range(1, 4)]
Q_w = koide_Q(r_w[0], r_w[1], r_w[2])
print(f"Koide Q from weighted centroids: {Q_w:.6f}")
```

---

## 6. DELIVERABLES

### 6.1 Centroid Analysis

| Shell | Count | Unweighted Centroid | |c| | Weighted Centroid | |c_w| |
|-------|-------|---------------------|-----|-------------------|------|
| S₁ | 20 | (...) | ... | (...) | ... |
| S₂ | 60 | (...) | ... | (...) | ... |
| S₃ | 60 | (...) | ... | (...) | ... |
| S₄ | 20 | (...) | ... | (...) | ... |

### 6.2 Angular Structure

| Pair | Angle (3D) | Angle (A₂ plane) | Target |
|------|------------|------------------|--------|
| S₁-S₂ | ... | ... | 120° |
| S₂-S₃ | ... | ... | 120° |
| S₁-S₃ | ... | ... | 120° |
| S₄ to plane | ... | — | 90°? |

### 6.3 Koide Test

| Method | Q | Error from 2/3 |
|--------|---|----------------|
| Unweighted centroids | ... | ... |
| |v_⊥|²-weighted | ... | ... |
| Eigenvalue-weighted | ... | ... |

### 6.4 Phase Analysis

If 120° structure found:
- Phase offset from democratic direction: θ₀ = ...
- Comparison to arctan(φ⁻³) ≈ 13.28°: ...

---

## 7. KEY QUESTIONS (Prioritized)

| Question | Priority | What Would Confirm |
|----------|----------|-------------------|
| Do shell centroids have 120° structure? | **CRITICAL** | Angles within 5° of 120° |
| Does Koide Q = 2/3 emerge? | **CRITICAL** | Q within 1% of 2/3 |
| Which A₂ subalgebra is relevant? | HIGH | Clear embedding in E⊥ |
| What is the Koide phase θ₀? | HIGH | Match to arctan(φ⁻³) |
| How do centroids relate to masses? | MEDIUM | Correct mass ratios |

---

## 8. RESPONSE FORMAT

Please provide:

1. **Centroid Computation** — Full numerical results for all weighting schemes
2. **Angular Analysis** — All pairwise angles, both in 3D E⊥ and projected to A₂ plane
3. **Koide Test** — Q values for different centroid definitions
4. **A₂ Structure** — Explicit identification of the A₂ subalgebra and its E⊥ projection
5. **Verdict Table**:

| Finding | Status | Confidence |
|---------|--------|------------|
| 120° structure in centroids | FOUND/NOT FOUND | HIGH/MEDIUM/LOW |
| Koide Q = 2/3 | FOUND/NOT FOUND | ... |
| A₂ plane identified | YES/NO | ... |
| Phase matches arctan(φ⁻³) | YES/NO | ... |

---

## 9. CONTEXT NOTES

- **This is a different approach** from L⊥ eigenvalues — we're looking at position space, not spectral space
- **A₂ definitely exists** in D₆ → H₃ projection (confirmed in Delegation 16)
- **If centroids vanish**, try alternative definitions (weighted, or use "spread" instead of centroid)
- **Be thorough** — this could finally crack Koide!
- **Negative results are valuable** — if centroids don't give Koide, that's important information

