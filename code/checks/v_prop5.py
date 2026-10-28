"""Brute-force check of Proposition 5 (breakdown under private sovereignty costs).

sigma ~ U[0, sbar], private. Conditions (i),(ii) of Prop 4 hold; a = b1 - rc > 0; R = d*Q2 > 0;
e = -gN + [Q1+a1]^+ (> 0 under chi_ai=1 because gN < 0).
US options: (0) no ultimatum: gain 0.
            (1) ultimatum with credible cut and payment T >= 0: type sigma accepts iff
                T - sigma - rc >= -b1 + R, i.e. sigma <= T + a - R.  Gain if accept: R - T;
                if refuse: -e.
            (2) ultimatum with non-credible cut (m < e): accept iff T - sigma - rc >= R. Gain <= 0.
We maximize the gain directly over a fine grid of T (plus local refinement) and compare with
s* = max{a - R, min{sbar, (a+e)/2}}, P_b = [1 - s*/sbar]^+, and with the issuance condition.
"""
import random, math
import numpy as np
from scipy.optimize import minimize_scalar

def pos(x): return x if x > 0 else 0.0

def gain(T, a, R, e, sbar):
    s = T + a - R
    P = min(max(s / sbar, 0.0), 1.0)
    return P * (R - T) - (1 - P) * e

def optimize(a, R, e, sbar):
    Tmax = R + sbar + abs(a) + 5
    grid = np.linspace(0, Tmax, 20001)
    s = grid + a - R
    P = np.clip(s / sbar, 0, 1)
    G = P * (R - grid) - (1 - P) * e
    i = int(np.argmax(G))
    lo = grid[max(i - 2, 0)]; hi = grid[min(i + 2, len(grid) - 1)]
    res = minimize_scalar(lambda T: -gain(T, a, R, e, sbar), bounds=(lo, hi), method='bounded',
                          options={'xatol': 1e-12})
    Tb, Gb = (res.x, -res.fun) if -res.fun >= G[i] else (grid[i], G[i])
    # T = 0 corner explicitly
    if gain(0.0, a, R, e, sbar) >= Gb - 1e-12:
        if gain(0.0, a, R, e, sbar) > Gb:
            Tb, Gb = 0.0, gain(0.0, a, R, e, sbar)
    return Tb, Gb

def formula(a, R, e, sbar):
    s = max(a - R, min(sbar, (a + e) / 2))
    Pb = pos(1 - s / sbar)
    return s, Pb

def issue_full(a, R, e, sbar):
    s, _ = formula(a, R, e, sbar)
    x = a - s  # = R - T
    if s >= sbar:
        return x  # everyone accepts
    return (s * x - (sbar - s) * e) / sbar

def issue_proof_interior(a, R, e, sbar):
    return (a + e) ** 2 > 4 * sbar * e

def main(N=40000, seed=3):
    rng = random.Random(seed)
    st = dict(n=0, s_mismatch=0, Pb_mismatch=0, issue_mismatch=0,
              interior_rule_wrong_outside_interior=0, interior_n=0, interior_rule_wrong_in_interior=0)
    ex = {}
    for i in range(N):
        a = rng.uniform(0.01, 6); R = rng.uniform(0.01, 6)
        e = rng.choice([rng.uniform(0.001, 6), rng.uniform(0.001, 0.2)])
        sbar = rng.uniform(0.05, 8)
        Tb, Gb = optimize(a, R, e, sbar)
        s_num = Tb + a - R
        s_f, Pb_f = formula(a, R, e, sbar)
        st['n'] += 1
        # compare acceptance cutoff (clip both at sbar since s>sbar is payoff-equivalent only if T same)
        if abs(min(s_num, max(sbar, a - R)) - s_f) > 1e-4 and Gb > -e + 1e-9:
            st['s_mismatch'] += 1; ex.setdefault('s', (a, R, e, sbar, s_num, s_f))
        Pb_num = pos(1 - s_num / sbar)
        if abs(Pb_num - Pb_f) > 1e-4:
            st['Pb_mismatch'] += 1; ex.setdefault('Pb', (a, R, e, sbar, Pb_num, Pb_f))
        issues_num = Gb > 1e-9
        issues_full = issue_full(a, R, e, sbar) > 1e-9
        if issues_num != issues_full:
            st['issue_mismatch'] += 1; ex.setdefault('issue', (a, R, e, sbar, Gb, issue_full(a, R, e, sbar)))
        interior = (a - R) < (a + e) / 2 < sbar
        if interior:
            st['interior_n'] += 1
            if issue_proof_interior(a, R, e, sbar) != issues_num:
                st['interior_rule_wrong_in_interior'] += 1
        else:
            if issue_proof_interior(a, R, e, sbar) != issues_num:
                st['interior_rule_wrong_outside_interior'] += 1
                ex.setdefault('interior_rule_outside', (a, R, e, sbar, Gb))
    print(st)
    for k, v in ex.items():
        print(k, v)

    # Comparative statics, conditional and unconditional, by finite differences
    rng = random.Random(9)
    cs = {k: [0, 0, 0] for k in ['b1', 'e', 'rc', 'sbar', 'R_corner']}  # [n, cond_viol, uncond_viol]
    cexs = {}
    for i in range(20000):
        b1 = rng.uniform(0.1, 7); rc = rng.uniform(0, 3); R = rng.uniform(0.01, 5)
        e = rng.uniform(0.01, 5); sbar = rng.uniform(0.1, 8)
        if b1 - rc <= 0: continue
        h = 0.05
        def PB(b1, rc, R, e, sbar):
            a = b1 - rc
            if a <= 0: return None, None
            s, Pb = formula(a, R, e, sbar)
            _, Gb = optimize(a, R, e, sbar)
            return Pb, (Pb if Gb > 1e-9 else 0.0)
        base = PB(b1, rc, R, e, sbar)
        for name, args, sign in [('b1', (b1 + h, rc, R, e, sbar), -1), ('e', (b1, rc, R, e + h, sbar), -1),
                                 ('rc', (b1, rc + h, R, e, sbar), +1), ('sbar', (b1, rc, R, e, sbar + h), +1)]:
            new = PB(*args)
            if new[0] is None: continue
            cs[name][0] += 1
            if sign * (new[0] - base[0]) < -1e-9:
                cs[name][1] += 1
            if sign * (new[1] - base[1]) < -1e-9:
                cs[name][2] += 1; cexs.setdefault(name, ((b1, rc, R, e, sbar), args, base, new))
        a = b1 - rc
        if a - R > min(sbar, (a + e) / 2):
            new = PB(b1, rc, R + h, e, sbar)
            cs['R_corner'][0] += 1
            if not (new[0] > base[0] + 1e-12):
                cs['R_corner'][1] += 1; cexs.setdefault('R_corner_not_increasing', ((b1, rc, R, e, sbar), base, new))
    print('\ncomparative statics [n, violations conditional on issuance, violations unconditional]:')
    for k, v in cs.items(): print('  ', k, v)
    for k, v in cexs.items(): print('  counterexample', k, v)

    # explicit examples
    print('\nExplicit: corner a-R >= sbar gives Pb = 0, flat in R')
    for R in (1.0, 1.5):
        print('   a=5,R=%.1f,e=1,sbar=2 ->' % R, formula(5, R, 1, 2), 'US gain', optimize(5, R, 1, 2)[1])
    print('Explicit: unconditional breakdown non-monotone in rc (b1=7,R=5,e=1,sbar=10)')
    for rc in (0.0, 1.0, 1.7):
        a = 7 - rc
        s, Pb = formula(a, 5, 1, 10); Tb, Gb = optimize(a, 5, 1, 10)
        print('   rc=%.1f: s*=%.3f P_b(cond)=%.3f US gain=%.4f issues=%s' % (rc, s, Pb, Gb, Gb > 0))
    print('Explicit: interior rule (a+e)^2>4*sbar*e applied in corner s*=sbar')
    a, R, e, sbar = 0.5, 5.0, 3.5, 1.0
    print('   a=%.1f R=%.1f e=%.1f sbar=%.1f: (a+e)^2=%.2f 4sbar e=%.2f ; true max gain=%.4f (=a-sbar)'
          % (a, R, e, sbar, (a + e) ** 2, 4 * sbar * e, optimize(a, R, e, sbar)[1]))

if __name__ == '__main__':
    main()
