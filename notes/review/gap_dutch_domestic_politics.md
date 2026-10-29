# Dutch domestic politics and state-firm relations, October 2025 to October 2026: the holder as a two-level actor (cabinet, parliament, ASML, the MATCH Act fight). Fact-checked gap memo (as of 29 October 2026)

Strand: gap_dutch_domestic_politics. Feeds the holder side of the model in notes/model_design_v2.md: the gatekeeper premium Q_NL and targeted benefit x_h (Remark G), the firm between jurisdictions (Remark F: y, f^F, p_C, p_B, zeta), the sovereignty cost sigma and enforceability Delta_c (Propositions 4 and 5), the self-binding versus dual-key remark, and the rupture hazard lambda (Proposition 1).

## How this was checked, and its limits

The session's web-search budget was exhausted before this check began (the first WebSearch call was refused), so no item below rests on a search-engine result. Every item was checked by retrieving the primary document directly:

- Tweede Kamer: the motion pages on tweedekamer.nl (text, co-signers, cabinet appraisal, vote by faction) for all 15 motions cited, and the open-data API (gegevensmagazijn.tweedekamer.nl) for vote dates (Zaak, Besluit, Agendapunt, Activiteit), faction seats (Fractie), document metadata, party membership of signatories (Persoon), and full-text documents (the Beethoven letter to ASML, the 2024 export-control report, the Rekenkamer reply, written questions 2026Z20701).
- officielebekendmakingen.nl: Kamerstukken 33009-141, 33009-159, 33009-166, 32637-717, 36696-2, 36696-3, 29826-281 and its annex (Semicon Visie 2035), 22054-459, 22054-484; Aanhangsel Handelingen 2023-2024 nr. 2044 and 2025-2026 nrs. 352, 1903, 2251 and 2526; Staatscourant 2025, 38653.
- The coalition agreement PDF (67 pages), searched page by page.
- govinfo: bill-status XML for H.R. 8170, S. 4281, H.R. 8800 and S. 4784; the texts of H.R. 8800 (EH) and S. 4784 (RS). The congress.gov API was rate-limited, so govinfo's bill-status files were used instead.
- lda.gov API: all 2025 and 2026 filings whose client name contains "ASML".
- SEC EDGAR: ASML's FY2025 20-F (filing index and full text) and the Q3 2026 6-K (14 October 2026).
- Pew Research Center topline PDF (23 June 2026) and the ECFR report PDF (June 2026).
- Crossref records retrieved by DOI (not by search) for all journal articles and three books; Open Library records retrieved by ISBN for Mastanduno (1992), Schelling (1960) and Culpepper (2010).
- Direct page fetches: NL Times (7 articles), Euronews, Bits&Chips, IO+, government.nl, wetten.overheid.nl, and Wikipedia (Jetten cabinet; 2025 Dutch general election; Nexperia).

What could not be checked: the Kiesraad certification of the 2025 election (the Kiesraad page did not link the 2025 report; seats were confirmed from the Tweede Kamer's own vote records of 9 December 2025 instead), the Pew fieldwork dates (not in the topline), the Evertiq CNY 8bn figure, Jetten's 25 September 2026 Bloomberg TV remark, the ASML CFO's remarks on MATCH after the Q3 2026 results, and whether the Beethoven export-control dialogue actually meets.

## Verdict in brief

The memo's sources are real and almost all quotations are exact. All 21 citations exist. The corrections that matter for the model are these.

1. **The "alternative majority" does not exist in the current House.** The memo's main alternative majority (VVD, PVV, JA21, Groep Markuszower, FvD, BBB) holds 67 of 150 seats. Adding SGP, 50PLUS and Keijzer gives 73. Every right-leaning majority needs CDA: VVD, CDA, PVV, JA21 and Markuszower hold 75, and with BBB 78. Inside that 78-seat bloc, the parties that voted for the Bamenga motion (VVD, CDA, JA21, BBB) hold 52 seats against 26 for those that opposed it (PVV, Markuszower). So the claim that a government change makes bilateral compliance more likely than Europeanised compliance is not supported. What the votes do support is narrower. Europeanised export control is robust to a change of government. EU coercive countermeasures against Washington are not: PVV, JA21, FvD, Markuszower and BBB all voted against the Piri motion on keeping countermeasures, including the Anti-Coercion Instrument, in reserve over Greenland.
2. **Notation mismatch on zeta.** In model_design_v2 (Remark F), zeta is the holder's cost of compelling ASML to *exit*, that is, to ship or service in China against US objection when the firm would rather comply with US measures. The memo uses zeta for the cost of compelling ASML to *cut* China servicing. That is a different object: a domestic political cost of a concession. On the 2026 evidence (lobbying against MATCH, 20-F risk factors), ASML would ship if licensed, so the compulsion branch of Remark F is inactive today. It becomes active only if MATCH or a new foreign direct product rule raises f^F.
3. **The Beethoven export-control dialogue is a promise, not an observed practice.** The annexed letter to ASML says a structural dialogue "zal worden opgezet" between General Affairs, Foreign Affairs, Economic Affairs "en andere relevante partijen en ASML", fortnightly, monthly and quarterly. No later document we read confirms that it meets. The memo's present tense ("It meets fortnightly") is unsupported. The EUR 2.51bn also funds the region and the sector (talent EUR 450m, infrastructure EUR 718m plus EUR 340m regional, housing EUR 425m), not ASML directly.
4. **Spare parts are inside the licensing scope, and the opacity claim is dated.** The current national regulation (in force since 25 November 2025) covers the listed equipment and its "speciaal ontworpen onderdelen en toebehoren", so spare-parts exports need a licence. Servicing labour is not mentioned. The "no reporting obligation" statement comes from the 2024 report (27 June 2025). It predates Staatscourant 2025, 38653, which moved all items of the supplementary national regulation, and part of the semiconductor regulation, into Annex I of Regulation 2021/821 from 15 November 2025. The statement now applies with certainty only to the residual national items (3B801.f.6 and f.7). Whether licences for the transferred items appear in the Dutch dual-use licence data is unverified.
5. **Lobbying was understated.** Besides ASML US's in-house spending (USD 600k, 600k and 500k in Q1 to Q3 2026) and Alpine Group (USD 70k a quarter), a second outside firm, OGR, was paid USD 70k a quarter and lists "H.R.8170/S.4281, MATCH" in its Q2 and Q3 2026 reports. Orrick is registered for ASML Netherlands B.V. but filed no-activity reports. ASML-funded federal lobbying in Q1 to Q3 2026 thus totals USD 2.12m. The Q1 in-house report, covering January to March, already names H.R. 8170, which was introduced on 2 April.
6. **MATCH is stalled in procedure, not in support.** New and verified: the Senate failed to invoke cloture on the motion to proceed to the Senate NDAA (S. 4784), 50 to 46, on 14 July 2026. H.R. 8170 has 31 cosponsors (21 Republican, 10 Democratic), the latest added on 1 October 2026. S. 4281 has 11 (5 Republican, 6 Democratic, including Schumer, Risch, Crapo, Cotton and Warren), the latest added on 14 September 2026. Neither NDAA text contains MATCH.
7. **"Firm and state agree" overreaches.** The documented agreement is on the extraterritorial form of MATCH and on opposing blanket bans. The cabinet also says it "deelt in algemene zin de veiligheidszorgen" of its partners and that "nationale veiligheidsoverwegingen zijn doorslaggevend". Jetten said Washington should "not only hear from ASML what is good or less good for ASML", which claims a state voice distinct from the firm's commercial interest. Licence decisions are confidential, so quiet divergence on substance cannot be ruled out. That is exactly what Culpepper's quiet-politics argument predicts.
8. **Smaller corrections.** JA21's second written-question set (Aanhangsel 2526) concerned US claims that an EUV tool reached China, not MATCH. The Piri motion's co-signers were from D66, CDA, 50PLUS, CU, PvdD and SP, and the caretaker cabinet advised against it. The Semicon Visie's "zorgvuldige weging" passage starts by saying national-security considerations are "leidend". In the Dekker motion, "stimuleren of zelfs afdwingen" is in the preamble, not in the request. The Van Houwelingen motion's 14 votes came from FvD and the Markuszower group. Boswijk is State Secretary (staatssecretaris) for Defence: the Tweede Kamer addresses him as such, while government.nl's English page styles him "Minister for". The coalition agreement's pledge to cut dependence for "essentiële wapensystemen" targets countries outside NATO (p. 32), not the United States. Culpepper (2015) defines structural power as "mutual dependencies between business and the state", not as anticipated exit. Culpepper's book is dated 2010 by Crossref and Open Library.

## Corrected synthesis

The Netherlands is not a unitary holder, but its internal divisions mostly do not run the way a referee would expect. Three findings matter for the model.

**First, on the MATCH Act the firm and the state oppose the same thing, and their channels are institutionalised.** After ASML's 2024 relocation signals, the Rutte IV caretaker cabinet launched Project Beethoven: EUR 2.51bn to 2030 from the state, region and business (EUR 1.73bn from the state), plus EUR 80.5m a year from 2031 (Kamerstuk 33009-141, 28 March 2024). The money goes to talent, infrastructure, housing and grid capacity in the Brainport region. In its letter to ASML, the cabinet stated its "hoop en verwachting" that ASML would keep its "statutaire, fiscale en werkelijke zetel" in the Netherlands, an expectation rather than a condition. Point 4 of the package promised a structural dialogue on export control between General Affairs, Foreign Affairs, Economic Affairs, other relevant parties and ASML: fortnightly at working level, monthly at senior civil-service level "om strategie voor te bereiden en inzet te bepalen", quarterly at political level "om strategie te bepalen". We found no public record that this dialogue meets as planned. Since early 2025 the Semicon Board NL has seated ASML's C-level alongside the ministers of Economic Affairs (chair), Education, Defence and Foreign Trade. Its Semicon Visie 2035, sent to parliament on 1 April 2026, says a strong position "biedt daarmee geopolitieke leverage". On export control it says national-security considerations are "leidend" while "een zorgvuldige weging" of effectiveness and economic impact takes place. The coalition agreement adopts the growth target of the Wennink report (written by ASML's former CEO, who retired on 24 April 2024) and names Project Beethoven as a model of mission-driven government (pp. 6, 30). It does not mention ASML or export control.

On MATCH, cabinet and company line up against the extraterritorial mechanism. The cabinet opposes it in written answers of 12 May and 15 June 2026: "Elk land is verantwoordelijk voor zijn eigen exportcontrolewetgeving." ASML US names H.R. 8170 in every 2026 lobbying report. With Alpine Group and OGR, ASML-funded federal lobbying reached USD 2.12m in the first three quarters of 2026. But the agreement is about form and breadth, not necessarily substance. The cabinet "deelt in algemene zin de veiligheidszorgen", calls its approach "chirurgisch" and case-by-case, and calls national security "doorslaggevend". Jetten told ANP that Washington should "not only hear from ASML what is good or less good for ASML". The record therefore fits a joint principal on delay and on resisting the bilateral, extraterritorial form. It cannot show whether the state and the firm diverge on individual licences, because those decisions are not published. Firm-state conflict over domestic inputs (talent, grid, tax, permits) was real and was settled with side payments to the region. ASML broke ground on its Brainport Industries Campus North expansion on 8 September 2026, with at least 3,000 jobs by 2029 and up to 20,000 in total. That is quiet politics (Culpepper) and mutual dependence (Culpepper 2015; Fairfield 2015) at work.

For the model, the firm's preference matters through Remark F. ASML would ship and service in China if licensed (y is large), the Chinese penalty for complying with US measures is credible (the cabinet itself described China's decree on foreign extraterritorial measures and its planned entity list), and the EU Blocking Statute penalty is zero today. The compulsion cost zeta is therefore inactive in 2026. The domestic cost of a *concession* (denying licences or cutting servicing) is a separate parameter. The state has the legal tool, since spare-parts exports need a licence, and Bloomberg reported in 2024, through anonymous sources the government never confirmed, that top-DUVi servicing licences would not be renewed. Whether the 2026 servicing licences were renewed is unknown.

**Second, the sovereignty cost attaches to the form of compliance, and parliament has said so in a motion.** The cabinet objects to MATCH because it "druist in tegen het uitgangspunt dat Nederland haar eigen exportcontrolebeleid vormgeeft". JA21 asked whether Dutch export controls must not be steered by "onbewezen aantijgingen of buitenlandse druk" (while staying open to partners' signals), and the minister answered "Ja" (10 July 2026). Sjoerdsma told NOS that MATCH "could potentially put our national security in American hands", and told ANP: "That is a matter for us to decide."

The only adopted motion that touches MATCH is the Bamenga motion (37020-XVII nr. 11). It was signed by members of all three coalition parties (Bamenga, D66; Lohman, CDA; Maes, VVD), the cabinet left it to the House ("oordeel Kamer"), and it passed 110 to 40 on 13 October 2026. It asks the cabinet to use the evaluation of the Dual-Use Regulation to push for harmonised EU export control and to argue for "gezamenlijk Europees optreden wanneer derde landen individuele lidstaten onder druk zetten om hun exportbeleid aan te passen", and to report progress to the House. In the model's terms this is parliamentary support for self-binding through Europeanised controls (the self-binding versus dual-key remark) at a low sovereignty cost sigma^b, combined with resistance to a dual key that gives Washington a veto.

Parliament has not tied the cabinet's hands against alignment on substance. No motion rejects MATCH, and the cabinet refuses to "speculeren" about instruments or Chinese countermeasures, while noting that EU law has "verschillende mitigatiemogelijkheden" against foreign extraterritorial measures. Its public commitments are written answers, so Fearon-style audience costs are modest. Public opinion is a latent cost. Pew (spring 2026) finds that 41 percent of Dutch respondents call the US a reliable partner, down from 88 percent in 2022; 25 percent view the US favourably; and confidence in Xi (28 percent) exceeds confidence in Trump (15 percent).

**Third, a change of government is a real hazard, but its direction depends on the instrument.** The Jetten cabinet (D66, VVD, CDA, sworn in on 23 February 2026) holds 66 of 150 seats with no support agreement. Votes show two cross-cutting axes:

- **Atlanticism.** The Maes-Hoogeveen motion on reminding allies of US indispensability passed 87 to 63, with D66 voting against its coalition partners although the cabinet had left the motion to the House. The Hoogeveen-van Dijk motion on good relations with the US passed 113 to 37. Only 29 MPs voted to reduce dependence on US weapons systems.
- **Europeanisation.** Only PVV, FvD, the Markuszower group, SP, PvdD and Keijzer (40 seats) voted against the Bamenga motion.

Seat arithmetic constrains the counterfactual. Any right-leaning majority needs VVD, CDA, PVV, JA21 and Markuszower (75 seats), and in practice BBB too. Within such a bloc, Bamenga's supporters outnumber its opponents by 52 to 26, while the Piri motion's supporters and opponents are close (40 to 38). A government change would therefore leave Europeanised export control intact but make EU coercive countermeasures against Washington harder to sustain. In the Netherlands a cabinet collapse normally leads to an election, so today's seats are only a guide.

Nexperia calibrates the state's instruments. The Goods Availability Act order (30 September 2025) was suspended after seven weeks (19 November 2025), once China resumed export licences for Nexperia chips. An information duty on moving production assets and knowledge remained. The Enterprise Chamber's provisional measures persisted, and in February 2026 it ordered a formal inquiry and kept the CEO suspended. Courts supply commitment that ministers do not. Parliament rejected a broad new intervention instrument (33 to 117) but asked the cabinet to explore extending the Wet vifo toolkit to other sectors and to examine strategic state participation (116 to 34).

The live test has not happened. H.R. 8170 has not moved since HFAC ordered it reported, 36 to 8, on 22 April 2026, though cosponsors keep joining. The House passed its FY2027 NDAA (H.R. 8800) 216 to 212 on 22 July 2026 with no MATCH text. The Senate committee text (S. 4784) has none either, and cloture on the motion to proceed failed 50 to 46 on 14 July. NU.nl's August report that MATCH was "on track to be added to the U.S. defense budget" is not borne out by either text as of 27 October 2026.

## Verified facts table

Verdicts: V = verified as stated; C = verified after correction (corrected wording shown); U = unverifiable; F = false. Items 51 to 60 are new.

| # | Claim (corrected where needed) | Verdict | Source (date) | Note |
|---|---|---|---|---|
| 1 | Project Beethoven: the state, region and business commit EUR 2.51bn through 2030 (EUR 1.73bn state, EUR 778m region and business), plus EUR 80.5m a year from the state from 2031; the cabinet states "de hoop en verwachting" that ASML realises its expansion in the Netherlands and keeps its "statutaire, fiscale en werkelijke zetel" there. | V | https://zoek.officielebekendmakingen.nl/kst-33009-141.html (28 Mar 2024); annex 2024D12374 | Filed under dossiers 33009 and 32637. Signed by Adriaansens, Harbers, Heijnen, De Jonge and Dijkgraaf. EUR 1.28bn of the state share comes from the National Growth Fund. |
| 2 | Beethoven point 4: a structural dialogue "zal worden opgezet" between General Affairs, Foreign Affairs, Economic Affairs "en andere relevante partijen en ASML": fortnightly at working level, monthly at senior civil-service level "om strategie voor te bereiden en inzet te bepalen", quarterly at political level "om strategie te bepalen en inzet en voortgang te bespreken", plus ad hoc consultation; the trade minister will push for "vergaande Europese coördinatie"; the state will strive for an international level playing field for measures "zoals exportcontrole op halfgeleiderproductieapparatuur". | C | https://gegevensmagazijn.tweedekamer.nl/OData/v4/2.0/Document(958a035e-acd7-4ecd-b7ce-0ff0185e009c)/resource (28 Mar 2024) | A promise. No later document found confirms that the dialogue meets. The progress letters 33009-159 (27 May 2025) and 33009-166 (1 Sep 2025) do not mention it. |
| 3 | Sneller, Podt (D66) and Inge van Dijk (CDA) asked about "het dreigende vertrek van ASML", citing De Telegraaf (6 Mar 2024); Adriaansens and Van Gennip answered (21 Jun 2024) that Beethoven started "vanwege het grote belang van de microchipsector voor Nederland, met ASML als grote aanjager". | V | https://zoek.officielebekendmakingen.nl/ah-tk-20232024-2044.html (21 Jun 2024) | Questions submitted 7 Mar 2024. |
| 4 | Bloomberg (anonymous sources), via Bits&Chips: the Dutch government will not renew ASML's licences to service and supply spare parts for "top-of-the-line DUV immersion machines" in China after they expire at end-2024; Washington reportedly threatened to "halt service operations through unilateral actions". | V | https://bits-chips.com/article/asml-faces-more-restrictions-in-china-as-dutch-government-gives-in-to-us-pressure/ (29 Aug 2024) | Secondary report, "allegedly". No tool models named. Not confirmed by the government. |
| 5 | The 2024 export-control report says the national regulation for advanced semiconductor production equipment (since Sept 2023) and the supplementary regulation (since 1 Dec 2024) "kennen geen rapportageverplichting zoals deze geldt in EU-Verordening 2021/821". | V | https://gegevensmagazijn.tweedekamer.nl/OData/v4/2.0/Document(c68ae81e-e1b6-4ed0-bbd8-be647f8f7546)/resource (27 Jun 2025; annex to Kamerstuk 22054-459) | Predates the 15 Nov 2025 transfer of items to EU Annex I (item 9), so it now applies with certainty only to the residual national items. |
| 6 | Nexperia: the economy minister issued a Goods Availability Act order on 30 Sep 2025 and suspended it on 19 Nov 2025, citing Chinese export licences for Nexperia chips and diplomatic progress; an information duty on moving production assets and knowledge remains; the Enterprise Chamber's provisional measures "sterken mij in dit vertrouwen". | V | https://zoek.officielebekendmakingen.nl/kst-32637-717.html (19 Nov 2025) | Minister V.P.G. Karremans (Economic Affairs). |
| 7 | Initiative note by Paternotte (D66) and Boswijk (CDA), "Nieuwe China-Strategie" (36696-2, 12 Feb 2025): ASML is "de belangrijkste leverancier" of TSMC; a China-Taiwan crisis "slaat Nederland knock-out"; "Wij zijn niet alleen afhankelijk van China; China is dat ook van ons"; proposes an EU deterrence action plan and sanctions packages. Cabinet response 36696-3 (3 Oct 2025). | V | https://zoek.officielebekendmakingen.nl/kst-36696-2.html (12 Feb 2025); kst-36696-3 (3 Oct 2025) | Response signed by the Minister of Foreign Affairs. |
| 8 | Election of 29 Oct 2025: D66 26, PVV 26, VVD 22, GL-PvdA 20, CDA 18, JA21 9, FvD 7, BBB 4, DENK, SGP, PvdD, CU, SP 3 each, 50PLUS 2, Volt 1. | V | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2025Z21261&did=2025D50238 (vote of 9 Dec 2025, seats by faction); https://en.wikipedia.org/wiki/2025_Dutch_general_election | Confirmed by the House's own seat table. Kiesraad certification not retrieved. |
| 9 | Regulation of the State Secretary for Foreign Affairs (A. de Vries) of 20 Nov 2025 (Stcrt. 2025, 38653, published 24 Nov 2025, in force from 15 Nov 2025): repeals the supplementary control regulation because "alle producten" moved to Annex I via the Commission's delegated regulation of 8 Sep 2025; replaces the annex of the semiconductor regulation, part of whose items also moved. Remaining national lithography items: 3B801.f.6 (light source 193 nm or longer, MRF 45 nm or less, DCO above 1.50 nm and at most 2.40 nm) and 3B801.f.7 (throughput upgrades for 3B801.f.6 or EU item 3B501.f.1.b). Basis: Article 9 of Reg. 2021/821. Existing licences continue under Article 12. | V | https://zoek.officielebekendmakingen.nl/stcrt-2025-38653.html (24 Nov 2025) | The number "2025/2003" is in a footnote not read here; the model note uses it. |
| 10 | The current Regeling geavanceerde productieapparatuur voor halfgeleiders (in force since 25 Nov 2025): Article 2 prohibits export "zonder vergunning van de Minister"; covered equipment includes "speciaal ontworpen onderdelen en toebehoren daarvoor"; no article mentions maintenance, repair or software updates; annex software and technology entries cover "ontwikkeling", "productie" or "gebruik". | C | https://wetten.overheid.nl/BWBR0048439/ (consulted 29 Oct 2026, via page fetch) | Correction: spare parts are inside the licensing scope through the parts-and-accessories clause. |
| 11 | Nexperia debate motions, votes of 9 Dec 2025: Dassen c.s. (32637-730), an instrument to intervene at any firm with serious geopolitical risks, rejected 33 to 117 (D66, PVV, VVD, CDA, JA21, FvD, BBB, SGP, 50PLUS against; cabinet advised against). Dekker (FvD, 32637-733), explore extending the Wet vifo toolkit to other sectors and examine strategic state participation, adopted 116 to 34 (VVD, JA21, SGP against). Van der Lee c.s. (32637-735), six-monthly economic-security reporting, adopted 107 to 43 (VVD, CDA, SGP against). | C | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2025Z21264&did=2025D50241 and the pages for 2025Z21261, 2025Z21266 (9 Dec 2025) | "stimuleren of zelfs afdwingen" is in the Dekker preamble, not the request. Van der Lee's co-signers included Oualhadj (D66). |
| 12 | Wennink report "De Route Naar Toekomstige Welvaart" (12 Dec 2025). Peter Wennink retired as ASML President and CEO on 24 Apr 2024. The coalition agreement steers on 1.5% structural growth "Conform het rapport-Wennink" (p. 30). | V | https://zoek.officielebekendmakingen.nl/kst-29826-281.html (fn. 3); ASML 20-F FY2025 (25 Feb 2026); coalition agreement p. 30 (30 Jan 2026) | |
| 13 | Groep Markuszower (7 seats) active from 20 Jan 2026, reducing PVV to 19; GL-PvdA sits as PRO (20) from 9 Jun 2026; Lid Keijzer from 24 Feb 2026 (BBB to 3). Current House: D66 26, VVD 22, PRO 20, PVV 19, CDA 18, JA21 9, Markuszower 7, FvD 7, CU, SP, PvdD, SGP, BBB, DENK 3 each, 50PLUS 2, Keijzer 1, Volt 1. | V | https://gegevensmagazijn.tweedekamer.nl/OData/v4/2.0/Fractie (queried 29 Oct 2026) | |
| 14 | Piri c.s. (21501-20 nr. 2364), act with France and Germany in the EU and keep economic countermeasures "waaronder het antidwanginstrument" in reserve while the US president maintains his Greenland claim: adopted 103 to 46 on 22 Jan 2026 (PVV, JA21, FvD, Markuszower, BBB against; Volt absent); co-signers Klos (D66), Boswijk (CDA), Struijs (50PLUS), Ceder (CU), Teunissen (PvdD), Dobbe (SP); the caretaker cabinet advised against. Teunissen and Dobbe (nr. 2366), reduce dependence on US weapons systems: rejected 29 to 120 (only GL-PvdA, DENK, PvdD, SP for). | C | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z01210&did=2026D02880; id=2026Z01212&did=2026D02882 (22 Jan 2026) | Memo listed only D66 and CDA as co-signers. |
| 15 | Coalition agreement "Aan de slag. Bouwen aan een beter Nederland. Coalitieakkoord 2026-2030" (D66, VVD, CDA; 67 pp.; 30 Jan 2026) does not mention ASML or export control ("export" appears nowhere). It names Project Beethoven as a model for mission teams (p. 6) and continues the area-based nitrogen approach for Brainport (p. 21). | C | https://www.kabinetsformatie2025.nl/site/binaries/site-content/collections/documents/2026/01/30/aan-de-slag---coalitieakkoord-2026-2030/coalitieakkoord-d66-vvd-cda.pdf (30 Jan 2026) | Addition only. |
| 16 | Coalition agreement on defence: p. 31, "De NAVO vormt de hoeksteen van onze collectieve veiligheid. De Verenigde Staten zijn de wereldmacht met wie wij de meeste belangen delen"; reducing "eenzijdige afhankelijkheden" and building a European pillar lets the Netherlands address the US "geloofwaardig"; "We accepteren niet dat we voor onze bescherming afhankelijk blijven van anderen"; 3.5% of GDP, anchored in law. p. 32: 40 percent of defence procurement jointly with European partners; "constructief" on strengthening a European nuclear deterrent; accession to the Treaty of Aachen; reduce dependence on "landen buiten het NAVO-bondgenootschap" for essential weapons systems. | C | coalition agreement pp. 31-32 (30 Jan 2026) | Added the non-NATO clause: the weapons-dependence pledge does not target the US. |
| 17 | Coalition agreement p. 34: protect freedoms against "Rusland, China, en Iran"; "We benutten waar dat nog mogelijk is kansen in onze relatie met China"; act "onverbiddelijk" against IP theft; "We blijven ons inspannen voor onze trans-Atlantische band", using diplomatic channels to address the US "altijd met oog voor de relatie en het behoud van kritieke veiligheidsbelangen"; reduce "eenzijdige afhankelijkheid" in defence, software and critical raw materials; learn "de taal van macht"; "harde grenzen waar onze technologie of veiligheid in het geding is". | V | coalition agreement p. 34 (30 Jan 2026) | |
| 18 | Coalition agreement on economic security: p. 35 tighten investment screening and block transfer of sensitive technology "(zoals fotonica en quantum)"; p. 14 "steeds vaker doelwit van ongewenste overdracht van kennis en technologie door landen als China en Iran"; p. 58 "afhankelijkheden van de VS en China toenemen"; p. 59 "We versterken onze positie in de halfgeleiderindustrie"; p. 49 knowledge-security screening law; p. 27 use of Chips Act 2.0 and IPCEI co-financing; a national investment institution (pp. 10, 27, 29, 65). | V | coalition agreement (30 Jan 2026) | |
| 19 | Stoffer c.s. (SGP, with Hoogeveen, JA21, and Boswijk, CDA; 36800-V nr. 72), prevent added Rotterdam container-terminal capacity going to a Chinese state enterprise: adopted 150 to 0 on 4 Feb 2026. | V | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z01719&did=2026D04078 (4 Feb 2026) | |
| 20 | The Enterprise Chamber ordered a formal investigation into Nexperia, appointing two independent investigators, kept CEO Wing (Xuezheng) Zhang suspended, cited clear signs he acted "with a conflicting interest", kept limits on Wingtech's shareholder influence, and noted the European and Chinese operations "now function almost like two distinct companies". | V | https://nltimes.nl/2026/02/11/enterprise-chamber-orders-investigation-nexperia-keeps-ceo-suspended (11 Feb 2026) | |
| 21 | Jetten cabinet sworn in on 23 Feb 2026: a minority coalition of D66, CDA and VVD with 66 of 150 seats, needing opposition support for each bill. | V | https://www.euronews.com/2026/02/23/new-dutch-minority-government-sworn-in-under-the-nations-youngest-prime-minister-rob-jette (23 Feb 2026) | No support agreement is mentioned. |
| 22 | Portfolio holders: PM Rob Jetten (D66); Foreign Trade and Development Cooperation, the licensing authority, Sjoerd Sjoerdsma (D66); Economic Affairs and Climate Heleen Herbert (CDA); Defence and Deputy PM Dilan Yesilgoz-Zegerius (VVD); Foreign Affairs Tom Berendsen (CDA); Finance Eelco Heinen (VVD); Derk Boswijk (CDA), State Secretary for Defence (arms procurement and personnel). | C | https://www.government.nl/government/members-of-cabinet; https://en.wikipedia.org/wiki/Jetten_cabinet; Tweede Kamer letter 2026D50059 "Aan staatssecretaris Defensie" (9 Oct 2026) | Resolves the memo's ambiguity: government.nl styles all members "Minister" in English. |
| 23 | ASML FY2025 20-F: "Countries affected by export control restrictions may also introduce countermeasures, which could result in conflicting regulations and legal liabilities"; "Geopolitical instability and potential nationalization of assets also poses risks"; installed-base revenue may fall because "we may be limited by export control restrictions"; "We share relevant dynamics with governments to foster understanding of potential impacts of current and future measures." China was 29.1% of 2025 and 36.1% of 2024 total net sales. | V | https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/asml-20251231.htm (filed 25 Feb 2026) | |
| 24 | Semicon Visie 2035 (sent with 29826-281 by Minister Herbert, dated 1 Apr 2026, published 3 Apr 2026), produced by the Semicon Board NL (started early 2025; ministers of Economic Affairs (chair), Education, Defence, Foreign Trade; C-level members from ASML, ASM, VDL ETG, NXP, SMART Photonics, Nearfield Instruments, Axelera AI, plus FME, High Tech NL and TKI HTSM): "Een sterke positie in het halfgeleider-ecosysteem biedt daarmee geopolitieke leverage"; "Met deze positie heeft Nederland toegang tot andere cruciale goederen en diensten". Under "Blijf in gesprek over exportcontrole": "overwegingen van nationale veiligheid leidend en vindt tegelijkertijd een zorgvuldige weging plaats op basis van de effectiviteit en de economische impact van de maatregelen". | C | https://zoek.officielebekendmakingen.nl/kst-29826-281.html and blg-1242444 (1 Apr 2026) | The memo dropped "nationale veiligheid leidend" and presented a description as a request. |
| 25 | H.R. 8170 (MATCH Act; sponsor Baumgartner, R-WA) introduced 2 Apr 2026, ordered reported in the nature of a substitute (amended) by HFAC, 36 to 8, on 22 Apr 2026; no later action. S. 4281 (sponsor Ricketts, R-NE) introduced 13 Apr 2026 and referred to Senate Banking; no later action. | V | https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr8170.xml; .../s/BILLSTATUS-119s4281.xml (updated 2 Oct and 15 Sep 2026) | Cosponsor counts in item 52. |
| 26 | Hoogeveen (JA21) asked about MATCH on 10 Apr 2026; Sjoerdsma answered on 12 May 2026: firms might no longer service already delivered machines "zonder vergunning", with a "presumption of denial"; "Het kabinet kijkt daarom met zorg naar de MATCH Act"; "Het kabinet is tegen de extraterritoriale werking ... Elk land is verantwoordelijk voor zijn eigen exportcontrolewetgeving"; "exportcontrole geen exportverbod is"; objections raised with Congress and the administration, including during the royal visit; "Nederland deelt in algemene zin de veiligheidszorgen". | V | https://zoek.officielebekendmakingen.nl/ah-tk-20252026-1903.html (12 May 2026) | |
| 27 | Jetten raised export controls at Trump's White House dinner during the royal visit and with White House economic advisers; called it "one of the main reasons" for the trip; said they should "not only hear from ASML what is good or less good for ASML" but "also hear from the prime minister"; "some disagreement", "without reaching consensus". | V | https://nltimes.nl/2026/04/14/netherlands-pushes-back-proposed-us-export-limits-asml (14 Apr 2026; ANP) | |
| 28 | ASML US, LLC in-house lobbying: USD 300k, 300k, 400k, 500k (Q1 to Q4 2025); USD 600k (Q1 2026, posted 17 Apr), 600k (Q2, 17 Jul), 500k (Q3, 20 Oct 2026); every 2026 report names "the Multilateral Alignment of Technology Controls on Hardware (MATCH) Act (H.R. 8170)". Outside firms: Alpine Group Partners (USD 70k a quarter; "MATCH Act STRIDE Act" in Q3 2026) and OGR (USD 70k a quarter; "H.R.8170/S.4281, MATCH" in Q2 and Q3 2026). Orrick is registered for ASML Netherlands B.V. with no-activity reports. Filings do not state the position taken. | C | https://lda.gov/api/v1/filings/?client_name=ASML&filing_year=2026 (filings posted 2 Apr to 20 Oct 2026) | OGR and Orrick were missing. Total Q1 to Q3 2026: USD 2.12m. The Q1 report (Jan to Mar) names H.R. 8170 although it was introduced on 2 Apr. |
| 29 | Hoogeveen (JA21; 21501-02 nr. 3416), work in the EU for "de-escalatie van de handelsspanningen met China" and reciprocal market access: adopted 114 to 36 on 21 May 2026. Against: GL-PvdA, Markuszower, CU, DENK, PvdD. | V | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z10537&did=2026D23834 (21 May 2026) | Cabinet: "oordeel Kamer". |
| 30 | Hoogeveen and Diederik van Dijk (SGP; 36715 nr. 42), "een aanjagersrol ... voor zo goed mogelijke betrekkingen met de Verenigde Staten": adopted 113 to 37 on 26 May 2026. Against: GL-PvdA, FvD, DENK, PvdD, SP, Volt. | V | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z10476&did=2026D23710 (26 May 2026) | |
| 31 | Maes (VVD) and Hoogeveen (JA21; 21501-02 nr. 3425), remind allies "hoe essentieel de betrokkenheid en bijdrage van de Verenigde Staten zijn voor de veiligheid van Europa", criticising "anti-Amerikaanse of polariserende sentimenten": adopted 87 to 63 on 27 May 2026. Against: D66, GL-PvdA, FvD, DENK, PvdD, SP, Volt. | V | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z10995&did=2026D24946 (27 May 2026) | Cabinet: "oordeel Kamer", so D66 voted against a motion its own cabinet did not oppose. |
| 32 | ASML and FNV, CNV, De Unie and VHP2 (with Belgian ACV) finalised a social plan for 1,700 job cuts, mainly in Development and Engineering and in IT and Data; no compulsory layoffs until 1 May 2027; no mention of export controls or China. | V | https://nltimes.nl/2026/06/10/asml-unions-finalize-social-plan-address-1700-job-cuts (10 Jun 2026) | |
| 33 | Buhler and Lohman (CDA) asked about MATCH after Trouw (18 May 2026); Sjoerdsma answered on 15 Jun 2026: "Het kabinet hecht aan goede samenwerking met partners, maar is tegen de extraterritoriale werking"; MATCH "druist in tegen het uitgangspunt dat Nederland haar eigen exportcontrolebeleid vormgeeft"; "Het kabinet gaat niet speculeren over de inzet van welk instrument dan ook in relatie tot de Act"; EU law has "verschillende mitigatiemogelijkheden" for foreign extraterritorial provisions; declined to speculate on Chinese countermeasures but described China's decree on countering foreign extraterritorial measures and its planned entity list. | V | https://zoek.officielebekendmakingen.nl/ah-tk-20252026-2251.html (15 Jun 2026) | Questions submitted 21 May 2026. |
| 34 | S. 4784 (Senate FY2027 NDAA) reported on 15 Jun 2026 (S. Rept. 119-127); no provisions on semiconductor manufacturing equipment controls, foreign direct product rules or MATCH; its only SME mention is in an AI-chip definition. Cloture on the motion to proceed failed 50 to 46 on 14 Jul 2026 (Record Vote 195); latest action a motion to proceed on 27 Jul 2026. | V | https://www.govinfo.gov/content/pkg/BILLS-119s4784rs/xml/BILLS-119s4784rs.xml; BILLSTATUS-119s4784.xml (updated 27 Oct 2026) | Cloture vote newly verified. |
| 35 | Van der Lee (PRO; 21501-20 nr. 2429, amended), a coalition of the willing and a partnership with Taiwan and Taiwanese chip firms: rejected 55 to 95 on 17 Jun 2026; BBB, CDA, D66, FvD, PVV and VVD against. | V | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z13359&did=2026D30220 (17 Jun 2026) | JA21, Markuszower, SGP, CU, DENK, PvdD, SP, 50PLUS, Keijzer and Volt voted for. |
| 36 | Sjoerdsma met his US counterpart (unnamed) in Washington on 23 Jun 2026. To ANP: "What makes us unhappy is that the bill seems to suggest that the United States could then impose measures on us"; "Cross-border cooperation must be on a voluntary basis, but coercion makes that very difficult"; "That is a matter for us to decide." To NOS: "It is very unfortunate that this could potentially put our national security in American hands." NOS: ASML earned EUR 27bn in China over three years (26 to 36 percent of revenue). | V | https://nltimes.nl/2026/06/24/dutch-government-irritated-us-plans-new-asml-export-restrictions (24 Jun 2026) | |
| 37 | On 3 Jul 2026 the Tweede Kamer asked the Algemene Rekenkamer (after a 25 Jun committee request) to investigate export control of strategic goods, focusing on licensing criteria, the foreign-policy test, the human-rights criterion and information to parliament. The Court accepted on 30 Sep 2026 and expects to report in mid-2027. | V | https://zoek.officielebekendmakingen.nl/kst-22054-484.html (25 Jun 2026); Kamerstuk 22054-492, document 2026D47550 (30 Sep 2026) | Filed in the arms-export dossier. Not ASML-specific, but it covers how parliament is informed. |
| 38 | Sjoerdsma met Chinese commerce minister Wang Wentao in Beijing, seeking to "put an end to the recent period of disagreement"; the relationship "perhaps resembled a bumper car park"; the Nexperia dispute is settled between the governments; ASML was among the disputes, without details. | V | https://nltimes.nl/2026/07/08/netherlands-tried-settle-nexperia-asml-disputes-trade-visit-china (8 Jul 2026; ANP) | |
| 39 | Answers of 10 Jul 2026 (Aanhangsel 2526) to Hoogeveen's questions of 23 Jun on Bloomberg's report (19 Jun 2026) that US officials are concerned an EUV tool reached China: enforcement action is taken when warranted, "Daar is op dit moment geen sprake van"; asked whether the Netherlands should be open to partners' signals but not steered "door onbewezen aantijgingen of buitenlandse druk", he answered "Ja"; enforcement rests on "Nederlandse wet- en regelgeving, objectieve feiten en een zelfstandige risicobeoordeling". | V | https://zoek.officielebekendmakingen.nl/ah-tk-20252026-2526.html (10 Jul 2026) | Compound question; this set is about EUV allegations, not MATCH. |
| 40 | The House passed H.R. 8800 (FY2027 NDAA) 216 to 212 (Roll no. 278) on 22 Jul 2026; the engrossed text has no provision on semiconductor manufacturing equipment, foreign direct product rules or de minimis; the Senate received it on 14 Sep 2026, with no later action. | V | https://www.govinfo.gov/content/pkg/BILLS-119hr8800eh/xml/BILLS-119hr8800eh.xml; BILLSTATUS-119hr8800.xml (updated 26 Oct 2026) | |
| 41 | NU.nl, via NL Times: through MATCH the US would push the Netherlands to stop ASML's DUV sales to China and servicing of delivered tools; "Dutch government officials are fiercely lobbying in Washington ... but their chances seem slim"; bipartisan support; "on track to be added to the U.S. defense budget". | V | https://nltimes.nl/2026/08/20/us-preparing-force-netherlands-ban-asml-selling-china (20 Aug 2026) | As a report. The NDAA route had not materialised in either chamber's text by 27 Oct 2026. |
| 42 | Nexperia litigation (Wikipedia citing Reuters): Wingtech challenged the Dutch government at the Supreme Court (Nov 2025; Reuters 28 Nov 2025); Wingtech sought USD 1.2bn damages in a new suit (Reuters 22 May 2026); a Chinese court froze about USD 300m of Nexperia's Chinese assets (Reuters 31 Aug 2026; SCMP USD 318m; Dongguan Intermediate Court per RFI); partnership with Tata Electronics (Reuters 17 Sep 2026). | V | https://en.wikipedia.org/wiki/Nexperia (consulted 29 Oct 2026) | Secondary. The Evertiq CNY 8bn Anti-Foreign Sanctions Law suit was not checked (U). |
| 43 | ASML began construction at Brainport Industries Campus North: up to 20,000 extra jobs, at least 3,000 by the end of phase one in 2029. Jetten, Schoof and Eindhoven mayor Dijsselbloem attended. Reported enablers: Beethoven, a TenneT high-voltage station extension at Best, and a rare nitrogen permit granted on grounds of "major public interest". | V | https://nltimes.nl/2026/09/08/asml-celebrates-start-campus-construction-will-open-extra-20000-jobs (8 Sep 2026) | |
| 44 | Martens-America (VVD) asked on 1 Oct 2026 how "de totale beschikbare financiële middelen van ruim € 2,5 miljard" have been spent and how the motion to use Beethoven as a blueprint was implemented; the answer was postponed on 20 Oct 2026. Earlier (6 Nov 2025), answering Eerdmans (JA21), Minister Karremans saw "geen directe signalen" of firms leaving Brainport over nitrogen or grid problems and put Beethoven's extra infrastructure investment at EUR 1,058m. | V | https://zoek.officielebekendmakingen.nl/ah-tk-20252026-352.html (6 Nov 2025); 2026Z20701, documents 2026D47758 and 2026D52153 | |
| 45 | IO+ reports, citing FD, that the Dutch government wants the MATCH bill "off the table". Its figures (USD 1bn to 1.5bn of service revenue "usually cited"; up to USD 9bn of Chinese sales at risk) are unattributed, and its claim that MATCH was introduced in both chambers on 2 April is wrong (Senate: 13 April). | V | https://ioplus.nl/en/posts/asml-caught-between-us-and-china-over-match-act (12 Oct 2026) | Low-quality source; use only for the FD attribution. |
| 46 | Bamenga (D66) with Lohman (CDA) and Maes (VVD) (37020-XVII nr. 11), filed at the 5 Oct 2026 legislative consultation and adopted 110 to 40 on 13 Oct 2026, cabinet appraisal "oordeel Kamer": use the Dual-Use Regulation evaluation to push EU harmonisation ("gezamenlijke veiligheidsafwegingen, uniforme regels en afgestemde handhaving") and "pleiten voor gezamenlijk Europees optreden wanneer derde landen individuele lidstaten onder druk zetten om hun exportbeleid aan te passen, zodat Europa zelf bepaalt wat wel en niet mag worden geëxporteerd", and inform the House of progress. For: D66, VVD, PRO, CDA, JA21, BBB, CU, DENK, SGP, 50PLUS, Volt. Against: PVV, FvD, Markuszower, PvdD, SP, Keijzer. | V | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z21071&did=2026D48603 (13 Oct 2026) | |
| 47 | Maes and Lohman (37020-XVII nr. 15), measures to reduce Europe's strategic dependence on critical raw materials: adopted 147 to 3 on 13 Oct 2026 (only PvdD against). Van Houwelingen (FvD; 37020-X nr. 18), plan for a scenario in which the Netherlands leaves the EU and/or NATO: rejected 14 to 136 on 6 Oct 2026, with FvD and the Markuszower group for. | C | https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z21075&did=2026D48613; id=2026Z20290&did=2026D46921 | Added who supported Van Houwelingen. |
| 48 | Tweede Kamer open data (subjects and titles, Sept 2025 to 28 Oct 2026) show no motion on ASML, the MATCH Act or ASML's China servicing licences. MATCH-specific scrutiny took the form of written questions from JA21 (1903) and CDA (2251); a second JA21 set (2526) concerned EUV allegations. The China committee debate set for 15 Oct 2026 was moved to 3 Feb 2027; a round-table on the trade relationship with China is planned for 9 Dec 2026. | C | https://gegevensmagazijn.tweedekamer.nl/OData/v4/2.0/Zaak and Activiteit (queried 29 Oct 2026) | Subject search only; full texts of all motions were not searched. |
| 49 | Pew, spring 2026, Netherlands: US favourable 25%, unfavourable 71%; confidence in Trump 15%, in Xi 28%; US a reliable partner 41% (80% in 2021, 88% in 2022); US contributes to peace and stability 19% (58% in 2023); US takes Dutch interests into account 11% (40% in 2023); approve of Trump on tariffs 10%. | V | https://www.pewresearch.org/wp-content/uploads/sites/20/2026/06/pg_2026.06.23_us-image-2026_topline.pdf (23 Jun 2026) | Fieldwork dates are not in the topline (U). |
| 50 | ECFR poll (Dutch sample 1,012, 30 Apr to 15 May 2026, margin 4.08): majorities in every country polled think the US would not support them if attacked; even PVV supporters trust "at least some European countries"; governing-party voters in the Netherlands mostly favour common European debt for defence; most people in the Netherlands would accept prioritising defence over other spending. | V | https://ecfr.eu/wp-content/uploads/2026/06/Home-alone-Europeans-are-ready-to-defend-themselves-v3.pdf (June 2026; ECFR/640) | Dutch country figures appear only in charts. |
| 51 | New: Senate cloture on the motion to proceed to S. 4784 failed 50 to 46 on 14 Jul 2026 (Record Vote 195). | V | govinfo BILLSTATUS-119s4784.xml (updated 27 Oct 2026) | Resolves an open question in the memo. |
| 52 | New: H.R. 8170 has 31 cosponsors (21 R, 10 D; latest Van Epps and Khanna on 1 Oct 2026). S. 4281 has 11 (5 R, 6 D, including Kim, Risch, Schumer, Crapo, Shaheen, Cotton, Coons, Banks, Warren, Britt, Schatz; latest 14 Sep 2026). | V | govinfo BILLSTATUS-119hr8170.xml, BILLSTATUS-119s4281.xml | Stalled in procedure, still accruing support. |
| 53 | New: ASML's Q3 2026 6-K (press release, presentation and financial statements, filed 14 Oct 2026) does not mention MATCH; export controls appear only in boilerplate risk language. | V | https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/ (14 Oct 2026) | The CFO's oral remarks were not checked. |
| 54 | New: national semiconductor controls were extended on 7 Sep 2024 and again on 1 Apr 2025. | V | https://zoek.officielebekendmakingen.nl/kst-33009-159.html (27 May 2025) | |
| 55 | New: on 8 Oct 2026 an MP asked for a written reaction to the report "Problemen voor de F-35: China heeft gevoelige onderdelen in handen"; the committee forwarded it to the State Secretary for Defence on 9 Oct 2026. | V | Tweede Kamer open data, Zaak 2026Z21598, documents 2026D49789 and 2026D50059 | Headline only; the content was not checked. Links US-defence dependence to Chinese supply-chain exposure. |
| 56 | New: in December 2025 the House asked for a cabinet reaction to the report "Nieuwe escalatie in Nexperia-vete: China publiceert namen Nederlandse spionnen". | V | Tweede Kamer open data, Zaak 2025Z21560 (10 Dec 2025) and 2025Z21766 | Headline only. |
| 57 | New: no 2026 government letter with "Nexperia" in its subject exists in Tweede Kamer open data; the last ministerial documents date from 19 Dec 2025. | V | Tweede Kamer open data, Zaak and Document (queried 29 Oct 2026) | Consistent with the memo's open question. |
| 58 | New: Jan Struijs (Piri co-signer) sits for 50PLUS; Klos and Bamenga for D66; Lohman for CDA and Maes for VVD (both since 25 Feb 2026); Hoogeveen for JA21. | V | Tweede Kamer open data, Persoon and FractieZetelPersoon | |
| 59 | New: the cabinet appraisals were "ontraden" (advise against) for Dassen (Dec 2025) and Piri (Jan 2026, caretaker cabinet), and "oordeel Kamer" for Dekker, Van der Lee 735, Stoffer, Hoogeveen 3416, Hoogeveen-van Dijk, Maes-Hoogeveen, Bamenga and Maes-Lohman. | V | Motion pages on tweedekamer.nl | |
| 60 | New: in the House's current 150 seats, VVD, PVV, JA21, Markuszower, FvD and BBB hold 67; a right-leaning majority needs CDA (VVD, CDA, PVV, JA21, Markuszower: 75; with BBB: 78). | V | Arithmetic on item 13 | Corrects the memo's "alternative majority". |

## Citation verdicts

| Key | Verdict | Accurate characterization | Note |
|---|---|---|---|
| putnam1988diplomacy | verified | Ratification constraints define win-sets; a small win-set can be a bargaining advantage; negotiators can target the other side's domestic actors (reverberation). | IO 42(3): 427-460. |
| fearon1994domestic | verified | In a crisis model, rising audience costs let leaders signal resolve; costs require a public commitment. | APSR 88(3): 577-592. |
| schultz1998domestic | verified | Opposition parties' public stances can confirm a government's threat or reveal that it is a bluff. | APSR 92(4): 829-844. The application to written questions is loose; JA21 and CDA did not endorse a threat. |
| tomz2007domestic | verified | Survey experiments show citizens disapprove of leaders who threaten and then back down. | IO 61(4): 821-840. |
| iida1993when | verified | Two-level games with incomplete information about domestic constraints. | JCR 37(3): 403-426. Full title includes "Two-Level Games with Uncertainty". |
| tarar2001international | verified | With constraints on both sides, a generalized Schelling conjecture holds only under some conditions (for example one side highly constrained, the other not). | JCR 45(3): 320-340. |
| culpepper2011quiet | corrected | Business power is greatest in low-salience arenas dominated by managerial expertise and weakens as salience rises. | Crossref print date 22 Nov 2010; Open Library gives 2010. Key kept; year corrected to 2010 (often cited as 2011). Cambridge Studies in Comparative Politics. |
| culpepper2015structural | corrected | Reanimates structural power for IPE and CPE, conceptualized "as a set of mutual dependencies between business and the state". | BAP 17(3): 391-409. Not primarily about anticipated exit. |
| culpepper2014structural | verified | Structural power is exercised strategically; banks with credible exit options (UK) resisted bailout terms that US banks had to accept. | Politics and Society 42(4): 427-454. |
| fairfield2015structural | verified | Distinguishes structural (disinvestment-based) from instrumental (ties, lobbying, expertise) power and shows how both shape policy formulation. | BAP 17(3): 411-441. |
| fairfield2015private | verified | Book-length theory of business power over tax policy in Chile, Argentina and Bolivia. | CUP 2015; subtitle "Business Power and Tax Politics". |
| hacker2002business | verified | Structural power varies with the level of government (capital mobility across states versus the nation), so venue matters. | Politics and Society 30(2): 277-325. |
| lindblom1982market | verified | Market systems automatically punish policies that threaten business investment, so governments anticipate business reactions. | JOP 44(2): 324-336. |
| woll2014power | verified | Banks shaped bailouts through collective inaction rather than active lobbying. | Cornell UP 2014. |
| mastanduno1992economic | corrected | Study of CoCom and US-allied bargaining over East-West export controls; recurrent conflict over scope and US extraterritorial pressure. | Cornell UP 1992, ISBN 0801499968 (Open Library); reissue DOI 10.7591/9781501737145 (2020). |
| malkin2024geoeconomics | verified | US extraterritorial reach over semiconductor value chains as a geoeconomic tool in the US-China rivalry. | RIPE 31(2): 674-699. |
| gjesvik2023private | verified | Privately owned infrastructure shapes weaponized interdependence; owners are actors, not conduits. | RIPE 30(2): 722-746 (online 2022). |
| farrell2019weaponized | verified | States with jurisdiction over network hubs can use panopticon and chokepoint effects. | IS 44(1): 42-79. |
| bown2020marched | verified | How US export controls and FDP expansions drew the semiconductor industry, including allied firms, into the trade war. | EAER 24(4): 349-388. |
| schelling1960strategy | verified | Commitment, the bargaining power of a constrained negotiator, and the threat that leaves something to chance. | Harvard UP 1960. No DOI. |
| coalitieakkoord2026 | verified | Positions on NATO and 3.5 percent (p. 31), joint European procurement, nuclear deterrence, Aachen and non-NATO dependence (p. 32), China and the US (p. 34), investment screening (p. 35), semiconductors (p. 59); no mention of ASML or export controls. | 67 pp., 30 Jan 2026. |
| kst33009_141 | corrected | Beethoven package (EUR 2.51bn) and the promised export-control dialogue with ASML (annexed letter). | Authors: Adriaansens, Harbers, Heijnen, De Jonge, Dijkgraaf. Dossiers 33009 and 32637. |
| semiconvisie2026 | verified | The government states that a strong position "biedt geopolitieke leverage"; ASML's C-level sits on the board that wrote it. | Letter dated 1 Apr 2026, published 3 Apr 2026. |

## Modeling implications

These map the evidence onto the notation of model_design_v2.md and notes/v2/resolutions.md. Protocol (f) of the earlier design has been dropped, so breakdown points go to lambda, psi and Proposition 5.

1. **Remark F (firm between jurisdictions).** ASML's revealed preference is to keep shipping and servicing in China within licences: it lobbies on MATCH every quarter, and its 20-F flags conflicting countermeasures. So y is large. The Chinese penalty for complying with US measures, p_C, is credible: the cabinet itself described China's decree on foreign extraterritorial measures and its planned entity list, and Nexperia showed targeted Chinese retaliation. The Blocking Statute penalty p_B is zero today: the cabinet "gaat niet speculeren" and only notes "mitigatiemogelijkheden". The compulsion cost zeta is therefore inactive in 2026. It switches on only if MATCH or a new FDP rule raises the credible US penalty f^F above y + p_C. ASML's USD 2.12m of US lobbying in 2026 is direct evidence that the firm acts on f^F. A three-player variant could make f^F endogenous to firm lobbying.
2. **Do not call the domestic cost of a concession zeta.** The memo's "cost of compelling ASML to cut servicing" is a cost to the holder of making a concession. In v2 it enters Q_NL (through c_NL) or the cost side of a reversible concession, not Remark F. Give it its own symbol, for example c_F. It is low for licence denials under existing law: the state holds the licence, spare parts need one, and Bloomberg's 2024 non-renewal report suggests the state can impose such cuts. It is bounded above by ASML's relocation threat, which has weakened since sunk investment in Veldhoven (campus groundbreaking, 3,000 jobs by 2029).
3. **Delta_c (enforceability of a control transfer).** Three things lower Delta_c for a 2031-style US holding company: the Dutch state's override instruments (the Goods Availability Act used against Nexperia's owner, Enterprise Chamber measures, parliament's 116-34 request to extend the Wet vifo toolkit and examine state participation), the coalition's pledge to tighten investment screening, and ASML's deepening Dutch footprint. By Corollary (iii) of Proposition 4, Gamma is nondecreasing in Delta_c, so the ultimatum is less attractive to Washington than Europe 2031 assumes, all else equal.
4. **sigma (sovereignty cost of a transfer) and its distribution F in Proposition 5.** The evidence puts mass on high sigma for foreign control of strategic Dutch assets: the 150-0 Rotterdam terminal motion, the vifo motion, and cross-party language that controls must not be steered by "buitenlandse druk". The US's uncertainty about sigma is real for a minority cabinet. Breakdown probability 1 - F(shat) should be calibrated as non-trivial.
5. **Self-binding versus dual key.** The Bamenga motion (110-40, all three coalition parties, cabinet neutral) is direct evidence that the holder's cost of self-binding through Europeanised controls, sigma^b, is low. The cabinet's objection to extraterritoriality ("Elk land is verantwoordelijk voor zijn eigen exportcontrolewetgeving") is evidence that a dual key with a US veto carries a sovereignty cost close to sigma. The remark predicts binding when -sigma^b - r^b exceeds the ultimatum payoff. Sjoerdsma's July 2026 Beijing visit to end the "bumper car" period reads as an effort to keep China's punishment of binding, r^b, low. A US strategy of routing demands through EU harmonisation (a delegated act) would face the lowest Dutch resistance.
6. **Rupture hazard and government change.** A change of government is better modelled as a shock to the holder's type (sigma, c_NL, Q_NL) than as a rupture with hazard lambda. Its direction depends on the instrument. Europeanised export control survives any plausible majority: within a VVD-CDA-PVV-JA21-Markuszower-BBB bloc (78 seats), Bamenga supporters outnumber opponents by 52 to 26. EU coercive countermeasures against Washington do not: in the same bloc the Piri motion splits 40 to 38. So a shock lowers the probability of an EU countermeasure (the Remark E stage-1 vote) but not of Europeanised compliance. The "threat that leaves something to chance" weakens against Washington on countermeasures only. Against Beijing, PVV and JA21 favour de-escalation (Hoogeveen 3416) while voting for the 150-0 port motion, so their effect on China-facing exit is mixed.
7. **Gatekeeper premium and targeted benefits (Remark G).** US-targetable conditional parts in c_NL are large and stable in parliament: NATO is the "hoeksteen", the US is the power "met wie wij de meeste belangen delen", and only 29 MPs voted to reduce dependence on US weapons. The coalition's weapons-dependence pledge targets countries outside NATO. Public opinion (US reliable at 41 percent) erodes the value of US promises but has not moved parliamentary votes. D66's vote against the Maes-Hoogeveen motion shows the security linkage is party-dependent within the coalition. The F-35 parts question (October 2026) is a reminder that defence dependence on the US also carries exposure to China.
8. **Audience costs.** These are low and asymmetric. There is no motion against alignment, commitments come as written answers, and licensing data for national items are unpublished. Bamenga adds a weak reporting duty ("de Kamer over de voortgang te informeren"), and the Rekenkamer study (mid-2027) on information provision may raise transparency. Apply an audience cost only to a visible, bilateral cave.
9. **Joint principal, not agent.** Model the state and ASML as co-principals sharing a preference for delay and against the extraterritorial form, with possible divergence on substance that licensing secrecy hides. Jetten's "not only hear from ASML" is the state asserting its own voice, so do not model the state as ASML's agent abroad.
10. **Courts as a commitment device.** Nexperia shows ministerial instruments are reversible within weeks under targeted Chinese retaliation, while judicial measures persist and escalate. Let the holder's commitment technology vary by instrument: executive licence decisions low, judicial or EU-legal anchors high. This links to the enforceability term Delta_c and to self-binding.
11. **Timing.** In October 2026 MATCH is an announced but uncommitted US threat. It has growing cosponsorship but no NDAA vehicle, and Senate floor action on the NDAA has stalled since the failed cloture vote of 14 July. If enacted, its alignment deadlines would fall during the minority cabinet's term. Treat MATCH as a threat with an exogenous probability of becoming credible, not as enacted law.

## Open questions

1. Did the Netherlands renew, narrow or let lapse ASML's 2026 licences for DUVi servicing and spare parts in China? Since 15 November 2025 many items are licensed under Article 12 of Regulation 2021/821. Check whether they now appear in the Dutch dual-use licence data, which the 2024 report says are published regularly for all dual-use licences.
2. Item numbering: the Staatscourant uses 3B801.f.6 and 3B801.f.7, and the EU item is 3B501.f.1.b. A project note's "3B901f6" from Commission compilation C/2026/3577 was not checked; use the Staatscourant numbering.
3. Does the Beethoven export-control dialogue meet? No public record was found. A Woo (freedom of information) request or the pending answer to Martens-America (2026Z20701) may tell.
4. Will MATCH enter the FY2027 NDAA through a Senate floor amendment or conference text? The mrkt30 claim of a Senate manager's amendment remains unverified. The failed cloture vote (14 July) is now verified.
5. If MATCH is enacted, will the cabinet align within the deadlines, push for an EU delegated act as Bamenga implies, or resist? The cabinet refuses to "speculate".
6. Status of the Nexperia Goods Availability Act order (suspended or revoked), the Enterprise Chamber inquiry's findings, and the Dongguan suits. There is no 2026 government letter on Nexperia; the Evertiq CNY 8bn figure was not checked.
7. ASML's public position on MATCH. The Q3 2026 6-K is silent; the CFO's remarks on the 14 October results day (reported via Global Times citing Reuters) need the call transcript. Brainport Development's and the unions' positions remain unfound.
8. Jetten's 25 September 2026 Bloomberg TV remark ("workable agreement") is known only through a Dutch paraphrase.
9. Eerste Kamer composition and whether the minority coalition can pass a law anchoring 3.5 percent or a national blocking or anti-coercion instrument.
10. Kiesraad certification date; Pew fieldwork dates; Dutch polls (Clingendael Barometer, I&O, Ipsos) with direct questions on ASML or export control.
11. Content of the October 2026 F-35 report and the December 2025 Nexperia "spies" report, both known here only by headline.

## BibTeX (verified or corrected entries)

```bibtex
@article{putnam1988diplomacy,
  author  = {Putnam, Robert D.},
  title   = {Diplomacy and Domestic Politics: The Logic of Two-Level Games},
  journal = {International Organization},
  year    = {1988},
  volume  = {42},
  number  = {3},
  pages   = {427--460},
  doi     = {10.1017/S0020818300027697}
}

@article{fearon1994domestic,
  author  = {Fearon, James D.},
  title   = {Domestic Political Audiences and the Escalation of International Disputes},
  journal = {American Political Science Review},
  year    = {1994},
  volume  = {88},
  number  = {3},
  pages   = {577--592},
  doi     = {10.2307/2944796}
}

@article{schultz1998domestic,
  author  = {Schultz, Kenneth A.},
  title   = {Domestic Opposition and Signaling in International Crises},
  journal = {American Political Science Review},
  year    = {1998},
  volume  = {92},
  number  = {4},
  pages   = {829--844},
  doi     = {10.2307/2586306}
}

@article{tomz2007domestic,
  author  = {Tomz, Michael},
  title   = {Domestic Audience Costs in International Relations: An Experimental Approach},
  journal = {International Organization},
  year    = {2007},
  volume  = {61},
  number  = {4},
  pages   = {821--840},
  doi     = {10.1017/S0020818307070282}
}

@article{iida1993when,
  author  = {Iida, Keisuke},
  title   = {When and How Do Domestic Constraints Matter? Two-Level Games with Uncertainty},
  journal = {Journal of Conflict Resolution},
  year    = {1993},
  volume  = {37},
  number  = {3},
  pages   = {403--426},
  doi     = {10.1177/0022002793037003001}
}

@article{tarar2001international,
  author  = {Tarar, Ahmer},
  title   = {International Bargaining with Two-Sided Domestic Constraints},
  journal = {Journal of Conflict Resolution},
  year    = {2001},
  volume  = {45},
  number  = {3},
  pages   = {320--340},
  doi     = {10.1177/0022002701045003004}
}

@book{culpepper2011quiet,
  author    = {Culpepper, Pepper D.},
  title     = {Quiet Politics and Business Power: Corporate Control in {Europe} and {Japan}},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  series    = {Cambridge Studies in Comparative Politics},
  year      = {2010},
  doi       = {10.1017/CBO9780511760716},
  note      = {Crossref print date 22 November 2010; often cited as 2011}
}

@article{culpepper2015structural,
  author  = {Culpepper, Pepper D.},
  title   = {Structural Power and Political Science in the Post-Crisis Era},
  journal = {Business and Politics},
  year    = {2015},
  volume  = {17},
  number  = {3},
  pages   = {391--409},
  doi     = {10.1515/bap-2015-0031}
}

@article{culpepper2014structural,
  author  = {Culpepper, Pepper D. and Reinke, Raphael},
  title   = {Structural Power and Bank Bailouts in the {United Kingdom} and the {United States}},
  journal = {Politics \& Society},
  year    = {2014},
  volume  = {42},
  number  = {4},
  pages   = {427--454},
  doi     = {10.1177/0032329214547342}
}

@article{fairfield2015structural,
  author  = {Fairfield, Tasha},
  title   = {Structural Power in Comparative Political Economy: Perspectives from Policy Formulation in {Latin America}},
  journal = {Business and Politics},
  year    = {2015},
  volume  = {17},
  number  = {3},
  pages   = {411--441},
  doi     = {10.1515/bap-2014-0047}
}

@book{fairfield2015private,
  author    = {Fairfield, Tasha},
  title     = {Private Wealth and Public Revenue in {Latin America}: Business Power and Tax Politics},
  publisher = {Cambridge University Press},
  address   = {New York},
  year      = {2015},
  doi       = {10.1017/CBO9781316104767}
}

@article{hacker2002business,
  author  = {Hacker, Jacob S. and Pierson, Paul},
  title   = {Business Power and Social Policy: Employers and the Formation of the {American} Welfare State},
  journal = {Politics \& Society},
  year    = {2002},
  volume  = {30},
  number  = {2},
  pages   = {277--325},
  doi     = {10.1177/0032329202030002004}
}

@article{lindblom1982market,
  author  = {Lindblom, Charles E.},
  title   = {The Market as Prison},
  journal = {The Journal of Politics},
  year    = {1982},
  volume  = {44},
  number  = {2},
  pages   = {324--336},
  doi     = {10.2307/2130588}
}

@book{woll2014power,
  author    = {Woll, Cornelia},
  title     = {The Power of Inaction: Bank Bailouts in Comparison},
  publisher = {Cornell University Press},
  address   = {Ithaca, NY},
  year      = {2014},
  doi       = {10.7591/cornell/9780801452352.001.0001}
}

@book{mastanduno1992economic,
  author    = {Mastanduno, Michael},
  title     = {Economic Containment: {CoCom} and the Politics of {East-West} Trade},
  publisher = {Cornell University Press},
  address   = {Ithaca, NY},
  year      = {1992},
  isbn      = {0801499968},
  note      = {Reissued 2020, doi:10.7591/9781501737145}
}

@article{malkin2024geoeconomics,
  author  = {Malkin, Anton and He, Tian},
  title   = {The Geoeconomics of Global Semiconductor Value Chains: Extraterritoriality and the {US-China} Technology Rivalry},
  journal = {Review of International Political Economy},
  year    = {2024},
  volume  = {31},
  number  = {2},
  pages   = {674--699},
  doi     = {10.1080/09692290.2023.2245404}
}

@article{gjesvik2023private,
  author  = {Gjesvik, Lars},
  title   = {Private Infrastructure in Weaponized Interdependence},
  journal = {Review of International Political Economy},
  year    = {2023},
  volume  = {30},
  number  = {2},
  pages   = {722--746},
  doi     = {10.1080/09692290.2022.2069145}
}

@article{farrell2019weaponized,
  author  = {Farrell, Henry and Newman, Abraham L.},
  title   = {Weaponized Interdependence: How Global Economic Networks Shape State Coercion},
  journal = {International Security},
  year    = {2019},
  volume  = {44},
  number  = {1},
  pages   = {42--79},
  doi     = {10.1162/isec_a_00351}
}

@article{bown2020marched,
  author  = {Bown, Chad P.},
  title   = {How the {United States} Marched the Semiconductor Industry into Its Trade War with {China}},
  journal = {East Asian Economic Review},
  year    = {2020},
  volume  = {24},
  number  = {4},
  pages   = {349--388},
  doi     = {10.11644/kiep.eaer.2020.24.4.384}
}

@book{schelling1960strategy,
  author    = {Schelling, Thomas C.},
  title     = {The Strategy of Conflict},
  publisher = {Harvard University Press},
  address   = {Cambridge, MA},
  year      = {1960}
}

@misc{coalitieakkoord2026,
  author       = {{D66} and {VVD} and {CDA}},
  title        = {Aan de slag. Bouwen aan een beter {Nederland}. Coalitieakkoord 2026--2030},
  howpublished = {Kabinetsformatie 2025, The Hague},
  year         = {2026},
  month        = jan,
  note         = {Presented 30 January 2026; 67 pp.},
  url          = {https://www.kabinetsformatie2025.nl/site/binaries/site-content/collections/documents/2026/01/30/aan-de-slag---coalitieakkoord-2026-2030/coalitieakkoord-d66-vvd-cda.pdf}
}

@misc{kst33009_141,
  author       = {Adriaansens, M. A. M. and Harbers, M. G. J. and Heijnen, V. L. W. A. and {de Jonge}, H. M. and Dijkgraaf, R. H.},
  title        = {Investeringen in ondernemingsklimaat microchipsector},
  howpublished = {Kamerstukken II 2023/24, 33009 en 32637, nr. 141, with annexed letter to ASML (2024D12374)},
  year         = {2024},
  month        = mar,
  note         = {Dated 28 March 2024},
  url          = {https://zoek.officielebekendmakingen.nl/kst-33009-141.html}
}

@misc{semiconvisie2026,
  author       = {Herbert, H. G. and {Semicon Board NL}},
  title        = {Semicon Visie 2035},
  howpublished = {Kamerstukken II 2025/26, 29826, nr. 281 and annex},
  year         = {2026},
  month        = apr,
  note         = {Letter dated 1 April 2026, published 3 April 2026},
  url          = {https://zoek.officielebekendmakingen.nl/kst-29826-281.html}
}

@misc{kst37020xvii11,
  author       = {Bamenga, M. and Lohman, J. and Maes, N.},
  title        = {Motie van het lid {Bamenga} c.s. over de evaluatie van de {Europese} Dualuseverordening benutten om binnen de {EU} aan te sturen op harmonisatie van exportcontrole},
  howpublished = {Kamerstukken II 2026/27, 37020-XVII, nr. 11; adopted 13 October 2026, 110--40},
  year         = {2026},
  url          = {https://www.tweedekamer.nl/kamerstukken/moties/detail?id=2026Z21071&did=2026D48603}
}

@misc{ahtk20252026_1903,
  author       = {Sjoerdsma, S.},
  title        = {Antwoord op vragen van het lid {Hoogeveen} over de {Amerikaanse} {MATCH} {Act} en de gevolgen daarvan voor {ASML}},
  howpublished = {Aanhangsel Handelingen II 2025/26, nr. 1903},
  year         = {2026},
  month        = may,
  url          = {https://zoek.officielebekendmakingen.nl/ah-tk-20252026-1903.html}
}

@misc{ahtk20252026_2251,
  author       = {Sjoerdsma, S.},
  title        = {Antwoord op vragen van de leden {B\"uhler} en {Lohman} over exportrestricties voor {ASML}},
  howpublished = {Aanhangsel Handelingen II 2025/26, nr. 2251},
  year         = {2026},
  month        = jun,
  url          = {https://zoek.officielebekendmakingen.nl/ah-tk-20252026-2251.html}
}

@misc{ahtk20252026_2526,
  author       = {Sjoerdsma, S.},
  title        = {Antwoord op vragen van het lid {Hoogeveen} over het bericht dat de {Verenigde} {Staten} {ASML} beschuldigen van de verkoop van {EUV}-technologie aan {China}},
  howpublished = {Aanhangsel Handelingen II 2025/26, nr. 2526},
  year         = {2026},
  month        = jul,
  url          = {https://zoek.officielebekendmakingen.nl/ah-tk-20252026-2526.html}
}

@misc{kst32637_717,
  author       = {Karremans, V. P. G.},
  title        = {Ontwikkelingen {Nexperia}},
  howpublished = {Kamerstukken II 2025/26, 32637, nr. 717},
  year         = {2025},
  month        = nov,
  note         = {Dated 19 November 2025},
  url          = {https://zoek.officielebekendmakingen.nl/kst-32637-717.html}
}

@misc{stcrt2025_38653,
  author       = {{Staatssecretaris van Buitenlandse Zaken}},
  title        = {Regeling van 20 november 2025, nr. {BZ2520952}, houdende intrekking van de Regeling aanvullende controlemaatregelen op de Verordening producten voor tweeërlei gebruik en de wijziging van de Regeling geavanceerde productieapparatuur voor halfgeleiders},
  howpublished = {Staatscourant 2025, 38653},
  year         = {2025},
  url          = {https://zoek.officielebekendmakingen.nl/stcrt-2025-38653.html}
}

@techreport{pew2026usimage,
  author      = {{Pew Research Center}},
  title       = {Spring 2026 Global Attitudes Survey: {U.S.} Image Topline},
  institution = {Pew Research Center},
  address     = {Washington, DC},
  year        = {2026},
  month       = jun,
  note        = {Released 23 June 2026},
  url         = {https://www.pewresearch.org/wp-content/uploads/sites/20/2026/06/pg_2026.06.23_us-image-2026_topline.pdf}
}

@techreport{ecfr2026homealone,
  author      = {{European Council on Foreign Relations}},
  title       = {Home Alone: Europeans Are Ready to Defend Themselves},
  institution = {European Council on Foreign Relations},
  type        = {Policy Brief},
  number      = {ECFR/640},
  year        = {2026},
  month       = jun,
  url         = {https://ecfr.eu/wp-content/uploads/2026/06/Home-alone-Europeans-are-ready-to-defend-themselves-v3.pdf}
}
```
