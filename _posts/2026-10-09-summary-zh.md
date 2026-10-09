---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09 23:03:42 +0000
lang: zh
report: default
---

> 从 202 条内容中筛选出 6 条重要资讯。

---

1. [Anthropic 推出开源漏洞扫描服务 OSS Scanner](#item-1) ⭐️ 8.0/10
2. [中国天眼 FAST 发现首例仍在演化阶段的原生脉冲星三体系统](#item-2) ⭐️ 8.0/10
3. [Telegram Desktop 曝一键窃取任意文件漏洞](#item-3) ⭐️ 8.0/10
4. [亚马逊造出第 1000 颗卫星，太空互联网服务即将商用](#item-4) ⭐️ 7.0/10
5. [JetBrains 发布开源编程模型 Mellum2.1，12B MoE 架构](#item-5) ⭐️ 7.0/10
6. [Meta 在美国、日本等七国封禁字节跳动广告](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 推出开源漏洞扫描服务 OSS Scanner](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source) ⭐️ 8.0/10

Anthropic 宣布推出 OSS Scanner，这是一项面向符合条件的开源项目、免费且自愿接入的漏洞扫描服务，报告由 Claude 等模型自动生成。Anthropic 称过去半年共发现逾 2.9 万个候选漏洞，其中约 6000 个经过人工审查，早期测试的 97 个高危或严重漏洞中有 85 个符合其披露流程要求。 这标志着 LLM 辅助的大规模安全研究正在成为现实，让缺乏资金的开源维护者可以免费发现商业扫描工具和志愿者审查常常遗漏的缺陷。如果模型生成的发现经得起检验，AI 驱动的漏洞初筛有望成为开源供应链安全的标准环节。 这些报告由模型自动生成、未经人工审核，因此可能存在错误；报告内含漏洞复现步骤、漏洞说明，并在条件允许时给出补丁建议。符合条件的项目核心维护者可通过提交 GitHub PR 申请接入，该服务还提供可选的快速通道。

telegram · zaihuapd · 10月9日 02:00

**背景**: Claude 是 Anthropic 开发的大语言模型系列，最早于 2023 年 3 月以聊天机器人形式发布。开源项目通常由小型志愿者团队维护，没有预算做安全审计，因此 AI 厂商开始提供免费扫描服务，既做公益也展示模型能力。OSS Scanner 依托 Anthropic 的前沿模型，在代码仓库中搜索安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://red.anthropic.com/oss-scanner/">OSS Scanner</a></li>
<li><a href="https://github.com/anthropics/oss-scanner">GitHub - anthropics/ oss - scanner · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude ( AI ) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI security`, `#vulnerability scanning`, `#open source`, `#Anthropic`, `#Claude`

---

<a id="item-2"></a>
## [中国天眼 FAST 发现首例仍在演化阶段的原生脉冲星三体系统](https://nao.cas.cn/news/gd/202610/t20261009_8289939.html) ⭐️ 8.0/10

中欧科学家独立确认，中国天眼 FAST 发现的脉冲星 PSR J0435+3233 属于首例仍处于演化阶段的原生三体系统，由脉冲星、白矮星和类太阳恒星组成，其内、外轨道周期分别为 8 天和 73.5 年。相关成果于 2026 年 10 月 9 日发表于《天体物理学杂志快报》（ApJL）。 这是迄今被确认的第二例脉冲星三体系统，也是首例在轨道尚未稳定前就被捕捉到的系统，为天文学家提供了观察此类层级系统如何形成与演化的罕见“活样本”。同时，它也展示了 FAST 探测其他望远镜难以分辨的微小轨道与时序变化的能力，巩固了中国在脉冲星与引力物理研究中的地位。 PSR J0435+3233 是一颗不寻常的毫秒脉冲星，其自转减慢率比银河系中任何已知毫秒脉冲星都高约两个数量级，在周期—周期导数（P–Ṗ）图上显著位于“自旋加速线”之上。它的第二颗伴星被确认为类太阳的 G 型亚巨星，研究人员还在 Fermi 数据中探测到该系统的伽马射线辐射，这为确认其三体结构及仍处于演化阶段提供了关键证据。

telegram · zaihuapd · 10月9日 05:14

**背景**: FAST（500 米口径球面射电望远镜）位于中国贵州，是世界上最大的单口径射电望远镜，对中子星发出的微弱而精确计时的射电脉冲尤为敏感。脉冲星是高速自转、磁场极强的中子星，其脉冲如同极其稳定的时钟，因此脉冲到达时间的微小变化可以揭示看不见的伴星所产生的引力影响。所谓“原生”（ primordial）三体系统，是指三颗恒星一起形成并始终束缚在同一系统中，而非后期通过恒星俘获或交换形成。脉冲星三体系统是检验引力理论和恒星演化的天然实验室，因为其轨道会受到多体引力场的共同作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.01227">The PSR J 0435 + 3233 Triple System</a></li>
<li><a href="http://english.cas.cn/research/platforms/large-research-infrastructures/homepage-display/202604/t20260408_1155383.shtml">Scientists Identify Millisecond Pulsar PSR J 0435 + 3233 , Challenging...</a></li>
<li><a href="https://focus.scol.com.cn/zgsz/202610/83336491.html">“中国天眼”发现首例 原 生 演化 脉 冲 星 三 体 系 统 _四川在线</a></li>

</ul>
</details>

**标签**: `#astronomy`, `#FAST`, `#pulsar`, `#triple-system`, `#astrophysics`

---

<a id="item-3"></a>
## [Telegram Desktop 曝一键窃取任意文件漏洞](https://telegram.me/zaihuapd/44307) ⭐️ 8.0/10

Telegram Desktop 7.2.9 以下版本被曝存在编号为 CVE-2026-107181 的严重漏洞，用户只要点击恶意的 tg:// 深链接，攻击者就可能在没有任何确认提示的情况下悄悄窃取本地任意文件。官方已在 7.2.9 版本中完成修复，建议用户尽快升级。 Telegram Desktop 是拥有数亿用户的跨平台客户端，这种“一点即窃”的漏洞对普通用户和安全从业者都构成严重威胁，可能导致文档、浏览器会话、SSH 密钥乃至加密钱包被窃取。它也说明桌面应用的深链接处理器与 IPC 机制很容易演变为高危害的攻击面。 据报道，该漏洞源于 Core::Sandbox 的 IPC 处理逻辑：链接中的分号未被转义，被当作一条独立的 IPC 命令，配合 interpret: 处理器即可盗取任意文件。攻击者可窃取文档、浏览器会话数据、SSH 密钥和加密钱包；建议的缓解措施是升级到 7.2.9 及以上版本、警惕异常 tg:// 链接，并启用本地密码。

telegram · zaihuapd · 10月9日 09:51

**背景**: Telegram Desktop 是 Telegram 在 Windows、macOS 和 Linux 上的官方客户端，通过网络层的 MTProto 协议与服务器通信。tg:// 深链接（以及 t.me 链接）能让其它应用或网页把某个操作直接交给 Telegram 执行，比如打开某个对话或某个设置项，用户无需手动输入。在实现上，桌面客户端内部使用 IPC（进程间通信）并配合沙箱组件安全地执行部分任务，而分号一类的分隔符常用于在单条记录中编码多条命令；一旦这些分隔符没有被正确转义，被注入的内容就会被当作额外命令执行，这正是本次漏洞所利用的典型注入模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cve.org/CVERecord?id=CVE-2026-107181">CVE Record: CVE - 2026 - 107181</a></li>
<li><a href="https://securityvulnerability.io/vulnerability/CVE-2026-107181">CVE - 2026 - 107181 : IPC Record-Separation Injection Vulnerability in...</a></li>
<li><a href="https://core.telegram.org/api/links">Deep links</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#telegram`, `#CVE`, `#desktop`

---

<a id="item-4"></a>
## [亚马逊造出第 1000 颗卫星，太空互联网服务即将商用](https://arstechnica.com/space/2026/10/amazon-builds-1000th-satellite-is-weeks-away-from-space-internet-rollout/) ⭐️ 7.0/10

亚马逊已在华盛顿州柯克兰工厂完成其 Amazon Leo 低轨互联网星座的第 1000 颗卫星，并称距离启动商业服务仅剩数周时间。即将发射的卫星将搭乘 ULA 的 Vulcan 火箭执行复飞任务，另有一枚 Vulcan 正在准备于 2026 年发射更多卫星。 卫星数量突破 1000 颗，意味着亚马逊从纸面规划变成了 SpaceX 星链之外真正具备规模的第二个商业挑战者，可能重塑卫星宽带市场的价格与覆盖格局。若部署顺利，企业、政府和网络欠发达地区将获得低延迟连接的可靠替代选择，同时也让亚马逊更加依赖仍属新秀的 ULA Vulcan 火箭。 Amazon Leo 卫星此次搭乘的是 Vulcan 在助推器问题导致停飞后的复飞任务，而亚马逊此前还提议将星座规模扩展至最多 5105 颗卫星，并提供直连智能手机的语音与数据服务。第 1000 颗卫星这一里程碑反映的是产能而非在轨部署数量，因此真正投入运行的在轨星座规模仍远小于累计制造数量。

telegram · zaihuapd · 10月9日 04:30

**背景**: 低地球轨道（LEO）星座把数百至数千颗小型卫星部署在距地面几百公里的轨道上，相比传统地球同步轨道卫星能提供更高带宽和更低通信延迟，这正是 SpaceX 星链和如今的 Amazon Leo 选择该轨道的原因。Vulcan Centaur 是美国联合发射联盟（ULA）的重型运载火箭，采用蓝色起源的 BE-4 发动机，用于取代 Atlas V 和 Delta IV；它于 2024 年 1 月首飞，2025 年 3 月获得美国国家安全发射认证，但在 2026 年因固体火箭助推器问题一度停飞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vulcan_rocket">Vulcan rocket</a></li>
<li><a href="https://en.wikipedia.org/wiki/Low_Earth_orbit">Low Earth orbit - Wikipedia</a></li>
<li><a href="https://www.aol.com/articles/amazon-leo-proposes-constellation-over-130615000.html">Amazon &#x27;s Leo proposes satellite constellation for... - AOL</a></li>

</ul>
</details>

**标签**: `#Amazon`, `#satellite internet`, `#space`, `#LEO constellation`, `#Vulcan rocket`

---

<a id="item-5"></a>
## [JetBrains 发布开源编程模型 Mellum2.1，12B MoE 架构](https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/) ⭐️ 7.0/10

JetBrains 发布了 Mellum 2.1，这是一个以 Apache 2.0 许可开源的编程模型，采用 12B 参数的混合专家（MoE）架构、2.5B 激活参数，模型权重已在 Hugging Face 上提供。与前代相比，强化学习从短期的代码补全扩展为核心训练环节，并在数百万个软件工程与算法沙箱环境中进行了针对性强化，使模型能够探索代码库、编辑文件并检查自己的修改。 JetBrains 推出一款明确面向编程代理、且采用宽松许可证的模型，降低了企业与个人开发者私有化、本地化部署编程助手的门槛，使其不必依赖闭源 API 服务商。这也表明 IDE 与开发工具厂商正从单纯的前沿模型使用者，转变为自研并发布面向代理的模型，从而与 Qwen-Coder 等开源编程模型一道，加剧开源权重编程模型领域的竞争。 12B 总参数与 2.5B 激活参数的划分意味着每个 token 只实际计算被选中的专家子网络，因此推理成本与延迟取决于约 2.5B 的激活参数，而非完整的 12B 权重规模，这正是该模型被定位为本地代理“快速”选项的实际原因。代价是服务时仍需把完整权重加载进内存，因此其部署所需的显存/内存仍明显高于同等激活规模的稠密模型。

telegram · zaihuapd · 10月9日 07:30

**背景**: 混合专家（MoE）是一种稀疏神经网络架构：模型内部包含许多专门的“专家”子网络，外加一个路由器，每个输入只激活与任务相关的少数专家，而不像稠密模型那样让所有参数都参与计算。这正是 MoE 模型常用两个数字来描述的原因——总参数（全部权重，决定内存占用）与激活参数（每个 token 实际使用的权重，决定速度与算力成本）。“编程代理”则是指由大模型驱动、不止于代码补全的工具：它可以阅读代码库、规划多步修改、编辑文件并运行或验证代码，因此通常需要在可执行环境中进行强化学习，而不能只依赖静态代码文本的训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.brandeploy.io/en-ai-architecture-mixture-of-experts-moe">The triumph of mixture - of - experts : AI&#x27;s secret to... — Brandeploy</a></li>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between Total and...</a></li>
<li><a href="https://www.openhands.dev/">OpenHands | Open Source AI Coding Agent Platform</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#coding-agents`, `#LLM`, `#JetBrains`

---

<a id="item-6"></a>
## [Meta 在美国、日本等七国封禁字节跳动广告](https://www.theverge.com/tech/1008658/meta-tiktok-bytedance-ads-ban) ⭐️ 6.0/10

Meta 已在七个国家禁止字节跳动在其平台上投放广告，包括美国、加拿大、埃及、印尼、日本、泰国和越南，该禁令于当地时间 10 月 8 日生效。此举同时限制了字节跳动的付费营销，以及指向 TikTok 的第三方广告。 此举升级了两大短视频与社交平台之间的竞争，把付费分发渠道变成争夺用户注意力和广告预算的“守门”武器。这也表明大型平台越来越倾向于限制竞争对手接触自家用户，而非纯粹在产品层面竞争。 Meta 发言人将这一决定描述为常见的商业做法，称公司没有义务为试图把用户拉离自家应用的竞争对手提供广告服务。该禁令出台之前，Meta 刚与美国多个州就儿童安全和青少年成瘾指控达成 170 亿美元和解，并在和解后公开呼吁 TikTok 和 YouTube 采取类似限制措施。

telegram · zaihuapd · 10月9日 16:04

**背景**: Meta 与字节跳动是短视频和社交媒体领域的直接竞争对手，Meta 旗下的 Reels 和 Instagram 与字节跳动的 TikTok 争夺同一批用户和广告收入。第三方广告指的是为推广平台之外的产品或落地页而购买的广告投放，在这里特指投放在 Meta 应用上、却把用户导向 TikTok 的广告。平台通常自行制定广告政策，拒绝为直接竞争对手投放广告在媒体和科技行业由来已久，但如此大规模地实施仍属少见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.buaq.net/go-438233.html">Meta 将支付 170 ...</a></li>
<li><a href="https://www.bilibili.com/video/BV1bp8f64EmP/">天价赔偿！ Meta 同意支付171... | 哔哩哔哩</a></li>
<li><a href="https://privat-nn.ru/manyvoices/read/news_ifeng_com_c_8wtkueil3nd_5f2de684">莫让“手机式 童 年”遮住成长的阳光 - ManyVoices</a></li>

</ul>
</details>

**标签**: `#Meta`, `#ByteDance`, `#TikTok`, `#Advertising`, `#Platform Policy`

---