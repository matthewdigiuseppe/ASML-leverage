# v2 resolutions: final statements, notation, labels (binding for all drafters)

This file overrides notes/model_design_v2.md wherever they differ. Proofs and exact LaTeX for each result are in the verification reports notes/v2/verify_m1.md ... verify_m4.md ("Final statement" and "Proof" blocks). Drafters must use the statements below (or the verified blocks they point to) without changing their content. Change only notation as listed in Section 1 and wording needed for flow.

## 1. Notation (final; overrides the reports)

| Symbol | Meaning | Note |
|---|---|---|
| $E$, $U$, $C$ | Europe (holder), United States (patron), China (rival) | prose: Europe, Washington or the United States, Beijing or China |
| $a\in\{A,X\}$ | alignment: Atlantic or exit | Exit $X$: Europe lets ASML sell and service EUV and advanced immersion DUV tools for Chinese fabs against US objection (broad realignment of the chokepoint). Hedging = legacy-tool sales and servicing (a secondary choice). |
| $\bar m_U,\bar m_C$ | largest stake a power can attach to one public conditional commitment | unified commitment technology; one stake per commitment, not a shared budget |
| $W_C=(1-\theta)W+\rho V$ | most China would pay for exit | $\rho\ge0$ relative-gains weight; $\theta$ share blocked by US flow jurisdiction |
| $\omega=\lambda_C\min\{W_C,\bar m_C\}$ | China's credible offer in European utility | $\lambda_C\in(0,1]$: Europe's valuation of a unit of China's in-kind promise; China's cost of a promise $\tau_C$ is $\tau_C$ |
| $d_j$ | conditional part of instrument $j$ | $d_j=v_j(x_j(A))-v_j(x_j(X))$ |
| $\kappa$, $S_k$ | conditionality of the core guarantee; Europe's crisis-weighted stake in core defence | $\kappa=G(s_A)-G(s_X-m_S)$, $s_A=s_X+s_L$, $s_X=s_0+s_B$ |
| $d_p$, $d_{ai}$, $d_f=\chi_f f$ | posture/enablers; frontier AI access; firm-level penalties | $\chi_f=\mathbf 1\{\varphi V\le\gamma+\bar m_U\}$ |
| $c=\kappa S_k+d_p+d_{ai}+d_f+\eta$ | credible cost of exit | $\eta\ge0$ intrinsic cost |
| $Q=\omega-c$ | exit premium | |
| $\Lambda=\pos{-Q}$ | slack | credit the term "slack" to Clayton, Maggiori and Schreger (key clayton2026putting, and clayton2026framework) |
| $\beta\in[0,1)$ | Europe's probability of proposing | |
| $\lambda$, $r$ | breakdown (rupture) hazard; discount rate | |
| $\psi=\lambda/(\lambda+r)$ | **rupture weight** | replaces $\omega_b$ in verify_m1/m2. Discrete analogue $\psi_\Delta=\mu/(1-\upsilon)$ with $\upsilon=\delta(1-\mu)=e^{-(r+\lambda)\Delta}$ (replaces $k$ and $\omega_\Delta$ in verify_m1) |
| $P^*$ | equilibrium transfer flow from Washington to Europe (negative: European concession) | "leverage" means $\pos{P^*}$ or, in the bidding benchmark, $\pos{Q}$ |
| $u(J)$, $d(J)$, $B(J)$, $J^c$ | unconditional part, conditional part, bite of threat set $J$; credible set | $B(J)=u(J)+\min\{d(J),\Lambda\}$ |
| $t_k$, $w_k$, $T_{\mathrm r}$, $T_{\mathrm s}$, $W(S)$ | demand cost to Europe, value to Washington, reversible and sunk totals, value of set $S$ | |
| $r_k$, $\bar r_k$, $e^C_k$, $z_k$ | China's counter-threat on concession $k$, its cap, China's execution cost, China's loss from $k$ | |
| $y_H$, $w_H$, $e_F$ | value of a hedge to Europe, its value to Washington, net ex post cost of flow jurisdiction | |
| $H(\kappa)$, $\nu$, $Q_0$, $\kappa_0$, $\bar\kappa$ | assurance cost of conditionality; Washington's value per unit of slack converted (was $w$); premium at $\kappa_0$; least and largest conditionality | $\kappa_z=\kappa_0+Q_0/S_k$; $\kappa_x=\inf\{\kappa\ge\kappa_0:H'(\kappa)\ge x\}$; $\kappa_1=\kappa_{S_k}$, $\kappa_\nu=\kappa_{\nu S_k}$ |
| $v_c$, $\iota$, $\Delta_c$, $\sigma$, $r^c$ | intrinsic value of control to Washington; **issuing cost** (was $k$); enforceability; sovereignty cost; China's punishment of a transfer | |
| $\bar I$, $K$ | premium increase from Europe's autonomy investment; its cost | was $\bar I$, $K_I$ |
| $\Delta R_U$, $\Delta R_H$, $\Gamma$, $T^*$, $B_1$ | rents control removes (US side, holder side), US gain from an ultimatum, payment, bite | |
| $F$, $f$, $\bar\sigma$, $\hat s$, $s^*$, $\tilde b=B_1-r^c$, $R=\delta\pos{Q_2}$, $e$ | breakdown proposition | |
| $c_E(t)$, $c_U(t)$, $\hat C_i(t)$, $N(t)=\beta\hat C_U(t)-(1-\beta)\hat C_E(t)$, $x^\circ(t)=\psi M+(1-\psi)N(t)$, $M=Q+\beta(V-Q)$, $\bar Q$ | hold-up | $N$ replaces $G(t)$ and $x^\circ$ replaces $x_F$ in verify_m2; write $r+\lambda$ instead of $\rho$ |
| $\ell$, $c_S$, $h$, $t_U$, $D$, $\bar t$ | interruption: Europe's own flow cost; US flow cost of interrupted servicing; share of US-fab servicing Washington can compel; US buffer (stock); gain term; threshold | |
| $Q_{NL}$, $x_h$ | gatekeeper's premium; targeted benefit | |
| $y$, $f^F$, $p_C$, $p_B$, $\zeta$ | firm's China profit, credible US penalty on the firm, Chinese penalty for compliance with US measures (Decree 835), EU Blocking Statute penalty, cost of compulsion | |
| $q_i$, $\mathcal B$, $\Phi(0)$ | member $i$'s net gain from an anti-US countermeasure; blocking family; cost of buying a blocking minority | |

Macro: `\pos{x}` = $[x]^+$ (defined in preamble). Do not use $\omega_b$, $k$ (except as an index), $G(t)$, $x_F$, $\rho$ for $r+\lambda$, $w$ for the per-unit value, $K_I$.

Terminology (use exactly these words): "exit premium" ($Q$); "slack" ($\Lambda$); "bite" ($B$); "conditionality" ($\kappa$ or the conditional parts $d_j$); "rupture weight" ($\psi$); "leverage" = the transfer Europe obtains for its chokepoint ($\pos{P^*}$; $\pos{Q}$ in the bidding benchmark); "concession" = what Europe gives up. Never use "leverage" for Washington's power or for Europe's share in a hold-up. The channels through which $V$ (Washington's dependence on the chokepoint) affects outcomes are named exactly: (1) **agenda power under rupture risk** ($\beta\psi$), (2) **the rival's valuation** ($\rho V$ in $W_C$ when China's cap does not bind), (3) **self-harming sanctions** ($\chi_f$), (4) **the silicon shield** ($V$ raising $s_X$, sign depends on the density of crisis costs), (5) **hold-up** (Europe's power to impose pain during a dispute). "Instrument" (not lever/linkage) for a patron's tool; "the AI instrument" for frontier AI access.

## 2. Results, labels and sources

Section 4 (sec:model). Subsections: sec:setup, sec:commitment, sec:security, sec:bidding, sec:master.
- **Lemma 1** `lem:bidding` (Bidding benchmark): verify_m1.md Lemma 1 block, verbatim modulo notation. Put the alternating-raise remark in the appendix proof. Credit: Groseclose and Snyder 1996 (one-voter case), Dekel, Jackson and Wolinsky 2008 Prop. 2 (English auction in undominated strategies), Bernheim and Whinston 1986, Bueno de Mesquita and Smith 2016; the CMS framework supplement B.2 two-hegemon Bertrand result.
- **Proposition 1** `prop:master` (Bargaining with an outside option and rupture risk): verify_m1.md Prop 1 block, with $\psi,\psi_\Delta,\upsilon$. Discrete closed forms may be stated in the appendix only; the main text states (i) payoff uniqueness for every SPE and every $\Delta$, uniqueness and immediate agreement when $\lambda>0$, and (iii) the limit $P^*=\max\{Q,\psi(Q+\beta(V-Q))\}$ with the threshold $\hat Q=\lambda\beta V/(r+\lambda\beta)$. Footnote on alternative exit timing: verify_m1.md "Suggested footnote" (credit Shaked 1994 `shaked1994opting`, Binmore, Shaked and Sutton 1989, Ponsati and Sakovics 1998).
- **Corollary 1** `cor:master` (Threshold and channels): verify_m1.md Corollary 1 block (a)-(e) plus nesting, notation changed. In (e) use the five channel names above.

Section 5 (sec:slack). Subsections: sec:slackprinciple, sec:counter, sec:conditionality.
- **Proposition 2** `prop:slack` (Slack principle): verify_m3.md Prop 2 parts (a), (b), (c)(i)-(iii), and (c)(iv) renamed as part (d) "Assurance". Keep the assumptions sentence. 
- **Corollary 2** `cor:rationing` (Rationing): verify_m3.md Prop 2(d) text.
- **Proposition 3** `prop:counter` (Counter-threats and hedges): part (a) = verify_m3.md Prop 2(e) with its setup; part (b) = Prop 2(f).
- **Proposition 4** `prop:conditionality` (Conditionality is the price of concessions): verify_m3.md Prop 3 final statement, with $w\to\nu$ and $\kappa_w\to\kappa_\nu$. Part (d) as corrected: $d\bar\kappa/ds_X=g(s_X+s_L)-g(s_X-\bar m_U)$; $\bar\kappa$ falls with $s_X$ when the density $g$ of crisis costs is nonincreasing on $[s_X-\bar m_U,s_X+s_L]$ (for example when Washington would almost surely defend a loyal Europe), and can rise otherwise.

Section 6 (sec:control). Subsections: sec:controlsetup, sec:preventive, sec:windows, sec:bind, sec:breakdown.
- **Proposition 5** `prop:control` (Preventive control): verify_m4.md Prop 4 block, with $\iota$ for the issuing cost and $K$ for the investment cost.
- **Corollary 3** `cor:control` (Motive, investment, enforceability, China): merge verify_m4.md corollaries (i), (ii), (iii), (v) as parts (a)-(d). Corollary (iv) (the special case) goes into the text after the proposition and in the appendix. Part on investment includes the zero-bite purchase implication.
- **Lemma 2** `lem:selflimit` (Spent and self-limiting cuts): verify_m4.md lemma block with its scope conditions.
- **Corollary 4** `cor:windows` (Windows): verify_m4.md windows block (note $t'\ge t$; equivalent to $t'>t$ when all unconditional parts are zero, as in Figure fig:windows).
- **Remark 1** `rem:bind` (Self-binding and dual key): verify_m4.md remark block, corrected version.
- **Proposition 6** `prop:breakdown` (Breakdown): verify_m4.md Prop 5 block (threat-backed ultimatum and the purchase option; comparative statics for threat-backed ultimatums hold for every continuous $F$; uniqueness of $s^*$ uses log-concavity).

Section 7 (sec:decide). Subsections: sec:gatekeeper, sec:firm, sec:council, sec:holdup.
- **Remark 2** `rem:gatekeeper`: verify_m2.md Remark G block.
- **Remark 3** `rem:firm`: verify_m2.md Remark F statement (write as a remark with the qualifications: $f^F=\chi_f f$; $p_B>0$ only if US measures were listed in the Blocking Statute annex, which today lists no US export-control law; compulsion used only if $Q-\zeta>0$).
- **Remark 4** `rem:council`: verify_m2.md Remark E block, with the ACI procedure as confirmed in facts_history.md item 4.3 (Council determination by QMV within 8 to 10 weeks; response measures are Commission implementing acts under the examination procedure with a no-opinion clause; in the appeal committee the Commission may adopt unless a qualified majority votes against). Include the population arithmetic table (from verify_m2.md) in the text or appendix.
- **Proposition 7** `prop:pain` (Pain and rupture): verify_m2.md Prop 6 block with $N(t)$, $x^\circ(t)$, $\psi$.
- **Corollary 5** `cor:interrupt` (Interruption): verify_m2.md corollary block. Cite Fernandez and Glazer 1991, Haller and Holden 1990, Busch and Wen 1995 for multiplicity when one side chooses disagreement actions each round; state that we characterize Markov equilibria.

Figures and tables: fig:timing (figures/fig_timing.tex, already written), fig:master (figures/fig_master.pdf), fig:slack (figures/fig_slack.pdf), fig:windows (figures/fig_windows.pdf); tab:notation (Section 4), tab:implications (Section 8: predictions vs rival accounts), tab:cases (Section 8: comparison of cases), tab:scenario (Appendix C), tab:council (Section 7 or Appendix).

Appendices: app:proofs (A_proofs.tex), app:numerics (B_numerics.tex), app:scenario (C_scenario.tex).

## 3. Points every drafter must respect

1. The static threshold is not new: credit the outside-option principle (Binmore, Shaked and Sutton 1989; Shaked and Sutton 1984; Sutton 1986), Groseclose and Snyder 1996, Dekel, Jackson and Wolinsky 2008, Bueno de Mesquita and Smith 2016, Wagner 1988, Hirschman 1945, and the CMS two-hegemon result. Slack as a source of power is CMS's ("Threats generate power to the extent that they generate slack in the participation constraint", clayton2026putting). Our additions: the rival's bid inside the participation constraint; the split of each instrument into conditional and unconditional parts and the result that conditional bites share one budget; sequential rationality of each threat with spent instruments; the coercer's assurance problem; counter-threats that tax the patron; conditionality as the price of concessions; preventive conversion of a wasting slack into control; hold-up through pain and rupture risk.
2. In CMS the pooled threats are enforcement threats that raise the target's inside option; cut-off threats appear only in their Supplement B.3.1 (lit_theory.md). Say this precisely when contrasting.
3. Jehiel, Moldovanu and Stacchetti (1996): with identity-dependent externalities the seller extracts surplus from non-buyers; our agenda-power channel is a binary instance. Harstad (2016): buy versus lease; Wolford and Kim (2017) for self-harming sanctions; Benson and Smith (2023) and Lake (1996), Frieden (1994), Grossman and Hart (1986), Hart and Moore (1990), Cooley and Spruyt (2009) for control rights; Coase (1972), Bulow (1982), Morita and Waldman (2004) for servicing as a renewable lever.
4. The empirical record supports the jurisdictional channel and leaves the security channel largely untested (Referee 2). Say so.
5. No "confirms", "rejects", "cannot fail", "predicts" about the fictional scenario. The scenario is a hook (introduction, one or two paragraphs) and Appendix C.
6. The December 2024 Supplement No. 4 exclusion is coded as a threat left unexercised conditioned on Europe's own capacity to control (BIS: "Governments in those destinations ... have the authority to control key SME items of concern"), equivalently a reward for self-binding, not a transfer (Referee 3; facts_record.md 11.1-11.2).
7. Nexperia is inside the model as a US-backed demand on the Netherlands met by a Chinese counter-threat that was executed and followed by the Dutch suspension of the ministerial order once the US suspended its Affiliates Rule at Busan. Use the Enterprise Chamber record (gerechtshof2025nexperia: the 12 June 2025 Dutch minutes of a meeting with the State Department's ISN bureau, "almost certain the CEO will have to be replaced to qualify for the exemption from the entity list", a Dutch record of US views). Read the executed Chinese export ban as either crowding out (Prop 3(a)(iii)) or Dutch misjudgment of China's resolve (incomplete information, outside the model): say which reading needs what.
8. Only cite keys that exist in paper/refs.bib. Only state facts that appear, sourced, in notes/review/*.md or notes/v2/facts_*.md (or in the v1 sections, which were fact-checked), and cite the corresponding key.
