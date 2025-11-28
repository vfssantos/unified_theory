# Delegation Prompts for Deep Research

These prompts are designed to be given to independent research agents (LLMs with deep research capabilities, literature search, or computational tools) to complete specific investigations for The Golden Selection theory.

---

## 🔍 DELEGATION 1: Weinberg Angle — Remaining Questions

**Priority**: HIGH (blocks rigorous physics derivation)

**Status**: 🟡 PARTIAL — Numerical calculation exists, needs theoretical justification

### What We Have

A calculation using the "Moxness basis" golden projection gives:

```
|x_SU3|² = 0.553
|x_SU2|² = 1.447
|x_U1|²  = 0.732
sin²θ_W  = 0.2327  (calculated)
(3/8)φ⁻¹ = 0.2318  (target)
Experiment = 0.2312
```

**Agreement**: The calculated value is within 0.4% of (3/8)φ⁻¹ and 0.6% of experiment.

### Existing Code (Partial Verification)

```python
import numpy as np

phi = (1 + np.sqrt(5)) / 2

# Moxness basis
x_vec = np.array([1, phi, 0, -1, phi, 0, 0, 0])
y_vec = np.array([phi, 0, 1, phi, 0, -1, 0, 0])
z_vec = np.array([0, 1, phi, 0, -1, phi, 0, 0])
w_vec = np.array([0, 0, 0, 0, 0, 0, phi**2, 1/phi])
M = np.vstack([x_vec, y_vec, z_vec, w_vec])

# Projection matrix
Q, _ = np.linalg.qr(M.T)
P_phys = Q.T

# SM samples (normalized ||²=2)
su3_root = np.array([1, -1, 0, 0, 0, 0, 0, 0])
su2_root = np.array([0, 0, 0, 1, -1, 0, 0, 0])
y_dir = np.array([1/3, 1/3, 1/3, -1/2, -1/2, 0, 0, 0])
u1_gen = y_dir * np.sqrt(2 / np.dot(y_dir, y_dir))

# Projections
print("|x_SU3|²:", np.dot(P_phys @ su3_root, P_phys @ su3_root))
print("|x_SU2|²:", np.dot(P_phys @ su2_root, P_phys @ su2_root))
print("|x_U1|²:", np.dot(P_phys @ u1_gen, P_phys @ u1_gen))

# sin²θ_W (g² ~ |x|²)
rho = np.dot(P_phys @ su2_root, P_phys @ su2_root) / np.dot(P_phys @ u1_gen, P_phys @ u1_gen)
sin2 = 1 / (1 + (5/3) * rho)
print("sin²θ_W:", sin2)  # → 0.2327
```

---

### ❓ REMAINING QUESTIONS (What We Need)

#### Question 1: Is the Moxness Basis = Elser-Sloane Projection?

**Task**: Verify that the "Moxness basis" used above is equivalent (up to rotation) to the canonical Elser-Sloane golden projection from their 1987 paper.

- The Moxness basis vectors are:
  ```
  x = [1, φ, 0, -1, φ, 0, 0, 0]
  y = [φ, 0, 1, φ, 0, -1, 0, 0]
  z = [0, 1, φ, 0, -1, φ, 0, 0]
  w = [0, 0, 0, 0, 0, 0, φ², 1/φ]
  ```
- **Reference**: Elser & Sloane, J. Phys. A 20 (1987) 6161-6168
- **Deliverable**: Confirm they produce the same 600-cell structure, or identify the difference

#### Question 2: Is the SM Embedding Canonical?

**Task**: Justify or correct the choice of SM generators used in the calculation.

The code uses:
- SU(3) root: `[1, -1, 0, 0, 0, 0, 0, 0]` — a D₈-type root
- SU(2) root: `[0, 0, 0, 1, -1, 0, 0, 0]` — a D₈-type root  
- U(1) direction: `[1/3, 1/3, 1/3, -1/2, -1/2, 0, 0, 0]` — hypercharge Cartan

**Questions**:
1. Is this the standard SM embedding in E₈ (via E₈ ⊃ SO(16) ⊃ SO(10) ⊃ SU(5) ⊃ SM)?
2. Are there other valid embeddings that give different results?
3. **Reference**: Slansky (1981) "Group Theory for Unified Model Building"

**Deliverable**: Explicit mapping from SM generators to E₈ roots with literature citation

#### Question 3: Why ρ ≈ 1.98 Instead of φ ≈ 1.618?

**Observation**: The ratio |x_SU2|²/|x_U1|² ≈ 1.98, not φ ≈ 1.618.

Yet sin²θ_W still comes out close to (3/8)φ⁻¹.

**Task**: Explain this. Is there:
- A deeper algebraic identity at play?
- Cancellation that makes the final answer "golden"?
- Just numerical coincidence?

**Deliverable**: Either an algebraic proof that sin²θ_W = (3/8)φ⁻¹ exactly, or explanation of why the match is approximate

#### Question 4: What is the Exact Algebraic Value?

**Task**: If possible, compute sin²θ_W symbolically (not numerically) from the projection.

- Express |x_SU2|² and |x_U1|² as algebraic expressions in φ
- Derive sin²θ_W as an exact algebraic formula
- Determine if it equals (3/8)φ⁻¹ exactly or only approximately

**Deliverable**: Exact symbolic expression for sin²θ_W from the projection geometry

---

### Summary: What Would Complete This

| Question | Status | Blocks |
|----------|--------|--------|
| Q1: Moxness = Elser-Sloane? | ⬜ | Verification of projection |
| Q2: SM embedding canonical? | ⬜ | Physical interpretation |
| Q3: Why ρ ≠ φ but result works? | ⬜ | Theoretical understanding |
| Q4: Exact algebraic value? | ⬜ | Rigorous theorem |

**If all answered**: Promotes from CONJECTURE to THEOREM

---

## 🔍 DELEGATION 2: The Golden Lock — Rigorous D=3 Selection

**Priority**: HIGH (core claim of the theory)

**Task**: Establish rigorously whether D=3 is the unique dimension supporting stable aperiodic order.

### Context

The Golden Selection theory claims that stable aperiodic (quasicrystalline) order exists **only** in D=3 due to:

- **Lower bound (D ≥ 3)**: Generalized Peierls arguments; topological defects insufficient for protection in D < 3
- **Upper bound (D ≤ 3)**: Zeeman's unknotting theorem; Hopfion-type topological solitons cannot form stable knots in D > 3

The mechanism is called the "Golden Lock": phason degrees of freedom in quasicrystals can form topologically protected Hopfion configurations only in D=3.

### Research Questions

#### Part A: Lower Bound (D ≥ 3)

1. **What do generalized Peierls arguments actually say?**
   - Do they apply to aperiodic systems or only periodic ones?
   - What is the precise statement about long-range order in D < 3?
   - Sources: Mermin-Wagner theorem, Kosterlitz-Thouless, Imry-Ma arguments

2. **Are there stable 2D quasicrystals?**
   - Real 2D quasicrystalline thin films exist (e.g., Al-Pd-Mn surfaces)
   - Are these truly stable or only metastable?
   - Does "stable" here mean thermodynamically stable or kinetically trapped?

3. **What topological defects exist in D=2 vs D=3?**
   - π₁ gives vortices (D=2), π₂ gives monopoles (D=3), π₃ gives Hopfions (D=3)
   - Is there a classification of what protects what?

#### Part B: Upper Bound (D ≤ 3)

1. **Zeeman's Unknotting Theorem**
   - Find the original paper: Zeeman (1963) "Unknotting combinatorial balls"
   - Precise statement: 1-spheres can knot only in 3-space
   - What about higher-dimensional generalizations? (k-spheres in n-space)

2. **Can Hopfions exist in D > 3?**
   - Hopf fibration is S³ → S² → S¹ (3D phenomenon)
   - Are there D > 3 analogs?
   - What is π₃(S²) in different dimensions?

3. **Are there alternative stabilization mechanisms in D > 3?**
   - Could 4D quasicrystals be stabilized by energetic barriers (not topological)?
   - What about frustration or geometrical constraints?
   - Are there any papers on 4D quasicrystal stability?

#### Part C: The Specific Mechanism

1. **Do phason fields actually form Hopfions?**
   - Find papers on phason dynamics in 3D quasicrystals
   - Is there experimental or theoretical evidence for topological protection?
   - Key search terms: "phason dynamics," "quasicrystal relaxation," "topological defects in quasicrystals"

2. **The "topological jamming" claim**
   - Reference cited: "Slow Flip Dynamics in Three-Dimensional Rhombus Tilings"
   - Verify this paper exists and says what is claimed
   - Does it specifically attribute slow dynamics to topological linking?

3. **Photonic Hopfions reference**
   - Reference cited: "Photonic Spin Hopfions and Monopole Loops" (2024)
   - Verify and check if relevant to quasicrystal stability

### Deliverables

1. **Literature review**: What is mathematically proven about dimensional dependence of aperiodic order stability?
2. **Gap analysis**: What claims in the Golden Lock argument are proven vs. plausible vs. speculative?
3. **Counterexample search**: Any evidence of stable aperiodic order in D ≠ 3?
4. **Recommendation**: Is the Golden Lock argument defensible, and what would strengthen it?

---

## 🔍 DELEGATION 3: Why H₃ Over Other Quasicrystal Symmetries?

**Priority**: MEDIUM (affects uniqueness claim)

**Task**: Determine whether maximizing complexity specifically selects H₃ (icosahedral) symmetry over other non-crystallographic symmetries.

### Context

The theory claims:
1. 3D quasicrystals must have non-crystallographic symmetry (true by definition)
2. H₃ is the "unique maximal" non-crystallographic point group in 3D (true)
3. Therefore, complexity maximization selects H₃ (questionable)

**The problem**: Real 3D quasicrystals also exist with lower symmetries:
- Decagonal (10-fold axis, 2D quasiperiodic, 1D periodic)
- Octagonal (8-fold axis)
- Dodecagonal (12-fold axis)

These are non-crystallographic but not H₃.

### Research Questions

1. **Classification of 3D quasicrystal symmetries**
   - What symmetries are realized in nature?
   - Which are thermodynamically stable vs. metastable?
   - Sources: Shechtman et al. (1984), Levine & Steinhardt (1984), review articles

2. **Complexity comparison**
   - What is the statistical complexity Cμ of icosahedral vs. decagonal quasicrystals?
   - Has anyone computed this?
   - Is there a theorem that icosahedral maximizes Cμ among all 3D quasicrystals?

3. **The "maximal point group" argument**
   - Does maximal symmetry imply maximal complexity?
   - Or could a lower-symmetry structure have higher information content?
   - What is the relationship between group order and statistical complexity?

4. **Physical selection**
   - Why are icosahedral quasicrystals common in nature?
   - Is this due to complexity maximization, or other factors (energetics, kinetics)?

### Deliverables

1. **Table** of all known 3D quasicrystal symmetry types with stability status
2. **Analysis** of whether complexity (Cμ) can distinguish H₃ from alternatives
3. **Assessment** of whether the H₃ selection claim is rigorous or needs additional postulates

---

## 🔍 DELEGATION 4: E₈ Uniqueness and Minimality

**Priority**: MEDIUM (affects geometric foundation)

**Task**: Verify the claim that E₈ is the "unique minimal lattice admitting an H₄-symmetric projection."

### Context

The theory's geometric chain is:
$$H_3 \text{ (3D)} \leftarrow H_4 \text{ (4D)} \leftarrow E_8 \text{ (8D)}$$

Claims made:
1. H₃ requires H₄ as parent (via subgroup relation) ✓
2. H₄ cannot tile 4D (crystallographic restriction) ✓
3. E₈ is the "unique minimal" lattice for H₄ — **needs verification**

### Research Questions

1. **What lattices can produce H₄ upon projection?**
   - E₈ does (Elser-Sloane)
   - Does D₈ work? A₈? Other 8D lattices?
   - What about 6D lattices (the "standard" embedding for icosahedral QC)?

2. **The "even self-dual" criterion**
   - Why require even self-dual?
   - This is stated as maximizing "regularity" but is it derived from the axiom?
   - What happens if we drop this requirement?

3. **Why not the Leech lattice (24D)?**
   - Claim: "Leech cannot project to H₄" — is this proven?
   - Reference needed
   - Leech is based on Golay code (binary) — does this preclude golden ratio structure?

4. **Dimension minimality**
   - 6D icosahedral quasicrystals exist (standard model)
   - Why does the theory require 8D?
   - What extra structure does E₈ provide over ℤ⁶?

### Key References to Find

- Elser-Sloane (1987): E₈ → 600-cell projection
- Conway-Sloane: Lattice classification
- Standard icosahedral QC papers using 6D embedding
- Any paper on Leech lattice and icosahedral symmetry

### Deliverables

1. **Classification**: Which lattices (by dimension) admit H₄-preserving projections?
2. **Uniqueness proof** (or counterexample): Is E₈ actually unique, or merely convenient?
3. **Justification assessment**: Are the criteria (even self-dual, minimal dimension) derived or imposed?

---

## 🔍 DELEGATION 5: Three Generations from 600-Cell Geometry

**Priority**: HIGH (major physics claim)

**Task**: Derive or refute the claim that exactly 3 fermion generations emerge from 600-cell geometry.

### Context

The 600-cell has 120 vertices distributed across latitude bands (heights) when viewed vertex-first:

| Height h | Count | 3D Polytope |
|----------|-------|-------------|
| ±2 | 1 | Pole |
| ±φ | 12 | Icosahedron |
| ±1 | 20 | Dodecahedron |
| ±φ⁻¹ | 12 | Icosahedron |
| 0 | 30 | Icosidodecahedron |

Total: 1+12+20+12+30+12+20+12+1 = 120 ✓

The theory claims:
- "Matter" lives in the dodecahedral band (20 vertices at h = ±1)
- The 3 generations arise from some 3-fold structure within this

**But**: There are **9 distinct latitude values**, not 3. Why do exactly 3 correspond to generations?

### Research Questions

1. **What is the explicit identification?**
   - Which vertices = which fermions?
   - Where is the 3-fold structure that gives generations?
   - Is it the ±1 splitting? (Only gives 2)
   - Is it some substructure within the dodecahedron?

2. **The dodecahedron structure**
   - 20 vertices of dodecahedron
   - Can be partitioned: 20 = 8 (cube) + 12 (icosahedron)?
   - Or: 20 = 4 × 5 (five tetrahedra)?
   - Or: related to 16 fermions + 4 Higgs?

3. **Chirality and generations**
   - Standard Model has 16 Weyl fermions per generation (including right-handed neutrino)
   - 3 generations = 48 fermions
   - Does 600-cell geometry give this counting?

4. **The two 600-cells**
   - E₈ → 120 + 120 = 240 roots
   - Inner 600-cell + outer 600-cell
   - Claim: one is "matter," one is "mirror" — where's the generation structure?

5. **Literature search**
   - Has anyone else proposed generation structure from polytope geometry?
   - Search: "three generations polytope," "E₈ generations," "600-cell fermions"

### Deliverables

1. **Explicit mapping** (or acknowledgment that none exists): vertices → fermions × generations
2. **Counting check**: Does the geometry give 3 × 16 = 48?
3. **Mechanism**: What geometric principle gives "3" rather than 9 (latitude bands) or other numbers?
4. **Assessment**: Is this a derivation or a fit?

---

## 🔍 DELEGATION 6: Koide Formula from A₂ Geometry

**Priority**: MEDIUM (interesting physics connection)

**Task**: Verify or refute the geometric derivation of Koide's formula from A₂ lattice structure.

### Context

Koide's formula (empirical, 1982):
$$Q \equiv \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

This holds to ~0.01% for charged leptons (remarkable!).

The theory claims:
- The Q = 2/3 value arises from masses lying on an A₂ (hexagonal) lattice in "mass space"
- The angle θ₀ ≈ 347° (Koide phase) equals 360° - arctan(φ⁻³)

### Research Questions

1. **What does "A₂ lattice in mass space" mean precisely?**
   - Mass space = (√m_e, √m_μ, √m_τ) ∈ ℝ³?
   - What constraint does A₂ impose?
   - Why A₂ rather than another lattice?

2. **Geometric derivation of Q = 2/3**
   - If (√m₁, √m₂, √m₃) lies at angle 45° to the (1,1,1) direction, then Q = 2/3
   - Is this the claim?
   - How does this connect to E₈ or 600-cell geometry?

3. **The Koide phase θ₀**
   - Standard parameterization: √m_i = M₀(1 + √2 cos(θ₀ + 2πi/3))
   - Observed: θ₀ ≈ 0.222 rad ≈ 12.7° (or 360° - 12.7° = 347.3°)
   - Theory claims: θ₀ = arctan(φ⁻³) ≈ 13.28°
   - Check: Does this match within uncertainties?

4. **Quark Koide formulas**
   - Do quarks satisfy Koide-like relations?
   - What ratios does the theory predict?
   - Compare to measured quark masses (with uncertainties!)

5. **Literature on Koide formula**
   - Original: Koide (1982)
   - Geometric interpretations: Brannen, others
   - Any connection to E₈ or polytope geometry in literature?

### Numerical Check

```python
import numpy as np

# Lepton masses (MeV)
m_e = 0.51099895
m_mu = 105.6583755
m_tau = 1776.86

# Koide ratio
sqrt_m = np.sqrt([m_e, m_mu, m_tau])
Q = sum([m_e, m_mu, m_tau]) / sum(sqrt_m)**2
print(f"Koide Q = {Q:.6f} (should be ~0.666...)")

# Koide phase
# From √m_i = M₀(1 + √2 cos(θ₀ + 2πi/3))
# Solve for θ₀ numerically
# ...

# Golden prediction
phi = (1 + np.sqrt(5)) / 2
theta_golden = np.arctan(phi**(-3)) * 180 / np.pi
print(f"arctan(φ⁻³) = {theta_golden:.2f}°")
```

### Deliverables

1. **Precise statement** of the geometric claim
2. **Numerical verification** of θ₀ prediction vs. observed
3. **Assessment**: Is this a derivation from E₈ geometry, or an independent numerological observation?
4. **Quark predictions**: What does the theory predict, and how well do they match?

---

## 🔍 DELEGATION 7: CKM and PMNS Mixing Angles from Golden Geometry

**Priority**: MEDIUM (testable predictions)

**Task**: Verify the claimed geometric derivations of quark and lepton mixing angles.

### Context

The theory claims:

| Angle | Formula | Predicted | Observed |
|-------|---------|-----------|----------|
| θ_Cabibbo (θ₁₂ CKM) | arctan(φ⁻³) | 13.28° | 13.04° |
| θ₂₃ (CKM) | arctan(1/24) | 2.39° | 2.38° |
| θ₁₃ (CKM) | arcsin(φ⁻¹²) | 0.18° | 0.20° |
| δ (CP phase) | arctan(φ²) | 69.1° | 68.8° |
| θ₁₃ (PMNS) | arcsin(φ⁻⁴) | 8.39° | 8.57° |
| θ₁₂ (PMNS) | 45° - arctan(φ⁻³) | 31.72° | 33.41° |

### Research Questions

1. **What is the geometric origin of each formula?**
   - Cabibbo: "D₄ → A₃ misalignment" — what does this mean precisely?
   - Why φ⁻³ specifically?
   - Why 1/24 for θ₂₃?
   - Why φ⁻¹² for θ₁₃?

2. **Are these derivations or fits?**
   - Post-hoc: We knew the angles and found φ expressions that match
   - Derivation: The geometry predicts these specific combinations
   - Which is it?

3. **Numerical accuracy check**
   - Get current PDG values for all CKM and PMNS parameters with uncertainties
   - Compute predicted values
   - Calculate χ² or significance of matches

4. **The "φ⁻³ appears everywhere" observation**
   - sin²θ_W ≈ φ⁻³
   - θ_Cabibbo = arctan(φ⁻³)
   - θ₀ (Koide) = 360° - arctan(φ⁻³)
   - Is there a unified geometric origin for all three?
   - Or is φ⁻³ ≈ 0.236 just a "convenient" number?

5. **Literature search**
   - Has anyone else derived mixing angles from E₈ or polytope geometry?
   - Discrete flavor symmetry models (A₄, S₄, etc.) — any overlap?

### Deliverables

1. **Table**: All mixing angle predictions vs. PDG 2024 values with uncertainties
2. **Statistical assessment**: How significant are the matches? (Given 6+ angles, some matches expected by chance)
3. **Derivation status**: For each angle, is the geometric origin explicit or hand-wavy?
4. **Common origin**: Is there a single principle giving all φ⁻³ appearances?

---

## 🔍 DELEGATION 8: Higgs Mass Prediction m_H = m_Z × (15/11)

**Priority**: MEDIUM (specific testable prediction)

**Task**: Verify and understand the geometric origin of the Higgs mass prediction.

### Context

The theory claims:
$$m_H = m_Z \times \frac{15}{11} = 91.188 \times 1.3636... = 124.35 \text{ GeV}$$

Observed: m_H = 125.10 ± 0.14 GeV (0.6% discrepancy)

### Research Questions

1. **Where does 15/11 come from?**
   - Is this derived from 600-cell geometry?
   - Is 15 or 11 related to vertex counts, face counts, etc.?
   - Or is this a post-hoc fit?

2. **Why m_Z specifically?**
   - Why relate m_H to m_Z rather than m_W or v (Higgs VEV)?
   - Is there a geometric reason?

3. **Alternative formula mentioned**
   - Theory also mentions: m_H = (√5/3) m_t ≈ 129 GeV (less accurate)
   - Which is the "real" prediction?
   - Are they related?

4. **Consistency check**
   - Does 15/11 relate to φ in any way?
   - 15/11 ≈ 1.364 vs. φ⁻¹ + 1 = 1.618, or other φ combinations?

5. **Literature**
   - Any other theories predicting m_H/m_Z ratio?
   - Is 15/11 special in any known context?

### Deliverables

1. **Geometric derivation** (if one exists) of the 15/11 factor
2. **Numerical verification** with current experimental values
3. **Assessment**: Prediction or fit?

---

## 🔍 DELEGATION 9: Mirror Fermions and the Second 600-Cell

**Priority**: LOW (speculative, but testable)

**Task**: Clarify and assess the prediction of mirror fermions at ~TeV scale.

### Context

The Elser-Sloane projection gives:
- E₈ (240 roots) → Inner 600-cell (120 vertices) + Outer 600-cell (120 vertices)
- Radius ratio: R_outer/R_inner = φ

The theory claims:
- Inner 600-cell → Standard Model particles
- Outer 600-cell → "Mirror" particles
- Mirror mass scale: m_mirror ~ m_SM × φ³ ~ TeV

### Research Questions

1. **What exactly are "mirror fermions"?**
   - Same quantum numbers as SM fermions?
   - Opposite chirality (like left-right symmetric models)?
   - How do they couple to SM?

2. **Why φ³ for the mass ratio?**
   - φ³ ≈ 4.24, so if SM masses ~ 100 GeV, mirrors ~ 400 GeV?
   - Or if VEV v = 246 GeV, mirror scale ~ v × φ³ ~ 1 TeV?
   - Where does the specific power come from?

3. **Existing searches**
   - What are current LHC limits on heavy fermions?
   - Vector-like quarks, heavy leptons, etc.
   - Does the prediction survive current bounds?

4. **Theoretical consistency**
   - Mirror fermions would contribute to electroweak precision observables
   - Are there constraints from S, T, U parameters?
   - What about Higgs couplings?

5. **Related literature**
   - Left-right symmetric models
   - Mirror matter models (Foot, etc.)
   - Any connection to E₈ GUTs?

### Deliverables

1. **Precise prediction**: Mass, quantum numbers, production cross-section of mirror fermions
2. **Current constraints**: What's already ruled out?
3. **Discovery potential**: What experiments could test this?

---

## 🔍 DELEGATION 10: Cosmological Predictions (Dark Energy / Slice Field)

**Priority**: LOW (highly speculative)

**Task**: Assess the cosmological predictions from the "dynamical slice field."

### Context

Postulate 3 of the theory introduces a "slice field" Σ that determines the projection orientation. This field has:
- A potential V(Σ) with minimum at the Golden Slice configuration
- Dynamics governed by an action S_Σ

Claims:
- Residual potential energy acts as dark energy
- Equation of state: w ≈ -0.98 (slightly above -1, "thawing quintessence")
- Slow variation of "constants" (Δα/α ~ 10⁻⁶ per Gyr)

### Research Questions

1. **Is w ≈ -0.98 distinguishable from w = -1?**
   - Current constraints: w = -1.03 ± 0.03 (Planck + SNe)
   - What precision is needed to detect w = -0.98?
   - Future experiments: DESI, Euclid, Roman — can they reach this?

2. **Thawing vs. freezing quintessence**
   - Theory predicts "thawing" (w increasing toward -1)
   - How does this compare to data?

3. **Varying constants prediction**
   - α variation of 10⁻⁶/Gyr
   - Current limits: |Δα/α| < 10⁻⁵ from quasar spectra
   - Is the prediction testable?

4. **Slice field dynamics**
   - What is the explicit form of V(Σ)?
   - How does it couple to matter?
   - Is this equivalent to known quintessence models?

5. **Energy scale**
   - What is the energy scale of the slice field?
   - How does it relate to the cosmological constant problem?

### Deliverables

1. **Testability assessment**: When (if ever) can w = -0.98 be confirmed/ruled out?
2. **Comparison**: How does slice field compare to standard quintessence models?
3. **Constraints**: Does varying-constants prediction conflict with existing data?

---

# Summary: Priority Order

| Delegation | Priority | Reason |
|------------|----------|--------|
| 1. Weinberg Angle Calculation | **HIGH** | Core physics prediction, calculation missing |
| 2. Golden Lock (D=3) | **HIGH** | Most original claim, needs rigorous proof |
| 5. Three Generations | **HIGH** | Major physics claim, derivation unclear |
| 3. H₃ Selection | MEDIUM | Affects uniqueness argument |
| 4. E₈ Uniqueness | MEDIUM | Foundation needs verification |
| 6. Koide Formula | MEDIUM | Interesting connection, needs clarity |
| 7. Mixing Angles | MEDIUM | Many predictions, need systematic check |
| 8. Higgs Mass | MEDIUM | Specific prediction |
| 9. Mirror Fermions | LOW | Speculative but testable |
| 10. Cosmology | LOW | Highly speculative |

---

# How to Use These Prompts

For each delegation:

1. **Copy the full prompt** to the research agent
2. **Specify output format**: Request structured deliverables
3. **Request citations**: All claims should have literature references
4. **Request code**: For numerical checks, ask for executable code
5. **Cross-validate**: For important results, send to 2+ agents

When results return, update the main theory documents with:
- Confirmations (promote conjectures to theorems)
- Refutations (revise or abandon claims)
- Open questions (add to research agenda)

