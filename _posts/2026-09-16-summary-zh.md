---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16 23:03:56 +0000
lang: zh
report: default
---

> 从 186 条内容中筛选出 6 条重要资讯。

---

1. [低质中文赌场网站暗藏高危恶意软件基础设施](#item-1) ⭐️ 8.0/10
2. [新浪云 SAE 永久下线，Archive Team 紧急抢救早期 B 站视频](#item-2) ⭐️ 8.0/10
3. [美光称展示全球首款 512GB DDR5 模组，2027 年具备量产条件](#item-3) ⭐️ 8.0/10
4. [阶跃星辰发布 StepAudio 3 Music：用自然语言生成完整歌曲](#item-4) ⭐️ 7.0/10
5. [微信 8.0.78 支持将聊天记录打包转发给 ChatGPT](#item-5) ⭐️ 7.0/10
6. [极客湾：苹果首款 2nm 芯片 A20 Pro 随 iPhone 18 Pro 发布](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [低质中文赌场网站暗藏高危恶意软件基础设施](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 8.0/10

一家安全公司追踪到约 170 万个低质中文赌场网站，其中部分被与中国有关联的 APT 组织用作恶意软件传播和命令控制（C2）基础设施。自 2023 年以来，其中一个组织利用名为“PeckBirdy”的框架，把 C2 域名隐藏在赌博网站中，并通过虚假软件更新诱骗用户下载恶意程序。 这一手法把海量看似无害的赌博网站变成可长期使用的攻击基础设施，使其混入正常的互联网噪声之中，显著加大了安全团队的检测和归因难度。由于相关流量看起来只是普通的赌博浏览，安全运营中心的分析人员可能把恶意连接误判为员工违规上网，而不是升级为安全事件处理。 攻击者所依赖的关键点在于，这些网站的外观与普通赌博页面几乎完全一致，而恶意程序则以合法软件更新的名义投递。安全团队被提醒不要想当然地把访问这些域名的连接当作与工作无关的浏览行为，因为这一假设正是攻击者所利用的盲区。

telegram · zaihuapd · 9月16日 07:31

**背景**: APT（高级持续威胁）通常指资源充足、长期潜伏的入侵组织，往往与国家级背景相关，会隐蔽地维持对目标网络的访问。C2（命令控制）基础设施是这类组织向受感染主机下发指令、回传窃取数据的通道，因此把 C2 域名藏进外观正常的网站，有助于其规避黑名单封堵和下线打击。本案引人注目之处在于伪装层的规模：约 170 万个中文赌博和成人网站为恶意域名提供了掩护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7684659924174340122">红队渗透进阶：高级内网、域渗透、红队演练、护网攻防02...</a></li>
<li><a href="https://www.secrss.com/articles/16332">MuddyWater和 APT 34的背后会 是 同一个 组 织 吗？</a></li>

</ul>
</details>

**标签**: `#网络安全`, `#APT`, `#恶意软件`, `#威胁情报`, `#C2基础设施`

---

<a id="item-2"></a>
## [新浪云 SAE 永久下线，Archive Team 紧急抢救早期 B 站视频](https://tracker.archiveteam.org/sinavideo/#show-all) ⭐️ 8.0/10

国内首个公有 PaaS 平台新浪云 SAE（Sina App Engine）将于 2026 年 9 月 16 日 24 时正式永久下线，届时所有用户数据将被彻底删除。仍有约 420 TB 早期 B 站视频源文件存放在新浪云的 S3 存储桶中，志愿者组织 Archive Team 已累计抢救约 680 TB 数据，项目进度为 96.26%。 这是一次重要的互联网保存事件：关停可能抹去一段别无副本的早期中国视频文化史料，也凸显出一次普通的云服务退场就可能悄无声息地毁掉不可替代的数字遗产。同时它也展示了此前曾成功抢救 GeoCities、Yahoo\! Video 等服务的分布式志愿归档模式。 跟踪页面显示抢救进度为 96.26%，这意味着一旦到期后存储桶被清空，仍可能有虽小但并非可忽略的一部分数据彻底丢失。值得注意的是，这里所说的存储是新浪云自有的 S3 风格对象存储桶，而非亚马逊 AWS 的 S3；整个归档行动通过 Archive Team 的公开跟踪页和 GitHub 仓库协调。

telegram · zaihuapd · 9月16日 15:00

**背景**: 新浪云 SAE 于 2009 年上线，是中国首个公有云 PaaS 平台，提供 PHP、MySQL、Memcached、任务队列和存储等服务，以低成本、免运维著称，积累了庞大的开发者群体。B 站早期曾依赖新浪云存储托管其视频源文件，这正是大量原始素材至今仍留在该平台上的原因。Archive Team 是由 Jason Scott 等人于 2009 年共同发起的志愿者组织，专门在服务消失前抢先抓取处于风险中的互联网内容，成果通常存入互联网档案馆的 Wayback Machine。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wanyr.com/2026/06/%E6%96%B0%E6%B5%AA%E4%BA%91%EF%BC%88sae%EF%BC%89%E5%AE%A3%E5%B8%839%E6%9C%8816%E6%97%A5%E6%B0%B8%E4%B9%85%E5%85%B3%E5%81%9C%EF%BC%9A%E5%9B%BD%E5%86%85%E9%A6%96%E5%AE%B6paas%E5%B9%B3%E5%8F%B017.html">新浪云（SAE）宣布9月16日永久关停：国内首家PaaS平台17年历程落幕</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive_Team">Archive Team</a></li>
<li><a href="https://sae.sina.com.cn/">SinaAppEngine（SAE）– 免运维的云计算服务厂商</a></li>

</ul>
</details>

**标签**: `#data-preservation`, `#cloud-computing`, `#internet-archive`, `#bilibili`, `#paas`

---

<a id="item-3"></a>
## [美光称展示全球首款 512GB DDR5 模组，2027 年具备量产条件](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 8.0/10

美光称已展示全球首款面向服务器的 512GB DDR5 RDIMM，速率最高可达 9200 MT/s，并已交由 AMD 和 Intel 在未来服务器平台上进行验证。美光预计该模组将在 2027 年具备量产条件。 把 512GB 塞进单根服务器内存条大幅提升了内存密度——24 根即可组成 12TB 内存——这对内存需求巨大的 AI、内存数据库和虚拟化工作负载意义重大。美光还声称功耗降幅超过 60%，因此这项进步不只是容量提升，也是每 GB 能效的改善。 该模组采用 3D 堆叠 DRAM 芯片而非传统平面封装，美光给出的单根功耗为 16W，而四根等效的 128GB 模组合计为 44.2W。9200 MT/s 的速率和 2027 年的量产时间表都属于前瞻性说法，产品目前尚不可得，最终规格仍可能发生变化。

telegram · zaihuapd · 9月16日 16:15

**背景**: RDIMM（带寄存器的 DIMM）是服务器内存模组，在 DRAM 与内存控制器之间加入寄存器芯片，从而稳定信号完整性，并让单系统能容纳远比消费级 UDIMM 更多的模组。DDR5 的速率通常以 MT/s（每秒百万次传输）表示，衡量的是实际数据传输次数而非时钟周期，因此 DDR5-9200 意味着每个数据引脚每秒完成 9200 百万次传输。美光此次使用的 3D 堆叠技术，是把多颗 DRAM 芯片垂直键合并通过硅通孔互连——这与广泛用于 GPU 配套的 HBM 在基本原理上一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kingston.com/en/blog/pc-performance/mts-vs-mhz">MT/s vs MHz: A Better Measure for Memory Speed - Kingston ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#Micron`, `#Server Memory`, `#Hardware`, `#3D Stacking`

---

<a id="item-4"></a>
## [阶跃星辰发布 StepAudio 3 Music：用自然语言生成完整歌曲](https://static.stepfun.com/blog/stepaudio3/music/) ⭐️ 7.0/10

阶跃星辰发布了 AI 音乐生成模型 StepAudio 3 Music，它采用 MoE（混合专家）架构与 AR + DiT 生成范式，把自然语言的创作意图转化为完整的 48 kHz 立体声歌曲。该模型通过 ABC-COT 技术先生成歌曲结构、过渡与编曲规划再进行音频合成，阶跃星辰称其在 Audiobox 与 MuQ-Similarity 两项评测中均取得 SOTA 成绩。 音乐生成是生成式音频领域进展最快的前沿方向之一，一个同时兼顾高音频保真度（48 kHz 立体声）与细粒度可控性的模型，有望加速其在短视频配乐、词曲 Demo 和游戏主题曲等场景中的落地。阶跃星辰的入局也表明，中国 AI 实验室正在消费级与创作者工具市场上，与 Google Lyria 等既有音乐生成模型正面竞争。 模型的控制入口就是文本提示词本身：用户只需写明风格、人声、情绪、乐器、调性与速度，因此其定位更强调可控性而非单纯的音质。不过，Audiobox 与 MuQ-Similarity 上的 SOTA 结果均来自阶跃星辰自己的宣称，目前尚无独立基准测试或第三方验证公布。

telegram · zaihuapd · 9月16日 08:48

**背景**: AI 音乐生成模型的常见做法是先把音频压缩成离散或连续的 token，再学习生成这些 token：自回归（AR）方式逐个预测 token，擅长处理长时结构；扩散方式（DiT）则擅长生成高保真的音频细节。StepAudio 3 Music 将两者结合——用 AR 做规划、用 DiT 做合成——并置于 MoE 主干之中，通过把不同输入路由到专门的子网络来高效扩展模型容量。ABC-COT 借鉴了大语言模型中的思维链（Chain-of-Thought）思路：模型不是直接生成音频，而是先对歌曲结构与编曲进行推理规划，从而保证长曲目的连贯性。MuQ-Similarity 则是基于 MuQ 这一自监督音乐编码器构建的评测指标，用于衡量生成音乐与参考或提示词的契合程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stepaudiollm.github.io/step-audio-3-music/">StepAudio 3 Music</a></li>
<li><a href="https://www.emergentmind.com/topics/muq">MuQ : Self-Supervised Music Encoder</a></li>
<li><a href="https://gemini.google/us/overview/music-generation/?hl=en">Lyria — Gemini AI music &amp; song generator</a></li>

</ul>
</details>

**标签**: `#AI music generation`, `#generative audio`, `#MoE`, `#diffusion models`, `#StepFun`

---

<a id="item-5"></a>
## [微信 8.0.78 支持将聊天记录打包转发给 ChatGPT](https://www.chaincatcher.com/article/2290109) ⭐️ 7.0/10

手机微信升级至 8.0.78 后，用户在「多选聊天记录」并选择「转发到其他应用」时，除了腾讯自家的元宝和 WorkBuddy，还能通过「选择手机中的应用」直接把内容交给 ChatGPT 等第三方 App，一次最多 100 条。微信会把聊天内容打成 ZIP 压缩包，内含按时间排序的 TXT 文本及附件；电脑端微信也开放了类似入口，社区开发者已基于此做出中转工具，可将聊天记录送进 ChatGPT、Claude 等 AI。 这是来自全球用户量最大的即时通讯应用之一的重要产品改动，它把原本封闭的聊天记录变成可供外部 AI 助手读取的数据源，等于为腾讯无法完全掌控的跨应用 AI 工作流开了口子。其意义在于：一方面让批量导出私密对话数据变得「合规化」，带来总结、翻译、检索长对话等实用效率场景；另一方面也让数亿用户面临隐私与数据外流的现实问题。 该功能每次最多导出 100 条消息，并以 ZIP 压缩包形式交付，其中是按时间整理的 TXT 文本加附件，而不是结构化 JSON 或 API 式数据流，因此接收方 AI 需要自行解析纯文本包。入口复用的是已有的「转发到其他应用」流程，新增之处在于「选择手机中的应用」可把 ChatGPT、Claude 等已安装的第三方 App 暴露出来；电脑端微信也开放了类似入口，社区中转工具正是基于此开发。

telegram · zaihuapd · 9月16日 14:15

**背景**: 微信是腾讯在中国市场的主导级即时通讯应用，过去想把聊天记录搬出微信相当困难，导出渠道基本局限于腾讯自家生态，或者靠手动截图与复制粘贴。本次更新中提到的腾讯自家 AI 产品包括：2024 年 5 月基于自研混元大模型推出的全能 AI 助手「元宝」，以及腾讯云出品的全场景 AI 办公工作台 WorkBuddy，后者支持多 Agent 并行并内置 MCP、Skills 等扩展能力。新功能把同样的转发思路延伸到非腾讯系的 AI 应用上，这对长期坚持封闭生态、对外部集成较为谨慎的微信来说并不常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.workbuddy.cn/">WorkBuddy - AI Agent 办公新范式</a></li>
<li><a href="https://36kr.com/p/3192816744210825">元 宝 逆袭登顶， 腾 讯 “大力出奇迹”能维持多久？ -36氪</a></li>
<li><a href="https://www.aiww.com/aitool/tengxunyuanbao/jianjie">元 宝 详细介绍_优势特点_使用流程 - AIWW</a></li>

</ul>
</details>

**标签**: `#wechat`, `#ai-integration`, `#privacy`, `#chatgpt`, `#product-update`

---

<a id="item-6"></a>
## [极客湾：苹果首款 2nm 芯片 A20 Pro 随 iPhone 18 Pro 发布](https://www.bilibili.com/video/BV1oZeA6fERD) ⭐️ 6.0/10

苹果发布了搭载首款 2nm 旗舰芯片 A20 Pro 的 iPhone 18 Pro 系列，该芯片集成 6 核 CPU（超核提速最多 20%）、7 核 GPU（提速 40%）与双 16 核神经网络引擎，苹果称其为「所有智能手机中速度最快」的芯片。此次发布同时带来自研 C2 调制解调器（上传提速 50%、功耗降低 15%）以及苹果首款定制无线芯片 N1，支持 Wi-Fi 7 与蓝牙 6。 这是旗舰智能手机首次采用 2nm 级别制程，标志着产业正式转向环栅（GAA）纳米片晶体管时代，也让苹果在能效比上取得领先，Android 阵营需要跟进回应。同时，苹果第三代自研调制解调器继续侵蚀高通在 iPhone 基带中的份额，而基带是移动芯片中最赚钱的品类之一。 除晶体管微缩之外，A20 Pro 还采用借鉴 M 系列的全新封装设计，并叠加面积约为上代 3 倍的 VC 均热板，苹果称其持续性能最多可提升 40%。C2 调制解调器以 C1X 为基础，依靠 AI 改善蜂窝网络质量，新增 5G 毫米波支持（n258、n260、n261 频段）与 sub-6GHz 的 4×4 MIMO；不过本条新闻本身只是对极客湾视频的简要第三方转述，并非附带跑分的一手资料。

telegram · zaihuapd · 9月16日 13:24

**背景**: 制程节点是制造芯片的工艺配方，数字越小通常意味着晶体管更多、频率更高、能效更好，2nm 是 3nm 之后的下一代节点。2nm 的关键结构变化是从 FinFET 转向环栅（GAA）纳米片晶体管，栅极从四面包围沟道，从而降低漏电。台积电已于 2025 年 12 月宣布其 N2 2nm 工艺进入量产，苹果则在 2026 年 8 月将其用于 M6 芯片，A20 Pro 相当于把该节点延伸到 iPhone。VC 均热板是一种通过液-气相变导热的密封金属板，效率通常比传统热管高 20%~30%，因此在轻薄手机中加大均热板面积对持续性能释放尤为关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/2%E7%BA%B3%E7%B1%B3%E5%88%B6%E7%A8%8B">2纳米制程 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.ithome.com/1/000/540.htm">苹果发布自研 C2 5G 调制解调器：上传提速 50%，美版 iPhone 18 Pro ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/721318644">高效散热解决方案：VC均热板技术解析 - 知乎</a></li>

</ul>
</details>

**标签**: `#apple`, `#semiconductor`, `#mobile-chips`, `#hardware`, `#2nm`

---