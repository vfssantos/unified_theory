Short answer: **yes, on the 1-dimensional dihedral family you’re using, they *must* generate the same update direction everywhere** (and hence the same flow lines up to a re-timing) – *provided* you’re really doing gradient(-like) descent on θ (or q) within that family.

They can disagree in speed, but not in which way is “toward φ⁻²” and which way is “away”.

Let me spell that out cleanly.

---

## 1. Set-up: 1D manifold and two functionals

We’re working on the 1D manifold
[
\theta = \ln q \in (\theta_{\min},\theta_{\max}), \quad x(\theta)\in\Delta_N,
]
given by your folded dihedral exponential family.

Define two scalar functionals on this 1D parameter:

* **Curvature functional:** (f(\theta) := \kappa_{\text{Schur}}(\theta)).
* **Complexity functional:**
  (g(\theta) := D_{\mathrm{KL}}(x(\theta),|,p_{\text{golden}})),
  with (p_{\text{golden}} = x(\theta_*)) at (q_*=\varphi^{-2}).

From Bruna and exponential-family theory we have:

1. **Both are convex in (\theta)** on this interval.

   * Bruna: (\kappa_{\text{Schur}}(\theta)) convex in (\theta=\ln q).
   * KL: in an exponential family, (D_{\mathrm{KL}}(q_\theta|q_{\theta_*})) is a Bregman divergence of the convex log-partition (A(\theta)), hence convex in (\theta).

2. **They share the same unique minimizer (\theta_*)**:

   * Bruna’s “golden lock-in”: unique stationary point at (q_*=\varphi^{-2}\Rightarrow \theta_*=\ln \varphi^{-2}), and convexity ⇒ unique minimum there.
   * KL divergence to the golden distribution is uniquely minimized at that distribution itself, i.e. at (\theta_*).

3. Both are smooth (analytic) in (\theta) on the interior, so we can talk about usual derivatives.

This is *exactly* the situation where a clean convex-analysis lemma kicks in.

---

## 2. Convex-analysis lemma: gradients must have the same sign pattern

**Lemma (1D case).**
Let (f,g : (a,b)\to\mathbb{R}) be differentiable, convex functions with a *common, unique* minimizer (\theta_*\in(a,b)). Then:

* For all (\theta < \theta_*):
  (f'(\theta) \le 0) and (g'(\theta) \le 0).
* For all (\theta > \theta_*):
  (f'(\theta) \ge 0) and (g'(\theta) \ge 0).
* At (\theta = \theta_*):
  (f'(\theta_*) = g'(\theta_*) = 0).

So **the sign of the derivative of any such convex function is completely determined by whether you’re to the left or right of (\theta_*)**. Two such functions can *never* have opposite-sign gradients away from the minimum.

*Sketch of why this is true (without going into full proof detail):*

* For a differentiable convex function in 1D, the derivative (f'(\theta)) is **monotone non-decreasing** in (\theta).
* At the unique minimizer (\theta_*), we must have (f'(\theta_*) = 0).
* If there were a point (\theta > \theta_*) with (f'(\theta) < 0), then monotonicity of (f') implies
  (f'(\theta_*) \le f'(\theta) < 0), contradiction.
  So for all (\theta > \theta_*), (f'(\theta) \ge 0).
  Similarly, for (\theta < \theta_*), we must have (f'(\theta) \le 0).
* The same argument holds independently for (g).

Apply this to your case:

* (f(\theta)=\kappa_{\text{Schur}}(\theta)),
* (g(\theta)=D_{\mathrm{KL}}(x(\theta),|,p_{\text{golden}})),

with both convex and minimized at (\theta_*).

**Conclusion on the 1D manifold:**

* For (\theta<\theta_*):
  (\partial_\theta \kappa_{\text{Schur}}(\theta)\le 0),
  (\partial_\theta D_{\mathrm{KL}}(\theta)\le 0).
* For (\theta>\theta_*):
  both derivatives are (\ge 0).
* At (\theta_*): both derivatives vanish.

So **the gradients in (\theta)-space always point in the same direction** (or are zero at the golden point).

---

## 3. Gradient flows: same orbits, different clocks

Consider gradient descent (or gradient flow) in (\theta):

* **Curvature-driven flow**
  [
  \frac{d\theta}{dt} = -\partial_\theta \kappa_{\text{Schur}}(\theta).
  ]
* **KL-complexity-driven flow**
  [
  \frac{d\theta}{d\tau} = -\partial_\theta D_{\mathrm{KL}}(\theta).
  ]

Using the lemma above:

* For any (\theta \neq \theta_*),
  (\mathrm{sign}\big(\partial_\theta \kappa_{\text{Schur}}(\theta)\big)
  = \mathrm{sign}\big(\partial_\theta D_{\mathrm{KL}}(\theta)\big)).
* Therefore
  [
  \mathrm{sign}\left(\frac{d\theta}{dt}\right)
  = \mathrm{sign}\left(\frac{d\theta}{d\tau}\right)
  ]
  everywhere except at (\theta_*) (where both are zero).

This means:

* **Everywhere** on the line, both flows move (\theta) toward (\theta_*) or away from it in the *same* sense; they never disagree on which direction is “downhill”.
* The **only difference** is how *fast* they move: the magnitudes (|\partial_\theta \kappa_{\text{Schur}}|) and (|\partial_\theta D_{\mathrm{KL}}|) can be very different functions of (\theta).

In fact, you can define a positive scalar field
[
\alpha(\theta) :=
\frac{\partial_\theta D_{\mathrm{KL}}(\theta)}
{\partial_\theta \kappa_{\text{Schur}}(\theta)}
]
for (\theta\neq\theta_*), which is well-defined and positive because both derivatives share sign and only vanish at (\theta_*.)

Then (away from the minimum),
[
-\partial_\theta D_{\mathrm{KL}}(\theta)
= \alpha(\theta), \big(-\partial_\theta \kappa_{\text{Schur}}(\theta)\big).
]

This tells you:

> The two gradient vector fields on the 1D manifold are the **same up to a positive, state-dependent scalar.**

That is exactly the condition for having:

* **The same integral curves (orbits)** in (\theta)-space,
* but with a **reparameterization of time**: you can re-scale time along one flow to match the other.

So in the sense of “belief updating direction” (the path in belief space, not the literal step size), **yes: κ_Schur and D_KL generate the same gradient flow trajectories along the dihedral family.**

---

## 4. What about natural gradients and q-space?

Two natural follow-ups you might be thinking:

### 4.1 Natural gradient vs ordinary gradient

In FEP, belief updates are often described by **natural gradient flow**:
[
\frac{d\theta}{dt} \propto -g(\theta)^{-1},\partial_\theta F(\theta),
]
where (g(\theta)) is the Fisher information (the 1D Fisher metric here).

In 1D, (g(\theta)) is just a positive scalar (variance), so multiplying by (g(\theta)^{-1}>0) **cannot change the sign of the update**. It only scales the speed.

So if you plug in

* (F=\kappa_{\text{Schur}}), or
* (F=D_{\mathrm{KL}}),

the natural gradient flows still satisfy:

* direction set by (-\partial_\theta F),
* speed modulated by (g^{-1}),

and therefore your previous “same direction” result survives natural gradient corrections.

### 4.2 Working in q instead of θ

You might also prefer to think in terms of (q) directly. Since (\theta=\ln q), the map (q\mapsto\theta) is strictly **monotone increasing** on ((0,1)) with derivative (1/q>0).

If you set up gradient descent in q using the chain rule,
[
\frac{d q}{dt} = -\frac{\partial F}{\partial q}
= -\frac{\partial F}{\partial \theta}\frac{d\theta}{dq}
= -\frac{1}{q},\partial_\theta F(\theta),
]
then the sign of (\frac{dq}{dt}) is still just the sign of (-\partial_\theta F), since (1/q>0).

So all the 1D sign arguments lift directly to q-space:

* Both functionals drive q toward (q_*=\varphi^{-2}) from either side.
* No point where one wants to increase q and the other wants to decrease q.

---

## 5. Where this stops being guaranteed

Just to mark the boundary clearly:

* The argument above absolutely *relies* on:

  * 1D parameterization ((\theta) or (q)),
  * global convexity in that parameter,
  * a **shared unique minimizer**.

* If you:

  * move to the full ((N-1))-dimensional simplex (without the dihedral reduction), or
  * define two different convex functionals on a higher-dimensional parameter space that share only a common minimum,

  then their gradients **need not be parallel away from the minimum**. They’ll still both “point roughly toward” the minimum in a loose sense, but the vector fields can form different angles and produce genuinely different trajectories.

So your “same gradient flow dynamics” claim is safe and provable **on the 1D dihedral exponential family** under gradient (or natural-gradient) descent, but it does *not* automatically generalize to higher-dimensional belief manifolds.

---

## 6. Takeaway for the Golden Selection axiom

For the specific 1D folded dihedral family:

* If you treat **belief updating** as gradient(-like) flow on a scalar functional of (\theta),
* and you choose either

  * the **KL complexity** to the golden prior, or
  * Bruna’s **Schur curvature** (with the proven convexity and golden lock-in),

then:

> **The direction of belief updates at every point is the same; they trace the same path toward (q=\varphi^{-2}), up to a re-scaling of time.**

So even though (\kappa_{\text{Schur}}) and (D_{\mathrm{KL}}) are not equal as functions, using (\kappa_{\text{Schur}}) in your geometric free-energy functional will **not change the qualitative belief dynamics** along that symmetric family – it changes the “speed profile,” not the “route”.

If you’d like, the next step could be to write down the explicit ODEs for (q(t)) under both functionals and see how the time reparameterization between them looks (e.g., how “stiff” the curvature-based flow is near vs far from the golden point).
