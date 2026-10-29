"""v2 verifier m4: lemma on multi-period cuts and the N-period windows corollary.

PART A (lemma). Dates s = 1..N with premia Q_s, U's value V_s, cap mbar_U. A cut over a set S of dates
withdraws at each s in S an instrument bundle with unconditional part u_s, conditional part d_s and
direct ex post cost g_s >= 0. Each date has its own static contest (Lemma 1): with premium p, E's
payoff above its aligned baseline is [min{p, V_s, mbar_U}]^+ (U pays [p]^+ when p < V_s, p <= mbar_U).
We compute E's loss and U's extra cost by direct comparison of the two paths and compare with
  bite = sum_s delta^{s-1} (u_s + min{d_s, Lambda_s}),   extra rent = sum_s delta^{s-1}([Q_s+d_s]^+ - [Q_s]^+).
We also show that the formula needs Q_s + d_s <= min{V_s, mbar_U} and no investment response.

PART B (windows). N = 2..6 dates, Delta_c = infinity, v_c = 0, issuing cost k (k = 0 with strict
issuing, and k = 1e-9 exactly). At any date t at which E still holds control U may issue an
ultimatum: transfer control for all remaining dates for T >= 0, or a date-t cut (u_t, d_t, g_t)
backed by a stake m in {0, mbar_U}. E accepts iff it weakly gains. After a refusal U executes the cut
iff its ex post payoff is weakly higher; the game continues at t+1 with E in control (repeated
ultimatums allowed). Exact rational arithmetic (fractions). We compare "U issues on path" with
  memo   : exists t with credible cut, b_t > sigma + r^c, and t' >  t with Q_t' > 0;
  revised: exists t with credible cut, b_t > sigma + r^c, and t' >= t with Q_t' > 0,
with b_t = u_t + min{d_t, [-Q_t]^+}.
Run: python3 -I v2_m4_cuts_windows.py
"""
import random
from fractions import Fraction as Fr


def pos(x):
    return x if x > 0 else 0 * x


# ----------------------------------------------------------------------------- part A
def static_E(p, V, mbar):
    return pos(min(p, V, mbar))


def part_A(rng, n=20000):
    st = dict(n=0, n_in_scope=0, bite_err=0.0, rent_err=0.0, out_scope=0, out_scope_bite_larger=0,
              ext_nonneg_Q_extra_bite_minus_u=0.0, ext_nonneg_Q_cost_minus_d=0.0)
    for _ in range(n):
        N = rng.randint(1, 5)
        d = rng.choice([1.0, rng.uniform(0.3, 1)])
        Q = [rng.uniform(-5, 4) for _ in range(N)]
        u = [rng.choice([0.0, rng.uniform(0, 2)]) for _ in range(N)]
        dd = [rng.uniform(0, 5) for _ in range(N)]
        V = [rng.uniform(2, 12) for _ in range(N)]
        mbar = rng.uniform(1, 15)
        S = [s for s in range(N) if rng.random() < 0.6]
        st["n"] += 1
        Eloss = 0.0
        Ucost = 0.0
        in_scope = True
        for s in range(N):
            w = d ** s
            base = static_E(Q[s], V[s], mbar)
            if s in S:
                cut = -(u[s] + dd[s]) + static_E(Q[s] + dd[s], V[s], mbar)
                if Q[s] + dd[s] >= min(V[s], mbar) or Q[s] >= min(V[s], mbar):
                    in_scope = False
                Eloss += w * (base - cut)
                Ucost += w * (pos(Q[s] + dd[s]) - pos(Q[s]))
        bite_f = sum(d ** s * (u[s] + min(dd[s], pos(-Q[s]))) for s in S)
        rent_f = sum(d ** s * (pos(Q[s] + dd[s]) - pos(Q[s])) for s in S)
        if in_scope:
            st["n_in_scope"] += 1
            st["bite_err"] = max(st["bite_err"], abs(Eloss - bite_f))
            st["rent_err"] = max(st["rent_err"], abs(Ucost - rent_f))
            # extension into a date with Q_s >= 0
            for s in S:
                if Q[s] >= 0:
                    one_cut = -(u[s] + dd[s]) + static_E(Q[s] + dd[s], V[s], mbar)
                    st["ext_nonneg_Q_extra_bite_minus_u"] = max(st["ext_nonneg_Q_extra_bite_minus_u"],
                                                                abs((static_E(Q[s], V[s], mbar) - one_cut) - u[s]))
                    st["ext_nonneg_Q_cost_minus_d"] = max(st["ext_nonneg_Q_cost_minus_d"],
                                                          abs(pos(Q[s] + dd[s]) - pos(Q[s]) - dd[s]))
        else:
            st["out_scope"] += 1
            if Eloss > bite_f + 1e-9:
                st["out_scope_bite_larger"] += 1
    # investment response example: Q2=-1, d2=1, Ibar=3, K_I=2.5, delta=1
    def valH(q, Ib=3.0, KI=2.5):
        return max(pos(q), pos(q + Ib) - KI)
    inv_bite = valH(-1.0) - (-(0 + 1.0) + valH(-1.0 + 1.0))
    st["investment_example_bite_(formula_1.0)"] = inv_bite
    return st


# ----------------------------------------------------------------------------- part B
def solve_windows(Q, u, dd, g, mbar, c0, d, k):
    """Backward induction; returns (on-path issue date or None, VU, VE)."""
    N = len(Q)
    VU, VE = Fr(0), Fr(0)
    plan = [False] * N
    for t in range(N - 1, -1, -1):
        U_no = -pos(Q[t]) + d * VU
        E_no = pos(Q[t]) + d * VE
        best_iss = None
        for m in (Fr(0), mbar):
            Ucut = -g[t] - pos(Q[t] + dd[t]) + d * VU
            Unc = -m - pos(Q[t]) + d * VU
            cut = Ucut >= Unc
            Eref = (-(u[t] + dd[t]) + pos(Q[t] + dd[t]) if cut else pos(Q[t])) + d * VE
            Uref = Ucut if cut else Unc
            T = pos(Eref + c0)                         # least T that E accepts (E accepts iff T - c0 >= Eref)
            for (Uo, Eo) in ((-k - T, T - c0), (-k + Uref, Eref)):   # accepted offer / refused offer
                if best_iss is None or Uo > best_iss[0]:
                    best_iss = (Uo, Eo, (Uo, Eo) == (-k - T, T - c0))
        if best_iss[0] > U_no:
            VU, VE = best_iss[0], best_iss[1]
            plan[t] = best_iss[2]
            if not best_iss[2]:
                raise RuntimeError("refused ultimatum strictly optimal")
        else:
            VU, VE = U_no, E_no
    path = next((t for t in range(N) if plan[t]), None)
    return path, VU, VE


def eligible(Q, u, dd, g, mbar, c0, strict_later):
    N = len(Q)
    out = []
    for t in range(N):
        e = g[t] + pos(Q[t] + dd[t]) - pos(Q[t])
        b = u[t] + min(dd[t], pos(-Q[t]))
        later = range(t + 1, N) if strict_later else range(t, N)
        if e <= mbar and b > c0 and any(Q[s] > 0 for s in later):
            out.append(t)
    return out


def part_B(rng, n=60000):
    st = dict(n=0, n_with_u=0, memo_mis=0, memo_mis_u0=0, revised_mis_k0=0, revised_mis_ktiny=0,
              k0_vs_ktiny_differ=0, issued=0, issued_outside_window=0, issued_at_last_eligible=0)
    ex = {}
    for i in range(n):
        N = rng.randint(2, 6)
        Q = [Fr(rng.randint(-6, 4)) for _ in range(N)]
        with_u = rng.random() < 0.4
        u = [Fr(rng.choice([0, rng.randint(0, 4)])) if with_u else Fr(0) for _ in range(N)]
        dd = [Fr(rng.randint(0, 5)) for _ in range(N)]
        g = [Fr(rng.randint(0, 3)) for _ in range(N)]
        mbar = Fr(rng.randint(0, 8))
        c0 = Fr(rng.randint(0, 4), rng.choice([1, 2]))
        d = rng.choice([Fr(1), Fr(1, 2), Fr(9, 10)])
        st["n"] += 1
        st["n_with_u"] += with_u
        p0, _, _ = solve_windows(Q, u, dd, g, mbar, c0, d, Fr(0))
        pk, _, _ = solve_windows(Q, u, dd, g, mbar, c0, d, Fr(1, 10 ** 9))
        if (p0 is None) != (pk is None):
            st["k0_vs_ktiny_differ"] += 1
        el_m = eligible(Q, u, dd, g, mbar, c0, True)
        el_r = eligible(Q, u, dd, g, mbar, c0, False)
        if (p0 is not None) != (len(el_m) > 0):
            st["memo_mis"] += 1
            if not with_u:
                st["memo_mis_u0"] += 1
            ex.setdefault("memo", (Q, u, dd, g, mbar, c0, d, p0, el_m, el_r))
        if (p0 is not None) != (len(el_r) > 0):
            st["revised_mis_k0"] += 1
            ex.setdefault("revised", (Q, u, dd, g, mbar, c0, d, p0, el_r))
        if (pk is not None) != (len(el_r) > 0):
            st["revised_mis_ktiny"] += 1
        if p0 is not None:
            st["issued"] += 1
            if p0 not in el_r:
                st["issued_outside_window"] += 1
            if el_r and p0 == el_r[-1]:
                st["issued_at_last_eligible"] += 1
    return st, ex


def main():
    rng = random.Random(4242)
    print("PART A: multi-period cuts")
    for k, v in part_A(rng).items():
        print(f"  {k}: {v}")
    print("PART B: windows corollary")
    st, ex = part_B(rng)
    for k, v in st.items():
        print(f"  {k}: {v}")
    for k, v in ex.items():
        print("example", k, [str(x) if not isinstance(x, list) else [str(y) for y in x] for x in v])
    # hand-picked: unconditional bite while Q_t > 0 and no later rents
    Q = [Fr(1), Fr(-5)]
    print("hand-picked (Q=(1,-5), u=(3,0), d=0, sigma+r^c=1):",
          solve_windows(Q, [Fr(3), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(0)], Fr(0), Fr(1), Fr(1), Fr(1, 10 ** 9))[0],
          "memo eligible:", eligible(Q, [Fr(3), Fr(0)], [Fr(0)] * 2, [Fr(0)] * 2, Fr(0), Fr(1), True))


if __name__ == "__main__":
    main()
