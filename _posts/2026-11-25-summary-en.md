---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25 23:03:35 +0000
lang: en
report: default
---

> From 156 items, 8 important content pieces were selected

---

1. [Minecraft Java RCE via Malicious Resource-Pack Font, No Patch Yet](#item-1) ⭐️ 8.0/10
2. [Commerce Department Threatened Intel Into Handing Over 10% Stake, Court Filings Show](#item-2) ⭐️ 8.0/10
3. [SpaceX and Tesla reportedly form special committees to negotiate $3.5T all-stock merger](#item-3) ⭐️ 7.0/10
4. [Samsung and SK Hynix to Adopt YMTC&\#x27;s Xtacking Bonding Tech for 3D NAND](#item-4) ⭐️ 7.0/10
5. [LeCun Accuses Amodei of Using AI-Risk Fear to Justify Open-Model Bans](#item-5) ⭐️ 6.0/10
6. [SpaceX gives up $738M BEAD subsidy to hand out free Starlink terminals](#item-6) ⭐️ 6.0/10
7. [OpenAI Bets on Cybersecurity as a Business Bigger Than Coding](#item-7) ⭐️ 6.0/10
8. [Asian Data Centers Seek U.S. Buyers for Surplus AI Compute After U.S. Closes Export Loophole](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Minecraft Java RCE via Malicious Resource-Pack Font, No Patch Yet](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

A public proof-of-concept called minecraft2shell, published on November 22 by GitHub user &\#x27;bikini&\#x27;, shows that a Minecraft: Java Edition server can push a crafted resource pack containing a malicious TrueType font that triggers a native out-of-bounds write in FreeType 2.14.3 and earlier, ultimately achieving arbitrary code execution on a Windows client. All Java Edition versions from 1.20.5 through 1.21.10, plus the 26.1–26.4 snapshots, are affected, while 1.20.4 and earlier and Bedrock Edition are not; Mojang still ships lwjgl-freetype 3.4.3 and has released no official fix. The attack surface is unusually wide because server resource packs can be delivered and applied automatically when a player joins, meaning a player only has to connect to a malicious or compromised server to be exposed. With a public PoC circulating and no upstream patch, every Java Edition server operator and player on 1.20.5+ has to rely on community workarounds or manual hardening in the meantime. The flaw is a native memory-corruption bug in FreeType reached through Minecraft&\#x27;s font rendering path, and the published exploit is demonstrated against the Windows client since it depends on platform-specific payload delivery. The community fix m2sfix 1.0.0, released November 24, works as a Java agent or a mod and neutralizes the bug by loading every font with hinting disabled, so the font&\#x27;s own bytecode never runs. The reporter&\#x27;s interim advice is to add no resource packs at all and to set the multiplayer server resource-pack policy to &\#x27;Disabled&\#x27; until an official patch lands.

telegram · zaihuapd · Nov 25, 12:46

**Background**: FreeType is the widely used open-source font rasterizer that Minecraft: Java Edition reaches through LWJGL&\#x27;s lwjgl-freetype bindings to draw TrueType text, so any memory-safety bug in FreeType becomes a bug in the game itself. TrueType fonts can carry hinting bytecode — a small instruction set interpreted by the font engine to improve rendering at small sizes — which makes font files a genuine code-execution surface rather than inert data. FreeType has a long history of such parsing bugs; CVE-2025-27363, an out-of-bounds write when parsing TrueType GX and variable-font subglyph structures, was added to CISA&\#x27;s Known Exploited Vulnerabilities catalog. Resource packs are normally harmless cosmetic bundles of textures, sounds and fonts, but server-side resource packs are downloaded and applied automatically on join, which is what turns a font file into a remote attack vector.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cyberkendra.com/2026/11/minecraft2shell-minecraft-java-rce-resource-pack.html">Minecraft2Shell RCE in Minecraft Java Still Unpatched</a></li>
<li><a href="https://threatcluster.io/cluster/minecraft2shell-unpatched-freetype-rce-in-minecraft-java-via-7b380721">Minecraft2Shell: Unpatched FreeType RCE in Minecraft Java via ...</a></li>
<li><a href="https://wurst.wiki/minecraft2shell">Minecraft2Shell Vulnerability [Wurst.Wiki]</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#minecraft`, `#freetype`, `#rce`

---

<a id="item-2"></a>
## [Commerce Department Threatened Intel Into Handing Over 10% Stake, Court Filings Show](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 8.0/10

Court documents reviewed by WIRED show that in August 2025 a US Commerce Department lawyer told Intel&\#x27;s CFO on a phone call not to &quot;mistake this for a negotiation,&quot; saying the President wanted the agreement announced that Friday and warning that while the board could refuse, doing so would bring unpredictable consequences. Days later Intel&\#x27;s board transferred the shares, and Trump announced the US government &quot;fully owns and controls&quot; 10% of Intel — a stake reportedly acquired without payment that is now worth roughly $11 billion. This is a paradigm shift in US industrial policy: Washington is no longer just subsidizing chipmakers but taking equity under explicit pressure, which raises fundamental questions about property rights and corporate governance for every company reliant on federal support. The precedent could reshape how semiconductor firms, and the investors who fund them, weigh the political risk of accepting CHIPS Act money. The account comes from court filings rather than Intel or Commerce Department statements, and it describes a single phone call rather than a written agreement. The government&\#x27;s framing is that it did not pay cash because the equity was structured around converting previously committed federal grant money — the distinction between &quot;free&quot; and &quot;no new money&quot; is central to the dispute.

telegram · zaihuapd · Nov 25, 13:25

**Background**: Under the 2022 CHIPS and Science Act, the US government pledged roughly $52.7 billion in subsidies to rebuild domestic semiconductor manufacturing, and Intel was the largest single recipient. Intel had been burning cash on a costly foundry build-out while losing share to rivals, leaving it unusually dependent on federal support. Historically, Washington has used grants, loans and tax credits rather than direct equity stakes in private firms, making a 10% government holding in a strategic chipmaker highly unusual.

**Tags**: `#semiconductors`, `#Intel`, `#US policy`, `#tech regulation`, `#geopolitics`

---

<a id="item-3"></a>
## [SpaceX and Tesla reportedly form special committees to negotiate $3.5T all-stock merger](https://thenextweb.com/news/spacex-tesla-merger-five-directors-special-committees) ⭐️ 7.0/10

SpaceX and Tesla have each formed a special committee of directors — five in total — to negotiate a potential all-stock merger valued at roughly $3.5 trillion, with the parties reportedly aiming to reach a deal by the end of the year. If completed, it would be the largest merger in corporate history. The deal would combine Musk&\#x27;s rocket and satellite-broadband business with the world&\#x27;s most valuable automaker into a single privately-influenced giant, concentrating capital, talent and Musk&\#x27;s personal control in one entity. It could reshape how investors value both companies and raise significant governance and regulatory questions for U.S. markets. The committees still need to settle the exchange ratio for the all-stock deal, build shareholder support, and guard against investor litigation of the kind triggered by Musk&\#x27;s earlier transactions; sources say the two sides are not yet close to an agreement. The report is based on unnamed people familiar with the matter and has not been confirmed by either company.

telegram · zaihuapd · Nov 25, 00:41

**Background**: SpaceX is Musk&\#x27;s privately held space launch and Starlink satellite-internet company, while Tesla is a publicly traded electric-vehicle and energy-storage maker. An all-stock merger means no cash changes hands; instead, shareholders of one company receive shares of the other at an agreed exchange ratio, which makes the ratio the central point of negotiation. Because SpaceX is not publicly listed, combining it with Tesla would effectively bring the rocket business into public markets through Tesla&\#x27;s existing listing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/zh/learn/articles/how-special-committees-review-related-party-mergers">特别委员会如何审查关联方并购？从利益冲突到股东权益保护</a></li>
<li><a href="https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E/all-stock">ALL-STOCK在劍橋英語詞典中的解釋及翻譯</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Tesla`, `#Merger`, `#Musk`, `#Business`

---

<a id="item-4"></a>
## [Samsung and SK Hynix to Adopt YMTC&\#x27;s Xtacking Bonding Tech for 3D NAND](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

Samsung Electronics and SK Hynix have reportedly agreed, through a cross-licensing arrangement, to adopt parts of YMTC&\#x27;s Xtacking wafer-bonding technology in their own 3D NAND production. All three companies declined to comment on the report, which was relayed by an Omdia senior analyst who noted that bonding-based approaches offer clear advantages over conventional NAND manufacturing. Samsung and SK Hynix together dominate global memory production, so their willingness to license technology from a Chinese memory maker marks a notable reversal in the usual direction of technology flow. It also validates wafer-to-wafer hybrid bonding as a mainstream alternative to conventional NAND scaling at a time when stacking past 300 layers is straining traditional processes. Xtacking builds the NAND memory array and the CMOS periphery on two separate wafers that are then bonded together through metal interconnect vias, letting each side be manufactured and optimized independently. According to the Omdia analyst, this lets a memory maker fabricate the array itself while sourcing the logic die from a foundry, giving access to more advanced process nodes; the report remains unconfirmed and no licensing terms or timelines were disclosed.

telegram · zaihuapd · Nov 25, 14:33

**Background**: 3D NAND stores data by stacking vertical layers of memory cells, and the conventional approach places the CMOS control circuitry directly beneath the array on the same wafer \(CMOS-under-array\). Hybrid bonding instead joins a separately fabricated array wafer to a CMOS wafer using direct dielectric and copper-to-copper bonding without solder bumps or through-silicon vias, enabling sub-micron interconnect pitch. YMTC, China&\#x27;s leading NAND maker, pioneered this split-wafer scheme under the Xtacking brand and has taken it through several generations, and the approach is now being examined across the industry as a route to higher layer counts.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/656053590">关于直接混合键合工艺（Hybrid Bonding） - 知乎 Hybrid Bonding在长江存储Xtacking架构中应用 - 今日头条 Hybrid bonding technology for 3D Integration: Fundamentals ... High-Density 3-D NAND Cell Array Design With Hybrid Bonding [2611.27479] 3D-NAND-CIM: A Hybrid-Bonded 3D-NAND-Flash-based ... 决战混合键合 - 36氪</a></li>
<li><a href="https://developer.aliyun.com/article/1100149">长 江 存 储 YMTC Xtacking 技 术 演进与芯片级解密-开发者社区-阿里云</a></li>
<li><a href="https://www.toutiao.com/article/7665954183945765416/">Hybrid Bonding在长江存储Xtacking架构中应用 - 今日头条</a></li>

</ul>
</details>

**Tags**: `#3D NAND`, `#semiconductor manufacturing`, `#hybrid bonding`, `#YMTC`, `#memory industry`

---

<a id="item-5"></a>
## [LeCun Accuses Amodei of Using AI-Risk Fear to Justify Open-Model Bans](https://x.com/ylecun/status/2124550037912920090) ⭐️ 6.0/10

On November 22, Yann LeCun posted on X accusing Anthropic CEO Dario Amodei of having hyped AI danger since the GPT-2 era in order to push for making open models illegal and keep control of the technology. LeCun claimed Amodei left OpenAI because he could not obtain control there, and likened the approach to the Ottoman Empire&\#x27;s ban on Arabic-language printing, calling it &quot;a new form of medieval obscurantism.&quot; The exchange pits two of the most prominent figures in AI against each other over a live policy question: whether open-weight models should be restricted. With governments still drafting AI rules, a Nobel-level Turing laureate framing safety arguments as a control grab could intensify the split between the open-source camp and the frontier-lab safety camp. The post is a single accusatory tweet with no technical argument or linked analysis, and it flattens a more nuanced position: Anthropic has said Amodei does not support a categorical ban on open-weight models and is mainly concerned with frontier systems that could have dangerous capabilities. The dispute is therefore partly a framing fight over whether &quot;safety&quot; means testing the most powerful models or restricting openness in general.

telegram · zaihuapd · Nov 25, 01:30

**Background**: Yann LeCun is a French-American computer scientist who shared the 2018 Turing Award with Geoffrey Hinton and Yoshua Bengio, largely for his work on convolutional neural networks such as LeNet, developed at Bell Labs from the late 1980s. He spent about 12 years as Meta&\#x27;s chief AI scientist before leaving in November 2025 to found AMI Labs, a startup focused on &quot;world models&quot; rather than large language models. Dario Amodei, a former OpenAI researcher, co-founded Anthropic, the company behind the Claude models, which has positioned itself around AI safety research. The open-weight debate concerns models whose trained parameters are publicly downloadable, as opposed to closed API-only systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yann_LeCun">Yann LeCun - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/01/23/whos-behind-ami-labs-yann-lecuns-world-model-startup/">Who&#x27;s behind AMI Labs , Yann LeCun &#x27;s ‘world model’ startup</a></li>
<li><a href="https://www.thestreet.com/technology/anthropic-open-weight-ai-ban-dario-amodei-dario-amodei">Anthropic clarifies stance on open - weight AI models - TheStreet</a></li>
<li><a href="https://en.wikipedia.org/wiki/LeNet">LeNet - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open source AI`, `#AI safety debate`, `#Yann LeCun`, `#industry commentary`

---

<a id="item-6"></a>
## [SpaceX gives up $738M BEAD subsidy to hand out free Starlink terminals](https://x.com/SawyerMerritt/status/2125314062997467640) ⭐️ 6.0/10

SpaceX has agreed to a &\#x27;zero-dollar&\#x27; agreement under the NTIA&\#x27;s BEAD program, forgoing $738 million in federal broadband subsidies and receiving $0 in federal funding. In exchange, the company commits to providing free Starlink terminals to eligible US households, service of at least 100 Mbps down and 20 Mbps up, low-cost monthly plans, and a 10-year service commitment. The deal shows a major satellite ISP trading subsidy dollars for regulatory relief, which could reshape how BEAD funding is structured for other participants and how quickly unserved households get connected. It also matters politically, since BEAD has faced Republican criticism over slow fiber-centric buildouts and satellite providers were long seen as marginal to the program. SpaceX still must meet the same delivery timelines and network performance testing as other BEAD subvented recipients, but it is exempted from most financial audit, procurement and administrative reporting obligations. The 100/20 Mbps floor matches BEAD&\#x27;s baseline speed requirement for funded deployments.

telegram · zaihuapd · Nov 25, 02:17

**Background**: The BEAD \(Broadband Equity, Access, and Deployment\) program is a $42.45 billion grant initiative created by the 2021 Infrastructure Investment and Jobs Act and administered by the National Telecommunications and Information Administration \(NTIA\), a Commerce Department agency. It channels money to states to subsidize broadband buildout in unserved and underserved areas, historically with a strong preference for fiber. Satellite providers such as Starlink have argued they can reach remote locations faster and cheaper than trenching fiber, and the terms of their participation have been contested throughout the program&\#x27;s rollout.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fierce-network.com/broadband/ntia-toots-its-own-horn-regard-bead-or-it-swan-song">NTIA toots its own horn in regard to BEAD . Or is it a swan song?</a></li>
<li><a href="https://broadbandbreakfast.com/ntia-says-its-delivering-on-broadband-pledges/">NTIA Says It&#x27;s Delivering on Broadband Pledges</a></li>
<li><a href="https://www.americantv.com/ntia-must-not-allow-bead-to-fall-victim-to-past-mistakes.php">The NTIA Must Not Allow BEAD to Fall Victim to Past Mistakes</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starlink`, `#broadband-policy`, `#BEAD`, `#satellite-internet`

---

<a id="item-7"></a>
## [OpenAI Bets on Cybersecurity as a Business Bigger Than Coding](https://www.theinformation.com/newsletters/ai-agenda/openais-roadmap-making-cyber-bigger-coding-remains-blurry) ⭐️ 6.0/10

OpenAI is now positioning cybersecurity as its next major growth engine, with President Greg Brockman saying it could become a larger business for the company than coding, while CFO Sarah Friar argued that external estimates of a $300B+ cybersecurity market are still far too low. The company has rolled out GPT-6 Cyber for security research and is expanding its Daybreak trusted-access program, which by September covered thousands of verified defenders and roughly 2,000 approved organizations and workspaces for vulnerability discovery, codebase analysis, and binary reverse engineering. If cybersecurity really becomes a bigger revenue line than coding for OpenAI, it signals that frontier labs see defensive security—not just code generation—as the highest-value enterprise use case for agentic models, which would reshape how security tooling budgets are allocated across enterprises and put pressure on Anthropic and Google in the same market. It also raises the stakes around gated access: who gets powerful offensive-capable models, and under what verification regime, becomes a competitive and policy question rather than a purely technical one. Daybreak is split into access tiers \(Daybreak Blue and Daybreak Red\), with the more capable security models such as GPT-6 Cyber gated behind the Red tier and requiring that tier to be enabled at the API project level; OpenAI has also committed $1 billion in subsidized Daybreak access, training, and partnerships aimed at critical infrastructure, governments, community banks, nonprofits, and open-source projects. The Information notes that OpenAI&\#x27;s competition with Anthropic and Google, and the path to scaled commercialization, remain unclear, and some product specifics circulating in secondary coverage are unverified.

telegram · zaihuapd · Nov 25, 04:51

**Background**: Frontier AI labs have started selling specialized, access-controlled versions of their models for cybersecurity work, because general-purpose chatbots are deliberately restricted from helping with tasks like finding exploitable vulnerabilities. Daybreak is OpenAI&\#x27;s answer to that tension: a vetted-access program that lets approved defenders and enterprises use stronger models for authorized security work such as vulnerability discovery, codebase auditing, and binary reverse engineering—analyzing compiled software to recover its internal logic and find flaws. Vendors frame this as a way to protect critical infrastructure while keeping the same capabilities out of unauthorized hands.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/daybreak/">Daybreak | OpenAI for cybersecurity</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-cyber/">GPT‑6 Cyber: Advancing the frontier of aligned ... - OpenAI</a></li>
<li><a href="https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview">OpenAI Daybreak - Trusted Access for Cyber overview</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#cybersecurity`, `#AI industry strategy`, `#business`, `#AI agents`

---

<a id="item-8"></a>
## [Asian Data Centers Seek U.S. Buyers for Surplus AI Compute After U.S. Closes Export Loophole](https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand) ⭐️ 6.0/10

After Washington tightened an export-control loophole that had let Chinese tech companies obtain Nvidia&\#x27;s most advanced AI chips, data center operators across Asia are now scrambling to resell their surplus AI compute capacity to U.S. buyers. Ronit Jain, CEO of Liquid Compute, said the new rules on exporting advanced AI accelerators to the region are hitting providers that had built capacity expecting to rent it to Chinese customers. The shift shows how export controls are redrawing the global map of AI compute demand: capacity built in Asia for Chinese tenants now needs new customers, potentially pushing prices down for U.S. AI startups and reshaping which regions host training clusters. It also signals that Washington&\#x27;s rules are now reaching beyond physical chip shipments into cross-border compute rental, a business model many Asian operators had counted on. The affected capacity is rented compute rather than hardware sales, so the loosened-then-closed path was remote access to advanced accelerators hosted outside China rather than direct chip shipments. The Bloomberg item gives no figures on how much capacity is stranded or what discounts operators are offering, so the scale of the glut remains unclear.

telegram · zaihuapd · Nov 25, 11:35

**Background**: U.S. export controls bar the sale of the most capable Nvidia data center GPUs to China, but for years Chinese firms could still reach similar performance by renting compute from data centers in third countries or through cloud services — a gap often called the remote-access loophole. Regulators moved to close that gap by targeting cross-border access to advanced AI accelerators, not just physical shipments. Meanwhile, smuggling of chips and high-bandwidth memory through intermediaries such as South Korea has also drawn enforcement attention. Asia&\#x27;s AI data centers are specialized facilities built for power-hungry training and inference workloads, and many were planned around regional demand that has now been constrained.

<details><summary>References</summary>
<ul>
<li><a href="https://asiaaifyi.beehiiv.com/p/u-s-cloud-export-controls-closing-the-remote-access-loophole-for-chinese-ai-firms">U . S . Cloud Export Controls : Closing the Remote Access Loophole ...</a></li>
<li><a href="https://www.cnas.org/publications/cnas-insights/cnas-insights-the-export-control-loophole-fueling-chinas-chip-production">CNAS Insights | The Export Control Loophole Fueling China &#x27;s Chip ...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/ai-chip-smugglers-exploit-trade-control-loophole-to-bring-banned-hbm-from-south-korea-into-china-expensive-memory-chips-packaged-with-cheap-unsanctioned-processors-to-become-legal-exports">AI chip smugglers exploit trade control loophole to... | Tom&#x27;s Hardware</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#export controls`, `#data centers`, `#Nvidia`, `#geopolitics`

---