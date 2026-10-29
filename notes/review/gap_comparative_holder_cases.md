# Out-of-sample holders (Japan, Korea, Taiwan/TSMC) and US control precedents. Fact-checked gap memo (as of 29 October 2026)

Strand: gap_comparative_holder_cases. Supplies the out-of-sample rows for the structured comparison in Section 7 (notes/model_design_v2.md, Section 9) and tests predictions (a) to (d) against holders other than the Netherlands: (a) leverage equals the exit premium; (b) hedging is policed by flow jurisdiction rather than linkage (Proposition 2(f)); (c) the patron pays in revocable kind; (d) preventive control (Proposition 4).

## How this was checked, and its limits

The shared WebSearch budget for this turn was exhausted before this check began (the first query was refused), so nothing below rests on a search-engine result. Every item was checked by retrieving the document itself:

- govinfo and the Federal Register API: 85 FR 29849, 85 FR 51596, 89 FR 96790, 90 FR 5298, 90 FR 42321, 90 FR 43535 (EO 14345), 91 FR 2443 (Proclamation 11002); H.R. 8170 as introduced.
- SEC EDGAR: SK hynix 424B4 prospectus (filed 10 July 2026); TSMC 20-F for FY2025 (filed 16 April 2026); US Steel 8-Ks of 16 and 18 June 2025; MP Materials 8-K of 10 July 2025 (located through the EDGAR submissions API); Lithium Americas 8-K of 1 October 2025; ASML Q3 2026 6-K. Filing dates were read from the EDGAR index pages.
- Primary pages fetched directly: White House (US-ROK fact sheet; US-Japan minerals framework), Intel, TSMC newsroom (three releases), xLight (two releases), Rep. Baumgartner, CFR (Teer), CSIS (Govella), GMF (Glaser and Lan), TNW, Al Jazeera, Fortune (AP), Malay Mail (Reuters), CNN, ArentFox Schiff, The Standard (Reuters).
- MOFCOM: Announcements No. 11, 12, 27 and 28 of 2026, read in Chinese with the English entity names in the annexes.
- Japanese Diet record API (kokkai.ndl.go.jp): House of Representatives Budget Committee, 7 November 2025, speeches 184 to 192.
- Crossref, Semantic Scholar and OSF records retrieved by DOI or identifier (not by search); the Army War College landing page for McKinney and Harris.

Access problems. Reuters, AP, Bloomberg, WSJ, NHK (the cited URL returns 404), Taylor and Francis, the Congress.gov API (rate limit) and the MP Materials investor site (403) could not be read. One attempt to fetch Reuters and AP pages from the shell was refused by the session's permission system and was not retried. Claims that rest only on those outlets are marked U (reported, not opened). The HFAC vote on MATCH and the ASML Q3 2026 regional split were verified in earlier strands (asml_facts.md, gap_servicing_time_to_pain.md) from Congress.gov and the ASML 6-K, and are carried over. Wikipedia was used only to locate references.

## Verdict in brief

The memo's architecture holds. Of its 41 facts, 30 are verified as stated, 7 need correction and 4 remain unverifiable; the table below also adds 10 new rows. Of its 31 citations, 23 are verified, 8 are corrected and none is fabricated or mischaracterized beyond repair. The corrections that matter for the model:

1. **Japan is evidence about punishing security alignment, not export-control alignment.** The trigger for China's 2025 to 2026 measures was Takaichi's statement on a Taiwan contingency (Diet record, 7 November 2025), not Japan's 2023 equipment controls. The four MOFCOM announcements list 80 Japanese entities: defence units of MHI, IHI, Kawasaki, NEC, Fujitsu and Mitsubishi Electric, JAXA, defence research institutes, and a watch list that includes TDK, Mitsubishi Materials, Nitto Denko, ENEOS and Subaru. None is a maker of chipmaking equipment or photoresists. The memo's proposal to give China a positive g_r is right for the security channel. It does not show that China punishes a holder for aligning on the chokepoint itself.
2. **The US control precedents are stronger than reported.** The MP Materials 8-K gives the Department of Defense consent rights over any sale of 15% or more of voting stock or of the project company, over issuing more than 14.9% of common stock to persons from non-permitted jurisdictions and over non-US-citizen board nominees, and it bars sales to "Restricted Buyers". That is control over ownership, exit and customers, close to what Europe 2031 has Washington demand of ASML. Like the other precedents, it attaches to a US-sited asset the patron finances.
3. **The Lithium Americas deal is weaker than reported.** It is a "non-binding agreement in principle"; the JV warrants are for a "non-voting, non-transferable" 5% economic interest; governance runs only through a board observer.
4. **The US Steel golden share was "to be issued" subject to regulatory approvals** as of 18 June 2025. The rights cover "non-ordinary course matters ... including relating to governance, domestic production and trade matters"; no consent list is public in the filings checked.
5. **Pax Silica.** On 25 June 2026 the EU was "set to join", with permanent representatives expected to authorise the Commission; it had not joined. Greece, Finland and Sweden had signed individually. The Netherlands is not named as a signatory. "Colonise" is TNW's paraphrase of France's framing, not a quotation. Whether the EU joined later is unverified.
6. **Tariff promises.** Proclamation 11002 says the President "may consider" broader tariffs "as well as an accompanying tariff offset program"; it promises nothing. After the February 2026 Supreme Court ruling against the IEEPA tariffs, TSMC reports a replacement tariff under Section 122 and two Section 301 investigations (March 2026) that include Taiwan. The memo's "shifted to Section 232" is incomplete.
7. **Korea's investment vehicle.** The fact sheet says the USD 150bn shipbuilding investment is "approved by the United States". It does not say that Washington selects projects under the USD 200bn MOU, which had not been signed. US project selection is verified for Japan only (EO 14345; CSIS).
8. **Security bundles exist for Japan too.** EO 14345 records that "Japan will purchase United States-made commercial aircraft, as well as United States defense equipment." The claim that linkage ran on a separate track from export controls survives, but both Asian trade packages bundle defence procurement.
9. **The silicon-shield literature is more skeptical than the memo implies.** Weil, Gottwald and Taube (2025) conclude that the shield "is largely a hopeful narrative" lacking rigorous grounding. Their paper does not anchor the s_B(V) channel; it is a rival account.
10. **Two open items are now resolved, as reported.** Reuters (30 December 2025, two sources) reports that Samsung as well as SK hynix received an annual licence for 2026. ArentFox Schiff quotes the BIS release of 29 August 2025: BIS "intends to grant export license applications to allow former VEU participants to operate their existing fabs in China" but does not "intend to grant licenses to expand capacity or upgrade technology."

## Corrected synthesis

The Asian holders give the paper the variation across holders that an IO referee will ask for, and they mostly confirm the model. In each case Washington polices the holder's China hedge with a rule aimed at the specific flow. It pays in exemptions that it can withdraw at the next renewal. No holder extracts rent. Three readings in the memo need repair. Japan shows China punishing a security statement, not a chokepoint holder's export-control alignment. The US control precedents include one deal (MP Materials) with real consent rights over ownership and customers. And several descriptions of sources overstate what the documents say.

**Flow jurisdiction, not linkage.** Against Huawei's use of foreign foundries, of which TSMC was the largest, BIS extended the foreign direct product rule in May and August 2020 (85 FR 29849; 85 FR 51596). The rules name Huawei, not TSMC; their incidence fell on TSMC's output. In January 2025 BIS added due-diligence duties for foundries and assembly and test firms (90 FR 5298). Against the China fabs of Samsung and SK hynix, BIS removed validated end-user (VEU) status (90 FR 42321; filed 29 August 2025, published 2 September, effective 31 December 2025) and estimated "an additional 1,000 license applications annually". The BIS release, as quoted by ArentFox Schiff, would license operation of existing fabs but not expansion or upgrades. TSMC's Nanjing VEU expired on the same date. Against allied toolmakers, the pending MATCH Act (H.R. 8170, as introduced) would require US agencies, 150 days after enactment, either to certify that every "allied supplier country" has countrywide controls and a policy of denial for covered facilities, or to extend US jurisdiction over those countries' equipment, including items with "more than zero percent de minimis" US content, and to deny licences for "all servicing of any applicable item located in any covered facility". The bill names no country; its sponsor's release quotes Chris McGuire that chipmaking equipment is "the largest export from the Netherlands to China, the second largest from Japan".

Security linkage ran on a separate track. The US-ROK fact sheet of 13 November 2025 bundles a 15% tariff ceiling, USD 350bn of investment (USD 150bn in shipbuilding plus USD 200bn under a strategic investment MOU, capped at USD 20bn a year), defence spending of 3.5% of GDP "as soon as possible", USD 25bn of US arms purchases by 2030, USD 33bn of support for US Forces Korea, US support for a process leading to Korean civil enrichment and reprocessing, and US approval of nuclear-powered attack submarines. It does not mention export controls or China. EO 14345 for Japan likewise records purchases of "United States defense equipment" alongside a USD 550bn investment pledge and contains no semiconductor commitment. We found no public document that ties the VEU revocation or Japan's controls to an alliance threat. That is what Proposition 2(f) predicts when flow jurisdiction is cheap. The evidence is an absence in public documents, so it cannot exclude private linkage. The January 2023 Washington talks that produced the Dutch-Japanese understanding were led by the national security adviser and also covered Ukraine (AP, via Fortune); Kirby declined to say whether there was a deal.

**Payment in revocable kind.** The currency of US compensation is the revocable exemption. The December 2024 rule (89 FR 96790) created Supplement No. 4 to Part 742: 33 destinations, comprising 25 EU member states (all but Cyprus and Malta), Japan, the UK, Canada, Australia, New Zealand, Norway, Switzerland and Iceland. Exporters there are excluded from the new chipmaking-equipment direct product licence requirements, and the Footnote 5 rule "does not generally apply" to them because their governments belong to the regimes and "have the authority to control key SME items of concern". South Korea and Taiwan are not listed. BIS can amend the list by rule. When VEU status lapsed, BIS moved to annual licences. SK hynix reports "an annual approval mechanism under which we are required to submit yearly plans" and a licence for 2026 granted in December 2025. TSMC reports the same for Nanjing and warns there is "no assurance that this annual export license will not be terminated". Reuters reports that Samsung received one too. CHIPS money comes with similar strings: SK hynix lists a ban on certain new high-tech investments in China "for at least a decade" and "sharing of certain excess profits with the U.S. Government" among the conditions. Each instrument pays and enforces at once, because every renewal date is a cheap point of withdrawal.

**Japan: coercion, but of a different act.** On 7 November 2025 Prime Minister Takaichi told the House of Representatives Budget Committee that a Taiwan contingency involving warships and the use of force "could, however one looks at it, be a case that becomes a survival-threatening situation" (our translation of the Diet record; she added that this did not mean an immediate determination). China then:
- issued a travel advisory (mid-November) and told Japan it would halt seafood imports (19 November, per Kyodo; the foreign ministry said there was "no market");
- banned exports of dual-use items for "end-user purposes that could enhance Japan's military capabilities" (January 2026, CFR);
- opened an anti-dumping case on dichlorosilane in January and imposed deposits of up to 99.2% in September 2026 (Bloomberg, reported);
- placed 20 entities on its export-control list and 20 on its watch list on 24 February 2026, and another 20 and 20 on 29 June 2026 (MOFCOM Announcements No. 11, 12, 27, 28);
- cut "several rare earths and gallium to Tokyo to near zero throughout 2026" (CFR, 21 September 2026).

We found no US compensation for any of this. The US-Japan critical minerals framework was signed on 28 October 2025, before the remarks, and is not legally binding. CFR writes that "Top U.S. and European leaders have not publicly condemned China for its specific economic coercion against Japan". Ambassador Glass and the State Department spokesperson did reaffirm the treaty commitment, and the WSJ and Reuters reported that Trump urged Takaichi to avoid escalation, which Tokyo denied; none of these reports was opened. With a deeply negative premium, the slack absorbs r, as the model predicts.

The memo reads this as China punishing alignment on the equilibrium path. The record supports a narrower reading. The trigger was a declaratory statement on Taiwan, a core interest, not Japan's 2023 chipmaking-equipment controls. The 80 listed entities are defence-linked firms and institutes plus civilian firms that China says it cannot verify (TDK, Mitsubishi Materials, Nitto Denko, ENEOS, Subaru, the Institute of Science Tokyo). None is Tokyo Electron, Nikon, Canon, JSR, TOK or Shin-Etsu. The one chip-related step, the dichlorosilane case, restricts Chinese imports from Japan rather than Japan's sales of the inputs China needs. So the case gives China a positive ex post value from punishing security alignment on Taiwan, with a plausible demonstration motive (CFR: "Beijing making an example of Japan"; an academic quoted by Al Jazeera says the goal is "showing other countries that violating Bejing's defined red lines on Taiwan risks long-term economic pain"). It says nothing about punishing a holder for aligning on a chokepoint China depends on. For Europe the security channel is already live: CFR reports that in July 2026 China placed Rheinmetall and 13 other European entities, "including a Dutch shipbuilding company, a research lab, and a technical university", on its export-control list. Together with Nexperia (gap_european_cost_parameters.md, item 11), the record no longer supports r_A = 0. But the model should separate the two channels.

**Korea: policing the hedge.** Korea is the cleanest case of prediction (b). The China fabs depend on US-origin tools. BIS replaced a durable authorization with a one-year licence while Washington negotiated the trade and security package separately. The timing is suggestive but not proof of a quid pro quo: the revocation was announced on 29 August 2025, the fact sheet came on 13 November, and the 2026 licences followed in December. China is a large exposure: sales subsidiaries located in China took 24.3% of SK hynix revenue in Q1 2026 (19.7% in 2025), against 64.7% for US-located subsidiaries. Korea and Taiwan together took 63% of ASML's net system sales in Q3 2026 (31% and 32%).

**Taiwan: relocation instead of shares.** TSMC's US commitment grew from about USD 12bn (May 2020, one 5nm fab, 2021 to 2029) to "more than US$65 billion" (April 2024) and USD 165bn (March 2025). The April 2024 CHIPS terms were a "non-binding preliminary memorandum of terms"; the final agreements followed in November 2024 (TSMC 20-F). The memo attributes the growth to AI demand raising the value of leading-edge capacity. That is one reading. Tariff pressure is a rival: GMF reports that more than 80% of Taiwanese respondents (Global Views Research, March 2025) saw the investments as "a result of US pressure", the provisional US tariff on Taiwan was 20% against 15% for Japan and Korea, and the Section 232 investigation into semiconductors opened in April 2025. Proclamation 11002 (14 January 2026) imposed 25% on certain advanced chips, exempting imports for US data centres, and said broader tariffs might come with "an accompanying tariff offset program to incentivize domestic manufacturing". TSMC reports that the January 2026 US-Taiwan agreement caps reciprocal tariffs at 15% and "grants preferential Section 232 treatment for Taiwanese semiconductor producers investing in U.S. manufacturing capacity". Lutnick's reported "50-50" proposal fits this pattern but was not verified. A patron that can relocate production does not need shares. The Europe 2031 holding-company ultimatum is therefore plausible only if relocating EUV production and servicing is infeasible, which the paper should argue from Zeiss optics and ASML know-how rather than assume. xLight is relevant here: Commerce made its first CHIPS R&D award under the current administration (USD 150m, LOI 1 December 2025, final 2 June 2026) to a US firm building free-electron-laser EUV sources at Albany. On our reading it is at most a long-run substitute for one ASML module (the light source), not for the scanner.

**Control on US soil.** We found no verified US proposal for equity or a golden share in ASML or any foreign chipmaking-equipment firm; because search was unavailable, this is an absence in the sources we could read, not a finding. The control rights Washington did take are over US-sited assets:
- US Steel: a Golden Share (one share of Class G preferred) "to be issued" to the US Government under a National Security Agreement with Nippon Steel (13 June 2025), with rights over "non-ordinary course matters ... including relating to governance, domestic production and trade matters", plus about USD 11bn of investment by 2028.
- Intel: a passive 9.9% stake (433.3m shares at USD 20.47, funded by USD 5.7bn of unpaid CHIPS grants and USD 3.2bn of Secure Enclave funds), "no Board representation or other governance or information rights", and a five-year warrant for 5% more, exercisable only if Intel "ceases to own at least 51% of the foundry business".
- MP Materials: USD 400m of convertible preferred plus a warrant (15% as converted), a 10-year NdPr price floor of USD 110/kg, a 10-year offtake of "the entire amount of magnets produced at the 10X Facility", a USD 150m loan, and consent rights over a sale of control, foreign ownership above 14.9%, non-US-citizen board nominees and sales to "Restricted Buyers".
- Lithium Americas (Vancouver): a non-binding agreement in principle giving DOE warrants for 5% of the company and a non-voting 5% economic interest in the Thacker Pass JV, a board observer and a USD 182m deferral of debt service.

The precedents span passive ownership (Intel) to consent rights over exit, ownership and customers (MP, US Steel). The strongest rights come where the patron pays most (MP: price floor, offtake, equity, loan) or approves a foreign takeover (US Steel). That supports Proposition 4's logic of paying for enforceable control, and it shows the patron prefers forms whose enforceability does not depend on a foreign government. The Europe 2031 holding company, a US controlling vote in a firm on Dutch soil, has no precedent. Its nearest analogues are the US Steel golden share (control as the price of an ally's acquisition of a US asset), MP's consent rights (control bought with a floor and offtake) and the relocation pressure on TSMC.

**Silicon shield.** The scholarship disagrees on what the shield is and what relocation does to it. Weil, Gottwald and Taube (2025) conclude that the shield "is largely a hopeful narrative" rather than a credible deterrent. Liao (2025, preprint) argues that "decoupling" and "reshoring" treat "physical relocation as a proxy for strategic autonomy" and stresses institutional absorptive capacity. Kochumon and Josukutty (2026) treat the shield as a balancer in the Taiwan-US-China triangle (title level). McKinney and Harris (2021) propose a "tailored deterrence package" beyond fighting or abandoning; the TSMC-denial element was not checked against the full text. The model takes a side by letting s_B rise with V. The Taiwanese public reads it the same way: per GMF, a majority think US production weakens the shield. The paper should present s_B'(V) > 0 as a contested assumption and cite Weil et al. as the skeptical view.

**Coalition.** Japan and Korea have signed Pax Silica, the US-led initiative launched in December 2025 to coordinate AI chip supply chains and export controls. Japan has accepted an investment vehicle in which Washington selects projects. Both depend on exemptions renewed by rule (Japan) or annually (Korea). They are poor partners for a bloc that bargains against the United States, as the scenario's 2028 episode implies. They are natural partners for insurance against Chinese coercion, along the lines of Cha (2023) and Teer's allied compensation mechanism (CFR, framed for Washington and Brussels). The EU's own position is in motion: on 25 June 2026 it was set to join Pax Silica as a bloc, three member states had already signed, and France objected. The paper should make the coalition's purpose a parameter and show that only the insurance version is stable.

**Still unverified.** Japan's official response to MATCH; the wording of Lutnick's 50-50 proposal and Taiwan's reply; Taiwan's N-2 rule; Taiwan's June 2025 listing of Huawei and SMIC; the dichlorosilane measures and the zero terbium and dysprosium exports (Bloomberg and Reuters, not opened); the US reactions of November 2025; any equity component in xLight's award; and whether the EU formally joined Pax Silica.

## Corrected comparison table

| Parameter | Netherlands/ASML (reference) | Japan (TEL, Nikon, Canon; JSR, TOK, Shin-Etsu) | Korea (Samsung, SK hynix) | Taiwan (TSMC) | US control precedents |
|---|---|---|---|---|---|
| Chokepoint | EUV monopoly; DUVi; servicing | Coater/developers, etch, DUV lithography, photoresists (shares not verified) | Memory incl. HBM; China fabs as the hedge; 31% of ASML Q3 2026 system sales | Leading-edge foundry; 32% of ASML Q3 2026 system sales | Intel foundry; MP magnets; US Steel; Thacker Pass lithium; xLight EUV source |
| kappa: dependence and conditionality signals | NATO dependence (security strand) | Treaty ally; Article V and Senkakus reaffirmed by ambassador and State Department (reported); no top-level US condemnation of China's coercion (CFR); Trump reportedly urged restraint (reported, denied by Tokyo); EO 14345 includes US defence equipment purchases | Very high and bundled: fact sheet links tariffs, USD 350bn, 3.5% of GDP, USD 25bn arms, USD 33bn USFK support, enrichment process, submarine approval | Highest dependence, no treaty; shield caps credible conditionality if s_B'(V) > 0 (contested); >80% see TSMC US investment as US pressure | n.a. (CFIUS, CHIPS, DoD and DOE finance as levers) |
| theta: US jurisdiction over flows | FDPR, US persons; Supp. No. 4 excludes exports from NL; MATCH would reach servicing | Supp. No. 4 (Dec 2024): applied theta low, latent high; MATCH covers every "allied supplier country", zero de minimis, servicing denial | Exercised: VEU revoked (90 FR 42321); operate but no expansion or upgrade (BIS release as quoted); annual licences | Exercised: Huawei FDPR (2020) reached TSMC output; foundry due diligence (Jan 2025); Nanjing annual licence | Ownership and contract rights, not the EAR |
| r: Chinese coercion; omega: China's offer | Nexperia (Oct 2025); rare-earth suspension to 10 Nov 2026; China about 20% of ASML 2026 sales (guidance) | Very high, executed, triggered by a Taiwan statement: travel advisory, seafood, dual-use ban for military end uses (Jan 2026), 40 + 40 listings (no SME or resist makers), dichlorosilane (reported), rare earths and gallium near zero | Latent: China fabs as hostages; China-located sales subsidiaries 24.3% of SK hynix Q1 2026 revenue; THAAD precedent (Lim and Ferguson) | Military pressure; no credible economic offer | n.a. |
| Compensation received | Supp. No. 4; no cash | Supp. No. 4 (revocable by rule); 15% tariff rule (EO 14345; IEEPA basis struck down Feb 2026); non-binding minerals framework (before the coercion); nothing found for the 2026 coercion | Annual licences for 2026 (SK hynix filing; Samsung per Reuters); submarine approval; tariff ceilings; semiconductors and SME "no less favorable" clause | Nanjing annual licence; CHIPS up to USD 6.6bn plus 5bn loans; Section 232 preference for firms investing in US capacity (Jan 2026) | Patron pays (grants converted to equity, preferred stock, loans, price floor, offtake) for control rights |
| What the holder paid | DUVi controls 2023-24; servicing licences | USD 550bn with US project selection; 50/50 then 90/10 (CSIS) | USD 350bn (USD 150bn shipbuilding "approved by the United States"; USD 200bn MOU, max 20bn a year); defence commitments | USD 165bn TSMC US programme; Huawei/SMIC listing (June 2025, reported) | Firms accept a golden share, warrants, consent rights, price-linked sharing |
| Timing vs. outside option | Controls phased in as China's share spiked | Exemption followed 2023 alignment; Nov 2025 coercion brought no US payment | Revocation announced 29 Aug 2025 during investment talks; licences in Dec 2025, after the 13 Nov fact sheet | Demands grew 2020 to 2025 with AI value and tariff pressure; Section 232 preference (Jan 2026) | Rights taken where exit or foreign control was feared (Intel foundry warrant; US Steel; MP fundamental events) |
| (a) leverage = exit premium | Holds | Holds (no rent despite large r) | Holds | Holds | n.a. |
| (b) flow jurisdiction, not linkage | Holds | Holds prospectively (MATCH) | Holds strongly | Holds | n.a. |
| (c) revocable in-kind payment | Holds | Holds | Holds strongly | Holds | n.a. |
| (d) preventive control | Scenario only | Not observed | Not observed (US approval of Korean shipbuilding investment instead) | Partial: relocation as control; 50-50 and N-2 unverified | Holds on US soil only; strongest at MP and US Steel |
| China punishes alignment on path? | Nexperia (response to Dutch Wbg order) | Yes, for a security statement; SME firms spared | Not in 2025-26 (Hanwha unverified) | n.a. | n.a. |
| Availability for a middle-power coalition | Proposer | Low against the US (Pax Silica, revocable exemption); high for anti-coercion insurance | Low against the US; moderate for insurance | Very low | n.a. |

## Verified facts table

Verdicts: V = verified as stated; C = verified after correction (corrected wording shown); U = unverifiable from sources we could open; F = false.

| # | Claim (corrected where needed) | Verdict | Source (date) | Note |
|---|---|---|---|---|
| J1 | AP (via Fortune): Japan and the Netherlands "have agreed to a deal with the U.S. to restrict China's access to materials used to make advanced computer chips", per one unnamed person; not formally announced; White House declined to comment. Kirby confirmed Sullivan-led talks covering emerging technologies and Ukraine but "declined to say whether there was a deal". ASML knew no details. | V | https://fortune.com/2023/01/30/biden-china-chips-export-controls-netherlands-dutch-japanese (30 Jan 2023) | Source spoke on Sunday 29 Jan; talks Friday 27 Jan. No public text exists. |
| J2 | "The Government of Japan added ArF-wet lithography equipment and other advanced semiconductor manufacturing equipment to its control list for all regions on July 23, 2023." | V | https://www.govinfo.gov/content/pkg/FR-2024-12-05/html/2024-28270.htm (89 FR 96790, fn. 1; 5 Dec 2024) | The 23-item count from METI's May 2023 release is unverified. |
| J3 | 89 FR 96790-96830 (published 5 Dec 2024, effective 2 Dec 2024) creates Supplement No. 4 to Part 742 with 33 destinations: 25 EU states (not Cyprus or Malta), Japan, UK, Canada, Australia, New Zealand, Norway, Switzerland, Iceland. Korea and Taiwan are not listed. The FN5 FDP rule "does not generally apply" to them; their governments "have the authority to control key SME items of concern". | V | https://www.govinfo.gov/content/pkg/FR-2024-12-05/html/2024-28270.htm (5 Dec 2024) | Exclusion is from new SME licence requirements on exports from listed countries; a Footnote 5 requirement remains for listed-country firms exporting from outside A:5 (gap_servicing_time_to_pain.md). Already in refs.bib as bis2024fdpr. |
| J4 | EO 14345 (4 Sep 2025; 90 FR 43535-43538, 9 Sep 2025): 15% all-in tariff rule; "the Government of Japan has agreed to invest $550 billion in the United States", investments "selected by the United States Government"; "Should Japan fail to implement its commitments under the Agreement, I may modify this order". Japan will also purchase "United States defense equipment". No semiconductor commitment. | V | https://www.govinfo.gov/content/pkg/FR-2025-09-09/html/2025-17389.htm (9 Sep 2025) | Defence-purchase clause added; relevant to the linkage claim. |
| J5 | CSIS on the US-Japan MOU: Commerce-chaired investment committee; Japan funds within 45 days; refusing forfeits distributions and may bring higher tariffs; SPVs pay 50/50 until a "deemed allocation amount", then 90/10; investments before 19 Jan 2029. Some elements are "reportedly" in the MOU. | V | https://www.csis.org/analysis/new-documents-reveal-next-steps-us-japan-trade-deal (9 Sep 2025) | Author Kristi Govella. |
| J6 | US-Japan critical minerals framework, signed in Tokyo on 28 Oct 2025 by Trump and Takaichi: financial support for selected projects "within six months"; will "consider a mutually complementary stockpiling arrangement"; Rapid Response Group under the US Energy Secretary and Japan's METI minister; "does not constitute or create any legally binding or enforceable obligations". | V | https://www.whitehouse.gov/briefings-statements/2025/10/united-states-japan-framework-for-securing-the-supply-of-critical-minerals-and-rare-earths-through-mining-and-processing/ (Oct 2025) | Does not mention China. Predates the Takaichi remarks. |
| J7 | Takaichi, House of Representatives Budget Committee, 7 Nov 2025 (speech 188): if a Taiwan contingency "uses warships and also involves the use of force, I believe this is, however one looks at it, a case that could become a survival-threatening situation" (our translation). In speech 192 she added that this did not mean immediately determining one and using force. | C | https://kokkai.ndl.go.jp/txt/121905261X00220251107/188 (7 Nov 2025) | Primary source replaces Wikipedia. |
| J8 | China issued a travel advisory in mid-November 2025 ("last week" per CNN on 19 Nov) and on 19 Nov the foreign ministry said there would be "no market" for Japanese seafood; Kyodo reported that China informed Japan through diplomatic channels it would temporarily halt seafood imports. | C | https://www.cnn.com/2025/11/19/china/japan-china-taiwan-dispute-intl-hnk (19 Nov 2025) | The formal halt rests on Kyodo (not opened); CNN describes the "threat of a new seafood ban". |
| J9 | MOFCOM "banned the export of all items on this dual-use list to Japan for any 'end-user purposes that could enhance Japan's military capabilities' in January 2026"; the list "contains a wide variety of essential industrial gases". | V | https://www.cfr.org/reports/dismantling-chinas-supply-chain-weapon (21 Sep 2026) | The 6 Jan date comes from a Bloomberg headline not opened. |
| J10 | Dichlorosilane anti-dumping probe on imports from Japan (7 Jan 2026) and cash deposits of up to 99.2% (8 Sep 2026). | U | https://www.bloomberg.com/news/articles/2026-09-08/china-hits-japan-with-anti-dumping-measures-on-chip-chemical (8 Sep 2026) | Bloomberg not opened; located via Wikipedia. |
| J11 | MOFCOM Announcements No. 11 and No. 12 of 2026 (24 Feb 2026): 20 Japanese entities on the export-control list (led by MHI Shipbuilding; includes IHI, Kawasaki, NEC and Fujitsu defence units, the National Defense Academy and JAXA) and 20 on the watch list (incl. Subaru, ENEOS, Institute of Science Tokyo, Mitsubishi Materials, Sumitomo Heavy Industries, TDK, Nitto Denko). | V | https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_b5159a773124428a9813884015d1b8b3.html ; https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_bac18400512d408a8d4c2f964e36ac11.html (24 Feb 2026) | The memo's NHK URL returns 404; primary source used. Watch-list exports to Japanese military end uses "不予批准" (will not be approved). |
| J12 | MOFCOM Announcements No. 27 and 28 (29 Jun 2026): 20 more on the control list (National Institute for Defense Studies, Ground, Naval and Air Systems Research Centers, Mitsubishi Precision, MHI Logitec, Kawajyu Gifu Manufacturing and others) and 20 on the watch list (Mitsui E&S, Terra Drone, Hitachi Advanced Systems, OKI units and others). Spokesperson cited "remilitarisation". | V | https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_df87be1437044874a35f85cf6e076f3d.html ; https://www.aljazeera.com/economy/2026/6/29/china-slaps-export-controls-on-dozens-of-japanese-entities (29 Jun 2026) | Spelling per MOFCOM: "MHI Logitec". |
| J13 | None of the 80 entities in the four announcements is Tokyo Electron, Nikon, Canon, JSR, TOK or Shin-Etsu. | V | MOFCOM annexes as in J11 and J12 | New. China's listings spared Japan's chipmaking-equipment and photoresist firms. |
| J14 | Chinese exports of terbium and dysprosium oxide to Japan were zero from Nov 2025 to June 2026, with one small yttrium oxide shipment. | U | https://www.reuters.com/world/asia-pacific/chinas-rare-earths-curbs-extend-pressure-supply-japan-2026-06-21/ (22 Jun 2026) | Reuters not opened. Consistent with CFR (J15). |
| J15 | CFR: China "has reduced supplies of several rare earths and gallium to Tokyo to near zero throughout 2026", ostensibly punishment for Takaichi's statement, despite Trump's post-Busan assurances; "Top U.S. and European leaders have not publicly condemned China for its specific economic coercion against Japan"; "Beijing making an example of Japan"; proposes "an allied compensation mechanism" so China cannot "split individual allies from the coalition". | V | https://www.cfr.org/reports/dismantling-chinas-supply-chain-weapon (21 Sep 2026) | Title is "Dismantling China's Supply-Chain Weapon: A Transatlantic Strategy for Critical Minerals" (Joris Teer). |
| J16 | CFR: in July 2026 China added Rheinmetall and 13 other European entities, "including a Dutch shipbuilding company, a research lab, and a technical university", to its export-control list. | V | https://www.cfr.org/reports/dismantling-chinas-supply-chain-weapon (21 Sep 2026) | New. Entity names and trigger not verified (MOFCOM announcement not located without search). |
| J17 | US reactions: Glass called the seafood ban economic coercion and said the US "has Japan's back" (20 Nov 2025); State Department reaffirmed the treaty commitment; WSJ (26 Nov) and Reuters (27 Nov) reported Trump urged Takaichi to avoid escalation; Tokyo denied. | U | https://www.bloomberg.com/news/articles/2025-11-20/the-us-has-japan-s-back-in-any-dispute-with-china-glass-says (20 Nov 2025) | None opened. Wikipedia also cites the FT as saying the US gave little public support beyond Glass's statements. |
| J18 | Al Jazeera quotes Naoise McDonagh (Edith Cowan University): "there is also a broader goal of showing other countries that violating Bejing's defined red lines on Taiwan risks long-term economic pain". | V | https://www.aljazeera.com/economy/2026/6/29/china-slaps-export-controls-on-dozens-of-japanese-entities (29 Jun 2026) | New. Expert opinion, not evidence of intent. |
| J19 | Japan Times (7 Oct 2026, reported): China's foreign minister told a Japanese delegation that China would restrict critical-material exports for military use but allow them for civilian purposes. | U | https://www.japantimes.co.jp (7 Oct 2026; exact URL not opened) | New, located via Wikipedia. Suggests the measures persisted into October 2026 under a military/civilian distinction. |
| M1 | H.R. 8170 (introduced 2 Apr 2026, Baumgartner and 10 original cosponsors incl. Moolenaar). "Allied supplier country" = any non-country-of-concern producing covered equipment; covered equipment includes "all deep ultraviolet immersion photolithography machines, through silicon via deposition and etch tools, cryogenic etch equipment, and cobalt deposition equipment". Within 150 days of enactment the covered agency heads must certify allied countrywide controls or list non-implementers; absent certification they must extend US jurisdiction (applicable items include those with "more than zero percent de minimis" US content) and "require a license for all servicing of any applicable item located in any covered facility" with a policy of denial. One waiver of up to 90 days. | C | https://www.congress.gov/119/bills/hr8170/BILLS-119hr8170ih.htm (2 Apr 2026) | The duty falls on US agencies, not on allies. Text is as introduced; the committee substitute was not available. |
| M2 | Baumgartner's release quotes Chris McGuire (CFR): chipmaking equipment is "the largest export from the Netherlands to China, the second largest from Japan, and the third largest from the United States". Sens. Ricketts and Kim are introducing a companion bill. | V | https://baumgartner.house.gov/2026/04/02/baumgartner-introduces-bipartisan-bill-to-tighten-controls-on-sensitive-chipmaking-equipment (2 Apr 2026) | Advocate's statement, not an official statistic. |
| M3 | HFAC ordered H.R. 8170 reported in the nature of a substitute, 36 to 8, on 22 Apr 2026; no later action found. | V | https://www.congress.gov/bill/119th-congress/house-bill/8170/all-actions (22 Apr 2026) | Verified earlier in this project via the Congress.gov API (asml_facts.md row 67); this session hit the API rate limit. |
| M4 | Japan's official response to MATCH. | U | n.a. | Dutch objections are documented in asml_facts.md (13 Apr, 12 May 2026). |
| P1 | Pax Silica, launched by Washington in December 2025, coordinates AI chip supply chains and export controls. By 25 June 2026 the UK, Japan, South Korea, India and Australia had signed; Greece, Finland and Sweden had signed individually; the EU was "set to join", with permanent representatives expected to authorise the Commission. TNW reports that France framed the pact "as an attempt to colonise Europe". | C | https://thenextweb.com/news/eu-pax-silica-ai-chips (25 Jun 2026) | The EU had not joined on that date; "colonise" is a paraphrase. The Netherlands is not named. Later accession unverified. |
| K1 | 90 FR 42321-42322 (filed 29 Aug 2025; published 2 Sep 2025; effective 31 Dec 2025) removes Intel Semiconductor (Dalian), Samsung China Semiconductor and SK hynix Semiconductor (China) from the VEU list; BIS estimates "an additional 1,000 license applications annually". No licensing policy in the rule; TSMC Nanjing not named. | V | https://www.govinfo.gov/content/pkg/FR-2025-09-02/html/2025-16735.htm (2 Sep 2025) | Already in refs.bib as bis2025veu. |
| K2 | BIS release of 29 Aug 2025, as quoted: it "intends to grant export license applications to allow former VEU participants to operate their existing fabs in China" and does not "intend to grant licenses to expand capacity or upgrade technology". TSMC said separately that Nanjing would lose VEU status on the same date. | V | https://www.afslaw.com/perspectives/alerts/bis-revokes-veu-authorizations-foreign-owned-chip-factories-china (15 Sep 2025) | New; resolves an open question. Law-firm quotation of the BIS release. |
| K3 | SK hynix prospectus: one-year BIS authorization in Oct 2022; VEU in Oct 2023; "On August 29, 2025, the BIS announced that our designation as a VEU would be revoked effective December 31, 2025"; "an annual approval mechanism under which we are required to submit yearly plans"; "In December 2025, the BIS granted us an annual license for 2026". | V | https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm (filed 10 Jul 2026) | |
| K4 | Reuters: the US granted Samsung and SK hynix annual licences for their China facilities for 2026 (two people familiar). | V | https://www.thestandard.com.hk/innovation/article/320428/US-approves-Samsung-SK-Hynix-chipmaking-tool-shipments-to-China-for-2026-sources-say (30 Dec 2025) | New; Samsung's licence now reported. Already in refs.bib as reuters2025koreanlicence. |
| K5 | SK hynix prospectus: sales subsidiaries in China 24.3% of revenue in Q1 2026 and 19.7% in 2025 (US-located 64.7% and 68.8%); Indiana: up to USD 458m in CHIPS subsidies and USD 570m in loans; CHIPS conditions include "a ban on certain new, high-tech investments in China or other 'countries of concern' for at least a decade" and "sharing of certain excess profits with the U.S. Government". | V | https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm (filed 10 Jul 2026) | Shares are by location of the sales subsidiary, not end customer. |
| K6 | US-ROK fact sheet (13 Nov 2025), trade: reciprocal tariff at the higher of KORUS/MFN or 15%; Section 232 autos, parts and timber at 15%; for Section 232 tariffs on "semiconductors (including semiconductor manufacturing equipment)", terms "no less favorable than terms that may be offered in a future agreement covering a volume of semiconductor trade at least as large as Korea's"; USD 150bn shipbuilding investment "approved by the United States" plus USD 200bn under an MOU "expected to be signed"; no more than USD 20bn per calendar year. No mention of export controls or China. | V | https://www.whitehouse.gov/fact-sheets/2025/11/joint-fact-sheet-on-president-donald-j-trumps-meeting-with-president-lee-jae-myung/ (13 Nov 2025) | Accurate as stated in the memo's facts. The memo's synthesis, however, says Washington selects the projects; the fact sheet does not say so for the MOU. Already in refs.bib as whitehouse2025korea. |
| K7 | Same fact sheet, security: defence spending to 3.5% of GDP "as soon as possible"; USD 25bn of US military equipment by 2030; USD 33bn of support for USFK; US "supports the process that will lead to the ROK's civil uranium enrichment and spent fuel reprocessing for peaceful uses"; "The United States has given approval for the ROK to build nuclear-powered attack submarines." | V | same (13 Nov 2025) | Enrichment clause added. |
| K8 | ASML Q3 2026 net system sales by ship-to: Taiwan 32%, South Korea 31%, China 23%, US 13%. | V | https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/a2026_10x14xpresentation.htm (14 Oct 2026) | Carried over from gap_servicing_time_to_pain.md row 24; the chart is an image and was not re-read here. |
| T1 | TSMC Arizona announcement: 5nm, 20,000 wafers a month, about USD 12bn "from 2021 to 2029", construction from 2021, production targeted for 2024. | V | https://pr.tsmc.com/english/news/2033 (15 May 2020) | |
| T2 | 85 FR 29849-29863 (published 19 May 2020, effective 15 May 2020) amends General Prohibition Three to reach foreign-produced items for Huawei and its listed affiliates; 85 FR 51596-51629 (published 20 Aug 2020, effective 17 Aug 2020) adds affiliates and revises the rule. | V | https://www.federalregister.gov/documents/2020/05/19/2020-10856 ; https://www.federalregister.gov/documents/2020/08/20/2020-18213 | The rules target Huawei; TSMC is not named. Their incidence fell on foundry output. |
| T3 | TSMC Arizona: a "non-binding preliminary memorandum of terms" for up to USD 6.6bn of direct funding and up to USD 5bn of loans; Phoenix capex "more than US$65 billion"; third fab at "2nm or more advanced processes". Final agreements were signed in November 2024. | V | https://pr.tsmc.com/english/news/3122 (8 Apr 2024); TSMC 20-F FY2025 | Accurate as stated; preliminary status and November 2024 finalization added for context. |
| T4 | BIS foundry due-diligence rule, 90 FR 5298-5321 (published and effective 16 Jan 2025). | V | https://www.federalregister.gov/documents/2025/01/16/2025-00711/implementation-of-additional-due-diligence-measures-for-advanced-computing-integrated-circuits (16 Jan 2025) | |
| T5 | TSMC: "an additional $100 billion" (three fabs, two advanced packaging facilities, an R&D team center) on top of the "ongoing $65 billion"; total USD 165bn. | V | https://pr.tsmc.com/english/news/3210 (4 Mar 2025) | |
| T6 | GMF (Glaser and Lan): Global Views Research (March 2025) finds "a majority" think TSMC's US production "weakens a 'silicon shield'" and "More than 80% of respondents believe that the investments are a result of US pressure"; TPOF: 57.2% say the US is less dependable under Trump; provisional US tariff on Taiwan 20%, against 15% for Japan and Korea. | V | https://www.gmfus.org/news/taiwans-growing-distrust-united-states (18 Aug 2025) | |
| T7 | Taiwan added Huawei and SMIC to its export-control entity list in June 2025. | U | https://apnews.com/article/china-taiwan-huawei-smic-export-restrictions-semiconductor-6f43d0b9f34d39258ca3e3c1406d9055 (Jun 2025) | AP not reachable. |
| T8 | TSMC 20-F: "Although the VEU authorization expired in December 2025, the U.S. Department of Commerce has granted TSMC Nanjing Company Limited ... an annual export license"; "there is no assurance that this annual export license will not be terminated, or we can timely get the license renewed in the future". | V | https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm (filed 16 Apr 2026) | Already in refs.bib as tsmc2026annual. |
| T9 | TSMC 20-F: the January 2026 US-Taiwan agreement would cut reciprocal tariffs on Taiwan to "no more than 15%" and "grants preferential Section 232 treatment for Taiwanese semiconductor producers investing in U.S. manufacturing capacity". The IEEPA tariffs "were declared unlawful by a February 2026 U.S. Supreme Court ruling"; the US then "imposed a replacement tariff under Section 122", and in March 2026 USTR opened two Section 301 investigations "targeting various economies, including Taiwan". The Section 232 semiconductor investigation (April 2025) concluded in December 2025. | V | https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm (filed 16 Apr 2026) | Memo fact accurate; Section 122 and 301 details added. They correct the memo's modeling implication that the US "shifted to Section 232". Dollar terms of the agreement unverified. |
| T10 | Proclamation 11002 (14 Jan 2026; 91 FR 2443-2456, 20 Jan 2026): 25% duty on certain advanced computing chips from 15 Jan 2026, not applied to imports for US data centres, US repairs, R&D, startups and some consumer uses; the President "may consider imposing significant tariffs" on semiconductors and SME "as well as an accompanying tariff offset program to incentivize domestic manufacturing"; further action possible if no agreement within 180 days (19 U.S.C. 1862(c)). | V | https://www.govinfo.gov/content/pkg/FR-2026-01-20/html/2026-01052.htm (20 Jan 2026) | The memo's synthesis says the proclamation "promises" offsets; it only signals them. |
| T11 | Lutnick's "50-50" production proposal and Taiwan's reply. | U | n.a. | Reportedly NewsNation, late Sep 2025. |
| T12 | Taiwan's "N-2" rule on overseas production at leading nodes. | U | n.a. | |
| U1 | US Steel 8-K: under a National Security Agreement of 13 Jun 2025 with the US Government (Treasury and Commerce), "subject to receipt of certain regulatory approvals, the Company will issue one share of Class G Preferred Stock (the 'Golden Share')", giving "certain rights with respect to non-ordinary course matters ... including relating to governance, domestic production and trade matters". Ex. 99.1: "approximately $11 billion in new investments will be made by 2028", including a greenfield project completed after 2028. | C | https://www.sec.gov/Archives/edgar/data/1163302/000110465925060674/tm2517314d1_8k.htm (filed 18 Jun 2025); https://www.sec.gov/Archives/edgar/data/1163302/000110465925059596/tm2518073d1_ex99-1.htm (13 Jun 2025) | "To be issued", not issued, at filing. No consent list in the filings. |
| U2 | MP Materials 8-K (Transaction Agreement 9 Jul 2025; closing 11 Jul): DoD buys USD 400m of Series A preferred, with up to USD 350m more committed; preferred plus warrant convertible into 15% of common; 10-year NdPr price floor of USD 110/kg; 10-year offtake of "the entire amount of magnets produced at the 10X Facility"; USD 150m DoD loan; at least USD 1bn of JPMorgan and Goldman Sachs financing. During a "Specified Period" MP may not, without DoD consent, consummate a "Fundamental Event" (sale of 15% or more of voting stock or of the project company), knowingly issue more than 14.9% of common stock to persons from non-permitted foreign jurisdictions, or sell to "Restricted Buyers"; the board may not nominate non-US citizens without DoD consent. | C | https://www.sec.gov/Archives/edgar/data/1801368/000119312525157310/d43796d8k.htm (filed 10 Jul 2025) | Press release URL returned 403; the "largest shareholder" phrasing was not checked. Consent rights are new and material. |
| U3 | Intel (22 Aug 2025): 433.3m shares at USD 20.47 (9.9%), USD 8.9bn funded from USD 5.7bn of unpaid CHIPS grants and USD 3.2bn of Secure Enclave funds; "passive ownership, with no Board representation or other governance or information rights"; votes with the Board "with limited exceptions"; five-year warrant for 5% at USD 20 "exercisable only if Intel ceases to own at least 51% of the foundry business". | V | https://www.intc.com/news-events/press-releases/detail/1748/intel-and-trump-administration-reach-historic-agreement-to (22 Aug 2025) | The deal also eliminated claw-back and profit-sharing on the earlier USD 2.2bn CHIPS grant. |
| U4 | Lithium Americas (Vancouver, 30 Sep 2025): "non-binding agreement in principle" with DOE on the first USD 435m draw; DOE defers USD 182m of debt service and receives warrants at USD 0.01 for 5% of LAC and for a 5% "non-voting, non-transferable" economic interest in the Thacker Pass JV; a DOE observer at JV board meetings. | C | https://www.sec.gov/Archives/edgar/data/1966983/000119312525225972/d98794dex991.htm (8-K filed 1 Oct 2025) | Non-binding and non-voting added. |
| U5 | xLight signed a USD 150m CHIPS LOI on 1 Dec 2025 ("First CHIPS Award Under Trump Administration", from the CHIPS R&D Office) and a final USD 150m award on 2 Jun 2026; first free-electron laser at the Albany Nanotech Complex. | V | https://www.xlight.com/blog/xlight-signs-150-million-letter-of-intent-with-the-u-s-department-of-commerce (1 Dec 2025); https://www.xlight.com/blog/xlight-finalizes-150m-chips-incentives-with-u-s-department-of-commerce (2 Jun 2026) | Neither release mentions government equity; any equity component is unverified. |
| U6 | Reuters (republished by Malay Mail), citing Bloomberg of 18 Jun 2026: Lutnick told ASML leaders in a series of meetings that Washington is concerned an EUV tool may be in China; ASML: it "has never shipped an EUV machine to China nor have we shipped to China any component, module or equipment specially designed to be used in an EUV machine". | C | https://www.malaymail.com/news/money/2026/06/19/us-tells-asml-it-is-concerned-one-of-its-chipmaking-tools-may-be-in-china-bloomberg-news-reports/224390 (19 Jun 2026) | Source chain corrected: Reuters relaying Bloomberg. |
| U7 | No US proposal for equity or a golden share in ASML or another foreign SME firm. | U | n.a. | Absence claim; cannot be established without search. |
| S1 | Liao's preprint is on SocArXiv only: v1 published 26 Jul 2025, v2 28 Jul 2025, v3 28 Oct 2025 (latest); versioned DOIs resolve; the unversioned DOI 10.31235/osf.io/ybxm5 does not exist in Crossref; OSF lists no article DOI. SSRN copy 10.2139/ssrn.5365340. | V | https://api.osf.io/v2/preprints/ybxm5/ (checked 29 Oct 2026) | |

## Citation verdicts

| Key | Verdict | Note |
|---|---|---|
| liao2025beyond | verified | SocArXiv v3; cite the versioned DOI. Abstract confirms the relocation-as-proxy argument. |
| weil2025european | corrected | Crossref title has "The European Union. Taiwan, and ..." (probably a publisher typo for a comma). Abstract: the shield argument "lacks rigorous academic grounding"; conclusion: it "is largely a hopeful narrative". A skeptical rival account, not an anchor for s_B(V). |
| kochumon2026taiwan | verified | East Asia 43(1): 23-36; second author registered as "Josukutty C. A."; title level only (no abstract available). |
| mckinney2021broken | verified | Parameters 51(4): 23-36; abstract describes "a tailored deterrence package that goes beyond either fighting over Taiwan or abandoning it". The TSMC-denial element was not checked against the full text (PDF blocked). Reply: Chan, Parameters 52(1): 167-180, doi:10.55540/0031-1723.3138. |
| horster2025silicon | verified | SSRN posted 2025; not peer reviewed; title level. |
| farrell2019weaponized | verified | Already in refs.bib. |
| cha2023collective | verified | A proposed strategy; trade data show targets export USD 46.6bn of goods on which China is more than 70% dependent. |
| lim2022informal | verified | Already in refs.bib. THAAD 2016-2017; introduces "regulatory availability and opportunism" as mediating variables. |
| gholz2021market | verified | Already in refs.bib. Japan "was able to adjust to avoid the Chinese sanction's bite". |
| kim2021making | corrected | Explains Japan's 2019 restrictions by "domestic symbolism" and Abe's electoral incentives. Relevant because allied chokepoint coercion can be driven by domestic audiences, which bears on coalition cohesion. |
| gerzhoy2015alliance | verified | Already in refs.bib. |
| mastanduno1992economic | corrected | Original Cornell University Press 1992 (already in refs.bib). The DOI 10.7591/9781501737145 is the 2020 digital edition (Crossref issued 2020-04-28); cite the 1992 edition. |
| lake1996anarchy | verified | Already in refs.bib. |
| teer2026dismantling | corrected | Full title "Dismantling China's Supply-Chain Weapon: A Transatlantic Strategy for Critical Minerals"; datePublished 21 Sep 2026. The compensation mechanism is proposed for Washington and Brussels. |
| glaser2025taiwan | verified | Authors Bonnie S. Glaser and Jennifer Lan; 18 August 2025. Not yet in refs.bib (refs.bib has glaser2026scorecard, a different item). |
| govella2025new | verified | |
| bis2025veu | verified | Already in refs.bib. |
| bis2024fdp | verified | Already in refs.bib as bis2024fdpr; reuse that key. |
| bis2025foundry | verified | Pages 5298-5321. |
| bis2020huawei | verified | Pages 29849-29863. Targets Huawei; add the August rule (85 FR 51596). |
| proc11002 | verified | Signals, does not promise, a tariff offset program. |
| eo14345 | verified | Also records Japanese purchases of US defence equipment. |
| wh2025korea | verified | Already in refs.bib as whitehouse2025korea; reuse that key. |
| hr8170 | verified | Already in refs.bib. Text as introduced. |
| skhynix2026prospectus | verified | Filed 10 Jul 2026. |
| tsmc2026form20f | verified | Already in refs.bib as tsmc2026annual; reuse that key. |
| ussteel2025nsa | corrected | Golden Share "will" be issued subject to regulatory approvals; USD 11bn figure is in Ex. 99.1 of the 16 Jun 2025 8-K. |
| intel2025agreement | verified | |
| mp2025dod | corrected | Press release blocked (403). Cite the 8-K (accession 0001193125-25-157310), which also discloses DoD consent rights. |
| lac2025doe | corrected | Non-binding agreement in principle; JV interest is non-voting; 8-K filed 1 Oct 2025. |
| tnw2026paxsilica | corrected | EU "set to join", not joined, on 25 Jun 2026; "colonise" is a paraphrase. |

## Modeling implications

1. **Split China's punishment of alignment into two channels and drop r_A = 0.** Japan 2025-26 shows China executing and sustaining costly punishment of a declaratory security act on Taiwan, with a plausible demonstration motive. Nexperia shows punishment following a Dutch state action on a Chinese-owned firm. Neither shows China punishing a holder for aligning on the chokepoint China needs: the 80 Japanese listings spare TEL, Nikon, Canon, JSR, TOK and Shin-Etsu. Write r_A = r_A^sec + r_A^x. Give r_A^sec an ex post value g_r = g_0 + g_demo >= 0, so it is executed on path, adds to Q and consumes slack one for one. Keep r_A^x small and endogenous to how much China needs the holder's output (omega), since punishing the holder's chokepoint firms would hurt China's own supply. For Europe, r_A^sec is live (July 2026 listing of 14 European entities, per CFR). The US paid Japan nothing found for r_A^sec, which matches the prediction that a patron facing a negative premium does not compensate.
2. **In-kind compensation as renewable conditional parts.** Annual licences (SK hynix and, per Reuters, Samsung; TSMC Nanjing with "no assurance" of renewal), list membership amendable by rule (Supplement No. 4) and CHIPS guardrails (a ten-year ban on certain new high-tech investment in China) each pay and enforce. Prediction to add: as a holder's premium rises, the patron converts durable authorizations into renewable ones and attaches operating limits ("operate but not expand or upgrade"). The 2025 Korean and Taiwanese conversions are the first observations.
3. **Code theta by instrument, not by country.** FDPR on foundry output (Huawei rules, 2020); due diligence on foundries (2025); licence requirements on US-origin tools for fabs in China, with an operate-only policy (Korea, Nanjing); the Supplement No. 4 carve-out (Japan, Netherlands); zero de minimis plus servicing denial (MATCH, pending). We found no public alliance threat used to enforce export controls in the three Asian cases. That supports Proposition 2(f), with the caveat that private linkage cannot be excluded.
4. **Rank control forms by enforceability, and calibrate Delta_c with MP Materials.** In the record, control rights attach to US-sited assets bought with US money or approvals: passive equity with an exit-triggered warrant (Intel); a golden share over governance, domestic production and trade (US Steel); consent rights over a sale of control, foreign ownership, board nationality and customers (MP); a non-voting interest and an observer (Lithium Americas). Toward TSMC the US pushed relocation instead. Rank Delta_c: relocation > consent rights over a US-sited subsidiary > equity in a foreign-domiciled firm. MP shows that the patron will pay heavily (floor, offtake, equity, loan) for strong consent rights, so a large positive T* in Proposition 4 has a precedent. The Europe 2031 holding company is an equilibrium only when relocating EUV and its servicing is infeasible.
5. **Make the silicon-shield channel explicit and contestable.** If s_B rises with value on the holder's territory, relocation lowers it and raises kappa_bar. GMF polling shows Taiwanese voters read TSMC's US investment that way. Weil, Gottwald and Taube (2025) argue the shield is a "hopeful narrative", which implies s_B'(V) near zero. Present both and note that the comparative statics in Proposition 3(d) depend on the sign. A home-node rule such as Taiwan's reported N-2 (unverified) would be an autonomy investment in the sense of Proposition 4(ii).
6. **Test the one-budget result with the Japan and Korea bundles.** EO 14345 bundles tariffs, USD 550bn under US project selection, aircraft and US defence equipment. The Korea fact sheet bundles tariffs, USD 350bn, defence spending, arms purchases, USFK support, enrichment and submarines. Export-control enforcement ran separately through flow rules. Code concessions by issue area to test whether they substitute within a holder's slack (Proposition 2(c) and (d)).
7. **Coalition purpose as a parameter.** Japan and Korea are in Pax Silica, depend on renewable US exemptions, and (Japan) fund US-selected projects. Remark G applies: the patron can target each member's conditional parts. A bloc that bargains against the patron is unstable. An insurance coalition against Chinese coercion (pooled stockpiles, compensation of targeted members, as in Cha 2023 and Teer 2026) is stable and lowers each member's r_A^sec. Side effect: it erodes the patron's ability to sell supply insurance as a carrot. Note that the EU itself was moving into Pax Silica in mid-2026, which lowers the plausibility of a Europe-led bloc against Washington.
8. **US commitment stakes differ by instrument.** The February 2026 Supreme Court ruling removed the IEEPA basis for the reciprocal tariffs whose reductions were promised to Japan, Korea and Taiwan. The administration turned to a Section 122 replacement tariff, Section 301 investigations (including Taiwan) and Section 232 with investment-linked preferences. Promises delivered through licences are durable but revocable; promises delivered through tariffs proved legally fragile. Europe should discount 2031 carrots accordingly.
9. **Out-of-sample table.** Code each holder on kappa (dependence and conditionality signals), theta (instrument), r_A^sec and r_A^x, omega, form of compensation, what the holder paid, and timing relative to changes in the outside option. Use the Netherlands as the reference row. Japan is the security-coercion case, Korea the hedge-policing case, Taiwan the relocation case, and the US equity deals calibrate the form and price of control.

## Open questions

- Methods: the shared WebSearch budget was exhausted at the first query; all checks used direct retrieval. Reuters, AP, Bloomberg, WSJ, NHK and Taylor and Francis could not be opened.
- Lutnick's "50-50" proposal (wording, date, venue) and Taiwan's reply.
- Taiwan's N-2 rule: legal instrument, date and scope.
- Japan's official response to MATCH, and whether METI restricted servicing of Japanese tools at Chinese fabs.
- METI's May 2023 release and the 23-item count.
- The MOFCOM announcement behind the July 2026 listing of Rheinmetall and 13 other European entities: names of the Dutch shipbuilder and the technical university, and the stated trigger.
- The dichlorosilane measures (January and September 2026) and the zero exports of terbium and dysprosium oxide, which rest on Bloomberg and Reuters.
- The US reactions of 20 to 27 November 2025 (Glass, State Department, Trump-Takaichi call).
- China's October 2025 sanctions on US-linked subsidiaries of Hanwha Ocean and their reported suspension after Busan.
- Dollar terms of the January 2026 US-Taiwan agreement; the reported further TSMC pledge of July 2026.
- Whether xLight's award includes government equity; whether Commerce's equity-for-grants approach was applied to or waived for foreign-owned recipients (TSMC, Samsung, SK hynix).
- Whether the EU formally joined Pax Silica after 25 June 2026, and whether the Netherlands signed.
- Holder-side self-binding: JIC's take-private of JSR (2023-24); Korea Zinc's reported US venture.
- Firm-level China exposure for Tokyo Electron, Nikon, Canon, JSR, TOK and Shin-Etsu.
- MATCH provisions in the FY2027 NDAA conference as of late October 2026.

## BibTeX (verified or corrected entries)

Keys already in paper/refs.bib are not repeated: farrell2019weaponized, lim2022informal, gholz2021market, gerzhoy2015alliance, mastanduno1992economic (1992 edition, correct as is), lake1996anarchy, bis2025veu, bis2024fdpr (memo key bis2024fdp), hr8170, whitehouse2025korea (memo key wh2025korea), tsmc2026annual (memo key tsmc2026form20f), afs2025veu, reuters2025koreanlicence.

```bibtex
@misc{liao2025beyond,
  author       = {Liao, Kerwin Xiang},
  title        = {Beyond the Silicon Shield: {TSMC}, Geopolitical Turbulence, and the Institutional Politics of Global Tech Power},
  howpublished = {SocArXiv preprint, version 3},
  year         = {2025},
  doi          = {10.31235/osf.io/ybxm5_v3},
  note         = {Posted 28 October 2025 (v1 26 July 2025; v2 28 July 2025). Also SSRN, doi:10.2139/ssrn.5365340. Not peer reviewed}
}

@article{weil2025european,
  author  = {Weil, Steffi and Gottwald, Joern Carsten and Taube, Markus},
  title   = {The {European Union}. {Taiwan}, and the {Silicon Shield} argument: a conceptual assessment through the lens of grand theories},
  journal = {European Politics and Society},
  volume  = {26},
  number  = {3},
  pages   = {537--563},
  year    = {2025},
  doi     = {10.1080/23745118.2024.2417028},
  note    = {Published online 4 November 2024. Title punctuation as registered with Crossref}
}

@article{kochumon2026taiwan,
  author  = {Kochumon, Jubil and {Josukutty C. A.}},
  title   = {{Taiwan}'s Silicon Shield Balancer in the {Taiwan-US-China} Triangularity},
  journal = {East Asia},
  volume  = {43},
  number  = {1},
  pages   = {23--36},
  year    = {2026},
  doi     = {10.1007/s12140-025-09455-1},
  note    = {Published online 19 June 2025}
}

@article{mckinney2021broken,
  author  = {McKinney, Jared M. and Harris, Peter},
  title   = {Broken Nest: Deterring {China} from Invading {Taiwan}},
  journal = {The US Army War College Quarterly: Parameters},
  volume  = {51},
  number  = {4},
  pages   = {23--36},
  year    = {2021},
  doi     = {10.55540/0031-1723.3089}
}

@article{chan2022broken,
  author  = {Chan, Eric},
  title   = {On ``Broken Nest: Deterring {China} from Invading {Taiwan}'' and Authors' Response},
  journal = {The US Army War College Quarterly: Parameters},
  volume  = {52},
  number  = {1},
  pages   = {167--180},
  year    = {2022},
  doi     = {10.55540/0031-1723.3138}
}

@misc{horster2025silicon,
  author       = {H{\"o}rster, Tim},
  title        = {Silicon Shield or Silicon Trap? {Taiwan}'s Semiconductor Dominance and the Strategic Calculus of {Chinese} Military Aggression},
  howpublished = {SSRN preprint},
  year         = {2025},
  doi          = {10.2139/ssrn.5245142},
  note         = {Not peer reviewed}
}

@article{cha2023collective,
  author  = {Cha, Victor D.},
  title   = {Collective Resilience: Deterring {China}'s Weaponization of Economic Interdependence},
  journal = {International Security},
  volume  = {48},
  number  = {1},
  pages   = {91--124},
  year    = {2023},
  doi     = {10.1162/isec_a_00465}
}

@article{kim2021making,
  author  = {Kim, Ji Young and Li, Wenxin and Lee, Seunghee},
  title   = {Making Sense of {Japan}'s Export Restrictions against {South Korea}},
  journal = {Asian Survey},
  volume  = {61},
  number  = {4},
  pages   = {683--710},
  year    = {2021},
  doi     = {10.1525/as.2021.61.4.683}
}

@misc{teer2026dismantling,
  author       = {Teer, Joris},
  title        = {Dismantling {China}'s Supply-Chain Weapon: A Transatlantic Strategy for Critical Minerals},
  howpublished = {Council on Foreign Relations, Report},
  year         = {2026},
  month        = sep,
  url          = {https://www.cfr.org/reports/dismantling-chinas-supply-chain-weapon},
  note         = {Published 21 September 2026}
}

@misc{govella2025new,
  author       = {Govella, Kristi},
  title        = {New Documents Reveal Next Steps for {U.S.-Japan} Trade Deal},
  howpublished = {Center for Strategic and International Studies, Commentary},
  year         = {2025},
  month        = sep,
  url          = {https://www.csis.org/analysis/new-documents-reveal-next-steps-us-japan-trade-deal},
  note         = {Published 9 September 2025}
}

@misc{glaser2025taiwan,
  author       = {Glaser, Bonnie S. and Lan, Jennifer},
  title        = {{Taiwan}'s Growing Distrust of the {United States}},
  howpublished = {German Marshall Fund of the United States},
  year         = {2025},
  month        = aug,
  url          = {https://www.gmfus.org/news/taiwans-growing-distrust-united-states},
  note         = {18 August 2025}
}

@misc{bis2025foundry,
  author       = {{U.S. Department of Commerce, Bureau of Industry and Security}},
  title        = {Implementation of Additional Due Diligence Measures for Advanced Computing Integrated Circuits; Amendments and Clarifications; and Extension of Comment Period},
  howpublished = {Federal Register 90: 5298--5321 (FR Doc. 2025-00711)},
  year         = {2025},
  month        = jan,
  url          = {https://www.federalregister.gov/documents/2025/01/16/2025-00711/implementation-of-additional-due-diligence-measures-for-advanced-computing-integrated-circuits},
  note         = {Interim final rule, published and effective 16 January 2025}
}

@misc{bis2020huawei,
  author       = {{U.S. Department of Commerce, Bureau of Industry and Security}},
  title        = {Export Administration Regulations: Amendments to General Prohibition Three (Foreign-Produced Direct Product Rule) and the Entity List},
  howpublished = {Federal Register 85: 29849--29863 (FR Doc. 2020-10856)},
  year         = {2020},
  month        = may,
  url          = {https://www.federalregister.gov/documents/2020/05/19/2020-10856},
  note         = {Published 19 May 2020, effective 15 May 2020}
}

@misc{bis2020huawei2,
  author       = {{U.S. Department of Commerce, Bureau of Industry and Security}},
  title        = {Addition of {Huawei} Non-{U.S.} Affiliates to the Entity List, the Removal of Temporary General License, and Amendments to General Prohibition Three (Foreign-Produced Direct Product Rule)},
  howpublished = {Federal Register 85: 51596--51629 (FR Doc. 2020-18213)},
  year         = {2020},
  month        = aug,
  url          = {https://www.federalregister.gov/documents/2020/08/20/2020-18213},
  note         = {Published 20 August 2020, effective 17 August 2020}
}

@misc{proc11002,
  author       = {{The President of the United States}},
  title        = {Proclamation 11002 of January 14, 2026: Adjusting Imports of Semiconductors, Semiconductor Manufacturing Equipment, and Their Derivative Products Into the {United States}},
  howpublished = {Federal Register 91: 2443--2456 (FR Doc. 2026-01052)},
  year         = {2026},
  month        = jan,
  url          = {https://www.govinfo.gov/content/pkg/FR-2026-01-20/html/2026-01052.htm},
  note         = {Signed 14 January 2026, published 20 January 2026}
}

@misc{eo14345,
  author       = {{The President of the United States}},
  title        = {Executive Order 14345 of September 4, 2025: Implementing the {United States-Japan} Agreement},
  howpublished = {Federal Register 90: 43535--43538 (FR Doc. 2025-17389)},
  year         = {2025},
  month        = sep,
  url          = {https://www.govinfo.gov/content/pkg/FR-2025-09-09/html/2025-17389.htm},
  note         = {Published 9 September 2025}
}

@misc{wh2025japanminerals,
  author       = {{The White House}},
  title        = {{United States-Japan} Framework for Securing the Supply of Critical Minerals and Rare Earths through Mining and Processing},
  howpublished = {The White House},
  year         = {2025},
  month        = oct,
  url          = {https://www.whitehouse.gov/briefings-statements/2025/10/united-states-japan-framework-for-securing-the-supply-of-critical-minerals-and-rare-earths-through-mining-and-processing/},
  note         = {Signed in Tokyo 28 October 2025. Not legally binding}
}

@misc{skhynix2026prospectus,
  author       = {{SK hynix Inc.}},
  title        = {Prospectus ({Form} 424{B}4)},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0001193125-26-299963},
  year         = {2026},
  url          = {https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm},
  note         = {Filed 10 July 2026}
}

@misc{ussteel2025nsa,
  author       = {{United States Steel Corporation}},
  title        = {Current Report on {Form} 8-{K} ({National Security Agreement}; {Golden Share})},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0001104659-25-060674},
  year         = {2025},
  url          = {https://www.sec.gov/Archives/edgar/data/1163302/000110465925060674/tm2517314d1_8k.htm},
  note         = {Filed 18 June 2025. Investment figure in Ex. 99.1 to the 8-K filed 16 June 2025 (accession 0001104659-25-059596)}
}

@misc{intel2025agreement,
  author       = {{Intel Corporation}},
  title        = {{Intel} and {Trump} Administration Reach Historic Agreement to Accelerate {American} Technology and Manufacturing Leadership},
  howpublished = {Intel press release (Business Wire)},
  year         = {2025},
  month        = aug,
  url          = {https://www.intc.com/news-events/press-releases/detail/1748/intel-and-trump-administration-reach-historic-agreement-to},
  note         = {22 August 2025}
}

@misc{mp2025dod,
  author       = {{MP Materials Corp.}},
  title        = {Current Report on {Form} 8-{K} (Transaction Agreement with the {Department of Defense})},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0001193125-25-157310},
  year         = {2025},
  url          = {https://www.sec.gov/Archives/edgar/data/1801368/000119312525157310/d43796d8k.htm},
  note         = {Filed 10 July 2025; Transaction Agreement dated 9 July 2025}
}

@misc{lac2025doe,
  author       = {{Lithium Americas Corp.}},
  title        = {{Lithium Americas} Reaches Agreement with {GM} and {U.S. DOE} Regarding First Draw on {DOE} Loan},
  howpublished = {Exhibit 99.1 to {Form} 8-{K}, U.S. Securities and Exchange Commission, EDGAR, accession 0001193125-25-225972},
  year         = {2025},
  url          = {https://www.sec.gov/Archives/edgar/data/1966983/000119312525225972/d98794dex991.htm},
  note         = {News release dated 30 September 2025; 8-K filed 1 October 2025}
}

@misc{tnw2026paxsilica,
  author       = {Stanciuc, Ana-Maria},
  title        = {The {EU} Signs Up to {Pax Silica}, the {US}-Led Chip Pact {France} Called Colonisation},
  howpublished = {TNW (The Next Web)},
  year         = {2026},
  month        = jun,
  url          = {https://thenextweb.com/news/eu-pax-silica-ai-chips},
  note         = {Published 25 June 2026}
}

@misc{mofcom2026japan11,
  author       = {{Ministry of Commerce of the People's Republic of China}},
  title        = {{MOFCOM} Announcement No. 11 of 2026 Placing 20 {Japanese} Entities on the Export Control List},
  howpublished = {MOFCOM},
  year         = {2026},
  month        = feb,
  url          = {https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_b5159a773124428a9813884015d1b8b3.html},
  note         = {In Chinese (Shangwubu gonggao 2026 nian di 11 hao). 24 February 2026. Announcement No. 12 (watch list) at art\_bac18400512d408a8d4c2f964e36ac11.html}
}

@misc{mofcom2026japan27,
  author       = {{Ministry of Commerce of the People's Republic of China}},
  title        = {{MOFCOM} Announcement No. 27 of 2026 Placing 20 {Japanese} Entities on the Export Control List},
  howpublished = {MOFCOM},
  year         = {2026},
  month        = jun,
  url          = {https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_df87be1437044874a35f85cf6e076f3d.html},
  note         = {In Chinese (Shangwubu gonggao 2026 nian di 27 hao). 29 June 2026. Announcement No. 28 (watch list) at art\_c2ab731429dc4bc3ba8696cd0e6ad857.html}
}

@misc{kokkai2025takaichi,
  author       = {{House of Representatives of Japan}},
  title        = {Minutes of the Budget Committee, {House of Representatives}, 219th {Diet}, No. 2},
  howpublished = {National Diet Library, Diet Record Search System},
  year         = {2025},
  month        = nov,
  url          = {https://kokkai.ndl.go.jp/txt/121905261X00220251107/188},
  note         = {In Japanese. 7 November 2025, speech 188 (Prime Minister Takaichi)}
}

@misc{tsmc2020arizona,
  author       = {{Taiwan Semiconductor Manufacturing Company Limited}},
  title        = {{TSMC} Announces Intention to Build and Operate an Advanced Semiconductor Fab in the {United States}},
  howpublished = {TSMC press release},
  year         = {2020},
  month        = may,
  url          = {https://pr.tsmc.com/english/news/2033},
  note         = {15 May 2020}
}

@misc{tsmc2024chips,
  author       = {{Taiwan Semiconductor Manufacturing Company Limited}},
  title        = {{TSMC Arizona} and {U.S. Department of Commerce} Announce up to {US\$6.6} Billion in Proposed {CHIPS Act} Direct Funding},
  howpublished = {TSMC press release},
  year         = {2024},
  month        = apr,
  url          = {https://pr.tsmc.com/english/news/3122},
  note         = {8 April 2024. Non-binding preliminary memorandum of terms}
}

@misc{tsmc2025expand,
  author       = {{Taiwan Semiconductor Manufacturing Company Limited}},
  title        = {{TSMC} Intends to Expand Its Investment in the {United States} to {US\$165} Billion to Power the Future of {AI}},
  howpublished = {TSMC press release},
  year         = {2025},
  month        = mar,
  url          = {https://pr.tsmc.com/english/news/3210},
  note         = {4 March 2025}
}

@misc{xlight2025loi,
  author       = {{xLight}},
  title        = {{xLight} Signs \$150 million Letter of Intent with the {U.S. Department of Commerce}},
  howpublished = {xLight news release},
  year         = {2025},
  month        = dec,
  url          = {https://www.xlight.com/blog/xlight-signs-150-million-letter-of-intent-with-the-u-s-department-of-commerce},
  note         = {1 December 2025. Final award announced 2 June 2026}
}

@misc{power2026china,
  author       = {Power, John},
  title        = {{China} Slaps Export Controls on Dozens of {Japanese} Entities},
  howpublished = {Al Jazeera},
  year         = {2026},
  month        = jun,
  url          = {https://www.aljazeera.com/economy/2026/6/29/china-slaps-export-controls-on-dozens-of-japanese-entities},
  note         = {29 June 2026}
}

@misc{durbin2023biden,
  author       = {Durbin, Dee-Ann and Madhani, Aamer},
  title        = {{Biden}'s Huge Computer Chips Campaign against {China} Has Won Over the {Dutch} and {Japanese}, Source Says},
  howpublished = {Associated Press, via Fortune},
  year         = {2023},
  month        = jan,
  url          = {https://fortune.com/2023/01/30/biden-china-chips-export-controls-netherlands-dutch-japanese},
  note         = {30 January 2023}
}
```
