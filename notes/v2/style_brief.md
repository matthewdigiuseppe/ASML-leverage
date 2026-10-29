# Style brief for drafters (author's house style; binding)

The author is a quantitative political scientist. The paper targets International Organization. Write as the author ("we").

## Hard bans
- **No em dashes, ever** (no "---" in LaTeX prose, no "—"). Use parentheses for an aside or start a new sentence. En dashes ("--") only for ranges (2019--2026) and compounds (US--China).
- **Negative parallelism**: "not X but Y", "It's not X. It's Y", "less about X, more about Y". Test: delete the negated half; if what remains is trivial, the sentence made no claim. Real contrasts ("on conditionality, not size") are fine when the negated half is a position someone holds (name them).
- **Trailing significance clauses**: ", highlighting/underscoring/reflecting ...". Cut.
- **Uplift endings**, signposted conclusions ("In conclusion", "Ultimately", "To sum up"), meta-commentary ("It is important to note", "makes the central point concrete", "Two features matter."), announced counts ("Three bodies of work...") unless the count is the point and correct.
- **Vague attribution** ("commentators", "the conventional view", "scholars argue", "is believed"). Name who, with a citation, or cut.
- **Fractal summaries**: a section that previews and then recaps itself; repeating the same computation or verdict in several places. One roadmap paragraph in the introduction only.
- **Copula avoidance** ("serves as", "stands for", "represents" where "is" works).
- **Dead vocabulary**: delve, tapestry, intricate, pivotal, realm, testament, garner, bolster, landscape, interplay, crucial, nuanced, robust (except as a term of art), underscore.
- **Elegant variation**: same name for the same thing every time (see the terminology list in notes/v2/resolutions.md).

## Structure and rhythm
- Vary sentence length (target burstiness, stdev/mean of sentence length, above 0.5) and paragraph length. Short sentences where a point stands alone.
- No paragraph ends by restating its first sentence.
- Lists of two, four or five where the content has two, four or five items. Do not default to triads.
- Prose over bullets when items are related.
- Light concession: clause-final "though" is fine; avoid stacking "However"/"Moreover".

## Substance
- Take positions. Attach hedges to an agent: "we think", "on our reading", "we cannot rule out". Avoid impersonal "it may be argued", "appears to".
- Concrete particulars (dates, numbers, named cases) only if sourced in the notes; cite them. If a needed particular is unknown, say so; never invent.
- Cross-reference constantly with \cref (Proposition~\cref{...}, \cref{sec:...}, \cref{fig:...}).
- Show where cited works disagree (e.g., Gerzhoy 2015 vs Lanoszka 2018 on West Germany; Kroenig 2009 vs Gray 2012 on commercial motives).
- State scope conditions in the theory sections.
- Do not overclaim: "the record is consistent with", "we read X as", not "X confirms the model".

## LaTeX conventions
- Citations: \citet{key} / \citep{key}; only keys in paper/refs.bib.
- Use \pos{...} for positive part; \cref / \Cref (cleveref loaded); theorem environments: proposition, lemma, corollary, remark, definition, assumption (amsthm).
- Use \emph sparingly. \paragraph{...} run-in heads are fine.
- Figures: \includegraphics[width=...]{figures/fig_x.pdf}; tables with booktabs.
- Each section file starts with \section{...}\label{sec:...}.
