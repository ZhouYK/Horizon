---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
report: default
---

> 从 237 条内容中筛选出 7 条重要资讯。

---

1. [多家科技巨头签署开放权重 AI 领导力公开信](#item-1) ⭐️ 8.0/10
2. [AMD 确认 Zen 7 EPYC 于 2028 年推出，Zen 8 将在 2030 年登场](#item-2) ⭐️ 7.0/10
3. [微软将用 TPM 芯片封堵盗版 Windows 激活](#item-3) ⭐️ 7.0/10
4. [DeepSeek 因内部言论泄露暂停新一轮融资](#item-4) ⭐️ 7.0/10
5. [上海交大医学院成立工作组调查科研不端](#item-5) ⭐️ 7.0/10
6. [长鑫科技登陆上交所，创 A 股最大规模 IPO](#item-6) ⭐️ 7.0/10
7. [下一代 iPad mini 传闻将成为苹果首款防水 iPad](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [多家科技巨头签署开放权重 AI 领导力公开信](https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/) ⭐️ 8.0/10

谷歌、AMD、Cloudflare 等多家科技巨头正式签署了一封公开信，倡导开放权重 AI 模型和美国的 AI 领导力。 这一广泛的行业背书表明了对开放权重 AI 的统一支持，可能影响美国 AI 政策，并塑造全球 AI 模型的开发与共享方式。 该公开信此前已有 OpenAI、Meta、Microsoft、Nvidia 和 IBM 签署，如今谷歌、AMD 和 Cloudflare 也加入。签署方涵盖了软件、硬件和基础设施领域的 AI 领导者。

telegram · zaihuapd · 7月26日 02:00

**背景**: 开放权重模型是指其参数（即“权重”）对外公开，允许任何人下载和使用的 AI 模型。与开源 AI 不同，开放权重模型可能不包含训练代码或数据。这已成为 AI 治理中的一个关键辩论，涉及开放性与安全性及控制之间的平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-weight`, `#policy`, `#industry`

---

<a id="item-2"></a>
## [AMD 确认 Zen 7 EPYC 于 2028 年推出，Zen 8 将在 2030 年登场](https://www.techspot.com/news/113233-amd-confirms-zen-7-epyc-florence-2028-previews.html) ⭐️ 7.0/10

AMD 正式确认，其下一代 Zen 7 架构将用于代号为 &\#x27;Florence&\#x27; 的第七代 EPYC 服务器处理器，计划于 2028 年推出；基于 Zen 8 的第八代 EPYC &\#x27;Ravenna&\#x27; 则计划于 2030 年登场。 这一长期路线图为数据中心规划提供了关键的可预见性，并表明 AMD 通过持续架构创新，致力于与英特尔及其他 AI 加速服务器解决方案竞争。 Florence 处理器将包含常规 Zen 7 核心和高密度 Zen 7c 核心，支持下一代 MRDIMM 和 LPDDR 内存，并在 SP7 和 SP8 平台上配备 AI 计算扩展，用于 &\#x27;Ferrara&\#x27; AI 机架系统。

telegram · zaihuapd · 7月25日 14:05

**背景**: AMD 的 Zen 架构驱动其 EPYC 服务器处理器，与英特尔 Xeon 竞争，并越来越多地用于 AI 和高性能计算。MRDIMM（Multiplexed Rank DIMM，多列直插内存模组）是一种高带宽内存技术，通过组合多个 DDR5 列来提升性能；SP7 和 SP8 是 AMD 的服务器插槽平台，分别支持不同代的 EPYC CPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lenovopress.lenovo.com/lp2028-introduction-to-mrdimm-memory-technology">Introduction to MRDIMM Memory Technology &gt; Lenovo Press</a></li>
<li><a href="https://www.amd.com/en/products/processors/server/epyc/9006-series.html">AMD EPYC™ 9006 Server CPUs for AI-First Data Centers</a></li>

</ul>
</details>

**标签**: `#AMD`, `#CPU`, `#Zen`, `#server`, `#roadmap`

---

<a id="item-3"></a>
## [微软将用 TPM 芯片封堵盗版 Windows 激活](https://www.techspot.com/news/113232-microsoft-using-tpm-chips-crack-down-pirated-windows.html) ⭐️ 7.0/10

微软宣布将为其企业批量激活工具 KMS 加入基于 TPM 芯片的硬件安全验证。新的“TPM 证明”机制会先确认 KMS 服务器的硬件身份，之后才允许处理激活请求，针对盗版者使用的伪造 KMS 服务器。 此举可能使许多依赖 KMS 的激活破解工具失效，对企业和盗版社区都产生重大影响。但攻防对抗仍在继续，如 Massgrave 组织已推出 TSforge 等新绕过方法。 该功能将在下一版 Windows Server 中成为强制要求，并自 2026 年 8 月起在 Windows Server 2025 中推送准备提示。微软已在 2025 年封死了 KMS38 漏洞，新的 TPM 证明专门针对需要每半年续期的在线 KMS 模拟器。

telegram · zaihuapd · 7月25日 15:55

**背景**: KMS（密钥管理服务）是微软用于企业内部批量激活 Windows 和 Office 的技术，通常使用本地 KMS 服务器。盗版者长期通过设置伪造 KMS 服务器来激活未授权副本。TPM（可信平台模块）是一种硬件安全芯片，可验证系统完整性。新的 TPM 证明机制确保只有经微软认证的 KMS 服务器才能发放激活令牌，从而增加伪造难度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notebookcheck.net/Microsoft-Windows-and-Office-activation-cracked-again-TSforge-introduces-a-new-more-permanent-DRM-bypass.963349.0.html">Microsoft Windows and Office activation cracked again: TSforge ...</a></li>
<li><a href="https://github.com/massgravel/Microsoft-Activation-Scripts">GitHub - massgravel/Microsoft- Activation -Scripts: Open-source...</a></li>
<li><a href="https://learn.microsoft.com/ru-ru/windows-server/get-started/kms-client-activation-keys">Активация клиента службы управления ключами ( KMS ) и ключи...</a></li>

</ul>
</details>

**标签**: `#Windows`, `#TPM`, `#DRM`, `#KMS`, `#反盗版`

---

<a id="item-4"></a>
## [DeepSeek 因内部言论泄露暂停新一轮融资](https://www.bloomberg.com/news/articles/2026-07-25/deepseek-said-to-tell-backers-of-funding-pause-after-viral-posts) ⭐️ 7.0/10

DeepSeek 已通知部分投资者暂停第二轮融资，本轮原计划募资至少 1000 亿元人民币，投前估值不低于 4800 亿元人民币，原因是创始人梁文锋对内部讨论被泄露表示不满。 此次融资暂停凸显了数据安全对高额 AI 投资的影响，可能延迟 DeepSeek 的扩张计划，同时该公司正筹备最快于 2026 年内递交 IPO 申请。 首轮融资于 2026 年 6 月完成，筹得 70 亿美元，投资方包括腾讯、宁德时代及国家人工智能产业投资基金。暂停部分源于创始人梁文锋对会议内容被泄露的不满，促使团队重新评估信息披露流程和投资者沟通机制。

telegram · zaihuapd · 7月26日 01:17

**背景**: DeepSeek 由梁文锋于 2023 年 7 月创立，是一家以高性价比、开放权重大型语言模型（如 DeepSeek-R1）闻名的中国 AI 公司。它最初由对冲基金 High-Flyer 孵化，因在受美出口限制的情况下使用约束硬件进行高效训练而受到全球关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://internetquadrant.com/industry-news/deepseek-7b-funding-ai-model">DeepSeek完成70亿美元首轮巨额融 资 _腾讯宁德时代重 金 入局_AI...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI funding`, `#data security`, `#Chinese AI`, `#business news`

---

<a id="item-5"></a>
## [上海交大医学院成立工作组调查科研不端](https://www.shsmu.edu.cn/news/info/1023/30895.htm) ⭐️ 7.0/10

2026 年 7 月 26 日，上海交通大学医学院宣布成立专项工作组，调查针对医学研究论文和一项临床研究的不端行为指控。 此次调查彰显了该机构对科研诚信的重视，可能为中国医学研究中处理不端指控树立先例。 调查对象是研究人员仇某某的论文和新华医院的一项临床研究，调查结果将严肃处理。

telegram · zaihuapd · 7月26日 06:01

**背景**: 科研不端行为包括研究中的捏造、篡改或剽窃。在全球对科研伦理日益关注的背景下，中国高校近期加强了诚信监督。

**标签**: `#research integrity`, `#investigation`, `#medical research`, `#Shanghai Jiao Tong University`

---

<a id="item-6"></a>
## [长鑫科技登陆上交所，创 A 股最大规模 IPO](https://www.bloomberg.com/news/articles/2026-07-26/memory-frenzy-primes-china-champion-cxmt-for-historic-debut?srnd=phx-technology) ⭐️ 7.0/10

长鑫科技（CXMT）将于 2026 年 7 月 27 日在上海证券交易所上市，此前通过 IPO 募资 666 亿元人民币（98 亿美元），为 2010 年以来 A 股最大规模 IPO。散户认购部分超额认购 212 倍，940 万个订单共冻结约 7.07 万亿元资金。 长鑫科技上市有望成为 A 股市值最高的公司，突显中国推动半导体自主可控的战略决心。巨大的市场热情反映出在全球供应链调整背景下，投资者对国产存储芯片企业的信心增强。 发行价每股 8.66 元，初始市值约 5800 亿元。分析师预计，若首周股价上涨约 330%，长鑫科技将超越工商银行成为 A 股市值最高公司；华西证券更给出 5 万亿元市值预期。

telegram · zaihuapd · 7月26日 07:31

**背景**: 长鑫科技是我国规模最大、技术最先进的 DRAM IDM（设计制造一体化）企业，即自行设计、制造和销售 DRAM 芯片。DRAM（动态随机存取存储器）是一种用于计算机和服务器的易失性存储器。A 股市场是指在中国大陆交易所（上海和深圳）上市、以人民币计价的股票市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Random-access_memory">Random - access memory - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchstorage/definition/DRAM">What is DRAM ( Dynamic Random Access Memory )? How Does it...</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#semiconductor`, `#IPO`, `#China`, `#memory`

---

<a id="item-7"></a>
## [下一代 iPad mini 传闻将成为苹果首款防水 iPad](https://www.macrumors.com/2026/07/25/first-water-resistant-ipad/) ⭐️ 6.0/10

据传闻，下一代 iPad mini 将成为苹果首款防水 iPad，采用振动发声系统以取消传统扬声器开孔，配备 8.4 英寸 OLED 屏幕，芯片升级至 A19 Pro 或 A20 Pro，预计在 2026 年 10 月前发布。 防水功能将是 iPad 产品线的重要新增特性，扩展了在浴室、泳池边等潮湿环境的使用场景，而振动发声技术可能使未来设备更薄、密封性更好。 具体的 IP 等级尚未公布，但传闻称其防护能力与 iPhone 相当。据报道，三星显示已在量产该 OLED 面板，价格可能比现款 599 美元的起售价贵约 100 美元。

telegram · zaihuapd · 7月26日 06:46

**背景**: 振动发声技术，也称为骨传导或表面振动，利用设备机身直接振动产生声音，取代了传统扬声器振膜。这样就可以取消扬声器开孔——这些开孔通常是水和灰尘进入设备的主要途径。苹果早在 2014 年就申请了相关专利，表明在该领域进行了长期研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fix-myspeaker.com/">Fix My Speaker - Best Speaker Cleaner App | Eject Water &amp; Dust</a></li>
<li><a href="https://www.youtube.com/watch?v=A4NCodkoGk4">Secretly Turning People&#x27;s Windows Into Giant Speakers ... - YouTube</a></li>

</ul>
</details>

**标签**: `#iPad`, `#Apple`, `#rumor`, `#water resistance`, `#OLED`

---