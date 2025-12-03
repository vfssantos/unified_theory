# C. Verifications

Status tracking for each major claim in the theory. Each subfolder documents:
- The claim being verified
- Methods used
- Current results
- Remaining gaps

---

## Verification Summary

| # | Claim | Status | Confidence | Notes |
|---|-------|--------|------------|-------|
| 01 | sin²θ_W = (393-75√5)/968 | ✅ | High | 0.67% error, exact algebraic form |
| 02 | D=3 uniquely selected (Golden Lock) | ✅ | High | Bruna (2025) proves φ⁻² |
| 03 | H₃ is forced symmetry | ✅ | High | Four converging arguments |
| 04 | E₈/D₆ equivalent | ✅ | High | Same predictions, D₆ minimal |
| 05 | 3 generations from geometry | ✅ | High | Occupation domains + φ-ladder |
| 06 | Koide Q = 2/3 from A₂ | ✅ | High | 45° cone condition proven |
| 07 | CKM/PMNS from φ | ✅ | High | All angles < 3% error |
| 08 | m_H = m_Z × φ^(2/3) | ✅ | High | 0.34% error |
| 09 | Quantum emergence | ✅ | High | Topological jamming + Born rule |
| 10 | Scale paradox (CSDR) | ✅ | High | Projection = EWSB at EW scale |
| 11 | Chirality from A₂ | ⚠️ | Medium | Numerical support, needs rigor |

---

## Folder Contents

| Folder | Topic | Key Files |
|--------|-------|-----------|
| `01_weinberg_angle/` | Electroweak mixing | `weinberg.py`, `derivation.md` |
| `02_golden_lock/` | D=3 selection | `README.md` (Bruna reference) |
| `04_generations/` | Three generations | `occupation_domains.py` |
| `05_mass_mechanism/` | Koide + L⊥ | `q_two_thirds.md`, `lagrangian_structure.md` |
| `06_leptons/` | Charged lepton masses | `koide_leptons.py` |
| `07_quarks/` | Quark masses | `quark_koide.py` |
| `07_ckm_pmns/` | Mixing matrices | `ckm_tunneling.py` |
| `08_higgs_mass/` | Higgs mass | `higgs_mass.py` |
| `08_mixing/` | PMNS angles | `ckm_pmns_derivation.py` |
| `09_quantum_emergence/` | QM from topology | `README.md` (jamming + Born) |
| `10_scale_paradox/` | CSDR resolution | `README.md` (why Z-pole) |
| `11_chirality/` | V-A structure | `chirality_projection.py` |

---

## Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| ✅ | Verified | Rigorous derivation complete, matches observation |
| ⚠️ | Partial | Some support, but gaps or ambiguities remain |
| ❌ | Refuted | Calculation contradicts claim |
| 🔄 | In Progress | Actively being worked on |
| ⬜ | Not Started | No verification attempted |

---

## Key Results Summary

### Electroweak Sector
- **Weinberg angle**: sin²θ_W = (393-75√5)/968 ≈ 0.2327 (0.67% error)
- **Higgs mass**: m_H = m_Z × φ^(2/3) = 125.68 GeV (0.34% error)
- **Scale**: Matches Z-pole via CSDR interpretation

### Lepton Masses
- **Q = 2/3**: From 45° A₂ cone condition
- **θ₀ = 2/9**: From θ₀ = Q/3 identity
- **μ/e ratio**: 0.001% error
- **τ/e ratio**: 0.007% error
- **Neutrino sum**: Σm_ν = 63.3 meV (testable)

### Quark Sector
- **Q_up = 6/7**: From D₄ subalgebra
- **Q_down = 11/15**: From A₃ subalgebra
- **CKM V_ub**: 2.7% error via Fibonacci tunneling

### Foundations
- **φ selection**: Bruna (2025) proves unique stationary point at φ⁻²
- **H₃ selection**: Four converging arguments (dimensional, thermodynamic, golden, topological)
- **QM emergence**: Topological jamming requires quantum tunneling
- **Born rule**: Derived from Parseval + Axiom 0

---

## Cross-References to Main Text

| Verification | Theory Section | Calculations |
|--------------|----------------|--------------|
| Weinberg angle | IV.2 | `B_calculations/02_projections/` |
| Golden lock | I.B | (Bruna paper) |
| H₃ selection | I.C | — |
| Generations | IV.4 | `B_calculations/02_projections/` |
| Koide formula | IV.5, IV.6 | `B_calculations/04_mass_formulas/` |
| CKM/PMNS | IV.8 | `B_calculations/05_mixing_angles/` |
| Higgs mass | IV.9 | — |
| QM emergence | IV.1, IV.4 | `B_calculations/06_golden_walk/` |
| Scale paradox | IV.2 | — |
| Chirality | IV.6 | — |
