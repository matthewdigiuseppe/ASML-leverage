# Gap strand: closest formal models and the novelty claim

Strand: hegemonic-alignment trade models, alliance-trade bargaining, client auctions, control rights, and the economics of aftermarket (servicing) hold-up.

Checked 2026-10-29 (task date 2026-10-28). Adversarial re-check of the strand memo.

## Method and limits

The shared WebSearch budget for this turn was exhausted before the first query of this check, so no keyword web search was run. That was also true of the original memo. Every bibliographic item was instead checked against primary records by direct lookup:

- Crossref DOI records for all items that have a DOI, and OpenAlex DOI records for abstracts and online dates.
- RePEc/IDEAS article pages for items without a usable Crossref record (Jehiel, Moldovanu and Stacchetti 1996; Bernheim and Whinston 1986 pages; Jehiel and Moldovanu 1995 pages; Morita and Waldman 2004; Carlton and Waldman 2010; Hart and Moore 1990).
- Full texts where an open copy existed: Bueno de Mesquita and Smith (2016, author PDF); Harstad (NBER WP 17409); Clayton, Maggiori and Schreger (NBER WP 31852, NBER WP 33681, and the published Econometrica supplemental appendix); Broner, Martin, Meyer and Trebesch (Kiel WP 2292); Alekseev and Lin (author PDF); Eastman Kodak v. Image Technical Services (United States Reports, Library of Congress PDF).
- Publisher or author pages: NBER abstract pages (w17409, w31852, w33681, w34108), the Econometric Society article page for ECTA23206, EconStor, Cambridge Core (Carson, Metz and Poast; Danilovic review of Crawford), and Matteo Camboni's research page.
- One citation-graph pass (OpenAlex works citing Clayton, Maggiori and Schreger's Econometrica paper, 2025 onward) to look for recent close models. A second pass on Bueno de Mesquita and Smith returned no data.

Because no keyword search was possible, the novelty claim remains conditional on the discovery queries listed under Open questions. The Becko, Grossman and Helpman PDF is behind an NBER login, so details of their model beyond the abstract were not re-verified.

Status counts for the 43 citations returned: 35 verified, 6 corrected (Harstad 2016, the Clayton-Maggiori-Schreger Framework appendix location, Crawford 2003, Carson-Metz-Poast byline, Slantchev 2011 subtitle, Benson and Smith 2023), 0 mischaracterized, 2 unverifiable (Becko and O'Connor 2025; Borenstein, MacKie-Mason and Netz 1995 page range).

## Corrected synthesis

The novelty claim survives in a narrower form than the introduction states. Two results that the paper presents as its own have close precedents that a referee will name. One point the memo missed: `03_literature.tex` (line 21) already cites Bueno de Mesquita and Smith (2016), Groseclose and Snyder (1996) and Bernheim and Whinston (1986), and says that "the winning bidder pays roughly the loser's valuation." The problem is not that these works are missing. The introduction (`01_intro.tex`, line 7) omits them while claiming novelty for a rival "who would pay for access", and the literature section describes Bueno de Mesquita and Smith too vaguely ("the client's price depends on the competition between them").

**The pricing result in Proposition 1 is not new.** A contested client that earns what the losing bidder would pay, with the winner's own stake dropping out, is the one-voter case of Groseclose and Snyder (1996). Their abstract states the structure: vote buyers move sequentially and the loser gets a last chance to attack. Bernheim and Whinston's (1986) menu auctions imply the same result for simultaneous offers. The result is also already in International Studies Quarterly. In Bueno de Mesquita and Smith (2016), leaders of donor nations "simultaneously offer" aid-for-policy deals. In Proposition 2 the target is indifferent between the competing offers (equation 6), one donor is "exhausted," and "the successful bidder pays no more than is absolutely necessary to exhaust their rival" (author PDF, p. 6). They also test the comparative static that our China corollary implies. The United States "paid less ... and gained more in policy terms through aid before the Soviet Union became a significant aid player," and paid more and got less afterwards (abstract). Since their offers are simultaneous, their equilibrium corresponds to our protocol (b), not our sequential baseline. The paper already says that V dropping out "is not a discovery about chokepoints" (`04_model.tex`, line 85). It should also say whose result this is.

**The claim that the patron's dependence returns when the holder can commit is the central lesson of Jehiel, Moldovanu and Stacchetti (1996).** When buyers who do not get an object suffer identity-dependent externalities, "outside options and participation constraints are endogenous; the seller extracts surplus also from agents who do not obtain the auctioned object; and the seller is better-off by not selling at all ... if externalities are much larger than valuations" (AER abstract). Our protocol (d) is a binary-action instance of this, and our necessary-condition corollary is its no-commitment converse.

Harstad (2016) gives a dynamic version of our threshold. In the published abstract, "the seller prefers to conserve if the buyer is expected to buy, but the buyer is unwilling to pay as long as the seller conserves." In the working paper, "there is only one Markov-perfect equilibrium in pure strategies: B never buys; S always cuts." Other equilibria are in mixed strategies with cutting at a positive rate, and cutting increases with the number of interested buyers. The memo garbled one detail. The published condition is that a leasing market dominates a sales market "if and only if the consumption value and the buyer's protection cost are large." The memo's wording ("conservation value low relative to consumption value") comes from the 2011 working paper abstract, not the journal version. This buy-or-lease comparison remains the closest formal analogue we found to the US choice between paying rents and demanding the holding company. Harstad's line "conservation abroad is leased, while domestic conservation is bought" gives a sharp prediction: a patron should demand ownership of a foreign asset only when protecting that ownership remotely is cheap.

**The geoeconomics framework already owns the language of slack.** The NBER Macroeconomics Annual paper by Clayton, Maggiori and Schreger states: "Threats generate power to the extent that they generate slack in the participation constraint" (WP 33681, p. 2). Our effective bite, min{alpha, [-Q]^+}, is that slack. If v2 is organized around a "slack principle," the principle must be credited to them. What they leave open is what we supply. They write "We leave credibility and coalition building to fuller treatments in the literature," and they list "models of multiple hegemons and endogenous emergence of hegemons" as an open theory question.

The memo's one open point on this work is now settled. The two-hegemon competition result survives in the published Econometrica supplemental appendix, Section B.2 ("Hegemonic competition for dominance"), Proposition 5. In the June 2024 NBER revision it was Online Appendix B.1. With fully overlapping threats the two hegemons "bid each other down to zero transfers," which the authors liken to the Bertrand paradox. For a firm domestic to one hegemon, "the joint threats that the firm's own hegemon can provide become that firm's outside option, to which that firm is held by the other hegemon." This is a cousin of Proposition 1 with transfers running the other way.

The memo's contrast on credibility needs care. In the Framework paper, threats are grim-trigger strategies in a repeated game, and equilibria are subgame perfect and Markov. Because equilibria are Markov, "the hegemon offers a contract only for the current [period] (cannot commit to future contracts)." Credibility there is therefore built into a repeated-game equilibrium; it is not assumed away. Our difference is that each linked threat (security conditionality, AI denial, firm penalties, rival coercion) must be sequentially rational in a one-shot game against a holder that the patron needs.

**What remains new is the combination, and it is defensible.** No formal model we found puts all of these in one game: a client that holds an input its patron needs, depends on that patron for security, can sell the input to the patron's rival, and faces linked threats that must each be sequentially rational. Each close model lacks at least one element.

- *Bueno de Mesquita and Smith* have rival bidders but only carrots. There is no security dependence and no asset the winner needs.
- *Wolford and Kim (2017, PSRM 5(4))* have the inverse. A small ally that is politically valuable to a larger one protects its market unpunished, because "their allies' threats of retaliation are incredible." There is no rival bidder. Their mechanism is how V enters our exit premium, through the credibility of firm-level penalties (chi_f), and they belong where chi_f is introduced.
- *Fang, Johnson and Leeds (2014)* show in a three-player crisis-bargaining model that "when a target values an alliance highly, an ally's recommendation for settlement can encourage the target to concede." They do not separate dependence from conditionality, which is where our determinants corollary adds something.
- *Crawford (2003)*: in Danilovic's review, pivotal deterrence requires that the two adversaries see each other as more threatening than the pivot, that the pivot be "at least equal in power to them" and prefer the status quo, and that it believe both adversaries are revisionist. Europe fails the power condition outright. Its security dependence on one side also undermines the credibility of aligning with the other, which the definition of a pivot presupposes. Crawford's pivot restrains a war between two adversaries rather than pricing an asset, so the comparison is an analogy, not a precedent.
- *Becko, Grossman and Helpman (2025)* and *Broner, Martin, Meyer and Trebesch (2025)* model alignment among many small countries. In Broner et al., countries lie on a circle and coordinate on a sunspot. Their hegemon "can ... commit to cut its trade link with any country" that does not align, threats are non-discriminatory (footnote 10), and coercion is used only by a hegemon that is "neither too small ... nor too large." These are the assumptions Lemma 1 is built to avoid: committed threats and no pivotal holder. Becko, Grossman and Helpman's abstract confirms unipolar and bipolar settings, PTAs as carrots, and optimal tariffs above Mill-Bickerdike. The memo's further details (a continuum of small countries with alignment-cost draws, simultaneous Nash tariff setting) come from an earlier reading and could not be re-checked because the PDF is gated.

One recent formal paper turned up in the citation-graph pass. Woods (2026, Chinese Political Science Review, online 25 March 2026) models economic coercion as "a conditional restriction on the set of feasible inputs," with power driven by low substitutability rather than trade volume. It is a sender-target model with no ally, no rival bidder and no control stage. It supports our treatment of denial as bite that depends on substitutes, and it does not threaten the novelty claim.

**On preventive control, the novelty is in timing and coercion, not in the idea of buying control.** Klein, Crawford and Alchian (1978), Grossman and Hart (1986) and Hart and Moore (1990) make integration the remedy for hold-up. Lake (1996) defines the continuum from alliance to empire by "the parties' rights of residual control" and explains the choice through expected costs of opportunism. Frieden (1994) links colonial control to investments "whose rents were particularly easy to seize or protect, and whose protection did not require multilateral action." Cooley and Spruyt (2009) treat sovereignty transfers as incomplete contracts that are "intentionally ambiguous and subject to future renegotiation." Benson and Smith (2023) show that allies can offset an alliance-induced power shift with concessions or slower implementation. When such bargains fail, preventive incentives arise, but "the conditions that make it most attractive also make it unlikely to be carried out." None of these works times a patron's demand for control to a window in which its threats still bite, before a rival raises the holder's outside option. None lets the rival's punishment of the transfer protect the holder. That combination of Fearon (1996) and Grossman and Hart appears to be ours, subject to the keyword searches still owed.

**Servicing has a formal home the paper ignores.** Coase (1972) and Bulow (1982) explain why tools that have been sold are a wasting lever. Bulow's abstract states that renting, or making binding promises about future production, ameliorates the durable-goods monopolist's problem. Morita and Waldman (2004) show that monopolizing maintenance, "similar to leasing," "reduces or even eliminates problems due to time inconsistency," first in a Bulow-type setting. Borenstein, MacKie-Mason and Netz (2000) show that aftermarket prices exceed marginal cost "despite competition in the equipment market," because firms weigh future buyers against "current, locked-in equipment owners." Carlton and Waldman (2010) caution that aftermarket monopolization is often efficiency-enhancing. In Kodak (1992), evidence that Kodak controlled "nearly 100% of the parts market and 80% to 95% of the service market" sufficed to survive summary judgment on monopoly power. The Court found it plausible that "locked-in customers, high information costs, and discriminatory pricing" let Kodak profit from aftermarket power. Together these works justify treating servicing as a renewable flow lever. They also show that a US stockpile of maintenance know-how is an attempt to turn a flow dependence into a stock, which our buffer t_U measures.

## Verified facts table

| # | Claim (corrected where needed) | Verdict | Source URL | Source date | Note |
|---|---|---|---|---|---|
| 1 | Bueno de Mesquita and Smith (2016): donor leaders "simultaneously offer" aid-for-policy deals. In Proposition 2 the target is indifferent between the rival offers (eq. 6), one donor is "exhausted," and "the successful bidder pays no more than is absolutely necessary to exhaust their rival." A dominant single donor "captures all the surplus." The US paid more and got less after the USSR entered. | verified | https://wp.nyu.edu/alastairsmith/wp-content/uploads/sites/4178/2016/06/Competition-and-Collaboration-in-Aid-for-Policy-Deals.pdf | 2016-04-12 (ISQ advance access) | Full text read. Offers are simultaneous, so the analogue is our protocol (b). |
| 2 | Clayton, Maggiori and Schreger: the two-hegemon Bertrand result ("bid each other down to zero transfers"; the own hegemon's threats become the firm's outside option) is in the published Econometrica Supplemental Appendix, Section B.2, Proposition 5. In NBER WP 31852 (Nov 2023, revised June 2024) it is Online Appendix B.1. | corrected | https://www.econometricsociety.org/publications/econometrica/2026/01/01/A-Framework-for-Geoeconomics/supp/23206SUPP.pdf | 2026-01 | Resolves the memo's open question. Cite the published supplement, Section B.2, not "Appendix B.1." |
| 3 | CMS Framework: equilibria are subgame perfect and Markov, and the hegemon "cannot commit to future contracts." Threats are grim-trigger strategies in a repeated game. The hegemon makes take-it-or-leave-it offers. | verified | https://www.nber.org/papers/w31852 | 2024-06 (revision) | Text of WP 31852, lines on Markov equilibria and the TIOLI contract. |
| 4 | CMS, "Putting Economics Back Into Geoeconomics": "Threats generate power to the extent that they generate slack in the participation constraint." "We leave credibility and coalition building to fuller treatments in the literature." Multiple hegemons are listed as open. ASML is the example of a US threat to withhold tools from China, effective only if China lacks close substitutes. NBER Macroeconomics Annual 2025, vol. 40, pp. 23-87 (issued 2026), doi 10.1086/738941; WP 33681, April 2025. | verified | https://www.nber.org/papers/w33681 | 2025-04 | Quotes found in WP text, pp. 2 and in Section 2. |
| 5 | CMS, "A Framework for Geoeconomics," Econometrica 94(1):105-136 (January 2026), doi 10.3982/ECTA23206. CMS, "A Theory of Economic Coercion and Fragmentation," JPE, online 15 October 2026, doi 10.1086/744505, with no volume or pages yet. | verified | https://api.crossref.org/works/10.1086/744505 | 2026-10-15 | The JPE paper is already in `notes/v2/bib_theory.bib` as `clayton2026theory`. |
| 6 | Broner, Martin, Meyer and Trebesch, "Hegemonic Globalization," Kiel Working Paper No. 2292, June 2025. Countries sit on a circle and coordinate on a sunspot. In the coercion extension the largest hegemon "can ... commit to cut its trade link" with non-aligned countries and their partners. Threats are non-discriminatory. Coercion is used only by a hegemon "neither too small ... nor too large." A rising hegemon "eventually deviates regardless of the incumbent's threats" if preferences differ enough. The paper also has an empirical part: a Global Treaties Database of 77,000 agreements (1800-2020). | verified | https://hdl.handle.net/10419/320425 | 2025-06 | The memo omitted the empirical half. SSRN doi 10.2139/ssrn.5324403 is confirmed in Crossref. |
| 7 | "Hegemony and International Alignment," AEA Papers and Proceedings 115:593-598 (May 2025), doi 10.1257/pandp.20251041, has five authors: Broner, Martin, Meyer, Trebesch and Jiaxian Zhou Wu. | verified | https://api.crossref.org/works/10.1257/pandp.20251041 | 2025-05-01 | |
| 8 | Becko, Grossman and Helpman, NBER WP 34108 (August 2025). Unipolar case: the hegemon uses PTAs to attract partners. Bipolar case: two great powers compete. Optimal tariffs exceed Mill-Bickerdike when geopolitics matters, and rival tariffs may be strategic complements or substitutes. Calibration uses UN voting, an estimate of the cost of buying UN votes, and military spending. | verified | https://www.nber.org/papers/w34108 | 2025-08 | Abstract verified. JEL codes, the continuum of small countries and simultaneous Nash tariffs come from an earlier reading; the gated PDF was not re-checked. |
| 9 | Wolford and Kim, PSRM 5(4):587-611, October 2017; first online 19 June 2015. Small, politically valuable allies engage in "socially suboptimal protectionism, as their allies' threats of retaliation are incredible." Antidumping data cover 1980-2013. | verified | https://doi.org/10.1017/psrm.2015.19 | 2017-10 | Abstract via Crossref; full text not read. |
| 10 | Thoenig, "Trade in the shadow of war: A quantitative toolkit for geoeconomics," Handbook of the Economics of Conflict (Elsevier, ISBN 9780323988919), pp. 325-380, doi 10.1016/bs.hoec.2024.10.003. | verified | https://api.crossref.org/works/10.1016/bs.hoec.2024.10.003 | 2024 | The memo's claim that BGH's reference list gives "Trade Policy in the Shadow of War" could not be re-checked (gated PDF). |
| 11 | Alekseev and Lin, "Export policy for dual-use goods," draft of 3 February 2026, first circulated 1 November 2025 as "Trade policy in the shadow of conflict: The case of dual-use goods." With unilateral policy, China's export policy is more impactful than the US's (2.1% vs 1.7% military advantage). Under coalition export enforcement, the US impact becomes three times larger than China's. Reshipping through third countries cuts the effects by more than half, and stockpile depletion doubles the impact of trade policy. | verified | https://www.maximalekseev.com/files/trade_dualuse.pdf | 2026-02-03 | The unilateral-baseline finding was missing from the memo. The claim that BGH cite it as a 2025 mimeo was not re-checked. |
| 12 | Eastman Kodak Co. v. Image Technical Services, 504 U.S. 451: argued 10 December 1991, decided 8 June 1992. Blackmun wrote for the Court, joined by Rehnquist, White, Stevens, Kennedy and Souter; Scalia dissented, joined by O'Connor and Thomas. The evidence that Kodak controlled "nearly 100% of the parts market and 80% to 95% of the service market" sufficed to survive summary judgment on monopoly power. Lock-in, information costs and discriminatory pricing made the inference of aftermarket power plausible. | verified | https://tile.loc.gov/storage-services/service/ll/usrep/usrep504/usrep504451/usrep504451.pdf | 1992-06-08 | Syllabus read. |
| 13 | Crawford (2003), Pivotal Deterrence, Cornell University Press, Ithaca, NY, 304 pp. In the review, the necessary conditions are: the adversaries see each other as more threatening than the pivot; the pivot is at least equal in power to them, prefers the status quo, and believes both adversaries are revisionist and willing to go to war if assured of its support. | corrected | https://doi.org/10.1017/S1537592704770589 | 2004-12 (review) | The "believes" qualifier was dropped in the memo. "Ability to align with either" is implied by the definition, not listed as a condition. The DOI is the review's, not the book's; the book has no DOI. |
| 14 | Kim (2016), The Supply Side of Security, Stanford University Press. Chapter 2, "A Market Theory of Alliances," pp. 28-48, doi 10.11126/stanford/9780804796965.003.0002. Allies exchange diverse goods, with gains from comparative advantage, economies of scale, and informational and institutional effects. | verified | https://doi.org/10.11126/stanford/9780804796965.003.0002 | 2016-04-13 | The De Gruyter e-edition doi 10.1515/9780804798594 has a 2020 Crossref date. |
| 15 | Cooley and Spruyt (2009), Contracting States: Sovereign Transfers in International Relations, Princeton University Press, doi 10.1515/9781400830657. The book uses incomplete contracts, "intentionally ambiguous and subject to future renegotiation," and covers decolonization, US overseas basing and integration. | verified | https://doi.org/10.1515/9781400830657 | 2009-04-20 | |
| 16 | Slantchev (2011), Military Threats: The Costs of Coercion and the Price of Peace, Cambridge University Press, doi 10.1017/CBO9780511778940. The Crossref record includes the subtitle. | corrected | https://api.crossref.org/works/10.1017/CBO9780511778940 | 2011-02-03 | The memo wrongly said that Crossref lists the main title only. |
| 17 | Harstad, JET 166:124-151 (November 2016; online 3 August 2016). The published abstract says leasing dominates sales "if and only if the consumption value and the buyer's protection cost are large." "Conservation abroad is leased, while domestic conservation is bought." The WP (NBER 17409, Sept 2011) says "only one Markov-perfect equilibrium in pure strategies: B never buys; S always cuts"; mixed equilibria involve cutting at a positive rate, and cutting rises with the number of buyers. | corrected | https://doi.org/10.1016/j.jet.2016.07.003 | 2016-11 | The lease-versus-sale condition is now quoted from the journal version. The pure-strategy statement was verified in the WP text only. |
| 18 | Camboni and Porcellacchia, "Spheres of Influence" (draft July 2025; SSRN doi 10.2139/ssrn.5269194). Countries design foreign policies to manage coercion risk from two great powers. As the world becomes less unipolar, countries deepen alignments, and China's growth may lead countries in the US sphere to offer the US greater concessions. | verified | https://sites.google.com/view/matteocamboni | 2025-07 | The author page says "New draft coming soon." |
| 19 | Carson, Metz and Poast, "Allies and Access," IO 79(S1):S103-S116, online 20 November 2025. The byline is "Rachel Metz" (OpenAlex display name Rachel Tecott Metz). The paper argues that "ally-enabled access" is an overlooked benefit of US alliances. | corrected | https://doi.org/10.1017/S0020818325100982 | 2025-11-20 | Cite as Metz, Rachel, as published; this matches `notes/v2/bib_security.bib`. |
| 20 | Willis and Preble, FPA 22(3), article orag008. Online 25 March 2026 (OpenAlex). Covers 1990-2018. Larger and longer US deployments reduce the probability and the volume of sanctions-busting trade among defense-pact partners. The effect dissipates after deployments of 40 years. | verified | https://doi.org/10.1093/fpa/orag008 | 2026-03-25 | Crossref lists the issue date as May 2026. |
| 21 | Yang, JCR 70(7-8):1152-1182 (online 7 February 2026). A major power offers economic aid to a rival's protege when relations between the protege and its patron deteriorate rapidly. Directed dyad-years, 1960-2010. | verified | https://doi.org/10.1177/00220027261417327 | 2026-02-07 | |
| 22 | Izumikawa, JEI 47(6):987-1002, concludes that neither the US nor China ("none of them") seems to have adopted a comprehensive strategy toward Europe. The special-issue introduction is by Simón and Fiott, JEI 47(6):785-803. | verified | https://doi.org/10.1080/07036337.2025.2537362 | 2025-08-18 | Abstract via OpenAlex. Spell Simón with the accent. |
| 23 | Borenstein, MacKie-Mason and Netz, JEMS 9(2):157-188 (June 2000): aftermarket price exceeds marginal cost "despite competition in the equipment market." The result holds under Bertrand, differentiated duopoly and monopoly. The abstract cites "over 20 recent antitrust cases." | verified | https://doi.org/10.1111/j.1430-9134.2000.00157.x | 2000-06 | |
| 24 | Morita and Waldman, JEMS 13(2):273-302 (June 2004): maintenance monopolization, "similar to leasing," reduces or eliminates time inconsistency. The result is shown first in a Bulow (1982)-type setting. | verified | https://ideas.repec.org/a/bla/jemstr/v13y2004i2p273-302.html | 2004-06 | |
| 25 | Jehiel, Moldovanu and Stacchetti, AER 86(4):814-829 (September 1996). With identity-dependent externalities, participation constraints are endogenous, the seller extracts surplus from non-acquirers, and it may do better by not selling. | verified | https://ideas.repec.org/a/aea/aecrev/v86y1996i4p814-29.html | 1996-09 | No DOI in Crossref. |
| 26 | Bulow (1982) and Coase (1972) are not in `paper/refs.bib`. Bulow: JPE 90(2):314-332, doi 10.1086/261058. Coase: JLE 15(1):143-149, doi 10.1086/466731. | verified | https://api.crossref.org/works/10.1086/261058 | 2026-10-29 (grep of refs.bib) | |
| 27 | Bueno de Mesquita and Smith, Groseclose and Snyder, and Bernheim and Whinston are already cited in `paper/sections/03_literature.tex` (line 21). The introduction (`01_intro.tex`, line 7) does not cite any of them. | verified | file:///home/user/ASML-leverage/paper/sections/03_literature.tex | 2026-10-29 | The memo implied that the bidding literature was absent; it is absent only from the intro. |
| 28 | Woods, "The Price is Not Right: Economic Power as Control Over Feasibility in International Political Economy," Chinese Political Science Review, online 25 March 2026, doi 10.1007/s41111-026-00341-6. It is a formal model of coercion as a conditional restriction on feasible inputs. | verified | https://doi.org/10.1007/s41111-026-00341-6 | 2026-03-25 | New find from the citation-graph pass. No volume or pages yet. Sender-target only. |
| 29 | Becko and O'Connor (2025), "Strategic (Dis)Integration" (Princeton mimeo), is said to be cited by BGH. | unverifiable | https://www.nber.org/papers/w34108 | n/a | No Crossref record, the BGH PDF is gated, and no web search was available. |

## Modeling implications

1. **Rewrite the novelty sentence in `01_intro.tex`, line 7.** Replace "None of these considers a dependent ally that holds a chokepoint its patron needs, in a race in which a rival great power would pay for access." with: "Formal models have priced a client's alignment when rival powers bid for it \citep{groseclose1996buying, bueno2016competition}, shown that a patron's threats against a valuable ally can lack credibility \citep{wolford2017alliances}, and located a hegemon's power in the slack its threats create in a target's participation constraint \citep{clayton2026framework, clayton2026putting}. To our knowledge, none combines these elements: a client that depends on its patron for security, holds an input the patron needs, and could sell that input to the patron's rival, with every linked threat required to be sequentially rational."

2. **Tighten `03_literature.tex`, line 21.** Replace "the client's price depends on the competition between them" with a statement of the result: with rival donors making simultaneous offers, the target is held to indifference and the winner pays only what it takes to exhaust its rival. Replace "roughly the loser's valuation" with "the loser's willingness to pay, net of the client's own preference."

3. **After Proposition 1 (`04_model.tex`, around line 83).** Say that the pricing logic is Bueno de Mesquita and Smith's (2016) Proposition 2 under a sequential protocol, and the one-voter case of Groseclose and Snyder (1996). Their simultaneous-offer "exhaustion" equilibrium corresponds to the lower bound [Q]^+ of our protocol (b). Chen and Zapal (2022, JET 205:105529) generalize sequential vote buying and can serve as the robustness reference.

4. **Protocol proposition, case (d).** Present it as the binary-action version of Jehiel, Moldovanu and Stacchetti (1996): a holder that can commit to sell to the patron's worst rival extracts the patron's externality V. The necessary-condition corollary is then the no-commitment converse. This turns a likely referee objection into positioning. Jehiel and Moldovanu (1995) show that negative externalities can cause delay, a formal relative of the time-to-pain proposition.

5. **Slack principle.** If v2 is organized around slack, credit Clayton, Maggiori and Schreger. Use the Macroeconomics Annual quotation for the principle, and the Econometrica supplement, Section B.2, Proposition 5, for two-hegemon Bertrand competition. State our distinct contributions in their own terms. Credibility comes from one-shot sequential rationality of each linked instrument, where their enforcement comes from repeated-game trigger strategies. A second great power bids and coerces, a case they list as open.

6. **Lemma 1(iii) and determinants corollary, part (c).** Cite Wolford and Kim (2017) where chi_f is introduced as the formal precedent for "a patron's need for an ally makes its retaliation incredible." Our model confines that channel to firm-level penalties, because cheap jurisdiction over China-bound flows (theta) remains credible for any V.

7. **Control-rights section: use Harstad's published condition.** Leasing dominates buying iff the holder's consumption value (here, the value of selling to China) and the buyer's remote protection cost are large. Two implications follow.
   - The US should prefer paying rents or tier status (leasing) unless it can protect ownership of a Dutch asset cheaply, for example through FDPR jurisdiction or a controlling vote that Dutch law cannot easily undo. This gives the windows corollary a testable comparative static: the control demand is likelier when the US's post-transfer protection cost is low and the Dutch sovereignty cost sigma is low.
   - Add a post-transfer re-nationalization or renegotiation hazard (Cooley and Spruyt 2009). This lowers the value of control and should shrink the US window.

8. **Servicing extension.** Model ASML output as a stock K of installed tools plus a per-period servicing flow s_t in {0,1}.
   - Tool sales are a Coase-Bulow stock lever that decays, and Europe cannot commit not to dilute it.
   - Monopoly maintenance works like leasing (Morita and Waldman 2004) and is renewable.
   - Calibrate c_U as the installed base's per-period utilization loss without vendor service (Borenstein, MacKie-Mason and Netz 2000; Kodak 1992). Treat t_U as the installed base's self-maintenance horizon. US acquisition of know-how, the analogue of Kodak's independent service organizations, lengthens it.
   - Note Carlton and Waldman (2010): servicing control can be efficient in peacetime. The welfare cost appears only when service is withheld.

9. **Theta and China's leverage.** Alekseev and Lin (2026) find that, acting alone, China's export policy has more bite than the US's. Under coalition enforcement the US impact becomes three times China's, and reshipping halves the effects.
   - This supports making theta depend on allied enforcement, and therefore on Europe's alignment.
   - It also supports the model's assumption that China's coercive instruments (rare earths, legacy chips) are credible when used unilaterally.

10. **Benchmarks in the literature section.** Position Becko, Grossman and Helpman (2025) and Broner et al. (2025) as many-small-country alignment benchmarks with committed instruments. Broner et al.'s footnote 10 (non-discriminatory threats) and their "commit to cut" assumption make the contrast with Lemma 1 explicit. One sentence is enough.

11. **Holder, not pivot.** Use Crawford (2003) after the determinants corollary. Pivotal leverage requires the pivot to be at least equal in power to the adversaries and able to throw its weight either way. In our notation that means kappa near zero and Q > 0, which Europe does not satisfy.

12. **Empirical hooks for Section 7.** Willis and Preble (2026) support the kappa > 0 channel: US troop presence reduces sanctions busting among defense-pact partners. Yang (2026) supports the timing of China's bids: rivals offer aid when patron-protege relations sour. Izumikawa (2025) supports the claim that the gap is formal, not topical.

13. **Benson and Smith (2023).** If cited for preventive incentives, include their finding that the conditions making preventive war most attractive also make it unlikely to be carried out. The analogue is that a US control ultimatum is most attractive exactly when executing the stick is most costly, which fits our audience-cost requirement for the stick's credibility.

## Open questions

- **Keyword discovery searches are still owed** before the novelty claim can be called verified. No web search was possible in this check or in the original memo. Queries to run: "alignment auction", "bidding for allies", "competition for clients formal model", "chokepoint bargaining model", "export controls allies game theory", "extraterritorial sanctions coalition model", "preventive acquisition control rights", "patron client rival great power auction", and "servicing hold-up export controls".
- **Becko and O'Connor (2025), "Strategic (Dis)Integration."** It is still unretrieved and could be close to our baseline (a hegemon using trade threats as carrot and stick toward one partner). Check whether the partner holds an input the hegemon needs and whether a rival bids.
- **Wolford and Kim (2017) and Fang, Johnson and Leeds (2014)** were checked from abstracts only. Check in the full texts (i) whether the patron's threats are derived as sequentially rational and (ii) whether either model has a third-party bidder.
- **Harstad (2016).** The "only pure-strategy MPE: B never buys, S always cuts" statement was verified in NBER WP 17409 only. Confirm that it survives in the JET version before quoting it.
- **Becko, Grossman and Helpman (2025).** Details beyond the abstract (continuum of small countries, cost distribution, simultaneous Nash tariffs, JEL codes) and their reference-list entries for Thoenig and for Alekseev and Lin were not re-checked because the PDF is gated.
- **Characterizations not read in full text:** Shapiro and Teece (1994); Farrell and Klemperer (2007), whose volume editors (Armstrong and Porter) come from knowledge and are not in Crossref; and Bernheim and Whinston's binary-action "loser sets the price" reading, which is standard but was not re-derived from the text. Borenstein, MacKie-Mason and Netz (1995, Antitrust Law Journal 63:455) has its start page only.
- **Harstad's buyer count.** Does his result that cutting rises with the number of buyers carry over? With several conservation-minded co-funders (US, Japan, Korea), would exit become more likely, giving a formal reason why Japan and Korea decline to coordinate in the scenario?
- **Fearon (1996)** is unpublished and cited from the project bibliography. Re-read it to confirm that it has no third party whose offer drives the power shift, since the preventive-control novelty claim depends on that.

## BibTeX (verified or corrected entries)

Keys already in `paper/refs.bib`: `bueno2016competition`, `groseclose1996buying`, `bernheim1986menu`, `clayton2026framework`, `grossman1986costs`, `fearon1996bargaining`. Keys already in `notes/v2/*.bib`: `fang2014concede`, `clayton2026theory`, `carson2025allies`, `cooley2009contracting`. Those are repeated below only where this check confirmed or corrected them; check for duplicates before merging.

```bibtex
% ---- Client auctions, vote buying, externalities ----
@article{bueno2016competition,
  author  = {Bueno de Mesquita, Bruce and Smith, Alastair},
  year    = {2016},
  title   = {Competition and Collaboration in Aid-for-Policy Deals},
  journal = {International Studies Quarterly},
  volume  = {60},
  number  = {3},
  pages   = {413--426},
  doi     = {10.1093/isq/sqw011}
}

@article{groseclose1996buying,
  author  = {Groseclose, Tim and Snyder, Jr., James M.},
  year    = {1996},
  title   = {Buying Supermajorities},
  journal = {American Political Science Review},
  volume  = {90},
  number  = {2},
  pages   = {303--315},
  doi     = {10.2307/2082886}
}

@article{chen2022sequential,
  author  = {Chen, Ying and Z{\'a}pal, Jan},
  year    = {2022},
  title   = {Sequential Vote Buying},
  journal = {Journal of Economic Theory},
  volume  = {205},
  pages   = {105529},
  doi     = {10.1016/j.jet.2022.105529}
}

@article{bernheim1986menu,
  author  = {Bernheim, B. Douglas and Whinston, Michael D.},
  year    = {1986},
  title   = {Menu Auctions, Resource Allocation, and Economic Influence},
  journal = {Quarterly Journal of Economics},
  volume  = {101},
  number  = {1},
  pages   = {1--31},
  doi     = {10.2307/1884639}
}

@article{jehiel1996how,
  author  = {Jehiel, Philippe and Moldovanu, Benny and Stacchetti, Ennio},
  year    = {1996},
  title   = {How (Not) to Sell Nuclear Weapons},
  journal = {American Economic Review},
  volume  = {86},
  number  = {4},
  pages   = {814--829},
  note    = {No DOI registered. \url{https://ideas.repec.org/a/aea/aecrev/v86y1996i4p814-29.html}}
}

@article{jehiel1995negative,
  author  = {Jehiel, Philippe and Moldovanu, Benny},
  year    = {1995},
  title   = {Negative Externalities May Cause Delay in Negotiation},
  journal = {Econometrica},
  volume  = {63},
  number  = {6},
  pages   = {1321--1335},
  doi     = {10.2307/2171772}
}

@article{harstad2016market,
  author  = {Harstad, B{\aa}rd},
  year    = {2016},
  title   = {The Market for Conservation and Other Hostages},
  journal = {Journal of Economic Theory},
  volume  = {166},
  pages   = {124--151},
  doi     = {10.1016/j.jet.2016.07.003},
  note    = {Earlier version: NBER Working Paper 17409 (2011), doi:10.3386/w17409}
}

% ---- Geoeconomics and hegemonic alignment ----
@article{clayton2026framework,
  author  = {Clayton, Christopher and Maggiori, Matteo and Schreger, Jesse},
  year    = {2026},
  title   = {A Framework for Geoeconomics},
  journal = {Econometrica},
  volume  = {94},
  number  = {1},
  pages   = {105--136},
  doi     = {10.3982/ECTA23206},
  note    = {Two-hegemon competition: Supplemental Appendix, Section B.2, Proposition 5}
}

@article{clayton2026putting,
  author  = {Clayton, Christopher and Maggiori, Matteo and Schreger, Jesse},
  year    = {2026},
  title   = {Putting Economics Back into Geoeconomics},
  journal = {NBER Macroeconomics Annual},
  volume  = {40},
  pages   = {23--87},
  doi     = {10.1086/738941},
  note    = {NBER Macroeconomics Annual 2025. Working paper version: NBER Working Paper 33681 (April 2025), doi:10.3386/w33681}
}

@techreport{becko2025optimal,
  author      = {Becko, John S. and Grossman, Gene M. and Helpman, Elhanan},
  year        = {2025},
  title       = {Optimal Tariffs with Geopolitical Alignment},
  institution = {National Bureau of Economic Research},
  type        = {NBER Working Paper},
  number      = {34108},
  doi         = {10.3386/w34108}
}

@techreport{broner2025hegemonic,
  author      = {Broner, Fernando and Martin, Alberto and Meyer, Josefin and Trebesch, Christoph},
  year        = {2025},
  title       = {Hegemonic Globalization},
  institution = {Kiel Institute for the World Economy},
  type        = {Kiel Working Paper},
  number      = {2292},
  note        = {June 2025. \url{https://hdl.handle.net/10419/320425}. Also SSRN, doi:10.2139/ssrn.5324403}
}

@article{broner2025hegemony,
  author  = {Broner, Fernando and Martin, Alberto and Meyer, Josefin and Trebesch, Christoph and Wu, Jiaxian Zhou},
  year    = {2025},
  title   = {Hegemony and International Alignment},
  journal = {AEA Papers and Proceedings},
  volume  = {115},
  pages   = {593--598},
  doi     = {10.1257/pandp.20251041}
}

@unpublished{camboni2025spheres,
  author = {Camboni, Matteo and Porcellacchia, Michael},
  year   = {2025},
  title  = {Spheres of Influence},
  note   = {Working paper, draft July 2025. SSRN, doi:10.2139/ssrn.5269194}
}

@article{woods2026price,
  author  = {Woods, Dwayne},
  year    = {2026},
  title   = {The Price is Not Right: Economic Power as Control Over Feasibility in International Political Economy},
  journal = {Chinese Political Science Review},
  doi     = {10.1007/s41111-026-00341-6},
  note    = {Published online 25 March 2026; volume and pages not yet assigned}
}

@incollection{thoenig2024trade,
  author    = {Thoenig, Mathias},
  year      = {2024},
  title     = {Trade in the Shadow of War: A Quantitative Toolkit for Geoeconomics},
  booktitle = {Handbook of the Economics of Conflict},
  publisher = {Elsevier},
  pages     = {325--380},
  doi       = {10.1016/bs.hoec.2024.10.003}
}

@unpublished{alekseev2026export,
  author = {Alekseev, Maxim and Lin, Xinyue},
  year   = {2026},
  title  = {Export Policy for Dual-Use Goods},
  note   = {Working paper, draft of 3 February 2026. First circulated 1 November 2025 as ``Trade Policy in the Shadow of Conflict: The Case of Dual-Use Goods.'' \url{https://www.maximalekseev.com/files/trade_dualuse.pdf}}
}

% ---- Alliances, trade and third parties ----
@article{wolford2017alliances,
  author  = {Wolford, Scott and Kim, Moonhawk},
  year    = {2017},
  title   = {Alliances and the High Politics of International Trade},
  journal = {Political Science Research and Methods},
  volume  = {5},
  number  = {4},
  pages   = {587--611},
  doi     = {10.1017/psrm.2015.19}
}

@article{fang2014concede,
  author  = {Fang, Songying and Johnson, Jesse C. and Leeds, Brett Ashley},
  year    = {2014},
  title   = {To Concede or to Resist? {The} Restraining Effect of Military Alliances},
  journal = {International Organization},
  volume  = {68},
  number  = {4},
  pages   = {775--809},
  doi     = {10.1017/S0020818314000137}
}

@book{crawford2003pivotal,
  author    = {Crawford, Timothy W.},
  year      = {2003},
  title     = {Pivotal Deterrence: Third-Party Statecraft and the Pursuit of Peace},
  publisher = {Cornell University Press},
  address   = {Ithaca, NY}
}

@book{kim2016supply,
  author    = {Kim, Tongfi},
  year      = {2016},
  title     = {The Supply Side of Security: A Market Theory of Military Alliances},
  publisher = {Stanford University Press},
  address   = {Stanford, CA},
  note      = {Chapter 2, ``A Market Theory of Alliances,'' pp. 28--48, doi:10.11126/stanford/9780804796965.003.0002}
}

@book{slantchev2011military,
  author    = {Slantchev, Branislav L.},
  year      = {2011},
  title     = {Military Threats: The Costs of Coercion and the Price of Peace},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  doi       = {10.1017/CBO9780511778940}
}

@article{carson2025allies,
  author  = {Carson, Austin and Metz, Rachel and Poast, Paul},
  year    = {2025},
  title   = {Allies and Access: Implications of an {American} Turn Away from Alliances},
  journal = {International Organization},
  volume  = {79},
  number  = {S1},
  pages   = {S103--S116},
  doi     = {10.1017/S0020818325100982}
}

@article{willis2026friends,
  author  = {Willis, Charmaine N. and Preble, Keith A.},
  year    = {2026},
  title   = {With Friends Like These: The Impact of {US} Troop Deployments on Economic Sanctions Busting},
  journal = {Foreign Policy Analysis},
  volume  = {22},
  number  = {3},
  pages   = {orag008},
  doi     = {10.1093/fpa/orag008}
}

@article{yang2026major,
  author  = {Yang, Hankyeul},
  year    = {2026},
  title   = {Major Power Rivalry and Wedge Strategy of Concessions},
  journal = {Journal of Conflict Resolution},
  volume  = {70},
  number  = {7--8},
  pages   = {1152--1182},
  doi     = {10.1177/00220027261417327}
}

@article{simon2025player,
  author  = {Sim{\'o}n, Luis and Fiott, Daniel},
  year    = {2025},
  title   = {Player and Playground: {Europe} in {US}--{China} Competition},
  journal = {Journal of European Integration},
  volume  = {47},
  number  = {6},
  pages   = {785--803},
  doi     = {10.1080/07036337.2025.2537372}
}

@article{izumikawa2025wedging,
  author  = {Izumikawa, Yasuhiro},
  year    = {2025},
  title   = {Wedging, Binding and {Europe} in the {US}-{China} Competition: Theoretical and Policy Implications},
  journal = {Journal of European Integration},
  volume  = {47},
  number  = {6},
  pages   = {987--1002},
  doi     = {10.1080/07036337.2025.2537362}
}

@article{benson2023commitment,
  author  = {Benson, Brett V. and Smith, Bradley C.},
  year    = {2023},
  title   = {Commitment Problems in Alliance Formation},
  journal = {American Journal of Political Science},
  volume  = {67},
  number  = {4},
  pages   = {1012--1025},
  doi     = {10.1111/ajps.12693}
}

@book{benson2025window,
  author    = {Benson, Brett V. and Smith, Bradley C.},
  year      = {2025},
  title     = {The Window Before: The Politics of Alliance Implementation},
  publisher = {Oxford University Press},
  address   = {New York, NY},
  doi       = {10.1093/9780197806760.001.0001}
}

% ---- Control rights ----
@article{lake1996anarchy,
  author  = {Lake, David A.},
  year    = {1996},
  title   = {Anarchy, Hierarchy, and the Variety of International Relations},
  journal = {International Organization},
  volume  = {50},
  number  = {1},
  pages   = {1--33},
  doi     = {10.1017/S002081830000165X}
}

@article{frieden1994international,
  author  = {Frieden, Jeffry A.},
  year    = {1994},
  title   = {International Investment and Colonial Control: A New Interpretation},
  journal = {International Organization},
  volume  = {48},
  number  = {4},
  pages   = {559--593},
  doi     = {10.1017/S0020818300028319}
}

@book{cooley2009contracting,
  author    = {Cooley, Alexander and Spruyt, Hendrik},
  year      = {2009},
  title     = {Contracting States: Sovereign Transfers in International Relations},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  doi       = {10.1515/9781400830657}
}

@article{klein1978vertical,
  author  = {Klein, Benjamin and Crawford, Robert G. and Alchian, Armen A.},
  year    = {1978},
  title   = {Vertical Integration, Appropriable Rents, and the Competitive Contracting Process},
  journal = {Journal of Law and Economics},
  volume  = {21},
  number  = {2},
  pages   = {297--326},
  doi     = {10.1086/466922}
}

@article{hart1990property,
  author  = {Hart, Oliver and Moore, John},
  year    = {1990},
  title   = {Property Rights and the Nature of the Firm},
  journal = {Journal of Political Economy},
  volume  = {98},
  number  = {6},
  pages   = {1119--1158},
  doi     = {10.1086/261729}
}

% ---- Durable goods and aftermarkets ----
@article{coase1972durability,
  author  = {Coase, R. H.},
  year    = {1972},
  title   = {Durability and Monopoly},
  journal = {Journal of Law and Economics},
  volume  = {15},
  number  = {1},
  pages   = {143--149},
  doi     = {10.1086/466731}
}

@article{bulow1982durable,
  author  = {Bulow, Jeremy I.},
  year    = {1982},
  title   = {Durable-Goods Monopolists},
  journal = {Journal of Political Economy},
  volume  = {90},
  number  = {2},
  pages   = {314--332},
  doi     = {10.1086/261058}
}

@article{morita2004durable,
  author  = {Morita, Hodaka and Waldman, Michael},
  year    = {2004},
  title   = {Durable Goods, Monopoly Maintenance, and Time Inconsistency},
  journal = {Journal of Economics and Management Strategy},
  volume  = {13},
  number  = {2},
  pages   = {273--302},
  doi     = {10.1111/j.1530-9134.2004.00011.x}
}

@article{borenstein2000exercising,
  author  = {Borenstein, Severin and MacKie-Mason, Jeffrey K. and Netz, Janet S.},
  year    = {2000},
  title   = {Exercising Market Power in Proprietary Aftermarkets},
  journal = {Journal of Economics and Management Strategy},
  volume  = {9},
  number  = {2},
  pages   = {157--188},
  doi     = {10.1111/j.1430-9134.2000.00157.x}
}

@article{carlton2010competition,
  author  = {Carlton, Dennis W. and Waldman, Michael},
  year    = {2010},
  title   = {Competition, Monopoly, and Aftermarkets},
  journal = {Journal of Law, Economics, and Organization},
  volume  = {26},
  number  = {1},
  pages   = {54--91},
  doi     = {10.1093/jleo/ewp006}
}

@article{shapiro1994systems,
  author  = {Shapiro, Carl and Teece, David J.},
  year    = {1994},
  title   = {Systems Competition and Aftermarkets: An Economic Analysis of {Kodak}},
  journal = {The Antitrust Bulletin},
  volume  = {39},
  number  = {1},
  pages   = {135--162},
  doi     = {10.1177/0003603X9403900104}
}

@incollection{farrell2007coordination,
  author    = {Farrell, Joseph and Klemperer, Paul},
  year      = {2007},
  title     = {Coordination and Lock-In: Competition with Switching Costs and Network Effects},
  booktitle = {Handbook of Industrial Organization},
  volume    = {3},
  chapter   = {31},
  publisher = {Elsevier},
  pages     = {1967--2072},
  doi       = {10.1016/S1573-448X(06)03031-7},
  note      = {Volume editors (Armstrong and Porter) not confirmed in Crossref}
}

@misc{kodak1992,
  author       = {{Supreme Court of the United States}},
  year         = {1992},
  title        = {Eastman Kodak Co. v. Image Technical Services, Inc.},
  howpublished = {504 U.S. 451},
  note         = {Argued December 10, 1991; decided June 8, 1992. \url{https://tile.loc.gov/storage-services/service/ll/usrep/usrep504/usrep504451/usrep504451.pdf}}
}
```
