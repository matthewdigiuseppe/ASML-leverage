"""v2 verifier m4: Proposition 5 (breakdown with private sovereignty cost, general log-concave F).

sigma ~ F on [0, sbar]. Conditions of Prop 4 with Delta_c = inf, no investment, Q1 < 0, mbar_U >= e.
R = delta[Q2]^+, bt = B1 - r^c. U chooses a payment T >= 0 by DIRECT numerical optimization
(grid of 4001 points on [0, Tmax], bounded local refinement, explicit T = 0 corner).
  threat-backed ultimatum: type sigma accepts iff T - sigma - r^c >= R - B1; U's gain
       accept: v_c + R - T - k ; refuse: -e - k (the threat is executed).
  unthreatened purchase offer (stake 0, so no credible threat): accept iff T - sigma - r^c >= R;
       gain accept: v_c + R - T - k ; refuse: -k.
Memo formula: s* solves bt + v_c + e - s = F(s)/f(s); shat = max{bt - R, min{sbar, s*}};
U issues iff F(shat)(bt + v_c - shat) - (1 - F(shat)) e > k; P_b = 1 - F(shat).
Distributions: uniform, truncated normal, Beta(2,2), triangular, truncated exponential (both signs of the
rate); plus a bimodal (not log-concave) mixture to test robustness of the comparative statics.
Comparative statics: brute-force P_b (threat-backed only) after raising B1, e, v_c, r^c, R, k; and the
same with U free to choose the purchase offer instead, for (a) refusal probability and (b) breakdown
probability (refusal followed by the executed threat).
Run: python3 -I v2_m4_prop5.py
"""
import math
import random
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.special import ndtr


# ----------------------------------------------------------------------------- distributions
def make_dist(kind, sbar, rng):
    if kind == "uniform":
        F = lambda s: np.clip(np.asarray(s, float) / sbar, 0, 1)
        f = lambda s: np.where((np.asarray(s) >= 0) & (np.asarray(s) <= sbar), 1 / sbar, 0.0)
        return F, f, {}
    if kind == "tnormal":
        mu = rng.uniform(-0.5, 1.5) * sbar
        tau = rng.uniform(0.1, 1.0) * sbar
        a, b = ndtr((0 - mu) / tau), ndtr((sbar - mu) / tau)
        Z = b - a
        F = lambda s: np.clip((ndtr((np.clip(np.asarray(s, float), 0, sbar) - mu) / tau) - a) / Z, 0, 1)
        f = lambda s: np.where((np.asarray(s) >= 0) & (np.asarray(s) <= sbar),
                               np.exp(-0.5 * ((np.asarray(s, float) - mu) / tau) ** 2) / (tau * math.sqrt(2 * math.pi) * Z), 0.0)
        return F, f, dict(mu=mu, tau=tau)
    if kind == "beta22":
        F = lambda s: (lambda x: 3 * x ** 2 - 2 * x ** 3)(np.clip(np.asarray(s, float) / sbar, 0, 1))
        f = lambda s: (lambda x: np.where((x >= 0) & (x <= 1), 6 * x * (1 - x) / sbar, 0.0))(np.asarray(s, float) / sbar)
        return F, f, {}
    if kind == "triangular":
        c = rng.choice([0.0, sbar, rng.uniform(0, sbar)])

        def F(s):
            x = np.clip(np.asarray(s, float), 0, sbar)
            left = x ** 2 / (sbar * c) if c > 0 else np.zeros_like(x)
            right = 1 - (sbar - x) ** 2 / (sbar * (sbar - c)) if c < sbar else np.ones_like(x)
            return np.where(x <= c, left, right)

        def f(s):
            x = np.asarray(s, float)
            left = 2 * x / (sbar * c) if c > 0 else np.zeros_like(x)
            right = 2 * (sbar - x) / (sbar * (sbar - c)) if c < sbar else np.zeros_like(x)
            return np.where((x < 0) | (x > sbar), 0.0, np.where(x <= c, left, right))
        return F, f, dict(c=c)
    if kind == "texp":
        lam = rng.choice([1, -1]) * rng.uniform(0.2, 3.0) / sbar
        Z = 1 - math.exp(-lam * sbar)
        F = lambda s: np.clip((1 - np.exp(-lam * np.clip(np.asarray(s, float), 0, sbar))) / Z, 0, 1)
        f = lambda s: np.where((np.asarray(s) >= 0) & (np.asarray(s) <= sbar), lam * np.exp(-lam * np.asarray(s, float)) / Z, 0.0)
        return F, f, dict(lam=lam)
    if kind == "bimodal":   # NOT log-concave
        m1, m2, tau = 0.2 * sbar, 0.8 * sbar, 0.06 * sbar
        a1, b1 = ndtr(-m1 / tau), ndtr((sbar - m1) / tau)
        a2, b2 = ndtr(-m2 / tau), ndtr((sbar - m2) / tau)

        def F(s):
            x = np.clip(np.asarray(s, float), 0, sbar)
            return 0.5 * (ndtr((x - m1) / tau) - a1) / (b1 - a1) + 0.5 * (ndtr((x - m2) / tau) - a2) / (b2 - a2)

        def f(s):
            x = np.asarray(s, float)
            g = lambda m, Z: np.exp(-0.5 * ((x - m) / tau) ** 2) / (tau * math.sqrt(2 * math.pi) * Z)
            return np.where((x < 0) | (x > sbar), 0.0, 0.5 * g(m1, b1 - a1) + 0.5 * g(m2, b2 - a2))
        return F, f, {}
    raise ValueError(kind)


# ----------------------------------------------------------------------------- direct optimization
def optimize(F, P, threat, sbar, ngrid=4001):
    """Maximize U's gain over T >= 0. Returns (gain, cutoff s, acceptance prob)."""
    B1, rc, e, vc, k, R = P["B1"], P["rc"], P["e"], P["vc"], P["k"], P["R"]
    shift = (B1 - rc - R) if threat else (-rc - R)     # cutoff s = T + shift
    loss = e if threat else 0.0

    def gain(T):
        Fs = F(T + shift)
        return Fs * (vc + R - T) - (1 - Fs) * loss - k

    Tmax = max(0.0, sbar - shift) + 1.0
    Tg = np.linspace(0.0, Tmax, ngrid)
    G = gain(Tg)
    i = int(np.argmax(G))
    lo, hi = Tg[max(i - 1, 0)], Tg[min(i + 1, ngrid - 1)]
    res = minimize_scalar(lambda T: -float(gain(T)), bounds=(lo, hi), method="bounded", options={"xatol": 1e-11})
    cands = [(float(G[i]), Tg[i]), (-res.fun, res.x), (float(gain(0.0)), 0.0)]
    g, T = max(cands, key=lambda x: x[0])
    s = T + shift
    return g, s, float(F(s))


def formula(F, f, P, sbar):
    bt = P["B1"] - P["rc"]
    A = bt + P["vc"] + P["e"]
    phi = lambda s: float(f(s)) * (A - s) - float(F(s))
    if A <= 0:
        sstar = 0.0
    elif phi(sbar) >= 0:
        sstar = sbar
    else:
        lo = 1e-12
        sstar = brentq(phi, lo, sbar, xtol=1e-13) if phi(lo) > 0 else lo
    shat = max(bt - P["R"], min(sbar, sstar))
    Fh = float(F(shat))
    issue = Fh * (bt + P["vc"] - shat) - (1 - Fh) * P["e"] > P["k"]
    return shat, 1 - Fh, issue, Fh * (bt + P["vc"] - shat) - (1 - Fh) * P["e"] - P["k"]


def draw(rng):
    return dict(B1=rng.uniform(0.05, 6), rc=rng.choice([0.0, rng.uniform(0, 3)]), e=rng.uniform(0.01, 6),
                vc=rng.choice([0.0, rng.uniform(0, 4)]), k=rng.choice([0.0, rng.uniform(0, 1)]),
                R=rng.choice([0.0, rng.uniform(0, 6)]))


def outcome(F, P, sbar, allow_offer):
    gT, sT, FT = optimize(F, P, True, sbar)
    opts = [(gT, "threat", FT)]
    if allow_offer:
        g0, s0, F0 = optimize(F, P, False, sbar)
        opts.append((g0, "offer", F0))
    best = max(opts, key=lambda x: x[0])
    if best[0] <= 1e-9:
        return None
    refuse = 1 - best[2]
    breakdown = refuse if best[1] == "threat" else 0.0
    return dict(kind=best[1], refuse=refuse, breakdown=breakdown, gain=best[0])


def main():
    rng = random.Random(5)
    kinds = ["uniform", "tnormal", "beta22", "triangular", "texp", "bimodal"]
    print("Proposition 5: direct optimization of U's offer vs memo formula")
    for kind in kinds:
        st = dict(n=0, s_err=0.0, Pb_err=0.0, issue_mis=0, near_tie_skipped=0, corner_T0=0, all_accept=0,
                  offer_beats_threat=0, offer_beats_threat_vc_le_rc=0)
        for i in range(1500):
            sbar = rng.uniform(0.5, 8)
            F, f, _ = make_dist(kind, sbar, rng)
            P = draw(rng)
            st["n"] += 1
            g, s, Fs = optimize(F, P, True, sbar)
            shat, Pb, iss, gform = formula(F, f, P, sbar)
            if abs(gform) < 1e-6:
                st["near_tie_skipped"] += 1
                continue
            if (g > 1e-9) != iss:
                st["issue_mis"] += 1
            if kind != "bimodal":
                s_cmp = min(s, max(sbar, P["B1"] - P["rc"] - P["R"]))
                if g > 1e-9:   # cutoff is pinned down only when U issues (else flat regions)
                    st["s_err"] = max(st["s_err"], abs(s_cmp - shat))
            st["Pb_err"] = max(st["Pb_err"], abs((1 - Fs) - Pb))
            if shat == P["B1"] - P["rc"] - P["R"]:
                st["corner_T0"] += 1
            if Pb == 0:
                st["all_accept"] += 1
            g0, _, _ = optimize(F, P, False, sbar)
            if g0 > max(g, 0) + 1e-7:
                st["offer_beats_threat"] += 1
                if P["vc"] <= P["rc"]:
                    st["offer_beats_threat_vc_le_rc"] += 1
        print(f" {kind}: {st}")

    print("\nComparative statics (brute force). Counts of violations / comparisons with issuance in both.")
    steps = dict(B1=+1, e=+1, vc=+1, rc=+1, R=+1, k=+1)
    claim = dict(B1="nonincreasing", e="nonincreasing", vc="nonincreasing", rc="nondecreasing", R="nondecreasing", k="constant")
    for kind in kinds:
        viol = {p: [0, 0] for p in steps}
        viol_ref = {p: [0, 0] for p in steps}
        viol_bd = {p: [0, 0] for p in steps}
        for i in range(500):
            sbar = rng.uniform(0.5, 8)
            F, f, _ = make_dist(kind, sbar, rng)
            P = draw(rng)
            base_T = outcome(F, P, sbar, False)
            base_O = outcome(F, P, sbar, True)
            for p in steps:
                Q = dict(P)
                Q[p] = P[p] + rng.uniform(0.05, 1.5)
                new_T = outcome(F, Q, sbar, False)
                new_O = outcome(F, Q, sbar, True)
                for (b, n, key, store) in ((base_T, new_T, "refuse", viol), (base_O, new_O, "refuse", viol_ref),
                                           (base_O, new_O, "breakdown", viol_bd)):
                    if b is None or n is None:
                        continue
                    store[p][1] += 1
                    dlt = n[key] - b[key]
                    bad = ((claim[p] == "nonincreasing" and dlt > 1e-6) or (claim[p] == "nondecreasing" and dlt < -1e-6)
                           or (claim[p] == "constant" and abs(dlt) > 1e-6))
                    store[p][0] += bad
        print(f" {kind}: threat-only P_b {viol}")
        print(f" {kind}: with purchase option, refusal prob {viol_ref}")
        print(f" {kind}: with purchase option, breakdown prob {viol_bd}")

    # hand-picked: unthreatened purchase offer beats the threat
    F, f, _ = make_dist("uniform", 10.0, rng)
    P = dict(B1=1.0, rc=0.0, e=20.0, vc=8.0, k=0.0, R=0.0)
    print("\nhand-picked uniform sbar=10, B1=1, e=20, v_c=8, R=0: threat", optimize(F, P, True, 10.0),
          " purchase offer", optimize(F, P, False, 10.0), " formula", formula(F, f, P, 10.0))
    for e in (0.2, 20.0):
        P = dict(B1=1.0, rc=0.0, e=e, vc=8.0, k=0.0, R=0.0)
        print(f"  e={e}: U's choice with purchase option:", outcome(F, P, 10.0, True))
    for B1 in (1.0, 2.0):
        P = dict(B1=B1, rc=0.0, e=1.0, vc=8.0, k=0.0, R=0.0)
        print(f"  B1={B1}, e=1: U's choice with purchase option:", outcome(F, P, 10.0, True))
    for vc in (8.0, 10.0):
        P = dict(B1=1.0, rc=0.0, e=1.0, vc=vc, k=0.0, R=0.0)
        print(f"  v_c={vc}, B1=1, e=1: U's choice with purchase option:", outcome(F, P, 10.0, True))
    for rc in (0.0, 2.0):
        P = dict(B1=1.0, rc=rc, e=1.0, vc=10.0, k=0.0, R=0.0)
        print(f"  r^c={rc}, B1=1, e=1, v_c=10: U's choice with purchase option:", outcome(F, P, 10.0, True))


if __name__ == "__main__":
    main()
