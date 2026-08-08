---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
lang: zh
report: default
---

> 从 239 条内容中筛选出 11 条重要资讯。

---

1. [中国研发投入首次超过美国，2024 年居全球第一](#item-1) ⭐️ 8.0/10
2. [macOS 屏幕共享高危漏洞（CVE-2026-65400）无需密码即可登录](#item-2) ⭐️ 8.0/10
3. [微软 Edge 将禁用旧版 MV2 广告拦截器，uBlock Origin 再失阵地](#item-3) ⭐️ 7.0/10
4. [因人类仅识别 13.6%危险命令，Claude Code 默认启用自动模式](#item-4) ⭐️ 7.0/10
5. [xAI 发布 Imagine Image 2.0，Arena 排名第二](#item-5) ⭐️ 7.0/10
6. [月之暗面引入国资股东，推进赴港上市](#item-6) ⭐️ 7.0/10
7. [Claude Code 新增跨会话消息，AI 会话可互发通信](#item-7) ⭐️ 6.0/10
8. [X 推出原创内容奖励计划，停止旧版分成计划申请](#item-8) ⭐️ 6.0/10
9. [Dopamine 3.0 为 iOS 26 带来首个越狱，支持 A12/A13 设备](#item-9) ⭐️ 6.0/10
10. [腾讯将 WorkBuddy 列为战略级产品，领跑国内办公智能体](#item-10) ⭐️ 6.0/10
11. [115 网盘 API 开放平台将于 2026 年暂停服务](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [中国研发投入首次超过美国，2024 年居全球第一](https://www.nikkei.com/article/DGXZQOSG05ALB0V00C26A8000000/) ⭐️ 8.0/10

根据日本文部科学省《科学技术指标 2026》，2024 年中国研发投入达 97.1 万亿日元，同比增长 13.1%，超过美国的 95.3 万亿日元，位居全球第一；日本以 22.1 万亿日元排名第三。 这一里程碑标志着全球科技竞争格局的范式转变，显示中国从研发投入的追赶者转变为领先者，可能影响各国政策重点、企业战略以及整体国际技术竞争态势。 增长主要由企业研发投入推动，企业研发经费达 75.4 万亿日元，重点集中在计算机、电子和光学产品制造领域。此外，中国前 10%和前 1%高被引论文数量分别自 2018 年和 2019 年起领先全球。

telegram · zaihuapd · 8月8日 06:16

**背景**: 研发投入是衡量国家创新能力的重要指标。日本文部科学省定期发布《科学技术指标》，2026 年版统计了截至 2024 年的数据。中国科研论文数量已于 2017 年超过美国，如今企业主导的研发扩张反映了推动科技自主和产业升级的整体战略。

**社区讨论**: 本条新闻没有相关的社区评论。

**标签**: `#R&amp;D`, `#China`, `#science-policy`, `#economics`, `#technology`

---

<a id="item-2"></a>
## [macOS 屏幕共享高危漏洞（CVE-2026-65400）无需密码即可登录](https://x.com/calif_io/status/2086022794840793454) ⭐️ 8.0/10

安全研究人员公开了 macOS 屏幕共享中关键漏洞 CVE-2026-65400 的概念验证（PoC）利用程序，该漏洞允许网络攻击者在无需密码的情况下以任意账户身份登录。苹果已在 macOS 26.6.1 中修复此问题，并强烈建议用户立即升级。 这是一个影响严重的认证绕过漏洞，一旦屏幕共享处于开启状态，受影响的 Mac 可能面临未授权的远程访问风险。由于屏幕共享在远程管理和技术支持中被广泛使用，在安装补丁前被利用的可能性很大。 研究人员已逆向工程苹果的补丁，以厘清漏洞的根因与利用路径，完整技术分析计划于次日发布。该漏洞仅在启用屏幕共享的系统中存在影响，目前尚未透露其他利用前提。

telegram · zaihuapd · 8月8日 14:20

**背景**: 屏幕共享是 macOS 内置的一项功能，允许用户通过网络查看和控制另一台 Mac。CVE 标识符是公开披露的安全漏洞的标准命名方式，而 PoC 利用程序是一种无害的演示，用于证明漏洞真实存在。此问题已在 macOS 26.6.1 中修复，用户应尽快安装该更新以确保安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-65400">NVD - CVE - 2026 - 65400</a></li>
<li><a href="https://support.apple.com/guide/mac-help/share-the-screen-of-another-mac-mh14066/mac">Share the screen of another Mac - Apple Support</a></li>
<li><a href="https://www.techtarget.com/searchsecurity/definition/proof-of-concept-PoC-exploit">What is a Proof of Concept (PoC) Exploit?| Definition from ...</a></li>

</ul>
</details>

**标签**: `#security`, `#macOS`, `#vulnerability`, `#CVE`

---

<a id="item-3"></a>
## [微软 Edge 将禁用旧版 MV2 广告拦截器，uBlock Origin 再失阵地](https://www.theverge.com/tech/976880/microsoft-edge-extensions-ad-blockers-mv2-mv3) ⭐️ 7.0/10

微软 Edge 宣布将禁用 Manifest V2 \(MV2\) 扩展，包括 uBlock Origin，消费者用户过渡从本月开始，目标在 2026 年底前完成，企业用户支持则于 2027 年初终止。这紧随 Google Chrome 早前推出的同类淘汰计划。 又一款主流浏览器淘汰 MV2，将大幅减少 uBlock Origin 等功能强大的完整版广告拦截器的可用性。用户将被迫转向 uBlock Origin Lite 等功能较弱的 MV3 替代品，这可能会影响整个网络的广告拦截效果。 据微软称，Edge 商店中仅有 58 个 MV2 扩展拥有「实际使用量」，其中只有 3 个尚未提供 MV3 版本。Opera 表示将维持对现有 MV2 扩展的支持，「只要技术上合理就会继续」，Firefox 也是可选方案之一。

telegram · zaihuapd · 8月8日 01:14

**背景**: Manifest V3 \(MV3\) 是基于 Chromium 的浏览器的最新扩展平台，旨在提升隐私、安全和性能。它用 Service Worker 替代后台页面，并实施更严格的内容安全策略，从而限制了广告拦截器过滤网络请求的方式。uBlock Origin 是一款依赖 MV2 API 的流行开源广告拦截器；其兼容 MV3 的版本 uBlock Origin Lite 功能更少，追踪器拦截效果也较弱。这一过渡是 Google、微软等推动浏览器扩展现代化的更广泛行业举措的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V3 | Chrome for Developers</a></li>
<li><a href="https://adblock-tester.com/ad-blockers/ublock-origin-vs-ublock-origin-lite/">uBlock Origin Lite: Modes, Review &amp; Is It Good in 2026?</a></li>

</ul>
</details>

**标签**: `#Microsoft Edge`, `#Manifest V2`, `#uBlock Origin`, `#Ad blocking`, `#Browser extensions`

---

<a id="item-4"></a>
## [因人类仅识别 13.6%危险命令，Claude Code 默认启用自动模式](https://claude.com/blog/auto-mode-default-in-claude-code) ⭐️ 7.0/10

自 8 月 14 日起，Claude Code 将在 Pro、Max 和 Team 计划的新会话中默认启用自动模式。此模式下，每次工具调用都会经过分类器检查，以拦截不可逆、破坏性或超出用户环境的操作，且 Anthropic 不再向上述用户收取额外开销费用。 这一转变意义重大，因为它把智能体安全设置为默认而非自愿启用，针对了人类开发者漏看危险命令的已知弱点（识别率仅 13.6%）。这可能提高整个行业 AI 编程智能体的安全标准，并减轻权限提示疲劳，影响开发者与企业采用自主编程工具的方式。 自动模式最初于 2026 年 3 月推出，是一种由 Claude 在有安全防护下作出决策的权限模式，其分类器基于 Claude Sonnet 4.6。在一项涉及 1,053 名付费测试者的研究中，自动模式拦截了 89%的危险命令，而人类测试者仅识别出 13.6%；不过 Enterprise、Claude API 及部分云平台用户仍需手动启用，官方计划在未来一个月内逐步改为默认。

telegram · zaihuapd · 8月8日 03:02

**背景**: Claude Code 是 Anthropic 开发的智能体编程工具，可帮助开发者编辑文件、运行命令并更快交付软件。常规使用时，它会在执行许多操作前请求用户授权，而用户会批准其中约 93%的请求。自动模式用 AI 分类器取代了部分提示，由分类器自动判断操作是否安全，仅在操作不可逆、具有破坏性或针对用户环境之外时进行干预。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude by Anthropic</a></li>
<li><a href="https://code.claude.com/docs/en/auto-mode-config">Configure auto mode - Claude Code Docs</a></li>
<li><a href="https://www.anthropic.com/engineering/claude-code-auto-mode">How we built Claude Code auto mode: a safer way to skip permissions \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude Code`, `#Safety`, `#Developer Tools`

---

<a id="item-5"></a>
## [xAI 发布 Imagine Image 2.0，Arena 排名第二](http://grok.com/imagine) ⭐️ 7.0/10

xAI 已发布 Imagine Image 2.0，现作为 Quality Mode 在 grok.com/imagine 及 iOS、Android 应用中开放。该模型增强了生成和编辑能力，支持局部编辑、区域分割、透明背景导出和多图参考编辑等功能。 此次发布让一款重要的图像生成与编辑模型全面开放，使 xAI 在文生图和图像编辑领域位列顶级竞争者之列。随着 API 即将推出，它可能挑战图像生成市场的既有领先者。 Imagine Image 2.0 强化了指令理解、文字渲染、版式处理和多轮编辑中的内容保持能力。它支持单次输入最多 5 张参考图片进行生成，支持按比例生成和多种工作流模板。

telegram · zaihuapd · 8月8日 05:40

**背景**: Arena 排行榜基于用户盲测投票对 AI 图像生成和编辑模型进行排名，为模型质量提供公开基准。xAI 的 Grok 平台现已整合此模型，与其他前沿图像系统竞争，同时公司计划很快提供 API 访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arena.ai/leaderboard/image-edit">Image Editing AI Leaderboard - Best Models Compared</a></li>
<li><a href="https://arena.ai/leaderboard">Arena Leaderboard | Compare &amp; Benchmark the Best Frontier AI ...</a></li>
<li><a href="https://artificialanalysis.ai/image/leaderboard/editing">Image Editing Leaderboard - Top AI Image Models</a></li>

</ul>
</details>

**标签**: `#AI`, `#image-generation`, `#xAI`, `#image-editing`

---

<a id="item-6"></a>
## [月之暗面引入国资股东，推进赴港上市](https://www.theblockbeats.info//flash/360480) ⭐️ 7.0/10

据英国《金融时报》报道，月之暗面正在重组股权结构并引入多家国资背景投资者，以争取监管部门批准其赴港上市。上周，该公司已将中国境内主体由有限责任公司变更为股份有限公司，目前正与投行及律师协调解决海外投资者持股转移问题。 这标志着中国领先 AI 创业公司在监管趋严背景下推进上市的重要一步，也显示出国有资本对 AI 领域的支持。若以高达 500 亿美元的估值成功上市，将成为中国 AI 企业赴海外上市的标杆事件。 公司近期完成两轮融资，估值最高预计达 500 亿美元，股东名单已包括全国社保基金、上海及贵州地方政府引导基金以及人民日报旗下投资主体。此前市场传闻公司计划本月提交香港 IPO 申请、募资约 30 亿美元，月之暗面回应称消息不实。

telegram · zaihuapd · 8月8日 09:02

**背景**: 月之暗面是中国知名的 AI 创业公司，以其 Kimi 大模型闻名。中国企业赴境外上市通常需要获得监管部门批准，并且往往需要将境内主体改制为股份有限公司以满足上市要求。引入国资背景投资者有助于推进审批流程，并释放政策支持的信号。

**标签**: `#AI`, `#IPO`, `#Moonshot AI`, `#startup`, `#business`

---

<a id="item-7"></a>
## [Claude Code 新增跨会话消息，AI 会话可互发通信](https://code.claude.com/docs/en/cross-session-messaging) ⭐️ 6.0/10

Claude Code v2.1.224 起在 macOS 和 Linux 上支持跨会话消息功能，Claude 可通过 ListAgents 自动发现其他会话，并用 SendMessage 发送消息。该功能默认可用，支持会话间协调并行工作并回报长时间运行的任务状态。 该功能减少了在不同终端或 worktree 间重复解释上下文的麻烦，提升了多会话工作流中的开发效率。这也标志着 Claude Code 在实现更自主的多智能体协作方面迈出了一步。 消息仅为纯文本通信，不会绕过权限提示，接收方也无法修改配置或执行命令。该功能不支持原生 Windows，在 Amazon Bedrock、Google Cloud Agent Platform 等平台上不可用；用户可通过 crossSessionInbound 设置为 accept、hold 或 refuse 来控制入站消息。

telegram · zaihuapd · 8月8日 02:12

**背景**: Claude Code 是 Anthropic 推出的智能编程工具，在终端中运行 AI 会话。此前各会话相互隔离；本次更新引入了收件箱/发件箱模型，Claude 可以列出其他会话并传递消息，而无需用户直接调用这些工具。该功能在 macOS 和 Linux 上默认启用，需要 Claude Code v2.1.224 及以上版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/cross-session-messaging">Message your other Claude Code sessions - Claude Code Docs</a></li>
<li><a href="https://www.macrumors.com/2026/08/08/claude-code-adds-cross-session-messaging/">Claude Code Adds Cross-Session Messaging on macOS</a></li>
<li><a href="https://explainx.ai/blog/claude-code-cross-session-messaging-list-agents-2026">Claude Code Cross-Session Messaging Guide (2026) | explainx.ai</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI tools`, `#developer tools`, `#cross-session communication`, `#feature update`

---

<a id="item-8"></a>
## [X 推出原创内容奖励计划，停止旧版分成计划申请](https://x.com/XCreators/status/2085835082166653393) ⭐️ 6.0/10

X 宣布推出新的「原创内容奖励计划」，以取代原有的收益分成计划。旧版计划即日起停止新注册，现有参与者可在 9 月 7 日前继续获得收益，并将在 8 月 14 日、8 月 28 日及大约 9 月 11 日收到最后三笔付款。 这一转变标志着 X 对创作者报酬方式的重大调整，优先奖励原创内容，而非转发或低质量互动。这可能会重塑平台上的创作者变现策略，并对整个创作者经济生态产生影响。 要获得新计划资格，创作者必须年满 18 岁、订阅 X Premium（X 高级版）、拥有至少 500 名认证粉丝，并在近 90 天内获得 50 万次认证用户首页曝光。新计划每两周根据高级订阅用户带来的合格曝光结算一次，旧版计划成员可自 9 月 8 日起申请转入。

telegram · zaihuapd · 8月8日 05:17

**背景**: X（原 Twitter）此前运行着一个收益分成计划，根据回复线程中展示的广告向创作者支付报酬。新的「原创内容奖励计划」旨在奖励体现创作者独特声音的原创报道、分析、帖子、照片、视频、梗图或图形。此次变更延续了 X 在马斯克收购后推动高质量原创内容的大方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/08/x-replaces-misaligned-revenue-sharing-program-with-original-content-rewards/">X replaces ‘misaligned’ revenue sharing program with Original ...</a></li>
<li><a href="https://help.x.com/en/using-x/original-content-rewards">Original Content Rewards Program - help.x.com</a></li>
<li><a href="https://arynews.tv/x-launches-original-content-rewards-program">X launches Original Content Rewards Program</a></li>

</ul>
</details>

**标签**: `#social media`, `#monetization`, `#X`, `#creators`, `#content rewards`

---

<a id="item-9"></a>
## [Dopamine 3.0 为 iOS 26 带来首个越狱，支持 A12/A13 设备](https://www.macrumors.com/2026/08/07/ios-26-dopamine-jailbreak/) ⭐️ 6.0/10

由 Lars Fröder（opa334）开发的 Dopamine 3.0 新增了对 iOS 26.0 和 26.0.1 的支持，适用于 A12 和 A13 芯片设备，成为首个支持 iOS 26 的越狱工具。该版本还将兼容范围扩展到所有运行 iOS 16.5.1 至 17.3.1 的设备。 这一发布对越狱和 iOS 安全社区意义重大，因为它表明即使苹果不断加强防护，最新版的 iOS 系统仍然可以被越狱。它为 iPhone XS/XR 和 iPhone 11 系列用户带来了定制化与安全研究的可能性。 该越狱仅支持搭载 A12 或 A13 芯片的设备，包括 iPhone XS、XR 及 11 系列。此前版本支持 iOS 15 和 16，而新版本还将兼容范围扩展到所有运行 iOS 16.5.1 至 17.3.1 的设备。

telegram · zaihuapd · 8月8日 07:00

**背景**: Dopamine 是一款半绑定（semi-untethered）的 rootless 越狱工具，最初面向 iOS 15 和 16。Rootless 越狱只允许写入文件系统的特定部分，而非完全根目录访问。值得注意是，安全研究人员在 A12 和 A13 芯片中发现了一个无法修补的 SecureROM 漏洞，这有助于解释为何这些较旧的设备能够支持 iOS 26 越狱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/opa334/Dopamine">GitHub - opa334/ Dopamine : Dopamine is a semi-untethered jailbreak ...</a></li>
<li><a href="https://ellekit.space/dopamine/">Dopamine Jailbreak</a></li>
<li><a href="https://icymi.in/article/a12-a13-apple-devices-face-an-unpatchable-securerom-vulnerability">A 12 &amp; A 13 Apple devices face an unpatchable SecureROM vulnerability</a></li>

</ul>
</details>

**标签**: `#jailbreak`, `#iOS security`, `#Dopamine`, `#iOS 26`, `#cybersecurity`

---

<a id="item-10"></a>
## [腾讯将 WorkBuddy 列为战略级产品，领跑国内办公智能体](https://mp.weixin.qq.com/s/TRUjakoaprGFSYYQB301xw) ⭐️ 6.0/10

腾讯已将 WorkBuddy 列为内部战略优先级最高的 AI 产品之一，据称是继 QQ、微信之后的第三个战略级产品。易观数据显示，2026 年二季度 WorkBuddy 以 2097 万次 PC 端月访问量位居国内办公智能体平台第一，月活约 2000 万，日活达百万级别。 此举表明腾讯将其 AI 智能体业务整合到 WorkBuddy 之下，企业办公 AI 成为战略要地。凭借约 2000 万月活，WorkBuddy 是中国 AI 智能体市场的领先者，将影响企业采用 AI 办公自动化的方式。 WorkBuddy 已接入腾讯文档、企业微信、腾讯会议等生态，支持混元、DeepSeek、GLM 等多种模型。目前仍处投入阶段，未设商业化 KPI，年内重点是扩大企业客户覆盖；今年 7 月，腾讯将 QClaw 相关业务调整至 WorkBuddy 所在部门，多线探索收口。

telegram · zaihuapd · 8月8日 13:50

**背景**: WorkBuddy 是腾讯推出的办公 AI 智能体，基于多智能体协作，可自动拆分复杂任务并交付报告、演示文稿、表格等成品。QClaw 是腾讯推出的个人 AI 助手，可通过微信等应用远程执行任务。办公智能体是一类通过自然对话完成实际知识工作（如生成文档、分析数据）的 AI 助手，是办公软件中快速增长的新品类。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.workbuddy.ai/">WorkBuddy - AI Agent for Everyday Office Work</a></li>
<li><a href="https://copilot.tencent.com/work/">WorkBuddy - AI Agent 办公新范式 - copilot.tencent.com</a></li>
<li><a href="https://www.tencent.com/en-us/articles/2202318.html">Tencent Launches QClaw Globally, Lowering Barriers to AI ...</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#AI agents`, `#office automation`, `#China tech`

---

<a id="item-11"></a>
## [115 网盘 API 开放平台将于 2026 年暂停服务](https://q.115.com/115/T976421.html#) ⭐️ 6.0/10

8 月 8 日，115 网盘 API 开放平台宣布将于 2026 年 8 月 9 日 0:00 起暂停服务。公告未给出恢复时间，仅表示以官方公告为准。 这将影响所有依赖 115 官方 API 实现直链和文件操作的第三方工具、NAS 设备和播放器。115 生态内的开发者和用户可能面临服务中断，但两年的过渡期提供了迁移时间。 该 API 平台支持文件上传、下载、分享、重命名、移动、删除、查询及部分播放能力。此次暂停之前，115 网盘已启动针对违规使用的专项治理。

telegram · zaihuapd · 8月8日 19:48

**背景**: 115 网盘是中国的一款云存储服务。其 API 开放平台约在 1 月下旬开始内测，允许开发者构建第三方客户端并将 115 存储集成到应用中。NAS（网络附属存储）是一种连接网络的存储设备，常用于家庭影音中心；CD2 等许多 NAS 软件和播放器都通过 115 官方 API 直接访问文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aishare.jizhiku.net/archives/38771">115网盘API开放平台暂停，第三方服务或面临集体下线 - AI技能智慧站</a></li>
<li><a href="https://www.miwap.com/978.html">115网盘推出Api开放平台/115网盘内测开发者API服务进行远程调用</a></li>
<li><a href="https://tieba.baidu.com/p/9548446283">115open和115有何区别？官方API与风控差异解析</a></li>

</ul>
</details>

**标签**: `#115网盘`, `#API`, `#cloud storage`, `#NAS`, `#suspension`

---