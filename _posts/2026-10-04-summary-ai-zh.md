---
layout: default
title: "Horizon Summary: 2026-10-04 (ZH)"
date: 2026-10-04 23:03:05 +0000
lang: zh
report: ai
---

> 从 139 条内容中筛选出 9 条重要资讯。

---

1. [Simon Willison 呼吁按用量服务默认设置硬性预算上限](#item-1) ⭐️ 7.0/10
2. [特朗普组建“超级智能力量”AI 特别工作组，Jay Clayton 领衔](#item-2) ⭐️ 7.0/10
3. [法院因播放“受害者原谅凶手”的 AI 视频而撤销判决](#item-3) ⭐️ 7.0/10
4. [Sam Altman 对 Politico 表示：世界必须接受 AI 带来的部分负面后果](#item-4) ⭐️ 6.0/10
5. [联邦上诉法院暂停明尼苏达州 AI&quot;裸化&quot;禁令](#item-5) ⭐️ 6.0/10
6. [谷歌发射首颗实验卫星，测试将人工智能送上太空](#item-6) ⭐️ 6.0/10
7. [西雅图及华盛顿州爆发抗议，呼吁暂停 AI 数据中心扩张热潮](#item-7) ⭐️ 6.0/10
8. [中国黑客冒充 Anthropic 员工窃取 AI 机密](#item-8) ⭐️ 6.0/10
9. [黄仁勋成为 AI 末日论最主要的反对方](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Simon Willison 呼吁按用量服务默认设置硬性预算上限](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) ⭐️ 7.0/10

在 2026 年 10 月 3 日发布的一篇文章中，Simon Willison 主张按用量计费的服务和 API 应当默认提供硬性预算上限——一旦达到消费阈值就直接切断服务并返回错误，而不是只发一封警告邮件的软性上限。他指出 AWS 已于 2026 年 9 月 16 日推出月度支出限额功能，项目一旦触及限额就会在当月被暂停；Google Cloud 也在 7 月推出了名为“Spend Caps”的类似功能。 AI 编程代理和个人代理大幅降低了启动代码的门槛，而这些代码往往会调用付费 API 或开通按量计费的存储与算力，因此一个失控的服务可能在一夜之间烧掉数百甚至数千美元。默认硬性上限能让按用量计费的平台对业余开发者、个人项目和小团队变得安全，并把避免天价账单的责任从用户转移到服务提供商身上。 Willison 强调这些限制必须是真正的硬性限制——只触发告警的软性上限“根本不够用”——并建议把取消上限做成一个醒目且需主动勾选的选项，勾选后用户需自行承担后续费用。他还指出，AWS 新的支出限额体验目前仍只向有限数量的客户开放，尚未对现有账户全面可用。

rss · Simon Willison · 10月3日 23:34

**背景**: 按用量计费的云服务和 API 依据实际消耗而非固定订阅收费，这意味着一个配置错误的循环、一次忘记清理的测试部署，或一个过于“勤奋”的代理都可能产生无上限的费用。过去 AWS Budgets 之类的工具只能在超过阈值后发送告警，无法真正阻止消费，许多开发者正是因为这种破产风险而对个人项目使用 AWS 心存顾虑。具备自主能力的 AI 代理进一步放大了这一风险，因为它们可以在几乎无人监督的情况下自行创建并部署会产生费用的基础设施。

**标签**: `#AI agents`, `#API billing`, `#budget caps`, `#cloud costs`, `#software engineering`

---

<a id="item-2"></a>
## [特朗普组建“超级智能力量”AI 特别工作组，Jay Clayton 领衔](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbzN5aFk5YXQ1bXNDRVBTc25iSmg1MkJXQjA3NzNlS3NrMUM2NlVXTFdNVGhZUW1ieWg3SWVrbWhaQjNhWmRNUFBYdXgtZEhBcFRMZXE1amFkeEwtcG1zaFl6NXdMN3lZWng2RTIyMzc4WVpPd1N3R0JLVnlIMTNHRA?oc=5) ⭐️ 7.0/10

特朗普总统宣布成立一个名为“超级智能力量”（Super Intelligence Force，简称 SI）的新联邦 AI 特别工作组，由国家情报总监 Jay Clayton 领导。该工作组需在 120 天内提交一份报告，评估人工智能带来的风险以及联邦政府应对该技术承担何种责任。 这标志着美国联邦政府更直接地介入 AI 政策制定，并表明华盛顿优先考虑保持先进 AI 领域的领先地位——尤其是对中国的领先——而非出台新的监管。工作组的命名和领导层安排显示，AI 监管正被框定为国家安全与情报事务，这可能重塑政府与产业界、消费者及各类利益团体的互动方式。 据报道，该工作组之所以命名为“超级智能力量”，是因为这是特朗普对 AI 偏好的称谓，其任务是协调联邦政府与消费者、公共利益团体及宗教组织的沟通。尽管外界对 AI 安全风险的担忧升温，特朗普仍拒绝出台新监管，转而支持一套包含外部安全审计和更强内部管控的自愿框架。

google\_news · CBS News · 10月4日 13:25

**背景**: 超级智能（Superintelligence）指的是智能超越最杰出人类心智的假想主体，这一概念由哲学家 Nick Bostrom 普及，并常在 AI 安全讨论中被提及。近年来，各国政府一直在权衡如何监管快速发展的 AI 系统，在创新与经济竞争力同滥用、网络威胁、安全失效等风险之间寻求平衡。美国总体上倾向于轻触式、以行业为主导的做法，而其他地区则推行更严格的规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dw.com/en/trump-ai-czar-clayton-task-force/a-79537966">Trump taps Jay Clayton as AI czar for new task force</a></li>
<li><a href="https://gizmodo.com/trump-names-national-intelligence-director-as-new-super-intelligence-czar-2000821343">Trump Names National Intelligence Director as New &#x27; Super ...</a></li>
<li><a href="https://www.straitstimes.com/world/united-states/us-ai-task-force-led-by-jay-clayton-to-report-on-technologys-risks-wsj">US AI task force to assess risks and report on super intelligence</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#government`, `#Trump`, `#superintelligence`, `#national security`

---

<a id="item-3"></a>
## [法院因播放“受害者原谅凶手”的 AI 视频而撤销判决](https://news.google.com/rss/articles/CBMinAFBVV95cUxOcU1Ia3ZTSnVXbXFnNEp6TnBlbDJUOVI5cUNvNDlXRm1NRjc5dXFkTC1CVDI2SXFkaVhlZkUzcE9Vb19pbWwzcDVWZlg0N1ROSzRrME9FWDdMVFRfdURtcFpkWWNuV2Y5SkwzN2RTeVcyVVZMS1kzcUpFcTNlODR6Q2FkcEllWlVDQzMtNVBaY3c3Y2NyaEJSUm82RHU?oc=5) ⭐️ 7.0/10

在一起杀人案的量刑程序中，有人播放了一段由 AI 生成的视频，内容是受害者原谅其凶手，法院随后撤销了该案的判决。这是已知最早因合成媒体被作为证据出示而导致量刑结果被推翻的案例之一。 此案表明深度伪造已从理论上的法庭风险变成导致司法错误的现实原因，迫使法官、检察官和辩护律师重新思考数字证据的认证方式。这很可能加速推动强制披露规则和针对 AI 生成证据的程序性保障措施，从而影响所有涉及视频、音频或图像证据的案件当事人。 这段视频极具说服力，以至于在公开庭审中被播放并影响了裁判结果，然而法院目前并没有常规使用的标准技术手段来验证视频是否为合成生成。现行可采性规则（如证据认证要求）是针对传统媒介制定的，通常并不要求当事人披露某项证据是由 AI 生成的。

google\_news · The New York Times · 10月4日 21:04

**背景**: 深度伪造（deepfake）是指由 AI 生成或篡改的图像、音频或视频，能够逼真地模仿真实人物说出或做出他们从未真正做过的事情。法院长期以来要求证据在获准采用前必须经过认证、与案件相关且可靠，而法律从业者如今被呼吁建立识别 AI 生成证据、并就真实性争议进行诉讼的框架。由于生成式视频工具变得廉价且效果逼真，法官和陪审团越来越难以区分真实的受害者陈述与伪造内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deepfake">Deepfake - Wikipedia</a></li>
<li><a href="https://legaltek.ai/blog/deepfakes-courtroom">Deepfakes Are Alreadyin Your Courtroom | LegalTek.ai</a></li>
<li><a href="https://jasonyanofski.com/blog/ai-generated-evidence-how-2025-courts-grapple-with-synthetic-text-and-images">AI-Generated Evidence : How 2025 Courts Grapple With Synthetic ...</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#deepfakes`, `#criminal justice`, `#generative AI`, `#legal tech`

---

<a id="item-4"></a>
## [Sam Altman 对 Politico 表示：世界必须接受 AI 带来的部分负面后果](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNYWFnWk90ajlEOFlsMktzU0RvSjc1cWpxRW9hb2FyZDBKR1pKanpPUE13TmpvRm5kdzY3NDN3WTZuQXB3bnVodlktZkRnS1JLR0E3NzlMR1k1aWZWUm5XUkIxSzA2Ynp0QzBwRmFZQTZGWjd6WWlOS09qbWZFM1lNYU1fTnlaMmY3?oc=5) ⭐️ 6.0/10

在接受 Politico 旗下节目 Decoded 采访时，OpenAI 首席执行官 Sam Altman 表示，为了获得人工智能带来的收益，社会应当愿意承受一些负面后果。这一表态直接勾勒出他的公司以及整个行业在 AI 系统不断普及过程中所主张的取舍逻辑。 这一表态之所以重要，是因为 Altman 领导着最具影响力的 AI 实验室之一，他的论述会影响政策制定者、监管机构和公众如何在 AI 风险与预期收益之间权衡。它直接卷入了围绕 AI 安全、监管以及 AI 造成损害时由谁负责的持续争论。 这句话更像是一句简短的访谈金句，而非详尽的政策方案；它出自媒体访谈而非正式声明，因此并未给出具体承诺、时间表，也没有界定什么程度的危害才算“可以接受”。

google\_news · Politico · 10月4日 20:55

**背景**: Sam Altman 是 OpenAI 的首席执行官，该公司开发了 ChatGPT 和 GPT 系列模型，他本人也是 AI 行业曝光度最高的发声者之一。Politico 的 Decoded 是一档访谈节目，邀请新闻人物讨论科技与政策议题。他所描述的“以部分危害换取广泛收益”的取舍，正是 AI 安全争论中的一个反复出现的主题；批评者认为，淡化风险会拖慢监管、推迟防护措施的落地。

**标签**: `#AI policy`, `#AI safety`, `#Sam Altman`, `#OpenAI`, `#tech ethics`

---

<a id="item-5"></a>
## [联邦上诉法院暂停明尼苏达州 AI&quot;裸化&quot;禁令](https://news.google.com/rss/articles/CBMioAFBVV95cUxNMENON2hETU83NHA5NHk3S2tlXzA3OGg3QkV1MjdZaG1seXZGZDlhM19McGJUZGxBNmlNT3BNYVM5M0h3MjZkSXU5SFlFQVB0Z2tiY2k4NFJ3dm1wRlNGRTZvd2dHZUZqUDF4clNaUDAzT3B1OGYwOHp3NHlET3JNS0xDNzAzcmM1b2J3bThUWUg4WHNlNzhqLVJCNThuTXZY?oc=5) ⭐️ 6.0/10

一家联邦上诉法院已暂停执行明尼苏达州针对 AI 生成&quot;裸化&quot;（nudification）图像的禁令，在相关诉讼继续进行期间暂时中止该州法律的执行。此前，埃隆·马斯克旗下 AI 公司 xAI 起诉明尼苏达州，试图阻止这项禁令生效。 这是美国首批重大案例之一，用来检验州政府能否在不违反第一修正案的前提下，直接禁止某种 AI 能力本身，而不是仅仅惩处对它的未经同意的滥用。其判决结果可能成为先例，影响其他州如何起草深度伪造与 AI 图像相关法律，并波及 AI 开发者、平台以及未经同意图像受害者等各方。 法院此举属于上诉期间的临时中止执行，而非最终推翻该法律的判决，因此如果州政府最终胜诉，禁令仍可能恢复效力。争议的核心在于：一项直接禁止相关技术本身、而不仅仅是禁止未经同意制作和传播的法律，是否构成对言论以及作为表达媒介的软件的违宪限制。

google\_news · CBS News · 10月4日 18:46

**背景**: &quot;裸化&quot;（nudification）类应用利用生成式 AI，把真人照片中的衣物数字移除，往往未经当事人同意，从而生成逼真的色情图像。明尼苏达州是美国最早将制作和传播此类 AI 合成私密图像入罪化的州之一。这类禁令让隐私与反骚扰保护，与 AI 开发者提出的言论自由主张形成对立——后者认为，措辞宽泛的法律可能连图像生成模型的合法用途也一并入罪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2kyell6WEVSRkw4V0pialUwUzNDZ0FQAQ?hl=en-GB&amp;gl=GB&amp;ceid=GB:en">Google News - Elon Musk&#x27;s xAI sues Minnesota over AI nudification ...</a></li>
<li><a href="https://arxiv.org/html/2411.09751">Analyzing the AI Nudification Application Ecosystem</a></li>
<li><a href="https://www.bloomberg.com/explainers/what-are-deepfakes">What Are Deepfakes and Nudification Apps? Can They... - Bloomberg</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#deepfakes`, `#First Amendment`, `#law`, `#Minnesota`

---

<a id="item-6"></a>
## [谷歌发射首颗实验卫星，测试将人工智能送上太空](https://news.google.com/rss/articles/CBMi4AFBVV95cUxPODdmMC1TVzBNX0VXZnV6UGNBYUUtbWxGVGpzM0FaY2JsYXN4a1FQTUdPMnE4YjdyWVN1MHE1UHVjc296bzBHX01TTW1LVXFndmJnLU93OWZ4YWVFZXRqT3J3ZEFUVFdRUTFhenBSNEdrcEhqX0dINGZIMDhRVzluNlRodWkwNmtsTTFSZzYxVEZMMm5qNnVZc3ptRV9ndEtEbVBBNmI0LXpUUUhUbnFTbGJVNWNrZXJWVDJjU2RZTHVFNUwwNHFrNEpIR3ZBTHZUWHExTktDcXhNVEJ0bm1PTg?oc=5) ⭐️ 6.0/10

据 Noticias Ambientales 报道，谷歌发射了其首颗实验卫星，用于测试能否在太空中直接运行人工智能。该任务被定位为一次实验而非商业服务，目标是验证 AI 工作负载能否在轨道环境中运行。 如果 AI 推理能够在轨道上稳定运行，卫星就可以在轨分析图像和传感器数据，而不必把所有原始数据都传回地面，从而降低延迟和带宽成本。这也是谷歌将 AI 算力从地面数据中心向外延伸的又一步，契合整个行业向边缘计算发展的趋势。 目前公开的报道内容较为简略：未说明运载火箭、发射日期、轨道、卫星平台，以及星上搭载的具体 AI 模型和处理器。这类任务的核心工程难点在于，太空硬件必须抗辐射，并且要在严格的功耗、热控和质量预算内工作，这通常意味着无法直接使用标准的数据中心加速器。

google\_news · Noticias Ambientales · 10月4日 18:06

**背景**: 边缘计算是一种分布式计算模式，它把计算和数据存储放到数据产生的地方附近，而不是把所有数据都送到集中式的云数据中心，通常与物联网联系在一起。把 AI 应用于航天技术，是指在卫星、航天器和任务运营中嵌入 AI 算法，使其能够自主决策并高效处理数据，无需等待与地面站之间的往返通信。传统卫星一般把原始数据下传，依赖地面进行处理，这种方式速度慢，且受通信窗口限制。谷歌此次实验正是对“能否把处理过程放到轨道上完成”的早期验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Edge_computing">Edge computing</a></li>
<li><a href="https://grokipedia.com/page/AI_in_Space_Technology">AI in Space Technology</a></li>

</ul>
</details>

**标签**: `#AI`, `#Space Tech`, `#Google`, `#Satellite`, `#Edge Computing`

---

<a id="item-7"></a>
## [西雅图及华盛顿州爆发抗议，呼吁暂停 AI 数据中心扩张热潮](https://news.google.com/rss/articles/CBMirwFBVV95cUxPYzZzb2VPdWlkc2NDa2k2Mzhnb3VmRG1sTnhjUzFvVDd1bklSd0hGeFBwNGtRTVp1aGhYdHNfX1dBUWU5cHNTd1g2RElxUGFNZ0pGQ21ZU1dzRVBXeHdTUGNydERjLVUyLVFXTXdxSnQ4aTkzdTZGUTZqMDl1a01BRUVyUXVYT0htMVN4M3NIV2dHV0lhOWdjeDAwb3FLOVhVcWdoX0MtU25QTmNXenZ3?oc=5) ⭐️ 6.0/10

西雅图及华盛顿州多地爆发抗议活动，呼吁暂停 AI 数据中心的快速建设，理由是当地对基础设施压力和能源消耗的担忧。这些示威凸显出地方社会对 AI 热潮“实体足迹”的组织化抵制，而非针对 AI 模型本身。 这场抗议是美国各地反对 AI 数据中心建设的浪潮之一，据报道到 2026 年年中，此类地方阻力已导致价值约 1300 亿美元的项目被阻止。对科技公司、电力公司和电网规划者而言，地方审批与民意正变得与芯片供应和资本同等关键，直接决定 AI 算力究竟能建在哪里。 面向 AI 的数据中心每个服务器机架通常耗电约 60 千瓦，而通用数据中心约为 10 千瓦，同时冷却还需消耗大量水资源，并产生热量与噪音。所提供的报道内容本身没有任何技术细节、金额数字或具体政策诉求，因此抗议的规模以及是否提出了具体的监管方案仍不明确。

google\_news · The Seattle Times · 10月4日 22:45

**背景**: AI 数据中心是为训练和运行 AI 模型而专门优化的设施，依赖 GPU、TPU 等 AI 加速器以及高速互联，因此耗电量远高于普通数据中心。随着 2020 年代 AI 热潮加速，各公司争相建设此类设施，大型科技公司据估计仅在 2026 年就将投入约 6500 亿美元；据称该财年全球约 70%的计算机内存产量被 AI 数据中心买走。由于这类设施需要大量电力与水资源，并会影响当地土地利用、噪音和空气质量，美国许多社区已开始组织起来反对在本地区建设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_data_center">AI data center</a></li>
<li><a href="https://grokipedia.com/page/Power_in_AI_Data_Centers">Power in AI Data Centers</a></li>

</ul>
</details>

**标签**: `#AI data centers`, `#policy`, `#infrastructure`, `#energy`, `#Seattle`

---

<a id="item-8"></a>
## [中国黑客冒充 Anthropic 员工窃取 AI 机密](https://news.google.com/rss/articles/CBMimAFBVV95cUxOVGlSM2lMaWg5Ym1HS3gxSXNMaC1raEUyUm5TdkgtOTY4ak5NNm9tMTRydmlRRTFfQ01sOGtLWUpNQ25oVzJrckMwQU5fb3hrQUhDRDhOeFJvamdjNVF4VmRfSk0wS0prZkx0MlNNQjUxdW9jV0hBTTlTWkZOZXZya0Vfc3RMVmtPeHV5dURneFpsWmNSQ1B6LQ?oc=5) ⭐️ 6.0/10

据 Futurism 报道，疑似与中国有关的黑客冒充 Anthropic 公司员工，试图套取该公司的 AI 机密信息。该事件被描述为一次针对这家 AI 公司的社会工程式行动，而非纯粹依靠技术手段的网络入侵。 这一事件表明，AI 实验室正因其掌握的模型权重、研究路线图和专有训练数据而成为高价值的情报窃取目标。它也说明 AI 安全中最薄弱的一环往往不是代码而是人与人之间的信任，可能促使 AI 企业加强身份验证与内部威胁防护。 目前可获得的信息缺少技术细节：报道并未确认攻击者具体想获取哪些信息、冒充行为是否得逞，也未说明他们是如何接触目标的。涉及时间范围、具体冒充手段（例如电子邮件、即时通讯软件或电话）以及归因证据等细节，在现有材料中均未得到证实。

google\_news · Futurism · 10月4日 20:03

**背景**: Anthropic 是一家以开发 Claude 系列大语言模型而闻名的 AI 安全公司，属于少数处于前沿的 AI 实验室之一，其内部研究和模型权重具有极高价值。冒充他人（即社会工程）是一种经典的情报手段，攻击者伪装成可信的同事、供应商或高管，诱使员工交出凭据或机密资料。近年来，国家支持的黑客组织越来越多地盯上 AI 与半导体企业，因为 AI 技术的进步被认为在经济和军事竞争中都具有战略意义。

**标签**: `#AI security`, `#cybersecurity`, `#Anthropic`, `#hacking`, `#espionage`

---

<a id="item-9"></a>
## [黄仁勋成为 AI 末日论最主要的反对方](https://news.google.com/rss/articles/CBMif0FVX3lxTE9VX2xQSnFmUmlVT193Tk12UThLN0VzWGNyRFNHLUVBT0pMQzJiNm9FZW1LQlBwN3o1am81NlFCZGxoZFA0dlpTMGlmaGI2eGUxdnh2QVY3Z0QzQUN5WUIzcG1XT2d1U1NmekhFNHRuUk9qSF9xSkpjbG1CdzIxWjQ?oc=5) ⭐️ 6.0/10

《财富》杂志报道称，英伟达 CEO 黄仁勋已成为业界反对“AI 末日论”最突出的声音——该观点认为先进人工智能会对人类构成生存性风险。文章将他描述为科研人员与 AI 安全倡导者所持警告的主要制衡者，这些人担心超级智能系统可能脱离人类控制。 英伟达供应了用于训练和运行前沿 AI 模型所需的绝大多数 GPU，因此黄仁勋的公开立场在“AI 发展应被多严格监管或暂停”的政策争论中分量极重。他的表态凸显出算力供应方与 AI 安全研究者之间的明显分歧：前者从快速落地部署中获益，后者则主张谨慎、放慢并更可控地扩展模型规模。 《财富》这篇文章属于评论与分析，而非技术或产品发布，也没有提出任何新的英伟达硬件、基准测试或政策承诺。其关注点在于这场争论本身的框架设定，即由谁来定义 AI 风险，而非关于模型能力或安全性的新证据。

google\_news · Fortune · 10月4日 12:00

**背景**: AI 末日论通常指这样一种信念：人工智能的持续进步可能导致人类灭绝，或使人类永久丧失对技术的控制权；这一立场与 Geoffrey Hinton、Eliezer Yudkowsky 等研究者以及“AI 安全中心”（Center for AI Safety）等组织相关，后者曾在 2023 年发布简短声明警告 AI 带来的灭绝风险。英伟达之所以处于这场争论的中心，是因为其数据中心 GPU（包括 H100 以及更新的 Blackwell 系列）几乎是所有主要 AI 实验室构建更大模型所依赖的稀缺资源。黄仁勋的论点通常把 AI 描绘成提升生产力和推动科学的工具，其收益超过那些推测性的灾难性风险，这与英伟达希望 AI 持续快速扩张的商业利益相一致。

**标签**: `#AI safety`, `#Jensen Huang`, `#Nvidia`, `#AI doomerism`, `#existential risk`

---