# Computation Request: Internal Operator L⊥ on D₆→H₃ Quasicrystal

## 1. BACKGROUND

### The Golden Selection Framework

The Golden Selection theory derives physics from a D₆ → H₃ quasicrystal projection:

- **D₆ lattice** in 6D splits into **E∥** (physical 3D) and **E⊥** (internal 3D)
- Projection uses the **Koca–Al-Siyabi matrix** with golden ratio φ built in
- The 60 D₆ roots project to two **icosidodecahedral shells** (30+30 vertices)
- Shell radii ratio = φ (golden ratio)

### What We've Established (Delegation 15)

Using a "zig-zag" mass functional $\mathcal{M}_f^2 = \frac{\sum |\alpha_\perp|^2}{\sum |\alpha_\parallel|^2}$, we found:

| Shell | $\mathcal{M}^2$ |
|-------|-----------------|
| Outer roots (SU(2)) | φ⁻² |
| Inner roots (SU(3)) | φ² |
| ω₃ 20-shell (small) | φ⁶ |
| ω₃ 20-shell (large) | φ⁻⁶ |

**Problem**: This gives φ-powers, but not specific SM mass ratios. The functional is ad-hoc.

### The New Approach

Instead of guessing mass formulas, define a **single internal operator L⊥** whose eigenvalues ARE the masses:

$$L_\perp \psi_f = \lambda_f \psi_f \quad \Rightarrow \quad m_f^2 \propto \lambda_f$$

This operator should be:
1. **Local** — built from quasicrystal graph connectivity
2. **Symmetric** — respects D₆/H₃ symmetry
3. **Selected by Axiom 0** — extremizes Schur-convex curvature

---

## 2. THE COMPUTATION GOAL

**Build a toy L⊥ operator on a finite D₆→H₃ patch and compute its spectrum.**

Specifically:
1. Construct the D₆→H₃ quasicrystal graph (vertices + edges)
2. Define L⊥ as a simple internal Laplacian
3. Compute eigenvalues numerically
4. Check if eigenvalue ratios match φ², φ⁶, or SM-like patterns

---

## 3. INPUTS

### 3.1 The Koca–Al-Siyabi Projection Matrix

$$P_\parallel = \frac{1}{\sqrt{5+\sqrt{5}}} \begin{pmatrix} 1 & -1 & 0 & 0 & \phi & -\phi \\ \phi & \phi & 1 & 1 & 0 & 0 \\ 0 & 0 & \phi & -\phi & 1 & 1 \end{pmatrix}$$

where $\phi = \frac{1+\sqrt{5}}{2}$.

### 3.2 D₆ Root System

$$\Phi(D_6) = \{\pm e_i \pm e_j : 1 \le i < j \le 6\}$$

60 roots, each with $|\alpha|^2 = 2$.

### 3.3 D₆ Fundamental Weights

- $\omega_1 = (1, 0, 0, 0, 0, 0)$
- $\omega_2 = (1, 1, 0, 0, 0, 0)$
- $\omega_3 = (1, 1, 1, 0, 0, 0)$ — generates 160-weight orbit
- $\omega_4 = (1, 1, 1, 1, 0, 0)$
- $\omega_5 = (1/2, 1/2, 1/2, 1/2, 1/2, -1/2)$
- $\omega_6 = (1/2, 1/2, 1/2, 1/2, 1/2, 1/2)$

---

## 4. STEP-BY-STEP COMPUTATION

### Step 1: Construct the Quasicrystal Graph

**Option A: Use D₆ roots as vertices**
- 60 vertices (the D₆ roots)
- Project each to E∥ and E⊥
- Define edges: connect roots α, β if they are "neighbors" in some sense

**Option B: Use a model set (cut-and-project)**
- Start with D₆ lattice points in a ball of radius R
- Apply acceptance window in E⊥
- Project accepted points to E∥
- Connect nearest neighbors in E∥

For simplicity, start with **Option A** (60-vertex graph from roots).

**Neighborhood definition**: Two roots α, β are neighbors if:
- $|\alpha - \beta|^2 \le 4$ (i.e., they differ by at most another root), OR
- Their E∥ projections are within some threshold distance

### Step 2: Define the Internal Laplacian L⊥

**Simple Definition**:

For each vertex (root) α, define an internal coordinate:
$$\xi_\alpha = |\alpha_\perp|^2 = |P_\perp \alpha|^2$$

This is the "internal depth" of the root.

**Graph Laplacian with internal weighting**:

$$(L_\perp \psi)_\alpha = \sum_{\beta \sim \alpha} w_{\alpha\beta} (\psi_\alpha - \psi_\beta)$$

where:
- $\beta \sim \alpha$ means β is a neighbor of α
- $w_{\alpha\beta}$ is a weight depending on internal coordinates

**Weight options**:

1. **Uniform**: $w_{\alpha\beta} = 1$ (standard graph Laplacian)

2. **Internal-weighted**: $w_{\alpha\beta} = \frac{|\alpha_\perp|^2 + |\beta_\perp|^2}{2}$

3. **Difference-weighted**: $w_{\alpha\beta} = ||\alpha_\perp|^2 - |\beta_\perp|^2|$

4. **Product-weighted**: $w_{\alpha\beta} = |\alpha_\perp|^2 \cdot |\beta_\perp|^2$

Try all four and compare spectra.

### Step 3: Compute the Spectrum

For each L⊥ definition:
1. Build the 60×60 matrix
2. Compute eigenvalues $\lambda_1 \le \lambda_2 \le \cdots \le \lambda_{60}$
3. Record the spectrum

### Step 4: Analyze the Spectrum

**Questions to answer**:

1. **Degeneracy structure**: How many distinct eigenvalues? What are the multiplicities?
   - Expected: degeneracies matching D₆/H₃ orbit sizes (30, 20, 12, etc.)

2. **φ-structure**: Do eigenvalue ratios involve φ?
   - Compute $\lambda_i / \lambda_j$ for all pairs
   - Check if any equal φ, φ², φ³, φ⁻¹, etc.

3. **Shell correspondence**: 
   - The 60 roots split into two shells (inner/outer, 30 each)
   - Do eigenvectors localize on one shell or the other?
   - What are the eigenvalues associated with each shell?

4. **Comparison to zig-zag functional**:
   - We know $\mathcal{M}^2_{\text{outer}} = \phi^{-2}$, $\mathcal{M}^2_{\text{inner}} = \phi^{2}$
   - Does any eigenvalue ratio equal φ⁴ (the ratio of these)?

### Step 5: Extend to ω₃ Weight Orbit (Optional)

If time permits, repeat for the 160-weight ω₃ orbit:
1. Generate all 160 weights
2. Build graph (neighbors in E∥)
3. Define L⊥ with internal weighting
4. Compute spectrum
5. Check for φ⁶ structure (matching the 20-shell mass functional)

---

## 5. EXPECTED OUTPUTS

### 5.1 The Graph

```
Number of vertices: 60
Number of edges: ???
Average degree: ???
```

### 5.2 Spectrum for Each L⊥ Definition

| Weighting | Distinct eigenvalues | Largest | Smallest (nonzero) | Ratio max/min |
|-----------|---------------------|---------|-------------------|---------------|
| Uniform | ? | ? | ? | ? |
| Internal-weighted | ? | ? | ? | ? |
| Difference-weighted | ? | ? | ? | ? |
| Product-weighted | ? | ? | ? | ? |

### 5.3 Eigenvalue Ratios

For each L⊥, list any eigenvalue ratios that are close to:
- φ ≈ 1.618
- φ² ≈ 2.618
- φ³ ≈ 4.236
- φ⁴ ≈ 6.854
- φ⁶ ≈ 17.944
- 15/11 ≈ 1.364
- 2/3 ≈ 0.667 (Koide)

### 5.4 Shell Localization

For each eigenvector, compute:
$$\text{Inner fraction} = \frac{\sum_{\alpha \in \text{inner}} |\psi_\alpha|^2}{\sum_{\alpha} |\psi_\alpha|^2}$$

Report which eigenvalues have eigenvectors localized on:
- Inner shell only (fraction > 0.9)
- Outer shell only (fraction < 0.1)
- Delocalized (fraction ≈ 0.5)

### 5.5 Algebraic Structure (If Clean)

If any eigenvalues have simple algebraic forms, express them in terms of φ.

---

## 6. CODE SKELETON

```python
import numpy as np
from scipy.linalg import eigh
from itertools import combinations

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Koca-Al-Siyabi projection matrix
norm = np.sqrt(5 + np.sqrt(5))
P_parallel = np.array([
    [1, -1, 0, 0, phi, -phi],
    [phi, phi, 1, 1, 0, 0],
    [0, 0, phi, -phi, 1, 1]
]) / norm

# Compute P_perp (orthogonal complement)
# Use SVD to find null space of P_parallel
U, S, Vt = np.linalg.svd(P_parallel)
P_perp = Vt[3:, :]  # Last 3 rows of Vt

# Generate D6 roots
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
print(f"Number of D6 roots: {len(roots)}")

# Project roots
roots_parallel = roots @ P_parallel.T
roots_perp = roots @ P_perp.T

# Internal squared lengths
xi = np.sum(roots_perp**2, axis=1)

# Build adjacency matrix
def build_adjacency(roots, threshold=4.0):
    n = len(roots)
    adj = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            diff = roots[i] - roots[j]
            if np.sum(diff**2) <= threshold:
                adj[i, j] = 1
                adj[j, i] = 1
    return adj

adj = build_adjacency(roots)
print(f"Number of edges: {int(np.sum(adj) / 2)}")
print(f"Average degree: {np.mean(np.sum(adj, axis=1))}")

# Build Laplacian with different weightings
def build_laplacian(adj, xi, weighting='uniform'):
    n = len(xi)
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if adj[i, j] > 0:
                if weighting == 'uniform':
                    w = 1.0
                elif weighting == 'internal':
                    w = (xi[i] + xi[j]) / 2
                elif weighting == 'difference':
                    w = abs(xi[i] - xi[j])
                elif weighting == 'product':
                    w = xi[i] * xi[j]
                else:
                    w = 1.0
                
                L[i, j] = -w
                L[i, i] += w
    
    return L

# Compute spectra for all weightings
weightings = ['uniform', 'internal', 'difference', 'product']
for w in weightings:
    L = build_laplacian(adj, xi, weighting=w)
    eigenvalues, eigenvectors = eigh(L)
    
    print(f"\n=== {w.upper()} WEIGHTING ===")
    print(f"Eigenvalues: {eigenvalues[:10]}...")  # First 10
    print(f"Nonzero eigenvalues: {eigenvalues[eigenvalues > 1e-10]}")
    
    # Check for phi-ratios
    nonzero = eigenvalues[eigenvalues > 1e-10]
    if len(nonzero) >= 2:
        ratio = nonzero[-1] / nonzero[0]
        print(f"Max/min ratio: {ratio}")
        print(f"log_phi(ratio): {np.log(ratio) / np.log(phi)}")

# Shell localization analysis
# ... (extend as needed)
```

---

## 7. SUCCESS CRITERIA

| Outcome | Meaning |
|---------|---------|
| Spectrum has φ-power ratios | Geometry is controlling eigenvalues ✅ |
| Eigenvectors localize on shells | Shells are dynamically meaningful ✅ |
| Eigenvalue ratio ≈ φ⁴ | Matches zig-zag functional prediction ✅ |
| No φ-structure at all | L⊥ definition needs refinement ⚠️ |
| Eigenvalue ratio ≈ 15/11 | Unexpected bonus! 🎉 |

---

## 8. CONTEXT NOTES

- **This is exploratory**: We're testing whether L⊥ is a viable path, not expecting final answers.
- **Simplicity first**: Start with the simplest definitions; complexity can come later.
- **Report everything**: Even "boring" results (like uniform spectrum) are informative.
- **φ is the target**: If eigenvalue ratios involve φ, we're on the right track.

The goal is to see if the **spectrum of a natural internal operator** reproduces the φ-hierarchy we found with the ad-hoc zig-zag functional. If it does, we have a principled mass mechanism. If not, we learn what's missing.

---

## 9. REFERENCES

1. **Delegation 15**: Mass mechanism results (φ², φ⁻², φ⁶, φ⁻⁶ for shells)
2. **Delegation 10**: D₆→H₃ shell structure
3. **Koca et al. (2020)**: "Icosahedral Polyhedra from D₆ Lattice" — projection matrix
4. **Baggioli & Landry (2020)**: Phason EFT — for physical interpretation

