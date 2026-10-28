# Brute-force checks of Proposition 6(c) (blocking minorities, K(0) and K(B)).
# Model: members i=1..n, net gain q_i from adopting. US pays tau_i >= 0 (vote-contingent, paid for voting no).
# No rival: i votes yes iff q_i > tau_i. Rival (moves second, values adoption at B) offers bribes b_i >= 0 for yes;
# i votes yes iff q_i + b_i > tau_i (strict; indifferent members vote no). Rival bids only if strictly profitable.
import itertools, math, random, sys
import numpy as np
from scipy.optimize import linprog

def subsets(n):
    for r in range(n + 1):
        for S in itertools.combinations(range(n), r):
            yield frozenset(S)

def make_game(n, kind, w=None):
    """Return list of winning (qualified-majority) coalitions."""
    N = frozenset(range(n))
    W = []
    for S in subsets(n):
        if kind == "maj":            # k-of-n
            win = len(S) >= w
        elif kind == "qmv":          # QMV-like: count >= ceil(.55n) and weight >= .65, unless fewer than mb non-yes
            wt, mb = w
            cnt_ok = len(S) >= math.ceil(0.55 * n - 1e-12)
            pop_ok = sum(wt[i] for i in S) >= 0.65 - 1e-12
            win = (cnt_ok and pop_ok) or (len(N - S) < mb and cnt_ok)
        elif kind == "weighted":
            wt, quota = w
            win = sum(wt[i] for i in S) >= quota - 1e-12
        if win:
            W.append(S)
    return W

def blocking_family(n, W):
    N = frozenset(range(n))
    Wset = set(W)
    return [S for S in subsets(n) if (N - S) not in Wset]

def K0(n, W, q):
    Bf = blocking_family(n, W)
    return min(sum(max(q[i], 0) for i in S) for S in Bf)

def KB(n, W, q, B, support=None):
    """Exact solution of min sum tau s.t. sum_{i in S}[tau_i - q_i]^+ >= B for all S in W,
    by enumerating which positive-q members are 'protected' (tau_i >= q_i); else tau_i = 0.
    support: optional set of members allowed to receive tau_i > 0."""
    pos = [i for i in range(n) if q[i] > 0]
    best, arg = math.inf, None
    for r in range(len(pos) + 1):
        for P in itertools.combinations(pos, r):
            P = set(P)
            lin = [i for i in range(n) if q[i] <= 0 or i in P]   # members in the linear region
            bounds = []
            ok = True
            for i in range(n):
                lo = max(q[i], 0) if i in P else 0.0
                hi = 0.0 if (q[i] > 0 and i not in P) else None
                if support is not None and i not in support:
                    if lo > 0:
                        ok = False
                    hi = 0.0
                bounds.append((lo, hi))
            if not ok:
                continue
            A, b = [], []
            feas = True
            for S in W:
                row = [-1.0 if (i in S and i in lin) else 0.0 for i in range(n)]
                rhs = -(B + sum(q[i] for i in S if i in lin))
                if all(v == 0 for v in row):
                    if 0 > rhs + 1e-12 or -0.0 < rhs - 1e-12 and False:
                        pass
                    # constraint: 0 >= B  (no linear members in S): infeasible since B>0
                    if B > 1e-15:
                        feas = False; break
                    continue
                A.append(row); b.append(rhs)
            if not feas:
                continue
            res = linprog(np.ones(n), A_ub=np.array(A) if A else None, b_ub=np.array(b) if b else None,
                          bounds=bounds, method="highs")
            if res.status == 0 and res.fun < best - 1e-12:
                best, arg = res.fun, res.x
    return best, arg

def rival_cost_formula(W, q, tau):
    return min(sum(max(tau[i] - q[i], 0.0) for i in S) for S in W)

def rival_buys_bruteforce(n, W, q, tau, B, eps):
    """Rival chooses bribes on grid eps*{0,1,...}; i votes yes iff q_i + b_i > tau_i.
    Returns True if some bribe vector yields adoption with strictly positive profit B - sum bribes."""
    # cheapest grid bribe for each member to vote yes
    need = []
    for i in range(n):
        if q[i] > tau[i]:
            need.append(0.0)
        else:
            k = math.floor((tau[i] - q[i]) / eps + 1e-9) + 1
            need.append(k * eps)
    # exhaustive over all bribe vectors would be the same as choosing a yes-set; enumerate yes-sets
    best = -math.inf
    for S in subsets(n):
        yes = set(S) | {i for i in range(n) if q[i] > tau[i]}
        cost = sum(need[i] for i in S)
        adopted = frozenset(yes) in set(W) or any(frozenset(yes) >= Wc for Wc in W)
        prof = (B if adopted else 0.0) - cost
        best = max(best, prof)
    return best > 1e-12

def bruteforce_US(n, W, q, B, grid, eps):
    """US grid search: min sum tau on grid^n such that rival (bribe grid eps) does not buy and no-rival
    vote does not adopt."""
    best = math.inf; arg = None
    for tau in itertools.product(grid, repeat=n):
        s = sum(tau)
        if s >= best:
            continue
        if not rival_buys_bruteforce(n, W, q, tau, B, eps):
            best, arg = s, tau
    return best, arg

if __name__ == "__main__":
    # 1. Paper's example: three members, adoption by two, q = 0
    W = make_game(3, "maj", 2)
    q = [0, 0, 0]; B = 1.0
    print("Example 3 members, 2-of-3, q=0, B=1: K(0) =", K0(3, W, q), " K(B) =", KB(3, W, q, B)[0])

    # 2. Rival response: formula vs brute-force bribing on a fine grid, random tau (including exact ties)
    random.seed(7)
    mism = 0; tot = 0; tie_mism = 0
    for trial in range(3000):
        n = random.randint(3, 5)
        kind = random.choice(["maj", "qmv", "weighted"])
        if kind == "maj":
            W = make_game(n, "maj", random.randint(n // 2 + 1, n))
        elif kind == "qmv":
            wt = np.random.dirichlet(np.ones(n)); W = make_game(n, "qmv", (wt, random.choice([1, 2])))
        else:
            wt = np.random.dirichlet(np.ones(n)); W = make_game(n, "weighted", (wt, random.uniform(0.5, 0.8)))
        if not W:
            continue
        q = [random.choice([-1, -0.5, 0, 0.5, 1, 2]) for _ in range(n)]
        B = random.choice([0.5, 1, 1.5, 2, 3])
        tau = [random.choice([0, 0.5, 1, 1.5, 2, 2.5]) for _ in range(n)]
        f = rival_cost_formula(W, q, tau)
        pred = f < B
        act = rival_buys_bruteforce(n, W, q, tau, B, eps=1e-4)
        tot += 1
        if pred != act:
            # classify: within n*eps of a tie?
            if abs(f - B) < n * 1e-4 + 1e-9 or any(abs(tau[i] - q[i]) < 1e-12 for i in range(n)):
                tie_mism += 1
            else:
                mism += 1
    print(f"Rival-response check: {tot} draws, non-tie mismatches {mism}, tie-only mismatches {tie_mism}")

    # 3. US optimum: exact enumeration LP vs grid search with a fine-grid rival
    random.seed(11)
    worst = 0; cnt = 0
    for trial in range(60):
        n = random.choice([3, 3, 4])
        kind = random.choice(["maj", "qmv", "weighted"])
        if kind == "maj":
            W = make_game(n, "maj", random.randint(n // 2 + 1, n))
        elif kind == "qmv":
            wt = np.random.dirichlet(np.ones(n)); W = make_game(n, "qmv", (wt, random.choice([1, 2])))
        else:
            wt = np.random.dirichlet(np.ones(n)); W = make_game(n, "weighted", (wt, random.uniform(0.5, 0.8)))
        if not W:
            continue
        q = [random.choice([-1, -0.5, 0, 0.5, 1]) for _ in range(n)]
        B = random.choice([1.0, 2.0])
        h = 0.5 if n == 4 else 1/6
        top = max(q) + B + 0.5
        grid = [k * h for k in range(int(top / h) + 1)]
        g, ga = bruteforce_US(n, W, q, B, grid, eps=1e-3)
        e, ea = KB(n, W, q, B)
        cnt += 1
        # grid optimum must be >= exact LP value - n*eps (rival grid makes deterrence slightly cheaper)
        # and <= exact + n*h (grid coarseness)
        if g < e - n * 1e-3 - 1e-9 or g > e + n * h + 1e-9:
            print("MISMATCH", n, kind, q, B, "grid", g, ga, "exact", e, ea)
        worst = max(worst, e - g)
    print(f"US-optimum check: {cnt} games, max(exact - grid) = {worst:.4f} (should be <= n*eps)")
