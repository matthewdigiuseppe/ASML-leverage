# Critique of the minimal model (notes/minimal/design.md)

## Verdict

The core gets the paper's main point right, and its numbers are correct: with c >= 0 and a credible threat to withdraw all of k, Europe's net take of c - k is exactly what the paper's two steps give (Lemma 1 and Proposition 1 price Europe at max{0, Q}; Proposition 2 then takes back min{d, slack}). Four things need fixing before it goes to general readers. (1) "Washington sets the terms" makes the irrelevance of V look like an artifact of giving Washington all the bargaining power. In the paper it comes from costless delay, and the text has to say so. (2) Add-on B contradicts the core: the core lets Washington squeeze, the add-on turns the squeeze off, and if the squeeze were left on, Washington would never demand control. (3) Add-on A treats two different kinds of US need as one, and it leaves out the paper's other channel (talks that can collapse into realignment) and the claw-back result. (4) The parameter u, and the claim built on it, overstate what the paper says about unconditional help. The model can also lose about a third of its symbols without losing any content (section 2).

## 1. Does it capture the main point, and what misleads?

The main point, from the abstract, introduction and README: Europe's leverage over Washington is its exit premium (what China would credibly give it for switching, net of what switching would credibly cost it). It is not how much Washington needs ASML. When the premium is negative, Washington can extract concessions up to the shortfall (the slack), and every demand it makes draws on that one budget. The core model delivers both halves. The design's R1 and R1' reproduce the paper's floor and its positive-part result (Corollary 1(b) with lambda = 0), and R3 reproduces the one-budget result (Proposition 2(c)(i)). I checked the core formula against the paper's bite formula in 100,000 random draws, and they agree exactly once the general case below is allowed for.

### 1.1 "Washington sets the terms" (major)

In the minimal game as written, the proposer is what kills V. If Europe made the offer instead, with c > k, it could demand up to V: Washington would pay rather than face a credible switch. A reader will conclude, correctly for this game, that Europe gets nothing for being needed because the model hands Washington all the bargaining power. That is a much weaker claim than the paper's. In Proposition 1, with no rupture risk, Europe gets max{0, Q} for every beta < 1 (Corollary 1(b): "whoever proposes"). The reason is that failed talks cost neither side anything. Washington can turn down any European demand above Europe's walk-away value and come back with its own offer. Europe's only threat is to switch, and switching is worth only c - k.

Fix: keep Washington as the proposer for arithmetic convenience, but justify it in one sentence: "Failed talks cost no one anything, so Washington can always refuse a European demand and return with its own offer; letting Washington name the deal is a shortcut for this, not an assumption that it holds all the cards." Add-on A then becomes the natural relaxation of exactly this assumption (failed talks become costly), and the core and the add-on tell one story.

A smaller point: the paper's result also uses a timing convention (Europe can exit after rejecting a US offer; see the footnote to Proposition 1, where other timings admit equilibria in which Europe gets up to V). The minimal note does not need it, but it should not claim more robustness than the paper does.

### 1.2 Credibility of the threat, and what happens after it is carried out (moderate)

Assuming a credible threat matches the paper. Proposition 2 assumes a credible set J^c secured by stakes (audience costs), and R1' correctly reproduces the no-commitment case. The problem is the story told off the equilibrium path. In the design, Washington cuts off k, Europe then switches, and Washington loses V. A reader will ask why Washington would ever do something so self-destructive, and the threat will look absurd. In the paper Washington keeps Europe after a cut by paying the rent the cut creates (Proposition 2 assumes "the United States retains Europe after every history"). Europe's payoff is the same, c - k, so nothing in the results changes.

The fix also brings out the paper's central mechanism, which the design leaves implicit: **carrying out the threat frees Europe.** Once k is gone, Europe has nothing more to lose by switching, so its alternative jumps from c - k to c, and Washington must match c or lose it. That is why a cut-off threat bites only up to the gap k - c and not up to k. Say it in one sentence. It is the most useful single sentence for a general reader.

### 1.3 c >= 0 (minor, but say what it hides)

As a value of China's offer, c >= 0 is natural. What it hides is the paper's distinction between slack and bite. In general, Europe's take under a credible threat is max{0, c} - k, which matches the paper's max{0, Q} - min{d, slack} in every draw I ran. With c >= 0 this collapses to c - k, so the squeeze equals the gap. The paper's premium also includes eta, Europe's own reluctance to arm a rival that supports Russia's war. Washington cannot withdraw it, so it widens the gap without adding to Washington's squeeze, and with it the squeeze is capped at k. The design drops eta silently. Keep c >= 0, and add a footnote: "If Europe's own reluctance to switch outweighed China's offer, Washington could squeeze no more than k, the most it can take away."

### 1.4 "V only caps the price" (moderate)

This holds with c and k held fixed. In the paper V also moves c and k (Corollary 1(e)). China bids more for exit the more it values Washington's loss (rho V in W_C). Washington cannot credibly penalize ASML itself once V is large, because the penalty hurts US fabs (chi_f), which lowers k. The silicon-shield channel has no fixed sign. The design's summary line "Europe is paid for its alternative (c - k), not for being needed (V)" is therefore slightly too strong. Add one sentence: "Being needed can still help Europe indirectly, by making China bid more and making Washington reluctant to punish a firm it depends on." This costs no symbols, and it keeps the note from implying that V never matters.

### 1.5 u and R2 (moderate)

The design defines u as help Europe keeps "whatever it does". That makes R2 true by definition, and it misstates the paper. In Proposition 2(a), unconditional help (what Washington would still give a Europe that had switched) can be threatened if Washington can commit to withdrawing it. When it is, it bites in full and is not capped by the slack (Figure 3, panel (a): the unconditional threat "is the only one that still works" as slack falls to zero). What the paper does say is narrower: only the conditional part enters the exit premium, and Europe's dependence enters only through kappa S_k. So the summary bullet "Only the help Washington would actually withdraw gives it a hold" is wrong as a statement about the squeeze.

Fix: drop u. Make R2 part of the definition of k ("k counts only what Washington would really cut off if Europe switched; protection it would give a switched Europe anyway is not in k, however large"). If the note wants the paper's nuance, a footnote can add that threats to cut off help Washington would give in any case are a different and costly kind of threat (they punish an ally that stayed loyal), which the paper expects to be rare. Section 6 of the paper says this about the core guarantee.

### 1.6 Add-on A (moderate to major)

Three problems.

(a) It treats two different US needs as one. V is what Washington loses if Chinese fabs gain the tools. The design's x is what Washington's own fabs lose without ASML's servicing, the paper's c_S. The paper keeps them apart deliberately (Section 7: hold-up "works through Washington's own need for ASML's servicing, not through V"), and the distinction has a payoff: the Europe 2031 stockpile lowers c_S and leaves V where it was (Appendix D). The phrase "Washington's need for ASML enters through x" should go. Use two plain names (section 3).

(b) It drops the paper's first channel. The README and the conclusion name two ways in which need can pay: talks that can collapse into realignment while Europe makes proposals (Proposition 1), and hold-up (Proposition 6). Add-on A covers only the second. The two merge into a single formula at no extra cost. With constant costs, Proposition 6 gives Europe max{Q, x0}, where x0 = psi[Q + beta(V - Q)] + (1 - psi)[beta x - (1 - beta) y]. That is identical to

  x0 = beta X - (1 - beta) Y, with X = psi V + (1 - psi) x and Y = -psi Q + (1 - psi) y.

(I checked this identity numerically.) So: "each round of stalled talks costs Washington X and Europe Y; Europe gets the larger of c - k and beta X - (1 - beta) Y." X picks up V only through the chance that talks collapse, and x only through a stoppage. The design's Claim A is the special case psi = 0 with exit not binding.

(c) It ignores claw-back, and so it is inconsistent with the core. The core lets Washington back its offer with a credible threat. With that threat present, Europe's gain from Add-on A can be taken back down to c - k (Remark 1, stated in the paper for collapse risk). I verified the same algebra for the stoppage: with a standoff value N, a credible conditional cut of k bites min{k, max(0, N - (c - k))}. The paper does not state the stoppage case, so the note should either set Add-on A in the world where Washington cannot make its threats stick or add the caveat that the paper proves claw-back only for collapse risk.

Smaller points. "Patient players" is not needed (Proposition 6 requires r > 0; frequent offers are what matter). The design's commitment "before talks" is stronger than the paper needs: the paper requires Europe to choose before offers in each round and to be unable to lift the stoppage after rejecting an offer (Corollary 5 and variant (b)). That timing condition is the policy-relevant part and should stay.

### 1.7 Add-on B (major for internal consistency)

The add-on assumes that without a demand for control "Washington pays Europe max{0, q_t} each period and makes no other demands." That switches off the squeeze the core has just established. The paper makes the same assumption ("no other period-1 demand draws on the bite"; Section 6), but in the minimal note it reads as a contradiction, and it hides a condition the result needs. The core assumes concessions are "valued equally by both". If Washington can take today's squeeze as such concessions, it never demands control. Taking k_1 - c_1 in ordinary concessions and paying q_2 tomorrow beats control by exactly s, the sovereignty cost a handover destroys. I checked this in 100,000 draws (Washington's payoff gap equals s in every draw). The preventive motive needs today's squeeze to have no better use: Washington's other demands must be worth less to it than they cost Europe.

Fix: (i) drop "valued equally by both" from the core (no core result needs it, since only Europe's cost matters for acceptance); (ii) in Add-on B, state that Washington's other demands are worth little to it, so it cannot simply cash in today's squeeze; (iii) set delta = 1. The condition then reads cleanly as "q_2 > 0 and k_1 - c_1 > s", which matches the special case stated after Proposition 5.

The citation "Corollary 3(iv)" is wrong. Corollary 3 has parts (a) to (d), and (d)(iv) concerns China's deterrence of a transfer. Cite "Proposition 5 (special case in the text after it)".

### 1.8 Omissions

Leaving out China's counter-threats (Proposition 3) and the decision-maker material (Section 7) is right for a minimal note. One result costs a single sentence in this framework and is the README's third finding, so it should be included: Washington chooses k. Tying support to loyalty costs it trust with other allies, so a Washington that wants nothing beyond alignment raises k only until c - k reaches zero, and it goes further only to create squeeze room it plans to spend (Proposition 4(a) and (b)).

## 2. Parsimony

Drop:
- u (fold R2 into the definition of k; see 1.5).
- The demand costs d_1, ..., d_n in R3. The notation also clashes with the paper's d (conditional part) and with the paper's use of k as a demand index. One sentence carries R3.
- "Valued equally by both" (see 1.7).
- delta in Add-on B (set it to 1).
- The payment formula T* in Add-on B. Keep the condition; the price is a detail.
- "Patient players" in Add-on A.

Merge:
- R1 and R1' into one result with two cases (threats stick or they do not).
- R3 into R1 as its interpretation, with one added sentence the design lacks: splitting k into separate threats for separate demands does not raise the total, because carrying out one threat raises Europe's walk-away value by the amount withdrawn (Figure 3, panel (b)). That is the non-obvious part of the paper's one-budget result.
- Add-on A's two channels into the single X, Y formula of 1.6(b).

Rename: see section 3. Use one symbol for the key quantity (or none, by writing c - k throughout), and do not introduce q unless Add-on B needs period subscripts.

On the add-ons:
- **Add-on A: keep, shortened to one paragraph.** Without it the core is open to the objection in 1.1. The objection gets its answer here: being needed pays only when stalled talks hurt Washington and Europe sometimes names the terms. Use the merged formula, state the timing condition, and add the claw-back caveat.
- **Add-on B: shorten to one paragraph with one condition.** The preventive-control result is the paper's most distinctive policy claim and ties to the Europe 2031 hook, so it is worth a paragraph. A full two-period model is not. State the assumption from 1.7 and drop T* and delta.

The resulting model has three numbers in the core (c, k, V), two results, one extension with three more (beta, X, Y) and one with one more (s). The design has eleven symbols.

### Proposed revised minimal model

Numbers (Europe's payoff units, relative to the status quo in which Europe stays with Washington and no one pays):
- c >= 0, China's offer: what China's offer is really worth to Europe if it switches, after discounting promises Europe doubts and the part of China's gain that US legal reach would block anyway.
- k >= 0, Washington's penalty: what Washington would really cut off if Europe switched (on the paper's reading mainly US parts and staff for ASML and access to frontier AI, with the loyalty-tied part of security support). Help Washington would give a switched Europe anyway is not in k.
- V > 0, Washington's need: what Washington loses if Europe switches.
- Europe's walk-away value is c - k. When negative, k - c is Washington's squeeze room.

Rules: Washington names a deal t (t > 0: it pays Europe; t < 0: Europe makes concessions costing it -t). Failed talks cost no one anything, so Washington can refuse any European counter-demand and come back with its own offer, and letting Washington name the deal is only a shortcut for that. Washington may back the deal with a public threat: if Europe refuses, it cuts off k. A Europe that has been cut off has nothing more to lose by switching, so it can take China's offer, and Washington must match c or let Europe go. Either way Europe ends with c - k.

Result 1 (price and squeeze). Europe can always secure c - k. If Washington's threat does not stick, it pays max{0, c - k}. If it sticks, Washington offers exactly c - k: it pays when c > k and takes concessions worth k - c when c < k. Washington keeps Europe if and only if c - k <= V, so V decides whether Washington pays, not how much.

Result 2 (one budget). Because Europe can always walk away with c - k, no combination of demands and threats takes more than k - c in total. Separate threats for separate demands do not add up.

Extension A (when need pays). If each round of stalled talks costs Washington X and Europe Y (from a servicing stoppage, or from the chance that talks collapse into realignment, which is where V enters), and Europe names the terms a share beta of the time, Europe gets the larger of c - k and beta X - (1 - beta) Y. A stoppage counts only if Europe chooses it before offers and cannot lift it after rejecting one. Washington's credible threats can take the gain back down to c - k.

Extension B (control). Suppose c - k is negative today and will be positive tomorrow, and Washington has nothing else it values to spend today's squeeze on. Washington then demands control of ASML, and Europe accepts, if and only if today's squeeze room exceeds s, the sovereignty cost to Europe of handing over control. The handover only saves Washington payments, so s is a pure loss.

Optional sentence (conditionality): Washington chooses k, and because tying support to loyalty costs it trust with other allies, it pushes k past c only if it has demands to spend the extra squeeze on.

## 3. Plain-language names and statements

| Symbol | Paper's term | Proposed plain name | One-line gloss |
|---|---|---|---|
| c | omega, China's credible offer | China's offer | what China would really give Europe for switching, after discounting promises Europe doubts |
| k | c (credible cost of exit), conditional parts d_j | Washington's penalty | what Washington would really cut off if Europe switched |
| u | unconditional part u(J) | (drop) help Washington gives anyway | support Washington would give even a Europe that had switched |
| V | V, US loss from exit | Washington's need | what Washington loses if Europe switches and China gets the tools |
| c - k | exit premium Q | Europe's walk-away value | how much better off Europe would be switching sides, all things counted |
| k - c (if positive) | slack Lambda | Washington's squeeze room | the most Washington can extract with threats |
| s | sigma, sovereignty cost | cost of surrender | what handing over control of ASML costs Europe politically |
| x | (1 - h) c_S, US cost of interruption | Washington's stoppage cost | what Washington's own fabs lose each round ASML stops servicing them |
| y | ell, Europe's cost of interruption | Europe's stoppage cost | what Europe loses each round it stops servicing (lost sales, US retaliation) |
| beta | beta, Europe's proposal probability | Europe's say | the share of the time Europe gets to name the terms |

Use "Washington's need" only for V and "stoppage cost" for x; the two must not share a name (1.6(a)). If the merged formula is used, X and Y are "the cost of stalled talks" to Washington and to Europe.

Plain statements:

**Europe is paid for its alternative, not for being needed.** Europe's bargaining strength is its walk-away value: what China would really give it for switching sides, minus what Washington would really take away. Washington never has to pay more than that. If Europe asks for more, Washington can say no and wait, and Europe can do no better than switch, which is worth only its walk-away value. How badly Washington needs ASML decides only whether Washington would rather pay or let Europe go. Need can still help Europe indirectly, by making China bid more and by making Washington reluctant to punish a firm it depends on.

**Threats work only on the downside.** When Europe's walk-away value is positive, Washington must pay it, threats or no threats. When it is negative, a Washington that cannot make its threats stick pays nothing and gets nothing. A Washington that can make them stick goes further and extracts concessions up to the squeeze room. It cannot extract more, because carrying out a threat to cut Europe off also frees Europe to take China's offer.

**Only what Washington would really cut off counts.** Europe depends on the United States for a great deal, but its walk-away value counts only the part Washington would actually withdraw if Europe switched. Protection Washington would give Europe anyway, for its own reasons, does not enter, however large it is. On the paper's reading, US legal reach over ASML's parts and staff, and access to frontier AI, weigh more in that part than troops do.

**Washington's squeeze room is one budget.** Export controls, limits on servicing Chinese fabs, tariff cuts and arms purchases all draw on the same squeeze room, so a concession Washington wins on one issue leaves less to win on the others. This explains why Europe complies with some demands and resists others. Splitting its threats across issues does not help Washington: once it carries out one, Europe has less left to lose by switching, and the remaining threats bite less.

**Being needed pays only when stalled talks hurt Washington and Europe has a say.** Stalled talks can hurt Washington in two ways. Europe can stop servicing the machines in Washington's own fabs, or a breakdown can tip Europe toward China without either side choosing it. Then the more often Europe names the terms, the more it collects. A stoppage helps only if Europe decides on it before offers are made and cannot lift it after rejecting one. The EU's present rules let it suspend countermeasures quickly, so on the paper's reading a stoppage threat is not believable today. Whatever Europe wins this way, a Washington with credible threats can claw back.

**A shrinking squeeze room invites a demand for control.** Washington's squeeze room lasts only as long as Europe's alternative stays poor. If Washington expects that alternative to improve, and has nothing better to spend today's squeeze on, it has a reason to use the squeeze now to take control of ASML, so that it never has to pay later. It does so when today's squeeze room exceeds what surrender would cost Europe. The handover costs Europe sovereignty and only saves Washington payments, so it destroys value, as preventive war does.

## 4. One figure

**Figure M1. What Europe gets for ASML.** One panel, illustrative units, V = 3.

- Horizontal axis: "Europe's walk-away value, c - k", from -3 to 5, with the tick at 0 labelled "c = k".
- Vertical axis: "What Washington pays Europe (below zero: concessions Europe makes)", from -3 to 4.
- Solid dark line, "Washington's threats stick": payment = c - k, the 45-degree line from (-3, -3) to (3, 3).
- Dashed line, "Washington's threats do not stick": payment = max{0, c - k}, flat at zero from -3 to 0, then on the solid line to (3, 3). Offset it by a line width where the two coincide, or note "lines coincide" in a small label.
- Light fill in the triangle between the two lines for c - k < 0 (vertices (-3, 0), (0, 0), (-3, -3)), labelled "Washington's squeeze room, k - c: one budget for every demand".
- Vertical dotted line at c - k = V = 3, labelled "Washington's need, V". Pale grey fill to its right, labelled "Washington lets Europe go".
- A second, fainter vertical dotted line at 4.5, labelled "greater need", with a short horizontal arrow from 3 to 4.5 along the top edge and a faint extension of both payment lines from 3 to 4.5. Annotate: "More need moves only where Washington stops paying. It does not raise the line."
- Optional reference: a faint grey horizontal line at payment = V = 3 across the whole range, labelled "If being needed were leverage (Europe names the terms and stalled talks mean realignment)". This is the paper's corner beta -> 1, lambda -> infinity (Corollary 1, nesting). It shows the reader the view the paper rejects. Drop it if the panel is crowded.

Caption: "Europe is paid its walk-away value, not its importance. Washington's need V decides only where Washington stops paying and lets Europe go. Below zero, Washington's credible threats let it extract concessions up to the squeeze room, and every demand draws on that room."

The figure carries Result 1, the downside-only role of threats, the one-budget result and the irrelevance of V in one picture. It is the lambda = 0 curve of the paper's Figure 2 with the squeeze line added, so it stays consistent with the paper. I would not mark where Europe sits today on the axis. The paper's claim that the premium has been negative since 2019 is a reading, not a measurement, and a dot on a chart would overstate it.

## Checks behind this critique

Four brute-force checks (100,000 random draws each, numpy-free Python): (1) the rewrite of Proposition 6's constant-cost x0 as beta X - (1 - beta) Y, maximum error 2.7e-15; (2) with ordinary concessions valued at par, control never beats the plain squeeze, and the gap is exactly s; (3) under a standoff value N, a credible conditional cut of k bites min{k, max(0, N - (c - k))}; (4) Europe's take under a credible threat, max{0, c} - k, equals the paper's max{0, Q} - min{d, slack}, maximum error 0. Checks (2) and (3) concern claims the paper does not state, so they should be proved before any of this goes into the paper itself.
