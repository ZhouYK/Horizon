---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22 23:04:07 +0000
lang: en
report: default
---

> From 192 items, 13 important content pieces were selected

---

1. [Alibaba Unveils Zhenwu V900, Claiming Strongest Domestic AI Chip With 3x Compute](#item-1) ⭐️ 8.0/10
2. [Cloudflare Python Workers reaches general availability](#item-2) ⭐️ 8.0/10
3. [DeepSeek Releases DSec Sandbox Report: 3M Sandboxes Served Daily for Agent Training](#item-3) ⭐️ 8.0/10
4. [Douyin Launches Wealth Management Section With Fund Purchases and Brokerage Accounts](#item-4) ⭐️ 7.0/10
5. [OpenAI Forms Math and AI Advisory Group at Institute for Advanced Study](#item-5) ⭐️ 7.0/10
6. [Mimo CLI Reportedly Contains Undisclosed Telemetry and Code Collection Function](#item-6) ⭐️ 7.0/10
7. [DeepSeek to brief UN Security Council on AI risks](#item-7) ⭐️ 7.0/10
8. [iOS 27.2 Beta 2 Adds China-Only Motion Data Restriction Setting](#item-8) ⭐️ 7.0/10
9. [China Probes DeepSeek and Moonshot Over Alleged Data Leaks](#item-9) ⭐️ 7.0/10
10. [Anthropic ships Claude Opus 5.5 with 40% lower cost](#item-10) ⭐️ 7.0/10
11. [All five major Chinese smartphone brands now integrated into China&\#x27;s earthquake early warning network](#item-11) ⭐️ 6.0/10
12. [US Proposes AI Incident Reporting Channel With China](#item-12) ⭐️ 6.0/10
13. [OpenAI to Let Outside Groups Evaluate AI Models Earlier](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Alibaba Unveils Zhenwu V900, Claiming Strongest Domestic AI Chip With 3x Compute](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 8.0/10

At the 2026 Apsara \(Yunqi\) Conference in Hangzhou on September 22, Alibaba&\#x27;s chip unit T-Head \(Pingtouge\) unveiled the Zhenwu V900 AI chip, which it claims delivers 3x the compute of the previous-generation Zhenwu M890 and can scale to clusters of 500,000 cards. CEO Wu Yongming also said the self-developed M890 supernode already supports inference for 2-trillion-parameter models and will be deployed at scale on Alibaba Cloud this quarter, while the Qwen team plans new models in the 5T-10T parameter range and targets more than 20GW of global data center capacity by 2032. The announcement positions Alibaba as a full-stack AI player owning models, chips and cloud, a combination that matters as Chinese cloud providers seek to reduce dependence on Nvidia accelerators under export restrictions. If the claimed 3x compute improvement and 500,000-card cluster ceiling hold up, it would strengthen the domestic AI accelerator ecosystem and give Chinese labs a more viable path to training ever-larger frontier models. The performance figures are vendor claims with no independent benchmarking disclosed, and details such as process node, memory bandwidth, interconnect technology and power consumption were not specified. The 500,000-card figure describes a maximum cluster scale rather than a demonstrated deployment, and Alibaba did not share timeline or pricing for the Zhenwu V900; the 20GW data center target for 2032 is also an extremely ambitious capacity goal.

telegram · zaihuapd · Sep 22, 03:30

**Background**: T-Head \(Pingtouge\) is Alibaba&\#x27;s wholly owned semiconductor arm, formed in 2018 when the company acquired C-SKY Microsystems, then China&\#x27;s only independently developed embedded CPU IP core vendor, and merged it with the chip team from its DAMO Academy. The term &\#x27;supernode&\#x27; used in the announcement refers to a design that uses near-non-blocking, high-bandwidth interconnect and unified memory addressing to weave hundreds or thousands of AI processors into one logically unified, high-density compute unit. Alibaba&\#x27;s multi-trillion-parameter Qwen plan and the chip roadmap are therefore closely linked, since model scale is limited by how many accelerators can be trained and served together.

<details><summary>References</summary>
<ul>
<li><a href="https://cj.sina.com.cn/articles/view/6192937794/17120bb4202002ngou?froms=ggmp">cj.sina.com.cn/articles/view/6192937794/17120bb4202002ngou?froms...</a></li>
<li><a href="https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E3%80%8A%E8%B6%85%E8%8A%82%E7%82%B9%E5%8F%91%E5%B1%95%E6%8A%A5%E5%91%8A%E3%80%8B.pdf">CONTENTS</a></li>
<li><a href="https://t.cj.sina.com.cn/articles/view/6336727143/179b2c86700101deye?finpagefr=p_103">从炫技到务实， 超 节 点 的祛魅时刻__财经头条__新浪财经</a></li>

</ul>
</details>

**Tags**: `#AI芯片`, `#阿里`, `#云栖大会`, `#AI基础设施`, `#国产芯片`

---

<a id="item-2"></a>
## [Cloudflare Python Workers reaches general availability](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

On September 21, Cloudflare announced that Python Workers is now generally available \(GA\), making Python a first-class supported language on its developer platform alongside JavaScript/TypeScript. The release adds native support for frameworks such as FastAPI, Django and Flask, plus new low-level networking capabilities that let developers run PostgreSQL databases and AI libraries like LangChain directly inside a Worker. Python is the dominant language for AI, data and backend scripting, so first-class support removes a major adoption barrier for teams that did not want to rewrite code in JavaScript to use the edge. It also lets Cloudflare compete directly with other serverless and edge platforms for AI-oriented workloads, tying Python code closely to Workers AI, R2 and D1 services. The feature was first launched two years ago and has now been stabilized, with the key technical advance being low-level socket/networking support that enables direct database drivers and AI libraries inside the Workers runtime. The announcement does not detail pricing or per-plan limits for Python Workers, so existing Workers plan quotas are the relevant constraint.

telegram · zaihuapd · Sep 22, 04:00

**Background**: Cloudflare Workers is a serverless platform that runs code across Cloudflare&\#x27;s global edge network instead of in a single region, which reduces latency but traditionally limited runtimes to JavaScript/TypeScript and WASM. Workers AI provides one-API-call inference on Cloudflare&\#x27;s GPUs, R2 is an S3-compatible object storage service with no egress fees, and D1 is a distributed SQL database built on SQLite and integrated into the Workers ecosystem. Python Workers aims to bring the same ecosystem to Python developers without container cold starts.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Cloudflare_Workers">Cloudflare Workers</a></li>
<li><a href="https://www.cloudflare.com/products/workers-ai/">Cloudflare Workers AI - Edge AI Inference Platform</a></li>
<li><a href="https://juejin.cn/post/7496528481843691555">秒杀传统 数 据 库 ！ Cloudflare D 1 + Drizzle...</a></li>

</ul>
</details>

**Tags**: `#Cloudflare Workers`, `#Python`, `#Serverless`, `#Edge Computing`, `#AI`

---

<a id="item-3"></a>
## [DeepSeek Releases DSec Sandbox Report: 3M Sandboxes Served Daily for Agent Training](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI and Tsinghua University jointly published a technical report on DeepSeek Elastic Compute \(DSec\), a sandbox platform that serves roughly 3 million sandbox instances per day to support large-scale agent training and evaluation. The platform exposes four execution backends through a unified SDK — FnCall, containers, Firecracker microVMs, and full VMs — and is designed to work tightly with reinforcement learning frameworks. Agentic reinforcement learning is bottlenecked less by GPU compute than by the ability to spin up millions of isolated, stateful execution environments on demand, so a proven design for doing that at this scale is directly useful to any team building coding, computer-use, or security agents. By decoupling stateful rollout execution from preemptible GPU training, DSec offers a template for keeping expensive accelerators saturated while sandboxes churn in the background. A single production unit spans about 160 nodes and handles peaks above 380,000 concurrent sandboxes with a creation rate exceeding 5,000 per second, packing up to 3,200 containers or 800 microVMs onto one node. Loading EROFS images on demand from the 3FS distributed file system instead of doing full Docker pulls reportedly cuts task completion time by 1.7x, reduces disk writes by 57%, and lowers peak memory usage by about 40%.

telegram · zaihuapd · Sep 22, 04:45

**Background**: Sandboxes are isolated execution environments that let AI agents run code, operate a desktop, or attempt security exploits without endangering the host system — a prerequisite for training agents through trial and error. Firecracker is AWS&\#x27;s open-source lightweight virtualization technology that provides hardware-level isolation with very low overhead, while EROFS is a read-only Linux file system originally developed by Huawei that is optimized for compact, high-performance images. 3FS is DeepSeek&\#x27;s own open-source distributed file system for AI workloads, released during its Open Source Week in early 2025, which DSec uses to stream those images to nodes on demand.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker - microvm / firecracker : Secure and fast microVMs...</a></li>
<li><a href="https://en.wikipedia.org/wiki/EROFS">EROFS - Wikipedia</a></li>
<li><a href="https://www.caveman.press/article/deepseek-3fs-distributed-file-system-ai-workloads">DeepSeek Unleashes 3 FS : A Groundbreaking Distributed File ...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI Agents`, `#Sandbox Infrastructure`, `#Reinforcement Learning`, `#ML Systems`

---

<a id="item-4"></a>
## [Douyin Launches Wealth Management Section With Fund Purchases and Brokerage Accounts](https://finance.jrj.com.cn/2026/09/21194458502389.shtml) ⭐️ 7.0/10

Douyin has opened fund-purchasing functionality inside its app: users go to &quot;My Wallet&quot; and find a fund entry at the bottom of the wealth-management page, which offers five categories — demand wealth management, bank certificates of deposit, steady wealth management, dividend funds, and a return-seeking section — mapping to money market funds, bond funds, fixed-income-plus \(固收+\) products, active equity funds, and QDII public mutual funds. The section also supports opening securities brokerage accounts, arriving just as China&\#x27;s new rules on online marketing of financial products are about to take effect. A platform with massive traffic like Douyin moving from advertising financial products to actually hosting fund sales and brokerage account opening marks a significant step for large internet firms into financial distribution, potentially reshaping how Chinese retail investors are reached. It lands right before the new online-marketing rules take effect on September 30, 2026, which will draw a hard line between licensed institutions and unlicensed influencers, so the competitive landscape for fund sales and brokerage client acquisition could shift sharply. The 《金融产品网络营销管理办法》 was jointly issued on April 21, 2026 by the People&\#x27;s Bank of China and seven other departments and takes effect on September 30, 2026; it requires that organizations or individuals other than financial institutions and third-party platforms — explicitly including internet influencers and finance bloggers — must not conduct or disguisedly conduct online marketing of financial products. Douyin&\#x27;s ability to offer these functions therefore depends on operating as a compliant, licensed third-party platform rather than as an unlicensed promoter.

telegram · zaihuapd · Sep 22, 01:56

**Background**: Chinese public mutual funds \(公募基金\) are commonly grouped by risk and asset type: money market funds for daily liquidity, bond funds, &quot;fixed-income plus&quot; \(固收+\) funds that hold mostly bonds but add roughly 10%–30% equity exposure for extra return, active equity funds, and QDII funds, which invest in overseas markets under the Qualified Domestic Institutional Investor scheme. The new 《金融产品网络营销管理办法》 \(Measures for the Administration of Online Marketing of Financial Products\) expands regulation to cover both financial institutions&\#x27; own online marketing and third-party internet platforms that provide such marketing services on their behalf, while banning &quot;unlicensed&quot; institutions and individuals from doing so. That regulatory backdrop is what makes Douyin&\#x27;s timing — launching the wealth-management section weeks before the rules take effect — notable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.21jingji.com/article/20220816/herald/0dcb134eb927f7059894a238c15c134d.html">万亿“ 固 收 +” 基 金 迎监管窗口指导：明确权益投资比例30%的上限 - 21...</a></li>
<li><a href="https://www.gffunds.com.cn/jjkt/tzjhl/202401/t20240110_389472.shtml">QDII 基 金 悄悄火了？ 3个热门问题，看懂这类产品-投资进化论-广发 基 金</a></li>
<li><a href="https://wlaq.gmw.cn/2026-05/07/content_38751671.htm">严 管 金 融 产 品 网 络 营 销 守好百姓“钱袋子” _光明 网</a></li>

</ul>
</details>

**Tags**: `#抖音`, `#理财`, `#基金`, `#金融科技`, `#监管`

---

<a id="item-5"></a>
## [OpenAI Forms Math and AI Advisory Group at Institute for Advanced Study](https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/) ⭐️ 7.0/10

On September 21, OpenAI announced the creation of an independent Mathematics and AI advisory group based at the Institute for Advanced Study in Princeton, with an initial cohort of nine mathematicians. The group is tasked with evaluating research results, coordinating releases, and providing advice. The move is a credibility and governance play: OpenAI says its internal models have already solved more than 100 open mathematics problems, a claim that has drawn sharp criticism from leading mathematicians, so an outside body may help validate or temper such announcements. It also signals that AI-for-math is entering a phase where research claims increasingly need external review rather than company self-reporting. The advisory group explicitly has no authority to change OpenAI&\#x27;s research roadmap, and the Institute for Advanced Study does not take part in the AI company&\#x27;s decisions, so its role is purely advisory. The initial membership is limited to nine mathematicians.

telegram · zaihuapd · Sep 22, 03:00

**Background**: The Institute for Advanced Study in Princeton is a renowned independent research institution historically associated with figures such as Albert Einstein, and it is not a corporate or product-focused lab. The Fields Medal is often described as the highest honor in mathematics, awarded every four years to a small number of mathematicians, typically under the age of 40. In recent years, AI labs have increasingly applied large models to open problems in mathematics — questions that have been posed but never proven or disproven — making the boundary between genuine mathematical discovery and overhyped benchmarks a matter of active dispute.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ali213.net/news/html/2026-9/1041955.html">OpenAI 模 型 解 决 大量 数 学 难 题 ！ 将成立 数 学 与 AI ...</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/%E8%8F%B2%E5%B0%94%E5%85%B9%E5%A5%96">菲尔兹奖 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.bbc.com/zhongwen/articles/c86npjqxpx9o/simp">王虹、邓煜获菲尔兹奖，中国人首摘全球数学界最高荣誉 - BBC News 中文</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI for Math`, `#AI Governance`, `#Mathematics`, `#Research Ethics`

---

<a id="item-6"></a>
## [Mimo CLI Reportedly Contains Undisclosed Telemetry and Code Collection Function](https://linux.do/t/topic/2935748) ⭐️ 7.0/10

A user who reverse-engineered Mimo CLI reported that the tool may by default upload the current project&\#x27;s repository URL, commit hash, and branch information, an behavior that can be turned off by setting MIMOCODE\_ENABLE\_ANALYSIS=false. The same analysis found that closed-source extensions bundled with the CLI contain a function named collectCodebase\(\) that is capable of enumerating files in a Git repository, reading source code, and compressing it into an archive, although the function was not observed being called and no upload of such data was confirmed. Developer CLI tools run with broad access to local repositories, so undisclosed telemetry or hidden code-reading capabilities inside an otherwise open-source tool raise real privacy and software supply-chain concerns. The finding gives developers an immediate, actionable mitigation, but because the vendor has not confirmed it and no exfiltration was observed, it is a caution flag rather than a proven incident. The capability is said to live in closed-source extensions named trajectory-bundle and codebase-bundle rather than in Mimo CLI&\#x27;s official open-source repository, which means auditing the published source alone would not reveal it. No invocation of collectCodebase\(\) has been observed, no evidence of external data upload exists, and none of the conclusions have been confirmed by the vendor.

telegram · zaihuapd · Sep 22, 08:18

**Background**: Mimo CLI is a command-line tool associated with Xiaomi&\#x27;s MiMo model family, offering text chat, speech synthesis, web search, and vision understanding from the terminal. Like many AI coding assistants, such tools often ship with telemetry to help vendors improve their products, and they frequently load prebuilt or closed-source extensions alongside the open-source core. Reverse engineering the distributed binary or extension bundle is therefore a common way for the community to check what a tool actually does when the published source code does not tell the whole story.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimocode/cli-options">Reference for the flags accepted by each MiMo Code CLI command ...</a></li>
<li><a href="https://github.com/lzg14/MiMo-cli">GitHub - lzg14/ MiMo - cli : Command - line tool for Xiaomi MiMo models.</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#security`, `#telemetry`, `#supply-chain`, `#developer-tools`

---

<a id="item-7"></a>
## [DeepSeek to brief UN Security Council on AI risks](https://www.reuters.com/world/asia-pacific/deepseek-brief-un-security-council-ai-this-week-sources-say-2026-09-22/) ⭐️ 7.0/10

DeepSeek, the Chinese AI startup, will brief the 15-member UN Security Council this week on the risks posed by artificial intelligence, according to two people familiar with the matter. The Council is scheduled to meet on Wednesday to discuss AI and international security, with OpenAI CEO Sam Altman also planning to attend and a senior Anthropic representative expected to take part. This puts a Chinese frontier-model developer alongside leading US AI labs in the same UN forum, signaling that AI safety and governance are now being treated as high-level international security issues rather than purely technical or commercial ones. It also marks a rare instance of US and Chinese AI companies appearing together in a multilateral diplomatic setting, which could shape future norms and rules for frontier AI. DeepSeek and Moonshot AI \(月之暗面\) were among the Chinese AI companies invited to speak, and DeepSeek founder Liang Wenfeng is not planning to attend, though the arrangements could still change at short notice. No specific policy proposals or outcomes from the session have been disclosed.

telegram · zaihuapd · Sep 22, 11:34

**Background**: The UN Security Council is the 15-member body responsible for maintaining international peace and security, and it has increasingly hosted discussions on emerging technologies such as AI. DeepSeek is a Chinese AI company known for releasing capable open-weight models at low cost, while Anthropic is an AI safety and research company behind the Claude model family, and Moonshot AI is a Beijing-based developer of the Kimi assistant known for long-context models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI Governance`, `#AI Safety`, `#DeepSeek`, `#UN Security Council`, `#Industry News`

---

<a id="item-8"></a>
## [iOS 27.2 Beta 2 Adds China-Only Motion Data Restriction Setting](https://telegram.me/zaihuapd/43986) ⭐️ 7.0/10

Apple&\#x27;s iOS 27.2 beta 2 reportedly introduces a China-mainland-only toggle named &quot;Restrict Motion Data&quot; \(限制動作資料\) located under Settings → Privacy &amp; Security → Motion &amp; Fitness, which, when enabled, blocks designated third-party apps from reading accelerometer, gyroscope and other motion sensor data. This is a region-specific privacy control that could break or degrade step counting, fitness tracking, motion-controlled games and some AR features for third-party apps in mainland China, and it signals that Apple is willing to ship China-exclusive permission layers that developers must plan around. According to user testing cited in the post, the option only appears when the App Store account is signed in with a mainland China Apple ID, and the reporter notes it cannot be ruled out that the setting will later expand to other Apple ID regions; the change is unconfirmed by Apple and the report is brief.

telegram · zaihuapd · Sep 22, 12:37

**Background**: iOS apps read motion data through Apple&\#x27;s Core Motion framework, which exposes the accelerometer, gyroscope, magnetometer and barometer to developers. Access to that data is already gated by the user-facing &quot;Motion &amp; Fitness&quot; permission, so this new toggle appears to be an additional, region-limited layer on top of the existing one, aimed at cutting off motion sensor access for third-party apps entirely.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@ios_guru/core-motion-and-cmdevicemotion-for-working-with-device-motion-c70c30b9896f">Core Motion and CMDeviceMotion for Working with Device... | Medium</a></li>
<li><a href="https://clouddevs.com/swift/core-motion/">Crafting Motion -Driven Experiences: Swift &amp; Core Motion Unveiled</a></li>
<li><a href="https://stepsly.app/blog/troubleshoot/motion-fitness-permission-missing-iphone">Fix: Motion Fitness Permission Missing iPhone on iPhone | Stepsly</a></li>

</ul>
</details>

**Discussion**: The only community input included is a tester&\#x27;s note that the setting requires a mainland China Apple ID to appear and may later be extended to other regions, so there is no substantive debate, agreement or counterargument to summarize yet.

**Tags**: `#iOS`, `#privacy`, `#sensors`, `#China`, `#mobile-development`

---

<a id="item-9"></a>
## [China Probes DeepSeek and Moonshot Over Alleged Data Leaks](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 7.0/10

China&\#x27;s internet regulator is reportedly investigating DeepSeek and Moonshot AI \(月之暗面\) after Anthropic published a 154-page report on September 10 accusing seven Chinese companies of improperly forwarding sensitive user data to its Claude models. One cited example claims DeepSeek routed requests from an engineer working on police surveillance systems to Claude. This marks a rare case of Chinese authorities investigating their own flagship AI labs over how data flows to foreign models, and it escalates the already tense US-China AI rivalry. The outcome could reshape cross-border API usage rules for Chinese developers and set a compliance precedent for how domestic labs handle user prompts. The allegation is not a conventional database breach but the forwarding of user prompts to a third-party model operated by an American company, and the report names seven Chinese firms in total. Neither DeepSeek nor Moonshot has been publicly charged, and the probe is based on information from people familiar with the matter rather than an announced enforcement action.

telegram · zaihuapd · Sep 22, 14:37

**Background**: Claude is the large language model series developed by the US company Anthropic, whose terms of service prohibit using its outputs to train competing models. DeepSeek is a Hangzhou-based lab funded by the hedge fund High-Flyer, while Moonshot AI is a Beijing company behind the Kimi series and is counted among China&\#x27;s &quot;AI Tigers&quot;. Forwarding user data to an overseas model can run afoul of Chinese data-export and cybersecurity rules, which are enforced by the country&\#x27;s internet regulator, typically the Cyberspace Administration of China \(CAC\).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Claude">Anthropic Claude</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#data privacy`, `#DeepSeek`, `#Anthropic`, `#China tech policy`

---

<a id="item-10"></a>
## [Anthropic ships Claude Opus 5.5 with 40% lower cost](https://www.anthropic.com/claude-opus-5-5) ⭐️ 7.0/10

Anthropic released Claude Opus 5.5, the first model in its Claude 5.5 family, which reportedly matches the prior Fable 5.1 on most tasks while running at 40% lower cost than Opus 5 and producing output more than 30% faster. Anthropic says the model posts its best result yet on automated behavior audits, ships with safeguards for cybersecurity and biosecurity domains, and will be followed by Claude Sonnet 5.5 and Haiku 5.5 in the coming weeks. The model is also available through AWS. A flagship-quality model at 40% lower cost directly cuts the price of running agentic and long-context workloads, where per-token economics often decide whether a product is viable at scale. It also intensifies price-performance competition across the frontier-lab market, since buyers can now get roughly the same capability for materially less money. The announcement is a short, single-source Telegram post with no published benchmark tables, token pricing, context-window size, or release date for the follow-up Sonnet 5.5 and Haiku 5.5 models, so the 40% cost and 30% speed figures should be treated as vendor claims until independent evaluations appear. The stated safety work is notable, because Anthropic is positioning automated behavioral auditing alongside domain-specific safeguards rather than as a separate research effort.

telegram · zaihuapd · Sep 22, 16:30

**Background**: Anthropic organizes its Claude models into tiers: Opus is the most capable and most expensive, Sonnet balances capability and price, and Haiku is the fastest and cheapest; search results also reference a Fable/Mythos-class line positioned for long-running, complex, asynchronous coding and knowledge work, which makes Opus 5.5 matching Fable 5.1 on most tasks a meaningful claim. Automated behavior auditing refers to using AI agents to systematically probe a model for undesirable traits such as sycophancy, sabotage, or self-preservation; Anthropic has open-sourced tooling for this, including the Petri framework and a companion evaluation suite. Together, cheaper flagships and standardized auditing tooling shape how enterprises decide which model tier to deploy and how they document safety due diligence.

<details><summary>References</summary>
<ul>
<li><a href="https://alignment.anthropic.com/2025/petri/">Petri: An open-source auditing tool to accelerate AI safety research</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://www.youtube.com/watch?v=Bb_FP1kuNhk">Claude &#x27;s Four Tiers Explained: Fable, Opus , Sonnet and Haiku</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#LLM`, `#model-release`, `#AI-industry`, `#cost-efficiency`

---

<a id="item-11"></a>
## [All five major Chinese smartphone brands now integrated into China&\#x27;s earthquake early warning network](https://mp.weixin.qq.com/s/ARFDE8FufvPEE_5RYOGoCw) ⭐️ 6.0/10

Honor&\#x27;s earthquake early warning application recently passed technical evaluation by the China Earthquake Networks Center and was officially connected to the China Earthquake Early Warning Network, meaning Huawei, vivo, OPPO, Xiaomi and Honor are all now authorized to provide free earthquake early warnings. Users do not need to download any app — they simply search for &quot;地震预警&quot; \(earthquake warning\) in their phone settings and switch it on, with Huawei and vivo each already exceeding 100 million users. This closes the loop on a public-safety capability that now reaches hundreds of millions of people by default rather than through opt-in third-party apps, and it turns the country&\#x27;s earthquake monitoring infrastructure into a consumer-facing alert channel delivered at the system level. For a country that experiences frequent destructive earthquakes, shaving alert delivery down to the second and removing the app-download barrier could meaningfully increase the number of people who receive a warning before strong shaking arrives. Alerts are pushed as four color-coded levels — blue, yellow, orange and red — to areas where the estimated seismic intensity is 2 degrees or higher, following the Chinese seismic intensity scale. The service is free, system-level and app-free, which is what allows second-scale delivery, but it depends on users having enabled the setting and on the phone being powered on and connected.

telegram · zaihuapd · Sep 22, 02:30

**Background**: Earthquake early warning does not predict earthquakes; it exploits the fact that fast-moving P-waves arrive before the more destructive S-waves and surface waves, giving stations near the epicenter a few seconds&\#x27; head start to broadcast an alert to people farther away. China completed its National Earthquake Early Warning Project in July 2024, building what the China Earthquake Administration describes as the world&\#x27;s largest such network with roughly 15,900 monitoring stations nationwide. The Chinese seismic intensity scale \(CSIS\) measures shaking impact in 12 degrees of intensity, or liedu, rather than magnitude, which is why alerts are triggered by estimated intensity in a given area.

<details><summary>References</summary>
<ul>
<li><a href="https://news.cgtn.com/news/2024-07-27/China-establishes-world-s-largest-quake-early-warning-network-1vzsfwWoOMU/p.html">China establishes world&#x27;s largest quake early warning network - CGTN</a></li>
<li><a href="https://en.wikipedia.org/wiki/China_seismic_intensity_scale">China seismic intensity scale - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#earthquake-early-warning`, `#mobile`, `#public-safety`, `#China-tech`, `#emergency-alerting`

---

<a id="item-12"></a>
## [US Proposes AI Incident Reporting Channel With China](https://x.com/rohanpaul_ai/status/2102254209597157548) ⭐️ 6.0/10

During talks in New York on September 20, the United States proposed setting up an AI incident reporting channel with China, intended to notify the other side of AI-related events that cross national security thresholds. US Treasury Secretary Bessent framed the move as a way to improve transparency between the two countries, and the two sides also plan a regular US-China AI dialogue on shared risks, though China&\#x27;s official statement only confirmed that AI issues were discussed and did not explicitly accept the specific mechanism. If implemented, this would be one of the first government-to-government channels specifically for AI incident notification between the world&\#x27;s two leading AI powers, potentially reducing the risk of miscalculation or escalation when high-stakes AI events occur. It also signals that AI safety and risk management are moving from academic and corporate discussions into formal diplomatic and national security agendas. The proposal is not yet a bilateral agreement or treaty, and no concrete definition of the national security threshold, reporting timeline, or verification mechanism has been made public. It remains unclear whether China will accept the mechanism, since its official readout stopped at confirming that AI-related topics were discussed.

telegram · zaihuapd · Sep 22, 06:48

**Background**: An AI incident reporting channel generally refers to a formal process through which parties share information about AI-related events — such as accidents, harmful model behavior, or near-misses — that meet some agreed severity or national security threshold, similar in spirit to crisis hotlines used in other security domains. The United States and China are the two largest developers of frontier AI models, and how they coordinate on AI risks affects global AI governance efforts. This proposal is part of a broader effort to build regular US-China AI dialogue on shared risks, but as of the talks reported it has not been formalized in any binding document.

<details><summary>References</summary>
<ul>
<li><a href="https://incidentdatabase.ai/">Welcome to the Artificial Intelligence Incident Database</a></li>
<li><a href="https://superkind.ai/ai-lexicon/ai-incident-reporting">AI Incident Reporting | AI Guide | Superkind</a></li>
<li><a href="https://watchdogsecurity.io/iso-42001/external-reporting-capabilities">ISO 42001 A.8.3: External Reporting of AI Adverse Impacts</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#US-China relations`, `#AI policy`, `#AI safety`, `#geopolitics`

---

<a id="item-13"></a>
## [OpenAI to Let Outside Groups Evaluate AI Models Earlier](https://www.bloomberg.com/news/articles/2026-09-22/openai-to-let-outside-groups-evaluate-ai-models-at-earlier-phase) ⭐️ 6.0/10

OpenAI plans to let third-party organizations conduct technical safety evaluations of its AI models at earlier stages of training, evaluation, and release, with the details to be published in a blog post on Tuesday. Previously such evaluations were typically scheduled only shortly before a model&\#x27;s public launch, and the company now says external evaluators must meet requirements for independent mechanisms, scientific rigor, and clear accountability. Moving independent safety testing earlier in the development lifecycle could give outside researchers meaningful influence before a model is finalized, rather than only a pre-launch snapshot. As AI companies face rising internal concern about catastrophic risk, this sets a precedent for how frontier labs structure third-party oversight and could shape emerging AI governance expectations. OpenAI is reportedly in talks with organizations such as METR and Redwood Research, and may allow external evaluators to work on sensitive tasks inside its offices — a notable concession given typical confidentiality constraints around unreleased models. The arrangement is described as a procedural and policy change rather than a release of new technical research, and the exact scope of access has not yet been detailed.

telegram · zaihuapd · Sep 22, 17:39

**Background**: Frontier AI labs have historically kept model internals confidential until launch, when they publish system cards and limited safety documentation. METR \(Model Evaluation and Threat Research\) is a Berkeley-based nonprofit that evaluates frontier models&\#x27; ability to perform long-horizon, agentic tasks that some researchers argue could pose catastrophic risks. Third-party evaluation is a central demand of the AI safety community, on the theory that internal teams face commercial pressure that can bias self-assessment. The news also follows recent reports of models unexpectedly intruding into other companies&\#x27; systems during testing, which intensified employee concerns about dangerous capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/METR">METR - Wikipedia</a></li>
<li><a href="https://metr.org/">METR</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#OpenAI`, `#AI Governance`, `#Model Evaluation`, `#Industry News`

---