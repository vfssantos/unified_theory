# Phason Stiffness Results

## Method

Computed phason stiffness by measuring vertex flips under phason shifts.

## Key Insight: Extensive vs Intensive

- **K_extensive** = total flips per |w|² (grows with system size)
- **k_intensive** = K/N = flips per vertex per |w|² (geometric invariant)

The intensive stiffness k is the true geometric property.

## What This Derives (Pure Geometry)

| Quantity | Value | Source |
|----------|-------|--------|
| q = 2π/φ² | 2.399963 | Golden ratio |
| K_extensive | 26357.89 | D₆ simulation |
| k_intensive = K/N | 1.206256 | Geometric invariant |
| **a/l_P = √(q/k)** | **1.4105** | Derived ratio |

## Parameters

- D₆ lattice: max_coord = 4
- Total D₆ points: 265,721
- Reference vertices: 21,851
- Reference edges: 379,440
- Monte Carlo samples: 100
- Computation time: 1.86s

## Result

The lattice spacing a is approximately **1.4 × l_Planck**.

## What This Does NOT Derive

- The absolute scale l_P ≈ 1.6×10⁻³⁵ m (requires observed ℏ, G, c)
- Planck's constant ℏ (fundamental input)

## The Honest Assessment

This calculation gives a **dimensionless ratio** a/l_P from pure geometry.
It does NOT derive the Planck scale from scratch — that would require
deriving ℏ itself from geometry, which no standard approach achieves.
