---
layout: default
title: "Horizon Summary: 2026-10-08 (ZH)"
date: 2026-10-08 23:03:56 +0000
lang: zh
report: ai
---

> 从 192 条内容中筛选出 10 条重要资讯。

---

1. [OpenAI 发布 GPT-6，新增可即时生成交互工具的“智能界面”](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Haiku 5.5，价格直降 90%](#item-2) ⭐️ 8.0/10
3. [微软发布 MAI Code1.1 Flash，GitHub Copilot 将支持本地与云端混合推理](#item-3) ⭐️ 8.0/10
4. [OpenAI 发布数百项 AI 生成的数学成果，数学界震动](#item-4) ⭐️ 7.0/10
5. [谷歌开源 EmbeddingGemma 2：不足 600MB 的端侧多模态搜索模型](#item-5) ⭐️ 7.0/10
6. [美国地方媒体起诉微软与 OpenAI，指控其未经授权用文章训练 AI](#item-6) ⭐️ 7.0/10
7. [开源 AI 初创公司 Nous Research 完成 9000 万美元 B 轮融资，估值达 15 亿美元](#item-7) ⭐️ 7.0/10
8. [美国政府新政策推动进入“超级智能”时代](#item-8) ⭐️ 6.0/10
9. [PFN 发布 PLaMo 3 Translate 31B，日本自主研发的翻译模型](#item-9) ⭐️ 6.0/10
10. [WordPress 7.1.3 紧急补丁修复 7 个漏洞，Anthropic 获致谢](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6，新增可即时生成交互工具的“智能界面”](https://www.aibase.com/news/31473) ⭐️ 9.0/10

OpenAI 发布了 GPT-6，并同步推出“智能界面”（Intelligent Interface）功能：模型可以根据用户提问，直接在聊天窗口内自动生成图表、按钮、表单和动态计算器等交互组件。用户可以让它当场创建一个分账工具、计算器或小游戏，并在对话框里直接操作，而不再只是阅读一段文字回答。 这标志着 AI 交互从纯文本问答转向“生成式 UI”，模型输出的不再是一段文字，而是一个可用的界面。如果这一能力能够大规模稳定落地，它可能改变数亿 ChatGPT 用户完成任务的方式，也会给目前依靠手工编写前端工具和仪表盘的开发者带来压力。 该公告在技术细节上相当简略：没有给出基准测试成绩、延迟数据、API 开放情况、定价，也没有说明 AI 生成的交互组件在安全方面如何处理。公开资料显示 GPT-6 并非单一模型，而是一个模型家族，包含 Astra、Sol 和 Luna 等版本，其中 Astra 被定位为 OpenAI 迄今最强、对齐程度最高的模型，覆盖计算机操作、编程、网络安全和科学研究等能力。

aibase · AIbase · 10月8日 16:01

**背景**: 生成式 UI（Generative UI）指的是一种前端架构：界面本身由 AI 模型生成，而不是完全由开发者手工硬编码。Google 的研究人员已经展示过这类系统，可以针对一条提示词生成完整的交互体验，例如网页、工具、游戏和应用。GPT-6 是 OpenAI 的下一代大语言模型家族，而“智能界面”把生成式 UI 的思路搬到了 ChatGPT 内部，使聊天窗口实际上成为 AI 生成小部件的运行环境，而不再只是一段对话记录。这也是它与早期插件或代码解释器类工具的区别所在——界面是针对每一次请求即时搭建出来的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/discover/generative-ui">What is Generative UI? Building Agent-Powered Interfaces</a></li>
<li><a href="https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/">Generative UI: A rich, custom, visual interactive user ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6">GPT-6 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#Generative UI`, `#Interactive Interfaces`, `#AI Models`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Haiku 5.5，价格直降 90%](https://www.aibase.com/news/31467) ⭐️ 8.0/10

Anthropic 在 Claude 5.5 系列中发布了轻量级模型 Claude Haiku 5.5，对 10 万 token 以内的常规请求，输入与输出价格分别降至每百万 token 0.10 美元和 0.50 美元，相比上一代官方定价下降约 90%。该模型定位于系列中最快的一档，并且是首个搭载自适应思考（adaptive thinking）与 effort 档位设置的 Haiku 模型。 入门级低延迟模型价格下降 90%，会显著降低实时客服、摘要抽取、数据分类等高频高并发场景的推理成本，使“又快又便宜”的模型真正具备大规模生产可用性。这也会对其他厂商的小模型定价形成压力，并影响“廉价模型先行、昂贵模型兜底”的级联路由策略的成本核算。 与模型一同推出的是分层定价机制（tiered pricing），自适应思考让模型自行决定投入多少推理算力，但推理过程产生的 token 同样计费。据 Artificial Analysis 的测算，Claude Haiku 5.5（max 档）在单个 Intelligence Index 任务上约消耗 16.2 万输出 token，比 Opus 5.5（max）还多，约为 GPT-6 Luna（max）的 3 倍，因此名义上的降价可能被更长的思考链部分抵消。

aibase · AIbase · 10月8日 14:01

**背景**: Haiku 是 Anthropic Claude 家族中体积最小、速度最快的一档模型，定位低于 Sonnet 和 Opus，面向那些更看重延迟与成本、而非极致推理能力的任务。大模型 API 按 token（分词器切出的近似词片段）计费，输出 token 的价格通常是输入 token 的 3 到 5 倍，因此输出量大、思考链长的任务才是真正烧钱的部分。“自适应思考”指的是推理模型会按请求动态分配内部推理算力，而这些推理 token 会被生成并照常计费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/articles/claude-haiku-5-5">Anthropic has released Claude Haiku 5 . 5 | Artificial Analysis</a></li>
<li><a href="https://openrouter.ai/docs/cookbook/evaluate-and-optimize/model-migrations/claude-5-5">Claude 5 . 5 Migration Guide | OpenRouter Documentation</a></li>
<li><a href="https://kie.ai/claude-haiku-5-5">Claude Haiku 5 . 5 API – Run the Fastest Claude 5 . 5 Model at... | Kie AI</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude Haiku`, `#LLM pricing`, `#AI models`, `#adaptive thinking`

---

<a id="item-3"></a>
## [微软发布 MAI Code1.1 Flash，GitHub Copilot 将支持本地与云端混合推理](https://www.aibase.com/news/31464) ⭐️ 8.0/10

在 2026 年 10 月 7 日举行的 Windows 与 Surface 新品发布会上，微软宣布 GitHub Copilot 将在本月底前支持端侧 AI 模型，开发者可以自由切换或在云端模型与本地模型之间自动调度。同时，微软推出了 MAI Code1.1 Flash 混合专家（MoE）编程模型，总参数量 1370 亿、激活参数 68 亿，旨在缓解边缘侧推理的内存瓶颈和长上下文带来的资源消耗。 这标志着 GitHub Copilot 从完全依赖云端的服务向混合架构转变，可能改变开发者对 AI 编程工具在延迟、成本、隐私和离线可用性方面的预期。这也表明微软愈发倾向于自研并交付自家编程模型，而不再完全依赖 OpenAI 的技术。 MAI Code1.1 Flash 将量化与投机解码（speculative decoding）结合使用——这是一种“先草拟、后验证”的技术，由小模型提出候选 token，再由大模型并行校验——从而在保证输出质量的前提下降低内存占用并加快生成速度。由于每个 token 只调用激活的专家子集，68 亿激活参数决定了单次请求的计算量和内存带宽，而 1370 亿总参数则代表模型所存储的整体知识；微软在发布会上以飞行模式演示了该模型的运行，但在本地运行它仍需要一台性能相当强的 PC。

aibase · AIbase · 10月8日 12:01

**背景**: GitHub Copilot 是微软的 AI 编程助手，此前其代码补全和对话功能都由运行在云端的模型生成，因此需要网络连接并产生按次计费的推理成本。混合专家（MoE）是一种模型架构，它把网络拆分为许多专门的“专家”子网络，每个 token 只被路由到其中少数几个专家，因此模型可以拥有极大的总参数量，而每次只有一小部分参数被激活。投机解码则是另一种推理期优化手段，能够在不改变模型输出质量的情况下加速 token 生成，自 2025 年前后已成为生产环境的标准做法。边缘侧或端侧推理指的是直接在用户自己的硬件上运行模型，以牺牲部分能力换取隐私保护、离线可用和更低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/alifar/microsoft-brings-mai-code-11-flash-local-inference-to-github-copilot-2j4d">Microsoft Brings MAI Code 1 . 1 Flash Local... - DEV Community</a></li>
<li><a href="https://www.neowin.net/news/microsofts-new-coding-ai-model-can-run-locally-but-youll-need-a-monster-pc/">Microsoft &#x27;s new coding AI model can run locally, but you&#x27;ll... - Neowi...</a></li>
<li><a href="https://www.automataai.com.au/blog/moe-architecture-active-vs-total-parameters-explained">MoE Architecture: Active vs Total Parameters Explained</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#GitHub Copilot`, `#AI models`, `#Mixture-of-Experts`, `#Edge AI`

---

<a id="item-4"></a>
## [OpenAI 发布数百项 AI 生成的数学成果，数学界震动](https://news.google.com/rss/articles/CBMijgFBVV95cUxPODBqdjFtSkFGUTZYd2w1WlRnaWFfX3NiWDJ4OXgzdGozcV94WFV1T2JWY0lrekg2ZGR6Sk1wMGtNMzNDeXFmdnc2Zl9zTk0zMDhCLXMyYUFVSjRVNk1CTkF2Y2h2VF9HRVZvV2xfRkpiUTJsQUlNV0ZnaFBTWGxJUW5mbkVEdjVuQ25HMHV3?oc=5) ⭐️ 7.0/10

OpenAI 公布了一批由尚未发布的内部前沿模型产出的新数学成果，共发布 722 篇手稿、归入 372 个成果族，并在 GitHub 上同步公开了 Lean 形式化证明与研究细节。据《纽约时报》报道，数学界对此次发布的规模与速度反应强烈，用“令人叹为观止”和“毁灭性”来形容。 此次发布表明，AI 系统已能在研究级数学的开放问题上做出贡献，且产出速度与数量远超人类学界所能匹敌的水平，这可能重塑数学研究的优先级排序、验证方式与成果归属。同时它也引发了令人不安的问题：若机器生成的成果持续快于人类审核速度，人类数学家的角色、研究节奏与职业前景将如何变化。 这些成果出自一个 OpenAI 尚未对外发布的内部前沿模型，公司为手稿配套提供了 Lean 形式化证明，使至少部分工作可以被机器检验，而不必仅凭信任接受。值得注意的是，这些产出被描述为针对多个开放问题的一系列结果，而非某一条轰动性的定理，而完整的验证负担在很大程度上仍落在人类数学家身上。

google\_news · The New York Times · 10月8日 21:53

**背景**: 自动定理证明是人工智能与数理逻辑中长期存在的一个分支，目标是让计算机程序证明定理，传统上依赖人工编写的搜索与演绎规则。近年来，大型语言模型开始与 Lean 等证明助手结合：Lean 是一种依赖类型编程语言和交互式证明环境，其中证明的每一步都由一个很小的可信内核检验，因此只要命题被忠实形式化，机器验证过的证明基本可以确认无误。这一点之所以重要，是因为数学是少数可以客观验证 AI 输出的领域之一，因而成为观察 AI 生成的研究成果如何被学术界吸收的早期试验场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/sharing-ai-progress-in-mathematics/">Sharing AI progress in mathematics - OpenAI</a></li>
<li><a href="https://www.unite.ai/openai-releases-722-math-manuscripts-from-an-unreleased-ai-model/">OpenAI Releases 722 Math Manuscripts From an Unreleased AI Model</a></li>
<li><a href="https://www.scientificamerican.com/article/openai-unleashes-hundreds-more-math-results-upon-a-field-already-in-shock/">OpenAI unleashes hundreds more math results upon a field ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Mathematics`, `#AI/ML`, `#Research Breakthrough`, `#Industry News`

---

<a id="item-5"></a>
## [谷歌开源 EmbeddingGemma 2：不足 600MB 的端侧多模态搜索模型](https://www.aibase.com/news/31476) ⭐️ 7.0/10

谷歌发布了开源多模态嵌入模型 EmbeddingGemma 2，体积不足 600MB，可将文本、图像、音频和视频编码到同一个 768 维向量空间中，实现跨模态检索。该模型可直接在手机和笔记本电脑上本地运行，无需联网即可完成图像、音频和视频搜索。 通过把多模态检索模型压缩到消费级设备可承载的体积，谷歌让用户不必把私人照片、音频或视频上传到云端，这对隐私保护型搜索意义重大。同时它也降低了开发者为移动端构建离线 RAG 与语义搜索应用的门槛，可能推动端侧 AI 从简单文本任务扩展到更多场景。 该模型基于 Gemma 4 架构，既能把单一模态，也能把同一输入中组合的多种模态编码进共享向量空间，支持检索、语义相似度、聚类和分类任务。谷歌的 AI Edge 工具链提供了端侧示例演示，但关于精度、延迟和所支持硬件的公开信息仍然有限，也缺乏广泛的第三方独立验证。

aibase · AIbase · 10月8日 17:01

**背景**: 嵌入模型把句子、图像、音频等非结构化数据转换成数值向量，使内容相近的数据在向量空间中彼此靠近，这是语义搜索和检索增强生成（RAG）的基础。多模态嵌入模型进一步把不同类型的数据放进同一个共享空间，让文本查询可以检索到匹配的图像或视频片段。早期 Gemma 系列主要面向文本，而要在端侧运行这类模型通常需要激进的量化和内存优化，因此一个不足 600MB 的多模态模型格外引人关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/transformers/model_doc/embedding_gemma2">EmbeddingGemma2 · Hugging Face</a></li>
<li><a href="https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/">EmbeddingGemma 2: The Developer Guide- Google Developers Blog</a></li>
<li><a href="https://developers.googleblog.com/en/google-ai-edge-with-embeddinggemma-2/">Bring multimodal semantic search to the edge with ...</a></li>

</ul>
</details>

**标签**: `#Google`, `#EmbeddingGemma2`, `#on-device AI`, `#multimodal search`, `#open source`

---

<a id="item-6"></a>
## [美国地方媒体起诉微软与 OpenAI，指控其未经授权用文章训练 AI](https://www.aibase.com/news/31466) ⭐️ 7.0/10

美国多家地方媒体对微软和 OpenAI 提起诉讼，指控这两家公司在其未获付费、也未获授权的情况下，将数万篇新闻报道用于训练 AI 模型。原告称，其受版权保护的新闻内容被用于构建商业化的生成式 AI 产品，却从未达成任何授权协议。 这起诉讼是新闻机构针对生成式 AI 开发者不断扩大的版权诉讼浪潮中的一例，其判决结果可能影响 AI 公司今后如何为训练所用的新闻内容获取授权、标注来源或支付费用。若被告被判败诉，可能推高训练数据的获取成本，并促使整个行业与出版方签订正式的内容授权协议。 案件的核心指控是未经授权使用了数万篇文章且未支付任何补偿，而此类诉讼通常围绕合理使用（fair use）抗辩以及训练数据的获取方式展开。目前公开报道尚未明确受理法院、文章的确切数量以及索赔金额等细节。

aibase · AIbase · 10月8日 14:01

**背景**: 像 OpenAI 旗下的这类生成式 AI 模型需要依赖从网络抓取的海量文本进行训练，其中很大一部分是受版权保护的新闻内容。出版方认为这属于对自己劳动成果的无偿使用，而 AI 公司通常主张，使用公开可获取的材料进行训练属于合理使用（fair use）。微软是 OpenAI 的重要投资方与合作伙伴，其 Bing、Copilot 等服务均依赖 OpenAI 的模型，因此在这些诉讼中常与 OpenAI 一同被列为被告。

**标签**: `#AI copyright`, `#OpenAI`, `#Microsoft`, `#legal`, `#media`

---

<a id="item-7"></a>
## [开源 AI 初创公司 Nous Research 完成 9000 万美元 B 轮融资，估值达 15 亿美元](https://www.aibase.com/news/31462) ⭐️ 7.0/10

成立三年的开源 AI 初创公司 Nous Research 确认完成 9000 万美元 B 轮融资，由 Robot Ventures 领投，NVIDIA、Union Square Ventures、Menlo Ventures、三星以及 1789 Capital 参投。本轮融资后公司估值达到 15 亿美元，累计融资总额达到 1.5 亿美元。 这是一个重要信号：不只是闭源前沿模型，开源的 AI 智能体同样能够吸引顶级企业资本和战略投资者——NVIDIA 和三星都在支持一家代码以宽松许可证免费开放的公司。这表明企业市场越来越愿意采用可自托管、由开发者驱动的智能体框架，这可能在价格和开放性两方面对闭源智能体厂商形成压力。 这轮热度的主要推动力是 Hermes Agent——Nous Research 采用 MIT 许可证的自托管智能体，具备持久记忆、从经验中生成技能、定时任务（cron）以及支持 Telegram、Discord 和 Slack 的消息网关等功能。Nous Research 此前以在 Hugging Face 上发布开源语言模型而闻名，因此这一估值反映的是模型训练与智能体工具两条产品线的综合价值，而非单一产品。

aibase · AIbase · 10月8日 12:01

**背景**: Nous Research 是美国开源 AI 运动的一员，专注于训练并公开以开放许可证发布语言模型，而不是将它们封闭在 API 之后。所谓“AI 智能体”是指超越单纯问答的系统，它能够调用工具、记住过往会话并自主执行多步骤任务。Hermes Agent 是该公司的主力智能体产品，以 MIT 许可证发布，任何人都可以运行或修改；而“B 轮融资”通常是公司在找到产品市场契合点后用于规模化扩张的风险投资轮次。对处于这一阶段的初创公司而言，15 亿美元估值意味着它已跻身“独角兽”行列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NousResearch/hermes-agent">GitHub - NousResearch/hermes-agent: The agent that grows with you</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent — Open-Source AI Agent That... | Nous Research</a></li>
<li><a href="https://nousresearch.com/">NOUS RESEARCH</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#open-source AI`, `#startup funding`, `#enterprise AI`, `#Nous Research`

---

<a id="item-8"></a>
## [美国政府新政策推动进入“超级智能”时代](https://news.google.com/rss/articles/CBMiwAFBVV95cUxONW5RalFyWmlnT3BaM2ZRYkI1clFIZEh0dVg3REp5dGpyNDQ1cFNwRDExU0xrZkkzNm4yc1FYejExR0FxaGgxUl9Od2ZDSW44bkk1NkZfQkgxWFA0OU5BVE1ieWtFR2hZTWRvR3RnUndjWVMxMTE3bHlmVmJlRFR0MW81N1BYRlBORXBNeU5GTF85SUZITjdrcF9GZFNWQWM2UjVNTmFPRU51aEdYTDRPWFFqWlNGbnRmV3NreTdOalc?oc=5) ⭐️ 6.0/10

El Cronista 的一则 Google News 标题报道称，美国政府的新政策标志着进入“超级智能”新时代，但文章正文在撰写时无法获取。相关报道显示，该政策的核心是一项行政命令，在联邦文件中将 AI 重新命名为“超级智能”，并成立了由国家情报总监 Jay Clayton 领导的“超级智能部队”（SIF）特别工作组。 如果这一政策得到证实，将标志着美国政府在 AI 政策的表述与组织方式上的一次显著转变——用语从“人工智能”上升到“超级智能”，并表明华盛顿优先考虑在先进 AI 领域的国家领导地位与安全，而非国际监管。这种定调可能影响联邦采购、研究资助、出口管制和外交立场，波及美国政府机构与私营 AI 开发者。 相关行政命令（被引为第 14409 号行政命令《促进先进人工智能》）声明，美国的政策是通过与私营部门合作来促进 AI 创新与安全、保护美国知识产权不被对手窃取，并培育先进的 AI 赋能能力。值得注意的是，改用“超级智能”一词在很大程度上是政策与品牌层面的决定，而非真正存在超级智能系统的证据，因为真正的人工超级智能目前仍属假设。

google\_news · El Cronista · 10月8日 19:15

**背景**: 超级智能（Superintelligence），或称人工超级智能（ASI），是一种假设中的人工智能，其认知能力在几乎所有领域都远超最杰出的人类心智；哲学家 Nick Bostrom 将其定义为“在几乎所有相关领域中认知表现都大大超越人类的心智”。目前并不存在这样的系统，研究人员距离造出它也仍然遥远，因此该词目前更多用于政策与思辨语境，而非工程实践。AI 治理指的是指导 AI 发展、以尽量减少偏见、安全威胁和隐私泄露等风险的政策与框架。美国的新做法与参议员 Bernie Sanders 提出的《禁止人工超级智能法案》形成对比——后者主张通过国际协议和出口管制来阻止全球范围内的超级智能研发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aimagazine.com/news/trumps-super-intelligence-force-us-ai-policy-explained">Trump&#x27;s Super Intelligence Force: US AI Policy Explained</a></li>
<li><a href="https://www.govinfo.gov/content/pkg/DCPD-202600376/pdf/DCPD-202600376.pdf">Executive Order 14409—Promoting Advanced Artificial ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence">Superintelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#superintelligence`, `#US government`, `#technology regulation`, `#AI governance`

---

<a id="item-9"></a>
## [PFN 发布 PLaMo 3 Translate 31B，日本自主研发的翻译模型](https://www.aibase.com/news/31470) ⭐️ 6.0/10

Preferred Networks（PFN）发布了 PLaMo 3 Translate 31B，这是一款基于 PLaMo 3 基座模型构建的翻译模型，训练数据中约 30% 为日语。上一代仅支持日语和英语，新模型将语言支持范围大幅扩展，并新增了覆盖 15 种语言的在线会议翻译模式。 这表明一款完全由日本自主研发的模型也能达到顶级翻译水平——PFN 声称其在四项权威翻译基准测试的平均分上超过了 OpenAI 的 GPT-6.1Sol 和 GPT-6Astra。对于需要高质量、本土研发语言基础设施的日本企业和公共机构而言，这意味着它们不必完全依赖美国模型厂商。 该模型拥有 310 亿参数，采用 PLaMo 社区许可证发布，商用需要另行提交申请；其基座为 PLaMo 3 NICT 日英双语模型，采用交错滑动窗口与全注意力混合的架构。与 OpenAI 模型的基准对比数据来自 PFN 官方声明，在发布时尚未经过第三方独立验证。

aibase · AIbase · 10月8日 15:01

**背景**: Preferred Networks（PFN）是一家以深度学习框架和工业 AI 闻名的日本人工智能公司，PLaMo 是其与日本信息通信研究机构（NICT）合作研发的国产大语言模型系列。专用翻译模型通常是在通用基座模型上进行微调，以专门强化跨语言任务，因此 PLaMo 3 Translate 被描述为构建在 PLaMo 3 之上。对日语数据的高度侧重，反映了日本推动“主权 AI”的整体趋势，即确保外国模型往往处理不佳的本国语言与文化覆盖能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/31470">PFN Releases PLaMo 3 Translate 31 B Model, Demonstrates...</a></li>
<li><a href="https://xix.ai/live/7730">Japan&#x27;s Preferred Networks launched PLaMo 3 Translate 31 B , a fu - xix.ai</a></li>
<li><a href="https://huggingface.co/pfnet/plamo-3-nict-31b-base">pfnet/plamo-3-nict-31b-base · Hugging Face</a></li>

</ul>
</details>

**标签**: `#machine translation`, `#NLP`, `#model release`, `#Japanese AI`, `#PLaMo`

---

<a id="item-10"></a>
## [WordPress 7.1.3 紧急补丁修复 7 个漏洞，Anthropic 获致谢](https://www.aibase.com/news/31460) ⭐️ 6.0/10

WordPress 于 10 月 6 日发布 7.1.3 版本，这是一次紧急更新，共修复了 7 个安全漏洞和 4 个程序缺陷。值得注意的是，AI 公司 Anthropic 报告了其中 3 个漏洞，与 Trail of Bits 等老牌安全团队一同出现在致谢名单中。 由于全球有极高比例的网站运行在 WordPress 之上，这种计划外的安全版本会迫使数百万站长、主机服务商和插件开发者尽快升级，否则就可能面临被攻击的风险。同时，一家 AI 实验室出现在漏洞报告者名单中，也说明漏洞发现的主体正从传统的安全研究员和漏洞赏金社区向外扩展。 该公告没有给出 CVE 编号、漏洞类型（如跨站脚本、SQL 注入或权限提升）以及严重等级，因此无法判断这 7 个问题中哪些风险最高。此类紧急小版本发布通常意味着至少有一个缺陷被认为足够严重，不能再等到下一个常规小版本才修复。

aibase · AIbase · 10月8日 11:01

**背景**: WordPress 是一款开源内容管理系统，支撑着公共网络上极大比例的网站，因此它的安全版本影响面异常广泛。漏洞通常通过协同披露流程处理：外部研究人员或机构私下报告缺陷，维护者开发并测试修复方案，随后在发布说明中对报告者致谢。紧急版本不属于常规更新节奏，只用于那些在例行版本发布前就可能被实际利用的问题。本次致谢名单中的 Trail of Bits 之一，就是知名的安全研究与工程公司。

**标签**: `#WordPress`, `#Security`, `#Vulnerabilities`, `#Anthropic`, `#CMS`

---