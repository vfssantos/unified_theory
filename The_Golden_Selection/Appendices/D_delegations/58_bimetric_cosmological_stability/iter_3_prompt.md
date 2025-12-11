# Deep Research Request: Closing the Gaps — From PLAUSIBLE to PROVEN

## 1. CONTEXT: Where We Are

### Previous Findings (Iterations 1-2)

We established that the GS bi-metric gravity (γ = 0, M_f = M_g, m ~ 10⁻²² eV) faces cosmological instabilities, but a **phase transition at H ~ m** provides a plausible resolution:

| Finding | Status |
|---------|--------|
| Higuchi violation at early times (H >> m) | ✅ Confirmed |
| Phase transition at z ~ 10⁶ numerically viable | ✅ Verified |
| Axiom 0 can forbid unstable configs (ghost → κ_Schur → ∞) | 🟡 Conceptually clean |
| Timeline: BBN → Crystallization → Equality → CMB | ✅ Safe |

**Current status**: PLAUSIBLE — the argument structure is sound but not yet a theorem.

### What's Missing for PROVEN

From iter_2, three specific gaps were identified:

1. **Gap A**: No explicit **κ_Schur[g,f;H]** functional for FLRW bigravity
2. **Gap B**: No explicit **β_n derivation** from D₆ → H₃ elasticity  
3. **Gap C**: No proof that **F_bi > F_GR for H >> m** and **F_bi < F_GR for H < m**

This delegation aims to close these gaps or determine what explicit calculations are needed.

---

## 2. THE THREE GAPS

### Gap A: Constructing κ_Schur for Bigravity

**The setup**: In GS, Axiom 0 minimizes F = E_strain + λ·κ_Schur, where κ_Schur is a Schur-convex curvature functional.

**For D₆ → H₃**: κ_Schur is constructed on the eigenvalue spectrum of the internal Laplacian L⊥, and its unique minimum at φ⁻² selects the golden ratio.

**For bigravity cosmology**: We need a κ_Schur defined on FLRW configurations (g_μν, f_μν).

**Natural candidate**: The eigenvalues of √(g⁻¹f), denoted λ₁, λ₂, λ₃, λ₄, enter the HR potential via elementary symmetric polynomials e_n(λ). A Schur-convex functional of these eigenvalues could serve as κ_Schur.

**Questions**:
1. Is there existing literature on **Schur-convex functionals in gravity/cosmology**?
2. Can we construct κ_Schur(λ₁,...,λ₄) such that:
   - It diverges when Higuchi is violated (ghost mode)
   - It has a minimum on the stable cosmological branch
3. Does majorization order of λ⃗ correlate with stability conditions (r'(N) ≥ 0, ω² < 0)?

### Gap B: Deriving β_n from D₆ Elasticity

**What we know from GS**:
- Transport tensors: T_u = T_w = 20·I (exactly isotropic)
- Coupling tensor: C ≈ 0 (phonon-phason decoupling at quadratic level)
- This gives: M_f = M_g (equal Planck masses), γ = 0 (no kinetic mixing)

**What we need**: The interaction parameters β₀, β₁, β₂, β₃, β₄.

**The mapping**: In quasicrystal elasticity, the phason-phonon coupling is described by elastic tensors (Socolar, Steinhardt, de Boissieu). The HR potential e_n(√(g⁻¹f)) should emerge from the anharmonic terms in the elastic free energy.

**Questions**:
1. How does quasicrystal elastic theory map to the HR β_n parameters?
2. For **icosahedral quasicrystals** (H₃ symmetry), what constraints does isotropy impose on β_n?
3. Does **M_f = M_g + isotropy** imply the symmetric condition **β_n = β_{4-n}**?
4. Is there literature on **bi-metric gravity from elastic media** that provides this mapping?

**Key insight**: If the D₆ lattice's icosahedral isotropy forces β_n = β_{4-n}, this is exactly the **Symmetric Branch** condition that recent literature identifies as potentially stable.

### Gap C: Free Energy Comparison F_bi vs F_GR

**The claim**: Axiom 0 selects the minimum of F = E_strain + λ·κ_Schur.

**What we need to show**:
- For H >> m: F_bi > F_GR (bi-metric disfavored)
- For H < m: F_bi < F_GR (bi-metric preferred)

**Approaches**:

1. **Thermodynamic**: Use de Sitter temperature T_dS = H/(2π) and compute free energies
2. **Information-theoretic**: κ_Schur measures "roughness" — ghost modes have maximal roughness
3. **Stability-based**: Unstable configurations have F → ∞ by definition

**Questions**:
1. Is there literature on **free energy of bigravity vacua** as a function of H?
2. Can the Higuchi ghost be interpreted as **infinite free energy** in some sense?
3. Has anyone computed **thermodynamic phase diagrams** for HR bigravity?

---

## 3. SPECIFIC RESEARCH TASKS

### Task A: κ_Schur Construction

**Search for**:
- "Schur convex" + "cosmology" or "gravity"
- "Majorization" + "metric eigenvalues"  
- "Information geometry" + "bi-metric gravity"
- "Entropy production" + "bigravity"

**Look for**:
- Any Schur-convex functional defined on spacetime metrics
- Entropy functionals for two-metric systems
- Information-geometric treatments of bigravity

### Task B: Elastic → β_n Mapping

**Search for**:
- "Quasicrystal elastic" + "bigravity" or "bi-metric"
- "Phason phonon" + "graviton"
- "Elastic theory" + "Hassan Rosen" or "massive gravity"
- "Icosahedral" + "gravity" + "isotropy"

**Key papers to find**:
- Socolar et al. on generalized quasicrystal elasticity
- Any work connecting elastic media to bi-metric gravity
- Treatments of **analog gravity** in elastic/acoustic systems

**Specific question**: In analog bi-metric models (e.g., acoustic metrics), how do elastic constants map to β_n?

### Task C: Symmetric Branch Stability

**Search for**:
- "Symmetric bimetric" + "cosmology" + "stable"
- "β_n = β_{4-n}" + "bigravity"
- "Democratic bigravity" + "FLRW"
- Recent (2023-2025) papers on bi-metric cosmology

**Key question**: Is there a **proven theorem** that the Symmetric Branch (β_n = β_{4-n}, M_f = M_g) is cosmologically stable?

**If such a theorem exists**, GS automatically satisfies it via D₆ isotropy!

### Task D: Bigravity Thermodynamics

**Search for**:
- "Bigravity" + "thermodynamics" + "phase transition"
- "Hassan Rosen" + "free energy"
- "Massive gravity" + "de Sitter temperature"
- "Graviton" + "thermal" + "Higuchi"

**What we're looking for**:
- Free energy F(H, m, β_n) for bigravity vacua
- Phase diagrams in (H, m) space
- Thermodynamic interpretation of the Higuchi bound

---

## 4. THE KEY THEOREM WE'RE LOOKING FOR

**Ideal outcome**: A theorem (existing or constructible) of the form:

> **THEOREM (Symmetric Bigravity Stability)**:
> For Hassan-Rosen bigravity with:
> - M_f = M_g (equal Planck masses)
> - β_n = β_{4-n} (symmetric potential)
> - γ = 0 (no kinetic mixing)
>
> The cosmological evolution is **stable** (no Higuchi ghosts, c_s² > 0) for all epochs where m² > 2H².
>
> **Corollary**: Such a theory naturally admits a phase transition at H ~ m, with single-metric GR at early times and bi-metric structure at late times.

If this theorem exists or can be proven, the GS bi-metric sector is **PROVEN** cosmologically viable.

---

## 5. WHAT WOULD CONFIRM vs REQUIRE MORE WORK

### Would CONFIRM (upgrade to PROVEN):

1. **Explicit theorem** that Symmetric Branch (β_n = β_{4-n}, M_f = M_g) is stable for m² > 2H²
2. **Derivation** showing D₆ isotropy ⟹ β_n = β_{4-n}
3. **Construction** of κ_Schur[g,f] that diverges for Higuchi violation
4. **Calculation** showing F_bi > F_GR at H >> m and F_bi < F_GR at H < m

### Would still require MORE WORK:

1. If Symmetric Branch stability is "mostly true" but with caveats
2. If β_n mapping requires explicit numerical calculation from D₆ tensors
3. If κ_Schur construction is possible but not in existing literature

### Would FALSIFY the approach:

1. Proof that Symmetric Branch is **always** unstable regardless of H
2. Proof that D₆ isotropy gives β_n in an unstable region
3. Counterexample showing no phase transition can save democratic bigravity

---

## 6. DELIVERABLES

### 6.1 Gap Status Table

| Gap | Status | Evidence/Citation | What's Missing |
|-----|--------|-------------------|----------------|
| A: κ_Schur construction | | | |
| B: β_n from D₆ | | | |
| C: F_bi vs F_GR | | | |

### 6.2 Symmetric Branch Analysis

Provide a detailed analysis of what's known about the Symmetric Branch:
- Definition in the literature
- Stability properties
- Cosmological viability
- Connection to M_f = M_g

### 6.3 Elastic → β_n Mapping

If found:
- The explicit mapping formula
- What constraints isotropy imposes
- Whether D₆ parameters land in stable region

### 6.4 Recommendations

Based on findings:
- What can be claimed as PROVEN?
- What requires explicit GS-specific calculation?
- What should be the next computational step?

---

## 7. RESPONSE FORMAT

```markdown
# Closing the Gaps: From PLAUSIBLE to PROVEN

## Executive Summary
[Can we upgrade to PROVEN? What's the path?]

## 1. Gap A: κ_Schur for Bigravity
### 1.1 Literature Review
### 1.2 Possible Constructions
### 1.3 Status

## 2. Gap B: β_n from D₆ Elasticity
### 2.1 Elastic → Bigravity Mapping
### 2.2 Isotropy Constraints
### 2.3 Does D₆ give β_n = β_{4-n}?
### 2.4 Status

## 3. Gap C: Free Energy Comparison
### 3.1 Bigravity Thermodynamics Literature
### 3.2 F(H, m) Calculations
### 3.3 Status

## 4. The Symmetric Branch
### 4.1 Definition and Properties
### 4.2 Stability Theorems
### 4.3 Connection to GS Parameters

## 5. Synthesis
### 5.1 What Can Be Claimed as PROVEN
### 5.2 What Requires GS-Specific Calculation
### 5.3 Recommended Next Steps

## 6. Gap Status Table
| Gap | Status | Path to PROVEN |

## 7. Verdict
[PROVEN / NEARLY PROVEN / REQUIRES CALCULATION / BLOCKED]

## 8. References
```

---

## 8. CONTEXT NOTES

- We're trying to **close the loop** — turn a plausible argument into a theorem
- The key insight is that **D₆ isotropy might automatically give Symmetric Branch**, which might be **proven stable**
- If the Symmetric Branch has established stability theorems, we just need to show GS maps to it
- We're looking for existing results to leverage, not asking you to prove new theorems
- If explicit GS calculations are needed, specify exactly what needs to be computed

The goal is to determine: **Is there a path from PLAUSIBLE to PROVEN, or is this as far as literature can take us?**

