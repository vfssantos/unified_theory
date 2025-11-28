# II.B — H₄ as Parent Symmetry

## Statement

> **THEOREM II.B.1 (H₄ Parentage)**:
> 
> An H₃ quasicrystal in 3D requires **H₄** as its 4D parent symmetry.

---

## The Subgroup Relation

### H₃ ⊂ H₄

The icosahedral group H₃ is naturally embedded in the hyper-icosahedral group H₄:

$$H_3 \subset H_4$$

This embedding arises geometrically: the 600-cell (H₄'s defining polytope) contains icosahedral cross-sections.

### Group Data

| Group | Dimension | Order | Defining Polytope |
|-------|-----------|-------|-------------------|
| H₃ | 3D | 120 | Icosahedron/Dodecahedron |
| **H₄** | **4D** | **14,400** | **600-cell/120-cell** |

H₄ has 120× more symmetry than H₃.

---

## The 600-Cell

### Definition

The **600-cell** is the 4D regular polytope with:
- 120 vertices
- 720 edges
- 1200 triangular faces
- 600 tetrahedral cells

### Coordinates

The 120 vertices of the 600-cell (radius 2) include:

**Type 1**: 8 vertices of form (±2, 0, 0, 0) and permutations

**Type 2**: 16 vertices of form (±1, ±1, ±1, ±1)

**Type 3**: 96 vertices involving the golden ratio:
- (±φ, ±1, ±φ⁻¹, 0) and even permutations

### Slicing: H₄ → H₃

When the 600-cell is sliced perpendicular to a vertex-first axis, the cross-sections reveal H₃ structures:

| Height h | Vertex Count | 3D Shape |
|----------|--------------|----------|
| h = 2 | 1 | North pole |
| h = φ | 12 | **Icosahedron** |
| h = 1 | 20 | **Dodecahedron** |
| h = φ⁻¹ | 12 | Icosahedron |
| h = 0 | 30 | Icosidodecahedron |
| ... | ... | ... |

**Total**: 1 + 12 + 20 + 12 + 30 + 12 + 20 + 12 + 1 = 120 ✓

---

## The Problem: H₄ Cannot Tile 4D

### Crystallographic Restriction in 4D

> **THEOREM**: The only finite groups that can be point groups of 4D lattices have rotations of order 1, 2, 3, 4, or 6.

**H₄ has 5-fold rotations** (order 5).

**Consequence**: There is no H₄ lattice. The 600-cell cannot tile 4D space.

### Why This Matters

If we want a **physical structure** (not just an abstract polytope), we need:
1. A lattice that can tile space (periodic)
2. That lattice must contain H₄ symmetry upon projection

This forces us to go beyond 4D.

---

## The Resolution

### LEMMA II.B.1a: H₄ must be embedded in a higher-dimensional lattice

Since H₄ cannot form a lattice in 4D, we need a lattice in dimension n > 4 that:
1. Is periodic (can tile ℝⁿ)
2. Contains H₄ as a substructure or projection symmetry

### The Answer: E₈

The E₈ lattice in 8D satisfies both requirements:
- It tiles ℝ⁸ periodically
- It projects to two H₄ structures (two 600-cells) under the golden projection

→ Section II.C proves this is the **unique minimal** solution.

---

## Summary

| Question | Answer |
|----------|--------|
| Why H₄? | H₃ ⊂ H₄ (natural parent) |
| Can H₄ tile 4D? | **No** (5-fold forbidden) |
| What's needed? | Higher-D lattice containing H₄ |
| Answer? | E₈ (8D) |

---

## References

- Coxeter, H.S.M. "Regular Polytopes" (1973)
- Du Val, P. "Homographies, Quaternions and Rotations" (1964)


