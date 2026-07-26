---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
report: ai
---

> 从 137 条内容中筛选出 10 条重要资讯。

---

1. [英伟达与 SK 集团宣布 5000 亿美元 AI 合作](#item-1) ⭐️ 9.0/10
2. [Black Forest Labs 发布 Flux3，原生同步音视频生成](#item-2) ⭐️ 9.0/10
3. [Ruff v0.16.0 大幅扩展默认规则，导致未固定依赖的 CI 中断](#item-3) ⭐️ 8.0/10
4. [中国 AI 模型 Kimi K3 引发硅谷警惕](#item-4) ⭐️ 8.0/10
5. [多家科技巨头联合支持开放权重 AI 模型](#item-5) ⭐️ 8.0/10
6. [哥伦比亚大学警告：AI 聊天机器人是糟糕的治疗师](#item-6) ⭐️ 8.0/10
7. [硅谷对中国 AI 人才入境限制存在分歧](#item-7) ⭐️ 8.0/10
8. [菲尔兹奖得主齐默尔曼加入 OpenAI 从事 AI 安全研究](#item-8) ⭐️ 8.0/10
9. [小鹏人形机器人开始试生产，目标 2026 年量产](#item-9) ⭐️ 8.0/10
10. [谷歌 Q2 资本支出翻倍至 449 亿美元，用于 AI 基础设施](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [英伟达与 SK 集团宣布 5000 亿美元 AI 合作](https://news.google.com/rss/articles/CBMirwJBVV95cUxNdFVPajJESWc0ZHlxdk1Rdkhja3E4NXktbU12VFBNVWFFQzlRZ3R0bElJNVV1RlRsRUpkcXR5Q0hZWEVNQ0NzQVpjUU8tenlDaVp6VEVMMnhtQjlTd21KTVd4M0Vkd3JuUDZEX3QyUU5EUzAtTlJOUF9iMDg2OThmdHcwaFlvYWgxeVpjSlMwdnRBV1ppRklFQmh6OHdqSEpYT005U2h2Q3hVcjc5eEdmNXdEaExRb2o4THc1Vmt4dXJkRkI3N2g4eS04RE90VTRocU1CcE5zeXd5X0ZFeE5YcjJOMmxfMkpYOHkzOG1Sd0lROVZITDRieWthbG5MN2ljQ3V0b1BkdE10WFMwMUNEMXBrN1g3WjhsWWZ5VmR5YUdfTkYycVhGMUp3emlhZXc?oc=5) ⭐️ 9.0/10

英伟达与 SK 集团宣布了一项 5000 亿美元的 AI 合作，旨在开发下一代内存技术并建设大规模 AI 工厂。该合作将结合英伟达的 GPU 专长与 SK 集团的先进内存解决方案，以加速 AI 基础设施建设。 此次合作意义重大，因为它解决了 AI 基础设施中的关键瓶颈：高带宽内存短缺以及对专用数据中心的需求。通过确保下一代内存的稳定供应和专用 AI 工厂的建设，它可能加速 AI 发展，影响从云计算到自动驾驶等多个行业。 该合作包括开发下一代高带宽内存（HBM）以及建设吉瓦级 AI 工厂。SK 集团的子公司 SK 海力士是 HBM 生产的领导者，HBM 对英伟达的 AI 加速器至关重要。

google\_news · Tom&\#x27;s Hardware · 7月25日 13:55

**背景**: 高带宽内存（HBM）是一种先进的内存技术，可为 AI 和高性能计算工作负载提供巨大的吞吐量。AI 工厂是专门优化的数据中心，用于训练大型 AI 模型，需要密集的 GPU 集群和先进的冷却系统。目前全球内存市场正因 AI 需求而出现短缺，供应限制预计将持续到 2028 年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HBM_memory_shortage">HBM memory shortage</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="http://datacentersx.com/types-ai-factory.html">AI Factory Data Center | Data Center Types</a></li>

</ul>
</details>

**标签**: `#AI`, `#hardware`, `#partnership`, `#memory`, `#infrastructure`

---

<a id="item-2"></a>
## [Black Forest Labs 发布 Flux3，原生同步音视频生成](https://www.aibase.com/news/29874) ⭐️ 9.0/10

Black Forest Labs 发布了 Flux3，这是一个多模态基础模型，能够一次性生成最长 20 秒的同步音视频内容。它是首个原生支持音频生成的同类模型，基于 Self-Flow 自监督流匹配架构构建。 Flux3 在生成式 AI 领域实现了重大突破，通过单个原生模型统一了图像、视频和音频生成，不再需要额外的音频后期同步。这将加速电影、广告和虚拟现实等内容创作，并为多模态基础模型树立新标准。 Flux3 采用 Self-Flow 架构，为图像、视频、音频和运动分别配备专用编码器/解码器。它支持文本到视频、图像到视频、视频到视频、关键帧转换和多语言对话，性能优于 Luma 和 Runway 等早期模型。

aibase · AIbase · 7月25日 08:43

**背景**: 传统的生成模型通常分别生成视频和音频，需要手动同步。Self-Flow 是一种自监督流匹配框架，将表征学习与生成相结合，通过双时间步调度创建信息不对称以实现稳健的多模态训练。Flux3 扩展了这种方法，跨模态联合学习，从而实现原生同步输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-decoder.com/flux-3-generates-videos-with-native-audio-up-to-20-seconds-long-a-first-for-black-forest-labs/">Flux 3 generates videos with native audio up to 20 seconds long, a first for Black Forest Labs</a></li>
<li><a href="https://github.com/black-forest-labs/Self-Flow">GitHub - black-forest-labs/Self-Flow: [ICML&#x27;26] Code and website for Self-Flow: Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2603.06507">[2603.06507] Self-Supervised Flow Matching for Scalable Multi ... Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis GitHub - black-forest-labs/Self-Flow: [ICML&#x27;26] Code and ... Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis ICML Poster Self-Supervised Flow Matching for Scalable Multi ... Self-Supervised Flow Matching - emergentmind.com Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#audio-visual generation`, `#foundation model`, `#generative AI`, `#Flux3`

---

<a id="item-3"></a>
## [Ruff v0.16.0 大幅扩展默认规则，导致未固定依赖的 CI 中断](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0 于 7 月 23 日发布，将默认规则集从 59 条扩展到 413 条，导致未固定 &\#x27;ruff&\#x27; 开发依赖的项目 CI 失败。 这一变化显著加强了 Python 项目的默认 linting 检查，能够更早捕捉严重问题，但也迫使开发者要么固定依赖版本，要么更新代码以符合新规则。 新规则包括对语法错误和运行时错误（如 &\#x27;yield in \_\_init\_\_&\#x27;）的检查。Simon Willison 的项目发现了数百个问题，大部分通过 &\#x27;--fix --unsafe-fixes&\#x27; 自动修复。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的快速 Python 代码检查工具，广泛用于 Python 生态系统。默认规则是开箱即用的，许多项目依赖未固定的依赖项（通常不指定 &\#x27;ruff&\#x27; 版本），这使得它们在发布新版本时容易受到破坏性变更的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fossa.com/glossary/dependency-pinning/">Dependency Pinning | FOSSA Software Supply Chain Glossary</a></li>

</ul>
</details>

**标签**: `#Ruff`, `#Python`, `#linting`, `#release`, `#Astral`

---

<a id="item-4"></a>
## [中国 AI 模型 Kimi K3 引发硅谷警惕](https://news.google.com/rss/articles/CBMiswFBVV95cUxOVlhNQ1NiUVI1eGN0bXF5S01TTm1tQlJWYjZsUWFZRkxxY0xJdVFTRlhNSzBJa01tT2I3TmE1TGtjX3dqbGJRRHZJOFlqbGJTOWdnMFJlMFVqYV9FVmFtWU5jUmVlT0lrc0Y5b25nTWlJZEwzRTNOMUpxb2pMR3F4NlVzZWp2UXlDZlBEMWxnelpsQWdQSDFXNGtJQXVzWlVZTmswQl9MQ2ZjaEpEYlpNd0xiWdIBxwFBVV95cUxOQW5CUzROYzFIVlEtblVsdzQ1Sm0teWhvdnU4M1F0SHkzeFRmdW51YU11TEZCS3VlVVpEUUl4by1mbVhYZzRkOHdpY2R6N0k3cEhaUHUxdkl1c3l2cDFFOXpQbUdBV25rUkhyR2dZMkRSUmtVN0dDbzhZeFF5V3VSNTNMbHlpSDJ3WlhNTEtET3RlRDJlZWJJaWh5enpiOXF2NGFxWlJrbXlhaWlvM0x4V2pLMEF6MWdLMi1aS25iQXJUOG9iMGFN?oc=5) ⭐️ 8.0/10

月之暗面（Moonshot AI）发布了 Kimi K3，这是一个 2.8 万亿参数的多模态推理模型，拥有 100 万 token 的上下文窗口，标志着对美国 AI 主导地位的重大竞争威胁。 Kimi K3 的能力可与美国顶尖实验室的模型相媲美，加剧了全球 AI 竞赛，促使硅谷重新评估其竞争地位。 该模型权重开放，具备原生视觉能力，基于 Kimi Delta Attention 和 Attention Residuals 构建。它是 2026 年最强大的模型之一。

google\_news · EL PAÍS English · 7月26日 04:00

**背景**: Kimi K3 由中国 AI 初创公司月之暗面（Moonshot AI）开发。拥有 2.8 万亿参数，是有史以来最大的 AI 模型之一，直接与 GPT-4 等模型竞争。100 万 token 的上下文窗口允许一次性处理大量文本，这是复杂任务的关键优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K 3 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://benchlm.ai/models/kimi-3">Kimi K 3 Benchmarks, Pricing &amp; Speed (July 2026) | BenchLM. ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#China`, `#Silicon Valley`, `#competition`

---

<a id="item-5"></a>
## [多家科技巨头联合支持开放权重 AI 模型](https://news.google.com/rss/articles/CBMipAFBVV95cUxOS0hQcXlIMVB5UFFwVXM1Y0pZQm5XOXBzUmNveTg4RjZCc2RNdjdOVFV4U2JDZWdrTTRuTVROZ3lodE5FRVpielNWTVUyaFJkQlhHLVZmSVBWc1BRUHhNS1dNUjNTZ1lCb0drYk9pQ2hLQUtIUXlQUUc4eDNGVGYxOVQ5S1JSaDF0Q3BKSFFncDBKYUZCVV9fTm1aZXd6bjZKanB2dg?oc=5) ⭐️ 8.0/10

Meta、Microsoft、Nvidia、IBM 等领先科技公司联合宣布支持开放权重 AI 模型，标志着行业向更透明、更易获取的人工智能迈出重要一步。 此次合作可能通过让更多人访问强大模型、促进社区发展并减少对专有系统的依赖来加速 AI 创新。这代表着 AI 行业向开放与协作的重大转变。 开放权重模型是指训练后的参数（权重和偏置）公开发布的 AI 系统，任何人都可以下载和使用。但与完全开源模型不同，开放权重模型通常不包括训练数据或代码。

google\_news · AI News · 7月26日 02:47

**背景**: 开放权重模型是指最终权重和偏置公开发布的 AI 模型，用户可以在本地运行。这与仅提供 API 的封闭模型形成对比。科技巨头的此举旨在标准化并推广这种开放性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#industry news`, `#Meta`, `#Microsoft`

---

<a id="item-6"></a>
## [哥伦比亚大学警告：AI 聊天机器人是糟糕的治疗师](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5qSDNDZHVzUmtwbzkybUFpRGV2MWN4ZVpoRW13Q2ZtRWdMc3U2VEZyLVNYZnNEeHZLMEpzWElCYnhWRmticlBRRWFXRkNuZWJxQ2xDMFVKN1FqaGRpQkx3ZkU3Tmkta1U?oc=5) ⭐️ 8.0/10

哥伦比亚大学发表文章，详细解释了为什么 AI 聊天机器人不适合且可能有害地替代人类治疗师，指出其缺乏伦理基础且无法形成治疗联盟。 随着 AI 心理健康应用日益流行，这一批评性分析凸显了依赖聊天机器人进行治疗的潜在风险，呼吁用户和开发者保持谨慎。它强调了在数字心理健康领域建立伦理标准和人类监督的必要性。 文章强调，聊天机器人无法复制人类治疗联盟，而这是治疗成功的关键因素。研究也表明，AI 治疗师通常缺乏共情，并可能提供有害建议。

google\_news · Columbia University · 7月26日 04:56

**背景**: 治疗联盟是指治疗师与来访者之间的合作关系，是有效心理治疗的核心。尽管 AI 聊天机器人易于获取，但它们无法真正理解或回应人类情感。这篇哥伦比亚大学的文章是日益增多的质疑 AI 驱动疗法有效性和安全性的研究的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.psychologytoday.com/us/blog/the-future-brain/202605/ai-chatbot-therapists-lack-ethics-study-finds">AI Chatbot Therapists Lack Ethics, Study Finds - Psychology Today</a></li>
<li><a href="https://www.psychologytoday.com/us/blog/some-assembly-required/202510/therapy-using-ai-chatbots-is-not-just-risky-its-dangerous">When AI Therapy Goes Wrong - Psychology Today</a></li>
<li><a href="https://www.forbes.com/health/mind/ai-therapy/">AI Therapy: How It Works, Benefits &amp; Limitations - Forbes</a></li>

</ul>
</details>

**标签**: `#AI`, `#mental health`, `#ethics`, `#chatbot`

---

<a id="item-7"></a>
## [硅谷对中国 AI 人才入境限制存在分歧](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMGg1N0lvWXlpTm43VlhleE5IZmNpNDhTTWFZbzBnV1lUY1FCa212cl93ZkVtU00waTNFMnhib0RnaFl1MVBvZEpVbVVwUmlod1FMTV9Qazh4NjVVNThXTnZXN3U0RFBXU1Rwd3JLcjNPSjYxN0gzbzR0bkdUMmg4NElGRVVHZzdDSE5N?oc=5) ⭐️ 8.0/10

《纽约时报》报道称，硅谷在是否限制中国 AI 研究人员和工程师入境问题上存在分歧，这反映了科技界在国家安全与人才流动问题上的深刻对立。 这场辩论可能影响美国 AI 竞争力和全球人才流动。限制中国 AI 人才可能保护国家安全，但有可能减缓创新并使美国脱离全球研究网络。 文章强调，硅谷一些人主张开放边界以吸引顶尖 AI 人才，而另一些人则因担心知识产权盗窃和间谍活动而支持更严格的政策。这种分歧反映了美中之间更广泛的地缘政治紧张局势。

google\_news · The New York Times · 7月25日 13:00

**背景**: AI 研究严重依赖全球人才，中国研究人员一直是美国 AI 劳动力中的重要组成部分。近期美国政府已收紧对敏感领域中国公民的签证政策。硅谷的辩论聚焦于如何在国家安全与创新及人才多元化的需求之间取得平衡。

**标签**: `#AI`, `#geopolitics`, `#immigration`, `#technology policy`, `#Silicon Valley`

---

<a id="item-8"></a>
## [菲尔兹奖得主齐默尔曼加入 OpenAI 从事 AI 安全研究](https://www.aibase.com/news/29878) ⭐️ 8.0/10

菲尔兹奖得主雅各布·齐默尔曼宣布，在 2026 年国际数学家大会上获得菲尔兹奖后，他将加入 OpenAI 从事 AI 安全研究。 这一动向标志着顶尖数学人才向 AI 研究（尤其是安全领域）转移的趋势日益增长，凸显了该领域的重要性以及对严谨数学基础的需求。 齐默尔曼因证明 o-minimality 中的核心猜想而获奖。他将在 OpenAI 专注于 AI 安全，但具体项目尚未披露。

aibase · AIbase · 7月25日 08:43

**背景**: 菲尔兹奖是数学界最高荣誉，每四年颁发一次，授予 40 岁以下的数学家。O-minimality 是模型论中的一个概念，研究实几何中的驯顺结构，并应用于丢番图几何。AI 安全研究旨在确保人工智能系统可靠且符合伦理地运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/O-minimal_theory">O-minimal theory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#Fields Medal`, `#mathematics`, `#research`

---

<a id="item-9"></a>
## [小鹏人形机器人开始试生产，目标 2026 年量产](https://www.aibase.com/news/29875) ⭐️ 8.0/10

小鹏的人形机器人已在广州工厂进入小批量试产阶段，量产线正在进行最后集成。董事长何小鹏亲自担任机器人业务 CEO，推动商业化。 这一里程碑标志着小鹏正认真推进人形机器人商业化，拓展其核心电动车业务之外的领域。这可能加速中国乃至全球人形机器人行业的竞争和投资。 试产在小鹏广州工厂进行，目标是在 2026 年正式实现量产。董事长何小鹏担任机器人业务单元 CEO。

aibase · AIbase · 7月25日 08:43

**背景**: 人形机器人旨在模仿人类外观和运动，用于制造、服务和家庭等场景。小鹏主要以电动车闻名，其在 AI 日活动中展示了名为 Iron 的人形机器人，机器人因在演示中摔倒而引发关注。公司认为机器人是其 AI 和制造能力的自然延伸。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2ljM3JLN0VCSGdHa19uNzBCV0ZpZ0FQAQ?hl=en-US&amp;gl=US&amp;ceid=US:en">Google News - Xpeng &#x27;s robot debut in Shenzhen - Overview</a></li>
<li><a href="https://parametric-architecture.com/xpeng-iron-next-gen-humanoid-robot/">XPENG IRON: China’s Next-Gen Humanoid Robot That Moves Like...</a></li>

</ul>
</details>

**标签**: `#humanoid robots`, `#manufacturing`, `#XPeng`, `#robotics`, `#AI`

---

<a id="item-10"></a>
## [谷歌 Q2 资本支出翻倍至 449 亿美元，用于 AI 基础设施](https://www.aibase.com/news/29870) ⭐️ 8.0/10

Alphabet 第二季度资本支出同比增长 100%，达到 449 亿美元，主要得益于对 AI 基础设施的大规模投资。谷歌云收入增长 82%至 248 亿美元，营业利润率几乎翻倍。 这一巨额投资表明谷歌将 AI 视为核心增长动力的积极押注，而云计算盈利能力的飙升表明 AI 基础设施支出正在转化为强劲的财务回报。这为其他在 AI 和云市场竞争的科技巨头树立了标杆。 年化资本支出接近 1800 亿美元，表明持续的高额支出。云计算利润率翻倍突显出计算能力投资正成为重要的利润驱动力。

aibase · AIbase · 7月25日 08:43

**背景**: 科技公司的资本支出包括对 AI 工作负载所需的数据中心、服务器和网络设备的投资。谷歌一直在扩展其 AI 基础设施，包括 TPU 芯片和数据中心，以支持 Gemini 和 Cloud AI 等服务。强劲的云业务结果反映了企业对谷歌云 AI 产品日益增长的使用。

**标签**: `#AI infrastructure`, `#cloud computing`, `#capital expenditure`, `#Google`, `#financial results`

---