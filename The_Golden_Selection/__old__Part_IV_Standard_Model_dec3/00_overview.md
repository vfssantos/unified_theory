# Part IV: The Standard Model — Physics from Geometry

## Overview

Parts I–III established the D₆ → H₃ quasicrystal with golden ratio scaling and 3D internal space E⊥. Part IV derives the **Standard Model** from this geometry in a coherent narrative arc: from the emergence of spacetime to the specific mass values of fermions.

**The central result**: Starting from the D₆ lattice and H₃ projection (no free parameters), we derive 20+ observables with typical accuracies of 0.1–5%.

---

## The Narrative Arc

```
THE STAGE (IV.1-3)           THE ACTORS (IV.4-5)       THE SCRIPT (IV.6-7)
Spacetime, Planck Scale      Gauge Groups &            Dynamics &
& General Relativity         Fermion Content           Lagrangian
      │                           │                         │
      ▼                           ▼                         ▼
IV.1 Spacetime (c=1)         IV.4 Gauge                IV.6 Dynamics
IV.2 Planck Scale (G)        IV.5 Fermions             IV.7 Lagrangian
IV.3 Gravity (Einstein)
                                  │
          ┌───────────────────────┴────────────────────────┐
          ▼                                                ▼
THE TWIST (IV.8-10)                              THE RESULT (IV.11-14)
Chirality & Symmetry                             Mass Spectrum &
Breaking (Higgs)                                 Mixing Angles
          │                                                │
          ▼                                                ▼
IV.8 Chirality (V-A)                             IV.11 Generations
IV.9 Electroweak (θ_W)                           IV.12 Mass Mechanism
IV.10 Higgs (m_H)                                IV.13 Leptons/Quarks
                                                 IV.14 Mixing (CKM/PMNS)
```

---

## What This Part Proves

| Section | Topic | Key Question | Answer | Status |
|---------|-------|--------------|--------|--------|
| **IV.1** | Spacetime | What is time? | D₆ geodesic distance; c=1; Lorentz to 3% | **[DERIVED]** |
| **IV.2** | Planck Scale | What sets the scale? | q=2π/φ² (stability); k≈1.21; a/l_P≈√2 | **[DERIVED]** |
| **IV.3** | Gravity | Why is G so small? | Sakharov: G = kc³/K; Einstein from elasticity | **[DERIVED]** |
| **IV.4** | Gauge | Where do forces come from? | SU(3)×SU(2)×U(1) from D₆ subalgebras | [VERIFIED] |
| **IV.5** | Fermions | What is matter? | ω₅ spinor → 32 states per generation | [VERIFIED] |
| **IV.6** | Dynamics | How do they move? | Quantum walk → Dirac equation | [OPEN] |
| **IV.7** | Lagrangian | How do they interact? | Mass term derived; kinetic terms pending | [PARTIAL] |
| **IV.8** | Chirality | Why parity violation? | Leptons: R alignment = 0; L/R ≈ √5 | [DERIVED] |
| **IV.9** | Electroweak | What is sin²θ_W? | (393-75√5)/968 ≈ 0.2327 (0.6% error) | [VERIFIED] |
| **IV.10** | Higgs | What is the Higgs mass? | m_H = m_Z × φ^(2/3) = 125.68 GeV | [DERIVED] |
| **IV.11** | Generations | Why three families? | Core/Shell/Skin occupation domains | [DERIVED] |
| **IV.12** | Mass Mech | What sets mass scales? | L⊥ (radial) + Koide (angular) | [DERIVED] |
| **IV.13** | Masses | Lepton/Quark masses? | Koide Q=2/3; rational tunneling | [VERIFIED] |
| **IV.14** | Mixing | CKM and PMNS? | Geometric overlaps + φ⁻² tunneling | [DERIVED] |

---

## Files in This Part

### Section A: Spacetime & Gravity (The Stage)
- **`01_spacetime.md`**: Time as D₆ geodesic; c=1; Lorentz invariance; Planck scale derivation.
- **`02_gauge.md`**: D₆ subalgebras → SM gauge group; shell placement verified.
- **`03_gravity.md`**: Einstein equations from Sakharov induced gravity; G = kc³/K.

### Section B: Matter & Forces (The Actors)
- **`04_gauge.md`**: Gauge symmetry SU(3)×SU(2)×U(1) from D₆ structure.
- **`05_fermions.md`**: ω₅ spinor reproduces all SM quantum numbers exactly.

### Section C: Dynamics (The Script)
- **`06_dynamics.md`**: Derivation of Dirac equation (quantum walk) and Yang-Mills (Wilson loops).
- **`07_lagrangian.md`**: Assembling the pieces. Mass term derived; kinetic terms from 06.

### Section D: Electroweak Geometry (The Twist)
- **`08_chirality.md`**: V-A structure from A₂ geometry; leptons have zero R alignment.
- **`09_electroweak.md`**: Weinberg angle from projection anisotropy.
- **`10_higgs.md`**: m_H = m_Z × φ^(2/3) from A₂ Goldstone geometry.

### Section E: The Mass Spectrum (The Result)
- **`11_generations.md`**: φ² : φ : 1 occupation domains → three families.
- **`12_mass_mechanism.md`**: L⊥ operator (radial) ⊥ Koide geometry (angular).
- **`13_masses.md`**: Charged + neutrino masses; Σm_ν = 63 meV prediction.
- **`14_mixing.md`**: CKM from φ⁻² tunneling; PMNS from A₄ + Koide perturbation.

---

## Key Results Summary

| Prediction | Formula | Accuracy | Status |
|------------|---------|----------|--------|
| **c = 1** | Hyperspace geodesic time | **2%** | [DERIVED] |
| **a/l_P** | √(q/k) ≈ √2 | — | [DERIVED] |
| **G** | kc³/K (Sakharov) | — | [DERIVED] |
| **sin²θ_W** | (393-75√5)/968 | **0.6%** | [VERIFIED] |
| **m_μ/m_e** | Koide (Q=2/3) | **0.001%** | [VERIFIED] |
| **m_τ/m_e** | Koide (Q=2/3) | **0.007%** | [VERIFIED] |
| **m_H** | m_Z × φ^(2/3) | **0.34%** | [DERIVED] |
| **L/R Chirality** | ≈ √5 = φ + φ⁻¹ | **3%** | [DERIVED] |
| **PMNS θ₁₃** | Q²/3 rad | **0.6%** | [DERIVED] |

**Derived constants** (not fitted):
- Golden quantum angle: q = 2π/φ² (from stability)
- Phason stiffness: k ≈ 1.21 (geometric invariant)
- Koide Q = 2/3 (A₂ cone)
- Koide θ₀ = 2/9 rad (θ₀ = Q/3)
- ε_ch = √2 (D₆ root length)
- ε_ν = 1/√φ (φ² constraint)
- M₀ = m_N / 3.0557 (spectral gap ratio)

---

## What Comes Next

Part IV establishes the Standard Model + General Relativity. The remaining Parts address deeper questions:

- **Part V (Quantum)**: Measurement problem, entanglement, collapse.
- **Part VI (Cosmology)**: Big Bang, inflation, dark matter/energy.
- **Part VII (Status)**: Assessment, open problems, falsifiability.
