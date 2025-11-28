# Scripts

Python and Mathematica scripts for numerical verification.

---

## Planned Scripts

| Script | Purpose | Status |
|--------|---------|--------|
| `e8_roots.py` | Generate all 240 E₈ roots | ⬜ |
| `golden_projection.py` | Elser-Sloane projection | ⬜ |
| `600cell_analysis.py` | 600-cell properties and slicing | ⬜ |
| `weinberg_calculation.py` | Gauge coupling ratios | ⬜ |
| `koide_check.py` | Verify Koide formula | ⬜ |
| `mixing_angles.py` | CKM/PMNS predictions | ⬜ |
| `mass_predictions.py` | All mass formulas | ⬜ |

---

## Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install numpy scipy matplotlib sympy

# Optional: for notebooks
pip install jupyter
```

---

## Script Template

```python
#!/usr/bin/env python3
"""
[Script Name]

Purpose: [What this calculates]
Supports: [Which theorem/claim]
Status: [Complete/Partial/Draft]

Usage:
    python script_name.py

Output:
    [Description of output]
"""

import numpy as np
from typing import List, Tuple

# ============================================================
# CONSTANTS
# ============================================================

PHI = (1 + np.sqrt(5)) / 2       # Golden ratio
PHI_INV = PHI - 1                # 1/φ = φ - 1
SQRT5 = np.sqrt(5)

# ============================================================
# MAIN FUNCTIONS
# ============================================================

def main():
    """Main entry point."""
    pass

def verify():
    """Run verification checks."""
    pass

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
    verify()
```

---

## Running Verification Suite

```bash
# Run all verification scripts
python -m pytest scripts/ -v

# Or run individually
python scripts/e8_roots.py
python scripts/golden_projection.py
# etc.
```

---

## Output Convention

Each script should output:
1. **Computed value**
2. **Expected value** (from theory)
3. **Observed value** (experimental, if applicable)
4. **Discrepancy** (% error)
5. **Status** (PASS/FAIL/INCONCLUSIVE)

Example:
```
=== Weinberg Angle Verification ===
Computed:  sin²θ_W = 0.2318
Expected:  sin²θ_W = (3/8)φ⁻¹ = 0.2318
Observed:  sin²θ_W = 0.2312 ± 0.0001
Error:     0.26%
Status:    PASS (within tolerance)
```

