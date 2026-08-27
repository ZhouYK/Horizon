---
layout: default
title: "Horizon Summary: 2026-08-27 (EN)"
date: 2026-08-27 00:49:49 +0000
lang: en
report: default
---

> From 346 items, 4 important content pieces were selected

---

1. [China Achieves First Earth-Moon Bidirectional High-Speed Laser Communication](#item-1) ⭐️ 9.0/10
2. [Tencent Open-Sources Multimodal Embedding Family WeMM-Embedding](#item-2) ⭐️ 8.0/10
3. [Alibaba Qwen Releases Qwen3.8-Flash, Claiming Performance On Par with Top Models](#item-3) ⭐️ 8.0/10
4. [Z.ai Releases GLM-5.3-Flash: 320B MoE, 10x Cheaper, Runs on Domestic Chips](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [China Achieves First Earth-Moon Bidirectional High-Speed Laser Communication](https://www.stdaily.com/web/gdxw/2026-08/26/content_570163.html) ⭐️ 9.0/10

The Chinese Academy of Sciences&\#x27; Technology and Engineering Center for Space Utilization successfully established a bidirectional laser link over 400,000 kilometers, demonstrating the first Earth-Moon bidirectional high-speed laser communication. The test achieved a downlink rate of 100 Mbps and an uplink rate of 1.25 Mbps using the DRO-A satellite. This milestone marks China&\#x27;s space laser communication capability expanding from near-Earth orbit to cislunar space, significantly enhancing deep-space data transmission. It enables rapid delivery of high-resolution scientific data, such as 8K lunar imagery, and lays a critical foundation for future lunar exploration and deep-space missions. The DRO-A satellite carried the laser communication payload, jointly developed by CAS and Zhijiang Laboratory. The uplink rate was 1.25 Mbps and the downlink rate 100 Mbps; a 8K lunar image that takes 4–5 minutes over a 5 Mbps microwave link can be transmitted in about 12 seconds via this laser link.

telegram · zaihuapd · Aug 27, 00:33

**Background**: Laser communication uses light beams to encode and transmit data, offering far higher bandwidth than traditional radio-frequency \(RF\) communications. Achieving a reliable link over the 400,000 km Earth-Moon distance requires extremely precise beam acquisition, pointing, and tracking, as atmospheric turbulence and distance attenuation pose major challenges. The DRO-A satellite, developed by Chinese research institutions, served as the test platform for this demonstration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.chinanews.com.cn/sh/2026/08-26/10684802.shtml">地月“信息高速路”开通 中国空间激光通信迈入地月空间-中新网</a></li>
<li><a href="https://www.ithome.com/0/994/732.htm">地 月 “ 信 息 高 速 路” 通 了：我国成功建立超过 40 万公里 双 向 激 光 链路 - IT...</a></li>

</ul>
</details>

**Tags**: `#space communication`, `#laser communication`, `#aerospace`, `#scientific breakthrough`, `#China`

---

<a id="item-2"></a>
## [Tencent Open-Sources Multimodal Embedding Family WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) ⭐️ 8.0/10

Tencent&\#x27;s WeChat Vision team released WeMM-Embedding, a family of universal multimodal embedding models in 2B, 4B, and 9B parameter sizes. The models are open-sourced under the Apache 2.0 license and achieve state-of-the-art results on multiple benchmarks, though audio input is not yet supported. Multimodal embeddings unify text, image, video, and document representations in a shared vector space, which is crucial for retrieval and RAG. Tencent&\#x27;s open-source release with permissive licensing could accelerate research and production use of multimodal search across the community. The three model sizes are built on natively multimodal Qwen3.5 backbones. WeMM-Embedding supports text, image, video, visual documents, and hybrid multimodal inputs, but does not support audio. The technical report is available on arXiv.

telegram · zaihuapd · Aug 26, 13:15

**Background**: Embedding models map data into vectors, enabling semantic similarity search. Multimodal embedding models extend this to multiple data types, allowing cross-modal retrieval such as searching images with text or matching videos to documents. Tencent&\#x27;s release follows a trend of large tech companies open-sourcing foundation models to encourage community adoption and ecosystem growth.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent/WeMM-Embedding">GitHub - Tencent/ WeMM - Embedding : WeMM - Embedding is a family...</a></li>
<li><a href="https://arxiv.org/html/2608.24053v1">WeMM - Embedding : WeChat Multi-Modal Embedding Technical Report</a></li>

</ul>
</details>

**Tags**: `#multimodal-embedding`, `#open-source`, `#Tencent`, `#SOTA`, `#AI/ML`

---

<a id="item-3"></a>
## [Alibaba Qwen Releases Qwen3.8-Flash, Claiming Performance On Par with Top Models](https://x.com/Alibaba_Qwen/status/2092591393424515114) ⭐️ 8.0/10

Alibaba&\#x27;s Qwen team released Qwen3.8-Flash, a multimodal Mixture-of-Experts reasoning model with 125B total parameters and only 6B activated per token. It also open-sourced Qwen3.8-Flash-Next as an early preview of the Qwen4 architecture, claiming performance comparable to Anthropic Opus 4.6 and DeepSeek V4-Flash. This release is significant because it brings frontier-level reasoning and multimodal ability to open-source models at a fraction of the cost, undercutting proprietary competitors on price. Developers can now serve a 1M-token-context model for $0.16 per million input tokens, which could reshape cost expectations for agentic and long-video workflows. Qwen3.8-Flash supports a native context of 262K tokens, extendable to 1M, and is priced at $0.16 per million input tokens and $0.47 per million output tokens. Its training cost is roughly one-ninth that of Qwen3.7-Plus, and it reportedly performs better on coding and office tasks; the open-weights Qwen3.8-Flash-Next preview highlights Qwen4 architecture changes in attention, residual flow, embeddings, and optimization.

telegram · zaihuapd · Aug 26, 13:36

**Background**: Mixture of Experts \(MoE\) is an architecture that splits a model into specialized &\#x27;expert&\#x27; sub-networks and activates only a small subset for each token, allowing large total parameter counts without proportional compute cost. Qwen is Alibaba&\#x27;s open-source model family; Qwen3.7-Plus is an earlier API model, while Opus 4.6 and V4-Flash are top-tier competitors from Anthropic and DeepSeek. The &\#x27;Flash&\#x27; naming indicates a lightweight, low-cost tier, and Qwen3.8-Flash-Next is an early open-weights release meant to preview the architecture of the upcoming Qwen4 family.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/ramses-engineering/not-one-brain-but-many-how-mixture-of-experts-moe-makes-ai-smarter-and-faster-568f41220852">Not One Brain, But Many: How Mixture of Experts ( MoE )... | Medium</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next-FP8">Qwen/ Qwen 3 . 8 - Flash -Next-FP8 · Hugging Face</a></li>
<li><a href="https://developer.tenten.co/qwen38-flash-next-qwen4-architecture">Qwen3.8-Flash-Next: A Qwen 4 Architecture Preview</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Model Release`, `#MoE`, `#Qwen`, `#Cost Efficiency`

---

<a id="item-4"></a>
## [Z.ai Releases GLM-5.3-Flash: 320B MoE, 10x Cheaper, Runs on Domestic Chips](http://z.ai/) ⭐️ 8.0/10

Z.ai released GLM-5.3-Flash, its first natively multimodal model in the GLM-5 series, with 320B total parameters and only 18B active parameters. During a limited-time promotion, API input costs $0.075 per million tokens — roughly one-tenth the price of its predecessor, GLM-5.2. The 10x price cut makes frontier-scale intelligence far more accessible to developers and enterprises, while the hybrid sparse/linear attention architecture enables efficient long-context inference. Running entirely on domestic AI chips with a 3x inference performance boost signals a maturing domestic ecosystem that could reduce dependence on Nvidia GPUs — significant for China&\#x27;s AI supply chain and for global AI cost economics. The model uses a Mixture-of-Experts architecture with 320B total and 18B active parameters, combining sparse attention with linear attention. Limited-time API prices are $0.075 per million input tokens, $0.015 for cached input, and $0.25 for output \(cache storage free\), while regular prices are $0.15, $0.03, and $0.50 respectively; it also outperforms GLM-5.2 on several coding and agent benchmarks, approaching Claude Opus 4.8.

telegram · zaihuapd · Aug 26, 14:23

**Background**: Large language models fall into dense models, which activate all parameters for every token, and Mixture-of-Experts \(MoE\) models, which route each token to a small subset of &\#x27;expert&\#x27; sub-networks via a router. In MoE, total parameters determine storage footprint while active parameters determine per-token compute cost, so the 320B/18B design aims for high capability at lower inference expense. &\#x27;Linear attention&\#x27; refers to Transformer-style mechanisms that replace softmax with kernel feature maps, reducing quadratic complexity to linear — valuable for long-context tasks. Z.ai&\#x27;s hybrid sparse/linear attention and domestic-chip deployment mirror a broader trend among Chinese AI labs to cut serving costs and reduce reliance on Nvidia GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://latenteast.com/insights/moe-total-vs-active-parameters">MoE Total vs Active Parameters , Explained | The Latent East</a></li>
<li><a href="https://www.emergentmind.com/topics/linear-attention">Linear Attention in Transformers</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts ( MoE )</a></li>

</ul>
</details>

**Tags**: `#AI`, `#GLM`, `#model release`, `#efficiency`, `#hardware`

---