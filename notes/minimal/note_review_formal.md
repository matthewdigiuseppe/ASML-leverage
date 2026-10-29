# Formal review of paper/minimal/minimal_model.tex

Checked against `notes/minimal/verify.md`, `notes/minimal/critique.md`, `paper/sections/*.tex` and the printed numbers in `paper/main.aux` / `paper/main.pdf` (compiled 29 Oct 2026, 10:32; the note's PDF is newer than its .tex, so it is current). The note was not edited.

## Summary verdict

The formal core is right. Every formula in the appendix holds:
- Proposition 1: the payment is $q$ with commitment and $[q]^+$ without. The $c=0$ knife edge is stated correctly in the appendix.
- Proposition 2: the bundle condition $t-\sum d_i\ge q$ and the bound $[-q]^+$.
- The X, Y rewrite of Proposition 6: I checked the identity $\beta X-(1-\beta)Y=\psi[q+\beta(V-q)]+(1-\psi)[\beta x-(1-\beta)y]$ numerically, with a maximum error of 1.8e-15 in 100,000 draws.
- The one-line Rubinstein derivation, $T^*$, $\Gamma$, and the $\alpha$ condition. I re-derived the $\alpha$ condition by hand: the two-case comparison with the plain squeeze reduces exactly to the two stated inequalities.

The cross-references are also right, with one exception. Lemma 1, Proposition 2(a), Proposition 5 with its special case (printed directly after it, before Corollary 3) and Proposition 6 ("Pain and rupture", the hold-up result) all match main.aux. The exception is that the sequential-demand result is Proposition 2(d), not (c).

The problems are in the plain-language layer:
- The abstract states a false necessary condition for being needed to pay.
- Section 3 says piecemeal demands always get less, which contradicts the note's own appendix and Proposition 2(d).
- Proposition 3 leaves out that the threat must stick.
- The conditionality section turns Proposition 4's case-dependent results into unconditional claims.

**Check script.** `python3 -I code/checks/minimal_model_check.py` ran in 71.9 s with exit code 0. It printed 25 PASS lines and "Failures: 0", which matches the note's "all 25 checks pass". The script does not check the X, Y identity, so I checked it separately (above).

## Findings

### 1. Abstract: false necessary condition (essential)

**Anchor:** "Washington's need for ASML matters only if stalled talks hurt Washington, Europe has a say in the terms, and Europe can tie its own hands."

**Problem:**
- Through the collapse channel ($\psi>0$), $V$ enters Europe's payoff with weight $\beta\psi$ (Proposition 1; Corollary 1(e)), and no hand-tying is needed. The commitment condition applies only to a servicing stoppage (Corollary 5, variant (b)).
- The abstract leaves out the condition that Section 4 lists third: credible threats can claw the gain back (Remark 1).
- "Matters only if" also ignores the indirect channels through China's offer and Washington's penalty. The note's last section mentions them (Corollary 1(e); verify.md, suggested edit 5).

**Replacement:** "Washington's need for ASML raises Europe's price directly only if stalled talks hurt Washington, Europe has a say in the terms, and Washington cannot claw the gain back with threats; a stoppage of servicing adds to Europe's price only if Europe can tie its own hands."

### 2. Section 3: "only by" and "get less" overclaim (important)

**Anchor:** "Washington reaches the full budget only by making all its demands at once. Piecemeal demands get less, because a Europe that expects more demands to follow its concessions has less reason to make them \citep{pauly2024damned}."

**Problem:** Proposition 2(d) of the paper says that without commitment Washington still obtains the single-ultimatum value in two cases: when all demands are reversible and $B(J^c)\ge\Lambda$, which always holds in the minimal model since $B=\Lambda$; or when a best single ultimatum contains all its demands. With $n\le b$ identical sunk demands, piecemeal gets all $n$. Piecemeal *can* get less ($n \bmod (b+1)$ of them), and the note's own appendix says exactly that ("can get strictly less"). The main text contradicts it.

**Replacement:** "Washington is sure of the full budget only if it makes all its demands at once. Piecemeal demands can get less, because a Europe that expects more demands to follow its concessions has less reason to make them \citep{pauly2024damned}."

### 3. Appendix: wrong part of Proposition 2 cited (important)

**Anchor:** "This is Proposition~2(b)--(c) of the full paper."

**Problem:** In main.pdf, Proposition 2(c) ("One budget") gives the bound in every SPE of adaptive sequences. The finding that piecemeal demands can yield strictly less, with the $n \bmod (b+1)$ example, is Proposition 2(d) ("Assurance"). verify.md's "(c)(iii)-(iv)" uses an older lettering.

**Replacement:** "This is Proposition~2(b)--(d) of the full paper: the bundle condition is part (b), the bound for any sequence of demands is part (c)(i), and the shortfall of piecemeal demands is part (d)."

### 4. Proposition 3: missing condition that the threat sticks (important)

**Anchor:** "Suppose Europe's walk-away value is negative today and will be positive tomorrow, and Washington has nothing else it values to spend today's squeeze on."

**Problem:** The result needs the period-1 threat to be credible. In the paper's special case, $B_1=0$ if the threat is not credible, so $\Gamma=\min\{\delta[Q_2]^+,-\sigma\}\le0$ and control is never demanded. The appendix assumes the threat is carried out ("threatens to cut $k_1$"), but the proposition does not say so. Proposition 1 does distinguish the two cases, so readers will expect the distinction here too.

**Replacement:** "Suppose Europe's walk-away value is negative today and will be positive tomorrow, Washington's threat sticks, and Washington has nothing else it values to spend today's squeeze on."

The appendix could also add after "handing over control costs Europe $s\ge 0$": "control is permanent and Washington values it only for the payments it saves (the paper's $\Delta_c=\infty$, $v_c=0$)".

### 5. Abstract: missing control caveat (important)

**Anchor:** "When Europe's position is set to improve, Washington has a reason to demand control of ASML while it can still squeeze."

**Problem:** By the note's own $\alpha$ result, a Washington that can cash the squeeze in concessions worth as much to it as they cost Europe never demands control. The condition "nothing else it values to spend today's squeeze on" is essential, and verify.md (Add-on B) asks for it in the plain-language line. The threshold ($k-c>s$) is also missing.

**Replacement:** "When Europe's position is set to improve and Washington has nothing better to spend its squeeze on, Washington has a reason to demand control of ASML while it can still squeeze, if the squeeze exceeds what surrender would cost Europe."

### 6. Section 4: the three conditions are not parallel (important)

**Anchors:** "Being needed pays only under three conditions." and "Third, for the collapse channel the full paper shows that a Washington with credible threats can take the gain back down to Europe's walk-away value."

**Problem:**
- The second condition (timing) applies only to the stoppage channel, so it is not necessary for the collapse channel.
- The third is stated as a result, not a condition.
- Remark 1 lets credible conditional threats claw back down to the exit premium only if they are large enough. The bound holds with equality only when the outside option binds after the withdrawal ($Q+d(J)\ge\hat Q$, with $r>0$). In the paper's own example, $Q=-1$, $d=3$ costs Europe 1.8, not the full 2.2.

**Replacements:**
- "Being needed pays only under three conditions." becomes "Being needed pays only if Europe has a say and Washington cannot take the gain back; a stoppage also needs the right timing."
- "Third, for the collapse channel the full paper shows that a Washington with credible threats can take the gain back down to Europe's walk-away value." becomes "Third, Washington must lack credible threats large enough to push Europe back to its walk-away value: for the collapse channel the full paper (Remark~1) shows that such threats take the gain back."

### 7. Conditionality section: case-dependent results stated as unconditional (important)

**Anchors:** "A Washington that wants nothing beyond alignment ties just enough support to hold Europe's walk-away value at zero." and "A stronger Chinese offer is therefore met with more strings attached to American protection, not with money."

**Problem:**
- Proposition 4(a), with $\nu=0$, gives $\kappa^*=\kappa_0$ when the premium is already at or below zero, so Washington does not loosen ties to bring the walk-away value up to zero.
- When the premium is positive, Proposition 4(a) gives $\min\{\kappa_z,\kappa_1,\bar\kappa\}$: Washington stops short of zero if assurance becomes too costly first. The paper says "or less if assurance becomes too costly first".
- "Not with money" is Proposition 4(c)(i) only, the case where assurance is cheap at the margin. Under (c)(ii) and (c)(iv), the rent rises one for one with China's offer.

**Replacements:**
- "A Washington that wants nothing beyond alignment ties at most enough support to bring Europe's walk-away value down to zero, and stops short if the lost trust becomes too costly first."
- "While tying more support costs Washington little in trust, a stronger Chinese offer is therefore met with more strings attached to American protection, not with money."

### 8. Proposition 1: tie at $c-k=V$ (minor)

**Anchor:** "Either way, Washington keeps Europe if and only if $c-k\le V$."

**Problem:** At $c-k=V$, Washington is indifferent and both outcomes are SPE (verify.md R1; the script's edge case "c-k=V"). The appendix says so; the statement does not.

**Replacement:** "Either way, Washington keeps Europe if $c-k<V$ and lets it go if $c-k>V$; at $c-k=V$ it is indifferent."

### 9. Proposition 1: knife edge in the no-commitment case (minor)

**Anchor:** "If the threat does not stick, Washington pays $\max\{0,c-k\}$."

**Problem:** This needs $c>0$, or a positive cost to Washington of cutting a loyal Europe. At $c=0$ with a costless cut, SPE payments range over $[-k,0]$ (verify.md R1'). Only the appendix says this.

**Replacement:** "If the threat does not stick, Washington pays $\max\{0,c-k\}$ (when $c>0$; the appendix treats $c=0$)."

### 10. The rule: rematch not in the formal game (minor)

**Anchor:** "and Washington must match $c$ or let Europe go."

**Problem:** The formal game in the appendix has no rematch after a cut: Europe simply stays ($-k$) or switches ($c-k$). The rematch is the paper's replayed contest (Proposition 2 assumes "the United States retains Europe after every history"). Europe's payoff is $c-k$ either way, so nothing changes, but the rule and the appendix describe different games.

**Fix:** Add to the appendix proof of Proposition 1, after "switching gives $c-k$": "(If Washington could instead pay Europe $c$ to stay after a cut, as in the paper's replayed contest, Europe would still get $c-k$.)"

### 11. Section 4: "each round" is the wrong unit (minor)

**Anchor:** "Suppose instead that each round of stalled talks costs Washington $X$ and Europe $Y$"

**Problem:**
- The formula $\beta X-(1-\beta)Y$ holds for costs that are flows per unit of time. If costs are fixed per round, the take is $(\beta x-(1-\beta)y)/(1-\delta)$, which has the same sign but is not the same value (the script's check "costs fixed per round").
- The collapse component $\psi V$ is a hazard-weighted average, not a per-round cost.

**Replacement:** "Suppose instead that stalled talks cost Washington $X$ and Europe $Y$ for as long as they last"

### 12. Section 4: lifting the stoppage (minor)

**Anchor:** "A stoppage Europe would call off at Washington's first offer is never used."

**Problem:** The paper's variant (b) is a stoppage that Europe can lift *after rejecting* an offer. "Never used" holds in Markov equilibria and in finite truncations, not in every SPE of the infinite game (verify.md, Add-on A, Timing; the paper cites Fernandez and Glazer).

**Replacement:** "A stoppage Europe could lift after rejecting an offer is never used, at least in the equilibria the paper studies."

The appendix's "so the stoppage is never used" should get the same qualifier: "(in every Markov equilibrium)".

### 13. Appendix, hold-up paragraph: timing, Corollary 5 and Remark 1 (minor)

**Anchor:** "Europe's payoff is $\max\{q,\ \beta X-(1-\beta)Y\}$, which is the full paper's Proposition~6 with constant costs rewritten:"

**Problem:**
- Proposition 6 needs $r>0$.
- The formula takes the stoppage as in force. The timing results are Corollary 5 and its variants, which the note does not cite.
- If Europe can decide after learning that it proposes, $y$ drops out and it gets $\beta x$ (verify.md A; Corollary 5, variant (c)).

**Replacement:** "Europe's payoff is $\max\{q,\ \beta X-(1-\beta)Y\}$ when the stoppage is set before Europe learns who proposes ($r>0$; Markov perfect equilibrium), which is the full paper's Proposition~6 with constant costs rewritten (the timing variants are Corollary~5 and the text after it; a Europe that chooses after learning it proposes gets $\beta x$):"

**Further fix:** Replace "the full paper's remark on slack under rupture risk" with "the full paper's Remark~1 (slack under rupture risk)", since main.aux prints it as Remark 1.

### 14. Title-page footnote overclaims (minor)

**Anchor:** "Every result is a special case of a result proved in the full paper"

**Problem:**
- The $\alpha$ condition at the end of the appendix is not in the paper. The critique says it needs proof before it goes into the paper; the note's script verifies it.
- When $c-k>V$, Lemma 1 gives Europe $\min\{V,\bar m_U\}$ (China bids), while the minimal model gives $c-k$ (fixed offer; verify.md, "Consistency with the paper").

**Replacement:** "Every numbered result is a special case of a result proved in the full paper (with China's offer fixed rather than bid)"

### 15. "What this note leaves out": reading of the record overstated (minor)

**Anchor:** "The paper's reading of the record finds that US legal reach over ASML's parts and staff, and the threat to withhold frontier AI, weigh more in Washington's penalty than troops do,"

**Problem:** Section 8 says two narrower things:
- The record is "consistent with" a jurisdictional source of slack, and that source works partly through China's offer ($\theta$), not only through the penalty.
- The AI term is "likelier than the core guarantee to decide the sign of $Q$" only "if Washington's AI threat is credible".

**Replacement:** "On the paper's reading of the record, US legal reach over ASML's parts and staff, which both shrinks China's offer and adds to Washington's penalty, is enough on its own to keep Europe's walk-away value negative, and the threat to withhold frontier AI, if credible, is likelier than troops to decide its sign,"

### 16. Europe's own reluctance ($\eta$) dropped silently (minor)

**Anchor:** "Each threat has to be credible on its own terms."

**Problem:** The paper's cost of exit includes $\eta$, Europe's own reluctance to switch, which Washington cannot withdraw. With $\eta>0$, the squeeze room is capped at $k$, not at $k-c+\eta$ (critique 1.3).

**Replacement:** Append after the anchor: "Europe's own reluctance to arm a rival that backs Russia's war lowers its walk-away value, but Washington cannot withdraw it, so the squeeze can never exceed $k$."

### 17. Abstract and figure caption: "Europe is paid its walk-away value" (minor)

**Anchors:** "Europe is paid its walk-away value, the first number minus the second, and not its importance to Washington." (abstract) and "Europe is paid its walk-away value, China's offer minus Washington's penalty, and not its importance to Washington." (caption)

**Problem:** When the value is negative and threats do not stick, Europe is paid zero, which is the dashed line in the figure.

**Replacement (abstract):** "Europe's price is set by its walk-away value, the first number minus the second, and not by its importance to Washington."

**Replacement (caption):** "Europe's price is set by its walk-away value, China's offer minus Washington's penalty, and not by its importance to Washington."

### 18. Definition of $x$ is wider than the paper's (minor)

**Anchor:** "which costs those plants something every round (call it $x$)"

**Problem:** In Corollary 5, Washington's cost is $(1-h)c_S$, after the buffer: only the servicing Washington cannot compel ASML's US staff to continue. The paper puts $h$ near one on US soil, so $x$ as worded overstates Europe's hold-up power.

**Replacement:** "which costs those plants whatever servicing Washington cannot force ASML's US staff to keep doing (call it $x$)"

## Checked and correct (no change)

- **Appendix, Proposition 1.** Refusal payoff $\max\{-k,c-k\}=q$ using $c\ge0$. No-commitment logic. Knife edge. Lemma 1 plus Proposition 2(a), with bite $\min\{k,[-q]^+\}=[-q]^+$ (valid because $c\ge0$).
- **Appendix, Proposition 2.** Single-bundle condition. Reversible demands, with the excess repaid (Proposition 2(b)). Bound under sequential demands.
- **X, Y and the identity.** $X=\psi V+(1-\psi)x$ and $Y=\psi(k-c)+(1-\psi)y$ reproduce Proposition 6(iii) with constant costs, $P^*=\max\{Q,x^\circ\}$, with $c_U=x$ and $c_E=y$. The "one line" recursion and $v=\beta x-(1-\beta)y$ are exact for every round length.
- **Appendix, Proposition 3.** $T^*=[q_1+\delta[q_2]^++s]^+$ and $\Gamma=\min\{[q_1]^++\delta[q_2]^+,[k_1-c_1]^+-s\}$. Positive iff $q_2>0$ and $k_1-c_1>s$ (needs $\delta>0$, stated; strict tie rule, stated). This matches the paper's special case $\Gamma=\min\{\delta[Q_2]^+,B_1-\sigma-r^c\}$ with $B_1=[k_1-c_1]^+$, $u_1=0$, $r^c=0$. The $\alpha$ condition and the $\alpha=1$ corollary are correct.
- **Printed numbers.** Lemma 1 (lem:bidding), Proposition 2 (prop:slack), Proposition 5 and the special case after it (prop:control), Proposition 6 (prop:pain, Hold-up) and Remark 1 (rem:rupture) all match main.aux.
- **Main-text claims.** "Threats matter only on the downside", "Washington's need ... does not raise the price" (within the rule), splitting threats across issues does not help (Figure 3(b)), and the $\beta=0$ claim (V and $x$ drop out). All agree with the formal statements.
