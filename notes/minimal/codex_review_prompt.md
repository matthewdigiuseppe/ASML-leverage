# Error check of the minimal-model note

You are checking a short theory note for errors. Find mistakes; do not praise, summarize or rewrite the note.

## What to read

- `paper/minimal/minimal_model.tex` (the note; the compiled version is `paper/minimal/minimal_model.pdf`)
- `paper/minimal/make_minimal_figure.py` (the note's only figure)
- `code/checks/minimal_model_check.py` (brute-force checks of the note's results)
- The full paper the note summarizes: `paper/sections/*.tex`, with printed result numbers in `paper/main.aux` (for example `\newlabel{prop:slack}{{2}...}` means "Proposition 2")
- `paper/refs.bib` for the citations

Do not read anything in `notes/minimal/` other than this file. We want a read that is independent of earlier reviews.

## What counts as an error

1. **Math.** Re-derive every proposition and every appendix proof yourself. Check each equality and inequality, the boundary and tie cases, and whether each stated "if and only if" really runs both ways. Look for hidden assumptions a result needs but does not state.
2. **Statement versus proof.** Check that each plain-language claim in the main text, the abstract and the figure caption follows from the formal results, with no condition dropped and no claim made stronger than what is proved.
3. **Consistency with the full paper.** Check that every cross-reference ("Proposition 2(b)–(d) of the full paper", "Lemma 1", "Remark 1", "Corollary 5", "the special case after Proposition 5", "Proposition 6") names the right result in `paper/main.aux`, and that the note's version is a correct special case of it.
4. **Figure.** Check that the lines, regions and labels in the figure match the propositions, for example where the payment lines sit, what is shaded, and where Washington lets Europe go.
5. **Facts and citations.** Check that each dated fact is supported by the `refs.bib` entry cited for it and agrees with how the full paper states it.
6. **Internal contradictions** between sections of the note.

Run `python3 -I code/checks/minimal_model_check.py` (about 70 seconds) and report whether all checks pass. You may write and run your own short Python checks in a scratch location; do not add them to the repository.

## Output

Write your report to `notes/minimal/review_codex.md`. Do not edit any other file.

For each error give:
- **Severity:** essential (a result or claim is wrong), important (a missing condition or a real overclaim), or minor (precision or wording).
- **Anchor:** the exact text from the `.tex` file.
- **Problem:** what is wrong and why. For math, show the derivation or a counterexample with numbers.
- **Fix:** replacement text.

List errors from most to least severe. Then list what you checked and found correct, so we know what was covered. If you find no errors in a category, say so.
