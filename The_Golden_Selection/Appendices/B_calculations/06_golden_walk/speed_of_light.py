"""
Speed of Light Derivation from Golden Walk

Purpose: Extract the emergent "speed of light" from the ballistic transport
         in hyperspace time.

The Physics:
- In hyperspace time t_hyper, transport is ballistic: ⟨x_∥²⟩ ~ t_hyper²
- This implies a maximum velocity: c = lim(t→∞) √⟨x_∥²⟩ / t_hyper
- This velocity is the "speed of light" in the emergent spacetime

Key Questions:
1. What is the numerical value of c (in lattice units)?
2. Is c isotropic (same in all directions)?
3. How does c relate to the golden ratio φ?
4. Is c universal (same for all excitations)?

Dependencies:
- numpy
- matplotlib (optional)

References:
- Delegation 40: Time Emergence Alternatives
- PHASON_TIME_RESULTS.md: Breakthrough results
"""

import numpy as np
from typing import Dict, Tuple, List
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from h3_graph import H3Graph
from golden_walk import DTQW


def compute_velocity_profile(
    max_coord: int = 2,
    n_steps: int = 100,
    n_directions: int = 12,
    verbose: bool = True
) -> Dict:
    """
    Compute the velocity in physical space as a function of hyperspace time.
    
    For ballistic transport: v = dx/dt_hyper
    The "speed of light" is the asymptotic velocity.
    
    Args:
        max_coord: Size of D₆ lattice
        n_steps: Number of DTQW steps
        n_directions: Number of directions to test for isotropy
        verbose: Print progress
        
    Returns:
        Dict with velocity data and speed of light estimate
    """
    if verbose:
        print("=" * 60)
        print("SPEED OF LIGHT DERIVATION")
        print("=" * 60)
        print()
    
    # Generate graph
    graph = H3Graph(max_coord=max_coord, use_root_adjacency=True, verbose=verbose)
    
    # Find central vertex
    distances = np.linalg.norm(graph.positions, axis=1)
    origin_idx = np.argmin(distances)
    
    if verbose:
        print(f"\nOrigin vertex: {origin_idx}")
        print(f"  Position: {graph.positions[origin_idx]}")
    
    # Initialize DTQW
    qw = DTQW(graph)
    psi = qw.initial_state_localized(origin_idx)
    
    # Track evolution
    r0_phys = graph.positions[origin_idx]
    r0_d6 = graph.d6_coords[origin_idx].astype(float)
    
    step_count = np.arange(n_steps, dtype=float)
    msd_parallel = np.zeros(n_steps)
    msd_d6 = np.zeros(n_steps)
    hyperspace_time = np.zeros(n_steps)
    
    # Also track directional velocities for isotropy test
    # Project positions onto different directions
    directions = []
    for i in range(n_directions):
        theta = 2 * np.pi * i / n_directions
        phi = np.pi / 2  # Equatorial plane
        d = np.array([
            np.sin(phi) * np.cos(theta),
            np.sin(phi) * np.sin(theta),
            np.cos(phi)
        ])
        directions.append(d)
    
    msd_directional = np.zeros((n_directions, n_steps))
    
    if verbose:
        print(f"\nRunning DTQW and tracking velocities...")
    
    for i in range(n_steps):
        if i > 0:
            psi = qw.step(psi)
        
        # Compute probability distribution
        probs = np.zeros(graph.n_vertices)
        np.add.at(probs, qw.vertex_of_state, np.abs(psi) ** 2)
        
        # MSD in physical space
        displacements = graph.positions - r0_phys
        msd_parallel[i] = np.sum(probs * np.sum(displacements**2, axis=1))
        
        # MSD in D₆ space
        d6_displacements = graph.d6_coords.astype(float) - r0_d6
        msd_d6[i] = np.sum(probs * np.sum(d6_displacements**2, axis=1))
        
        # Hyperspace time
        hyperspace_time[i] = np.sqrt(msd_d6[i])
        
        # Directional MSD for isotropy
        for j, d in enumerate(directions):
            projected_disp = np.dot(displacements, d)
            msd_directional[j, i] = np.sum(probs * projected_disp**2)
        
        if verbose and i % max(1, n_steps // 5) == 0:
            rms_phys = np.sqrt(msd_parallel[i])
            t_h = hyperspace_time[i]
            v = rms_phys / t_h if t_h > 0 else 0
            print(f"  Step {i}: √MSD_∥ = {rms_phys:.3f}, t_hyper = {t_h:.3f}, v = {v:.3f}")
    
    # Compute velocity profile: v(t) = d(√MSD) / d(t_hyper)
    rms_parallel = np.sqrt(msd_parallel)
    
    # Instantaneous velocity (finite difference)
    velocity = np.zeros(n_steps)
    for i in range(1, n_steps):
        dt = hyperspace_time[i] - hyperspace_time[i-1]
        dr = rms_parallel[i] - rms_parallel[i-1]
        if dt > 0:
            velocity[i] = dr / dt
    
    # Average velocity (cumulative)
    avg_velocity = np.zeros(n_steps)
    for i in range(1, n_steps):
        if hyperspace_time[i] > 0:
            avg_velocity[i] = rms_parallel[i] / hyperspace_time[i]
    
    # Fit for speed of light: √MSD_∥ = c * t_hyper (ballistic)
    # Use linear regression on the ballistic regime
    valid = (hyperspace_time > 0.1) & (hyperspace_time < hyperspace_time.max() * 0.8)
    if np.sum(valid) > 5:
        t_valid = hyperspace_time[valid]
        r_valid = rms_parallel[valid]
        
        # Linear fit: r = c * t + b
        A = np.vstack([t_valid, np.ones(len(t_valid))]).T
        c_fit, b_fit = np.linalg.lstsq(A, r_valid, rcond=None)[0]
        
        # R² for the fit
        r_pred = c_fit * t_valid + b_fit
        ss_res = np.sum((r_valid - r_pred)**2)
        ss_tot = np.sum((r_valid - np.mean(r_valid))**2)
        r_squared = 1 - ss_res / ss_tot
    else:
        c_fit = avg_velocity[-1]
        b_fit = 0
        r_squared = 0
    
    # Directional velocities for isotropy
    directional_c = []
    for j in range(n_directions):
        rms_dir = np.sqrt(msd_directional[j])
        if hyperspace_time[-1] > 0:
            c_dir = rms_dir[-1] / hyperspace_time[-1]
            directional_c.append(c_dir)
    
    directional_c = np.array(directional_c)
    c_mean = np.mean(directional_c)
    c_std = np.std(directional_c)
    anisotropy = c_std / c_mean if c_mean > 0 else 0
    
    results = {
        'step_count': step_count,
        'hyperspace_time': hyperspace_time,
        'rms_parallel': rms_parallel,
        'velocity': velocity,
        'avg_velocity': avg_velocity,
        'c_fit': c_fit,
        'c_intercept': b_fit,
        'c_r_squared': r_squared,
        'directional_c': directional_c,
        'c_mean': c_mean,
        'c_std': c_std,
        'anisotropy': anisotropy,
        'n_vertices': graph.n_vertices,
    }
    
    if verbose:
        print("\n" + "=" * 60)
        print("SPEED OF LIGHT RESULTS")
        print("=" * 60)
        print()
        print(f"Speed of light (linear fit): c = {c_fit:.4f} (lattice units)")
        print(f"  Fit quality: R² = {r_squared:.4f}")
        print(f"  Intercept: b = {b_fit:.4f}")
        print()
        print(f"Isotropy test ({n_directions} directions):")
        print(f"  Mean c: {c_mean:.4f}")
        print(f"  Std c: {c_std:.4f}")
        print(f"  Anisotropy: {anisotropy:.4f} ({anisotropy*100:.1f}%)")
        print()
        
        # Compare to golden ratio
        phi = (1 + np.sqrt(5)) / 2
        print("Comparison to golden ratio:")
        print(f"  c = {c_fit:.4f}")
        print(f"  φ = {phi:.4f}")
        print(f"  1/φ = {1/phi:.4f}")
        print(f"  √φ = {np.sqrt(phi):.4f}")
        print(f"  1/√φ = {1/np.sqrt(phi):.4f}")
        print(f"  φ² = {phi**2:.4f}")
        print(f"  c/φ = {c_fit/phi:.4f}")
        print(f"  c*φ = {c_fit*phi:.4f}")
        print()
        
        # Physical interpretation
        print("Physical interpretation:")
        print(f"  In hyperspace time, the walker moves at velocity c ≈ {c_fit:.3f}")
        print(f"  This is the emergent 'speed of light' in lattice units")
        print()
        
        if anisotropy < 0.1:
            print("✓ ISOTROPY CONFIRMED (< 10% variation)")
        else:
            print(f"⚠ ANISOTROPY DETECTED ({anisotropy*100:.1f}% variation)")
    
    return results


def analyze_golden_ratio_connection(c: float, verbose: bool = True) -> Dict:
    """
    Analyze how the speed of light relates to the golden ratio.
    
    The D₆ → H₃ projection is built on φ, so c might be expressible
    in terms of φ.
    """
    phi = (1 + np.sqrt(5)) / 2
    
    # Test various φ-based expressions
    candidates = {
        'φ': phi,
        '1/φ': 1/phi,
        'φ²': phi**2,
        '1/φ²': 1/phi**2,
        '√φ': np.sqrt(phi),
        '1/√φ': 1/np.sqrt(phi),
        '√(φ-1)': np.sqrt(phi - 1),
        '√(φ+1)': np.sqrt(phi + 1),
        'φ/√5': phi / np.sqrt(5),
        '2/φ²': 2/phi**2,
        '(φ+1)/φ²': (phi+1)/phi**2,
        '1/√(φ+1)': 1/np.sqrt(phi+1),
        '√(2/φ)': np.sqrt(2/phi),
        'φ^(1/3)': phi**(1/3),
        'φ^(2/3)': phi**(2/3),
    }
    
    # Find best match
    best_match = None
    best_error = float('inf')
    
    results = {}
    for name, value in candidates.items():
        error = abs(c - value) / value
        results[name] = {'value': value, 'error': error}
        if error < best_error:
            best_error = error
            best_match = name
    
    if verbose:
        print("\n" + "=" * 60)
        print("GOLDEN RATIO CONNECTION")
        print("=" * 60)
        print()
        print(f"Measured c = {c:.6f}")
        print()
        print("Comparison to φ-based expressions:")
        print()
        print("| Expression | Value | Error |")
        print("|------------|-------|-------|")
        for name, data in sorted(results.items(), key=lambda x: x[1]['error']):
            print(f"| {name:12s} | {data['value']:.6f} | {data['error']*100:.2f}% |")
        print()
        print(f"Best match: c ≈ {best_match} (error: {best_error*100:.2f}%)")
    
    return {
        'c': c,
        'candidates': results,
        'best_match': best_match,
        'best_error': best_error,
    }


def plot_velocity_profile(results: Dict, save_path: str = None):
    """Plot the velocity profile and speed of light fit."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available")
        return
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    t = results['hyperspace_time']
    r = results['rms_parallel']
    v = results['avg_velocity']
    c = results['c_fit']
    
    # 1. RMS displacement vs hyperspace time
    ax = axes[0, 0]
    valid = t > 0
    ax.plot(t[valid], r[valid], 'b.', markersize=3, label='Data')
    t_fit = np.linspace(0, t.max(), 100)
    ax.plot(t_fit, c * t_fit + results['c_intercept'], 'r-', 
            label=f'Fit: c = {c:.3f}')
    ax.set_xlabel('Hyperspace time $t_{hyper}$')
    ax.set_ylabel('RMS displacement $\\sqrt{\\langle x_\\parallel^2 \\rangle}$')
    ax.set_title(f'Ballistic Transport (R² = {results["c_r_squared"]:.3f})')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 2. Average velocity vs hyperspace time
    ax = axes[0, 1]
    ax.plot(t[valid], v[valid], 'g-', linewidth=1)
    ax.axhline(y=c, color='r', linestyle='--', label=f'c = {c:.3f}')
    ax.set_xlabel('Hyperspace time $t_{hyper}$')
    ax.set_ylabel('Average velocity $v = r/t$')
    ax.set_title('Velocity Profile')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 3. Directional velocities (isotropy)
    ax = axes[1, 0]
    n_dir = len(results['directional_c'])
    angles = np.linspace(0, 360, n_dir, endpoint=False)
    ax.bar(angles, results['directional_c'], width=360/n_dir * 0.8, alpha=0.7)
    ax.axhline(y=results['c_mean'], color='r', linestyle='--', 
               label=f'Mean = {results["c_mean"]:.3f}')
    ax.set_xlabel('Direction (degrees)')
    ax.set_ylabel('Directional velocity')
    ax.set_title(f'Isotropy Test (anisotropy = {results["anisotropy"]*100:.1f}%)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 4. Step count vs hyperspace time
    ax = axes[1, 1]
    N = results['step_count']
    valid = (t > 0) & (N > 0)
    ax.loglog(N[valid], t[valid], 'b.', markersize=3)
    ax.set_xlabel('Step count N')
    ax.set_ylabel('Hyperspace time $t_{hyper}$')
    ax.set_title('Time Dilation: $t_{hyper}$ vs N')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Speed of Light Derivation')
    parser.add_argument('--size', choices=['small', 'medium', 'large'], default='small')
    parser.add_argument('--steps', type=int, default=100)
    parser.add_argument('--directions', type=int, default=12)
    parser.add_argument('--plot', action='store_true')
    parser.add_argument('--save', type=str, default=None)
    
    args = parser.parse_args()
    
    size_map = {'small': 2, 'medium': 3, 'large': 4}
    
    results = compute_velocity_profile(
        max_coord=size_map[args.size],
        n_steps=args.steps,
        n_directions=args.directions,
        verbose=True
    )
    
    # Analyze golden ratio connection
    analyze_golden_ratio_connection(results['c_fit'], verbose=True)
    
    if args.plot or args.save:
        plot_velocity_profile(results, args.save)

