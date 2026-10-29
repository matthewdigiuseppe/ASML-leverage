# Final check: facts (tag: facts)

Scope: factual claims that the v2 revision added or changed in 02_background.tex, 07_decide.tex, 08_evidence.tex, 09_implications.tex, C_scenario.tex, D1_control.tex and D2_decide.tex. The added text was identified with `git diff 82adc1c 63de2c0`. Each claim was traced to a verification row in notes/review/*.md or notes/v2/*.md, and the cited key was read in paper/refs.bib. All 141 keys cited in these files exist in refs.bib. One item (the 2019 EUV licence) was re-read at its source (NL Times, 6 January 2020).

## Confirmed, no change needed

- Bamenga motion (37020-XVII nr. 11): adopted 13 October 2026, 110 to 40, signed by D66, CDA and VVD members, with the cabinet leaving it to the House. The 40 votes against are PVV 19, FvD 7, Markuszower 7, PvdD 3, SP 3 and Keijzer 1, which matches the seat table. Source: gap_dutch_domestic_politics.md rows 13, 46. Key kst37020xvii11 is correct.
- Piri motion (21501-20 nr. 2364): adopted 22 January 2026, 103 to 46, against the caretaker cabinet's advice. The 46 against are PVV 19, JA21 9, FvD 7, Markuszower 7 and BBB 4 (before Keijzer left BBB), with Volt absent. Source: row 14. Key kst21501_20_2364 is correct.
- The seat figures 52 to 26 and 40 to 38 are arithmetically correct for the 78-seat bloc (VVD, CDA, PVV, JA21, Markuszower, BBB). See finding 5 on scope.
- Pew spring 2026: 41 percent call the US a reliable partner, against 88 percent in 2022 (row 49). Key pew2026usimage is correct.
- MATCH: introduced 2 April 2026; HFAC ordered it reported 36 to 8 on 22 April; no later action; neither FY2027 NDAA text contains it. The bill sets a 150-day certification deadline, covers all DUVi tools, and imposes licensing with a policy of denial on servicing at covered facilities (rows 25, 34, 40; gap_comparative_holder_cases.md M1). Keys hr8170 and baumgartner2026match are correct.
- Korea: VEU revoked by 90 FR 42321 (published 2 September 2025, effective 31 December 2025). BIS said it would license operation of existing fabs but not expansion or upgrades. Annual 2026 licences were granted, and the 13 November 2025 fact sheet does not mention export controls (facts_record.md 5.1 to 5.4; K1 to K7). Keys bis2025veu, afs2025veu, skhynix2026prospectus, reuters2025koreanlicence and whitehouse2025korea are correct.
- Takaichi, 7 November 2025, speech 188 (J7). Key kokkai2025takaichi is correct. See finding 2 on the listings.
- TSMC's US commitment grew from about USD 12bn (May 2020) to USD 165bn (March 2025) (T1; tsmc2020arizona, tsmc2025expand). The terms of MP Materials (consent rights, equity, price floor, offtake), US Steel (golden share under the NSA with Nippon Steel) and Intel (passive stake) match gap_comparative_holder_cases.md lines 59 to 61.
- Pax Silica: Japan and South Korea had signed by 25 June 2026, and the EU was "set to join" (P1; tnw2026paxsilica).
- Council record: positive opinions on 9 April and 24 July 2025; Regs 2025/786 (14 April 2025) and 2025/1727 (5 August 2025); a renewal after the 28 January 2026 committee meeting; Reg. 2026/1893 with no end date. ACI recital 85, Statement C/2023/1341 and Art. 12(5) were all verified (gap_council_revealed_positions.md rows 6 to 15, 21, 22, 25). See finding 3 on one citation.
- Section 1250A, FY2024 NDAA, 22 U.S.C. 1928f: two-thirds of the Senate or an Act of Congress (security.md row 43). Key usc1928f is correct.
- Orders of magnitude: d_ai of EUR 4, 50 and 130bn; kappa S_k of 12.5bn at kappa = 0.10 and S = 125bn, with a range of 2.5 to 37.5bn; China's lever at 3 and 77bn with a geometric midpoint of about 15bn (gap_european_cost_parameters.md synthesis). The arithmetic checks.
- Hold-up numbers: EUR 4.09bn of US-sited revenue (0.34bn a month); central l of 1.9bn a month; US$3.9 to 4.8bn a month of EUV-node wafer revenue; c_S of about 2, 13 and 40bn; h* of about 0.85; t-bar of about 26 and 15 months (gap_servicing_time_to_pain.md items 1, 5 and 3; table rows for l and c_S).
- Background figures: China's share of 26.3, 36.1 and 29.1 percent; IBM at 25.1 percent; AEI's 70 percent and six-month maintenance cycle; 8,242 US staff (18.7 percent); Supplement No. 4 (33 countries, 25 EU members); the Diffusion Rule (ten EU members in the favoured group, rescission announced 13 May, two days before compliance was due); the August 2025 joint statement (USD 40bn); NSS quotes; Hegseth's order of 1 May 2026; Spain on 30 March 2026; Decrees 834 and 835; Nuctech on 15 May 2026.
- Europe 2031 quotes in C_scenario.tex ("now, while the option still exists", "roughly halving European allocations", "the full displeasure of both great powers at once", "amassed enough EUV machines and maintenance know-how", the August 2030 Chinese credit, the eight-state coalition) all match e2031.md rows 38 to 43 and lit_ai.md row 117.
- D2: Hungary's change of government (Magyar appointed 9 May 2026; secondary source only), 28.06 percent for the scenario seven, and the completion rule (gap_council_revealed_positions.md row 46 and item 6).

## Findings

### 1. [important] 02_background.tex: the rare-earth pause extension is stated as settled

Anchor: "were suspended after the Busan summit of 30 October 2025, a pause the two governments agreed in September 2026 to extend to 10 January 2027"

Problem: Announcement 70 (mofcom2025pause) suspends the October 2025 controls only until 10 November 2026. MOFCOM's 28 September 2026 statement (mofcom2026extension) extends the Kuala Lumpur arrangement to 10 January 2027, but it does not mention export controls or rare earths. As of 29 October 2026 no MOFCOM act amending Announcement 70 had been found (facts_record.md 2.3, 2.5 and open items). The sentence presents a political truce extension as a legal extension of the rare-earth suspension. That suspension lapses on 10 November unless it is re-gazetted.

Replacement: "Its broader, extraterritorial controls of October 2025 \citep{mayerbrown2025rareearth} were suspended until 10 November 2026 after the Busan summit of 30 October 2025 \citep{whitehouse2025busan, mofcom2025pause}. In September 2026 the two governments agreed to extend their truce to 10 January 2027, but by late October China had not amended the suspension itself \citep{mofcom2026extension}; \cref{sec:tests} asks what a lapse would bring."

### 2. [important] 08_evidence.tex: the Japanese listings are miscounted against their sources, and "no toolmaker" is broader than the check

Anchors: "China listed eighty Japanese entities, none of them a maker of chipmaking equipment or photoresists \citep{mofcom2026japan11, mofcom2026japan27}" and, in tab:cases, "2025--26: 80 entities listed after a Taiwan statement, no toolmaker among them"

Problem:
- The 80 entities are 40 on China's export-control list (Announcements 11 and 27) plus 40 on its watch list (Announcements 12 and 28). The cited keys are titled "Placing 20 Japanese Entities on the Export Control List", so a reader who checks finds 40.
- The verification (gap_comparative_holder_cases.md J13) confirms only that Tokyo Electron, Nikon, Canon, JSR, Tokyo Ohka and Shin-Etsu are absent. The 24 February watch list includes Sumitomo Heavy Industries (J11), whose group makes ion implanters. "None of them a maker of chipmaking equipment" is therefore unsupported as stated.

Replacement (text): "China placed forty Japanese entities on its export-control list and forty more on its watch list \citep{mofcom2026japan11, mofcom2026japan27}. None is among Japan's leading makers of lithography, deposition and etch tools or photoresists (Tokyo Electron, Nikon, Canon, JSR, Tokyo Ohka, Shin-Etsu)."

Replacement (table cell): "2025--26: 40 entities controlled and 40 watch-listed after a Taiwan statement, none of Japan's leading toolmakers among them"

### 3. [important] 07_decide.tex: the source cited for the Greenland withdrawal predates it

Anchor: "the suspension was renewed in January 2026 after Washington dropped the tariffs it had threatened over Greenland \citep{dazio2026greenland, tbc2026summaryjan}"

Problem: dazio2026greenland is the AP report of 19 January 2026 on the tariff threat. Washington withdrew the threat on 21 January (security.md row 48, ttnews.com). The AP piece cannot support "dropped the tariffs". tbc2026summaryjan supports only the renewal. The renewal act is Reg. 2026/295 of 4 February 2026 (gap_council_revealed_positions.md row 12), and it has no key.

Replacement: "the suspension was renewed in January 2026, a week after Washington dropped the tariffs it had threatened over Greenland \citep{ttnews2026greenland, tbc2026summaryjan}". Add to refs.bib: `@misc{ttnews2026greenland, title={Trump Drops Greenland Tariffs}, howpublished={Transport Topics}, year={2026}, note={21 January 2026}, url={https://www.ttnews.com/articles/trump-greenland-drops-tariffs}}` (confirm the author and headline when adding).

### 4. [important] 07_decide.tex: the legal basis for the Chinese penalty is dated to April 2026

Anchor: "Since April 2026, $p_C$ has a legal basis. Decree 835 lets Beijing"

Problem: China's first blocking order (MOFCOM Announcement 21 of 2026, 2 May 2026) was issued under the 2021 MOFCOM Rules on Counteracting Unjustified Extra-territorial Application of Foreign Legislation, not under Decree 835 (facts_record.md 2.8). Those rules, and the 2021 Anti-Foreign Sanctions Law, already gave a penalty for complying with US measures a legal basis. Decree 835 broadened that basis; it did not create it. The same overstatement appears in 08_evidence.tex at "and since Decrees 834 and 835 stopping it carries a Chinese counter-threat".

Replacement (07): "China's 2021 blocking rules already gave $p_C$ a legal basis, and Decree 835 of April 2026 widened it. The decree lets Beijing"

Replacement (08): "and since China's 2021 blocking rules and Decrees 834 and 835, stopping it carries a Chinese counter-threat (\cref{sec:background})"

### 5. [important] 08_evidence.tex: the seat arithmetic is claimed for "any" right-leaning majority

Anchor: "By our count, within any right-leaning majority in the current house the first motion's supporters outnumber its opponents by 52 seats to 26, while the second's divide 40 to 38."

Problem: The figures hold only for the 78-seat bloc of VVD, CDA, PVV, JA21, the Markuszower group and BBB (gap_dutch_domestic_politics.md item 1 and row 60). The minimal 75-seat majority without BBB gives 49 to 26 and 40 to 35, and larger majorities give other numbers. A nearby sentence also omits a year: "On 22 January it had adopted".

Replacement: "Every right-leaning majority in the current house needs VVD, CDA, PVV, JA21 and the Markuszower group, and in practice BBB. Within that 78-seat bloc the first motion's supporters outnumber its opponents by 52 seats to 26, while the second's divide 40 to 38." Also replace "On 22 January it had adopted" with "On 22 January 2026 it had adopted".

### 6. [minor] 02_background.tex: the 2019 EUV episode leaves out the 2018 licence

Anchor: "From 2019 The Hague left ASML's application to ship an EUV machine to China undecided, reportedly after US lobbying"

Problem: The cited source (nltimes2020pressured, reporting Reuters) says the government had licensed the sale in 2018, that the licence expired, and that it was not renewed after US lobbying in 2019. ASML said it was awaiting a new licence. asml_facts.md (Position 2 and line 92) confirms only that the application was pending in October 2020. "Left undecided" is defensible, but it hides that The Hague had first said yes.

Replacement: "The Hague licensed an EUV sale to China in 2018, and after US lobbying in 2019 it did not renew the expired licence; ASML's new application was still pending in October 2020 \citep{nltimes2020pressured, kaag2020asml}."

### 7. [minor] 07_decide.tex: the local-repair figure is a pay target, not a plan

Anchor: "ASML's plan to have 50 to 70 percent of service parts repaired locally \citep{asml2026annual}"

Problem: The source is a 2026 to 2028 long-term incentive sub-measure in the remuneration report: threshold 50 percent, target 60 percent, stretch 70 percent of service parts sent for repair locally, framed as cutting logistics emissions (gap_servicing_time_to_pain.md row 17).

Replacement: "ASML's 2026--2028 executive pay target of 50 to 70 percent of service parts repaired locally \citep{asml2026annual}"

### 8. [minor] 08_evidence.tex: the low end of China's lever has no source

Anchor: "China's input lever over Europe runs from about 3 billion to 77 billion, the high end being the ECB's estimated loss"

Problem: The EUR 3bn low end is an assumption, not a bound. The verification notes that the Nexperia episode does not bound it (gap_european_cost_parameters.md item 4). As written, the sentence reads as if both ends were sourced.

Replacement: "China's input lever over Europe runs from about 3 billion, our assumption for graduated punishment, to 77 billion, the ECB's estimated loss"

### 9. [minor] 09_implications.tex: the scope sentence carries the claim corrected in finding 2

Anchor: "China spared Japan's equipment makers while punishing a security statement"

Replacement: "China spared Japan's leading equipment and photoresist makers while punishing a security statement"

### 10. [minor] 08_evidence.tex: the NDAA claim has no citation

Anchor: "and neither chamber's FY2027 defence authorization contains it."

Problem: The claim is verified (gap_dutch_domestic_politics.md rows 34 and 40, govinfo texts of H.R. 8800 and S. 4784) but uncited. It is the only factual sentence in the paragraph without a key.

Replacement: "and neither chamber's FY2027 defence authorization contains it \citep{hr8800eh, s4784rs}". Add `@misc{hr8800eh, title={{H.R.} 8800, National Defense Authorization Act for Fiscal Year 2027, Engrossed in the House}, year={2026}, url={https://www.govinfo.gov/content/pkg/BILLS-119hr8800eh/xml/BILLS-119hr8800eh.xml}}` and `@misc{s4784rs, title={{S.} 4784, National Defense Authorization Act for Fiscal Year 2027, Reported in the Senate}, year={2026}, url={https://www.govinfo.gov/content/pkg/BILLS-119s4784rs/xml/BILLS-119s4784rs.xml}}`.
