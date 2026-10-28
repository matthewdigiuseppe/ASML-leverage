"""Figures for 'Owning the Chokepoint'. Run: python3 make_figures.py (writes PDFs next to this file)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SURFACE = "#ffffff"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
MUTED = "#8a8984"
GRID = "#e6e5e1"
BLUE = ["#86b6ef", "#2a78d6", "#104281"]   # sequential blue steps 250 / 450 / 650
ORANGE = "#eb6834"
AQUA = "#1baf7a"

plt.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.edgecolor": MUTED, "axes.labelcolor": TEXT2,
    "xtick.color": TEXT2, "ytick.color": TEXT2, "axes.linewidth": 0.6, "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE, "legend.frameon": False,
})


def style(ax):
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


# Figure 1: break-even conditionality kappa* = omega / S (other exit costs set to zero, which favours Europe)
def fig_breakeven():
    fig, ax = plt.subplots(figsize=(5.4, 3.4))
    omega = np.linspace(0, 60, 400)
    for S, col in zip((150, 250, 350), BLUE):
        k = np.minimum(omega / S, 1)
        ax.plot(omega, k, color=col, lw=1.6, solid_capstyle="round",
                label=f"S = EUR {S}bn a year")
        ax.text(60.8, min(60 / S, 1), f"S = {S}", color=TEXT2, va="center", fontsize=8)
    for x, lab in ((9.5, "ASML sales\nto China, 2025"), (32.7, "ASML total\nsales, 2025")):
        ax.axvline(x, color=MUTED, lw=0.6)
        ax.text(x + 0.6, 0.385, lab, color=TEXT2, fontsize=7.5, va="top")
    ax.text(14, 0.27, "No leverage\n(exit premium $\\leq 0$)", color=TEXT, fontsize=8.5)
    ax.text(21, 0.012, "Leverage possible", color=TEXT, fontsize=8.5)
    ax.set_xlim(0, 66)
    ax.set_ylim(0, 0.4)
    ax.set_xlabel("China's credible offer, $\\omega$ (EUR bn a year)")
    ax.set_ylabel("Break-even conditionality, $\\kappa^*$")
    ax.legend(loc="lower right", bbox_to_anchor=(0.99, 0.02), fontsize=7.5, handlelength=1.6)
    style(ax)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_breakeven.pdf"))
    plt.close(fig)


# Figure 2: windows for preventive control (illustrative units)
def fig_windows():
    t = np.arange(0, 11)
    sig_rc = 1.0          # sigma + r^c
    alpha = 2.0           # AI stick, constant
    paths = {
        "(a) Rising exit premium": -3.4 + 0.42 * t,
        "(b) Exit premium rises but stays negative": -3.4 + 3.0 * (1 - np.exp(-0.3 * t)),
    }
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.9), sharey=True)
    for ax, (title, Q) in zip(axes, paths.items()):
        us = (Q < -sig_rc) & (alpha > sig_rc)
        eu = Q > 0
        for i in range(len(t)):
            if us[i]:
                ax.axvspan(t[i] - 0.5, t[i] + 0.5, color=BLUE[1], alpha=0.10, lw=0)
            if eu[i]:
                ax.axvspan(t[i] - 0.5, t[i] + 0.5, color=ORANGE, alpha=0.12, lw=0)
        ax.axhline(0, color=MUTED, lw=0.8)
        ax.axhline(-sig_rc, color=MUTED, lw=0.6, ls=(0, (1, 2)))
        ax.plot(t, Q, color=TEXT, lw=1.6, marker="o", ms=3.5, mec=SURFACE, mew=1.0)
        ax.set_title(title, fontsize=9, color=TEXT, loc="left")
        ax.set_xlabel("Period")
        ax.set_xlim(-0.5, 10.5)
        style(ax)
        ax.grid(False)
        if eu.any():
            first_eu = t[eu][0]
            last_us = t[us][-1] if us.any() else None
            ax.text(first_eu - 0.35, -2.1, "Europe's\nwindow", color=TEXT2, fontsize=7.5)
            pass
        ax.text(0.0, -1.55, "US window", color=TEXT2, fontsize=7.5)
        if not eu.any():
            ax.text(5.8, 0.35, "no later rents:\nno demand", color=TEXT2, fontsize=7.5)
    axes[0].set_ylabel("Exit premium $Q_t$")
    axes[1].text(10.4, -sig_rc - 0.32, "$-(\\sigma + r^c)$", color=TEXT2, fontsize=7.5, ha="right")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_windows.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    fig_breakeven()
    fig_windows()
    print("written")
