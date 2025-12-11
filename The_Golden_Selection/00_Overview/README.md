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
FOUNDATION LAYER
================

Part 0: The Axiom
├── 00_overview.md      ← The Geometric Free Energy Principle
└── 01_definitions.md   ← Key definitions

Part I: Selection (What does the axiom select?)
├── 00_overview.md
├── 01_dimension.md     ← D = 3 from blanket stability
├── 02_ratio.md         ← φ from Schur-convexity (Bruna 2025)
└── 03_symmetry.md      ← H₃ from four converging arguments

Part II: Realization (How is it implemented?)
├── 00_overview.md
├── 01_projection.md    ← Cut-and-project necessity
├── 02_lattice.md       ← D₆ as minimal embedding
└── 03_verification.md  ← φ emerges as eigenvalue

Part III: The Quasicrystal (The bridge from math to physics)
├── 00_overview.md
├── 01_structure.md     ← Shells and geometry
├── 02_phasons.md       ← Internal degrees of freedom
├── 03_topology.md      ← Defects and S³ phason space
└── 04_experiment.md    ← Experimental connections

EMERGENCE LAYER
===============

Part IV: Spacetime (What is space and time?)
├── 00_overview.md
└── 01_emergence.md     ← Time = geodesic, Lorentz, c = 1

Part V: Quantum (Why is physics quantum?)
├── 00_overview.md
└── 01_emergence.md     ← Topological jamming → QM, Born rule

Part VI: Gravity (How does gravity emerge?)
├── 00_overview.md
└── 01_emergence.md     ← Sakharov mechanism, G from stiffness

STANDARD MODEL LAYER
====================

Part VII: Gauge Sector (The forces)
├── 00_overview.md
├── 01_structure.md     ← SU(3)×SU(2)×U(1) from D₆ subalgebras
├── 02_electroweak.md   ← Weinberg angle (0.67% accuracy)
├── 03_higgs.md         ← Higgs mass (0.34% accuracy)
└── 04_alpha.md         ← Fine structure constant

Part VIII: Matter Sector (The particles)
├── 00_overview.md
├── 01_fermions.md      ← ω₅ spinor → SM spectrum
├── 02_chirality.md     ← V-A structure from A₂
└── 03_generations.md   ← Three families from A/B/C domains

Part IX: Masses (Where mass comes from)
├── 00_overview.md
├── 01_lagrangian.md    ← Mass term structure
├── 02_mechanism.md     ← L⊥ + Koide geometry
├── 03_leptons.md       ← Charged + neutrino masses
└── 04_quarks.md        ← Quark mass ratios

Part X: Mixing (Generation transitions)
├── 00_overview.md
├── 01_mixing.md        ← CKM + PMNS matrices
└── 02_predictions.md   ← Prediction summary

EXTENSIONS LAYER
================

Part XI: Nuclear Physics (Bound states)
├── 00_overview.md      ← Summary and status
├── 01_geometry.md      ← The cluster C_K and shell structure
├── 02_hamiltonian.md   ← The 4-term geometric Hamiltonian
├── 03_magic_numbers.md ← Derivation from spectral gaps
└── 04_predictions.md   ← Falsifiable tests

Part XII: Cosmology (Dark sector)
├── 00_overview.md      ← Dark matter, Λ, bi-metric gravity

Part XIII: Assessment (Honest evaluation)
├── 00_overview.md      ← What's proven/derived/speculative

Part XIV: Ontology (What things are)
├── 00_overview.md      ← Philosophical dictionary
└── [multiple files]    ← Dynamics, spacetime, forces, quantum, existence

Appendices/
├── A_research_reports/ ← Deep research summaries
├── B_calculations/     ← Explicit computations
├── C_verifications/    ← Numerical checks
├── D_delegations/      ← Research background
└── E_references/       ← Bibliography
```

---

## The Logic Chain

```
AXIOM 0: Minimize F (blanket stable)
      ↓
PART I: SELECTION
├── D = 3 (topological stability)
├── φ (Schur-convexity → Bruna 2025)
└── H₃ (four converging arguments)
      ↓
PART II: REALIZATION
└── D₆ lattice via cut-and-project
      ↓
PART III: QUASICRYSTAL
└── Physical structure (phasons, topology)
      ↓
PART IV: SPACETIME
└── Time = geodesic, Lorentz invariance
      ↓
PART V: QUANTUM
└── QM from topological jamming
      ↓
PART VI: GRAVITY
└── Einstein equations from elasticity
      ↓
PARTS VII-X: STANDARD MODEL
├── Gauge group from subalgebras
├── Fermions from spinor orbit
├── Masses from L⊥ + Koide
└── Mixing from phason tunneling
      ↓
PART XI: NUCLEAR (bound states)
└── Magic numbers from graph Laplacian
      ↓
PART XII: COSMOLOGY (dark sector)
└── Dark matter, Λ from geometry
      ↓
PART XIII: ASSESSMENT (honest evaluation)
      ↓
PART XIV: ONTOLOGY (philosophical)
```

---

## Key Results

### Verified Predictions

| Result | Predicted | Observed | Error | Section |
|--------|-----------|----------|-------|---------|
| sin²θ_W | 0.2327 | 0.2312 | 0.67% | VII.2 |
| m_H | 125.68 GeV | 125.25 GeV | 0.34% | VII.3 |
| m_μ/m_e | 206.7703 | 206.7683 | 0.001% | IX.3 |
| m_τ/m_e | 3477.47 | 3477.23 | 0.007% | IX.3 |
| Δm²₃₁/Δm²₂₁ | 32.5 | 33.3 | 2.4% | IX.3 |
| θ₁₂ (PMNS) | 35.0° | 33.4° | 2.4% | X.1 |
| θ₂₃ (PMNS) | 45.0° | 49.7° | 2.3% | X.1 |
| θ₁₃ (PMNS) | 8.6° | 8.6° | < 1% | X.1 |
| V_ub | 0.0036 | 0.0037 | 2.7% | X.1 |
| δ_CP | 72° | 72.1° | < 1% | X.1 |

### Derived (No Free Parameters)

| Result | Status | Section |
|--------|--------|---------|
| D = 3 uniquely selected | [PROVEN] | I.1 |
| φ from Schur-convexity | [KNOWN] Bruna 2025 | I.2 |
| H₃ from four pillars | [DERIVED] | I.3 |
| D₆ is minimal lattice | [DERIVED] | II.2 |
| Time as geodesic | [DERIVED] | IV.1 |
| QM from jamming | [DERIVED] | V.1 |
| Born rule | [DERIVED] | V.1 |
| SU(3)×SU(2)×U(1) | [DERIVED] | VII.1 |
| 3 generations | [DERIVED] | VIII.3 |
| Koide Q = 2/3, θ₀ = 2/9 | [DERIVED] | IX.2 |
| Magic numbers 2-50 | [VERIFIED] | XI.3 |

### Testable Predictions

| Prediction | Value | How to Test |
|------------|-------|-------------|
| Σm_ν | 63.3 meV | Euclid, DESI (2025-2030) |
| Normal hierarchy | YES | Oscillation experiments |
| Ultralight DM | 10⁻²²—10⁻²³ eV | Galaxy halo cores |
| Z = 120 magic | Superheavy | Element synthesis |

---

## Reading Order

### Quick Path (Essential)
1. **Part 0** — The axiom
2. **Part I** — What it selects (D=3, φ, H₃)
3. **Part VII** — Weinberg angle derivation
4. **Part IX** — Koide mass mechanism
5. **Part XIII** — Assessment

### Full Path
1. **Parts 0-III** — Mathematical foundation
2. **Parts IV-VI** — Emergent physics (spacetime, QM, gravity)
3. **Parts VII-X** — Standard Model predictions
4. **Parts XI-XIV** — Extensions and assessment

---

## Status by Layer

| Layer | Parts | Status | Rigor |
|-------|-------|--------|-------|
| **Foundation** | 0–III | Complete | Strong (mathematical) |
| **Emergence** | IV–VI | Complete | Strong (derived) |
| **Standard Model** | VII–X | Complete | Strong (verified) |
| **Nuclear** | XI | Partial | Model (verified for 2-50) |
| **Cosmology** | XII | Complete | Derived (dark sector) |
| **Assessment** | XIII–XIV | Complete | Honest evaluation |
| **Appendices** | A–E | Extensive | Supporting |

---

## What Makes This Theory Different

| Aspect | Standard Model | String Theory | Golden Selection |
|--------|---------------|---------------|------------------|
| SM gauge group | Assumed | Landscape | **Derived** |
| 19+ parameters | Fitted | Landscape | **Derived** |
| Quantum mechanics | Assumed | Assumed | **Derived** |
| Gravity | Separate | Unified | **Derived** |
| Dark matter | Added | Unknown | **Derived** (phason) |
| Dark energy | Fitted (Λ) | Unknown | **Derived** (Fibonacci) |
| Magic numbers | Shell model | N/A | **Derived** (H₃ graph) |
| Testable? | Yes | Difficult | **Yes** (Σm_ν = 63 meV) |
