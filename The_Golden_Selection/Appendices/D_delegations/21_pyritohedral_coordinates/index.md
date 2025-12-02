# Delegation 21: Pyritohedral Coordinate Computation

## Status: 🟡 IN PROGRESS

**Goal**: Compute explicit D₆ coordinates for the 8_L, 8_R, and 4_H vertices in the pyritohedral decomposition of the S₁ and S₄ dodecahedral shells.
**Result**: S₁ coordinates verified; S₄, chirality, quantum numbers pending

---

## Status: 🟢 COMPLETE

**Goal**: Compute explicit D₆ coordinates for the 8_L, 8_R, and 4_H vertices
**Result**: ✅ Radial split confirmed; 8+8+4 preserved across sub-shells; exotic quantum numbers

---

## Summary

| Question | Status | Result |
|----------|--------|--------|
| Q1: ω₃ orbit verification | ✅ | 160 weights, all |v|²=3 |
| Q2: Shell structure | ✅ | 20+60+60+20 confirmed |
| Q3: S₁ geometry | ✅ | **Radial split**: 8 (outer) + 12 (inner) |
| Q4: 8+8+4 decomposition | ✅ | 8_L (outer) + 8_R + 4_H (inner) |
| Q5: Quantum numbers | ✅ | **Exotic** (7/6, 13/12, etc.) — preon model |
| Q6: Grok norm-2 error | ✅ | Explained: used ω₂ not ω₃ |

---

## 🔑 KEY FINDINGS

### 1. Radial Shell Split (CONFIRMED)

The "S₁ shell" (20 vertices) splits into **two radial sub-shells**:

| Sub-shell | R² | Count | Geometry | Label |
|-----------|-----|-------|----------|-------|
| **Outer** | 0.434 | 8 | Cube | 8_L |
| **Inner** | 0.158 | 12 | Pyritohedron | 8_R + 4_H |

The inner 12 further decomposes: **8_R (cube) + 4_H (tetrahedron)**

### 2. Chirality Mechanism

- **8_L**: Outer sub-shell (R² ≈ 0.434)
- **8_R**: Inner sub-shell (R² ≈ 0.158), rotated π/4 from 8_L
- **4_H**: Inner sub-shell, tetrahedron (Higgs)

**Chirality = radial position**, not just T_h orbit assignment.

### 3. Quantum Numbers: EXOTIC

| Q value | Fraction | SM-compatible? |
|---------|----------|----------------|
| +1.17 | 7/6 | ❌ |
| +1.08 | 13/12 | ❌ |
| +0.42 | 5/12 | ❌ |
| ±0.33 | ±1/3 | ✅ (d-quark-like) |

**Interpretation**: ω₃ = **preon/composite layer**, not elementary SM fermions.

### 4. Where Are SM Fermions?

Grok found SM charges because it used **ω₂ (norm 2)** by mistake.

**Hypothesis**: ω₂ hosts elementary fermions; ω₃ hosts preons/composites.

---

## Chronological Log

| # | Date | Type | File | Summary |
|---|------|------|------|---------|
| 1 | 2024-11 | Prompt | `iter_1_prompt.md` | Initial coordinate request |
| 2 | 2024-11 | Response | `iter_1_response.md` | S₁ structure (Gemini) |
| 3 | 2024-11 | Prompt | `iter_2_prompt.md` | S₄, chirality, quantum numbers |
| 4 | 2024-11 | Response | `iter_2_response.md` | Partial S₄, disphenoid (Gemini) |
| 5 | 2024-11 | Cross-check | — | Grok: norm-2 weights |
| 6 | 2024-11 | Prompt | `iter_3_prompt.md` | Reconciliation request |
| 7 | 2024-11 | Response | `iter_3_response.md` | **FINAL: Radial split + exotic Q confirmed** |

---

## Impact on Theory

**Must update `Part_IV_Standard_Model/03_matter.md`**:

1. Radial split: Dodecahedral shell = pseudo-dodecahedron (8 outer + 12 inner)
2. Chirality: L/R from radial position
3. Open question: ω₃ = preons vs ω₂ = fermions

---

## Next Steps
1. ✅ Delegation complete
2. ⬜ Update 03_matter.md with radial split finding
3. ⬜ Investigate ω₂ orbit for SM charges
4. ⬜ Decide: preon model vs direct embedding
