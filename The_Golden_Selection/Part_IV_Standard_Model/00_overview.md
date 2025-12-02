# Part IV: The Standard Model — Physics from Geometry

## Overview

Parts I–III established the D₆ → H₃ quasicrystal with golden ratio scaling and 3D internal space E⊥. Part IV derives the **Standard Model** from this geometry: gauge groups from subalgebras, fermions from spinors, generations from occupation domains, and masses from the dual L⊥ + Koide mechanism.

**The central result**: Starting from the D₆ lattice and H₃ projection (no free parameters), we derive 20+ observables with typical accuracies of 0.1–5%.

---

## The Derivation Chain

```
Part III: D₆ quasicrystal with H₃ symmetry + E⊥ internal space
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    IV.1 GAUGE           IV.3 FERMIONS       IV.4 GENERATIONS
    SU(3)×SU(2)×U(1)     ω₅ spinor → 32      A/B/C domains → 3
    from D₆ subalgebras  SM states/gen       via E⊥ stratification
         │                    │                    │
         ▼                    └────────┬───────────┘
    IV.2 ELECTROWEAK                   ▼
    sin²θ_W = 0.2327          IV.5 MASS MECHANISM
    (0.6% accuracy)           L⊥ (radial) + Koide (angular)
                                       │
              ┌────────────────────────┼─────────────────┐
              ▼                        ▼                 ▼
         IV.6 LEPTONS            IV.7 QUARKS       IV.8 MIXING
         e,μ,τ + ν₁,ν₂,ν₃       u,c,t / d,s,b      CKM + PMNS
         (0.01% accuracy)        (rational Q)       (0.3–8%)
                                       │
              ┌────────────────────────┼─────────────────┐
              ▼                        ▼                 ▼
         IV.9 HIGGS            IV.10 LAGRANGIAN   IV.11 CHIRALITY
         S₄ anomaly →          Interactions        V-A structure
         Electroweak breaking  from geometry       from projection
                                       │
                                       ▼
                             IV.12 PREDICTIONS
                             (Summary of all results)
```

---

## What This Part Proves

| Section | Question | Answer | Status |
|---------|----------|--------|--------|
| **IV.1** | How do gauge groups emerge? | SU(3)×SU(2)×U(1) from A₂+A₁+U(1) subalgebras | [VERIFIED] |
| **IV.2** | What is the Weinberg angle? | sin²θ_W = (393-75√5)/968 ≈ 0.2327 | [VERIFIED] |
| **IV.3** | What is the fermion spectrum? | ω₅ spinor → 32 SM states per generation | [VERIFIED] |
| **IV.4** | Why three generations? | Core/Shell/Skin occupation domains in E⊥ | [DERIVED] |
| **IV.5** | What determines mass? | L⊥ (which generation) + Koide (mass within) | [DERIVED] |
| **IV.6** | What are lepton masses? | 6 masses from m_e + derived parameters | [VERIFIED] |
| **IV.7** | What are quark masses? | Rational Q-values (6/7, 11/15) | [VERIFIED] |
| **IV.8** | How do generations mix? | CKM tunneling + PMNS symmetry breaking | [DERIVED] |
| **IV.9** | What is the Higgs mass? | m_H = m_Z × φ^(2/3) = 125.68 GeV (0.34%) | **[DERIVED]** |
| **IV.10** | How do particles interact? | Mass term derived; kinetic terms NOT derived | [PARTIAL] |
| **IV.11** | Why parity violation? | Leptons: R alignment = 0; L/R ≈ √5; A₂ geometry | **[DERIVED]** |

---

## Files in This Part

| File | One-Line Summary |
|------|------------------|
| `01_gauge.md` | D₆ subalgebras → SM gauge group; shell placement verified |
| `02_electroweak.md` | Weinberg angle from projection anisotropy (0.6% accuracy) |
| `03_fermions.md` | ω₅ spinor reproduces all SM quantum numbers exactly |
| `04_generations.md` | φ² : φ : 1 occupation domains → three families |
| `05_mass_mechanism.md` | L⊥ operator (radial) ⊥ Koide geometry (angular) |
| `06_masses_leptons.md` | Charged + neutrino masses; Σm_ν = 63 meV prediction |
| `07_masses_quarks.md` | D₄/A₃ rational cones; tunneling dynamics |
| `08_mixing.md` | CKM from φ⁻² tunneling; PMNS from A₄ + Koide perturbation |
| `09_higgs.md` | m_H = m_Z × φ^(2/3) from A₂ Goldstone geometry (0.34%) [DERIVED] |
| `10_lagrangian.md` | Mass Lagrangian derived; kinetic terms NOT derived [PARTIAL] |
| `11_chirality.md` | V-A from A₂ geometry; leptons have zero R alignment [DERIVED] |
| `12_predictions.md` | Complete summary of all predictions + testable values |

---

## Key Results Summary

| Prediction | Formula | Accuracy | Status |
|------------|---------|----------|--------|
| sin²θ_W | (393-75√5)/968 | 0.6% | [VERIFIED] — `C_verifications/01_weinberg_angle/` |
| m_μ/m_e | Koide (Q=2/3, θ₀=2/9) | 0.001% | [VERIFIED] — `C_verifications/06_leptons/` |
| m_τ/m_e | Koide | 0.007% | [VERIFIED] — `C_verifications/06_leptons/` |
| Δm²₃₁/Δm²₂₁ | Koide (ε=1/√φ) | 2.4% | [VERIFIED] — `C_verifications/06_leptons/` |
| θ_C (Cabibbo) | arctan(φ⁻³) | 2% | [DERIVED] — `C_verifications/08_mixing/` |
| V_ub | V_us × V_cb × φ⁻² | 4% | [DERIVED] — tunneling mechanism |
| PMNS θ₁₃ | Q²/3 rad | 0.6% | [DERIVED] — `C_verifications/08_mixing/` |
| **m_H** | m_Z × φ^(2/3) | **0.34%** | **[DERIVED]** — Q = 2/3 (Koide connection) |

**Derived constants** (not fitted):
- Koide Q = 2/3 (A₂ cone)
- Koide θ₀ = 2/9 rad (θ₀ = Q/3)
- ε_ch = √2 (D₆ root length)
- ε_ν = 1/√φ (φ² constraint: ε²_ch + ε²_ν = φ²)
- M₀ = m_N / 3.0557 (spectral gap ratio)

---

## What Comes Next

Part IV establishes the Standard Model. The remaining Parts address deeper questions:

| Part | Title | Key Questions |
|------|-------|---------------|
| **V** | Spacetime | Time emergence, Lorentz invariance, Gravity |
| **VI** | Quantum Foundations | Measurement problem, Entanglement, Collapse |
| **VII** | Cosmology | Big Bang, Inflation, Dark Matter/Energy |
| **VIII** | Status | Assessment, Open Problems, Falsifiability |

---

## Verification Requirement

Every claim marked **[VERIFIED]** has traceable code in `Appendices/C_verifications/`. Run the scripts to reproduce results.
