# Council practice and member states' revealed positions on coercive measures. Fact-checked gap memo (as of 29 October 2026)

Strand: gap_council_revealed_positions. Checks the memo that tests the ACI pivot analysis and the claim in Section 7 that the scenario's failed 2029 ACI vote "is not an equilibrium," using Council practice (consensus norms, Commission gatekeeping) and member states' revealed positions on coercive measures against the US and China. Computations: `code/checks/council_revealed_blocking.py`.

## How this was checked, and its limits

The shared WebSearch budget for this turn was already used up when this check began; the WebSearch calls returned a refusal. Nothing below rests on a search-engine result. Every item was checked by retrieving the document itself:

- Crossref records by DOI for all 28 scholarly items, plus OpenAlex records by DOI for the nine items whose abstracts Crossref does not carry. Zhang's chapter was read in the ANU Press PDF (Table 6.2, pp. 134-135).
- EUR-Lex texts via Cellar content negotiation: Regulation (EU) 2023/2675 (ACI), Regulation (EU) No 182/2011, Statement C/2023/1341, Council Decisions 2009/937/EU, (EU) 2016/1316 and (EU, Euratom) 2025/2427, and Commission Implementing Regulations 2024/2754, 2025/786, 2025/1446, 2025/1564, 2025/1727, 2026/295 and 2026/1893. Two Cellar SPARQL queries were re-run (acts on export control or economic security since 24 January 2024; any act referring to Regulation 2023/2675 or "economic coercion" since 2024).
- The Commission comitology register API: meeting lists for the ACI committee (C127800) and the Trade Barriers Committee (C22700), the document search for five meetings, the opinion records for the EV and July 2025 votes, the two public formal voting results (V109145, V109281), the summary records of 28 January and 17 July 2026, the ACI committee's rules of procedure, and the register's own label file (to read "label.no-vote").
- Press-corner API for STATEMENT/24/5041 and STATEMENT/25/1025; the Eurostat EUROPOP2023 API; Kamerstukken 32637-717 and 32637-720 on officielebekendmakingen.nl.
- News pages fetched directly: Al Jazeera (28 July 2025), AP via ABC7 (19 January 2026), E24 (18 January 2026), Times of Israel/agencies (18 January 2026), Euronews Hungarian (19 January 2026), Aftenposten (20 January 2026), stm.dk (6 January 2026), Bits&Chips (24 June 2026), NL Times (14 April 2026), electrive (10 November 2025), and Wikipedia for two dates of office.
- The memo's script was rerun and reproduced every number it reports. An independent eight-million-draw Monte Carlo (numpy) checked the Shapley-Shubik indices, and a supplementary script computed minimal blocking sets under supermajority norms.

Not reached: Politico Europe (fetch refused again), Reuters, consilium.europa.eu (so the Council's own voting-results database and any Council conclusions), the undisclosed per-state voting sheets, and the full text of Golub (1999), which is closed access.

## Verdict in brief

The memo's arithmetic is exact and its main recommendation (formal QMV as the primitive, plus a Commission gatekeeping move) survives. Four of its supporting claims need correcting, and two corrections cut in opposite directions.

1. **The arithmetic reproduces.** Every share, pivot list and power index in the memo matches the rerun. An independent Monte Carlo gives Shapley-Shubik DE 17.53 (s.e. 0.01), FR 13.48, IT 11.55, NL 3.66, confirming the script and refuting the eu_inst memo's DE 17.74, FR 13.64 and IT 11.60. The eu_inst Banzhaf figures were already right.
2. **"Every recorded vote on the US side is dovish" is false.** Member states gave positive committee opinions to two US-facing countermeasure packages, on 9 April 2025 (Commission: "EU Member States have voted in favour") and on 24 July 2025 (Regulation 2025/1564, "in accordance with the opinion of the Trade Barriers Committee"). Neither package ever applied. Each suspension followed a US move: Regulation 2025/778 and its suspension 2025/786 were adopted on the same day, 14 April 2025, after the US 90-day tariff pause of 9 April; 2025/1564 was due to apply from 7 August 2025 and was suspended on 5 August after the Turnberry agreement of 27 July; the January 2026 renewal came a week after Washington withdrew the Greenland tariff threat on 21 January. The record is "authorise, then suspend on a US concession." That is conditional reciprocity with a revealed reluctance to let measures bite, not a dovish majority. The July 2026 suspension (2026/1893) has no end date.
3. **Formally, opponents are even weaker at the response-measure stage than the memo says.** Article 18(2) of the ACI bars adoption after a "no opinion" in the committee, but it routes the act to the appeal committee, and under Article 6(3) of Regulation 182/2011 the Commission "may adopt" if the appeal committee gives no opinion. A formal block at that stage needs a qualified majority against. What binds is the Commission's self-commitment, written into recital 85 of the ACI itself and repeated in Statement C/2023/1341, to avoid "going against any predominant position amongst Member States." This strengthens the memo's central point: gatekeeping, not the formal threshold, is the binding constraint.
4. **The Presidency argument applies only to the Council determination.** In the scenario the item that fails is the measure restricting ASML exports and servicing to US fabs, that is, an Article 8 response measure. Those are voted in the ACI committee, which the Commission chairs. The Dutch Presidency (July to December 2029) has no formal role there. It matters only at the Article 5 determination, where Article 5(6) obliges the Council to act within 8 weeks unless it notifies the Commission of a delay.
5. **Golub (1999) is mischaracterised.** Its abstract challenges the received view that restoring majority voting "unblocked and expedited" EC legislation, finds that institutional reforms "encumbered rather than eased" the legislative process, and finds that institutional effects are "mediated by the underlying distribution of member state preferences." It does not establish that decisions are made "in the shadow of the vote" (the title is a question). Häge (2013) is the right authority for keeping the formal threshold as the primitive.
6. **Smaller corrections.**
   - Mattila (2004) and Mattila and Lane (2001) find that large states are *more* likely to vote "no." The memo's phrase "large states vote no more often than small ones" reads as the opposite. Mattila (2004) finds that presidencies vote against the majority "less than otherwise," not "rarely."
   - Germany's a priori power is 4.8 times the Netherlands' on Shapley-Shubik but 3.2 times on normalised Banzhaf, so "about five times" holds for one index only.
   - Bulgaria completes a blocking minority with the scenario seven plus HU, SK and CZ in 2029 as well as in 2026.
   - The supermajority examples are not minimal. Under a 75 per cent norm, Italy, Poland and the Netherlands (25.50 per cent) suffice. Under 85 per cent, Italy and the Netherlands (17.21 per cent) suffice. Above 86.81 per cent, Italy alone blocks.
   - "All 27 states favoured every rebalancing suspension" overstates the record. There are two public formal votes, both 27 to 0 (July and August 2025). The April 2025 suspension has no published result. The January and July 2026 renewals record a favourable opinion and "Members expressed support," with no per-state breakdown.
   - The HU-SK-CZ "bloc" is uneven. Hungary's foreign minister said Hungary "will not vote for any EU statement" on Greenland. Babiš wrote "we will support dialogue, not statements." Fico's statement after Mar-a-Lago simply omitted Greenland. Statements of this kind need unanimity, so they are weak proxies for votes on a QMV trade measure.
   - The claim that Tusk "said Poland would not deploy troops" is not supported by the cited source.
   - The ACI committee's rules let any member ask for its position to be recorded in the minutes (Art. 10(1)), so individual positions can surface even though the summary record omits them.
7. **Additions.**
   - The ACI allows urgent, immediately applicable acts only to suspend or amend response measures (Art. 12(5)), never to adopt them. De-escalation is fast and in the Commission's hands; escalation is slow and committee-gated.
   - The Dutch government's 19 November 2025 letter says the Nexperia suspension followed diplomatic talks "in coordination with our European partners and the European Commission."
   - On 22 January 2026 the Tweede Kamer adopted a motion (103 to 46) to keep the ACI in reserve over Greenland, against the caretaker cabinet's advice. This is from the dutch-politics strand and was not re-fetched here.
   - The Commission and High Representative issued a Joint Communication, "Strengthening EU economic security" (JOIN(2025) 977, 3 December 2025). Cellar shows no Council act responding to it or to the 2024 White Paper on Export Controls.

## Corrected synthesis

The referee's objection is half right, and the memo's diagnosis is the right one. Under formal QMV and 2026 Council weights, the states the scenario names (Netherlands, Ireland, Poland, Lithuania, Latvia and Estonia opposed; Italy abstaining) hold 28.06 per cent of the population and cannot block. The only single states that complete a blocking minority are Germany, France and Spain, in every year from 2026 to 2031 under EUROPOP2023 weights. Without one of them, at least three more states are needed; no two-state completion exists, even with Romania. So the formal arithmetic is not in doubt. The question is whether formal QMV is the rule that binds, and the evidence says it is not. What binds is whether the Commission tables a measure at all.

**Literature.** Heisenberg (2005) reports that 81 per cent of Council decisions are taken by consensus and argues that this informal norm undercuts rational-institutionalist models built on formal rules. Hayes-Renshaw, van Aken and Wallace (2006) find that explicit contested voting at ministerial level is rare (1994 to 2004). In nearly half the roll calls the dissent comes from a lone member state, and Germany votes "no" or abstains more often than any other state. Where QMV could be used, voting "occurs implicitly rather than explicitly, operates mostly at the level of officials," and is not recorded systematically. Novak (2013) explains why: a formal vote would disclose who opposed, and ministers do not register opposition because they expect to be blamed at home. Declared positions therefore understate opposition. Mattila and Lane (2001) and Mattila (2004) find that large states are more likely than small ones to vote against the majority, and Mattila (2004) finds that governments holding the Presidency vote against the majority less than they otherwise would.

Häge (2013) reconciles the consensus finding with formal rules. In his agent-based model consensus emerges as an unintended by-product of governments forming blocking coalitions, and raising the voting threshold enlarges winning coalitions while adding members does not. This is the authority for keeping the formal threshold as the primitive. Golub (1999) should not be cited for that point. His abstract argues that the restoration of majority voting did not unblock EC decision-making, that reforms encumbered legislation, and that institutional effects depend on the distribution of preferences.

Recent work confirms both halves. Novak, Rozenberg and Bendjaballah (2021) find that consensus remained the norm through 2019, with only a moderate shift toward majoritarian decision-making. Hagemann, Hobolt and Wratil (2017) show that the opposition that does get recorded responds to domestic Euroscepticism, especially when integration is salient. Pircher and Farjam (2021) trace oppositional voting from 2010 to 2019 to party Euroscepticism and left-right positions. Hobolt and Wratil (2020) find more contestation in public ECOFIN deliberations (2010 to 2015) than in votes.

On agenda control, Boranbay-Akan, König and Osnabrügge (2017) show that co-decision proposals (1993 to 2009) are more often withdrawn when uncertainty about the pivotal actor rises. Van Gruisen and Crombez (2021) derive, in a spatial model, that the Commission keeps legislative power by timing proposals to Presidencies close to its own position. Häge (2017) shows empirically that the Presidency shapes how much working-party time each policy area gets. Meunier (2000) supplies the external implication: restrictive internal rules weaken the Union when it seeks to change a partner's behaviour, and a counter-coercion measure is that kind of move. No political-science study of Council or committee voting on the ACI or on export controls was found. Zhang (2025) compiles the EV vote, and Evenett and Vermulst (2005) is the closest systematic work on member-state votes in trade defence. They find frequent disagreement over anti-dumping duties in the late 1990s, which "may well have been partly responsible" for the later fall in investigations.

**The ACI's procedure, read from the text.** There are four gates.

1. *Examination.* The Commission "may, on its own initiative or upon a duly substantiated request" examine a third-country measure (Art. 4(1)); the examination "shall normally not exceed 4 months" (Art. 4(2)).
2. *Determination.* If it finds coercion, the Commission "shall submit a proposal" for a Council implementing act (Art. 5(1)). The Council acts by qualified majority (Art. 5(5)) "within 8 weeks." It may go beyond 8 weeks if it informs the Commission of the delay and its reasons, and the total "shall normally not exceed 10 weeks" (Art. 5(6)).
3. *Response measures.* These are Commission implementing acts under the examination procedure (Art. 18(2)). A positive opinion needs a qualified majority in favour. If the committee delivers no opinion, the Commission "shall not adopt" and the appeal route of Art. 5(4) third subparagraph of Regulation 182/2011 applies.
4. *Appeal.* In the appeal committee, "where no opinion is delivered, the Commission may adopt" (Reg. 182/2011, Art. 6(3)). Only a qualified majority against stops it formally.

The binding constraints are political commitments. Recital 85 of the ACI says the Commission should give special attention to "solutions which command the widest possible support" and, "at all stages of the procedure, including in the appeal committee," avoid "going against any predominant position amongst Member States." Statement C/2023/1341 repeats this. After a no-opinion the Commission "will prioritise return to the committee with an amended draft act," and it "will act in such a way as to avoid going against any predominant position within the appeal committee." The ACI committee's rules let the chair record a positive opinion by consensus unless a member objects (Art. 4(3)) and keep individual positions out of the summary record (Art. 10(2)). Members may still ask for their position to be recorded in the minutes (Art. 10(1)), and the committee's discussions are confidential (Art. 13(2)). Urgent, immediately applicable acts are available only to suspend or amend response measures (Art. 12(5)). The committee met once, on 7 February 2024, to adopt its rules; the register holds no later meeting, and Cellar holds no act under the Regulation apart from a 2024 corrigendum.

**Revealed positions.**

*China-facing default-adopt.* On 4 October 2024 the Trade Defence Instruments Committee delivered "No Opinion" on definitive duties on Chinese battery EVs (the register's label "label.no-vote" renders as "No Opinion"). Zhang's compilation has 10 states for, 5 against (Germany, Hungary, Malta, Slovakia, Slovenia) and 12 abstentions. Re-weighted with 2026 figures, the for-votes hold 45.98 per cent. Recital 1432 of Regulation 2024/2754 records the no-opinion, and the Commission adopted anyway, as Article 5(4) of Regulation 182/2011 allows for trade defence unless a simple majority opposes. The Commission called this "the necessary support." Under the ACI's positive-QMV rules the same distribution would fall 19.02 points and five states short.

*US-facing: arm, then suspend.* Member states approved US-facing countermeasures twice:

- 9 April 2025: "EU Member States have voted in favour" (STATEMENT/25/1025).
- 24 July 2025: a positive opinion on the consolidated package, which became Regulation 2025/1564.

Neither package applied. Each was suspended under the urgency procedure of Article 8 of Regulation 182/2011 and only then sent to the committee:

- 2025/786, adopted on 14 April 2025, the same day as 2025/778, after the US 90-day pause of 9 April.
- 2025/1446, adopted on 14 July 2025.
- 2025/1727, adopted on 5 August 2025, after the Turnberry agreement and before the duties' 7 August start date.

The only two per-state results in the public register are for the July and August 2025 suspensions, both 27 to 0 by written procedure. The renewals of 28 January 2026 (one week after the Greenland threat was withdrawn) and 17 July 2026 record that "Members expressed support," and all 27 states attended both meetings. The July 2026 renewal (2026/1893) has no end date. It followed the adoption on 25 June 2026 of Regulations 2026/1455 and 2026/1461, which implement the EU's own tariff cuts under the Joint Statement.

Two readings fit this record. A dovish reading says member states never let a measure bite. A conditional-reciprocity reading says they armed measures by QMV and holstered them each time Washington moved. The record cannot separate the two, because execution was never tested against a US refusal.

*Greenland.* Seven leaders (France, Germany, Italy, Poland, Spain, the UK and Denmark) signed the 6 January 2026 statement that "Greenland belongs to its people." Eight targeted countries (Denmark, Finland, France, Germany, the Netherlands and Sweden, plus Norway and the UK) warned on 18 January of "a dangerous downward spiral." France, through sources close to Macron (Bloomberg) and his staff (AFP), was reported ready to ask for ACI activation. No other government is named as backing activation in the sources reached. Lange (the trade committee chair in the European Parliament), Renew's Hayer and the German engineering association echoed the call, and "some EU diplomats said now was not the time to escalate." Germany's reported request that the Commission explore the ACI rests on Politico via Wikipedia and remains unverified. Hungary's foreign minister said Hungary would not vote for any EU statement ("I don't think it is an EU matter"). Babiš wrote "we will support dialogue, not statements," and Fico's statement after meeting Trump omitted Greenland. Meloni called the tariffs "a mistake" without discussing retaliation. A Commission spokesperson said the EU's priority was "contact, not escalation."

*Turnberry.* Reactions to the July 2025 deal ranged from Bayrou's "submission" and Orbán's "This is not an agreement" to welcomes from Merz, Orpo and Bolojan. Meloni called the deal positive, with a caveat about the details, and said escalation would have had "potentially devastating consequences." Harris gave a qualified welcome, Sánchez supported it "without any enthusiasm," Dousa called it "the least bad alternative," and Løkke Rasmussen said "it is not our choice." No government called for retaliation or the ACI.

*Nexperia.* The Dutch record says "European partners repeatedly expressed their understanding and support." Germany and the UK were informed on 30 September 2025, the day of the order. The 19 November letter suspending the order says that talks with China "in coordination with our European partners and the European Commission" made clear that suspension would help. It also cites China's licensing of exports and the US-China announcement of 1 November. MOFCOM had tied its easing to a demand that the EU urge the Netherlands to reverse course. There is no sign of a Council fight, and the climb-down was coordinated with partners.

*MATCH Act.* The only member-state positions found are Dutch: Jetten raised export controls with Trump on 13 April 2026, and Sjoerdsma said on 24 June 2026, "If cooperation becomes cooperation by force, that's undesirable." Without search, the absence of other governments' positions cannot be established.

**Pivots.** Adding Hungary, Slovakia and Czechia to the scenario seven gives 33.79 per cent (2026) and 33.45 per cent (2031). One more state then suffices. That can be any of twelve states in 2026: DE, FR, ES, RO, BE, PT, SE, GR, AT, BG, DK, FI. In 2029 it is ten: those minus DK and FI. In 2030 and 2031 it is nine: minus BG as well. Alternatively any three more states complete the 13-member count route. Without Hungary (31.68 per cent), only DE, FR, ES or RO completes it. Hungary changed government on 9 May 2026, so the CEE trio is not a fixed bloc. On a priori power, Germany is the largest voter (Shapley-Shubik 17.54 per cent, normalised Banzhaf 12.03 per cent), 4.8 and 3.2 times the Netherlands' figures (3.66 and 3.80).

**The 2029 episode.** A measure that is tabled and then visibly fails is the least plausible version of the scenario. It is less plausible under the formal rules than the memo says, because at the response-measure stage only a qualified majority against can formally stop the Commission after appeal. It is more plausible under the Commission's own commitment not to go against a "predominant position," whose threshold is undefined. On the equilibrium path we would expect one of three outcomes: no examination opened; an examination that ends without a determination proposal; or a response package from which the ASML element has been dropped. If the scenario's failure is placed at the Council determination instead, the Presidency matters. The Netherlands holds it from July to December 2029 and Slovakia from January to June 2030. The Commission proposal would be public, so a stalled determination would be visible even if per-state votes were not published.

## Verified facts table

Verdicts: V = verified as stated; C = verified after correction (corrected wording shown); U = unverifiable with the sources reached; F = false.

| # | Claim (corrected where needed) | Verdict | Source (date) | Note |
|---|---|---|---|---|
| 1 | EV definitive CVD vote, 4 Oct 2024: for BG, DK, EE, FR, IE, IT, LV, LT, NL, PL (10); against DE, HU, MT, SK, SI (5); abstain AT, BE, HR, CY, CZ, FI, GR, LU, PT, RO, ES, SE (12). Zhang: 45.99 / 22.65 / 31.36% of population; 2026 weights 45.98 / 22.38 / 31.63%. | V | https://press-files.anu.edu.au/downloads/press/n14544/pdf/ch06.pdf (Table 6.2, "Source: Author's compilation"; book 25 Nov 2025) | Secondary compilation; re-weighting reproduced. |
| 2 | Register: Trade Defence Instruments Committee meeting CMTD(2024)1752 (4 Oct 2024); opinion code "label.no-vote", which the register's label file renders "No Opinion"; voting sheet 102870 and summary record 102871 listed. | V | https://ec.europa.eu/transparency/comitology-register/core/api/front/documents/CMTD(2024)1752/71405/findVotingAssociated (retrieved 29 Oct 2026) | Disclosure status of 102870/102871 not re-tested. |
| 3 | Regulation 2024/2754 (29 Oct 2024), recital 1432: "The Committee established by Article 15(1) of Regulation (EU) 2016/1036 did not deliver an opinion on the measures provided for in this Regulation." | V | http://data.europa.eu/eli/reg_impl/2024/2754/oj (29 Oct 2024) | |
| 4 | STATEMENT/24/5041: the proposal "has obtained the necessary support from EU Member States for the adoption of tariffs." | V | https://ec.europa.eu/commission/presscorner/detail/en/statement_24_5041 (4 Oct 2024) | |
| 5 | Reg. 182/2011 Art. 5(4)-(5): after a no-opinion the Commission may adopt unless (among others) a simple majority opposes; for definitive AD/CVD measures with a simple majority opposed, the act goes to the appeal committee. | V (added) | http://data.europa.eu/eli/reg/2011/182/oj (OJ L 55, 28.2.2011) | Explains why 5 "against" did not stop the EV duties. |
| 6 | 9 Apr 2025 (meeting CMTD(2025)681): STATEMENT/25/1025, "EU Member States have voted in favour" of countermeasures; register lists voting result 107095 and summary record 107061. | V | https://ec.europa.eu/commission/presscorner/detail/en/statement_25_1025 (9 Apr 2025) | Per-state breakdown not public; Hungary "against" press reports unverified. |
| 7 | 24 Jul 2025 (CMTD(2025)1395): positive opinion on the package that became Reg. 2025/1564; voting sheet 109049. | V | https://ec.europa.eu/transparency/comitology-register/core/api/front/documents/CMTD(2025)1395/79595/findVotingAssociated | Reg. 2025/1564 recital 34 confirms "in accordance with the opinion." |
| 8 | Reg. 2025/1564 duties were to apply from 7 Aug 2025; Reg. 2025/1727 (5 Aug 2025) suspended them, citing the 27 Jul political agreement. | V (added) | http://data.europa.eu/eli/reg_impl/2025/1564/oj ; http://data.europa.eu/eli/reg_impl/2025/1727/oj | Neither 2025 package ever applied. |
| 9 | Reg. 2025/778 and suspension Reg. 2025/786 both adopted 14 Apr 2025; recital 9 cites the US 90-day reduction of 9 Apr 2025 as the reason. | V (added) | http://data.europa.eu/eli/reg_impl/2025/786/oj (14 Apr 2025) | |
| 10 | V109145/01: written consultation, urgency procedure, opinion 18 Jul 2025: 27 for, none against, no abstentions. Draft act D109124/01 (the 2025/1446 suspension, per the register meeting title). | V | https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/484242/109145/1/attachment (Ares(2025)6207499, 30 Jul 2025) | |
| 11 | V109281/01: written consultation, urgency, opinion 12 Aug 2025: 27 for, none against, no abstentions (Reg. 2025/1727). | V | https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/485429/109281/1/attachment (Ares(2025)6617481, 14 Aug 2025) | |
| 12 | TBR Committee, 28 Jan 2026: "Members expressed support"; favourable opinion; all 27 states listed as participating. Became Reg. 2026/295 (4 Feb 2026), applying 7 Feb to 6 Aug 2026. | V | https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/517999/113452/1/attachment (28 Jan 2026) | Voting sheet 113482 listed, not read. |
| 13 | US withdrew the Greenland tariff threat on 21 Jan 2026 (Davos, "framework of a future deal"), a week before the 28 Jan meeting. | V (cross-strand) | https://www.ttnews.com/articles/trump-greenland-drops-tariffs (21 Jan 2026), via notes/review/security.md | Not re-fetched here. |
| 14 | TBR Committee, 17 Jul 2026: "Members expressed support"; favourable opinion; 27 participants. Became Reg. 2026/1893 (30 Jul 2026), applying from 7 Aug 2026 with no end date, after Regs 2026/1455 and 2026/1461 (25 Jun 2026) implemented EU tariff cuts. | C | https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/541599/117365/1/attachment (Ares(2026)7539075); http://data.europa.eu/eli/reg_impl/2026/1893/oj | Added: open-ended suspension. |
| 15 | 2025/786, 2025/1446 and 2025/1727 were adopted "in view of imperative grounds of urgency" under Art. 8 of Reg. 182/2011 and submitted to the committee within 14 days; 2026/295 and 2026/1893 state they are "in accordance with the opinion of the Trade Barriers Committee." | V | EUR-Lex texts (14 Apr 2025 to 30 Jul 2026) | |
| 16 | "All 27 states favoured every rebalancing suspension in 2025-26." Corrected: two public formal votes, both 27 to 0 (Jul, Aug 2025); April 2025 suspension (written procedure CMTD(2025)830) has no voting result in the register; 2026 renewals are favourable opinions with "Members expressed support." No recorded dissent. | C | Register document search, CMTD(2025)830 (one document, the act) | |
| 17 | "Every recorded vote on the US side is dovish." Member states twice gave positive opinions on countermeasures (9 Apr and 24 Jul 2025); both packages were suspended before applying, each after a US move. | F | Rows 6 to 12 | Replace with "authorise, then suspend." |
| 18 | ACI committee (C127800): two register records, both titled "First meeting," dated 7 Feb 2024; no later meeting through 29 Oct 2026. | V | https://ec.europa.eu/transparency/comitology-register/core/api/front/committees/C127800/meetings?lang=en&page=0&size=50 | Duplicate record, one meeting. |
| 19 | Cellar holds no act under Reg. 2023/2675 since 2024 except the corrigendum 32023R2675R(01) (10 Jul 2024). | V (added) | https://publications.europa.eu/webapi/rdf/sparql (query run 29 Oct 2026) | |
| 20 | ACI committee RoP: Art. 4(3) consensus without formal vote unless a member objects; Art. 4(5) widest possible support; Art. 10(2) summary record "shall not mention the individual position of the members"; Art. 13(2) discussions confidential. Added: Art. 10(1) members "shall have the right to ask for their position to be recorded in the minutes." | C | https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/380298/095426/1/attachment (7 Feb 2024; Ares(2024)1439526) | Art. 10(1) omitted by memo. |
| 21 | C/2023/1341: widest possible support; after a no-opinion "will prioritise return to the committee with an amended draft act"; in the appeal committee "will act in such a way as to avoid going against any predominant position ... against the appropriateness of the draft implementing act"; a united response "will support the key features of the instrument, namely, deterrence and effectiveness." | V | http://data.europa.eu/eli/C/2023/1341/oj (OJ C, 7 Dec 2023) | |
| 22 | ACI recital 85 itself contains the commitment to avoid "going against any predominant position amongst Member States" at "all stages of the procedure, including in the appeal committee." | V (added) | http://data.europa.eu/eli/reg/2023/2675/oj | Stronger basis than the statement alone. |
| 23 | ACI: Art. 4(1) "may, on its own initiative or upon a duly substantiated request"; Art. 4(2) examination "shall normally not exceed 4 months"; Art. 5(5) Council acts by QMV; Art. 5(6) "within 8 weeks," extendable on notice, total "shall normally not exceed 10 weeks"; Art. 18(2) no-opinion bars adoption and Art. 5(4) third subpara of 182/2011 applies; Art. 19(3) review no later than 3 years after the first Art. 5 act or by 27 Dec 2028, whichever is earlier. | V | http://data.europa.eu/eli/reg/2023/2675/oj (22 Nov 2023; OJ 7 Dec 2023) | |
| 24 | Reg. 182/2011 Art. 6(3): if the appeal committee delivers no opinion, "the Commission may adopt the draft implementing act." A formal block of an ACI response measure after appeal therefore needs a QMV against. | V (added) | http://data.europa.eu/eli/reg/2011/182/oj | |
| 25 | ACI Art. 12(5): urgent, immediately applicable acts only "to suspend or amend Union response measures." | V (added) | http://data.europa.eu/eli/reg/2023/2675/oj | |
| 26 | Council RoP (2009 text): Art. 11(1) Council votes on the President's initiative; the President must open a vote at a member's or the Commission's initiative if a majority so decides. Art. 9(1) vote results public for non-legislative acts in Art. 8(1), which excludes "acts concerning interinstitutional or international relations"; Art. 9(2)(b) otherwise by Council or Coreper decision at a member's request. | V | http://data.europa.eu/eli/dec/2009/937/oj (OJ L 325, 11.12.2009) | Later amendments to Arts 9 and 11 not checked; classification of an ACI determination is our reading. |
| 27 | Presidencies: IT Jan-Jun 2028, LV Jul-Dec 2028, LU Jan-Jun 2029, NL Jul-Dec 2029, SK Jan-Jun 2030, MT Jul-Dec 2030. | V | http://data.europa.eu/eli/dec/2016/1316/oj (Annex I; OJ L 208, 2.8.2016, p. 42) | |
| 28 | Joint statement on Greenland, 6 Jan 2026, signed by Macron, Merz, Meloni, Tusk, Sánchez, Starmer, Frederiksen: "Greenland belongs to its people." | V | https://stm.dk/statsministeriet/publikationer/faellesudtalelse-om-groenland/ (6 Jan 2026) | |
| 29 | 18 Jan 2026 statement by DK, NO, SE, FR, DE, UK, NL, FI: tariff threats "undermine transatlantic relations and risk a dangerous downward spiral." Meloni called the tariffs "a mistake." AP reports no government backing retaliation. | V | https://abc7news.com/post/europe-warns-dangerous-downward-spiral-trump-threatens-tariffs-greenland/18427942/ (AP, 19 Jan 2026) | |
| 30 | France: Bloomberg (source close to Macron) and AFP (staff member) reported Macron ready to ask for ACI activation; Lange called for immediate activation; Hayer and the German engineering association echoed; "some EU diplomats said now was not the time to escalate." | V | https://e24.no/internasjonal-oekonomi/i/k0RzJQ/eu-medlemmer-vurderer-aa-aktivere-bazookaen (18 Jan 2026); https://www.timesofisrael.com/trumps-greenland-tariffs-spark-calls-for-unprecedented-eu-bazooka-countermeasure/ (18 Jan 2026) | |
| 31 | Germany said it would ask the Commission to explore the ACI (Politico, 20 Jan 2026, via Wikipedia). | U | https://www.politico.eu/article/eu-bazooka-trade-us-greenland-france-threat-nato/ | Fetch refused. |
| 32 | Hungary: FM Szijjártó, "Hungary will not vote for any EU statement" on Greenland; "I don't think it is an EU matter." Slovakia: Fico's post-Mar-a-Lago statement did not mention Greenland. Czechia: Babiš, "we will support dialogue, not statements." Euronews: the agreement of Hungary, Slovakia and Czechia "will also be needed." | C | https://hu.euronews.com/my-europe/2026/01/19/orban-fico-babis-europa-trump-parti-vezetoi-csendben-vannak-a-gronlandi-valsaggal-kapcsola (19 Jan 2026); https://www.aftenposten.no/verden/i/j0B2En/ungarn-vil-neppe-stoette-felles-eu-uttalelse-om-groenland (20 Jan 2026) | Slovakia was silent rather than declining; statements need unanimity, unlike a QMV trade act. |
| 33 | Commission spokesperson: "The EU's priority is contact, not escalation" (19 Jan 2026), ahead of a crisis meeting "Thursday this week." | V | Aftenposten (20 Jan 2026) | Article does not name 22 Jan or call it a leaders' meeting. |
| 34 | Turnberry reactions: Bayrou "submission"; Orbán "This is not an agreement"; Merz averted a conflict; Meloni "positive" if details hold, escalation "potentially devastating"; Orpo and Bolojan welcomed; Harris qualified; Sánchez "without any enthusiasm"; Dousa "least bad alternative"; Løkke Rasmussen "not our choice." No call for retaliation or the ACI. | V | https://www.aljazeera.com/news/2025/7/28/how-european-leaders-are-reacting-to-eu-us-trade-deal (28 Jul 2025) | |
| 35 | Nexperia: order 30 Sep 2025; UK and Germany informed the same day; "Europese partners hebben herhaaldelijk hun begrip en steun uitgesproken"; senior civil-service delegation in Beijing 18-19 Nov; 19 Nov letter cites "brede steun" and says talks with China "in coördinatie met onze Europese partners en de Europese Commissie" made clear that suspension would help. | C | https://zoek.officielebekendmakingen.nl/kst-32637-720.html (2 Dec 2025); https://zoek.officielebekendmakingen.nl/kst-32637-717.html (19 Nov 2025) | Added coordination sentence. |
| 36 | MOFCOM linked easing of the Nexperia export ban to a demand that the EU urge the Netherlands to reverse its actions. | V | https://www.electrive.com/2025/11/10/china-eases-export-ban-on-nexperia-chips (10 Nov 2025) | |
| 37 | MATCH Act: Sjoerdsma, "If cooperation becomes cooperation by force, that's undesirable from our point of view" (24 Jun 2026); Jetten raised export controls with Trump at the 13 Apr 2026 dinner. No other member state's position in either article. | V | https://bits-chips.com/article/dutch-minister-pushes-back-on-us-bid-to-tighten-china-chip-controls/ (24 Jun 2026); https://nltimes.nl/2026/04/14/netherlands-pushes-back-proposed-us-export-limits-asml (14 Apr 2026) | Absence elsewhere not established. |
| 38 | No Council act on the 2024 White Paper on Export Controls in Cellar; related items found are Commission or EESC documents, plus JOIN(2025) 977 "Strengthening EU economic security" (3 Dec 2025) and an EP-Commission joint statement (26 Jun 2026). | C | Cellar SPARQL (29 Oct 2026) | Council conclusions not checkable. |
| 39 | 2026 Council populations (Decision 2025/2427, Annex III): total 452,162,974; DE 83,502,300 (18.47%), FR 68,635,943 (15.18%), IT 59,635,202 (13.19%), ES 49,093,546 (10.86%), PL 37,475,594 (8.29%), RO 19,036,031 (4.21%), NL 18,191,086 (4.02%); 65% threshold 293,905,933; applies from 1 Jan 2026. | V | http://data.europa.eu/eli/dec/2025/2427/oj (17 Nov 2025; OJ 27 Nov 2025) | All 27 figures match the script. |
| 40 | EUROPOP2023 (proj_23np, BSL): EU-27 452,876,789 (2029), 452,700,101 (2030), 452,518,492 (2031); 2026 projection 453,303,452 with DE at 18.82% vs 18.47% in the Council figures. | V | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/proj_23np (updated 12 May 2026) | |
| 41 | Scenario seven hold 28.06% (2026), 27.82% (2029), 27.79% (2030), 27.76% (2031); only DE, FR, ES complete a block singly; no two-state completion exists; smallest completions otherwise need three states (e.g. BE, CZ, PT). | V | code/checks/council_revealed_blocking.py (rerun 29 Oct 2026) | Two-state check added. |
| 42 | Scenario + HU, SK, CZ: 33.79% (2026), 33.45% (2031). Single completions: 12 in 2026 (DE, FR, ES, RO, BE, PT, SE, GR, AT, BG, DK, FI); 10 in 2029 (adds BG to the 2031 list); 9 in 2030 and 2031. Without HU (31.68%): DE, FR, ES, RO. | C | Same script | Memo said BG "2026 only." |
| 43 | 13 smallest hold 9.58% and block by count; ordering A pivot RO at 38.00% (2026) and 37.45% (2031); ordering B pivot DE at 50.73%. | V | Same script | |
| 44 | Exact SS / normalised Banzhaf (2026): DE 17.54/12.03, FR 13.48/10.12, IT 11.53/8.87, ES 9.39/7.81, PL 6.69/6.32, RO 3.79/3.90, NL 3.66/3.80, IE 1.64/2.31, MT 0.87/1.74. 2031: DE 17.88/12.19, NL 3.69/3.84, RO 3.64/3.81. DE/NL ratio 4.8 (SS), 3.2 (Banzhaf). | C | Same script; independent 8m-draw MC (DE 17.53±0.01, FR 13.48±0.01, NL 3.66±0.01) | eu_inst's DE 17.74, FR 13.64, IT 11.60 are wrong; "about five times" holds for SS only. |
| 45 | Supermajority norms: scenario yes-share 71.94% (2026), 72.24% (2031), 20 yes-states. Minimal blocking subsets of the scenario seven: tau 75% IT+PL+NL (25.50%); 80% IT+PL (21.48%); 85% IT+NL (17.21%); above 86.81% IT alone (13.19%). | C | Supplementary script (scratchpad, 29 Oct 2026) | Memo's 75% and 90% examples were not minimal. |
| 46 | Magyar appointed Hungarian PM 9 May 2026 after Tisza won the 12 Apr 2026 election; Babiš inaugurated Czech PM 9 Dec 2025. | V | https://en.wikipedia.org/wiki/P%C3%A9ter_Magyar ; https://en.wikipedia.org/wiki/Andrej_Babi%C5%A1 | Secondary only. |
| 47 | Voting-result template says QMV is "at least 55% of the Member States (ie. 16)"; for EU-27 it is 15. | V | V109145/01 | |
| 48 | Scenario 2029: Commission opens first ACI examination (May 2029), finds coercion after four months; Arizona measure falls short of QMV; NL, IE oppose (transatlantic), PL and Baltics oppose (Russia), IT abstains. | V (cross-strand) | https://europe2031.ai (11 Jun 2026), via notes/review/e2031.md | The failing item is a response measure, voted in committee. |
| 49 | Tweede Kamer motion Piri c.s. (22 Jan 2026), keep economic countermeasures "waaronder het antidwanginstrument" in reserve over Greenland: adopted 103 to 46; caretaker cabinet advised against. | V (cross-strand) | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z01210&did=2026D02880, via notes/review/gap_dutch_domestic_politics.md | Not re-fetched. |

### Position matrix, corrected

Codes as in the memo. EV: F for, A against, Ab abstain (Zhang, verified for all 27). Suspensions: "nd" means no recorded dissent (27-0 in the two public votes). Turnberry: W welcomed, Q qualified, C critical, H hostile. Greenland: ACI sought activation; S6/S18 signed the 6 or 18 January statement; NS = would not vote for an EU statement; NM = no mention; Dlg = "dialogue, not statements"; M = tariffs "a mistake." Scenario 2029: O oppose, Ab abstain, Y implied yes. Completes = completes a blocking minority with the scenario seven plus HU, SK and CZ.

| State | EV | Susp. | Turnberry | Greenland | Other | Scenario | Verdict and correction |
|---|---|---|---|---|---|---|---|
| AT | Ab | nd | - | - | - | Y | V. Completes 2026 to 2031. |
| BE | Ab | nd | - | - | - | Y | V. Completes 2026 to 2031. |
| BG | F | nd | - | - | - | Y | C. Completes in 2026 and 2029, not "2026 only." |
| HR | Ab | nd | - | - | - | Y | V. Count route only. |
| CY | Ab | nd | - | - | - | Y | V. Count route only. |
| CZ | Ab | nd | - | Dlg | - | Y | V. Babiš quote verified. |
| DK | F | nd | Q | S6, S18 | - | Y | V. Completes 2026 only. |
| EE | F | nd | - | - | - | O | V. |
| FI | Ab | nd | W | S18 | - | Y | V. Completes 2026 only (35.03%). |
| FR | F | nd | C | ACI, S6, S18 | - | Y | V. Single-state completion of the scenario seven. |
| DE | A | nd | W | S6, S18, ACI? | Nexperia: informed 30 Sep 2025 | Y | C. "ACI?" unverified (Politico); pressure on The Hague over Nexperia unverified. |
| GR | Ab | nd | - | - | - | Y | V. Completes 2026 to 2031. |
| HU | A | nd | H | NS | Gov't change 9 May 2026 | Y | C. Wording: "will not vote for any EU statement." April 2025 "against" unverified. |
| IE | F | nd | Q | - | - | O | V. |
| IT | F | nd | Q (positive if details hold) | S6, M | Presidency H1 2028 | Ab | C. Turnberry coded Q rather than W: Meloni conditioned her view on the details. |
| LV | F | nd | - | - | Presidency H2 2028 | O | V. |
| LT | F | nd | - | - | - | O | V. |
| LU | Ab | nd | - | - | Presidency H1 2029 | Y | V. |
| MT | A | nd | - | - | Presidency H2 2030 | Y | V. |
| NL | F | nd | - | S18 | Nexperia order 30 Sep 2025, suspended 19 Nov 2025; MATCH: opposes coercion; Tweede Kamer ACI motion 22 Jan 2026 | O | C. Added parliamentary motion; Presidency H2 2029. |
| PL | F | nd | - | S6 | - | O | C. "Tusk said Poland would not deploy troops" not in the cited source: U. |
| PT | Ab | nd | - | - | - | Y | V. Completes 2026 to 2031. |
| RO | Ab | nd | W | - | - | Y | V. Completes with scenario + SK + CZ even without HU; pivot of ordering A. |
| SK | A | nd | - | NM | Presidency H1 2030 | Y | C. Silent (statement omitted Greenland), not "declined." |
| SI | A | nd | - | - | - | Y | V. |
| ES | Ab | nd | Q | S6 | - | Y | V. Single-state completion. |
| SE | Ab | nd | Q | S18 | - | Y | V. Completes 2026 to 2031. |

## Citation verdicts

| Key | Verdict | Note |
|---|---|---|
| heisenberg2005institution | V | EJPR 44(1): 65-90. "81 per cent of decisions are made by consensus." |
| hage2013coalition | V | BJPS 43(3): 481-504 (online 25 Sep 2012). Threshold raises winning-coalition size; membership does not. |
| novak2013silence | V | JCMS 51(6): 1091-1107. |
| mattila2004contested | C | EJPR 43(1): 29-50. Large countries "more likely to vote 'no' than small countries"; presidencies "vote less against the majority ... than otherwise," not "rarely." |
| meunier2000single | V | IO 54(1): 103-135. Conservative vs reformist contexts in the abstract; the direction (restrictive rules weaken a reformist EU) is from the article body, not re-read here. |
| golub1999shadow | M | IO 53(4): 733-764. Abstract challenges the view that majority voting unblocked EC decision-making; reforms "encumbered rather than eased"; effects mediated by preferences. Does not support "decisions are made in the shadow of the vote." Closed access; full text not read. |
| hayesrenshaw2006when | V | JCMS 44(1): 161-194. Rare explicit voting; nearly half of roll calls lone dissent; Germany "no" or abstains most often; implicit voting at officials' level, unrecorded. |
| mattila2001why | V | EUP 2(1): 31-52. Crossref title is "Why Unanimity in the Council?" without subtitle; subtitle "A Roll Call Analysis of Council Voting" not confirmed. |
| mattila2009roll | V | EJPR 48(6): 840-857. North-south-east pattern. |
| hosli2011voting | V | JCMS 49(6): 1249-1270 (2004-2006 votes). |
| hagemann2017government | V | CPS 50(6): 850-876 (online 12 Jan 2016). |
| bailer2015money | V | JCMS 53(3): 437-456 (online 7 Aug 2014). "Structural attributes" of member states; ideology "inconsistent and marginal." |
| pircher2021oppositional | V | EUP 22(3): 472-494. |
| wratil2019public | V | EUP 20(3): 511-531. Positions "predict subsequent votes on legislative acts." |
| hobolt2020contestation | V | JEPP 27(3): 362-381. ECOFIN 2010-2015. |
| novak2021enduring | V | JEI 43(4): 475-493 (online 7 Aug 2020). |
| boranbayakan2017imperfect | V | EUP 18(2): 168-187. Co-decision, Nov 1993 to Dec 2009. |
| vangruisen2021commission | V | EJPE 70: 102040. A spatial-model result, not an empirical finding. |
| hage2017scheduling | V | JEPP 24(5): 695-713 (online 13 Apr 2016). Working-party meeting time 1995-2014. |
| lewis2005janus | V | IO 59(4): 937-971. |
| kleine2013informal | V | Cornell University Press, 2013, ISBN 9780801452116. |
| thomson2011resolving | V | Cambridge University Press, 2011; subtitle "Legislative Decision-Making before and after Enlargement" confirmed in Crossref. |
| evenett2005politicisation | V | World Economy 28(5): 701-717. Disagreements "may well have been partly responsible" for fewer investigations (hedged). |
| zhang2025countervailing | V | Song and Zhou (eds), ANU Press, 2025, pp. 125-149; Table 6.2 verified. |
| bauerledanzman2024geoeconomic | V | JCMS 62(4): 1097-1115. |
| schmitz2023open | V | JCMS 61(3): 834-852. "Coalition magnet." |
| jackson2025deter | V | JIEL 28(4): 567-588. |
| hillebrandt2014transparency | V | ELJ 20(1): 1-20. |
| commission2023acistatement | V | OJ C, C/2023/1341, 7.12.2023. |
| council2009rules | V | OJ L 325, 11.12.2009, p. 35. Later amendments not checked. |
| council2016presidency | V | OJ L 208, 2.8.2016, p. 42; full title below. |
| acicommittee2024rop | C | Add Art. 10(1) (position recorded in minutes on request). |
| commission2024bev | V | Recital 1432 verified. |
| eurostat2023europop | V | Dataset updated 12 May 2026. |
| eu2023aci (added) | V | Regulation (EU) 2023/2675; recital 85, Arts 4, 5, 12(5), 18, 19(3). |
| eu2011comitology (added) | V | Regulation (EU) No 182/2011, Arts 5 and 6. |
| council2025population (added) | V | Council Decision (EU, Euratom) 2025/2427. |

## Modeling implications

1. **Keep formal QMV as the primitive and justify it with Häge (2013), not Golub (1999).** The formal blocking family defines the shadow; consensus is what is observed on the path. Golub supports only the weaker statement that institutional effects are conditional on preferences.

2. **Game form, corrected.**
   - G0 (Commission): examine or not (Art. 4(1), full discretion).
   - G1 (Council): determination by positive QMV, abstention counting as no. The Presidency controls the timing of a vote (RoP Art. 11(1)), subject to a majority forcing one and to the 8-week clock of Art. 5(6), which can be extended on notice.
   - G2a (committee, Commission chair): positive QMV on response measures; a no-opinion bars adoption.
   - G2b (appeal committee): the Commission may adopt unless a QMV is against (Reg. 182/2011 Art. 6(3)), but has committed, in ACI recital 85 and C/2023/1341, not to go against "any predominant position."

   The binding rule at G2 is therefore an effective threshold tau set by the Commission's own norm, not the formal rule. Model tau as a parameter with support from about 55 per cent (simple majority) to 100 per cent (consensus). The Presidency parameter enters only at G1.

3. **Restate the 2029 claim.** Suggested wording: "Under formal rules and 2026 weights the states the scenario names (28.06 per cent, seven members) cannot block the Council determination, and at the response-measure stage they cannot block at all once the Commission takes the act to appeal. The failed vote is an equilibrium only if the Commission's commitment not to override a 'predominant position' makes the effective threshold exceed about 72 per cent of population or 20 states, or if the non-yes set is larger than the scenario says. In either case the observable we expect is no ASML measure tabled, or one tabled without the ASML element, rather than a recorded defeat."

4. **Arm versus fire.** The US-facing record separates two acts. Member states authorise countermeasures by QMV readily (April and July 2025). They suspend them readily and without dissent when Washington makes a concession, and the Commission does the suspending by urgency procedure before consulting the committee. The ACI hard-wires the same asymmetry: urgency is available to suspend or amend response measures, never to adopt them (Art. 12(5)). Model escalation and de-escalation as different moves. Arming is cheap and passes the formal threshold. Firing has never been tested. De-escalation is unilateral for the Commission. This bears on credibility. Europe can commit to *withdrawing* a threat quickly (an assurance) more easily than to executing one, and a small US concession reliably defuses an armed measure. For the US, the cost of defeating a countermeasure, Phi(0), should include the option of a cheap partial concession that triggers suspension, not only the cost of buying a blocking minority.

5. **Prior on US-facing resolve.** Replace "a majority of member states are doves" with "member states arm by QMV and suspend on concessions; their willingness to let a measure bite against a non-conceding US is unobserved." Use a diffuse prior on execution and a tight prior on suspension after a concession.

6. **Pivots.** Formal QMV, all years 2026-2031: the scenario seven need DE, FR or ES, or at least three other states. With HU, SK and CZ added, one of twelve states (2026), ten (2029) or nine (2030-2031) suffices, or any three more by count. Without HU, the completing states are DE, FR, ES and RO. Romania (welcomed Turnberry, EV abstention, eastern flank) is the cheapest single pivot for Washington when the CEE governments hold. The CEE "bloc" should be modelled as a random set: Hungary's government changed in May 2026, Slovakia was silent rather than opposed in January 2026, and Greenland statements need unanimity, so they reveal less about QMV behaviour than a vote would.

7. **Supermajority robustness, corrected.** The scenario coalition blocks if and only if tau > 71.94 per cent (2026) or 72.24 per cent (2031). The minimal blocking subsets of the scenario seven are IT, PL and NL at tau = 75 per cent; IT and PL at 80; IT and NL at 85; and Italy alone above 86.81 per cent. Under strict consensus any one state blocks. The comparative static is that the cheapest blocking coalition shrinks toward Italy as tau rises. Italy is the scenario's abstainer and held the Presidency in H1 2028, so it is the natural target of US side-payments in a high-tau world.

8. **Abstention is cheap.** In the EV vote 12 of 27 states abstained. At G1 and G2a an abstention has the effect of a no. At G2b, under the formal rule, abstention helps the Commission because only votes against count, which flips its value. Price an abstention below a no at G1 and G2a, and note that the US must convert abstentions into votes against to block formally at G2b.

9. **Asymmetry of defaults (China versus US).** In trade defence the Commission adopted with 10 supporters holding 46 per cent, because a no-opinion lets it adopt unless a simple majority opposes. Under the ACI's positive-QMV gates the same distribution would fall 19.02 points and five states short. Build the default rule into the game form, consistent with Meunier's (2000) conservative versus reformist logic.

10. **Cross-direction coalitions.** The Netherlands, Ireland, Poland and the Baltic states voted for the China-facing EV duties and are the scenario's opponents of the US-facing measure. Germany and the CEE states voted against or abstained on EVs. Use separate q_i for China-facing and US-facing measures; one Atlanticist-autonomist axis does not fit.

11. **Power indices.** Use DE 17.54 (SS) and 12.03 (Banzhaf), and NL 3.66 and 3.80, and say "4.8 times on Shapley-Shubik, 3.2 times on Banzhaf." Correct the eu_inst table to FR 13.48 and IT 11.53. Dutch leverage still comes from gatekeeping, not voting weight.

12. **Review clause.** The Commission must review the ACI no later than 27 December 2028 (Art. 19(3)), just before the scenario's 2029 use. Treat tau and the G2 rules as potentially endogenous (Europe tying its hands), as proposed in lit_alliance.

13. **Data action.** Under Regulation 1049/2001, request voting sheets 102870 (EV), 107095 (April 2025), 109049 (July 2025), 113482 (January 2026) and 117368 (July 2026), and summary records 102871, 107061 and 109043. Separately, the Council's public voting results for Regulations 2026/1455 and 2026/1461 (legislative acts adopted 25 June 2026 to implement Turnberry concessions) would give per-state votes on a US-facing file without any request, since votes on legislative acts are public.

## Open questions

- Per-state votes on the 9 April and 24 July 2025 countermeasure opinions (Hungary "against" in April 2025 is reported but unverified).
- Council voting results on Regulations 2026/1455 and 2026/1461 (25 June 2026): did any state vote against or abstain on implementing the EU's Turnberry tariff cuts? consilium.europa.eu was not reachable.
- Did Germany formally ask the Commission to explore the ACI in January 2026 (Politico, 20 January 2026)? Which states backed France at the 18 January ambassadors' meeting?
- How does the Commission interpret "predominant position" in recital 85 and C/2023/1341: a simple majority, a QMV, or any sizeable minority? No ACI case exists to reveal it; comitology practice in other sensitive files may.
- Would per-state results of a Council vote on an ACI determination be published automatically (RoP Art. 9(1)), or does the "international relations" exclusion in Art. 8(1) apply? Have Arts 8, 9 or 11 been amended since 2009?
- Has the Magyar government taken any position on US trade coercion, the ACI or Chinese investment screening that would move Hungary out of the CEE set?
- Will the review due by 27 December 2028 propose changes to Art. 18(2) or to the urgency asymmetry in Art. 12(5)?
- Base rate: how often has the Commission concluded an examination or tabled a Council implementing act that then failed to obtain QMV? This would calibrate the cost of visible failure.

## BibTeX (verified or corrected entries)

```bibtex
@article{heisenberg2005institution,
  author  = {Heisenberg, Dorothee},
  title   = {The Institution of `Consensus' in the {European Union}: Formal versus Informal Decision-Making in the {Council}},
  journal = {European Journal of Political Research},
  year    = {2005},
  volume  = {44},
  number  = {1},
  pages   = {65--90},
  doi     = {10.1111/j.1475-6765.2005.00219.x}
}

@article{hage2013coalition,
  author  = {H{\"a}ge, Frank M.},
  title   = {Coalition Building and Consensus in the {Council of the European Union}},
  journal = {British Journal of Political Science},
  year    = {2013},
  volume  = {43},
  number  = {3},
  pages   = {481--504},
  doi     = {10.1017/S0007123412000439}
}

@article{novak2013silence,
  author  = {Novak, St{\'e}phanie},
  title   = {The Silence of Ministers: Consensus and Blame Avoidance in the {Council of the European Union}},
  journal = {JCMS: Journal of Common Market Studies},
  year    = {2013},
  volume  = {51},
  number  = {6},
  pages   = {1091--1107},
  doi     = {10.1111/jcms.12063}
}

@article{mattila2004contested,
  author  = {Mattila, Mikko},
  title   = {Contested Decisions: Empirical Analysis of Voting in the {European Union Council of Ministers}},
  journal = {European Journal of Political Research},
  year    = {2004},
  volume  = {43},
  number  = {1},
  pages   = {29--50},
  doi     = {10.1111/j.1475-6765.2004.00144.x}
}

@article{meunier2000single,
  author  = {Meunier, Sophie},
  title   = {What Single Voice? {European} Institutions and {EU}--{U.S.} Trade Negotiations},
  journal = {International Organization},
  year    = {2000},
  volume  = {54},
  number  = {1},
  pages   = {103--135},
  doi     = {10.1162/002081800551136}
}

@article{golub1999shadow,
  author  = {Golub, Jonathan},
  title   = {In the Shadow of the Vote? {Decision} Making in the {European Community}},
  journal = {International Organization},
  year    = {1999},
  volume  = {53},
  number  = {4},
  pages   = {733--764},
  doi     = {10.1162/002081899551057}
}

@article{hayesrenshaw2006when,
  author  = {Hayes-Renshaw, Fiona and van Aken, Wim and Wallace, Helen},
  title   = {When and Why the {EU Council of Ministers} Votes Explicitly},
  journal = {JCMS: Journal of Common Market Studies},
  year    = {2006},
  volume  = {44},
  number  = {1},
  pages   = {161--194},
  doi     = {10.1111/j.1468-5965.2006.00618.x}
}

@article{mattila2001why,
  author  = {Mattila, Mikko and Lane, Jan-Erik},
  title   = {Why Unanimity in the {Council}? {A} Roll Call Analysis of Council Voting},
  journal = {European Union Politics},
  year    = {2001},
  volume  = {2},
  number  = {1},
  pages   = {31--52},
  doi     = {10.1177/1465116501002001002},
  note    = {Crossref lists the title as ``Why Unanimity in the Council?''; subtitle not confirmed}
}

@article{mattila2009roll,
  author  = {Mattila, Mikko},
  title   = {Roll Call Analysis of Voting in the {European Union Council of Ministers} after the 2004 Enlargement},
  journal = {European Journal of Political Research},
  year    = {2009},
  volume  = {48},
  number  = {6},
  pages   = {840--857},
  doi     = {10.1111/j.1475-6765.2009.01850.x}
}

@article{hosli2011voting,
  author  = {Hosli, Madeleine O. and Mattila, Mikko and Uriot, Marc},
  title   = {Voting in the {Council of the European Union} after the 2004 Enlargement: A Comparison of Old and New Member States},
  journal = {JCMS: Journal of Common Market Studies},
  year    = {2011},
  volume  = {49},
  number  = {6},
  pages   = {1249--1270},
  doi     = {10.1111/j.1468-5965.2011.02196.x}
}

@article{hagemann2017government,
  author  = {Hagemann, Sara and Hobolt, Sara B. and Wratil, Christopher},
  title   = {Government Responsiveness in the {European Union}: Evidence from {Council} Voting},
  journal = {Comparative Political Studies},
  year    = {2017},
  volume  = {50},
  number  = {6},
  pages   = {850--876},
  doi     = {10.1177/0010414015621077}
}

@article{bailer2015money,
  author  = {Bailer, Stefanie and Mattila, Mikko and Schneider, Gerald},
  title   = {Money Makes the {EU} Go Round: The Objective Foundations of Conflict in the {Council of Ministers}},
  journal = {JCMS: Journal of Common Market Studies},
  year    = {2015},
  volume  = {53},
  number  = {3},
  pages   = {437--456},
  doi     = {10.1111/jcms.12194}
}

@article{pircher2021oppositional,
  author  = {Pircher, Brigitte and Farjam, Mike},
  title   = {Oppositional Voting in the {Council of the EU} between 2010 and 2019: Evidence for Differentiated Politicisation},
  journal = {European Union Politics},
  year    = {2021},
  volume  = {22},
  number  = {3},
  pages   = {472--494},
  doi     = {10.1177/14651165211004754}
}

@article{wratil2019public,
  author  = {Wratil, Christopher and Hobolt, Sara B.},
  title   = {Public Deliberations in the {Council of the European Union}: Introducing and Validating {DICEU}},
  journal = {European Union Politics},
  year    = {2019},
  volume  = {20},
  number  = {3},
  pages   = {511--531},
  doi     = {10.1177/1465116519839152}
}

@article{hobolt2020contestation,
  author  = {Hobolt, Sara B. and Wratil, Christopher},
  title   = {Contestation and Responsiveness in {EU Council} Deliberations},
  journal = {Journal of European Public Policy},
  year    = {2020},
  volume  = {27},
  number  = {3},
  pages   = {362--381},
  doi     = {10.1080/13501763.2020.1712454}
}

@article{novak2021enduring,
  author  = {Novak, St{\'e}phanie and Rozenberg, Olivier and Bendjaballah, Selma},
  title   = {Enduring Consensus: Why the {EU} Legislative Process Stays the Same},
  journal = {Journal of European Integration},
  year    = {2021},
  volume  = {43},
  number  = {4},
  pages   = {475--493},
  doi     = {10.1080/07036337.2020.1800679}
}

@article{boranbayakan2017imperfect,
  author  = {Boranbay-Akan, Serra and K{\"o}nig, Thomas and Osnabr{\"u}gge, Moritz},
  title   = {The Imperfect Agenda-Setter: Why Do Legislative Proposals Fail in the {EU} Decision-Making Process?},
  journal = {European Union Politics},
  year    = {2017},
  volume  = {18},
  number  = {2},
  pages   = {168--187},
  doi     = {10.1177/1465116516674338}
}

@article{vangruisen2021commission,
  author  = {van Gruisen, Philippe and Crombez, Christophe},
  title   = {The {Commission} and the {Council Presidency} in the {European Union}: Strategic Interactions and Legislative Powers},
  journal = {European Journal of Political Economy},
  year    = {2021},
  volume  = {70},
  pages   = {102040},
  doi     = {10.1016/j.ejpoleco.2021.102040}
}

@article{hage2017scheduling,
  author  = {H{\"a}ge, Frank M.},
  title   = {The Scheduling Power of the {EU Council Presidency}},
  journal = {Journal of European Public Policy},
  year    = {2017},
  volume  = {24},
  number  = {5},
  pages   = {695--713},
  doi     = {10.1080/13501763.2016.1158203}
}

@article{lewis2005janus,
  author  = {Lewis, Jeffrey},
  title   = {The {Janus} Face of {Brussels}: Socialization and Everyday Decision Making in the {European Union}},
  journal = {International Organization},
  year    = {2005},
  volume  = {59},
  number  = {4},
  pages   = {937--971},
  doi     = {10.1017/S0020818305050320}
}

@book{kleine2013informal,
  author    = {Kleine, Mareike},
  title     = {Informal Governance in the {European Union}: How Governments Make International Organizations Work},
  publisher = {Cornell University Press},
  address   = {Ithaca, NY},
  year      = {2013},
  isbn      = {9780801452116},
  doi       = {10.7591/cornell/9780801452116.001.0001}
}

@book{thomson2011resolving,
  author    = {Thomson, Robert},
  title     = {Resolving Controversy in the {European Union}: Legislative Decision-Making before and after Enlargement},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2011},
  isbn      = {9781107013766},
  doi       = {10.1017/CBO9781139005357}
}

@article{evenett2005politicisation,
  author  = {Evenett, Simon J. and Vermulst, Edwin},
  title   = {The Politicisation of {EC} Anti-dumping Policy: Member States, Their Votes and the {European Commission}},
  journal = {The World Economy},
  year    = {2005},
  volume  = {28},
  number  = {5},
  pages   = {701--717},
  doi     = {10.1111/j.1467-9701.2005.00701.x}
}

@incollection{zhang2025countervailing,
  author    = {Zhang, ZhongXiang},
  title     = {The {European Union}'s Countervailing Duties on Electric Vehicles from {China}: Disputes and Prospects},
  booktitle = {The Great Energy Transformation in {China}},
  editor    = {Song, Ligang and Zhou, Yixiao},
  publisher = {ANU Press},
  address   = {Canberra},
  year      = {2025},
  pages     = {125--149},
  isbn      = {9781760467210},
  doi       = {10.22459/GETC.2025.06}
}

@article{bauerledanzman2024geoeconomic,
  author  = {Bauerle Danzman, Sarah and Meunier, Sophie},
  title   = {The {EU}'s Geoeconomic Turn: From Policy Laggard to Institutional Innovator},
  journal = {JCMS: Journal of Common Market Studies},
  year    = {2024},
  volume  = {62},
  number  = {4},
  pages   = {1097--1115},
  doi     = {10.1111/jcms.13599}
}

@article{schmitz2023open,
  author  = {Schmitz, Luuk and Seidl, Timo},
  title   = {As Open as Possible, as Autonomous as Necessary: Understanding the Rise of Open Strategic Autonomy in {EU} Trade Policy},
  journal = {JCMS: Journal of Common Market Studies},
  year    = {2023},
  volume  = {61},
  number  = {3},
  pages   = {834--852},
  doi     = {10.1111/jcms.13428}
}

@article{jackson2025deter,
  author  = {Jackson, Miles and Paddeu, Federica},
  title   = {`To Deter and Counteract Economic Coercion': The Puzzle of Countermeasures in the {European Union}'s {Anti-Coercion Instrument}},
  journal = {Journal of International Economic Law},
  year    = {2025},
  volume  = {28},
  number  = {4},
  pages   = {567--588},
  doi     = {10.1093/jiel/jgaf047}
}

@article{hillebrandt2014transparency,
  author  = {Hillebrandt, Maarten Zbigniew and Curtin, Deirdre and Meijer, Albert},
  title   = {Transparency in the {EU Council of Ministers}: An Institutional Analysis},
  journal = {European Law Journal},
  year    = {2014},
  volume  = {20},
  number  = {1},
  pages   = {1--20},
  doi     = {10.1111/eulj.12051}
}

@misc{eu2023aci,
  author       = {{European Parliament and Council of the European Union}},
  title        = {Regulation ({EU}) 2023/2675 of the {European Parliament} and of the {Council} of 22 {November} 2023 on the Protection of the {Union} and Its Member States from Economic Coercion by Third Countries},
  howpublished = {Official Journal of the European Union, L series, 2023/2675, 7.12.2023},
  year         = {2023},
  url          = {http://data.europa.eu/eli/reg/2023/2675/oj}
}

@misc{eu2011comitology,
  author       = {{European Parliament and Council of the European Union}},
  title        = {Regulation ({EU}) No 182/2011 of the {European Parliament} and of the {Council} of 16 {February} 2011 Laying Down the Rules and General Principles Concerning Mechanisms for Control by Member States of the {Commission}'s Exercise of Implementing Powers},
  howpublished = {Official Journal of the European Union, L 55, 28.2.2011, p. 13},
  year         = {2011},
  url          = {http://data.europa.eu/eli/reg/2011/182/oj}
}

@misc{commission2023acistatement,
  author       = {{European Commission}},
  title        = {Statement by the {Commission} on the Use of Examination Procedure for {Union} Response Measures under {Regulation (EU) 2023/2675} on the Protection of the {Union} and Its Member States from Economic Coercion by Third Countries},
  howpublished = {Official Journal of the European Union, C series, C/2023/1341, 7.12.2023},
  year         = {2023},
  url          = {http://data.europa.eu/eli/C/2023/1341/oj}
}

@misc{council2009rules,
  author       = {{Council of the European Union}},
  title        = {Council Decision of 1 {December} 2009 Adopting the {Council}'s Rules of Procedure (2009/937/{EU})},
  howpublished = {Official Journal of the European Union, L 325, 11.12.2009, p. 35},
  year         = {2009},
  url          = {http://data.europa.eu/eli/dec/2009/937/oj}
}

@misc{council2016presidency,
  author       = {{Council of the European Union}},
  title        = {Council Decision ({EU}) 2016/1316 of 26 {July} 2016 Amending Decision 2009/908/{EU}, Laying Down Measures for the Implementation of the {European Council} Decision on the Exercise of the Presidency of the {Council}, and on the Chairmanship of Preparatory Bodies of the {Council}},
  howpublished = {Official Journal of the European Union, L 208, 2.8.2016, p. 42},
  year         = {2016},
  url          = {http://data.europa.eu/eli/dec/2016/1316/oj}
}

@misc{council2025population,
  author       = {{Council of the European Union}},
  title        = {Council Decision ({EU}, {Euratom}) 2025/2427 of 17 {November} 2025 Amending the {Council}'s Rules of Procedure},
  howpublished = {Official Journal of the European Union, L series, 2025/2427, 27.11.2025},
  year         = {2025},
  url          = {http://data.europa.eu/eli/dec/2025/2427/oj}
}

@misc{acicommittee2024rop,
  author       = {{Anti-Coercion Committee}},
  title        = {Rules of Procedure for the {Anti-Coercion Committee} ({Committee} on the Protection of the Interests of the {Union} and Its Member States from Economic Coercion by Third Countries), Adopted at the Meeting of 7 {February} 2024},
  howpublished = {Commission comitology register, Ares(2024)1439526},
  year         = {2024},
  url          = {https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/380298/095426/1/attachment}
}

@misc{commission2024bev,
  author       = {{European Commission}},
  title        = {Commission Implementing Regulation ({EU}) 2024/2754 of 29 {October} 2024 Imposing a Definitive Countervailing Duty on Imports of New Battery Electric Vehicles Designed for the Transport of Persons Originating in the {People's Republic of China}},
  howpublished = {Official Journal of the European Union, L series, 2024/2754, 29.10.2024},
  year         = {2024},
  url          = {http://data.europa.eu/eli/reg_impl/2024/2754/oj}
}

@misc{commission2025rebalancing1564,
  author       = {{European Commission}},
  title        = {Commission Implementing Regulation ({EU}) 2025/1564 of 24 {July} 2025 on Commercial Rebalancing Measures Concerning Certain Products Originating in the {United States of America} and Certain Products Exported from the {Union} to the {United States of America}},
  howpublished = {Official Journal of the European Union, L series, 2025/1564, 24.7.2025},
  year         = {2025},
  url          = {http://data.europa.eu/eli/reg_impl/2025/1564/oj}
}

@misc{commission2025suspension786,
  author       = {{European Commission}},
  title        = {Commission Implementing Regulation ({EU}) 2025/786 of 14 {April} 2025 Suspending Commercial Rebalancing Measures Concerning Certain Products Originating in the {United States} Imposed by Implementing Regulation ({EU}) 2025/778 and Amending Implementing Regulation ({EU}) 2023/2882},
  howpublished = {Official Journal of the European Union, L series, 2025/786, 14.4.2025},
  year         = {2025},
  url          = {http://data.europa.eu/eli/reg_impl/2025/786/oj}
}

@misc{commission2025suspension1727,
  author       = {{European Commission}},
  title        = {Commission Implementing Regulation ({EU}) 2025/1727 of 5 {August} 2025 Suspending Commercial Rebalancing Measures Concerning Certain Products Originating in the {United States of America} and Certain Products Exported from the {Union} to the {United States of America} Imposed by Implementing Regulation ({EU}) 2025/1564},
  howpublished = {Official Journal of the European Union, L series, 2025/1727, 5.8.2025},
  year         = {2025},
  url          = {http://data.europa.eu/eli/reg_impl/2025/1727/oj}
}

@misc{commission2026suspension1893,
  author       = {{European Commission}},
  title        = {Commission Implementing Regulation ({EU}) 2026/1893 of 30 {July} 2026 Suspending Commercial Rebalancing Measures Concerning Certain Products Originating in the {United States of America} and Certain Products Exported from the {Union} to the {United States of America} Imposed by Implementing Regulation ({EU}) 2025/1564},
  howpublished = {Official Journal of the European Union, L series, 2026/1893, 31.7.2026},
  year         = {2026},
  url          = {http://data.europa.eu/eli/reg_impl/2026/1893/oj}
}

@misc{tbc2025vote109145,
  author       = {{European Commission, DG Trade}},
  title        = {Overall Voting Result on a Formal Opinion, Committee {C22700}, Voting Sheet {V109145/01} (Written Consultation, Urgency Procedure, Opinion of 18 {July} 2025)},
  howpublished = {Commission comitology register, Ares(2025)6207499, 30.7.2025},
  year         = {2025},
  url          = {https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/484242/109145/1/attachment}
}

@misc{tbc2025vote109281,
  author       = {{European Commission, DG Trade}},
  title        = {Overall Voting Result on a Formal Opinion, Committee {C22700}, Voting Sheet {V109281/01} (Written Consultation, Urgency Procedure, Opinion of 12 {August} 2025)},
  howpublished = {Commission comitology register, Ares(2025)6617481, 14.8.2025},
  year         = {2025},
  url          = {https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/485429/109281/1/attachment}
}

@misc{tbc2026summaryjan,
  author       = {{European Commission, DG Trade}},
  title        = {Summary Record, Meeting of the {Trade Barriers Committee}, 28 {January} 2026},
  howpublished = {Commission comitology register, document 113452},
  year         = {2026},
  url          = {https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/517999/113452/1/attachment}
}

@misc{tbc2026summaryjul,
  author       = {{European Commission, DG Trade}},
  title        = {Summary Record, Meeting of the {Trade Barriers Committee}, 17 {July} 2026},
  howpublished = {Commission comitology register, Ares(2026)7539075, 31.7.2026},
  year         = {2026},
  url          = {https://ec.europa.eu/transparency/comitology-register/core/api/integration/ers/541599/117365/1/attachment}
}

@misc{commission2024evstatement,
  author       = {{European Commission}},
  title        = {Commission Proposal to Impose Tariffs on Imports of Battery Electric Vehicles from {China} Obtains Necessary Support from {EU} Member States},
  howpublished = {Statement STATEMENT/24/5041, 4 October 2024},
  year         = {2024},
  url          = {https://ec.europa.eu/commission/presscorner/detail/en/statement_24_5041}
}

@misc{commission2025usstatement,
  author       = {{European Commission}},
  title        = {Commission Proposal to Impose Trade Countermeasures against {US} Obtains Necessary Support from {EU} Member States},
  howpublished = {Statement STATEMENT/25/1025, 9 April 2025},
  year         = {2025},
  url          = {https://ec.europa.eu/commission/presscorner/detail/en/statement_25_1025}
}

@misc{karremans2025nexperia717,
  author       = {Karremans, V. P. G.},
  title        = {Brief van de {Minister} van {Economische Zaken} over {Nexperia} (opschorting bevel)},
  howpublished = {Kamerstukken II 2025/26, 32 637, nr. 717, 19 November 2025},
  year         = {2025},
  url          = {https://zoek.officielebekendmakingen.nl/kst-32637-717.html}
}

@misc{karremans2025nexperia720,
  author       = {Karremans, V. P. G.},
  title        = {Brief van de {Minister} van {Economische Zaken} met openbare tijdslijn {Nexperia}},
  howpublished = {Kamerstukken II 2025/26, 32 637, nr. 720, 2 December 2025},
  year         = {2025},
  url          = {https://zoek.officielebekendmakingen.nl/kst-32637-720.html}
}

@misc{aljazeera2025turnberry,
  author       = {{News Agencies}},
  title        = {How {European} Leaders Are Reacting to {EU}-{US} Trade Deal},
  howpublished = {Al Jazeera, 28 July 2025 (byline ``By News Agencies'')},
  year         = {2025},
  url          = {https://www.aljazeera.com/news/2025/7/28/how-european-leaders-are-reacting-to-eu-us-trade-deal}
}

@misc{dazio2026greenland,
  author       = {Dazio, Stefanie and Lawless, Jill and Burrows, Emma},
  title        = {Europe Warns of `Dangerous Downward Spiral' after {Trump} Threatens Tariffs over {Greenland}},
  howpublished = {Associated Press, via ABC7 News, 19 January 2026},
  year         = {2026},
  url          = {https://abc7news.com/post/europe-warns-dangerous-downward-spiral-trump-threatens-tariffs-greenland/18427942/}
}

@misc{stm2026greenland,
  author       = {{Statsministeriet (Danish Prime Minister's Office)}},
  title        = {F{\ae}llesudtalelse om {Gr{\o}nland}},
  howpublished = {Joint statement by the leaders of France, Germany, Italy, Poland, Spain, the United Kingdom and Denmark, 6 January 2026},
  year         = {2026},
  url          = {https://stm.dk/statsministeriet/publikationer/faellesudtalelse-om-groenland/}
}

@misc{zsiros2026greenland,
  author       = {Zs{\'\i}ros, S{\'a}ndor},
  title        = {Bot a k{\"u}ll{\H o}k k{\"o}z{\"o}tt: {Magyarorsz{\'a}g} blokkol b{\'a}rmilyen {EU}-s {\'a}ll{\'a}sfoglal{\'a}st {Gr{\"o}nandr{\'o}l}},
  howpublished = {Euronews (Hungarian edition), 19 January 2026, updated 20 January 2026},
  year         = {2026},
  url          = {https://hu.euronews.com/my-europe/2026/01/19/orban-fico-babis-europa-trump-parti-vezetoi-csendben-vannak-a-gronlandi-valsaggal-kapcsola},
  note         = {Byline reads ``Zs{\'\i}ros S{\'a}ndor \& FT''; ``Gr{\"o}nandr{\'o}l'' [sic] in the headline}
}

@misc{vangerven2026sjoerdsma,
  author       = {van Gerven, Paul},
  title        = {Dutch Minister Pushes Back on {US} Bid to Tighten {China} Chip Controls},
  howpublished = {Bits\&Chips, 24 June 2026},
  year         = {2026},
  url          = {https://bits-chips.com/article/dutch-minister-pushes-back-on-us-bid-to-tighten-china-chip-controls/}
}

@misc{eurostat2023europop,
  author       = {{Eurostat}},
  title        = {{EUROPOP2023} Population Projections: Population on 1st January by Age, Sex and Type of Projection (proj\_23np)},
  howpublished = {Eurostat database, dataset updated 12 May 2026, retrieved 29 October 2026},
  year         = {2026},
  url          = {https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/proj_23np}
}
```
