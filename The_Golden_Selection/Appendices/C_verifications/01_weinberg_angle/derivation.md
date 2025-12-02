# Weinberg Angle: Full Derivation

## Overview

This document provides the complete step-by-step derivation of the Weinberg angle from D₆ → H₃ projection geometry, with all algebraic details.

**Result**:
$$\sin^2\theta_W = \frac{393 - 75\sqrt{5}}{968} \approx 0.2327$$

---

## Step 1: The Projection Matrix

The Koca–Al-Siyabi D₆ → H₃ projection is:

$$P = \frac{1}{\sqrt{5+\sqrt{5}}} \begin{pmatrix} 1 & -1 & 0 & 0 & \varphi & -\varphi \\ \varphi & \varphi & 1 & 1 & 0 & 0 \\ 0 & 0 & \varphi & -\varphi & 1 & 1 \end{pmatrix}$$

where $\varphi = \frac{1+\sqrt{5}}{2}$.

**Key properties**:
- $\varphi^2 = \varphi + 1$
- $\varphi^{-1} = \varphi - 1$
- $(1-\varphi)^2 = \varphi^{-2} = 2 - \varphi$
- $5 + \sqrt{5} = 5 + (\varphi + \varphi^{-1}) = 5 + 2\varphi - 1 = 4 + 2\varphi$

---

## Step 2: SU(2) Generator Projection

The SU(2)$_L$ generator (neutral component $W^3$) is:

$$W^3 = (0, 0, 0, 1, -1, 0)$$

**Projection calculation**:

$$\vec{x}_{SU2} = P \cdot W^3 = \frac{1}{\sqrt{5+\sqrt{5}}} \begin{pmatrix} 0 + 0 + 0 + 0 + \varphi \cdot 1 + (-\varphi)(-1) \\ 0 + 0 + 0 + 1 + 0 + 0 \\ 0 + 0 + 0 + (-\varphi) + 1 + 0 \end{pmatrix}$$

$$= \frac{1}{\sqrt{5+\sqrt{5}}} \begin{pmatrix} 2\varphi \\ 1 \\ 1 - \varphi \end{pmatrix}$$

**Squared length**:

$$|\vec{x}_{SU2}|^2 = \frac{1}{5+\sqrt{5}} \left[ (2\varphi)^2 + 1 + (1-\varphi)^2 \right]$$

$$= \frac{1}{5+\sqrt{5}} \left[ 4\varphi^2 + 1 + 1 - 2\varphi + \varphi^2 \right]$$

$$= \frac{1}{5+\sqrt{5}} \left[ 5\varphi^2 + 2 - 2\varphi \right]$$

Using $\varphi^2 = \varphi + 1$:

$$= \frac{1}{5+\sqrt{5}} \left[ 5(\varphi + 1) + 2 - 2\varphi \right]$$

$$= \frac{1}{5+\sqrt{5}} \left[ 5\varphi + 5 + 2 - 2\varphi \right]$$

$$= \frac{3\varphi + 7}{5+\sqrt{5}}$$

Now $3\varphi = \frac{3(1+\sqrt{5})}{2} = \frac{3+3\sqrt{5}}{2}$, so:

$$3\varphi + 7 = \frac{3 + 3\sqrt{5}}{2} + 7 = \frac{17 + 3\sqrt{5}}{2}$$

And $5 + \sqrt{5} = \frac{10 + 2\sqrt{5}}{2}$.

Therefore:

$$|\vec{x}_{SU2}|^2 = \frac{17 + 3\sqrt{5}}{10 + 2\sqrt{5}} = \frac{17 + 3\sqrt{5}}{2(5 + \sqrt{5})}$$

**Rationalize**:

Multiply by $\frac{5 - \sqrt{5}}{5 - \sqrt{5}}$:

$$= \frac{(17 + 3\sqrt{5})(5 - \sqrt{5})}{2(5 + \sqrt{5})(5 - \sqrt{5})} = \frac{(17 + 3\sqrt{5})(5 - \sqrt{5})}{2(25 - 5)}$$

$$= \frac{85 - 17\sqrt{5} + 15\sqrt{5} - 3 \cdot 5}{40} = \frac{85 - 15 - 2\sqrt{5}}{40} = \frac{70 - 2\sqrt{5}}{40}$$

$$= \frac{35 - \sqrt{5}}{20} = \frac{35}{20} - \frac{\sqrt{5}}{20} = \frac{7}{4} - \frac{\sqrt{5}}{20}$$

Hmm, this doesn't simplify to $1 + \sqrt{5}/5$ directly. Let me verify numerically:

$$1 + \frac{\sqrt{5}}{5} = 1 + \frac{2.236...}{5} = 1 + 0.4472... = 1.4472...$$

$$\frac{35 - \sqrt{5}}{20} = \frac{35 - 2.236...}{20} = \frac{32.76...}{20} = 1.638...$$

There's an error in my algebra. Let me redo with the correct normalization.

**Correct calculation** (verified numerically):

The projection matrix has normalization $N = \sqrt{5 + \sqrt{5}} \approx 2.5344$.

For $W^3 = (0, 0, 0, 1, -1, 0)$:

$$\vec{x}_{SU2} = \frac{1}{N} \begin{pmatrix} 0 - 0 + 0 + 0 + \varphi(1) + (-\varphi)(-1) \\ \varphi(0) + \varphi(0) + 1 + 1 + 0 + 0 \\ 0 + 0 + \varphi(1) + (-\varphi)(-1) + 1 + (-1) \end{pmatrix}$$

Wait, I need to be more careful. The projection matrix rows are:
- Row 1: $[1, -1, 0, 0, \varphi, -\varphi]$
- Row 2: $[\varphi, \varphi, 1, 1, 0, 0]$
- Row 3: $[0, 0, \varphi, -\varphi, 1, 1]$

Dotting with $W^3 = [0, 0, 0, 1, -1, 0]$:
- Component 1: $1(0) + (-1)(0) + 0(0) + 0(1) + \varphi(-1) + (-\varphi)(0) = -\varphi$
- Component 2: $\varphi(0) + \varphi(0) + 1(0) + 1(1) + 0(-1) + 0(0) = 1$
- Component 3: $0(0) + 0(0) + \varphi(0) + (-\varphi)(1) + 1(-1) + 1(0) = -\varphi - 1$

So:

$$\vec{x}_{SU2} = \frac{1}{N} \begin{pmatrix} -\varphi \\ 1 \\ -\varphi - 1 \end{pmatrix}$$

**Squared length**:

$$|\vec{x}_{SU2}|^2 = \frac{1}{5+\sqrt{5}} \left[ \varphi^2 + 1 + (\varphi + 1)^2 \right]$$

$$= \frac{1}{5+\sqrt{5}} \left[ \varphi^2 + 1 + \varphi^2 + 2\varphi + 1 \right]$$

$$= \frac{2\varphi^2 + 2\varphi + 2}{5+\sqrt{5}}$$

Using $\varphi^2 = \varphi + 1$:

$$= \frac{2(\varphi + 1) + 2\varphi + 2}{5+\sqrt{5}} = \frac{4\varphi + 4}{5+\sqrt{5}} = \frac{4(\varphi + 1)}{5+\sqrt{5}}$$

$$= \frac{4\varphi^2}{5+\sqrt{5}}$$

Now $\varphi^2 = \varphi + 1 = \frac{3+\sqrt{5}}{2}$.

So: $4\varphi^2 = 2(3+\sqrt{5}) = 6 + 2\sqrt{5}$.

And: $5 + \sqrt{5}$.

$$|\vec{x}_{SU2}|^2 = \frac{6 + 2\sqrt{5}}{5+\sqrt{5}}$$

**Rationalize**:

$$= \frac{(6 + 2\sqrt{5})(5 - \sqrt{5})}{(5+\sqrt{5})(5-\sqrt{5})} = \frac{30 - 6\sqrt{5} + 10\sqrt{5} - 2 \cdot 5}{25 - 5}$$

$$= \frac{30 - 10 + 4\sqrt{5}}{20} = \frac{20 + 4\sqrt{5}}{20} = 1 + \frac{\sqrt{5}}{5}$$

$$\boxed{|\vec{x}_{SU2}|^2 = 1 + \frac{\sqrt{5}}{5} \approx 1.4472}$$ ✓

---

## Step 3: U(1) Generator Projection

The hypercharge direction in SU(5) convention (unnormalized):

$$Y_{\text{raw}} = \left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}, -\frac{1}{2}, -\frac{1}{2}, 0\right)$$

**Squared length of raw vector**:

$$|Y_{\text{raw}}|^2 = 3 \cdot \frac{1}{9} + 2 \cdot \frac{1}{4} = \frac{1}{3} + \frac{1}{2} = \frac{5}{6}$$

**Normalization**: To match SU(5) convention where roots have $|α|^2 = 2$, we scale:

$$Y = Y_{\text{raw}} \cdot \sqrt{\frac{2}{5/6}} = Y_{\text{raw}} \cdot \sqrt{\frac{12}{5}}$$

**Projection of Y_raw**:

Let $N = \sqrt{5+\sqrt{5}}$ and compute $P \cdot Y_{\text{raw}}$:

Component 1:
$$\frac{1}{N}\left[1 \cdot \frac{1}{3} + (-1) \cdot \frac{1}{3} + 0 + 0 \cdot (-\frac{1}{2}) + \varphi \cdot (-\frac{1}{2}) + (-\varphi) \cdot 0\right]$$
$$= \frac{1}{N}\left[\frac{1}{3} - \frac{1}{3} - \frac{\varphi}{2}\right] = \frac{-\varphi}{2N}$$

Component 2:
$$\frac{1}{N}\left[\varphi \cdot \frac{1}{3} + \varphi \cdot \frac{1}{3} + 1 \cdot \frac{1}{3} + 1 \cdot (-\frac{1}{2}) + 0 + 0\right]$$
$$= \frac{1}{N}\left[\frac{2\varphi}{3} + \frac{1}{3} - \frac{1}{2}\right] = \frac{1}{N}\left[\frac{4\varphi + 2 - 3}{6}\right] = \frac{4\varphi - 1}{6N}$$

Component 3:
$$\frac{1}{N}\left[0 + 0 + \varphi \cdot \frac{1}{3} + (-\varphi) \cdot (-\frac{1}{2}) + 1 \cdot (-\frac{1}{2}) + 1 \cdot 0\right]$$
$$= \frac{1}{N}\left[\frac{\varphi}{3} + \frac{\varphi}{2} - \frac{1}{2}\right] = \frac{1}{N}\left[\frac{2\varphi + 3\varphi - 3}{6}\right] = \frac{5\varphi - 3}{6N}$$

**Squared length of projected Y_raw**:

$$|\vec{x}_{Y_{\text{raw}}}|^2 = \frac{1}{N^2}\left[\frac{\varphi^2}{4} + \frac{(4\varphi - 1)^2}{36} + \frac{(5\varphi - 3)^2}{36}\right]$$

Expand each term using $\varphi^2 = \varphi + 1$:
- $\frac{\varphi^2}{4} = \frac{\varphi + 1}{4}$
- $\frac{(4\varphi - 1)^2}{36} = \frac{16\varphi^2 - 8\varphi + 1}{36} = \frac{16(\varphi + 1) - 8\varphi + 1}{36} = \frac{8\varphi + 17}{36}$
- $\frac{(5\varphi - 3)^2}{36} = \frac{25\varphi^2 - 30\varphi + 9}{36} = \frac{25(\varphi + 1) - 30\varphi + 9}{36} = \frac{-5\varphi + 34}{36}$

Sum with common denominator 36:
$$= \frac{9(\varphi + 1) + (8\varphi + 17) + (-5\varphi + 34)}{36} = \frac{9\varphi + 9 + 8\varphi + 17 - 5\varphi + 34}{36} = \frac{12\varphi + 60}{36} = \frac{\varphi + 5}{3}$$

So:
$$|\vec{x}_{Y_{\text{raw}}}|^2 = \frac{\varphi + 5}{3N^2} = \frac{\varphi + 5}{3(5 + \sqrt{5})}$$

With $\varphi = \frac{1 + \sqrt{5}}{2}$, we have $\varphi + 5 = \frac{11 + \sqrt{5}}{2}$.

$$= \frac{11 + \sqrt{5}}{6(5 + \sqrt{5})}$$

**Rationalize** by multiplying by $\frac{5 - \sqrt{5}}{5 - \sqrt{5}}$:

$$= \frac{(11 + \sqrt{5})(5 - \sqrt{5})}{6(25 - 5)} = \frac{55 - 11\sqrt{5} + 5\sqrt{5} - 5}{120} = \frac{50 - 6\sqrt{5}}{120} = \frac{25 - 3\sqrt{5}}{60}$$

**After normalization** (scaling by $\frac{12}{5}$ for $|Y|^2 = 2$):

$$|\vec{x}_{U1}|^2 = \frac{12}{5} \times \frac{25 - 3\sqrt{5}}{60} = \frac{12(25 - 3\sqrt{5})}{300} = \frac{300 - 36\sqrt{5}}{300} = 1 - \frac{3\sqrt{5}}{25}$$

$$\boxed{|\vec{x}_{U1}|^2 = 1 - \frac{3\sqrt{5}}{25} = \frac{25 - 3\sqrt{5}}{25} \approx 0.7317}$$ ✓

---

## Step 4: The Ratio ρ

$$\rho = \frac{|\vec{x}_{SU2}|^2}{|\vec{x}_{U1}|^2} = \frac{1.4472...}{0.7317...} \approx 1.9780$$

**Exact algebraic form** (from symbolic computation):

$$\boxed{\rho = \frac{10\sqrt{5} + 35}{29}}$$

**Verification**:
$$\frac{10\sqrt{5} + 35}{29} = \frac{10 \cdot 2.236... + 35}{29} = \frac{22.36... + 35}{29} = \frac{57.36...}{29} = 1.9779...$$  ✓

---

## Step 5: Weinberg Angle Formula

The GUT normalization gives:

$$\sin^2\theta_W = \frac{1}{1 + \frac{5}{3}\rho}$$

Substituting $\rho = \frac{10\sqrt{5} + 35}{29}$:

$$\sin^2\theta_W = \frac{1}{1 + \frac{5}{3} \cdot \frac{10\sqrt{5} + 35}{29}}$$

$$= \frac{1}{\frac{29 + \frac{5(10\sqrt{5} + 35)}{3}}{29}}$$

$$= \frac{29}{29 + \frac{50\sqrt{5} + 175}{3}}$$

$$= \frac{29}{\frac{87 + 50\sqrt{5} + 175}{3}}$$

$$= \frac{3 \cdot 29}{262 + 50\sqrt{5}}$$

$$= \frac{87}{262 + 50\sqrt{5}}$$

---

## Step 6: Rationalization

Multiply by $\frac{262 - 50\sqrt{5}}{262 - 50\sqrt{5}}$:

$$\sin^2\theta_W = \frac{87(262 - 50\sqrt{5})}{262^2 - (50\sqrt{5})^2}$$

**Denominator**:
$$262^2 - 50^2 \cdot 5 = 68644 - 12500 = 56144$$

**Numerator**:
$$87 \cdot 262 - 87 \cdot 50\sqrt{5} = 22794 - 4350\sqrt{5}$$

So:
$$\sin^2\theta_W = \frac{22794 - 4350\sqrt{5}}{56144}$$

**Simplify**: Find GCD of 22794, 4350, and 56144.

$22794 = 2 \cdot 3 \cdot 3799$
$4350 = 2 \cdot 3 \cdot 725 = 2 \cdot 3 \cdot 5^2 \cdot 29$
$56144 = 2^4 \cdot 3509 = 2^4 \cdot 11 \cdot 319$

Actually, let's factor 56144:
$56144 / 2 = 28072$
$28072 / 2 = 14036$
$14036 / 2 = 7018$
$7018 / 2 = 3509$
$3509 = 11 \cdot 319 = 11 \cdot 11 \cdot 29 = 121 \cdot 29$

So $56144 = 16 \cdot 11^2 \cdot 29 = 16 \cdot 121 \cdot 29$.

Hmm, let me try dividing by 58:
$22794 / 58 = 393$ ✓
$4350 / 58 = 75$ ✓
$56144 / 58 = 968$ ✓

So GCD is 58.

$$\boxed{\sin^2\theta_W = \frac{393 - 75\sqrt{5}}{968}}$$

---

## Step 7: Numerical Verification

$$\sin^2\theta_W = \frac{393 - 75\sqrt{5}}{968} = \frac{393 - 75 \cdot 2.2360679...}{968}$$

$$= \frac{393 - 167.705...}{968} = \frac{225.295...}{968} = 0.23274...$$

**Experimental value**: $\sin^2\theta_W(M_Z) = 0.23121 \pm 0.00004$

**Error**: $\frac{0.2327 - 0.2312}{0.2312} = 0.67\%$

---

## Summary

| Quantity | Algebraic Form | Numerical Value |
|----------|----------------|-----------------|
| $\|x_{SU2}\|^2$ | $1 + \frac{\sqrt{5}}{5} = \frac{5 + \sqrt{5}}{5}$ | 1.4472 |
| $\|x_{U1}\|^2$ | $1 - \frac{3\sqrt{5}}{25} = \frac{25 - 3\sqrt{5}}{25}$ | 0.7317 |
| $\rho$ | $\frac{35 + 10\sqrt{5}}{29}$ | 1.9780 |
| $\sin^2\theta_W$ | $\frac{393 - 75\sqrt{5}}{968}$ | **0.2327** |
| Experimental | — | 0.23121 |
| Error | — | **0.67%** |

