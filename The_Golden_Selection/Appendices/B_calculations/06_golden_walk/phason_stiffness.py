"""
Phason Stiffness Calculation for D₆ → H₃ Projection (OPTIMIZED)

Purpose: Compute the dimensionless phason stiffness K from D₆ geometry.

What We Derive (Pure Geometry):
- K: phason stiffness (dimensionless, from lattice structure)
- q = 2π/φ²: golden quantum angle (dimensionless)
- a/l_P = √(q/K): ratio of lattice spacing to Planck length (dimensionless)

What We Do NOT Derive:
- ℏ, G, c (these are observed constants)
- The absolute scale of l_P (this requires ℏ, G, c)

The Value:
The ratio a/l_P is a geometric prediction. If K ≈ q, then a ≈ l_P.
"""

import numpy as np
import sys
import os
import time

# Golden ratio constants
PHI = (1 + np.sqrt(5)) / 2
# Pre-compute Q for output
Q_ANGLE = 2 * np.pi / PHI**2

def get_projection_matrices():
    """Build D6 -> E_parallel and E_perp projection matrices."""
    sqrt5 = np.sqrt(5)
    
    # 6x3 matrices projecting D6 to physical and internal space
    # (Transposed for N x 6 @ 6 x 3 multiplication)
    P_par = np.array([
        [1, PHI, 0, -1, PHI, 0],
        [PHI, 0, 1, PHI, 0, -1],
        [0, 1, PHI, 0, -1, PHI]
    ]).T / sqrt5
    
    P_perp = np.array([
        [PHI, -1, 0, PHI, 1, 0],
        [-1, 0, PHI, 1, 0, PHI],
        [0, PHI, -1, 0, PHI, 1]
    ]).T / sqrt5
    
    return P_par, P_perp

def generate_d6_grid(max_coord):
    """
    Generate D6 points using optimized numpy grids.
    Uses int8 or int16 to save memory for large grids.
    """
    # Determine smallest dtype needed
    if max_coord < 127:
        dtype = np.int8
    else:
        dtype = np.int16
        
    rng = np.arange(-max_coord, max_coord + 1, dtype=dtype)
    
    # Create grid (N^6 points)
    # Using simple meshgrid approach - sufficient for N < 15
    grid = np.array(np.meshgrid(*[rng]*6)).T.reshape(-1, 6)
    
    # D6 Condition: Sum of coordinates must be even
    # np.sum over axis 1, check modulo 2
    mask = (np.sum(grid, axis=1) % 2) == 0
    return grid[mask]

def count_edges_once(d6_points, active_mask):
    """
    Count edges only for the active vertices. 
    This is slow, so we only do it ONCE for the reference state.
    """
    # Extract only the active points
    active_points = d6_points[active_mask]
    n_verts = len(active_points)
    
    if n_verts == 0:
        return 0
        
    # Create a fast lookup set using tuples (most compatible)
    pt_set = set(map(tuple, active_points))

    # Generate the 30 positive roots of D6 (i < j)
    # Roots: 1 at i, 1 at j  AND  1 at i, -1 at j
    roots = []
    dims = 6
    for i in range(dims):
        for j in range(i + 1, dims):
            # r1 = e_i + e_j
            r1 = np.zeros(dims, dtype=active_points.dtype)
            r1[i], r1[j] = 1, 1
            roots.append(r1)
            # r2 = e_i - e_j
            r2 = np.zeros(dims, dtype=active_points.dtype)
            r2[i], r2[j] = 1, -1
            roots.append(r2)
            
    roots = np.array(roots)
    
    # Count connections
    edge_count = 0
    
    # Iterate through active points and check neighbors
    for pt in active_points:
        neighbors = pt + roots
        for neighbor in neighbors:
            if tuple(neighbor) in pt_set:
                edge_count += 1
                
    return edge_count  # Counts undirected edges once (only positive roots used)

def compute_stiffness_optimized(max_coord=3, n_samples=100, max_shift=0.5):
    t0 = time.time()
    
    print("=" * 60)
    print(f"PHASON STIFFNESS CALCULATION (OPTIMIZED)")
    print(f"Lattice Size: max_coord={max_coord}")
    print("=" * 60)

    # 1. Setup Geometry
    P_par, P_perp = get_projection_matrices()
    d6_points = generate_d6_grid(max_coord)
    print(f"Total D6 candidates: {len(d6_points):,}")

    # 2. Pre-project entire lattice to Perp Space (Internal Space)
    # We only need perp space to determine if a point is in the window.
    # We do this ONCE.
    print("Projecting to perpendicular space...")
    x_perp_static = d6_points @ P_perp
    
    # 3. Define Window
    window_radius = max_coord * 0.6
    window_radius_sq = window_radius**2
    
    # 4. Build Reference State
    # Calculate norms squared
    norms_sq_ref = np.sum(x_perp_static**2, axis=1)
    mask_ref = norms_sq_ref <= window_radius_sq
    
    n_ref = np.sum(mask_ref)
    print(f"Reference Quasicrystal Vertices: {n_ref:,}")
    
    # Calculate edges only once for reporting
    print("Counting reference edges...")
    e_ref = count_edges_once(d6_points, mask_ref)
    print(f"Reference Edges: {e_ref:,}")

    if n_ref < 10:
        print("Error: Lattice too small.")
        return None

    # 5. Monte Carlo Loop (Vectorized)
    print(f"\nRunning {n_samples} phason shifts (Vectorized)...")
    
    shifts_sq = []
    vertex_losses = []
    
    # Pre-generate random shifts to allow batch processing if needed, 
    # but simple loop is fast enough now.
    directions = np.random.randn(n_samples, 3)
    directions /= np.linalg.norm(directions, axis=1)[:, np.newaxis]
    magnitudes = np.random.uniform(0.05, max_shift, n_samples)
    
    # Actual loop
    for i in range(n_samples):
        shift_vec = directions[i] * magnitudes[i]
        
        # Apply shift to static perp coordinates
        # Broadcasting: (N,3) - (3,)
        x_perp_shifted = x_perp_static - shift_vec
        
        # Check window condition (using squared distance to avoid sqrt)
        # sum(x^2) is faster than linalg.norm
        dists_sq = np.sum(x_perp_shifted**2, axis=1)
        mask_shifted = dists_sq <= window_radius_sq
        
        # LOGICAL XOR:
        # Points in Ref but not Shifted (Lost) = True ^ False = True
        # Points in Shifted but not Ref (Gained) = False ^ True = True
        # Points in both or neither = False
        # Sum of XOR gives total "flips" (Hamming distance)
        flips = np.count_nonzero(np.logical_xor(mask_ref, mask_shifted))
        
        shifts_sq.append(magnitudes[i]**2)
        vertex_losses.append(flips)

    # 6. Analysis
    shifts_sq = np.array(shifts_sq)
    vertex_losses = np.array(vertex_losses)
    
    # Linear Regression through origin: y = Kx
    # K = sum(x*y) / sum(x^2)  where y=losses, x=w^2
    # Standard formula for slope constraint to 0
    numerator = np.sum(vertex_losses * shifts_sq)
    denominator = np.sum(shifts_sq**2)
    K_extensive = numerator / denominator
    
    # CRITICAL: K_extensive is proportional to N (system size)
    # The INTENSIVE stiffness (per vertex) is the geometric invariant
    k_intensive = K_extensive / n_ref
    
    # Geometric ratio using intensive stiffness
    if k_intensive > 0:
        a_over_lP = np.sqrt(Q_ANGLE / k_intensive)
    else:
        a_over_lP = float('inf')

    t1 = time.time()
    dt = t1 - t0
    
    print("\n" + "-" * 60)
    print(f"CALCULATION COMPLETE in {dt:.4f} seconds")
    print("-" * 60)
    print(f"Golden Quantum Angle (q):     {Q_ANGLE:.4f}")
    print(f"Extensive Stiffness (K):      {K_extensive:.2f} (system-size dependent)")
    print(f"Intensive Stiffness (k=K/N):  {k_intensive:.4f} (geometric invariant)")
    print(f"Geometric Ratio (a/l_P):      {a_over_lP:.4f}")
    print("-" * 60)
    
    # Interpretation
    print(f"""
INTERPRETATION:
  K_extensive ≈ {K_extensive:.0f} = total flips per unit |w|²
  k_intensive = K/N ≈ {k_intensive:.3f} = flips per VERTEX per unit |w|²
  
  The intensive k is the geometric invariant (independent of system size).
  
  Golden quantum angle: q = 2π/φ² ≈ {Q_ANGLE:.2f}
  
  From k·a² = q·ℏ (in appropriate units):
    a/l_P = √(q/k) = √({Q_ANGLE:.2f}/{k_intensive:.3f}) ≈ {a_over_lP:.2f}
  
RESULT: The lattice spacing a ≈ {a_over_lP:.1f} × l_Planck
  
NOTE: This ratio is derived from PURE GEOMETRY.
      The absolute scale (l_P ≈ 10⁻³⁵ m) requires observed ℏ, G, c.
""")
    
    # Save results
    outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "STIFFNESS_RESULTS.md")
    with open(outfile, "w") as f:
        f.write("# Phason Stiffness Results\n\n")
        f.write("## Method\n\n")
        f.write("Computed phason stiffness by measuring vertex flips under phason shifts.\n\n")
        f.write("## Key Insight: Extensive vs Intensive\n\n")
        f.write("- **K_extensive** = total flips per |w|² (grows with system size)\n")
        f.write("- **k_intensive** = K/N = flips per vertex per |w|² (geometric invariant)\n\n")
        f.write("The intensive stiffness k is the true geometric property.\n\n")
        f.write("## What This Derives (Pure Geometry)\n\n")
        f.write(f"| Quantity | Value | Source |\n")
        f.write(f"|----------|-------|--------|\n")
        f.write(f"| q = 2π/φ² | {Q_ANGLE:.6f} | Golden ratio |\n")
        f.write(f"| K_extensive | {K_extensive:.2f} | D₆ simulation |\n")
        f.write(f"| k_intensive = K/N | {k_intensive:.6f} | Geometric invariant |\n")
        f.write(f"| **a/l_P = √(q/k)** | **{a_over_lP:.4f}** | Derived ratio |\n\n")
        f.write("## Parameters\n\n")
        f.write(f"- D₆ lattice: max_coord = {max_coord}\n")
        f.write(f"- Total D₆ points: {len(d6_points):,}\n")
        f.write(f"- Reference vertices: {n_ref:,}\n")
        f.write(f"- Reference edges: {e_ref:,}\n")
        f.write(f"- Monte Carlo samples: {n_samples}\n")
        f.write(f"- Computation time: {dt:.2f}s\n\n")
        f.write("## Result\n\n")
        f.write(f"The lattice spacing a is approximately **{a_over_lP:.1f} × l_Planck**.\n\n")
        f.write("## What This Does NOT Derive\n\n")
        f.write("- The absolute scale l_P ≈ 1.6×10⁻³⁵ m (requires observed ℏ, G, c)\n")
        f.write("- Planck's constant ℏ (fundamental input)\n\n")
        f.write("## The Honest Assessment\n\n")
        f.write("This calculation gives a **dimensionless ratio** a/l_P from pure geometry.\n")
        f.write("It does NOT derive the Planck scale from scratch — that would require\n")
        f.write("deriving ℏ itself from geometry, which no standard approach achieves.\n")
    
    print(f"Results saved to: {outfile}")
    
    return k_intensive, Q_ANGLE, a_over_lP

if __name__ == "__main__":
    # Increased parameters for better precision because the code is faster
    # max_coord=4 is significantly larger than 3 (approx 530k points vs 117k)
    compute_stiffness_optimized(max_coord=4, n_samples=100, max_shift=0.6)
