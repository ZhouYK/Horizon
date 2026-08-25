---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25 23:35:50 +0000
lang: zh
report: default
---

> 从 285 条内容中筛选出 11 条重要资讯。

---

1. [英伟达 Vera Rubin NVL72 首测：DeepSeek 吞吐提升 30 倍、成本降 35 倍](#item-1) ⭐️ 9.0/10
2. [OpenAI 自研芯片 Jalapeño 早期基准测试超越英伟达 GB300](#item-2) ⭐️ 9.0/10
3. [SpaceX 计划 2027 年将英伟达 Vera Rubin NVL72 送入太空](#item-3) ⭐️ 8.0/10
4. [苹果发布 M6 与 M5 Ultra：2 纳米制程与四芯片架构](#item-4) ⭐️ 8.0/10
5. [AI 设计的定制 CPU 在《Turing Complete》中成功运行《毁灭战士》](#item-5) ⭐️ 8.0/10
6. [Anthropic 预估潜在收入超 30 万亿美元，超过 SpaceX 纪录](#item-6) ⭐️ 8.0/10
7. [微软泄露的实验系统 Project Aion 曝光：无桌面图标，Copilot 包办一切](#item-7) ⭐️ 6.0/10
8. [Linux 迎来发布 35 周年](#item-8) ⭐️ 6.0/10
9. [宇树科技股价较首日高点回撤 45%，市值蒸发 2008 亿元](#item-9) ⭐️ 6.0/10
10. [Qwen 预告 Qwen3.8-Flash-Next 开源，基于 Qwen4 架构](#item-10) ⭐️ 6.0/10
11. [英伟达发布 Jetson Orin Nano 2 边缘模块，推理翻倍、功耗降 40%](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [英伟达 Vera Rubin NVL72 首测：DeepSeek 吞吐提升 30 倍、成本降 35 倍](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) ⭐️ 9.0/10

英伟达首次公布下一代机柜级系统 Vera Rubin NVL72 的实测数据：在智能体编码任务中运行 DeepSeek-V4-Pro，每兆瓦吞吐量较 GB300 最高提升 30 倍，每百万 Token 成本最高下降 35 倍。同期还宣布推理加速芯片 Groq 3 LPX 进入量产，并发布面向 AI 智能体的 Vera CPU。 这标志着 AI 推理经济性的重大飞跃，大幅降低智能体 AI 工作负载的成本和能耗，可能加速 AI Agent 的普及。同时，英伟达通过专用推理加速器和 CPU 扩展产品线，加剧了 AI 硬件领域的竞争。 Vera Rubin NVL72 在一个液冷机柜内整合 72 颗 Rubin GPU 和 36 颗 Vera CPU，通过 NVLink 6 互联。Groq 3 LPX 在运行 Gemma 4 31B 时创下单用户每秒 3400 输出 Token 的纪录，单个机柜级部署最多可链接 256 个 LP30 加速器。SpaceXAI 也宣布部署 Vera CPU，并计划 2028 年将优化版机柜送入太空。

telegram · zaihuapd · 8月25日 14:48

**背景**: 机柜级系统（如 GB200 NVL72 和 Vera Rubin NVL72）代表了从独立 GPU 向紧密协同设计、液冷超算的转变。智能体 AI（AI 模型自主执行编码等任务）非常依赖推理效率，因为智能体在单个请求中往往需要多次顺序调用模型。英伟达新推出的“LPX”产品线针对这种交互式推理场景，而 Vera CPU 则专为低功耗处理智能体编排任务而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/">NVIDIA Advances Vera Rubin Inference With New LPX ... | NVIDIA Blog</a></li>
<li><a href="https://siliconangle.com/2026/08/24/nvidias-dedicated-inference-accelerator-groq-3-lpx-enters-full-production-to-supercharge-ai-agents/">Nvidia&#x27;s dedicated inference accelerator Groq 3 LPX ... - SiliconANGLE</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Vera Rubin`, `#AI inference`, `#hardware`, `#DeepSeek`

---

<a id="item-2"></a>
## [OpenAI 自研芯片 Jalapeño 早期基准测试超越英伟达 GB300](https://openai.com/index/jalapeno-first-results/) ⭐️ 9.0/10

OpenAI 公布了其自研推理芯片 Jalapeño 的首批基准测试结果：在三个大语言模型上，其能效比英伟达 GB300 高 1.5 至 1.9 倍，延迟低 1.7 至 3.6 倍。该芯片计划于今年年底前部署在 OpenAI 自有的数据中心中。 这是 OpenAI 降低对英伟达依赖、自主掌控 AI 基础设施的重要里程碑，可能重塑 AI 硬件竞争格局。尤其值得注意的是，对比对象 GB300 是英伟达当前的旗舰推理平台，而非老产品。 该芯片由 OpenAI 与博通合作开发，是专为大语言模型推理而设计的 ASIC，不用于训练。其额定功耗为 700 瓦，实测持续功耗不高于 550 瓦；基准测试覆盖 GPT-OSS 120B、DeepSeek R1 670B 和 Kimi K2.5 1T 三个模型，但未与英伟达刚开始出货的 Vera Rubin 进行比较。

telegram · zaihuapd · 8月25日 16:08

**背景**: Jalapeño 是 OpenAI 与博通合作设计的定制推理芯片，据称借助 AI 辅助设计在九个月内完成开发。OpenAI 表示该芯片能为现代模型提供更高吞吐量和更低延迟，第二代芯片已进入深入开发阶段，第三代正在设计。英伟达 GB300 基于 Blackwell Ultra 架构，而 Vera Rubin 是英伟达面向智能体 AI 和推理工作负载的下一代平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/jalapeno-first-results/">Jalapeño’s first results show industry-leading speed and efficiency in AI inference | OpenAI</a></li>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks">OpenAI’s 700W Jalapeño ASIC outpaces 1,400W Nvidia flagship GPU...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#custom silicon`, `#AI hardware`, `#inference`, `#Nvidia`

---

<a id="item-3"></a>
## [SpaceX 计划 2027 年将英伟达 Vera Rubin NVL72 送入太空](https://www.theregister.com/off-prem/2026/08/25/spacex-claims-it-will-put-a-vera-rubin-nvl72-rack-scale-system-into-orbit-next-year/5292067) ⭐️ 8.0/10

SpaceX 计划于 2027 年将一套英伟达 Vera Rubin NVL72 机架级 AI 系统送入轨道，以验证太空 AI 计算能力。该系统包含 72 颗 Rubin GPU 和 36 颗 Vera CPU，功耗超过 100 千瓦。 这将是迄今为止在轨道上运行完整机架级 AI 超算的最雄心勃勃的尝试之一，有望推动轨道数据中心愿景的发展。如果成功，它可为卫星自主运行、对地观测和深空任务提供在轨 AI 推理能力，减少对将数据回传地球的依赖。 Vera Rubin NVL72 在地面通常需要液冷和大型供电设施，因此 SpaceX 必须解决太空中的供电、散热、辐射防护和通信问题。该公司尚未公布具体发射时间、目标轨道高度，以及系统在轨供电和冷却方案。

telegram · zaihuapd · 8月25日 08:03

**背景**: 机架级 AI 系统通过 NVLink 等互连技术将多颗 GPU 和 CPU 集成在一个液冷机架中，以提供强大的 AI 算力。天基数据中心是一种被提出的概念，计划将 AI 基础设施部署在太阳同步轨道上，利用天基太阳能供电；已有 Starcloud 等公司在轨道上使用 Nvidia H100 训练大语言模型。SpaceX 的计划是 Google、SpaceX 和中国都在参与的轨道数据中心探索竞赛的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space-based_data_center">Space-based data center - Wikipedia</a></li>
<li><a href="https://introl.com/blog/orbital-data-centers-space-ai-infrastructure-guide-2025">Orbital Data Centers | Introl Blog</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#NVIDIA`, `#AI`, `#Space Computing`, `#Orbital Data Center`

---

<a id="item-4"></a>
## [苹果发布 M6 与 M5 Ultra：2 纳米制程与四芯片架构](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 8.0/10

苹果发布了 M6 与 M5 Ultra 芯片，其中 M6 是苹果首款 2 纳米芯片，M5 Ultra 采用四芯片架构。M6 搭载于新款 Mac mini，而 M5 Ultra 则用于新款 Mac Studio，最高配备 36 核 CPU 和 80 核 GPU。 这一发布标志着 Apple Silicon 在性能和 AI 算力上的重大飞跃，M5 Ultra 的四芯片架构和 2 纳米制程为高性能计算树立了新标杆。它将深刻影响从事 AI/ML 工作负载的开发者和研究人员，同时新款 Mac mini 和 Mac Studio 以有竞争力的价格提供了前所未有的性能。 M6 配备 12 核 CPU、12 核 GPU、双 16 核神经网络引擎，统一内存带宽最高 170GB/s。M5 Ultra 最高支持 512GB 内存，统一内存带宽达 1.2TB/s，比 M3 Ultra 高 50%，其中 512GB 内存配置将于 10 月末推出。

telegram · zaihuapd · 8月25日 13:06

**背景**: 苹果 M 系列芯片由苹果自主设计，并由台积电代工。M6 是苹果首款采用 2 纳米制程的芯片，该制程使用全环绕栅极（GAA）纳米片晶体管，以提升性能和能效。M5 Ultra 采用四芯片设计，通过苹果的 UltraFusion 互连技术将两颗 M5 Max 芯片组合在一起，从而实现最高 36 核 CPU 和 80 核 GPU。神经网络引擎自 A11 Bionic 起引入，是苹果用于加速 AI 和机器学习任务的专用 NPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm">2nm Technology - Taiwan Semiconductor Manufacturing Company Limited</a></li>
<li><a href="https://www.pcmag.com/news/apple-m5-ultra-and-m6-silicon-explained">Apple M5 Ultra and M6 Silicon Explained: 2nm Tech, Quad-Die Chips Promise Macs Massive AI Muscle | PCMag</a></li>

</ul>
</details>

**标签**: `#Apple Silicon`, `#M6`, `#M5 Ultra`, `#2nm`, `#Hardware`

---

<a id="item-5"></a>
## [AI 设计的定制 CPU 在《Turing Complete》中成功运行《毁灭战士》](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coder-gets-doom-running-on-a-custom-cpu-designed-by-gpt-5-6-sol-game-viewport-is-overlaid-on-a-pulsing-schematic-of-the-cpu-in-turing-completes-sandbox-environment) ⭐️ 8.0/10

一位 AI 爱好者展示了 GPT-5.6 Sol 模型在《Turing Complete》沙盒中从逻辑门设计出定制 CPU“Codex-R32”，并成功启动《毁灭战士》\(1993\)。游戏通过 PureDOOM 的 C 语言移植版编译为 RV32IM 机器码，直接在模拟硬件上运行。 这标志着 AI 在端到端硬件设计（从门级逻辑到运行真实应用）方面的一个重要里程碑。它预示着 AI 辅助芯片设计的未来，但该成果更多是概念验证，而非可投入生产的方法。 这款名为 Codex-R32 的 CPU 是在游戏沙盒模式中用基础逻辑元件搭建的，游戏画面被叠加在处理器的实时门级电路示意图上。当被调侃“下一步跑《孤岛危机》”时，AI 回应说需要一块 GPU、几 GB 内存，以及一张从太空可见的电路图。

telegram · zaihuapd · 8月25日 15:23

**背景**: 《Turing Complete》是一款教育解谜游戏，玩家需要从 NAND 门开始逐步搭建计算机直至汇编语言，类似 nand2tetris 课程。RV32IM 是 32 位 RISC-V 指令集架构，包含基础整数指令以及整数乘除指令。PureDOOM 是一个单文件、无依赖的《DOOM》源码移植版，设计目标是在几乎所有设备上运行，因此常用于各种“把 Doom 跑在奇怪设备上”的尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://turingcomplete.game/">Turing Complete</a></li>
<li><a href="https://github.com/Daivuk/PureDOOM">GitHub - Daivuk/PureDOOM: Pure DOOM - Single Header Doom Source Port · GitHub</a></li>
<li><a href="https://arxiv.org/pdf/2010.16171">RVCoreP- 32 IM : An effective architecture to</a></li>

</ul>
</details>

**社区讨论**: 社区反应主要是带点玩笑的惊叹：观众调侃“下一步跑《孤岛危机》”，AI 也用同样轻松的语气回应，说那需要一块 GPU、额外内存和一张巨大的电路图。这段对话既体现了这类演示的趣味性，也反映了 DIY 演示与现代游戏硬件之间的实际差距。

**标签**: `#AI`, `#CPU Design`, `#GPT-5.6`, `#Doom`, `#Turing Complete`

---

<a id="item-6"></a>
## [Anthropic 预估潜在收入超 30 万亿美元，超过 SpaceX 纪录](https://www.wsj.com/tech/ai/anthropic-expected-to-tell-investors-it-sees-over-30-trillion-in-potential-revenue-a611efea) ⭐️ 8.0/10

开发 Claude AI 模型的 Anthropic 据称打算告诉投资者，其潜在收入机会超过 30 万亿美元，超过了 SpaceX 创纪录的 28.5 万亿美元估算。该消息由《华尔街日报》援引知情人士报道。 这一惊人的预估表明市场对人工智能抱有巨大期望，并可能影响 AI 投资趋势。如果实现，这将使 Anthropic 成为估值最高的私营公司之一，并重塑 AI 竞争格局。 30 万亿美元的数字指的是&\#x27;潜在收入机会&\#x27;，这是一种非标准的远期指标，而非实际或近期预测的收入。SpaceX 此前在 IPO 前以 28.5 万亿美元的估算测试了这一指标的极限。

telegram · zaihuapd · 8月25日 17:32

**背景**: Claude 是 Anthropic 开发的一系列大型语言模型，于 2023 年 3 月作为 AI 聊天机器人推出。Anthropic 是与 OpenAI 竞争的主要 AI 公司之一，其收入预测反映了围绕生成式 AI 的更广泛炒作。该报道的估算基于匿名消息来源，尚未得到 Anthropic 公开确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude (AI)</a></li>
<li><a href="https://grokipedia.com/page/Claude_language_model">Claude (language model)</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI`, `#Finance`, `#Revenue`, `#Market`

---

<a id="item-7"></a>
## [微软泄露的实验系统 Project Aion 曝光：无桌面图标，Copilot 包办一切](https://www.windowslatest.com/2026/08/24/microsofts-leaked-new-os-is-one-youll-hope-stays-buried-and-its-not-windows/) ⭐️ 6.0/10

泄露文档披露了微软 2024 年研发的实验操作系统 Project Aion（又称 Copilot OS）：它以 Copilot 为核心，没有开始菜单和桌面图标。该系统基于定制版 Edge 浏览器和精简版 Windows 内核 Win3，不支持 Win32 应用，并需依赖 Windows 365 云电脑提供完整功能。 这次泄露让人们难得一窥微软对「AI 优先、以智能体为核心」操作系统的长远构想，未来可能重塑 Windows 的运作方式。即便 Project Aion 最终不会发布，它也指明了 Copilot 跨设备整合的方向，并解释了微软为何正逐步移除 Windows 11 的部分 Copilot 功能。 泄露文档称 Project Aion 被定位为跨设备「智能体 OS」，同时支持 AOSP（Android 开源项目）与 Windows 11，每段对话可生成独立的窗口和图标。微软目前正在移除 Windows 11 的部分 Copilot 功能，因此该项目大概率不会发布。

telegram · zaihuapd · 8月25日 03:41

**背景**: Win32 是大多数传统 Windows 桌面程序所依赖的经典应用程序接口，不支持 Win32 应用意味着该系统无法兼容现有绝大多数 Windows 软件。Windows 365 是微软的云电脑服务，可将完整的 Windows 桌面从云端流式传输到任何设备，并于 2021 年 8 月正式全面上市。AOSP 即 Android 开源项目，是 Android 系统的开放源代码基础，这意味着该项目理论上可同时运行 Android 应用与 Windows 11。综合来看，Project Aion 更像是一个依赖云端、由 Copilot 驱动的早期操作系统概念，而非 Windows 的传统继任者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ultima.com/blog/making-pcs-cloudy-with-windows-365/">Making PCs Cloudy with Windows 365</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Windows_library_files">Microsoft Windows library files - Wikipedia</a></li>
<li><a href="https://source.android.com/">Android Open Source Project</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Copilot`, `#Windows`, `#OS leak`, `#experimental`

---

<a id="item-8"></a>
## [Linux 迎来发布 35 周年](https://9to5linux.com/happy-35th-birthday-linux) ⭐️ 6.0/10

8 月 25 日，9to5Linux 发布了一篇纪念文章，庆祝 Linux 发布 35 周年。这篇文章回顾了这一开源软件历史上的重要里程碑，但并未包含新的技术内容。 Linux 支撑着现代基础设施的很大一部分，从服务器、超级计算机到 Android 设备。这一周年纪念凸显了一个自由共享的内核如何成为数字世界的基石，并成为协作开发的持久象征。 这一天标志着 1991 年 8 月 25 日林纳斯·托瓦兹首次宣布他的内核项目。最初只是个人爱好，Linux 此后通过全球数千名开发者的贡献不断演进。

telegram · zaihuapd · 8月25日 07:29

**背景**: Linux 是一个类 Unix 操作系统内核，由托瓦兹创建，旨在提供專有系统的免费替代品。与 GNU 工具结合后，它便构成完整的操作系统，其开源许可允许任何人查看、修改和重新分发代码。这一周年纪念被开源社区广泛视为对历史上最有影响力的软件项目之一的庆祝。

**标签**: `#Linux`, `#anniversary`, `#open source`, `#history`, `#milestone`

---

<a id="item-9"></a>
## [宇树科技股价较首日高点回撤 45%，市值蒸发 2008 亿元](https://www.reuters.com/business/finance/china-robot-maker-unitrees-post-listing-slump-sparks-bubble-fears-2026-08-25/) ⭐️ 6.0/10

宇树科技股价在科创板首日大涨 629.44%后，连续三日下跌，较首日高点回撤约 45%，市值蒸发约 2008 亿元。创始人王兴兴在 2026 世界机器人大会上表示，具身智能的‘ChatGPT 时刻’预计还需 2-3 年到 5-10 年才会到来。 这一大幅回调引发了对中国人形机器人行业泡沫风险及高位买入散户亏损的担忧。创始人对具身智能时间线的坦诚表态，也为这一全球 AI 竞赛关键前沿领域降温预期。 宇树科技上市首日开盘价 1100 元，大涨 629.44%，总市值达 4449 亿元，随后连续三日下跌。分析人士认为下跌源于市场情绪过热和估值过高，而整个行业仍普遍面临泛化能力不足的挑战。

telegram · zaihuapd · 8月25日 12:38

**背景**: 具身智能是指将 AI 融入物理系统（如人形机器人、自动驾驶汽车），使其通过真实世界交互而非仅靠数据来感知、行动和学习。泛化能力是 AI 模型处理训练数据之外的新情况的能力，目前仍是机器人领域的关键技术瓶颈。王兴兴的估计表明，该领域可能需要数年研究，才能迎来类似大语言模型 ChatGPT 那样的突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">Embodied AI: What Is It and How to Build It?</a></li>
<li><a href="https://www.sciencedirect.com/topics/computer-science/generalization-ability">sciencedirect.com/topics/computer-science/ generalization - ability</a></li>

</ul>
</details>

**标签**: `#Unitree`, `#humanoid robots`, `#embodied AI`, `#IPO`, `#market sentiment`

---

<a id="item-10"></a>
## [Qwen 预告 Qwen3.8-Flash-Next 开源，基于 Qwen4 架构](https://www.modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) ⭐️ 6.0/10

Qwen 在魔搭社区上线了 Qwen3.8-Flash-Next 的预告页，这是一款基于下一代 Qwen4 架构的多模态 MoE 模型，并宣布将于 2026 年 8 月 26 日 23 时（UTC+8）开放下载，提供标准版和 FP8 两个版本。 这是 Qwen4 架构的首次公开亮相，让社区能在完整 Qwen4 系列发布前提前适配工具和工作流。同时，它延续了开源前沿模型的趋势，可能促使其他实验室公开更多架构细节。 该模型为多模态 MoE 设计，将发布标准精度和 FP8 量化两个检查点。不过，官方页面除架构说明外，提供的技术细节很少。

telegram · zaihuapd · 8月25日 12:59

**背景**: Qwen 是阿里巴巴的开源大语言模型系列，Qwen3.8-Flash-Next 定位为预览下一代 Qwen4 架构的“Flash”变体。MoE 模型使用多个专家子网络，将 token 路由到最相关的专家，从而在不按比例增加算力的情况下提升容量。FP8 是一种低精度浮点格式，能降低显存和延迟，但可能带来数值不稳定。提前开源该模型，似乎是希望开发者能在 Qwen4 正式到来前提前构建工具和微调生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=EM08mb4sqQs">Qwen 4 Is Coming! Qwen3.8 MoE Reveals the Next Architecture</a></li>
<li><a href="https://medium.com/ramses-engineering/not-one-brain-but-many-how-mixture-of-experts-moe-makes-ai-smarter-and-faster-568f41220852">Not One Brain, But Many: How Mixture of Experts ( MoE )... | Medium</a></li>
<li><a href="https://www.secureagi.org/posts/deep-seek-v3-training">DeepSeek V3 Deep Dive: Training Methodologies and Their Impact</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Qwen`, `#open-source`, `#model architecture`

---

<a id="item-11"></a>
## [英伟达发布 Jetson Orin Nano 2 边缘模块，推理翻倍、功耗降 40%](https://www.therobotreport.com/jetson-orin-nano-2-doubles-inference-performance-robotics-edge-says-nvidia/) ⭐️ 6.0/10

英伟达于 8 月 25 日发布入门级边缘 AI 计算机 Jetson Orin Nano 2，算力达 78 TOPS，内存 8 GB。与上一代 Orin Nano Super 相比，推理性能翻倍，同性能下功耗降低 40%，模块与开发套件将于 2027 年上半年上市。 此举进一步强化了英伟达在机器人与边缘 AI 计算领域的产品线，让 Cosmos、Qwen 3 等大模型能在边缘侧以更低功耗实时运行。对于使用其机器人技术栈的 300 多万开发者，以及正在评估或采用该产品的 Wing、Matic 等企业来说，意味着更高效、更省电的边缘推理方案。 关键参数是 78 TOPS 算力和 8 GB 内存，推理性能相对 Orin Nano Super 翻倍，同性能下功耗降低 40%。需要注意的是，TOPS 只是理论峰值指标，实际推理吞吐还取决于内存带宽、软件栈、散热条件以及具体负载。

telegram · zaihuapd · 8月25日 16:54

**背景**: 边缘 AI 计算机是指在机器人等设备本地运行神经网络推理的硬件，无需将数据发送到云端。TOPS（每秒万亿次操作）是常见的性能指标，但实际推理速度受架构、内存、软件栈、功耗和散热等整个系统影响。Nvidia Cosmos 是英伟达面向物理 AI 的生成式世界基础模型平台，Qwen 3 则是阿里巴巴推出的新一代大语言模型系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://semiengineering.com/one-more-time-tops-do-not-predict-inference-throughput/">One More Time: TOPS Do Not Predict Inference Throughput</a></li>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://ollama.com/library/qwen3">qwen 3</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Edge AI`, `#Hardware`, `#Jetson`, `#Robotics`

---