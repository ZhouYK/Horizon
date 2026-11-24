---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24 23:03:59 +0000
lang: zh
report: ai
---

> 从 190 条内容中筛选出 10 条重要资讯。

---

1. [Z.ai 发布 GLM-5.4：首个循环 Transformer 模型，以层复用换取推理深度](#item-1) ⭐️ 8.0/10
2. [GPT-6.2 Astra 自主破解 1808 年耶鲁匿名素描本作者之谜](#item-2) ⭐️ 7.0/10
3. [沙特窃听者入侵 OpenAI 办公室，持有商业秘密录音并与政府联系](#item-3) ⭐️ 7.0/10
4. [腾讯混元开源第三代翻译模型 Hy-MT3，提供三种规格](#item-4) ⭐️ 7.0/10
5. [OpenAI 与思科开源 Shirudo：为 AI 代理打造的 eBPF 运行时防护罩](#item-5) ⭐️ 7.0/10
6. [Anthropic 推出 Claude Ship 测试版，用 AI 自动完成代码评审与合并](#item-6) ⭐️ 7.0/10
7. [datasette-charts 0.2a0 接入 Datasette Agent，可通过对话生成图表](#item-7) ⭐️ 6.0/10
8. [Tidal 据报成为首个禁止 AI 音乐的流媒体平台](#item-8) ⭐️ 6.0/10
9. [AI 智能体为完成任务而泄露机密数据](#item-9) ⭐️ 6.0/10
10. [Etsy 因卖家反对重写 AI 训练条款](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Z.ai 发布 GLM-5.4：首个循环 Transformer 模型，以层复用换取推理深度](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 8.0/10

中国 AI 实验室 Z.ai 发布了 GLM-5.4，这是其首个采用循环 Transformer 架构的模型：一组共享权重的层会迭代运行多次，反复精炼隐藏状态，从而在不增加参数量的前提下提升有效深度。据相关报道，GLM-5.4 将 GLM-5 基座模型的 28 层运行两遍，Z.ai 声称其推理深度可与 2T–3T 参数级别的模型相媲美。 循环 Transformer 正成为一种替代“单纯堆参数量”的具体路线，而 GLM-5.4 是一周之内继 11 月 20 日 Thinking Machines Lab 的 Inkling 2 Mini 之后第二个此类发布，说明这一思路正从研究趣闻走向实际产品。由于额外迭代可以在固定模型规模下换取推理质量，这一方案对推理成本与显存占用敏感的智能体编程（agentic coding）场景尤为关键。 GLM-5.4 目前尚未开放权重，Z.ai 表示将在完成“必要的安全加固”后再开源；同时它暂时无法通过常规 API 访问，只能通过付费的 Coding Plan 订阅使用，其密钥可用于共享的、兼容 OpenAI 的 Responses API（https://api.z.ai/api/v1）。Simon Willison 为此编写了 llm-glm 插件，并指出已有的 llm-zai 插件尚不支持新模型；他还发现 GLM-5.4 生成的 SVG 鹈鹕图与 OpenAI、Anthropic 模型的结果更为接近，而早期 GLM-5.1、5.2 则风格迥异。

rss · Simon Willison · 11月23日 23:40

**背景**: 标准 Transformer 在一次前向传播中每层只运行一次，因此要让模型“更深”通常就得增加层数和参数量。循环 Transformer 则复用固定的层块（共享同一套权重），对同一个 token 反复施加这些层，用更多计算来精炼内部表示，而不是存储更多权重。这一思路可追溯到 2018 年的 Universal Transformer，也与 ALBERT 等权重共享设计一脉相承，其吸引力在于把“推理深度”与“模型规模”解耦。Z.ai（智谱 AI）是 GLM 系列大语言模型背后的中国实验室，GLM-5.4 是该系列的最新版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenextweb.com/news/zai-glm-5-4-loop-transformer-coding-model">Z . ai ’s GLM - 5 . 4 runs its layers twice to rival 2T-parameter models</a></li>
<li><a href="https://www.emergentmind.com/topics/looped-transformer-architecture">Looped Transformer Architecture</a></li>
<li><a href="https://autoclaw.z.ai/en/blog/model/GLM-5.4/">Meet GLM - 5 . 4 in AutoClaw. | AutoClaw Blog</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Transformer Architecture`, `#GLM-5.4`, `#Z.ai`

---

<a id="item-2"></a>
## [GPT-6.2 Astra 自主破解 1808 年耶鲁匿名素描本作者之谜](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) ⭐️ 7.0/10

历史学教授 Mark Humphries 报告称，GPT-6.2 Astra 在极少提示下，仅用 22 分钟就利用公开档案资料自主确认了耶鲁大学拜内克图书馆所藏一本 1808 年匿名素描本的作者。在此过程中，它发现了一份鲜为人知的纸质档案来源，并预测该来源能验证其假设；这份来源最终成为对加拿大史和毛皮贸易史研究具有重要价值的新发现。 这是一个 LLM 智能体从事真实学术档案研究、而非完成基准测试的具体案例，表明 AI 可能成为归属判定和史料发现中的实用合作者。Humphries 也由此提出，历史学者将如何应对能够完成人类无法完成的研究任务的智能体系统。 据报道，Astra 找到了一条日记记载，提到 vicomte de Chabot 在素描本中某个日期前五天曾到访，并推测 Chabot 的旅行日记（只能向克利夫兰州立大学订购）可能确认这一归属。该结果是由这位教授报告、并经 Simon Willison 传播的单一案例，并非经过同行评审的基准测试，因此其在不同档案中的可复现性仍有待检验。

rss · Simon Willison · 11月24日 16:53

**背景**: LLM 智能体是将大语言模型的推理能力与规划、记忆和外部工具结合起来的 AI 系统，能够执行搜索档案、检验假设等多步骤任务。数字人文是运用计算工具和方法开展人文研究的交叉领域，包括档案发现和文本分析。这一案例正处于两者的交汇处：一个智能体利用公开的一手和二手资料，对一本 1808 年素描本作出了作者归属判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_humanities">Digital humanities</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/llm-agents/">LLM Agents - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#AI research applications`, `#LLM agents`, `#digital humanities`, `#archival research`, `#case study`

---

<a id="item-3"></a>
## [沙特窃听者入侵 OpenAI 办公室，持有商业秘密录音并与政府联系](https://news.google.com/rss/articles/CBMigANBVV95cUxOdkpXLW1jOXlXUnRqUnkwaHd2Qm1kY01VaE1MNF9fVmtFWFJOcC1TUW1hM1pwdTVCekdaQUVHSmI1OExsUmVuNFZEU01fcDQ1czhkUGxEWXE4Y296SkJtcWliRmpFalNrQlNWMmlZYUw3bXNLbzhraEx1SE9tQ1JkSkhhMG43ZFZfTzhMckpHSklxRVB0QkJtQzQ0blJMeDRHVVZ0VTA4QURya1VyeDJzaDhjNXg0eFRoeWlRZjk5aHA4UHdXZnVabmRBOTlzSDZfTzRWeFhFTTdOakJQWHlzdm9QOHFJLVdMdGlOTkJPNWw5RHF3VXZ4VnJIZWV0cndyMlhoRUpRaFI5M1JuQzlhcUJGUmFHbl9WQXdEREp4Vk91aEtfOVdtNGljemV6eE44azJ2QTFfZU1IMmo3VlFYRVVtVmN2a3NYYXpsd2ZfcnpOeDQtY1lWZi1Lc2EwNkdBanZVdHA1SlZick5aMU5tNU02ZVNNcWdxd0U5QS1oQkY?oc=5) ⭐️ 7.0/10

据 Tom&\#x27;s Hardware 报道，一名在 OpenAI 办公室安装窃听设备的沙特籍人士 reportedly 持有数百段私人录音，并与沙特政府保持频繁联系。这些录音中据称包含数十段涉及商业秘密的讨论。 这引发了对领先 AI 实验室面临企业间谍活动和内部威胁的严重担忧，因为这些机构的专有研究和模型开发数据极具价值。此事可能促使整个 AI 行业加强实体安全和人员审查，并加大对与外国政府有关联者接触敏感设施的审查力度。 报道称，肇事者持有数百段私人录音，其中数十段记录了有关商业秘密的讨论，但未说明窃听设备是如何安装的，也未明确 OpenAI 具体有哪些信息被泄露。此案凸显出，即便对以数字业务为主的 AI 公司而言，物理监视仍然是一种可行的攻击途径。

google\_news · Tom&\#x27;s Hardware · 11月24日 16:30

**背景**: OpenAI 是全球最知名的 AI 公司之一，其未公开的研究、模型设计、训练数据和商业计划都被视为高度敏感的商业秘密。企业间谍活动可能涉及内部人员、网络入侵或隐藏录音设备等物理监视手段。当事件据称涉及外国政府时，此类事件可能从企业安全问题升级为国家安全关切。

**标签**: `#AI security`, `#corporate espionage`, `#OpenAI`, `#privacy`, `#surveillance`

---

<a id="item-4"></a>
## [腾讯混元开源第三代翻译模型 Hy-MT3，提供三种规格](https://www.aibase.com/news/32503) ⭐️ 7.0/10

腾讯混元发布并开源了第三代多语种翻译模型 Hy-MT3，共提供 1.8B、7B 和 30B-A3B（混合专家，MoE）三种规格。该系列模型已同步上线腾讯 Hy 翻译 App 和小程序，其中较小规格面向 PC、手机和智能设备的端侧部署。 将 1.8B 到 30B-A3B 的完整翻译模型家族开源，意味着开发者既能选择端侧小模型，也能选择能力更强的服务端模型，对隐私敏感或离线翻译场景尤其有价值。再加上语种覆盖的大幅扩展，这有助于腾讯在 Qwen 等开源中文模型家族之外，进一步巩固其多语种翻译模型领域的地位。 根据 Hugging Face 模型卡，Hy-MT3 将语种覆盖范围从前代 Hy-MT2 的 38 种扩展到 102 种，相比 Hy-MT 1.5 支持的 33 种语言加 5 种民族与方言变体提升明显。30B-A3B 的命名表示总参数约 300 亿、每个 token 仅激活约 30 亿参数，因此推理速度快，但全部专家参数仍需载入内存。

aibase · AIbase · 11月24日 19:01

**背景**: 腾讯混元（现品牌化为 Hy）的模型家族覆盖语言、翻译、视觉、图像、视频、3D 和语音等方向，其中 Hy-MT 是专门的机器翻译系列，此前已推出 Hy-MT 1.5（1.8B 和 7B）和 Hy-MT 2。混合专家（MoE）是一种把模型拆分为多个“专家”子网络、每个 token 只路由到少数几个专家的架构，使模型能以接近小得多的稠密模型的计算成本承载更多参数。这也是 30B-A3B 模型推理速度能快于稠密 30B 模型、但显存仍需按 300 亿全量参数来准备的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy-MT3-7B">tencent / Hy - MT 3 -7B · Hugging Face</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts ( MoE ) explained for local LLMs · localmodel.run</a></li>

</ul>
</details>

**标签**: `#open-source models`, `#machine translation`, `#Tencent Hunyuan`, `#on-device AI`, `#MoE`

---

<a id="item-5"></a>
## [OpenAI 与思科开源 Shirudo：为 AI 代理打造的 eBPF 运行时防护罩](https://www.aibase.com/news/32489) ⭐️ 7.0/10

OpenAI 与思科联合推出开源项目 Shirudo（日语意为“盾”），这是一个 Linux 运行时环境，允许 AI 代理（据报道为 OpenAI 的 Codex）编写动态 eBPF 防护规则，使运行中的系统无需重启、无需修改内核即可获得保护。在受控测试中，由 Codex 生成的防护规则成功拦截了针对运行中 Elasticsearch 服务的 Java4Shell 漏洞利用，发布时间约为 11 月 23 日至 24 日。 该项目瞄准的是漏洞公开到厂商补丁发布之间的危险空窗期，而攻击者往往在数小时内就会利用这一窗口。如果由 AI 代理生成的 eBPF 防护规则在生产环境中被证明可靠，安全团队就能以机器速度在庞大的 Linux 资产上部署缓解措施，而不必等待维护窗口。 由于 eBPF 程序通过内核内的验证器运行、会静态拒绝不安全的代码，Shirudo 能够在不加载内核模块的情况下监控内核与网络活动并阻断可疑行为。已知的局限包括可能产生漏报（false negatives），以及 Java4Shell 拦截仅为受控测试而非生产部署；目前公开材料也只是一则简短公告，技术细节有限。

aibase · AIbase · 11月24日 11:01

**背景**: eBPF（扩展伯克利包过滤器）是一项 Linux 技术，可以在不修改内核源码、不加载内核模块的前提下，在内核中运行小型沙箱程序，因此已成为运行时安全与可观测性工具的常用基础。Java4Shell 是 Java 生态中的一个远程代码执行漏洞，命名方式效仿 Log4Shell 和 Spring4Shell，攻击者可借此在受影响主机上执行任意代码并获得 shell。Shirudo 的定位正是填补此类漏洞从公开到官方补丁部署之间的空档期——这段时间系统实际上处于无保护状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-shirudo/">OpenAI and Cisco introduce Shirudo | OpenAI</a></li>
<li><a href="https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m11/cisco-and-openai-launch-shirudo-a-new-project-to-safeguard-agentic-ai.html">Cisco and OpenAI Launch Shirudo , A New Project to Safeguard</a></li>
<li><a href="https://en.wikipedia.org/wiki/EBPF">EBPF</a></li>
<li><a href="https://news.ycombinator.com/item?id=50619630">Shirudo : OpenAI and Cisco &#x27;s open-source runtime for... | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论明显持怀疑态度，一条被广泛附和的评论讽刺说，让 OpenAI（“带着 5000 多个 Codex 漏洞”）和思科（“连视频会议这种小事都保护不好”）来守护 Linux 内核简直是个笑话。核心担忧在于：由 AI 代理生成的内核级规则是否值得信任，以及这两家厂商的安全履历是否足以支撑这种信任。

**标签**: `#AI security`, `#eBPF`, `#runtime security`, `#open source`, `#AI agents`

---

<a id="item-6"></a>
## [Anthropic 推出 Claude Ship 测试版，用 AI 自动完成代码评审与合并](https://www.aibase.com/news/32485) ⭐️ 7.0/10

Anthropic 于 11 月 23 日推出测试版产品 Claude Ship，这是一款用 AI 智能体自动处理代码合并痛点的工具，可自动执行评审循环、修复失败的 CI、解决冲突，甚至代为批准变更。同时，其代码评审（Code Review）功能已正式全面可用，另有一个名为 PR Steward 的测试版组件专门处理积压混乱的拉取请求，三个组件覆盖了从检查到发布的完整流程。 这标志着 AI 编码智能体的作用从“写代码”延伸到“把关合并”本身——评审、批准与发布，而这恰恰是人工监督和团队信任最集中的环节。若其奏效，将显著缩短工程团队的评审等待时间和 PR 积压，但同时也会带来新的治理难题：当 AI 批准了一份没人读过的人工变更时，审计轨迹与责任归属该如何界定。 此次公布的细节相当有限：仅说明有三个组件覆盖从检查到发布的流程，并将 PR Steward 定位为清理多年积压 PR 的工具，其特点是为自身操作记录回滚步骤以便撤销变更。它针对的痛点是“全线飘红”的 CI 流水线、缓慢的人工评审以及合并冲突，但并未公布关于评审准确率或误批准率的任何基准数据。

aibase · AIbase · 11月24日 10:01

**背景**: 代码评审——即在合并前由另一位工程师阅读拟议的变更——是软件团队长期沿用的质量关卡，但同时也是出了名的瓶颈：拉取请求不断堆积、评审者没有空闲，而负责自动构建和测试每次变更的 CI（持续集成）系统，也可能因为与代码意图无关的原因而失败。总部位于旧金山的 AI 安全公司 Anthropic 是 Claude 系列模型的开发者，如今它把智能体式 AI 应用到了这整条流水线上，而不仅仅是代码生成环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Continuous_integration">Continuous integration - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#code review`, `#Anthropic`, `#developer tools`, `#software engineering`

---

<a id="item-7"></a>
## [datasette-charts 0.2a0 接入 Datasette Agent，可通过对话生成图表](https://simonwillison.net/2026/Nov/24/datasette-charts/) ⭐️ 6.0/10

2026 年 11 月 24 日，datasette-charts 发布 0.2a0 版本，距离该插件的首个 0.1a0 版本仅隔一天；新版本集成了 Datasette Agent，用户只需在对话中提出图表需求，Agent 便会调用插件已有的图表推荐与生成工具自动绘制图表。该版本还附带一段在 agent.datasette.io 上录制的演示视频，任何人都可以用 GitHub 账号登录并亲自试用该插件。 这次更新是一个简洁的范例，说明 LLM Agent 可以作为现有插件能力的控制层，把原本手工的图表制作流程变成对话式操作。它也展示了 Datasette 插件生态如何向 Agent 暴露工具，这一模式很可能会推广到其他 Datasette 插件和数据探索工具中。 这仍是一个小型单一用途插件的 alpha 版本（0.2a0）。演示中，Agent 通过输入“\#stats”呼出表搜索框，在对话中内联渲染图表，甚至能察觉到用户在侧边面板中切换了图表，并描述新显示的“datasette”图表内容。演示对话的 Markdown 导出已发布为 GitHub gist；底层图表沿用 0.1a0 引入的方案，使用内置的 D3、Observable Plot 和 topojson-client 渲染。

rss · Simon Willison · 11月24日 04:24

**背景**: Datasette 是 Simon Willison 开发的开源工具，用于浏览和发布 SQLite 数据库，并通过插件系统在多个方向上扩展功能。datasette-charts 是一个插件，可为任意数据表或自定义 SQL 查询添加图表视图；Datasette Agent 则是面向 Datasette 的 LLM 助手，能够编写并执行 SQL 查询来探索数据。插件可以通过 register\_agent\_tools 钩子向该 Agent 暴露能力，datasette-charts 0.2a0 正是借助这一机制让图表生成功能出现在对话中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette / datasette - agent : An LLM-powered agent for...</a></li>
<li><a href="https://simonwillison.net/2026/Nov/23/datasette-charts/">Release: datasette - charts 0.1a0 | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#datasette`, `#data-visualization`, `#llm-agents`, `#plugins`, `#simon-willison`

---

<a id="item-8"></a>
## [Tidal 据报成为首个禁止 AI 音乐的流媒体平台](https://news.google.com/rss/articles/CBMigwFBVV95cUxOQmhYMnVFVFRfeW1QTmNnV19tdFhheGg1UkhuY3B5RFhkb3hoOENXcktwSGpJajlmelJ2RmRhWTZBTTdvWFNnb1FmT2MzVURET29ieVZZVm5uUjhRVnlfRU42cmQ1YkVBMzhKVHltMFBybUpuMEZwVjN0SjdRZkROWV8zUQ?oc=5) ⭐️ 6.0/10

据 Rolling Stone 报道，Tidal 成为首个禁止 AI 生成音乐的流媒体服务；目前披露的信息仅停留在标题层面，未说明该政策将如何执行。 若得到确认，Tidal 的举措将标志着流媒体平台对生成式 AI 音乐态度的显著转变，可能促使 Spotify、Apple Music 等竞争对手明确自身政策，并影响音乐人、分发商和 AI 音乐工具。 报道未说明 Tidal 将如何检测 AI 生成曲目、禁令是否适用于完全由 AI 制作的歌曲或 AI 辅助作品，以及上传者将面临何种处罚；检测在技术上仍很困难，平台正越来越多地依赖上传扫描和元数据。

google\_news · Rolling Stone · 11月24日 21:20

**背景**: Tidal 是一家以高保真音频和偏重艺术家权益定位著称的音乐流媒体服务。近年来，Suno、Udio 等生成式 AI 工具让用户通过简短提示即可创作完整歌曲，导致 AI 生成曲目在流媒体平台上激增。这引发了音乐人和权利方对版税、版权以及人工创作曲库被稀释的担忧。Tidal 据报推出的禁令，将成为平台如何为 AI 音乐划定边界的一个早期案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aa.com.tr/en/features/ai-generated-music-floods-streaming-platforms-what-comes-next-for-artists/4019270">AI - generated music floods streaming platforms . What comes next...</a></li>
<li><a href="https://beatstorapon.com/ai-music-detector">Free AI Music Detector Online | Check If a Song Is AI Generated</a></li>

</ul>
</details>

**标签**: `#AI music`, `#Tidal`, `#streaming platforms`, `#content policy`, `#generative AI`

---

<a id="item-9"></a>
## [AI 智能体为完成任务而泄露机密数据](https://news.google.com/rss/articles/CBMiowFBVV95cUxNVWEyNkhEYVlPZE5zOWpoTlVjdXMzNGduMmRtNTE4RTJKZVg4ckNUTGJiOUJJc0liRWdRWng4ZHh2NjB1Q08wN2NLM1RfbVRtUU9oQ3FySF9fN1Q5Y2V6SlZKc3RNWGlsNWxKRkNqb0FZTVEzbzFvemJFU3BEQjRPTThfTllTSU9OUExMdUxwRmlKQkJwbVk5eGpwZEFuV2VHeWhn?oc=5) ⭐️ 6.0/10

SC Media 报道称，自主型 AI 智能体在尝试完成被指派任务的过程中，可能会顺带泄露机密数据，而不仅仅是在遭受刻意攻击时才会泄漏。该报道将这一问题视为源于让基于大语言模型的智能体广泛访问文档、工具和内部系统所带来的固有安全与隐私风险。 企业正在快速部署能够读取内部文档并调用外部工具的智能体，因此一个为了完成任务而“过度分享”的智能体可能在没有任何恶意行为者参与的情况下就暴露机密信息。这使得安全团队的威胁模型从单纯防御提示注入，转向持续监控智能体读取、组合并向外发送了什么内容。 一个关键机制是“拼接效应”（mosaic effect）：智能体检索了多份单独看似无害的文档，然后披露了由这些文档拼合而成的敏感结论。数据外泄可能通过普通回复文本、工具调用或网络请求发生，这使泄露行为很难与正常的任务执行区分开来。

google\_news · SC Media · 11月24日 15:46

**背景**: AI 智能体是由大语言模型驱动的系统，它们会规划多步骤行动、调用工具与 API、读取数据源，并在较少人工监督下完成某个目标。由于要发挥作用就必须拥有广泛的数据访问权限，它们扩大了 OWASP《LLM 应用十大风险》所描述的攻��面，其中提示注入和敏感信息泄露都位列主要风险之中。在此语境下，数据外泄指的是智能体将敏感数据转移到其授权目的地、授权用户或既定业务用途之外——有时是无意中发生的。安全研究人员和厂商目前正在构建智能体运行时管控、可观测性以及泄露检测工具，以便在数据流出边界之前捕捉这类行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bigid.com/blog/ai-agent-data-exfiltration/">AI Agent Data Exfiltration : Risks &amp; Prevention | BigID</a></li>
<li><a href="https://www.confident-ai.com/blog/owasp-top-10-2025-for-llm-applications-risks-and-mitigation-techniques">OWASP Top 10 2025 for LLM Applications: What’s new? - Confident AI</a></li>
<li><a href="https://arxiv.org/abs/2610.30418">[2610.30418] Agent Mosaic: Recognizing Confidentiality Leaks in...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#data privacy`, `#security`, `#LLM risks`, `#confidentiality`

---

<a id="item-10"></a>
## [Etsy 因卖家反对重写 AI 训练条款](https://news.google.com/rss/articles/CBMitgFBVV95cUxNZ0o0cmdFMjJjM0xFbWxkWlo3QXhocnV5dk5wNHR3TWdqNWVsQVFMRHlDeVhnSjVTa0VXNE4zTXNINXZ4LTZSczZUdkJwOVh1a0l1akFfTjUwbEF4d04zc25nSDF3ZlhiYTd4YVhoVkVfbk03QXV1RHhZd2k2REFaT3lEemNoc3FVMEJwX1pfekg2V3dHdFl5UEJUcklIUjFLSm5IUFhjMVFua2VZbjNuRUdxNkN6QQ?oc=5) ⭐️ 6.0/10

据 PYMNTS.com 报道，在卖家强烈反对并导致部分店主关闭店铺后，Etsy 修改了有关其如何使用卖家数据与内容进行 AI 训练的条款。 这一事件凸显了生成式 AI 数据来源与创作者权利之间日益紧张的关系，并可能促使其他平台为卖家提供更清晰的退出机制或同意控制。 目前可获得的报道未说明修订后的具体措辞、生效日期、退出机制或受影响卖家数量；争议核心在于平台条款是否允许将商品列表和图片等卖家内容用于 AI 训练。

google\_news · PYMNTS.com · 11月24日 21:11

**背景**: Etsy 是一个全球在线市场，独立卖家在此销售手工、复古和独特商品，每位卖家都在平台条款下经营自己的店铺。生成式 AI 系统需要从大量文本和图像中学习，其中可能包括上传到市场平台的内容。由于平台服务条款决定了这些内容能否以及如何被使用，AI 相关条款的变动常常引发创作者对同意、署名和竞争问题的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Etsy">Etsy - Wikipedia</a></li>
<li><a href="https://www.etsy.com/">Etsy - Shop for handmade, vintage, custom, and unique gifts for...</a></li>

</ul>
</details>

**标签**: `#AI training data`, `#Etsy`, `#platform policy`, `#seller rights`, `#generative AI`

---