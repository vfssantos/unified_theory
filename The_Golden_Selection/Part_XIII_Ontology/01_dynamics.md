# IX.1–4 — Dynamical Quantities

---

## IX.1 — What Is Mass?

### The Standard Answer

Mass is a measure of:
1. **Inertia**: Resistance to acceleration (F = ma)
2. **Gravitational charge**: Source of gravitational attraction
3. **Energy content**: E = mc² (rest mass = rest energy)

In the Standard Model, mass arises from the Higgs mechanism — particles acquire mass by coupling to the Higgs field.

### The Golden Selection Answer

> **Mass is the eigenvalue of the internal Laplacian L⊥.**

More precisely:

$$m \propto \sqrt{\lambda(L_\perp)}$$

where λ(L⊥) is the eigenvalue of the graph Laplacian on the internal space E⊥.

**In plain terms**: Mass measures how "tightly bound" a particle is to the internal geometry. Heavy particles oscillate rapidly in E⊥; light particles oscillate slowly.

### The Derivation

From [Part IV.5]:

1. Fermions live on the ω₅ spinor orbit in D₆
2. The orbit projects to physical space (E∥) and internal space (E⊥)
3. The internal Laplacian L⊥ has discrete eigenvalues
4. These eigenvalues determine mass via the Koide geometry

The mass formula:
$$m_i = M_0 \cdot T_i^4$$

where T_i are the Koide parameters determined by L⊥ eigenstates.

### Status

**[DERIVED]** — The mass mechanism is explicit and produces verified predictions (lepton masses to 0.01%).

### Implications

1. **Mass is geometric**: Not a free parameter, but a calculable eigenvalue
2. **Mass hierarchy**: Different generations = different L⊥ bands
3. **Masslessness**: Particles with zero L⊥ eigenvalue (photon, gluon) are massless
4. **Higgs role**: The S₄ shell sets the overall mass scale, not individual masses

---

## IX.2 — What Is Energy?

### The Standard Answer

Energy is:
1. **Capacity to do work**: E = ∫F·dx
2. **Conserved quantity**: From time-translation symmetry (Noether)
3. **Equivalent to mass**: E = mc²

### The Golden Selection Answer

> **Energy is the total strain in the quasicrystal configuration.**

More precisely:

$$E = E_{\text{strain}} + E_{\text{kinetic}} + E_{\text{potential}}$$

where:
- **E_strain**: Deviation from ideal H₃ geometry (the "cost" of matter)
- **E_kinetic**: Rate of phason updates (motion through the lattice)
- **E_potential**: Configuration energy from inter-site couplings

**In plain terms**: Energy measures how much the quasicrystal is "stressed" by the presence of particles and their motion.

### The Derivation

From [Part 0 — Axiom]:

The Geometric Free Energy is:
$$F = E_{\text{strain}} + \lambda \cdot \kappa_{\text{Schur}}$$

Energy is the first term — the elastic cost of deforming the ideal lattice.

For a particle at rest:
$$E_{\text{rest}} = mc^2 = M_0 \cdot T^4 \cdot c^2$$

This is the strain energy of maintaining a localized excitation in E⊥.

### Status

**[PARTIAL]** — Rest energy is derived (via mass). Kinetic energy requires the dynamics of Part V.

### Implications

1. **E = mc²**: Rest energy is the "strain cost" of existence
2. **Conservation**: Follows from the lattice's discrete time-translation symmetry
3. **Binding energy**: Nuclear binding = reduced total strain when nucleons combine

---

## IX.3 — What Is Momentum?

### The Standard Answer

Momentum is:
1. **Mass times velocity**: p = mv
2. **Conserved quantity**: From space-translation symmetry (Noether)
3. **Generator of translations**: In quantum mechanics, p = -iℏ∇

### The Golden Selection Answer

> **Momentum is the phase gradient of the wave function across the lattice.**

More precisely:

$$p = \hbar \cdot \nabla_{\text{lattice}} \phi$$

where φ is the phase of the quantum amplitude at each lattice site.

**In plain terms**: Momentum measures how rapidly the quantum phase changes from site to site. A particle "moving right" has phase increasing to the right.

### The Derivation

**[OPEN]** — This requires the quantum walk formalism of Part V.2.

The expected derivation:
1. A particle is a localized wave packet on the H₃ graph
2. The packet's center moves at the group velocity
3. Momentum is the wave vector of the packet
4. Conservation follows from lattice translation symmetry

### Status

**[OPEN]** — Awaits Part V (Spacetime Dynamics).

### Implications

1. **Discrete momentum**: On a lattice, momentum is bounded (Brillouin zone)
2. **Lorentz transformation**: Must emerge in the continuum limit
3. **Uncertainty principle**: Δx·Δp ≥ ℏ/2 from wave packet properties

---

## IX.4 — What Is Inertia?

### The Standard Answer

Inertia is:
1. **Resistance to acceleration**: F = ma
2. **Equivalent to mass**: Inertial mass = gravitational mass (equivalence principle)
3. **Unexplained**: Why does mass resist acceleration?

### The Golden Selection Answer

> **Inertia is the "drag" from updating the internal configuration during acceleration.**

More precisely:

When a particle accelerates, its internal state (in E⊥) must be continuously updated to match the new velocity frame. This update has a "cost" proportional to mass.

**In plain terms**: A heavy particle has a complex internal structure (high L⊥ eigenvalue). Accelerating it requires reorganizing this structure, which takes effort proportional to its complexity.

### The Derivation

**[OPEN]** — This is speculative and requires:
1. A dynamics for the internal degrees of freedom
2. A coupling between E∥ motion and E⊥ updates
3. Derivation of F = ma from this coupling

### Status

**[OPEN]** — Highly speculative. This is one of the deepest questions.

### Implications

1. **Mach's principle**: Inertia might relate to the global lattice structure
2. **Equivalence principle**: If gravity is also lattice curvature, inertial = gravitational mass
3. **Quantum inertia**: At small scales, inertia might show discrete effects

---

## Summary

| Concept | Golden Selection Definition | Status |
|---------|----------------------------|--------|
| **Mass** | L⊥ eigenvalue | [DERIVED] |
| **Energy** | Lattice strain | [PARTIAL] |
| **Momentum** | Phase gradient | [OPEN] |
| **Inertia** | Update drag | [OPEN] |

**The pattern**: Dynamical quantities are **geometric properties** of the quasicrystal — eigenvalues, strains, gradients. They are not fundamental; they emerge from the structure.

