---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
report: default
---

> 从 282 条内容中筛选出 10 条重要资讯。

---

1. [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](#item-1) ⭐️ 9.0/10
2. [苹果联手阿里自研中国专属 AI 模型，或成首个获批外企](#item-2) ⭐️ 9.0/10
3. [AI 机器人实验室每年测试 300 万人体组织样本，有望取代动物试验](#item-3) ⭐️ 8.0/10
4. [苹果提议对美国区 App Store 外部购买抽成最高 15%](#item-4) ⭐️ 8.0/10
5. [PostgreSQL 修复高危 to\_char 漏洞，可导致任意代码执行](#item-5) ⭐️ 8.0/10
6. [Hermes Agent 推出 Bot Mode，支持多机器人协作分工](#item-6) ⭐️ 7.0/10
7. [GLM-5.3 发布，自测代码基准提升 50%](#item-7) ⭐️ 7.0/10
8. [美国法官令谷歌取消第三方应用商店安装障碍](#item-8) ⭐️ 7.0/10
9. [Anthropic 第二季度营收突破 115 亿美元](#item-9) ⭐️ 6.0/10
10. [中信旗下信宸资本接近以超 15 亿美元收购阿里游戏部门灵犀](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 9.0/10

小红书 dots 实验室开源了 dots3-note preview，这是 dots3 系列首个开放权重模型。该模型总参数 280B，每次仅激活 16B，支持 512K 上下文，并可处理文字、图片、视频和音频。 这次发布是开放权重 AI 的一个重要里程碑，表明大规模 MoE 模型可以以较低的推理成本运行。它还引入了一种新的强化学习方法（TEMPO）和两个智能体基准，有望推动长程自主智能体的研究。 该模型采用 TEMPO 强化学习方法，基于自批判和测试时价值估计来训练长程智能体。权重已在 Hugging Face 开放，同时发布 VibeSearchBench 和 VibeLifeBench 两个真实场景智能体基准。

telegram · zaihuapd · 8月14日 08:27

**背景**: 混合专家（MoE）模型每次只激活一部分参数，从而在保持总参数规模很大的同时降低计算成本。长上下文和多模态支持使这类模型在文档分析、视频理解和智能体工作流等任务中很有用。强化学习通常用于预训练之后来改进推理和工具使用能力，而基准测试则是衡量真实世界表现的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.27882">VibeSearchBench : Benchmarking Long-horizon Proactive Search in...</a></li>
<li><a href="https://huggingface.co/papers/2605.27882">Paper page - VibeSearchBench : Benchmarking Long-horizon...</a></li>
<li><a href="https://paperswithcode.co/paper/2608.10875">VibeLifeBench : Can Your Life Agent Be Proactive... | Papers with Code</a></li>

</ul>
</details>

**标签**: `#MoE`, `#open-source`, `#reinforcement-learning`, `#multimodal`, `#AI`

---

<a id="item-2"></a>
## [苹果联手阿里自研中国专属 AI 模型，或成首个获批外企](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 9.0/10

苹果正在阿里巴巴的支持下，为中国市场专门训练一款大语言模型，改变此前依赖第三方模型的策略。苹果的生成式 AI 服务已在中国网信办备案，Apple Intelligence 预计未来数月将随 iOS 更新在华上线。 如果获批，苹果将成为首家获准在中国提供自有 AI 模型的外国公司，这是在监管严格的市场中的一个里程碑。此举让苹果能更好地掌控中国用户的 AI 体验，并可能重塑全球科技企业的竞争格局。 据知情人士透露，这款模型是专为中国市场训练，并得到阿里巴巴的支持。中国网信办已于上月对苹果的生成式 AI 服务进行备案，这是在中国推出公开 AI 服务的前提条件。Apple Intelligence 结合端侧与服务器处理，适用于 iPhone 15 Pro 及后续机型等受支持设备。

telegram · zaihuapd · 8月14日 14:47

**背景**: Apple Intelligence 是苹果在 2024 年 6 月 WWDC 上发布的一套人工智能功能，涵盖写作工具、图像生成、通知摘要以及 ChatGPT 集成等。它内置在 iOS 18、iPadOS 18 和 macOS Sequoia 中，适用于 Apple 芯片 Mac 以及 iPhone 16 系列、iPhone 15 Pro 等较新机型。在中国，外国公司提供 AI 服务必须获得监管批准，因此苹果与阿里巴巴的合作以及向网信办备案具有重要意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#LLM`

---

<a id="item-3"></a>
## [AI 机器人实验室每年测试 300 万人体组织样本，有望取代动物试验](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 8.0/10

位于旧金山南部的初创公司 Vivodyne 展示了由 12 个“蜂巢”机器人实验室组成的网络，利用 AI 设计的实验每年对 300 多万个人体组织样本进行受控测试，容量约为美国全部临床试验年总量的两倍。该系统旨在让药物疗效与安全性测试更快、更贴近人体。 大约 90%在动物试验中成功的药物最终仍会在人体临床试验中失败，因此能够生成海量人体组织数据的平台，有望降低药物研发风险，并加速取代动物试验。若经充分验证，它可能重塑监管科学、制药研发和个性化医疗。 这些“蜂巢”是衣柜大小的机器人系统，培养人体组织并执行 AI 设计的实验方案，生成多组学数据——Vivodyne 称之为“让生物学可计算”。不过，器官芯片等微生理系统仍处于发展早期，孤立组织可能无法完全再现全身的复杂生理过程。

telegram · zaihuapd · 8月14日 01:48

**背景**: 器官芯片和微生理系统是使用活体人类细胞模拟器官功能的微流控设备，长期以来被视为动物试验的替代方案。然而，传统器官芯片通量低，且可能遗漏全身系统性相互作用。Vivodyne 的做法是将工程化人体组织与 AI 设计的实验及机器人自动化相结合，实现组织检测的工业化，弥补了规模与通量上的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>
<li><a href="https://en.wikipedia.org/wiki/Organ-on-a-chip">Organ-on-a-chip</a></li>

</ul>
</details>

**标签**: `#AI`, `#Biotech`, `#Drug Discovery`, `#Animal Testing`, `#Automation`

---

<a id="item-4"></a>
## [苹果提议对美国区 App Store 外部购买抽成最高 15%](https://9to5mac.com/2026/08/13/apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us/) ⭐️ 8.0/10

苹果已向美国法院提交提案，对 App Store 外部购买收取最高 15% 的抽成。费率因项目而异：标准应用为 15%，视频、新闻等合作项目及订阅续费为 10%，小型企业计划应用为 5%。 这是苹果与 Epic 反垄断案的重要进展，因为它为外部购买制定了具体的抽成比例，可能影响未来的 App Store 政策。结果将直接影响开发者的收入，以及关于 App Store 垄断行为的更广争议。 该提案是在美国最高法院驳回苹果暂停下级法院费率审理的请求后提出的。Epic 将有机会回应，苹果预计将于 9 月 14 日前向最高法院提交书面意见。

telegram · zaihuapd · 8月14日 02:33

**背景**: Epic Games 于 2020 年起诉苹果，指控 App Store 的抽成和外部支付限制构成反竞争。2021 年，地区法院命令苹果允许开发者提供外部支付链接，但此类购买的费用结构仍未解决。苹果此前已通过多个项目提供降低的抽成比例，例如面向符合条件开发者的 App Store 小型企业计划（15%），以及专门面向订阅新闻出版商的 News Partner 计划和面向优质视频订阅提供商的 Video Partner 计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2021/08/apple-introduces-the-news-partner-program/">Apple introduces the News Partner Program - Apple</a></li>
<li><a href="https://developer.apple.com/programs/video-partner/">Apple Video Partner Program - Apple Developer... - Apple Developer</a></li>
<li><a href="https://qonversion.io/blog/apple-reduces-app-store-commission-to-15">Apple Small Business Program 2026: How to Get... | Qonversion Blog</a></li>

</ul>
</details>

**标签**: `#Apple`, `#App Store`, `#Epic Games`, `#Antitrust`, `#Commissions`

---

<a id="item-5"></a>
## [PostgreSQL 修复高危 to\_char 漏洞，可导致任意代码执行](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL 披露了 CVE-2026-14669，这是一个存在于 to\_char\(timestamptz\) 函数中的堆缓冲区溢出漏洞，可能导致任意代码执行。相关修复已包含在 18.6、17.11、16.15、15.19 和 14.24 这些次版本更新中。 该漏洞的 CVSS 评分为 8.8，允许低权限数据库用户以 PostgreSQL 服务进程的操作系统权限执行任意代码，影响多个受支持版本。升级到已修复的版本对数据库安全至关重要。 该漏洞由 to\_char\(timestamptz\) 函数处理超长 POSIX 时区缩写时触发，导致堆缓冲区溢出。由于 18.5 因回归问题未发布，18.x 用户应直接升级到 18.6；本次更新只需替换程序文件并重启服务，无需转储数据库或运行 pg\_upgrade。

telegram · zaihuapd · 8月14日 14:35

**背景**: PostgreSQL 中的 to\_char 函数用于将日期/时间值转换为格式化的字符串，timestamptz 表示带时区的时间戳。堆缓冲区溢出是指程序在堆中分配的缓冲区之外写入数据，可能导致数据损坏或代码执行。时区缩写（如 &\#x27;EST&\#x27; 或自定义的 POSIX 名称）可能很长；如果格式化函数未正确检查长度，攻击者就可能利用此漏洞覆盖内存。该漏洞需要低权限的数据库账户，并非无需认证即可利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/functions-formatting.html">PostgreSQL: Documentation: 18: 9.8. Data Type Formatting ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heap_overflow">Heap overflow - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">List of tz database time zones - Wikipedia</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#CVE`, `#security`, `#buffer overflow`, `#vulnerability`

---

<a id="item-6"></a>
## [Hermes Agent 推出 Bot Mode，支持多机器人协作分工](https://x.com/Teknium/status/2088003994904113614) ⭐️ 7.0/10

Hermes Agent（来自 Nous Research）推出了 Bot Mode 新功能，它能把代理档案变成各自独立的命名机器人，每个机器人都有自己的聊天、头像、性格和日程，并且机器人之间可以互相通信。目前正在通过 GitHub 插件在 Hermes Desktop 上开展为期一天的公开测试，收集反馈后会再并入正式桌面应用。 这一功能意义重大，因为它使得不同 AI 代理之间可以分工协作、共同完成复杂任务，是迈向实用化代理间工作流的关键一步。这也反映出开源 AI 工具在消费级平台上支持多角色协调自动化的趋势。 Bot Mode 是 Hermes Agent 的桌面应用插件，随桌面应用一起安装；它是现有 sessions 模式之外的一种新方式。公开测试为期一天，根据项目描述，该功能在用户本地运行，每个机器人拥有自己的记忆和模型设置。

telegram · zaihuapd · 8月14日 04:13

**背景**: Hermes Agent 是由 Nous Research 开发的开源 AI 代理，旨在利用大语言模型执行自主的多步骤任务，并通过持久化记忆和技能与用户共同成长。它提供了适用于 macOS、Windows 和 Linux 的原生桌面应用，用户可以在其中与代理对话并管理档案。Bot Mode 在此基础上扩展，将每个档案变成一个命名机器人，并让这些机器人可以相互交互，从而在用户自己的机器上形成一个小的多代理系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NousResearch/Hermes-Bot-Mode">GitHub - NousResearch/Hermes-Bot-Mode: Bot Mode for the ...</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent | Nous Research</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hermes_Agent">Hermes Agent</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Hermes Agent`, `#multi-agent`, `#AI tools`, `#announcement`

---

<a id="item-7"></a>
## [GLM-5.3 发布，自测代码基准提升 50%](http://z.ai/) ⭐️ 7.0/10

智谱发布了 GLM-5.3，模型沿用 GLM-5.2 基座，全部提升来自后训练。官方称其在内部 Z.ai Code Bench 上较前代提升 50%，并在 Terminal Bench 3.0 等公开基准上达到开源最优。 这次发布说明仅靠后训练就能带来显著的编码能力提升，也加剧了开源权重模型之间的竞争。由于官方承诺两周后开源权重，开发者和企业有望很快采用或微调该模型。 需要留意的是，这些基准成绩为官方自测，且安全评估显示漏洞利用基准得分较 GLM-5.2 翻倍以上。智谱还称已协助安全团队在 269 个项目中识别 2436 个漏洞，其中 1097 个为中高危。

telegram · zaihuapd · 8月14日 05:27

**背景**: GLM-5.x 是智谱（Z.ai）最新一代大语言模型系列，定位为对标闭源推理模型的开源权重产品。后训练是指在基座模型预训练之后进行的微调与对齐，而 Z.ai Code Bench 看起来是智谱内部用于评估编码能力的基准，Terminal Bench 3.0 则是一个面向终端智能体任务的社区共建基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/z-ai/glm-5.2">GLM 5.2 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://www.tbench.ai/">Terminal-Bench</a></li>
<li><a href="https://www.frontierbench.ai/announcement">Terminal-Bench 3.0</a></li>

</ul>
</details>

**标签**: `#GLM`, `#LLM`, `#code generation`, `#AI`, `#open source`

---

<a id="item-8"></a>
## [美国法官令谷歌取消第三方应用商店安装障碍](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 7.0/10

美国联邦法官下令谷歌删除阻止或吓退用户安装第三方安卓应用商店的多余步骤和警告弹窗。法院给予谷歌一周时间，使其让安装竞品商店变得像安装普通安卓应用一样直接。 这是一项重大的反垄断裁决，直接影响安卓应用的分发方式，可能为竞品应用商店与 Google Play 更公平地竞争打开大门。开发者和用户将因障碍减少而受益，并可能重塑移动生态系统的格局。 该指令源自 Epic 诉谷歌反垄断案，此前陪审团裁定谷歌在安卓应用分发上构成非法垄断。法官还去除了“恐吓弹窗”和多步“安装”确认界面，法院称这些是蓄意制造的“反竞争摩擦”。

telegram · zaihuapd · 8月14日 09:55

**背景**: 安卓应用通常通过 Google Play 分发，但用户也可以从其他来源侧载 APK 文件。谷歌历来为安装第三方应用商店增加了额外警告和步骤，法院认定其意图是劝阻用户。该裁决是监管机构对谷歌在安卓应用分发领域控制权进行更广泛审视的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androidauthority.com/google-android-sideloading-unverified-apps-new-rules-3650343/">Android&#x27;s new sideloading rules are here, and they come with ...</a></li>
<li><a href="https://www.androidauthority.com/how-android-sideloading-restrictions-may-work-3595355/">Google&#x27;s plan to restrict sideloading on Android has a ...</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#Google`, `#Android`, `#app stores`, `#regulation`

---

<a id="item-9"></a>
## [Anthropic 第二季度营收突破 115 亿美元](https://www.reddit.com/r/finance/comments/1vok26d/anthropic_revenue_surges_to_over_115_billion_in/) ⭐️ 6.0/10

Anthropic 公布第二季度营收超过 115 亿美元，较此前大幅增长，显示其 AI 产品的商业采用速度加快。该公告标志着这家 AI 公司的重要财务里程碑，但未提供更详细的财务分项。 这一里程碑凸显了 Anthropic 作为 AI 行业主要商业力量的崛起，正与更大的竞争对手展开角逐。强劲的营收增长也表明企业对尖端 AI 模型的需求正在加速，可能影响整个行业的投资与竞争格局。 115 亿美元这个数字指该季度的营收，对一家私营 AI 公司而言规模可观。公告中未包括按产品线或盈利能力的明细，因此其成本结构和利润率仍不得而知。

reddit · r/finance · /u/FrankLucasV2 · 8月14日 21:26

**背景**: Anthropic 是一家领先的 AI 研发与部署公司，以 Claude 系列大语言模型和对 AI 安全的高度关注而闻名。该公司在快速扩张的生成式 AI 市场中与 OpenAI 等头部实验室直接竞争。此类营收里程碑被视为衡量 AI 研究突破能否转化为可持续商业业务的关键指标。

**标签**: `#Anthropic`, `#AI business`, `#revenue`, `#finance`

---

<a id="item-10"></a>
## [中信旗下信宸资本接近以超 15 亿美元收购阿里游戏部门灵犀](https://www.bloomberg.com/news/articles/2026-08-14/trustar-is-said-to-near-1-5-billion-deal-for-alibaba-gaming-arm) ⭐️ 6.0/10

中信集团旗下私募机构信宸资本（Trustar Capital）正接近收购阿里巴巴的游戏业务灵犀互娱，估值或超过 15 亿美元。这笔交易是阿里巴巴在 CEO 吴泳铭主导下剥离非核心资产、聚焦 AI 与云计算的又一举措。 这显示阿里巴巴正积极剥离游戏等非核心业务，全力转向人工智能和云计算。同时，也反映出私募资本对中国大型游戏资产的兴趣，即便行业仍面临监管和市场压力。 灵犀的旗舰产品《三国志·战略版》是与日本光荣特库摩合作开发的大型多人在线策略游戏。信宸资本在多家游戏公司等竞购者中胜出，成为最可能的买家，但磋商仍在进行，尚未作出最终决定。

telegram · zaihuapd · 8月14日 10:24

**背景**: 灵犀互娱是阿里巴巴旗下的游戏工作室，源于阿里在数字娱乐领域的整体布局。阿里巴巴 CEO 吴泳铭一直在精简集团业务，剥离游戏等非核心部门，以更聚焦 AI、云计算和电商。信宸资本是中信集团旗下的亚洲私募股权机构，而中信是中国最大的国有背景金融企业之一。

**标签**: `#Alibaba`, `#Acquisition`, `#Gaming`, `#Private Equity`, `#Tech Industry`

---