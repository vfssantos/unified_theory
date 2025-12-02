#!/usr/bin/env python3
"""
Koide Mass Formula Verification

Verifies the mass mechanism from IV.5:
- Q = 2/3 from A₂ cone condition
- θ₀ = Q/3 = 2/9 radians
- Mass ratios for charged leptons
- φ² constraint for neutrinos
"""

import math

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio

# ============================================================
# Part 1: Charged Lepton Masses
# ============================================================

print("=" * 60)
print("CHARGED LEPTON MASS VERIFICATION")
print("=" * 60)

# Derived parameters
Q = 2/3                    # From A₂ cone condition
theta_0 = Q / 3            # θ₀ = Q/3 identity (2/9 rad)
epsilon_ch = math.sqrt(2)  # From D₆ root length

print(f"\nDerived parameters:")
print(f"  Q (Koide parameter) = {Q:.8f}")
print(f"  θ₀ (phase)          = {theta_0:.8f} rad = {math.degrees(theta_0):.4f}°")
print(f"  ε (amplitude)       = {epsilon_ch:.8f}")

# Koide T-values
def T_koide(n, theta_0, epsilon):
    """Koide T-value: T = 1 + ε cos(θ₀ + 2πn/3)"""
    return 1 + epsilon * math.cos(theta_0 + 2*math.pi*n/3)

# Assignment: n=0 → τ, n=1 → e, n=2 → μ
T_tau = T_koide(0, theta_0, epsilon_ch)
T_e = T_koide(1, theta_0, epsilon_ch)
T_mu = T_koide(2, theta_0, epsilon_ch)

print(f"\nT-values (√m ∝ T):")
print(f"  T_τ = {T_tau:.6f}")
print(f"  T_μ = {T_mu:.6f}")
print(f"  T_e = {T_e:.6f}")

# Mass ratios (m ∝ T²)
ratio_mu_e = (T_mu / T_e)**2
ratio_tau_e = (T_tau / T_e)**2
ratio_tau_mu = (T_tau / T_mu)**2

# Observed values
obs_mu_e = 206.7683
obs_tau_e = 3477.2283
obs_tau_mu = 16.818

print(f"\nMass ratios:")
print(f"  μ/e:  predicted = {ratio_mu_e:.4f}, observed = {obs_mu_e:.4f}, error = {abs(ratio_mu_e - obs_mu_e)/obs_mu_e*100:.4f}%")
print(f"  τ/e:  predicted = {ratio_tau_e:.4f}, observed = {obs_tau_e:.4f}, error = {abs(ratio_tau_e - obs_tau_e)/obs_tau_e*100:.4f}%")
print(f"  τ/μ:  predicted = {ratio_tau_mu:.4f}, observed = {obs_tau_mu:.4f}, error = {abs(ratio_tau_mu - obs_tau_mu)/obs_tau_mu*100:.4f}%")

# ============================================================
# Part 2: Singularity Analysis
# ============================================================

print("\n" + "=" * 60)
print("SINGULARITY MECHANISM")
print("=" * 60)

# Singularity at T = 0: θ = arccos(-1/ε)
theta_sing = math.acos(-1/epsilon_ch)
theta_sing_deg = math.degrees(theta_sing)

print(f"\nSingularity location (T = 0):")
print(f"  θ_sing = arccos(-1/√2) = {theta_sing:.6f} rad = {theta_sing_deg:.4f}°")

# Phase positions for each particle
phases = {
    'τ': math.degrees(theta_0),
    'e': math.degrees(theta_0 + 2*math.pi/3),
    'μ': math.degrees(theta_0 + 4*math.pi/3)
}

print(f"\nParticle phases and distances from singularity:")
for particle, phase in phases.items():
    # Normalize phase to 0-360
    phase_norm = phase % 360
    distance = abs(phase_norm - theta_sing_deg)
    if distance > 180:
        distance = 360 - distance
    print(f"  {particle}: phase = {phase_norm:.2f}°, distance from 135° = {distance:.2f}°")

# ============================================================
# Part 3: Q = 2/3 Verification
# ============================================================

print("\n" + "=" * 60)
print("Q = 2/3 FROM CONE ANGLE")
print("=" * 60)

# Observed masses (MeV)
m_e = 0.51099895
m_mu = 105.6583755
m_tau = 1776.86

# Compute Q from masses
Q_obs = (m_e + m_mu + m_tau) / (math.sqrt(m_e) + math.sqrt(m_mu) + math.sqrt(m_tau))**2

print(f"\nQ from observed masses:")
print(f"  Q_obs = {Q_obs:.8f}")
print(f"  Q_theory (2/3) = {2/3:.8f}")
print(f"  Error = {abs(Q_obs - 2/3)/(2/3)*100:.4f}%")

# Verify Q = 1/(3 cos²α) with α = 45°
alpha = math.pi/4  # 45 degrees
Q_from_angle = 1 / (3 * math.cos(alpha)**2)

print(f"\nQ from cone angle (α = 45°):")
print(f"  Q = 1/(3 cos²45°) = 1/(3 × 0.5) = {Q_from_angle:.8f}")

# Compute cone angle from Q
alpha_from_Q = math.acos(1/math.sqrt(3*Q_obs))
print(f"\nCone angle from observed Q:")
print(f"  α = {math.degrees(alpha_from_Q):.4f}° (expected: 45.00°)")

# ============================================================
# Part 4: φ² Constraint (Neutrinos)
# ============================================================

print("\n" + "=" * 60)
print("φ² CONSTRAINT FOR NEUTRINOS")
print("=" * 60)

# Charged lepton amplitude
eps_ch_sq = 2  # ε²_ch = 2

# φ² constraint: ε²_ch + ε²_ν = φ²
eps_nu_sq = PHI**2 - eps_ch_sq  # Should be 1/φ

print(f"\nφ² constraint:")
print(f"  φ² = {PHI**2:.8f}")
print(f"  ε²_ch = {eps_ch_sq:.8f}")
print(f"  ε²_ν = φ² - 2 = {eps_nu_sq:.8f}")
print(f"  1/φ = {1/PHI:.8f}")
print(f"  Match: {abs(eps_nu_sq - 1/PHI) < 1e-10}")

epsilon_nu = math.sqrt(eps_nu_sq)
print(f"\n  ε_ν = 1/√φ = {epsilon_nu:.8f}")

# Verify identity: φ² - 2 = 1/φ
# Using φ² = φ + 1: φ² - 2 = φ + 1 - 2 = φ - 1 = 1/φ
print(f"\nIdentity verification:")
print(f"  φ² - 2 = {PHI**2 - 2:.8f}")
print(f"  φ - 1 = {PHI - 1:.8f}")
print(f"  1/φ = {1/PHI:.8f}")
print(f"  All equal: {abs(PHI**2 - 2 - (PHI - 1)) < 1e-10 and abs(PHI - 1 - 1/PHI) < 1e-10}")

# ============================================================
# Part 5: Neutrino Mass Ratios
# ============================================================

print("\n" + "=" * 60)
print("NEUTRINO MASS RATIOS")
print("=" * 60)

# Same phase, different amplitude
T_nu = [T_koide(n, theta_0, epsilon_nu) for n in range(3)]

print(f"\nNeutrino T-values (ε = 1/√φ = {epsilon_nu:.6f}):")
for n, T in enumerate(T_nu):
    print(f"  T_{n} = {T:.6f}")

# Check all positive
all_positive = all(T > 0 for T in T_nu)
print(f"\nAll T > 0: {all_positive}")

# Mass-squared differences (m ∝ T⁴ for √m ∝ T²)
# Actually m ∝ T² since √m ∝ T
T_sorted = sorted(T_nu)
m_ratios = [T**2 for T in T_sorted]  # Relative masses

# Δm² ratios
# Δm²₂₁ ∝ m₂² - m₁²
# Δm²₃₁ ∝ m₃² - m₁²
dm_21 = T_sorted[1]**4 - T_sorted[0]**4
dm_31 = T_sorted[2]**4 - T_sorted[0]**4
ratio_dm = dm_31 / dm_21

print(f"\nNeutrino Δm² ratio:")
print(f"  Δm²₃₁/Δm²₂₁ predicted = {ratio_dm:.2f}")
print(f"  Δm²₃₁/Δm²₂₁ observed  = 32.6")
print(f"  Error = {abs(ratio_dm - 32.6)/32.6*100:.1f}%")

# ============================================================
# Part 6: Summary
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
DERIVED PARAMETERS (no free parameters!):
  Q = 2/3           ← A₂ cone condition (45°)
  θ₀ = 2/9 rad      ← θ₀ = Q/3 identity
  ε_ch = √2         ← D₆ root length
  ε_ν = 1/√φ        ← φ² constraint spillover

VERIFIED PREDICTIONS:
  μ/e ratio:        0.001% error
  τ/e ratio:        0.007% error
  Δm²₃₁/Δm²₂₁:      ~0.2% error

KEY MECHANISM:
  The electron sits 2.3° from the zero-mass singularity at 135°.
  This geometric proximity creates the 3477× hierarchy naturally.
""")

