"""
Areal Density Calculation for D₆ → H₃ Projection

Purpose: Calculate the exact areal density of edges/vertices on a 2D slice of the D₆ quasicrystal.
This computes the coefficient ρ_2D(φ) for the holographic entropy derivation.

Mechanism:
1. Generate a large patch of the H₃ quasicrystal (D₆ projection).
2. Define a probe disk of radius R at the center.
3. Generate random planes passing through the origin.
4. Count the number of graph edges that intersect the disk.
5. Compute density ρ = N_cuts / (π R²).
6. Normalize by the average edge length squared to get the dimensionless coefficient.

Output:
- Areal density ρ (in units of 1/L²)
- Dimensionless coefficient C = ρ * a_avg²
- Comparison with simple geometric estimates
"""

import numpy as np
import sys
import os
import time

# Add current directory to path to find h3_graph
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from h3_graph import H3Graph

def compute_areal_density(max_coord=6, n_planes=1000, r_fraction=0.7):
    """
    Compute the areal density of edges cutting a plane.
    
    Args:
        max_coord: Size of lattice to generate (larger = better statistics)
        n_planes: Number of random planes to average over
        r_fraction: Fraction of the cloud radius to use for the probe disk
                    (avoids boundary effects)
    """
    print(f"Generating H3 Graph (max_coord={max_coord})...")
    t0 = time.time()
    # use_root_adjacency=True ensures we use real physical edges (D6 roots)
    graph = H3Graph(max_coord=max_coord, use_root_adjacency=True, verbose=True)
    print(f"Graph generated in {time.time()-t0:.2f}s")
    print(f"Vertices: {graph.n_vertices}")
    
    # 1. Extract Edges and Calculate Lengths
    edges = []
    edge_lengths = []
    
    # Iterate over adjacency dict to get unique edges
    for i in range(graph.n_vertices):
        u = graph.positions[i]
        for j in graph.neighbors[i]:
            if j > i: # Unique edges only
                v = graph.positions[j]
                edges.append((u, v))
                edge_lengths.append(np.linalg.norm(u - v))
    
    edges = np.array(edges) # Shape (N_edges, 2, 3)
    n_edges = len(edges)
    avg_edge_length = np.mean(edge_lengths)
    avg_edge_length_sq = np.mean(np.array(edge_lengths)**2)
    
    print(f"\nEdge Statistics:")
    print(f"  Total Edges: {n_edges}")
    print(f"  Avg Length <a>: {avg_edge_length:.6f}")
    print(f"  Avg Length² <a²>: {avg_edge_length_sq:.6f}")
    
    # 2. Define Probe Volume
    # Center is roughly origin (0,0,0) since D6 generation is symmetric
    # Calculate radius of the point cloud
    dists = np.linalg.norm(graph.positions, axis=1)
    cloud_radius = np.max(dists)
    probe_radius = cloud_radius * r_fraction
    probe_area = np.pi * probe_radius**2
    
    print(f"\nProbe Geometry:")
    print(f"  Cloud Radius: {cloud_radius:.4f}")
    print(f"  Probe Radius: {probe_radius:.4f}")
    print(f"  Probe Area:   {probe_area:.4f}")
    
    # Filter edges: roughly check if they are within range to potentially intersect
    # (Optimization: only keep edges where at least one point is within 1.2 * probe_radius)
    # Actually, let's just vectorize the intersection check.
    
    print(f"\nSampling {n_planes} random planes...")
    
    intersection_counts = []
    
    # 3. Loop over random planes
    for p in range(n_planes):
        # Random normal vector
        normal = np.random.normal(0, 1, 3)
        normal /= np.linalg.norm(normal)
        
        # Plane passing through origin: n·x = 0
        
        # Edge (u, v) intersects plane if (n·u) and (n·v) have opposite signs
        # AND the intersection point is within probe_radius
        
        u_proj = np.dot(edges[:, 0, :], normal)
        v_proj = np.dot(edges[:, 1, :], normal)
        
        # Check signs (crossing plane)
        # Use strict inequality to avoid points exactly on plane (measure zero)
        crossing_mask = (u_proj * v_proj) < 0
        
        if np.sum(crossing_mask) == 0:
            intersection_counts.append(0)
            continue
            
        # Get crossing edges
        crossing_edges = edges[crossing_mask]
        u_c = u_proj[crossing_mask]
        v_c = v_proj[crossing_mask]
        
        # Calculate intersection points
        # P = u + t(v - u)
        # n·P = 0 => n·u + t(n·v - n·u) = 0
        # t = - (n·u) / (n·v - n·u)
        
        denom = v_c - u_c
        # Avoid division by zero (shouldn't happen given crossing_mask)
        t = -u_c / denom
        
        # Vectorized intersection points
        # edges[mask] is (K, 2, 3)
        # u is (K, 3), v is (K, 3)
        u_vec = crossing_edges[:, 0, :]
        v_vec = crossing_edges[:, 1, :]
        
        # t needs to be broadcastable (K, 1)
        t_col = t[:, np.newaxis]
        
        P = u_vec + t_col * (v_vec - u_vec)
        
        # Check if P is within probe disk
        # |P| <= probe_radius
        p_dist_sq = np.sum(P**2, axis=1)
        valid_intersections = np.sum(p_dist_sq <= probe_radius**2)
        
        intersection_counts.append(valid_intersections)
    
    # 4. Results
    avg_cuts = np.mean(intersection_counts)
    std_cuts = np.std(intersection_counts)
    
    rho_2d = avg_cuts / probe_area
    
    # Dimensionless coefficient C = rho * a^2
    # We use <a^2> because the area is dimension L^2.
    C = rho_2d * avg_edge_length_sq
    
    print(f"\nResults:")
    print(f"  Avg Intersections: {avg_cuts:.2f} ± {std_cuts:.2f}")
    print(f"  Areal Density ρ:   {rho_2d:.6f} edges/unit_area")
    print(f"  Dimensionless C:   {C:.6f} (ρ * <a²>)")
    
    # Theoretical checking
    # For a simple cubic lattice with spacing a=1, length=1:
    # Isotropic flux through unit area is 3 * (projection of unit vectors)
    # 3 directions * 0.5 (average |cos theta|) * density 1?
    # The standard result for random lines of length L density n is n L / 2?
    # Let's just rely on the Monte Carlo.
    
    return {
        'rho': rho_2d,
        'C': C,
        'avg_len': avg_edge_length,
        'avg_cuts': avg_cuts
    }

if __name__ == "__main__":
    # Use max_coord=6 for good statistics (approx 5000 vertices)
    compute_areal_density(max_coord=6, n_planes=2000)

