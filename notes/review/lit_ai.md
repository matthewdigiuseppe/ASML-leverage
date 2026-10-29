# Review: the AI race, compute governance and semiconductor geopolitics (strand: lit_ai)

Fact-check completed 28 October 2026. The shared WebSearch budget for this turn was used up before this check began, so no keyword searches were run. Every item was checked another way:
- **Journal works:** Crossref and OpenAlex by DOI, with authors, title, venue, volume, issue, pages and abstract compared field by field.
- **arXiv preprints:** the arXiv API.
- **Horowitz (2018):** DataCite and the TNSR article page.
- **Books:** Open Library and Crossref.
- **Everything else:** the primary pages fetched directly. These include europe2031.ai, the two Anthropic statements, the GovAI report PDF, the White House orders and the AI Action Plan PDF, the Federal Register text of 90 FR 4544, the BIS press release, si.gov, gov.cn, the CSIS, CSET, CNAS, MERICS, Rhodium, BCG, ECFR, Bruegel, NY Fed, Huawei, TSMC, Nvidia, SK hynix, ASML, TechInsights and SemiAnalysis pages, and the Epoch AI CSV files.

Reuters cannot be fetched from here, so the Reuters EUV-prototype report was confirmed through its syndicated text in The Jakarta Post, which carries the Reuters credit line. All Epoch shares were recomputed from the CSV files, and all the memo's figures reproduce.

**Outcome.** All 42 cited works exist. None is unverifiable. All 48 facts were confirmed, and 8 of them needed correction.
- **Citations corrected (5):**
  - Ding (2024, book): the hardcover ISBN is 9780691260334, and the JSTOR DOI 10.2307/jj.12228596 has been added.
  - Bown (2020, PIIE): the abstract says export controls can "redistribute economic well-being across countries, even from one ally to another". It does not say they "strain multilateral regimes". It discusses COCOM, Wassenaar and new challenges for WTO dispute settlement.
  - Allen and Goldston (2025): Russia's membership makes Wassenaar consensus "unfeasible" on sensitive items. The report does not say Russia blocked a specific proposal.
  - Pilz, Heim and Brown: first posted November 2023 (v2 February 2024). The key is kept.
  - Allen (2025, DeepSeek): the report says China "likely remains stuck at the 7 nm technology node until and unless they develop a domestic EUV lithography capability". The word "flawed" for 5 nm is ours.
- **Synthesis uses corrected (no citation verdict changed):**
  - Lehdonvirta, Wu and Hawkins (2024) map where public-cloud GPU compute is located. They do not propose a coalition of chokepoint holders.
  - Trager et al. (2023) is an international-governance proposal, not middle-power literature.
  - Armstrong et al., Stafford et al. and Emery-Xu et al. model trade-offs between safety and performance. "Marginal capability is worth more in decisive races" is our extension, not their result.
  - Crosignani et al. measure costs to US suppliers that lost Chinese customers. Applying this to a US cutoff of European AI access is our analogy.
  - Gilli and Gilli (2019) say nothing about EUV. Reading them against the Shenzhen timeline is our inference.
- **Facts corrected (8):**
  - Reuters EUV prototype: no working chips yet. The government target is 2028; insiders say 2030.
  - AI Diffusion rule: the 19 listed destinations include the United States itself. The 790 million TPP cap is a per-country allocation.
  - BIS rescission release: the wording on Huawei Ascend chips is corrected.
  - EO 14409: the order says nothing in Section 3 authorizes mandatory licensing, rather than "barring" it.
  - CSIS, TSMC dies for Huawei: "through shell companies" is not in the CSIS text checked.
  - Allen (2024a): the pre-control stockpiling is his "most likely explanation", not an established finding.
  - MERICS, September 2026 summit: it was the second Trump-Xi summit of 2026. The two also met at Busan in 2025.
  - Synthesis: "every frontier accelerator rests on EUV" is false, because Huawei's Ascend line is made at 7 nm without EUV.
- **Duration of the June 2026 cutoff:** the export controls lasted 18 days (12 to 30 June). Fable 5 came back worldwide on 1 July. Mythos 5 came back only for a set of US organizations, and international partners were still pending as of 30 June. The memo's line that "the cutoff lasted 18 days" holds only for the controls and for Fable 5.

**Keys that duplicate other strands (same work, different key):**
- juijn2026europe = juijn2026europe2031 (e2031)
- miller2022chip = miller2022chipwar
- khan2021semiconductor = khan2021cset
- allen2022choking = allen2022csis
- bown2020marched also appears as bown2020semiconductor

None of these collides with a different work. Keys should be unified when the master .bib is built. Note that khan2021cset in another strand lists the authors as Khan, Mann, Peterson. The cover order is Khan, Peterson, Mann.

## Synthesis (edited)

Literature IV supplies the payoffs our bargaining model takes as primitives:
- **V:** how much the United States loses if Europe defects.
- **W:** how much China gains.
- **theta:** how much of China's gain Washington can block through its own jurisdiction.
- **alpha:** how much Washington can hurt Europe by cutting off frontier AI access.

Taken together, the work points Europe to a sharper and less flattering conclusion than the chokepoint framing suggests. ASML is indispensable to producing frontier compute. But indispensability in production is not leverage in bargaining, because between 2026 and 2031 most components of Europe's exit premium are moving against it.

**Production.** The descriptive literature agrees that lithography is the deepest chokepoint in the chain. Khan, Peterson and Mann (2021) call lithography tools "China's most critical chokepoint". Their endnotes record that ASML "controls over 85 percent of the market for scanners and steppers". They report that ASML exclusively produces EUV scanners, which are "necessary for mass-producing 5 nm node chips". Thadani and Allen (2023) describe ASML as "the sole provider of the latest generation of photolithography scanner equipment", and Miller (2022) tells the same story historically.

The leading US accelerators rest on EUV:
- Nvidia's Blackwell is built on a custom TSMC 4NP process.
- ASML states that chipmakers use its EUV systems for the foundation layers of their 7, 5 and 3 nm nodes.
- TSMC's N2 entered volume production in the fourth quarter of 2025.
- SK hynix moved DRAM onto EUV in 2021.

The exception is Huawei's Ascend line. Its 7 nm logic comes from SMIC, which makes 7 nm chips without EUV, or from dies TSMC made before the controls bit. Of the AI-chip compute that arrived between 2022 and mid-2026, the United States hosts about 72 percent and the EU-27 about 5 percent. That is our calculation from Epoch AI's import data; these are shares by location, not by ownership. The US build-out therefore runs on ASML output, and V is large.

**Supply interruption.** The model should not let Europe count on that. Taiwan and South Korea took 38 to 67 percent of ASML's net sales in 2022 to 2025 (figures verified in the asml_facts strand), so most of the installed EUV base sits outside Europe. Allen (2024b) documents that the December 2024 rules extended US foreign direct product rules to the sales of Dutch, Japanese and other equipment firms from outside their home countries. Exports from home markets that apply equivalent controls are exempt. In Allen's reading, "U.S. export controls will follow ASML ... wherever they go". The 2025 AI Action Plan says that if partners and allies backfill, "America should use tools such as the Foreign Direct Product Rule and secondary tariffs to achieve greater international alignment". It also calls for new controls on semiconductor manufacturing subsystems.

The literature therefore supports our lemma that interrupting supply to the United States is not a credible threat. It also supports treating theta as high for any flow that passes through non-Dutch jurisdiction or carries US-origin content. Servicing of the installed base is the only hold-up channel with real force. Allen and Goldston (2025) show why it is contested: allied services controls apply only to WMD end-uses, so Dutch and Japanese firms could keep providing services that US firms could not.

**China.** This is where the literature is most useful and most often misread. Two findings cut W down.

First, lithography is not the only constraint binding China's advanced-node expansion. Allen (2025) reports that SMIC holds ASML immersion tools that could support about 85,000 FinFET wafers a month, bought before the Dutch controls took effect in mid-2023. Its 7 nm expansion is limited by "U.S. tools for etching, deposition, inspection, and metrology", not by lithography. A European defection on DUVi alone would therefore buy China less than a simple chokepoint count implies, because US jurisdiction covers the complementary tools.

Second, China is working around the node gap. At Huawei Connect 2025, Eric Xu said that "the Chinese mainland will lag behind in semiconductor manufacturing process nodes for a relatively long time". Huawei's roadmap compensates with scale: SuperPoDs of up to 8,192 Ascend 950DT chips in Q4 2026 and 15,488 Ascend 960 chips in Q4 2027. SemiAnalysis estimates that CloudMatrix 384 delivers nearly double the dense BF16 compute of a GB200 NVL72 at 4.1 times the power. Where power is cheap and silicon scarce, EUV access raises Chinese compute per wafer and per watt. That matters, but it is not a binary capability barrier.

Reuters reported in December 2025 that a Shenzhen EUV prototype built with help from former ASML engineers generates EUV light but had not yet produced working chips. The government target for working chips is 2028; people close to the project say 2030. If the programme stays on that path, Europe's offer of EUV or servicing becomes a wasting asset over exactly the scenario window. The pace is uncertain. Gilli and Gilli (2019) show, for weapons systems, that rising complexity limits catch-up by imitation, and applying that to lithography is our inference. In the short run, what stays valuable to China is servicing its installed DUV base. That is the hedge option H in our model, and it is what the Dutch give up in Europe 2031's 2028 episode.

**Race decisiveness.** The race literature does not directly price inputs. It does identify the parameter that should scale them:
- **Armstrong, Bostrom and Shulman (2016):** more competing teams and more enmity raise the danger of disaster.
- **Stafford, Trager and Dafoe (2022):** under intense rivalry a close laggard cuts corners to gamble for advantage.
- **Emery-Xu, Park and Trager (2024):** more decisive races, "in which small performance leads produce larger probabilities of victory, are usually more dangerous".

Our extension is that decisiveness also raises the value of marginal capability, and so the value of chokepoint inputs.

Official rhetoric in 2025 and 2026 sits at the decisive end. The AI Action Plan opens with "a race to achieve global dominance in artificial intelligence". The Genesis Mission order says America "is in a race for global technology dominance". si.gov states "America is in a race for Super Intelligence. We intend to win it." On our reading, Europe 2031 belongs to the same genre as Situational Awareness and AI 2027, which both assume a decisive US-China race.

Ding (2024) and Horowitz (2018) push the other way. If power comes from diffusing a general-purpose technology across the economy, the frontier lead matters less, and so does denying chips to China or frontier models to Europe. We should not settle this by assumption. Race decisiveness should enter as the scale parameter Z. The key comparative static is that a decisive race raises V, W and alpha together, and Europe gains only if China's gain net of what the US can block rises faster than the AI stick.

**Compute governance and alpha.** The compute governance literature suggests it will not rise faster. Sastry et al. (2024) argue that compute is "detectable, excludable, and quantifiable, and is produced via an extremely concentrated supply chain". Heim et al. (2024) show how cloud providers can act as securers, record keepers, verifiers and enforcers. These features make alpha cheap to target, and the record now bears this out.

- **The January 2025 AI Diffusion rule (90 FR 4544)** listed 19 destinations for favourable treatment, the United States included. Ten were EU member states. Other non-D:5 destinations were held to a per-country allocation of 790 million TPP for 2025 to 2027. That is the scenario's tiered inference rule in embryo, and it is a ready-made wedge inside the Council.
- **On 12 June 2026** a US export-control directive barred access to Anthropic's Fable 5 and Mythos 5 by foreign nationals. Unable to restrict access by nationality, Anthropic disabled both models for all customers.
- **GovAI's analysis of 375 model releases** finds that, relative to the US, 11 percent were delayed or withheld in the EU and 7 percent in the UK, mostly because of data-protection regulation. It concludes that "US national security concerns – rather than regulation – may pose the greater barrier to European access to frontier AI".

**What it costs Washington to use alpha.** The export controls were lifted on 30 June, 18 days after they were imposed. Fable 5 came back worldwide on 1 July, but Mythos 5 came back only for a set of US organizations, with international partners still pending. The short duration is consistent with high execution costs for US firms, but it does not show them. Anthropic's statements say only that it disagreed with the finding and worked to restore access. Crosignani et al. (2024) show by analogy that export controls are costly for the sender's own firms: affected US suppliers lost about $130 billion in market value and did not replace their Chinese customers.

That execution cost is Europe's real counter-lever. It is what the Europe 2031 epilogue points to when it asks that data centres built in Europe be "bolted to our floor". Hosting US-owned capacity raises what it costs Washington to carry out Tier 3. The trend runs the wrong way, however:
- The EU-27's share of AI-chip compute arrivals fell from 5.7 percent in 2024 to 5.1 percent in 2025 and 4.6 percent in the first half of 2026.
- The epilogue's full coalition (EU-27, UK, Norway, Canada, Japan and South Korea) hosts about 9.3 percent of cumulative arrivals since 2022. That is far from the 15 to 20 percent the epilogue proposes for Europe alone.

**Three positions for the model.**

1. Treat ASML's value to the United States as large but irrelevant to Europe's leverage unless Europe can credibly interrupt servicing.
2. Model W as declining and theta as high. China's realistic gain is concentrated in servicing the installed DUV base and in EUV access before Chinese tools mature.
3. Model alpha as rising and cheap to target member by member. It is limited mainly by what US AI firms lose when they lose European customers.

Under these parameters, the AI dimension alone turns Europe's exit premium into a wasting asset, which pushes in the opposite direction from rearmament. Whether the net premium rises or falls over 2026 to 2031 is the empirical question on which the two-clocks result turns, and the paper should say so openly.

One way out is a coalition of chokepoint holders that conditions access jointly. Trager et al. (2023) sketch the institutional template: states certify jurisdictions and enforce standards through import bans and multilateral controls on inputs such as hardware. Lehdonvirta, Wu and Hawkins (2024) show that only states that host compute are well placed to govern through it, and Europe hosts little. The coalition idea is our extension of both. Japan and Korea face the same security linkage as Europe, though, so the coalition faces the same credibility problem one level up.

## Verified facts

| Claim | Date | Source |
|---|---|---|
| Europe 2031 was published 11 June 2026. Authors: Daan Juijn, Stan van Baarsen, Judith Dada, Maximilian Negele, Lily Stelling, Philip Fox, Alex Petropoulos and Michiel Bakker. "Copywriting and editing by Tom Chivers" (Chivers is not an author). | 2026-06-11 | https://europe2031.ai |
| Europe 2031, June 2026 baseline: "Europe hosts only five per cent of the world's total AI compute"; the United States "hosts eighty". The largest US AI supercomputer runs at 1,250 MW, the largest European one at 83 MW. | 2026-06-11 | https://europe2031.ai |
| Europe 2031 epilogue (framed as a June 2034 interview with Caroline): "We could have got to fifteen, maybe twenty per cent in five years, if we had wanted it badly enough." The proposed coalition is "the Netherlands, Germany, France, Norway, the UK, Canada, Japan, South Korea, perhaps assisted by the European Commission". "We screwed up royally with ASML, but it could have been avoided. The problem was that we tried to coordinate among twenty-seven Member States." Data centres built should be "bolted to our floor". | 2026-06-11 | https://europe2031.ai |
| Europe 2031, May 2028: ASML EUV "output has risen from sixty to eighty-five machines a year". In 2031 the US claims that through Taiwanese partners it "has amassed enough EUV machines and maintenance know-how" to forgo ASML access longer than Europe can forgo frontier AI. No stockpile figure is given. | 2026-06-11 (scenario dates 2028, 2031) | https://europe2031.ai |
| Our calculation from Epoch AI's by-country CSV (page updated 27 Oct 2026). Cumulative AI-chip compute arrivals 2022 Q1 to 2026 Q2 total 27.39M H100e: US 19.76M (72.2%), China 2.64M (9.6%), EU-27 1.39M (5.1%); UK, Norway, Switzerland and Iceland together 2.2%. The page reports the US range as 14.2M to 25M (5th to 95th percentile). Shares are by location of arrival, not ownership. | data through 2026 Q2; page 2026-10-27 | https://epoch.ai/data/ai-chip-imports (CSV: https://epoch.ai/data/ai_chip_trade/ai_chip_trade_by_country.csv) |
| Our calculation from the same CSV, shares of new arrivals by year. US 61.3% (2024), 72.3% (2025), 77.7% (2026 H1). China 15.2%, 10.1%, 6.1%. EU-27 5.7%, 5.1%, 4.6%. | 2024 to 2026 H1 | https://epoch.ai/data/ai-chip-imports |
| Our calculation from Epoch's designer breakdown. China's cumulative 2.64M H100e through 2026 Q2: Nvidia 1.60M, Huawei 0.98M, Cambricon 0.05M, AMD 0.01M. Domestic designers are about 39%. Epoch notes that the split by designer is modelled, because customs records do not identify chip models. | through 2026 Q2 | https://epoch.ai/data/ai_chip_trade/ai_chip_trade_by_country_breakdown.csv |
| Our calculation: the epilogue coalition (EU-27, Japan, UK, Canada, Norway, South Korea) hosts about 9.3% of cumulative arrivals through 2026 Q2 (EU 5.07, Japan 1.58, UK 1.24, Canada 0.53, Norway 0.47, South Korea 0.38 percent). | through 2026 Q2 | https://epoch.ai/data/ai-chip-imports |
| Pilz, Sanders, Rahman and Heim: dataset of 500 AI supercomputers, 2019 to 2025. Performance doubles about every nine months. The US holds about 75% of total performance and China about 15% (March 2025). If trends hold, the leading system in 2030 would use about 2 million chips, cost about $200 billion in hardware and need about 9 GW. | 2025-04-22 | https://arxiv.org/abs/2504.16026 |
| Epoch AI data-centres database: 96 sites, 14.5 GW IT power (18.9 GW facility), 15.2M H100e. Epoch estimates this covers 44% (90% CI 30 to 80%) of global deployed AI compute. | 2026-10-28 | https://epoch.ai/data/ai-data-centers |
| AI 2027 (Kokotajlo, Alexander, Larsen, Lifland, Dean; 3 April 2025): in mid-2026 "China has managed to maintain about 12% of the world's AI-relevant compute". | 2025-04-03 | https://ai-2027.com/ |
| ASML: EUV technology is "unique to ASML". "Chipmakers use our NXE systems to print the highly complex foundation layers of their 7 nm, 5 nm and 3 nm nodes." NXE:3800E and NXE:3600D also support "leading-edge DRAM nodes". | accessed 2026-10-28 | https://www.asml.com/en/products/euv-lithography-systems |
| Nvidia: Blackwell GPUs are "packed with 208 billion transistors" and "manufactured using a custom-built 4NP TSMC process". (Calling 4NP "5 nm-class" is our gloss: TSMC's N4 family derives from N5.) | 2024-03-18 | https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing |
| TSMC: N3 entered high-volume production in 2022. N2 "started volume production in 4Q25 as planned". N2P volume production is "scheduled for the second half of 2026". | accessed 2026-10-28 | https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_3nm |
| SK hynix announced on 12 July 2021 that it had started mass production that month of 8Gb LPDDR4 on its 1a nm node, its first use of EUV in mass production. It plans to use EUV "for production of all its 1anm DRAM products going forward". | 2021-07-12 | https://news.skhynix.com/sk-hynix-starts-mass-production-of-1anm-dram-using-euv-equipment/ |
| SK hynix completed HBM4 development on its 1b nm (fifth-generation 10 nm-class) process. The release does not mention EUV. | 2025-09-12 | https://news.skhynix.com/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/ |
| CSET (Khan, Peterson, Mann): ASML "controls over 85 percent of the market for scanners and steppers" (endnote). ASML exclusively produces EUV scanners, which are "necessary for mass-producing 5 nm node chips". Lithography tools are "China's most critical chokepoint". The Dutch ban on EUV exports "already prevents it from building capacity more advanced than 7 nm". | 2021-01 | https://cset.georgetown.edu/wp-content/uploads/The-Semiconductor-Supply-Chain-Issue-Brief-1.pdf |
| CSET: the US contributes 39% of the total value of the global semiconductor supply chain. US allies (Japan, Europe, Taiwan, South Korea) contribute 53% and China 6%. | 2021-01 | https://cset.georgetown.edu/publication/the-semiconductor-supply-chain/ |
| Thadani and Allen: ASML is "the sole provider of the latest generation of photolithography scanner equipment". Sales of microlithography equipment to China, mainly by ASML and Japanese firms, more than tripled between 2017 and 2021. | 2023-05-30 | https://www.csis.org/analysis/mapping-semiconductor-supply-chain-critical-role-indo-pacific-region |
| Allen (CSIS) on SMIC: about 20% yield and "20,000 7 nm monthly wafer production", with a target of 50,000 WPM of 7 nm by end-2025. As of December 2024, SMIC had immersion DUV tools that could support about 85,000 FinFET wafers per month across SN1 and SN2, bought before the mid-2023 Dutch controls. The 7 nm bottleneck is "U.S. tools for etching, deposition, inspection, and metrology". | 2025-03-07 | https://www.csis.org/analysis/deepseek-huawei-export-controls-and-future-us-china-ai-race |
| CORRECTED. CSIS, citing government officials: "TSMC manufactured more than 2 million Ascend 910B logic dies and ... all of these are now with Huawei", "enough dies to make 1 million Ascend 910C units". The CSIS text checked does not say "through shell companies". | 2025-03-07 | https://www.csis.org/analysis/deepseek-huawei-export-controls-and-future-us-china-ai-race |
| CORRECTED. Allen (CSIS): Chinese firms supplied 3.2% of semiconductor equipment by value globally and 9.6% of equipment bought in China in 2023 (Sanford Bernstein puts the domestic share nearer 15%). His "most likely explanation" for high allied sales to China is that Chinese firms bought earlier, ahead of expected controls. Partial controls impose most of the costs of aggressive ones with "comparatively few of the strategic benefits". | 2024-11-26 | https://www.csis.org/analysis/true-impact-allied-export-controls-us-and-chinese-semiconductor-manufacturing-equipment |
| Allen (CSIS): the BIS rules of 2 December 2024 extended FDP rules to restrict "a Japanese, Dutch, or other firm's sales from outside their home countries", exempting home markets with equivalent controls (Supplement No. 4 to Part 742: 33 countries, including most EU states and Japan). They added the first country-wide controls on advanced HBM to China and 140 Entity List entries. | 2024-12-02 (rules); article 2024-12-11 | https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls |
| Allen and Goldston (CSIS): the Netherlands referenced Article 9 of Regulation (EU) 2021/821 for its June 2023 regulation, and enforcement began in September 2023. Allied services controls apply "only ... for WMD end-uses", so Japanese and Dutch firms can keep supplying items and services that US firms cannot. | 2025-03-14 | https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export |
| TechInsights found that the Kirin 9000s in Huawei's Mate 60 Pro is made on SMIC's 7 nm (N+2) process, an advance achieved "without EUV lithography tools". (The page shows no date; September 2023 is inferred from the image path.) | 2023-09 | https://www.techinsights.com/blog/techinsights-finds-smic-7nm-n2-huawei-mate-60-pro |
| SemiAnalysis: CloudMatrix 384 (384 Ascend 910C) delivers about 300 PFLOPs dense BF16, almost double a GB200 NVL72, at 4.1x the power and 2.5x worse power per FLOP. "China has No Power Constraints, just Silicon Constraints." | 2025-04-16 | https://newsletter.semianalysis.com/p/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72 |
| Huawei Connect 2025 (Eric Xu): Ascend 950PR Q1 2026, 950DT Q4 2026, 960 Q4 2027, 970 Q4 2028. Self-developed HBM (HiBL 1.0, HiZQ 2.0). Atlas 950 SuperPoD of up to 8,192 chips (Q4 2026) and Atlas 960 of up to 15,488 (Q4 2027). "The Chinese mainland will lag behind in semiconductor manufacturing process nodes for a relatively long time." | 2025-09-18 | https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech |
| CORRECTED. Reuters (Fanny Potkin): a prototype EUV machine in a Shenzhen lab, completed in early 2025 with help from former ASML engineers, generates EUV light but "has not yet produced working chips". The government goal is working chips by 2028; people close to the project say 2030 is more realistic. Parts from older ASML machines on secondary markets helped. | 2025-12-17 (Reuters); 2025-12-18 (syndicated) | https://www.reuters.com/world/china/how-china-built-its-manhattan-project-rival-west-ai-chips-2025-12-17/ ; text checked at https://www.thejakartapost.com/business/2025/12/18/how-china-built-its-manhattan-project-to-rival-the-west-in-ai-chips |
| MERICS (Hmaidi): LineShine, an all-CPU system built on Huawei's ARMv9-based LX2, debuted at the top of the June 2026 TOP500 list (2.198 EFLOPS). It ranks fourth on HPL-MxP, an AI-workload benchmark, well behind El Capitan, and is unlikely to meaningfully ease China's AI training bottleneck. | 2026-09-10 | https://merics.org/en/comment/supercomputer-lineshine-restrictions-driven-leap-limitations |
| AI Action Plan: "We should encourage partners and allies to follow U.S. controls, and not backfill. If they do, America should use tools such as the Foreign Direct Product Rule and secondary tariffs to achieve greater international alignment." It also says: "develop new export controls on semiconductor manufacturing sub-systems". | 2025-07-23 | https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf |
| AI Action Plan opening: "The United States is in a race to achieve global dominance in artificial intelligence (AI)." "It is imperative that the United States and its allies win this race." | 2025-07-23 | https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf |
| EO 14320 sets up an American AI Exports Program for full-stack packages (hardware, data pipelines, models, security, applications), with federal financing coordinated by the Economic Diplomacy Action Group. Its policy is to "decrease international dependence on AI technologies developed by our adversaries". | 2025-07-23 | https://www.whitehouse.gov/presidential-actions/2025/07/promoting-the-export-of-the-american-ai-technology-stack/ |
| EO 14363 (Genesis Mission, led by DOE): America "is in a race for global technology dominance". The effort should be "comparable in urgency and ambition to the Manhattan Project". | 2025-11-24 | https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/ |
| si.gov: "America is in a race for Super Intelligence. We intend to win it." ai.gov redirects to si.gov (checked 28 Oct 2026). | accessed 2026-10-28 | https://www.si.gov/ |
| State Council, Guofa [2025] No. 11, on the "AI+" action (signed 21 Aug, published 26 Aug 2025). Targets: penetration of new-generation intelligent terminals and agents above 70% by 2027 and above 90% by 2030. | 2025-08-26 | https://www.gov.cn/zhengce/content/202508/content_7037861.htm |
| CORRECTED. AI Diffusion IFR (90 FR 4544 to 4584; published 15 Jan 2025, effective 13 Jan, compliance date 15 May 2025). Supplement No. 5 to Part 740(a) lists 19 destinations, the United States included. Ten are EU member states: Belgium, Denmark, Finland, France, Germany, Ireland, Italy, Netherlands, Spain, Sweden. Other non-D:5 destinations get a per-country allocation of 790,000,000 TPP for 2025 to 2027. | 2025-01-15 | https://www.govinfo.gov/content/pkg/FR-2025-01-15/html/2025-00636.htm |
| CORRECTED. BIS announced rescission of the AI Diffusion rule, whose compliance requirements were due on 15 May 2025, and told enforcement officials not to enforce it. It issued guidance "alerting industry to the risks of using PRC advanced computing ICs, including specific Huawei Ascend chips". It announced additional licensing for exports to Malaysia and Thailand "due to known instances of diversion". (The page as accessed reads "SI chips" where "AI chips" is meant.) | 2025-05-13 | https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens |
| CORRECTED. EO 14409 sets up a voluntary framework that gives the government access to covered frontier models "for a period of up to 30 days" before release to other trusted partners. Covered models are designated by a classified benchmarking of advanced cyber capabilities, with the Director of NSA making the determination. Section 3(c) says nothing in it authorizes "mandatory governmental licensing, preclearance, or permitting". The order has no export-control or foreign-access provision. | 2026-06-02 | https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/ |
| Anthropic: a US government export-control directive, under national security authority, barred access to Fable 5 and Mythos 5 by foreign nationals wherever located. Unable to restrict access by nationality, Anthropic disabled both models for all customers. Other models were unaffected. | 2026-06-12 | https://www.anthropic.com/news/fable-mythos-access |
| Anthropic: "As of today, June 30, the export controls on Fable 5 and Mythos 5 have been lifted." Fable 5 was available globally from 1 July. Mythos 5 was restored to "a set of US organizations" after US government approval on 26 June, and expansion to domestic and international Glasswing partners was still being coordinated. | 2026-06-30 | https://www.anthropic.com/news/redeploying-fable-5 |
| GovAI (Lidiard, Vereschak, Gibbs, Anderljung) analysed 375 LLM releases, June 2018 to May 2026. Relative to the US, 11% were delayed or not released to the EU and 7% to the UK. Regulation was the primary cause in 56 of 68 cases, with data protection the main barrier. Delays fell over time, with none for public releases in January to May 2026. "US national security concerns – rather than regulation – may pose the greater barrier to European access to frontier AI." A footnote says European organizations were initially absent from Project Glasswing (7 April 2026). | 2026-06-28 | https://www.governance.ai/research-paper/delays-to-frontier-ai-in-the-eu-and-uk (PDF: https://govai.b-cdn.net/Delays_to_Frontier_AI_in_the_EU_and_UK.pdf) |
| CNAS (Chilukuri): on 16 October 2026 MOFCOM and MOST announced "draft export controls for 40 different technologies", citing a post on X rather than the MOFCOM text. The drafts do not seem to affect China's existing open-weight models but may prepare the ground for restricting future ones. | 2026-10-26 (article); 2026-10-16 (event) | https://www.cnas.org/publications/cnas-insights/cnas-insights-a-closing-door-on-open-weights-implications-for-ai-sovereignty |
| CORRECTED. MERICS: Xi arrived in the US on 23 September 2026 for the second Trump-Xi summit of 2026, after their May meeting during Trump's visit to China. The US extended its suspension of additional tariffs from the 2025 Busan agreement until 10 January. "China will not further tighten export controls on rare earths for the time being." The US has "effectively halted foreign military sales" to Taiwan since Trump's China visit. A grand bargain on AI is "highly unlikely". | 2026-09-24 | https://merics.org/en/merics-briefs/ai-trump-xi-summit-taiwan-ev-overcapacities |
| Crosignani, Han, Macchiavelli and Silva (NY Fed SR 1096, April 2024, revised February 2025): affected US suppliers lost $130 billion in market capitalization, found no new customers at home or in aligned regions (no reshoring or friend-shoring), and saw profitability, employment and bank lending fall. | 2024-04 (rev. 2025-02) | https://www.newyorkfed.org/research/staff_reports/sr1096 |
| Rhodium Group (with SNV): China "currently controls around 30% of 50-180nm manufacturing capacity globally", possibly about 35% within five years. China and Taiwan hold about 60% of 20 to 45 nm capacity (China alone 27%). | 2023-04-04 | https://rhg.com/research/running-on-ice/ |
| BCG/SIA: "more than 50 points across the supply chain where one region holds over 65% of the global market share". Capacity below 10 nm was in Taiwan (92%) and South Korea (8%). Fully self-sufficient regional supply chains would have required at least about $1 trillion in incremental upfront investment. | 2021-04-01 | https://www.bcg.com/publications/2021/strengthening-the-global-semiconductor-supply-chain |
| Fist and Grunewald (CNAS): smuggling into China in 2023 was "likely in the hundreds, but plausibly in the low thousands". PRC-linked actors could smuggle "on the order of thousands to tens of thousands of AI chips per year". In the most optimistic case for smugglers, about 4% of 2025 global AI-chip production. | 2023-10-24 | https://www.cnas.org/publications/reports/preventing-ai-chip-smuggling-to-china |
| Allen (CSIS) on the 7 October 2022 controls: "strangling with an intent to kill", through four interlocking chokepoints (AI chips, EDA software, SME, SME components). "Cooperation from Europe, Japan, and South Korea is also needed." | 2022-10-11 | https://www.csis.org/analysis/choking-chinas-access-future-ai |

## Modeling implications

- **V, the US loss from defection: large but strategically inert.** In the short run all of TSMC's leading logic nodes (N5 to N2 families, including Blackwell's 4NP) and SK hynix's EUV DRAM nodes depend on ASML. The lemma that Europe cannot credibly interrupt supply to the US is still well supported, for three reasons: most of the installed base sits at Asian fabs; the December 2024 FDP rules reach ASML's non-Dutch sales; and the AI Action Plan threatens the FDPR and secondary tariffs. The only interruption channel with teeth is servicing and spare parts for the installed EUV base. If we model hold-up, we should model servicing, not shipments.
- **W, China's gain: split by option.**
  - **W_H (DUVi sales and servicing)** is modest and mostly about servicing. SMIC already holds DUVi for about 85,000 FinFET wafers a month, and its binding constraint is US etch, deposition and metrology tools.
  - **W_X (EUV, or high-end servicing and know-how)** is large but decays over 2028 to 2031 if the Shenzhen prototype reaches working chips on the official 2028 target or the insiders' 2030 estimate.
  - Let W_t decline, with a hazard tied to Chinese indigenization, and treat the decay rate as uncertain.
- **theta, the share of China's gain the US can block: high and rising.** US jurisdiction covers complementary tools, US-origin components and ASML's sales from outside the Netherlands. The Action Plan calls for controls on subsystems. This mechanically lowers Europe's exit premium Q_a = (1 - theta_a)W_a - c_a + r and strengthens Corollary 1(ii).
- **Z, race decisiveness: a scale parameter.** Use decisiveness in the sense of Emery-Xu, Park and Trager.
  - The decisive branch (Action Plan, Genesis, si.gov, AI 2027, Situational Awareness, and Europe 2031 on our reading) raises V, W and alpha together.
  - The diffusion branch (Ding 2024; Horowitz 2018) lowers all three.
  - The link from decisiveness to the value of inputs is our modelling assumption, not a result of the race papers.
  - Report Prop. 2 as conditional: Europe gains from race intensity only if (1 - theta) w > a. The evidence suggests that condition fails.
- **alpha, the US frontier-AI stick: credible, cheap to target and member-specific.** Two precedents:
  - The January 2025 AI Diffusion rule gave favourable treatment to 10 EU member states, among 19 listed destinations including the US, and held the rest to per-country allocations.
  - The 12 June 2026 directive cut off Fable 5 and Mythos 5 for foreign nationals.

  This supports member-specific alpha_i in Prop. 3, and a US divide-and-rule strategy that targets the veto player (the Netherlands as Tier 1).
- **c_U(alpha), the US cost of executing the AI cut.** Add it, increasing in US AI firms' European revenue and in US-owned compute sited in Europe. The evidence is suggestive, not conclusive. The June 2026 controls were lifted after 18 days for reasons Anthropic does not state. Crosignani et al. show that sender firms bear real costs when export controls cut them off from customers, but their case is China, not Europe. This parameter is the formal counterpart of the epilogue's "bolted to our floor" strategy, and the main route by which Europe can make the Tier 3 threat non-credible (Lemma 2).
- **Europe's compute base: calibrate with location data.** The EU-27 holds about 5% of cumulative AI-chip compute and took 4.6% of 2026 H1 arrivals; the full epilogue coalition (EU-27, UK, Norway, Canada, Japan, South Korea) holds about 9.3%. The epilogue's 15 to 20% target implies tripling Europe's share against a falling trend. Any "indispensability" extension should treat compute share as a costly investment with a lag of several years. Location is not ownership; see open questions.
- **The two-clocks corollary needs a caveat.** On the AI dimension the evidence points to Q_t falling (W declining, theta rising, alpha rising). Rearmament lowers kappa*S and pushes Q_t up. The direction of the net change is an empirical question. Present the window result as conditional on rearmament outpacing the decay of the AI-side premium.
- **r, China's coercive instrument: time-varying.**
  - China's mature-node share (about 30% of 50 to 180 nm in early 2023) gives it standing coercive capacity.
  - MERICS reports that China will not further tighten rare-earth controls "for the time being" (September 2026). The October 2025 controls and their suspension are verified in the china_dep and asml_facts strands.
  - The MOFCOM/MOST draft controls on 40 technologies (16 October 2026) widen China's menu.
  - The 2026 US-China summits add a risk from the side: a US-China bargain that devalues Europe's swing position. MERICS reports that US arms sales to Taiwan were effectively halted after the May summit, which shows that Washington is willing to trade with Beijing.
- **The US stockpile claim: a private-information extension.** Use one for the US claim, in Europe 2031, to have stockpiled enough EUV machines and maintenance know-how. Emery-Xu et al. show that revealing capabilities has opposing effects on race risk. Our inference, not theirs, is that the US has an incentive to misrepresent its outside option to ASML. Uncertainty about V and theta, not only about sigma, could then drive breakdown.

## Open questions

- **Verification limits.** WebSearch was unavailable for this strand, so every item was confirmed by fetching primary pages, by Crossref, OpenAlex, DataCite or arXiv lookups, or by recomputing from Epoch's CSV files. Three items were excluded for lack of confirmation:
  - a separate Bown piece on Dutch and Japanese alignment (Bown and Wang 2024 is the nearest confirmed work);
  - a CNAS or Clingendael report titled "The Netherlands and the chip war";
  - a journal venue for Stafford, Trager and Dafoe (only the November 2022 GovAI draft is confirmed).
- **ASML's China share and Q3 2026 results.** These were not checked in this strand. The asml_facts strand reports China at 29.1% of 2025 total net sales, about 20% guided for 2026, and 23% of Q3 2026 system sales. Those figures should feed W_H and ASML's own cost of compliance.
- **Does leading-edge HBM strictly require EUV?** SK hynix adopted EUV at 1a nm and builds HBM4 on 1b nm, but its HBM4 release does not mention EUV. ASML says its NXE systems support "leading-edge DRAM nodes". The answer decides whether China's HBM bottleneck is an ASML chokepoint or a US and Korean one.
- **How mature is China's EUV programme?** Reuters (December 2025) reports a working EUV light source but no chips. The decay rate of W_X over 2028 to 2031 depends heavily on whether the 2028 government target or the insiders' 2030 estimate holds, or neither. The asml_facts strand flags a June 2026 US claim that an EUV tool reached China; it is not verified here.
- **What was the legal basis of the June 2026 directive?** Anthropic cites only national security authority. EO 14409 contains no provisions on foreign access. Is a formal US rule on cross-border access to frontier models or inference coming? The model's analogue of the FISR rests on this.
- **Is the Busan truce, extended in September 2026 to 10 January, a stable US-China accommodation?** If so, the US may relax chip controls on China while still demanding European compliance, the scenario's "caved with nothing in return" pattern. That would lower V and change the structure of the three-player game.
- **Location versus ownership.** Epoch's country shares measure where chips arrive, not who owns or controls them. Much "European" compute is owned by US hyperscalers, which cuts both ways for leverage: hostages for Europe, levers for the US. A measure adjusted for ownership would sharpen the calibration of c_U(alpha).
- **Are Japan and Korea credible coalition partners?** They are the other lithography and memory chokepoint holders, but they share Europe's security dependence on the US. Neither Trager et al. (2023) nor Lehdonvirta et al. (2024) addresses whether pooling chokepoints helps when every member faces the same patron linkage. This is a gap our coalition extension should fill.

## BibTeX

```bibtex
@misc{juijn2026europe,
  author       = {Juijn, Daan and van Baarsen, Stan and Dada, Judith and Negele, Maximilian and Stelling, Lily and Fox, Philip and Petropoulos, Alex and Bakker, Michiel},
  title        = {Europe 2031},
  howpublished = {Scenario website},
  year         = {2026},
  month        = jun,
  url          = {https://europe2031.ai},
  note         = {Published 11 June 2026. Copywriting and editing by Tom Chivers. Accessed 28 October 2026}
}

@book{miller2022chip,
  author    = {Miller, Chris},
  title     = {Chip War: The Fight for the World's Most Critical Technology},
  publisher = {Scribner},
  address   = {New York},
  year      = {2022},
  isbn      = {9781982172008}
}

@misc{sastry2024computing,
  author        = {Sastry, Girish and Heim, Lennart and Belfield, Haydn and Anderljung, Markus and Brundage, Miles and Hazell, Julian and O'Keefe, Cullen and Hadfield, Gillian K. and Ngo, Richard and Pilz, Konstantin and Gor, George and Bluemke, Emma and Shoker, Sarah and Egan, Janet and Trager, Robert F. and Avin, Shahar and Weller, Adrian and Bengio, Yoshua and Coyle, Diane},
  title         = {Computing Power and the Governance of Artificial Intelligence},
  year          = {2024},
  eprint        = {2402.08797},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2402.08797},
  url           = {https://arxiv.org/abs/2402.08797}
}

@misc{heim2024governing,
  author        = {Heim, Lennart and Fist, Tim and Egan, Janet and Huang, Sihao and Zekany, Stephen and Trager, Robert and Osborne, Michael A. and Zilberman, Noa},
  title         = {Governing Through the Cloud: The Intermediary Role of Compute Providers in {AI} Regulation},
  year          = {2024},
  eprint        = {2403.08501},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2403.08501},
  url           = {https://arxiv.org/abs/2403.08501}
}

@misc{pilz2024increased,
  author        = {Pilz, Konstantin and Heim, Lennart and Brown, Nicholas},
  title         = {Increased Compute Efficiency and the Diffusion of {AI} Capabilities},
  year          = {2023},
  eprint        = {2311.15377},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2311.15377},
  url           = {https://arxiv.org/abs/2311.15377},
  note          = {v1 26 November 2023; v2 13 February 2024}
}

@misc{pilz2025trends,
  author        = {Pilz, Konstantin F. and Sanders, James and Rahman, Robi and Heim, Lennart},
  title         = {Trends in {AI} Supercomputers},
  year          = {2025},
  eprint        = {2504.16026},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2504.16026},
  url           = {https://arxiv.org/abs/2504.16026}
}

@misc{epoch2026imports,
  author       = {{Epoch AI}},
  title        = {Data on {AI} Chip Imports},
  howpublished = {Dataset, CC BY 4.0},
  year         = {2026},
  url          = {https://epoch.ai/data/ai-chip-imports},
  note         = {Last updated 27 October 2026; accessed 28 October 2026}
}

@misc{allen2022choking,
  author       = {Allen, Gregory C.},
  title        = {Choking off {China}'s Access to the Future of {AI}},
  howpublished = {Center for Strategic and International Studies},
  year         = {2022},
  month        = oct,
  url          = {https://www.csis.org/analysis/choking-chinas-access-future-ai},
  note         = {11 October 2022}
}

@techreport{thadani2023mapping,
  author      = {Thadani, Akhil and Allen, Gregory C.},
  title       = {Mapping the Semiconductor Supply Chain: The Critical Role of the {Indo-Pacific} Region},
  institution = {Center for Strategic and International Studies},
  type        = {CSIS Brief},
  year        = {2023},
  month       = may,
  url         = {https://www.csis.org/analysis/mapping-semiconductor-supply-chain-critical-role-indo-pacific-region},
  note        = {30 May 2023}
}

@misc{allen2024true,
  author       = {Allen, Gregory C.},
  title        = {The True Impact of Allied Export Controls on the {U.S.} and {Chinese} Semiconductor Manufacturing Equipment Industries},
  howpublished = {Center for Strategic and International Studies},
  year         = {2024},
  month        = nov,
  url          = {https://www.csis.org/analysis/true-impact-allied-export-controls-us-and-chinese-semiconductor-manufacturing-equipment},
  note         = {26 November 2024}
}

@misc{allen2024understanding,
  author       = {Allen, Gregory C.},
  title        = {Understanding the {Biden} Administration's Updated Export Controls},
  howpublished = {Center for Strategic and International Studies},
  year         = {2024},
  month        = dec,
  url          = {https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls},
  note         = {11 December 2024}
}

@techreport{allen2025deepseek,
  author      = {Allen, Gregory C.},
  title       = {{DeepSeek}, {Huawei}, Export Controls, and the Future of the {U.S.-China} {AI} Race},
  institution = {Center for Strategic and International Studies},
  type        = {Report},
  year        = {2025},
  month       = mar,
  url         = {https://www.csis.org/analysis/deepseek-huawei-export-controls-and-future-us-china-ai-race},
  note        = {7 March 2025}
}

@misc{allen2025allies,
  author       = {Allen, Gregory C. and Goldston, Isaac},
  title        = {Understanding {U.S.} Allies' Current Legal Authority to Implement {AI} and Semiconductor Export Controls},
  howpublished = {Center for Strategic and International Studies},
  year         = {2025},
  month        = mar,
  url          = {https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export},
  note         = {14 March 2025}
}

@techreport{khan2021semiconductor,
  author      = {Khan, Saif M. and Peterson, Dahlia and Mann, Alexander},
  title       = {The Semiconductor Supply Chain: Assessing National Competitiveness},
  institution = {Center for Security and Emerging Technology},
  type        = {Issue Brief},
  year        = {2021},
  month       = jan,
  doi         = {10.51593/20190016},
  url         = {https://cset.georgetown.edu/publication/the-semiconductor-supply-chain/}
}

@article{bown2020marched,
  author  = {Bown, Chad P.},
  title   = {How the {United States} Marched the Semiconductor Industry into Its Trade War with {China}},
  journal = {East Asian Economic Review},
  year    = {2020},
  volume  = {24},
  number  = {4},
  pages   = {349--388},
  doi     = {10.11644/KIEP.EAER.2020.24.4.384}
}

@techreport{bown2020export,
  author      = {Bown, Chad P.},
  title       = {Export Controls: {America}'s Other National Security Threat},
  institution = {Peterson Institute for International Economics},
  type        = {Working Paper},
  number      = {20-8},
  year        = {2020},
  month       = may,
  url         = {https://www.piie.com/publications/working-papers/export-controls-americas-other-national-security-threat},
  note        = {Also on SSRN, doi:10.2139/ssrn.3607276}
}

@article{bown2024semiconductors,
  author  = {Bown, Chad P. and Wang, Dan},
  title   = {Semiconductors and Modern Industrial Policy},
  journal = {Journal of Economic Perspectives},
  year    = {2024},
  volume  = {38},
  number  = {4},
  pages   = {81--110},
  doi     = {10.1257/jep.38.4.81}
}

@techreport{varas2021strengthening,
  author      = {Varas, Antonio and Varadarajan, Raj and Palma, Ramiro and Goodrich, Jimmy and Yinug, Falan},
  title       = {Strengthening the Global Semiconductor Supply Chain in an Uncertain Era},
  institution = {Boston Consulting Group and Semiconductor Industry Association},
  year        = {2021},
  month       = apr,
  url         = {https://www.bcg.com/publications/2021/strengthening-the-global-semiconductor-supply-chain}
}

@techreport{kleinhans2020global,
  author      = {Kleinhans, Jan-Peter and Baisakova, Nurzat},
  title       = {The Global Semiconductor Value Chain: A Technology Primer for Policy Makers},
  institution = {Stiftung Neue Verantwortung},
  address     = {Berlin},
  year        = {2020},
  month       = jun,
  url         = {https://www.interface-eu.org/publications/global-semiconductor-value-chain-technology-primer-policy-makers},
  note        = {SNV is now interface. Landing page dated 10 June 2020}
}

@techreport{kleinhans2023running,
  author      = {Kleinhans, Jan-Peter and Goujon, Reva and Hess, Julia and Piper, Lauren D.},
  title       = {Running on Ice: {China}'s Chipmakers in a {Post-October 7} World},
  institution = {Rhodium Group},
  year        = {2023},
  month       = apr,
  url         = {https://rhg.com/research/running-on-ice/},
  note        = {4 April 2023. Prepared in cooperation with Stiftung Neue Verantwortung}
}

@book{ding2024technology,
  author    = {Ding, Jeffrey},
  title     = {Technology and the Rise of Great Powers: How Diffusion Shapes Economic Competition},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  year      = {2024},
  isbn      = {9780691260334},
  doi       = {10.2307/jj.12228596}
}

@article{ding2024diffusion,
  author  = {Ding, Jeffrey},
  title   = {The Diffusion Deficit in Scientific and Technological Power: Re-assessing {China}'s Rise},
  journal = {Review of International Political Economy},
  year    = {2024},
  volume  = {31},
  number  = {1},
  pages   = {173--198},
  doi     = {10.1080/09692290.2023.2173633}
}

@article{ding2021logic,
  author  = {Ding, Jeffrey and Dafoe, Allan},
  title   = {The Logic of Strategic Assets: From Oil to {AI}},
  journal = {Security Studies},
  year    = {2021},
  volume  = {30},
  number  = {2},
  pages   = {182--212},
  doi     = {10.1080/09636412.2021.1915583}
}

@article{armstrong2016racing,
  author  = {Armstrong, Stuart and Bostrom, Nick and Shulman, Carl},
  title   = {Racing to the Precipice: A Model of Artificial Intelligence Development},
  journal = {AI \& Society},
  year    = {2016},
  volume  = {31},
  number  = {2},
  pages   = {201--206},
  doi     = {10.1007/s00146-015-0590-y}
}

@misc{stafford2022safety,
  author       = {Stafford, Eoghan and Trager, Robert and Dafoe, Allan},
  title        = {Safety Not Guaranteed: International Strategic Dynamics of Risky Technology Races},
  howpublished = {Centre for the Governance of AI, working paper (draft)},
  year         = {2022},
  month        = nov,
  url          = {https://www.governance.ai/research-paper/safety-not-guaranteed-international-strategic-dynamics-of-risky-technology-races},
  note         = {Draft dated November 2022; journal publication not confirmed}
}

@article{emeryxu2024uncertainty,
  author  = {Emery-Xu, Nicholas and Park, Andrew and Trager, Robert},
  title   = {Uncertainty, Information, and Risk in International Technology Races},
  journal = {Journal of Conflict Resolution},
  year    = {2024},
  volume  = {68},
  number  = {10},
  pages   = {2019--2047},
  doi     = {10.1177/00220027231214996}
}

@article{han2020regulate,
  author  = {Han, The Anh and Pereira, Lu{\'\i}s Moniz and Santos, Francisco C. and Lenaerts, Tom},
  title   = {To Regulate or Not: A Social Dynamics Analysis of an Idealised {AI} Race},
  journal = {Journal of Artificial Intelligence Research},
  year    = {2020},
  volume  = {69},
  pages   = {881--921},
  doi     = {10.1613/jair.1.12225}
}

@article{naude2020race,
  author  = {Naud{\'e}, Wim and Dimitri, Nicola},
  title   = {The Race for an Artificial General Intelligence: Implications for Public Policy},
  journal = {AI \& Society},
  year    = {2020},
  volume  = {35},
  number  = {2},
  pages   = {367--379},
  doi     = {10.1007/s00146-019-00887-x}
}

@article{horowitz2018artificial,
  author  = {Horowitz, Michael C.},
  title   = {Artificial Intelligence, International Competition, and the Balance of Power},
  journal = {Texas National Security Review},
  year    = {2018},
  volume  = {1},
  number  = {3},
  pages   = {36--57},
  doi     = {10.15781/T2639KP49}
}

@article{gilli2019china,
  author  = {Gilli, Andrea and Gilli, Mauro},
  title   = {Why {China} Has Not Caught Up Yet: Military-Technological Superiority and the Limits of Imitation, Reverse Engineering, and Cyber Espionage},
  journal = {International Security},
  year    = {2019},
  volume  = {43},
  number  = {3},
  pages   = {141--189},
  doi     = {10.1162/isec_a_00337}
}

@inproceedings{lehdonvirta2024compute,
  author    = {Lehdonvirta, Vili and Wu, Boxi and Hawkins, Zoe},
  title     = {Compute North vs. Compute South: The Uneven Possibilities of Compute-based {AI} Governance Around the Globe},
  booktitle = {Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society},
  year      = {2024},
  volume    = {7},
  pages     = {828--838},
  doi       = {10.1609/aies.v7i1.31683}
}

@misc{trager2023international,
  author        = {Trager, Robert and Harack, Ben and Reuel, Anka and Carnegie, Allison and Heim, Lennart and Ho, Lewis and Kreps, Sarah and Lall, Ranjit and Larter, Owen and {\'O} h{\'E}igeartaigh, Se{\'a}n and Staffell, Simon and Villalobos, Jos{\'e} Jaime},
  title         = {International Governance of Civilian {AI}: A Jurisdictional Certification Approach},
  year          = {2023},
  eprint        = {2308.15514},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2308.15514},
  url           = {https://arxiv.org/abs/2308.15514}
}

@techreport{crosignani2024securing,
  author      = {Crosignani, Matteo and Han, Lina and Macchiavelli, Marco and Silva, Andr{\'e} F.},
  title       = {Securing Technological Leadership? The Cost of Export Controls on Firms},
  institution = {Federal Reserve Bank of New York},
  type        = {Staff Reports},
  number      = {1096},
  year        = {2024},
  month       = apr,
  doi         = {10.59576/sr.1096},
  url         = {https://www.newyorkfed.org/research/staff_reports/sr1096},
  note        = {Revised February 2025. Previously titled ``Geopolitical Risk and Decoupling: Evidence from U.S. Export Controls''}
}

@techreport{fist2023preventing,
  author      = {Fist, Tim and Grunewald, Erich},
  title       = {Preventing {AI} Chip Smuggling to {China}},
  institution = {Center for a New American Security},
  type        = {Working Paper},
  year        = {2023},
  month       = oct,
  url         = {https://www.cnas.org/publications/reports/preventing-ai-chip-smuggling-to-china},
  note        = {24 October 2023}
}

@misc{chilukuri2026closing,
  author       = {Chilukuri, Vivek},
  title        = {A Closing Door on Open Weights? Implications for {AI} Sovereignty},
  howpublished = {CNAS Insights, Center for a New American Security},
  year         = {2026},
  month        = oct,
  url          = {https://www.cnas.org/publications/cnas-insights/cnas-insights-a-closing-door-on-open-weights-implications-for-ai-sovereignty},
  note         = {26 October 2026}
}

@techreport{lidiard2026delays,
  author      = {Lidiard, John and Vereschak, Oleksandra and Gibbs, Tom and Anderljung, Markus},
  title       = {Delays to Frontier {AI} in the {EU} and {UK}: Analysis of 375 {LLM} Releases by {Meta}, {Google}, {OpenAI}, and {Anthropic}},
  institution = {Centre for the Governance of AI},
  type        = {Technical Report},
  year        = {2026},
  month       = jun,
  url         = {https://www.governance.ai/research-paper/delays-to-frontier-ai-in-the-eu-and-uk},
  note        = {28 June 2026}
}

@techreport{gehrke2023power,
  author      = {Gehrke, Tobias and Ringhof, Julian},
  title       = {The Power of Control: How the {EU} Can Shape the New Era of Strategic Export Restrictions},
  institution = {European Council on Foreign Relations},
  type        = {Policy Brief},
  year        = {2023},
  month       = may,
  url         = {https://ecfr.eu/publication/the-power-of-control-how-the-eu-can-shape-the-new-era-of-strategic-export-restrictions/},
  note        = {17 May 2023}
}

@techreport{poitiers2021new,
  author      = {Poitiers, Niclas and Weil, Pauline},
  title       = {A New Direction for the {European Union}'s Half-Hearted Semiconductor Strategy},
  institution = {Bruegel},
  type        = {Policy Contribution},
  number      = {17/2021},
  year        = {2021},
  month       = jul,
  url         = {https://www.bruegel.org/policy-brief/new-direction-european-unions-half-hearted-semiconductor-strategy},
  note        = {15 July 2021}
}

@misc{hmaidi2026lineshine,
  author       = {Hmaidi, Antonia},
  title        = {Supercomputer {LineShine}: A Restrictions-Driven Leap with Limitations},
  howpublished = {MERICS Comment, Mercator Institute for China Studies},
  year         = {2026},
  month        = sep,
  url          = {https://merics.org/en/comment/supercomputer-lineshine-restrictions-driven-leap-limitations},
  note         = {10 September 2026}
}

@misc{aschenbrenner2024situational,
  author       = {Aschenbrenner, Leopold},
  title        = {Situational Awareness: The Decade Ahead},
  howpublished = {Essay series},
  year         = {2024},
  month        = jun,
  url          = {https://situational-awareness.ai/}
}

@misc{kokotajlo2025ai2027,
  author       = {Kokotajlo, Daniel and Alexander, Scott and Larsen, Thomas and Lifland, Eli and Dean, Romeo},
  title        = {{AI} 2027},
  howpublished = {AI Futures Project, scenario website},
  year         = {2025},
  month        = apr,
  url          = {https://ai-2027.com/},
  note         = {3 April 2025}
}

@techreport{whitehouse2025actionplan,
  author      = {{The White House}},
  title       = {Winning the Race: {America}'s {AI} Action Plan},
  institution = {Executive Office of the President},
  year        = {2025},
  month       = jul,
  url         = {https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf}
}

% Additional primary sources used in the synthesis (verified in this review)

@misc{bis2025diffusion,
  author       = {{U.S. Department of Commerce, Bureau of Industry and Security}},
  title        = {Framework for Artificial Intelligence Diffusion},
  howpublished = {Interim final rule, Federal Register 90(9): 4544--4584, FR Doc. 2025-00636},
  year         = {2025},
  month        = jan,
  url          = {https://www.govinfo.gov/content/pkg/FR-2025-01-15/html/2025-00636.htm},
  note         = {Published 15 January 2025; effective 13 January 2025}
}

@misc{bis2025rescission,
  author       = {{U.S. Department of Commerce, Bureau of Industry and Security}},
  title        = {Department of Commerce Announces Rescission of {Biden}-Era Artificial Intelligence Diffusion Rule, Strengthens Chip-Related Export Controls},
  howpublished = {Press release},
  year         = {2025},
  month        = may,
  url          = {https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens},
  note         = {13 May 2025}
}

@misc{anthropic2026directive,
  author       = {{Anthropic}},
  title        = {Statement on the {US} Government Directive to Suspend Access to {Fable 5} and {Mythos 5}},
  howpublished = {Company statement},
  year         = {2026},
  month        = jun,
  url          = {https://www.anthropic.com/news/fable-mythos-access},
  note         = {12 June 2026}
}

@misc{anthropic2026redeploy,
  author       = {{Anthropic}},
  title        = {Redeploying {Fable 5}},
  howpublished = {Company statement},
  year         = {2026},
  month        = jun,
  url          = {https://www.anthropic.com/news/redeploying-fable-5},
  note         = {30 June 2026}
}

@misc{potkin2025reuters,
  author       = {Potkin, Fanny},
  title        = {How {China} Built Its `{Manhattan Project}' to Rival the {West} in {AI} Chips},
  howpublished = {Reuters; republished in The Jakarta Post, 18 December 2025},
  year         = {2025},
  month        = dec,
  url          = {https://www.thejakartapost.com/business/2025/12/18/how-china-built-its-manhattan-project-to-rival-the-west-in-ai-chips}
}

@misc{eo14409,
  author       = {{The White House}},
  title        = {Promoting Advanced Artificial Intelligence Innovation and Security (Executive Order 14409)},
  year         = {2026},
  month        = jun,
  url          = {https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/},
  note         = {2 June 2026}
}

@misc{eo14363,
  author       = {{The White House}},
  title        = {Launching the {Genesis Mission} (Executive Order 14363)},
  year         = {2025},
  month        = nov,
  url          = {https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/},
  note         = {24 November 2025}
}

@misc{xu2025huaweiconnect,
  author       = {Xu, Eric},
  title        = {Groundbreaking {SuperPoD} Interconnect: Leading a New Paradigm for {AI} Infrastructure},
  howpublished = {Keynote, Huawei Connect 2025, Shanghai},
  year         = {2025},
  month        = sep,
  url          = {https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech},
  note         = {18 September 2025}
}
```
