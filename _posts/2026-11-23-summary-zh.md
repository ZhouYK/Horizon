---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23 23:03:50 +0000
lang: zh
report: default
---

> 从 177 条内容中筛选出 8 条重要资讯。

---

1. [Codex2api 疑似遭供应链投毒并外泄 GitHub Actions 密钥](#item-1) ⭐️ 8.0/10
2. [谷歌搭建名为 Mirror Dimension 的模拟互联网，用于测试 Chrome AI 代理](#item-2) ⭐️ 7.0/10
3. [Windows Server 2028 默认移除 WoW64，32 位应用需手动装回](#item-3) ⭐️ 7.0/10
4. [Meta AI 负责人称超级智能将至，人类控制权堪忧](#item-4) ⭐️ 7.0/10
5. [蚂蚁集团领投 1 亿美元，中国具身智能公司 Simplexity 估值达 16 亿美元](#item-5) ⭐️ 6.0/10
6. [GLM-5.4 向所有 GLM Coding Plan 用户开放，新增视觉能力并提升 50% 配额](#item-6) ⭐️ 6.0/10
7. [Anthropic 限制 IPO 承销团队人数，禁止其为 AI 竞争对手服务](#item-7) ⭐️ 6.0/10
8. [开源 nospeaker 用 MacBook 触控板振动“念”出文字](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Codex2api 疑似遭供应链投毒并外泄 GitHub Actions 密钥](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

据报道，Codex2api 作者账号被黑，攻击者绕过 main 分支直接推送 tag，使 Release 构建出的版本带有后门。v3.1.11 移除了鉴权，等于可无密码远程执行命令；同时有 workflow 将仓库的 16 个 GitHub Actions secrets 外传，波及同一账号下至少 21 个仓库。 任何安装或更新过 3.1.10–3.1.12 的用户都应立即停用、退回 3.1.9，并轮换 GitHub token、SSH key、数据库凭据以及 DeepSeek 等相关密钥。该事件表明，单个维护者账号被攻破就足以把可信的发布产物变成跨多个下游仓库的凭据窃取渠道。 事件复盘称，攻击者通过推送 Git tag 绕开 main 分支保护，并触发 Release 构建；受影响版本为 3.1.10–3.1.12，其中 v3.1.11 明确移除了鉴权。报告还指出有 16 个 Actions secrets 被外传，同一账号下至少 21 个仓库受到影响，因此问题并不局限于 Codex2api 仓库本身。

telegram · zaihuapd · 11月23日 11:21

**背景**: Codex2api 被描述为一个 AI API 网关和管理面板，位于应用与模型 API 之间。GitHub Actions secrets 是存放在仓库或组织级别、供 CI/CD workflow 引用的加密值，一旦泄露就可能暴露部署凭据、token 和第三方 API 密钥。供应链攻击是指攻击者攻破可信分发环节——在这里是维护者账号及其发布流水线——让用户主动安装恶意代码。由于发布流程常由 tag 触发，即使 main 分支受保护，推送 tag 仍可能发布构建产物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codex2api.com/">Codex 2 API - AI API Gateway</a></li>
<li><a href="https://github.com/features/actions">GitHub Actions · CI/CD and automations · Agentic Workflows...</a></li>
<li><a href="https://tari.moe/article/2024/zh-an-obscure-actions-workflow-vulnerability-in-googles-flank">谷歌Flank潜藏3年的 Github Action 供 应 链 攻 击 | tari Blog</a></li>

</ul>
</details>

**标签**: `#supply-chain-security`, `#backdoor`, `#github-actions`, `#security-incident`, `#credential-rotation`

---

<a id="item-2"></a>
## [谷歌搭建名为 Mirror Dimension 的模拟互联网，用于测试 Chrome AI 代理](https://www.landian.news/archives/128701.html) ⭐️ 7.0/10

据报道，谷歌为 Chrome 的 AI 代理搭建了一个名为 Mirror Dimension 的隔离模拟互联网，用于测试它打开网站、搜索浏览、登录、加购以及完成各类任务的能力。该环境包含数千个模拟网站，每名工程师使用独立的隔离实例，每天运行超过 1000 个测试案例，重点防御来自恶意网页的提示词注入攻击。 能够点击、输入和完成交易的浏览器 AI 代理，几乎继承了开放网络的全部攻击面，因此用一个带有逼真假网站的受控沙盒来提前发现问题，是一种务实做法。如果这一方法奏效，它可能成为业界安全上线代理式浏览功能的参考范式。 据报道，该方案强调隔离性——每位工程师都拥有独立环境，而不是共用一个模拟网络；模拟站点中还包含仿真的银行和社交网络，让代理在无害却逼真的场景中处理敏感流程。其对提示词注入的重点关注，正说明代理读取的任何网页都可能携带隐藏指令，试图劫持其行为。

telegram · zaihuapd · 11月23日 01:30

**背景**: AI 代理与聊天机器人的区别在于它会执行动作——浏览页面、填写表单、点击按钮——这意味着恶意或被攻陷的网站可能试图操控它。提示词注入正是这样一类攻击：网页或文档中隐藏的文本覆盖了开发者原本的指令，使代理泄露数据或执行非预期操作。由于真实网站不可预测且不断变化，测试这类代理的团队需要一个可复现、能模拟网络但又不暴露真实账号与服务的安全环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://3dnews.ru/1151600/google-sozdala-parallelniy-internet-dlya-obucheniya-iiagentov-v-nyom-est-dage-poddelnie-banki-i-sotsseti">Google создала параллельный интернет для обучения ИИ-агентов...</a></li>
<li><a href="https://wylsa.com/u-google-est-svoj-myortvyj-internet-tolko-dlya-ii-agentov/">У Google есть свой мёртвый интернет только для... — Wylsacom</a></li>
<li><a href="https://openai.com/safety/prompt-injections/">Understanding prompt injections | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#browser security`, `#prompt injection`, `#Chrome`, `#testing infrastructure`

---

<a id="item-3"></a>
## [Windows Server 2028 默认移除 WoW64，32 位应用需手动装回](https://www.windowslatest.com/2026/11/23/32-bit-apps-days-are-numbered-as-microsoft-strips-support-bit-by-bit-starting-with-windows-server-2028-but-windows-11-is-safe-for-now/) ⭐️ 7.0/10

在 Ignite 2026 上，微软表示 Windows Server 2028 将不再默认包含 WoW64 兼容子系统，因此开箱即无法运行 32 位应用。该版本计划于 2027 年秋季与 Windows 11 27H2 一同发布；仍需 32 位支持的管理员可以通过按需功能（FoD）把 WoW64 装回，在 Server Core 上一般使用 PowerShell 或 DISM 完成。 这对企业 IT 来说是一次重要的兼容性变化：仍在服务器上运行老旧 32 位管理代理、业务线软件或旧驱动的组织，必须在升级前审计现有工作负载并制定应对方案。这也表明微软有意在其平台产品线中逐步淘汰 32 位支持，尽管 Windows 11 客户端目前仍保留 WoW64。 WoW64 并非被永久删除，而是变成一个必须显式安装的可选 FoD 包，这意味着依赖 32 位二进制文件的镜像和部署脚本在默认安装环境下会失败。微软将这一改动解释为减少攻击面、阻止 32 位恶意软件，并且尚未公布在 Windows 11 中移除 WoW64 的计划。

telegram · zaihuapd · 11月23日 03:03

**背景**: WoW64（Windows 32-bit on Windows 64-bit）是让 32 位应用能在 64 位 Windows 上运行的子系统，负责在 32 位与 64 位执行环境之间进行转换，并处理注册表和文件系统重定向。按需功能（FoD）是指默认不安装的可选 Windows 组件，可通过 Windows Update、PowerShell 或 DISM 添加，这种做法在 Server Core 上很常见——Server Core 是不含完整桌面外壳的最小化 Windows Server 安装选项。由于 Server Core 没有图形界面，管理员通常使用 Add-WindowsCapability 这个 PowerShell 命令或 DISM 命令行工具来添加此类组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WoW64">WoW64 - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/zh-cn/windows/win32/winprog64/wow64-implementation-details">WOW64 实现详细信息 - Win32 apps | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#Windows Server`, `#WoW64`, `#32-bit compatibility`, `#Microsoft`, `#enterprise IT`

---

<a id="item-4"></a>
## [Meta AI 负责人称超级智能将至，人类控制权堪忧](https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk) ⭐️ 7.0/10

Meta 首席 AI 官、超级智能实验室负责人 Alexandr Wang 在 X 上发布长文，称超级智能已不再是&quot;未来某天&quot;的议题；他援引数学家 Levent Alpöge 借助 Anthropic 的 Claude 完成、并于周六经 Lean 与 Mathlib 社区机器校验的黎曼猜想证明作为证据。他警告说，人类将很难继续掌控能够无限自我改进、或聪明程度是人类 1000 倍的系统，并呼吁紧急投入安全、对齐与防护方面的研究。 这是一位前沿实验室负责人相当直白的公开表态，把超级智能的讨论从遥远的假想议题推向了近在眼前的安全问题。如果各家前沿实验室在内部采纳这一判断，可能会影响研究优先级、安全投入，以及整个行业对监管和外部监督的态度。 这一说法完全建立在二手信息之上：目前既没有发布人类可读的证明，也没有来自 Levent Alpöge、Anthropic 或 Lean/Mathlib 社区的第一手确认，因此在得到验证之前，这一黎曼猜想成果应被视为高度存疑。Wang 更具体的技术论点是：AI 与顶尖人类数学家之间的差距只剩三块——具体知识、工程整合与实验。

telegram · zaihuapd · 11月23日 12:49

**背景**: 黎曼猜想由 Bernhard Riemann 于 1859 年提出，是数学中最著名的未解难题之一，也是克雷数学研究所悬赏的&quot;千禧年大奖难题&quot;之一，涉及黎曼 zeta 函数零点位置。Lean 是一个开源的证明助手和函数式编程语言，数学家可以在其中把定理与证明编码，由机器逐步检查正确性。Mathlib 则是一个由社区驱动的大型 Lean 数学库，为研究级形式化提供所需的定义与引理。所谓&quot;机器校验的证明&quot;，是指 Lean 内核接受了该证明项，这比证明梗概或非正式论证要强得多；但它仍需要转换成人类可读的版本并经专家评审，才能被数学界正式接受。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://mathlib.org/">Mathlib</a></li>
<li><a href="https://leanprover-community.github.io/">GitHub Pages - Lean and its Mathematical Library</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#superintelligence`, `#AI alignment`, `#frontier AI`, `#formal verification`

---

<a id="item-5"></a>
## [蚂蚁集团领投 1 亿美元，中国具身智能公司 Simplexity 估值达 16 亿美元](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 6.0/10

2025 年 7 月在杭州成立的具身智能公司 Simplexity Robotics 完成 1 亿美元 pre-A 轮融资，由马云关联的蚂蚁集团领投，投后估值达 16 亿美元，老股东阿里巴巴、腾讯、HongShan（红杉中国）和蓝驰创投跟投。董事长兼联合创始人 Wang Kai 已向彭博确认该消息。 这轮融资表明中国头部互联网公司正集体将人形机器人与具身智能视为战略赛道，彭博称中国已占全球人形机器人出货量约 97%。这笔资金让一家成立仅一年多的初创公司有能力与宇树、优必选等在硬件上更成熟的厂商正面竞争。 Simplexity 核心团队来自理想汽车，贾鹏任 CEO、王佳佳任 COO；公司今年 3 月曾披露成立半年内完成五轮融资、累计 20 亿元人民币，当时投后估值已超 10 亿美元。本轮资金将用于与更成熟的机器人厂商争夺市场，而非对应某项已披露的技术突破。

telegram · zaihuapd · 11月23日 02:02

**背景**: 具身智能指通过实体在物理世界中感知并行动的 AI 系统，最典型的表现是结合大模型与硬件控制的人形机器人。中国人形机器人行业近年获得大量政府与民间投资，宇树和优必选是目前出货较为知名的厂商。蚂蚁集团作为马云关联、脱胎于阿里生态的公司，正把投资版图从支付与金融科技扩展到 AI 领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race">Ant Group Bets on Simplexity in China’s Humanoid Race - Bloomberg</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embodied_intelligence">Embodied intelligence</a></li>
<li><a href="https://www.unitree.com/">Robot Dog_Quadruped_Humanoid Robotics Company</a></li>

</ul>
</details>

**标签**: `#embodied-ai`, `#humanoid-robotics`, `#venture-funding`, `#china-tech`, `#industry-news`

---

<a id="item-6"></a>
## [GLM-5.4 向所有 GLM Coding Plan 用户开放，新增视觉能力并提升 50% 配额](https://x.com/ZixuanLi_/status/2124719275864670681) ⭐️ 6.0/10

智谱 AI 的 GLM-5.4 现已向所有 GLM Coding Plan 订阅用户开放，新增视觉能力，整体编程表现进一步增强。对于按周计算配额的套餐，GLM-5.4 的配额比 GLM-5.3 提高了 50%。 此次开放让 GLM-5.4 在没有涨价的情况下成为付费订阅者的主力编程模型，直接影响在 Claude Code、Cline、Kilo Code 等工具中使用 GLM 的开发者。把视觉能力整合进同一个模型，也让智能体能够读取截图、图表和 UI 设计稿，弥补了此前需要切换到独立视觉模型的短板。 50% 的配额提升专门针对按周计费的套餐，按月或按 token 计费的档位未必享受同等增幅。GLM-5.4 采用循环 Transformer（looped transformer）架构，通过让同一组权重多次迭代处理 token，在不膨胀参数量的前提下提升推理深度。

telegram · zaihuapd · 11月23日 04:47

**背景**: GLM 是智谱 AI（Z.ai）的大模型系列，该团队脱胎于清华大学，长期专注于中文理解、代码生成与复杂推理。GLM Coding Plan 是一项订阅服务（Lite 档约每月 18 美元起，Max 档约每月 168 美元），把 GLM 系列模型接入 Claude Code、Cline、OpenCode、Kilo Code 等第三方编程智能体与 IDE。与按 token 计费的 API 不同，这类套餐按配额窗口计量用量，因此配额提升本身就是公告中的重要一环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/subscribe">GLM Coding Plan — AI Coding Powered by GLM-5.4 &amp; GLM-5.3 ...</a></li>
<li><a href="https://wccftech.com/z-ai-debuts-glm-5-4-with-a-novel-looped-transformer-architecture-skipping-ai-benchmarks-entirely/">Z. ai Debuts GLM - 5 . 4 With a Novel Looped Transformer Architecture...</a></li>
<li><a href="https://codingplan.org/en/plans/glm">GLM Coding Plan Pricing 2026: Subscription Cost from $18/mo</a></li>

</ul>
</details>

**标签**: `#GLM-5.4`, `#AI coding`, `#model release`, `#multimodal`, `#developer tools`

---

<a id="item-7"></a>
## [Anthropic 限制 IPO 承销团队人数，禁止其为 AI 竞争对手服务](https://www.reuters.com/world/like-spacex-anthropic-ran-an-unusual-ipo-process-chafing-some-bankers-2026-11-22/) ⭐️ 6.0/10

在创纪录的 IPO 中，Anthropic 要求承销银行把参与交易的团队压缩到不超过 4 名资深银行家，并要求部分银行高管签署竞业协议：上市后六个月内不得为 OpenAI、Cursor、DeepSeek、Hugging Face 等竞争对手服务。公司还通过带个人水印、禁止保存的在线系统追踪文件浏览，并在路演前夕凌晨 2 点下发修正版招股书，只给投行留出数小时签字，导致部分银行家拒绝签署。 这一事件显示，当下最炙手可热的 AI 实验室对华尔街拥有多大的议价能力：一场上市就能强制规定人员配置、保密方式和交易后的执业限制，而这些条款银行平时几乎不会接受。它还引发了关于利益冲突和信息隔离的现实问题，因为同一批银行同时服务众多 AI 公司与投资者。 这些限制包括每支交易团队最多 4 名资深银行家、上市后六个月内不得为指定竞争对手工作，以及一套带水印的文档系统——它会记录谁浏览了哪份文件并禁止下载保存。凌晨 2 点左右下发、距离签字仅剩数小时的修正版招股书，被银行家视为部分人拒签的主要原因之一。

telegram · zaihuapd · 11月23日 05:15

**背景**: IPO 承销商是帮助公司上市的投资银行：它向投资者推介股票、组织路演和簿记建档，通常还承诺投入资金，以换取承销费用。承销 IPO 一般需要庞大的团队，而且银行往往同时服务许多客户，因此针对单一客户的竞业条款和极小规模的交易团队极不寻常。成立于 2021 年、开发 Claude 系列模型的 Anthropic 是估值最高的 AI 实验室之一，这使它在争抢上市角色的银行面前拥有罕见的议价权。被点名的对手覆盖 AI 编程（Cursor）、中国开源权重模型研发（DeepSeek）以及模型与数据集托管（Hugging Face），这些都是覆盖 AI 行业的银行可能提供服务的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_%28code_editor%29">Cursor (code editor)</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_%28Company%29">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#non-compete`, `#business news`

---

<a id="item-8"></a>
## [开源 nospeaker 用 MacBook 触控板振动“念”出文字](https://m.mydrivers.com/newsview/1167826.html?ref=https%3A//www.google.com/) ⭐️ 6.0/10

开发者 Cody Collier 开源了 nospeaker 工具，它把 MacBook Force Touch 触控板下方的触觉马达驱动频率提升到每秒 4000 次，使玻璃振动快到人耳可闻，从而重放 macOS 从文字合成的语音。 这是一个颇为引人注目的概念验证：普通的触觉硬件可以被推到音频级振动，从而变成一只粗糙的扬声器，这对硬件改造爱好者和触觉研究者显然很有吸引力。但该工具依赖私有框架、且只在单一机型上验证，因此它仍只是小众实验，而非实用的语音输出方案。 该工具每 10 毫秒从 macOS 语音合成中提取两个共振峰，连同响度和音高一起通过触控板重放，因此听感明显偏机器人；作者称输出在 100 Hz 到 4 kHz 范围内可闻，1 kHz 附近最清晰。它只能念文字，不能播放音乐或视频；它绕开苹果公开的触觉接口，调用私有框架 MultitouchSupport，需要 Force Touch 触控板，而且据称只在 M5 Max 的 MacBook Pro 上跑通。

telegram · zaihuapd · 11月23日 07:16

**背景**: 苹果的 Force Touch 触控板并没有物理按压动作，而是由触觉马达模拟按压；当把马达驱动到音频频率时，触控板表面就变成了一只微弱的高频扬声器。共振峰是人类声道谐振形成的频谱峰值，决定了元音和浊音的音色，而共振峰合成只用少数几个峰值来重建语音，这正是听感偏机器人的原因。MultitouchSupport 是苹果的私有框架，爱好者常用它读取触控板原始数据，但依赖私有框架的应用可能在 macOS 更新后失效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Kyome22/OpenMultitouchSupport">GitHub - Kyome22/OpenMultitouchSupport: This enables you ...</a></li>
<li><a href="https://cocoapods.org/pods/OpenMultitouchSupport">OpenMultitouchSupport on CocoaPods.org</a></li>

</ul>
</details>

**标签**: `#haptics`, `#open-source`, `#macOS`, `#speech-synthesis`, `#hardware-hacking`

---