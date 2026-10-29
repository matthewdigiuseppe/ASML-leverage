# Europe's side of the exit premium: alpha, r, kappa*S and t_E. Fact-checked gap memo (as of 29 October 2026)

Strand: gap_european_cost_parameters. Checks the memo that recalibrates Europe's exit premium Q and the break-even conditionality kappa* in Section 7 (`paper/sections/07_revisited.tex`, Figure `fig:breakeven`), using the exit-cost decomposition in `notes/model_design_v2.md` (Section 1, "Exit cost" and "Remark (untargeted Chinese punishment of alignment)").

## How this was checked, and its limits

The shared web-search budget for this turn was already used up when this check began; the one WebSearch call returned a refusal. Nothing below rests on a search-engine result. Every item was checked by retrieving the primary document or dataset directly, and most numbers were recomputed from the raw data:

- Crossref and OpenAlex records retrieved by DOI (not by search) for all eight journal and OECD items, including abstracts where deposited.
- Eurostat APIs re-queried on 29 October 2026: Comext DS-045409 (annual and monthly, CN 8505.11, last update 16 October 2026), `sts_inpr_m` (updated 28 October 2026), `nama_10_gdp` (updated 22 October 2026), `sbs_ovw_act`, `irt_lt_mcby_m`. ECB Data Portal for USD/EUR.
- ECB Economic Bulletin PDFs (5/2025, 6/2025, 2/2026, 6/2026) read in full text at the cited passages.
- IEA PDFs (rare earth report, created 7 April 2026; Global Critical Minerals Outlook 2026, created 15 July 2026), the CFR report page, the Kiel PDF and the Bruegel page, the ECFR PDF and its chart images.
- Epoch AI: three data-insight pages fetched fresh; `benchmark_data.zip` re-downloaded (its `eci_scores.csv` is byte-identical to the copy used by the memo); `ai_chip_trade_by_country.csv` re-downloaded (identical hash); GPU clusters CSV recomputed.
- Anthropic: both news posts on Fable 5, the Economic Index report page, and the country-level data files for the June 2026 and September 2025 releases.
- SEC EDGAR 10-K texts for Alphabet, Microsoft and Amazon, and ASML's FY2025 20-F.
- MOFCOM: all six cited pages fetched fresh and read in Chinese.
- Stars and Stripes (three articles), ABC News (May 2026 Germany withdrawal), ACEA (two press releases), EuroHPC call page, Council Regulation (EU) 2026/150 text.
- The memo's break-even script was rerun, and a separate script (`scratchpad/gapeu_scripts/recheck.py`) recomputed every derived number and ran alternative ranges.

What could not be checked without search: the IISS report itself (only the Stars and Stripes account), whether MOFCOM has amended Announcement 70 since 19 October, the OECD paper number, any GDP-loss estimate for a magnet cutoff from the Bundesbank, Kiel, ifo or JRC, and current (October 2026) revenue run-rates for the US labs.

## Verdict in brief

The memo is careful and its arithmetic reproduces. Its headline survives on its own ranges: the AI term and China's input lever move Q far more than the security term does. But the result is more fragile than the memo says, and several inputs need correcting.

1. **The sign of Q at central values turns on a small number.** With r = 15 and kappa*S = 12.5, Q is negative whenever alpha exceeds EUR 12bn a year (0.06% of EU GDP), which is the bottom of the memo's alpha range. The memo's low alpha (EUR 13bn) excludes the lowest published productivity estimate it cites. Acemoglu (2025) implies TFP gains of at most 0.66% over ten years, about 0.07 points a year, against the memo's low g of 0.2. With g = 0.07 and Delta = 4 months, alpha is about EUR 4bn, P(Q > 0) rises from 0.21 to 0.37 and the median Q moves from -25 to -10.
2. **Delta's low value is lenient.** Epoch's four-month open-weight lag uses a criterion under which an open model has "caught up" if it beats the earlier frontier model in at least 5% of bootstrap samples. With point estimates the lag is six months, and Epoch says the figure "may tend to understate the true gap." The insight's title is "Open models lag state-of-the-art closed models by 4 months" (29 May 2026). It does not say that all leading open models are Chinese.
3. **The magnet squeeze barely shows in the EU import data.** Year on year, EU imports of CN 8505.11 magnets from China fell 1% in May 2025, 5% in June and 25% in July, and total 2025 imports from China were 2.6% higher than in 2024 by weight. The memo's "fell by about a quarter in June and July" is true only against the January to March 2025 average.
4. **The Nexperia bound does not hold.** ACEA wrote on 29 October 2025 that assembly-line stoppages "might only be days away," so the October 2025 dip in EU motor-vehicle output (-4.9%) predates any stoppage. Monthly swings of this size are routine in the series (August 2025 -6.0%, April 2026 -4.9%, July 2026 -9.6%). The low r of EUR 3bn is an assumption, not a bound.
5. **MOFCOM's 15 October statement is a reciprocity framing, not an explicit condition.** He Yadong said China "is willing to continue" facilitating rare-earth licences for Europe and "also hopes" the EU will reciprocally facilitate key dual-use cases for China. That supports a graduated, reciprocal r, but "explicitly conditional" overstates it.
6. **IEA.** The "7-10% of IEA countries' GDP" phrasing is wrong. The rare earth report says exposure is "almost 10%" of the combined GDP of countries outside China; GCMO 2026 says "around 7%" for the same group. The IEA does not define "Europe" in the USD 1.5tn figure in the passages read.
7. **Anthropic, June 2026.** Cloud channels went dark because Anthropic disabled the models everywhere, not because hyperscalers acted on their own. The directive covered foreign nationals "whether inside or outside the United States," so it bound persons, not locations. The Opus 4.8 routing applies to requests blocked by the new classifier after redeployment. A 1 July update says Fable 5 and Mythos 5 were redeployed.
8. **"Nearly a quarter."** The scenario quote is verified, but the comparison should be Tier 2 Europe. The Netherlands and the UK are Tier 1 in the scenario. EU-27 minus the Netherlands is 14.4% to 16.0% of Claude.ai usage raw, 17.6% to 18.2% renormalised. The renormalisation residual is mostly usage with no geography ("not_classified" was 15.7% of usage in August 2025), so the renormalised share is an upper estimate.
9. **Smaller corrections.** Acemoglu's article is volume 40 (2025), not 2024. Filippucci, Gal and Schief (2026) report "up to 0.9" points of US TFP growth; the "0.3" lower bound is not in the abstract. The CFR title is "Dismantling China's Supply-Chain Weapon: A Transatlantic Strategy for Critical Minerals." The ECB's 2.2% (NATO definition) is for euro-area NATO members; all euro-area countries are at 2.0%, and the euro area now has 21 members. IISS also prices US personnel at USD 12.3bn a year, and its scenario assumes the US keeps the nuclear deterrent. Poland's spread widened 12 bp in May 2026 and 14 bp in September 2026, and Finland's 10 bp in January 2026; "did not widen" is too strong for monthly data that cannot settle the question either way.
10. **Script.** `breakeven.py` computes the Europe-favourable corner with alpha = 10 (kappa* = 1.91); the memo reports 1.84, which matches alpha = 13. The binning for alpha's variance share uses 10 as the lower bound. Neither changes the conclusions.
11. **Cross-strand inconsistency.** `notes/model_design_v2.md` (line 48) sets r_A = 0 because there is "no instance in the record." Nexperia is an instance. ACEA (29 October 2025) refers to "the political dispute that has led to the prohibition of Nexperia chip exports from China," which followed the Dutch Wbg order of 30 September 2025 (china_dep.md, lines 56 to 63). The memo's chi_r = 1 is right and the model note should be amended.

The memo's two framing corrections stand. DiGiuseppe and Poast (2018) is a military-spending substitution study (defense pacts and military expenditures, 1950 to 2001), not a bond-market study. Under the model's own exit-cost definition a credible Chinese punishment of alignment enters Q with a plus sign, so kappa* = (omega - chi_ai*alpha - chi_f*f - eta + chi_r*r)/S.

## Corrected synthesis

Section 7 currently prices Europe's exit premium with one term, the security guarantee, and gets kappa* = 9.5/250 = 0.038. The memo argues that once the AI lever and China's input lever are priced, the security term is the least consequential of the four. We agree with the direction and think the paper should say so. We disagree with how firmly the memo states it. The evidence pins down the order of magnitude of r and kappa*S reasonably well and leaves alpha uncertain by more than an order of magnitude, with its lower end understated.

**alpha.** The memo prices denial of US frontier AI as a productivity delay: alpha is roughly g x Delta x Y, where g is AI's contribution to annual labour productivity growth, Delta the capability lag of the best substitute Europe could use, and Y EU GDP (EUR 18,884.6bn in 2025). The inputs check out. Filippucci, Gal, Laengle and Schief (2025) estimate 0.4 to 1.3 points a year for the US and UK and gains "up to 50% smaller" in several other G7 economies. Epoch's ECI data give the substitute lags: on 28 October 2026 Kimi K3 (non-commercial licence) matched the US frontier of 5 March 2026 (7.8 months back); GLM-5.3 and Meta's Muse Spark Open (both "restricted use") and DeepSeek V4.1 Flash (unrestricted) matched the frontier of 11 December 2025 (10.5 months); Mistral Large 4 (access "unknown") matched 7 October 2025 (12.7 months). Two things widen the range. Acemoglu (2025), whom the memo cites as the lower anchor, implies about 0.07 points a year of TFP growth, so a defensible low alpha is about EUR 4bn rather than 13bn. And g x Delta assumes that productivity is limited by frontier capability. If diffusion is the binding constraint, as the OECD framework's emphasis on adoption suggests, a lag of a few months in capability costs much less than g x Delta. We would report alpha as EUR 4bn, 50bn and 130bn, with the high value conditional on capability-limited growth. The AI lever is conditional only if aligned Europe keeps better access than an exited Europe. In the scenario's 2029 world aligned Europe is already Tier 2, so the relevant alpha is the loss from Tier 2 to Tier 3, smaller than full denial.

The scenario's claim that "European customers currently account for nearly a quarter of US frontier inference" is plausible for wider Europe and too high for Tier 2 Europe. Anthropic's June 2026 release puts the EU-27 at 15.4% (April) and 17.0% (May) of Claude.ai usage and the EU-27 minus the Netherlands at 14.4% to 16.0%. API traffic has no geography. No measured cost of the June 2026 suspension exists; it lasted from 12 June to 30 June (18 days), and other Anthropic models stayed available.

**r.** The 98% magnet figure should go. Eurostat Comext shows China supplied 92.4% of extra-EU imports of CN 8505.11 metal permanent magnets by weight and 88.2% by value (EUR 942.8m) in 2025. That code includes non-rare-earth magnets. The ECB's model puts the euro area's loss of final demand from a sudden halt of all critical-dependency imports from the China-led bloc at 0.41% (2023 tables), about EUR 66bn on euro-area GDP or EUR 77bn if applied to the EU. That is a full-halt counterfactual with low substitution elasticities. The IEA's "over USD 1.5 trillion" for Europe is gross sales of magnet-dependent products, an exposure measure. The observed episodes are far smaller than either. In 2025 China's global magnet exports fell about 75% year on year in May (ECB), yet EU imports from China were down only 1% that month, down 25% in July, and up 2.6% for the year. Nexperia produced warnings and line-stoppage threats but no loss we can measure in the monthly output series. Our reading is that graduated Chinese punishment has so far cost Europe little in aggregate, and that the memo's r of EUR 3bn, 15bn and 77bn spans the plausible range. The central EUR 15bn is a geometric midpoint, not an estimate, as the memo says.

The lever is reciprocal. MOFCOM tied rare-earth facilitation for Europe to a "hope" for EU facilitation of dual-use licences (15 October 2026), and the 8 to 9 October consultation produced EU commitments to push key dual-use cases and to "substantively launch" mutual delisting. On 27 October Wang Wentao told Bernd Lange that the EU's recent run of trade-restriction tools had hurt supply-chain stability. The IEA's stockpile costs (USD 3m to 180m a year to operate, for all countries outside China combined) show that r is cheap to reduce.

**kappa*S.** The memo is right that a replacement cost is an upper bound on S only if Europe would replace US protection fully. Burilkov and Wolff's EUR 250bn (Kiel Policy Brief 183, co-published by Bruegel) takes spending from about 2% to about 3.5% of GDP and leaves out nuclear deterrence and hybrid warfare. NATO's 3.5% core target for 2035 was reaffirmed in July 2026, and JANES projects euro-area spending at 2.5% of GDP in 2035 (ECB EB 6/2026), so part of that increment is spent under either alignment. IISS prices equipment at more than USD 1tn over 25 years (about EUR 35bn a year) plus USD 12.3bn a year for personnel, so a low S of about EUR 45bn is better grounded than 40. The ECFR poll bounds public beliefs: net confidence that the US "would come to defend" one's country ranges from about -64 (Spain) to about -16 (Poland) in the chart. Converting these to probabilities of 0.13 to 0.37 is a heuristic. A share of respondents who are "confident" is not a subjective probability, and public beliefs are not the US decision rule that kappa describes. Behavioural evidence of conditionality is stronger than the survey: the Pentagon ordered about 5,000 troops out of Germany on 1 May 2026 after Merz said "Americans clearly have no strategy" on Iran, and a senior official cited "recent German rhetoric" (ABC News). Lithuania received a rotation in October and Poland the PAC-3 maintenance hub. The posture review had no reported decision by 15 October. Monthly spreads show no consistent reaction to US commitment shocks, but monthly averages cannot identify one. We keep kappa at 0.02, 0.10 and 0.30 and note that conditionality on the guarantee extends to issues unrelated to China (the Germany cut followed criticism over Iran).

**t_E.** Europe's AI buffer is short. The EU hosts 5.1% of cumulative AI-chip compute (Epoch, through 2026 Q2), the scenario's own figure is "five per cent," and five US hyperscalers own about 71% of the world's AI compute (Q4 2025). The June 2026 directive bound foreign nationals inside the United States as well as abroad, so European location gave no protection, and the scenario's epilogue concedes the point when it asks for compute "Washington could not commandeer at six hours' notice." European-controlled compute is roughly 0.3% to 1.5% of the world total on our estimate from Epoch's tracked clusters (79.7k H100e in the EU, 59% public). The AI gigafactory tenders close on 3 December 2026 (large) and 4 February 2027 (medium). MOFCOM/MOST Announcement 2026 No. 48 proposes adding 23 AI technologies (large models, agents, compute clusters) to the export catalogue, excluding what is already public through open source; whether future open-sourcing counts as an export is not stated. We keep t_E at 0, 6 and 24 months.

**Recomputed break-even.** At central values with both threats credible, kappa* = (9.5 - 50 + 15)/125 = -0.20 and Q = -EUR 38bn at kappa = 0.10. With chi_ai = 0, kappa* = 0.20 and Q = +EUR 12bn. With alpha at our proposed low of EUR 4bn the Europe-favourable corner is 2.05 instead of 1.84. Across the memo's ranges the first-order variance shares of Q are 0.66 (alpha), 0.25 (r), 0.05 (kappa) and 0.02 (S); widening kappa to 0.05 to 0.50 raises the security shares to 0.11 and 0.07 and still leaves alpha dominant. These shares are mechanical consequences of the ranges and of treating alpha and kappa as independent, which the scenario's 2031 ultimatum (AI denial and loss of protection offered as one package) does not. The robust statement is narrower than the memo's. If the US AI threat is credible and alpha exceeds about EUR 12bn a year, Europe has no leverage at the central values of r and kappa*S, and the security guarantee is not what decides that.

## Verified facts table

Verdicts: V = verified as stated; C = verified after correction (corrected wording shown); U = unverifiable with the sources reached; F = false.

| # | Claim (corrected where needed) | Verdict | Source (date) | Note |
|---|---|---|---|---|
| 1 | In 2025 China supplied 92.4% of extra-EU imports of CN 8505.11 metal permanent magnets by weight (353,221 of 382,189 x100 kg) and 88.2% by value (EUR 942.8m of EUR 1,068.5m). Shares by weight: 91.6% (2022), 91.5% (2023), 92.1% (2024). | V | https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/data/DS-045409/A.EU27_2020.CN+EXT_EU27_2020.850511.1.VALUE_IN_EUROS+QUANTITY_IN_100KG/?startPeriod=2022&endPeriod=2025&format=SDMX-CSV (data updated 16 Oct 2026) | Recomputed. 8505.11 covers all metal permanent magnets, not only rare-earth magnets. Source of the "98%" not located. |
| 2 | EU imports of 8505.11 magnets from China: 3,075 t (Jan 2025), 3,183 (Feb), 3,149 (Mar), 2,650 (Apr), 2,691 (May), 2,354 (Jun), 2,269 (Jul), 2,771 (Aug), 3,518 (Sep), 3,525 (Oct), 2,944 (Nov), 3,193 (Dec 2025); 3,247 t in Aug 2026. June and July 2025 were 25% and 28% below the Jan-Mar 2025 average; year on year, May was -1.2%, June -5.2% and July -25.3%. Annual 2025 imports from China were 2.6% above 2024 by weight. | C | https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/data/DS-045409/M.EU27_2020.CN+EXT_EU27_2020.850511.1.QUANTITY_IN_100KG/?startPeriod=2024-01&format=SDMX-CSV (updated 16 Oct 2026) | Values verified; the "fell by about a quarter in June and July" framing holds only against Q1 2025, which was itself high. |
| 3 | ECB EB 6/2025, Box 1 (Banin, D'Agostino, Gunnella, Lebastard): China supplies 70% of euro-area rare-earth imports (HS 280530, 284690); in May 2025 Chinese shipments of rare-earth magnets fell about 75% year on year, forcing some carmakers to pause production; the euro area "had generally not stockpiled"; by June aggregate imports from China were below typical levels. | V | https://www.ecb.europa.eu/pub/pdf/ecbu/eb202506.en.pdf (2025) | The 75% refers to China's global magnet shipments, not to EU imports (see row 2). |
| 4 | ECB EB 5/2025, Article 1 (Attinasi, Boeckelmann, Gerinovics, Meunier): in a Baqaee-Farhi model with low substitution elasticities, a sudden halt of critical-dependency supply from the China-led eastern bloc lowers euro-area final demand by 0.41% (2023 tables; 0.04% in 1995); US 0.08% to 0.32%; China's loss from a western halt 2.1% to 1.4%. | V | https://www.ecb.europa.eu/pub/pdf/ecbu/eb202505.en.pdf (2025) | 0.41% x EU GDP = EUR 77bn; x euro-area (EA21) GDP = EUR 66bn (our calculation). Covers all critical dependencies, not magnets alone. |
| 5 | IEA: full implementation of China's October 2025 rare-earth controls would put USD 6.5tn a year of downstream production at risk outside China (USD 4.2tn for IEA countries); the US and Europe each face "over USD 1.5 trillion"; automotive "over USD 3 trillion." The exposure equals "almost 10%" of the combined GDP of countries outside China (rare earth report) or "around 7%" (GCMO 2026). Method: magnet-dependent product counts times prices across 24 product categories, i.e. exposed revenue. | C | https://iea.blob.core.windows.net/assets/88d2b060-4c5b-46cc-8727-c60576cb937d/RareearthelementsPathwaystosecureanddiversifiedsupplychains.pdf (PDF created 7 Apr 2026), pp. 8, 38; GCMO 2026 (PDF created 15 Jul 2026), p. 237 | Memo's "7-10% of IEA countries' GDP" corrected. "Europe" is not defined in the passages read. |
| 6 | Teer (CFR, 21 Sept 2026) writes that the IEA "estimates the cost of China entirely blocking 'just' rare-earth permanent magnet supply to be around $3.5 trillion per year ... in the United States and Europe combined," linking to the IEA report. | V | https://www.cfr.org/reports/dismantling-chinas-supply-chain-weapon (2026-09-21) | Title corrected (row C15 below). IEA text says "over USD 1.5 trillion" each. |
| 7 | IEA: the operating cost of a strategic stockpile covering one year of exposed imports, for all countries outside China combined, ranges from about USD 3m a year (magnet rare-earth metals) to USD 180m (rare-earth magnets) under an industry-held government-owned model; initial purchase over USD 2.5bn. | V | IEA rare earth report (Apr 2026) | Not a European figure. |
| 8 | ACEA, 16 Oct 2025: on 10 Oct automakers received notice that Nexperia could no longer guarantee chip deliveries; stocks "generally predicted to last only a few weeks"; homologating new suppliers "would take several months." | V | https://www.acea.auto/press-release/acea-calls-for-quick-resolution-to-critical-chip-supply-shortage/ (2025-10-16) | No loss figures. |
| 9 | ACEA, 29 Oct 2025: "the political dispute that has led to the prohibition of Nexperia chip exports from China remains unresolved"; members working through reserve stocks; "assembly line stoppages might only be days away." | V | https://www.acea.auto/press-release/critical-chip-shortage-worsens-by-the-day/ (2025-10-29) | Evidence that stoppages had not begun by end-October. |
| 10 | Eurostat production index, manufacture of motor vehicles (C291, SCA, 2021 = 100), EU-27: 108.6 (Jul 2025), 102.1 (Aug), 111.2 (Sep), 105.7 (Oct, -4.9%), 112.1 (Nov), 107.2 (Dec 2025); 109.5 (Mar 2026), 104.1 (Apr), 109.4 (Jun), 98.9 (Jul), 96.1 (Aug 2026). Germany: 113.5, 108.5, 116.0 (Sep to Nov 2025). Attributing the October 2025 dip to Nexperia is not supported. | C | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_inpr_m?format=JSON&lang=EN&sinceTimePeriod=2025-06&geo=EU27_2020&geo=DE&nace_r2=C291&s_adj=SCA&unit=I21 (updated 2026-10-28) | Values verified. Swings of 5-6% are routine; ACEA (row 9) says stoppages were still "days away" on 29 Oct. The Jul-Aug 2026 fall is unexplained here. |
| 11 | EU C29 net turnover EUR 1,343,191m (2024). | V | Eurostat `sbs_ovw_act` (updated 2026-09-30) | |
| 12 | EU-27 GDP EUR 18,884.6bn (2025), EUR 18,131.2bn (2024); euro area EA20 EUR 15,876.8bn and EA21 EUR 15,993.3bn (2025). | V | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp?format=JSON&lang=EN&geo=EU27_2020&geo=EA20&geo=EA21&unit=CP_MEUR&na_item=B1GQ&sinceTimePeriod=2023 (updated 2026-10-22) | Euro area has 21 members (ECB EB 6/2026). |
| 13 | MOFCOM Americas and Oceania Dept, 28 Sept 2026: the October 2025 Kuala Lumpur arrangement suspended some tariff and non-tariff measures until 10 Nov 2026; at talks on 20-23 Sept the sides agreed to extend it to 10 Jan 2027 and to seek a further extension through high-level contacts before year end. The same readout records a new US-China AI dialogue (He Lifeng and Bessent), next round before end-November. | V | https://www.mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_cd060e0649964da8ae13216c3bb1a645.html (2026-09-28) | Does not name Announcement 70 or rare earths. |
| 14 | No MOFCOM instrument formally amending the 10 Nov 2026 end of Announcement 70 (2025) was found; latest announcements read are No. 48 (16 Oct) and No. 52 (19 Oct, dual-use customs questioning procedures), neither on rare earths. | U | https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_bd9c3f79b64e4700bede88d06edac2d4.html (2026-10-19) | No. 52 content verified; absence of an amendment cannot be confirmed without search. |
| 15 | MOFCOM press conference, 15 Oct 2026. Asked (CNBC) whether rare-earth licences for the EU depend on the January US-China talks, He Yadong said China is willing to continue facilitating rare-earth export licence approvals for Europe and also hopes the EU will reciprocally facilitate key dual-use licensing cases for China, and that the export-control dialogue mechanism will continue. | C | https://www.mofcom.gov.cn/xwfbzt/2026/swbzklxxwfbh2026n10y15r/index.html (2026-10-15) | Corrected from "tied ... explicitly conditional": the text is a reciprocity expectation ("也希望"), not a stated condition. Same conference discusses an EU-China understanding on hybrid car exports. |
| 16 | MOFCOM Europe Dept readout of the second China-EU Trade and Investment Consultation Mechanism meeting (Wang Wentao and Sefcovic, Beijing, 8-9 Oct 2026): EU will keep pushing key dual-use licensing cases for China and consider facilitation measures; both sides will "support and substantively launch" mutual delisting processes; ministerial video call in January; third meeting March 2027. | V | https://www.mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_50522231086142f8a41b0163bc6483b2.html (2026-10-10) | |
| 17 | MOFCOM/MOST Announcement 2026 No. 48 (16 Oct 2026): proposes adding 40 technologies (AI, biomedicine, photovoltaics) to the Catalogue of Technologies Prohibited or Restricted from Export; 23 AI technologies cover large models, agents, compute clusters and information processing; technologies already public through open source or publication are excluded; comments 16 Oct to 15 Nov 2026; pre-export registration applies from publication. | V | https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_0a31a3c9ac404f7a9b0e917ce3412997.html (2026-10-16) | Registration covers transfers, licensing and changes of control. Whether future open-sourcing is an export is not stated. |
| 18 | Wang Wentao told EP INTA chair Bernd Lange on 27 Oct 2026 that the EU's recent intensive push of trade-restriction tools has had a negative impact on China-EU supply-chain stability. | V | https://www.mofcom.gov.cn/syxwfb/art/2026/art_c50a6d3655844ed28905540b2682f3eb.html (posted 2026-10-28) | |
| 19 | No Chinese export-control or unreliable-entity listing of a Dutch firm was found. | U | MOFCOM readout (2026-10-10) | Needs a targeted search. |
| 20 | Anthropic Economic Index, June 2026 release (Claude.ai chat and Cowork): EU-27 15.40% (Apr 2026) and 17.02% (May 2026) of global usage; EU-27 plus UK, NO, CH, IS 19.70% and 21.56%; US 20.97% and 20.16%. Published country shares sum to 82.0% and 87.5%; renormalised, EU-27 18.8-19.5% and wider Europe 24.0-24.6%. EU-27 minus NL (scenario Tier 2) 14.43% and 15.95% raw, 17.6% and 18.2% renormalised. 1P API data have no geography. | C | https://huggingface.co/datasets/Anthropic/EconomicIndex/tree/main/release_2026_06_26 (2026-06-26) | Recomputed. Added the Tier 2 comparison. The unpublished remainder is mostly unclassified geography (row 21), so renormalised shares are upper estimates. |
| 21 | Anthropic Economic Index, September 2025 release (Claude.ai Free and Pro, 4-11 Aug 2025): EU-27 13.1%, EU-27 plus UK/NO/CH/IS 17.0%, US 21.6%; "not_classified" geography 15.7%. | V | https://huggingface.co/datasets/Anthropic/EconomicIndex/tree/main/release_2025_09_15 | Recomputed; the not_classified share is new. |
| 22 | Europe 2031 (2029 chapter): "European customers currently account for nearly a quarter of US frontier inference on their own"; Tier 1 includes the Five Eyes, Japan, South Korea, Taiwan and the Netherlands; "most of Europe" is Tier 2; the 2031 epilogue says Europe hosted "only five per cent of global compute." | V | https://europe2031.ai (2026-06-11) | Authors are Juijn, van Baarsen, Dada, Negele, Stelling, Fox, Petropoulos and Bakker; Tom Chivers is credited for copywriting and editing. |
| 23 | Alphabet FY2025 10-K: EMEA revenues USD 117,152m, 29% of USD 402,836m (2024: USD 102,127m, 29%). | V | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm (filed 2026-02-05) | |
| 24 | Microsoft FY2026 10-K: revenue United States USD 170,794m, other countries USD 161,045m (48.5% of USD 331,839m); long-lived assets outside the US USD 175,159m. | V | https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm (filed 2026-07-29) | US figure includes billings to OEMs and some multinationals. |
| 25 | Amazon FY2025 10-K: net sales Germany USD 45,900m, UK USD 43,212m, of USD 716,924m; AWS not split by geography. | V | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm (filed 2026-02-06) | |
| 26 | Epoch AI: OpenAI annualised revenue USD 20bn (31 Dec 2025); Anthropic USD 14bn (12 Feb 2026). | V | https://epoch.ai/data-insights/anthropic-openai-revenue (2026-02-19) | Stale by October 2026 given the growth rates Epoch reports; the EUR 4.5-6bn spending floor is dated. |
| 27 | Filippucci, Gal, Laengle and Schief (OECD): annual aggregate labour productivity growth from AI of 0.4-1.3 points in high-exposure G7 economies (US, UK); gains in several other G7 economies "up to 50% smaller." | V | https://doi.org/10.1787/a5319ab5-en (2025-06-26) | Abstract via OpenAlex. |
| 28 | Epoch (Edwards and Emberson), "Open models lag state-of-the-art closed models by 4 months": since January 2026 the best open-weight models lagged closed frontier models by four months on average (8 ECI points, 90% CI 7-11); six months if the open model's point estimate must exceed the earlier frontier; the estimate "may tend to understate the true gap." | C | https://epoch.ai/data-insights/open-closed-eci-gap (2026-05-29) | Corrected title and added the six-month variant. "All leading open models in 2026 are Chinese" is not stated in the text. |
| 29 | Epoch ECI scores (28 Oct 2026): top US models Claude Opus 5.5 (168.83, 22 Sep 2026) and GPT-6 Astra (168.81); Kimi K3 (157.9, non-commercial) equals the US frontier of 5 Mar 2026 (7.8 months); GLM-5.3 (156.0, restricted use), DeepSeek V4.1 Flash (155.9, unrestricted) and Muse Spark Open (155.1, restricted use) equal the frontier of 11 Dec 2025 (10.5 months); Mistral Large 4 (150.0, access unknown) equals 7 Oct 2025 (12.7 months); Mistral Medium 3.5 (141.4) is 22.3 months behind. US frontier rose about 1.6 ECI points a month over the past year. | V | https://epoch.ai/data/benchmark_data.zip (eci_scores.csv, accessed 2026-10-29) | Recomputed; 10.5 vs memo's 10.6 is rounding. ECI CIs are about +/-4 points, i.e. +/-2-3 months of lag. |
| 30 | Epoch (16 Oct 2026): open-weight models trail closed models in cyber capabilities by 6-7 months; GLM-5.3 is the top open-weight model on Cyber ECI. | V | https://epoch.ai/data-insights (listing, 2026-10-16) | New; read from the listing summary only. |
| 31 | Anthropic, 12 Jun 2026: a US export-control directive suspended all access to Fable 5 and Mythos 5 by any foreign national "whether inside or outside the United States"; Anthropic disabled both models for all customers; other models unaffected. | V | https://www.anthropic.com/news/fable-mythos-access (2026-06-12) | |
| 32 | Anthropic, 30 Jun 2026 (updated 1 Jul): controls lifted 30 Jun; Fable 5 available globally from 1 Jul; access via AWS, Google Cloud and Microsoft Foundry to be re-enabled; Mythos 5 restored for a set of US organisations after US approval on 26 Jun; the 1 Jul update says both models were redeployed. Requests blocked by the new classifier are sent to Opus 4.8. No cost figures. | C | https://www.anthropic.com/news/redeploying-fable-5 (2026-06-30, updated 2026-07-01) | Opus 4.8 routing concerns post-redeployment classifier blocks, not the suspension. Cloud channels were off because Anthropic disabled the models everywhere. |
| 33 | ECB EB 2/2026, Box 6 (Ferrando, Lamboglia, Rariga, Schmidt): 38% of euro-area firms at an advanced stage of AI adoption and 33% at an early stage (SAFE, Q4 2025). | V | https://www.ecb.europa.eu/pub/pdf/ecbu/eb202602.en.pdf (2026) | |
| 34 | Kiel Policy Brief 183 (Burilkov and Wolff, Feb 2025), joint with Bruegel (Analysis 05/2025, 21 Feb 2025): spending must rise from about 2% of GDP; about EUR 250bn a year more (around 3.5% of GDP) in the short term; 300,000 additional troops; nuclear deterrence and hybrid warfare not discussed; replacing US military aid to Ukraine 0.12% of EU GDP; debt-funded increase should boost activity. | V | https://www.kielinstitut.de/fileadmin/Dateiverwaltung/IfW-Publications/fis-import/1e4328c0-81e2-470f-b665-f109137e6570-KPB_183_en.pdf ; https://www.bruegel.org/analysis/defending-europe-without-us-first-estimates-what-needed | Joint publication confirmed on the Bruegel page. |
| 35 | IISS (15 May 2025, via Stars and Stripes): USD 226-344bn to replace US conventional systems; more than USD 1tn over a 25-year life cycle (about EUR 35bn a year at 1.13, our calculation); USD 12.3bn a year to replace US personnel; about a decade to match US ground forces; scenario assumes the US keeps providing NATO's nuclear deterrent. | C | https://www.stripes.com/theaters/europe/2025-05-16/europe-trump-nato-defense-17807650.html (2025-05-16) | Added personnel cost and nuclear assumption. IISS report not read directly. |
| 36 | ECB EB 6/2026, Article 2 (Checherita-Westphal, Rodriguez-Vives, Lalinsky, Parker): NATO members committed in June 2025 to 5% of GDP by 2035 (3.5% core), reaffirmed at the July 2026 summit; JANES projects euro-area defence spending up almost 1 point to 2.5% of GDP in 2035; euro-area COFOG spending almost 1.5% of GDP in 2025; on NATO definitions about 2.2% for euro-area NATO members and 2.0% for all euro-area countries; cumulative GDP multiplier around unity at peak (Box 2). | C | https://www.ecb.europa.eu/pub/pdf/ecbu/eb202606.en.pdf (2026) | Corrected the 2.2% scope. |
| 37 | ECFR "Home alone" (Kobzova and Zerka, ECFR/640, June 2026; fieldwork 30 Apr to 19 May 2026, 15 countries, 19,481 respondents): majorities in every country think the US would not support them if attacked; net confidence that "the United States would come to defend it" runs from about -64 (Spain) to about -16 (Poland) in the chart; 11% overall see the US as an ally; about 24% in Poland and 8% in Germany (trend chart). | V | https://ecfr.eu/wp-content/uploads/2026/06/Home-alone-Europeans-are-ready-to-defend-themselves-v3.pdf (PDF modified 2026-06-22) | Chart values read from the image (axis calibrated). Net confidence is not a probability. |
| 38 | Eurostat convergence yields, spreads over Germany (bp): Feb vs Jan 2024 EE 116/113, LV 108/120, LT 55/70, PL 303/306, FI 55/62; Jan 2026 vs Dec 2025 EE 45/57, LV 85/85, LT 7/7, PL 229/240, FI 45/35; May vs Apr 2026 PL 270/258, LV 73/79; Sep vs Aug 2026 PL 276/262, LT -59/-31. No consistent widening; Poland +12 and +14 bp in May and Sep 2026 and Finland +10 bp in Jan 2026. | C | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/irt_lt_mcby_m?format=JSON&lang=EN&sinceTimePeriod=2023-12&geo=DE&geo=PL&geo=LT&geo=LV&geo=FI&geo=EE | Values verified; wording corrected. Monthly averages cannot identify the effect either way. |
| 39 | Covachev and Fazakas (2026): CAARs of 5-6% for European defence-ETF constituents over the four trading days after the November 2024 election result and 16-18% after the February 2025 Trump-Zelenskyy meeting. | V | https://doi.org/10.1080/10242694.2026.2658649 (online 2026-04-30) | Abstract via OpenAlex. |
| 40 | ABC News, 2 May 2026: Hegseth ordered about 5,000 troops out of Germany over 6-12 months after Trump threatened withdrawals following Merz's remarks on the Iran war; a senior Pentagon official cited "recent German rhetoric"; the move returns US troop levels to roughly pre-2022 levels. | V | https://www.goodmorningamerica.com/amp/news/story/us-withdraw-5000-troops-germany-132587562 (2026-05-02) | Source for the memo's "troops left Germany after Merz's criticism." The criticism concerned Iran, not China. |
| 41 | Stars and Stripes, 15 Oct 2026: up to 100 US personnel in Pabrade, two battalions by mid-November; the Pentagon is conducting a broader posture review; cuts may be considered while expanding the presence in Poland is discussed; the 1 May withdrawal of 5,000 troops from Germany returned brigade levels to pre-2022, and most of those forces were connected to the brigade headed to Poland. | V | https://www.stripes.com/branches/army/2026-10-15/lithuania-us-troop-deployment-23160843.html (2026-10-15) | By John Vandiver. No decision timeline reported. |
| 42 | Pentagon announced on 27 Oct 2026 that Poland will host Europe's first PAC-3 maintenance facility (about USD 253m, operational in about a year, per Reuters), chosen over Germany, the Netherlands and Norway. | V | https://www.stripes.com/theaters/europe/2026-10-28/poland-patriot-missile-maintenance-hub-23286863.html (2026-10-28) | |
| 43 | EuroHPC call EUROHPC-2026-CEI-AIGF-01: published and opened 30 Jul 2026, status open; Lot 2 (large) deadline 3 Dec 2026; Lot 1 (medium) extended to 4 Feb 2027 for national budget commitments; each AIGF needs at least three to four times the advanced AI processors of the most powerful current European AI factories. | V | https://www.eurohpc-ju.europa.eu/call-tenders-selection-artificial-intelligence-gigafactory-consortia-and-establishment-ai_en (accessed 2026-10-29) | |
| 44 | Council Regulation (EU) 2026/150 of 16 Jan 2026 (OJ L 2026/150, 19.1.2026): EU contribution up to 17% of AI-gigafactory computing capex (or equivalent guaranteed access-time purchase), at least matched by participating states; participation of entities from non-participating states may be restricted or excluded; access agreements with third-country entities "that might raise concerns" need prior approval of the public governance body; no operational dates. | V | http://data.europa.eu/eli/reg/2026/150/oj | Qualifier on prior approval added. |
| 45 | Epoch chip imports: cumulative AI-chip compute arrivals 2022 Q1 to 2026 Q2 total 27.39M H100e; EU 1.388M (5.1%; range 1.03-2.57M); US 19.76M (72.2%); China 2.64M (9.6%). By location, not ownership. | V | https://epoch.ai/data/ai_chip_trade/ai_chip_trade_by_country.csv (accessed 2026-10-29) | Recomputed from the "European Union" row. |
| 46 | Epoch (Emberson, You, Somala), "Five hyperscalers now own over two-thirds of global AI compute": Amazon, Google, Meta, Microsoft and Oracle hold an estimated 71% of cumulative AI compute as of Q4 2025, up from 62.5% in Q1 2024. | V | https://epoch.ai/data-insights/hyperscalers-control-most-compute (2026-04-14) | |
| 47 | Epoch GPU clusters (existing, standard analysis): EU-located tracked clusters 79.7k H100e (5.1% of tracked); 58.8% public, 41.1% private. Ownership-adjusted European-controlled compute of 0.3-1.5% of world cumulative compute is our estimate. | V (data) / U (estimate) | https://epoch.ai/data/gpu_clusters.csv | The upper bound applies the global non-hyperscaler share (29%) to EU imports, which overstates European control. |
| 48 | ECB reference rate: USD per EUR 1.1300 (2025 average), 1.1513 (September 2026). | V | https://data-api.ecb.europa.eu/service/data/EXR/A.USD.EUR.SP00.A?format=csvdata&startPeriod=2024 | |
| 49 | ASML FY2025: total net sales to China EUR 9,519.7m, 29.1% of EUR 32,667.3m (omega). | V | https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/asml-20251231.htm (filed 2026-02-25) | 2026 guidance (about 20% of EUR 36-40bn) not re-verified here. |
| 50 | ECB EB 6/2026: euro-area energy producer price inflation rose to 12.9% in July 2026 from 8.8% in June. | V | https://www.ecb.europa.eu/pub/pdf/ecbu/eb202606.en.pdf | New; a plausible confounder for the Jul-Aug 2026 fall in vehicle output (row 10). |

## Citation verdicts

| Key | Verdict | Note |
|---|---|---|
| digiuseppe2018arms | V | BJPolS 48(4): 981-1003, online 8 Nov 2016. Abstract: democratic alliances associated with lower military spending (defense pacts and military expenditures, 1950-2001). Not a bond-market study. |
| ferry2025crises | V | JCR 69(10): 1713-1740, online 25 Mar 2025. Commercial defaults 1970-2012; US support raises restructuring, lowers post-restructuring borrowing costs and shortens exclusion. |
| albalate2024paying | V | JEBO 223: 234-247. 138 countries, 1996-2020; more trade with, and a larger surplus for, the alliance leader means lower minor-partner defence spending. |
| covachev2026effects | V | Defence and Peace Economics, online 30 Apr 2026, pp. 1-21. |
| filippucci2025g7 | V | OECD AI Papers, 26 Jun 2025 (Crossref "published" 30 Jun). Paper number not verified. |
| filippucci2024miracle | V | OECD AI Papers, 22 Nov 2024; 0.25-0.6 pp TFP, 0.4-0.9 pp labour productivity. |
| filippucci2026aggregate | C | AEA P&P 116: 31-35. Claim corrected to "up to 0.9 pp of annual US TFP growth"; Baumol effect "quantitatively small" when substitution elasticities are large or factors reallocate. |
| acemoglu2024simple | C | Year is 2025 (Economic Policy 40(121): 13-58; online 6 Aug 2024). TFP gain no more than 0.66% over ten years, below 0.53% after the hard-task adjustment. Implies g far below the memo's low value. |
| attinasi2025hidden | V | ECB EB 5/2025, Article 1, p. 77 ff. |
| banin2025rare | V | ECB EB 6/2025, Box 1, p. 39 ff. |
| checherita2026defence | C | ECB EB 6/2026, Article 2. 2.2% scope corrected; multiplier finding is in Box 2 by different authors. |
| ferrando2026adopting | V | ECB EB 2/2026, Box 6. |
| iea2026ree | C | Exists and supports the figures; "7-10% of IEA countries' GDP" corrected. Publication month inferred from PDF metadata (April 2026). |
| iea2026gcmo | V | Gives "around 7%" of GDP of countries outside China, pp. 237-238. |
| teer2026dismantling | C | Title is "Dismantling China's Supply-Chain Weapon: A Transatlantic Strategy for Critical Minerals"; published 21 Sep 2026. |
| burilkov2025defending | V | Kiel Policy Brief 183, Feb 2025; joint publication with Bruegel (Analysis 05/2025). |
| kobzova2026home | V | ECFR/640, June 2026. Chart values verified by reading the image. |
| massenkoff2026cadences | V | Report page fetched; title, date and contributors match. |
| edwards2026openclosed | C | Title corrected to "Open models lag state-of-the-art closed models by 4 months." |
| epoch2026eci | V | Dataset re-downloaded; ECI file identical. |
| council2026reg150 | V | Text verified at the cited provisions. |

## Modeling implications

1. **Keep the sign correction and drop r_A = 0.** Under the model's exit-cost definition (`model_design_v2.md`, Section 1), a credible Chinese punishment of alignment adds to Q, so kappa* = (omega - chi_ai*alpha - chi_f*f - eta + chi_r*r)/S. The Remark that sets r_A = 0 for lack of an instance should be revised: the Nexperia export ban followed the Dutch Wbg order, and MOFCOM's 9 November 2025 easing came with a demand that the EU press The Hague (china_dep.md). Model r as graduated and reciprocal, a function of Europe's export-control behaviour (Section 6 hedging extension), rather than as a single cutoff.

2. **Report the decisive threshold rather than variance shares.** At central r and kappa*S, Q < 0 iff alpha > EUR 12bn a year (0.06% of EU GDP). This is the cleanest statement of the result and does not depend on distributional assumptions. The variance decomposition (alpha 0.66, r 0.25, kappa 0.05, S 0.02) follows mechanically from the chosen ranges and from independence. If kappa runs from 0.05 to 0.50, the security shares rise to 0.11 and 0.07 and P(Q > 0) falls to 0.15.

3. **Widen alpha downward and make its high end conditional.** Use EUR 4bn, 50bn and 130bn. The low value follows from Acemoglu (2025) with Delta = 4 months; the high value assumes growth is limited by frontier capability, which the OECD's adoption-driven framework does not assume. With the lower floor, P(Q > 0 | chi_ai = 1) is 0.37 rather than 0.21. Define alpha as the conditional part d_ai, the loss from moving from aligned access to exited access. In the scenario aligned Europe is already Tier 2, so d_ai is smaller than full denial.

4. **Delta.** Use 6 months as the central lower anchor (Epoch's point-estimate version) and 10.5 months for the best commercially usable open weights. Epoch's cyber-specific lag (6-7 months, 16 October 2026) suggests the lag is similar across capability domains.

5. **Treat alpha and kappa as linked.** The scenario's 2031 ultimatum bundles Tier 3 status with the protectorate offer, and the May 2026 Germany cut shows that US security provision responds to political behaviour on unrelated issues. A positive correlation between the AI threat and the security threat is the natural assumption; the Monte Carlo should allow it.

6. **S.** Use EUR 45bn, 125bn and 250bn (the low value adds IISS's USD 12.3bn a year for personnel). Keep the decomposition S = min{R_inc, p_c*D} + rho*p_c*D_w and say that nuclear cover is outside both the Kiel and IISS numbers.

7. **kappa.** The ECFR conversion is a heuristic ceiling on public beliefs, not an estimate of kappa. The better evidence is behavioural and differentiated by member state (Germany cut; Lithuania rotation; Poland Patriot hub). Heterogeneous kappa_i predicts the scenario's ACI blocking coalition (Poland, the Baltics) without different preferences over China, which links to the nested-chokepoint section.

8. **r is cheap to reduce, and that matters for welfare, not leverage.** Stockpiles (USD 3m to 180m a year for all non-China countries) lower r. Lowering r lowers Q but never lowers Europe's payoff ([Q]^+ - chi_r*r is weakly decreasing in r). The paper should state that measured leverage and welfare move in opposite directions here.

9. **t_E near zero for US-owned capacity.** The June 2026 directive bound persons, inside and outside the US, so European siting of US-owned compute bought no time. Whether EU or member-state emergency law (the Dutch Wbg used on Nexperia) could keep such capacity running against a US directive decides whether t_E is near zero or nearer two years.

10. **Redraw Figure `fig:breakeven`** in (alpha, r) space with iso-kappa* lines for S = 45, 125 and 250, mark the alpha = EUR 12bn threshold at central r and kappa*S, and show the chi_ai = 0 case. Fix the corner in `breakeven.py` (alpha = 13 or the new low of 4) before regenerating.

## Open questions

- Has MOFCOM amended Announcement 70 or the gallium, germanium and antimony suspension after 19 October, or will it rely on the Kuala Lumpur extension to 10 January 2027?
- What caused the 9.6% fall in EU motor-vehicle output in July 2026? The energy shock (ECB EB 6/2026) is the obvious candidate; a Chinese input measure would matter for r.
- Realised losses from the 2025 magnet squeeze and from Nexperia: no ACEA, VDA, CLEPA or company figure was found.
- Geography of enterprise and API revenue for US labs, and current run-rates (Epoch's figures end in February 2026).
- The IISS report itself, to confirm whether the USD 1tn life-cycle figure includes personnel.
- Country-level ECFR tables for the Netherlands and Germany on US defence confidence.
- A daily CDS and spread event study around the 2024 to 2026 commitment shocks (needs Bloomberg or LSEG data).

## BibTeX (verified or corrected entries)

```bibtex
@article{digiuseppe2018arms,
  author  = {DiGiuseppe, Matthew and Poast, Paul},
  title   = {Arms versus Democratic Allies},
  journal = {British Journal of Political Science},
  year    = {2018},
  volume  = {48},
  number  = {4},
  pages   = {981--1003},
  doi     = {10.1017/S0007123416000247}
}

@article{ferry2025crises,
  author  = {Ferry, Lauren L. and Shea, Patrick E.},
  title   = {Crises and Consequences: The Role of {U.S.} Support in International Bond Markets},
  journal = {Journal of Conflict Resolution},
  year    = {2025},
  volume  = {69},
  number  = {10},
  pages   = {1713--1740},
  doi     = {10.1177/00220027251327970}
}

@article{albalate2024paying,
  author  = {Albalate, Daniel and Bel, Germ{\`a} and Mazaira-Font, Ferran A. and Ros-Oton, Xavier},
  title   = {Paying for protection: bilateral trade with an alliance leader and defense spending of minor partners},
  journal = {Journal of Economic Behavior \& Organization},
  year    = {2024},
  volume  = {223},
  pages   = {234--247},
  doi     = {10.1016/j.jebo.2024.05.012}
}

@article{covachev2026effects,
  author  = {Covachev, Svetoslav and Fazakas, Gergely},
  title   = {The effects of the 2024 {U.S.} presidential election and the 2025 {Trump--Zelenskyy} meeting on {European} defence stocks: an event study analysis},
  journal = {Defence and Peace Economics},
  year    = {2026},
  pages   = {1--21},
  note    = {Published online 30 April 2026},
  doi     = {10.1080/10242694.2026.2658649}
}

@techreport{filippucci2025g7,
  author      = {Filippucci, Francesco and Gal, Peter and Laengle, Katharina and Schief, Matthias},
  title       = {Macroeconomic productivity gains from Artificial Intelligence in {G7} economies},
  institution = {OECD Publishing},
  type        = {OECD Artificial Intelligence Papers},
  address     = {Paris},
  year        = {2025},
  doi         = {10.1787/a5319ab5-en}
}

@techreport{filippucci2024miracle,
  author      = {Filippucci, Francesco and Gal, Peter and Schief, Matthias},
  title       = {Miracle or Myth? Assessing the macroeconomic productivity gains from Artificial Intelligence},
  institution = {OECD Publishing},
  type        = {OECD Artificial Intelligence Papers},
  address     = {Paris},
  year        = {2024},
  doi         = {10.1787/b524a072-en}
}

@article{filippucci2026aggregate,
  author  = {Filippucci, Francesco and Gal, Peter and Schief, Matthias},
  title   = {Aggregate Productivity Gains from Artificial Intelligence: A Sectoral Perspective},
  journal = {AEA Papers and Proceedings},
  year    = {2026},
  volume  = {116},
  pages   = {31--35},
  doi     = {10.1257/pandp.20261035}
}

@article{acemoglu2024simple,
  author  = {Acemoglu, Daron},
  title   = {The simple macroeconomics of {AI}},
  journal = {Economic Policy},
  year    = {2025},
  volume  = {40},
  number  = {121},
  pages   = {13--58},
  note    = {Published online 6 August 2024},
  doi     = {10.1093/epolic/eiae042}
}

@article{attinasi2025hidden,
  author  = {Attinasi, Maria-Grazia and Boeckelmann, Lukas and Gerinovics, Rinalds and Meunier, Baptiste},
  title   = {Unveiling the hidden costs of critical dependencies},
  journal = {ECB Economic Bulletin},
  number  = {5/2025},
  year    = {2025},
  note    = {Article 1},
  url     = {https://www.ecb.europa.eu/pub/pdf/ecbu/eb202505.en.pdf}
}

@article{banin2025rare,
  author  = {Banin, Mattia and D'Agostino, Mario and Gunnella, Vanessa and Lebastard, Laura},
  title   = {How vulnerable is the euro area to restrictions on {Chinese} rare earth exports?},
  journal = {ECB Economic Bulletin},
  number  = {6/2025},
  year    = {2025},
  note    = {Box 1},
  url     = {https://www.ecb.europa.eu/pub/pdf/ecbu/eb202506.en.pdf}
}

@article{checherita2026defence,
  author  = {Checherita-Westphal, Cristina and Rodr{\'\i}guez-Vives, Marta and Lalinsk{\'y}, Tibor and Parker, Miles},
  title   = {Defence spending and its short and longer-term macroeconomic effects},
  journal = {ECB Economic Bulletin},
  number  = {6/2026},
  year    = {2026},
  note    = {Article 2},
  url     = {https://www.ecb.europa.eu/pub/pdf/ecbu/eb202606.en.pdf}
}

@article{ferrando2026adopting,
  author  = {Ferrando, Annalisa and Lamboglia, Sara and Rariga, Judit and Schmidt, Maurice},
  title   = {Adopting and investing in {AI}: evidence from euro area firms in the {SAFE}},
  journal = {ECB Economic Bulletin},
  number  = {2/2026},
  year    = {2026},
  note    = {Box 6},
  url     = {https://www.ecb.europa.eu/pub/pdf/ecbu/eb202602.en.pdf}
}

@techreport{iea2026ree,
  author      = {{International Energy Agency}},
  title       = {Rare earth elements: Pathways to secure and diversified supply chains},
  institution = {IEA},
  address     = {Paris},
  year        = {2026},
  note        = {Licence CC BY 4.0; PDF dated April 2026},
  url         = {https://iea.blob.core.windows.net/assets/88d2b060-4c5b-46cc-8727-c60576cb937d/RareearthelementsPathwaystosecureanddiversifiedsupplychains.pdf}
}

@techreport{iea2026gcmo,
  author      = {{International Energy Agency}},
  title       = {Global Critical Minerals Outlook 2026},
  institution = {IEA},
  address     = {Paris},
  year        = {2026},
  url         = {https://www.iea.org/reports/global-critical-minerals-outlook-2026}
}

@techreport{teer2026dismantling,
  author      = {Teer, Joris},
  title       = {Dismantling {China's} Supply-Chain Weapon: A Transatlantic Strategy for Critical Minerals},
  institution = {Council on Foreign Relations},
  type        = {Council Report},
  year        = {2026},
  month       = sep,
  url         = {https://www.cfr.org/reports/dismantling-chinas-supply-chain-weapon}
}

@techreport{burilkov2025defending,
  author      = {Burilkov, Alexandr and Wolff, Guntram B.},
  title       = {Defending {Europe} Without the {US}: First Estimates of What is Needed},
  institution = {Kiel Institute for the World Economy},
  type        = {Kiel Policy Brief},
  number      = {183},
  year        = {2025},
  month       = feb,
  note        = {Joint publication with Bruegel (Bruegel Analysis 05/2025, 21 February 2025)},
  url         = {https://www.kielinstitut.de/fileadmin/Dateiverwaltung/IfW-Publications/fis-import/1e4328c0-81e2-470f-b665-f109137e6570-KPB_183_en.pdf}
}

@techreport{kobzova2026home,
  author      = {Kobzov{\'a}, Jana and Zerka, Pawe{\l}},
  title       = {Home alone: {Europeans} are ready to defend themselves},
  institution = {European Council on Foreign Relations},
  type        = {Policy Brief},
  number      = {ECFR/640},
  year        = {2026},
  month       = jun,
  url         = {https://ecfr.eu/wp-content/uploads/2026/06/Home-alone-Europeans-are-ready-to-defend-themselves-v3.pdf}
}

@online{massenkoff2026cadences,
  author  = {Massenkoff, Maxim and Lyubich, Eva and Sacher, Szymon and Hitzig, Zoe and Zhang, Shaoyi and Heller, Ryan and McCrory, Peter},
  title   = {Anthropic Economic Index report: Cadences},
  year    = {2026},
  date    = {2026-06-26},
  organization = {Anthropic},
  url     = {https://www.anthropic.com/research/economic-index-june-2026-report}
}

@online{edwards2026openclosed,
  author  = {Edwards, Jack and Emberson, Luke},
  title   = {Open models lag state-of-the-art closed models by 4 months},
  year    = {2026},
  date    = {2026-05-29},
  organization = {Epoch AI},
  note    = {Data Insight},
  url     = {https://epoch.ai/data-insights/open-closed-eci-gap}
}

@online{emberson2026hyperscalers,
  author  = {Emberson, Luke and You, Josh and Somala, Venkat},
  title   = {Five hyperscalers now own over two-thirds of global {AI} compute},
  year    = {2026},
  date    = {2026-04-14},
  organization = {Epoch AI},
  note    = {Data Insight},
  url     = {https://epoch.ai/data-insights/hyperscalers-control-most-compute}
}

@online{emberson2026revenue,
  author  = {Emberson, Luke and Edelman, Yafah},
  title   = {Anthropic could surpass {OpenAI} in annualized revenue by mid-2026},
  year    = {2026},
  date    = {2026-02-19},
  organization = {Epoch AI},
  note    = {Data Insight},
  url     = {https://epoch.ai/data-insights/anthropic-openai-revenue}
}

@misc{epoch2026eci,
  author  = {{Epoch AI}},
  title   = {Epoch Capabilities Index scores ({Benchmarking Hub} data)},
  year    = {2026},
  howpublished = {Dataset, eci\_scores.csv in benchmark\_data.zip},
  note    = {Accessed 29 October 2026},
  url     = {https://epoch.ai/data/benchmark_data.zip}
}

@misc{epoch2026chiptrade,
  author  = {{Epoch AI}},
  title   = {Data on {AI} chip imports by country},
  year    = {2026},
  howpublished = {Dataset, ai\_chip\_trade\_by\_country.csv},
  note    = {Through 2026 Q2; accessed 29 October 2026},
  url     = {https://epoch.ai/data/ai_chip_trade/ai_chip_trade_by_country.csv}
}

@misc{council2026reg150,
  author  = {{Council of the European Union}},
  title   = {Council Regulation ({EU}) 2026/150 of 16 January 2026 amending Regulation ({EU}) 2021/1173 on establishing the {European} High Performance Computing Joint Undertaking},
  howpublished = {Official Journal of the European Union, L series 2026/150, 19 January 2026},
  year    = {2026},
  url     = {http://data.europa.eu/eli/reg/2026/150/oj}
}

@online{anthropic2026directive,
  author  = {{Anthropic}},
  title   = {Statement on the {US} government directive to suspend access to {Fable 5} and {Mythos 5}},
  year    = {2026},
  date    = {2026-06-12},
  url     = {https://www.anthropic.com/news/fable-mythos-access}
}

@online{anthropic2026redeploy,
  author  = {{Anthropic}},
  title   = {Redeploying {Fable 5}},
  year    = {2026},
  date    = {2026-06-30},
  note    = {Updated 1 July 2026},
  url     = {https://www.anthropic.com/news/redeploying-fable-5}
}

@online{martinez2026germany,
  author  = {Martinez, Luis},
  title   = {{US} to withdraw 5,000 troops from {Germany}, {Pentagon} announces},
  year    = {2026},
  date    = {2026-05-02},
  organization = {ABC News},
  url     = {https://www.goodmorningamerica.com/amp/news/story/us-withdraw-5000-troops-germany-132587562}
}

@online{vandiver2026lithuania,
  author  = {Vandiver, John},
  title   = {{US} troop rotation arrives in {Lithuania} as {Pentagon} reviews {Europe} posture},
  year    = {2026},
  date    = {2026-10-15},
  organization = {Stars and Stripes},
  url     = {https://www.stripes.com/branches/army/2026-10-15/lithuania-us-troop-deployment-23160843.html}
}

@online{mofcom2026pc1015,
  author  = {{Ministry of Commerce of the People's Republic of China}},
  title   = {Shangwubu zhaokai lixing xinwen fabuhui (2026 nian 10 yue 15 ri) [{MOFCOM} regular press conference, 15 October 2026]},
  year    = {2026},
  date    = {2026-10-15},
  language = {Chinese},
  url     = {https://www.mofcom.gov.cn/xwfbzt/2026/swbzklxxwfbh2026n10y15r/index.html}
}

@online{mofcom2026ann48,
  author  = {{Ministry of Commerce} and {Ministry of Science and Technology}},
  title   = {Shangwubu Kejibu gonggao 2026 nian di 48 hao [{MOFCOM} and {MOST} Announcement No. 48 of 2026 on revising the Catalogue of Technologies Prohibited or Restricted from Export]},
  year    = {2026},
  date    = {2026-10-16},
  language = {Chinese},
  url     = {https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_0a31a3c9ac404f7a9b0e917ce3412997.html}
}
```
