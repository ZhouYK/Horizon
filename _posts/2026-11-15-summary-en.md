---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15 23:04:10 +0000
lang: en
report: default
---

> From 203 items, 6 important content pieces were selected

---

1. [SpaceX Starship caught by launch tower arms after orbital return for the first time](#item-1) ⭐️ 8.0/10
2. [Meituan open-sources LongCat-2.5, a 1.6T-parameter agent model trained without NVIDIA GPUs](#item-2) ⭐️ 8.0/10
3. [Huawei Cloud launches open-source openPangu-2.1-Pro on its MaaS platform](#item-3) ⭐️ 7.0/10
4. [Tesla Cybercab Requires $299/Month Subscription to Operate](#item-4) ⭐️ 6.0/10
5. [FAA Ground Stop Traced to Router Failure After Copper-to-Fiber Upgrade](#item-5) ⭐️ 6.0/10
6. [US Judge Denies Micron, Samsung, SK Hynix Bid to Dismiss DRAM Price-Fixing Suit](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [SpaceX Starship caught by launch tower arms after orbital return for the first time](https://www.spacex.com/launches/starship-flight-15) ⭐️ 8.0/10

SpaceX says Starship Flight 15 completed a roughly 22.5-hour flight of about 14 orbits around Earth, then returned to its Texas launch site and was caught directly by the launch tower&\#x27;s mechanical arms — the first catch of a Starship vehicle after an orbital-class return. The mission also deployed 26 next-generation Starlink V3 satellites. Catching the upper stage directly on the tower is the step that turns Starship from an expendable test vehicle into a potentially fully and rapidly reusable launch system, which is the core of SpaceX&\#x27;s plan to drive down cost per kilogram to orbit. Progress here also affects Starlink V3 deployment cadence, since large numbers of the heavier, higher-capacity satellites depend on Starship&\#x27;s payload capacity. The milestone was only partial: the Super Heavy booster failed to return to the tower as planned and instead splashed down in the Gulf of Mexico, so the two-stage simultaneous recovery SpaceX ultimately wants was not achieved on this flight. The 26 deployed Starlink V3 satellites are SpaceX&\#x27;s highest-capacity design, with per-satellite downlink design throughput around 1 Tbps — roughly 10 times a V2 Mini — and uplink around 160 Gbps.

telegram · zaihuapd · Nov 14, 23:49

**Background**: Starship is a two-stage system: the Super Heavy booster lifts the Starship upper stage off the pad, and the upper stage itself is the spacecraft that reaches orbit and later reenters. SpaceX&\#x27;s launch tower is equipped with large mechanical arms — nicknamed the &\#x27;chopsticks&\#x27; or &\#x27;Mechazilla&\#x27; — designed to catch returning vehicles instead of letting them land on legs, so they can be inspected and reflown quickly. Earlier flights focused on getting the booster caught by those arms; catching the orbital upper stage is a considerably harder problem because it returns from orbital velocity with a heat shield that must survive reentry intact.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spacex.com/launches">SpaceX - Launches</a></li>
<li><a href="https://tele.ofweek.com/2026-08/ART-8320501-8460-30697797.html">星 链 V 3 ：马斯克要在太空建一张10... - OFweek通信网</a></li>
<li><a href="https://zh-cn.topwar.ru/293078-mask-zamahnulsja-na-100-kratnyj-rost-propusknoj-sposobnosti-starlink-za-2-3-goda.html">马斯克的目标是在 2-3 年内将 Starlink 的吞吐量提高 100 倍</a></li>

</ul>
</details>

**Tags**: `#spacex`, `#starship`, `#reusable-spacecraft`, `#aerospace`, `#news`

---

<a id="item-2"></a>
## [Meituan open-sources LongCat-2.5, a 1.6T-parameter agent model trained without NVIDIA GPUs](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

Meituan&\#x27;s LongCat team released the weights of LongCat-2.5 one week after the official launch, a 1.6-trillion-parameter multimodal agent model licensed under MIT for commercial use. The team claims the model was trained entirely on Chinese Huawei Ascend accelerator cards with no NVIDIA GPUs, and it scores 88.4 on Terminal Bench v2.1 versus 89.1 for Claude Opus 5. It is one of the largest open-weight agent models released under a permissive MIT license, putting frontier-level long-horizon task performance directly in the hands of commercial developers. Just as importantly, the claim of training a trillion-parameter model entirely on Huawei Ascend silicon is a strong signal that China&\#x27;s domestic AI chip stack can support frontier-scale workloads despite US export controls. LongCat-2.5 activates roughly 48 billion of its 1.6 trillion parameters per token, indicating a sparse mixture-of-experts architecture, and it accepts text, image and video input. Its 0.7-point gap to Claude Opus 5 on Terminal Bench v2.1 is narrow but real, and the Ascend-only training claim is self-reported rather than independently verified.

telegram · zaihuapd · Nov 15, 11:08

**Background**: Huawei Ascend is Huawei&\#x27;s own line of AI processors and accelerator cards, sold alongside the Atlas servers and the MindIE/CANN software stack, and is the most prominent non-NVIDIA option for large-scale model training in China. Trillion-parameter models like this one are only practical because of mixture-of-experts designs, which route each token to a small subset of expert sub-networks so that only a fraction of the parameters is computed per token. Terminal Bench is a benchmark that measures whether an AI agent can actually complete real, multi-step command-line tasks, which is why labs use it to compare agentic coding ability.

<details><summary>References</summary>
<ul>
<li><a href="https://e.huawei.com/cn/products/computing/ascend">昇 腾 计算- 华 为 Ascend -AI计算- 华 为 企业业务 | Huawei Enterprise</a></li>
<li><a href="https://www.dian8dian.com/terminalbench-2-yu-harbor-kuang-jia-tong-bu-fa-bu-gou-jian">Terminal - Bench 2.0 与 Harbor 框架同步发布：构建 AI... | 点点资讯</a></li>
<li><a href="https://www.iopencloud.com/ai-models/ai-moe-engineering">MoE 架构：大模型 稀 疏 化的工程革命 - i开源架构</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-source`, `#Huawei Ascend`, `#agent models`, `#AI hardware`

---

<a id="item-3"></a>
## [Huawei Cloud launches open-source openPangu-2.1-Pro on its MaaS platform](https://mp.weixin.qq.com/s/8JfFmscBTDl_mPQMycD8Nw) ⭐️ 7.0/10

On November 15, Huawei Cloud officially added the open-source openPangu-2.1-Pro model to its MaaS \(Model-as-a-Service\) platform, upgrading capabilities in three areas: Agent development, AI coding, and reasoning optimization. The model was tuned on over 100,000 task-specific samples to improve Skills triggering and tool calling, with a focus on HarmonyOS ArkTS development and Ascend operator generation, and it is wired into products including AgentArts, CodeArts, and OfficeAce. Huawei is betting that a domestically built, open-weight model tightly coupled to HarmonyOS and Ascend hardware can win over Chinese developers who need agentic and coding workloads that stay inside the company&\#x27;s own stack. Publishing the weights and offering metered MaaS pricing also positions Pangu as a self-reliant alternative to imported or third-party models in China&\#x27;s crowded LLM market. Pricing is 0.8 yuan per million input tokens, 3.2 yuan per million output tokens, and just 0.016 yuan per million cached input tokens, making prompt caching by far the cheapest path. The announcement is short on benchmarks and does not disclose parameter count, context length, or license terms, and community feedback has been minimal so far.

telegram · zaihuapd · Nov 15, 16:03

**Background**: MaaS, or Model-as-a-Service, is a cloud delivery model in which providers host large models behind an API and bill per token, letting developers skip GPU provisioning and inference engineering; Huawei Cloud offers this through its ModelArts-based MaaS platform. openPangu is the open-source branch of Huawei&\#x27;s Pangu model family, and the preceding openPangu 2.0 Pro was reported to be a Mixture-of-Experts model with roughly 505 billion total and 18 billion active parameters, shipped with weights, inference code, and a technical report. ArkTS is the primary programming language for native HarmonyOS apps, while Ascend is Huawei&\#x27;s in-house AI accelerator line, so optimizing code generation for both ties the model directly to Huawei&\#x27;s own ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/1/022/974.htm">消息称华为云 MaaS 平台 11 月 15 日更新上线 openPangu - 2 . 1 - Pro ...</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E9%B8%BF%E8%92%99%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F">鸿蒙 操作系统 - 维基百科，自由的百科全书</a></li>
<li><a href="https://dsml.kz/ai-radar/2026-07-31-fb758de3883622d5">Huawei открыла 505-миллиардную openPangu 2 .0 Pro … | AI Radar</a></li>

</ul>
</details>

**Tags**: `#Huawei Pangu`, `#open-source LLM`, `#AI agents`, `#code generation`, `#Ascend`

---

<a id="item-4"></a>
## [Tesla Cybercab Requires $299/Month Subscription to Operate](https://www.tesla.com/configurator/api/v4/terms?category=autonomy_subs&amp;amp;locale=en_US&amp;amp;model=cc&amp;amp;saleType=Sale) ⭐️ 6.0/10

Tesla has published autonomy subscription terms for the Cybercab: the $29,990 vehicle requires a $299-per-month subscription to function at all, and Tesla can change the price with one month&\#x27;s notice. The terms also allow suspension or cancellation for non-payment or misuse, with three warnings triggering a one-week autonomous-driving lockout. This is a consequential shift in vehicle-ownership economics: a core driving function is gated behind a recurring fee, so the car becomes inoperable if the subscription lapses. If adopted more broadly, it could reshape consumer expectations and the unit economics of Tesla&\#x27;s robotaxi business. The Cybercab is restricted to designated operating areas, and owners may not put it on ride-hailing, delivery, or rental platforms without authorization. Electrek notes that the Cybercab and the Model Y used for Robotaxi share AI4 hardware and the same autonomous-driving software, but FSD for ordinary owners still requires human supervision.

telegram · zaihuapd · Nov 15, 01:10

**Background**: Tesla is positioning the Cybercab as a purpose-built vehicle for autonomous ride-hailing, and the subscription terms define how owners would pay for that capability. A geofence is a virtual boundary that uses location data to restrict where a vehicle may operate, which explains the designated-area limitation. The mandatory fee differs from Tesla&\#x27;s existing FSD model, where the software is an optional paid feature rather than a prerequisite for the car to move.

<details><summary>References</summary>
<ul>
<li><a href="https://www.angeltranslation.com/glossary/geofencing/">Geofencing 地 理 围 栏 | Angel Translation</a></li>
<li><a href="https://www.tesla.com/">Electric Cars, Solar &amp; Clean Energy | Tesla</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#Cybercab`, `#autonomous-driving`, `#subscription-model`, `#robotaxi`

---

<a id="item-5"></a>
## [FAA Ground Stop Traced to Router Failure After Copper-to-Fiber Upgrade](https://www.theverge.com/transportation/1033898/faa-ground-stop-sean-duffy-faa-copper-wire) ⭐️ 6.0/10

On November 14, U.S. Transportation Secretary Sean Duffy said Friday&\#x27;s nationwide FAA ground stop was triggered by a router failure at a remote facility that had just completed a routine maintenance upgrade from old copper wiring to fiber optics. The newly installed router then flooded other routers with more than a thousand connection requests every 4 to 5 seconds, disrupting radar signals and aircraft communications and forcing thousands of flights to be halted. A single misbehaving router at a remote site was able to paralyze the busiest air traffic control system in the world, exposing how brittle the FAA&\#x27;s aging communications infrastructure remains. The incident is already being used to argue that Congress must fund air traffic control modernization, and it highlights operational risk for any organization that treats network upgrades as routine maintenance. Duffy said the root cause has not been pinned down and could be a hardware fault, a configuration error, or a mistake by contractor L3Harris, and officials have found no sign of a cyberattack. Recovery was slow: cancellations on Saturday topped 6,000 as airlines struggled to restore normal schedules after departures were halted for more than four hours on Friday.

telegram · zaihuapd · Nov 15, 02:10

**Background**: The Federal Aviation Administration, part of the U.S. Department of Transportation, operates air traffic control across U.S. airspace and surrounding international waters, managing the National Airspace System through a mix of radar, communications links and control centers. A nationwide ground stop is a rare, blanket order halting all departing flights, and is normally reserved for severe safety events. The upgrade in question — replacing legacy copper cabling with fiber — is a standard part of telecom modernization, but such changes touch the underlying transport that carries radar and voice traffic. L3Harris Technologies, formed in 2019 from the merger of L3 Technologies and Harris Corporation, is one of the largest U.S. defense contractors and supplies command-and-control, avionics and communications systems to government customers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/L3Harris">L3Harris</a></li>
<li><a href="https://en.m.wikipedia.org/wiki/Federal_Aviation_Administration">Federal Aviation Administration - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#network outage`, `#infrastructure reliability`, `#aviation systems`, `#router failure`, `#systems engineering`

---

<a id="item-6"></a>
## [US Judge Denies Micron, Samsung, SK Hynix Bid to Dismiss DRAM Price-Fixing Suit](https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge) ⭐️ 6.0/10

US District Judge Noël Wise denied motions by Micron, Samsung and SK Hynix to dismiss a DRAM price-fixing class action, ruling that the plaintiffs&\#x27; new evidence made coordinated conduct plausible and likening the three suppliers&\#x27; parallel behavior to &quot;hawks flying in formation.&quot; The defendants must respond by December 7, with a case management conference scheduled for January 2027. The ruling keeps alive an antitrust case against the three companies that together supply nearly all of the world&\#x27;s DRAM, so the litigation carries real potential exposure for memory pricing and allocation decisions. It also sharpens scrutiny of how memory makers manage supply at a time when AI-driven demand has made DRAM a scarce and politically sensitive component. The plaintiffs — 17 individuals and small businesses — allege the three suppliers took four parallel actions within a single year to restrict DRAM supply, pushing prices up by as much as 500%. The decision is only a ruling at the pleading stage, not a finding of liability, and the schedule stretching to a 2027 case management conference signals a long road ahead.

telegram · zaihuapd · Nov 15, 16:39

**Background**: DRAM \(dynamic random-access memory\) is the main working memory in PCs, servers and smartphones, and its global supply is concentrated in an oligopoly of Samsung, SK Hynix and Micron. In US federal civil procedure, a motion to dismiss asks a judge to throw out a case before discovery begins, so denying it means the lawsuit proceeds. Antitrust law generally treats mere parallel conduct — so-called conscious parallelism — as insufficient proof of collusion; plaintiffs must add evidence suggesting an actual agreement, which is what the judge found plausible here.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.csdn.net/qq_59495408/article/details/143904302">一分钟带你了解常 用 的 存 储 器 _ 存 储 器 有哪些-CSDN博客</a></li>
<li><a href="https://www.fapingedu.com/sys-nd/11907.html">法律英语知识之 Motion （ 动 议 ） - 法平教育</a></li>
<li><a href="https://chinaipr.com/wp-content/uploads/2012/10/aba-china-aml-ip-guidelines-comments_finalpackage.pdf">Microsoft Word - ABA China AML IP Guidelines Comments_final.docx</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#antitrust`, `#semiconductor industry`, `#hardware supply chain`, `#price fixing`

---