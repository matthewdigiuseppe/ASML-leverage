import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import linprog
from nested_check import make_game, K0, KB
from hedge_check import contest_US_payoff
from holdup_b import T0, paper

# 6(c): the program is not linear. Naive linearization sum_{i in S}(tau_i - q_i) >= B vs exact value.
W = make_game(3, "maj", 2); q = [10.0, 0.0, 0.0]; B = 1.0
A = []; b = []
for S in W:
    A.append([-1.0 if i in S else 0.0 for i in range(3)]); b.append(-(B + sum(q[i] for i in S)))
lin = linprog(np.ones(3), A_ub=np.array(A), b_ub=np.array(b), bounds=[(0, None)] * 3, method="highs")
print("6(c) q=(10,0,0), 2-of-3, B=1: exact K(B) =", KB(3, W, q, B)[0], "tau =", KB(3, W, q, B)[1], "; naive LP =", lin.fun, lin.x, "; K(0) =", K0(3, W, q))
# feasible set non-convex: (2,0) and (0,2) on members 2,3 with q=1 each, S={2,3}
qq = [1, 1]; f = lambda t: sum(max(t[i] - qq[i], 0) for i in range(2))
print("  nonconvexity: f(2,0) =", f((2, 0)), "f(0,2) =", f((0, 2)), "f(1,1) =", f((1, 1)), "(B = 1)")

# 8: clean counterexample when Q + D_k > V
Q, D, V, BU, m, g = 0.0, 2.0, 1.0, 1.0, 0.0, 1.5
c = 3.0 - Q
u_no = -m + contest_US_payoff(c, 3.0, 5.0, V, BU); u_wh = g + contest_US_payoff(c - D, 3.0, 5.0, V, BU)
print("8: Q=0, D_k=2, V=B_U=1, m_k=0, g_k(H)=1.5: formula says credible:", m + g >= max(Q + D, 0) - max(Q, 0),
      "; brute force:", u_wh >= u_no, "(", u_wh, "vs", u_no, ")")
Q, D, V, BU, m, g = 0.0, 2.0, 5.0, 1.0, 0.0, 2.0
c = 3.0 - Q
u_no = -m + contest_US_payoff(c, 3.0, 5.0, V, BU); u_wh = g + contest_US_payoff(c - D, 3.0, 5.0, V, BU)
print("8: Q=0, D_k=2, V=5, B_U=1, m_k=0, g_k(H)=2: formula says credible:", m + g >= max(Q + D, 0) - max(Q, 0),
      "; brute force:", u_wh >= u_no, "(", u_wh, "vs", u_no, ")")

# 7(b): tie (1-psi)u = psi(a+l) not excluded by the stated genericity condition
p = (0.5, 0.2, 0.1, 0.3, 1.0)
print("7(b) tie psi=.5,a=.2,l=.1,u=.3,tauU=1: paper predicts", paper(*p), "; T0 with w(T)=1:", round(T0(*p, 0.002, 40, 1.0), 4), ", w(T)=0:", round(T0(*p, 0.002, 40, 0.0), 4))
