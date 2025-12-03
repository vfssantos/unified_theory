"""
H₃ Quasicrystal Graph Generation

Purpose: Generate the 3D icosahedral quasicrystal graph from D₆ → H₃ projection
         for use in quantum walk simulations.

Method: Cut-and-project from D₆ lattice with golden-ratio acceptance window.
        Adjacency built from TRUE D₆ nearest neighbors (root vectors).

Dependencies:
- numpy
- scipy (for spatial algorithms)

References:
- Al-Siyabi, Koca, Koca (2020). "Icosahedral Polyhedra from D₆ Lattice"
- Delegation 39: D₆ Hamiltonian & Emergent Dynamics
"""

import numpy as np
from scipy.spatial import KDTree
from typing import Tuple, Dict, List
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '02_projections'))
from d6_to_h3_projection import (
    get_projection_matrix, 
    get_internal_projection_matrix,
    generate_d6_roots,
    PHI, PHI_INV
)

# =============================================================================
# CONSTANTS
# =============================================================================

# Acceptance window radius in E_perp (controls density)
DEFAULT_WINDOW_RADIUS = 1.0

# Neighbor distance threshold (fallback for 3D-based adjacency)
DEFAULT_NEIGHBOR_THRESHOLD = 0.8


# =============================================================================
# D₆ LATTICE POINT GENERATION
# =============================================================================

def generate_d6_points_efficient(max_coord: int = 5) -> np.ndarray:
    """
    Efficiently generate D₆ lattice points using numpy broadcasting.
    
    D₆ = {(x₁,...,x₆) ∈ ℤ⁶ : Σxᵢ is even}
    
    Args:
        max_coord: Maximum absolute value for each coordinate
        
    Returns:
        Array of D₆ lattice points (N × 6)
    """
    coords = np.arange(-max_coord, max_coord + 1)
    grids = np.meshgrid(coords, coords, coords, coords, coords, coords, indexing='ij')
    all_points = np.stack([g.ravel() for g in grids], axis=1)
    
    # Filter for D₆ condition (sum is even)
    sums = all_points.sum(axis=1)
    d6_mask = (sums % 2 == 0)
    
    return all_points[d6_mask]


# =============================================================================
# CUT-AND-PROJECT METHOD
# =============================================================================

def cut_and_project(
    d6_points: np.ndarray,
    window_radius: float = DEFAULT_WINDOW_RADIUS
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Apply cut-and-project method to D₆ points.
    
    Projects points to E_∥ (physical) and E_⊥ (internal) spaces.
    Keeps only points whose E_⊥ projection falls within acceptance window.
    
    Args:
        d6_points: Array of D₆ lattice points (N × 6)
        window_radius: Radius of acceptance window in E_⊥
        
    Returns:
        Tuple of:
        - physical_coords: Accepted points in E_∥ (M × 3)
        - internal_coords: Corresponding E_⊥ coordinates (M × 3)
        - d6_indices: Indices of accepted points in original array
    """
    P_phys = get_projection_matrix()
    P_int = get_internal_projection_matrix()
    
    phys_coords = d6_points @ P_phys.T
    int_coords = d6_points @ P_int.T
    
    int_distances = np.linalg.norm(int_coords, axis=1)
    accepted_mask = int_distances <= window_radius
    
    return (
        phys_coords[accepted_mask],
        int_coords[accepted_mask],
        np.where(accepted_mask)[0]
    )


# =============================================================================
# GRAPH CONSTRUCTION
# =============================================================================

def build_adjacency_graph_from_d6_roots(
    d6_coords: np.ndarray
) -> Tuple[np.ndarray, Dict[int, List[int]]]:
    """
    Build adjacency using exact D₆ nearest neighbors.
    
    Two vertices are connected if their 6D coordinates differ
    by a D₆ root vector ±eᵢ ± eⱼ.
    
    This is the CORRECT way to build the tight-binding graph.
    
    Args:
        d6_coords: 6D integer coordinates of accepted vertices (N × 6)
        
    Returns:
        adjacency_matrix: (N × N) dense int8 adjacency matrix
        neighbor_lists: dict i -> list of neighbor indices
    """
    n_vertices = len(d6_coords)
    
    # Map 6D integer coordinates -> vertex index
    coord_to_index: Dict[Tuple[int, ...], int] = {}
    for idx, v in enumerate(d6_coords):
        coord_to_index[tuple(int(x) for x in v)] = idx
    
    # All 60 D₆ roots
    roots = generate_d6_roots().astype(int)
    
    adjacency = np.zeros((n_vertices, n_vertices), dtype=np.int8)
    neighbor_lists: Dict[int, List[int]] = {i: [] for i in range(n_vertices)}
    
    for i, base in enumerate(d6_coords):
        base_tuple = tuple(int(x) for x in base)
        
        for r in roots:
            neighbor_coord = tuple(base_tuple[j] + int(r[j]) for j in range(6))
            j = coord_to_index.get(neighbor_coord)
            if j is not None and j != i:
                # Undirected edge i–j (avoid duplicates)
                if adjacency[i, j] == 0:
                    adjacency[i, j] = 1
                    adjacency[j, i] = 1
                    neighbor_lists[i].append(j)
                    neighbor_lists[j].append(i)
    
    return adjacency, neighbor_lists


def build_adjacency_graph_3d_threshold(
    physical_coords: np.ndarray,
    neighbor_threshold: float = DEFAULT_NEIGHBOR_THRESHOLD
) -> Tuple[np.ndarray, Dict[int, List[int]]]:
    """
    Build adjacency graph from 3D physical coordinates using distance threshold.
    
    This is a FALLBACK method — prefer build_adjacency_graph_from_d6_roots.
    
    Args:
        physical_coords: Vertex positions in 3D (N × 3)
        neighbor_threshold: Maximum distance for edge connection
        
    Returns:
        adjacency_matrix, neighbor_lists
    """
    n_vertices = len(physical_coords)
    tree = KDTree(physical_coords)
    pairs = tree.query_pairs(r=neighbor_threshold)
    
    adjacency = np.zeros((n_vertices, n_vertices), dtype=np.int8)
    neighbor_lists = {i: [] for i in range(n_vertices)}
    
    for i, j in pairs:
        adjacency[i, j] = 1
        adjacency[j, i] = 1
        neighbor_lists[i].append(j)
        neighbor_lists[j].append(i)
    
    return adjacency, neighbor_lists


def compute_coordination_numbers(neighbor_lists: Dict[int, List[int]]) -> np.ndarray:
    """Compute coordination number (degree) for each vertex."""
    n_vertices = len(neighbor_lists)
    return np.array([len(neighbor_lists[i]) for i in range(n_vertices)])


# =============================================================================
# H₃ GRAPH CLASS
# =============================================================================

class H3Graph:
    """
    Represents the H₃ icosahedral quasicrystal graph.
    
    Attributes:
        n_vertices: Number of vertices
        positions: 3D coordinates of vertices (N × 3)
        internal_coords: Internal space coordinates (N × 3)
        d6_coords: Original 6D D₆ coordinates (N × 6)
        adjacency: Adjacency matrix
        neighbors: Dict of neighbor lists
        coordination: Coordination numbers
    """
    
    def __init__(
        self,
        max_coord: int = 3,
        window_radius: float = DEFAULT_WINDOW_RADIUS,
        use_root_adjacency: bool = True,
        neighbor_threshold: float = DEFAULT_NEIGHBOR_THRESHOLD,
        verbose: bool = True
    ):
        """
        Generate H₃ graph from D₆ lattice.
        
        Args:
            max_coord: Size of D₆ coordinate box
            window_radius: Acceptance window radius
            use_root_adjacency: If True, use D₆ root vectors for neighbors (RECOMMENDED)
                               If False, use 3D distance threshold
            neighbor_threshold: Edge connection threshold (only if use_root_adjacency=False)
            verbose: Print progress information
        """
        if verbose:
            print(f"Generating D₆ lattice (max_coord={max_coord})...")
        
        d6_points = generate_d6_points_efficient(max_coord)
        if verbose:
            print(f"  Generated {len(d6_points)} D₆ points")
        
        if verbose:
            print(f"Applying cut-and-project (window_radius={window_radius})...")
        
        self.positions, self.internal_coords, self._d6_indices = cut_and_project(
            d6_points, window_radius
        )
        self.n_vertices = len(self.positions)
        
        # Keep the accepted D₆ coordinates (6D integer vectors)
        self.d6_coords = d6_points[self._d6_indices]
        
        if verbose:
            print(f"  Accepted {self.n_vertices} vertices")
        
        # Build graph
        if verbose:
            if use_root_adjacency:
                print("Building adjacency graph from D₆ roots (true nearest neighbors)...")
            else:
                print(f"Building adjacency graph (3D threshold={neighbor_threshold})...")
        
        if use_root_adjacency:
            self.adjacency, self.neighbors = build_adjacency_graph_from_d6_roots(
                self.d6_coords
            )
        else:
            self.adjacency, self.neighbors = build_adjacency_graph_3d_threshold(
                self.positions, neighbor_threshold
            )
        
        self.coordination = compute_coordination_numbers(self.neighbors)
        
        if verbose:
            self._print_stats()
    
    def _print_stats(self):
        """Print graph statistics."""
        n_edges = np.sum(self.adjacency) // 2
        coord_unique, coord_counts = np.unique(self.coordination, return_counts=True)
        
        print(f"\n=== H₃ Graph Statistics ===")
        print(f"Vertices: {self.n_vertices}")
        print(f"Edges: {n_edges}")
        print(f"Average coordination: {np.mean(self.coordination):.2f}")
        print(f"Max coordination: {np.max(self.coordination)}")
        print(f"Min coordination: {np.min(self.coordination)}")
        print(f"Coordination distribution:")
        for c, n in zip(coord_unique, coord_counts):
            if n > 0:
                print(f"  k={c}: {n} vertices ({100*n/self.n_vertices:.1f}%)")
        
        # Edge length statistics
        edge_lengths = []
        for i in range(self.n_vertices):
            for j in self.neighbors[i]:
                if j > i:  # avoid double counting
                    d = np.linalg.norm(self.positions[i] - self.positions[j])
                    edge_lengths.append(d)
        
        if edge_lengths:
            edge_lengths = np.array(edge_lengths)
            print(f"\nEdge length statistics:")
            print(f"  Min: {np.min(edge_lengths):.4f}")
            print(f"  Max: {np.max(edge_lengths):.4f}")
            print(f"  Mean: {np.mean(edge_lengths):.4f}")
            print(f"  Std: {np.std(edge_lengths):.4f}")
    
    def get_laplacian(self) -> np.ndarray:
        """Compute the graph Laplacian L = D - A."""
        D = np.diag(self.coordination)
        return D - self.adjacency
    
    def get_normalized_laplacian(self) -> np.ndarray:
        """Compute the normalized graph Laplacian."""
        D_inv_sqrt = np.diag(1.0 / np.sqrt(self.coordination + 1e-10))
        return np.eye(self.n_vertices) - D_inv_sqrt @ self.adjacency @ D_inv_sqrt


# =============================================================================
# TESTING
# =============================================================================

def test_h3_graph():
    """Test H₃ graph generation with D₆-root adjacency."""
    print("=" * 60)
    print("H₃ QUASICRYSTAL GRAPH TEST (D₆-ROOT ADJACENCY)")
    print("=" * 60)
    print()
    
    # Test with D₆-root adjacency (correct method)
    print("--- D₆-Root Adjacency (max_coord=2) ---")
    g_root = H3Graph(max_coord=2, use_root_adjacency=True, verbose=True)
    
    print()
    
    # Compare with 3D threshold (for reference)
    print("--- 3D Threshold Adjacency (max_coord=2, threshold=0.8) ---")
    g_3d = H3Graph(max_coord=2, use_root_adjacency=False, neighbor_threshold=0.8, verbose=True)
    
    print()
    print("=" * 60)
    print("COMPARISON")
    print("=" * 60)
    print(f"D₆-root method: {np.sum(g_root.adjacency)//2} edges, avg coord = {np.mean(g_root.coordination):.2f}")
    print(f"3D threshold:   {np.sum(g_3d.adjacency)//2} edges, avg coord = {np.mean(g_3d.coordination):.2f}")
    
    return g_root


if __name__ == "__main__":
    test_h3_graph()
