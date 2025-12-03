"""
Phason Proper Time Test

Purpose: Test if transport becomes "normal" when measured in phason proper time
         rather than step count.

The Hypothesis (from Delegation 40):
- Time = accumulated motion in internal space (E_⊥)
- τ(N) = Σ|Δx_⊥(k)| (phason proper time)
- If ⟨x_∥²⟩ ~ τ^γ with γ ≈ 1 or 2, then TIME IS HIDING IN PHASON COORDINATE

This would explain why β ≈ 0.66 in step count: the walker is "burning time"
in internal rearrangements, not just moving in physical space.

Dependencies:
- numpy
- matplotlib (optional)

References:
- Delegation 40: Time Emergence Alternatives
- All 4 agents agreed: phason proper time is the strongest candidate
"""

import numpy as np
from typing import Dict, Tuple
import sys
import os

# Add parent directory
sys.path.insert(0, os.path.dirname(__file__))
from h3_graph import H3Graph
from golden_walk import DTQW, analyze_transport


def run_phason_time_test(
    max_coord: int = 2,
    n_steps: int = 100,
    verbose: bool = True
) -> Dict:
    """
    Run the phason proper time test.
    
    Tracks both physical (x_∥) and internal (x_⊥) coordinates,
    then compares transport exponents in different time variables.
    
    Args:
        max_coord: Size of D₆ lattice
        n_steps: Number of DTQW steps
        verbose: Print progress
        
    Returns:
        Dict with results for different time definitions
    """
    if verbose:
        print("=" * 60)
        print("PHASON PROPER TIME TEST")
        print("=" * 60)
        print()
    
    # Generate graph
    graph = H3Graph(max_coord=max_coord, use_root_adjacency=True, verbose=verbose)
    
    # Find central vertex
    distances = np.linalg.norm(graph.positions, axis=1)
    origin_idx = np.argmin(distances)
    
    if verbose:
        print(f"\nOrigin vertex: {origin_idx}")
        print(f"  Physical position: {graph.positions[origin_idx]}")
        print(f"  Internal position: {graph.internal_coords[origin_idx]}")
    
    # Initialize DTQW
    qw = DTQW(graph)
    psi = qw.initial_state_localized(origin_idx)
    
    # Track multiple time variables
    step_count = np.arange(n_steps, dtype=float)
    phason_time = np.zeros(n_steps)      # τ = √⟨x_⊥²⟩ (RMS internal displacement)
    hyperspace_time = np.zeros(n_steps)  # t_flow = √⟨|X_D6|²⟩
    msd_parallel = np.zeros(n_steps)     # ⟨x_∥²⟩
    msd_internal = np.zeros(n_steps)     # ⟨x_⊥²⟩
    
    # Origin coordinates
    r0_phys = graph.positions[origin_idx]
    r0_int = graph.internal_coords[origin_idx]
    r0_d6 = graph.d6_coords[origin_idx].astype(float)
    
    if verbose:
        print(f"\nRunning DTQW with phason tracking...")
        print(f"  State space dimension: {qw.dim}")
    
    for i in range(n_steps):
        if i > 0:
            psi = qw.step(psi)
        
        # Compute probability distribution over vertices
        probs = np.zeros(graph.n_vertices)
        np.add.at(probs, qw.vertex_of_state, np.abs(psi) ** 2)
        
        # MSD from origin in different spaces
        msd_parallel[i] = np.sum(probs * np.sum((graph.positions - r0_phys)**2, axis=1))
        msd_internal[i] = np.sum(probs * np.sum((graph.internal_coords - r0_int)**2, axis=1))
        
        # D6 distance from origin
        d6_displacements = graph.d6_coords.astype(float) - r0_d6
        msd_d6 = np.sum(probs * np.sum(d6_displacements**2, axis=1))
        
        # Phason time = sqrt of internal MSD (RMS displacement in E_⊥)
        # This measures "how far the walker has explored in internal space"
        phason_time[i] = np.sqrt(msd_internal[i])
        
        # Hyperspace time = sqrt of D6 MSD
        hyperspace_time[i] = np.sqrt(msd_d6)
        
        if verbose and i % max(1, n_steps // 10) == 0:
            print(f"  Step {i}: MSD_∥={msd_parallel[i]:.3f}, MSD_⊥={msd_internal[i]:.3f}, τ={phason_time[i]:.3f}")
    
    # Analyze transport in different time variables
    if verbose:
        print("\nAnalyzing transport in different time variables...")
    
    results = {
        'step_count': step_count,
        'phason_time': phason_time,
        'hyperspace_time': hyperspace_time,
        'msd_parallel': msd_parallel,
        'msd_internal': msd_internal,
    }
    
    # Fit MSD vs different time variables
    # 1. Step count (original)
    analysis_step = analyze_transport(msd_parallel, step_count)
    results['beta_step'] = analysis_step['beta']
    results['r2_step'] = analysis_step['r_squared']
    
    # 2. Phason proper time
    analysis_phason = analyze_transport(msd_parallel, phason_time)
    results['gamma_phason'] = analysis_phason['beta']
    results['r2_phason'] = analysis_phason['r_squared']
    
    # 3. Hyperspace geodesic time
    analysis_hyper = analyze_transport(msd_parallel, hyperspace_time)
    results['gamma_hyper'] = analysis_hyper['beta']
    results['r2_hyper'] = analysis_hyper['r_squared']
    
    # 4. Spectral time (reparametrized step count)
    beta = analysis_step['beta']
    spectral_time = step_count ** beta if beta > 0 else step_count
    analysis_spectral = analyze_transport(msd_parallel, spectral_time)
    results['gamma_spectral'] = analysis_spectral['beta']
    results['r2_spectral'] = analysis_spectral['r_squared']
    
    # Print results
    if verbose:
        print("\n" + "=" * 60)
        print("RESULTS: TRANSPORT EXPONENTS IN DIFFERENT TIME VARIABLES")
        print("=" * 60)
        print()
        print("| Time Variable | Symbol | Exponent | R² | Interpretation |")
        print("|---------------|--------|----------|-----|----------------|")
        print(f"| Step count | N | β = {results['beta_step']:.3f} | {results['r2_step']:.3f} | Original (sub-diffusive) |")
        print(f"| Phason time | τ | γ = {results['gamma_phason']:.3f} | {results['r2_phason']:.3f} | Internal clock |")
        print(f"| Hyperspace | t_flow | γ = {results['gamma_hyper']:.3f} | {results['r2_hyper']:.3f} | D₆ geodesic |")
        print(f"| Spectral | N^β | γ = {results['gamma_spectral']:.3f} | {results['r2_spectral']:.3f} | Reparametrized |")
        print()
        
        # Interpret results
        if results['gamma_phason'] > results['beta_step'] + 0.2:
            print("✓ PHASON TIME SHOWS IMPROVED TRANSPORT!")
            print(f"  Exponent increased from {results['beta_step']:.3f} to {results['gamma_phason']:.3f}")
            if results['gamma_phason'] > 1.5:
                print("  → Transport is BALLISTIC in phason time!")
                print("  → TIME IS HIDING IN THE INTERNAL COORDINATE")
            elif results['gamma_phason'] > 0.9:
                print("  → Transport is DIFFUSIVE in phason time")
                print("  → Phason clock partially explains sub-diffusion")
        else:
            print("✗ Phason time does not significantly improve transport")
            print("  The sub-diffusive behavior may be intrinsic")
    
    return results


def plot_phason_test(results: Dict, save_path: str = None):
    """Plot comparison of transport in different time variables."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available")
        return
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    msd = results['msd_parallel']
    
    # 1. Step count
    ax = axes[0, 0]
    t = results['step_count']
    valid = (t > 0) & (msd > 0)
    ax.loglog(t[valid], msd[valid], 'b.', markersize=3)
    ax.set_xlabel('Step count N')
    ax.set_ylabel('MSD ⟨x²⟩')
    ax.set_title(f'Step Count: β = {results["beta_step"]:.3f}')
    ax.grid(True, alpha=0.3)
    
    # 2. Phason time
    ax = axes[0, 1]
    t = results['phason_time']
    valid = (t > 0) & (msd > 0)
    ax.loglog(t[valid], msd[valid], 'r.', markersize=3)
    ax.set_xlabel('Phason time τ')
    ax.set_ylabel('MSD ⟨x²⟩')
    ax.set_title(f'Phason Time: γ = {results["gamma_phason"]:.3f}')
    ax.grid(True, alpha=0.3)
    
    # 3. Hyperspace time
    ax = axes[1, 0]
    t = results['hyperspace_time']
    valid = (t > 0) & (msd > 0)
    ax.loglog(t[valid], msd[valid], 'g.', markersize=3)
    ax.set_xlabel('Hyperspace time t_flow')
    ax.set_ylabel('MSD ⟨x²⟩')
    ax.set_title(f'Hyperspace Time: γ = {results["gamma_hyper"]:.3f}')
    ax.grid(True, alpha=0.3)
    
    # 4. Comparison
    ax = axes[1, 1]
    labels = ['Step (β)', 'Phason (γ)', 'Hyper (γ)', 'Spectral (γ)']
    values = [results['beta_step'], results['gamma_phason'], 
              results['gamma_hyper'], results['gamma_spectral']]
    colors = ['blue', 'red', 'green', 'purple']
    bars = ax.bar(labels, values, color=colors, alpha=0.7)
    ax.axhline(y=1.0, color='gray', linestyle='--', label='Diffusive')
    ax.axhline(y=2.0, color='black', linestyle='--', label='Ballistic')
    ax.set_ylabel('Transport Exponent')
    ax.set_title('Comparison of Time Variables')
    ax.legend()
    ax.set_ylim(0, 2.5)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Phason Proper Time Test')
    parser.add_argument('--size', choices=['small', 'medium'], default='small')
    parser.add_argument('--steps', type=int, default=100)
    parser.add_argument('--plot', action='store_true')
    parser.add_argument('--save', type=str, default=None)
    
    args = parser.parse_args()
    
    size_map = {'small': 2, 'medium': 3}
    
    results = run_phason_time_test(
        max_coord=size_map[args.size],
        n_steps=args.steps,
        verbose=True
    )
    
    if args.plot or args.save:
        plot_phason_test(results, args.save)

