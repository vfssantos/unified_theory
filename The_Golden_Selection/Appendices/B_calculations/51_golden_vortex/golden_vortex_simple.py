"""
Golden Vortex Hypothesis Test (Simple Version - No Matplotlib)
==============================================================

Tests whether vortex configurations with Golden Angle (Vogel spiral) packing
have lower directional roughness κ_GST = ∫|∇ω̂|² than standard configurations.
"""

import numpy as np

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618
GOLDEN_ANGLE = 2 * np.pi / PHI**2  # ≈ 137.5° in radians

print("=" * 70)
print("GOLDEN VORTEX HYPOTHESIS TEST")
print("=" * 70)
print(f"Golden ratio φ = {PHI:.6f}")
print(f"Golden angle Ψ = 2π/φ² = {np.degrees(GOLDEN_ANGLE):.2f}°")
print()

# =============================================================================
# Create grid
# =============================================================================

def create_grid(N=48, L=1.5):
    """Create a 3D grid for vorticity field."""
    x = np.linspace(-L, L, N)
    dx = x[1] - x[0]
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    return X, Y, Z, dx

# =============================================================================
# Vorticity configurations
# =============================================================================

def gaussian_vortex_tube(X, Y, Z, radius=0.3, strength=1.0):
    """Standard Gaussian vortex tube along z-axis."""
    r_sq = X**2 + Y**2
    omega_z = strength * np.exp(-r_sq / (2 * radius**2))
    return np.zeros_like(X), np.zeros_like(X), omega_z

def vogel_spiral_bundle(X, Y, Z, n_filaments=34, radius=0.4, fil_r=0.08):
    """Bundle of vortex filaments in Vogel spiral (Golden Angle) pattern."""
    omega_z = np.zeros_like(X)
    
    for n in range(1, n_filaments + 1):
        theta = n * GOLDEN_ANGLE
        r = radius * np.sqrt(n / n_filaments)
        cx, cy = r * np.cos(theta), r * np.sin(theta)
        r_sq = (X - cx)**2 + (Y - cy)**2
        omega_z += np.exp(-r_sq / (2 * fil_r**2))
    
    return np.zeros_like(X), np.zeros_like(X), omega_z

def hexagonal_bundle(X, Y, Z, n_rings=3, spacing=0.2, fil_r=0.08):
    """Bundle of vortex filaments in hexagonal arrangement."""
    omega_z = np.zeros_like(X)
    
    positions = [(0, 0)]
    for ring in range(1, n_rings + 1):
        for i in range(6 * ring):
            angle = i * np.pi / (3 * ring) + np.pi / 6
            r = ring * spacing
            positions.append((r * np.cos(angle), r * np.sin(angle)))
    
    for cx, cy in positions:
        r_sq = (X - cx)**2 + (Y - cy)**2
        omega_z += np.exp(-r_sq / (2 * fil_r**2))
    
    return np.zeros_like(X), np.zeros_like(X), omega_z

def random_bundle(X, Y, Z, n_filaments=34, max_r=0.4, fil_r=0.08, seed=42):
    """Bundle of vortex filaments at random positions."""
    np.random.seed(seed)
    omega_z = np.zeros_like(X)
    
    for _ in range(n_filaments):
        r = max_r * np.sqrt(np.random.random())
        theta = 2 * np.pi * np.random.random()
        cx, cy = r * np.cos(theta), r * np.sin(theta)
        r_sq = (X - cx)**2 + (Y - cy)**2
        omega_z += np.exp(-r_sq / (2 * fil_r**2))
    
    return np.zeros_like(X), np.zeros_like(X), omega_z

# =============================================================================
# Compute κ_GST = ∫|∇ω̂|²
# =============================================================================

def compute_kappa_GST(omega_x, omega_y, omega_z, dx, eps=1e-10):
    """
    Compute κ_GST = ∫|∇ω̂|² dx (Dirichlet energy of direction field)
    """
    # Magnitude
    mag = np.sqrt(omega_x**2 + omega_y**2 + omega_z**2)
    mask = mag > eps
    
    # Direction field (unit vector)
    omega_hat_x = np.where(mask, omega_x / mag, 0)
    omega_hat_y = np.where(mask, omega_y / mag, 0)
    omega_hat_z = np.where(mask, omega_z / mag, 0)
    
    # Gradients of each component
    def grad_mag_sq(f):
        gx = np.gradient(f, dx, axis=0)
        gy = np.gradient(f, dx, axis=1)
        gz = np.gradient(f, dx, axis=2)
        return gx**2 + gy**2 + gz**2
    
    grad_sq = grad_mag_sq(omega_hat_x) + grad_mag_sq(omega_hat_y) + grad_mag_sq(omega_hat_z)
    
    # Integrate where vorticity is significant
    kappa = np.sum(grad_sq * mask) * dx**3
    
    # Also compute enstrophy for comparison
    enstrophy = 0.5 * np.sum(mag**2) * dx**3
    
    return kappa, enstrophy

# =============================================================================
# Run the test
# =============================================================================

print("Creating vorticity fields (N=48 grid)...")
X, Y, Z, dx = create_grid(N=48, L=1.5)

configs = {
    'Gaussian Tube': gaussian_vortex_tube(X, Y, Z),
    'Golden (Vogel)': vogel_spiral_bundle(X, Y, Z),
    'Hexagonal': hexagonal_bundle(X, Y, Z),
    'Random': random_bundle(X, Y, Z),
}

print()
print("-" * 70)
print(f"{'Configuration':<20} {'κ_GST':>15} {'Enstrophy':>15} {'κ/Enstrophy':>15}")
print("-" * 70)

results = {}
for name, (ox, oy, oz) in configs.items():
    kappa, enstrophy = compute_kappa_GST(ox, oy, oz, dx)
    results[name] = {'kappa': kappa, 'enstrophy': enstrophy}
    ratio = kappa / enstrophy if enstrophy > 0 else 0
    print(f"{name:<20} {kappa:>15.4f} {enstrophy:>15.4f} {ratio:>15.4f}")

print("-" * 70)
print()

# =============================================================================
# Analysis
# =============================================================================

golden_k = results['Golden (Vogel)']['kappa']
random_k = results['Random']['kappa']
hex_k = results['Hexagonal']['kappa']
gauss_k = results['Gaussian Tube']['kappa']

print("ANALYSIS")
print("=" * 70)
print()
print("κ_GST comparisons (lower = smoother direction field):")
print()
print(f"  Golden vs Random:    {golden_k/random_k:.3f}x")
print(f"  Golden vs Hexagonal: {golden_k/hex_k:.3f}x")
print(f"  Golden vs Gaussian:  {golden_k/gauss_k:.3f}x")
print()

# Find best
best = min(results.keys(), key=lambda k: results[k]['kappa'])
print(f"Lowest κ_GST: {best} ({results[best]['kappa']:.4f})")
print()

# Key test
print("=" * 70)
print("KEY TEST: Golden Direction Hypothesis")
print("=" * 70)
print()

if golden_k < random_k:
    print("✓ SUPPORTED: Golden (Vogel) packing has LOWER κ_GST than Random")
    print(f"  Improvement: {(1 - golden_k/random_k)*100:.1f}% reduction in directional roughness")
else:
    print("✗ NOT SUPPORTED: Random has lower κ_GST than Golden")

print()

if golden_k < hex_k:
    print("✓ Golden packing beats Hexagonal (crystalline) arrangement")
else:
    print("✗ Hexagonal packing has lower κ_GST than Golden")

print()

# Physical interpretation
print("=" * 70)
print("PHYSICAL INTERPRETATION")
print("=" * 70)
print()
print("κ_GST = ∫|∇ω̂|² measures how rapidly the vorticity DIRECTION changes.")
print()
print("Lower κ_GST means:")
print("  • Vortex lines are more smoothly aligned")
print("  • Direction field has less 'roughness'")
print("  • Constantin-Fefferman criterion more easily satisfied")
print("  • LESS likely to form singularities")
print()
print("The Golden Angle Ψ = 2π/φ² ≈ 137.5° generates the Vogel spiral,")
print("which avoids resonances and provides optimal isotropic packing.")
print()

# Summary
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print(f"Golden ratio φ = {PHI:.6f}")
print(f"Golden angle  Ψ = {np.degrees(GOLDEN_ANGLE):.2f}°")
print()
print("Result: The Golden Direction Hypothesis predicts that vortex")
print("bundles with Vogel spiral packing have minimal directional roughness.")
print()
if golden_k < random_k:
    print("This simple numerical test SUPPORTS the hypothesis.")
    print("Golden packing reduces κ_GST compared to random arrangement.")
else:
    print("This simple test does NOT support the hypothesis in its basic form.")
    print("More sophisticated tests may be needed.")

