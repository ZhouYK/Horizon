---
layout: default
title: "Horizon Summary: 2026-08-07 (EN)"
date: 2026-08-07
lang: en
report: default
---

> From 278 items, 8 important content pieces were selected

---

1. [OpenAI Warns Upcoming Astra Model May Hit &\#x27;Critical&\#x27; Cyber Capability Threshold](#item-1) ⭐️ 9.0/10
2. [Critical OAuth flaw in sub2api lets attackers take over accounts using only email](#item-2) ⭐️ 8.0/10
3. [Anthropic Updates Fable 5 Biological Safety Guardrails, Cutting False Positives by 85%](#item-3) ⭐️ 7.0/10
4. [SEC Approves Nasdaq 23-Hour Trading, Launching December 6, 2026](#item-4) ⭐️ 7.0/10
5. [US Reviews Chinese AI Firms&\#x27; Offshore Access to Nvidia Chips](#item-5) ⭐️ 7.0/10
6. [SK Hynix Confirms 375-Layer V10 NAND with Wafer Bonding for AI](#item-6) ⭐️ 7.0/10
7. [AWS cracks down on CPU waste as agentic AI hikes demand](#item-7) ⭐️ 7.0/10
8. [OpenAI Publishes First Country-Level ChatGPT Usage Data](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Warns Upcoming Astra Model May Hit &\#x27;Critical&\#x27; Cyber Capability Threshold](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) ⭐️ 9.0/10

On August 7, 2026, OpenAI disclosed that its upcoming Astra model showed enough progress in agentic coding and cybersecurity in internal evaluations that it may reach the &\#x27;Critical&\#x27; cyber capability threshold under its Preparedness Framework. Previous frontier models like GPT-5.6-Sol were only rated &\#x27;High,&\#x27; and the company has expanded safety testing, which could delay Astra&\#x27;s release. This marks the first time a frontier model may cross the most severe cybersecurity risk threshold, with major implications for release decisions, national security policy, and AI governance. It could also push the entire industry to adopt stricter safety evaluation and deployment standards for the next generation of models. Under OpenAI&\#x27;s framework, reaching the Critical threshold means the model could autonomously discover and exploit zero-day vulnerabilities in hardened real-world critical systems, or devise and execute end-to-end novel cyberattacks from high-level objectives. In response, OpenAI has paused certain internal activities involving Astra that do not yet meet enhanced safety requirements, and will conduct third-party testing with government agencies and AI safety organizations in isolated environments with encryption and monitoring.

telegram · zaihuapd · Aug 7, 16:44

**Background**: OpenAI&\#x27;s Preparedness Framework is a structured process for tracking, evaluating, and mitigating catastrophic risks posed by frontier AI, with cybersecurity as one of its core tracked categories. Agentic coding refers to AI agents autonomously performing software development tasks such as code generation, debugging, and testing. Every prior frontier model, including GPT-5.6-Sol, was rated at the &\#x27;High&\#x27; cyber threshold rather than &\#x27;Critical,&\#x27; which is the highest severity level in the framework.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/">Responding to the next frontier of critical cyber capabilities</a></li>
<li><a href="https://openai.com/index/updating-our-preparedness-framework/">Our updated Preparedness Framework | OpenAI</a></li>
<li><a href="https://www.unite.ai/openai-says-upcoming-astra-model-may-cross-critical-cybersecurity-threshold/">OpenAI Says Upcoming Astra Model May Cross Critical ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#cybersecurity`, `#frontier models`, `#release delay`

---

<a id="item-2"></a>
## [Critical OAuth flaw in sub2api lets attackers take over accounts using only email](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 8.0/10

sub2api v0.1.171 and earlier contains a CVSS 8.8 OAuth account-takeover vulnerability. An attacker who knows the victim&\#x27;s email can bind their own OAuth identity to the victim&\#x27;s account without a password, code, or user interaction, gaining full control of API keys, billing balance, and subscription quota. This is a high-severity flaw in a widely used AI API gateway: exploitation is trivial and requires no user interaction, so any user whose email is known is potentially at risk. It underscores how OAuth binding logic must validate existing users before linking a new identity. The vulnerability lies in the pending-session flow&\#x27;s existingUser branch, which skips password and verification-code checks and allows the target user ID to be set to the victim. After the attack, every subsequent OAuth login by the attacker resolves to the victim&\#x27;s account.

telegram · zaihuapd · Aug 7, 14:59

**Background**: sub2api is an open-source AI API proxy that unifies subscriptions for Claude, OpenAI, Gemini, and Antigravity, letting users access upstream AI services through platform-generated API keys while the platform handles authentication, billing, load balancing, and request forwarding. OAuth account takeover is a known class of web security issue in which flaws in the OAuth authorization flow let an attacker bind their own identity to a victim&\#x27;s account. Here, the missing checks in the existing-user branch of the pending-session flow make that binding possible with only an email address.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Wei-Shaw/sub2api">GitHub - Wei-Shaw/sub2api: Sub2API 一站式开源中转服务，让 Claude...</a></li>
<li><a href="https://grokipedia.com/page/Sub2API">Sub2API</a></li>
<li><a href="https://hacktricks.wiki/en/pentesting-web/oauth-to-account-takeover.html">OAuth to Account takeover - HackTricks</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#OAuth`, `#account takeover`, `#sub2api`

---

<a id="item-3"></a>
## [Anthropic Updates Fable 5 Biological Safety Guardrails, Cutting False Positives by 85%](http://claude.ai/) ⭐️ 7.0/10

On August 7, Anthropic announced an update to Fable 5&\#x27;s biological safety guardrails that reduces system downgrades for biology-related queries by about 85%. Overall fallbacks on Claude.ai are projected to drop by roughly 67%. This significantly improves user experience for everyday health and education queries that were previously over-blocked, while preserving safeguards for high-risk dual-use research. It demonstrates a more nuanced approach to AI safety that balances usability with risk mitigation. The update was achieved by rewriting the safety classifier&\#x27;s rules and training data. Requests involving virology, toxicology, molecular design, and drug development still fall back to Opus 5 to address dual-use risks.

telegram · zaihuapd · Aug 7, 06:05

**Background**: Safety classifiers are computational models that screen inputs and outputs of AI systems to detect and mitigate harmful content. Many AI systems use a downgrade fallback mechanism that routes sensitive requests to a smaller, less capable model as a precaution. In the biosecurity context, dual-use risk refers to the possibility that legitimate research tools or knowledge could be misused to create biological threats.

<details><summary>References</summary>
<ul>
<li><a href="https://forum.effectivealtruism.org/posts/EReJtGRtZAQXnQQoK/why-dual-use-risk-bio-matters-now-in-llms-a-simple-guide-and">Why Dual - Use Risk Bio Matters Now in LLMs. A Simple... — EA Forum</a></li>
<li><a href="https://futureagi.com/blog/what-is-llm-fallback-strategy-2026/">What Is an LLM Fallback Strategy? A 2026 Field Guide</a></li>
<li><a href="https://arxiv.org/abs/2311.00172">Robust Safety Classifier for Large Language Models ... A New Approach to AI Safety: Layer Enhanced Classification ... Safety Classifier Explained: Definition, Examples &amp; Use Cases ... Benchmarking guardrail models for safety, refusal, and latency</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#Anthropic`, `#Claude`, `#model update`, `#safety guardrails`

---

<a id="item-4"></a>
## [SEC Approves Nasdaq 23-Hour Trading, Launching December 6, 2026](https://finance.sina.com.cn/stock/bxjj/2026-08-07/doc-inimnkup0012339.shtml) ⭐️ 7.0/10

The U.S. Securities and Exchange Commission \(SEC\) has approved Nasdaq&\#x27;s 23-hour, 5-day trading schedule, set to go live on December 6, 2026. The market will close for only one hour each day, from 20:00 to 21:00 ET, for system clearing and data processing. Extending trading to 23 hours fundamentally reshapes U.S. equity market structure, affecting exchanges, brokerages, and investors around the world. It also intensifies competitive pressure on other venues and raises new concerns about liquidity and investor protection during overnight sessions. Nasdaq will suspend trading only between 20:00 and 21:00 ET for clearing and data processing. NYSE Arca has already received accelerated SEC approval for 22-hour trading, and Cboe has proposed a near-24x5 schedule, with all targeting December 2026. The SEC will hold a roundtable on September 17 to discuss investor protection issues.

telegram · zaihuapd · Aug 7, 10:03

**Background**: Currently, U.S. stock exchanges operate roughly 6.5 hours per day on weekdays, but retail investors already trade overnight through alternative trading systems \(ATS\) such as Blue Ocean ATS, and platforms like Robinhood and Charles Schwab offer extended-hours services. Because overnight sessions have thin liquidity and wide spreads, regulators are scrutinizing the risks. The move toward near-24-hour trading mirrors the structure of crypto and forex markets, which operate around the clock.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Alternative_trading_system">Alternative trading system</a></li>
<li><a href="https://blueocean-tech.io/blue-ocean-ats/">Blue Ocean ATS – Blue Ocean Technologies LLC</a></li>
<li><a href="https://www.tradinghours.com/markets/nasdaq">NASDAQ Market Hours &amp; Holidays 2026 - 2028 - TradingHours.com</a></li>

</ul>
</details>

**Tags**: `#finance`, `#trading`, `#regulation`, `#nasdaq`, `#sec`

---

<a id="item-5"></a>
## [US Reviews Chinese AI Firms&\#x27; Offshore Access to Nvidia Chips](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 7.0/10

The US Commerce Department&\#x27;s Bureau of Industry and Security \(BIS\) is investigating how Chinese AI companies obtain Nvidia chips offshore, including by remotely renting computing capacity in other countries. The review follows the release of the Kimi K3 model and a White House official&\#x27;s allegation that it was built using illegally acquired Nvidia chips accessed remotely via Thailand. This move could lead to new export-control rules that restrict not only physical chip shipments but also cloud-based access to advanced AI hardware. It would affect Chinese AI developers, global cloud providers, and Nvidia&\#x27;s offshore business, and may set a precedent for how AI compute is regulated internationally. BIS is reportedly compiling two country lists: one of black-market locations suspected of smuggling restricted chips into China, and another of countries where Chinese firms remotely rent chips. The legal basis for restricting remote computing access is uncertain, but the US House has passed a bipartisan bill to grant that authority, which is expected to face opposition from Nvidia and other tech companies.

telegram · zaihuapd · Aug 7, 11:18

**Background**: The Bureau of Industry and Security \(BIS\) enforces US export controls through the Export Administration Regulations \(EAR\), which restrict the export and re-export of advanced computing items to certain countries, including China. Remote cloud computing services allow customers to use high-end AI chips located abroad without physically importing them, creating a potential loophole in chip export controls. The Kimi K3 model, released by Moonshot AI, is a 2.8T-parameter model and the world&\#x27;s first open 3T-class model, which has drawn attention to China&\#x27;s AI progress despite US restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bis.gov/">Homepage | Bureau of Industry and Security</a></li>
<li><a href="https://www.trade.gov/us-export-controls">U.S. Export Controls - International Trade Administration Top Stories Export Administration Regulations (EAR) | Bureau of Industry ... Guidance on end-user and end-use controls and U.S. person ... U.S. Export Regulations - International Trade Administration The Ultimate Guide to the Bureau of Industry and Security (BIS)</a></li>

</ul>
</details>

**Tags**: `#export-controls`, `#AI`, `#Nvidia`, `#China`, `#policy`

---

<a id="item-6"></a>
## [SK Hynix Confirms 375-Layer V10 NAND with Wafer Bonding for AI](https://www.gelonghui.com/live/2599953) ⭐️ 7.0/10

SK Hynix confirmed at FMS 2026 that its next-generation V10 NAND flash will feature 375-layer stacking, succeeding its 321-layer V9 4D NAND. This is also the company&\#x27;s first NAND product to adopt wafer bonding technology. This announcement marks a significant advance in NAND density and energy efficiency, offering 2.5 times better performance per watt than the previous generation, which is crucial for AI infrastructure that must balance power consumption and performance. The move could pressure rivals Samsung and Micron to accelerate their own high-layer-count and wafer-bonding roadmaps. The V10 uses a 375-layer stack and is specifically optimized for AI infrastructure workloads. SK Hynix&\#x27;s announcement does not disclose exact storage densities or mass-production timelines.

telegram · zaihuapd · Aug 7, 12:19

**Background**: NAND flash stores data in vertical 3D stacks, and increasing the number of layers is the main way to raise capacity and lower cost per bit. Wafer bonding is a technique that joins two processed wafers directly or via intermediate layers, allowing different parts of a memory cell to be manufactured separately and then combined; SK Hynix&\#x27;s &\#x27;4D NAND&\#x27; branding emphasizes such innovations built on conventional 3D NAND architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dymek.cn/case-item-138.html">晶 圆 键 合 是 什 么 - 键 合 原理- 键 合 应用-岱美仪器</a></li>
<li><a href="https://www.elecfans.com/d/6228534.html">晶 圆 键 合 技 术 的类型有哪些-电子发烧友网</a></li>

</ul>
</details>

**Tags**: `#NAND`, `#SK Hynix`, `#semiconductor`, `#wafer bonding`, `#AI infrastructure`

---

<a id="item-7"></a>
## [AWS cracks down on CPU waste as agentic AI hikes demand](https://www.tomshardware.com/pc-components/cpus/amazon-cracks-down-on-cpu-waste-among-engineers-as-agentic-ai-crunch-intensifies-cpu-demand-makes-low-utilization-ec2-instances-a-hot-commodity) ⭐️ 7.0/10

Since May, Amazon AWS has required engineers to reduce CPU waste to preserve capacity for customers, causing internal EC2 instance request wait times to stretch from hours to multiple days. This is a direct operational response to rising CPU demand from agentic AI workloads. Agentic AI workloads rely heavily on CPU-based tool calls and GPU orchestration, shifting data center GPU-to-CPU ratios from 8:1 or 4:1 toward 1:1. This raises the strategic importance of CPU supply for hyperscalers and affects cloud capacity planning, infrastructure costs, and hardware investment decisions. Some engineers report having never waited this long for EC2 instances in years of work, highlighting the severity of the internal backlog. AMD and Nvidia have both expanded their data center CPU lineups to capture this emerging demand.

telegram · zaihuapd · Aug 7, 16:31

**Background**: Agentic AI differs from traditional reactive AI models: it operates autonomously, sets goals, reasons about its environment, and proactively performs tasks, often via tool calls. These workflows generate substantial general-purpose CPU load alongside GPU accelerator use, so data centers now need far more CPUs per GPU. Historically, AI data centers were built with a high GPU-to-CPU ratio \(e.g., 8:1 or 4:1\), but agentic scenarios are pushing the ratio toward 1:1.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/demand-for-data-center-cpus-has-surged-and-ai-agents-are-responsible-why-the-cpu-to-gpu-ratio-is-more-important-than-ever-for-hyperscalers">Demand for data center CPUs has surged, and AI agents are ...</a></li>
<li><a href="https://insights.trendforce.com/p/agentic-ai-cpu-gpu">The Great Rebalance: How Agentic AI Is Reshaping the CPU:GPU ...</a></li>
<li><a href="https://www.hostinger.com/ph/tutorials/what-is-agentic-ai">What is agentic AI ?</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#AI infrastructure`, `#CPU`, `#agentic AI`, `#cloud computing`

---

<a id="item-8"></a>
## [OpenAI Publishes First Country-Level ChatGPT Usage Data](https://openai.com/index/how-the-world-is-putting-chatgpt-to-work/) ⭐️ 6.0/10

OpenAI released its first country-level ChatGPT usage dataset, revealing that users now leverage the AI for work-related tasks more than twice as often as for personal use. Multimedia interactions have become the fastest-growing use case, reaching 7.8% of global messages since ChatGPT Images 2.0 launched in April. This data signals that AI is transitioning from a conversational novelty to a mainstream production tool, with meaningful implications for workforce productivity and business workflows. It also shows that adoption gaps between early and emerging markets are narrowing, pointing to a more globally distributed AI economy. In France and Czechia, the message share from users aged 35 and older grew by more than 10 percentage points over the past year. In countries like Brazil and Colombia, over one-tenth of ChatGPT messages now involve multimedia processing, reflecting rapid adoption of image-generation features.

telegram · zaihuapd · Aug 7, 08:43

**Background**: ChatGPT is OpenAI&\#x27;s conversational AI assistant that can answer questions, write code, analyze data, and generate images. In April 2025, OpenAI introduced ChatGPT Images 2.0, a state-of-the-art image generation model with improved text rendering and multilingual support. This country-level usage report is part of OpenAI&\#x27;s broader effort to show how AI tools are being adopted across different regions and demographics.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-0/">Introducing ChatGPT Images 2 . 0 | OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#AI adoption`, `#Usage trends`, `#Industry data`

---