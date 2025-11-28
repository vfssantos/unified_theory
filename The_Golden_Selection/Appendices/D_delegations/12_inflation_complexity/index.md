# Delegation 12: Inflation Symmetry and Statistical Complexity

## Status: 🟡 IN PROGRESS

**Goal**: Verify that $C_\mu \to \infty$ specifically requires **inflation symmetry** (substitution rules), not just aperiodicity.

**Motivation**: The current argument in Part I.A conflates "aperiodic" with "quasicrystal." There are many aperiodic structures (incommensurate crystals, limit-periodic, non-substitutive Sturmian) that may not have unbounded statistical complexity. We need to verify that inflation symmetry is the distinguishing property.

**Result**: [Pending]

---

## Background

### The Gap Identified

| Structure Type | Periodic? | Inflation Symmetry? | $C_\mu$? |
|----------------|-----------|---------------------|----------|
| Crystal | Yes | No | Bounded |
| Incommensurate crystal | No | No | ? |
| Limit-periodic | No | No | ? |
| Sturmian (non-substitutive) | No | No | ? |
| **Substitution tiling** | No | **Yes** | → ∞ (claimed) |

### The Proposed Fix

If confirmed, the logic chain becomes:

```
I.A: C_μ → ∞ requires INFLATION SYMMETRY (not just aperiodicity)
I.B: Stable μ(G) ≥ 6 requires D = 3
I.C: H₃ selected among 3D inflation tilings (isotropic C_μ)
II: H₃ + cut-and-project FORCES φ-inflation
```

---

## Key Questions

| # | Question | Status | Result |
|---|----------|--------|--------|
| Q1 | Do substitution tilings have $C_\mu \to \infty$? | ⬜ | |
| Q2 | Do limit-periodic structures have bounded $C_\mu$? | ⬜ | |
| Q3 | Do incommensurate crystals have bounded $C_\mu$? | ⬜ | |
| Q4 | Do non-substitutive Sturmian sequences have bounded $C_\mu$? | ⬜ | |
| Q5 | Does H₃ cut-and-project force inflation symmetry? | ⬜ | |

---

## Key Gaps

| Gap | Impact | Priority |
|-----|--------|----------|
| Inflation ↔ $C_\mu$ equivalence | Core claim of I.A | **CRITICAL** |
| H₃ → inflation connection | Links I.C to II | **HIGH** |
| Non-inflation $C_\mu$ bounds | Eliminates alternatives | **HIGH** |

---

## Chronological Log

| # | Date | Type | File | Summary |
|---|------|------|------|---------|
| 1 | 2025-11 | Prompt | `iter_1_prompt.md` | Initial investigation |

---

## Next Steps

1. Await iter_1 response
2. If confirmed: Update Part I.A theorem statement
3. If complicated: Revise argument or add caveats

