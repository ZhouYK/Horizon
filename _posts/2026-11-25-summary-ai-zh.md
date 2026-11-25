---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25 23:03:35 +0000
lang: zh
report: ai
---

> 从 156 条内容中筛选出 8 条重要资讯。

---

1. [腾讯混元开源 224B Hy4 Flash 的 GGUF 量化权重，64GB Mac mini 也能跑](#item-1) ⭐️ 8.0/10
2. [OpenAI 称 GPT-6 无需专用生物模型即可设计蛋白质](#item-2) ⭐️ 8.0/10
3. [Simon Willison 总结十二个月内大模型的三个拐点](#item-3) ⭐️ 7.0/10
4. [PrismML 三值压缩模型 Bonsai 2.5 27B：内存降至九分之一，保留 93.7% 编程能力](#item-4) ⭐️ 7.0/10
5. [LibreOffice 母机构 TDF 出台严格 AI 编程规则，规范 AI 辅助代码贡献](#item-5) ⭐️ 7.0/10
6. [黄仁勋回归英伟达，重燃华盛顿对华芯片准入之争](#item-6) ⭐️ 6.0/10
7. [欧盟据报计划向人工智能投资 500 亿欧元](#item-7) ⭐️ 6.0/10
8. [蚂蚁集团发布医疗 AI 安全防护模型 LingSante MedGuard](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [腾讯混元开源 224B Hy4 Flash 的 GGUF 量化权重，64GB Mac mini 也能跑](https://www.aibase.com/news/32527) ⭐️ 8.0/10

11 月 25 日，腾讯混元通过其模型压缩工具箱 AngelSlim 开源了 224B 参数模型 Hy4 Flash 的 GGUF 量化权重与推理代码，共提供 Q4\_K\_M、Q3\_K、IQ2-AH 以及 Spark 4-bit 等多个量化档位。其中最小的 IQ2-AH 版本约 125.73 GiB，仅为原始约 410.27 GiB 的 30% 左右，配合 Strata offload 框架可在 64GB 的 Mac mini 上运行。 一个 224B 级别的模型能被塞进消费级台式机的统一内存中，大幅降低了在本地运行超大模型的门槛，把过去需要多卡服务器才能承载的能力搬到了单台 Mac mini 上。评测分数几乎无损也说明激进的低比特量化正在从实验走向实用，这对注重隐私、需要离线运行或受成本约束的部署场景意义重大。 腾讯称 Q3\_K 版本（约 144.70 GiB）在 DeepSWE v1.1 等评测中与原模型的得分差距不超过 0.4 分；在 48GB 显存设备上 10K 上下文时生成速度达每秒 89 个 token，而在 128GB 的 M5 Max 上使用 Q3\_K、32K 上下文时约为每秒 47 个 token。这些数字依赖 Strata offload 框架在不同内存层级之间搬运权重，因此实际速度会很大程度上取决于存储带宽和所选的量化档位。

aibase · AIbase · 11月25日 16:01

**背景**: GGUF 是 llama.cpp 以及众多本地推理引擎用来存放量化模型权重的文件格式，Q4\_K\_M、IQ2\_AH 这类命名分别表示比特宽度和量化方案，数字越小文件越小、但可能损失更多精度。AngelSlim 是腾讯混元的模型压缩工具箱，集成了量化、投机解码、token 剪枝和蒸馏等技术。Strata 则是一个第三方开源推理引擎，通过把不活跃的层在显存、系统内存和 NVMe 存储之间调度，让消费级硬件也能运行超大规模模型，因此同一时刻只需驻留一部分权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mljourney.com/gguf-quantization-formats-explained-q4_k_m-q5-q8-and-more/">GGUF Quantization Formats Explained: Q4_K_M, Q5, Q8 and More</a></li>
<li><a href="https://stratallm.org/">Strata LLM – Run 125B+ MoE Models on 12GB VRAM Consumer GPUs ...</a></li>
<li><a href="https://github.com/Tencent/AngelSlim">GitHub - Tencent / AngelSlim : Model compression toolkit engineered...</a></li>

</ul>
</details>

**标签**: `#LLM quantization`, `#GGUF`, `#Tencent Hunyuan`, `#local inference`, `#open-source AI`

---

<a id="item-2"></a>
## [OpenAI 称 GPT-6 无需专用生物模型即可设计蛋白质](https://www.aibase.com/news/32513) ⭐️ 8.0/10

11 月 24 日，OpenAI 发布了一篇预印本论文，显示其 GPT-6 系列模型无需任何专用生物模型，仅凭推理能力和通用编程工具就能设计蛋白质的三维结构与氨基酸序列。在与生物技术公司 Onava 的合作中，团队以 GPT-6.2 的设计为蓝本合成了 322 个覆盖 5 个靶点的微型结合蛋白并进行湿实验验证，其中约 10%（约 10.9%）出现了结合迹象。 如果通用聊天模型也能做出有意义的蛋白质设计，这意味着通用推理模型可能减少对扩散类蛋白质生成器等专用工具的依赖，从而降低缺乏结构生物学机器学习积累的实验室的入门门槛。这也表明 OpenAI 正从聊天机器人向 AI 药物发现领域扩张，而该领域目前由专注生物 AI 的公司领跑。 报道中的约 10.9%结合命中率明显低于专用结构生成模型的典型水平，而且该研究仍是未经同行评审的预印本，消息本身来自聚合类网站而非原始论文。据报道论文还涉及序列重设计任务，在 MDM2 靶点上成功率约为 85%，并将 GPT-6 的优势归结为内生的推理能力加代码执行，而非训练出来的蛋白质专用网络。

aibase · AIbase · 11月25日 11:01

**背景**: 蛋白质设计的目标是发明新的氨基酸序列，使其折叠成特定的三维结构并能与选定的分子靶点结合；微型结合蛋白（minibinder）就是经过设计、体积小且稳定、能紧密结合同一靶点的小型蛋白。过去这类工作主要依靠 RFdiffusion、ProteinMPNN 等专用生成模型与基于结构的工具，它们需要领域专用的训练数据和流程。任何计算方法得到的候选分子都必须先合成、再在实验室中检测，即所谓“湿实验验证”，因为只有实验才能证明设计出的蛋白是否真的能折叠、表达并发生结合。本文报告的核心指标就是：一次纯计算的设计工作中，约 10%的候选出现了结合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT-6 models demonstrate intrinsic protein-design ... - OpenAI</a></li>
<li><a href="https://explainx.ai/blog/openai-gpt-6-intrinsic-protein-design-onava-lab-binding-november-2026">GPT-6 Protein Design: 10.9% Minibinder Hits in Lab Tests ...</a></li>
<li><a href="https://www.dawan.africa/news/openai-says-gpt-6-designed-proteins-that-bound-five-targets-in-lab-tests-with-onava">OpenAI Says GPT-6 Designed Proteins That Bound Five Targets ...</a></li>

</ul>
</details>

**标签**: `#AI biology`, `#protein design`, `#GPT-6`, `#LLM reasoning`, `#wet-lab validation`

---

<a id="item-3"></a>
## [Simon Willison 总结十二个月内大模型的三个拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 7.0/10

在一篇基于其在 AI Engineer Code Summit（2026 年 11 月 10 日至 12 日于旧金山举行）主题演讲的文章中，Simon Willison 提出大模型与编码智能体在过去十二个月里经历了三个重要拐点，第一个拐点是 2025 年 11 月 24 日发布、至今正好一周年的 Claude Opus 4.5。他以该模型让 Claude Code 变得足够可靠、成为日常主力工具为线索，并延伸到后来出现的他称之为“Fable 级模型”的新品类。 Willison 是大模型工具领域最受关注的观察者之一，他的梳理为开发者提供了一条清晰的时间线，说明 AI 编码智能体何时从“需要不断纠正”变成“默认基本正确”，这对判断自身的技术采纳决策和厂商路线图都很有参考价值。文章还揭示了竞争格局变化之快：Anthropic 的 Opus 4.5 与 OpenAI 的 GPT-5.1 系列在同一个月内相继发布，引发了 12 月的集中试用，到 1 月便转化为真实的生产力。 Willison 将“Fable 级模型”定义为：只要给出明确目标并提供必要工具，就能靠“暴力穷举”解决问题——他的例子是 Claude Fable 为了修复 Safari 的一个显示故障，自行搭建了基于 pyobjc-framework-Quartz 的截图机制和一个启用 CORS 的本地日志服务器。他还提到，经过安全限制处理的 Claude Fable 5（源自未发布的 Claude Mythos）仅上线三天就被美国出口管制叫停，直到 7 月 1 日才恢复可用。

rss · Simon Willison · 11月24日 23:02

**背景**: Claude Code 是 Anthropic 的命令行编码智能体，最早于 2025 年 2 月 24 日与 Claude 3.7 Sonnet 一同推出，因此 Opus 4.5 发布时它才诞生约九个月。Claude Opus 4.5 是 Anthropic 当时的旗舰模型，宣称在更低价格下具备业界领先的编码与智能体能力，此后已被更新的 Opus 版本取代。Simon Willison 是数据工具 Datasette 的创造者、Django 的联合创始人，其博客是业界广泛阅读的大模型实操记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-4-5">Introducing Claude Opus 4.5 \ Anthropic</a></li>
<li><a href="https://ai.engineer/code/2026">AI Engineer Code Summit 2026: AI Engineering Conference, Nov...</a></li>
<li><a href="https://www.youtube.com/watch?v=9RKrSF9d2SE">2026 in LLMs — Simon Willison - YouTube</a></li>

</ul>
</details>

**标签**: `#LLM`, `#coding agents`, `#AI engineering`, `#Claude Opus`, `#retrospective`

---

<a id="item-4"></a>
## [PrismML 三值压缩模型 Bonsai 2.5 27B：内存降至九分之一，保留 93.7% 编程能力](https://www.aibase.com/news/32522) ⭐️ 7.0/10

PrismML 发布了 Ternary Bonsai 2.5 27B，这是基于 Qwen3.8 27B 的三值量化版本，权重被限制为 -1、0、+1 三个取值，使内存占用从全精度的约 53.8GB 降至 5.9GB。在 SWE-bench Verified 上，压缩后模型得分为 75.6，而基础模型为 80.6，保留了约 93.7% 的智能体编程能力，同时相比去年 9 月的 Bonsai 2 27B 有所提升。 这一结果表明，激进的三值压缩如今可以用较小的精度代价应用于编程智能体，使 27B 级别的智能体编程模型能在消费级 GPU 和本地工作站上运行，而不必依赖数据中心硬件。如果这些数据在独立复现中得到验证，约 9 倍的内存压缩配合约 94% 的能力保留，将为愈演愈烈的模型效率竞赛树立一个有力基准。 三值权重需配合缩放因子使用，每个存储值映射为 -α、0 或 +α，这才使得相对 16 位精度约 9 倍的压缩成为可能，同时让矩阵乘法保持廉价。代价是在 SWE-bench Verified 上下降 5 分（从 80.6 到 75.6），且该报告未给出其他基准、长上下文表现或吞吐数据，因此压缩在编程任务之外的代价仍待验证。

aibase · AIbase · 11月25日 15:01

**背景**: 三值量化（ternary quantization）把神经网络中的每个权值限制为 -1、0、+1 三个取值之一，通常还配合每层一个缩放因子，因此每个权重所需的比特数远少于 16 位浮点数，矩阵乘法在很大程度上可以退化为加法。SWE-bench Verified 是 SWE-bench 中经人工校验的 500 道题子集，智能体需要解决 Python 仓库中真实的 GitHub issue 并通过项目测试套件，如今已成为评测编程智能体的标准标尺。基础模型 Qwen3.8 27B 是阿里 Qwen3 系列中的中等规模稠密模型，该系列参数覆盖 0.6B 至 235B，包含稠密与 MoE 两种架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2303.01505">Ternary Quantization: A Survey - arXiv.org</a></li>
<li><a href="https://grokipedia.com/page/Ternary_Weights">Ternary Weights — Grokipedia</a></li>
<li><a href="https://www.swebench.com/verified.html">SWE-bench Verified</a></li>

</ul>
</details>

**标签**: `#LLM compression`, `#ternary quantization`, `#coding agents`, `#SWE-bench`, `#model efficiency`

---

<a id="item-5"></a>
## [LibreOffice 母机构 TDF 出台严格 AI 编程规则，规范 AI 辅助代码贡献](https://www.aibase.com/news/32515) ⭐️ 7.0/10

维护 LibreOffice 的文档基金会（The Document Foundation，TDF）出台了规范大语言模型使用的新规则，要求开发者在提交代码时必须披露是否使用了 AI 辅助。其核心红线是双重的：既要公开 AI 使用情况，又必须能够理解并解释自己提交的每一行代码。 LibreOffice 是规模最大、使用最广的开源桌面项目之一，因此其政策很可能成为其他正被大量低质量 AI 生成补丁困扰的开源社区效仿的范本。该规则把责任重新压回到人类贡献者身上，意在维护整个生态的代码可维护性与代码审查能力。 这一规则的关键闸门是“人能否理解”，而非禁止使用 AI 工具：贡献者无法解释清楚的代码实际上会被拒绝，哪怕它能跑通。从目前报道看，公告只阐述了原则与红线，并未说明具体的执行工具、披露模板或处罚措施，因此判断解释是否充分仍依赖代码审查者。

aibase · AIbase · 11月25日 11:01

**背景**: LibreOffice 是一款自由开源的办公套件，由 TDF 治理下的大量志愿者与企业贡献者共同开发。大约从 2022 年起，基于大语言模型的编程助手使得批量生成看似合理的代码变得非常容易，维护者认为这带来了“逻辑黑箱”、难以维护的“代码屎山”以及审查不足的补丁。因此，开源项目开始陆续制定明确的 AI 贡献政策，而 TDF 的这套规则被称为其迄今最严格的一版。

**标签**: `#open source`, `#LibreOffice`, `#AI-assisted programming`, `#code quality`, `#governance`

---

<a id="item-6"></a>
## [黄仁勋回归英伟达，重燃华盛顿对华芯片准入之争](https://www.thenews.com.pk/latest/1425062-jensen-huangs-return-to-nvidia-reignites-washington-fight-over-chinas-chip-access) ⭐️ 6.0/10

报道称，黄仁勋回归执掌英伟达后，重新点燃了华盛顿围绕“美国企业可以向中国出售多少先进 AI 芯片技术”的政策争论。文章将这场再度升温的辩论与黄仁勋对美方出口管制的公开批评联系起来——他曾称这些管制是“失败的”，因为中国企业正在转向本土自研的替代方案。 出口管制的走向直接决定哪些英伟达加速器可以卖到中国这一全球最大的 AI 硬件市场之一，因此政策的任何变化都会牵动数十亿美元营收，并改变中国 AI 实验室可获得的算力规模。由于英伟达芯片实际上已成为大模型训练的事实标准，这一结果的影响还会外溢到美国和中国之外的盟友政府与供应链。 这场争论发生在自 2022 年 10 月以来层层叠加的规则体系之上：英伟达为此多次设计面向中国的降规版本（如 H20），而 H20 自 2025 年 4 月起需要美国许可证，公司因此计提了数十亿美元级别的损失。执行层面更为复杂，监管机构担心受限芯片会经由第三国间接流入中国，而政策也在不断收紧与有条件发放许可之间反复摇摆，并非一条清晰界线。

gdelt · thenews.com.pk · 11月25日 14:15

**背景**: 自 2022 年 10 月起，美国商务部工业与安全局（BIS）开始限制向中国出口先进 GPU 和半导体制造设备，并在 2023 年和 2024 年多次大幅更新规则，下调性能门槛、限制美国人员支持中国先进芯片工厂。GPU 及同类加速器是 AI 训练与推理的核心算力来源，因此控制其供应是华盛顿延缓中国前沿 AI 发展的主要抓手。英伟达的应对是推出刚好卡在门槛之下的对华特供芯片，同时华为、寒武纪等中国企业加速推进国产替代。黄仁勋的观点是，过于严苛的限制主要让美国企业损失市场份额，却无法阻止中国的进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China">United States New Export Controls on Advanced... - Wikipedia</a></li>
<li><a href="https://laweconcenter.org/resources/us-export-controls-on-ai-and-semiconductors/">US Export Controls on AI and Semiconductors - International Center...</a></li>
<li><a href="https://www.qatar-tribune.com/article/177910/business/china-slams-us-bullying-over-new-warnings-on-chips">China slams US ‘bullying’ over new warnings on chips - Read Qatar...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#China chip access`, `#export controls`, `#AI hardware`, `#US policy`

---

<a id="item-7"></a>
## [欧盟据报计划向人工智能投资 500 亿欧元](https://www.diariolibre.com/mundo/europa/2026/11/25/ue-planea-invertir-50000-millones-de-euros-en-inteligencia-artificial/3731128) ⭐️ 6.0/10

据初步新闻报道，欧盟正在筹备一项规模达 500 亿欧元的人工智能投资计划。这一消息表明欧盟打算通过大规模公共资金投入来扩大欧洲本土的人工智能研发能力。 500 亿欧元的规模将使其成为主要经济体中对人工智能最大规模的单笔公共投入之一，可能改变欧洲的研究机构、初创公司和高校获取算力、模型与人才资金的途径。这也表明布鲁塞尔把人工智能能力视为战略优先事项，而不仅仅是监管议题，这将影响所有在欧盟市场销售或部署人工智能的企业。 目前的报道将该数字描述为一项“计划”而非已获批的预算，资金来源、算力基础设施与研究投入之间的分配比例、拨付时间表以及对私人共同投资的条件等细节均未得到确认。因此在欧盟官方文件或立法提案公布之前，这一数字应被视为一个宣示性目标。

gdelt · diariolibre.com · 11月25日 14:15

**背景**: 欧洲拥有雄厚的人工智能研究基础，但在私人人工智能投资规模和本土算力方面一直难以与美国和中国匹敌，这导致许多欧洲人工智能创业者选择迁往海外或到海外融资。欧盟的公共资助项目通常由中央预算、成员国出资以及欧洲投资银行的贷款或担保工具共同组成，这也是为什么如此规模的宣布往往需要数年时间才能转化为实际拨款。与此同时，欧盟还在推进《人工智能法案》这一覆盖面广泛的监管框架，官员们一直主张资金与规则必须同步推进，欧洲才能保持竞争力。

**标签**: `#AI policy`, `#EU funding`, `#artificial intelligence`, `#investment`, `#technology governance`

---

<a id="item-8"></a>
## [蚂蚁集团发布医疗 AI 安全防护模型 LingSante MedGuard](https://www.aibase.com/news/32523) ⭐️ 6.0/10

11 月 25 日，蚂蚁集团发布了 LingSante MedGuard——一个拥有 270 亿参数的医疗 AI 安全模型，用于审查 AI 回答的安全性、合规性与伦理问题，并同步开放了一个医疗风险评测数据集。根据技术报告，该模型将医疗护栏教师模型与六个医疗能力专家模型的监督信号蒸馏整合进统一模型，在公开的 LingSante MedGuardBench 上取得了 87.4%的平均 F1 分数。 通用护栏往往无法识别医疗领域特有的失效模式，例如把 LDH 数值错配到相邻的肌酸激酶结果上、让隐藏错误层层传播，或引用并不适用的临床指南。专用的医疗护栏加上开放的風險评测基准，为医院和 AI 厂商提供了可复用的安全层，而当前临床 AI 部署正随着欧盟 AI 法案和 FDA SaMD 等监管要求而加速推进。 该系统被设计为能力增强型护栏而非普通分类器：它将医疗护栏教师模型与六个能力专家结合，覆盖检验值错配、评分计算错误、指南适用性等医疗特有风险。蚂蚁同时开放了风险评测数据集，但此次公告对许可证、推理成本，以及这个 270 亿参数模型如何与现有临床大模型配合部署等细节披露有限。

aibase · AIbase · 11月25日 15:01

**背景**: AI 护栏是位于用户与大语言模型之间的独立模型或过滤器，在提示词和回答到达用户之前，按照安全性、合规性和政策规则进行检查。医疗场景风险更高，因为错误往往细微且与具体数值相关——把检验值挂到错误的检查项目上、引用过时的指南、或算错临床评分，这些对通用检查器来说看起来都很合理。LingSante MedGuardBench 这类基准以及蚂蚁开放的数据集，目的就是衡量护栏是否真能捕获这些医疗失效模式，而不只是应对泛泛的有害内容或提示注入攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.25509">[2611.25509] LingSante MedGuard Technical Report - arXiv.org</a></li>
<li><a href="https://huggingface.co/papers/2611.25509">Paper page - LingSante MedGuard Technical Report</a></li>
<li><a href="https://arxiv.org/html/2611.25509v3">LingSante MedGuard Technical Report - arXiv.org</a></li>

</ul>
</details>

**标签**: `#Medical AI`, `#AI Safety`, `#Guardrails`, `#Evaluation Dataset`, `#Ant Group`

---