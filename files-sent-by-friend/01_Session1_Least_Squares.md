# Module 4 — Session 1: When the Equations Disagree
### (Least Squares & the Normal Equations)

*Slides: M04-Session1-Slides.pdf + M04-Session1-Supplement-Slides.pdf*

This whole module is the math behind **fitting a model to data** (regression).
Session 1 = the *idea* (geometry, normal equations). Session 2 = *computing it
safely* on real data.

---

## 1. The running example (know this cold — everything builds on it)

Timing a web service. Each request costs a fixed overhead plus a per-MB cost:

> **t = x₁ + x₂·s**   where x₁ = overhead (ms), x₂ = cost per MB (ms/MB)

- s = payload size (MB), t = time (ms). **The x's are the unknowns we solve for;
  s and t are the measured data.**

Measurements:
| payload s | time t | equation |
|---|---|---|
| 1 MB | 3 ms | 3 = x₁ + 1·x₂ |
| 2 MB | 5 ms | 5 = x₁ + 2·x₂ |

Two equations, two unknowns → solves exactly: x₁ = 1, x₂ = 2 (overhead 1 ms, 2 ms/MB).

**Then a third measurement arrives** (e.g. 3 MB → 6 ms). Now 3 equations, 2 unknowns.
The three lines don't all agree. Three questions the slide raises:
1. Which measurement is wrong?
2. Should we throw one away — which one?
3. If none is "wrong," what should "the answer" even mean?

That third question is what least squares answers.

---

## 2. When does Ax = b have an exact solution?

Write the system in matrix form **Ax = b**:
- A = the coefficient matrix (here each row is [1, sᵢ])
- x = the unknowns (x₁, x₂)
- b = the measured outputs (the times)

**Key idea (column picture, from Module 2):** Ax is always a *linear combination of
A's columns*. So:

> **Ax = b has a solution exactly when b lies in the column space col(A).**

In the 3-measurement case: A's 2 columns live in 3-D space and span a **plane**. The
data vector b = (3, 5, 6) **sticks out of that plane** → no exact solution.

**Rank test (how to check):**
- rank(A) = 2, but rank([A | b]) = 3.
- Adding b as an extra column *raised* the rank → b is NOT a combination of A's
  columns → **no exact solution exists.**
- (If adding b had kept the rank the same, b would be reachable and a solution would
  exist.)

---

## 3. The three cases every linear system falls into

| Shape / rank | Solutions | Where you meet it |
|---|---|---|
| Square, full rank | Exactly one | Textbook exercises; rare with real data |
| **Tall** (more equations than unknowns) | Usually **none** | Classic regression — many data points, few parameters |
| Wide, or redundant columns | Infinitely many | Duplicated features; overparameterized models |

- **Session 1 handles the TALL case** → least squares.
- **Session 2 handles the redundant case** → SVD / pseudoinverse.

---

## 4. "Least wrong" — measured how? (three ways to score errors)

Define **error = measured time − predicted time** for each point. We want ONE number
scoring a whole candidate line. Three options:

1. **Add up the errors.** Bad: positive and negative errors cancel. A useless flat
   line (t = 4.67, ignoring payload) can get errors summing to exactly 0 — a "perfect"
   score that's actually terrible.
2. **Add up |errors|** (absolute values). Reasonable, and gentler on a wild outlier.
   But it measures distance like walking city blocks (L1) → **no clean formula, you
   have to search.** (This is the idea behind Module 7's Lasso.)
3. **Add up errors²** (squared). **This is least squares.** Stack all errors into one
   vector; the sum of squares is its **squared straight-line length, ‖Ax − b‖²**
   (the L2 norm from Module 2). Smallest error = closest point = clean geometry.

> **Least squares: minimize ‖Ax − b‖²**

---

## 5. The best fit is a shadow (projection)

No x reaches b exactly. So find the point **in col(A) that is closest to b.**

- Analogy: which point on the floor is closest to a light bulb hanging above it? The
  point directly below — the **shadow** (perpendicular drop).
- Module 2 did this projecting onto a *line*. Here we project onto a *plane* — same
  idea, one more dimension.
- The closest point is called **Ax̂** (A times the best estimate x̂).

---

## 6. Perpendicular residual ⇒ the normal equations (the key derivation)

The **residual** is r = b − Ax̂ (the leftover, the arrow from the prediction up to b).

For Ax̂ to be the closest point, the residual must be **perpendicular to the plane**:

1. r must be perpendicular to the plane col(A)
2. perpendicular to the plane ⇔ perpendicular to **every column of A** ⇔ **Aᵀr = 0**
3. Substitute r = b − Ax̂ and rearrange:

> **Aᵀ(b − Ax̂) = 0  ⟹  AᵀAx̂ = Aᵀb**   ← **THE NORMAL EQUATIONS**

This is a small square system — here **2×2, no matter how many data points** you have.
(1000 measurements still give a 2×2 system, because there are only 2 unknowns.) That
shrinking is the whole payoff.

Solving it gives **x̂ = (AᵀA)⁻¹Aᵀb** (the textbook formula — but see Session 2 for why
you don't actually compute it this way).

---

## 7. The worked answer on our three measurements

Solving the normal equations for the 3 points gives:
- **x₁ = 1.67 ms** (fixed overhead)
- **x₂ = 1.5 ms per MB**
- residuals = (−0.17, +0.33, −0.17), which **sum to exactly 0**

**Why do the residuals sum to exactly zero?** Because the model has an **intercept
column** (the column of 1's for x₁). The residual must be perpendicular to *every*
column of A, including that all-1's column. Perpendicular to the all-1's vector means
the dot product (1,1,1)·r = 0, i.e. r₁ + r₂ + r₃ = 0 — the residuals sum to zero.
(This is a property of having an intercept, not a coincidence.)

---

## 8. The supplement slides (the 3 extras)

**(a) "Throw one away? Which one?"** — dropping each point gives a different line:
| Dropped point | Line | Slope |
|---|---|---|
| 1 MB | t = 3 + 1·s | 1 |
| 2 MB | t = 1.5 + 1.5·s | 1.5 |
| 3 MB | t = 1 + 2·s | 2 |
Three choices, three answers, **nothing principled to pick between them** → that's why
you don't throw data away; you use all of it via least squares.

**(b) "Two pictures of the same problem."** Each *measurement* becomes an axis. Our 3
measured times are **one point b** in that 3-D space. Every possible line produces 3
predicted times = **one point on a plane**. Least squares = the plane point closest to b.

**(c) The worked example with the fitted line** — same 1.67 / 1.5 / residuals-sum-to-0
result, drawn as a line through the data.

---

## 9. You've been running this for years (the payoff slide)

All of these solve the *same* least-squares projection:
- `lm(dist ~ speed)` (R) · Excel "Add Trendline" · `numpy.linalg.lstsq(A, b)` ·
  `sklearn LinearRegression().fit(X, y)`

**The projection itself is a matrix P** (the "hat matrix"):
- It puts the hat on y: **ŷ = Py**
- **P² = P**: projecting twice = projecting once (a shadow of a shadow is itself)
- Statisticians reuse P in Module 7 for leverage & diagnostics.

**Cliffhanger for Session 2:** every textbook writes x̂ = (AᵀA)⁻¹Aᵀb, but R's lm()
**never computes it that way.** Why not? → conditioning (Session 2).

---

### Exam angles (Session 1)
- **Theory:** when does Ax=b have a solution (column space / rank test); the 3 cases;
  why least squares (3 error measures); why residual ⊥ plane gives AᵀAx̂ = Aᵀb; why
  residuals sum to zero with an intercept; what P² = P means.
- **Calculation:** set up A, x, b for a small fitting problem; write the normal
  equations; possibly solve a 2×2 system; do the rank test on [A | b].
