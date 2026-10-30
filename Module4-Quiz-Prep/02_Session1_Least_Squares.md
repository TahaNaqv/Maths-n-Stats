# Lesson 2 — Session 1: When the Equations Disagree

Slides: `Lectures/M04-Session1-Slides.pdf` + `M04-Session1-Supplement-Slides.pdf`

---

## 1. The story (the instructor uses this example for everything)

A web request costs a **fixed overhead** x₁ (ms) plus a **cost per MB** x₂ (ms/MB):

    t = x₁ + x₂·s          s = payload (MB), t = time (ms)

The **x's are unknowns**. s and t are **measured data**. (Don't mix these up — in
regression the data go INTO A, the parameters are x.)

| s | t | equation |
|---|---|---|
| 1 | 3 | 3 = x₁ + 1·x₂ |
| 2 | 5 | 5 = x₁ + 2·x₂ |

Two equations, two unknowns. Subtract: x₂ = 2, then x₁ = 1. Done, exact.

**Then a third measurement arrives: s = 3, t = 6.** The line through the first two
points predicts 1 + 2·3 = 7, not 6. Now no line passes through all three. The slide asks:
1. Which measurement is wrong?
2. Should we throw one away? Which one?
3. If none is "wrong", what should the answer even mean?

## 2. Supplement slide: "Throw one away?"

Drop each point in turn and fit the line through the other two:

| Dropped | Line | Slope |
|---|---|---|
| 1 MB point | t = 3 + 1·s | 1 |
| 2 MB point | t = 1.5 + 1.5·s | 1.5 |
| 3 MB point | t = 1 + 2·s | 2 |

Three choices → three different answers → **nothing principled to pick between them.**
Lesson: don't throw data away. Use all of it and define "best" properly.

## 3. Matrix form, and why there's no solution

Each row of A is [1, sᵢ] (the 1 multiplies the overhead x₁ — this is the **intercept
column**):

    A = [1 1]    x = [x₁]    b = [3]
        [1 2]        [x₂]        [5]
        [1 3]                    [6]

**Column picture:** Ax = x₁·(1,1,1) + x₂·(1,2,3). Two columns in 3-D span a **plane**.
The data vector b = (3,5,6) **sticks out of that plane**.

**Rank test:** rank(A) = 2, rank([A | b]) = 3. Adding b raised the rank → b is not a
combination of A's columns → **no exact solution.**

## 4. The three cases (memorize the table)

| Shape / rank | Solutions | Where you meet it |
|---|---|---|
| Square, full rank | Exactly one | Textbook exercises; rare with real data |
| **Tall** (more equations than unknowns) | **Usually none** | Classic regression — many data points, few parameters |
| Wide, or redundant columns | Infinitely many | Duplicated features; overparameterized models |

Session 1 → the **tall** case (least squares). Session 2 → the **redundant** case (SVD).

## 5. "Least wrong" — measured how?

error = measured − predicted. We need ONE number scoring a whole line.

| Score | Verdict |
|---|---|
| **Σ errors** | Useless: + and − cancel. The flat line t = 4.67 (the mean, ignores s!) has errors −1.67, +0.33, +1.33 → sum = 0, a "perfect" score. |
| **Σ \|errors\|** | Reasonable, gentler on one wild outlier. But it's "city-block" distance → **no clean formula, you have to search.** (Module 7's **Lasso** uses this idea.) |
| **Σ errors²** | Stack errors into one vector e = b − Ax; Σ eᵢ² = **‖Ax − b‖²**, its squared straight-line length. Smallest error = **closest point**. That's geometry → clean formula. |

**Least squares: choose x̂ to minimize ‖Ax − b‖².**

## 6. Two pictures of the same problem (supplement)

- **Picture 1 (usual):** s on the x-axis, t on the y-axis, 3 dots, a line through them.
- **Picture 2 (measurement space):** each *measurement* is an axis. The 3 measured
  times form **one point b = (3,5,6)** in 3-D. Every possible line gives 3 predicted
  times = one point Ax, and all such points form **a plane** (col(A)).
  Best line ⟺ the point on that plane **closest to b**.

## 7. The best fit is a shadow

"Which point on the floor is closest to a light bulb above it?" → the one **directly
below**: drop a perpendicular. The closest point Ax̂ is the **projection** (shadow) of b
onto the plane col(A). Module 2 projected onto a line; this is one more dimension.

## 8. Derivation of the normal equations (be able to write this out)

1. Residual r = b − Ax̂ (the arrow from the shadow up to b).
2. Closest ⟺ r is **perpendicular to the plane**.
3. Perpendicular to the plane ⟺ perpendicular to **every column of A** ⟺ **Aᵀr = 0**
   (Tool 5: Aᵀr is the list of column·r dot products).
4. Substitute: Aᵀ(b − Ax̂) = 0 → Aᵀb − AᵀAx̂ = 0 →

        AᵀA x̂ = Aᵀb        ← THE NORMAL EQUATIONS

5. AᵀA is (unknowns × unknowns): **2×2 here no matter how many data points.** A million
   measurements still give a 2×2 system.

Textbook form: x̂ = (AᵀA)⁻¹Aᵀb. (Session 2: why computers don't actually do this.)

## 9. THE CALCULATION — recipe + the lecture example

For the model t = x₁ + x₂·s with n data points, you never need to multiply matrices
out — just make these sums:

    AᵀA = [ n     Σs  ]         Aᵀb = [ Σt   ]
          [ Σs    Σs² ]               [ Σs·t ]

**Lecture data** s = (1,2,3), t = (3,5,6):
- n = 3, Σs = 6, Σs² = 1 + 4 + 9 = 14
- Σt = 14, Σs·t = 3 + 10 + 18 = 31

        [3  6] [x₁]   [14]
        [6 14] [x₂] = [31]

Solve (Tool 6): det = 3·14 − 6·6 = 6

    x̂ = (1/6)·[14 −6; −6 3]·(14, 31) = (1/6)·(196 − 186, −84 + 93) = (10/6, 9/6)

**x̂₁ = 5/3 ≈ 1.67 ms overhead, x̂₂ = 3/2 = 1.5 ms per MB.** (Slide: "1.67 ms / 1.5 ms")

**Fitted values** ŷ = 5/3 + 1.5s: 3.17, 4.67, 6.17
**Residuals** r = t − ŷ: (−0.17, +0.33, −0.17)  → **sum = 0**

Always finish with the residual check: Aᵀr should be (0, 0).
- (1,1,1)·r = −0.17 + 0.33 − 0.17 = 0 ✓
- (1,2,3)·r = −0.17 + 0.67 − 0.5 = 0 ✓

## 10. Why do the residuals sum to exactly zero? (the slide's question)

Because the model has an **intercept**, A has an **all-ones column**. The normal
equations force r ⊥ every column, including (1,1,…,1). And (1,1,…,1)·r = r₁ + r₂ + … .
So Σrᵢ = 0. It's forced by the geometry, not a coincidence.

**Without** an intercept (t = x·s through the origin) the residuals generally do NOT
sum to zero — but r · s = 0 still holds. (Practice problem 6.)

## 11. You've been running this for years

`lm(dist ~ speed)` · Excel "Add Trendline" · `numpy.linalg.lstsq(A, b)` ·
`sklearn LinearRegression().fit(X, y)` — all solve this same projection.

## 12. The projection matrix P (the "hat matrix")

The shadow is a matrix applied to b:

    P = A(AᵀA)⁻¹Aᵀ        ŷ = Py   ("puts the hat on y")

Properties (Backup A):
- **P² = P** — project twice = project once. "The shadow of a shadow is itself."
- **Pᵀ = P** — symmetric ⟺ it projects **straight down** (orthogonally), not at an angle.
- **I − P** projects onto the perpendicular direction → gives the residual: r = (I − P)b.
- Statisticians use P's diagonal for **leverage / diagnostics** (Module 7).

Tiny example: A = (1, 1)ᵀ (just an intercept, 2 points).
AᵀA = 2, so P = (1/2)·[1 1; 1 1]. For y = (3, 5): Py = (4, 4) — the mean again.
Check P²: (1/2)[1 1;1 1]·(1/2)[1 1;1 1] = (1/4)[2 2;2 2] = (1/2)[1 1;1 1] = P ✓

## 13. The calculus road (Backup C, preview of Module 5)

Minimize f(x) = ‖Ax − b‖². Set the gradient to zero:
∇f = 2Aᵀ(Ax − b) = 0 ⟹ **AᵀAx = Aᵀb** — the same normal equations by a second road.
The Hessian (matrix of second derivatives) is **2AᵀA**, which is **positive
semidefinite** → the critical point is a **minimum**, not a maximum.
"Two independent arguments, one answer" — geometry and calculus agree.

## 14. Cliffhanger

Every textbook writes (AᵀA)⁻¹Aᵀb. **R's lm() never computes it. Why not?** → Lesson 3.
