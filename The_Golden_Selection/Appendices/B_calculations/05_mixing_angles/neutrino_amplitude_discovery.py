#!/usr/bin/env python3
"""
Neutrino Amplitude Discovery Script
====================================

This script validates and discovers the correct Koide parameters for neutrinos.

Key Finding: ε = 1/√φ at θ = 2/9 rad gives Δm²₃₁/Δm²₂₁ ≈ 32.6

Author: Golden Selection Project
Date: 2024-11
"""

import math

# Constants
phi = (1 + math.sqrt(5)) / 2  # Golden ratio ≈ 1.618


def koide_masses(theta_rad, epsilon):
    """
    Calculate Koide mass terms T_i = 1 + ε*cos(θ + 2πi/3)
    
    Standard Koide: √m = M₀ × T, so m = M₀² × T²
    """
    T_vals = []
    for i in range(3):
        phase = theta_rad + 2 * math.pi * i / 3
        T = 1 + epsilon * math.cos(phase)
        T_vals.append(T)
    return T_vals


def mass_ratio(T_vals):
    """
    Calculate Δm²₃₁/Δm²₂₁ using CORRECT formula.
    
    Since m = M₀² × T², we have m² = M₀⁴ × T⁴
    Therefore Δm² = M₀⁴ × (T⁴_i - T⁴_j)
    
    The ratio is independent of M₀.
    """
    T4_vals = [t**4 for t in T_vals]
    T4_sorted = sorted(T4_vals)
    
    dm21 = T4_sorted[1] - T4_sorted[0]
    dm31 = T4_sorted[2] - T4_sorted[0]
    
    if dm21 > 1e-12:
        return dm31 / dm21
    return float('inf')


def koide_Q(T_vals):
    """Calculate Koide Q parameter."""
    m_vals = [t**2 for t in T_vals]
    sqrt_m = [math.sqrt(m) for m in m_vals]
    return sum(m_vals) / sum(sqrt_m)**2


def search_epsilon_at_theta(theta_rad, target_ratio=32.6, eps_range=(0.01, 1.5)):
    """Find epsilon that gives target ratio at given theta."""
    best_eps = 0
    best_diff = float('inf')
    best_ratio = 0
    
    for eps_x1000 in range(int(eps_range[0]*1000), int(eps_range[1]*1000)):
        eps = eps_x1000 / 1000
        T_vals = koide_masses(theta_rad, eps)
        
        # Skip if any T is negative
        if any(t <= 0 for t in T_vals):
            continue
        
        ratio = mass_ratio(T_vals)
        diff = abs(ratio - target_ratio)
        
        if diff < best_diff:
            best_diff = diff
            best_eps = eps
            best_ratio = ratio
    
    return best_eps, best_ratio


def search_2d(target_ratio=32.6):
    """Search (θ, ε) space for solutions."""
    solutions = []
    
    for theta_deg in range(0, 60):
        for eps_x100 in range(1, 150):
            eps = eps_x100 / 100
            theta_rad = math.radians(theta_deg)
            
            T_vals = koide_masses(theta_rad, eps)
            
            if any(t <= 0 for t in T_vals):
                continue
            
            ratio = mass_ratio(T_vals)
            
            if abs(ratio - target_ratio) < 0.5:
                solutions.append({
                    'theta_deg': theta_deg,
                    'epsilon': eps,
                    'ratio': ratio,
                    'Q': koide_Q(T_vals)
                })
    
    return solutions


def validate_discovery():
    """Validate the ε = 1/√φ discovery."""
    print("=" * 70)
    print("NEUTRINO AMPLITUDE DISCOVERY - VALIDATION")
    print("=" * 70)
    print()
    
    # The discovery
    theta = 2/9  # radians (Brannen phase)
    eps_nu = 1/math.sqrt(phi)
    eps_ch = math.sqrt(2)
    
    print("PARAMETERS:")
    print(f"  Charged leptons: θ = 2/9 rad = {math.degrees(theta):.2f}°, ε = √2 = {eps_ch:.4f}")
    print(f"  Neutrinos:       θ = 2/9 rad = {math.degrees(theta):.2f}°, ε = 1/√φ = {eps_nu:.4f}")
    print()
    
    # Calculate neutrino masses
    T_vals = koide_masses(theta, eps_nu)
    
    print("NEUTRINO T VALUES:")
    for i, T in enumerate(T_vals):
        print(f"  T_{i} = {T:.4f}")
    print(f"  All T > 0: {all(t > 0 for t in T_vals)}")
    print()
    
    # Calculate ratio
    ratio = mass_ratio(T_vals)
    Q = koide_Q(T_vals)
    
    print("RESULTS:")
    print(f"  Δm²₃₁/Δm²₂₁ = {ratio:.2f} (observed: 32.6)")
    print(f"  Q parameter = {Q:.4f}")
    print()
    
    # The beautiful relationship
    print("THE BEAUTIFUL RELATIONSHIP:")
    print(f"  ε²_charged = 2")
    print(f"  ε²_neutrino = 1/φ = {1/phi:.4f}")
    print(f"  Ratio ε_ch/ε_ν = √(2φ) = {math.sqrt(2*phi):.4f}")
    print()
    
    return ratio, Q


def compare_formulas():
    """Show the difference between correct and incorrect formulas."""
    print("=" * 70)
    print("FORMULA COMPARISON")
    print("=" * 70)
    print()
    
    theta = math.radians(113.06)  # Agent's claimed angle
    eps = math.sqrt(2)
    
    T_vals = koide_masses(theta, eps)
    
    print(f"At θ = 113.06°, ε = √2:")
    print(f"  T values: {[f'{t:.4f}' for t in T_vals]}")
    print()
    
    # Incorrect formula (what agent used)
    m_vals = [t**2 for t in T_vals]
    m_sorted = sorted(m_vals)
    dm21_wrong = m_sorted[1] - m_sorted[0]
    dm31_wrong = m_sorted[2] - m_sorted[0]
    ratio_wrong = dm31_wrong / dm21_wrong
    
    print("INCORRECT FORMULA (Δm² = T² differences):")
    print(f"  Ratio = {ratio_wrong:.2f}")
    print()
    
    # Correct formula
    ratio_correct = mass_ratio(T_vals)
    
    print("CORRECT FORMULA (Δm² = T⁴ differences):")
    print(f"  Ratio = {ratio_correct:.2f}")
    print()
    
    print("The agent used the WRONG formula!")


if __name__ == "__main__":
    # Run validation
    ratio, Q = validate_discovery()
    
    print()
    compare_formulas()
    
    print()
    print("=" * 70)
    print("2D SEARCH RESULTS")
    print("=" * 70)
    print()
    
    solutions = search_2d()
    print(f"Found {len(solutions)} solutions with ratio ≈ 32.6")
    print()
    print("Best solutions (sorted by ratio accuracy):")
    for sol in sorted(solutions, key=lambda x: abs(x['ratio'] - 32.6))[:10]:
        print(f"  θ = {sol['theta_deg']}°, ε = {sol['epsilon']:.2f}, "
              f"ratio = {sol['ratio']:.2f}, Q = {sol['Q']:.3f}")

