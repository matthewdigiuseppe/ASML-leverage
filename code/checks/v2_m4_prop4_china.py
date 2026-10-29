"""v2 verifier m4: Proposition 4, corollary (v) (strategic Chinese punishment of a transfer).

Stage 0: China announces a punishment r in a grid on [0, rbar] and a stake m_C in {0, mbar_C}.
         Executing r after a transfer has ex post value -gam*r to China. The threat is credible iff
         China would execute: gam*r <= m_C (ties: execute). E and U see r_eff = r if credible, else 0.
Stage 1+: the two-period game of v2_m4_prop4.py, solved by brute force with r^c = r_eff.
After a transfer China executes iff -gam*r >= -m_C (forfeit otherwise).
China's payoff: H_C if E keeps control; if control is transferred: -gam*r if it executes, -m_C if not.
We compute ALL China-optimal announcements and check, in every such equilibrium:
  (a) a transfer that happens on path is never punished (when gam > 0);
  (b) a credible r > 0 is announced only if it deters (brute-force: U does not issue);
  (c) with H_C > 0 the transfer happens iff U would issue at r = 0 and U would still issue at the
      largest credible r, min{rbar, mbar_C/gam}; the payment on path is the r^c = 0 payment.
Variant gam < 0 (self-rewarding punishment) shows that (a) needs a negative ex post value.
Run: python3 -I v2_m4_prop4_china.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2_m4_prop4 import solve, formula, draw_exact, INF  # noqa: E402


def china_game(par, gam, HC, rbar, mbarC, h=1 / 64, step=0.5):
    rs = [i * step for i in range(int(rbar / step) + 1)]
    cache = {}
    outcomes = []
    for r in rs:
        for mC in (0.0, mbarC):
            cred = (gam * r <= mC + 1e-12)
            reff = r if cred else 0.0
            if reff not in cache:
                cache[reff] = solve(dict(par, rc=reff), h)
            bf = cache[reff]
            transfer = bool(bf["issue"] and bf["accepted"])
            if transfer:
                execute = (-gam * r >= -mC - 1e-12)
                pay = -gam * r if execute else -mC
            else:
                execute = False
                pay = HC
            outcomes.append(dict(r=r, mC=mC, cred=cred, reff=reff, transfer=transfer, punished=transfer and execute and r > 0,
                                 pay=pay, T=bf["T"] if transfer else None))
    best = max(o["pay"] for o in outcomes)
    return [o for o in outcomes if o["pay"] >= best - 1e-12], cache


def main():
    rng = random.Random(7)
    st = dict(n=0, n_HC0=0, a_viol=0, b_viol=0, c_viol=0, T_viol=0, transfers=0, deterred=0,
              n_neg=0, neg_punished_on_path=0)
    ex = {}
    for i in range(5000):
        par = draw_exact(rng)
        par["rc"] = 0.0
        gam = rng.choice([1.0, 0.5, 2.0])
        HC = rng.choice([0.0, 1.0, 0.25])
        rbar = float(rng.randint(0, 6))
        mbarC = float(rng.randint(0, 6))
        opt, cache = china_game(par, gam, HC, rbar, mbarC)
        st["n"] += 1
        st["n_HC0"] += HC == 0
        for o in opt:
            if o["punished"]:
                st["a_viol"] += 1
                ex.setdefault("a", (par, gam, HC, o))
            if o["cred"] and o["r"] > 0 and o["transfer"]:
                st["b_viol"] += 1
                ex.setdefault("b", (par, gam, HC, o))
        if HC == 0 and len(set(o["transfer"] for o in opt)) > 1:
            st["HC0_transfer_outcome_not_unique"] = st.get("HC0_transfer_outcome_not_unique", 0) + 1
        if HC > 0:
            rmax = min(rbar, mbarC / gam)
            # largest credible grid point
            rmax = max([r for r in [j * 0.5 for j in range(int(rbar / 0.5) + 1)] if gam * r <= mbarC + 1e-12])
            iss0 = solve(dict(par, rc=0.0), 1 / 64)["issue"]
            issm = solve(dict(par, rc=rmax), 1 / 64)["issue"]
            pred_transfer = bool(iss0 and issm)
            for o in opt:
                if o["transfer"] != pred_transfer:
                    st["c_viol"] += 1
                    ex.setdefault("c", (par, gam, HC, rbar, mbarC, o))
                if o["transfer"]:
                    if abs(o["T"] - formula(dict(par, rc=0.0))["T"]) > 1e-9:
                        st["T_viol"] += 1
            st["transfers"] += pred_transfer
            st["deterred"] += bool(iss0 and not issm)
        # variant: positive ex post value of punishing (gam < 0)
        optn, _ = china_game(par, -0.5, HC, rbar, mbarC)
        st["n_neg"] += 1
        if any(o["punished"] for o in optn):
            st["neg_punished_on_path"] += 1
            ex.setdefault("neg", (par, HC, rbar, [o for o in optn if o["punished"]][0]))
    print("Corollary (v): strategic Chinese counter-threat to a transfer")
    for k, v in st.items():
        print(f"  {k}: {v}")
    for k, v in ex.items():
        print("example", k, v)


if __name__ == "__main__":
    main()
