"""
Spectral Roughness Analysis of Vortex Configurations
=====================================================

Computes the Jacobian matrix of point vortex interactions and analyzes
the eigenvalue spectrum to measure "Schur-Roughness."

Key prediction: Golden (Vogel) will have LOWER roughness than Hexagonal.
"""

import numpy as np

PHI = (1 + np.sqrt(5)) / 2
GOLDEN_ANGLE = np.pi * (3 - np.sqrt(5))  # ≈ 137.5°

print("=" * 70)
print("SPECTRAL ROUGHNESS ANALYSIS: Golden vs Hexagonal")
print("=" * 70)
print()

# =============================================================================
# Point generation
# =============================================================================

def generate_golden_points(N):
    """Vogel spiral (Golden angle packing)."""
    points = []
    for i in range(N):
        r = np.sqrt(i / N)  # Uniform density
        theta = i * GOLDEN_ANGLE
        points.append([r * np.cos(theta), r * np.sin(theta)])
    return np.array(points)

def generate_hexagonal_points(N):
    """Hexagonal lattice within unit circle."""
    points = []
    # Estimate lattice constant to fit N points in unit circle
    layers = int(np.sqrt(N / 3)) + 1
    a = 0.9 / layers
    
    for q in range(-layers, layers + 1):
        for r_hex in range(-layers, layers + 1):
            x = a * (3/2 * q)
            y = a * (np.sqrt(3)/2 * q + np.sqrt(3) * r_hex)
            if x**2 + y**2 < 0.95:
                points.append([x, y])
    
    points = np.array(points)
    # Truncate to exactly N
    if len(points) > N:
        # Take closest N to center
        dists = np.sum(points**2, axis=1)
        idx = np.argsort(dists)[:N]
        points = points[idx]
    elif len(points) < N:
        print(f"Warning: Only generated {len(points)} hexagonal points")
    
    return points

def generate_random_points(N, seed=42):
    """Random points in unit circle."""
    np.random.seed(seed)
    points = []
    while len(points) < N:
        x, y = 2 * np.random.random(2) - 1
        if x**2 + y**2 < 0.95:
            points.append([x, y])
    return np.array(points[:N])

# =============================================================================
# Jacobian computation (Biot-Savart law for 2D point vortices)
# =============================================================================

def compute_jacobian(points):
    """
    Computes the 2N x 2N Jacobian matrix of the velocity field induced 
    by point vortices with unit circulation.
    
    The velocity induced at point i by all other vortices:
    u_i = -1/(2π) * Σ (y_i - y_j) / r_ij²
    v_i =  1/(2π) * Σ (x_i - x_j) / r_ij²
    
    The Jacobian J has blocks:
    J[i,j]     = ∂u_i/∂x_j
    J[i,N+j]   = ∂u_i/∂y_j
    J[N+i,j]   = ∂v_i/∂x_j  
    J[N+i,N+j] = ∂v_i/∂y_j
    """
    N = len(points)
    J = np.zeros((2*N, 2*N))
    x = points[:, 0]
    y = points[:, 1]
    
    const = 1.0 / (2 * np.pi)
    
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            r2 = dx**2 + dy**2
            
            if r2 < 1e-10:  # Avoid singularity
                continue
                
            r4 = r2**2
            
            # ∂u_i/∂x_j (how x_j affects u_i)
            J_xx = -const * (-2 * dy * dx) / r4
            # ∂u_i/∂y_j
            J_xy = -const * (r2 - 2*dy**2) / r4
            
            # ∂v_i/∂x_j
            J_yx = const * (r2 - 2*dx**2) / r4
            # ∂v_i/∂y_j
            J_yy = const * (-2 * dx * dy) / r4
            
            # Off-diagonal blocks (interaction j → i)
            J[i, j] = J_xx
            J[i, N+j] = J_xy
            J[N+i, j] = J_yx
            J[N+i, N+j] = J_yy
            
            # Diagonal blocks (self terms - conservation)
            J[i, i] -= J_xx
            J[i, N+i] -= J_xy
            J[N+i, i] -= J_yx
            J[N+i, N+i] -= J_yy
    
    return J

# =============================================================================
# Spectral analysis
# =============================================================================

def analyze_spectrum(points, name):
    """Compute Jacobian eigenvalues and extract metrics."""
    J = compute_jacobian(points)
    eigs = np.linalg.eigvals(J)
    
    N = len(points)
    
    # Metrics
    # 1. Spectral Radius (Max growth rate)
    radius = np.max(np.abs(eigs))
    
    # 2. Schur-Roughness (normalized sum of squared eigenvalues)
    roughness = np.sum(np.abs(eigs)**2) / (N**2)
    
    # 3. Spectral variance (how spread out the eigenvalues are)
    variance = np.var(np.abs(eigs))
    
    # 4. Max real part (max exponential growth)
    max_real = np.max(np.real(eigs))
    
    # 5. Distribution in complex plane
    real_spread = np.std(np.real(eigs))
    imag_spread = np.std(np.imag(eigs))
    isotropy = min(real_spread, imag_spread) / max(real_spread, imag_spread) if max(real_spread, imag_spread) > 0 else 1
    
    print(f"{name} (N={N}):")
    print(f"  Schur-Roughness κ:    {roughness:.6f}")
    print(f"  Spectral Radius ρ:    {radius:.4f}")
    print(f"  Max Real Part:        {max_real:.4f}")
    print(f"  Spectral Variance:    {variance:.4f}")
    print(f"  Isotropy (0-1):       {isotropy:.4f}")
    
    return {
        'eigenvalues': eigs,
        'roughness': roughness,
        'radius': radius,
        'max_real': max_real,
        'variance': variance,
        'isotropy': isotropy
    }

# =============================================================================
# Main execution
# =============================================================================

print("Generating point configurations...")
print()

# Test multiple sizes
for N in [50, 100, 150, 200]:
    print("-" * 70)
    print(f"N = {N} vortices")
    print("-" * 70)
    
    # Generate points
    pts_golden = generate_golden_points(N)
    pts_hex = generate_hexagonal_points(N)
    pts_random = generate_random_points(N)
    
    # Analyze
    res_golden = analyze_spectrum(pts_golden, "Golden")
    print()
    res_hex = analyze_spectrum(pts_hex, "Hexagonal")
    print()
    res_random = analyze_spectrum(pts_random, "Random")
    print()
    
    # Compare
    improvement = res_hex['roughness'] / res_golden['roughness']
    print(f"COMPARISON:")
    print(f"  Improvement Factor (Hex/Golden): {improvement:.2f}x")
    
    if res_golden['roughness'] < res_hex['roughness']:
        print(f"  ✓ Golden has LOWER roughness than Hexagonal")
    else:
        print(f"  ✗ Golden has higher roughness than Hexagonal")
    
    if res_golden['isotropy'] > res_hex['isotropy']:
        print(f"  ✓ Golden is MORE isotropic ({res_golden['isotropy']:.3f} vs {res_hex['isotropy']:.3f})")
    
    print()

# =============================================================================
# Final summary
# =============================================================================

print("=" * 70)
print("FINAL SUMMARY")
print("=" * 70)
print()

# Use N=150 for final comparison
N_final = 150
pts_golden = generate_golden_points(N_final)
pts_hex = generate_hexagonal_points(N_final)

res_golden = analyze_spectrum(pts_golden, "Golden")
print()
res_hex = analyze_spectrum(pts_hex, "Hexagonal")
print()

print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print()

improvement = res_hex['roughness'] / res_golden['roughness']
radius_improvement = res_hex['radius'] / res_golden['radius']

print(f"Roughness Improvement:  {improvement:.2f}x (Golden is {improvement:.2f}x smoother)")
print(f"Radius Improvement:     {radius_improvement:.2f}x (Golden has {radius_improvement:.2f}x smaller max eigenvalue)")
print()

if improvement > 1.2:
    print("✓ STRONG SUPPORT for Golden Direction Hypothesis")
    print("  The Golden ratio geometry minimizes spectral roughness")
    print("  This prevents rapid instability growth → protects from singularity")
elif improvement > 1.0:
    print("✓ MODERATE SUPPORT for Golden Direction Hypothesis")
    print("  Golden has lower roughness, but effect is modest")
else:
    print("✗ Results do not support hypothesis")
    print("  Further analysis needed")

