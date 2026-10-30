# Module 4 — Practice Quiz (QUESTIONS)

Attempt these by hand first. Answer key is in the separate file
`04_Quiz_ANSWER_KEY.md`. Mix of theory-reasoning and calculation, in your
instructor's style. ~20–25 min.

---

### Q1 (theory)
When does the system Ax = b have an exact solution? State the condition in terms of
the column space, and explain how the rank test on [A | b] detects it.

### Q2 (theory)
A linear system falls into one of three cases by shape/rank. Name all three, state how
many solutions each has, and say which one least squares is designed for.

### Q3 (theory)
Three ways to score the total error of a fitted line are: sum the errors, sum the
absolute errors, sum the squared errors. Give the main problem with the first, the main
drawback of the second, and the reason the third is preferred.

### Q4 (calculation)
You measure a web service twice: 1 MB → 3 ms, 2 MB → 5 ms. Using the model
t = x₁ + x₂·s:
(a) Write the matrix A, the vector x, and the vector b for Ax = b.
(b) Solve for x₁ and x₂ (exact solution exists here).

### Q5 (theory + derivation)
Starting from "the residual must be perpendicular to the column space," derive the
normal equations. Show each logical step.

### Q6 (theory)
In the 3-measurement least-squares fit, the residuals came out (−0.17, +0.33, −0.17),
which sum to exactly 0. Explain *why* they must sum to zero.

### Q7 (theory)
What does P² = P mean in words, and what is P (the "hat matrix") used for?

### Q8 (calculation / reasoning)
A matrix A has condition number κ(A) = 10⁶. A double holds about 16 significant digits.
(a) Roughly how many digits of accuracy do you lose if you solve via QR?
(b) Roughly how many do you lose if you solve via the normal equations? Show why.
(c) Which method would you trust here?

### Q9 (theory)
State the relationship between κ(AᵀA) and κ(A), and explain in one or two sentences why
this makes the normal equations risky on real data.

### Q10 (theory)
What does QR factorization produce (describe Q and R), and why does using it avoid the
conditioning problem of the normal equations?

### Q11 (theory)
In A⁺, what does the "+" mean — and what does it NOT mean? Describe briefly how the
pseudoinverse is computed from the SVD, including what it does with tiny singular
values.

### Q12 (applied reasoning)
In the mtcars example, car weight was entered twice — once in pounds, once in
kilograms. 
(a) Why does this make A rank-deficient?
(b) What does each of the three solvers do: normal equations, lm() (pivoted QR), SVD
pseudoinverse?

### Q13 (reasoning)
You run lm() in R and one coefficient comes back as NA. What is this telling you, and
what is the correct response?

### Q14 (theory / connections)
Session 2 says the gradient of ‖Ax − b‖² set to zero gives the same normal equations.
Name the three later modules this module connects to and the one idea each adds.

### Q15 (fill-in-the-table, calculation-style recall)
Reproduce the three-solver comparison table with these rows: "Forms AᵀA?",
"Sensitivity (κ)", "Handles redundant columns?", "Relative cost", for the three columns
Normal equations / QR / SVD.
