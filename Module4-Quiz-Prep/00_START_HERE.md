# Module 4 Quiz Prep — Start Here

Quiz scope: **Module 4 — Systems & Projections** (everything after Sessional 1).
- Session 1 — When the equations disagree (least squares, normal equations)
- Session 1 supplement — "Throw one away?", "Two pictures", worked example
- Session 2 — Computing it without breaking it (conditioning, QR, SVD/pseudoinverse)
- Session 2 backup slides A–D (optional reading, but cheap marks — covered here)

## Study order (≈ 4–5 hours total)

| Step | File | Time | Goal |
|---|---|---|---|
| 1 | `01_Toolkit_From_Zero.md` | 60 min | The 7 tools everything else uses. Do NOT skip. |
| 2 | `02_Session1_Least_Squares.md` | 75 min | The idea + the by-hand calculation |
| 3 | `03_Session2_Computing_Safely.md` | 60 min | Condition number, QR, pseudoinverse |
| 4 | `04_Practice_Problems.md` | 60 min | Do them on paper, no peeking |
| 5 | `05_Practice_Solutions.md` | 20 min | Mark yourself, re-read weak spots |
| 6 | `../files-sent-by-friend/04_Quiz_QUESTIONS.md` | 25 min | Timed mock (answer key in same folder) |
| 7 | `../files-sent-by-friend/03_Cheatsheet.md` | 10 min | Last thing before the quiz |

Your friend's files are accurate (I checked them against the slides). What they
skip is the **arithmetic** — the instructor worked the normal equations AND the QR
route by hand on the slides, so expect to do both on the quiz. Files 02 and 03 show
every step.

## The whole module in 6 sentences

1. Ax = b has an exact solution only if b is a combination of A's columns (b ∈ col(A)).
2. With more measurements than unknowns, it usually isn't — so we find the x whose
   Ax is **closest** to b: minimize ‖Ax − b‖² (least squares).
3. Closest point = perpendicular drop (a shadow), so the residual r = b − Ax̂ is
   perpendicular to every column: Aᵀr = 0 ⟹ **AᵀAx̂ = Aᵀb** (normal equations).
4. On a computer, forming AᵀA **squares the condition number**: κ(AᵀA) = κ(A)², and
   you lose about log₁₀κ of your 16 digits.
5. **QR** (Gram–Schmidt) solves the same problem via Rx̂ = Qᵀb without forming AᵀA, so
   it only pays κ(A). It is R's lm() default.
6. If columns are exactly redundant, use the **SVD pseudoinverse A⁺** (+ ≠ transpose):
   invert trusted singular values, zero the tiny ones → minimum-norm solution.
