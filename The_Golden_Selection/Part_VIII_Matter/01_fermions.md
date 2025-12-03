# IV.3 — Fermions: The ω₅ Spinor Orbit

## Statement

> **THEOREM IV.3.1 (Fermions from Spinors)** [VERIFIED]:
>
> Standard Model fermions emerge from the **ω₅ spinor orbit** of D₆:
> - **32 spinor weights**: $\frac{1}{2}(\pm1, \pm1, \pm1, \pm1, \pm1, \pm1)$ with even parity
> - **Quantum numbers**: $I_3$, $Y$, $Q$ follow directly from weight components
> - **SM charges reproduced exactly**: $Q \in \{0, -1, +\frac{2}{3}, -\frac{1}{3}\}$
>
> The factor of 2 in the hypercharge formula is a **basis conversion** (spinor ±½ → SM ±1), not a free parameter.

---

## Intuition

**In plain terms**: The D₆ lattice has different types of special points — roots, weights, and spinors. Each type has a distinct physical role:

- **Roots (ω₂)**: The 60 roots connect different states → gauge bosons
- **Spinors (ω₅)**: The 32 spinor weights carry half-integer coordinates → fermions
- **Weights (ω₃)**: The 160 weights form a composite/vacuum sector

This is exactly how **SO(10) and E₆ Grand Unified Theories** organize particles:
- Fermions live in **spinor representations**
- Gauge bosons live in the **adjoint (root) representation**

D₆ inherits this structure because it's the root system of SO(12), which naturally contains SO(10) as a subgroup. The spinor-fermion correspondence is not postulated—it's inherited from standard GUT physics.

---

## Prerequisites

This section requires:

- **[THEOREM IV.1.1]**: Standard Model gauge groups in D₆ (SU(3) × SU(2) × U(1) embedding)
- **[THEOREM IV.2.1]**: Hypercharge direction and Weinberg angle geometry
- **[KNOWN]**: SO(10) spinor decomposition under SU(5)

---

## The D₆ Orbit Zoo

The D₆ lattice has several distinguished Weyl orbits, each with a physical interpretation:

| Orbit | Definition | |v|² | Count | Physical Content |
|-------|------------|------|-------|------------------|
| **ω₂ (Roots)** | $\pm e_i \pm e_j$ | 2 | 60 | **Gauge bosons** |
| **ω₃ (Weights)** | Third fundamental | 3 | 160 | Composites / Higgs |
| **ω₅ (Spinor)** | $\frac{1}{2}(\pm1)^6$, even | 3/2 | 32 | **SM Fermions** |
| **ω₆ (Spinor')** | $\frac{1}{2}(\pm1)^6$, odd | 3/2 | 32 | Anti-fermions (CPT) |

**Key point**: The spinor orbits (ω₅ and ω₆) are distinguished by **parity** — the number of minus signs. They are **CPT conjugates** of each other:
- ω₅: even number of minus signs → particles
- ω₆: odd number of minus signs → antiparticles

Together, ω₅ + ω₆ = 64 states = one complete generation (matter + antimatter).

---

## The ω₅ Spinor Orbit

### Definition

The spinor weights of D₆:

$$\omega_5 = \frac{1}{2}(\pm 1, \pm 1, \pm 1, \pm 1, \pm 1, \pm 1) \quad \text{with even parity}$$

**Even parity** means an even number of minus signs (0, 2, 4, or 6).

**Count**: $\binom{6}{0} + \binom{6}{2} + \binom{6}{4} + \binom{6}{6} = 1 + 15 + 15 + 1 = 32$

**Squared length**: Each weight has $|v|^2 = 6 \times \frac{1}{4} = \frac{3}{2}$.

### Why Spinors = Fermions

This is standard GUT physics:

1. **SO(12) contains SO(10)**: The D₆ root system is the root system of SO(12), which contains SO(10) = D₅.

2. **SO(10) spinor = one SM generation**: The 16-dimensional spinor representation of SO(10) decomposes under SU(5) as:
   $$\mathbf{16} = \mathbf{\bar{5}} \oplus \mathbf{10} \oplus \mathbf{1}$$
   This is exactly one generation of SM fermions (including right-handed neutrino).

3. **D₆ spinor = 2 × SO(10) spinor**: The 32-dimensional spinor of SO(12) restricts to $\mathbf{16} \oplus \mathbf{\overline{16}}$ under SO(10), giving particles + antiparticles.

**The takeaway**: The spinor-fermion identification is not our invention—it's the foundation of all SO(10)-based GUTs since Georgi-Glashow (1974).

---

## Quantum Number Formula

### The Embedding

From [THEOREM IV.1.1], the Standard Model is embedded in D₆ with:
- **Color SU(3)**: coordinates (1, 2, 3)
- **Weak SU(2)**: coordinates (4, 5)
- **Hypercharge U(1)**: coordinate 6 direction

### Weak Isospin

$$I_3 = \frac{w_4 - w_5}{2}$$

For spinor weights with $w_4, w_5 \in \{+\frac{1}{2}, -\frac{1}{2}\}$:
- $I_3 = +\frac{1}{2}$ when $(w_4, w_5) = (+\frac{1}{2}, -\frac{1}{2})$
- $I_3 = -\frac{1}{2}$ when $(w_4, w_5) = (-\frac{1}{2}, +\frac{1}{2})$
- $I_3 = 0$ when $w_4 = w_5$ (singlets)

### Hypercharge

$$Y_{\text{SM}} = 2 \times \left(\frac{w_1 + w_2 + w_3}{3} - \frac{w_4 + w_5}{2}\right)$$

The structure is:
- **Color contribution**: $(w_1 + w_2 + w_3)/3$ — average color charge
- **Weak contribution**: $(w_4 + w_5)/2$ — SU(2) embedding
- **Factor of 2**: basis conversion (see below)

### Electric Charge

$$Q = I_3 + \frac{Y_{\text{SM}}}{2}$$

This is the standard Gell-Mann–Nishijima formula.

---

## The ×2 Factor Explained

### The Puzzle

Why does the hypercharge formula have a factor of 2? Is this a free parameter?

### The Resolution: Basis Conversion

**No** — it's a **required basis conversion**, not a tunable parameter.

| Representation | Coordinate Range | Y(electron) |
|----------------|------------------|-------------|
| Spinor weights | $\pm\frac{1}{2}$ | $-\frac{1}{2}$ |
| SM convention | $\pm 1$ (integers) | $-1$ |

The Standard Model conventionally uses **integer hypercharges** for leptons:
- $Y(e_L) = -1$
- $Y(\nu_L) = -1$
- $Y(e_R) = -2$

But spinor weights have entries $\pm\frac{1}{2}$, which naturally produce half-integer hypercharges. The factor of 2 converts between these bases.

### Comparison with Other Normalizations

| Factor | Origin | Purpose |
|--------|--------|---------|
| **×2 (this)** | Spinor → SM basis | Representation-theoretic |
| $\sqrt{5/3}$ (SU(5) GUT) | Coupling unification | Running to GUT scale |
| $\sqrt{3/5}$ (hypercharge) | Trace normalization | Generator normalization |

These are **different** normalizations serving different purposes. The ×2 is about mapping half-integer spinor entries to integer SM conventions.

### Mathematical Necessity

The ×2 factor ensures **charge quantization** comes out correctly:
- Without ×2: $Q \in \{0, -\frac{1}{2}, +\frac{1}{3}, -\frac{1}{6}, ...\}$ — non-standard
- With ×2: $Q \in \{0, -1, +\frac{2}{3}, -\frac{1}{3}\}$ — exactly SM

**Conclusion**: The ×2 is the **unique** factor that reproduces SM charge quantization from spinor weights.

---

## SM Fermion Matching

### The Complete Table

| Weight | $I_3$ | $Y$ | $Q$ | Particle | Description |
|--------|-------|-----|-----|----------|-------------|
| $(-\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2})$ | $-\frac{1}{2}$ | $-1$ | **−1** | $e_L$ | Left electron |
| $(-\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2})$ | $+\frac{1}{2}$ | $-1$ | **0** | $\nu_L$ | Left neutrino |
| $(+\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2})$ | $+\frac{1}{2}$ | $+\frac{1}{3}$ | **+⅔** | $u_L$ | Left up quark (one color) |
| $(+\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2})$ | $-\frac{1}{2}$ | $+\frac{1}{3}$ | **−⅓** | $d_L$ | Left down quark (one color) |
| $(-\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2})$ | $0$ | $-2$ | **−1** | $e_R$ | Right electron |
| $(+\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2})$ | $0$ | $0$ | **0** | $\nu_R$ | Right neutrino |
| $(+\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2})$ | $0$ | $+\frac{4}{3}$ | **+⅔** | $u_R$ | Right up quark (one color) |
| $(+\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2})$ | $0$ | $-\frac{2}{3}$ | **−⅓** | $d_R$ | Right down quark (one color) |

**Note**: Quarks appear in 3 colors (permutations of ±½ in the first three coordinates), giving 3 weights per quark type.

### Verification

Let's verify two particles explicitly:

**Electron ($e_L$)**: Weight $w = (-\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, +\frac{1}{2}, +\frac{1}{2})$

$$I_3 = \frac{w_4 - w_5}{2} = \frac{-\frac{1}{2} - \frac{1}{2}}{2} = -\frac{1}{2} \quad ✓$$

$$Y = 2 \times \left(\frac{-\frac{1}{2} - \frac{1}{2} - \frac{1}{2}}{3} - \frac{-\frac{1}{2} + \frac{1}{2}}{2}\right) = 2 \times \left(-\frac{1}{2} - 0\right) = -1 \quad ✓$$

$$Q = I_3 + \frac{Y}{2} = -\frac{1}{2} - \frac{1}{2} = -1 \quad ✓$$

**Up quark ($u_R$)**: Weight $w = (+\frac{1}{2}, +\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, -\frac{1}{2})$

$$I_3 = \frac{-\frac{1}{2} - (-\frac{1}{2})}{2} = 0 \quad ✓$$

$$Y = 2 \times \left(\frac{+\frac{1}{2} + \frac{1}{2} - \frac{1}{2}}{3} - \frac{-\frac{1}{2} - \frac{1}{2}}{2}\right) = 2 \times \left(\frac{1}{6} + \frac{1}{2}\right) = +\frac{4}{3} \quad ✓$$

$$Q = 0 + \frac{4/3}{2} = +\frac{2}{3} \quad ✓$$

### Charge Spectrum

The full ω₅ orbit contains particles AND antiparticles:

| Charge $Q$ | Multiplicity | Particles |
|------------|--------------|-----------|
| $-1$ | 2 | $e_L$, $e_R$ |
| $-\frac{2}{3}$ | 6 | $\bar{u}_L$ (3 colors), $\bar{u}_R$ (3 colors) |
| $-\frac{1}{3}$ | 6 | $d_L$ (3 colors), $d_R$ (3 colors) |
| $0$ | 4 | $\nu_L$, $\nu_R$ (×2) |
| $+\frac{1}{3}$ | 6 | $\bar{d}_L$ (3 colors), $\bar{d}_R$ (3 colors) |
| $+\frac{2}{3}$ | 6 | $u_L$ (3 colors), $u_R$ (3 colors) |
| $+1$ | 2 | $\bar{e}_L$, $\bar{e}_R$ |
| **Total** | **32** | |

**All Standard Model charges are reproduced exactly.**

---

## One Generation = 32 States

### The Count

One generation of SM fermions contains:

| Particle Type | Weak × Color × Chirality | States |
|---------------|--------------------------|--------|
| Leptons ($e$, $\nu$) | 2 × 1 × 2 | 4 |
| Quarks ($u$, $d$) | 2 × 3 × 2 | 12 |
| **Subtotal** | | **16** |
| + Antiparticles | × 2 | **32** |

The ω₅ orbit has exactly 32 weights — matching one complete generation (particles + antiparticles).

### CPT Structure

The two spinor orbits (ω₅ and ω₆) are **CPT conjugates**:

| Orbit | Parity | Weights | Physical Content |
|-------|--------|---------|------------------|
| ω₅ | Even | 32 | 1 generation (matter + antimatter) |
| ω₆ | Odd | 32 | Same generation (CPT image) |

**Note**: ω₅ and ω₆ contain the same physical information — they're related by a sign flip (CPT). We don't get two generations from the two orbits; we get one generation described twice.

---

## The Generation Question (Preview)

### The Problem

The ω₅ spinor orbit gives **exactly one generation** of SM fermions.

But the Standard Model has **three generations**:
- Generation 1: $(e, \nu_e, u, d)$
- Generation 2: $(\mu, \nu_\mu, c, s)$
- Generation 3: $(\tau, \nu_\tau, t, b)$

**Where do the other two generations come from?**

### The Answer (Preview)

The "3" does not come from additional spinor orbits — D₆ only has one pair (ω₅, ω₆).

Instead, the three generations arise from the **internal structure** of the quasicrystal:

> When D₆ projects to 3D, the acceptance domain in the perpendicular space $E_\perp$ stratifies into **three Occupation Domains** with φ-related volumes.

This is developed fully in **[IV.4 — Generations]**.

### What We've Established Here

This section establishes the **fermion content** of one generation:
- ω₅ spinors ↔ SM fermions (verified)
- Quantum number formulas (derived)
- The ×2 factor (explained)

The *replication* into three generations requires additional structure (occupation domains), which is the subject of IV.4.

---

## The ω₃ Weight Orbit (Brief)

For completeness, we note the third fundamental orbit:

| Property | Value |
|----------|-------|
| Definition | Third fundamental weight of D₆ |
| Count | 160 weights |
| |v|² | 3 |
| Shell structure | 20 + 60 + 60 + 20 |

The ω₃ orbit has **exotic charges** not found in the SM:
- $Q \in \{\pm\frac{7}{6}, \pm\frac{13}{12}, ...\}$

This suggests ω₃ represents a **composite/vacuum sector** — possibly related to Higgs physics or bound states. The full analysis belongs in **[IV.5 — Mass Mechanism]**.

---

## Summary

| Result | Statement |
|--------|-----------|
| **Fermion orbit** | ω₅ spinor (32 weights) |
| **Quantum numbers** | $I_3$, $Y$, $Q$ from weight components |
| **×2 factor** | Basis conversion (spinor ±½ → SM ±1) |
| **Charges** | $Q \in \{0, -1, +\frac{2}{3}, -\frac{1}{3}\}$ exactly |
| **Generation count** | One ω₅ = one generation |
| **Three generations** | From occupation domains (IV.4) |

---

## Claim Status

| Claim | Status | Source |
|-------|--------|--------|
| ω₅ has 32 spinor weights | **[VERIFIED]** | `C_verifications/05_generations/spinor_charges.py` |
| SM charges from ω₅ | **[VERIFIED]** | `C_verifications/05_generations/spinor_charges.py` |
| ×2 is basis conversion | **[VERIFIED]** | `C_verifications/05_generations/spinor_charges.py` |
| One ω₅ = one generation | **[VERIFIED]** | `C_verifications/05_generations/spinor_charges.py` |
| Spinors = fermions | **[KNOWN]** | Georgi-Glashow (1974), Slansky (1981) |

**Verification**: Run `python3 Appendices/C_verifications/05_generations/spinor_charges.py`

---

## References

1. **Georgi, H. & Glashow, S. L.** (1974). "Unity of All Elementary-Particle Forces." *Phys. Rev. Lett.* 32, 438.

2. **Slansky, R.** (1981). "Group Theory for Unified Model Building." *Phys. Rep.* 79, 1–128.

3. **Wilczek, F. & Zee, A.** (1982). "Families from Spinors." *Phys. Rev. D* 25, 553.

4. **Verification Code**: `Appendices/C_verifications/05_generations/spinor_charges.py`
