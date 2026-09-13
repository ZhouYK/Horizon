---
layout: default
title: "Horizon Summary: 2026-09-13 (ZH)"
date: 2026-09-13 23:03:54 +0000
lang: zh
report: default
---

> 从 145 条内容中筛选出 6 条重要资讯。

---

1. [Homebrew 7.0.0 发布：带来官方原生 macOS 图形界面与更严格沙箱](#item-1) ⭐️ 9.0/10
2. [山姆·奥特曼确认 OpenAI 2026 年不会上市](#item-2) ⭐️ 7.0/10
3. [北京全域禁飞无人机，11 月 15 日起开放三种处置渠道](#item-3) ⭐️ 7.0/10
4. [CUDA 护城河：AMD 的 DeepSeek v4.1 镜像性能落后 NVIDIA 最多 42 倍](#item-4) ⭐️ 7.0/10
5. [麒麟 9050 Pro 评测称 3D 堆叠电路提升性能与能效](#item-5) ⭐️ 6.0/10
6. [iOS 27 被曝允许 Claude 等第三方模型接管 Siri](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Homebrew 7.0.0 发布：带来官方原生 macOS 图形界面与更严格沙箱](https://brew.sh/2026/09/13/homebrew-7.0.0/) ⭐️ 9.0/10

Homebrew 发布 7.0.0 版本，新增官方 macOS 原生图形界面，提升了安装与升级速度，并引入更严格的沙箱保护、内置漏洞检查与安全公告数据库。该版本同时停止支持 macOS 10.15 及更早版本，将 Intel Mac 调整为 Tier 3（不再提供新的预编译包），并把 Linux 沙箱从 Bubblewrap 改用 Landlock。 Homebrew 是 macOS 开发者事实上的标准包管理器，官方原生图形界面降低了不熟悉命令行的用户的使用门槛，而漏洞数据库与更严格的沙箱则提升了整个 brew 依赖链的软件供应链安全。平台支持策略的调整也标志着 Apple Silicon 迁移时代基本结束，Intel Mac 此后只能获得尽力而为的维护。 由于 Intel Mac 被降为 Tier 3，它们将不再获得新的预编译 bottle，用户可能不得不从源码自行编译，而 macOS 10.15 Catalina 及更早系统则完全不再受支持。Linux 沙箱改用 Landlock——这是 Linux 5.13 合入的内核级非特权访问控制模块，因此内核版本较旧用户可能需要升级内核才能获得此前 Bubblewrap 提供的同等沙箱保护。

telegram · zaihuapd · 9月13日 11:23

**背景**: Homebrew 是广泛使用的开源包管理器，用于在 macOS 和 Linux 上安装命令行工具与应用，它定义了正式的“支持层级”（Support Tiers）来说明自身在各平台上的可用程度。Bubblewrap 是一款轻量级非特权沙箱工具，以支撑 Flatpak 而闻名；Landlock 则是可叠加的 Linux 安全模块（LSM），让非特权进程也能限制自身的文件系统访问，作为额外的安全层。Intel Mac 被划入 Tier 3 意味着只能获得最低级别的自动化覆盖与社区支持，与完全维护的 Tier 1 平台形成鲜明对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.brew.sh/Support-Tiers">Homebrew Documentation: Support Tiers</a></li>
<li><a href="https://github.com/containers/bubblewrap">GitHub - containers/bubblewrap: Low-level unprivileged ...</a></li>
<li><a href="https://landlock.io/">Landlock : the Linux sandboxing mechanism</a></li>

</ul>
</details>

**标签**: `#Homebrew`, `#package-manager`, `#macOS`, `#release`, `#security`

---

<a id="item-2"></a>
## [山姆·奥特曼确认 OpenAI 2026 年不会上市](https://fortune.com/2026/09/12/sam-altman-openai-ipo-delay-ill-advised-moment-safety-concerns/) ⭐️ 7.0/10

山姆·奥特曼确认 OpenAI 不会在 2026 年上市，他表示鉴于当前的人工智能安全问题，此时推进 IPO 时机不当，公司将等到业务与社会环境准备好后再行动。他还表示 OpenAI 仍有大量安全与对齐工作要完成，并呼吁人工智能企业与政府加强合作。 这是来自全球最受关注的人工智能实验室掌舵人的公开表态，明确把一项重大企业里程碑与安全和对齐进展挂钩，传递出战略上的审慎而非急于上市的信号。它推迟了最受期待的科技公司上市之一，使投资者和持股员工缺乏清晰的流动性时间表，也可能影响其他 AI 公司对自身上市计划的表述方式。 奥特曼并未给出新的目标时间，强调这是“是否准备就绪”的问题，而非永久放弃上市，并明确把上市时机与完成安全和对齐工作、以及加强 AI 企业与政府合作联系在一起。该表态中没有披露任何财务数据、估值目标或未来上市的结构性细节。

telegram · zaihuapd · 9月13日 01:14

**背景**: AI 安全是一个跨学科领域，旨在防止人工智能系统引发事故、滥用或其他有害后果，其中包含“对齐”——即确保 AI 系统可靠地追求人类预期的目标、偏好或伦理原则。对齐领域知名的难题包括“奖励黑客”（模型以非预期方式优化代理目标），以及在一些先进大语言模型中观察到的策略性欺骗或追求权力等行为。该领域在 2023 年生成式 AI 热潮中受到广泛关注，当时研究人员和企业高管公开警告相关风险，美国和英国等政府也相继设立了自己的人工智能安全研究所。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#IPO`, `#AI safety`, `#Sam Altman`, `#industry news`

---

<a id="item-3"></a>
## [北京全域禁飞无人机，11 月 15 日起开放三种处置渠道](https://pc.bjd.com.cn/detail?id=s6aa5e790e4b039a8e2f101cd) ⭐️ 7.0/10

北京市十六届人大常委会第二十六次会议表决通过新修订的《北京市无人驾驶航空器管理规定》，自 2026 年 11 月 15 日起实施。规定明确北京全市行政区域为无人驾驶航空器管制空域，禁止飞行，同时禁止持有、存放无人驾驶航空器及其核心部件，禁止运输、携带相关设备及核心部件进入本市行政区域。为方便市民合规处置存量设备，本市开放现场回购、报废回收、寄递出京三种渠道并分类补贴：9 月 12 日至 10 月 31 日回购补贴为成交价的 30%、上限 3000 元/台，11 月 1 日至 14 日为 15%、上限 1500 元/台。 这是目前全球最严格的无人机管理规则之一：它不只是限制飞行，而是禁止持有、存放，甚至禁止将无人机及其核心部件运输、携带进入首都，直接影响无人机爱好者、商业运营者以及全球最大消费级无人机市场中的硬件厂商（大疆占据主导地位）。由于该规定是地方性法规，并依据国家《无人驾驶航空器飞行管理暂行条例》制定，它可能成为其他中国城市收紧空域管控的模板，也意味着监管思路开始把无人机硬件本身当作受管制物品来对待。 该规定的关键在于两个定义：一是“管制空域”，在此类空域内飞行须经空中交通管理机构批准；二是“核心部件”，通常涵盖飞控、电机、电调、螺旋桨、电池、GPS 模块以及摄像头/图传等，这意味着被禁止的不只是整机，拆散的零部件同样在管制范围内。补贴具有明确的时间窗口且逐级递减，从 9 月 12 日算起，机主大约只有两个月时间在 11 月 15 日新规生效前完成处置。

telegram · zaihuapd · 9月13日 02:07

**背景**: 中国于 2023 年出台的《无人驾驶航空器飞行管理暂行条例》建立了空域管理框架，将空域划分为“适飞空域”和“管制空域”，并按微型、轻型、小型无人机设定不同要求，例如轻型无人机无需操控员执照，而小型无人机则需要。北京此前已于 2026 年 3 月 27 日通过自己的《北京市无人驾驶航空器管理规定》，自 2026 年 5 月 1 日起实施；2026 年 9 月的修订进一步收紧，将全市划定为管制空域，并把禁令从“飞行”扩展到“持有、存放、运输”。新规与国家标准及《民用航空法》《反恐怖主义法》等上位法配套执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E5%B8%82%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6%E8%88%AA%E7%A9%BA%E5%99%A8%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A/67542534">北京市无人驾驶航空器管理规定_百度百科</a></li>
<li><a href="https://www.gov.cn/zhengce/content/202306/content_6888799.htm">无人驾驶航空器飞行管理暂行条例_航天、航空_中国政府网</a></li>
<li><a href="https://www.bjrd.gov.cn/zyfb/202603/t20260327_4568482.html">北京市无人驾驶航空器管理规定_重要发布_北京市人民代表大会常务委员...</a></li>

</ul>
</details>

**标签**: `#drones`, `#regulation`, `#China policy`, `#UAV`, `#airspace`

---

<a id="item-4"></a>
## [CUDA 护城河：AMD 的 DeepSeek v4.1 镜像性能落后 NVIDIA 最多 42 倍](https://x.com/SemiAnalysis_/status/2098618867035557984) ⭐️ 7.0/10

SemiAnalysis 报告称，在 CUDA 版 vLLM 已支持 DeepSeek v4.1 Flash 两天之后，AMD 才发布了自己的 DeepSeek v4.1 Flash 镜像；该镜像虽然开箱即用，但每美元性能比 NVIDIA H200 最多差 14.8 倍、比 B200/B300 最多差 42 倍。也就是说功能可用，但跑同一负载的经济性差距极大。 这是关于 CUDA 软件生态（而非单纯的芯片硬件）如何决定 LLM 推理真实成本的一个具体量化数据点，对做推理硬件选型和推理服务栈规划的人尤其重要。它说明在模型迭代极快的环境下，AMD 晚一步的适配仍可能转化为决定性的成本劣势，而 NVIDIA 凭借首日优化保持优势。 该差距以“每美元性能”而非纯吞吐量来衡量，因此同时包含了运行时效率与硬件价格因素，对比对象则是 NVIDIA Hopper 架构的 H200 与 Blackwell 架构的 B200/B300。该帖本身是对 SemiAnalysis X 推文的简短二手转发，未披露测试配置、批大小或精度设置，因此这些数字宜作为方向性参考，而非完全可复现的结论。

telegram · zaihuapd · 9月13日 05:55

**背景**: vLLM 是一个开源的大语言模型推理与服务框架，最初由加州大学伯克利分校 Sky Computing Lab 开发，核心是用于高效管理 KV 缓存的 PagedAttention，如今已成为快速部署开放权重模型的事实标准之一。CUDA 是 NVIDIA 专有的并行计算平台与编程模型，SemiAnalysis 提到其拥有约 600 万开发者的生态，这种长期积累的工具链优势使得 DeepSeek v4.1 Flash 这类新模型往往在第一天就针对 NVIDIA GPU 完成优化。AMD 对应的开源软件栈（ROCm）需要单独做算子与库的适配工作，这正是其同一模型镜像发布更晚的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek-V4.1-Flash">DeepSeek-V4.1-Flash</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_B200">Nvidia B200</a></li>

</ul>
</details>

**标签**: `#CUDA`, `#AMD`, `#LLM Inference`, `#vLLM`, `#Hardware Performance`

---

<a id="item-5"></a>
## [麒麟 9050 Pro 评测称 3D 堆叠电路提升性能与能效](https://www.bilibili.com/video/BV1HEYv6XETo) ⭐️ 6.0/10

据极客湾评测总结（经 B 站转发）称，华为麒麟 9050 Pro 采用微观电路 3D 堆叠设计，9 核 16 线程 CPU 在 2.75 GHz 同频下较前代功耗降低超过 30%，即便在 3.1 GHz 峰值频率下功耗也未明显增加。该评测还称马良 955 GPU 的 3DMark 成绩提升近 40%，NPU 实测 INT8 算力为 67.7 TOPS，搭载该芯片的 Mate XT 2 在三款重载手游中整体表现达到骁龙 8 Elite 级别。 如果这些数据成立，这将意味着华为海思在先进制程受限的情况下，转而在先进封装层面寻求突破，通过 3D 堆叠而非更小的工艺节点来提升能效，具有标志性意义。这也表明此前主要用于数据中心和高端封装的 3D 堆叠技术正在进入旗舰移动 SoC，可能改变整个移动芯片行业追求每瓦性能的路线。 报道中提到的设计是在移动 SoC 的微观电路层面实现 3D 堆叠，这与服务器和高端封装中常见的基于 TSV、chiplet 的堆叠方式相比并不常见。这些数据——同频功耗降低超 30%、GPU 提升约 40%、INT8 算力 67.7 TOPS——均来自一段简短的评测转发，未披露原始数据、测试方法或第三方验证。

telegram · zaihuapd · 9月13日 13:22

**背景**: 3D 堆叠（也称三维集成）是一种半导体制造技术，将多颗芯片垂直堆叠，并通过硅通孔（TSV）或铜-铜键合互连，使其作为单一器件工作，从而提升密度、带宽和功耗效率。华为旗下的芯片设计公司海思负责麒麟移动 SoC 系列以及自研的马良 GPU 和 NPU 模块，但受到出口管制限制，难以获得最先进的制造工艺。移动 SoC 的能效通常依靠转向更先进的制程节点来提升，因此改用 3D 堆叠是实现更高每瓦性能的另一条路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Three-dimensional_integrated_circuit">Three-dimensional integrated circuit - Wikipedia</a></li>
<li><a href="https://www.assured-systems.com/faq/understanding-3d-chip-stacking/">Understanding 3D Chip Stacking - Assured Systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/HiSilicon">HiSilicon - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Huawei Kirin`, `#semiconductor`, `#3D stacking`, `#mobile SoC`, `#hardware benchmarks`

---

<a id="item-6"></a>
## [iOS 27 被曝允许 Claude 等第三方模型接管 Siri](https://x.com/itspdfu/status/2099122424209916015) ⭐️ 6.0/10

X 上的一则爆料称，iOS 27 与 macOS &quot;Golden Gate&quot; 在苹果的 App Intents 框架内包含一个私有的 &quot;Model Delegation API&quot;，允许应用注册 Siri 拓展，从而用第三方模型替换 Siri 的 AI 后端。该帖以 Claude 为例，称其可出现在 Siri 的&quot;询问……&quot;菜单中并生成 CSV 文件，而设置提醒之类的系统操作会被交回给 Siri 执行；相关能力需要私有的 com.apple.developer.model-delegation 授权（entitlement）。 如果属实，这将是一次重要的平台转向：苹果历来把 Siri 的后端封闭起来，而开放委托通道实际上会让 Siri 变成架在 Claude 等竞品助手之上的路由层。这会影响第三方模型厂商、希望借 Siri 获得新分发渠道的开发者，以及可以自行选择由哪个大模型回答问题的用户——不过该说法仍是关于未发布软件的、未获证实的传言。 据称该接口是私有的，并由非公开的授权（entitlement）控制，这意味着它并非官方文档化的开发者功能，第三方模型厂商大概需要先申请才能使用。实现细节同样未经验证：爆料中没有给出构建版本号，没有任何文档，甚至连 macOS 代号 &quot;Golden Gate&quot; 本身也只是传言的一部分。

telegram · zaihuapd · 9月13日 13:48

**背景**: App Intents 是苹果自 iOS 16 起引入的框架，用于让应用的内容和操作能被 Apple Intelligence 以及 Siri、Spotlight、快捷指令和小组件等系统体验发现，其重要性在近几届 WWDC 上不断提升。Siri 是苹果横跨 iPhone、iPad、Mac、Apple Watch、AirPods、Apple TV、HomePod 和 Apple Vision Pro 的语音助手，长期以来都是封闭系统，早期的 SiriKit 只允许接入少数预设的服务类别，而不支持替换通用模型。这里的&quot;模型委托&quot;指的是由第三方模型处理用户请求，同时把系统级操作交回给 Siri；而 entitlement（授权）是苹果为受限能力向应用签发的许可凭证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/appintents">App Intents | Apple Developer Documentation</a></li>
<li><a href="https://www.ithinkdiff.com/claude-already-works-inside-siris-menu-in-macos-27/">Claude and GPT-5.6 Already Work Inside Siri &#x27;s Menu in macOS 27</a></li>
<li><a href="https://forums.macrumors.com/threads/apples-rumored-siri-extensions-quietly-shipped-in-macos-27-i-got-ask-claude-working.2486206/">Apple ’s rumored Siri Extensions quietly shipped... | MacRumors Forums</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Siri`, `#LLM Integration`, `#iOS`, `#Rumors`

---