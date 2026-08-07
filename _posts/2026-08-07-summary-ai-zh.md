---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
report: ai
---

> 从 278 条内容中筛选出 10 条重要资讯。

---

1. [AI 生成的噬菌体基因组中 16 个在实验室得到验证](#item-1) ⭐️ 9.0/10
2. [ChatGPT 接入 Adobe 全家桶，自然语言即可调用 70 余款创意工具](#item-2) ⭐️ 8.0/10
3. [OpenAI 发布 Agent Plugins 标准 1.0.0，统一 AI 智能体插件](#item-3) ⭐️ 8.0/10
4. [字节跳动押注 50 万亿参数大模型，内部禁止蒸馏](#item-4) ⭐️ 8.0/10
5. [ChatGPT 免费版获无限 GPT-5.6 Luna，付费用户享 Sol](#item-5) ⭐️ 8.0/10
6. [ChatGPT 重大更新：免费用户升级 GPT-5.6 Luna 并获无限聊天](#item-6) ⭐️ 8.0/10
7. [Codex 与 GPT-5.6 Sol Ultra 联手打造超越 Claude Fable 5 的浣熊抢劫游戏](#item-7) ⭐️ 7.0/10
8. [《自然》综述审视 AI 在药物发现中的现状与未来路径](#item-8) ⭐️ 7.0/10
9. [AI 与化学结合拓展电池电解液设计空间](#item-9) ⭐️ 7.0/10
10. [高盛预测 2026 年全球 AI 投资将超过 1 万亿美元](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 生成的噬菌体基因组中 16 个在实验室得到验证](https://www.aibase.com/news/30192) ⭐️ 9.0/10

斯坦福大学和 Arc 研究所的研究人员使用 Evo 基因组语言模型生成了约 70 万个候选噬菌体序列，合成了其中 285 个，并确认有 16 种噬菌体能够复制、感染并杀死大肠杆菌。该研究成果于 8 月 6 日发表在《科学》杂志上。 这一里程碑将生成生物学从单一蛋白质设计推进到完整病毒基因组的从头创建，证明 AI 仅凭 DNA 序列就能生成具有功能的生物制剂。同时，它也引发了双重用途的安全担忧，因为同样的方法可能被用于更危险的病原体。 Evo 是一个拥有 70 亿参数的基因组基础模型，训练数据为 OpenGenome，这是一个包含约 3000 亿个 token 的原核生物全基因组数据集，上下文长度为 131 千碱基，分辨率达到单核苷酸水平。尽管候选序列数量庞大，但在 285 个合成序列中只有 16 个被验证为有功能的噬菌体，这凸显了序列生成与生物适应性之间的差距。

aibase · AIbase · 8月7日 14:47

**背景**: 基因组语言模型（gLMs）借用自然语言处理的技术，将 DNA 序列视为由 A、C、G、T 四个字母组成的“文本”，并从大规模基因组数据集中学习统计模式。Evo 就是这样一个模型的例子，它能够从分子尺度到基因组尺度预测和生成 DNA 序列。此前，生成生物学主要专注于设计新型蛋白质，而这项工作将该方法扩展到整个病毒基因组，为生物技术和合成生物学开辟了新的可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/evo-design/evo">GitHub - evo-design/evo: Biological foundation modeling from ...</a></li>
<li><a href="https://www.science.org/doi/10.1126/science.ado9336">Sequence modeling and design from molecular to genome scale ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#generative biology`, `#genomics`, `#viral genomes`, `#biosecurity`

---

<a id="item-2"></a>
## [ChatGPT 接入 Adobe 全家桶，自然语言即可调用 70 余款创意工具](https://www.aibase.com/news/30185) ⭐️ 8.0/10

Adobe 扩大与 OpenAI 的合作，使 ChatGPT 用户可以通过自然语言指令调用包括 Photoshop 和 Premiere 在内的 70 多款创意应用。该集成基于 OpenAI Apps SDK，从 8 月 6 日起将覆盖 Adobe 几乎全系列工具，用户可在设置中添加插件。 此举将 ChatGPT 从文本聊天助手带入专业创意工作流，无需切换软件即可完成 AI 辅助修图、视频制作和 PDF 生成。它巩固了 OpenAI 在创意产业生态中的地位，也为 AI 与专业工具深度融合树立了先例。 该集成由 OpenAI Apps SDK 提供支持，其内部使用模型上下文协议（MCP）保持服务器、模型和界面同步。虽然去年已开始支持部分工具，但 8 月 6 日起的扩展将覆盖 Adobe 几乎全套应用，用户需在 ChatGPT 设置中添加插件。

aibase · AIbase · 8月7日 10:47

**背景**: OpenAI Apps SDK 是 OpenAI 官方提供的开发工具包，用于构建直接集成到 ChatGPT 中的自定义连接器（即“应用”）。这些应用依赖模型上下文协议（MCP）这一开放标准，该标准统一了线路格式、身份验证和元数据，使 ChatGPT 能够像处理内置工具一样调用外部工具。Adobe 的合作正是这一生态从聊天扩展到专业软件领域的实例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Apps_SDK">OpenAI Apps SDK</a></li>
<li><a href="https://github.com/openai/openai-apps-sdk-examples">GitHub - openai/openai-apps-sdk-examples: Example apps for the Apps SDK · GitHub</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#Adobe`, `#AI integration`, `#Creative tools`, `#OpenAI`

---

<a id="item-3"></a>
## [OpenAI 发布 Agent Plugins 标准 1.0.0，统一 AI 智能体插件](https://www.aibase.com/news/30183) ⭐️ 8.0/10

OpenAI 发布了 Agent Plugins 标准（1.0.0 版），这是一个开放、与厂商无关的标准，将可复用的 AI 智能体组件（Agent Skills 和 MCP servers）打包为便携插件。该规范定义了一种通用格式，使兼容的客户端能够以相同规则发现和加载插件，不受平台限制。 此举旨在终结 AI 智能体插件生态碎片化的局面，让开发者只需一次构建，即可在不同智能体和客户端中运行。作为 OpenAI 提出的早期生态定义规范，它可能塑造 AI 智能体的扩展方式，并加速跨平台互操作性。 1.0.0 规范涵盖两个核心概念：Agent Skills，为 AI 智能体提供可复用的指令和资源；以及 MCP（Model Context Protocol）服务器，将智能体连接到工具和服务。该标准托管在 agentplugins GitHub 组织下，规范发布在 agent-plugins.org。

aibase · AIbase · 8月7日 10:47

**背景**: Agent Plugins 建立在两种现有的开放格式之上：Agent Skills——一种轻量级开放格式，一个技能就是一个包含 SKILL.md 文件的文件夹；以及 MCP——一个开放协议，它标准化了应用程序向 LLM 提供上下文的方式，常被描述为“AI 应用的 USB-C 接口”。新标准定义了一种可移植的包格式，将这些组件打包在一起，使兼容的客户端能够一致地加载它们。OpenAI 的参与，连同其 Agents SDK 和更广泛的智能体生态，表明业界正努力为跨供应商扩展 AI 智能体创建一种通用语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agent-plugins.org/">Agent Plugins</a></li>
<li><a href="https://vercel.com/blog/introducing-agent-plugins">Introducing Agent Plugins - Vercel</a></li>
<li><a href="https://github.com/agentplugins/agent-plugins-spec">GitHub - agentplugins/ agent - plugins - spec : Agent Plugins ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#OpenAI`, `#interoperability`, `#standards`, `#plugins`

---

<a id="item-4"></a>
## [字节跳动押注 50 万亿参数大模型，内部禁止蒸馏](https://www.aibase.com/news/30181) ⭐️ 8.0/10

据报道，字节跳动正在规划参数量达 50 万亿的大语言模型，规模将超过 Kimi K3 与 Qwen 3.8-Max。该计划仍处于早期阶段，由项亮和沈科牵头，张一鸣已下令内部禁止使用知识蒸馏技术。 如果实现，这将成为中国最大、也可能是全球最大的大语言模型之一，有望重塑 AI 竞争格局。此举表明字节跳动致力于原创基础模型研究，而非依赖蒸馏或模仿竞争对手的模型。 该项目仍处于早期讨论阶段，字节跳动正在围绕它重组 Seed AI 部门。报告中的参数规模存在不一致：标题为 50 万亿，而正文写的是“超过 5 万亿”，因此确切规模尚未证实。

aibase · AIbase · 8月7日 09:47

**背景**: 知识蒸馏是一种机器学习技术，将知识从大模型迁移到小模型，使 AI 模型更便宜、运行更快。字节跳动 Seed 团队成立于 2023 年，专注于大语言模型、语音、视觉和世界模型等领域。Moonshot AI 于 2025 年 7 月发布的 Kimi K3 拥有 2.7 万亿参数，是目前最大的开源权重模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_%28AI%29">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://seed.bytedance.com/">ByteDance Seed</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#ByteDance`, `#Industry News`, `#Model Training`

---

<a id="item-5"></a>
## [ChatGPT 免费版获无限 GPT-5.6 Luna，付费用户享 Sol](https://www.aibase.com/news/30180) ⭐️ 8.0/10

OpenAI 本周开始推出 ChatGPT 重大更新，免费用户将获得 GPT-5.6 Luna 模型的无限文本对话。与此同时，Plus 和 Pro 付费用户可使用 GPT-5.6 Sol，该模型准确度和回答质量更高。 这次更新意义重大，因为它首次让免费用户无限制使用新一代强大模型，可能扩大 ChatGPT 的用户群并加剧 AI 聊天机器人市场的竞争。同时，付费用户获得旗舰版 Sol 模型，也让订阅服务的吸引力大增。 GPT-5.6 是一个包含三档模型的产品系列：Luna、Terra 和 Sol。免费用户可无限使用 Luna 进行聊天，付费用户则使用 Sol；Sam Altman 表示 Sol 相比之前模型有大幅改进。

aibase · AIbase · 8月7日 09:47

**背景**: OpenAI 于 2026 年 7 月 9 日发布了 GPT-5.6 系列，包含三个按能力排序的变体：Luna、Terra 和 Sol。Luna 是最快、最具成本效益的模型，适合摘要、起草等日常任务；Sol 则是旗舰模型，针对编程、科学和网络安全进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techjournal.org/openai-gpt-5-6-sol-terra-luna">GPT-5.6 Explained: Sol, Terra &amp; Luna (July 2026)</a></li>
<li><a href="https://www.layer3labs.io/guides/gpt-5-6-luna-explained">GPT-5.6 Luna Explained: The Cheap, Fast Tier - layer3labs.io</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#GPT-5.6`, `#AI product update`, `#LLM`

---

<a id="item-6"></a>
## [ChatGPT 重大更新：免费用户升级 GPT-5.6 Luna 并获无限聊天](https://www.aibase.com/news/30179) ⭐️ 8.0/10

OpenAI 宣布对 ChatGPT 进行重大改版：免费用户和 Go 用户默认升级至 GPT-5.6 Luna 模型，下周起无限文本聊天，并新增“思考”按钮用于高级推理。付费用户则可使用滑块调整每次回答的思考深度。 此次更新大幅将 OpenAI 最新的高性价比模型开放给免费用户，同时让付费用户能更精细地控制推理深度。这可能重塑数百万用户与 AI 助手的交互方式，使先进 AI 更易获取且更具可定制性。 GPT-5.6 Luna 是 OpenAI 最具成本效益的模型，定价为每百万输入 token 0.10 美元、每百万输出 token 0.60 美元，上下文窗口为 1,050,000 个 token。文件上传和图像生成的细节尚未披露，“思考”按钮带有反滥用保护机制。

aibase · AIbase · 8月7日 09:47

**背景**: OpenAI 此前发布的 GPT-5.6 系列包括旗舰模型 Sol、适合日常平衡工作的 Terra，以及面向高容量工作负载的最具成本效益的 Luna。免费版和 Go 用户的无限文本聊天将于下周启用。新的思考深度滑块建立在 ChatGPT 现有的推理模式（Instant、Thinking 和 Pro）之上，让用户能在速度与深度推理之间进行权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-luna">GPT-5.6 Luna - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://aitoolsclub.com/how-to-use-chatgpts-new-thinking-time-to-control-gpt-5s-speed-and-depth/">How to Use ChatGPT’s New Thinking Time to Control GPT-5’s ...</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#OpenAI`, `#GPT-5.6`, `#AI product update`, `#language model`

---

<a id="item-7"></a>
## [Codex 与 GPT-5.6 Sol Ultra 联手打造超越 Claude Fable 5 的浣熊抢劫游戏](https://simonwillison.net/2026/Aug/7/moonlight-mayhem/#atom-everything) ⭐️ 7.0/10

Simon Willison 用 Codex Desktop 搭配 GPT-5.6 Sol Ultra 运行了完全相同的游戏构建提示，结果产出了远比 Claude Fable 5 早期版本更好的游戏《Moonlight &amp; Mayhem》。整个项目耗时 52 分钟，按完整 API 价格估算成本为 23.28 美元。 这次实际对比为两个前沿 AI 编程代理——OpenAI 的 Codex 搭配 GPT-5.6 Sol Ultra 与 Anthropic 的 Claude Fable 5——处理同一开放式创意编程任务提供了实证。它凸显了基于子代理的工作流日益增强的能力，可以直接从一次性提示中产出精致且可玩的游戏。 一次性输出存在一个缺陷：每只浣熊的眼睛变成了一个巨大的黑色球体，而 Codex 在审查截图时未能发现；Simon 通过提示“为什么浣熊身上有巨大的黑色球体？”然后再说“修复它”解决了问题。他还将完整的 Codex 对话记录、生成的纹理和提示发布在项目的 GitHub 仓库中。

rss · Simon Willison · 8月7日 19:18

**背景**: Codex Desktop 是 OpenAI 推出的桌面端编程代理应用；GPT-5.6 Sol 于 2026 年 7 月 9 日发布，在编码和知识工作方面树立了新标准，其 Ultra 模式将多代理编排能力融入模型本身，使一次 Sol 调用就能并行生成并协调多个子代理。Claude Fable 5 是 Anthropic 于 2026 年 6 月公开发布的“Mythos 级”模型，并为 Anthropic 的编程代理 Claude Code 提供支持。这次对比展示了编排多个 AI 子代理可以显著提高诸如从简单前提构建游戏这类复杂、长周期编码任务的质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://openai.com/index/introducing-the-codex-app/">Introducing the Codex app | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#code generation`, `#LLM comparison`, `#game development`, `#GPT-5.6`

---

<a id="item-8"></a>
## [《自然》综述审视 AI 在药物发现中的现状与未来路径](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5PRnBXREdkUzdBRklQY3VoTXdBbm96TU5uckNwS2ZhX2ZsUmc3eFdpREpSeXREZlFwZ0twM2o3RlAtajBNaEMyNWpzeTZMN2hpalBfT05xUzNzUVJkZ0t3?oc=5) ⭐️ 7.0/10

《自然》杂志新发表的一篇综述文章，回顾了人工智能在药物发现领域的当前状态、挑战和未来方向。这是一篇综合性的述评，而非某一项实验突破的报告。 这篇综述意义重大，因为人工智能在降低药物研发成本和时间方面正变得日益关键，但该领域仍面临验证和数据方面的挑战。它为研究者和制药公司提供了一张路线图，帮助其将精力聚焦在 AI 最能产生影响的领域。 该综述可能涵盖虚拟筛选、分子对接和全新药物设计等计算方法及其局限。它强调，AI 模型需要严格的基准测试、高质量的数据，并与实验验证相结合，才能在临床上有用。

google\_news · Nature · 8月7日 09:50

**背景**: 人工智能在药物发现中的应用，是利用机器学习预测小分子与生物靶标之间的相互作用，并生成新的候选药物。虚拟筛选通过计算手段从大型化合物库中筛选出有潜力的先导化合物；分子对接则预测配体与靶标之间的优势结合构象和亲和力。全新药物设计则更进一步，从零开始生成全新的分子结构。这些计算技术已存在数十年，但深度学习的进展极大增强了它们的能力和应用范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Virtual_screening">Virtual screening</a></li>
<li><a href="https://en.wikipedia.org/wiki/Molecular_docking">Molecular docking</a></li>
<li><a href="https://en.wikipedia.org/wiki/De_novo_drug_design">De novo drug design</a></li>

</ul>
</details>

**标签**: `#AI`, `#drug discovery`, `#healthcare`, `#machine learning`

---

<a id="item-9"></a>
## [AI 与化学结合拓展电池电解液设计空间](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZW9DbFdpeTh0emlXSEkxaE9FdmFuTlhraFZQbWtwSGtVMWUwUWM0SWc3dkVHaVo1T01EZEphSnlzR0pZT1llVUluNzlHSFJhSE5NdXBfckFYTDZfWXdOVTIxNEhuQXlPVEFrMno4NHRuUnlWZTY2eUpWY3ZneHBnYkpOWHI3bFFORTZoclNuNGVuVlFOR0pWMzFVdTk?oc=5) ⭐️ 7.0/10

康奈尔大学的一篇研究报道称，将人工智能与化学知识相结合可以拓宽电池电解液的设计空间，使研究人员能比传统方法探索更多候选材料。 拓展电解液设计对于提升电池性能、安全性和成本至关重要。这种 AI 与化学相结合的方法可以加速材料发现，并有助于开发下一代储能技术。 文章摘要未提供具体方法和结果，但该工作凸显了机器学习在分子与材料科学中日益重要的作用。康奈尔纪事报的文章可能描述了 AI 模型如何提出或筛选化学家可能忽略的新型电解液配方。

google\_news · Cornell Chronicle · 8月7日 18:00

**背景**: 电池电解液是让离子在电极之间移动的介质，其组成对电池性能影响很大。传统的电解液设计在很大程度上依赖试错法和高通量筛选，速度慢且范围有限。机器学习和生成式分子设计越来越多地被用来探索广阔的化学空间，并在实验验证之前预测有前景的候选材料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s42256-024-00843-5">Machine learning-aided generative molecular design - Nature</a></li>
<li><a href="https://www.nature.com/articles/s41586-018-0337-2">Machine learning for molecular and materials science - Nature Molecular machine learning in chemical process design ... Machine-Learning-Driven Molecular Design and Structure ... - MDPI Generative AI for the Design of Molecules: Advances and ... Inverse molecular design using machine learning: Generative ... Images</a></li>
<li><a href="https://en.wikipedia.org/wiki/High-throughput_screening">High-throughput screening - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#chemistry`, `#battery`, `#electrolyte`, `#materials science`

---

<a id="item-10"></a>
## [高盛预测 2026 年全球 AI 投资将超过 1 万亿美元](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOeDZ2dUk3YUJGenFKNm9feDlCc3RxZU9jaXA0WkYxM21uY2dBVmpGXzVMVkQtSXpUbjNEVEJjSGY0M1ZWcExLZ0U1dFNfaVhRc3FSV0IwOXJRMWwwLXpkQTE5RWZvYXBIV1B3NVVvUTdscUlScm5id29aRnNXVEF1OU56T25qbnAwV3dVNUJTZDdaVF8tRHE1SExhb1g5TThkQ0tHbWxBNlI?oc=5) ⭐️ 7.0/10

高盛发布预测，全球在人工智能领域的投资将在 2026 年超过 1 万亿美元。这一预测表明与 AI 相关的资本支出将大幅加速。 来自这家领先金融机构的预测凸显了 AI 在各行业采用的规模和势头。它为投资者、政策制定者和规划长期 AI 战略的公司提供了基准。 该估算可能涵盖 AI 基础设施的支出，包括数据中心、半导体和电力系统，以及软件和服务。与当前 AI 相关投资水平相比，1 万亿美元的数字代表显著增长。

google\_news · Goldman Sachs · 8月7日 18:56

**背景**: 人工智能投资是指将资本支出投入到 AI 技术中，例如计算硬件、数据中心建设和算法研究。受生成式 AI 和大语言模型进步的推动，各大科技公司和政府一直在增加 AI 资金投入。高盛的报告从宏观角度阐述了未来几年 AI 支出可能如何增长。

**标签**: `#AI`, `#investment`, `#industry trends`, `#economics`, `#forecast`

---