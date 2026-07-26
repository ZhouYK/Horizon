---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 26 条内容中筛选出 3 条重要资讯。

---

1. [vLLM v0.26.0 发布：支持 Inkling 模型，优化 DeepSeek-V4 性能，灵活注意力后端](#item-1) ⭐️ 8.0/10
2. [开放权重 AI 迎来类比 Kubernetes 的基础设施时刻](#item-2) ⭐️ 8.0/10
3. [市场监管总局对携程罚没 51.79 亿元](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布：支持 Inkling 模型，优化 DeepSeek-V4 性能，灵活注意力后端](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 新增了对 Inkling 模型系列的全面支持，为 DeepSeek-V4 带来了跨供应商的性能优化，通过 head\_dtype 支持 fp32 lm\_head，并实现了可针对每个 KV 缓存组选择的灵活注意力后端。 作为广泛使用的大语言模型推理服务库，这些改进直接提升了生产环境的推理效率、模型灵活性和硬件利用率，使大规模部署大语言模型的开发者受益。 Inkling 支持包括分段 CUDA 图、Hopper FA4 相对注意力、MTP=1 推测解码、LoRA 和 ModelOpt NVFP4 量化。DeepSeek-V4 的优化包括专用路由内核（端到端 TPOT 提升 2.94%）和 fused\_topk\_bias（内核加速 1.5–2 倍）。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个开源的高吞吐量大语言模型推理引擎，利用 CUDA 图等优化技术减少 GPU 开销。分段 CUDA 图将模型的计算图拆分为多个片段，以更高效地处理变长输入，并绕过不支持的运算（如注意力）。NVFP4 是 NVIDIA Model Optimizer 提供的 4 位量化格式，可在保持精度的同时减少内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.sglang.io/advanced_features/piecewise_cuda_graph.html">Piecewise CUDA Graph - SGLang Documentation</a></li>
<li><a href="https://docs.vllm.ai/en/stable/design/cuda_graphs/">CUDA Graphs - vLLM</a></li>
<li><a href="https://github.com/vllm-project/tml-fa4">GitHub - vllm-project/tml-fa4: FA4-based Relative Attention ...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM serving`, `#GPU optimization`, `#DeepSeek`, `#performance`

---

<a id="item-2"></a>
## [开放权重 AI 迎来类比 Kubernetes 的基础设施时刻](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

一篇文章指出，开放权重 AI 模型正成为标准化的基础设施层，类似于 Kubernetes 对云计算的革命性影响。 这一转变对 AI 监管、定价和协作具有深远影响，可能建立通用基线，减少供应商锁定并促进创新。 该文章评分 8.0/10，引发了 313 个赞和 257 条评论的广泛社区讨论，涉及模型禁令的技术可行性以及推理定价动态。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: Kubernetes 是一个用于自动化部署、扩展容器化应用的开源平台，已被广泛采用为行业标准。开放权重 AI 模型指其训练参数公开释放的模型，任何人都可以运行、审计和定制，与封闭 API 形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/open-models/">Open models by OpenAI</a></li>
<li><a href="https://onyx.app/self-hosted-llm-leaderboard">Best Self-Hosted LLM Leaderboard 2026 | Open-Weight Model Rankings for ...</a></li>

</ul>
</details>

**社区讨论**: 评论强调按来源禁止模型的不可行性，因为权重只是数字；质疑专有 API 定价的波动性；并建议类似 Linux 或 Kubernetes 的共享模型协作才是未来方向。

**标签**: `#open-weight AI`, `#Kubernetes`, `#AI regulation`, `#open-source`, `#infrastructure`

---

<a id="item-3"></a>
## [市场监管总局对携程罚没 51.79 亿元](https://www.xinhuanet.com/fortune/20260725/693124245aa44d2bbc7520b7a0c244ea/c.html) ⭐️ 8.0/10

国家市场监督管理总局对携程滥用市场支配地位行为作出行政处罚，没收违法所得 16.58 亿元，并处罚款 35.21 亿元，合计 51.79 亿元。 这是中国科技公司有史以来最大规模的反垄断罚款之一，标志着对平台经济垄断行为的监管进一步升级，可能重塑中国在线旅游市场的竞争格局。 监管部门还责令携程全额退还强制扣除酒店经营者的订单储备金 1.22 亿元，并要求全面整改并公开整改措施。

telegram · zaihuapd · 7月25日 02:24

**背景**: 携程是中国最大的在线旅行服务公司，在酒店预订和机票代理市场占据主导地位。此次处罚依据《反垄断法》，该法禁止滥用市场支配地位的行为，如要求交易相对人仅与携程交易或收取不合理保证金。

**标签**: `#antitrust`, `#China`, `#regulation`, `#tech`, `#Ctrip`

---