---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17 23:03:45 +0000
lang: zh
report: default
---

> 从 186 条内容中筛选出 7 条重要资讯。

---

1. [MiMo-V2.6 启动大规模 RL 训练，细节将陆续开源](#item-1) ⭐️ 7.0/10
2. [GLM 的 Infra Agent 在 10 万颗国产芯片上自建推理基础设施](#item-2) ⭐️ 7.0/10
3. [苹果考虑搭载英伟达技术重返服务器市场，推出 M8 Ultra AI 服务器](#item-3) ⭐️ 6.0/10
4. [PS5 Linux 开发者因“Slop Kiddies”向索尼上报漏洞而退出项目](#item-4) ⭐️ 6.0/10
5. [Kimi 发布金融行业 AI 解决方案，首批落地工商银行、中信建投](#item-5) ⭐️ 6.0/10
6. [比亚迪拟在欧洲布局四座工厂，加速本土化生产](#item-6) ⭐️ 6.0/10
7. [苹果 M5 Ultra 跑分泄露：Metal 成绩超越 RTX 5090](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [MiMo-V2.6 启动大规模 RL 训练，细节将陆续开源](https://x.com/_LuoFuli/status/2100296686719610932) ⭐️ 7.0/10

小米 MiMo 团队负责人 Fuli Luo 在 X 上宣布，经过近半年研究，MiMo-V2.6 正在进行大规模强化学习训练，并在三个方面扩展：每步约 20 亿 tokens 的算力、多任务 agentic RL 环境以及裁判计算。她表示技术细节将在未来几周内陆续开源。 这一消息表明，一家重要的中国模型团队正把 RL 算力、agentic 环境和裁判计算视为下一代大模型的关键扩展方向，而不再主要依赖预训练规模。若承诺的细节得以开源，将为研究者提供复现大规模多任务 agentic RL 的罕见参考，并可能加剧 agentic 推理模型领域的竞争。 披露的规模约为每个 RL 步骤 20 亿 tokens，同时还包括多任务 agentic 训练环境和额外的裁判/评估器算力；但目前尚无基准结果、模型 ID 或公开 API，MiMo-V2.6 Pro 和 Flash 仍被描述为处于 RL 训练中。团队表示细节会逐步发布，而非一次性给出完整技术报告。

telegram · zaihuapd · 9月17日 01:52

**背景**: MiMo 是小米的大语言模型系列；其上一代万亿参数模型 MiMo-V2-Pro 在今年 3 月曾位列 Artificial Analysis 全球大模型综合智能排行榜第 8 名。强化学习是一种后训练技术，通过奖励信号改进模型行为，如今已成为训练推理模型和 agent 模型的核心手段。多任务 agentic RL 指让 agent 在多种环境和任务中接受训练，而裁判计算则指用于奖励模型或评估器模型的算力，这些模型负责给 agent 的输出打分。开源这些细节之所以重要，是因为大规模 RL 的训练配方通常比基础模型训练更难复现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apimaster.ai/blog/mimo-v2-6-api">MiMo - V 2 . 6 API: Release Date, Status and What You... | APIMaster.AI</a></li>
<li><a href="https://news.aibase.com/news/31131">Xiaomi Publicly Reveals the RL Training Process of MiMo - V 2 . 6 Large...</a></li>
<li><a href="https://galileo.ai/blog/scaling-judge-compute-ai-evaluation">Scaling Judge Compute : The Next Frontier in AI Evaluation | Galileo</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Reinforcement Learning`, `#Agentic AI`, `#Open Source`, `#MiMo`

---

<a id="item-2"></a>
## [GLM 的 Infra Agent 在 10 万颗国产芯片上自建推理基础设施](https://z.ai/blog/glm-built-its-inference-infrastructure) ⭐️ 7.0/10

2026 年 9 月 17 日，Z.ai 发布技术复盘，称由 GLM-5.3 驱动的 Infra Agent 协助构建了 GLM-5.3-Flash 的生产推理服务，部署在超过 10 万颗国产 AI 加速器之上。该系统从模型适配到正式上线耗时不到两周，端到端吞吐量提升约 3 倍（其他报道给出的具体数字为 13 天内提升 3.22 倍）。 这一声明的意义在于，它把大模型智能体放进了「为该模型家族提供服务的推理基础设施」的工程建设回路之中，是朝着业界长期讨论的递归自我改进目标迈出的具体一步。同时它也表明，大规模生产级推理栈可以完全基于国产 AI 加速器而非英伟达 GPU 端到端搭建，这对处于出口管制环境下的中国 AI 生态具有重要价值。 团队通过分层测试、日志、追踪和基准测试建立了「密集反馈」机制，使智能体能够持续定位问题并优化代码，最终由工程师与智能体共同完成系统优化。Z.ai 明确说明这尚不构成递归自我改进；此外，公开材料是企业博客性质的技术复盘，而非包含可独立复现基准的同行评审论文。

telegram · zaihuapd · 9月17日 08:38

**背景**: 递归自我改进（RSI）指系统能够提升「自身改进自身」的能力，这一概念可追溯到更早的「种子 AI」（seed AI）设想，即一个能自我启动并不断放大自身能力的系统。近期综述研究把「有界自我精炼」与「开放式递归自我改进」区分开来：前者收敛可控、已在工业界普遍实践，后者则仍受制于现实锚定要求、模型坍缩动力学与算力约束。文中提到的「国产 AI 加速器」指华为昇腾、寒武纪、摩尔线程、壁仞、沐曦等中国厂商的芯片，它们是受对华出口限制的英伟达硬件的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/glm-built-its-inference-infrastructure">Toward Recursive Self-Improvement: How GLM Built Its Own Inference Infrastructure</a></li>
<li><a href="https://www.explainx.ai/blog/glm-5-3-infra-agent-dense-feedback-inference-2026">GLM-5.3 Infra Agent: 3.22x Throughput in 13 Days | explainx.ai Blog | explainx.ai</a></li>
<li><a href="https://www.unite.ai/z-ai-details-glm-5-3-flash-inference-build-on-100-000-chinese-chips/">Z.ai Details GLM-5.3-Flash Inference Build on 100,000 Chinese ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#LLM agents`, `#inference serving`, `#self-improvement`, `#AI accelerators`

---

<a id="item-3"></a>
## [苹果考虑搭载英伟达技术重返服务器市场，推出 M8 Ultra AI 服务器](https://www.reuters.com/technology/apple-considers-nvidia-tech-return-server-market-information-reports-2026-09-16/) ⭐️ 6.0/10

据 The Information 报道（路透社 2026 年 9 月 16 日跟进），苹果正考虑重返企业服务器市场，推出搭载自研 M8 Ultra 芯片的 AI 服务器，提供双芯片和四芯片两种版本，并可能采用英伟达的 NVLink Fusion 互联技术。若最终落地，这将是苹果自 2011 年停产 Xserve 以来首次推出专用服务器硬件。 这标志着苹果可能重新踏入企业级 AI 基础设施市场——一个它 15 年前放弃、目前毫无存在的领域，同时也暗示苹果与英伟达近二十年的紧张关系可能出现缓和。若成功，苹果的 M 系列芯片将直接与基于英伟达的系统争夺 AI 开发者、企业和政府客户。 该服务器预计最早 2029 年才能上市，报道也提醒项目仍可能被取消，或最终放弃使用英伟达技术。NVLink Fusion 是英伟达提供的高带宽、低延迟互联 IP，允许超大规模厂商和 AI 原生公司把自己的定制 XPU 和 CPU 接入英伟达的 AI 基础设施；值得关注的是，苹果若采用它，就意味着将非英伟达的加速器与英伟达的互联架构搭配使用。

telegram · zaihuapd · 9月17日 02:40

**背景**: 苹果的 Xserve 是 2002 年至 2011 年 1 月间销售的机架式服务器产品线，停产后苹果引导客户转向 Mac Pro 和 Mac mini，此后便再无专用服务器产品。M 系列中的 “Ultra” 是苹果最高端的系统级芯片（SoC）设计，用于高端 Mac 台式机，特点是统一内存容量大、内存带宽高。NVLink 是英伟达专有的 GPU 互连技术，目前已发展到第六代并配套 NVLink Switch；NVLink Fusion 则把这一互连架构开放给第三方的定制芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/nvlink-fusion/">Build Semi-Custom AI Infrastructure | NVIDIA NVLink Fusion</a></li>
<li><a href="https://9to5mac.com/2026/09/16/apple-planning-to-sell-ai-servers-powered-by-m8-ultra-chips-says-report/">Apple planning to sell AI servers powered by M8 Ultra chips ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Xserve">Xserve - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Apple`, `#NVIDIA`, `#AI Servers`, `#Hardware`, `#Industry News`

---

<a id="item-4"></a>
## [PS5 Linux 开发者因“Slop Kiddies”向索尼上报漏洞而退出项目](https://www.techpowerup.com/352739/ps5-linux-dev-drops-project-after-slop-kiddies-cash-in-on-crucial-exploit) ⭐️ 6.0/10

2026 年早些时候发布 PS5 Linux 项目的开发者 Andy Nguyen（即 TheFlow0）宣布退出 PS5 破解圈，并停止 PS5 Linux 的开发工作，正在开发中的 PS5 Pro 支持也随之搁置。他表示，一群借助 LLM 编写脚本的“Slop Kiddies”发现了 PS5 Pro 上最后一个 Hypervisor 漏洞，并（据称为了漏洞赏金）将其上报给索尼，迫使他不得不放弃计划。 这一事件是 LLM 辅助漏洞挖掘与主机破解/自制软件文化正面碰撞的早期具体案例——在后者中，漏洞通常被刻意囤积并选择时机发布，以最大化社区利益，而非直接上报给平台方。它同时移除了在 PS5 Pro 硬件上运行 Linux 的最主要途径，也凸显出漏洞赏金计划如何抽干一个圈子中本就稀少的剩余漏洞资源。 Nguyen 原本希望把这个漏洞保留到《GTA 6》发售，好让破解用户既能在同一台主机上玩到《GTA 6》，又能运行 Linux；他曾请求上报者至少等到那时，但未获理会。已有的 PS5 Linux 代码此前已在 GitHub 上以 GPL-3.0 协议公开，但 PS5 Pro 相关部分尚未包含在内，意味着这部分工作很可能就此流失。

telegram · zaihuapd · 9月17日 07:43

**背景**: PS5 Linux 能把一台已破解的 PlayStation 5 变成通用 Linux 桌面，释放其 8 个 Zen 2 核心（16 线程，最高 3.5 GHz）以及最高 2.23 GHz 的 RDNA 2 GPU。由于这类项目依赖底层 Hypervisor（HV）漏洞——即让代码逃出主机固件沙箱的缺陷——每一个被索尼获知并修补的漏洞，对社区而言就等于永久作废。历史上，像 Nguyen 这样的破解开发者会有选择地公开漏洞，或把发布时机安排在重要游戏发售前后，这也是此次一个罕见的“最后一个可用漏洞”被泄露并上报会造成如此大破坏的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/352739/ps5-linux-dev-drops-project-after-slop-kiddies-cash-in-on-crucial-exploit">PS5 Linux Dev Drops Project After &quot;Slop Kiddies&quot; Cash in on ...</a></li>
<li><a href="https://www.gamesradar.com/games/ps5-linux-dev-abandons-the-project-as-ai-slop-kiddies-ruin-open-source-mods-ahead-of-gta-6-just-a-bunch-of-noobs-using-llms-and-writing-hacks-they-dont-even-understand/">PS5 Linux dev abandons the project as AI &quot;slop kiddies&quot; ruin ...</a></li>
<li><a href="https://www.tomshardware.com/software/linux/ps5-linux-loadr-goes-public-turning-phat-consoles-into-full-linux-pcs">PS5 Linux loader goes public, turning ‘Phat’ consoles into ...</a></li>

</ul>
</details>

**标签**: `#PS5`, `#Linux`, `#Security`, `#Exploit`, `#LLM`

---

<a id="item-5"></a>
## [Kimi 发布金融行业 AI 解决方案，首批落地工商银行、中信建投](https://www.cnfin.com/cmjj-lb/detail/20260917/4471293_1.html) ⭐️ 6.0/10

月之暗面 Kimi 发布金融行业 AI 解决方案，整合十余个权威数据源与 9 项金融专业技能，并称工商银行、中信建投、中金公司、易方达基金等数十家头部机构已使用或共建相关能力。材料还宣称，财务建模的人力投入由 5—15 人天降至 2—4 人天，行业深度报告研究由 10—20 天缩短至 2—4 天。 这标志着 Kimi 从通用聊天机器人向垂直企业级 AI 的延伸，而中国金融业监管严格、银行、券商与基金公司既是最有价值的客户，也是对合规最敏感的客户。如果效率提升的说法成立，可能会改变卖方研究与财务建模的用人方式，并使月之暗面与既有金融数据厂商以及其他争夺同一预算的中国大模型公司直接竞争。 该方案设置了数据分级、访问授权和人工复核等合规措施，这些是被中国持牌金融机构采用的前提条件。需要注意的是，所有数字均来自厂商自己的材料：既无第三方验证，也未披露底层使用哪些模型或智能体架构，更没有价格信息，也未说明各被点名机构实际推广的范围有多大。

telegram · zaihuapd · 9月17日 10:51

**背景**: 月之暗面（Moonshot AI）是一家总部位于北京的 AI 公司，以 Kimi 聊天机器人和助手最为人熟知。“垂直 AI”指面向某一具体行业构建的 AI 系统，依托领域数据和定制化工作流，而非追求通用性的广度，金融、医疗、法律是最常见的方向。财务建模指基于电子表格搭建估值与预测模型，历来是分析师耗时较大的工作；行业深度报告则是卖方分析师用数天到数周产出的长篇研究文档。中国金融机构受严格的数据治理规则约束，因此任何处理内部或市场数据的 AI 工具都必须具备访问控制与可审计能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E6%9C%88%E4%B9%8B%E6%9A%97%E9%9D%A2_%28%E5%85%AC%E5%8F%B8%29">月之暗面 (公司) - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.aiworldtoday.net/p/vertical-ai-explained-what-it-is-why-it-matters">Vertical AI Explained: What It Is, Why It Matters, and How It ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#enterprise-ai`, `#fintech`, `#Kimi`, `#vertical-ai`

---

<a id="item-6"></a>
## [比亚迪拟在欧洲布局四座工厂，加速本土化生产](https://www.bloomberg.com/news/articles/2026-09-17/china-s-byd-targets-four-european-plants-to-anchor-regional-push) ⭐️ 6.0/10

比亚迪计划在欧洲长期建立 3 座整车工厂和 1 座电池工厂，其首座欧洲乘用车工厂已在匈牙利投产。公司计划在今年年底前确定第二座工厂的选址，并且目前更倾向于收购并改造欧洲现有的工厂设施，而非从零新建。 本土化生产是比亚迪能否在欧洲持续增长的关键，因为在关税和本地含量规则下，从中国出口整车的成本越来越高。这一举动也意味着中国车企正在成为欧洲本土制造业的直接竞争者，将给传统车企带来压力，并可能重塑当地汽车供应链与就业格局。 四座工厂属于长期规划框架，而非立即动工的承诺，除匈牙利之外比亚迪尚未公布具体选址，也未披露投资金额。公司倾向于收购并改造现有工厂，说明其希望以更快、资本投入更低的方式获取产能，而不是新建工厂。

telegram · zaihuapd · 9月17日 11:54

**背景**: 比亚迪是全球最大的电动汽车制造商之一，近年大举拓展海外市场，但欧盟已对中国产电动车加征额外关税以保护本土产业。为降低这一成本并符合贸易规则，中国车企越来越多地在欧洲建厂或收购工厂。比亚迪的匈牙利工厂是其在欧洲的首个乘用车制造基地，也为后续更大规模的布局提供了样板。

**标签**: `#BYD`, `#electric vehicles`, `#Europe`, `#manufacturing`, `#localization`

---

<a id="item-7"></a>
## [苹果 M5 Ultra 跑分泄露：Metal 成绩超越 RTX 5090](https://browser.geekbench.com/v7/gpu/171745) ⭐️ 6.0/10

一份泄露的 Geekbench 结果显示，苹果尚未发布的 M5 Ultra 在 Metal GPU 测试中取得 360,019 分，略微超过 RTX 5090 的 OpenCL 350,160 分；而在 Vulkan 项目中，RTX 5090 以 375,290 分领先。泄露信息还提到 80 核 GPU、1.2 TB/s 内存带宽以及最高 512 GB 统一内存。 如果数据属实，这将标志着一个不同寻常的时刻：苹果的集成式 Apple Silicon GPU 已能与 NVIDIA 的旗舰消费级显卡抗衡，进一步强化苹果把大内存 Mac 定位为本地 AI 机器的策略。这也将加剧关于 Apple Silicon 能否在 AI 工作负载上真正挑战 NVIDIA 的持续争论。 这一对比本质上是跨图形 API 的：M5 Ultra 的成绩来自 Metal，而 RTX 5090 的分数来自 OpenCL 和 Vulkan，因此二者并不具备直接可比性；而且该结果只是单条 Geekbench 提交记录，尚未得到验证。对于大语言模型推理而言，512 GB 统一内存上限的意义往往超过纯 GPU 吞吐，因为显存容量常常比峰值算力更关键。

telegram · zaihuapd · 9月17日 15:20

**背景**: Geekbench 是一款专有的跨平台 CPU 与 GPU 基准测试工具，其 GPU 测试在不同平台上会调用不同的图形 API，这使得跨厂商的分数很难直接解读。Metal 是苹果为其自研芯片打造的低层图形与计算 API，而 Vulkan 和 OpenCL 则是广泛用于 Windows 和 Linux 的开放跨平台 API。苹果的统一内存架构自 2020 年随 M1 推出，让 CPU、GPU 和神经引擎共享同一个高带宽内存池，而不再像传统电脑那样把系统内存与独立显存分开，这使苹果如今能够为本地 AI 工作提供超大内存配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geekbench">Geekbench - Wikipedia</a></li>
<li><a href="https://www.amd.com/en/products/graphics/ecosystems/vulkan.html">AMD Vulkan ™ Graphics API</a></li>
<li><a href="https://grokipedia.com/page/Unified_Memory_Apple">Unified Memory (Apple)</a></li>

</ul>
</details>

**标签**: `#Apple M5 Ultra`, `#GPU benchmarks`, `#Geekbench`, `#local AI`, `#hardware leak`

---