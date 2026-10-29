---
layout: default
title: "Horizon Summary: 2026-10-29 (ZH)"
date: 2026-10-29 23:03:53 +0000
lang: zh
report: default
---

> 从 195 条内容中筛选出 6 条重要资讯。

---

1. [Anthropic 借助 Claude 用 Rust 重写 Messages API，CPU 用量下降 40%–50%](#item-1) ⭐️ 7.0/10
2. [谷歌开放第三方安卓应用商店注册，年费 1 万美元](#item-2) ⭐️ 7.0/10
3. [美国土安全部逾 4.1 万员工信息经 Okta 泄露](#item-3) ⭐️ 7.0/10
4. [Google 将 AI 模式搜索广告推向全球，核心广告增长放缓](#item-4) ⭐️ 6.0/10
5. [群晖 NAS 用户遭遇 LOCK3D 勒索攻击](#item-5) ⭐️ 6.0/10
6. [Claude 企业版智能报告可标记员工偏离工作的 AI 使用](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 借助 Claude 用 Rust 重写 Messages API，CPU 用量下降 40%–50%](https://latent.space/p/opus55/) ⭐️ 7.0/10

Anthropic 将原本运行在单一 GCP 区域的 Python 单体 Messages API 整体迁移到 Rust，由 Claude 负责生成代码实现，工程师则负责系统设计与验证。迁移后 CPU 用量降低约 40% 至 50%，首个 token 的响应时间缩短约 10% 至 20%。 这是一份来自头部 AI 公司的量化案例：既展示了用 Rust 重写关键生产服务的真实收益，也说明 AI 辅助编程已被用于真正的系统工程，而不只是玩具示例。对于正在权衡语言迁移、或想知道 AI 生成代码能走多远的团队来说，这是一个有具体数据支撑的参考。 值得注意的是，项目启动时团队里 reportedly 没有任何 Rust 开发者，验证方式是对照新旧系统的输出来做差分比对，而不是重写测试或逐行人工审查。公布的收益集中在 CPU 用量和首 token 延迟两项指标上，并不涉及 GPU 算力或整体推理吞吐。

telegram · zaihuapd · 10月29日 03:13

**背景**: Messages API 是开发者调用 Claude 模型的核心接口：请求里带上文本和图像的对话内容，返回下一条助手消息，因此它位于每个请求的关键路径上。首 token 时间（TTFT）指从发出请求到收到回复第一个片段之间的延迟，其中包含网络传输、排队等待，以及模型读取整个提示词的 prefill 阶段，所以服务端的 CPU 效率会直接影响用户感知到的响应速度。Rust 是一门无需垃圾回收即可保证内存安全的系统级语言，常被用于那些因流量增长而超出 Python 承载能力的、对延迟和 CPU 敏感的服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/api/messages">Messages - Claude API Reference - Anthropic</a></li>
<li><a href="https://lyceum.technology/magazine/time-to-first-token-what-actually-determines-llm/">Time to first token (TTFT): what drives LLM API latency</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Anthropic`, `#Claude`, `#AI-assisted development`, `#performance optimization`, `#code migration`

---

<a id="item-2"></a>
## [谷歌开放第三方安卓应用商店注册，年费 1 万美元](https://www.landian.news/archives/127767.html) ⭐️ 7.0/10

谷歌正式开放“Android Registered App Stores（注册应用商店）”计划的申请，通过审核的第三方应用商店可获得一键安装与后台静默自动更新等系统级权限，用户从这类商店安装应用时不再需要逐次确认系统弹窗。该计划为自愿参加、仅限美国以外的指定地区，自 2026 年 12 月 1 日起在 Android 17 QPR2 及以上设备启用，年费为 1 万美元。 这是谷歌首次向外部分发方开放与 Play 商店同等的“无摩擦”安装与更新体验，可能让第三方商店在安卓上第一次具备真正的竞争力。但 1 万美元年费和完整应用库送审的要求，意味着这一开放主要利好 Epic Games、亚马逊等大型厂商，而中小型和开源分发平台实际上被挡在门外。 申请方必须持有企业开发者账号，并将完整应用库交由谷歌进行安全扫描，而且这些权限只在指定的美国以外地区生效，并非全球通用。该计划要到 2026 年 12 月的 Android 17 QPR2 才落地，距离在量产设备上实际可见仍有相当长的等待期。

telegram · zaihuapd · 10月29日 04:39

**背景**: 安卓历来允许用户从任意来源侧载应用，但每次安装都要经过繁琐的确认弹窗，而谷歌近年通过开发者验证规则不断收紧对未验证侧载应用的限制。QPR 即“季度平台发布”（Quarterly Platform Release），是谷歌对安卓的季度更新机制，2025 年 12 月发布的 Android 16 QPR2 就是首个采用次要 SDK 版本的版本。此次新计划是谷歌 2026 年对 Play 经济体系整体调整的一部分，此前谷歌已将标准抽成降至 20% 并支持第三方支付，这些变化与 Epic 诉谷歌案的裁决压力密切相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ic.work/article/google-android-registered-app-stores-launch-december-1-10k-a">Google Android Registered App Stores 12月1日上线，年费1万美元换一...</a></li>
<li><a href="https://developer.android.com/blog/posts/android-16-qpr-2-is-released?hl=zh-cn">Android 16 QPR2 已发布 - Android Developers&#x27; Blog</a></li>
<li><a href="https://support.google.com/googleplay/android-developer/answer/17118006?hl=zh-Hans">加入“Google Play 上的第三方应用商店”计划 - Play 管理中心帮助</a></li>

</ul>
</details>

**标签**: `#Android`, `#app stores`, `#Google`, `#mobile platforms`, `#platform policy`

---

<a id="item-3"></a>
## [美国土安全部逾 4.1 万员工信息经 Okta 泄露](https://www.theverge.com/tech/1021528/ice-cbp-data-leak) ⭐️ 7.0/10

一个自称“和平部”（Department of Peace）的黑客组织据称通过美国国土安全部（DHS）使用的 Okta 身份管理服务，获取了超过 4.1 万名 DHS 员工的记录。该数据集由 DDoSecrets 以“Icepick”名义托管，包含姓名、职务、电话、邮箱和办公地点，其中约 2.1 万条属于海关与边境保护局（CBP），近 7000 条属于移民与海关执法局（ICE）。 此次泄露涉及 DHS 下属的移民执法、海关和网络安全机构人员，可能让联邦雇员面临钓鱼攻击、精准定位和社会工程攻击的风险。它也凸显出第三方身份与访问管理平台可能成为敏感员工数据的高价值集中点。 目前描述的泄露字段属于目录型信息，并未明确说明包含凭据，但 DHS 未回应置评请求，完整影响范围仍未确认。据称“Icepick”数据集还包含这些机构可用的监控工具信息。

telegram · zaihuapd · 10月29日 07:04

**背景**: 美国国土安全部是负责移民执法、海关、边境安全和网络安全协调的联邦部门，ICE、CBP 和 CISA 都是其下属机构。Okta 是一个广泛使用的身份与访问管理平台，集中处理员工和应用程序的身份认证、单点登录与访问控制。DDoSecrets 成立于 2018 年，是一个常被称为 WikiLeaks 后继者的泄密发布网站，此前曾发布过大量政府和公司数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Okta,_Inc.">Okta, Inc. - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DDoSecrets">DDoSecrets</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cybersecurity_and_Infrastructure_Security_Agency">Cybersecurity and Infrastructure Security Agency - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#Okta`, `#DHS`, `#privacy`

---

<a id="item-4"></a>
## [Google 将 AI 模式搜索广告推向全球，核心广告增长放缓](https://techcrunch.com/2026/10/28/google-expands-ai-search-ads-globally-as-core-ad-growth-slows/) ⭐️ 6.0/10

在第三季度财报电话会议上，Alphabet 宣布将 AI 模式搜索广告扩展至全球更多市场，新增加拿大、印度等 10 个国家，并在美国推出支持多轮对话的对话式广告。公司表示，AI 模式中赞助商品列表的点击率已接近自然搜索结果。 这是 Google 迄今为止将生成式 AI 搜索转化为实际收入来源的最直接尝试，意在防止 AI 回答蚕食传统付费链接。与此同时，搜索广告收入同比增速从前两个季度的 17% 和 19% 降至 12%，Alphabet 股价盘后一度跌超 10%，显示投资者对 AI 搜索的变现能力日益焦虑。 Alphabet 第三季度营收达 1276 亿美元，同比增长 25%，但搜索广告增速明显放缓。管理层还预警第四季度搜索收入将继续承压，云业务利润率也面临短期压力，同时将 AI 模式中接近持平的点击率视为新广告形式的早期积极信号。

telegram · zaihuapd · 10月29日 01:43

**背景**: Google 的 AI 模式是一种对话式搜索体验，于 2025 年 3 月推出，由 Gemini 模型驱动，直接生成综合答案而非链接列表。由于用户往往无需点击网站即可获得答案，AI 模式对内容发布者的流量和 Google 传统的按点击付费广告模式都构成威胁，因此公司一直在测试由 Gemini 构建的原生广告形式，例如对话式广告、高亮答案赞助展示和 AI 购物广告。将这些形式推向全球，正是 Google 在 AI 优先的搜索时代维持广告收入增长的核心计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/products/ads-commerce/ads-in-ai-mode-global/">Ads in AI Mode expand to 10 new countries - The Keyword</a></li>
<li><a href="https://blog.google/products/ads-commerce/google-marketing-live-search-ads/">New ad formats built with Gemini coming to Google Search</a></li>
<li><a href="https://wallstreetcn.com/articles/3784718">谷歌电话会：承认 AI 搜 索 变现偏低，TPU...</a></li>

</ul>
</details>

**标签**: `#Google`, `#AI search`, `#advertising`, `#monetization`, `#tech business`

---

<a id="item-5"></a>
## [群晖 NAS 用户遭遇 LOCK3D 勒索攻击](https://www.v2ex.com/t/1252735) ⭐️ 6.0/10

一份安全公告称，正在活跃的 LOCK3D 勒索活动会加密群晖 NAS 上的文件并追加 .LOCK3D 或 .L0CK3D 后缀，V2EX 上还有用户反映最新 DSM 版本也中招。 群晖 NAS 被大量自建用户和小型企业使用，因此这场活跃的勒索攻击可能造成直接的数据丢失，也促使管理员减少公网暴露并核验离线备份。 公告建议用户检查异常文件后缀和勒索信，关闭不必要的公网服务，更新套件及容器镜像，并核验 NAS 无法写入的离线或异地备份；若已中招，应断网隔离并保留日志和勒索信。

telegram · zaihuapd · 10月29日 05:22

**背景**: LOCK3D 是一种会加密文件并追加 .LOCK3D 或 .L0CK3D 后缀的勒索软件；TerraMaster 论坛上也有类似针对 NAS 的攻击报告，说明这类恶意软件并非只针对单一品牌。群晖 NAS 运行的是 DSM 系统，用户常通过公网访问、套件和容器提供文件共享等服务，暴露面越大风险越高。集中存放数据的 NAS 一旦被加密影响面很大，因此需要把 DSM、套件和容器镜像及时更新，并保留离线或异地不可写备份。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forum.terra-master.com/en/viewtopic.php?t=3940">Urgent! . LOCK 3 D ransomware is attacking your TNAS | Forum</a></li>
<li><a href="https://www.backblaze.com/blog/nas-ransomware-guide-how-to-protect-your-nas-from-attacks/">NAS Ransomware Guide: How to Protect Your NAS From Attacks</a></li>
<li><a href="https://kb.synology.com/en-sg/DSM/help/DSM/MainMenu/security?version=7">Security | DSM - Synology Knowledge Center</a></li>

</ul>
</details>

**标签**: `#security`, `#ransomware`, `#NAS`, `#Synology`, `#backup`

---

<a id="item-6"></a>
## [Claude 企业版智能报告可标记员工偏离工作的 AI 使用](https://mashable.com/tech/claude-smart-reports-anthropic-ai-worker-overview) ⭐️ 6.0/10

Anthropic 已将 Claude Enterprise 智能报告正式开放，管理者可以查看团队过去 28 天的 AI 使用情况、费用、产出，以及被标记为个人或偏离工作话题的对话。付费 Claude Enterprise 用户每月最多可免费生成 10 份报告。 该功能将 AI 治理进一步推向员工行为监控，一方面为企业提供更清晰的投入产出和合规数据，另一方面也引发了关于员工 AI 对话如何被分析的隐私与信任问题。它可能影响企业如何制定可接受的 AI 使用政策，以及供应商向管理者提供多大可见度。 智能报告是 Claude Enterprise 一轮更广泛更新的一部分，同时还包括池化团队预算和应用内调查，这些功能在测试后均已正式开放。可用性会因配置而异，包括采用 HIPAA 配置或客户管理加密密钥的组织。

telegram · zaihuapd · 10月29日 07:49

**背景**: Claude 是 Anthropic 的大语言模型和 AI 助手系列，Claude Enterprise 则是面向企业、带有管理和合规控制的版本。智能报告旨在通过汇总使用情况、成本和产出，让组织了解 AI token 花费到底带来了什么。监控哪些员工对话属于“个人”或“偏离工作”，则触及了长期以来关于职场隐私和 AI 可接受使用政策的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets">Smart reports , surveys, and pooled group... | Claude by Anthropic</a></li>
<li><a href="https://explainx.ai/blog/claude-enterprise-smart-reports-surveys-pooled-group-budgets-token-spend-roi-2026">Claude Enterprise Smart Reports : See What Spend Buys | explainx.ai</a></li>
<li><a href="https://www.zdnet.com/innovation/claude-enterprise-efficiency-cost-tracking/">These Claude Enterprise features let you track AI ROI... - ZDNET</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude Enterprise`, `#AI monitoring`, `#workplace privacy`, `#enterprise AI`

---