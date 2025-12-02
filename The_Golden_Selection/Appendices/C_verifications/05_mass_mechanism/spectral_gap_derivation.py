#!/usr/bin/env python3
"""
Spectral Gap Derivation Verification
====================================

Verifies the derivation of the Mass Scale M₀ from the Spectral Gap Ratio:
M₀ = m_nucleon / (λ(D₆) / λ(A₂))

Using the PRODUCT WEIGHTED Laplacian L⊥:
w_ij = |π_⊥(r_i)|² |π_⊥(r_j)|²

Prerequisites:
- D₆ → H₃ projection matrix (from d6_to_h3_projection.py)
"""

import numpy as np
import sys
import os

# Add path to B_calculations to import projection matrix
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../B_calculations/02_projections')))
from d6_to_h3_projection import get_internal_projection_matrix

# ============================================================
# Constants
# ============================================================

M_NUCLEON = 939.565  # MeV
M0_KOIDE_FIT = 313.86 # MeV

# ============================================================
# Lattice Construction
# ============================================================

def get_d6_roots():
    """Generate the 60 roots of D₆."""
    roots = []
    dims = 6
    for i in range(dims):
        for j in range(i + 1, dims):
            for s1 in [1, -1]:
                for s2 in [1, -1]:
                    r = np.zeros(dims)
                    r[i] = s1
                    r[j] = s2
                    roots.append(r)
    return np.array(roots)

def get_a2_roots_embedded():
    """
    Generate the 6 roots of A₂ embedded in D₆.
    Standard embedding in first 3 coords: ±(e1-e2), ±(e2-e3), ±(e1-e3)
    """
    roots = []
    # e1-e2
    r = np.zeros(6); r[0]=1; r[1]=-1; roots.append(r)
    roots.append(-r)
    # e2-e3
    r = np.zeros(6); r[1]=1; r[2]=-1; roots.append(r)
    roots.append(-r)
    # e1-e3
    r = np.zeros(6); r[0]=1; r[2]=-1; roots.append(r)
    roots.append(-r)
    
    return np.array(roots)

# ============================================================
# Weighted Laplacian
# ============================================================

def build_weighted_laplacian(roots, P_perp):
    """
    Construct the Weighted Laplacian L⊥.
    Weights: w_ij = |π_⊥(r_i)|² |π_⊥(r_j)|²
    Edges: Nearest neighbors (<r_i, r_j> = 1)
    """
    n = len(roots)
    adj = np.zeros((n, n))
    
    # Pre-compute perp norms squared
    perp_norms_sq = []
    for r in roots:
        proj = P_perp @ r
        perp_norms_sq.append(np.dot(proj, proj))
    perp_norms_sq = np.array(perp_norms_sq)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Check adjacency (inner product = 1)
            dot = np.dot(roots[i], roots[j])
            
            if np.isclose(dot, 1.0):
                # Product weighting
                w = perp_norms_sq[i] * perp_norms_sq[j]
                adj[i, j] = w
                adj[j, i] = w
                
    # Laplacian L = D - A
    degrees = np.sum(adj, axis=1)
    D = np.diag(degrees)
    L = D - adj
    return L

def compute_spectral_gap(L):
    """Compute smallest non-zero eigenvalue."""
    eigvals = np.linalg.eigvalsh(L)
    eigvals = sorted(eigvals)
    for val in eigvals:
        if val > 1e-6: # Tolerance
            return val
    return 0.0

# ============================================================
# Verification
# ============================================================

def verify():
    print("=" * 60)
    print("SPECTRAL GAP DERIVATION (WEIGHTED LAPLACIAN)")
    print("=" * 60)
    
    # Get projection matrix
    P_perp = get_internal_projection_matrix()
    
    # 1. D₆
    d6_roots = get_d6_roots()
    L_d6 = build_weighted_laplacian(d6_roots, P_perp)
    gap_d6 = compute_spectral_gap(L_d6)
    
    # 2. A₂
    a2_roots = get_a2_roots_embedded()
    L_a2 = build_weighted_laplacian(a2_roots, P_perp)
    gap_a2 = compute_spectral_gap(L_a2)
    
    # 3. Ratio
    ratio = gap_d6 / gap_a2
    m0_derived = M_NUCLEON / ratio
    
    print(f"\nResults:")
    print(f"  λ(D₆) = {gap_d6:.4f}")
    print(f"  λ(A₂) = {gap_a2:.4f}")
    print(f"  Ratio = {ratio:.4f}")
    print(f"  Derived M₀ = {m0_derived:.2f} MeV")
    print(f"  Observed M₀ = {M0_KOIDE_FIT:.2f} MeV")
    print(f"  Error = {abs(m0_derived - M0_KOIDE_FIT)/M0_KOIDE_FIT*100:.2f}%")

if __name__ == "__main__":
    verify()
