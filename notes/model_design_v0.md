# Model design v0 (working notes, not paper prose)

## Core idea
Europe (E) holds ASML. Two great powers bid for E's alignment: the US (U, security patron, first mover)
and China (C, rival). E's leverage is the transfer it can extract. Credibility enters through which
sanctions are ex post rational; linkage enters through U's security and AI instruments; China
dependence enters through C's bids and C's coercion.

## Static alignment contest (baseline)
Alignment options k in {A, H, P}:
- A  Atlantic: full compliance with U's denial requirements (no DUV/servicing to China).
- H  Hedge: status quo ante 2028, legacy DUV sales and servicing to China.
- P  Pivot: advanced tools, servicing or licensing to China.

Primitives (all >= 0):
- V_k   U's loss if E chooses k instead of A (V_H < V_P).
- W_k   C's gain if E chooses k instead of A (W_H < W_P).
- S     value to E of the US security guarantee (defense dependence).
- kappa_k = pi_A - pi_k   conditionality of the guarantee against option k (kappa_H ~ 0, kappa_P ~ 1).
- alpha_k   E's loss from US frontier-AI access restrictions triggered by k (credible under compute scarcity).
- theta  US extraterritorial reach (FDPR, de minimis, US-origin content): blocks share theta of W_k.
- f_k    firm-level penalties on ASML if U enforces jurisdiction.
- eta_k  E's intrinsic aversion to China gaining (values, Russia-China axis).
- r      C's coercion of E if E chooses A (rare earths, legacy chips).

Pivot premium: Q_k = (1 - theta) W_k - kappa_k S - alpha_k - f_k - eta_k + r.
Linkage L_k = kappa_k S + alpha_k + f_k.

Timing: U offers t_U (paid if A); C offers t_C^k (paid if k); E chooses; sanctions realize.
Tie-breaking / existence: Groseclose and Snyder (1996) style first-mover preemption.

Prop 1 (outside-option / losing-bidder logic):
  If V_k >= Q_k for all k: E chooses A, t_U* = max{0, max_k Q_k}.
  E payoff = -r + max{0, max_k Q_k}. Independent of V. Leverage zero if all Q_k <= 0.
  If some V_k < Q_k: C wins, E payoff = V_k - r (patron dependence matters only when E realigns).
Robustness: same outcome under Rubinstein with outside options (Binmore-Shaked-Sutton 1989) when
status quo supply continues during bargaining (inside option = status quo). V matters only if E can
credibly interrupt supply during bargaining (hold-up), which requires an ex post rational interruption.

Corollaries:
- Defense dependence matters only through conditionality kappa*S. Unconditional guarantee (kappa=0)
  or worthless guarantee (pi_A=0) both remove the security lever. U's leverage is maximized by a
  guarantee that is reliable for the loyal and void for the disloyal (hierarchy, Lake 2009).
- China's coercion r raises U's cost one for one when Q>0 but never raises E's welfare; it lowers
  E's welfare at the corner Q<=0. China dependence is a tax on the alliance, not a source of rent.
- China's demand W raises E's rent one for one once Q>0: the losing bidder sets the price. De-risking
  that lowers W lowers E's leverage over U.
- theta (jurisdiction) caps leverage: if theta -> 1 and f>0, Q<0 regardless of W. De-Americanizing
  ASML's supply chain is a precondition for leverage.

## Denial crisis (2028 episode)
U demands move from H to A. U's instrument: FDPR enforcement (theta, f) with own cost phi.
Credible iff theta*V_H >= phi. Under uncertainty about phi (prob p of enforcement), E complies iff
p f_H >= (1-theta) W_H - ... : with existential f, tiny p suffices (threat that leaves something to
chance; asymmetric stakes). "ASML cannot call the bluff" is an equilibrium of asymmetric stakes.

## Hold-up / using ASML against the US (2029 ACI episode)
Threat to interrupt EUV servicing to US-aligned fabs to win Tier 1. Not ex post rational for E
(loses revenue, no buyer gains), and U holds escalation dominance (security). Credible only with
commitment devices (delegation, automaticity) or if C pays for the interruption (collapses to pivot).

## Collective choice (divide and rule)
Pivot requires approval of a coalition in family K (holder veto for national export licensing;
QMV/blocking minority for ACI). U moves first with member-specific transfers; C second
(Groseclose-Snyder vote buying). U's cost = cost of making the cheapest veto player unwilling.
Holder's paradox: the holder bears targeted penalties (FDPR on its firm, targeted Tier status) while
the gains from leverage are an EU public good; U targets the holder (Netherlands Tier 1 in Europe 2031).
Delegation to an agent internalizing EU-wide gains and less exposed raises leverage (Rogoff analogue),
if delegation is itself credible.

## Dynamics: two clocks and preventive control (2031 episode)
Periods t=1,2. Q_t rises as S_t falls (rearmament, d<1) and falls as W_t decays (China's indigenous EUV,
m<1) and as alpha_t grows (AI dependence, g>1).
- E's window: Q_t > 0.
- U's ultimatum credibility (AI stick for refusing control): executing Tier 3 must not trigger pivot,
  i.e. Q_t + alpha_t <= 0 (security and jurisdiction alone deter pivot).
- Since Q_t + alpha_t >= Q_t, U's ultimatum window closes before E's leverage window opens.
- Preventive control: U demands control at t=1 iff Q_2 > 0 (future window), Q_1 + alpha_1 <= 0
  (credible ultimatum), and alpha_1 > sigma + r^c (stick exceeds sovereignty cost plus China's
  punishment of the transfer). Requires Q_2 - Q_1 > alpha_1: a large, rapid shift (Fearon/Powell).
- China's threat to punish the transfer (r^c) protects European ownership by raising U's price.
- Incomplete information about sigma (Dutch domestic politics): risk-return trade-off, breakdown
  (Tier 3 executed, E keeps ASML) with positive probability.
- Threat-promise trade-off: a binding commitment to future Atlantic alignment removes U's preventive
  motive but sets future rents to zero. E can have a credible promise or a credible threat, not both.

## Europe 2031 revisited
- 2028 cave: equilibrium given theta ~ 1 and existential f. Solidarity from other states does not change theta.
- 2029 ACI failure: cheapest blocking minority is security dependent; holder opposes (Tier 1).
- 2031 ultimatum: preventive control under anticipated shift; China's threat on "neither" is
  strategically confused (punishing both sign and neither removes the wedge).
- Epilogue remedies: compute on European soil lowers effective alpha (hostage); coalition helps only
  with complementary assets and internal transfers.
