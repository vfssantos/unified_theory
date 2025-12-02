1. **Executive Summary**

There is, as of now, **no published, rigorous derivation of Standard Model masses or mixings from a D₆ → H₃ quasicrystal projection**. Your Weinberg-angle story is in much better shape because it depends only on static geometry (projection lengths and group embeddings). Masses, in contrast, need **dynamics**: an operator whose eigenvalues are the masses or whose couplings determine them.

Among your candidate mechanisms:

* Treating **mass as something internal to the 6D → 3D cut-and-project construction** (via |x⊥|, phason dynamics, or eigenvalues of a D₆/H₃ operator) is conceptually well-motivated and matches what people do in Kaluza–Klein and in quasicrystal physics.
* Treating mass as **angles / overlaps between fermion and Higgs “vertices”** is also in line with many extra-dimensional / string models.

But I couldn’t find any work that actually gets **m_H = 15/11 m_Z**, **Koide Q = 2/3**, or **θ_C = arctan φ⁻³** from D₆ geometry in a way that would pass the standard of “we wrote a Hamiltonian or action, diagonalized it, and got these numbers.” Those specific relations are, at present, best described as **numerology dressed in a geometric language**.

The good news is: there *is* a mathematically solid framework already built for **D₆ model sets and quasicrystal dynamics**, and it’s compatible with your Axiom 0 / geometric realism philosophy. Amaral’s “emergence of spacetime and matter from model sets” is very close in spirit: mass-like parameters arise from **statistics of local configurations in a D₆-based model set**, but no concrete SM spectrum yet. ([Preprints][1])

So the picture looks like this:

* **Weinberg angle**: close to “DERIVABLE” from group + projection geometry (as you already have).
* **Masses / mixings**: currently **SPECULATIVE** in the D₆–H₃ setting, but there is a plausible route if you’re willing to build and analyze an explicit dynamical model on the D₆ model set.

Below I’ll go mechanism-by-mechanism, then tackle Higgs, Koide, and Cabibbo, and finally spell out what’s concretely missing to turn your program into real derivations.

---

## 2. Mechanism Analysis (A–E)

### Summary table

| Mechanism                                         | Viable? (my assessment)                                                        | Evidence / Analogies                                                                                                       | Main Problems                                                                                                     |
| ------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| A. Mass from internal-space depth                 | **Plausible** conceptual template                                              | Kaluza–Klein mass ∝ p⊥²; internal coordinates & phasons in D₆ quasicrystals                                                | x⊥ is a *coordinate*, not obviously a conserved momentum; no explicit mass operator yet                           |
| B. Mass from distance to reference point in D₆    | **Mostly numerological**                                                       | Distances in weight space relate to Casimirs; used informally in some GUT toy models                                       | No natural preferred “mass origin” in D₆; distances alone don’t yield realistic spectra                           |
| C. Mass from eigenvalues (Laplacian/Casimir/etc.) | **Plausible and structurally strong**                                          | Casimirs determine representation scales; Laplacians on quasicrystals have φ-structured spectra                            | Need to actually define the operator on your D₆ model set and show SM fields correspond to its eigenmodes         |
| D. Mass from geometric Higgs–fermion coupling     | **Plausible** if embedded in a full model                                      | Extra-dimensional models commonly get Yukawas from overlaps/angles of localized wavefunctions ([INDICO-FNAL (Indico)][2])  | You still need a concrete map: which D₆ weights are which fermions/Higgs, and what operator produces the Yukawas? |
| E. Mass from phason dynamics                      | **Plausible for generation structure / mixing**, uncertain for absolute masses | Phasons are genuine degrees of freedom whose elastic energy & dispersion are well-studied in quasicrystals ([SciSpace][3]) | No existing construction where phason modes *are* SM flavors with correct masses and mixings                      |

Now a bit more detail on each.

---

### A. Mass from Internal-Space Depth (|x⊥|²)

**Analogy that works elsewhere**

In standard Kaluza–Klein theories, if an extra dimension is compact of radius R, then modes with quantized momentum n/R in that direction acquire mass

[
m_n^2 = m_0^2 + \frac{n^2}{R^2}.
]

So the internal momentum is literally the rest mass contribution. ([cds.cern.ch][4])

In cut-and-project quasicrystals, a lattice point (X ∈ D₆) splits as (x∥, x⊥):

* x∥ ∈ E∥ (physical)
* x⊥ ∈ E⊥ (internal / phason space)

and the set of allowed points is selected by a window W ⊂ E⊥. In Koca et al.’s construction of icosahedral quasicrystals from D₆, you literally have this structure: D₆ projected into a physical E and an internal E⊥ by the eigenbasis of the Cartan matrix. ([ResearchGate][5])

**How to turn this into “mass”**

A natural generalization of KK would be:

* Define an internal “wavevector” or displacement operator (\hat{p}_\perp) conjugate to x⊥.
* Let the mass operator be something like ( \hat{M}^2 \propto \hat{p}*\perp^2 + V(x*\perp)), where V arises from some effective potential in E⊥ (e.g., from window edges, phason stiffness, etc.).
* In a tight-binding picture on the D₆ model set, x⊥ labels *local environments*; the phason field w(x∥) describes smooth variations of these internal coordinates across physical space, and the phason elastic energy is of the general form (\int K_{ij} \partial_i w \partial_j w , d^3x). ([SciSpace][3])

Then:

* Different “particle species” could correspond to different **band minima** in (p∥, p⊥)-space.
* Their **effective masses** come from the curvature of the dispersion relation near those minima, which *does* depend sensitively on the internal-space structure.

**Pros**

* Natural source of **hierarchies**: discretized values of p⊥ or of allowed x⊥-orbits can easily exhibit φ-scaling, because D₆ → H₃ projections already encode φ in their scaling factors.
* Compatible with your phason = generations idea: different generations could be different internal “depths”.

**Cons / Problems**

* x⊥ in a static cut-and-project model is a coordinate, not a momentum. You need a dynamical model (a Hamiltonian or Lagrangian) on the model set where phason modes are quantized fields.
* Amaral’s work on “Emergence of spacetime and matter from model sets” builds exactly this sort of geometric state-sum on D₆-based model sets, but stops at the level of a general framework for defining energies and probabilities from local vertex-type frequencies; it doesn’t yet tie a specific operator’s eigenvalues to SM masses. ([Preprints][1])

**Verdict on A**

* **Viable?** Yes, conceptually **PLAUSIBLE**.
* But to get from “nice idea” to “Higgs = 125 GeV” you need a concrete Hamiltonian where eigenvalues are mass², and a proof that the relevant eigenvalues are (up to a scale) |x⊥|² for specific orbits.

---

### B. Mass from Distance to a Reference Point

The idea: pick a special point (\Lambda_0 \in D_6 \otimes \mathbb{R}) (origin, or a particular weight like the highest weight of a representation), and set

[
m \propto |\Lambda - \Lambda_0|.
]

It’s easy to *fit* spectra like this—lots of people have done distance-based numerology in weight space—but there’s no widely accepted mechanism in gauge theory that says “rest mass is literally Euclidean distance in the abstract weight space.”

* In many GUTs, you *do* see mass scales related to **quadratic Casimirs** C₂(R). Those are quadratic in the weights and roots, so they’re related to norms in root space—but in a group-theoretic way, not “distance from some arbitrary point”.
* You can always pick (\Lambda_0) such that a linear combination of distances gives your preferred numbers, but this has the same freedom as tuning parameters in a Lagrangian.

**Verdict on B**

* Without a dynamical principle that singles out a unique (\Lambda_0) and a specific function f(dist), Mechanism B is essentially **numerology**.
* Any serious attempt here immediately morphs into Mechanism C: masses as functions of Casimirs / eigenvalues, not raw distances.

---

### C. Mass from Eigenvalues (Laplacian, Casimir, etc.)

This is the most structurally promising mechanism.

**1. Casimirs**

* For a gauge group G, the masses of heavy gauge bosons after symmetry breaking often scale like

  [
  M \sim g v \sqrt{C_2(R_{\text{eff}})}
  ]

  where C₂ is the quadratic Casimir of the representation under which the field transforms. ([people.fjfi.cvut.cz][6])

* In a D₆-based GUT (SO(12)), it’s perfectly natural that different multiplets (and thus SM fields embedded therein) have different C₂ values, giving rational ratios of masses.

**2. Laplacians on quasicrystals**

* Tight-binding Hamiltonians / Laplacians on quasiperiodic graphs have spectra with **hierarchical, often φ-structured features**, especially in 1D Fibonacci and 2D Penrose systems. ([repository.ubn.ru.nl][7])
* D₆ → H₃ noncrystallographic model sets fall into this general category. Their spectral measures and density of states can, in principle, be computed.

**3. D₆/H₃-specific structure**

* Koca et al. show that the projection from D₆ to H₃ is naturally split into E (physical) and E⊥ (internal) spaces, where the Coxeter element has eigenvalues involving powers of φ. ([ResearchGate][5])
* Those eigenvalues (essentially e^{2πi m/h} with exponents related to φ) already control **inflation factors** and local coordination statistics.

So it’s very plausible that:

* some **natural operator** (Laplacian, Dirac operator, or a geometric state-sum eigenvalue) on the D₆ model set has eigenvalues organized by φ,
* and that these eigenvalues could be normalized to match SM mass ratios.

But:

* I could not find a paper where such an operator is explicitly defined and diagonalized with an SM interpretation on a D₆/H₃ quasicrystal.
* Amaral’s state-sum construction defines weights using **relative frequencies of local vertex types and their overlaps**, leading to an invariant partition function and associated expectation values. That’s ripe for being turned into an effective Hamiltonian, but they do not go as far as embedding the Standard Model or computing a mass spectrum. ([Preprints][1])

**Verdict on C**

* **Viable?** **PLAUSIBLE**, and probably the right backbone for a rigorous program.
* But in the current literature, **no explicit D₆/H₃ operator has been shown to produce SM masses or your specific ratios.**

---

### D. Mass from Geometric Higgs–Fermion Couplings

This is the “angle or overlap between fermion vertex and Higgs vertex” story.

In many extra-dimensional and string-inspired models, Yukawa couplings come from **overlap integrals of localized wavefunctions**:

* If ψ_L(x,y), ψ_R(x,y), and H(x,y) are localized on branes or curves in internal space, then

  [
  y_{ij} \sim \int d^n y, \psi_{Li}(x,y) \psi_{Rj}(x,y) H(x,y)
  ]

  and exponential hierarchies naturally appear as e^{-distance² / width²}, or as trigonometric factors depending on angles in the internal space. ([INDICO-FNAL (Indico)][2])

Your E₈-based heuristic m_H = (√5/3) m_t:

* uses two fixed vectors v_F=(1,1,1) and v_H=(0, φ, φ⁻¹) with |v_F|²=|v_H|²=3,
* and cos(angle) = v_F·v_H / (|v_F||v_H|) = √5/3.

That’s exactly what one expects from a **purely geometric Yukawa factor**.

In a D₆ → H₃ setting:

* The 20-vertex dodecahedron from the ω₃ weight orbit decomposes as something like 8_L + 8_R + 4_H in your picture; those 4 special vertices are your Higgs.
* If you can identify **fermion weight vectors** for each generation in D₆, then define

  [
  y_f \sim F(\angle(\Lambda_f, \Lambda_H))
  ]

  or a similar geometric function (e.g., overlap via distance within the acceptance window), you get a mechanistic handle on Yukawas.

**What I could find**

* I did not find a paper where *D₆ weights are explicitly assigned to Standard Model fermions plus Higgs* in a way that defines Yukawas as such geometric functions.
* However, there *are* many works using icosahedral family symmetry A₅ or binary icosahedral groups for neutrino mixing, where mixing angles are functions of φ from group representation theory. ([APS Link][8])

So there is a strong precedent for:

* “Angles between representation vectors” → “mixing angles” and “Yukawa ratios”.

**Verdict on D**

* **Viable?** **PLAUSIBLE** and quite attractive for explaining relations like m_H ∼ √5/3 m_t.
* But there is currently **no D₆/H₃-based paper** that explicitly computes such angles and equates them with observed Yukawas or masses.

---

### E. Mass from Phason Dynamics

Phasons are the “hidden” degrees of freedom of quasicrystals:

* In the cut-and-project picture, they correspond to **shifts in internal-space coordinates x⊥**.
* Phason excitations show up in diffraction and in thermal/deformation experiments; their elastic and kinetic properties are well-characterized in quasicrystal materials. ([SciSpace][3])

In your framework:

* 3 phason dimensions ↔ 3 generations is a natural idea.
* Masses and mixings could come from how strongly each mode “wiggles” in E⊥.

This lines up nicely with two things:

1. **Quasicrystal physics:** phasons have associated energy costs (stiffness) and dispersion relations; in some lattice models, electrons interacting with quasiperiodic potentials develop effective masses and localization patterns heavily influenced by phason disorder. ([repository.ubn.ru.nl][7])
2. **Flavor physics:** some models of neutrino mixing and mass hierarchies use specific discrete symmetries (A₅, icosahedral) to give golden ratio mixing angles and hierarchical masses. ([APS Link][8])

So, thinking of each generation as a different phason eigenmode is not crazy.

**What’s missing**

* No explicit model where **phason modes of a D₆/H₃ model set are quantized as SM flavors**.
* No clear identification of “phason kinetic energy” with **rest mass** rather than some emergent, condensed-matter-like energy scale.

**Verdict on E**

* **Viable?** **PLAUSIBLE** for generation structure and mixing.
* For absolute masses and specific ratios (like φ-depth), it’s still **SPECULATIVE**.

---

## 3. Derivation Attempts for Specific Observables

### 3.1 Higgs Mass (m_H)

**Your target relations**

* m_H ≈ (15/11) m_Z ≈ 124.35 GeV
* m_H ≈ (√5/3) m_t ≈ 128.8 GeV

#### 3.1.1 What the Standard Model gives structurally

In the SM:

[
M_W = \frac{g v}{2}, \quad
M_Z = \frac{v}{2}\sqrt{g^2 + g'^2}, \quad
m_H = \sqrt{2\lambda}, v.
]

Therefore

[
\frac{m_H}{M_Z} = \sqrt{\frac{8\lambda}{g^2 + g'^2}}.
]

Your D₆ → H₃ Weinberg-angle derivation fixes the **ratio** g'/g (and thus sin²θ_W = g'^2/(g²+g'^2)), but does not fix λ.

* Using your sin²θ_W ≈ 0.2327, cos²θ_W ≈ 0.7673.
* If we **assume** λ = c g², then

  [
  \frac{m_H}{M_Z} = \sqrt{8 c \cos^2\theta_W}.
  ]

So any specific m_H/M_Z ratio translates directly into a choice of c.

* For m_H/M_Z = 15/11, we get

  [
  c = \frac{(15/11)^2}{8\cos^2\theta_W}
  = \frac{207 - 27\sqrt{5}}{484} \approx 0.303.
  ]

This is not obviously a simple φ-expression; it’s a messy algebraic combination.

* If instead we choose a **simple φ-motivated** ratio, say λ/g² = 1/(2φ) (which is natural in a φ-based theory), then with your θ_W we get m_H/M_Z ≈ 1.377, already close to the experimental ≈ 1.373, *without* the contrived 15/11.

So:

* From pure SM structure plus your θ_W, **no special status** for 15/11 emerges.
* You can get *approximate* agreement with data by a φ-based λ/g² choice, but that doesn’t single out 15/11 either.

#### 3.1.2 Geometric route via D₆ / Higgs orbit

To truly “derive” m_H from D₆ geometry, you’d need:

1. **Field identification:** specify which D₆ weight orbit = Higgs (your 4 poles in the pyritohedral decomposition).
2. **Quartic coupling from geometry:** express λ as a function of D₆ invariants of that orbit:

   * e.g. λ ∝ some combination of vertex-type frequencies and overlaps in the D₆ model set that include the Higgs vertices (this is exactly the kind of object Amaral defines in his hits measure / state sum). ([Preprints][1])
   * or λ ∝ C₂(R_H) / (some normalization) where R_H is a representation of D₆ or H₃.
3. **Gauge couplings from geometry:** you already have a geometric derivation for g, g' via projection lengths, giving θ_W.
4. **Plug & compute:** with λ(g, geometry), evaluate m_H/M_Z from the SM formula.

I did not find any work that completes steps (2)–(4) for D₆/H₃.

#### 3.1.3 Verdict on m_H formulas

* m_H = (15/11) m_Z:

  * I found no published derivation from D₆, D₆/H₃, or any other group.
  * Within SM + your θ_W, 15/11 corresponds to an obscure choice of λ/g² with no obvious geometric meaning.
  * **Classification:** **NUMEROLOGY** in the D₆ context at present.

* m_H = (√5/3) m_t:

  * This arises naturally as cos(angle) between two particular E₈ vectors, but I do not see a D₆/H₃ paper reproducing that from the D₆ structure.
  * You can *embed* that angle into H₃ (icosahedral geometry loves φ), but that’s reverse engineering, not derivation.
  * **Classification:** **SPECULATIVE**; has a clean geometric form, but not yet tied to D₆/H₃ dynamics.

---

### 3.2 Koide Formula Q = 2/3

[
Q = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}.
]

**What geometry already explains (independently of D₆)**

* Write the vector of square roots (\vec{v} = (\sqrt{m_e}, \sqrt{m_\mu}, \sqrt{m_\tau})) and (\vec{u}=(1,1,1)).

* Many authors (Foot, Brannen, Kocik, etc.) show Q = 2/3 iff the angle between v and u is 45°:

  [
  Q = \frac{1}{3}\left(1 + 2 \cos^2 \theta\right), \quad Q=2/3 \Rightarrow \theta=45^\circ.
  ]

  ([brannenworks.com][9])

* In the phase formulation, the masses can be parametrized as

  [
  m_i = M\left(1 + \sqrt{2}\cos(\theta_0 + 2\pi i/3)\right)^2,
  ]

  where θ₀ is a phase angle; Q=2/3 corresponds to a specific constraint on that phase.

So Koide is very naturally about:

* A **3D vector at a specific angle**,
* or a complex vector with **three phases 120° apart** (an A₂ structure in phase space).

**Embedding into A₂ ⊂ D₆**

* D₆ certainly contains many A₂ subalgebras: pick any equilateral triangle in the D₆ root system.
* Under projection to H₃, an A₂ root system (hexagon in 2D) can be realized as a regular hexagon in some 2D subspace of E∥.
* So it’s easy to find A₂’s geometrically; the challenge is: **why that particular A₂, and why that particular angle?**

I did not find any paper that:

1. Identifies a specific A₂ ⊂ D₆ whose **projected** geometry forces the Koide angle (45°) or Q=2/3, and
2. Assigns e, μ, τ to three *fixed* weights in that A₂ such that their squared norms or some geometric function of them give the observed masses.

There is related work:

* Kocik’s “Koide lepton mass formula and geometry of circles” shows Koide as a Descartes circle configuration, again with a special angle condition. ([Academia][10])
* Newer work (e.g., Li 2025) views Koide as a **phase-coherence condition** for internal vectors; again, no D₆ embedding, but a strong geometric/topological flavor. ([Preprints][11])

**Verdict on Koide in D₆**

* Q = 2/3 is very naturally geometric (angle / phase), but that geometry is **generic 3D Euclidean**, not specifically D₆-derived.
* Embedding an A₂ with that geometry inside D₆ is always possible, but picking one *post hoc* does not count as a derivation.
* **Classification in the D₆ program:** **SPECULATIVE**; Koide’s beauty is real but independent of D₆ so far.

---

### 3.3 Cabibbo Angle θ_C = arctan(φ⁻³)

Numerically:

* φ ≈ 1.618
* φ⁻³ ≈ 0.2361
* θ_C = arctan(φ⁻³) ≈ 13.28°, vs experimental ≈ 13.02°.

Your narrative: D₄ → A₃ twist inside D₆, with the twist angle or relative orientation under H₃ projection giving φ⁻³.

**What’s in the literature**

* Golden-ratio-based mixing is well known for **neutrinos**, not quarks: Everett & Stuart used icosahedral symmetry to predict solar neutrino θ₁₂ via φ-related angles. ([APS Link][8])
* Some speculative works (including one from QGR) associate Cabibbo with φ⁻³ or similar, using polyhedral helices or crystal/quasicrystal geometry, but not from D₆ root-space embeddings.
* I couldn’t locate a paper that actually constructs the D₄ and A₃ inside D₆, projects them to H₃, and *computes the angle* between relevant subspaces to be arctan(φ⁻³).

Mathematically, D₄ and A₃ are certainly subalgebras of D₆:

* D₄ ~ so(8) and A₃ ~ su(4) both embed in so(12).
* There will be many ways to embed them, related by automorphisms.
* Without a fully fixed GUT or gauge-Higgs-unification model specifying *which* D₄ and *which* A₃ correspond to up/down quark sectors, the “twist” angle is not unique.

**Verdict on Cabibbo**

* The φ⁻³ relation is neat, but I didn’t find an embedding-based derivation from D₆.
* **Classification:** **SPECULATIVE** from the D₆ perspective; currently numerology supported by post hoc geometric stories.

---

### 3.4 φ-depth Mass Hierarchies

Your idea: mass ratios scale like φⁿ for integer (or half-integer) “depths”.

There *are* hints in the literature that φ-scaling might be relevant to fermion masses and mixings, especially for neutrinos:

* icosahedral / A₅ flavor models for neutrino mixing, where φ appears in mixing angles and sometimes in mass ratios. ([APS Link][8])
* various “golden ratio” models for neutrinos and some quirky golden-ratio fits to Higgs/top/Z masses. ([inspirehep.net][12])

In quasicrystal physics, φ appears everywhere:

* inflation/deflation factors,
* frequency of local patches,
* spectral gaps and scaling of density of states. ([MDPI][13])

So as a *pattern*, φ^n hierarchies are unsurprising in a D₆ → H₃ quasicrystal.

But:

* I found no D₆-based model where each SM fermion is tied to a specific “φ-depth” defined from internal coordinates or vertex-type frequencies *and* the resulting φ^n scaling matches observed masses at the few-percent level without extra tunings.

**Verdict on φ-depth**

* As a coarse phenomenological ansatz, **PLAUSIBLE** in a φ-based quasicrystal geometry.
* As a derivation from D₆/H₃, **SPECULATIVE** until an explicit operator and mapping of states is provided.

---

## 4. Literature Review (selected, relevant)

### D₆ / H₃ quasicrystals and model sets

* **Koca, Al-Ajmi, Al-Barwani (2020)**, *Icosahedral Polyhedra from D6 Lattice and Danzer’s ABCK Tiling.*

  * Constructs H₃-symmetric polyhedra (including dodecahedron/icosidodecahedron) from D₆, with explicit projection matrices and decomposition into E and E⊥. ([ResearchGate][5])
* **Amaral (2022)**, *On the Emergence of Spacetime and Matter from Model Sets.*

  * Develops a state-sum and probabilistic measure on model sets (e.g. D₆-derived quasicrystals) using local vertex-type frequencies and overlaps; proposes “geometric realism” where dynamics and parameters like mass should emerge from the discrete geometry itself, but no explicit SM spectrum yet. ([Preprints][1])

### Phasons and quasicrystal dynamics

* Reviews and papers on phason elasticity and dynamics: phasons as Goldstone-like modes with characteristic elastic constants and diffusive dynamics; their contribution to physical properties is well established in quasicrystal materials. ([SciSpace][3])

### Mass from extra dimensions and geometry

* Kaluza–Klein and gauge-Higgs-unification models: mass towers (m_n^2 = m_0^2 + n^2/R^2), Higgs as extra-dimensional component of gauge fields with masses determined by compactification geometry. ([cds.cern.ch][4])

### Koide and geometric interpretations

* **Brannen (2006)**, *The Lepton Masses.*

  * Discusses Koide’s relation, shows its exactness for leptons at the time and connects it to circulant matrices and phases. ([brannenworks.com][9])
* **Kocik (2012)**, *The Koide Lepton Mass Formula and Geometry of Circles.*

  * Relates Koide to Descartes circle theorem; Q=2/3 corresponds to a specific geometric condition on four mutually tangent circles. ([Academia][10])
* **Li (2025)**, *The Koide Relation and Lepton Mass Hierarchy from Phase Coherence.*

  * Proposes Koide as a universal phase coherence condition in an internal phase space; again, geometric but not D₆-specific. ([Preprints][11])

### Icosahedral / golden ratio flavor models

* **Everett & Stuart (2009)**, *Icosahedral family symmetry and the golden ratio prediction for the solar neutrino mixing angle.*

  * Uses A₅ (icosahedral) family symmetry to derive φ-related neutrino mixing angles. ([APS Link][8])
* **Gu (2020)**, *A possible origin of three generations of neutrinos and mass hierarchy.*

  * Uses icosahedral/binary icosahedral group structures to explain three generations and mass hierarchies; golden ratio patterns appear in mixing. ([APS Link][14])

### Quasicrystal / golden-ratio-based physics speculations

* Multiple works (including some associated with quantum gravity / E₈ / golden ratio) derive approximate Weinberg angles, fine-structure constants, and mass ratios from φ, but typically outside a D₆/H₃ framework and without a fully accepted dynamical theory. ([Academia][15])

---

## 5. Gap Analysis – What’s Missing

To upgrade from “these numbers match nicely” to “these numbers are derived from D₆/H₃ geometry”, you need at least:

1. **A concrete dynamical model on a D₆ model set.**

   * Lattice Hamiltonian or Lagrangian whose degrees of freedom live on D₆-projected sites (E∥) with internal labels (x⊥ or vertex type).
   * An explicit operator (Dirac operator, Laplacian, or state-sum-derived evolution operator) whose eigenvalues are interpreted as mass².

2. **A precise mapping from SM fields to D₆/H₃ structures.**

   * Assign each SM fermion, gauge boson, and the Higgs to:

     * specific D₆ weight or root or
     * a specific orbit of local configurations in the quasicrystal (e.g. a vertex type class).
   * Ensure gauge charges and chiralities work out (likely via an E₆/E₈ “parent”, but the projection must be clear).

3. **A geometric definition of λ (Higgs self-coupling) in terms of D₆ invariants.**

   * Something like “the quartic coupling is proportional to a combination of vertex frequencies and overlaps involving the 4-Higgs vertices” or to a Casimir invariant of a D₆ representation.
   * This is what you’d need to turn your θ_W derivation into a simultaneous (θ_W, m_H) derivation.

4. **A principle that fixes Koide’s angle / phase.**

   * From the A₂ picture, you need a reason the internal phase vector lies exactly at 45° to (1,1,1).
   * In a D₆ context, that might come from:

     * a constraint in the geometric state sum (e.g. maximizing or minimizing a Schur-convex functional over a set of allowed phase configurations), or
     * a specific A₂ embedding that is singled out by your Axiom 0 (maximal topological stability).

5. **A unique D₄/A₃ embedding and twist for Cabibbo.**

   * Without specifying which D₄ and A₃ subalgebras are physically realized, the relative “Cabibbo” angle is not determined.
   * You need an argument that Axiom 0 + projection geometry picks out exactly one (or a D₆-automorphism class of) embedding(s) with twist arctan(φ⁻³).

6. **Control over radiative corrections.**

   * Even if you get tree-level mass relations right, you must show they survive quantum corrections to within your claimed accuracy, or explain why the relations are defined at some particular scale (e.g., unification scale).

---

## 6. Recommendations – Concrete Next Steps

Here are some focused, technically meaningful things that would move the program toward “derivable”:

1. **Build a toy D₆ quasicrystal Hamiltonian and compute spectra numerically.**

   * Use a simple tight-binding model on a D₆ → H₃ model set (e.g. Danzer ABCK tiling) with:

     * one scalar field (Higgs-like),
     * possibly one fermionic field.
   * Introduce a φ-based local interaction (e.g. coupling proportional to local vertex-type frequencies) and compute low-lying eigenvalues.
   * Check if eigenvalue ratios show φ^n patterns that could map onto lepton/quark hierarchies.

2. **Define an explicit “mass operator” from Amaral-style state sums.**

   * Start from the geometric state sum WT₄ and associated probabilities μ(T). ([Preprints][1])
   * Define an operator whose eigenvalues measure “geometric frustration” or “curvature” at each local configuration.
   * Propose that the expectation of this operator for a given orbit = m² for a particle associated to that orbit.

3. **Classify A₂ subalgebras of D₆ and their H₃ projections.**

   * Use root-system mathematics to find all A₂ ⊂ D₆ up to the Weyl group.
   * Compute the angle between the vector (1,1,1) in the “mass space” and the projection of simple roots; look for a unique set that reproduces the Koide 45° condition.
   * If there is a unique, symmetry-preferred A₂ giving that angle, that’s strong evidence that Koide might be *derivable* in this framework.

4. **Do the same for the D₄/A₃ embedding and Cabibbo.**

   * Fix a specific SO(12) GUT embedding and identify D₄ (up-type) and A₃ (down-type) subsectors.
   * Compute the relative orientation of their relevant SU(2) subgroups after D₆ → H₃ projection.
   * See whether any natural embedding yields θ_C ≈ arctan(φ⁻³).

5. **Geometric determination of λ from the Higgs orbit.**

   * Take the 4 Higgs vertices in the pyritohedral decomposition.
   * Define a quartic functional over the D₆ model set (e.g. count of 4-point clusters involving those vertices).
   * Use Axiom 0 (minimize a Schur-convex curvature functional) to fix λ in terms of these counts.
   * Plug into the SM formula with your θ_W and see whether m_H/m_Z comes out close to observed value *without* fitting.

If even a simplified toy version works for one of these observables, it elevates that observable from “numerology” to at least “PLAUSIBLE with a concrete mechanism.”

---

## 7. Overall Verdict

### 7.1 Mechanism Assessment (A–E)

| Mechanism                                       | Viable?                                | Evidence                                                                                                                                        | Problems                                                                                                                    |                                                                                                      |    |                                                                         |                                           |    |                                                            |
| ----------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -- | ----------------------------------------------------------------------- | ----------------------------------------- | -- | ---------------------------------------------------------- |
| **A: Internal depth (                           | x⊥                                     | ²)**                                                                                                                                            | **PLAUSIBLE**                                                                                                               | Strong analog with KK mass from extra dimensions; phason/internal coordinates in D₆ model sets allow | x⊥ | -type quantities; Amaral’s framework supports geometry-based parameters | Lacks explicit dynamical operator linking | x⊥ | to mass; x⊥ is coordinate, not momentum; no SM mapping yet |
| **B: Distance to reference point**              | **Largely NUMEROLOGY**                 | Distances in weight space loosely related to Casimirs                                                                                           | No natural distinguished point, and no dynamical principle selecting a specific distance formula                            |                                                                                                      |    |                                                                         |                                           |    |                                                            |
| **C: Eigenvalue structure (Laplacian/Casimir)** | **PLAUSIBLE and structurally strong**  | Casimirs and Laplacians routinely control mass scales in field theories; D₆/H₃ has φ-rich spectral structure                                    | No explicit D₆/H₃ operator has been built and diagonalized with SM identifications; still a blueprint, not a model          |                                                                                                      |    |                                                                         |                                           |    |                                                            |
| **D: Higgs–fermion coupling angles**            | **PLAUSIBLE**                          | Overlap/angle-based Yukawas are standard in extra dim / string models; angle formulas like √5/3 are naturally geometric                         | Requires a concrete assignment of fermion and Higgs weights in D₆; missing an explicit Yukawa operator                      |                                                                                                      |    |                                                                         |                                           |    |                                                            |
| **E: Phason dynamics**                          | **PLAUSIBLE (for generations/mixing)** | Phasons are genuine degrees of freedom with well-understood elastic and dynamical properties; mapping generations to phason modes is attractive | No demonstrated mapping from phason eigenmodes to SM flavours, and no direct identification of phason energy with rest mass |                                                                                                      |    |                                                                         |                                           |    |                                                            |

### 7.2 Specific Predictions

| Prediction                | Derivable now? | Mechanism that *could* work                                       | Current status                                                                                                                      |
| ------------------------- | -------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| m_H (Higgs mass / m_Z)    | **No**         | C + D (Casimir-based λ plus geometric Yukawas)                    | 15/11 m_Z and √5/3 m_t are not currently derivable from D₆; they require tuned λ/g² or chosen angles; **NUMEROLOGY** at present     |
| Koide Q = 2/3             | **No**         | C/A₂ phase geometry with an internal angle/phase fixed by Axiom 0 | Koide is beautifully geometric, but the geometry is generic 3D / complex phases, not specifically D₆; **SPECULATIVE** in D₆ context |
| Cabibbo θ_C = arctan(φ⁻³) | **No**         | D (misalignment of D₄/A₃ embeddings)                              | No explicit D₄/A₃ embedding in D₆ has been shown to produce this; **SPECULATIVE** within D₆                                         |

### 7.3 Overall Verdict

For the **mass mechanism from D₆ → H₃ quasicrystal geometry** as of today:

* **Verdict:** **SPECULATIVE**
* **Confidence in this classification:** ~80%.

Reasoning:

* The D₆ → H₃ geometrical machinery is solid and well-documented.
* There’s a clear, mathematically respectable path to defining **geometry-based operators** on D₆ model sets whose eigenvalues or couplings could become masses.
* But no one has yet walked that full path through for the actual Standard Model spectrum, especially for the specific relations you listed.

The upside: you’re not trying to force pure numerology onto arbitrary numbers. You’re sitting on top of a rich, φ-laced, D₆/H₃ geometry and there *are* known mechanisms (KK-like internal momenta, eigenvalue problems, geometric Yukawas, phason dynamics) that can, in principle, produce discrete mass spectra and mixing angles.

The next leap is to **pick one mechanism (C + D is the strongest candidate), write down an explicit operator or state-sum model on your D₆ quasicrystal, and calculate**. That’s where this stops being numerology and starts becoming physics.

[1]: https://www.preprints.org/manuscript/202111.0359/v2/download "On the Emergence of Spacetime and Matter from Model Sets"
[2]: https://indico.fnal.gov/event/1965/contributions/53382/attachments/33212/40735/080818_Ponton.pdf?utm_source=chatgpt.com "Lectures on Extra Dimensions Part I"
[3]: https://scispace.com/pdf/effective-field-theory-for-quasicrystals-and-phasons-2py5kgcmwm.pdf?utm_source=chatgpt.com "Effective Field Theory for Quasicrystals and Phasons Dynamics"
[4]: https://cds.cern.ch/record/365240/files/9809406.pdf?utm_source=chatgpt.com "Cosmological Phase Transitions and Radius Stabilization ..."
[5]: https://www.researchgate.net/figure/The-Coxeter-Dynkin-diagram-of-E-8_fig4_231028701?utm_source=chatgpt.com "The Coxeter-Dynkin diagram of E 8 ."
[6]: https://people.fjfi.cvut.cz/snobllib/Casimirs_Lesna.pdf?utm_source=chatgpt.com "Representations of Lie algebras, Casimir operators and ..."
[7]: https://repository.ubn.ru.nl/bitstream/handle/2066/18948/18948.pdf?utm_source=chatgpt.com "Electronic properties of quasicrystals - A tight-binding study"
[8]: https://link.aps.org/doi/10.1103/PhysRevD.79.085005?utm_source=chatgpt.com "Icosahedral () family symmetry and the golden ratio prediction ..."
[9]: https://brannenworks.com/MASSES2.pdf?utm_source=chatgpt.com "The Lepton Masses"
[10]: https://www.academia.edu/24595560/The_Koide_Lepton_Mass_Formula_and_Geometry_of_Circles?utm_source=chatgpt.com "The Koide Lepton Mass Formula and Geometry of Circles"
[11]: https://www.preprints.org/manuscript/202505.2156?utm_source=chatgpt.com "The Koide Relation and Lepton Mass Hierarchy from ..."
[12]: https://inspirehep.net/files/e15463841abb31ecf8a9805f451a5f98?utm_source=chatgpt.com "The Higgs mass coincidence problem"
[13]: https://www.mdpi.com/2073-8994/12/12/1983 "Icosahedral Polyhedra from D6 Lattice and Danzer’s ABCK Tiling"
[14]: https://link.aps.org/doi/10.1103/PhysRevResearch.2.033290?utm_source=chatgpt.com "A possible origin of three generations of neutrinos and mass ..."
[15]: https://www.academia.edu/Documents/in/Topological_Quantum_Computing?utm_source=chatgpt.com "Topological Quantum Computing Research Papers"
