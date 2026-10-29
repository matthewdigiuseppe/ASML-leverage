"""Figure for the minimal model: what Europe gets for ASML as a function of its walk-away value c - k."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT, TEXT2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1"
BLUE_DARK, BLUE_MID, BLUE_LIGHT = "#104281", "#2a78d6", "#dbe9fb"

# Computer Modern (shipped with matplotlib) to match the note's Latin Modern.
plt.rcParams.update({"font.family": "serif", "font.serif": ["cmr10"], "mathtext.fontset": "cm",
                     "axes.formatter.use_mathtext": True, "font.size": 9.5,
                     "axes.edgecolor": MUTED, "axes.labelcolor": TEXT2, "xtick.color": TEXT2,
                     "ytick.color": TEXT2, "axes.linewidth": 0.6, "legend.frameon": False,
                     "pdf.fonttype": 42})

V, V2 = 2.5, 4.2          # Washington's need, and a larger need for comparison
XMIN, XMAX, YMIN, YMAX = -3, 5.8, -3, 4.7
fig, ax = plt.subplots(figsize=(6.3, 4.1))
ax.grid(True, color=GRID, linewidth=0.6); ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)

# Europe switches beyond V (dark grey), and beyond V2 only if need were larger
ax.axvspan(V, XMAX, color="#f3f2ee", lw=0)
ax.axvspan(V2, XMAX, color="#e9e8e3", lw=0)
ax.axvline(V, color=MUTED, lw=0.8, ls=(0, (1, 2)))
ax.axvline(V2, color=MUTED, lw=0.8, ls=(0, (1, 2)), alpha=0.7)
ax.text(V - 0.08, 4.45, "Washington's need, $V$", color=TEXT2, fontsize=8.5, ha="right")
ax.text(V2 - 0.08, 4.45, "more need, $V'$", color=TEXT2, fontsize=8.5, ha="right")
ax.text(V + 0.08, -2.85, "Europe goes if\nWashington's\nneed is $V$", color=TEXT2, fontsize=8)
ax.text(V2 + 0.08, -2.85, "Europe goes\neven if the\nneed is $V'$", color=TEXT2, fontsize=8)

# squeeze room: a vertical distance at each negative walk-away value
xs = np.linspace(XMIN, 0, 50)
ax.fill_between(xs, xs, 0, color=BLUE_LIGHT, lw=0)
ax.annotate("", xy=(-2, 0), xytext=(-2, -2),
            arrowprops=dict(arrowstyle="<->", color=BLUE_DARK, lw=0.8, shrinkA=0, shrinkB=0))
ax.text(-1.92, -1.15, "$k-c$", color=BLUE_DARK, fontsize=9)
ax.annotate("Washington's squeeze room,\n$k-c$: one budget\nfor every demand",
            xy=(-0.9, -0.45), xytext=(0.3, -2.3), color=BLUE_DARK, fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=BLUE_DARK, lw=0.6))

# payment lines: solid up to V, faint from V to V2 (what more need would add)
ax.axhline(0, color=MUTED, lw=0.5, alpha=0.6)
x = np.linspace(XMIN, V, 400)
ax.plot(x, x, color=BLUE_DARK, lw=1.8, label="Washington's threats stick", zorder=3)
ax.plot(x, np.maximum(0, x), color=BLUE_MID, lw=1.6, ls=(0, (4, 2.5)),
        label="Washington's threats do not stick", zorder=4)
x2 = np.linspace(V, V2, 100)
ax.plot(x2, x2, color=BLUE_DARK, lw=1.4, alpha=0.3, zorder=3)
ax.annotate("", xy=(V2, 0.75), xytext=(V, 0.75),
            arrowprops=dict(arrowstyle="->", color=TEXT2, lw=0.7, shrinkA=0, shrinkB=0))
ax.text((V + V2) / 2, 0.9, "more need extends\nthe line; it does\nnot lift it",
        color=TEXT2, fontsize=8, ha="center", va="bottom")
ax.text(0.75, 0.12, "above zero the\ntwo lines coincide", color=TEXT2, fontsize=8)

ax.set_xlim(XMIN, XMAX); ax.set_ylim(YMIN, YMAX)
ax.set_xticks(range(-3, 6))
ax.set_xticklabels(["$-3$", "$-2$", "$-1$", "0\n($c=k$)", "1", "2", "3", "4", "5"])
ax.set_xlabel("Europe's walk-away value, $c-k$ (China's offer minus Washington's penalty)")
ax.set_ylabel("What Washington pays Europe\n(below zero: Europe's concessions)")
ax.legend(loc="upper left", fontsize=8.5, handlelength=2.4)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_minimal.pdf"))
print("written")
