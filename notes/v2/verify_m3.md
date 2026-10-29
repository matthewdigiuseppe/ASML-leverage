# Verification report m3: Proposition 2 (slack principle) and Proposition 3 (endogenous conditionality)

Scripts (run with `python3 -I` from any directory; each finishes in under 20 seconds):

- `code/checks/v2_m3_prop2.py`: Proposition 2 (a)-(d), (f), and the protocol variants (set-valued backward induction over adaptive ultimatum sequences).
- `code/checks/v2_m3_prop2e.py`: Proposition 2(e), with China as a player that chooses counter-threats before U's demands (loads the solver from `v2_m3_prop2.py`).
- `code/checks/v2_m3_prop3.py`: Proposition 3 (grid plus golden-section optimization over $\kappa$ for six families of convex $H$; part (d) for four distributions $G$).

Notation as in the memo: $\pos{x}=\max\{x,0\}$, $\Lambda=\pos{-Q}$, $u(J)=\Delta^X(J)$, $d(J)=\Delta^A(J)-\Delta^X(J)$, $B(J)=u(J)+\min\{d(J),\Lambda\}$. For a set $S$ of concessions, $T_{\mathrm r}(S)$ and $T_{\mathrm s}(S)$ are the totals of reversible and sunk costs, and $W(S)=\sum_{k\in S}w_k$.

| Result | Verdict | One-line summary |
|---|---|---|
| 2(a) | confirmed | $B(J)=\min\{\Delta^A(J),\Delta^X(J)+\Lambda\}$ is the bite of an ultimatum at the baseline. It is nondecreasing in $J$, and $B=u$ if $Q\ge 0$. After concessions or withdrawals the marginal bite depends on history. |
| 2(b) | confirmed | Exact for a single (or final) ultimatum issued at the baseline. |
| 2(c) | corrected | The bound $B(J^c)$ holds in every SPE of the adaptive protocol, for every $Q$ (including $Q>0$) and every tie-breaking rule. It needs a fixed credible set $J^c$. It does not need U to fix its sequence in advance. Attainment by one bundle needs U to commit to a single ultimatum. Without commitment, threats that deter are not spent, U reuses them, and U can do strictly worse (a ratchet). |
| 2(d) | corrected | The knapsack is wrong in general. U can overfill $\Lambda$ and pay the excess as rent. Correct program: $\max \sum w_k y_k-\pos{\sum t_k y_k-\Lambda}$ s.t. $\min\{\sum t_k y_k,\Lambda\}\le B(J^c)$. It reduces to the knapsack if $B(J^c)<\Lambda$, or if demands are divisible and $w_k\le t_k$. |
| 2(e) | corrected | Every counter-threat China executes on path is pivotal and crowds out another demand. On-path execution does occur (151 executed threats in 4000 draws). E's loss is unchanged only if U fills the budget. Otherwise it can rise or fall. |
| 2(f) | corrected | Linkage stops the hedge whenever $\min\{y_H,\Lambda\}\le B(J^c)$, at rent $\pos{y_H-\Lambda}$. It is free only if $y_H\le\min\{\Lambda,B(J^c)\}$. |
| 3(a) | corrected | Formula confirmed. Slack is zero only if $Q_0\ge 0$. If $Q_0<0$, $\kappa^*=\kappa_0$ and $\Lambda^*=-Q_0$, so U creates no slack. |
| 3(b) | confirmed | Needs $\kappa_z\ge\kappa_0$ for $H'(\kappa_z)$ to be defined. General closed form given below. |
| 3(c) | corrected | The three listed regimes are confirmed. The memo omits the regime $\kappa^*=\kappa_1<\kappa_z$, where U pays a rent that rises one for one with $Q_0$, and the corner $\kappa^*=\kappa_0$ with $Q_0<0$. |
| 3(d) | refuted (corrected) | $d\bar\kappa/ds_X=g(s_X+s_L)-g(s_X-\bar m_U)$, which can be positive (standard normal $G$, $s_X=0$, $s_L=1$, $\bar m_U=2$). The claim holds if $g$ is nonincreasing on $[s_X-\bar m_U,s_X+s_L]$, or if $s_A$ is held fixed. |

---

## Ambiguities fixed (Proposition 2)

The memo leaves six points open. I fix them as follows.

1. **Payoffs.** E's aligned baseline payoff is $0$ and its exit payoff is $Q$. With conceded set $S$ and withdrawn set $J_w$, E's aligned payoff before rent is $a=-\Delta^A(J_w)-T_{\mathrm r}(S)-T_{\mathrm s}(S)$ and its exit payoff is $x=Q-\Delta^X(J_w)-T_{\mathrm s}(S)$. The replayed contest gives E $\max\{a,x\}$ and costs U the rent $\pos{x-a}=\pos{Q+d(J_w)+T_{\mathrm r}(S)}$. E's baseline payoff is $\pos{Q}$, and its *net loss* is $\pos{Q}-\max\{a,x\}$.
2. **U retains E.** $V$ and $\bar m_U$ exceed every rent that can arise. Without this, E exits after some histories. E's payoff then is at least $x$, so every upper bound on E's loss below survives.
3. **Credible set.** $J^c$ is fixed at the start of the period. Every subset of $J^c$ is a credible threat (for example, one stake per instrument). No instrument outside $J^c$ can be withdrawn during the period.
4. **Execution costs.** Executing a withdrawal of $J$ costs U $e(J)\ge 0$, because the baseline is U's ex post optimal provision.
5. **Protocol.** Each ultimatum names a nonempty set of unconceded demands and a nonempty threat set of unwithdrawn instruments. A deterring threat that is not executed stays available, as the memo implies ("withdrawn instruments stay withdrawn"). U may stop at any time. Every ultimatum either adds a concession or spends an instrument, so the game is finite.
6. **Ties.** E accepts when indifferent unless stated otherwise. The bounds hold for every tie-breaking rule. The scripts compute all SPE outcomes under both rules.

---

## 1. Proposition 2 (slack principle)

### Final statement

```latex
\begin{proposition}[Slack principle]\label{prop:slack}
Let $\Lambda=\pos{-Q}$, $u(J)=\Delta^X(J)$, $d(J)=\Delta^A(J)-\Delta^X(J)$ and
$B(J)=u(J)+\min\{d(J),\Lambda\}=\min\{\Delta^A(J),\Delta^X(J)+\Lambda\}$. Every subset of $J^c$ is a credible
threat, no other instrument can be withdrawn during the period, executing a withdrawal of $J$ costs the United
States $e(J)\ge 0$, and the United States retains Europe after every history.
\begin{enumerate}[label=(\alph*)]
\item \emph{Bite.} Refusing an ultimatum backed by $J$, issued when nothing has been conceded or withdrawn, costs
Europe $B(J)$, net of the rent the United States must then pay. $B$ is nondecreasing in $J$. If $Q\ge 0$, then
$B(J)=u(J)$: only unconditional parts bite.
\item \emph{Reversible concessions.} Europe's net loss from reversible concessions totalling $T$ is
$\min\{T,\Lambda\}$. Faced with a single ultimatum that asks for reversible concessions $T_{\mathrm r}$ and sunk
concessions $T_{\mathrm s}$ and is backed by $J$, Europe accepts if and only if
$\min\{T_{\mathrm r},\Lambda\}+T_{\mathrm s}\le B(J)$.
\item \emph{One budget.}
  \begin{enumerate}[label=(\roman*)]
  \item In every subgame perfect equilibrium of every adaptive sequence of ultimatums, and for every $Q$,
  Europe's total net loss is at most $B(J^c)$. Conditional instruments share one budget: $B(J)-u(J)\le\Lambda$
  for every $J$, and reversible concessions cost Europe at most $\Lambda$ in total, however they are backed.
  \item The United States' equilibrium payoff is at most
  $V_1=\max\{W(S)-\pos{Q+T_{\mathrm r}(S)}:\ \min\{T_{\mathrm r}(S),\Lambda\}+T_{\mathrm s}(S)\le B(J^c)\}$,
  the payoff of the best single ultimatum backed by $J^c$.
  \item If the United States can commit to a single ultimatum, one bundled ultimatum backed by $J^c$ yields
  $V_1$. Europe's loss then equals $B(J^c)$ if the United States has a divisible sunk demand of positive value
  and sufficient size.
  \item Without that commitment the United States still obtains $V_1$ if all demands are reversible and
  $B(J^c)\ge\Lambda$, or if some best single ultimatum contains all of its demands. (In every equilibrium if
  $e(\{j\})>0$ for every $j$; in some equilibrium otherwise.) In general it can obtain strictly less. Threats
  that deter are not spent, so the United States reuses them after Europe concedes, and Europe anticipates
  this. With one instrument with $d=0$ and $n$ identical sunk demands of cost $\tau$, the United States obtains
  exactly $n \bmod (b+1)$ of them, where $b=\lfloor B(J^c)/\tau\rfloor$.
  \end{enumerate}
\item \emph{Rationing.} Suppose all demands are reversible and either the United States can commit to a single
ultimatum or $B(J^c)\ge\Lambda$. Then its optimal demand set solves
\[ \max_{y\in\{0,1\}^K}\ \sum_k w_k y_k-\pos{\textstyle\sum_k t_k y_k-\Lambda}
   \quad\text{s.t.}\quad \min\Big\{\sum_k t_k y_k,\Lambda\Big\}\le B(J^c). \]
This is the knapsack $\max\sum_k w_k y_k$ s.t. $\sum_k t_k y_k\le\min\{\Lambda,B(J^c)\}$ if $B(J^c)<\Lambda$,
or if demands are divisible ($y\in[0,1]^K$) and $w_k\le t_k$ for every $k$. In general the United States may
exceed $\Lambda$ and pay the excess back as rent. The free capacity $\min\{\Lambda,B(J^c)\}$ falls as $Q$ rises
toward $0$. Demands from every issue area draw on it.
\item \emph{Counter-threats.} Before the United States moves, China chooses credible counter-threats
$r_k\in[0,\bar r_k]$. If concession $k$ is made and $r_k>0$, China executes at cost $e^C_k>0$ and Europe bears
the sunk loss $r_k$. China loses $z_k\ge 0$ when concession $k$ is made. The United States makes a single
ultimatum backed by $J^c$, and its optimal bundle is unique at the profiles compared below.
  \begin{enumerate}[label=(\roman*)]
  \item A counter-threat adds $r_k$ to the sunk cost of $k$: Europe accepts $S$ if and only if
  $\min\{T_{\mathrm r}(S),\Lambda\}+T_{\mathrm s}(S)+\sum_{k\in S}r_k\le B(J^c)$.
  \item China does better than with no threats only if the United States' demand set changes.
  \item If a counter-threat on $k$ is executed in China's optimal profile, then dropping it changes the
  United States' demand set to one that contains a demand outside the equilibrium set. China executes on path
  only to crowd out other demands, and this occurs for an open set of parameters.
  \item The United States' payoff is weakly lower under any profile of counter-threats.
  \item Europe's net loss is at most $B(J^c)$ with or without counter-threats. It equals $B(J^c)$ in both cases
  if the United States has a divisible sunk demand of positive value that China cannot threaten. The
  counter-threat then taxes the patron, not the holder. Otherwise Europe's loss can rise or fall.
  \end{enumerate}
\item \emph{Policing a hedge.} Stopping a hedge worth $y_H$ to Europe is a reversible concession. If it is the
only demand, linkage stops the hedge if and only if $\min\{y_H,\Lambda\}\le B(J^c)$ and
$w_H\ge\pos{y_H-\Lambda}$, where $w_H$ is its value to the United States. The United States then pays rent
$\pos{y_H-\Lambda}$. Linkage is free only if $y_H\le\min\{\Lambda,B(J^c)\}$, and its free part
$\min\{y_H,\Lambda\}$ vanishes as $Q\to 0$. A staked threat to block the hedge by flow jurisdiction, with net
ex post cost $e_F$, is credible if and only if $e_F\le\bar m_U$. It leaves $Q$ unchanged and is never executed.
Executing a conditional withdrawal $J$ raises Europe's premium to $Q+d(J)$.
\end{enumerate}
\end{proposition}
```

### Proof

```latex
\begin{proof}
\emph{Step 0 (final-state payoffs).} Let $S$ be the conceded set and $J_w$ the withdrawn set at the end of the
period. Europe's aligned payoff before rent is $a=-\Delta^A(J_w)-T_{\mathrm r}-T_{\mathrm s}$ and its exit payoff is
$x=Q-\Delta^X(J_w)-T_{\mathrm s}$. The replayed contest costs the United States $\pos{x-a}=\pos{Q+d(J_w)+T_{\mathrm r}}$
and gives Europe $\max\{a,x\}=-u(J_w)-T_{\mathrm s}+\max\{Q,-d(J_w)-T_{\mathrm r}\}$. If $Q\ge 0$, the maximum is $Q$,
because $d\ge 0$ and $T_{\mathrm r}\ge 0$. If $Q<0$, then $-\max\{Q,-d-T_{\mathrm r}\}=\min\{\Lambda,d+T_{\mathrm r}\}$.
In both cases Europe's net loss relative to its baseline payoff $\pos{Q}$ is
\[ L(S,J_w)=T_{\mathrm s}+u(J_w)+\min\{d(J_w)+T_{\mathrm r},\Lambda\}
          =T_{\mathrm s}+\min\{\Delta^A(J_w)+T_{\mathrm r},\ \Delta^X(J_w)+\Lambda\}. \]
The second form shows that $L$ is nondecreasing in $J_w$ and in $S$, because $\Delta^A$ and $\Delta^X$ are
nondecreasing. (The conditional part $d$ need not be monotone.) The United States' payoff is
$W(S)-\pos{Q+d(J_w)+T_{\mathrm r}}-e(J_w)$. If the rent exceeded what the United States can credibly pay,
Europe would exit with a payoff of at least $x$, so its loss would be at most $L$.

\emph{(a)} Refusal executes $J$ and nothing has been conceded, so the loss is $L(\emptyset,J)=B(J)$.
Monotonicity of $B$ follows from Step 0. If $Q\ge 0$, then $\Lambda=0$ and $B=u$. After a history with conceded
set $S_0$ and withdrawn set $J_0$, the bite of $J$ is $L(S_0,J_0\cup J)-L(S_0,J_0)$, which in general differs
from $B(J)$.

\emph{(b)} $L(S,\emptyset)=T_{\mathrm s}+\min\{T_{\mathrm r},\Lambda\}$, which equals $\min\{T,\Lambda\}$ if all
concessions are reversible. Accepting a single ultimatum gives loss $L(S,\emptyset)$ and refusing gives $B(J)$.

\emph{(c)(i)} Fix a subgame perfect equilibrium and let Europe deviate to refusing every ultimatum. On the
resulting path nothing is conceded and every withdrawn instrument belongs to $J^c$. The loss is
$L(\emptyset,J_w)=B(J_w)\le B(J^c)$. Europe's equilibrium loss cannot exceed the loss from a deviation. The
argument uses only that withdrawals come from $J^c$, so it holds for adaptive strategies, every $Q$ and every
tie-breaking rule. Next, $B(J)-u(J)=\min\{d(J),\Lambda\}\le\Lambda$. Finally, for fixed $J_w$ the reversible
concessions raise the loss by $\min\{d+T_{\mathrm r},\Lambda\}-\min\{d,\Lambda\}\le\min\{T_{\mathrm r},\Lambda\}\le\Lambda$.

\emph{(c)(ii)} Let $(S,J_w)$ be an equilibrium outcome. By (i) and Step 0,
$L(S,\emptyset)\le L(S,J_w)\le B(J^c)$. So $S$ is acceptable as a single ultimatum backed by $J^c$. The United
States' equilibrium payoff is $W(S)-\pos{Q+d(J_w)+T_{\mathrm r}(S)}-e(J_w)\le W(S)-\pos{Q+T_{\mathrm r}(S)}\le V_1$.

\emph{(c)(iii)} By (b), Europe accepts the maximizer $S^*$ in the definition of $V_1$, so a single ultimatum
yields $V_1$. Let $x\in[0,X]$ be a divisible sunk demand of cost $x$ and value $\omega x$ with $\omega>0$. If
$L(S,\emptyset)<B(J^c)$, adding $x=B(J^c)-L(S,\emptyset)$ keeps the bundle acceptable and raises the United
States' payoff by $\omega x>0$. With $X\ge B(J^c)$, every optimal bundle therefore has $L=B(J^c)$.

\emph{(c)(iv)} \emph{All demands reversible and $B(J^c)\ge\Lambda$.} Every set $S$ satisfies
$L(S,\emptyset)\le\Lambda\le B(J^c)$, so $V_1=\max_S\{W(S)-\pos{Q+T_{\mathrm r}(S)}\}$. Let $S^*$ be an
inclusion-maximal maximizer. Consider the subgame after Europe has conceded $S^*$ with nothing withdrawn. Every
terminal outcome $(S',J_w)$ of that subgame has $S'\supseteq S^*$ and gives the United States at most
$W(S')-\pos{Q+T_{\mathrm r}(S')}-e(J_w)$. This is strictly below $V_1$ if $S'\neq S^*$ (maximality of $S^*$),
and if $J_w\ne\emptyset$ when all $e(\{j\})>0$. So the United States stops, and Europe's loss is
$L(S^*,\emptyset)\le B(J^c)$. Refusing the root ultimatum $(S^*,J^c)$ executes $J^c$, after which no ultimatum
can be made. The refusal loss is therefore exactly $B(J^c)$, and Europe accepts. The United States thus obtains
$V_1$, and by (ii) no more. If some $e(\{j\})=0$, stopping is still optimal in the subgame, which gives an
equilibrium with payoff $V_1$.
\emph{Some best bundle $S^*$ contains every demand.} After $S^*$ is conceded no ultimatum can be made. Europe
accepts $(S^*,J^c)$ because $L(S^*,\emptyset)\le B(J^c)$, which is the refusal loss.
\emph{Ratchet.} Let the only instrument have $\Delta^A=\Delta^X=\beta$, so $u=\beta=B(J^c)$ and $d=0$. Give the
United States $n$ sunk demands of cost $\tau$ and value $w>0$, and let $e>0$. The rent is always $\pos{Q}$.
Every ultimatum is backed by the single instrument, and after a refusal no further ultimatum can be made. Let
$g(m)$ be the number of further concessions from a state with $m$ demands left and the instrument intact. I
show by induction that $g(m)=m \bmod (b+1)$. Clearly $g(0)=0$. An ultimatum asking for $x\in\{1,\dots,m\}$
demands leads, if accepted, to $x+g(m-x)$ concessions in total, at an additional loss $(x+g(m-x))\tau$. Refusal
costs $\beta$. So Europe accepts if and only if $x+g(m-x)\le b$. By the induction hypothesis
$x+g(m-x)\equiv m\pmod{b+1}$. Its only possible value in $\{1,\dots,b\}$ is $\rho=m \bmod (b+1)$, and $x=\rho$
attains it. If $\rho\ge 1$, the United States obtains $\rho$ concessions. If $\rho=0$, no ultimatum is
accepted, and the United States stops because a refused ultimatum costs it $e>0$. So $g(m)=\rho$. With
$n=b+1$ the United States obtains nothing, whereas a single ultimatum would yield $\min\{n,b\}=b$ demands.

\emph{(d)} For every $Q$ and $T\ge 0$, $\pos{Q+T}=\pos{Q}+\pos{T-\Lambda}$. (If $Q\ge 0$, then $\Lambda=0$. If
$Q<0$, then $Q+T=T-\Lambda$.) So the United States' payoff from conceded reversible set $S$ with nothing
withdrawn is $-\pos{Q}+W(S)-\pos{T(S)-\Lambda}$. By (b) and (c)(iii)-(iv) it chooses $S$ to maximize this
subject to $\min\{T(S),\Lambda\}\le B(J^c)$. If $B(J^c)<\Lambda$, the constraint is $T(S)\le B(J^c)<\Lambda$
and the rent term vanishes. If demands are divisible and $w_k\le t_k$, any solution with $T>\Lambda$ can be
reduced: lowering $y_k$ by $\varepsilon$ on some $k$ with $t_k>0$ changes the objective by
$\varepsilon(t_k-w_k)\ge 0$ while $T>\Lambda$. So some optimum has $T\le\Lambda$. If $B(J^c)\ge\Lambda$ (the
other case is covered above), the constraint is slack and this optimum solves the knapsack with capacity
$\Lambda=\min\{\Lambda,B(J^c)\}$.
Without divisibility this fails. Take $\Lambda=B(J^c)=1$ and one demand with $t=1.5$ and $w=1.4$. The
knapsack value is $0$, but the United States obtains $1.4-0.5=0.9$.

\emph{(e)} (i) A counter-threat is a sunk loss that lowers $a$ and $x$ equally. Apply Step 0 and (b).
(iv) Counter-threats leave the United States' payoff from every bundle unchanged (the rent does not depend on
$r$) and shrink the set of acceptable bundles. (ii) China's payoff is
$-\sum_{k\in S}(z_k+e^C_k\mathbf 1\{r_k>0\})$, which is at most its no-threat payoff if $S$ does not change.
(iii) Let $r^*$ be optimal for China, $S^*=S(r^*)$, $k\in S^*$ with $r^*_k>0$, and $r'$ equal to $r^*$ except
$r'_k=0$. If $S(r')=S^*$, China gains $e^C_k>0$ by switching to $r'$, which contradicts optimality. So
$S'=S(r')\ne S^*$. $S^*$ is still acceptable under $r'$ and gives the United States the same payoff, so by
uniqueness the United States strictly prefers $S'$. Then $S'$ was not acceptable under $r^*$. Acceptable sets
are closed under subsets, because the cost in (i) is monotone in $S$. Hence $S'\not\subseteq S^*$: some demand
$j\in S'\setminus S^*$ is crowded out. Example: $B(J^c)=2$. Demand 1 is sunk with $t_1=0.3$, $w_1=1$ and
$z_1=5$, and China cannot threaten it. Demand 2 is sunk with $t_2=1.5$ and $w_2=20$, and China can threaten it
with $\bar r_2=0.4$ at $e^C_2=0.1$. Without threats the United States demands both. With $r_2=0.4$ the pair
costs $2.2>2$, so the United States demands only $k=2$, and China executes. China's payoff rises from $-5$ to
$-0.1$. This persists under small perturbations. (v) The bound is (c)(i), applied to the costs in (i). With
the divisible filler of (c)(iii), every optimal bundle has loss $B(J^c)$ under every profile. In the example,
Europe's loss rises from $1.8$ to $1.9$. Substitution examples in which the loss falls are in the script.

\emph{(f)} The hedge is a reversible demand with $t=y_H$. By (b) Europe accepts if and only if
$\min\{y_H,\Lambda\}\le B(J^c)$. By the identity in (d) the United States gains $w_H-\pos{y_H-\Lambda}$.
Flow jurisdiction is a threat with net execution cost $e_F$, so it is credible if and only if
$e_F\le\bar m_U$. Under complete information it deters and is not executed, and it involves no instrument
whose withdrawal changes $Q$. Executing a withdrawal $J$ gives rent $\pos{Q+d(J)}$ by Step 0.
\end{proof}
```

### Remarks on assumptions (for the text or a footnote)

- **Does (c) need that U cannot add instruments after a refusal?** It needs a fixed credible set. U may choose every threat adaptively from $J^c$, and the bound still holds. If a refusal can make a new instrument credible, the bound fails with respect to the initial set. In the script, an instrument unlocked by the first refusal raises E's loss above $B(J^c_{\text{initial}})$ by up to 4.42. The bound holds with respect to the enlarged set (excess at most $10^{-16}$). Under the memo's stake technology the credible set is $\{j:e_j\le\bar m_U\}$ whatever the history, so the assumption is natural there.
- **Bundle credibility.** Suppose one stake backs one announced ultimatum, so that a bundled threat needs $e(J)\le\bar m_U$. Then the credible sets are not closed under union. The bound $B(\cup\text{credible sets})$ still holds (0 violations in 150 instances). The best single credible bundle can be beaten by a sequence (10 of 150) or can beat the adaptive SPE (7 of 150). Part (c)(iii) needs every subset of $J^c$ to be credible.
- **Commitment.** Within the memo's technology, U can make (c)(iii) available with a staked promise to make no further demand in the period. This promise is credible if $\bar m_U$ exceeds the value of further extraction. If the paper keeps the adaptive protocol, it should say that the bound always holds, and that attainment by one bundle requires this commitment or the conditions in (c)(iv).
- **Spent deterrence as a commitment device.** In the adaptive protocol U sometimes executes a threat on purpose, to remove bite it would otherwise reuse. Example: two instruments with $u=1.2$ and $u=1.0$ ($d=0$), sunk demands $t=1$ ($w=5$) and $t=1.5$ ($w=1$), and $e=0.1$ each. The single-ultimatum value is 5. In every SPE, U first issues an ultimatum that E refuses, which burns one instrument. It then obtains the first demand. Its payoff is 4.9.

### Numerical check (Proposition 2)

`v2_m3_prop2.py` builds random instances with 1 to 4 instruments and 1 to 4 demands. Set functions are additive (40%) or general monotone ($\Delta^X(J)=\max_{I\subseteq J}g(I)$; $\Delta^A=\max\{\Delta^X,h\}$ with $h$ monotone, so $d$ is often non-monotone). $Q$ is negative, zero or positive. Demands are reversible or sunk. Execution costs are zero or positive. Both continuous and integer draws are used, the integer draws to create ties. The solver computes payoffs only from the final-state primitives ($a$, $x$, rent). It finds the full set of SPE outcomes of the adaptive protocol by set-valued backward induction over states (unwithdrawn instruments, conceded demands). Every ultimatum (nonempty demand set, nonempty threat set) is allowed. E accepts when indifferent, or (in a separate run) either response is allowed. A separate solver computes the best single ultimatum. Results: (a) maximum error of $B(J)$ and of $\min\{T,\Lambda\}$ is $8.9\times10^{-16}$ over 3000 instances. (b) 0 acceptance mismatches in 123,300 (threat set, bundle) pairs. (c) 0 bound violations in 4000 adaptive instances (about 1000 with $Q>0$), with maximum excess $1.1\times10^{-16}$. U's SPE payoff never exceeds $V_1$. It falls strictly below $V_1$ in 325 of 2000 continuous instances (127 of 1004 with all $e_j>0$). The sufficient conditions in (c)(iv) hold in 1593 instances, and adaptive and single-ultimatum values coincide in all of them. Refusals on some SPE path occur in 61 of 1004 instances with $e_j>0$. The ratchet lemma has 0 mismatches in 300 draws. (d) In reversible-only instances the memo's knapsack differs from U's optimal value in 521 of 1046 cases, and the corrected program in 0. (f) 0 mismatches in 3000 single-demand draws. Hand-picked cases cover $B=b\tau$ exactly, $Q>0$, the burning example and the parity sequence. With $n=1,\dots,6$ identical demands ($t=1$, $B=1.5$), the adaptive SPE gives $2,0,2,0,2,0$ against a single-ultimatum value of 2. `v2_m3_prop2e.py` gives China a grid of counter-threat levels (4 or 5 levels on each threatenable demand). Over 4000 instances it finds: 0 acceptance-rule mismatches in 13,286 checks; 615 instances where China gains, all with a changed demand set; 140 instances with on-path execution (151 executed threats), all pivotal and all crowding out another demand; 0 cases where U gains; E's loss higher in 89, lower in 405, equal in 3506; and, with a divisible filler, E's loss equal to $B(J^c)$ within $8.9\times10^{-16}$. In 300 adaptive-protocol instances, both executed counter-threats were pivotal.

---

## 2. Proposition 3 (endogenous conditionality)

**Ambiguities fixed.** $H$ is convex and increasing on $[\kappa_0,\bar\kappa]$ with $H(\kappa_0)=0$. $H'$ denotes the right derivative, which is nondecreasing and right-continuous. $w\in[0,1]$ (this makes $\Pi$ concave), and $S_k>0$. For $x\ge 0$ let $\kappa(x)=\inf\{\kappa\in[\kappa_0,\bar\kappa]:H'(\kappa)\ge x\}$, with $\inf\emptyset=+\infty$. Let $\kappa_1=\kappa(S_k)$ and $\kappa_w=\kappa(wS_k)$, so $\kappa_0\le\kappa_w\le\kappa_1$.

### Final statement

```latex
\begin{proposition}[Endogenous conditionality]\label{prop:kappa}
Let $\kappa_z=\kappa_0+Q_0/S_k$ and let $\kappa_1$, $\kappa_w$ be as defined above. Then
\[ \kappa^*=\min\big\{\bar\kappa,\ \max\{\kappa_w,\ \min\{\kappa_z,\kappa_1\}\}\big\} \]
maximizes $\Pi$, uniquely if $H$ is strictly convex, and $Q(\kappa^*)=(\kappa_z-\kappa^*)S_k$.
\begin{enumerate}[label=(\alph*)]
\item If $w=0$, then $\kappa^*=\kappa_0$ when $Q_0\le 0$, and $\kappa^*=\min\{\kappa_z,\kappa_1,\bar\kappa\}$
otherwise. The United States never makes its guarantee more conditional than needed to hold the premium at
zero. It creates no slack: $\Lambda^*=\pos{-Q_0}$.
\item If $w>0$, $\kappa_0\le\kappa_z<\bar\kappa$ and $H'(\kappa_z)<wS_k$, then
$\kappa^*=\min\{\kappa_w,\bar\kappa\}>\kappa_z$ and $\Lambda^*=(\kappa^*-\kappa_z)S_k>0$: conditionality is the
price of concessions. If $Q_0<0$, then $\kappa^*=\min\{\kappa_w,\bar\kappa\}$ and
$\Lambda^*=(\kappa^*-\kappa_z)S_k\ge -Q_0$.
\item Let $H$ be strictly convex and differentiable. Away from regime boundaries:
  \begin{enumerate}[label=(\roman*)]
  \item if $\kappa^*=\kappa_z$, then $d\kappa^*/dQ_0=1/S_k$ and the United States pays no rent: a stronger
  Chinese bid elicits a more conditional guarantee, not a payment;
  \item if $\kappa^*=\kappa_1<\min\{\kappa_z,\bar\kappa\}$ (assurance is costly at the margin before the premium
  reaches zero), $\kappa^*$ does not depend on $Q_0$ and the rent $Q(\kappa_1)>0$ rises one for one with $Q_0$;
  \item if $\kappa^*=\kappa_w\in(\max\{\kappa_z,\kappa_0\},\bar\kappa)$, or if $\kappa^*=\kappa_0>\kappa_z$,
  then $\kappa^*$ does not depend on $Q_0$ and slack falls one for one with $Q_0$: China's bid is paid for out
  of the United States' concessions;
  \item if $\kappa^*=\bar\kappa$, the United States pays $\pos{Q(\bar\kappa)}$, which rises one for one with
  $Q_0$ when $Q(\bar\kappa)>0$. Otherwise slack falls one for one.
  \end{enumerate}
\item $\partial\bar\kappa/\partial s_X=g(s_X+s_L)-g(s_X-\bar m_U)$, with $s_L$ and $\bar m_U$ fixed. Hence
$\bar\kappa$ is nonincreasing in $s_X$ on any range where $g$ is nonincreasing on
$[s_X-\bar m_U,\,s_X+s_L]$, for example if $G$ is unimodal with mode at most $s_X-\bar m_U$. It is then
nonincreasing in access value and, if $s_B'(V)\ge 0$, in $V$. If instead $g(s_X+s_L)>g(s_X-\bar m_U)$,
$\bar\kappa$ rises with $s_X$. If $s_A$ is held fixed when $s_X$ rises (the access value raises the United
States' stake in defending an exiter but not a loyal ally), $\bar\kappa$ is nonincreasing in $s_X$ for every $G$.
\end{enumerate}
\end{proposition}
```

### Proof

```latex
\begin{proof}
Write $\Pi(\kappa)=\varphi(\kappa)-H(\kappa)$ with $\varphi(\kappa)=-\pos{Q(\kappa)}+w\pos{-Q(\kappa)}$ and
$Q(\kappa)=(\kappa_z-\kappa)S_k$. $\varphi$ is continuous and piecewise linear, with slope $S_k$ for
$\kappa<\kappa_z$ and slope $wS_k$ for $\kappa>\kappa_z$. Since $w\le 1$, $\varphi$ is concave, so $\Pi$ is
concave, and strictly concave if $H$ is strictly convex. Its right derivative is
$\Pi'(\kappa)=S_k\mathbf 1\{\kappa<\kappa_z\}+wS_k\mathbf 1\{\kappa\ge\kappa_z\}-H'(\kappa)$, which is
nonincreasing. A concave function on $[\kappa_0,\bar\kappa]$ attains its maximum at
$\min\{\bar\kappa,\sup P\}$, where $P=\{\kappa:\Pi'(\kappa)>0\}$ (and $\sup\emptyset=\kappa_0$). By
right-continuity of $H'$, $H'(\kappa)<x$ if and only if $\kappa<\kappa(x)$.

\emph{Case $\kappa_z\le\kappa_0$.} On the whole interval $\Pi'=wS_k-H'$, so $P=[\kappa_0,\kappa_w)$ and the
maximizer is $\min\{\bar\kappa,\kappa_w\}$. Because $\min\{\kappa_z,\kappa_1\}\le\kappa_0\le\kappa_w$, this is
the formula.

\emph{Case $\kappa_z>\kappa_0$.} Here $\kappa\in P$ if and only if $\kappa<\min\{\kappa_z,\kappa_1\}$ or
$\kappa_z\le\kappa<\kappa_w$. If $\kappa_1<\kappa_z$, then $\kappa_w\le\kappa_1<\kappa_z$, the second set is
empty and $\sup P=\kappa_1=\max\{\kappa_w,\min\{\kappa_z,\kappa_1\}\}$. If $\kappa_1\ge\kappa_z$, then
$P=[\kappa_0,\max\{\kappa_z,\kappa_w\})$, and again $\sup P=\max\{\kappa_w,\min\{\kappa_z,\kappa_1\}\}$.

\emph{(a)} If $w=0$, then $\kappa_w=\kappa_0$ because $H'\ge 0$. The formula becomes
$\min\{\bar\kappa,\max\{\kappa_0,\min\{\kappa_z,\kappa_1\}\}\}$, which equals $\kappa_0$ if $Q_0\le 0$ and
$\min\{\kappa_z,\kappa_1,\bar\kappa\}$ otherwise. If $Q_0\ge 0$, then $\kappa^*\le\kappa_z$, so
$Q(\kappa^*)\ge 0$ and $\Lambda^*=0$. If $Q_0<0$, then $\Lambda^*=-Q(\kappa_0)=-Q_0$.

\emph{(b)} $H'(\kappa_z)<wS_k$ means $\kappa_z<\kappa_w\le\kappa_1$. So $\min\{\kappa_z,\kappa_1\}=\kappa_z$ and
$\kappa^*=\min\{\bar\kappa,\kappa_w\}>\kappa_z$. Then $\Lambda^*=-Q(\kappa^*)=(\kappa^*-\kappa_z)S_k>0$. If
$Q_0<0$, the first case applies and $\Lambda^*=(\kappa^*-\kappa_z)S_k\ge(\kappa_0-\kappa_z)S_k=-Q_0$.

\emph{(c)} $\kappa_1$, $\kappa_w$ and $\bar\kappa$ do not depend on $Q_0$, and $\partial\kappa_z/\partial Q_0=1/S_k$.
In the interior of each regime the active branch of the formula is locally constant, except in regime (i),
where it is $\kappa_z$. With $Q(\kappa^*)=(\kappa_z-\kappa^*)S_k$, rent $\pos{Q(\kappa^*)}$ and slack
$\pos{-Q(\kappa^*)}$, the stated derivatives follow: in (i) $Q(\kappa^*)=0$; in (ii) and in (iv) with
$Q(\bar\kappa)>0$, $\partial Q(\kappa^*)/\partial Q_0=1$ and $Q>0$; in (iii) and in (iv) with
$Q(\bar\kappa)<0$, $\partial Q(\kappa^*)/\partial Q_0=1$ and $Q<0$.

\emph{(d)} $\bar\kappa=G(s_X+s_L)-G(s_X-\bar m_U)$. Differentiate in $s_X$. If $g$ is nonincreasing on the
interval, the derivative is nonpositive. If $s_A$ is held fixed, $\partial\bar\kappa/\partial s_X
=-g(s_X-\bar m_U)\le 0$. For the standard normal with $s_X=0$, $s_L=1$ and $\bar m_U=2$, $\bar\kappa=0.8186$ at
$s_X=0$ and $0.8664$ at $s_X=0.5$. The silicon-shield statement follows from the chain rule with
$s_X=s_0+s_B(V)$.
\end{proof}
```

### Numerical check (Proposition 3)

`v2_m3_prop3.py` draws 1500 random problems. $H$ comes from six families: $ax^2+bx$, $ax^2$, $a(e^{cx}-1)$, $ax^p$ with $p\in\{1.5,2,3,4\}$, a kinked piecewise-linear convex function, and a linear function (which produces ties). Other draws: $\kappa_0\in[0,0.3]$, $\bar\kappa-\kappa_0\in[0.05,0.75]$, $S_k\in[0.5,10]$, $Q_0$ negative, zero or positive, and $w\in\{0,1\}$ or uniform on $[0,1]$. Each problem is maximized on a 200,001-point grid with golden-section polishing. The thresholds $\kappa_1$ and $\kappa_w$ come from bisection on $H'$, independently of the grid. The general formula is never beaten: the maximum payoff shortfall is $8.9\times10^{-16}$, and the maximum argmax gap is $3.3\times10^{-8}$ when the maximizer is unique. The memo's (a) applies in 402 draws and (b) in 474 draws, with shortfalls $4.4\times10^{-16}$ and $8.9\times10^{-16}$. All five regimes occur (counts: $\kappa_0$ corner 381, $\kappa_1<\kappa_z$ 257, $\kappa_w>\kappa_z$ 173, $\kappa_z$ 187, capped 502). Finite differences in $Q_0$ over 2000 strictly convex draws give exactly the following triples $(S_k\,d\kappa^*/dQ_0,\ d\,\text{rent}/dQ_0,\ d\,\text{slack}/dQ_0)$: $(1,0,0)$ in regime $\kappa_z$; $(0,1,0)$ in regime $\kappa_1<\kappa_z$ and in the capped regime with $Q(\bar\kappa)>0$; $(0,0,-1)$ in regime $\kappa_w$, at the $\kappa_0$ corner, and in the capped regime with $Q(\bar\kappa)\le 0$. For (d), across 3000 draws of $(s_X,s_L,\bar m_U)$ per distribution, $\bar\kappa$ rises with $s_X$ in 1218 normal, 1198 logistic, 974 exponential and 973 uniform cases. The derivative formula matches finite differences to $3\times10^{-11}$.
