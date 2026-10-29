"""v2 Proposition 1 and Corollary 1 (master bargaining game): brute-force checks.

Game (memo v2, Section 3).  Rounds of length D.  E proposes w.p. beta, U otherwise.  The
responder accepts (flow P forever; normalized payoffs P to E, -P to U) or rejects.  After
rejecting a U offer, E may exit (Q to E, -V to U forever).  If there is no voluntary exit,
breakdown into exit occurs w.p. mu = 1 - exp(-lam D) immediately; otherwise the period's
status-quo flows (0, 0) accrue and the next round starts after discounting delta = exp(-r D).

Nothing below uses the claimed closed forms to compute equilibria.  Values are obtained by
backward induction (finite horizon, arbitrary terminal values) in which each proposer
compares every offer on a grid, plus the responder's indifference point, with the payoff of
making an unacceptable offer, and E compares exit with continuation.  The closed forms are
only used for comparison.

Sections
 A  discrete D: finite-horizon BI from random terminal values -> compare with x*(D)
 B  frequent-offer limit: BI at small D with Richardson extrapolation -> compare with P*
 C  Corollary 1 (a)-(e) and nesting, using the numerical limits
 D  SPE payoff uniqueness: (i) BI limits independent of terminal values, (ii) the
    Shaked-Sutton sup/inf bound maps iterated from wide boxes
 E  knife-edge lambda = 0: stationary SPE with delay (one-shot deviation check)
 F  alternative timing (E may also exit after U rejects E's demand): stationary value,
    and a nonstationary SPE giving E close to V (one-shot deviation check)
 G  rate of convergence near beta -> 1 and non-commuting limits
 H  negative P* (European concession) and P* >= Q
Run: python3 -I v2_m1_prop1.py   (about two minutes)
"""
import math
import random

import numpy as np


# ------------------------------------------------------------------------------------------
# closed forms (for comparison only)
# ------------------------------------------------------------------------------------------
def closed_x(Q, V, beta, lam, r, D):
    mu = 1 - math.exp(-lam * D)
    de = math.exp(-r * D)
    w = mu / (1 - de * (1 - mu))
    xA = w * (Q + beta * (V - Q))
    xB = ((1 - beta) * Q + beta * mu * V) / (1 - beta * de * (1 - mu))
    return max(xA, xB), xA, xB


def closed_P(Q, V, beta, lam, r):
    wb = lam / (lam + r)
    return max(Q, wb * (Q + beta * (V - Q)))


# ------------------------------------------------------------------------------------------
# one round of backward induction (base timing), continuation values (v, u) after a
# rejection without exit and without breakdown (u NOT assumed equal to -v)
# ------------------------------------------------------------------------------------------
def round_values(Q, V, beta, mu, k, v, u, grid=None, timing='base'):
    """Returns E's and U's round-start values plus diagnostics.
    timing='base': E may exit only after rejecting a U offer.
    timing='alt' : E may also exit right after U rejects E's demand (ties -> continue)."""
    cont_E = mu * Q + k * v          # E: rejection, no exit
    cont_U = mu * (-V) + k * u       # U: rejection, no exit
    # ---- U proposes ----
    exitE = Q > cont_E
    RE = Q if exitE else cont_E      # E's rejection value
    RU_rej = -V if exitE else cont_U  # U's payoff if its offer is rejected
    cands = [RE] if grid is None else np.concatenate([grid, [RE]])
    if grid is None:
        best_acc = -RE
    else:
        acc = cands[cands >= RE]
        best_acc = float(np.max(-acc))
    if best_acc >= RU_rej:
        eU, uU, delayU = -best_acc, best_acc, best_acc == RU_rej
    else:
        eU, uU, delayU = RE, RU_rej, True
    # ---- E proposes ----
    if timing == 'alt' and Q > cont_E:
        RUe = -V                     # U's rejection triggers exit
        E_rej = Q
    else:
        RUe = cont_U
        E_rej = cont_E
    thr = -RUe                       # U accepts iff P <= thr
    if grid is None:
        best_acc = thr
    else:
        c2 = np.concatenate([grid, [thr]])
        best_acc = float(np.max(c2[c2 <= thr]))
    if best_acc >= E_rej:
        eE, uE, delayE = best_acc, -best_acc, best_acc == E_rej
    else:
        eE, uE, delayE = E_rej, RUe, True
    v_new = beta * eE + (1 - beta) * eU
    u_new = beta * uE + (1 - beta) * uU
    return v_new, u_new, (delayU, delayE, exitE)


def solve_bi(Q, V, beta, lam, r, D, v0, u0, grid=None, timing='base', tol=1e-13,
             maxit=2_000_000):
    mu = 1 - math.exp(-lam * D)
    k = math.exp(-r * D) * (1 - mu)
    v, u = v0, u0
    for it in range(maxit):
        vn, un, diag = round_values(Q, V, beta, mu, k, v, u, grid, timing)
        if abs(vn - v) < tol and abs(un - u) < tol:
            return vn, un, diag, it
        v, u = vn, un
    return v, u, diag, maxit


def limit_value(Q, V, beta, lam, r, D1=0.004, timing='base'):
    """Second-order Richardson extrapolation of BI values at D1, D1/2, D1/4."""
    a = solve_bi(Q, V, beta, lam, r, D1, 0.0, 0.0, timing=timing)[0]
    b = solve_bi(Q, V, beta, lam, r, D1 / 2, 0.0, 0.0, timing=timing)[0]
    c = solve_bi(Q, V, beta, lam, r, D1 / 4, 0.0, 0.0, timing=timing)[0]
    return (8 * c - 6 * b + a) / 3, c


def draw(rng):
    V = rng.uniform(0.5, 5)
    Q = rng.uniform(-2 * V, 0.98 * V)
    beta = rng.choice([0.0, rng.uniform(0, 0.95)])
    lam = rng.choice([0.0, rng.uniform(0.05, 3), rng.uniform(0.05, 3)])
    r = rng.uniform(0.05, 2)
    return Q, V, beta, lam, r


def main():
    rng = random.Random(7)
    # ======================================================================================
    print("A. discrete D: BI with grid offers, random terminal values, vs x*(D) = max{xA, xB}")
    errs, n, uerr, delay_strict = [], 0, 0.0, 0
    for _ in range(250):
        Q, V, beta, lam, r = draw(rng)
        D = rng.choice([1.0, 0.5, 0.2, 0.1])
        grid = np.linspace(-3 * V, 3 * V, 601)
        for _t in range(2):
            v0 = rng.uniform(-3 * V, 3 * V)
            u0 = rng.uniform(-3 * V, 3 * V)
            v, u, diag, it = solve_bi(Q, V, beta, lam, r, D, v0, u0, grid=grid)
            x = closed_x(Q, V, beta, lam, r, D)[0]
            errs.append(abs(v - x))
            uerr = max(uerr, abs(u + v))
            if lam > 0 and (diag[0] or diag[1]):
                delay_strict += 1
            n += 1
    print(f"   runs={n}  max|v_BI - x*|={max(errs):.2e}  max|u_BI + v_BI|={uerr:.2e}  "
          f"runs where a proposer weakly preferred delay with lam>0: {delay_strict}")

    # ======================================================================================
    print("B. frequent-offer limit: Richardson-extrapolated BI (D = 0.004, 0.002, 0.001) vs P*")
    errs, n, worst = [], 0, None
    samples = []
    for _ in range(120):
        V = rng.uniform(0.5, 5)
        Q = rng.uniform(-2 * V, 0.98 * V)
        beta = rng.choice([0.0, rng.uniform(0, 0.9)])
        lam = rng.choice([0.0, rng.uniform(0.3, 3), rng.uniform(0.3, 3)])
        r = rng.uniform(0.3, 2)
        P_num, _ = limit_value(Q, V, beta, lam, r)
        P = closed_P(Q, V, beta, lam, r)
        e = abs(P_num - P)
        errs.append(e)
        samples.append((Q, V, beta, lam, r, P_num))
        if worst is None or e > worst[0]:
            worst = (e, Q, V, beta, lam, r)
        n += 1
    print(f"   draws={n}  max|P_num - P*|={max(errs):.2e}  (worst at Q,V,beta,lam,r="
          f"{tuple(round(z, 3) for z in worst[1:])})")

    # ======================================================================================
    print("C. Corollary 1, using the numerical limits from B")
    tol = 2e-3
    a_fail = sum(1 for (Q, V, b, l, r, P) in samples if P < Q - tol)
    print(f"   (a) P* >= Q: violations {a_fail} / {len(samples)}")
    bl = [(Q, P) for (Q, V, b, l, r, P) in samples if l == 0]
    b_fail = sum(1 for (Q, P) in bl if abs(P - max(Q, 0)) > tol)
    print(f"   (b) lam = 0 -> P* = [Q]^+: violations {b_fail} / {len(bl)}")
    b0 = [(Q, l, r, P) for (Q, V, b, l, r, P) in samples if b == 0]
    b0_fail = sum(1 for (Q, l, r, P) in b0 if abs(P - max(Q, l / (l + r) * Q)) > tol)
    thr_fail = sum(1 for (Q, l, r, P) in b0 if Q <= 0 and P > tol)
    print(f"   (b) beta = 0 -> P* = max(Q, w_b Q): violations {b0_fail} / {len(b0)}; "
          f"Q<=0 but P*>0: {thr_fail}")
    c_fail = 0
    for (Q, V, b, l, r, P) in samples:
        pred = (Q > 0) or (l > 0 and Q + b * (V - Q) > 0)
        if abs(P) > tol and (P > 0) != pred:
            c_fail += 1
    print(f"   (c) sign of P*: violations {c_fail} / {len(samples)} (|P*| > tol)")
    # (d) dP*/dV holding Q fixed, by finite differences of numerical limits
    d_err, d_n = 0.0, 0
    for _ in range(25):
        V = rng.uniform(1, 4)
        Q = rng.uniform(-V, 0.3 * V)
        beta = rng.uniform(0.2, 0.9)
        lam = rng.uniform(0.5, 3)
        r = rng.uniform(0.3, 1.5)
        wb = lam / (lam + r)
        if not wb * (Q + beta * (V - Q)) > Q + 0.05:
            continue
        h = 0.05
        p1, _ = limit_value(Q, V + h, beta, lam, r)
        p0, _ = limit_value(Q, V - h, beta, lam, r)
        d_err = max(d_err, abs((p1 - p0) / (2 * h) - beta * wb))
        d_n += 1
    print(f"   (d) dP*/dV|_Q = beta w_b where the second term binds: draws={d_n}, "
          f"max err={d_err:.2e}")
    # regime threshold Qhat = lam beta V/(r + lam beta)
    reg_fail = 0
    for (Q, V, b, l, r, P) in samples:
        Qh = l * b * V / (r + l * b) if (r + l * b) > 0 else 0
        sec = (l / (l + r)) * (Q + b * (V - Q))
        if abs(Q - Qh) > 1e-2 and ((Q < Qh) != (sec > Q)):
            reg_fail += 1
    print(f"   second term binds iff Q < lam beta V/(r + lam beta): violations {reg_fail}")
    # nesting
    Q, V, beta = 0.4, 2.0, 0.35
    for lam in [0.5, 2.0]:
        vals = [limit_value(Q, V, beta, lam, r, D1=0.01)[0] for r in [0.05, 0.02, 0.01]]
        print(f"   nesting r->0 (lam={lam}): P_num at r=.05,.02,.01 = "
              f"{[round(x, 4) for x in vals]}  target Q+beta(V-Q) = {Q + beta * (V - Q):.4f}")
    for (b, l) in [(0.9, 20.0), (0.99, 200.0), (0.999, 2000.0)]:
        Dl = 0.05 / l
        P_num = limit_value(Q, V, b, l, 0.5, D1=Dl)[0]
        print(f"   nesting beta->1, lam->inf: beta={b}, lam={l}: P_num={P_num:.4f}  (V = {V})")
    for (Qq, lam) in [(0.5, 0.0), (-0.5, 0.0)]:
        print(f"   nesting lam=0, Q={Qq}: P_num={limit_value(Qq, V, 0.5, lam, 0.5)[0]:.4f} "
              f"(target [Q]^+ = {max(Qq, 0)})")

    # ======================================================================================
    print("D. SPE payoff uniqueness")
    spread = 0.0
    for _ in range(60):
        Q, V, beta, lam, r = draw(rng)
        D = rng.choice([0.5, 0.2, 0.1])
        ends = [(V, -V), (min(Q, 0), 0.0), (-3 * V, 3 * V), (3 * V, 3 * V), (Q, -V),
                (rng.uniform(-5, 5), rng.uniform(-5, 5))]
        vals = [solve_bi(Q, V, beta, lam, r, D, a, b)[0] for (a, b) in ends]
        spread = max(spread, max(vals) - min(vals))
    print(f"   (i) BI limits over 6 terminal conditions (incl. infeasible ones): max spread "
          f"= {spread:.2e}")
    # (ii) sup/inf maps of the proof (M, m: sup/inf E payoff; Uh, Ul: sup/inf U payoff)
    worst = 0.0
    for _ in range(300):
        Q, V, beta, lam, r = draw(rng)
        D = rng.choice([1.0, 0.5, 0.2, 0.1])
        mu = 1 - math.exp(-lam * D)
        k = math.exp(-r * D) * (1 - mu)
        g = lambda z: max(Q, mu * Q + k * z)
        M, m, Uh, Ul = 10 * V, -10 * V, 10 * V, -10 * V
        for _it in range(200000):
            Uh_new = min(Uh, -m)                       # total payoff <= 0
            # E's payoff bounds
            M_new = beta * (mu * V - k * Ul) + (1 - beta) * g(M)
            m_new = beta * (mu * V - k * Uh_new) + (1 - beta) * g(m)
            Ul_new = beta * (-mu * V + k * Ul) + (1 - beta) * (-g(M))
            M_new, m_new = min(M, M_new), max(m, m_new)
            Ul_new = max(Ul, Ul_new)
            if max(abs(M_new - M), abs(m_new - m), abs(Ul_new - Ul), abs(Uh_new - Uh)) < 1e-13:
                break
            M, m, Uh, Ul = M_new, m_new, Uh_new, Ul_new
        x = closed_x(Q, V, beta, lam, r, D)[0]
        worst = max(worst, abs(M - x), abs(m - x), abs(Uh + x), abs(Ul + x))
    print(f"   (ii) sup/inf bound maps from the box [-10V,10V]^2: max distance of "
          f"(M, m, -Uh, -Ul) from x* = {worst:.2e}")

    # ======================================================================================
    print("E. lam = 0 knife-edge: stationary SPE with delay (one-shot deviation check)")
    for (Q, V, beta, r, D) in [(0.6, 2.0, 0.4, 0.5, 0.2), (-0.5, 2.0, 0.4, 0.5, 0.2)]:
        de = math.exp(-r * D)
        # profile: E always demands P = 10V (rejected); U offers max(Q, de x); exit iff Q > de x
        # value: x = beta*de*x + (1-beta)*max(Q, de*x)
        x = 0.0
        for _ in range(100000):
            x = beta * de * x + (1 - beta) * max(Q, de * x)
        u = -x
        # one-shot deviations (grid of offers)
        G = np.linspace(-5 * V, 5 * V, 2001)
        # E proposing: profile payoff = de*x (rejected demand, continuation); deviation: any
        # demand P accepted iff -P >= de*u, i.e. P <= de*x
        prof = de * x
        dev = max(G[G <= de * x].max(initial=-1e9), de * x)
        okE = dev <= prof + 1e-12
        # U proposing: offer max(Q, de x) accepted; deviation to unacceptable offer gives
        # -V if E exits else de*u
        RE = max(Q, de * x)
        dev_U = (-V if Q > de * x else de * u)
        okU = dev_U <= -RE + 1e-12
        print(f"   Q={Q}: value x={x:.4f} (base-game x*={closed_x(Q, V, beta, 0.0, r, D)[0]:.4f}); "
              f"E indifferent between acceptable and rejected demand: {okE}; U no deviation: {okU};"
              f" delay prob per round = beta = {beta}")

    # ======================================================================================
    print("F. alternative timing (exit also after U rejects E's demand)")
    # stationary SPE: find v with v in T'(v) by bisection on the sign of T'(v) - v (u = -v)
    def Tprime(Q, V, beta, mu, k, v, p=None):
        cont = mu * Q + k * v
        PU = max(Q, cont)
        if Q > cont:
            PE = V
        elif Q < cont:
            PE = mu * V + k * v
        else:
            PE = p * V + (1 - p) * (mu * V + k * v)
        return beta * PE + (1 - beta) * PU

    def x_alt_closed(Q, V, beta, lam, r, D):
        mu = 1 - math.exp(-lam * D)
        de = math.exp(-r * D)
        w = mu / (1 - de * (1 - mu))
        xA = w * (Q + beta * (V - Q))
        xBp = beta * V + (1 - beta) * Q
        if de * xA >= Q:
            return xA
        return min(xBp, Q / de)

    errs, mixing_cases, n = [], 0, 0
    osd_fail, osd_n, high_vals = 0, 0, []
    for _ in range(300):
        Q, V, beta, lam, r = draw(rng)
        if beta == 0:
            beta = rng.uniform(0.05, 0.95)
        D = rng.choice([0.5, 0.2, 0.05, 0.01])
        mu = 1 - math.exp(-lam * D)
        k = math.exp(-r * D) * (1 - mu)
        lo, hi = -10 * V, 10 * V
        f = lambda v: Tprime(Q, V, beta, mu, k, v, 0.5) - v
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                lo = mid
            else:
                hi = mid
        v_st = (lo + hi) / 2
        # mixing equilibrium: jump straddles zero
        eps = 1e-9 * max(1, abs(v_st))
        if f(v_st - eps) > 1e-7 and f(v_st + eps) < -1e-7:
            mixing_cases += 1
        errs.append(abs(v_st - x_alt_closed(Q, V, beta, lam, r, D)))
        n += 1
        # nonstationary high SPE: state H (E demands V; after U rejects, E exits;
        # after E rejects U's offer, stay in H), punishment state L = stationary SPE
        de = math.exp(-r * D)
        vL = v_st
        if vL <= Q / de + 1e-12 and Q > 0:
            vH = (beta * V + (1 - beta) * mu * Q) / (1 - (1 - beta) * k)
            PUH = max(Q, mu * Q + k * vH)
            vH = beta * V + (1 - beta) * PUH
            for _ in range(10000):
                PUH = max(Q, mu * Q + k * vH)
                vH = beta * V + (1 - beta) * PUH
            uH = -vH
            G = np.linspace(-3 * V, 3 * V, 1201)
            ok = True
            # E proposing in H: demand P<=V accepted; P>V rejected -> exit (Q) or continue to L
            best_dev = max(G[G <= V].max(), max(Q, mu * Q + k * vL))
            ok &= best_dev <= V + 1e-9
            # U responding to V: accept -V; reject -> E exits -> -V
            ok &= -V >= -V
            # E's exit after U's rejection: Q >= mu Q + k vL
            ok &= Q >= mu * Q + k * vL - 1e-9
            # U proposing in H: offer PUH accepted; lower offer -> E rejects; E exits iff
            # Q > mu Q + k vH; else continuation in H for U: -mu V + k uH
            dev_U = -V if Q > mu * Q + k * vH else -mu * V + k * uH
            ok &= dev_U <= -PUH + 1e-9
            # E responding to U's offer P: accepts iff P >= max(Q, mu Q + k vH) (by construction)
            osd_n += 1
            osd_fail += (not ok)
            high_vals.append((D, Q, V, beta, lam, r, vL, vH))
    print(f"   stationary value: draws={n}, max|v_bisection - x'| (x' = xA if delta xA >= Q, else min{{xB', Q/delta}})="
          f"{max(errs):.2e}; mixing equilibria found: {mixing_cases}")
    print(f"   nonstationary 'high' SPE (E demands V): constructed in {osd_n} draws, "
          f"one-shot-deviation failures {osd_fail}")
    ex = [h for h in high_vals if h[0] == 0.01][:4]
    for (D, Q, V, beta, lam, r, vL, vH) in ex:
        print(f"      D={D}: Q={Q:.3f} V={V:.3f} beta={beta:.3f} lam={lam:.3f} r={r:.3f}: "
              f"stationary {vL:.4f} (P*={closed_P(Q, V, beta, lam, r):.4f}), high SPE {vH:.4f}")
    # frequent-offer limit of the alternative-timing stationary value equals P*
    errs = []
    for _ in range(200):
        Q, V, beta, lam, r = draw(rng)
        D = 1e-5
        errs.append(abs(x_alt_closed(Q, V, beta, lam, r, D) - closed_P(Q, V, beta, lam, r)))
    print(f"   limit of alternative-timing stationary value vs P* (D=1e-5): max diff "
          f"{max(errs):.2e}")
    # without exit regime (Q < Qhat): no SPE can make exit credible -> unique
    # (illustrated by the sup/inf bound: inf E payoff >= x* > Q/delta)

    # ======================================================================================
    print("G. convergence near beta -> 1 (Q = 1.5, V = 2, lam = r = 1, so w_b V = 1 < Q)")
    Q, V, lam, r = 1.5, 2.0, 1.0, 1.0
    for beta in [0.9, 0.99, 0.999]:
        row = []
        for D in [1e-2, 1e-3, 1e-4]:
            x = solve_bi(Q, V, beta, lam, r, D, 0.0, 0.0)[0]
            approx = beta * (r + lam) * D * (Q - lam / (lam + r) * V) / ((1 - beta) + beta * (r + lam) * D)
            row.append(f"D={D:g}: P*-x={closed_P(Q, V, beta, lam, r) - x:.4f} (approx {approx:.4f})")
        print(f"   beta={beta}: " + "; ".join(row))
    print(f"   beta = 1 exactly (any D): x = w V -> w_b V = {lam / (lam + r) * V} < Q = {Q}: "
          f"lim_beta->1 P* = max(Q, w_b V) = {max(Q, lam / (lam + r) * V)}  (limits do not commute)")

    # ======================================================================================
    print("H. negative P* and P* >= Q")
    Q, V, beta, lam, r = -1.0, 1.0, 0.25, 1.0, 1.0
    Pn = limit_value(Q, V, beta, lam, r)[0]
    print(f"   Q={Q}, V={V}, beta={beta}, lam=r=1: P_num={Pn:.4f}, P*={closed_P(Q, V, beta, lam, r):.4f}"
          f" (< 0: E concedes; concession {-Pn:.4f} <= slack {-Q})")
    m = 1e9
    for _ in range(200000):
        Q, V, beta, lam, r = draw(rng)
        m = min(m, closed_P(Q, V, beta, lam, r) - Q)
    print(f"   min over 200000 draws of P* - Q (closed form) = {m:.3e}")


if __name__ == '__main__':
    main()
