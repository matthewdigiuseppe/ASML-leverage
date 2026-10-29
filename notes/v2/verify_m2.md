# Verification report m2: Proposition 6, interruption corollary, Remarks G, F, E

Scripts (run with `python3 -I`, all under 15 seconds):

- `code/checks/v2_m2_prop6_holdup.py`: Proposition 6 (backward induction, time-varying costs).
- `code/checks/v2_m2_interruption.py`: interruption corollary (four timing and buffer models).
- `code/checks/v2_m2_remarks_GFE.py`: Remarks G, F, E (Council arithmetic from `pop_check.py`).

Notation: $\rho \equiv r+\lambda$, $\omega_b \equiv \lambda/\rho$ (the memo's $w_b$), $M \equiv Q+\beta(V-Q)$, $\pos{x} \equiv \max\{x,0\}$, $\Lambda \equiv \pos{-Q}$. Throughout, $r>0$, $\beta\in[0,1)$, $Q<V$.

| Result | Verdict | One-line summary |
|---|---|---|
| Prop. 6 | corrected | Formula right; "exit never binds" is exactly $Q \le \inf_{t\ge 0} x_F(t)$, not a condition at $t=0$; general value is an optimal-stopping value; immediate agreement can fail when $\lambda=0$ and $c_E+c_U=0$ on an interval. |
| Interruption corollary | corrected | Confirmed for the stock buffer with exit not binding, and the decision is time consistent. When exit binds, the memo condition is necessary but not sufficient. The condition fails under a calendar-time buffer. With interruption chosen after offers it is never used ($\ell>0$). With interruption chosen after the proposer is drawn, $\ell$ drops out. |
| Remark G | confirmed (qualified) | Identities hold if $x_h$ is part of the baseline, with credible withdrawal. If $x_h$ is a promised increment above baseline, U saves nothing. |
| Remark F | confirmed | Firm ships iff $y+p_C+p_B \ge f^F$ (ties ship); effective premium $Q-\zeta\,\mathbf 1\{\cdot\}$. |
| Remark E | corrected | Stage-1 rule confirmed. The frontline core cannot block. A 13-member eastern/Nordic group blocks by count with 26.77%. Delegated act: 8 members (3.18%) or 3 large members keep it in force, because no four-member clause applies. Members with $q_i<0$ join a blocking coalition for free, but $\Phi(0)=0$ only if they themselves form one. |

---

## 1. Proposition 6 (pain and breakdown)

**Verdict: corrected.** The memo's formula is the correct frequent-offer limit whenever exit never binds, and the numerics confirm it to $3\times 10^{-7}$. Three things need fixing. (i) The exact condition for "exit never binds" is a condition on the whole forward path, $Q\le\inf_{t\ge0}x_F(t)$. Checking only at $t=0$ is not enough, and I give a counterexample. (ii) Without that condition, the limit value is an optimal-stopping value, which is strictly above the formula. (iii) "Immediate agreement" needs $\lambda>0$, or $c_E+c_U>0$ at the round in question. Otherwise there are payoff-equivalent equilibria with delay.

**Ambiguities fixed.** Rounds start at $t_k=k\Delta$. After a rejection the order is as follows. If U proposed, E may exit (normalized value $Q$ to E, $-V$ to U). Otherwise breakdown occurs with probability $\mu=1-e^{-\lambda\Delta}$, with the same values. Otherwise the status quo runs for the period with normalized flows $-c_E(t_k)$ and $-c_U(t_k)$ (weight $1-\delta$, $\delta=e^{-r\Delta}$), and play moves to round $k+1$. The costs $c_i$ are in the same normalized flow units as $Q$ and $V$. They are bounded, and each unit interval has at most $N$ discontinuity points, with $c_i$ uniformly continuous between them. "Markov" means that strategies depend only on the round index (calendar time) and the current offer.

### Final statement

```latex
\begin{proposition}[Pain and breakdown]\label{prop:pain}
Consider the game of Proposition~1 with disagreement flow costs $c_E(t),c_U(t)\ge 0$, bounded and
piecewise uniformly continuous with finitely many discontinuities in every bounded interval. Let
$\rho=r+\lambda$, $\omega_b=\lambda/\rho$, $M=Q+\beta(V-Q)$,
$\hat C_i(t)=\rho\int_0^\infty e^{-\rho s}c_i(t+s)\,ds$, $G(t)=\beta\hat C_U(t)-(1-\beta)\hat C_E(t)$ and
\[ x_F(t)=\omega_b M+(1-\omega_b)\,G(t). \]
\begin{enumerate}
\item For every $\Delta>0$ Europe's Markov perfect equilibrium payoff is unique. In every round in which
$\lambda>0$ or $c_E+c_U>0$, every Markov perfect equilibrium has immediate agreement. If $\lambda=0$ and
$c_E(t)+c_U(t)=0$ on an interval, there are also payoff-equivalent equilibria with delay during that interval.
\item As $\Delta\to 0$, Europe's equilibrium payoff converges to
\[ P^*=\sup_{\tau\in[0,\infty]}\Big\{\int_0^\tau e^{-\rho s}\big(\lambda M+r\,g(s)\big)ds+e^{-\rho\tau}Q\Big\}
      = x_F(0)+\pos{\sup_{t\ge 0}e^{-\rho t}\big(Q-x_F(t)\big)}, \]
where $g=\beta c_U-(1-\beta)c_E$.
\item $P^*=x_F(0)=\omega_b[Q+\beta(V-Q)]+(1-\omega_b)[\beta\hat C_U-(1-\beta)\hat C_E]$ if and only if
\[ Q\le \inf_{t\ge 0}x_F(t)\quad\Longleftrightarrow\quad
   Q\le \bar Q\equiv \inf_{t\ge 0}\frac{\lambda\beta V+r\,G(t)}{r+\lambda\beta}. \]
Under this condition the limiting equilibrium value at every date $t$ is $x_F(t)$, so the exit option is never
used. The condition $Q\le x_F(0)$ alone is not sufficient. With constant costs, $P^*=\max\{Q,x_F\}$.
\end{enumerate}
\end{proposition}
```

### Proof

```latex
\begin{proof}
\emph{Recursion.} Fix $\Delta$ and write $c_{i,k}=c_i(t_k)$, $g_k=\beta c_{U,k}-(1-\beta)c_{E,k}$ and
$\kappa=\delta(1-\mu)=e^{-\rho\Delta}$. In a Markov equilibrium the continuation after a rejection does not depend
on the rejected offer. Let $x_{k+1}$ be Europe's value at the start of round $k+1$. All outcomes are agreements
(which sum to zero), exit (which sums to $Q-V<0$) or disagreement flows (which sum to at most zero), and
agreement is immediate (shown below). So the United States' value is $-x_{k+1}$. If the United States rejects
Europe's offer, its value is $-\mu V+(1-\mu)[-(1-\delta)c_{U,k}-\delta x_{k+1}]$. Europe therefore offers
$P_{E,k}=\mu V+(1-\mu)[(1-\delta)c_{U,k}+\delta x_{k+1}]$, and the United States accepts (acceptance at
indifference is needed for an optimal offer to exist). If Europe rejects the United States' offer, its value is
$\max\{Q,d_{E,k}\}$ with $d_{E,k}=\mu Q+(1-\mu)[-(1-\delta)c_{E,k}+\delta x_{k+1}]$. The United States offers
exactly this. Hence
\[ x_k=\Phi_k(x_{k+1})\equiv \beta P_{E,k}+(1-\beta)\max\{Q,d_{E,k}\}=\max\{A_k(x_{k+1}),B_k(x_{k+1})\}, \]
\[ A_k(x)=\mu M+(1-\mu)(1-\delta)g_k+\kappa x,\qquad
   B_k(x)=(1-\beta)Q+\beta\big[\mu V+(1-\mu)(1-\delta)c_{U,k}+\kappa x\big]. \]
\emph{Part 1.} Each $\Phi_k$ is nondecreasing with modulus $\kappa<1$, so $(x_k)\mapsto(\Phi_k(x_{k+1}))$ is
a contraction on bounded sequences. Its unique fixed point is the unique Markov equilibrium value, since all
payoffs are bounded. A proposer gains from making an acceptable offer, rather than an unacceptable one, by
$\mu(V-Q)+(1-\mu)(1-\delta)(c_{E,k}+c_{U,k})$ when Europe proposes. When the United States proposes and exit
does not bind, the gain is the same. When exit binds, the gain is at least $V-Q>0$. This gain is strictly
positive if $\lambda>0$ (because $Q<V$) or if $c_{E,k}+c_{U,k}>0$. If it is zero, both offers give the same
payoffs, so delay is payoff equivalent.

\emph{Part 2.} By standard dynamic programming for monotone contractions, $x_0$ is the largest value of
$\sigma_0\circ\sigma_1\circ\cdots$ over sequences $\sigma_k\in\{A_k,B_k\}$. Let
$h(s)=\lambda M+r g(s)$, $J_t(\tau)=\int_t^\tau e^{-\rho(s-t)}h(s)ds+e^{-\rho(\tau-t)}Q$ and
$W(t)=\sup_{\tau\ge t}J_t(\tau)$. $W$ is bounded, $W\ge Q$, and $W(t)\ge\int_t^{t+\Delta}e^{-\rho(s-t)}h\,ds+
e^{-\rho\Delta}W(t+\Delta)$. The last inequality gives $W(t+\Delta)\le W(t)+C\Delta$.

(Lower bound.) Fix $\tau<\infty$ and use $A$ in rounds with $t_k<\tau$ and $B$ afterwards. Using $B$ forever
from round $K$ gives a value $v_K$ with $|v_K-Q|\le C\Delta/(1-\beta)$, since $B$ puts weight $1-\beta$ on $Q$
and has modulus $\beta\kappa$. Using $A$ in round $k$ adds
$\mu M+(1-\mu)(1-\delta)g_k=\int_{t_k}^{t_{k+1}}e^{-\rho(s-t_k)}h\,ds+\varepsilon_k$, with
$|\varepsilon_k|\le C\Delta^2+r\Delta\,\mathrm{osc}_{[t_k,t_{k+1}]}g$. Summing with weights $\kappa^k$ gives a
total error of $O(\Delta)+(r/\rho)\,\varpi(\Delta)+O(N\Delta)$, where $\varpi$ is the modulus of continuity of
$g$ between jumps. The $O(N\Delta)$ term covers the rounds that contain a jump. So the policy value tends to
$J_0(\tau)$, and $\liminf x_0\ge\sup_\tau J_0(\tau)$. The case $\tau=\infty$ is a limit of finite $\tau$.

(Upper bound.) By the inequalities above, $W(t_k)\ge A_k(W(t_{k+1}))-\varepsilon_k$. Also
$B_k(W(t_{k+1}))\le(1-\beta)W(t_k)+\beta W(t_k)+C\Delta$, because $Q\le W(t_k)$ and
$W(t_{k+1})\le W(t_k)+C\Delta$. For any policy, let $e_k=\pos{v_k-W(t_k)}$. Then $e_k\le\kappa e_{k+1}+\varepsilon_k$
after an $A$ step and $e_k\le \beta e_{k+1}+C\Delta$ after a $B$ step. The $m$-th $B$ step's error is discounted
by $\beta^{m-1}$, so all $B$ steps together contribute at most $C\Delta/(1-\beta)$. The $A$ steps contribute
$\sum_k\kappa^k|\varepsilon_k|\to 0$ as in the lower bound, and the tail beyond a long horizon is negligible
because $\kappa^k\to0$ and everything is bounded. Hence $\limsup x_0\le W(0)$, and $P^*=W(0)$.

\emph{Part 3.} Because $\int_\tau^\infty e^{-\rho s}h(s)ds=e^{-\rho\tau}x_F(\tau)$, we have
$J_0(\tau)=x_F(0)-e^{-\rho\tau}(x_F(\tau)-Q)$, and $J_0(\infty)=x_F(0)$. This gives the second expression for
$P^*$. It also shows that $P^*=x_F(0)$ if and only if $x_F(\tau)\ge Q$ for every $\tau$. Next,
$\rho(x_F(t)-Q)=\lambda\beta(V-Q)+r(G(t)-Q)$, so $x_F(t)\ge Q$ is equivalent to
$Q(r+\lambda\beta)\le\lambda\beta V+rG(t)$. Applying the same argument from any date $t$ shows that the limit
value at $t$ is $W(t)=x_F(t)$ for all $t$ exactly under this condition. With constant costs $x_F$ is constant, and
$P^*=\max\{Q,x_F\}$. Counterexample to the condition at $t=0$ only: take $\beta=\lambda=0$, $r=\tfrac12$,
$c_U=0$, $c_E=0$ on $[0,2)$ and $c_E=2$ afterwards, and $Q=-1$. Then $x_F(0)=-2e^{-1}\approx-0.736\ge Q$, but
$x_F(t)=-2<Q$ for $t\ge2$. Hence $P^*=x_F(0)+e^{-1}(Q+2)=-e^{-1}\approx-0.368$, which exceeds the formula.
\end{proof}
```

### Numerical check

`v2_m2_prop6_holdup.py` solves the discrete game by backward induction on the $\Delta$-grid. It does not use the formula. Costs are random piecewise-constant paths with up to three breaks, and are constant after a random date $T_0\le 4$, where the exact stationary fixed point of the discrete recursion (including the exit floor) is the terminal value. I drew 6,000 parameter sets with $r\in(0.05,1.5)$, $\lambda=0$ in 20% of draws, $\beta=0$ in 15%, and $Q$ placed below, above, at, and around the exact threshold $\bar Q$. I used $\Delta=0.002$ and $0.001$ with Richardson extrapolation. The maximum error against the formula when $Q\le\bar Q$ is $3.1\times10^{-7}$ (at $Q=\bar Q$ exactly: $2.1\times10^{-4}$). The test $Q\le\bar Q$ classifies all 6,000 draws in the same way as the test $Q\le\inf_tx_F(t)$. Whenever exit binds, the backward-induction value exceeds the formula in every draw. Against the stopping value the error converges at first order: $1.4\times10^{-1}$, $7.3\times10^{-2}$, $3.8\times10^{-2}$, $1.9\times10^{-2}$, $9.7\times10^{-3}$ for $\Delta=0.004,\dots,0.00025$, with mean errors $3.6\times10^{-3}$ down to $2.3\times10^{-4}$. The largest errors are at $\beta$ near $0.95$, where the exit-floor branch carries a factor $1/(1-\beta)$. The counterexample above reproduces: backward induction gives $-0.3679$ and the formula gives $-0.7358$. Edge cases nest Proposition 1 exactly: $\lambda=0$ with $c=0$ gives $\pos{Q}$, and constant costs give $\max\{Q,x_F\}$.

---

## 2. Interruption corollary

**Verdict: corrected.** In the memo's model (the US buffer is a stock that depletes only in rounds with interruption, and interruption is chosen at the start of each round before the proposer is drawn), the condition and the time-consistency claim are both right, provided exit does not bind. Corrections and additions: (a) when exit binds, the exact condition has an extra term, and the memo condition is necessary but not sufficient; (b) the result depends on the stock model, and with a calendar-time buffer the condition is wrong; (c) if interruption is chosen after offers within a round, it is never used when $\ell>0$; (d) if it is chosen after the proposer is drawn but before offers, the cost $\ell$ drops out of the condition.

**Setup fixed.** Baseline disagreement flows are $c_E^0$ and $c_U^0$. These may include the US cost of an AI cut, from $t=0$. In a round with interruption, Europe's disagreement flow rises by $\ell$. The United States' flow rises by $(1-h)c_S$ only if the stock $b$ is exhausted at the start of the round. The stock falls by $\Delta$ in each round with interruption and stays put otherwise, starting at $b=t_U$. Write $D\equiv\beta(1-h)c_S e^{-\rho t_U}-(1-\beta)\ell$ and $K\equiv\beta(1-h)c_S-(1-\beta)\ell$. The no-interruption value is $x_F^0$, as in Proposition 6.

### Final statement

```latex
\begin{corollary}[Interruption]\label{cor:interrupt}
Let Europe choose, at the start of each round and before the proposer is drawn, whether servicing is
interrupted. Interruption costs Europe a flow $\ell$, and costs the United States a flow $(1-h)c_S$ once its
buffer is exhausted. The buffer is a stock of $t_U$ units of interruption time, depleted only in rounds with
interruption. Let $D=\beta(1-h)c_S e^{-\rho t_U}-(1-\beta)\ell$. In the frequent-offer limit:
\begin{enumerate}
\item If exit never binds without interruption (Proposition~\ref{prop:pain}(3) with the baseline costs), then
allowing interruption raises $P^*$ by $(1-\omega_b)\pos{D}$. Interruption raises $P^*$ if and only if
$\beta(1-h)c_S e^{-\rho t_U}>(1-\beta)\ell$, that is, if and only if
$t_U<\bar t\equiv \ln[\beta(1-h)c_S/((1-\beta)\ell)]/\rho$ (with $\bar t=\infty$ if $\ell=0<\beta(1-h)c_S$).
\item With constant baseline costs and the exit option,
$P^*=\max\{Q,\;x_F^0,\;x_F^0+(1-\omega_b)D\}$. Interruption raises $P^*$ if and only if
$(1-\omega_b)D>\pos{Q-x_F^0}$. If exit binds without interruption, the condition of part~1 is necessary but not
sufficient.
\item The decision is time consistent. At stock $b$, Europe interrupts if and only if
$\beta(1-h)c_S e^{-\rho b}>(1-\beta)\ell$. Along an interruption path $b$ falls, so the condition keeps holding.
If the condition fails at $t=0$, the stock never moves and the condition fails in every round.
\end{enumerate}
The result depends on the stock buffer and on the timing. (i) If the buffer runs out at calendar date $t_U$
whatever Europe does, Europe never interrupts before $t_U$. Interruption then raises $P^*$ by
$(1-\omega_b)e^{-\rho t_U}\pos{\beta(1-h)c_S-(1-\beta)\ell}$, so it helps if and only if
$\beta(1-h)c_S>(1-\beta)\ell$, for any finite $t_U$. (ii) If Europe chooses interruption after an offer is
rejected and $\ell>0$, the unique Markov equilibrium has no interruption, and $P^*$ is unchanged. (iii) If Europe
chooses after the proposer is drawn but before offers, Europe interrupts in the rounds in which it proposes, at no
cost on the equilibrium path. Interruption then raises $P^*$ whenever $\beta(1-h)c_S>0$ and $t_U<\infty$, by at
least $(1-\omega_b)\beta(1-h)c_S e^{-\rho t_U/\beta}$, whatever the value of $\ell$.
\end{corollary}
```

### Proof

```latex
\begin{proof}
\emph{Limit problem.} The state is $(t,b)$. As in the proof of Proposition~\ref{prop:pain}, Europe's value is
the value of a Bellman equation in which Europe chooses interruption $i_k\in\{0,1\}$ each round. The offers
depend on the state only through the continuation value, so Europe's choice maximizes its own continuation.
The convergence argument of Proposition~\ref{prop:pain}, applied state by state, gives the limit value: the
supremum, over measurable $i:[0,\infty)\to\{0,1\}$ and stopping times $\tau$, of
\[ J(i,\tau)=\int_0^\tau e^{-\rho s}\big(h_0(s)+r\,\Delta g(s)\big)ds+e^{-\rho\tau}Q, \qquad
\Delta g(s)=i(s)\big[-(1-\beta)\ell+\beta(1-h)c_S\mathbf 1\{B(s)=0\}\big], \]
where $h_0=\lambda M+r(\beta c_U^0-(1-\beta)c_E^0)$ and $B(s)=\pos{t_U-\int_0^s i}$. Let $T$ be the first date with
$B=0$ ($T\ge t_U$, and $T=\infty$ if the buffer is never exhausted).

\emph{Key bound.} For every $i$ and $\tau$,
\[ r\int_0^\tau e^{-\rho s}\Delta g(s)ds\le (1-\omega_b)\,e^{-\rho(T-t_U)}D\le (1-\omega_b)\pos{D}. \]
If $T>\tau$ the integrand is $-(1-\beta)\ell i\le 0$. Otherwise, before $T$ the interruption set has measure
$t_U$. The discounted cost $\int_0^T e^{-\rho s}i\,ds$ is smallest when this set is $[T-t_U,T]$ (a bathtub
argument), where it equals $e^{-\rho T}(e^{\rho t_U}-1)/\rho$. After $T$ the integrand is at most $\pos{K}$.
So the left side is at most
$\frac r\rho e^{-\rho T}\big[-(1-\beta)\ell(e^{\rho t_U}-1)+\pos{K}\big]$. If $K\ge0$ this equals
$(1-\omega_b)e^{-\rho(T-t_U)}D$. If $K<0$ it is negative, and so is $D$.

\emph{Part 1.} Since exit never binds without interruption, $\sup_\tau J(0,\tau)=J(0,\infty)=x_F^0(0)$. By the
key bound, $J(i,\tau)\le J(0,\tau)+(1-\omega_b)\pos{D}\le x_F^0(0)+(1-\omega_b)\pos{D}$. If $D>0$, the policy
$i\equiv1$, $\tau=\infty$ attains this. If $D\le 0$, $i\equiv0$ is optimal and interruption does not raise $P^*$.
Strictness and the threshold $\bar t$ follow because $D$ is strictly decreasing in $t_U$ and $r>0$ gives
$1-\omega_b>0$.

\emph{Part 2.} Let $\alpha=h_0-\rho Q$, a constant, so that $x_F^0-Q=\alpha/\rho$. Then
$J(i,\tau)-Q=\int_0^\tau e^{-\rho s}(\alpha+r\Delta g)ds$. If $T>\tau$, this is at most
$\int_0^\tau e^{-\rho s}\alpha\,ds\le\pos{\alpha}/\rho$. If $T\le\tau$, apply the bathtub step on $[0,T]$ and
bound the integrand on $[T,\tau]$ by $\pos{\alpha+rK}$. This gives
$J-Q\le[\alpha(1-e^{-\rho T})+e^{-\rho T}(\pos{\alpha+rK}-r(1-\beta)\ell(e^{\rho t_U}-1))]/\rho$.
If $\alpha+rK\ge0$, then, since $K-(1-\beta)\ell(e^{\rho t_U}-1)=e^{\rho t_U}D$, the bound equals
$\alpha/\rho+(1-\omega_b)e^{-\rho(T-t_U)}D$. This expression is affine in $e^{-\rho(T-t_U)}\in(0,1]$, so it is at
most $\max\{\alpha/\rho,\ \alpha/\rho+(1-\omega_b)D\}\le\max\{\pos{\alpha}/\rho,\ \alpha/\rho+(1-\omega_b)D\}$. If $\alpha+rK<0$, the bound is at most $\pos{\alpha}/\rho$. Hence
$J\le\max\{Q,x_F^0,x_F^0+(1-\omega_b)D\}$. The three terms are attained by $\tau=0$, by $(i\equiv0,\tau=\infty)$
and by $(i\equiv1,\tau=\infty)$. Without interruption the value is $\max\{Q,x_F^0\}$, which gives the
condition.

\emph{Part 3.} The problem from state $(t,b)$ is the same problem with $t_U$ replaced by $b$, so the optimal
choice there is $i=1$ if and only if $\beta(1-h)c_S e^{-\rho b}>(1-\beta)\ell$. Along $i\equiv1$ the stock is
$b=t_U-t$, and the left side rises with $t$. Without interruption $b$ stays at $t_U$.

\emph{(i) Calendar buffer.} Now $\Delta g(s)=i(s)[-(1-\beta)\ell+\beta(1-h)c_S\mathbf 1\{s\ge t_U\}]$, which
can be maximized pointwise: $i=1$ if and only if $s\ge t_U$ and $K>0$. This gives the increment
$(1-\omega_b)e^{-\rho t_U}\pos{K}$, and interruption before $t_U$ strictly lowers the value when $\ell>0$.

\emph{(ii) Choice after a rejection.} Ex post, Europe picks $i$ to maximize its own disagreement value
$\mu Q+(1-\mu)[-(1-\delta)(c_E^0+\ell i)+\delta x(b_i')]$. At $b=0$ interruption leaves the state unchanged and
costs $(1-\mu)(1-\delta)\ell>0$, so $i=0$, and $x(0)=y_0$, the no-interruption value. Suppose $x(b-\Delta)=y_0$.
If Europe interrupted at $b$, the value there would be $x_1=\Phi^{(1)}(y_0)$, with
$y_0-x_1\in[0,(1-\beta)(1-\mu)(1-\delta)\ell]$ (the two values differ only in the exit-floor term). Interrupting
would then change Europe's disagreement value by
$(1-\mu)[-(1-\delta)\ell+\delta(y_0-x_1)]\le(1-\mu)(1-\delta)\ell[-1+\delta(1-\beta)(1-\mu)]<0$. So $i=0$ is the
unique consistent choice, and $x(b)=y_0$. Induction over $b$ completes the argument.

\emph{(iii) Choice after the proposer is drawn.} When Europe proposes, its offer equals the United States'
disagreement value. Interruption raises this by $(1-\mu)(1-\delta)(1-h)c_S\mathbf 1\{b=0\}$ plus
$(1-\mu)\delta[x(b-\Delta)-x(b)]\ge0$. It does not involve Europe's own cost $\ell$, because the offer is
accepted. So Europe interrupts in all of its proposer rounds. The stock then falls at rate at least $\beta$ per
unit of disagreement time. After exhaustion, the flow gain is $r\beta(1-h)c_S$ with no cost. This gives the
stated lower bound, which is the value of the policy that interrupts only in Europe's proposer rounds.
\end{proof}
```

### Numerical check

`v2_m2_interruption.py` solves each model by backward induction over the buffer state, with the exit floor included and constant baselines. It uses 3,000 random draws (exit binds without interruption in 977), with $\lambda=0$ in 25%, $\beta=0$ in 10%, $h=0$ in 20%, $\ell=0$ in 5% and $t_U\in[0,3]$. I used $\Delta=0.002$ and $0.001$ with Richardson extrapolation. Results:

- **Memo model.** Max error against part 2's closed form is $8.1\times10^{-4}$.
  - The decision agrees with the exact condition $(1-\omega_b)D>\pos{Q-x_F^0}$ in all 2,834 non-tie draws (margin above $0.005$).
  - It agrees with the memo condition in all 1,862 non-tie draws where exit does not bind.
  - In 188 draws exit binds and the memo condition holds, yet interruption does not raise $P^*$.
  - Time consistency has 0 violations: every draw that interrupts at $b=t_U$ also interrupts at every lower stock, 1,048 draws in all.
  - At finite $\Delta$, exit-binding draws show spurious gains of $10^{-9}$ to $10^{-4}$. These vanish under extrapolation.
- **Calendar model.** Max error against $\max\{Q,x_F^0+(1-\omega_b)e^{-\rho t_U}\pos{K}\}$ is $8.1\times10^{-4}$. No draw interrupts before $t_U$. In 435 draws the memo condition fails, yet interruption raises $P^*$.
- **After-offer timing.** In the 2,852 draws with $\ell>0$, the gain is exactly 0 and the equilibrium is unique at every stock. With $\ell=0$ and ties broken toward interruption, it matches the memo model to $2\times10^{-16}$.
- **Proposer-known timing.** The value is never below the memo-timing value. In 551 of 1,070 eligible draws the gain is positive although the memo condition fails. The gain is at least the better of the two constant policies, up to $2\times10^{-3}$ (discretization at $\Delta=0.004/0.002$).
- **Hand-picked case.** With $r=0.2$, $\lambda=0.3$, $\beta=0.5$, $\ell=0.5$, $c_S=2$, $h=0$: $\bar t=2.773$. For $t_U=0.5$ the gain is $0.2115$, and for $t_U=2$ it is $0.0472$, both matching the closed form.

---

## 3. Remark G (gatekeeper, targeted benefit)

**Verdict: confirmed, with two qualifications.** The algebra is an identity. It needs (a) $x_h$ to be part of the baseline, meaning provision that U finds ex post optimal for a loyal gatekeeper (for example, a preferential AI tier). Its withdrawal on exit must be credible: execution cost at most $\bar m_U$. It also needs (b) Lemma 1's conditions before and after. If $x_h$ is instead a promised increment above baseline, U pays it on path. Its total outlay is then $x_h+\pos{Q_{NL}-x_h}=\max\{x_h,Q_{NL}\}\ge\pos{Q_{NL}}$, so the benefit saves nothing.

```latex
\begin{remark}[Gatekeeper]
Let $x_h\ge0$ be the value to the Netherlands of a benefit that the United States provides to a loyal
Netherlands in the baseline and credibly withdraws if the Netherlands licenses exit. Then
$Q_{NL}'=Q_{NL}-x_h$. If $Q_{NL}'<V$ and $Q_{NL}'\le\bar m_U$, the United States' payment falls from
$\pos{Q_{NL}}$ to $\pos{Q_{NL}-x_h}$, that is, by $\min\{x_h,\pos{Q_{NL}}\}$. The gatekeeper's slack rises from
$\pos{-Q_{NL}}$ to $\pos{x_h-Q_{NL}}$, that is, by $\pos{x_h-\pos{Q_{NL}}}$. If $Q_{NL}>\min\{V,\bar m_U\}$, the
benefit restores alignment if and only if $Q_{NL}-x_h\le\bar m_U$ (and $Q_{NL}-x_h<V$). A benefit paid as a
promised increment above the baseline lowers no payment, since the total outlay is
$\max\{x_h,Q_{NL}\}\ge\pos{Q_{NL}}$.
\end{remark}
\begin{proof}
Withdrawal on exit raises $c_{NL}$ by $x_h$, so $Q_{NL}$ falls by $x_h$. Lemma~1 gives the payment $\pos{Q}$.
For $x\ge0$: if $Q\le0$, then $\pos{Q}-\pos{Q-x}=0=\min\{x,\pos{Q}\}$, and
$\pos{x-Q}-\pos{-Q}=x=\pos{x-\pos{Q}}$. If $Q>0$, then $Q-\pos{Q-x}=\min\{x,Q\}$, and
$\pos{x-Q}-0=\pos{x-\pos{Q}}$. If $x_h$ is a transfer, Europe aligns if and only if $x_h+\tau\ge Q$, so the
cheapest outlay is $x_h+\pos{Q-x_h}=\max\{x_h,Q\}$.
\end{proof}
```

**Numerical check.** `v2_m2_remarks_GFE.py` brute-forces the least staked promise $\tau$ (on a $10^{-3}$ grid) that makes the gatekeeper align, and the largest reversible concession it accepts, before and after the benefit. It uses 20,000 draws, including $Q=0$, $x_h=0$ and $x_h=|Q|$ ties. The maximum error is $4\times10^{-16}$ for the rent and $9\times10^{-16}$ for the slack. In the transfer variant the saving is never positive.

---

## 4. Remark F (firm between jurisdictions)

**Verdict: confirmed.** Under a licence, the firm compares shipping, $y-f^F$, with complying with US measures, $-p_C-p_B$, and ships iff $y+p_C+p_B\ge f^F$ (ties ship). If it would not ship, exit requires compulsion at cost $\zeta$, so the holder's exit value is $Q-\zeta\mathbf 1\{y+p_C+p_B<f^F\}$. Notes for the text: $f^F$ should be the credible penalty $\chi_f f$. $p_B$ applies only if the US measures are listed in the Blocking Statute annex. Compulsion is used only if $Q-\zeta>0$. $\zeta$ must exclude the firm's own net loss, which is already in $\omega$ and $c$ through $y$ and $d_f$. For a servicing ban in China, $p_C$ enters as $r_k$ in Proposition 2(e) only if Europe internalizes the firm's loss.

**Numerical check.** I enumerated 200,000 integer-valued draws, which include many ties. The firm's choice and the holder's exit value match the formulas in every draw.

---

## 5. Remark E (two-stage ACI; delegated act)

**Verdict: corrected (arithmetic added; one claim sharpened; one rule corrected).** Population shares are from Council Decision 2025/2427 as coded in `pop_check.py` (27 members; the shares sum to 100.00).

**Stage 1 (Council determination, QMV on a Commission proposal).** A QMV needs at least 15 of 27 members ($\lceil 0.55\cdot27\rceil$) and at least 65% of population. The non-yes set $N$ blocks iff $|N|\ge13$ or ($|N|\ge4$ and population above 35%). I checked this against the treaty rule, including the "deemed attained" clause, on 403,168 non-yes sets with zero mismatches. Implications:

- DE+FR+IT hold 46.84% but are only 3 members, so the measure passes against them.
- The smallest-population blocking coalition is the 13 smallest members, with 9.57%.
- The smallest 4-member population block is DE, FR, SK, LU, with 35.01%.
- Without DE, FR, IT and ES, a population block needs at least 12 members.

| Coalition | Members | Population % | Blocks stage 1 | Blocks a Council objection to a delegated act |
|---|---|---|---|---|
| Frontline core: PL, LT, LV, EE, FI, RO | 6 | 15.09 | no | no |
| Core + SE, DK | 8 | 18.75 | no | yes (8 members) |
| Bucharest Nine EU members + FI, SE, DK | 12 | 25.91 | no | yes |
| Core + SE, DK, CZ, SK, HU, BG, HR | 13 | 26.77 | **yes (count)** | yes |
| Same, with SI replacing HU | 13 | 25.13 | yes (count) | yes |
| Same, with SI and GR replacing HU and HR | 13 | 26.57 | yes (count) | yes |

The 13-member group is minimal: dropping any member ends the block. To block by population, the core needs two more members, which must include two of the big four or DE plus one of NL, BE, CZ, PT, SE, GR, HU, AT (14 pairs in all). Without DE, FR, IT and ES it needs 8 more, so the count route (7 more members) is the relevant one. I add SE, DK, CZ, SK, HU, BG and HR as the members most exposed to US posture cuts: Nordic-Baltic and Bucharest Nine members whose defence depends on US forward presence. HU is politically doubtful, but SI or GR can replace it and the group still has 13 members.

**Stage 2 (Commission implementing act, appeal committee).** Taking the memo's procedure as given, the Commission may adopt unless a QMV of 15 members and 65% votes against. The 13-member group cannot stop stage 2 alone. I did not verify from the regulation's text whether a "no opinion" bar applies; the EUR-Lex fetch returned nothing.

**Delegated act (removal of the US from EU001).** The Council does not act on a Commission proposal, so Art. 238(2) TFEU applies. This rule derogates from Art. 16(4) TEU and carries no four-member blocking clause: an objection needs at least 20 members ($\lceil0.72\cdot27\rceil$) and at least 65%. The act therefore stays in force if the non-objectors number at least 8 or hold more than 35%. I checked this on 241,708 sets with zero mismatches.

- The smallest coalition by count is any 8 members. The 8 smallest (MT, LU, CY, EE, LV, SI, LT, HR) hold 3.18%.
- By population, no pair suffices, but 20 three-member sets do. The smallest is DE+FR+BG (35.07%). Only FR+IT+PL (36.66%) and FR+IT+ES (39.23%) exclude DE.
- If a four-member clause were read in, the population route would need 4 members.
- For the 13-member frontline group to object, it needs 7 more members with at least 38.23 percentage points of population, e.g. DE, FR, BE, IE, SI, LU, MT.
- In the European Parliament, an objection needs a majority of component members (361 of 720).

**Groseclose-Snyder cost.**

```latex
\begin{remark}[Blocking minorities]
Let $\mathcal B$ be the family of stage-1 blocking coalitions: $|J|\ge13$, or $|J|\ge4$ with more than 35
percent of population. With enforceable vote-contingent payments and no rival bidder, the United States defeats
the determination at cost $\Phi(0)=\min_{J\in\mathcal B}\sum_{i\in J}\pos{q_i}$. Members with $q_i\le0$ join
any blocking coalition at zero cost, so $\Phi(0)$ is the cheapest completion of $F=\{i:q_i\le0\}$ into a
blocking coalition, and $\Phi(0)=0$ if and only if $F\in\mathcal B$. The six frontline states (15.09 percent)
do not block. Thirteen eastern and Nordic members (26.77 percent) do, by number. A defeat at stage~2 or by
Council objection to a delegated act needs a qualified majority against, which is itself in $\mathcal B$, so it
costs at least $\Phi(0)$.
\end{remark}
\begin{proof}
Member $i$ votes against if paid $\tau_i\ge q_i$. Payments are only needed inside the chosen blocking set,
and adding members with $q_i\le0$ costs nothing and preserves blocking, since $\mathcal B$ is upward closed. Any
coalition of 15 or more members (hence any QMV against, and any 20-member objection coalition) has at least 13
members and so lies in $\mathcal B$.
\end{proof}
```

**Numerical check.** The script computes $\Phi(0)$ exactly in two parts. The 13-member route takes the 13 cheapest members. The population route is a dynamic program over member count (capped at 4) and population in hundredths. The population route matches brute force on 30 random 14-member sub-councils (difference $2\times10^{-15}$). Illustrations:

| Profile | $\Phi(0)$ | Cheapest route |
|---|---|---|
| Uniform $q_i=1$ | 4 | three large states plus one |
| $q_i=-1$ for the core six, $+1$ otherwise | 2 | DE plus one partner |
| $q_i=-1$ for the 13-member group | 0 | free set blocks |
| $q_i$ = population share, negative for the core | 4.24 | count route (population route 19.92) |

The memo's phrase "members with $q_i<0$ block for free" should read "join a blocking coalition for free". Six frontline members are not enough to block. Thirteen are.
