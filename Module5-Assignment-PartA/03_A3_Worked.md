# A3 — Beyond the Zoo, Worked Step by Step [6 marks: choose any 6]

Each one needs checklist **items 1–5** (½ mark) plus a labelled sketch (½ mark). Items
6–7 are optional, but they're included here because they're one line each.

## Which six should you pick?

All ten are worked below. If you're short on time, the **quickest six** need only the
power rule and no tricky algebra:

> **A3.1 x², A3.2 x³, A3.3 |x|, A3.4 1/x, A3.5 √x, A3.9 −ln p**

The other four (A3.6, A3.7, A3.8, A3.10) are slightly longer but are the most
"ML-flavoured", so read them before the exam even if you don't submit them. A3.7
also feeds A4.3.

---

## A3.1  f(x) = x²   (squared-error loss)

1. **Domain / range:** ℝ / [0, ∞)
2. **Special values:** f(0) = 0; only zero x = 0. f(±1) = 1, f(±2) = 4.
3. **Ends:** x → ±∞: x² → +∞. No asymptotes.
4. **f′ = 2x.** Negative for x < 0 (decreasing), positive for x > 0 (increasing).
   Critical point x = 0: f′ goes − → + ⇒ **local and global minimum at (0, 0)**. No max.
5. **f″ = 2 > 0** ⇒ concave up everywhere, no inflection.
6. Even: (−x)² = x².
7. Squared-error loss (y − ŷ)²: big errors are punished quadratically.

**Sketch:** a ∪ parabola with its vertex at (0, 0), passing through (±1, 1) and (±2, 4). → `plots/A3_01_x2.png`

---

## A3.2  f(x) = x³   (f′(0) = 0, yet no max or min. Why?)

1. **Domain / range:** ℝ / ℝ
2. **Special values:** f(0) = 0, the only zero. f(1) = 1, f(−1) = −1, f(2) = 8.
3. **Ends:** x → +∞: +∞; x → −∞: −∞. No asymptotes.
4. **f′ = 3x² ≥ 0.** Critical point x = 0 (f′(0) = 0). But f′ > 0 on **both** sides
   (3x² is positive for any x ≠ 0) ⇒ the sign doesn't change ⇒ **neither max nor min**.
   f is increasing on all of ℝ: it pauses flat for an instant at 0, then keeps climbing.
5. **f″ = 6x:** negative for x < 0 (∩), positive for x > 0 (∪). The sign flips ⇒
   **inflection at (0, 0)**.
6. Odd: (−x)³ = −x³.
7. Shows that "gradient = 0" doesn't guarantee a minimum. In higher
   dimensions this becomes a saddle point.

**Why f′(0) = 0 isn't an extremum (write this):** a max needs the function to go up
then down (f′: + → −), and a min needs down then up (− → +). For x³, f′ is positive on
both sides of 0, so the curve rises into 0 and keeps rising out of it. Below 0 the
values are smaller and above 0 they're larger, so 0 is neither the highest nor the
lowest nearby. It's a **flat inflection point**.

**Sketch:** through (−1, −1), (0, 0), (1, 1); a horizontal tangent stroke at the origin;
∩ on the left and ∪ on the right. → `plots/A3_02_x3.png`

---

## A3.3  f(x) = |x|   (L1 loss, Lasso. What happens to f′ at 0?)

Piecewise: |x| = −x for x < 0, and x for x ≥ 0.

1. **Domain / range:** ℝ / [0, ∞)
2. **Special values:** f(0) = 0, the only zero. f(±1) = 1.
3. **Ends:** → +∞ on both sides (along the lines y = −x and y = x). No asymptotes.
4. **f′ = −1 for x < 0, +1 for x > 0.** At 0: left slope −1 ≠ right slope +1 ⇒
   **f′(0) DNE (corner)**. x = 0 is a critical point (f′ DNE), and f′ goes − → +
   ⇒ **global minimum at (0, 0)**. Decreasing on (−∞, 0), increasing on (0, ∞).
5. **f″ = 0 for x ≠ 0** (straight pieces); **f″(0) DNE**. Concavity doesn't change
   (lines on both sides, slope only increases) ⇒ **no inflection**.
6. Even: |−x| = |x|.
7. L1 / absolute-error loss and the Lasso penalty.

**What happens to f′ at 0:** it jumps from −1 to +1, so the derivative doesn't exist
(a V-shaped corner). In ML the gradient doesn't shrink as you approach 0 the way x²'s
does (2x → 0). The constant pull of size 1 is what pushes Lasso weights to **exactly**
zero.

**Sketch:** a V with its vertex at (0, 0), arms of slope ±1. → `plots/A3_03_abs.png`

---

## A3.4  f(x) = 1/x   (decreasing on each piece, but on the whole domain?)

1. **Domain / range:** x ≠ 0, i.e. (−∞, 0) ∪ (0, ∞) / y ≠ 0, the same set.
2. **Special values:** **no intercepts** (x = 0 not allowed; 1/x is never 0).
   f(1) = 1, f(−1) = −1, f(2) = ½.
3. **Ends:** x → ±∞: 1/x → 0 ⇒ **horizontal asymptote y = 0**.
   x → 0⁺: +∞; x → 0⁻: −∞ ⇒ **vertical asymptote x = 0**.
4. **f′ = −1/x² < 0** for every x in the domain ⇒ **decreasing on (−∞, 0) and
   decreasing on (0, ∞)**. f′ is never 0, and x = 0 isn't in the domain ⇒ **no critical
   points, no max/min**.
5. **f″ = 2/x³:** x < 0 → negative (∩); x > 0 → positive (∪). The concavity differs on
   the two pieces, but **no inflection point**, because the change happens at x = 0,
   which isn't in the domain. There's no point on the graph where it switches.
6. Odd: 1/(−x) = −1/x.

**Decreasing over the whole domain? NO.** Take −1 < 1. If f were decreasing on the
whole domain we'd need f(−1) > f(1). But f(−1) = −1 < 1 = f(1). The function *jumps
up* across the gap at x = 0.

**Why it matters:** "f′ < 0 ⇒ decreasing" is only valid **on an interval** (a
connected stretch with no gaps). That's why the sheet says to analyse disconnected
domains interval by interval. Always state "decreasing on (−∞, 0) and on (0, ∞)
separately", never "decreasing on its domain".

**Sketch:** dashed axes as asymptotes; one branch in quadrant III through (−1, −1) and
one in quadrant I through (1, 1), each hugging both asymptotes. → `plots/A3_04_reciprocal.png`

---

## A3.5  f(x) = √x   (slope as x → 0⁺?)

1. **Domain / range:** [0, ∞) / [0, ∞)
2. **Special values:** f(0) = 0, the only zero. f(1) = 1, f(4) = 2.
3. **Ends:** x → ∞: √x → ∞ (slowly, no asymptote). Left edge: the curve starts at (0, 0).
4. **f′ = 1/(2√x)** for x > 0, which is > 0 ⇒ **increasing**. At x = 0, f′ DNE
   (division by 0). No critical points inside (0, ∞). Check the **endpoint** x = 0:
   f(0) = 0 is the smallest value ⇒ **global minimum at (0, 0), at the boundary**. No max.
5. **f″ = −1/(4x^(3/2)) < 0** for x > 0 ⇒ concave down, no inflection.
6. Neither (the domain isn't symmetric).
7. Standard deviation = √variance; RMSE = √MSE.

**Slope as x → 0⁺:** f′ = 1/(2√x) → **+∞**. The curve leaves the origin heading
**straight up**, so **the tangent at the origin is vertical** (the line x = 0). That's
why f′(0) doesn't exist as a number: a vertical line has no finite slope.

**Sketch:** start at (0, 0) going vertically, bend over (∩) through (1, 1) and (4, 2). → `plots/A3_05_sqrt.png`

---

## A3.6  f(x) = e^(−x²)   (Gaussian bell: max and both inflections)

1. **Domain / range:** ℝ / (0, 1]   (max 1 attained, never reaches 0)
2. **Special values:** f(0) = e⁰ = **1**. **No zeros** (e^anything > 0).
3. **Ends:** x → ±∞: −x² → −∞, so e^(−x²) → 0 ⇒ **horizontal asymptote y = 0 on both sides**.
4. **f′ = −2x e^(−x²)** (chain rule: inside −x² has derivative −2x).
   e^(−x²) > 0, so the sign of f′ is the sign of −2x: **x < 0 → increasing, x > 0 →
   decreasing**. Critical point x = 0, with f′ going + → − ⇒ **global maximum at (0, 1)**.
5. **f″** (product rule on (−2x)·e^(−x²)):

       f″ = (−2)·e^(−x²) + (−2x)·(−2x e^(−x²))
          = e^(−x²) (4x² − 2)

   f″ = 0 ⇔ 4x² = 2 ⇔ **x = ±1/√2 ≈ ±0.707**.
   Test the sign of (4x² − 2): at x = 0 it's −2 (∩); at x = 2 it's 14 (∪).
   **Concave down on (−1/√2, 1/√2); concave up for |x| > 1/√2.** The sign flips at both
   ⇒ **inflections at (±1/√2, e^(−1/2)) ≈ (±0.71, 0.61)**.
6. Even: e^(−(−x)²) = e^(−x²).
7. The shape of the Gaussian (normal) density, minus the 1/√(2π) constant.

**Sketch:** dashed y = 0; peak (0, 1); inflection dots at (±0.71, 0.61); ∩ between them,
∪ outside, tails flattening into y = 0. → `plots/A3_06_gauss.png`

---

## A3.7  softplus(x) = ln(1 + eˣ)   (smooth ReLU: two asymptotes)

1. **Domain / range:** ℝ / (0, ∞)   (1 + eˣ > 1 so ln(·) > 0)
2. **Special values:** f(0) = ln(1 + 1) = **ln 2 ≈ 0.69**. **No zeros.**
3. **Ends:**
   - x → −∞: eˣ → 0, so f → ln 1 = 0 ⇒ **horizontal asymptote y = 0**.
   - x → +∞: factor out eˣ:
     ln(1 + eˣ) = ln(eˣ(e⁻ˣ + 1)) = **x + ln(1 + e⁻ˣ)**.
     The second piece → ln 1 = 0, so f(x) − x → 0 ⇒ **oblique asymptote y = x**.
4. **f′ = eˣ/(1 + eˣ) = σ(x)** (proof in A4.3). This lies in (0, 1), so it's > 0 ⇒
   **increasing**, no critical points, no max/min.
5. **f″ = σ′(x) = σ(x)(1 − σ(x)) > 0** ⇒ **concave up everywhere**, no inflection.
6. Neither. *(Bonus fact: f(x) − f(−x) = x.)*
7. A smooth, differentiable-everywhere version of ReLU.

**Sketch:** dashed y = 0 (left) and dashed y = x (right); point (0, 0.69); the curve rises
from y = 0, bends up, and merges with y = x. It stays **above** both asymptotes
(and above ReLU). → `plots/A3_07_softplus.png`

---

## A3.8  Leaky ReLU: f(x) = x if x > 0, 0.1x if x ≤ 0

1. **Domain / range:** ℝ / ℝ   (the left piece 0.1x reaches every negative number)
2. **Special values:** f(0) = 0, the only zero. f(1) = 1, f(−1) = −0.1, f(−10) = −1.
3. **Ends:** x → +∞: +∞; x → −∞: −∞ (slowly, slope 0.1). No asymptotes; each side is a line.
4. **f′ = 0.1 for x < 0, 1 for x > 0.** At 0: left slope 0.1 ≠ right slope 1 ⇒
   **f′(0) DNE**. f′ > 0 on both sides ⇒ **strictly increasing on ℝ**. x = 0 is a
   critical point (f′ DNE), but f′ is + on both sides ⇒ **neither max nor min**.
5. **f″ = 0 for x ≠ 0, DNE at 0.** Both sides are lines and the slope only increases
   (0.1 → 1) ⇒ concavity doesn't change ⇒ **no inflection** (a corner).
6. Neither: f(−1) = −0.1 but −f(1) = −1.
7. Fixes "dying ReLU": negative inputs still pass gradient 0.1 instead of 0.

**Differentiable at 0? NO.** Write it out:
left-hand slope = lim (h → 0⁻) (0.1h − 0)/h = 0.1;
right-hand slope = lim (h → 0⁺) (h − 0)/h = 1.
0.1 ≠ 1 ⇒ no single tangent ⇒ not differentiable (a corner). It is still
*continuous* (both pieces meet at 0). In practice libraries just pick a slope there.

**Sketch:** a gentle line (slope 0.1) on the left, a 45° line on the right, a corner dot at (0, 0). → `plots/A3_08_leaky.png`

---

## A3.9  f(p) = −ln p, for 0 < p ≤ 1   (negative log-likelihood)

1. **Domain / range:** (0, 1] / [0, ∞)
2. **Special values:** f(1) = −ln 1 = **0**, the only zero (at the right endpoint). f(0.5) = ln 2 ≈ 0.69, f(0.1) ≈ 2.30.
3. **Ends:** p → 0⁺: ln p → −∞, so −ln p → **+∞** ⇒ **vertical asymptote p = 0**.
   Right edge: p = 1 gives 0 (filled dot).
4. **f′ = −1/p < 0** ⇒ **decreasing** on (0, 1]. Never 0 ⇒ no critical points inside.
   Check the **endpoint p = 1**: f = 0, and every other value is > 0 ⇒ **global minimum
   (1, 0) at the boundary** (even though f′(1) = −1 ≠ 0). No max (unbounded as p → 0).
5. **f″ = 1/p² > 0** ⇒ **concave up**, no inflection.
6. Neither (the domain isn't symmetric).
7. Cross-entropy / NLL loss: the penalty for giving probability p to the true class.

**What happens as p → 0:** the loss → ∞. A model that's **confidently wrong** (gives
near-zero probability to the correct class) is punished without limit.
**Where is the minimum:** at p = 1 (perfectly confident and correct), with loss 0.

**Sketch:** dashed p = 0; the curve comes down from +∞ near the asymptote, bends (∪),
and ends at a filled dot (1, 0). → `plots/A3_09_nll.png`

---

## A3.10  f(x) = x ln x, for x > 0   (entropy building block)

1. **Domain / range:** (0, ∞) / [−1/e, ∞)   (−1/e from the minimum below)
2. **Special values:** zero when ln x = 0 ⇒ **x = 1**. (x = 0 isn't in the domain.)
3. **Ends:**
   - x → ∞: x → ∞ and ln x → ∞ ⇒ f → ∞.
   - **x → 0⁺** looks like 0 · (−∞), which is undecided. Rewrite it as a fraction and use
     L'Hôpital:

         lim x ln x = lim  ln x / (1/x)          (now −∞ / ∞)
                    = lim  (1/x) / (−1/x²)        (differentiate top and bottom)
                    = lim  −x  = 0

     **lim (x → 0⁺) x ln x = 0.** The curve heads toward the point (0, 0), but that
     point isn't included (open circle).
4. **f′ = ln x + 1** (product rule: 1·ln x + x·(1/x)).
   f′ = 0 ⇔ ln x = −1 ⇔ **x = e⁻¹ = 1/e ≈ 0.368**.
   x < 1/e → f′ < 0 (decreasing); x > 1/e → f′ > 0 (increasing) ⇒ **global minimum
   f(1/e) = (1/e)·(−1) = −1/e ≈ −0.368**.
5. **f″ = 1/x > 0** ⇒ **concave up**, no inflection.
6. Neither (the domain isn't symmetric).
7. Entropy H = −Σ p ln p uses exactly this function (with the convention 0 ln 0 = 0).

**Why the limit exists even though ln x → −∞:** it's a tug-of-war between x → 0
(pulling the product to 0) and ln x → −∞ (pulling it to −∞). x wins, because ln x
diverges **far more slowly** than x shrinks. Numbers: x = 0.001 gives
0.001 × (−6.9) = −0.0069, and x = 10⁻⁶ gives 10⁻⁶ × (−13.8) ≈ −0.0000138. That's why
entropy can safely define 0·ln 0 = 0.

**Sketch:** open circle at (0, 0); dip down to the min (0.37, −0.37); back up through
(1, 0); then up. ∪ throughout. → `plots/A3_10_xlnx.png`
