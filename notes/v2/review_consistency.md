# Consistency review of the v2 draft (tag: consistency)

Scope: paper/sections/00 to 10, A_proofs, B_numerics, C_scenario, preamble.tex, figures/make_figures.py, checked against notes/v2/resolutions.md, style_brief.md, integration_notes.md (including the late section on verified scenario quotes), draft_issues.txt and the verification reports. Anchors are exact phrases from the files. Replacement text follows the house style (no em dashes).

## 0. Verdict

The formal core is in good shape. Every numbered statement in the main text matches its verified block in verify_m1 to verify_m4 modulo the notation changes in resolutions.md, labels and part numbering match resolutions.md and main.aux, and every proof in A_proofs proves the statement it is attached to. Nothing in the appendix proves a different result. The problems are of four kinds.

1. **The thesis sentence is stated more strongly than Proposition 1 allows.** The abstract, the introduction and the conclusion say that the holder's leverage is "bounded by its exit premium" and that a hub confers power "only if the holder's exit premium is positive". By Proposition 1 and Corollary 1(c), leverage can exceed the premium, and can be positive with a negative premium, when talks risk rupture and Europe has agenda power. The body says so. The framing sentences do not. Referee 1 raised the same point last round.
2. **Five places where the text claims more than the appendix proves.** These are Proposition 4(d)'s example (essential: it gets the sign of the silicon shield wrong), the Lemma 1 discussion ("weak dominance selects the price"), the scope of Corollary 5(iii) and variants (a) and (c), the reading of execution costs in Proposition 2(d), and the uniform case of Proposition 6(a). There are also two small gaps: Remark 1(c)'s example and Remark 4's delegated-act clause.
3. **Two wrong cross-references and several part-references that cite a nearby result for a claim it does not make.** The two wrong ones: sec:record is cited for the Supplement No. 4 coding (it is in sec:coding), and sec:predictions is cited for the direction of drift (it is not there).
4. **Heavy duplication across sections.** About 45 facts, quotes, credits and arguments are told in full in two to five places (Section 5 below). Removing the duplicates is the cheapest part of the cut to 19,000 words. My estimate is 3,000 to 3,500 words, with no loss of content.

Most of the drafters' open issues about missing bib keys are now solvable. bis2025rescission, eu2025dualuse, stcrt2024duv, stcrt2025metrology, kaag2020asml, allen2025deepseek, kst32637_717, kst32637720, bis2025affiliates and schelling1966arms all exist in refs.bib. Five TODO comments in the sections can therefore be resolved at once.

## 1. Formal statements: main text vs resolutions.md vs A_proofs

| Result | Label and number (main.aux) | Statement vs verified block | Proof proves the statement? | Issue |
|---|---|---|---|---|
| Lemma 1 bidding | lem:bidding, Lemma 1 | matches verify_m1 | yes | Text after the lemma overstates the alternating-raise claim (F4) |
| Prop 1 master | prop:master, Prop 1 | matches. (i), (ii) and (iii) as resolutions require. Discrete closed forms are in the appendix only | yes | none |
| Cor 1 | cor:master, Cor 1 | matches, and (e) uses the five channel names | yes | none |
| Prop 2 slack | prop:slack, Prop 2 | (a), (b), (c)(i) to (iii) and (d) "Assurance", as required | yes | (d) parenthesis needs "every nonempty J" (F6) |
| Cor 2 rationing | cor:rationing, Cor 2 | matches | yes | uses K as the number of demands (F18) |
| Prop 3 counter | prop:counter, Prop 3 | (a)(i) to (v) and (b) match | yes (weak tie in (b), consistent with "if and only if ... w_H >=") | none |
| Prop 4 conditionality | prop:conditionality, Prop 4 | matches resolutions, including the corrected (d) | (d): the appendix proves the derivative and gives a correct sufficient condition (G unimodal with mode at or below s_X - mbar_U). The text's example "Washington would almost surely defend a loyal Europe" is not sufficient | **F3, essential** |
| Prop 5 control | prop:control, Prop 5 | matches verify_m4 with iota and K | yes | none |
| Cor 3 | cor:control, Cor 3 | (a) to (d) merged as required; investment part includes the zero-bite purchase | yes | (d) reuses r, c, H (F17) |
| Lemma 2 | lem:selflimit, Lemma 2 | matches with scope conditions | yes | moving to appendix (Section 9) |
| Cor 4 windows | cor:windows, Cor 4 | matches (t' >= t; t' > t when u_t = 0) | yes, and the counterexample is in the appendix | none |
| Rem 1 bind | rem:bind, Rem 1 | matches the corrected block | yes, but (c) needs Delta_c = infinity, no investment and mbar_U >= 1, which the appendix states and the text omits | F8 |
| Prop 6 breakdown | prop:breakdown, Prop 6 | matches verify_m4 Prop 5 | yes | (a) uniform formula needs "when below sigma-bar" (F7); s_0, f and Pi clash (F16, F19) |
| Rem 2 gatekeeper | rem:gatekeeper, Rem 2 | matches | yes | none |
| Rem 3 firm | rem:firm, Rem 3 | matches, with the required qualifications | yes | none |
| Rem 4 council | rem:council, Rem 4 | matches | yes | "qualified majority against" for a delegated act should be "reinforced" (F9) |
| Prop 7 pain | prop:pain, Prop 7 | matches, with n(t), N(t), x°(t), psi and r > 0 | yes | none |
| Cor 5 interrupt | cor:interrupt, Cor 5 | matches verify_m2 | (iii) and variants (a) and (c) are proved only where exit never binds; the statement does not say so | F5 |

Labels: all labels in resolutions.md exist and carry the numbers resolutions.md assigns. LaTeX reports "Label(s) may have changed. Rerun", so rebuild once more before circulating. There are no "??" in the PDF.

## 2. Notation

- No leftover omega_b, omega_Delta, K_I, x_F, G(t), w as the per-unit value, or k as the issuing cost in the main text or the appendix. The figure legend uses psi (the drafter's issue is closed).
- Clashes that remain (Referee 1 asked last round for c, r, m, sigma and delta to be disambiguated):
  - **s_0** is the US own interest in European security (eq:kappa) and also the purchase-offer cutoff in Prop 6(b). Rename the cutoff s_P. (F16)
  - **r** is the discount rate (Props 1 and 7). In Cor 3(d) it is China's announced punishment, next to r_k and rbar_k (Prop 3) and r^c. **c_C** sits next to c (exit cost). **H_C** sits next to H(kappa). Rename them r^c, rbar^c, e^C(r^c) and z_C. (F17)
  - **f** is the firm penalty in eq:Q and also the density of sigma in Prop 6. **Pi** is the objective in Prop 4 and the gain in Prop 6. Write F' for the density and Pi_U for Prop 6. (F19)
  - **K** is the investment cost and also the dimension of y in Cor 2. (F18)
  - **N** is the number of dates in Lemma 2 and Cor 4, and also N(t) in Prop 7. (F21)
  - **g_1, g_s** (direct execution cost) sit next to g (density of crisis costs). (F22)
  - **phi_U** (in-kind cost, footnote to Lemma 1) and **varphi** (self-harm) look alike. (F20)
  - Lesser overloads that can stay but should be noticed: b (ratchet count in Prop 2(d), bite b_t in Cor 4, buffer stock in Cor 5(iii)); tau (China's promise, sunk demand cost in Prop 2(d), stopping time in Prop 7); W (China's gain) and W(S) (value of a demand set); S (concession set, date set, S_k).
- Rendering: cleveref has crefname lines only for proposition, lemma, corollary and assumption. The PDF therefore prints "remark 3", "section 5.3", "appendix A" and "figure 2" in lower case next to "Proposition 3". (F23)
- Figure 2 x-axis: "patron's stake V = 3". V is Washington's dependence, and "stake" is the paper's word for m. (F24)

## 3. Cross-references that name a result part

I checked every \cref{...}(x). Most are right. These are not:

- 06_control: "\cref{sec:record} codes it as a reward for self-binding". The coding is in sec:coding. (F10)
- 06_control: "\cref{sec:predictions} states what each answer implies". sec:predictions (tab:implications) does not discuss the direction of drift; 09_implications "Expect a preventive demand" does. Meanwhile 09 points back to sec:windows and sec:predictions, so the reader goes in a circle. (F11)
- 05_slack (Germany drawdown) and 09_implications (Lessons for Washington) cite prop:counter(b) for "spends the instrument". Spending is in the setup of Prop 2 (sec:slackprinciple). Only the premium increase is in the last sentence of Prop 3(b). (F12)
- 08_evidence: "a hedge that by \cref{prop:counter}(b) Washington polices with flow jurisdiction whenever that is credible". Prop 3(b) gives the conditions for each instrument. It does not say Washington chooses flow jurisdiction. (F13)
- 01_intro: the summary of Prop 3(a)(v) drops "sunk" ("a divisible demand China cannot threaten"). (F14)
- 01_intro: "gets nothing ... unless the dispute risks rupture" omits agenda power (beta > 0), which Cor 1(c) requires. (F15)

## 4. Numbers and dates repeated across files

All of these agree: 28.06 percent and the seven named states (07, B; C gives no number); 13 members and 26.77 percent (Rem 4, tab:council, A_proofs, verify_m2); 15.09 percent; 70.46 and 29.54 percent; Busan on 30 October 2025, the Affiliates Rule suspended from 10 November, China's suspension to 10 November 2026, the extension to 10 January 2027 (02, 08 twice); 5,000 troops and 1 May 2026 (02, 05, tab:cases); 25,000 or more troops in September 2026 (02, 05); 8,242 and 18.7 percent (02, matching facts_history 7.1); China shares of 26.3, 36.1 and 29.1 percent (02), "36 percent" in 2024 (01), "26 to 36 percent" (08, tab:cases), 14 and 23 percent of system sales in Q2 and Q3 2026 (08). China is ASML's largest market in 2025 (EUR 9.52bn against Taiwan 8.34bn and Korea 8.16bn): correct. The Nexperia dates (5 and 12 June, 30 September, early October, 19 November 2025; "seven weeks later" in 07) agree. The hold-up numbers (EUR 4.09bn, 0.34bn and 1.9bn a month; h about 0.85; 26 and 15 months) match gap_servicing_time_to_pain.md. The 20,199 and 1,202 figures appear in both 06 and B.

These disagree with a verified source:
- **Council completion of the scenario seven (07 and C).** "Germany, France or Spain would also have to withhold support, or six more members of any size" (07). "(six more, or a large state)" (C). gap_council_revealed_positions.md (rows 41 and 44) says three suitably chosen further states complete a block by population (for example Belgium, Czechia and Portugal), and that no two-state completion exists. "Six more" is sufficient by number but is not the minimum. (F25)
- **Hungary (07).** "Hungary's support is doubtful". Hungary changed government on 9 May 2026 (integration_notes; gap_council memo), so the HU-SK-CZ group is not a fixed bloc. (F26)
- **Quote wording.** tk2026match is rendered as "every country is responsible for its own export-control legislation" (06) and "... export control legislation" (10). Use one form. (F27, minor)
- **"The only card Europe still holds".** This is now verified (integration_notes, scenario quotes) as appearing on the scenario's summary page, in the form "The only card Europe still holds is ASML". Attribute it to the summary page in 01. (F28; this closes drafter issues I3 and M8)

## 5. Home-rule violations (same fact, argument or credit told in full in more than one place)

Each item gives the anchors, where the item should live, and the approximate words saved.

| # | Item | Anchors | Home | Save |
|---|---|---|---|---|
| H1 | Supplement No. 4 exclusion, BIS quote and coding | 01 "We code it as a threat left unexercised for as long as Europe controls the items itself"; 02 "we code it as a threat left unexercised, equivalently a reward for self-binding"; 08 "The December 2024 exclusion of the Netherlands and the other countries on Supplement No.~4"; 06 "The December 2024 exclusion of exporters in the Netherlands"; 10 "What The Hague obtained in December 2024 was a place on Supplement No.~4" | fact and quote in 02; coding in 08 sec:coding; others cite | 220 |
| H2 | Dutch control sequence with dates and tool names | 01 "In September 2024 licensing for the older NXT:1970i and NXT:1980i"; 02 "The controls themselves arrived in steps"; 06 "In September 2024 The Hague took over licensing"; 08 "Since 2019 The Hague has aligned in steps, and from 2023 each step followed a US move" | 02 | 200 |
| H3 | 2019 EUV licence lapse | 01 "In 2019, after US lobbying reported by Reuters"; 02 "reportedly after US lobbying" | 02 | 35 |
| H4 | MATCH Act content and Dutch opposition | 01 "In April 2026 bills in both chambers of Congress, the MATCH Act"; 02 "The MATCH Act, introduced in Congress in April 2026"; 08 "The MATCH Act would police it by flow jurisdiction"; 06 "The Dutch government's answer to the MATCH Act"; 10 "What The Hague opposed in May 2026" | facts in 02; reading in 08 | 160 |
| H5 | CMS quote "Threats generate power..." | 01, 03 "state the principle we build on", 04 "for whom ``threats generate power", 05 "\paragraph{What is new here.}" | quote once in 01; credit by citation in 03, 04, 05 | 90 |
| H6 | CMS enforcement vs cut-off threats (B.3.1) and novelty list | 01 contribution 1; 03 "Each of these works lacks a result we derive"; 05 "What is new here" | 03 | 230 (from 05) |
| H7 | Bidding and outside-option credits | 03 "That a contested client earns what the losing bidder would pay is old"; 04 "None of this is new. It is the one-voter case"; 04 "The threshold in part (b) is the outside-option principle" | 03 for the list; 04 keeps one sentence for each result | 120 |
| H8 | Wagner 1988 | 01, 03 "Following \citet{wagner1988economic}", 04 "\citet{wagner1988economic} showed" | 04 (where the threshold is stated) | 40 |
| H9 | Kyrgyzstan and Manas | 01 "as Kyrgyzstan was"; 03 "In 2009 Kyrgyzstan announced the closure"; 08 "as Kyrgyzstan was for Manas"; 09 "Kyrgyzstan, which used a Russian aid package" | 03 for the fact; 01 one clause | 70 |
| H10 | Taiwan 50-50 | 06 "Washington floated one for Taiwan in 2025"; tab:cases; 09 "Taiwan fails the third condition" | tab:cases; 09 one clause | 60 |
| H11 | Scope placement of Taiwan and UAE | 08 "Taiwan and the United Arab Emirates fall outside the scope conditions"; 09 Scope paragraph | 09 sec:scope | 50 |
| H12 | Tokyo Electron retaliation threat | 05 "When Washington pressed Tokyo in 2024"; tab:cases; 09 "Beijing threatened retaliation when Washington pressed Tokyo" | tab:cases | 50 |
| H13 | Nuctech determination | 02 "Its first application was aimed at Brussels"; 05 "the first use of its new regulation on countering foreign extraterritorial jurisdiction"; 09 "such as the Nuctech investigation" | 02 | 40 |
| H14 | China does not punish alignment as such | 04 "\paragraph{Chinese punishment of alignment.}"; 05 "We do not let China punish alignment as such." | 04 | 60 |
| H15 | AI Diffusion Rule tiers and rescission | 02 "The AI Diffusion Rule of January 2025 put ten EU members"; 04 "The January 2025 AI Diffusion Rule placed ten EU member states"; 07 "The AI Diffusion Rule of January 2025 placed ten EU members"; C "The real AI Diffusion Rule, rescinded before it took effect" | 02; 04 keeps the inference only; 07 keeps the 70.46 computation | 110 |
| H16 | National Security Strategy quote | 02 "potentially through more favorable treatment"; 05 "It promises ``more favorable treatment on commercial matters"; 05 "The 2025 National Security Strategy ties favourable treatment"; 08 "The same rule codes the ``more favorable treatment''" | quote in 02; reading in 05 sec:conditionality | 50 |
| H17 | August 2025 joint statement | 02 "In the August 2025 joint statement on trade"; 05 "So are the trade terms of August 2025"; 05 "in the August 2025 joint statement the United States undertook"; 06 "The August 2025 joint statement, in which the EU said" | 02 | 80 |
| H18 | Germany withdrawal and the 25,000 drawdown | 02 "Defense Secretary Hegseth ordered about 5,000 troops"; 05 "Two kinds of US drawdown have opposite places in the model."; 08 "Nor do the security signals of 2025 and 2026 settle it." | facts in 02; reading in 05 (shortened); delete 08 paragraph | 150 |
| H19 | Spain base access | 02 "Spain was already refusing US use of jointly operated bases"; 07 "In March 2026 Spain refused US use of jointly operated bases" | fact in 02; 07 keeps the hold-up reading | 30 |
| H20 | Keohane sensitivity vs vulnerability | 03 "separated sensitivity, the cost of a cutoff before anyone adjusts"; 07 "\citet{keohane1977power} distinguished sensitivity" | 07 | 30 |
| H21 | Fearon (1996) unpublished, Benson and Smith, Debs/Bas/Spaniel, Krainin/Powell, Harstad | 03 "\citet{fearon1996bargaining}, an unpublished manuscript"; 06 "which is close to the case in which bargaining over such an object is efficient"; 03 "\citet{benson2023commitment} show"; 06 "\citet{benson2023commitment} find"; 03 "with leasing dominant"; 06 "\citet{harstad2016market} reaches a similar conclusion" | 06 states each comparison once; 03 keeps one sentence per strand | 180 |
| H22 | Gerzhoy, Lanoszka, Pauly, Blankenship | 03 "The coercion literature disagrees about which instrument worked"; 05 "The assurance literature supplies the cost side of the proposition." | 03; delete the 05 paragraph | 160 |
| H23 | Carson (2025) access | 03 "\citet{carson2025allies} argue"; 04 "\citet{carson2025allies} argue that a less committed United States"; 05 "which also raises $s_X$ \citep{carson2025allies}" | 04 | 30 |
| H24 | Jehiel et al. | 03 "\citet{jehiel1996how} show"; 04 "binary instance of the identity-dependent externalities" | 04 | 25 |
| H25 | Silicon shield sign stated before the result | 04 "By \cref{prop:conditionality}(d), $d\bar\kappa/ds_X=g(s_X+s_L)-g(s_X-\bar m_U)$"; Cor 1(e); Prop 4(d); 05 "Part (d) gives the sign of the silicon shield" | Prop 4(d) and 05; 04 one sentence | 60 |
| H26 | Security primitives recalled | 04 sec:security; 05 "Recall from \cref{sec:security} that Washington defends Europe" | 04; 05 keeps kappa_0 and kappa-bar | 55 |
| H27 | Weaponized interdependence third condition | 01 contribution 4; 10 "The result adds a condition to the theory of weaponized interdependence." | 10 (with the fix in F2); 01 one sentence | 50 |
| H28 | Information limitation | 09 "Complete information about conditionality is the strongest assumption."; 10 "The limitation we would worry about most is information." | 09 | 100 |
| H29 | Survey experiment and event dataset | 08 sec:tests; 10 "How conditional the guarantee is can be measured." | 08 | 70 |
| H30 | Nexperia compulsion cost | 07 "In the Nexperia case the Dutch state used the Goods Availability Act"; 08 "The reversal under Chinese pressure is also evidence that compelling a firm is costly" | 08 | 40 |
| H31 | Busan expiry facts | 02 "In September 2026 the two governments agreed to extend"; 08 "\paragraph{The Busan expiry.}" | facts in 02; 08 keeps the implication | 50 |
| H32 | Decree 835 tool list | 02 "Decree 835 of 13 April 2026 creates a Malicious Entity List"; 07 "Decree 835 lets Beijing put those who implement" | 07 (where p_C uses it); 02 one clause | 30 |
| H33 | EU001 and Article 12 licensing | 02 "Under Article 12(2) of the EU dual-use regulation"; 07 "Under Article 12(2) of the dual-use regulation the licence is granted" | 07 | 90 |
| H34 | Scenario Council arithmetic | 07 "The same arithmetic applies to the Council vote in \emph{Europe 2031}."; C table row and "The failed Council vote is the least secure episode." | C (appendix) | 75 |
| H35 | Cost-minimization rival | 05 "A coercer that minimizes cost polices partial defection"; 08 "A cost-minimizing coercer polices each demand" | 08 sec:predictions | 40 |
| H36 | Lake "partly on legitimacy" (also unsourced) | 03 "sustained partly by legitimacy"; 08 "rests on protection already provided and partly on legitimacy" | 03, reworded (F31) | 10 |
| H37 | Double roadmap in the introduction | 01 paragraphs starting "In the game of \cref{sec:model}" and "\Cref{sec:background} describes ASML's position" | first paragraph | 50 |
| H38 | Model opener and closer restating Section 5 | 04 "Part (a) links the bargaining game to the rest of the paper."; 05 opening paragraph | 05 | 60 |
| H39 | Master-game nesting told twice | Cor 1 "Nesting:" line; 04 "The master game nests the protocols one might propose." | Cor 1; text keeps the "only card" corner | 60 |
| H40 | Preventive-war analogy | 03 "which makes it the analogue of preventive war"; 06 "That is the logic of preventive war" | 06 | 40 |
| H41 | Hedge and Q unchanged under flow jurisdiction | 05 "Flow jurisdiction does not depend on slack"; 08 coding "it leaves $Q$ unchanged and needs no concession"; C "which by \cref{prop:counter}(b) is credible whenever" | 05 | 40 |
| H42 | US persons and ASML US subsidiaries | 02 "Because the Export Administration Regulations count"; 07 "ASML's US subsidiaries and the people they employ in the United States are US persons"; 08 "ASML's US entities and staff are US persons" | 02 | 30 |
| H43 | "No public record linking chip controls to US security" | 01 "We found no public record that links"; 08 "we have found no documented case that links"; 08 "Washington uses the security channel, but the record does not show it using that channel on ASML." | 08 sec:record; 01 one clause | 40 |

Total from removing duplicates: about 3,200 words.

## 6. Terminology (resolutions.md section 1)

- "leverage": 08 "Transfers are a narrow measure of leverage" and the subsection title "Coding transfers, threats and leverage" treat delay, scope, retained jurisdiction and tolerated hedges as "broader measures" of leverage. resolutions.md fixes leverage as [P*]^+. Referee 4 flagged this kind of variation last round. (F29)
- "rupture weight": used correctly. Channel names: Cor 1(e), 05 and 07 use the exact five names. The abstract says "rupture risk" for channel (1). (F30)
- "instrument": 03 "Sold tools are a wasting lever ... servicing is therefore a renewable lever". 07 calls servicing "Europe's own hold-up instrument". Use instrument. (F32)
- "exit premium", "slack", "bite" and "conditionality": consistent. "Premium" is used alone after first mention in each section, which is acceptable.
- The definition of the exit premium differs slightly. The abstract says "net of the costs the patron can credibly impose". The intro says "net of the costs the patron can credibly impose on exit and the value the holder places on alignment". eq:Q includes eta. Harmonize the abstract with "net of the credible costs of exit". (part of F1)

## 7. Drafters' open issues (draft_issues.txt): status and fix

Intro, abstract and conclusion drafter
- I1 metrology and 2025/2003 cited to asml2026annual: **open, now fixable**. stcrt2025metrology and eu2025dualuse are in refs.bib. In 01 replace the citation after "took effect on 1 April 2025" and after "Delegated Regulation 2025/2003" with \citep{stcrt2025metrology} and \citep{eu2025dualuse}.
- I2 2019 lapse rests on a press report: **open, now fixable**. kaag2020asml (Kamerstukken 35570 XVII nr. 7, 27 October 2020) is in refs.bib. It documents that the application was pending, not the lobbying, so keep "reported by Reuters" and add kaag2020asml for the licence status. Keep this only in 02 (H3).
- I3 "the only card Europe still holds": **closed by integration_notes** (summary page). Attribute it (F28).
- I4 translation flag: closed. Harmonize the hyphen (F27).
- I5 Zeiss "reportedly": closed.
- I6 Decree 834 reading: closed (hedged in 01 and 08).
- I7 assumed cross-references: closed (02 now names US persons, and sec:coding, sec:tests and tab:implications exist with the assumed content).
- I8 "no public record": closed in substance. Three phrasings exist (H43).
- I9 abstract Japan claim: closed (supported in 01 and tab:cases).
- I10 channel names: Cor 1 is closed. The abstract still says "rupture risk" (F30).
- I11 preview consistency: two small mismatches remain (F14, F15). The thesis sentence is a substantive mismatch (F1).

Background and literature drafter
- B1 Section 1250A has no key: **open**. Either add @misc{usc1928f} (22 U.S.C. 1928f, as added by NDAA FY2024 sec. 1250A) or keep the inline statute and delete the TODO comment. The citation form is acceptable in political science.
- B2 brigade-combat-team cut uncited: **open**. Delete the clause "Later that month the US brigade combat teams based in Europe were cut from four to three," with its TODO. It is not used anywhere else, and it saves words.
- B3 bis2025rescission: **open, now fixable**. Add \citep{bis2025rescission} after the quote in 02 and delete the TODO. In 04 delete the rescission sentence and its TODO and cite back to 02 (H15).
- B4 eu2025dualuse, stcrt2024duv, stcrt2025metrology: **open, now fixable**. In 02, cite stcrt2024duv with asml2024license for the September 2024 step, stcrt2025metrology for the January 2025 step and eu2025dualuse for 2025/2003, and delete the TODO. Do the same in 06 (sec:bind) and 09 ("Delegated Regulation 2025/2003 put the most advanced immersion tools on the EU list (\cref{sec:bind})": add \citep{eu2025dualuse}).
- B5 multiple patterning: **open, now fixable**. Add allen2025deepseek and the integration-note correction. After "``printing its way'' toward self-sufficiency in the AEI authors' phrase \citep{aei2026lithography}" add: "Huawei's Ascend accelerators are made at 7nm this way, without EUV \citep{allen2025deepseek}." Then check that allen2025deepseek supports the 7nm claim (lit_ai strand).
- B6 Dutch national list cited to the annual report: open, acceptable as is.
- B7 EUV and US accelerators: open, acceptable. The wording "the most advanced US AI accelerators" already meets integration note 2.
- B8 2019 licence: see I2.
- B9 Busan extension wording: closed and consistent with 08. Duplicated (H31).
- B10 duplicate bib entries: **open**. aei2026lithography/fedasiuk2026aei, kst32637_717/kst32637717, bis2025affiliates/bis2025affiliatesrule, and possibly pew2026usimage/pew2026european. None of the second keys is cited, so they are harmless in the bibliography, but delete them before submission.
- B11 Lake "partly on legitimacy" unsourced: **open** (F31).
- B12 and B13 cross-references and the control framing: closed and consistent with 06.

Model drafter
- M1 rescission citation: see B3.
- M2 figure legend: closed (psi). The axis label is a new issue (F24).
- M3 varphi vs phi_U: **open** (F20).
- M4 in-kind cap qualification: open, unverified. Keep the parenthesis but mark it "on our reading", or drop the footnote (Section 9 moves it).
- M5 appendix content: the closed forms and the alternating-raise claim are present with psi_Delta, upsilon and mu. The text's description of the claim is wrong (F4).
- M6 cross-references: closed. 02 does not describe "post-2023 hedging disputes" as such, so the clause in 04 "Hedging is the margin of the real disputes since 2023 (\cref{sec:background})" should point to sec:record, where the servicing dispute is read.
- M7 paragraph rather than remark: fine. Duplicated in 05 (H14).
- M8 quote source: closed (F28).
- M9 shaked1994opting unchecked: open, low risk. It is only cited for "on the timing of outside options".
- M10 security foundations: closed.
- M11 necessary condition and the silicon shield: the conclusion's "third condition" sentence now overstates necessity (F2). The fix there covers this.

Slack drafter
- S1 length: see Section 9.
- S2 digital-rules hypothetical: **open**. Delete "A demand on Europe's digital rules would draw on the same budget." (F33)
- S3 Schelling 1960 for "compliance must end the threat": **open, now fixable**. schelling1966arms is in refs.bib. Replace \citep{schelling1960strategy} in 05 "What is new here" with \citep{schelling1966arms}. Keep schelling1960strategy for "a threat that leaves something to chance" (04) and self-binding (03).
- S4 reversible vs sunk classification: closed. Nothing in 08 contradicts it.
- S5 and S6 cross-references and notation: closed. 04 defines kappa-bar. kappa_0 is defined in 05. x_p(A) is an instance of x_j(A).
- S7 relabelling to d_j is unverified: **open**. In 05 replace "so it applies with $d_j$ in place of $\kappa S_k$ to any instrument whose conditional part Washington sets" with "and on our reading the argument carries over, with $d_j$ in place of $\kappa S_k$, to any instrument whose conditional part Washington sets before the bidding stage at a convex cost."
- S8 examples: the counter-threat example is in the A_proofs proof of Prop 3(a)(iii). The burning example (5 vs 4.9) is only in B_numerics as a hand-picked case, not in A_proofs. If the footnote is cut, move it to B_numerics with its numbers.
- S9 Germany via Prop 3(b): **open** (F12).
- S10: closed.

Control drafter
- C1 length: Section 9.
- C2 eu2025dualuse: **open, now fixable** (06 sec:bind: replace \citep{eu2021dualuse, asml2026annual} with \citep{eu2025dualuse, asml2026annual}).
- C3 Goods Availability Act key: optional. kst32637_717 now exists for the suspension.
- C4 simulation count: closed (B reports 20,199 and 1,202).
- C5 inferences flagged: closed.
- C6 cross-section assumptions: **two are wrong** (F10, F11). The Taiwan case is closed.
- C7 overlap: FSR thresholds only in 06 (fine). The preference-share foundation and Vifo are by name only (fine).
- C8 coalition sources: closed.
- C9 Cor 4 only for v_c = 0: closed (06 limits the v_c > iota claim to two periods).
- C10 stale v1 files: **closed** (05_control.tex, 07_revisited.tex and 08_implications.tex are no longer in paper/sections).

Who-decides drafter
- D1 length: Section 9.
- D2 n(s) and labels: closed (A_proofs uses n and (i) to (iii)).
- D3 tab:council enumeration check: closed (B_numerics, rem:council paragraph).
- D4 recital 85: closed.
- D5 and D6: closed (flagged in text).
- D7 parameters flagged: closed. They match the gap memo.
- D8 uncited Nexperia sentence: **open, now fixable**. Add \citep{kst32637_717} after "suspended the order seven weeks later" in 07, or delete the sentence (H30).
- D9 70.46/29.54: closed.
- D10 Decree 835 tools listed twice: **open** (H32).
- D11 Spain: closed.
- D12 28.06 appears once in 07: closed, but the completion claim is wrong (F25) and the paragraph duplicates C (H34).
- D13 Rem 4 Phi(0) only: closed.

Evidence drafter
- E1 TODO kst32637_717: **open, now fixable**. Replace the TODO with \citep{kst32637_717} after "The Enterprise Chamber's measures were separate from the order and outlasted it."
- E2 Nexperia dates: optional. kst32637720 and bis2025affiliates now exist. Given the cut, leave them out.
- E3 Dutch security-grounds sentence: optional. Keys exist. Leave it out for length.
- E4 to E5: closed (hedged).
- E6 tab:cases: **open**. The build log reports "Float too large for page by 213.8pt on input line 111" (08_evidence.tex, the end of tab:cases). See F34.
- E7 to E11: closed.

Implications and scenario drafter
- P1 eu2025dualuse: **open, now fixable** (see B4).
- P2: closed.
- P3 information limitation duplicated: **open** (H28).
- P4 stale v1 files: closed.
- P5 to P8: closed. The C table row and paragraph still restate the Council verdict (H34).

Appendix drafter
- A1 Prop 4(d) wording: **open, essential** (F3).
- A2 Rem 1(c) assumptions: **open** (F8).
- A3 Cor 5 qualification: **open** (F5).
- A4 Prop 2(d) additive costs: **open** (F6).
- A5 Prop 3(b) tie rule: closed. The statement's weak inequality matches the appendix assumption. Only B_numerics tests the strict version, a knife edge.
- A6 Lemma 1 discussion: **open** (F4).
- A7 Prop 6(a) uniform: **open** (F7).
- A8 4.91 and 21/13: closed for the paper. B quotes 4.9 and no main-text sentence uses 4.42 or 10/7.
- A9 local notation in proofs: fine.
- A10 hardcoded bookmark numbers: **will become wrong** after the moves in Section 9 (F35).
- A11: closed.
- A12 float too large: F34.

## 8. Integration notes that create inconsistencies if left out

These are not drafting gaps for the consistency checker to fill, but they touch statements already in the draft:

- **ACI timing and Corollary 5 (09 and 07).** 09 says an ACI response measure "could be such a rule". The verified finding is the opposite: escalation through the ACI is slow and committee-gated, and suspension is fast and in the Commission's hands (Art. 12(5)). The ACI's timing therefore resembles variant (b), under which interruption is never used. (F36)
- **Hungary and the CEE trio** (F26). **Council completions** (F25).
- **US control precedents** (MP Materials, US Steel golden share, Intel) support the Delta_c logic of Prop 5 and belong in sec:cases or sec:controlsetup, which now argues enforceability only from Bloomberg and Nexperia.
- **Silicon shield contested** (Weil, Gottwald and Taube 2025). One sentence in 05 after Prop 4(d) fits the "empirical question" sentence already there.
- **Orders of magnitude** (alpha, r, kappa*S) and **Dutch two-level politics** (the Bamenga motion as support for self-binding without a dual key, which fits Rem 1(d)) are absent. They need roughly 300 to 400 words inside the evidence budget. The cuts in Section 9 make room.
- Integration note 2 (Ascend at 7nm without EUV) belongs in 02 (B5).

## 9. What to cut, merge or move (by section, with budgets)

Raw word counts (wc, including LaTeX and statements) against budgets: intro 1,885/1,600; background 1,704/1,100; literature 1,750/1,400; model 3,883/3,000; slack 4,256/3,000; control 4,625/3,000; who-decides 3,749/2,400; evidence 4,452/3,000; implications 1,456/1,000; conclusion 489/450.

**Moves to the appendix (the editors' plan), with consistency consequences**
1. Prop 6 (breakdown) to the appendix. Keep one informal paragraph in sec:breakdown (about 120 words): "Under complete information an ultimatum is either accepted or never issued. If Washington does not know what a transfer would cost the Dutch government, refusal and the executed cut occur with positive probability. Refusal is likelier when China's punishment of a transfer is credible and large, when Europe's future premium is high, and when the threat is cheap for Washington to carry out. When Washington values control for its own sake, a larger bite can move it from a purchase offer to a threat and raise the chance of breakdown (\cref{prop:breakdown} in \cref{app:proofs})." Saves about 550 words with the 06 discussion paragraphs.
2. Lemma 2 to the appendix, with one sentence in sec:windows: "A cut is spent once executed, and extending a conditional cut into dates at which Europe's premium is positive adds nothing to its bite (\cref{lem:selflimit})." Saves about 250. C cites lem:selflimit(iii), so keep the part labels in the appendix version.
3. Rem 4 details, tab:council, the BEV vote and the consensus-norm paragraph to the appendix (a new subsection of app:proofs or app:numerics). Keep in sec:council the two routes in three sentences plus an informal statement: "Washington defeats a countermeasure most cheaply by buying a blocking minority before the Council's determination, and members with large conditional exposure join it for free. The frontline core cannot block. Thirteen eastern and Nordic members block by number (\cref{rem:council})." Saves about 650.
4. Numbering: the theorem counters are global, so a moved Prop 6 keeps its number but appears after Prop 7. Either give appendix-only results their own counter (for example \newtheorem{propositionA}{Proposition}[section], printed as Proposition A.1), or keep them in place with numbers and move only the proofs. Either way, update the hardcoded PDF bookmarks in A_proofs (\texorpdfstring{\Cref{prop:breakdown}}{Proposition 6} and so on), the intro sentence "\Cref{cor:windows,rem:bind,prop:breakdown} cover the timing of demands, self-binding and refusal", and the C table rows that cite prop:breakdown and rem:council (F35).
5. Other candidates: the alternative-exit-timing footnote (04) down to one sentence; the in-kind footnote (04) to sec:coding or the appendix; the burning-instrument footnote (05) to B_numerics; the numerical counter-threat example (05) to A_proofs, where it already is; the special case after Prop 5 (06) to the appendix, where it already is; tab:cases to an appendix, which also fixes the float overflow.

**Section by section** (duplicate numbers refer to Section 5)
- Intro (-300): compress the control-sequence paragraph to two sentences (H2, H3); trim the MATCH, Japan and Korea paragraph (H4); delete the second roadmap (H37); keep one CMS quote (H5).
- Background (-600): shorten the Supplement No. 4 mechanics, keeping the fact, the quote and "BIS can amend the list by rule" (H1); move the EU001 and Article 12 mechanics to sec:gatekeeper and sec:council (H33); keep the Decree 835 list to one clause (H32); delete the uncited brigade clause (B2); trim the Nuctech sentence.
- Literature (-350): cut the duplicate strands now argued in 06 and 07 (H20, H21, H40); keep the CMS contrast here as the home (H6), and the bidding credits (H7).
- Model (-880): one-sentence credit after Lemma 1 (H7); cut the restatement of Prop 4(d) (H25); keep the AI rescission to an inference plus a cref (H15); trim the Chinese-punishment paragraph (H14); shorten the exit-timing footnote; trim the nesting and "Part (a) links" paragraphs (H38, H39).
- Slack (-1,250): cut "What is new here" to the assurance point (H6), about 230; move the burning footnote, about 70; delete digital rules (F33); cut the duplicate Chinese-punishment lead (H14); move the numerical counter-threat example to the appendix, keeping one sentence, about 120; cut the NSS re-quote (H16); shorten the drawdown paragraph (H18), about 110; delete the assurance-literature paragraph (H22), about 160; trim the recalled primitives (H26).
- Control (-1,600): moves 1 and 2 above, about 800; cut the duplicated literature comparisons (H21), about 180; trim the sec:bind application paragraph (H1, H2, H17), about 130; trim the FSR detail and the special case, about 120; trim the windows comparison with Powell, about 80.
- Who decides (-1,350): move 3 above, about 650; move the scenario arithmetic to C (H34); trim Bank Melli, Decree 835 and tiering, about 190; trim the hold-up calibration paragraph to central values (keep h about 0.85 and the two t-bar values), about 220; add one sentence on ACI timing (F36), about +50.
- Evidence (-1,450, plus room for the integration items): move tab:cases to an appendix, or cut it to the contemporary holders (F34); delete the security-signals paragraph (H18); trim the Nexperia narrative to the dated facts and the two readings, about 170; trim the strains paragraphs, about 180; trim sec:tests and the Busan expiry (H29, H31).
- Implications (-450): shorten the scope cases to cross-references (H9 to H12); trim the CRMA and Blocking Statute detail; rewrite the interruption paragraph (F36).
- Conclusion (-40, net): delete the information paragraph (H28); shorten the measurement paragraph (H29); fix the thesis sentence (F1, F2).
