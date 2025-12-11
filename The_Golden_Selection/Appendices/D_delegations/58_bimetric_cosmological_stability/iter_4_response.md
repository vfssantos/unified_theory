Here’s a cleaned-up, consistently formatted version of your text, with LaTeX-style math and fixed artifacts.

---

I’ll tell you the punchline first, then show the machinery.

### Short answer

From the information we have
((D_6 \to H_3) quasicrystal, standard quasicrystal elasticity, and analog-gravity mapping), we can derive:

* the Hassan–Rosen (HR) form of the interaction potential on homogeneous backgrounds;
* the exchange symmetry constraint
  [
  M_g = M_f, \qquad \beta_n = \beta_{4-n},
  ]
* and, if we additionally impose a *Golden vacuum* at (r = \varphi, \varphi^{-1}) in the symmetric branch, the linear relation
  [
  \beta_0 - 3 \beta_2 = \sqrt{5},\beta_1
  ]
  (up to overall normalization).

However:

* The actual numerical values
  [
  \beta_0 \approx -0.857, \qquad \beta_1 \approx 0.958, \qquad \beta_2 = -1,
  ]
  do **not** follow uniquely from (D_6) elasticity alone.

They require additional GS input:

* the choice of **ghost-free HR potential** (linear in the elementary symmetric polynomials (e_n));
* (E_\parallel \leftrightarrow E_\perp) symmetry;
* and **Axiom 0 / Golden vacuum** (roots (r = \pm 1, \varphi, \varphi^{-1})).

So the status is:

> **“Constrained but not unique.”**

(D_6) geometry + symmetry explain **why** the (\beta)’s sit in a small subspace (exchange symmetry + golden linear relation), but **not** their precise values; those are still ansatz-level, tied to the choice of variational free-energy functional rather than derivable from the lattice alone.

Below I’ll go through:

1. Elastic invariants (up to cubic order) for icosahedral quasicrystals with phonons + phasons.
2. Emergent metrics from the (D_6) embedding.
3. How the non-derivative HR-like potential arises on homogeneous backgrounds and how symmetries constrain (\beta_n).
4. How the *Golden vacuum* fixes a linear relation among (\beta)’s.
5. Where the derivation stops, and the minimal extra assumptions needed to land on the current GS (\beta)’s.
6. JSON + code artifacts at the end.

---

## 1. Quasicrystal elasticity: invariants and symmetries

### 1.1 Standard elastic theory for icosahedral quasicrystals

For an icosahedral quasicrystal, you have two displacement fields:

* **phonons** (u_i(x)) in physical space (E_\parallel),
* **phasons** (w_i(x)) in perpendicular space (E_\perp).

The generalized small-strain tensors (in the Steinhardt–Lubensky–Socolar / Fan / Trebin formalism)(^*) are
[
\eta^{u}*{ij} = \frac{1}{2}\left(\partial_i u_j + \partial_j u_i\right), \qquad
\eta^{w}*{ij} = \frac{1}{2}\left(\partial_i w_j + \partial_j w_i\right).
]

Linear (quadratic) elasticity for icosahedral quasicrystals takes the form
[
F_2
= \frac{1}{2} C^{uu}*{ijkl},\eta^{u}*{ij}\eta^{u}_{kl}

* \frac{1}{2} C^{ww}*{ijkl},\eta^{w}*{ij}\eta^{w}_{kl}
* C^{uw}*{ijkl},\eta^{u}*{ij}\eta^{w}_{kl},
  ]
  with icosahedral symmetry strongly reducing the number of independent elastic constants.

Ricker, Bachteler & Trebin (2001) show that the icosahedral case has **five** independent linear elastic constants, usually denoted (\mu_1,\dots,\mu_5): two phononic, two phasonic, and one phonon–phason coupling constant (\mu_3).

In particular, *isotropic phonon elasticity in thermal equilibrium* implies
[
\mu_3 = 0,
]
i.e. **decoupled phonon–phason elasticity** to leading order.

That’s exactly the structural content of your GS assumption
[
T_u = T_w, \qquad C \approx 0,
]
with (T_u, T_w) the phonon / phason stiffnesses and (C) the coupling tensor.

**Derived vs assumed:**

* Decoupling (C \approx 0) is *not generic* but is *well-motivated* by isotropic icosahedral elasticity.
* Equality (T_u = T_w) is stronger: quasicrystal elasticity only requires both phonon and phason sectors to be isotropic in their own 3D spaces, not identical. That equality is a **GS symmetry assumption**, plausibly motivated by the underlying (D_6) root geometry and (E_\parallel \leftrightarrow E_\perp) exchange, but not enforced by quasicrystal elasticity alone.

---

### 1.2 Third-order (cubic) invariants

For nonlinear elasticity, Ricker & Trebin (2002) explicitly classify the **third-order strain invariants** for icosahedral quasicrystals, including phason strain:

* There are **20 independent** third-order elastic constants.

Invariants are grouped as:

* 4 of type (uuu) (pure phonon cubic),
* 4 of type (uuw),
* 7 of type (uww),
* 5 of type (www),

for a total of 20.

Schematically, in a compact notation:

* phonon-only invariants:
  [
  I^{(1)}*{uuu} \sim (\operatorname{Tr}\eta^u)^3,\quad
  I^{(2)}*{uuu} \sim (\operatorname{Tr}\eta^u),\operatorname{Tr}\big[(\eta^u)^2\big],\quad
  I^{(3)}_{uuu} \sim \operatorname{Tr}\big[(\eta^u)^3\big],
  ]
  plus a fourth icosahedral anisotropic combination;

* phason-only invariants (I^{(i)}_{www}) are analogous with (\eta^w);

* mixed invariants:
  [
  I^{(i)}_{uuw} \sim (\operatorname{Tr}\eta^u)^2,\operatorname{Tr}\eta^w,\quad
  \operatorname{Tr}\big[(\eta^u)^2\big]\operatorname{Tr}\eta^w,\quad
  \operatorname{Tr}(\eta^u\eta^w),\operatorname{Tr}\eta^u,\dots
  ]
  plus the 7 (uww) combinations where (u) and (w) are interchanged.

All are chosen to be invariant under the **icosahedral rotation group** in 3D space ((H_3) symmetry).

---

### 1.3 Isotropic long-wavelength limit and (E_\parallel \leftrightarrow E_\perp)

In the **GS regime** we care about:

* long-wavelength, almost homogeneous deformations (cosmology: FRW);
* approximate (E_\parallel \leftrightarrow E_\perp) exchange symmetry inherited from the (D_6) root lattice projection;
* an effective 3D isotropy ((H_3 \to SO(3)) in the continuum limit).

In that limit:

The strains are dominated by scalar “volumetric” components:
[
\eta^u_{ij} \approx \frac{1}{3}\theta_u,\delta_{ij}, \qquad
\eta^w_{ij} \approx \frac{1}{3}\theta_w,\delta_{ij},
]
with (\theta_u = \operatorname{Tr}\eta^u), (\theta_w = \operatorname{Tr}\eta^w).

All anisotropic / deviatoric invariants vanish on the background, and the quadratic/cubic free energy reduces to a polynomial in (\theta_u, \theta_w).

So up to cubic order we can write, for homogeneous isotropic backgrounds:
[
F(\theta_u,\theta_w) = F_2 + F_3 + \dots
]
with
[
F_2 = \frac{1}{2}\big[A_u \theta_u^2 + A_w \theta_w^2 + 2 A_{uw}\theta_u\theta_w\big],
]
[
F_3 = \frac{1}{6}\big[
B_{uuu}\theta_u^3 + 3 B_{uuw}\theta_u^2\theta_w + 3 B_{uww}\theta_u\theta_w^2 + B_{www}\theta_w^3
\big] + \dots
]
where the dots hide cubic invariants which vanish for pure isotropic strain.

Under (E_\parallel \leftrightarrow E_\perp):
[
\theta_u \leftrightarrow \theta_w, \qquad F(\theta_u,\theta_w) = F(\theta_w,\theta_u),
]
we must have
[
A_u = A_w \equiv A,\quad
B_{uuu} = B_{www} \equiv B_3,\quad
B_{uuw} = B_{uww} \equiv B_2.
]

So the background free energy reduces to:
[
F_2 = \frac{A}{2}(\theta_u^2 + \theta_w^2) + A_{uw}\theta_u\theta_w,
]
[
F_3 = \frac{1}{6}\big[
B_3(\theta_u^3 + \theta_w^3) + 3 B_2(\theta_u^2\theta_w + \theta_u\theta_w^2)
\big].
]

This is a **2-parameter family at quadratic order** ((A, A_{uw})) and a **2-parameter family at cubic order** ((B_2, B_3)) for homogeneous isotropic strain.

The specific values of (A, A_{uw}, B_2, B_3) encode details of the **microscopic interactions** on the (D_6) lattice (interatomic potentials, local environment, etc.) and are **not fixed** by symmetry alone.

So: symmetry has crushed the 20 third-order constants down to (effectively) **two** relevant cubic parameters for the isotropic background sector.

---

## 2. Emergent metrics from the (D_6) embedding

### 2.1 Six-dimensional embedding and maps

Let (G_{AB}) be the metric on (\mathbb{R}^6) containing the (D_6) root lattice, and decompose
[
\mathbb{R}^6 = E_\parallel \oplus E_\perp.
]

Define two embedding maps of 4D spacetime into this 6D ambient space:

* **“Physical / phonon sector”**
  [
  X^A_\parallel(x^\mu) = X^{A(0)}_\parallel(x^\mu) + U^A(x^\mu),
  ]
* **“Internal / phason sector”**
  [
  X^A_\perp(x^\mu) = X^{A(0)}_\perp(x^\mu) + W^A(x^\mu),
  ]
  with (U, W) reducing in the 3D spatial slices to (u_i(x), w_i(x)).

The induced metrics are
[
g_{\mu\nu} = \partial_\mu X^A_\parallel ,\partial_\nu X^B_\parallel,G_{AB}, \qquad
f_{\mu\nu} = \partial_\mu X^A_\perp ,\partial_\nu X^B_\perp,G_{AB}.
]

Expanding around a flat background (G_{AB}) and the undeformed embeddings (X^{(0)}):
[
g_{\mu\nu} = \eta_{\mu\nu} + 2,\eta^{u}*{\mu\nu} + \mathcal{O}(\eta^2),\qquad
f*{\mu\nu} = \eta_{\mu\nu} + 2,\eta^{w}*{\mu\nu} + \mathcal{O}(\eta^2),
]
where (\eta^{u,w}*{\mu\nu}) extend the spatial strain tensors to 4D (with time components vanishing or small in the quasi-static background). So **metric perturbations are directly proportional to strain**.

---

### 2.2 Homogeneous isotropic (FRW) sector

For cosmology, take spatially flat FRW forms:
[
g_{\mu\nu}dx^\mu dx^\nu = -N_g^2 dt^2 + a^2(t),\delta_{ij}dx^i dx^j,
]
[
f_{\mu\nu}dx^\mu dx^\nu = -N_f^2 dt^2 + b^2(t),\delta_{ij}dx^i dx^j.
]

A natural embedding of spatial slices is:
[
X^i_\parallel = a(t),x^i,\qquad
X^i_\perp = b(t),x^i,
]
so that the spatial strains are essentially pure isotropic expansions, with
[
\theta_u \propto \ln\frac{a}{a_\star}, \qquad
\theta_w \propto \ln\frac{b}{b_\star}.
]

At the level of potential energy density, the detailed logarithmic vs linear dependence is not important; what matters is that:

* the overall “common” expansion couples to a cosmological-constant sector;
* the **relative expansion** encoded in the scale-factor ratio
  [
  r \equiv \frac{b}{a}
  ]
  determines a **relative strain** between the two metrics.

Define symmetric / antisymmetric combinations:
[
\theta_+ \equiv \frac{1}{2}(\theta_u + \theta_w),\qquad
\theta_- \equiv \frac{1}{2}(\theta_u - \theta_w).
]

By construction, (E_\parallel \leftrightarrow E_\perp) exchange acts as
[
\theta_+ \to \theta_+,\qquad \theta_- \to -\theta_-.
]

Thus the background free energy collapses to:
[
F_2 = \tilde{A}*+,\theta*+^2 + \tilde{A}*-,\theta*-^2,
]
[
F_3 = C_+,\theta_+^3 + C_{+-},\theta_+\theta_-^2,
]
with no odd powers of (\theta_-) allowed (by exchange symmetry).

In cosmological applications, (\theta_+) can be absorbed into an effective cosmological constant (and redefinitions of Planck masses), whereas (\theta_-) encodes the **massive spin-2 sector**. So all the interesting HR-like structure comes from the (\theta_-^2) and (\theta_+\theta_-^2) terms.

At the homogeneous, isotropic level, the **non-derivative interaction energy density** is therefore a function
[
V(r) \equiv F\big(\theta_+, \theta_-(r)\big),
]
which, because (\theta_-) flips sign under (g \leftrightarrow f) but the energy must be invariant, satisfies
[
V(r) = V(1/r).
]

So
[
D_6 + E_\parallel \leftrightarrow E_\perp + \text{isotropy}
\quad\Rightarrow\quad
\text{background potential symmetric under } r \leftrightarrow 1/r.
]

---

## 3. HR interaction potential on homogeneous backgrounds

### 3.1 Hassan–Rosen action and FLRW / proportional backgrounds

The HR action is (as you wrote)
[
S = \int d^4x\left[
\frac{M_g^2}{2}\sqrt{-g},R(g) + \frac{M_f^2}{2}\sqrt{-f},R(f)

* m^2 M_g^2 \sqrt{-g},\sum_{n=0}^4 \beta_n,e_n\big(\sqrt{g^{-1}f}\big)

- \sqrt{-g},\mathcal{L}_m(g,\psi)
  \right].
  ]

For **proportional backgrounds** (f_{\mu\nu} = c^2 g_{\mu\nu}), the HR potential contribution to the effective cosmological constants is well-known (see Schmidt-May 2015). One finds
[
\Lambda_g(c) = \frac{m^4}{M_g^2}\big(\beta_0 + 3c,\beta_1 + 3c^2\beta_2 + c^3\beta_3\big),
]
[
\Lambda_f(c) = \frac{m^4}{(M_f c)^2}\big(c,\beta_1 + 3c^2\beta_2 + 3c^3\beta_3 + c^4\beta_4\big).
]

The background Einstein equations reduce to
[
G_{\mu\nu}(\bar{g}) + \Lambda_g(c),\bar{g}*{\mu\nu} = 0,\qquad
G*{\mu\nu}(\bar{g}) + \Lambda_f(c),\bar{g}_{\mu\nu} = 0,
]
so we must have
[
\Lambda_g(c) = \Lambda_f(c).
]

This gives a **polynomial equation in (c)** (the ratio of metrics) with coefficients determined by (\beta_n) and the Planck-mass ratio (\alpha \equiv M_f/M_g).

Explicitly:
[
\alpha^2 c^2\big(\beta_0 + 3c\beta_1 + 3c^2\beta_2 + c^3\beta_3\big)

* \big(c\beta_1 + 3c^2\beta_2 + 3c^3\beta_3 + c^4\beta_4\big) = 0.
  ]

---

### 3.2 Symmetric branch: (M_g = M_f,; \beta_n = \beta_{4-n})

From the (D_6) exchange symmetry:

* The transport tensors equal (\Rightarrow M_g = M_f \equiv M).

Interchanging the two sectors in the microscopic theory corresponds to (g \leftrightarrow f) in the IR; for the HR potential this imposes, up to volume factors, the familiar condition
[
\beta_n = \beta_{4-n}
]
for the action to be invariant under this exchange. (This is exactly the “symmetric HR” class often discussed in the bimetric literature.)

Set (M_f = M_g) and
[
\beta_4 = \beta_0,\qquad \beta_3 = \beta_1.
]
The background condition then simplifies dramatically.

Starting from
[
c^2\big(\beta_0 + 3c\beta_1 + 3c^2\beta_2 + c^3\beta_3\big)

* \big(c\beta_1 + 3c^2\beta_2 + 3c^3\beta_3 + c^4\beta_4\big) = 0,
  ]
  substitute (\beta_3 = \beta_1,; \beta_4 = \beta_0) and factor out (c \neq 0). You get
  [
  (c^2 - 1)\Big[\beta_1(c^2 + 1) + c(3\beta_2 - \beta_0)\Big] = 0.
  ]

So the vacuum equation splits as:

* Two universal roots:
  [
  c = \pm 1,
  ]
  corresponding to proportional metrics that are identical (or sign-flipped).

* A quadratic for nontrivial vacua:
  [
  \beta_1 c^2 + (3\beta_2 - \beta_0)c + \beta_1 = 0.
  ]

That is the **symmetric-branch vacuum polynomial** in HR bimetric theory.

This already shows:

* Symmetry (g \leftrightarrow f) (from (D_6) exchange) forces:
  [
  M_g = M_f,\qquad \beta_n = \beta_{4-n},\qquad
  P(c) = (c^2 - 1)\times \text{(quadratic in } c + 1/c).
  ]

Thus (D_6) symmetry **explains why** the HR vacuum polynomial is **even under** (c \to 1/c) and factorizes with ((c^2 - 1)).

None of this uses quasicrystal elasticity in detail—just the **exchange symmetry** and isotropy.

---

## 4. Matching (D_6) elasticity to HR form

Now: how do we get from **microscopic elastic free energy** to an **HR-like potential** with specific (\beta)’s?

### 4.1 Structure of the homogeneous potential from elasticity

From Section 2, the background quasicrystal free energy (per physical volume) is
[
F(\theta_+,\theta_-) = \tilde{A}*+,\theta*+^2 + \tilde{A}*-,\theta*-^2

* C_+,\theta_+^3 + C_{+-},\theta_+\theta_-^2 + \dots
  ]

(\theta_+) (common volumetric mode) can be absorbed into redefinitions of cosmological constants and effective Planck masses; the relative mode is (\theta_-).

For nearly homogeneous FRW geometries, you expect (\theta_-) to be some monotone function of the ratio (r = b/a), with:

* (\theta_-(r=1) = 0) (no relative strain when metrics match).

Under exchange, (r \to 1/r) and (\theta_- \to -\theta_-), consistent with (F(\theta_-) = F(-\theta_-)).

To leading order around (r = 1) you can always write:
[
\theta_-(r) \approx \kappa (r - 1) + \mathcal{O}\big((r-1)^3\big),
]
so near (r=1) the potential is approximately
[
V(r) \equiv F(\theta_-(r)) \approx V_0 + \mu (r-1)^2 + \lambda (r-1)^4 + \dots
]
(only even powers survive by symmetry, (\theta_- \to -\theta_-)).

Thus:

* Locally near (r=1), the low-order structure is a generic **even function** of (r-1).
* Globally in (r), the exact functional form (V(r)) carries non-perturbative information about how the (D_6) lattice energy depends on relative scaling of (E_\parallel) and (E_\perp). There is no purely group-theoretic reason for it to be a **quartic polynomial** in (r); that’s an effective truncation.

---

### 4.2 HR potential in FLRW form

The HR potential, when evaluated on FLRW metrics with ratio (r = b/a), yields an interaction energy density of the form (schematically; see e.g. bimetric cosmology literature)
[
\rho_{\text{int}}(r,\xi) \propto
\beta_0 + 3\beta_1(\xi + r) + 3\beta_2(\xi r + r^2) + \beta_3\xi r^2 + \beta_4 \xi r^3,
]
where (\xi = N_f/N_g) is the lapse ratio. The Bianchi constraint gives an algebraic relation between (\xi) and (r); in vacuum, this reduces essentially to the proportional-background condition, which on the symmetric branch gives our polynomial in (c = r).

The key is:

* the HR potential is **by construction** a **linear combination of symmetric polynomials** (e_n(S)) in the eigenvalues of
  [
  S \equiv \sqrt{g^{-1}f}.
  ]

A *generic* diffeomorphism-invariant potential built from (g^{-1}f) would be some analytic function
[
V_{\text{gen}}(S) = F(e_1, e_2, e_3, e_4),
]
with **nonlinear** dependence on (e_n). HR picks out the **special subclass**
[
V_{\text{HR}} = \sum_{n=0}^4 \beta_n,e_n(S).
]

From the point of view of **emergent elasticity**, there is **no a priori reason** the microscopic potential must lie in the HR subclass. The HR form is imposed as a **UV consistency condition** (BD ghost-freedom) in the 4D effective theory, not as a consequence of (D_6) symmetry.

So the mapping

> “(D_6) elasticity (\to) exactly HR potential”

is not purely geometric; it depends on imposing **ghost freedom** as an extra dynamical principle.

Once we **assume** that the IR potential can indeed be written in HR form, the exchange symmetry analysis above tells us:

**Constraint 1 (exchange):**
[
M_g = M_f, \qquad \beta_n = \beta_{4-n}.
]

Then the quasicrystal potential for (r) can be matched to the HR FLRW reduction; this defines (\beta)’s as linear combinations of the microscopic couplings.

---

### 4.3 (\beta)’s as linear combinations of microscopic elastic couplings

On isotropic backgrounds, the quasicrystal potential can be written, after absorbing (\theta_+) into constants, as a function of a single scalar (\theta_-(r)):
[
V(r) = \tilde{\mu},\theta_-^2(r) + \tilde{\lambda},\theta_-^4(r) + \dots,
]
with (\theta_-(r)) some odd function of ((r - 1/r)) dictated by the underlying projection geometry ((D_6 \to H_3)), involving (\varphi) in its detailed form.

If we insist on representing this as an HR potential near the background, then:

* We expand both (V(r)) and the HR energy density around a chosen vacuum (r = r_\star) (e.g. (r_\star = 1) or (r_\star = \varphi)),
* expand in powers of (\delta r = r - r_\star),
* and **match coefficients** order by order in (\delta r).

This defines the (\beta)’s as linear combinations of the microscopic couplings ((\tilde{\mu}, \tilde{\lambda}, \dots)) and the derivatives of (\theta_-(r)) at the vacuum.

Schematically:
[
\beta_n = \sum_k c_{nk}(\varphi),\alpha_k,
]
where:

* (\alpha_k) are the small set of isotropic elastic constants (A, A_{uw}, B_2, B_3,\dots) (and possibly higher-order ones if you match beyond cubic),
* the (c_{nk}(\varphi)) are **pure numbers** built from projection geometry (i.e. the golden ratio) and combinatorial factors from the expansions.

This gives the **formal structure** you requested: (\beta)’s as linear combinations of microscopic elastic couplings.

But crucially:

* The exact values of the (c_{nk}) depend on the **explicit functional form** (\theta_-(r)) and the full nonlinear elasticity (beyond cubic).
* The current GS document does **not** supply a complete microscopic calculation of (\theta_-(r)) from (D_6) plus realistic interatomic potentials; instead, it posits Axiom 0 and the Schur-curvature term as an effective geometric variational principle.

So at this stage, we **cannot** compute the numerical (c_{nk}) from first principles; we can only assert the **existence** of such a linear map given the assumption that the IR potential is HR-like.

---

## 5. Golden vacuum and constraints on (\beta_n)

Now, assume:

* **Symmetric branch**:
  [
  M_g = M_f, \qquad \beta_n = \beta_{4-n}.
  ]
* The vacuum polynomial for the proportional background possesses roots
  [
  c = \pm 1,\quad c = \varphi,\quad c = \varphi^{-1},
  ]
  where (\varphi = \frac{1+\sqrt{5}}{2}) is the golden ratio.

From Section 3.2, the proportional vacuum condition is
[
(c^2 - 1)\Big[\beta_1(c^2 + 1) + c(3\beta_2 - \beta_0)\Big] = 0.
]

Thus the nontrivial branch is the quadratic
[
\beta_1 c^2 + (3\beta_2 - \beta_0)c + \beta_1 = 0.
]

If its roots are (c = \varphi) and (c = \varphi^{-1}), then its polynomial is proportional to
[
(c - \varphi)(c - \varphi^{-1}) = c^2 - (\varphi + \varphi^{-1})c + 1.
]

Using (\varphi + \varphi^{-1} = \sqrt{5}), this is
[
c^2 - \sqrt{5},c + 1.
]

So we must have
[
\beta_1 c^2 + (3\beta_2 - \beta_0)c + \beta_1 \propto c^2 - \sqrt{5},c + 1.
]

Matching coefficients:

* Coefficient of (c^2): (\beta_1 \propto 1) (this just sets overall normalization).
* Constant term: same (\Rightarrow) consistent with that.
* Coefficient of (c):
  [
  3\beta_2 - \beta_0 = -\sqrt{5},\beta_1.
  ]

So **Golden vacuum** (roots at (\varphi,\varphi^{-1})) + symmetric branch implies the linear relation
[
\beta_0 - 3\beta_2 = \sqrt{5},\beta_1.
]

That’s the central **GS-compatible constraint on (\beta)’s** which really does encode the golden ratio.

If we now fix a normalization (for example choose (\beta_2 = -1), as in your GS ansatz), this gives
[
\beta_0 = -3 + \sqrt{5},\beta_1.
]

Your GS numbers
[
\beta_0^{\text{GS}} \approx -0.857,\qquad
\beta_1^{\text{GS}} \approx 0.958,\qquad
\beta_2^{\text{GS}} = -1
]
satisfy this to within rounding:
[
\sqrt{5},\beta_1 \approx 2.236\times 0.958 \approx 2.142,
]
[
-3 + 2.142 \approx -0.858 \approx \beta_0^{\text{GS}}.
]

So we’ve recovered:

* **Constraint 1 (exchange symmetry):**
  [
  \beta_n = \beta_{4-n}.
  ]
* **Constraint 2 (Golden vacuum):**
  [
  \beta_0 - 3\beta_2 = \sqrt{5},\beta_1.
  ]

Up to an overall normalization and one remaining free parameter (e.g. (\beta_1)), these define a **1-parameter family** of (\beta)’s; setting (\beta_2 = -1) picks out the specific GS numbers.

Importantly, Constraint 2 does **not** follow from (D_6) symmetry alone. It follows from:

* choosing the **HR functional form**, and
* imposing **golden roots** as an extra vacuum selection criterion.

Within GS, that vacuum selection is encoded in **Axiom 0** via Schur-convexity of the geometric variational free energy
[
F[G] = E_{\text{strain}} + \lambda,\kappa_{\text{Schur}},
]
not from the bare elastic Hamiltonian.

---

## 6. Is the HR form itself derivable from (D_6)? No-go / non-uniqueness

Let me be blunt:

From (D_6 + H_3) symmetry + quasicrystal elasticity, you get:

* Two displacement fields (phonon + phason) with the generalized elastic free energy as in Socolar–Lubensky–Steinhardt / Fan / Trebin.
* For icosahedral quasicrystals, quadratic and cubic invariant structures with a finite set of independent elastic constants (5 quadratic, 20 cubic).
* In the isotropic, exchange-symmetric sector: a **2-parameter quadratic** and **2-parameter cubic** description of homogeneous strain energy in terms of (\theta_+, \theta_-).
* An emergent **two-metric structure** for wave propagation (phonon vs phason modes) consistent with analog gravity arguments for multi-field systems, which generically lead to multi-metric effective descriptions.

What you do **not** get from (D_6) by itself:

* **Ghost freedom** in the emergent spin-2 theory, i.e. the restriction of the potential to a linear combination of (e_n(S)).
* The **specific linear relation** among (\beta)’s that encodes the golden ratio.

Where HR comes from conceptually:

* HR is the **unique 4D local bimetric theory** of two spin-2 fields with ghost-free interactions.
* It is an **effective field theory consistency condition**, not a statement about microscopic lattice interactions.

Thus:

The mapping

> “(D_6) quasicrystal (\to) exactly HR potential with the GS (\beta)’s”

requires **extra input** beyond elasticity:

* demand of **BD ghost-freedom**,
* desire to interpret the phonon+phason background as a **bimetric spin-2 system**,
* the **Golden vacuum** requirement, and
* some **normalization condition** (e.g. fixing (\beta_2) or the Fierz–Pauli mass).

Without these, the most you can say is that the space of allowed (\beta)’s compatible with (D_6) symmetry and a Golden vacuum is the **2D subspace**:
[
\beta_n = \beta_{4-n},\qquad \beta_0 - 3\beta_2 = \sqrt{5},\beta_1,
]
plus overall scale.

The **detailed numerical values** of (\beta)’s are still ansatz-level, derived from a **choice of effective Golden free-energy functional**, not from directly summing lattice energies.

To go beyond this, you would need:

* A fully specified **microscopic model** on the (D_6) lattice (actual interatomic potential or fully geometric energy functional),
* a credible **coarse-graining procedure** showing that the emergent IR spin-2 sector is *precisely* HR-like,
* and a demonstration that the resulting (\beta)’s satisfy the GS numbers.

That is a very hard open problem, and it is **not** solved by the currently available GS material.

---

## 7. Executive summary (for a mathematical physicist)

### Context

The **Golden Selection** starts from a (D_6) root lattice and selects a 3D icosahedral quasicrystal ((H_3)) via cut-and-project, with physical space (E_\parallel) and internal space (E_\perp), and displacement fields (u) (phonons) and (w) (phasons).

Quasicrystal elasticity (Socolar, Lubensky, Steinhardt, Fan, Ricker & Trebin) describes quadratic and cubic invariants built from phonon and phason strains.

GS imposes a **democratic** structure: (T_u = T_w), phonon–phason coupling small, suggesting (M_g = M_f), and an approximate (E_\parallel \leftrightarrow E_\perp) symmetry.

### Elastic invariants

* For icosahedral quasicrystals, linear elasticity has **five** independent constants (two phonon, two phason, one coupling), with **phonon–phason coupling small** and vanishing in the isotropic limit.
* Ricker & Trebin show there are **20 independent** third-order elastic constants, grouped into (uuu, uuw, uww, www) invariants.
* In the **isotropic, exchange-symmetric, homogeneous** sector relevant for cosmology, this collapses to:

  * 2 quadratic constants ((A, A_{uw})),
  * 2 cubic constants ((B_2, B_3)),
    with the background free energy a polynomial in
    [
    \theta_+ = (\theta_u + \theta_w)/2,\qquad
    \theta_- = (\theta_u - \theta_w)/2.
    ]

### Emergent metrics and bimetric structure

Using a 6D embedding, the phonon and phason embeddings yield induced metrics (g_{\mu\nu}, f_{\mu\nu}) whose linear perturbations are proportional to the phonon and phason strain tensors.

On homogeneous FRW backgrounds, the metrics take the usual form with scale factors (a(t), b(t)), and the **relative strain** is encoded in the ratio
[
r = \frac{b}{a}.
]

The background elastic free energy then defines an effective potential (V(r)), symmetric under exchange of sectors:
[
V(r) = V(1/r).
]

### HR potential and (D_6) exchange symmetry

Assuming the effective IR spin-2 theory is described by Hassan–Rosen bimetric gravity, the interaction potential is a linear combination of elementary symmetric polynomials (e_n(S)) in the eigenvalues of (S = \sqrt{g^{-1}f}).

On proportional backgrounds (f = c^2 g), the HR potential gives effective cosmological constants
[
\Lambda_g(c) = \frac{m^4}{M_g^2}(\beta_0 + 3c\beta_1 + 3c^2\beta_2 + c^3\beta_3),
]
[
\Lambda_f(c) = \frac{m^4}{(M_f c)^2}(c\beta_1 + 3c^2\beta_2 + 3c^3\beta_3 + c^4\beta_4).
]

The vacuum condition (\Lambda_g(c) = \Lambda_f(c)) yields a **quartic polynomial** in (c). On the **symmetric branch**
[
M_g = M_f,\qquad \beta_n = \beta_{4-n},
]
this factorizes as
[
(c^2 - 1)\big[\beta_1(c^2 + 1) + c(3\beta_2 - \beta_0)\big] = 0
]
(\Rightarrow) universal roots (c = \pm 1) plus a quadratic governing nontrivial vacua.

The (D_6) exchange symmetry thus forces:

* (M_g = M_f,\quad \beta_n = \beta_{4-n}),

and makes the vacuum polynomial even under (c \to 1/c), in direct analogy to the symmetry of the quasicrystal potential (V(r)).

### Golden vacuum and linear constraint on (\beta)’s

If we now impose that the symmetric-branch quadratic has roots at the **golden ratio pair**
[
c = \varphi,\quad c = \varphi^{-1},
]
we must have (up to normalization)
[
\beta_1 c^2 + (3\beta_2 - \beta_0)c + \beta_1 \propto c^2 - \sqrt{5},c + 1.
]

This yields the **linear constraint**
[
\beta_0 - 3\beta_2 = \sqrt{5},\beta_1.
]

Together with (\beta_n = \beta_{4-n}), this defines a **two-parameter family** (plus overall scale) of (\beta)’s consistent with:

* (D_6) exchange symmetry, and
* a **Golden vacuum** (roots (\pm 1, \varphi, \varphi^{-1})).

The GS ansatz
[
\beta_2 = -1,\quad \beta_0 \approx -0.857,\quad \beta_1 \approx 0.958
]
is a particular point in this subspace, consistent with the linear constraint but **not uniquely determined** by it.

### Derivation status

**Derived (modulo HR assumption):**

* HR-like potential structure on homogeneous backgrounds;
* Exchange symmetry constraints (M_g = M_f, \beta_n = \beta_{4-n});
* Golden vacuum constraint (\beta_0 - 3\beta_2 = \sqrt{5}\beta_1).

**Not derived (still ansatz):**

* The **exact HR form** (linear in (e_n)) from (D_6) elasticity: ghost freedom is a 4D EFT requirement, not a lattice symmetry consequence.
* The **specific numerical values** of (\beta)’s: they depend on the detailed functional form of the microscopic free energy (F[G]) (including the Schur-curvature term in Axiom 0) and on normalization choices.

Hence:

> The GS (D_6) quasicrystal geometry **constrains** the HR (\beta)’s to a small, golden-structured subspace but does **not uniquely derive** their numerical values with presently available information.

The current (\beta)’s remain **ansatz-level**, albeit now with a clear mapping:
[
\text{symmetry} \Rightarrow \beta_n = \beta_{4-n},
]
[
\text{golden vacuum} \Rightarrow \beta_0 - 3\beta_2 = \sqrt{5},\beta_1,
]
remaining freedom tied to microscopic elastic constants and overall mass normalization.

---

## 8. Machine-readable artifacts

### 8.1 JSON/YAML schematic

Here is a **schematic YAML** capturing:

* the isotropic elastic invariant basis,
* the mapping structure to (\beta)’s,
* the symmetry constraints.

```yaml
elastic_invariants:
  quadratic:
    - name: I_u2
      type: u-u
      expression: "(Tr(eta_u))^2"
    - name: J_u2
      type: u-u
      expression: "Tr(eta_u^2)"
    - name: I_w2
      type: w-w
      expression: "(Tr(eta_w))^2"
    - name: J_w2
      type: w-w
      expression: "Tr(eta_w^2)"
    - name: I_uw
      type: u-w
      expression: "Tr(eta_u * eta_w)"

  cubic_isotropic:
    # Only invariants nonzero for homogeneous isotropic strain retained
    - name: K_uuu
      type: u-u-u
      expression: "(Tr(eta_u))^3"
    - name: K_www
      type: w-w-w
      expression: "(Tr(eta_w))^3"
    - name: K_uuw
      type: u-u-w
      expression: "(Tr(eta_u))^2 * Tr(eta_w)"
    - name: K_uww
      type: u-w-w
      expression: "Tr(eta_u) * (Tr(eta_w))^2"

isotropic_parameters:
  # Coefficients of the above invariants in the elastic free energy density
  quadratic:
    A_u: coefficient of I_u2
    B_u: coefficient of J_u2
    A_w: coefficient of I_w2
    B_w: coefficient of J_w2
    A_uw: coefficient of I_uw
  cubic:
    C_uuu: coefficient of K_uuu
    C_www: coefficient of K_www
    C_uuw: coefficient of K_uuw
    C_uww: coefficient of K_uww

symmetry_constraints:
  # E_parallel <-> E_perp exchange
  - "A_u = A_w"
  - "B_u = B_w"
  - "C_uuu = C_www"
  - "C_uuw = C_uww"
  # optional: small phonon-phason coupling in isotropic limit
  - "A_uw approximately 0"

relative_strain:
  definitions:
    theta_u: "Tr(eta_u)"
    theta_w: "Tr(eta_w)"
    theta_plus: "0.5 * (theta_u + theta_w)"
    theta_minus: "0.5 * (theta_u - theta_w)"
  symmetry:
    - "theta_minus -> -theta_minus under E_parallel <-> E_perp"

effective_potential:
  # background energy density
  form:
    V(theta_plus, theta_minus): >
      A_plus * theta_plus^2 + A_minus * theta_minus^2
      + C_plus * theta_plus^3 + C_pm * theta_plus * theta_minus^2
      + higher orders
  exchange_symmetry:
    - "V(theta_plus, theta_minus) = V(theta_plus, -theta_minus)"

hr_parameters:
  # HR beta_n expressed as linear combinations of microscopic couplings
  mapping_structure:
    beta0: "sum_k c_0k(alpha_k)"
    beta1: "sum_k c_1k(alpha_k)"
    beta2: "sum_k c_2k(alpha_k)"
    beta3: "beta1  # symmetric branch"
    beta4: "beta0  # symmetric branch"
  microscopic_parameters:
    - "alpha_k in {A_u, A_w, A_uw, C_uuu, C_uuw, C_uww, C_www, ...}"
  notes:
    - "c_nk are dimensionless coefficients determined by the detailed form of
       theta_minus(r) and the coarse-graining procedure; they depend on the
       golden ratio via the D6->H3 projection."

beta_constraints:
  # Constraints derived in this analysis
  - "beta3 = beta1"
  - "beta4 = beta0"
  - "Golden vacuum: beta0 - 3*beta2 = sqrt(5) * beta1"
  - "Overall normalization of {beta_n} remains free"

  # GS choice:
  gs_choice:
    beta2: -1.0
    beta1: 0.958
    beta0: -0.857
    consistency:
      - "beta3 = beta1"
      - "beta4 = beta0"
      - "beta0 - 3*beta2 ≈ sqrt(5)*beta1"
```

This is deliberately schematic: it captures the **structure** and **constraints** without pretending we have explicit numbers for the (c_{nk}).

---

### 8.2 Python skeleton for HR–Golden mapping

A simple **symbolic script** (using `sympy`) to reproduce the core HR–golden relation:

```python
import sympy as sp

# Symbols
c = sp.symbols('c', real=True)
beta0, beta1, beta2 = sp.symbols('beta0 beta1 beta2', real=True)

# Symmetric-branch vacuum polynomial from HR:
# (c^2 - 1)*(beta1*(c**2 + 1) + c*(3*beta2 - beta0)) = 0
P_quartic = (c**2 - 1) * (beta1 * (c**2 + 1) + c * (3*beta2 - beta0))

# Extract the quadratic factor
P_quadratic = sp.simplify(beta1 * (c**2 + 1) + c * (3*beta2 - beta0))

# Golden-ratio polynomial with roots phi, 1/phi:
phi = (1 + sp.sqrt(5)) / 2
P_golden = (c - phi) * (c - 1/phi)

# Expand and compare coefficients
P_golden_expanded = sp.expand(P_golden)

# Match P_quadratic ~ lambda * P_golden_expanded
lambda_symbol = sp.symbols('lambda', real=True)
equations = sp.Eq(P_quadratic, lambda_symbol * P_golden_expanded)
coeffs_equations = sp.Eq(
    sp.Poly(P_quadratic, c).all_coeffs(),
    sp.Poly(lambda_symbol * P_golden_expanded, c).all_coeffs()
)

# Solve for the linear relation among beta0, beta1, beta2
solution = sp.solve(coeffs_equations, (beta0, beta2, lambda_symbol), dict=True)
print(solution)
```

---

If you’d like, I can now also strip this down into a shorter “note-style” version or convert it into a LaTeX article template.
