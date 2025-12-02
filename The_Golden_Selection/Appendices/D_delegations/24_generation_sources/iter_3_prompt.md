# Delegation 24 - Iteration 3: Spectral Analysis of the Three-Domain Potential

## 1. BACKGROUND: What We've Established

### 1.1 The Generation Mechanism (Iterations 1-2)

We've confirmed that the D₆ → H₃ quasicrystal has **three Occupation Domains** in internal space (E⊥):

| Domain | Position in E⊥ | Physical Role |
|--------|----------------|---------------|
| **Core** | Deep (center) | Cluster centers |
| **Shell** | Middle | Standard framework |
| **Skin** | Shallow (outer) | Boundary/glue |

### 1.2 The Spectral Hypothesis

The three generations are **NOT** spatially separated. Instead:

> **3 Generations = 3 lowest-energy eigenmodes** of the spinor field interacting with the three-domain potential.

The spinor weights land in the "voids" (Voronoi centers) of the D₆ lattice, where they feel the combined potential from all three domain types.

### 1.3 The φ³ Volume Ratios

The volumes of the three domains scale by powers of φ³:
$$\frac{V_{Core}}{V_{Shell}} \sim \phi^{-3}, \quad \frac{V_{Shell}}{V_{Skin}} \sim \phi^{-3}$$

This suggests the **mass hierarchy** is encoded in the geometry.

---

## 2. THE TASK

We need to **calculate the spectrum** of an appropriate operator on the ω₅ spinor orbit, incorporating the three-domain structure.

### 2.1 The Setup

**Spinor orbit**: ω₅ = 32 half-integer weights
$$\omega_5 = \{\tfrac{1}{2}(\pm 1, \pm 1, \pm 1, \pm 1, \pm 1, \pm 1) : \text{odd number of minus signs}\}$$

**Projection matrices** (Koca–Al-Siyabi):
- Physical: P∥ (3×6)
- Internal: P⊥ (3×6, orthogonal complement)

**Three domains** in E⊥:
- Core: |x⊥| < r₁
- Shell: r₁ < |x⊥| < r₂  
- Skin: r₂ < |x⊥| < r₃

### 2.2 The Operator

We want to study a **Laplacian-like operator** on the spinor orbit, modified by the three-domain potential.

**Option A: Graph Laplacian with Domain-Dependent Weights**

Define a graph where:
- Nodes = 32 spinor weights
- Edges = connect weights that are "neighbors" (e.g., differ by one sign flip)
- Edge weights = depend on which domain(s) the endpoints occupy

The Laplacian:
$$L_{ij} = \begin{cases} -w_{ij} & i \neq j, \text{ connected} \\ \sum_k w_{ik} & i = j \\ 0 & \text{otherwise} \end{cases}$$

**Option B: Discrete Schrödinger Operator**

$$H = L_0 + V$$

where:
- L₀ = standard graph Laplacian on ω₅
- V = diagonal potential based on E⊥ position

$$V_{ii} = V(x_i^\perp) = \begin{cases} V_{Core} & x_i \in \text{Core} \\ V_{Shell} & x_i \in \text{Shell} \\ V_{Skin} & x_i \in \text{Skin} \end{cases}$$

**Option C: Internal-Space Laplacian (L⊥)**

From Delegation 16, we defined L⊥ as the graph Laplacian in internal space. Apply this to ω₅ and check for 3-band structure.

---

## 3. SPECIFIC QUESTIONS

### Q1: Does L⊥ on ω₅ Show 3 Bands?

In Delegation 16, L⊥ on ω₃ (160 weights) gave **4 bands**.

**Task**: Compute L⊥ on ω₅ (32 weights).
- How many spectral bands?
- Are there exactly 3 low-energy bands?
- What are the eigenvalue ratios?

### Q2: Do the Bands Correspond to Domains?

If we get 3 bands:
- Do the eigenvectors localize on specific domains (Core, Shell, Skin)?
- Or are they delocalized across all three?

### Q3: Are the Eigenvalue Ratios φ-Related?

Check if:
$$\frac{\lambda_2}{\lambda_1} \sim \phi^k, \quad \frac{\lambda_3}{\lambda_2} \sim \phi^k$$

for some power k (possibly k=3, matching volume ratios).

### Q4: Does Adding a Domain Potential Change the Picture?

Compare:
1. **Bare L⊥** (no potential)
2. **L⊥ + V** (with domain-dependent potential)

Does the potential sharpen the 3-band structure?

---

## 4. COMPUTATIONAL TASKS

### Task A: Build the ω₅ Graph

```python
import numpy as np
from itertools import product

phi = (1 + np.sqrt(5)) / 2

# Generate ω₅ spinor weights
def get_omega5():
    weights = []
    for signs in product([1, -1], repeat=6):
        if np.prod(signs) == -1:  # Odd parity
            weights.append(0.5 * np.array(signs))
    return np.array(weights)

omega5 = get_omega5()  # Shape: (32, 6)

# Define adjacency: connect weights that differ by 2 sign flips
def build_adjacency(weights):
    n = len(weights)
    adj = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            # Count differing signs
            diff = np.sum(weights[i] != weights[j])
            if diff == 2:  # Adjacent in spinor graph
                adj[i, j] = adj[j, i] = 1
    return adj

adj = build_adjacency(omega5)
```

### Task B: Compute Internal Projections

```python
# Koca projection matrix
P_par = (1/np.sqrt(2 * (1 + phi**2))) * np.array([
    [phi, -phi, 0, 0, 1, -1],
    [0, 0, phi, -phi, 0, 0],
    [1, 1, 1, 1, phi, phi]
])

# Get P_perp via SVD
U, S, Vt = np.linalg.svd(P_par.T)
P_perp = Vt[3:, :]

# Project spinors to internal space
omega5_perp = omega5 @ P_perp.T  # Shape: (32, 3)

# Compute internal radii
r_perp = np.linalg.norm(omega5_perp, axis=1)
```

### Task C: Assign Domain Labels

```python
# Find natural domain boundaries
# (Use clustering or percentile-based thresholds)
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
domain_labels = kmeans.fit_predict(omega5_perp)

# Or use radial thresholds
r_sorted = np.sort(r_perp)
r1 = np.percentile(r_perp, 33)
r2 = np.percentile(r_perp, 67)

def assign_domain(r):
    if r < r1:
        return 0  # Core
    elif r < r2:
        return 1  # Shell
    else:
        return 2  # Skin
```

### Task D: Build and Diagonalize L⊥

```python
# Graph Laplacian
degree = np.sum(adj, axis=1)
L = np.diag(degree) - adj

# Diagonalize
eigenvalues, eigenvectors = np.linalg.eigh(L)

# Sort by eigenvalue
idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Eigenvalues:", eigenvalues[:10])
```

### Task E: Add Domain Potential

```python
# Define potential values
V_core = 0.0   # Reference
V_shell = 1.0  # Intermediate
V_skin = 2.0   # Highest

# Build potential matrix
V = np.zeros(32)
for i, r in enumerate(r_perp):
    V[i] = V_core if r < r1 else (V_shell if r < r2 else V_skin)

# Schrödinger operator
H = L + np.diag(V)

# Diagonalize
eig_H, vec_H = np.linalg.eigh(H)
print("Eigenvalues with potential:", eig_H[:10])
```

### Task F: Analyze Eigenvector Localization

```python
# For each eigenvector, compute "participation" in each domain
def domain_participation(eigenvector, domain_labels):
    participation = np.zeros(3)
    for d in range(3):
        mask = domain_labels == d
        participation[d] = np.sum(eigenvector[mask]**2)
    return participation / np.sum(eigenvector**2)

for i in range(5):
    print(f"Eigenvector {i}: {domain_participation(eigenvectors[:, i], domain_labels)}")
```

---

## 5. EXPECTED OUTCOMES

### Scenario A: Clear 3-Band Structure

If we find:
- 3 distinct low-energy bands
- Each band localized on one domain
- φ-related eigenvalue ratios

**Conclusion**: The spectral mechanism works! Generations = eigenmodes.

### Scenario B: More Than 3 Bands

If we find 4+ bands (like ω₃):
- The "3" may come from a different principle
- Or need to identify which 3 bands are "physical"

### Scenario C: No Clear Band Structure

If eigenvalues are continuous/degenerate:
- The spectral mechanism needs refinement
- May need different operator or potential

---

## 6. CONNECTION TO MASS HIERARCHY

If eigenvalues λ₁ < λ₂ < λ₃ correspond to generations 1, 2, 3:

**Hypothesis**: Mass ∝ eigenvalue (or some function thereof)

Check if:
$$\frac{m_\tau}{m_\mu} \approx \frac{\lambda_3}{\lambda_2}, \quad \frac{m_\mu}{m_e} \approx \frac{\lambda_2}{\lambda_1}$$

Or if the ratios are φ-powers:
$$\frac{\lambda_2}{\lambda_1} \sim \phi^3, \quad \frac{\lambda_3}{\lambda_2} \sim \phi^3$$

---

## 7. DELIVERABLES

Please provide:

1. **Eigenvalue spectrum** of L⊥ on ω₅ (all 32 eigenvalues)
2. **Band structure analysis**: How many distinct bands? Gaps?
3. **Eigenvector localization**: Which domains do low eigenvectors prefer?
4. **φ-ratio check**: Are eigenvalue ratios related to φ?
5. **Effect of potential**: Does adding V sharpen the structure?
6. **Generation assignment**: Can we identify 3 "generation eigenmodes"?

---

## 8. RESPONSE FORMAT

```
## EXECUTIVE SUMMARY
[Does L⊥ on ω₅ show 3 bands corresponding to 3 generations?]

## 1. EIGENVALUE SPECTRUM
| Index | Eigenvalue | Band | Domain Localization |
|-------|------------|------|---------------------|
| 0 | λ₀ | ? | Core/Shell/Skin |
| 1 | λ₁ | ? | ... |
| ... | ... | ... | ... |

## 2. BAND STRUCTURE
| Band | Eigenvalue Range | # States | Interpretation |
|------|------------------|----------|----------------|
| 1 | [λ_min, λ_max] | ? | Generation 1? |
| 2 | ... | ? | Generation 2? |
| 3 | ... | ? | Generation 3? |

## 3. φ-RATIO ANALYSIS
| Ratio | Value | Closest φ-power | Error |
|-------|-------|-----------------|-------|
| λ₂/λ₁ | ? | φ^? | ?% |
| λ₃/λ₂ | ? | φ^? | ?% |

## 4. POTENTIAL EFFECT
[Does adding domain potential improve the 3-band structure?]

## 5. VERDICT
[ ] Clear 3-band structure → Generations = eigenmodes
[ ] Partial structure → Mechanism plausible but needs work
[ ] No clear structure → Need different approach
```

