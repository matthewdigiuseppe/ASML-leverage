"""v2 verifier m4: Proposition 4 (preventive control) and corollaries (i)-(iv).

Two-period game solved by brute force from primitives (no use of the Gamma / T* formulas inside
the solver):
  start of period 1: U chooses (a) no ultimatum, or (b) an ultimatum at cost k: a stake m in
     {0, mbar_U} on a period-1 withdrawal of an instrument bundle (unconditional part u, conditional
     part dd, direct ex post cost g >= 0 to U) and a payment T >= 0 on a grid of mesh h.
  E accepts or refuses (an indifferent E accepts).
  accept : control passes; premia fall by Dc at both dates; U gets v_c; E bears sigma + r^c.
           U then decides whether to withdraw anyway (no stake is triggered); it withdraws only if
           that is strictly profitable ex post.
  refuse : U decides whether to execute the withdrawal (executes iff ex post payoff incl. forfeiting
           m is weakly lower without executing, i.e. ties go to execution).
  Period-1 contest (static benchmark, Lemma 1): with premium p and no withdrawal E gets [p]^+ and U
     pays it; after a withdrawal E's aligned payoff falls by u+dd and its premium rises to p+dd, so E
     gets -(u+dd)+[p+dd]^+ and U gets -g-[p+dd]^+.
  After the period-1 outcome E chooses to invest Ibar at cost K_I (strictly profitable only, unless
     the alternative tie rule is requested); the period-2 contest gives E delta[q2+Ibar*inv]^+.
U issues iff its best ultimatum payoff is STRICTLY above the no-ultimatum payoff.

The script compares with the memo formulas
  Gamma = v_c - k + min{dRU, (dRU - dRH) + B1 - sigma - r^c},   T* = [dRH - B1 + sigma + r^c]^+
with B1 = u + min{dd, [-Q1]^+} if the threat is credible (g + [Q1+dd]^+ - [Q1]^+ <= mbar_U), else 0,
and checks corollaries (i)-(iv) on brute-force quantities.
Run: python3 -I v2_m4_prop4.py
"""
import math
import random
import numpy as np

INF = float("inf")


def pos(x):
    return x if x > 0 else 0.0


# ----------------------------------------------------------------------------- brute force
def stage2(q, par, tie_invest=False, tol=1e-12):
    """E's period-2 value (net of K_I) and U's period-2 rent payment, both in period-1 units."""
    d, Ib, KI = par["d"], par["Ib"], par["KI"]
    if q == -INF:
        return 0.0, 0.0, 0
    no = d * pos(q)
    yes = d * pos(q + Ib) - KI
    inv = (yes > no + tol) or (tie_invest and yes >= no - tol)
    if inv:
        return yes, d * pos(q + Ib), 1
    return no, d * pos(q), 0


def period1(p, withdrawn, par):
    u, dd, g = par["u"], par["dd"], par["g"]
    if withdrawn:
        return -(u + dd) + pos(p + dd), -g - pos(p + dd)
    return pos(p), -pos(p)


def solve(par, h, tie_invest=False, tol=1e-9):
    Q1, Q2, Dc = par["Q1"], par["Q2"], par["Dc"]
    vc, k, sig, rc, mbar = par["vc"], par["k"], par["sig"], par["rc"], par["mbar"]
    # no ultimatum
    E2, C2, _ = stage2(Q2, par, tie_invest)
    E1, U1 = period1(Q1, False, par)
    E0, U0 = E1 + E2, U1 - C2
    # acceptance branch
    qa1 = Q1 - Dc
    qa2 = Q2 - Dc
    _, Ucut_a = period1(qa1, True, par)
    _, Unc_a = period1(qa1, False, par)
    cut_after_accept = Ucut_a > Unc_a + tol
    E1a, U1a = period1(qa1, cut_after_accept, par)
    E2a, C2a, _ = stage2(qa2, par, tie_invest)
    Eacc0 = -sig - rc + E1a + E2a          # + T
    Uacc0 = vc - k + U1a - C2a             # - T
    Tmax = pos(Q1) + par["d"] * pos(Q2 + par["Ib"]) + sig + rc + 2.0
    Tg = np.arange(0.0, Tmax + h / 2, h)
    best = None
    cuts = []
    Uacc_max = (-INF, None, None)
    for m in (0.0, mbar):
        E1c, U1c = period1(Q1, True, par)
        Ucut = U1c - C2
        Unc = -m + U1 - C2
        cut = Ucut >= Unc - tol
        cuts.append(cut)
        Eref = (E1c if cut else E1) + E2
        Uref = -k + (Ucut if cut else Unc)
        acc = Eacc0 + Tg >= Eref - tol
        Upay = np.where(acc, Uacc0 - Tg, Uref)
        i = int(np.argmax(Upay))
        # best accepted ultimatum (smallest accepted grid T)
        if acc.any():
            j = int(np.argmax(acc))
            Uacc_best, Tacc = Uacc0 - Tg[j], Tg[j]
        else:
            Uacc_best, Tacc = -INF, None
        cand = dict(m=m, U=Upay[i], accepted=bool(acc[i]), T=Tg[i], Uacc=Uacc_best, Tacc=Tacc,
                    Eref=Eref, cut=cut)
        if best is None or cand["U"] > best["U"] + tol or (
                abs(cand["U"] - best["U"]) <= tol and cand["accepted"] and not best["accepted"]):
            best = cand
        if Uacc_best > Uacc_max[0] + tol:
            Uacc_max = (Uacc_best, Tacc, Eref)
    issue = best["U"] > U0 + tol
    out = dict(issue=issue, accepted=best["accepted"], T=best["T"], gain=best["U"] - U0,
               Gnum=Uacc_max[0] - U0, Tacc=Uacc_max[1], E0=E0, U0=U0,
               Eref=Uacc_max[2], dRU=(-U1 + C2) - (-U1a + C2a),
               dRH=(E1 + E2) - (E1a + E2a), cut_after_accept=cut_after_accept,
               Epay=(Eacc0 + best["T"]) if issue else E0, cuts=tuple(cuts))
    return out


# ----------------------------------------------------------------------------- memo formulas
def formula(par, tie_invest=False):
    d, Ib, KI = par["d"], par["Ib"], par["KI"]
    Q1, Q2, Dc = par["Q1"], par["Q2"], par["Dc"]

    def I(q):
        if q == -INF:
            return 0
        x = d * (pos(q + Ib) - pos(q))
        return 1 if (x > KI + 1e-12 or (tie_invest and x >= KI - 1e-12)) else 0

    def RU(q):
        return 0.0 if q == -INF else d * pos(q + Ib * I(q))

    def VH(q):
        return RU(q) - KI * I(q)

    dRU = pos(Q1) - pos(Q1 - Dc) + RU(Q2) - RU(Q2 - Dc)
    dRH = pos(Q1) - pos(Q1 - Dc) + VH(Q2) - VH(Q2 - Dc)
    e = par["g"] + pos(Q1 + par["dd"]) - pos(Q1)
    B1 = par["u"] + min(par["dd"], pos(-Q1)) if e <= par["mbar"] + 1e-12 else 0.0
    G = par["vc"] - par["k"] + min(dRU, dRU - dRH + B1 - par["sig"] - par["rc"])
    T = pos(dRH - B1 + par["sig"] + par["rc"])
    Epay = max(dRH - B1, -par["sig"] - par["rc"]) + pos(Q1 - Dc) + VH(Q2 - Dc)
    return dict(G=G, T=T, B1=B1, dRU=dRU, dRH=dRH, e=e, I2=I(Q2), I2c=I(Q2 - Dc), Epay=Epay)


# ----------------------------------------------------------------------------- draws
def draw_exact(rng):
    """Small integer parameters, dyadic delta: every threshold lies on the grid of mesh 1/64."""
    return dict(
        d=rng.choice([1.0, 0.5, 0.75, 0.25]),
        Q1=float(rng.randint(-6, 4)), Q2=float(rng.randint(-5, 6)),
        Dc=rng.choice([1.0, 2.0, 3.0, 5.0, INF, INF]),
        vc=float(rng.choice([0, 0, rng.randint(0, 3)])), k=float(rng.choice([0, 0, rng.randint(0, 2)])),
        sig=float(rng.randint(0, 3)), rc=float(rng.choice([0, rng.randint(0, 3)])),
        Ib=float(rng.choice([0, rng.randint(0, 4)])), KI=float(rng.randint(0, 3)),
        u=float(rng.choice([0, 0, rng.randint(0, 3)])), dd=float(rng.randint(0, 6)),
        g=float(rng.choice([0, rng.randint(0, 2)])), mbar=float(rng.randint(0, 8)))


def draw_cont(rng):
    return dict(
        d=rng.choice([1.0, rng.uniform(0.05, 1)]),
        Q1=rng.uniform(-6, 4), Q2=rng.uniform(-5, 6),
        Dc=rng.choice([rng.uniform(0.1, 6), INF]),
        vc=rng.choice([0.0, rng.uniform(0, 3)]), k=rng.choice([0.0, rng.uniform(0, 2)]),
        sig=rng.uniform(0, 3), rc=rng.choice([0.0, rng.uniform(0, 3)]),
        Ib=rng.choice([0.0, rng.uniform(0, 4)]), KI=rng.uniform(0, 3),
        u=rng.choice([0.0, rng.uniform(0, 3)]), dd=rng.uniform(0, 6),
        g=rng.uniform(0, 2), mbar=rng.uniform(0, 8))


EDGE = [
    # Q1 = 0, Q2 = 0, ties sigma + r^c = B1, Gamma = 0
    dict(d=1.0, Q1=0.0, Q2=0.0, Dc=INF, vc=0.0, k=0.0, sig=0.0, rc=0.0, Ib=0.0, KI=0.0, u=0.0, dd=2.0, g=0.0, mbar=0.0),
    dict(d=1.0, Q1=-2.0, Q2=3.0, Dc=INF, vc=0.0, k=0.0, sig=1.0, rc=1.0, Ib=0.0, KI=0.0, u=0.0, dd=2.0, g=0.0, mbar=2.0),
    dict(d=1.0, Q1=-3.0, Q2=3.0, Dc=INF, vc=0.0, k=0.0, sig=1.0, rc=1.0, Ib=0.0, KI=0.0, u=0.0, dd=2.0, g=1.0, mbar=1.0),
    # credibility knife-edge e = mbar
    dict(d=1.0, Q1=-1.0, Q2=3.0, Dc=INF, vc=0.0, k=0.0, sig=0.0, rc=0.0, Ib=0.0, KI=0.0, u=0.0, dd=3.0, g=1.0, mbar=3.0),
    # investment tie: d([q+I]^+-[q]^+) = K_I
    dict(d=1.0, Q1=-4.0, Q2=-1.0, Dc=INF, vc=0.0, k=0.0, sig=0.0, rc=0.0, Ib=3.0, KI=2.0, u=0.0, dd=5.0, g=0.0, mbar=8.0),
    # zero-bite purchase driven by investment (Q1 > 0, no threat)
    dict(d=1.0, Q1=1.0, Q2=-0.5, Dc=INF, vc=0.0, k=0.0, sig=1.0, rc=0.0, Ib=3.0, KI=2.0, u=0.0, dd=0.0, g=0.0, mbar=0.0),
    # finite Dc smaller than Q2: residual rent after transfer
    dict(d=0.5, Q1=2.0, Q2=5.0, Dc=2.0, vc=1.0, k=0.5, sig=0.0, rc=0.0, Ib=1.0, KI=0.0, u=2.0, dd=1.0, g=0.0, mbar=3.0),
    # unconditional bite with Q1 > 0
    dict(d=1.0, Q1=1.0, Q2=-5.0, Dc=INF, vc=0.0, k=0.0, sig=0.5, rc=0.5, Ib=0.0, KI=0.0, u=3.0, dd=0.0, g=0.0, mbar=0.0),
    # g = 0 and U indifferent about withdrawing after acceptance
    dict(d=1.0, Q1=-5.0, Q2=2.0, Dc=1.0, vc=0.0, k=0.0, sig=0.0, rc=0.0, Ib=0.0, KI=0.0, u=0.0, dd=1.0, g=0.0, mbar=0.0),
]


def main():
    rng = random.Random(20261029)
    st = dict(n=0, issue_mis=0, T_err=0.0, G_err=0.0, E_err=0.0, refused_on_path=0, cut_after_accept=0,
              skipped_near_tie=0, n_issue=0, cor_i_viol=0, cor_ii_viol=0, cor_ii_ident_err=0.0,
              cor_iii_viol=0, cor_iv_err=0.0, n_iv=0, n_iii=0, tie_rule_diff=0, zero_bite_purchases=0,
              n_exact=0, n_cont=0, n_edge=0)
    ex = {}

    def check(par, h, exact):
        tol_cmp = 1e-9 if exact else 2 * h + 1e-9
        bf = solve(par, h)
        fm = formula(par)
        st["n"] += 1
        if not exact and abs(fm["G"]) < 3 * h:
            st["skipped_near_tie"] += 1
            return
        pred = fm["G"] > 1e-12
        if bf["issue"] and not bf["accepted"]:
            st["refused_on_path"] += 1
        if bf["cut_after_accept"]:
            st["cut_after_accept"] += 1
        if bf["issue"] != pred:
            st["issue_mis"] += 1
            ex.setdefault("issue_mis", (par, bf, fm))
            return
        # Gamma compared with the best ACCEPTED ultimatum (defined whether or not U issues)
        key = "G_err" if not exact else "G_err_exact"
        st[key] = max(st.get(key, 0.0), abs(bf["Gnum"] - fm["G"]) if bf["Gnum"] > -INF else 0)
        if abs(bf["Gnum"] - fm["G"]) > tol_cmp:
            ex.setdefault("G", (par, bf, fm))
        if bf["issue"]:
            st["n_issue"] += 1
            key = "T_err" if not exact else "T_err_exact"
            st[key] = max(st.get(key, 0.0), abs(bf["T"] - fm["T"]))
            if abs(bf["T"] - fm["T"]) > tol_cmp:
                ex.setdefault("T", (par, bf, fm))
            # E's payoff: max{dRH - B1, -sig - rc} + [Q1-Dc]^+ + ValH(Q2-Dc)
            key = "E_err" if not exact else "E_err_exact"
            st[key] = max(st.get(key, 0.0), abs(bf["Epay"] - fm["Epay"]))
            if fm["B1"] == 0 and par["Q1"] >= 0 and par["u"] == 0:
                st["zero_bite_purchases"] += 1
            # (i): with v_c <= k, issuance needs dRU > 0 and B + dRU - dRH > sig + rc (brute-force quantities)
            if par["vc"] <= par["k"]:
                Bnum = bf["E0"] - bf["Eref"]
                dRU = bf["dRU"]
                if not (dRU > 1e-12 and Bnum + dRU - bf["dRH"] > par["sig"] + par["rc"] + 1e-12 - tol_cmp):
                    st["cor_i_viol"] += 1
                    ex.setdefault("cor_i", (par, bf, fm))
        # (ii) identity dRU - dRH = K_I [I(Q2) - I(Q2-Dc)] >= 0, and Gamma(with investment) >= Gamma(no investment)
        if bf["dRU"] is not None:
            ident = (bf["dRU"] - bf["dRH"]) - par["KI"] * (fm["I2"] - fm["I2c"])
            st["cor_ii_ident_err"] = max(st["cor_ii_ident_err"], abs(ident))
        p0 = dict(par, Ib=0.0)
        bf0 = solve(p0, h)
        if bf["Gnum"] < bf0["Gnum"] - tol_cmp:
            st["cor_ii_viol"] += 1
            ex.setdefault("cor_ii", (par, bf["Gnum"], bf0["Gnum"]))
        # alternative investment tie rule changes the answer?
        bft = solve(par, h, tie_invest=True)
        if bft["issue"] != bf["issue"]:
            st["tie_rule_diff"] += 1
            ex.setdefault("tie_rule", (par, bf["issue"], bft["issue"], formula(par, True)["G"]))
        # (iv) special case
        if par["vc"] == 0 and par["k"] == 0 and par["Dc"] == INF and par["Ib"] == 0 and par["Q1"] < 0:
            st["n_iv"] += 1
            Giv = min(par["d"] * pos(par["Q2"]), fm["B1"] - par["sig"] - par["rc"])
            st["cor_iv_err"] = max(st["cor_iv_err"], abs(Giv - bf["Gnum"]))

    for p in EDGE:
        st["n_edge"] += 1
        check(p, 1 / 64, True)
    for i in range(20000):
        st["n_exact"] += 1
        check(draw_exact(rng), 1 / 64, True)
    for i in range(10000):
        st["n_cont"] += 1
        check(draw_cont(rng), 1e-3, False)

    # (iii) monotonicity in Dc (brute-force Gamma over an increasing sequence of Dc)
    seq = [0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 9.0, INF]
    for i in range(3000):
        par = draw_exact(rng)
        prev = -INF
        st["n_iii"] += 1
        for Dc in seq:
            g = solve(dict(par, Dc=Dc), 1 / 64)["Gnum"]
            if g < prev - 1e-9:
                st["cor_iii_viol"] += 1
                ex.setdefault("cor_iii", (par, Dc, prev, g))
                break
            prev = g

    # alternative investment tie rule (invest when indifferent): formulas with the weak indicator
    alt_bad = 0
    for i in range(5000):
        par = draw_exact(rng)
        bf = solve(par, 1 / 64, tie_invest=True)
        fm = formula(par, tie_invest=True)
        if bf["issue"] != (fm["G"] > 1e-12) or abs(bf["Gnum"] - fm["G"]) > 1e-9 or (
                bf["issue"] and abs(bf["T"] - fm["T"]) > 1e-9):
            alt_bad += 1
    st["alt_tie_rule_mismatches_(5000)"] = alt_bad

    # does the credibility condition depend on Dc?  (cut decision after refusal, for each Dc)
    dep = 0
    for i in range(2000):
        par = draw_cont(rng)
        cuts = set()
        for Dc in seq[1:]:
            cuts.add(solve(dict(par, Dc=Dc), 1e-2)["cuts"])
        if len(cuts) > 1:
            dep += 1
    st["credibility_depends_on_Dc"] = dep

    print("Proposition 4 brute force vs memo formulas")
    for k_, v in st.items():
        print(f"  {k_}: {v}")
    for k_, v in ex.items():
        print("example", k_, v)
    # illustrative examples quoted in the report
    print("\nzero-bite purchase example (Q1=1, Q2=-0.5, Ibar=3, K_I=2, sigma=1, no threat):")
    p = EDGE[5]
    print("  brute force:", {k_: solve(p, 1 / 64)[k_] for k_ in ("issue", "T", "gain")}, " formula:", formula(p))


if __name__ == "__main__":
    main()
