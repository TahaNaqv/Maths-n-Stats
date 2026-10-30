# Module 5 — Multivariable Calculus Assignment · Part A

**Name:** ____________  **Roll No:** ____________  **Date:** 20 October 2026

> ✏️ = draw this sketch by hand at that spot. Matching reference graphs are in `plots/`.
> Label every asymptote (dashed), intercept and special point with its coordinates.

---

## A1. Recognize [8]

| Plot | Formula | Distinguishing feature |
|---|---|---|
| 1 | (g) ln(1+eˣ) | Value at x = 0 is ≈ 0.69 = ln 2 (not 0, so not ReLU); smooth, → 0 on left, grows ≈ x on right (≈ 5 at x = 5). |
| 2 | (i) σ′(x) | Bell with maximum height 0.25 at x = 0, since σ′(0) = ¼. (e^(−x²) would peak at 1.) |
| 3 | (c) −ln x | Defined only for x > 0, zero at x = 1, decreasing, → +∞ as x → 0⁺. (ln x would be increasing.) |
| 4 | (e) tanh x | S-curve through (0, 0) with range (−1, 1), flattening at y = ±1. |
| 5 | (a) eˣ | Passes through (0, 1); value ≈ 7.39 = e² at x = 2; always positive, → 0 on left. |
| 6 | (h) e^(−x²) | Bell with maximum height 1 at x = 0 (e⁰ = 1). |
| 7 | (j) x³ | Negative for x < 0 (≈ −8 at x = −2, 8 at x = 2), flat at origin, odd symmetry. |
| 8 | (d) σ(x) | S-curve with range (0, 1) and value 0.5 at x = 0. |

Unused: (b) ln x and (f) ReLU(x).

---

## A2. The ML function zoo [8]

### A2.1  f(x) = eˣ

1. **Domain / range:** ℝ / (0, ∞)
2. **Special values:** f(0) = 1; f(1) = e ≈ 2.72; no zeros since eˣ > 0.
3. **Ends:** x → −∞: eˣ → 0 ⇒ horizontal asymptote y = 0. x → +∞: eˣ → ∞.
4. **f′(x) = eˣ > 0** ⇒ increasing everywhere; f′ ≠ 0 and always exists ⇒ no critical points, no extrema. Slope at 0 is 1.
5. **f″(x) = eˣ > 0** ⇒ concave up everywhere; no inflection points.
6. **Symmetry:** f(−x) = 1/eˣ ≠ ±eˣ ⇒ neither.
7. **In ML:** makes scores positive; used in softmax, sigmoid and likelihoods.

✏️ Dashed y = 0 on the left; point (0, 1) with slope-1 tangent; point (1, e); concave-up curve rising steeply.

### A2.2  f(x) = ln x

1. **Domain / range:** (0, ∞) / ℝ
2. **Special values:** no y-intercept; zero at x = 1 (ln 1 = 0); ln e = 1.
3. **Ends:** x → 0⁺: ln x → −∞ ⇒ vertical asymptote x = 0. x → ∞: ln x → ∞ slowly (no horizontal asymptote).
4. **f′(x) = 1/x > 0** for x > 0 ⇒ increasing; no critical points, no extrema.
5. **f″(x) = −1/x² < 0** ⇒ concave down everywhere; no inflection.
6. **Symmetry:** domain not symmetric ⇒ neither even nor odd.
7. **In ML:** log-likelihood / cross-entropy; turns products of probabilities into sums.

✏️ Dashed x = 0; point (1, 0) with slope-1 tangent; point (e, 1); curve rises from −∞ near the y-axis, concave down.

### A2.3  f(x) = tanh x = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ)

1. **Domain / range:** ℝ / (−1, 1)
2. **Special values:** tanh 0 = (1 − 1)/(1 + 1) = 0; only zero x = 0.
3. **Ends:** x → +∞: e⁻ˣ → 0 so tanh → 1. x → −∞: eˣ → 0 so tanh → −1. Horizontal asymptotes y = ±1.
4. **f′(x)** (quotient rule, with u = eˣ − e⁻ˣ, v = eˣ + e⁻ˣ, u′ = v, v′ = u):
   f′ = (v² − u²)/v² = 1 − tanh²x. Since |tanh x| < 1, f′ > 0 ⇒ increasing everywhere, no critical points. Steepest at x = 0 with slope 1.
5. **f″(x) = −2 tanh x (1 − tanh²x).** (1 − tanh²x) > 0, so sign of f″ = sign of −tanh x:
   x < 0 ⇒ f″ > 0 (concave up); x > 0 ⇒ f″ < 0 (concave down). Inflection at (0, 0).
6. **Symmetry:** tanh(−x) = (e⁻ˣ − eˣ)/(e⁻ˣ + eˣ) = −tanh x ⇒ odd.
7. **In ML:** zero-centred activation (RNNs/LSTMs).

✏️ Dashed y = 1 and y = −1; point (0, 0) with slope-1 tangent; concave up on left, concave down on right.

### A2.4  f(x) = ReLU(x) = max(0, x) = { 0 if x ≤ 0;  x if x > 0 }

1. **Domain / range:** ℝ / [0, ∞)
2. **Special values:** f(0) = 0; every x ≤ 0 is a zero.
3. **Ends:** x → −∞: f = 0. x → +∞: f = x → ∞.
4. **f′(x) = 0 for x < 0, 1 for x > 0.** At x = 0: left slope 0 ≠ right slope 1 ⇒ f′(0) does not exist. f is non-decreasing. Critical point x = 0 (f′ DNE). Minimum value 0, attained for all x ≤ 0; no maximum.
5. **f″(x) = 0 for x ≠ 0;** f″(0) does not exist (f′ jumps from 0 to 1).
6. **Symmetry:** ReLU(−1) = 0, ReLU(1) = 1 ⇒ neither.
7. **In ML:** default hidden-layer activation; gradient 1 for active units.

**At x = 0:** f′ does not exist (one-sided slopes 0 and 1 differ) and f″ does not exist. The point is a **corner**. It is **not an inflection point**: both sides are straight lines (f″ = 0), and the slope only increases from 0 to 1, so concavity never changes (ReLU is convex). **Corner only, not both.**

✏️ Flat line along the negative x-axis, corner dot at (0, 0), line of slope 1 to the right.

---

## A3. Beyond the zoo — chosen: A3.1, A3.2, A3.3, A3.4, A3.5, A3.9 [6]

### A3.1  f(x) = x²

1. Domain / range: ℝ / [0, ∞)
2. f(0) = 0, only zero; f(±1) = 1, f(±2) = 4.
3. x → ±∞: f → +∞; no asymptotes.
4. f′ = 2x: < 0 for x < 0 (decreasing), > 0 for x > 0 (increasing). Critical point x = 0, sign − → + ⇒ global minimum (0, 0).
5. f″ = 2 > 0 ⇒ concave up everywhere; no inflection.
6. Even: (−x)² = x². 7. Squared-error loss.

✏️ Parabola, vertex (0, 0), through (±1, 1), (±2, 4).

### A3.2  f(x) = x³

1. Domain / range: ℝ / ℝ
2. f(0) = 0, only zero; f(1) = 1, f(−1) = −1.
3. x → +∞: +∞; x → −∞: −∞; no asymptotes.
4. f′ = 3x² ≥ 0. Critical point x = 0 (f′(0) = 0). f′ > 0 on both sides of 0 ⇒ no sign change ⇒ **neither max nor min**; f is increasing on ℝ.
5. f″ = 6x: < 0 for x < 0 (concave down), > 0 for x > 0 (concave up) ⇒ inflection at (0, 0).
6. Odd: (−x)³ = −x³.

**Why f′(0) = 0 is not an extremum:** a max requires f′ to change + → −, a min − → +. Here f′ is positive on both sides, so f increases into and out of 0: values left of 0 are smaller and values right are larger. x = 0 is a flat (stationary) inflection point.

✏️ Through (−1, −1), (0, 0), (1, 1); horizontal tangent at origin; concave down left, concave up right.

### A3.3  f(x) = |x| = { −x if x < 0;  x if x ≥ 0 }

1. Domain / range: ℝ / [0, ∞)
2. f(0) = 0, only zero; f(±1) = 1.
3. x → ±∞: f → +∞; no asymptotes.
4. f′ = −1 for x < 0, +1 for x > 0. At 0: left slope −1 ≠ right slope +1 ⇒ f′(0) does not exist (corner). Critical point x = 0; sign − → + ⇒ global minimum (0, 0). Decreasing on (−∞, 0), increasing on (0, ∞).
5. f″ = 0 for x ≠ 0, DNE at 0; concavity does not change ⇒ no inflection.
6. Even: |−x| = |x|.

**f′ at 0:** jumps from −1 to +1, so the derivative does not exist. Unlike x² (gradient 2x → 0 near 0), |x| keeps a constant pull of size 1, which is why Lasso pushes weights exactly to zero.

✏️ V-shape, vertex (0, 0), slopes −1 and +1.

### A3.4  f(x) = 1/x

1. Domain: (−∞, 0) ∪ (0, ∞). Range: (−∞, 0) ∪ (0, ∞).
2. No intercepts (x = 0 not in domain; 1/x ≠ 0). f(1) = 1, f(−1) = −1.
3. x → ±∞: f → 0 ⇒ horizontal asymptote y = 0. x → 0⁺: +∞; x → 0⁻: −∞ ⇒ vertical asymptote x = 0.
4. f′ = −1/x² < 0 ⇒ decreasing on (−∞, 0) and decreasing on (0, ∞) separately. No critical points (f′ ≠ 0; x = 0 not in domain); no extrema.
5. f″ = 2/x³: < 0 for x < 0 (concave down), > 0 for x > 0 (concave up). No inflection point, because x = 0 is not in the domain.
6. Odd: 1/(−x) = −1/x.

**Decreasing on the whole domain? No.** −1 < 1 but f(−1) = −1 < f(1) = 1, so f increases across the gap. "f′ < 0 ⇒ decreasing" holds only on an interval; the domain is two disconnected intervals, so each must be analysed separately.

✏️ Dashed axes as asymptotes; branch in quadrant III through (−1, −1); branch in quadrant I through (1, 1).

### A3.5  f(x) = √x

1. Domain / range: [0, ∞) / [0, ∞)
2. f(0) = 0, only zero; f(1) = 1, f(4) = 2.
3. x → ∞: f → ∞ (slowly, no asymptote).
4. f′ = 1/(2√x) > 0 for x > 0 ⇒ increasing; f′(0) does not exist. No interior critical points. Endpoint x = 0: f(0) = 0 is the smallest value ⇒ global minimum (0, 0) at the boundary; no maximum.
5. f″ = −1/(4x^(3/2)) < 0 for x > 0 ⇒ concave down; no inflection.
6. Neither (domain not symmetric).

**Slope as x → 0⁺:** f′ = 1/(2√x) → +∞. The tangent at the origin is **vertical** (the line x = 0), so f′(0) has no finite value.

✏️ Start at (0, 0) going straight up, bend over through (1, 1) and (4, 2).

### A3.9  f(p) = −ln p, 0 < p ≤ 1

1. Domain / range: (0, 1] / [0, ∞)
2. f(1) = −ln 1 = 0, only zero; f(0.5) = ln 2 ≈ 0.69.
3. p → 0⁺: ln p → −∞ so −ln p → +∞ ⇒ vertical asymptote p = 0.
4. f′ = −1/p < 0 ⇒ decreasing on (0, 1]; no interior critical points. Endpoint p = 1: f(1) = 0 and f > 0 elsewhere ⇒ global minimum (1, 0) at the boundary (even though f′(1) = −1 ≠ 0). No maximum.
5. f″ = 1/p² > 0 ⇒ concave up; no inflection.
6. Neither (domain not symmetric).

**As p → 0:** loss → +∞, so a confident wrong prediction is penalised without bound. **Minimum:** at p = 1 (correct class predicted with certainty), loss 0.

✏️ Dashed p = 0; curve falls from +∞ near the axis, concave up, through (0.5, 0.69), ending at filled dot (1, 0).

---

## A4. Connections [3 + 1]

Facts used: σ(x) = 1/(1 + e⁻ˣ), σ(0) = ½, σ′(x) = σ(x)(1 − σ(x)), so σ′(0) = ½ · ½ = ¼.

### A4.1  σ(x), σ(2x), σ(x − 3)

The midpoint (y = ½) occurs where the input to σ is 0.

- **σ(x):** midpoint x = 0, i.e. (0, ½). Slope σ′(0) = ¼.
- **σ(2x):** 2x = 0 ⇒ midpoint (0, ½). d/dx σ(2x) = 2σ′(2x) ⇒ slope at 0 = 2 · ¼ = **½**. Horizontally squeezed by 2: twice as steep.
- **σ(x − 3):** x − 3 = 0 ⇒ midpoint (3, ½). d/dx σ(x − 3) = σ′(x − 3) ⇒ slope at 3 = σ′(0) = **¼**. Shifted right by 3, same steepness.

All three have asymptotes y = 0 and y = 1.

✏️ One set of axes: dashed y = 0, y = 1; the three S-curves with midpoints (0, ½), (0, ½) steeper, and (3, ½) labelled with their slopes.

### A4.2  tanh x = 2σ(2x) − 1

2σ(2x) − 1 = 2/(1 + e^(−2x)) − 1
= [2 − (1 + e^(−2x))] / (1 + e^(−2x))
= (1 − e^(−2x)) / (1 + e^(−2x))

Multiply numerator and denominator by eˣ:
= (eˣ − e⁻ˣ) / (eˣ + e⁻ˣ) = tanh x ∎

**In words:** start from σ: (i) σ(2x) squeezes it horizontally by 2; (ii) multiplying by 2 stretches it vertically, range (0, 1) → (0, 2); (iii) subtracting 1 shifts it down, range → (−1, 1) and midpoint (0, ½) → (0, 0). The result is tanh: a rescaled, re-centred sigmoid with slope 1 at the origin.

### A4.3  d/dx ln(1 + eˣ) = σ(x)

By the chain rule: d/dx ln(1 + eˣ) = [1/(1 + eˣ)] · eˣ = eˣ/(1 + eˣ).
Multiply numerator and denominator by e⁻ˣ: = 1/(e⁻ˣ + 1) = σ(x) ∎

**Meaning:** the slope of softplus is σ(x) ∈ (0, 1). Far left (x → −∞), σ → 0: softplus is flat, like ReLU's slope 0. Far right (x → +∞), σ → 1: slope 1, like ReLU's slope 1 (softplus approaches the line y = x). In between, the slope changes smoothly instead of jumping at a corner.

### A4.4  Bonus

Differentiate tanh x = 2σ(2x) − 1 using the chain rule:
tanh′(x) = 2 · σ′(2x) · 2 = **4σ′(2x)** ∎

At x = 0: σ′(0) = σ(0)(1 − σ(0)) = ½ · ½ = **¼**, so tanh′(0) = 4 · ¼ = **1**.

**Gradient flow:** in backpropagation the gradient is multiplied by each activation's derivative. With inputs near 0, each sigmoid multiplies it by about ¼, so after n layers it is scaled by (¼)ⁿ (e.g. n = 5: 1/1024 ≈ 0.001), shrinking exponentially. Each tanh multiplies by about 1, so the gradient is preserved: 1ⁿ = 1. Therefore **tanh is less likely to make the gradient shrink rapidly**, because its slope at zero is 1 while the sigmoid's is only ¼.

---

*AI disclosure: ____________________________________________*
