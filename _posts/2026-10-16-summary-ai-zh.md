---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16 23:04:10 +0000
lang: zh
report: ai
---

> 从 166 条内容中筛选出 10 条重要资讯。

---

1. [Quanta 杂志报道：推动 AI 基准测试成为一门严谨科学](#item-1) ⭐️ 8.0/10
2. [Claude Code 团队：AI 评审正在重新定义人类代码评审的意义](#item-2) ⭐️ 7.0/10
3. [AWS 推出面向智能体编程的开源权重模型 Reflection Beam](#item-3) ⭐️ 7.0/10
4. [《自然》发文：面向全生命周期可持续材料发现的 AI 方法](#item-4) ⭐️ 7.0/10
5. [微型脑类器官“读取”盲文，生物混合计算迈出关键一步](#item-5) ⭐️ 7.0/10
6. [《纽约时报》报道陶哲轩站在 AI 与数学未来争论的最前线](#item-6) ⭐️ 7.0/10
7. [公民科学团体应对 AI 垃圾内容激增](#item-7) ⭐️ 6.0/10
8. [美国医学会发布医疗智能体 AI 治理框架](#item-8) ⭐️ 6.0/10
9. [奥兰多母亲就其 14 岁儿子自杀事件与 AI 公司达成和解](#item-9) ⭐️ 6.0/10
10. [法国 24 台：书籍被扫描并销毁，用于训练人工智能模型](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Quanta 杂志报道：推动 AI 基准测试成为一门严谨科学](https://news.google.com/rss/articles/CBMinAFBVV95cUxPMXlhU1kzY09uSjZ3ZkVzWTRGNDFNeHZYRlBPcGRkVHEtTGRhQUJlLVRUZHJHQXpzekdSWGNITDRIWms4LUxwbldZU09pQ01wLTBzY0hkYVoxbnpvWVItTEtsWE4yLV9NS280amEwMVNnRnR6Sl9jNlZZVFQycEVHNVFjTXd4VEhDRkpFT1hKWE5MVWRGTGRMTngtUUU?oc=5) ⭐️ 8.0/10

Quanta 杂志刊登了一篇人物报道，介绍一位研究者主张把 AI 基准测试（即用标准化测试给模型打分）发展成一门严谨的科学学科，而不是他所称的那种随意、缺乏记录的“黑暗艺术”。这篇文章把基准测试方法本身——而不仅仅是分数——当作值得严肃研究的对象。 基准测试分数如今越来越多地影响模型发布决策、研究经费分配、采购选择甚至 AI 政策讨论，因此不可靠或容易被“刷分”的基准可能会系统性地误导整个领域，让人误判哪些系统真的更优秀。把评测当作科学来对待，有望改善可复现性、让模型之间的横向比较更加公平，并为研究者和从业者的结论提供更可信的证据。 文章指出了当前评测实践中反复出现的方法论缺陷，例如结果高度依赖任意的随机种子、训练算力预算不公开、基准数据污染（测试数据泄漏进训练集），以及报告的分数缺少统计置信区间。该领域已有一些正式方案，比如 BenchCouncil 提出的“平衡 AI 基准测试”方法论，把评测拆解为若干明确组成部分，而不是只依赖排行榜上的单个数字。

google\_news · Quanta Magazine · 10月16日 16:59

**背景**: AI 基准测试是用来衡量和比较模型在特定任务（如问答、编程或推理）上表现的标准化测试或数据集，其结果通常汇总成公开的排行榜。机器学习领域长期面临与其他学科类似的“可复现性危机”：论文常常不公开代码、不记录超参数，或者只挑选对自己有利的实验结果。由于模型训练成本高昂、难以做绝对比较，基准测试已成为衡量进展的事实标准，因此其设计方式和统计严谨性影响格外重大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atticusli.com/replication-crisis/machine-learning-reproducibility/">Machine Learning &#x27;s Reproducibility Crisis : NeurIPS... | Atticus Li</a></li>
<li><a href="https://www.benchcouncil.org/aibench/training/">AIBench Training | Balanced AI Benchmarking , BenchCouncil</a></li>

</ul>
</details>

**标签**: `#AI benchmarking`, `#machine learning evaluation`, `#reproducibility`, `#AI research`, `#Quanta Magazine`

---

<a id="item-2"></a>
## [Claude Code 团队：AI 评审正在重新定义人类代码评审的意义](https://simonwillison.net/2026/Oct/16/code-review/) ⭐️ 7.0/10

在《How the Claude Code team does code review》一文中，Addy Osmani、Morgan Westlee Lunt 和 Qing Wang 提出：&quot;有没有人类读过这段代码&quot;只是对真正问题的一种不精确的替代指标，真正该问的是&quot;这次改动可能出什么问题，以及应当由自动化检查还是人类来捕获它&quot;。他们表示，评审如今已经变成持续进行的过程，大多数改动在请人类查看之前，至少已被 Claude 评审并修复过一次。 这标志着软件工程实践的一次转变：代码评审从拉取请求末尾的单一人工关卡，变为持续进行、基于风险的流程，由每次改动所携带的风险来决定采用自动化检查还是人工检查。若被广泛采纳，它将改变团队分配稀缺的资深工程师精力的方式，以及他们定义质量门禁的方式，从而影响几乎所有使用 AI 编码代理的开发者。 作者把评审描述为持续进行的、&quot;像写作时的拼写检查&quot;，声称这样可以捕获大多数常规错误，并把团队的注意力释放到更高层次的问题与审查上。该摘录篇幅简短，没有给出量化指标、工具细节，也未说明哪些检查仍需由人类完成，因此它更像是一种理念陈述而非技术报告。

rss · Simon Willison · 10月16日 22:06

**背景**: 传统上，代码评审是流程末端的一道关卡：开发者写代码、提交拉取请求，然后等待同事阅读 diff 之后才能合并。Claude Code 是 Anthropic 推出的代理式编码工具，能够理解代码库、编辑文件并在终端中运行命令，这使得 AI 代理可以在代码编写过程中实时检查改动。AI 代码评审工具如今已普遍接入持续集成流水线，在提交或拉取请求到达时自动触发；这篇文章主张，下一步应当是重新思考人类评审者究竟负责捕获哪一类问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://www.ibm.com/think/insights/ai-code-review">What is AI code review? - IBM</a></li>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#AI code review`, `#Claude Code`, `#Anthropic`, `#software engineering`, `#developer productivity`

---

<a id="item-3"></a>
## [AWS 推出面向智能体编程的开源权重模型 Reflection Beam](https://news.google.com/rss/articles/CBMivgFBVV95cUxPSElxZ0NWWkFqY3FmY29PN3JhMHRxSVo3eEJMLUYxMmtNNVl2LUlzNjZsU05heFlmby1aWFh4ZFRCRTRobDMwdjZvdGI1NlNCb1ZGRS0zMUdqQjJvRFpQb0JoN1NFLXhGdzI1WFl0Z0UtRWNVNWYySEZDV05GdGhzZHhsdU1BT3Z2Y09uWUo2TXZJZEY4ekotQVJYM0hWQ3VyWHJvSnU2WFU0T2JLVTNGSkVlcTk0c2M5amhJN01n?oc=5) ⭐️ 7.0/10

亚马逊云科技（AWS）发布公告，介绍了面向在 AWS 上运行的智能体编程（agentic coding）场景的开源权重模型 Reflection Beam。Beam 是 Reflection AI 的首个开源权重模型，采用稀疏混合专家（MoE）架构，总参数量 501B，每个 token 激活 23B 参数，面向编程、推理与智能体任务设计。 由大型云厂商支持的前沿级开源权重编程模型，为企业提供了可自行部署的替代方案，以取代 Claude Code 或基于 GPT 的智能体等闭源编程 API，这对成本控制、数据驻留和厂商锁定问题意义重大。同时也加剧了西方实验室与中国开源权重模型（如智谱 Z.ai 的 GLM 系列）之间的竞争。 经过指令微调的 Beam 模型已在 Hugging Face 上以 BF16、FP8 和 NVFP4 三种数值格式发布，可适配不同 GPU 精度需求；Reflection 声称其推理性能与智谱 Z.ai 的 GLM-5.2 持平，并优于许多西方开源权重模型。由于本条新闻在素材中仅有标题，AWS 具体的服务集成方式（例如是否上线 Bedrock 或 SageMaker）以及定价信息尚未得到确认。

google\_news · Amazon Web Services \(AWS\) · 10月16日 15:23

**背景**: 开源权重模型是指训练好的参数（权重）被公开发布的 AI 模型，任何人都可以下载、检查、在本地运行或进行微调，这与只能通过 API 访问的闭源模型不同。Reflection Beam 采用混合专家（MoE）架构，每个 token 只激活一小部分参数，因此 501B 总参数的模型每个 token 实际只需约 23B 参数的计算量。“智能体编程”指将大模型推理能力与读写文件、执行 shell 命令、搜索网页等工具结合起来的编程智能体，能够自主编写、测试和修改软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/reflection/Beam-1.0-501B-A23B">reflection / Beam -1.0-501B-A23B · Hugging Face</a></li>
<li><a href="https://www.marktechpost.com/2026/10/05/reflection-ai-introduces-beam-a-501b-open-weight-moe-model-with-23b-active-parameters-for-coding-and-agentic-workloads/">Reflection AI Introduces Beam : A 501B Open - Weight MoE Model ...</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**标签**: `#Agentic coding`, `#Open-weight models`, `#AWS`, `#AI agents`, `#LLM`

---

<a id="item-4"></a>
## [《自然》发文：面向全生命周期可持续材料发现的 AI 方法](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5vVHdtU29sd1FMbVJMRFBNclhrTlZYZlJfX2JnS2RGc29vUmF2NGs2TGlFVWtDRUdMTEVRaWMxakVMWkY4aTRiWkhVWC03MldoZVdndm9iNlFzbXNUQk5Z?oc=5) ⭐️ 7.0/10

《自然》（Nature）新发表了一篇题为《Artificial intelligence for life-cycle-aware sustainable materials discovery》（面向全生命周期可持续材料发现的人工智能）的文章，探讨如何利用人工智能与机器学习加速可持续材料的发现，同时将材料全生命周期的环境影响纳入考量。该工作不再只以性能或成本为优化目标，而是把生命周期评估（LCA）指标作为 AI 驱动发现流程的有机组成部分。 材料发现是脱碳努力的核心环节——电池、催化剂、光伏与结构材料都依赖它——但此前的 AI 模型通常只优化导电性、稳定性等材料属性，而忽略了从摇篮到坟墓的环境负担。将生命周期意识直接嵌入 AI 筛选流程，有助于研究者避免选出那些在开采、合成或回收阶段环境代价高昂的所谓“可持续”候选材料，进而可能重塑学术界与产业界规划研发优先级的思路。 该方法将用于预测材料属性的机器学习与生命周期评估相结合，后者是由 ISO 14040 和 ISO 14044 标准定义的一套系统化方法，用于盘点产品供应链中的能源、物质流与排放。一个关键挑战在于，LCA 数据往往稀疏、不确定，且高度依赖系统边界与假设条件，这意味着 AI 模型必须在常规材料描述符之外，同时处理带有噪声或不完整的环境数据。

google\_news · Nature · 10月16日 10:14

**背景**: 生命周期评估（LCA）是一种评估产品全生命周期各阶段环境影响的方法，涵盖从原材料开采、制造、分销、使用，到最终回收或处置的全过程，并由 ISO 14000 系列环境管理标准加以规范。另一方面，AI 材料发现利用机器学习、生成模型和高通量筛选，以远快于传统试错实验的速度提出并排序新的候选材料；近期发表在《Nature Materials》和《Nano-Micro Letters》等期刊上的综述也记录了该领域的快速演进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Life-cycle_assessment">Life-cycle assessment</a></li>
<li><a href="https://www.nature.com/articles/s41563-025-02403-7">Artificial intelligence-driven approaches for materials ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s40820-025-01945-4">Artificial Intelligence Empowered New Materials: Discovery ...</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#Materials Discovery`, `#Sustainability`, `#Machine Learning`, `#Life-Cycle Assessment`

---

<a id="item-5"></a>
## [微型脑类器官“读取”盲文，生物混合计算迈出关键一步](https://news.google.com/rss/articles/CBMizwFBVV95cUxNTlYwaVZfbHZfT1BsQ3lhWndiRUFNWGRKZ3lZY05ZS2h1RHhyWVR0RmwtLURMbnZndFBnUVFjd1M0dTI3RHA2TXdDZXNFSU41eHdFcGJzYkk1czZJbjR2UWhrTjdQTEttTUJ3bzQ5TnM0UkRPUWh2N0R4cGh3UVdMd3VzT01iX2Vtb1hxUnFoOXExcm9TX1Q1WUNtZmllZ3drM3R5U3RvNzdsTDJ3V05KYzJ1Wmx6THFDZU5MMHhaVm1OQ2YtN0JQdkJ3ekNZb3c?oc=5) ⭐️ 7.0/10

研究人员在 Frontiers 的一篇文章中报告，以人类前脑为模型培育的微型类器官能够对盲文式的点阵输入作出反应并“读取”这些模式，这是活体神经组织解读结构化信号的首次此类演示。该成果被视为迈向生物混合计算的关键一步，即在传统电子器件之外，把生物神经元当作计算介质来使用。 如果活体神经元能够可靠地编码和解码有规律的信息，它们就有可能成为极为节能的处理器，因为生物组织完成复杂模式识别所消耗的能量远低于硅基芯片。这使类器官智能与生物混合计算这一新兴领域更接近实际应用，并对低功耗计算、药物测试以及神经科学研究产生长远的潜在影响。 据该报道，实验中使用的类器官以人类前脑为模型，并专门用于探索高能效的生物混合计算。与大多数类器官研究一样，这种组织仅能模拟大脑发育的早期阶段，而长期存活能力、可重复性、可扩展性以及人类来源神经组织的伦理处理等实际障碍仍未解决。

google\_news · Frontiers · 10月16日 04:01

**背景**: 脑（大脑）类器官是实验室中通过培养多能干细胞、使其自组织成类似人脑部分结构的三维微型组织，被广泛用作神经发育与神经退行性疾病的体外模型。生物混合系统则把这类生物材料与电子器件、机械部件等人工组件结合起来，而“类器官智能”正是把这一思路用于计算。盲文是一种由凸起圆点构成的触觉书写系统，恰好可以作为结构化的输入模式来测试神经元的反应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain_organoid">Brain organoid</a></li>

</ul>
</details>

**标签**: `#biohybrid computing`, `#brain organoids`, `#neuroscience`, `#biocomputing`, `#Braille`

---

<a id="item-6"></a>
## [《纽约时报》报道陶哲轩站在 AI 与数学未来争论的最前线](https://news.google.com/rss/articles/CBMib0FVX3lxTE5obDJaUW0zTDU0Q2RqRGd6QlRabDFENjNiMTJtR0ZLOXkycWhXNjVlT2Vxc1hFRWhacTd6MEFyM01fU1c5UmNxME82N1VVVDFCWnBKWVZ0bDdvVXRZLXFXaldhNF83RG1keHVIV04xVQ?oc=5) ⭐️ 7.0/10

《纽约时报》发表文章，专门报道了澳大利亚裔数学家陶哲轩（Terence &quot;Terry&quot; Tao），聚焦他在关于人工智能将如何重塑数学的持续争论中所扮演的突出角色。文章审视了陶哲轩既作为 AI 工具使用者、又作为其数学研究影响的公共评论者的双重身份。 陶哲轩被广泛认为是当今最伟大的在世数学家之一，因此他的立场在塑造研究界如何看待 AI 辅助数学方面具有非同寻常的分量。随着机器学习工具逐渐能够证明定理、提出猜想，他的观点可能影响数学家、高校以及资助机构采纳或抵制这些技术的方式。 目前可获取的材料仅为标题和链接，没有文章正文，因此无法在此核实《纽约时报》文章中的具体论点、案例和引语。这篇文章应被理解为 AI 系统被应用于自动定理证明与数学发现这一更广泛趋势的一部分。

google\_news · The New York Times · 10月16日 20:15

**背景**: 陶哲轩 1975 年出生于南澳大利亚，是菲尔兹奖得主，其研究横跨数论、调和分析、偏微分方程与组合数学，常被认为是最伟大的在世数学家之一。自动定理证明是人工智能与数理逻辑中长期存在的一个子领域，指由计算机程序尝试构造数学定理的证明；早期乐观情绪曾一度消退，但随着现代机器学习的发展，该领域重新活跃起来。陶哲轩很早就将 AI 助手用于自己的数学工作，这使他的公开评论具有特别的公信力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2015/07/26/magazine/the-singular-mind-of-terry-tao.html">The Singular Mind of Terry Tao - The New York Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving - Wikipedia</a></li>
<li><a href="https://www.ebsco.com/research-starters/biography/terence-tao">Terence Tao | Biography | Research Starters | EBSCOhost</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#Terry Tao`, `#research`, `#future of math`

---

<a id="item-7"></a>
## [公民科学团体应对 AI 垃圾内容激增](https://news.google.com/rss/articles/CBMie0FVX3lxTE0tOHlmZ29mTmVUOUU1OGJ6NW0yRWo1c1lrVFV0VmNSd2FwMzViZGNtNWIyVHVmaVUwTERmeFVKZkhwN1R5Z0xmWHlDSS1IaG1kaUNoY3lnQUd5cVgzN3pIRGZGR3Y1V29Gc2hSbnRfX0NPRi1EVWZSM1RxMA?oc=5) ⭐️ 6.0/10

《纽约时报》报道称，公民科学团体正艰难应对日益增多的 AI 生成低质量内容（即所谓的“AI 垃圾内容”），这些内容正在影响他们的数据和工作流程。 这很重要，因为公民科学依赖志愿者贡献的数据，而 AI 垃圾内容会降低数据质量、浪费研究人员的时间，并破坏对众包研究的信任。它凸显了生成式 AI 使大规模生产低质量内容变得轻而易举所带来的更广泛挑战。 AI 垃圾内容指用生成式 AI 制作的、被认为缺乏努力、质量或意义的数字内容。在公民科学中，这可能表现为虚假观察、垃圾提交或需要过滤的低质量贡献，不过文章中的具体例子尚不可得。

google\_news · The New York Times · 10月16日 18:36

**背景**: 公民科学是由非科学家参与的科学研究的统称，例如鸟类计数或星系分类。AI 垃圾内容是指低质量 AI 生成内容在网上泛滥的术语。这两种趋势的交汇正迫使公民科学平台制定新的审核策略以维护数据完整性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_science">Citizen science - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI slop`, `#citizen science`, `#data quality`, `#crowdsourcing`, `#AI-generated content`

---

<a id="item-8"></a>
## [美国医学会发布医疗智能体 AI 治理框架](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPWHpsNFBWMDdsUVpza0hwN3BMeUZnSEhhdkNIWWNNS01KUWg2ZFZpLU5KSktYUFo2alVPQTJRQlV6eEZqdWo4cU50R2hXc19hb29pU1c3ZzJSVkl4dTY0Nk5yc3ZtUDRRV09NN1lsUmRmSmJrZTRxTXoyTU1fZGF3bEZ0MFlNQUVCTWQ3Wm9SUWpoNjdjSTRMTnBVQkkydTI5T2lJUG9BTHlSNzRnOGloTncyWXowOC1CcFJ0cDFTY0NCdw?oc=5) ⭐️ 6.0/10

美国医学会（AMA）正式发布了一套治理框架，用于指导医疗场景中智能体 AI（agentic AI）解决方案的部署。据 Fierce Healthcare 报道，这标志着这一大型医师组织开始正式回应自主式、多步骤 AI 系统应如何被治理的问题。 当美国医学会这样具有影响力的机构介入智能体 AI 议题时，说明自主式 AI 正从实验性试点走向临床现实，机构希望在规模化采用之前先建立护栏。这类指引可能会影响医院、厂商和监管者对“会行动而非仅仅提供建议”的 AI 系统在问责、安全与责任划分上的思考方式。 该框架针对的是智能体 AI——即能够围绕某个目标进行规划并执行多步骤行动的系统，而非仅根据提示生成文本的模型——这在临床环境中会带来独特风险，因为一次错误的自主操作可能直接影响患者安全。就目前报道而言，这只是一条标题式新闻，因此其具体条款、适用范围，以及它是自愿性指引还是强制性标准，在现有资料中均未详细说明。

google\_news · Fierce Healthcare · 10月16日 18:00

**背景**: 智能体 AI 指的是能够感知环境、做出决策，并为实现某一目标而跨多个步骤采取行动的 AI 系统，它超越了典型生成式 AI“单轮提示—回答”的行为模式。在医疗领域，这可能意味着智能体可以在有限人工监督下安排预约、总结病历或协调诊疗流程。美国医学会是美国最大的医师专业组织，经常发布影响临床实践与机构标准的政策性指引。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emrullahaydogan.medium.com/what-is-agentic-ai-and-why-everyones-talking-about-it-fba9da43e4c1">What Is Agentic AI — and Why Everyone’s Talking About It | Medium</a></li>
<li><a href="https://www.hostinger.com/ph/tutorials/what-is-agentic-ai">What is agentic AI ?</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#agentic AI`, `#healthcare AI`, `#policy`, `#responsible AI`

---

<a id="item-9"></a>
## [奥兰多母亲就其 14 岁儿子自杀事件与 AI 公司达成和解](https://news.google.com/rss/articles/CBMixwFBVV95cUxONGhRNVZTeFFpQk5FZHlfcDVFSDRqLS1fbThkMFlaWEVUdFY2N3RNZHdlSGpYMjBlVUtONDFEb0gyRGhIZ25WSlBrTDJQWmlCSzEtUzYzX2xaWGdpcGduZTJnNndHWW1SQTUwWDFUdmt5emxXWURpa2JpVzR3N1VvTDV3UVlIN2VGekowMm5VbTROR3NjZkNoQ3ZaWVBPbThHOUw5SVNBeVJ3Wjl3amlZdkgxYnRwRlBMeFdVZWxDNGRhNVNxdy1n?oc=5) ⭐️ 6.0/10

据 WKMG 报道，美国奥兰多一位母亲已就 14 岁儿子的死亡与一家人工智能公司达成和解。该和解终结了最早一批将 AI 聊天机器人服务商列为被告的过失致死诉讼之一，不过现有报道中并未披露和解的具体条款。 如果 AI 聊天机器人服务商可能因未成年人长期使用后受到伤害而被追责，那么陪伴型聊天机器人的设计、营销与年龄限制方式都将随之改变，同时也会为专门针对面向儿童的 AI 系统立法提供更强理由。和解虽避免了公开庭审判决，但它仍向业界释放出明确信号：因聊天机器人导致伤害而引发的诉讼风险真实存在，且代价高昂。 现有素材仅为 WKMG 的一条标题，因此 AI 公司的具体身份、和解金额以及是否约定安全改进措施，在来源中均未得到确认。此类案件通常同时主张过失责任与产品责任，原告方也曾提出《通信规范法》第 230 条对第三方内容的豁免并不自动适用于公司自身生成模型的输出内容。

google\_news · WKMG · 10月16日 21:50

**背景**: Character.AI、Replika 等 AI 陪伴型聊天机器人允许用户与 AI 生成的人格角色进行开放式、带有情感亲密性的对话，自 2023 年起在青少年中极为流行。自 2024 年以来，美国已有多个家庭起诉聊天机器人公司，指控其产品使未成年用户产生情感依赖，并在用户表达自残或自杀念头时未能及时干预。这些诉讼备受关注，因为它们正在检验长期以来适用于互联网的责任豁免规则与传统产品责任法能否适用于生成式 AI。

**标签**: `#AI safety`, `#AI ethics`, `#legal`, `#chatbots`, `#product liability`

---

<a id="item-10"></a>
## [法国 24 台：书籍被扫描并销毁，用于训练人工智能模型](https://news.google.com/rss/articles/CBMixAFBVV95cUxQT2N5ak5YY2JzWFEzOGdsM2owZlNCNEYxSFd0SmdZZnhMVEtSdW9vN2Z1Q1RQS2IzTE9RT0RHUmNzeTQwSWNpMHg0SS1kYUpuYlJEUXhuZVlZeGM5N3g0ZTl2X2F6ZFRSa0JGUmVHSXdFU0JSQ0dON0t5d19DcFkxWXBPdzUzOXNEenAyZDZaQ2lxbUh2ZHhvWU84OEY5Q0VVRlRjV2lTb0U0cmFsR0lZdk9MbmdPcldEeGxTVzJ0YmpKVlYz?oc=5) ⭐️ 6.0/10

法国 24 台的《Focus》栏目报道称，人工智能公司正成百万册地收购纸质书，将其拆解、逐页扫描为训练数据集，随后丢弃或销毁原书。该报道延续了此前的披露：Anthropic 曾为构建模型销毁数百万册纸质书，而亚马逊也被追踪到大量收购稀有和绝版书籍用于 AI 训练数据。 这凸显了 AI 训练数据需求与版权、文化保存及伦理之间日益加剧的冲突，因为许多被扫描的书籍从未获得作者或出版商的授权。由于稀有和绝版书籍往往不可替代，实体副本的销毁意味着不可挽回的文化遗产损失。 破坏性扫描通常需要切掉书脊，使单页能平整地送入高速扫描仪进行 OCR 识别，这比互联网档案馆那种翻页式非破坏性设备更快也更便宜。值得注意的是，OpenAI 与微软宣布与哈佛大学图书馆合作，用据称非破坏性的方式在近百万册图书上训练模型，说明兼顾保存的方法在规模化上也是可行的。

google\_news · France 24 · 10月16日 09:31

**背景**: 大型语言模型通过吸收海量文本来学习，在抓取完大部分公开网页后，AI 开发者转向书籍，因为书籍提供高质量、长篇且经过精心编辑的文字。&quot;破坏性图书扫描&quot;是一条工业化流水线：先切掉书脊，再将散页高速扫描，通过光学字符识别（OCR）把图像转为机器可读文本，并抽取元数据以构建干净的数据集。尽管一些公司主张，对合法购买的书籍进行训练属于合理使用，但作者和出版商对此提出异议，而这一做法还带来额外担忧：独一无二的实体副本会在过程中永久消失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2025/06/anthropic-destroyed-millions-of-print-books-to-build-its-ai-models/">Anthropic destroyed millions of print books to build its AI models</a></li>
<li><a href="https://www.erecordsusa.com/destructive-book-scanning-ai-training-data/">AI Book Scanning for Training Data: How Destructive Scanning ...</a></li>
<li><a href="https://actionmodel.com/blog/anthropic-buying-rare-books-feeding-ai-destroying-them">Anthropic Are Buying Rare Books , Feeding Them Into AI , Then...</a></li>

</ul>
</details>

**标签**: `#AI training data`, `#copyright`, `#books`, `#ethics`, `#media`

---