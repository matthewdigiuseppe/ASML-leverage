"""Figure for the minimal model: what Europe gets for ASML as a function of its walk-away value c - k."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT, TEXT2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1"
BLUE_DARK, BLUE_MID, BLUE_LIGHT, ORANGE = "#104281", "#2a78d6", "#dbe9fb", "#eb6834"
plt.rcParams.update({"font.family": "serif", "font.size": 9, "axes.edgecolor": MUTED,
                     "axes.labelcolor": TEXT2, "xtick.color": TEXT2, "ytick.color": TEXT2,
                     "axes.linewidth": 0.6, "legend.frameon": False})

V = 3.0
fig, ax = plt.subplots(figsize=(5.8, 3.9))
ax.grid(True, color=GRID, linewidth=0.6); ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)

# Europe switches beyond V
ax.axvspan(V, 5.2, color="#efeeea", lw=0)
ax.text(V + 0.12, -2.75, "Washington lets\nEurope go", color=TEXT2, fontsize=8)
ax.axvline(V, color=MUTED, lw=0.8, ls=(0, (1, 2)))
ax.text(V + 0.12, 3.85, "Washington's need, $V$", color=TEXT2, fontsize=8, ha="left")

# squeeze room
xs = np.linspace(-3, 0, 50)
ax.fill_between(xs, xs, 0, color=BLUE_LIGHT, lw=0)
ax.text(-2.95, -0.75, "Washington's squeeze room, $k-c$:\none budget for every demand", color=BLUE_DARK, fontsize=8)

# payment lines
x = np.linspace(-3, V, 400)
ax.plot(x, np.maximum(0, x), color=BLUE_MID, lw=1.6, ls=(0, (4, 2.5)), label="Washington's threats do not stick")
ax.plot(x, x, color=BLUE_DARK, lw=1.8, label="Washington's threats stick")

ax.axhline(0, color=MUTED, lw=0.8)
ax.text(1.25, 0.55, "above zero the\ntwo lines coincide", color=TEXT2, fontsize=7.5)
ax.set_xlim(-3, 5.2); ax.set_ylim(-3, 4.2)
ax.set_xlabel("Europe's walk-away value, $c-k$ (China's offer minus Washington's penalty)")
ax.set_ylabel("What Washington pays Europe\n(below zero: Europe's concessions)")
ax.legend(loc="upper left", fontsize=8, handlelength=2.4)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_minimal.pdf"))
print("written")
