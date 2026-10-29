# Verification of the minimal model (notes/minimal/design.md)

Script: `code/checks/minimal_model_check.py` (numpy only, `python3 -I`, about 70 s, 25 checks, 0 failures). Every solver works by backward induction from terminal payoffs and enumerates the SPE outcomes that differ only in tie-breaking. No solver uses the formula it checks.

Notation: $q=c-k$, $[z]^+=\max\{z,0\}$.

## Verdicts

| Claim | Verdict | Change needed |
|---|---|---|
| R1 | confirmed | At $q=V$ Washington is indifferent and both outcomes are SPE. Europe's payoff is $q$ in every SPE. |
| R1' | confirmed (one knife edge) | Needs $c>0$, or a small cost to Washington of cutting a Europe that stays. At $c=0$ with a costless cut, SPE transfers range over $[-k,0]$. |
| R2 | confirmed as written, misleading as a slogan | True only because $u$ cannot be threatened by definition. If Washington can commit to cutting $u$, then $t^*=c-k-u$, as in the paper's Proposition 2(a). Reword. |
| R3 | confirmed (precision) | Single bundle, sunk demands, no transfer. With a transfer: accept iff $t-\sum d_i\ge c-k$. Demands issued one at a time keep the bound but can yield Washington less (ratchet). |
| A | confirmed (sharpened) | Exact with no usable exit; with exit $q>0$ the condition is necessary, not sufficient. The timing claim needs restating: what matters is that the stoppage is set before the round's proposer is known and cannot be lifted after a rejection. A once-and-for-all commitment is not needed. If Europe can choose after learning it proposes, $y$ drops out. |
| B | confirmed (two conditions, one caveat) | Needs $\delta>0$ and the tie rule that Washington demands only if it gains strictly. The result holds only if the period-1 squeeze has no other use. If the same threat could extract cash-like concessions, control is never strictly better. General condition below. Fix the citation: the paper's "special case after Proposition 5", not Corollary 3(iv). |

## Formalization choices

1. **Core.** Europe's payoffs are measured from the status quo. Staying after accepting $t$ gives $u+t$. After a rejection with the threat executed, staying gives $u-k$ and switching gives $u+c-k$. Washington gets $-t$ if Europe stays after accepting, $-V$ if Europe switches, and $0$ if Europe rejects and stays. An indifferent Europe accepts. This is forced in any SPE with a continuum of offers. All other ties are enumerated.
2. **R1' (no commitment).** After a rejection Washington chooses whether to cut $k$, at a cost $e\ge 0$ to itself if Europe stays. Europe then stays or switches. Switching always costs Europe $k$, by the definition of $k$.
3. **R2.** "$u$ is kept whatever Europe does" means $u$ is received at every terminal node, including after a rejection. The check also solves the variant in which Washington can commit to cutting $u$.
4. **R3.** Demands are sunk costs $d_i$ to Europe, worth the same to Washington. They are attached to one ultimatum backed by the committed $k$-threat. The script also solves a protocol of one demand per ultimatum in which Washington may stop at any time.
5. **A.** Rounds of length $\Delta$, $\delta=e^{-r\Delta}$. Each round Europe proposes with probability $\beta$. A proposal is a permanent transfer $P$, worth $(P,-P)$. After a rejection, a stoppage in force costs Washington $(1-\delta)x$ and Europe $(1-\delta)y$ that round. So $x$ and $y$ are flow rates in payoff units. Costs fixed per round give the same sign condition. "Exit not attractive" is taken in its strong form, with no usable exit option. The script also solves the game with an exit option $q$, available after rejecting Washington's offer as in the paper's Proposition 1, and with rupture risk $\lambda$. Washington has no threat in these talks. Four timings are compared: commitment before talks; a choice at the start of each round, before the proposer is drawn; a choice after the proposer is drawn; and a choice by Europe after an offer is rejected. The script uses finite-horizon backward induction, so each SPE is unique, with horizon $(r+\lambda)N\Delta\ge 40$.
6. **B.** Without control, each period Washington offers $p_t\ge0$ with no threat. Europe stays or switches for that period, with $q_t\le V_t$. After a refusal, $k_1$ is cut and the period-1 stage is replayed. Europe's stay value is then $-k_1$ and its switch value $c_1-k_1$. Washington pays the retention rent $c_1$, the paper's replayed contest, so Europe gets $q_1$ in period 1 either way. After control, Europe gets $T-s$ and is paid nothing more. Ties: an indifferent Europe accepts, and Washington demands only if it strictly gains, as in the paper.

## Core model

**R1.** With a committed threat: if $q<V$, the unique SPE outcome is that Washington offers $t^*=q$ and Europe accepts. If $q>V$, Europe switches. If $q=V$, both outcomes are SPE and give the same payoffs. Europe's payoff is $q$ in every SPE. $V$ affects only whether Washington keeps Europe, not $t^*$.

*Proof.* After a rejection, Europe gets $\max\{-k,c-k\}=q$ because $c\ge0$. So it accepts $t$ iff $t\ge q$. Washington compares $-q$ with its rejection payoff. That payoff is $-V$ if $c>0$. If $c=0$ it may be $0$, when Europe stays at indifference, but then $q=-k\le0$, so offering $q$ is still weakly better. $\square$

**R1'.** Without commitment, $t^*=[q]^+$ if $q<V$ and Europe switches if $q>V$, provided $c>0$ or $e>0$. *Proof.* If $q\le0$ and $c>0$, cutting $k$ makes Europe switch at a cost of $V$ to Washington, while not cutting keeps Europe. So Washington does not cut. If $q>0$, Europe switches anyway. So rejection gives Europe $[q]^+$. *Knife edge:* if $c=0$, $e=0$ and $k>0$, Europe stays whether or not $k$ is cut, so Washington is indifferent. SPE then give Europe $0$ or $-k$ (any value in between with mixing). The script finds this case in all 1,197 draws where it occurs.

**R2 (corrected statement).** $t^*$ does not depend on help that Washington provides whatever Europe does and cannot credibly threaten to cut. If Washington can commit to cutting such help, worth $u'$, then rejection gives Europe $q-u'$ and $t^*=c-k-u'$ (when $c-k-u'\le V$). That help then bites one for one at every $q$. This is the paper's Proposition 2(a): $B(J)=u(J)+\min\{d(J),\Lambda\}$, and if $Q\ge0$ only unconditional parts bite. In the minimal model the $k$-threat is purely conditional, so its bite is $\min\{k,[k-c]^+\}=[-q]^+$, and $t^*=[q]^+-[-q]^+=q$. The slogan "only the help Washington would actually withdraw gives it a hold" should read: *Europe's price depends only on what Washington would withdraw if Europe left. Help that Washington provides anyway gives it a hold only if it can credibly threaten to cut it, and then that help bites in full.*

**R3 (precise statement).** Take a single ultimatum backed by the committed $k$-threat, with sunk demands $S$ and transfer $t$. Europe accepts iff $t-\sum_{i\in S}d_i\ge c-k$; with $t=0$, iff $\sum_{S}d_i\le k-c$. *Proof:* rejection gives $q$, as in R1. Two precisions follow, both matching the paper:
- If Europe could still switch later and the demands lapse when it switches (reversible demands), it accepts any bundle, but Washington must return the excess over $k-c$ as rent. Europe's net cost is $\min\{\sum d_i,k-c\}$. The budget is the same (Proposition 2(b)).
- If demands come one at a time, each backed by the same unspent threat, Europe's total loss is at most $k-c$ in every SPE. Europe can always refuse the first demand. But Washington can get less than the single-bundle value. With $n$ identical demands of cost 1 it gets $n \bmod (b+1)$ of them, where $b=\lfloor k-c\rfloor$. Reaching the full budget therefore requires committing to one bundle (Proposition 2(c)(iii)-(iv)).

## Add-on A (standoff)

**Statement.** Assume no rupture risk and no usable exit option. If the stoppage is committed before talks, or set at the start of each round before the proposer is drawn, Europe's take is exactly $\beta x-(1-\beta)y$ for every round length, against $0$ without a stoppage. So committing raises the take iff $\beta x>(1-\beta)y$. At $\beta=0$ the gain is $-y\le0$. $V$ does not enter. Extensions:
- **Exit option $q$, frequent-offer limit.** The take is $\max\{q,0\}$ without a stoppage and $\max\{q,\beta x-(1-\beta)y\}$ with one. The stoppage helps iff $\beta x-(1-\beta)y>\max\{q,0\}$. The sign condition is therefore exact if $q\le0$, and necessary but not sufficient if $q>0$.
- **Rupture risk.** The gain is $(1-\psi)[\beta x-(1-\beta)y]^+$, with $\psi=\lambda/(\lambda+r)$, when exit does not bind. The sign condition is the same.
- **Timing.** If Europe can lift the stoppage after an offer is rejected and $y>0$, the stoppage is never used and the take is unchanged. This holds in the unique SPE of every finite truncation and in Markov equilibria. Non-Markov equilibria of the infinite game can differ, as in Fernandez and Glazer. If Europe chooses after learning that it proposes, it stops only in its own proposal rounds, at no cost on the path. Its take is then $\beta x$, whatever $y$ is.

So the precise requirement is that the stoppage is set before the round's proposer is known and cannot be lifted after a rejection. The per-round decision is time consistent, so no long-run commitment is needed.

*Proof.* Let $v$ be Europe's value at the start of a round. Agreement is immediate, because delay destroys $(1-\delta)(x+y)\ge0$, so Washington's value is $-v$. When Europe proposes, it offers Washington's disagreement value: $P=(1-\delta)x+\delta v$. When Washington proposes, it offers $-(1-\delta)y+\delta v$. So $v=\beta[(1-\delta)x+\delta v]+(1-\beta)[-(1-\delta)y+\delta v]$, which gives $v=\beta x-(1-\beta)y$. Without a stoppage $v=0$. The map is a contraction, so the value is unique. If the stoppage can be lifted after a rejection, lifting saves $(1-\delta)y$ and leaves the continuation unchanged, so the stoppage is never kept. If the proposer is known, the stoppage raises Washington's disagreement value by $(1-\delta)x$ in Europe's rounds, at no cost to Europe because its offer is accepted, and it only costs Europe in Washington's rounds. So $v=\beta x$. The exit and rupture versions are the paper's Proposition 7 and Corollary 5 with constant costs. $\square$

## Add-on B (control)

**Statement.** Let $\delta\in(0,1]$ and assume Washington has no other use for its period-1 threat. Washington's gain from demanding control is
$$\Gamma=\min\{[q_1]^+ +\delta[q_2]^+,\ [k_1-c_1]^+-s\}.$$
It demands control, and Europe accepts, iff $q_2>0$ and $k_1-c_1>s$. The payment is $T^*=[q_1+\delta[q_2]^++s]^+$, which equals the claimed $\max\{0,\delta q_2+s-(k_1-c_1)\}$ when $q_2>0$. The joint payoff falls by $s$. When $\Gamma=0$, for instance when $k_1-c_1=s$, or $q_2=0$, or $\delta=0$, Washington is indifferent and control can also occur in an SPE. This is why the strict tie rule matters.

*Proof.* Europe accepts iff $T-s\ge q_1+\delta[q_2]^+$, so $T^*$ is as stated. Washington's gain is $[q_1]^++\delta[q_2]^+-T^*$. If $T^*>0$, the gain is $[-q_1]^+-s$. If $T^*=0$, then $q_1\le-s-\delta[q_2]^+\le0$ and the gain is $\delta[q_2]^+\le[-q_1]^+-s$. Both cases equal $\Gamma$. If $k_1-c_1>s\ge0$, then $q_1<0$, so $\Gamma>0$ iff $\delta q_2>0$. $\square$

**Caveat (the squeeze has an opportunity cost).** The baseline says Washington "makes no other demands"; the paper makes the same assumption (Proposition 5, assumption 3). Suppose instead that the same period-1 threat could extract sunk concessions worth $\alpha\in[0,1]$ to Washington per unit of cost to Europe. Then Washington demands control iff
$$(1-\alpha)\,\delta q_2>\alpha s\quad\text{and}\quad(1-\alpha)(k_1-c_1)>s .$$
With pure transfers ($\alpha=1$, the units of R1 and R3), control is never strictly better than simply squeezing. Taking $k_1-c_1$ now and paying $\delta q_2$ later dominates control, which costs $s$ more. *Proof sketch:* combine control with concessions $D$ and payment $T$. Europe accepts iff $T\ge D+s+\delta q_2-(k_1-c_1)$. The optimal $D$ is $[k_1-c_1-s-\delta q_2]^+$, which gives a gain of $\min\{\delta q_2,k_1-c_1-s\}+\alpha[k_1-c_1-s-\delta q_2]^+$. Compare this with $\alpha(k_1-c_1)$, the gain from the squeeze alone. The plain-language line should read: *when Europe's alternative is set to improve, Washington wants control while it can still squeeze, unless it can cash the squeeze directly.*

## Consistency with the paper

Mapping: minimal $c$ = paper's $\omega$; minimal $k$ = paper's credible cost of exit, all of it conditional and threatened ($d(J)=k$, $u(J)=0$); $q=Q$; $[k-c]^+=\Lambda$; $u$ = unconditional parts outside the credible set; $x=(1-h)c_S$; $y=\ell$; $s=\sigma$ with $r^c=v_c=\iota=0$, $\Delta_c=\infty$, $\bar I=0$.

- **Lemma 1.** R1' reproduces the payment $[Q]^+$ when $Q<V$. One difference: when $q>V$, Lemma 1 gives Europe $\min\{V,\bar m_U\}$, because China bids competitively, while the minimal model gives $q$, because China's offer is fixed. Either way, the price does not depend on $V$ while Europe stays. That also matches Proposition 1 when $\lambda=0$ or $\beta=0$.
- **Proposition 2(a).** R1 is $[q]^+$ minus the bite $\min\{k,\Lambda\}=\Lambda$. The R2 correction is exactly the paper's unconditional term. R3 is Proposition 2(b) for sunk demands with $B=\Lambda$, together with (c)(i). The ratchet in the script is (c)(iv).
- **Proposition 5, special case** (paper text after the proposition; verify_m4 corollary (iv)): $\Gamma=\min\{[Q_1]^++\delta[Q_2]^+,B_1-\sigma-r^c\}$ with $B_1=[k_1-c_1]^+$. This matches B. The design's citation "Corollary 3(iv)" is wrong: Corollary 3 has parts (a) to (d), and the special case is not one of them. The paper requires the threat to be credible ($e=c_1-[q_1]^+\le\bar m_U$); the minimal model assumes commitment.
- **Corollary 5** with $t_U=0$, $h=0$: $D=\beta x-(1-\beta)y$. The gain $(1-\psi)[D]^+$, the exit condition in part (ii), and timing variants (b) and (c) all match A.

## Check results (script output, summarized)

- **R1:** 40,000 draws (18,963 squeeze, 13,662 pay, 7,375 switch or tie), 0 mismatches. The only payoff-distinct multiple outcomes are at $q=V$ (1,569 draws).
- **R1':** 0 mismatches. The knife edge $c=0$, $e=0$ appears in 1,197 draws, as described above.
- **R2:** 0 mismatches. The threatened-$u$ variant gives $t^*=c-k-u$ (0 mismatches).
- **R1 and R1' on a lattice grid of offers:** 0 mismatches.
- **R3:** 4,000 draws, all subsets, with and without a transfer, 0 mismatches.
- **R3 sequential:** 1,500 draws under four tie rules. The loss bound $k-c$ is never violated. Washington gets strictly less than the single-bundle value in 363 draws. The formula $n\bmod(b+1)$ holds in 49 of 49 cases.
- **A, no exit, $\Delta=0.1$ and $0.01$:** the take equals $\beta x-(1-\beta)y$ to $10^{-13}$ in 3,000 draws. These include 152 exact ties (gain 0), 223 draws with $\beta=0$ and 245 with $\beta=1$. The sign condition never fails. $V$ has no effect, and per-round costs give the same sign. The before-proposer timing equals commitment. With lift-after-rejection and $y>0$ (2,830 draws) the gain is exactly 0. With proposer-known timing the take is $\beta x$, and it rises in 1,156 draws where $\beta x\le(1-\beta)y$.
- **A with exit:** errors against the limit shrink at first order: 0.30, 0.09, 0.025, and 0.004 after Richardson extrapolation. The classification never fails: 1,929 draws with $q\le0$ and 844 with $q>0$. In 164 of the latter the sign condition holds but there is no gain.
- **A with rupture:** errors 0.21, 0.06, 0.017; 1,119 draws classified without error.
- **B:** 20,000 draws (2,568 with a demand), 0 mismatches in the decision, in $T^*$ and in the joint loss $s$. The grid brute force agrees. In the squeeze variant ($\alpha=1$), control is never strictly better. The $\alpha$ condition holds in 2,639 lattice draws. Edge cases: $\delta=0$, $k_1-c_1=s$ and $q_2=0$ all give zero gain with multiple SPE; $s=0$, $c_1=0$ gives $T^*=0$.

## Suggested edits to design.md

1. R1: add "Europe's payoff is $c-k$ in every case; at $c-k=V$ Washington is indifferent."
2. R1': add "(if $c>0$, or if cutting a loyal Europe costs Washington anything)."
3. R2 and the third summary bullet: use the corrected wording above.
4. R3: say "single bundle, sunk demands, no transfer". Add that demands issued one at a time keep the bound but need commitment to reach it.
5. A: replace "commitment has to be made before offers" with "the stoppage must be set before Europe knows who proposes and must not be liftable after a rejection; if Europe can stop only when it proposes, $y$ drops out." Add "exit not attractive means $q\le0$." In the fourth summary bullet, add "in this model" after "matters only": in the full paper, $V$ also works through rupture risk, the rival's valuation, self-harming sanctions and the silicon shield.
6. B: add $\delta>0$, the strict tie rule, and the assumption that the period-1 squeeze has no other use, with the $\alpha$ condition as a footnote. Replace "Corollary 3(iv)" with "the special case stated after Proposition 5".
