"""
Vortex Point Dynamics Simulation
================================

Simulates N-point vortex dynamics to test the Golden Direction Hypothesis.
Compares stability of Golden (Vogel) vs Hexagonal vs Random configurations.

The stability prediction:
- Hexagonal: Has "soft modes" (slip planes) → unstable under perturbation
- Golden: "Jammed" (no soft modes) → stable under perturbation
"""

import numpy as np

# Constants
PHI = (1 + np.sqrt(5)) / 2
GOLDEN_ANGLE = 2 * np.pi / PHI**2  # ≈ 137.5°

print("=" * 70)
print("VORTEX POINT DYNAMICS: Golden vs Hexagonal Stability Test")
print("=" * 70)
print(f"Golden angle = {np.degrees(GOLDEN_ANGLE):.2f}°")
print()

# =============================================================================
# Generate initial configurations
# =============================================================================

def golden_positions(N, R=1.0):
    """Vogel spiral positions."""
    positions = []
    for n in range(1, N + 1):
        theta = n * GOLDEN_ANGLE
        r = R * np.sqrt(n / N)
        positions.append(r * np.exp(1j * theta))
    return np.array(positions)

def hexagonal_positions(N, spacing=0.2):
    """Hexagonal lattice positions (approximately N points)."""
    positions = [0j]  # Center
    ring = 1
    while len(positions) < N:
        for i in range(6 * ring):
            if len(positions) >= N:
                break
            angle = i * np.pi / (3 * ring)
            r = ring * spacing
            positions.append(r * np.exp(1j * angle))
        ring += 1
    return np.array(positions[:N])

def random_positions(N, R=1.0, seed=42):
    """Random positions within radius R."""
    np.random.seed(seed)
    r = R * np.sqrt(np.random.random(N))
    theta = 2 * np.pi * np.random.random(N)
    return r * np.exp(1j * theta)

# =============================================================================
# Vortex dynamics
# =============================================================================

def compute_velocity(z, Gamma=1.0):
    """
    Compute velocity of each vortex due to all others.
    dz_j/dt = (Γ/2πi) Σ_{k≠j} 1/(z_j - z_k)
    """
    N = len(z)
    v = np.zeros(N, dtype=complex)
    
    for j in range(N):
        for k in range(N):
            if j != k:
                dz = z[j] - z[k]
                if abs(dz) > 1e-10:  # Avoid singularity
                    v[j] += 1.0 / dz
    
    v *= Gamma / (2 * np.pi * 1j)
    return v

def compute_energy(z, Gamma=1.0):
    """
    Compute Kirchhoff Hamiltonian (interaction energy).
    H = -(Γ²/4π) Σ_{j<k} ln|z_j - z_k|
    """
    N = len(z)
    H = 0.0
    for j in range(N):
        for k in range(j + 1, N):
            dz = abs(z[j] - z[k])
            if dz > 1e-10:
                H -= np.log(dz)
    return H * Gamma**2 / (4 * np.pi)

def compute_dispersion(z):
    """Measure how spread out the vortices are (standard deviation of |z|)."""
    return np.std(np.abs(z))

def compute_angular_momentum(z):
    """Total angular momentum (moment of inertia)."""
    return np.sum(np.abs(z)**2)

def step_rk4(z, dt, Gamma=1.0):
    """Runge-Kutta 4th order step."""
    k1 = compute_velocity(z, Gamma)
    k2 = compute_velocity(z + 0.5 * dt * k1, Gamma)
    k3 = compute_velocity(z + 0.5 * dt * k2, Gamma)
    k4 = compute_velocity(z + dt * k3, Gamma)
    return z + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

# =============================================================================
# Stability analysis: compute Jacobian eigenvalues
# =============================================================================

def compute_stability_matrix(z):
    """
    Compute the linearized stability matrix for small perturbations.
    Returns eigenvalues of the Jacobian.
    """
    N = len(z)
    # Build 2N x 2N real matrix (treating z = x + iy)
    M = np.zeros((2*N, 2*N))
    
    for j in range(N):
        for k in range(N):
            if j != k:
                dz = z[j] - z[k]
                r2 = abs(dz)**2
                if r2 > 1e-10:
                    # d(v_j)/d(z_k) contribution
                    # v_j = Σ 1/(z_j - z_k), so dv_j/dz_k = 1/(z_j-z_k)^2
                    coeff = 1.0 / (dz**2)
                    
                    # Real and imaginary parts
                    M[2*j, 2*k] = -np.real(coeff) / (2 * np.pi)
                    M[2*j, 2*k+1] = np.imag(coeff) / (2 * np.pi)
                    M[2*j+1, 2*k] = -np.imag(coeff) / (2 * np.pi)
                    M[2*j+1, 2*k+1] = -np.real(coeff) / (2 * np.pi)
                    
                    # Diagonal contribution
                    M[2*j, 2*j] += np.real(coeff) / (2 * np.pi)
                    M[2*j, 2*j+1] += -np.imag(coeff) / (2 * np.pi)
                    M[2*j+1, 2*j] += np.imag(coeff) / (2 * np.pi)
                    M[2*j+1, 2*j+1] += np.real(coeff) / (2 * np.pi)
    
    eigenvalues = np.linalg.eigvals(M)
    return eigenvalues

def analyze_spectrum(eigenvalues, name):
    """Analyze the eigenvalue spectrum."""
    real_parts = np.real(eigenvalues)
    
    # Count soft modes (near zero)
    soft_threshold = 0.1
    n_soft = np.sum(np.abs(real_parts) < soft_threshold)
    
    # Max growth rate
    max_growth = np.max(real_parts)
    
    # Spectral gap (smallest non-zero |Re(λ)|)
    nonzero = np.abs(real_parts[np.abs(real_parts) > 1e-6])
    gap = np.min(nonzero) if len(nonzero) > 0 else 0
    
    # Schur measure (sum of squares)
    schur = np.sum(real_parts**2)
    
    print(f"{name}:")
    print(f"  Soft modes (|Re(λ)| < {soft_threshold}): {n_soft}")
    print(f"  Max growth rate: {max_growth:.4f}")
    print(f"  Spectral gap: {gap:.4f}")
    print(f"  Schur measure: {schur:.4f}")
    
    return {'soft': n_soft, 'max_growth': max_growth, 'gap': gap, 'schur': schur}

# =============================================================================
# Run the simulation
# =============================================================================

N_VORTICES = 19  # Number of vortices
DT = 0.01  # Time step
N_STEPS = 500  # Number of steps
PERTURBATION = 0.05  # Initial perturbation amplitude

print(f"Parameters: N={N_VORTICES}, dt={DT}, steps={N_STEPS}")
print(f"Perturbation amplitude: {PERTURBATION}")
print()

# Generate initial configurations
configs = {
    'Golden': golden_positions(N_VORTICES, R=0.8),
    'Hexagonal': hexagonal_positions(N_VORTICES, spacing=0.25),
    'Random': random_positions(N_VORTICES, R=0.8, seed=42),
}

# =============================================================================
# Part 1: Eigenvalue Analysis (Static)
# =============================================================================

print("=" * 70)
print("PART 1: STABILITY SPECTRUM ANALYSIS")
print("=" * 70)
print()

spectrum_results = {}
for name, z0 in configs.items():
    # Center the configuration
    z0 = z0 - np.mean(z0)
    eigenvalues = compute_stability_matrix(z0)
    spectrum_results[name] = analyze_spectrum(eigenvalues, name)
    print()

# Compare
print("-" * 40)
print("COMPARISON:")
golden_soft = spectrum_results['Golden']['soft']
hex_soft = spectrum_results['Hexagonal']['soft']
random_soft = spectrum_results['Random']['soft']

if golden_soft < hex_soft:
    print(f"✓ Golden has FEWER soft modes than Hexagonal ({golden_soft} vs {hex_soft})")
else:
    print(f"✗ Golden has more soft modes than Hexagonal ({golden_soft} vs {hex_soft})")

if spectrum_results['Golden']['gap'] > spectrum_results['Hexagonal']['gap']:
    print(f"✓ Golden has LARGER spectral gap ({spectrum_results['Golden']['gap']:.4f} vs {spectrum_results['Hexagonal']['gap']:.4f})")

print()

# =============================================================================
# Part 2: Dynamic Evolution
# =============================================================================

print("=" * 70)
print("PART 2: DYNAMIC EVOLUTION UNDER PERTURBATION")
print("=" * 70)
print()

def run_dynamics(z0, name, dt=DT, n_steps=N_STEPS, pert=PERTURBATION):
    """Run vortex dynamics and track metrics."""
    # Add random perturbation
    np.random.seed(123)  # Same perturbation for all
    z = z0.copy() + pert * (np.random.randn(len(z0)) + 1j * np.random.randn(len(z0)))
    
    # Center
    z = z - np.mean(z)
    
    # Track metrics
    times = [0]
    energies = [compute_energy(z)]
    dispersions = [compute_dispersion(z)]
    
    # Evolve
    for step in range(n_steps):
        z = step_rk4(z, dt)
        
        # Check for numerical instability (vortices getting too close)
        min_dist = np.min([abs(z[i] - z[j]) for i in range(len(z)) for j in range(i+1, len(z))])
        if min_dist < 0.01:
            print(f"  {name}: Vortices collided at step {step}!")
            break
        
        if step % 50 == 0:
            times.append(step * dt)
            energies.append(compute_energy(z))
            dispersions.append(compute_dispersion(z))
    
    return {
        'final_z': z,
        'times': times,
        'energies': energies,
        'dispersions': dispersions,
        'final_dispersion': dispersions[-1],
        'dispersion_change': dispersions[-1] / dispersions[0] if dispersions[0] > 0 else 1
    }

print("Running dynamics...")
print()

dynamics_results = {}
for name, z0 in configs.items():
    z0_centered = z0 - np.mean(z0)
    result = run_dynamics(z0_centered, name)
    dynamics_results[name] = result
    
    print(f"{name}:")
    print(f"  Initial dispersion: {result['dispersions'][0]:.4f}")
    print(f"  Final dispersion:   {result['final_dispersion']:.4f}")
    print(f"  Change ratio:       {result['dispersion_change']:.4f}")
    print()

# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("SUMMARY: GOLDEN DIRECTION HYPOTHESIS TEST")
print("=" * 70)
print()

print("STABILITY SPECTRUM:")
print(f"  Golden soft modes:    {spectrum_results['Golden']['soft']}")
print(f"  Hexagonal soft modes: {spectrum_results['Hexagonal']['soft']}")
print(f"  Random soft modes:    {spectrum_results['Random']['soft']}")
print()

print("DYNAMIC STABILITY (dispersion change):")
for name in ['Golden', 'Hexagonal', 'Random']:
    dc = dynamics_results[name]['dispersion_change']
    print(f"  {name}: {dc:.3f}x")
print()

# Verdict
golden_more_stable = (
    spectrum_results['Golden']['soft'] <= spectrum_results['Hexagonal']['soft'] and
    dynamics_results['Golden']['dispersion_change'] <= dynamics_results['Hexagonal']['dispersion_change']
)

print("VERDICT:")
if golden_more_stable:
    print("✓ Golden configuration shows BETTER stability than Hexagonal")
    print("  - Fewer (or equal) soft modes in spectrum")
    print("  - Less dispersion under perturbation")
    print()
    print("This SUPPORTS the Golden Direction Hypothesis:")
    print("  φ-based packing eliminates destabilizing resonances")
else:
    print("Results are mixed - more analysis needed")

print()
print("Note: This is a simplified 2D point-vortex model.")
print("Full 3D Navier-Stokes would require DNS simulation.")

