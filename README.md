# Owning the Chokepoint: ASML, Alliance Dependence, and the Limits of Europe's Leverage over Washington

**Read the paper:** [`paper/ASML_leverage_v2_draft.pdf`](paper/ASML_leverage_v2_draft.pdf) (working draft, 29 October 2026, 103 pages)

Authors: Matt DiGiuseppe and Claude (Anthropic)

## What this repository is

This project is an experiment. We wanted to see whether a large language model, Claude, made by Anthropic, could write a formal model of an important global issue: the leverage the Netherlands and the European Union hold through ASML, the only maker of the extreme ultraviolet lithography machines on which the most advanced AI chips depend.

Claude did the work in Claude Code with Ultracode turned on. In that mode Claude plans the work and runs it through multi-agent workflows: it sends out research, verification, drafting and review tasks to many subagents, then reads their results and decides what to do next.

Almost all of what is here was written by Claude: the literature and fact review, the model, the proofs, the numerical checks, the text, the tables and the figures. Matt DiGiuseppe, a quantitative political scientist, supplied the research question, the instructions and the reading material, and steered the work with a few short follow-up requests. The opening instruction, in full, was:

> Let's write a formal theory paper that probes the leverage NL/EU have with ASML in the AI race. Start with Europe2031. Consider the broader dependence of EU/NL on the US for defense, credibility of the commitment, and economic dependence on China. Do a little review before starting

The work took place on 28 and 29 October 2026.

## Status: read this before citing anything

- **This is an unreviewed working draft.** No human referee has read it. The referee reports that shaped the revisions were written by Claude subagents asked to act as hostile reviewers for *International Organization*. They are not real peer review.
- **The proofs were checked by machine, not by a person.** Every proposition has a written proof in Appendix B. Independent subagents also checked each result by brute-force computation (scripts in `code/checks/`). These checks found and fixed several errors, and one claim was refuted outright. Matt DiGiuseppe has not yet independently verified the proofs or every factual claim.
- **Facts are as of late October 2026.** Each factual claim traces to a source listed in the verification notes (`notes/review/`, `notes/v2/facts_*.md`). Several items were live at the time of writing and may since have changed: the MATCH Act, the US-China trade truce, and the expiry of China's suspended export controls.
- ***Europe 2031* is fiction.** The paper uses that published scenario as its opening hook and reads it against the model in Appendix D. The empirical puzzle is the real record from 2019 to 2026.

## What the model finds, in brief

1. **ASML pays Europe only if Europe has a credible alternative.** Europe's leverage starts from what it could credibly get by realigning with China, net of what Washington could credibly make that move cost. On our reading that alternative has been worse than staying aligned since 2019, so Washington has not had to pay. The 2024 US exemption for the Netherlands is a status Washington can revoke, not a payment. Washington's own need for ASML matters only through narrow channels: when talks could break down while Europe gets to make offers, and when Europe can hurt Washington during a dispute.
2. **Washington's pressure draws on one budget.** Washington can extract concessions only up to the gap between what realigning would cost Europe and what China would credibly give it. Demands on export controls, servicing, trade terms and defence spending all compete for that same gap. That is why Europe complies with some demands and resists others, such as limits on servicing machines already in China.
3. **Making protection depend on loyalty is the price of concessions.** A Washington that wants nothing beyond alignment ties its defence guarantee to Europe's behaviour only as far as it must. Tying it further costs Washington allied confidence, and it pays that cost only to extract more.
4. **China's pressure mostly costs Washington.** Beijing targets specific European steps (the 2025 Nexperia dispute is the leading case) rather than alignment as such. That mainly changes which concessions Washington can get.
5. **A shrinking hold invites a demand for control.** If Europe's alternatives improve, Washington has a reason to lock in control of ASML while its threats still work. Visible European investment in autonomy hastens that demand. Europe's best defence is to bind itself first, through EU-level controls, which works only if Washington does not want control for its own sake.
6. **Stopping service is Europe's strongest card, and today it is not believable.** The European Union's instruments let it call off countermeasures quickly but escalate only slowly. So Europe cannot commit in advance to an interruption that Washington could not end with its first offer.

Empirically, the record is consistent with US legal reach over ASML's inputs and staff doing most of the work. How closely Washington's security commitments are tied to Europe's export controls remains untested.

## Repository layout

| Path | Contents |
|---|---|
| `paper/` | LaTeX source (`main.tex`, `sections/`, `preamble.tex`, `refs.bib`), figures, and the compiled PDF |
| `paper/sections/` | One file per section; `A0_supplementary`, `A_proofs`, `B_numerics` and `C_scenario` are the appendices |
| `code/checks/` | Python scripts that check each result by brute force; `README.md` there maps scripts to results (the `v2_*` scripts check the current results) |
| `notes/review/` | The initial literature and fact review, written and fact-checked by subagents |
| `notes/model_design_v2.md`, `notes/v2/` | The design memo for the current model, the verification reports for each result, verified literature and facts, the binding drafting decisions, and the simulated review and final-check reports |
| `notes/v1_sections/` | The first full draft, kept for the record |

## How the work was done

1. **Review.** Subagents surveyed the literatures on weaponized interdependence, alliance politics, commitment problems, EU decision rules, Chinese economic coercion and frontier AI. They checked facts against primary sources.
2. **Design and verification.** Claude designed a game-theoretic model. Independent subagents then tried to refute each result, writing proofs and brute-force checks.
3. **Drafting.** Subagents drafted the sections in parallel from shared, binding statements of each result.
4. **Simulated peer review.** Four subagent referees (a formal theorist, a security scholar, an IPE and EU specialist, and a style auditor) reviewed the first draft. Two recommended reject-and-resubmit, one major revision and one (the style auditor) minor revision. The paper was rebuilt around their critiques.
5. **Revision and checks.** Further rounds of verification, review, editing and final checks followed.

Each round caught real errors. Among them: the first draft's headline result was already known in the literature; the revised thesis was briefly stated backwards; one example in the paper was false; and Claude itself made a mistake in a new result, which a subagent caught.

## Building the paper and running the checks

```bash
cd paper
python3 figures/make_figures.py          # figures (numpy, matplotlib)
pdflatex main && bibtex main && pdflatex main && pdflatex main

cd ..
python3 -I code/checks/v2_rupture_bite.py   # any v2_* script (numpy; some use scipy)
```

The paper builds with a standard TeX Live installation (natbib, cleveref, tikz and lmodern) and the `aer` bibliography style.

## Licence

The code in `code/` is released under the MIT License (`LICENSE`). The paper, figures and notes are released under the Creative Commons Attribution 4.0 International licence (`LICENSE-paper.md`).
