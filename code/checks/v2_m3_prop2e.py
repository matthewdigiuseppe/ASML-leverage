"""v2 verifier m3: Proposition 2(e) (Chinese counter-threats) with China as a player.

Timing: China chooses credible, capped counter-threats r_k in [0, rbar_k] (grid) on U's
demands; then U chooses its ultimatum(s); E accepts or refuses; if E makes concession k
with r_k > 0, China executes (it is committed by a stake) at execution cost eC_k > 0 and
E bears the sunk loss r_k (both payoffs fall, Q unchanged).  China's payoff:
    -sum_{k conceded} z_k - sum_{k conceded, r_k>0} eC_k,
where z_k >= 0 is China's loss from concession k.  U, E payoffs as in v2_m3_prop2.py.

Main protocol: one bundled ultimatum backed by all of U's credible instruments J^c (U can
commit to a single ultimatum; see the report for why).  A smaller check repeats the key
claim (every executed counter-threat is pivotal) in the adaptive protocol.

Ties: E accepts when indifferent; U breaks ties toward the bundle that is better for E;
China breaks ties toward the profile with smaller total threat, then lexicographically.

Run: python3 -I v2_m3_prop2e.py   (about 1-2 minutes)
"""
import itertools
import os
import random
import sys
import time
import importlib.util

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('m3p2', os.path.join(HERE, 'v2_m3_prop2.py'))
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

TOL = 1e-9


def us_choice(I, filler=None):
    """One bundled ultimatum backed by J^c.  Returns (D, accepted, uU, uE, x_filler).
    filler = (w_f, X): a divisible sunk demand of size up to X, value w_f per unit, that
    China cannot threaten (used to model 'enough demands')."""
    full = (1 << I.nJ) - 1
    ref = P.final(I, full, 0)
    best = (0, True) + P.final(I, 0, 0) + (0.0,)
    for D in range(1 << I.K):
        acc = P.final(I, 0, D)
        x = 0.0
        if filler is not None:
            # largest x with E still accepting: E's loss is linear in sunk x
            slack_E = acc[1] - ref[1]
            if slack_E >= -TOL:
                x = max(0.0, min(filler[1], slack_E))
                acc = (acc[0] + filler[0] * x, acc[1] - x)
        if D == 0 and x == 0.0:
            continue
        if acc[1] >= ref[1] - TOL:
            z = (D, True, acc[0], acc[1], x)
        else:
            z = (D, False, ref[0], ref[1], 0.0)
        if z[2] > best[2] + TOL or (abs(z[2] - best[2]) <= TOL and z[3] > best[3] + TOL):
            best = z
    return best


def china_payoff(I, D, accepted, z, eC):
    if not accepted:
        return 0.0
    return -sum(z[k] + (eC[k] if I.r[k] > 0 else 0.0) for k in P.bits(D))


def china_opt(I, rbar, z, eC, levels, chooser):
    best = None
    for prof in itertools.product(*[[l * rbar[k] for l in levels] if rbar[k] > 0 else [0.0]
                                    for k in range(I.K)]):
        I.r = list(prof)
        res = chooser(I)
        pc = china_payoff(I, res[0], res[1], z, eC)
        key = (pc, -sum(prof))
        if best is None or key[0] > best[0][0] + TOL or \
                (abs(key[0] - best[0][0]) <= TOL and key[1] > best[0][1] + TOL):
            best = (key, list(prof), res)
    I.r = best[1]
    return best


def gen(rng, K=None):
    I = P.make_inst(rng, K=K if K is not None else rng.randint(1, 4),
                    nJ=rng.randint(1, 3))
    rbar = [rng.choice([0.0, rng.uniform(0.2, 3.0)]) for _ in range(I.K)]
    z = [rng.choice([0.0, rng.uniform(0.1, 5.0)]) for _ in range(I.K)]
    eC = [rng.uniform(0.05, 1.0) for _ in range(I.K)]
    return I, rbar, z, eC


def main():
    t0 = time.time()
    rng = random.Random(7)
    # E0: acceptance rule with counter-threats
    mism = 0
    tot = 0
    for _ in range(2000):
        I, rbar, z, eC = gen(rng)
        I.r = [rng.uniform(0, rb) for rb in rbar]
        full = (1 << I.nJ) - 1
        ref = P.final(I, full, 0)[1]
        for D in range(1, 1 << I.K):
            acc = P.final(I, 0, D)[1] >= ref - TOL
            pred = P.bundle_cost(I, D) <= P.B_of(I, full) + TOL
            tot += 1
            mism += (acc != pred)
    print("(e) acceptance with counter-threats: min(Trev,Lam)+Ts+R <= B(J^c) mismatches %d of %d"
          % (mism, tot))

    N = 4000
    st = dict(exec_onpath=0, exec_threats=0, nonpivotal=0, no_crowd=0, gain_wo_change=0,
              U_up=0, E_up=0, E_down=0, E_eq=0, ex=None, ex_down=None, fill_dev=0.0,
              china_gain=0)
    for it in range(N):
        I, rbar, z, eC = gen(rng)
        levels = [0, 1 / 3, 2 / 3, 1] if I.K == 4 else [0, 0.25, 0.5, 0.75, 1]
        I.r = [0.0] * I.K
        base = us_choice(I)
        base_pc = china_payoff(I, base[0], base[1], z, eC)
        best = china_opt(I, rbar, z, eC, levels, us_choice)
        rstar = best[1]
        res = best[2]
        D, accd = res[0], res[1]
        pc = best[0][0]
        if pc > base_pc + TOL:
            st['china_gain'] += 1
            if (D if accd else 0) == (base[0] if base[1] else 0):
                st['gain_wo_change'] += 1
        if res[2] > base[2] + 1e-9:
            st['U_up'] += 1
        lossE_star = P.base_uE(I) - res[3]
        lossE_0 = P.base_uE(I) - base[3]
        if lossE_star > lossE_0 + 1e-9:
            st['E_up'] += 1
            if st['ex'] is None:
                st['ex'] = (P.fmt_inst(I), rbar, z, eC, rstar, base, res)
        elif lossE_star < lossE_0 - 1e-9:
            st['E_down'] += 1
            if st['ex_down'] is None:
                st['ex_down'] = (P.fmt_inst(I), rbar, z, eC, rstar, base, res)
        else:
            st['E_eq'] += 1
        executed = [k for k in P.bits(D) if accd and rstar[k] > 0]
        if executed:
            st['exec_onpath'] += 1
        for k in executed:
            st['exec_threats'] += 1
            I.r = list(rstar)
            I.r[k] = 0.0
            alt = us_choice(I)
            Dalt = alt[0] if alt[1] else 0
            if Dalt == D:
                st['nonpivotal'] += 1
            elif (Dalt & ~D) == 0:
                st['no_crowd'] += 1
            I.r = list(rstar)
        # 'enough demands': divisible sunk filler that China cannot threaten
        filler = (0.05, 100.0)
        I.r = [0.0] * I.K
        b0 = us_choice(I, filler)
        I.r = list(rstar)
        b1 = us_choice(I, filler)
        B = P.B_of(I, (1 << I.nJ) - 1)
        st['fill_dev'] = max(st['fill_dev'], abs(P.base_uE(I) - b0[3] - B),
                             abs(P.base_uE(I) - b1[3] - B))
    print("\n(e) China-optimal counter-threats, one bundled ultimatum, %d instances" % N)
    print("  China strictly gains in %d; of these, with unchanged demand set: %d"
          % (st['china_gain'], st['gain_wo_change']))
    print("  instances with a counter-threat executed on path: %d (%d executed threats)"
          % (st['exec_onpath'], st['exec_threats']))
    print("  executed threats that are not pivotal (dropping it leaves U's bundle unchanged): %d"
          % st['nonpivotal'])
    print("  executed pivotal threats without crowding out (U's alternative adds no new demand): %d"
          % st['no_crowd'])
    print("  U's payoff higher with China's threats: %d" % st['U_up'])
    print("  E's loss with China's threats vs without: higher %d, lower %d, equal %d"
          % (st['E_up'], st['E_down'], st['E_eq']))
    print("  with a divisible filler demand: max |E loss - B(J^c)| (with and without threats) = %.2e"
          % st['fill_dev'])
    if st['ex'] is not None:
        print("  example, E hurt by the counter-threat:", st['ex'])
    if st['ex_down'] is not None:
        print("  example, E helped by the counter-threat:", st['ex_down'])

    # hand example: crowding out with execution on path, E hurt
    I = P.Inst()
    I.nJ, I.K = 1, 2
    I.DX, I.DA = [0.0, 2.0], [0.0, 2.0]
    I.Q = -1.0
    I.t, I.w, I.rev, I.e = [0.3, 1.5], [1.0, 20.0], [False, False], [0.01]
    I.r = [0.0, 0.0]
    b0 = us_choice(I)
    best = china_opt(I, [0.0, 0.4], [5.0, 0.0], [0.1, 0.1], [0, 0.5, 1], us_choice)
    print("\nHand example (B=2; k1: t=.3,w=1,z=5, no threat possible; k2: t=1.5,w=20, rbar=.4,"
          " eC=.1):")
    print("  no threats: U demands %s, E loss %.2f; China optimum r=%s: U demands %s, E loss %.2f,"
          " China payoff %.2f (threat on k2 executed)"
          % (bin(b0[0]), P.base_uE(I) - b0[3], best[1], bin(best[2][0]),
             P.base_uE(I) - best[2][3], best[0][0]))

    # adaptive protocol: executed threats pivotal?
    nonpiv = 0
    execs = 0
    n_ad = 0
    rng2 = random.Random(11)

    def ad_choice(I):
        S = P.solve_adaptive(I, tie='accept')
        zbest = max(S, key=lambda q: (round(q[0], 9), round(q[1], 9)))
        return (zbest[2], True, zbest[0], zbest[1])

    for it in range(300):
        I = P.make_inst(rng2, K=rng2.randint(1, 3), nJ=rng2.randint(1, 2), zero_e=False)
        rbar = [rng2.choice([0.0, rng2.uniform(0.2, 3.0)]) for _ in range(I.K)]
        z = [rng2.choice([0.0, rng2.uniform(0.1, 5.0)]) for _ in range(I.K)]
        eC = [rng2.uniform(0.05, 1.0) for _ in range(I.K)]
        best = china_opt(I, rbar, z, eC, [0, 0.5, 1], ad_choice)
        n_ad += 1
        rstar = best[1]
        C = best[2][0]
        for k in P.bits(C):
            if rstar[k] > 0:
                execs += 1
                I.r = list(rstar)
                I.r[k] = 0.0
                if ad_choice(I)[0] == C:
                    nonpiv += 1
                I.r = list(rstar)
    print("\nAdaptive protocol (%d instances): executed counter-threats %d, non-pivotal %d"
          % (n_ad, execs, nonpiv))
    print("Total time %.1fs" % (time.time() - t0))


if __name__ == '__main__':
    main()
