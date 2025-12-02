#!/usr/bin/env python3
"""
Mixing Matrix Verification (CKM & PMNS)
=======================================

Verifies the geometric derivation of mixing angles for both quarks and leptons.

THEORY:
  1. CKM (Quarks): Defined by E_perp rotations and Phason Tunneling
     - θ_C = arctan(φ⁻³) (Golden Axis deviation)
     - V_cb = (φ/2) * φ⁻⁶ (Pentagonal factor * suppression)
     - V_ub = V_us * V_cb * φ⁻² (Tunneling penalty)
     - δ_CP = 2π/5 (Pentagrid Berry phase)

  2. PMNS (Leptons): Defined by A₄ symmetry + Koide Perturbation
     - θ₁₃ = Q²/3 (Koide structure)
     - θ₂₃ = 45° + θ₁₃/2 (Maximal mixing perturbation)
     - θ₁₂ = 35.26° - θ₁₃/5 (TBM correction)

Usage:
    python ckm_pmns_derivation.py
"""

import math
import cmath

# ============================================================
# Constants
# ============================================================

PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
Q_KOIDE = 2/3                 # Lepton Koide parameter

# ============================================================
# CKM Matrix (Quarks)
# ============================================================

def verify_ckm():
    print("\n" + "="*60)
    print("CKM MATRIX VERIFICATION (Quarks)")
    print("="*60)

    # 1. Cabibbo Angle (V_us)
    # Theory: θ_C = 45° - arctan(1/φ) = arctan(φ⁻³)
    # Geometric origin: Angle between 'Democratic' (1,1,1) and 'Golden' (1,φ,φ²) axes
    
    theta_c_rad = math.atan(PHI**-3)
    theta_c_deg = math.degrees(theta_c_rad)
    v_us_pred = math.sin(theta_c_rad)
    v_us_obs = 0.22500  # PDG 2024
    
    print(f"\n1. Cabibbo Angle (V_us)")
    print(f"   Formula:   arctan(φ⁻³) = arctan({PHI**-3:.5f})")
    print(f"   Predicted: {theta_c_deg:.4f}°")
    print(f"   V_us pred: {v_us_pred:.5f}")
    print(f"   V_us obs:  {v_us_obs:.5f}")
    print(f"   Error:     {abs(v_us_pred - v_us_obs)/v_us_obs*100:.2f}%")

    # 2. V_cb (Heavy Quark Mixing)
    # Theory: V_cb = (φ/2) * φ⁻⁶
    # Origin: Pentagonal projection factor (φ/2) * 6th order suppression
    
    v_cb_pred = (PHI/2) * (PHI**-6)
    v_cb_obs = 0.04182
    
    print(f"\n2. V_cb (Heavy Mixing)")
    print(f"   Formula:   (φ/2) * φ⁻⁶")
    print(f"   Predicted: {v_cb_pred:.5f}")
    print(f"   Observed:  {v_cb_obs:.5f}")
    print(f"   Error:     {abs(v_cb_pred - v_cb_obs)/v_cb_obs*100:.2f}%")

    # 3. V_ub (Tunneling)
    # Theory: V_ub = V_us * V_cb * φ⁻²
    # Origin: Non-adjacent mixing requires crossing a 'Short' interval (prob φ⁻²)
    
    tunneling_factor = PHI**-2
    v_ub_pred = v_us_pred * v_cb_pred * tunneling_factor
    v_ub_obs = 0.00369
    
    print(f"\n3. V_ub (Tunneling)")
    print(f"   Formula:   V_us * V_cb * φ⁻²")
    print(f"   Factor:    φ⁻² = {tunneling_factor:.5f}")
    print(f"   Predicted: {v_ub_pred:.6f}")
    print(f"   Observed:  {v_ub_obs:.6f}")
    print(f"   Error:     {abs(v_ub_pred - v_ub_obs)/v_ub_obs*100:.2f}%")

    # 4. CP Phase
    # Theory: δ = 2π/5
    
    delta_pred_deg = 360 / 5
    delta_obs_deg = 68.8 # PDG average (approx)
    
    print(f"\n4. CP Phase")
    print(f"   Formula:   2π/5")
    print(f"   Predicted: {delta_pred_deg:.2f}°")
    print(f"   Observed:  {delta_obs_deg:.2f}°")
    print(f"   Error:     {abs(delta_pred_deg - delta_obs_deg)/delta_obs_deg*100:.2f}%")

# ============================================================
# PMNS Matrix (Leptons)
# ============================================================

def verify_pmns():
    print("\n" + "="*60)
    print("PMNS MATRIX VERIFICATION (Leptons)")
    print("="*60)
    
    # Base: Tribimaximal (TBM)
    # θ₁₂ = arcsin(1/√3) ≈ 35.26°
    # θ₂₃ = 45°
    # θ₁₃ = 0°
    
    tbm_theta12 = math.degrees(math.asin(1/math.sqrt(3)))
    
    # 1. Reactor Angle θ₁₃ (The Trigger)
    # Theory: θ₁₃ = Q²/3 radians
    # Origin: Koide parameter Q=2/3 breaks A4 symmetry
    
    theta13_rad = (Q_KOIDE**2) / 3
    theta13_deg = math.degrees(theta13_rad)
    theta13_obs = 8.54
    
    print(f"\n1. Reactor Angle θ₁₃")
    print(f"   Formula:   Q²/3 rad = (2/3)²/3 = 4/27 rad")
    print(f"   Predicted: {theta13_deg:.4f}°")
    print(f"   Observed:  {theta13_obs:.4f}°")
    print(f"   Error:     {abs(theta13_deg - theta13_obs)/theta13_obs*100:.2f}%")
    
    # 2. Atmospheric Angle θ₂₃
    # Theory: θ₂₃ = 45° + θ₁₃/2
    # Origin: Maximal mixing perturbed by half the reactor angle
    
    theta23_deg = 45 + theta13_deg/2
    theta23_obs = 49.1
    
    print(f"\n2. Atmospheric Angle θ₂₃")
    print(f"   Formula:   45° + θ₁₃/2")
    print(f"   Predicted: {theta23_deg:.4f}°")
    print(f"   Observed:  {theta23_obs:.4f}°")
    print(f"   Error:     {abs(theta23_deg - theta23_obs)/theta23_obs*100:.2f}%")
    
    # 3. Solar Angle θ₁₂
    # Theory: θ₁₂ = θ₁₂(TBM) - θ₁₃/5
    # Origin: TBM angle reduced by 1/5th of reactor angle (pentagonal scaling)
    
    theta12_deg = tbm_theta12 - theta13_deg/5
    theta12_obs = 33.41
    
    print(f"\n3. Solar Angle θ₁₂")
    print(f"   Formula:   35.26° - θ₁₃/5")
    print(f"   Predicted: {theta12_deg:.4f}°")
    print(f"   Observed:  {theta12_obs:.4f}°")
    print(f"   Error:     {abs(theta12_deg - theta12_obs)/theta12_obs*100:.2f}%")

if __name__ == "__main__":
    verify_ckm()
    verify_pmns()

