# Delegations Overview

This folder contains sub-tasks delegated to the Research Agent. Each folder represents a specific research topic containing prompts (`iter_N_prompt.md`), responses (`iter_N_response.md`), and a status index.

## Active Delegations

| ID | Topic | Status | Goal |
|---|---|---|---|
| 01 | Weinberg Angle | 🟢 DONE | Verify $\sin^2\theta_W$ derivation and value |
| 02 | Golden Lock | 🟢 DONE | Confirm D=3 selection via knot stability |
| 03 | SM Embedding | 🟡 IN PROGRESS | Map E8 roots to Standard Model particles |
| 04 | Axiom Justification | 🟢 DONE | Justify "Maximize Complexity" axiom |
| 05 | Stability Circularity | 🟡 IN PROGRESS | Check for circular logic in stability args |
| 06 | H3 Complexity | 🟢 DONE | Verify H3 maximizes complexity metrics |
| 07 | E8 Uniqueness | 🟢 DONE | Why E8 and not other lattices? |
| 08 | E6 Alternative | 🟢 DONE | Investigate E6 vs E8 selection |
| 09 | Why Higher D | 🟢 DONE | Justify 8D/6D parent lattices |
| 10 | D6 Shell Structure | 🟢 DONE | Analyze D6 shells for particle counts |
| 11 | D6 Dynamics | 🟡 IN PROGRESS | Emergence of time/dynamics from lattice |
| 12 | Inflation & Complexity | 🟢 DONE | Inflation symmetry vs $C_\mu \to \infty$ |
| 13 | FEP Cosmology | 🟡 IN PROGRESS | Map Golden Selection to Free Energy Principle |

---

## Standard Workflow

1. **Create Folder**: `XX_topic_name/`
2. **Initialize**: Create `index.md` with status 🟡
3. **Prompt**: Write `iter_1_prompt.md` (SELF-CONTAINED)
4. **Execute**: Run research agent
5. **Update**: Save `iter_1_response.md`, update `index.md`
6. **Iterate**: If needed, create `iter_2_prompt.md`
7. **Finalize**: Mark 🟢, summarize findings in main text

## Verdict Categories

| Verdict | Meaning |
|---|---|
| **PROVEN** | Mathematical theorem or experimental fact |
| **PLAUSIBLE** | Supported by strong evidence/theory |
| **SPECULATIVE** | Hypothesis with some support |
| **FALSE** | Contradicted by evidence |
