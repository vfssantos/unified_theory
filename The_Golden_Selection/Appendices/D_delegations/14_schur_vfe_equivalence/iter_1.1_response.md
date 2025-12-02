Response from Agent 1:

--- 
**Overall verdict: SPECULATIVE**

There *is* a real web of connections between

* Schur-convexity, curvature and “free-energy-like” functionals, and
* variational free energy, Fisher information and information geometry.

Bruna’s Schur-convex curvature sits right in the middle of that web. But I don’t see any existing theorem – or a straightforward derivation – that makes
(\kappa_{\text{Schur}}) *equal* (even up to simple scaling/offset) to the VFE complexity term (D_{\mathrm{KL}}(q|p)), even in the highly symmetric dihedral exponential families you’re using. The structures line up locally and qualitatively, but they don’t match globally.

So I’d classify your equivalence claim as:

> **SPECULATIVE**: structurally suggestive, lots of supporting analogies, but substantial gaps and some structural mismatches that make literal equivalence unlikely without extra, very specific assumptions.

Below I’ll lay out what’s known, how the structures compare, where a derivation runs aground, and what would still need to be done.

---

## 1. Literature findings

### 1.1 Schur-convexity, curvature and free energy

There *is* literature connecting curvature, Schur-convexity and free-energy-type quantities:

* Gibilisco & Isola (2006) introduce the problem of **Schur-convex scalar curvature** for statistical models equipped with monotone (Fisher-type) metrics. They note that in information geometry of thermodynamics, the **scalar curvature is often postulated to be proportional to free-energy density** (or its inverse).

* Ruppeiner’s “thermodynamic geometry” identifies the scalar curvature (R) of a thermodynamic metric (essentially the Hessian of the entropy or free energy) with **correlation volume or inverse free-energy density** near criticality.

* Gibilisco & Isola explicitly remark that, in this geometric approach, *“the scalar curvature is proportional to free energy density.”*

So: *curvature as a free-energy density* in thermodynamic/information-geometric settings is absolutely a thing.

Separately, there’s a broad body of work where **free-energy-like Lyapunov functions are Schur-convex** in the probability vector:

* Gorban’s “General H-theorem and entropies that violate the second law” treats a large class of convex (f)-divergences (including KL) as **Massieu–Planck potentials**, i.e. *negative free energy*, and links their behavior to Schur-convexity/majorization under doubly stochastic maps.

* Majorization-based thermodynamics and resource theories (e.g. Gour et al., Brandão et al., summarized in “Entropy, Divergence, and Majorization in Classical and Quantum Information”) use **Schur-convex functionals** as monotones; free-energy functionals are canonical examples.

* There are explicit thermodynamic constructions where **non-equilibrium free energy** is Schur-convex in the eigenvalue vector of the state, and the second laws are formulated as the monotonic decrease of Schur-convex free-energy functionals.

So conceptually, you can legitimately say:

> **“Schur-convex curvature” and “free-energy-like quantities” are already linked in the literature.**

Bruna’s paper then adds a *new* curvature functional, defined via the **Schur complement of a Hessian under dihedral symmetry** and shown to be a quadratic Schur-convex function of low-order moments.

### 1.2 Information geometry and the Free Energy Principle

On the FEP side:

* Friston’s “A Free Energy Principle for a Particular Physics” defines the **variational free energy**
  [
  F[q] = \mathbb{E}_q[\ln q(\eta) - \ln p(\eta,s)]
  ]
  and shows its decompositions into KL-divergence and evidence / accuracy–complexity forms.

* Da Costa et al. (2021) show that neural dynamics under active inference **approximate natural gradient descent** (i.e. steepest descent in the Fisher–information metric) on VFE.

* The FEP literature in general treats belief trajectories as **flows on an information manifold** with the Fisher metric, with VFE as a Lyapunov function – an “information-geometric action functional” sitting above the KL divergence.

So VFE is tightly bound to **Fisher geometry**, but it’s a *divergence* (a potential) rather than a curvature scalar.

### 1.3 Exponential families, symmetry and variational inference

There are well-developed connections between exponential families, symmetry and variational inference:

* Bui, Huynh & de Salvo Braz (2012) use group **automorphisms of graphical models** to define *lifted variational inference*: exponential families are constrained by symmetry (e.g. automorphism group orbits), leading to reduced parameterizations and invariant variational free energies.

* The broader lifted inference literature shows that imposing a symmetry group (G) on an exponential family essentially restricts the variational family to **(G)-invariant submanifolds**.

However, I don’t see any existing work that:

* introduces Bruna’s specific **Schur-complement curvature** (\kappa_{\text{Schur}}), **and**
* identifies it with **KL-based complexity** in variational free energy.

### 1.4 Majorization and thermodynamics

Finally, majorization itself is deeply embedded in thermodynamics:

* Gómez (2019) analyzes **majorization dynamics** of continuous distributions and notes how Schur-convexity and quasi-convexity underpin entropy increase and thermodynamic behavior.

* Quantum thermodynamics and one-shot resource-theory formulations explicitly use **Schur-convex “free energies”** as second-law monotones.

So the “triangle” **(majorization, Schur-convexity, free energy)** is well-established.

**What I do *not* find** is:

* any mention of Friston or “active inference” in Bruna’s paper;
* any place in the FEP literature where a **Schur-complement curvature** is introduced;
* any theorem stating that “scalar curvature” or “Schur curvature” *is exactly* a KL complexity term.

---

## 2. Mathematical structure comparison

Let’s put the two objects side by side, in the specific setting you care about: the folded dihedral exponential family

[
x_r(q) = \frac{q^r}{S_0(q)}, \quad S_0(q) = \sum_{r=1}^N q^r, \quad r=1,\dots,N, ; 0<q<1, ; \theta = \ln q.
]

### 2.1 Bruna’s Schur-convex curvature

From Bruna:

* Let (F(x)) be some **reduced functional** defined on the simplex (\Delta_N), with Hessian (H(\theta)) evaluated at the orbit (x(\theta)). The tangent space splits orthogonally into **collective mode** (O=\mathrm{span}{1}) and **band sector** (B), under a fixed projector metric of radius (m_\rho^2).

* Block-decompose the Hessian:
  [
  H(\theta) =
  \begin{pmatrix}
  H_{BB}(\theta) & H_{BO}(\theta)\
  H_{OB}(\theta) & H_{OO}(\theta)
  \end{pmatrix},
  ]
  with (H_{OO}(\theta)\succ 0).

* Define the **Schur curvature** as the normalized trace of the Schur complement eliminating the collective mode:
  [
  \kappa_{\text{Schur}}(\theta) = \frac{1}{\dim B},\mathrm{Tr}\left[H_{BB}(\theta) - H_{BO}(\theta) H_{OO}(\theta)^{-1} H_{OB}(\theta)\right]. \tag{*}
  ]

* Under the PSD exponential-sum assumptions and (D_N)-equivariance, Bruna proves:

  * **Convexity**: (\theta \mapsto \kappa_{\text{Schur}}(\theta)) is convex.
  * **Golden lock-in**: there is a unique stationary point at (q_*=\varphi^{-2}) for dihedral order a multiple of 12 (particularly (N=12)).
  * **Quadratic folded law**: for fixed ((N,m_\rho^2)),
    [
    \kappa_{\text{Schur}}(q)
    = A(N,m_\rho^2),I_1(q)^2

    * B(N,m_\rho^2),\big(I_2(q) - I_1(q)^2\big),
      ]
      where (I_1, I_2) are the folded moments (mean and second moment of the index (r)), and the coefficients (A,B) are rational functions fixed by the projector geometry.

So (\kappa_{\text{Schur}}) is:

* A **scalar curvature-like functional** defined from a matrix Schur complement;
* Convex in the **log-parameter** (\theta);
* A **quadratic Schur-convex function** of the low-order invariants (I_1, I_2);
* Entirely **geometric / structural**: it depends on ((N,m_\rho^2)) and the orbit (x(q)), but not on any prior/posterior or observed data.

### 2.2 Variational free energy and complexity

For a generative model (p(\eta,s)) and variational density (q(\eta)), variational free energy is:

[
F[q] = \mathbb{E}_q[\ln q(\eta) - \ln p(\eta,s)].
]

Key decompositions:

* **Divergence + evidence**
  [
  F[q] = D_{\mathrm{KL}}(q(\eta)|p(\eta\mid s)) - \ln p(s).
  ]

* **Inaccuracy + complexity**
  [
  F[q] = \underbrace{\mathbb{E}*q[-\ln p(s\mid\eta)]}*{\text{inaccuracy}}

  * \underbrace{D_{\mathrm{KL}}(q(\eta)|p(\eta))}_{\text{complexity}}.
    ]

It’s the **complexity term**
[
C[q] := D_{\mathrm{KL}}(q(\eta)|p(\eta))
]
you’re trying to match to (\kappa_{\text{Schur}}).

Now specialise (q(\eta)) to the folded exponential family (x(q)) over discrete latent causes (r=1,\dots,N), with natural parameter (\theta = \ln q):

[
q_\theta(r) = \frac{e^{\theta r}}{\sum_{k=1}^N e^{\theta k}}.
]

Let’s pick a prior (p(\eta)) also in this family:

[
p(\eta=r) = q_{\theta_0}(r),
]
so the prior is just another point (\theta_0) on the same manifold (we’ll pick (\theta_0 = \theta_*) later to center things at the golden ratio).

Then the complexity is a **KL between two points in the same exponential family**. In standard exponential-family form, with (T(r)=r) and log-partition (A(\theta)=\log \sum_{k} e^{\theta k}), we have

[
q_\theta(r) = \exp{\theta r - A(\theta)}.
]

KL divergence between two such members is the Bregman divergence of (A):

[
D_{\mathrm{KL}}(q_\theta ,|,q_{\theta_0})
= (\theta - \theta_0) A'(\theta) - A(\theta) + A(\theta_0). \tag{KL1}
]

Here (A'(\theta)=\mathbb{E}*{q*\theta}[r] = I_1(\theta)).

Differentiating:

* First derivative:
  [
  \frac{d}{d\theta} D_{\mathrm{KL}}(q_\theta|q_{\theta_0})
  = (\theta - \theta_0),A''(\theta)
  = (\theta - \theta_0),\mathrm{Var}*{q*\theta}[r]. \tag{KL2}
  ]

* Second derivative:
  [
  \frac{d^2}{d\theta^2} D_{\mathrm{KL}}(q_\theta|q_{\theta_0})
  = \mathrm{Var}*{q*\theta}[r] + (\theta - \theta_0),\frac{d}{d\theta}\mathrm{Var}*{q*\theta}[r].
  ]

At the minimum (\theta = \theta_0), this reduces to

[
D''*{\mathrm{KL}}(\theta_0) = \mathrm{Var}*{q_{\theta_0}}[r],
]
which is just the **Fisher information** (g(\theta_0)) – standard information-geometric fact.

So the **complexity term** on this 1D manifold:

* Is **convex** in (\theta), with unique minimum at (\theta_0).
* Has **local curvature** (second derivative at the minimum) equal to the Fisher information (variance of (r)).
* Is a **Bregman divergence of the log-partition function** (A(\theta)), i.e. it depends on (A(\theta)) itself, not just its low-order moments.

### 2.3 Structural contrasts

Now compare:

1. **Inputs**

   * (\kappa_{\text{Schur}}) depends on a *single distribution* (x(q)), the projector metric (m_\rho^2) and the symmetry-restricted Hessian of a reduced functional. No prior or data.
   * (D_{\mathrm{KL}}(q|p)) depends on a **pair** of distributions (posterior/approximate and prior).

2. **Functional form**

   * Bruna:
     [
     \kappa_{\text{Schur}}(q)
     = A I_1(q)^2 + B\big(I_2(q) - I_1(q)^2\big),
     ]
     a **quadratic polynomial** in the mean and variance of (r).
   * KL complexity:
     [
     C(\theta) = (\theta - \theta_0) I_1(\theta) - A(\theta) + A(\theta_0),
     ]
     a **Bregman divergence** in terms of **log-sums** (A(\theta)=\log\sum_k e^{\theta k}).

   These are very different classes of functions: quadratic in moments vs. log-sum-exp.

3. **Geometric level**

   * (\kappa_{\text{Schur}}) is a **curvature-like scalar** derived from the second derivative *of some functional in probability coordinates* and then projected via Schur complement.
   * (D_{\mathrm{KL}}) is a **potential / divergence** on the statistical manifold; its local second-order expansion is governed by the **metric** (g_{ij}) (Fisher), and *curvature* is a *further* contraction of derivatives of that metric.

   In other words, (D_{\mathrm{KL}}) lives at the “potential” level; curvature (like (\kappa_{\text{Schur}}) or Ruppeiner’s (R)) lives *one differential order higher*.

4. **Symmetry**

   * Both are invariant under the dihedral action when everything is set up symmetrically.
   * Bruna’s result shows that under (D_N) symmetry **any equivariant quadratic functional on the band sector** reduces to a function of two invariants, ((I_1, I_2 - I_1^2)).
   * KL between two members of the same family is also invariant under the group, but its expression in terms of (I_1,I_2) would necessarily involve **log-partition terms** that cannot be recast as a polynomial in (I_1,I_2) alone.

So structurally, (\kappa_{\text{Schur}}) and (D_{\mathrm{KL}}) occupy **different levels** in the geometric hierarchy:

* (D_{\mathrm{KL}}) → generates the **metric** (second derivatives at coincidence).
* The metric → generates **curvature scalars** (Ruppeiner, Petz/Gibilisco–Isola, etc.).
* Bruna’s (\kappa_{\text{Schur}}) is exactly such a scalar defined via a Schur complement plus symmetry constraints.

That already makes “(\kappa_{\text{Schur}} = D_{\mathrm{KL}})” a **strong** claim: you’re asking a curvature scalar to equal a divergence, not just to be derived from its second derivatives.

---

## 3. Derivation attempt and where it breaks

Let’s follow your suggested proof strategy and see how far we can get.

### 3.1 KL for the dihedral exponential family

Take the folded family (x_r(q)) with (\theta = \ln q), and choose the prior to be **the golden-ratio point**:

[
p_0(r) = x_r(q_*), \quad \theta_* = \ln q_* = \ln \varphi^{-2}.
]

Then the complexity term is

[
C(\theta) := D_{\mathrm{KL}}(x(\theta),|,x(\theta_*))
= (\theta - \theta_*),I_1(\theta) - A(\theta) + A(\theta_*), \tag{KL1 again}
]
with (I_1(\theta) = A'(\theta)).

Properties:

* Unique minimum at (\theta=\theta_*). (Direct from (KL2): gradient zero only at (\theta=\theta_*), and convexity.)
* Local expansion:
  [
  C(\theta_* + \delta\theta)
  = \tfrac12 g(\theta_*),\delta\theta^2 + O(\delta\theta^3),
  ]
  with (g(\theta_*) = \mathrm{Var}*{x(\theta**)}[r] = I_2(\theta_*) - I_1(\theta_*)^2).

So **near the golden ratio**, the complexity term is essentially a quadratic in (\delta\theta) with coefficient given by the variance.

### 3.2 (\kappa_{\text{Schur}}) in terms of Fisher data

Bruna gives:

[
\kappa_{\text{Schur}}(\theta)
= A,I_1(\theta)^2 + B\big(I_2(\theta) - I_1(\theta)^2\big)
= A,I_1(\theta)^2 + B,\mathrm{Var}_{x(\theta)}[r]. \tag{S1}
]

Note that (I_2 - I_1^2 = A''(\theta)) is exactly the **Fisher information** (g(\theta)) for this 1D family. So you can rewrite

[
\kappa_{\text{Schur}}(\theta) = B,g(\theta) + A,I_1(\theta)^2.
]

This is already telling:

* One term is **metric-like** (proportional to Fisher information);
* The other is a **quadratic in the expectation** of the sufficient statistic.

So (\kappa_{\text{Schur}}) is a *particular scalar built from the first two derivatives of the log-partition function* (A(\theta)).

Meanwhile, the KL complexity (C(\theta)) in (KL1) is a **Bregman divergence of (A)**: it involves (A) itself as well as (A').

So:

* (\kappa_{\text{Schur}}) is a function of **(A',A'')**;
* (C(\theta)) is a function of **(A,A')**.

Unless (A) satisfies some very special differential relation, you cannot generally expect a function of ((A',A'')) to equal a function of ((A,A')) for all (\theta).

### 3.3 Can we force (\kappa_{\text{Schur}}) to equal KL?

Suppose we try to enforce
[
\kappa_{\text{Schur}}(\theta) = \alpha, C(\theta) + \beta
]
for all (\theta), with some constants (\alpha,\beta) (this is the “up to scale and offset” equivalence you want).

Differentiate:

1. First derivative:
   [
   \kappa'(\theta)
   = \alpha C'(\theta)
   = \alpha(\theta - \theta_*),g(\theta)
   ]
   (using (KL2)).

   But differentiating (S1) gives
   [
   \kappa'(\theta)
   = 2A I_1 I_1' + B(I_2' - 2 I_1 I_1')
   = B I_2' + (2A - 2B) I_1 I_1'.
   ]
   Using the moment identities for the exponential family, (I_1' = I_2 - I_1^2 = g(\theta)) and (I_2' = I_3 - I_1 I_2), this becomes a linear combination of **variance and third moment**:
   [
   \kappa'(\theta)
   = B\big(I_3 - I_1 I_2\big) + (2A-2B) I_1 g(\theta).
   ]

   Meanwhile, (C'(\theta) = (\theta - \theta_*)g(\theta)) depends only on the **variance** and the parameter difference.

   For these to be proportional for all (\theta), we would need a rigid relation of the form
   [
   B\big(I_3 - I_1 I_2\big) + (2A-2B) I_1 g(\theta) = \alpha (\theta -\theta_*) g(\theta)
   ]
   for all (\theta), which ties the **third moment** of the truncated geometric distribution to its mean, variance and parameter. For a general finite (N\ge 3), these are independent degrees of freedom; there’s no known identity of this form, and Bruna’s paper doesn’t impose such a constraint.

2. Even if you somehow solve that, the **second derivative** would have to obey
   [
   \kappa''(\theta) = \alpha C''(\theta)
   = \alpha\left[g(\theta) + (\theta - \theta_*)g'(\theta)\right].
   ]
   But (\kappa''(\theta)) from (S1) is a combination of first through fourth moments; matching this to the KL expression for all (\theta) would impose another set of nontrivial ODE-type constraints on (A(\theta)).

Given that (A(\theta)=\log\sum_{k=1}^N e^{\theta k}) for a finite geometric-like family, this is a very rigid analytic function. There is no hint in Bruna’s work (or standard exponential-family theory) of identities that would make (\kappa_{\text{Schur}}) and (D_{\mathrm{KL}}) proportional as functions of (\theta); they simply depend on **different combinations of the derivatives of (A)**.

### 3.4 What *can* be aligned?

There *are* two nice alignments you can get:

1. **Same minimum (Golden Lock-in)**
   If you choose the prior (p(\eta)) to be the golden-ratio point (x(q_*)), the complexity term (D_{\mathrm{KL}}(x(\theta)|x(\theta_*))) has its unique minimum at (\theta=\theta_*).
   Bruna proves that (\kappa_{\text{Schur}}(\theta)) (and the reduced functional (F_{\text{red}}) combining it with a mass term) has its unique stationary point at exactly the same (q_*=\varphi^{-2}) when (N) is a multiple of 12.

   So if you identify the “preferred prior” with the golden-ratio distribution, **both functionals select the same equilibrium point**.

2. **Same local quadratic behavior up to scaling**
   Near the minimum, both are convex functions of a single variable; their Taylor expansions are
   [
   C(\theta_*+\delta\theta) = \tfrac12 g(\theta_*),\delta\theta^2 + O(\delta\theta^3),
   ]
   [
   \kappa_{\text{Schur}}(\theta_*+\delta\theta)
   = \kappa_* + \kappa_2,\delta\theta^2 + O(\delta\theta^3),
   ]
   with (\kappa_2>0) by convexity. By choosing a coupling (\lambda) and additive constant appropriately, you can always arrange
   [
   \lambda \kappa_{\text{Schur}}(\theta) + \text{const}
   \approx C(\theta) \quad \text{to second order in }\delta\theta.
   ]

   This is exactly what happens in Ruppeiner-style thermodynamic geometry: *locally*, the scalar curvature or metric-based scalars and the free energy density are tightly tied together; globally, they differ.

So you get **local equivalence of minima and quadratic behavior**, but **not global functional equality**.

### 3.5 No “opposite predictions”

One thing *in favor* of your mapping is that both functionals are:

* Convex in (\theta);
* Unimodal with a unique minimum at the same point (if you pick the prior appropriately);
* Symmetry-respecting under the dihedral group.

This means that **gradient descent on either functional** (in (\theta)) will flow towards the same golden-ratio equilibrium and never disagree on which direction is “downhill”. So you will *not* find a parameter region where they give *opposite* predictions about stability – only differences in “how steep” the slope is.

---

## 4. Gap analysis

Here are the key gaps between your desired theorem and what we can actually support:

### 4.1 Missing generative model that yields (\kappa_{\text{Schur}})

To *derive* (\kappa_{\text{Schur}}) as the complexity term of a VFE, you would need:

1. A **specific generative model** (p(\eta,s)) on the dihedral-symmetric simplex such that
2. The **Hessian** of the VFE (or some reduced version of it) with respect to the variational parameters, after eliminating collective modes, is exactly the matrix (H(\theta)) Bruna starts with, whose Schur complement yields (\kappa_{\text{Schur}}).

Bruna’s paper is intentionally agnostic: (H(\theta)) is any DN-equivariant Hessian with a PSD exponential-sum dependence. It is *not derived* from a specific log-likelihood or KL divergence; it is a **structural object** satisfying convexity and symmetry assumptions.

Without specifying such a generative model, we’re missing the crucial step: mapping the **Hessian of log-likelihood / free energy** to Bruna’s (H(\theta)).

### 4.2 Curvature vs divergence

The nearest analogues in the literature are:

* Ruppeiner: curvature scalar (R) proportional (up to sign) to **correlation volume or inverse free energy density**.
* Gibilisco & Isola: conjectures that **scalar curvature is Schur-convex** and can be interpreted as “average statistical uncertainty”; in thermodynamic settings, they directly link **scalar curvature to free-energy density**.

But in all these cases, curvature is related to **derivatives of free energy**, not directly to a KL divergence between two probability distributions.

Friston’s VFE, by contrast, is explicitly a **KL divergence + energy term**.

So at best, one can hope for:

* (\kappa_{\text{Schur}}) being **proportional to a local free-energy density**, and
* that free-energy density being in turn related (via Massieu–Planck potentials or f-divergences) to **KL-type complexity**.

That’s a **two-step analogy**, not a direct equality.

### 4.3 Role of (\lambda)

In your axiom
[
F[\mathcal{G}] = E_{\text{strain}}[\mathcal{G}] + \lambda,\kappa_{\text{Schur}}[\mathcal{G}],
]
(\lambda) plays the same formal role as:

* An **inverse temperature / precision**, weighting the curvature term relative to strain, or
* A **regularization weight** in convex optimization.

In FEP, the complexity term’s weight is essentially **fixed at 1** (you can move “temperature-like” parameters into the likelihood), although “precision” parameters in the generative model modulate the relative influence of accuracy and complexity.

Interpreting (\lambda) as something like “effective temperature” is *natural*, but it’s **not derivable** from FEP as currently formulated. It’s a free phenomenological parameter.

### 4.4 Extension from (D_{12}) to (H_3)

Bruna’s result is in 1D (ring) dihedral symmetry. Extending to a full 3D (H_3) icosahedral quasicrystal would require:

* Defining appropriate **icosahedral exponential families** on higher-dimensional simplices or configuration spaces;
* Generalizing the **band/collective decomposition** and **Schur curvature** to that setting;
* Showing that convexity + (H_3) symmetry forces a unique stationary point corresponding to your desired golden-ratio scaling.

None of that exists yet in the literature; it’s conceptually plausible (group-theoretic machinery generalizes), but completely open.

---

## 5. Implications and verdict

Putting it all together:

### 5.1 What *is* well-supported

1. There is a mature literature where:

   * **Scalar curvature** of an information-geometric / thermodynamic metric is **proportional to free-energy density** or correlation volume.
   * Such curvature is conjectured (and in some cases proved) to be **Schur-convex** in the probability vector.

2. KL divergences and f-divergences are widely interpreted as **(negative) free entropies / Massieu–Planck potentials**, serving as free energies in generalized H-theorems and thermodynamic resource theories.

3. In FEP, variational free energy is **explicitly** a KL divergence + energy, and belief updates follow (approximate) **natural gradient descent** under the Fisher metric.

4. Bruna’s (\kappa_{\text{Schur}}) is a **Schur-convex curvature functional** on a (D_N)-equivariant exponential family, convex in (\theta), with a unique golden-ratio stationary point and a quadratic dependence on the mean and variance of the sufficient statistic.

5. If you choose the prior in the FEP setting to be the golden-ratio distribution (x(q_*)), then the **KL complexity term** and Bruna’s curvature-based (F_{\text{red}}) both have their **unique minima at (q_*)** and are **convex** in (\theta).

This makes your mapping

| VFE term   | Geometric analog                  |
| ---------- | --------------------------------- |
| inaccuracy | strain energy (E_{\text{strain}}) |
| complexity | curvature (\kappa_{\text{Schur}}) |

**structurally coherent** as a *design principle* for a geometric FEP.

### 5.2 What is *not* (yet) supported

1. There is **no theorem in the current literature** that identifies Bruna’s (\kappa_{\text{Schur}}) with KL complexity, even in special cases.

2. At the level of explicit formulas:

   * (\kappa_{\text{Schur}}(\theta)) is a **quadratic polynomial in (I_1(\theta)) and (\mathrm{Var}_{x(\theta)}[r])**.
   * (D_{\mathrm{KL}}(x(\theta)|x(\theta_*))) is a **Bregman divergence of the log-partition function** (A(\theta)).

   These are **different analytic objects**; making them equal for all (\theta) would require strong, nonstandard identities relating (A), (A') and (A'') that are not satisfied by the truncated geometric family.

3. The mapping from **“Hessian of a reduced functional”** to **“Hessian of VFE”** is undeveloped: we don’t have a generative model (p(\eta,s)) whose VFE Hessian yields Bruna’s (H(\theta)).

4. The role of (\lambda) as a **temperature-like parameter** is a reasonable modeling choice but not forced by the FEP formalism.

5. The extension from the 1D dihedral family to a full **3D (H_3) quasicrystal** is mathematically and physically open.

### 5.3 Final classification

Given all of this, I’d summarise:

* The idea that **“Schur-convex curvature acts like a free-energy density”** is **PLAUSIBLE** and has concrete support in thermodynamic and information-geometric literature (Ruppeiner, Gibilisco–Isola, etc.).
* The idea that **Bruna’s specific (\kappa_{\text{Schur}}) is literally equal (even up to affine transform) to the KL complexity term in Friston’s VFE** is **not supported by current results** and runs into structural mismatches at the level of explicit formulas.

So for *your* claim:

> **Hypothesis:** Bruna’s (\kappa_{\text{Schur}}) is mathematically equivalent to the complexity term in Friston’s VFE, when both are applied to dihedral-symmetric exponential families.

I’d label it:

> **Verdict: SPECULATIVE.**
> There is a strong and elegant **analogy** (both are convex, Schur-convex, and can share the same golden-ratio equilibrium under suitable priors), and they can be locally matched near that equilibrium. But no theorem currently establishes equality, and the analytic structures (quadratic-in-moments vs log-sum-exp divergence) make global equivalence unlikely without very special, as yet unspecified, generative assumptions.

---

### Where to go next (if you want to push this toward “PLAUSIBLE”)

If you want to sharpen this further toward a theorem (or a clean no-go result), concrete next steps would be:

1. **Specify a generative model** (p(\eta,s)) on the (D_N) simplex whose VFE Hessian matches Bruna’s (H(\theta)), or show this is impossible under reasonable assumptions.

2. **Work in Legendre variables**: express both (\kappa_{\text{Schur}}) and (D_{\mathrm{KL}}(q_\theta|q_{\theta_*})) purely as functionals of (A(\theta)) and its derivatives, then look for an ODE relating them; prove either the existence or nonexistence of such an ODE for finite (N).

3. **Numerical sanity checks**: for (N=12), plug Bruna’s explicit (A_{12}(2), B_{12}(2)) into (S1), compute (\kappa_{\text{Schur}}(\theta)) and the KL complexity to the golden-ratio prior over a grid of (\theta), and see how close they can be made with optimal scaling. If they cannot be made to agree even on a wide neighborhood, that strengthens the “non-equivalent but analogous” conclusion.

If you’d like, we can next sketch a concrete generative model that *does* make golden-ratio priors natural under FEP, and then see how to retrofit (\kappa_{\text{Schur}}) into that story as an emergent curvature term.


---
