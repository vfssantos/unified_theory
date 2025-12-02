#!/usr/bin/env python3
"""
Verification: THEOREM IV.3.1 (Fermions from Spinors)

This script verifies that:
1. The ω₅ spinor orbit of D₆ contains exactly 32 weights
2. The quantum number formulas produce exact SM charges
3. The charge spectrum is Q ∈ {0, ±1, ±2/3, ±1/3}
4. The ×2 factor is necessary for SM charge quantization

Expected output:
- 32 spinor weights with even parity
- All 8 SM particle types found with correct (I₃, Y, Q)
- Charge census matches 1 generation + antiparticles

Requirements: Python 3 standard library only
"""

from itertools import product
from fractions import Fraction
import math

# ============================================================
# CONSTANTS
# ============================================================
SQRT5 = math.sqrt(5)
PHI = (1.0 + SQRT5) / 2.0
TOLERANCE = 1e-10

def isclose(a, b, tol=TOLERANCE):
    """Check if two floats are approximately equal."""
    return abs(a - b) < tol

# ============================================================
# QUANTUM NUMBER FORMULAS
# ============================================================

def compute_quantum_numbers(w, y_scale=2):
    """
    Compute (I₃, Y, Q) from spinor weight w = (w₁, w₂, w₃, w₄, w₅, w₆).
    
    Formulas:
        I₃ = (w₄ - w₅) / 2
        Y  = y_scale × [(w₁+w₂+w₃)/3 - (w₄+w₅)/2]
        Q  = I₃ + Y/2
    
    Parameters:
        w: 6-tuple of weight components (each ±½)
        y_scale: hypercharge scaling factor (default 2 for SM)
    
    Returns:
        (I₃, Y, Q) tuple
    """
    I3 = (w[3] - w[4]) / 2
    Y = y_scale * ((w[0] + w[1] + w[2]) / 3 - (w[3] + w[4]) / 2)
    Q = I3 + Y / 2
    return I3, Y, Q

# ============================================================
# SPINOR WEIGHT GENERATION
# ============================================================

def generate_omega5_spinors():
    """
    Generate all 32 weights in the ω₅ spinor orbit of D₆.
    
    Definition: ω₅ = ½(±1, ±1, ±1, ±1, ±1, ±1) with even parity
    (even number of minus signs: 0, 2, 4, or 6)
    
    Returns:
        List of 32 weight tuples
    """
    spinors = []
    for signs in product([-0.5, 0.5], repeat=6):
        minus_count = sum(1 for s in signs if s < 0)
        if minus_count % 2 == 0:  # even parity
            spinors.append(signs)
    return spinors

# ============================================================
# SM PARTICLE DEFINITIONS
# ============================================================

# Expected quantum numbers for SM particles (one generation)
SM_PARTICLES = {
    # Left-handed doublets
    'e_L':   {'I3': -0.5, 'Y': -1,    'Q': -1},
    'nu_L':  {'I3': +0.5, 'Y': -1,    'Q':  0},
    'u_L':   {'I3': +0.5, 'Y': +1/3,  'Q': +2/3},  # ×3 colors
    'd_L':   {'I3': -0.5, 'Y': +1/3,  'Q': -1/3},  # ×3 colors
    # Right-handed singlets
    'e_R':   {'I3':  0,   'Y': -2,    'Q': -1},
    'nu_R':  {'I3':  0,   'Y':  0,    'Q':  0},
    'u_R':   {'I3':  0,   'Y': +4/3,  'Q': +2/3},  # ×3 colors
    'd_R':   {'I3':  0,   'Y': -2/3,  'Q': -1/3},  # ×3 colors
}

# Expected multiplicities (including color)
EXPECTED_MULTIPLICITIES = {
    'e_L': 1, 'nu_L': 1, 'e_R': 1, 'nu_R': 2,  # leptons (nu_R has 2 weights)
    'u_L': 3, 'd_L': 3, 'u_R': 3, 'd_R': 3,    # quarks ×3 colors
}

# ============================================================
# VERIFICATION FUNCTIONS
# ============================================================

def verify_spinor_count(spinors):
    """Verify ω₅ has exactly 32 weights."""
    count = len(spinors)
    expected = 32
    passed = (count == expected)
    
    print(f"  Count: {count} (expected {expected})")
    print(f"  Binomial: C(6,0)+C(6,2)+C(6,4)+C(6,6) = 1+15+15+1 = 32")
    
    return passed

def verify_squared_lengths(spinors):
    """Verify all spinor weights have |v|² = 3/2."""
    expected_len_sq = 1.5
    all_correct = True
    
    for w in spinors:
        len_sq = sum(x**2 for x in w)
        if not isclose(len_sq, expected_len_sq):
            print(f"  ERROR: Weight {w} has |v|² = {len_sq}")
            all_correct = False
    
    print(f"  All |v|² = 3/2: {all_correct}")
    return all_correct

def verify_sm_charges(spinors):
    """Verify all SM particle types are found with correct quantum numbers."""
    print("\n  Searching for SM particles:")
    
    all_found = True
    found_counts = {name: 0 for name in SM_PARTICLES}
    
    for w in spinors:
        I3, Y, Q = compute_quantum_numbers(w)
        
        for name, expected in SM_PARTICLES.items():
            if (isclose(I3, expected['I3']) and
                isclose(Y, expected['Y']) and
                isclose(Q, expected['Q'])):
                found_counts[name] += 1
    
    for name, expected in SM_PARTICLES.items():
        expected_count = EXPECTED_MULTIPLICITIES[name]
        actual = found_counts[name]
        status = "✓" if actual == expected_count else "✗"
        print(f"    {name:6s}: found {actual} (expected {expected_count}) {status}")
        if actual != expected_count:
            all_found = False
    
    return all_found

def verify_charge_spectrum(spinors):
    """Verify the charge spectrum is exactly SM."""
    charge_counts = {}
    
    for w in spinors:
        _, _, Q = compute_quantum_numbers(w)
        Q_frac = Fraction(Q).limit_denominator(10)
        Q_key = float(Q_frac)
        charge_counts[Q_key] = charge_counts.get(Q_key, 0) + 1
    
    print("\n  Charge spectrum:")
    expected_charges = {-1: 2, -2/3: 6, -1/3: 6, 0: 4, 1/3: 6, 2/3: 6, 1: 2}
    
    all_match = True
    for Q in sorted(charge_counts.keys()):
        count = charge_counts[Q]
        exp = expected_charges.get(Q, 0)
        status = "✓" if count == exp else "✗"
        Q_frac = Fraction(Q).limit_denominator(10)
        print(f"    Q = {Q_frac:>5}: {count:2d} weights (expected {exp}) {status}")
        if count != exp:
            all_match = False
    
    total = sum(charge_counts.values())
    print(f"    Total: {total} (expected 32)")
    
    return all_match and total == 32

def verify_y_scale_necessity(spinors):
    """Verify that y_scale=2 is necessary for SM charge quantization."""
    print("\n  Testing hypercharge scaling:")
    
    # With y_scale=1 (no scaling)
    charges_scale1 = set()
    for w in spinors:
        _, _, Q = compute_quantum_numbers(w, y_scale=1)
        charges_scale1.add(round(Q, 6))
    
    # With y_scale=2 (SM scaling)
    charges_scale2 = set()
    for w in spinors:
        _, _, Q = compute_quantum_numbers(w, y_scale=2)
        charges_scale2.add(round(Q, 6))
    
    sm_charges = [-1, -2/3, -1/3, 0, 1/3, 2/3, 1]
    
    print(f"    y_scale=1: Q ∈ {{{', '.join(f'{q:.3f}' for q in sorted(charges_scale1))}}}")
    print(f"    y_scale=2: Q ∈ {{{', '.join(f'{q:.3f}' for q in sorted(charges_scale2))}}}")
    print(f"    SM expected: Q ∈ {{-1, -2/3, -1/3, 0, +1/3, +2/3, +1}}")
    
    # Check if scale=2 gives exactly SM charges (using tolerance)
    scale2_correct_count = len(charges_scale2) == len(sm_charges)
    scale2_matches = scale2_correct_count and all(
        any(isclose(q, sm_q, tol=1e-5) for sm_q in sm_charges)
        for q in charges_scale2
    )
    
    # Also check scale=1 gives MORE charges (non-SM)
    scale1_non_sm = len(charges_scale1) > len(sm_charges)
    
    print(f"    y_scale=2 gives exactly 7 SM charges: {scale2_matches}")
    print(f"    y_scale=1 gives {len(charges_scale1)} charges (non-SM): {scale1_non_sm}")
    
    return scale2_matches and scale1_non_sm

def verify_explicit_weights():
    """Verify the explicit weights given in the paper."""
    print("\n  Verifying explicit weights from paper:")
    
    # Weights from Table IV.3.1
    explicit_weights = [
        ((-0.5, -0.5, -0.5, -0.5, +0.5, +0.5), 'e_L',  (-0.5, -1, -1)),
        ((-0.5, -0.5, -0.5, +0.5, -0.5, +0.5), 'nu_L', (+0.5, -1, 0)),
        ((+0.5, +0.5, -0.5, +0.5, -0.5, +0.5), 'u_L',  (+0.5, +1/3, +2/3)),
        ((+0.5, +0.5, -0.5, -0.5, +0.5, +0.5), 'd_L',  (-0.5, +1/3, -1/3)),
        ((-0.5, -0.5, -0.5, +0.5, +0.5, -0.5), 'e_R',  (0, -2, -1)),
        ((+0.5, +0.5, +0.5, +0.5, +0.5, +0.5), 'nu_R', (0, 0, 0)),
        ((+0.5, +0.5, -0.5, -0.5, -0.5, -0.5), 'u_R',  (0, +4/3, +2/3)),
        ((+0.5, +0.5, -0.5, +0.5, +0.5, -0.5), 'd_R',  (0, -2/3, -1/3)),
    ]
    
    all_correct = True
    for weight, name, (exp_I3, exp_Y, exp_Q) in explicit_weights:
        I3, Y, Q = compute_quantum_numbers(weight)
        match = (isclose(I3, exp_I3) and
                 isclose(Y, exp_Y) and
                 isclose(Q, exp_Q))
        
        status = "✓" if match else "✗"
        print(f"    {name:6s}: I₃={I3:+.2f}, Y={Y:+5.2f}, Q={Q:+5.2f} {status}")
        
        if not match:
            print(f"           Expected: I₃={exp_I3:+.2f}, Y={exp_Y:+5.2f}, Q={exp_Q:+5.2f}")
            all_correct = False
        
        # Also verify parity (even number of minus signs)
        minus_count = sum(1 for x in weight if x < 0)
        if minus_count % 2 != 0:
            print(f"           ERROR: Odd parity ({minus_count} minus signs)")
            all_correct = False
    
    return all_correct

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("Verification: THEOREM IV.3.1 (Fermions from Spinors)")
    print("=" * 60)
    
    results = []
    
    # Generate spinor weights
    print("\n[1] Generating ω₅ spinor weights...")
    spinors = generate_omega5_spinors()
    results.append(("Spinor count = 32", verify_spinor_count(spinors)))
    
    # Verify squared lengths
    print("\n[2] Verifying squared lengths...")
    results.append(("All |v|² = 3/2", verify_squared_lengths(spinors)))
    
    # Verify SM particle charges
    print("\n[3] Verifying SM particle quantum numbers...")
    results.append(("SM charges found", verify_sm_charges(spinors)))
    
    # Verify charge spectrum
    print("\n[4] Verifying charge spectrum...")
    results.append(("Charge spectrum = SM", verify_charge_spectrum(spinors)))
    
    # Verify y_scale necessity
    print("\n[5] Verifying ×2 factor necessity...")
    results.append(("×2 gives SM charges", verify_y_scale_necessity(spinors)))
    
    # Verify explicit weights from paper
    print("\n[6] Verifying explicit weights from paper...")
    results.append(("Explicit weights correct", verify_explicit_weights()))
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "PASSED" if passed else "FAILED"
        print(f"  {name}: {status}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("ALL VERIFICATIONS PASSED ✓")
    else:
        print("SOME VERIFICATIONS FAILED ✗")
    print("=" * 60)
    
    return all_passed

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
