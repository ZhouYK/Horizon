---
layout: default
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
lang: en
report: default
---

> From 282 items, 10 important content pieces were selected

---

1. [Xiaohongshu Open-Sources dots3-note: 280B MoE with 16B Active Parameters](#item-1) ⭐️ 9.0/10
2. [Apple trains China-specific AI model with Alibaba, eyes first foreign approval](#item-2) ⭐️ 9.0/10
3. [AI-Driven Human Tissue Labs Test 3 Million Samples a Year, Could Replace Animal Testing](#item-3) ⭐️ 8.0/10
4. [Apple Proposes Up to 15% Commission on External App Store Purchases](#item-4) ⭐️ 8.0/10
5. [PostgreSQL Fixes Critical to\_char Vulnerability Allowing Code Execution](#item-5) ⭐️ 8.0/10
6. [Hermes Agent Unveils Bot Mode for Collaborative AI Agents](#item-6) ⭐️ 7.0/10
7. [GLM-5.3 Released, Claims 50% Code Bench Gain, Open Weights in Two Weeks](#item-7) ⭐️ 7.0/10
8. [US Judge Orders Google to Ease Third-Party App Store Installations](#item-8) ⭐️ 7.0/10
9. [Anthropic Revenue Surges Past $11.5 Billion in Q2](#item-9) ⭐️ 6.0/10
10. [CITIC&\#x27;s Trustar Capital Near Deal for Alibaba Gaming Arm Lingxi](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Xiaohongshu Open-Sources dots3-note: 280B MoE with 16B Active Parameters](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 9.0/10

Xiaohongshu&\#x27;s dots lab open-sourced dots3-note preview, the first open-weight model in the dots3 series, featuring 280B total parameters with only 16B active parameters, 512K context length, and text, image, video, and audio understanding. The release also introduces TEMPO, a new reinforcement learning method, alongside two new agent benchmarks: VibeSearchBench and VibeLifeBench. This release is significant because it brings a highly efficient 280B-scale MoE model to the open-weight community, enabling frontier-level performance with far lower inference costs. It also advances agentic AI by introducing a novel reinforcement learning approach and realistic benchmarks, which could accelerate progress in long-horizon, proactive agent research. The model supports 512K context length and multimodal inputs including text, images, video, and audio. TEMPO, the new reinforcement learning method, trains long-horizon agents via self-critique and test-time value estimation, and the model weights are available on Hugging Face along with the two new real-world agent benchmarks.

telegram · zaihuapd · Aug 14, 08:27

**Background**: Mixture of Experts \(MoE\) is an architecture that divides a model into many specialized sub-networks and activates only a subset for each input, which is why a 280B total-parameter model can run with just 16B active parameters. This separation between total and active parameters is key to scaling models while keeping computational costs practical. The new benchmarks, VibeSearchBench and VibeLifeBench, evaluate long-horizon proactive behavior in real-world-like search and everyday-life scenarios, a challenging area for current frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2507.11181v2">Mixture of Experts in Large Language Models - arXiv.org</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://eu.36kr.com/en/p/3938759517896072">Xiaohongshu Open-Sourced Dots 3 -Note: The Same-Series Model ...</a></li>

</ul>
</details>

**Tags**: `#MoE`, `#open-source`, `#reinforcement-learning`, `#multimodal`, `#AI`

---

<a id="item-2"></a>
## [Apple trains China-specific AI model with Alibaba, eyes first foreign approval](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 9.0/10

Apple is training a dedicated large language model for the Chinese market with support from Alibaba, shifting from its previous reliance on third-party models. Apple Intelligence is expected to launch in China via an iOS update in the coming months, and the company has already completed a generative AI service filing with the Cyberspace Administration of China. If approved, Apple would become the first foreign company allowed to offer its own AI model in China, giving it greater control over the AI experience in the world&\#x27;s largest smartphone market. The move strengthens Alibaba&\#x27;s role as a key AI infrastructure partner and could reshape how foreign tech firms navigate China&\#x27;s AI regulations. The model is trained specifically for the Chinese market with Alibaba&\#x27;s support, a departure from Apple&\#x27;s earlier strategy of relying on third-party models. Apple Intelligence will arrive in China through an iOS update in the coming months, and the company&\#x27;s generative AI service was filed with the CAC last month.

telegram · zaihuapd · Aug 14, 14:47

**Background**: Apple Intelligence is Apple&\#x27;s suite of AI features announced in June 2024, combining on-device and server processing and integrated into iOS 18 and later systems. China&\#x27;s CAC requires generative AI services to complete a filing under its interim management rules. By late 2025, the regulator began approving some foreign companies&\#x27; large-model products, including Tesla&\#x27;s xBot and Volvo&\#x27;s smart assistant, but foreign ownership of AI services remains tightly controlled.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://www.cac.gov.cn/2026-05/13/c_1780413225190669.htm">关于发布生成式人工智能服务已备案信息的公告（2026年3月至4月）_中央...</a></li>
<li><a href="https://www.sohu.com/a/954040609_121134737">首批外企大模型产品获批上线，特斯拉、沃尔沃、奔驰等在列_服务_xBot_...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#LLM`

---

<a id="item-3"></a>
## [AI-Driven Human Tissue Labs Test 3 Million Samples a Year, Could Replace Animal Testing](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 8.0/10

Vivodyne has built 12 &\#x27;hive&\#x27; robotic laboratories south of San Francisco that grow human tissues and use AI-designed experiments. These labs can run controlled tests on over 3 million human tissue samples annually, roughly double the total capacity of all U.S. clinical trials. This breakthrough could significantly reduce the need for animal testing and improve drug development success rates, since currently about 90% of clinical trials fail even after passing animal tests. It offers a faster, more human-relevant path for evaluating drug efficacy and safety. The robotic labs are described as closet-sized, with each &\#x27;hive&\#x27; operating autonomously to culture realistic human tissues. Vivodyne claims the system can test 3 million human tissue samples per year, which is roughly twice the capacity of all clinical trials conducted in the U.S.

telegram · zaihuapd · Aug 14, 01:48

**Background**: Traditional drug development relies heavily on animal models, which often fail to accurately predict human responses, contributing to high costs and low success rates. Organ-on-a-chip and microphysiological systems are emerging technologies that use microfluidic devices containing living human tissues to better mimic organ functions. Vivodyne&\#x27;s approach scales up this concept by integrating AI and robotics to screen millions of tissue samples efficiently. Organizations like the Wyss Institute have pioneered organ-chip technologies, but Vivodyne&\#x27;s industrial-scale automation represents a major step forward.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>
<li><a href="https://en.wikipedia.org/wiki/Organ-on-a-chip">Organ-on-a-chip - Wikipedia</a></li>
<li><a href="https://wyss.harvard.edu/technology/human-organs-on-chips/">Human Organs-on-Chips - Wyss Institute Organ-on-chip technology: Opportunities and challenges A guide to the organ-on-a-chip - Nature Reviews Methods Primers Organ-on-a-chip: recent breakthroughs and future prospects Organ-on-a-chip technology replicates decades of human aging ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Biotech`, `#Drug Discovery`, `#Animal Testing`, `#Automation`

---

<a id="item-4"></a>
## [Apple Proposes Up to 15% Commission on External App Store Purchases](https://9to5mac.com/2026/08/13/apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us/) ⭐️ 8.0/10

Apple has submitted a proposal to a US court setting commission rates of up to 15% for purchases made outside the App Store. The rates vary by app type: 15% for standard apps, 10% for video and news partner programs and subscription renewals, and 5% for small business program apps. This is a significant development in the Apple-Epic antitrust case, as it concretely defines how Apple will charge for off-store purchases. The proposal could influence App Store economics and set a precedent for similar disputes globally, directly affecting developers&\#x27; revenue and platform policies. The proposal applies to the US market and follows the Supreme Court&\#x27;s rejection of Apple&\#x27;s request to suspend the lower court&\#x27;s proceedings on fee rates. Epic will have an opportunity to respond, and Apple is expected to file written arguments with the Supreme Court by September 14.

telegram · zaihuapd · Aug 14, 02:33

**Background**: This dispute stems from the long-running legal battle between Apple and Epic Games over App Store policies, particularly the requirement that developers use Apple&\#x27;s in-app payment system. A lower court previously ruled that Apple must allow external payment links, and the commission structure is part of the remedy. The Supreme Court&\#x27;s involvement reflects the broader debate over app store antitrust practices and digital marketplace regulation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2021/08/apple-introduces-the-news-partner-program/">Apple introduces the News Partner Program - Apple</a></li>
<li><a href="https://developer.apple.com/programs/video-partner/">Apple Video Partner Program - Apple Developer... - Apple Developer</a></li>
<li><a href="https://qonversion.io/blog/apple-reduces-app-store-commission-to-15">Apple Small Business Program 2026: How to Get... | Qonversion Blog</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#App Store`, `#Epic Games`, `#Antitrust`, `#Commissions`

---

<a id="item-5"></a>
## [PostgreSQL Fixes Critical to\_char Vulnerability Allowing Code Execution](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL disclosed CVE-2026-14669, a heap buffer overflow in the to\_char\(timestamptz\) function that can lead to arbitrary code execution. Fixes are available in PostgreSQL 18.6, 17.11, 16.15, 15.19, and 14.24; 18-series users must upgrade to 18.6 because 18.5 was skipped due to a regression. This vulnerability is rated CVSS 8.8 and can be exploited by any database user who can set time zones, potentially gaining operating-system-level code execution as the PostgreSQL service account. Given it affects all supported PostgreSQL branches, timely patching is critical for database administrators. Exploitation requires a low-privileged database account that can set timezone settings; it does not work without authentication. The update is a minor release so no dump/restore or pg\_upgrade is required — just replace binaries and restart the server.

telegram · zaihuapd · Aug 14, 14:35

**Background**: to\_char is a PostgreSQL formatting function that converts data types to formatted strings, commonly used for date/time output. POSIX time zone specifications are a standard format for defining time zone offsets and abbreviations, which PostgreSQL accepts in certain contexts. A heap buffer overflow occurs when a program writes more data to a memory region than it can hold, potentially corrupting data or enabling code execution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pgtutorial.com/postgresql-string-functions/postgresql-to_char/">PostgreSQL TO_CHAR Function</a></li>
<li><a href="https://www.postgresql.org/docs/current/functions-formatting.html">PostgreSQL: Documentation: 18: 9.8. Data Type Formatting ...</a></li>
<li><a href="https://www.postgresql.org/docs/19/datetime-posix-timezone-specs.html">PostgreSQL: Documentation: 19: B.5. POSIX Time Zone ...</a></li>

</ul>
</details>

**Tags**: `#PostgreSQL`, `#CVE`, `#security`, `#buffer overflow`, `#vulnerability`

---

<a id="item-6"></a>
## [Hermes Agent Unveils Bot Mode for Collaborative AI Agents](https://x.com/Teknium/status/2088003994904113614) ⭐️ 7.0/10

Nous Research announced Bot Mode for Hermes Agent, a new feature that lets each agent profile run as an independent bot with tasks, descriptions, and avatars, and allows bots to communicate with each other. A one-day public test will start via a GitHub plugin on Hermes Desktop. Bot Mode addresses a growing demand for multi-agent systems, where specialized bots can divide labor and exchange information, potentially enabling more complex automation. It could make Hermes a more attractive platform for users building collaborative AI workflows. The feature is offered as a new mode alongside the existing &\#x27;sessions&\#x27; mode, with each agent profile getting its own bot. The public test lasts one day through a GitHub plugin on Hermes Desktop, and author Teknium is collecting feedback before integrating it into the official desktop app.

telegram · zaihuapd · Aug 14, 04:13

**Background**: Hermes Agent is an open-source AI agent by Nous Research designed for autonomous, multi-step tasks using large language models. Hermes Desktop is the native desktop companion for installing, configuring, and chatting with the agent, offering streaming tool output, profiles, skills, and settings. Bot Mode extends this by allowing multiple distinct agent profiles to run simultaneously and interact, moving beyond single-session interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hermes_Agent">Hermes Agent</a></li>
<li><a href="https://hermes-agent.org/">Hermes Agent — Open-Source AI Agent with Persistent Memory</a></li>
<li><a href="https://hermes-agent.nousresearch.com/docs/user-guide/desktop">Desktop App | Hermes Agent</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Hermes Agent`, `#multi-agent`, `#AI tools`, `#announcement`

---

<a id="item-7"></a>
## [GLM-5.3 Released, Claims 50% Code Bench Gain, Open Weights in Two Weeks](http://z.ai/) ⭐️ 7.0/10

Z.ai released GLM-5.3, a new model built on the GLM-5.2 base with all improvements coming from post-training. The company claims a 50% gain over GLM-5.2 on its internal Z.ai Code Bench and best-in-class open-source results on Terminal Bench 3.0. As an open-weight model from a major Chinese AI lab, GLM-5.3 strengthens the open-source ecosystem&\#x27;s competitiveness against proprietary frontier models. The promised open release in two weeks could make advanced code-generation and agentic capabilities widely available to developers. Z.ai reports that GLM-5.3&\#x27;s vulnerability-exploitation benchmark scores more than doubled versus GLM-5.2, and that it helped security teams identify 2,436 vulnerabilities across 269 projects, including 1,097 medium-to-high severity issues. Access is currently limited to Z.ai&\#x27;s GLM Coding Plan and ZCode agent with a points-based quota system, and these benchmark results are self-reported, not independently verified.

telegram · zaihuapd · Aug 14, 05:27

**Background**: Z.ai, formerly known as Zhipu AI outside China, is a Chinese artificial intelligence company that has released its GLM family of large language models under the open-source MIT license since July 2025. It is considered one of China&\#x27;s &\#x27;AI tiger&\#x27; companies and listed on the Hong Kong Stock Exchange in January 2026. Terminal Bench 3.0 is a benchmark for measuring how well AI agents perform real tasks in containerized environments, used by virtually all frontier labs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.2">GLM 5.2</a></li>
<li><a href="https://www.tbench.ai/contributors/terminal-bench-3">Terminal - Bench</a></li>
<li><a href="https://www.explainx.ai/blog/glm-5-3-launch-cyber-defense-benchmarks-august-2026">GLM-5.3 Launch: Benchmarks, Pricing &amp; Access (Aug 2026 ...</a></li>

</ul>
</details>

**Tags**: `#GLM`, `#LLM`, `#code generation`, `#AI`, `#open source`

---

<a id="item-8"></a>
## [US Judge Orders Google to Ease Third-Party App Store Installations](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 7.0/10

US District Judge James Donato ordered Google to remove extra warning screens and steps in the Play Store that hinder installation of competing Android app stores. Google must make the changes within one week, following the Epic v. Google antitrust ruling. This ruling could reshape Android app distribution by lowering the friction that competing stores such as the Epic Games Store face when users try to install them. It gives app store rivals and developers a more direct path to Android users. The order specifically targets the Play Store&\#x27;s &\#x27;friction,&\#x27; such as requiring users to review further warnings before the Install button appears for third-party stores. Judge Donato said these multi-step prompts were deliberately designed to scare off ordinary users, and Google must make installing a rival store as direct as installing a typical Android app.

telegram · zaihuapd · Aug 14, 09:55

**Background**: Android allows users to install apps outside the official Google Play Store, a process called sideloading that uses APK files and the Android package installer. Google Play Protect scans devices and apps for harmful behavior, and until now the Play Store could present warnings during sideloading when installing unverified apps. Epic Games sued Google over its app distribution practices, and a jury previously found that Google illegally monopolized Android app distribution. This court order comes from that antitrust case as part of the remedy phase.

<details><summary>References</summary>
<ul>
<li><a href="https://www.androidauthority.com/google-android-sideloading-unverified-apps-new-rules-3650343/">Android&#x27;s new sideloading rules are here, and they come with ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Play_Protect">Google Play Protect</a></li>
<li><a href="https://developer.android.com/reference/android/content/pm/PackageInstaller">PackageInstaller | API reference | Android Developers</a></li>

</ul>
</details>

**Tags**: `#antitrust`, `#Google`, `#Android`, `#app stores`, `#regulation`

---

<a id="item-9"></a>
## [Anthropic Revenue Surges Past $11.5 Billion in Q2](https://www.reddit.com/r/finance/comments/1vok26d/anthropic_revenue_surges_to_over_115_billion_in/) ⭐️ 6.0/10

Anthropic&\#x27;s revenue surged past $11.5 billion in the second quarter, signaling strong commercial growth for the AI firm. The figure indicates a notable acceleration in demand for its AI products. This milestone highlights Anthropic&\#x27;s rapid ascent as a major commercial player in the AI industry. It also suggests that enterprise adoption of AI assistants and models continues to expand, intensifying competition among frontier AI companies. The figure comes from a Reddit post in r/finance rather than an official earnings announcement, so the exact reporting period and methodology are not independently verified. The one-line summary describes the result as a business milestone but notes that it lacks technical depth or novel engineering insights.

reddit · r/finance · /u/FrankLucasV2 · Aug 14, 21:26

**Background**: Anthropic is an artificial intelligence company known for developing the Claude family of large language models. Revenue milestones like this are closely watched because frontier AI development requires enormous spending on compute and research, making commercial revenue a key indicator of a company&\#x27;s long-term sustainability. This news surfaced through a community discussion on Reddit rather than an official corporate release.

**Tags**: `#Anthropic`, `#AI business`, `#revenue`, `#finance`

---

<a id="item-10"></a>
## [CITIC&\#x27;s Trustar Capital Near Deal for Alibaba Gaming Arm Lingxi](https://www.bloomberg.com/news/articles/2026-08-14/trustar-is-said-to-near-1-5-billion-deal-for-alibaba-gaming-arm) ⭐️ 6.0/10

Trustar Capital, the private equity arm of CITIC Group, is close to acquiring Alibaba&\#x27;s gaming unit Lingxi Interactive Entertainment at a valuation exceeding $1.5 billion, having outbid several gaming companies. Negotiations are still ongoing and no final decision has been made. The deal highlights Alibaba&\#x27;s continued divestment of non-core assets under CEO Eddie Wu to sharpen focus on AI and cloud computing. It also underscores private equity interest in gaming assets amid broader industry consolidation. Lingxi&\#x27;s flagship title is the MMO strategy game &\#x27;Three Kingdoms Tactics&\#x27; \(三国志·战略版\), developed with Japan&\#x27;s Koei Tecmo. Trustar Capital beat several gaming companies in the bidding, but talks are still in progress.

telegram · zaihuapd · Aug 14, 10:24

**Background**: Trustar Capital is the rebranded name of CITIC Capital, a private equity platform under CITIC Group; it adopted the new name in March 2021. Lingxi Interactive Entertainment, formerly Jianyue Technology, was fully acquired by Alibaba in 2017 and operates a &\#x27;research and operation integrated&\#x27; model with platforms such as 9game and Trading Cat. Alibaba has been divesting non-core businesses to focus more on AI and cloud.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/%E4%B8%AD%E4%BF%A1%E8%B5%84%E6%9C%AC">中 信 资 本 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/%E7%81%B5%E7%8A%80%E4%BA%92%E5%A8%B1/68094905">灵犀互娱 - 百度百科</a></li>
<li><a href="https://www.lingxigames.com/">灵犀互娱官网</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#Acquisition`, `#Gaming`, `#Private Equity`, `#Tech Industry`

---