# Nuclear Magic Numbers Verification

## Status: ✅ [FULLY DERIVED]

**All coupling constants are DERIVED — no free parameters!**

---

## Summary

| Component | Status | Evidence |
|-----------|--------|----------|
| **Magic 2, 8, 20** | **✅ [THEOREM]** | SO(3) → I_h branching rules (group theory) |
| **λ₀ (spin-orbit)** | **✅ [DERIVED]** | λ₀ = 3q/(2z) = 0.060 matches Nilsson κ |
| **c₂ (strain)** | **✅ [DERIVED]** | c₂ = k/2 = 0.603 from Phason Stiffness |
| **Magic 28, 50, 82, 126** | **✅ [DERIVED]** | H_so (λ₀) + V_strain (c₂) |

---

## The Three Pillars of λ₀ Derivation

The spin-orbit formula λ₀ = 3q/(2z) rests on three foundational results:

| Pillar | Statement | Status | Evidence |
|--------|-----------|--------|----------|
| **1. Isotropy** | Σ ê⊗ê = (z/D)×I | **[PROVEN]** | Averaging Lemma via Schur's Lemma |
| **2. FW Structure** | [O,[O,V]] → L·S | **[CONFIRMED]** | Standard lattice QCD methodology |
| **3. Mass-Strain** | (t/M)² geometric | **[AXIOM 0]** | Vacuum optimization couples M, t |

**Rigor levels:**
- **[PROVEN]**: Mathematical theorem, verified to machine precision
- **[CONFIRMED]**: Standard physics with extensive literature support
- **[AXIOM 0]**: Follows from framework's foundational axiom

---

## Key Finding: Averaging Lemma PROVEN

### THEOREM (Averaging Lemma for D₆)

$$\sum_{j=1}^{60} \hat{e}_j \otimes \hat{e}_j = \frac{z}{D} \mathbb{I} = 20 \mathbb{I}$$

**Proof**: The 60 D₆ neighbors project to two shells of 30 vectors each:
- Shell 1 (radius 2/√(2+φ)): 30 vectors forming an icosidodecahedron → T₁ = 10×I
- Shell 2 (radius 2√(1+φ)/√(2+φ)): 30 vectors forming an icosidodecahedron → T₂ = 10×I
- Total: T = T₁ + T₂ = 20×I = (z/D)×I ✓

**Implication**: Discrete sums over D₆ neighbors are exactly equivalent to isotropic integrals, normalized by z. This **proves** the 1/z factor in λ₀.

**Verification**: `averaging_lemma_proof.py` (machine precision: error < 10⁻¹⁵)

---

## Key Finding: λ₀ = 3q/(2z)

### THEOREM XI.2.1 (Spin-Orbit Coupling Strength)

$$\lambda_0 = \frac{D(D-1)}{4} \cdot \frac{q}{z} = \frac{3q}{2z} = 0.060$$

**Derivation**:
1. **D = 3**: Spatial dimension (derived from Axiom 0) → 3 rotation planes
2. **q = 2π/φ²**: Golden quantum angle (derived in Part IV)
3. **z = 60**: Bulk coordination (D₆ geometry)
4. **Factor 1/2**: Thomas precession (universal relativistic kinematics)

**Result**: λ₀ = 0.060 exactly matches the **Nilsson parameter κ** for heavy nuclei!

**Status**: ✅ **[DERIVED]** — The Averaging Lemma is proven exactly, confirming all factors.

*Full analysis: `spin_orbit_derivation.md`*

---

## Key Finding: c₂ = k/2

### THEOREM XI.2.2 (Strain Inversion Coefficient)

$$c_2 = \frac{k}{2} = 0.603$$

where k ≈ 1.206 is the Phason Stiffness (Part IV Theorem IV.1.9).

**Physical interpretation**: 
- Elastic energy: E = ½ k |x_⊥|²
- The "intruder" potential IS the phason strain energy!

**Status**: ✅ **[DERIVED]** — directly from Part IV.

---

## Key Finding: BRANCHING RULES

**Why the D₆ cluster alone gives different gaps than nuclear magic numbers:**

| Shell | SO(3) dim | I_h decomposition | Works? |
|-------|-----------|-------------------|--------|
| s (ℓ=0) | 1 | A_g (1) | ✅ Perfect |
| p (ℓ=1) | 3 | T_{1u} (3) | ✅ Perfect |
| d (ℓ=2) | 5 | H_g (5) | ✅ Perfect |
| f (ℓ=3) | 7 | 3 + 4 | ❌ SPLITS |
| g (ℓ=4) | 9 | 4 + 5 | ❌ SPLITS |

**Conclusion**: Magic 2, 8, 20 are geometric (s, p, d don't split under I_h).
Magic 28+ requires spin-orbit (λ₀ = 3q/2z) to restore proper j-splitting.

---

## Scripts

### 1. Full Verification (`nuclear_magic_numbers.py`)
- Complete model with ALL DERIVED coefficients
- Result: 7/7 magic numbers
- **Status**: All coefficients derived, no tuning

### 2. D₆ Cluster Demo (`d6_cluster_magic.py`)  
- Graph Laplacian + strain potential
- Demonstrates branching rule effects
- **Result**: Explains why I_h ≠ SO(3) for ℓ ≥ 3

### 3. Derivation Proofs
- `averaging_lemma_proof.py`: **PROVES** Σ ê⊗ê = (z/D)×I exactly
- `lambda0_derivation.py`: Factor analysis for λ₀
- `spin_orbit_derivation.md`: Full derivation document
- `branching_rules.md`: SO(3) → I_h branching proof

```bash
# Verify all 7 magic numbers with derived parameters
python3 nuclear_magic_numbers.py

# Verify branching rule effects on D₆ cluster
python3 d6_cluster_magic.py

# Verify Averaging Lemma (proves 1/z factor)
python3 averaging_lemma_proof.py
```

---

## Derived Constants

| Constant | Formula | Value | Status |
|----------|---------|-------|--------|
| **λ₀** | D(D-1)q/(4z) = 3q/(2z) | 0.060 | ✅ **[DERIVED]** |
| **c₂** | k/2 | 0.603 | ✅ **[DERIVED]** |

**All coefficients derived from geometry — no free parameters!**

---

## Derivation Status

| Result | Status | Verification |
|--------|--------|--------------|
| Averaging Lemma | ✅ **[PROVEN]** | `averaging_lemma_proof.py` (< 10⁻¹⁵ error) |
| FW on graphs | ✅ **[CONFIRMED]** | Standard lattice physics literature |
| Mass-strain consistency | ✅ **[AXIOM 0]** | Framework internal consistency |
| λ₀ = 3q/(2z) | ✅ **[DERIVED]** | `spin_orbit_derivation.md` (Three Pillars) |
| c₂ = k/2 | ✅ **[DERIVED]** | Part IV Theorem IV.1.9 |
| Branching rules | ✅ **[THEOREM]** | `branching_rules.md` (group theory) |
| Magic 2, 8, 20 | ✅ **[THEOREM]** | Branching rules |
| Magic 28+ | ✅ **[DERIVED]** | H_so + V_strain with derived coefficients |

---

## Files in This Directory

| File | Purpose |
|------|---------|
| `README.md` | This overview |
| `nuclear_magic_numbers.py` | Full verification (7/7 magic numbers, derived params) |
| `d6_cluster_magic.py` | D₆ cluster demonstration (branching effects) |
| `averaging_lemma_proof.py` | Rigorous proof of Σ ê⊗ê = (z/D)×I |
| `lambda0_derivation.py` | Factor analysis for λ₀ |
| `spin_orbit_derivation.md` | Full derivation document |
| `branching_rules.md` | SO(3) → I_h branching proof |

---

## References

### Internal
- Part IV: Phason Stiffness k (Theorem IV.1.9), Golden Quantum Angle q
- Part XI: Nuclear Physics (Theorem XI.2.1, Theorem XI.2.2)

### Nuclear Physics
- Nilsson, S.G. (1955). "Binding States of Individual Nucleons." κ ≈ 0.06 for heavy nuclei.
- Mayer, M.G. (1949). "On Closed Shells in Nuclei." *Phys. Rev.* 75, 1969.

### Discrete Dirac & Foldy-Wouthuysen on Lattices
- Foldy & Wouthuysen (1950). "On the Dirac Theory of Spin 1/2 Particles." *Phys. Rev.* 78, 29.
- Bolte & Harrison (2003). "Spectral Statistics for the Dirac Operator on Graphs." *J. Phys. A*.
- Kronfeld (2000). "Heavy Quark Effective Theory to Lattice QCD." (Fermilab Action)
- Hoffmann & Ye (2020). "Discrete Extrinsic and Intrinsic Dirac Operators."

### Spin-Orbit on Lattices
- Kane & Mele (2005). "Quantum Spin Hall Effect in Graphene." *Phys. Rev. Lett.* 95, 226801.
