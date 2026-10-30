# Lesson 1 — The Toolkit (from zero)

Everything in Module 4 is built from these 7 tools. Get each one solid, try the
mini-check at the end of each, then move on.

---

## Tool 1 — Vectors and the dot product

A **vector** is a list of numbers: a = (1, 2, 3). Think of it as an arrow, or as a
point in space (3 numbers → a point in 3-D).

The **dot product** multiplies matching entries and adds:

    a · b = a₁b₁ + a₂b₂ + a₃b₃

    (1, 2, 3) · (3, 5, 6) = 3 + 10 + 18 = 31

Special case — dotting with all ones just **adds up the entries**:

    (1, 1, 1) · (3, 5, 6) = 3 + 5 + 6 = 14

Remember that one; it's why the residuals sum to zero later.

**Mini-check:** (1, 1, 1, 1) · (2, 3, 5, 6) = ?   → 16

---

## Tool 2 — Length (norm) and "perpendicular"

**Length** of a vector (the L2 norm, Module 2):

    ‖a‖ = √(a₁² + a₂² + …)        ‖(−1, 0, 1)‖ = √(1 + 0 + 1) = √2

So the **squared length** is just the sum of squares:

    ‖a‖² = a₁² + a₂² + …  = a · a

Least squares minimizes ‖Ax − b‖² = **sum of squared errors**. Same thing.

**Perpendicular (orthogonal)** ⟺ dot product is zero:

    (1, 1, 1) · (−1, 0, 1) = −1 + 0 + 1 = 0   → perpendicular

A **unit vector** has length 1. To make one, divide by the length (**normalize**):

    (1, 1, 1) has length √3  →  q = (1, 1, 1)/√3

**Orthonormal** vectors = mutually perpendicular AND each of length 1.

**Mini-check:** Is (1, 2) perpendicular to (2, −1)? → 2 − 2 = 0, yes.

---

## Tool 3 — Matrix times vector: the COLUMN picture

    A = [1 1]      x = [x₁]
        [1 2]          [x₂]
        [1 3]

Two ways to compute Ax — same answer:

**Row picture:** each row dotted with x →  (x₁ + x₂,  x₁ + 2x₂,  x₁ + 3x₂)

**Column picture (the one Module 4 is built on):** Ax is a **mix of A's columns**,
with x giving the amounts:

    Ax = x₁·(1, 1, 1) + x₂·(1, 2, 3)

So whatever x you pick, **Ax is always some combination of the columns of A.**
You can never get out of the "space the columns make".

**Mini-check:** with x = (1, 2), Ax = 1·(1,1,1) + 2·(1,2,3) = (3, 5, 7).

---

## Tool 4 — Column space and rank

- **Column space col(A)** = every vector you can make by mixing A's columns.
  Two (non-parallel) columns in 3-D make a **plane** through the origin.
- **Rank** = number of genuinely independent columns = dimension of col(A).
  - columns (1,1,1) and (1,2,3): not multiples of each other → rank 2 (a plane).
  - columns (1,2,3) and (2,4,6): second is 2× the first → rank 1 (just a line).
    That's a **redundant column** — it adds nothing new.

**The rank test for Ax = b:**
Glue b on as an extra column: [A | b]. Compare ranks.

| rank([A|b]) vs rank(A) | Meaning | Exact solution? |
|---|---|---|
| same | b was already a mix of A's columns | **Yes** |
| bigger (by 1) | b points in a new direction, sticks out of col(A) | **No** |

**Mini-check:** A has columns (1,1,1),(1,2,3). Is b = (2,4,6) reachable?
→ b = 0·(1,1,1) + 2·(1,2,3). Yes, rank stays 2. But b = (3,5,6)? No — rank jumps
to 3 (that's the lecture example).

---

## Tool 5 — Transpose, and what Aᵀr really means

**Transpose** Aᵀ: rows become columns.

    A = [1 1]        Aᵀ = [1 1 1]
        [1 2]             [1 2 3]
        [1 3]

**The key fact:** Aᵀr = the dot product of **each column of A** with r, stacked up.

    Aᵀr = [ (1,1,1)·r ]
          [ (1,2,3)·r ]

So **Aᵀr = 0** means "r is perpendicular to every column of A". That one sentence is
the heart of the normal equations.

Also: **AᵀA** is a small square table of column-dot-column products:

    AᵀA = [ col1·col1   col1·col2 ]  =  [ 3   6 ]
          [ col2·col1   col2·col2 ]     [ 6  14 ]

(1,1,1)·(1,1,1) = 3, (1,1,1)·(1,2,3) = 6, (1,2,3)·(1,2,3) = 1+4+9 = 14.

**Mini-check:** Aᵀb for b = (3,5,6) → ((1,1,1)·b, (1,2,3)·b) = (14, 31).

---

## Tool 6 — Solving a 2×2 system (two methods)

**Elimination:**

    3x₁ +  6x₂ = 14
    6x₁ + 14x₂ = 31

Multiply eq.1 by 2: 6x₁ + 12x₂ = 28. Subtract from eq.2: 2x₂ = 3 → **x₂ = 1.5**.
Back into eq.1: 3x₁ + 9 = 14 → **x₁ = 5/3 ≈ 1.67**.

**Inverse formula** (memorize):

    [a b]⁻¹  =   1/(ad − bc) · [ d  −b]
    [c d]                      [−c   a]

    [3  6]⁻¹ = 1/(42 − 36) · [14 −6]  = (1/6)·[14 −6]
    [6 14]                   [−6  3]          [−6  3]

    x = (1/6)·(14·14 − 6·31,  −6·14 + 3·31) = (1/6)·(10, 9) = (5/3, 3/2)  ✓

If ad − bc = 0 the matrix has **no inverse** (it's singular) — that happens exactly
when columns are redundant.

**Back-substitution** (for triangular systems — used in QR):

    [2  5 ] [x₁]   [8    ]
    [0 √5 ] [x₂] = [7/√5 ]

Start from the **bottom** row: √5·x₂ = 7/√5 → x₂ = 7/5 = 1.4.
Then top row: 2x₁ + 5(1.4) = 8 → x₁ = 0.5.

---

## Tool 7 — Projection onto a line (Module 2 refresher)

The closest point to b on the line through vector a (the "shadow" of b):

    p = (a·b / a·a) · a        and the leftover  r = b − p  is perpendicular to a.

Example: project b = (3, 5) onto a = (1, 1):
a·b = 8, a·a = 2 → p = 4·(1,1) = (4, 4). Leftover r = (−1, 1). Check r·a = 0 ✓.

Notice: projecting onto the all-ones vector gives **the mean** (4 = average of 3
and 5). Fitting "just a constant" = taking the average.

Module 4 = the same idea, but projecting onto a **plane** (or bigger) instead of a line.

---

## Tool 8 (bonus, from Module 3) — Singular values in one paragraph

Every matrix can be written **A = UΣVᵀ** (the SVD). U and V are rotations
(orthonormal), Σ is diagonal with **singular values** σ₁ ≥ σ₂ ≥ … ≥ 0. Think of the
σ's as **how much A stretches space in each independent direction.**
- Largest σ = most stretch, smallest σ = least stretch.
- A σ that is **0** (or ~10⁻¹⁵ on a computer) = a direction A squashes flat =
  a redundant column. Those are what the pseudoinverse throws away.
- **Condition number** κ(A) = σ_max / σ_min (how lopsided the stretching is).

That's all the SVD you need for this quiz.
