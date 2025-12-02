# Mass Mechanism Verifications

This directory contains verification materials for the dual mass mechanism (L⊥ + Koide geometry) presented in **IV.5**.

## Contents

| File | Claim Verified | Status |
|------|----------------|--------|
| `q_two_thirds.md` | Q = 2/3 from A₂ cone condition | ✅ PROVEN |
| `theta_derivation.md` | θ₀ = Q/3 = 2/9 identity | ✅ DERIVED |
| `koide_masses.py` | Numerical verification of mass ratios | ✅ VERIFIED |
| `L_perp_weighting.md` | Why product weighting is selected | ✅ DERIVED |

## Quick Verification

Run the numerical verification:

```bash
python3 koide_masses.py
```

Expected output:
- μ/e ratio: 206.7703 (obs: 206.7683, error: 0.001%)
- τ/e ratio: 3477.4728 (obs: 3477.2283, error: 0.007%)

## Key Results

### Q = 2/3 (A₂ Cone)
The Koide parameter Q equals 2/3 because the mass vector lies on a 45° cone:
$$Q = \frac{1}{3\cos^2(45°)} = \frac{1}{3 \times \frac{1}{2}} = \frac{2}{3}$$

### θ₀ = 2/9 (Phase)
The Koide phase is determined by Q through the identity:
$$\theta_0 = \frac{Q}{3} = \frac{2/3}{3} = \frac{2}{9} \text{ rad}$$

### Singularity Proximity
The electron phase (132.7°) sits only 2.3° from the zero-mass singularity at 135°. This geometric accident creates the 3477× hierarchy naturally.

