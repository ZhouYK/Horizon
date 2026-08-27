---
layout: default
title: "Horizon Summary: 2026-08-27 (ZH)"
date: 2026-08-27 00:49:49 +0000
lang: zh
report: default
---

> 从 346 条内容中筛选出 4 条重要资讯。

---

1. [我国首次实现地月双向高速激光通信，下行速率 100Mbps](#item-1) ⭐️ 9.0/10
2. [腾讯开源多模态嵌入模型 WeMM-Embedding，多项基准达 SOTA](#item-2) ⭐️ 8.0/10
3. [阿里通义发布 Qwen3.8-Flash 混合专家模型，称性能比肩 Opus 4.6 与 V4-Flash](#item-3) ⭐️ 8.0/10
4. [Z.ai 发布 GLM-5.3-Flash：320B MoE 模型，激活参数仅 18B，价格降十倍](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [我国首次实现地月双向高速激光通信，下行速率 100Mbps](https://www.stdaily.com/web/gdxw/2026-08/26/content_570163.html) ⭐️ 9.0/10

中国科学院空间应用工程与技术中心牵头，在超过 40 万公里的地月距离上建立了双向激光链路，首次实现了地月双向高速激光通信。试验依托 DRO-A 卫星，初步达到上行 1.25 Mbps、下行 100 Mbps 的速率。 这标志着我国空间激光通信技术从近地轨道迈入地月空间，实现了重大能力跨越。激光通信能够快速传回 8K 月面高清图像等大容量数据，对未来的深空探测和载人登月任务至关重要。 以 8K 月面高清图像为例，传统 5 Mbps 微波下传需要约 4 到 5 分钟，而百 Mbps 激光通信仅需约 12 秒。任务依托运行在远距离逆行轨道上的 DRO-A 卫星实施。

telegram · zaihuapd · 8月27日 00:33

**背景**: 空间激光通信利用激光而非无线电波进行传输，带宽更高、数据传输速度更快。美国 NASA 的深空光通信（DSOC）也已在深空验证了激光链路，而我国此次试验的亮点是在地月距离上实现双向激光链路。DRO-A 是中国部署在地月空间的三星星座之一，其中 DRO-A 卫星驻留在远距离逆行轨道，DRO-B 卫星运行在地月空间机动轨道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.globaltimes.cn/page/202608/1369111.shtml">China achieves 1st two-way laser communication ... - Global Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laser_communication_in_space">Laser communication in space - Wikipedia</a></li>
<li><a href="https://www.bastillepost.com/global/article/4754255-china-builds-three-satellite-constellation-in-earth-moon-space">China builds three- satellite constellation in Earth-moon space</a></li>

</ul>
</details>

**标签**: `#space communication`, `#laser communication`, `#aerospace`, `#scientific breakthrough`, `#China`

---

<a id="item-2"></a>
## [腾讯开源多模态嵌入模型 WeMM-Embedding，多项基准达 SOTA](https://github.com/Tencent/WeMM-Embedding) ⭐️ 8.0/10

腾讯微信视觉团队开源了 WeMM-Embedding 多模态嵌入模型系列，提供 2B、4B、9B 三种参数规模，采用 Apache 2.0 协议。模型统一支持文本、图像、视频、视觉文档及混合多模态输入，在多个基准上取得领先表现。 这一开源具有重要意义，它为开源社区带来了强大的多模态检索能力，有望推动跨模态搜索、检索增强生成（RAG）和文档理解等应用。多规格与宽松许可证使开发者可以在不同硬件上部署，同时保持高性能。 模型基于原生多模态的 Qwen3.5 主干构建，并提供 Matryoshka（俄罗斯套娃）维度，可灵活调整嵌入维度以平衡性能与成本。目前暂不支持音频输入，模型已在 GitHub 和 Hugging Face 上发布。

telegram · zaihuapd · 8月26日 13:15

**背景**: 多模态嵌入模型将来自多种模态（文本、图像、视频、文档）的数据转换为向量，用于检索、聚类和相似度搜索等任务。传统文本嵌入无法理解视觉内容，而多模态模型可以在同一空间中对图像和文本进行联合编码。WeMM-Embedding 进一步支持视频和混合输入，并且采用宽松的 Apache 2.0 许可证，与部分商业产品有所区别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.24053v1">WeMM - Embedding : WeChat Multi-Modal Embedding Technical Report</a></li>
<li><a href="https://github.com/Tencent/WeMM-Embedding">GitHub - Tencent/ WeMM - Embedding : WeMM - Embedding is a family...</a></li>
<li><a href="https://huggingface.co/tencent/WeMM-Embedding-9B">tencent/ WeMM - Embedding -9B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#multimodal-embedding`, `#open-source`, `#Tencent`, `#SOTA`, `#AI/ML`

---

<a id="item-3"></a>
## [阿里通义发布 Qwen3.8-Flash 混合专家模型，称性能比肩 Opus 4.6 与 V4-Flash](https://x.com/Alibaba_Qwen/status/2092591393424515114) ⭐️ 8.0/10

阿里通义发布了多模态混合专家模型 Qwen3.8-Flash，总参数 125B、每个 token 仅激活 6B，并开源了作为 Qwen4 架构预览的 Qwen3.8-Flash-Next。阿里称其性能可与 Anthropic Opus 4.6 和 DeepSeek V4-Flash 比肩。 这一发布意义重大，因为它将前沿水平性能带入开源模型，同时大幅降低训练和推理成本。开发者可以以每百万输入 tokens 0.16 美元、每百万输出 tokens 0.47 美元的价格采用 Qwen3.8-Flash。 该模型原生上下文长度为 262K tokens，可扩展至 1M，训练成本仅为 Qwen3.7-Plus 的大约九分之一，且在编码和办公任务上表现更优。Qwen3.8-Flash 是 Qwen3.8-Flash-Next 的生产版本，默认支持 1M 上下文并内置工具。

telegram · zaihuapd · 8月26日 13:36

**背景**: 混合专家（MoE）模型每个 token 只激活一小部分参数，从而在保留大参数总量的同时降低计算和推理成本。Qwen3.8-Flash-Next 是 Qwen4 所基于架构的早期预览，类似于 Qwen3-Next 对 Qwen3.5 系列所起的作用。其设计延续了 Qwen3.5/3.6 系列中出现的混合 Gated DeltaNet + Gated Attention 结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/ Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>
<li><a href="https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next">Qwen 3 . 8 - Flash - Next - SGLang Documentation</a></li>

</ul>
</details>

**标签**: `#AI`, `#Model Release`, `#MoE`, `#Qwen`, `#Cost Efficiency`

---

<a id="item-4"></a>
## [Z.ai 发布 GLM-5.3-Flash：320B MoE 模型，激活参数仅 18B，价格降十倍](http://z.ai/) ⭐️ 8.0/10

Z.ai 发布了 GLM-5 系列首个原生多模态模型 GLM-5.3-Flash，总参数量 320B，激活参数仅 18B。其 API 价格约为上一代的十分之一，限时输入价格低至每百万 tokens 0.075 美元。 该发布推动了大型 MoE 模型的高效推理与降本，性能接近更大规模的稠密模型，同时使先进 AI 的部署成本大幅降低。它也表明国产 AI 芯片获得更多信心，官方称在国产硬件上端到端推理性能提升 3 倍。 GLM-5.3-Flash 采用稀疏与线性注意力混合架构，匿名测试期间成为本周最受欢迎模型，且全部流量由国产 AI 芯片服务。标准价格为每百万 tokens 输入 0.15 美元、缓存输入 0.03 美元、输出 0.50 美元，缓存存储暂时免费。

telegram · zaihuapd · 8月26日 14:23

**背景**: MoE（混合专家）模型保持总参数量很大，但每个 token 只激活一小部分专家，因此激活参数数量决定推理速度和成本，总参数量决定内存占用。稀疏注意力通过只关注部分 token 来减少计算，而线性注意力以 O\(N\) 复杂度近似完整注意力，将两者结合可以进一步提升效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters : What’s the Difference?</a></li>
<li><a href="https://latenteast.com/insights/moe-total-vs-active-parameters">MoE Total vs Active Parameters , Explained | The Latent East</a></li>
<li><a href="https://arxiv.org/pdf/2507.19595">Efficient Attention Mechanisms for Large Language Models: A Survey</a></li>

</ul>
</details>

**标签**: `#AI`, `#GLM`, `#model release`, `#efficiency`, `#hardware`

---