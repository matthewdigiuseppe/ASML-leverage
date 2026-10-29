# Verification report m1: Lemma 1, Proposition 1, Corollary 1

Verifier tag: m1. Scripts: `code/checks/v2_m1_lemma1.py` (about 11 s) and `code/checks/v2_m1_prop1.py` (about 3 s). Both run with `python3 -I`.

## Summary of verdicts

| Result | Verdict | What changes |
|---|---|---|
| Lemma 1 (i) | confirmed | Needs the separability assumption stated below (stakes on promises and on threats are separate commitments, each capped at $\bar m_U$). |
| Lemma 1 (ii) | corrected (precision) | The alignment outcome holds in every subgame-perfect equilibrium (SPE) away from ties. The payment $\pos{Q}$ is pinned down only in weakly undominated strategies (loser bids up to its maximal credible bid). In SPE alone the price can be anything in $[0,\pos{Q}]$. Tie at $Q=\bar m_U<V$ needs the rule that an indifferent E aligns. Added: E's payoff is $\pos{\min\{Q,V,\bar m_U\}}$ in all cases. |
| Lemma 1 inefficient exit | confirmed (sharpened) | Every binding $\tau\in[Q,V)$ makes E and U strictly better off; this holds in every SPE, not only the selected one. |
| Proposition 1 | corrected (strengthened, one knife-edge) | Needs $r+\lambda>0$. For $\lambda>0$: the SPE is unique (not only among stationary profiles) and agreement is immediate. For $\lambda=0$: SPE payoffs are unique but there are stationary SPE with delay, so "unique stationary SPE with immediate agreement" fails at $\lambda=0$. Limit $P^*$ confirmed. |
| Corollary 1 (a) | confirmed | Holds in the limit only; for $\Delta>0$, $x^*(\Delta)$ can fall below $Q$ by $O(\Delta/(1-\beta))$. |
| Corollary 1 (b) | confirmed | At $\lambda=0$, immediate agreement requires a tie rule (see Prop. 1). |
| Corollary 1 (c) | confirmed | |
| Corollary 1 (d) | confirmed (precision) | It is the partial derivative holding $Q$ fixed. Added: the second term binds iff $Q<\lambda\beta V/(r+\lambda\beta)$. |
| Corollary 1 (e) | confirmed (precision) | The security channel runs through $\kappa$ (equal to $\bar\kappa$ only when U stakes its full capacity), and its sign is not determined without an assumption on the density of $\xi$. |
| Nesting claims | confirmed | Order of limits matters near $\beta=1$ when $Q>\omega_b V$ (see item iii). |
| (i) SPE payoff uniqueness | established | Shaked-Sutton sup/inf proof below. The paper can claim uniqueness of SPE payoffs for all $\lambda\ge 0$ and uniqueness of the SPE for $\lambda>0$. |
| (ii) Alternative timing | worked out | Stationary SPE unique with the same limit $P^*$. But when the outside option binds ($Q>\lambda\beta V/(r+\lambda\beta)$, $\beta>0$), nonstationary SPE give E up to $V$ in the limit. Footnote text below. |
| (iii) Rate near $\beta\to 1$ | worked out | Error $O(\Delta)$ where the second term binds, $O(\Delta/(1-\beta))$ where $Q$ binds; the limits $\Delta\to 0$ and $\beta\to 1$ do not commute when $Q>\omega_b V$. |
| (iv) Sign of $P^*$ | confirmed | $P^*\ge Q$ always; $P^*<0$ iff $\lambda>0$ and $Q+\beta(V-Q)<0$. Example: $Q=-1$, $V=1$, $\beta=1/4$, $\lambda=r$ gives $P^*=-1/4$. |

Notation: as instructed, the weight $w_b$ is written $\omega_b=\lambda/(\lambda+r)$ and its discrete counterpart $\omega_\Delta=\mu/(1-\delta(1-\mu))$. Flag for the editor: $\omega$ (no subscript) is also China's credible offer in the memo. The subscripts keep them apart, but the paper may prefer another letter.

## Assumptions fixed where the memo is ambiguous

1. (Lemma 1, C's bids.) C's cost of a winning promise $\tau_C$ is $\tau_C$; E values it at $\lambda_C\tau_C$ with $\lambda_C\in(0,1]$; C's value of E's exit is $W_C$ and losing gives C zero. This is the reading under which $\omega=\lambda_C\min\{W_C,\bar m_C\}$. If instead $\lambda_C$ were the probability that C honours a promise and C paid only when it honours, C would bid up to $\min\{W_C/\lambda_C,\bar m_C\}$ and the formula would become $\omega=\min\{W_C,\lambda_C\bar m_C\}$. The paper should say which reading it uses.
2. (Lemma 1, stakes.) Each announced conditional action carries its own stake of at most $\bar m_U$ (memo: "a stake $m\le\bar m_i$ to any announced conditional action"). If $\bar m_U$ were instead a total budget across the bid and the threats, the bid cap and the credible threat set would compete and Lemma 1 would change.
3. (Lemma 1, separability.) U's ex post instrument payoffs do not depend on whether it paid its promise. Payoffs are additive in transfers and instruments.
4. (Ties.) An indifferent E aligns. A power that is indifferent between paying a staked promise and forfeiting the stake pays (this is the memo's "credible iff $\tau\le\bar m_i$").
5. (Prop. 1, timing.) After a rejection without voluntary exit, breakdown is realized immediately with probability $\mu$ (exit flows start at once); otherwise the round's status-quo flows $(0,0)$ accrue and the next round starts after discounting by $\delta$. This is the timing that produces the memo's $x_A$ and $x_B$. Offers are real numbers (no sign restriction). We assume $Q<V$, $\beta\in[0,1)$, $r\ge 0$, $\lambda\ge 0$ and $r+\lambda>0$.

---

## Lemma 1 (bidding benchmark)

**Verdict: corrected (precision).**

### Final statement

```latex
\begin{lemma}[Bidding benchmark]\label{lem:bidding}
Suppose U and C bid for E's alignment in an ascending (clock) auction in which bids are staked promises, E values C's promise $\tau_C$ at $\lambda_C\tau_C$, E chooses its alignment after the auction, and instruments are then used. Let $\bar z_U=\min\{V,\bar m_U\}$ and $Q=\lambda_C\min\{W_C,\bar m_C\}-c$.
\begin{enumerate}[(i)]
\item After alignment $a$, U provides $x_j(a)$ for every instrument $j$, so exit lowers E's payoff, before transfers, by $c=\sum_j d_j+\eta$.
\item A promise of $\tau$ by power $i$ is honoured if and only if $\tau\le\bar m_i$. Bidding up to one's maximal credible bid (in units of E's payoff, $\bar z_U$ for U and $Q$ for C) is weakly dominant. In weakly undominated strategies, with an indifferent E aligning:
 \begin{enumerate}[(a)]
 \item if $Q<V$ and $Q\le\bar m_U$, E aligns and U pays $\pos{Q}$;
 \item if $Q>\min\{V,\bar m_U\}$, E exits, and C's promise gives E $\min\{V,\bar m_U\}$ net of $c$.
 \end{enumerate}
 In both cases E's payoff is $\pos{\min\{Q,V,\bar m_U\}}$.
\item If $\bar m_U<Q<V$, every binding transfer $\tau\in[Q,V)$ from U to E would make both E and U strictly better off than the equilibrium (inefficient exit from limited US commitment).
\end{enumerate}
\end{lemma}
```

Remark for the paper (robustness; can go in the appendix):

```latex
\begin{remark}
The alignment outcome in \cref{lem:bidding}(ii) does not depend on the selection. In the alternating-raise auction on a grid with mesh $\varepsilon$ (each bidder in turn may raise its standing bid or pass; two consecutive passes end the auction; bids above one's own valuation excluded), every subgame-perfect equilibrium has E aligned when $Q<\bar z_U-\varepsilon$ and exiting when $Q>\bar z_U+\lambda_C\varepsilon$. The price is not pinned down by subgame perfection alone: when $0<Q<\bar z_U$, any payment in $[0,Q]$ (up to the grid) is supported, because the losing bidder is indifferent between bidding and staying out. Weak dominance (or trembling-hand perfection) selects $\pos{Q}$. Part (iii) holds in every subgame-perfect equilibrium, since E's payoff after exit never exceeds $\bar z_U$ by more than one grid step.
\end{remark}
```

### Proof

```latex
\begin{proof}[Proof of \cref{lem:bidding}]
(i) Stakes on threats are attached before E moves and are separate from stakes on promises. After E's alignment $a$ is fixed, U chooses each instrument to maximize its ex post payoff given these stakes; by separability, its choice does not depend on whether it pays a promise. So U provides $x_j(a)$ and E's payoff before transfers is $\sum_j v_j(x_j(a))-\eta\mathbf 1\{a=X\}$. The difference between $a=A$ and $a=X$ is $\sum_j d_j+\eta=c$.

(ii) Credibility. At the payment stage, paying a promise of $\tau$ costs $\tau$ and has no ex post value, and not paying forfeits the stake $m\le\bar m_i$. The promiser pays iff $\tau\le m$, so the largest promise that is honoured is $\bar m_i$. E anticipates this and assigns zero value to larger promises.

Clock auction. Measure the clock $z$ in units of E's payoff relative to the aligned baseline. While U is active at $z$ it stands behind the promise $\tau_U=z$; while C is active at $z$ it stands behind $\tau_C=(z+c)/\lambda_C$. The clock starts at $z=0$, and a bidder that has dropped cannot re-enter. When one bidder drops at $z$ (or never enters, in which case $z=0$), the other wins at $z$; if both drop at the same level, E is indifferent and aligns. A strategy is a drop level.

U's maximal credible bid is $\bar z_U=\min\{V,\bar m_U\}$. Above $\bar m_U$ its promise is worthless; above $V$ winning is worse than losing. Fix any drop level $d_C$ of C. If $d_C\le\bar z_U$, the drop level $\bar z_U$ wins at price $\max\{d_C,0\}\le V$, which is the best U can obtain against $d_C$. If $d_C>\bar z_U$, the drop level $\bar z_U$ loses and yields $-V$; any credible drop level that wins pays at least $d_C$, and $d_C>V$ whenever $\bar m_U\ge d_C>\bar z_U$, so winning is worse. Hence dropping at $\bar z_U$ is weakly dominant.

C wins at level $z$ only if it stays strictly longer than U, and then earns $W_C-(z+c)/\lambda_C$, which is nonnegative iff $z\le\lambda_C W_C-c$. Its promise is credible iff $z\le\lambda_C\bar m_C-c$. So C's maximal credible bid is $\lambda_C\min\{W_C,\bar m_C\}-c=Q$. The same argument shows that dropping at $Q$ is weakly dominant (if $Q<0$, C cannot offer E even the baseline and stays out).

Outcome. With both bidders at their dominant drop levels, U wins iff $\bar z_U\ge Q$ (ties go to alignment) and pays the level at which C drops, $\max\{Q,0\}=\pos{Q}$. If $Q<V$ and $Q\le\bar m_U$, then $Q\le\bar z_U$, which gives (a). If $Q>\bar z_U$, C wins at the level at which U drops, $\bar z_U\ge 0$; E then receives $\lambda_C\tau_C-c=\bar z_U$, and C's payment $\tau_C=(\bar z_U+c)/\lambda_C$ is credible and profitable because $\bar z_U<Q$. This gives (b). In case (a) E's payoff is $\pos{Q}=\pos{\min\{Q,\bar z_U\}}$ and in case (b) it is $\bar z_U=\pos{\min\{Q,\bar z_U\}}$. The excluded case $Q=V\le\bar m_U$ leaves U indifferent between winning and losing, and both outcomes occur.

(iii) If $\bar m_U<Q<V$, then $\bar z_U=\bar m_U$ and by (ii)(b) E exits with payoff $\bar m_U$ while U receives $-V$. A binding transfer $\tau\in[Q,V)$ with alignment gives E $\tau\ge Q>\bar m_U$ and U $-\tau>-V$.
\end{proof}
```

Proof of the remark (alternating-raise game).

```latex
\begin{proof}[Proof of the remark]
Bids above one's valuation are excluded, so U's E-value never exceeds $\bar z_U$ and C's never exceeds $Q$. The game is finite. Suppose $Q<\bar z_U-\varepsilon$ and some equilibrium path ends with C leading. C's last raise was followed by a move of U. At that node U could raise to the smallest grid bid $b\ge Q$, which satisfies $b\le\bar z_U$ and $b<V$. No C bid can then beat $b$ (C's E-value is at most $Q\le b$ and ties go to alignment), so the raise guarantees U the payoff $-b>-V$, while passing gives $-V$. This contradicts optimality. Symmetrically, if $Q>\bar z_U+\lambda_C\varepsilon$, C can answer any U bid with a grid bid whose E-value lies in $(\bar z_U,Q)$; U cannot top it, and C's payoff is strictly positive, whereas losing gives zero. So C wins in every equilibrium. For the price, let C never bid and let U answer any C bid with the smallest grid bid $b\ge Q$. C is indifferent (it earns zero either way), U's responses are optimal by the argument above, and E receives zero. Variants in which C raises up to an intermediate level and then stops support intermediate prices (the numerical check finds every grid price in $[0,Q]$ in its example). After exit, C pays only enough to beat U's last bid, so E's payoff is at most $\bar z_U$ plus one grid step, which proves (iii) for every equilibrium.
\end{proof}
```

### Numerical check (`v2_m1_lemma1.py`)

The script computes equilibria in three ways, none of which uses the claimed formula, with exact rational arithmetic. (1) Clock auction: for 300 random draws on an integer lattice ($\lambda_C\in\{1,1/2,2/3,3/4,1/3,5/6\}$, caps binding or not, $Q$ negative, zero or positive), it enumerates all pairs of drop levels on a grid of mesh 1/12 (fine enough that $Q$ and $\bar z_U$ lie on it), verifies that dropping at one's maximal credible bid is weakly dominant for both bidders, and compares the dominant-strategy outcome with the statement: 0 failures, maximum error in E's payoff 0 (draws with $Q=V$ excluded). (2) Alternating-raise auction: for 400 small draws and both first movers (800 games), it computes the full set of pure SPE outcomes by set-valued backward induction with no tie-breaking. The winner matched the lemma in all 580 games with $Q<\bar z_U-\text{grid}$ and all 44 with $Q>\bar z_U+\text{grid}$; the largest E payoff across SPE equalled $\pos{\min\{Q,V,\bar m_U\}}$ within one grid step in all 800 games; and in 108 games the smallest E payoff across SPE was below the claimed price by more than a grid step (example: $Q=7/2$ with SPE payoffs $0,1,2,3,4$), which is the price indeterminacy reported above. A first run that allowed bids above one's own valuation produced winner failures at zero-profit ties, which is why the remark excludes such bids (they are weakly dominated). (3) Single-valued backward induction on larger grids (bids up to 22) under four tie-breaking rules (loser raises or passes when indifferent; E's ties to A or to X), 70 draws each: no winner failures; with the "loser raises" rule the maximal price error was 0.83 and 1.0 grid units. Edge cases checked: $Q<0$ (price 0 in every SPE), $Q=\bar m_U<V$ (A only under the alignment tie rule), $Q=V$ (both outcomes), $\bar m_U<Q<V$ (exit in every SPE; E receives $\bar m_U$ up to grid; every $\tau\in[Q,V)$ Pareto-improves E and U), $Q>V$, binding cap $\bar m_C<W_C$, $\lambda_C=1/2$, and $Q=0$.

---

## Proposition 1 (master bargaining game)

**Verdict: corrected (strengthened, plus one knife-edge).** The closed forms $x_A$, $x_B$, $x^*=\max\{x_A,x_B\}$ and the limit $P^*$ are correct. Two precisions: $r+\lambda>0$ is needed (otherwise there is no contraction and $\omega_b$ is undefined), and at $\lambda=0$ the stationary SPE is not unique and need not have immediate agreement (payoffs are still unique). On the positive side, uniqueness holds for all SPE, not only stationary ones.

### Final statement

```latex
Let $\mu=1-e^{-\lambda\Delta}$, $\delta=e^{-r\Delta}$, $k=\delta(1-\mu)=e^{-(r+\lambda)\Delta}$, $\omega_\Delta=\mu/(1-k)$ and
\[
x_A=\omega_\Delta\big(Q+\beta(V-Q)\big),\qquad
x_B=\frac{(1-\beta)Q+\beta\mu V}{1-\beta k},\qquad
x^*=\max\{x_A,x_B\}.
\]
\begin{proposition}[Master bargaining game]\label{prop:master}
Let $Q<V$, $\beta\in[0,1)$, $r,\lambda\ge 0$ and $r+\lambda>0$.
\begin{enumerate}[(i)]
\item For every $\Delta>0$, every subgame-perfect equilibrium gives E the payoff $x^*(\Delta)$ and U the payoff $-x^*(\Delta)$. There is a stationary equilibrium in which U offers $P_U=\max\{Q,\mu Q+kx^*\}$, E demands $P_E=\mu V+kx^*$, each offer is accepted at once, and E would exit after rejecting a US offer iff $Q>\delta x^*$.
\item If $\lambda>0$, this equilibrium is the unique subgame-perfect equilibrium (up to E's exit choice when $Q=\delta x^*$, which does not affect payoffs), and agreement is immediate. If $\lambda=0$, there are also stationary equilibria with delay, with the same payoffs.
\item As $\Delta\to 0$, $x^*(\Delta)$, $P_U(\Delta)$ and $P_E(\Delta)$ converge to
\[
P^*=\max\big\{Q,\ \omega_b\big(Q+\beta(V-Q)\big)\big\},\qquad \omega_b=\frac{\lambda}{\lambda+r}\in[0,1].
\]
If $r>0$, the second term is the larger one iff $Q<\hat Q\equiv \lambda\beta V/(r+\lambda\beta)$.
\end{enumerate}
\end{proposition}
```

### Proof

```latex
\begin{proof}[Proof of \cref{prop:master}]
Normalize payoffs per unit of flow. Agreement on $P$ gives $(P,-P)$, exit gives $(Q,-V)$, and the status quo gives $(0,0)$ per period.

\emph{Step 1 (feasible payoffs).} Every outcome gives a total payoff of $0$ (agreement or perpetual status quo) or $Q-V<0$ (exit), so in every subgame the two players' payoffs sum to at most zero. Payoffs are bounded: U can reject every demand and so never pays more than $V$, and E can reject every offer without exiting and so never gets less than $\min\{Q,0\}$. Because $k<1$, payoffs are continuous at infinity and the one-shot deviation principle applies.

\emph{Step 2 (the map $T$).} Define $g(v)=\max\{Q,\mu Q+kv\}$ and $T(v)=\beta(\mu V+kv)+(1-\beta)g(v)$. $T$ is nondecreasing with Lipschitz constant $k<1$, so $T(v)-v$ is strictly decreasing and $T$ has a unique fixed point. Write $T=\max\{T_A,T_B\}$ with $T_A(v)=\mu(Q+\beta(V-Q))+kv$ and $T_B(v)=\beta\mu V+(1-\beta)Q+\beta kv$, whose fixed points are $x_A$ and $x_B$. If $x_A\ge x_B$, then $T_B(x_A)-x_A\le T_B(x_B)-x_B=0$ because $T_B(v)-v$ is strictly decreasing, so $T(x_A)=x_A$. The case $x_B\ge x_A$ is symmetric. Hence the fixed point is $x^*=\max\{x_A,x_B\}$. Moreover $g(x^*)=Q$ iff $Q\ge\mu Q+kx^*$ iff $Q\ge\delta x^*$.

\emph{Step 3 (a stationary equilibrium).} Consider the profile in (i): E accepts a US offer $P$ iff $P\ge g(x^*)$ and, after rejecting, exits iff $Q>\mu Q+kx^*$; U accepts a demand $P$ iff $P\le P_E=\mu V+kx^*$. Under this profile E's value is $\beta P_E+(1-\beta)P_U=T(x^*)=x^*$ and U's is $-x^*$. A responding E gets $P$ by accepting and $g(x^*)$ by rejecting; a responding U gets $-P$ by accepting and $-\mu V-kx^*=-P_E$ by rejecting. So the acceptance rules are optimal. A proposing U gets $-g(x^*)$ from $P_U$; any rejected offer gives it $-V<-Q$ if E exits and $-\mu V-kx^*\le-\mu Q-kx^*$ if E does not, both at most $-g(x^*)$. A proposing E gets $P_E$, while a rejected demand gives it $\mu Q+kx^*\le P_E$. Both comparisons are strict when $\mu>0$. By the one-shot deviation principle the profile is a subgame-perfect equilibrium.

\emph{Step 4 (all equilibria have the same payoffs).} Every round-start subgame is a copy of the game. Let $M$ and $m$ be the supremum and infimum of E's equilibrium payoffs and $\bar U$, $\underline U$ those of U; they are finite by Step 1.
(a) By Step 1, $\bar U\le -m$.
(b) When E proposes, any demand $P<\mu V-k\bar U$ is accepted in every equilibrium, because rejection gives U at most $-\mu V+k\bar U<-P$. So E's payoff at such a node is at least $\mu V-k\bar U\ge\mu V+km$.
(c) When U proposes, E can reject and obtain at least $g(m)$.
Hence $m\ge \beta(\mu V+km)+(1-\beta)g(m)=T(m)$, and since $T(v)-v$ is strictly decreasing with root $x^*$, $m\ge x^*$.
(d) When U proposes, any offer $P>g(M)$ is accepted in every equilibrium, because rejection gives E at most $g(M)$. So U's payoff at such a node is at least $-g(M)$. When E proposes, U can reject and obtain at least $-\mu V+k\underline U$. Hence $\underline U\ge\beta(-\mu V+k\underline U)-(1-\beta)g(M)$, that is, $-\underline U\le[\beta\mu V+(1-\beta)g(M)]/(1-\beta k)$.
(e) At every node E's payoff is at most minus U's payoff (Step 1). So E gets at most $\mu V-k\underline U$ when it proposes and at most $g(M)$ when U proposes. Using (d),
\[
M\le\beta\mu V+(1-\beta)g(M)+\beta k\,\frac{\beta\mu V+(1-\beta)g(M)}{1-\beta k}=\frac{\beta\mu V+(1-\beta)g(M)}{1-\beta k}\equiv S(M).
\]
$S$ has Lipschitz constant $(1-\beta)k/(1-\beta k)<1$, and $S(v)=v$ iff $T(v)=v$. So $S(v)-v$ is strictly decreasing with root $x^*$, and $M\le x^*$.
Therefore $m=M=x^*$. Then $\bar U\le-x^*$ by (a) and $\underline U\ge-S(x^*)=-x^*$ by (d), so U's payoff is $-x^*$ in every equilibrium. This proves the payoff part of (i).

\emph{Step 5 (uniqueness and immediate agreement for $\lambda>0$).} Payoffs sum to zero in every equilibrium. If a first-round proposal were rejected with positive probability, the total payoff after the rejection would be $Q-V<0$ (exit) or $\mu(Q-V)+k s$ with $s\le 0$ (no exit), which is negative when $\mu>0$. So agreement is immediate. Since continuation payoffs from every round start are $(x^*,-x^*)$, E accepts every offer above $g(x^*)$ and rejects every offer below it, and U accepts every demand below $P_E$ and rejects every demand above it. U must offer exactly $g(x^*)$ and E must accept it: if E rejected $g(x^*)$, U would have no best offer, and any lower offer is rejected and gives U strictly less (Step 3). The same argument pins down E's demand $P_E$ and U's acceptance of it. E's exit choice after rejecting an offer is determined unless $Q=\delta x^*$. If $\lambda=0$ and $Q>0$, the stationary profile in which E always makes a demand U rejects, while U offers $P_U=Q$, gives E $\beta\delta x+(1-\beta)Q=x$, so $x=x_B=x^*$; E is indifferent between this and the demand $\delta x^*$, so the profile is an equilibrium with delay. If $\lambda=0$ and $Q\le 0$, perpetual disagreement is an equilibrium with payoffs $(0,0)=(x^*,-x^*)$.

\emph{Step 6 (the limit).} As $\Delta\to0$, $\mu=\lambda\Delta+O(\Delta^2)$ and $1-k=(r+\lambda)\Delta+O(\Delta^2)$, so $\omega_\Delta\to\omega_b$ and $x_A\to\omega_b(Q+\beta(V-Q))$. In $x_B$ the numerator tends to $(1-\beta)Q$ and the denominator to $1-\beta>0$, so $x_B\to Q$. The maximum is continuous, so $x^*\to P^*$. Finally $P_U=g(x^*)\to\max\{Q,P^*\}=P^*$ and $P_E=\mu V+kx^*\to P^*$. For the threshold, with $r>0$: $\omega_b(Q+\beta(V-Q))>Q$ iff $Q(r+\lambda\beta)<\lambda\beta V$.
\end{proof}
```

### Numerical check (`v2_m1_prop1.py`, sections A, B, D, E)

The script never uses the closed forms to compute equilibria. It runs finite-horizon backward induction in which each proposer compares every offer on a 601-point grid, together with the responder's indifference point, with the payoff of making an unacceptable offer, E compares exit with continuation, and U's continuation value is tracked separately (it is not set to $-v$). (A) 500 runs (250 random draws, two random terminal values each; $\beta=0$ and $\lambda=0$ included; $\Delta\in\{1,0.5,0.2,0.1\}$): maximum $|v-x^*(\Delta)|=1.7\times10^{-11}$ and maximum $|u+v|=2.9\times10^{-11}$; with $\lambda>0$ no proposer ever weakly preferred delay. (B) Frequent-offer limit: backward induction at $\Delta=0.004,0.002,0.001$ with second-order Richardson extrapolation on 120 draws ($\beta\le0.9$): maximum $|P_{\text{num}}-P^*|=7.5\times10^{-6}$. (D) SPE uniqueness: limits of backward induction from six terminal conditions per draw, including infeasible ones such as $(3V,3V)$, differ by at most $4.5\times10^{-12}$ over 60 draws; iterating the four sup/inf maps of Step 4 from the box $[-10V,10V]^2$ converges to $(x^*,x^*,-x^*,-x^*)$ within $4.4\times10^{-12}$ on 300 draws. (E) At $\lambda=0$, the stationary profiles with delay ($Q=0.6$ and $Q=-0.5$) pass the one-shot deviation check with the same values as $x^*$, confirming the knife-edge.

---

## Corollary 1

**Verdict: confirmed, with the precisions noted in (a), (d), (e).**

### Final statement

```latex
\begin{corollary}\label{cor:master}
Under the conditions of \cref{prop:master}:
\begin{enumerate}[(a)]
\item $P^*\ge Q$: Europe never concedes more than its slack, $-P^*\le\Lambda=\pos{-Q}$. (For $\Delta>0$ the value $x^*(\Delta)$ can be below $Q$, by at most $\beta(1-k)\pos{Q-\omega_\Delta V}/(1-\beta k)$.)
\item If $\lambda=0$, $P^*=\pos{Q}$; if $\beta=0$, $P^*=\max\{Q,\omega_b Q\}$. In either case $Q\le 0$ implies $P^*\le 0$.
\item $P^*>0$ iff $Q>0$, or $\lambda>0$ and $Q+\beta(V-Q)>0$.
\item Holding $Q$ fixed, $\partial P^*/\partial V=\beta\omega_b$ where the second term binds ($Q<\hat Q$) and $0$ where $Q>\hat Q$. If $Q$ itself depends on $V$, then $dP^*/dV=\omega_b[\beta+(1-\beta)\,dQ/dV]$ in the first case and $dQ/dV$ in the second.
\item $V$ enters $P^*$ directly only through the term $\beta\omega_b V$, and indirectly only through $Q$: through $W_C$ when $W_C<\bar m_C$ ($\partial\omega/\partial V=\lambda_C\rho$), through $\chi_f=\mathbf 1\{\varphi V\le\gamma+\bar m_U\}$ (a rise in $V$ past $(\gamma+\bar m_U)/\varphi$ raises $Q$ by $f$), and through $\kappa=G(s_X+s_L)-G(s_X-m_S)$ via $s_X=s_0+s_B(V)$ (which equals $\bar\kappa$ when $m_S=\bar m_U$).
\end{enumerate}
Nesting: $\lambda=0$ gives $\pos{Q}$ (the outside-option principle); $r\to 0$ with $\lambda>0$ gives $Q+\beta(V-Q)$; $\beta=0$ gives $\max\{Q,\omega_b Q\}$ (US proposes); $\beta\to1$ and $\lambda\to\infty$ give $V$.
\end{corollary}
```

### Proof

```latex
\begin{proof}[Proof of \cref{cor:master}]
(a) $P^*$ is a maximum one of whose terms is $Q$. If $Q\ge0$ then $P^*\ge0$, and if $Q<0$ then $-P^*\le-Q$; in both cases $-P^*\le\pos{-Q}$. For $\Delta>0$, $x^*\ge x_B$ and $x_B-Q=\beta(1-k)(\omega_\Delta V-Q)/(1-\beta k)$, which gives the bound.
(b) $\lambda=0$ gives $\omega_b=0$ and $P^*=\max\{Q,0\}$. $\beta=0$ gives $P^*=\max\{Q,\omega_b Q\}$. If $Q\le0$, both terms are nonpositive.
(c) $P^*>0$ iff $Q>0$ or $\omega_b(Q+\beta(V-Q))>0$, and $\omega_b>0$ iff $\lambda>0$.
(d) Where $\omega_b(Q+\beta(V-Q))>Q$, $P^*=\omega_b(1-\beta)Q+\omega_b\beta V$; differentiate. Where $Q$ is the larger term, $P^*=Q$. The regime condition is the threshold in \cref{prop:master}(iii).
(e) In the formula for $P^*$, $V$ appears only in $\beta\omega_b V$; $\beta$, $\lambda$ and $r$ do not depend on $V$. The remaining dependence runs through $Q=\omega-c$ with $\omega=\lambda_C\min\{W_C,\bar m_C\}$, $W_C=(1-\theta)W+\rho V$, and $c=\sum_j d_j+\eta$, whose components depending on $V$ are $d_f=\chi_f f$ and $d_{\text{core}}=\kappa S_k$.
Nesting: the first three follow by substitution ($\omega_b\to1$ as $r\to0$, and $Q+\beta(V-Q)\ge Q$). For the last, $P^*$ is continuous in $(\beta,\omega_b)\in[0,1]^2$ and equals $\max\{Q,V\}=V$ at $(1,1)$.
\end{proof}
```

Precision on (e): $\partial\kappa/\partial s_X=g(s_X+s_L)-g(s_X-m_S)$, where $g$ is the density of $\xi$. Its sign depends on the shape of $g$ between the two points, so the silicon-shield channel can raise or lower $Q$ unless the paper assumes, for example, that $g$ is nonincreasing on $[s_X-\bar m_U,s_A]$. **Flag for the Prop 3 verifier:** memo Prop 3(d) ("$\bar\kappa$ is nonincreasing in $s_X$") is false without such an assumption. Counterexample: $\xi\sim N(0,1)$, $s_X-\bar m_U=-2$, $s_A=0$; then $\partial\bar\kappa/\partial s_X=\phi(0)-\phi(-2)>0$.

### Numerical check (`v2_m1_prop1.py`, section C)

All corollary checks use the numerical limits from section B, not the formula. (a) $P_{\text{num}}\ge Q$: 0 violations in 120 draws. (b) $\lambda=0$: $P_{\text{num}}=\pos{Q}$ in all 43 draws; $\beta=0$: $P_{\text{num}}=\max\{Q,\omega_bQ\}$ in all 59 draws, and never $P^*>0$ with $Q\le0$. (c) Sign: 0 violations. (d) Central finite differences in $V$ at fixed $Q$ in the second-term regime (25 draws): maximum error against $\beta\omega_b$ of $6.6\times10^{-10}$. The regime threshold $\hat Q$ classified every draw correctly. Nesting: $r=0.05,0.02,0.01$ move $P_{\text{num}}$ toward $Q+\beta(V-Q)$, as $\omega_b\to1$ predicts; $(\beta,\lambda)=(0.9,20),(0.99,200),(0.999,2000)$ give $1.795,1.979,1.998$ against $V=2$; $\lambda=0$ gives $\pos{Q}$ exactly.

---

## Additional items

### (i) Uniqueness of SPE payoffs

Established for the base timing. Step 4 above is a Shaked-Sutton sup/inf argument adapted to the random proposer, breakdown and the outside option. It needs only $Q<V$ (so total payoffs are at most zero) and $k<1$. It also holds at $\beta=1$. The paper can state: "every subgame-perfect equilibrium gives Europe $x^*(\Delta)$; if $\lambda>0$ the equilibrium is unique and agreement is immediate." It need not restrict to stationary equilibria.

### (ii) Alternative timing (E may also exit right after U rejects E's demand)

Result:

```latex
Suppose E may also exit right after U rejects E's demand, and let $x_B'=\beta V+(1-\beta)Q$.
(1) For each $\Delta>0$ the stationary equilibrium value is unique and equals $x'=x_A$ if $\delta x_A\ge Q$ and $x'=\min\{x_B',Q/\delta\}$ otherwise. In the last case with $Q/\delta<x_B'$, E randomizes over exit after U rejects its demand. As $\Delta\to0$, $x'\to P^*$.
(2) If $\delta x^*>Q$ (for small $\Delta$, this is $Q<\hat Q$), exit is never credible and the equilibrium set and payoffs coincide with those of the base game.
(3) If $\beta>0$ and $\delta x_A\le Q$ (for small $\Delta$, $Q>\hat Q$, which requires $Q>0$), there are nonstationary equilibria in which E's payoff is
\[ v_H=\max\Big\{x_B',\ \frac{\beta V+(1-\beta)\mu Q}{1-(1-\beta)k}\Big\}, \]
the largest equilibrium payoff for E, and $v_H\to V$ as $\Delta\to0$.
```

Proof.

```latex
\begin{proof}
(1) In a stationary equilibrium with values $(v,-v)$, E's continuation after any rejection without exit is $\mu Q+kv$, so E exits after a rejection iff $Q>\delta v$. U offers $\max\{Q,\mu Q+kv\}$. U's rejection of E's demand gives U $-V$ if E then exits and $-\mu V-kv$ otherwise, so E demands $V$ if $Q>\delta v$, $\mu V+kv$ if $Q<\delta v$, and $pV+(1-p)(\mu V+kv)$ if $Q=\delta v$ and E exits with probability $p$. If $v>Q/\delta$, then $v=T_A(v)$ and $v=x_A$. If $v<Q/\delta$, then $v=x_B'$. If $v=Q/\delta$, the value equation requires $T_A(Q/\delta)\le Q/\delta\le x_B'$, that is, $x_A\le Q/\delta\le x_B'$. The first two cases cannot both hold: $x_A>Q/\delta>x_B'$ would require $x_B'<x_A=\omega_\Delta x_B'$, so $x_B'<0$ and $Q<0$, but then $Q/\delta<Q\le x_B'$. Hence exactly one value exists. If $\delta x_A<Q$ then $Q>0$, since otherwise $x_A\ge\min\{Q,0\}\ge Q/\delta$. As $\Delta\to0$: if $Q<\hat Q$ then $\delta x_A>Q$ eventually and $x'=x_A\to P^*$; if $Q>\hat Q$ then $x'=\min\{x_B',Q/\delta\}\to\min\{Q+\beta(V-Q),Q\}=Q=P^*$; if $Q=\hat Q$ both expressions tend to $Q=P^*$.
(2) Steps 4(a) to 4(c) of the proof of \cref{prop:master} remain valid, because U's rejection of a demand gives U at most $\max\{-V,-\mu V+k\bar U\}=-\mu V+k\bar U$. So every equilibrium continuation value of E is at least $x^*$. If $\delta x^*>Q$, then $\mu Q+kv'>Q$ for every continuation value $v'$, exit after a rejection is never optimal, and the game is strategically the base game.
(3) Let L be the stationary equilibrium of (1), with value $v_L=\min\{x_B',Q/\delta\}\le Q/\delta$. In state H, E demands $V$ and U accepts any demand up to $V$; after U rejects a demand, E exits and play would otherwise continue in L; U offers $g_H=\max\{Q,\mu Q+kv_H\}$; after E rejects an offer without exiting, play continues in H. Then $v_H=\beta V+(1-\beta)g_H$, whose solution is the stated maximum (Step 2 of the proof of \cref{prop:master}). One-shot deviations: E's exit after U's rejection is optimal because $\mu Q+kv_L\le Q$. U is indifferent between accepting $V$ and rejecting it (exit gives $-V$). A demand above $V$ is rejected and gives E at most $\max\{Q,\mu Q+kv_L\}=Q<V$. A US offer below $g_H$ is rejected and gives U $-V$ or $-\mu V-kv_H$, both below $-g_H$. E's acceptance rule in H is optimal by construction. Every equilibrium gives E at most $V$ when it proposes (U can always secure $-V$) and at most $g(M')$ when U proposes, so $M'\le\beta V+(1-\beta)g(M')$. The right side minus $M'$ is strictly decreasing and vanishes at $v_H$, so $M'\le v_H$. As $\Delta\to 0$, $(\beta V+(1-\beta)\mu Q)/(1-(1-\beta)k)\to\beta V/\beta=V$.
\end{proof}
```

Suggested footnote:

```latex
If Europe could also exit right after the United States rejects Europe's own demand, the stationary equilibrium would have the same frequent-offer limit $P^*$. But when the outside option binds ($Q>\lambda\beta V/(r+\lambda\beta)$), there would also be nonstationary equilibria in which Europe obtains up to $V$: a US rejection can be followed by a continuation that holds Europe to its outside option, which makes exit after the rejection credible, so the United States accepts any demand up to $V$. Allowing exit only after Europe rejects a US offer is what pins down the outside-option principle.
```

Numerical check (`v2_m1_prop1.py`, section F): the stationary value of the alternative-timing game was computed on 300 draws by bisection on the sign of the correspondence $T'(v)-v$ built from node-by-node optimization. It matched the piecewise formula within $1.6\times10^{-14}$ and found 42 mixing equilibria (a downward jump through zero). The two-state "high" profile was built in 67 draws where $v_L\le Q/\delta$ and $Q>0$, and passed the one-shot deviation check (offers on a 1201-point grid) in all 67. Examples at $\Delta=0.01$: $Q=0.608$, $V=1.629$ gives a stationary value of 0.609 and a high-SPE value of 1.626. At $\Delta=10^{-5}$ the stationary value differs from $P^*$ by at most $5\times10^{-5}$ over 200 draws.

### (iii) Rate of convergence near $\beta\to1$

Using $|\max\{a,b\}-\max\{c,d\}|\le\max\{|a-c|,|b-d|\}$:

```latex
\[
|x^*(\Delta)-P^*|\le\max\Big\{|\omega_\Delta-\omega_b|\,\big|Q+\beta(V-Q)\big|,\ \frac{\beta(1-k)}{1-\beta k}\,|\omega_\Delta V-Q|\Big\},
\]
with $\omega_\Delta=\omega_b\big(1+\tfrac{r\Delta}{2}\big)+O(\Delta^2)$, $1-k=(r+\lambda)\Delta+O(\Delta^2)$, and $\frac{\beta(1-k)}{1-\beta k}\le\frac{\beta(r+\lambda)\Delta}{1-\beta}$.
```

Where the second term binds, the error is $O(\Delta)$ uniformly in $\beta$. Where $Q$ binds, $P^*-x^*(\Delta)\approx(Q-\omega_bV)\,\beta(r+\lambda)\Delta/[(1-\beta)+\beta(r+\lambda)\Delta]$, which is $O(\Delta/(1-\beta))$ and not uniform in $\beta$. For fixed $\Delta$, $\lim_{\beta\to1}x^*(\Delta)=\omega_\Delta V\to\omega_bV$, while $\lim_{\beta\to1}P^*=\max\{Q,\omega_bV\}$. So the limits $\Delta\to0$ and $\beta\to1$ do not commute when $Q>\omega_bV$, and at $\beta=1$ exactly the formula would be $\omega_bV$ (E can never use its outside option). Reading: the formula is accurate when US proposals arrive much faster than breakdown and discounting, $(1-\beta)/\Delta\gg r+\lambda$. This is a reason to keep $\beta<1$ in the statement. Section G of the script (with $Q=1.5$, $V=2$, $\lambda=r=1$, so $\omega_bV=1<Q$) gives, for $\beta=0.9,0.99,0.999$ and $\Delta=10^{-2},10^{-3},10^{-4}$, gaps $P^*-x^*$ of $(0.075,0.009,0.001)$, $(0.328,0.083,0.010)$ and $(0.471,0.333,0.083)$, matching the approximation to three decimals for $\Delta\le10^{-3}$. In the alternative timing of (ii), the stationary value is continuous at $\beta=1$ (it tends to $\max\{\omega_\Delta V,Q/\delta\}$).

### (iv) Sign of $P^*$

$P^*\ge Q$ always (Corollary 1(a)); the minimum of $P^*-Q$ over 200,000 random closed-form draws is exactly 0. $P^*<0$ iff both terms are negative, that is, iff $\lambda>0$ and $Q+\beta(V-Q)<0$, which is $Q<-\beta V/(1-\beta)$ (with $\lambda=0$, $P^*=\pos{Q}\ge 0$). Then Europe pays a flow to the United States: when $Q<0$, breakdown hurts Europe, and the United States can extract part of the value of avoiding the breakdown risk. Example (section H): $Q=-1$, $V=1$, $\beta=1/4$, $\lambda=r=1$ gives $P^*=-1/4$ by backward induction and by the formula; the concession $1/4$ is below the slack $\Lambda=1$. With $\lambda=0$, $P^*=\pos{Q}\ge0$, so concessions require breakdown risk.

## Other remarks for the paper

- In Prop. 1 the disagreement point is the aligned status quo with zero transfer, so $P^*$ is the whole transfer, not a supplement to the $\pos{Q}$ of Lemma 1. When the two are combined, say that the bargaining game replaces the bidding stage's payment and takes $\omega$ (hence $Q$) as given.
- For $\Delta>0$, E's equilibrium value can be below its exit payoff $Q$ (E can exit only after rejecting a US offer). This disappears in the limit and should not be stated as a property of the discrete game.
