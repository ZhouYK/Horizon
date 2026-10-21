---
layout: default
title: "Horizon Summary: 2026-10-21 (ZH)"
date: 2026-10-21 23:03:37 +0000
lang: zh
report: ai
---

> 从 172 条内容中筛选出 10 条重要资讯。

---

1. [eMudhra 中间 CA 私钥泄露，全球信任库被迫紧急更新](#item-1) ⭐️ 9.0/10
2. [PHP 紧急发布 RCE 补丁，CVE 信息提前泄露](#item-2) ⭐️ 8.0/10
3. [Anthropic 预览个人 AI 代理 Claude Duet](#item-3) ⭐️ 7.0/10
4. [沃尔玛推出新工具，允许 AI 智能体代客购物](#item-4) ⭐️ 6.0/10
5. [将人工智能写入宪法：算法国家的全球宪制时刻 - www.iconnectblog.com](#item-5) ⭐️ 6.0/10
6. [哈佛数学家就 AI 在科研与教学中的作用产生分歧](#item-6) ⭐️ 6.0/10
7. [辛顿：AI 有 1%概率毁灭人类，但我不是末日论者](#item-7) ⭐️ 6.0/10
8. [前政府官员敦促哥伦比亚特区巡回上诉法院重审 Anthropic 与五角大楼案裁定](#item-8) ⭐️ 6.0/10
9. [《纽约时报》：中国免费 AI 模型前景陷入不确定](#item-9) ⭐️ 6.0/10
10. [同一 AI 查询在得州比在瑞典排放更多二氧化碳](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [eMudhra 中间 CA 私钥泄露，全球信任库被迫紧急更新](https://simonwillison.net/2026/Oct/20/emudhra-certificates/) ⭐️ 9.0/10

印度证书机构 eMudhra 的 8 张中间 CA 证书私钥遭到泄露，这些中间证书链上的根证书被 Mozilla、Microsoft、Apple 和 Chrome 根证书计划以及众多下游信任库所信任。Mozilla 在 10 月 17 日收到报告后约 3 小时内即向 Firefox 用户推送封锁，Google 同日屏蔽受影响的公钥并计划于 10 月 27 日移除相关根证书，同时 uv 0.13.4、pip 26.2.2 和 certifi 2026.10.19 等已发布包含更新证书列表的版本。 任何掌握泄露中间 CA 私钥的人都能为任意域名签发看似合法的 HTTPS 证书，从而搭建极具迷惑性的钓鱼网站或实施流量劫持，因此这起事件的严重程度可与 DigiNotar 事件相提并论。由于影响范围横跨操作系统、浏览器、Linux 发行版和语言级证书包，所有内置或缓存可信证书列表的软件都必须更新。 据随附报道，受影响私钥的随机性极弱，仅有约 256 种可能，几秒内即可被穷举还原——其中 6 张证书可用于签发 TLS 服务器证书，2 张可用于代码签名。修复工作按生态碎片化推进：Linux 发行版需要发布新的 ca-certificates 软件包，Python 用户则需升级到 uv 0.13.4、pip 26.2.2 或 certifi 2026.10.19（及更高版本），另有一个专门的追踪网站和 GitHub 仓库持续跟进各项目的进展。

rss · Simon Willison · 10月20日 23:50

**背景**: 公钥基础设施依赖一条“信任链”：离线的根 CA 签发中间 CA 证书，中间 CA 再签发网站和代码所使用的终端证书。浏览器和操作系统内置根证书库，在连接 TLS 站点时会沿证书链一路验证到受信任的根证书。Python 的 certifi 包内置了 Mozilla 维护的 CA 列表，Linux 发行版则在 ca-certificates 软件包中提供类似集合，因此一张被攻破的中间证书必须在所有这些位置分别吊销，而不存在单一的中心化处理点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://khimananda.com/blog/root-ca-vs-intermediate-ca">Root CA vs Intermediate CA: PKI Security Guide 2026</a></li>
<li><a href="https://deepwiki.com/certifi/python-certifi">certifi/python-certifi | DeepWiki</a></li>
<li><a href="https://github.com/FiloSottile/mkcert">FiloSottile/mkcert: A simple zero-config tool to make locally trusted ...</a></li>

</ul>
</details>

**社区讨论**: 随新闻流传的评论语气相当直白，把这家 CA 称为“草台”，批评其生成的私钥熵值过低，仅 256 种取值、几秒钟就能穷举完毕。讨论的重点在于：一家被公开信任的 CA 出现如此基础的实现失误，会动摇整个证书信任模型，同时也对 Mozilla 和 Google 异常迅速的响应表示关注。

**标签**: `#security-incident`, `#PKI`, `#TLS-certificates`, `#certificate-authority`, `#supply-chain-security`

---

<a id="item-2"></a>
## [PHP 紧急发布 RCE 补丁，CVE 信息提前泄露](https://simonwillison.net/2026/Oct/21/php-security-release/) ⭐️ 8.0/10

2026 年 10 月 21 日，PHP 项目为 PHP 8.2 至 8.5 发布带外安全更新（8.2.35、8.3.36、8.4.27 和 8.5.12），修复两个远程代码执行漏洞 CVE-2026-109618 与 CVE-2026-109619，CVSS 评分均为 9.2。由于 CVE 编号于 10 月 20 日提前泄露、利用概念验证开始流传，官方将原定 10 月 22 日的发布时间提前了一天。 PHP 支撑着包括 WordPress 和 Drupal 在内的大量网站，而在 mod\_php 等常见部署方式下，这些漏洞可在业务代码执行前触发，因此任何暴露在公网的 PHP 8.x 实例都面临直接风险。信息提前泄露与 PoC 快速扩散意味着必须立即修补，而不能按常规节奏处理。 这两个漏洞性质不同：一个源于内存耗尽时的异常处理，使未初始化的数据进入清理流程；另一个是释放后使用问题，失效的内部状态会残留到后续请求，攻击者可能借此以 Web 工作进程的权限执行代码。官方仅为受支持分支（8.2–8.5）提供正式版本，但额外为 7.4、8.0 和 8.1 发布了最小化源码补丁；PHP 基金会的复盘还指出，泄露的 CVE 编号附带了错误的发布时间和被夸大的 10.0 评分，而某安全公司误发布的 PoC 视频加速了漏洞利用的开发。

rss · Simon Willison · 10月21日 18:41

**背景**: CVE 编号是公开披露漏洞时使用的标准标识，CVSS 则是 0 到 10 的严重性评分体系，9.0 及以上属于“严重”级别。协同漏洞披露是指先给厂商留出修补时间、再公开细节的做法；一旦保密期被打破，防御方就失去了“补丁发布到利用出现”之间的缓冲窗口。PHP 是一种开源的服务器端脚本语言，被大量网站使用，目前其安全流程由 PHP 基金会负责。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System">Common Vulnerability Scoring System - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure - Wikipedia</a></li>

</ul>
</details>

**标签**: `#PHP`, `#security`, `#vulnerability-disclosure`, `#remote-code-execution`, `#open-source`

---

<a id="item-3"></a>
## [Anthropic 预览个人 AI 代理 Claude Duet](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNSFZYTW81ai1KaU91ZGZUV1VlUkFrRkVfWVpraWlRMl9rWXJnUXV2cnZ3dlFBUUtCeldidHR0MVhJdmY3MGVzSzZDYnYxODNQNXdxS1Z5ZVNIcHd4bklybjBOR3hQeEhwUkFBVW1WdVA1Q0V2WTZfbFAwSVdPcVRKdG5jc3dhYzZiYm01X1hqbDR2ZlVtblF6NmZUWVV0TFlVSkZJWHJUeG_SAa4BQVVfeXFMUDZ1eGN2Uncyczl3by1yNFAxQlJfd2JmSDBaX05QaEpFb0tGY3FJWGY4R2RzcXBRMXRYdzFhTWFIVEluT0I5MExZZG9hX3U0MXliVFJYS3hxN0FtME5obUdWOW9CZTBYdkpsVXFHN2d1VXp2VVI2NG5BNFF4MkEwLTlmZkVWZ016RkRtRHNsUi1RSEVERG1SNzB2aFlVLXFNSF80dEtDUnNZN05RSlh3?oc=5) ⭐️ 7.0/10

Anthropic 于 2026 年 10 月 21 日宣布预览 Claude Duet，这是一款面向小企业和专业人士的个人 AI 代理，并已开放等候名单。 此次发布使 Anthropic 进入快速增长的个人代理市场，与 Meta 的 Muse 和 OpenAI 的 Dots 展开竞争，也标志着从对话式聊天机器人转向能处理收件箱、日历和后续事项的助手。 Claude Duet 被描述为一款用户可以通过消息交互的个人 AI 代理，能处理收件箱、日历和后续事项，并在有事情需要用户处理时主动发消息提醒。预览和等候名单意味着访问权限有限，全面开放的时间等细节尚未公布。

google\_news · CNBC · 10月21日 21:42

**背景**: Anthropic 是 Claude 聊天机器人背后的 AI 公司，Claude Duet 是其进军代理式助手领域的一步，这类助手不仅能回答提示，还能执行任务。Meta 的 Muse 和 OpenAI 的 Dots 等个人 AI 代理旨在连接应用并处理多步骤任务，OpenAI 在 2026 年 9 月底的 DevDay 大会上推出了 Dots。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/10/21/anthropic-preview-of-claude-duet-personal-ai-agent-take-on-muse-dots.html">Anthropic preview of Claude Duet, personal AI agent take on ...</a></li>
<li><a href="https://claude.com/product/claude-duet">Claude Duet | Your personal AI assistant</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/openai-follows-meta-into-the-red-hot-market-for-personal-agents.html">OpenAI follows Meta into the red-hot market for personal agents</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI agents`, `#product announcement`, `#AI/ML`

---

<a id="item-4"></a>
## [沃尔玛推出新工具，允许 AI 智能体代客购物](https://news.google.com/rss/articles/CBMiywFBVV95cUxONUhOU1BONzZmZHJsa0thYXhuNWZ1enBCZ3FOaXpaNUg4NjRSX2dsWmFfalZlNl9Sald4YVhzREhpeXpGeV8tNG1TOG9OT0puYWNLMWpxQWRycXZzUmkwa19CcDV5aDY5SWI0clEtZ1JBNTRkN1RmVDR2cm5MRVJmVkZrTkFmQjFMbXhESFNIU1p5VzY2TndhZDhYM2x3ZmxHNEFDNkM5V2gwNVB0QUZMLWVYOEZBZWl2Sy1iMWhhajRraW45bm9ROTVqNA?oc=5) ⭐️ 6.0/10

据《世界报》（Le Monde.fr）报道，沃尔玛宣布推出一套工具，旨在让 AI 智能体代替顾客完成购物。此举使沃尔玛成为公开支持“智能体电商”的最大零售商之一，在这一模式下，由自主运行的软件而非人工点击来完成商品搜索与购买流程。 如果沃尔玛这种体量的零售商把 AI 智能体浏览和下单的方式标准化，智能体电商就可能从试验性尝试变成主流渠道，进而改变商品被发现的方式以及商家争夺“机器可读”注意力的方式。这也会给其他大型电商平台带来压力，迫使它们要么向智能体开放，要么将其拒之门外。 目前可获得的报道仅为一则标题，因此诸如沃尔玛支持哪些智能体协议或 API、哪些商品品类适用、以及支付与账户授权如何完成等技术细节均未披露。总体而言，智能体电商需要机器可读的商品数据、对智能体友好的结账流程，以及可委托给软件执行的支付机制。

google\_news · Le Monde.fr · 10月21日 22:08

**背景**: 智能体电商（agentic commerce，也称 agent-based commerce）指的是一种新兴的电子商务形态：半自主或完全自主的 AI 智能体可代表用户独立搜索商品、比较选项、做出购买决策并完成支付，无需真人实时参与。它融合了生成式 AI、自主智能体、API 与数字支付基础设施。这种模式仍存在争议：据报道，包括亚马逊在内的一些大型电商平台已开始限制外部 AI 购物智能体在其站点上浏览和下单，使得“智能体准入”成为新的竞争焦点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_commerce">Agentic commerce</a></li>
<li><a href="https://teckhustlers.com/amazon-blocks-ai-shopping-agents-google/">Amazon Is Locking AI Shopping Agents Out, and... - Teck Hustlers</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#e-commerce`, `#retail`, `#agentic AI`, `#Walmart`

---

<a id="item-5"></a>
## [将人工智能写入宪法：算法国家的全球宪制时刻 - www.iconnectblog.com](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOYkpNYzYxc2h1TzBFdDRXTXZqR3dQQnB1VUg2YUF2d2VoZW8taURPSjFRd3V0X0gtVmlmMG8zb19jeUdaNWY5bVFyaFFrcjNSV1JNNG5WWjlSMTN0NlgxZXdCcHYwMlViZFp6Qk5sRzFrXzlWUGpNUUVScmlRcFo2SUpPOHJycUM5N0w3WGVkNmc0Z3V1UzE1S0FpUjh4cnJXbEE4YlVUM1RkM2tFd0N5dml1VmV4WUEyU1pfeEJ6SnZDZFBaeTBtX3ZVT3pFSU9MTUtz?oc=5) ⭐️ 6.0/10

一篇宪法学博客文章认为，算法治理的兴起创造了一个“全球宪制时刻”，在此背景下，人工智能原则应被直接写入国家宪法。

google\_news · www.iconnectblog.com · 10月21日 06:09

**标签**: `#AI governance`, `#constitutional law`, `#AI regulation`, `#algorithmic accountability`, `#public policy`

---

<a id="item-6"></a>
## [哈佛数学家就 AI 在科研与教学中的作用产生分歧](https://news.google.com/rss/articles/CBMiekFVX3lxTE9ZQzJEODcyZzRTdHl6d1ZxSFpSY01uNUdtMS04ODI4b19MZ0lSd0E4ZmJoeGFIWkhxODBmakJKUDF2dHNkYW02akJaWDcwTnl1aWhFOTZFOENvVTdKT0ZBdXhnTlR3LVJQWG0yT1lFeUhuVzM3WjIwRzFn?oc=5) ⭐️ 6.0/10

据《哈佛深红报》报道，哈佛大学的数学家在人工智能应如何应用于科研与教学这一问题上出现了明显分歧，而这一争论在 OpenAI 取得一项引人注目的突破后进一步升温。报道描述的是一种教师层面的意见分裂，而非已经确定的政策，且除标题所传达的框架外目前没有更多正文细节可供核实。 顶尖学府的数学家公开出现分歧，说明 AI 辅助证明与解题正从某种“新鲜事物”变成精英院系必须面对的方法论问题。哈佛这类机构如何确立使用 AI 工具进行引用、验证与教学的规范，很可能影响整个数学界的研究标准和学生培养方式。 报道的框架同时涉及科研与教学两方面的争议，说明这些张力既关乎证明的可验证性，也关乎学术诚信与课堂教学。由于目前仅有标题层面的摘要，文中提到的具体 OpenAI 成果以及哈佛个别教师的立场在此无法详细说明。

google\_news · The Harvard Crimson · 10月21日 19:17

**背景**: 大语言模型在数学推理方面的能力显著提升，于是不断有人宣称 AI 系统能够解决竞赛级乃至研究级的数学问题。数学作为 AI 的试验场具有特殊性：其正确性可以被形式化检验，因此关于 AI 能力的宣称原则上能通过证明本身来验证，而不是凭主观印象。这使得数学系成为围绕署名权、验证负担以及学生应被要求独立完成哪些工作等问题的最早争论阵地。

**标签**: `#AI in research`, `#mathematics`, `#academia`, `#OpenAI`, `#AI in education`

---

<a id="item-7"></a>
## [辛顿：AI 有 1%概率毁灭人类，但我不是末日论者](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNTkxXMlBfdUxNLWFHemh6SWlmTmlOeDZLSGMwWDg0SzNCNUJHbXRWb09DMi1COEFpcE5uZWVvY1lHV29CV1dxSkJXSE9FVmFab3l3NTRHSTZPbzkxbDlsMXBmWWxNY3FaSUxuWVF5bHRRalN1STEyLWdxR3lVVTlqVU1heTVOZ2VpZ0tPMnhYbllMQU0wZktQSVVEeVJsOUI3ZklVY1VpSTVhZzdEbGdyOTlJQUE1cmJZUmZyc2ZUUzFBWVU1ajhUa3l1bDZJX0FIRy04ejNySmJEdm9nZzJCaEtBUUIwYXfSAfsBQVVfeXFMT2NHWklaV0c5R09la3JJdkNUV1ZlY1F3TW0ySE9IVUxqYXB6SmVYTkwzYVRsT0l1ZFo0NkpYSmdGSUprYXI4dEREUDBoV1pHQXZNSmtyT0h4cDlEN0l3THNxQmU3MmpEMUVDbUItTTVzcXhKX0dUak9EeXdEcF85MWNrSWxhcXdCbHZ2MzVTVGMzVXJMRVpjaG55N0xZNlZjS1dEUVJpUmFXTjFnaGd6ODAzc0tqa205NTBaNDRKaE5Ud3dEN2JjalNvRjJJNTNmZGdfeWZCQ0RfZk0tNGVWcGVCeTkyYWVIakNnT0VwWGRmNmJ4cjI2S2VFY2s?oc=5) ⭐️ 6.0/10

杰弗里·辛顿表示，他并非“末日论者”，并估计 AI 有 1%的概率毁灭人类。 一位人工智能先驱给出具体的生存风险估计，可能影响公众、研究人员和政策制定者讨论 AI 安全以及权衡监管与创新的方式。 这一数字值得注意，因为它来自一位顶尖 AI 人物，是一个非零的生存风险估计，但他明确与宿命论保持距离；不过，目前提供的条目只有标题和链接，因此无法得知 1%这一数字背后的推理依据。

google\_news · EL PAÍS English · 10月21日 19:07

**背景**: 杰弗里·辛顿是一位人工智能先驱，因其在神经网络和深度学习方面的基础性工作而常被称为“AI 教父”。在 AI 讨论中，“末日论者”通常指认为先进 AI 会导致人类灭绝或不可逆灾难的人。辛顿的言论进一步加入了关于先进 AI 是否构成生存风险以及社会应如何严肃对待这些风险的广泛争论。

**标签**: `#AI safety`, `#existential risk`, `#Geoffrey Hinton`, `#AI policy`, `#technology commentary`

---

<a id="item-8"></a>
## [前政府官员敦促哥伦比亚特区巡回上诉法院重审 Anthropic 与五角大楼案裁定](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPazV1Y2dCb0s2SlJQSnh2TUdlcE1NQ01hSXVqWTVuSVNxc2lSY1c0eW1fSmZpYXM0MjNZWEFFZUUtYW4tSUNSLU8xOGxNbUNwcnVZOXl5bWc1VjlHeFFOX05aLVdZQTBwSGR6MjZSdU4zUVEzWU45YmhKQ3FOclNNRGt1VUpCc2s0?oc=5) ⭐️ 6.0/10

据 DefenseScoop 报道，一批美国前政府官员正请求哥伦比亚特区巡回上诉法院重新审议其在 AI 公司 Anthropic 与五角大楼之间法律纠纷中作出的裁定。此举表明，这起处于 AI 治理与国家安全政策交汇点的案件在上诉阶段仍处于激烈争夺之中。 该案的裁决结果可能界定 AI 开发者在多大程度上能对其模型被军方使用的方式拥有话语权，以及政府是否可以强制将商业 AI 系统用于国防用途。由于哥伦比亚特区巡回上诉法院经常审理国家安全与监管类案件，其判决理由可能成为未来 AI 实验室与联邦机构之间纠纷的参考依据。 现有报道只披露了这份请求的主旨，并未给出这些前官员的姓名、他们援引的具体程序机制，也未提供被质疑的哥伦比亚特区巡回上诉法院裁定原文，因此确切的法律争点仍不清晰。提出请求的是前政府官员而非诉讼当事方，这说明此案承载的政策意义已超出 Anthropic 自身的商业利益。

google\_news · DefenseScoop · 10月21日 22:19

**背景**: 哥伦比亚特区巡回上诉法院是设在华盛顿特区的联邦上诉法院，经常审理涉及联邦机构、国家安全与监管权限的案件。Anthropic 是 Claude 系列 AI 模型的开发商，其已公布的使用政策对全自主武器和大规模监控等应用作出限制，同时也推出了面向政府的相关产品；而五角大楼则在快速扩大对商业 AI 的采用。此案属于一场更广泛争论的一部分：当商业 AI 模型被用于国防目的时，由谁来划定边界。

**标签**: `#AI policy`, `#national security`, `#legal`, `#Anthropic`, `#Pentagon`

---

<a id="item-9"></a>
## [《纽约时报》：中国免费 AI 模型前景陷入不确定](https://news.google.com/rss/articles/CBMiggFBVV95cUxNVGtOTkNCaEJUNWpyTEJIU3dDbzJNcGxxLUNlemU0a2ZxUmdObVQ0WUVkbXpnS0ZEVW5PZVZ0T2UxMnpKczlFM2ZYRHZJMWFqOU9PMnBYQ3V2bVVPRUdKcFppeHhDejJ2VTQzLWU4d0paSV8wRUFtMm9XS1FjTnNLUUxR?oc=5) ⭐️ 6.0/10

《纽约时报》刊发报道称，中国免费 AI 模型——即那些可公开下载、低成本使用并推动了中国近期开放权重模型热潮的系统——正被抛入不确定的境地。现有摘要未说明具体触发因素，但指向监管与市场双重压力，这可能改变这些模型的发布与分发方式。 中国的开放权重模型已占据全球开源 AI 生态的相当大份额，因此其发布自由度一旦生变，将影响全球范围内基于这些模型进行开发的开发者、初创公司和企业。这同时也会重塑中国实验室与 Mistral、Reflection 等西方开放权重阵营之间的竞争格局。 目前提供的内容仅有标题和一句摘要，没有正文，因此具体的监管措施、受影响的公司或模型系列均无法确认。这种不确定性似乎集中在免费发布模型的许可与可获得性上，而非其技术能力本身。

google\_news · The New York Times · 10月21日 14:43

**背景**: 开放权重模型是指将训练好的参数公开、任何人都可以下载、在本地运行并微调的 AI 系统，这与只能通过 API 访问的闭源模型形成对比。DeepSeek、阿里巴巴的 Qwen 等中国实验室已在宽松许可下发布了大量此类模型，因而在全球开发者中广受欢迎。中国自 2023 年起推出并持续演进的生成式 AI 管理规定主要针对面向公众提供的服务，对于如何适用于可下载的模型权重仍留有疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/science.ady7922">China’s emerging regulation toward an open future for AI</a></li>
<li><a href="https://www.justsecurity.org/111053/chinas-open-source-ai-regulation/">Open Questions for China’s Open-Source AI Regulation</a></li>
<li><a href="https://www.axios.com/2026/10/06/reflection-mistral-open-weight-ai-models-china">Western AI labs challenge China &#x27;s open - model lead</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#China`, `#open-source AI`, `#regulation`, `#industry news`

---

<a id="item-10"></a>
## [同一 AI 查询在得州比在瑞典排放更多二氧化碳](https://news.google.com/rss/articles/CBMirwFBVV95cUxNRnhmbVhqUk1GWTJxS3k0YWxGM1ZBNUYwSmxZOXY2eXJLdm9zUndVS2xvN2NqeHFSdmhaS3R6N24tdzlGSXdxR25kVEItY3V1YXFWTTBlRERBUWFjWFFWbHE2RDVkcDdHV3FiSzE2X3RQajBSWlZZYkJSc2ViaGJCdXhSQ21xcFNxb0c1NHRQSDNnQ1hFZTFhdWxXcXd1cy1IUVpzVktJUUhNdkxpYnR3?oc=5) ⭐️ 6.0/10

CIO 发表文章指出，同一个 AI 问题在不同地区可能产生不同的二氧化碳排放，并以得克萨斯州和瑞典作为对比案例。由于提供的摘要未包含文章正文，具体使用的模型、查询内容或实测排放数据尚不清楚。 这表明 AI 的运行碳排放具有明显的地域依赖性，因此数据中心选址和云区域选择可能会显著影响相同工作负载的排放。它也推动可持续性讨论从笼统的“AI 能耗”转向考虑电网差异的核算方式。 AI 推理的运行排放取决于每次查询消耗的电量乘以当地电网的碳强度，而 PUE 等数据中心基础设施开销会进一步增加影响。得州与瑞典的实际差距还会因模型、硬件、利用率、一天中的时段以及是否计入可再生能源证书或其他抵消机制而不同。

google\_news · CIO · 10月21日 20:44

**背景**: LLM 推理在模型回答每次查询时都会消耗电力，这种用电量可以用每次查询的瓦时数来估算。电网碳强度衡量每千瓦时电力排放多少克二氧化碳，并因各地区煤炭、天然气、核能、水电、风电和太阳能等发电结构不同而有很大差异。电源使用效率（PUE）描述数据中心在 IT 设备之外为冷却和其他开销额外消耗多少能源。每次查询能耗、PUE 和电网碳强度共同决定了 AI 请求的运行碳足迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2505.09598">How Hungry is AI? Benchmarking Energy , Water, and Carbon ...</a></li>
<li><a href="https://greencalculus.com/factors/grid-electricity-carbon-intensity-factors/">Grid Electricity Carbon-Intensity Factors by Country</a></li>
<li><a href="https://clearcomfort.com/pue-wue-ai-data-centers/">Good PUE &amp; WUE for AI Data Centers : 2026 Benchmarks</a></li>

</ul>
</details>

**标签**: `#AI sustainability`, `#carbon emissions`, `#energy grids`, `#LLM inference`, `#data centers`

---