# Delegation 21 - Iteration 1: Pyritohedral Coordinate Computation

## 1. BACKGROUND: The Pyritohedral Decomposition

### 1.1 The Regular Dodecahedron

A regular dodecahedron has **20 vertices** and **12 pentagonal faces**. It is one of the five Platonic solids and has **icosahedral symmetry** $I_h$ (order 120).

**Standard Coordinates**: The 20 vertices of a unit dodecahedron can be written as:
- 8 vertices: $(\pm 1, \pm 1, \pm 1)$ — a cube
- 12 vertices: $(0, \pm \phi, \pm 1/\phi)$, $(\pm 1/\phi, 0, \pm \phi)$, $(\pm \phi, \pm 1/\phi, 0)$

where $\phi = (1+\sqrt{5})/2$ is the golden ratio.

**Reference**: Coxeter, H.S.M. (1973). *Regular Polytopes*. Dover Publications.

### 1.2 The Pyritohedral Group $T_h$

The **pyritohedral group** $T_h$ is a subgroup of $I_h$ with **order 24**. It is the symmetry group of the pyritohedron (a distorted dodecahedron found in pyrite crystals).

$T_h$ can be described as:
$$T_h \cong A_4 \times C_2$$

where $A_4$ is the alternating group (tetrahedral rotations) and $C_2$ is inversion.

**Generators**:
- 3-fold rotation about body diagonal: $(x,y,z) \to (y,z,x)$
- 2-fold rotation about coordinate axis: $(x,y,z) \to (-x,-y,z)$
- Inversion: $(x,y,z) \to (-x,-y,-z)$

**Reference**: Koca, M. et al. (2011). "Catalan Solids Derived From 3D-Root Systems and Quaternions." *J. Math. Phys.* 52, 043507.

### 1.3 The 8+8+4 Decomposition

Under the action of $T_h$, the 20 vertices of the dodecahedron split into **three orbits**:

| Orbit | Size | Geometry | Description |
|-------|------|----------|-------------|
| **8_L** | 8 | Cube | Inscribed cube #1 (left-handed) |
| **8_R** | 8 | Cube | Inscribed cube #2 (right-handed) |
| **4_H** | 4 | Tetrahedron | Residual vertices |

**Geometric Picture**:
- Two cubes can be inscribed in a dodecahedron in "dual" orientations
- These correspond to the two chiral forms of the compound of five tetrahedra
- The 4 remaining vertices form a regular tetrahedron

**Physical Interpretation** (in particle physics models):
- **8_L**: Left-handed fermion states
- **8_R**: Right-handed fermion states
- **4_H**: Higgs doublet (2 complex = 4 real degrees of freedom)

**Reference**: 
- Koca, M. (2006). "Pyritohedral constructions of icosahedron, dodecahedron, pseudo-icosahedron and pyritohedron." *SQU Journal for Science*.
- Conway, J.H. & Smith, D.A. (2003). *On Quaternions and Octonions*. A K Peters.

### 1.4 The D₆ Lattice and ω₃ Orbit

The **D₆ root lattice** in $\mathbb{R}^6$ consists of vectors:
$$D_6 = \{ x \in \mathbb{Z}^6 : \sum_i x_i \equiv 0 \pmod{2} \}$$

The **ω₃ weight orbit** is the Weyl orbit of the third fundamental weight:
$$\omega_3 = (1, 1, 1, 0, 0, 0)$$

This orbit contains **160 weights** of squared length $|v|^2 = 3$.

### 1.5 The D₆ → H₃ Projection

The **Koca–Al-Siyabi projection** maps 6D to 3D with icosahedral (H₃) symmetry:

$$P_\parallel = \frac{1}{\sqrt{2(1+\phi^2)}} \begin{pmatrix} \phi & -\phi & 0 & 0 & 1 & -1 \\ 0 & 0 & \phi & -\phi & 0 & 0 \\ 1 & 1 & 1 & 1 & \phi & \phi \end{pmatrix}$$

Under this projection, the 160 ω₃ weights split into **4 shells**:

| Shell | $|v_\parallel|^2$ | Count | 3D Geometry |
|-------|-------------------|-------|-------------|
| **S₁** | 0.158 | 20 | Dodecahedron |
| **S₂** | 1.053 | 60 | Intermediate |
| **S₃** | 1.947 | 60 | Intermediate |
| **S₄** | 2.842 | 20 | Dodecahedron |

**Key Point**: The 20-vertex shells (S₁ and S₄) project to **dodecahedra** in 3D, which can be decomposed under $T_h$.

**Reference**: Koca, M. et al. (2020). "Icosahedral Polyhedra from D₆ Lattice and Danzer's ABCK Tiling." *Symmetry* 12, 1983.

---

## 2. THE TASK

### Goal A: Identify the S₁ and S₄ Shells

From the 160 ω₃ weights:
1. Project each weight to 3D using $P_\parallel$
2. Compute $|v_\parallel|^2$ for each
3. Identify the 20 weights with smallest $|v_\parallel|^2$ → **S₁**
4. Identify the 20 weights with largest $|v_\parallel|^2$ → **S₄**

### Goal B: Apply Pyritohedral Decomposition

For each dodecahedral shell (S₁ and S₄):

1. **Construct $T_h$ generators** acting on the projected 3D coordinates
2. **Find the three orbits** under $T_h$ action
3. **Identify**:
   - Which 8 vertices form 8_L (inscribed cube #1)
   - Which 8 vertices form 8_R (inscribed cube #2)
   - Which 4 vertices form 4_H (residual tetrahedron)

### Goal C: Report Full Coordinate Tables

For each set (8_L, 8_R, 4_H) in both S₁ and S₄, report:

| Index | 6D Coordinate | 3D Physical ($E_\parallel$) | 3D Internal ($E_\perp$) |
|-------|---------------|-----------------------------|-----------------------|
| 1 | [...] | [...] | [...] |
| ... | ... | ... | ... |

### Goal D: Verify Geometric Properties

Confirm:
1. **8_L forms a cube**: All 12 edges have equal length
2. **8_R forms a cube**: All 12 edges have equal length
3. **8_L and 8_R are "dual"**: Rotated by $\pi/4$ about a common axis
4. **4_H forms a tetrahedron**: All 6 edges have equal length

---

## 3. VERIFICATION CODE

```python
import numpy as np
from itertools import permutations, product
from collections import defaultdict

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# ============================================================
# PART 1: Standard Dodecahedron in 3D
# ============================================================

def standard_dodecahedron():
    """Generate the 20 vertices of a standard dodecahedron."""
    vertices = []
    
    # 8 cube vertices
    for signs in product([1, -1], repeat=3):
        vertices.append(list(signs))
    
    # 12 rectangular vertices
    coords = [
        (0, phi, 1/phi), (0, phi, -1/phi), (0, -phi, 1/phi), (0, -phi, -1/phi),
        (1/phi, 0, phi), (-1/phi, 0, phi), (1/phi, 0, -phi), (-1/phi, 0, -phi),
        (phi, 1/phi, 0), (phi, -1/phi, 0), (-phi, 1/phi, 0), (-phi, -1/phi, 0)
    ]
    vertices.extend(coords)
    
    return np.array(vertices)

print("Standard dodecahedron vertices:")
dodeca = standard_dodecahedron()
print(f"  Count: {len(dodeca)}")

# ============================================================
# PART 2: Pyritohedral Group T_h
# ============================================================

def generate_Th_group():
    """Generate the 24 elements of T_h as 3x3 matrices."""
    matrices = []
    
    # A_4 rotations (12 elements)
    # Identity
    I = np.eye(3)
    
    # 3-fold rotations about body diagonals (8 elements)
    rot3_1 = np.array([[0,1,0],[0,0,1],[1,0,0]])  # (xyz) -> (yzx)
    rot3_2 = np.array([[0,0,1],[1,0,0],[0,1,0]])  # (xyz) -> (zxy)
    
    # 2-fold rotations about coordinate axes (3 elements)
    rot2_x = np.diag([1,-1,-1])
    rot2_y = np.diag([-1,1,-1])
    rot2_z = np.diag([-1,-1,1])
    
    # Generate A_4 by combining these
    A4 = [I]
    for r in [rot3_1, rot3_2, rot2_x, rot2_y, rot2_z]:
        A4.append(r)
    
    # Generate full A_4 by closure
    while True:
        new = []
        for g1 in A4:
            for g2 in A4:
                prod = g1 @ g2
                is_new = True
                for g in A4 + new:
                    if np.allclose(prod, g):
                        is_new = False
                        break
                if is_new:
                    new.append(prod)
        if not new:
            break
        A4.extend(new)
    
    # T_h = A_4 × C_2 (add inversion)
    inversion = -np.eye(3)
    Th = []
    for g in A4:
        Th.append(g)
        Th.append(g @ inversion)
    
    return Th

Th = generate_Th_group()
print(f"\nPyritohedral group T_h:")
print(f"  Order: {len(Th)}")

# ============================================================
# PART 3: Find orbits under T_h
# ============================================================

def find_Th_orbits(vertices, Th):
    """Partition vertices into orbits under T_h action."""
    n = len(vertices)
    visited = [False] * n
    orbits = []
    
    for i in range(n):
        if visited[i]:
            continue
        orbit = [i]
        visited[i] = True
        
        for g in Th:
            v_transformed = g @ vertices[i]
            for j in range(n):
                if not visited[j] and np.allclose(v_transformed, vertices[j], atol=1e-10):
                    orbit.append(j)
                    visited[j] = True
                    break
        
        orbits.append(orbit)
    
    return orbits

orbits = find_Th_orbits(dodeca, Th)
print(f"\nOrbits under T_h:")
for i, orb in enumerate(orbits):
    print(f"  Orbit {i+1}: {len(orb)} vertices")

# ============================================================
# PART 4: D₆ → H₃ Projection
# ============================================================

# Koca-Al-Siyabi projection matrix (3x6)
P_par = (1/np.sqrt(2 * (1 + phi**2))) * np.array([
    [phi, -phi, 0, 0, 1, -1],
    [0, 0, phi, -phi, 0, 0],
    [1, 1, 1, 1, phi, phi]
])

# Internal projection (orthogonal complement)
U, S, Vt = np.linalg.svd(P_par.T)
P_perp = Vt[3:, :]  # 3x6

# ============================================================
# PART 5: Generate ω₃ Weyl Orbit
# ============================================================

def generate_omega3_orbit():
    """Generate the 160-point Weyl orbit of ω₃ under D₆."""
    weights = set()
    base = [1, 1, 1, 0, 0, 0]
    
    # All permutations
    for perm in permutations(base):
        # All sign changes (even number of minus signs for D₆)
        for signs in product([1, -1], repeat=6):
            if sum(1 for s in signs if s == -1) % 2 == 0:
                w = tuple(int(p * s) for p, s in zip(perm, signs))
                weights.add(w)
    
    return np.array(list(weights))

weights = generate_omega3_orbit()
print(f"\nω₃ Weyl orbit:")
print(f"  Count: {len(weights)}")

# Project to physical and internal space
v_par = weights @ P_par.T   # Nx3
v_perp = weights @ P_perp.T  # Nx3

# Compute squared lengths
r2_par = np.sum(v_par**2, axis=1)

# Identify shells
r2_unique = np.unique(np.round(r2_par, 6))
print(f"\nShell structure:")
for r2 in r2_unique:
    count = np.sum(np.abs(r2_par - r2) < 0.001)
    print(f"  |v_∥|² = {r2:.6f}: {count} points")

# Extract S₁ (smallest r²) and S₄ (largest r²)
min_r2, max_r2 = r2_unique[0], r2_unique[-1]
S1_mask = np.abs(r2_par - min_r2) < 0.001
S4_mask = np.abs(r2_par - max_r2) < 0.001

S1_weights = weights[S1_mask]
S1_v_par = v_par[S1_mask]
S4_weights = weights[S4_mask]
S4_v_par = v_par[S4_mask]

print(f"\nS₁ shell: {len(S1_weights)} points")
print(f"S₄ shell: {len(S4_weights)} points")

# ============================================================
# PART 6: Apply T_h to S₁ and S₄
# ============================================================

# Normalize S₁ vertices to unit dodecahedron scale for T_h analysis
S1_scale = np.sqrt(np.mean(np.sum(S1_v_par**2, axis=1)))
S1_normalized = S1_v_par / S1_scale

print(f"\nApplying T_h decomposition to S₁...")
S1_orbits = find_Th_orbits(S1_normalized, Th)
print(f"  Orbits found: {[len(o) for o in S1_orbits]}")

# Identify 8_L, 8_R, 4_H based on orbit sizes
for orb in S1_orbits:
    if len(orb) == 8:
        print(f"  8-vertex orbit (cube): indices {orb[:4]}...")
    elif len(orb) == 4:
        print(f"  4-vertex orbit (tetrahedron): indices {orb}")

# ============================================================
# PART 7: Output Tables
# ============================================================

print("\n" + "="*60)
print("S₁ SHELL DECOMPOSITION")
print("="*60)

for orbit_idx, orb in enumerate(S1_orbits):
    if len(orb) == 8:
        label = "8_L" if orbit_idx == 0 else "8_R"
    else:
        label = "4_H"
    
    print(f"\n{label} ({len(orb)} vertices):")
    print(f"{'Idx':<4} {'6D Coordinate':<30} {'3D Physical':<25} {'3D Internal':<25}")
    print("-" * 84)
    
    for i, idx in enumerate(orb):
        w6d = S1_weights[idx]
        v3d_par = S1_v_par[idx]
        v3d_perp = (weights @ P_perp.T)[S1_mask][idx]
        
        w6d_str = str(list(w6d))
        v3d_par_str = f"[{v3d_par[0]:.4f}, {v3d_par[1]:.4f}, {v3d_par[2]:.4f}]"
        v3d_perp_str = f"[{v3d_perp[0]:.4f}, {v3d_perp[1]:.4f}, {v3d_perp[2]:.4f}]"
        
        print(f"{i+1:<4} {w6d_str:<30} {v3d_par_str:<25} {v3d_perp_str:<25}")
```

---

## 4. DELIVERABLES

### Required Output

**Table 1: S₁ Shell (20 vertices)**

| Set | Index | 6D Coordinate | 3D Physical | 3D Internal |
|-----|-------|---------------|-------------|-------------|
| 8_L | 1 | [...] | [...] | [...] |
| ... | ... | ... | ... | ... |
| 8_R | 1 | [...] | [...] | [...] |
| ... | ... | ... | ... | ... |
| 4_H | 1 | [...] | [...] | [...] |
| ... | ... | ... | ... | ... |

**Table 2: S₄ Shell (20 vertices)** — Same format

**Verification Checks**:
| Property | S₁ Result | S₄ Result |
|----------|-----------|-----------|
| 8_L edge length | ? | ? |
| 8_R edge length | ? | ? |
| 8_L ⊥ 8_R angle | ? | ? |
| 4_H edge length | ? | ? |

---

## 5. REFERENCES

1. **Coxeter, H.S.M.** (1973). *Regular Polytopes*. Dover Publications.

2. **Koca, M. et al.** (2011). "Catalan Solids Derived From 3D-Root Systems and Quaternions." *J. Math. Phys.* 52, 043507.

3. **Koca, M.** (2006). "Pyritohedral constructions of icosahedron, dodecahedron, pseudo-icosahedron and pyritohedron." *SQU Journal for Science*.

4. **Koca, M. et al.** (2020). "Icosahedral Polyhedra from D₆ Lattice and Danzer's ABCK Tiling." *Symmetry* 12, 1983. https://doi.org/10.3390/sym12121983

5. **Conway, J.H. & Smith, D.A.** (2003). *On Quaternions and Octonions*. A K Peters.

6. **Humphreys, J.E.** (1990). *Reflection Groups and Coxeter Groups*. Cambridge University Press.

---

## 6. CONTEXT

This computation provides the **explicit particle-to-vertex mapping** for the Golden Selection theory:

- **8_L vertices** → Left-handed fermion quantum numbers
- **8_R vertices** → Right-handed fermion quantum numbers
- **4_H vertices** → Higgs doublet degrees of freedom

The coordinates in 6D (D₆ lattice) and their projections to 3D physical space ($E_\parallel$) and 3D internal space ($E_\perp$) are needed to:
1. Verify the pyritohedral decomposition works for D₆-projected dodecahedra
2. Establish explicit fermion assignments
3. Connect to the mass mechanism (internal depth $|v_\perp|^2$)

**Be thorough. Report all coordinates. Verify geometric properties.**
