---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21 23:02:33 +0000
lang: zh
report: default
---

> 从 41 条内容中筛选出 9 条重要资讯。

---

1. [浙江大学在超导芯片上首次真机实现 QRAM](#item-1) ⭐️ 9.0/10
2. [台积电暂停对中国企业 16nm 及以下芯片订单](#item-2) ⭐️ 8.0/10
3. [微软在 Windows 上实现 RDMA over USB4，多台 PC 可合力跑本地 AI 模型](#item-3) ⭐️ 8.0/10
4. [口服 daraxonrasib 联合化疗一线治疗胰腺癌缓解率达 60.7%](#item-4) ⭐️ 8.0/10
5. [OpenAI 强化反蒸馏防护，推理链提取成功率降至 0.2%](#item-5) ⭐️ 7.0/10
6. [OpenRouter 警告 MiniMax 模型提示词疑遭第三方读取](#item-6) ⭐️ 7.0/10
7. [特朗普提议对在海外建 AI 数据中心的美国企业征税](#item-7) ⭐️ 6.0/10
8. [Debian 维护者组建游戏硬件团队，拟推专用游戏发行版](#item-8) ⭐️ 6.0/10
9. [国家数据局将健全词元计量计费与质量测评标准](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [浙江大学在超导芯片上首次真机实现 QRAM](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 9.0/10

浙江大学超导量子计算团队在自主研制的“天目 2 号”超导量子芯片上，首次在真机上实现量子随机存储器（QRAM），成果发表于《自然·物理》。芯片上运行的原型分别完成了 4 位和 8 位数据调取，准确率为 80.9%和 60.4%，线路深度较未优化方案降低 30%以上，并首次实验验证了该架构的局部抗噪特性。 QRAM 是许多需要在叠加态下读取数据的量子算法所急需的组件，此次硬件演示使其从理论方案走向可实验检验的构建模块。如果该方案能够扩展，它将有望支撑量子机器学习、量子数据库搜索等数据密集型量子应用，不过当前原型规模仍然很小且准确率有限。 报告显示，4 位原型的调取准确率为 80.9%，而 8 位版本降至 60.4%，说明随着地址位宽增加，准确率会下降。团队还称线路深度较未优化实现降低 30%以上，并首次验证了局部抗噪特性，下一步将推进 QRAM 的规模化研究。

telegram · zaihuapd · 11月21日 08:31

**背景**: 量子随机存储器（QRAM）是经典随机存储器的量子对应物：它允许量子计算机用处于叠加态的地址从存储阵列中读取数据，从而有可能并行访问多个存储单元。QRAM 的建造难度很大，因为所需量子线路较深且容易出错，因此此前多数工作停留在理论或小规模阶段。“天目 2 号”是浙江大学超导量子计算团队研制的超导量子芯片，而超导量子比特是目前量子计算的主流技术路线之一。此次发表于《自然·物理》的成果，是迈向实用量子存储器的重要实验进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2305.10310v1">QRAM : A Survey and Critique</a></li>
<li><a href="https://baike.baidu.com/en/item/Tianmu-2/4929794">Tianmu-2_Baiduwiki - 百度百科</a></li>
<li><a href="https://arxiv.org/pdf/2012.05340">Resilience of quantum random access memory to generic noise</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#quantum hardware`, `#Nature Physics`

---

<a id="item-2"></a>
## [台积电暂停对中国企业 16nm 及以下芯片订单](https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls) ⭐️ 8.0/10

据 AppleInsider 报道，台积电已通知客户暂停承接中国企业的 16nm 及以下先进制程订单。按照收紧后的美国半导体出口新规，除非事先取得美国出口许可或豁免，否则台积电不得供货；此前台积电可自行评估客户设计是否符合豁免条件的做法也已终止。 此举实质上把中国芯片设计公司限制在 28nm、40nm 等旧制程，使其无法获得 AI 数据中心加速器所需的前沿工艺与高带宽内存。这是美国出口管制首次如此明确地在晶圆厂接单环节落地执行，将直接影响中国的 AI 硬件路线图与全球供应链。 据报道，中国企业只能使用 28nm、40nm 等旧制程，无法获得 AI 数据中心硬件所需的高带宽内存（HBM）。美国获批名单中有苹果、AMD、英伟达，尚无中国公司，台积电则表示将遵守新规。

telegram · zaihuapd · 11月21日 02:01

**背景**: 16nm、28nm、40nm 这类“制程节点”指的是芯片的制造世代：数字越小通常意味着晶体管密度更高、性能更好、功耗更低，因此 16nm 及以下集中了绝大多数先进逻辑芯片，而 28nm、40nm 属于成熟、廉价的制程。高带宽内存（HBM）是由三星、AMD 和 SK 海力士开发、并于 2013 年被 JEDEC 采纳的 3D 堆叠 DRAM 标准，常与 GPU、FPGA 和 AI 加速器配合使用，为成千上万个核心提供巨大带宽。由于台积电生产 HBM 的基础裸片（base die），并且是多家存储厂商的关键代工伙伴，晶圆厂层面的限制会沿着整个 AI 硬件栈层层传导，而不只是影响某一款芯片设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory</a></li>
<li><a href="https://semiconductorx.com/mfg-process-nodes.html">Semiconductor Process Nodes: Names, Transistors and Who Makes ...</a></li>
<li><a href="https://semiengineering.com/knowledge_centers/manufacturing/process/nodes/">Nodes - Semiconductor Engineering</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#TSMC`, `#export-controls`, `#China`, `#AI-hardware`

---

<a id="item-3"></a>
## [微软在 Windows 上实现 RDMA over USB4，多台 PC 可合力跑本地 AI 模型](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

微软发布了 Windows 平台的 RDMA over USB4 开发者预览版，多台 PC 只需用普通 USB4 线缆连接即可共享内存与 GPU 算力，无需专用网卡或交换机就能共同运行同一个本地 AI 大模型。在演示中，三台搭载 AMD Ryzen AI Max+ 395 的机器以 4-bit 量化方式运行 Qwen3-235B-A22B，速度约为 18.5 token/s，该功能将通过 Windows Insider 渠道推送。 这大幅降低了分布式本地推理的硬件门槛：用户和小型团队不必购买数据中心级互联设备，只要把消费级机器凑在一起，就能运行远超单机内存容量的大模型。这也表明微软正把普通 Windows PC 视为可松散组网的 AI 集群，可能改变本地大模型负载的规划方式。 该方案依托 USB4 的高速链路（信号速率为 20/40/80 Gbit/s）承载 RDMA 流量，因此性能与兼容性取决于线缆、接口和驱动的质量，而非成熟的网络交换架构。它目前仍是开发者预览版，且演示中 235B 参数混合专家模型约 18.5 token/s 的吞吐是在 4-bit 量化下取得的，并非全精度推理。

telegram · zaihuapd · 11月21日 06:13

**背景**: RDMA（远程直接内存访问）允许一台机器直接读写另一台机器的内存，绕过 CPU 和操作系统，从而实现低延迟与高带宽，是 AI 训练集群高速互联的基础。USB4 是最新的 USB 标准，基于 Thunderbolt 3 协议，可在 USB-C 接口上以最高 80 Gbit/s 隧道传输 PCI Express、DisplayPort 和 USB 流量。Qwen3-235B-A22B 是阿里巴巴推出的 2350 亿参数混合专家模型，激活参数约 220 亿，单次计算量不大，但整体体积远超普通消费级单卡显存容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://habr.com/ru/articles/1110636/">Microsoft представила решение на базе USB4 и RDMA для... / Хабр</a></li>
<li><a href="https://en.wikipedia.org/wiki/USB4">USB4</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3-235B-A22B">Qwen/Qwen3-235B-A22B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#RDMA`, `#USB4`, `#Windows`, `#Local AI`, `#Distributed Inference`

---

<a id="item-4"></a>
## [口服 daraxonrasib 联合化疗一线治疗胰腺癌缓解率达 60.7%](https://event.eortc.org/ena2026/2026/11/20/metastatic-pancreatic-cancer-responds-well-to-initial-treatment/) ⭐️ 8.0/10

11 月 20 日，在巴塞罗那举行的 EORTC-NCI-AACR（ENA 2026）大会上，研究者以 late-breaking 口头报告形式公布了一项单臂 I/II 期研究数据：61 例既往未治疗的转移性胰腺导管腺癌患者接受口服 daraxonrasib 200 mg 每日一次联合吉西他滨/白蛋白紫杉醇治疗。结果显示确认客观缓解率 60.7%、完全缓解率 8.2%（约十二分之一）、疾病控制率 90.2%、中位无进展生存 12.8 个月，中位随访 18.3 个月时 12 个月总生存率为 76.6%。 转移性胰腺癌是最致命的实体瘤之一，除细胞毒化疗外有效选择极少，因此一线治疗中出现如此幅度的缓解信号立刻引发关注；加之 daraxonrasib 已基于 III 期总生存获益获 FDA 批准（商品名 RASONQUE）用于既往治疗后的患者。不过，该研究为无化疗对照的单臂设计，尚不能称为改变临床实践，结论仍需正在进行的 III 期研究验证。 主要研究者明确提醒，疗效对比必须依靠正在进行的 III 期研究来回答；化疗的历史 1 年生存率参照区间为 22%–48%（MPACT 试验 35%，mFOLFIRINOX 48%），因此 76.6% 这一数字不宜简单表述为「远高于化疗」。机制上，daraxonrasib 是一种口服 RAS\(ON\) 多选择性抑制剂，通过三复合物机制作用于活跃态 RAS，覆盖多种 KRAS/NRAS 突变，而非像 G12C 选择性药物那样只针对单一突变亚型。

telegram · zaihuapd · 11月21日 11:24

**背景**: RAS 蛋白是胰腺癌中最常见的致癌驱动因素，绝大多数肿瘤携带 KRAS 突变，但多年来只有针对 KRAS G12C 的选择性抑制剂可用，且仅覆盖很小一部分患者。RAS\(ON\) 多选择性抑制剂是较新的一类药物，通过结合处于活性（GTP 负载）状态的 RAS，力求覆盖多种 KRAS 与 NRAS 变异；daraxonrasib（原代号 RMC-6236）是该类药物的代表性临床品种。该药已于 8 月 26 日获 FDA 批准，商品名 RASONQUE，用于既往治疗后的患者，依据是 III 期 RASolute 302（RMC-302）研究中位总生存 13.2 个月对标准化疗 6.7 个月的结果。此次公布的新数据则将该药与化疗联合推进到一线治疗场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hcp.rasonque.com/ras-on/moa">Mechanism of action | RASONQUE™ (daraxonrasib) | HCP</a></li>
<li><a href="https://ascopubs.org/doi/10.1200/JCO.2025.43.16_suppl.TPS4230">Trial in progress: RASolute 302—A phase 3, multicenter ...</a></li>
<li><a href="https://www.mskcc.org/cancer-care/clinical-trials/24-363">A Phase 3 Study of RMC-6236 versus Standard Therapy for ...</a></li>

</ul>
</details>

**标签**: `#pancreatic cancer`, `#oncology`, `#KRAS inhibitor`, `#clinical trial`, `#daraxonrasib`

---

<a id="item-5"></a>
## [OpenAI 强化反蒸馏防护，推理链提取成功率降至 0.2%](https://openai.com/index/combatting-adversarial-distillation/) ⭐️ 7.0/10

OpenAI 于 11 月 20 日发文详细介绍其针对「对抗性蒸馏」的防御措施，称在 GPT-6.2 Astra 与 Sol 上，红队测试中从历史请求中提取推理内容的成功率已从 54.0% 降至 0.2%。OpenAI 同时表示，每周会对数千至数万个蒸馏账号采取执法行动。 蒸馏是前沿实验室失去对专有能力控制的主要途径之一，而成功率下降约两个数量级说明这类防御正变得真正有效。从单纯依靠模型侧加固转向叠加账号层面的主动执法，将影响所有通过 OpenAI API 训练或微调竞品的开发者，并可能成为其他实验室效仿的先例。 OpenAI 称其采取分层策略，将模型训练、安全防护、检测与执法结合起来，并曾就 DeepSeek 疑似蒸馏行为向美国国会汇报。但 54.0% 至 0.2% 这一数据来自 OpenAI 自建的红队测试环境，尚未经过独立验证，文章也未说明具体测试了哪些提取手法或多大的查询量。

telegram · zaihuapd · 11月21日 01:30

**背景**: 知识蒸馏通常指用一个较小的「学生」模型去学习较大「教师」模型的输出，是一种合法且被广泛使用的能力压缩技术。对抗性蒸馏则是未经授权的版本：攻击者大规模调用专有模型，收集其回答与思维链推理内容，再据此训练竞品模型。由于推理模型会输出很长的中间推理过程，单次查询泄露的信息远多于普通回答，这正是各实验室如今重点加固这一环节的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/reasoning-extraction-attacks">Reasoning Extraction Attacks - emergentmind.com</a></li>
<li><a href="https://arxiv.org/html/2603.07835">DistillGuard: Evaluating Defenses Against LLM Knowledge Distillation</a></li>
<li><a href="https://arxiv.org/abs/2506.14374">[2506.14374] Excessive Reasoning Attack on Reasoning LLMs Break-The-Chain: Reasoning Failures in LLMs via Adversarial ... A Survey on Model Extraction Attacks and Defenses for Large ... (PDF) A Survey on Model Extraction Attacks and Defenses for ... Excessive Reasoning Attack on Reasoning LLMs - OpenReview Stepwise Reasoning Disruption Attack of LLMs - ACL Anthology</a></li>

</ul>
</details>

**标签**: `#AI model security`, `#adversarial distillation`, `#OpenAI`, `#model extraction`, `#IP protection`

---

<a id="item-6"></a>
## [OpenRouter 警告 MiniMax 模型提示词疑遭第三方读取](https://news.ycombinator.com/item?id=50585962) ⭐️ 7.0/10

OpenRouter 已通知用户，发往 MiniMax 模型的提示词可能已被第三方读取：安全研究者在 2026 年 7 月至 10 月间把带有唯一标识的测试 URL 放进提示词，结果这些 URL 在 40 到 130 小时后被第三方访问。OpenRouter 已下架受影响端点的「零数据保留」（ZDR）标签，并建议可能泄露敏感凭证的用户更换 API Key 和密码。 「零数据保留」承诺正是企业敢把专有代码、客户数据和内部文档发给第三方推理服务商的前提，因此这一承诺被打破，受损的不只是一个模型，而是整条模型路由层的信任基础。任何曾通过 OpenRouter 把机密材料发往 MiniMax 端点的用户，都应假定这些提示词已被记录，并可能被预期之外的服务商链条看到。 问题被归因于 MiniMax 及其转发/转售其推理能力的中介方 AtlasCloud、Novita 和 StreamLake，而 OpenRouter 官网目前尚未发布相关公告。该检测方法值得注意，因为它依据的是行为而非日志：为每条提示词生成唯一 URL，无需服务商配合即可发现后续访问，而 40 到 130 小时的延迟说明数据被持久化存储，而非仅在内存中短暂处理。

telegram · zaihuapd · 11月21日 06:53

**背景**: OpenRouter 是一个模型路由与聚合平台，开发者通过一个兼容 OpenAI 的 API 就能调用众多模型，请求会被转发到最便宜或最快的基础服务商。零数据保留（ZDR）指服务商在推理结束后不存储提示词和响应，这也意味着其无法用这些数据训练模型；OpenRouter 允许用户全局、按模型组或按单次请求强制启用 ZDR，使流量只流向声明该策略的端点。由于包括 MiniMax 在内的许多模型不仅由模型开发方提供，也由第三方推理服务商和转售商提供，ZDR 标签实际上是一串层层传递的保证，其可靠性取决于链条中最薄弱的一环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/docs/guides/features/zdr">Zero Data Retention - How OpenRouter gives you control over ...</a></li>
<li><a href="https://openrouter.ai/blog/insights/zero-data-retention/">Zero Data Retention (ZDR): What It Means for AI APIs</a></li>
<li><a href="https://www.piiblock.com/blog/openrouter-zero-data-retention">Zero Data Retention on OpenRouter, and how to check the claim</a></li>

</ul>
</details>

**标签**: `#security`, `#privacy`, `#LLM APIs`, `#data-retention`, `#OpenRouter/MiniMax`

---

<a id="item-7"></a>
## [特朗普提议对在海外建 AI 数据中心的美国企业征税](https://apnews.com/article/trump-artificial-intelligence-data-centers-f1ac03b73d13445400eeed8631d9d879) ⭐️ 6.0/10

当地时间 11 月 20 日，美国总统特朗普在白宫记者会上表示，计划对在美国境外建设 AI 数据中心的美国科技公司征收“巨额税款”，并称尚未向政府内部官员透露这一计划。他还敦促全美各地社区接纳数据中心，建议社区与开发商谈判，争取由开发商向社区付款。 这一表态为微软、谷歌、亚马逊和 Meta 等美国超大规模云厂商带来了新的潜在政策风险——这些公司正全球范围扩张 AI 算力，倾向于选择电力与土地更便宜、审批更快的地点。若最终转化为实际税收政策，可能改变未来 AI 数据中心的选址格局，并成为中美在 AI 基础设施竞争中的新战线。 目前该提议仅停留在口头表态层面，尚未披露税率、法律机制、适用范围或时间表，特朗普还称尚未向政府内部官员透露该计划。他同时施压地方社区接纳数据中心，并建议与开发商谈判争取付款，而当前全美多地社区正因用电需求和噪音问题反对新建项目。

telegram · zaihuapd · 11月21日 03:26

**背景**: AI 模型的训练与推理依赖部署在数据中心内的大规模 GPU 集群，这些设施需要消耗大量电力、土地和冷却水。由于美国电网接入和建设审批往往需要数年时间，科技公司越来越多地转向其他国家寻求更便宜的电力与更快的审批。特朗普多次将 AI 基础设施视为与中国竞争中的国家安全和竞争力议题，这使得数据中心的选址从单纯的商业决策变成了政策问题。

**标签**: `#AI infrastructure`, `#data centers`, `#policy regulation`, `#US-China AI competition`, `#Trump administration`

---

<a id="item-8"></a>
## [Debian 维护者组建游戏硬件团队，拟推专用游戏发行版](https://www.ithome.com/1/030/390.htm) ⭐️ 6.0/10

Debian 维护者 Karamtoth 组建了「Debian 游戏硬件团队」，将测试包括游戏掌机、模拟器设备和家用主机在内的游戏硬件，并探索让 Debian 在这些设备上运行。该团队还计划推出面向硬件集成商与爱好者的专用版本，装好系统后即可直接进入游戏模式。 Debian 约两年一次的大版本节奏和对新硬件的保守支持，长期把游戏用户推向 Fedora 系和 Arch 系的游戏发行版，因此官方的游戏方向尝试有望让 Debian 成为真正的替代选择。由于 Ubuntu、Mint 等大量发行版都衍生自 Debian，这里产出的兼容性修复与文档可能惠及整个 Linux 生态的很大一部分。 该计划看起来会先从测试和记录硬件兼容性与问题入手，再推进提交补丁和修复，而不是立刻交付成品。面向集成商的游戏专用版本尚未公布发布时间表或正式范围，而且该团队属于社区自发行动，并非 Debian 官方发布项目。

telegram · zaihuapd · 11月21日 09:10

**背景**: Debian 是历史最悠久的社区运营 Linux 发行版之一，以志愿者治理、长期稳定性和对自由软件的严格立场著称，Ubuntu、Linux Mint 等众多流行发行版都构建在其之上。Debian 大约每两年发布一个稳定大版本，这意味着对新芯片和外设的支持往往来得较晚。与此同时，Linux 游戏生态近年快速成熟，专用游戏发行版通常基于 Fedora 或 Arch，因为这些发行版能提供更新的内核、驱动和图形栈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gamingonlinux.com/2026/11/debian-linux-forms-a-debian-gaming-hardware-team-for-testing-handhelds-and-consoles/">Debian Linux forms a Debian Gaming Hardware... | GamingOnLinux</a></li>
<li><a href="https://www.techpowerup.com/355046/debian-linux-forms-gaming-hardware-team-for-handheld-and-bleeding-edge-hardware-testing">Debian Linux Forms Gaming Hardware Team for... | TechPowerUp</a></li>
<li><a href="https://itsfoss.com/linux-gaming-distributions/">11 Best Linux Gaming Distributions in 2025</a></li>

</ul>
</details>

**标签**: `#Debian`, `#Linux gaming`, `#Linux distributions`, `#handheld gaming`, `#open source`

---

<a id="item-9"></a>
## [国家数据局将健全词元计量计费与质量测评标准](https://www.cls.cn/detail/2540805) ⭐️ 6.0/10

2026 年 11 月 20 日，国家数据局局长刘烈宏在湖南长沙举行的 2026 世界计算大会开幕式上表示，词元打通了算力、模型、数据间的价值传导链路，已成为数智经济的价值锚点。他表示，国家数据局下一步将拓展词元服务应用场景，健全词元计量计费、质量测评等标准规范，避免低质量重复建设。 如果国家数据局将这一表态落地为正式标准，词元消耗量有望成为国内 AI 服务定价与评价的事实性统一单位，从而影响云厂商、模型厂商与企业客户对模型及 API 用量的计费方式与横向比较方式。这也释放出监管层将词元生产视为需要规范的基础设施、而非纯市场化自由竞争的信号，可能重塑 AI 服务商的定价、采购与准入门槛。 目前这只是一则简短的政策表态，尚未公布标准草案、时间表、计量指标定义或执行机制，因此质量测评具体如何衡量仍不明确。此番表述的核心是“词元工厂”——将算力租赁、模型供给与数据能力打包为词元生产服务——这意味着相关标准可能不仅涉及应用层计费，还会覆盖算力提供方与模型厂商。

telegram · zaihuapd · 11月21日 10:19

**背景**: 词元（Token）是大语言模型处理与生成文本的基本单位，中文定名“词元”是在“令牌”“智元”等译法之争后确定下来的，其背景之一是计费模式正从按席位、按年采购转向按词元消耗量计费。所谓“词元工厂”，是一种较新的基础设施概念，指数据中心与 AI 平台厂商把异构算力、模型调度与推理优化打包，把词元作为产出品来销售。中国已开始围绕这一概念布局政策：2026 年 9 月，北京市经济和信息化局与市发展改革委联合印发全国首个省级词元经济专项政策《北京市加快词元经济发展的行动方案（2026—2028 年）》，围绕词元生产、质量评测、分发流通与场景应用作出部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.drc.gov.cn/DocView.aspx?chnid=379&amp;leafid=1338&amp;docid=2909986">陈波：加快构建词元质量评价标准体系 - 国务院发展研究中心</a></li>
<li><a href="https://baike.baidu.com/item/%E8%AF%8D%E5%85%83%E8%B4%A8%E9%87%8F%E8%AF%84%E4%BB%B7%E6%A0%87%E5%87%86%E4%BD%93%E7%B3%BB/68095458">词元质量评价标准体系 - 百度百科</a></li>
<li><a href="https://developer.volcengine.com/articles/7626208860692611078">告别“令牌”与“智 元 ”之争，“ 词 元 ”定名背后的140...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#tokenization`, `#China tech regulation`, `#AI infrastructure`, `#standards`

---