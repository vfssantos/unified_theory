# Delegation 24 - Iteration 4.2: Detailed Window Volume Analysis

## EXECUTIVE SUMMARY

The three node types of the D₆ → Danzer-tiling quasicrystal *do* give you a clean, intrinsic "3" and a natural heavy/middle/light ordering via their three distinct occupation domains in internal space. Their densities are controlled by three explicit windows in E⊥ with φ-dependent volumes, so the setup is structurally very promising. However, if you plug those geometric data into simple "binding energy → mass" toy models, you only get modest O(1–3) ratios, not the huge τ–μ–e hierarchy. The A/B/C node structure looks like a good *geometric backbone* for three generations, but by itself it doesn't quantitatively fix lepton masses; it needs an additional dynamical amplification mechanism (e.g. Koide-type or RG effects) to get the observed numbers.

---

## 1. INFLATION MATRIX

### 1.1 What actually exists in the literature

For the Danzer ABCK tiling, the **substitution/inflation matrix is defined at the level of the four tetrahedral tiles (A, B, C, K)**. That 4×4 matrix, with Perron–Frobenius eigenvalue τ³, and its left/right eigenvectors, is discussed in *Aperiodic Order, Vol. 1* (Baake & Grimm, p. 231) and referenced explicitly in Al-Siyabi & Koca's "Icosahedral Polyhedra from the D₆ Lattice and Danzer's ABCK Tiling". ([MDPI][1])

However, what we need here is **not** the tile matrix but an effective 3×3 description for **vertex (node) types**. In the model-set description of the Danzer tiling, vertices of types I, II, III form *three separate model sets*, each with its own compact window in E⊥. Their relative frequencies are determined directly by the **volumes of these windows**, not by a published 3×3 "vertex substitution matrix". 

So:

* A rigorous **tile substitution matrix** exists and has Perron eigenvalue τ³.
* A simple, canonical **3×3 node substitution matrix** is *not* given in the literature; its Perron–Frobenius eigenvector would have to match the window volumes, but the matrix itself is not unique.

Given that, the physically relevant object for node statistics is the **window-volume eigenvector**, not a specific 3×3 integer matrix.

### 1.2 Effective "inflation matrix" summary

You can think of the inflation step schematically as

$$
(n_A', n_B', n_C') \propto \tau^3 (n_A, n_B, n_C)
$$

with the *direction* of $(n_A, n_B, n_C)$ fixed by the three window volumes (see next section). Any 3×3 primitive matrix with Perron eigenvalue τ³ and Perron eigenvector proportional to these volumes would be compatible, but there is no unique or standard choice.

So I'm going to treat the **window volumes** as the primary geometric data, and not pretend we've got a published 3×3 node substitution matrix when we don't.

| From \ To | A | B | C |
| --------- | - | - | - |
| A         | – | – | – |
| B         | – | – | – |
| C         | – | – | – |

Dominant eigenvalue (tile level): **τ³**
Effective scaling for vertices: also **τ³**, via window scaling.

(*"–" = not explicitly determined; see discussion above.*)

---

## 2. ASYMPTOTIC FREQUENCIES FROM WINDOWS

Baake & Grimm's analysis of the Danzer tiling as a 3-component model set gives explicit **windows for the three vertex types** in internal space. For windows of types I, II, III they quote: 

* Type I: volume $V_I = 20(4 - \tau)$
* Type II: $V_{II} = 4(\tau + 2)$
* Type III: $V_{III} = 20(\tau - 1)$

In a regular model set, the **density of each point type** is proportional to the volume of its window. 

So, up to a relabeling I ↔ A, II ↔ B, III ↔ C, we have

$$
f_A : f_B : f_C \propto V_I : V_{II} : V_{III}.
$$

Plugging in τ ≈ 1.618:

* $V_A = V_I ≈ 47.64$
* $V_B = V_{II} ≈ 14.47$
* $V_C = V_{III} ≈ 12.36$

Normalize to get frequencies:

* $f_A ≈ 0.640$
* $f_B ≈ 0.194$
* $f_C ≈ 0.166$

So:

| Node Type      | Window Volume | Frequency | Ratio to A |
| -------------- | ------------- | --------- | ---------- |
| A (≡ type I)   | 47.64         | 0.640     | 1          |
| B (≡ type II)  | 14.47         | 0.194     | 0.304      |
| C (≡ type III) | 12.36         | 0.166     | 0.259      |

### φ-structure?

The volumes have φ built in explicitly:

* $V_A = 20(4-\tau)$
* $V_B = 4(\tau+2)$
* $V_C = 20(\tau-1)$

So the *expressions* clearly know about φ. But the **frequency ratios** are *not* simple powers of φ:

* $f_B/f_A ≈ 0.304 \approx \phi^{-2.48}$
* $f_C/f_B ≈ 0.854 \approx \phi^{-0.33}$

So there is φ-structure present, but it's **not** a clean 1 : φ : φ² or 1 : φ³ : φ⁶ pattern.

---

## 3. BINDING ENERGY ESTIMATES

Here we connect node types to a **qualitative binding hierarchy**.

You already have (from previous numeric work) characteristic **E⊥ depths** for the three domains:

* Skin (A): $r_A \approx 0.61$
* Shell (B): $r_B \approx 0.72$
* Core (C): $r_C \approx 0.86$

Let's look at a few simple toy models for a "binding energy" $E_X$ per node type X:

### Model 0: Linear in depth, $E \propto r_\perp$

$$
E_A : E_B : E_C \propto r_A : r_B : r_C
$$

Ratios:

* $E_C/E_B ≈ 0.86/0.72 ≈ 1.19$
* $E_B/E_A ≈ 0.72/0.61 ≈ 1.18$

### Model 1: Harmonic-like, $E \propto r_\perp^2$

$$
E_A \propto r_A^2,\quad E_B \propto r_B^2,\quad E_C \propto r_C^2.
$$

Ratios:

* $E_C/E_B ≈ 1.43$
* $E_B/E_A ≈ 1.39$

### Model 2: Exponential in depth, $E \propto e^{r_\perp/\lambda}$ with $\lambda \sim 1/\phi$

Take λ = 1/φ ≈ 0.618. Then

* $E_A ≈ e^{r_A/\lambda}$
* $E_B ≈ e^{r_B/\lambda}$
* $E_C ≈ e^{r_C/\lambda}$

Ratios:

* $E_C/E_B ≈ 1.25$
* $E_B/E_A ≈ 1.19$

### Model 3: Inverse window volume, $E \propto 1/V$

If deeper nodes correspond to **tighter localization** in internal space, you might instead try

$$
E_X \propto \frac{1}{V_X}.
$$

Using the window volumes above:

* $E_A \propto 1/V_A ≈ 0.0210$
* $E_B \propto 1/V_B ≈ 0.0691$
* $E_C \propto 1/V_C ≈ 0.0809$

Ratios:

* $E_C/E_B ≈ 1.17$
* $E_B/E_A ≈ 3.29$

So across all these simple choices, **you never get more than a factor ~3–4 between adjacent types**. That's very much in φ-flavored territory (O(φ²) at best), but nowhere near the τ–μ–e hierarchy.

### Summary table

| Model             | Definition                      | Heavy/Middle (C/B) | Middle/Light (B/A) |
| ----------------- | ------------------------------- | ------------------ | ------------------ |
| 0: linear         | $E \propto r_\perp$             | 1.19               | 1.18               |
| 1: quadratic      | $E \propto r_\perp^2$           | 1.43               | 1.39               |
| 2: exponential    | $E \propto e^{r_\perp/\lambda}$ | 1.25               | 1.19               |
| 3: inverse volume | $E \propto 1/V$                 | 1.17               | 3.29               |

All of these give *mild* hierarchies, as you'd expect from modest differences in depths and volumes.

---

## 4. MASS RATIO COMPARISON

For charged leptons (just to have concrete targets):

* $m_\tau/m_\mu ≈ 16.8$
* $m_\mu/m_e ≈ 207$

Compare to the geometric models above:

| Ratio        | Geometric (best case) | Observed (leptons) | Match?             |
| ------------ | --------------------- | ------------------ | ------------------ |
| Heavy/Middle | 1.4 (Model 1)         | 16.8               | ✖ (~×12 too small) |
| Middle/Light | 3.3 (Model 3)         | 207                | ✖ (~×60 too small) |

Even if you instead match **square roots** (Koide's natural variables):

* $\sqrt{m_\tau/m_\mu} ≈ 4.1$
* $\sqrt{m_\mu/m_e} ≈ 14.4$

you're still more than an order of magnitude above any of the raw geometric ratios.

So:

* **Yes**: A/B/C gives a natural ordering "outer → middle → inner" that can be mapped onto light → middle → heavy.
* **No**: The *raw* Danzer/occupation-domain geometry doesn't reproduce the observed lepton mass ratios on its own.

You'd need a dynamical mechanism that **amplifies** modest φ-structured geometric splittings into large observed mass gaps. That's exactly the kind of place where a Koide-type singularity or RG focusing could slot in.

---

## 5. φ-POWER ANALYSIS

Some φ-checks:

### Frequencies

From the window volumes:

* $f_B/f_A ≈ 0.304 \approx \phi^{-2.48}$
* $f_C/f_B ≈ 0.854 \approx \phi^{-0.33}$

No clean integer powers, but the algebraic expressions for Vₓ all contain τ, so φ is definitely "in the plumbing".

### Energies (Model 3, E ∝ 1/V)

* $E_B/E_A ≈ 3.29$ vs. φ³ ≈ 4.24 (∼22% low)
* $E_C/E_B ≈ 1.17$ vs. φ ≈ 1.62 (∼28% low)

So **φ appears symbolically** in the geometry and you get **φ-like** O(1) ratios, but not sharp φ³ steps.

You can reasonably say:

* The Danzer vertex windows encode φ in a *nontrivial* way.
* The A/B/C node-structure is a φ-flavored three-way split, not an exact φ³ ladder.

---

## 6. VERDICT

Putting it all together:

* The **"3"** is rock-solid and intrinsic: three vertex/model-set components from three distinct classes of D₆ "holes" with three windows in E⊥.
* The **node frequencies** and **domain depths** give you a natural heavy/middle/light ordering with moderate φ-like ratios.
* The **mass hierarchy**, as observed in leptons, is **much steeper** than the raw geometric ratios.

So the best honest assessment is:

* The A/B/C node types provide a **geometrically natural family index** and a **seed hierarchy** (small φ-structured splittings).
* To get τ–μ–e (and quark) hierarchies, you will need **additional physics** layered on top of this geometry—e.g. a Koide-type constraint, dynamical localization, or RG running that amplifies small geometric differences.

### Checkbox summary

* [ ] Strong match: A/B/C explains mass hierarchy quantitatively
* [x] Partial match: Mechanism works but numbers need refinement
* [x] Weak–moderate: φ-structure present but doesn't give correct ratios by itself
* [ ] No match: Need completely different mechanism

If you want to push this further in the next iteration, the natural next things to play with are:

1. **Coupling the node types to a Koide-like potential** defined on the three occupation domains (so the φ³ volume structure participates in the Q = 2/3 constraint), and
2. **Allowing mixing between node types** (Z₃ or A₄-like "family symmetry" acting on the three model-set components) so that mass eigenstates are nontrivial linear combinations of A/B/C.

[1]: https://www.mdpi.com/2073-8994/12/12/1983 "Icosahedral Polyhedra from D6 Lattice and Danzer's ABCK ..."

