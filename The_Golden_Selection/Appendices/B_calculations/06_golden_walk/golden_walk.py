"""
Golden Walk: Quantum Walk on H₃ Quasicrystal

Purpose: Test whether transport on the D₆ → H₃ quasicrystal is BALLISTIC or LOCALIZED.

The Critical Test:
- Measure mean squared displacement ⟨r²⟩ as function of time steps t
- Fit to ⟨r²⟩ ∝ t^β
- If β = 2: BALLISTIC → Theory viable (emergent Lorentz invariance possible)
- If β < 2: SUB-BALLISTIC → Theory fails (universe "freezes")

Methods implemented:
1. Continuous-Time Quantum Walk (CTQW): H = -A (adjacency matrix)
2. Discrete-Time Quantum Walk (DTQW): U = S·C with Grover coin (LOCAL implementation)

Dependencies:
- numpy
- scipy
- matplotlib (optional, for plotting)

References:
- Delegation 39: D₆ Hamiltonian & Emergent Dynamics
- Part IV.1: Spacetime emergence
- Damanik et al. (2014): Anomalous Lieb-Robinson bounds
"""

import numpy as np
from scipy.linalg import expm
from typing import Tuple, Optional, Dict
import argparse
import time

from h3_graph import H3Graph


# =============================================================================
# CONTINUOUS-TIME QUANTUM WALK (CTQW)
# =============================================================================

class CTQW:
    """
    Continuous-Time Quantum Walk on a graph.
    
    Hamiltonian: H = -γ·A (negative adjacency matrix)
    Evolution: |ψ(t)⟩ = exp(-iHt)|ψ(0)⟩
    """
    
    def __init__(self, graph: H3Graph, gamma: float = 1.0):
        """
        Initialize CTQW.
        
        Args:
            graph: H₃ quasicrystal graph
            gamma: Hopping amplitude
        """
        self.graph = graph
        self.gamma = gamma
        self.n = graph.n_vertices
        
        # Hamiltonian: H = -γA
        self.H = -gamma * graph.adjacency.astype(np.float64)
    
    def evolve(self, psi0: np.ndarray, t: float) -> np.ndarray:
        """
        Evolve state by time t.
        
        Args:
            psi0: Initial state (N,) complex array
            t: Time to evolve
            
        Returns:
            Final state |ψ(t)⟩
        """
        U = expm(-1j * self.H * t)
        return U @ psi0
    
    def compute_msd(self, psi: np.ndarray, origin_idx: int) -> float:
        """
        Compute mean squared displacement from origin.
        
        MSD = ⟨ψ|r²|ψ⟩ = Σᵢ |ψᵢ|² |rᵢ - r₀|²
        """
        probs = np.abs(psi) ** 2
        r0 = self.graph.positions[origin_idx]
        displacements_sq = np.sum((self.graph.positions - r0) ** 2, axis=1)
        return np.sum(probs * displacements_sq)


# =============================================================================
# DISCRETE-TIME QUANTUM WALK (DTQW) WITH LOCAL GROVER COIN
# =============================================================================

class DTQW:
    """
    Discrete-Time Quantum Walk with site-dependent Grover coin,
    implemented LOCALLY (no dim×dim dense matrices).
    
    State index s corresponds to an oriented edge |v, a⟩:
      - v = vertex index
      - a = local direction index at v (which neighbor)
    
    Data structures:
      - state_to_vd[s]     = (v, d, neighbor)
      - vertex_states[v]   = list of state indices at vertex v
      - back_state[s]      = state index of the oriented edge that points back
      - vertex_of_state[s] = v (for fast MSD computation)
    """
    
    def __init__(self, graph: H3Graph):
        """
        Initialize DTQW.
        
        Args:
            graph: H₃ quasicrystal graph
        """
        self.graph = graph
        self.n = graph.n_vertices
        
        # Build oriented-edge state space
        self._build_state_space()
    
    def _build_state_space(self):
        """Build mapping between state indices and (vertex, direction) pairs."""
        self.state_to_vd = []                 # s -> (v, d, neighbor)
        self.vertex_states = [[] for _ in range(self.n)]
        self.vd_to_state = {}                 # (v, d) -> s
        
        state_idx = 0
        for v in range(self.n):
            neighs = self.graph.neighbors[v]
            for d, neighbor in enumerate(neighs):
                self.state_to_vd.append((v, d, neighbor))
                self.vd_to_state[(v, d)] = state_idx
                self.vertex_states[v].append(state_idx)
                state_idx += 1
        
        self.dim = state_idx
        
        # Precompute back_state: where does |v,d⟩ go under the shift S?
        self.back_state = np.empty(self.dim, dtype=int)
        
        for s, (v, d, neighbor) in enumerate(self.state_to_vd):
            neighbor_list = self.graph.neighbors[neighbor]
            try:
                d_back = neighbor_list.index(v)
                s_back = self.vd_to_state[(neighbor, d_back)]
                self.back_state[s] = s_back
            except ValueError:
                # Asymmetric edge (should not happen); map to itself
                self.back_state[s] = s
        
        # For MSD: which vertex does each state belong to?
        self.vertex_of_state = np.empty(self.dim, dtype=int)
        for s, (v, _, _) in enumerate(self.state_to_vd):
            self.vertex_of_state[s] = v
    
    def initial_state_localized(self, vertex: int) -> np.ndarray:
        """
        Create initial state localized at vertex with uniform coin.
        
        |ψ₀⟩ = (1/√k) Σₐ |vertex⟩ ⊗ |a⟩
        """
        psi = np.zeros(self.dim, dtype=np.complex128)
        states = self.vertex_states[vertex]
        k = len(states)
        
        if k == 0:
            return psi
        
        amp = 1.0 / np.sqrt(k)
        for s in states:
            psi[s] = amp
        return psi
    
    def step(self, psi: np.ndarray) -> np.ndarray:
        """
        One DTQW step: U = S·C, applied as:
          1. Local Grover coin at each vertex
          2. Global shift via back_state permutation
        """
        # --- Grover coin: C ---
        psi_coin = psi.copy()
        
        for v in range(self.n):
            states = self.vertex_states[v]
            k = len(states)
            if k == 0:
                continue
            
            block = psi[states]
            s_sum = block.sum()
            # (Cψ)_a = 2/k * Σ_b ψ_b - ψ_a
            psi_coin[states] = (2.0 * s_sum / k) - block
        
        # --- Shift: S ---
        psi_next = np.zeros_like(psi_coin)
        psi_next[self.back_state] = psi_coin
        
        return psi_next
    
    def evolve(self, psi0: np.ndarray, n_steps: int) -> np.ndarray:
        """Evolve state by n_steps."""
        psi = psi0.copy()
        for _ in range(n_steps):
            psi = self.step(psi)
        return psi
    
    def vertex_probability(self, psi: np.ndarray, vertex: int) -> float:
        """Total probability at a vertex (sum over coin states)."""
        states = self.vertex_states[vertex]
        return float(np.sum(np.abs(psi[states]) ** 2))
    
    def compute_msd(self, psi: np.ndarray, origin_idx: int) -> float:
        """
        Compute mean squared displacement from origin.
        
        MSD = Σ_v P(v) |r_v - r_0|², where P(v) = Σ_a |ψ_{v,a}|².
        """
        # Aggregate probabilities per vertex in a vectorized way
        probs = np.zeros(self.n, dtype=float)
        np.add.at(probs, self.vertex_of_state, np.abs(psi) ** 2)
        
        r0 = self.graph.positions[origin_idx]
        disp_sq = np.sum((self.graph.positions - r0) ** 2, axis=1)
        return float(np.sum(probs * disp_sq))


# =============================================================================
# TRANSPORT ANALYSIS
# =============================================================================

def analyze_transport(
    msd_values: np.ndarray,
    time_values: np.ndarray,
    fit_start: int = 5
) -> Dict:
    """
    Analyze transport exponent from MSD data.
    
    Fits ⟨r²⟩ = A·t^β using log-log linear regression.
    
    Args:
        msd_values: Array of MSD values
        time_values: Array of time values
        fit_start: Index to start fitting (skip transient)
        
    Returns:
        Dict with fit parameters and analysis
    """
    # Use data after transient
    t = time_values[fit_start:]
    msd = msd_values[fit_start:]
    
    # Avoid log(0)
    valid = (t > 0) & (msd > 0)
    t = t[valid]
    msd = msd[valid]
    
    if len(t) < 2:
        return {'beta': np.nan, 'A': np.nan, 'error': 'Insufficient data'}
    
    # Log-log fit: log(MSD) = log(A) + β·log(t)
    log_t = np.log(t)
    log_msd = np.log(msd)
    
    # Linear regression
    coeffs = np.polyfit(log_t, log_msd, 1)
    beta = coeffs[0]
    log_A = coeffs[1]
    A = np.exp(log_A)
    
    # Compute R² for fit quality
    log_msd_fit = np.polyval(coeffs, log_t)
    ss_res = np.sum((log_msd - log_msd_fit) ** 2)
    ss_tot = np.sum((log_msd - np.mean(log_msd)) ** 2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    
    # Classify transport
    if beta > 1.8:
        transport_type = "BALLISTIC"
    elif beta > 1.2:
        transport_type = "SUPER-DIFFUSIVE"
    elif beta > 0.8:
        transport_type = "DIFFUSIVE"
    elif beta > 0.2:
        transport_type = "SUB-DIFFUSIVE"
    else:
        transport_type = "LOCALIZED"
    
    return {
        'beta': beta,
        'A': A,
        'r_squared': r_squared,
        'transport_type': transport_type,
        'theory_viable': beta > 1.5  # Need at least super-diffusive
    }


# =============================================================================
# MAIN SIMULATION
# =============================================================================

def run_golden_walk(
    max_coord: int = 3,
    n_steps: int = 100,
    method: str = 'ctqw',
    dt: float = 0.1,
    use_root_adjacency: bool = True,
    verbose: bool = True
) -> Dict:
    """
    Run the Golden Walk simulation.
    
    Args:
        max_coord: Size of D₆ lattice box
        n_steps: Number of time steps
        method: 'ctqw' or 'dtqw'
        dt: Time step for CTQW
        use_root_adjacency: Use D₆-root neighbors (True) or 3D threshold (False)
        verbose: Print progress
        
    Returns:
        Dict with results
    """
    if verbose:
        print("=" * 60)
        print("GOLDEN WALK SIMULATION")
        print("=" * 60)
        print(f"Method: {method.upper()}")
        print(f"Lattice size: max_coord={max_coord}")
        print(f"Steps: {n_steps}")
        print(f"Adjacency: {'D₆-root (correct)' if use_root_adjacency else '3D threshold'}")
        print()
    
    # Generate graph
    t0 = time.time()
    graph = H3Graph(max_coord=max_coord, use_root_adjacency=use_root_adjacency, verbose=verbose)
    t_graph = time.time() - t0
    
    if graph.n_vertices < 10:
        print("ERROR: Graph too small. Increase max_coord.")
        return {'error': 'Graph too small'}
    
    # Find central vertex (closest to origin)
    distances = np.linalg.norm(graph.positions, axis=1)
    origin_idx = np.argmin(distances)
    
    if verbose:
        print(f"\nOrigin vertex: {origin_idx}")
        print(f"  Position: {graph.positions[origin_idx]}")
        print(f"  Coordination: {graph.coordination[origin_idx]}")
    
    # Initialize quantum walk
    if verbose:
        print(f"\nInitializing {method.upper()}...")
    
    t0 = time.time()
    
    if method == 'ctqw':
        qw = CTQW(graph)
        psi = np.zeros(graph.n_vertices, dtype=np.complex128)
        psi[origin_idx] = 1.0
        
        # Time evolution
        times = np.arange(0, n_steps * dt, dt)
        msd_values = np.zeros(len(times))
        
        if verbose:
            print("Running CTQW evolution...")
        
        for i, t in enumerate(times):
            if i > 0:
                psi = qw.evolve(psi, dt)
            msd_values[i] = qw.compute_msd(psi, origin_idx)
            
            if verbose and i % max(1, len(times) // 10) == 0:
                print(f"  Step {i}/{len(times)-1}, MSD = {msd_values[i]:.4f}")
        
        time_values = times
        
    elif method == 'dtqw':
        qw = DTQW(graph)
        psi = qw.initial_state_localized(origin_idx)
        
        if verbose:
            print(f"  State space dimension: {qw.dim}")
        
        # Discrete evolution
        time_values = np.arange(n_steps, dtype=float)
        msd_values = np.zeros(n_steps, dtype=float)
        
        if verbose:
            print("Running DTQW evolution (local Grover coin)...")
        
        for i in range(n_steps):
            if i > 0:
                psi = qw.step(psi)
            msd_values[i] = qw.compute_msd(psi, origin_idx)
            
            if verbose and i % max(1, n_steps // 10) == 0:
                print(f"  Step {i}/{n_steps-1}, MSD = {msd_values[i]:.4f}")
    
    else:
        raise ValueError(f"Unknown method: {method}")
    
    t_sim = time.time() - t0
    
    # Analyze transport
    if verbose:
        print("\nAnalyzing transport...")
    
    analysis = analyze_transport(msd_values, time_values)
    
    # Print results
    if verbose:
        print("\n" + "=" * 60)
        print("RESULTS")
        print("=" * 60)
        print(f"Transport exponent β = {analysis['beta']:.4f}")
        print(f"Fit quality R² = {analysis['r_squared']:.4f}")
        print(f"Transport type: {analysis['transport_type']}")
        print()
        
        if analysis['theory_viable']:
            print("✓ THEORY VIABLE: Transport is sufficiently ballistic")
            print("  Emergent Lorentz invariance is possible")
        else:
            print("✗ THEORY CHALLENGED: Transport is sub-ballistic")
            print("  May indicate localization effects")
        
        print()
        print(f"Timing: Graph={t_graph:.2f}s, Simulation={t_sim:.2f}s")
    
    return {
        'graph': graph,
        'time_values': time_values,
        'msd_values': msd_values,
        'analysis': analysis,
        'method': method,
        'n_steps': n_steps,
        'origin_idx': origin_idx
    }


# =============================================================================
# PLOTTING (optional)
# =============================================================================

def plot_results(results: Dict, save_path: Optional[str] = None):
    """Plot MSD vs time with power-law fit."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available, skipping plot")
        return
    
    t = results['time_values']
    msd = results['msd_values']
    analysis = results['analysis']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Linear plot
    ax1.plot(t, msd, 'b-', linewidth=1.5, label='Data')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('MSD ⟨r²⟩')
    ax1.set_title('Mean Squared Displacement')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Log-log plot with fit
    valid = (t > 0) & (msd > 0)
    ax2.loglog(t[valid], msd[valid], 'b.', markersize=3, label='Data')
    
    # Plot fit line
    t_fit = t[valid]
    msd_fit = analysis['A'] * t_fit ** analysis['beta']
    ax2.loglog(t_fit, msd_fit, 'r-', linewidth=2, 
               label=f'Fit: β = {analysis["beta"]:.3f}')
    
    # Reference lines
    if len(t_fit) > 10:
        ref_idx = 10
        ax2.loglog(t_fit, t_fit**2 * msd[ref_idx]/t[ref_idx]**2, 'g--', alpha=0.5, label='β=2 (ballistic)')
        ax2.loglog(t_fit, t_fit * msd[ref_idx]/t[ref_idx], 'm--', alpha=0.5, label='β=1 (diffusive)')
    
    ax2.set_xlabel('Time')
    ax2.set_ylabel('MSD ⟨r²⟩')
    ax2.set_title(f'Transport Analysis: {analysis["transport_type"]}')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


# =============================================================================
# COMMAND LINE INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Golden Walk: Quantum Walk on H₃ Quasicrystal'
    )
    parser.add_argument('--size', choices=['tiny', 'small', 'medium', 'large'],
                        default='small', help='Graph size')
    parser.add_argument('--steps', type=int, default=100,
                        help='Number of time steps')
    parser.add_argument('--method', choices=['ctqw', 'dtqw'],
                        default='ctqw', help='Quantum walk method')
    parser.add_argument('--plot', action='store_true',
                        help='Generate plot')
    parser.add_argument('--save', type=str, default=None,
                        help='Save plot to file')
    parser.add_argument('--threshold', action='store_true',
                        help='Use 3D threshold adjacency instead of D₆-root')
    
    args = parser.parse_args()
    
    # Map size to max_coord
    size_map = {
        'tiny': 1,
        'small': 2,
        'medium': 3,
        'large': 4
    }
    max_coord = size_map[args.size]
    
    # Run simulation
    results = run_golden_walk(
        max_coord=max_coord,
        n_steps=args.steps,
        method=args.method,
        use_root_adjacency=not args.threshold,
        verbose=True
    )
    
    # Plot if requested
    if args.plot or args.save:
        plot_results(results, args.save)
    
    return results


if __name__ == "__main__":
    main()
