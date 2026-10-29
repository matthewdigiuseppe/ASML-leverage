# A minimal model of Europe's ASML leverage (design, to be verified)

Goal: the smallest model that delivers the paper's main point in a form a non-specialist can follow.

## Core model (one round)

Numbers (all in Europe's payoff units, relative to the status quo in which Europe stays with Washington and nobody pays anyone):
- c >= 0: what China's offer is really worth to Europe if Europe switches sides (after Europe's discount for doubts about Chinese promises).
- k >= 0: what Europe would lose from Washington if it switched: the benefits Washington would actually withdraw (security support it would cut, AI access, US parts and staff).
- u >= 0: US benefits Europe keeps whatever it does (Washington provides them for its own reasons).
- V > 0: what Washington loses if Europe switches.
Europe's position: q = c - k.

Timing (Washington sets the terms):
1. Washington proposes a deal t (t > 0: Washington pays Europe t; t < 0: Europe makes concessions worth -t to Washington, valued equally by both). It attaches a threat: if Europe rejects, Washington withdraws k. Washington can commit to the threat (for example by making it public).
2. Europe accepts (stays, gets t) or rejects.
3. After a rejection the threat is carried out. Europe then stays (payoff -k) or switches (payoff c - k, since k is already lost). Switching costs Washington V.

Claims:
R1 (price and squeeze). If c - k <= V, Washington offers t* = c - k and Europe accepts: Washington pays Europe c - k when it is positive, and squeezes concessions worth k - c when it is negative. If c - k > V, Washington would rather lose Europe, and Europe switches. V does not affect t*.
R1' (threats only matter on the downside). If Washington cannot commit to its threat, t* = max{0, c - k}: it still pays when Europe's position is positive, but it can no longer squeeze.
R2 (only the part Washington would withdraw counts). t* depends on k and not on u, so Europe's total dependence (u + k) is irrelevant; only the part Washington would actually withdraw matters.
R3 (one budget). If Washington bundles several demands costing Europe d_1, ..., d_n, all backed by the same threat, Europe accepts a bundle S iff sum_{i in S} d_i <= k - c. Every demand draws on the same gap.

## Add-on A: when Washington's need matters (power to hurt)

Talks over a deal run in rounds; Europe makes the proposal with probability beta, Washington otherwise. Before talks, Europe commits to a standoff policy: until agreement, Europe stops servicing, costing Washington x per round and Europe y per round (its own lost sales plus anything Washington does in return). Patient players, frequent rounds, exit not attractive.
Claim A: committing to the standoff raises Europe's take iff beta * x > (1 - beta) * y. If Washington sets the terms (beta = 0) Europe's power to hurt is worth nothing. Washington's need for ASML enters through x. The commitment has to be made before offers; a stoppage Europe can lift after any offer is never used. (Special case of the paper's Corollary 5 with no stockpile and no compelled servicing.)

## Add-on B: when Washington demands control

Two periods. Europe's positions q_1 = c_1 - k_1 and q_2 = c_2 - k_2. Without a demand, Washington pays Europe max{0, q_t} each period and makes no other demands. At the start of period 1 Washington can demand control of ASML for both periods (Europe can then never switch), paying T >= 0 and threatening to withdraw k_1 in period 1 if Europe refuses. Handing over control costs Europe s >= 0 (sovereignty, domestic politics). Discount delta.
Claim B: Washington demands control, and Europe accepts, iff q_2 > 0 (Europe's position tomorrow is positive) and k_1 - c_1 > s (today's squeeze exceeds Europe's cost of surrender). The payment is T* = max{0, delta*q_2 + s - (k_1 - c_1)}. The handover destroys s to avoid rents that are only transfers. (Special case of the paper's Proposition 5 / Corollary 3(iv).)

## Plain-language summary
- Europe is paid for its alternative (c - k), not for being needed (V).
- When the alternative is bad, Washington can squeeze up to the gap, and every demand shares it.
- Only the help Washington would actually withdraw gives it a hold.
- Washington's need matters only if Europe can hurt it during a standoff, has a say in the talks, and commits in advance.
- When Europe's alternative is set to improve, Washington wants control while it can still squeeze.
