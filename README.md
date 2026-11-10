# Owning the Chokepoint: ASML, Alliance Dependence, and the Limits of Europe's Leverage over Washington

**Read the paper:** [`paper/ASML_leverage_v3_draft.pdf`](paper/ASML_leverage_v3_draft.pdf) (working draft, version 3, 10 November 2026, 115 pages). The previous draft is kept as [`paper/ASML_leverage_v2_draft.pdf`](paper/ASML_leverage_v2_draft.pdf); see [Version history](#version-history).

Authors: Matt DiGiuseppe and Claude (Anthropic)

## What this repository is

This project is an experiment. We wanted to see whether a large language model, Claude, made by Anthropic, could write a formal model of an important global issue: the leverage the Netherlands and the European Union hold through ASML, the only maker of the extreme ultraviolet lithography machines on which the most advanced AI chips depend.

Claude did the work in Claude Code with Ultracode turned on. In that mode Claude plans the work and runs it through multi-agent workflows: it sends out research, verification, drafting and review tasks to many subagents, then reads their results and decides what to do next.

Almost all of what is here was written by Claude: the literature and fact review, the model, the proofs, the numerical checks, the text, the tables and the figures. Matt DiGiuseppe, a quantitative political scientist, supplied the research question, the instructions and the reading material, and steered the work with a few short follow-up requests. The opening instruction, in full, was:

> Let's write a formal theory paper that probes the leverage NL/EU have with ASML in the AI race. Start with Europe2031. Consider the broader dependence of EU/NL on the US for defense, credibility of the commitment, and economic dependence on China. Do a little review before starting

The work took place on 28 and 29 October 2026.

## Status: read this before citing anything

- **This is an unreviewed working draft.** No human referee has read it. The referee reports that shaped the revisions were written by Claude subagents asked to act as hostile reviewers for *International Organization*. They are not real peer review.
- **The proofs have not been checked by a person.** Every proposition has a written proof in Appendix B. Each result was also spot-checked numerically by brute-force computation on random and edge-case parameters (scripts in `code/checks/`). That is evidence, not formal verification. These checks found and fixed several errors, and one claim was refuted outright. Matt DiGiuseppe has not yet independently verified the proofs or every factual claim.
- **Facts are as of late October 2026.** Each factual claim traces to a source listed in the verification notes (`notes/review/`, `notes/v2/facts_*.md`). Several items were live at the time of writing and may since have changed: the MATCH Act, the US-China trade truce, and the expiry of China's suspended export controls.
- ***Europe 2031* is fiction.** The paper uses that published scenario as its opening hook and reads it against the model in Appendix D. The empirical puzzle is the real record from 2019 to 2026.

## What the model finds, in brief

1. **ASML pays Europe only if Europe has a credible alternative.** Europe's leverage starts from what it could credibly get by realigning with China, net of what Washington could credibly make that move cost. On our reading that alternative has been worse than staying aligned since 2019, so Washington has not had to pay. The 2024 US exemption for the Netherlands is a status Washington can revoke, not a payment. Washington's own need for ASML matters only through narrow channels: when talks could break down for a long time while Europe gets to make offers, and when Europe can hurt Washington during a dispute. If a breakdown would soon be undone, Washington's need counts only in proportion to how long it would last. If China values what Washington pays, it bids the price up to the limit of its own credibility.
2. **Washington's linked demands draw on one budget.** However Europe's price is set, Washington's conditional threats can extract at most Europe's surplus over what realigning would give it. Demands compete for that surplus only where Washington enforces them through the alliance itself. A concession that Washington can enforce with a penalty of its own, such as a tariff threat, escapes the budget but costs Europe more, because realigning no longer undoes it. So whether a concession on trade leaves less to extract on servicing depends on how Washington enforces it.
3. **Refusals need uncertainty.** If Washington knew what each demand costs Europe, it would never make one Europe would refuse. Refusals arise when Washington is unsure. As Europe's alternative approaches alignment in value, Washington's conditional threats bite less, so the refusals it can prevent at any price become fewer. A request Washington does not back with a threat can be refused at no cost; Dutch and Japanese resistance to limits on servicing in China fits that pattern.
4. **Making protection depend on loyalty is the price of concessions.** A Washington that wants nothing beyond alignment ties its defence guarantee to Europe's behaviour only as far as it must. Tying it further costs Washington the confidence, and the slack, of other allies who watch, and it pays that cost only to extract more.
5. **China's pressure mostly costs Washington.** Beijing targets specific European steps (the 2025 Nexperia dispute is the leading case) rather than alignment as such. That mainly changes which concessions Washington can get.
6. **A shrinking hold invites a demand for control.** If Europe's alternatives improve, Washington has a reason to lock in control of ASML while its threats still work. Visible European investment in autonomy hastens that demand. When talks can break down, the motive exists even if Europe's alternative stays worse than alignment, because control removes the leverage that the risk of breakdown gives Europe. Europe's best defence is to bind itself first, through EU-level controls, which works only if Washington does not want control for its own sake.
7. **Stopping service is Europe's strongest card, and whether it is believable depends on expectations.** The European Union's instruments escalate slowly and can be called off after any US offer. Under that timing there are equilibria in which the threat to interrupt servicing works at full strength without ever being used, and equilibria in which it is worthless. The record of suspended countermeasures fits the second.

Empirically, the record is consistent with US legal reach over ASML's inputs and staff doing most of the work. How closely Washington's security commitments are tied to Europe's export controls remains untested.

## Repository layout

| Path | Contents |
|---|---|
| `paper/` | LaTeX source (`main.tex`, `sections/`, `preamble.tex`, `refs.bib`), figures, and the compiled PDF |
| `paper/sections/` | One file per section; `A0_supplementary`, `A_proofs`, `B_numerics` and `C_scenario` are the appendices |
| `code/checks/` | Python scripts that spot-check each result by brute force; `README.md` there maps scripts to results (`v3_*` scripts check the results new or changed in version 3, `v2_*` scripts the results carried over) |
| `notes/review/` | The initial literature and fact review, written and fact-checked by subagents |
| `notes/v2_sections/` | The version 2 LaTeX sections, kept for the record |
| `notes/model_design_v2.md`, `notes/v2/` | The design memo for the current model, the verification reports for each result, verified literature and facts, the binding drafting decisions, and the simulated review and final-check reports |
| `notes/v1_sections/` | The first full draft, kept for the record |

## How the work was done

1. **Review.** Subagents surveyed the literatures on weaponized interdependence, alliance politics, commitment problems, EU decision rules, Chinese economic coercion and frontier AI. They checked facts against primary sources.
2. **Design and verification.** Claude designed a game-theoretic model. Independent subagents then tried to refute each result, writing proofs and brute-force checks.
3. **Drafting.** Subagents drafted the sections in parallel from shared, binding statements of each result.
4. **Simulated peer review.** Four subagent referees (a formal theorist, a security scholar, an IPE and EU specialist, and a style auditor) reviewed the first draft. Two recommended reject-and-resubmit, one major revision and one (the style auditor) minor revision. The paper was rebuilt around their critiques.
5. **Revision and checks.** Further rounds of verification, review, editing and final checks followed.

Each round caught real errors. Among them: the first draft's headline result was already known in the literature; the revised thesis was briefly stated backwards; one example in the paper was false; and Claude itself made a mistake in a new result, which a subagent caught.

## Version history

**Version 3 (10 November 2026).** Matt DiGiuseppe asked Claude to check whether the game theory in version 2 was sound. Claude re-derived the main results and checked them with new brute-force solvers. It found no errors in the propositions, but several headline findings rested on modelling choices more than on strategic interaction. It recommended changes, and was asked to make them. This version:

- states the slack principle for any rule that settles Europe's price (bidding, bargaining under rupture risk, hold-up, price driving), replacing the separate remark on rupture risk;
- adds a linkage result: a concession draws on the shared budget only through the part that Washington enforces through the alliance, not through any part it can enforce with a penalty of its own;
- lets ruptures be repaired at rate φ, so Washington's dependence is weighted by λ/(λ+r+φ);
- shows that a China that values Washington's payments drives the price to its credibility bound, which pins down the price in the alternating-raise auction;
- adds private information about the cost of a demand, which produces refusals and executed threats, and lets Washington make requests it does not back;
- shows that every subgame-perfect equilibrium of the hold-up game has the Markov payoff under the main timing, and gives the full range of equilibrium payoffs under the timing of the EU's instruments;
- derives the assurance cost of conditionality from a second ally's slack, and moves the conditionality proposition to the supplementary appendix;
- extends preventive control to a general settlement, so that the motive can arise with a negative premium;
- fixes smaller points: the credibility condition behind the slack principle's attainment claims, a self-binding example's dependence on the commitment cap, and the scope of binding agreements in the bargaining game.

The changes add about 12 pages. An independent subagent review of the new proofs found one error in a side claim (removed) and several overstatements (corrected) before release. Claude also suggested building a shorter paper around the general slack principle and the linkage result; that restructuring has not been done.

**Version 2 (29 October 2026).** The draft described above under "How the work was done".

## Building the paper and running the checks

```bash
cd paper
python3 figures/make_figures.py          # figures (numpy, matplotlib)
pdflatex main && bibtex main && pdflatex main && pdflatex main

cd ..
python3 -I code/checks/v3_settlement_slack.py   # any v2_* or v3_* script (numpy; some use scipy)
```

The paper builds with a standard TeX Live installation (natbib, cleveref, tikz and lmodern) and the `aer` bibliography style.

## Licence

The code in `code/` is released under the MIT License (`LICENSE`). The paper, figures and notes are released under the Creative Commons Attribution 4.0 International licence (`LICENSE-paper.md`).
