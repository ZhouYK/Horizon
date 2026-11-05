---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05 23:04:23 +0000
lang: zh
report: ai
---

> 从 197 条内容中筛选出 10 条重要资讯。

---

1. [《自然》论文提出 MetaGen-LLM，用语言引导超材料逆向设计](#item-1) ⭐️ 8.0/10
2. [中科大 structRFM RNA 大模型登上 Nature 并全面开源](#item-2) ⭐️ 8.0/10
3. [Marvell 以 1150 亿美元全股票交易收购 Lumentum，加码 AI 光互连](#item-3) ⭐️ 7.0/10
4. [美国民主党人提议立法禁止超级智能研发，违者最高判 20 年监禁](#item-4) ⭐️ 7.0/10
5. [百度开源 2800 亿参数 ERNIE 5.5 Flash Base 模型](#item-5) ⭐️ 7.0/10
6. [美国中期选举把数据中心变成地方公投议题](#item-6) ⭐️ 7.0/10
7. [中期选举获胜后，民主党高层呼吁全国暂停数据中心建设](#item-7) ⭐️ 6.0/10
8. [普林斯顿：AI 回答投票问题表现尚可，但可靠性仍不足](#item-8) ⭐️ 6.0/10
9. [美国司法部据报成立“超级智能”特别工作组](#item-9) ⭐️ 6.0/10
10. [Claude Code 助用户越狱 NordicTrack 跑步机，绕过 iFIT 订阅墙](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [《自然》论文提出 MetaGen-LLM，用语言引导超材料逆向设计](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAtUjh0Z0FUajhsRGJKa0ZKbFpMX1h5Z3U2YVZQLUszU2tMMXJ6RVJiVUEyY1ZsZ2o3dGRrclRybVpCRWhvc19KTW16NjNZTHl6UWNleDk0NU1zanpwWE5V?oc=5) ⭐️ 8.0/10

一篇发表于《自然》的论文提出了 MetaGen-LLM（Metamaterial generation with large language model），这是一个以自然语言为引导的生成式框架，能够在八种不同的结构类别中完成高保真超材料的逆向设计。与以往依赖数值目标、且局限于单一结构族的做法不同，该方法接受自然语言描述作为设计输入，并可跨多个超材料类别进行探索。 让逆向设计可以通过语言来驱动，降低了非机器学习专业的研究人员和工程师的使用门槛，而跨结构族的搜索则把设计空间拓展到单一类别模型无法触及的范围。这也是一个明确信号：大语言模型正逐渐成为 AI 驱动材料科学的交互接口，而不仅仅是文本工具。 该框架覆盖八种超材料结构类别，这也是“multiclass（多类别）”一词的由来；论文的表述显示，其解决的核心技术难点是跨结构族的探索，而非单一类别下的精度本身。关于数据集规模、性能目标以及实验验证的具体细节只能在全文当中看到，因此性能结论应以原文为准，而不是仅凭标题判断。

google\_news · Nature · 11月5日 08:10

**背景**: 超材料是一类人工设计的结构，其宏观性能——力学、声学或光学——来自几何构型而非化学成分。传统设计是“正向”的：先提出结构，再仿真其行为。逆向设计则反过来，从期望性能出发，搜索能产生该性能的结构，这是一个高度非线性的难题，近年来 VAE、扩散模型等生成式方法在此展现出潜力。现有大多数工作要求以数值目标向量作为输入，并且一次只在一个结构族上训练，因此使用者必须先知道该在哪一类结构中搜索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s44455-026-00044-7">Language-guided inverse design of multiclass metamaterials ...</a></li>
<li><a href="https://www.nature.com/articles/s42256-023-00762-x">Inverse design of nonlinear mechanical metamaterials via video ... - Nature</a></li>
<li><a href="https://dl.acm.org/doi/full/10.1145/3774746.3779240">MMetaMix: A Multiclass Metamaterial Mixed Encoding for ...</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#metamaterials`, `#inverse design`, `#language-guided design`, `#materials science`

---

<a id="item-2"></a>
## [中科大 structRFM RNA 大模型登上 Nature 并全面开源](https://www.aibase.com/news/32107) ⭐️ 8.0/10

中国科学技术大学（中科大）的研究团队开发了结构引导的 RNA 基础模型 structRFM，相关成果发表在《Nature》上。团队还通过 GitHub 仓库 heqin-zhu/structRFM 免费公开了配套的配对数据、模型权重和源代码，供全球研究者使用。 相比 DNA 和蛋白质领域，RNA 基础模型的成熟度明显落后，因此一个登上《Nature》且数据、权重、代码全部开放的模型，为 RNA 生物学和药物研发提供了一个可复用的基座，而不是又一个封闭的一次性系统。全面开源也让算力有限的实验室能够直接微调和评测该模型，而不必从零重建预训练流程。 根据项目 GitHub 页面的说明，structRFM 是一个结构引导的模型，通过专门的预训练策略融合序列与结构知识，面向结构推断和功能推断两类任务。不过此次公布的内容并未披露参数量、预训练语料规模或基准测试成绩，因此相较 RNA-FM 等现有 RNA 模型的具体提升仍有待独立评测验证。

aibase · AIbase · 11月5日 11:01

**背景**: 生物领域的基础模型通常先在大规模无标注序列数据上用自监督目标进行预训练，再迁移到下游任务。RNA 的字母表只有四种碱基（A/U/C/G），且实验解析出的结构数据稀缺，模型往往只能从序列本身或从含噪的预测结构中学习。结构引导模型试图在预训练阶段注入结构信号，使学到的嵌入表示能更好地迁移到二级结构预测、三维建模和功能注释等任务上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/heqin-zhu/structRFM">GitHub - heqin-zhu/ structRFM : structRFM : A fully open...</a></li>
<li><a href="https://arxiv.org/html/2204.00300">Interpretable RNA Foundation Model from Unannotated Data for...</a></li>
<li><a href="https://github.com/YuanLi-X/Awesome-RNA-Foundation-Models">GitHub - YuanLi-X/Awesome- RNA - Foundation - Models · GitHub</a></li>

</ul>
</details>

**标签**: `#RNA foundation model`, `#AI for science`, `#open-source`, `#bioinformatics`, `#Nature`

---

<a id="item-3"></a>
## [Marvell 以 1150 亿美元全股票交易收购 Lumentum，加码 AI 光互连](https://news.google.com/rss/articles/CBMimwFBVV95cUxOV0pKeUszR0lQek0yWllGajNWeWZXYWJ1TC0tWS10OTZJdDRBZzhSVGt0MHRuMWhLNVdTUndZd3pRSURIQ0FSaTdDaWFMdVBTQVAxTi1lc25sS2VDQlBVenlmUXA4Z001WXRBaTJ5R3NnSXhsOEhXcGhLVExpeks2bUNvR3FOUGNWb1FtM0J5UHJxNnBwaDRISUhHYw?oc=5) ⭐️ 7.0/10

据双方联合公告以及 CNBC、Yahoo Finance 的报道，Marvell Technology（纳斯达克代码：MRVL）已同意以全股票方式收购光器件厂商 Lumentum（纳斯达克代码：LITE），隐含企业价值约 1150 亿美元。交易完成后，Lumentum 的激光器、光模块组件和光子学子系统业务将被并入 Marvell 的数据基础设施产品线。 这笔交易将打造规模最大的 AI 连接端到端供应商之一：Marvell 的定制芯片、DSP 与网络芯片将与 Lumentum 的光器件相结合，而此时超大规模云厂商正竞相在 AI 数据中心内部用光互连替代铜缆连接。它也预示着光互连供应链将出现一波整合潮，并可能改变 AI 集群获取高带宽链路的方式。 该交易采用全股票结构，公布的隐含企业价值约为 1150 亿美元；Marvell 在新闻稿中说明，其中包含的初步财务数据为未经审计的管理层估计值，仍需经过季末结账程序。与任何同等规模的交易一样，最终完成还需股东表决和监管批准，因此交易条款与时间表仍可能发生变化。

google\_news · Manufacturing Dive · 11月5日 16:21

**背景**: Lumentum 是一家光子学公司，其光器件与子系统被广泛用于电信、企业和数据中心网络，其激光器还支撑下一代 3D 传感等应用。在 AI 数据中心中，光互连越来越多地用于在 GPU 与交换机之间传输高带宽流量，因为相比铜缆电连接，光链路能在更长距离上以更低功耗传输更多数据，而硅光技术是构建这类链路的主流方案。Marvell 为云厂商和运营商客户设计定制芯片、网络芯片和光 DSP，因此收购 Lumentum 可将其连接路线图向上游关键光器件供应延伸，实现垂直整合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity">Marvell and Lumentum to Combine, Creating a Category Leader ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/02/marvell-lumentum-ai-deal.html">Marvell to buy Lumentum in all-stock deal - CNBC</a></li>
<li><a href="https://aiinframap.com/companies/lumentum">Lumentum AI Infrastructure Profile | AI Infrastructure Map</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#M&amp;A`, `#Marvell`, `#Lumentum`, `#photonics`

---

<a id="item-4"></a>
## [美国民主党人提议立法禁止超级智能研发，违者最高判 20 年监禁](https://www.aibase.com/news/32122) ⭐️ 7.0/10

美国民主党议员提出了一项名为《禁止人工超级智能法案》的草案，拟全面禁止对人工超级智能（ASI）的研究、开发与部署。草案规定的处罚极为严厉：涉事公司将被强制解散，违规个人最高可被判处 20 年联邦监禁，其量刑标准明确参照非法开发核武器的处罚。 该提案是迄今为止针对前沿 AI 风险最严格的立法思路之一，可能影响围绕先进 AI 能力究竟应被监管还是彻底禁止的广泛讨论。尽管它仍只是远未落地的草案，但表明立法者已开始把超级智能视为国家级安全威胁，这可能影响美国乃至全球未来的 AI 治理走向。 该法案将直接禁止 ASI 的研究、开发与部署，而不是采用许可或审计式的监管；与核武器法的类比表明，其意图是对故意违规行为追究刑事责任，而不仅是施加民事罚款。作为草案，它仍需经过漫长的委员会审议与表决程序，因此目前不具备任何法律效力。

aibase · AIbase · 11月5日 18:01

**背景**: 人工超级智能（ASI）是一种假想中的 AI 系统，其智能范围远超最杰出的人类头脑，这一概念由哲学家尼克·博斯特罗姆（Nick Bostrom）推广开来。由于 ASI 尚不存在，AI 安全研究者主要致力于理解和降低能力不断增强的系统可能带来的风险，也有批评者认为激烈的竞争压力正迫使实验室以快于安全研究进展的速度推进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence">Superintelligence - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/artificial-superintelligence">What Is Artificial Superintelligence ? | IBM</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#AI regulation`, `#superintelligence`, `#AI safety`, `#legislation`

---

<a id="item-5"></a>
## [百度开源 2800 亿参数 ERNIE 5.5 Flash Base 模型](https://www.aibase.com/news/32118) ⭐️ 7.0/10

11 月 5 日，百度开源了 ERNIE 5.5 Flash Base，这是一个总参数 2800 亿、每 token 激活 140 亿参数的混合专家（MoE）模型，预训练使用了 33.5 万亿 token。百度声称该模型在知识、推理、数学、编程、多语言和长上下文基准上，在同尺寸模型中达到新的最先进水平（SOTA），超过 DeepSeek-V4-Flash-Base 和 Hy3-preview-Base 等模型。 此次发布以一个中国团队开发的大型 MoE 模型扩展了开放权重模型的边界，在较高总参数容量与较低的每 token 激活计算量之间取得平衡。它可能为企业与开发者提供又一个高效的基础模型用于微调，但其影响仍取决于百度自报基准成绩能否得到独立验证。 这是一个基础模型，而非指令微调或对话模型，百度的 SOTA 声明属于自报，尚无详细的独立基准结果。该模型采用混合注意力 MoE 设计，预训练上下文为 128K，微调和推理可支持最多 100 万 token，同时其 Hugging Face 页面显示 2860 亿参数，与公告中的 2800 亿略有差异。

aibase · AIbase · 11月5日 16:01

**背景**: 混合专家（MoE）模型包含许多称为“专家”的参数模块，但每个 token 只经过其中一部分，因此总参数体现模型容量，而激活参数在很大程度上决定每 token 的计算成本。2800 亿总参数、1400 亿激活参数的配置旨在以更可控的推理效率提供大模型能力。基础模型是在原始文本上预训练用于预测下一个 token 的模型，尚未针对对话或指令遵循进行对齐，因此用户通常需要进一步微调。100 万 token 上下文能力指模型一次可处理的文本量，这对长文档有用，但也会增加内存与成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/baidu/ERNIE-5.5-Flash-Base">baidu/ERNIE-5.5-Flash-Base · Hugging Face</a></li>
<li><a href="https://ernie.baidu.com/release/ernie-5-5-flash-base/">ERNIE 5.5 Flash Base · ERNIE - ernie.baidu.com</a></li>
<li><a href="https://www.techcityauthority.com/2026/11/ernie-5-5-flash-base-open-source.html">Baidu open-sources ERNIE 5.5 Flash Base, a 280B model with ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Baidu`, `#ERNIE`, `#open-source`, `#MoE`

---

<a id="item-6"></a>
## [美国中期选举把数据中心变成地方公投议题](https://www.aibase.com/news/32106) ⭐️ 7.0/10

在 2026 年美国中期选举前夕，数据中心已成为地方政治的核心议题：报道援引的 NBC 民调显示，76%的选民反对在自己所在社区建设数据中心，全美 45 项相关地方议案中有 33 项倾向限制。具体行动已经落地——缅因州韦尔斯市对大型项目实施 180 天暂停，俄亥俄州多个城市禁止用电量超过 25 兆瓦的项目，堪萨斯州等地也出现了抵制。 地方规划委员会和市议会正在成为 AI 算力扩张的实际否决点，AI 基础设施的瓶颈正从芯片和资本转向许可证与社区同意。如果这一限制趋势延续到中期选举之后，可能拖慢数据中心的部署进度，并推高依赖高集中度、高耗电园区的超大规模云厂商和 AI 实验室的成本。 俄亥俄州城市采用的 25 兆瓦门槛值得注意：十年前 30 兆瓦的设施已算大型，而如今面向 AI 负载的 200 兆瓦园区已是常态，因此这类上限实际上把几乎所有 AI 规模的项目排除在外。该报道仅为单篇新闻摘要，未披露民调的样本量、调查方法或各项地方议案的具体范围，因此这一趋势能否持续仍不确定。

aibase · AIbase · 11月5日 11:01

**背景**: AI 训练与推理的平均功率密度异常之高，因此现代化的 AI 就绪数据中心耗电量远超传统服务器机房，供电能力与散热已成为与 GPU 供应同等关键的制约因素。由于美国的选址决策主要由市和县一级做出，即使没有联邦法规适用，居民也可以通过分区投票、暂停令和公用事业协议阻止项目落地。兆瓦是衡量数据中心规模的标准简写，表示设施可获取的电力容量，这也是地方条例常以功率阈值形式撰写的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-a-data-center">What is a data center ? | McKinsey</a></li>
<li><a href="https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers">The cost of compute power: A $7 trillion race | McKinsey</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#regulation`, `#local politics`, `#compute`

---

<a id="item-7"></a>
## [中期选举获胜后，民主党高层呼吁全国暂停数据中心建设](https://news.google.com/rss/articles/CBMihwFBVV95cUxONG85QmJuZGVEWUIxSW4ybHJPVmN2RmR2VjBTdnkydmZSOGV6YllsWEUtbVpYclRTSWhQS09EZGxJSllyY0otS1QtQVdVY3BhY0ZqMWxfR25WeWo3Q3d5LUg5dVZrUGRneGh2LTRBQjY3SERxNTdLaXNkaU9VaHVPb0lKQW10WmvSAYwBQVVfeXFMTWdsc2pjdEpUS1NXdWRzcld3SFp2eVBhWkU2NWNOTXRsUS1WbTNRVlg3S0ZRalhiYnR5WTNKQUxiR1JXNkI3b3ItbnBsZkdoZE9lbWJkVFB1eTFwMFluVFNobUtfLU1sTUJPSlRVSU1IUnRhYXFPVzNEc0NRempsZGM3MTFTVFZSUGUzS0Y?oc=5) ⭐️ 6.0/10

据 CNBC 报道，在中期选举取得进展后，民主党高层人物呼吁遏制人工智能基础设施建设，并喊出“立即全国暂停数据中心”的口号。这一动向标志着相关讨论从此前局限于地方选址问题，升级为全国层面的政策诉求。 全国性暂停将直接冲击人工智能发展的物理基础——超大规模数据中心，并可能拖慢美国云计算与人工智能厂商的产能扩张。这也把人工智能基础设施变成了明确的选举议题，提醒电力公司、电网运营商和开发商的审批与供电接入可能面临政治争议。 目前该报道仅有一个标题，尚无公开的立法文本，因此无法确认这项提议是具有约束力的暂停令、审批冻结，还是谈判姿态。其表述聚焦于人工智能相关的建设，而非所有数据中心，关键未知项包括覆盖范围、持续时间，以及是否会附加电网或能效方面的条件。

google\_news · CNBC · 11月5日 20:16

**背景**: 数据中心是容纳服务器、支撑云服务与人工智能模型的物理设施，而人工智能训练集群的耗电量远高于传统负载，超大规模设施通常需要申请 300 兆瓦至 1 吉瓦的电网容量，并面临长达数年的接入周期。电力需求的激增使地方电网承压，也让选址之争日益政治化，催生出“数据中心暂停”运动，类似呼声此前已在英国等国家出现。民意调查也显示，相当一部分公众支持全国性暂停，这正是该主张在政界获得关注的原因之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://heatmap.news/plus/the-fight/spotlight/data-center-moratorium-poll?campaign_id=9&amp;emc=edit_nn_20260806&amp;instance_id=179921&amp;nl=the-morning&amp;regi_id=57935594&amp;segment_id=224274&amp;user_id=49827aaaf19c03a56050421d0ee26f8a">Most Americans Want a National Data Center Moratorium</a></li>
<li><a href="https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/06/ai-data-center-power-demand-grid-constraints-energy-resilience">AI Power Demand: Data Center Growth Strains Global Grids</a></li>
<li><a href="https://www.energy.gov/sites/default/files/2024-08/Powering+AI+and+Data+Center+Infrastructure+Recommendations+July+2024.pdf">Recommendations on Powering Artificial Intelligence and Data ...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#regulation`, `#data centers`, `#politics`, `#AI infrastructure`

---

<a id="item-8"></a>
## [普林斯顿：AI 回答投票问题表现尚可，但可靠性仍不足](https://news.google.com/rss/articles/CBMirAFBVV95cUxPRExCUjRZVFppb1Y2NDRyWDhGcmszelpaV2NsUmxLT2dLQ3dRNVkza0RERWhQbmtfTzdLUUsyeHV4emxaSnZ5UVpDSmVHRm9IaFdfY1NoQmIxc05ucTU3QWVtc3NON3JaeXBMYzJyOHhTajZSM0pGLUMzOTZ3VU5QY003Um0taHg2RnB0S1JTNTItaXVWby1abDBJalFrYWpEeGs0M1p0RHFyeGgz?oc=5) ⭐️ 6.0/10

普林斯顿大学公共与国际事务学院的一篇文章指出，当前的人工智能模型在回答投票相关问题方面表现尚可，但其答案仍不足以可靠地用于高风险的选举信息场景。 由于选民经常通过聊天机器人查询实用的选举信息，即使不大的错误率也可能误导人们了解登记截止日期、投票地点或选票规则；这一发现凸显出 AI 公民工具需要人工监督和权威信息来源。 目前提供的条目只有标题和来源链接，因此文章的具体评测基准、模型列表、问题集和错误率均无法获得；读者应将该标题视为概括性说法，而非详细的评测结果。

google\_news · Princeton School of Public and International Affairs · 11月5日 15:06

**背景**: 大语言模型通过预测文本生成流畅答案，但可能产生幻觉或依赖过时信息；要评估其公民用途，需要用权威选举规则进行测试，并衡量事实准确性、拒绝回答行为和来源依据。与此同时，研究人员已表明大语言模型能够大规模生成有说服力的选举虚假信息，这提高了可靠性与滥用风险的重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.evidentlyai.com/llm-guide/llm-evaluation">LLM evaluation : a beginner&#x27;s guide</a></li>
<li><a href="https://www.turing.ac.uk/news/publications/large-language-models-can-consistently-generate-high-quality-content-election">Large language models can consistently generate high-quality ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#elections`, `#LLM evaluation`, `#civic tech`, `#misinformation`

---

<a id="item-9"></a>
## [美国司法部据报成立“超级智能”特别工作组](https://news.google.com/rss/articles/CBMisgFBVV95cUxPSkpVWFNFb0pHTnJDamdUdFdXVGdnUEpqdGgwNS1vZ1pqaC1FaVpPb1ltNHl0S0VKcW5qZ2lZVUlkZlYwT1pXUG5VZUxfaGhKalh2YjBKd1VxakZBTVAwZG9CWmQ5ejktLUxpRHFQRzMycnFfRmxieDU3Q3lSN2RpdGRaOUFhLVRqUzJPeU5BTUxhaEdIaTF2S3k1R0xHU3g1aElEMVhTYlpwZXlSTE9YUGRB0gFaQVVfeXFMTk1zbW00VU14NXlZQWt2cW9mRHB2WVlPQmsxRzNxQVRJMXdvUXNtVWN3Y3IzVmQybmdURXpqX0RSeE5DVjhlNnVJSXh1YVdmY3FwM2ZXQ3BFR1pn?oc=5) ⭐️ 6.0/10

据 MLex 报道，美国司法部已成立一个“超级智能特别工作组”（Super Intelligence Task Force），成为最新一个围绕先进人工智能风险组建专门机构的联邦部门。该报道仅停留在标题层面，未说明工作组的成员构成、职权范围或时间表，目前也尚无法确认司法部是否发布了正式公告。 如果消息得到证实，此举表明美国执法与国家安全机构正在为可能超越人类监管能力的前沿人工智能模型做准备，这可能会改变 AI 开发者接受审计、被传唤或被追责的方式。同时，这也让白宫、商务部门与国家安全机构之外又多了一个联邦主体，使本已拥挤的 AI 治理格局出现职权重叠的问题。 目前细节极为有限：报道没有说明该工作组究竟是一个起诉办案单位、政策审议机构，还是风险评估小组。关于另一个白宫“超级智能”工作组的报道提到，该工作组将在 120 天内评估 AI 的风险与机遇，并要求开发者报告模型的异常行为，这暗示司法部的这一举措可能与更广泛的白宫计划相关联。

google\_news · MLex · 11月5日 17:12

**背景**: 超级智能（superintelligence）是一种假设性的人工智能系统，其在几乎所有认知任务上都将超越人类；它既没有正式的技术定义，目前也并不存在。围绕这类系统的担忧已经从学术讨论进入政府政策层面：特朗普政府设立了由国家情报总监牵头的超级智能特别工作组，负责评估风险、厘清联邦政府职责，并维护美国的领先地位。若司法部也成立工作组，则意味着这一努力将延伸至司法领域，涉及 AI 系统的责任认定、犯罪滥用以及企业问责等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nbcnews.com/politics/trump-administration/trump-announces-members-ai-task-force-rcna601494">Trump announces members of ‘ Super Intelligence Force ’ to...</a></li>
<li><a href="https://www.kucoin.com/news/flash/white-house-establishes-super-intelligence-task-force-to-assess-ai-risks-and-opportunities-in-120-days">The White House Establishes a Superintelligence Task Force to...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence">Superintelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#regulation`, `#DOJ`, `#superintelligence`, `#policy`

---

<a id="item-10"></a>
## [Claude Code 助用户越狱 NordicTrack 跑步机，绕过 iFIT 订阅墙](https://www.aibase.com/news/32125) ⭐️ 6.0/10

一名 Reddit 用户借助 Anthropic 的 Claude Code 越狱了 NordicTrack Commercial 2250 跑步机，解除其 10 英寸控制台上 iFIT 的订阅锁定，把原本封闭的屏幕改造成可自由安装流媒体应用的开放界面。这个项目是为他女朋友的跑步机做的，据报道前后大约花了一天半时间完成。 这一案例表明 AI 编程助手正在降低消费级硬件改造的门槛，让非专业人士也能绕过自己已购设备上的订阅锁。它直接呼应了“维修权”与物联网设备归属权的争论——昂贵的健身器材上被锁死的固件和付费墙功能，正引发越来越多的不满。 据称该改造保留了跑步机的速度、坡度等核心控制功能，同时加入了 Netflix、Crunchyroll 等应用以及自定义训练界面，机器仍能正常作为健身器材使用。不过由于信息来自 Reddit 上的个人分享而非完整可复现的教程，技术细节较为有限，而且此类改动可能导致保修失效，或在 iFIT 后续固件更新后失效。

aibase · AIbase · 11月5日 19:01

**背景**: NordicTrack 跑步机运行 iFIT 专有平台，将训练内容和流媒体应用打包在付费订阅之后，控制台实际上被锁死在该服务上。Claude Code 是 Anthropic 推出的智能体式编程工具，在终端中运行，能够自主完成多步骤工程任务。此前的社区项目 NordicUnchained 等已经探索过重新获取 NordicTrack 控制台的高级权限，但通常需要相当的技术功底。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androidauthority.com/claude-nordictrack-treadmill-ifit-subscription-3731515/">Claude helps NordicTrack owner unlock treadmill streaming apps</a></li>
<li><a href="https://theidea.works/blog/jailbreak-nordictrack-treadmill/">Jailbreaking Your NordicTrack Treadmill: Free It From the ...</a></li>
<li><a href="https://geekyschmidt.com/post/2026-07-28-nordictrack2026/">Reclaiming Your Nordic Track : A 2026 iFit Bypass... | Geeky Schmidt</a></li>

</ul>
</details>

**标签**: `#AI coding assistants`, `#right-to-repair`, `#consumer IoT`, `#jailbreaking`, `#subscription models`

---