---
layout: default
title: "Horizon Summary: 2026-11-08 (ZH)"
date: 2026-11-08 23:03:12 +0000
lang: zh
report: ai
---

> 从 132 条内容中筛选出 7 条重要资讯。

---

1. [Simon Willison 对比 C 与 Rust 实现的 parse\_number\(\) SQLite 扩展](#item-1) ⭐️ 7.0/10
2. [英伟达调查 CEO 黄仁勋与疑似中国间谍的关系](#item-2) ⭐️ 7.0/10
3. [调查：两家获准购买英伟达 AI 芯片的中企疑与受制裁军工供应商有关](#item-3) ⭐️ 7.0/10
4. [极客玩家用第二代 Optane 内存,仅靠 CPU 跑通 2.8 万亿参数 AI 模型](#item-4) ⭐️ 7.0/10
5. [美国人工智能安全研究所员工改为向白宫汇报，独立性引发担忧](#item-5) ⭐️ 6.0/10
6. [AI 预测数千个与人类疾病相关的线粒体蛋白相互作用](#item-6) ⭐️ 6.0/10
7. [澳洲联储演讲探讨：当“智能”越来越便宜，经济会怎样？](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Simon Willison 对比 C 与 Rust 实现的 parse\_number\(\) SQLite 扩展](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 7.0/10

Simon Willison 分别用 C 和 Rust 实现了同一个 SQLite 可加载扩展：一个 parse\_number\(\) 函数，能把 &quot;-$1,234.56&quot; 或 &quot;12.5%&quot; 这类字符串转换成可求和、可排序的数值，最初的代码和研究报告由 Claude Opus 5.5 生成。Rust 版本体积为 321 KB（使用 Rusqlite）和 298 KB（使用 sqlite-loadable-rs），而 C 版本只有 14 KB；但 Rust 起初更快，因为 Rust 中对应 C 的 strtod 的函数大约快一倍。在提示 Claude 编写自定义 C 数字解析器之后，手写的 C 实现在 200 万行混合数据上每行仅需 19 纳秒，反超了 Rust 的 46 纳秒（Rusqlite）和 41 纳秒（sqlite-loadable-rs）。 这项实验为 SQLite 扩展领域中长期的 C 与 Rust 之争提供了一个具体且可复现的数据点，说明“Rust 更快更安全”的常见假设可能取决于底层库实现，而非语言本身。它还表明，对于用户要加载到嵌入式数据库或打包进容器的扩展来说，产物体积（14 KB 对比约 300 KB）确实可能成为考量因素。 该基准测试覆盖三种工作负载：混合数据、纯整数和纯小数，重写后的 C 解析器在三项上都领先：混合数据 19 纳秒对 46/41 纳秒，纯整数 16 纳秒对 36/32 纳秒，纯小数 18 纳秒对 55/47 纳秒。而最初那个朴素的 C 版本在纯小数场景下其实是全场最慢的，高达 106 纳秒，这正是用专用解析器替换 strtod 成为关键改动的原因。

rss · Simon Willison · 11月8日 22:26

**背景**: SQLite 支持运行时加载扩展：即共享库（Unix 上是 .so，Windows 上是 .dll，macOS 上是 .dylib），它们被动态加载进数据库连接，用来添加自定义 SQL 函数、聚合函数、排序规则或虚拟表，而无需重新编译 SQLite 本身。传统上扩展是用 C 针对 sqlite3\_create\_function\(\) API 和 sqlite3ext.h 分发表编写的；在 Rust 侧，Rusqlite 和 asg017 的 sqlite-loadable-rs 这类封装提供了安全绑定以及便于构建 cdylib 的框架。C 标准库的 strtod\(\) 用于从字符串解析十进制数，而 Rust 标准库中的对应实现已知要快得多，这解释了最初那个出人意料的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite.org/loadext.html">Run-Time Loadable Extensions - SQLite Building and Loading Extensions | clibs/sqlite | DeepWiki Application-Defined SQL Functions - SQLite sql - How to load extensions into SQLite? - Stack Overflow How to compile an extension into sqlite? - Stack Overflow</a></li>
<li><a href="https://github.com/asg017/sqlite-loadable-rs">GitHub - asg017/ sqlite -loadable-rs: A framework for writing fast and...</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#Rust`, `#C`, `#extensions`, `#performance`

---

<a id="item-2"></a>
## [英伟达调查 CEO 黄仁勋与疑似中国间谍的关系](https://news.google.com/rss/articles/CBMilAFBVV95cUxQaHdZZkpucG9aOVF5R2JPeHljWV85XzlhbUxnbUREYWlKQzBiR1UzeWxwaF9EMnpDajI1aXlmMlo0aENzeGdyRzJDSEtJR0xVanhFSkN3bXE0R1FYV2VWZHdIV1A1MmFlczN4VnRZcVZ5QV9xdUlxZXVlZVl3eHRqVWxsVmE1dktHZzdnelB0ZjUwejJj?oc=5) ⭐️ 7.0/10

据《纽约时报》报道，并经 NBC 新闻等媒体跟进，英伟达已启动内部调查，起因是有报道称公司 CEO 黄仁勋遭到中国情报机构针对，并与一名被指为中国间谍的人员存在往来。英伟达尚未公开说明调查范围或涉事人员的具体身份。 这项调查使全球市值最高的芯片公司及其高调 CEO 处于美中国家安全博弈的焦点，考虑到英伟达在 AI 硬件供应链中的关键地位以及受出口管制的直接影响，这一位置格外敏感。若调查久拖不决，可能影响投资者信心、公司在华业务，以及华盛顿对半导体行业与中国实体往来的看法。 目前的报道基于匿名消息源，英伟达和美国官方均未证实相关指控，也未提出任何指控或起诉；报道称公司正在审查该接触的性质，而非公布调查结论。由于最初只是标题式报道，事件时间线、所指情报行动的具体内容以及执法部门是否介入等细节仍未经证实。

google\_news · The New York Times · 11月8日 22:05

**背景**: 英伟达是用于 AI 训练和推理的 GPU 的主要设计厂商，其 CEO 黄仁勋是科技界最知名的人物之一。美中科技竞争使半导体企业高管及其公司成为反情报关注的对象，美国政府多次警告中国试图获取先进芯片技术和相关信息。美国对华出口先进 AI 芯片的管制本已让英伟达与政府的关系格外微妙，因此涉及 CEO 与外国情报人员接触的报道会被企业和监管机构严肃对待。

**标签**: `#Nvidia`, `#Jensen Huang`, `#national security`, `#semiconductors`, `#corporate investigation`

---

<a id="item-3"></a>
## [调查：两家获准购买英伟达 AI 芯片的中企疑与受制裁军工供应商有关](https://news.google.com/rss/articles/CBMi6wJBVV95cUxONjlUN25OeGR5Y3ZBZGFzYU5ZR3ExemVBSENRSzRwcUdDUXlIV3JTZEZUcHpMaGZtaktka3p1WUQxNGU3WTZmV1VuS3R3RUFyWW8xZGRhaTZxQTB5N2F1VnRPS1ljSHJrQl9QeWRzVjhuckZrMTlLQm91YjI5S2ZPb1E1TTl3ZzNGbHFrX091ODBjVWlSNkphb3dmMHZrRDRLRGxmZXlQNEQ2RDJjUVVXQlJjVGVNOW90cVpWZHhhNTB2azJKLXdtRFdjdENrSVB3Sk8xcXRBTUM3V3B2WEcxY2M4clZZRlV2T2ljVlhtY0NNWkVCR0prbGR0NmpCUTRrZGw1Smx4eWhDUEJya3ozR1p4b2Y4bjN6MThQTGNUYjdPY25qUE5ubUNrSjQ1TDhseXpMSjluVEZ2Vkc0NjdWcnBVUGFZQnVxVXpzMlhhbExNOVc2SDFXV0VEeDJ0LTQwOWdBQXBYcHFqMUE?oc=5) ⭐️ 7.0/10

Tom&\#x27;s Hardware 的一项调查报道称，两家获准购买受限制英伟达 AI 芯片的中国公司办公室空置、地址不明，且这些企业与已受制裁的中国军工供应商存在关联。 这一案例凸显美国出口管制可能存在的执行漏洞：先进 AI 加速器的许可证本应用来防止相关产品流入与军方有关的实体，但终端用户核查不力可能导致受控芯片被转移。 报道关注的是实体办公场所和股权关联与合法终端用户身份不符的公司，这引发了对美国工业与安全局（BIS）如何审查许可证申请、是否充分筛查空壳公司迹象的疑问。根据美国规定，英伟达的 A100、A800、H100、H800 和 L40S 等产品对华出口需要许可证。

google\_news · Tom&\#x27;s Hardware · 11月8日 13:00

**背景**: 美国逐步收紧对华先进 AI 芯片出口管制，要求高性能英伟达数据中心 GPU 出口需获得许可证。美国商务部工业与安全局（BIS）维护实体清单（Entity List），限制向被认定构成国家安全风险的外国实体出口，并设有军事最终用户清单（MEU List）等相关名单。管制执行依赖于核查申报买家是否为真实终端用户，而不是受限制方的前台公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/news/us-govt-speeds-up-export-restrictions-for-nvidias-gpus">US Govt Speeds Up Export Restrictions for Nvidia&#x27;s GPUs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Entity_List">Entity List - Wikipedia</a></li>
<li><a href="https://www.morganlewis.com/pubs/2025/01/dods-expanding-list-of-chinese-military-companies">DOD’s Expanding List of Chinese Military Companies</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI chips`, `#export controls`, `#China`, `#sanctions`

---

<a id="item-4"></a>
## [极客玩家用第二代 Optane 内存,仅靠 CPU 跑通 2.8 万亿参数 AI 模型](https://news.google.com/rss/articles/CBMihwNBVV95cUxOVmZreDJxdElUVnFWT3lOV24tNGxvRi1sQkd0ZFdfSkx1OWRZX2VXTUg2MUtOV0N2Z3A3TTFYZ3RTVVZHczdMbUwtOWhzU0RQWWUwaHN1ZkNhLTV4ZTlOcW5HNVg3cUQ5M3F1UVhETDdYdHQ3V2RTMFcxb093OUxSWHJXQUlJUTFkUEUwMU5TSE9sWWZTQUlWNVJkWHBpNVdMNi1FZm51aHpnNDIycENVWmdkZm5xUmlSYXhuMEV5WHJfcVBNMmQ4MTYzX3dNeXRCc1Y3YjBsVmhyanZRSHh4c2FfaWluX3FRLWdjQ3liQ3BmMFhoaWY5T3N3WmMyUnBPWjhvdEZvTFpQRW9UY3ZyY1pEM2MyZ25haVJpWmstYzBuTkNOV3BVb184bXItdHBLd1J3dEh1b2NHX3VUMHR6cmZPSnprYWY3NnhEdmxIUnlQWm1TLTZLUExfX1NseDg0Nm1tZWIzalNWNENQc3dSSDAyTTRuekNNM2RYY2l1aWZVLVRnSWlF?oc=5) ⭐️ 7.0/10

一位 Reddit 上的家庭实验室玩家借助已停产的英特尔第二代 Optane 持久内存 200 系列,搭配一颗 40 核第三代 Xeon Scalable 处理器,完全依靠 CPU\(推理过程不使用 GPU\)跑通了 Moonshot AI 的 2.8 万亿参数 Kimi K3 模型。该玩家提醒说,Optane 模组发热极高,可能把旁边的 DRAM 内存“烧坏”,因此不得不加装鼓风机风扇,防止相邻内存条过热损坏。 这次实验说明,在 DRAM 价格高企的当下,已停产的服务器级 Optane 持久内存可以作为低成本的“大容量存储层”来承载超大模型权重,让爱好者能在本地跑起前沿规模的模型,而不必租用 GPU 集群。它还暴露出一个现实的散热隐患:任何把 Optane 内存条与普通内存混插的玩家都必须提前考虑如何应对。 Optane 持久内存 200 系列采用 DDR4 内存条外形,却具备类似存储的持久化能力和容量,这正是它能以远低于等量 DRAM 的成本承载数 TB 级模型工作集的原因;代价是带宽远低于 DRAM,因此在 CPU 上生成 token 的速度较慢。散热警告值得注意,因为 Optane 模组散发的巨大热量可能让相邻的 DRAM 内存条性能劣化甚至损坏,仅靠机箱常规风道不够,需要额外的主动送风。

google\_news · Tom&\#x27;s Hardware · 11月8日 12:20

**背景**: 英特尔 Optane 持久内存\(常被称作 PMem 或 DCPMM\)是插在 DDR4 插槽上的模组,兼具接近 DRAM 的访问方式和类似固态盘的持久化能力,可让服务器把数 TB 内存当作一个层级来寻址;英特尔已在 2022 年关停 Optane 业务,因此这些模组如今在二手市场上以很低的价格流通。在 CPU 上运行超大模型是可行的,因为大模型推理主要受内存带宽限制,只要机器总容量足够大,即便没有 GPU 也能从较慢的内存中流式读取权重。本次搭建延续了此前的另一项家庭实验室项目:那位玩家用 768 GB Optane 加一块 12 GB 显卡的混合流水线运行了 1 万亿参数的 Kimi K2.5,速度约为每秒 4 个 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/INTC/homelab-builder-runs-28t-parameter-ai-model-on-optane-memory-with-cpu-only-25489775">Homelab Builder Runs 2.8T-Parameter AI Model on Optane Memory ...</a></li>
<li><a href="https://blog.progressiverobot.com/768gb-of-cheap-intel-optane-dimm-memory-sticks-used-to-run-1-trillion-parameter-llm-on-a-system-with-a-single-gpu-local-kimi-k25-install-achieved-roughly-4-tokens-per-second">Running A Trillion Parameter LLM On Intel Optane Memory</a></li>
<li><a href="https://lenovopress.lenovo.com/lp1380-intel-optane-persistent-memory-200-series">Intel Optane Persistent Memory 200 Series Product Guide...</a></li>

</ul>
</details>

**标签**: `#Optane`, `#AI inference`, `#homelab`, `#hardware cooling`, `#LLM systems`

---

<a id="item-5"></a>
## [美国人工智能安全研究所员工改为向白宫汇报，独立性引发担忧](https://news.google.com/rss/articles/CBMizwFBVV95cUxOdmZYc2w5LXZFeVMtNEtZWUR2cURFcUhqbVA4Rk5sNXZBVnlFOWdXZ3RSenBJVG5YLWwtM2hNUWcwaUo0aFVMdTNlLTdxQVRMM1k0RlBwSVJmMk1wbWRyeHdkX19nUGZ2TGhKdTl3eWxBdG10bU1iMHU1dTYxeGpYYk5rZF9JejdRbjllTGdSRW1FNUNnVHhiUzZITGxiRlk4OW95bkN6V0wwYzFWYXZFNWxkU1I2c1RLYzBMVnhlX2ZNaWUzQ3hIRDM4TzBhLXPSAdQBQVVfeXFMTnU1Q19ObTZjMTdYTHZseGk4ek1GMHNsaEs0REFFRE85Y013bzNmVU5PMXVOdk9KMWZZdUNkSlRJZ1VvN1FFdHRJY0llWmMySHJ3WThkYzFBcW1jSXhBSU1OV3cyRFZLYUxEQ09mdHRQNlllSmE3dU5TWjNWU1A2MGh4TC1rRm5lQzRiWlJOQmlNT3ZOaXphdWJ1ZXNLVmxWamNvcFdXODJlb0p3Y1VDbFlzTVdYRGZkY3ZsUHdGUGFWNXdQQnlGOThSVmNTaXhiS1NITFE?oc=5) ⭐️ 6.0/10

据美联社报道，美国人工智能安全中心（即设于美国国家标准与技术研究院 NIST 之下的美国人工智能安全研究所）的员工如今改为直接向白宫汇报，而不再通过商务部/NIST 的常规指挥链运作。报道还指出，该机构目前没有常任负责人，并且已停止发布其研究成果。 这一变化的重要性在于：政府对前沿人工智能模型进行独立且公开记录的评估，是对企业自我评估的重要制衡；批评者认为，由白宫直接监管可能使有关网络安全、生物武器等风险的结论被政治化。这也标志着美国人工智能安全监管治理方式的更大转变，将影响模型实验室、下游部署方以及依赖该研究所评估结果的国际同行。 美国人工智能安全研究所是作为国家支持的评估机构而设立的，专门评估先进的所谓“前沿”人工智能模型，它过去隶属于联邦政府的主要标准机构 NIST，这使其工作带有技术和科学色彩。当前的担忧集中在三点：常任所长的缺位、评估研究发布的中止，以及“企业自行开展的评估无法替代政府对在真实环境中行动的 AI 智能体进行独立测试”这一论点。

google\_news · PBS · 11月8日 18:05

**背景**: 美国人工智能安全研究所（AISI）是美国国家标准与技术研究院（NIST）内部的一个小型联邦机构，任务是理解并缓解先进人工智能模型的风险，英国人工智能安全研究所等机构与之类似。这类研究所通常只负责评估和测试模型，而不具备监管或阻止模型部署的权力，因此其影响力在很大程度上取决于其结论的可信度与公开程度。由于人工智能安全工作涉及模型能力、网络攻击、生物安全等政治敏感议题，研究所在政府架构中的位置会直接影响外界对其结论独立性的判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apnews.com/article/ai-safety-trump-white-house-d3318eb2cf011df53e9ddb3e03d25f13">Who decides what AI safety looks like has been up for grabs ...</a></li>
<li><a href="https://www.wtva.com/2026/11/08/staff-us-center-ai-safety-are-reporting-white-house-raising-independence-concerns/">Staff at the US center for AI safety are reporting to the ...</a></li>
<li><a href="https://www.unite.ai/white-house-request-raises-us-ai-safety-center-independence-concerns/">White House Request Raises US AI Safety Center Independence ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#US policy`, `#AI governance`, `#White House`, `#regulatory independence`

---

<a id="item-6"></a>
## [AI 预测数千个与人类疾病相关的线粒体蛋白相互作用](https://news.google.com/rss/articles/CBMirgFBVV95cUxOaDBKZmdKb3dVSzJNaVBJZGo5MHl3ZHdzMW9qYnBBTUtTWllBMTlQaW43UzZDYVhPZzE1Z09OMExMNzIxWGxLcFFob011aUV4LXNxZ1R6b1VsT3dmNnpxeF9HcFE2dUJZbmFRbUZrR2k2eDJWS29UNkpPLVNPaHI0ejRTNVZ5emV4QnRrM0gtUWY4N3Z0Tm9pNVo2elpfZ1dPbG1XUGVkMEpRM3dQQlE?oc=5) ⭐️ 6.0/10

据 Bioengineer.org 报道，一个基于 AI 的系统预测出了人类线粒体蛋白质组中数千个蛋白质—蛋白质相互作用，其中许多与人类疾病相关。该工作很可能对应一个以结构预测为驱动的相互作用组图谱（据报道名为“MitoMatch”），它基于 AlphaFold Multimer，为功能未知的线粒体蛋白推断潜在的相互作用伙伴和分子功能。 目前仍有相当比例的线粒体蛋白缺乏明确的分子功能注释，因此大规模预测的相互作用组为线粒体疾病（包括神经退行性疾病和代谢性疾病）研究提供了一个系统性的假说生成地图。这也说明 AlphaFold 级别的结构预测正在从单个蛋白走向整个细胞器的网络生物学。 这些结果是计算预测而非实验验证的相互作用，因此在解读时需要关注置信度评分、覆盖范围局限以及假阳性率；该方法依赖 AlphaFold Multimer 式的复合物建模，通常是对亲和纯化质谱等湿实验手段的补充而非替代。所提供的材料中并未包含预测相互作用的确切数量、验证实验以及数据可获取性等细节。

google\_news · Bioengineer.org · 11月8日 18:43

**背景**: 线粒体是细胞内具有双层膜的“能量工厂”，其中含有约上千种不同的蛋白质，它们大多由细胞质输入并组装成大型复合物。蛋白质—蛋白质相互作用决定了这些复合物如何形成与发挥功能，但在蛋白质组尺度上通过实验进行绘制既缓慢又昂贵。AlphaFold Multimer 及相关深度学习工具能够预测两个蛋白是否形成复合物以及如何对接，这使得全基因组范围的相互作用预测首次变得可行——尽管结果仍带有噪声。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41467-026-77112-z">The predicted interactome of the human mitochondrial proteome</a></li>
<li><a href="https://www.nature.com/articles/s41580-018-0092-0">Mitochondrial proteins: from biogenesis to functional ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6684368/">Mitochondrial protein organization: from biogenesis to ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#protein interactions`, `#mitochondria`, `#disease research`, `#computational biology`

---

<a id="item-7"></a>
## [澳洲联储演讲探讨：当“智能”越来越便宜，经济会怎样？](https://news.google.com/rss/articles/CBMiakFVX3lxTE9qWTFiTFlWZm9BRnRKQUZDdThvU0dBU3hjZFY4UV9EQnMyTlpkeXdBSlIwSjMyckZvQ2QwWEhZdGZlSnptWFpZbV9aWGxwY2RKVFh0OXhNV3VkaTdsRjlGMkp4bG0ya0ZMSHc?oc=5) ⭐️ 6.0/10

澳大利亚储备银行（澳洲联储）发布了一篇题为《当“智能”越来越便宜，经济会怎样？》的演讲，探讨人工智能成本不断下降可能如何重塑宏观经济格局。该演讲把 AI 视为一种价格快速下跌的生产投入要素，并追问这对经济增长、生产率、物价和就业意味着什么。 各国央行如今正公开思考：廉价的 AI 究竟会提升生产率、压低通胀，还是会扰乱劳动力市场并影响需求——这些问题直接关系到利率决策。由一家主要央行发表此类演讲，意味着 AI 已被视为头等重要的宏观经济变量，而非小众的技术话题，这将影响政策制定者、投资者和劳动者对未来的判断。 该演讲的框架把“智能”视为一种价格快速下跌的经济投入要素，并将其与电力和计算等早期通用技术的路径相类比，进而追问当关键投入变得极其便宜时，物价、工资和市场结构会发生什么变化。需注意：目前仅能看到标题与链接，演讲的具体论点、数据和政策结论无法在此核实，应查阅原文确认。

google\_news · Reserve Bank of Australia · 11月8日 22:30

**背景**: 澳大利亚储备银行是澳大利亚的中央银行，负责设定现金利率并把通胀维持在 2%–3% 的目标区间内，因此其演讲往往预示政策思路的演变。这一问题背后的经济逻辑很直接：如果生产商品和服务的关键投入变得极其便宜，生产成本就会下降，生产率可能上升，这既能压低通胀，也可能取代某些类型的工作。电力化和计算等早期通用技术正是遵循这一模式——带来了巨大但滞后且分配不均的收益，而这篇演讲似乎正用这一视角来审视 AI。

**标签**: `#AI economics`, `#macroeconomics`, `#productivity`, `#labor markets`, `#central banking`

---