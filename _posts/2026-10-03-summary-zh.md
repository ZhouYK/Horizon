---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03 23:03:06 +0000
lang: zh
report: default
---

> 从 138 条内容中筛选出 5 条重要资讯。

---

1. [Qt 6.12 LTS 发布，首次将 HarmonyOS 纳入官方 LTS 支持平台](#item-1) ⭐️ 7.0/10
2. [Google 更新指南，禁止伪造作者署名](#item-2) ⭐️ 7.0/10
3. [谷歌收紧 Gemini 权限：10 月 9 日起免费用户仅能用 Flash-Lite](#item-3) ⭐️ 6.0/10
4. [Google Antigravity 上线 Opus 5.5 与 Sonnet 5.5，第三方模型将转为付费专属](#item-4) ⭐️ 6.0/10
5. [美股 12 月 6 日起进入 23 小时交易时代](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qt 6.12 LTS 发布，首次将 HarmonyOS 纳入官方 LTS 支持平台](https://www.qt.io/blog/qt-6.12-released) ⭐️ 7.0/10

Qt 6.12 LTS 于 2026 年 9 月 30 日正式发布，提供长达 5 年的维护支持周期。这也是华为 HarmonyOS 首次被纳入 Qt 的 LTS 官方支持平台列表。 Qt 是最广泛使用的 C++ 跨平台框架之一，把 HarmonyOS 提升到 LTS 支持层级，意味着开发者可以用同一套代码库直接覆盖华为生态，而无需自行做移植适配。这既反映了华为构建独立软件栈的推进力度，也说明 Qt 愿意跟随企业客户进入该市场。 关键在于“LTS”这一层级：企业通常只把长期维护的版本作为标准化目标，维护周期以年而非月计，因此 HarmonyOS 支持现在被纳入了这份长期承诺，而不再只是昙花一现的实验性后端。另外需要注意，Qt 的长期支持通常分为最初的公开维护阶段和与商业授权绑定的延长支持阶段。

telegram · zaihuapd · 10月3日 04:52

**背景**: Qt 是一个用于构建图形界面和多平台应用的 C++ 框架，遵循“一次编写、随处编译”的理念，让同一份代码可以运行在桌面、移动和嵌入式平台上。Qt 会定期指定某一个版本为 LTS（长期支持）版本，企业偏爱这类版本，因为它们能在数年内持续获得修复，而不会被迅速淘汰。HarmonyOS 是华为面向手机、平板、PC 和可穿戴设备推出的分布式操作系统，其较新的 HarmonyOS NEXT 一代是自研的专有系统而非基于 Android 衍生，这正是 Qt 这类框架需要专门做适配才能支持它的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qt_%28software%29">Qt (software) - Wikipedia</a></li>
<li><a href="https://www.qt.io/development/qt-framework">Qt Framework – Build Fast, Scalable Cross-Platform Software | Qt</a></li>

</ul>
</details>

**标签**: `#Qt`, `#HarmonyOS`, `#C++`, `#Cross-Platform`, `#Release`

---

<a id="item-2"></a>
## [Google 更新指南，禁止伪造作者署名](https://futurism.com/artificial-intelligence/google-updates-guidelines-fake-bylines-ai-generated-headshots) ⭐️ 7.0/10

Google 更新了搜索指南，明确禁止伪造作者署名和 AI 生成的头像，此前有报道揭露 AI 内容农场伪造专家身份。

telegram · zaihuapd · 10月3日 16:31

**标签**: `#Google Search`, `#SEO`, `#AI Content`, `#Misinformation`, `#Content Farms`

---

<a id="item-3"></a>
## [谷歌收紧 Gemini 权限：10 月 9 日起免费用户仅能用 Flash-Lite](https://support.google.com/gemini/answer/17004136) ⭐️ 6.0/10

谷歌开始调整个人用户的 Gemini 模型访问权限：从 10 月 9 日起，未订阅 Google AI 服务的用户将只能使用 Gemini Flash-Lite 模型，Flash 与 Pro 不再向免费用户开放。付费用户则保留更高阶模型，其中 AI Plus 可使用 Flash-Lite 和 Flash，AI Pro 与 AI Ultra 还可额外使用 Pro。 这一调整把 Gemini 免费层从“多模型可选”压缩为“仅一个轻量模型”，使 Flash 和 Pro 成为付费专属能力，并会推动重度用户转向 AI Plus、Pro 或 Ultra 订阅。它表明谷歌正从追求免费用户规模转向对 Gemini 变现，同时也会抬高其他 AI 助手在免费额度上的竞争门槛。 使用额度将根据所用模型、提示词复杂度以及调用的功能等因素综合计算，每 5 小时刷新一次，并另设有每周上限。图像生成、视频生成和 Deep Research 等高算力功能会比普通文本对话消耗更多额度。

telegram · zaihuapd · 10月3日 06:09

**背景**: Gemini 是谷歌的大语言模型家族，按能力分层：主打速度与低成本的轻量级 Flash-Lite、中端的 Flash，以及能力更强的 Pro。谷歌面向普通用户提供免费层和 Google AI Plus、Pro、Ultra 等付费方案，付费方案此前可解锁更高阶模型和更大使用额度。Deep Research 这类功能属于自主智能体工具，能够自行规划、联网检索并综合出多步研究报告，因此其算力消耗远高于普通对话。

**标签**: `#Google Gemini`, `#AI pricing`, `#LLM access`, `#product policy`, `#AI subscriptions`

---

<a id="item-4"></a>
## [Google Antigravity 上线 Opus 5.5 与 Sonnet 5.5，第三方模型将转为付费专属](https://www.reddit.com/r/google_antigravity/comments/1wwfcav/google_finally_added_opus_55_and_sonnet_55_on) ⭐️ 6.0/10

Google Antigravity 在其智能体优先的开发平台上新增了 Anthropic 的 Claude Opus 5.5 和 Claude Sonnet 5.5 模型，并宣布自 11 月 2 日起，所有第三方模型将仅限于付费的 Pro 和 Ultra 套餐用户使用。 这一调整实际上剥夺了免费用户使用非 Google 前沿模型的权利，把「模型选择权」变成了付费功能，也表明 Antigravity 正从以拉新为主的阶段转向商业化，依赖免费套餐的业余开发者和个人开发者将直接受到影响。 据 Anthropic 介绍，Claude Sonnet 5.5 比 Sonnet 5 快 30% 以上，且大多数任务成本最多降低 30%；Claude Opus 5.5 则被定位为长时运行的智能体编码与知识工作的推荐默认模型，价格比 Opus 5 低约 20%。11 月 2 日的截止日期仅针对第三方模型，这意味着 Google 自家的 Gemini 模型在免费套餐中仍可继续使用。

telegram · zaihuapd · 10月3日 06:32

**背景**: Google Antigravity 是 Google 推出的「智能体优先」AI 开发环境，把 AI 辅助代码编辑器与一个管理界面结合起来，让自主智能体能够异步执行复杂的编程任务。此类平台通常允许开发者自选驱动智能体的底层大模型，因此用户可以混用第一方模型（Google 的 Gemini）与第三方模型（Anthropic 的 Claude）。Anthropic 的 Claude Opus 和 Sonnet 系列被广泛用于编码智能体，其中 Sonnet 主打成本与速度，Opus 则主打在更困难、更耗时的任务上的最强能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>
<li><a href="https://www.datacamp.com/blog/gpt-6-1-sol-vs-opus-5-5">GPT-6.1 Sol vs. Claude Opus 5 . 5 : Which Model to Use | DataCamp</a></li>
<li><a href="https://www.searchyour.ai/en/google-antigravity-ai">Google Antigravity AI - Google ’s agentic development platform</a></li>

</ul>
</details>

**标签**: `#Google Antigravity`, `#Anthropic Claude`, `#AI models`, `#pricing`, `#platform update`

---

<a id="item-5"></a>
## [美股 12 月 6 日起进入 23 小时交易时代](https://wallstreetcn.com/articles/3782956) ⭐️ 6.0/10

自 12 月 6 日起，纳斯达克、纽交所 Arca 等四大核心交易所将新增夜盘交易时段，使美股每日交易时间延长至 23 小时，仅在美东时间 20 时至 21 时休市进行系统维护。该安排仍需获得 SEC 批准，是美国交易所为覆盖非美交易时段而推进的整体举措之一。 这是近年来美国股票市场基础设施最重要的结构性变化之一，使亚洲和欧洲投资者可以在本地白天时段交易美股，并可能重塑盈透证券、Robinhood 等已提供隔夜交易渠道的券商的收入结构。同时，它也引发了市场对流动性、价格发现以及行情与清算基础设施能否支撑近乎全天候交易的疑问。 SEC 数据显示，当前夜盘成交量约占美股总成交量的 1%，但同比增幅约为 358%。据报道，机构投资者担忧夜间时段流动性不足以及买卖价差扩大，而海外资金和散户仍是该时段的主要参与者。

telegram · zaihuapd · 10月3日 07:29

**背景**: 纽交所 Arca 是纽约证券交易所集团（隶属洲际交易所集团）旗下的全电子化美国证券交易所，在交易所交易产品（ETP）的上市与交易方面居美国市场领先地位。历史上美股仅在约 6.5 小时的常规时段加上盘前、盘后延长时间内交易，亚洲白天大部分时间处于休市状态。买卖价差即最优买价与卖价之间的差额，是衡量市场流动性和交易成本的标准指标，因此夜盘价差走阔意味着此时交易成本更高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/stocks/articles/night-nasdaq-23-hour-trading-131500796.html?fr=sycsrp_catchall">Up All Night: How Nasdaq’s 23-Hour Trading Could Wake Up Wall ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/NYSE_Arca">NYSE Arca</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bid-ask_spread">Bid-ask spread</a></li>

</ul>
</details>

**标签**: `#US stock market`, `#23-hour trading`, `#Nasdaq`, `#NYSE`, `#market infrastructure`

---