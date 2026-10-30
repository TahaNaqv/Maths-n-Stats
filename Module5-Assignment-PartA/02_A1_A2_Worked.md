# A1 + A2 — Worked Step by Step

Reference plots are in `plots/`. Open them **after** you've drawn your own.

---

# A1. Recognize [8 marks]

**The method:** don't match on shape ("it's S-shaped"). Read the **axis numbers** and
check one hard fact per plot: the value at 0, the max height, the range, or the domain.

First, the fingerprints of the ten candidates:

| Formula | Value at x=0 | Range / limits | Fingerprint |
|---|---|---|---|
| (a) eˣ | 1 | (0, ∞) | passes through (0,1); e² ≈ 7.39 |
| (b) ln x | undefined | ℝ, only x > 0 | zero at x=1, **increasing** |
| (c) −ln x | undefined | ℝ, only x > 0 | zero at x=1, **decreasing**, blows up at 0⁺ |
| (d) σ(x) | 0.5 | (0, 1) | S-curve between 0 and 1 |
| (e) tanh x | 0 | (−1, 1) | S-curve between −1 and 1 |
| (f) ReLU | 0 | [0, ∞) | sharp corner at 0, flat zero on the left |
| (g) ln(1+eˣ) | ln 2 ≈ 0.69 | (0, ∞) | smooth ReLU, ≈ x on the right |
| (h) e^(−x²) | 1 | (0, 1] | bell with peak **1** |
| (i) σ′(x) | 0.25 | (0, 0.25] | bell with peak **0.25** |
| (j) x³ | 0 | ℝ | flat at 0, negative on the left |

### Answers

| Plot | Formula | Distinguishing feature (write this) |
|---|---|---|
| 1 | **(g) ln(1+eˣ)** | At x = 0 the value is ≈ 0.69 = ln 2, not 0, and the curve is smooth with no corner (so it isn't ReLU). Approaches 0 on the left and grows like y = x on the right (≈5 at x=5). |
| 2 | **(i) σ′(x)** | Symmetric bell whose **maximum height is 0.25** at x = 0, and σ′(0) = ¼. The bell e^(−x²) peaks at 1, so this can't be it. |
| 3 | **(c) −ln x** | Defined only for x > 0, crosses zero at **x = 1**, **decreasing**, and → +∞ as x → 0⁺. ln x would be increasing. |
| 4 | **(e) tanh x** | S-shape with range **(−1, 1)**: passes through (0, 0), flattens at y = ±1. σ would go 0 → 1. |
| 5 | **(a) eˣ** | Passes through **(0, 1)**, value ≈ 7.4 = e² at x = 2, → 0 on the left, always positive. |
| 6 | **(h) e^(−x²)** | Bell with **max height 1** at x = 0, since e⁰ = 1. Distinguishes it from σ′ (peak 0.25). |
| 7 | **(j) x³** | Takes **negative** values (≈ −8 at x = −2, +8 at x = 2) and is flat at the origin (f′(0) = 0). Odd symmetry. |
| 8 | **(d) σ(x)** | S-shape with range **(0, 1)**, value **0.5 at x = 0**. tanh would be 0 at 0 and go to −1. |

**Unused: (b) ln x and (f) ReLU.**

> Why the tricky pairs are tricky: Plots 4 and 8 are both S-curves, and Plots 2 and 6
> are both bells. The **y-axis numbers** separate them. That's exactly what the "read
> the axis numbers" warning is about.

---

# A2. The ML function zoo [8 marks, 2 each]

Each gets: ½ for domain/range/intercepts/limits, ½ for derivatives/monotonicity/
extrema/concavity/symmetry, and 1 for the sketch. Lay each one out as a table like the
sigmoid example.

---

## A2.1  f(x) = eˣ

| Item | Answer |
|---|---|
| Domain / range | ℝ / (0, ∞) |
| Special values | f(0) = e⁰ = **1** (y-intercept); f(1) = e ≈ 2.72. **No zeros**, because eˣ > 0 always. |
| Ends | x → −∞: eˣ → 0 ⇒ **horizontal asymptote y = 0** (left only). x → +∞: eˣ → ∞ (no asymptote; grows faster than any power). |
| f′ | f′(x) = eˣ > 0 ⇒ **increasing everywhere**. f′ is never 0 and always exists ⇒ **no critical points, no max/min**. Slope at 0 is 1. |
| f″ | f″(x) = eˣ > 0 ⇒ **concave up everywhere**, **no inflection points**. |
| Symmetry | f(−x) = e⁻ˣ = 1/eˣ, which is neither eˣ nor −eˣ ⇒ **neither**. |
| In ML | Turns any score into a positive number: the heart of softmax, the sigmoid, and exponential-family likelihoods. |

**Sketch:** dashed y = 0 on the left; point (0, 1) with a tangent stroke of slope 1;
point (1, e); the curve hugs y = 0 on the left, bends upward (∪), and shoots up on the
right. → `plots/A2_1_exp.png`

---

## A2.2  f(x) = ln x

| Item | Answer |
|---|---|
| Domain / range | (0, ∞) / ℝ |
| Special values | **No y-intercept** (0 not in domain). Zero at **x = 1** since ln 1 = 0. Also ln e = 1. |
| Ends | x → 0⁺: ln x → −∞ ⇒ **vertical asymptote x = 0**. x → ∞: ln x → ∞ (slowly; **no** horizontal asymptote). |
| f′ | f′(x) = 1/x > 0 for all x > 0 ⇒ **increasing** on the whole domain. Never 0 ⇒ **no critical points**, no max/min (the domain is open, so no endpoints either). Slope at x = 1 is 1. |
| f″ | f″(x) = −1/x² < 0 ⇒ **concave down everywhere**, **no inflection**. |
| Symmetry | Domain isn't symmetric (−x isn't allowed) ⇒ **neither** even nor odd. |
| In ML | Log-likelihood and cross-entropy: ln turns products of probabilities into sums, and it's increasing, so maximizing ln L = maximizing L. |

**Sketch:** dashed x = 0; point (1, 0) with a slope-1 tangent stroke; point (e, 1);
the curve plunges down the asymptote near 0 and rises slowly with a ∩ bend.
→ `plots/A2_2_ln.png`

> Tip: ln x is the mirror image of eˣ across the line y = x (they undo each other).

---

## A2.3  f(x) = tanh x = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ)

| Item | Answer |
|---|---|
| Domain / range | ℝ / (−1, 1) |
| Special values | tanh 0 = (1−1)/(1+1) = **0**; the **only zero** is x = 0 (passes through the origin). |
| Ends | x → +∞: e⁻ˣ → 0, tanh → eˣ/eˣ = **1**. x → −∞: eˣ → 0, tanh → −e⁻ˣ/e⁻ˣ = **−1**. Two **horizontal asymptotes y = ±1**. |
| f′ | f′(x) = 1 − tanh²x (derivation in Lesson 1, Tool 4). Since −1 < tanh < 1, tanh² < 1, so f′ > 0 ⇒ **increasing everywhere**, no critical points. **Steepest at 0, slope f′(0) = 1 − 0 = 1.** |
| f″ | Chain rule: f″ = −2 tanh x · tanh′x = −2 tanh x (1 − tanh²x). The factor (1 − tanh²) > 0, so the sign of f″ is the sign of −tanh x: **x < 0 → f″ > 0, concave up; x > 0 → f″ < 0, concave down.** Sign flips at 0 ⇒ **inflection at (0, 0)**. |
| Symmetry | tanh(−x) = (e⁻ˣ − eˣ)/(e⁻ˣ + eˣ) = −tanh x ⇒ **odd** (point-symmetric about the origin). |
| In ML | A zero-centred activation (outputs in (−1, 1)), used in RNNs/LSTMs. A rescaled sigmoid (see A4.2). |

**Sketch:** dashed y = 1 and y = −1; point (0, 0) with a slope-1 tangent stroke (along
y = x); ∪ on the left rising off y = −1, ∩ on the right flattening into y = 1.
→ `plots/A2_3_tanh.png`

---

## A2.4  f(x) = ReLU(x) = max(0, x)

First rewrite it piecewise: **f(x) = 0 if x ≤ 0, and x if x > 0.**

| Item | Answer |
|---|---|
| Domain / range | ℝ / [0, ∞) (0 is attained, so square bracket). |
| Special values | f(0) = 0. **Zeros: every x ≤ 0** (a whole half-line of zeros, not one point). |
| Ends | x → −∞: f = 0 (constant, so the curve *is* the line y = 0 there). x → +∞: f = x → ∞, and the curve *is* the line y = x. |
| f′ | x < 0: f′ = 0. x > 0: f′ = 1. **At x = 0: left slope 0 ≠ right slope 1 ⇒ f′(0) DNE.** f′ ≥ 0, so f is **non-decreasing** (flat on the left, increasing on the right). Critical point x = 0 (f′ DNE). Minimum value **0**, attained at every x ≤ 0 (a global min, not strict); no maximum. |
| f″ | f″ = 0 for x ≠ 0 (both pieces are straight lines); **f″(0) DNE** (because f′ jumps from 0 to 1). |
| Symmetry | ReLU(−1) = 0 but ReLU(1) = 1, which is neither equal nor opposite ⇒ **neither**. |
| In ML | The default hidden-layer activation: cheap, and its gradient is exactly 1 for active units (no shrinking). |

### The question: what happens at x = 0? Corner, inflection, or both?

- **First derivative:** does not exist. The one-sided slopes are 0 (left) and 1
  (right). They disagree, so the graph has a sharp bend.
- **Second derivative:** does not exist at 0 (f′ jumps). Everywhere else f″ = 0.
- **Corner: YES.** A corner is exactly a point where the left and right slopes differ.
- **Inflection: NO.** An inflection needs the concavity to **change** sign. Both sides
  are straight lines (f″ = 0 on each side), so there's no ∪ on one side and ∩ on the
  other. The slope goes 0 → 1, only ever *increasing*, which means ReLU bends upward
  (it's a convex function overall). Concavity never switches.
- **Answer: a corner, not an inflection point.** f″(0) DNE makes 0 a *candidate*, but
  the concavity doesn't change, so it fails the test.

**Sketch:** flat line on the negative x-axis, a filled dot at (0, 0) labelled "corner",
a 45° line (slope 1) to the right. → `plots/A2_4_relu.png`
