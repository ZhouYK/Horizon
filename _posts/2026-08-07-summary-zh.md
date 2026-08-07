---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
report: default
---

> 从 278 条内容中筛选出 8 条重要资讯。

---

1. [OpenAI 称 Astra 或达关键网络能力，扩大安全测试或推迟发布](#item-1) ⭐️ 9.0/10
2. [sub2api 曝 OAuth 高危漏洞：仅凭邮箱即可接管账户](#item-2) ⭐️ 8.0/10
3. [Anthropic 更新 Fable 5 生物学安全防护，误拦截大减](#item-3) ⭐️ 7.0/10
4. [SEC 批准纳斯达克 23 小时交易制，2026 年 12 月 6 日上线](#item-4) ⭐️ 7.0/10
5. [美国审查中国 AI 企业海外获取英伟达芯片渠道](#item-5) ⭐️ 7.0/10
6. [SK 海力士确认 V10 NAND 为 375 层堆叠并导入晶圆键合技术](#item-6) ⭐️ 7.0/10
7. [亚马逊整顿内部 CPU 浪费，智能体 AI 推高算力需求](#item-7) ⭐️ 7.0/10
8. [OpenAI 首曝 ChatGPT 国别使用数据：AI 从问答走向干活](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 称 Astra 或达关键网络能力，扩大安全测试或推迟发布](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) ⭐️ 9.0/10

2026 年 8 月 7 日，OpenAI 披露其即将推出的 Astra 模型在内部评估中于代理编码与网络安全方面取得重大进展，无法排除达到“关键”网络能力阈值的可能性。公司已暂停不符合强化安全要求的内部活动，实施隔离测试等措施，并将与政府机构和 AI 安全组织合作进行第三方测试。 若 Astra 达到关键阈值，它可能无需人工干预就能自主发现并利用加固系统中的零日漏洞，这对国家安全具有严重影响。这一披露可能改变前沿模型发布时间的预期，并加剧业界对部署前安全测试的讨论。 根据 OpenAI 的预备框架，此前 GPT-5.6-Sol 在同一网络安全评估中仅被评为“高”，因此“关键”可能性是明显的升级。公司已将 Astra 纳入隔离测试环境，加强加密与通用监控，并暂停不符合强化安全要求的内部活动。

telegram · zaihuapd · 8月7日 16:44

**背景**: OpenAI 的预备框架（Preparedness Framework）是一套用于追踪和降低前沿 AI 灾难性风险的结构化流程，网络安全是其核心类别之一。代理编码（agentic coding）指 AI 代理在最少人工干预下规划、编写、测试和修改代码。该框架的“关键”网络阈值用于标记能够自主执行复杂攻击（例如利用加固系统中的零日漏洞）的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/updating-our-preparedness-framework/">Our updated Preparedness Framework | OpenAI</a></li>
<li><a href="https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf">Preparedness Framework</a></li>
<li><a href="https://explainx.ai/blog/openai-astra-next-major-model-announcement-2026">OpenAI Astra: Next Major Model Explained | explainx.ai Blog</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#cybersecurity`, `#frontier models`, `#release delay`

---

<a id="item-2"></a>
## [sub2api 曝 OAuth 高危漏洞：仅凭邮箱即可接管账户](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 8.0/10

sub2api v0.1.171 及之前版本被披露存在一个 CVSS 8.8 的严重 OAuth 账户接管漏洞。攻击者仅知道受害者注册邮箱，即可在无需密码、验证码或用户交互的情况下，将自己的 OAuth 身份绑定到受害者账户。 该漏洞可导致攻击者完全接管 AI API 代理服务中的 API 密钥、账单余额和订阅配额。由于利用方式简单且仅需一个邮箱地址，受影响用户面临凭据被盗和配额被滥用的直接风险。 该缺陷位于 pending session 交换流程的 existingUser 分支，该分支在绑定 OAuth 身份时不校验密码和验证码。攻击者将目标用户 ID 设为受害者的 ID，此后每次 OAuth 登录都会被解析为受害者账户。

telegram · zaihuapd · 8月7日 14:59

**背景**: sub2api 是一个开源 AI API 代理项目，用于统一管理 Claude、OpenAI、Gemini 和 Antigravity 的订阅。OAuth 是一种常见的授权框架，允许用户使用第三方身份登录；pending session 流程用于将新的 OAuth 身份关联到已有账户，而该关联过程中的缺陷可能导致账户被接管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Wei-Shaw/sub2api/issues/5350">OAuth Account Takeover via Pending Exchange Bypass in sub2api</a></li>
<li><a href="https://grokipedia.com/page/Sub2API">Sub2API</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#OAuth`, `#account takeover`, `#sub2api`

---

<a id="item-3"></a>
## [Anthropic 更新 Fable 5 生物学安全防护，误拦截大减](http://claude.ai/) ⭐️ 7.0/10

8 月 7 日，Anthropic 宣布更新 Claude Fable 5 的生物学安全防护，将生物学相关查询的误降级次数减少约 85%。预计 Claude.ai 上的总回退次数也将下降约 67%。 此次更新大幅改善了解读化验结果、了解症状、学习生物学等日常健康与教育问题的用户体验，同时保留了对高风险双重用途研究的降级回退机制。这展示了如何在不过度拦截的情况下完善 AI 安全防护，同时不削弱生物安全。 此次更新通过重写安全分类器的规则与训练数据实现。出于双重用途风险考虑，病毒学、毒理学、分子设计等高风险请求仍会回退至 Opus 5。

telegram · zaihuapd · 8月7日 06:05

**背景**: Claude Fable 5 是 Anthropic 于 2026 年 6 月 9 日推出的最强大的广泛发布模型，属于 Mythos 级模型，并已针对一般使用进行了安全化处理。生物学安全防护旨在防止 AI 被用于有害的生物研究。常见技术是“降级”，即将有风险的提示路由到能力较弱的模型，但过于宽泛的规则可能会拦截良性查询。此次更新旨在平衡安全性与可用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Anthropic`, `#Claude`, `#model update`, `#safety guardrails`

---

<a id="item-4"></a>
## [SEC 批准纳斯达克 23 小时交易制，2026 年 12 月 6 日上线](https://finance.sina.com.cn/stock/bxjj/2026-08-07/doc-inimnkup0012339.shtml) ⭐️ 7.0/10

美国证券交易委员会（SEC）已批准纳斯达克的 23 小时交易制度（23/5），将于 2026 年 12 月 6 日上线。根据该计划，美股市场每天仅休市 1 小时（美东时间 20:00 至 21:00）用于清算和数据处理，其余 23 小时连续开放交易。 这一批准使美国主要交易所的股票交易正式接近全天候（24/5），交易系统、市场微观结构和金融科技基础设施都必须适应接近永不收盘的市场。此前散户投资者已通过 Blue Ocean ATS 等另类交易系统进行隔夜交易，而延长时段成为交易所标配后，可能影响流动性和价格发现。 每天 1 小时的休市时间为美东时间 20:00 至 21:00，用于系统清算和数据处理。SEC 将于 9 月 17 日举办圆桌会议，讨论隔夜时段的投资者保护问题；隔夜交易通常流动性较薄、价差较大。

telegram · zaihuapd · 8月7日 10:03

**背景**: Blue Ocean ATS 由 Blue Ocean Technologies 推出，是首个延长市场交易时间、在美东时间晚上 8 点至凌晨 4 点提供美股连续隔夜交易的另类交易系统。另类交易系统（ATS）是一种非交易所交易场所，以经纪商而非全国性证券交易所的身份接受监管，负责撮合证券买卖订单。在此次批准之前，NYSE Arca 已获得 SEC 加速批准将交易延长至每日 22 小时，Cboe 也提交了近 24×5 的提案，均瞄准 2026 年 12 月。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blueocean-tech.io/">Blue Ocean Technologies LLC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alternative_trading_system">Alternative trading system</a></li>

</ul>
</details>

**标签**: `#finance`, `#trading`, `#regulation`, `#nasdaq`, `#sec`

---

<a id="item-5"></a>
## [美国审查中国 AI 企业海外获取英伟达芯片渠道](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 7.0/10

美国商务部工业与安全局（BIS）已启动系统性审查，调查中国 AI 企业如何通过海外渠道（包括远程租用云计算算力）获取英伟达芯片。此次审查是在月之暗面发布 Kimi K3 模型，以及出现通过泰国等途径非法获取芯片的指控后展开的。 这项调查可能将美国出口管制扩展到远程访问先进芯片的范畴，影响全球云服务商和中国 AI 发展。同时，这也引发了白宫、国会与英伟达之间关于芯片限制范围的立法与政策博弈。 据报道，BIS 正在整理两份国家名单：一份涉及将受限芯片走私进入中国的黑市所在地，另一份是中国企业远程租用芯片的国家。美国众议院已通过一项两党法案，拟明确授权 BIS 监管此类云计算访问，但预计会遭到英伟达等公司反对；报道还称阿里巴巴通过开曼实体控制的新加坡壳公司，利用正被调查的 Megaspeed 在马来西亚使用英伟达芯片。

telegram · zaihuapd · 8月7日 11:18

**背景**: 自 2022 年以来，美国一直限制向中国出口先进英伟达芯片，以减缓其 AI 和军事发展。BIS 负责执行《出口管理条例》（EAR），该条例要求向包括中国在内的 D:5 国家组实体出口某些先进计算物项需取得许可证。然而，中国企业仍可通过租用其他国家云提供商的算力来间接使用这些芯片，而这一做法目前并未被出口管制规则明确覆盖。月之暗面发布的 Kimi K3 是一个开放权重、参数量达 2.8 万亿的多模态模型，已缩小了与美国前沿模型的性能差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bis.gov/">Homepage | Bureau of Industry and Security</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi - K 3 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#export-controls`, `#AI`, `#Nvidia`, `#China`, `#policy`

---

<a id="item-6"></a>
## [SK 海力士确认 V10 NAND 为 375 层堆叠并导入晶圆键合技术](https://www.gelonghui.com/live/2599953) ⭐️ 7.0/10

SK 海力士在 FMS 2026 峰会新闻稿中确认，其下一代 V10 NAND 闪存将采用 375 层堆叠，取代 321 层 V9 4D NAND。这将是该公司首款采用晶圆键合技术的 NAND 产品。 这标志着 NAND 在突破传统 3D 堆叠限制方面迈出了重要一步。官方宣称的每瓦性能提升 2.5 倍，主要面向 AI 基础设施，而能效与高带宽在其中日益关键。 采用晶圆键合技术可分别制造 CMOS 逻辑层和存储层，从而实现更密集的堆叠和更好的电气特性。SK 海力士将 V10 NAND 定位为专门针对兼顾性能与能效的 AI 工作负载而优化。

telegram · zaihuapd · 8月7日 12:19

**背景**: NAND 闪存通过堆叠存储单元层数来提升密度，而无需缩小晶体管尺寸，因此各主要厂商在层数上展开竞争。SK 海力士的“4D NAND”在单元阵列下方集成外围电路以减少芯片面积。晶圆键合是一种在晶圆级将两片已加工完成的晶圆结合在一起的制造技术，能够实现传统单片工艺难以实现的异构集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wafer_bonding">Wafer bonding - Wikipedia</a></li>
<li><a href="https://wccftech.com/sk-hynix-pushing-nand-to-limit-with-worlds-highest-238-layer-4d-nand-1h-2023-production/">SK hynix Pushing NAND To The Limits With World&#x27;s Highest...</a></li>
<li><a href="https://www.imec-int.com/en/articles/wafer-wafer-hybrid-bonding-pushing-boundaries-400nm-interconnect-pitch">Wafer-to-wafer hybrid bonding | imec</a></li>

</ul>
</details>

**标签**: `#NAND`, `#SK Hynix`, `#semiconductor`, `#wafer bonding`, `#AI infrastructure`

---

<a id="item-7"></a>
## [亚马逊整顿内部 CPU 浪费，智能体 AI 推高算力需求](https://www.tomshardware.com/pc-components/cpus/amazon-cracks-down-on-cpu-waste-among-engineers-as-agentic-ai-crunch-intensifies-cpu-demand-makes-low-utilization-ec2-instances-a-hot-commodity) ⭐️ 7.0/10

今年 5 月，亚马逊 AWS 开始严查工程师对 EC2 实例的浪费使用，以确保客户容量，导致内部申请实例的等待时间从此前数小时延长至数天。有工程师表示工作多年从未等过这么久。 智能体 AI 工作负载正在根本性地重塑数据中心 CPU 与 GPU 的配比，从 8:1 或 4:1 逐步逼近 1:1，给 CPU 供应带来新的压力。这一变化影响着云服务商、AI 基础设施规划，以及依赖 EC2 容量的企业。 内部资源紧张源于智能体 AI 大量使用工具调用和复杂的 GPU 编排，其中很大一部分负载运行在 CPU 上。AMD 和英伟达均已加大数据中心 CPU 布局，以争夺这一新兴需求。

telegram · zaihuapd · 8月7日 16:31

**背景**: 智能体 AI（Agentic AI）指无需人类逐步批准、能够自主完成多步骤目标的 AI 系统，不同于单轮对话式 AI。这类系统依赖“工具调用”机制与外部函数、API 或数据库交互，这会在 GPU 推理调用之间增加大量 CPU 开销。随着智能体工作流增长，数据中心必须重新平衡 CPU/GPU 配比，云服务商也面临新的容量规划挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtarget.com/ai/definition/Agentic-AI-explained-Key-concepts-and-enterprise-use-cases">What Is Agentic AI ? Complete Guide | TechTarget</a></li>
<li><a href="https://www.jetlink.io/post/comprehensive-guide-to-tool-calling-for-developers-unlocking-agentic-ai">Comprehensive Guide to Tool Calling : Unlocking Agentic AI</a></li>

</ul>
</details>

**标签**: `#AWS`, `#AI infrastructure`, `#CPU`, `#agentic AI`, `#cloud computing`

---

<a id="item-8"></a>
## [OpenAI 首曝 ChatGPT 国别使用数据：AI 从问答走向干活](https://openai.com/index/how-the-world-is-putting-chatgpt-to-work/) ⭐️ 6.0/10

OpenAI 发布了首份 ChatGPT 国别使用数据，显示用户在工作中使用 ChatGPT 的频率是工作外的两倍多。自今年 4 月 ChatGPT Images 2.0 上线以来，全球多媒体相关消息占比已达 7.8%，且几乎所有国家 35 岁以上用户的参与度都在上升。 这是 OpenAI 自己对 ChatGPT 正从问答工具转向生产工具的佐证，可能会影响企业、教育者和个人评估 AI 投资的方式。国别数据还显示全球采用差距正在缩小，拉丁美洲、非洲和大洋洲正快速追赶早期市场。 在巴西和哥伦比亚，超过十分之一的 ChatGPT 消息涉及多媒体处理；法国和捷克 35 岁以上用户的消息份额在过去一年内增长超过 10 个百分点。该数据反映出多媒体使用和老年用户参与度在不同地区均呈强劲增长。

telegram · zaihuapd · 8月7日 08:43

**背景**: ChatGPT 是 OpenAI 广泛使用的 AI 助手，这份报告似乎是 OpenAI 首次发布国别层面的采用与使用模式数据。ChatGPT Images 2.0 上线时引入了一款最先进的图像生成模型，支持改进的文本渲染、多语言和视觉推理能力，有助于解释多媒体消息的快速增长。这些使用趋势表明 AI 工具正从简单的问答走向写作、编程和创造性分析等实际任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-0/">Introducing ChatGPT Images 2.0 | OpenAI</a></li>
<li><a href="https://chatgpt.com/images/">ChatGPT Images 2.0 | AI Image Generator</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#AI adoption`, `#Usage trends`, `#Industry data`

---