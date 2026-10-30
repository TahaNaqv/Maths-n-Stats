# Lesson 1 — The Calculus Toolkit (from zero)

The whole assignment uses only the tools below. Learn them in order. Each one ends
with a mini-check. Answers are in brackets, so cover them first.

---

## Tool 1 — Function, domain, range

A **function** is a machine: put in x, get out one number f(x).

- **Domain**: the x values you're *allowed* to put in.
  - `ln x` needs x > 0 (no log of zero or negatives) → domain (0, ∞)
  - `1/x` can't divide by zero → domain: every x except 0
  - `√x` needs x ≥ 0 → domain [0, ∞)
  - `eˣ`, `x²`, `tanh x`: anything goes → domain ℝ (all real numbers)
- **Range**: the y values that actually come *out*.
  - `eˣ` is always positive, and every positive number does come out, so range = (0, ∞)
  - `x²` is never negative → range [0, ∞)

**Bracket notation:** `(` means the endpoint is *not included* and `[` means it *is*.
`(0, 1)` = strictly between 0 and 1. `[0, ∞)` = 0 and everything above it. ∞ always
gets a round bracket.

Mini-check: what is the domain of −ln p? [p > 0, i.e. (0, ∞). The assignment then
restricts it further to (0, 1].]

---

## Tool 2 — The three special functions you must know cold

### eˣ (the exponential), with e ≈ 2.718

    e⁰ = 1        e¹ ≈ 2.72      e² ≈ 7.39      e⁻¹ ≈ 0.37
    eᵃ · eᵇ = eᵃ⁺ᵇ       e⁻ᵃ = 1/eᵃ        eˣ > 0 ALWAYS

As x → −∞, eˣ → 0 (e⁻¹⁰⁰ = 1/e¹⁰⁰ is tiny). As x → +∞, eˣ explodes.

### ln x (natural log): the *undo* button for eˣ

    ln(eˣ) = x        e^(ln x) = x
    ln 1 = 0          ln e = 1           ln 2 ≈ 0.69
    ln(ab) = ln a + ln b      ln(a/b) = ln a − ln b     ln(1/a) = −ln a

As x → 0⁺ (from the right), ln x → −∞. As x → ∞, ln x → ∞ but *very slowly*
(ln 1,000,000 ≈ 13.8).

### Hyperbolic tangent

    tanh x = (eˣ − e⁻ˣ) / (eˣ + e⁻ˣ)

Big positive x: e⁻ˣ ≈ 0, so tanh ≈ eˣ/eˣ = 1. Big negative x: eˣ ≈ 0, so
tanh ≈ −e⁻ˣ/e⁻ˣ = −1. At 0: (1−1)/(1+1) = 0.

### Sigmoid (already worked in the sheet)

    σ(x) = 1 / (1 + e⁻ˣ)      σ(0) = 1/2      range (0, 1)

Mini-check: ln(e³) = ? [3] · tanh(0) = ? [0] · σ(0) = ? [1/2]

---

## Tool 3 — Limits and asymptotes ("what happens at the ends")

`lim f(x) as x → a` means "the value f(x) gets closer and closer to as x approaches a".

**Horizontal asymptote** y = L: the curve flattens out towards height L as x → ±∞.
- eˣ → 0 as x → −∞ ⇒ HA **y = 0** on the left.
- σ(x) → 0 on the left and → 1 on the right ⇒ two HAs.

**Vertical asymptote** x = a: the curve shoots to ±∞ as x approaches a.
- ln x → −∞ as x → 0⁺ ⇒ VA **x = 0**.
- 1/x: 1/0.001 = 1000, 1/(−0.001) = −1000 ⇒ VA x = 0, blowing up in opposite directions.

**Oblique (slanted) asymptote** y = mx + c: the curve hugs a tilted line.
Softplus does this with y = x (see A3.7).

**How to compute a limit by hand:** plug in a large number (or a tiny one) and see
what each piece does. The rule of thumb is that **exponentials beat powers, and powers
beat logs**:

    as x → ∞:   ln x  ≪  x  ≪  x²  ≪  eˣ
    as x → 0⁺:  x · ln x → 0     (x shrinks to 0 faster than ln x runs to −∞)

**L'Hôpital's rule** (needed once, in A3.10). If a limit looks like ∞/∞ or 0/0, you
may differentiate top and bottom separately and try again:

    lim f/g = lim f′/g′

Mini-check: lim (x → −∞) e^(−x²) = ? [0] · lim (x → ∞) 1/x = ? [0]

---

## Tool 4 — The derivative = slope

`f′(x)` is the **slope** of the curve at x: how fast f rises per unit step right.

- f′ > 0 → curve going **up** (increasing)
- f′ < 0 → curve going **down** (decreasing)
- f′ = 0 → **flat** for an instant (a candidate peak, valley or flat step)

### The derivative rules you need (all of them)

| Rule | Formula | Example |
|---|---|---|
| Constant | (c)′ = 0 | (5)′ = 0 |
| Power | (xⁿ)′ = n xⁿ⁻¹ | (x³)′ = 3x² ; (√x)′ = (x^½)′ = ½x^(−½) = 1/(2√x) ; (1/x)′ = (x⁻¹)′ = −x⁻² |
| Exponential | (eˣ)′ = eˣ | it is its own slope |
| Log | (ln x)′ = 1/x | |
| Constant multiple | (c·f)′ = c·f′ | (0.1x)′ = 0.1 |
| Sum | (f + g)′ = f′ + g′ | |
| **Product** | (f·g)′ = f′g + fg′ | (x ln x)′ = 1·ln x + x·(1/x) = ln x + 1 |
| **Quotient** | (f/g)′ = (f′g − fg′)/g² | |
| **Chain** | (f(g(x)))′ = f′(g(x)) · g′(x) | (e^(−x²))′ = e^(−x²) · (−2x) |

**The chain rule in words:** differentiate the outside function (leaving the inside
alone), then multiply by the derivative of the inside. You'll use it everywhere:

    (ln(1 + eˣ))′ = 1/(1 + eˣ) · eˣ          outside ln(·) → 1/(·);  inside 1+eˣ → eˣ
    (σ(2x))′      = σ′(2x) · 2                outside σ(·) → σ′(·);   inside 2x → 2

### Two derivatives worth memorising
- **σ′(x) = σ(x)(1 − σ(x))**, which is 1/4 at x = 0 (the sheet gives it).
- **tanh′(x) = 1 − tanh²(x)**, which is 1 at x = 0.

  *Derivation (quotient rule):* top u = eˣ − e⁻ˣ, bottom v = eˣ + e⁻ˣ. Note u′ = v
  and v′ = u. So tanh′ = (v·v − u·u)/v² = 1 − (u/v)² = 1 − tanh².

### When the derivative does NOT exist
At a **corner** (sharp point) like |x| at 0, the slope from the left (−1) and from the
right (+1) disagree. Then f′(0) **does not exist (DNE)**. Always compute both
one-sided slopes and compare them.

Mini-check: (x²)′ = ? [2x] · (e^(3x))′ = ? [3e^(3x)] · (ln(2x))′ = ? [(1/(2x))·2 = 1/x]

---

## Tool 5 — Critical points: is it a max, min, or neither?

A **critical point** is an x *inside the domain* where f′(x) = 0 or f′ DNE.

**First-derivative test:** check the sign of f′ just left and just right.

| f′ left → right | Verdict |
|---|---|
| + → − | local **max** (up then down) |
| − → + | local **min** (down then up) |
| same sign both sides | **neither** (e.g. x³ at 0: up, flat, up) |

**Endpoints** (like x = 0 for √x, or p = 1 for −ln p) can hold the max or min even
when f′ ≠ 0 there, so always check them separately. The sheet explicitly asks for this.

Mini-check: f′ = 3x² at x = 0. Sign left? [+] right? [+] So x = 0 is... [neither]

---

## Tool 6 — Second derivative = concavity (the bend)

f″ is the derivative of f′. It tells you which way the curve **bends**.

- f″ > 0 → **concave up** ∪ (holds water; the slope is increasing)
- f″ < 0 → **concave down** ∩ (spills water; the slope is decreasing)
- **Inflection point**: a point *in the domain* where the concavity **changes**
  (∪ → ∩ or ∩ → ∪). Find candidates where f″ = 0 or f″ DNE, then **check that the
  sign actually flips**. f″ = 0 by itself is not enough.

Straight lines have f″ = 0: they bend neither way.

Mini-check: f″ = 6x. Concave up where? [x > 0] Inflection at? [x = 0, since the sign flips]

---

## Tool 7 — Symmetry

Test by plugging in −x:
- **Even**: f(−x) = f(x). Mirror image across the y-axis. Examples: x², |x|, e^(−x²).
- **Odd**: f(−x) = −f(x). Spin 180° about the origin. Examples: x³, 1/x, tanh x.
- **Neither**: most functions. Examples: eˣ, ln x, ReLU.

If the domain itself isn't symmetric (ln x lives only on x > 0), the function
**can't** be even or odd. Say exactly that; it's a full answer.

Mini-check: tanh(−x) = (e⁻ˣ − eˣ)/(e⁻ˣ + eˣ) = ? [−tanh x, so odd]

---

## How to turn the checklist into a sketch (every time)

1. Draw axes. Draw the **asymptotes dashed** first.
2. Plot the **special points** (intercepts, max/min, inflections) with their coordinates
   written next to them.
3. Add a **short tangent stroke** at key points if you know the slope (e.g. slope 1/4 at σ's middle).
4. Connect the dots, respecting: up/down from f′, ∪/∩ from f″, and approaching the asymptotes.
5. Mark open circles ○ for excluded points and filled ● for included ones.

The marks are for **features** (asymptotes, intercepts, monotonicity, concavity,
extrema), not neatness. So label everything.
