---
layout: default
title: "Horizon Summary: 2026-07-26 (EN)"
date: 2026-07-26
lang: en
---

> From 25 items, 5 important content pieces were selected

---

1. [vLLM 0.26.0: New Inkling Model Family, Performance Boosts](#item-1) ⭐️ 8.0/10
2. [Open-weight AI is having its Kubernetes moment](#item-2) ⭐️ 8.0/10
3. [Ruff v0.16.0 expands default rules from 59 to 413](#item-3) ⭐️ 8.0/10
4. [Qualcomm Announces Across-the-Board Price Hike from Sept 1](#item-4) ⭐️ 8.0/10
5. [DeepSeek pauses $10B+ funding after founder&\#x27;s leak](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM 0.26.0: New Inkling Model Family, Performance Boosts](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 introduces full support for the Inkling model family \(Thinking Machines Lab\), significant performance improvements for DeepSeek-V4, fp32 lm\_head for generation models, flexible attention backends, KV offloading enhancements, multimodal support in the Rust frontend, and migration to Transformers 5.13.0 for several models. vLLM is a key LLM inference infrastructure; this release expands model support to new architectures \(Inkling\) and delivers performance optimizations that improve inference efficiency and reduce deployment costs, benefiting the broader LLM serving community. Inkling is a Mamba-hybrid MoE model with 256 experts, supporting piecewise CUDA graph, Hopper FA4 relative attention, MTP=1 speculative decoding, LoRA, and NVFP4 quantization. DeepSeek-V4 optimizations include a specialized routing kernel \(2.94% E2E TPOT improvement\), fused\_topk\_bias \(1.5-2x kernel speedup\), and redundant repeat/copy removal \(1.8% E2E TPOT\). The attention backend can now be selected per KV-cache group.

github · khluu · Jul 25, 10:38

**Background**: vLLM is an open-source, high-performance LLM inference engine supporting various model architectures and hardware. The Inkling model from Thinking Machines Lab uses a hybrid Mamba-MoE architecture with 256 experts, combining state-space models with mixture-of-experts. Piecewise CUDA graph is a technique that runs attention in eager mode while capturing the rest of the model graph, reducing launch overhead. NVFP4 is a 4-bit floating-point quantization format from NVIDIA ModelOpt, enabling memory-efficient inference.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/features/torch_compile_and_piecewise_cuda_graph.html">Torch Compile &amp; Piecewise CUDA Graph — TensorRT LLM</a></li>
<li><a href="https://docs.vllm.ai/projects/vllm-omni/en/latest/user_guide/quantization/modelopt/">ModelOpt - vLLM-Omni</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#open source`, `#deep learning`

---

<a id="item-2"></a>
## [Open-weight AI is having its Kubernetes moment](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

The article argues that open-weight AI models are becoming the standard platform for AI deployment, analogous to how Kubernetes standardized container orchestration. This shift could lead to commoditization of AI models, enabling startups and enterprises to build on a common, open foundation, reducing vendor lock-in and fostering innovation. The author suggests that American labs need to release frontier-grade open-weight models under permissive licenses for startups to build upon, and that a truly open model would require public training data and collaboration like Linux.

hackernews · tknaup · Jul 25, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49048034)

**Background**: Kubernetes is an open-source container orchestration system that became the industry standard, allowing applications to be deployed and scaled across any cloud. Open-weight AI models are models whose trained parameters \(weights\) are publicly released, enabling anyone to run them locally, fine-tune, or build upon them, unlike closed-source models like GPT-4.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/open-models/">Open models by OpenAI</a></li>
<li><a href="https://onyx.app/self-hosted-llm-leaderboard">Best Self-Hosted LLM Leaderboard 2026 | Open-Weight Model ...</a></li>

</ul>
</details>

**Discussion**: Commenters discuss the feasibility of banning Chinese models, noting weights are just numbers and hard to regulate. They also compare the pricing volatility of API-based models to the stable baseline provided by open-weight models, and foresee a future where companies collaborate on a shared open AI model similar to Linux.

**Tags**: `#open-weight-ai`, `#kubernetes`, `#AI-industry`, `#standards`, `#open-source`

---

<a id="item-3"></a>
## [Ruff v0.16.0 expands default rules from 59 to 413](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0, released on July 23, 2026, increases its default rule set from 59 to 413 rules, enabling many previously disabled checks that catch syntax errors and runtime errors. This change abruptly breaks CI for projects with unpinned Ruff dev dependencies, forcing developers to update code or pin versions. The expanded rule set helps catch severe issues earlier, but requires configuration adjustments. Since Ruff v0.1.0, the total number of rules grew from 708 to 968. New default rules include load-before-global-declaration \(SyntaxError\) and yield-in-init \(immediate runtime error\), which can often be auto-fixed with \`ruff check --fix --unsafe-fixes\`.

rss · Simon Willison · Jul 25, 22:44

**Background**: Ruff is a fast Python linter written in Rust, widely used in CI pipelines. Unpinned dev dependencies \(e.g., \`&quot;ruff&quot;\` without version constraint\) allow automatic updates, which can introduce breaking changes like new default rules, leading to non-reproducible builds and sudden failures.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/rules/load-before-global-declaration/">load - before - global - declaration (PLE0118) | Ruff</a></li>
<li><a href="https://mergify.com/blog/stop-lying-to-your-dependency-resolver-the-real-rules-for-python-dependency-management">Stop Lying to Your Dependency Resolver: The Real Rules... — Mergify</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ ruff : An extremely fast Python linter and code...</a></li>

</ul>
</details>

**Tags**: `#Python`, `#linting`, `#Ruff`, `#CI`, `#software engineering`

---

<a id="item-4"></a>
## [Qualcomm Announces Across-the-Board Price Hike from Sept 1](https://tw.news.yahoo.com/%E7%8D%A8%E5%AE%B6-%E9%AB%98%E9%80%9A%E6%BC%B2%E5%83%B9%E4%BF%A1%E6%9B%9D%E5%85%89-%E5%85%A8%E7%B7%9A%E7%94%A2%E5%93%819-1%E8%B5%B7%E8%AA%BF%E6%BC%B2-%E7%9B%B4%E8%A8%80-142730846.html) ⭐️ 8.0/10

Qualcomm issued a price adjustment notice on July 24, 2026, informing customers that all products shipped on or after September 1 will see price increases. The company cited rising costs in wafer fabrication, packaging, and substrate materials, as well as surging AI and data center demand. As Qualcomm&\#x27;s chips are used in smartphones, PCs, IoT, and automotive, this price hike could ripple through the entire electronics supply chain, potentially leading to higher consumer prices or reduced features. It signals a structural cost increase in semiconductor manufacturing driven by AI demand. Qualcomm did not specify a uniform percentage or list affected product models, but stated that account managers will contact customers individually with new quotes. Orders already placed but scheduled for shipment after September may also be subject to revised pricing.

telegram · zaihuapd · Jul 25, 03:01

**Background**: Advanced packaging refers to techniques that aggregate multiple semiconductor dies into a single package, enabling higher performance and integration without relying solely on transistor scaling. This includes technologies like fan-out wafer-level packaging and 3D ICs. The substrate is a key component that connects the chip to the circuit board, and rising costs for these materials reflect increased demand from AI and data center applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_%28semiconductors%29">Advanced packaging (semiconductors)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Integrated_circuit_packaging">Integrated circuit packaging - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Qualcomm`, `#chip shortage`, `#price hike`, `#AI`, `#supply chain`

---

<a id="item-5"></a>
## [DeepSeek pauses $10B+ funding after founder&\#x27;s leak](https://www.bloomberg.com/news/articles/2026-07-25/deepseek-said-to-tell-backers-of-funding-pause-after-viral-posts) ⭐️ 8.0/10

DeepSeek has orally informed some second-round investors to pause signing investment agreements, partly due to founder Liang Wenfeng&\#x27;s dissatisfaction with leaked internal remarks about investors. This funding pause could reshape the competitive landscape of China&\#x27;s AI industry, as DeepSeek is a major player that recently raised $7 billion. The leak highlights governance challenges in high-profile AI startups. DeepSeek completed its first funding round in June 2026, raising $7 billion, and planned to raise at least 100 billion RMB \(~$14 billion\) in this round at a pre-money valuation of 480 billion RMB \(~$67 billion\). The company is also preparing for an IPO, potentially filing in 2026.

telegram · zaihuapd · Jul 26, 01:17

**Background**: DeepSeek is a Chinese AI startup known for developing competitive large language models. It raised $7 billion in its first funding round in June 2026, backed by Tencent, CATL, and the National AI Industry Investment Fund. The recent funding pause stems from founder Liang Wenfeng&\#x27;s anger over leaked internal comments regarding investor meetings, leading to a reassessment of disclosure processes and investor communication.

**Tags**: `#DeepSeek`, `#AI startup`, `#funding`, `#China AI`, `#business`

---