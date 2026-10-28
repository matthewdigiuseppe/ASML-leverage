# Checks for the "chokepoint attrition with buffers" proposal.
# Random-proposer bargaining with flow (fixed per-period) costs, normalized by stakes.
# W(t) = expected share of E (p = 1-q, q = scope of US control) at start of period t.
# W(t) = psi*max(W(t+1)-cE(t),0) + (1-psi)*min(1, W(t+1)+cU(t))
import random, math

def solve(psi, cE_fun, cU_fun, T, W_T):
    W = W_T
    for t in range(T-1, -1, -1):
        W = psi*max(W - cE_fun(t), 0.0) + (1-psi)*min(1.0, W + cU_fun(t))
    return W

def formula(psi, cE, cU, D):
    # continuous-time limit; cE, cU are per-unit-time normalized costs post-buffer; D = tauU - tauE
    if psi*cE < (1-psi)*cU:
        return max(0.0, 1 - psi*cE*D) if D >= 0 else 1.0
    else:
        return 0.0 if D >= 0 else min(1.0, (1-psi)*cU*(-D))

random.seed(1)
dt = 0.001
maxerr = 0.0
worst = None
for trial in range(400):
    psi = random.uniform(0.2, 0.8)
    cE = random.uniform(0.05, 2.0)
    cU = random.uniform(0.05, 2.0)
    tauU = random.uniform(0, 3)
    tauE = random.uniform(0, 3)
    if abs(psi*cE - (1-psi)*cU) < 0.05: continue
    T = int((max(tauU, tauE) + 8) / dt)
    cEf = lambda t: cE*dt if t*dt >= tauE else 0.0
    cUf = lambda t: cU*dt if t*dt >= tauU else 0.0
    # uniqueness check: two terminal conditions
    w0 = solve(psi, cEf, cUf, T, 0.0)
    w1 = solve(psi, cEf, cUf, T, 1.0)
    f = formula(psi, cE, cU, tauU - tauE)
    err = max(abs(w0-f), abs(w1-f))
    if err > maxerr:
        maxerr = err; worst = (psi, cE, cU, tauU, tauE, w0, w1, f)
print("A1 max abs error vs formula:", round(maxerr,4), worst)

# A2: credible hold-up. Without interruption: cU = gamma (tiny, from t=0), cE = (1-phi)*alpha after tauE.
# With interruption: cE = (1-phi)*(alpha*1{t>=tauE} + ell), cU = gamma + beta*1{t>=tauU}. (normalized by stakes)
viol = 0; n = 0
for trial in range(300):
    psi = random.uniform(0.3, 0.7)
    alpha = random.uniform(0.1, 2); ell = random.uniform(0.0, 0.5); phi = random.uniform(0, 0.6)
    beta = random.uniform(0.1, 3); gamma = 0.01
    tauU = random.uniform(0, 4); tauE = 0.0
    T = int((tauU + 8)/dt)
    noint = solve(psi, lambda t: (1-phi)*alpha*dt, lambda t: gamma*dt, T, 0.5)
    cEi = (1-phi)*(alpha+ell)
    withint = solve(psi, lambda t: cEi*dt, lambda t: (gamma + (beta if t*dt >= tauU else 0))*dt, T, 0.5)
    strong = psi*cEi < (1-psi)*(beta+gamma)
    pred_cred = strong and (psi*cEi*tauU - (1-psi)*gamma*tauU < 1)
    if abs(psi*cEi - (1-psi)*(beta+gamma)) < 0.05 or abs(psi*cEi*tauU - (1-psi)*gamma*tauU - 1) < 0.02: continue
    n += 1
    actual_cred = withint > noint + 1e-3
    if pred_cred != actual_cred: viol += 1
print("A2 credible hold-up condition violations:", viol, "of", n)
