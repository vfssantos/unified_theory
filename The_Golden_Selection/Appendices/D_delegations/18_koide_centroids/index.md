# Delegation 18: Koide from E⊥ Centroids

## Status: 🟢 COMPLETE (Negative Result — But Informative!)

**Goal**: Test whether Koide's Q = 2/3 emerges from the **angular structure of generation centroids** in the internal space E⊥, rather than from L⊥ eigenvalues.

**Result**: ❌ **Shell centroids vanish** — Weyl symmetry kills naive centroids. But this is **useful**: it confirms Koide needs **symmetry-breaking weights** (e.g., L⊥ eigenvectors).

---

## Summary

| Question | Status | Result |
|----------|--------|--------|
| Q1: Do shell centroids form 120° angles? | ❌ | **NO — All centroids ≈ 0** (Weyl symmetry) |
| Q2: Does Q = 2/3 emerge from centroid structure? | ❌ | **NO — Q undefined (0/0)** |
| Q3: Which 2-plane contains the A₂ structure? | ✅ | **YES — x-y plane of E⊥** (but angles are 45°/90°, not 60°/120°) |
| Q4: How does this connect to mass formula? | ⚠️ | **Needs eigenvector-weighted centroids** |

---

## Background

### Why L⊥ Eigenvalues Failed for Koide

Delegation 16 and 17 exhaustively searched for Koide Q = 2/3 in L⊥ eigenvalues:
- Best Q ≈ 0.61 (8% from 2/3)
- No parameter choice in the (a, b, c) family brings Q closer
- A₂ 120° structure exists in D₆ roots, but NOT in L⊥ eigenvector shell profiles

### The Alternative: Position Space

The Koide formula involves **√m**, suggesting it's about **amplitudes** (positions) not **frequencies** (eigenvalues):

$$Q = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

If masses are related to **positions in E⊥**, then Koide could emerge from the **geometric arrangement** of generation centroids.

### The 120° Hypothesis

The A₂ root system has 6 roots at 60° intervals (or 3 pairs at 120°). If the 3 generations correspond to 3 directions in a 2-plane within E⊥ at 120° angles, this would naturally give Koide's structure.

---

## Key Questions

1. **Shell Centroids**: What are the centroids of S₁, S₂, S₃ in E⊥?
2. **Angular Structure**: Do these centroids form 120° angles (or project to 120° in some 2-plane)?
3. **A₂ Identification**: Which A₂ subalgebra of D₆ corresponds to generations?
4. **Mass Connection**: How do centroid positions relate to √m?

---

## Key Findings (Iteration 1)

### 1. Shell Structure

The ω₃ orbit has **12 distinct radial shells** (by |v⊥|²), not 4:

| Shell | |v⊥|² | Count |
|-------|-------|-------|
| 1 | 0.158 | 12 |
| 2 | 0.329 | 16 |
| 3 | 0.500 | 8 |
| ... | ... | ... |
| 12 | 3.565 | 8 |

**Important**: These are **radial shells**, NOT the 20/60/60/20 L⊥ eigenbands!

### 2. All Centroids Vanish

For **every** radial shell (all 12):
- Unweighted centroid: **|c| ≈ 0** (to 10⁻¹⁷)
- |v⊥|²-weighted centroid: **|c| ≈ 0** (to 10⁻¹⁷)

**Reason**: Weyl symmetry — for each weight, there's a Weyl image that cancels it.

### 3. A₂ Plane Identified

The A₂ roots (e_i - e_j for i,j ∈ {1,2,3}) project to the **x-y plane of E⊥**.

But angles in this plane are **45°/90°/135°**, NOT 60°/120°!

This is because the Koca–Al-Siyabi projection doesn't preserve Euclidean angles.

### 4. Koide Tests Failed

- **From shell centroids**: Q = 0/0 (undefined — centroids vanish)
- **From radial radii**: Best Q ≈ 0.50, far from 2/3
- **From sector partition**: Best Q ≈ 0.34, still far from 2/3

---

## Critical Insight from E₈ Documents

The `E_appendix_calculations.md` reveals the **actual Koide mechanism**:

### The Real Koide Mechanism (E₈ Theory)

1. **Koide is NOT about shell centroids** — it's about **specific A₂ triples of roots**
2. **400 A₂ triples exist** in the inner 600-cell with perfect 120° geometry
3. **Explicit lepton triple found**: Roots #2, #7, #30 with heights (-2, +1, +1)
4. **The Koide phase θ₀ ≈ 347°** sets mass ratios, NOT height or shell position

### The Mass Formula (from E.13)

$$\sqrt{m_i} = M_0 \left(1 + \sqrt{2}\cos\left(\theta_0 + \frac{2\pi i}{3}\right)\right)$$

where:
- **θ₀ ≈ 347°** (or equivalently 360° - arctan(φ⁻³))
- The **120° spacing** (2πi/3) gives Q = 2/3 automatically
- **Height h selects WHICH roots**, not mass magnitude

### Why Quarks Don't Fit Koide

| Sector | Q value | Koide? |
|--------|---------|--------|
| Leptons | **0.6667** | ✅ Exact |
| Up quarks | 0.849 | ❌ No |
| Down quarks | 0.731 | ❌ No |

**Only leptons satisfy Koide!** Quarks need a different mechanism (Q = 6/7 for up, Q = 11/15 for down).

---

## Implications for D₆ Theory

### What This Means

1. **Naive shell centroids don't work** — Weyl symmetry kills them
2. **Koide needs specific root triples**, not shell averages
3. **The mechanism is angular (θ₀)**, not positional (centroids)
4. **Need to find A₂ triples in D₆** that mirror the E₈ structure

### Next Steps

1. **Eigenvector-weighted centroids**: Use L⊥ eigenvectors to break Weyl symmetry
2. **Find D₆ A₂ triples**: Look for 120° triples in D₆ roots (not ω₃ weights)
3. **Port E₈ mechanism**: The E₈ theory has explicit roots — adapt to D₆

---

## Chronological Log

| Iter | Date | Files | Summary |
|------|------|-------|---------|
| 1 | 2025-11 | `iter_1_prompt.md` | Request: Compute centroids and test 120° hypothesis |
| 1 | 2025-11 | `iter_1_response.md` | **All centroids vanish** — Weyl symmetry; A₂ plane found but wrong angles |

---

## Verdict Table

| Finding | Status | Confidence |
|---------|--------|------------|
| 120° in shell centroids | **NOT FOUND** | High |
| Koide Q = 2/3 from centroids | **NOT FOUND** | High |
| A₂ plane in E⊥ | **FOUND** (x-y plane) | High |
| Angles are 60°/120° | **NO** (45°/90°) | High |
| Koide needs symmetry-breaking | **SUPPORTED** | High |

---

## References

- **Delegation 16**: L⊥ operator — Koide NOT found in eigenvalues
- **Delegation 17**: Axiom 0 selection — Koide still NOT found with parameter scan
- **E₈ Document**: "generations at 120° in an internal 2-plane"
- **E_appendix_calculations.md**: **KEY** — Explicit Koide mechanism with A₂ triples

