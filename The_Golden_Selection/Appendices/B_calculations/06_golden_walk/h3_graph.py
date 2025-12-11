"""
H₃ Quasicrystal Graph Generation

Purpose: Generate the 3D icosahedral quasicrystal graph from D₆ → H₃ projection
         for use in quantum walk simulations and gauge theory.

Method: Cut-and-project from D₆ lattice with golden-ratio acceptance window.
        Adjacency built from TRUE D₆ nearest neighbors (root vectors).
        **NEW**: Face/plaquette computation for Wilson action and DEC.

Dependencies:
- numpy
- scipy (for spatial algorithms)

References:
- Al-Siyabi, Koca, Koca (2020). "Icosahedral Polyhedra from D₆ Lattice"
- Delegation 39: D₆ Hamiltonian & Emergent Dynamics
- Delegation 52: Kinetic Gap — Faces needed for Wilson action & simplicial complex
- Christ, Friedberg, Lee (1982): "Random Lattice Gauge Theory"
- Frettlöh: "Icosahedral tilings in R³: The ABCK tilings"
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
# FACE / PLAQUETTE COMPUTATION
# =============================================================================

def find_triangular_faces(
    neighbor_lists: Dict[int, List[int]]
) -> List[Tuple[int, int, int]]:
    """
    Find all triangular faces (3-cycles) in the graph.
    
    A triangle is three vertices (i, j, k) where each pair is connected.
    
    Returns:
        List of (i, j, k) tuples with i < j < k (canonical ordering)
    """
    triangles = set()
    n_vertices = len(neighbor_lists)
    
    for i in range(n_vertices):
        neighbors_i = set(neighbor_lists[i])
        for j in neighbor_lists[i]:
            if j > i:
                neighbors_j = set(neighbor_lists[j])
                # Find common neighbors
                common = neighbors_i & neighbors_j
                for k in common:
                    if k > j:
                        triangles.add((i, j, k))
    
    return list(triangles)


def find_rhombic_faces(
    positions: np.ndarray,
    neighbor_lists: Dict[int, List[int]],
    planarity_tol: float = 0.1,
    parallelogram_tol: float = 0.1
) -> Tuple[List[Tuple[int, int, int, int]], np.ndarray, np.ndarray]:
    """
    Find all rhombic (4-cycle parallelogram) faces in the graph.
    
    A rhombic face is a 4-cycle (i, j, k, l) that forms a planar parallelogram.
    In icosahedral quasicrystals, these are the faces of thick/thin rhombohedra.
    
    Args:
        positions: 3D vertex coordinates (N × 3)
        neighbor_lists: Adjacency lists
        planarity_tol: Maximum deviation from planarity (normalized)
        parallelogram_tol: Maximum deviation from parallelogram condition
        
    Returns:
        faces: List of (i, j, k, l) vertex index tuples (ordered around face)
        areas: Area of each face
        face_types: 'thick' or 'thin' classification based on acute angle
    """
    n_vertices = len(neighbor_lists)
    found_faces = set()
    face_list = []
    areas = []
    types = []
    
    # Golden angle thresholds for classification
    # Thin rhombus: acute angle ≈ 36° (π/5)
    # Thick rhombus: acute angle ≈ 72° (2π/5)
    THIN_ANGLE = np.pi / 5  # 36°
    THICK_ANGLE = 2 * np.pi / 5  # 72°
    ANGLE_BOUNDARY = (THIN_ANGLE + THICK_ANGLE) / 2  # ~54°
    
    # For each edge (i, j), look for 4-cycles
    for i in range(n_vertices):
        neighbors_i = set(neighbor_lists[i])
        
        for j in neighbor_lists[i]:
            if j <= i:
                continue
            
            neighbors_j = set(neighbor_lists[j])
            
            # For each pair of different vertices (k, l) where:
            # k is neighbor of i but not j
            # l is neighbor of j but not i
            # k and l are neighbors of each other
            
            k_candidates = neighbors_i - neighbors_j - {j}
            l_candidates = neighbors_j - neighbors_i - {i}
            
            for k in k_candidates:
                neighbors_k = set(neighbor_lists[k])
                for l in l_candidates:
                    if l in neighbors_k:
                        # Found 4-cycle: i - j - l - k - i
                        # Order canonically: smallest index first, then traverse
                        face_indices = [i, j, l, k]
                        # Create canonical representation
                        min_idx = np.argmin(face_indices)
                        canonical = tuple(face_indices[min_idx:] + face_indices[:min_idx])
                        # Also check reverse direction
                        reversed_indices = [i, k, l, j]
                        min_idx_r = np.argmin(reversed_indices)
                        canonical_r = tuple(reversed_indices[min_idx_r:] + reversed_indices[:min_idx_r])
                        
                        # Use lexicographically smaller canonical form
                        canonical = min(canonical, canonical_r)
                        
                        if canonical in found_faces:
                            continue
                        
                        # Check planarity
                        p0, p1, p2, p3 = [positions[idx] for idx in canonical]
                        
                        # Compute normal via cross product of diagonals
                        d1 = p2 - p0
                        d2 = p3 - p1
                        normal = np.cross(d1, d2)
                        normal_len = np.linalg.norm(normal)
                        
                        if normal_len < 1e-10:
                            continue  # Degenerate
                        
                        normal = normal / normal_len
                        
                        # Check planarity: all points should be in the plane
                        center = (p0 + p1 + p2 + p3) / 4
                        deviations = [abs(np.dot(positions[idx] - center, normal)) 
                                     for idx in canonical]
                        max_deviation = max(deviations)
                        avg_edge = (np.linalg.norm(p1 - p0) + np.linalg.norm(p2 - p1) +
                                   np.linalg.norm(p3 - p2) + np.linalg.norm(p0 - p3)) / 4
                        
                        if max_deviation / avg_edge > planarity_tol:
                            continue  # Not planar enough
                        
                        # Check parallelogram condition: opposite sides should be parallel
                        e01 = p1 - p0
                        e12 = p2 - p1
                        e23 = p3 - p2
                        e30 = p0 - p3
                        
                        # For parallelogram: e01 ≈ -e23 and e12 ≈ -e30
                        parallel_error1 = np.linalg.norm(e01 + e23) / (np.linalg.norm(e01) + 1e-10)
                        parallel_error2 = np.linalg.norm(e12 + e30) / (np.linalg.norm(e12) + 1e-10)
                        
                        if max(parallel_error1, parallel_error2) > parallelogram_tol:
                            continue  # Not a parallelogram
                        
                        # Accept this face
                        found_faces.add(canonical)
                        face_list.append(canonical)
                        
                        # Compute area (parallelogram area = |d1 × d2| / 2)
                        # But for rhombus, use side1 × side2
                        area = np.linalg.norm(np.cross(e01, e12))
                        areas.append(area)
                        
                        # Classify by acute angle
                        # Acute angle is between adjacent edges
                        side1 = np.linalg.norm(e01)
                        side2 = np.linalg.norm(e12)
                        cos_angle = np.dot(e01, e12) / (side1 * side2 + 1e-10)
                        angle = np.arccos(np.clip(cos_angle, -1, 1))
                        acute_angle = min(angle, np.pi - angle)
                        
                        if acute_angle < ANGLE_BOUNDARY:
                            types.append('thin')
                        else:
                            types.append('thick')
    
    return face_list, np.array(areas), np.array(types)


def compute_face_statistics(
    faces: List[Tuple],
    areas: np.ndarray,
    types: np.ndarray,
    verbose: bool = True
) -> Dict:
    """
    Compute statistics about the faces for verification.
    
    Expected for H₃ quasicrystal:
    - Two types of rhombic faces (thick and thin)
    - Area ratio should be φ (golden ratio)
    
    Returns:
        Dict with statistics
    """
    stats = {}
    
    if len(faces) == 0:
        if verbose:
            print("No faces found!")
        return stats
    
    # Count by type
    n_thick = np.sum(types == 'thick')
    n_thin = np.sum(types == 'thin')
    
    thick_areas = areas[types == 'thick']
    thin_areas = areas[types == 'thin']
    
    stats['n_faces'] = len(faces)
    stats['n_thick'] = n_thick
    stats['n_thin'] = n_thin
    stats['thick_ratio'] = n_thick / len(faces) if len(faces) > 0 else 0
    
    if len(thick_areas) > 0 and len(thin_areas) > 0:
        avg_thick = np.mean(thick_areas)
        avg_thin = np.mean(thin_areas)
        area_ratio = avg_thick / avg_thin if avg_thin > 0 else float('inf')
        stats['avg_thick_area'] = avg_thick
        stats['avg_thin_area'] = avg_thin
        stats['area_ratio'] = area_ratio
        stats['area_ratio_vs_phi'] = area_ratio / PHI
    
    if verbose:
        print(f"\n=== Face Statistics ===")
        print(f"Total faces: {len(faces)}")
        print(f"  Thick (prolate): {n_thick} ({100*n_thick/len(faces):.1f}%)")
        print(f"  Thin (oblate): {n_thin} ({100*n_thin/len(faces):.1f}%)")
        
        if len(thick_areas) > 0 and len(thin_areas) > 0:
            print(f"\nArea statistics:")
            print(f"  Avg thick area: {stats['avg_thick_area']:.6f}")
            print(f"  Avg thin area: {stats['avg_thin_area']:.6f}")
            print(f"  Ratio (thick/thin): {stats['area_ratio']:.6f}")
            print(f"  Expected φ = {PHI:.6f}")
            print(f"  Ratio / φ = {stats['area_ratio_vs_phi']:.6f} (should be ~1)")
    
    return stats


# =============================================================================
# VORONOI WEIGHTS FOR CHRIST-FRIEDBERG-LEE ACTION
# =============================================================================

def compute_edge_voronoi_weights(
    positions: np.ndarray,
    neighbor_lists: Dict[int, List[int]],
    faces: List[Tuple]
) -> Dict[Tuple[int, int], float]:
    """
    Compute Voronoi dual cell volumes for each edge.
    
    For the Christ-Friedberg-Lee Wilson action:
    S = Σ_l (V_l / l²) Tr(1 - U_plaquette)
    
    The weight V_l is the "dual volume" associated with edge l.
    For 3D, this is approximately the area of dual faces meeting at the edge.
    
    Args:
        positions: Vertex positions
        neighbor_lists: Adjacency lists  
        faces: List of face vertex tuples
        
    Returns:
        Dict mapping edge (i, j) with i < j to weight V_l
    """
    # Build edge -> faces mapping
    edge_faces: Dict[Tuple[int, int], List[int]] = {}
    
    for face_idx, face in enumerate(faces):
        n = len(face)
        for k in range(n):
            i, j = face[k], face[(k + 1) % n]
            edge = (min(i, j), max(i, j))
            if edge not in edge_faces:
                edge_faces[edge] = []
            edge_faces[edge].append(face_idx)
    
    # Compute weights
    weights = {}
    
    for i in range(len(neighbor_lists)):
        for j in neighbor_lists[i]:
            if j > i:
                edge = (i, j)
                edge_length = np.linalg.norm(positions[j] - positions[i])
                
                # Simple weight: sum of incident face areas / edge_length
                # This is a first-order approximation to the Voronoi dual volume
                incident_faces = edge_faces.get(edge, [])
                
                if len(incident_faces) == 0:
                    # Boundary edge - use edge length as weight
                    weights[edge] = edge_length
                else:
                    # For interior edges, weight by incident face geometry
                    # More sophisticated: use circumradii or Voronoi cell volumes
                    weights[edge] = edge_length * len(incident_faces) / 2
    
    return weights


# =============================================================================
# H₃ GRAPH CLASS
# =============================================================================

class H3Graph:
    """
    Represents the H₃ icosahedral quasicrystal graph with full cell complex structure.
    
    Attributes:
        n_vertices: Number of vertices (0-cells)
        positions: 3D coordinates of vertices (N × 3)
        internal_coords: Internal space coordinates (N × 3)
        d6_coords: Original 6D D₆ coordinates (N × 6)
        adjacency: Adjacency matrix
        neighbors: Dict of neighbor lists (1-cells via adjacency)
        coordination: Coordination numbers
        
        # NEW: Cell complex structure for DEC / Wilson action
        triangles: List of triangular faces (3-cycles)
        faces: List of rhombic faces (4-cycles) — the main plaquettes
        face_areas: Area of each face
        face_types: 'thick' or 'thin' classification
        face_stats: Statistics about face distribution
        edge_weights: Voronoi weights for Christ-Friedberg-Lee action
    """
    
    def __init__(
        self,
        max_coord: int = 3,
        window_radius: float = DEFAULT_WINDOW_RADIUS,
        use_root_adjacency: bool = True,
        neighbor_threshold: float = DEFAULT_NEIGHBOR_THRESHOLD,
        compute_faces: bool = True,
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
            compute_faces: If True, compute faces/plaquettes (2-cells)
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
        
        # Build graph (1-cells: edges)
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
        
        # Initialize face attributes
        self.triangles = []
        self.faces = []
        self.face_areas = np.array([])
        self.face_types = np.array([])
        self.face_stats = {}
        self.edge_weights = {}
        
        # Build 2-cells (faces/plaquettes)
        if compute_faces and self.n_vertices > 0:
            if verbose:
                print("Computing faces/plaquettes (2-cells)...")
            
            # Find triangular faces
            self.triangles = find_triangular_faces(self.neighbors)
            if verbose:
                print(f"  Found {len(self.triangles)} triangular faces (3-cycles)")
            
            # Find rhombic faces (main plaquettes for Wilson action)
            self.faces, self.face_areas, self.face_types = find_rhombic_faces(
                self.positions, self.neighbors
            )
            if verbose:
                print(f"  Found {len(self.faces)} rhombic faces (4-cycles)")
            
            # Compute statistics
            self.face_stats = compute_face_statistics(
                self.faces, self.face_areas, self.face_types, verbose=verbose
            )
            
            # Compute Voronoi weights for gauge theory
            if verbose:
                print("Computing edge Voronoi weights...")
            self.edge_weights = compute_edge_voronoi_weights(
                self.positions, self.neighbors, self.faces
            )
        
        if verbose:
            self._print_stats()
    
    def _print_stats(self):
        """Print graph statistics."""
        n_edges = np.sum(self.adjacency) // 2
        coord_unique, coord_counts = np.unique(self.coordination, return_counts=True)
        
        print(f"\n=== H₃ Graph Statistics ===")
        print(f"Vertices (0-cells): {self.n_vertices}")
        print(f"Edges (1-cells): {n_edges}")
        print(f"Triangles (3-cycles): {len(self.triangles)}")
        print(f"Rhombic faces (4-cycles): {len(self.faces)}")
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
        
        # Euler characteristic check
        if len(self.faces) > 0:
            # χ = V - E + F (for closed surface, χ = 2)
            # For graph embedded in 3D, this is just informative
            chi = self.n_vertices - n_edges + len(self.faces) + len(self.triangles)
            print(f"\nCell complex:")
            print(f"  V - E + F = {self.n_vertices} - {n_edges} + {len(self.faces) + len(self.triangles)} = {chi}")
    
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
    g_root = H3Graph(max_coord=2, use_root_adjacency=True, compute_faces=True, verbose=True)
    
    print()
    
    # Compare with 3D threshold (for reference)
    print("--- 3D Threshold Adjacency (max_coord=2, threshold=0.8) ---")
    g_3d = H3Graph(max_coord=2, use_root_adjacency=False, neighbor_threshold=0.8, 
                   compute_faces=True, verbose=True)
    
    print()
    print("=" * 60)
    print("COMPARISON")
    print("=" * 60)
    print(f"D₆-root method: {np.sum(g_root.adjacency)//2} edges, avg coord = {np.mean(g_root.coordination):.2f}")
    print(f"3D threshold:   {np.sum(g_3d.adjacency)//2} edges, avg coord = {np.mean(g_3d.coordination):.2f}")
    
    return g_root


def test_face_computation():
    """
    Test face computation and verify golden ratio in area ratios.
    
    Expected results for H₃ quasicrystal:
    - Faces should be rhombic (4-cycles forming parallelograms)
    - Two types: thick (prolate) and thin (oblate)
    - Area ratio thick/thin should equal φ (golden ratio)
    """
    print("=" * 70)
    print("H₃ FACE/PLAQUETTE COMPUTATION TEST")
    print("=" * 70)
    print()
    print("Expected: Two types of rhombic faces with area ratio = φ ≈ 1.618")
    print()
    
    # Generate graph with face computation
    print("--- Generating H₃ graph (max_coord=3) ---")
    g = H3Graph(max_coord=3, use_root_adjacency=True, compute_faces=True, verbose=True)
    
    print()
    print("=" * 70)
    print("VERIFICATION: Golden Ratio in Face Areas")
    print("=" * 70)
    
    if 'area_ratio' in g.face_stats:
        ratio = g.face_stats['area_ratio']
        phi_error = abs(ratio - PHI) / PHI * 100
        
        print(f"Measured area ratio (thick/thin): {ratio:.6f}")
        print(f"Expected φ = {PHI:.6f}")
        print(f"Error: {phi_error:.2f}%")
        
        if phi_error < 10:
            print("\n✅ GOLDEN RATIO VERIFIED in face areas!")
        else:
            print(f"\n⚠️ Ratio differs from φ by {phi_error:.1f}%")
            print("   This may be due to boundary effects or face classification thresholds.")
    else:
        print("Could not compute area ratio (insufficient faces of each type)")
    
    print()
    print("=" * 70)
    print("IMPLICATIONS FOR GAUGE THEORY")
    print("=" * 70)
    print(f"""
The {len(g.faces)} rhombic faces are the PLAQUETTES for:
1. Wilson action: S = Σ_plaquettes (V/a²) Tr(1 - U_□)
2. DEC curvature: F = dA lives on 2-cells (faces)
3. Simplicial complex: H₃ graph + faces forms a 2-complex

Thick/thin ratio should affect:
- Gauge coupling renormalization
- Topological properties (winding numbers)
- Holonomy statistics
""")
    
    return g


def test_wilson_action_structure():
    """
    Demonstrate the Wilson action structure on the H₃ quasicrystal.
    
    The Christ-Friedberg-Lee action for irregular lattices:
    S = Σ_l (V_l / l²) Tr(1 - U_plaquette)
    
    where V_l is the Voronoi dual volume for edge l.
    """
    print("=" * 70)
    print("WILSON ACTION STRUCTURE TEST")
    print("=" * 70)
    print()
    
    g = H3Graph(max_coord=2, use_root_adjacency=True, compute_faces=True, verbose=False)
    
    print(f"Graph: {g.n_vertices} vertices, {np.sum(g.adjacency)//2} edges, {len(g.faces)} faces")
    print()
    
    # Show edge weight statistics
    if g.edge_weights:
        weights = np.array(list(g.edge_weights.values()))
        print(f"Edge Voronoi weights:")
        print(f"  Min: {np.min(weights):.4f}")
        print(f"  Max: {np.max(weights):.4f}")
        print(f"  Mean: {np.mean(weights):.4f}")
        print(f"  Std: {np.std(weights):.4f}")
        
        # Coefficient of variation (should be small for isotropic gauge theory)
        cv = np.std(weights) / np.mean(weights)
        print(f"  Coefficient of variation: {cv:.2f}")
        
        if cv < 0.3:
            print("\n✅ Weights are relatively uniform — isotropic gauge action expected")
        else:
            print(f"\n⚠️ Weights vary significantly — may need anisotropy corrections")
    
    return g


if __name__ == "__main__":
    print("\n" + "="*70)
    print("RUNNING ALL TESTS")
    print("="*70 + "\n")
    
    # Basic graph test
    g1 = test_h3_graph()
    
    print("\n" + "-"*70 + "\n")
    
    # Face computation test
    g2 = test_face_computation()
    
    print("\n" + "-"*70 + "\n")
    
    # Wilson action test
    g3 = test_wilson_action_structure()
