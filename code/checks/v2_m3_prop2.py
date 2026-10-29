"""v2 verifier m3: Proposition 2 (slack principle), parts (a)-(d) and (f).

Brute force from primitives (no use of the claimed formulas inside the solvers).

Model (one period, memo Section 4).  E aligned, exit premium Q.  Instruments j in
{0..nJ-1}; withdrawing set J lowers E's aligned payoff by DA[J] and exit payoff by
DX[J] (general monotone set functions, 0 <= DX <= DA, DA[0]=DX[0]=0).  Demands k with
cost t_k to E, value w_k to U, reversible (undone on exit) or sunk.  Execution of a
withdrawal J costs U e(J) >= 0.  At the end the bidding contest is replayed:
    aligned = -DA[Jw] - Trev - Ts,   exit = Q - DX[Jw] - Ts,
    rent = [exit - aligned]^+,  uE = aligned + rent,  uU = W - rent - e(Jw).
U is assumed to retain E (V, mbar_U large).  E's net loss = [Q]^+ - uE.

Solvers
  solve_adaptive : all SPE outcomes (set-valued backward induction) of the adaptive
                   protocol: U issues any finite sequence of ultimatums (nonempty demand
                   set D among unconceded demands, nonempty threat set among instruments
                   not yet withdrawn); E accepts or refuses; refused threats are executed
                   and spent; U may stop at any time.  tie='accept' (E accepts when
                   indifferent) or tie='any' (both responses allowed: all SPE).
  solve_oneshot  : U commits to at most one ultimatum (bundle D backed by J^c).

Run: python3 -I v2_m3_prop2.py      (about 1-2 minutes)
"""
import itertools
import random
import sys
import time

TOL = 1e-9


def submasks(mask):
    s = mask
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & mask


def bits(mask):
    i = 0
    while mask:
        if mask & 1:
            yield i
        mask >>= 1
        i += 1


def pos(x):
    return x if x > 0 else 0.0


# ---------------------------------------------------------------- instances
def monotone_setfun(n, rng, additive, scale, integer):
    N = 1 << n
    if additive:
        v = [rng.randint(0, scale) if integer else rng.uniform(0, scale) for _ in range(n)]
        return [sum(v[i] for i in bits(m)) for m in range(N)]
    g = [0.0] * N
    for m in range(1, N):
        g[m] = rng.randint(0, scale * bin(m).count('1')) if integer else \
            rng.uniform(0, scale * bin(m).count('1'))
    f = [0.0] * N
    for m in range(N):  # f(J) = max_{I subset J} g(I): monotone, f(0)=0
        f[m] = max(g[s] for s in submasks(m))
    return f


class Inst:
    pass


def make_inst(rng, nJ=None, K=None, integer=False, additive=None, Qmode=None,
              kinds=None, zero_e=None):
    I = Inst()
    I.nJ = nJ if nJ is not None else rng.randint(1, 4)
    I.K = K if K is not None else rng.randint(1, 4)
    if additive is None:
        additive = rng.random() < 0.4
    sc = 4 if integer else 3.0
    DX = monotone_setfun(I.nJ, rng, additive, sc, integer)
    H = monotone_setfun(I.nJ, rng, additive, sc, integer)
    if additive:
        DA = [DX[m] + H[m] for m in range(1 << I.nJ)]
    else:
        DA = [max(DX[m] + 0.0, H[m]) + (rng.randint(0, 2) if integer else 0) * (m > 0)
              for m in range(1 << I.nJ)]
        # make DA monotone again after the random bump
        for m in range(1 << I.nJ):
            DA[m] = max(DA[s] for s in submasks(m))
            DA[m] = max(DA[m], DX[m])
    I.DX, I.DA = DX, DA
    if Qmode is None:
        Qmode = rng.choice(['neg', 'neg', 'pos', 'zero'])
    if Qmode == 'neg':
        I.Q = -(rng.randint(1, 8) if integer else rng.uniform(0.1, 8))
    elif Qmode == 'pos':
        I.Q = rng.randint(1, 4) if integer else rng.uniform(0.05, 4)
    else:
        I.Q = 0.0
    I.t = [rng.randint(1, 5) if integer else rng.uniform(0.2, 5) for _ in range(I.K)]
    I.w = [rng.randint(1, 6) if integer else rng.uniform(0.1, 6) for _ in range(I.K)]
    if kinds is None:
        I.rev = [rng.random() < 0.5 for _ in range(I.K)]
    else:
        I.rev = [kinds == 'rev'] * I.K
    if zero_e is None:
        zero_e = rng.random() < 0.5
    I.e = [0.0 if zero_e else (rng.randint(0, 2) if integer else rng.uniform(0, 1))
           for _ in range(I.nJ)]
    I.r = [0.0] * I.K  # Chinese counter-threats (used in the (e) script)
    return I


def final(I, Jw, C):
    Trev = sum(I.t[k] for k in bits(C) if I.rev[k])
    Ts = sum(I.t[k] for k in bits(C) if not I.rev[k])
    R = sum(I.r[k] for k in bits(C))
    aligned = -I.DA[Jw] - Trev - Ts - R
    exitv = I.Q - I.DX[Jw] - Ts - R
    rent = pos(exitv - aligned)
    uE = aligned + rent
    uU = sum(I.w[k] for k in bits(C)) - rent - sum(I.e[j] for j in bits(Jw))
    return uU, uE


def base_uE(I):
    return pos(I.Q)


# ---------------------------------------------------------------- solvers
def solve_adaptive(I, tie='accept', threat_ok=None, extra_after_refusal=None):
    """Set of SPE outcomes at the root.  Outcome = (uU, uE, C, Jw, nref, nult).
    extra_after_refusal: optional instrument index that becomes available only after the
    first refusal (used to show the role of a fixed credible set)."""
    nJ, K = I.nJ, I.K
    full = (1 << nJ) - 1
    allK = (1 << K) - 1
    memo = {}

    def key(z):
        return (round(z[0], 7), round(z[1], 7))

    def out(R, C, unlocked):
        k0 = (R, C, unlocked)
        if k0 in memo:
            return memo[k0]
        avail = full
        if extra_after_refusal is not None and not unlocked:
            avail = full & ~(1 << extra_after_refusal)
        Jw = full & ~R
        if extra_after_refusal is not None and not unlocked:
            Jw &= ~(1 << extra_after_refusal)
        su, se = final(I, Jw, C)
        opts = [[(su, se, C, Jw, 0, 0)]]
        remK = allK & ~C
        Ravail = R & avail
        for D in submasks(remK):
            if D == 0:
                continue
            for J in submasks(Ravail):
                if J == 0:
                    continue
                if threat_ok is not None and not threat_ok(J):
                    continue
                A = out(R, C | D, unlocked)
                Rf = out(R & ~J, C, True if extra_after_refusal is not None else unlocked)
                res = {}
                for x in A:
                    for y in Rf:
                        if x[1] > y[1] + TOL:
                            z = x[:5] + (x[5] + 1,)
                            res[key(z)] = z
                        elif x[1] < y[1] - TOL:
                            z = y[:4] + (y[4] + 1, y[5] + 1)
                            res[key(z)] = z
                        else:
                            z = x[:5] + (x[5] + 1,)
                            res[key(z)] = z
                            if tie == 'any':
                                z = y[:4] + (y[4] + 1, y[5] + 1)
                                res[key(z)] = z
                opts.append(list(res.values()))
        m = max(min(z[0] for z in o) for o in opts)
        S = {}
        for o in opts:
            for z in o:
                if z[0] >= m - 1e-7:
                    S[key(z)] = z
        memo[k0] = list(S.values())
        return memo[k0]

    unlocked0 = False if extra_after_refusal is not None else True
    return out(full, 0, unlocked0)


def solve_oneshot(I, J=None):
    """U commits to at most one ultimatum backed by J (default: all instruments).
    E accepts when indifferent.  Returns (uU, uE, D, accepted) of U's best choice and the
    list of all (D, accepted, uU, uE)."""
    full = (1 << I.nJ) - 1 if J is None else J
    allK = (1 << I.K) - 1
    best = None
    rows = []
    su, se = final(I, 0, 0)
    best = (su, se, 0, True)
    ref = final(I, full, 0)
    for D in submasks(allK):
        if D == 0:
            continue
        acc = final(I, 0, D)
        if acc[1] >= ref[1] - TOL:
            z = (acc[0], acc[1], D, True)
        else:
            z = (ref[0], ref[1], D, False)
        rows.append(z)
        if z[0] > best[0] + TOL:
            best = z
    return best, rows


# ---------------------------------------------------------------- memo formulas
def Lam(I):
    return pos(-I.Q)


def u_of(I, J):
    return I.DX[J]


def d_of(I, J):
    return I.DA[J] - I.DX[J]


def B_of(I, J):
    return u_of(I, J) + min(d_of(I, J), Lam(I))


def bundle_cost(I, D):
    Trev = sum(I.t[k] for k in bits(D) if I.rev[k])
    Ts = sum(I.t[k] for k in bits(D) if not I.rev[k])
    R = sum(I.r[k] for k in bits(D))
    return min(Trev, Lam(I)) + Ts + R


# ---------------------------------------------------------------- checks
def check_a_b(rng, n):
    """(a) loss from refusing a single ultimatum backed by J equals B(J);
    (b) E accepts a single (final) ultimatum iff min(Trev,Lam)+Ts <= B(J)."""
    erra = 0.0
    mism_b = 0
    cnt = 0
    for it in range(n):
        I = make_inst(rng, integer=(it % 3 == 0))
        for J in range(1, 1 << I.nJ):
            uE_ref = final(I, J, 0)[1]
            erra = max(erra, abs((base_uE(I) - uE_ref) - B_of(I, J)))
            for D in range(1, 1 << I.K):
                uE_acc = final(I, 0, D)[1]
                acc = uE_acc >= uE_ref - TOL
                pred = bundle_cost(I, D) <= B_of(I, J) + TOL
                cnt += 1
                if acc != pred:
                    mism_b += 1
                # (b) first clause: net loss from reversible concessions = min(T, Lam)
                if all(I.rev[k] for k in bits(D)):
                    T = sum(I.t[k] for k in bits(D))
                    erra = max(erra, abs(base_uE(I) - uE_acc - min(T, Lam(I))))
    return erra, mism_b, cnt


def check_c_d(rng, n, integer, tie):
    stats = dict(n=0, bound_viol=0, maxexcess=-1e9, U_above_oneshot=0,
                 U_below_oneshot=0, onpath_refusal=0, multiU=0,
                 cond_eq_fail=0, cond_cases=0, refusal_examples=[], below_examples=[],
                 knap_mismatch=0, corr_mismatch=0, rev_cases=0, Q_pos_cases=0,
                 epos=0, onpath_refusal_epos=0, below_epos=0)
    for it in range(n):
        I = make_inst(rng, integer=integer, K=rng.randint(1, 3) if it % 2 else None,
                      nJ=rng.randint(1, 3) if it % 2 else None)
        full = (1 << I.nJ) - 1
        S = solve_adaptive(I, tie=tie)
        B = B_of(I, full)
        stats['n'] += 1
        if I.Q > 0:
            stats['Q_pos_cases'] += 1
        losses = [base_uE(I) - z[1] for z in S]
        ex = max(losses) - B
        stats['maxexcess'] = max(stats['maxexcess'], ex)
        if ex > 1e-7:
            stats['bound_viol'] += 1
        best1, _ = solve_oneshot(I)
        U_vals = [z[0] for z in S]
        if max(U_vals) - min(U_vals) > 1e-7:
            stats['multiU'] += 1
        if max(U_vals) > best1[0] + 1e-7:
            stats['U_above_oneshot'] += 1
        if min(U_vals) < best1[0] - 1e-7:
            stats['U_below_oneshot'] += 1
            if len(stats['below_examples']) < 3:
                stats['below_examples'].append((I, best1, S))
        if all(x > 0 for x in I.e):
            stats['epos'] += 1
            if any(z[4] > 0 for z in S):
                stats['onpath_refusal_epos'] += 1
            if min(U_vals) < best1[0] - 1e-7:
                stats['below_epos'] += 1
        if any(z[4] > 0 for z in S):
            stats['onpath_refusal'] += 1
            if len(stats['refusal_examples']) < 2:
                stats['refusal_examples'].append((I, S))
        # sufficient conditions for adaptive = one-shot (claimed in the report):
        # (i) all demands reversible and B(J^c) >= Lam; (ii) one-shot optimum concedes all demands
        allrev = all(I.rev)
        cond = (allrev and B >= Lam(I) - TOL) or (best1[3] and best1[2] == (1 << I.K) - 1)
        if cond and tie == 'accept':
            stats['cond_cases'] += 1
            if abs(min(U_vals) - best1[0]) > 1e-7 or abs(max(U_vals) - best1[0]) > 1e-7:
                stats['cond_eq_fail'] += 1
        # (d) reversible demands only: one-shot U gain vs memo knapsack and corrected program
        if allrev:
            stats['rev_cases'] += 1
            gain = best1[0] - final(I, 0, 0)[0]
            cap = min(Lam(I), B)
            knap = 0.0
            corr = 0.0
            for D in range(1 << I.K):
                T = sum(I.t[k] for k in bits(D))
                W = sum(I.w[k] for k in bits(D))
                if T <= cap + TOL:
                    knap = max(knap, W)
                if min(T, Lam(I)) <= B + TOL:
                    corr = max(corr, W - pos(T - Lam(I)))
            if abs(gain - knap) > 1e-7:
                stats['knap_mismatch'] += 1
            if abs(gain - corr) > 1e-7:
                stats['corr_mismatch'] += 1
    return stats


def fmt_inst(I):
    return ("nJ=%d DX=%s DA=%s Q=%g t=%s w=%s rev=%s e=%s" %
            (I.nJ, [round(x, 3) for x in I.DX], [round(x, 3) for x in I.DA], I.Q,
             [round(x, 3) for x in I.t], [round(x, 3) for x in I.w], I.rev,
             [round(x, 3) for x in I.e]))


def hand_examples():
    print("\n--- Hand-picked examples (execution cost 0.01 per instrument) ---")
    # Ratchet: one instrument with unconditional bite 1.5, two sunk demands of cost 1.
    I = Inst()
    I.nJ, I.K = 1, 2
    I.DX, I.DA = [0.0, 1.5], [0.0, 1.5]
    I.Q = -1.0
    I.t, I.w, I.rev, I.e, I.r = [1.0, 1.0], [3.0, 2.0], [False, False], [0.01], [0.0, 0.0]
    S = solve_adaptive(I, tie='any')
    b1, _ = solve_oneshot(I)
    print("Ratchet example (2 sunk demands t=1, B=1.5): one-shot U gain = %.3g (E loss %.3g);"
          " adaptive SPE (U gain, E loss) = %s" %
          (b1[0], base_uE(I) - b1[1], sorted({(round(z[0], 3), round(base_uE(I) - z[1], 3))
                                             for z in S})))
    # Parity: n identical sunk demands
    for n in range(1, 7):
        I.K = n
        I.t, I.w, I.rev, I.r = [1.0] * n, [2.0] * n, [False] * n, [0.0] * n
        S = solve_adaptive(I, tie='accept')
        b1, _ = solve_oneshot(I)
        print("  n=%d identical sunk demands (t=1,w=2), B=1.5: one-shot gain %.3g, adaptive gain %s"
              % (n, b1[0], sorted({round(z[0], 3) for z in S})))
    # Fine grid: demands of size 0.25 with total mass M; B = 1.0
    print("  fine grid, item cost 0.25, B=1 (sunk), adaptive E loss by total demand mass M:")
    I.DX, I.DA = [0.0, 1.0], [0.0, 1.0]
    row = []
    for n in range(1, 11):
        I.K = n
        I.t, I.w, I.rev, I.r = [0.25] * n, [1.0] * n, [False] * n, [0.0] * n
        S = solve_adaptive(I, tie='accept')
        row.append((n * 0.25, sorted({round(base_uE(I) - z[1], 3) for z in S})))
    print("   ", row)
    # Reversible-only, conditional instrument, B < Lam: ratchet inside Lam
    I = Inst()
    I.nJ, I.K = 1, 2
    I.DX, I.DA = [0.0, 0.0], [0.0, 1.5]
    I.Q = -5.0
    I.t, I.w, I.rev, I.e, I.r = [1.0, 1.0], [1.0, 1.0], [True, True], [0.01], [0.0, 0.0]
    S = solve_adaptive(I, tie='any')
    b1, _ = solve_oneshot(I)
    print("Reversible, d=1.5 < Lam=5, u=0, two demands t=1: one-shot gain %.3g; adaptive %s"
          % (b1[0], sorted({round(z[0], 3) for z in S})))
    I.Q = -1.5  # now B = Lam: no ratchet
    S = solve_adaptive(I, tie='accept')
    b1, _ = solve_oneshot(I)
    print("  same with Lam=1.5=B: one-shot gain %.3g; adaptive %s"
          % (b1[0] - final(I, 0, 0)[0], sorted({round(z[0] - final(I, 0, 0)[0], 3) for z in S})))
    # Knapsack counterexample (d): Lam=1, one reversible demand t=1.5, w=1.4 <= t
    I = Inst()
    I.nJ, I.K = 1, 1
    I.DX, I.DA = [0.0, 0.0], [0.0, 3.0]
    I.Q = -1.0
    I.t, I.w, I.rev, I.e, I.r = [1.5], [1.4], [True], [0.0], [0.0]
    b1, _ = solve_oneshot(I)
    print("(d) counterexample: Lam=1, B=1, reversible t=1.5, w=1.4: knapsack value 0, "
          "U's actual gain %.3g (pays rent 0.5)" % (b1[0] - final(I, 0, 0)[0]))
    # Hedge (f): y_H > Lam
    I.t, I.w = [2.0], [3.0]
    b1, _ = solve_oneshot(I)
    print("(f) hedge y_H=2 > Lam=1, w_H=3, B=1: stopped=%s, U gain %.3g = w_H-(y_H-Lam)=%.3g"
          % (b1[3] and b1[2] == 1, b1[0] - final(I, 0, 0)[0], 3 - 1.0))
    # Deliberate burning of a threat on path (U executes an instrument as a commitment device)
    I = Inst()
    I.nJ, I.K = 2, 2
    I.DX, I.DA = [0.0, 1.2, 1.0, 2.2], [0.0, 1.2, 1.0, 2.2]
    I.Q = -5.0
    I.t, I.w, I.rev, I.e, I.r = [1.0, 1.5], [5.0, 1.0], [False, False], [0.1, 0.1], [0.0, 0.0]
    S = solve_adaptive(I, tie='any')
    b1, _ = solve_oneshot(I)
    print("Burning example (u=1.2,1.0; sunk t=1 (w=5), t=1.5 (w=1); e=0.1): one-shot U=%.3g;"
          " adaptive SPE (uU, E loss, conceded, withdrawn, #refusals) = %s"
          % (b1[0], [(round(z[0], 3), round(base_uE(I) - z[1], 3), z[2], z[3], z[4]) for z in S]))
    # Ratchet lemma, random: one instrument with B = u (d = 0), n identical sunk demands of
    # size tau, value w > 0, e > 0.  Claim: U obtains exactly n mod (b+1) demands,
    # b = floor(B / tau), in every SPE.
    rng = random.Random(123)
    bad = 0
    for _ in range(300):
        tau = rng.choice([1.0, 0.5, rng.uniform(0.2, 2.0)])
        b = rng.randint(0, 4)
        Bv = tau * b + rng.choice([0.0, rng.uniform(0, tau * 0.999)])
        n = rng.randint(1, 7)
        I = Inst()
        I.nJ, I.K = 1, n
        I.DX, I.DA = [0.0, Bv], [0.0, Bv]
        I.Q = rng.choice([-3.0, 0.0, 1.0])
        I.t, I.w, I.rev = [tau] * n, [rng.uniform(0.1, 3)] * n, [False] * n
        I.e, I.r = [rng.uniform(0.01, 1)], [0.0] * n
        exact = (Bv == tau * b)
        for tie in (['accept'] if exact else ['accept', 'any']):
            S = solve_adaptive(I, tie=tie)
            counts = {bin(z[2]).count('1') for z in S}
            if counts != {n % (b + 1)}:
                bad += 1
    print("Ratchet lemma (n identical sunk demands, one instrument), 300 draws (all SPE when "
          "B/tau is not an integer; E accepting when indifferent otherwise): SPE concession "
          "count != n mod (b+1) in %d" % bad)
    # (f) hedge, random: single reversible demand y_H with value w_H
    rng = random.Random(99)
    bad = 0
    for _ in range(3000):
        I = make_inst(rng, K=1, kinds='rev')
        lam, B = Lam(I), B_of(I, (1 << I.nJ) - 1)
        b1, _ = solve_oneshot(I)
        stopped = b1[3] and b1[2] == 1
        gain = b1[0] - final(I, 0, 0)[0]
        feas = min(I.t[0], lam) <= B + TOL
        pred_gain = I.w[0] - pos(I.t[0] - lam)
        pred_stop = feas and pred_gain > TOL
        if stopped != pred_stop or (stopped and abs(gain - pred_gain) > 1e-9):
            bad += 1
    print("(f) hedge as one reversible demand, 3000 draws: mismatches with 'stopped iff "
          "min(y_H,Lam) <= B(J^c) and w_H > [y_H-Lam]^+, U's net gain w_H-[y_H-Lam]^+': %d" % bad)
    # Q>0 bound
    I = Inst()
    I.nJ, I.K = 2, 2
    I.DX, I.DA = [0.0, 1.0, 0.5, 2.0], [0.0, 3.0, 2.0, 6.0]
    I.Q = 0.7
    I.t, I.w, I.rev, I.e, I.r = [1.2, 0.9], [3.0, 3.0], [False, True], [0.0, 0.0], [0.0, 0.0]
    S = solve_adaptive(I, tie='any')
    print("Q=0.7>0, u(J^c)=2: max adaptive E loss %.3g <= B=%.3g"
          % (max(base_uE(I) - z[1] for z in S), B_of(I, 3)))


def check_new_instrument(rng, n):
    """If a refusal makes a new instrument available, the bound B(J^c) (J^c = instruments
    available at the start) can fail; with the enlarged set it holds."""
    worst = -1e9
    worst_big = -1e9
    for _ in range(n):
        I = make_inst(rng, nJ=rng.randint(2, 3), K=rng.randint(1, 3), kinds='sunk')
        x = I.nJ - 1
        S = solve_adaptive(I, tie='accept', extra_after_refusal=x)
        Jc0 = ((1 << I.nJ) - 1) & ~(1 << x)
        L = max(base_uE(I) - z[1] for z in S)
        worst = max(worst, L - B_of(I, Jc0))
        worst_big = max(worst_big, L - B_of(I, (1 << I.nJ) - 1))
    return worst, worst_big


def check_capped_bundles(rng, n):
    """Variant: only threat sets with e(J) <= mbar are credible (family not closed under
    union).  Bound B(union of credible sets) still holds; best single bundle can be worse
    than the adaptive SPE, and vice versa."""
    viol = 0
    better_seq = 0
    worse_seq = 0
    for _ in range(n):
        I = make_inst(rng, nJ=rng.randint(2, 3), K=rng.randint(1, 3), zero_e=False)
        I.e = [rng.uniform(0.2, 1.0) for _ in range(I.nJ)]
        mbar = rng.uniform(0.3, 1.5)
        ok = lambda J: sum(I.e[j] for j in bits(J)) <= mbar
        S = solve_adaptive(I, tie='accept', threat_ok=ok)
        Jc = 0
        for J in range(1, 1 << I.nJ):
            if ok(J):
                Jc |= J
        L = max(base_uE(I) - z[1] for z in S)
        if L > B_of(I, Jc) + 1e-7:
            viol += 1
        best = final(I, 0, 0)[0]
        for J in range(1, 1 << I.nJ):
            if ok(J):
                best = max(best, solve_oneshot(I, J)[0][0])
        if min(z[0] for z in S) > best + 1e-7:
            better_seq += 1
        if max(z[0] for z in S) < best - 1e-7:
            worse_seq += 1
    return viol, better_seq, worse_seq


def main():
    t0 = time.time()
    rng = random.Random(20261029)
    print("Proposition 2 (a),(b): single ultimatum")
    erra, mb, cnt = check_a_b(rng, 3000)
    print("  (a) max |loss(refuse J) - B(J)| and |rev loss - min(T,Lam)| = %.2e" % erra)
    print("  (b) acceptance mismatches: %d of %d (instrument set x bundle) pairs" % (mb, cnt))

    for integer, tie, n in [(False, 'accept', 2000), (True, 'accept', 1000), (True, 'any', 1000)]:
        st = check_c_d(rng, n, integer, tie)
        print("\nProposition 2 (c),(d): adaptive SPE, %s draws, tie=%s, %d instances (Q>0 in %d)"
              % ('integer' if integer else 'continuous', tie, st['n'], st['Q_pos_cases']))
        print("  bound violations (E loss > B(J^c)): %d; max(loss - B) = %.2e"
              % (st['bound_viol'], st['maxexcess']))
        print("  U's SPE value above one-shot optimum: %d; below one-shot optimum: %d"
              % (st['U_above_oneshot'], st['U_below_oneshot']))
        print("  instances with multiple SPE U values: %d; with a refusal on some SPE path: %d"
              % (st['multiU'], st['onpath_refusal']))
        print("  with all execution costs e_j > 0 (%d instances): refusal on an SPE path in %d;"
              " U below one-shot in %d" % (st['epos'], st['onpath_refusal_epos'], st['below_epos']))
        if tie == 'accept':
            print("  sufficient conditions (all reversible & B>=Lam, or one-shot concedes all):"
                  " %d cases, adaptive != one-shot in %d" % (st['cond_cases'], st['cond_eq_fail']))
        print("  (d) reversible-only cases %d: memo knapsack != one-shot optimum in %d; "
              "corrected program != one-shot optimum in %d"
              % (st['rev_cases'], st['knap_mismatch'], st['corr_mismatch']))
        for (I, b1, S) in st['below_examples'][:1]:
            print("  example U below one-shot:", fmt_inst(I))
            print("     one-shot U=%.3f; adaptive U values %s" %
                  (b1[0], sorted({round(z[0], 3) for z in S})))
        for (I, S) in st['refusal_examples'][:1]:
            print("  example on-path refusal:", fmt_inst(I))
            print("     SPE outcomes (uU,uE,C,Jw,#refusals,#ultimatums):",
                  [tuple(round(v, 3) if isinstance(v, float) else v for v in z) for z in S][:4])

    hand_examples()
    w1, w2 = check_new_instrument(rng, 150)
    print("\nNew instrument after first refusal: max(loss - B(initial J^c)) = %.3g; "
          "max(loss - B(enlarged set)) = %.2e" % (w1, w2))
    v, bs, ws = check_capped_bundles(rng, 150)
    print("Bundle-capped credibility (e(J) <= mbar): bound violations %d; adaptive better "
          "than best credible single bundle in %d; worse in %d (of 150)" % (v, bs, ws))
    print("\nTotal time %.1fs" % (time.time() - t0))


if __name__ == '__main__':
    main()
