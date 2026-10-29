# Referee report (formal theory): "Owning the Chokepoint: ASML, Alliance Dependence, and the Limits of Europe's Leverage over Washington"

Tag: formal. Reviewed: paper/main.tex and sections 00 to 10, appendices A to C (proofs read in full for Lemma 1, Proposition 1, Corollary 1, Proposition 2, Corollary 2, Proposition 3, Proposition 4, Proposition 5, Corollary 3, Lemma 2, Corollary 4, Remark 1, Proposition 6, Remarks 2 to 4; Proposition 7 and Corollary 5 read at the level of statement, assumptions and appendix structure). Read against the previous round's Referee 1 report (scratchpad ref1.txt), notes/v2/resolutions.md, style_brief.md, integration_notes.md and the drafters' open issues (draft_issues.txt).

## Recommendation

Major revision. The paper is now a different and much better paper than the one Referee 1 reviewed. The static core is credited where it belongs, the slack principle organizes the theory, one commitment technology governs threats and promises, and the dynamic analysis of control has explicit value of control, issuing cost, finite enforceability, an autonomy investment and a strategic China. The proofs I checked are correct. Three things stand between this draft and acceptance. First, the headline sentence in the abstract, introduction and conclusion states the master result backwards, and the slack principle (the organizing theorem) is proved only in the corner of the master game in which the patron's dependence does not matter; both are fixable with a sentence and a short lemma. Second, two modelling details create errors that propagate into the evidence: US flow jurisdiction scales China's gain but not Washington's loss or China's relative gain, and an example attached to Proposition 4(d) is false and flips the substantive reading of the silicon shield. Third, the paper still carries 18 formal statements in the main text; the editors' cut to 19,000 words is feasible only if about eight of them move to the appendix with informal statements in the text. I give a statement-by-statement plan below.

## Has Referee 1 been answered?

| Ref 1 point | Status | Comment |
|---|---|---|
| 1. Headline result not new; do not lead with it | Mostly | Lemma 1 and Corollary 1 are credited to Groseclose and Snyder, Dekel, Jackson and Wolinsky, the outside-option principle, Wagner and CMS. But the abstract's fourth sentence still leads with the known bound and states it in the wrong direction (finding 1). |
| 2. Say what each related model cannot deliver | Yes | Section 3.3, "Each of these works lacks a result we derive", does this well. It is now said three times (intro item 1, Section 3.3, Section 5 "What is new here"); keep one. |
| 3. Conditionality exogenous; security treated asymmetrically | Yes, with a reduced form | $m_S$ is staked under the common technology and $H(\kappa)$ makes the choice interior. $H$ is a reduced form, and only security carries an assurance cost; the closing sentence after Proposition 4 extends the argument to any $d_j$. Acceptable. |
| 4. Organize around the slack principle | Yes | Proposition 2 and Corollary 2. Scope problem under rupture risk (finding 2). |
| 5. Work out relation to shifting-power models | Yes | Preventive-war analogy, Powell and Krainin contrast, Debs and Monteiro, Bas and Coe, Spaniel, Benson and Smith. The inefficiency claim needs a qualifier (finding 5). |
| 6. Fictional scenario framing | Mostly | Scenario is a hook and Appendix C. The Council arithmetic for the scenario is still in Section 7.3 (move it). |
| 7. Why $V$ drops out | Yes, and the paper corrects Referee 1 | The text rightly says $V$ drops out for lack of rupture risk, not for lack of proposal power: a Europe that proposes in almost every round still cannot charge for $V$ when $\lambda=0$. |
| 8. One master game | Yes | Proposition 1 confirms Referee 1's conjecture, $P^*=\max\{Q,\psi(Q+\beta(V-Q))\}$, with payoff uniqueness for every $\Delta$ and the exit-timing footnote. I re-derived the stationary value; it is right. One inconsistency with the commitment technology remains (finding 4). |
| 9. One commitment technology | Yes | Section 4.2. Untargeted Chinese punishment of alignment is set to zero with a reason. |
| 10. Double counting AI; TU at par | Yes | Baseline at $x_j(A)$; in-kind footnote with $\phi_U$. |
| 11. Additivity, binary instruments | Yes | Proposition 2 uses general set functions $\Delta^A,\Delta^X$; AI allocation is continuous. |
| 12. China's objective | Yes, but see finding 3 | Relative-gains weight $\rho$ added. Its interaction with $\theta$ is inconsistent. |
| 13. Dynamic control underdeveloped | Largely | $v_c$, $\iota$, $\Delta_c$, observable investment, strategic China (Cor 3(d)), multi-date cuts and repeated ultimatums (Lemma 2, Cor 4). Investment is observable and chosen after the ultimatum, so the Debs and Monteiro or Bas and Coe information problem is absent; say so in Limitations. |
| 14. Breakdown with general $F$, repeated offers | Yes | Log-concave $F$; Topkis for general $F$; Coasean discussion. |
| 15. Hold-up: discounting, costs, multiplicity | Yes | $r>0$, US cost of cutting AI included, Markov equilibria stated and the literature cited. |
| 16. Demote Council result; two-step ACI | Yes | Remark 4 and the two stages. |
| 17 to 18. Back-of-envelope bounds; strategic valuation of China's offer | Partly | The calculation is gone, but the evidence section's claim that a large $\theta$ makes $\omega$ small ignores $\rho V$ (finding 3). The orders of magnitude listed in integration_notes.md are not yet in Section 8. |
| 19. Internal inconsistency of the record reading | Mostly | Supplement No. 4 is now coded as a threat left unexercised; Nexperia is read through Prop 3(a)(iii) with the misjudgment alternative named; stockpiling is disowned. A new inconsistency: the "rationing" reading of the Dutch sequence conflicts with coding the sales controls as flow jurisdiction (finding 7). |
| 20. Predictions that separate from cost minimization | Partly | The separation claimed in Section 5.2 and tab:implications holds only against a cost minimizer with fixed instrument costs (finding 8). |
| Smaller points (anonymity, notation table, citations) | Partly | Notation table added; missing citations added. main.tex still has `\anonymousfalse`, the author name and the AI-assistance footnote; switch for submission. |

## Contribution and positioning

The contribution is now clear and correctly positioned. Against Groseclose and Snyder and Dekel, Jackson and Wolinsky: the bidding benchmark is theirs, and the paper says so; what is added is that the client can propose and talks can rupture, so the patron's dependence returns through $\beta\psi V$. Against the outside-option principle: the threshold in Corollary 1(b) is the principle, credited as such. Against Clayton, Maggiori and Schreger: the contrast (cut-off threats that must each be sequentially rational and are spent, versus pooled enforcement threats; a rival's bid inside the participation constraint; one alignment choice) is stated precisely and matches lit_theory.md. Against Fearon, Powell and Krainin: the windows result (speed affects timing, not occurrence, when $\Delta_c=\infty$; size and speed matter again when $\Delta_c$ is finite) is a genuine and clearly explained contrast.

Two positioning points need work. (i) Grossman and Hart. In the model, control is a commitment device that lowers the holder's future exit premium by $\Delta_c$; it does not allocate residual rights that shape relationship-specific investment. The closer cousins are Fearon (1996) and Hart and Moore on outside options. The one Grossman-Hart effect in the model is in Corollary 3(b), where a transfer spares Europe an investment it would sink only to secure rents, and that effect makes the transfer efficient, contradicting the paper's claim that the transfer is inefficient (finding 5). (ii) The slack principle's novelty relative to CMS is real but would be sharper if the paper showed, in one sentence, that it is a property of the holder's surplus over its outside option and not of the auction protocol (finding 2 gives the generalization).

## Correctness: what I checked

- Lemma 1 and the alternating-raise claim: correct. The text's phrase "weak dominance selects the price $\pos{Q}$" overstates what is proved (finding 18).
- Proposition 1: I re-derived $x_A$, $x_B$, $x^*=\max\{x_A,x_B\}$, the limit and $\hat Q=\lambda\beta V/(r+\lambda\beta)$. The figure thresholds ($Q>-1$ and $Q>-3$) are right. The sup/inf argument in Step 4 is clean.
- Corollary 1: correct.
- Proposition 2: correct. The one-budget bound in (c)(i) is a refuse-everything deviation argument and holds for every tie rule. I checked the ratchet $n \bmod (b+1)$ by hand for $n=b+1,b+2$.
- Corollary 2, Proposition 3: correct, including both numerical examples.
- Proposition 4: the concavity argument and the formula for $\kappa^*$ are correct. Part (d)'s derivative is correct; the example attached to it is false (finding 6).
- Proposition 5 and Corollary 3: correct. I reproduced the zero-bite purchase ($T^*=2.5$, $\Gamma=1$) and the Remark 1(c) example ($\Gamma=2.5$, $T^*=4.5$).
- Corollary 4: correct, and the figure's window dates ($t\le5$ and $t\ge9$ in panel (a)) check out.
- Proposition 6: correct, including the four counterexamples in (e) (I recomputed the first).
- Remarks 2 to 4: correct.

I also checked numerically (200,000 random draws, script in the scratchpad) the generalization proposed in finding 2: under rupture risk the conditional bite never exceeds $\min\{d,P^*(Q)-Q\}$, and it exceeds the stated cap $\min\{d,\pos{-Q}\}$ in about a quarter of draws.

## Required changes, ranked

### Essential

**1. The headline states the master result backwards.** Files 00_abstract.tex, 01_intro.tex, 10_conclusion.tex.
Anchors: "A holder's leverage is bounded by its exit premium" (abstract); "We argue that a chokepoint holder's leverage is bounded by its exit premium" (intro); "we add a third: the holder's exit premium must be positive" (intro); "the hub confers power on its holder only if the holder's exit premium is positive" (conclusion); "A chokepoint holder's leverage over its patron is bounded by its exit premium" (conclusion).
Problem: By Corollary 1(a), $P^*\ge Q$: the exit premium is a floor on what the holder gets, not a ceiling. With rupture risk ($\lambda>0$) and agenda power ($\beta>0$), $P^*$ exceeds $\pos{Q}$, and by Corollary 1(c) the holder is paid even with $Q<0$ whenever $Q+\beta(V-Q)>0$. The upper bound the paper proves is on concessions ($-P^*\le\Lambda$). The weaponized-interdependence condition is likewise overstated.
Fix (abstract): "Without a risk that talks rupture, a holder's leverage is the positive part of its exit premium: the rival's credible offer, net of the costs the patron can credibly impose. Rupture risk adds a share of the patron's dependence that grows with the holder's power to propose." Intro: "We argue that, absent rupture risk, a chokepoint holder's leverage is the positive part of its exit premium, and that a patron's demands are bounded by the holder's slack." Intro item 4 and conclusion: "the holder's exit premium must be positive, or talks must carry a risk of rupture while the holder can make proposals (\cref{cor:master}(c))." Also move the abstract's lead onto the slack principle (Referee 1 point 1).

**2. The slack principle is proved only where rupture risk is zero, but the text claims it in the master game.** Files 05_slack.tex, 04_model.tex.
Anchors: "Consider one period in which Europe is aligned, its premium is" (05); "shows that it bounds what Washington can obtain by any combination of conditional threats" (04).
Problem: Section 5 replays the bidding contest, so Europe's period payoff is $\pos{Q}$, which is the $\lambda=0$ corner of Proposition 1, the corner in which $V$ does not matter. Under rupture risk Europe's payoff is $P^*(Q)$, whose slope in $Q$ is $\psi(1-\beta)<1$ below $\hat Q$. A conditional withdrawal of size $d$ then costs Europe $d-[P^*(Q+d)-P^*(Q)]$, which can exceed $\min\{d,\pos{-Q}\}$. Example: $V=12$, $\beta=\psi=0.5$, $Q=-1$, $d=4$: the bite is 3, while the stated cap is $\Lambda=1$. So $B(J)-u(J)\le\Lambda$ in Proposition 2(c)(i) fails once $\lambda>0$, and the Section 4 sentence that links the two results is not supported.
Fix: State the scope at the top of Section 5.1 and add a two-line lemma (proof in the appendix) that restores the principle in the master game: "This section works in the bidding benchmark, where the rupture weight is zero. Under rupture risk the same argument holds with Europe's surplus over exit, $\Lambda_\psi=P^*(Q)-Q$, in place of $\Lambda$. Because $P^*$ is nondecreasing with slope at most one and $P^*(q)\ge q$, a conditional withdrawal of size $d$ costs Europe $d-[P^*(Q+d)-P^*(Q)]\le\min\{d,\Lambda_\psi\}$ (with zero direct execution cost). $\Lambda_\psi=\pos{-Q}$ when $\lambda=0$, and below $\hat Q$ it equals $\psi\beta V-(1-\psi+\psi\beta)Q$, which rises with $V$." In Section 4 replace the anchored clause with "and \cref{sec:slack} shows that, in the bidding benchmark, slack also bounds what Washington can obtain by any combination of conditional threats." Then say in one sentence what the generalization means: when rupture risk gives Europe a payment, Washington's conditional threats can claw back part of it, so its dependence enlarges the budget it can spend.

**3. Flow jurisdiction scales China's gain but not Washington's loss or China's relative gain.** Files 04_model.tex, 08_evidence.tex, 09_implications.tex.
Anchors: "of which a share $\theta\in[0,1]$ can be blocked by US jurisdiction over China-bound flows" (04); "which makes $\theta$ large and $\omega$ small" (08).
Problem: $V$ is defined as what Washington loses "if Chinese fabs gain access to ASML's frontier tools". If US flow jurisdiction blocks a share $\theta$ of that access, Washington's loss is $(1-\theta)V$, and so is the $\rho V$ term in $W_C=(1-\theta)W+\rho V$. As written, jurisdiction cannot reduce China's relative-gains valuation, and the evidence section's claim that a large $\theta$ makes $\omega$ small is false whenever $\rho V$ is large and the cap does not bind (the zero-sum case Section 4 itself raises). This is Referee 1 point 18 returning through the new $\rho$ term.
Fix: In "Stakes", add: "We measure $V$ net of what US flow jurisdiction blocks: if exit gave Chinese fabs only the share $1-\theta$ of the access it would otherwise give, $V$ is Washington's loss from that share." Then $W_C=(1-\theta)W+\rho V$ is consistent and both terms shrink with $\theta$. In Section 8 write: "which makes $\theta$ large, and with it both what China gains from exit and the relative gain it values, so that $\omega$ is small unless China's cap and Europe's discount on its promises bind first." In "Reduce the nesting" (09) add that lowering $\theta$ also raises $V$ and hence the rupture channel.

**4. Proposition 1 steps outside the one commitment technology.** File 04_model.tex.
Anchors: "Agreements are binding." and "After the bidding stage fixes".
Problem: Section 4.2 says one technology governs every promise and a promise is honoured only up to $\bar m_U$. The master game makes agreements binding, so a perpetual US flow $P^*$ is enforced with no cap, and China's exit flow is honoured forever. Referee 1's point (v) about inconsistent caps between results returns in a new form. The phrase "After the bidding stage fixes $\omega$" also leaves unclear how the auction and the bargaining combine, since $P$ "replaces the bidding stage's payment".
Fix: Replace "Agreements are binding." with "An agreed flow is a staked promise under \cref{sec:commitment}; we assume $P^*\le\bar m_U$ and $\omega\le\lambda_C\bar m_C$ per period, so every agreement and China's exit offer are honoured." Add "$P^*\le\bar m_U$" to the hypotheses of \cref{prop:master}. Replace the first anchored sentence with "China's credible offer $\omega$, and hence $Q$, is fixed and is open to Europe as an exit option throughout."

**5. "The transfer is inefficient" is false with the investment option, and $r^c$ is not destroyed on the path.** Files 06_control.tex, 01_intro.tex.
Anchors: "When $v_c=0$, the transfer is inefficient." and "Washington pays $\sigma+r^c+\iota$ in joint surplus" (06); "an accepted transfer is inefficient in the way preventive war is" (01).
Problem: With $\bar I>0$ the transfer can raise joint surplus: in the paper's own example after Corollary 3, the transfer spares Europe $K=2$ at sovereignty cost $\sigma=1$. And by Corollary 3(d)(i), China does not punish a completed transfer on the path unless punishment is self-rewarding, so $r^c$ is not part of the deadweight loss on the path.
Fix: "When $v_c=0$ and Europe has no investment option, the transfer is inefficient. The rents it avoids are transfers between Washington and Europe, while the sovereignty cost and the issuing cost are destroyed (China's punishment is destroyed too when it is self-rewarding, \cref{cor:control}(d)). With an investment option the transfer can be efficient, because it spares Europe an investment it would sink only to secure rents; this is the one place where the logic of \citet{grossman1986costs} operates in our model." Intro: "When Washington places little value on control and Europe has no autonomy investment to forgo, an accepted transfer is inefficient in the way preventive war is."

**6. The example attached to Proposition 4(d) is false and reverses the reading of the silicon shield.** Files 04_model.tex, 05_slack.tex.
Anchors: "(for example when Washington would almost surely defend a loyal Europe)" (04); "for example when Washington would almost surely defend a loyal Europe, and it is then nonincreasing" (05, Prop 4(d)); "In the case the proposition singles out, where Washington would almost surely defend a loyal Europe" (05); "That pattern is what part (d) implies when the density of crisis costs is decreasing" (05).
Problem: $G(s_A)\approx1$ does not make $g$ nonincreasing on $[s_X-\bar m_U,s_X+s_L]$. When a staked abandonment makes defence of an exiter unlikely, $s_X-\bar m_U$ lies in the left tail, where $g$ is rising, and $\bar\kappa$ rises with $s_X$. The appendix's own example (standard normal, $s_X=0$, $s_L=1$, $\bar m_U=2$: defence of a loyal Europe 84 percent, of an exiter 2 percent) has $\bar\kappa$ rising with $s_X$. The correct sufficient condition, already in the appendix proof, is a unimodal $G$ with mode at or below $s_X-\bar m_U$. The substantive reading flips: the silicon shield lowers maximal conditionality when Washington would probably defend even an exiter, and can raise it in the case the paper treats as typical.
Fix: In Prop 4(d) replace the example with "for example when $G$ is unimodal with its mode at or below $s_X-\bar m_U$, that is, when the most likely crisis costs lie below Washington's net stake in a Europe that has exited". Replace the discussion sentence with "Where the most likely crisis costs lie below Washington's net stake in an exiter, a higher $s_X$ lowers the most conditionality Washington can create. Where a staked abandonment makes defence of an exiter unlikely, the sign can reverse, and holding the chokepoint can make the guarantee more conditional." Qualify the Blankenship sentence the same way. In Section 4.3 delete the derivative sentence and keep a pointer (see cut C2).

**7. Cut the main text from 18 formal statements to about 10.** Files 05_slack.tex, 06_control.tex, 07_decide.tex.
Anchors: "\subsection{Private sovereignty costs and breakdown}"; "\begin{lemma}[Spent and self-limiting cuts]"; "\begin{proposition}[Pain and rupture]"; "The result depends on the stock buffer and on the timing."
Problem: Lemma 1, Prop 1, Cor 1, Prop 2, Cor 2, Prop 3, Prop 4, Prop 5, Cor 3, Lemma 2, Cor 4, Remark 1, Prop 6, Remarks 2 to 4, Prop 7 and Cor 5 are all stated formally in the text. Referee 1's complaint that the paper does too much still applies, and the word budgets cannot be met otherwise.
Fix: Keep formal in the text: Lemma 1 (parts (i) and (iii) can move), Prop 1, Cor 1 (parts (a), (c), (e) and nesting), Prop 2 (parts (a) to (c); state (d) informally with the $n\bmod(b+1)$ example), Cor 2, Prop 3 (state (a)(iii), (a)(v) and (b); move (a)(i), (ii), (iv) to the appendix), Prop 4 ($\kappa^*$, (b), (c)(i), (d); move (c)(ii) to (iv)), Prop 5, Cor 3 (parts (a) to (c); state (d) informally), Cor 4. Move to the appendix with informal text: Lemma 2, Remark 1 (keep (a), (c), (d) in prose), Prop 6, Remarks 2 to 4, and the regularity conditions and stopping formula of Prop 7 (state $P^*=\psi M+(1-\psi)N$ when exit does not bind, and Cor 5(i) with variant (b)). Replacement text for each move is in the cuts list below.

### Important

**8. The prediction that separates the model from cost minimization rests on a cost minimizer that ignores rent.** Files 05_slack.tex, 08_evidence.tex.
Anchors: "Holding the costs of instruments fixed, that account predicts no change" (05); "Cost minimization implies no such change" and "Cheapest credible instrument, unchanged as $Q$ moves" (08).
Problem: In Prop 3(b) linkage becomes costly as $Q\to0$ because Washington must pay the rent $\pos{y_H-\Lambda}$. A cost minimizer that counts that rent as the cost of linkage predicts the same switch. The separation holds only against a coercer with fixed, separately priced instrument costs, which should be said. Three implications survive against any cost minimizer that prices instruments one demand at a time: conditional bites are not additive, so demands in different issue areas crowd each other out within a period (Prop 2(c)(i), Cor 2); adding a demand can reduce what the patron obtains (Prop 2(d)); and a stronger rival bid is answered with more conditionality and no payment (Prop 4(c)(i)).
Fix: Define the rival in Section 8.1: "a coercer that prices each demand at a fixed cost of the cheapest credible instrument, one demand at a time". Lead the discussion after tab:implications with the cross-issue row: "The third row discriminates most. Under cost minimization the instruments used on one demand do not change the price of another; in our model a concession on tariffs leaves less to extract on servicing, because conditional bites share one budget." Change the table cell to "Instruments priced separately at fixed cost; linkage shifts only if its cost is defined to include rent".

**9. The "linkage fades" prediction needs $w_H<y_H$.** File 05_slack.tex.
Anchor: "So linkage against hedging should appear when the ally has slack and fade as its premium approaches zero".
Problem: By Prop 3(b), Washington keeps using linkage at $Q\to0$ whenever $w_H\ge y_H$; it then pays the rent. Linkage fades only for hedges worth less to Washington than to Europe.
Fix: "So linkage against a hedge worth less to Washington than to Europe ($w_H<y_H$) should appear when the ally has slack and fade as its premium approaches zero".

**10. "No payment" identifies $\lambda\beta\approx0$, not $Q\le0$.** File 08_evidence.tex.
Anchors: "If talks carry no risk of rupture, or Washington makes the offers"; "Holder is paid only if $Q>0$, or if talks risk rupture and it has agenda power".
Problem: For ASML $V$ is large, so with any $\lambda>0$ and $\beta>0$, Corollary 1(c) gives a positive transfer unless $Q<-\beta V/(1-\beta)$. The absence of payments is therefore evidence on rupture risk and agenda power at least as much as on the premium, and since $P^*\to\pos{Q}$ continuously as $\lambda\to0$, a small payment cannot be told apart from none.
Fix: Add after the first anchored sentence: "Because $V$ is large for ASML, any rupture risk combined with Dutch agenda power would imply a positive transfer unless $Q<-\beta V/(1-\beta)$. Reading the record as $Q\le0$ therefore assumes that The Hague could not make demands whose rejection risked realignment, an assumption the record of voice without exit supports but does not test."

**11. The "rationing" reading of the Dutch sequence conflicts with coding the sales controls as flow jurisdiction.** File 08_evidence.tex.
Anchor: "We read this as rationing: Washington spent Europe's slack first on the sales controls it valued most".
Problem: tab:cases codes the instrument behind the Dutch steps as flow jurisdiction (zero de minimis, SME FDP rule, MATCH). By Prop 3(b), a credible threat to block the flows directly uses no slack. If that coding is right, the sales controls drew on no slack and the delay on servicing is not rationing. Rationing requires that some steps were backed by conditional linkage, which the paper says it cannot document.
Fix: "If the sales controls were backed by flow jurisdiction, as \cref{tab:cases} codes them, they drew on no slack (\cref{prop:counter}(b)), and the late arrival of servicing controls reflects the cost of the flow threat, not rationing. Rationing would require that some steps were backed by conditional linkage, which we have not found."

**12. Preventive demand for binding versus control.** File 06_control.tex.
Anchors: "Europe could try to remove the commitment problem itself."; "No other period-1 demand draws on the same bite".
Problem: With $v_c=0$ Washington gains from control only by removing rents. A Europe bound with $\Delta_b=\infty$ removes the same rents. Washington could therefore demand binding (Europeanized or treaty-entrenched controls) at sovereignty cost $\sigma^b$, and would prefer that demand whenever $\sigma^b+r^b<\sigma+r^c$ and $v_c$ is small. Remark 1 treats binding only as Europe's unilateral pre-emption. This matters for the evidence: the 2024 and 2025 steps may be the outcome of a preventive demand met by binding. Separately, the intro says every demand, control included, competes for one budget, while Prop 5 gives the control demand the whole budget.
Fix: Add after Remark 1(d): "Washington can also demand binding itself. \Cref{prop:control} prices that demand with $(\Delta_b,\sigma^b,r^b)$ in place of $(\Delta_c,\sigma,r^c)$ and $v_c=0$, so when Washington values control little for its own sake it prefers a demand for binding whenever $\sigma^b+r^b<\sigma+r^c$. A preventive demand need not be a demand for ownership." After the anchored assumption add: "With other demands in the same period, control enters \cref{cor:rationing} as a sunk demand."

**13. Proposition 2(d) applies only when the stake cap is small.** File 05_slack.tex.
Anchor: "Washington can buy the commitment with a staked promise to make no further demand in the period".
Problem: Stakes are free (Section 4.2). Washington can therefore commit to a single ultimatum whenever $\bar m_U$ exceeds the value of further extraction, and the assurance shortfall of part (d) disappears. The offsets reading in tab:cases ("repeated renegotiation, Prop 2(d)") relies on this condition failing.
Fix: Add to the statement of part (d): "This requires that $\bar m_U$ be smaller than the value to the United States of the demands it would make after a concession." In the text: "Under our commitment technology this is free whenever $\bar m_U$ exceeds the value of further extraction, so part (d) describes a patron whose stakes are small relative to its later demands."

**14. Executed threats in the evidence need an on-path mechanism.** File 05_slack.tex.
Anchor: "It punished an act, so in the model it is an executed threat".
Problem: Under complete information a threat that deters is never executed. Executed threats occur on the path only when an instrument is burned as a commitment device (the footnote to Prop 2) or under incomplete information. The Germany withdrawal had no prior public demand, so it is outside the demand-and-threat structure.
Fix: "It punished an act for which there was no prior demand, so it lies outside our demand-and-threat structure. If it is read as the execution of an implicit threat, \cref{prop:counter}(b) says what execution does: it spends the instrument and raises the target's premium. Why it was executed at all requires either the burning logic of the footnote to \cref{prop:slack} or incomplete information."

**15. Proposition 4's assumptions on $\nu$ are buried.** File 05_slack.tex.
Anchor: "Washington converts slack into concessions worth".
Problem: The objective uses a constant value $\nu\le1$ per unit of slack. Concavity of $\Pi$, and hence the formula for $\kappa^*$, needs $\nu\le1$. The knapsack of Cor 2 gives a concave, piecewise-linear value of capacity, not a constant, and $\nu\le1$ says concessions are worth less to Washington than they cost Europe. Parts (a) and (b) then follow almost from the objective; the substance is in (c)(i) and (d).
Fix: Add: "Linearity is a simplification of the concave value of capacity in \cref{cor:rationing}, and $\nu\le 1$ says that a concession is worth less to Washington than it costs Europe, which keeps $\Pi$ concave. With $\nu>1$ Washington would buy such concessions with rent and would not need slack."

**16. Grossman-Hart positioning.** File 03_literature.tex.
Anchor: "Control rights come from the theory of the firm".
Problem: The model's control is a commitment device that lowers the holder's future exit premium by $\Delta_c$, not an allocation of residual rights that shapes relationship-specific investment. Citing Grossman and Hart as the source of the mechanism invites a referee to look for an investment-incentive effect, and the only one (Cor 3(b)) cuts against the inefficiency claim.
Fix: After the first sentence of that paragraph add: "In our model control matters through a different channel. It removes the holder's future outside option, as in \citet{fearon1996bargaining}, and its one investment effect is that a transfer spares the holder an investment made only to raise its rents (\cref{cor:control}(b))."

**17. Intro overclaims the cap on the control demand.** File 01_intro.tex.
Anchor: "We show that a patron's power to demand control is capped by the holder's current slack".
Problem: Only the conditional part of the bite is capped. Unconditional parts, the value of control and the investment effect (the zero-bite purchase) all permit a demand without slack.
Fix: "We show that the conditional part of a patron's coercive power to demand control is capped by the holder's current slack, so a coerced demand comes in windows while that slack lasts".

### Minor

**18.** 04_model.tex, anchor "and that weak dominance selects the price $\pos{Q}$". The appendix proves weak dominance in the clock auction and the price $\pos{Q}$, within one grid step, in the alternating game when the losing bidder raises whenever indifferent. Fix: "and that the price is $\pos{Q}$, up to one grid step, when a losing bidder raises whenever it is indifferent".

**19.** 05_slack.tex, anchor "Europe's loss then equals $B(J^c)$ if the United States has a divisible sunk demand of positive value and sufficient size." Fix: replace "and sufficient size" with "of size at least $B(J^c)$".

**20.** 05_slack.tex, anchor "(In every equilibrium if $e(\{j\})>0$ for every $j$; in some equilibrium otherwise.)". The proof needs $e(J)>0$ for every nonempty $J$. Fix: "(In every equilibrium if $e(J)>0$ for every nonempty $J$, as with additive execution costs; in some equilibrium otherwise.)"

**21.** 06_control.tex, anchor "For uniform $F$, $s^*=(\tilde b+v_c+e)/2$." Fix: "For uniform $F$, $s^*=\min\{(\tilde b+v_c+e)/2,\ \bar\sigma\}$." (Moves to the appendix with Prop 6 in any case.)

**22.** 07_decide.tex, anchor "\item The decision is time consistent." Part (iii)'s "if and only if" holds where exit never binds. Fix: add "When exit does not bind," at the start of the item.

**23.** Notation. $\varphi$ (self-harm, Section 4.3) and $\phi_U$ (in-kind cost, footnote to Lemma 1) are easily confused; rename $\phi_U$ to $a_U$. main.tex: set `\anonymoustrue` and drop the AI-assistance footnote from the submission build (Referee 1 smaller points).

**24.** 00_abstract.tex, anchor "We verify each result by brute-force computation." Proofs prove; the numerics check. The sentence is a methods detail. Cut it (and "Every threat is sequentially rational", which is a modelling assumption better stated in the introduction).

## Cuts, merges and moves (to reach about 19,000 words)

Raw word counts (wc, LaTeX included) and targets: intro 1,885 to 1,600; background 1,704 to 1,100; literature 1,750 to 1,400; model 3,883 to 3,000; slack 4,256 to 3,000; control 4,625 to 3,000; who decides 3,749 to 2,400; evidence 4,452 to 3,000; implications 1,456 to 1,000; conclusion 489 to 450.

**Model (save about 900).**
- C1. Cut the paragraph "\paragraph{Chinese punishment of alignment.}" to one sentence: "We set China's untargeted punishment of alignment to zero; Chinese coercion enters as counter-threats on particular concessions (\cref{prop:counter}) and on a transfer of control (\cref{sec:control})." The justification already appears at "We do not let China punish alignment as such." in Section 5.2; keep it there only.
- C2. Delete "By \cref{prop:conditionality}(d), $d\bar\kappa/ds_X..." through "it can rise otherwise." in "Access and the silicon shield"; replace with "\Cref{prop:conditionality}(d) gives the sign." (Removes the third statement of the same derivative.)
- C3. Delete the paragraph beginning "The master game nests the protocols one might propose." The nesting line in Cor 1 covers it. Keep its last two sentences (the Europe 2031 corner) as a single sentence after the corollary.
- C4. Compress the posture and AI paragraphs (keep the definitions of $d_p$, $d_{ai}$ and the rescission as evidence that tiering loyal allies is costly; the Diffusion Rule tiers are already in Section 2).

**Slack (save about 1,250).**
- C5. Cut "\paragraph{What is new here.}" to two sentences: "The slack and the participation constraint are \citeauthor{clayton2026putting}'s. Our additions are that only conditional parts are capped by slack, that conditional bites share one budget, and that a coercer that cannot commit to stop demanding obtains less (part (d)) \citep{pauly2024damned}." The comparison with CMS stays in Section 3.3.
- C6. Move the burning footnote and the counter-threat numerical example (paragraph after Prop 3, from "A numerical case shows" to "Europe's loss rises from $1.8$ to $1.9$.") to the appendix proofs, where both already appear.
- C7. Delete the paragraph "The assurance literature supplies the cost side of the proposition." (Pauly, Gerzhoy and Lanoszka are in Section 3.2; keep the Blankenship sentence, corrected per finding 6, as one sentence after part (d)).
- C8. Move the paragraph "Two kinds of US drawdown have opposite places in the model." to Section 8.3, corrected per finding 14, or cut it to two sentences.
- C9. Move Prop 4(c)(ii) to (iv) to the appendix; keep (c)(i) in the statement and one sentence: "Where assurance is already costly at the margin, or Washington is already spending slack, Washington pays for China's bid in rent or in forgone concessions (\cref{app:proofs})."

**Control (save about 1,600).**
- C10. Move Section 6.5 "Private sovereignty costs and breakdown" (Prop 6 and both paragraphs) to the appendix. Replacement paragraph in Section 6.2: "Under complete information an ultimatum is accepted or never issued. If Europe's sovereignty cost is private, a threat-backed ultimatum is refused with positive probability. Refusal is more likely when China's punishment of a transfer is large, when Europe's future premium is high and when the threat is cheap for Washington to carry out, the risk-return trade-off of \citet{fearon1995rationalist} (\cref{prop:breakdown} in \cref{app:proofs})."
- C11. Move Lemma 2 to the appendix. Replacement: "Cuts over several dates add up date by date, and extending a purely conditional cut into a date at which Europe's premium is positive adds nothing to its bite, so a threat of permanent exclusion bites no more than a threat to exclude Europe while its premium is negative (\cref{lem:selflimit})."
- C12. Delete "Of the 20,199 simulated games with an ultimatum in \cref{app:numerics}, 1,202 issued it at a date that was not itself eligible." It is in Appendix B.
- C13. Compress the paragraph "We read the European steps of 2024 and 2025" to three sentences; the facts are in Section 2 and the coding of Supplement No. 4 is in Section 8.2.
- C14. Move Remark 1(b) (Europe's payoff comparison) to the appendix; keep (a), (c), (d) and the new sentence of finding 12.

**Who decides (save about 1,350).**
- C15. Move tab:council, the paragraph "Informal norms and procedural defaults pull the outcome away from the formal arithmetic", and the paragraph "The same arithmetic applies to the Council vote in \emph{Europe 2031}." to the appendix (the last to Appendix C). Keep Remark 4 in prose: "With enforceable vote-contingent payments and no rival bidder, Washington defeats an Anti-Coercion Instrument determination by buying the cheapest blocking minority, and members with no gain from the measure join it for free. The six frontline states cannot block; thirteen eastern and Nordic members can, by number. Every later stage of either route needs a coalition at least as large, so Washington buys its block before the determination (\cref{rem:council})."
- C16. State Remarks 2 and 3 in prose and move the formal versions to the appendix. Compress the Bank Melli paragraph to one sentence.
- C17. Move the paragraph "The other parameters are poorly measured." (buffer, TSMC revenue, multipliers) to Appendix B or a new short appendix; keep one sentence: "On our rough numbers, interruption pays only if Washington can compel less than about 85 percent of the servicing at stake, and $h$ is the parameter with the least evidence behind it."
- C18. Keep Prop 7 as an informal statement plus Cor 5(i) and variant (b) (the institutional result). Move parts (ii) and (iii) of Cor 5 and variants (a) and (c) to the appendix.

**Evidence (save about 1,450).**
- C19. Move the three historical rows of tab:cases (offsets, United Kingdom 1957, Brazil deal) and the paragraph "\paragraph{Where the comparison strains the model.}" to an appendix; keep one sentence in the text noting that the offsets are the one documented case of security linkage extracting sunk payments.
- C20. Cut the paragraph "China's share of ASML's system sales rose" (it reports a fact the model does not address).
- C21. Compress "\paragraph{An elite survey experiment.}" and delete the near-duplicate conclusion paragraph "How conditional the guarantee is can be measured."
- C22. Compress the Nexperia narrative by about 200 words (dates of the June meetings can go to a footnote).

**Literature (save about 350).** Cut the nonproliferation sentences (Kroenig, Gray, Miller, Coe) to one; cut Leeds and Fang; compress "These works disagree" to two sentences; cut the repeated note that Fearon (1996) is unpublished (it is said twice in Section 3.4 and again in Section 6.2; keep one).

**Introduction (save about 300).** Cut contribution item 1 to its last sentence (the CMS contrast is in Section 3.3). Merge the two results paragraphs ("In the game of \cref{sec:model}..." and "\Cref{sec:control} shows...") into one of about 200 words.

**Background (save about 600).** Move the EU001 and Council material from "Under Article 12(2) of the EU dual-use regulation" into Section 7 and keep two sentences here. Cut "The controls themselves arrived in steps" to the dates not already given in the introduction's second paragraph. Shorten the Decree 834/835 and Nuctech sentences.

**Implications and conclusion (save about 500).** Delete "\subsection{Lessons for Washington}" (it restates Props 2 and 4). Keep the information limitation once: either "The limitation we would worry about most is information." in the conclusion or the Limitations subsection, not both. Compress "\paragraph{Chinese counter-threats.}" to three sentences.

## Is the slack principle motivated and illustrated well?

Yes, with one gap. The section opens with the right question (what can a patron obtain from an ally whose premium is negative), the reversible/sunk distinction is intuitive, and fig:slack panel (b) is the clearest single illustration in the paper of why conditional bites do not add. The gap is that the illustration and the theorem live in the bidding benchmark, which the reader has just been told is the corner in which $V$ is irrelevant (finding 2). With the $\Lambda_\psi$ generalization the section would also connect back to the master game. The assurance result (part (d)) is the most surprising implication and deserves the one-line example in the text ($b+1$ identical demands yield none), while the general statement can move.

## Are the master game and hold-up proposition presented clearly?

Proposition 1 is clear and correct, and the explanation of why $V$ drops out is right. Two fixes: the commitment inconsistency and the description of how the bidding stage feeds the bargaining (finding 4). The order-of-limits caveat (the formula describes bargaining in which US proposals arrive much faster than rupture and discounting) is buried in Appendix A; one clause after the proposition would help. Proposition 7 is correct as far as I checked but is presented at appendix level of generality in the main text (sup over stopping times, piecewise uniform continuity). The reader needs $P^*=\psi M+(1-\psi)N$ when exit does not bind and Corollary 5's timing result; the rest can move (C18).

## Do the empirical implications follow from the model and separate it from cost minimization?

They follow from the model, with the corrections in findings 9 to 11. The separation from cost minimization is weaker than claimed (finding 8). The strongest discriminating implications are the cross-issue budget (a concession in one domain lowers what can be extracted in another within the same period), the response to a stronger rival bid (more conditionality, no payment), and the timing of control demands (while the holder is weak and expected to strengthen, and as demands for binding as often as for ownership, per finding 12). The event-dataset design in Section 8.5 should be organized around the first of these.
