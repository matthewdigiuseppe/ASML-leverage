"""Brute-force check of Lemma 1 (credible conditionality).

Stage-4 decisions are computed by comparing ex post payoffs directly, keeping the
full SET of optimal actions (no tie-breaking).  We then compare the implied
exit cost with c = kappa*S + chi_ai*alpha + chi_f*f + eta and the Atlantic cost chi_r*r.
Parameters are drawn on a coarse integer lattice so that ties occur.
"""
import random
from fractions import Fraction as F

random.seed(1)

def best_set(payoffs):
    m = max(payoffs.values())
    return {k for k, v in payoffs.items() if v == m}

def us_ai(a, nu, kA, kX, m_ai):
    # deny yields nu - k_a; supply yields 0, minus audience cost if exit and not denied
    if a == 'A':
        return best_set({'deny': nu - kA, 'supply': 0})
    return best_set({'deny': nu - kX, 'supply': -m_ai})

def us_firm(a, gamma, phiV, m_f):
    if a == 'A':
        return best_set({'pen': -phiV, 'no': 0})
    return best_set({'pen': gamma - phiV, 'no': -m_f})

def china_pun(a, g_r, m_r, g_r_after_X=None):
    if a == 'A':
        return best_set({'pun': g_r, 'no': -m_r})
    # paper asserts punishment after X "has no rationale"; model never specifies payoff
    if g_r_after_X is None:
        return {'no'}
    return best_set({'pun': g_r_after_X, 'no': 0})

n = 200000
tie_fail = {'ai': 0, 'firm': 0, 'china': 0}
generic_mismatch = 0
examples = {}
for _ in range(n):
    nu = random.randint(0, 6)
    kX = random.randint(0, 4)
    kA = kX + random.randint(1, 4)
    m_ai = random.randint(0, 3)
    gamma = random.randint(0, 4)
    phiV = random.randint(0, 6)          # phi*V, phi >= 0 allowed
    m_f = random.randint(0, 3)
    g_r = random.randint(-3, 3)
    m_r = random.randint(0, 3)
    alpha, f, r, eta = (random.randint(0, 5) for _ in range(4))
    # chi formulas from eq. (chi)
    chi_ai = int(nu + m_ai >= kX) * int(nu < kA)
    chi_f = int(phiV <= gamma + m_f)
    chi_r = int(g_r + m_r >= 0)
    # brute-force sets
    aiA, aiX = us_ai('A', nu, kA, kX, m_ai), us_ai('X', nu, kA, kX, m_ai)
    fA, fX = us_firm('A', gamma, phiV, m_f), us_firm('X', gamma, phiV, m_f)
    cA = china_pun('A', g_r, m_r)
    # possible conditional AI costs across all SPE selections
    ai_costs = {alpha * ((dx == 'deny') - (da == 'deny')) for dx in aiX for da in aiA}
    f_costs = {f * ((px == 'pen') - (pa == 'pen')) for px in fX for pa in fA}
    r_costs = {r * (p == 'pun') for p in cA}
    ok_ai = ai_costs == {alpha * chi_ai}
    ok_f = f_costs == {f * chi_f}
    ok_r = r_costs == {r * chi_r}
    if not ok_ai and alpha > 0:
        tie_fail['ai'] += 1
        examples.setdefault('ai', dict(nu=nu, kX=kX, kA=kA, m_ai=m_ai, sets=(aiA, aiX)))
    if not ok_f and f > 0:
        tie_fail['firm'] += 1
        examples.setdefault('firm', dict(gamma=gamma, phiV=phiV, m_f=m_f, sets=(fA, fX)))
    if not ok_r and r > 0:
        tie_fail['china'] += 1
        examples.setdefault('china', dict(g_r=g_r, m_r=m_r, sets=cA))
    # generic check: drop draws with any tie
    tie = (nu + m_ai == kX) or (nu == kA) or (phiV == gamma + m_f) or (phiV == 0) or (g_r + m_r == 0)
    if not tie and not (ok_ai and ok_f and ok_r):
        generic_mismatch += 1

print('draws', n)
print('generic (no-tie) mismatches:', generic_mismatch)
print('"every SPE" failures at ties (instrument has positive cost):', tie_fail)
for k, v in examples.items():
    print(' example', k, v)

# Security: expected loss with crisis probability q is q*(1-pi_a)*S, so exit adds q*kappa*S, not kappa*S
q = F(1, 4); S = 10; piA = F(9, 10); piX = F(3, 10)
print('security exit cost with crisis prob q=1/4:', q * (piA - piX) * S, ' vs paper kappa*S =', (piA - piX) * S)
