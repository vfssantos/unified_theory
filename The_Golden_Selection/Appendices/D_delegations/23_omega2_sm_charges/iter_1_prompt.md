# Delegation 23 - Iteration 1: ω₂ Orbit and Standard Model Charges

## 1. BACKGROUND: The Quantum Number Problem

### 1.1 The Issue with ω₃

The Golden Selection theory proposes that Standard Model fermions emerge from the **D₆ lattice** projected to 3D via the Koca–Al-Siyabi projection.

Previous work (Delegation 21) investigated the **ω₃ weight orbit**:
- ω₃ = Weyl orbit of (1, 1, 1, 0, 0, 0)
- 160 weights, all with |v|² = 3
- Projects to 4 shells: 20 + 60 + 60 + 20

**Problem**: The calculated quantum numbers are **exotic**:

| Q (calculated) | Fraction | SM-compatible? |
|----------------|----------|----------------|
| +1.17 | 7/6 | ❌ |
| +1.08 | 13/12 | ❌ |
| +0.42 | 5/12 | ❌ |
| ±0.33 | ±1/3 | ✅ |
| -0.92 | -11/12 | ❌ |

These don't match Standard Model fermions (Q ∈ {0, ±1/3, ±2/3, ±1}).

### 1.2 The ω₂ Hypothesis

An earlier computation accidentally used **norm-2 weights** and found SM-compatible charges.

**Hypothesis**: The **ω₂ orbit** (or D₆ roots) hosts elementary SM fermions, while ω₃ represents a preon/composite layer.

---

## 2. THE D₆ LATTICE

### 2.1 Definition

The D₆ root lattice in ℝ⁶:
$$D_6 = \{ x \in \mathbb{Z}^6 : \sum_i x_i \equiv 0 \pmod{2} \}$$

### 2.2 Root System

The D₆ roots are the 60 vectors of squared length 2:
$$\pm e_i \pm e_j \quad (i \neq j)$$

where $e_i$ are the standard basis vectors.

### 2.3 Fundamental Weights

| Weight | Representative | |v|² | Orbit Size |
|--------|----------------|------|------------|
| ω₁ | (1, 0, 0, 0, 0, 0) | 1 | 12 |
| ω₂ | (1, 1, 0, 0, 0, 0) | 2 | 60 |
| ω₃ | (1, 1, 1, 0, 0, 0) | 3 | 160 |
| ω₄ | (1, 1, 1, 1, 0, 0) | 4 | 240 |
| ω₅ | ½(1, 1, 1, 1, 1, -1) | 3/2 | 32 (spinor) |
| ω₆ | ½(1, 1, 1, 1, 1, 1) | 3/2 | 32 (spinor) |

---

## 3. THE KOCA–AL-SIYABI PROJECTION

### 3.1 Projection Matrix

The projection from D₆ to H₃ (physical 3D space):

$$P_\parallel = \frac{1}{\sqrt{2(1+\phi^2)}} \begin{pmatrix} \phi & -\phi & 0 & 0 & 1 & -1 \\ 0 & 0 & \phi & -\phi & 0 & 0 \\ 1 & 1 & 1 & 1 & \phi & \phi \end{pmatrix}$$

where $\phi = (1+\sqrt{5})/2 \approx 1.618$.

### 3.2 Internal Projection

The orthogonal complement $P_\perp$ projects to the internal 3D space $E_\perp$.

---

## 4. QUANTUM NUMBER FORMULAS

### 4.1 Standard Embedding

Based on the D₆ subalgebra structure:
- **SU(3)** on coordinates 1-3
- **SU(2)** on coordinates 4-5
- **U(1)_Y** hypercharge direction

### 4.2 Quantum Number Calculation

For a weight $w = (w_1, w_2, w_3, w_4, w_5, w_6)$:

$$I_3 = \frac{w_4 - w_5}{2}$$

$$Y = \frac{w_1 + w_2 + w_3}{3} - \frac{w_4 + w_5}{2}$$

$$Q = I_3 + \frac{Y}{2}$$

**Note**: These formulas gave exotic charges for ω₃. They may need adjustment for ω₂.

---

## 5. TASKS

### TASK 1: Generate the ω₂ Orbit

Generate all weights in the ω₂ Weyl orbit.

**Expected**:
- Base weight: (1, 1, 0, 0, 0, 0)
- All permutations and sign changes consistent with D₆
- Total: 60 weights (same as D₆ roots)
- All with |v|² = 2

Provide the complete list of 60 weights.

### TASK 2: Project to 3D Shells

Apply the Koca projection to all 60 ω₂ weights.

**Questions**:
1. How many distinct shell radii |P_∥ · v|² are there?
2. How many weights fall into each shell?
3. Do any shells have 20 vertices (like ω₃'s dodecahedral shells)?

### TASK 3: Compute Quantum Numbers

For each ω₂ weight, compute Q, I₃, and Y using the formulas above.

**Questions**:
1. What distinct Q values appear?
2. Are they SM-compatible: Q ∈ {0, ±1/3, ±2/3, ±1}?
3. If not, is there a rescaling or different Y-direction that gives SM charges?

Provide a table:

| Weight | |v|² | Shell R² | Q | I₃ | Y | SM Particle? |
|--------|------|---------|---|-----|---|--------------|
| (1,1,0,0,0,0) | 2 | ? | ? | ? | ? | ? |
| ... | ... | ... | ... | ... | ... | ... |

### TASK 4: Compare ω₂ vs ω₃

| Property | ω₂ | ω₃ |
|----------|-----|-----|
| Orbit size | 60 | 160 |
| |v|² | 2 | 3 |
| Shell structure | ? | 20+60+60+20 |
| Q values | ? | Exotic (7/6, 13/12, ...) |
| SM-compatible? | ? | ❌ |

### TASK 5: Alternative Embeddings

If the standard embedding (Task 3) doesn't give SM charges, try:

1. **Different Y-direction**: 
   - $Y' = (1/3, 1/3, 1/3, -1/2, -1/2, 0) \times k$ for various $k$
   - $Y' = (1, 1, 1, -1, -1, 0) / \sqrt{6}$ (normalized)

2. **Different SU(2) assignment**:
   - SU(2) on coordinates (1,2) instead of (4,5)
   - SU(2) on coordinates (5,6)

3. **Spinor weights** (ω₅ or ω₆):
   - 32 weights each
   - May give half-integer charges naturally

Report which embedding (if any) reproduces SM charges.

---

## 6. STANDARD MODEL FERMION CHARGES

For reference, the SM fermion quantum numbers:

### Left-handed (doublets)

| Particle | Q | I₃ | Y |
|----------|---|-----|---|
| ν_L | 0 | +1/2 | -1 |
| e_L | -1 | -1/2 | -1 |
| u_L | +2/3 | +1/2 | +1/3 |
| d_L | -1/3 | -1/2 | +1/3 |

### Right-handed (singlets)

| Particle | Q | I₃ | Y |
|----------|---|-----|---|
| ν_R | 0 | 0 | 0 |
| e_R | -1 | 0 | -2 |
| u_R | +2/3 | 0 | +4/3 |
| d_R | -1/3 | 0 | -2/3 |

**Distinct Q values**: {0, -1, +2/3, -1/3}

---

## 7. DELIVERABLES

Please provide:

1. **Complete ω₂ orbit** (60 weights)
2. **Shell decomposition** (radii and counts)
3. **Quantum number table** (Q, I₃, Y for all 60 weights)
4. **SM compatibility assessment**: Do any weights match SM fermions?
5. **Alternative embedding results** (if standard fails)
6. **Comparison table**: ω₂ vs ω₃ vs spinor orbits

---

## 8. VERIFICATION CHECKLIST

Before submitting:

- [ ] All 60 ω₂ weights listed
- [ ] All weights have |v|² = 2
- [ ] Shell radii computed for all weights
- [ ] Q, I₃, Y computed for all weights
- [ ] Gell-Mann–Nishijima verified: Q = I₃ + Y/2
- [ ] SM compatibility assessed
- [ ] At least one alternative embedding tried

---

## 9. REFERENCES

- Koca, M. & Al-Siyabi, A. (2012). "Quaternionic Roots of E8 Related Coxeter Graphs and Quasicrystals." *Turkish J. Phys.* 36, 79-94.
- Koca, M. et al. (2011). "Catalan Solids Derived From 3D-Root Systems and Quaternions." *J. Math. Phys.* 52, 043507.
- Georgi, H. & Glashow, S.L. (1974). "Unity of All Elementary-Particle Forces." *Phys. Rev. Lett.* 32, 438.

