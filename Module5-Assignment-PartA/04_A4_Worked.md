# A4 — Connections, Worked Step by Step [3 marks + 1 bonus]

You need three facts about the sigmoid, all from the sheet's worked example:

    σ(x) = 1/(1 + e⁻ˣ)      σ(0) = ½      σ′(x) = σ(x)(1 − σ(x))      σ′(0) = ½·½ = ¼

---

## A4.1 Transformations [1]: σ(x), σ(2x), σ(x − 3) on one set of axes

**The midpoint** is where the output = ½. σ(stuff) = ½ exactly when stuff = 0.

| Curve | Midpoint: solve inside = 0 | Slope there (chain rule) |
|---|---|---|
| σ(x) | x = 0 | σ′(0)·1 = **¼** |
| σ(2x) | 2x = 0 ⇒ **x = 0** | d/dx σ(2x) = 2σ′(2x) ⇒ at x = 0: 2·¼ = **½** |
| σ(x − 3) | x − 3 = 0 ⇒ **x = 3** | d/dx σ(x−3) = σ′(x−3)·1 ⇒ at x = 3: σ′(0) = **¼** |

**In words:**
- **σ(2x)** = σ squeezed horizontally by a factor of 2. Same midpoint (0, ½), twice as
  steep (slope ½). It switches from 0 to 1 faster.
- **σ(x − 3)** = σ shifted **right by 3**. Midpoint (3, ½), same steepness (¼).
- All three keep the same asymptotes, y = 0 and y = 1.

**Sketch:** dashed y = 0, y = 1, and a light y = ½ line. Three S-curves: the original
through (0, ½); a steeper one through (0, ½); and a copy of the original slid over to
(3, ½). Label each midpoint and its slope. → `plots/A4_1_transforms.png`

*(ML link: in logistic regression σ(wx + b), the weight w sets the steepness and the bias
b shifts the midpoint to x = −b/w.)*

---

## A4.2 Two activations are one [1]: show tanh x = 2σ(2x) − 1

Start from the **right-hand side** and follow the hint.

    2σ(2x) − 1 = 2/(1 + e^(−2x)) − 1

**Step 1: a single fraction** (write 1 as (1 + e^(−2x))/(1 + e^(−2x))):

    = [2 − (1 + e^(−2x))] / (1 + e^(−2x))
    = (1 − e^(−2x)) / (1 + e^(−2x))

**Step 2: multiply top and bottom by eˣ** (using eˣ·e^(−2x) = e^(−x)):

    = (eˣ − e⁻ˣ) / (eˣ + e⁻ˣ)
    = tanh x   ∎

**In words: how the sketch of σ turns into tanh.** Three moves, applied to σ's graph:
1. **σ(2x):** squeeze horizontally by 2 (steeper; midpoint slope ¼ → ½).
2. **2σ(2x):** stretch vertically by 2. The range (0, 1) becomes (0, 2) and the slope
   ½ becomes 1.
3. **− 1:** shift down by 1. The range (0, 2) becomes (−1, 1) and the midpoint (0, ½)
   becomes (0, 0).

The result is an S-curve through the origin with slope 1, flattening at ±1: exactly tanh.
**tanh is a rescaled, re-centred sigmoid.**

---

## A4.3 Smooth ReLU, sigmoid slope [1]: show d/dx ln(1 + eˣ) = σ(x)

**Chain rule** (outside ln(u) → 1/u; inside u = 1 + eˣ → u′ = eˣ):

    d/dx ln(1 + eˣ) = 1/(1 + eˣ) · eˣ = eˣ/(1 + eˣ)

**Multiply top and bottom by e⁻ˣ:**

    = (eˣ·e⁻ˣ) / (e⁻ˣ + eˣ·e⁻ˣ) = 1/(e⁻ˣ + 1) = σ(x)   ∎

**What it says about softplus's slope:**
- **Far left** (x → −∞): σ(x) → 0. Softplus becomes **flat**, like ReLU's slope 0 for x < 0.
- **Far right** (x → +∞): σ(x) → 1. Softplus has **slope 1**, like ReLU's slope 1 for
  x > 0 (matching its asymptote y = x).
- In between, the slope moves **smoothly** from 0 to 1 (it's ½ at x = 0). ReLU's slope
  instead jumps from 0 to 1 at a corner. Softplus is a smoothed ReLU, and its derivative
  is the sigmoid.

---

## A4.4 Bonus (+1): activation slopes and gradient flow

**Show tanh′(x) = 4σ′(2x).** Differentiate both sides of A4.2, tanh x = 2σ(2x) − 1:

    tanh′(x) = 2 · σ′(2x) · 2      (chain rule: the inside 2x has derivative 2; the constant −1 → 0)
             = 4σ′(2x)   ∎

**At 0:**

    σ′(0) = σ(0)(1 − σ(0)) = ½ · ½ = ¼
    tanh′(0) = 4σ′(0) = 4 · ¼ = 1

**Gradient flow.** Backpropagation multiplies the gradient by each activation's
derivative as it passes back through the layers. With inputs near 0, each layer
multiplies by about:

| Activation | Factor per layer | After 5 layers | After 10 layers |
|---|---|---|---|
| sigmoid | ¼ | (¼)⁵ = 1/1024 ≈ 0.001 | (¼)¹⁰ ≈ 10⁻⁶ |
| tanh | 1 | 1⁵ = 1 | 1 |

**Answer: tanh is less likely to make the gradient shrink rapidly.** Its slope at 0
is 1, so the gradient passes through unchanged. The sigmoid's slope is at most ¼, so
each layer cuts the gradient to a quarter or less, and it shrinks exponentially with
depth (the *vanishing gradient* problem). Under the stated simplification (inputs near
zero), tanh preserves the gradient and sigmoid shrinks it.

*(As the sheet notes, this compares slopes near zero only. For large |x| both saturate
and their slopes → 0, which is part of why ReLU, with slope exactly 1 for x > 0, became the default.)*
