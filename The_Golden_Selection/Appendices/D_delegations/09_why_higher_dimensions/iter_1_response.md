

# **Dimensional Necessity: The Ontological Status of Higher-Dimensional Embeddings in Quasicrystalline Physics**

## **1\. Introduction: The Crystallographic Paradigm Shift and the Dimensional Crisis**

The discovery of quasicrystals in 1982 by Dan Shechtman marked a rupture in the foundational logic of condensed matter physics, a field previously governed by the rigid dichotomy between periodic order (crystals) and disorder (amorphous solids/glasses).1 The diffraction pattern of the rapidly solidified $Al\_6Mn$ alloy, displaying sharp Bragg peaks arranged with icosahedral point symmetry, presented an immediate and profound paradox. According to the crystallographic restriction theorem, which had stood unchallenged for nearly a century, translational periodicity in three dimensions is incompatible with 5-fold, 8-fold, 10-fold, or 12-fold rotational symmetries.2 The existence of such symmetries in a material exhibiting long-range order—evidenced by the sharpness of the diffraction spots—demanded a radical reformulation of the concept of a "crystal."

The resolution to this paradox, developed in the years following Shechtman’s discovery, relied on a mathematical maneuver that would have profound ontological implications: the elevation of the system's description into higher-dimensional superspace. The seminal insight, formalized by de Bruijn, Kramer, Neri, Duneau, and Katz, was that the symmetry forbidden in three Euclidean dimensions ($d=3$) could be recovered as a valid lattice symmetry in a higher-dimensional space ($N \> 3$).3 For icosahedral quasicrystals, the minimal embedding dimension required to restore translational periodicity is $N=6$. In this 6-dimensional (6D) "superspace," the structure is a perfectly periodic hypercubic lattice. The physical quasicrystal is realized not as a disordered 3D object, but as a specific, irrational 3D slice (or projection) of this 6D hypercrystal.5

This "superspace" formalism has become the standard model for quasicrystallography, allowing for the precise indexing of diffraction patterns and the refinement of atomic structures.6 However, the success of this mathematical framework raises a disturbing question about the nature of physical reality in these materials. Is the 6D lattice merely a "bookkeeping" device—a convenient parameter space for organizing data—or does it possess a physical reality that governs the material's behavior? Furthermore, recent theoretical developments, often grouped under the "Golden Selection" theory or "Emergence Theory," have pushed this dimensionality even further, positing that the fundamental substrate is not merely 6D, but the 8-dimensional $E\_8$ root lattice, from which 3D reality is projected.8

This report conducts a rigorous investigation into the necessity of these higher-dimensional embeddings. We evaluate the competing hypotheses: the "Intrinsic 3D" view, which argues that local matching rules in physical space are sufficient to describe the structure, versus the "Superspace Realism" view, which argues that the dynamic properties of quasicrystals—specifically phason modes, topological defects, and information-theoretic constraints—are inexplicable without reference to the hyper-dimensional degrees of freedom. We further explore the specific claims of the E8 embedding, analyzing whether the "Golden Selection" provides a necessary unification of geometric frustration and fundamental particle symmetries that a purely 3D or even 6D description cannot accommodate.

## **2\. The Mathematical Necessity: Recovering Integer Indices**

### **2.1 The Failure of 3D Indexing**

To understand the necessity of higher dimensions, one must first confront the failure of 3D crystallography. In a conventional crystal, the diffraction condition is given by the Laue equations, which state that constructive interference occurs at wavevectors $\\mathbf{k}$ equal to reciprocal lattice vectors $\\mathbf{G}$. These vectors are linear combinations of three primitive basis vectors $\\mathbf{b}\_1, \\mathbf{b}\_2, \\mathbf{b}\_3$ with integer coefficients (Miller indices) $h, k, l$:

$$\\mathbf{G} \= h\\mathbf{b}\_1 \+ k\\mathbf{b}\_2 \+ l\\mathbf{b}\_3$$

This integer indexing is the hallmark of translational periodicity. However, in an icosahedral quasicrystal, the diffraction peaks are dense in reciprocal space. To describe the positions of the peaks using basis vectors aligned with the icosahedral symmetry axes, one requires not three, but six basis vectors $\\mathbf{q}\_1, \\dots, \\mathbf{q}\_6$, which point to the vertices of an icosahedron.2  
Any diffraction vector $\\mathbf{Q}$ in the quasicrystal can be expressed as:

$$\\mathbf{Q} \= \\sum\_{i=1}^6 n\_i \\mathbf{q}\_i$$

where $n\_i$ are integers. In 3D space, these six vectors are linearly dependent over the real numbers (since the dimension is 3), but they are linearly independent over the field of rational numbers.10 This linear independence over $\\mathbb{Q}$ is the algebraic signature of a dimension greater than 3\. The rank of the $\\mathbb{Z}$-module generated by the diffraction vectors is 6, implying that the reciprocal space is effectively 6-dimensional projected onto 3D.11

### **2.2 The Superspace Embedding ($N=6$)**

The "Cut-and-Project" (or strip projection) method formalizes this observation. We consider a 6-dimensional periodic lattice $\\Lambda \\subset \\mathbb{R}^6$ (typically the simple hypercubic lattice or the face-centered $D\_6$ lattice).12 The 6D space is decomposed into two orthogonal subspaces: the physical space (or parallel space) $E\_{\\parallel}$ and the perpendicular space (or internal space) $E\_{\\perp}$.

$$\\mathbb{R}^6 \= E\_{\\parallel} \\oplus E\_{\\perp}$$

The physical quasicrystal is the set of points projected onto $E\_{\\parallel}$ from a strip of the 6D lattice. Specifically, a lattice point $\\mathbf{r} \\in \\Lambda$ is projected to $\\mathbf{r}\_{\\parallel} \= P\_{\\parallel} \\mathbf{r}$ if and only if its perpendicular component $\\mathbf{r}\_{\\perp} \= P\_{\\perp} \\mathbf{r}$ falls within a bounded region $W \\subset E\_{\\perp}$ called the "acceptance window" or "atomic surface".4  
Mathematically, the set of atomic positions $\\mathcal{Q}$ is:

$$\\mathcal{Q} \= \\{ P\_{\\parallel} \\mathbf{x} \\mid \\mathbf{x} \\in \\Lambda, P\_{\\perp} \\mathbf{x} \\in W \\}$$  
This formalism restores the fundamental laws of crystallography. The diffraction pattern of the quasicrystal is simply the projection of the diffraction pattern of the 6D lattice. The intensity of the peaks is modulated by the Fourier transform of the window function $W$. Because $W$ is a bounded object in $E\_{\\perp}$, its Fourier transform decays with the perpendicular wavevector $\\mathbf{G}\_{\\perp}$. This explains why the diffraction pattern is not "white noise" (dense everywhere) but consists of bright peaks (where $\\mathbf{G}\_{\\perp}$ is small) and infinitely many dim peaks (where $\\mathbf{G}\_{\\perp}$ is large).2

The 6D embedding is strictly *necessary* to recover a discrete reciprocal lattice with integer indexing. Without it, one is forced to treat the diffraction pattern as a dense set of irrational numbers without a unifying group structure.

### **2.3 Equivalence of Multigrid and Projection**

An alternative 3D-centric approach was proposed by N.G. de Bruijn in 1981: the "Multigrid Method".3 De Bruijn showed that Penrose tilings could be constructed as the dual graphs of a "pentagrid"—five families of parallel lines in the plane. The intersections of these lines determine the location and type of rhombic tiles.  
While this method appears to operate entirely within the lower dimension, de Bruijn himself, along with Kramer and Neri, proved that the Multigrid method is mathematically isomorphic to the Cut-and-Project method.4 The parameters defining the grid shifts in the multigrid method correspond exactly to the translation of the cut through the 5D (for Penrose) or 6D (for icosahedral) unit cell.14  
This equivalence is profound. It implies that even when we use "local" construction methods like grids, we are implicitly manipulating coordinates in a higher-dimensional space. The "grid" is just the shadow of the hyperlattice planes intersecting the physical space. The topology of the tiling—how the tiles connect—is determined by the topology of the 6D lattice.15

## **3\. The Physical Reality of Perpendicular Space: Phasons**

The kinematic description of diffraction proves the mathematical utility of 6D superspace. However, for the embedding to be considered "physically necessary" (ontologically real), the extra dimensions must possess dynamic degrees of freedom that influence the material's energy, entropy, and evolution. This leads us to the concept of **phasons**.

### **3.1 Hydrodynamics and Symmetry Breaking**

In the hydrodynamic theory of crystals, developed by Landau and Lifshitz, the low-energy excitations of a solid are derived from its broken symmetries. A periodic crystal breaks continuous translational symmetry in 3 directions, leading to 3 gapless Goldstone modes known as acoustic phonons (sound waves).16  
Quasicrystals break the continuous translational symmetry of the full 6D superspace. The free energy of the system is invariant under a rigid translation of the 6D hypercrystal:

$$\\mathbf{u} \\to \\mathbf{u} \+ \\mathbf{c}, \\quad \\mathbf{c} \\in \\mathbb{R}^6$$

This 6-component displacement field $\\mathbf{u}(\\mathbf{r})$ decomposes into:

$$\\mathbf{u} \= (\\mathbf{u}\_{\\parallel}, \\mathbf{u}\_{\\perp})$$

* $\\mathbf{u}\_{\\parallel}$: The conventional phonon field (3 modes). This represents the displacement of atoms in physical space.  
* $\\mathbf{u}\_{\\perp}$: The **phason** field (3 modes). This represents the relative displacement of the density waves that comprise the quasicrystal.17

From a purely 3D perspective, a "phason" is a bizarre and non-intuitive rearrangement of atoms. It involves "phason flips"—local jumps of atoms between sites that are energetically nearly degenerate.18 However, from the superspace perspective, a phason is simply a phonon in the perpendicular direction. It is a rigid translation of the cut window $W$ relative to the high-dimensional lattice.20

### **3.2 Phason Strain and Diffraction Shifts**

The physical reality of the phason field is evidenced by its effect on diffraction. If a quasicrystal contains a uniform gradient in the phason field (linear phason strain), the Bragg peaks shift from their ideal positions. The shift $\\Delta \\mathbf{G}\_{\\parallel}$ is proportional to the perpendicular component of the lattice vector $\\mathbf{G}\_{\\perp}$:

$$\\Delta \\mathbf{G}\_{\\parallel} \= \\mathbf{M} \\cdot \\mathbf{G}\_{\\perp}$$

where $\\mathbf{M}$ is the phason strain tensor.21  
This relationship is verified experimentally. In many icosahedral alloys (e.g., $i$-AlCuFe, $i$-AlPdMn), peak shifts are observed that scale linearly with $\\mathbf{G}\_{\\perp}$. A purely 3D theory would have no reason to associate the shift of a peak with its index in a hypothetical 6th dimension. The fact that the physical observable (peak shift) is governed by the "hidden" variable ($\\mathbf{G}\_{\\perp}$) is strong evidence for the structural realism of the superspace.13

### **3.3 Diffuse Scattering: The "Butterfly" Signature**

Beyond static strain, thermal fluctuations of the phason field give rise to Diffuse Scattering (DS) around the Bragg peaks. Hydrodynamic theory predicts that the intensity of Phason Diffuse Scattering (PDS) should decay as $1/q^2$ (where $q$ is the distance from the Bragg peak) but with a specific anisotropy determined by the elastic constants of the 6D lattice.22  
Experimental measurements using synchrotron X-rays and neutrons on high-quality single quasicrystals (e.g., $i$-ZnMgSc) reveal complex, butterfly-shaped diffuse scattering patterns.22 These patterns cannot be explained by standard thermal diffuse scattering (phonons) alone. They are perfectly fitted by the 6D elastic theory, which includes phonon-phason coupling terms.24 The anisotropy of the scattering maps directly to the symmetry of the phason elastic tensor, confirming that the "phason" is a propagating (or diffusive) mode with defined stiffness and energetics.26

### **3.4 Phasons as Channels for Heat and Matter**

Perhaps the most striking evidence for the "reality" of these modes comes from their role in transport. In the mineral fresnoite ($Ba\_2TiSi\_2O\_8$), which possesses an incommensurate structure (a 1D quasicrystal analog), neutron scattering experiments revealed that heat energy propagates through the lattice via phasons.27 Remarkably, these phasons were observed to carry heat faster than the speed of sound (supersonic transport).  
Furthermore, in the growth of decagonal quasicrystals from a liquid melt, real-time imaging has shown that the coalescence of grains involves a rigid rotation facilitated by phason defects.28 The grains adjust their orientation to match the global quasiperiodic order by "eating" phason strain. This implies that the phason is not just a descriptive error term but a dynamic vehicle for reordering matter—a "synthetic dimension" through which the system relaxes.20

## **4\. The Intrinsic 3D Perspective: Matching Rules and Their Limitations**

Given the success of the superspace description, is it possible to dispense with it and describe quasicrystals entirely via 3D mechanisms? This is the program of "Matching Rules."

### **4.1 The Promise of Local Rules**

The discovery of the Penrose tiling was driven by the question of whether aperiodic order could be enforced by local constraints. Penrose discovered that by decorating the edges of tiles (kites and darts) with arrows and requiring that arrows match across shared edges, one could force the tiling to be non-periodic.30  
In 3D, the analogue is the Socolar-Steinhardt tiling. Levine, Steinhardt, and Socolar demonstrated that icosahedral quasicrystals can be constructed from a set of four zonohedra (derived from the 6D hypercube) decorated with 3D matching rules (keys and slots on the faces).31 These rules are "local" in the sense that a tile only "knows" about its immediate neighbors. If such rules exist, then the quasicrystal can be understood as the ground state of a local Hamiltonian (where mismatched faces cost energy), without referencing higher dimensions.

### **4.2 "Weak" vs. "Perfect" Rules: The Crisis of Uniqueness**

A critical distinction exists in tiling theory between "perfect" matching rules and "weak" matching rules.

* **Perfect Rules:** These enforce the condition that *every* tiling satisfying the rules is locally isomorphic to the perfect quasicrystal. No periodic structures are allowed.  
* **Weak Rules:** These allow the perfect quasicrystal but do not strictly exclude periodic approximants or structures with defects that do not violate the local constraints.33

While perfect rules exist for 2D Penrose tilings, the situation in 3D is more ambiguous. Socolar proved that "weak" matching rules exist for any rotationally symmetric tiling (including icosahedral).33 However, finding *perfect* local rules for generic 3D icosahedral phases that can be realistically implemented by atomic potentials remains an open challenge.6 The "alternation condition" (a parity rule for faces) is a form of rule, but it is often insufficient to banish all periodic competitors.6

### **4.3 The Non-Locality of Growth**

The most severe blow to the "purely 3D" view is the Growth Problem. Even if perfect matching rules exist, they do not guarantee that a defect-free quasicrystal can be grown, atom-by-atom, using only local information.  
In a periodic crystal, if you place a unit cell, you know exactly where the next one goes forever. In a quasicrystal, placing a tile locally according to matching rules can lead to a "dead end" or a "decapod" defect—a configuration that cannot be extended further without violating the rules.34 To avoid these dead ends, the system effectively needs to "look ahead" or possess non-local information about the global topology.  
This non-locality paradox suggests that the information required to build the structure is not contained in the 3D unit cell alone. In the superspace formalism, this information is global—it is encoded in the irrational slope of the cut. The fact that real quasicrystals grow with high perfection (often better than periodic crystals) suggests that nature has access to this "non-local" information, or that the stabilization mechanism is fundamentally different (e.g., entropic stabilization via the Random Tiling Model).36  
The Random Tiling Model (Henley) argues that the "perfect" quasicrystal is an idealization; real quasicrystals are stabilized by the entropy of phason flips.37 This model accepts the phason as a fundamental thermodynamic degree of freedom, implicitly acknowledging the extra dimensional phase space, even if it rejects the rigid "energy-only" matching rule picture.

## **5\. The Golden Selection and E8: The Deepest Embedding**

While the 6D framework is the standard for crystallography, a deeper theoretical current—often termed "Golden Selection" or "Emergence Theory"—posits that the relevant embedding is not 6D, but 8D. This view, championed by researchers like Klee Irwin, Fang Fang, and mathematical physicists studying the Elser-Sloane quasicrystal, suggests that 3D quasicrystals are shadows of the $E\_8$ lattice.8

### **5.1 The E8 $\\to$ 4D $\\to$ 3D Cascade**

Standard icosahedral quasicrystals are projections of the $D\_6$ lattice (face-centered hypercubic). However, the $E\_8$ lattice—the unique even, unimodular lattice in 8 dimensions and the densest sphere packing in 8D—offers a more unified geometry.  
The "Golden Selection" theory proposes a specific projection chain:

1. **E8 to 4D:** A projection of the $E\_8$ lattice onto a 4D subspace using a specific orientation (often related to the Hopf fibration) yields the **Elser-Sloane Quasicrystal**.38 This 4D structure possesses $H\_4$ symmetry (the symmetry of the 600-cell polytope) and is built from 600-cells.39  
2. **4D to 3D:** A slice of the 4D Elser-Sloane quasicrystal yields a 3D structure. The fundamental unit of the 600-cell is the tetrahedron. Thus, the 3D projection is a packing of tetrahedra. In 3D, regular tetrahedra cannot tile space (geometric frustration). However, they pack perfectly in the 4D 600-cell. The 3D quasicrystal (e.g., the **Fibonacci Icosagrid** or **Quasicrystalline Spin Network**) captures the "shadow" of this perfect 4D packing.40

### **5.2 Physical Necessity of E8: Unification and Code**

Why is this 8D embedding "necessary" rather than just a curiosity? The arguments are twofold:

1. **Fundamental Particle Unification:** The $E\_8$ Lie algebra contains the symmetries of the Standard Model of particle physics ($SU(3) \\times SU(2) \\times U(1)$) and potential Grand Unified Theories (GUTs) like $E\_6$ or $SO(10)$.41 "Emergence Theory" posits that the geometry of spacetime (the quasicrystal) and the geometry of internal gauge symmetries (particles) are unified in the $E\_8$ lattice. A phonon in the $E\_8$ lattice could manifest as a graviton, while specific local rotational defects could manifest as electrons or quarks.43 In this view, the 8D embedding is ontologically primary; the 3D world is merely the "screen" where these high-dimensional geometric interactions are measured.  
2. **Information Density (The Code Theoretic Axiom):** Klee Irwin and colleagues argue that reality is fundamentally information-theoretic.45 The $E\_8$ lattice is the most efficient information packing structure in 8D. Its projection to 3D via the Golden Ratio ($\\phi$) creates a "code" (the quasicrystal) that is maximally efficient and robust against errors.47 This "Code Theoretic Axiom" suggests that the laws of physics are not arbitrary but are derived from the syntactical rules of this high-dimensional geometric language. The non-locality of quantum mechanics is reinterpreted as the natural non-locality of the code updating across the global quasicrystalline network.48

### **5.3 The "Fibonacci Icosagrid" (FIG)**

Recent work has explicitly constructed the **Fibonacci Icosagrid (FIG)** as a 3D quasicrystal that maps directly to the $E\_8$ lattice.40 The FIG is formed by the intersection of 5 sets of planar grids (like the de Bruijn pentagrid but in 3D). The spacing of these grids follows the Fibonacci sequence. The vertices of the FIG correspond to specific projections of the $E\_8$ roots. This provides a concrete mathematical bridge between the 3D "grid" view and the 8D "lattice" view, reinforcing the idea that the 3D structure is an encoding of 8D information.

## **6\. Synthesis: Ontological Status and "Synthetic Dimensions"**

### **6.1 Mathematical Convenience or Physical Reality?**

We return to the core question: Is the higher dimension *real*?

* **The Case for Convenience:** One could argue that the 6D indices are just quantum numbers, like spin or isospin. We don't say an electron lives in "spin space"; we say it has an internal property. Similarly, "phason coordinate" could be viewed as an internal state of the 3D material.  
* **The Case for Structural Realism:** However, unlike abstract quantum numbers, the phason coordinate has a *metric*. It has elastic stiffness ($K\_{phason}$), it transports energy (heat), and it governs topology (defects). A dislocation in a quasicrystal is a topological defect that cannot be fully characterized without its 6D Burgers vector. The defect "unwinds" or resolves only in the higher dimension.37 If the topology of the system requires 6D to be well-defined, then in a structural realist framework, the 6D structure is real.

### **6.2 The "Synthetic Dimension" Compromise**

A modern synthesis in condensed matter physics views phasons as "synthetic dimensions." In phason-engineered metamaterials, researchers have experimentally demonstrated that a 1D quasicrystal can exhibit topological properties (like the Quantum Hall Effect) that belong to a 2D system, by treating the phason phase as the second dimension ($k\_y$).20  
This blurs the boundary between "real" and "mathematical." If a 3D quasicrystal exhibits 4D or 6D topological invariants (Chern numbers) because of its phasons, then for all physical purposes—transport, conductivity, edge states—it is a higher-dimensional object folded into 3D.

## **7\. Conclusion**

The investigation into the dimensionality of quasicrystals yields a nuanced but decisive conclusion: **The higher-dimensional embedding is physically necessary to fully describe and understand the system.**

1. **Descriptive Necessity:** The 6D embedding is the only rigorous way to index the diffraction pattern and define the lattice structure (the "where"). Purely 3D descriptions fail to capture the rank-6 module structure of the reciprocal lattice.  
2. **Dynamic Necessity:** The dynamics of the system—specifically **phasons**—are the Goldstone modes of the broken symmetry in the higher dimension. The experimental reality of phason strain, diffuse scattering, and phason-assisted heat transport confirms that the "perpendicular" degrees of freedom store energy and facilitate motion. A theory without them is incomplete.  
3. **Ontological Necessity (E8/Golden Selection):** While more speculative, the E8 framework offers a unification of the crystallographic anomaly with fundamental particle physics. If the "Code Theoretic" view holds, the 3D quasicrystal is not just a material but a projection of a fundamental 8D reality.

The 3D quasicrystal can be *observed* in 3D, but its *identity*—its symmetry, its defects, and its vibrations—is inextricably rooted in a higher-dimensional geometry. To describe it solely in 3D is to mistake the shadow for the object.

---

### **Data Tables**

#### **Table 1: Comparison of Quasicrystal Description Frameworks**

| Feature | Intrinsic 3D (Matching Rules) | Standard Superspace (6D) | Golden Selection (E8 / 8D) |
| :---- | :---- | :---- | :---- |
| **Primary Object** | Set of Prototiles (e.g., Zonohedra) | Periodic Hyperlattice ($D\_6$ or Hypercubic) | $E\_8$ Root Lattice |
| **Mechanism** | Local Energy Minimization (Edge Matching) | Cut-and-Project (Global Topology) | Projection to 4D $\\to$ 3D (Hopf Map) |
| **Defects** | Mismatches, Decapods, Dead Ends | Phason Strain, 6D Dislocations | Topological Defects in Spin Network |
| **Phason Nature** | Discrete Configuration Flip / "Mistake" | Hydrodynamic Goldstone Mode ($u\_{\\perp}$) | Quasiparticle / Code Update |
| **Diffraction** | Fourier Transform of Tiling | Projection of 6D Reciprocal Lattice | Unified Geometry of Spacetime & Gauge |
| **Primary Failure** | **Growth Problem:** Non-locality of rules | **Abstractness:** "Where are the atoms?" | **Speculation:** Theoretical, not yet standard |
| **Status** | Theoretical capability; experimentally difficult | **Standard Scientific Model** | **Vanguard / Theoretical Physics** |

#### **Table 2: Physical Evidence for Higher Dimensions (Phasons)**

| Phenomenon | Observation | Superspace Interpretation | 3D Interpretation Difficulty |
| :---- | :---- | :---- | :---- |
| **Diffraction Indexing** | Peaks at $\\sum n\_i q\_i$ ($i=1..6$) | Integer indices in 6D reciprocal lattice | Requires dense set of irrational numbers; no group structure. |
| **Peak Shifts** | Shift $\\propto \\mathbf{G}\_{\\perp}$ | Linear elastic strain in perpendicular space ($E\_{\\perp}$) | Requires ad-hoc "phason strain" parameter without geometric origin. |
| **Diffuse Scattering** | Anisotropic "Butterfly" shapes | Thermal fluctuations of 6D elastic field ($u\_{\\perp}$) | Hard to explain specific anisotropy without 6D elastic tensor. |
| **Heat Transport** | Supersonic heat flow in fresnoite | Phasons act as additional, faster channels | Impossible; phonons limited by sound speed. |
| **Grain Coalescence** | Rigid rotation of grains in melt | Phason-assisted defect motion | Requires massive coordinated atomic jumps; statistically unlikely. |

### **References**

1

#### **Referências citadas**

1. Quasicrystal \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Quasicrystal](https://en.wikipedia.org/wiki/Quasicrystal)  
2. Introduction to higher dimensional description of quasicrystal structures \- Tohoku University, acessado em novembro 28, 2025, [https://www.tfc.tohoku.ac.jp/wp-content/uploads/2019/06/2019QSC\_tutorial\_HiroyukiTakakura\_s.pdf](https://www.tfc.tohoku.ac.jp/wp-content/uploads/2019/06/2019QSC_tutorial_HiroyukiTakakura_s.pdf)  
3. Draft – 10/26/13 \- Cornell Mathematics, acessado em novembro 28, 2025, [https://pi.math.cornell.edu/\~klindsey/DraftGOL.pdf](https://pi.math.cornell.edu/~klindsey/DraftGOL.pdf)  
4. Penrose tiling \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Penrose\_tiling](https://en.wikipedia.org/wiki/Penrose_tiling)  
5. Dynamical Systems Seminar- On Penrose tilings and tiling dynamical systems: I | The Department of Mathematics | Columbian College of Arts & Sciences, acessado em novembro 28, 2025, [https://math.columbian.gwu.edu/dynamical-systems-seminar-penrose-tilings-and-tiling-dynamical-systems-i](https://math.columbian.gwu.edu/dynamical-systems-seminar-penrose-tilings-and-tiling-dynamical-systems-i)  
6. Crystallography of Quasicrystals: Concepts, Methods and Structures (Springer Series in Materials Science), acessado em novembro 28, 2025, [https://www.xray.cz/kryst/kvazi.pdf](https://www.xray.cz/kryst/kvazi.pdf)  
7. PyQCstrc.ico: a computing package for structural modelling of icosahedral quasicrystals \- PMC \- NIH, acessado em novembro 28, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8366420/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8366420/)  
8. A Deep Link Between 3D and 8D (VISUALIZATION) \- Quantum Gravity Research, acessado em novembro 28, 2025, [https://quantumgravityresearch.org/portfolio/a-deep-link-between-3d-and-8d/](https://quantumgravityresearch.org/portfolio/a-deep-link-between-3d-and-8d/)  
9. (PDF) Eight Things a First Principles Theory of Everything Should Possess \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/316170495\_Eight\_Things\_a\_First\_Principles\_Theory\_of\_Everything\_Should\_Possess](https://www.researchgate.net/publication/316170495_Eight_Things_a_First_Principles_Theory_of_Everything_Should_Possess)  
10. LETTER TO THE EDITOR: Quasiperiodic icosahedral tilings from the six-dimensional bcc lattice \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/253864587\_LETTER\_TO\_THE\_EDITOR\_Quasiperiodic\_icosahedral\_tilings\_from\_the\_six-dimensional\_bcc\_lattice](https://www.researchgate.net/publication/253864587_LETTER_TO_THE_EDITOR_Quasiperiodic_icosahedral_tilings_from_the_six-dimensional_bcc_lattice)  
11. by N.G. de Bruijn, acessado em novembro 28, 2025, [https://new.math.uiuc.edu/oldnew/quasicrystals/papers/debruijnFourier.pdf](https://new.math.uiuc.edu/oldnew/quasicrystals/papers/debruijnFourier.pdf)  
12. Icosahedral Mesh/Polyhedron \- Emergent Mind, acessado em novembro 28, 2025, [https://www.emergentmind.com/topics/icosahedral-mesh-polyhedron](https://www.emergentmind.com/topics/icosahedral-mesh-polyhedron)  
13. Insight into the structure of decagonite – the extraterrestrial decagonal quasicrystal \- PMC, acessado em novembro 28, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7792992/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7792992/)  
14. Algebraic theory of Penrose's non-periodic \- Brown University, acessado em novembro 28, 2025, [https://www.math.brown.edu/\~res/M272/pentagrid.pdf](https://www.math.brown.edu/~res/M272/pentagrid.pdf)  
15. The Empire Problem in Penrose Tilings \- Computer Science, acessado em novembro 28, 2025, [https://www.cs.williams.edu/\~bailey/06le.pdf](https://www.cs.williams.edu/~bailey/06le.pdf)  
16. Phason \- Wikipedia, acessado em novembro 28, 2025, [https://en.wikipedia.org/wiki/Phason](https://en.wikipedia.org/wiki/Phason)  
17. Hydrodynamics of icosahedral quasicrystals, acessado em novembro 28, 2025, [https://www.to.infn.it/\~mussod/PhysRevB.32.7444.pdf](https://www.to.infn.it/~mussod/PhysRevB.32.7444.pdf)  
18. Structure and phason energetics of Al-Co decagonal phases, acessado em novembro 28, 2025, [https://euler.phys.cmu.edu/widom/pubs/PDF/philmagA\_1998\_p593.pdf](https://euler.phys.cmu.edu/widom/pubs/PDF/philmagA_1998_p593.pdf)  
19. University of Groningen Ordering and low energy excitations in, acessado em novembro 28, 2025, [https://research.rug.nl/files/130266890/03\_c3.pdf](https://research.rug.nl/files/130266890/03_c3.pdf)  
20. Coexistence of 1D and 2D topology and genesis of Dirac cones in the chiral Aubry-André model \- arXiv, acessado em novembro 28, 2025, [https://arxiv.org/html/2401.03541v2](https://arxiv.org/html/2401.03541v2)  
21. Varied linear phason strain and its induced domain structure in quasicrystalline precipitates of Zr–Al–Ni–Cu–Nb bulk metallic glass matrix composites | Journal of Materials Research \- Cambridge University Press & Assessment, acessado em novembro 28, 2025, [https://www.cambridge.org/core/journals/journal-of-materials-research/article/varied-linear-phason-strain-and-its-induced-domain-structure-in-quasicrystalline-precipitates-of-zralnicunb-bulk-metallic-glass-matrix-composites/B8FCF1F6F16DCD2099CAF77E97AC2CC2](https://www.cambridge.org/core/journals/journal-of-materials-research/article/varied-linear-phason-strain-and-its-induced-domain-structure-in-quasicrystalline-precipitates-of-zralnicunb-bulk-metallic-glass-matrix-composites/B8FCF1F6F16DCD2099CAF77E97AC2CC2)  
22. Atomic structure and phason modes of the Sc–Zn icosahedral quasicrystal \- IUCr Journals, acessado em novembro 28, 2025, [https://journals.iucr.org/m/issues/2016/04/00/gq5006/](https://journals.iucr.org/m/issues/2016/04/00/gq5006/)  
23. Dynamics of Long-wavelength Phason Fluctuations in the Icosahedral Quasicrystal i-AlPdMn \- European Synchrotron Radiation Facility (ESRF), acessado em novembro 28, 2025, [https://www.esrf.fr/UsersAndScience/Publications/Highlights/2003/XASMS/XASMS10](https://www.esrf.fr/UsersAndScience/Publications/Highlights/2003/XASMS/XASMS10)  
24. Experimental observation of phonon-strain and phason-strain relaxation... | Download Scientific Diagram \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/figure/Experimental-observation-of-phonon-strain-and-phason-strain-relaxation-following-the\_fig1\_6145602](https://www.researchgate.net/figure/Experimental-observation-of-phonon-strain-and-phason-strain-relaxation-following-the_fig1_6145602)  
25. arXiv:cond-mat/0401353v3 \[cond-mat.mtrl-sci\] 17 Jun 2005, acessado em novembro 28, 2025, [https://arxiv.org/pdf/cond-mat/0401353](https://arxiv.org/pdf/cond-mat/0401353)  
26. Full article: Direct experimental evidence of phonon–phason coupling in an Al-Pd-Mn icosahedral quasicrystal \- Taylor & Francis Online, acessado em novembro 28, 2025, [https://www.tandfonline.com/doi/full/10.1080/14786435.2022.2052376](https://www.tandfonline.com/doi/full/10.1080/14786435.2022.2052376)  
27. Supersonic propagation of lattice energy by phasons in fresnoite \- PMC \- NIH, acessado em novembro 28, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5940883/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5940883/)  
28. Formation of a single quasicrystal upon collision of multiple grains \- PMC \- NIH, acessado em novembro 28, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8505427/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8505427/)  
29. arXiv:2106.14074v1 \[cond-mat.mtrl-sci\] 26 Jun 2021, acessado em novembro 28, 2025, [https://arxiv.org/pdf/2106.14074](https://arxiv.org/pdf/2106.14074)  
30. Algebraic theory of non-periodic tilings of the plane by two simple building blocks : a square and a rhombus \- Pure, acessado em novembro 28, 2025, [https://pure.tue.nl/ws/files/4269555/253166.pdf](https://pure.tue.nl/ws/files/4269555/253166.pdf)  
31. Local rules for quasicrystals, acessado em novembro 28, 2025, [http://jetp.ras.ru/cgi-bin/dn/e\_066\_05\_1046.pdf](http://jetp.ras.ru/cgi-bin/dn/e_066_05_1046.pdf)  
32. Quasicrystals I: Definition and Structure \- Paul J. Steinhardt, acessado em novembro 28, 2025, [https://paulsteinhardt.org/wp-content/uploads/2020/10/QuasiPartI.pdf](https://paulsteinhardt.org/wp-content/uploads/2020/10/QuasiPartI.pdf)  
33. Weak Matching Rules for Quasicrystals \- Project Euclid, acessado em novembro 28, 2025, [https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-129/issue-3/Weak-matching-rules-for-quasicrystals/cmp/1104180853.pdf](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-129/issue-3/Weak-matching-rules-for-quasicrystals/cmp/1104180853.pdf)  
34. Quasicrystals. II. Unit-cell configurations \- Paul J. Steinhardt, acessado em novembro 28, 2025, [https://paulsteinhardt.org/wp-content/uploads/2020/10/QuasiPartII.pdf](https://paulsteinhardt.org/wp-content/uploads/2020/10/QuasiPartII.pdf)  
35. Decapods: Defects in Quasicrystals \- Justin Kulp, acessado em novembro 28, 2025, [https://justinkulp.com/wp-content/uploads/2022/10/DecapodPoster.pdf](https://justinkulp.com/wp-content/uploads/2022/10/DecapodPoster.pdf)  
36. Quasicrystals | Series on Directions in Condensed Matter Physics, acessado em novembro 28, 2025, [https://www.worldscientific.com/worldscibooks/10.1142/1304](https://www.worldscientific.com/worldscibooks/10.1142/1304)  
37. Phonons, phasons and dislocations in quasicrystals \- Paul J. Steinhardt, acessado em novembro 28, 2025, [https://paulsteinhardt.org/wp-content/uploads/2020/10/PhoPhaDef.pdf](https://paulsteinhardt.org/wp-content/uploads/2020/10/PhoPhaDef.pdf)  
38. The-E8-lattice-and-quasicrystals.pdf \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/profile/Jean-Francois-Sadoc/publication/243298250\_The\_E8\_lattice\_and\_quasicrystals/links/5ac084ebaca27222c759d102/The-E8-lattice-and-quasicrystals.pdf](https://www.researchgate.net/profile/Jean-Francois-Sadoc/publication/243298250_The_E8_lattice_and_quasicrystals/links/5ac084ebaca27222c759d102/The-E8-lattice-and-quasicrystals.pdf)  
39. (PDF) A highly symmetric four-dimensional quasicrystal \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/230915931\_A\_highly\_symmetric\_four-dimensional\_quasicrystal](https://www.researchgate.net/publication/230915931_A_highly_symmetric_four-dimensional_quasicrystal)  
40. From the Fibonacci Icosagrid to E8 (Part I): The Fibonacci Icosagrid, an H3 Quasicrystal, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/377856840\_From\_the\_Fibonacci\_Icosagrid\_to\_E8\_Part\_I\_The\_Fibonacci\_Icosagrid\_an\_H3\_Quasicrystal](https://www.researchgate.net/publication/377856840_From_the_Fibonacci_Icosagrid_to_E8_Part_I_The_Fibonacci_Icosagrid_an_H3_Quasicrystal)  
41. quasicrystalline spin foam with matter: definitions \- arXiv, acessado em novembro 28, 2025, [https://arxiv.org/pdf/2306.01964](https://arxiv.org/pdf/2306.01964)  
42. (PDF) Quasicrystalline Spin Foam with Matter: Definitions and Examples \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/371310903\_Quasicrystalline\_Spin\_Foam\_with\_Matter\_Definitions\_and\_Examples](https://www.researchgate.net/publication/371310903_Quasicrystalline_Spin_Foam_with_Matter_Definitions_and_Examples)  
43. Toward the Unification of Physics and Number Theory \- Quantum Gravity Research, acessado em novembro 28, 2025, [https://quantumgravityresearch.org/wp-content/uploads/2017/02/Toward-the-Unification-of-Physics2-1.pdf](https://quantumgravityresearch.org/wp-content/uploads/2017/02/Toward-the-Unification-of-Physics2-1.pdf)  
44. Emergence of an Aperiodic Dirichlet Space from the Tetrahedral Units of an Icosahedral Internal Space \- MDPI, acessado em novembro 28, 2025, [https://www.mdpi.com/2227-7390/5/2/29](https://www.mdpi.com/2227-7390/5/2/29)  
45. The Self-Simulation Hypothesis Interpretation of Quantum Mechanics \- PMC \- NIH, acessado em novembro 28, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7516678/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7516678/)  
46. (PDF) The Code Theoretic Axiom The Third Ontology \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/320741140\_The\_Code\_Theoretic\_Axiom\_The\_Third\_Ontology](https://www.researchgate.net/publication/320741140_The_Code_Theoretic_Axiom_The_Third_Ontology)  
47. katieniedz (u/Neat\_Pound\_9029) \- Reddit, acessado em novembro 28, 2025, [https://www.reddit.com/user/Neat\_Pound\_9029/](https://www.reddit.com/user/Neat_Pound_9029/)  
48. The Code Theoretic Axiom 1 Introduction 2 Is Reality Information Theoretic? \- Quantum Gravity Research, acessado em novembro 28, 2025, [https://www.quantumgravityresearch.org/wp-content/uploads/2019/07/The-Code-Theoretic-Axiom-20190318.pdf](https://www.quantumgravityresearch.org/wp-content/uploads/2019/07/The-Code-Theoretic-Axiom-20190318.pdf)  
49. Revealing the Boundary Weyl Physics of the Four-Dimensional Hall Effect via Phason Engineering in Metamaterials | Request PDF \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/355421938\_Revealing\_the\_Boundary\_Weyl\_Physics\_of\_the\_Four-Dimensional\_Hall\_Effect\_via\_Phason\_Engineering\_in\_Metamaterials](https://www.researchgate.net/publication/355421938_Revealing_the_Boundary_Weyl_Physics_of_the_Four-Dimensional_Hall_Effect_via_Phason_Engineering_in_Metamaterials)  
50. Tiling Spaces and the Expanding Universe: Bridging Quantum Mechanics and Cosmology, acessado em novembro 28, 2025, [https://arxiv.org/html/2407.14520v2](https://arxiv.org/html/2407.14520v2)  
51. The DiSCovery of QuaSiCrySTalS \- Nobel Prize, acessado em novembro 28, 2025, [https://www.nobelprize.org/uploads/2018/06/advanced-chemistryprize2011.pdf](https://www.nobelprize.org/uploads/2018/06/advanced-chemistryprize2011.pdf)  
52. The Quasicrystalline Nature of Consciousness in the Universe \- Quantum Gravity Research, acessado em novembro 28, 2025, [https://quantumgravityresearch.org/wp-content/uploads/2019/05/2016-Presentation-The-Quasicrystalline-nature-of-consciousness-in-the-universe-Irwin-SAND-conference.pdf](https://quantumgravityresearch.org/wp-content/uploads/2019/05/2016-Presentation-The-Quasicrystalline-nature-of-consciousness-in-the-universe-Irwin-SAND-conference.pdf)  
53. Quasicrystalline compactification \- Harvard DASH, acessado em novembro 28, 2025, [https://dash.harvard.edu/bitstreams/718188dc-0e1f-4529-bb1b-ed990d897e37/download](https://dash.harvard.edu/bitstreams/718188dc-0e1f-4529-bb1b-ed990d897e37/download)  
54. Michael B. Schulz: Research Interests \- String Theory Compactifications, acessado em novembro 28, 2025, [https://www.brynmawr.edu/inside/academic-information/departments-programs/physics/faculty-staff/michael-b-schulz/michael-b-schulz-research-interests-string-theory-compactifications](https://www.brynmawr.edu/inside/academic-information/departments-programs/physics/faculty-staff/michael-b-schulz/michael-b-schulz-research-interests-string-theory-compactifications)  
55. The birth of E8 out of the spinors of the icosahedron \- PMC \- PubMed Central, acessado em novembro 28, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4786034/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4786034/)  
56. PDF hosted at the Radboud Repository of the Radboud University, acessado em novembro 28, 2025, [https://repository.ubn.ru.nl/bitstream/handle/2066/28029/28029\_\_\_.PDF](https://repository.ubn.ru.nl/bitstream/handle/2066/28029/28029___.PDF)  
57. Quasicrystalline Ground States Without Matching Rules Abstract, acessado em novembro 28, 2025, [https://www.math.uni-bielefeld.de/\~gaehler/papers/cluster95.pdf](https://www.math.uni-bielefeld.de/~gaehler/papers/cluster95.pdf)  
58. Looking for alternatives to the superspace description of icosahedral quasicrystals \- PMC, acessado em novembro 28, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6364603/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6364603/)  
59. Effective field theory for quasicrystals and phasons dynamics (Journal Article) | OSTI.GOV, acessado em novembro 28, 2025, [https://www.osti.gov/biblio/1702449](https://www.osti.gov/biblio/1702449)  
60. Entropic formation of a thermodynamically stable colloidal quasicrystal with negligible phason strain | PNAS, acessado em novembro 28, 2025, [https://www.pnas.org/doi/10.1073/pnas.2011799118](https://www.pnas.org/doi/10.1073/pnas.2011799118)  
61. Diffuse scattering and phasons in the i-Zn-Mg-Sc phase and its 1/1 approximant \- IUCr Journals, acessado em novembro 28, 2025, [https://journals.iucr.org/paper?a32061](https://journals.iucr.org/paper?a32061)  
62. Emergence Theory Overview \- Quantum Gravity Research, acessado em novembro 28, 2025, [https://quantumgravityresearch.org/lay-person-overview/](https://quantumgravityresearch.org/lay-person-overview/)  
63. arXiv:hep-th/9708009v1 4 Aug 1997, acessado em novembro 28, 2025, [https://arxiv.org/pdf/hep-th/9708009](https://arxiv.org/pdf/hep-th/9708009)  
64. Aperiodic crystals and superspace concepts \- SciSpace, acessado em novembro 28, 2025, [https://scispace.com/pdf/aperiodic-crystals-and-superspace-concepts-2a3gn53oaf.pdf](https://scispace.com/pdf/aperiodic-crystals-and-superspace-concepts-2a3gn53oaf.pdf)  
65. About \- Klee Irwin Emergence Theory \- WordPress.com, acessado em novembro 28, 2025, [https://kleeirwinresearch.wordpress.com/about/](https://kleeirwinresearch.wordpress.com/about/)  
66. arXiv:cond-mat/9903010v1 \[cond-mat.mtrl-sci\] 28 Feb 1999, acessado em novembro 28, 2025, [https://arxiv.org/pdf/cond-mat/9903010](https://arxiv.org/pdf/cond-mat/9903010)  
67. Contents \- arXiv, acessado em novembro 28, 2025, [https://arxiv.org/html/2502.19468v1](https://arxiv.org/html/2502.19468v1)  
68. (PDF) The E8 lattice and quasicrystals \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/publication/243298250\_The\_E8\_lattice\_and\_quasicrystals](https://www.researchgate.net/publication/243298250_The_E8_lattice_and_quasicrystals)  
69. The Coxeter-Dynkin diagram of E 8 \- ResearchGate, acessado em novembro 28, 2025, [https://www.researchgate.net/figure/The-Coxeter-Dynkin-diagram-of-E-8\_fig4\_231028701](https://www.researchgate.net/figure/The-Coxeter-Dynkin-diagram-of-E-8_fig4_231028701)  
70. Is a phason a Goldstone mode? \- Physics Stack Exchange, acessado em novembro 28, 2025, [https://physics.stackexchange.com/questions/252035/is-a-phason-a-goldstone-mode](https://physics.stackexchange.com/questions/252035/is-a-phason-a-goldstone-mode)  
71. Space-Dependent Symmetries and Fractons \- Frontiers, acessado em novembro 28, 2025, [https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2021.792621/full](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2021.792621/full)  
72. The discrete curvature transformation, shown in the 3-space of He4, acessado em novembro 28, 2025, [https://www.researchgate.net/figure/The-discrete-curvature-transformation-shown-in-the-3-space-of-He4-a-the-initial\_fig4\_325399082](https://www.researchgate.net/figure/The-discrete-curvature-transformation-shown-in-the-3-space-of-He4-a-the-initial_fig4_325399082)