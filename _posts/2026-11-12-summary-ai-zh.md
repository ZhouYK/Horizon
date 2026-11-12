---
layout: default
title: "Horizon Summary: 2026-11-12 (ZH)"
date: 2026-11-12 23:03:38 +0000
lang: zh
report: ai
---

> 从 187 条内容中筛选出 10 条重要资讯。

---

1. [百度发布文心 ERNIE 5.5 Flash Preview，2800 亿参数，承诺 11 月 25 日前开源权重](#item-1) ⭐️ 8.0/10
2. [AWS 宣布 OpenAI Codex 上线 Amazon Bedrock](#item-2) ⭐️ 7.0/10
3. [Claude API 支持会话中动态调整 effort 等级](#item-3) ⭐️ 7.0/10
4. [Runway 以 Apache 2.0 开源 27B 世界动作模型 Praxis-1](#item-4) ⭐️ 7.0/10
5. [CACM 探讨从智能体到智能体社会的演进](#item-5) ⭐️ 6.0/10
6. [186 个假冒 AI 域名散播 ClickFix 诱饵与浏览器劫持程序](#item-6) ⭐️ 6.0/10
7. [谷歌据报将 TPU 芯片改造为面向 AI 智能体与安全的专用系统](#item-7) ⭐️ 6.0/10
8. [Matrix-Game4.0 在单块消费级显卡上实现浏览器端 60 FPS 游戏世界生成](#item-8) ⭐️ 6.0/10
9. [Anthropic 升级 Claude 连接器：支持全屏展开并可直接交互](#item-9) ⭐️ 6.0/10
10. [阿里官宣 Qwen4 大模型：核心架构更新，Qwen 应用已上线预览版](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [百度发布文心 ERNIE 5.5 Flash Preview，2800 亿参数，承诺 11 月 25 日前开源权重](https://www.aibase.com/news/32278) ⭐️ 8.0/10

百度在文心官方博客上发布了 ERNIE 5.5 Flash Preview，称其是在此前发布的 ERNIE 5.5 Flash Base 之上训练的首个后训练版本。该模型总参数达 2800 亿、每 token 激活 140 亿，支持 100 万 token 的上下文窗口，百度同时承诺将在 11 月 25 日前公开完整模型权重。 如果百度如期兑现，开源一个 2800 亿参数级别的模型将使其跻身可公开获取的最大模型之列，对开放权重生态是一次重要补充。这也表明中国实验室如今在前沿规模模型和开放发布两条战线上同时竞争，将进一步加剧全球 AI 市场的竞争态势。 该模型采用混合专家（MoE）架构，总参数 2800 亿、激活参数 140 亿，百度强调其在编程、智能体能力、3D 建模、知识工作、深度研究和内容创作方面表现突出。据称其底层 Base 模型采用了高度压缩的注意力机制：43 层中有 37 层在压缩 128 倍的序列上做注意力，另有 6 个 MLA-DSA 层维持长上下文性能——不过这些预览阶段的说法尚未经过独立基准测试验证。

aibase · AIbase · 11月12日 16:01

**背景**: 文心（ERNIE）是百度的大语言模型旗舰系列，其中“Base”指尚未经过针对对话与指令遵循的微调或对齐的预训练基础模型，而“后训练（post-trained）”版本才是针对实际使用优化的模型。上下文窗口衡量模型一次能处理的文本量——包括提示词、代码、文档或对话历史——100 万 token 大约相当于 75 万个单词。开放权重（open weights）指公开训练好的参数文件供任何人下载运行，这与完全开源（同时公开训练数据和代码）并不相同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ernie.baidu.com/zh/release/ernie-5-5-flash-preview/">Introducing ERNIE 5.5 Flash Preview · ERNIE - ernie.baidu.com</a></li>
<li><a href="https://openrouter.ai/baidu/ernie-5.5-flash-preview:free">ERNIE-5.5-Flash-Preview (free) - API Pricing &amp; Providers</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models ? | Analytics Vidhya</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source models`, `#Baidu ERNIE`, `#long-context`, `#AI industry news`

---

<a id="item-2"></a>
## [AWS 宣布 OpenAI Codex 上线 Amazon Bedrock](https://news.google.com/rss/articles/CBMigwFBVV95cUxNaTMtak5LN2ZUam9haGF5ekhPR1hvdFNyU2lybEN0YU0xdWtnNFBEZ2o4clJNT050OXZXWXJtRm9iOFZLVHI5SEc1aWdmb3NHM1Y4UE5MdUc5MlNPaGE2SEJ6cjhyeUlEaGFNeUxUeVRYTGQzeUZNdDB4YmZfNENOVDVsZw?oc=5) ⭐️ 7.0/10

亚马逊云科技（AWS）发布公告称，OpenAI 的 AI 编程智能体 Codex 现已在 Amazon Bedrock 上提供。该消息出现在 AWS 自己的人工智能博客上，但目前流传的内容仅是一个标题和链接，并未给出可用区域、价格或模型版本等技术细节。 若细节得到确认，这将是一个值得关注的转变：Codex 登陆 Bedrock 意味着 AWS 企业客户可以在既有的 AWS 安全、计费和治理边界内使用 OpenAI 的编程智能体，而不必经由 OpenAI 自家平台。这也表明 OpenAI 与微软此前紧密的模型分发绑定有所松动，并将加剧 Bedrock、Microsoft Foundry 与 Google Cloud 等云 AI 平台之间的竞争。 目前可得的内容没有任何工程细节——既未说明通过 Bedrock 提供的是哪一层 Codex 能力（CLI、IDE 集成还是更广泛的智能体平台），也未涉及定价、可用区域或数据处理条款。在 AWS 或 OpenAI 公布模型卡与文档之前，读者应将该公告视为厂商的宣传性信息。

google\_news · Amazon Web Services \(AWS\) · 11月11日 23:35

**背景**: OpenAI Codex 是 OpenAI 推出的一系列 AI 编程智能体，最早于 2025 年 4 月以 Codex CLI 形式发布，如今可通过 ChatGPT 网页版、桌面应用、IDE 集成和命令行使用；据报道，到 2026 年 3 月其周活跃用户已超过 200 万，并被定位为更广泛的企业级智能体平台。Amazon Bedrock 是 AWS 于 2023 年推出的全托管服务，通过统一 API 提供多家 AI 公司的基础模型，并配套构建生成式 AI 应用的工具。Bedrock 作为企业 AI 平台与 Microsoft Foundry、Google Cloud 相互竞争，在其上托管竞争对手的旗舰编程智能体将是一项意义重大的跨厂商安排。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://en.wikipedia.org/wiki/Amazon_Bedrock">Amazon Bedrock</a></li>

</ul>
</details>

**标签**: `#OpenAI Codex`, `#Amazon Bedrock`, `#AWS`, `#AI coding`, `#cloud AI`

---

<a id="item-3"></a>
## [Claude API 支持会话中动态调整 effort 等级](https://www.aibase.com/news/32271) ⭐️ 7.0/10

11 月 12 日，Anthropic 为 Claude API 新增 Beta 功能：开发者可在对话中途插入一条空内容的 system 消息并设置新的 output\_config.effort，从而调整后续回答的努力等级，无需新建会话，提示缓存仍可命中。新等级从下一条带新输入的用户消息起生效。 这让构建 Claude 智能体和聊天产品的团队可以逐轮在回答深度、延迟和成本之间做权衡，而不必为整个会话固定一个 effort 设置。保持缓存命中也很关键，因为在长对话中缓存未命中会同时增加延迟和 token 成本。 该功能处于 Beta 阶段，需要携带 mid-conversation-output-config-2026-07-01 beta 头；摘要称其支持 Fable 5.2、Opus 5.5、Sonnet 5.5、Haiku 5.5 等模型，并覆盖 Amazon Bedrock、Google Cloud、Azure 等平台。新设置仅从下一条带新输入的用户消息开始生效，不会追溯改变当前正在生成的回答。

aibase · AIbase · 11月12日 12:01

**背景**: 在 Claude API 中，output\_config.effort 是一个告诉模型在回答上投入多少努力的参数，思考过程也包含在内，常见等级包括 low、medium、high、xhigh 和 max。提示缓存（prompt caching）让 API 复用此前处理过的提示前缀，从而降低重复或长上下文请求的处理时间与成本。由于缓存命中依赖提示前缀和请求配置保持一致，能够在不使缓存失效的情况下调整 effort 正是此次更新的关键之处。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.gloo.com/api-guides/anthropic-messages">Anthropic Messages API - Gloo</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching">Prompt caching - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude API`, `#LLM infrastructure`, `#API design`, `#cost optimization`

---

<a id="item-4"></a>
## [Runway 以 Apache 2.0 开源 27B 世界动作模型 Praxis-1](https://www.aibase.com/news/32267) ⭐️ 7.0/10

Runway 以 Apache 2.0 许可证完整开源了 Praxis-1，这是一个基于混合专家（MoE）扩散 Transformer 架构、拥有 270 亿参数的世界动作模型。此次发布包含全部模型权重以及推理和微调代码，Runway 称该模型在权威机器人排行榜上登顶，并允许商业使用。 对于大型具身智能模型而言，在宽松的商业许可下完全开放权重并附带相关代码仍然十分罕见——当前领先的机器人基础模型通常是闭源的，或者以受限条款发布。如果其排行榜成绩经得起验证，Praxis-1 将显著降低机器人初创公司和研究实验室构建、微调自有世界动作策略的门槛。 该模型是 270 亿参数的混合专家扩散 Transformer，意味着每次推理只激活部分专家参数，从而将计算开销控制在低于同等规模稠密模型的水平。值得注意的是，公告并未指明具体的排行榜名称、评测任务或对比基线，目前也没有针对其登顶声明的独立验证结果公布。

aibase · AIbase · 11月12日 11:01

**背景**: 世界动作模型（WAM）将预测式世界建模（预判场景将如何演化）与动作生成结合起来，使机器人能够在执行前先在“想象”中推演某个动作的结果；这与直接将观测映射为动作的视觉-语言-动作（VLA）策略形成对比。扩散 Transformer（DiT）是把 Transformer 架构用于基于扩散的生成建模，而混合专家（MoE）变体引入了稀疏专家路由，使模型在扩大参数规模时不必按比例增加推理成本。Apache 2.0 是一种宽松的开源许可证，允许在署名前提下进行商业使用、修改和再分发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.16074">[2609.16074] World-Action Models for Robot Learning and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://github.com/feizc/DiT-MoE">GitHub - feizc/DiT-MoE: Scaling Diffusion Transformers with ...</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#robotics`, `#embodied intelligence`, `#world models`, `#Runway`

---

<a id="item-5"></a>
## [CACM 探讨从智能体到智能体社会的演进](https://news.google.com/rss/articles/CBMieEFVX3lxTE0wRHpsYjlKNjZvOHVNNnJEN2tYS2FwWDVWX3lSUWR6aUNjbS1zOHdVS2ViVTkyeElWOGFuaC1yczdDZElQMDVTUVhuSWRES2htYmV5enNEbm9CSDRsSlcxZ0d4aUVLRG9rYjNHOVNMT3lNdUFfN0ZHTQ?oc=5) ⭐️ 6.0/10

《Communications of the ACM》发表了一篇题为“From Intelligent Agents to Agent Societies”的文章，讨论从单个智能体向由相互作用智能体组成的社会演进。现有摘要显示，这更像是一篇概念与技术综述，而不是具体产品发布或基准测试结果。 这一主题具有时效性，因为多智能体 AI 系统正从研究原型走向实用框架和商业应用。像《Communications of the ACM》这样有声誉的刊物讨论智能体社会，可能有助于塑造分布式 AI 的术语、架构模式和研究优先级。 目前只有标题和一句话摘要，因此文章的具体论点、案例、技术深度和局限性都无法核实。读者应将其视为指向《Communications of the ACM》一篇多智能体系统文章的线索，而不是已确认的新突破证据。

google\_news · Communications of the ACM · 11月12日 20:59

**背景**: 智能体是能够感知环境并采取行动以实现目标的软件或硬件实体。多智能体系统由多个相互作用的智能体组成，它们通过合作、竞争或协调来解决单个智能体难以解决的问题。“智能体社会”这一术语进一步强调角色、社会结构、通信协议以及大量智能体之间的涌现行为。分布式人工智能是一个相关领域，研究去中心化 AI 系统，既包括智能体有各自利益的开放多智能体系统，也包括智能体共享共同目标的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_system">Multi-agent system - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Distributed_artificial_intelligence">Distributed artificial intelligence - Wikipedia</a></li>
<li><a href="https://docs.camel-ai.org/">CAMEL - Build Multi- Agent AI Systems</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#agent societies`, `#AI agents`, `#distributed AI`, `#CACM`

---

<a id="item-6"></a>
## [186 个假冒 AI 域名散播 ClickFix 诱饵与浏览器劫持程序](https://news.google.com/rss/articles/CBMiggFBVV95cUxOUlkxU1FZT2s0bUk0MVdJc1YtNGF5XzBCTGo5NGZsSS1FZzhSWGtQa0taWkpzT19ScW8zSDktX3FLbXVCVUxybjNsTWlsakNBcGN3c0Y0VlIxbkxlTUZuTDVPUzFCV29SaDEzenNROHR1U1c0UVNqMGdic1gzRjVpN1JB?oc=5) ⭐️ 6.0/10

研究人员发现了一个由 186 个假冒 AI 主题域名构成的攻击活动，这些域名会将访问者重定向到 ClickFix 诱饵页面、浏览器恶意软件以及搜索引擎劫持程序。该网络利用人们对 AI 工具的兴趣把受害者引向欺骗性页面，而不是在域名本身直接托管恶意软件。 由于 AI 品牌域名在寻找新工具的用户眼中显得相当可信，这一活动表明廉价的域名注册加上重定向链条就能把钓鱼操作规模化。安全防御人员和普通用户在搜索 AI 服务时，应把仿冒域名和突如其来的“验证”提示视为高风险信号。 ClickFix 类攻击并不利用软件漏洞，而是展示伪造的错误提示或 CAPTCHA 页面，引导用户把命令粘贴到“运行”对话框或终端中，而这一步实际上会下载恶意软件。该活动还投放浏览器劫持程序，悄悄修改主页和默认搜索引擎，另有一些域名仅充当重定向跳板，以隐藏最终的载荷基础设施。

google\_news · The Hacker News · 11月12日 15:15

**背景**: ClickFix 是一种社会工程手法：网站声称访问者必须“修复”某个浏览器或安全问题，并给出让用户自行执行的命令，受害者等于亲手运行了恶意软件，从而绕过许多安全防护。浏览器劫持程序则是在未经同意的情况下修改主页和默认搜索引擎等浏览器设置的非预期软件，通常用于注入广告或把搜索流量导向攻击者控制的引擎。攻击者经常围绕热门话题注册域名，而生成式 AI 工具已成为极具吸引力的诱饵，因为用户会主动搜索新服务，并且习惯了在陌生网站上注册。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Browser_hijacking">Browser hijacking - Wikipedia</a></li>
<li><a href="https://www.malwarebytes.com/blog/threats/browser-hijacker">Browser Hijackers | What is a Browser Hijacker &amp; how to ...</a></li>
<li><a href="https://www.interest.co.nz/technology/132398/devious-clickfix-technique-phishing-campaign-targets-hotels-bogus-booby-trapped">Phishers hone their attacks with &#x27; ClickFix ... | interest.co.nz</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#malware`, `#phishing`, `#browser hijacking`, `#AI-themed domains`

---

<a id="item-7"></a>
## [谷歌据报将 TPU 芯片改造为面向 AI 智能体与安全的专用系统](https://news.google.com/rss/articles/CBMi7gJBVV95cUxNUFdBQlBXR3dOb0dJUUh5Rk9wX19ucEY1QlB5cnVtOXhvSk9Xd21KWW9xcXdQc2RuQ3lMY0RVOHl0cDhVNUh4Q0N5Q2xlWWRxRmpSYjRnWHJ6X19XOEFKVFB3N28yMjJlUTdPMy1CWG5wNFdVMTZncEZmN2tvSWVaa0pIMURmOE5sM0ZsbTY5MzBHamZxelByenBwSFUwWFhjb3VwTWZLaWlDTlVXd1ZaMWZ5RnQ4VHZKLUNnLTdkYmpoeUxUc3Zld0VZcExsQ1JoNU80MkhNYzhCR2dHNy1LdFlmVmxfUm9qUndLb2VhdUhDcDVia3ZuckI3NlpqWGJPNGtOdHo3R2JyWnB6Yy1VQnJNYkhiWUoxMnlXZXlRUi01YnVPMndFSWVqSHl0LTVIdUxQSEhFZ0daYTlsZktKN3p2UHFzVWlfendrbUNMSmUydUJWZjd0RkN0dzNYS1d0Zm5oQ3BycXlMVWtiOWc?oc=5) ⭐️ 6.0/10

据 Tom&\#x27;s Hardware 报道，谷歌正在将其张量处理单元（TPU）芯片改造为面向 AI 智能体工作负载和安全计算的专用系统。报道将此描述为谷歌从提供通用加速芯片转向将 TPU 硬件打包成用途定制的系统，但现有资料中并未给出具体的产品名称、规格参数或时间表。 若消息属实，这表明谷歌将针对特定工作负载的硬件——而非通用的“一刀切”加速器——视为 AI 基础设施的下一个竞争前沿，尤其是因为智能体式 AI 需要长时间、多步骤的执行并涉及工具调用与记忆。这一举措可能影响云客户部署 AI 智能体的方式，以及谷歌如何以其 TPU 技术栈对抗基于 GPU 的竞争对手。 目前可获得的信息仅限于标题和一句摘要，因此尚未披露芯片代次、内存配置、互连方式或性能数据等技术细节。同样不清楚的是，这些专用系统将通过谷歌云提供、作为本地部署硬件出售，还是仅供内部使用。

google\_news · Tom&\#x27;s Hardware · 11月12日 11:00

**背景**: 张量处理单元（TPU）是谷歌为神经网络机器学习专门开发的神经处理单元专用集成电路（ASIC），支持 TensorFlow、JAX 和 PyTorch 等框架；谷歌于 2015 年开始在内部使用 TPU，并在 2018 年通过其云服务向第三方开放。AI 智能体是能够在一定程度上自主做出决策、追求目标并采取行动的 AI 程序，通常由大语言模型驱动，并常与记忆、规划逻辑和工具接口相结合。由于智能体工作负载与单次模型推理差异很大——涉及大量顺序模型调用、检索与编排——硬件厂商正日益探索针对这类模式而非单纯训练吞吐量优化的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://cloud.google.com/tpu">Tensor Processing Units (TPUs) | Google Cloud</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>

</ul>
</details>

**标签**: `#Google TPU`, `#AI hardware`, `#AI agents`, `#security`, `#specialized systems`

---

<a id="item-8"></a>
## [Matrix-Game4.0 在单块消费级显卡上实现浏览器端 60 FPS 游戏世界生成](https://www.aibase.com/news/32285) ⭐️ 6.0/10

据报道，Matrix-Game4.0 已在面向世界模型的实时 AI 基础设施平台 Reactor 上线，能够在单块消费级显卡上、以 60 FPS 在网页浏览器中实现“边玩边生成”的游戏世界生成。其宣称的核心在于整个可交互世界是即时合成的而非预先渲染，浏览器则作为 Reactor 低延迟推理栈的客户端。 如果这一说法成立，将意味着游戏世界从预先制作的资产转向逐帧实时生成，从而大幅降低构建可交互环境的成本。在浏览器中依托单块消费级显卡达到 60 FPS 同样关键，因为它让生成式世界模型不再只是数据中心实验室的专属，普通玩家和独立开发者也能触及。 该消息源自一篇宣传性质的新闻稿，并未披露基准测试、分辨率、延迟数据、模型规模，也没有说明世界中有多少是真正生成、多少来自缓存或预置内容。值得注意的是，60 FPS 这一目标明显高于同类实时世界模型演示此前公开展示的水平，因此关于帧率与画质取舍的独立验证仍然缺失。

aibase · AIbase · 11月12日 18:01

**背景**: 世界模型是一类 AI 系统，它学习模拟某个环境，并根据玩家的操作预测场景的下一帧，而不是回放预先做好的 3D 资产。在游戏和机器人领域，它被视为生成无穷且不重复的交互内容的手段，但实时推理的算力开销一直是主要瓶颈。Reactor 将自身定位为承载此类模型并以超低延迟提供服务的基础设施，让开发者无需自行运行模型即可构建交互式 AI 应用。“边玩边生成”意味着没有加载界面、也没有预先搭建的关卡——世界随着玩家的移动被即时创造出来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reactor.inc/">Reactor - Real-time AI infrastructure for video, robotics ...</a></li>
<li><a href="https://www.reactor.inc/blog/reactor-launch">Introducing Reactor: The Developer Platform for World Models</a></li>
<li><a href="https://lab.rosebud.ai/blog/real-time-world-models-gaming-the-future-is-already">Real-time World Models Gaming: AI Generates Infinite Worlds</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#real-time rendering`, `#game AI`, `#browser gaming`, `#GPU acceleration`

---

<a id="item-9"></a>
## [Anthropic 升级 Claude 连接器：支持全屏展开并可直接交互](https://www.aibase.com/news/32279) ⭐️ 6.0/10

Anthropic 升级了 Claude 的连接器功能，接入的应用现在可以在对话旁边以全屏视图打开，而不再是狭窄的侧边预览，用户还能在与 Claude 对话的同时直接在这些工具中交互和编辑内容。该功能正在向 Claude 的网页版和桌面版套餐推送。 这使 Claude 从一个仅仅引用外部工具的聊天窗口，变成一个助手与用户并排编辑同一份内容的工作空间，有望显著减少文档、设计和项目管理流程中的上下文切换成本。这也表明 Anthropic 的竞争重点不仅在模型本身的能力，还在于集成式的应用体验。 此次更新被描述为从侧边预览转向全屏工作流，即接入的工具会在对话旁边保持一个持续存在的面板，用户无需离开对话去操作。该功能目前仅限网页版和桌面版套餐使用，且被定位为渐进式的用户体验改进，而非新模型或新的 API 能力。

aibase · AIbase · 11月12日 16:01

**背景**: Claude 连接器是 Anthropic 提供的集成机制，让助手能够接入第三方应用和数据源，Anthropic 官方在类似功能的演示中曾展示过 Adobe、Confluence 和 Box 等工具。此前这些接入的应用只以受限的侧边预览形式出现，在其中操作更像是聊天的附属行为。让它们支持全屏和直接交互，缩小了“向 Claude 询问某个文档”和“与 Claude 一起编辑该文档”之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=ybWVeBY2sio">Claude Just Put Your Apps INSIDE the Chat!- YouTube</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI assistants`, `#product update`, `#developer tools`

---

<a id="item-10"></a>
## [阿里官宣 Qwen4 大模型：核心架构更新，Qwen 应用已上线预览版](https://www.aibase.com/news/32274) ⭐️ 6.0/10

阿里巴巴正式官宣了下一代大语言模型 Qwen4，称其采用全新的核心架构，核心能力全面升级，在知识理解、语义解析范围以及对长上下文和复杂上下文的处理上都有明显提升。目前预览版已经接入 Qwen 应用，官方表示正式版即将发布。 Qwen 是开放权重生态中使用最广泛的模型家族之一，因此这次代际更新会直接影响大量基于 Qwen 权重和 API 进行开发的开发者，也关系到阿里与其他中外前沿模型之间的竞争格局。同时把预览版直接接入面向消费者的 Qwen 应用，说明阿里希望在新模型正式发布前就让终端用户先用上新能力。 这次公告更像一次预告：没有公布参数量、基准测试成绩、架构细节、开源许可条款或具体发布日期，而且消息来自资讯聚合站点而非阿里官方渠道。早期体验信息显示存在面向复杂多步任务、编程和智能体运行的 Qwen4-Max-Preview 版本，而上一代 Qwen3 以可切换的“思考/非思考”混合模式著称。

aibase · AIbase · 11月12日 15:01

**背景**: Qwen（又称通义千问）是阿里云推出的一系列以大开放权重为主的大、小语言模型，按代际迭代发布，其中 Qwen3 引入了混合推理模式，让用户可以在速度与推理深度之间做权衡。Qwen 应用则是一个独立的消费级产品：由 Qwen 系列模型驱动的 AI 助手，接入了阿里生态，用户通过对话即可点外卖、打车、购物或预订机酒。“语义解析”指的是自然语言处理中把自由文本映射为结构化、机器可用含义的任务，对于把用户请求转化为这类助手中可执行的动作至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.alibabagroup.com/en-US/about-alibaba-businesses-1951035128754995200">Qwen-Alibaba Group</a></li>
<li><a href="https://mobidevices.com/en/alibaba-qwen-4-max">Alibaba launches flagship AI model Qwen 4 Max</a></li>

</ul>
</details>

**标签**: `#qwen`, `#llm`, `#alibaba`, `#model-release`, `#ai-announcements`

---