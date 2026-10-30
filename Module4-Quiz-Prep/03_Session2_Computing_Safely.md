# Lesson 3 — Session 2: Computing It Without Breaking It

Slides: `Lectures/M04-Session2-Slides.pdf`

Session 1 found the answer. Session 2: **the textbook formula can destroy that answer
on a real computer** — and what to use instead.

---

## 1. Floats aren't the real numbers (callback to Day 1)

- Day 1: integers in a computer aren't closed under + → overflow.
- Reals get the same treatment: a **double stores ~16 significant digits** and rounds
  the rest. `0.1 + 0.2 == 0.3` → **FALSE**.
- Usually harmless. But if a calculation **amplifies tiny errors by 10¹²**, only
  ~16 − 12 = 4 trustworthy digits are left.

## 2. Condition number κ(A)

**κ(A) measures how much A amplifies small errors.** Formula (from the SVD):

    κ(A) = σ_max / σ_min      (largest singular value ÷ smallest)

- κ ≈ 1 → well-conditioned (great). Huge κ → ill-conditioned.
- **Rule of thumb: you lose about log₁₀ κ digits** (out of ~16).

| κ | digits lost | digits kept |
|---|---|---|
| 10³ | 3 | 13 |
| 10⁸ | 8 | 8 — fine |
| 10¹⁶ | 16 | **0 — garbage** |

## 3. The key danger: κ(AᵀA) = κ(A)²

The normal equations solve with AᵀA, and **forming AᵀA squares the condition number**:

    κ(A) = 10⁸  (lose 8, keep 8)   →   κ(AᵀA) = 10¹⁶  (lose 16, keep none)

"The normal equations square the problem's sensitivity **before** solving it."
That's the answer to the cliffhanger: **lm() never forms AᵀA.**

**Why it squares (Backup B — learn these 3 lines):**
1. A = UΣVᵀ, so AᵀA = VΣUᵀUΣVᵀ = VΣ²Vᵀ (because UᵀU = I).
2. So the singular values of AᵀA are σᵢ² — biggest and smallest both get squared.
3. κ(AᵀA) = σ²_max / σ²_min = (σ_max/σ_min)² = κ(A)².
(QR works with R, which has the **same** singular values as A → only κ(A).)

Your lecture example: κ(A) ≈ 6.79, κ(AᵀA) ≈ 46.1 = 6.79². Harmless there — it's
the big κ's that kill you.

## 4. Real data: cars (stopping distance vs speed, n = 50)

Fit polynomials of increasing degree in speed (columns 1, s, s², …, s⁵):
- Degree 5: **κ(A) ≈ 2.3 × 10⁸**, **κ(AᵀA) ≈ 5.3 × 10¹⁶** — past 1/ε ≈ 4.5 × 10¹⁵,
  i.e. all 16 digits gone.
- Normal equations in R → **"system is computationally singular"**.
- QR on the same data → solves it; fitted values match a stable reference to ~10⁻¹¹.

Why polynomials are so bad: s⁴ and s⁵ (for s from 4 to 25) look almost like the same
column → nearly redundant → huge κ.

## 5. What A would make least squares trivial?

If A's columns were **orthonormal** (call that matrix Q), then QᵀQ = I, and the normal
equations QᵀQx = Qᵀb become just **x = Qᵀb** — dot products, nothing to invert, no κ².

So: **can we swap A's columns for orthonormal ones that span the same space?** Yes → QR.

## 6. Gram–Schmidt: project, subtract, repeat

1. Keep a₁; normalize it → **q₁ = a₁/‖a₁‖**
2. From a₂, subtract its projection onto q₁ (Module 2): **v₂ = a₂ − (a₂·q₁)q₁**
3. Normalize what's left → **q₂ = v₂/‖v₂‖**. Continue for a₃, a₄, … (subtract projections
   onto ALL previous q's).
4. The amounts you used form an **upper-triangular R**:

        R = [ ‖a₁‖    a₂·q₁ ]
            [ 0       ‖v₂‖  ]

Result: **A = QR** (Q orthonormal columns, R upper-triangular).

## 7. Solving least squares with QR

Substitute A = QR into AᵀAx = Aᵀb:
RᵀQᵀQRx = RᵀQᵀb → RᵀRx = RᵀQᵀb → **Rx̂ = Qᵀb**, then **back-substitute** (bottom row
first). Never forms AᵀA.

**Lecture example — do this by hand** (a₁ = (1,1,1), a₂ = (1,2,3), b = (3,5,6)):

- ‖a₁‖ = √3 → **q₁ = (1,1,1)/√3**
- a₂·q₁ = (1+2+3)/√3 = 6/√3 = **2√3**
- v₂ = a₂ − (a₂·q₁)q₁ = (1,2,3) − 2√3·(1,1,1)/√3 = (1,2,3) − (2,2,2) = **(−1, 0, 1)**
- ‖v₂‖ = √2 → **q₂ = (−1,0,1)/√2**

        R = [√3   2√3]        Qᵀb = [q₁·b] = [14/√3]
            [0    √2 ]              [q₂·b]   [3/√2 ]

  (q₂·b = (−3 + 0 + 6)/√2 = 3/√2)

- Bottom row: √2·x₂ = 3/√2 → **x₂ = 3/2**
- Top row: √3·x₁ + 2√3·(3/2) = 14/√3 → multiply by √3: 3x₁ + 9 = 14 → **x₁ = 5/3**

Same answer as the normal equations (5/3, 3/2) ✓ — same projection, safer route.

**The slide's punchline:** (−1, 0, 1) is s = (1,2,3) **minus its mean** (2).
**Centering a feature is one step of Gram–Schmidt against the intercept column.**
(Subtracting the projection onto the all-ones vector = subtracting the mean — Tool 7.)

## 8. Redundant columns: the SVD returns

QR handles *bad* conditioning. What if columns are **exactly** redundant (rank-deficient)?

**Production bug (mtcars):** car weight entered twice — in 1000 lb and in kg. One
column is a constant multiple of the other → linearly dependent → **rank-deficient**.

Singular values of A: **8617, 1.62, 6 × 10⁻¹⁵**. The last is zero up to rounding → that
direction **carries no information**.

| Solver | Result |
|---|---|
| Normal equations | error: computationally singular |
| lm() (pivoted QR) | redundant coefficient reported as **NA** |
| SVD pseudoinverse | **minimum-norm** solution; **same predictions** |

## 9. The pseudoinverse A⁺

**The + means pseudoinverse — NOT a transpose.** (Instructor explicitly clarified this.)

From A = UΣVᵀ:

    A⁺ = V Σ⁺ Uᵀ,   Σ⁺ = take 1/σ for each singular value you trust,
                          and SET 1/σ TO 0 for the tiny ones.
    x̂ = A⁺b

"Invert the singular values you trust, zero the rest." Without zeroing,
1/(6 × 10⁻¹⁵) ≈ 1.7 × 10¹⁴ would blow the answer up.

**What "minimum-norm" means** — example: A has columns (1,2,3) and (2,4,6),
b = (1,2,3). Then any x with x₁ + 2x₂ = 1 fits perfectly — infinitely many answers
(the "wide/redundant" case!). (1, 0), (0, 0.5), (3, −1)… all give the same predictions.
The pseudoinverse picks the **shortest** x on that line: **(0.2, 0.4)**
(‖x‖ = 0.447, smaller than ‖(0, 0.5)‖ = 0.5 or ‖(1, 0)‖ = 1).
It splits the effect across the duplicate columns instead of picking one arbitrarily.

## 10. Three solvers, different failure modes (MEMORIZE)

|  | Normal equations | QR | SVD |
|---|---|---|---|
| Forms AᵀA? | Yes | No | No |
| Sensitivity | κ(A)² | κ(A) | κ(A) |
| Redundant columns | Fails | Detects (pivoting → NA) | Handles (minimum norm) |
| Relative cost | Cheapest | Moderate | Most expensive |
| You'll find it in | Textbooks, hand calculations | R's lm() | numpy.linalg.lstsq |

> **Default: QR. Reach for SVD when features may be redundant. Use the normal
> equations on paper, not in production.**

## 11. What this changes day-to-day

- **Standardize features.** Degree-5 cars fit: κ(A) drops from **2.3 × 10⁸ to 62**
  after centering and scaling speed. Now even the normal equations cope.
- **Read NA as a message.** An NA coefficient in lm() means two features carry the
  same information. **Fix the data, don't fight the solver.**
- **Too big to factor?** Millions of rows and columns → even QR too expensive →
  **iterate** instead (gradient descent, Module 8).

## 12. Inside R's lm() (Backup D)

lm() → lm.fit() → C_Cdqrls → **dqrdc2**
- lm.fit() supports only method = "qr". **It never forms XᵀX.**
- dqrdc2 = R's modified LINPACK **Householder QR** with **limited column pivoting**:
  columns with near-zero norm (after orthogonalizing) get moved to the end.
- Those moved columns are **"aliased"** → that's why their coefficients print as **NA**.

## 13. Where ‖Ax − b‖² shows up next

| Module | Idea added |
|---|---|
| 5 — Multivariable calculus | Gradient of ‖Ax − b‖² = 0 → same normal equations, second road |
| 7 — Regression & statistics | Add **λ‖x‖²** → **ridge regression**; also cures bad conditioning and redundancy |
| 8 — Optimization | A too big to factor → walk downhill on ‖Ax − b‖²: **gradient descent** |
