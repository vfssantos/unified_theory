# Appendices

This folder contains all supporting material for The Golden Selection theory:
- Research reports from literature review
- Numerical calculations and verifications
- Verification status for each claim
- Delegation tasks for external research
- Reference materials

---

## Folder Structure

```
Appendices/
│
├── A_research_reports/       # Deep research reports (literature review)
│   ├── R1_*.md              # Dimensional selection research
│   └── R2_*.md              # Hopfion/phason research
│
├── B_calculations/           # Numerical/symbolic calculations
│   ├── 01_e8_roots/         # E₈ lattice and root system
│   ├── 02_projections/      # Elser-Sloane and golden projections
│   ├── 03_gauge_couplings/  # Coupling constant calculations
│   ├── 04_mass_formulas/    # Mass predictions (Koide, Higgs, etc.)
│   └── 05_mixing_angles/    # CKM/PMNS angle calculations
│
├── C_verifications/          # Verification status for each major claim
│   ├── 01_weinberg_angle/   # sin²θ_W = (3/8)φ⁻¹
│   ├── 02_golden_lock/      # D=3 selection mechanism
│   ├── 03_h3_selection/     # Why icosahedral symmetry
│   ├── 04_e8_uniqueness/    # E₈ as unique minimal lattice
│   ├── 05_generations/      # Three generations from 600-cell
│   ├── 06_koide/            # Koide formula from A₂ geometry
│   ├── 07_ckm_pmns/         # Mixing angles from golden geometry
│   ├── 08_higgs_mass/       # m_H = m_Z × (15/11)
│   ├── 09_mirror_fermions/  # Mirror sector predictions
│   └── 10_cosmology/        # Dark energy / slice field
│
├── D_delegations/            # Tasks delegated to research agents
│   ├── delegation_prompts.md # Master list of all prompts
│   ├── pending/             # Tasks not yet assigned
│   ├── in_progress/         # Tasks currently being researched
│   └── completed/           # Finished research with results
│
├── E_references/             # Bibliography and reference materials
│
└── scripts/                  # Python/Mathematica verification scripts
```

---

## Quick Links

### Research Reports (Completed)
| Report | Topic | Supports |
|--------|-------|----------|
| [R1_full_report.md](A_research_reports/R1_full_report.md) | Graph minors, Colin de Verdière, Zeeman | Theorem I.B.1 |
| [R2_full_report.md](A_research_reports/R2_full_report.md) | Hopfions, phason topology, Golden Lock | Theorem I.B.2 |

### Delegation Tasks
| Priority | Task | Status |
|----------|------|--------|
| 🔴 HIGH | Weinberg Angle Root Calculation | Pending |
| 🔴 HIGH | Golden Lock Rigorous Proof | Pending |
| 🔴 HIGH | Three Generations Mechanism | Pending |
| 🟡 MEDIUM | H₃ Selection Justification | Pending |
| 🟡 MEDIUM | E₈ Uniqueness Verification | Pending |
| 🟡 MEDIUM | Koide Formula Derivation | Pending |
| 🟡 MEDIUM | CKM/PMNS Angles | Pending |
| 🟡 MEDIUM | Higgs Mass Formula | Pending |
| 🟢 LOW | Mirror Fermions | Pending |
| 🟢 LOW | Cosmology Predictions | Pending |

See [D_delegations/delegation_prompts.md](D_delegations/delegation_prompts.md) for full prompts.

---

## Verification Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified (calculation complete, matches theory) |
| ⚠️ | Partial (some aspects verified, gaps remain) |
| ❌ | Refuted (calculation contradicts claim) |
| 🔄 | In Progress |
| ⬜ | Not Started |

---

## How to Add New Material

### Adding a Calculation
1. Create file in `B_calculations/[category]/`
2. Include: code, inputs, outputs, interpretation
3. Update verification status in `C_verifications/`

### Adding a Verification
1. Create `README.md` in `C_verifications/[topic]/`
2. Document: claim, method, result, status
3. Link to supporting calculations

### Adding Delegation Results
1. Move task file from `in_progress/` to `completed/`
2. Create summary in relevant `C_verifications/` folder
3. Update main theory documents if needed

---

## Key External References

### Dimension Selection (D=3)
- Zeeman (1963) "Unknotting combinatorial balls" — *Annals of Mathematics*
- Colin de Verdière (1990) "Sur un nouvel invariant" — *J. Comb. Theory B*
- Conway & Gordon (1983) "Knots and links in spatial graphs" — *J. Graph Theory*

### E₈ and Projections
- Elser & Sloane (1987) "Highly symmetric 4D quasicrystal" — *J. Physics A*
- Conway & Sloane (1999) *Sphere Packings, Lattices and Groups* — Springer

### Quasicrystal Theory
- de Bruijn (1981) "Algebraic theory of Penrose tilings" — *Proc. KNAW*
- Levine & Steinhardt (1984) "Quasicrystals" — *Physical Review Letters*
