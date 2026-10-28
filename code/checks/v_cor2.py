"""Brute-force check of Corollary 2 (windows) in a T-period version, T = 2..6.

Game: at each date t with Europe in control, the US may issue a (public) ultimatum:
transfer control for all remaining dates for payment T_t >= 0. If accepted: E gets T - sig - rc,
U gets -T, game ends (normalized zeros afterwards). If refused, US decides whether to cut AI in
period t only (credible iff mbar + gN_t >= [Q_t+a_t]^+ - [Q_t]^+). Period-t static payoffs:
  no cut : E +[Q_t]^+,             U -[Q_t]^+
  cut    : E [Q_t+a_t]^+ - a_t,     U gN_t - [Q_t+a_t]^+
then date t+1 (discount d).

Three solution concepts:
  P : paper's implicit convention: US issues only if strictly better, cuts iff credible (>=),
      Europe accepts at indifference.
  M : Markov SPE set: at every tie, both actions admissible; continuation selection depends only
      on the state (same continuation after no-issue and after refusal).
  N : full SPE set: continuation selection may differ after no-issue / refusal-cut / refusal-nocut.
Corollary claim: an ultimatum is issued (on path) at some date iff there is an eligible date t
(cut credible at t, b_t > sig+rc, and Q_s > 0 for some s > t).
"""
import random, itertools, sys

def pos(x):
    return x if x > 0 else 0.0

EPS = 1e-9

def bite(Q, a):
    return min(a, pos(-Q))

def solve_P(par):
    Q, A, G, mbar, sig, rc, d = par
    T = len(Q)
    # value from date t (t index 0..T-1), E in control, no ultimatum issued yet
    VU, VE = 0.0, 0.0
    first_issue = None
    issue_dates = []
    for t in reversed(range(T)):
        Delta = pos(Q[t] + A[t]) - pos(Q[t])
        cred = mbar + G[t] >= Delta - 1e-12
        U0 = -pos(Q[t]) + d * VU
        E0 = pos(Q[t]) + d * VE
        if cred:
            Eref = pos(Q[t] + A[t]) - A[t] + d * VE
        else:
            Eref = E0
        Tst = pos(Eref + sig + rc)
        Uiss = -Tst
        if Uiss > U0 + EPS:
            VU, VE = Uiss, Tst - sig - rc
            issue_dates.append(t)
            first_issue = t
        else:
            VU, VE = U0, E0
            if first_issue is not None and first_issue > t:
                pass
    # on path: the earliest date at which the US issues (backward-induction plan), path stops there
    path_issue = min(issue_dates) if issue_dates else None
    return path_issue, VU, VE

def eligible_dates(par):
    Q, A, G, mbar, sig, rc, d = par
    T = len(Q)
    el = []
    for t in range(T):
        Delta = pos(Q[t] + A[t]) - pos(Q[t])
        cred = mbar + G[t] >= Delta - 1e-12
        if cred and bite(Q[t], A[t]) > sig + rc + 1e-12 and any(Q[s] > 0 for s in range(t + 1, T)):
            el.append(t)
    return el

def solve_set(par, markov=True, cap=400):
    """Return set of SPE outcomes from date 0: tuples (U, E, issued_on_path(bool), issue_date)."""
    Q, A, G, mbar, sig, rc, d = par
    T = len(Q)
    S = {(0.0, 0.0, None)}  # continuation set from date T
    for t in reversed(range(T)):
        Delta = pos(Q[t] + A[t]) - pos(Q[t])
        thr = Delta - G[t]
        newS = set()
        Slist = list(S)
        if markov:
            combos = [(c, c, c) for c in Slist]
        else:
            combos = list(itertools.product(Slist, Slist, Slist))
            if len(combos) > 20000:
                combos = random.sample(combos, 20000)
        for (c0, ccut, cnc) in combos:
            U0 = -pos(Q[t]) + d * c0[0]
            E0 = pos(Q[t]) + d * c0[1]
            # cut-indifference selection at m == thr
            for tie_sel in ('cut', 'nocut'):
                Ucut = G[t] - pos(Q[t] + A[t]) + d * ccut[0]
                Ecut = pos(Q[t] + A[t]) - A[t] + d * ccut[1]
                Unc0 = -pos(Q[t]) + d * cnc[0]
                Enc = pos(Q[t]) + d * cnc[1]
                # cut credible given selected continuations: m + Ucut >= Unc0 - m ... compare
                # cut iff Ucut >= -m + Unc0  <=>  m >= Unc0 - Ucut
                thr_m = Unc0 - Ucut
                regimes = []
                if mbar > thr_m + EPS:
                    regimes.append((Ecut, Ucut, 'cut'))
                if thr_m > EPS:
                    regimes.append((Enc, Unc0, 'nocut'))
                if -EPS <= thr_m <= mbar + EPS:
                    if tie_sel == 'cut':
                        regimes.append((Ecut, Ucut, 'cut'))
                    else:
                        regimes.append((Enc, Unc0 - max(thr_m, 0.0), 'nocut'))
                opts = []
                for (Er, Ur, lab) in regimes:
                    Tst = pos(Er + sig + rc)
                    opts.append((-Tst, Tst - sig - rc, t))           # accepted ultimatum at t
                    cont_issue = ccut[2] if lab == 'cut' else cnc[2]
                    opts.append((Ur, Er, cont_issue))                # refused ultimatum
                best = max(o[0] for o in opts) if opts else -1e18
                if best > U0 + EPS:
                    for o in opts:
                        if abs(o[0] - best) <= EPS:
                            newS.add((round(o[0], 9), round(o[1], 9), o[2]))
                elif best < U0 - EPS:
                    newS.add((round(U0, 9), round(E0, 9), c0[2]))
                else:
                    newS.add((round(U0, 9), round(E0, 9), c0[2]))
                    for o in opts:
                        if abs(o[0] - best) <= EPS:
                            newS.add((round(o[0], 9), round(o[1], 9), o[2]))
        if len(newS) > cap:
            newS = set(random.sample(sorted(newS), cap))
        S = newS
    return S

def draw(rng, T, mode):
    if mode == 'cont':
        Q = []
        q = rng.uniform(-6, 1)
        for t in range(T):
            Q.append(q)
            q += rng.uniform(-1.5, 3.5)
        A = [rng.choice([0.0, rng.uniform(0, 5)]) for _ in range(T)]
        G = [-rng.uniform(0.01, 3) for _ in range(T)]
        mbar = rng.uniform(0, 8)
        sig = rng.choice([0.0, rng.uniform(0, 3)])
        rc = rng.choice([0.0, rng.uniform(0, 3)])
        d = rng.choice([1.0, rng.uniform(0.05, 1)])
    else:
        Q = [rng.randint(-6, 4) for _ in range(T)]
        A = [rng.randint(0, 5) for _ in range(T)]
        G = [-rng.randint(1, 3) for _ in range(T)]
        mbar = rng.randint(0, 8); sig = rng.randint(0, 3); rc = rng.randint(0, 3)
        d = rng.choice([1.0, 0.5, 0.9])
    return (Q, A, G, mbar, sig, rc, d)

def main(N=100000, seed=11):
    rng = random.Random(seed)
    random.seed(seed + 1)
    st = dict(n=0, P_mismatch=0, P_issue_outside_window=0, P_issue_n=0,
              M_mismatch=0, M_strict_cases=0, N_mismatch=0, N_checked=0)
    ex = {}
    for i in range(N):
        T = rng.randint(2, 6)
        mode = 'cont' if i % 2 == 0 else 'grid'
        par = draw(rng, T, mode)
        Q, A, G, mbar, sig, rc, d = par
        el = eligible_dates(par)
        pred = len(el) > 0
        st['n'] += 1
        pi, VU, VE = solve_P(par)
        if (pi is not None) != pred:
            st['P_mismatch'] += 1
            ex.setdefault('P_mismatch', par)
        if pi is not None:
            st['P_issue_n'] += 1
            Delta = pos(Q[pi] + A[pi]) - pos(Q[pi])
            in_window = (mbar + G[pi] >= Delta - 1e-12) and bite(Q[pi], A[pi]) > sig + rc + 1e-12
            if not in_window:
                st['P_issue_outside_window'] += 1
                ex.setdefault('P_issue_outside_window', (par, pi, el))
        # Markov SPE set
        S = solve_set(par, markov=True)
        issued_any = any(s[2] is not None for s in S)
        not_issued_any = any(s[2] is None for s in S)
        if pred and not_issued_any:
            st['M_mismatch'] += 1; ex.setdefault('M_pred_yes_but_noissue_SPE', (par, sorted(S, key=str)))
        if (not pred) and issued_any:
            st['M_mismatch'] += 1; ex.setdefault('M_pred_no_but_issue_SPE', (par, sorted(S, key=str)))
        if i % 10 == 0 and T <= 4:
            st['N_checked'] += 1
            SN = solve_set(par, markov=False, cap=60)
            if pred and any(s[2] is None for s in SN):
                st['N_mismatch'] += 1; ex.setdefault('N_pred_yes_but_noissue', (par,))
            if (not pred) and any(s[2] is not None for s in SN):
                st['N_mismatch'] += 1
    print(st)
    for k, v in ex.items():
        print('\n==', k)
        for x in v:
            print('  ', x)

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 100000)
