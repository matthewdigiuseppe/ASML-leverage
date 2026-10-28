# Model draft v1 (for critique). Formal statements and proof sketches.

Notation: [x]^+ = max{0, x}.

## 1. Primitives

Players: Europe (E), United States (U), China (C). E controls the export and servicing decisions over ASML
(in practice: Dutch export licensing, firm compliance, EU instruments). E is unitary in Sections 1-3.

Alignment. E chooses a in {A, H, X}.
- A (Atlantic): ASML supplies only US-aligned fabs and complies with all US denial requirements.
- H (Hedge): ASML continues to sell and service legacy immersion DUV tools in China (the pre-2028 status quo in Europe 2031).
- X (Exit): ASML supplies China with frontier tools, servicing or licences (realignment).

Valuations (relative to A):
- V_a > 0: US net loss if E chooses a (V_H < V_X). Includes the AI-race cost of China's gain, net of any sanctions U executes.
- W_a > 0: China's gross gain from a (W_H < W_X).
- theta_a in [0,1]: share of China's gain the US can block through extraterritorial jurisdiction (FDPR, de minimis,
  US-origin content, control of US-made subsystems such as the EUV light source).

Linkage and other exit costs to E if a != A:
- S >= 0: value to E of US protection. pi_A, pi_a: probability US defends E under alignment A, a.
  kappa_a := pi_A - pi_a >= 0 (conditionality). Expected security cost of a: kappa_a S.
- alpha_a >= 0: E's loss from US restrictions on frontier AI (inference/model access), credible under compute scarcity.
- f_a >= 0: expected firm-level penalties (FDPR enforcement, entity listing, denial of US inputs).
- eta_a >= 0: E's intrinsic cost of China's gain (values, Russia-China axis).
Exit cost: c_a := kappa_a S + alpha_a + f_a + eta_a.

China's coercion: if E chooses A, China imposes r >= 0 (critical-input restrictions: rare earths, legacy chips).

Exit premium of option a: Q_a := (1 - theta_a) W_a - c_a + r.  Q* := max{Q_H, Q_X}.

Transfers: U promises tau_U >= 0 paid if a = A (Tier-1 access, tariff relief, reassurance, capital).
C promises tau_C^a >= 0 paid if E chooses a in {H, X} (market access, credit, co-production).

Payoffs:
u_E = tau_U - r if A;  tau_C^a - c_a if a in {H,X}.
u_U = -tau_U if A;     -V_a if a.
u_C = 0 if A;          (1 - theta_a) W_a - tau_C^a if a.

Timing: (1) U offers tau_U. (2) C observes and offers (tau_C^H, tau_C^X). (3) E chooses a. (4) Transfers and sanctions realize.
Offers lie on a grid of mesh eps > 0; E breaks ties in favour of A. We characterize limits as eps -> 0.

Assumption 1 (credible sanctions): the sanctions in c_a and r are carried out whenever the triggering alignment is chosen.
(Dynamic section endogenizes the credibility of the AI sanction.)
Assumption 2 (patron values the asset most): V_a >= Q_a for a in {H, X}.

## 2. Results

Proposition 1 (exit premium). As eps -> 0, every SPE has E choosing A, tau_U -> [Q*]^+, u_E -> -r + [Q*]^+,
u_U -> -[Q*]^+, u_C -> 0.
Proof sketch. Given tau_U, C can induce a only with tau_C^a > tau_U - r + c_a; doing so is profitable iff
(1-theta_a)W_a > tau_U - r + c_a + eps (grid), i.e. iff tau_U < Q_a - eps. So U wins iff tau_U >= Q* - eps (approximately),
and U's cheapest winning offer is the smallest grid point >= [Q*]^+ - eps. Losing costs V_{a*} >= Q* by Assumption 2.

Corollary 1. Leverage rho := [Q*]^+.
(i) rho does not depend on V_a (the patron's dependence) under Assumption 2.
(ii) rho is nonincreasing in S, kappa_a, alpha_a, f_a, eta_a, theta_a and nondecreasing in W_a.
(iii) d tau_U / dr = 1 when Q* > 0, but E's payoff -r + rho = max{-r, max_a[(1-theta_a)W_a - c_a]} is nonincreasing in r.
(iv) rho = 0 iff Q_a <= 0 for all a.
Conditional guarantee: kappa_a = pi_A - pi_a. Leverage falls with the credibility of the guarantee to a loyal E (pi_A) and
rises with the guarantee to a realigned E (pi_a). Unconditional (pi_a = pi_A) or worthless (pi_A = 0) guarantees remove
security from the bargain.

Robustness remark. Same outcome under Rubinstein alternating offers with E's exit as outside option and the status quo
(supply continues, protection continues) as inside option (Binmore, Shaked and Sutton 1989). V enters only if E can credibly
interrupt supply to U during bargaining. Lemma (no credible hold-up): if U's response to an interruption is a sanction
whose cost to E exceeds E's revenue-weighted gain from interrupting, interruption is never part of an SPE of the finite game.

Proposition 2 (race intensity). Let W_a = w_a Z, alpha_a = a_a Z, V_a = v_a Z with Z > 0 the intensity of the AI race.
Then dQ_a/dZ = (1-theta_a) w_a - a_a. If (1-theta_a) w_a < a_a for all a, leverage is nonincreasing in Z and is zero for all
Z beyond a finite threshold. The US's preventive incentive (Section 3) and its stick alpha_1 both rise with Z.

Proposition 3 (veto players). Suppose E is a set of members and option a requires the consent of every member of some
coalition in a family K_a (national competence: every coalition contains holder h; QMV for EU instruments). Members have
member-specific exit costs c_{a,i}, coercion r_i, and receive targeted transfers. U moves first with member-specific transfers,
C second. (a) Under holder veto with C buying only h: U's cost is [Q_{a,h}]^+, where Q_{a,h} uses h's own exit costs.
(b) Holding aggregate linkage fixed, U minimizes its cost by concentrating firm-level and targeted sanctions on the veto
player (FDPR on ASML; Tier-1 status for the Netherlands whose withdrawal raises alpha_h). (c) For an instrument that requires a
qualified majority to adopt (using ASML against the US via the ACI), U needs only to keep a blocking minority opposed; its cost
is the cheapest blocking minority's aggregate premium.

## 3. Dynamics: control rights, two clocks, preventive demands

Periods t = 1, 2, discount delta. Parameters indexed by t; Q_t is the period-t exit premium if E retains control.
Assume V_t >= Q_t (U always wins contests). If E retains control, period-t payoffs are as in Prop. 1.

At the start of t = 1, U may demand control: E transfers to U a veto over ASML's customers (joint holding) for t = 1, 2
in exchange for T >= 0. China punishes a transfer with r^c >= 0. E bears sovereignty cost sigma >= 0.
If E refuses, U chooses whether to cut E's frontier-AI access in t = 1 (Tier 3). Cutting removes alpha_1 from E's exit
costs in t = 1, so the period-1 premium becomes Q_1 + alpha_1.

Payoffs (relative to baseline: A, zero transfers):
Accept: E: T - sigma - r^c; U: -T.
Refuse, cut: E: -alpha_1 + [Q_1 + alpha_1]^+ + delta[Q_2]^+;  U: -[Q_1 + alpha_1]^+ - delta[Q_2]^+.
Refuse, no cut: E: [Q_1]^+ + delta[Q_2]^+; U: -[Q_1]^+ - delta[Q_2]^+.
No demand: as refuse, no cut.

Lemma 2 (credibility of the ultimatum). U cuts after a refusal iff Q_1 + alpha_1 <= 0 (security, jurisdiction and values
alone deter exit). With a public commitment carrying audience cost a_U, iff [Q_1+alpha_1]^+ - [Q_1]^+ <= a_U.

Proposition 4 (preventive control). With complete information and a_U = 0, U demands control in t = 1 iff
(i) Q_2 > 0, (ii) Q_1 + alpha_1 <= 0, and (iii) alpha_1 > sigma + r^c. E accepts. Then T* = [delta Q_2 + sigma + r^c - alpha_1]^+.
(i) and (ii) jointly require Q_2 - Q_1 > alpha_1 > 0: a large, rapid rise in E's exit premium.
(Verified by brute force over random parameters.)

Corollary 2 (two clocks). Suppose Q_t is increasing over a longer horizon (rearmament lowers kappa S faster than China's
indigenous lithography lowers W and AI dependence raises alpha). Let t_U be the last date at which Q_t + alpha_t <= 0 and t_E
the first date at which Q_t > 0. Then t_U < t_E: the US's ultimatum window closes before Europe's leverage window opens.
Preventive demands happen near t_U if a window is anticipated. Gradual shifts (Q_{t+1} - Q_t < alpha_t) let E's window open
without preemption. China's threat to punish a transfer (r^c) protects European ownership.

Proposition 5 (incomplete information). sigma ~ U[0, bar sigma] private to E; condition (ii) holds. Let R = delta[Q_2]^+ > 0,
a = alpha_1 - r^c > 0. U's optimal offer leaves E with acceptance cutoff s* = min{a/2, bar sigma} if a/2 <= R, or s* = a - R
if a/2 > R (T* = 0). Breakdown probability 1 - s*/bar sigma > 0 when s* < bar sigma: Tier 3 is executed, E keeps ASML and
loses alpha_1 (deadweight). Breakdown is decreasing in alpha_1, increasing in r^c and bar sigma, and (in the T*=0 corner)
increasing in Q_2. U demands control iff a > 0 and R > 0.

Proposition 6 (self-binding). Before t = 1, E can adopt a binding commitment to A in t = 2 (dual-key licensing / allied
export-control compact) at cost sigma_c. Then U has no preventive motive. Under complete information, E strictly prefers to bind
iff sigma_c < sigma + r^c and alpha_1 - delta Q_2 > sigma_c (when Prop. 4 conditions hold). E can have a credible promise
or a credible threat, not both.

## 4. Europe 2031 mapping
- 2028 cave (H to A): with theta_H near 1 and existential f_H, Q_H < 0 even with large W_H; uncertainty over U's
  enforcement (prob p) still yields compliance since p f_H is large (asymmetric stakes).
- 2029 ACI vote: Prop. 3(c): cheapest blocking minority is security-dependent (Poland, Baltics) plus holder with Tier-1.
- 2031: Prop. 4/5: preventive demand under anticipated drift; China's threat against "neither" removes the wedge between
  signing and refusing, which is strategically confused unless it is meant to induce exit.
- Epilogue: compute on European soil lowers effective alpha (hostage); coalition of middle powers helps only with
  complementary assets and internal transfers, otherwise U buys the cheapest member.
