# Model design v2 (after referee round 1)

Status: design memo. Every statement below is a CLAIM to be verified (proof + brute-force numerics) before it goes in the paper. Notation is final unless a verifier finds a problem.

## 0. What changes and why

| Referee demand | v2 response |
|---|---|
| R1: static result is known; lead with the slack principle | Static threshold becomes Lemma 1 + Prop 1 (credited to Bertrand/Groseclose-Snyder/outside-option principle). Organizing result is Prop 2 (slack principle). |
| R1: one master game instead of six protocol cases | Prop 1: random-proposer bargaining with breakdown hazard, discounting, outside option, frequent-offer limit: P* = max{Q, w_b(Q + beta(V - Q))}. Old cases (b), (c) dropped (appendix remark only). |
| R1: one commitment technology | Unified stakes: any public conditional commitment (promise or threat) can carry a stake m <= mbar_i forfeited if broken. Caps B_U, B_C become mbar_U, mbar_C. Security conditionality uses the same stakes, plus an ex ante assurance cost (Prop 3). |
| R1/R3: China's on-path punishment of alignment | Removed from Q. Chinese coercion is modelled as counter-threats attached to specific concessions (Prop 2(e)) and to a control transfer (Prop 4); under complete information these are executed only if they change the patron's demands. Remark: untargeted punishment of alignment would be executed on path and is made only if self-rewarding; record suggests none. |
| R1: relative gains for China | W_C = (1-theta)W + rho V; omega = lambda_C min{W_C, mbar_C}. In a zero-sum race the cap binds, so lambda_C and mbar_C, not China's interest, set omega. |
| R1: AI double counting; in-kind transfers | Baseline = patron's ex post optimal provision to a loyal holder. Transfers are promised increments above baseline; threats are withdrawals below it. AI access is one instrument with conditional part d_ai. In-kind cost factor phi_U noted in a footnote. |
| R1: binary instruments, additivity | Instruments are general: withdrawing set J lowers aligned payoff by Delta^A(J) and exit payoff by Delta^X(J). No additivity needed for Prop 2. AI U-shape demoted to a remark with continuous allocation. |
| R1/R2: dependence vs conditionality true by definition; kappa exogenous | Security micro-founded (s_A = s_X + s_L; s_X = s_0 + s_B(V)); graduated (core vs posture); conditionality chosen at a cost (Prop 3: interior optimum; "conditionality is the price of concessions"). |
| R2: access channel / silicon shield; Europe's access denial | s_X rises with access value and possibly V, capping credible conditionality (kappa_bar falls). Access denial enters as a European hold-up instrument in Prop 6. |
| R1: dynamic control underdeveloped | Prop 4 with explicit value of control v_c, issuing cost k, enforceability Delta_c, holder investment, strategic China. Prop 5 (breakdown) for log-concave F. Remark on self-binding vs dual key. |
| R1: Prop 6 issues | Hold-up rebuilt inside the master game with disagreement flows and buffers; Markov equilibrium; US cost of the AI cut included; nesting (share h of servicing under US compulsion) included; multiplicity literature cited. |
| R1/R3: demote Prop 5; ACI two stages | Section 6 "Who decides" as Remarks: gatekeeper and divide-and-rule; firm between jurisdictions (Decree 835, Blocking Statute); two-stage ACI and delegated-act route with member-specific exposure. |
| R2/R3: scenario anchor; calibration | Intro hook keeps Europe 2031 (user's request) but the puzzle is the 2019-2026 record. Calibration figure dropped; replaced by an orders-of-magnitude paragraph that states the bias directions and puts the weight on mbar_C and lambda_C. Scenario reading moves to an appendix table without "confirms/rejects". |
| R1/R2/R3: discriminating predictions; cases | Section 7: coding rules, observable implications vs rival accounts, structured comparison of real cases, proposed tests. |

## 1. Primitives (Section 3 of the paper)

Players: holder E (Europe; the Netherlands as gatekeeper in Section 6), patron U, rival C.

**Alignment.** a in {A, X}. Exit X: the holder lets ASML sell and service EUV and advanced immersion DUV tools for Chinese fabs against US objection. Hedging (legacy immersion tools and their servicing) is a secondary choice, handled in Section 4.

**Instruments and baseline.** U provides instruments j (core defence; posture and enablers; frontier AI access; ASML's access to US inputs, persons and customers). After alignment a, U chooses provision x_j(a) sequentially rationally given any stakes. E values j at v_j(x). Conditional part d_j = v_j(x_j(A)) - v_j(x_j(X)) >= 0. Baseline: E aligned, U provides x_j(A), no transfers. A *transfer* is a promised increment above baseline; a *threat* is a withdrawal below it.

**Commitment technology (unified).** Before E moves, each great power i may attach a stake m <= mbar_i to any announced conditional action (promise or threat); it forfeits m if the condition is met and it does not act. Creating a stake is free; only forfeiture costs. Hence a promise of tau is credible iff tau <= mbar_i (paying has no ex post value); a threat with ex post execution cost e is credible iff e <= mbar_i. A threat that is executed on the equilibrium path costs its executor e; a threat that deters is never executed.

**Security (graduated, micro-founded).**
- Core: in a crisis (probability folded into S_k) U defends iff s_a - m_S 1{a=X} >= xi, xi ~ G continuous. s_A = s_X + s_L (s_L >= 0: value of a loyal ally, e.g. reputation with other holders). s_X = s_0 + s_B (U's own interest in European security and the access value of European territory; s_B may rise with V: "silicon shield"). m_S <= mbar_U is a stake on abandoning a realigned holder. kappa(m_S) = G(s_A) - G(s_X - m_S); kappa_bar = G(s_A) - G(s_X - mbar_U). d_core = kappa S_k.
- Posture and enablers: continuous flow p; conditional part d_p (cheap to withdraw selectively).

**AI access:** one instrument, conditional part d_ai (Remark A1: with continuous allocation, d_ai vanishes under extreme scarcity only if loyal allies are cut to the exiter's level).

**Firm-level penalties:** d_f = chi_f f, chi_f = 1{phi V <= gamma + mbar_U} (self-harm limits credibility).

**Exit cost:** c = sum_j d_j + eta (eta >= 0 intrinsic cost of exit).

**China's credible offer:** W_C = (1-theta)W + rho V (rho >= 0 relative-gains weight; theta = share blocked by US flow jurisdiction); omega = lambda_C min{W_C, mbar_C}.

**Exit premium:** Q = omega - c. **Slack:** Lambda = [-Q]^+.

**Remark (untargeted Chinese punishment of alignment).** A threat to punish alignment itself is executed whenever E aligns despite it, so China makes it only if its ex post value g_r >= 0 or it flips the outcome; if made with g_r >= 0 it adds r_A to Q. We set r_A = 0 (no instance in the record).

## 2. Lemma 1 (bidding benchmark)

U and C bid for E's alignment in an open ascending auction; bids are staked promises (U up to mbar_U; C's bids valued by E at lambda_C, up to the cap). Then E chooses, then instruments are used.

**Lemma 1.** (i) After alignment, U's instrument choices are as above; exit costs E c relative to alignment. (ii) If Q < V and Q <= mbar_U, E aligns and U pays [Q]^+. If Q > min{V, mbar_U}, E exits; when mbar_U < Q < V both E and U would prefer a transfer in [Q, V] (inefficient exit from limited US commitment).

(Proof: standard; ascending auction ends at the loser's maximal credible bid net of c.)

## 3. Proposition 1 (master bargaining game)

After the bidding stage fixes omega, E and U bargain over a perpetual signed transfer flow P (P > 0: U pays E; P < 0: E concedes). Offers every Delta. Each round: E proposes w.p. beta in [0,1), U otherwise. Responder accepts (game ends) or rejects. After rejecting a U offer, E may exit (flows Q to E, -V to U forever). If no voluntary exit, breakdown into exit occurs w.p. mu = 1 - e^{-lambda Delta}; otherwise the status quo (flows 0, 0) continues; discount delta = e^{-r Delta}. All values normalized per unit flow (multiply PV by 1-delta). Assume Q < V and agreements are binding.

Discrete Delta: stationary values
- x_A = w (Q + beta (V - Q)), w = mu / (1 - delta (1 - mu)) [exit not used]
- x_B = ((1-beta) Q + beta mu V) / (1 - beta delta (1 - mu)) [exit used after rejecting a U offer]
- x* = max{x_A, x_B} (fixed point of a contraction).

**Proposition 1.** For each Delta > 0 there is a unique stationary SPE; agreement is immediate at E's value x*(Delta) above. As Delta -> 0,
  P* = max{ Q, w_b (Q + beta (V - Q)) },  w_b = lambda / (lambda + r) in [0,1].

**Corollary 1.** (a) P* >= Q: E never concedes more than its slack. (b) If lambda = 0, P* = [Q]^+; if beta = 0, P* = max{Q, w_b Q}; so with no breakdown risk or no agenda power, Q <= 0 implies P* <= 0 (threshold). (c) P* > 0 iff Q > 0 or (lambda > 0 and Q + beta(V-Q) > 0). (d) Where the second term binds, dP*/dV = beta w_b. (e) V enters P* only through beta w_b, and through Q via W_C (if the cap does not bind), chi_f, and kappa_bar (silicon shield); Section 6 adds hold-up.

Nesting: lambda = 0 gives the outside-option principle ([Q]^+; old case e); r -> 0 with lambda > 0 gives Q + beta(V-Q) (old case f); beta = 0 gives the US-proposer benchmark; beta -> 1, lambda -> infinity gives V (E take-it-or-leave-it with certain rupture).

## 4. Proposition 2 (slack principle) - organizing theorem

**Setup (one period).** E is aligned; exit premium Q (E receives [Q]^+ from the bidding stage). U has a finite set of demands k with cost t_k > 0 to E and value w_k > 0 to U. A concession is *reversible* (undone if E later exits: E's exit payoff unaffected; e.g. policy alignment) or *sunk* (lowers both aligned and exit payoffs: payments, asset or control transfers). U's credible instruments J^c. Withdrawing J from an aligned E for the period lowers E's aligned payoff by Delta^A(J) and its exit payoff by Delta^X(J), 0 <= Delta^X <= Delta^A, both nondecreasing in J. Define u(J) = Delta^X(J) (unconditional part) and d(J) = Delta^A(J) - Delta^X(J) (conditional part = contribution to exit cost). Withdrawn instruments stay withdrawn for the period ("threats are spent"). Protocol: U issues any finite sequence of ultimatums (adaptive); each names concessions and a threat set from the instruments not yet withdrawn; E accepts or refuses (threat executed). At the end, the bidding contest is replayed: U pays [Q + d(J_w) + T_rev]^+ where J_w = withdrawn set and T_rev = reversible concessions made. (Sunk concessions shift both payoffs and leave Q unchanged.)

**Proposition 2.** Let Lambda = [-Q]^+.
(a) *Bite.* Refusing an ultimatum backed by J costs E B(J) = u(J) + min{d(J), Lambda}, net of the rent U must then pay. If Q >= 0 only unconditional parts bite.
(b) *Reversible concessions.* E's net loss from reversible concessions totalling T is min{T, Lambda} (Q < 0) [beyond Lambda U pays the excess back as rent]; it accepts a bundle (T_rev reversible, T_s sunk) backed by J iff min{T_rev, Lambda} + T_s <= B(J).
(c) *One budget.* In any equilibrium of any sequence of ultimatums in the period, E's total net loss is at most B(J^c) = u(J^c) + min{d(J^c), Lambda}; the bound is attained by one bundled ultimatum if U has enough demands. Conditional instruments share one budget, Lambda: their bites are not additive. Reversible concessions cost E at most Lambda in total, however backed.
(d) *Rationing.* With reversible demands only, U's optimal demand set solves max sum_k w_k y_k s.t. sum_k t_k y_k <= min{Lambda, B(J^c)}, y in {0,1}^K. As Q rises toward 0 the capacity falls; demands from every issue area (export controls, servicing, trade, defence spending) draw on it.
(e) *Counter-threats.* A credible Chinese threat to impose sunk loss r_k on E if E makes concession k adds r_k to the sunk cost of k. A counter-threat that changes no demand is either never triggered or executed at a loss to China; so under complete information China gains only through the demands its threats remove. If U has other demands that fill the budget, E's total loss is unchanged: the counter-threat taxes the patron (lower-value concessions), not the holder.
(f) *Policing a hedge.* Stopping a hedge worth y_H to E by linkage requires y_H <= min{Lambda, B(J^c)} (reversible concession); by flow jurisdiction (cost e_F to U, Q unchanged) requires only e_F <= mbar_U. Hence linkage against hedging is used only when E has slack Lambda >= y_H, and disappears as Q -> 0 even where flow jurisdiction is unavailable; executing a conditional withdrawal raises Q by its d (spent deterrence).

## 5. Proposition 3 (endogenous conditionality)

U chooses kappa in [kappa_0, kappa_bar] before bidding, at assurance cost H(kappa), H(kappa_0)=0, H increasing and convex (other allies discount a guarantee with a broad withdrawal rule; risk of triggering by mistake). Q(kappa) = Q_0 - (kappa - kappa_0) S_k. U converts slack into concessions worth w in [0,1] per unit of E cost (its best reversible demands), assuming B(J^c) >= Lambda. U's payoff Pi(kappa) = -[Q(kappa)]^+ + w Lambda(kappa) - H(kappa). Let kappa_z = kappa_0 + Q_0/S_k (premium zero).

**Proposition 3.** (a) If w = 0, kappa* = min{kappa_z, kappa_1, kappa_bar} (with kappa_1 solving H' = S_k, kappa_0 if Q_0 <= 0): U never makes its guarantee more conditional than needed to hold the premium at zero; slack is zero. (b) If w > 0 and H'(kappa_z) < w S_k (and kappa_z < kappa_bar), kappa* = min{kappa_w, kappa_bar} > kappa_z with H'(kappa_w) = w S_k; slack Lambda* = (kappa* - kappa_z) S_k > 0: conditionality is the price of concessions. (c) In the regime kappa* = kappa_z, d kappa*/d Q_0 = 1/S_k and U pays no rent: a stronger Chinese bid elicits a more conditional guarantee, not a payment. In the interior-slack regime, kappa* does not depend on Q_0 and slack falls one for one with Q_0 (China's bid is paid for out of U's concessions). In the capped regime, if Q(kappa_bar) > 0, U pays [Q(kappa_bar)]^+. (d) kappa_bar is nonincreasing in s_X, hence in access value and (silicon shield) V.

## 6. Proposition 4 (preventive control) + corollaries

Two periods, discount delta. Premia Q_1, Q_2 if E holds control. U may issue an ultimatum at the start of period 1 (cost k >= 0): transfer control (payment T >= 0 at signing) or face a threat with bite B_1 in period 1 (Prop 2(a), credible: execution cost e <= mbar_U). Transfer: lowers E's premium at both dates by Delta_c in (0, infinity] (enforceability: relocation, US-held technical controls, US subsidiaries vs Dutch override), gives U intrinsic value v_c >= 0, costs E sovereignty cost sigma >= 0 (incl. preference-share foundation, investment screening, FSR review) and China's credible punishment of a transfer r^c >= 0. Investment: after the period-1 outcome E may invest Ibar at cost K_I to raise its period-2 premium by Ibar; it invests iff delta([q + Ibar]^+ - [q]^+) > K_I, where q is its period-2 premium (Q_2 or Q_2 - Delta_c). Define I(q) that indicator, Rent_U(q) = delta[q + Ibar I(q)]^+, Val_H(q) = Rent_U(q) - K_I I(q).

ΔR_U = [Q_1]^+ - [Q_1 - Delta_c]^+ + Rent_U(Q_2) - Rent_U(Q_2 - Delta_c)
ΔR_H = [Q_1]^+ - [Q_1 - Delta_c]^+ + Val_H(Q_2) - Val_H(Q_2 - Delta_c)

**Proposition 4.** U issues, and E accepts, iff Gamma = v_c - k + min{ΔR_U, (ΔR_U - ΔR_H) + B_1 - sigma - r^c} > 0. The payment is T* = [ΔR_H - B_1 + sigma + r^c]^+.
Corollaries: (i) preventive motive: with v_c <= k, issuance requires ΔR_U > 0, i.e. a positive premium at some date that control removes, and B_1 + (ΔR_U - ΔR_H) > sigma + r^c; (ii) investment: ΔR_U - ΔR_H = K_I [I(Q_2) - I(Q_2 - Delta_c)] >= 0, so an autonomy investment E cannot commit to forgo raises Gamma; (iii) Gamma is nondecreasing in Delta_c; (iv) with v_c = k = 0, Delta_c = infinity, no investment, Q_1 < 0: Gamma = min{delta[Q_2]^+, B_1 - sigma - r^c} (old Prop 3); (v) if China's ex post value from punishing a transfer is negative (rho = 0), China's threat is made only if it deters (r^c large enough that Gamma <= 0), so on path a transfer is never punished.

**Lemma (spent and self-limiting cuts).** The bite of a multi-period cut is sum_s delta^{s-1}[u_s + min{d_s, Lambda_s}]; extending a cut into dates with Q_s >= 0 adds only unconditional bite and costs U d_s in rent.

**Corollary (windows), N periods.** As before (v_c = 0, Delta_c = infinity, k -> 0+): U issues at some date iff there is a date t with credible threat, b_t > sigma + r^c and a later date t' > t with Q_t' > 0.

**Remark (self-binding vs dual key).** Self-binding (Europeanized controls such as Delegated Regulation 2025/2003; treaty-entrenched controls) lowers E's premium by Delta_b at cost sigma^b with E holding the key; dual-key licensing lowers it by Delta_d with U holding a veto over China-bound licences (a partial control transfer, with sovereignty cost below sigma). With Delta_b = infinity: binding pre-empts the ultimatum iff v_c <= k (or Gamma after binding <= 0), and E strictly prefers to bind iff -sigma^b - r^b > its ultimatum payoff max{ΔR_H - B_1, -sigma - r^c} (when Q_1 < 0, Delta_c = infinity, no investment).

## 7. Proposition 5 (breakdown, general F)

sigma private, CDF F on [0, sigma_bar] with density f, F log-concave. Conditions of Prop 4 with Delta_c = infinity, no investment, Q_1 < 0, mbar_U >= e. Write R = delta[Q_2]^+, btilde = B_1 - r^c. If U issues with payment T, E accepts iff sigma <= T + btilde - R. U's gain with cutoff s: F(s)(btilde + v_c - s) - (1 - F(s)) e - k. Interior optimum: btilde + v_c + e - s = F(s)/f(s) (unique by log-concavity), s*. Constraint T >= 0: s >= btilde - R.

**Proposition 5.** shat = max{btilde - R, min{sigma_bar, s*}}; U issues iff F(shat)(btilde + v_c - shat) - (1 - F(shat)) e > k. Conditional on issuance, breakdown probability P_b = 1 - F(shat) is nonincreasing in B_1, e and v_c and nondecreasing in r^c. Uniform F gives s* = (btilde + v_c + e)/2.
(Discuss: repeated offers and Coasean screening; not modelled.)

## 8. Section 6: who decides; hold-up

**Remark G (gatekeeper and divide-and-rule).** China-facing exit requires the Dutch licence (Reg. 2021/821 Art. 12(2)). The relevant premium is Q_NL = omega_NL - c_NL, where c_NL counts conditional parts U can target at the Netherlands. Partners affect Q_NL only through transfers. A benefit x_h targeted at the gatekeeper and credibly withdrawn on exit lowers the gatekeeper's rent by min{x_h, [Q_NL]^+} and raises its slack by [x_h - [Q_NL]^+]^+.

**Remark F (firm between jurisdictions).** ASML ships under a licence iff y + p_C + p_B >= f^F (y China profit; f^F US penalty; p_C Chinese penalty for complying with US measures, e.g. Decree 835; p_B EU Blocking Statute penalty if US measures were listed). Otherwise exit needs compulsion at cost zeta: effective premium Q - zeta 1{y + p_C + p_B < f^F}. For servicing bans in China (a concession), p_C is a Chinese counter-threat in the sense of Prop 2(e).

**Remark E (two-stage ACI; delegated act).** Stage 1: Council determination by QMV (blocking: >= 4 members with > 35% population, or >= 13 members). Stage 2: Commission implementing act, examination procedure; appeal committee: Commission may adopt unless QMV against. Delegated act removing the US from EU001: stands unless EP majority or Council reinforced QMV (20 members, 65%) objects. Members vote q_i (net gain from countermeasure, falling in member-specific exposure kappa_i S_i). U's cheapest defeat: buy a stage-1 blocking minority at cost Phi(0) = min_{J in blocking} sum_{i in J} [q_i]^+; members with q_i < 0 (frontline) block for free. With a rival bidder for adoption, Groseclose-Snyder program (cite Banks 2000; Dekel, Jackson and Wolinsky 2008).

**Proposition 6 (pain and breakdown: hold-up).** Master game of Prop 1 with disagreement flow costs c_E(t), c_U(t) >= 0 (bounded, piecewise continuous). Assume exit never binds. In the frequent-offer limit the unique Markov SPE has immediate agreement at
  P* = w_b [Q + beta (V - Q)] + (1 - w_b) [beta Chat_U - (1 - beta) Chat_E],  Chat_i = (r + lambda) int_0^inf e^{-(r+lambda) t} c_i(t) dt.
Corollary (interruption): if Europe can interrupt servicing (cost l to itself from t = 0; cost (1-h) c_S to U from t_U, h = share of US-fab servicing performed by persons U can compel), interruption raises P* iff beta (1-h) c_S e^{-(r+lambda) t_U} > (1 - beta) l, i.e. iff t_U < tbar = ln[beta (1-h) c_S / ((1-beta) l)] / (r + lambda). With the interruption decided at the start of each round and the US buffer depleting only while servicing is interrupted, the decision is time consistent (holds every round iff at t = 0). Same formula for access denial (bases, overflight). The US cost of an AI cut on a loyal Europe enters c_U from t = 0.

## 9. Evidence plan (Section 7)

Coding rules; observable implications vs rivals (shared interest / eta, Lake hierarchy, Morrow trade-off, Drezner conflict expectations, simple cost minimization); structured comparison table (NL 2019-26; Japan 2023; Korea VEU 2025; Germany Zeiss/Trumpf; Taiwan 50/50 2025; FRG offsets 1961-67; UK and CoCom China differential 1957; FRG-Brazil 1975-77); proposed tests (event dataset; elite survey experiment on kappa; process tracing with Woo requests).
