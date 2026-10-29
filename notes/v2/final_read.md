# Final read (tag: read): editor's read-through, PDF order

Scope: whole paper read start to finish in PDF order (main text pp. 1-48, references pp. 49-66, Appendix A pp. 67-71, B proofs pp. 71-97, C numerics pp. 97-101, D scenario pp. 101-103). A fresh scratch compile (pdflatex, bibtex, pdflatex x2) produces a PDF identical in text to paper/main.pdf, 103 pages, with no undefined references or citations and no overfull boxes. The "Label(s) may have changed" line in paper/main.log is stale: a rerun changes nothing. No em dashes, no TODOs and no hardcoded result numbers remain. Every label that moved to Appendix A still resolves. Section word counts (detex, tables excluded) are within the brief's ceilings.

## Verdict

Ready to circulate as a working paper once the first five fixes below are made. Each takes one sentence or one clause. The argument is clear from the abstract and introduction, and the sections follow one another. The formal results and the appendix moves are clean. What remains is a small set of cross-section inconsistencies:
- what the record shows about linkage (Section 5.2 against Section 8.3);
- how the Council result is reported (introduction against Section 7.3);
- whether hold-up is a channel of V (introduction and Corollary 1(e) against Section 7.4);
- whether the security scope condition is met (Section 9.1 against Sections 8.3 and 9.2);
- the jurisdictional finding, which the conclusion puts first and the abstract leaves out.

The rest are minor: layout, terminology and repetition.

## Fixes in order of importance

### 1. Essential. Section 8.3 says no conditional linkage has been found, but Section 5.2 cites some.
- File: sections/08_evidence.tex
- Anchor: "Rationing would require that some steps were backed by conditional linkage, which we have not found."
- Problem: Section 5.2 (05_slack.tex: "The 2025 National Security Strategy and the August 2025 joint statement tie favourable treatment and US AI exports to export-control alignment (\cref{sec:background}), a reversible concession.") presents exactly this as conditional linkage behind export-control alignment. Section 8.2 defines linkage through AI access and trade terms as "conditional linkage", so a reader meets two contradictory claims about what the record shows. The two can be reconciled because the documents postdate the 2023-2025 sales steps, but the text does not say so. Section 5.3 also reads the same NSS passage as a rise in conditionality answering China's bid, a third use of one document.
- Replacement: "Rationing would require that some of the 2023--2025 sales steps were backed by conditional linkage, which we have not found. The general linkage of AI exports and favourable treatment to export-control alignment (\cref{sec:counter}) came later, in August and December 2025, and names no Dutch step."

### 2. Important. The introduction reports the Council result that Section 7.3 says does not bind.
- File: sections/01_intro.tex
- Anchor: "and Washington defeats a countermeasure most cheaply by buying a blocking minority before the Council's determination (\cref{rem:council})."
- Problem: Section 7.3 concludes that "The formal threshold is not what binds" and that "Washington has a route cheaper than buying a blocking minority: a concession that triggers suspension". The introduction reports only the vote-buying result, against editor brief A.9.
- Replacement: "and Washington can defeat a countermeasure by buying a blocking minority before the Council's determination (\cref{rem:council}), although the record points to a cheaper route: the Union arms countermeasures against Washington and suspends them once Washington makes a concession (\cref{sec:council})."

### 3. Important. Hold-up is called a channel of V, but Section 7.4 says it works through c_S.
- Files: sections/01_intro.tex, sections/04_model.tex (Corollary 1(e)).
- Anchors: in 01_intro.tex, "Washington's dependence on ASML enters through five channels: agenda power under rupture risk, the rival's valuation, self-harming sanctions, the silicon shield and hold-up (\cref{cor:master})."; in 04_model.tex, "\Cref{prop:pain} adds the fifth channel, hold-up."
- Problem: V is defined as Washington's loss if China gains the tools. Section 7.4 ("In \cref{prop:pain} the relevant loss is $c_S$ ... and it raises Europe's transfer without any rupture risk") and Appendix D ("It lowers $c_S$ ... and leaves $V$ ... where it was") both say that hold-up runs through Washington's need for ASML's servicing of its own fabs, not through V. A reader of the introduction will take the five channels to be five routes for V.
- Replacement in 01_intro.tex: "Washington's dependence on ASML enters through five channels: agenda power under rupture risk, the rival's valuation, self-harming sanctions and the silicon shield, which carry its loss $V$ if China gains the tools, and hold-up, which carries what its own fabs would lose without ASML's servicing (\cref{cor:master,prop:pain})."
- Replacement in Corollary 1(e): "\Cref{prop:pain} adds the fifth channel, hold-up, which works through Washington's own need for ASML's servicing ($c_S$), not through $V$."

### 4. Important. Section 9.1 says the security scope condition is met, but Sections 8.3 and 9.2 call it untested.
- File: sections/09_implications.tex
- Anchor: "The Netherlands, Japan and South Korea meet the first, second and fourth."
- Problem: condition (ii) is "a partly conditional guarantee" ($\kappa S_k+d_p>0$). Section 8.3 says "the security channel [is] untested", and Section 9.2 says "the guarantee's conditionality is untested". The scope section asserts as fact what the evidence section leaves open, and this sits at the centre of the paper's framing (the title's "Alliance Dependence").
- Replacement: "The Netherlands, Japan and South Korea meet the first and fourth. On the second, the May 2026 posture order against Germany (\cref{sec:background}) suggests that $d_p$ is positive, while the conditionality of the core guarantee is untested (\cref{sec:record})."

### 5. Important. The abstract leaves out the paper's main empirical finding, jurisdiction.
- File: sections/00_abstract.tex
- Anchor: "The sign of Europe's premium turns on China's credible promises and, if Washington's threat to withhold frontier AI is credible, on that instrument, which on our orders of magnitude weighs more than how conditional the US guarantee is."
- Problem: the introduction ("its jurisdiction over ASML's inputs and staff can make the premium negative without any security term") and the conclusion ("turns first on that shared jurisdiction") both put US jurisdiction first. The abstract leaves it out. The abstract also switches from "the Netherlands" and "holder" to "Europe" without saying that Europe is the holder in the model. Finally, "weighs more than how conditional the US guarantee is" compares an instrument with a degree.
- Replacement: "US jurisdiction over ASML's inputs and staff can keep Europe's premium negative without any security term. Beyond that, the sign of the premium turns on China's credible promises and, if Washington's threat to withhold frontier AI is credible, on that instrument, which on our orders of magnitude weighs more than the conditional part of the US guarantee." This adds about 15 words to an abstract of 187. To stay under 190, cut "We prove each result and check it numerically." (Appendices B and C say this.)

### 6. Important. The abstract and conclusion overstate the bound on demands, and "slack" is used for two quantities.
- Files: sections/00_abstract.tex, sections/10_conclusion.tex, sections/04_model.tex.
- Anchors:
  - 00_abstract.tex: "The patron's demands are bounded by the holder's slack, which all its conditional threats share."
  - 10_conclusion.tex: "The patron's demands are bounded by the holder's slack. Under rupture risk Washington's dependence on ASML raises both what Europe obtains in bargaining and the slack that Washington's conditional threats can claw back"
  - 04_model.tex: "Washington's dependence thus raises both what Europe obtains in bargaining and the slack Washington can coerce."
- Problem: by Proposition 2, slack caps only what conditional threats extract. Sunk concessions and unconditional parts "escape the cap" (Section 5.1), and the bound is the bite $B(J^c)$. Under rupture risk the cap is $\Lambda_\psi=P^*(Q)-Q$, which Remark 1 calls "Europe's surplus over exit". The model section and the conclusion call this "slack", although resolutions.md fixes "slack" as $\Lambda=\pos{-Q}$.
- Replacements:
  - Abstract: "What the patron can extract with conditional threats is bounded by the holder's slack, a budget all those threats share."
  - Conclusion: "What the patron can extract with conditional threats is bounded by the holder's slack. Under rupture risk Washington's dependence on ASML raises both what Europe obtains in bargaining and Europe's surplus over exit, which Washington's conditional threats can claw back (\cref{rem:rupture})."
  - 04_model.tex: "Washington's dependence thus raises both what Europe obtains in bargaining and the surplus over exit that Washington can coerce."

### 7. Important. The conclusion says the Netherlands "has the institutions" for the direction in which it bargains.
- File: sections/10_conclusion.tex
- Anchor: "The Netherlands licenses ASML's exports, so it has the institutions."
- Problem: Sections 2.2, 3.1 and 7.3 establish that The Hague's licence decides only the China-bound direction. Turning ASML against Washington is collective, through EU001 and the Council. The third condition is about a holder bargaining with the dependent patron, so the conclusion's claim cuts against the paper's own institutional argument.
- Replacement: "The Netherlands licenses ASML's exports to China, so it has the institutions in that direction. Turning the tools against Washington takes a Union decision (\cref{sec:council})."

### 8. Important. A verdict on Europe 2031 remains in the main text.
- File: sections/07_decide.tex
- Anchor: "The seven states that \emph{Europe 2031} names as opposing or abstaining on its failed 2029 measure hold 28.06 percent of EU population \citep{juijn2026europe, council2025population} and cannot block."
- Problem: brief A.11 says "no verdicts on Europe 2031 in the main text", and resolutions 3.5 limits the scenario to the introduction and the scenario appendix. Appendix D already says this and points back to Section 7.3 for the arithmetic, so the main text can keep the arithmetic without the scenario.
- Replacement: "A coalition of the Netherlands, Ireland, Italy, Poland and the three Baltic states holds 28.06 percent of EU population \citep{council2025population} and cannot block." Keep the following sentence ("Any blocking completion needs ...") as it stands.

### 9. Important. The "fifth row" reference in Section 8.1 does not match the table.
- File: sections/08_evidence.tex
- Anchor: "The fifth row also holds against any coercer that prices demands one at a time, as does the result that an added demand can lower what a patron with small stakes obtains (\cref{prop:slack}(d))."
- Problem: the fifth row of Table 2 is "Rival bids" (a stronger bid elicits a more conditional guarantee). Nothing in the text explains why that row separates the model from one-at-a-time pricing. Section 8.5 makes the one-at-a-time contrast for the cross-issue budget, which is the third row.
- Replacement (if the third row is meant): "The third row also separates the model from any coercer that prices demands one at a time, as does the result that an added demand can lower what a patron with small stakes obtains (\cref{prop:slack}(d))." If the fifth row is meant, add the reason in one sentence.

### 10. Important (layout). Table 6 floats to the last page of the paper.
- File: sections/C_scenario.tex
- Anchor: "\begin{table}[t]" (the table tab:scenario)
- Problem: in the PDF, Appendix D's text runs on pp. 101-102 and Table 6 sits alone on p. 103 after all of it, so the paper ends on a stray table. The table is too tall for the default top fraction on p. 102.
- Replacement: "\begin{table}[!tp]"

### 11. Minor. The conclusion ends on a quotation that restates Section 8.
- File: sections/10_conclusion.tex
- Anchor: "What The Hague opposed in May 2026 was the extraterritorial reach of the MATCH Act, on the ground that ``every country is responsible for its own export control legislation'' \citep[our translation]{tk2026match}."
- Problem: the last paragraph is the fourth telling of the Supplement No. 4 coding, and the paper ends on a quote without saying what the model makes of it. The model does have a reading.
- Replacement: add after the quotation: "In the model that is a defence of who holds the key, not of the price. Keeping the licence decision in Europe does not make the premium positive, and it deters a demand for control only if Washington values control little for its own sake (\cref{rem:bind})." Consider cutting the preceding sentence on Supplement No. 4, which the introduction and Section 8.2 already make.

### 12. Minor. The sentence "Whatever agenda power wins..." is told three times.
- Files: sections/04_model.tex and sections/05_slack.tex
- Anchor in 04_model.tex: "Whatever agenda power wins Europe above $\pos{Q}$, Washington's credible conditional threats can claw back, down to the exit premium itself (\cref{rem:rupture})."
- Problem: near-identical sentences appear in the introduction, at the end of Section 4.5 and after Remark 1. Style brief: each argument told once, in its home.
- Replacement: delete the sentence in 04_model.tex. The next sentence already points to Remark 1.

### 13. Minor. "until \cref{rem:rupture}" implies that later results use rupture risk.
- File: sections/05_slack.tex
- Anchor: "We work in the bidding benchmark, without rupture risk, until \cref{rem:rupture}."
- Problem: Propositions 3 and 4 after the remark also use $\pos{Q}$.
- Replacement: "We work in the bidding benchmark, without rupture risk, throughout this section; \cref{rem:rupture} states what changes under rupture risk."

### 14. Minor. Section 7.2's "which" has no antecedent, and the point is repeated in Section 8.3.
- File: sections/07_decide.tex
- Anchor: "If the Chinese ban moved The Hague, $\zeta$ is high when China retaliates against compulsion itself, and the record does not tell us which (\cref{sec:record})."
- Problem: "which" has no pair of alternatives to refer to. Section 8.3 makes the same point ("If China's ban, and not Washington's suspension, moved The Hague ... The sequence does not tell us which").
- Replacement: "Whether China's ban or Washington's suspension moved The Hague, and so whether compulsion is costly when China retaliates against it, the record does not show (\cref{sec:record})." Then delete the last two sentences of the Nexperia cost paragraph in 08_evidence.tex, from "If China's ban, and not Washington's suspension" to "The sequence does not tell us which."

### 15. Minor. The Drezner finding is stated twice, and Section 8.1 places it as if it were a fifth rival.
- File: sections/08_evidence.tex
- Anchor: "\citet{drezner1999sanctions} finds that allies rarely coerce one another but can win significant concessions when they do; his account says nothing about a rival's bid."
- Problem: Section 3.2 already gives the same finding in nearly the same words. In Section 8.1 it follows "The fourth rival ..." and reads like a fifth column of Table 2.
- Replacement: delete the sentence, or shorten it to "\citet{drezner1999sanctions} has no rival bidder."

### 16. Minor. The abstract and introduction use "agenda power" and "hold-up" before defining them.
- File: sections/00_abstract.tex
- Anchor: "Without rupture risk or agenda power, and without hold-up, its leverage is the positive part of that premium."
- Replacement: "Unless talks can rupture while the holder makes proposals, or the holder can impose costs on the patron while they bargain, its leverage is the positive part of that premium."

### 17. Minor. The Dutch motion lacks a year, and spelling is inconsistent.
- File: sections/08_evidence.tex
- Anchors: "On 22 January it had adopted"; "harmonised EU export control"; "Europeanised controls" (twice).
- Problem: the date has no year, unlike every other date in the paragraph. The rest of the paper spells these words "harmonized" and "Europeanized" (03_literature.tex, 06_control.tex).
- Replacement: "On 22 January 2026 it had adopted"; "harmonized"; "Europeanized".

### 18. Minor. Two different qualifiers describe the security channel.
- Files: sections/01_intro.tex ("the security channel is largely untested") and sections/08_evidence.tex ("leaves the security channel untested")
- Replacement: use "largely untested" in both, since 08_evidence.tex goes on to concede that private linkage cannot be excluded. Separately, "jurisdictional channel" and "security channel" share the word "channel" with the five channels of V. Define them on first use in the introduction: "consistent with the jurisdictional source of a negative premium (US reach over ASML's inputs and staff)". In the conclusion, "the jurisdictional half of the argument" should become "the jurisdictional source of Europe's slack".

### 19. Minor (layout and captions).
- figures caption in 04_model.tex. Anchor: "Equilibrium transfer to Europe in the master bargaining game". "Master" is internal jargon. Replacement: "Equilibrium transfer to Europe under rupture risk".
- Table 5 (D2_decide.tex, tab:council). The X first column is squeezed by the wide last header, and coalition names wrap over three lines (p. 71). Replacement: shorten the header "Keeps delegated act in force" to "Saves delegated act" and the third header to "Blocks det.", and define both in the note.
- Table 1 is placed at the top of p. 15 and splits Lemma 1 across pp. 14-15. Optional fix: move the table environment to just before "\paragraph{Timing.}" with "[t]" so that it lands on p. 14, or accept as is.
- Table 4 sources and the references cite "Deutsche Bundesbank (n.d.)". Add a year or an access date to the bib entry.
