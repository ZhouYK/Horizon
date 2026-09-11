---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11 23:04:26 +0000
lang: zh
report: default
---

> 从 199 条内容中筛选出 8 条重要资讯。

---

1. [OpenAI 在 API 中上线全双工语音模型 GPT-Live-1](#item-1) ⭐️ 8.0/10
2. [GitLab 修复 CVSS 10.0 漏洞：未认证用户可读取服务器文件](#item-2) ⭐️ 8.0/10
3. [OpenAI 推出 Agents API 公测版，支持生产级云端智能体](#item-3) ⭐️ 8.0/10
4. [Altman 向员工表态：OpenAI 愿意放缓前沿 AI 开发](#item-4) ⭐️ 7.0/10
5. [中国重组月球探测工程，嫦娥八号原方案被取消](#item-5) ⭐️ 7.0/10
6. [Waymo 效应：AI 如何悄然削弱科研协作](#item-6) ⭐️ 7.0/10
7. [消息称 Anthropic 正构建监控系统监视反 AI 人士](#item-7) ⭐️ 7.0/10
8. [日本数字厅服务器遭未授权访问，约 24.6 万人数据或泄露](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 在 API 中上线全双工语音模型 GPT-Live-1](https://openai.com/index/introducing-gpt-live-1-in-the-api/) ⭐️ 8.0/10

OpenAI 于 2026 年 9 月 10 日将 GPT-Live-1 上线 API，这是一个可同时听说、并支持自然打断、背景噪声处理和长对话的全双工语音模型。OpenAI 还表示，该模型可将复杂推理与工具调用交给后端模型处理，并声称其在 Full Duplex Bench 上较 GPT-Realtime-2.1 提升 30 个百分点。 具备可打断能力的全双工语音到语音交互，再加上后端工具调用，对语音智能体而言是一次实质性的能力跃升，有望让电话客服机器人和实时语音助手听起来自然得多。由于它直接通过 OpenAI API 提供，语音前端价格据称为每分钟 0.05 美元，这降低了过去需要自行搭建流式传输与轮流发言机制的门槛。 该公告称 GPT-Live-1 在 Full Duplex Bench 上较 GPT-Realtime-2.1 提升 30 个百分点，语音前端价格为每分钟 0.05 美元，但没有给出基准测试的细分结果、延迟数据、支持语言范围，也没有说明后端委派机制的限制。所报道的 2026 年 9 月 10 日发布日期较为异常，且信息源只是一则简短转述，缺乏独立验证，因此在得到确认之前这些说法应视为厂商自述。

telegram · zaihuapd · 9月11日 03:09

**背景**: 传统语音助手采用轮流发言模式：先等你停止说话，再转写音频、生成回复，最后朗读出来。全双工语音模型则是一边生成语音一边持续聆听，因此能够像人类听者那样处理插话、附和和语音重叠。Full Duplex Bench 是一个公开评测套件，专门衡量停顿处理、轮流发言和打断管理等交互行为；而 GPT-Realtime-2.1 是 OpenAI 更早推出的低延迟流式语音到语音模型，支持可配置的推理强度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/DanielLin94144/Full-Duplex-Bench">GitHub - DanielLin94144/Full-Duplex-Bench: A Benchmark for ...</a></li>
<li><a href="https://arxiv.org/abs/2503.04721">[2503.04721] Full-Duplex-Bench: A Benchmark to Evaluate Full ... [2510.07838] Full-Duplex-Bench-v2: A Multi-Turn Evaluation ... Full-Duplex-Bench-v3 Full-Duplex-Bench: Real-Time Dialogue Benchmark GitHub - pengyizhou/FD-Bench</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-realtime-2.1">GPT-Realtime-2.1 Model | OpenAI API</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#voice-ai`, `#real-time-speech`, `#API-release`, `#LLM`

---

<a id="item-2"></a>
## [GitLab 修复 CVSS 10.0 漏洞：未认证用户可读取服务器文件](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) ⭐️ 8.0/10

9 月 10 日，GitLab 发布 19.3.2、19.2.6 和 19.1.8 三个紧急补丁版本，修复 CVE-2026-85706：该漏洞官方评为 CVSS 10.0，未认证用户可利用代码仓库 commits API 的路径约束与认证缺陷，读取 GitLab 服务器上的任意文件。受影响版本包括 18.7 至 19.1.8 之前的版本、19.2.6 之前的 19.2 版本，以及 19.3.2 之前的 19.3 版本。 一个最高严重等级、且无需认证的任意文件读取漏洞，意味着任何可被公网访问的自建 GitLab 实例都可能被匿名攻击者窃取源代码、配置文件、密钥或 CI/CD 凭据，因此官方强烈建议运维人员立即升级。这也再次说明，集中托管源码与流水线密钥的 DevOps 平台已成为高价值攻击目标，GitLab 为三条并行版本分支同时发布紧急补丁，对整个自建生态都意义重大。 GitLab 表示 GitLab.com 已完成修复，GitLab Dedicated 用户无需操作，因此暴露风险主要集中在自建实例上；该漏洞由研究员 s3ntago 通过 HackerOne 报告。官方目前未公开具体前置条件，发布时网上也没有可复现的公开 PoC，尚无证据显示该漏洞已遭在野利用。

telegram · zaihuapd · 9月11日 11:05

**背景**: GitLab 是一个 DevOps 平台，企业可以把整套系统部署在自己的服务器上，也就是俗称的“自建实例”，它与厂商托管的 GitLab.com SaaS 服务以及托管式的 GitLab Dedicated 不同。commits API 是 GitLab REST API 的一部分，用于让工具和脚本以编程方式读取仓库的提交数据；一旦该接口对文件路径处理不当，攻击者就可能突破仓库边界，访问服务器上的其他文件。CVSS 是业界通行的 0 至 10 分严重程度评分体系，10.0 为满分，通常代表漏洞可远程利用、无需认证，且机密性影响极为严重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.gitlab.com/api/rest/">REST API | GitLab Docs</a></li>
<li><a href="https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator">NVD CVSS v3 Calculator</a></li>
<li><a href="https://about.gitlab.com/install/">Download and install GitLab</a></li>

</ul>
</details>

**标签**: `#GitLab`, `#security-vulnerability`, `#CVE`, `#infosec`, `#patch-release`

---

<a id="item-3"></a>
## [OpenAI 推出 Agents API 公测版，支持生产级云端智能体](https://openai.com/index/introducing-the-agents-api/) ⭐️ 8.0/10

2026 年 9 月 10 日，OpenAI 推出 Agents API 公测版，开发者只需一次 API 调用即可创建生产级云端智能体，并可选择 OpenAI 托管沙箱、自有基础设施或合作伙伴环境来运行。该 API 基于开源 Codex harness 构建，并新增了长会话上下文压缩、工具搜索、并行工具调用和子智能体协作等能力。 这把智能体开发从自建工程变成了托管式平台产品，可能促使许多团队放弃自研智能体框架，转而采用 OpenAI 的技术栈。由于 Anthropic、Google 以及众多开源智能体运行时都在争夺同一批开发者，此举抬高了智能体平台之争的竞争强度，也使 OpenAI 在模型供应商之外，进一步成为运行时（runtime）供应商。 该 API 基于开源 Codex harness 构建，OpenAI 此前已将其定位为可编程智能体工作流的平台；公测期间不收取额外费用，开发者只需为智能体消耗的令牌和工具调用付费。上下文压缩之所以重要，是因为长时间运行的智能体历史会不断增长，既推高内存成本又会导致推理质量下降，而子智能体协作则允许把任务拆分到相互隔离的并行智能体上执行。

telegram · zaihuapd · 9月11日 11:12

**背景**: 这里的“智能体”指的是被赋予工具和循环机制的 LLM，能够自主执行多步操作，而不只是回答单次提问；而“harness”则是管理这一循环、工具调用、沙箱和状态的周边运行时。OpenAI 的 Codex harness 源自其 Codex 编程智能体，已经开源，开发者可通过命令行、SDK 或 app-server 在其上构建应用。上下文压缩是长周期智能体领域的研究热点，因为智能体不断累积的观察记录、推理轨迹和工具结果，最终会超出固定上下文窗口的容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/blog/codex-as-a-platform">Codex as a platform: build on the open agent harness</a></li>
<li><a href="https://arxiv.org/abs/2510.00615">ACON: Optimizing Context Compression for Long-horizon LLM Agents Acon: Optimizing Context Compression for Long-horizon LLM Agents ACON: Optimizing Context Compression for Long-horizon LLM Agents Context Compression for LLM Agents: A Survey of Methods ... ACON: Optimizing Context Compression for Long-horizon LLM Agents Awesome Agent Context Compression - GitHub GitHub - microsoft/acon: Official implementation of paper ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI Agents`, `#API`, `#Developer Tools`, `#LLM`

---

<a id="item-4"></a>
## [Altman 向员工表态：OpenAI 愿意放缓前沿 AI 开发](https://www.bloomberg.com/news/articles/2026-09-11/openai-is-open-to-slowing-cutting-edge-ai-ceo-sam-altman-tells-staff) ⭐️ 7.0/10

据多名知情人士透露，OpenAI 首席执行官萨姆·奥尔特曼本周在全员会议上表示，公司可能愿意与其他 AI 实验室协调，放慢前沿 AI 的开发进度，但部分公司或许不愿配合。OpenAI 近期已因安全担忧放缓部分模型开发，并暂停了某些内部 AI 训练，公司对此拒绝置评。 在一个长期以速度竞争为主的领域里，头部实验室公开表示可以接受协调一致的放缓，是一个值得注意的转向，也可能为自愿安全标准和前沿 AI 治理注入动力。如果这真的带来实际协调，将会影响到所有构建或依赖最前沿模型的人，从初创公司到企业用户。 该报道来自匿名的二手消息源，OpenAI 本身拒绝置评，因此放缓的时间表、范围和机制都尚未得到确认。任何暂停还取决于能否与竞争对手实验室协调，而其中一些可能拒绝配合；此外，OpenAI 首席科学家也单独呼吁，在建立共同安全标准之前自愿放缓未来的开发。

telegram · zaihuapd · 9月11日 02:23

**背景**: 前沿 AI 指的是能力处于最领先水平的一类最先进通用模型，例如能够处理复杂任务的大型推理模型和多模态系统。AI 安全是研究如何确保这类系统按设计意图运行、不造成伤害的领域，而 AI 治理则涉及用于监管它们的规则、标准和制度。所谓“自愿放缓”，指的是实验室主动限制或推迟自身的训练计划，而不是被监管强制要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>
<li><a href="https://builtin.com/artificial-intelligence/ai-safety">What Is AI Safety ? | Built In</a></li>
<li><a href="https://www.ncsc.gov.uk/frontier-ai">Frontier AI: what you need to know | National Cyber Security ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#frontier AI`, `#AI governance`, `#industry news`

---

<a id="item-5"></a>
## [中国重组月球探测工程，嫦娥八号原方案被取消](https://spacenews.com/china-alters-change-8-lunar-south-pole-mission-amid-lunar-program-reorganization/) ⭐️ 7.0/10

2026 年 5 月，中国载人航天工程办公室宣布把原由国家航天局负责的无人探月工程与载人登月工程整合为统一的“月球探测工程”，在任务、资源和队伍三方面进行统筹。受此影响，原定 2029 年前后发射、登陆月球南极莫顿环形山的嫦娥八号独立任务被取消或大幅调整；巴基斯坦已于 2026 年 9 月证实该任务取消，其原定国际载荷拟转至 2030—2031 年的其他登月任务。 此次重组让载人航天机构掌握了月球任务的总体管理权，这一变化会波及国际合作排期、月球科学规划以及各合作伙伴的预期，巴基斯坦载荷被重新安排就是首个公开的受影响案例。它也表明中国正把资源集中到一条“无人+载人”一体化的路径上，服务于其载人登月南极目标与国际月球科研站（ILRS）的总体计划，而非继续维持各自独立的机器人任务线。 嫦娥八号原计划由着陆器、巡视器和机器人组成，搭载约 14 台科学仪器，其中包含为国际月球科研站做准备的“月壤制砖”等原位资源利用实验。该任务的发射时间在不同报道中于 2028 年至 2029 年之间浮动，而因取消而失去搭载机会的载荷将被推迟到 2030—2031 年的任务，使合作方的科学研究延后数年。

telegram · zaihuapd · 9月11日 04:00

**背景**: 中国的探月工程此前以一系列无人嫦娥任务的形式推进：嫦娥四号于 2019 年实现人类首次月球背面软着陆，嫦娥五号于 2020 年完成采样返回，嫦娥六号于 2024 年带回月球背面样品，而嫦娥七号原本负责为嫦娥八号勘察月球南极。月球南极之所以受重视，是因为永久阴影区内的环形山可能蕴藏水冰，而几乎常年受光照的区域（“永昼峰”）有利于发电，这两点对中国牵头、多国参与的国际月球科研站都至关重要。与此同时，中国载人航天工程办公室一直在研制长征十号火箭和载人月面着陆器，目标是在 2030 年前实现中国航天员登月，而此次重组把无人探月线路并入了这一整体努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scmp.com/news/china/science/article/3251854/china-calls-developers-change-8-mission-make-and-assemble-moon-bricks">China calls for developers in Chang ’ e 8 mission to make and...</a></li>
<li><a href="http://english.scio.gov.cn/chinavoices/2025-04/24/content_117842431.html">China to launch Chang &#x27; e - 8 lunar mission around... | english.scio.gov.cn</a></li>
<li><a href="https://interestingengineering.com/space/HUMANOID-ROBOT-COULD-JOIN-CHINA-MISSION-TO-MOON-2028">Humanoid robot could join China&#x27;s Chang &#x27; e 8 mission to the moon</a></li>

</ul>
</details>

**标签**: `#space`, `#china`, `#lunar-exploration`, `#chang&\#x27;e-8`, `#policy`

---

<a id="item-6"></a>
## [Waymo 效应：AI 如何悄然削弱科研协作](https://www.researchagenda.news/articles/the-waymo-effect.html) ⭐️ 7.0/10

Research Agenda 发表的一篇文章提出用“Waymo 效应”来类比大语言模型在科研中的角色：正如无人驾驶汽车消除了道路上人际互动的摩擦，大语言模型也消除了科研中与他人合作时的摩擦。作者认为，尽管个人产出可能更快，但推动优秀研究的质疑、偶遇与共同思考会被侵蚀，导致研究观点趋于同质、协作网络被削弱。 这一论点把讨论从“研究者该不该用 AI”转向“机构应如何重新设计激励与基础设施”，直接影响那些以速度和个体产出为奖励导向的资助方、高校与实验室管理者。如果该论断成立，AI 的普及可能提高论文数量，却降低科学观点的多样性与稳健性——这是系统性风险，而非单纯的个人效率问题。 该文属于概念性、观点驱动的分析，而非实证研究，因此并未给出协作度或观点趋同程度的量化数据。其具体主张是：人类应继续掌握研究问题、研究路径与结论；资助方与机构应把面对面交流、访问交流和非结构化讨论视为研究基础设施；同时应减少对速度的单一奖励。

telegram · zaihuapd · 9月11日 13:57

**背景**: Waymo 是 Alphabet 旗下的自动驾驶公司，无人驾驶常被形容为消除了驾驶中的人际摩擦——无需与其他司机博弈、无需寒暄、无需临场应变。而在科研领域，ChatGPT、Claude 等大语言模型已被广泛用于文献综述、编程和写作，同样让个人能够独立完成过去需要与同行讨论才能完成的任务。文章借用 Waymo 的类比指出，AI 消除的这些摩擦，恰恰也是科研中偶遇灵感、相互质疑与形成共同理解的重要来源，而这些正是科学运作的核心。

**标签**: `#AI 与科研`, `#研究协作`, `#大语言模型`, `#科研政策`, `#技术哲学`

---

<a id="item-7"></a>
## [消息称 Anthropic 正构建监控系统监视反 AI 人士](https://prospect.org/2026/09/09/anthropic-artificial-intelligence-surveillance-system-monitor-activists/) ⭐️ 7.0/10

据报道，Anthropic 正在构建一套监控系统，用于追踪反 AI 活动人士、监视其高管与资产附近的抗议活动，并预测风险以便向警方举报嫌疑人。

telegram · zaihuapd · 9月11日 15:33

**标签**: `#AI ethics`, `#Anthropic`, `#surveillance`, `#AI governance`, `#privacy`

---

<a id="item-8"></a>
## [日本数字厅服务器遭未授权访问，约 24.6 万人数据或泄露](https://www.bloomberg.com/news/articles/2026-09-11/japan-s-digital-agency-hit-by-unauthorized-access-to-servers) ⭐️ 6.0/10

日本数字厅宣布其服务器遭到未经授权的访问，约 24.6 万人的个人数据可能因此泄露。调查显示，攻击者在 6 月下旬利用一个虚拟专用网络（VPN）漏洞，并通过维护账号访问了大量文件。 日本数字厅是统筹日本政府服务数字化的核心机构，因此这种规模的泄露会引发外界对日本公共部门 IT 整合过程中安全防护能力的担忧。同时它也再次说明，未修补的 VPN 入口和高权限维护账号依然是攻击者侵入政府网络的常见突破口。 可能泄露的数据包括姓名、电子邮箱和电话号码，该机构目前尚未确认这些信息是否已被实际滥用。此次入侵据称发生在 6 月下旬，这意味着从最初的入侵到事件公开披露之间存在时间差。

telegram · zaihuapd · 9月11日 05:10

**背景**: 日本数字厅（デジタル庁）成立于 2021 年 9 月，目标是统一并现代化日本政府原本分散的 IT 系统，推动公共服务的数字化。VPN（虚拟专用网络）允许员工和管理员远程接入内部系统，因此一台未修补漏洞的 VPN 设备就可能让攻击者在网络内部获得立足点。维护账号尤其敏感，因为它们通常拥有较高权限，而受到的监控往往又比普通用户账号更宽松。

**标签**: `#cybersecurity`, `#data breach`, `#Japan`, `#government`, `#VPN vulnerability`

---