---
layout: default
title: "Horizon Summary: 2026-07-31 (ZH)"
date: 2026-07-31
lang: zh
report: default
---

> 从 400 条内容中筛选出 10 条重要资讯。

---

1. [字节跳动发布 Seedance 2.5，单次生成 30 秒视频](#item-1) ⭐️ 8.0/10
2. [DeepSeek 上线 V4-Flash 正式版 API 公测，Agent 能力大幅增强](#item-2) ⭐️ 8.0/10
3. [华为开源 505B 参数 MoE 大模型 openPangu-2.0-Pro](#item-3) ⭐️ 8.0/10
4. [美法官质疑 Anthropic 供应链风险认定，或永久撤销禁令](#item-4) ⭐️ 8.0/10
5. [MiniMax 多模态视频模型 H3 将于 8 月 3 日开源](#item-5) ⭐️ 8.0/10
6. [德国法院裁定 AI 音乐公司 Suno 侵犯版权](#item-6) ⭐️ 8.0/10
7. [卫健委通报第五批涉&\#x27;论文工厂&\#x27;科研失信案件，共 21 起](#item-7) ⭐️ 6.0/10
8. [特朗普政府拟向留学生征收 10 万美元毕业后工作费](#item-8) ⭐️ 6.0/10
9. [美团联合苏州上线外卖骑手“等灯停表”](#item-9) ⭐️ 6.0/10
10. [YouTube 以涉性内容政策封禁多名 ASMR 创作者](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [字节跳动发布 Seedance 2.5，单次生成 30 秒视频](https://seed.bytedance.com/zh/blog/%E4%B8%80%E9%95%9C%E6%88%90%E7%89%87-%E9%9A%8F%E5%BF%83%E5%8F%82%E8%80%83-seedance-2-5-%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83) ⭐️ 8.0/10

字节跳动于 7 月 31 日正式发布 Seedance 2.5，将单次生成视频时长从 15 秒提升至 30 秒。该模型还支持多轮延长以生成数分钟连贯视频，单次输入最多可接受 30 张图片、10 段视频及 10 段音频作为参考素材。 Seedance 2.5 将当前 AI 视频模型的单次生成时长提升了一倍，并引入强大的多模态参考控制，可显著改善创作流程和画面真实度。它陆续上线即梦 AI、豆包专业版及火山方舟 API，并在教育、工业仿真、具身智能和自动驾驶等领域落地，显示字节跳动正力争领跑 AI 视频生成市场。 Seedance 2.5 可单次生成原生 30 秒 4K 视频，并支持通过时间戳精准控制画面与节奏。该模型已陆续上线字节跳动旗下多款产品，API 服务也将于近期接入火山方舟。

telegram · zaihuapd · 7月31日 04:16

**背景**: AI 视频生成模型通常只能生成几秒至 15 秒的短片，往往需要拼接才能形成更长的场景。Seedance 2.5 是字节跳动最新推出的视频生成模型，在 2026 年火山引擎 FORCE 大会上发布，可原生输出 30 秒片段。多模态参考输入——使用图片、视频、音频或 3D 资产作为锚点——有助于创作者在多次生成中保持角色和场景的一致性。字节跳动还宣布了在具身智能和自动驾驶等领域的应用，这些领域可利用 AI 生成合成数据来支持训练和仿真。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">One-take Creation, Flexible Referencing: Introducing Seedance 2 . 5</a></li>
<li><a href="https://seeddance.ai/seedance-2-5">Seedance 2 . 5 — Native 30s 4K AI Video with 50... | SeedDance</a></li>
<li><a href="https://dreamina.capcut.com/seedance/seedance-2-5">Official Seedance 2 . 5 : 4K &amp; 30s AI Video Generator</a></li>

</ul>
</details>

**标签**: `#video generation`, `#ByteDance`, `#AI model`, `#multimodal`, `#Seedance`

---

<a id="item-2"></a>
## [DeepSeek 上线 V4-Flash 正式版 API 公测，Agent 能力大幅增强](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 8.0/10

2026 年 7 月 31 日，DeepSeek 上线 V4-Flash 正式版 API 公测。该版本原生支持 Responses API 格式并针对 Codex 做了适配，基准测试成绩远超 V4-Pro-Preview。 此次公测标志着 DeepSeek 在面向 Agent 的模型服务方向上迈出重要一步，可能扩大其企业开发者基础。在 Terminal Bench 2.1 等 Agent 基准上的显著提升，有望使 DeepSeek 在 AI Agent 基础设施竞争中占据更有利位置。 模型结构与尺寸与 V4-Flash-preview 保持一致，仅重新进行了后训练。此次仅升级 V4-Flash 的 API 接口，V4-Pro API 及 APP/WEB 端未做更改，V4-Pro 正式版将尽快发布；公告还提到测试使用了即将发布的 DeepSeek Harness 极简模式。

telegram · zaihuapd · 7月31日 05:50

**背景**: Terminal-Bench 2.1 是一个开源基准测试，用于检验模型在沙盒终端环境中完成任务的能力，包含从模型训练到系统管理共 89 项任务。CyberGym 是 UC Berkeley 推出的大规模网络安全评估框架，用于评估 AI Agent 能否在 C/C++ 代码中发现真实的内存安全漏洞并处理现实漏洞分析。DSBench 包含来自 Eloquence 和 Kaggle 竞赛的 466 个数据分析任务和 74 个数据建模任务，为评估数据科学 Agent 提供真实场景。DeepSeek 报告在这些基准上分别取得 82.7（Terminal Bench 2.1）、76.7（Cybergym）、68.7（DSBench-FullStack）和 59.6（DSBench-Hard）的成绩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tbench.ai/benchmarks/terminal-bench-2-1">Terminal-Bench 2.1 benchmark</a></li>
<li><a href="https://github.com/sunblaze-ucb/cybergym">GitHub - sunblaze-ucb/cybergym: CyberGym is a large-scale, high-quality cybersecurity evaluation framework designed to rigorously assess the capabilities of AI agents on real-world vulnerability analysis tasks. · GitHub</a></li>
<li><a href="https://liqiangjing.github.io/dsbench.github.io/">DSBench : How Far are Data Science Agents Becoming Data Science...</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#api`, `#model-release`, `#agent`, `#benchmarks`

---

<a id="item-3"></a>
## [华为开源 505B 参数 MoE 大模型 openPangu-2.0-Pro](https://huggingface.co/openpangu/openPangu-2.0-Pro) ⭐️ 8.0/10

华为在 Hugging Face 上发布了 openPangu-2.0-Pro，这是一个总参数约 505B 的混合专家（MoE）大语言模型。该模型基于昇腾 NPU 训练，支持 512k 上下文长度，在 AIME 2026 数学推理中得分 95.4。 开源一个 505B 参数的 MoE 模型是开放权重 AI 生态的重要一步，表明大规模高性能模型可以在主流 GPU 生态之外完成训练。这也证明了昇腾 NPU 在前沿规模训练上的可行性，可能为行业提供 NVIDIA 之外的硬件选择。 模型采用 MLA 注意力以及 DSA+SWA 独立分层混合设计，并带有 3 头 MTP 自投机解码模块。后训练阶段结合了快慢合一微调和多专项强化学习；Thinking 版本在 AIME 2026 得分 95.4，在 GPQA-Diamond 得分 87.9。

telegram · zaihuapd · 7月31日 06:50

**背景**: MoE 模型每个 token 只激活部分参数，从而在大规模下提升推理效率。MLA 通过低秩潜在表示压缩 KV 缓存，减少推理时的内存瓶颈；DSA 和 SWA 则结合稀疏注意力与滑动窗口注意力来设计查询对上下文的关注方式。昇腾 NPU 是华为的 AI 加速器，为训练和推理提供了 GPU 之外的另一种选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://planetbanatt.net/articles/mla.html">Understanding Multi-Head Latent Attention</a></li>
<li><a href="https://www.tensoreconomics.com/p/deepseek-sparse-attention-from-first">DeepSeek Sparse Attention from First Principles</a></li>
<li><a href="https://veomni.readthedocs.io/en/latest/hardware_support/get_started_npu.html">Get Started with Ascend NPU — VeOmni 0.1.11 documentation</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#MoE`, `#Large Language Model`, `#Open Source`, `#AI`

---

<a id="item-4"></a>
## [美法官质疑 Anthropic 供应链风险认定，或永久撤销禁令](https://techcrunch.com/2026/07/30/judge-says-trump-admin-still-lacks-evidence-for-anthropic-supply-chain-risk-label/) ⭐️ 8.0/10

联邦地区法官 Rita Lin 在周四听证会上表示，特朗普政府未提供足够证据，证明将 Anthropic 列为「供应链风险」并禁止联邦机构使用其 AI 是合理的。她此前已临时叫停该禁令，目前正考虑永久撤销。 此案可能开创先例，决定政府能否因联邦承包商批评其政策而进行报复，引发与政府合作的科技公司关于言论自由的担忧。裁决结果也将影响 Anthropic 等 AI 公司能否在军事用途上落实其技术使用保障。 争端源于 Anthropic 与国防部合同谈判破裂：Anthropic 要求其 AI 不被用于对美国人进行大规模监控或致命武器决策，国防部则认为私营企业不应规定军方如何使用技术。Anthropic 于 3 月提起两起诉讼，政府律师计划在 9 月 30 日前完成停用 Anthropic 产品。

telegram · zaihuapd · 7月31日 08:00

**背景**: Anthropic 是一家人工智能公司，其 AI 服务被政府机构和企业使用。在此事件中，「供应链风险」是联邦政府的一种认定标签，可限制各机构采购或使用某公司的产品。法官 Lin 表示，政府以 Anthropic 公开批评国防部为由实施封禁的逻辑「非常令人不安」，可能开创报复与政府意见不合的承包商的先例。

**标签**: `#AI policy`, `#Anthropic`, `#legal`, `#government`, `#supply chain`

---

<a id="item-5"></a>
## [MiniMax 多模态视频模型 H3 将于 8 月 3 日开源](https://modelscope.cn/models/MiniMax/MiniMax-H3) ⭐️ 8.0/10

MiniMax 将于 8 月 3 日开源其 H3 多模态视频模型，支持文本、图像、音频和视频的理解与生成。

telegram · zaihuapd · 7月31日 12:37

**标签**: `#AI`, `#multimodal`, `#video generation`, `#open-source`, `#MiniMax`

---

<a id="item-6"></a>
## [德国法院裁定 AI 音乐公司 Suno 侵犯版权](https://www.dw.com/en/german-court-rules-that-ai-music-firm-suno-violated-copyrights/a-78152227) ⭐️ 8.0/10

慕尼黑地区法院周五裁定，AI 音乐公司 Suno 未经授权使用受版权保护的音乐训练模型，构成侵权。法院责令 Suno 披露其获利并支付赔偿，具体金额待定。 这是全球首批检验版权法如何适用于 AI 音乐训练的重大裁决之一，可能为其他生成式 AI 公司树立先例。该判决增强了 GEMA 等权利人在推动平等许可谈判而非未经授权使用方面的筹码。 该诉讼由德国音乐版权集体管理组织 GEMA 于 2025 年 1 月提起。庭审中，GEMA 演示了 Suno 生成的歌曲与原受保护作品高度相似；Suno 表示不认同判决，将评估包括上诉在内的所有选项。

telegram · zaihuapd · 7月31日 13:11

**背景**: Suno 是一个生成式 AI 音乐平台，可根据文本或音频提示创作歌曲，于 2023 年 12 月全面上线，后来集成到微软 Copilot 中。GEMA 是德国的音乐版权集体管理组织，代表逾 9.5 万名会员及全球超过 200 万名权利持有人。AI 音乐系统通常使用大量现有录音进行训练，这种使用是否需获权利人许可，是全球法院正在解答的关键法律问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Suno_AI">Suno AI</a></li>

</ul>
</details>

**标签**: `#AI copyright`, `#Suno`, `#legal ruling`, `#generative music`, `#GEMA`

---

<a id="item-7"></a>
## [卫健委通报第五批涉&\#x27;论文工厂&\#x27;科研失信案件，共 21 起](https://www.nhc.gov.cn/qjjys/ycdtxx/202607/22372dfb50574e56b12827f142c873f2.shtml) ⭐️ 6.0/10

7 月 30 日，国家卫健委公开通报第五批涉&\#x27;论文工厂&\#x27;科研失信案件，共 21 起，涉及福建、江西、浙江、湖北、广东、甘肃等地多家医院的医务人员。相关责任人被禁止承担财政性资金支持的科技活动，并被记入科研诚信严重失信行为数据库。 这标志着中国对医学研究中论文买卖等学术不端行为的持续高压整治，处罚力度升级至终身禁止承担科技活动。也反映出政府清理以论文数量为导向的学术评价体系、遏制论文购买风气的决心。 通报点名了江西省人民医院邵靓、抚州市第一人民医院张萍等责任人，因其与此前通报案件合并处理而被终身禁止参与相关科技活动；广州市红十字会医院梁伟国因违纪违法已被开除公职并服刑，调查终止。部分其他署名作者被认定不存在科研失信行为。

telegram · zaihuapd · 7月31日 05:40

**背景**: &\#x27;论文工厂&\#x27;指以商业化方式售卖伪造论文、代写代投、提供虚假实验数据和署名资格的服务，帮助医务人员快速积累论文成果。中国设有全国科研诚信严重失信行为数据库，违规者可能被取消财政性科研项目资格、撤销职称晋升资格并追回奖励。2026 年 7 月早些时候已有 28 起案件的通报批次，另有一批涉及 49 名医务人员，显示全国性整治持续加码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinanews.com.cn/gn/2026/07-10/10656868.shtml">涉 数 据 造假、论文买卖等 国家卫健委通报28...</a></li>
<li><a href="https://36kr.com/p/3205474137252098">从 论 文 工 厂 到学术难民，被AI揭开的学术伤疤-36氪</a></li>
<li><a href="https://www.163.com/dy/article/KT1LALOF0552MD9C.html">刚刚，又有49位医务人员被国家卫健委通报！</a></li>

</ul>
</details>

**标签**: `#research integrity`, `#scientific misconduct`, `#paper mills`, `#healthcare`, `#academic publishing`

---

<a id="item-8"></a>
## [特朗普政府拟向留学生征收 10 万美元毕业后工作费](https://www.bloomberg.com/news/articles/2026-07-30/trump-weighs-100-000-fee-for-foreign-students-to-work-post-grad) ⭐️ 6.0/10

特朗普政府正考虑对参加选择性实践培训（OPT）的国际学生收取 10 万美元费用，OPT 允许他们在毕业后留美工作。白宫官员表示暂无即将出台的政策变化，但未否认正在进行讨论。 若实施，该费用可能大幅减少留美工作的国际毕业生数量，冲击依赖国际学生学费的高校以及雇佣这些毕业生的硅谷和华尔街科技公司。这也标志着政府进一步收紧学生签证政策。 报道称，去年秋季近 30 万国际学生持 OPT 留美。本月初，国土安全部将学生签证居留期限缩短为四年；政府还曾拟对 H-1B 签证收取同等费用，但 6 月被联邦法官裁定违法，白宫正在上诉。

telegram · zaihuapd · 7月31日 09:00

**背景**: 选择性实践培训（OPT）是一种工作许可，允许符合条件的 F-1 国际学生在美国从事与其专业领域直接相关的工作。H-1B 签证是一种非移民签证，允许美国雇主临时聘用 IT、工程等专业领域的外国工人。该提案是围绕国际学生和技术移民在美国经济中作用的更广泛辩论的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.waypointimmigration.org/copy-of-o-1">OPT | Waypoint Immigration USA</a></li>
<li><a href="https://www.irishtimes.com/business/2025/09/22/what-is-happening-with-the-h-1b-visa-scheme-in-the-us-and-how-will-it-affect-irish-tech-workers/">What is the H - 1 B visa and how will changes to the scheme affect 372...</a></li>

</ul>
</details>

**标签**: `#immigration`, `#international-students`, `#tech-industry`, `#policy`, `#OPT`

---

<a id="item-9"></a>
## [美团联合苏州上线外卖骑手“等灯停表”](https://www.meituan.com/news/NN260731177009116) ⭐️ 6.0/10

7 月 31 日，美团与苏州公安正式上线外卖骑手“等灯停表”功能，在苏州率先路测。系统记录骑手等红灯的时长，并在订单完成后相应顺延最晚送达时间。 这是外卖行业在算法公平上迈出的务实一步，直接针对骑手因配送时间紧张而闯红灯的痛点。若该模式推广到更多城市，可能重塑平台配送时效计算方式，推动交通信号数据更广泛地接入物流算法。 该功能依靠骑手位置轨迹和实时信号灯数据判断等灯状态；骑手同时配送多笔订单时，等待时长会计入每笔订单的配时。首批在姑苏区和苏州工业园区接入约 1100 个路口，北京、无锡已同步对接测试，上海、杭州等 20 余个城市正在评估。

telegram · zaihuapd · 7月31日 11:00

**背景**: 传统外卖配送通常对所有订单采用“一刀切”的计时方式，不预留等红灯等不可避免的耗时，长期导致骑手因配送时间紧张而冒险闯红灯、抢灯或逆行。苏州试点是各地推进平台算法治理的一部分，此前多地已通过立法和考核机制优化来应对骑手交通违规，但较少触及算法本身。“等灯停表”是智慧交通数据直接接入配送时效计算的早期案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.mp.oeeee.com/a/BAAFRD0000202607311636133.html">刚刚！ 美 团 和苏州联合发布上线外卖骑手“ 等 灯 停 表 ”试点功能 | 南都N视频</a></li>
<li><a href="https://m.mp.oeeee.com/a/BAAFRD0000202607241631724.html">苏州试点 骑 手 等 红 灯 不扣 配 送 时 长 ，多地立 法 加强平台 算 法 治理</a></li>
<li><a href="http://m.scitoday.cn/zhuanlan/info-43354.aspx">给 算 法 加上“ 红 绿 灯 ”，受益的不只是 骑 手 -评论专栏-今日科学</a></li>

</ul>
</details>

**标签**: `#delivery`, `#gig economy`, `#algorithmic fairness`, `#smart city`, `#logistics`

---

<a id="item-10"></a>
## [YouTube 以涉性内容政策封禁多名 ASMR 创作者](https://www.404media.co/youtube-asmr-ban-sex-and-nudity-policy/) ⭐️ 6.0/10

本周 YouTube 以违反「性满足类」内容政策为由，封禁了 ItsBunniiASMR、Slight Sounds、Nananightray、Roseasmr 等多名知名 ASMR 频道。创作者在毫无预警的情况下收到移除通知，且申诉均未成功。 该事件凸显了平台内容审核规则的模糊性和执行不一致性，可能突然终结创作者的谋生之道。它也反映了外界对 ASMR 的性化污名化，尽管 ASMR 主要被用于放松和助眠。 部分被封频道拥有大量受众，例如 Bunnii 约有 22.7 万订阅者和 5500 万次播放量。YouTube 于 2019 年引入相关政策，2022 年又明确针对 ASMR 内容作出说明，但创作者认为标准模糊且执行不公。

telegram · zaihuapd · 7月31日 15:58

**背景**: ASMR（自发性知觉经络反应）是一种主观上的愉悦感，通常由轻柔的声音或温和的视觉刺激触发，常用于放松和助眠。YouTube 的「裸体与性内容政策」禁止以提供性满足为目的的内容，包括某些恋物内容，且适用于现实、插画、动画和戏剧化素材。创作者坚持认为他们的 ASMR 视频与性无关，此次封禁混淆了 ASMR 与色情内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ASMR">ASMR - Wikipedia</a></li>
<li><a href="https://support.google.com/youtube/answer/2802002?hl=en-GBfollow">Nudity &amp; Sexual Content Policy - YouTube Help</a></li>
<li><a href="https://web.archive.org/web/20190611173509/https://support.google.com/youtube/answer/2802002?hl=en">Nudity and sexual content policies - YouTube Help</a></li>

</ul>
</details>

**标签**: `#YouTube`, `#ASMR`, `#内容审核`, `#平台政策`, `#创作者经济`

---