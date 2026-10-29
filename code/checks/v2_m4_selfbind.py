"""v2 verifier m4: remark on self-binding vs dual key.

Stage 0: E chooses whether to bind. Binding lowers E's premium at both dates by Delta_b (E keeps the
key), costs sigma^b and draws a Chinese punishment r^b (taken as given). Then the two-period game of
v2_m4_prop4.py is solved by brute force with premia Q_t - Delta_b; the bite of U's threat is
recomputed from primitives (it depends on E's slack, which binding raises).
Checks:
  (1) Delta_b = inf: binding pre-empts the ultimatum iff v_c <= k or v_c - k + u + dd <= sigma + r^c
      (credible threat after binding iff g <= mbar_U); i.e. iff Gamma after binding <= 0.
  (2) Memo comparison (Q1 < 0, Delta_c = inf, Ibar = 0, Delta_b = inf):
      E strictly prefers to bind iff -sigma^b - r^b > max{delta[Q2]^+ - B1, -sigma - r^c}.
      Revised: compare -sigma^b - r^b - 1{not pre-empted} min{sigma + r^c, B1^b} with E's no-binding
      payoff, which is max{delta[Q2]^+ - B1, -sigma - r^c} if Gamma > 0 and delta[Q2]^+ otherwise.
  (3) Partial binding (finite Delta_b) can INVITE an ultimatum (Gamma rises because slack raises the bite).
  (4) Dual key: U chooses among full control (Dc = inf, sigma) and a dual-key arrangement
      (Dc = Delta_d, sigma_d < sigma, v_d); it demands the arrangement with the larger positive Gamma.
Run: python3 -I v2_m4_selfbind.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2_m4_prop4 import solve, formula, draw_exact, INF, pos  # noqa: E402

H = 1 / 64


def shifted(par, Db):
    return dict(par, Q1=par["Q1"] - Db, Q2=par["Q2"] - Db)


def main():
    rng = random.Random(99)
    st = dict(n=0, preempt_mis=0, memo_mis=0, memo_mis_when_Gamma_pos_and_preempt=0, revised_mis=0,
              partial_invites=0, n_partial=0, dual_mis=0, n_dual=0, dual_chosen=0)
    ex = {}
    for i in range(6000):
        par = draw_exact(rng)
        par.update(Dc=INF, Ib=0.0)
        if par["Q1"] >= 0:
            par["Q1"] = -float(rng.randint(1, 6))
        sb = float(rng.randint(0, 3))
        rb = float(rng.choice([0, rng.randint(0, 2)]))
        st["n"] += 1
        # brute force: no binding
        bf_n = solve(par, H)
        E_n = bf_n["Epay"]
        # binding with Delta_b = inf
        pb = shifted(par, INF)
        bf_b = solve(pb, H)
        E_b = bf_b["Epay"] - sb - rb
        # (1) pre-emption
        cred_b = par["g"] <= par["mbar"]
        Bb = par["u"] + par["dd"] if cred_b else 0.0
        preempt_pred = (par["vc"] <= par["k"]) or (par["vc"] - par["k"] + Bb <= par["sig"] + par["rc"])
        if preempt_pred == bool(bf_b["issue"]):
            st["preempt_mis"] += 1
            ex.setdefault("preempt", (par, bf_b["issue"]))
        # (2) memo statement
        fm = formula(par)
        prefers_bind = E_b > E_n + 1e-12
        memo = -sb - rb > max(par["d"] * pos(par["Q2"]) - fm["B1"], -par["sig"] - par["rc"]) + 1e-12
        if memo != prefers_bind:
            st["memo_mis"] += 1
            ex.setdefault("memo", (par, sb, rb, E_n, E_b))
            if fm["G"] > 0 and preempt_pred:
                st["memo_mis_when_Gamma_pos_and_preempt"] += 1
        E_n_rev = (max(par["d"] * pos(par["Q2"]) - fm["B1"], -par["sig"] - par["rc"]) if fm["G"] > 1e-12
                   else par["d"] * pos(par["Q2"]))
        E_b_rev = -sb - rb - (0.0 if preempt_pred else min(par["sig"] + par["rc"], Bb))
        if (E_b_rev > E_n_rev + 1e-12) != prefers_bind:
            st["revised_mis"] += 1
            ex.setdefault("revised", (par, sb, rb, E_n, E_b, E_n_rev, E_b_rev))
        # (3) partial binding
        Db = float(rng.randint(1, 5))
        st["n_partial"] += 1
        if (not bf_n["issue"]) and solve(shifted(par, Db), H)["issue"]:
            st["partial_invites"] += 1
            ex.setdefault("partial", (par, Db))
        # (4) dual key
        Dd = float(rng.randint(1, 4))
        sd = float(rng.randint(0, int(par["sig"]))) if par["sig"] >= 1 else 0.0
        vd = float(rng.randint(0, int(par["vc"]))) if par["vc"] >= 1 else 0.0
        full = solve(par, H)
        dual_par = dict(par, Dc=Dd, sig=sd, vc=vd)
        dual = solve(dual_par, H)
        st["n_dual"] += 1
        # U's brute-force choice among the two arrangements and no ultimatum
        opts = [(0.0, "none"), (full["gain"] if full["issue"] else -INF, "full"), (dual["gain"] if dual["issue"] else -INF, "dual")]
        choice = max(opts, key=lambda x: (x[0], x[1] == "none"))[1]
        Gf, Gd = formula(par)["G"], formula(dual_par)["G"]
        pred = "none" if max(Gf, Gd) <= 1e-12 else ("full" if Gf >= Gd else "dual")
        if choice != pred and not (abs(Gf - Gd) < 1e-12 and choice in ("full", "dual")):
            st["dual_mis"] += 1
            ex.setdefault("dual", (par, Dd, sd, vd, Gf, Gd, choice))
        st["dual_chosen"] += choice == "dual"
    print("Remark (self-binding vs dual key)")
    for k, v in st.items():
        print(f"  {k}: {v}")
    for k, v in ex.items():
        print("example", k, v)
    # hand-picked: partial binding invites an ultimatum
    par = dict(d=1.0, Q1=-1.0, Q2=10.0, Dc=INF, vc=0.0, k=0.0, sig=1.5, rc=0.0, Ib=0.0, KI=0.0,
               u=0.0, dd=5.0, g=0.0, mbar=8.0)
    print("hand-picked: no binding:", {k: solve(par, H)[k] for k in ("issue", "Epay")},
          " binding Delta_b=3:", {k: solve(shifted(par, 3.0), H)[k] for k in ("issue", "T", "Epay")})


if __name__ == "__main__":
    main()
