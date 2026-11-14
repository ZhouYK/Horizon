---
layout: default
title: "Horizon Summary: 2026-11-14 (ZH)"
date: 2026-11-14 23:03:16 +0000
lang: zh
report: ai
---

> 从 143 条内容中筛选出 6 条重要资讯。

---

1. [研究人员称 DeepSeek、Kimi 等中国模型使用了被禁售的英伟达 Blackwell GPU 训练](#item-1) ⭐️ 8.0/10
2. [Futurism 报道：AI 聊天机器人仍在向购物用户推荐诈骗网站](#item-2) ⭐️ 6.0/10
3. [《台北时报》：世界濒临自主武器革命](#item-3) ⭐️ 6.0/10
4. [联合国将讨论对 AI 驱动的自主武器实施限制](#item-4) ⭐️ 6.0/10
5. [Anthropic 被指侵犯神经网络专利，卷入新专利纠纷](#item-5) ⭐️ 6.0/10
6. [AI 模型据称可在症状出现前数年预测阿尔茨海默病进展](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [研究人员称 DeepSeek、Kimi 等中国模型使用了被禁售的英伟达 Blackwell GPU 训练](https://news.google.com/rss/articles/CBMi_wJBVV95cUxQR0JoRXdycDVWakNINktZeHpUS1pLN2xxS0p1dVhFODJ1bkpPMEExZG9yb0dGSlRTMkhzbkNVYTlkWXl4OWk4Ujc4dEtJU0stNG5fT2JpdjJHNTRfZUxjSmk3cXEwa0F0YmNsRGtFMml0NWdzSjB4NnBaNS1vMFp4MWhsdDFBUlM4OEd6dlh1MGZBOUloRFlsam11dUh3WHJVSWVUWElwajhZWk9kS1hQbU54U2dlQy1EWHhsa1oyN0pDNElRd0hBdmY5bG1KeFlzSkhKNXg1dkxYNmFBVTJld3M5UkZDbHRsLTU0Y0J5TjFNQlp3Tl9DVnU1d1VTTGV6VGVzaTA2YXlPUGNHNXZIMXlsQ0xLVGtycVBzQzB4RHNHRDkzY08wMDJUcmtKb29TU1NuaktQYkw4WEJJNndJQVdPbU1WVC1WT3RudVJXM3VDM3Mwd3N5THZEcnBvOVBvZXE5UV9IbzhSbGM1Z2djcGI0Ym9hS0xjUHZQZ09lQQ?oc=5) ⭐️ 8.0/10

研究人员对五个开放模型（据称包括 DeepSeek-V4-Pro、月之暗面的 Kimi K3 以及 Ling-3.1-flash）进行了分析，声称这些模型初始权重中的可识别特征表明它们是在英伟达 Blackwell GPU 而非较旧的 Hopper 架构上训练的。该团队使用了一种新的 GPU“指纹识别”方法，通过比对 GPU 核心布局来区分 Blackwell 与 Hopper 硬件。 Blackwell 代际的加速卡受美国出口管制约束，不能合法出售给中国企业，因此这些指控意味着中国主要 AI 实验室可能存在规避出口管制的行为，也让“AI 算力究竟能否被治理与审计”成为尖锐问题。如果这种指纹识别方法站得住脚，监管者和研究者就获得了验证某个模型由何种硬件训练的技术手段，而不必依赖企业自述或供应链追踪。 该分析基于对模型初始权重和 GPU 核心布局的检查，而非直接接触硬件，指纹所暗示的训练集群规模据报约为 3,000 至 4,500 块 GPU；这些结论来自独立分析的指控，并非经确认的审计结果，也不代表英伟达或相关实验室的官方表态。

google\_news · Tom&\#x27;s Hardware · 11月14日 14:50

**背景**: 英伟达的 Blackwell 架构（2024 年 3 月在 GTC 上发布，旗舰 B200 由两颗芯片拼接而成）接替 Hopper 成为其顶级 AI 训练平台，而美国的出口规定限制此类先进芯片对华销售。GPU 指纹识别最初源于安全研究，通过时序与渲染上的细微差异来识别单个设备——例如 NDSS 2022 上发表的“Drawn Apart”技术，可通过 WebGL 远程区分外观完全相同的 GPU。这项新研究把思路延伸到模型权重上：由于不同芯片架构上的浮点运算会产生略有差异的数值结果，模型训练后的参数可能残留特定架构的痕迹，从而暴露其所用硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/deepseek-and-moonshot-ai-models-appear-to-carry-hidden-nvidia-blackwell-fingerprints-in-their-starting-weights-pointing-to-training-clusters-of-3000-to-4500-gpus/">DeepSeek And Moonshot AI Models Appear To Carry Hidden NVIDIA ...</a></li>
<li><a href="https://www.tomshardware.com/news/researchers-gpus-can-be-used-for-digital-fingerprinting-and-web-tracking">GPU Fingerprinting Can Be Used to Track You... | Tom&#x27;s Hardware</a></li>
<li><a href="https://sercankulcu.github.io/posts/2024/03/nvidia-announces-the-blackwell-gpu-architecture/">NVIDIA Announces the Blackwell GPU Architecture - Point Zero</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#GPU fingerprinting`, `#Nvidia Blackwell`, `#DeepSeek`, `#China AI`

---

<a id="item-2"></a>
## [Futurism 报道：AI 聊天机器人仍在向购物用户推荐诈骗网站](https://news.google.com/rss/articles/CBMie0FVX3lxTE5aSHlZX2RZQmFWSnF1S25wUHlTb1ZvdURmZ3VMcjV4b3kzRE1oVW4wRHdLVmR5QzN4Umx1a1pwbXRxc3dpTE9fUkxlUFk1WTRHRVdiUE82N2RsYkJFaGM3ZEZzN1dBUmNOc3pWZ2hzTUt4YWJpdnVmemg5TQ?oc=5) ⭐️ 6.0/10

Futurism 报道称，当用户向 AI 聊天机器人咨询购物建议时，这些机器人仍会推荐诈骗网站，说明该问题在已上线的消费级产品中持续存在，而非偶发故障。报道将此视为商用大模型助手中尚未解决的可靠性与信任安全问题。 聊天机器人正越来越多地被当作购物助手使用，因此一次错误推荐可能直接让用户损失金钱或暴露于欺诈风险，而不只是给出一句尴尬的回答。由于该问题反复出现，它动摇了“大模型助手可作为中立购物顾问”这一前提，也会促使厂商增加核验机制或给出更明确的提示。 该条目仅为一条新闻标题链接，并未公布测试方法，因此无法确定测试了哪些聊天机器人、用了多少提示词，也无法判断诈骗网站是源自模型幻觉、过时的训练数据，还是来自被 SEO 垃圾内容污染的搜索或 RAG 结果。报道也没有说明模型是被直接要求给出链接，还是通过浏览工具自动检索到这些网站。

google\_news · Futurism · 11月14日 18:02

**背景**: 大语言模型聊天机器人通过预测看似合理的文本来生成回答，当它们给出店铺或链接时，往往依赖训练中学到的模式或查询时抓取的网页结果，而这两者都无法保证商家是合法的。诈骗网站和代发货网站正是利用这一点，用经过 SEO 优化的页面充斥搜索结果和联盟营销内容，因此只会复述高频网址的模型可能反而放大欺诈。这属于已知的大模型失效类型，与幻觉引用以及带浏览功能助手中的提示注入风险密切相关。

**标签**: `#AI Safety`, `#LLM Reliability`, `#Chatbots`, `#Consumer Protection`, `#E-commerce`

---

<a id="item-3"></a>
## [《台北时报》：世界濒临自主武器革命](https://news.google.com/rss/articles/CBMieEFVX3lxTE5UbDUxN0dlazNyUXZWakZ5OGVSRTFWMGhpbkd0NTRUWE84aFdRbFU2aF9CVzJ6ZzBmQkZwX2lobUoyU1RRS19LOXV4REtXcnk2SWUyUFJCbks5WWV4bWxIcnZ4cWZFRUQ1WURmZ3BqYnVRVDA4TVFETA?oc=5) ⭐️ 6.0/10

《台北时报》发布了一则标题，称世界可能正处在自主武器革命的前夕，但所提供的内容只有标题和链接，没有文章正文。 如果这一说法反映了军事人工智能领域的真实转变，那么它意义重大，因为自主武器可能改变战争方式，并就人工智能伦理、国防政策和国际稳定提出紧迫问题。 所提供的内容没有技术细节、时间表、案例或具名系统，因此仅凭现有信息无法核实或深入评估该标题中的说法。

google\_news · Taipei Times · 11月14日 16:00

**背景**: 自主武器是设计用于在无实时人工控制的情况下选择并攻击目标的军事系统。它们与军事人工智能和人工智能伦理密切相关，其发展受到各国政府和民间社会关注，因为目标选择决策可能带来严重的法律和道德后果。

**标签**: `#autonomous weapons`, `#military AI`, `#AI ethics`, `#defense technology`, `#policy`

---

<a id="item-4"></a>
## [联合国将讨论对 AI 驱动的自主武器实施限制](https://news.google.com/rss/articles/CBMisgFBVV95cUxOcloza1U3a1BwWGxhREpyVnVOVHhmQ2lURlA2Q0pUekUtd3VPOTRza2k3b3dYc010eWt1cW5NUXQ1ck5ybUdrbDRnUXR0R21PWnY1QnJxWWhWbEUzU3NmSnliLWF0X290alpKZkZPQVBhdWtzTGpPaXhFTnJoQVpETHVrZ2xXM2ZjNVB4YjZCQ1BVOVVscHNNX20zTzlCbnI5Z0JGYzVTMGZEMG9DZTVtQjVB0gG3AUFVX3lxTFBaanBpUmhROS1KSExhaHBUZUpvU2hlQU53ZDEyb0V2WXktUDdoQ3lpTDlpMnhCVTNPOTRCRWN5aUJ4OHZ4UzJXWG9KbjhxTk1haERldjAxT0Q3Zno1NnExVFlPR1dkVWdCZlhsRzhZT1lxNVgwdWdKX0tHakxCZmY3Ym8wWnlWTGVpRnllYjVNWXFMbDJ6amZHUFBDd0pMcjRVNXF1ZGpOaDJGY0hVRlNPWExEV2YwMA?oc=5) ⭐️ 6.0/10

据乌克兰通讯社（Ukrinform）报道，联合国将就限制 AI 驱动的自主武器展开讨论，为围绕军事 AI 的长期争论新增一条多边外交轨道。这一消息表明，在人们对机器无需人工干预即可选择并打击目标的担忧日益加深之际，该议题在国际议程中的地位正在上升。 即便具有约束力的条约仍遥遥无期，联合国层面的限制讨论也可能塑造相关规范、出口管制和采购规则，从而影响正在研发自主系统的国家和国防承包商。其意义还在于，此前的治理努力主要停留在专家层面而非高规格政治辩论，因此把议题提升到更高层级会增加主要军事大国公开表明立场的压力。 这些讨论的核心分歧在于对武力使用保持“有意义的人类控制”这一概念：一些国家和红十字国际委员会（ICRC）主张具有法律约束力的限制，另一些则倾向于非约束性原则和现行的国际人道法。尚未解决的关键技术问题包括：如何界定目标选择中的自主性、如何核查合规情况，以及如何将完全自主武器与保留人类在环的 AI 辅助决策工具区分开来。

google\_news · Ukrinform · 11月14日 21:27

**背景**: 致命性自主武器系统（LAWS）是指一经激活即可在无操作员进一步干预的情况下选择并打击目标的武器，这与只打击由人类选定目标的半自主系统不同。由于此类系统在责任归属和遵守国际人道法方面引发疑问——尤其是在区分原则和比例原则方面——该议题已在日内瓦的《联合国特定常规武器公约》（CCW）框架下讨论了十多年，而该公约的协商一致规则使正式监管进展缓慢。红十字国际委员会、斯德哥尔摩国际和平研究所（SIPRI）和联合国裁军研究所（UNIDIR）等机构就现行法律的适用问题发表了大量分析，而美国等国家则出台了国家政策，例如要求在对武力使用时保持适当程度人类判断的国防部第 3000.09 号指令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapon">Lethal autonomous weapon - Wikipedia</a></li>
<li><a href="https://www.icrc.org/en/law-and-policy/autonomous-weapons">Autonomous weapons | ICRC</a></li>
<li><a href="https://aigovref.com/military-ai">Military AI &amp; Autonomous Weapons | AI Governance Reference</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#autonomous weapons`, `#UN policy`, `#AI ethics`, `#military AI`

---

<a id="item-5"></a>
## [Anthropic 被指侵犯神经网络专利，卷入新专利纠纷](https://news.google.com/rss/articles/CBMi_AFBVV95cUxQa09ZQllGRFA4eTctdzhDMFk4VmkxeGhZcTNpcWQ5SXhSVU83akhfT3lTMDZoMG00U3NTNHl4amhsTjBTYjhmbi1hZGtVZF8xSTFqZ29aZE02WEZvcXpzbW9Zb2s0azROS25sZHpCUlNGbFQ5WHhBRlpja3ZwcktkREZmMDNFbGVDcnlvdHdkeTNFRVV6N21rc3hlQTJUSUk1WFFiM1FidlRfT2RpWVByR2ZYN2lUVU1EUXB1R0JGQkdWaWRzQXFhaERnaTljZDN3QUN0V05WOWtnbkl2ZElqYTAtcVE5TU5NaGItcEctQ0x0SnhBUnBuU2tUdUw?oc=5) ⭐️ 6.0/10

VitalLaw.com 的专利新闻栏目报道称，Anthropic 的人工智能系统被指控侵犯了神经网络相关专利。目前该报道仅以标题形式呈现，尚未披露原告身份、涉案专利号、受理法院或起诉时间等具体信息。 Anthropic 是规模最大的前沿 AI 开发商之一，因此针对它的专利诉讼可能会检验早期的神经网络专利能否被宽泛地用来主张现代大语言模型系统侵权。判决结果可能影响整个生成式 AI 行业的诉讼风险与专利许可成本，而不只是 Anthropic 一家公司。 由于目前只有标题信息，涉案专利的具体内容、权利要求范围以及被指控的产品均不得而知，也无法判断这是一起新提起的诉讼、正在进行的案件，还是专利许可纠纷。在 AI 领域，专利主张往往取决于通用的神经网络架构与训练方法是否被描述得足够具体，从而能够经受住美国专利法第 101 条可专利性以及现有技术方面的无效挑战。

google\_news · VitalLaw.com · 11月13日 23:03

**背景**: 神经网络是一种机器学习模型，它把多层计算堆叠起来以产生分类结果或生成文本等输出，早在 20 世纪 80 年代和 90 年代就已出现各种形式的专利。美国专利分类 706/15 专门涵盖神经网络相关的发明，从专用神经网络处理器到卷积网络设计的各类申请都说明这一领域多么拥挤。Anthropic 开发的是大语言模型，例如其 Claude 系列助手，这些模型依托于在海量数据上训练的 Transformer 架构神经网络。随着生成式 AI 的商业价值不断上升，涉及基础性 AI 技术的专利纠纷也变得越来越常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://patents.google.com/patent/US20210019618A1/en">US20210019618A1 - Neural Network Processor - Google Patents</a></li>
<li><a href="https://patents.justia.com/patents-by-us-classification/706/15">Neural Network Patents (Class 706/15)</a></li>

</ul>
</details>

**标签**: `#AI patents`, `#Anthropic`, `#litigation`, `#intellectual property`, `#neural networks`

---

<a id="item-6"></a>
## [AI 模型据称可在症状出现前数年预测阿尔茨海默病进展](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPTTdOQjdpalh3dThBa2c0Um5PVElVbnFmTGNGaGxNQjdVenlKbzFoQzJRTUJCVXg3S0hBNEh5ekNoMlNJRW9YN2N6eUZiU1pUNHo1dGx6d0NjUmpzcEFDWnRldXJlVGVYVDBmZ3FnY3RYY0xVV1FQUWFGcUhnb0tObVpLQUs5UHo0RTNVOXllMjByWHRaMUx1enRSN0ZncWV2RC05SGtBQzBjT0xtZkdwUG1aWk1UVjRSWG1aQUVWQkVVQQ?oc=5) ⭐️ 6.0/10

Bioengineer.org 发布了一则报道标题，称人工智能模型能够在临床症状出现前数年预测阿尔茨海默病的进展情况。目前可获取的内容仅为一个标题和链接，没有附带研究出处、方法说明、数据集描述或准确率指标。 阿尔茨海默病具有漫长的临床前阶段，因此任何能够提前标记出可能进展的工具，都对临床试验的患者筛选、更早的生活方式与风险因素干预以及照护规划具有重要意义。如果相关工作能够通过独立验证，将进一步支持这样一种日益增多的证据：将机器学习应用于生物标志物和临床记录，可以优于传统的预后评估量表。 在没有原始论文的情况下，一些关键问题仍无答案：模型基于何种数据训练（如 MRI 或淀粉样蛋白/tau PET 等影像、脑脊液或血液生物标志物、认知评分，或电子健康记录）、预测能够提前多久、以及敏感度和特异度是如何测量的。该领域此前的研究常因样本量小、仅来自单一队列，以及结果难以在不同医院和人群中复现而受到批评，因此独立的前瞻性验证将是决定性的检验。

google\_news · Bioengineer.org · 11月14日 01:37

**背景**: 阿尔茨海默病是一种进行性神经退行性疾病，也是最常见的痴呆病因；其脑内变化（如淀粉样蛋白斑块和 tau 缠结的积累）在记忆问题明显出现之前数年甚至数十年就已开始。因此，研究人员依赖生物标志物（包括脑影像以及血液或脑脊液检测）来识别处于这一临床前窗口期的人群。机器学习模型在此颇具吸引力，因为它们能够把来自影像、化验结果和病史的众多微弱信号整合为单一风险估计，而这用人工编写的规则很难做到。该标题很可能指向某个具体学术团队发表或报告的研究，但仅凭现有条目无法核实其细节。

**标签**: `#AI in healthcare`, `#Alzheimer&\#x27;s disease`, `#medical AI`, `#predictive modeling`, `#biomedical research`

---