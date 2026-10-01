---
layout: default
title: "Horizon Summary: 2026-10-01 (ZH)"
date: 2026-10-01 23:03:30 +0000
lang: zh
report: default
---

> 从 154 条内容中筛选出 8 条重要资讯。

---

1. [Reddit 将停用 RSS 订阅与公开 API 访问，归咎于 AI 机器人抓取](#item-1) ⭐️ 8.0/10
2. [OpenAI 瓦解模型蒸馏活动，指认与月之暗面相关人员有关](#item-2) ⭐️ 8.0/10
3. [Google DeepMind 推出 SynthID Bio，为 AI 设计蛋白质加入“水印”](#item-3) ⭐️ 8.0/10
4. [腾讯与甲骨文签署约 70 亿美元租约，租用 10 万枚 AI 芯片](#item-4) ⭐️ 8.0/10
5. [VS Code 1.140 发布：Copilot harness 支持多目录代理，HydraFusion 进入预览](#item-5) ⭐️ 6.0/10
6. [极客湾实测：麒麟 9050 Pro 接近骁龙 8 Elite](#item-6) ⭐️ 6.0/10
7. [美国国防部人事系统遭入侵，逾 300 万人信息泄露](#item-7) ⭐️ 6.0/10
8. [Cloudflare 征集面向 AI Agent 的下一代 Git 平台](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Reddit 将停用 RSS 订阅与公开 API 访问，归咎于 AI 机器人抓取](https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/) ⭐️ 8.0/10

Reddit 宣布将于 11 月 13 日停止对 RSS 订阅的支持，并将在 2027 年 3 月前关闭公开 API 访问，理由是平台遭遇大规模抓取和自动化滥用，尤其是 AI 机器人。公司建议版主迁移到 Reddit 自家托管的 Discord Relay 应用，并提醒第三方应用与机器人开发者必须在 2027 年 1 月 12 日前完成注册，否则将被切断 API 访问权限。 RSS 和公开 API 是无数第三方 Reddit 客户端、研究工具、社交聆听产品以及 AI 助手赖以运行的基础设施，停用它们意味着开放且机器可读的网络空间又少了一大块。这也为其他在“封堵 AI 抓取”与“保持开放”之间权衡的平台树立了先例，标志着 Reddit 从开放平台彻底转向受控的数据供应商。 时间表是分阶段推进的：RSS 于 11 月 13 日率先停用，第三方开发者须在 2027 年 1 月 12 日前注册，公开 API 访问则在 2027 年 3 月前终止；旧版 Reddit 的访问也被限制为仅近期登录过的用户可用。Reddit 推荐的替代方案 Discord Relay 依赖其自家托管的 Devvit 平台，把选定事件推送到 Discord——数据依然离开 Reddit，但只经由 Reddit 批准的应用程序，而大多数其他 RSS 用例并无对应的替代方案。

telegram · zaihuapd · 10月1日 00:27

**背景**: RSS（Really Simple Syndication，简易信息聚合）是一种历史悠久的标准化、机器可读的订阅格式，让用户和应用程序无需访问网站或使用专有 API 即可拉取站点更新。Reddit 的公开 API 则是让外部程序读取帖子和评论的接口，长期以来支撑着第三方客户端、学术研究、社交聆听看板以及 AI 助手。当平台声称自动化抓取的成本已难以承受时，削弱甚至关闭这些通道是常见的应对方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/">Reddit is killing RSS feeds and ending public API access because of...</a></li>
<li><a href="https://mangodeveloper.com/articles/reddit-kills-rss-and-public-api-access-cites-ai-scraping-as-the-culprit">Reddit kills RSS and public API access, cites AI scraping as the culprit</a></li>
<li><a href="https://savedelete.com/article/reddit-rss-api-shutdown/">Reddit Ends RSS and Public API: Dates and What... | SaveDelete</a></li>

</ul>
</details>

**标签**: `#Reddit`, `#API`, `#RSS`, `#AI bots`, `#platform policy`

---

<a id="item-2"></a>
## [OpenAI 瓦解模型蒸馏活动，指认与月之暗面相关人员有关](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/) ⭐️ 8.0/10

OpenAI 宣布已瓦解一起协同化的模型蒸馏活动，攻击者通过操纵交互来提取受保护的推理内容，涉及 4000 多名用户提交的约 1.6 万次请求；相关活动最早出现在 7 月初，7 月 24 日至 25 日达到高峰，到 7 月 28 日前已有超过 1.5 万名用户的相关活动被终止。OpenAI 将核心活动归因于与月之暗面（Kimi 模型开发商）有关的人员，并表示已通过 Frontier Model Forum 等渠道与业界及政府共享信息。 如果属实，这标志着 AI 知识产权与模型安全争端的一次明显升级：一家美国头部实验室公开点名与一家知名中国模型开发商有关的人员，这可能影响服务条款的执行力度、出口与政策讨论，以及未来实验室之间的相互关系。这也说明，长期处于灰色地带的模型蒸馏行为，如今正被从账号与基础设施层面主动加以管控。 OpenAI 将这一活动定性为协同操纵交互、提取受保护推理内容的行为，并把此次披露定位为与业界及政府渠道的协同行动，而非纯粹的私下法律事务。值得注意的是，公告并未披露攻击方法的技术细节，例如使用了哪些接口、账号或混淆手段，也未包含月之暗面的任何回应。

telegram · zaihuapd · 10月1日 01:18

**背景**: 模型蒸馏通常指训练一个更小或更廉价的模型去模仿更强的模型；而在攻击语境下，它指的是反复查询某个专有模型，并利用其输入输出对来训练竞争模型，从而无需承担原始训练成本。由于前沿模型需要巨额算力、数据和专业能力，非法获取输出结果可以让攻击者省去大部分投入。蒸馏之所以难以监管，是因为支撑正常应用的大量 API 调用与提取行为在数据上十分相似；而 Frontier Model Forum 是一个由行业支持的非营利组织，主要实验室通过它共享安全与安保信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@tahirbalarabe2/understanding-llm-distillation-attacks-929306ca38cd">Understanding LLM Distillation Attacks | by Tahir | Oct, 2025 | Medium</a></li>
<li><a href="https://www.penligent.ai/hackinglabs/model-distillation-attack/">Model Distillation Attack : How Illicit Distillation Steals LLM...</a></li>
<li><a href="https://www.frontiermodelforum.org/">Frontier Model Forum</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#model-distillation`, `#AI-security`, `#Moonshot-AI`, `#AI-industry-news`

---

<a id="item-3"></a>
## [Google DeepMind 推出 SynthID Bio，为 AI 设计蛋白质加入“水印”](https://arstechnica.com/science/2026/09/google-figures-out-how-to-watermark-ai-designed-proteins/) ⭐️ 8.0/10

Google DeepMind 于 2026 年 9 月 30 日发布 SynthID Bio，这是一组水印方法，可向 AI 设计的蛋白质氨基酸序列以及 AI 预测的三维结构中嵌入可检测的标记。在蛋白质设计实验中，研究人员把水印与逆折叠模型 ProteinMPNN 结合，只有当水印建议的氨基酸不影响蛋白质功能时才采纳它们。 该方法为合成生物学增加了一层“来源可追溯”能力：开发者与 DNA 合成厂商可以核查某个序列是否来自可信的 AI 设计流程，而非来源不明的产物。由于 AI 生成的蛋白质设计可能绕过基于相似性的生物安全筛查，SynthID Bio 被定位为 AI 时代生物安全纵深防御体系中的一层保障。 Google DeepMind 称实验中带水印的蛋白质仍能与目标蛋白结合，检测效果也较好；在结构预测方面，它微调了 AlphaFold 3 扩散网络的局部，使水印写入模型权重，从而无论由谁运行该模型都能保留可检测特征。局限依然存在：目前只验证了特定设计流程和少数目标，短蛋白质、其他设计工具以及人为去除或稀释水印仍是待解问题。关键在于，SynthID Bio 是一种来源验证工具，而不是能够自行判断蛋白质是否有害的检测器。

telegram · zaihuapd · 10月1日 03:40

**背景**: 像 ProteinMPNN 这样的蛋白质设计模型解决的是“逆折叠”问题：给定一个固定的三维蛋白质骨架，预测能够折叠成该骨架的氨基酸序列；而 AlphaFold 类模型则相反，从序列预测结构。SynthID 是 Google DeepMind 已有的隐形水印技术家族，此前用于图像、文本、音频和视频；SynthID Bio 把这套思路延伸到了生物序列与结构上。其动因是：AI 工具如今能够生成编码危险蛋白质的 DNA，而依赖与已知威胁序列相似度比对的传统生物安全筛查可能漏检。水印无法阻止滥用，但有助于把设计追溯到可信来源，并标记出未加标签的 AI 生成序列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/introducing-synthid-bio/">SynthID Bio : Watermarking methods for... — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synthid-bio/">SynthID Bio watermarks AI-designed proteins</a></li>
<li><a href="https://www.unite.ai/deepmind-embeds-verifiable-watermarks-in-ai-designed-proteins/">DeepMind Embeds Verifiable Watermarks in AI - Designed Proteins</a></li>
<li><a href="https://www.npr.org/2025/10/02/nx-s1-5558145/ai-artificial-intelligence-dangerous-proteins-biosecurity">AI designs for dangerous DNA can slip past biosecurity ... : NPR</a></li>

</ul>
</details>

**标签**: `#AI biosecurity`, `#protein design`, `#watermarking`, `#DeepMind`, `#SynthID`

---

<a id="item-4"></a>
## [腾讯与甲骨文签署约 70 亿美元租约，租用 10 万枚 AI 芯片](https://www.ft.com/content/8799b33d-f07c-4a03-82f0-bf5d3d1d29e9) ⭐️ 8.0/10

腾讯与甲骨文签署了一份为期五年、价值约 70 亿美元的租约，租用约 10 万枚无法在中国境内直接购买的先进 AI 芯片，成为腾讯迄今规模最大的海外租赁交易。相关算力覆盖东南亚多个数据中心，主要用于加速腾讯的 AI 模型与智能体（AI Agent）工具开发，其中约 30%的款项需要预付。 这笔交易表明，中国头部科技公司正通过海外算力租赁来绕开美国的出口管制，继续训练和部署前沿模型，实际上把数十亿美元的 AI 基础设施支出转向境外。它也让甲骨文这类云厂商在 AI 芯片地缘政治中扮演起中间人角色，并可能促使美国监管机构重新审视并收紧这一租赁通道。 按照目前披露的条款，约 70 亿美元中约 30%需要预付，租用的算力分布在东南亚多个数据中心而非单一站点。这一安排利用了美国规则中的一处空隙：规则禁止中国企业直接购买先进芯片，却并未禁止它们在海外租用同等算力。

telegram · zaihuapd · 10月1日 05:07

**背景**: 自 2022 年 10 月起，美国逐步限制向中国出口英伟达高端数据中心 GPU 等先进 AI 加速芯片，并在 2023 年以及 2024 年末进一步收紧规则，把更多半导体制造设备、软件工具和高带宽内存（HBM）纳入管制范围。由于中国企业仍可合法租用境外云端算力，像甲骨文云基础设施（Oracle Cloud Infrastructure）这样提供 GPU 算力的服务商，就成了间接获得同类硬件的途径。腾讯自研混元系列大模型和 AI 智能体工具，二者都高度依赖大规模 GPU 训练与推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jiuyangongshe.com/a/gc8k77lmwl">美 国 本周将发布 对 华 AI 芯 片 新限 制 ，中 国 院士：需构建 国 产万算力卡系统</a></li>
<li><a href="https://www.betteryeah.com/blog/harness-engineering-vs-ai-agent-difference-connection-analysis">Harness 工 程和 Agent 区别联系：企业级 智 能 体 控制系统深度解析</a></li>
<li><a href="https://baoyu.io/translations/a-mental-model-for-agentic-ai-applications">与 智 能 体 交朋友： AI 智 能 体 （Agentic AI ）应用的心 智 模型 | 宝玉的分享</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Tencent`, `#Oracle`, `#export controls`, `#cloud computing`

---

<a id="item-5"></a>
## [VS Code 1.140 发布：Copilot harness 支持多目录代理，HydraFusion 进入预览](https://code.visualstudio.com/updates/v1_140) ⭐️ 6.0/10

Visual Studio Code 1.140 引入了新的 Copilot harness，允许单一代理会话同时操作多个文件夹，并能把任务委托给远程代理主机执行；同时推出 HydraFusion 多模型编排的研究预览。该版本还支持跨 worktree 复用被忽略的文件夹，改进了 Dev Container 与会话管理，并新增企业 AI 版本要求以及 Auto 模型默认层级的控制。 这表明代理式编程正在从「单文件夹、单模型」的助手，转向代理可覆盖整个代码库、并在多个模型之间分配任务的编排式工作流。对于在大型 monorepo 或多根项目中使用 Copilot 的团队来说，harness 与 HydraFusion 预览会直接影响成本、延迟，以及开发流程中有多少环节可以在编辑器内实现自动化。 具体细节记录在 VS Code 1.140 的发布说明中，其中 Copilot harness 被定位为位于代理配置与底层推理模型之间的运行时层。HydraFusion 被明确标注为研究预览，因此其多模型路由行为仍属实验性质而非生产级稳定：根据检索结果，它先用便宜模型起草、在困难步骤上升级到更强模型，并在多个模型家族之间交叉审查。

telegram · zaihuapd · 10月1日 09:33

**背景**: VS Code 大致每月发布一个版本，因此每个版本更像是功能的渐进式汇总，而非平台级的大变革。「代理 harness（agent harness）」指的是介于代理配置、工具与提示词之间、为代理提供推理能力的 AI 模型所处的运行时环境；目前 VS Code 支持 Local、GitHub Copilot、Anthropic Claude 和 OpenAI Codex 等 harness，还提供用于远程运行代理的 Cloud 目标。多模型编排指把一个任务的不同部分动态路由到不同的 LLM，以在成本、延迟和推理深度之间取得平衡，而不是全程绑定单一模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.visualstudio.com/docs/agents/run/agent-harnesses">Choose and use an agent harness</a></li>
<li><a href="https://www.datastudios.org/post/github-launches-hydrafusion-multi-model-orchestration-dynamic-routing-lower-cost-coding-and-the">GitHub Launches HydraFusion : Multi - Model Orchestration , Dynamic...</a></li>
<li><a href="https://www.creativeainews.com/articles/github-copilot-hydrafusion-multi-model-2026/">Copilot HydraFusion : Multi - Model Orchestration</a></li>

</ul>
</details>

**标签**: `#VS Code`, `#GitHub Copilot`, `#AI Agents`, `#Multi-Model Orchestration`, `#Developer Tools`

---

<a id="item-6"></a>
## [极客湾实测：麒麟 9050 Pro 接近骁龙 8 Elite](https://www.bilibili.com/video/BV1fHaB6WEh1/) ⭐️ 6.0/10

极客湾对华为 Mate XT 2 搭载的麒麟 9050 Pro 进行了实测，GeekBench 7 单核得分 1813、多核得分 8159，NPU 实测达到 67.7 TOPS。测试称该芯片在 CPU、GPU、NPU 三方面均有提升，且在《原神》《异环》《鸣潮》等游戏中，Mate XT 2 的表现已接近搭载骁龙 8 Elite 的三星三折叠机型。 如果这些数据成立，意味着华为在制造工艺受限的情况下，仍把旗舰级性能差距缩小到了接近高通顶级 Android 芯片的水平，这对中国高端手机市场和华为维持 Mate 系列在游戏与端侧 AI 场景中的竞争力意义重大。这也顺应了国产厂商把 NPU 的 TOPS 数值作为端侧 AI 卖点的整体趋势。 报道强调该芯片在制造工艺和微架构上基本没有明显变化，因此性能提升更像是调优而非新制程或核心重设计的结果；同时这只是通过 Telegram 频道转述的单机测试数据，并未经独立验证。像 67.7 TOPS 这样的数值还高度依赖所用的数值精度（例如 INT8 与 FP16 的差别），缺少这一前提时不同厂商之间的数据无法直接比较。

telegram · zaihuapd · 10月1日 11:50

**背景**: 麒麟 9050 Pro 是华为自研 Kirin 系列手机 SoC 的最新产品，而骁龙 8 Elite 是高通当前的旗舰移动平台，也是 Android 手机性能的常见参照标准。极客湾是国内知名的硬件评测频道，其跑分视频在华语科技圈中被广泛引用。NPU（神经网络处理单元）是专门加速 AI 与机器学习负载的处理器，而 TOPS（每秒万亿次运算）是用于宣传其算力的常用指标。微架构指的是某一指令集在芯片上的具体实现方式，这也是芯片在未更换制程节点的情况下仍能提升性能的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://d33gy59ovltp76.cloudfront.net/news/what-is-tops-and-why-is-it-important-for-ai">What is TOPS and why is it important for AI?</a></li>
<li><a href="https://www.prodigitalweb.com/what-is-an-npu-neural-processing-unit/">What Is An NPU ? Neural Processing Unit Explained 2026</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microarchitecture">Microarchitecture</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Kirin 9050 Pro`, `#Snapdragon 8 Elite`, `#mobile SoC`, `#benchmarks`

---

<a id="item-7"></a>
## [美国国防部人事系统遭入侵，逾 300 万人信息泄露](https://www.techspot.com/news/114056-pentagon-data-breach-exposed-data-more-than-3.html) ⭐️ 6.0/10

美国国防部披露，国防人力数据中心（DMDC）的一套系统在 2025 年 10 月至 2026 年 7 月期间遭未授权访问，受影响人数约 306 万，其中约 276 万为在世人士、29.4 万为已故人士。国防部称，被暴露的信息包括社会安全号码（SSN）和任职/服役信息。 社会安全号码是美国身份验证体系的核心，一旦数百万现役与退役军人、文职雇员、承包商及军属的 SSN 泄露，将带来长期的身份盗用与金融欺诈风险。而入侵行为在长达约九个月的时间里未被发现，也令外界对国防部的安全监测与检测能力提出严重质疑。 国防部表示已修补相关漏洞，目前尚未发现数据被滥用的证据，并正向受影响者提供身份保护和信用监测服务。但该部门并未公布入侵者如何进入系统、实际被查看或窃取的数据量，以及漏洞为何在九个月内未被察觉。

telegram · zaihuapd · 10月1日 14:16

**背景**: 国防人力数据中心（DMDC）隶属于美国国防部长办公室，负责汇总美军的人事、兵力、训练和财务等各类数据。它保存个人的服役状态记录，包括服役开始与终止日期，也是《军人公民救济法》（SCRA）资格核验等信息的重要来源。由于该中心汇总了现役与退役人员、文职雇员、承包商及军属等多类人群的记录，一旦被攻破，可能同时波及数百万人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Defense_Manpower_Data_Center">Defense Manpower Data Center - Wikipedia</a></li>
<li><a href="https://www.servicememberscivilreliefact.com/about-us/defense-manpower-data-center/">Defense Manpower Data Center ( DMDC ) - SRCA Centralized...</a></li>
<li><a href="https://govfacts.org/government/federal/agencies/defense/verifying-military-service-the-complete-guide-to-scra-and-dmdc-resources/">Verifying Military Service: The Complete Guide to SCRA and DMDC ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data-breach`, `#government`, `#privacy`, `#defense`

---

<a id="item-8"></a>
## [Cloudflare 征集面向 AI Agent 的下一代 Git 平台](https://blog.cloudflare.com/next-git-platform-on-cloudflare/) ⭐️ 6.0/10

Cloudflare 公开征集开发者，基于 Cloudflare Workers 和刚进入公开 Beta 阶段的 Artifacts 服务，构建面向 AI Agent 协作的下一代 Git 平台。参赛者需在 2026 年 10 月 14 日截止日期前提交 5–10 分钟的演示视频、以 MIT、Apache 或 BSD 等宽松许可证发布的源代码以及运行说明，第一名团队可获得 25,000 美元 Cloudflare 点数。 这一竞赛释放出一个信号：长期以来为人类开发者异步协作而优化的 Git 版本控制，可能需要围绕以机器速度读取、修改和合并代码的自主 Agent 重新设计。如果这一方向获得关注，可能会影响整个开发者工具生态如何处理多 Agent 并行、自动化代码审查与上下文管理。 Artifacts 提供可编程、支持 Git 操作的版本化仓库，开发者可以在此基础上自行设计多 Agent 并行开发、代码审查、变更合并与上下文管理等功能。值得注意的是，参赛并不要求交付完整可用的产品，评审重点在于演示视频和以宽松许可证发布的开源代码。

telegram · zaihuapd · 10月1日 14:57

**背景**: Git 是几乎所有软件团队都在使用的分布式版本控制系统事实标准，而 GitHub 等平台则托管仓库并提供拉取请求等协作流程。Cloudflare Workers 是 Cloudflare 的无服务器平台，可在其全球边缘网络上运行代码，并能从零自动扩展到数百万请求规模。Artifacts 目前处于公开 Beta 阶段，是 Cloudflare 为大规模场景打造的、兼容 Git 的版本化存储层，可创建数千万个仓库并从任意远程仓库 fork，任何 Git 客户端只要拿到 URL 即可使用。本次竞赛要求开发者把这些基础能力组合起来服务于 AI Agent——即能够自主编写和修改代码的程序——而不是服务于人类贡献者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/products/artifacts/">Cloudflare Artifacts - Versioned Git-compatible storage for agents</a></li>
<li><a href="https://developers.cloudflare.com/artifacts/">Artifacts · Cloudflare Artifacts docs</a></li>
<li><a href="https://www.cloudflare.com/products/workers/">Cloudflare Workers - Global Serverless Functions Platform</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#Git`, `#AI Agents`, `#Developer Tools`, `#Contest`

---