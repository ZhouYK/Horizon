---
layout: default
title: "Horizon Summary: 2026-11-04 (ZH)"
date: 2026-11-04 23:04:30 +0000
lang: zh
report: default
---

> 从 188 条内容中筛选出 11 条重要资讯。

---

1. [NIKKE PC 启动器被指遭供应链投毒植入远控木马](#item-1) ⭐️ 9.0/10
2. [月之暗面开源 Kimi K3.1 Pro 权重，上下文约 100 万 token](#item-2) ⭐️ 9.0/10
3. [Anthropic 开源 FlashProve，用于验证 AI 模型身份](#item-3) ⭐️ 8.0/10
4. [甲骨文在美国施压下取消与腾讯 70 亿美元 AI 芯片租赁协议](#item-4) ⭐️ 8.0/10
5. [腾讯混元 Hy4 发布，首次引入视觉能力](#item-5) ⭐️ 7.0/10
6. [黑客团队 Calif 演示绕过锁定模式且越狱在 iOS 27.2 更新后仍存活](#item-6) ⭐️ 7.0/10
7. [华为要求昇腾 960DT 客户自行解决 HBM 内存采购](#item-7) ⭐️ 7.0/10
8. [Google 对 K-12 学校账号默认关闭 Gemini 与搜索](#item-8) ⭐️ 6.0/10
9. [华为、阿里等 20 家单位联合发布《智能体发展自律公约》](#item-9) ⭐️ 6.0/10
10. [印度成 ChatGPT 全球最大市场，用户数自 1 月以来翻倍](#item-10) ⭐️ 6.0/10
11. [Cloudflare 推出个人 AI 代理流量分析与分级管控](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [NIKKE PC 启动器被指遭供应链投毒植入远控木马](https://github.com/WormW/nikke_malware_analysis) ⭐️ 9.0/10

独立研究者与玩家分析称，《胜利女神：NIKKE》PC 启动器加载的官方 CDN 文件被植入加载器，进而下载并运行远控木马；该木马据称包含 19 条命令，可执行任意命令、截屏，并窃取开发者与 AI 工具凭据及 28 个浏览器钱包扩展数据。Level Infinite 已于 11 月 3 日替换两个被篡改文件，但尚未公开说明。 游戏启动器是玩家信任的官方分发通道，一旦遭供应链投毒，影响范围可覆盖大量 PC 玩家，并可能波及开发者凭据和加密资产安全。此类事件也凸显厂商在发现篡改后应及时公开披露，并提供可验证的修复指引。 研究者给出的自查方式是在 debug.log 中搜索 k2f\_chan，并建议在厂商说明前暂不启动 PC 版；目前结论来自独立逆向分析，厂商尚未公开确认，相关指标应视为可操作但有待进一步核实的线索。

telegram · zaihuapd · 11月4日 07:00

**背景**: 游戏启动器通常会从内容分发网络（CDN）下载更新或运行所需文件，因此一旦这些上游文件被篡改，恶意代码就可能借“官方更新”路径进入玩家电脑。这类攻击属于供应链投毒：攻击者不逐一钓鱼受害者，而是篡改软件或其分发基础设施。远控木马（RAT）能让攻击者交互式控制受害主机，执行命令并窃取数据；浏览器钱包扩展则常因可能暴露助记词或私钥而成为重点目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/weixin_29322855/article/details/165536215">远程访问木马（RAT）攻击原理与安全防护实践指南-CSDN博客</a></li>
<li><a href="https://baike.baidu.com/item/%E8%BF%9C%E7%A8%8B%E8%AE%BF%E9%97%AE%E6%9C%A8%E9%A9%AC/17610868">远程访问木马 - 百度百科</a></li>
<li><a href="https://developer.aliyun.com/article/1734511">developer.aliyun.com/article/1734511</a></li>

</ul>
</details>

**标签**: `#supply-chain-attack`, `#malware-analysis`, `#security-incident`, `#credential-theft`, `#game-security`

---

<a id="item-2"></a>
## [月之暗面开源 Kimi K3.1 Pro 权重，上下文约 100 万 token](http://platform.kimi.ai/) ⭐️ 9.0/10

据报道，月之暗面在 Hugging Face 上发布了 Kimi K3.1 Pro 的开放权重，这是一个原生多模态的智能体模型，总参数 2.8T、激活参数 104B，上下文窗口约 100 万 token，也是 K3.1 系列的首个模型。与权重同步，官方在 platform.kimi.ai 开放了 API，模型名为 kimi-k3.1-pro，兼容 OpenAI 与 Anthropic 两套接口，权重以 MXFP4 量化形式发布。 把万亿级参数、百万 token 上下文、原生多模态与智能体能力的“前沿级”权重公开，是一个不小的转变，因为这一量级的模型此前基本只以闭源 API 形式提供。它为需要长上下文智能体与编码任务的团队提供了可自托管的替代方案，也会给其他实验室带来压力，需要为其保留闭源的决定给出理由。 该模型采用混合专家（MoE）架构，因此 2.8T 是总容量，而每个 token 实际只激活约 104B 参数，推理成本远低于标题数字给人的印象。MXFP4 是一种 4 位微缩放量化格式，能大幅压缩权重文件，但会带来精度上的取舍；此外不同来源报道的参数规模存在差异（有说法称约 3T），具体规格最好以 Hugging Face 模型卡为准。

telegram · zaihuapd · 11月4日 15:47

**背景**: 月之暗面是 Kimi 助手背后的中国实验室，其 Kimi K 系列模型以超长上下文著称。混合专家（MoE）模型把参数拆分成许多专门的“专家”子网络，每个 token 只被路由到其中少数几个，因此总参数（全部专家都要载入显存）远大于激活参数（单 token 实际使用的部分），这一区别对硬件规划影响很大。“开放权重”指训练好的参数可以下载并自行部署，但并不等同于开源，因为训练数据与代码未必公开。MXFP4（微缩放 4 位浮点）是一种 4 位浮点格式，一组数值共享一个缩放指数，近期因 gpt-oss 等大型开放权重模型的发布而受到关注。兼容 OpenAI/Anthropic 接口意味着为这些厂商编写的现有客户端代码只需很少改动就能指向月之暗面的端点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yottalabs.ai/post/kimi-k3-1-pro-specs-price-open-weights-benchmarks">Kimi K 3 . 1 Pro : Specs, Price, Open Weights Date, and... | Yotta Labs</a></li>
<li><a href="https://osfoundry.io/articles/mixture-of-experts-explained">Mixture of Experts Explained: Total vs Active Parameters ...</a></li>
<li><a href="https://www.kapilsharma.dev/posts/mxfp4-visualizer/">Understanding MXFP4 Quantization | Kapil Sharma</a></li>

</ul>
</details>

**标签**: `#Moonshot AI`, `#Kimi`, `#open weights`, `#large language models`, `#multimodal AI`

---

<a id="item-3"></a>
## [Anthropic 开源 FlashProve，用于验证 AI 模型身份](https://assets.claude.com/8e1d181a83015078581c92d896757041713f0160.pdf) ⭐️ 8.0/10

Anthropic 正在开发并开源 FlashProve，这是一套通过加密证明来验证某段 AI 输出是否确实由指定模型生成的系统。该实验室已发布技术规范和代码，该系统可帮助用户识别模型被替换的情况，也能核实第三方关于某个模型执行了某项任务的说法。 可靠的模型身份验证有望成为 AI 溯源、审计与信任体系的基础组件，使客户和监管方能够确认某段回复由哪个模型生成，而无需服务商公开模型权重。若被采用，它将让模型提供方有能力为其“究竟是哪个系统在为用户服务”的说法提供佐证，而随着模型被转售、微调或在 API 背后被替换，这一问题正日益突出。 模型提供方需要为每个发布的模型公开一个指纹，以便日后将输出与指纹进行匹配；该指纹不会泄露模型权重，验证也可以用户在本地设备上自行完成。该研究仍在进行中，Anthropic 表示目前没有部署计划。

telegram · zaihuapd · 11月4日 10:16

**背景**: zkSNARK 等加密证明系统允许一方在不披露底层数据的前提下证明某项计算被正确执行——在这里，底层数据即模型专有的权重。将这一技术应用于大语言模型十分困难，因为推理涉及数十亿次运算，因此 Anthropic 将 FlashProve 定位为通向实用化“可证明推理”的进展，而非成品。该工作与水印、内容签名等其他溯源手段并列，后者的目标都是让 AI 生成的内容可被追溯。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/provable-inference">Progress on provable inference for large language models</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/anthropic-flashprove-cryptographic-model-verification">Anthropic unveils cryptographic tool to verify model outputs</a></li>
<li><a href="https://enterpriseai.economictimes.indiatimes.com/news/industry/anthropic-develops-cryptographic-verification-based-open-source-system-to-verify-ai-model-outputs/135531548">Anthropic Unveils FlashProve: A Breakthrough in AI Model ...</a></li>

</ul>
</details>

**标签**: `#AI provenance`, `#model verification`, `#cryptography`, `#Anthropic`, `#open source`

---

<a id="item-4"></a>
## [甲骨文在美国施压下取消与腾讯 70 亿美元 AI 芯片租赁协议](https://www.tradingview.com/news/seekingalpha:e51e68f4d094b:0-oracle-cancels-7b-ai-chip-lease-with-tencent-amid-us-concerns-ft/) ⭐️ 8.0/10

甲骨文取消了一笔与腾讯签署的、价值约 70 亿美元的五年期 AI 芯片租赁协议，该协议原本允许腾讯通过甲骨文在东南亚的多个数据中心使用约 10 万枚先进 AI 芯片，首付款约占 30%。据报道，在美国官员向甲骨文表达担忧、且公司承受特朗普政府压力之后，这笔交易被叫停。 这笔交易的取消，堵上了中国云与 AI 企业获取先进算力的少数剩余迂回渠道之一——在美国出口管制下，它们无法直接购买这些芯片；这也表明华盛顿愿意向海外数据中心运营商等第三方中间商施压。它还说明美国出口政策正日益决定全球 AI 算力可以在何处、以何种方式部署，而大型云厂商正被夹在中间。 该租赁协议是通过甲骨文在东南亚（而非中国境内）的数据中心来使用芯片，而这些芯片同时受到华盛顿和北京两方面的限制。据报道，条款包括五年期内约 10 万枚先进 AI 加速芯片、约 30%首付款，因此协议被推翻对腾讯而言是财务与算力规划上的重大挫折。

telegram · zaihuapd · 11月4日 11:01

**背景**: 美国工业与安全局（BIS）依据《出口管理条例》（EAR）实施出口管制，限制向中国和澳门出售最先进的半导体及相关算力。由于这些规则不仅管直接销售，也涉及受管制硬件可被如何使用和访问，中国企业一直在探索在第三国租赁算力等替代方案。东南亚已成为 AI 数据中心的重要建设区域，因此成为这类安排颇具吸引力、但如今受到更严格审视的通道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/ai/oracle-kills-7bn-tencent-ai-chip-deal-under-trump-pressure">Oracle Kills $7BN Tencent AI Chip Deal Under Trump... | ZeroHedge</a></li>
<li><a href="https://informedclearly.com/en/ai/54192/us-china-ai-chip-war-export-controls-2026">US-China AI Chip War 2026: Export Controls, Rare Earths ...</a></li>
<li><a href="https://digitalinasia.com/southeast-asia-ai-data-centre-boom/">Who is Building AI Data Centres in Southeast Asia in 2026? A ...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Oracle`, `#Tencent`, `#export controls`, `#cloud infrastructure`

---

<a id="item-5"></a>
## [腾讯混元 Hy4 发布，首次引入视觉能力](https://mp.weixin.qq.com/s/JrQeiqx3PXBDSGish2IzwA) ⭐️ 7.0/10

腾讯于 11 月 4 日正式发布混元 Hy4，首次为混元大模型引入视觉理解能力，同时支持电脑操作，并针对 Blender、CAD 等专业软件进行了专项训练。在 579 个真实金融任务的众测中，Hy4 以 3.04 分位居开源模型第一，幻觉率则从 15.76% 降至 5.45%。 引入视觉与电脑操作能力，意味着混元从纯文本模型家族转向多模态智能体平台，使腾讯更直接地参与到能够“看屏幕、操作软件”的前沿模型竞争中。金融任务排名第一以及幻觉率大幅下降，对企业客户而言尤为关键，因为这些场景对输出可靠性要求极高。 模型已在腾讯云和 OpenRouter 路由平台上线，API 价格保持不变；官方还表示计划开源模型权重，并将在近期推出更具性价比的 Hy4 flash。不过公告本身披露的技术细节有限，例如参数量、上下文长度或评测方法均未提及，因此大部分性能结论仍依赖腾讯自有的测试数据。

telegram · zaihuapd · 11月4日 07:33

**背景**: 混元是腾讯自研的大模型系列，此前 8 月发布的 Hy4 preview 据报道总参数为 770B、激活参数 49B，上下文长度突破 1M。所谓“电脑操作能力”（computer use），是指模型能够识别屏幕内容并驱动鼠标键盘，跨应用完成多步骤任务，这一能力最早由 Claude 等前沿模型引入，随后被 OpenAI 的 Codex 与 GPT 系列扩展。Hy4 此次上线的 OpenRouter 是一个第三方模型路由平台，通过一套兼容 OpenAI 的 API 提供来自数十家厂商的数百个模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/1/019/328.htm">首次引入视觉理解， 腾 讯 混 元 Hy 4 、 Hy 4 flash AI 模 型 即将发布 - IT之家</a></li>
<li><a href="https://www.tmtpost.com/8121424.html">腾 讯 猛踩油门， 混 元 追赶的127天-钛媒体官方网站</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter</a></li>

</ul>
</details>

**标签**: `#Tencent Hunyuan`, `#multimodal AI`, `#LLM release`, `#computer use`, `#open-source models`

---

<a id="item-6"></a>
## [黑客团队 Calif 演示绕过锁定模式且越狱在 iOS 27.2 更新后仍存活](https://appleinsider.com/articles/26/11/04/apples-lockdown-mode-thwarted-by-a-new-persistent-iphone-jailbreak) ⭐️ 7.0/10

黑客团队 Calif 在 X 上发布视频，展示一台已开启锁定模式的 iPhone 18 Pro 被越狱，并且在设备通过 OTA 升级到 iOS 27.2 之后越狱状态依然保持。视频中先通过 AirDrop 传输一个 PDF 文件，随后用户在“设置”中完成系统更新，更新后越狱据称仍然有效。 锁定模式是苹果面向高风险人群推出的最强反间谍软件加固功能，苹果曾在 2026 年 3 月宣称其自 2022 年以来防护成功率达到 100%，因此一个能跨越系统更新的绕过演示会直接削弱这一面向记者、活动人士等高风险用户的安全承诺。这也说明即便攻击面被刻意收窄，一条由用户主动接受文件传输的路径仍可能足以启动完整利用链。 Calif 并未公开技术细节，表示正在将漏洞披露给苹果，同时不会发布越狱工具，因此该说法目前无法被第三方独立验证。演示中的具体信息——iPhone 18 Pro 与 iOS 27.2——尚属未经证实的超前内容，公开材料也只是一段短视频和 Telegram 频道摘要，而非技术报告。

telegram · zaihuapd · 11月4日 14:38

**背景**: 锁定模式是 iOS 中的一项可选设置，它通过大幅削减攻击面来对抗针对特定个人的商业间谍软件：限制大多数消息附件类型、削减网页浏览与媒体处理能力、禁用部分有线连接、拦截未知 FaceTime 来电等。越狱传统上意味着突破苹果沙盒、取得内核级控制权，而这类利用通常会被系统更新清除，因为更新会重刷并修补受影响的组件。若越狱能在 OTA 更新后持续存在，意味着利用链能在用户态重新建立，或潜伏于更新未完全替换的组件之中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://appleinsider.com/articles/26/11/04/apples-lockdown-mode-thwarted-by-a-new-persistent-iphone-jailbreak">Apple&#x27;s Lockdown Mode thwarted by a new iPhone jailbreak</a></li>
<li><a href="https://www.switchingtomac.com/iphone-jailbreak-bypasses-lockdown-mode-persists-ios-updates/">iPhone jailbreak demo gets past Lockdown Mode and survives an ...</a></li>
<li><a href="https://support.apple.com/en-us/105120">About Lockdown Mode - Apple Support</a></li>

</ul>
</details>

**标签**: `#iOS security`, `#jailbreak`, `#Lockdown Mode`, `#vulnerability disclosure`, `#mobile exploitation`

---

<a id="item-7"></a>
## [华为要求昇腾 960DT 客户自行解决 HBM 内存采购](https://thenextweb.com/news/huawei-hbm-smuggling-samsung-sk-hynix-ascend-960dt) ⭐️ 7.0/10

据 The Information 报道，华为已告知部分客户，其下一代旗舰 AI 芯片昇腾 960DT 将主要采用三星和 SK 海力士的 HBM，并且由于中国本土厂商 HBM 产能不足，客户需要自行解决内存来源。深圳一名芯片经纪人称，单颗 HBM3E 的价格已从一年前的数百美元涨至约 4000 美元，而相当一部分货源是通过将焊有 HBM 的低性能处理器按处理器编码报关运至香港、再人工携带入境的方式走私进来的。 这揭示了中国最重要的一款 AI 芯片所面临的严重供应链瓶颈：华为能够设计出有竞争力的加速器，但在本土 HBM 产能不足的情况下，无法为客户提供完整可部署的系统。报道中的走私路径和约十倍的涨价幅度表明，美国对先进内存的出口管制正在重塑中国 AI 基础设施的成本结构，并迫使买家转向灰色市场渠道。 据报道，走私的 HBM 被焊在性能极弱的处理器上，按处理器编码报关后运至香港，再由个人携带入境内地，最后通过加热拆下。约 4000 美元一颗 HBM3E 的价格来自单个经纪人的说法，而非广泛的市场指数；相关内容源自 The Information 的报道并经二手聚合转述，并非华为官方披露。

telegram · zaihuapd · 11月4日 14:52

**背景**: HBM（高带宽内存）是由三星、AMD 和 SK 海力士共同开发的 3D 堆叠 DRAM 接口，可为 AI 加速器和高性能计算系统提供所需的巨大内存带宽，通常通过先进封装与 GPU 或 NPU 裸片封装在一起。美国的出口管制限制了对华销售先进 HBM，这正是长鑫存储等本土厂商被要求加速扩产的原因；华为曾表示，面向训练优化的昇腾 960DT 计划于 2027 年第一季度前后实现商用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/09/17/huawei-plans-q1-2027-launch-of-new-ai-chip-as-it-takes-on-nvidia/">Huawei plans Q1 2027 launch of new AI chip as it takes on ...</a></li>
<li><a href="https://www.micron.com/products/memory/hbm">High-bandwidth memory (HBM) | Micron Technology Inc.</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Ascend 960DT`, `#HBM`, `#AI chips`, `#export controls`, `#semiconductor supply chain`

---

<a id="item-8"></a>
## [Google 对 K-12 学校账号默认关闭 Gemini 与搜索](https://9to5google.com/2026/11/03/google-search-ai-guided-learning-changes/) ⭐️ 6.0/10

2026 年 11 月 3 日，Google 宣布对学校管理的 K-12 学生账号默认关闭 Gemini、Gemini Notebook、Classroom 中的 Gemini 以及整合了 AI 的 Google 搜索，需要管理员手动开启。该政策本月起在美国部分学校试点，到 2027 年初，学校将不得不在“启用完整 AI 搜索”与“用 Guided Learning 取代搜索”之间二选一。 由于 AI Overviews 等生成式功能已经深度嵌入 Google 搜索，选择不用 AI 实际上就等于放弃搜索本身，这让 K-12 学区面临“全有或全无”的抉择，而不是细粒度的隐私管控。此举为教育场景中 AI 默认设置的治理立下了重要先例，并将影响数百万学生、教师和 IT 管理员使用 Google Workspace for Education 的方式。 到 2027 年初，学校只有两条路：启用包含 AI Overviews 在内的完整功能，或者用 Guided Learning 取代搜索，否则学生将完全无法使用搜索。Guided Learning 基于 Google 专为教育开发的语言模型 LearnLM 构建，设计目标是引导学生理解知识，而不是直接给出答案。

telegram · zaihuapd · 11月4日 05:00

**背景**: AI Overviews 是一项生成式 AI 功能，会在 Google 搜索结果顶部给出 AI 撰写的摘要，并附上可供深入查阅的链接。Guided Learning 是 Gemini 中偏重学习与理解、而非快速给答案的模式；Google Workspace for Education 则是学校为学生账号开启或关闭各项服务的管理控制台。由于搜索与 AI 功能日益共用同一套底层技术栈，Google 无法简单地剔除 AI 而保留“纯搜索”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech-insider.org/google-student-search-gemini-off-by-default-schools-opt-in-2026/">Google Turns Off Student Search and Gemini by Default</a></li>
<li><a href="https://blog.google/products-and-platforms/products/education/guided-learning/">Guided Learning in Gemini: From answers to understanding</a></li>

</ul>
</details>

**标签**: `#google`, `#education`, `#ai-policy`, `#search`, `#gemini`

---

<a id="item-9"></a>
## [华为、阿里等 20 家单位联合发布《智能体发展自律公约》](https://www.cls.cn/detail/2524879) ⭐️ 6.0/10

11 月 4 日，中国信通院联合华为、阿里、腾讯、小米等 20 家单位共同发布《智能体发展自律公约》。公约提出共建智能体互联基础设施，推进智能体注册与解析、能力描述与发现、协议兼容与互认等技术与标准，以降低跨域发现与连接的成本。 当前智能体协议碎片化严重、多种规范并存，由国内主要云与终端厂商联手行业主要标准机构推动统一，有望显著降低开发者构建多智能体系统时的集成成本。这也表明中国企业希望在外部主导的协议成为事实标准之前，尽早参与塑造智能体互联规范与治理话语权。 该公约明确定位为自愿性的自律约定，而非强制性技术标准，公告中未给出时间表、版本号、参考实现或开源承诺。除互联互通外，公约还提出发展低门槛的智能体开发部署工具，并合作研发面向真实作业场景的智能体，推动其嵌入现有生产系统和业务流程。

telegram · zaihuapd · 11月4日 08:45

**背景**: 智能体（AI Agent）是借助大语言模型进行规划并执行多步骤任务的软件，它经常需要调用其他智能体或工具，因此“智能体之间如何相互发现与通信”成为关键问题。目前业界已出现多种相互竞争的智能体协议：Anthropic 于 2024 年 11 月主导提出 MCP，Google 于 2025 年 4 月发布 A2A，AgentUnion 于 2025 年 5 月发布 ACP，AIP 的首版代码则在 2025 年 10 月底发布。中国信通院是隶属工业和信息化部的研究机构，长期牵头协调国内标准制定工作，这也是此类多企业联合发布中其署名具有分量的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E6%99%BA%E8%83%BD%E4%BD%93%E5%8D%8F%E8%AE%AE/67694554">智能体协议 - 百度百科</a></li>
<li><a href="https://w3c-cg.github.io/ai-agent-protocol/index_cn.html">智能体网络协议技术报告 - w3c-cg.github.io</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1987615007253489160">【智能体互联协议解析】如何实现跨域的智能体互联协作？ - 知乎</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#industry standards`, `#interoperability`, `#China tech`, `#AI governance`

---

<a id="item-10"></a>
## [印度成 ChatGPT 全球最大市场，用户数自 1 月以来翻倍](https://economictimes.indiatimes.com/tech/newsletters/morning-dispatch/openais-india-user-base-doubles-rapido-gov-quadruples/articleshow/135478625.cms) ⭐️ 6.0/10

OpenAI 印度区负责人表示，按周活跃用户计算，印度已成为 ChatGPT 全球最大的市场，印度用户数自今年 1 月以来已经翻倍。公司还预计将在未来数周内公布与 UPI 及支付相关的消息，同时印度市场的企业应用正从试点阶段转向规模化部署。 印度在周活跃用户上超越其他地区，说明 ChatGPT 的增长越来越依赖价格敏感、以移动端为主的新兴市场，而不再只是美国和欧洲。即将到来的 UPI 与支付集成则让 OpenAI 得以在本地实现变现，并可能成为其在其他市场推广“对话式商务”的模板。 此次公布属于宏观市场层面的更新，除“自 1 月以来翻倍”外并未披露具体用户规模，OpenAI 也未说明将推出哪些支付产品。印度此前已是更便宜的 ChatGPT Go 订阅（每月 399 卢比、支持 UPI）的首发市场，而该套餐在印度推出免费试用时，曾因需求过大出现 UPI 验证报错和支付失败。

telegram · zaihuapd · 11月4日 09:31

**背景**: UPI（统一支付接口）是印度国家支付公司（NPCI）打造的即时支付系统，用户凭一个 UPI ID 即可在手机上完成跨行个人转账和个人对商户付款。它已成为印度人线上支付的主流方式，因此支持 UPI 几乎是任何面向消费者的订阅服务进入该国市场的必要条件。ChatGPT Go 是 OpenAI 以印度为首发市场推出的低价套餐，而 OpenAI 对支付的兴趣表明它希望从单纯订阅走向在聊天界面内完成交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://timesofindia.indiatimes.com/technology/tech-news/openai-launches-chatgpt-go-in-india-at-rs-399-per-month-with-upi-support-what-you-get-what-you-dont/articleshow/123377874.cms">OpenAI launches ChatGPT Go in India at Rs 399 per month with UPI ...</a></li>
<li><a href="https://telanganatoday.com/chatgpt-gos-free-rollout-in-india-hits-upi-glitch-amid-surge-in-demand">ChatGPT Go’s free rollout in India hits UPI glitch... - Telangana Today</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#India`, `#market growth`, `#UPI payments`

---

<a id="item-11"></a>
## [Cloudflare 推出个人 AI 代理流量分析与分级管控](https://blog.cloudflare.com/personal-agents-visibility-control/) ⭐️ 6.0/10

Cloudflare 在 Security Analytics 的机器人分析图中新增了「个人助理（Personal Assistants）」类别，并在 Top 统计下新增组件，可按单个代理展示请求数、请求路径与状态码。Agents 策略现在支持按代理设置三种动作——允许、仅在含广告页面拦截、拦截，并更名为「AI Crawler and Agent access policies」；启用 Account Abuse Protection 的站点还能看到代理代表的是哪位用户。 代表个人用户浏览网页的个人 AI 代理模糊了人类流量与自动化流量的界限，因此为站点提供可视化能力以及「广告页拦截」这一中间选项，可以让发布者把代理访问变现，而不必在允许与拦截之间二选一。这把 Cloudflare 已有的 AI 爬虫管控从训练爬虫、搜索爬虫延伸到了面向消费者的助理类代理，对依赖机器人管理与广告收入的站点意义重大。 新类别与 Verified Bot、Likely Human、Likely Automated、Automated 等既有机器人分析分组并列，使团队可以单独按时间追踪代理流量。管控执行与 Cloudflare 托管的 robots.txt 及 AI Crawl Control 挂钩，而按用户归因的视图需要启用 Account Abuse Protection，该功能目前面向 Bot Management 企业版客户开放早期访问。

telegram · zaihuapd · 11月4日 15:42

**背景**: Cloudflare 维护着其自称全球最大的已验证机器人目录，将到达客户站点的流量分类，使管理员可以针对已知机器人而非原始 IP 制定策略。机器人大致被划分为搜索爬虫、AI 训练爬虫和 AI 代理爬虫三类，Cloudflare 一直在推动 AI 公司把搜索抓取与训练、代理抓取区分开来，并威胁对含广告页面实施默认的网络层拦截。Account Abuse Protection 则是一套独立的反欺诈能力，用于识别人与机器人中的高风险身份和滥用行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/cloudflare-personal-agents-analytics-access-policies-2026">Cloudflare Personal Agents: Allow, Block or Ad-Gate Each One ...</a></li>
<li><a href="https://www.unite.ai/cloudflare-adds-personal-agent-analytics-and-per-agent-access-controls/">Cloudflare Adds Personal Agent Analytics and Per-Agent Access ...</a></li>
<li><a href="https://developers.cloudflare.com/bots/account-abuse-protection/">Account Abuse Protection (Early Access) · Cloudflare bot ...</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#AI agents`, `#bot management`, `#web analytics`, `#access control`

---