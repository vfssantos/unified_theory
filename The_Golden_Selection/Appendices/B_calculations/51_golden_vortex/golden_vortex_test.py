"""
Golden Vortex Hypothesis Test
=============================

Tests whether vortex configurations with Golden Angle (Vogel spiral) packing
have lower directional roughness κ_GST = ∫|∇ω̂|² than standard configurations.

The Golden Direction Hypothesis claims:
- κ_GST[ω̂] = Dirichlet energy of direction field
- Minimizing κ_GST → Constantin-Fefferman criterion → NS regularity
- Golden Angle packing minimizes κ_GST for vortex bundles
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618
GOLDEN_ANGLE = 2 * np.pi / PHI**2  # ≈ 137.5° in radians

print("=" * 60)
print("GOLDEN VORTEX HYPOTHESIS TEST")
print("=" * 60)
print(f"Golden ratio φ = {PHI:.6f}")
print(f"Golden angle Ψ = {np.degrees(GOLDEN_ANGLE):.2f}°")
print()

# =============================================================================
# PART 1: Create vorticity fields
# =============================================================================

def create_grid(N=64, L=2.0):
    """Create a 3D grid for vorticity field."""
    x = np.linspace(-L, L, N)
    y = np.linspace(-L, L, N)
    z = np.linspace(-L, L, N)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    dx = x[1] - x[0]
    return X, Y, Z, dx

def gaussian_vortex_tube(X, Y, Z, radius=0.5, strength=1.0):
    """
    Standard Gaussian vortex tube along z-axis.
    Vorticity ω = (0, 0, ω_z) with Gaussian profile.
    """
    r_sq = X**2 + Y**2
    omega_z = strength * np.exp(-r_sq / (2 * radius**2))
    
    # Vorticity vector field
    omega_x = np.zeros_like(X)
    omega_y = np.zeros_like(X)
    
    return omega_x, omega_y, omega_z

def vogel_spiral_vortex_bundle(X, Y, Z, n_filaments=34, radius=0.3, filament_radius=0.1, strength=1.0):
    """
    Bundle of vortex filaments arranged in Vogel spiral pattern.
    Uses Golden Angle for optimal packing.
    """
    omega_x = np.zeros_like(X)
    omega_y = np.zeros_like(X)
    omega_z = np.zeros_like(X)
    
    # Generate filament positions using Vogel spiral
    for n in range(1, n_filaments + 1):
        theta = n * GOLDEN_ANGLE
        r = radius * np.sqrt(n / n_filaments)  # Fermat spiral scaling
        
        cx = r * np.cos(theta)
        cy = r * np.sin(theta)
        
        # Each filament is a small Gaussian vortex
        r_sq = (X - cx)**2 + (Y - cy)**2
        omega_z += strength * np.exp(-r_sq / (2 * filament_radius**2))
    
    return omega_x, omega_y, omega_z

def hexagonal_vortex_bundle(X, Y, Z, n_rings=3, spacing=0.25, filament_radius=0.1, strength=1.0):
    """
    Bundle of vortex filaments in hexagonal (crystalline) arrangement.
    Like Abrikosov lattice in superconductors.
    """
    omega_x = np.zeros_like(X)
    omega_y = np.zeros_like(X)
    omega_z = np.zeros_like(X)
    
    # Generate hexagonal lattice positions
    positions = [(0, 0)]  # Center
    for ring in range(1, n_rings + 1):
        for i in range(6 * ring):
            angle = i * np.pi / (3 * ring) + np.pi / 6
            r = ring * spacing
            positions.append((r * np.cos(angle), r * np.sin(angle)))
    
    for cx, cy in positions:
        r_sq = (X - cx)**2 + (Y - cy)**2
        omega_z += strength * np.exp(-r_sq / (2 * filament_radius**2))
    
    return omega_x, omega_y, omega_z

def random_vortex_bundle(X, Y, Z, n_filaments=34, max_radius=0.5, filament_radius=0.1, strength=1.0, seed=42):
    """
    Bundle of vortex filaments at random positions.
    """
    np.random.seed(seed)
    omega_x = np.zeros_like(X)
    omega_y = np.zeros_like(X)
    omega_z = np.zeros_like(X)
    
    for _ in range(n_filaments):
        r = max_radius * np.sqrt(np.random.random())
        theta = 2 * np.pi * np.random.random()
        cx = r * np.cos(theta)
        cy = r * np.sin(theta)
        
        r_sq = (X - cx)**2 + (Y - cy)**2
        omega_z += strength * np.exp(-r_sq / (2 * filament_radius**2))
    
    return omega_x, omega_y, omega_z

# =============================================================================
# PART 2: Compute κ_GST = ∫|∇ω̂|² (Dirichlet energy of direction field)
# =============================================================================

def compute_direction_field(omega_x, omega_y, omega_z, epsilon=1e-10):
    """
    Compute unit direction field ω̂ = ω/|ω|
    Returns NaN where |ω| < epsilon (undefined direction)
    """
    omega_mag = np.sqrt(omega_x**2 + omega_y**2 + omega_z**2)
    
    # Avoid division by zero
    mask = omega_mag > epsilon
    
    omega_hat_x = np.where(mask, omega_x / omega_mag, np.nan)
    omega_hat_y = np.where(mask, omega_y / omega_mag, np.nan)
    omega_hat_z = np.where(mask, omega_z / omega_mag, np.nan)
    
    return omega_hat_x, omega_hat_y, omega_hat_z, omega_mag, mask

def compute_gradient_magnitude_squared(field, dx):
    """
    Compute |∇f|² using central differences.
    """
    # Gradients in each direction
    grad_x = np.gradient(field, dx, axis=0)
    grad_y = np.gradient(field, dx, axis=1)
    grad_z = np.gradient(field, dx, axis=2)
    
    return grad_x**2 + grad_y**2 + grad_z**2

def compute_kappa_GST(omega_x, omega_y, omega_z, dx, epsilon=1e-10):
    """
    Compute κ_GST = ∫|∇ω̂|² dx
    
    This is the Dirichlet energy of the direction field.
    Lower values = smoother direction field = better for regularity.
    """
    # Get direction field
    omega_hat_x, omega_hat_y, omega_hat_z, omega_mag, mask = \
        compute_direction_field(omega_x, omega_y, omega_z, epsilon)
    
    # Compute |∇ω̂|² for each component
    # Only compute where direction is well-defined
    grad_sq_x = compute_gradient_magnitude_squared(np.nan_to_num(omega_hat_x), dx)
    grad_sq_y = compute_gradient_magnitude_squared(np.nan_to_num(omega_hat_y), dx)
    grad_sq_z = compute_gradient_magnitude_squared(np.nan_to_num(omega_hat_z), dx)
    
    # Total |∇ω̂|²
    grad_omega_hat_sq = grad_sq_x + grad_sq_y + grad_sq_z
    
    # Integrate only where vorticity is significant
    # Weight by vorticity magnitude to focus on active regions
    weighted_integrand = grad_omega_hat_sq * (omega_mag > epsilon)
    
    kappa_GST = np.nansum(weighted_integrand) * dx**3
    
    # Also compute weighted version (more physical)
    kappa_weighted = np.nansum(grad_omega_hat_sq * omega_mag**2) * dx**3
    
    # Volume where vorticity is significant
    active_volume = np.sum(omega_mag > epsilon) * dx**3
    
    return kappa_GST, kappa_weighted, active_volume, grad_omega_hat_sq

def compute_enstrophy(omega_x, omega_y, omega_z, dx):
    """Compute enstrophy Ω = ½∫|ω|² dx"""
    omega_sq = omega_x**2 + omega_y**2 + omega_z**2
    return 0.5 * np.sum(omega_sq) * dx**3

# =============================================================================
# PART 3: Run the comparison
# =============================================================================

print("Creating vorticity fields...")
print()

# Create grid
N = 64  # Grid resolution
L = 1.5  # Domain half-size
X, Y, Z, dx = create_grid(N, L)

# Create different vortex configurations
configs = {}

# 1. Single Gaussian vortex tube
configs['Gaussian Tube'] = gaussian_vortex_tube(X, Y, Z, radius=0.3, strength=1.0)

# 2. Vogel spiral bundle (Golden)
configs['Golden (Vogel)'] = vogel_spiral_vortex_bundle(X, Y, Z, n_filaments=34, 
                                                        radius=0.4, filament_radius=0.08)

# 3. Hexagonal bundle (Crystalline)
configs['Hexagonal'] = hexagonal_vortex_bundle(X, Y, Z, n_rings=3, 
                                                spacing=0.2, filament_radius=0.08)

# 4. Random bundle
configs['Random'] = random_vortex_bundle(X, Y, Z, n_filaments=34, 
                                          max_radius=0.4, filament_radius=0.08)

# Compute metrics for each configuration
print("-" * 60)
print(f"{'Configuration':<20} {'κ_GST':>12} {'κ_weighted':>14} {'Enstrophy':>12}")
print("-" * 60)

results = {}
for name, (omega_x, omega_y, omega_z) in configs.items():
    kappa, kappa_w, vol, grad_sq = compute_kappa_GST(omega_x, omega_y, omega_z, dx)
    enstrophy = compute_enstrophy(omega_x, omega_y, omega_z, dx)
    
    results[name] = {
        'kappa_GST': kappa,
        'kappa_weighted': kappa_w,
        'enstrophy': enstrophy,
        'volume': vol,
        'grad_sq': grad_sq,
        'omega': (omega_x, omega_y, omega_z)
    }
    
    print(f"{name:<20} {kappa:>12.4f} {kappa_w:>14.6f} {enstrophy:>12.4f}")

print("-" * 60)
print()

# =============================================================================
# PART 4: Analysis
# =============================================================================

# Find the best configuration
best_config = min(results.keys(), key=lambda k: results[k]['kappa_GST'])
golden_kappa = results['Golden (Vogel)']['kappa_GST']
gaussian_kappa = results['Gaussian Tube']['kappa_GST']

print("ANALYSIS")
print("=" * 60)
print(f"Lowest κ_GST: {best_config}")
print()

# Compare Golden vs others
print("Comparison to Golden (Vogel) spiral:")
for name, data in results.items():
    if name != 'Golden (Vogel)':
        ratio = data['kappa_GST'] / golden_kappa
        print(f"  {name}: κ_GST is {ratio:.2f}x the Golden value")

print()

# The key test: Is Golden lower than Random?
golden_vs_random = results['Random']['kappa_GST'] / golden_kappa
print(f"KEY TEST: Random/Golden ratio = {golden_vs_random:.3f}")
if golden_vs_random > 1:
    print("  ✓ Golden packing has LOWER directional roughness than random")
else:
    print("  ✗ Unexpected: Random has lower κ_GST")

print()

# =============================================================================
# PART 5: Visualization
# =============================================================================

print("Generating visualizations...")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot cross-sections of each configuration
for ax, (name, data) in zip(axes.flat, results.items()):
    omega_x, omega_y, omega_z = data['omega']
    
    # Take middle z-slice
    z_mid = N // 2
    omega_slice = omega_z[:, :, z_mid]
    
    im = ax.imshow(omega_slice.T, origin='lower', cmap='RdBu_r',
                   extent=[-L, L, -L, L], vmin=-1, vmax=1)
    ax.set_title(f"{name}\nκ_GST = {data['kappa_GST']:.4f}")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('/Users/vfssantos/Documents/Research/Essays/golden_slice/The_Golden_Selection/Appendices/B_calculations/51_golden_vortex/vortex_comparison.png', dpi=150)
print("  Saved: vortex_comparison.png")

# Plot the Vogel spiral pattern
fig2, ax2 = plt.subplots(figsize=(8, 8))
n_points = 34
for n in range(1, n_points + 1):
    theta = n * GOLDEN_ANGLE
    r = 0.4 * np.sqrt(n / n_points)
    ax2.plot(r * np.cos(theta), r * np.sin(theta), 'ko', markersize=8)

ax2.set_title(f'Vogel Spiral (Golden Angle = {np.degrees(GOLDEN_ANGLE):.1f}°)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_aspect('equal')
ax2.set_xlim(-0.5, 0.5)
ax2.set_ylim(-0.5, 0.5)
ax2.grid(True, alpha=0.3)

# Add golden ratio annotation
ax2.text(0.02, 0.98, f'φ = {PHI:.4f}\nΨ = 2π/φ² = {np.degrees(GOLDEN_ANGLE):.1f}°', 
         transform=ax2.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.savefig('/Users/vfssantos/Documents/Research/Essays/golden_slice/The_Golden_Selection/Appendices/B_calculations/51_golden_vortex/vogel_spiral.png', dpi=150)
print("  Saved: vogel_spiral.png")

# Plot |∇ω̂|² for each configuration
fig3, axes3 = plt.subplots(2, 2, figsize=(12, 10))

for ax, (name, data) in zip(axes3.flat, results.items()):
    grad_sq = data['grad_sq']
    
    # Take middle z-slice
    z_mid = N // 2
    grad_slice = grad_sq[:, :, z_mid]
    
    # Clip for visualization
    vmax = np.percentile(grad_slice[~np.isnan(grad_slice)], 95)
    
    im = ax.imshow(np.clip(grad_slice.T, 0, vmax), origin='lower', cmap='hot',
                   extent=[-L, L, -L, L])
    ax.set_title(f"{name}\n|∇ω̂|² (directional roughness)")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    plt.colorbar(im, ax=ax, fraction=0.046)

plt.tight_layout()
plt.savefig('/Users/vfssantos/Documents/Research/Essays/golden_slice/The_Golden_Selection/Appendices/B_calculations/51_golden_vortex/direction_roughness.png', dpi=150)
print("  Saved: direction_roughness.png")

plt.close('all')

# =============================================================================
# PART 6: Summary
# =============================================================================

print()
print("=" * 60)
print("SUMMARY: GOLDEN DIRECTION HYPOTHESIS TEST")
print("=" * 60)
print()
print("The hypothesis predicts:")
print("  κ_GST = ∫|∇ω̂|² measures 'directional roughness'")
print("  Lower κ_GST → smoother direction field → better for regularity")
print("  Golden Angle packing should minimize κ_GST")
print()
print("Results:")
print(f"  Gaussian Tube:  κ_GST = {results['Gaussian Tube']['kappa_GST']:.4f}")
print(f"  Golden (Vogel): κ_GST = {results['Golden (Vogel)']['kappa_GST']:.4f}")
print(f"  Hexagonal:      κ_GST = {results['Hexagonal']['kappa_GST']:.4f}")
print(f"  Random:         κ_GST = {results['Random']['kappa_GST']:.4f}")
print()

# Verdict
if results['Golden (Vogel)']['kappa_GST'] < results['Random']['kappa_GST']:
    print("✓ HYPOTHESIS SUPPORTED: Golden packing has lower directional roughness")
    print("  than random arrangement")
else:
    print("✗ HYPOTHESIS NOT SUPPORTED in this simple test")

print()
print("Note: This is a simplified static test. A full validation would require:")
print("  1. Time evolution under Navier-Stokes")
print("  2. Testing stability against perturbations")
print("  3. Higher resolution simulations")
print("  4. Comparison with known blowup scenarios")

