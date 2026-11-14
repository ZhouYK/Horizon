---
layout: default
title: "Horizon Summary: 2026-11-14 (ZH)"
date: 2026-11-14 23:03:16 +0000
lang: zh
report: default
---

> 从 143 条内容中筛选出 8 条重要资讯。

---

1. [星舰成功入轨并部署 26 颗 Starlink V3 卫星，助推器返场爆炸](#item-1) ⭐️ 7.0/10
2. [Cloudflare 开源 Kitesurf：专为 AI 代理打造的无状态浏览器](#item-2) ⭐️ 7.0/10
3. [Anthropic IPO 据称因 ITAR 出口管制拒绝中国内地与香港投资者下单](#item-3) ⭐️ 7.0/10
4. [意大利因未经同意读取相册对 Meta 罚款 8.05 亿欧元](#item-4) ⭐️ 7.0/10
5. [OpenAI 解散独立机器人团队，改由通用模型直接驱动机器人](#item-5) ⭐️ 6.0/10
6. [全球最大无人货机 W5000 完成技术验证试飞](#item-6) ⭐️ 6.0/10
7. [新西兰仓库工人抗议 AI 追踪如厕时间](#item-7) ⭐️ 6.0/10
8. [谷歌 AI Studio 设计师借助 Gemini 与 WindowsiOS 让 Windows 11 跑上折叠 iPhone](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [星舰成功入轨并部署 26 颗 Starlink V3 卫星，助推器返场爆炸](https://www.spacex.com/launches/starship-flight-15) ⭐️ 7.0/10

SpaceX 于 11 月 13 日从得克萨斯州发射星舰第 15 次试飞，飞船成功入轨并部署了全部 26 颗 Starlink V3 卫星，其中 3 颗携带摄像头用于检查隔热瓦状态。原计划的“双塔捕”未能实现：超重型助推器因技术问题中止返场，改为在墨西哥湾受控溅落后爆炸，SpaceX 未公布具体原因。 这是星舰首次入轨并一次性部署整批可用的 Starlink V3 卫星，标志着它从携带测试配重转向承担真实商业载荷的关键一步。但助推器的失败表明两级快速完全复用仍不可靠，这一结果将影响 SpaceX 用星舰替代猎鹰 9 号发射星链星座的节奏。 飞船原计划在轨飞行约 22 小时、绕地球约 14 圈，次日返回 Starbase 尝试人类首次轨道级飞船塔捕，即垂直下降到发射塔旁由机械臂夹住承接点，而非落地或落海。助推器中止返场说明其返场点火或末端制导未满足条件，这次损失对助推器复用节奏是一次挫折，尽管飞船任务仍照常进行。

telegram · zaihuapd · 11月14日 03:03

**背景**: 星舰是 SpaceX 研制的两级完全可复用超重型火箭，由超重型助推器和星舰飞船上级组成，目标是向近地轨道、月球乃至火星运送大质量载荷和人员。SpaceX 用安装在发射塔上的巨型机械臂“Mechazilla”（由 mechanical 与 Godzilla 组合而成）回收助推器，该技术在 2024 年 10 月的第五次试飞中首次成功演示。而捕获飞船本身要难得多，因为它需从轨道速度再入并承受极端高温。Starlink V3 是 SpaceX 的下一代卫星设计，在容量、数据密度和发电功率上有大幅提升，每颗配备六台 400 Gbps 太空激光器，可在网状网络中转发流量，因此高度依赖星舰远大于猎鹰 9 号的运载能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://starlink.com/updates/starlink-version-3-satellites">Starlink Version 3 Satellites</a></li>
<li><a href="https://thespacebucket.com/how-exactly-does-starships-catching-mechanism-work/">How Exactly Does Starship’s Catching Mechanism Work?</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-chopsticks-catch-starship-upper-stage-flight-14">Watch SpaceX will attempt its 1st-ever &#x27;chopsticks&#x27; Starship ...</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#spaceflight`, `#Starlink`, `#reusable launch`

---

<a id="item-2"></a>
## [Cloudflare 开源 Kitesurf：专为 AI 代理打造的无状态浏览器](https://www.phoronix.com/news/Cloudflare-Kitesurf-Open-Source) ⭐️ 7.0/10

Cloudflare 以 Apache 2.0 协议开源了 Kitesurf，这是一个完全构建在 Cloudflare Workers 之上、专为 AI 代理设计的无状态浏览器。它无需浏览器容器即可解析 HTML、处理 CSS 并执行 JavaScript，相关代码已发布在 GitHub 上。 需要读取或操作真实网页的 AI 代理通常必须启动无头 Chromium 实例，这类方案 CPU 和内存开销高昂、扩展缓慢。Kitesurf 提供了一个轻量得多的替代方案，可在 Cloudflare 全球边缘网络上按需扩展，有望大幅降低大规模运行浏览器型代理时的成本与延迟。 Cloudflare 将 Kitesurf 定位为在截图、HTML 提取等常见代理任务上比 Chromium 轻量得多，可支持更高的并发会话数并更好地应对突发负载。值得注意的是，它依赖 Cloudflare Dynamic Workers 为每个页面创建隔离的 Worker，Cloudflare 也明确警告不要在缺乏前置身份认证的情况下部署它。

telegram · zaihuapd · 11月14日 09:33

**背景**: Cloudflare Workers 是一个无服务器平台，可在 Cloudflare 覆盖 335 多个城市的网络上运行代码，能从零自动扩展，且只按 CPU 执行时间计费而非空闲等待时间。以往需要浏览网页的 AI 代理通常依赖无头 Chromium 之类的浏览器引擎，而这类引擎必须为每个会话维护完整的浏览器进程、页面状态和渲染管线，是主要的资源瓶颈。所谓“无状态”浏览器是指每个请求独立处理、不保留持久会话，这正好契合 AI 代理抓取页面时高并发、即用即弃的特点，也天然适配 Workers 的执行模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cloudflare/kitesurf">GitHub - cloudflare / kitesurf : Kitesurf is an experimental browser...</a></li>
<li><a href="https://developers.cloudflare.com/browser-run/kitesurf/">Kitesurf · Cloudflare Browser Run docs</a></li>
<li><a href="https://www.cloudflare.com/products/workers/">Cloudflare Workers - Global Serverless Functions Platform</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#ai-agents`, `#serverless`, `#browser`, `#open-source`

---

<a id="item-3"></a>
## [Anthropic IPO 据称因 ITAR 出口管制拒绝中国内地与香港投资者下单](https://m.economictimes.com/markets/us-stocks/news/anthropic-ipo-share-orders-from-china-are-said-to-be-rebuffed/articleshow/135809948.cms) ⭐️ 7.0/10

据 Economic Times 及 Telegram 科技频道流传的消息，Anthropic 的 IPO 拒绝接受来自中国内地和香港投资者的认购订单，该限制据称与国际武器贸易条例（ITAR）出口管制有关。同一消息还称发行定价日为 11 月 18 日、次日以代码 ANT 上市，拟以 1.4 万亿美元估值募资至多 904 亿美元，由高盛与摩根士丹利牵头承销。 若消息属实，这将是领先 AI 实验室在上市环节以国家安全为由明确排除中国资本的先例之一，为前沿 AI 公司如何构建股东基础立下样板。它还会把中国投资者的需求挤向离岸载体，进一步加深中美两国在 AI 领域资本市场的分割。 该消息称认购需求约为可售股份的 6 倍，部分被拒资金转而通过英属维尔京群岛信托、SPV 和掉期结构间接获得敞口。值得注意的是，1.4 万亿美元估值和 904 亿美元募资这类异常巨大的数字来自一条 Telegram 来源的简短消息而非正式招股文件，在 SEC 或公司官方披露证实前应视为未经核实。

telegram · zaihuapd · 11月14日 10:18

**背景**: ITAR 是美国执行《武器出口管制法》的法规，管制《美国军品清单》所列防务物项与服务的出口和转移，限制向外国人共享受控技术数据，其中也包括通过投资或股权结构进行的接触。SPV（特殊目的载体）是为特定、狭窄目的设立的法律实体，此处指代无法直接认购的投资者持有股份或经济敞口的工具。英属维尔京群岛信托和总收益互换等离岸结构常被用来让受限投资者在不直接拥有标的股份的情况下获得间接经济敞口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pmddtc.state.gov/ddtc_public?id=ddtc_public_portal_itar_landing">Understand The ITAR - DDTC Public Portal</a></li>
<li><a href="https://en.wikipedia.org/wiki/Special-purpose_entity">Special - purpose entity - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Offshore_investment">Offshore investment - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#export controls`, `#AI industry`, `#China/Hong Kong`

---

<a id="item-4"></a>
## [意大利因未经同意读取相册对 Meta 罚款 8.05 亿欧元](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10321080) ⭐️ 7.0/10

意大利隐私监管机构 Garante Privacy 对 Meta 处以 8.05 亿欧元罚款，认定 Facebook 安卓应用的相册推荐功能默认开启，在未取得具体同意的情况下收集了约 2000 万意大利用户的照片、视频及元数据。监管机构要求 Meta 在 60 天内将该功能改为默认关闭并单独征得用户明确同意，否则不得对未有效授权的用户启用该功能。 这是针对大型平台开出的金额最高的隐私罚单之一，而且针对的不是数据泄露事件，而是同意的设计方式——默认开关与含糊的授权提示，而这恰恰是多数移动用户在现实中面对隐私选择的方式。这表明欧洲监管机构愿意对界面设计决策施加巨额罚款和具有约束力的整改期限，也可能促使其他应用重新考虑默认开启相册访问权限的做法。 涉事功能是 2023 年上线的相册推荐功能，监管机构认为它把相册访问权限捆绑在一个笼统的授权提示中，而没有就该用途单独征得具体同意。除罚款外还附带明确的合规命令：Meta 必须在 60 天内将默认设置改为关闭并增加单独的同意步骤，且不得对未有效授权的用户启用该功能——这意味着真正的成本不仅在于 8.05 亿欧元罚金，也在于重新设计整个同意流程。

telegram · zaihuapd · 11月14日 14:37

**背景**: 欧盟《通用数据保护条例》（GDPR）要求用户的同意必须是具体的、知情的和自愿给出的，这通常意味着不能把宽泛的数据访问权限藏在笼统的授权提示之后，也不能替用户预先勾选。Garante Privacy 是意大利独立的数据保护监管机构，也是欧洲较为活跃的 GDPR 执法者之一。在安卓系统上，照片和媒体等访问权限是在操作系统层面授予的，而应用如何表述这一请求、以及相关功能是否默认开启，正是监管机构眼中同意问题的来源。

**标签**: `#privacy`, `#Meta`, `#GDPR`, `#data-protection`, `#regulation`

---

<a id="item-5"></a>
## [OpenAI 解散独立机器人团队，改由通用模型直接驱动机器人](https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/) ⭐️ 6.0/10

据 Fortune 报道，OpenAI 已解散其独立的机器人团队，并将相关研究人员重新分配到更通用的研究团队中。公司表示机器人仍是其长期愿景的核心，但 GPT-6 Astra 等通用前沿模型如今已能直接操控机器人执行任务，因此不再需要专门的机器人团队。 如果消息属实，这标志着 OpenAI 在具身智能路线上的重要转向：不再构建机器人专用的技术栈，而是押注于通用模型的规模扩展足以驱动硬件。这一思路对整个机器人与基础模型生态都有影响，因为这意味着人形机器人厂商可能越来越依赖通用模型提供方，而非自建的机器人 AI 团队。 OpenAI 的机器人业务此前已多次调整：最早的机器人团队于 2020 年解散，2024 年重建并与 Figure AI 建立合作，但该合作已于 2025 年 2 月终止。据报道，公司目前仍在自研人形机器人，CEO 的目标是在 2027 年进行首次公开展示。

telegram · zaihuapd · 11月14日 04:00

**背景**: OpenAI 的 GPT-6 系列中包括旗舰型号 Astra，官方将其定位为面向长周期智能体任务（例如操作计算机与浏览器）的模型，而这类通用控制能力在原理上有望延伸到机器人的执行机构上。与此同时，Figure AI 等人形机器人初创公司之所以受到关注，很大程度上得益于与模型厂商的深度合作，Figure 的机器人一度被广泛称为“行走的 ChatGPT”。在继续自研人形机器人的同时解散内部机器人团队，意味着 OpenAI 把机器人的智能问题视为模型问题，而非硬件或控制层面的专门问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/zh-CN/openai/gpt-6-astra">GPT - 6 Astra - API 定价与基准测试 | OpenRouter</a></li>
<li><a href="https://awtmt.com/articles/3722958">不到半年， Figure AI 发布第二代 人 形 机 器 人 ，称为“地表最先进AI硬件”</a></li>
<li><a href="https://wallstreetcn.com/articles/3710427">成立仅2年，做出能和 人 类对话的 人 形 机 器 人 ， Figure AI ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#机器人`, `#通用模型`, `#组织调整`, `#AI行业动态`

---

<a id="item-6"></a>
## [全球最大无人货机 W5000 完成技术验证试飞](https://www.ithome.com/1/027/068.htm) ⭐️ 6.0/10

白鲸航线于 11 月 14 日宣布，W5000 大型无人货运飞机在内蒙古鄂托克前旗完成技术验证试飞，爬升、平飞、转弯、下降、进近着陆等全部科目均按计划完成。企业称该机为全球业载最大的无人货机，并预计在 2027 年上半年完成适航取证。 如果适航取证按计划推进，5 吨业载、2600 公里航程将让运营方在没有机上飞行员的情况下，把一整辆中型卡车的货物点对点直送，在公路货运与传统航空货运之间开辟新的运力层级。其“全球业载最大无人货机”的定位，也让中国厂商在这一仍以试验为主的细分领域处于前列。 W5000 最大起飞重量 10.8 吨、最大业载 5 吨、设计航程 2600 公里，采用涡桨动力与“自主驾驶 + 地面监控”模式，按设计一个机组可同时监控 6 至 7 架飞机。此次完成的只是技术验证试飞而非型号取证，2027 年完成适航取证的目标仍有待验证。

telegram · zaihuapd · 11月14日 05:00

**背景**: 大型货运无人机希望在有航线需求但机组成本高昂的场景中替代或补充有人货机，并能在设施相对简单的机场起降。在中国，民用无人机进入商业运营前通常需要走完型号合格证（TC）、生产许可证（PC）、单机适航证（AC）以及运营人所需的运营合格证（OC）等一系列审批，依据包括 CCAR-92 部、CCAR-21-R5 等规章。涡桨动力在中速中空巡航时燃油效率较好，适合货运；而“地面监控”模式意味着飞机自主飞行，由地面机组在控制站同时看管多架飞机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dronetest.cn/caac-wurenji-shiheng-renzheng-liucheng.html">2026年中国无人机CAAC适航认证全流程与要求详解</a></li>
<li><a href="https://www.sgpjbg.com/labelsyh/zhongxingwurenjishihangquzhengluxiantu/1/6621014.html">中型无人机适航取证路线图：TC/PC/AC/OC四证全流程指引2026｜LAEC</a></li>

</ul>
</details>

**标签**: `#unmanned aircraft`, `#autonomous flight`, `#cargo logistics`, `#aviation`, `#China tech`

---

<a id="item-7"></a>
## [新西兰仓库工人抗议 AI 追踪如厕时间](https://www.independent.co.uk/news/world/australasia/new-zealand-workers-ai-bathroom-breaks-b3084317.html) ⭐️ 6.0/10

新西兰最大零售商 The Warehouse 集团奥克兰和基督城配送中心的 300 多名工人本周举行抗议，工会 Workers First 指控员工的如厕时间受到追踪，甚至有员工被迫在配送过道排便。公司首席人力官否认这一说法，称所使用的扫描技术并非 AI、与如厕无关，也没有因库存无人机而裁撤岗位。 这场纠纷把仓库自动化和算法化管理推向了公开的劳资冲突，凸显出生产率追踪系统可能与企业员工的基本尊严和隐私发生碰撞。随着全球零售商在配送中心内部署更多机器人和无人机，这类监控如何实施与披露将影响劳资关系，并很可能引来监管关注。 工会还指称公司引入「巨型机器人」进行拣货，并用 AI 无人机替代部分库存盘点团队；公司则表示无法保证未来岗位，但承诺会进行协商并对受影响员工再培训安置。值得注意的是，公司连该技术是否属于 AI 都予以否认，因此争议的核心事实在于这套扫描系统究竟在测量什么。

telegram · zaihuapd · 11月14日 06:15

**背景**: 仓库自动化通常包括货到人机器人（把货架运到拣货员面前）以及自主无人机或地面机器人，它们通过扫描货架上的条码来盘点库存，速度远快于人工盘点。除硬件之外，许多大型零售商还使用绩效追踪软件，记录任务、扫描频率以及离岗时间，这一做法因亚马逊的生产率指标而广为人知。由于这类系统会持续生成个人数据，它们引发了关于监控、工作节奏以及员工如何对自动化判定提出异议的疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.independent.co.uk/news/world/australasia/new-zealand-workers-ai-bathroom-breaks-b3084317.html">New Zealand workers say their bathroom breaks are tracked by AI</a></li>
<li><a href="https://emergent.sh/news/new-zealand-workers-defecate-aisles-ai-tracks">New Zealand Workers Defecate in Aisles as AI Tracks Breaks</a></li>
<li><a href="https://www.dronescan.co/">DroneScan | AI-Powered Drone Warehouse Stocktake &amp; Robotic ...</a></li>

</ul>
</details>

**标签**: `#AI surveillance`, `#workplace privacy`, `#labor rights`, `#automation`, `#New Zealand`

---

<a id="item-8"></a>
## [谷歌 AI Studio 设计师借助 Gemini 与 WindowsiOS 让 Windows 11 跑上折叠 iPhone](https://www.windowslatest.com/2026/11/14/windows-11-can-run-on-apples-foldable-iphone-and-googles-ai-boss-proved-it-using-gemini-years-after-microsoft-gave-up-on-windows-phones/) ⭐️ 6.0/10

谷歌 AI Studio 产品设计负责人 Ammaar Reshi 演示了完整的 Windows 11 24H2 在苹果折叠手机 iPhone Duo 上本地运行，并表示他用 Gemini 4 Carbon 辅助完成了开源项目 WindowsiOS 的开发。他还公开了实机视频，显示 ARM64 版 Windows 在未越狱的设备上启动，据称完全没有使用 Hypervisor.framework。 这说明基于 JIT 的翻译方案可以把桌面级操作系统搬到封闭的 iOS 硬件上，而这一领域此前一直被苹果的虚拟化限制挡住，微软也早已放弃手机业务。更值得注意的是，一位谷歌高管借助 Gemini 完成了这项工作，反映出 AI 助手正被用来攻克通常需要团队投入大量时间的底层系统难题。 Windows 镜像约 12 GB，部署需要一台 Apple Silicon Mac 以及开发者工具来侧载并启用 JIT；x86/x64 传统应用只能通过微软的 Prism 模拟层运行，因此兼容性和性能远达不到原生水平。由于没有硬件虚拟化，一切都依靠用户态 JIT 翻译执行，这种方式本身比较脆弱，并且强依赖于特定的 iOS 版本和设备标识（如 iPhone19,4、A20 Pro、iOS 27 TXM）。

telegram · zaihuapd · 11月14日 06:52

**背景**: Windows on Arm 可以原生运行在 Arm 芯片上，但较旧的 x86/x64 软件需要翻译层，微软随 Windows 11 24H2 推出的 Prism 就扮演着类似苹果 Rosetta 2 在 Apple Silicon Mac 上的角色。在 iOS 上，应用通常无法使用即时编译（JIT）或硬件虚拟化，这也是长期以来在未越狱 iPhone 上运行完整桌面系统被认为不切实际的原因。WindowsiOS 的绕行方式是借助开发者签名获得的 JIT 权限，以接近原生的速度翻译 ARM64 代码，而不是模拟整台机器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ammaarreshi/WindowsiOS">GitHub - ammaarreshi/WindowsiOS: Native Windows 11 ARM64 on ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-x86-emulation">How emulation works on Arm | Microsoft Learn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compatibility_layer">Compatibility layer - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Windows 11`, `#iPhone`, `#emulation`, `#Gemini`, `#open-source`

---