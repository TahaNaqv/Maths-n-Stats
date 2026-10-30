# Module 4 — Practice Quiz (ANSWER KEY)

Attempt `04_Quiz_QUESTIONS.md` first, then check here.

---

### A1
Ax = b has an exact solution exactly when **b lies in the column space col(A)** — i.e.
b can be written as a linear combination of A's columns (since Ax is always such a
combination). **Rank test:** compute rank(A) and rank([A | b]). If they're equal, b is
reachable → a solution exists. If adding b as a column *raises* the rank
(rank([A|b]) > rank(A)), then b is not a combination of A's columns → no exact solution.

### A2
- **Square, full rank** → exactly **one** solution.
- **Tall** (more equations than unknowns) → **usually none**. ← least squares is for this
- **Wide / redundant columns** → **infinitely many**.
Least squares is designed for the **tall** case (classic regression).

### A3
- **Sum the errors:** positive and negative errors cancel, so a useless line can score 0
  — it doesn't actually measure fit.
- **Sum of absolute errors (L1):** reasonable and robust to outliers, but it has **no
  clean closed-form formula** — you have to search for the minimum.
- **Sum of squared errors (L2):** preferred because it's the squared straight-line
  length ‖Ax−b‖², giving clean geometry — the minimum is the closest point (a
  projection), solvable directly.

### A4
Model t = x₁ + x₂·s. Each row of A is [1, sᵢ].
(a)
A = [[1, 1], [1, 2]],  x = (x₁, x₂),  b = (3, 5).
(b) Solve:
- Eq1: x₁ + x₂ = 3
- Eq2: x₁ + 2x₂ = 5
- Subtract Eq1 from Eq2: x₂ = 2. Then x₁ = 3 − 2 = 1.
- **x₁ = 1 ms overhead, x₂ = 2 ms/MB.**

### A5
1. We want Ax̂ to be the closest point in col(A) to b. The leftover is the residual
   r = b − Ax̂.
2. "Closest" ⟺ r is **perpendicular to the plane** col(A).
3. Perpendicular to the plane ⟺ perpendicular to **every column of A** ⟺ **Aᵀr = 0.**
4. Substitute r: Aᵀ(b − Ax̂) = 0 → Aᵀb − AᵀAx̂ = 0 →
   **AᵀAx̂ = Aᵀb** (the normal equations).

### A6
The model has an **intercept**, so A contains an all-ones column. The residual must be
perpendicular to every column of A (that's Aᵀr = 0), including the all-ones column.
Perpendicular to (1,1,…,1) means (1,1,…,1)·r = 0, i.e. r₁ + r₂ + … = 0. So the residuals
sum to zero whenever an intercept column is present.

### A7
**P² = P** means applying the projection twice does nothing more than applying it once —
"the shadow of a shadow is itself." P is the **hat matrix**: it maps the measured y to
the fitted values, **ŷ = Py** (it "puts the hat on y"). It's reused in regression
diagnostics (leverage) in Module 7.

### A8
Rule: you lose about **log₁₀ κ** digits.
(a) **QR works with κ(A) = 10⁶ → lose ~6 digits**, keep ~10 of 16. Fine.
(b) Normal equations work with **κ(AᵀA) = κ(A)² = (10⁶)² = 10¹² → lose ~12 digits**,
keep ~4. Much worse.
(c) **Trust QR** — it keeps far more accuracy by not squaring the condition number.

### A9
**κ(AᵀA) = κ(A)².** Forming AᵀA squares the condition number, so it squares the
problem's sensitivity *before* solving — a matrix that was borderline (say κ=10⁸, still
usable) becomes κ=10¹⁶ (all 16 digits gone, "computationally singular"). That's why the
textbook (AᵀA)⁻¹Aᵀb formula is risky on real data.

### A10
QR produces **A = QR**, where **Q has orthonormal columns** (perpendicular, unit length)
and **R is upper-triangular**. It's built by Gram–Schmidt (project onto previous
directions, subtract, normalize). Because Q's columns are orthonormal, the solve works
with **κ(A)** directly and **never forms AᵀA**, so it avoids the κ(A)² blow-up — far more
numerically stable.

### A11
The **"+" means the pseudoinverse (a generalized inverse)** — it is **NOT a transpose.**
From the SVD A = UΣVᵀ, the pseudoinverse inverts the singular values you trust and
**sets 1/σ = 0 for the tiny/garbage singular values** (directions carrying no real
information). This avoids dividing by ~zero and gives a stable, minimum-norm solution,
even when A is rank-deficient.

### A12
(a) Weight in pounds and weight in kg are **exactly proportional** (one is a constant
multiple of the other), so the two columns are linearly dependent → A is
**rank-deficient** (a redundant column adds no new direction).
(b)
- **Normal equations:** fail — "computationally singular" error.
- **lm() (pivoted QR):** reports the redundant coefficient as **NA** (it pivots the
  aliased column to the end).
- **SVD pseudoinverse:** handles it — returns the minimum-norm solution with the same
  predictions.

### A13
An NA coefficient means **two (or more) features carry the same information** — they're
redundant/aliased, so the model can't separate their effects. The correct response is to
**fix the data** (remove or combine the duplicate feature), **not to fight the solver**.
It's a message, not a bug.

### A14
- **Module 5 (Multivariable calculus):** set the gradient of ‖Ax−b‖² to zero → the same
  normal equations, derived a second way.
- **Module 7 (Regression & statistics):** add λ‖x‖² → **ridge regression**, which also
  cures bad conditioning and redundancy.
- **Module 8 (Optimization):** when A is too big to factor, **gradient descent** — walk
  downhill on ‖Ax−b‖².

### A15
| | Normal equations | QR | SVD |
|---|---|---|---|
| Forms AᵀA? | Yes | No | No |
| Sensitivity (κ) | κ(A)² | κ(A) | κ(A) |
| Handles redundant columns? | No (fails) | Detects → NA | Yes (minimum norm) |
| Relative cost | Cheapest | Moderate | Most expensive |

Default QR; SVD for redundancy; normal equations on paper only.
