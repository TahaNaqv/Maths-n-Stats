# Module 5 Assignment, Part A — Start Here

**Due:** hand in on paper at the start of class, **Tuesday 20 October** (or upload a
photo/scan to Classroom → Classwork → Module 5 by the same time if you can't attend).
**Worth:** 25 of the assignment's 100 marks. Part B (75) comes after Thursday's class.

The sheet itself: `../Assignments/Math-Foundations-DS-CI_Module5_Assignment-MVC_PartA_Single-Variable.pdf`

## How to use this pack

This pack is a **study reference**, not something to copy. The sheet says *sketch by
hand first* and *show your reasoning*, so the marks are for work in your own hand.
As with Assignment 1, if you use AI help to understand the material, **disclose it on
your submission** (the course policy from Assignment 1's instructions).

Answer key: the instructor will post one after the due date. Compare it with this pack.

## Order (≈ 4 hours if you're starting cold)

| Step | File | Time | Goal |
|---|---|---|---|
| 1 | `01_Calculus_Toolkit_From_Zero.md` | 60 min | The 7 tools: domains, limits, derivative rules, critical points, concavity, symmetry, sketching |
| 2 | `02_A1_A2_Worked.md` | 60 min | A1 matching (8 marks) and the four zoo functions (8 marks) |
| 3 | `03_A3_Worked.md` | 60 min | Pick 6 of 10 (the quickest six are listed at the top) |
| 4 | `04_A4_Worked.md` | 30 min | Three short proofs + the bonus |
| 5 | `plots/` | 15 min | Check your hand sketches against these **after** drawing |

To regenerate the plots: `python3 make_plots.py`

## Marks map: where the 25 (+1) come from

| Part | Marks | What earns them |
|---|---|---|
| A1 | 8 | ½ formula + ½ **specific** feature (a value at 0, max height, range) × 8 plots |
| A2 | 8 | per function: ½ basics, ½ derivatives, **1 sketch** |
| A3 | 6 | per function: ½ items 1–5, ½ sketch |
| A4 | 3 + 1 | the algebra steps shown, plus a sentence of interpretation |

## Answers at a glance (to check yourself, not to replace working)

- **A1:** 1-g, 2-i, 3-c, 4-e, 5-a, 6-h, 7-j, 8-d. Unused: b (ln x), f (ReLU).
- **A2.4:** ReLU at 0 is a **corner, not an inflection** (f′ and f″ DNE; concavity never changes).
- **A3:** x³: flat inflection, not an extremum · 1/x: not decreasing on its whole domain,
  since f(−1) = −1 < f(1) = 1 · √x: vertical tangent at 0 · e^(−x²): max (0,1), inflections
  (±1/√2, e^(−½)) · softplus: HA y=0, OA y=x · x ln x: min (1/e, −1/e), limit 0 at 0⁺.
- **A4:** σ(2x): mid (0,½), slope ½ · σ(x−3): mid (3,½), slope ¼ · tanh = 2σ(2x)−1 ·
  softplus′ = σ · tanh′(0) = 1 vs σ′(0) = ¼, so **tanh** shrinks gradients less.

## Most common ways to lose marks here

1. Matching A1 on shape alone. Quote a **number** from the axes.
2. Saying "f′(0) = 0 so it's a min". Do the **sign test** (x³ fails it).
3. Calling f″ = 0 an inflection without checking the **sign change** (ReLU, |x|).
4. Forgetting the **endpoint** checks (√x at 0, −ln p at p = 1).
5. Saying 1/x is "decreasing" without "on each interval separately".
6. Sketches without **labelled** asymptotes and coordinates.
