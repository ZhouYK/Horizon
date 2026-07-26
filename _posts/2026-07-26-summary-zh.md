---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 25 条内容中筛选出 5 条重要资讯。

---

1. [vLLM 0.26.0：新增 Inkling 模型族与性能优化](#item-1) ⭐️ 8.0/10
2. [开源权重 AI 的 Kubernetes 时刻](#item-2) ⭐️ 8.0/10
3. [Ruff v0.16.0 默认规则从 59 条扩展至 413 条](#item-3) ⭐️ 8.0/10
4. [高通宣布全线产品自 9 月 1 日起涨价](#item-4) ⭐️ 8.0/10
5. [DeepSeek 因创始人言论泄露暂停超百亿美元融资](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM 0.26.0：新增 Inkling 模型族与性能优化](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 新增了对 Inkling 模型族（Thinking Machines Lab）的完整支持、DeepSeek-V4 的显著性能提升、生成模型的 fp32 lm\_head、灵活注意力后端、KV 卸载增强、Rust 前端的多模态支持，以及多模型迁移至 Transformers 5.13.0。 vLLM 是关键的 LLM 推理基础设施，此版本扩展了对新架构（如 Inkling）的模型支持，并通过性能优化提高了推理效率、降低了部署成本，惠及整个 LLM 服务社区。 Inkling 是一个 Mamba-hybrid MoE 模型，拥有 256 个专家，支持 piecewise CUDA graph、Hopper FA4 相对注意力、MTP=1 推测解码、LoRA 和 NVFP4 量化。DeepSeek-V4 的优化包括专用路由 kernel（提升 2.94%端到端每次输出 token 时间）、fused\_topk\_bias（kernel 加速 1.5-2 倍）以及去除冗余重复/拷贝（提升 1.8%端到端每次输出 token 时间）。注意力后端现在可按 KV-cache 分组选择。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个开源、高性能的 LLM 推理引擎，支持多种模型架构和硬件。Thinking Machines Lab 的 Inkling 模型采用混合 Mamba-MoE 架构，拥有 256 个专家，结合了状态空间模型和混合专家技术。Piecewise CUDA graph 是一种技术，它以 eager 模式运行注意力部分，同时捕获模型其他部分的 CUDA graph，从而减少启动开销。NVFP4 是 NVIDIA ModelOpt 提供的一种 4 位浮点量化格式，可实现内存高效的推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/features/torch_compile_and_piecewise_cuda_graph.html">Torch Compile &amp; Piecewise CUDA Graph — TensorRT LLM</a></li>
<li><a href="https://docs.vllm.ai/projects/vllm-omni/en/latest/user_guide/quantization/modelopt/">ModelOpt - vLLM-Omni</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#open source`, `#deep learning`

---

<a id="item-2"></a>
## [开源权重 AI 的 Kubernetes 时刻](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

文章指出，开源权重 AI 模型正成为 AI 部署的标准平台，类似于 Kubernetes 标准化容器编排的过程。 这一转变可能导致 AI 模型商品化，让初创企业和大型企业能够基于共同的、开放的基石进行构建，减少供应商锁定并促进创新。 作者认为，美国实验室需要以宽松许可证发布前沿级别的开源权重模型，以便初创公司在此基础上发展；而真正开放的模式需要像 Linux 一样公开训练数据并进行协作。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: Kubernetes 是一个开源容器编排系统，已成为行业标准，允许应用在任何云上部署和扩展。开源权重 AI 模型是指其训练参数（权重）公开发布，允许任何人本地运行、微调或在此基础上构建，这与 GPT-4 等闭源模型不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/open-models/">Open models by OpenAI</a></li>
<li><a href="https://onyx.app/self-hosted-llm-leaderboard">Best Self-Hosted LLM Leaderboard 2026 | Open-Weight Model ...</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了禁止中国模型的可行性，指出权重只是数字，难以监管。他们还比较了基于 API 的模型定价波动性与开源权重模型提供的稳定基线，并预见了企业像 Linux 那样合作开发共享开源 AI 模型的未来。

**标签**: `#open-weight-ai`, `#kubernetes`, `#AI-industry`, `#standards`, `#open-source`

---

<a id="item-3"></a>
## [Ruff v0.16.0 默认规则从 59 条扩展至 413 条](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0 于 2026 年 7 月 23 日发布，将其默认规则集从 59 条增加到 413 条，启用了许多以前未启用的检查，可捕获语法错误和运行时错误。 这一变化会突然破坏未锁定 Ruff 开发依赖的项目的 CI，迫使开发者更新代码或锁定版本。扩展的规则集有助于更早捕获严重问题，但需要调整配置。 自 Ruff v0.1.0 以来，总规则数从 708 条增至 968 条。新增默认规则包括 load-before-global-declaration（语法错误）和 yield-in-init（立即运行时错误），通常可通过 \`ruff check --fix --unsafe-fixes\` 自动修复。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的快速 Python 代码检查工具，广泛用于 CI 流水线。未锁定的开发依赖（例如不带版本约束的 \`&quot;ruff&quot;\`）允许自动更新，这可能会引入破坏性变化（如新的默认规则），导致构建不可重现和突然失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/rules/load-before-global-declaration/">load - before - global - declaration (PLE0118) | Ruff</a></li>
<li><a href="https://mergify.com/blog/stop-lying-to-your-dependency-resolver-the-real-rules-for-python-dependency-management">Stop Lying to Your Dependency Resolver: The Real Rules... — Mergify</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ ruff : An extremely fast Python linter and code...</a></li>

</ul>
</details>

**标签**: `#Python`, `#linting`, `#Ruff`, `#CI`, `#software engineering`

---

<a id="item-4"></a>
## [高通宣布全线产品自 9 月 1 日起涨价](https://tw.news.yahoo.com/%E7%8D%A8%E5%AE%B6-%E9%AB%98%E9%80%9A%E6%BC%B2%E5%83%B9%E4%BF%A1%E6%9B%9D%E5%85%89-%E5%85%A8%E7%B7%9A%E7%94%A2%E5%93%819-1%E8%B5%B7%E8%AA%BF%E6%BC%B2-%E7%9B%B4%E8%A8%80-142730846.html) ⭐️ 8.0/10

高通于 2026 年 7 月 24 日向客户发出价格调整通知，宣布自 9 月 1 日起对出货产品全线调涨价格。该公司表示，晶圆制造、封装测试、先进封装与基板材料成本持续上升，加上 AI 与数据中心需求大增，是涨价的主要原因。 由于高通芯片广泛应用于手机、PC、物联网及汽车等领域，此次涨价可能传导至整个电子供应链，导致终端消费品价格上涨或规格缩减。这标志着 AI 需求驱动的半导体制造成本正在发生结构性攀升。 高通未公布统一涨幅或具体产品型号，但表示客户经理将逐一联系客户提供新报价。部分已下单但排在 9 月后出货的订单也可能被重新报价。

telegram · zaihuapd · 7月25日 03:01

**背景**: 先进封装是指将多个半导体裸片集成到一个封装中的技术，无需单纯依赖晶体管微缩即可实现更高性能和集成度。这包括扇出型晶圆级封装和 3D IC 等技术。基板是连接芯片与电路板的关键部件，其材料成本上升反映了 AI 和数据中心应用带来的需求增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_%28semiconductors%29">Advanced packaging (semiconductors)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Integrated_circuit_packaging">Integrated circuit packaging - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Qualcomm`, `#chip shortage`, `#price hike`, `#AI`, `#supply chain`

---

<a id="item-5"></a>
## [DeepSeek 因创始人言论泄露暂停超百亿美元融资](https://www.bloomberg.com/news/articles/2026-07-25/deepseek-said-to-tell-backers-of-funding-pause-after-viral-posts) ⭐️ 8.0/10

DeepSeek 已口头通知部分第二轮意向投资者暂停签署投资协议，部分原因是创始人梁文锋对内部言论外泄感到不满。 此次融资暂停可能重塑中国 AI 行业的竞争格局，因为 DeepSeek 是近期融资 70 亿美元的重要参与者。此次泄密事件凸显了知名 AI 初创公司的治理挑战。 DeepSeek 于 2026 年 6 月完成首轮融资，筹得 70 亿美元，本轮原计划募资至少 1000 亿元人民币（约合 140 亿美元），投前估值不低于 4800 亿元人民币（约合 670 亿美元）。该公司同时正在筹备首次公开募股，最快或于 2026 年内递交申请。

telegram · zaihuapd · 7月26日 01:17

**背景**: DeepSeek 是一家以开发竞争性大语言模型闻名的中国 AI 初创公司。它在 2026 年 6 月的首轮融资中筹集了 70 亿美元，投资方包括腾讯、宁德时代及国家人工智能产业投资基金。此次融资暂停源于创始人梁文锋对内部投资者会议言论外泄的不满，导致团队重新评估信息披露流程和投资者沟通机制。

**标签**: `#DeepSeek`, `#AI startup`, `#funding`, `#China AI`, `#business`

---