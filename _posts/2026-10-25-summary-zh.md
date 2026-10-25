---
layout: default
title: "Horizon Summary: 2026-10-25 (ZH)"
date: 2026-10-25 23:03:02 +0000
lang: zh
report: default
---

> 从 144 条内容中筛选出 6 条重要资讯。

---

1. [Brotli 高危漏洞 CVE-2026-111497 波及 Python 与 Node.js 的 HTTP 组件](#item-1) ⭐️ 8.0/10
2. [GPU 租赁价格全面上涨，连五年前的老款 A100 也没能例外](#item-2) ⭐️ 7.0/10
3. [搜狗输入法 OPPO 定制版被 Play 保护机制标记为风险应用](#item-3) ⭐️ 6.0/10
4. [特斯拉自研 AI 地图将随 FSD v15 推送](#item-4) ⭐️ 6.0/10
5. [GEEKCON 上海站无人机攻防赛题引发厂商报警，赛事一度暂停](#item-5) ⭐️ 6.0/10
6. [苹果将于周三发布首款触屏 MacBook Pro](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Brotli 高危漏洞 CVE-2026-111497 波及 Python 与 Node.js 的 HTTP 组件](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 8.0/10

谷歌 Brotli 解码器存在堆缓冲区溢出漏洞 CVE-2026-111497，影响 1.0.3 至 1.2.0 版本，CVSS 4.0 评分高达 9.2。该漏洞最初以 Node2Shell 命名披露、后改称 HTTP2Shell，如今也波及 Python 的 HTTP 组件，修复版本为 Brotli 1.2.1、brotlicffi 1.2.1.0，以及 Node.js 22.23.4、24.22.1 和 26.12.1。 Brotli 是浏览器普遍支持的标准 HTTP 压缩格式之一，因此其解码器中可远程触发的内存破坏漏洞，会影响任何需要解压攻击者可控请求体的服务端，包括 Node.js 与 Python 的 Web 技术栈。由于利用该漏洞无需认证，且可能导致敏感数据泄露甚至任意代码执行，使用受影响版本的团队应尽快完成升级。 漏洞根因是 c/dec/decode.c 中的缓冲区溢出，被归类为越界写入（CWE-787），远程未认证攻击者可借此破坏相邻的解码器状态内存、泄露内存内容、导致进程崩溃，甚至通过特制的 Brotli 压缩流执行任意代码。Python 用户需升级至 Brotli 1.2.1 或 brotlicffi 1.2.1.0，Node.js 用户则需升级到 22.23.4、24.22.1 或 26.12.1；OpenAI 表示于今年 2 月发现了该问题。

telegram · zaihuapd · 10月25日 02:42

**背景**: Brotli 是谷歌开发的开源无损压缩算法，作为 &quot;br&quot; HTTP 内容编码与 gzip 并列被广泛使用，也常用于压缩网页字体、JSON 等资源。任何接收不可信压缩数据的程序都必须对其进行解码，这就使解码器漏洞成为可被远程触及的攻击面。brotlicffi 是参考 Brotli 库的 Python CFFI 绑定，API 与标准 Brotli Python C 绑定完全兼容，常用于 PyPy 等非 CPython 运行时。CVSS 4.0 是通用漏洞评分系统的最新版本，9.0 及以上分数代表“严重”级别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/cve-2026-111497">NVD-CVE-2026-111497</a></li>
<li><a href="https://www.tenable.com/cve/CVE-2026-111497">CVE-2026-111497 | Tenable®</a></li>
<li><a href="https://pypi.org/project/brotlicffi/">Python CFFI bindings to the Brotli library</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Brotli`, `#Python`, `#Node.js`

---

<a id="item-2"></a>
## [GPU 租赁价格全面上涨，连五年前的老款 A100 也没能例外](https://x.com/a16z/status/2113741008550990191) ⭐️ 7.0/10

a16z 跟踪的一项 GPU 租价指数（以 2026 年 1 月 1 日为 100）显示，截至 10 月 19 日租价大幅走高：H200 升至约 265，B200 约 225，RTX PRO 6000 工作站版约 165，H100 SXM 约 137，A100 SXM4 约 102。折算下来累计涨幅约为 H200 +160%、B200 +120%、RTX PRO 6000 +65%、H100 +35%，而 2020 年发布的 A100 仅略高于年初基准。 从最新旗舰到五年前的 A100，各代数据中心 GPU 租价同步上涨（A100 虽仅微涨但方向为正），说明算力紧张是普遍性的，而不只是对最新旗舰芯片的需求旺盛。这对 AI 训练与推理的预算制定、容量规划，以及判断新一代加速器出货后旧硬件是否会释放出来，都有直接影响。 这些数字是归一化价格指数的七日移动平均，而非绝对的每 GPU·小时美元价格，因此反映的是方向和相对幅度，而不是买家实际支付的时租价格。A100 SXM4 约 +2% 的涨幅远小于旗舰芯片，说明上一代产能正在以慢得多的价格增速承接溢出需求。

telegram · zaihuapd · 10月25日 06:39

**背景**: 指数中的芯片横跨 NVIDIA 数代产品：A100（Ampere 架构，2020 年）与 H100/H200（Hopper 架构）采用 SXM 板卡形态，这是一种高带宽插槽方案，用于八卡 HGX/DGX 系统，所有 GPU 通过 NVLink 互联，从而像一颗大芯片一样协同工作；B200 则是较新的 Blackwell 代旗舰。指数中的“SXM4”“SXM”后缀仅表示这种板卡形态，而非 PCIe 插卡版本，后者通常内存带宽和功耗余量更低。GPU 租价指数是对云端 GPU 费率的基准化度量，通常基于市场挂牌或实际成交数据（如 Ornn Compute Price Index）构建，被用作衡量 AI 算力供给松紧的代理指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vast.ai/article/nvidia-h200-vs-b200-comparing-datacenter-grade-accelerators">NVIDIA H200 vs. B200: Comparing Datacenter-Grade Accelerators</a></li>
<li><a href="https://en.wikipedia.org/wiki/SXM_%28socket%29">SXM (socket) - Wikipedia</a></li>
<li><a href="https://data.ornn.com/markets">GPU Market Prices : Compute Price Index (OCPI) | Ornn Data</a></li>

</ul>
</details>

**标签**: `#gpu-pricing`, `#ai-infrastructure`, `#compute-market`, `#hardware`, `#cloud-costs`

---

<a id="item-3"></a>
## [搜狗输入法 OPPO 定制版被 Play 保护机制标记为风险应用](https://telegram.me/zaihuapd/44689) ⭐️ 6.0/10

近日有 ColorOS 用户反馈，设备上的搜狗输入法定制版被 Google Play 保护机制判定为有害应用，系统安全组件自动移除了该应用的敏感权限、将其停用，并弹出提示警告其存在窥探短信、照片、录音和通话记录等隐私数据的风险。OPPO 客服回应称问题正在积极解决中，用户可先关闭 Play 保护机制。 输入法几乎接触到用户输入的一切内容，因此一款装机量巨大的键盘被标记为有害应用，同时牵涉隐私风险和用户对预装软件的信任问题。更值得注意的是官方建议用户关闭 Play 保护机制，这等于是让用户为了继续使用一个被系统判定为危险的应用，而放弃 Android 上部署最广泛的恶意软件防护。 Play 保护机制每天在设备本地扫描已安装应用，可以重置应用权限、向用户发出警告，或拦截和移除有害应用；本次它并未直接卸载该应用，而是移除了敏感权限并将其停用。该报道仅涉及 OPPO/ColorOS 定制版本的搜狗输入法，且未提供任何技术分析说明被标记的原因，因此无法判断是广告或数据采集 SDK 的行为、误报，还是其他因素导致。

telegram · zaihuapd · 10月25日 09:59

**背景**: Google Play 保护机制是 Android 内置的恶意软件防护功能，依托谷歌的机器学习技术每天在设备上扫描应用，并对判定为有害的应用发出警告或将其停用，谷歌称其为全球部署最广泛的移动威胁防护服务。ColorOS 是 OPPO 基于 Android 深度定制的系统界面，内置自家系统应用与服务，并常常预装由厂商定制的第三方本地化应用（如输入法）。这类定制版本通常不通过 Google Play 分发，因此不经过应用商店的审核流程，但设备端的 Play 保护机制仍会对其进行扫描。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.google.com/android/play-protect?hl=zh-cn">Play Protect | Google for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/ColorOS">ColorOS - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mobile security`, `#privacy`, `#Android`, `#Play Protect`, `#Sogou`

---

<a id="item-4"></a>
## [特斯拉自研 AI 地图将随 FSD v15 推送](https://www.digitaltoday.co.kr/en/view/118497/tesla-to-build-in-house-maps-and-navigation-to-address-fsd-limits) ⭐️ 6.0/10

特斯拉正在开发一套基于 AI 的自研地图与导航系统，数据来源为车队采集的道路信息，计划先在 FSD v15 的行程出发与到达阶段上线，随后数月内逐步覆盖导航、泊车等环节。该系统旨在解决股东此前指出的限速识别、泊车和路线选择问题，并支持语音指令与个性化路线偏好。 这是特斯拉的一次明显立场转向——它此前长期主张自动驾驶不应依赖地图，而将这一转变绑定到具体的 FSD v15 版本上，使战略调整有了明确时间表。如果基于车队数据的 AI 地图按预期奏效，它可能成为依赖第三方高精地图的竞争对手难以复制的数据飞轮优势。 该功能分阶段推进：FSD v15 初期仅在行程出发与目的地处理环节使用新地图，导航与泊车的完整覆盖要等到后续几个月，且数据来自量产车队采集而非专业测绘车。该报道只是一则简短新闻摘要，缺少技术细节，因此外界尚不清楚地图采用何种表示方式、如何验证，以及哪些硬件代际能够支持该功能。

telegram · zaihuapd · 10月25日 10:57

**背景**: 特斯拉在完全自动驾驶（FSD）上长期坚持“无图”路线，押注摄像头加神经网络可以在没有预建高精地图的情况下完成感知与规划；而高精地图是厘米级道路模型，许多中国和欧洲车企依赖它来实现车道级精度。特斯拉在这一路线上的优势在于车队规模：通过“影子模式”，车辆在人类驾驶时后台静默运行驾驶模型，并将模型预测与实际操作不一致的特定场景上传，形成持续的数据闭环。此次自研 AI 地图实际上是把两种思路结合起来，用车队数据生成类似地图的先验信息，而不是外包给地图供应商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unwire.hk/2026/07/21/tesla-fsd-v15-personalized-driving/fun-tech/">Tesla FSD v15 明年登場 參數規模擴大 10 倍 記低你駕駛習慣</a></li>
<li><a href="https://baike.baidu.com/item/%E5%BD%B1%E5%AD%90%E6%A8%A1%E5%BC%8F/67520502">影子模式_百度百科</a></li>
<li><a href="https://nev.ofweek.com/2024-01/ART-77015-8420-30623618.html">无 图 自 动 驾 驶 ， 高 精 地 图 真的不需要了吗？ - OFweek新能源汽车网</a></li>

</ul>
</details>

**标签**: `#autonomous-driving`, `#tesla`, `#fsd`, `#ai-maps`, `#navigation`

---

<a id="item-5"></a>
## [GEEKCON 上海站无人机攻防赛题引发厂商报警，赛事一度暂停](https://tech.ifeng.com/c/8xSZe56UAz6) ⭐️ 6.0/10

10 月 24 日晚闭幕的 GEEKCON 上海站上，据称一项无人机攻防赛题触发了某头部无人机厂商报警，相关人员被带走，赛事一度暂停。该赛题要求选手突破 GPS 禁飞限制，并夺取无人机的完整控制权。 这一事件凸显了中国白帽漏洞研究与厂商、法律回应之间脆弱的边界：一项赛事演示可能被重新定义为“攻击能力”，而非安全研究成果。若此类赛题开始招致警方介入，可能会打击无人机安全研究的积极性，并促使研究者放弃协同披露、转向沉默。 该说法尚未得到证实：它来自一段简短的、类 Telegram 风格的消息，GEEKCON 主办方、未具名的厂商以及警方均未确认，也没有披露涉及哪款无人机型号或何种漏洞的技术细节。GEEKCON 每年 10 月 24 日举办，长期赞助方包括华为、腾讯安全和蚂蚁等。

telegram · zaihuapd · 10月25日 13:29

**背景**: 消费级无人机通过写入固件和配套 App 的 GPS 地理围栏来执行禁飞限制，厂商通常只允许机主通过官方的自助解锁或授权流程解除限制，因此要求选手突破这些限制的赛题，本质上是在让研究者攻破一项安全管控措施。协同漏洞披露（CVD，又称负责任披露）是业界惯例：研究者先私下向厂商报告漏洞，留出修补时间后再公开细节。此处争议的焦点在于：一场现场赛事演示，究竟属于该模式下的正当研究，还是公开演示了一种攻击能力——在后一种理解下，厂商与监管方可能会将其视为威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure</a></li>
<li><a href="https://dronesgator.com/how-to-unlock-dji-geofencing">How to Unlock DJI Geofencing (2026 FlySafe Guide)</a></li>
<li><a href="https://www.robinradar.com/resources/10-counter-drone-technologies-to-detect-and-stop-drones-today">10 Types of Counter- drone Technology to Detect and Stop Drones ...</a></li>

</ul>
</details>

**标签**: `#security-research`, `#responsible-disclosure`, `#drone-security`, `#china-tech`, `#conference-news`

---

<a id="item-6"></a>
## [苹果将于周三发布首款触屏 MacBook Pro](https://www.bloomberg.com/news/newsletters/2026-10-25/apple-to-unveil-touch-screen-macbook-pro-executive-promotions-in-box-checker) ⭐️ 6.0/10

据 Bloomberg 报道，苹果计划于本周三发布首款触屏 MacBook Pro，这是 Mac 首次支持触摸操作并配备 OLED 屏幕，同时还加入灵动岛设计。报道称新品包含 14 英寸与 16 英寸两个版本，售价将高于现款 2499 美元的起售价。 此举推翻了苹果高管多年来以人体工学为由坚持的立场，使 MacBook 成为支持触控的设备，可能影响开发者设计 Mac 应用的方式，以及 iPad 与 Mac 产品线的定位。外界普遍认为这一转变更多出于营收与营销考虑，而非纯粹的工效学理由，因此会波及消费者、配件厂商以及长期推出触屏笔记本的整个 PC 行业。 触控预计将作为键盘与触控板的补充而非替代，报道并未给出 OLED 面板类型、刷新率、铰链设计或 Apple Pencil 支持等技术细节。该消息来自 Bloomberg 的新闻简报而非苹果官方发布，因此售价与配置信息仍有待确认。

telegram · zaihuapd · 10月25日 14:25

**背景**: OLED（有机发光二极管）屏幕通过有机半导体层让每个像素自行发光，因此像素可以完全熄灭，相比现款 MacBook 使用的 LCD 面板能带来更深的黑色与更高的对比度。灵动岛是苹果在 iPhone 14 Pro 上引入的药丸形交互式开孔，可展开显示通知、媒体播放与后台活动。苹果长期以来一直主张伸手触摸垂直的笔记本屏幕并不舒适，因此此次报道中的转变被视为对其公开立场的一次明显背离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/OLED%E5%8E%9F%E7%90%86/10088264">OLED原理 - 百度百科</a></li>
<li><a href="https://juejin.cn/post/7140919368648491016">灵 动 岛 是 什 么 iphone14pro...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#MacBook Pro`, `#触屏`, `#OLED`, `#硬件发布`

---