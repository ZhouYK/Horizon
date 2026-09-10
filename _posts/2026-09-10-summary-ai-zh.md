---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10 23:05:38 +0000
lang: zh
report: ai
---

> 从 280 条内容中筛选出 10 条重要资讯。

---

1. [Shopify 弃用 React Native，转向 Swift 与 Kotlin 原生开发，理由是 AI 智能体](#item-1) ⭐️ 8.0/10
2. [Calif Research 称 AI 两日内造出微信通话零点击蠕虫](#item-2) ⭐️ 8.0/10
3. [Anthropic 称已阻止可能助力生物武器的 AI 滥用行为](#item-3) ⭐️ 8.0/10
4. [加州颁布多项 AI 安全法案，获 OpenAI 与 Anthropic 罕见公开支持](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4.1 Flash 正式发布：552B MoE 架构全面超越 V4 Pro](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4.1 Flash 发布：552B MoE 多模态模型性能超越 Pro 版且价格更低](#item-6) ⭐️ 8.0/10
7. [Anthropic 称已拦截可能助长生物武器的 AI 滥用行为](#item-7) ⭐️ 7.0/10
8. [五角大楼洽谈向 AI 云初创公司 Fluidstack 提供 50 亿美元贷款](#item-8) ⭐️ 7.0/10
9. [Anthropic 称已阻止利用其 AI 开发生物武器的企图](#item-9) ⭐️ 7.0/10
10. [OpenAI 转变立场，呼吁制定全国性 AI 安全规则](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Shopify 弃用 React Native，转向 Swift 与 Kotlin 原生开发，理由是 AI 智能体](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify 宣布其移动应用将放弃 React Native，重新回到两套独立的原生代码库：iOS 使用 Swift，Android 使用 Kotlin，从而推翻了该公司 2020 年做出的跨平台决策。Shopify 在工程博客中表示，原生开发依然意味着要在两个平台上构建和维护软件，但 AI 编码智能体现在已经能够承担足够多的实现、翻译、测试和审查工作，因此重复劳动不再是决定性因素。 此举对“跨平台框架是节省工程投入的默认方案”这一主流假设构成了明显的反向信号；如果 AI 智能体确实能够消化维护两套代码库的成本，其他大公司可能也会重新考虑原生开发。由于 Shopify 一直是 React Native 生态的重要开源贡献者，这一决定还会对该生态产生直接影响。 Shopify 维护着三个重要的 React Native 库，这次迁移并不会让它们全部保持原样：react-native-skia 和 flash-list 正在移交给新的维护者，而 restyle 将于 2026 年底归档，原因是其用户规模小于公司其他库。Shopify 的文章对 React Native 给予了充分肯定，称其在长达六年的时间里是一个优秀的平台，并把此次转向描述为成本权衡的结果，而非对该框架质量的否定。

rss · Simon Willison · 9月10日 21:11

**背景**: React Native 是 Meta 推出的跨平台框架，开发者可以用共享的 JavaScript 或 TypeScript 代码在 iOS 和 Android 上驱动原生界面，这也是它长期以来被视为“不必把同一功能做两遍”的方案的原因。Swift 和 Kotlin 分别是 iOS 与 Android 的现代官方语言，能更紧密地调用平台 API，但需要各自独立的实现。AI 编码智能体是基于大语言模型的工具，能够跨多个文件自主编写、修改、调试和重构代码，规划多步骤的改动，而不仅仅是补全单行代码——这正是 Shopify 所称改变其权衡结果的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_coding_agent">AI coding agent</a></li>

</ul>
</details>

**标签**: `#mobile-development`, `#react-native`, `#ai-agents`, `#engineering-strategy`, `#swift-kotlin`

---

<a id="item-2"></a>
## [Calif Research 称 AI 两日内造出微信通话零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 8.0/10

Calif Research 发布了 WeWorm 的演示，称其为首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫，受害者完全无需接听电话或触碰手机。该团队表示，借助 AI 协作，他们在大约两天内找到了漏洞并写出首个远程代码执行（RCE）利用程序，随后又用约一周时间完成了蠕虫的构建。 如果这一说法成立，说明 AI 已将过去需要较大团队耗时数月完成的漏洞利用开发压缩到几天之内，从而大幅降低了对拥有十亿级用户的即时通讯平台发起自我传播式攻击的门槛。这会影响微信用户、被迫迅速修补漏洞的移动平台厂商，以及关于 AI 如何加速攻击性安全研究的更广泛讨论。 这只是一份自行发布的简短声明与演示，而非经过同行评审的技术报告，因此没有 CVE 编号、腾讯方面的厂商确认或补丁状态可供核实。原文还强调，如此规模的蠕虫过去需要更大团队耗费数月，如今人类的角色主要限于判断攻击目标以及如何安全地进行测试。

rss · Simon Willison · 9月10日 00:56

**背景**: 蠕虫是一种能够在系统之间自动自我复制的恶意软件，而“零点击”意味着受害者无需打开文件、点击链接，甚至无需接听电话，攻击就能得手。远程代码执行（RCE）指攻击者可经由网络在目标机器上运行任意代码的漏洞，被公认为最严重的一类安全缺陷。微信是腾讯在中国占主导地位的即时通讯应用，WeWorm 被描述为首个通过其通话功能在两大主流移动平台上传播的蠕虫。借助大语言模型进行逆向工程、模糊测试与漏洞利用编写的“AI 辅助漏洞利用开发”是一种新兴实践，此前的相关研究（例如针对生成式 AI 应用的 Morris II 零点击蠕虫）也曾对此进行探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Remote_code_execution">Remote code execution</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lwa1BUNUVSSEZTVFA0eDdRSktDZ0FQAQ?hl=en-US&amp;gl=US&amp;ceid=US:en">Google News - WeChat worm - Overview</a></li>
<li><a href="https://noirfate.github.io/assets/pdf/llm_paper/Unleashing+Zero-click+Worms+that+Target+GenAI-Powered+Applications.pdf">ComPromptMized: Unleashing Zero - click Worms that</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI-assisted exploitation`, `#zero-click worm`, `#WeChat`, `#remote code execution`

---

<a id="item-3"></a>
## [Anthropic 称已阻止可能助力生物武器的 AI 滥用行为](https://www.sandiegouniontribune.com/2026/09/10/anthropic-threat-report/) ⭐️ 8.0/10

Anthropic 在一份公司威胁报告中披露，其检测并阻止了可能被用于支持生物武器开发的 AI 滥用行为。该消息于 9 月 10 日被报道，这是大型模型厂商不仅发出理论性警告、而且实际拦截有害用途尝试的一个具体案例。 这表明前沿 AI 实验室正日益成为生物安全的第一道过滤器：在有人试图获取危险生物学知识时，模型厂商往往是最先观察到的一方。这类披露会影响围绕 AI 安全监管、模型访问权限管控以及政府 AI 安全研究机构角色的更广泛讨论。 相关信息来自 Anthropic 自家的威胁报告，因此属于企业自行披露，尚未经外部生物安全或政府专家的独立核实。Anthropic 的使用政策禁止利用其模型开发武器，而执行主要依赖自动化检测与人工对滥用信号的复核。

gdelt · sandiegouniontribune.com · 9月10日 22:30

**背景**: AI 安全是一个跨学科领域，旨在防止 AI 系统引发事故、被滥用或其他有害后果，其中包括对模型危险能力的监测。生物安全指防止有害生物制剂被故意或意外释放的相关措施，涵盖生物恐怖主义与大流行病威胁。威胁情报本是网络安全领域的实践，指收集和分析攻击者的行为与意图以便主动应对；如今 AI 实验室也采用类似的报告方式，说明其模型被滥用的情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biosecurity">Biosecurity</a></li>
<li><a href="https://en.wikipedia.org/wiki/Threat_intelligence">Threat intelligence</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#biosecurity`, `#Anthropic`, `#threat intelligence`, `#misuse prevention`

---

<a id="item-4"></a>
## [加州颁布多项 AI 安全法案，获 OpenAI 与 Anthropic 罕见公开支持](https://www.aibase.com/news/30960) ⭐️ 8.0/10

加州州长纽森签署了一系列人工智能监管法案，要求前沿大模型加强安全风险评估、透明度披露，并防范灾难性网络攻击。参数规模达到万亿级的模型在发布前必须完成红队演练和第三方审计，而该立法罕见地获得了 OpenAI、Anthropic 等硅谷头部 AI 公司的公开支持。 这是首批对前沿模型施加具体发布前义务的州级监管制度之一，而头部实验室的背书表明，领先开发者可能更倾向于可预期的合规规则，而非零散拼凑的临时限制。这些要求有可能成为事实上的全国标准，影响 AI 安全合规、审计与红队实践在全行业乃至加州以外的推广方式。 最严格义务的门槛设定在万亿参数规模，这意味着目前最重的红队演练与第三方审计要求仅适用于少数最大的前沿模型（例如蚂蚁集团开源的 Ling-1T），而不覆盖大多数商用部署的系统。审计旨在核实模型是否按预期运行、是否引入非法偏见，同时核查数据来源、模型设计以及是否符合相关法律。

aibase · AIbase · 9月10日 16:01

**背景**: 红队演练是一种结构化的对抗性测试流程，由专家主动探测系统，在真正的攻击者之前发现弱点和安全失效；在生成式 AI 中，它不仅覆盖技术缺陷，还涉及伦理、社会和安全风险。第三方审计则是独立审查，用于核实 AI 系统是否按预期运行、检查其数据来源与设计，并确认是否合规。参数量大致对应神经网络中学习到的权重数量，通常被用作模型规模与能力的粗略指标。在美国缺乏全面联邦规则的背景下，加州已成为 AI 立法的主要试验场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aisecurityandsafety.org/en/guides/ai-red-teaming/">AI Red Teaming: The Complete Guide to Testing AI Systems ...</a></li>
<li><a href="https://www.warden-ai.com/resources/third-party-ai-audit">What is a Third-Party AI Audit? A Simple Guide - Warden AI</a></li>
<li><a href="https://www.artificialintelligence-news.com/news/trillion-parameter-ai-model-ant-group-ling-1t/">Trillion - parameter AI model : Ant Group&#x27;s Ling-1T launch</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#AI safety`, `#California policy`, `#OpenAI`, `#Anthropic`

---

<a id="item-5"></a>
## [DeepSeek V4.1 Flash 正式发布：552B MoE 架构全面超越 V4 Pro](https://www.aibase.com/news/30957) ⭐️ 8.0/10

DeepSeek 正式发布 V4.1 Flash，这是一款拥有 552B 参数、采用全新非对称 Causal-Encoder-Decoder 架构的混合专家（MoE）模型，并原生支持多模态视觉。官方称其为新架构系列中体量最小的模型，但能力上全面超越此前的 V4 Pro，同时将 HBM 占用降至原来的四分之一。 这次发布说明前沿模型的竞争重心正从单纯的参数规模转向架构效率——更小的模型也能击败更大的前代产品。HBM 需求据称降至四分之一，这有望显著降低推理硬件成本，让大规模多模态部署对企业与云厂商都更可负担。 该模型采用稀疏激活机制：在 552B 总参数中，输入侧约激活 8B、输出侧约激活 16B，这正是其成本与显存节省的来源。不过「全面超越 V4 Pro」以及 HBM 降至四分之一等说法均来自官方发布说明，目前尚未有独立基准测试或第三方验证。

aibase · AIbase · 9月10日 14:01

**背景**: 混合专家（MoE）是一种把模型拆成许多专门化子网络（即「专家」）、每个 token 只路由到其中少数几个的架构，因此总参数量可以极大，而每个 token 的计算量却保持较低。HBM（高带宽内存）是 GPU 等 AI 加速器上使用的 3D 堆叠 DRAM，价格昂贵且供应紧张，因此降低推理对 HBM 的占用能直接压低部署成本。Causal-Encoder-Decoder 属于较少见的设计，它把处理输入的编码阶段与自左向右因果解码的生成阶段结合起来；DeepSeek 的版本被称为「非对称」，是因为两侧在规模和激活预算上并不相同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://architecturediagram.ai/blog/mixture-of-experts-architecture">Mixture of Experts ( MoE ) Architecture ... - ArchitectureDiagram.ai</a></li>
<li><a href="https://www.linkedin.com/learning/scaling-ai-models-with-mixture-of-experts-moe-design-principles-and-real-world-applications/intro-to-moe-architecture">Intro to MoE architecture - Scaling AI Models with Mixture of Experts ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#MoE`, `#AI model release`, `#multimodal`, `#efficiency`

---

<a id="item-6"></a>
## [DeepSeek V4.1 Flash 发布：552B MoE 多模态模型性能超越 Pro 版且价格更低](https://www.aibase.com/news/30955) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek V4.1 Flash，官方称其为自家最小的轻量级多模态模型，采用 552B 参数的混合专家（MoE）架构以及全新的因果编码器-解码器（Causal-Encoder-Decoder）设计。官方宣称 V4.1 Flash 的原生视觉理解能力已全面超越 Pro 版本，同时在能力上限、推理速度和吞吐量上均有提升，价格也有所下降，并且该设计有望扩展到更大规模的模型。 此次发布表明 DeepSeek 正在推出一条更便宜、更快的多模态产品线，并在视觉任务上超过自家旗舰模型，这可能在能力与价格两方面对多模态模型市场的竞争对手形成压力。若这些性能声明得到验证，它还将降低开发者构建视觉与智能体（Agent）应用的成本门槛。 该模型采用 552B 参数的 MoE 主干，意味着每个 token 只激活部分专家子网络，因此尽管总参数量庞大，推理成本仍然较低；据称因果编码器-解码器架构可将解码器的全局 KV 缓存直接投影出来，从而大幅降低缓存命中成本。DeepSeek 还将 V4.1 Flash 定位为可扩展的设计蓝图而非终点，预计同一设计会被应用到更大规模的模型上。

aibase · AIbase · 9月10日 14:01

**背景**: 混合专家（MoE）是一种机器学习技术，由多个专门的“专家”子网络划分问题空间，路由器为每个输入只选择少数几个专家，从而以一小部分算力获得超大模型的容量。传统的编码器-解码器模型先用编码器读取完整输入，再由解码器生成输出，这种结构在翻译和摘要任务上很强大，但规模化后成本高昂。DeepSeek 的改进在于采用因果型编码器-解码器变体，目标是削减缓存与推理成本，而这正是反复调用模型的智能体（Agent）工作负载最关心的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forkast.news/deepseeks-new-architecture-slashes-agentic-costs-by-80/">DeepSeek’s New Architecture Slashes Agentic Costs by 80%</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#multimodal AI`, `#MoE`, `#model release`, `#AI/ML`

---

<a id="item-7"></a>
## [Anthropic 称已拦截可能助长生物武器的 AI 滥用行为](https://www.twincities.com/2026/09/10/anthropic-threat-report/) ⭐️ 7.0/10

Anthropic 报告称，它检测并阻止了对其 AI 系统的滥用尝试，这些行为可能被用于支持生物武器的研发。该信息来自公司自身的威胁报告工作，其中表示相关活动已被识别并终止，而非任其继续。 这一披露是前沿 AI 实验室安全机制在真实滥用场景（而非假设的红队测试）中受到检验的具体案例，为对最强模型实施监控与访问控制的论点提供了支撑。它同时也直接影响当前关于生物安全，以及是否应对能力日益增强的模型加以门槛限制、审计或使用权限管控的政策讨论。 这份公开报告由实验室自行发布，属于摘要性质，因此涉及账号数量、具体模型版本以及尝试推进到何种程度等细节都较为有限，且未经独立核实。业界通常将此类被拦截的尝试描述为技术含量相对较低、单靠 AI 很难成功，因为制造生物武器还需要实验室设备、受管控的材料以及难以言传的实操经验，这些都不是聊天机器人能够提供的。

gdelt · twincities.com · 9月10日 22:30

**背景**: Anthropic 是一家以安全研究著称的 AI 公司，开发了 Claude 系列大语言模型；与其他前沿实验室一样，它设有威胁情报职能，用于监测模型的使用方式，并封禁违反使用政策的账号。这一领域的核心担忧是“能力提升”（uplift）：模型是否会通过提供原本需要专业训练才能掌握的知识，从而降低从事有害活动的门槛，而生物学正是典型的军民两用领域，因为同一套知识既支撑医学，也可能被用于武器化。由于能力评估与滥用情况报告目前仍以自愿、且主要由企业自行发布为主，这类披露是了解真实世界风险的重要但不完整的窗口。

**标签**: `#AI safety`, `#biosecurity`, `#Anthropic`, `#AI misuse`, `#policy`

---

<a id="item-8"></a>
## [五角大楼洽谈向 AI 云初创公司 Fluidstack 提供 50 亿美元贷款](https://news.google.com/rss/articles/CBMitwFBVV95cUxNQm56T2dLMnFMeVp3a0tJY2s1eVdLalpSQ2c4bXBGQ2dOclF3a0dCVjhDYldvcEJMbEQ5TUQ5RXJuZXllZ1FvR3phRVlGNHhBazR0LXlaTy1DQmdXUENkQ1hLcWZrZlh0Ni0zdVVhSEhNdGxSckNpbHpiMi1GbUM0aUhSOFluSkZ0aG9WVG9DZ0pzQm13d2ZjRG9hZEZrdFRYUTU3bHoyWmhVYjNXUFN4TGtZRGdXbmM?oc=5) ⭐️ 7.0/10

据路透社引用《华尔街日报》的报道，五角大楼正在洽谈向 AI 云初创公司 Fluidstack 提供约 50 亿美元的贷款。Fluidstack 是一家提供 GPU 算力的 AI 云服务商，目前相关谈判尚未敲定，具体条款和完成时间均未披露。 这笔交易若达成，将标志着美国政府以极为直接的方式为私营 AI 算力基础设施提供融资，模糊了国防采购与 AI 热潮中风险投资式投入之间的界限。在主权 AI 与国防级算力需求加速增长的背景下，它也将强化 Fluidstack 相对于大型云厂商的竞争地位。 报道中的 50 亿美元是仍在谈判中的贷款，而非已签署的承诺，《华尔街日报》也未说明还款条件、抵押安排或由五角大楼的哪个项目提供支持。此外，Fluidstack 此前被报道正以 180 亿美元估值融资约 10 亿美元，并公开将自己定位为 Anthropic 500 亿美元算力建设的主要部署方。

google\_news · Reuters · 9月10日 22:01

**背景**: Fluidstack 是一家 AI 云服务商，2017 年从牛津大学分拆成立，最初是一个把 AI 算力需求与闲置 GPU 资源对接的撮合市场，如今则对外出售用于模型训练和推理的大规模 GPU 算力。五角大楼即美国国防部总部，近年来持续扩大对商用 AI 与云服务的使用。政府向私营 AI 初创公司提供贷款是一种相对较新的机制，不同于普通的云服务采购合同，也反映出各国日益把 AI 算力视为战略性基础设施的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fluidstack.io/">Fluidstack</a></li>
<li><a href="https://www.royco.ai/companies/fluidstack">Fluidstack — Company Profile, Funding &amp; Valuation | Royco</a></li>

</ul>
</details>

**标签**: `#Pentagon`, `#AI infrastructure`, `#cloud computing`, `#defense funding`, `#Fluidstack`

---

<a id="item-9"></a>
## [Anthropic 称已阻止利用其 AI 开发生物武器的企图](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOb3RxODh4LWhOS0o0UFBGNUhHODA0Z2dqbTcyTlFmYVRwRzJVVnhKMFl4U2dqQUQwZXV6d0c1c0gwRHZXeF9wOFRTN2xCengtRnRuR0tJLUNDTlI3VjAyekRzRngwMWY4M01hSUVwWURFUFAxdkRjRC1HZUM3cG9YTnZ4UVFNcVlnT200?oc=5) ⭐️ 7.0/10

据《纽约时报》报道，Anthropic 表示其已发现并阻止了可能试图利用其 AI 系统协助开发生物武器的行为。该公司尚未公开具体的涉事用户、操作方式或威胁模型细节。 这是前沿 AI 实验室迄今最具体的公开披露之一——宣称已拦截借助 AI 构建生物武器的企图，这可能推动对更严格的生物安全筛查与 AI 滥用监测的呼声。同时，这也给其他领先实验室带来压力，要求其展示类似的防护措施与披露机制。 该披露来自 Claude 模型背后的 AI 安全公司 Anthropic，但报道未给出技术细节，例如这些企图是如何被检测和阻止的，以及是否触及危险能力阈值。即便有 AI 协助，真正制造生物武器仍面临巨大的物理和后勤壁垒。

google\_news · The New York Times · 9月10日 21:50

**背景**: Anthropic 是一家 AI 安全与研究公司，由前 OpenAI 成员于 2021 年创立，CEO 为 Dario Amodei，以打造可靠、可解释、可操控的 AI 系统为核心主张。AI 安全是一个跨学科领域，致力于防止 AI 引发的事故、滥用及其他有害后果，包括生存性风险和滥用风险。生物安全则指防止有害生物制剂被有意或无意释放、传播的一系列措施，涵盖大流行病和生物恐怖主义等威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biosecurity">Biosecurity</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#biosecurity`, `#Anthropic`, `#AI risk`, `#national security`

---

<a id="item-10"></a>
## [OpenAI 转变立场，呼吁制定全国性 AI 安全规则](https://news.google.com/rss/articles/CBMiugFBVV95cUxQLWRvMF9uc0JNaTV5dkthSV9KV0tnODBHUUxnbDlOZzJhYk9aZHZvNVhPLTRkQXpvOE1NNkRXN0Niek5kR0Vwc0FzeWJzRFNMVDd1eGh3RWlzc1RKOXZwTmhpQ3lyZWtJR0xqLW55aU5BSGJzM05zVjkwLXZ2YndNcG1JamVDY1kwY3Z3X3h5Q2dScmF4ZUNYX0NPejZZTTI3NE5ld2hSYlJtakVYazlRVXBydExpMDRVMEE?oc=5) ⭐️ 7.0/10

据《巴尔的摩太阳报》报道，OpenAI 已改变此前立场，公开呼吁制定全国性的人工智能安全规则。此举标志着该公司从过去的态度转向支持建立统一的、国家层面的 AI 安全监管框架。 OpenAI 是最具影响力的 AI 开发机构之一，其对全国性安全规则的支持可能为联邦层面的监管提供政治动力，并影响竞争对手、初创公司及下游用户需遵循的标准。这也表明，领先的 AI 企业可能越来越倾向于支持单一的国家框架，而非各州各自为政、日益碎片化的 AI 法律体系。 目前可获得的源材料基本只是一个标题和链接，因此报道并未详细说明 OpenAI 提议的具体内容，例如是否支持设立联邦监管机构、强制性安全测试、许可制度，或是否主张优先于各州法律。读者应注意，“立场转变”这一定性是报道的表述，而非一份完整的政策文件。

google\_news · Baltimore Sun · 9月10日 15:19

**背景**: OpenAI 是 ChatGPT 的开发方，该产品于 2022 年底发布，引发了当前的生成式 AI 投资热潮以及随之而来的安全争论。此后，美国的 AI 监管主要在州层面推进——例如科罗拉多州的《AI 法案》、加州被否决的 SB 1047 以及随后的 SB 53——而欧盟则推出了自己的《人工智能法案》。这种局面导致监管格局碎片化，AI 企业认为合规成本高昂，因此美国是否应以一部全国性规则取代众多州级法规，成为政策争论的核心问题。

**标签**: `#AI policy`, `#AI regulation`, `#OpenAI`, `#AI safety`, `#governance`

---