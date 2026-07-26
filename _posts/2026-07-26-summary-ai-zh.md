---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
report: ai
---

> 从 213 条内容中筛选出 10 条重要资讯。

---

1. [英伟达与 SK 集团达成 5000 亿美元 AI 合作](#item-1) ⭐️ 9.0/10
2. [Black Forest Labs 发布 Flux3：首个原生多模态音视频模型](#item-2) ⭐️ 9.0/10
3. [英伟达投资 15 亿美元与安靠合作扩大 AI 芯片封装](#item-3) ⭐️ 9.0/10
4. [Ruff v0.16.0 默认规则从 59 条扩展至 413 条](#item-4) ⭐️ 8.0/10
5. [韩国巨头将 AI 合作伙伴关系扩大至 9500 亿美元](#item-5) ⭐️ 8.0/10
6. [英伟达等 25 家公司呼吁谨慎对待开放 AI 模型限制](#item-6) ⭐️ 8.0/10
7. [Meta、微软、英伟达、IBM 等公司支持开放权重 AI](#item-7) ⭐️ 8.0/10
8. [硅谷就限制中国 AI 研究人员出现分歧](#item-8) ⭐️ 8.0/10
9. [菲尔兹奖得主加入 OpenAI 研究 AI 安全](#item-9) ⭐️ 8.0/10
10. [腾讯合并多模态与大语言模型部门为基座模型部](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [英伟达与 SK 集团达成 5000 亿美元 AI 合作](https://news.google.com/rss/articles/CBMirwJBVV95cUxNdFVPajJESWc0ZHlxdk1Rdkhja3E4NXktbU12VFBNVWFFQzlRZ3R0bElJNVV1RlRsRUpkcXR5Q0hZWEVNQ0NzQVpjUU8tenlDaVp6VEVMMnhtQjlTd21KTVd4M0Vkd3JuUDZEX3QyUU5EUzAtTlJOUF9iMDg2OThmdHcwaFlvYWgxeVpjSlMwdnRBV1ppRklFQmh6OHdqSEpYT005U2h2Q3hVcjc5eEdmNXdEaExRb2o4THc1Vmt4dXJkRkI3N2g4eS04RE90VTRocU1CcE5zeXd5X0ZFeE5YcjJOMmxfMkpYOHkzOG1Sd0lROVZITDRieWthbG5MN2ljQ3V0b1BkdE10WFMwMUNEMXBrN1g3WjhsWWZ5VmR5YUdfTkYycVhGMUp3emlhZXc?oc=5) ⭐️ 9.0/10

英伟达与 SK 集团宣布了一项 5000 亿美元的合作，专注于下一代内存技术（HBM4）和大型 AI 工厂，以构建下一代 AI 基础设施。 这一合作将确保高带宽内存的稳定供应并扩大 AI 计算能力，从而显著加速 AI 发展，解决 AI 基础设施中的关键瓶颈。 合作内容包括 SK 集团旗下的 SK 海力士向英伟达供应下一代 HBM4 内存，以及建设专门用于 AI 工作负载的 AI 工厂（即专用数据中心）。

google\_news · Tom&\#x27;s Hardware · 7月25日 13:55

**背景**: AI 工厂是专门建造的设施，集成加速计算硬件（如英伟达 GPU）和 AI 软件，以大规模生成 token。高带宽内存（HBM）是一种 3D 堆叠内存技术，对 AI 和高性能计算工作负载至关重要；当前的 HBM 短缺正促使内存制造商优先为 AI 数据中心生产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/solutions/ai-factories/">Data Center Solutions: AI Factories | NVIDIA</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#hardware`, `#partnership`, `#infrastructure`, `#memory`

---

<a id="item-2"></a>
## [Black Forest Labs 发布 Flux3：首个原生多模态音视频模型](https://www.aibase.com/news/29874) ⭐️ 9.0/10

Black Forest Labs 发布了 Flux3，这是一个基于 Self-Flow 架构的多模态基础模型，能够单次生成最长 20 秒的同步音频和视频。这是首个原生联合生成两种模态而无需后期对齐的模型。 Flux3 通过将音频和视频生成集成到单个原生模型中，标志着向统一多模态 AI 迈出了重要一步，有望简化内容创作流程。它优于先前针对特定生成任务的模型如 Luma 和 Runway，为同步音视频生成树立了新标杆。 Flux3 在 Self-Flow 框架内为图像、视频、音频和动作使用了专用编解码器，实现了跨模态的统一理解与生成。它支持文生视频、图生视频、关键帧转场以及多语言对话，并能输出最长 20 秒带原生音频的视频。

aibase · AIbase · 7月25日 09:09

**背景**: 多模态 AI 模型旨在单一架构内处理和生成多种数据类型（如文本、图像、视频、音频）。Flux3 基于 Self-Flow 自监督流匹配框架构建，该框架将流匹配生成范式扩展为联合建模不同模态。这与早期常使用独立模型或后期同步来实现音视频生成的方法形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bfl.ai/blog/flux-3">FLUX 3 - Real World Models: Towards Multimodal Flow Models as the...</a></li>
<li><a href="https://cctest.ai/en/articles/black-forest-labs-unveils-flux3-a-multimodal-model-built-for-native-audio-video-generation">Flux3 multimodal model debuts with native audio-video... - CCTest</a></li>

</ul>
</details>

**标签**: `#multimodal AI`, `#generative models`, `#audio generation`, `#video generation`, `#foundation model`

---

<a id="item-3"></a>
## [英伟达投资 15 亿美元与安靠合作扩大 AI 芯片封装](https://www.aibase.com/news/29861) ⭐️ 9.0/10

英伟达与安靠技术（Amkor）签署了价值约 15 亿美元的多年协议，用于扩建亚利桑那州的先进封装产能，重点开发用于 AI 和数据中心芯片的高密度互连和异构集成技术。 这笔投资为英伟达的 AI 芯片确保了关键的先进封装供应，减少对海外供应商的依赖，并确保能够满足云服务商和 AI 企业日益增长的需求。同时，它也强化了美国在先进封装领域的半导体供应链，而先进封装是 AI 计算的关键瓶颈。 合作涉及英伟达预付资金以支持安靠在亚利桑那州的设施扩建，双方将共同开发包括高密度互连和异构集成在内的先进封装技术。此举正值英伟达 H100 和 B200 等 AI 加速器需求持续飙升之际。

aibase · AIbase · 7月25日 09:09

**背景**: 先进封装将多个芯片组合到一个封装中以提升性能并降低功耗，这对 AI 加速器至关重要。台积电的 CoWoS 等技术用于堆叠存储器和逻辑芯片。英伟达目前严重依赖台积电进行先进封装，因此与安靠合作可以分散供应链风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_%28semiconductors%29">Advanced packaging (semiconductors)</a></li>
<li><a href="https://semiengineering.com/knowledge_centers/packaging/advanced-packaging/heterogeneous-integration/">Heterogeneous Integration - Semiconductor Engineering</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI hardware`, `#advanced packaging`, `#supply chain`, `#semiconductors`

---

<a id="item-4"></a>
## [Ruff v0.16.0 默认规则从 59 条扩展至 413 条](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0 于 2026 年 7 月 23 日发布，将默认 lint 规则从 59 条大幅增加到 413 条，实现了无需额外配置的更严格的代码质量检查。 此次更新使 Ruff 无需任何配置就能更有效地捕获语法错误和运行时错误等严重问题，提升了整个 Python 生态系统的代码质量基线。同时也展现了 Astral 在被 OpenAI 收购后持续改进的决心。 自 v0.1.0 版本以来，Ruff 的总规则数已从 708 条增长至 968 条。更新后的工具能检测出诸如 datetime.now\(\) 缺少时区参数、盲目捕获异常以及无用的属性访问等问题。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的极速 Python linter 和代码格式化工具，比 Flake8 和 Black 等现有工具快 10-100 倍。它用单个二进制文件替代了多个 lint 工具，并在 Python 社区中得到广泛采用。v0.16.0 版本发布前，Astral 已于 2026 年被 OpenAI 收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/">Ruff</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>

</ul>
</details>

**标签**: `#ruff`, `#python`, `#linting`, `#tooling`, `#release`

---

<a id="item-5"></a>
## [韩国巨头将 AI 合作伙伴关系扩大至 9500 亿美元](https://www.koreatimes.co.kr/business/companies/20260726/samsung-sk-hyundai-expand-ai-partnerships-with-big-tech-firms-to-950-bil) ⭐️ 8.0/10

三星、SK 集团和现代汽车集团共同扩大了与大型科技公司的 AI 合作伙伴关系，承诺总投资额达到 9500 亿美元。 这一巨额投资凸显了韩国最大企业集团向人工智能的战略转型，可能将重塑全球 AI 格局，加速关键行业的创新。 9500 亿美元的数字代表了一段未明确时期内的累计投资，涵盖与谷歌、微软及可能包括英伟达等合作伙伴的合资企业、研发合作和基础设施建设。

gdelt · koreatimes.co.kr · 7月26日 07:30

**背景**: 韩国企业集团（即财阀）传统上主导制造业和电子业。随着人工智能成为变革性技术，这些公司正寻求通过与全球科技领导者合作，发挥其在半导体、电池和汽车领域的优势。这一承诺的规模标志着韩国在国家层面推动保持 AI 竞争力的努力。

**标签**: `#AI`, `#partnerships`, `#Samsung`, `#SK Group`, `#Hyundai`

---

<a id="item-6"></a>
## [英伟达等 25 家公司呼吁谨慎对待开放 AI 模型限制](https://business24.ro/inteligenta-artificiala/nvidia-companii-prudenta-restrictii-modele-inteligenta-deschidere-1661686) ⭐️ 8.0/10

英伟达与约 25 家其他公司公开敦促政策制定者在限制开源人工智能模型时保持谨慎，警告过于严格的监管可能会扼杀创新。 这一联合声明表明业界对潜在的开源 AI 模型监管的重大反对，突显了 AI 治理中创新与安全之间的关键紧张关系，可能影响未来政策走向。 这些公司倡导一种平衡的方法，既保留开源 AI 模型的好处（如透明度和可访问性），同时解决关于滥用的合理担忧，但未详细说明具体的监管提案。

gdelt · business24.ro · 7月26日 07:30

**背景**: 开源 AI 模型是根据开源许可证公开发布源代码的系统，允许任何人使用、修改和分发。这种开放性推动了 AI 的快速创新，但也引发了关于滥用的担忧，导致政府和安全倡导者呼吁进行监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence">Regulation of artificial intelligence - Wikipedia</a></li>
<li><a href="https://gdprlocal.com/ai-regulations-in-the-us/">AI Regulations in the US: What You Need to Know in 2025 - GDPR Local</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#regulation`, `#Nvidia`, `#policy`

---

<a id="item-7"></a>
## [Meta、微软、英伟达、IBM 等公司支持开放权重 AI](https://news.google.com/rss/articles/CBMipAFBVV95cUxOS0hQcXlIMVB5UFFwVXM1Y0pZQm5XOXBzUmNveTg4RjZCc2RNdjdOVFV4U2JDZWdrTTRuTVROZ3lodE5FRVpielNWTVUyaFJkQlhHLVZmSVBWc1BRUHhNS1dNUjNTZ1lCb0drYk9pQ2hLQUtIUXlQUUc4eDNGVGYxOVQ5S1JSaDF0Q3BKSFFncDBKYUZCVV9fTm1aZXd6bjZKanB2dg?oc=5) ⭐️ 8.0/10

包括 Meta、微软、英伟达和 IBM 在内的多家大型科技公司联合支持开放权重 AI 模型，标志着行业向更易获取的 AI 迈进。 这些关键参与者的联合可能加速开放权重模型的采用，促进创新和透明度，同时挑战封闭 AI 系统的统治地位。 开放权重模型公开其训练后的参数供下载，但与开源 AI 不同，它们通常不包含训练代码或数据，限制了完全可复现性。

google\_news · AI News · 7月26日 02:47

**背景**: 开放权重 AI 模型指公开发布其训练参数（权重和偏置）的神经网络模型。这不同于开源 AI，后者要求完全公开训练代码、数据和方法。理解这一区别对于把握透明度和控制权的程度至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open-Weights Model? | AI21</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#industry collaboration`, `#open-weight AI`

---

<a id="item-8"></a>
## [硅谷就限制中国 AI 研究人员出现分歧](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMGg1N0lvWXlpTm43VlhleE5IZmNpNDhTTWFZbzBnV1lUY1FCa212cl93ZkVtU00waTNFMnhib0RnaFl1MVBvZEpVbVVwUmlod1FMTV9Qazh4NjVVNThXTnZXN3U0RFBXU1Rwd3JLcjNPSjYxN0gzbzR0bkdUMmg4NElGRVVHZzdDSE5N?oc=5) ⭐️ 8.0/10

《纽约时报》报道称，硅谷对美国限制中国 AI 研究人员和人才的政策存在分歧，一方主张国家安全，另一方警告这会损害创新。 这场辩论凸显了国家安全关切与 AI 人才全球性之间的矛盾，可能重塑行业未来和竞争格局。 文章指出，科技公司希望人才自由流动，而政策制定者主张更严格控制，双方对影响尚未达成共识。

google\_news · The New York Times · 7月25日 20:07

**背景**: 在中美 AI 战略竞争加剧的背景下，美国对中国科技公司和研究人员实施了多项限制。硅谷历史上受益于中国人才，但近期政策引发了关于人才流失和创新放缓的担忧。

**标签**: `#AI`, `#Geopolitics`, `#Policy`, `#Silicon Valley`, `#China`

---

<a id="item-9"></a>
## [菲尔兹奖得主加入 OpenAI 研究 AI 安全](https://www.aibase.com/news/29878) ⭐️ 8.0/10

菲尔兹奖得主雅各布·齐默尔曼宣布加入 OpenAI，专注于 AI 安全研究，从纯数学领域转向。 此举凸显了 AI 安全日益增长的重要性，以及 OpenAI 吸引顶尖数学人才解决领域关键挑战的决心。 齐默尔曼在 2026 年国际数学家大会上获得菲尔兹奖，表彰他证明了 o-minimality（模型论分支）中的一个核心猜想，该理论在数论和丢番图几何中有应用。

aibase · AIbase · 7月25日 09:09

**背景**: 菲尔兹奖是数学界最高荣誉，每四年颁发给 40 岁以下的数学家。O-minimality 是模型论中的一个概念，用于研究实几何中的温和结构，已被用于推动数论中如 André-Oort 猜想等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://people.maths.ox.ac.uk/pila/ODG.pdf">O-minimality and Diophantine geometry Jonathan Pila Abstract.</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#Fields Medal`, `#mathematics`, `#talent acquisition`

---

<a id="item-10"></a>
## [腾讯合并多模态与大语言模型部门为基座模型部](https://www.aibase.com/news/29871) ⭐️ 8.0/10

2024 年 7 月 23 日，腾讯将元多模态模型部与大语言模型部合并为基座模型部，由首席 AI 科学家姚顺宇领导。 此次合并标志着腾讯对开发统一全模态 AI 模型的战略承诺，有望加速在无缝融合文本、图像、视频和音频的模型方面取得突破。 合并旨在提升研发效率，并达到全模态模型的智能上限。姚顺宇已于 2023 年 12 月负责大语言模型团队，现在统筹双方。

aibase · AIbase · 7月25日 09:09

**背景**: 多模态 AI 将多种数据类型（文本、图像、视频、音频）整合到单个模型中以实现更丰富的理解。腾讯的混元系列是一系列多模态和大语言模型，已深度集成到微信、QQ 等产品中。“全模态”将多模态扩展到涵盖所有可能的数据类型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chozan.co/hunyuan-ai/">Hunyuan AI: Tencent’s Multimodal Models and How to Evaluate - ChoZan</a></li>
<li><a href="https://eu.36kr.com/en/p/3303284805523970">Tencent Hunyuan Updates: Focusing on Both Multimodality and Intelligent Agents - The Frontline</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#multimodal AI`, `#large language models`, `#organizational change`, `#AI strategy`

---