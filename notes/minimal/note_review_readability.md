# Readability and style review: minimal-model note

Reviewed: `paper/minimal/minimal_model.tex` (compiled `minimal_model.pdf`, 7 pages) and its figure (`fig_minimal.pdf`, from `make_minimal_figure.py`). Reader assumed: knows international politics, not game theory. House style: `notes/v2/style_brief.md`. The note itself was not edited.

All anchors below are exact strings from `minimal_model.tex` (line numbers from the source) unless marked as coming from `make_minimal_figure.py`.

## Verdict

The main point comes through. The abstract, Proposition 1, the paragraph after it and the figure all say the same thing: Europe is paid its walk-away value (China's offer minus Washington's penalty), and Washington's need decides only whether Washington pays or lets Europe go. The paragraph that begins "Carrying out the threat frees Europe" gives a non-specialist the reason in plain words, and the record paragraph on servicing and the MATCH Act shows the one-budget idea at work.

Four things blur it:

1. The word that splits Proposition 1 and the figure into two cases, a threat that "sticks", is never defined. The note also swaps between "sticks", "credible" and "committed".
2. The note asks a question in Section 1 ("why has Europe got so little for it?") and never answers it in one sentence.
3. The abstract and Section 4 disagree on when being needed pays.
4. Section 5 never says why control stops Washington's future payments, which is the whole mechanism.

The prose is mostly short and concrete. Burstiness (stdev/mean of sentence length in the body, appendix excluded) is about 0.56, above the 0.5 target. There are no em dashes. The main house-style problems are five negative parallelisms, five pieces of meta-commentary, two impersonal hedges, the main verdict repeated almost word for word in the abstract, Section 3 and the figure caption, and dated facts in Sections 1, 3, 4 and 7 that carry no citation although the keys exist in `refs.bib`.

The figure carries the price-and-squeeze result. It does not show that more need leaves the price where it is, which is the half of the headline that cuts against *Europe 2031*. One label also collides with the payment line.

## Findings, most severe first

### 1. [essential] "Sticks" is undefined and has three names

- Anchor (l.43): `If Washington's threat sticks, it offers exactly $c-k$`
- Also (l.34): `and it can back the deal with a public threat to cut off $k$ if Europe refuses.`
- Problem: Proposition 1, the paragraph after it and both lines in the figure turn on whether a threat "sticks". The word first appears inside the proposition with no definition. A reader cannot tell whether it means "is believed", "is carried out" or "works". The rule paragraph makes every threat "public", which reads as if every threat sticks, so the "does not stick" case seems to have no place in the rule. The note then calls the same thing "credible" (caption l.51, l.71, l.89) and "committed" (appendix l.101).
- Replacement: in l.34 write `and it can back the deal with a threat to cut off $k$ if Europe refuses.` After "Europe accepts or refuses." insert: `We say the threat \emph{sticks} if Washington has bound itself to carry it out after a refusal, for instance by making it public at a cost it cannot walk back. A threat that does not stick leaves Washington to decide afresh, after a refusal, whether cutting Europe off is worth it.` Then use "sticks" everywhere. Caption: `credible threats let Washington` becomes `threats that stick let Washington`. l.71: `a Washington with credible threats` becomes `a Washington whose threats stick`. l.89: see finding 30. Appendix l.101: `\emph{With a committed threat:}` becomes `\emph{With a threat that sticks:}` and `\emph{Without commitment:}` becomes `\emph{With a threat that does not stick:}`.

### 2. [important] The question in Section 1 is never answered, and the section ends in meta-commentary

- Anchor (l.20): `The full paper answers with a model of many parts. This note keeps only what is needed for the main answer.`
- Problem: Section 1 ends on a well-posed puzzle ("If Washington needs ASML so badly, why has Europe got so little for it?"). The next two sentences talk about the note instead of answering it, and they repeat the abstract's first sentence. Nowhere does the note say plainly that, on the authors' reading, Europe's walk-away value has been negative, so Washington has paid nothing and taken export controls instead. An IR reader has to assemble this from Proposition 1 and the record paragraph. (The full paper makes this claim in its introduction and Section 8. `critique.md` §4 warns against marking it as a point on the chart; it fits in the text as long as it is hedged.)
- Replacement: replace l.20 with `Our answer is that Europe is paid for what it could get by switching sides, net of what it would lose, and on our reading that number has been negative since 2019.` After `\Cref{fig:minimal} shows both cases.` (l.46) add: `On our reading this is the Dutch case since 2019: China's offer, net of what US legal reach would block, has been worth less to Europe than what Washington would cut off, so Washington has paid nothing and taken export controls instead.`

### 3. [important] The abstract states different conditions for "being needed pays" than Section 4

- Anchor (l.13): `Washington's need for ASML matters only if stalled talks hurt Washington, Europe has a say in the terms, and Europe can tie its own hands.`
- Problem: Section 4 gives a different list: Europe has a say, a stoppage is fixed in advance, and Washington's threats do not stick (the claw-back). The abstract leaves out the claw-back. It also makes hand-tying a condition for need to matter, but in Section 4 need ($V$) enters only through the risk that talks collapse, and that channel needs no hand-tying. Hand-tying matters only for a servicing stoppage, which works through $x$, not $V$.
- Replacement: `Washington's need raises Europe's price only if stalled talks risk a realignment neither side chose, Europe sometimes names the terms, and Washington's threats do not stick. A halt to servicing adds to the price only if Europe can tie its own hands.`

### 4. [important] Section 4's "third condition" is not a condition, and the paragraph mixes the two channels

- Anchor (l.71): `Third, for the collapse channel the full paper shows that a Washington with credible threats can take the gain back down to Europe's walk-away value.`
- Problem: the sentence announces a third condition but states a result. The reader has to work out that the condition is "Washington's threats must not stick". The second condition (hand-tying) applies only to a stoppage, and the third is proved only for collapse, but the paragraph presents all three as conditions for "being needed". "Collapse channel" is new jargon; the paragraph before it speaks of "two things", not channels. The European Union sentence runs to 38 words.
- Replacement for the paragraph (l.71):
  `Being needed pays only under three conditions. First, Europe must have a say: if Washington always names the terms ($\beta=0$), Europe's power to hurt is worth nothing. Second, Washington's threats must not stick. The full paper shows that a Washington whose threats stick can take the gain from collapse risk back down to Europe's walk-away value. We expect the same for a stoppage but have not proved it. Third, a stoppage counts only if Europe ties its own hands, setting it before offers are made with no way to lift it after rejecting one. Europe would lift a stoppage it was free to lift as soon as it rejected an offer, so Washington would ignore it. The European Union's tools are built the other way. They let Brussels suspend countermeasures at once but escalate only slowly. Twice in 2025 member states approved countermeasures against Washington and then suspended them as soon as Washington moved \citep{commission2025suspension786, commission2025suspension1727}.`

### 5. [important] Section 5 does not say why control ends Washington's payments

- Anchor (l.81): `Washington uses the squeeze while it still has one, to avoid paying Europe later.`
- Problem: the reader is told that control saves Washington future payments but not why. The missing step is that once Washington controls ASML, Europe has nothing left to sell China, so its walk-away value tomorrow no longer matters. The preventive-war comparison (`much as preventive war does.`) is apt for an IR reader, but the note leaves the shared logic unstated.
- Replacement for the first two sentences of l.81: `Once Washington controls ASML, Europe has nothing left to sell China, so Washington never has to pay the positive walk-away value Europe will have tomorrow. Washington spends today's squeeze room to buy that. The handover costs Europe sovereignty and saves Washington only payments, so it destroys value. Like a preventive war, it is a costly move the stronger side makes now because its advantage is about to shrink.`

### 6. [important] Section 6 overstates the full paper and seems to contradict Proposition 1

- Anchor (l.85): `A stronger Chinese offer is therefore met with more strings attached to American protection, not with money.`
- Problem: Proposition 1 has just said Washington pays $c-k$ when China's offer exceeds the penalty. Section 6 now says Washington does not pay, with no bridge between the two. The full paper's claim is conditional. Proposition 4(c)(i) (`sections/05_slack.tex` l.109, l.120) holds "when assurance is cheap at the margin"; otherwise Washington pays rent. The note drops that condition. The sentence is also a negative parallelism. The earlier sentence `A Washington that wants nothing beyond alignment ties just enough support to hold Europe's walk-away value at zero.` drops the full paper's "or less if assurance becomes too costly first".
- Replacement: open the section with `\Cref{min:price} takes the penalty $k$ as given.` Change the middle sentence to `A Washington that wants nothing beyond alignment ties just enough support to hold Europe's walk-away value at zero, or less if the lost trust becomes too costly first.` Replace the last sentence with `While the lost trust is cheap at the margin, Washington answers a stronger Chinese offer by tying more of its protection to Europe's loyalty, just enough to bring the walk-away value back to zero, and pays nothing. Once the lost trust is costly, it pays.`

### 7. [important] The figure does not show that more need leaves the price unchanged

- Anchor (caption, l.51): `Washington's need $V$ (here $3$) decides only where Washington stops paying and lets Europe go.`
- Problem: the headline claim rests on a comparison, need versus price, that the figure does not draw. With one value of $V$ the reader sees a cutoff, not that a larger $V$ would leave the line where it is. The design in `critique.md` §4 asked for this comparison and the figure leaves it out.
- Replacement (in `make_minimal_figure.py`): add a fainter dotted line at 4.5, faint extensions of both payment lines from 3 to 4.5, a short arrow from 3 to 4.5 near the top, and the label `More need moves only where Washington stops paying.\nIt does not lift the line.` For example: `ax.axvline(4.5, color=MUTED, lw=0.6, ls=(0,(1,3)), alpha=0.6)`; `x2=np.linspace(V,4.5,50); ax.plot(x2,x2,color=BLUE_DARK,lw=1.2,alpha=0.35)`; `ax.annotate("", xy=(4.5,3.5), xytext=(V,3.5), arrowprops=dict(arrowstyle="->", color=TEXT2, lw=0.7))`. Move "Washington lets Europe go" to the right of 4.5, or shade only beyond the larger value with a lighter grey.

### 8. [important] Figure label collides with the payment line, and the squeeze room reads as an area

- Anchor (`make_minimal_figure.py` l.30): `ax.text(-2.95, -0.75, "Washington's squeeze room, $k-c$:\none budget for every demand"`
- Problem: at print size the solid diagonal runs through the label at "room," and at "demand" (page 3 of the PDF). The shaded triangle also invites the reader to read the squeeze room as an area. It is a vertical distance at a given walk-away value.
- Replacement: move the label into the empty lower-right quadrant with a leader line, for example `ax.annotate("Washington's squeeze room, $k-c$:\none budget for every demand", xy=(-1.0,-0.5), xytext=(0.35,-1.9), color=BLUE_DARK, fontsize=8, arrowprops=dict(arrowstyle="-", color=BLUE_DARK, lw=0.6))`. Then add a vertical double arrow at $c-k=-2$: `ax.annotate("", xy=(-2,0), xytext=(-2,-2), arrowprops=dict(arrowstyle="<->", color=BLUE_DARK, lw=0.8)); ax.text(-1.93,-1.1,"$k-c$",color=BLUE_DARK,fontsize=8)`.

### 9. [important] The caption repeats the abstract instead of saying how to read the figure (fractal summary)

- Anchor (caption, l.51): `What Europe gets for ASML. Europe is paid its walk-away value, China's offer minus Washington's penalty, and not its importance to Washington.`
- Problem: the verdict appears almost word for word three times: in the abstract (l.13), in Section 3 (l.46) and here. The caption also uses "importance" and "credible", where the text says "need" and "stick". The style brief bans repeating the same verdict in several places.
- Replacement caption: `What Europe gets for ASML. Each line shows what Washington pays Europe at each walk-away value (China's offer minus Washington's penalty). Payment rises one for one with the walk-away value, whatever Washington's need; $V$ (here $3$) sets only where the lines stop and Washington lets Europe go. Below zero, a Washington whose threats stick takes concessions equal to the squeeze room (shaded), and every demand draws on it; one whose threats do not stick takes nothing. Illustrative units.`

### 10. [important] The key intuition adds a step the model does not have and does not derive $k-c$

- Anchor (l.38): `so its alternative jumps from $c-k$ to $c$, and Washington must match $c$ or let Europe go. That is why a threat to cut Europe off can take at most $k-c$, not $k$.`
- Problem: in the model Washington makes no move after the cut, so "Washington must match $c$" describes a step that does not exist. The reader also has to work out how "match $c$" leads to "at most $k-c$". The plain route is that a refusing Europe can always end up at $c-k$, so no threat pushes it lower. "Alternative" here is a second name for the walk-away value (finding 12).
- Replacement (sentences after `\emph{Carrying out the threat frees Europe.}`): `Once Washington has cut off $k$, Europe has nothing more to lose by switching, and switching gains it $c$. A Europe that refuses can therefore always end up at $c-k$, and no threat can push it lower. A threat to cut off $k$ takes at most $k-c$, not $k$.` (The "not $k$" contrast is legitimate: the negated half is the naive reading of the threat.)

### 11. [important] The abstract coins "shortfall" and leaves out that only threats that stick can squeeze

- Anchor (l.13): `Washington can squeeze Europe up to the shortfall, and every demand it makes draws on that one budget.`
- Problem: "shortfall" never appears again; the body calls this the squeeze room. "That one budget" points back to a budget not yet mentioned. Proposition 1 says only a Washington whose threats stick can squeeze.
- Replacement: `When that value is negative, a Washington whose threats stick can extract concessions up to the gap, its squeeze room, and every demand it makes draws on that single budget.`

### 12. [important] The walk-away value has three names: "walk-away value", "alternative", "position"

- Anchor (l.13): `When Europe's position is set to improve`
- Other instances: l.38 `its alternative jumps`; l.46 `Europe is paid for its alternative`; l.69 `when its alternative is poor`; l.75 `Washington's squeeze room lasts only while Europe's alternative stays poor.`
- Problem: the style brief requires one name per thing. A lay reader may take "alternative" for China's offer $c$, not $c-k$.
- Replacement: l.13 `When Europe's walk-away value is set to turn positive`; l.75 `Washington's squeeze room lasts only while Europe's walk-away value stays negative.`; l.69 see finding 24; l.46 see finding 14; l.38 see finding 10.

### 13. [important] Negative parallelism in the abstract

- Anchor (l.13): `Europe is paid its walk-away value, the first number minus the second, and not its importance to Washington.`
- Problem: the negated half is a real position, *Europe 2031*'s "only card", but the abstract does not name who holds it, as the brief requires. "Importance" is also a second name for "need".
- Replacement: `Europe is paid its walk-away value, the first number minus the second. Washington's need, the card \emph{Europe 2031} says Europe holds, does not raise the price.`

### 14. [important] Negative parallelism opening Section 3's main paragraph

- Anchor (l.46): `Europe is paid for its alternative, not for being needed. Washington's need, $V$, decides only whether Washington would rather pay or let Europe go.`
- Problem: unnamed contrast (see finding 13), plus "alternative" (finding 12).
- Replacement: `Europe is paid its walk-away value. Washington's need, $V$, the card \emph{Europe 2031} counts on, decides only whether Washington would rather pay or let Europe go.` Keep the next sentence, `It does not raise the price.`

### 15. [important] Negative parallelism in Section 2

- Anchor (l.36): `Giving Washington the first move is a shortcut for that fact, not an assumption that it holds every card. \Cref{sec:need} drops it.`
- Problem: the negated half answers an objection no one in the note has raised. "Drops it" has no clear referent (the shortcut? the first move?).
- Replacement: `Giving Washington the first move is a shortcut for that fact. \Cref{sec:need} lets Europe name the terms some of the time.`

### 16. [important] Negative parallelism in the record paragraph

- Anchor (l.61): `On our reading this is a government rationing concessions within a fixed budget, not defying its patron.`
- Problem: nobody is named as reading the Dutch objection as defiance. Delete the negated half and the claim still stands.
- Replacement: `On our reading, the Dutch government is rationing concessions within a fixed budget.`

### 17. [important] Meta-commentary: "One feature ... drives most of what follows"

- Anchor (l.38): `One feature of the rule drives most of what follows.`
- Problem: this is the kind of announcement the brief bans ("Two features matter."). The italic sentence after it does the work on its own.
- Replacement: delete it. Start the paragraph with `\emph{Carrying out the threat frees Europe.}`

### 18. [important] Meta-commentary in Section 5

- Anchor (l.81): `The condition that Washington has nothing better to spend the squeeze on matters.`
- Problem: "X matters" is meta-commentary, and the sentence after it already says why.
- Replacement: delete it, and change the next sentence to `If Washington could instead cash today's squeeze room in concessions worth as much to it as they cost Europe, it would take those and never bother with control.`

### 19. [important] Long sentence and overclaim in the record paragraph

- Anchor (l.61): `The budget explains a pattern in the record that otherwise looks inconsistent. The Netherlands gave way on controls over the sale of new machines, yet as of mid-2026 Dutch and Japanese firms were still servicing machines installed in Chinese plants, and the Dutch cabinet objected when a bill in Congress, the MATCH Act, proposed reaching into allied countries to stop that.`
- Problem: the second sentence runs to 49 words. "Explains" claims more than the brief allows ("the record is consistent with"). Japan is outside the model and distracts. Neither fact is cited, although `zakaria2026match`, `baumgartner2026match` and `tk2026match` are in `refs.bib` and support them in the full paper (`sections/02_background.tex` l.19).
- Replacement: `The budget makes sense of Dutch conduct that otherwise looks inconsistent. The Netherlands gave way on controls over the sale of new machines. Yet as of mid-2026 Dutch firms were still servicing machines installed in Chinese plants \citep{zakaria2026match}, and the Dutch cabinet objected when a bill in Congress, the MATCH Act, proposed reaching into allied countries to stop that \citep{baumgartner2026match, tk2026match}.`

### 20. [important] Impersonal hedge and a 44-word closing sentence

- Anchor (l.89): `The paper's reading of the record finds that US legal reach over ASML's parts and staff, and the threat to withhold frontier AI, weigh more in Washington's penalty than troops do, though how closely American protection is tied to Europe's export controls remains untested.`
- Problem: the brief wants hedges attached to "we", and "remains untested" has no agent. "Troops" is a fourth name for security support (finding 29).
- Replacement: `On our reading of the record, US legal reach over the American parts and staff ASML relies on, and the threat to withhold frontier AI, weigh more in Washington's penalty than American troops do. We have not tested how closely American protection is tied to Europe's export controls.`

### 21. [minor] Dated facts without citations

- Anchor (l.18): `What it received in December 2024, an exemption from new US rules on foreign-made chip tools, is a status Washington can take back by changing a rule.`
- Problem: the brief requires every concrete particular to be cited. Uncited here: December 2024 (l.18), "since 2019" (l.18), mid-2026 servicing and the MATCH Act (l.61, finding 19), "twice in 2025" (l.71, finding 4) and Nexperia (l.89). All the keys are in `refs.bib`.
- Replacement: add `\citep{bis2024fdpr}` after `foreign-made chip tools`; add `\citep{eu2025dualuse}` (or the keys the full paper uses in `sections/02_background.tex` l.13) after `restrict sales to China`; in l.89 add `\citep{taylorwessing2025nexperia, gerechtshof2025nexperia}` after `the chipmaker Nexperia`.

### 22. [minor] Logic gap and odd phrasing in the definition of China's offer

- Anchor (l.27): `part of what China would gain is blocked anyway by US legal reach over the American parts and staff inside ASML's machines.`
- Problem: the reader has to infer why a block on China's gain lowers what Europe would get (China will not pay for what it cannot use). "Staff inside ASML's machines" puts people inside machines. The same object is named three ways: "staff inside ASML's machines" (l.27), "the American parts and staff ASML needs" (l.28), "ASML's parts and staff" (l.89).
- Replacement: `and China will not pay for what US legal reach over the American parts and staff ASML relies on would block anyway.` Use "the American parts and staff ASML relies on" in l.28 and l.89 too.

### 23. [minor] Ambiguous "it" in the definition of the penalty

- Anchor (l.28): `Help Washington would give Europe anyway, for its own reasons, is not part of $k$, however large it is.`
- Problem: "it" can mean the help or $k$.
- Replacement: `Support Washington would give Europe anyway, for its own reasons, is not part of $k$, however large that support is.`

### 24. [minor] Long sentence and lowercase $x$, $y$ beside uppercase $X$, $Y$

- Anchor (l.69): `Or Europe might stop servicing the machines in Washington's own chip plants, which costs those plants something every round (call it $x$) and costs Europe its own lost sales and Washington's retaliation (call it $y$).`
- Also (l.69): `which costs Washington its need $V$ and costs Europe $k-c$ when its alternative is poor.`
- Problem: 35 words with two parentheticals. "Washington's own chip plants" are American firms' plants. A lay reader sees $x$ and $X$ and is never told how they relate.
- Replacement: `Or Europe might stop servicing the machines in American chip plants. Each round, the stoppage costs those plants $x$ and costs Europe $y$, its own lost sales plus Washington's retaliation.` For the collapse clause: `which costs Washington $V$ and, when Europe's walk-away value is negative, costs Europe its squeeze room, $k-c$.`

### 25. [minor] The note never says in words how $X$ and $Y$ are built

- Anchor (l.69): `The appendix gives the exact weights.`
- Problem: the reader learns the two sources of cost but not that $X$ mixes them, or that $V$ enters only in proportion to the risk of collapse. That is the point of "this is how Washington's need can enter the price".
- Replacement: `Washington's cost $X$ blends the two: it is close to $V$ when collapse is likely and close to $x$ when it is not. Europe's cost $Y$ blends $k-c$ and $y$ the same way. The appendix gives the weights.`

### 26. [minor] The formula has no plain gloss, and Europe's say gets no label

- Anchor (l.65): `and that Europe names the terms a share $\beta$ of the time.`
- Also (l.65): `Then Europe gets the larger of $c-k$ and`
- Problem: a reader without game theory needs the displayed formula read out once. "Europe's say", the name used later ("Europe must have a say"), is never attached to $\beta$.
- Replacement: `and that Europe names the terms a share $\beta$ of the time (Europe's say).` After the display add: `In words: Europe's say times what stalling costs Washington, less Washington's say times what stalling costs Europe.`

### 27. [minor] Proposition 1: ambiguous pronoun, max notation and "secures"

- Anchor (l.43): `Europe always secures its walk-away value $c-k$.` and `If the threat does not stick, Washington pays $\max\{0,c-k\}$.`
- Problem: "secures" is ambiguous when the value is negative. A Europe whose threatened partner cannot make threats stick gets more than $c-k$. In `If Washington's threat sticks, it offers exactly` the word "it" can be the threat. The max notation is the only formula in the main-text propositions and is easy to put in words.
- Replacement: `Europe always gets at least its walk-away value $c-k$. If Washington's threat sticks, Washington offers exactly $c-k$: ...` and `If the threat does not stick, Washington pays $c-k$ when it is positive and nothing otherwise.`

### 28. [minor] "Threats matter only on the downside" is vague, and "up to" undersells Proposition 1

- Anchor (l.46): `Threats matter only on the downside.`
- Also (l.46): `while a Washington whose threats stick extracts concessions up to the squeeze room.`
- Problem: "the downside" is a market idiom; the precise condition is a negative walk-away value. Proposition 1 says Washington takes exactly $k-c$; "up to" belongs to Proposition 2.
- Replacement: `Threats matter only when the walk-away value is negative.` Split the last sentence of the paragraph: `When it is negative, a Washington whose threats do not stick pays nothing and gets nothing. A Washington whose threats stick takes concessions worth the whole squeeze room.`

### 29. [minor] Security support has four names

- Anchor (l.28): `the part of its security support it would withdraw from a disloyal ally`
- Other instances: "support" (l.85), "American protection" (l.85, l.89), "troops" (l.89).
- Problem: elegant variation. A reader may think "troops" is a separate instrument.
- Replacement: use "security support" throughout, or define once: `security support (American protection, including troops)` and then use "American protection" each time.

### 30. [minor] "Credible on its own terms" is vague and reintroduces "credible"

- Anchor (l.89): `Each threat has to be credible on its own terms.`
- Replacement: `In the full paper each threat sticks or does not stick on its own, and Washington may be unable to make some of them stick.`

### 31. [minor] "Failed", "stalled" and "collapse" are used for different things without distinction

- Anchor (l.65): `The rule assumed that failed talks cost nobody anything.`
- Also (l.36): `If talks fail, Washington loses nothing`
- Problem: the note's plain term is "stalled talks" (delay). "Collapse" means an unchosen realignment. "Failed talks" could mean either.
- Replacement: l.65 `\Cref{sec:gets} assumed that stalled talks cost nobody anything.` l.36 `If talks stall, Washington loses nothing`. Keep "collapse" only for realignment, and drop "collapse channel" (finding 4).

### 32. [minor] Proposition 3 says "squeeze" for "squeeze room"

- Anchor (l.78): `and Washington has nothing else it values to spend today's squeeze on.`
- Also (l.75): `would raise Europe's walk-away value and shrink the room.`
- Replacement: `and Washington has no other demand it values enough to spend today's squeeze room on.` and `shrink the squeeze room.`

### 33. [minor] "Measured in what they are worth to Europe" does not fit $V$

- Anchor (l.24): `Three numbers describe the bargain, all measured in what they are worth to Europe.`
- Problem: $V$ is defined as Washington's loss, so a careful reader stalls here. What the authors mean is a common currency: a payment worth one unit to Europe costs Washington one unit.
- Replacement: `Three numbers describe the bargain, all in one currency: a payment worth a unit to Europe costs Washington a unit.`

### 34. [minor] Other meta-commentary

- Anchor (l.32): `The quantity that matters is Europe's \emph{walk-away value}, $c-k$:`
  Replacement: `Europe's \emph{walk-away value}, $c-k$, is how much better off Europe would be by switching, all things counted.`
- Anchor (l.89): `The full paper adds what the three numbers hide.`
  Replacement: delete. Start with `In the full paper, China puts a price on particular European concessions, ...`
- Anchor (l.109): `Without rupture risk and without a usable exit option, the derivation takes one line.`
  Replacement: `Suppose there is no rupture risk and no usable exit option.` The derivation takes four sentences, so "one line" is also inaccurate.

### 35. [minor] Overclaim on piecemeal demands

- Anchor (l.59): `Piecemeal demands get less`
- Problem: the appendix (l.103) says Washington "can get strictly less", not that it always does.
- Replacement: `Piecemeal demands can get less`

### 36. [minor] The appendix uses the full paper's jargon without a gloss

- Anchor (l.101): `less the bite $\min\{k,\pos{-q}\}=\pos{-q}$ gives $q$.`
- Also (l.109): `the full paper's remark on slack under rupture risk.`
- Replacement: at first use add `(the full paper's \emph{bite} is what a threat takes; its \emph{slack} is this note's squeeze room)`.

### 37. [minor] Figure typography

- Anchor (`make_minimal_figure.py` l.11): `"font.family": "serif", "font.size": 9`
- Problem: the figure is set in DejaVu Serif with DejaVu Sans oblique for $V$ and $k-c$ (`pdffonts`), against the note's Computer Modern. At `width=0.82\textwidth` the 7.5 to 8 pt annotations print at about 6 to 6.5 pt. Below zero the dashed "threats do not stick" line lies on the grey zero axis and is hard to see. The zero tick could carry the condition that defines it.
- Replacement: add `"mathtext.fontset": "cm"` and `"font.serif": ["CMU Serif", "Computer Modern Roman", "DejaVu Serif"]` to `rcParams`. Raise annotation sizes by 1 pt, or set the figure at `width=\textwidth`. Draw the zero line with `lw=0.5, alpha=0.6` and the dashed segment on top (`zorder=3`). Set `ax.set_xticks([-3,-2,-1,0,1,2,3,4,5]); ax.set_xticklabels(["−3","−2","−1","0\n($c=k$)","1","2","3","4","5"])`.

## Terminology audit (the note's plain names)

| Term | Where it is consistent | Where it drifts | Fix |
|---|---|---|---|
| China's offer, $c$ | l.27, Prop. 1, figure axis, l.75, l.85 | none | none |
| Washington's penalty, $k$ | l.28, Prop. 1, figure axis, l.85, l.89 | "what Washington would really cut off" (abstract, as a gloss, fine) | none |
| Washington's need, $V$ | l.29, l.46, l.69, l.89 | "importance to Washington" (l.13, l.51) | findings 9, 13 |
| Walk-away value, $c-k$ | most places | "alternative" (l.38, l.46, l.69, l.75), "position" (l.13) | finding 12 |
| Squeeze room, $k-c$ | l.32, l.46, l.59, Prop. 3, figure | "shortfall" (l.13), "the squeeze" (l.78, l.81 three times), "the room" (l.51, l.75); "budget" is fine once tied to the squeeze room (l.59) | findings 11, 18, 32 |
| Threat sticks | Prop. 1, l.46, figure legend | "credible" (l.51, l.71, l.89), "committed" (l.101), never defined | finding 1 |
| Stalled talks, $X$ and $Y$ | l.13, l.65 | "failed talks" (l.36, l.65), "collapse channel" (l.71) | findings 4, 31 |
| Europe's say, $\beta$ | "has a say" (l.13, l.71) | never attached to $\beta$ at definition | finding 26 |
| Political cost of handing over control, $s$ | Prop. 3, appendix | "sovereignty" (l.81) is a gloss, fine | none |
| Security support | l.28 | "support", "American protection", "troops" | finding 29 |

## House-style audit summary

- **Em dashes:** none. The only `--` is the range `2(b)--(c)` (l.103), which is allowed.
- **Negative parallelism:** l.13, l.36, l.46, l.61 and l.85 (findings 13, 15, 14, 16, 6). The contrast `can take at most $k-c$, not $k$` (l.38) is a real contrast with the naive reading of a threat and can stay.
- **Meta-commentary:** l.20, l.32, l.38, l.81, l.89, plus l.109 in the appendix (findings 2, 34, 17, 18). Announced counts at l.24 ("Three numbers"), l.69 ("Two things") and l.71 ("three conditions") are correct and are the point. l.71 becomes clean once its third item is stated as a condition (finding 4).
- **Hedges attached to "we":** good at l.61 ("On our reading") and l.71 ("We expect ... but have not proved it"). Impersonal at l.89 ("The paper's reading of the record finds", "remains untested") (finding 20).
- **Overclaim:** "The budget explains" (l.61) and "Piecemeal demands get less" (l.59) (findings 19, 35). Section 6 drops the full paper's scope condition (finding 6).
- **Fractal summary:** the verdict in the abstract, l.46 and the caption (finding 9); the abstract's first sentence repeated at l.20 (finding 2).
- **Sentence rhythm:** body burstiness about 0.56, so it passes. Sentences over 35 words: l.61 (49), l.89 (44), l.71 (38), l.69 (35), all with fixes above. Paragraph lengths vary well, and the short sentences ("It does not raise the price.", "Europe accepts or refuses.") land.
- **Uncited particulars:** l.18, l.61, l.71, l.89 (findings 19, 21, 4).
- **Dead vocabulary, trailing significance clauses, copula avoidance, stacked "However"/"Moreover":** none found.
- **Cross-references:** Sections 1, 6 and 7 have no `\label`. Finding 2's fix needs one on Section 1 if it cross-refers there; it can name the section in words instead.

## The figure

It does its main job. Payment is a single line in the walk-away value, the two threat regimes coincide above zero, the shaded region shows where threats pay, and the grey region shows where Washington lets Europe go. A reader who looks only at the figure and caption gets "Europe is paid its walk-away value" and "threats only help Washington below zero". The reader does not get "need does not raise the price", because only one value of $V$ is drawn (finding 7). Fix the label collision, show the squeeze room as a vertical distance (finding 8), and rewrite the caption so it explains how to read the figure rather than repeating the abstract (finding 9). The control result and the stalled-talks result are not in the figure, and they do not need to be.
