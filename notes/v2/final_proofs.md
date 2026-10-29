# Final check: formal statements against proofs (tag: proofs)

## Verdict

No essential problems remain. Every formal statement in the main text and in D1_control.tex and D2_decide.tex has a proof in A_proofs.tex with the same assumptions (up to the minor points below), the same part labels and the renamed notation: F' and Pi_U, s_P, Pi_P in the breakdown proposition; r^c, rbar^c, e^C, z_C and r^c_max in Corollary 3(d); a_U in the in-kind footnote; n(t) and n(s) in the hold-up statement and proof. No stale symbols (omega_b, x_F, K_I, G(t), kappa_w, w_b) remain in the paper, and there are no em dashes. Every \cref to a result part points to a part that exists. main.log shows no undefined references.

Remark rem:rupture and its proof agree: the bite formula, the bound u + min{d, Lambda_psi}, equality when Q + d >= Qhat, B_psi = B at lambda = 0, and part (c)(i) with B_psi and Lambda_psi are all proved. Lambda_psi - Lambda = P*(Q) - [Q]^+ holds identically, so the corrected statement ("exceeds Lambda exactly when P*(Q) > [Q]^+") is right; the proof still states the weak version (finding 3). The worked example (Lambda = 1, Lambda_psi = 2.2, bite 1.8, Qhat = 8/3) checks by hand.

Spot-checks: Proposition 4(d) (derivative, unimodal sufficient condition, normal counterexample with G(3) > 0.99 and g(3) > g(-4), and the 0.8186 to 0.8664 example) is correct. Corollary 5 parts (i) to (iii) and variants (a) to (c) are correct, including the bathtub bound and the identity bracket = e^{(r+lambda)t_U} D. The breakdown proposition is correct (cutoff form, log-concavity argument, Topkis argument, all four numerical examples in (e) recomputed), but one "can fail" claim in (e) has no example (finding 1).

Scripts: every script listed in code/checks/README.md exists, and every script named in B_numerics.tex exists. `python3 -I code/checks/v2_rupture_bite.py` prints "draws 13079; violations of B <= u + min(d, Lambda_psi): 0; max |B - (u + min(d, Lambda))| at lambda = 0: 8.88e-16" and "example: Lambda = 1.00, Lambda_psi = 2.20, bite of d = 3: 1.80", as B_numerics.tex and the README state. I also ran the other fourteen v2 scripts. All exit cleanly, each finishes in under 30 seconds when run alone (the slowest, v2_m4_prop5.py, takes 26.7 s), and their counts match B_numerics.tex except the hold-up error figure (finding 6).

## Important

### 1. Breakdown, part (e): one claimed failure direction has no example

- File: paper/sections/D1_control.tex (statement), paper/sections/A_proofs.tex (proof), paper/sections/B_numerics.tex
- Anchor (D1): "The other directions can fail: the refusal probability can rise with $e$ and fall with $R$, and the breakdown probability can rise with $B_1$ and $v_c$ and fall with $r^c$."
- Problem: The statement lists five directions that can fail. The proof ("For the remaining directions, take uniform $F$ on $[0,10]$ ...") gives examples for four of them: refusal rising with e, and breakdown rising with B_1, rising with v_c and falling with r^c. Nothing shows that the refusal probability can fall with R. The claim is true. A switch from the purchase offer to the threat needs the constraint s >= b~ - R to bind at low R, and I found and checked such a case. The brute-force script also finds R violations of refusal monotonicity in the truncated normal and truncated exponential families (one draw each).
- Replacement (A_proofs.tex, append after "Raising $r^c$ from $0$ to $2$ (with $B_1=e=1$, $v_c=10$) moves it from the threat (breakdown probability $0.4$) to the purchase offer ($0$)."): "Raising $R$ from $0$ to $2$ (with $B_1=5$, $e=1$, $v_c=1$, $r^c=0$) moves it from the purchase offer (refusal probability $0.95$) to the threat (refusal probability $0.65$). At $R=0$ the constraint $s\ge\tilde b-R=5$ binds and $\Pi_B=0<\Pi_P=0.025$. At $R=2$ the cutoff is $s^*=3.5$ and $\Pi_B=0.225$."
- Replacement (B_numerics.tex, anchor "and the four examples in the proof are reproduced"): "the examples in the proof for $e$, $B_1$, $v_c$ and $r^c$ are reproduced, and the refusal probability falls with $R$ in two draws (truncated normal and truncated exponential)".

### 2. Interruption: the text misstates when interruption helps

- File: paper/sections/07_decide.tex and paper/sections/09_implications.tex
- Anchor (07): "Interruption therefore helps only under a rule fixed before offers and kept in force for the dispute."
- Anchor (09): "Interruption raises Europe's transfer only if the US buffer is short, only for servicing Washington cannot compel, and only under a rule fixed before offers and kept in force for the dispute (\cref{cor:interrupt})."
- Problem: Variant (c), proved in A_proofs.tex, has Europe choose after the proposer is drawn but before offers. Europe then interrupts only in the rounds in which it proposes, and its gain is positive for every finite t_U, whatever ell is. Interruption therefore helps without a rule "kept in force for the dispute" and without a short buffer. What every helpful timing shares, and what variant (b) lacks, is a choice made before offers that cannot be revised after an offer is rejected. The 09 sentence also states the short-buffer condition, which holds only under the timing of the corollary itself, as if it held for all timings.
- Replacement (07): "Interruption therefore helps only if Europe makes the choice before offers in each round and cannot revise it after an offer is rejected."
- Replacement (09): "Under the timing of \cref{cor:interrupt}, interruption raises Europe's transfer only if the US buffer is short and only for servicing Washington cannot compel. Under every timing we consider, it helps only if Europe chooses before offers and cannot revise the choice after an offer is rejected (\cref{cor:interrupt})."

## Minor

### 3. rem:rupture proof proves the weak comparison, the statement the strict one

- File: paper/sections/A_proofs.tex
- Anchor: "So $\Lambda_\psi\ge\Lambda$ exactly when Europe's bargaining payoff is at least its bidding payment, which, because $P^*(Q)\ge Q$, is the case whenever $P^*(Q)\ge 0$."
- Problem: The remark says Lambda_psi exceeds Lambda exactly when P*(Q) > [Q]^+. The proof states the weak version. Both follow from the identity on the line above, but the proof should state what the remark states.
- Replacement: "So $\Lambda_\psi>\Lambda$ exactly when $P^*(Q)>\pos{Q}$, that is, when $\psi(Q+\beta(V-Q))>\max\{Q,0\}$, so that Europe's bargaining payoff exceeds its bidding payment."

### 4. rem:rupture statement omits two conditions its proof uses

- File: paper/sections/05_slack.tex
- Anchor: "Suppose Europe's payoff from alignment is the bargaining outcome $P^*(Q)$ of \cref{prop:master} rather than the bidding payment $\pos{Q}$."
- Problem: The proof assumes that the premium stays below V after every withdrawal, so that Proposition 1 applies. The script also draws only Q + d < V. The equality claim uses Qhat, which Proposition 1(iii) defines only for r > 0, and the proof adds "If $r>0$". Neither condition appears in the statement.
- Replacement: "Suppose Europe's payoff from alignment is the bargaining outcome $P^*(Q)$ of \cref{prop:master} rather than the bidding payment $\pos{Q}$, and that Europe's premium stays below $V$ after every withdrawal." In the same remark, replace "($Q+d(J)\ge\hat Q$)" with "($r>0$ and $Q+d(J)\ge\hat Q$)".

### 5. Script docstring repeats the superseded claim Lambda_psi >= Lambda

- File: code/checks/v2_rupture_bite.py
- Anchor: "Checks: (1) B <= u + min{d, Lambda_psi}, Lambda_psi = P*(Q) - Q >= Lambda = [-Q]^+;"
- Problem: This is false when lambda > 0, Q < 0 and Q + beta(V - Q) < 0. For example, Q = -5, V = 1, beta = 0.5, lambda = r = 1 gives P* = -1, Lambda_psi = 4 and Lambda = 5. The corrected remark and its proof say this case exists. The code itself does not test the claim.
- Replacement: "Checks: (1) B <= u + min{d, Lambda_psi}, Lambda_psi = P*(Q) - Q, which exceeds Lambda = [-Q]^+ exactly when P*(Q) > [Q]^+ and is below it when P*(Q) < 0;"

### 6. Hold-up numerics: the stated error covers only part of the no-exit draws

- File: paper/sections/B_numerics.tex
- Anchor: "Where $Q\le\bar Q$, the largest error against $x^\circ(0)$ is $3.1\times10^{-7}$"
- Problem: v2_m2_prop6_holdup.py reports 3.11e-07 only for draws with Q below Qbar by a margin ("mode=below"). In the 1,500 draws with Q exactly at Qbar ("mode=at") the error is 2.10e-04, and in the other no-exit draws it is 8.4e-05 and 5.1e-05. Over all 3,797 draws with Q <= Qbar, the largest error is 2.1e-04.
- Replacement: "Where $Q$ lies below $\bar Q$ by a margin (1,500 draws), the largest error against $x^\circ(0)$ is $3.1\times10^{-7}$; over all 3,797 draws with $Q\le\bar Q$, including 1,500 with $Q=\bar Q$, it is $2.1\times10^{-4}$"

### 7. Proposition 7 regularity condition is weaker than the one the proof uses

- File: paper/sections/07_decide.tex
- Anchor: "that are bounded and piecewise uniformly continuous, with finitely many discontinuities in every bounded interval"
- Problem: The proof ("each interval of unit length contains at most $N_d$ of their discontinuity points, and between discontinuities they are uniformly continuous") uses a uniform bound N_d and one modulus of continuity, and its error sum is built on that bound. The statement only requires finitely many discontinuities in each bounded interval.
- Replacement: "that are bounded, uniformly continuous between discontinuities, and have at most $N_d$ discontinuities in every interval of unit length"

### 8. Gatekeeper remark: the first case should condition on the original premium

- File: paper/sections/D2_decide.tex
- Anchor: "If $Q_{NL}'<V$ and $Q_{NL}'\le\bar m_U$, the United States' payment falls from $\pos{Q_{NL}}$ to $\pos{Q_{NL}-x_h}$"
- Problem: A payment "from $\pos{Q_{NL}}$" exists only if the Netherlands aligns at Q_NL. The proof assumes the conditions of Lemma 1 before and after the benefit. The remark handles Q_NL > min{V, mbar_U} separately.
- Replacement: "If $Q_{NL}<V$ and $Q_{NL}\le\bar m_U$, the United States' payment falls from $\pos{Q_{NL}}$ to $\pos{Q_{NL}-x_h}$"

### 9. Wrong part cited for the direct channel of V

- File: paper/sections/09_implications.tex
- Anchor: "which reaches the transfer directly only through agenda power under rupture risk (\cref{cor:master}(d))"
- Problem: Part (d) gives the derivative. The claim that V enters P* directly only through beta psi V is part (e).
- Replacement: "which reaches the transfer directly only through agenda power under rupture risk (\cref{cor:master}(e))"

### 10. Scope of the cut lemma: wrong inequality for the commitment cap

- File: paper/sections/A_proofs.tex
- Anchor: "(1) If $Q_s+d_s\ge\min\{V_s,\bar m_U\}$, the cut drives Europe out at $s$."
- Problem: By Lemma 1(ii)(a), Europe still aligns when Q_s + d_s = mbar_U < V_s. The lemma's own scope condition is Q_s + d_s <= mbar_U.
- Replacement: "(1) If $Q_s+d_s\ge V_s$ or $Q_s+d_s>\bar m_U$, the cut drives Europe out at $s$."

### 11. Main-text summary of the cut lemma drops one scope condition

- File: paper/sections/06_control.tex
- Anchor: "provided Washington retains Europe throughout (\cref{lem:selflimit} in \cref{app:cuts})"
- Problem: The lemma also requires that the cut not change the premium at any other date. The appendix lead-in says this condition matters (an autonomy investment can lower the bite).
- Replacement: "provided Washington retains Europe throughout and the cut leaves the premium at other dates unchanged (\cref{lem:selflimit} in \cref{app:cuts})"

### 12. z_C still has two meanings in the appendix

- File: paper/sections/A_proofs.tex (proof of lem:bidding)
- Anchor: "Fix China's drop level $z_C$."
- Problem: The editors gave z_C the meaning "China's gain if Europe keeps control" in Corollary 3(d), and z_C is used that way at the end of the proof of cor:control. The proof of the bidding lemma uses z_C (and z_U, z_i) for drop levels. The appendix declares proof symbols local, but this is the one rename the revision was meant to settle.
- Replacement: in the proof of lem:bidding, write the drop levels as $\hat z_i$, $\hat z_U$ and $\hat z_C$ ("A strategy is a drop level $\hat z_i$." "Fix China's drop level $\hat z_C$." "Fix Washington's drop level $\hat z_U$."). Keep $\bar z_U$ for the maximal credible bid.

### 13. Numerics paragraph overstates what the rupture script checks

- File: paper/sections/B_numerics.tex
- Anchor: "The bound of \cref{rem:rupture} has no violation"
- Problem: v2_rupture_bite.py checks the bite of a single withdrawal against u + min{d, Lambda_psi}, and the lambda = 0 case. It does not check the equality claim (Q + d >= Qhat) or the one-budget part (c)(i) with concessions and several instruments, which the remark also asserts.
- Replacement: "The bound on the bite of a single withdrawal in \cref{rem:rupture} has no violation. The equality case and the one-budget part of the remark are proved but not checked numerically"

### 14. Boundary in the cor:master(c) threshold

- File: paper/sections/08_evidence.tex
- Anchor: "would imply a positive transfer unless $Q<-\beta V/(1-\beta)$ (\cref{cor:master}(c))"
- Problem: By part (c), with Q <= 0 and lambda > 0, P* > 0 if and only if Q > -beta V/(1-beta). At equality the transfer is zero.
- Replacement: "would imply a positive transfer unless $Q\le-\beta V/(1-\beta)$ (\cref{cor:master}(c))"

### 15. "Washington's slack" in the scenario table

- File: paper/sections/C_scenario.tex
- Anchors: "Rationing a loyal Europe lowers $x_{ai}(A)$, hence $d_{ai}$ and Washington's slack." and "than the slack it loses."
- Problem: Slack is Europe's (Lambda = [-Q]^+). Washington spends it.
- Replacement: "Rationing a loyal Europe lowers $x_{ai}(A)$, hence $d_{ai}$ and Europe's slack." and "than the slack it can no longer spend."
