# Practice Solutions — Module 4

(Every numerical answer here was checked with numpy.)

---

## Part A — True / False

1. **F** — + means pseudoinverse (generalized inverse), not transpose.
2. **F** — AᵀA is (unknowns × unknowns); 2×2 for 2 parameters no matter how many points.
3. **F** — only the intercept (all-ones) column forces Σr = 0. See C5.
4. **T** — project twice = project once.
5. **F** — QR pays κ(A). The normal equations pay κ(A)².
6. **F** — lm() uses (Householder, pivoted) QR and never forms XᵀX.
7. **F** — L1 / city-block has no clean formula; you have to search.
8. **T** — cars degree-5: κ(A) 2.3 × 10⁸ → 62.
9. **F** — it means two features carry the same information (aliased). Fix the data.
10. **F** — SVD is the most expensive; normal equations are cheapest.
11. **F** — + and − errors cancel; the flat line scores a "perfect" 0.
12. **T** — symmetric projection = orthogonal projection.

## Part B — Short theory

**B1.**
(a) Tall → usually **no** exact solution → least squares.
(b) Square, full rank (det ≠ 0) → **exactly one**.
(c) Wide → **infinitely many** (if any).
(d) Redundant columns (rank 3, not 4) → **infinitely many** least-squares solutions →
SVD / pseudoinverse picks the minimum-norm one.

**B2.**
- Plain sum: positive and negative errors cancel → a useless line can score 0.
- Sum of |errors|: sensible and robust to outliers, but no clean formula — must search
  (→ Lasso, Module 7).
- Sum of squares = ‖Ax − b‖², squared straight-line distance → minimum = closest point
  = projection → clean formula (normal equations).

**B3.**
1. r = b − Ax̂ must be perpendicular to the plane col(A) (closest point = perpendicular drop).
2. Perpendicular to the plane ⟺ perpendicular to every column of A ⟺ Aᵀr = 0.
3. Substitute: Aᵀ(b − Ax̂) = 0 ⟹ Aᵀb − AᵀAx̂ = 0.
4. Rearrange: **AᵀAx̂ = Aᵀb** — a small square system (unknowns × unknowns).

**B4.** Gram–Schmidt's step 2 subtracts from a column its projection onto q₁. When q₁
is the normalized all-ones column, the projection of s onto it is (mean of s)·(1,…,1)
(Tool 7). So subtracting it = subtracting the mean = centering. E.g. (1,2,3) − (2,2,2)
= (−1,0,1).

**B5.** With an intercept, A contains the all-ones column. The normal equations say
Aᵀr = 0, i.e. r ⊥ every column, including (1,…,1). (1,…,1)·r = Σrᵢ, so Σrᵢ = 0.

## Part C — Calculations

### C1
(a) Try b = x₁(1,1,1) + x₂(1,2,3). Rows 1 and 2: x₁ + x₂ = 2, x₁ + 2x₂ = 4 → x₂ = 2,
x₁ = 0. Row 3: 0 + 3·2 = 6 ✓. **Yes, x = (0, 2).** rank([A|b]) = rank(A) = 2.
(b) Rows 1 and 2: x₁ + x₂ = 1, x₁ + 2x₂ = 1 → x₂ = 0, x₁ = 1. Row 3: 1 + 0 = 1 ≠ 2 ✗.
**No exact solution.** rank([A|b]) = 3 > 2. → least squares.

### C2
(a) A = [1 1; 1 2; 1 3; 1 4], x = (x₁, x₂), b = (2, 3, 5, 6).
(b) n = 4, Σs = 10, Σs² = 1+4+9+16 = 30, Σt = 16, Σs·t = 2+6+15+24 = 47.

    AᵀA = [ 4 10]      Aᵀb = [16]
          [10 30]            [47]

(c) det = 120 − 100 = 20.
x̂ = (1/20)·[30 −10; −10 4]·(16, 47) = (1/20)·(480 − 470, −160 + 188) = (1/20)·(10, 28)
**x̂₁ = 0.5, x̂₂ = 1.4.**
(d) Fitted 0.5 + 1.4s = (1.9, 3.3, 4.7, 6.1). Residuals t − ŷ = **(0.1, −0.3, 0.3, −0.1)**.
Check: Σr = 0 ✓; s·r = 0.1 − 0.6 + 0.9 − 0.4 = 0 ✓ → Aᵀr = 0.

### C3
(a) ‖a₁‖ = √4 = 2 → q₁ = (1,1,1,1)/2.
a₂·q₁ = (1+2+3+4)/2 = 5.
v₂ = (1,2,3,4) − 5·(1,1,1,1)/2 = (1,2,3,4) − (2.5,2.5,2.5,2.5) = (−1.5, −0.5, 0.5, 1.5)
(= s minus its mean 2.5 — centering!).
‖v₂‖ = √(2.25+0.25+0.25+2.25) = √5 → q₂ = (−1.5, −0.5, 0.5, 1.5)/√5.

    R = [2   5 ]
        [0  √5 ]

(b) q₁·b = 16/2 = 8. q₂·b = (−3 − 1.5 + 2.5 + 9)/√5 = 7/√5. Qᵀb = (8, 7/√5).
(c) Bottom: √5·x₂ = 7/√5 → x₂ = 7/5 = **1.4**. Top: 2x₁ + 5(1.4) = 8 → x₁ = **0.5**. ✓ matches.
(numpy gives R and Qᵀb with flipped signs — that's just a sign convention; x̂ is identical.)

### C4
(a) Errors t − 4 = (−2, −1, 1, 2). Σ = **0**, Σ|·| = **6**, Σ² = 4+1+1+4 = **10**.
(b) Σr² = 0.01 + 0.09 + 0.09 + 0.01 = **0.2**.
(c) The plain sum was fooled: the flat line scored a "perfect" 0 even though it ignores
s entirely. Squared error correctly ranks the fitted line (0.2) far better than the
flat line (10).

### C5
(a) A = (1,2,3)ᵀ. AᵀA = 14, Aᵀb = 31 → **x̂ = 31/14 ≈ 2.214**.
(b) ŷ = (2.214, 4.429, 6.643), r = **(0.786, 0.571, −0.643)**, Σr ≈ **0.714 ≠ 0**.
(c) r·s = 0.786 + 1.143 − 1.929 = **0**. The normal equations force r ⊥ every column
of A — the only column is s, so r ⊥ s. There's no all-ones column, so nothing forces Σr = 0.

### C6
(a) AᵀA = 3, AAᵀ = 3×3 all-ones → **P = (1/3)·[all-ones 3×3]**.
(b) Py = (14/3, 14/3, 14/3) ≈ (4.67, 4.67, 4.67) — the **flat line t = 4.67** from the
"Least wrong — measured how?" slide. Intercept-only fit = the mean.
(c) (I − P)y = y − Py = **(−1.67, 0.33, 1.33)** = the residuals of that flat line (sum 0).
(d) P² = (1/9)·[all-ones]·[all-ones] = (1/9)·[all-threes] = (1/3)·[all-ones] = P ✓.

### C7
(a) QR: lose ~**5** (keep 11). Normal equations: κ² = 10¹⁰ → lose ~**10** (keep 6).
(b) κ(A) = √(10¹⁴) = **10⁷**.
(c) κ(A) = 50/0.005 = **10⁴**; κ(AᵀA) = **10⁸**.
(d) κ(A)² ≈ 10¹⁶ → κ(A) ≈ **10⁸** (exactly the slide's example).

### C8
q₁ = (1,1)/√2. a₂·q₁ = 2/√2 = √2.
v₂ = (2,0) − √2·(1,1)/√2 = (2,0) − (1,1) = (1, −1). ‖v₂‖ = √2 → q₂ = (1,−1)/√2.

    R = [√2  √2]
        [0   √2]

Check column 2 of QR: √2·q₁ + √2·q₂ = (1,1) + (1,−1) = (2,0) = a₂ ✓.
Column 1: √2·q₁ = (1,1) = a₁ ✓.

### C9
(a) σ = 5, 2, 10⁻¹⁵. κ(A) = 5/10⁻¹⁵ = 5 × 10¹⁵ → hopeless.
(b) A⁺ = diag(1/5, 1/2, **0**) = diag(0.2, 0.5, 0).
(c) x̂ = (10·0.2, 4·0.5, 0) = **(2, 2, 0)**.
(d) Naive: x₃ = 1/10⁻¹⁵ = **10¹⁵**. That direction carries no real information (it's
rounding noise), yet it would dominate the answer. Zeroing 1/σ throws that garbage
direction away.

### C10
(a) Column 2 = 3 × column 1 → linearly dependent → rank 1. Exact solutions: all x with
x₁ + 3x₂ = 4 → **infinitely many**.
(b) e.g. (4, 0) and (1, 1). (Also (0, 4/3), (−2, 2), …)
(c) Shortest point on the line x₁ + 3x₂ = 4 lies along the direction (1, 3):
x = c·(1,3), c + 9c = 4 → c = 0.4 → **x̂ = (0.4, 1.2)**, ‖x̂‖ ≈ 1.26
(vs ‖(1,1)‖ ≈ 1.41, ‖(4,0)‖ = 4). Same predictions as every other solution.

### C11
(a) 8617/1.62 ≈ **5.3 × 10³** (fine). With all three: 8617/(6 × 10⁻¹⁵) ≈ **1.4 × 10¹⁸**
→ effectively infinite (rank-deficient).
(b) Normal equations → "computationally singular" error. lm() (pivoted QR) → aliases
the duplicate column, coefficient = **NA**. SVD pseudoinverse → sets 1/σ₃ = 0 →
minimum-norm solution, **same predictions**.
