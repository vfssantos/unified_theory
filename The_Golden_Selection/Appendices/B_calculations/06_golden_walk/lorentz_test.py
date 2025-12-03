"""
Lorentz Transformation Test

Purpose: Test if the D₆ → H₃ geometry supports Lorentz-like transformations.

Key Questions:
1. Does the hyperspace metric have Lorentzian signature (-,+,+,+)?
2. Can we identify boost generators in the D₆ algebra?
3. Is the "light cone" preserved under D₆ symmetry operations?

Approach:
- The metric in hyperspace time is ds² = -dt² + dx²
- We have t = |X_D6| (D₆ geodesic distance)
- We have x = |x_∥| (physical space distance)
- Check if the interval s² = -t² + x² is invariant

Dependencies:
- numpy
"""

import numpy as np
from typing import Dict, Tuple
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from h3_graph import H3Graph
from golden_walk import DTQW


def compute_spacetime_interval(
    max_coord: int = 2,
    n_steps: int = 50,
    verbose: bool = True
) -> Dict:
    """
    Compute the spacetime interval s² = x² - t² for the quantum walk.
    
    In Minkowski space, the interval is invariant under Lorentz transformations.
    For a particle moving at speed v < c:
        s² = x² - c²t² = -c²τ² (timelike, negative)
    For light (v = c):
        s² = 0 (lightlike, null)
    
    With c = 1, we expect s² = x² - t² to be approximately constant
    along the walker's trajectory.
    """
    if verbose:
        print("=" * 60)
        print("LORENTZ INVARIANCE TEST")
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
    
    # Initialize DTQW
    qw = DTQW(graph)
    psi = qw.initial_state_localized(origin_idx)
    
    # Track evolution
    x_rms = np.zeros(n_steps)  # Physical space RMS displacement
    t_hyper = np.zeros(n_steps)  # Hyperspace time
    interval_sq = np.zeros(n_steps)  # s² = x² - t²
    
    # Precompute
    phys_disp_sq = np.sum((graph.positions - r0_phys)**2, axis=1)
    d6_disp_sq = np.sum((graph.d6_coords.astype(float) - r0_d6)**2, axis=1)
    
    if verbose:
        print(f"\nComputing spacetime intervals...")
    
    for i in range(n_steps):
        if i > 0:
            psi = qw.step(psi)
        
        # Compute probabilities
        probs = np.zeros(graph.n_vertices)
        np.add.at(probs, qw.vertex_of_state, np.abs(psi) ** 2)
        
        # RMS displacements
        msd_phys = np.dot(probs, phys_disp_sq)
        msd_d6 = np.dot(probs, d6_disp_sq)
        
        x_rms[i] = np.sqrt(msd_phys)
        t_hyper[i] = np.sqrt(msd_d6)
        
        # Spacetime interval: s² = x² - t² (with c = 1)
        interval_sq[i] = msd_phys - msd_d6
    
    # The interval should be approximately constant (or slowly varying)
    # for a particle with definite rest mass
    
    # Compute "proper time" τ² = t² - x² (for timelike intervals)
    proper_time_sq = -interval_sq  # τ² = -s²
    proper_time = np.sqrt(np.maximum(proper_time_sq, 0))
    
    # Compute effective velocity v = x/t
    velocity = np.zeros(n_steps)
    for i in range(1, n_steps):
        if t_hyper[i] > 0:
            velocity[i] = x_rms[i] / t_hyper[i]
    
    # Compute Lorentz factor γ = t/τ = 1/√(1-v²)
    gamma = np.zeros(n_steps)
    for i in range(1, n_steps):
        if proper_time[i] > 0:
            gamma[i] = t_hyper[i] / proper_time[i]
    
    results = {
        'x_rms': x_rms,
        't_hyper': t_hyper,
        'interval_sq': interval_sq,
        'proper_time': proper_time,
        'velocity': velocity,
        'gamma': gamma,
    }
    
    if verbose:
        print("\n" + "=" * 60)
        print("RESULTS")
        print("=" * 60)
        print()
        print("| Step | x (phys) | t (hyper) | s² = x²-t² | τ = √(-s²) | v = x/t | γ = t/τ |")
        print("|------|----------|-----------|------------|------------|---------|---------|")
        
        for i in [0, 10, 20, 30, 40, min(49, n_steps-1)]:
            if i < n_steps:
                print(f"| {i:4d} | {x_rms[i]:8.3f} | {t_hyper[i]:9.3f} | {interval_sq[i]:10.3f} | "
                      f"{proper_time[i]:10.3f} | {velocity[i]:7.3f} | {gamma[i]:7.3f} |")
        
        print()
        
        # Check if interval is timelike (s² < 0)
        avg_interval = np.mean(interval_sq[10:])
        if avg_interval < 0:
            print("✓ INTERVAL IS TIMELIKE (s² < 0)")
            print(f"  Average s² = {avg_interval:.3f}")
            print("  This is consistent with a massive particle (v < c)")
        elif abs(avg_interval) < 0.1:
            print("✓ INTERVAL IS LIGHTLIKE (s² ≈ 0)")
            print(f"  Average s² = {avg_interval:.3f}")
            print("  This is consistent with a massless particle (v = c)")
        else:
            print("⚠ INTERVAL IS SPACELIKE (s² > 0)")
            print(f"  Average s² = {avg_interval:.3f}")
            print("  This would violate causality!")
        
        print()
        
        # Check Lorentz factor
        avg_gamma = np.mean(gamma[10:])
        avg_v = np.mean(velocity[10:])
        expected_gamma = 1 / np.sqrt(1 - avg_v**2) if avg_v < 1 else float('inf')
        
        print(f"Average velocity: v = {avg_v:.4f}")
        print(f"Average Lorentz factor: γ = {avg_gamma:.4f}")
        print(f"Expected γ = 1/√(1-v²) = {expected_gamma:.4f}")
        
        if abs(avg_gamma - expected_gamma) / expected_gamma < 0.1:
            print("\n✓ LORENTZ FACTOR MATCHES EXPECTATION!")
            print("  The relationship γ = 1/√(1-v²) holds.")
        else:
            print(f"\n⚠ Lorentz factor deviates by {abs(avg_gamma - expected_gamma)/expected_gamma*100:.1f}%")
    
    return results


def test_light_cone_structure(
    max_coord: int = 2,
    verbose: bool = True
) -> Dict:
    """
    Test if the light cone structure is preserved.
    
    In Minkowski space, the light cone separates:
    - Future timelike (reachable at v < c)
    - Future lightlike (reachable at v = c)
    - Spacelike (unreachable)
    
    We check if the quantum walk respects this structure.
    """
    if verbose:
        print("\n" + "=" * 60)
        print("LIGHT CONE STRUCTURE TEST")
        print("=" * 60)
        print()
    
    # Generate graph
    graph = H3Graph(max_coord=max_coord, use_root_adjacency=True, verbose=False)
    
    # Find central vertex
    distances = np.linalg.norm(graph.positions, axis=1)
    origin_idx = np.argmin(distances)
    
    r0_phys = graph.positions[origin_idx]
    r0_d6 = graph.d6_coords[origin_idx].astype(float)
    
    # For each vertex, compute:
    # - Physical distance x from origin
    # - D6 distance t from origin
    # - Light cone region: timelike (x < t), lightlike (x = t), spacelike (x > t)
    
    x_all = np.linalg.norm(graph.positions - r0_phys, axis=1)
    t_all = np.linalg.norm(graph.d6_coords.astype(float) - r0_d6, axis=1)
    
    # Classify vertices
    timelike = x_all < t_all  # Inside light cone
    lightlike = np.abs(x_all - t_all) < 0.1  # On light cone
    spacelike = x_all > t_all  # Outside light cone
    
    n_timelike = np.sum(timelike)
    n_lightlike = np.sum(lightlike)
    n_spacelike = np.sum(spacelike)
    
    results = {
        'x_all': x_all,
        't_all': t_all,
        'n_timelike': n_timelike,
        'n_lightlike': n_lightlike,
        'n_spacelike': n_spacelike,
    }
    
    if verbose:
        print(f"Total vertices: {graph.n_vertices}")
        print(f"  Timelike (x < t): {n_timelike} ({n_timelike/graph.n_vertices*100:.1f}%)")
        print(f"  Lightlike (x ≈ t): {n_lightlike} ({n_lightlike/graph.n_vertices*100:.1f}%)")
        print(f"  Spacelike (x > t): {n_spacelike} ({n_spacelike/graph.n_vertices*100:.1f}%)")
        print()
        
        # The ratio x/t should cluster around the speed of light
        ratio = x_all / np.maximum(t_all, 1e-10)
        ratio_valid = ratio[t_all > 0.1]
        
        print(f"Ratio x/t statistics (for t > 0.1):")
        print(f"  Mean: {np.mean(ratio_valid):.4f}")
        print(f"  Std: {np.std(ratio_valid):.4f}")
        print(f"  Min: {np.min(ratio_valid):.4f}")
        print(f"  Max: {np.max(ratio_valid):.4f}")
        
        if np.mean(ratio_valid) < 1.2:
            print("\n✓ LIGHT CONE STRUCTURE PRESERVED")
            print("  Most vertices are inside or on the light cone (x ≤ t)")
        else:
            print("\n⚠ LIGHT CONE STRUCTURE VIOLATED")
            print("  Many vertices are outside the light cone (x > t)")
    
    return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Lorentz Transformation Test')
    parser.add_argument('--size', choices=['small', 'medium'], default='small')
    parser.add_argument('--steps', type=int, default=50)
    
    args = parser.parse_args()
    
    size_map = {'small': 2, 'medium': 3}
    
    # Test spacetime interval
    results = compute_spacetime_interval(
        max_coord=size_map[args.size],
        n_steps=args.steps,
        verbose=True
    )
    
    # Test light cone structure
    cone_results = test_light_cone_structure(
        max_coord=size_map[args.size],
        verbose=True
    )

