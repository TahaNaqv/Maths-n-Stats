"""Reference plots for Module 5 Assignment Part A.
Run:  python3 make_plots.py   -> writes PNGs into ./plots/
Use these ONLY to check your hand sketches after drawing them.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots")
os.makedirs(OUT, exist_ok=True)

sig = lambda x: 1 / (1 + np.exp(-x))
INK, ASY, PT = "#1f3a68", "#c0392b", "#e67e22"


def base(title):
    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    ax.axhline(0, color="grey", lw=0.8)
    ax.axvline(0, color="grey", lw=0.8)
    ax.grid(alpha=0.3)
    ax.set_title(title)
    return fig, ax


def hline(ax, y, label=None):
    ax.axhline(y, color=ASY, ls="--", lw=1, label=label)


def vline(ax, x, label=None):
    ax.axvline(x, color=ASY, ls="--", lw=1, label=label)


def dot(ax, x, y, text, dx=0.15, dy=0.0, ha="left"):
    ax.plot([x], [y], "o", color=PT, ms=6, zorder=5)
    ax.annotate(text, (x, y), (x + dx, y + dy), fontsize=9, ha=ha)


def save(fig, ax, name):
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8, loc="best")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=110)
    plt.close(fig)


# ---------- A2 ----------
x = np.linspace(-4, 2.2, 400)
fig, ax = base("A2.1  e^x")
ax.plot(x, np.exp(x), color=INK, lw=2)
hline(ax, 0, "asymptote y=0 (x→−∞)")
dot(ax, 0, 1, "(0, 1)  slope 1")
dot(ax, 1, np.e, "(1, e≈2.72)")
save(fig, ax, "A2_1_exp.png")

x = np.linspace(0.02, 5, 400)
fig, ax = base("A2.2  ln x")
ax.plot(x, np.log(x), color=INK, lw=2)
vline(ax, 0, "asymptote x=0 (x→0⁺, y→−∞)")
dot(ax, 1, 0, "(1, 0)  slope 1")
dot(ax, np.e, 1, "(e, 1)", dy=-0.4)
save(fig, ax, "A2_2_ln.png")

x = np.linspace(-4, 4, 400)
fig, ax = base("A2.3  tanh x")
ax.plot(x, np.tanh(x), color=INK, lw=2)
hline(ax, 1, "asymptotes y=±1")
hline(ax, -1)
ax.plot(x, x, ":", color=PT, lw=1, label="tangent y=x at 0 (slope 1)")
ax.set_ylim(-1.5, 1.5)
dot(ax, 0, 0, "(0,0) inflection", dy=0.2)
save(fig, ax, "A2_3_tanh.png")

x = np.linspace(-3, 3, 401)
fig, ax = base("A2.4  ReLU(x) = max(0, x)")
ax.plot(x, np.maximum(0, x), color=INK, lw=2)
dot(ax, 0, 0, "corner at (0,0):\nslope 0 left, 1 right", dx=-0.2, dy=1.0, ha="right")
ax.set_ylim(-0.5, 3)
save(fig, ax, "A2_4_relu.png")

# ---------- A3 ----------
x = np.linspace(-3, 3, 400)
fig, ax = base("A3.1  x²")
ax.plot(x, x**2, color=INK, lw=2)
dot(ax, 0, 0, "(0,0) global min", dy=0.5)
dot(ax, 1, 1, "(1,1)")
dot(ax, -1, 1, "(−1,1)", dx=-0.15, ha="right")
save(fig, ax, "A3_01_x2.png")

x = np.linspace(-2, 2, 400)
fig, ax = base("A3.2  x³")
ax.plot(x, x**3, color=INK, lw=2)
dot(ax, 0, 0, "(0,0): f′=0, flat\ninflection, NOT max/min", dy=2)
dot(ax, 1, 1, "(1,1)", dy=-1)
dot(ax, -1, -1, "(−1,−1)", dx=-0.15, ha="right")
save(fig, ax, "A3_02_x3.png")

x = np.linspace(-3, 3, 401)
fig, ax = base("A3.3  |x|")
ax.plot(x, np.abs(x), color=INK, lw=2)
dot(ax, 0, 0, "corner (0,0), global min\nslope −1 left, +1 right", dx=0.3, dy=1.6)
save(fig, ax, "A3_03_abs.png")

fig, ax = base("A3.4  1/x")
for xs in (np.linspace(-4, -0.2, 200), np.linspace(0.2, 4, 200)):
    ax.plot(xs, 1 / xs, color=INK, lw=2)
hline(ax, 0, "asymptote y=0")
vline(ax, 0, "asymptote x=0")
dot(ax, 1, 1, "(1, 1)")
dot(ax, -1, -1, "(−1, −1)", dx=-0.15, ha="right")
save(fig, ax, "A3_04_reciprocal.png")

x = np.linspace(0, 6, 400)
fig, ax = base("A3.5  √x")
ax.plot(x, np.sqrt(x), color=INK, lw=2)
ax.plot([0, 0], [0, 0.8], ":", color=PT, lw=1.5, label="vertical tangent at origin")
dot(ax, 0, 0, "(0,0) min (endpoint)", dy=-0.3)
dot(ax, 1, 1, "(1,1)", dy=-0.3)
dot(ax, 4, 2, "(4,2)", dy=-0.3)
save(fig, ax, "A3_05_sqrt.png")

x = np.linspace(-3, 3, 400)
fig, ax = base("A3.6  e^(−x²)")
ax.plot(x, np.exp(-x**2), color=INK, lw=2)
hline(ax, 0, "asymptote y=0 (both ends)")
dot(ax, 0, 1, "(0,1) max", dy=-0.08)
k = 1 / np.sqrt(2)
dot(ax, k, np.exp(-0.5), "(0.71, 0.61)\ninflection")
dot(ax, -k, np.exp(-0.5), "(−0.71, 0.61)\ninflection", dx=-0.15, ha="right")
ax.set_ylim(-0.1, 1.2)
save(fig, ax, "A3_06_gauss.png")

x = np.linspace(-5, 5, 400)
fig, ax = base("A3.7  softplus = ln(1 + e^x)")
ax.plot(x, np.log1p(np.exp(x)), color=INK, lw=2, label="softplus")
ax.plot(x, np.maximum(0, x), ":", color="grey", lw=1.5, label="ReLU (for comparison)")
ax.plot(x, x, "--", color=ASY, lw=1, label="oblique asymptote y=x")
dot(ax, 0, np.log(2), "(0, ln2≈0.69)", dx=-0.2, dy=0.6, ha="right")
ax.set_ylim(-1, 5.5)
save(fig, ax, "A3_07_softplus.png")

x = np.linspace(-4, 3, 401)
fig, ax = base("A3.8  leaky ReLU")
ax.plot(x, np.where(x > 0, x, 0.1 * x), color=INK, lw=2)
dot(ax, 0, 0, "corner (0,0)\nslope 0.1 left, 1 right", dx=-0.3, dy=1.2, ha="right")
save(fig, ax, "A3_08_leaky.png")

p = np.linspace(0.02, 1, 400)
fig, ax = base("A3.9  −ln p,  0 < p ≤ 1")
ax.plot(p, -np.log(p), color=INK, lw=2)
vline(ax, 0, "asymptote p=0 (loss→∞)")
dot(ax, 1, 0, "(1, 0) min\n(endpoint)", dx=-0.05, dy=0.6, ha="right")
dot(ax, 0.5, np.log(2), "(0.5, 0.69)")
ax.set_xlabel("p")
save(fig, ax, "A3_09_nll.png")

x = np.linspace(0.001, 2, 400)
fig, ax = base("A3.10  x ln x,  x > 0")
ax.plot(x, x * np.log(x), color=INK, lw=2)
ax.plot([0], [0], "o", mfc="white", color=INK, ms=7, label="open circle: (0,0) not included")
dot(ax, 1 / np.e, -1 / np.e, "(1/e, −1/e) ≈ (0.37, −0.37)\nglobal min", dx=0.1, dy=-0.05)
dot(ax, 1, 0, "(1, 0)", dy=0.1)
ax.set_ylim(-0.6, 1.5)
save(fig, ax, "A3_10_xlnx.png")

# ---------- A4.1 ----------
x = np.linspace(-6, 8, 500)
fig, ax = base("A4.1  σ(x), σ(2x), σ(x−3)")
ax.plot(x, sig(x), color=INK, lw=2, label="σ(x): mid x=0, slope 1/4")
ax.plot(x, sig(2 * x), color="#16a085", lw=2, label="σ(2x): mid x=0, slope 1/2")
ax.plot(x, sig(x - 3), color="#8e44ad", lw=2, label="σ(x−3): mid x=3, slope 1/4")
hline(ax, 0.5)
ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "A4_1_transforms.png"), dpi=110)
plt.close(fig)

# ---------- A1 answer key picture ----------
fig, axs = plt.subplots(2, 4, figsize=(13, 6))
items = [
    ("Plot 1 = (g) ln(1+eˣ)", np.linspace(-5, 5, 300), lambda t: np.log1p(np.exp(t))),
    ("Plot 2 = (i) σ′(x)", np.linspace(-6, 6, 300), lambda t: sig(t) * (1 - sig(t))),
    ("Plot 3 = (c) −ln x", np.linspace(0.03, 3.2, 300), lambda t: -np.log(t)),
    ("Plot 4 = (e) tanh x", np.linspace(-4, 4, 300), np.tanh),
    ("Plot 5 = (a) eˣ", np.linspace(-3, 2, 300), np.exp),
    ("Plot 6 = (h) e^(−x²)", np.linspace(-3, 3, 300), lambda t: np.exp(-t**2)),
    ("Plot 7 = (j) x³", np.linspace(-2, 2, 300), lambda t: t**3),
    ("Plot 8 = (d) σ(x)", np.linspace(-6, 6, 300), sig),
]
for ax, (t, xs, f) in zip(axs.flat, items):
    ax.plot(xs, f(xs), color=INK, lw=2)
    ax.axhline(0, color="grey", lw=0.8)
    ax.axvline(0, color="grey", lw=0.8)
    ax.grid(alpha=0.3)
    ax.set_title(t, fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "A1_recreated.png"), dpi=100)
plt.close(fig)

print("wrote", len(os.listdir(OUT)), "plots to", OUT)
