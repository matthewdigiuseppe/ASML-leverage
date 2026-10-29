# Servicing hold-up: time to pain (t_U), US compulsion share (h), US-origin content (theta) and the US cost of interruption (c_U). Fact-checked gap memo (as of 29 October 2026)

Strand: gap_servicing_holdup. Calibrates t_U, h (the memo's mu), c_U (c_S in Proposition 6), l, theta and the China DUVi fleet for the time-to-pain corollary of Proposition 6 (notes/model_design_v2.md, Section 8).

## How this was checked, and its limits

The session's web-search budget was exhausted before this check began (the first WebSearch call was refused), so nothing below rests on a search-engine result. Every item was checked by retrieving the primary document directly:

- SEC EDGAR: ASML 20-F for FY2015 (unit tables for 2013 to 2015), FY2016, FY2017, FY2019, FY2021, FY2023, FY2024 and FY2025; ASML Q3 2026 6-K (press release and presentation slide 9); TSMC 20-F for FY2023, FY2024 and FY2025; NVIDIA 10-K for FY2026. Text was extracted and searched for the exact passages.
- govinfo: 88 FR 73424 (25 October 2023), 89 FR 96790 (5 December 2024), H.R. 8170 (IH) and S. 4281 (IS).
- eCFR versioner API: 15 CFR 734.4 as of 26 October 2026 (title 15 "up to date as of 2026-10-27").
- Congress.gov API: actions on H.R. 8170 (the S. 4281 query hit the rate limit).
- Crossref and Semantic Scholar records retrieved by DOI (not by search) for the SPIE papers and Fomenkov et al. (2017).
- Direct page fetches: europe2031.ai, Taipei Times, Rhodium Group, CSIS, AEI, TrendForce, IO+, Gigaphoton, SK hynix newsroom, the SIA report page and PDF.

Two access problems. De Gruyter Brill blocked retrieval of Fomenkov et al. (2017) in this session, so the full text was read from a copy of the publisher PDF downloaded earlier in this project; its header (journal, volume, pages, DOI, author list) matches Crossref exactly. The SPIE full texts were not accessible; for Brandt, Fomenkov and Graham (2021) and Zhu et al. (2025) we now have the publisher abstracts via their Semantic Scholar records, and those abstracts add numbers the original memo lacked.

## Verdict in brief

The memo is careful and most of its facts survive. The legal analysis of theta is right on the text. The corrections that matter for the model are these:

1. **Scope of the European threat.** The scenario's 2029 Anti-Coercion Instrument measure targets "ASML's exports and servicing to American fabs in Arizona" (europe2031.ai, 2029 chapter). The memo's c_U and l describe a much broader hold-up of all US-aligned fabs, including TSMC in Taiwan and Samsung and SK hynix in Korea, which is what the 2031 ultimatum implies ("through its Taiwanese partners"). These are different games. For the Arizona-only threat, ASML's entire US-sited revenue was EUR 4.09bn in 2025 (EUR 0.34bn a month), and the US can compel the ASML staff, parts and repair centres on its own soil, so h is close to one.
2. **The parts buffer is larger and more seizable than the memo says.** TSMC's NT$24.8bn of supplies and spare parts excludes ASML's own stock. ASML carried EUR 5.3bn of raw materials at end-2025 and attributes the increase "mainly" to "supporting our growing install base"; it runs repair centres in Linkou, Hwaseong, Wilton, San Diego and Vancouver (WA). Parts physically in Taiwan, Korea or the US are as exposed to commandeering as field staff. The location of ASML's parts inventory is not disclosed.
3. **The 2017 collector anchor needs three caveats.** 100 Gpulses was a demonstrated lifetime on NXE:3300 sources (Fomenkov et al. 2017), not a hard stop. Reflectivity falls gradually (0.4%/Gp in 2017), so a fab without replacements loses source power and throughput before it loses the tool. And ASML's design target for critical source components was 30,000 hours, which at 50 kHz is about 5,400 Gpulses (our arithmetic). The public anchors for t_U therefore span two orders of magnitude, and the memo's "implausible for parts beyond about a year" is a judgment, not a finding. New, verified: by 2021 EUV sources ran at 250 W "with 92% availability" (Brandt, Fomenkov and Graham 2021, abstract), and 500 W sources were at customer sites by 2025 (Zhu et al. 2025, abstract).
4. **The 95% indicator does not measure "what OEM service buys".** ASML's 95% (systems sold in the past 30 years still active) includes machines that ASML no longer services. ASML assumes that 33% of those remain active, and it says it will stop reporting the indicator. The 33% assumption is itself weak evidence that some (presumably older) tools keep running without OEM service.
5. **c_U inputs.** TSMC's node shares are shares of wafer revenue (NT$3,272.6bn, 85.9% of net revenue), not net revenue; N6, which uses EUV, sits in the 7nm bucket (14%); North America is defined by customer headquarters. Corrected EUV-node wafer revenue from US-headquartered customers is US$3.9bn to US$4.8bn a month (memo: US$4.6bn). The c_U range barely moves (about US$2bn to US$40bn a month, central about US$13bn).
6. **Smaller errors.** The variable-price language in ASML's 20-F refers to volume purchase agreements, not service contracts. The 20-year lifetime statement covers EUV (FY2024) and "both EUV and DUV" (FY2025). The Taiwan risk factor speaks of the "ability to serve customers in Taiwan". The TrendForce headline is misquoted. Gigaphoton's 30% maintenance-cycle claim is verified for the GT66A only. In H.R. 8170 the duty falls on the "covered agency heads" (BIS Under Secretary and Secretary of State), and the bill was ordered reported in the nature of a substitute, 36 to 8, on 22 April 2026; the text cited is the introduced version. The China installed-base arithmetic gives about 300 to 390 tools from 2015 to 2025, not 290 to 430.
7. **Cross-strand inconsistency.** lit_ai.md (line 165) says "the December 2024 FDP rules reach ASML's non-Dutch sales". On the Federal Register text, those rules reach exports to Macau, D:5 destinations and Footnote 5 entities from outside Supplement No. 4 countries. They impose no licence requirement on ASML shipments to Taiwan or South Korea. This memo's reading is the correct one, and lit_ai.md should be amended.

## Corrected synthesis

Europe 2031 has Washington claim, in the March 2031 ultimatum, that "through its Taiwanese partners, it has amassed enough EUV machines and maintenance know-how to forego ASML access for longer than Europe can forego access to frontier AI." The claim names machines and know-how. It is silent on consumables, optics, software and engineering support. Our position is that the claim is right about tools, largely right about field know-how, and unproven about consumables. Unproven is not the same as false: the open record gives a 2017 lower anchor and a design target that differ by a factor of about 200, and nothing in between that we could read.

**Tools.** ASML recognized 324 EUV systems from 2013 through 2025 (313 since 2017, six of them High-NA EXE) and expects to ship about 65 Low-NA systems in 2026. None can go to China. Brandt, Fomenkov and Graham (2021) count "over 85 EUV scanners" in high-volume manufacturing at customer sites in 2021, against 97 recognized through 2020, so the recognized count overstates the production fleet by roughly a dozen early tools. Because US partners already hold the whole fleet, a "stockpile of machines" is cheap to claim. What matters is how fast those tools lose output without ASML.

**Consumables.** Fomenkov et al. (2017) report that "over 100 Billion pulses collector lifetime has been demonstrated" on NXE:3300 sources, that typical reflectivity loss improved from 0.6%/Gp (SPIE 2016) to 0.4%/Gp (SPIE 2017), and that ASML set "a target of 30 000 h" for the most critical source components, of which the collector is "arguably the most critical component in terms of lifetime." At roughly 50 kHz, 100 Gp is about 23 days of continuous firing and 30,000 hours is about 5,400 Gp (our arithmetic). Sources fire in bursts, so calendar life exceeds continuous-firing time by the inverse of the duty cycle, which we could not source. Degradation is gradual, so the post-buffer output loss should rise smoothly rather than jump. Collectors and all other critical optics come from Carl Zeiss SMT under an exclusive arrangement, and ASML says Zeiss's capacity limits how many systems it can build. EUV source materials face "corrosive liquid tin" and include "strategic tantalum alloys and molybdenum", which are "limited in availability and costly" (ASML 20-F FY2023). Bloomberg's anonymous sources (May 2024) say EUV tools need "such frequent upkeep that without ASML's spare parts they quickly stop working." That is the only direct statement on the US buffer, and it is not quantified.

The memo treats TSMC's NT$24.8bn (about US$0.79bn) of supplies and spare parts as the parts buffer. That figure excludes ASML's own inventory: EUR 5.3bn of raw materials at end-2025, which ASML says grew "mainly" to support its installed base, held partly through regional warehouses and repair centres whose locations near customers ASML advertises. We do not know how much of it sits in Taiwan, Korea or the US. Whatever does is exposed to seizure in the same way as field labor. What Europe controls with certainty is the flow of new optics (Oberkochen), drive lasers (Trumpf, Ditzingen), modules made in Veldhoven and Berlin, software and engineering support. The memo's central t_U of six months is a defensible judgment. The range should run from one month (Bloomberg's "quickly" with 2017-vintage collector life) to two years or more (stockpiled consumables, seized local inventory and commandeered local repair).

**Know-how.** ASML has "around 10,000 customer support employees" worldwide (FY2025; "more than 10,000" in FY2024). It discloses headcount by country only above 10% of staff: Netherlands 23,707, United States 8,242 and Taiwan 4,548 at end-2025. The US figure is dominated by manufacturing and R&D at Wilton, San Diego and San Jose, so it overstates commandeerable field service. ASML's service contracts include "limited manpower agreements" and "parts availability or parts usage agreements"; Bloomberg reports joint service contracts in which "certain customers" do routine maintenance themselves and that allow "clients such as TSMC" to access their own machines' systems; and the 2026 to 2028 long-term incentive plan rewards having 50%, 60% or 70% of service parts "sent for repair locally". ASML's risk factors list customers performing services themselves or through third parties, "potential nationalization of assets", and cross-strait risk to its "ability to serve customers in Taiwan" (25.5% of 2025 total net sales). The MATCH bills define servicing to include remote work and "updating software or firmware", so Congress treats servicing as more than field labor. Washington and Taipei would not need to stockpile know-how. They could commandeer much of it, along with whatever parts sit in their territory. They could not commandeer new Zeiss optics, European-built modules, software updates or Veldhoven's engineering.

**Jurisdiction.** For China-bound DUVi, current US rules largely defer to The Hague. 15 CFR 734.4(a)(3) removes de minimis for 3B993.f.1 lithography destined for advanced-node production unless the first-export country lists the item, and the eCFR footnote records that the Netherlands listed it on 9 September 2024. The December 2024 rule exempts exporters located in Supplement No. 4 countries (the Netherlands included, South Korea and Taiwan not) from the new SME FDP licence requirements, and states that the Footnote 5 FDP rule "does not generally apply" to those destinations. US hooks remain: limits on support by US persons, licence requirements on US-origin parts, Entity List rules, and a Footnote 5 licence requirement for 3B993 items exported by Supplement No. 4-headquartered firms from countries outside A:5. Washington can widen its reach by amending Supplement No. 4 or by enacting MATCH, whose two versions reach items with "more than zero percent de minimis" US content and items containing chips "presumptively" made with EAR-subject tools. Theta is therefore a US policy choice with a cost, as the memo says.

For the hold-up, no current FDP or de minimis provision imposes a licence requirement on ASML shipments to Taiwan or South Korea. Section 734.4(a)(3) is keyed to an advanced-node end use rather than a destination, but it does not apply to Dutch-first-exported tools, and licence requirements for 3B993 items are destination-based. An export control can deny a shipment; it cannot compel one. The US counter-levers in a hold-up are physical: ASML staff, parts and repair centres on US soil, Cymer's San Diego operations, and whatever Taipei and Seoul do with ASML assets on theirs. Whether the Defense Production Act could order ASML's US subsidiaries to supply is a legal question we have not checked.

**US-origin share.** No public source measures the US share of ASML tool value. North American firms are 27% of EUV suppliers by count, and "3/4 of light source costs are from Europe" (SIA/BCG 2021, Exhibit 13). BIS needed a tool-specific 0% de minimis rule in 2023, which we read as evidence that controlled US content in at least some China-bound immersion tools was below the 25% threshold; the rule text gives a different stated rationale (it "recognizes the advancement of the state-of-the-art"), so this remains our inference. The memo's 15% (DUVi) and 20% (EUV) central values are guesses with low confidence.

**Cost of interruption.** Two scopes must be kept apart. In the scenario's 2029 ACI vote, the measure targets fabs in Arizona. ASML's whole US-sited revenue was EUR 4.09bn in 2025 (12.5% of sales, EUR 0.34bn a month), and the US can compel the servicing organization on its soil, so Europe's servicing lever over US-sited fabs runs only through new parts, optics and software. The 2031 threat is broader. For that scope, TSMC's 2025 wafer revenue was NT$3,272.6bn (US$104.3bn at the NT$31.37 rate implied by the 20-F). Nodes at 5nm and below were 60% of wafer revenue and 7nm (which includes EUV-using N6) another 14%; North American customers, defined by headquarters, were 75% of net revenue. EUV-node wafer revenue from US-headquartered customers is therefore US$3.9bn to US$4.8bn a month. With a downstream multiplier of 5 to 12 (SIA/BCG's one-year Taiwan scenario implies 490/42, about 11.7) and a post-buffer output loss of 10% to 70%, c_U runs from about US$2bn to US$40bn a month, central about US$13bn, close to NVIDIA's Data Center revenue of about US$16bn a month. These are revenues at risk, not welfare losses, and they omit Korean DRAM and HBM. Europe's own flow cost of a broad interruption is about EUR 1.9bn a month of ASML revenue on a 2025 basis (non-China share 70.9%).

**China.** ASML recognized 996 ArFi units from 2015 to 2025. Applying the memo's assumed China shares gives about 300 (low), 345 (central) and 390 (high). Its upper bound of 430 needs about 40 pre-2015 tools in China, which we could not verify. IO+ (unattributed) says "more than 300", and AEI says "several hundred". The three-year half-life for advanced-node use without ASML service is an assumption with no source behind it. Domestic DUVi output (about 5 tools in 2026 and 20 in 2027, per The Information via TrendForce) remains small next to the roughly 90 ArFi tools AEI says Chinese firms bought in 2024, and next to the 40 ArFi units ASML recognized worldwide in Q3 2026 alone, when China took 23% of system sales.

## Verified facts table

Verdicts: V = verified as stated; C = verified after correction (corrected wording shown); U = unverifiable; F = false.

| # | Claim (corrected where needed) | Verdict | Source (date) | Note |
|---|---|---|---|---|
| 1 | Europe 2031, March 2031 chapter: the US claims "through its Taiwanese partners, it has amassed enough EUV machines and maintenance know-how to forego ASML access for longer than Europe can forego access to frontier AI." | V | https://europe2031.ai (11 June 2026) | Authors: Juijn, van Baarsen, Dada, Negele, Stelling, Fox, Petropoulos, Bakker; Tom Chivers is credited for copywriting and editing, not as author. |
| 2 | Europe 2031, 2029: the proposed ACI measure is "restricting ASML's exports and servicing to American fabs in Arizona"; it fails QMV (NL and Ireland oppose, Poland and the Baltics oppose, Italy abstains). | V | https://europe2031.ai (11 June 2026) | New to this strand. Sets the scope of the scenario's own servicing threat. |
| 3 | Bloomberg via Taipei Times: ASML "can remotely force a shut-off which would act as a kill switch"; EUVs need such frequent upkeep that "without ASML's spare parts they quickly stop working"; ASML offers "certain customers joint service contracts where they do some of the routine maintenance themselves", allowing "clients such as TSMC" to access their own machines' systems; ASML says it cannot access customers' proprietary data; ASML, TSMC and the Dutch ministry declined to comment; the Netherlands ran invasion simulations. | V | https://www.taipeitimes.com/News/biz/archives/2024/05/22/2003818194 (22 May 2024, p. 12) | Anonymous sources. The article implies, but does not state, that TSMC holds a joint service contract. Original Bloomberg URL not checked. |
| 4 | Fomenkov et al. (2017): "Over 100 Billion pulses collector lifetime has been demonstrated"; reflectivity loss -0.6%/Gp (SPIE 2016) and -0.4%/Gp (SPIE 2017) on NXE-3300 collectors; "a target of 30 000 h was set for the most critical components of the source"; the collector is "arguably the most critical component in terms of lifetime"; CO2 laser operated "at ~50 kHz". | V | https://doi.org/10.1515/aot-2017-0029 (online 8 June 2017) | Figure 17B plots reflectivity to 200 Gp, so 100 Gp is not a hard limit. Text read from a project copy of the publisher PDF (see method). |
| 5 | Our arithmetic: at 50 kHz, 1 Gp = 5.56 hours of firing; 100 Gp = 23.1 days of continuous firing; 30,000 h = 5,400 Gp. | V | Arithmetic on row 4 | Calendar life is longer by the inverse of the burst duty cycle (not sourced). |
| 6 | The tin-droplet conversion "takes place 50,000 times per second." | V | ASML 20-F FY2021, https://www.sec.gov/Archives/edgar/data/937966/000093796622000013/asml-20211231.htm (9 Feb 2022) | SIA/BCG Exhibit 13 also says "50k molten tin droplets". The Trumpf source cited in the memo was not checked. |
| 7 | Brandt, Fomenkov and Graham (2021), abstract: "Over 85 EUV scanners are installed at customer factories"; "the latest generation of EUV sources are operating at 250W with 92% availability". | V | https://doi.org/10.1117/12.2601822 (30 Sept 2021); abstract via Semantic Scholar record | New. Source availability, not tool availability; no collector lifetime in the abstract. |
| 8 | Zhu et al. (2025), abstract: source power has doubled since the 250 W source of 2018; High-NA and 500 W EUV sources are "now operating at customer sites"; next-generation >600 W sources use a new laser architecture with "improved tin debris characteristics". | V | https://doi.org/10.1117/12.3052048 (22 April 2025); abstract via Semantic Scholar record | New. No lifetime figures in the abstract. |
| 9 | With OEM service, EUV systems in 2016 achieved "a four-week availability of more than 80 percent regularly"; best "more than 90 percent over four weeks"; consistency across systems and sites "still needs to be improved". | V | ASML 20-F FY2016 and FY2017, https://www.sec.gov/Archives/edgar/data/937966/000093796618000007/a2017integratedreportbased.htm (7 Feb 2018) | The FY2017 report repeats the 2016 sentence and adds that systems achieved >80% "more regularly" in 2017. |
| 10 | 95% of all (refurbished) systems sold in the past 30 years were still active at end-2024 and end-2025. ASML assumes that "of the machines no longer serviced by ASML, 33% are still active in the field", and says it anticipates it "will not report on this performance indicator going forward". | C | ASML 20-F FY2025, https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/asml-20251231.htm (25 Feb 2026); FY2024 | The memo presented 95% as what OEM service buys. The figure includes unserviced machines through an assumption. |
| 11 | "For EUV, we will continue to leverage our large and growing systems installed base to provide high-value service and upgrades over a lifetime of more than 20 years" (FY2024); FY2025 says "For both EUV and DUV". ASML guarantees support and spare parts per platform until committed dates, "subject to export control limitations". | C | ASML 20-F FY2024 and FY2025 | Memo attributed the 20-year phrase to EUV only, citing FY2025. |
| 12 | "Around 10,000 customer support employees" (FY2025; "more than 10,000" in FY2024). Headcount by country (only those above 10% of staff), end-2025: Netherlands 23,707; Taiwan 4,548; United States 8,242; total 44,175 (US share 18.7%). | V | ASML 20-F FY2025 | Customer-support staff by country not disclosed. |
| 13 | Repair centres: Hwaseong, Linkou, Beijing, Wilton, San Diego, Vancouver (WA), Veldhoven. Hwaseong campus used "for office, training and local repairs". Cymer Pyeongtaek: "a manufacturing site of light sources" (FY2025) versus "mainly used for refurbishment activities of light sources" (FY2023, FY2024). A second-line EUV customer support engineer is profiled in Chandler, Arizona, where ASML's US head office is. | V | ASML 20-F FY2023, FY2024, FY2025 | |
| 14 | Service contracts take the form of "full-service agreements, limited manpower agreements, other labor agreements, parts availability or parts usage agreements", typically fixed-price over a specified period. Time-based licence support is "integral to the customer's ability to continue to use the software license". | V | ASML 20-F FY2025 and FY2024 | |
| 15 | Variable consideration "dependent on the final volume of systems ordered by the customer or the system performance" appears in "most of our volume purchase agreements". | C | ASML 20-F FY2025 | The memo said some service contracts have performance-based prices. The 20-F says this of volume purchase agreements. |
| 16 | Risk factors: installed-base revenue may fall because "customers may perform more of these services themselves, find other third-party suppliers to provide them, or we may be limited by export control restrictions"; "potential nationalization of assets"; cross-strait changes "could affect our ability to serve customers in Taiwan", who were 25.5% of 2025 total net sales. | C | ASML 20-F FY2025 | Memo quoted "ability to service our customers in Taiwan"; the text says "serve". |
| 17 | LTI 2026 to 2028 ESG sub-measure (5% weight): "Localization of service part repair ... (% of service parts that were sent for repair locally)", threshold 50%, target 60%, stretch 70%. | V | ASML 20-F FY2025, remuneration report | Framed as reducing logistics emissions. |
| 18 | Carl Zeiss SMT is "our sole supplier of lenses, mirrors, illuminators, collectors and other critical optical components" under an exclusive arrangement; its capacity limits ASML output. | V | ASML 20-F FY2025 | |
| 19 | EUV source materials face "corrosive liquid tin"; "strategic tantalum alloys and molybdenum" are "limited in availability and costly". | V | ASML 20-F FY2023, https://www.sec.gov/Archives/edgar/data/937966/000093796624000008/asml-20231231.htm (14 Feb 2024) | Not repeated in FY2024. |
| 20 | ASML inventories at end-2025: raw materials EUR 5,298.5m, work in process EUR 4,768.5m, finished products EUR 2,135.1m; the increase is "mainly due to increasing raw materials to support our growing install base" and buybacks. | V | ASML 20-F FY2025, inventory note | New. Location of service-part stocks not disclosed. |
| 21 | EUV systems recognized: 2013 1; 2014 5; 2015 1; 2016 4; 2017 11; 2018 18; 2019 26; 2020 31; 2021 42; 2022 40; 2023 53; 2024 44 (2 EXE); 2025 48 (4 EXE). Sum 2013 to 2025 = 324; 2017 to 2025 = 313. | V | ASML 20-F FY2015, FY2016, FY2017, FY2019, FY2021, FY2023, FY2024, FY2025 | Units are "net system sales in units", i.e., recognized, not shipped. |
| 22 | ASML expects "to ship around 65 Low NA EUV systems" in 2026; 2027 Low-NA "close to being fully covered with orders". | V | ASML Q2 2026 investor call transcript (15 July 2026), via asml_facts.md | Transcript text re-read from the project copy. |
| 23 | ArFi units recognized: 2015 67; 2016 70; 2017 76; 2018 86; 2019 82; 2020 68; 2021 81; 2022 81; 2023 125; 2024 129; 2025 131. Sum 2015 to 2025 = 996 (2013: 77; 2014: 76). | V | Same 20-F filings as row 21 | Counts include used systems sold. |
| 24 | Q3 2026: total net sales EUR 11,662m; Installed Base Management EUR 3,289m; gross margin 57.5%; net system sales EUR 8.4bn by ship-to: Taiwan 32%, South Korea 31%, China 23%, USA 13%, rest of Asia 1%; units: EUV 17, ArFi 40. | V | ASML 6-K, https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/pressreleasefinancialresul.htm and presentation p. 9 (14 Oct 2026) | |
| 25 | ASML 2025: total net sales EUR 32,667.3m; China 29.1%, Taiwan 25.5% of total net sales; US-sited sales EUR 4,089.1m (12.5%); Installed Base Management EUR 8,193.0m. | V | ASML 20-F FY2025 | Basis for l and l_AZ. |
| 26 | TSMC 2025: net revenue NT$3,809,054m (US$121,423m); wafer revenue NT$3,272,553.5m (85.9% of net revenue); 3nm 24%, 5nm 36%, 7nm 14% of wafer revenue (74% at 7nm and below); North America 75% of net revenue, categorized "mainly based on the countries where our customers are headquartered"; supplies and spare parts NT$24,818.8m; first Arizona facility "entered high volume production at the end of 2024"; 2nm "entered volume production in 2025". | C | TSMC 20-F FY2025, https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm (16 April 2026) | Correction: node shares apply to wafer revenue, and North America is by customer HQ. |
| 27 | TSMC's 20-Fs for FY2023, FY2024 and FY2025 contain no mention of "EUV", "ultraviolet", "ASML" or "lithography". TSMC's share of the EUV installed base has no primary source. | V | TSMC 20-F FY2023 (filed 18 April 2024), FY2024 (17 April 2025), FY2025 | |
| 28 | NVIDIA FY2026 (ended 25 Jan 2026): revenue US$215,938m; Data Center US$193,737m; United States US$149,617m; customers headquartered outside the US 31% of revenue; uses TSMC and Samsung for wafers and buys memory from SK Hynix, Micron and Samsung; depends on "consistent and reliable supply from our overseas partners, especially in Taiwan and South Korea". | V | NVIDIA 10-K, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm (25 Feb 2026) | |
| 29 | SK hynix began mass production of 1a nm DRAM with EUV ("the first time that SK hynix adopted the EUV equipment for mass production") and plans EUV "for production of all its 1anm DRAM products going forward". | V | https://news.skhynix.com/sk-hynix-starts-mass-production-of-1anm-dram-using-euv-equipment/ (12 July 2021) | Blackwell on TSMC 4NP and N2 in 4Q25 were verified in lit_ai.md, not rechecked here. |
| 30 | SIA/BCG: in a one-year complete disruption, "Taiwanese foundries would lose their current cumulative $42 billion in revenues" and device makers would see "a $490 billion drop in revenue, or 12 times more"; replacement would take "a minimum of three years and $350 billion". | V | https://www.semiconductors.org/wp-content/uploads/2021/05/BCG-x-SIA-Strengthening-the-Global-Semiconductor-Value-Chain-April-2021_1.pdf (PDF dated 10 May 2021) | Device-maker figure based on the share of device applications supplied by Taiwanese fabs (footnote 14). |
| 31 | SIA/BCG Exhibit 13: EUV tool has "about 100,000 parts provided by over 5,000 suppliers"; suppliers by count: Netherlands 32%, North America 27%, Asia 27%, EMEA excluding Netherlands 14%. Light source: Cymer (US, ASML subsidiary), "Note: 3/4 of light source costs are from Europe". Trumpf CO2 laser, Zeiss optics, Berliner Glas wafer chuck, VDL vessel, Edwards vacuum system (UK). Source line: "ASML; expert interview; BCG research and analysis". | V | Same PDF, pp. 29 to 30 | |
| 32 | Rhodium: a blockade puts "well over two trillion dollars" of activity at risk (a floor); chip-dependent firms "could be forced to forego as much as $1.6 trillion in revenue annually", assuming revenue at risk is proportional to the share of chips sourced from TSMC. | V | https://rhg.com/research/taiwan-economic-disruptions/ (14 Dec 2022) | |
| 33 | 15 CFR 734.4(a)(3): no de minimis for 3B993.f.1 equipment destined for advanced-node IC development or production "unless the country from which the foreign-made item was first exported has this commodity specified on an export control list"; footnote: Japan listed it on 23 July 2023 and the Netherlands "on September 9, 2024". | V | eCFR as of 26 Oct 2026, https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.4 | The rule is keyed to end use, not destination. |
| 34 | 15 CFR 734.4(c)-(d): reexports with controlled US content of 10% or less are outside the EAR to any country; 25% or less to countries other than E:1 and E:2. | V | Same | |
| 35 | 88 FR 73424 (25 Oct 2023), interim final rule: adds 734.4(a)(3), a 0% de minimis rule for 3B001.f.1.b.2.b lithography for advanced-node production, except where the first-export country lists the item; for exports from countries without equivalent controls "BIS retains jurisdiction". | V | https://www.govinfo.gov/content/pkg/FR-2023-10-25/html/2023-23049.htm | Pages 73424 to 73455. |
| 36 | 89 FR 96790 (5 Dec 2024), interim final rule: new 734.4(a)(8) (no de minimis for listed 3B items containing a US-origin IC when destined for Macau or D:5, unless excluded under 742.4(a)(4) or 742.6(a)(6)); exclusion applies when the exporter is "located in a country specified in supplement no. 4 to part 742" and not headquartered in Macau or D:5; "The FN5 FDP does not generally apply to the destinations identified in new supplement no. 4"; licence required for 3B993 items exported from countries outside A:5 by entities headquartered in Supplement No. 4 countries (Footnote 5 scenario). Supplement No. 4 lists 33 countries including the Netherlands; not South Korea or Taiwan. | C | https://www.govinfo.gov/content/pkg/FR-2024-12-05/html/2024-28270.htm (pages 96790 to 96830) | Correction of emphasis: the exclusion turns on where the exporter is located and headquartered. lit_ai.md overstates the rule's reach. |
| 37 | CSIS (Allen and Goldston): under the December 2024 FDPR, US-origin ICs include "any such chips manufactured with U.S. machines, meaning that effectively all chips on earth are considered U.S. origin"; "Allied countries surveyed in this paper only apply services controls for WMD end-uses"; quoting Kevin Wolf, Japanese and Dutch firms "will still be able to export to China items and services that U.S. competitor companies cannot". No estimate of US content in ASML tools. | V | https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export (14 March 2025) | The items-and-services line is Wolf's testimony quoted in the report. |
| 38 | ASML 20-F: "under Dutch, US and other applicable laws, we are required to secure export licenses for EUV systems, specific DUV immersion systems"; US measures include "limitations on support by US persons for non-US origin items destined for advanced-node fabs in China"; US licences for foreign nationals to work on controlled US items have "become increasingly difficult". | V | ASML 20-F FY2025 | |
| 39 | S. 4281 (MATCH), introduced 13 April 2026 by Sen. Ricketts with Sens. Kim, Risch and Schumer, referred to Banking. Applicable items include foreign items "with more than zero percent de minimis United States-origin content" and items with ICs "presumptively designed or produced" with EAR-subject technology or equipment. "Servicing" covers work "whether in-person or remote", including "updating software or firmware", diagnosing, troubleshooting and "transfer of industry best practices for maintenance". Countrywide controls exclude fabs that existed at enactment and remain owned and operated by firms headquartered outside countries of concern. | V | https://www.govinfo.gov/content/pkg/BILLS-119s4281is/html/BILLS-119s4281is.htm | No action after referral could be checked (API rate limit). |
| 40 | H.R. 8170 (MATCH), introduced 2 April 2026 by Rep. Baumgartner with 10 original cosponsors. Without allied certification after 150 days, the "covered agency heads" (BIS Under Secretary and Secretary of State, in coordination with Energy and Defense) must "establish U.S. jurisdiction" over covered equipment "whether by establishing jurisdiction over such items and applying controls directly, or by restricting the end-uses of essential components ... or both", and require a licence, with a policy of denial, "for all servicing" at covered facilities. Applicable items include those with "more than zero percent de minimis controlled United States-origin content". Same servicing definition as S. 4281. Ordered reported in the nature of a substitute, 36 to 8, on 22 April 2026; no later action. | C | https://www.govinfo.gov/content/pkg/BILLS-119hr8170ih/html/BILLS-119hr8170ih.htm; Congress.gov API (checked 29 Oct 2026) | Text checked is as introduced; the committee substitute was not available. Covered facilities are in countries of concern, so TSMC and Samsung fabs outside China are not reached. |
| 41 | AEI: "SMIC and its peers likely acquired close to 90 ArFi machines" in 2024; "Chinese entities accounted for 70 percent of ASML's DUVi tool sales in 2024"; China has "several hundred existing DUVi machines"; they "require specialized maintenance approximately every six months", which "ASML itself often provides on-site in China"; China's fleet "could remain operational indefinitely" if servicing is not restricted. No discussion of spare parts or third-party servicing. | V | https://www.aei.org/research-products/report/the-lithography-loophole-how-china-is-printing-its-way-to-chip-self-sufficiency/ (21 April 2026) | |
| 42 | TrendForce: China "imported 95 DUV systems in 2025 alone" (HKCNA); state-backed Shanghai Aishengna leads China's production, with SMEE and other local lithography teams named by Reuters as contributors; the programme targets "around five DUV systems in 2026 and roughly 20 in 2027" (The Information), first deliveries in 2026 to SMIC, Hua Hong and CXMT; NU.nl reports the US may push restrictions to "servicing of machines already delivered". | C | https://www.trendforce.com/news/2026/08/25/news-u-s-may-push-near-total-asml-china-ban-on-duv-sales-and-servicing-amid-chinas-domestic-lithography-push/ (25 Aug 2026) | The memo said Aishengna "absorbed" SMEE's teams; the article says they contribute. |
| 43 | IO+: "the $1 billion to $1.5 billion in service revenue usually cited" (unattributed); "More than 300 of these machines are now thought to be running in Chinese fabs" (unattributed). | V | https://ioplus.nl/en/posts/asml-caught-between-us-and-china-over-match-act (12 Oct 2026) | Low-quality figures; usable only as a rough cross-check. |
| 44 | Gigaphoton GT66A ArFi light source: "We have extended the module maintenance cycle by 30% by introducing the latest high durability components"; "a high level of availability"; no absolute lifetimes. | C | https://www.gigaphoton.com/en/products/7536 (accessed 29 Oct 2026) | The GT80A appears only in a product list; the 30% claim is not verified for it. |
| 45 | China installed base of ASML ArFi tools: 300 / 345 / 390 from 2015 to 2025 under the memo's China-share assumptions; 430 requires about 40 pre-2015 tools. | C | Our arithmetic on rows 23 and 41 | Shares for 2015 to 2022 and 2025 are assumptions. |
| 46 | ASML China servicing revenue of EUR 0.7 / 1.2 / 2.0bn a year. | U | Memo's bound | ASML does not disclose it. |
| 47 | China fleet half-life without ASML service of 12 / 36 / 72 months. | U | None | Pure assumption; ASML's 33% survival assumption for unserviced machines (row 10) is the only adjacent number. |
| 48 | US-origin share of ASML tool value (DUVi 5 / 15 / 25%; EUV 10 / 20 / 35%). | U | Indirect bounds in rows 31 and 35 | No public measurement. |
| 49 | Bloomberg Economics' January 2024 estimate of the cost of a Taiwan war (about US$10tn). | U | Not fetched | Excluded, as in the memo. |
| 50 | TSMC's 56% share of the global EUV installed base. | U | No primary source | Excluded, as in the memo. |

## Citation verdicts

| Key | Verdict | Note |
|---|---|---|
| fomenkov2017light | verified | Metadata matches Crossref (AOT 6(3-4): 173-186, 21 authors). Content as characterized. |
| brandt2021performance | verified | Proc. SPIE 11854 confirmed via Crossref resource URL. Abstract now read: >85 scanners in HVM, 250 W sources at 92% availability. Article number not verified (Crossref page field 46). |
| zhu2025evolution | verified | Proc. SPIE 13424 confirmed. Abstract read: 500 W sources at customer sites, >600 W next generation. |
| salmaso2026euv | verified | Metadata only (Proc. SPIE 13979). No abstract available. |
| matsumoto2024maximizing | verified | Metadata only (Proc. SPIE 12953). No abstract; Gigaphoton affiliation assumed, not verified. |
| varas2021strengthening | verified | Title confirmed on the SIA report page; authors in the PDF's "About the Authors". |
| vest2022global | verified | |
| allen2025allies | verified | One quoted line is Kevin Wolf's testimony reproduced in the report. |
| fedasiuk2026aei | verified | |
| asml2026annual | verified | Metadata correct. Two characterizations drawn from it in the memo were wrong (95% indicator; variable pricing) and are corrected in the facts table. |
| tsmc2026annual | verified | Node shares are of wafer revenue. |
| nvidia2026annual | verified | |
| bis2024fdpr | verified | Interim final rule. Exclusion turns on exporter location and headquarters. |
| bis2023sme | verified | Interim final rule; request for comments. |
| ecfr7344 | verified | Checked as of 26 Oct 2026. |
| hr8170 | verified | Duties fall on covered agency heads, not BIS alone. Reported with a substitute amendment on 22 April 2026. |
| s4281 | verified | |
| bloomberg2024killswitch | verified | Taipei Times p. 12, Bloomberg wire. |
| trendforce2026duv | corrected | Headline reads "Amid China Domestic Lithography Push", not "China's". |
| juijn2026europe (added) | verified | |
| asml2022annual, asml2024annual, asml2018annual, asml2026q3 (added) | verified | Sources for rows 6, 9, 19, 24. |

## Modeling implications

Proposition 6's interruption corollary (model_design_v2.md, Section 8) says an interruption raises P* iff beta (1 - h) c_S exp(-(r + lambda) t_U) > (1 - beta) l. The memo's mu is the model's h. The calibration below maps onto those symbols.

**1. Model two threat scopes, not one.** The scenario itself has two. In the 2029 ACI vote the target is fabs in Arizona; in 2031 the claim concerns "Taiwanese partners". For the Arizona-only scope, l_AZ is at most EUR 0.34bn a month (all US-sited ASML sales in 2025) and h_AZ is near one, because ASML's US staff, parts and repair centres are on US soil and US persons are subject to US law. The corollary then predicts that the Arizona-only measure has little bite on the servicing channel whatever c_S is. Its bite runs only through optics, modules and software that Europe ships, which favours modelling it as a supply cut with a parts buffer rather than a labor cut. For the broad scope, h depends on Taipei and Seoul, not on Washington alone, which brings Taiwan and Korea into the game as third parties.

**2. Parameter table (broad scope unless stated).**

| Parameter | Low | Central | High | Basis | Confidence |
|---|---|---|---|---|---|
| t_U (months) | 1 | 6 | 24+ | Rows 3, 4, 5, 7, 20 | LOW. Anchors span 23 days of continuous firing (2017) to a 30,000 h design target. |
| h (share of servicing the US side can compel) | 0.5 | 0.7 | 0.85 | Rows 12 to 17, 20 | LOW. Our judgment; no country split of service staff or parts. |
| h_AZ (Arizona-only scope) | 0.85 | 0.95 | 1 | Rows 12, 13, 38 | LOW to MEDIUM. US jurisdiction over US-sited staff and parts. |
| c_S = c_U (USD bn a month, revenue at risk) | 2 | 13 | 40 | Rows 26, 28, 30 | Inputs HIGH, scaling LOW. Formula: s x R x 0.75 x m, R = 0.60 to 0.74 of US$104.3bn / 12, m = 5 / 10 / 12, s = 0.1 / 0.3 / 0.7. Rhodium cross-check for total loss: about 60. |
| l (EUR bn a month) | 0.6 | 1.9 | 3.0 | Rows 24, 25 | MEDIUM-HIGH. Revenue, not profit (Q3 2026 gross margin 57.5%). |
| l_AZ (EUR bn a month) | | at most 0.34 | | Row 25 | HIGH as an upper bound. |
| theta_current, China-bound DUVi and servicing shipped from NL | 0.1 | 0.25 | 0.4 | Rows 33, 36, 38 | Legal text HIGH, numbers LOW. |
| theta_latent (after MATCH or Supplement No. 4 change) | 0.8 | 0.9 | 0.95 | Rows 39, 40 | Legal text HIGH, numbers LOW. |
| US-origin share of tool value, DUVi / EUV | 5 / 10% | 15 / 20% | 25 / 35% | Rows 31, 35 | LOW. |
| China ArFi installed base (tools) | 300 | 345 | 390 (430 with pre-2015) | Rows 23, 41, 43, 45 | LOW-MEDIUM. |
| China fleet half-life without ASML (months) | 12 | 36 | 72 | None | LOW. Assumption. |

**3. A sharp threshold in h.** Set beta = 1/2. At t_U = 0 the interruption raises P* only if h < h* = 1 - l / c_S. With central values, c_S / l is about 6 to 7 for any USD/EUR rate between 1.0 and 1.2, so h* is about 0.85. At the low c_S the interruption never pays; at the high c_S, h* is about 0.95. The memo's high value of h sits on the threshold. With an illustrative r + lambda of 0.55 a year (our assumption), the corollary's cutoff tbar = ln[(1 - h) c_S / l] / (r + lambda) is about 26 months at h = 0.5, about 15 months at h = 0.7, and does not exist at h = 0.85. Against a central t_U of six months, the broad hold-up is credible when h is 0.7 or below and fails at 0.85. The result turns more on h than on t_U, and h is the parameter with the least evidence behind it.

**4. Comparative statics to state in the paper.** d tbar / d h < 0, so ASML's localization of repair (the 50% to 70% LTI target) and local parts stocks raise h and erode Europe's hold-up option. ASML's commercial and ESG choices act on Dutch leverage, which gives a Dutch state that wants to keep the option a reason to regulate where parts are stored and repaired. The same logic makes Germany a necessary member of any credible European interruption, because the scarce flows that cannot be commandeered (Zeiss optics, Trumpf lasers) are German.

**5. Output loss is gradual.** Collector reflectivity falls by fractions of a percent per Gpulse and source availability was 92% at 250 W in 2021. Model the post-buffer US flow cost as rising in t (c_U(t) = s(t) c_bar with s increasing from 0), which the master game already allows (c_i(t) piecewise continuous). A step function at t_U overstates how sharply pain arrives.

**6. Theta.** Keep the memo's treatment: theta is a US policy variable whose increase (amending Supplement No. 4, enacting MATCH) carries allied-friction costs that belong in the US payoff. For the hold-up subgame, do not invoke theta at all. No current rule gives Washington licence authority over ASML shipments to Taiwan or Korea, and no export rule can compel supply.

**7. China.** Let W_H decay with a half-life parameter and with domestic DUVi output, but present the half-life as a free parameter with comparative statics, not as a calibrated number.

## Open questions

1. What do the SPIE status papers report on collector lifetime (Gp), droplet-generator runtime and field tool availability for the NXE:3800E and EXE generations (Salmaso et al. 2026; Zhu et al. 2025 full text; De Ruiter et al. 2026, whose DOI we did not check)? These numbers would move t_U more than anything else.
2. What is the burst duty cycle of an EUV source in HVM? It converts Gpulses to calendar time.
3. Where does ASML hold its EUR 5.3bn of raw materials and service parts, and how much sits in Taiwan, Korea and the US?
4. Can TSMC, Samsung or Intel swap collectors and droplet generators without ASML engineers under limited-manpower or joint-service contracts? Who holds spare collectors, and are they refurbished only in Oberkochen?
5. What is the technical basis of the remote-disable claim, and how much scanner software needs licence renewal or remote access?
6. Could Taiwan's or Korea's government legally commandeer ASML staff, parts and repair centres in a crisis? Does the Defense Production Act reach ASML's US subsidiaries (Cymer, ASML US)?
7. What does the House Foreign Affairs Committee substitute for H.R. 8170 change relative to the introduced text, and has S. 4281 moved?
8. Is there any primary source for TSMC's share of the EUV installed base?
9. Do Gigaphoton or Chinese suppliers (for example Beijing RSLaser) service ArF excimer lasers at Chinese fabs? This decides China's fleet half-life.

## BibTeX (verified or corrected entries)

```bibtex
@article{fomenkov2017light,
  author  = {Fomenkov, Igor and Brandt, David and Ershov, Alex and Schafgans, Alexander and Tao, Yezheng and Vaschenko, Georgiy and Rokitski, Slava and Kats, Michael and Vargas, Michael and Purvis, Michael and Rafac, Rob and La Fontaine, Bruno and De Dea, Silvia and LaForge, Andrew and Stewart, Jayson and Chang, Steven and Graham, Matthew and Riggs, Daniel and Taylor, Ted and Abraham, Mathew and Brown, Daniel},
  title   = {Light Sources for High-Volume Manufacturing {EUV} Lithography: Technology, Performance, and Power Scaling},
  journal = {Advanced Optical Technologies},
  volume  = {6},
  number  = {3-4},
  pages   = {173--186},
  year    = {2017},
  doi     = {10.1515/aot-2017-0029}
}

@inproceedings{brandt2021performance,
  author    = {Brandt, David C. and Fomenkov, Igor V. and Graham, Matthew},
  title     = {Performance and Availability of {EUV} Sources in High Volume Manufacturing on Multiple Nodes in the Field and Advances in Source Power},
  booktitle = {International Conference on Extreme Ultraviolet Lithography 2021},
  series    = {Proceedings of SPIE},
  volume    = {11854},
  year      = {2021},
  doi       = {10.1117/12.2601822},
  note      = {Crossref page field 46; article number not verified}
}

@inproceedings{zhu2025evolution,
  author    = {Zhu, Qiushi and Schafgans, Alexander A. and Stewart, Jayson and Rich, Spencer and Purvis, Michael and Wang, Haining and Hummler, Klaus and LaForge, Andrew D. and Mayer, Peter and Urone, Dustin M. and Biabani, Omar and Dorobantu, Andrei and Ma, Yue and Rollinger, Bob},
  title     = {Evolution of {EUV} Light Source Architecture for Continued Advancements in {EUV} High Volume Manufacturing},
  booktitle = {Optical and EUV Nanolithography XXXVIII},
  series    = {Proceedings of SPIE},
  volume    = {13424},
  year      = {2025},
  doi       = {10.1117/12.3052048},
  note      = {Crossref page field 47; article number not verified}
}

@inproceedings{salmaso2026euv,
  author    = {Salmaso, Guido and van Lare, Claire and Smeets, Christophe and Klomp, Peter and Kielczewski, Adam and de Jong, Ivo},
  title     = {0.33 {NA} {EUV} Systems for High-Volume Manufacturing},
  booktitle = {Optical and EUV Nanolithography XXXIX},
  series    = {Proceedings of SPIE},
  volume    = {13979},
  year      = {2026},
  doi       = {10.1117/12.3090477},
  note      = {Crossref page field 35; content not accessed}
}

@inproceedings{matsumoto2024maximizing,
  author    = {Matsumoto, Shinichi and Tanaka, Satoshi and Oga, Toshihiro and Komaki, Takamitsu and Wakana, Katsuhiko and Ohta, Takeshi and Saitou, Takashi},
  title     = {Maximizing Availability by Enhancing Operational Efficiency and Implementing Sophisticated Maintenance Strategies in Complex {ArFi} Light Source},
  booktitle = {Optical and EUV Nanolithography XXXVII},
  series    = {Proceedings of SPIE},
  volume    = {12953},
  year      = {2024},
  doi       = {10.1117/12.3009846},
  note      = {Crossref page field 55; content not accessed}
}

@techreport{varas2021strengthening,
  author      = {Varas, Antonio and Varadarajan, Raj and Goodrich, Jimmy and Yinug, Falan},
  title       = {Strengthening the Global Semiconductor Supply Chain in an Uncertain Era},
  institution = {Boston Consulting Group and Semiconductor Industry Association},
  year        = {2021},
  month       = apr,
  url         = {https://www.semiconductors.org/wp-content/uploads/2021/05/BCG-x-SIA-Strengthening-the-Global-Semiconductor-Value-Chain-April-2021_1.pdf}
}

@misc{vest2022global,
  author       = {Vest, Charlie and Kratz, Agatha and Goujon, Reva},
  title        = {The Global Economic Disruptions from a {Taiwan} Conflict},
  howpublished = {Rhodium Group},
  year         = {2022},
  month        = dec,
  url          = {https://rhg.com/research/taiwan-economic-disruptions/},
  note         = {Published 14 December 2022}
}

@misc{allen2025allies,
  author       = {Allen, Gregory C. and Goldston, Isaac},
  title        = {Understanding {U.S.} Allies' Current Legal Authority to Implement {AI} and Semiconductor Export Controls},
  howpublished = {Center for Strategic and International Studies, Wadhwani AI Center},
  year         = {2025},
  month        = mar,
  url          = {https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export},
  note         = {Published 14 March 2025}
}

@techreport{fedasiuk2026aei,
  author      = {Fedasiuk, Ryan and Torres, Julia},
  title       = {The Lithography Loophole: How {China} Is Printing Its Way to Chip Self-Sufficiency},
  institution = {American Enterprise Institute},
  year        = {2026},
  month       = apr,
  url         = {https://www.aei.org/research-products/report/the-lithography-loophole-how-china-is-printing-its-way-to-chip-self-sufficiency/},
  note        = {Published 21 April 2026}
}

@misc{asml2026annual,
  author       = {{ASML Holding N.V.}},
  title        = {Annual Report on Form 20-F for the Fiscal Year Ended December 31, 2025},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0001628280-26-011378},
  year         = {2026},
  url          = {https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/asml-20251231.htm},
  note         = {Filed 25 February 2026}
}

@misc{asml2024annual,
  author       = {{ASML Holding N.V.}},
  title        = {Annual Report on Form 20-F for the Fiscal Year Ended December 31, 2023},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0000937966-24-000008},
  year         = {2024},
  url          = {https://www.sec.gov/Archives/edgar/data/937966/000093796624000008/asml-20231231.htm},
  note         = {Filed 14 February 2024}
}

@misc{asml2022annual,
  author       = {{ASML Holding N.V.}},
  title        = {Annual Report on Form 20-F for the Fiscal Year Ended December 31, 2021},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0000937966-22-000013},
  year         = {2022},
  url          = {https://www.sec.gov/Archives/edgar/data/937966/000093796622000013/asml-20211231.htm},
  note         = {Filed 9 February 2022}
}

@misc{asml2018annual,
  author       = {{ASML Holding N.V.}},
  title        = {Annual Report on Form 20-F for the Fiscal Year Ended December 31, 2017},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0000937966-18-000007},
  year         = {2018},
  url          = {https://www.sec.gov/Archives/edgar/data/937966/000093796618000007/a2017integratedreportbased.htm},
  note         = {Filed 7 February 2018}
}

@misc{asml2026q3,
  author       = {{ASML Holding N.V.}},
  title        = {{ASML} Reports {\euro}11.7 Billion Total Net Sales and {\euro}5.0 Billion Net Income in {Q3} 2026},
  howpublished = {Exhibit 99.1 to Report on Form 6-K, U.S. Securities and Exchange Commission, EDGAR, accession 0001628280-26-065813},
  year         = {2026},
  url          = {https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/pressreleasefinancialresul.htm},
  note         = {Veldhoven, 14 October 2026. Regional split from the accompanying investor presentation, p. 9}
}

@misc{tsmc2026annual,
  author       = {{Taiwan Semiconductor Manufacturing Company Limited}},
  title        = {Annual Report on Form 20-F for the Fiscal Year Ended December 31, 2025},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0001628280-26-025362},
  year         = {2026},
  url          = {https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm},
  note         = {Filed 16 April 2026}
}

@misc{nvidia2026annual,
  author       = {{NVIDIA Corporation}},
  title        = {Annual Report on Form 10-K for the Fiscal Year Ended January 25, 2026},
  howpublished = {U.S. Securities and Exchange Commission, EDGAR, accession 0001045810-26-000021},
  year         = {2026},
  url          = {https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm},
  note         = {Filed 25 February 2026}
}

@misc{bis2024fdpr,
  author       = {{U.S. Department of Commerce, Bureau of Industry and Security}},
  title        = {Foreign-Produced Direct Product Rule Additions, and Refinements to Controls for Advanced Computing and Semiconductor Manufacturing Items},
  howpublished = {Federal Register 89: 96790--96830 (interim final rule)},
  year         = {2024},
  month        = dec,
  url          = {https://www.govinfo.gov/content/pkg/FR-2024-12-05/html/2024-28270.htm},
  note         = {FR Doc. 2024-28270, published 5 December 2024}
}

@misc{bis2023sme,
  author       = {{U.S. Department of Commerce, Bureau of Industry and Security}},
  title        = {Export Controls on Semiconductor Manufacturing Items},
  howpublished = {Federal Register 88: 73424--73455 (interim final rule; request for comments)},
  year         = {2023},
  month        = oct,
  url          = {https://www.govinfo.gov/content/pkg/FR-2023-10-25/html/2023-23049.htm},
  note         = {FR Doc. 2023-23049, RIN 0694-AJ23, published 25 October 2023}
}

@misc{ecfr7344,
  author       = {{Office of the Federal Register}},
  title        = {15 {CFR} 734.4, De Minimis {U.S.} Content},
  howpublished = {Electronic Code of Federal Regulations},
  year         = {2026},
  url          = {https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.4},
  note         = {Text as of 26 October 2026; title 15 up to date as of 27 October 2026}
}

@misc{hr8170,
  author       = {Baumgartner, Michael},
  title        = {{H.R.} 8170, Multilateral Alignment of Technology Controls on Hardware Act ({MATCH} Act), as Introduced},
  howpublished = {119th Congress, 2nd Session},
  year         = {2026},
  url          = {https://www.govinfo.gov/content/pkg/BILLS-119hr8170ih/html/BILLS-119hr8170ih.htm},
  note         = {Introduced 2 April 2026; ordered reported in the nature of a substitute, 36--8, 22 April 2026}
}

@misc{s4281,
  author       = {Ricketts, Pete},
  title        = {{S.} 4281, Multilateral Alignment of Technology Controls on Hardware ({MATCH}) Act, as Introduced},
  howpublished = {119th Congress, 2nd Session},
  year         = {2026},
  url          = {https://www.govinfo.gov/content/pkg/BILLS-119s4281is/html/BILLS-119s4281is.htm},
  note         = {Introduced 13 April 2026 with Sens. Kim, Risch and Schumer; referred to the Committee on Banking, Housing, and Urban Affairs}
}

@misc{bloomberg2024killswitch,
  author       = {{Bloomberg News}},
  title        = {{ASML} and {TSMC} Can Disable {EUV} Machines},
  howpublished = {Taipei Times, p. 12 (Bloomberg wire)},
  year         = {2024},
  month        = may,
  url          = {https://www.taipeitimes.com/News/biz/archives/2024/05/22/2003818194},
  note         = {Published 22 May 2024; anonymous sources}
}

@misc{trendforce2026duv,
  author       = {{TrendForce News}},
  title        = {[News] {U.S.} May Push Near-Total {ASML} {China} Ban on {DUV} Sales and Servicing Amid {China} Domestic Lithography Push},
  howpublished = {TrendForce},
  year         = {2026},
  month        = aug,
  url          = {https://www.trendforce.com/news/2026/08/25/news-u-s-may-push-near-total-asml-china-ban-on-duv-sales-and-servicing-amid-chinas-domestic-lithography-push/},
  note         = {Published 25 August 2026; no individual byline}
}

@misc{juijn2026europe,
  author       = {Juijn, Daan and van Baarsen, Stan and Dada, Judith and Negele, Maximilian and Stelling, Lily and Fox, Philip and Petropoulos, Alex and Bakker, Michiel},
  title        = {Europe 2031},
  howpublished = {Scenario website},
  year         = {2026},
  url          = {https://europe2031.ai},
  note         = {Published 11 June 2026; copywriting and editing by Tom Chivers}
}

@misc{skhynix2021euv,
  author       = {{SK hynix}},
  title        = {{SK} hynix Starts Mass Production of 1anm {DRAM} Using {EUV} Equipment},
  howpublished = {SK hynix Newsroom},
  year         = {2021},
  month        = jul,
  url          = {https://news.skhynix.com/sk-hynix-starts-mass-production-of-1anm-dram-using-euv-equipment/},
  note         = {Published 12 July 2021}
}
```
