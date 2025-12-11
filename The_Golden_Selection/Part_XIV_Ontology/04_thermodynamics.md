# IX.13–15 — Thermodynamics

---

## IX.13 — What Is Temperature?

### The Standard Answer

Temperature is:
1. **Average kinetic energy**: T ∝ ⟨E_kinetic⟩ for ideal gas
2. **Statistical quantity**: Defined via Boltzmann distribution
3. **Conjugate to entropy**: dE = TdS (thermodynamic identity)
4. **Absolute zero**: Minimum possible temperature (0 K)

### The Golden Selection Answer

> **Temperature is the rate of phason fluctuations in the quasicrystal.**

More precisely:

$$T \propto \langle(\delta\phi)^2\rangle / \tau$$

where δφ are phason displacements and τ is the correlation time.

**In plain terms**: Temperature measures how "jiggly" the internal degrees of freedom are. Hot = rapid phason flips. Cold = frozen configuration.

### The Derivation

**[OPEN]** — This requires:
1. A statistical mechanics of phason modes
2. Identification of the "thermal bath" with phason fluctuations
3. Derivation of the Boltzmann distribution from lattice dynamics

### Status

**[OPEN]** — Plausible but not derived.

### Implications

1. **Absolute zero**: The ground state with minimal phason fluctuations
2. **Thermal equilibrium**: Equipartition of energy among phason modes
3. **Heat capacity**: Related to the density of phason states

---

## IX.14 — What Is Entropy?

### The Standard Answer

Entropy is:
1. **Measure of disorder**: S = k_B ln(Ω), where Ω = number of microstates
2. **Always increases**: Second law of thermodynamics
3. **Information-theoretic**: S = -Σ p_i ln(p_i)
4. **Mysterious**: Why does it increase? (Arrow of time)

### The Golden Selection Answer

> **Entropy is the logarithm of the number of valid quasicrystal tilings consistent with macroscopic constraints.**

More precisely:

$$S = k_B \ln(\Omega_{\text{tilings}})$$

where Ω_tilings counts the distinct tilings that produce the same coarse-grained configuration.

**In plain terms**: Entropy measures **how many ways** the quasicrystal can be arranged while looking the same at large scales. High entropy = many microscopic arrangements. Low entropy = few arrangements.

### The Derivation

From [Part III.2 — Phasons]:

1. Quasicrystals have **local isomorphism** — many tilings share the same local patches
2. Phason flips connect these equivalent tilings
3. The number of equivalent tilings grows exponentially with system size
4. Entropy = log of this number

### Status

**[CONJECTURE]** — The interpretation is natural, but quantitative derivation is missing.

### Implications

1. **Second law**: Entropy increases because the system explores more tilings over time
2. **Arrow of time**: The direction of increasing tiling diversity
3. **Black hole entropy**: Might count tilings on the horizon
4. **Information**: Entropy = missing information about the microstate

---

## IX.15 — What Is Heat?

### The Standard Answer

Heat is:
1. **Energy transfer**: Due to temperature difference
2. **Disordered energy**: Unlike work (ordered energy)
3. **Flows spontaneously**: From hot to cold

### The Golden Selection Answer

> **Heat is energy transferred via phason mode excitation.**

More precisely:

Heat transfer = excitation of phason modes that propagate from hot to cold regions.

**In plain terms**: When you heat something, you're exciting its internal "jiggle modes" (phasons). These excitations spread through the lattice, carrying energy.

### The Derivation

**[OPEN]** — Requires:
1. Phason dispersion relation (how fast phasons propagate)
2. Coupling between phasons and phonons (lattice vibrations)
3. Derivation of Fourier's law from lattice dynamics

### Status

**[OPEN]** — Conceptually clear, not quantitatively derived.

### Implications

1. **Thermal conductivity**: Related to phason propagation speed
2. **Insulators vs conductors**: Different phason-phonon coupling
3. **Quantum heat**: At low T, quantum effects in phason modes

---

## Summary

| Concept | Golden Selection Definition | Status |
|---------|----------------------------|--------|
| **Temperature** | Phason fluctuation rate | [OPEN] |
| **Entropy** | Log of tiling count | [CONJECTURE] |
| **Heat** | Phason mode energy transfer | [OPEN] |

**The pattern**: Thermodynamic quantities are **statistical properties** of the quasicrystal's internal degrees of freedom (phasons). The framework is natural but underdeveloped.

---

## The Deep Connection

Thermodynamics connects to the **Axiom** itself:

> **Minimize Geometric Free Energy**: F = E_strain + λ·κ_Schur

This is a **free energy minimization** — exactly the structure of thermodynamics!

- E_strain → Energy (internal)
- κ_Schur → Entropy-like term (complexity penalty)
- λ → Temperature-like parameter

The Axiom might **be** the fundamental thermodynamic principle, with physics emerging from free energy minimization.

