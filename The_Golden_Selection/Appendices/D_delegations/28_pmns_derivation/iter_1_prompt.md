# Delegation 28: PMNS Matrix from Face Geometry

## 1. BACKGROUND: The Golden Selection Theory

### 1.1 The Framework

The Golden Selection theory derives particle physics from the D₆ lattice projected to 3D via H₃ (icosahedral) symmetry. Key established results:

**Charged Leptons (Vertex Geometry)**:
- Mass formula: $m_i = M_0 (1 + \sqrt{2} \cos(\theta_0 + 2\pi i/3))^2$
- Koide parameter: Q = 2/3 (from A₂ cone condition)
- Phase: θ₀ = 2/9 radians ≈ 12.73°
- Amplitude: ε = √2 ≈ 1.414

**Neutrinos (Face Geometry)**:
- Live on the **dual lattice** (weights vs roots)
- Rotated by **30° (π/6)** from charged leptons
- Q ≈ 1/3 (near-degenerate)
- Mass scale: M_ν = M_ch / φ^48 ≈ 0.029 eV

### 1.2 The Problem

We have the **shape** (phase ≈ π/6) and **scale** (φ^(-48)) for neutrinos, but we lack:
1. The correct **amplitude ε** for neutrinos
2. Derivation of the **PMNS mixing angles** from geometry

### 1.3 Experimental Data (PDG 2024)

**Neutrino Masses** (Normal Ordering):
- Δm²₂₁ = 7.53 × 10⁻⁵ eV² (solar)
- Δm²₃₁ = 2.453 × 10⁻³ eV² (atmospheric)
- Ratio: Δm²₃₁/Δm²₂₁ ≈ **32.6**
- Sum: Σm_ν < 0.12 eV (Planck bound)

**PMNS Mixing Angles**:
- θ₁₂ = 33.41° ± 0.75° (solar angle)
- θ₂₃ = 49.1° ± 1.0° (atmospheric angle, Normal Ordering)
- θ₁₃ = 8.54° ± 0.12° (reactor angle)
- δ_CP ≈ 197° (CP phase, poorly constrained)

---

## 2. THE CORE QUESTIONS

### Question A: What is the Neutrino Amplitude?

For charged leptons, ε = √2 is fixed by the Koide constraint Q = 2/3.

**For neutrinos with Q ≈ 1/3, what determines ε?**

The Koide formula is:
$$m_i = M_0 (1 + \varepsilon \cos(\theta + 2\pi i/3))^2$$

The Q parameter relates to ε via:
$$Q = \frac{\sum m_i}{(\sum \sqrt{m_i})^2} = \frac{1 + \varepsilon^2/2}{3}$$

For Q = 2/3: ε = √2
For Q = 1/3: ε = ?

**Task A1**: Solve for ε given Q = 1/3.

**Task A2**: If Q = 1/3 gives ε = 0 (degenerate), what small perturbation produces the observed ratio 32.6?

### Question B: The Phase-Amplitude Consistency

We have claimed θ ≈ π/6 + small correction.

**Task B1**: Given the experimental mass ratio 32.6, perform a 2D search over (θ, ε) to find ALL solutions that reproduce this ratio.

**Task B2**: For each solution, compute:
- The three masses (relative)
- The Q parameter
- Whether any mass term T = 1 + ε·cos(phase) is negative

**Task B3**: Identify which solution(s) have geometric meaning in D₆/H₃.

### Question C: The PMNS Structure

The PMNS matrix connects flavor and mass eigenstates:
$$\begin{pmatrix} \nu_e \\ \nu_\mu \\ \nu_\tau \end{pmatrix} = U_{PMNS} \begin{pmatrix} \nu_1 \\ \nu_2 \\ \nu_3 \end{pmatrix}$$

Standard parameterization:
$$U = \begin{pmatrix} 
c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta} \\
-s_{12}c_{23} - c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23} - s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13} \\
s_{12}s_{23} - c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23} - s_{12}c_{23}s_{13}e^{i\delta} & c_{23}c_{13}
\end{pmatrix}$$

**Task C1**: In the D₆ → H₃ projection, what geometric angles exist between:
- The Vertex sublattice (charged leptons)
- The Face sublattice (neutrinos)
- The three generation domains (A, B, C occupation domains)

**Task C2**: The CKM matrix for quarks was derived from wavefunction overlaps with φ-scaled widths. Can the same mechanism work for PMNS?

**Task C3**: Literature suggests PMNS may have A₄ (tetrahedral) symmetry. Does A₄ ⊂ H₃? What angles does A₄ produce?

---

## 3. SPECIFIC NUMERICAL TASKS

### Task 1: Amplitude from Q

```python
import numpy as np

# From Koide: Q = (1 + eps^2/2) / 3
# Solve for eps given Q

def eps_from_Q(Q):
    """Calculate amplitude from Koide Q parameter."""
    eps_squared = 2 * (3*Q - 1)
    if eps_squared < 0:
        return None  # No real solution
    return np.sqrt(eps_squared)

print("Q = 2/3 (charged):", eps_from_Q(2/3))
print("Q = 1/3 (neutral?):", eps_from_Q(1/3))
print("Q = 0.337 (fitted):", eps_from_Q(0.337))
```

### Task 2: 2D Parameter Search

```python
import numpy as np

def compute_ratio(theta_rad, eps):
    """
    Compute Δm²₃₁/Δm²₂₁ for given (θ, ε).
    Returns ratio, masses, Q, and whether any T < 0.
    """
    phases = theta_rad + 2*np.pi*np.arange(3)/3
    T = 1 + eps * np.cos(phases)
    
    # Mass formula: m = T²
    m = T**2
    m_sorted = np.sort(m)
    
    # Compute mass splittings (assuming m represents mass, not mass²)
    dm21 = m_sorted[1] - m_sorted[0]
    dm31 = m_sorted[2] - m_sorted[0]
    
    ratio = dm31 / dm21 if dm21 > 1e-12 else np.inf
    
    # Compute Q
    sqrt_m = np.sqrt(m)
    Q = np.sum(m) / np.sum(sqrt_m)**2
    
    return ratio, m_sorted, Q, np.any(T < 0)

# Search the (θ, ε) space
target_ratio = 32.6
solutions = []

for theta_deg in np.linspace(0, 60, 600):
    for eps in np.linspace(0.01, 3.0, 300):
        theta_rad = np.radians(theta_deg)
        ratio, masses, Q, has_negative = compute_ratio(theta_rad, eps)
        
        if abs(ratio - target_ratio) < 0.5:
            solutions.append({
                'theta': theta_deg,
                'eps': eps,
                'ratio': ratio,
                'Q': Q,
                'negative_T': has_negative
            })

# Print solutions grouped by (θ, negative_T)
print(f"Found {len(solutions)} solutions with ratio ≈ 32.6")
# Show representative samples
```

### Task 3: Geometric Angle Analysis

```python
import numpy as np

phi = (1 + np.sqrt(5)) / 2

# Key angles in H₃/D₆ geometry
angles = {
    'pi/6 (Face offset)': 30,
    'pi/9': 20,
    '2/9 rad': np.degrees(2/9),
    'arctan(phi^-1)': np.degrees(np.arctan(1/phi)),
    'arctan(phi^-3)': np.degrees(np.arctan(phi**-3)),
    '45 - arctan(phi^-1)': 45 - np.degrees(np.arctan(1/phi)),
    'theta_13': 8.54,
    'theta_12': 33.41,
    'theta_23': 49.1,
}

print("Key angles in the theory:")
for name, val in angles.items():
    print(f"  {name}: {val:.2f}°")

# Check relationships
print("\nRelationships:")
print(f"  θ₁₂ - π/6 = {33.41 - 30:.2f}° (≈ θ₁₃/3 = {8.54/3:.2f}°?)")
print(f"  θ₂₃ - 45° = {49.1 - 45:.2f}°")
```

### Task 4: A₄ Symmetry Check

The alternating group A₄ has order 12 and is the symmetry group of the tetrahedron.

```python
import numpy as np

# A₄ generators in 3D
# Standard representation: even permutations of (1,2,3,4) on tetrahedron vertices

# The "Tribimaximal" mixing matrix (A₄ prediction):
U_TBM = np.array([
    [np.sqrt(2/3), 1/np.sqrt(3), 0],
    [-1/np.sqrt(6), 1/np.sqrt(3), -1/np.sqrt(2)],
    [-1/np.sqrt(6), 1/np.sqrt(3), 1/np.sqrt(2)]
])

# Extract angles from TBM
theta_12_TBM = np.degrees(np.arcsin(1/np.sqrt(3)))  # sin²θ₁₂ = 1/3
theta_23_TBM = 45  # maximal
theta_13_TBM = 0   # zero

print("Tribimaximal (A₄) predictions:")
print(f"  θ₁₂ = {theta_12_TBM:.2f}° (observed: 33.41°)")
print(f"  θ₂₃ = {theta_23_TBM:.2f}° (observed: 49.1°)")
print(f"  θ₁₃ = {theta_13_TBM:.2f}° (observed: 8.54°)")

# The key question: Can A₄ be embedded in H₃?
# H₃ has order 120, A₄ has order 12, so 120/12 = 10 copies possible
print("\nH₃ order: 120, A₄ order: 12")
print("Ratio: 10 (A₄ can be a subgroup of H₃)")
```

---

## 4. DELIVERABLES

### 4.1 Numerical Results
1. Complete (θ, ε) solution space for ratio = 32.6
2. Identification of geometrically meaningful solutions
3. Verification of whether ε has a clean formula (like √2 for charged)

### 4.2 Geometric Analysis
1. Relationship between Face geometry and PMNS angles
2. Role of A₄ ⊂ H₃ in mixing
3. Whether θ₁₃ can be derived (not input)

### 4.3 Assessment Table

| Claim | Status | Evidence |
|-------|--------|----------|
| ε = f(θ₁₃) | ? | Numerical search |
| θ₁₂ = π/6 + correction | ? | Geometric derivation |
| θ₂₃ = 45° (maximal) | ? | Symmetry argument |
| θ₁₃ from geometry | ? | A₄ or other |

---

## 5. CRITICAL CONSTRAINTS

### 5.1 Physical Requirements
- All masses must be positive (m_i > 0)
- If T = 1 + ε·cos(phase) < 0, justify physically (Majorana?)
- Sum of masses < 0.12 eV

### 5.2 Geometric Requirements
- ε should have a clean formula involving φ, π, or simple ratios
- Phase θ should relate to H₃ geometry (30°, 36°, 72° are natural)
- PMNS angles should emerge from D₆ → H₃ projection, not be fitted

### 5.3 What Would CONFIRM the Theory
- Finding ε = simple_function(φ, π)
- Deriving θ₁₃ ≈ 8.5° from geometry (not using it as input)
- PMNS structure emerging from A₄ ⊂ H₃

### 5.4 What Would REFUTE the Theory
- No clean formula for ε exists
- PMNS requires arbitrary parameters
- The ratio 32.6 cannot be achieved with geometric (θ, ε)

---

## 6. RESPONSE FORMAT

Please structure your response as:

1. **NUMERICAL RESULTS**: Output of all Python tasks
2. **SOLUTION SPACE**: Map of (θ, ε) solutions for ratio = 32.6
3. **GEOMETRIC ANALYSIS**: Which solutions have meaning in D₆/H₃
4. **A₄ CONNECTION**: Can A₄ explain PMNS?
5. **VERDICT TABLE**: Status of each claim (CONFIRMED/PLAUSIBLE/FAILED)
6. **RECOMMENDED FORMULA**: The best candidate for the neutrino Koide formula

---

## 7. CONTEXT NOTES

- Be rigorous: show all calculations
- Be critical: if the theory fails, say so clearly
- Previous iterations produced inconsistent results (ε = 4π×θ₁₃ was claimed but doesn't work at θ = 33°)
- We need CLEAN, VERIFIABLE mathematics
- Counterexamples are valuable


