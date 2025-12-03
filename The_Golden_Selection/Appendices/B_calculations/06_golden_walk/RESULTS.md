# Golden Walk Simulation Results

## Summary

**Date**: December 2024

**Critical Test**: Does the D₆ → H₃ quasicrystal support ballistic transport?

**Result**: **SUB-DIFFUSIVE** (β ≈ 0.6-0.8)

---

## Key Findings

### Transport Exponent

| Method | Graph Size | Steps | β | R² | Transport Type |
|--------|------------|-------|---|-----|----------------|
| CTQW | small (1805 vertices) | 50 | 0.04 | 0.01 | Localized |
| DTQW | small (1805 vertices) | 50 | 0.75 | 0.97 | Sub-diffusive |
| DTQW | small (1805 vertices) | 200 | 0.18 | 0.34 | Localized (finite-size) |
| DTQW | medium (5527 vertices) | 100 | **0.66** | **0.88** | **Sub-diffusive** |

### Interpretation

- **β = 2**: Ballistic (theory viable)
- **β = 1**: Diffusive
- **β < 1**: Sub-diffusive
- **β ≈ 0**: Localized

The D₆ → H₃ quasicrystal with Grover-coin DTQW shows **sub-diffusive transport** with β ≈ 0.66.

---

## Implications for the Theory

### The Bad News

The transport exponent β ≈ 0.66 is significantly below the ballistic threshold (β = 2). This suggests:

1. **Quasicrystalline structure induces anomalous transport** — similar to 1D quasiperiodic systems (Damanik et al.)
2. **Simple tight-binding / Grover-coin dynamics may not support emergent Lorentz invariance**

### The Nuanced View

However, several caveats apply:

1. **Finite-size effects**: Our largest graph (5527 vertices) may still be too small for asymptotic behavior
2. **Coin choice**: The Grover coin may not be optimal; other coins might give different β
3. **Hamiltonian tuning**: The simple H = -A tight-binding model may need modification
4. **3D vs 1D**: While 1D quasiperiodic systems show anomalous bounds, 3D might behave differently at larger scales

### What This Means for Part IV.1

The "Golden Walk" test provides **preliminary evidence against** simple ballistic transport on the H₃ quasicrystal. However:

- This doesn't definitively rule out emergent Lorentz invariance
- More sophisticated dynamics (e.g., fine-tuned coins, multi-band models) might restore ballistic behavior
- The theory should acknowledge this as an **open problem**

---

## Technical Details

### Graph Construction

- **Method**: D₆ lattice → cut-and-project with window_radius=1.0
- **Adjacency**: True D₆-root nearest neighbors (not 3D threshold)
- **Edge lengths**: 0.74 - 1.20 (golden ratio shells)
- **Max coordination**: 60 (number of D₆ roots)

### DTQW Implementation

- **Coin**: Grover diffusion operator (site-dependent, k-dimensional)
- **Shift**: Permutation via back_state array
- **Complexity**: O(dim) per step, where dim = Σ_v degree(v)

### CTQW Implementation

- **Hamiltonian**: H = -A (negative adjacency)
- **Evolution**: exp(-iHt) via scipy.linalg.expm
- **Issue**: Shows strong localization (β ≈ 0) — may be numerical artifact or genuine physics

---

## Next Steps

1. **Larger graphs**: Test with max_coord=4 or 5 (requires more memory)
2. **Alternative coins**: Try Hadamard-like or DFT coins adapted to H₃ symmetry
3. **Multi-band models**: Add internal degrees of freedom beyond the coin
4. **Theoretical analysis**: Investigate if H₃ symmetry can force isotropy despite sub-diffusive transport
5. **Literature comparison**: Compare to known results on 3D quasicrystal transport

---

## Files

- `h3_graph.py`: Graph generation with D₆-root adjacency
- `golden_walk.py`: CTQW and DTQW implementations
- `RESULTS.md`: This file

## References

- Delegation 39: D₆ Hamiltonian & Emergent Dynamics
- Part IV.1: Spacetime emergence
- Damanik et al. (2014): Anomalous Lieb-Robinson bounds in 1D quasiperiodic systems

