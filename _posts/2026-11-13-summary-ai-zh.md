---
layout: default
title: "Horizon Summary: 2026-11-13 (ZH)"
date: 2026-11-13 23:04:15 +0000
lang: zh
report: ai
---

> 从 181 条内容中筛选出 10 条重要资讯。

---

1. [开发者借助 Claude Code 完成 19.4 万行 Lean4 三素数定理形式化](#item-1) ⭐️ 8.0/10
2. [马来西亚与新加坡加紧调查英伟达 AI 芯片走私案，涉 917 台服务器](#item-2) ⭐️ 7.0/10
3. [FAA 调查新 AI 技术是否导致全美航班停飞](#item-3) ⭐️ 7.0/10
4. [浙江大学与联想提出 EM²Mem：面向多模态智能体的事件中心记忆](#item-4) ⭐️ 7.0/10
5. [OpenAI 在新一轮融资中筹得 150 亿美元，投前估值达 1.25 万亿美元](#item-5) ⭐️ 7.0/10
6. [ElevenLabs 发布 Scribe v3 与 Scribe v3 Live，支持 102 种语言语音识别](#item-6) ⭐️ 7.0/10
7. [美联储调查：AI 风险是金融系统最大威胁](#item-7) ⭐️ 6.0/10
8. [ACM 博客提出面向自主 AI 系统的行动就绪契约](#item-8) ⭐️ 6.0/10
9. [洛斯阿拉莫斯国家实验室将大部分生产计算迁移至开源 OpenCHAMI](#item-9) ⭐️ 6.0/10
10. [美国战争部将 CDAO 更名为超级智能办公室](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [开发者借助 Claude Code 完成 19.4 万行 Lean4 三素数定理形式化](https://www.aibase.com/news/32317) ⭐️ 8.0/10

据报道，独立开发者 Charlie Reams 借助 Claude Code 完成了三素数哥德巴赫猜想（弱哥德巴赫猜想）的 Lean4 形式化，代码总量约 19.4 万行且不含任何 \`sorry\`，即每一步都由证明助手机器检验，而非留作未证明的占位符。报道还称，AI 在这一过程中自主发现并修复了 11 处可追溯至 13 年前的缺陷。 如果这一说法经得起独立核验，它将成为迄今规模最大的、由大模型辅助完成的形式化工程之一，也是 AI 编程智能体能够胜任真实数学验证所需工程规模的有力信号。这对 Lean4 等证明助手生态，以及数学界如何审计和信任冗长的机器检验证明，都具有重要意义。 该报道篇幅简短且来自二手新闻站点，既没有给出公开代码仓库的链接，也没有说明所用 Lean4 或 Mathlib 的版本，更缺乏独立核验，因此相关说法应视为尚未证实。还需注意，形式化是对既有论证的机器检验，而非提出新证明——其数学内核是 Harald Helfgott 2013 年的工作——而“AI 发现 11 处历史缺陷”的说法也需要审视，因为这些究竟是真正的数学漏洞，还是仅为让非形式化证明通过内核检查而补齐的缺失步骤，目前并不清楚。

aibase · AIbase · 11月13日 17:01

**背景**: 三素数哥德巴赫猜想（又称弱哥德巴赫猜想、奇数哥德巴赫猜想）断言：任何大于 5 的奇数都可以写成三个素数之和；它被称为“弱”猜想，是因为它可由更强的偶数哥德巴赫猜想推出。Harald Helfgott 于 2013 年公布了该猜想的证明，2015 年被 Annals of Mathematics Studies 系列接受发表，此后仍在持续审阅与修订。Lean4 是一门依赖类型编程语言与交互式定理证明器，证明以代码形式书写并由一个小的可信内核检查；\`sorry\` 是它的占位关键字，允许证明在某个目标未被证明的情况下通过编译——因此“零 \`sorry\`”正是“没有留下任何缺口”这一主张的关键所在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ternary_Goldbach_conjecture">Ternary Goldbach conjecture</a></li>
<li><a href="https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/">Propositions and Proofs - lean-lang.org</a></li>
<li><a href="https://lean4.dev/academy/first-proofs/plan-with-sorry">Plan a proof, then fill it in | Your first Lean proofs ...</a></li>

</ul>
</details>

**标签**: `#AI for mathematics`, `#formal verification`, `#Lean4`, `#theorem proving`, `#Claude Code`

---

<a id="item-2"></a>
## [马来西亚与新加坡加紧调查英伟达 AI 芯片走私案，涉 917 台服务器](https://news.google.com/rss/articles/CBMiowNBVV95cUxNLVRQRDJjLUYybzVveW5wWEV2cU9ka3VhQXpvV3dWN00yNS11bzBnb0VDOTNENTVFdjh0ZkdMVDF4bjYxTTFZM0s4YmlsMHFyNUZjREFSRTN2Vi1QVk9mMjNqQ3JpY2hKWGRLUFNFR3ljWl91LWQ3dXhmQlNjdnR1WkMteHV2RklKek9UMElmLWVMa3NPU21yUnJ3akNvVDFBQ05fbW1EMVVOMzloYk5YZnU4di1SZ2VlVWkzOE1iUDVJM3R1OVFfb0E3bXpBLWJiY1pDekhXWUtScUplMU9TYVRSYkxYcmRmNmJTeTdKZ2RsU3NlM3pTalVXLWdwMlU5TmZDc0EwaS1wN3E2ZThQWEtjWDRteGRWZktZNDBIbDN4XzhJckg5akw0NXJHU1hxbUpfenhPVEpQQVFDTEZjOFg4d1VTbmNXSzVsZnZQQ01NTjZsamZDb0F0dE1HaDVQRDRONDRhQzRrOXNhbVFHOHJ3YUNHbEl3TVdkamVvNTRMcnFlVXV6LXBOcmNBaWtEeFBtRkRuNWNjZ1VxWUczdFUxTQ?oc=5) ⭐️ 7.0/10

马来西亚和新加坡当局正在加大对受限英伟达 AI 芯片流向的调查力度，目前已就 917 台走私服务器对中国籍人士提起诉讼。处于这场涉及英伟达 CEO 黄仁勋争议中心的公司也宣布启动库存审计，以清点其经手的所有受限 GPU。 此案表明，美国对先进 AI 加速器的出口管制正通过东南亚的刑事起诉来落实执行，使马来西亚和新加坡这类转运枢纽成为一线的关键卡点。若执法进一步收紧，可能拖慢中国买家获取英伟达硬件的灰色渠道，并使该地区合法的云服务和数据中心业务变得更加复杂。 相关程序的核心是涉嫌在未获适当许可情况下流转的 917 台服务器，而库存审计旨在将该公司的每一块受限 GPU 的收货记录与最终去向逐一核对。此类审计正成为经手受出口管制加速器的分销商和云服务商的事实上合规要求，因为序列号对不上即使没有主观故意证据也可能引发法律责任。

google\_news · Tom&\#x27;s Hardware · 11月13日 21:45

**背景**: 自 2022 年底以来，美国逐步限制英伟达数据中心 GPU 等先进 AI 芯片对华出口，并在后续几轮中不断收紧性能门槛和许可规则。由于这类芯片性能强大、价格高昂且 AI 训练需求旺盛，常被经第三国转运，而马来西亚和新加坡是重要的转运与数据中心枢纽。当地执法机构因此展开调查，核查装有受限英伟达硬件的服务器是否存在申报不实或在缺乏出口许可的情况下被转运。

**标签**: `#Nvidia`, `#AI chips`, `#export controls`, `#semiconductor supply chain`, `#geopolitics`

---

<a id="item-3"></a>
## [FAA 调查新 AI 技术是否导致全美航班停飞](https://news.google.com/rss/articles/CBMizwFBVV95cUxPLWtSN25JZ3FqRk1BTEdGZDR2SHc2RkdsTEhBMmdQUThHcVYwTUhseVFxSG44TVlCZ2xVLUtyejFFbkJWTlZCMm92QzZIb2p1aU5hQVVmakIxZjZNZy1jaDNUbWxVQ2kwZ2NiR2tjeW4ydmYxazZlM3dBRFcyQ1pDSnliSmRFVGk1WUt3czBuTWFlRlZiTG5NSXBRSldyQVFJazFUVXdlOXdsV3ZqSk9ZVUI0V2NxRVc0TkEtRjFDLXU4Vm9WUEVFZDVBUktEREk?oc=5) ⭐️ 7.0/10

Click2Houston 报道称，美国联邦航空管理局（FAA）正在调查新引入的人工智能技术是否对一次全美范围的停飞造成了影响。给定材料仅包含标题和链接，因此涉事具体系统、时间线和调查结论尚未详细披露。 如果得到证实，全美停飞与人工智能工具相关将成为民航领域影响最大的 AI 安全事件之一，并影响航空公司、乘客以及监管机构在关键运营中部署自动化的意愿。即使因果关系尚未确认，这项调查也可能影响 FAA 对空中交通管理 AI 辅助系统的认证和监管方式。 给定条目没有说明涉事 AI 系统的名称、作用，也没有表明停飞是由该技术而非其他安全或运营问题导致。搜索结果背景显示，FAA 已部署 AI 驱动的 SMART 系统作为辅助工具，该系统“不能用于取代”空中交通管制员或接管飞机控制。

google\_news · Click2Houston · 11月13日 22:57

**背景**: 全美范围停飞是 FAA 下令暂停美国空域系统内所有航班起飞的措施，通常只在特殊安全或运营紧急情况下使用；已在空中的航班可以继续飞行。FAA 一直在扩展 AI 辅助工具（包括 SMART 系统），以帮助管理空中交通拥堵并减轻管制员工作负荷，同时强调这类工具不控制飞机。航空属于安全关键领域，AI/ML 组件在承担安全关键功能前必须经过严格的安全保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://upgradedpoints.com/news/faa-ground-stop-november-2026/">FAA Grounds All US Flights: What Travelers Can Do Right Now</a></li>
<li><a href="https://arstechnica.com/ai/2026/11/faa-expands-ai-advice-to-manage-air-traffic-congestion-across-entire-us-airspace/">FAA expands AI advice to manage air traffic ... - Ars Technica</a></li>
<li><a href="https://www.faa.gov/aircraft/air_cert/step/roadmap_for_AI_safety_assurance">Roadmap for Artificial Intelligence Safety Assurance</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#aviation`, `#FAA`, `#incident investigation`, `#critical systems`

---

<a id="item-4"></a>
## [浙江大学与联想提出 EM²Mem：面向多模态智能体的事件中心记忆](https://www.aibase.com/news/32316) ⭐️ 7.0/10

浙江大学与联想团队联合提出 EM²Mem，这是一种面向多模态智能体长期记忆的事件中心框架，并在 EMNLP 2026 上公布。该方法把传统流程反转为“先对齐、后检索”：在记忆构建阶段将异构多模态证据绑定到事件锚点，再从事件索引的记忆单元中检索。 长期记忆一直是多模态智能体的薄弱环节：它们常常在单次接触后就遗忘信息，跨模态检索效率也不高。EM²Mem 以事件作为记忆组织单位，有望保留时间与跨模态上下文，从而改善长程推理并降低智能体应用中的检索噪声。 该框架将长视频解析为事件锚点，并构建事件中心的多模态记忆单元，把局部记录、时间上下文、图关联关系和语义事实对齐在一起。不过目前公布的信息较为简略，未披露基准测试结果或实现细节，因此其相对现有记忆流程的实际收益仍待验证。

aibase · AIbase · 11月13日 16:01

**背景**: 多模态智能体需要基于随时间积累的文本、图像、音频和视频进行推理，但传统长期记忆系统往往存储彼此割裂的片段，并采用“先检索、后对齐”的流程：先取回候选记忆，再尝试将其与当前查询对齐。事件中心记忆则把“事件”这一连贯的时间单元作为锚点，将异构证据绑定在一起，使时间与因果关系更加明确。EM²Mem 将这一思路用于长视频理解和智能体记忆场景，在这些场景中，跨大量观察保留上下文至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2609.00551">Paper page - EM^2 Mem : Event - Centric Multimodal Memory for...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2609.00551">EM^2 Mem : Event - Centric Multimodal Memory for Large... | alphaXiv</a></li>
<li><a href="https://arxiv.org/html/2609.00551">EM2 Mem : Event - Centric Multimodal Memory for Large Language...</a></li>

</ul>
</details>

**标签**: `#multimodal agents`, `#long-term memory`, `#event-centric retrieval`, `#EMNLP`, `#AI research`

---

<a id="item-5"></a>
## [OpenAI 在新一轮融资中筹得 150 亿美元，投前估值达 1.25 万亿美元](https://www.aibase.com/news/32311) ⭐️ 7.0/10

据 CNBC 报道，OpenAI 完成了一轮 150 亿美元的新私募融资，投前估值达 1.25 万亿美元，明显高于此前传闻中约 110 亿美元的规模。与此同时，《华尔街日报》的数据显示，OpenAI 第三季度营收约 100 亿美元，环比增长近 50%，但经营亏损从第二季度的 101 亿美元扩大至 109 亿美元。 1.25 万亿美元的估值将使 OpenAI 成为历史上最具价值的私营公司之一，并为整个人工智能初创企业的融资定价、人才成本和基础设施投入树立标杆。营收高速增长与亏损持续扩大并存的局面，也集中暴露了 AI 行业的核心疑问：当前的算力与资本开支能否最终转化为可持续的利润。 据报道，其调整后经营利润率较约 -150% 有所收窄，说明尽管亏损绝对额在扩大，收入的增长速度仍快于亏损。上述数字来自 CNBC 与《华尔街日报》的二手报道而非经审计的财报，因此在 OpenAI 或其投资方正式确认之前，1.25 万亿美元估值以及“IPO 前夜”的说法都应谨慎看待。

aibase · AIbase · 11月13日 15:01

**背景**: OpenAI 是 ChatGPT 和 GPT 系列模型的开发公司，已从微软、软银等投资方那里筹集了数百亿美元，用于建设大规模 AI 数据中心和采购芯片。投前估值是指在新资金注入之前公司的价值，而在上市前不久完成一轮融资，可以让公司锁定资金并为 IPO 设定价格参照。由于训练和运行前沿模型需要巨额算力开支，OpenAI 目前仍处于亏损状态，这在领先的 AI 实验室中相当普遍。

**标签**: `#OpenAI`, `#AI industry`, `#venture capital`, `#financials`, `#IPO`

---

<a id="item-6"></a>
## [ElevenLabs 发布 Scribe v3 与 Scribe v3 Live，支持 102 种语言语音识别](https://www.aibase.com/news/32303) ⭐️ 7.0/10

ElevenLabs 发布了新一代语音转文字模型：面向已录制音频的 Scribe v3 和面向低延迟实时转写的 Scribe v3 Live。Scribe v3 支持 102 种语言，相较上一代将词错误率降低约 25%，并显著提升了德语识别准确率，两款模型均可通过 ElevenAPI 和 ElevenAgents 供开发者使用。 语音识别的准确率和延迟是语音智能体、会议转写和通话分析的核心瓶颈，因此一次大幅的多语言精度提升加上专门的实时模型，为开发者提供了比现有 ASR 供应商更有竞争力的选择。尤其是 102 种语言的覆盖，对必须服务非英语市场、又不想为每个地区单独维护模型的产品意义重大。 根据 ElevenLabs 的文档，Scribe v3 沿用与 Scribe v2 相同的语音转文字 API 端点（POST /v1/speech-to-text），并保留词级时间戳、说话人分离、音频标签等此前的功能，同时新增语言提示与更完善的数字格式化能力。这两款模型专门针对多人对话、抢话打断和背景噪声等更困难的场景做了优化；102 种语言的数字是在 FLEURS 基准集上测得的，而公开的模型列表标注为 90 种以上语言。

aibase · AIbase · 11月13日 11:01

**背景**: 词错误率（WER）是自动语音识别领域事实上的标准指标，它统计词级别的替换、插入和删除错误，因此相对降低 25% 意味着相比上一代模型错误大约少了四分之一。ElevenLabs 以文本转语音和声音克隆闻名，Scribe 是其语音转文字产品线，最早为 Scribe v1，如今经由 v2 升级到 v3。该公司将模型封装为面向开发者的平台：ElevenAPI 提供可直接调用的原始模型，ElevenAgents 则面向希望以最少工程量构建对话式语音智能体的团队。像 Scribe v3 Live 这样的实时版本会用一部分准确率换取低延迟，以满足实时字幕和语音智能体交互回路的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://elevenlabs.io/docs/overview/capabilities/speech-to-text">Transcription | ElevenLabs Documentation</a></li>
<li><a href="https://elevenlabs.io/docs/overview/models">Models | ElevenLabs Documentation</a></li>
<li><a href="https://huggingface.co/learn/audio-course/chapter5/evaluation">Evaluation metrics for ASR · Hugging Face</a></li>

</ul>
</details>

**标签**: `#speech-to-text`, `#ElevenLabs`, `#real-time transcription`, `#AI models`, `#developer tools`

---

<a id="item-7"></a>
## [美联储调查：AI 风险是金融系统最大威胁](https://news.google.com/rss/articles/CBMihAFBVV95cUxOd1luSGcydUl6NE15cEcydlNhSnRuNjNjVHdMQldrQjRYcXpLZ3FfbnNrWndndDNTaUowRWJ6NDg0dUdaN084LW00YU4tNEhPTXh6Ymx3WVFpZk5MQTgwVFpMX1o4cFdXT2lCQi1xSzlncG9mUkpDa0xTUF9BY2E3cXVnS2fSAYoBQVVfeXFMTmZFcVNQMElxVkdHNTFNMVBOYTg0SGVKNm5ISHM5N3pGUUxKSE5Za2ZuMmZNb3RnY0FpVWxNbWtIdXFIdm0wOWVIa3FXWVJJaVhhTHBzOVpJbzVnY2VGZk04WE5aRHVBdjdkRlVpSm1VQXo1ckRPRTV4aDNjNGJNeGlhSXZ4ZEhIa1dR?oc=5) ⭐️ 6.0/10

据 CNBC 报道，美联储的一项调查将 AI 相关风险列为金融系统面临的最大威胁。 这一发现可能促使监管机构加强对 AI 模型、第三方 AI 供应商以及银行和市场基础设施运营韧性的监管。它也表明，AI 治理正在成为金融稳定问题，而不仅仅是技术合规议题。 提供的条目仅为一个标题链接，因此内容中并未包含该调查的名称、样本、方法、时间范围以及具体被排名的 AI 风险。读者应将该排名视为监管关注度的信号，而非详细的风险评估。

google\_news · CNBC · 11月13日 21:00

**背景**: 美联储负责监测金融系统中的脆弱性，并通过调查和市场联系来评估新兴风险。在金融领域，AI 风险可能包括模型错误、不透明性、网络与欺诈暴露，以及对少数技术供应商的依赖集中。当此类风险被列为高位时，可能影响监管优先事项和金融机构的风险管理预期。

**标签**: `#AI risk`, `#financial systems`, `#regulation`, `#AI governance`, `#industry news`

---

<a id="item-8"></a>
## [ACM 博客提出面向自主 AI 系统的行动就绪契约](https://news.google.com/rss/articles/CBMiigFBVV95cUxNRjhLRkJERHlxYlRpNU5WYU9wQ1djOHFySmdFRDd1dGNyWjJNclRGYkdnQl9hVklaWHlpcnp3Y3BpZW5XNVlPWGlVYVdsZ3ZzZHM5NFhyTkFSSWJjbEVSWVA5dVlBcXh4VmpBbUtKcVhLejRIX1MwT1RoRWNDTmlXMjJZazMxN2ZwSFE?oc=5) ⭐️ 6.0/10

《Communications of the ACM》的一篇博客文章提出“行动就绪契约”（Action-Readiness Contract，ARC）：在自主系统引发外部副作用之前，立即检查一组针对具体行动、可由机器评估的证据要求。文章认为，现有数据契约主要处理数据质量与模式问题，却在 AI 系统真正采取行动的那一刻留下空白。 随着 AI 智能体从生成文本转向执行支付、调用 API 和变更基础设施，行动前的证据校验可能成为关键的治理与问责控制点。该提案把契约讨论从数据管道边界推进到执行层面，也就是自主系统可能造成现实副作用的地方。 作者明确将 ARC 定位为设计提案，而非已部署的标准，也没有声称经过性能测量。其核心思想是针对具体行动定义可由机器评估的证据要求，并在外部副作用发生前立即检查，从而把契约执行从数据管道边界前移到推理与行动时刻。

google\_news · Communications of the ACM · 11月13日 19:42

**背景**: 数据契约是数据生产方与消费方之间的正式约定，通常涵盖模式、质量阈值、语义含义、新鲜度 SLA 和访问策略。自主 AI 系统（常被称为智能体）不仅消费数据，还会据此采取行动，因此传统数据契约可能无法充分约束行动时刻的风险。《Communications of the ACM》是 ACM 出版的旗舰计算机科学刊物，其博客栏目常发表面向工程实践的观点与设计提案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cacm.acm.org/blogcacm/the-missing-data-contract-for-autonomous-ai-systems/">The Missing Data Contract for Autonomous AI Systems</a></li>
<li><a href="https://arxiv.org/html/2601.08815v2">Agent Contracts: A Formal Framework for Resource-Bounded ...</a></li>
<li><a href="https://atlan.com/know/ai-agent/data-for-ai/data-contracts-for-ai/">Data Contracts for AI: Why They Matter More Than Ever</a></li>

</ul>
</details>

**标签**: `#AI systems`, `#data contracts`, `#autonomous systems`, `#software engineering`, `#AI governance`

---

<a id="item-9"></a>
## [洛斯阿拉莫斯国家实验室将大部分生产计算迁移至开源 OpenCHAMI](https://news.google.com/rss/articles/CBMilAFBVV95cUxPODNqVzJiSnN3eXBtMXVGTFljbERPaHdMUVZTeFNKcWo0X2xiaU15cVdIOWViWEpHYVIxVWZBS1Rud0hEOVp2UUg4QjVYN0U0bUM2RE1HZElycnc3V0tYSHM5a2FOQUpzcU1rZ1ZmMWZYTk5oR2dvYThXY2ItUC0wOW1QeC0zQ0NKR2QwWHk3YUtSX1lm?oc=5) ⭐️ 6.0/10

据 ExecutiveGov 报道，洛斯阿拉莫斯国家实验室（LANL）已将大部分生产计算迁移到开源 HPC 配置与系统管理平台 OpenCHAMI 上。这一转变是在 LANL 此前已用 OpenCHAMI 部署两套 AI 生产系统的里程碑之后发生的。 一家旗舰级美国国家实验室将大部分生产负载运行在开源管理栈上，这强烈表明 OpenCHAMI 已足够成熟，可以取代专有和遗留的集群配置工具。由于 OpenCHAMI 是 Linux Foundation 旗下项目，这一采用将降低其他 HPC 站点和厂商向统一云原生管理层靠拢的门槛。 OpenCHAMI 由模块化、容器化的微服务构成，负责节点发现、配置与启动操作，为裸金属 HPC 系统带来类似云环境的灵活性。目前公开信息尚未说明 LANL 此次迁移具体覆盖哪些集群或多少节点，而 OpenCHAMI 在 SC23 上的演示被明确描述为十节点的概念验证，而非可直接用于生产的产品。

google\_news · ExecutiveGov · 11月13日 22:31

**背景**: HPC 集群历来依赖系统管理工具来完成节点发现、磁盘镜像和网络启动，过去这套工具往往是厂商专有产品与老化的开源工具拼凑而成。OpenCHAMI（Open Composable Heterogeneous Adaptable Management Infrastructure）于 2023 年作为协作联盟成立，现为 Linux Foundation 旗下项目，以可组合的微服务替代单体式配置栈。它同样归入高性能软件基金会（HPSF）旗下，HPE 等厂商也已开始推广其用于 HPC 与 AI 基础设施管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openchami.org/">OpenCHAMI : Secure, Scalable HPC System Management</a></li>
<li><a href="https://github.com/OpenCHAMI/">openchami - GitHub</a></li>
<li><a href="https://hpsf.io/projects/openchami/">OpenCHAMI – High Performance Software Foundation (HPSF)</a></li>

</ul>
</details>

**标签**: `#HPC`, `#OpenCHAMI`, `#open source`, `#systems management`, `#LANL`

---

<a id="item-10"></a>
## [美国战争部将 CDAO 更名为超级智能办公室](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQR3dGS3AyeUgxYTAzTjRxLU9hVURMS3lrM2tCdUhoUzQ3elFpdGt1Qm9KX1pPcUJTR3B6NFp5UF9zZW0yb1JMenkzdnB3SE5jeTZTYmJZS2pGRFB2TVhjbDJId1doVUpyZGJDa3NYcGw3XzY4Z2NtOVBLSHA3UkgwcVkxNVJ0VUZ6eWNKNmtHM1lXS0xCdzY2Y0dPOU91TXA2aHBwYklHcGRYcVcxWVdQRDJDOXFmaS16YjUzY0NYXy0?oc=5) ⭐️ 6.0/10

根据 war.gov 发布的公告，美国战争部已将其首席数字与人工智能办公室（CDAO）重新指定为“超级智能办公室”。这一调整发生在 2026 年 9 月一项行政命令之后，该命令在行政部门范围内用“超级智能”（SI）取代“人工智能”（AI）一词。 这一更名表明美国军方核心人工智能办公室将在“超级智能”这一新术语框架下运作，并可能影响国防人工智能政策、采购和跨部门协调的表述方式。其重要性在于，CDAO 负责推动战争部对数据、分析和人工智能的采用，因此即使核心使命不变，名称变更也可能波及相关项目和供应商关系。 目前可获得的公告仅为标题，没有公开说明该办公室的新职责、预算、领导层，也没有说明 CDAO 这一缩写和内部结构是否会改变。CDAO 于 2022 年由联合人工智能中心、国防数字服务局和分析推进办公室合并而成，目前由卡梅伦·斯坦利领导。

google\_news · U.S. Department of War \(.gov\) · 11月13日 14:03

**背景**: 首席数字与人工智能办公室（CDAO）是美国军方推动数据、分析和人工智能应用的核心机构，于 2022 年 6 月由联合人工智能中心（JAIC）、国防数字服务局和分析推进办公室合并而成。战争部是负责提供军事力量以威慑战争并保障国家安全的美国政府机构。2026 年 9 月，一项白宫行政命令要求行政部门用“超级智能”取代“人工智能”，并将该术语描述为对技术前沿进步的认可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.war.gov/">Home | U.S. Department of War</a></li>
<li><a href="https://www.whitehouse.gov/fact-sheets/2026/09/fact-sheet-president-donald-j-trump-inaugurates-the-era-of-super-intelligence/">Fact Sheet: President Donald J. Trump Inaugurates The Era of Super ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chief_Digital_and_Artificial_Intelligence_Office">Chief Digital and Artificial Intelligence Office - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#defense`, `#government`, `#CDAO`, `#organizational change`

---