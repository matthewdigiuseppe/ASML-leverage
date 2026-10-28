"""Brute-force check of Lemma 2 (bite), Lemma 3 and Proposition 4 (preventive control).

Two-period game in 05_control.tex. Payoffs from the table (normalized):
  No ultimatum : E = [Q1]+ + d[Q2]+                 U = -[Q1]+ - d[Q2]+
  Accept       : E = T - sig - rc                   U = -T
  Refuse, cut  : E = [Q1+a1]+ - a1 + d[Q2]+         U = gN - [Q1+a1]+ - d[Q2]+
  Refuse, nocut: E = [Q1]+ + d[Q2]+                 U = -m - [Q1]+ - d[Q2]+
US chooses: issue or not; m in [0, mbar]; T >= 0.  Europe accepts/refuses.  US cuts or not.

We compute the SET of SPE outcomes, never breaking ties in favour of the proposition:
whenever a player is indifferent, both actions are admissible.
"""
import random, math, itertools, sys

def pos(x):
    return x if x > 0 else 0.0

EPS = 1e-9

def spe_outcomes(Q1, Q2, a1, gN, mbar, sig, rc, d):
    """Return list of (label, U, E, T) SPE outcomes. The US's response at a cut-indifference
    node is an equilibrium selection (enumerated), not a choice made at the issue stage."""
    U0 = -pos(Q1) - d * pos(Q2)
    E0 = pos(Q1) + d * pos(Q2)
    Delta = pos(Q1 + a1) - pos(Q1)
    Ecut = pos(Q1 + a1) - a1 + d * pos(Q2)
    Ucut = gN - pos(Q1 + a1) - d * pos(Q2)
    out = []
    for tie_sel in ('cut', 'nocut'):
        regimes = []
        thr = Delta - gN
        # m strictly above threshold available iff thr < mbar
        if thr < mbar - EPS:
            regimes.append((Ecut, Ucut, 'cut'))
        if abs(thr - mbar) <= EPS and tie_sel == 'cut':
            regimes.append((Ecut, Ucut, 'cut'))
        if thr >= 0 - EPS:  # m=0 gives no cut (strictly if thr>0)
            if thr > EPS or tie_sel == 'nocut':
                regimes.append((E0, -0.0 - pos(Q1) - d * pos(Q2), 'nocut'))
        issue_options = []
        for (Er, Ur, lab) in regimes:
            Tstar = pos(Er + sig + rc)
            issue_options.append(('accept', -Tstar, Tstar - sig - rc, Tstar))
            issue_options.append(('refuse_' + lab, Ur, Er, None))
        if not issue_options:
            out.append(('none', U0, E0, None)); continue
        best_issue = max(o[1] for o in issue_options)
        if best_issue > U0 + EPS:
            out += [('issue_' + o[0], o[1], o[2], o[3]) for o in issue_options if abs(o[1]-best_issue) <= EPS]
        elif best_issue < U0 - EPS:
            out.append(('none', U0, E0, None))
        else:
            out.append(('none', U0, E0, None))
            out += [('issue_' + o[0], o[1], o[2], o[3]) for o in issue_options if abs(o[1]-best_issue) <= EPS]
    return out

def predicted(Q1, Q2, a1, gN, mbar, sig, rc, d):
    b1 = min(a1, pos(-Q1))
    c1 = Q2 > 0
    c2 = mbar + gN >= pos(Q1 + a1) - pos(Q1)
    c3 = b1 > sig + rc
    ok = c1 and c2 and c3
    Tstar = pos(d * Q2 + sig + rc - b1)
    Epay = max(d * Q2 - b1, -sig - rc)
    return ok, Tstar, Epay, b1, (c1, c2, c3)

def draw(rng, mode):
    if mode == 'cont':
        Q1 = rng.uniform(-6, 4); Q2 = rng.uniform(-4, 6)
        a1 = rng.choice([0.0, rng.uniform(0, 5)])
        gN = -rng.uniform(0.001, 3)          # chi_ai=1 => nu1 < kA => gN < 0
        mbar = rng.uniform(0, 8)
        sig = rng.choice([0.0, rng.uniform(0, 3)])
        rc = rng.choice([0.0, rng.uniform(0, 3)])
        d = rng.choice([1.0, rng.uniform(0.05, 1)])
    else:  # integer grid to provoke ties
        Q1 = rng.randint(-6, 3); Q2 = rng.randint(-3, 4)
        a1 = rng.randint(0, 5); gN = -rng.randint(1, 3)
        mbar = rng.randint(0, 8); sig = rng.randint(0, 3); rc = rng.randint(0, 3)
        d = rng.choice([1.0, 0.5])
    return Q1, Q2, a1, gN, mbar, sig, rc, d

def main(N=200000, seed=1):
    rng = random.Random(seed)
    stats = dict(n=0, lemma2_bad=0, mismatch_iff=0, mismatch_T=0, mismatch_E=0,
                 tie_generic=0, tie_ii_equal=0, other=0)
    examples = {}
    for i in range(N):
        mode = 'cont' if i % 2 == 0 else 'grid'
        p = draw(rng, mode)
        Q1, Q2, a1, gN, mbar, sig, rc, d = p
        stats['n'] += 1
        # Lemma 2: bite formula
        b_direct = a1 - (pos(Q1 + a1) - pos(Q1))
        if abs(b_direct - min(a1, pos(-Q1))) > 1e-9:
            stats['lemma2_bad'] += 1
        outs = spe_outcomes(*p)
        ok, Tstar, Epay, b1, cs = predicted(*p)
        accepted = [o for o in outs if o[0] == 'issue_accept']
        others = [o for o in outs if o[0] != 'issue_accept']
        if ok:
            if others:
                stats['mismatch_iff'] += 1
                key = 'pred_yes_but_other_SPE'
                examples.setdefault(key, (p, outs, cs))
                if abs(mbar + gN - (pos(Q1 + a1) - pos(Q1))) < 1e-9:
                    stats['tie_ii_equal'] += 1
            for o in accepted:
                if abs(o[3] - Tstar) > 1e-7:
                    stats['mismatch_T'] += 1
                if abs(o[2] - Epay) > 1e-7:
                    stats['mismatch_E'] += 1
        else:
            if accepted:
                stats['mismatch_iff'] += 1
                if (not cs[0]) and b1 >= sig + rc and b1 > 0:
                    stats['tie_generic'] += 1
                    examples.setdefault('pred_no_but_accept_SPE (Q2<=0, b1>=sig+rc)', (p, outs, cs))
                else:
                    stats['other'] += 1
                    examples.setdefault('pred_no_but_accept_SPE (other)', (p, outs, cs))
    print(stats)
    for k, v in examples.items():
        print('\n==', k)
        print('  params (Q1,Q2,a1,gN,mbar,sig,rc,delta) =', v[0])
        print('  conditions (i,ii,iii) =', v[2])
        for o in v[1]:
            print('   SPE outcome:', o)

    # generic-tie region: how large is it among continuous draws?
    rng = random.Random(7)
    cnt = 0; tot = 0
    for i in range(200000):
        p = draw(rng, 'cont'); Q1, Q2, a1, gN, mbar, sig, rc, d = p
        b1 = min(a1, pos(-Q1))
        cred = mbar + gN >= pos(Q1 + a1) - pos(Q1)
        tot += 1
        if Q2 <= 0 and b1 > sig + rc and cred:
            cnt += 1
    print('\nShare of continuous draws in open tie region (Q2<=0, b1>sig+rc, cut credible):', cnt / tot)

    # explicit counterexample
    p = (-3.0, -1.0, 2.0, -0.5, 5.0, 0.5, 0.5, 0.9)
    print('\nExplicit example', p)
    for o in spe_outcomes(*p):
        print('   SPE outcome:', o)
    print('   predicted (ok,T*,E,b1,conds):', predicted(*p))

if __name__ == '__main__':
    main()
