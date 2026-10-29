# Citation and fact check of the v2 draft (tag: citations)

Checked 29 October 2026 against paper/refs.bib (609 entries), notes/v2/facts_record.md, facts_history.md, lit_theory.md, lit_security.md, lit_ipe.md, integration_notes.md, and notes/review/*.md (asml_facts, e2031, security, eu_inst, lit_ai, gap_*). Files read in full: 01_intro, 02_background, 03_literature, 07_decide, 08_evidence, 09_implications, C_scenario, 10_conclusion, 00_abstract; every citing sentence with a date, number or quote in 04_model, 05_slack and 06_control.

## Verdict

The factual record in the draft is mostly sound. Dates, percentages, quotes and the Council arithmetic match the verified notes almost everywhere. The problems are of four kinds.

1. **Primary keys that now exist are not used.** Every key the drafters reported missing (eu2025dualuse, stcrt2024duv, stcrt2025metrology, bis2025rescission, kst32637_717, kst32637720, bis2025affiliates, kaag2020asml, allen2025deepseek) is now in refs.bib, together with bis2025affiliatesrule, govnl2023controls, asml2026q3pres and stcrt2025_38653. Nine sentences still cite ASML's 20-F, a law-firm note or a news item for facts whose primary source is now available, and three TODO comments remain.
2. **One unverified source carries a whole narrative.** taylorwessing2025nexperia was never verified (the site was blocked during the asml_facts check), yet sec:record cites it four times for the Nexperia sequence. The Kamerstukken letters 720 and 717 support every one of those facts.
3. **A few claims go beyond their sources.** These are: the AI Diffusion Rule "rescinded before it took effect" (a rescission was announced, not published, and the rule's compliance date had not arrived); Lake (2009) resting authority "partly on legitimacy" (not in any verified note); Pauly's "assurance" used for reassurance of other allies (Pauly means assurance that compliance will not be punished); Schelling (1960) cited for a point from Arms and Influence (1966); the 2019 EUV licence "lapsed" (the primary source shows the application still pending in October 2020); and Drezner's allies who "often" win concessions (Drezner says they "can").
4. **Duplicate bibliography entries.** refs.bib holds at least 19 pairs or triples of keys for one work. One duplicate prints twice in the reference list: the same 2024 Bloomberg story is cited as bloomberg2024disable in 06_control and bloomberg2024killswitch in 07_decide.

Integration-notes section 1 corrections: (1) the Europe 2031 quote is verbatim in the intro and appears nowhere else; (3) "eight authors" is correct and the bib entry lists eight; (2) the Huawei/DUV route is only half done in 02_background (finding 11); (4) the power indices do not appear in the main text, but B_numerics says sec:council uses them (finding 25).

Verified as correct and needing no change: Europe 2031 date, byline and every scenario quote (including "the only card Europe still holds", now verified on the summary page); the MATCH Act dates and content; Jetten's 13 April dinner; tk2026match (12 May, Sjoerdsma, translation); Japan's 23 equipment types and "not aligning" quote; the Supplement No. 4 quote, country count and scope; China's sales shares (26.3, 36.1, 29.1 percent); 8,242 US staff (18.7 percent); Zeiss quote; Decree 834 and 835 dates and content; Nuctech determination of 15 May 2026; rare-earth dates (4 April 2025, 10 November 2026, 10 January 2027); the Hegseth order and Merz quote; Spain's airspace closure and Rubio quote; the NSS and August 2025 joint statement quotes; Vifo and preference-share facts; ACI deadlines; BEV vote (10/5/12, adopted 29 October 2024); all tab:council percentages (verify_m2); 70.46/29.54 and 28.06 percent; servicing numbers in sec:holdup (EUR 0.34bn and 1.9bn a month, US$3.9 to 4.8bn, multiplier 5 to 12, 50 to 70 percent local repair, Beijing repair centre, Fomenkov collector figures); every FRUS fact in sec:cases (offsets, CoCom 1957, FRG-Brazil); Heisenberg, Häge, Novak; Leeds, Gerzhoy, Lanoszka, Blankenship 2021 and 2023, Carson et al., Cooley 2008/2009/2012, Kroenig, Gray, Miller, Coe, Wolford and Kim, Fang et al., Dekel et al. Prop. 2, Banks, Bueno de Mesquita and Smith, Lacy and Niou, Farrell and Newman pp. 56-58 and 76, Kalyanpur and Newman, Bown, Chen and Evers pp. 194-195, Gholz and Hughes, CMS (B.3.1, B.2, the slack quote, the JPE self-binding result), Krainin, Bas and Coe, Spaniel, Benson and Smith, Harstad, Frieden, Morita and Waldman.

## Findings

Severity: essential = wrong, unsupported or unsourced as printed; important = secondary source where a primary key exists, or wording that overstates its source; minor = precision or housekeeping.

### Essential

**1. 08_evidence.tex, Nexperia narrative rests on an unverified source.**
Anchor: "after a US rule threatened Nexperia's operations, the economy minister used the Goods Availability Act to take control of the firm"
Problem: taylorwessing2025nexperia is cited four times (order, CEO suspension, China's export block, the 19 November suspension), but no note verified it; asml_facts.md lists Taylor Wessing among the sites that could not be fetched. Primary keys now in refs.bib cover every fact: kst32637720 (timeline: decision 25 September, order 30 September, provisional CEO suspension 2 October, China's Nexperia export control 4 October), kst32637_717 (suspension of 19 November; the Enterprise Chamber's measures remain), bis2025affiliatesrule (90 FR 47201, effective 29 September) and bis2025affiliates (the one-year suspension). The carmaker clause has no verified key. The TODO comment at the end of the paragraph is answered by kst32637_717.
Fix: replace from "On 30 September, after a US rule" to the end of the TODO comment with:
"On 30 September, the day after the Affiliates Rule took effect \citep{bis2025affiliatesrule}, the economy minister used the Goods Availability Act to take control of the firm, and the Enterprise Chamber suspended the chief executive in early October \citep{kst32637720, gerechtshof2025nexperia}. On 4 October China announced an export control aimed at Nexperia's Chinese plants \citep{kst32637720}. At Busan on 30 October, Washington agreed to suspend the Affiliates Rule for one year from 10 November, and China agreed to ``take appropriate measures to ensure the resumption of trade from Nexperia's facilities in China'' \citep{fmprc2025busan, whitehouse2025busan, bis2025affiliates}. On 19 November the Dutch minister suspended his order. The Enterprise Chamber's measures were separate from it and stayed in force \citep{kst32637_717}."
Also delete taylorwessing2025nexperia from the tab:cases "Sources by row" note and put kst32637720, kst32637_717 there instead.

**2. 07_decide.tex and C_scenario.tex: the AI Diffusion Rule was not "rescinded before it took effect".**
Anchors: "The rule was rescinded before it took effect" (07_decide) and "The real AI Diffusion Rule, rescinded before it took effect," (C_scenario)
Problem: The interim final rule was published on 15 January 2025 (bis2025diffusion) and its compliance requirements were due on 15 May 2025. On 13 May 2025 BIS *announced* a rescission and told enforcement officials not to enforce the rule. As of 29 October 2026 the Federal Register contained neither the formal rescission nor the promised replacement (facts_record 11.3; lit_ai row 150).
Fix (07_decide): "BIS announced its rescission two days before the compliance date and does not enforce it (\cref{sec:background}), so tiering is a latent instrument, but it shows how one rule can reward the gatekeeper and split the Council at once (\cref{sec:council})."
Fix (C_scenario): "The real AI Diffusion Rule, which BIS withdrew before compliance was due,"

**3. 02_background.tex: uncited quote with a TODO comment (rescission).**
Anchor: "downgrading them to second-tier status.''"
Problem: The key bis2025rescission is now in refs.bib. The Federal Register status is also missing and is needed to support finding 2.
Fix: replace the quote's end and the TODO comment with: "downgrading them to second-tier status'' \citep{bis2025rescission}. By late October 2026 neither the formal rescission nor a replacement rule had appeared in the Federal Register."

**4. 02_background.tex: Section 1250A has no bib key (TODO).**
Anchor: "Section 1250A of the FY2024 National Defense Authorization Act bars withdrawal"
Problem: The statute is cited inline only and the TODO comment remains. Source: security.md row 43 (Pub. L. 118-31, 22 Dec 2023; 22 U.S.C. 1928f; Kaine-Rubio amendment adopted 65 to 28 on 19 July 2023).
Fix: add to refs.bib
`@misc{usc1928f, author={{United States Code}}, title={22 U.S.C. \S~1928f, Limitation on Withdrawal from the North Atlantic Treaty}, howpublished={Enacted as Section 1250A of the National Defense Authorization Act for Fiscal Year 2024, Pub. L. 118-31, 22 December 2023}, year={2023}, url={https://www.law.cornell.edu/uscode/text/22/1928f}}`
and write "...without the consent of two-thirds of the Senate or an Act of Congress \citep{usc1928f}." Delete the TODO comment.

**5. 02_background.tex: uncited brigade-combat-team claim (TODO).**
Anchor: "Later that month the US brigade combat teams based in Europe were cut from four to three,"
Problem: No key; the only source is a Washington Examiner report of 19 May 2026 (security.md row 57, corrected wording "2021 levels"). The sentence is not needed for the argument, since the Hegseth order and the NBC report already make the point that posture is cheap to move.
Fix: delete the clause and its TODO comment, so that the sentence reads: "...``recent German rhetoric'' \citep{martinez2026germany}, and in September the Pentagon was weighing a drawdown of 25,000 or more troops \citep{nbc2026pentagon}." (Saves 15 words.) If the clause is kept, add a key for https://www.washingtonexaminer.com/?p=4575626 (19 May 2026).

**6. 01_intro.tex: paragraph 2 cites ASML's 20-F and a dead government page for regulatory facts, and overstates the 2019 episode.**
Anchor: "In 2019, after US lobbying reported by Reuters, the Dutch government let ASML's licence to ship an EUV machine to China lapse without renewal"
Problem: (a) The only primary source on 2019 (kaag2020asml, the trade minister's letter of 27 October 2020) shows ASML's application still pending in October 2020; the "lapse" and the lobbying account come from Reuters via NL Times and were not independently confirmed (asml_facts.md, Position 2 and corrections). (b) govnl2023export points to a government.nl page that now returns 404; govnl2023controls (Staatscourant 2023, 18212) replaces it. (c) The September 2024, January 2025 and November 2025 measures now have primary keys (stcrt2024duv, stcrt2025metrology, eu2025dualuse). The in-force date of 1 April 2025 and the regulation number come from these, not from the 20-F, which wrongly gives 15 January 2025 as "effective".
Fix: replace the first four sentences of paragraph 2 after "(\cref{sec:background})." with:
"From 2019 the Dutch government left ASML's application to ship an EUV machine to China undecided, after US lobbying reported by Reuters; it was still pending in October 2020 \citep{nltimes2020pressured, kaag2020asml}. National licensing of advanced immersion lithography took effect on 1 September 2023 \citep{govnl2023controls}. In September 2024 licensing for the older NXT:1970i and NXT:1980i moved from Washington to The Hague \citep{stcrt2024duv, asml2024license}, a measure on metrology and inspection systems published in January 2025 took effect on 1 April 2025 \citep{stcrt2025metrology}, and in November 2025 the EU put the most advanced immersion tools on the Union control list through Delegated Regulation 2025/2003 \citep{eu2025dualuse}."

**7. 02_background.tex: the control sequence uses secondary keys and carries a TODO comment.**
Anchor: "In 2019 the Dutch government let a licence for an EUV shipment to China lapse, reportedly after US lobbying"
Problem: The same issues as finding 6, plus the leftover TODO comment for eu2025dualuse.
Fix: replace the paragraph's citations as follows.
- First sentence: "From 2019 the Dutch government left ASML's application to ship an EUV machine to China undecided, reportedly after US lobbying; it was still pending in October 2020 \citep{nltimes2020pressured, kaag2020asml}."
- "...on 30 June 2023, in force from 1 September 2023 \citep{govnl2023controls}"
- "...rather than Washington for these shipments \citep{stcrt2024duv, asml2024license}"
- "...in force from 1 April 2025 \citep{stcrt2025metrology}"
- "On 15 November 2025 Commission Delegated Regulation (EU) 2025/2003 put the most advanced immersion tools on the EU list \citep{eu2025dualuse}. ASML reported that this ``did not mean a change'', and the licence decision stayed in The Hague \citep{asml2026annual, eu2021dualuse}." Then delete the TODO comment. Note that "because the tools already needed a Dutch licence" is our gloss, not ASML's words. Drop it, or keep it outside the quotation as it is now.

**8. 06_control.tex: secondary keys for the 2024 and 2025 binding steps and for the Nexperia order.**
Anchors: "the licence decision stayed in The Hague \citep{eu2021dualuse, asml2026annual}" and "In 2025 the Dutch state issued an order under the Goods Availability Act against Nexperia \citep{gerechtshof2025nexperia}"
Problem: The Delegated Regulation now has its own key. The Enterprise Chamber ruling records the order but is not its primary source; the government timeline (kst32637720) is.
Fix: "When Delegated Regulation 2025/2003 put the most advanced immersion tools on the EU list in November 2025 \citep{eu2025dualuse}, the licence decision stayed in The Hague \citep{eu2021dualuse, asml2026annual}." and "On 30 September 2025 the Dutch state issued an order under the Goods Availability Act against Nexperia \citep{kst32637720}". Also add stcrt2024duv to the September 2024 sentence: "...from Washington \citep{stcrt2024duv}, a change that ASML said...".

**9. 06_control.tex and 07_decide.tex: one Bloomberg story under two keys.**
Anchors: "that ASML had told Dutch officials it could disable machines remotely \citep{bloomberg2024disable}" (06_control) and "``without ASML's spare parts they quickly stop working'' \citep{bloomberg2024killswitch}" (07_decide)
Problem: Both keys are the same May 2024 Bloomberg report (Baazil, Koc and Robertson; reprinted in the Taipei Times on 22 May 2024). The reference list will print it twice. Only the Taipei Times reprint was read (gap_servicing row 3); the Bloomberg URL was not checked.
Fix: cite bloomberg2024killswitch in both places and delete bloomberg2024disable from refs.bib. Alternatively, keep the Bloomberg original as the single key and add the note "reprinted in Taipei Times, 22 May 2024, p. 12" to it.

### Important

**10. paper/refs.bib: duplicate entries for the same work.**
Anchor: "@techreport{fedasiuk2026aei,"
Problem: Only the one in finding 9 prints twice today, but each duplicate is a trap for the next edit. Pairs (the key the paper cites comes first; delete the others): aei2026lithography / fedasiuk2026aei; asml2026annual / asml2026form20f; asml2026q3 / asml2026q3pr; juijn2026europe / juijn2026europe2031; whitehouse2025nss / nss2025; tk2026match / ahtk20252026_1903; kst32637_717 / kst32637717 / karremans2025nexperia717; kst32637720 / karremans2025nexperia720; reedsmith2026decree / reedsmith2026decree835; vangerven2026dutch / vangerven2026sjoerdsma; ec2024bev / commission2024bev; council2025population / council2025decision2427; miller2022chip / miller2022chipwar; asml2024license / asml2024stmt; allen2022choking / allen2022csis; reuters2025euv / potkin2025reuters; ecfr2026home / kobzova2026home / ecfr2026homealone; bloomberg2024killswitch / bloomberg2024disable (finding 9). clayton2023geoeconomics is the NBER version of clayton2026framework. Keep it only if a WP page is pinpointed.
Fix: delete the second and later keys in each group. Before deleting, copy any better metadata into the kept entry: the url fields of asml2026form20f, asml2026q3pr, kst32637717 and nss2025, and the "Copywriting and editing by Tom Chivers" note of juijn2026europe2031.

**11. 02_background.tex: the China DUV route still lacks the integration-notes correction and cites a think-tank phrase where a direct source exists.**
Anchor: "Chinese fabs have used that route toward the advanced nodes on which domestic AI accelerators are made"
Problem: Integration note 1.2 requires saying that Huawei's Ascend accelerators are made at 7 nm without EUV, through DUV multiple patterning. allen2025deepseek is now in refs.bib and supports the node claim ("likely remains stuck at the 7 nm technology node until and unless they develop a domestic EUV lithography capability"; lit_ai). The sentence also cites aei2026lithography twice.
Fix: "Exposing the same layer several times (multiple patterning) lets these tools print features that would otherwise need EUV. SMIC makes 7 nm logic this way, and Huawei's Ascend AI accelerators are built on it, but without EUV China is likely to stay at about 7 nm \citep{allen2025deepseek}; in the phrase of \citet{aei2026lithography}, China is ``printing its way'' toward self-sufficiency." Also check the opening sentence of the subsection ("the most advanced US AI accelerators"). It is correct as written; do not widen it to "AI chips".

**12. 03_literature.tex and 08_evidence.tex: Lake (2009) "legitimacy" is not in any verified note.**
Anchors: "sustained partly by legitimacy" (03_literature); "rests on protection already provided and partly on legitimacy" (08_evidence); "Authority bounded issue by issue by legitimacy" (08_evidence, tab:implications)
Problem: The draft issues file says the wording came from Referee 2's description. The verified characterization (lit_alliance.md) is relational authority grounded in a social contract: the dominant state provides order, and the subordinate state complies.
Fix (03): "\citet{lake2009hierarchy} treats the patron's authority as relational, a social contract in which the patron provides order and protection and the subordinate complies." Fix (08 text): "In \citet{lake2009hierarchy} compliance is owed to a patron whose authority rests on a social contract: it provides order and protection, and the subordinate complies;". Fix (table cell): "Authority bounded issue by issue by the social contract".

**13. 01_intro.tex and 05_slack.tex: Pauly's "assurance" is not the paper's assurance cost.**
Anchors: "makes conditionality a choice with an assurance cost \citep{pauly2024damned}" (01_intro); "In our model those steps are the stakes that raise $\kappa$, and part of their cost is $H$." (05_slack)
Problem: lit_security.md: Pauly's "assurance" means the coercer's promise not to punish a target that complies, and his case is an adversary (Iran). In the paper, H is the discount that other allies put on a guarantee with a broad withdrawal rule, plus the risk of mistaken triggering (05_slack: "other allies discount a guarantee..."). Citing Pauly for H misattributes the concept.
Fix (01): "\Cref{prop:conditionality} makes conditionality a choice with a cost in allied assurance." (drop the citation, or move it to 05 where the relation is explained). Fix (05): "In our model those steps are the stakes that raise $\kappa$. Pauly's cost falls on the target's confidence that compliance ends the threat; ours, $H$, falls on other allies and on the risk of a mistaken trigger, so the two are related but not the same."

**14. 05_slack.tex: Schelling (1960) cited for a point from Arms and Influence.**
Anchor: "The problem is an old one in the theory of strategic moves \citep{schelling1960strategy}"
Problem: The point that a threat meant to induce compliance needs the assurance that compliance will end it is from Schelling (1966, Arms and Influence), not The Strategy of Conflict. The drafter could not locate it in 1960. schelling1966arms is now in refs.bib. lit_commit.md made the same kind of correction for "salami tactics".
Fix: "\citep{schelling1966arms}". Leave the 04_model citation of schelling1960strategy for "a threat that leaves something to chance" unchanged; that one is correct.

**15. 08_evidence.tex: China's quarterly share is cited to the wrong documents.**
Anchor: "China's share of ASML's system sales rose from 14 percent in the second quarter of 2026 to 23 percent in the third \citep{asml2026q2call, asml2026q3}"
Problem: Both figures are on slide 9 of the Q3 2026 investor presentation (asml_facts row 78: "China 23% (Q2: 14%)"). The press release (asml2026q3) and the Q2 call transcript do not give them.
Fix: "\citep{asml2026q3pres}".

**16. 08_evidence.tex: the cost-minimization rival rests on two unverified works.**
Anchor: "sizes sanctions so that punishing a small offence does not erode deterrence of a large one \citep{stigler1970optimum, shavell1992note}"
Problem: No note in notes/v2 or notes/review verifies stigler1970optimum or shavell1992note. They appear only in v1 drafts and in review_style.md. A column of tab:implications depends on them.
Fix: check both against the texts before submission (Stigler 1970, JPE 78(3): 526-536, on marginal deterrence; Shavell 1992, IRLE 12(3): 345-355). Until then, shorten the clause to "A cost-minimizing coercer polices each demand with the cheapest credible instrument." Cite the two papers only once their content is confirmed.

**17. 01_intro.tex and 08_evidence.tex: Drezner overstated.**
Anchors: "though rare, often wins concessions" (01_intro); "while allies win them when they try" (08_evidence)
Problem: Verified wording (lit_security; Drezner 1999 abstract): allies are reluctant to coerce, "but when they do they can win significant concessions." Neither "often" nor "win them when they try" is supported.
Fix (01): "finds that coercion among allies, though rare, can win significant concessions". Fix (08): "while allies, who rarely coerce one another, can win significant concessions when they do."

**18. 07_decide.tex: Nexperia sentence uncited.**
Anchor: "In the Nexperia case the Dutch state used the Goods Availability Act to compel a firm and suspended the order seven weeks later"
Problem: The drafter left it uncited because the key was missing. kst32637720 and kst32637_717 now exist. The source also gives the stated reason for the suspension: China resumed export licences for Nexperia chips (gap_dutch row 6).
Fix: "In the Nexperia case the Dutch state used the Goods Availability Act to compel a firm on 30 September 2025 and suspended the order on 19 November, after China had blocked and then resumed exports from Nexperia's Chinese plants \citep{kst32637720, kst32637_717}; we read the suspension as evidence that $\zeta$ is high when China retaliates against the compulsion itself (\cref{sec:record})."

**19. 02_background.tex: the residual Dutch national list is cited to the 20-F.**
Anchor: "Tools left on the Dutch national list still need a Dutch licence to leave the EU \citep{asml2026annual}"
Problem: The primary source is now in refs.bib: stcrt2025_38653 (Regeling of 20 November 2025, in force from 15 November 2025). It moved the supplementary national items into Annex I and leaves 3B801.f.6 and f.7 as national items (the NXT:1970i and 1980i class and throughput upgrades), licensed under Article 9 of Regulation 2021/821 (gap_dutch row 9).
Fix: "Tools left on the Dutch national list, the NXT:1970i and NXT:1980i class, still need a Dutch licence to leave the EU \citep{stcrt2025_38653}".

**20. 02_background.tex: the CEO's supply statement is not EUV-specific.**
Anchor: "its chief executive said that planned EUV supply for 2027 and 2028 would not fully meet demand"
Problem: The verified quote is "our supply as currently planned for both 2027 and 2028 will not fully meet the demand of our customers" (asml_facts row 65). It covers all of ASML's supply. The EUV-specific statement is the CFO's July remark that 2027 Low-NA EUV is "close to being fully covered with orders" (asml2026q2call).
Fix: "In October 2026 its chief executive said that ASML's planned supply for 2027 and 2028 would not fully meet customer demand \citep{asml2026q3}."

### Minor

**21. 01_intro.tex: who makes the 2031 offer.**
Anchor: "the White House proposes to the leaders of the Netherlands, Germany and France"
Problem: In the scenario the US vice president delivers the offer in a forty-minute call (integration notes; e2031 row "March 2031").
Fix: "the US vice president offers the leaders of the Netherlands, Germany and France a joint Dutch-American holding company in which Washington holds a controlling vote over output, customers and technology transfer."

**22. C_scenario.tex: the authors' disclaimer wording.**
Anchor: "Its authors say the storyline is not meant to be a forecast"
Problem: The verified wording (europe2031.ai/about) is "is not meant to be a prediction". "A bet, not a forecast" is Kaltheuner's title, so "forecast" risks blending the two.
Fix: "Its authors say the storyline ``is not meant to be a prediction''".

**23. 07_decide.tex: date of Spain's base refusal.**
Anchor: "In March 2026 Spain refused US use of jointly operated bases for the Iran war and closed its airspace to the aircraft involved"
Problem: The date Spain first refused base use is unverified; the source only says Spain was "already barring" base use when it closed its airspace on 30 March (facts_record 12.2). 02_background words this correctly.
Fix: "By 30 March 2026 Spain was refusing US use of jointly operated bases for the Iran war, and on that day it closed its airspace to the aircraft involved \citep{roque2026spain}."

**24. 09_implications.tex: VEU status belongs to the fabs, not the tools.**
Anchor: "Korea's fabs in China run on US-origin tools whose validated end-user status BIS withdrew in 2025"
Fix: "Korea's fabs in China, whose validated end-user status BIS withdrew in 2025, run on US-origin tools \citep{bis2025veu}". The same paragraph should cite eu2025dualuse wherever it names Delegated Regulation 2025/2003. Its anchor is "Delegated Regulation 2025/2003 put the most advanced immersion tools on the EU list (\cref{sec:bind})"; add \citep{eu2025dualuse} before the cref.

**25. B_numerics.tex: power indices are claimed to be used in sec:council, but they are not (integration correction 4).**
Anchor: "\Cref{sec:council} and \cref{app:scenario} use these numbers."
Problem: Neither section reports Shapley-Shubik or Banzhaf indices. If editors add them to sec:council, use the corrected values (gap_council row 44), not eu_inst's 17.7.
Fix: "\Cref{sec:council} and \cref{app:scenario} use the population shares and pivot sets. The indices are 17.54 percent (Shapley-Shubik) and 12.03 percent (normalized Banzhaf) for Germany against 3.66 and 3.80 percent for the Netherlands, ratios of 4.8 and 3.2."

**26. 06_control.tex: source of the "sole licensing authority" quote.**
Anchor: "``is the sole licensing authority'' \citep{asml2024license}"
Problem: The press release page was never read. The quote was verified in ASML's FY2024 20-F (facts_record 1.2; refs.bib note on asml2024stmt).
Fix: "\citep{asml2025annual}". Keep asml2024license only if someone reads the release.

**27. 01_intro.tex, 04_model.tex, 05_slack.tex: CMS quote pinpoint and version.**
Anchor: "\citet{clayton2026putting} write that ``threats generate power to the extent that they generate slack in the participation constraint''"
Problem: The quote was verified in NBER WP 33681, p. 2 (gap_closest row 4), while the key is the Macroeconomics Annual version (vol. 40, pp. 23-87), whose text was not read.
Fix: check the published page and add it as a pinpoint (\citealp[p.~XX]{clayton2026putting}), or add "Working paper version quoted" to the bib note. Also see cut 3: the quote appears four times.

**28. 08_evidence.tex: Busan expiry paragraph.**
Anchor: "The US suspension of the Affiliates Rule ran for one year from 10 November 2025"
Fix: cite the rule itself: "\citep{bis2025affiliates, whitehouse2025busan, mofcom2025pause}". bis2025affiliates also records that reimposition was written into the rule for 10 November 2026.

**29. 00_abstract.tex: Japan's alignment dates from 2023.**
Anchor: "has aligned its export controls with US demands while extracting little in return, as has Japan"
Fix: "as has Japan since 2023".

**30. 03_literature.tex: Fearon (1996) content not checked.**
Anchor: "finds efficient, gradual transfers when power varies continuously with holdings, and breakdown when it jumps"
Problem: No note verifies this summary against the manuscript (gap_closest flags it for a re-read). The paper already says it is unpublished.
Fix: confirm against the manuscript. If that is not possible, shorten the summary to "studies bargaining over objects that shape future bargaining power, in which a discontinuous shift can cause breakdown \citep{fearon1996bargaining}".

**31. 01_intro.tex: the "only card" quote now has a verified location.**
Anchor: "``the only card Europe still holds''"
Problem: The quote is verified on the scenario's summary page (integration notes), not in the narrative, which says "But Europe has one last card to play." The citation points to the site root.
Fix: none needed in the text. Add to the juijn2026europe note: "Quoted phrase from the summary page."

## Cuts, merges and moves that also fix citation problems

The same facts and quotes recur across sections, and each repetition is one more place for a citation to drift. Consolidating them saves about 650 words of main text.

1. **Supplement No. 4 quote ("have the authority to control key SME items of concern") appears five times** (01, 02, 06, 08, 10). Keep it in 02_background (full) and in 08_evidence sec:coding (the coding rule). In 01_intro keep the clause "BIS can withdraw the status by amending a rule" and drop the quote. In 06_control replace the sentence with "The December 2024 exclusion is the same reward for self-binding (\cref{sec:coding})." In 10_conclusion drop the quote and keep "a place on Supplement No.~4, which BIS can revoke by amending a rule". Saves about 90 words.
2. **The Dutch control sequence is narrated four times** (01 para 2, 02 last para, 06 sec:bind, 08 sec:record). Keep the full dated sequence with primary keys only in 02_background (finding 7). Cut 01 para 2 to two sentences: "Since 2019 The Hague has aligned its controls in steps, from 2023 each following a US move, and in November 2025 the EU listed the most advanced immersion tools (\cref{sec:background}). What The Hague received was a status." Then keep the Supplement No. 4 sentences. This saves about 110 words and leaves one place to maintain the citations of findings 6 and 7.
3. **The CMS slack quote appears four times** (01, 04 line 65, 05 line 3, 05 "What is new here"). Keep it in 01 and in 05 "What is new here". In 04 cut the sentence "We take the term from ... \citep{clayton2026putting}." to "We take the term from \citet{clayton2026putting}." and delete the 05 opening sentence that repeats the credit. Saves about 60 words.
4. **The MATCH Act objection is quoted or paraphrased five times** (01, 02, 06, 08, 10). Keep the translated quote in 01 and the "national security in American hands" quote in 02. In 08 cut to "The Dutch answer was voice (\cref{sec:background})." In 06 keep only the inference about $\sigma_d$ with a cref. In 10 keep the closing quote only if 01's is cut, since the two are near-identical translations of the same sentence. Saves about 80 words.
5. **Manas appears four times** (01, 03, 08, 09). Keep 03 (with the chapter cite) and 01. Cut the Manas clause from 08 sec:predictions ("as Kyrgyzstan was for Manas...") and the Kyrgyzstan sentence from 09 sec:scope. Saves about 60 words.
6. **The NSS "more favorable treatment" quote appears three times** (02, 05, 08). Keep it in 05 sec:conditionality, where it is analysed. In 02 shorten to "The National Security Strategy of December 2025 offers better treatment to countries that align their export controls \citep{whitehouse2025nss}." In 08 replace with a cref to sec:conditionality. Saves about 50 words.
7. **The AI Diffusion Rule tiers appear three times** (02, 04 line 35, 07). Keep 02 (with the corrected status, findings 2 and 3) and 07 (the Council arithmetic). Cut the 04 sentence. Saves about 30 words.
8. **Taiwan 50-50 appears three times** (06, 08 table, 09). Keep the 06 sentence and the table row; in 09 cut to "Taiwan fails the third condition: China threatens it and does not bid for it." Saves about 35 words.
9. **Decree 834/835 is described four times** (01, 02, 07, 08). Keep 02. In 07 sec:firm and 08 cut each description to a clause with \cref{sec:background}. Saves about 60 words.
10. **Nuctech appears three times** (02, 05, 09). Keep 02; in 05 and 09 refer back. Saves about 35 words.
11. **The brigade-combat-team clause in 02** (finding 5): cut.
12. **tab:cases "Sources by row" note**: after finding 1, the Netherlands row should cite kst32637720 and kst32637_717, not taylorwessing2025nexperia.
13. **Move to app:scenario**: the 07_decide paragraph on the scenario's 2029 Council vote (from "The same arithmetic applies to the Council vote in \emph{Europe 2031}" to its end, about 80 words) duplicates C_scenario's 2029 paragraph. Move its two numerical sentences to C_scenario and leave a one-line cref in 07.
