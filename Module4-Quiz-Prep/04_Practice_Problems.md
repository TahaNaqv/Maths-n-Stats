# Practice Problems — Module 4

Do these on paper. These use **new numbers** (not the lecture's), so you can't just
remember the answers. Solutions are in `05_Practice_Solutions.md`.

---

## Part A — True / False (1 line justification each)

1. A⁺ is the transpose of A.
2. The normal-equations system gets bigger as you collect more data points.
3. If the model has no intercept, the residuals still always sum to zero.
4. For the hat matrix, P² = P.
5. Solving least squares with QR has sensitivity κ(A)².
6. R's lm() computes (XᵀX)⁻¹Xᵀy.
7. Minimizing the sum of |errors| has a clean closed-form formula.
8. Centering and scaling a feature can reduce the condition number.
9. An NA coefficient from lm() means R has a bug.
10. The SVD is the cheapest of the three solvers.
11. Minimizing the plain sum of errors is a good way to fit a line.
12. Pᵀ = P tells you the projection is orthogonal ("straight down").

## Part B — Short theory

**B1.** Classify each system (one solution / usually none / infinitely many) and name
the case:
(a) 100 data points, model with 3 parameters.
(b) 2×2 system with determinant 7.
(c) 3 equations, 5 unknowns.
(d) 50 × 4 matrix whose 4th column is 2 × its 3rd column.

**B2.** Why does least squares use squared errors instead of plain errors or absolute
errors? (3 bullet points.)

**B3.** Write the 4-step derivation of the normal equations from "the residual is
perpendicular to the column space".

**B4.** Explain in 2–3 sentences why centering a feature is "one step of Gram–Schmidt
against the intercept column".

**B5.** Explain why the residuals of a fit with an intercept sum to zero.

## Part C — Calculations

**C1. Rank test.** A has columns a₁ = (1,1,1), a₂ = (1,2,3).
(a) Does Ax = b have an exact solution for b = (2, 4, 6)? If yes, find x.
(b) For b = (1, 1, 2)?

**C2. Least squares by the normal equations.**
Data: s = (1, 2, 3, 4), t = (2, 3, 5, 6). Model t = x₁ + x₂·s.
(a) Write A, x, b.
(b) Compute AᵀA and Aᵀb.
(c) Solve for x̂.
(d) Compute the fitted values and residuals. Check that Aᵀr = 0.

**C3. Same problem by QR.** Same A and b as C2.
(a) Run Gram–Schmidt on the columns to get q₁, q₂ and R.
(b) Compute Qᵀb.
(c) Solve Rx̂ = Qᵀb by back-substitution. Do you match C2?

**C4. Scoring lines.** Same data as C2.
(a) For the flat line t = 4 (the mean of t), compute Σ errors, Σ |errors|, Σ errors².
(b) For your fitted line from C2, compute Σ errors².
(c) Which score was fooled in (a)? Why?

**C5. No intercept.** Lecture data s = (1,2,3), t = (3,5,6), but the model is
t = x·s (no overhead).
(a) Find x̂ (A is a single column).
(b) Compute the residuals. Do they sum to zero?
(c) Compute r · s. Explain the result.

**C6. Hat matrix.** Model = intercept only: A = (1, 1, 1)ᵀ.
(a) Compute P = A(AᵀA)⁻¹Aᵀ.
(b) Compute Py for y = (3, 5, 6). Which lecture slide's line is this?
(c) Compute (I − P)y. What is it?
(d) Verify P² = P.

**C7. Condition numbers** (double ≈ 16 digits).
(a) κ(A) = 10⁵. Digits lost via QR? Via the normal equations?
(b) κ(AᵀA) = 10¹⁴. What is κ(A)?
(c) A has singular values 50 and 0.005. Find κ(A) and κ(AᵀA).
(d) Beyond roughly what κ(A) do the normal equations keep zero digits?

**C8. Gram–Schmidt in 2-D.** a₁ = (1, 1), a₂ = (2, 0). Find q₁, q₂, R, and check
that QR gives back A.

**C9. Pseudoinverse.** A = diag(5, 2, 10⁻¹⁵) (a 3×3 diagonal matrix, so U = V = I).
(a) What are the singular values and κ(A)?
(b) Write A⁺ (pseudoinverse with the tiny singular value zeroed).
(c) For b = (10, 4, 1), compute x̂ = A⁺b.
(d) What would naive inversion give for x₃? Why is that bad?

**C10. Minimum norm.** A has columns (1, 1) and (3, 3); b = (4, 4).
(a) Why is A rank-deficient? How many exact solutions?
(b) Give two different exact solutions.
(c) Find the minimum-norm solution (the one A⁺ returns).

**C11. mtcars.** Singular values of A were 8617, 1.62, 6 × 10⁻¹⁵.
(a) Compute κ(A) using the first two only, and using all three.
(b) What does each of the three solvers do with this A?
