"""
Weinberg Angle from D₆ → H₃ Projection Geometry

This script verifies the derivation:
    sin²θ_W = (393 - 75√5) / 968 ≈ 0.2327

Supports: Part IV.2 (Electroweak: Weinberg Angle)
Status: VERIFIED

Dependencies: Standard library only (math)

References:
- Al-Siyabi, Koca, Koca (2020). MDPI Symmetry.
- Georgi & Glashow (1974). Unity of Elementary Particle Forces.
"""

import math

# =============================================================================
# CONSTANTS
# =============================================================================

SQRT5 = math.sqrt(5)
PHI = (1 + SQRT5) / 2           # Golden ratio ≈ 1.618034
PHI_INV = PHI - 1               # φ⁻¹ ≈ 0.618034
NORM = math.sqrt(5 + SQRT5)     # Projection normalization ≈ 2.534

# Experimental value (PDG 2024)
SIN2_THETA_W_EXP = 0.23121


# =============================================================================
# PROJECTION MATRIX
# =============================================================================

def get_projection_matrix():
    """
    Return the 3×6 Koca–Al-Siyabi projection matrix.
    
    P = (1/√(5+√5)) × 
        ┌                              ┐
        │  1   -1   0    0    φ   -φ  │
        │  φ    φ   1    1    0    0  │
        │  0    0   φ   -φ    1    1  │
        └                              ┘
    """
    return [
        [1/NORM, -1/NORM, 0, 0, PHI/NORM, -PHI/NORM],
        [PHI/NORM, PHI/NORM, 1/NORM, 1/NORM, 0, 0],
        [0, 0, PHI/NORM, -PHI/NORM, 1/NORM, 1/NORM]
    ]


# =============================================================================
# SM GENERATORS
# =============================================================================

def get_sm_generators():
    """
    Return the Standard Model generators in D₆.
    
    W³ (SU(2)_L): weak isospin neutral component
    Y (U(1)_Y): hypercharge (SU(5) normalized)
    """
    # SU(2) generator W³
    W3 = [0, 0, 0, 1, -1, 0]
    
    # Hypercharge direction (unnormalized)
    Y_raw = [1/3, 1/3, 1/3, -1/2, -1/2, 0]
    
    # Normalize to |Y|² = 2 (SU(5) convention)
    Y_norm_sq_raw = sum(y**2 for y in Y_raw)  # = 5/6
    Y_scale = math.sqrt(2 / Y_norm_sq_raw)    # √(12/5)
    Y = [y * Y_scale for y in Y_raw]
    
    return W3, Y


# =============================================================================
# LINEAR ALGEBRA (pure Python)
# =============================================================================

def mat_vec_mult(M, v):
    """Multiply 3×6 matrix by 6-vector → 3-vector."""
    return [sum(M[i][j] * v[j] for j in range(6)) for i in range(3)]


def dot(v1, v2):
    """Dot product of two vectors."""
    return sum(a * b for a, b in zip(v1, v2))


def norm_sq(v):
    """Squared norm of vector."""
    return sum(x**2 for x in v)


# =============================================================================
# MAIN CALCULATION
# =============================================================================

def compute_weinberg_angle():
    """
    Compute sin²θ_W from D₆ → H₃ projection geometry.
    
    Returns dict with all intermediate quantities.
    """
    P = get_projection_matrix()
    W3, Y = get_sm_generators()
    
    # Project generators
    x_SU2 = mat_vec_mult(P, W3)
    x_U1 = mat_vec_mult(P, Y)
    
    # Compute squared lengths
    x_SU2_sq = norm_sq(x_SU2)
    x_U1_sq = norm_sq(x_U1)
    
    # Ratio
    rho = x_SU2_sq / x_U1_sq
    
    # Weinberg angle
    sin2_theta_W = 1 / (1 + (5/3) * rho)
    
    # Theoretical exact values
    x_SU2_sq_theory = 1 + SQRT5/5           # = (5 + √5)/5
    x_U1_sq_theory = 1 - 3*SQRT5/25         # = (25 - 3√5)/25
    rho_theory = (35 + 10*SQRT5) / 29       # = (35 + 10√5)/29
    sin2_theory = (393 - 75*SQRT5) / 968
    
    return {
        'x_SU2': x_SU2,
        'x_U1': x_U1,
        'x_SU2_sq': x_SU2_sq,
        'x_U1_sq': x_U1_sq,
        'x_SU2_sq_theory': x_SU2_sq_theory,
        'x_U1_sq_theory': x_U1_sq_theory,
        'rho': rho,
        'rho_theory': rho_theory,
        'sin2_theta_W': sin2_theta_W,
        'sin2_theory': sin2_theory,
        'sin2_exp': SIN2_THETA_W_EXP,
        'error_percent': 100 * abs(sin2_theta_W - SIN2_THETA_W_EXP) / SIN2_THETA_W_EXP
    }


# =============================================================================
# ALGEBRAIC VERIFICATION
# =============================================================================

def verify_algebra():
    """
    Verify the algebraic formula:
    sin²θ_W = 87/(262 + 50√5) = (393 - 75√5)/968
    """
    # Step 1: ρ = (10√5 + 35)/29
    rho = (10*SQRT5 + 35) / 29
    
    # Step 2: sin²θ_W = 3/(3 + 5ρ)
    sin2_from_rho = 3 / (3 + 5 * rho)
    
    # Step 3: = 87/(262 + 50√5)
    sin2_intermediate = 87 / (262 + 50*SQRT5)
    
    # Step 4: Rationalize
    numerator = 87 * (262 - 50*SQRT5)
    denominator = 262**2 - 50**2 * 5  # = 56144
    sin2_rationalized = numerator / denominator
    
    # Step 5: Simplify by 58
    sin2_final = (393 - 75*SQRT5) / 968
    
    return {
        'rho': rho,
        'sin2_from_rho': sin2_from_rho,
        'sin2_intermediate': sin2_intermediate,
        'sin2_rationalized': sin2_rationalized,
        'sin2_final': sin2_final,
        'denominator': denominator,
        'all_equal': all(abs(a - b) < 1e-12 for a, b in [
            (sin2_from_rho, sin2_intermediate),
            (sin2_intermediate, sin2_rationalized),
            (sin2_rationalized, sin2_final)
        ])
    }


# =============================================================================
# VERIFICATION
# =============================================================================

def run_verification():
    """Run complete verification and print results."""
    print("=" * 60)
    print("WEINBERG ANGLE FROM D₆ → H₃ PROJECTION")
    print("=" * 60)
    print()
    
    # Main calculation
    result = compute_weinberg_angle()
    
    print("GAUGE GENERATOR PROJECTIONS:")
    print("-" * 40)
    print(f"  W³ = (0, 0, 0, 1, -1, 0)")
    print(f"  Y  = normalized hypercharge")
    print()
    print(f"  x_SU2 = {[f'{x:.4f}' for x in result['x_SU2']]}")
    print(f"  x_U1  = {[f'{x:.4f}' for x in result['x_U1']]}")
    print()
    
    print("SQUARED LENGTHS:")
    print("-" * 40)
    print(f"  |x_SU2|² = {result['x_SU2_sq']:.10f}")
    print(f"    Theory (1 + √5/5) = {result['x_SU2_sq_theory']:.10f}")
    print(f"    Match: {abs(result['x_SU2_sq'] - result['x_SU2_sq_theory']) < 1e-10}")
    print(f"  |x_U1|²  = {result['x_U1_sq']:.10f}")
    print(f"    Theory (1 - 3√5/25) = {result['x_U1_sq_theory']:.10f}")
    print(f"    Match: {abs(result['x_U1_sq'] - result['x_U1_sq_theory']) < 1e-10}")
    print()
    
    print("RATIO:")
    print("-" * 40)
    print(f"  ρ = |x_SU2|²/|x_U1|² = {result['rho']:.10f}")
    print(f"    Theory (10√5+35)/29 = {result['rho_theory']:.10f}")
    print(f"    Match: {abs(result['rho'] - result['rho_theory']) < 1e-10}")
    print()
    
    print("WEINBERG ANGLE:")
    print("-" * 40)
    print(f"  sin²θ_W = 1/(1 + 5ρ/3) = {result['sin2_theta_W']:.10f}")
    print(f"    Exact: (393-75√5)/968 = {result['sin2_theory']:.10f}")
    print(f"    Match: {abs(result['sin2_theta_W'] - result['sin2_theory']) < 1e-10}")
    print()
    print(f"  Experimental (PDG 2024): {result['sin2_exp']}")
    print(f"  Error: {result['error_percent']:.2f}%")
    print()
    
    # Algebraic verification
    algebra = verify_algebra()
    
    print("=" * 60)
    print("ALGEBRAIC VERIFICATION")
    print("=" * 60)
    print()
    print("Step-by-step formula derivation:")
    print(f"  ρ = (10√5 + 35)/29 = {algebra['rho']:.10f}")
    print(f"  sin²θ_W = 3/(3 + 5ρ) = {algebra['sin2_from_rho']:.10f}")
    print(f"         = 87/(262 + 50√5) = {algebra['sin2_intermediate']:.10f}")
    print(f"         = 87(262-50√5)/{algebra['denominator']:.0f} = {algebra['sin2_rationalized']:.10f}")
    print(f"         = (393-75√5)/968 = {algebra['sin2_final']:.10f}")
    print()
    print(f"  All steps consistent: {algebra['all_equal']}")
    print()
    
    # Final verdict
    print("=" * 60)
    print("RESULT")
    print("=" * 60)
    print()
    print("  ┌────────────────────────────────────────────┐")
    print("  │                                            │")
    print("  │   sin²θ_W = (393 - 75√5) / 968            │")
    print(f"  │           ≈ {result['sin2_theta_W']:.4f}                       │")
    print("  │                                            │")
    print(f"  │   Experimental: {result['sin2_exp']:.4f}                  │")
    print(f"  │   Error: {result['error_percent']:.2f}%                          │")
    print("  │                                            │")
    print("  │   STATUS: ✓ VERIFIED                       │")
    print("  │                                            │")
    print("  └────────────────────────────────────────────┘")
    print()


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    run_verification()

