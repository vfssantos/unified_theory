# Delegation 16, Iteration 3: Intra-Band Structure, Koide, and Particle Mapping

## 1. BACKGROUND

Iterations 1 and 2 established that the product-weighted internal Laplacian (L⊥) on the D₆ → H₃ quasicrystal produces:

- **Exact φ⁴** on the 60 D₆ roots (sparse graph)
- **φ², φ⁴, φ⁶ to ~0.1%** on the 160 ω₃ weights
- **4-band structure** with strong shell localization (20/60/60/20)
- **S₄ anomaly**: S₄ doesn't fit the φ-ladder → interpreted as Higgs/UV sector, not a generation

This resolves "Why 3 generations?" — S₁, S₂, S₃ are the 3 generations; S₄ is special.

**But critical questions remain:**

1. **Intra-band structure**: Each band has internal spread (especially S₂ with 3.1× spread). Which specific eigenvalue corresponds to which particle?
2. **Koide ratio**: Q = 2/3 does NOT appear in eigenvalue ratios. Does it appear in eigenvector overlaps?
3. **15/11 ratio**: This appears as an intra-band ratio inside S₂. What does it mean physically?
4. **Overall mass scale**: What sets κ in m = κ√λ?

---

## 2. COMPUTATION GOALS

### Goal A: Intra-Band Eigenvalue Analysis

For each band (S₁, S₂, S₃, S₄), analyze the **internal structure**:

1. List all distinct eigenvalues within each band
2. Compute all pairwise ratios within each band
3. Check for φ-power ratios (φ, φ², φ³, etc.) within bands
4. Check for ratios matching known mass ratios:
   - Lepton: m_μ/m_e ≈ 206.8, m_τ/m_μ ≈ 16.8, m_τ/m_e ≈ 3477
   - Quark: m_c/m_u ≈ 500, m_t/m_c ≈ 136, m_s/m_d ≈ 20, m_b/m_s ≈ 50

### Goal B: Eigenvector Overlap Analysis (Koide)

The Koide formula involves √m, suggesting amplitudes matter. Compute:

1. For each pair of shell-localized eigenvectors (ψ_i, ψ_j), compute the overlap:
   $$O_{ij} = |\langle \psi_i | \psi_j \rangle|^2$$

2. For triplets of eigenvectors (one from each of S₁, S₂, S₃), compute:
   $$Q = \frac{\lambda_1 + \lambda_2 + \lambda_3}{(\sqrt{\lambda_1} + \sqrt{\lambda_2} + \sqrt{\lambda_3})^2}$$
   
   Check if any triplet gives Q ≈ 2/3.

3. Also try with eigenvector-weighted combinations:
   $$Q' = \frac{\sum_i w_i \lambda_i}{(\sum_i w_i \sqrt{\lambda_i})^2}$$
   
   where w_i could be overlap-based weights.

### Goal C: 15/11 Investigation

The ratio 15/11 ≈ 1.3636 appeared as an intra-band ratio inside S₂:
- λ ≈ 16.84 and λ ≈ 22.97, both S₂-dominated
- Error from 15/11: ~0.016%

Investigate:
1. What are the degeneracies of these eigenvalues?
2. What is the geometric meaning of these specific eigenvectors?
3. Is there a pattern connecting 15/11 to other ratios?

### Goal D: A₂ Subalgebra Structure

The 120° twist between SU(2) and SU(3) suggests A₂ geometry. The Koide formula has 120° phase structure.

1. Identify the A₂ subalgebra roots within D₆
2. Project them to H₃ and check their placement on shells
3. Look for triplets of eigenvalues/eigenvectors that form A₂-like 120° structures
4. Check if Koide emerges from this A₂ structure

---

## 3. INPUTS (Same as before)

1. **ω₃ Weight Orbit**: 160 weights from Weyl orbit of (1,1,1,0,0,0)
2. **Koca–Al-Siyabi Projection**: Same P_∥ matrix
3. **Product-weighted L⊥**: Same w_ij = ξ_i · ξ_j
4. **All 160 eigenvalues and eigenvectors** from iter_2

---

## 4. DETAILED STEPS

### Step 1: Intra-Band Analysis

For each band S_k:
```python
# Get eigenvalues in this band
band_evals = [evals[i] for i in range(len(evals)) if dominant_shell[i] == k]

# All pairwise ratios
for i, ev_i in enumerate(band_evals):
    for j, ev_j in enumerate(band_evals):
        if i < j:
            ratio = ev_j / ev_i
            # Check against targets
```

**Targets to check:**
- φ^n for n = 1, 2, 3, 4, 5, 6
- 15/11, 11/15
- 2/3, 3/2
- Known mass ratios (see Goal A)

### Step 2: Eigenvector Overlaps

```python
# For all pairs of eigenvectors
for i in range(160):
    for j in range(i+1, 160):
        overlap = np.abs(np.dot(evecs[:,i], evecs[:,j]))**2
        # Store if significant
```

Note: For a graph Laplacian, eigenvectors are orthonormal, so overlaps are 0 for different eigenvalues. Instead, compute **shell-projected overlaps**:

$$O_{ij}^{(k)} = \sum_{v \in S_k} \psi_i(v) \psi_j(v)$$

This measures how much two eigenvectors "share" amplitude on shell S_k.

### Step 3: Koide Triplet Search

```python
# For all triplets (one from each generation band)
for i in S1_indices:
    for j in S2_indices:
        for k in S3_indices:
            l1, l2, l3 = evals[i], evals[j], evals[k]
            Q = (l1 + l2 + l3) / (np.sqrt(l1) + np.sqrt(l2) + np.sqrt(l3))**2
            if abs(Q - 2/3) < 0.01:
                # Found a Koide triplet!
```

### Step 4: A₂ Structure

The A₂ simple roots in D₆ are:
- α₁ = e₁ - e₂
- α₂ = e₂ - e₃

The full A₂ root system:
- ±(e₁ - e₂), ±(e₂ - e₃), ±(e₁ - e₃)

Project these to H₃ and identify their shell placement.

---

## 5. DELIVERABLES

### 5.1 Intra-Band Structure Table

For each band:

| Band | # Eigenvalues | λ_min | λ_max | Spread | Notable Ratios |
|------|---------------|-------|-------|--------|----------------|
| S₁ | 20 | ... | ... | ... | ... |
| S₂ | 63 | ... | ... | ... | 15/11 at (..., ...) |
| S₃ | 56 | ... | ... | ... | ... |
| S₄ | 20 | ... | ... | ... | ... |

### 5.2 Koide Search Results

| Triplet (λ₁, λ₂, λ₃) | Shells | Q | Error from 2/3 |
|----------------------|--------|---|----------------|
| (best match) | S₁, S₂, S₃ | ... | ...% |
| ... | ... | ... | ... |

### 5.3 Eigenvector Overlap Matrix

Heatmap or table showing shell-projected overlaps between generation bands.

### 5.4 A₂ Structure Analysis

- A₂ root projections and shell placement
- Any 120° structures found in eigenvectors
- Connection to Koide (if any)

### 5.5 15/11 Analysis

- Which eigenvectors give 15/11?
- Their geometric interpretation
- Connection to Higgs mass (if any)

---

## 6. KEY QUESTIONS TO ANSWER

| Question | Priority | What Would Confirm |
|----------|----------|-------------------|
| Does Koide (Q=2/3) appear in eigenvector structure? | **CRITICAL** | A triplet with Q ≈ 2/3 to <1% |
| What is the physical meaning of 15/11 in S₂? | HIGH | Geometric interpretation |
| Can we map specific eigenvalues to specific particles? | HIGH | Mass ratio matches |
| Does A₂ structure explain Koide? | MEDIUM | 120° pattern in eigenvectors |

---

## 7. RESPONSE FORMAT

Please structure your response as:

1. **Executive Summary** (1 paragraph)
2. **Intra-Band Analysis** (tables + key findings)
3. **Koide Search** (best triplets + interpretation)
4. **Eigenvector Overlaps** (heatmap/table + patterns)
5. **A₂ Structure** (projections + 120° search)
6. **15/11 Investigation** (meaning + connection)
7. **Particle Mapping Attempt** (which eigenvalue = which particle?)
8. **Verdict Table**

| Finding | Status | Confidence |
|---------|--------|------------|
| Koide from eigenvectors | FOUND/NOT FOUND | HIGH/MEDIUM/LOW |
| 15/11 meaning | UNDERSTOOD/UNCLEAR | ... |
| Particle mapping | POSSIBLE/PARTIAL/FAILED | ... |

---

## 8. CONTEXT NOTES

- **Be thorough**: This is the critical step to connect L⊥ spectrum to actual SM masses
- **Koide is key**: If Q=2/3 emerges from geometry, it's a major result
- **15/11 is intriguing**: It appeared "for free" — understand why
- **Don't force it**: If Koide doesn't appear, that's important information too

