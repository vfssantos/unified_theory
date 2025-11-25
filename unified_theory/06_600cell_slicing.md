# 6. The 600-cell Latitude Decomposition

## Summary

This section derives the 12 + 20 + ... shell structure:

### 6.1 Vertex-First Slicing

- **Setup**: Choose a vertex v_pole of the 600-cell as "north pole"
- **Time axis**: t̂ = v_pole / |v_pole|
- **3D space**: H₃ = t̂⊥ ⊂ H₄
- **Decomposition**: Each vertex v = h·t̂ + v_⊥

### 6.2 Allowed Heights

- **Theorem**: For a 600-cell with |v|² = 4, the heights h take values:
  $$h \in \{±2, ±\varphi, ±1, ±1/\varphi, 0\}$$
  
- **Multiplicities**:
  | Height h | Count | 3D polytope |
  |----------|-------|-------------|
  | ±2 | 1 | Pole |
  | ±φ | 12 | Icosahedron |
  | ±1 | 20 | Dodecahedron |
  | ±1/φ | 12 | Icosahedron |
  | 0 | 30 | Icosidodecahedron |

### 6.3 Perpendicular Radii

- **Formula**: |v_⊥|² = 4 - h²
- **Explicit values**:
  - h = ±2: |v_⊥|² = 0 (poles)
  - h = ±φ: |v_⊥|² = 3 - φ
  - h = ±1: |v_⊥|² = 3
  - h = ±1/φ: |v_⊥|² = 2 + φ
  - h = 0: |v_⊥|² = 4

### 6.4 The Key Insight

- **Not radial shells**: The 12 and 20 are NOT at different 4D radii
- **Latitude bands**: They are different heights at the SAME 4D radius
- **Correction**: This fixes errors in naive "shell" interpretations

### 6.5 Physical Interpretation

- **h = 2**: The pole (related to time/observer direction)
- **h = φ (12 vertices)**: Gauge sector
- **h = 1 (20 vertices)**: Matter + Higgs sector
- **Lower bands**: Additional generations, heavy states

## Expected Length

~1500-2000 words

## Key Figures

- 600-cell with latitude bands highlighted
- Table of heights and polytopes
- Schematic of the 1-12-20-12-30-... structure

## Status

[ ] Draft
[ ] Review
[ ] Final

