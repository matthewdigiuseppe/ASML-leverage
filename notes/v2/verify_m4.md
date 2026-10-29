# Verification report m4: Proposition 4 and corollaries, multi-period cuts, windows, self-binding, Proposition 5

Verifier tag: m4. Scripts (all run with `python3 -I`, total under one minute):

| Script | Result | Run time |
|---|---|---|
| `code/checks/v2_m4_prop4.py` | Proposition 4, corollaries (i) to (iv), credibility and $\Delta_c$, investment tie rule | about 5 s |
| `code/checks/v2_m4_prop4_china.py` | Corollary (v), China chooses $r^c$ before U | about 2 s |
| `code/checks/v2_m4_cuts_windows.py` | Lemma on multi-period cuts (part A), windows corollary (part B) | about 21 s |
| `code/checks/v2_m4_selfbind.py` | Remark on self-binding and dual key | about 1 s |
| `code/checks/v2_m4_prop5.py` | Proposition 5 for six distributions, comparative statics | about 26 s |

The two scripts for corollary (v) and the remark import the brute-force solver from `v2_m4_prop4.py` (located through the script's own directory).

## Summary of verdicts

| Result | Verdict | What changes |
|---|---|---|
| Proposition 4 | confirmed | Holds under the timing and tie rules listed below. The period-1 rent after a transfer is $\pos{Q_1-\Delta_c}$ because the ultimatum precedes the period-1 contest. The credibility condition does not involve $\Delta_c$. Added: E's payoff, and that issued ultimatums are never refused. |
| Corollary (i) | confirmed (sharpened) | Exact condition: $\Delta R_U>k-v_c$ and $B_1+(\Delta R_U-\Delta R_H)>\sigma+r^c+k-v_c$. "Positive premium at some date" means $Q_1>0$ or the post-investment premium $Q_2+\bar I\,I(Q_2)>0$. |
| Corollary (ii) | confirmed (sharpened) | $\Gamma$ with the investment option is weakly above $\Gamma$ without it. New implication: with investment, U can buy control with zero bite (the transfer saves $K_I$). |
| Corollary (iii) | confirmed | $\Gamma$ and $T^*$ nondecreasing in $\Delta_c$, holding $\sigma,r^c,v_c,k$ fixed. |
| Corollary (iv) | confirmed | General form without $Q_1<0$: $\Gamma=\min\{\pos{Q_1}+\delta\pos{Q_2},\,B_1-\sigma-r^c\}$. |
| Corollary (v) | corrected | The condition is that executing the punishment has negative ex post value for China; the parenthetical "($\rho=0$)" is not that condition. Holds in every SPE. With $H_C>0$ (China strictly prefers E to keep control) the outcome is unique: transfer iff $\Gamma(r_{\max})>0$; with $H_C=0$ both outcomes can occur. On path the payment carries $r^c=0$. Fails if punishing is self-rewarding. |
| Lemma (multi-period cuts) | confirmed (scope stated) | Needs $Q_s+d_s<V_s$ and $Q_s+d_s\le\bar m_U$ at cut dates and no response of other dates' premia (no investment response). U's cost is $\delta^{s-1}(g_s+d_s)$. Outside the scope the formula is wrong in both directions (examples). |
| Windows corollary | corrected | The later rent date must be $t'\ge t$, not $t'>t$: with an unconditional part $u_t>0$ the bite can exceed $\sigma+r^c$ at a date with $Q_t>0$, and the transfer then removes the current rent. Identical to the memo when all $u_t=0$. |
| Remark (self-binding vs dual key) | corrected | Pre-emption condition confirmed. E's preference condition is correct only when U would issue the ultimatum absent binding and binding pre-empts it; general version given. New: partial binding ($\Delta_b<\infty$) can invite an ultimatum, because it raises slack and hence the bite. |
| Proposition 5 | corrected | Correct for threat-backed ultimatums and whenever $v_c\le r^c$ (so for $v_c=0$). With $v_c>r^c$, U may prefer an unthreatened purchase offer (stake zero); the issuance condition becomes $\max\{\Pi_B,\Pi_0\}>k$ and the comparative statics split between refusal and breakdown probabilities. The comparative static in $v_c$ holds for threat-backed ultimatums; with the purchase option the refusal probability falls in $v_c$ but the breakdown probability can rise. The comparative statics for threat-backed ultimatums hold for every continuous $F$ (Topkis); log-concavity is needed only for the first-order characterization. |

## Assumptions fixed where the memo is ambiguous

(P1) *Timing in period 1.* The ultimatum is issued at the start of period 1, before the period-1 bidding contest (as in the protocol of Proposition 2, where the contest is replayed at the end of the period). So after a transfer E's period-1 premium is $Q_1-\Delta_c$ and its period-1 rent is $\pos{Q_1-\Delta_c}$; after a refusal the contest is played after the threat is executed. If instead the period-1 rent were settled before the ultimatum (and a transfer could not undo it), the terms $\pos{Q_1}-\pos{Q_1-\Delta_c}$ would drop out of both $\Delta R_U$ and $\Delta R_H$; the rest of the formula is unchanged provided the threat's bite is still $B_1$. The two timings differ only when $Q_1>0$.

(P2) *Contests.* At every contest U retains E (Lemma 1 conditions): $Q_1+d_1<V$, $Q_1+d_1\le\bar m_U$, $Q_2+\bar I<V$, $Q_2+\bar I\le\bar m_U$. The payment $T$ is a spot payment at signing.

(P3) *Threat.* The ultimatum's threat withdraws in period 1 a bundle $J$ with unconditional part $u_1=\Delta^X(J)$, conditional part $d_1=\Delta^A(J)-\Delta^X(J)$ and direct ex post cost $g_1\ge 0$ to U ($g_1\ge 0$ because the baseline is U's ex post optimal provision to a loyal holder). Its execution cost is $e=g_1+\pos{Q_1+d_1}-\pos{Q_1}$ and it is credible iff $e\le\bar m_U$. $B_1=u_1+\min\{d_1,\Lambda_1\}$ if credible and $B_1=0$ otherwise, $\Lambda_1=\pos{-Q_1}$. U has no other period-1 demands competing for the same bite (Proposition 2(c)).

(P4) *Ties.* An indifferent E accepts. U issues only if it strictly gains (the $k\to 0^+$ convention when $k=0$). E invests only if strictly profitable (memo's rule; with the opposite rule every statement holds with $I$ defined by a weak inequality, checked numerically). After a transfer U keeps baseline provision unless withdrawal is strictly profitable, which it never is.

(P5) $\sigma$, $r^c$, $v_c$, $k$ do not depend on $\Delta_c$; $r^c$ is credible and executed after any transfer (endogenized in (v)); $\delta\in(0,1]$; $I(-\infty)=0$ and $\pos{-\infty}=0$ for $\Delta_c=\infty$.


## 1. Proposition 4 (preventive control)

**Verdict: confirmed** (under P1 to P5).

### Final statement

```latex
\begin{proposition}[Preventive control]\label{prop:control}
Let $I(q)=\mathbf 1\{\delta(\pos{q+\bar I}-\pos{q})>K_I\}$, $\mathrm{Rent}_U(q)=\delta\pos{q+\bar I\,I(q)}$ and $\mathrm{Val}_H(q)=\mathrm{Rent}_U(q)-K_I I(q)$, and let
\begin{align*}
\Delta R_U&=\pos{Q_1}-\pos{Q_1-\Delta_c}+\mathrm{Rent}_U(Q_2)-\mathrm{Rent}_U(Q_2-\Delta_c),\\
\Delta R_H&=\pos{Q_1}-\pos{Q_1-\Delta_c}+\mathrm{Val}_H(Q_2)-\mathrm{Val}_H(Q_2-\Delta_c).
\end{align*}
Let $B_1=u_1+\min\{d_1,\Lambda_1\}$ if the threat is credible ($e\le\bar m_U$, with $e=g_1+\pos{Q_1+d_1}-\pos{Q_1}$) and $B_1=0$ otherwise. In the subgame-perfect equilibrium, U issues the ultimatum, and E accepts, if and only if
\begin{equation*}
\Gamma\equiv v_c-k+\min\{\Delta R_U,\;(\Delta R_U-\Delta R_H)+B_1-\sigma-r^c\}>0 .
\end{equation*}
The payment is $T^*=\pos{\Delta R_H-B_1+\sigma+r^c}$, U's gain is $\Gamma$, and E's payoff is
$\max\{\Delta R_H-B_1,\,-\sigma-r^c\}+\pos{Q_1-\Delta_c}+\mathrm{Val}_H(Q_2-\Delta_c)$.
An ultimatum that is issued is accepted. The credibility condition $e\le\bar m_U$ does not depend on $\Delta_c$.
\end{proposition}
```

### Proof

```latex
\begin{proof}[Proof of \cref{prop:control}]
\emph{Period 2.} After the period-1 outcome E holds a premium $q\in\{Q_2,Q_2-\Delta_c\}$. If it invests, the period-2 contest (Lemma 1) gives it $\delta\pos{q+\bar I}$; otherwise $\delta\pos{q}$. It invests iff $\delta(\pos{q+\bar I}-\pos{q})>K_I$, that is iff $I(q)=1$. So E's continuation value, in period-1 units and net of $K_I$, is $\mathrm{Val}_H(q)$ and U's continuation cost is $\mathrm{Rent}_U(q)$. The function $h(q)=\pos{q+\bar I}-\pos{q}$ is nondecreasing, so $I$ is nondecreasing; hence $q+\bar I\,I(q)$ and $\mathrm{Rent}_U$ are nondecreasing, and $\mathrm{Val}_H(q)=\max\{\delta\pos{q},\delta\pos{q+\bar I}-K_I\}$ is nondecreasing.

\emph{No ultimatum.} E gets $\pos{Q_1}+\mathrm{Val}_H(Q_2)$ and U gets $-\pos{Q_1}-\mathrm{Rent}_U(Q_2)$.

\emph{Acceptance.} Control passes before the period-1 contest, so E's premia are $Q_1-\Delta_c$ and $Q_2-\Delta_c$. No stake is triggered, and withdrawing $J$ would cost U $g_1+\pos{Q_1-\Delta_c+d_1}-\pos{Q_1-\Delta_c}\ge 0$, so U keeps baseline provision. E gets $T-\sigma-r^c+\pos{Q_1-\Delta_c}+\mathrm{Val}_H(Q_2-\Delta_c)$ and U gets $v_c-k-T-\pos{Q_1-\Delta_c}-\mathrm{Rent}_U(Q_2-\Delta_c)$.

\emph{Refusal.} E keeps control. If U executes the threat, E's aligned payoff falls by $u_1+d_1$ and its premium rises to $Q_1+d_1$; by Lemma 1 E gets $-(u_1+d_1)+\pos{Q_1+d_1}$ in period 1 and U gets $-g_1-\pos{Q_1+d_1}$. If U does not execute, E gets $\pos{Q_1}$ and U gets $-m-\pos{Q_1}$, where $m\le\bar m_U$ is the stake. Period 2 is as above with $q=Q_2$ in both cases. U executes iff $e\le m$. Stakes are free, so U can set $m=\bar m_U$, and the threat is executed iff $e\le\bar m_U$. None of these payoffs involves $\Delta_c$, because the threat is executed only when E keeps control. When the threat is executed, E's period-1 loss relative to no ultimatum is $u_1+d_1-\pos{Q_1+d_1}+\pos{Q_1}$. If $Q_1\ge 0$ this is $u_1$; if $-d_1<Q_1<0$ it is $u_1-Q_1$; if $Q_1\le -d_1$ it is $u_1+d_1$. In all cases it equals $u_1+\min\{d_1,\Lambda_1\}=B_1$. So E's refusal payoff is $\pos{Q_1}-B_1+\mathrm{Val}_H(Q_2)$, with $B_1=0$ if the threat is not credible.

\emph{E's decision.} E accepts iff $T-\sigma-r^c+\pos{Q_1-\Delta_c}+\mathrm{Val}_H(Q_2-\Delta_c)\ge\pos{Q_1}-B_1+\mathrm{Val}_H(Q_2)$, that is iff $T\ge\Delta R_H-B_1+\sigma+r^c$.

\emph{U's decision.} With $T\ge 0$ and an indifferent E accepting, the cheapest accepted offer is $T^*=\pos{\Delta R_H-B_1+\sigma+r^c}$ (any lower offer is refused, and no optimal offer would exist if E refused at indifference). Relative to no ultimatum, the accepted offer gives U
\[
v_c-k+\Delta R_U-T^*=v_c-k+\min\{\Delta R_U,\;\Delta R_U-\Delta R_H+B_1-\sigma-r^c\}=\Gamma ,
\]
using $x-\pos{y}=\min\{x,x-y\}$. A refused ultimatum gives U $-k-e$ relative to no ultimatum when the threat is credible and $-k-m\le -k$ otherwise; since $e\ge 0$, this is never strictly positive. Hence U issues iff $\Gamma>0$, and every issued ultimatum is accepted. E's payoff is $T^*-\sigma-r^c+\pos{Q_1-\Delta_c}+\mathrm{Val}_H(Q_2-\Delta_c)$, and $T^*-\sigma-r^c=\max\{\Delta R_H-B_1,-\sigma-r^c\}$.
\end{proof}
```

### Numerical check

`v2_m4_prop4.py` solves the game by backward induction from primitives: E's investment by comparing its two payoffs, period rents from the static benchmark, U's execution decision after a refusal by comparing its ex post payoffs including the forfeited stake, U's withdrawal decision after acceptance, U's stake in $\{0,\bar m_U\}$ and its payment on a grid, E's accept or refuse, and U's issue decision by strict comparison with no ultimatum. No formula is used in the solver. Draws: 9 hand-picked edge cases (both premia zero; $\sigma+r^c=B_1$; $\Gamma=0$; $e=\bar m_U$; the investment tie $\delta(\pos{q+\bar I}-\pos q)=K_I$; $g_1=0$; finite $\Delta_c<Q_2$; unconditional bite with $Q_1>0$; a zero-bite purchase), 20,000 draws with small integers and dyadic $\delta$ on a grid of mesh $1/64$ (all thresholds on the grid, ties exact), and 10,000 continuous draws on a grid of mesh $10^{-3}$ (319 draws with $|\Gamma|<3\times 10^{-3}$ set aside). $\Delta_c$ is finite in more than half of the draws and the investment option is active in about half. Results: zero mismatches in the issue decision; maximum error in $\Gamma$, $T^*$ and E's payoff exactly $0$ on the integer draws and below $10^{-3}$ (the grid mesh) on the continuous draws; 7,715 draws with issuance and none with a refused ultimatum on path. Under the opposite investment tie rule the answer changes in 139 knife-edge draws, and the formulas with the weak indicator match the brute force in all of 5,000 further draws. Credibility: in 2,000 draws the execution decision after a refusal was the same for eight values of $\Delta_c$ in every draw.


## 2. Corollaries (i) to (v)

### (i) Preventive motive. Verdict: confirmed (sharpened)

```latex
\begin{corollary}[Preventive motive]
$\Gamma>0$ iff $\Delta R_U>k-v_c$ and $B_1+(\Delta R_U-\Delta R_H)>\sigma+r^c+k-v_c$. In particular, if $v_c\le k$, issuance requires $\Delta R_U>0$ and $B_1+(\Delta R_U-\Delta R_H)>\sigma+r^c$. For $\Delta_c>0$, $\Delta R_U>0$ if and only if $Q_1>0$ or $Q_2+\bar I\,I(Q_2)>0$: E's premium is positive at date 1, or its premium after its own investment is positive at date 2.
\end{corollary}
```

```latex
\begin{proof}
The first two statements restate $\Gamma>0$ with $\min\{a,b\}>c\iff a>c$ and $b>c$. For the third, $\pos{Q_1}-\pos{Q_1-\Delta_c}=\min\{\pos{Q_1},\Delta_c\}$, which is positive iff $Q_1>0$. Let $q=Q_2$ and $q'=Q_2-\Delta_c<q$. Since $I$ is nondecreasing, $q'+\bar I\,I(q')<q+\bar I\,I(q)$, so $\mathrm{Rent}_U(q)-\mathrm{Rent}_U(q')>0$ iff $q+\bar I\,I(q)>0$ (with $\delta>0$). Both terms of $\Delta R_U$ are nonnegative, which gives the claim.
\end{proof}
```

### (ii) Investment. Verdict: confirmed (sharpened)

```latex
\begin{corollary}[Autonomy investment]
$\Delta R_U-\Delta R_H=K_I\,[I(Q_2)-I(Q_2-\Delta_c)]\ge 0$. Both arguments of the minimum in $\Gamma$ are weakly larger than when E has no investment option ($\bar I=0$), so an autonomy investment that E cannot commit to forgo weakly raises $\Gamma$. With investment, U can obtain control with no bite at all: if $B_1=0$, the ultimatum is issued iff $\Delta R_U>k-v_c$ and $K_I[I(Q_2)-I(Q_2-\Delta_c)]>\sigma+r^c+k-v_c$, in which case the transfer saves E's investment cost. Example: $\delta=1$, $Q_1=1$, $Q_2=-\tfrac12$, $\bar I=3$, $K_I=2$, $\Delta_c=\infty$, $\sigma=1$, $r^c=v_c=k=0$, no threat: $\Gamma=1$ and $T^*=\tfrac52$.
\end{corollary}
```

```latex
\begin{proof}
The period-1 terms of $\Delta R_U$ and $\Delta R_H$ coincide, and $\mathrm{Rent}_U(q)-\mathrm{Val}_H(q)=K_I I(q)$, which gives the identity; it is nonnegative because $I$ is nondecreasing. Without investment both $\Delta R_U$ and $\Delta R_H$ equal $\Delta R^0=\pos{Q_1}-\pos{Q_1-\Delta_c}+\delta(\pos{Q_2}-\pos{Q_2-\Delta_c})$, so the second argument of the minimum is $B_1-\sigma-r^c$, and with investment it is larger by $K_I[I(Q_2)-I(Q_2-\Delta_c)]\ge 0$. For the first argument let $q=Q_2$, $q'=q-\Delta_c$ and $g(x)=\pos{x}-\pos{x-\Delta_c}$, which is nondecreasing. If $I(q)=I(q')=0$ the period-2 terms are equal. If $I(q)=I(q')=1$, $\mathrm{Rent}_U(q)-\mathrm{Rent}_U(q')=\delta g(q+\bar I)\ge\delta g(q)$. If $I(q)=1>I(q')$, $\mathrm{Rent}_U(q)-\mathrm{Rent}_U(q')=\delta(\pos{q+\bar I}-\pos{q'})\ge\delta(\pos{q}-\pos{q'})$. The case $I(q)=0<I(q')$ is impossible. So $\Delta R_U\ge\Delta R^0$. The zero-bite statement is (i) with $B_1=0$. In the example, $I(Q_2)=1$ since $\pos{2.5}-0>2$, $I(-\infty)=0$, $\Delta R_U=1+2.5$, $\Delta R_H=1+0.5$, so $\Gamma=\min\{3.5,\,2+0-1\}=1$ and $T^*=\pos{1.5+1}=2.5$.
\end{proof}
```

### (iii) Enforceability. Verdict: confirmed

```latex
\begin{corollary}[Enforceability]
Holding $\sigma$, $r^c$, $v_c$ and $k$ fixed, $\Gamma$ and $T^*$ are nondecreasing in $\Delta_c$; $B_1$ and the credibility condition do not depend on $\Delta_c$.
\end{corollary}
```

```latex
\begin{proof}
$\pos{Q_1-\Delta_c}$, $\mathrm{Rent}_U(Q_2-\Delta_c)$ and $\mathrm{Val}_H(Q_2-\Delta_c)$ are nonincreasing in $\Delta_c$ because $\pos{\cdot}$, $\mathrm{Rent}_U$ and $\mathrm{Val}_H$ are nondecreasing. So $\Delta R_U$ and $\Delta R_H$ are nondecreasing in $\Delta_c$, and so is $\Delta R_U-\Delta R_H=K_I[I(Q_2)-I(Q_2-\Delta_c)]$ because $I$ is nondecreasing. Both arguments of the minimum in $\Gamma$ are therefore nondecreasing in $\Delta_c$, and $T^*$ is nondecreasing because $\Delta R_H$ is. $B_1$ and $e$ are computed in the refusal branch, where E keeps control.
\end{proof}
```

### (iv) Old Proposition 3. Verdict: confirmed

```latex
\begin{corollary}
If $v_c=k=0$, $\Delta_c=\infty$ and $\bar I=0$, then $\Gamma=\min\{\pos{Q_1}+\delta\pos{Q_2},\;B_1-\sigma-r^c\}$; if moreover $Q_1<0$, $\Gamma=\min\{\delta\pos{Q_2},\,B_1-\sigma-r^c\}$.
\end{corollary}
```

```latex
\begin{proof}
With $\Delta_c=\infty$ and no investment, $\Delta R_U=\Delta R_H=\pos{Q_1}+\delta\pos{Q_2}$; substitute into $\Gamma$.
\end{proof}
```

### (v) Strategic Chinese counter-threat. Verdict: corrected

The memo's statement is right in substance, but the condition is not "$\rho=0$". What matters is the sign of China's ex post value of carrying out the punishment, which depends on the instrument (lost exports, retaliation), not on China's relative-gains weight. $\rho$ (or any value China places on Europe keeping control) matters for a different question: whether China strictly prefers to deter.

```latex
\begin{corollary}[Counter-threats against a transfer]
Before U decides, China announces a punishment $r\in[0,\bar r]$ of a transfer and a stake $m_C\le\bar m_C$. Carrying out $r$ after a transfer has ex post value $-c_C(r)$ to China, where $c_C$ is continuous and increasing with $c_C(0)=0$; the threat is credible iff $c_C(r)\le m_C$. China gets $H_C\ge 0$ if E keeps control, and the ex post payoff of its punishment decision ($-c_C(r)$ if it punishes, $-m_C$ if it does not) if control passes. Let $\Gamma(r)$ be $\Gamma$ with $r^c=r$ and $r_{\max}=\max\{r\le\bar r:c_C(r)\le\bar m_C\}$. In every subgame-perfect equilibrium:
\begin{enumerate}[(a)]
\item if control is transferred, China does not punish: on the path $r^c=0$, the payment is $\pos{\Delta R_H-B_1+\sigma}$ and $\Gamma(0)>0$;
\item a credible punishment $r>0$ is announced only if it deters, $\Gamma(r)\le 0$;
\item if $H_C>0$, control is transferred iff $\Gamma(r_{\max})>0$; otherwise China deters with a credible $r\ge v_c-k+\Delta R_U-\Delta R_H+B_1-\sigma$ whenever $\Gamma(0)>0$;
\item if $H_C=0$ and $\Gamma(0)>0\ge\Gamma(r_{\max})$, both the transfer and its deterrence are equilibrium outcomes.
\end{enumerate}
If punishing is self-rewarding ($c_C(r)<0$ for some $r$), (a) fails: China may let the transfer happen and punish it.
\end{corollary}
```

```latex
\begin{proof}
Given an announcement, E and U play the game of \cref{prop:control} with $r^c=r$ if the threat is credible and $r^c=0$ otherwise, and $\Gamma(r)$ is nonincreasing in $r$. After a transfer China punishes iff $c_C(r)\le m_C$.
(a) Suppose control passes on the path. Then $\Gamma(r^c)>0$ for the effective $r^c$, so $\Gamma(0)\ge\Gamma(r^c)>0$. If $r^c>0$, China punishes and gets $-c_C(r^c)<0$. If the threat is not credible but $m_C>0$, China forfeits $m_C$. In either case announcing $(0,0)$ instead leaves the transfer in place (because $\Gamma(0)>0$) and gives China $0$, a profitable deviation. So on the path China gets $0$, the effective $r^c$ is $0$, and $T^*=\pos{\Delta R_H-B_1+\sigma}$.
(b) By (a), a credible $r>0$ on the path is not followed by a transfer, so U does not issue, which by \cref{prop:control} means $\Gamma(r)\le 0$.
(c) If $\Gamma(0)\le 0$, no announcement produces a transfer. If $\Gamma(r_{\max})>0$, every announcement produces a transfer and, by (a), China announces no credible punishment. If $\Gamma(r_{\max})\le 0<\Gamma(0)$, announcing $r_{\max}$ with $m_C=\bar m_C$ deters and gives $H_C>0$, while any announcement that lets the transfer happen gives at most $0$; so China deters. The deterring credible announcements are those with $\Gamma(r)\le 0$, that is $r\ge v_c-k+\Delta R_U-\Delta R_H+B_1-\sigma$ (the first argument of the minimum is positive because $\Gamma(0)>0$).
(d) With $H_C=0$, China gets $0$ both from deterring and from announcing nothing and letting the transfer happen.
If $c_C(r)<0$, a transfer followed by punishment gives China $-c_C(r)>0$, which can exceed $H_C$.
\end{proof}
```

Under private information (Proposition 5) the argument in (a) does not carry over: types that accept are punished on the path, so a punishment with negative ex post value is executed with positive probability whenever U issues and $F(\hat s)>0$.

### Numerical check for the corollaries

Corollaries (i) to (iv) are checked inside `v2_m4_prop4.py` on the same 30,009 draws, using brute-force quantities only (U's rent saving, E's refusal loss, E's continuation values). (i): no issued ultimatum with $v_c\le k$ violated the two necessary conditions. (ii): the identity holds to $2.7\times 10^{-15}$, and $\Gamma$ computed by brute force with the investment option was never below $\Gamma$ with $\bar I=0$; the zero-bite purchase example gives $\Gamma=1$, $T^*=2.5$ in the brute force. (iii): 3,000 draws, each solved for $\Delta_c\in\{0,0.5,1,2,3,4,6,9,\infty\}$; the brute-force $\Gamma$ was nondecreasing in every draw. (iv): 1,504 draws in the special case, maximum error $0$ on integer draws and below $10^{-3}$ on continuous draws. (v): `v2_m4_prop4_china.py`, 5,000 integer draws; for each, China's announcement is chosen on a grid of $r$ (step $\tfrac12$ up to $\bar r\le 6$) and stakes $\{0,\bar m_C\}$ with $c_C(r)=\gamma r$, $\gamma\in\{\tfrac12,1,2\}$, $H_C\in\{0,\tfrac14,1\}$, and the full game is solved for each announcement. In every China-optimal announcement of every draw, (a), (b) and (c) held and the on-path payment matched $\pos{\Delta R_H-B_1+\sigma}$ (529 draws with a transfer, 394 with deterrence). With $H_C=0$ the transfer outcome was not unique in 183 draws. With a self-rewarding punishment ($\gamma=-\tfrac12$) China punished a transfer on the path in 968 of 5,000 draws.


## 3. Lemma (spent and self-limiting cuts)

**Verdict: confirmed (scope stated).**

### Final statement

```latex
\begin{lemma}[Spent and self-limiting cuts]\label{lem:selflimit}
Let dates $s=1,\dots,N$ have premia $Q_s$, slack $\Lambda_s=\pos{-Q_s}$ and discount $\delta$. A cut over a set $S$ of dates withdraws at each $s\in S$, before the date-$s$ contest, a bundle with unconditional part $u_s$, conditional part $d_s$ and direct ex post cost $g_s\ge 0$ to U. Suppose that at every $s\in S$ U still retains E after the cut ($Q_s+d_s<V_s$ and $Q_s+d_s\le\bar m_U$), and that the cut does not change the premium at any other date. Then:
\begin{enumerate}[(i)]
\item the bite of the cut, E's loss net of the rents U must then pay, is $\sum_{s\in S}\delta^{s-1}\big(u_s+\min\{d_s,\Lambda_s\}\big)$;
\item U's cost of carrying it out is $\sum_{s\in S}\delta^{s-1}e_s$ with $e_s=g_s+\pos{Q_s+d_s}-\pos{Q_s}$; with a separate stake at each date, the date-$s$ withdrawal is carried out iff $e_s\le m_s\le\bar m_U$;
\item extending a cut into a date with $Q_s\ge 0$ adds $\delta^{s-1}u_s$ to its bite and $\delta^{s-1}(g_s+d_s)$ to U's cost. A purely conditional instrument ($u_s=0$) extended into such a date adds nothing to the bite.
\end{enumerate}
\end{lemma}
```

### Proof

```latex
\begin{proof}[Proof of \cref{lem:selflimit}]
Fix $s\in S$. Without the cut, Lemma 1 gives E a date-$s$ payoff of $\pos{Q_s}$ above its aligned baseline and costs U $\pos{Q_s}$. With the cut, E's aligned payoff falls by $u_s+d_s$ and its exit payoff by $u_s$, so its premium becomes $Q_s+d_s$; since U still retains E, Lemma 1 gives E $-(u_s+d_s)+\pos{Q_s+d_s}$ and costs U $g_s+\pos{Q_s+d_s}$. E's date-$s$ loss is $u_s+d_s-\pos{Q_s+d_s}+\pos{Q_s}$, which equals $u_s$ if $Q_s\ge0$, $u_s-Q_s$ if $-d_s<Q_s<0$ and $u_s+d_s$ if $Q_s\le -d_s$, that is $u_s+\min\{d_s,\Lambda_s\}$. U's extra date-$s$ cost is $e_s$. Because the cut changes no other date's premium, the date-$s$ effects add up with weights $\delta^{s-1}$, which gives (i) and the first part of (ii). At date $s$, after the condition is met, U's continuation does not depend on whether it withdraws, so it withdraws iff $-e_s\ge -m_s$. For (iii), $Q_s\ge 0$ gives $\Lambda_s=0$ and $\pos{Q_s+d_s}-\pos{Q_s}=d_s$.
\end{proof}
```

Scope. Both conditions matter, in opposite directions. (1) If $Q_s+d_s\ge\min\{V_s,\bar m_U\}$, the cut drives E out at $s$; E's loss is then $u_s+d_s-\pos{\min\{Q_s+d_s,V_s,\bar m_U\}}+\pos{\min\{Q_s,V_s,\bar m_U\}}$, which exceeds the formula. (2) If E responds to the cut, for instance by the autonomy investment of \cref{prop:control} when the cut is known before E decides, the bite is smaller. Example: $\delta=1$, $Q_2=-1$, $d_2=1$, $u_2=0$, $\bar I=3$, $K_I=2.5$. Without the cut E does not invest and gets $0$; with it the premium is $0$, E invests and gets $3-2.5-1=-0.5$, so the bite is $0.5$, while the formula gives $1$.

### Numerical check

Part A of `v2_m4_cuts_windows.py`: 20,000 draws with $N\in\{1,\dots,5\}$, random cut sets, $u_s$ zero or positive, $\delta=1$ or random. E's loss and U's cost are computed by comparing the two paths of Lemma-1 contest outcomes date by date. In the 13,927 draws inside the scope the maximum errors are $3.6\times10^{-15}$ (bite) and $1.8\times10^{-15}$ (cost); the extension identities in (iii) hold to $1.3\times10^{-15}$. In all 6,073 draws outside the scope the true loss exceeds the formula. The investment example is reproduced (bite $0.5$ against $1$).


## 4. Windows corollary

**Verdict: corrected.** The memo requires a date $t'>t$ with $Q_{t'}>0$. With the general bite of Proposition 2(a), an unconditional part $u_t$ bites even when $Q_t\ge 0$, and an ultimatum at $t$ also removes the date-$t$ rent (the transfer precedes the date-$t$ contest). Counterexample: $N=2$, $\delta=1$, $Q=(1,-5)$, $u_1=3$, $d_1=g_1=0$, $\sigma+r^c=1$. No date satisfies the memo's condition, but at date 1 U gains $\min\{\pos{Q_1}+\delta\pos{Q_2},\,u_1-\sigma-r^c\}=1>0$ and issues. The fix is $t'\ge t$. When every $u_t=0$, a bite above $\sigma+r^c\ge 0$ requires $Q_t<0$, so the two conditions coincide and the old corollary is recovered.

### Final statement

```latex
\begin{corollary}[Windows]\label{cor:windows}
Consider $N$ dates with $v_c=0$ and $\Delta_c=\infty$. At any date $t$ at which E still holds control, U may issue, at cost $k>0$, an ultimatum: transfer control for all remaining dates against a payment $T\ge 0$, or face a cut at date $t$ only, with bite $b_t=u_t+\min\{d_t,\Lambda_t\}$ and execution cost $e_t=g_t+\pos{Q_t+d_t}-\pos{Q_t}$. Call $t$ \emph{eligible} if $e_t\le\bar m_U$, $b_t>\sigma+r^c$, and $Q_{t'}>0$ for some $t'\ge t$. There is $\bar k>0$ such that for every $k\in(0,\bar k)$, U issues an ultimatum on the equilibrium path if and only if some date is eligible. Every ultimatum issued is accepted, and the first one comes no later than the last eligible date (possibly at a date that is not eligible). The same holds at $k=0$ when U issues only if it strictly gains. If $u_t=0$ at every date, the condition $t'\ge t$ can be replaced by $t'>t$.
\end{corollary}
```

### Proof

```latex
\begin{proof}[Proof of \cref{cor:windows}]
Let $R_s=\sum_{\tau\ge s}\delta^{\tau-s}\pos{Q_\tau}$ be the value of the rents from date $s$ on, and $c=\sigma+r^c$.

\emph{Step 1.} If no date in $\{s,\dots,N\}$ is eligible, no ultimatum is issued in the subgame that starts at $s$ with E in control. By backward induction, suppose this holds from $s+1$. Then at $s$ the continuation after a refusal and after no ultimatum is the same: rents $R_{s+1}$ to E and $-R_{s+1}$ to U. As in the proof of \cref{prop:control} (with $\delta\,\mathrm{Rent}$ replaced by $\delta R_{s+1}$, $\Delta_c=\infty$, no investment), the cut is executed after a refusal iff $e_s\le\bar m_U$, E's refusal loss is $b_s$ if so and $0$ otherwise, and an accepted ultimatum gives U $-k+\min\{R_s,\,b_s^{\mathrm{eff}}-c\}$ relative to no ultimatum, where $b_s^{\mathrm{eff}}$ is $b_s$ or $0$. A refused ultimatum gives at most $-k$. Since $s$ is not eligible, $R_s=0$ or $b_s^{\mathrm{eff}}\le c$, so U's gain is at most $-k\le 0$ and U does not issue.

\emph{Step 2.} Suppose some date is eligible and let $t^*$ be the last one. By Step 1, no ultimatum is issued after $t^*$, so in the subgame at $t^*$ with E in control U's gain from issuing is $-k+\min\{R_{t^*},\,b_{t^*}-c\}$. Eligibility gives $b_{t^*}>c$ and $R_{t^*}>0$ (some $Q_{t'}>0$ with $t'\ge t^*$ and $\delta>0$). Let $\bar k=\min\{R_{t^*},b_{t^*}-c\}$. For $k<\bar k$ U issues at $t^*$ if E still holds control there. Hence on the path an ultimatum is issued at $t^*$ or earlier. If no date is eligible, Step 1 at $s=1$ shows that none is issued.

\emph{Step 3.} At any date, a refused ultimatum leaves the state unchanged (E holds control at the next date) and costs U $k$ plus the execution cost $e_t\ge 0$ or the stake, so it is never strictly better than issuing nothing. Every ultimatum issued is accepted. With $k=0$ and strict issuing the same steps apply with $\bar k$ replaced by any positive number.

\emph{Step 4.} If $u_t=0$, $b_t=\min\{d_t,\Lambda_t\}>c\ge 0$ requires $Q_t<0$, so a date $t'\ge t$ with $Q_{t'}>0$ satisfies $t'>t$.
\end{proof}
```

### Numerical check

Part B of `v2_m4_cuts_windows.py` reuses the backward induction of `v_cor2.py` and `coh_windows.py`, extended to bundles with unconditional parts and execution by comparison of U's ex post payoffs with a stake in $\{0,\bar m_U\}$. It uses exact rational arithmetic, so every tie is exact. 60,000 draws with $N\in\{2,\dots,6\}$, integer premia in $[-6,4]$, $\delta\in\{1,\tfrac12,\tfrac9{10}\}$, and $u_t>0$ possible in 24,111 draws; each draw is solved at $k=0$ with strict issuing and at $k=10^{-9}$. The memo's condition misclassifies 1,030 draws, all with some $u_t>0$ (none when all $u_t=0$). The revised condition matches every draw under both values of $k$, and the two values of $k$ never disagree. Of 20,199 draws with an ultimatum, 13,923 issue at the last eligible date and 1,202 issue at a date that is not itself eligible (earlier action to pre-empt a later window). No refused ultimatum is ever optimal.


## 5. Remark (self-binding vs dual key)

**Verdict: corrected.** The pre-emption claim is right. The memo's condition for E to prefer binding compares $-\sigma^b-r^b$ with E's payoff from an ultimatum; it is correct only when U would issue the ultimatum without binding and binding pre-empts it. If U would not issue absent binding, E never strictly prefers to bind (it gives up $\delta\pos{Q_2}\ge 0$ and pays $\sigma^b+r^b\ge 0$). Counterexample to the memo's condition: $\delta=\tfrac14$, $Q_1=-4$, $Q_2=-2$, $d_1=5$, $\bar m_U=5$, $\sigma=0$, $r^c=2$, $\sigma^b=1$, $r^b=0$, $v_c=k=0$. No ultimatum is issued ($Q_2<0$), E gets $0$ without binding and $-1$ with it, but the memo's condition $-1>\max\{0-4,\,-2\}$ says bind. A further point: binding raises E's slack, and with it the bite of U's threat. A partial binding ($\Delta_b<\infty$) can therefore invite an ultimatum that would not otherwise be issued.

### Final statement

```latex
\begin{remark}[Self-binding and dual key]\label{rem:bind}
Before period 1, E can adopt a binding rule (Europeanized or treaty-entrenched controls) that lowers its premium at both dates by $\Delta_b\in(0,\infty]$ at cost $\sigma^b$, drawing a Chinese punishment $r^b$; E keeps the key. The game of \cref{prop:control} is then played with premia $Q_t-\Delta_b$, and the bite of U's threat is computed at the new slack.
\begin{enumerate}[(a)]
\item With $\Delta_b=\infty$, control removes no rents, and the bite becomes $B_1^b=u_1+d_1$ if $g_1\le\bar m_U$ (and $0$ otherwise). U then issues iff $\Gamma^b=v_c-k+\min\{0,\,B_1^b-\sigma-r^c\}>0$, so binding pre-empts the ultimatum iff $v_c\le k$ or $v_c-k+B_1^b\le\sigma+r^c$. If it does not, U demands control and pays $\pos{\sigma+r^c-B_1^b}$.
\item Let $Q_1<0$, $\Delta_c=\infty$, no investment and $\Delta_b=\infty$. E's payoff is $-\sigma^b-r^b-\mathbf 1\{\Gamma^b>0\}\min\{\sigma+r^c,B_1^b\}$ if it binds, and $\max\{\delta\pos{Q_2}-B_1,\,-\sigma-r^c\}$ if it does not bind and $\Gamma>0$, or $\delta\pos{Q_2}$ if it does not bind and $\Gamma\le 0$. In particular, if U would issue the ultimatum without binding and binding pre-empts it, E strictly prefers to bind iff $-\sigma^b-r^b>\max\{\delta\pos{Q_2}-B_1,\,-\sigma-r^c\}$. If U would not issue without binding, E never strictly prefers to bind.
\item A partial binding ($\Delta_b<\infty$) lowers the rents control would remove but raises the slack, hence the bite, so it can make $\Gamma$ positive. Example: $\delta=1$, $Q_1=-1$, $Q_2=10$, $u_1=0$, $d_1=5$, $g_1=0$, $\sigma=1.5$, $r^c=v_c=k=0$. Without binding $\Gamma=\min\{10,\,1-1.5\}<0$. With $\Delta_b=3$, $\Gamma=\min\{7,\,4-1.5\}=2.5$ and U demands control at $T^*=4.5$.
\item Dual-key licensing is a partial control transfer with enforceability $\Delta_d<\infty$, sovereignty cost $\sigma_d<\sigma$, value $v_d$ and Chinese punishment $r^d$. If U can demand either arrangement, it demands the one with the larger of $\Gamma_{\mathrm{full}}$ and $\Gamma_{\mathrm{dual}}$ (each given by \cref{prop:control} with that arrangement's parameters), provided it is positive. Because $\sigma_d<\sigma$, U can obtain a dual key when the bite is too small to obtain full control.
\end{enumerate}
\end{remark}
```

### Proof

```latex
\begin{proof}[Proof of \cref{rem:bind}]
(a) With $\Delta_b=\infty$, $\pos{Q_t-\Delta_b}=0$ and $\mathrm{Rent}_U=\mathrm{Val}_H=0$ at both premia, before and after a transfer, so $\Delta R_U=\Delta R_H=0$. E's period-1 slack is infinite, so the bite of the threat is $u_1+\min\{d_1,\infty\}=u_1+d_1$, and its execution cost is $g_1+\pos{-\infty+d_1}-0=g_1$. \Cref{prop:control} gives $\Gamma^b$ and the payment $\pos{0-B_1^b+\sigma+r^c}$.
(b) After binding, E pays $\sigma^b+r^b$ and earns no rents. If $\Gamma^b>0$ it also accepts the ultimatum and gets $\pos{\sigma+r^c-B_1^b}-\sigma-r^c=-\min\{\sigma+r^c,B_1^b\}$. Without binding, \cref{prop:control} with $Q_1<0$, $\Delta_c=\infty$ and no investment gives $\Delta R_H=\delta\pos{Q_2}$ and E's payoff $\max\{\delta\pos{Q_2}-B_1,-\sigma-r^c\}$ if $\Gamma>0$, and $\pos{Q_1}+\delta\pos{Q_2}=\delta\pos{Q_2}$ if $\Gamma\le 0$. Comparing gives the statements; in the last case $-\sigma^b-r^b-\mathbf 1\{\Gamma^b>0\}\min\{\cdot\}\le 0\le\delta\pos{Q_2}$.
(c) Direct computation with \cref{prop:control}: after binding, $Q_1-\Delta_b=-4$, so $B_1=\min\{5,4\}=4$, and $\Delta R_U=\Delta R_H=7$.
(d) U's payoff from demanding an arrangement is its $\Gamma$ by \cref{prop:control}; it picks the largest, and issues only if it is positive.
\end{proof}
```

By the argument of corollary (v), if China's ex post value of punishing a binding rule is negative, a binding rule that E adopts on the path is not punished; $r^b$ then matters only through deterrence. This step was not checked numerically.

### Numerical check

`v2_m4_selfbind.py`, 6,000 integer draws with $Q_1<0$, $\Delta_c=\infty$, $\bar I=0$, solved by the brute-force solver of `v2_m4_prop4.py` with and without binding (premia shifted, bite recomputed from primitives). Pre-emption in (a): no mismatches. The memo's preference condition fails in 999 draws, none of them with $\Gamma>0$ and pre-emption; the revised condition in (b) matches all 6,000. A partial binding with $\Delta_b\in\{1,\dots,5\}$ invited an ultimatum not otherwise issued in 210 draws; the hand-picked example in (c) gives no ultimatum and E payoff $10$ without binding, and an ultimatum with $T^*=4.5$ and E payoff $3$ (before $\sigma^b$) with $\Delta_b=3$. Dual key: U's brute-force choice between the two arrangements matched (d) in every draw (dual key chosen in 370).


## 6. Proposition 5 (breakdown, general $F$)

**Verdict: corrected.** The memo's formula and comparative statics are right for an ultimatum backed by the threat. With $v_c>0$, a new option matters: U can offer to buy control without staking the threat (stake zero, so the threat is not credible). A refused purchase offer costs U nothing, while a refused threat costs it $e$. When $e$ is large relative to $B_1$ and $v_c>r^c$, U prefers the purchase offer, and the memo's issuance condition then misses issuance. Example (uniform, $\bar\sigma=10$, $B_1=1$, $r^c=0$, $e=20$, $v_c=8$, $R=0$, $k=0$): the memo's condition gives $-1<0$, no issuance, but a purchase offer with cutoff $4$ yields $0.4\times 4=1.6>0$. The purchase offer is never profitable when $v_c\le r^c$, in particular when $v_c=0$, so the memo's statement holds in that case. The comparative static in $v_c$ holds for threat-backed ultimatums. With the purchase option, the refusal probability falls with $v_c$, but the breakdown probability can rise with $v_c$.

### Final statement

```latex
\begin{proposition}[Breakdown]\label{prop:breakdown}
Assume the conditions of \cref{prop:control} with $\Delta_c=\infty$, no investment, $Q_1<0$ and $e\le\bar m_U$, and let $\sigma$ be E's private information, distributed with CDF $F$ on $[0,\bar\sigma]$, density $f>0$ on $(0,\bar\sigma)$, and $F$ log-concave. Let $R=\delta\pos{Q_2}$, $\tilde b=B_1-r^c$ and $\Pi(s;A,x)=F(s)(A-s)-(1-F(s))x$. For $A+x>0$ let $s^*(A,x)$ be the unique solution in $(0,\bar\sigma)$ of $A+x-s=F(s)/f(s)$ if one exists and $\bar\sigma$ otherwise; let $s^*(A,x)=0$ if $A+x\le 0$.
\begin{enumerate}[(a)]
\item \emph{Threat-backed ultimatum.} With payment $T$, E accepts iff $\sigma\le T+\tilde b-R$. U's optimal cutoff is $\hat s=\max\{\tilde b-R,\,\min\{\bar\sigma,s^*\}\}$ with $s^*=s^*(\tilde b+v_c,e)$, its payment is $\hat s-\tilde b+R\ge 0$, and its gain is $\Pi_B=\Pi(\hat s;\tilde b+v_c,e)-k$. Conditional on this ultimatum, E refuses and the threat is executed with probability $P_b=1-F(\hat s)$. For uniform $F$, $s^*=(\tilde b+v_c+e)/2$.
\item \emph{Purchase offer.} If U instead offers to buy control without staking the threat, E accepts iff $\sigma\le T-r^c-R$, the optimal cutoff is $s_0=s^*(v_c-r^c,0)$, and U's gain is $\Pi_0=\Pi(s_0;v_c-r^c,0)-k$. If $v_c\le r^c$, then $\Pi_0\le -k$.
\item U makes an offer iff $\max\{\Pi_B,\Pi_0\}>0$ and backs it with the threat iff $\Pi_B\ge\Pi_0$. If $v_c\le r^c$ (in particular if $v_c=0$), U issues iff $F(\hat s)(\tilde b+v_c-\hat s)-(1-F(\hat s))e>k$, and every offer is threat-backed.
\item Across parameter values at which U issues a threat-backed ultimatum, $P_b$ is nonincreasing in $B_1$, $e$ and $v_c$, nondecreasing in $r^c$ and $R$, and independent of $k$. These comparative statics hold for every continuous $F$ (not necessarily log-concave) when $\hat s$ is the largest, or the smallest, maximizer.
\item If $v_c>r^c$ and U chooses between (a) and (b), then across parameter values at which U makes an offer the refusal probability is nonincreasing in $B_1$ and $v_c$, and the breakdown probability (refusal followed by the executed threat) is nonincreasing in $e$ and nondecreasing in $R$. The refusal probability is nondecreasing in $r^c$ on any range where the threat-backed payment is positive. The other directions can fail: the refusal probability can rise with $e$ and fall with $R$, and the breakdown probability can rise with $B_1$ and $v_c$ and fall with $r^c$.
\end{enumerate}
\end{proposition}
```

Counterexamples for (e), all with uniform $F$ on $[0,10]$, $R=0$, $k=0$: raising $e$ from $0.2$ to $20$ ($B_1=1$, $r^c=0$, $v_c=8$) moves U from the threat (refusal $0.54$) to the purchase offer (refusal $0.6$); raising $B_1$ from $1$ to $2$ ($e=1$, $v_c=8$) moves U from the offer (breakdown $0$) to the threat (breakdown $0.45$); raising $v_c$ from $8$ to $10$ ($B_1=e=1$) moves U from the offer (breakdown $0$) to the threat (breakdown $0.4$); raising $r^c$ from $0$ to $2$ ($B_1=e=1$, $v_c=10$) moves U from the threat (breakdown $0.4$) to the offer (breakdown $0$).

### Proof

```latex
\begin{proof}[Proof of \cref{prop:breakdown}]
\emph{Acceptance.} A type that accepts gets $T-\sigma-r^c$ (no rents remain since $\Delta_c=\infty$). Refusing a threat-backed ultimatum gives $\pos{Q_1}-B_1+R=R-B_1$ by the refusal step of \cref{prop:control}; refusing a purchase offer gives $R$. So E accepts iff $\sigma\le T+\tilde b-R$, respectively $\sigma\le T-r^c-R$ (ties have probability zero).

\emph{U's gain.} Relative to no offer, an accepted offer gives U $v_c+R-T-k$. A refused threat-backed ultimatum gives $-e-k$, since $e\le\bar m_U$ and U executes; a refused purchase offer gives $-k$. A stake in $(0,e)$ is never executed and is forfeited after a refusal, so it is dominated by a stake of zero. Writing the cutoff as $s=T+\tilde b-R$ (threat) or $s=T-r^c-R$ (purchase), U's gain is $\Pi(s;\tilde b+v_c,e)-k$ subject to $s\ge\tilde b-R$, respectively $\Pi(s;v_c-r^c,0)-k$ subject to $s\ge -r^c-R$.

\emph{Shape of $\Pi$.} For $s\le 0$, $\Pi=-x$; for $s\ge\bar\sigma$, $\Pi=A-s$, which is decreasing. On $(0,\bar\sigma)$, $\partial\Pi/\partial s=f(s)\,[A+x-s-F(s)/f(s)]$. Log-concavity of $F$ means $f/F$ is nonincreasing, so $F/f$ is nondecreasing and the bracket is strictly decreasing in $s$. Hence the bracket changes sign at most once, $\Pi$ is nondecreasing on $(-\infty,s^*(A,x)]$ and nonincreasing on $[s^*(A,x),\infty)$, where $s^*(A,x)$ is as defined (the bracket is positive near $0$ iff $A+x>0$, since $F(s)/f(s)\to 0$ as $s\downarrow 0$ when $F(0)=0$ and $F$ is log-concave).

(a) The maximum of a function that rises up to $s^*$ and falls after it, over $s\ge L$, is at $\max\{L,s^*\}$. With $L=\tilde b-R$ and $s^*\le\bar\sigma$ this is $\hat s$, and $T=\hat s-\tilde b+R\ge 0$. For uniform $F$, $F(s)/f(s)=s$.
(b) Here $L=-r^c-R\le 0$ and $\Pi$ is constant on $(-\infty,0]$, so the constraint never binds and the cutoff is $s_0$. If $v_c\le r^c$, $\Pi(s;v_c-r^c,0)=F(s)(v_c-r^c-s)\le 0$ for $s\ge 0$.
(c) Immediate from (a) and (b).

(d) The bracket is increasing in $A+x$, so $s^*(A,x)$ is nondecreasing in $A+x=B_1-r^c+v_c+e$. Hence $\hat s=\max\{B_1-r^c-R,\,s^*\}$ is nondecreasing in $B_1$, $v_c$, $e$, nonincreasing in $r^c$ and $R$, and independent of $k$, and $P_b=1-F(\hat s)$ moves the opposite way. Without log-concavity: $\partial\Pi/\partial A=F(s)$ and $\partial\Pi/\partial x=F(s)-1$ are nondecreasing in $s$, so $\Pi$ has increasing differences in $(s,A)$ and in $(s,x)$. The feasible set $[B_1-r^c-R,\infty)$ rises with $B_1$ and falls with $r^c$ and $R$, in the same direction as $A$ (or with $A$ unchanged). By Topkis's monotonicity theorem the set of maximizers moves in the same direction in the strong set order, so its largest and smallest elements are monotone.

(e) Two facts. First, $\hat s\ge s_0$ always, because $\hat s\ge s^*(\tilde b+v_c,e)\ge s^*(v_c-r^c,0)=s_0$ as $(\tilde b+v_c+e)-(v_c-r^c)=B_1+e\ge 0$. Second, the direction in which U can switch. Write the threat-backed gain in terms of $T$: $\varphi_B(T)=F(T+\tilde b-R)(v_c+R-T+e)-e-k$. Only $T\le v_c+R+e$ can be optimal (a larger $T$ makes acceptance worse for U than refusal), and on that range $\varphi_B$ is nondecreasing in $B_1$ and nonincreasing in $e$ for each $T$, so $\Pi_B$ is nondecreasing in $B_1$ and nonincreasing in $e$. In the cutoff form, $R$ does not enter $\Pi(s;\tilde b+v_c,e)$ and only relaxes the constraint $s\ge\tilde b-R$, so $\Pi_B$ is nondecreasing in $R$. $\Pi_0$ depends on none of $B_1,e,R$. For $v_c$, the envelope theorem (applied to the cutoff form, whose feasible sets do not depend on $v_c$) gives $\partial\Pi_B/\partial v_c=F(\hat s)\ge F(s_0)=\partial\Pi_0/\partial v_c$. So as $B_1$, $R$ or $v_c$ rises U can switch only from the purchase offer to the threat, and as $e$ rises only from the threat to the offer. Within each option the cutoff is monotone as in (d) (for the offer, $s_0$ is nondecreasing in $v_c$ and independent of $B_1,e,R$). Combining: as $B_1$ or $v_c$ rises, the cutoff never falls (a switch moves it from $s_0$ up to $\hat s$), so the refusal probability is nonincreasing. As $e$ rises the breakdown probability is nonincreasing within the threat and drops to zero at a switch. As $R$ rises it is nondecreasing within the threat and rises from zero at a switch. For $r^c$: where the threat-backed payment is positive, the first-order condition in $T$ holds and the envelope theorem gives $\partial\Pi_B/\partial r^c=-F(\hat s)\le -F(s_0)=\partial\Pi_0/\partial r^c$ (the purchase payment $s_0+r^c+R$ is always positive when $v_c>r^c$). So switches go from the threat to the offer, the cutoff falls from $\hat s$ to $s_0$, and the refusal probability rises; within each option it is nondecreasing. The counterexamples in the text show the remaining directions can fail.
\end{proof}
```

### Numerical check

`v2_m4_prop5.py` maximizes U's gain directly over the payment $T\ge 0$ (grid of 4,001 points, bounded local refinement, explicit $T=0$ corner) for the threat-backed ultimatum and for the purchase offer, without using the first-order condition. Families: uniform; truncated normal (mean in $[-0.5,1.5]\bar\sigma$, scale in $[0.1,1]\bar\sigma$); Beta(2,2); triangular (mode at $0$, at $\bar\sigma$ or inside); truncated exponential (rate of either sign); and a bimodal normal mixture that is not log-concave. 1,500 draws per family with $\bar\sigma\in[0.5,8]$, $B_1\in(0,6)$, $r^c$ zero or in $[0,3]$ (so $\tilde b<0$ occurs), $e\in(0,6)$, $v_c$ zero or in $[0,4]$, $k$ zero or in $[0,1]$, $R$ zero or in $[0,6]$. For the five log-concave families, after setting aside 40 to 53 draws per family within $10^{-6}$ of the issuance threshold, the memo's issuance condition (threat-backed) matched the optimization in every draw, the maximum cutoff error over issuing draws was $3.4\times10^{-7}$, and the maximum error in $P_b$ was $2.2\times10^{-7}$. The $T\ge 0$ corner bound in 293 to 388 draws per family and every type accepted in 190 to 522. The purchase offer strictly beat the threat (and was profitable) in 104 to 133 draws per family, never when $v_c\le r^c$. For the bimodal family the first-order formula is wrong in 124 draws (multiple roots), as expected. Comparative statics: 500 draws per family, each parameter raised by a random step in $[0.05,1.5]$, comparisons kept when U issues before and after. For threat-backed ultimatums there were no violations of (d) in any of the six families, including the bimodal one. With the purchase option, the refusal probability violated monotonicity in $e$ (2 to 8 per family) and in $R$ (up to 1), and the breakdown probability in $B_1$ (6 to 12), $v_c$ (4 to 10) and $r^c$ (1 to 9); there were no violations of the directions claimed in (e). The four counterexamples above are reproduced by the script. A further targeted search (switch points in 4,299 random log-concave configurations) found no case in which a higher $r^c$ moved U from the purchase offer to the threat, but the corner case ($T=0$ at the switch) is not covered by the proof.
