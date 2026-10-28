# T-period preventive control. State: E holds control at start of t. U may issue a public ultimatum
# (audience cost up to mbar). Accept: control transfers for all remaining periods; E pays sig + rc (one-time), gets T.
# Refuse: U cuts AI in period t iff mbar + gN >= [Q_t+a_t]^+ - [Q_t]^+ (strict: >), cut lasts one period.
# Claim to test: U issues at some t iff exists t with credible cut, bite_t > sig+rc, and some s>t with Q_s>0.
import random
pos = lambda x: max(0.0, x)
def solve(Q, a, d, sig, rc, mbar, gN):
    T = len(Q)
    VE, VU = 0.0, 0.0   # continuation after last period
    issued_any = False
    for t in range(T-1, -1, -1):
        nE = pos(Q[t]) + d*VE; nU = -pos(Q[t]) + d*VU
        drent = pos(Q[t]+a[t]) - pos(Q[t])
        cred = mbar + gN > drent + 1e-12
        if cred:
            rE = pos(Q[t]+a[t]) - a[t] + d*VE; rU = gN - pos(Q[t]+a[t]) + d*VU
        else:
            rE, rU = nE, nU - mbar   # would not issue anyway
        Tst = pos(rE - (-sig - rc))
        if cred and -Tst > nU + 1e-12:
            VE, VU = Tst - sig - rc, -Tst
            issued_at = t
            issued_any = True
            # note: subgame from t on; earlier periods see this continuation
        else:
            VE, VU = nE, nU
    return issued_any
def pred(Q, a, d, sig, rc, mbar, gN):
    T = len(Q)
    for t in range(T):
        drent = pos(Q[t]+a[t]) - pos(Q[t]); cred = mbar + gN > drent + 1e-12
        bite = min(a[t], pos(-Q[t]))
        if cred and bite > sig + rc + 1e-12 and any(Q[s] > 1e-12 for s in range(t+1, T)):
            return True
    return False
random.seed(11); mism = 0; n = 100000
for _ in range(n):
    T = random.randint(2, 6)
    q0 = random.uniform(-5, 1); steps = [random.uniform(-0.5, 2.0) for _ in range(T)]
    Q = []; x = q0
    for s in steps: Q.append(x); x += s
    a = [random.uniform(0, 3) for _ in range(T)]
    d = random.uniform(0.5, 1); sig = random.uniform(0, 1.5); rc = random.uniform(0, 1)
    mbar = random.choice([0.0, random.uniform(0, 5)]); gN = random.choice([0.0, -random.uniform(0, 1)])
    s1 = solve(Q, a, d, sig, rc, mbar, gN); p1 = pred(Q, a, d, sig, rc, mbar, gN)
    if s1 != p1:
        mism += 1
        if mism < 6: print('mismatch', [round(q,2) for q in Q], [round(x,2) for x in a], round(d,2), round(sig,2), round(rc,2), round(mbar,2), round(gN,2), s1, p1)
print('draws', n, 'mismatches', mism)
