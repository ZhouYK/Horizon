---
layout: default
title: "Horizon Summary: 2026-10-22 (ZH)"
date: 2026-10-22 23:03:34 +0000
lang: zh
report: default
---

> 从 171 条内容中筛选出 9 条重要资讯。

---

1. [澳大利亚法院裁定苹果须向第三方应用商店开放 iPhone](#item-1) ⭐️ 8.0/10
2. [333 个被植入 Ebury 后门的 Tor 出口节点被下线](#item-2) ⭐️ 8.0/10
3. [被禁运的 Nvidia B300 芯片现身中国国资背景网络](#item-3) ⭐️ 8.0/10
4. [Anthropic 发布 Claude API 2026-10-21，移除 temperature 与 top\_p/top\_k](#item-4) ⭐️ 7.0/10
5. [特朗普：建数据中心的企业应向当地社区缴纳「分红」](#item-5) ⭐️ 7.0/10
6. [研究：关闭内容识别后智能电视仍在上报观看数据](#item-6) ⭐️ 7.0/10
7. [米哈游联合清华开源 GameScaling 游戏操作模型](#item-7) ⭐️ 7.0/10
8. [甲骨文就 JSSE 高危漏洞发布 Java SE 安全警报](#item-8) ⭐️ 7.0/10
9. [小鹏 IRON 机器人升级：每 0.2 秒重新推理一次做出反馈](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [澳大利亚法院裁定苹果须向第三方应用商店开放 iPhone](https://9to5mac.com/2026/10/21/apple-must-open-iphone-to-alternative-app-stores-in-australia-after-epic-games-ruling/) ⭐️ 8.0/10

澳大利亚联邦法院裁定，苹果须从 2027 年 3 月 1 日起允许澳区 iPhone 用户通过第三方应用商店和网站安装应用，并开放替代支付方式与外部支付链接。该裁决源于 Epic Games 提起的反垄断诉讼，Fortnite 将立即重返澳区 App Store；苹果表示将提起上诉并申请暂缓执行。 这是欧盟之外首个强制苹果开放 iOS 应用分发与支付体系的主要司法辖区，其判例可能被其他国家的监管机构和诉讼方援引。若上诉后裁决得以维持，将重塑这一规模可观市场中开发者的 App Store 经济模式，并加大苹果全球 15%–30% 抽成模式所面临的压力。 法官认定苹果在 iOS 应用分发和支付市场具有实质性市场力量，其限制行为实质性削弱了竞争，违反澳大利亚竞争法。相关义务将于 2027 年 3 月 1 日生效，但苹果计划上诉并申请暂缓执行，可能推迟或收窄这些要求，因此时间表尚未最终确定。

telegram · zaihuapd · 10月22日 06:54

**背景**: 侧载（sideloading）指绕过苹果的强制审核与应用内购买体系，从官方 App Store 之外向 iPhone 安装应用；苹果长期禁止这一做法，理由是保护用户安全与隐私。2020 年 Fortnite 因引入自有直接支付选项被下架后，Epic Games 起诉苹果，该案在美国已产生喜忧参半的判决，并助推了欧盟《数字市场法》的出台——在该法规下，苹果目前已在欧洲允许 AltStore PAL 等替代应用市场运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/2021/4/29/22410877/epic-games-apple-app-store-antitrust-trial-lawsuit-news">Epic Games v . Apple : the fight for the future of the App... | The Verge</a></li>
<li><a href="https://grokipedia.com/page/Sideloading_on_iOS">Sideloading on iOS</a></li>
<li><a href="https://altstore.io/">AltStore - Sideloading for Everyone</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#apple`, `#app-store`, `#regulation`, `#epic-games`

---

<a id="item-2"></a>
## [333 个被植入 Ebury 后门的 Tor 出口节点被下线](https://kaba.cx/posts/20261020_Tor/) ⭐️ 8.0/10

一名 Tor 中继运营者用脚本扫描了约 3000 个出口中继，发现其中 333 个（约 10%）被植入 Ebury 后门，这些节点会把 22 端口的 SSH 连接劫持到 12 台拦截服务器上以窃取登录凭据。这些中继于 10 月 4 日被标记为 BadExit，次日已全部下线。 出口中继是 Tor 流量重新进入公网的最后一跳，约 10% 的节点被攻陷意味着在攻击窗口期内，相当比例的用户 SSH 登录和明文数据可能被悄无声息地窃取。这也说明，目前主要依靠志愿运营者推动的 BadExit 标记机制，仍是抵御恶意中继的主要防线。 攻击者早在今年 8 月就已入侵这些服务器，并据称屏蔽了部分端口，以便专门收集未加密的邮件流量；SSH 会话则似乎是在用户接受已变更的主机密钥时被截获的。最初的入侵途径目前仍无定论，而且约 10% 这一比例来自单个运营者的扫描，并非 Tor 项目方的正式审计。

telegram · zaihuapd · 10月22日 14:52

**背景**: Tor 的流量要经过三跳中继，其中出口中继负责真正连接目标服务器，因此控制它的一方可以观察甚至篡改任何未做端到端加密的内容。Ebury 是 Linux 上一个为人熟知已久的 OpenSSH 后门兼凭据窃取程序，通常通过篡改 OpenSSH 加载的共享库实现注入，ESET 在 2024 年称其已控制约 40 万台服务器。Tor 的目录权威会给配置错误或存在恶意行为的中继打上 BadExit 标记，使其实际上变成“非出口”，从而让客户端不再经由它出网。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://attack.mitre.org/software/S0377/">Ebury, Software S0377 | MITRE ATT&amp;CK®</a></li>
<li><a href="https://www.eset.com/us/about/newsroom/press-releases/eset-research-ebury-botnet-alive-growing/">ESET Research: Ebury botnet alive &amp; growing; 400k Linux ...</a></li>
<li><a href="https://support-torran-614d1f0af8d705a14a8e1cd6f9898bed23485e1842c2493e.pages.torproject.net/relay-operators/what-is-the-bad-exit-flag/">What is the BadExit flag? | Tor Project | Support</a></li>
<li><a href="https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html">Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH ...</a></li>

</ul>
</details>

**标签**: `#Tor`, `#Ebury`, `#malware`, `#cybersecurity`, `#credential theft`

---

<a id="item-3"></a>
## [被禁运的 Nvidia B300 芯片现身中国国资背景网络](https://theinference.org/article/china-s-state-money-bought-banned-nvidia-b300-servers-then-redacted-the-receipts) ⭐️ 8.0/10

据报道，一家中国国资控股的半导体租赁集团为 AI 公司荣耀视图科技融资购入 32 台搭载英伟达 B300 芯片的华硕服务器，这只是一笔总额超 30 亿元人民币、逾 700 台服务器交易的一部分，计划部署于中国移动宁夏枢纽。相关备案在引发关注后被重新提交，硬件描述被抹去；英伟达表示正联合代工伙伴展开调查，华硕则称其遵守出口管制规定。 B300 处于美国出口管制中最严格的层级，对华基本禁运，因此它出现在国资相关部署中的报道，意味着最先进 AI 加速器的供应链可能存在执法漏洞。此事可能加剧美中科技政策摩擦，引发对服务器代工厂与租赁中介更严格的合规审查，并直接影响中国 AI 企业获取前沿算力的途径。 该报道基于公开备案文件而非经证实的企业或海关记录，因此这批货物仍未经核实；涉案硬件与华硕 XA NB3I-E12 相符，这是一款 9U 机箱、搭载 8 颗 NVIDIA HGX B300 GPU 的系统。B300 于 2025 年 9 月发布，单卡配备 288GB HBM3e、8TB/s 带宽，稠密 FP4 算力约 15 petaFLOPS，远高于需许可证才能对华销售的性能门槛。

telegram · zaihuapd · 10月22日 15:22

**背景**: 英伟达 B300 属于 Blackwell Ultra 世代的数据中心 GPU，是该公司性能最强的 AI 加速卡之一，因此被美国商务部工业与安全局（BIS）的对华先进芯片出口限制直接覆盖，此类出口需申请许可证且极少获批。中国移动宁夏枢纽属于国家“东数西算”算力网络工程的一部分，即在西部省份建设大型数据中心以服务全国的 AI 与云需求。在这类采购中，国资背景的租赁与融资平台常充当中介，先垫资购入硬件再转租给 AI 企业，这使得最终使用方与硬件流向更难追踪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://servers.asus.com/products/servers/gpu-servers/XA-NB3I-E12">XA NB3I-E12 | ASUS Servers</a></li>
<li><a href="https://resources.nvidia.com/en-us-dgx-systems/dgx-b300-datasheet">NVIDIA DGX B300 Datasheet</a></li>
<li><a href="https://www.nvidia.com/en-us/about-nvidia/company-policies/export-regulations/">NVIDIA Networking Export Regulation Compliance | NVIDIA</a></li>

</ul>
</details>

**标签**: `#export-controls`, `#nvidia`, `#semiconductors`, `#china`, `#ai-hardware`

---

<a id="item-4"></a>
## [Anthropic 发布 Claude API 2026-10-21，移除 temperature 与 top\_p/top\_k](https://x.com/ClaudeDevs/status/2113013247209021918) ⭐️ 7.0/10

Anthropic 发布了 Claude API 版本 2026-10-21，这是自 2023-06-01 以来的首次正式日期版本更新，移除了 temperature、top\_p 和 top\_k 三个采样参数，继续传入这些参数会返回 HTTP 400 错误。同时认证头改为 Authorization: Bearer，官方 SDK 与 ant CLI 已默认切到新版本，而旧的 2023-06-01 版本仍然受支持、尚未弃用。 这是对应用最广泛的 LLM API 之一所做的破坏性变更，任何硬编码 temperature 或 top\_p 的应用一旦采用新版本或升级后的 SDK，就会立刻开始收到 400 错误。这也释放出一个信号：API 设计正在从暴露采样参数控制转向由提示词层面和模型侧来控制输出，开发者需要相应调整。 由于 SDK 和 CLI 现在默认使用新版本，即使业务代码没有改动，仅升级客户端库也可能让现有代码失效，因此显式固定 anthropic-version: 2023-06-01 是当下最直接的规避方案。参数被移除意味着开发者失去了通过 temperature 调节输出确定性与创造性的手段，原先依靠采样参数调优的行为需要改由提示词或其他受支持的选项来实现。

telegram · zaihuapd · 10月22日 03:54

**背景**: Claude 的 API 通过 anthropic-version 请求头进行版本控制，客户端 SDK 会自动设置它，而像 2023-06-01 这样的日期化版本让 Anthropic 可以在演进请求格式时不悄悄破坏调用方。temperature、top\_p（核采样）和 top\_k 等采样参数长期以来是控制 LLM 下一个 token 分布的标准手段，用来在确定性与创造性之间取舍。认证过去使用 x-api-key 请求头，而 Authorization: Bearer 是更通用的 HTTP 认证方案，被更广泛的 API 生态所采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/api/versioning">Versions - Claude Platform Docs - Anthropic</a></li>
<li><a href="https://letsdatascience.com/blog/llm-sampling-temperature-top-k-top-p-and-min-p-explained">LLM Sampling Parameters Explained : Intuition... | Let&#x27;s Data Science</a></li>
<li><a href="https://apidog.com/blog/api-key-vs-bearer-token/">API Key vs Bearer Token: Which One Should You Choose?</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude API`, `#breaking changes`, `#LLM tooling`, `#API design`

---

<a id="item-5"></a>
## [特朗普：建数据中心的企业应向当地社区缴纳「分红」](https://www.reuters.com/business/retail-consumer/trump-says-companies-should-pay-dividend-communities-make-data-centers-popular-2026-10-21/) ⭐️ 7.0/10

美国总统特朗普于 10 月 21 日在 Truth Social 上发文表示，建设数据中心的企业若想获得当地欢迎，就应向所在社区缴纳「分红」，并称一些原本极不受欢迎的项目在达成财务协议后变得极受欢迎。他还表示，大型数据中心必须自建电力，并将多余电力赠予或出售给当地社区。 数据中心的能耗与水耗已成为全美政治争议焦点，总统公开支持向社区付费并要求自建电力，预示着未来 AI 基础设施交易的结构可能发生变化。这将迫使超大规模云厂商与开发商去谈判具有约束力的本地利益协议，而非仅依赖税收优惠，也可能促使选址向能源政策更友好的地区转移。 该表态只是社交媒体发文，而非正式政策提案，因此并不具备直接法律效力，是否会转化为立法、审批条件或联邦激励措施仍不明确。所谓「分红」如何计算、由谁收取、自建电力达到何种规模才算达标等具体细节均未界定。

telegram · zaihuapd · 10月22日 05:39

**背景**: AI 训练与推理负载推动了大型数据中心的快速建设，这类设施为算力消耗巨量电力，并在蒸发冷却中消耗大量水资源。围绕电网压力、用水、噪音和电费上涨的本地反对声浪不断上升，促使市政当局与开发商协商「社区利益协议」（CBA）——以本地支持换取保证性付款、基础设施或其他让步的法律约束性合同。与此同时，电网并网排队与容量瓶颈让燃气轮机、燃料电池等自建发电方式对运营商越来越有吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.brookings.edu/articles/why-community-benefit-agreements-are-necessary-for-data-centers/">Why community benefit agreements are necessary for data centers</a></li>
<li><a href="https://www.wri.org/technical-perspectives/community-benefits-agreements-data-centers">Powering Progress: How Community Benefits Agreements Can ...</a></li>
<li><a href="https://enkiai.com/data-center/data-center-power-2026-on-site-generation-is-mandatory/">Data Center Power 2026: On-Site Generation is Mandatory</a></li>

</ul>
</details>

**标签**: `#data-centers`, `#AI-infrastructure`, `#energy-policy`, `#regulation`, `#tech-industry`

---

<a id="item-6"></a>
## [研究：关闭内容识别后智能电视仍在上报观看数据](https://watchingthewatchers.github.io/watchingthewatchers/index.html) ⭐️ 7.0/10

一项针对 10 家厂商 12 台智能电视、共 5943 次受控实验的研究发现，部分机型即使用户在设置中关闭了自动内容识别（ACR）功能，仍会继续上报与观看内容相关的遥测数据。其中两个平台问题尤为突出：VIDAA OS 通过明文 MQTT 发送包含不可重置设备 ID 和音频指纹的数据，而 Vizio 的 WatchFree+ 则把节目名称写进用户无法关闭的未加密 DNS 查询中。 这些发现说明，厂商引导用户去拨动的那个“隐私开关”可能只是摆设，动摇了智能电视领域消费者知情同意的核心前提。由于至少有两个平台的数据是以明文离开设备的，局域网内或链路上的任何人都能看到，这就把单纯的追踪问题升级为窃听与设备指纹识别的风险，波及每一个使用这类电视的家庭。 该研究属于实证性、可复现的测量工作，覆盖 10 家厂商的 12 台电视、共 5943 次受控实验，并指出两条不同的泄露路径：一是应用层数据经 MQTT 未加密发送，二是内容标识在 DNS 解析层被暴露。这是一项聚焦美国市场的测量研究，而非全行业审计，因此结论描述的是受测的具体机型，而非市面上所有智能电视。

telegram · zaihuapd · 10月22日 09:50

**背景**: 自动内容识别（ACR）是一种通过采样音频或视频并与数据库比对，从而判断屏幕上正在播放什么内容（节目、广告或歌曲）的技术，原理上类似 Shazam 识别音乐。电视厂商利用 ACR 为用户观看习惯画像，用于广告投放和数据分析，而音频指纹——把一段声音压缩成简短的数字签名——正是其中的主要手段之一。MQTT 是一种为带宽受限的物联网设备设计的轻量级发布/订阅消息协议，它支持加密传输但并不强制，因此明文部署十分常见。这项研究提出的问题很简单：在设置里关掉 ACR，是否真能阻止内容识别与数据上报？

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_content_recognition">Automatic content recognition - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/MQTT_protocol">MQTT protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Audio_fingerprinting">Audio fingerprinting</a></li>

</ul>
</details>

**标签**: `#privacy`, `#smart-tv`, `#security-research`, `#data-tracking`, `#ACR`

---

<a id="item-7"></a>
## [米哈游联合清华开源 GameScaling 游戏操作模型](https://arxiv.org/abs/2610.28698v1) ⭐️ 7.0/10

米哈游崩坏 AI 团队联合清华大学等发布了 GameScaling，这是一套基于 Qwen3.5 的开源视觉语言模型系列，参数规模从 0.8B 到 27B，可预测未来 200 毫秒的键鼠操作以控制游戏。 该发布为游戏 AI 与具身智能体研究者提供了 Apache-2.0 许可的检查点和推理客户端，降低了复现和基于大规模动作预测模型进行二次开发的门槛，无需从零训练。 配套研究覆盖 120 组训练配置，发现数据越多同源表现越好，而更高的数据多样性有助于迁移到相近游戏，但对差异很大的游戏世界提升有限；本次开源包含八个检查点和推理客户端，但不含训练代码，因此完全复现仍受限制。

telegram · zaihuapd · 10月22日 11:32

**背景**: 视觉语言模型（VLM）能够联合处理图像和文本，在游戏 AI 中可把屏幕画面与指令映射为控制信号。GameScaling 将这一思路用于键鼠输入：它在 Qwen3.5 这一原生多模态模型系列上继续预训练，使模型一次输出覆盖 200 毫秒的短动作片段，而不是单个瞬时指令。缩放定律（scaling law）是描述模型性能如何随模型规模、数据量和计算量变化的经验规律，120 组配置的研究则检验了这些权衡在游戏动作预测中的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.5">Qwen3.5: Towards Native Multimodal Agents</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>

</ul>
</details>

**标签**: `#game AI`, `#vision-language models`, `#open-source`, `#scaling laws`, `#agents`

---

<a id="item-8"></a>
## [甲骨文就 JSSE 高危漏洞发布 Java SE 安全警报](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html) ⭐️ 7.0/10

甲骨文发布安全警报，披露 Java SE 的 JSSE 组件中存在编号为 CVE-2026-91403 的严重漏洞，CVSS 评分高达 9.1 分，攻击者可未经身份验证通过网络远程利用。该漏洞影响 Java SE 8u511、11.0.33、17.0.21、21.0.13、25.0.5、27.0.1 以及多个 GraalVM 版本，甲骨文已同步推出修复补丁并呼吁用户升级至受支持版本。 由于 JSSE 是 Java 运行时中 TLS/SSL 加密通信的基础组件，这里出现可远程、免认证利用的漏洞，会使大量 Java 服务器、中间件和企业应用面临风险。从 8u511 一直到 27.0.1 以及 GraalVM 的广泛受影响版本范围，意味着几乎所有运行 Java 基础设施的组织——包括大量仍在使用长期维护 LTS 版本的用户——都需要尽快评估并打补丁。 甲骨文指出该漏洞可能严重破坏数据的机密性与完整性，目前各受影响版本线的补丁均已提供，因此主要风险点在于未升级的部署仍将持续暴露。与大多数甲骨文 Java 安全公告一样，此次警报初期并未给出利用细节或概念验证代码，防御方只能依据 CVSS 评分和厂商指引，而无法依赖已知攻击特征。

telegram · zaihuapd · 10月22日 12:30

**背景**: JSSE（Java Secure Socket Extension，Java 安全套接字扩展）是实现 SSL 与 TLS 的 Java API 及内置 SunJSSE 提供者，让 Java 应用能够建立加密的网络连接。CVSS 是一套开放、厂商中立的漏洞严重性评分框架，依据攻击途径、复杂度、所需权限和影响等指标在 0.0 至 10.0 之间打分；9.1 分属于严重级别，在这里反映的是可远程、免认证利用。GraalVM 是 Oracle Labs 推出的高性能 JDK 发行版，额外提供 JIT 编译器、提前编译的 Native Image 以及多语言运行时支持，但它与 Java SE 共享大量相同代码，因此也被列入受影响产品清单。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Java_Secure_Socket_Extension">Java Secure Socket Extension - Wikipedia</a></li>
<li><a href="https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html">Java Secure Socket Extension ( JSSE ) Reference Guide</a></li>
<li><a href="https://nvd.nist.gov/vuln-metrics/cvss">NVD - Vulnerability Metrics Common Vulnerability Scoring System SIG - FIRST CVSS v4.0 Specification Document - FIRST NVD CVSS v3 Calculator CVSS Scores Explained: The Number Measures Severity, Not Risk CVSS Calculator — v2, v3.1 &amp; v4.0 Vulnerability Scoring</a></li>
<li><a href="https://en.wikipedia.org/wiki/GraalVM">GraalVM</a></li>

</ul>
</details>

**标签**: `#Java`, `#security-vulnerability`, `#CVE`, `#Oracle`, `#patching`

---

<a id="item-9"></a>
## [小鹏 IRON 机器人升级：每 0.2 秒重新推理一次做出反馈](https://www.ithome.com/1/016/667.htm) ⭐️ 6.0/10

小鹏汽车宣布，第二代 VLA（视觉-语言-动作）大模型已端侧落地到其人形机器人 IRON 上，使其每 0.2 秒就根据眼前的实时画面重新推理一次，并预测未来 6 秒内的动作变化。这使 IRON 在握手、击掌等互动中能够临场应变，例如对方手掌突然握成拳，或改变击掌的位置。 在本地以 0.2 秒的节奏反复重规划一个具身大模型，意味着机器人开始摆脱预编排动作、转向对人做出实时反应，而小鹏还给出了明确的商业化时间表：2026 年底量产、2027 年上半年开始交付。如果这一计划兑现，小鹏将成为最早把通用人形机器人投放进门店和商场场景的车企之一。 根据小鹏此前披露的信息，IRON 搭载 3 颗图灵 AI 芯片，有效算力约 2250 TOPS，第二代 VLA 端侧模型参数量扩大了约 3.5 倍，并从 3D 空间理解升级为 4D 时空理解。0.2 秒重新推理与 6 秒动作预测这两项数据均来自小鹏官方，尚未经过第三方独立验证；首批落地场景是门店和商场，而非家庭或工厂。

telegram · zaihuapd · 10月22日 13:37

**背景**: VLA 模型是在视觉-语言模型（VLM）上接一个“动作头”得到的架构，输入是摄像头画面和语言指令，输出是电机动作，目前已成为具身智能的主流路线。所谓“端侧”推理，是指模型运行在机器人自带的芯片上而不是云端服务器，好处是消除了网络延迟、断网时也能工作，代价是对算力和模型压缩要求很高。推理延迟和预测时域是这一领域的两个关键指标：机器人反应有多快、能预见多远，直接决定了人机交互是自然还是僵硬。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pingce.ifeng.com/c/8w2pJ1GIb49">小 鹏 第 二 代 VLA 大 模 型 迎来升级：从3D空间理解走向4D时空理解_凤凰网</a></li>
<li><a href="https://post.smzdm.com/p/a4qdq707/">小 鹏 第 二 代 VLA 重 大 升级,记住前30...</a></li>
<li><a href="https://www.diandonghome.com/4018/">小 鹏 第 二 代 VLA 升级，让AI 第 一次读懂时间 | 电动车之家</a></li>

</ul>
</details>

**标签**: `#humanoid robotics`, `#embodied AI`, `#VLA models`, `#on-device inference`, `#XPeng`

---