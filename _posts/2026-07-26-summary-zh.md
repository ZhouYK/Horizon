---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 27 条内容中筛选出 4 条重要资讯。

---

1. [vLLM v0.26.0 发布，新增 Inkling 模型家族和性能提升](#item-1) ⭐️ 8.0/10
2. [开放权重 AI 迎来 Kubernetes 时刻：成熟与采用挑战](#item-2) ⭐️ 8.0/10
3. [Android 或限制设备端 ADB，引发争议](#item-3) ⭐️ 8.0/10
4. [苹果游说特朗普采用中国存储芯片，遭美光阻挠](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布，新增 Inkling 模型家族和性能提升](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 引入了对 Thinking Machines Lab 新的 Inkling 模型家族（975B 参数 MoE 模型）的支持，以及 DeepSeek-V4 的显著性能优化和灵活的注意力后端。 此版本通过支持 Inkling 等前沿模型并为 DeepSeek-V4 带来显著性能提升，巩固了 vLLM 作为领先开源 LLM 推理引擎的地位，使研究人员和生产用户均受益。 该版本包含来自 212 位贡献者的 411 次提交，具有通过 head\_dtype 实现的 fp32 lm\_head 支持、每 KV 缓存组的注意力后端选择、KV 卸载改进以及支持多模态视频和音频的 Rust 前端。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎。新的 Inkling 模型是一个混合专家（MoE）Transformer，总参数 975B，活跃参数 41B，支持高达 1M token 的上下文窗口，并在 45 万亿 token 上进行了训练。分段 CUDA 图和 FlashAttention 4 相对注意力是优化推理性能的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://docs.sglang.io/docs/advanced_features/piecewise_cuda_graph">Piecewise CUDA Graph - SGLang Documentation</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/cuda_graphs/">CUDA Graphs - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#model support`, `#open-source`

---

<a id="item-2"></a>
## [开放权重 AI 迎来 Kubernetes 时刻：成熟与采用挑战](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

一篇分析文章指出，开放权重 AI 正在成熟，并面临与 Kubernetes 类似的采用挑战，围绕监管、定价和协作开发的辩论日益激烈。文章将 Kubernetes 生态系统与开放权重模型的当前状态进行了类比。 这一视角突显了 AI 开发中潜在的范式转变，开放权重模型可能成为 AI 的标准基础设施，就像 Kubernetes 在云原生应用中的地位一样。这影响到在开放权重领域探索的初创公司、企业和监管机构。 作者建议美国实验室需要以宽松许可证发布前沿级的开放权重模型。社区评论指出按来源禁止模型的挑战以及专有模型定价（代币经济学）的不可预测性。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开放权重 AI 模型的训练参数（权重）可公开下载和使用，但如果训练数据或代码未公开，它们可能并非完全开源。Kubernetes 是一个开源容器编排平台，在经历了最初的碎片化和商业化挑战后，成为了行业标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了按来源禁止模型的可行性（ozgung 认为这在技术上不可行），质疑了专有 AI 定价的波动性（firasd），并建议类似 Linux/Kubernetes 的协作模型开发可以稳定成本（pianopatrick）。一些人还希望像 OpenAI 这样的主要实验室能更频繁地更新模型（drnick1）。

**标签**: `#open-weight AI`, `#Kubernetes`, `#AI regulation`, `#open source`, `#AI economics`

---

<a id="item-3"></a>
## [Android 或限制设备端 ADB，引发争议](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/) ⭐️ 8.0/10

谷歌正在考虑更改 Android，以限制设备端 Android 调试桥（ADB）的访问，要求启用开发者选项和远程 ADB，作为安全改进的一部分。 此举可能严重影响依赖 ADB 进行调试、测试和侧载应用的开发者，可能会降低灵活性并增加 Android 开发工作流程中的摩擦。 该提案专门针对设备端 ADB（例如无线或基于网络的 ADB），而非 USB ADB，并需要通过开发者设置和启用远程 ADB 获得用户同意；一个限制较少的替代方案是限制对特定接口或 IP 地址的访问。

hackernews · shscs911 · 7月25日 06:57 · [社区讨论](https://news.ycombinator.com/item?id=49045159)

**背景**: Android 调试桥（ADB）是一个命令行工具，允许开发者与 Android 设备通信，用于调试、安装应用和运行 shell 命令。它通过 USB 或 TCP 运行，广泛用于开发和定制。拟议的限制旨在关闭潜在的安全漏洞，但批评者认为这破坏了 Android 的开放性，可能将用户推向受限制的生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Android_Debug_Bridge">Android Debug Bridge - Wikipedia</a></li>
<li><a href="https://developer.android.com/tools/adb">Android Debug Bridge (adb) | Android Studio | Android Developers</a></li>
<li><a href="https://www.howtogeek.com/125769/how-to-install-and-use-abd-the-android-debug-bridge-utility/">How to Install and Use ADB, the Android Debug Bridge Utility</a></li>

</ul>
</details>

**社区讨论**: 社区评论大多持批评态度：一些人认为攻击向量最小（需要同时启用开发者选项和远程 ADB），而另一些人则认为这是 Google 锁定 Android 的更广泛趋势的一部分，并将其与 iOS 相比。几位评论者对 Google 的动机表示不信任，暗示未来的限制可能需要身份验证或收费。

**标签**: `#Android`, `#ADB`, `#security`, `#developer experience`, `#Google`

---

<a id="item-4"></a>
## [苹果游说特朗普采用中国存储芯片，遭美光阻挠](https://www.wsj.com/tech/trump-apple-micron-china-chips-784bbd3d) ⭐️ 8.0/10

苹果正游说特朗普政府，允许在美国以外销售的产品中使用中国长鑫存储（CXMT）和长江存储（YMTC）的存储芯片，以降低生产成本。其主要供应商美光科技对此表示反对。 这一冲突凸显了全球科技巨头在成本压力与美国对华贸易限制之间的两难。结果可能重塑半导体供应链，影响苹果的定价、美光的市场份额以及芯片制造的更广泛地缘政治格局。 苹果正寻求获批使用长鑫存储的 DRAM 芯片和长江存储的 NAND 闪存芯片。游说活动包括 CEO 蒂姆·库克及其他高管直接向特朗普总统、商务部长和财政部长推销。据报道，美光正在施加反压力以保护其业务。

telegram · zaihuapd · 7月25日 04:02

**背景**: 长鑫存储是一家成立于 2016 年的中国 DRAM 制造商，总部位于合肥，专注于动态随机存取存储芯片。长江存储是一家中国 NAND 闪存生产商，以其 Xtacking 架构闻名。美光科技是美国主要的存储芯片制造商，也是苹果的关键供应商。美国出口管制目前限制在美国销售的产品中使用某些中国公司的芯片，但对于在其他地区销售的产品规则尚不明确，这为苹果的请求创造了空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/%E9%95%BF%E9%91%AB%E5%AD%98%E5%82%A8">长鑫存储 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.cxmt.com/">长鑫存储</a></li>
<li><a href="http://chip.com.cn/ymtc.html">长 江 存 储 ( YMTC ) - Glochip.com</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#semiconductors`, `#Apple`, `#Micron`, `#trade war`

---