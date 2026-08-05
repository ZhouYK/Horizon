---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
report: ai
---

> 从 281 条内容中筛选出 10 条重要资讯。

---

1. [Jeff Dean 在 AI 重组中离开谷歌，结束 27 年任期](#item-1) ⭐️ 9.0/10
2. [LLM 0.32 新增推理痕迹、服务端工具与智能日志](#item-2) ⭐️ 8.0/10
3. [谷歌重组 AI 领导层，DeepMind 主管改任新角色](#item-3) ⭐️ 8.0/10
4. [腾讯混元 Hy ASR 3.0 预览发布：大模型语音识别将字错率降至 3%](#item-4) ⭐️ 8.0/10
5. [Mistral 发布 Shieldstral：3B 开源多模态审核模型，16GB GPU 可运行](#item-5) ⭐️ 8.0/10
6. [字节跳动发布 SeedRealtime：全双工音视频模型已部署至豆包](#item-6) ⭐️ 8.0/10
7. [通义千问发布 Qwen-Image-3.0-Pro 登顶国内文生图竞技场](#item-7) ⭐️ 8.0/10
8. [阿里巴巴发布 Qwen-Image-3.0，API 定价每张图片 0.18 元起](#item-8) ⭐️ 8.0/10
9. [京东开源 JoyAI-Video-Edit：30fps 实时视频编辑模型](#item-9) ⭐️ 8.0/10
10. [Anthropic 向初创公司 Volta 下达 100 亿美元订单以确保 AI 电力](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Jeff Dean 在 AI 重组中离开谷歌，结束 27 年任期](https://news.google.com/rss/articles/CBMipwFBVV95cUxOakszXzhHclRmR3dMdk0xUTBqWHYtRGNUMXAwWVJIS3d5Uy1XZUJVWGlMX1pKOGJPS3BhUVpmLXlNb3JfMUQwakh2MjAxZlNoUkpWNmZ4UHl0bjd1SWFfRDBhRDNvNW92cWdfSl9pTjJjMDg4UVkzbTktV3lYM0x6MFZtZ0dWcDYwdUhhbklkd1lkVDNkN2pYVmlrNXYtTGlLRnZSUVZFRdIBpwFBVV95cUxOakszXzhHclRmR3dMdk0xUTBqWHYtRGNUMXAwWVJIS3d5Uy1XZUJVWGlMX1pKOGJPS3BhUVpmLXlNb3JfMUQwakh2MjAxZlNoUkpWNmZ4UHl0bjd1SWFfRDBhRDNvNW92cWdfSl9pTjJjMDg4UVkzbTktV3lYM0x6MFZtZ0dWcDYwdUhhbklkd1lkVDNkN2pYVmlrNXYtTGlLRnZSUVZFRQ?oc=5) ⭐️ 9.0/10

谷歌首席科学家 Jeff Dean 在 AI 部门重组中离开公司，结束了他在谷歌 27 年的职业生涯。这一变动标志着谷歌 AI 领导层的重大变化。 Jeff Dean 是人工智能和系统领域最具影响力的人物之一，曾共同创立 Google Brain，并为 MapReduce 和 TensorFlow 等基础技术作出了贡献。他的离开标志着谷歌 AI 组织战略转变，也可能影响业界对谷歌 AI 方向的看法。 Dean 已在谷歌工作 27 年，最近担任首席科学家。这次重组涉及 AI 领导层结构的变动，但报道未详细说明具体的接任者或新职位。

google\_news · CNBC · 8月5日 16:03

**背景**: Jeff Dean 是一位传奇计算机科学家，以在大规模分布式系统和机器学习方面的工作而闻名。他共同创立了推动深度学习发展的 Google Brain，并共同设计了 MapReduce、BigTable 和 TensorFlow 等支撑现代 AI 基础设施的系统。他的离开之所以引人注目，是因为几十年来他一直是谷歌 AI 工作的核心人物。

**标签**: `#Google`, `#AI`, `#Jeff Dean`, `#leadership`, `#industry news`

---

<a id="item-2"></a>
## [LLM 0.32 新增推理痕迹、服务端工具与智能日志](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 LLM 0.32，这是自项目启动以来最重要的一次更新，新增了可见的推理痕迹显示、服务端工具支持，以及重新设计的内容可寻址 SQLite 日志。该版本还支持 GPT-5.6 模型家族，默认模型改为性价比高的 GPT-5.6 Luna，并新增了 \`llm openai endpoint\` 命令，可对任意兼容 OpenAI 的端点执行提示词。 在 stderr 中显示推理痕迹，让开发者无需污染管道输出即可查看模型的“思考”过程；同时，OpenAI CodeInterpreter、WebSearch 等服务端工具使 CLI 在智能体工作流中更加强大。重新设计的内容可寻址 SQLite 日志提升了存储效率与完整性，惠及所有依赖 LLM 进行脚本编写和自动化的开发者生态。 新增的 \`-R/--hide-reasoning\` 参数可关闭推理痕迹输出；llm-anthropic 插件 0.26 增加了 WebSearch、WebFetch、CodeExecution 和 AnthropicMCP 工具。新的 \`llm openai endpoint\` 命令可对任意 OpenAI 兼容端点执行一次性提示词且不记录日志；通过 datasette-mcp 插件，可在 Anthropic API 的单个请求中调用 MCP 工具。

rss · Simon Willison · 8月4日 23:58

**背景**: LLM 是 Simon Willison 开发的命令行工具，通过统一接口调用各类大语言模型，并将对话日志存储在 SQLite 中。推理痕迹是模型在生成最终答案前产出的中间推理步骤。OpenAI 于 2025 年 3 月发布的 Responses API，将聊天补全与高级工具调用结合，简化了智能体应用的开发。内容可寻址存储以内容的哈希值作为引用，可提高去重与完整性，这也是 SQLite VFS 等实现中常见的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://jumpcloud.com/it-index/what-are-reasoning-traces-in-ai">What Are Reasoning Traces in AI ? - JumpCloud</a></li>
<li><a href="https://blog.textile.io/the-quest-for-a-content-addressable-sqlite">The Quest for a Content Addressable SQLite</a></li>

</ul>
</details>

**标签**: `#LLM`, `#OpenAI`, `#CLI`, `#SQLite`, `#reasoning`

---

<a id="item-3"></a>
## [谷歌重组 AI 领导层，DeepMind 主管改任新角色](https://news.google.com/rss/articles/CBMipAFBVV95cUxQaHV5Q1dFcHFPLTJhTmkyTG05amxnbm1QQkRGYnpCZ0tON1FJVnJ2d0pBQVZENUlJYm01cXBoWFhvVENnbklRLVZoNndsMVpiWGNhNnJ6cEt6VFdKUGdRQ0xPem5kaHo3Y24tTlFqWGFtZGZjS25UbFl5UUMxTWtsWkVRLWQzOTZWbTViWXJXbFdIYUU0STdDcTliOEJCUEFrR0x0cQ?oc=5) ⭐️ 8.0/10

路透社报道，谷歌正在重组其人工智能领导层，DeepMind 主管将改任其他职位。这标志着谷歌在管理其 AI 业务方面发生了重大变化。 此次领导层变动可能重塑谷歌的 AI 战略，以及 DeepMind 与公司其他部门的协作方式。这表明将前沿 AI 研究整合到谷歌更广泛的产品开发中变得越来越重要。 路透社的报道并未披露 DeepMind 主管的新职位或继任者的具体信息。此次重组正值各大科技公司在生成式 AI 领域的竞争日益激烈之际。

google\_news · Reuters · 8月5日 21:42

**背景**: DeepMind 是一家总部位于伦敦的人工智能研究实验室，于 2014 年被谷歌（现为 Alphabet 旗下公司）收购。它曾开发出 AlphaGo 和 AlphaFold 等具有里程碑意义的 AI 系统。谷歌 AI 领导层的重组可能会影响这些研究工作的优先级以及将其整合到商业产品中的方式。

**标签**: `#AI`, `#Google`, `#DeepMind`, `#leadership`, `#industry news`

---

<a id="item-4"></a>
## [腾讯混元 Hy ASR 3.0 预览发布：大模型语音识别将字错率降至 3%](https://www.aibase.com/news/30137) ⭐️ 8.0/10

腾讯混元发布了新一代语音识别模型 Hy ASR 3.0 预览版，它基于 Hy3 大语言模型构建。官方称其在普通话、英语和粤语上的字错率约为 3%，并覆盖十大方言区。 这标志着语音识别从单纯转写走向语义理解，有望提升语音助手、会议转写和客服分析等场景的表现。通过利用大模型的推理能力，它在方言鲁棒性和上下文准确性方面树立了新标杆。 该模型基于 Hy3 构建，Hy3 是一个拥有 295B 参数、21B 激活参数的混合专家（MoE）模型。它不依赖标准普通话，尤其在长音频场景中表现出色，可通过深层语义理解提升准确率。

aibase · AIbase · 8月5日 17:16

**背景**: 自动语音识别（ASR）将语音转换为文本，传统系统常受口音、方言和上下文歧义困扰。腾讯混元是腾讯的 AI 大模型家族，Hy3 是其推出的参数量达 295B 的大语言模型，已集成到腾讯云和多个产品中。Hy ASR 3.0 将 ASR 与大模型推理结合，能够理解语义而不仅是转写文字，在嘈杂音频或多方言环境下尤为有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibase.com/news/30108">Tencent Hunyuan Launches Hy ASR 3 . 0 Preview: Speech ...</a></li>
<li><a href="https://xix.ai/live/6411">Tencent Hunyuan launched Hy ASR 3 . 0 Preview, a speech ... - xix.ai</a></li>
<li><a href="https://www.tencent.com/en-us/articles/2202386.html">Tencent Hunyuan Officially Releases Hy3, Advancing Agent ...</a></li>

</ul>
</details>

**标签**: `#ASR`, `#Speech Recognition`, `#Tencent`, `#LLM`, `#AI`

---

<a id="item-5"></a>
## [Mistral 发布 Shieldstral：3B 开源多模态审核模型，16GB GPU 可运行](https://www.aibase.com/news/30132) ⭐️ 8.0/10

Mistral AI 发布了开源内容审核模型 Shieldstral，参数规模为 3B，采用 Apache 2.0 许可证。该模型可在单个 16GB GPU 上运行，并声称在多模态审核方面达到开源 SOTA 水平，性能可与 7 倍于其规模的模型相媲美。 Shieldstral 让计算资源有限的机构也能使用先进的多模态安全审核能力，有望提升 AI 部署中的信任与安全水平。其开源特性和小体积可能加速跨语言自定义审核策略的采用。 该模型支持 12 种语言，可在单个 16GB GPU 上运行。与大多数使用固定危害分类的保护模型不同，Shieldstral 据称可在推理时以纯文本形式读取审核策略，从而无需重新训练即可实现策略自定义。

aibase · AIbase · 8月5日 16:16

**背景**: 内容审核是指自动检测并移除违反策略的内容，而多模态审核需要同时理解文本、图像、音频和视频。传统的单模态系统常常无法发现跨模态的有害内容，例如梗图；同时许多现有安全模型依赖固定的危害分类体系。Mistral 的 Shieldstral 通过提供更小、开放权重的分类器，并支持自定义策略，来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/shieldstral/">Introducing Shieldstral. - Mistral AI</a></li>
<li><a href="https://www.explainx.ai/blog/mistral-shieldstral-safety-classifier-august-2026">Mistral Shieldstral: 3B Safety Classifier (2026) - explainx.ai</a></li>
<li><a href="https://arxiv.org/abs/2305.10547">[2305.10547] Rethinking Multimodal Content Moderation from an ... Dynamic Content Moderation in Livestreams: Combining ... CM-MRAG: A multimodal retrieval-augmented framework for ... Rethinking Multimodal Content Moderation from an Asymmetric ... 1st Workshop on Multimodal Content Moderation</a></li>

</ul>
</details>

**标签**: `#AI`, `#Machine Learning`, `#Content Moderation`, `#Open Source`, `#Mistral`

---

<a id="item-6"></a>
## [字节跳动发布 SeedRealtime：全双工音视频模型已部署至豆包](https://www.aibase.com/news/30128) ⭐️ 8.0/10

字节跳动 Seed 团队推出了 SeedRealtime，这是一个原生融合音频、视频和文本的全双工模型，并于 2026 年 8 月 5 日在豆包 App 中全面部署。这标志着这种端到端实时多模态交互模型的首次大规模落地。 SeedRealtime 代表了从级联流水线向原生端到端多模态架构的转变，能够实现无延迟地同时观看、收听和说话。这可能为实时 AI 交互树立新的行业方向，并给 OpenAI 的 GPT-4o realtime 等竞品带来压力。 与将感知和表达分段拼接的级联系统不同，SeedRealtime 采用端到端设计，感知、理解、决策和表达并行运行。该模型原生处理音频、视频和文本的连续流，消除了模态之间的割裂。

aibase · AIbase · 8月5日 14:16

**背景**: 传统的语音和多模态 AI 智能体依赖级联流水线，由不同的模型分别处理语音识别、语言理解和语音合成，导致延迟和上下文丢失。像 SeedRealtime 这样的原生端到端多模态模型将所有模态融合到一个架构中，从而实现实时、连续的交互。这种方法是更广泛的行业趋势的一部分，即向统一多模态大语言模型发展，例如 SenseNova-U1 等模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technode.com/2026/08/05/bytedance-launches-seedrealtime-full-duplex-audio-video-model/">ByteDance launches SeedRealtime full-duplex audio-video model</a></li>
<li><a href="https://smartfaqs.ai/learn/xvi-ai-agents-chatbots/practical-deployment-playbooks/voice-multimodal-agents">Voice &amp; Multimodal Agents - Learn | SmartFAQs. ai</a></li>
<li><a href="https://huggingface.co/papers/2605.12500">Paper page - SenseNova-U1: Unifying Multimodal Understanding and...</a></li>

</ul>
</details>

**标签**: `#AI`, `#multimodal`, `#real-time interaction`, `#ByteDance`, `#speech`

---

<a id="item-7"></a>
## [通义千问发布 Qwen-Image-3.0-Pro 登顶国内文生图竞技场](https://www.aibase.com/news/30127) ⭐️ 8.0/10

通义千问发布了 Qwen-Image-3.0-Pro 和 Standard 文生图模型，在 Arena 文生图排行榜上位列中国第一、主流模型第二。模型支持 4.5k token 长提示词、10px 级精细文字渲染和 12 种语言，Pro 版每张图片起价 0.04 美元。 这是中国文生图模型的重要里程碑，展示了在国际排行榜上的竞争实力。统一的生成与编辑架构加上低廉的价格，可能让企业、创作者和开发者更容易获得高质量的图像生成能力。 核心亮点是首次将生成与编辑集成到单一架构中，实现统一的多能力任务。Pro 版支持 10px 级文字渲染，每张图片仅需 0.04 美元，并原生支持 12 种语言。

aibase · AIbase · 8月5日 12:16

**背景**: 文生图模型根据自然语言提示生成图像，其中最具挑战性的问题之一就是准确渲染细小或复杂的文字。许多模型会出现文字扭曲或拼写错误，因此 10px 级渲染能力代表了显著的技术进步。类似 Arena 的排行榜通过盲测比较模型输出，以众包方式衡量模型质量。同时处理生成与编辑的统一架构是当前该领域的新兴趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen-image.net/blog/qwen-image-3-0">Qwen- Image -3.0: From Beautiful Images to Useful Visual Work</a></li>
<li><a href="https://artificialanalysis.ai/image/leaderboard/text-to-image">Text to Image Leaderboard - Top AI Image Models</a></li>
<li><a href="https://iclr-blogposts.github.io/2026/blog/2026/diffusion-architecture-evolution/">From U-Nets to DiTs: The Architectural Evolution of Text-to-Image Diffusion Models (2021–2025) | ICLR Blogposts 2026</a></li>

</ul>
</details>

**标签**: `#text-to-image`, `#Qwen`, `#AI model`, `#generative AI`, `#multimodal`

---

<a id="item-8"></a>
## [阿里巴巴发布 Qwen-Image-3.0，API 定价每张图片 0.18 元起](https://www.aibase.com/news/30126) ⭐️ 8.0/10

阿里巴巴发布 Qwen-Image-3.0，开放 Pro 和 Standard 两档 API 供开发者使用。文生图功能定价从每张 0.18 元起。 此次发布为开发者提供了一个性价比高且文字渲染能力强的图像生成选择，直接与同类模型竞争。这也提升了阿里巴巴在中国 AI 生态中的地位，而基准排名对模型采用至关重要。 Qwen-Image-3.0 在 Arena.ai 上位列中国模型第一，支持高达 4.5k tokens，可处理故事板、试卷和九宫格信息图等复杂版面。Pro 和 Standard 两档 API 提供不同的价格与性能选择，文生图每张图片 0.18 元起。

aibase · AIbase · 8月5日 12:16

**背景**: Arena.ai 是一个排行榜平台，用户可以在上面比较和排名文本、图像等不同模态的前沿 AI 模型。Qwen 是阿里巴巴开源大模型系列，Qwen-Image 则提供文生图能力。强大的文字渲染和长 token 支持，在生成海报、文档和结构化版式时尤为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arena.ai/leaderboard/">Arena Leaderboard | Compare &amp; Benchmark the Best Frontier AI Models</a></li>
<li><a href="https://arena.ai/leaderboard/text-to-image">Text-to-Image Leaderboard - Best AI Image Generators</a></li>

</ul>
</details>

**标签**: `#AI`, `#Image Generation`, `#Alibaba`, `#Qwen`, `#API`

---

<a id="item-9"></a>
## [京东开源 JoyAI-Video-Edit：30fps 实时视频编辑模型](https://www.aibase.com/news/30123) ⭐️ 8.0/10

京东开源了 JoyAI-Video-Edit，一个以每秒 30 帧进行推理的实时流式视频编辑模型，让用户可以边看边改视频。该模型已发布到 GitHub，据称在实时视频编辑各项指标上达到全球领先水平。 这标志着视频编辑从传统的先拍摄后剪辑模式，转向可实时交互的创作方式，有望改变创作者、直播主和开发者的工具生态。开源该模型降低了社区采用和扩展实时编辑能力门槛。 该模型通过渐进式图文生成与编辑课程，将双向编辑模型转换为分块因果编辑模型。它通过让处理与播放同步来解决延迟挑战，京东表示其性能优于现有代表性的实时流式视频编辑模型。

aibase · AIbase · 8月5日 11:16

**背景**: 传统视频编辑需要先录制素材，再在离线的后期步骤中应用修改。实时流式视频编辑则是在视频播放的同时处理开放式视频流，允许通过指令即时修改内容。这一方向建立在基于扩散模型的视频生成和编辑技术之上，这些模型根据文本提示生成或修改画面帧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jd-opensource/JoyAI-Video-Edit">GitHub - jd-opensource/JoyAI-Video-Edit · GitHub</a></li>
<li><a href="https://www.163.com/dy/article/L3IEQ1HH0511B8LM.html">视频能“边播边改”：京东开源自研JoyAI-Video-Edit模型|流式|edit|京东集团|知名企业|joyai_网易订阅</a></li>
<li><a href="https://arxiv.org/pdf/2608.03974">JoyAI- Video - Edit : Real - Time Open-Ended Video Editing with...</a></li>

</ul>
</details>

**标签**: `#AI`, `#video-editing`, `#open-source`, `#real-time`, `#JD.com`

---

<a id="item-10"></a>
## [Anthropic 向初创公司 Volta 下达 100 亿美元订单以确保 AI 电力](https://www.aibase.com/news/30120) ⭐️ 8.0/10

Anthropic 已向初创公司 Volta 下达据称约 100 亿美元的基础设施电力订单，而不是依赖亚马逊、微软或谷歌。这笔交易表明，电力而非资本已成为 AI 扩张的关键瓶颈。 这一交易打破了云巨头在 AI 基础设施上的主导地位，表明获取电力已成为决定谁能大规模建设的稀缺资源。其他 AI 实验室和数据中心开发商可能会效仿，与专注于电力的新兴供应商合作。 Volta 的做法据称通过预先获取电力接入、已批土地和监管许可，将 5-7 年的基础设施开发周期压缩到 12-18 个月。这笔交易也凸显出，三大云厂商在新数据中心电力交付时间上并不比新进入者更快。

aibase · AIbase · 8月5日 10:16

**背景**: AI 数据中心耗电量极大，而电网容量常常受限，因此运营商越来越多地签订长期购电协议（PPA）或建设表后发电设施。像 VoltaGrid 这样的初创公司通过天然气微电网和模块化基础设施为数据中心供电，而 Volta Infrastructure 则提前锁定电力、土地和许可以加快交付。现有云厂商同样面临漫长的并网排队，使得电力供应成为 AI 扩张的主要制约因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://voltagrid.com/data-centers">VoltaGrid - Data Centers</a></li>
<li><a href="https://www.voltainfra.com/platform">Platform — Volta</a></li>
<li><a href="https://www.computetape.com/learn/power-sourcing-for-ai/">Power Sourcing for AI : PPAs &amp; Behind-the-Meter | ComputeTape</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#power supply`, `#Anthropic`, `#cloud computing`, `#data centers`

---