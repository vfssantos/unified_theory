# The Golden Selection

## A Theory of Geometric Selection

This document presents the **Golden Selection** theory — a framework that derives the fundamental parameters of physics from a single variational principle.

---

## The Axiom

> **AXIOM 0 (Geometric Free Energy Principle)**:
>
> Reality minimizes Geometric Variational Free Energy:
> $$F[\mathcal{G}] = E_{\text{strain}} + \lambda \cdot \kappa_{\text{Schur}}$$
> subject to stable Markov blanket (topological boundary).

---

## Document Structure

```
Part 0: The Axiom
├── 00_overview.md      ← The Geometric Free Energy Principle
└── 01_definitions.md   ← Key definitions

Part I: Selection (What does the axiom select?)
├── 00_overview.md
├── 01_dimension.md     ← D = 3 from blanket stability
├── 02_ratio.md         ← φ from Schur-convexity
└── 03_symmetry.md      ← H₃ from maximal isotropy

Part II: Realization (How is it implemented?)
├── 00_overview.md
├── 01_projection.md    ← Cut-and-project necessity
├── 02_lattice.md       ← D₆ as minimal embedding
└── 03_verification.md  ← φ emerges as eigenvalue

Part III: The Quasicrystal (The physical system)
├── 00_overview.md
├── 01_structure.md     ← Shells and geometry
├── 02_phasons.md       ← Internal degrees of freedom
├── 03_topology.md      ← Defects and jamming
└── 04_experiment.md    ← Experimental connections

Part IV: The Standard Model (Particle physics)
├── 00_overview.md
├── 01_gauge.md         ← SU(3)×SU(2)×U(1) from subalgebras
├── 02_electroweak.md   ← Weinberg angle (0.6% accuracy)
├── 03_fermions.md      ← ω₅ spinor → SM spectrum
├── 04_generations.md   ← Three families from E⊥
├── 05_mass_mechanism.md ← L⊥ + Koide geometry
├── 06_masses_leptons.md ← Charged + neutrino masses
├── 07_masses_quarks.md  ← Quark mass ratios
├── 08_mixing.md        ← CKM + PMNS matrices
├── 09_higgs.md         ← S₄ anomaly → Higgs sector [CONJECTURE]
├── 10_lagrangian.md    ← Interactions from geometry [OPEN]
├── 11_chirality.md     ← V-A structure [OPEN]
└── 12_predictions.md   ← Complete prediction summary

Part V: Spacetime (The arena of reality)
├── 00_overview.md
├── 01_time_emergence.md ← Time = Computation [CONJECTURE]
├── 02_quantum_walk.md   ← Dirac equation from lattice [OPEN]
├── 03_lorentz.md        ← Emergent Lorentz invariance [OPEN]
├── 04_gravity.md        ← GR from quasicrystal [SPECULATIVE]
└── 05_black_holes.md    ← Information paradox [SPECULATIVE]

Part VI: Quantum Foundations (The rules of reality)
├── 00_overview.md
├── 01_measurement.md    ← Measurement problem [SPECULATIVE]
├── 02_entanglement.md   ← Non-locality [SPECULATIVE]
├── 03_collapse.md       ← Wave function collapse [PHILOSOPHICAL]
└── 04_decoherence.md    ← Classical emergence [SPECULATIVE]

Part VII: Cosmology (The history of reality)
├── 00_overview.md
├── 01_big_bang.md       ← Initial conditions [SPECULATIVE]
├── 02_inflation.md      ← Phason-driven expansion [SPECULATIVE]
├── 03_dark_matter.md    ← DM candidates [CONJECTURE]
├── 04_dark_energy.md    ← Λ from geometry [CONJECTURE]
└── 05_arrow_of_time.md  ← Entropy direction [SPECULATIVE]

Part VIII: Status (Assessment)
├── 00_overview.md       ← Complete assessment & open problems

Part IX: Ontology (What things are)
├── 00_overview.md       ← The philosophical dictionary
├── 01_dynamics.md       ← Mass, Energy, Momentum, Inertia
├── 02_spacetime.md      ← Space, Time, Causality
├── 03_forces.md         ← Charge, Magnetism, Strong, Weak, Gravity
├── 04_thermodynamics.md ← Temperature, Entropy, Heat
├── 05_quantum.md        ← Wave Function, Superposition, Entanglement, Measurement, Spin
└── 06_existence.md      ← Particle, Field, Vacuum, Information, Existence

Appendices/
├── A_research_reports/  ← Deep research summaries
├── B_calculations/      ← Explicit computations
├── C_verifications/     ← Numerical checks
├── D_delegations/       ← Research agent Q&A
└── E_references/        ← Bibliography
```

---

## The Logic Chain

```
AXIOM 0: Minimize F (blanket stable)
      ↓
I.A: Blanket stability → D = 3 (Zeeman)
      ↓
I.B: κ_Schur minimization → φ (Bruna)
      ↓
I.C: Max isotropy + φ + D=3 → H₃
      ↓
II.A-C: D₆ lattice via cut-and-project
      ↓
II.D: φ emerges as eigenvalue (verification)
      ↓
III: Physical Quasicrystal (Phasons)
      ↓
IV: Standard Model (Gauge, Fermions, Masses, Mixing)
      ↓
V: Spacetime (Time, Lorentz, Gravity)
      ↓
VI: Quantum Foundations
      ↓
VII: Cosmology
      ↓
VIII: Assessment & Open Problems
      ↓
IX: Ontology (What things are)
```

---

## Key Results

### Verified Predictions (12)

| Result | Accuracy | Section |
|--------|----------|---------|
| sin²θ_W = 0.2327 | 0.6% | IV.2 |
| m_μ/m_e | 0.001% | IV.6 |
| m_τ/m_e | 0.007% | IV.6 |
| Δm²₃₁/Δm²₂₁ | 2.4% | IV.6 |
| V_us (Cabibbo) | 2.1% | IV.8 |
| V_cb | 7.8% | IV.8 |
| V_ub | 2.7% | IV.8 |
| δ_CP | 4.7% | IV.8 |
| θ₁₃ (PMNS) | 0.6% | IV.8 |
| θ₂₃ (PMNS) | 0.3% | IV.8 |
| θ₁₂ (PMNS) | 0.5% | IV.8 |

### Derived (No Free Parameters)

| Result | Status | Section |
|--------|--------|---------|
| D = 3 uniquely selected | [PROVEN] | I.1 |
| φ from Schur-convexity | [PROVEN] | I.2 |
| H₃ from four pillars | [DERIVED] | I.3 |
| D₆ is minimal lattice | [DERIVED] | II.2 |
| SU(3)×SU(2)×U(1) | [VERIFIED] | IV.1 |
| 3 generations | [DERIVED] | IV.4 |
| Koide Q = 2/3, θ₀ = 2/9 | [DERIVED] | IV.5 |

### Open Problems

| Problem | Priority | Section |
|---------|----------|---------|
| Time emergence | **CRITICAL** | V.1 |
| Lorentz invariance | **CRITICAL** | V.3 |
| Higgs mass m_H = 125 GeV | HIGH | IV.10 |
| Chirality (V-A) | HIGH | IV.12 |
| Gravity | MEDIUM | V.4 |
| Dark matter | MEDIUM | VII.3 |

---

## Reading Order

1. Start with **Part 0** (the axiom)
2. Read **Part I** for the mathematical derivations
3. Read **Part II** for geometric implementation
4. Read **Part III** for the physical quasicrystal system
5. Read **Part IV** for particle physics predictions
6. Read **Part V** for spacetime dynamics (in development)
7. Skim **Parts VI–VII** for speculative extensions
8. Read **Part VIII** for honest assessment
9. Consult **Appendices** for details and verification code

---

## Status

| Part | Status | Rigor |
|------|--------|-------|
| **0–II** | Complete | Strong (mathematical) |
| **III** | Complete | Solid (physical) |
| **IV.1–9** | Complete | Strong (verified predictions) |
| **IV.10–12** | Outlines | Conjecture/Open |
| **V** | Overview | Critical gap |
| **VI** | Overview | Speculative |
| **VII** | Overview | Speculative |
| **VIII** | Complete | Assessment |
| **IX** | Complete | Philosophical |
| **Appendices** | Extensive | Supporting material |
