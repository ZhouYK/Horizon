---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06 23:03:40 +0000
lang: zh
report: ai
---

> 从 164 条内容中筛选出 10 条重要资讯。

---

1. [Mistral 发布万亿参数 MoE 模型 Mistral Large 4](#item-1) ⭐️ 8.0/10
2. [加州签署 20 余项 AI 法案，州级 AI 监管大幅扩张](#item-2) ⭐️ 7.0/10
3. [Simon Willison 称赞 EmbeddingGemma 2 的 Apache 2.0 许可可防止厂商锁定](#item-3) ⭐️ 6.0/10
4. [Simon Willison 演示用 Parseable 接收 Datasette 的 OpenTelemetry 追踪数据](#item-4) ⭐️ 6.0/10
5. [Mistral Large 4 与“犰狳基准”的饱和之争](#item-5) ⭐️ 6.0/10
6. [Simon Willison 测试 Claude Opus 5.5 创作冒险游戏配乐](#item-6) ⭐️ 6.0/10
7. [Anthropic 的 Cowork 从本地虚拟机转向云端按会话沙箱](#item-7) ⭐️ 6.0/10
8. [范德堡获 1280 万美元资助，用 AI 推动基因组学走向临床](#item-8) ⭐️ 6.0/10
9. [加州成为首个立法规范律师使用 AI 的州](#item-9) ⭐️ 6.0/10
10. [加州通过人工智能新法，覆盖就业、医疗与生物安全领域](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Mistral 发布万亿参数 MoE 模型 Mistral Large 4](https://simonwillison.net/2026/Oct/6/le-chonk/) ⭐️ 8.0/10

10 月 6 日，Mistral 发布了 Mistral Large 4 的预览版（绰号“le Chonk”），这是一个拥有 1 万亿总参数、490 亿激活参数的混合专家（MoE）模型，训练使用的是 Mistral 自有的约 3800 块 NVIDIA Grace Blackwell GPU 集群。该模型目前可通过 Mistral API 使用，官方承诺将在“本月底”发布开放权重版本。 这标志着 Mistral 重新回到前沿竞争行列：该模型在 Artificial Analysis 上得分 38，相比去年 12 月 Mistral Large 3 的 9 分是巨大飞跃，仅次于 5520 亿参数的 DeepSeek 4.1 Flash。如果承诺的开放权重如期发布，它将为自部署社区提供一个规模最大的公开 MoE 模型之一，也表明欧洲实验室依然有能力在自有硬件上训练前沿级模型。 API 只提供两个推理档位——“none”和“high”；在 Simon Willison 的“骑自行车鹈鹕”测试中，“high”档画出的结果更好，而且输出 token 数反而更少（2,717 对 3,275）。按 Mistral 自己的说法，该模型仍落后前沿大约六个月；另有 Telegram 消息称其用约 4000 块 Grace Blackwell GPU 训练了两个月，在编程等任务上仍落后于前沿模型。

rss · Simon Willison · 10月6日 20:18

**背景**: 混合专家（MoE）模型把参数切分成许多专门的“专家”子网络，每个 token 只激活其中一小部分，因此一个 1 万亿参数的模型可以有远小的激活参数量（这里是 490 亿），单次请求的算力开销远低于同等总参数的稠密模型。训练所用的 NVIDIA Grace Blackwell 平台把 Grace CPU 与 Blackwell GPU 组合成机架级系统（如 GB200 NVL72），专为大规模 AI 训练设计。“开放权重”指的是公开发布训练好的模型参数供任何人下载并在本地运行，但通常不公开训练数据和代码，这与完全开源的软件并不相同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models? - Analytics Vidhya</a></li>
<li><a href="https://www.linkedin.com/pulse/nvidia-grace-blackwell-nvlink72-engineering-1-exaflop-ramachandran-kkple">NVIDIA Grace Blackwell NVLink72: Engineering a 1-Exaflop, 120 kW...</a></li>

</ul>
</details>

**标签**: `#Mistral`, `#LLM`, `#AI`, `#open-weights`, `#model-release`

---

<a id="item-2"></a>
## [加州签署 20 余项 AI 法案，州级 AI 监管大幅扩张](https://news.google.com/rss/articles/CBMitAFBVV95cUxPUW9wanRYNmEycm1EWU5Ma2dUandkUmlndjRTYVZYUTJLNTFQNVptem9sTkthS2NIRE4zWXNMNU8zMVQtNDk4ZlB4QUU0b05lbXVTaHNwSnkwbkxtcG1sODhULXpHYnV5RktoZnZRY3lmZlphaG9yV09nNkg2aW8yZEdPbXU0SzJYQlZPTGd3NXV6MDZzcEJ6bUNzV2RzQWtqUG1KY2VUZkRMRzFMSEFJczNObl8?oc=5) ⭐️ 7.0/10

据 Inside Privacy 报道，加利福尼亚州州长签署了 20 多项与人工智能相关的法案，成为美国州级 AI 监管规模最大的一次集中扩张之一。这一消息属于标题级别的公告，表明这是一揽子立法而非单一法案，涉及 AI 开发与应用的多个领域。 加州聚集了大量头部 AI 实验室和科技公司，因此其法规往往事实上成为全国性标准，其合规实践的影响远超州界。由于美国国会尚未通过全面的联邦 AI 立法，此类州级一揽子法案正越来越直接地决定开发者、部署方和企业必须遵守的规则。 目前所见的报道未提供法案编号、生效日期或具体条款，因此针对模型开发者和部署方的具体义务还需逐项查阅法案原文。读者还应关注新法之间以及与加州现行法规之间如何衔接，因为要求重叠可能导致合规义务冲突或重复。

google\_news · Inside Privacy · 10月6日 18:54

**背景**: 加州一直是美国 AI 政策最活跃的州：2024 年州长签署了十多二十项 AI 相关法案，同时否决了更为激进的 SB 1047；2025 年立法机构又推进了一大批 AI 立法。其他司法辖区也在同步行动，包括科罗拉多州 AI 法案、得克萨斯州 TRAIGA，以及按风险分级对提供者和部署方设定义务的欧盟《人工智能法案》。在缺乏全面联邦 AI 成文法的情况下，各州已成为美国具有约束力的 AI 规则的主要来源。

**标签**: `#AI regulation`, `#policy`, `#California`, `#legislation`, `#AI governance`

---

<a id="item-3"></a>
## [Simon Willison 称赞 EmbeddingGemma 2 的 Apache 2.0 许可可防止厂商锁定](https://simonwillison.net/2026/Oct/6/hn-49983751/) ⭐️ 6.0/10

Simon Willison 在其博客引用的 Hacker News 评论中，特别点名 Google 新发布的 EmbeddingGemma 2，认为嵌入模型不应采用闭源、仅托管的形式，并尤其称赞其 Apache 2.0 许可证。他指出，当专有嵌入模型最终被下线时，用户将被迫付费重新计算数百万条已存储的向量。 对于任何大规模运行语义搜索、RAG 流水线或推荐系统的团队来说，这一点至关重要，因为嵌入向量会被长期存储，并与生成它们的特定模型绑定。这把开放权重定位为应对厂商下线的保险措施，而非意识形态偏好，可能促使更多团队倾向选择 Apache 2.0 等宽松许可的嵌入模型。 EmbeddingGemma 2 是一个基于 Gemma 4 的不到 10 亿参数的小型模型，可将文本（含代码）、图像、视频和音频映射到统一的 768 维向量空间。Willison 强调他本人并不想自行托管：他更愿意付费使用第三方托管服务，同时知道开放权重能在对方停止提供时作为退路。

rss · Simon Willison · 10月6日 20:37

**背景**: 嵌入模型把文本、图像或其他数据转换为稠密的数值向量，使机器能够衡量语义相似度；这些向量通常只生成一次，随后存入向量数据库供日后比对使用。检索增强生成（RAG）与语义搜索都依赖这一机制，而由两个不同模型产生的向量一般无法直接比较，因此更换模型意味着要重新生成整个语料库。这种重新生成的过程被称为“重新嵌入”（re-embedding），在数百万份文档的规模下成本高昂，这也是为什么对嵌入模型而言，许可证与长期可用性比普通的 LLM 聊天场景更为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/">EmbeddingGemma 2: The Developer Guide - Google Developers Blog</a></li>
<li><a href="https://ollama.com/library/embeddinggemma-2">embeddinggemma-2</a></li>
<li><a href="https://www.pinecone.io/learn/vector-embeddings/">What are Vector Embeddings | Pinecone</a></li>

</ul>
</details>

**标签**: `#embeddings`, `#open-source`, `#llm`, `#google`, `#model-licensing`

---

<a id="item-4"></a>
## [Simon Willison 演示用 Parseable 接收 Datasette 的 OpenTelemetry 追踪数据](https://simonwillison.net/2026/Oct/6/datasette-parseable-opentelemetry/) ⭐️ 6.0/10

Simon Willison 发布了一篇 TIL（Today I Learned）笔记，记录了如何在本地运行开源可观测性平台 Parseable，并把 Datasette 1.0a41 产生的 OpenTelemetry 追踪数据发送给它——该版本的 OpenTelemetry 支持由贡献者 Alex Garcia 加入。他用 OpenAI 的 Codex 摸索出配置方法，然后手写整理了这份教程，并附上一张截图：Parseable 的追踪查看界面中显示了一个耗时 40.9 毫秒、包含 247 个 span 的 Datasette 请求。 这篇文章展示了一套可行且门槛很低的方案，能把 Python Web 应用的追踪数据导入自托管的可观测性栈，对于希望获得生产级追踪能力、又不想绑定大型商业厂商的开发者很有价值。它也同时为两个较小的项目释放了积极信号：Datasette 新加入的埋点能力，以及 Parseable 作为“单个二进制文件”的轻量级可观测性平台替代方案的定位。 Parseable 的开源版本采用 AGPL 许可证、用 Rust 编写，以约 180MB 的单个二进制文件分发，另有提供额外功能的企业版和云托管版本。Datasette 的追踪功能于 2026 年 9 月 24 日在 1.0a41 版本中引入；截图中捕获的追踪显示了针对 datasette-local 数据库的嵌套 db.query 与 db.query.execute span，单次查询耗时从约 55 微秒到 6.11 毫秒不等。

rss · Simon Willison · 10月6日 19:07

**背景**: OpenTelemetry（OTel）是云原生计算基金会（CNCF）旗下一个厂商中立的开源可观测性框架，提供用于生成和导出分布式追踪与指标的 API、库、agent 以及 collector。Datasette 是 Simon Willison 开发的开源工具，用于把 SQLite 数据库以 Web 界面和 JSON API 的形式浏览与发布；Parseable 则是较新的统一可观测性平台，可通过 OpenTelemetry、Kafka、eBPF 等 agent 接收日志、指标和追踪数据。所谓“追踪（trace）”就是一次请求在应用中流转全过程的记录，它被拆分成带时间戳的“span”，从而揭示时间究竟消耗在哪些环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/parseablehq/parseable">GitHub - parseablehq/ parseable : Parseable is an open source, unified...</a></li>
<li><a href="https://opentelemetry.io/">OpenTelemetry</a></li>
<li><a href="https://www.parseable.com/">Parseable | Observability infrastructure for fast growing teams</a></li>

</ul>
</details>

**标签**: `#opentelemetry`, `#observability`, `#datasette`, `#parseable`, `#tutorial`

---

<a id="item-5"></a>
## [Mistral Large 4 与“犰狳基准”的饱和之争](https://simonwillison.net/2026/Oct/6/hn-49982139/) ⭐️ 6.0/10

Simon Willison 针对 Hacker News 上关于 Mistral Large 4 发布的讨论串做出了回应：他引用了一条称前沿模型基准测试已经“饱和”的评论，并用字面方式验证这一说法——通过自己的 LLM 命令行工具，以各模型的默认推理水平，将“生成一张穿渔网袜、在火星上乱穿马路的犰狳 SVG”这一提示词分别输入 claude-opus-5.5、gpt-6.1-sol、gemini-3.8-flash 和 mistral/mistral-large-4 四个前沿模型，并用他的 markdown-svg-renderer 工具并排发布了输出结果。 这凸显了 LLM 社区中一个真实且被广泛讨论的问题：当前沿模型在标准基准上的得分趋同、逼近上限时，排行榜所能提供的信息越来越少，从业者因此越来越依赖非正式的、定性的探测手段。同时对比四款相互竞争的前沿模型的 SVG 输出，也为最新发布的模型（包括 Mistral 的 Large 4）在单一任务中如何完成指令遵循、空间构图与代码生成提供了一个截面式观察。 这些对比使用的是各模型默认的推理设置，而非经过调优的配置，结果以渲染后的 SVG 形式通过 Willison 的 markdown-svg-renderer 工具所链接的 gist 分享，因此该评估是定性的、轶事式的，而非打分式的。值得注意的是，文中提到的一些模型标识（如 claude-opus-5.5 和 gpt-6.1-sol）反映的是未来/假设的模型世代，而且这篇帖子本身只是一则简短的博客式记录，并非严谨的基准研究。

rss · Simon Willison · 10月6日 18:20

**背景**: LLM 命令行工具是 Simon Willison 开发的开源 CLI 与 Python 库，可通过统一接口调用众多不同的大语言模型，因此用同一个提示词横跨各家厂商测试变得非常容易。“基准饱和”指的是领先模型在一项成熟测试（如 MMLU、HumanEval 等）上的得分都逼近上限，以致该测试再也无法区分它们，研究者报告称到 2026 年已有相当大比例的基准出现这种情况。作为回应，非正式的“体感测试”提示词已成为模型发布时社区事实上的仪式，其中最著名的就是 Willison 的“生成一张骑自行车的鹈鹕 SVG”，它演变成了一个被广泛追踪的、半开玩笑式的模型指令遵循与绘图构图评测基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm.datasette.io/">LLM : A CLI utility and Python library for interacting with Large...</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-07-23-investigating-ai-model-performance-are-frontier-labs-optimizing-for-the-famous-pelican-benchmark">Are AI Labs Pelicanmaxxing? Investigating LLM Benchmarks | AIToolly</a></li>
<li><a href="https://tokendyno.com/blog/state-of-llm-benchmarks-2026/">The State of LLM Benchmarks : 2026 Mid-Year Report — TokenDyno</a></li>

</ul>
</details>

**社区讨论**: 讨论由 Hacker News 用户 wren6991 的评论引发，他称“这个基准已经饱和了”，并调侃说前沿模型正在用“穿渔网袜、在火星上乱穿马路的犰狳”来测试，而 Willison 以真的运行了这一提示词的方式表示认同。这段互动反映了社区普遍的观感：传统基准已失去区分能力；同时也显示出一次纯定性、单提示词的对比能够承载多大的解读分量。

**标签**: `#Mistral`, `#LLM benchmarks`, `#model comparison`, `#SVG generation`, `#Hacker News`

---

<a id="item-6"></a>
## [Simon Willison 测试 Claude Opus 5.5 创作冒险游戏配乐](https://simonwillison.net/2026/Oct/6/scrimshaw-jukebox/) ⭐️ 6.0/10

Simon Willison 向 Claude Opus 5.5 提出要求：先设计一种简单的文本音乐格式，再构建一个能在浏览器中播放该格式的 artifact，并附带几首示例曲目，风格要对标《猴岛小英雄》。最终产物 Scrimshaw Jukebox 是一个复古像素风的网页播放器，内含六首原创 chiptune 风格曲目（例如 100 bpm 的《Moonlit Harbor》和 66 bpm 的《The Ghost Galleon》），支持可编辑的钢琴卷帘谱面、按声部静音，最多可同时演奏 16 个声部。 这是一个具体案例，说明纯文本的大语言模型能够自行发明一套小型领域专用记谱语言，并借此生成风格统一、听感尚可的音乐，其工作流与“提示词直接生成 artifact”的创意编程如出一辙。Willison 猜测这可能是一种近几个月才出现的新能力，类似文本模型近期获得的 3D 图形生成能力，但他也指出尚未通过与旧模型的严谨对比实验来确认。 六首曲目覆盖多种拍号与速度——4/4、6/8 与 3/4，速度从 66 到 152 bpm 不等——并使用了一套具名音色，包括钢鼓、长笛、马林巴、风琴、弦乐、无品贝斯、定音鼓以及各类打击乐。Willison 坦言模型对“猴岛”主题的投入远超他的预期，并明确提醒：要确认这是否真是一种全新能力，还需要对近期与更早的模型做严谨的对比实验。

rss · Simon Willison · 10月6日 15:17

**背景**: 《猴岛小英雄》（The Secret of Monkey Island）是 1990 年 LucasArts 出品的点击式冒险游戏，以 Michael Land 创作的加勒比风格配乐闻名；正是当时音频系统的局限促成了 iMUSE 这一交互式音乐系统的诞生，它能随玩家在游戏中的行动平滑切换音乐段落。ABC 记谱法、MIDI 文本格式和 tracker 模块等基于文本的音乐格式，让音乐可以像普通字符一样被书写和编辑，而不必依赖渲染后的音频。Claude Artifacts 是 Claude 生成并可在浏览器中直接运行的自包含交互网页，正因如此，“自创记谱格式 + 可播放合成器”才能在一次提示中一并完成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IMUSE">iMUSE - Wikipedia</a></li>
<li><a href="https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them">What are artifacts and how do I use them? | Claude Help Center</a></li>
<li><a href="https://www.lddgo.net/en/common/abc-music-notation">ABC Music Notation Editor Online</a></li>

</ul>
</details>

**标签**: `#llm`, `#ai-music-generation`, `#claude`, `#creative-coding`, `#generative-ai`

---

<a id="item-7"></a>
## [Anthropic 的 Cowork 从本地虚拟机转向云端按会话沙箱](https://simonwillison.net/2026/Oct/5/felix-rieseberg/) ⭐️ 6.0/10

Anthropic 的 Felix Rieseberg 表示，新版 Cowork 把模型推理和虚拟机都放在云端运行，每个会话各自拥有独立的沙箱，且会话之间不共享状态。当云端虚拟机需要用户设备上的东西（例如某个文件）时，由桌面应用负责执行这个文件访问的工具调用。 这一架构调整直接回应了此前本地虚拟机方案最受诟病的问题——占用磁盘、耗电、性能开销大，以及合上笔记本就中断任务——同时还让用户可以从手机端使用该智能体。这也表明，编码类与通用型智能体产品正逐渐把云端沙箱作为默认执行模式，云厂商推出的托管沙箱服务也体现了同样的趋势。 每个云端会话彼此隔离、不共享状态，而此前的本地虚拟机只映射用户显式加入该会话的数据；根据 Anthropic 的帮助文档，虽然云端已成为默认方式，但现有桌面部署仍可选择本地执行。桌面应用被专门保留在文件访问工具调用这一环节中，因此设备本地数据仍由客户端经手，而不是被整体上传。

rss · Simon Willison · 10月5日 23:56

**背景**: Claude Cowork 是 Anthropic 的智能体产品，它可以接管一项任务、在后台推进，并交付演示文稿、文档或表格等成果，还支持定时任务与数据连接。在最初的设计中，模型推理在云端进行，但工具调用是在 Anthropic 下发到用户电脑上的虚拟机里执行的，这样做是出于能力、安全和安保考量，以确保只暴露用户显式添加的数据。这里的“沙箱”指的是一种隔离的执行环境，用于限制智能体所能触及的代码与资源，这很重要，因为智能体会运行自动生成的代码并操作真实文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview">Claude Cowork architecture overview | Claude Help Center</a></li>
<li><a href="https://claude.com/product/cowork">Claude Cowork | Claude by Anthropic</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#sandboxing`, `#cloud architecture`, `#Anthropic`, `#Claude`

---

<a id="item-8"></a>
## [范德堡获 1280 万美元资助，用 AI 推动基因组学走向临床](https://news.google.com/rss/articles/CBMixAFBVV95cUxNR1QtSW15RlBPclVpal92Mko5bEFBMkZfR3FBNUp5Vnh2UE1TUG00SGxLUFVoZGl6M21YbURid2pqbUlaNlFfcDRxRFhTMmZJNnJhTFotckljR2N2Zy1DLXlWLUpZV01xQ1J6cmMxaEtPVGtvbGYxQ3Z1ZUIzMW9aNWZSVGE4UHFoY29YRG5PcHk1ZGU1eTB1NldlYjNRclJXeEpyX1FBTlA0QlhXMS1HRkxoeUgxWHUzMlEtY0c0UGExQ1dE?oc=5) ⭐️ 6.0/10

范德堡健康新闻（Vanderbilt Health News）报道称，范德堡获得一笔 1280 万美元的资助，将牵头开展一项计划，通过机器学习和人工智能推动基因组学更接近常规临床实践。该资助将支持一个多方参与的项目，把基因组数据转化为可在诊疗现场使用的工具。 如今基因测序的成本已相对低廉，但解读测序数据仍依赖人工、耗时且受专家资源限制，这正是基因组学难以进入日常医疗的主要瓶颈。如果机器学习能够可靠地辅助变异筛选与解读，就有可能加快诊断速度、让精准医疗走出少数专科中心，并影响医院与支付方将基因组学纳入常规诊疗的方式。 这只是一则简短的机构新闻稿，因此资助机构、参与合作机构的数量、针对的疾病或数据类型以及项目时间表等细节，在现有内容中均未披露。与大多数临床 AI 项目一样，真正的考验在于能否在多样化患者群体中得到验证并获得监管认可，而不只是模型本身的性能。

google\_news · Vanderbilt Health News · 10月6日 17:44

**背景**: 临床基因组学是指对患者的 DNA 进行测序，然后判断数百万个基因变异中哪些真正与疾病相关——这项工作传统上依赖受过训练的遗传学家和变异注释数据库。许多变异最终被归类为&quot;意义不明确的变异&quot;，从而延误诊断与治疗决策。机器学习正越来越多地被用于这一解读难题，例如预测某个变异是否会破坏蛋白质功能，或将基因组特征与临床结局和药物反应关联起来。

**标签**: `#AI in genomics`, `#machine learning`, `#precision medicine`, `#healthcare AI`, `#research funding`

---

<a id="item-9"></a>
## [加州成为首个立法规范律师使用 AI 的州](https://news.google.com/rss/articles/CBMiggFBVV95cUxNVnBxNmI2WW1GaDBPaHA3Z2hTVW1xYU5XWHRjUUxQNmJ1YkdfX1BzbURqNlFVWk03X0hLNEV0RWVsbTh6MllDTXM4el9EbzQ3d19saVp6Q0J0QmZva09oY0kyRTZ2MW80V2N5amx1WmFLNDgwRGRHTkxoZGhUYmhtaVdn?oc=5) ⭐️ 6.0/10

加州通过了一项被描述为美国首个针对律师如何使用人工智能的州级立法。该消息由 JDSupra 报道，但目前可获取的素材仅为一条标题，没有正文内容。 如果美国某个州以正式立法而非仅靠律师协会的道德意见来规范律师使用 AI，就会形成具有约束力的合规标准，其他州可能效仿，从而影响法律科技厂商的产品设计以及律所采用 AI 工具的方式。由于律师负有胜任义务与保密义务，这类规则会影响所有执业领域，而不仅仅是早期尝鲜者。 所提供素材仅包含一条标题链接，没有文章正文，因此法案编号、生效日期、禁止或要求的用途范围、以及罚则或披露义务等具体内容均无从得知，不应凭空假设。读者需要查阅立法原文或加州律师协会的相关指引，才能了解具有操作性的细节。

google\_news · JDSupra · 10月6日 20:13

**背景**: 美国法律职业道德规则传统上由各州最高法院参照美国律师协会（ABA）示范规则制定，遇到新技术引发的新问题时，州律师协会通常只发布不具约束力的指引。生成式 AI 工具（如大语言模型）已在法院中引发广泛关注的问题，包括律师提交的文书引用了聊天机器人凭空编造的虚假判例，这促使监管机构采取行动。加州律师协会在此次立法之前就已在研究 AI 相关指引与披露要求，因此这项新法属于州层面 AI 治理浪潮的一部分。

**标签**: `#AI regulation`, `#legal tech`, `#AI policy`, `#California`, `#lawyers`

---

<a id="item-10"></a>
## [加州通过人工智能新法，覆盖就业、医疗与生物安全领域](https://news.google.com/rss/articles/CBMizgFBVV95cUxNTl9PeWhxSEctaGRNSC1TVS1MS3lPRFlLM1lGYmhmS1NZZGk4WUFXeUdVOUZlRml6ZHhZVXVfcWFvd0lHS3JqRUZPdzdoQmdqaS0xM1JrTnluQWp0THFUVDFYX0VNX08xbUlZRGhxdVpCcjFxbTFhdWlzbWZwQXltNm9wNEczZi1PaXlqcFlwLXQ1SFdjVzlsazctZEE2Ym1yQUNFX3RvdXlhWDk1U3VWX0owTTE2Zjd5NGNaSFlsU0lvSThvWXNDVVBFd1pCUQ?oc=5) ⭐️ 6.0/10

据 Distilled Post 报道，加利福尼亚州已通过一套新法律，对人工智能在就业、医疗和生物安全领域的应用进行规范。该消息目前仅为标题式通告，未列出具体法案编号、生效日期或执法机构。 加州是美国经济体量最大的州，也是多数主要人工智能开发商的所在地，因此其规则往往成为事实上的全国标准，被企业套用到产品和招聘流程中。在联邦层面正推动优先于州级人工智能立法的背景下，此举进一步加剧了各州监管规则各异的碎片化格局。 由于该报道仅是标题，具体义务、适用门槛、处罚措施和生效日期尚未得到确认；此类加州法律通常于次年 1 月 1 日生效，除非附有紧急条款。这三个领域对应的机制可能各不相同：算法招聘与雇佣决策规则、对人工智能提供或影响医疗建议的限制，以及针对危险模型能力的生物安全筛查。

google\_news · Distilled Post · 10月6日 09:33

**背景**: 加州已成为美国在人工智能政策上最活跃的州：2024 年 9 月，州长加文·纽森否决了覆盖面广的前沿模型安全法案 SB 1047，同时签署了范围较窄的透明度措施。此后，州议会推进了多项针对具体危害而非整体模型开发的法案，包括要求前沿人工智能开发者披露信息，以及限制人工智能聊天机器人提供医疗建议。此处的“生物安全”指的是可能被用于制造生物或化学武器的人工智能系统，以及为防止这种情况而设置的筛查要求；“就业”则指用于招聘、晋升和员工管理中的人工智能，现有反歧视规则虽已适用，但面对不透明的模型难以执行。

**标签**: `#AI regulation`, `#California legislation`, `#employment AI`, `#healthcare AI`, `#biosecurity`

---