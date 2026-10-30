# Module 4 — Quiz Cheatsheet (Formulas & Key Facts)

Fast revision. Read this last, right before the quiz.

---

## SESSION 1 — Least Squares & Normal Equations

**Matrix form of a system:** Ax = b (A = coefficients, x = unknowns, b = measurements)

**Solution exists ⟺** b lies in **col(A)** (the column space).
- Rank test: if rank([A|b]) > rank(A), then **no exact solution** (b sticks out).

**Three cases:**
- Square + full rank → exactly one solution
- Tall (more equations than unknowns) → usually none → **least squares** (Session 1)
- Wide / redundant columns → infinitely many → **SVD** (Session 2)

**Least squares goal:** minimize **‖Ax − b‖²** (sum of squared errors = squared L2 length)

**Why squared (not sum or absolute):**
- plain sum → positives/negatives cancel (useless)
- absolute (L1) → no clean formula, must search (→ Lasso)
- squared (L2) → clean geometry, closest point

**Residual:** r = b − Ax̂

**Residual ⊥ plane ⟹ NORMAL EQUATIONS:**
> Aᵀr = 0  ⟹  **AᵀAx̂ = Aᵀb**  ⟹  x̂ = (AᵀA)⁻¹Aᵀb

- Always a small square system (2×2 if 2 unknowns), no matter how many data points.

**Residuals sum to 0** whenever there's an **intercept column** (the all-1's column):
r ⊥ (1,1,…,1) means Σrᵢ = 0.

**Hat matrix / projection P:**
- ŷ = Py
- **P² = P** (project twice = project once)
- P = A(AᵀA)⁻¹Aᵀ

**Worked example (3 web-service measurements):** overhead x₁ = 1.67 ms, cost
x₂ = 1.5 ms/MB, residuals (−0.17, +0.33, −0.17) sum to 0.

---

## SESSION 2 — Conditioning, QR, SVD

**Floats:** a double holds ~16 significant digits. `0.1 + 0.2 == 0.3` → FALSE.

**Condition number κ(A):** how much A amplifies small errors.
- **Lose ≈ log₁₀ κ digits.** (κ=10⁸ → lose 8, keep 8.)
- Small κ = well-conditioned (good); large κ = ill-conditioned (bad).

**THE KEY DANGER:**
> **κ(AᵀA) = κ(A)²**  → normal equations *square* the sensitivity.
- κ(A)=10⁸ → κ(AᵀA)=10¹⁶ → lose all 16 digits → "computationally singular."
- This is why **R's lm() never computes (AᵀA)⁻¹Aᵀb.**

**QR factorization:** A = QR, Q orthonormal columns, R upper-triangular.
- Built by **Gram–Schmidt** (project onto previous q's, subtract, normalize; subtracted
  amounts fill R).
- Works with κ(A), NOT κ(A)² → safe. Never forms AᵀA.
- Centering a feature = one Gram–Schmidt step against the intercept column.

**Pseudoinverse A⁺ (SVD):**
- ⚠️ the **+ is NOT a transpose** — it's a generalized inverse.
- From A = UΣVᵀ: invert the singular values you trust, **set 1/σ = 0 for tiny/garbage
  ones** (directions carrying no info).
- Handles **rank-deficient** (exactly redundant) columns → minimum-norm solution.

**Three solvers (memorize):**
| | Normal eqns | QR | SVD |
|---|---|---|---|
| Forms AᵀA? | Yes | No | No |
| Sensitivity | κ(A)² | κ(A) | κ(A) |
| Redundant cols | Fails | Detects → NA | Handles (min norm) |
| Cost | Cheapest | Moderate | Most expensive |
| Found in | textbooks/paper | R's lm() | numpy lstsq |

> Default **QR**. Redundant features → **SVD**. Normal equations → paper only.

**Redundant-column bug (mtcars):** weight in lb AND kg = proportional columns = rank-
deficient. Normal eqns → singular error; lm() → NA coefficient; SVD → works.

**NA coefficient in lm()** = two features carry the same information (aliased). Fix the
data, not the solver.

**Standardizing helps:** degree-5 cars fit κ(A) 2.3×10⁸ → 62 after centering/scaling.

**Connections:**
- Module 5: gradient of ‖Ax−b‖² = 0 → same normal equations (AᵀAx = Aᵀb); Hessian 2AᵀA
  is positive semidefinite → minimum.
- Module 7: add λ‖x‖² → ridge regression (cures conditioning + redundancy).
- Module 8: too big to factor → gradient descent.

---

## ONE-LINE HOOKS
- Ax=b solvable ⟺ b in col(A)
- least squares = minimize ‖Ax−b‖² = projection = shadow
- **AᵀAx̂ = Aᵀb** (normal equations, from residual ⊥ columns)
- residuals sum to 0 ⟺ intercept column present
- P² = P (projection / hat matrix)
- **κ(AᵀA) = κ(A)²** → why not to use normal equations
- lose log₁₀κ digits
- QR = default safe solver; SVD = handles redundancy; normal eqns = paper only
- A⁺ pseudoinverse, + ≠ transpose
- NA coefficient = redundant/aliased feature
