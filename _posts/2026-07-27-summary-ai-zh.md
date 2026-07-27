---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
report: ai
---

> 从 262 条内容中筛选出 10 条重要资讯。

---

1. [折扣 LLM 令牌转售的地下市场内幕](#item-1) ⭐️ 8.0/10
2. [开源 3D 打印便携式 MRI 机，成本低于 7 万美元](#item-2) ⭐️ 8.0/10
3. [Meta 允许 AI 生成虚假医生广告](#item-3) ⭐️ 8.0/10
4. [多家科技巨头支持开放权重 AI](#item-4) ⭐️ 8.0/10
5. [中国 AI 模型因低成本与开放性在美国崛起](#item-5) ⭐️ 7.0/10
6. [诺贝尔奖得主西蒙·约翰逊警告中国 AI 过度自动化风险](#item-6) ⭐️ 7.0/10
7. [英伟达和微软敦促美国保护开放 AI 模型](#item-7) ⭐️ 7.0/10
8. [科技巨头裁员 14 万，同时增加 AI 投资](#item-8) ⭐️ 7.0/10
9. [以色列科技行业低迷导致 AI 裁员激增](#item-9) ⭐️ 7.0/10
10. [三井不动产将在台积电熊本厂附近建设 AI 中心](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [折扣 LLM 令牌转售的地下市场内幕](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 8.0/10

Matt Lenhard 的调查揭露了一个黑市，转售者通过滥用免费试用、窃取凭证以及开源代理工具（如 one-api 和 new-api）来提供折扣的 LLM API 访问。 这个市场暴露了 LLM 提供商和合法用户的重大安全和经济风险，因为它助长了欺诈、绕过地理限制以及潜在的用于模型蒸馏的数据窃取。 这些代理主要基于开源项目 one-api 及其分支 new-api，两者都是合法的 API 网关，可以在多个 API 密钥之间进行负载均衡。买家包括寻求廉价令牌、避免地理限制或收集数据用于模型蒸馏的人。

rss · Simon Willison · 7月26日 19:30

**背景**: LLM API 令牌是允许开发者使用大型语言模型（如 GPT-4）的凭证。官方定价可能很昂贵，尤其是对于大量使用。One-api 和 new-api 是开源 API 代理工具，旨在管理和分发跨多个密钥的 API 调用，在这种情况下被滥用来聚合折扣或欺诈性令牌。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/26/relay-market/">An Inside Look at the Relay Market Powering Token Resellers and...</a></li>
<li><a href="https://github.com/songquanpeng/one-api/blob/main/README.en.md">one-api/README.en.md at main · songquanpeng/one-api</a></li>

</ul>
</details>

**标签**: `#LLM`, `#API fraud`, `#token reselling`, `#cybersecurity`, `#AI market`

---

<a id="item-2"></a>
## [开源 3D 打印便携式 MRI 机，成本低于 7 万美元](https://news.google.com/rss/articles/CBMi4AJBVV95cUxPVFVmeFlqU1MxUWR0QUtZVDdhUGc3V3Mtc0tmZk0yN2RVbEk3RkYzVVUxaU9WX2N6XzhTLVhSa2E0cFBVOTlrMTBsbWNfQmFXSE9mYWstUnFBVy1wdThid3FHWmxLbC0yQnZLWktIWDRlUEJURHF4bmw1RHNCbGtTNGhmWlNNUDNkdGNLN2o5dlRiMnVjZ0JDY3Rma05GUzhHcWtBTV9IU3I3QlJmUnIzeTBEZUplZ1RhbC1uMG12ajY4aU96Z2FmWjRhT2JSWngzQUpGNENieVFuMFBubjBuM3dHMWwyWlY0cEtCUkFfanVqS1FXRURXOUxpN3lpMFNreTJBNXJnRnYwSVE5QUxyN2RrbjMzbmRPVGZKVko1ZEFzUjFBMk94eFFKNUFkb2JaTnhhcjZYZTdkcXdkWk95cEZCM0FaZ1Fnc01GcHlyeVhVSGYxaUZZNnI4enlaZTB2?oc=5) ⭐️ 8.0/10

一支团队利用开源设计和 3D 打印技术，开发出一台便携式 MRI 机，成本不到 7 万美元，仅为传统全尺寸 MRI 机起步价 110 万美元的 7%。 这一突破可能通过大幅降低成本并支持本地制造，使 MRI 成像在资源匮乏和偏远地区普及。它同时也展示了开源硬件颠覆昂贵医疗设备市场的潜力。 该设备采用低场 MRI 技术，通常工作在 0.1–0.25 特斯拉，降低了磁体复杂性和成本，同时仍能生成临床可用图像。开源设计允许任何拥有 3D 打印机和基本电子技能的人复制该系统，促进了本地维修和定制。

google\_news · Tom&\#x27;s Hardware · 7月26日 14:36

**背景**: 传统 MRI 机价格在 100 万至 300 万美元之间，且需要专门的屏蔽和冷却设施，因此只能用于资金充足的医院。低场 MRI 使用较弱的磁体，降低了成本和尺寸，而近年来图像重建技术（如深度学习）的进步，改善了低场条件下的图像质量。开源医疗设备设计遵循节俭工程原则，提供免费的技术规格，以实现低成本本地制造。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Low-field_magnetic_resonance_imaging">Low-field magnetic resonance imaging - Wikipedia</a></li>
<li><a href="https://www.hopkinsmedicine.org/news/articles/2024/11/low-field-mri-could-democratize-access-to-medical-imaging">Low-Field MRI Could Democratize Access to Medical Imaging | Johns Hopkins Medicine</a></li>
<li><a href="https://www.nature.com/articles/s44222-024-00162-9">Open-source design of medical devices | Nature Reviews Bioengineering</a></li>

</ul>
</details>

**标签**: `#open-source`, `#3D-printing`, `#medical-devices`, `#healthcare`, `#DIY-hardware`

---

<a id="item-3"></a>
## [Meta 允许 AI 生成虚假医生广告](https://news.google.com/rss/articles/CBMifEFVX3lxTE1mVFJKdTZGSWhqU3hHVGl2UjZUNTVCTWxJTVFoU1RRMkNHOS1kV3NUX2xHc1FJSEIyX2JFcjN2U0NnSFo5ZlV0ZERwNVlnaFoyY19TdjEyS0hZX0loY3g4V0g0dnpaM0hhN0p0NkhhbjZGQ2EtQi1hamtrVTI?oc=5) ⭐️ 8.0/10

Futurism 的一项调查显示，Meta 允许 AI 生成的虚假医生资料在其平台上推销未经证实的医疗疗法。 这通过欺骗性的 AI 生成角色推销假药，构成严重的公共健康风险，并引发对平台内容审核和 AI 滥用的伦理担忧。 这些虚假资料使用 AI 生成的面孔和资质来显得正规，广告针对寻求医疗建议的弱势用户。

google\_news · Futurism · 7月26日 17:01

**背景**: 深度伪造是利用 AI 生成的合成媒体，通常借助生成对抗网络（GAN）制作逼真的图像或视频。此类技术可能被滥用来冒充医生等专业人士，正如本案例所示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deepfake_detection">Deepfake detection</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#misinformation`, `#social media`, `#healthcare`, `#platform moderation`

---

<a id="item-4"></a>
## [多家科技巨头支持开放权重 AI](https://news.google.com/rss/articles/CBMipAFBVV95cUxOS0hQcXlIMVB5UFFwVXM1Y0pZQm5XOXBzUmNveTg4RjZCc2RNdjdOVFV4U2JDZWdrTTRuTVROZ3lodE5FRVpielNWTVUyaFJkQlhHLVZmSVBWc1BRUHhNS1dNUjNTZ1lCb0drYk9pQ2hLQUtIUXlQUUc4eDNGVGYxOVQ5S1JSaDF0Q3BKSFFncDBKYUZCVV9fTm1aZXd6bjZKanB2dg?oc=5) ⭐️ 8.0/10

Meta、微软、英伟达、IBM 等多家科技巨头公开支持开放权重 AI 模型，标志着行业集体推动更易获取的 AI。 这些领先公司的支持可能加速开放权重模型的采用，减少对专有系统的依赖，并在各行业促进创新。 开放权重 AI 意味着模型的权重公开共享，但与完全开源 AI 不同，训练数据和代码可能不包含在内。这种方法平衡了透明度和实用性。

google\_news · AI News · 7月26日 07:27

**背景**: 在 AI 中，“权重”是模型在训练过程中学习的数值参数，决定其如何处理输入。开放权重模型使这些权重公开可用，允许他人使用和微调模型。然而，它并非完全开源，因为训练数据、代码和方法可能仍属专有。理解这一区别对于把握行业支持的影响至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://tech.yahoo.com/articles/openai-just-teased-open-weights-224557547.html">OpenAI Just Teased a New &#x27; Open - Weights &#x27; AI Model: Here&#x27;s What...</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#industry-news`, `#machine-learning`, `#big-tech`

---

<a id="item-5"></a>
## [中国 AI 模型因低成本与开放性在美国崛起](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQOG9xZXdnSm5sYXJDbHMxZDZ1SWJVWTdMLVNmVDNnbW96VHhvaUd6TGl4T1lFSGk3WUFlMGhlNmxIdG5PRUQ4SVVqQTBRYkRNRUJzSFhCUnVxU3NXczlvbHB0SGJ2V2h0emJiOFdnb2hHb0pLQXlSaWlFUzFrQzBPa1hFeW9IZUdrQWhfYUxHS19nOFh3aVhNUlhPdG95eG1iNzAxWUVyZWY5bmRtT3UwZjBMT1ZNM0xWS0picUM0Q2ZBSHl0dWk1SXFsM21xWVVhREE?oc=5) ⭐️ 7.0/10

中国 AI 模型（如 DeepSeek 的开放权重系列）正越来越被美国市场采纳，提供比美国开发的模型更廉价和开放的替代方案。 这标志着全球 AI 格局的转变，挑战了美国的主导地位并促进了开源创新。它影响了先进 AI 的竞争、定价和可及性。 DeepSeek 的模型是开放权重的，但训练数据未开放许可。DeepSeek-V4 Flash 具有 284B 参数的 MoE 架构和 100 万 token 的上下文窗口。

google\_news · Los Angeles Times · 7月26日 15:14

**背景**: DeepSeek 是一家中国 AI 公司，于 2023 年 11 月发布了首个模型。其开放权重模型允许全球开发者使用和微调，促进了快速采纳。美国市场传统上由美国 AI 实验室主导，但更便宜且具有竞争力的中国模型正在改变这一局面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://build.nvidia.com/deepseek-ai">AI Models by DeepSeek AI | Try NVIDIA NIM APIs</a></li>
<li><a href="https://openmodelmap.com/task/text-generation">Text Generation Models - OpenModelMap | OpenModelMap</a></li>

</ul>
</details>

**标签**: `#AI`, `#Chinese AI`, `#machine learning`, `#technology competition`

---

<a id="item-6"></a>
## [诺贝尔奖得主西蒙·约翰逊警告中国 AI 过度自动化风险](https://news.google.com/rss/articles/CBMiygFBVV95cUxPSTZKeVZrZ3VpOGd2V29ZdW94RGl0VTF1TlZadzdGckVTeEVhZW5qSkpFcGFoMjhEQXpubXFjdUpCNHNOX2JTVnNtRmVTc1c3Zlc4YVpMcllCQmRGX1lTanBkNjJxbFUxTGNBdmpaNDlwZGZsZnNZVTFnd09jWV82TnN0Ylk4blJIQjg3b3JVQzlxejZ1cFV6UjZCa05SWDhaT3NXYnRiSDRia1FTMHAwN3JSV3pGclJCaFEwMVZPZDVXQks1N0d6Y0pn0gHKAUFVX3lxTE02R3JuYnVmcmdVcVdKZ0lqMnlDcGJRODUwbkRFazNkWGVtSkxiWFllNE9nVDRqU1pLY1FRWTYyMmFva0RGNzJVa1hlTXYzcF9kZThlZjV3MmlPNXo2ODNzZjk1WTBZM1B3TVdwNjB5azNQRHJYdXQ3eTdZUk1sRTJFbWJ5REF1cExPek1IRGxheEFabGVTRjZNYzJvRldwUHozSkFWR29aRC1lY2ZfMnNJclpaeUdMbG1ZdEFrVkg2ZDNNODBJNEl3elE?oc=5) ⭐️ 7.0/10

在接受《南华早报》独家专访时，诺贝尔奖得主西蒙·约翰逊讨论了全球 AI 竞赛，并警告中国面临过度自动化的风险，即过度投资自动化可能导致失业和经济不平等。 这位知名经济学家的分析指出了中国积极推动 AI 可能带来的负面影响，这可能产生重大的社会和经济后果。它为关于平衡自动化与劳动力市场稳定的持续辩论增添了关键视角。 《权力与进步》合著者西蒙·约翰逊强调，过度自动化可能加剧不平等并削弱工人的议价能力。他建议中国应专注于补充而非替代人类劳动的 AI 应用。

google\_news · South China Morning Post · 7月26日 22:00

**背景**: 西蒙·约翰逊是诺贝尔经济学奖得主，以经济增长和产业政策研究著称。

“过度自动化”指的是自动化技术的部署速度导致其摧毁的就业岗位多于创造的就业岗位，从而引发结构性失业。中国作为工业战略的一部分，大力投资 AI 和自动化，这引发了关于就业替代的担忧。

**标签**: `#AI`, `#automation`, `#economics`, `#China`, `#Nobel laureate`

---

<a id="item-7"></a>
## [英伟达和微软敦促美国保护开放 AI 模型](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrN0E0NHI5bk4xb1ZLTHUxcGdDVjA3bXJuZ2VPRGFDU3hxQkpadmhxbTdGc1BEaUhyTFRNeXEtQUJvTmtGUjdHcFR3YkFqNExZTlRyZFJ3cHdLZENoNkN5blpkbUNkOElX?oc=5) ⭐️ 7.0/10

英伟达和微软正在游说美国政府，要求制定政策保护开放 AI 模型免受限制性法规的影响。 此举突显了在 AI 监管中如何不扼杀创新的重大政策辩论，并可能影响未来美国的 AI 法规，进而波及全球开发者和企业。 这些公司主张采取平衡的方法，在维护开放模型优势的同时应对潜在的滥用风险。

google\_news · calcalistech.com · 7月26日 18:03

**背景**: 开放 AI 模型是指权重和代码公开可访问的 AI 系统，允许自由使用、修改和分发。大型科技公司认为，过于严格的监管可能阻碍创新，并让封闭的专有模型占据优势。辩论的核心在于如何在管理强大 AI 的同时保持开放性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/models">Compare AI Models : Pricing, Context &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_ModelSphere">Open ModelSphere</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#open source`, `#Nvidia`, `#Microsoft`, `#AI policy`

---

<a id="item-8"></a>
## [科技巨头裁员 14 万，同时增加 AI 投资](https://news.google.com/rss/articles/CBMijwFBVV95cUxNbk5INXdaVl9jTWVsRnZoa1puR1UwTF9zNFZ6R0luOFBsd0ZGc2Y2RmRfSkVCUDYzTUVWOEtZNlgxZGFaWkJxcDN0ZUZrOEE0QTNsX1ZlcFB1a3piUmQxSWJuRnVqdFV3Mzk3V0N1b1pnc29BQ0U3M2ZUZ1MyQl9vUWlOYkVnMHpOV3VaYTJUaw?oc=5) ⭐️ 7.0/10

据最新报告，科技公司在大幅增加人工智能投资的同时，已裁减约 14 万个工作岗位。这标志着整个行业在劳动力和投资重点上的重大转变。 这一趋势表明资源正从传统岗位向 AI 驱动项目进行根本性重新分配，可能重塑科技就业格局。同时，它也引发了对岗位替代以及快速采用 AI 所带来的社会影响的担忧。 裁员波及多家科技巨头，工程、销售和支持岗位被裁撤，同时 AI 相关职位被新设。报告强调，公司正大力投资于 AI 基础设施、研究和部署，这往往以牺牲其他部门为代价。

google\_news · PYMNTS.com · 7月26日 23:10

**背景**: 科技行业正经历由生成式 AI 和大语言模型进步驱动的转型。谷歌、微软和 Meta 等公司竞相将 AI 集成到其产品中，导致对数据中心、芯片和 AI 人才的资本支出激增。与此同时，成本削减措施导致非 AI 领域的裁员。

**标签**: `#AI`, `#job market`, `#tech industry`, `#layoffs`, `#spending`

---

<a id="item-9"></a>
## [以色列科技行业低迷导致 AI 裁员激增](https://news.google.com/rss/articles/CBMibEFVX3lxTFBxeDBuUWxkU3g1eWpoZmhlN1JqZ2dIMXhsQ3BoSkZLX2NZRERnTlljaHMwX1MyZnVONVpZNUd1X25wdkJBOXlER0drQXRBNlZzRjdlN05kUXYtcVhsakxlT3ZMOWVsLW5rYmtIVQ?oc=5) ⭐️ 7.0/10

据《耶路撒冷邮报》报道，以色列的人工智能和软件公司正面临日益严重的裁员潮，这是更广泛的行业低迷的一部分。 这标志着以色列高科技行业（全球人工智能和软件创新的关键中心）显著收缩，可能影响全球科技人才流动和初创企业投资。 裁员波及多家 AI 公司，但未提供具体数字；文章强调软件行业正处于“血洗”之中，暗示大幅裁员。

google\_news · The Jerusalem Post · 7月26日 11:21

**背景**: 以色列科技行业（被称为“硅溪”）是经济的重要组成部分，拥有众多 AI 初创公司。2024-2025 年的全球科技放缓导致大规模裁员，以色列公司也无法幸免。文章可能指的是 AI21 Labs 等公司近期的裁员。

**标签**: `#AI`, `#layoffs`, `#Israeli tech`, `#software sector`

---

<a id="item-10"></a>
## [三井不动产将在台积电熊本厂附近建设 AI 中心](https://news.google.com/rss/articles/CBMizgFBVV95cUxNTGtDbGpIcGJ0bi0zQlQyX2lFVzNKNEQtMTdEWFJwN2dZQURaQVU0b0lCLXkxMEZEX3NZUEl4Mmg0RWpkVmlqemszcjJlaDgwNVRuZHZrLWx0ZEFKaW5xblA0T3FSUVFHR2dpdFFUOEdfM2ZTeTNoaFU2bkxMYUxkU3RCa250ZEVNSm52NUdpdmFaVWg2TzhVWFZmcFpnM243elI1NkNwZjJIOG1pczdpQVpZcHVUSUJBMU91elFkTEZqUGpsanR1YXdhVExxUQ?oc=5) ⭐️ 7.0/10

日本大型房地产开发商三井不动产宣布，计划在台积电位于熊本的半导体工厂旁建设一个物理 AI 中心。该中心旨在支持开发与物理世界交互的人工智能系统的公司，如机器人和自动驾驶汽车。 这一发展突显了将 AI 与半导体基础设施协同布局以加速创新的重要性。它使日本有望成为物理 AI 研究和制造的关键枢纽，可能吸引全球科技投资。 该中心将位于台积电熊本第一工厂附近，该工厂计划于 2024 年开始大规模芯片生产。三井不动产计划吸引从事具身 AI、机器人和自主系统领域的初创公司和成熟企业。

google\_news · Nikkei Asia · 7月26日 19:44

**背景**: 物理 AI 中心是一种专门设施，为开发和测试在现实世界中运行的 AI 系统（包括机器人和自主机器）提供基础设施。台积电在熊本的扩张是日本振兴半导体产业、确保先进制造能力的战略的一部分。AI 与芯片生产设施协同布局正成为全球趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.virginia.edu/initiatives/uva-research-hubs">UVA Research Hubs</a></li>

</ul>
</details>

**标签**: `#AI`, `#infrastructure`, `#TSMC`, `#Japan`, `#semiconductor`

---