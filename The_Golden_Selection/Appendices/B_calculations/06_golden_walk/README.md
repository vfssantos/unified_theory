# Golden Walk Simulation

## Purpose

This module implements the **critical test** for emergent spacetime in the Golden Selection framework.

The test: Does a quantum walk on the D₆ → H₃ quasicrystal exhibit **ballistic transport** ($\langle r^2 \rangle \propto t^2$) or **anomalous diffusion** ($\langle r^2 \rangle \propto t^\beta$, $\beta < 2$)?

- If **ballistic**: The framework can support emergent Lorentz-invariant spacetime
- If **localized**: The theory fails ("the universe freezes")

## Background

From [Delegation 39], four independent research agents agreed:

1. **Lieb-Robinson bounds apply** — a finite speed limit exists
2. **H₃ symmetry constrains isotropy** — rank-2 tensors forced toward isotropy
3. **1D quasiperiodic systems show anomalous bounds** (Damanik et al. 2014)
4. **3D likely ballistic** but unproven for quasicrystals

This simulation provides the definitive test.

## Files

- `golden_walk.py` — Main simulation code
- `h3_graph.py` — H₃ quasicrystal graph generation
- `results/` — Output data and plots

## Usage

```bash
# Generate H₃ graph and run quantum walk
python golden_walk.py

# Quick test (small graph)
python golden_walk.py --size small --steps 100

# Full simulation (large graph)
python golden_walk.py --size large --steps 1000
```

## Expected Results

| Outcome | β value | Implication |
|---------|---------|-------------|
| Ballistic | β = 2 | Theory viable |
| Diffusive | β = 1 | Marginal |
| Sub-diffusive | β < 1 | Theory fails |

## References

- [Delegation 39]: D₆ Hamiltonian & Emergent Dynamics
- [Part IV.1]: Spacetime emergence from D₆
- Damanik et al. (2014): Anomalous Lieb-Robinson bounds in 1D

