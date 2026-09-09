---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09 23:05:46 +0000
lang: zh
report: default
---

> 从 189 条内容中筛选出 6 条重要资讯。

---

1. [DeepSeek 10 日发布 V4.1 Flash，V4 Pro 请求将自动切换并按新价计费](#item-1) ⭐️ 8.0/10
2. [五角大楼要求 OpenAI 开发极少拒绝军事命令的模型](#item-2) ⭐️ 8.0/10
3. [OpenAI 称 GPT-6 Astra 思维链可监测性显著下降](#item-3) ⭐️ 8.0/10
4. [小米 OPPO vivo 荣耀统一标准，碰一碰无网直连秒传](#item-4) ⭐️ 7.0/10
5. [Tibo 称 Astra 需求空前，或暂停 ChatGPT Pro 新订阅](#item-5) ⭐️ 6.0/10
6. [OpenAI 用 AI 设计芯片，称成本低于开源模型](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek 10 日发布 V4.1 Flash，V4 Pro 请求将自动切换并按新价计费](https://platform.deepseek.com/usage) ⭐️ 8.0/10

DeepSeek 计划于北京时间 2026 年 9 月 10 日前后正式发布 V4.1 Flash 模型。在 V4.1 Flash 上线之后、V4.1 Pro 发布之前，DeepSeek 会将所有 V4 Pro 的 API 请求路由到 V4.1 Flash，并按 V4.1 Flash 的单价计费。 这意味着正在使用 V4 Pro 的开发者无需修改代码，其负载就会被自动切换到性能更强、价格更低的 V4.1 Flash。这也表明 DeepSeek 的 Flash 系列已经超越上一代 Pro 模型，可能会影响开发者在成本、延迟和性能方面的选型。 据 DeepSeek 称，内部和外部测试显示 V4.1 Flash 在性能、费用、速度、总用时等指标上全面优于 V4 Pro。此路由调整适用于所有 V4 Pro 请求，并将持续到 V4.1 Pro 正式上线为止。

telegram · zaihuapd · 9月9日 07:18

**背景**: DeepSeek（深度求索）是一家以开源前沿大模型著称的 AI 研究公司，代表作包括 DeepSeek-V4、DeepSeek-R1 和 DeepSeek-Coder 等。在 V4 系列中，Flash 是旗舰 Pro 型号之下更小、更快、更便宜的选择：V4-Pro 拥有约 1.6 万亿总参数（每个 token 约 490 亿激活参数），而 V4-Flash 拥有 2840 亿参数（每个 token 约 130 亿激活参数），采用混合专家（MoE）架构。自动将请求从旧的、更大的 Pro 模型切换到新的小模型，是 DeepSeek API 运维策略的一部分，目的是让用户以更低成本获得更好表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 Explained: V 4 -Pro 1.6T vs V 4 - Flash 284B (2026)</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI Model Release`, `#API Change`, `#V4.1 Flash`, `#Machine Learning`

---

<a id="item-2"></a>
## [五角大楼要求 OpenAI 开发极少拒绝军事命令的模型](https://theintercept.com/2026/09/08/pentagon-openai-military-contract/) ⭐️ 8.0/10

泄露的五角大楼合同文件 P00003 显示，美国国防部要求 OpenAI 提供专门设计的“OpenAI 任务模型”，其对军事命令的拒绝率“尽可能低”。OpenAI 与五角大楼均否认最终协议包含此类措辞。 这一事态引发了对 AI 用于战争的严重伦理担忧，因为一个几乎不拒绝军事命令的模型可能在人类监督减弱的情况下被部署于致命行动。它也凸显了主要 AI 实验室与美国军方之间日益密切且颇具争议的联系。 “最低拒绝率”条款出现在合同 P00003 版本中，该版本扩大了价值高达 2 亿美元、为期两年的原型交易。The Intercept 通过《信息自由法》诉讼获得相关文件，而 OpenAI 发言人 Nate Evans 表示从未执行过包含此类措辞的合同。

telegram · zaihuapd · 9月9日 09:02

**背景**: OpenAI 已逐渐转向军事与国家安全领域的工作，偏离了此前禁止其技术用于军事的政策。拒绝训练是一种常见的 AI 安全技术，教语言模型拒绝有关有害内容的请求，但要求“最低拒绝率”可能会削弱这些防护措施。五角大楼一直在扩展 AI 应用，包括 Project Maven 等计划，这加剧了围绕自主系统和致命决策的持续辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theintercept.com/2026/09/08/pentagon-openai-military-contract/">The Pentagon Asked OpenAI for Artificial Intelligence Designed to...</a></li>
<li><a href="https://www.unite.ai/openai-pentagon-contract-defines-mission-models-by-minimal-refusal-rates/">OpenAI Pentagon Contract Defines ‘Mission Models’ by Minimal ...</a></li>
<li><a href="https://www.remio.ai/post/openai-pentagon-contract-records-reveal-a-disputed-demand-for-ai-that-rarely-say">OpenAI Pentagon Contract Records Reveal a Disputed Demand for...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#military AI`, `#AI ethics`, `#Pentagon`, `#contract`

---

<a id="item-3"></a>
## [OpenAI 称 GPT-6 Astra 思维链可监测性显著下降](https://deploymentsafety.openai.com/gpt-6-astra) ⭐️ 8.0/10

OpenAI 披露，GPT-6 Astra 的思维链（CoT）可监测性较前代显著下降；首席科学家 Jakub Pachocki 表示，依赖 CoT 监测的能力正“逐步减弱”。官方还提醒，Astra 的智能体间消息可能出现语法或空格错误。 此事意义重大，因为 CoT 可监测性是针对前沿 AI 模型为数不多的具体监督手段之一。如果该能力在未来模型中持续退化，依赖阅读模型推理的安全评估和对齐技术将变得更不可靠，从而威胁整个人工智能安全生态。 OpenAI 表示，该模型越来越能控制自身推理过程，并在更少甚至无需语言化推理的情况下完成更复杂的任务。英国 AI 安全研究所（UK AI Safety Institute）的外部评估发现，Astra 的原始推理更加压缩，含义不清的短语有所增加。

telegram · zaihuapd · 9月9日 09:45

**背景**: 思维链（Chain-of-Thought，CoT）指语言模型在给出答案之前生成的逐步可见推理过程。CoT 可监测性是指由人类或监督工具阅读这一推理内容，以发现隐藏的有害意图或不安全计划。最近的研究，例如论文《Chain of Thought Monitorability: A New and Fragile...》，表明 CoT 监测具有前景但比较“脆弱”：随着模型能力增强，它们往往更倾向于用压缩的潜在表示进行推理，使可见的推理链更不可靠，也更难用于监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.11473">[2507.11473] Chain of Thought Monitorability : A New and Fragile...</a></li>
<li><a href="https://www.emergentmind.com/topics/cot-monitorability">Chain-of-Thought Monitorability</a></li>
<li><a href="https://forum.effectivealtruism.org/posts/HvF94NoWTTCWiezk8/a-potential-strategy-for-ai-safety-chain-of-thought">A Potential Strategy for AI Safety — Chain of Thought Monitorability</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#Chain-of-Thought`, `#AI Safety`, `#Model Monitoring`

---

<a id="item-4"></a>
## [小米 OPPO vivo 荣耀统一标准，碰一碰无网直连秒传](https://finance.sina.com.cn/tech/roll/2026-09-09/doc-inirfivw8597070.shtml) ⭐️ 7.0/10

9 月 9 日，荣耀宣布由其主导制定的《碰一碰互传技术标准》正式落地，MagicOS 11 支持跨品牌“碰一碰”分享，荣耀 Magic9 首发搭载，小米、OPPO、vivo 已陆续接入。该功能用 NFC 触发配对、Wi-Fi 直连完成传输，无需云端和移动网络。 这是中国主流安卓厂商之间首次形成大规模的跨品牌文件互传互通，打破了各品牌生态的封闭限制，让不同品牌手机用户也能获得类似隔空投送（AirDrop）的体验。这将显著提升用户跨设备使用便利性，并可能推动更多安卓厂商采用通用的本地传输标准。 互传采用 NFC 触发配对、Wi-Fi Direct 负责实际数据传输，文件不经过云端、不消耗移动数据流量且不会被压缩。荣耀表示，实测 1GB 视频约 8—12 秒传完，跨品牌传输单文件通常上限为 2GB；使用时手机需支持 NFC 并更新至相应系统版本。

telegram · zaihuapd · 9月9日 12:30

**背景**: 此前，近距离快速互传能力通常绑定在单一厂商生态内，例如苹果的“隔空投送”或各家安卓定制系统专属的分享功能，导致跨品牌传输很不方便。NFC 是短距离无线通信技术，用于快速触发配对；Wi-Fi Direct 则能在两台设备之间建立无需路由器和互联网的高速直连链路。荣耀牵头制定该标准，荣耀 Magic9 是首款搭载该能力的机型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://android.tgbus.com/news/244640">安卓跨品牌 一 碰 传 来了！ 碰 一 碰 互 传 标 准 落地，荣耀 Magic9 首发</a></li>
<li><a href="https://m.mydrivers.com/newsview/1149784.html">安卓手机跨品牌 碰 一 碰 互 传 正式落地：荣耀MagicOS 11... | 快科 技</a></li>
<li><a href="https://www.pcpop.com/article/6949309.shtml">安卓终于能&quot; 碰 一 碰 &quot;跨品牌 互 传 了？ 荣耀牵头，四大厂商都要接-泡泡网</a></li>

</ul>
</details>

**标签**: `#NFC`, `#Wi-Fi Direct`, `#file transfer`, `#interoperability`, `#mobile`

---

<a id="item-5"></a>
## [Tibo 称 Astra 需求空前，或暂停 ChatGPT Pro 新订阅](https://x.com/thsottiaux/status/2097559315150426222) ⭐️ 6.0/10

Tibo（@thsottiaux）在 X 上发文称，OpenAI Astra 的需求达到空前水平；如果需求持续，团队可能暂时停止接受新的 ChatGPT Pro 订阅。 这说明即使是 OpenAI 的旗舰模型，也可能面临显著的算力或服务容量瓶颈。暂停 Pro 订阅会影响依赖 ChatGPT Pro 的重度用户和企业，也反映出前沿 AI 模型大规模部署给整个行业带来的基础设施压力。 Tibo 表示团队正优先保证现有用户的服务稳定，并称当前增长比以往任何时期都更陡峭。帖文中没有提供 OpenAI 的官方确认，也没有说明暂停订阅的具体时间安排。

telegram · zaihuapd · 9月9日 07:10

**背景**: Astra 指的是 OpenAI 发布的 GPT-6 Astra，OpenAI 称其为新一代智能体，在计算机操作、浏览、软件工程、网络安全、科学和专业工作等任务上达到先进水平。ChatGPT Pro 是 OpenAI 面向高端用户推出的付费订阅档位，通常提供更高的使用额度和最新模型的访问权限。这条 X 帖文表示，由于 Astra 的需求极为旺盛，为保证现有用户的服务质量，团队可能需要暂停新的 Pro 订阅。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra : A new generation of intelligence | OpenAI</a></li>
<li><a href="https://openai.com/index/path-to-astra/">Path to Astra : critical capabilities and frontier ... - OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#OpenAI`, `#ChatGPT`, `#订阅`, `#行业动态`

---

<a id="item-6"></a>
## [OpenAI 用 AI 设计芯片，称成本低于开源模型](https://www.reuters.com/world/china/openai-offers-ai-chip-design-touts-cost-advantage-over-open-source-cfo-says-2026-09-09/) ⭐️ 6.0/10

OpenAI 首席财务官萨拉·弗里尔表示，公司正把 AI 用于芯片设计、生命科学和金融服务，并称在云端部署低价 Luna 模型的成本低于中国开源替代方案。OpenAI 还表示，其自研 Jalapeno 芯片在 9 个月内完成设计定稿；Luna 降价 80% 后，使用量增加约 10 倍。 这表明 AI 正在加速进入硬件工程领域，有望压缩传统上需要数年的芯片设计周期。这也凸显了专有 API 模型与开源替代方案之间日益激烈的成本竞争，可能影响企业如何选择 AI 模型。 Luna 是 OpenAI GPT-5.6 系列的一部分；据 OpenAI API 文档，它大致对应早期 GPT-5 版本中的 nano 模型层级。本文还提到 OpenAI 自研的 Jalapeno 芯片在 9 个月内完成设计定稿，但对模型和芯片本身没有透露更多技术细节。

telegram · zaihuapd · 9月9日 13:06

**背景**: 传统芯片设计是一个需要数年的复杂工程，涵盖架构设计、逻辑设计、验证和物理布局等阶段，通常依赖专门的电子设计自动化（EDA）工具。OpenAI 以 ChatGPT 和大语言模型闻名，也通过云 API 提供 Luna 等模型，并将 Luna 定位为面向高吞吐量场景的高性价比选项。开源模型通常可免费下载并在用户自有硬件上运行，因此 API 提供商往往会强调“总体部署成本更低”作为竞争点。这一背景有助于理解为什么 OpenAI 声称 Luna 的云端部署成本低于中国开源替代方案具有重要意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.6-luna">GPT-5.6 Luna Model | OpenAI API</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-luna">GPT-5.6 Luna - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#chip design`, `#AI`, `#cost`

---