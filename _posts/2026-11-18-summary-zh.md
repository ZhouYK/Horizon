---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18 23:06:20 +0000
lang: zh
report: default
---

> 从 251 条内容中筛选出 6 条重要资讯。

---

1. [Java4Shell：Java 爆出无需认证的严重远程代码执行漏洞（CVE-2026-114938）](#item-1) ⭐️ 8.0/10
2. [Xint 披露 NGINX2Root：5 个 nginx 漏洞串联可拿到主机 root](#item-2) ⭐️ 8.0/10
3. [美国芯片新规致 4.8 亿美元字节跳动相关 GPU 贷款暂停](#item-3) ⭐️ 7.0/10
4. [微信小微 AI 助手测试扩大，日活达 3000 万](#item-4) ⭐️ 7.0/10
5. [腾讯三季报：AI 资本开支远超预期，WorkBuddy 日均 Token 用量登顶国内](#item-5) ⭐️ 6.0/10
6. [旅行者 1 号成为首个距地球一光日的人造物体](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Java4Shell：Java 爆出无需认证的严重远程代码执行漏洞（CVE-2026-114938）](https://censys.com/advisory/cve-2026-114938/) ⭐️ 8.0/10

被命名为“Java4Shell”的高危 Java 远程代码执行漏洞 CVE-2026-114938 被公开，CVSS 4.0 评分高达 9.2，且利用时无需任何认证。据 Censys 的公告，该漏洞潜伏近四年，影响 Java 17（17.0.6 及之后所有版本）、Java 21、Java 25 和 Java 27。 Java 支撑着大量企业后端、应用服务器和中间件，因此出现在较新 LTS 级别版本中的无需认证远程代码执行漏洞，属于最严重的一类服务端缺陷，可能迫使大规模服务器集群紧急打补丁。不过其影响范围被部分收窄，因为利用该漏洞依赖特定的现代 x86-64 硬件，而不是波及所有 Java 部署环境。 该漏洞仅影响支持 AVX-512 VBMI 指令集的 x86-64 服务器处理器，大致对应 2021 年起发布的 Intel Ice Lake 及更新世代 Xeon，以及 2022 年起发布的 AMD Zen 4 及更新 EPYC/Ryzen，ARM64 架构不受影响。标准 Java 8 和 Java 11 通常不受影响，但 Oracle Java 8 Enterprise Performance Pack 是例外；目前公开信息仅为一份简短公告，缺少关于根本原因和利用手法的技术细节。

telegram · zaihuapd · 11月18日 03:55

**背景**: AVX-512 是 Intel 为 x86 指令集提出的 512 位 SIMD 扩展家族，而 VBMI（向量字节操作指令）是其中的子扩展之一，提供字节级重排操作，常被 JVM 内部高度优化的加密、字符串处理等 intrinsic 代码使用。CVSS 4.0 是由 FIRST 维护的通用漏洞评分系统当前版本，是一个用于衡量软件缺陷严重程度的开放框架，9.2 分属于“严重”区间。Oracle 的 Java SE 8 Enterprise Performance Pack 是一项商业产品，把 JDK 17 的 JVM 性能改进回移到 Java 8，这解释了为何某个 Java 8 版本可能继承较新 JDK 的代码路径。此类漏洞常被拿来与 2021 年引发全行业紧急打补丁的 Log4j 漏洞 Log4Shell 相比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AVX-512">AVX-512 - Wikipedia</a></li>
<li><a href="https://www.intel.com/content/www/us/en/developer/articles/technical/intel-avx-512-instructions.html">Intel® AVX-512 Instructions</a></li>

</ul>
</details>

**标签**: `#Java`, `#security vulnerability`, `#RCE`, `#CVE`, `#AVX-512`

---

<a id="item-2"></a>
## [Xint 披露 NGINX2Root：5 个 nginx 漏洞串联可拿到主机 root](https://nginx2root.com/) ⭐️ 8.0/10

安全研究者 Xint 公开了 NGINX2Root：由 5 个 nginx 漏洞加一个 Linux 内核缺陷组成的利用链，可从 nginx 的未认证访客一路提权到主机 root。其中最核心的 CVE-2026-123007 是 nginx HTTP/2 流控中的内存破坏漏洞，无需认证即可在 worker 进程中执行命令；nginx 1.30.7 与 1.31.9 已于 11 月 18 日连同另外 9 个 CVE 一起修复。 最严重的漏洞在仅提供 HTTPS 静态文件服务的机器上也能被未认证触发，这意味着自 2015 年起启用过 HTTP/2 的大量 nginx 部署都可能受影响。由于 Rapid7 已放出 PoC，且整条利用链的终点是主机 root 而非受限的 worker 用户，防御方应将其视为高优先级的修复任务。 CVE-2026-123007 是流控计数中的整数下溢，使非法的窗口值进入不安全的访存操作，可导致内存泄露、堆破坏乃至远程代码执行；问题代码可追溯到 2015 年的 nginx 1.9.5，影响范围延续到 1.31.8，同一段 HTTP/2 代码中还存在配套的释放后使用漏洞 CVE-2026-123633。目前尚未发现在野利用，无法及时升级的机构应关闭对外开放的 HTTP/2。

telegram · zaihuapd · 11月18日 16:21

**背景**: nginx 是被广泛使用的 Web 服务器与反向代理，采用一个 master 进程加若干 worker 进程的架构，由 worker 以较低权限处理进来的请求。HTTP/2 是较新的 HTTP 协议版本，可在单条连接上多路复用大量请求，其流控机制用于调节每条流可发送的数据量。该机制中的内存安全漏洞之所以危险，是因为以 worker 用户身份取得代码执行往往只是更长提权链的第一步——在本例中，攻击者再借助其余 nginx 漏洞和一个 Linux 内核缺陷，最终拿到宿主机的 root 权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://computingforgeeks.com/nginx-cve-2026-123007/">nginx CVE-2026-123007: Check, Disable HTTP/2, Patch ...</a></li>
<li><a href="https://safe.security/resources/blog/cve-2026-123007-cve-2026-123633-nginx-http-2-rce-two-critical-flaws-turn-protocol-handling-into-remote-code-execution/">NGINX HTTP/2 RCE: CVE-2026-123007 &amp; CVE-2026-123633 | SAFE</a></li>
<li><a href="https://docs.nginx.com/nginx/admin-guide/basic-functionality/runtime-control/">Control NGINX Processes at Runtime | NGINX Documentation</a></li>

</ul>
</details>

**标签**: `#nginx`, `#security`, `#vulnerabilities`, `#HTTP/2`, `#RCE`

---

<a id="item-3"></a>
## [美国芯片新规致 4.8 亿美元字节跳动相关 GPU 贷款暂停](https://www.bloomberg.com/news/articles/2026-11-17/banks-pause-480-million-chip-loan-tied-to-china-s-bytedance) ⭐️ 7.0/10

五家原本在评估一笔 4.8 亿美元贷款的银行已暂停推进该交易，这笔资金原计划为字节跳动在马来西亚的数据中心采购英伟达先进 GPU，而美国最新的 AI 芯片出口管制引发了合规担忧。部分银行内部已在讨论退出或不参与，在全面评估新规之前，这笔融资难以取得进展。 此次暂停表明，美国的出口管制不只是在实体芯片出货环节产生阻碍，如今已开始波及 AI 基础设施的融资环节，可能拖慢与中国相关的东南亚算力建设进度。这也会让那些在中国客户与英伟达硬件之间充当中间方的第三方云服务商面临更严格的审视，并可能使贷款机构对以 GPU 为抵押的项目融资整体上更加谨慎。 借款方为新加坡云服务商 Aolani Cloud，星展集团（DBS）担任牵头安排行；Aolani 表示正与监管机构及融资伙伴一同评估新规、确保项目合规，但银行业人士称，在全面理解新规之前这笔融资无法推进。此前的报道显示，该马来西亚项目计划部署约 500 套英伟达 Blackwell 计算系统，总计约 3.6 万颗 B200 芯片。

telegram · zaihuapd · 11月18日 05:11

**背景**: 美国政府持续收紧对华出口英伟达加速器等先进 AI 芯片的规定，并日益关注间接路径，包括中国企业在东南亚租用算力，或与马来西亚、新加坡、泰国的本地云服务商合作。由于 GPU 如今被视为可抵押资产，AI 云服务商常通过 GPU 抵押贷款或项目融资来采购硬件，这意味着出口规则的变动可能在一颗芯片尚未出货前就冻结整笔交易。正是这种合规风险与信用风险之间的连接，让一次监管更新演变成了一笔 4.8 亿美元融资的搁浅。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/zhongwen/articles/cmpdwn010nyvo/simp">特朗普访华之际 美 国 封堵中 国 公司在东南亚租 用 AI ... - BBC News 中文</a></li>
<li><a href="https://www.yfchuhai.com/article/10228107.html">TikTok砸250亿美元建东南亚 数 据 中 心 全球大厂为何涌向泰国建机房</a></li>
<li><a href="https://www.gate.com/zh/learn/articles/coreweave-gpu-financing">CoreWeave 为什么采用 GPU 抵押融资？AI 算力公司如何利用资产支持债...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#export controls`, `#ByteDance`, `#GPU financing`, `#US-China tech`

---

<a id="item-4"></a>
## [微信小微 AI 助手测试扩大，日活达 3000 万](https://mp.weixin.qq.com/s/r3NthxJZQJgztyLADwNV4A) ⭐️ 7.0/10

腾讯在 2026 年第三季度财报中披露，微信内置 AI 助手「小微」的测试范围已经扩大，日活跃用户数达到约 3000 万，并正逐步融入微信聊天、朋友圈、公众号和视频号等场景。腾讯同时表示，小微采用针对成本效率优化的定制版 WeLM 模型，推理成本较低且持续下降，未来部分推理任务预计将转移到用户设备端运行。 3000 万日活这一数字使小微成为中国规模最大的消费级 AI 助手部署之一，说明腾讯正借助已有的超级应用向用户分发 AI 能力，而非依赖独立聊天应用。其提出的向端侧推理迁移的方向，也反映出大型平台在助手使用量向数亿级扩张时，如何控制服务成本与延迟的打算。 腾讯将低成本归因于一款以成本效率而非绝对能力为优化目标的 WeLM 变体，但并未披露模型规模、延迟数据或端侧上线的具体时间表。该产品目前仍属测试（灰度）阶段而非全量上线，且 WeLM 本身主要服务微信内部 AI 产品，并未像混元那样提供面向广泛开发者的公开 API。

telegram · zaihuapd · 11月18日 11:35

**背景**: WeLM 是微信团队自研的中英双语预训练语言模型系列，公开资料介绍了在不足 14T tokens 语料上训练的 80B-A3B 稀疏 MoE 模型，以及通过深度扩展（Depth Up-Scaling）得到的 130B 变体。端侧推理指把模型直接运行在手机等终端设备上，而不必将每次请求发送到云端 API，可降低延迟、带宽消耗与隐私暴露，但受限于终端算力、内存、功耗和存储。小微是直接嵌入微信内部的 AI 助手，其规模增长更多依赖微信既有用户基础，而非拉新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://welm.weixin.qq.com/">WeLM Blog</a></li>
<li><a href="https://www.aihub.cn/ai-model/welm/">WeLM - 微信团队自研的微信生态大语言模型 - AIHub</a></li>
<li><a href="https://baike.baidu.com/item/%E7%AB%AF%E4%BE%A7%E6%8E%A8%E7%90%86/68743074">端侧推理 - 百度百科</a></li>

</ul>
</details>

**标签**: `#微信`, `#AI助手`, `#WeLM`, `#端侧推理`, `#腾讯`

---

<a id="item-5"></a>
## [腾讯三季报：AI 资本开支远超预期，WorkBuddy 日均 Token 用量登顶国内](https://api3.cls.cn/share/article/2537922?os=android&amp;amp;sv=8.8.5&amp;amp;app=cailianpress&amp;amp;selected=) ⭐️ 6.0/10

腾讯公布第三季度财报，营收 2073 亿元、同比增长 8%，略低于市场预期，归母净利润 636 亿元、同比增长 0.8%。当季资本开支达 814.33 亿元，远高于市场预估的 554 亿元，单季自由现金流为负 691 亿元；同时腾讯披露 WorkBuddy 已成为国内大语言模型日均 Token 用量最高的 AI 产品，每日消耗量超过 100 万亿。 实际资本开支与市场预期之间的巨大落差，说明腾讯正在以远超分析师预估的速度加码 AI 基础设施，甚至不惜让自由现金流转负，这在中国的超大规模云厂商中正变得越来越普遍。若 WorkBuddy 宣称的日均 100 万亿 Token 消耗量属实，它将成为国内规模最大的面向消费者的 LLM 工作负载，也是观察 AI 助手在办公场景普及速度的重要风向标。 营收略低于预期（同比增长 8%）、净利润基本持平，说明这份财报的重点在支出而非盈利。Token 消耗量只是衡量 AI 工作负载规模的粗略指标，而非收入指标——它反映的是模型读入和生成了多少文本——腾讯也没有披露这一用量中有多少来自付费用户、多少来自免费流量。

telegram · zaihuapd · 11月18日 09:20

**背景**: Token 是大语言模型处理文本的基本单位，大致一个中文词语、一个英文单词、一个数字或一个符号算作一个 Token，因此日均 Token 消耗量常被用来衡量一款 AI 产品实际被使用的强度。WorkBuddy 是腾讯面向职场效率的全场景 AI 智能体，已在 iOS、Android 和鸿蒙三个平台上线，支持多模型动态调用和本地批量信息处理。资本开支指用于数据中心、GPU 等训练与推理基础设施的投入；自由现金流是经营现金流减去这部分开支后的余额，因此 AI 投入激进时自由现金流就可能转为负值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://open2ai.cn/workbuddy.html">WorkBuddy - 腾 讯 全场景 AI 智能体</a></li>
<li><a href="https://m.ebrun.com/687414.html">WAIC亮点｜ 腾 讯 上线 WorkBuddy APP， AI 办公开始“移动化” - AI ...</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2550219">主流大模型Token计算方式全解析：从原理到选型-腾讯云开发者社区-腾讯...</a></li>

</ul>
</details>

**标签**: `#tencent`, `#ai-infrastructure`, `#earnings`, `#llm-adoption`, `#china-tech`

---

<a id="item-6"></a>
## [旅行者 1 号成为首个距地球一光日的人造物体](https://www.cnn.com/2026/11/18/science/voyager-1-light-day) ⭐️ 6.0/10

美国东部时间 11 月 18 日凌晨 5 时 16 分左右，飞行了 49 年的旅行者 1 号抵达距地球约 260 亿千米处，即一个光日的距离。无线电信号从地球到达探测器现在需要整整 24 小时，它由此成为首个飞到如此遥远距离的人造物体。 这一里程碑把“光日”这个抽象单位变成了人类硬件实际飞行距离的具体标尺，同时也说明探测器尽管电力持续衰减，仍能不断回传科学数据。如今每一次让它继续存活的供电调整，也在不断拓宽深空长周期任务运营的实践边界。 旅行者 1 号目前仅有两台科学仪器仍在工作，NASA 近期对设备供电的调整预计可节省约 10 瓦电力，使任务延长约两年半。与探测器之间的往返通信如今已需要近两天时间。

telegram · zaihuapd · 11月18日 14:41

**背景**: 光日指光在 24 小时内走过的距离，约 259 亿千米，因此旅行者 1 号处于 260 亿千米处，意味着它发出的无线电信息抵达地球时已是整整一天前发出的。旅行者 1 号于 1977 年 9 月 5 日发射，2012 年飞出太阳风层顶进入星际空间。它依靠放射性同位素温差发电机（RTG）供电，通过热电偶将钚-238 衰变产生的热量转化为电能；发电功率已从发射时的约 470 瓦降至约 215 瓦，平均每年衰减约 4 瓦。通信依赖 NASA 的深空网络，需要提前调度大型天线在漫长的传输窗口内对准探测器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnet.com/science/space/voyager-1-passes-one-light-day/">Voyager 1 Hits One Light-Day From Earth on Wednesday... - CNET</a></li>
<li><a href="https://en.wikipedia.org/wiki/Radioisotope_thermoelectric_generator">Radioisotope thermoelectric generator - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Voyager_1">Voyager 1 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Voyager 1`, `#space exploration`, `#NASA`, `#interstellar space`, `#science milestone`

---