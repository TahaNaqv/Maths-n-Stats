# Module 4 — Session 2: Computing It Without Breaking It
### (Conditioning, QR, SVD / Pseudoinverse)

*Slides: M04-Session2-Slides.pdf*

Session 1 gave the formula x̂ = (AᵀA)⁻¹Aᵀb. Session 2 is about why that formula is
**dangerous on real data** and what to use instead. This is the "numerical" half.

---

## 1. Callback to Day 1: floats aren't the real numbers

- Day 1: integers in a computer aren't closed under + — push far enough and they
  **overflow**. Real numbers get the same treatment: a **double stores ~16 significant
  digits** and rounds the rest.
- Usually harmless. Classic demo: `0.1 + 0.2 == 0.3` returns **FALSE** in R (and most
  languages) because of rounding.
- The danger: if a calculation **amplifies tiny input errors** by a huge factor (say
  10¹²), you can run out of trustworthy digits entirely.

---

## 2. Condition number κ(A) — how many digits you lose

> **κ(A)** (kappa) measures how much a matrix A **amplifies small errors.**

- **Rule of thumb: you lose about log₁₀ κ digits** of accuracy.
- Example: κ(A) = 10⁸ → lose ~8 digits, keep ~8 (out of 16) → fine.
- A **well-conditioned** matrix has small κ (close to 1); an **ill-conditioned** one
  has large κ.

**The crucial problem with the normal equations:**

> **κ(AᵀA) = κ(A)²**

Forming AᵀA **squares** the condition number — it squares the problem's sensitivity
*before* you even solve it.
- If κ(A) = 10⁸ (lose 8, keep 8 — fine), then κ(AᵀA) = 10¹⁶ → lose ~16 digits → **keep
  none.** The answer is numerically worthless.

**That is why R's lm() never computes (AᵀA)⁻¹Aᵀb** — it refuses to square the
conditioning. (Answer to Session 1's cliffhanger.)

---

## 3. Real-data illustration (stopping distance vs speed, cars data, n=50)

Fitting a polynomial of increasing degree:
- As degree rises, κ grows fast. At **degree 5**: κ(A) ≈ 2.3×10⁸, κ(AᵀA) ≈ 5.3×10¹⁶.
- **Normal equations in R:** fail — "system is computationally singular" (all 16 digits
  gone).
- **QR on the same data:** solves it fine — fitted values match a stable reference to
  ~10⁻¹¹.
- Takeaway: κ(A) is what QR works with; κ(AᵀA) (squared, far worse) is what the normal
  equations work with.

---

## 4. The idea behind QR: what matrix would make least squares trivial?

- If A's columns were **orthonormal** (perpendicular, each length 1), there'd be
  nothing to invert and no κ² — least squares would be **just dot products.**
- Question: **can we swap A's columns for orthonormal ones that span the same space?**
  Yes — that's QR.

---

## 5. Gram–Schmidt → the QR factorization

**Gram–Schmidt** = project, subtract, repeat. It turns A's columns into orthonormal
ones:
1. Keep a₁; normalize it → **q₁**
2. From a₂, subtract its **projection onto q₁** (Module 2 projection!) — removes the
   overlap, leaving a perpendicular piece
3. Normalize what's left → **q₂**. Continue for a₃, a₄, …
4. The amounts you subtracted off get recorded in an **upper-triangular matrix R**

Result: **A = QR**, where Q has orthonormal columns and R is upper-triangular.

**Why QR solves least squares safely:** because Q is orthonormal, solving uses κ(A)
directly (not κ(A)²). You never form AᵀA.

- Slide's example: (−1, 0, 1) is s = (1, 2, 3) minus its mean. **Centering a feature is
  literally one step of Gram–Schmidt against the intercept column.** (Nice link: mean-
  centering = removing the overlap with the all-1's column.)

---

## 6. Redundant columns: the SVD / pseudoinverse returns

QR handles bad conditioning, but what about **exactly redundant** columns (rank-
deficient A)? That's the SVD's job.

> **A⁺ is the pseudoinverse.** ⚠️ **The "+" is NOT a transpose** — it's a generalized
> inverse. (Your instructor explicitly flagged this.)

**How the pseudoinverse works:** using A = UΣVᵀ, you **invert the singular values you
trust, and zero out the ones you don't** (the tiny/garbage ones). That sidesteps the
"divide by ~zero" blow-up.

**Classic production bug (mtcars):** car weight entered twice — once in 1000-lb units,
once in kg. The two columns are **exactly proportional**, so A is **rank-deficient**.
Results from the three solvers:
| Solver | What happens |
|---|---|
| Normal equations | error: "computationally singular" |
| lm() (pivoted QR) | coefficient reported as **NA** |
| SVD pseudoinverse | minimum-norm solution; same predictions |

- For the useless direction, its singular value is ~0 (e.g. 6×10⁻¹⁵) → **set 1/σ to 0**
  because "the last direction carries no information."

---

## 7. Three solvers, different failure modes (MEMORIZE THIS TABLE)

| | Normal equations | QR | SVD |
|---|---|---|---|
| Forms AᵀA? | **Yes** | No | No |
| Sensitivity | **κ(A)²** | κ(A) | κ(A) |
| Redundant columns | **Fails** | Detects (pivoting → NA) | Handles (minimum norm) |
| Relative cost | Cheapest | Moderate | Most expensive |
| You'll find it in | Textbooks, hand calc | **R's lm()** | numpy.linalg.lstsq |

> **Default: QR. Reach for SVD when features may be redundant. Use the normal equations
> on paper, not in production.**

---

## 8. What this changes in day-to-day work

- **Standardize features:** degree-5 cars fit — κ(A) drops from 2.3×10⁸ to **62** after
  centering and scaling speed. Then even the normal equations cope. (Conditioning is
  often fixable by scaling.)
- **Read NA as a message:** an NA coefficient in lm() means **two features carry the
  same information.** Fix the data, don't fight the solver.
- **Too big to factor?** When A has millions of rows & columns, even QR is too
  expensive → you **iterate** instead (gradient descent) → that's Module 8.

---

## 9. Where ‖Ax − b‖² shows up next (the connections)

- **Module 5 (Multivariable calculus):** set the **gradient of ‖Ax − b‖² to zero** →
  get the *same* normal equations, by a second road.
- **Module 7 (Regression & stats):** add a term **λ‖x‖²** → **ridge regression**, which
  also cures bad conditioning and redundancy.
- **Module 8 (Optimization):** when A is too big to factor, **walk downhill on
  ‖Ax − b‖²** → gradient descent.

---

## 10. Backup slides (instructor said OPTIONAL — skim only if time)

- **Backup A — why P = A(AᵀA)⁻¹Aᵀ is a projection:** P² = P (shadow of a shadow is
  itself); Pᵀ = P (projects straight down, orthogonally); I − P projects onto the
  perpendicular → gives the residual r = (I − P)b.
- **Backup B — why κ(AᵀA) = κ(A)²:** A = UΣVᵀ, so AᵀA = VΣ²Vᵀ → singular values get
  squared → their ratio (the condition number) squares.
- **Backup C — the calculus road:** setting the gradient to zero gives AᵀAx = Aᵀb (same
  normal equations); the Hessian 2AᵀA is positive semidefinite → it's a minimum.
- **Backup D — inside R's lm():** uses QR (never forms XᵀX); near-zero columns get
  pivoted to the end and "aliased" → that's why they print as NA.

---

### Exam angles (Session 2)
- **Theory (most likely):** what κ(A) means; the "lose log₁₀κ digits" rule; why
  κ(AᵀA) = κ(A)² makes normal equations dangerous; what QR does and why it's safer;
  what the pseudoinverse A⁺ is (and that + ≠ transpose); the three-solver comparison;
  why an NA coefficient appears; how standardizing helps.
- **Calculation (lighter):** "if κ(A) = 10⁶, how many digits do you lose, and how many
  with the normal equations?" (6 digits via QR; 12 via normal equations). Possibly a
  conceptual Gram–Schmidt step.
