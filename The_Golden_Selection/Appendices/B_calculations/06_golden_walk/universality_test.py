"""
Universality Test: Is c = 1 for Different Excitation Types?

Purpose: Test if the speed of light c = 1 is universal across different
         quantum walk dynamics (DTQW vs CTQW).

If c is the same for both:
- The speed of light is a property of the GEOMETRY, not the dynamics
- Lorentz invariance is more robust

If c differs:
- The speed of light depends on the excitation type
- Need to understand which is the "physical" speed

Dependencies:
- numpy
- scipy
- matplotlib (optional)
"""

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply
from typing import Dict, Tuple
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from h3_graph import H3Graph
from golden_walk import DTQW


class FastCTQW:
    """
    Fast Continuous-Time Quantum Walk using sparse matrix exponential.
    
    Uses scipy.sparse.linalg.expm_multiply which is O(N) per step
    instead of O(N³) for dense expm.
    """
    
    def __init__(self, graph: H3Graph, gamma: float = 1.0):
        self.graph = graph
        self.gamma = gamma
        self.n = graph.n_vertices
        
        # Sparse Hamiltonian: H = -γA
        self.H_sparse = csr_matrix(-gamma * graph.adjacency.astype(np.float64))
    
    def evolve(self, psi0: np.ndarray, t: float) -> np.ndarray:
        """Evolve state by time t using sparse expm_multiply."""
        # exp(-iHt)|ψ⟩
        return expm_multiply(-1j * self.H_sparse * t, psi0)


def test_universality(
    max_coord: int = 2,
    n_steps: int = 100,
    verbose: bool = True
) -> Dict:
    """
    Test if the speed of light is the same for DTQW and CTQW.
    
    Args:
        max_coord: Size of D₆ lattice
        n_steps: Number of time steps
        verbose: Print progress
        
    Returns:
        Dict with results for both walk types
    """
    if verbose:
        print("=" * 60)
        print("UNIVERSALITY TEST: Is c the same for DTQW and CTQW?")
        print("=" * 60)
        print()
    
    # Generate graph
    graph = H3Graph(max_coord=max_coord, use_root_adjacency=True, verbose=verbose)
    
    # Find central vertex
    distances = np.linalg.norm(graph.positions, axis=1)
    origin_idx = np.argmin(distances)
    
    r0_phys = graph.positions[origin_idx]
    r0_d6 = graph.d6_coords[origin_idx].astype(float)
    
    if verbose:
        print(f"\nOrigin vertex: {origin_idx}")
        print(f"Testing both DTQW and CTQW...")
    
    results = {}
    
    # =========================================================================
    # Test 1: DTQW (Grover coin)
    # =========================================================================
    if verbose:
        print("\n--- DTQW (Grover coin) ---")
    
    dtqw = DTQW(graph)
    psi_dtqw = dtqw.initial_state_localized(origin_idx)
    
    msd_dtqw = np.zeros(n_steps)
    msd_d6_dtqw = np.zeros(n_steps)
    t_hyper_dtqw = np.zeros(n_steps)
    
    for i in range(n_steps):
        if i > 0:
            psi_dtqw = dtqw.step(psi_dtqw)
        
        # Compute probabilities
        probs = np.zeros(graph.n_vertices)
        np.add.at(probs, dtqw.vertex_of_state, np.abs(psi_dtqw) ** 2)
        
        # MSD in physical and D6 space
        msd_dtqw[i] = np.sum(probs * np.sum((graph.positions - r0_phys)**2, axis=1))
        d6_disp = graph.d6_coords.astype(float) - r0_d6
        msd_d6_dtqw[i] = np.sum(probs * np.sum(d6_disp**2, axis=1))
        t_hyper_dtqw[i] = np.sqrt(msd_d6_dtqw[i])
    
    # Fit for c
    rms_dtqw = np.sqrt(msd_dtqw)
    valid = (t_hyper_dtqw > 0.1) & (t_hyper_dtqw < t_hyper_dtqw.max() * 0.8)
    if np.sum(valid) > 5:
        t_v = t_hyper_dtqw[valid]
        r_v = rms_dtqw[valid]
        A = np.vstack([t_v, np.ones(len(t_v))]).T
        c_dtqw, b_dtqw = np.linalg.lstsq(A, r_v, rcond=None)[0]
        r_pred = c_dtqw * t_v + b_dtqw
        ss_res = np.sum((r_v - r_pred)**2)
        ss_tot = np.sum((r_v - np.mean(r_v))**2)
        r2_dtqw = 1 - ss_res / ss_tot
    else:
        c_dtqw = rms_dtqw[-1] / t_hyper_dtqw[-1] if t_hyper_dtqw[-1] > 0 else 0
        r2_dtqw = 0
    
    results['dtqw'] = {
        'c': c_dtqw,
        'r2': r2_dtqw,
        'msd': msd_dtqw,
        't_hyper': t_hyper_dtqw,
    }
    
    if verbose:
        print(f"  c_DTQW = {c_dtqw:.4f} (R² = {r2_dtqw:.4f})")
    
    # =========================================================================
    # Test 2: CTQW (tight-binding) - using FAST sparse implementation
    # =========================================================================
    if verbose:
        print("\n--- CTQW (tight-binding, sparse) ---")
    
    ctqw = FastCTQW(graph, gamma=1.0)
    psi_ctqw = np.zeros(graph.n_vertices, dtype=np.complex128)
    psi_ctqw[origin_idx] = 1.0
    
    msd_ctqw = np.zeros(n_steps)
    msd_d6_ctqw = np.zeros(n_steps)
    t_hyper_ctqw = np.zeros(n_steps)
    
    # Precompute displacement arrays
    phys_disp_sq = np.sum((graph.positions - r0_phys)**2, axis=1)
    d6_disp_sq = np.sum((graph.d6_coords.astype(float) - r0_d6)**2, axis=1)
    
    # Time steps for CTQW (continuous time, sample at discrete points)
    dt = 0.5  # Time step size
    
    for i in range(n_steps):
        if i > 0:
            psi_ctqw = ctqw.evolve(psi_ctqw, dt)
        
        probs = np.abs(psi_ctqw) ** 2
        
        # MSD in physical and D6 space (vectorized)
        msd_ctqw[i] = np.dot(probs, phys_disp_sq)
        msd_d6_ctqw[i] = np.dot(probs, d6_disp_sq)
        t_hyper_ctqw[i] = np.sqrt(msd_d6_ctqw[i])
        
        if verbose and i % 20 == 0:
            print(f"    Step {i}/{n_steps}")
    
    # Fit for c
    rms_ctqw = np.sqrt(msd_ctqw)
    valid = (t_hyper_ctqw > 0.1) & (t_hyper_ctqw < t_hyper_ctqw.max() * 0.8)
    if np.sum(valid) > 5:
        t_v = t_hyper_ctqw[valid]
        r_v = rms_ctqw[valid]
        A = np.vstack([t_v, np.ones(len(t_v))]).T
        c_ctqw, b_ctqw = np.linalg.lstsq(A, r_v, rcond=None)[0]
        r_pred = c_ctqw * t_v + b_ctqw
        ss_res = np.sum((r_v - r_pred)**2)
        ss_tot = np.sum((r_v - np.mean(r_v))**2)
        r2_ctqw = 1 - ss_res / ss_tot
    else:
        c_ctqw = rms_ctqw[-1] / t_hyper_ctqw[-1] if t_hyper_ctqw[-1] > 0 else 0
        r2_ctqw = 0
    
    results['ctqw'] = {
        'c': c_ctqw,
        'r2': r2_ctqw,
        'msd': msd_ctqw,
        't_hyper': t_hyper_ctqw,
    }
    
    if verbose:
        print(f"  c_CTQW = {c_ctqw:.4f} (R² = {r2_ctqw:.4f})")
    
    # =========================================================================
    # Compare
    # =========================================================================
    c_ratio = c_dtqw / c_ctqw if c_ctqw > 0 else float('inf')
    c_diff = abs(c_dtqw - c_ctqw)
    c_avg = (c_dtqw + c_ctqw) / 2
    c_variation = c_diff / c_avg if c_avg > 0 else 0
    
    results['comparison'] = {
        'c_ratio': c_ratio,
        'c_diff': c_diff,
        'c_variation': c_variation,
    }
    
    if verbose:
        print("\n" + "=" * 60)
        print("UNIVERSALITY RESULTS")
        print("=" * 60)
        print()
        print("| Walk Type | c | R² |")
        print("|-----------|---|-----|")
        print(f"| DTQW (Grover) | {c_dtqw:.4f} | {r2_dtqw:.4f} |")
        print(f"| CTQW (tight-binding) | {c_ctqw:.4f} | {r2_ctqw:.4f} |")
        print()
        print(f"Ratio: c_DTQW / c_CTQW = {c_ratio:.4f}")
        print(f"Variation: {c_variation * 100:.1f}%")
        print()
        
        if c_variation < 0.1:
            print("✓ UNIVERSALITY CONFIRMED!")
            print("  The speed of light is the same for both excitation types.")
            print("  c is a property of the GEOMETRY, not the dynamics.")
        elif c_variation < 0.3:
            print("⚠ PARTIAL UNIVERSALITY")
            print("  The speeds differ by ~{:.0f}%".format(c_variation * 100))
            print("  This may be due to finite-size effects or different regimes.")
        else:
            print("✗ UNIVERSALITY VIOLATED")
            print("  The speed of light depends on the excitation type.")
            print("  Need to identify which is the 'physical' speed.")
    
    return results


def test_dispersion_relation(
    max_coord: int = 2,
    verbose: bool = True
) -> Dict:
    """
    Test if the dispersion relation is linear: ω = c|k|
    
    For the tight-binding Hamiltonian H = -A, the eigenvalues are the
    energy spectrum. We can check if the spectrum has linear (Dirac-like)
    features.
    """
    from scipy.sparse.linalg import eigsh
    
    if verbose:
        print("\n" + "=" * 60)
        print("DISPERSION RELATION TEST")
        print("=" * 60)
        print()
    
    # Generate graph
    graph = H3Graph(max_coord=max_coord, use_root_adjacency=True, verbose=False)
    
    if verbose:
        print(f"Graph: {graph.n_vertices} vertices")
        print("Computing partial spectrum of H = -A (sparse)...")
    
    # Sparse Hamiltonian
    H_sparse = csr_matrix(-graph.adjacency.astype(np.float64))
    
    # Compute only extremal eigenvalues (much faster)
    n_eigs = min(100, graph.n_vertices - 2)
    
    # Get largest and smallest eigenvalues
    eigs_large = eigsh(H_sparse, k=n_eigs//2, which='LA', return_eigenvectors=False)
    eigs_small = eigsh(H_sparse, k=n_eigs//2, which='SA', return_eigenvectors=False)
    
    # Also get eigenvalues near zero (for Dirac point check)
    try:
        eigs_near_zero = eigsh(H_sparse, k=20, sigma=0.0, return_eigenvectors=False)
    except:
        eigs_near_zero = np.array([])
    
    eigenvalues = np.sort(np.concatenate([eigs_large, eigs_small, eigs_near_zero]))
    
    # Density of states
    n_bins = 50
    hist, bin_edges = np.histogram(eigenvalues, bins=n_bins, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # Check for linear features near E = 0 (Dirac point)
    # For Dirac fermions, DOS ~ |E| near E = 0
    near_zero = np.abs(bin_centers) < 5
    dos_near_zero = hist[near_zero]
    e_near_zero = bin_centers[near_zero]
    
    results = {
        'eigenvalues': eigenvalues,
        'dos': hist,
        'dos_energies': bin_centers,
        'e_min': eigenvalues.min(),
        'e_max': eigenvalues.max(),
        'bandwidth': eigenvalues.max() - eigenvalues.min(),
    }
    
    if verbose:
        print(f"\nSpectrum statistics:")
        print(f"  E_min = {eigenvalues.min():.3f}")
        print(f"  E_max = {eigenvalues.max():.3f}")
        print(f"  Bandwidth = {results['bandwidth']:.3f}")
        print(f"  DOS at E=0: {hist[len(hist)//2]:.4f}")
        print()
        
        # Check if DOS vanishes at E = 0 (Dirac point signature)
        dos_at_zero = hist[len(hist)//2]
        if dos_at_zero < np.mean(hist) * 0.5:
            print("✓ DOS suppressed near E = 0")
            print("  This is consistent with a Dirac-like linear dispersion!")
        else:
            print("⚠ DOS not suppressed at E = 0")
            print("  The dispersion may not be Dirac-like.")
    
    return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Universality Test')
    parser.add_argument('--size', choices=['small', 'medium'], default='small')
    parser.add_argument('--steps', type=int, default=100)
    parser.add_argument('--dispersion', action='store_true', 
                        help='Also test dispersion relation')
    
    args = parser.parse_args()
    
    size_map = {'small': 2, 'medium': 3}
    
    # Test universality
    results = test_universality(
        max_coord=size_map[args.size],
        n_steps=args.steps,
        verbose=True
    )
    
    # Test dispersion relation
    if args.dispersion:
        disp_results = test_dispersion_relation(
            max_coord=size_map[args.size],
            verbose=True
        )

