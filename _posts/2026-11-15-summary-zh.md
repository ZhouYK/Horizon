---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15 23:04:10 +0000
lang: zh
report: default
---

> 从 203 条内容中筛选出 6 条重要资讯。

---

1. [SpaceX 星舰轨道返回后首次被发射塔机械臂捕获](#item-1) ⭐️ 8.0/10
2. [美团开源 LongCat-2.5：1.6 万亿参数智能体模型，称全程未用英伟达 GPU](#item-2) ⭐️ 8.0/10
3. [华为云 MaaS 平台上线开源盘古模型 openPangu-2.1-Pro](#item-3) ⭐️ 7.0/10
4. [特斯拉 Cybercab 每月须付 299 美元订阅费，否则车辆无法运行](#item-4) ⭐️ 6.0/10
5. [FAA 全国停飞起因：铜线换光纤升级后路由器故障](#item-5) ⭐️ 6.0/10
6. [美法官驳回美光、三星、SK 海力士撤销 DRAM 价格操纵诉讼的动议](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [SpaceX 星舰轨道返回后首次被发射塔机械臂捕获](https://www.spacex.com/launches/starship-flight-15) ⭐️ 8.0/10

SpaceX 宣布星舰第 15 次试飞取得突破：飞船完成约 22.5 小时的轨道飞行后返回得克萨斯州发射基地，并首次由发射塔机械臂直接捕获，同时部署了 26 颗星链 V3 卫星。不过超重型助推器未能按计划返回发射塔，最终在墨西哥湾溅落，因此尚未实现两级同时回收。 这是可重复使用航天器的重大里程碑：用发射塔机械臂直接捕获轨道级飞船，有望相比海上溅落和船只回收大幅缩短周转时间并降低成本。同时，这也验证了星舰作为更大规模下一代星链卫星部署平台的能力。 据报道，飞船在绕地球约 14 圈后于得克萨斯州发射场被捕获。助推器未能被捕获说明两级完全复用仍在验证之中；星链 V3 卫星则是更大的新一代设计，旨在利用星舰的运载能力。

telegram · zaihuapd · 11月14日 23:49

**背景**: 星舰是 SpaceX 的超重型运载系统，由超重型一级助推器和星舰上面级组成，设计目标是实现完全可重复使用。SpaceX 使用发射塔上的大型机械臂来回收超重型助推器，而不是依靠着陆腿。星链 V3 是 SpaceX 第三代宽带卫星，容量和数据密度相比前代大幅提升，并且是为从星舰部署而设计的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spacex.com/launches">SpaceX - Launches</a></li>
<li><a href="https://starlink.com/updates/starlink-version-3-satellites">Starlink Version 3 Satellites</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Super_Heavy">SpaceX Super Heavy - Wikipedia</a></li>

</ul>
</details>

**标签**: `#spacex`, `#starship`, `#reusable-spacecraft`, `#aerospace`, `#news`

---

<a id="item-2"></a>
## [美团开源 LongCat-2.5：1.6 万亿参数智能体模型，称全程未用英伟达 GPU](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

美团旗下的 LongCat 团队在模型首次发布约一周后，公开了 LongCat-2.5 的权重，这是一个 1.6 万亿参数的多模态智能体模型。官方称该模型训练全程使用中国芯片——华为昇腾加速卡，未使用任何英伟达 GPU，并以 MIT 许可证发布权重，允许商业使用。 如果这一说法成立，它将成为“前沿规模模型训练可以脱离英伟达硬件完成”最有力的公开证据之一，在美国对华高端 AI 芯片出口管制的背景下具有重要战略意义。同时，MIT 许可证让一个万亿参数级别的智能体编程模型可以被免费商用，将对闭源智能体模型 API 形成直接竞争压力。 LongCat-2.5 采用稀疏混合专家（MoE）架构，每个 token 激活约 480 亿参数，上下文窗口最长可达 100 万 token，支持文本、图像和视频输入。它在 Terminal Bench v2.1 上得分 88.4，略低于 Claude Opus 5 的 89.1——具备竞争力但并非领先，而“仅用昇腾训练”的说法目前尚未得到第三方独立验证。

telegram · zaihuapd · 11月15日 11:08

**背景**: 混合专家（MoE）模型把参数拆分成许多专精子网络，每个 token 只激活其中一小部分，因此一个 1.6 万亿参数的模型每 token 只需约 480 亿参数的计算量。智能体模型经过专门调优，可以自主完成编写与调试代码等冗长、多步骤任务，而 Terminal Bench 这类基准用来衡量模型完成真实命令行工作的能力。华为昇腾芯片是中国旗舰级的国产 AI 加速卡，在美国出口管制限制中国企业获取英伟达高端硬件后，被作为英伟达 GPU 的替代方案大力推广。MIT 许可证是一种宽松的开源协议，允许在极少限制下进行商业复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpulsenews.tech/articles/meituan-longcat-2-5-1-6t-multimodal-agentic-coding">Meituan &#x27;s LongCat - 2 . 5 : A 1.6T-Parameter Multimodal Agent Model at...</a></li>
<li><a href="https://anyrouter.dev/model/meituan/longcat-2.5">LongCat - 2 . 5 · meituan · pricing &amp; API · AnyRouter</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#Huawei Ascend`, `#agent models`, `#AI hardware`

---

<a id="item-3"></a>
## [华为云 MaaS 平台上线开源盘古模型 openPangu-2.1-Pro](https://mp.weixin.qq.com/s/8JfFmscBTDl_mPQMycD8Nw) ⭐️ 7.0/10

11 月 15 日，华为云 MaaS（模型即服务）平台正式上线开源盘古模型 openPangu-2.1-Pro，围绕 Agent 开发、AI 编码和推理优化三大方向进行能力升级。该模型基于 10 万余条专项数据优化了 Skills 触发与工具调用能力，并重点适配鸿蒙 ArkTS 开发与昇腾算子生成。 华为把自家的旗舰盘古模型系列开放出来，并与鸿蒙软件生态和昇腾硬件生态深度绑定，为国内开发者提供了一套较为完整的国产化 Agent 与编码助手方案。同时公布明确的按 token 计费的 MaaS 价格，说明华为希望在国内云厂商的企业级大模型市场上正面竞争。 定价为输入 0.8 元/百万 tokens、输出 3.2 元/百万 tokens、缓存命中输入 0.016 元/百万 tokens，缓存命中的成本远低于常规输入。模型已接入智果 AgentArts、码道 CodeArts、果办 OfficeAce 等华为自有产品，但此次发布并未公布基准测试成绩或模型参数规模等细节。

telegram · zaihuapd · 11月15日 16:03

**背景**: MaaS（模型即服务）是一种云端交付方式，厂商托管大语言模型并通过 API 开放，开发者按 token 付费而无需自己运行 GPU。盘古是华为自研的模型系列，此次以开源形式发布而非仅作为闭源云服务提供，因而格外受到关注。昇腾是华为自研的 AI 芯片产品线，而高效生成昇腾算子一直是从业者的一块痛点，尤其是在难以依赖英伟达硬件的国内环境下；ArkTS 则是华为面向手机、平板等多设备的分发式操作系统鸿蒙上的主要应用开发语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Huawei">Huawei - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/HarmonyOS">HarmonyOS - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Huawei Pangu`, `#open-source LLM`, `#AI agents`, `#code generation`, `#Ascend`

---

<a id="item-4"></a>
## [特斯拉 Cybercab 每月须付 299 美元订阅费，否则车辆无法运行](https://www.tesla.com/configurator/api/v4/terms?category=autonomy_subs&amp;amp;locale=en_US&amp;amp;model=cc&amp;amp;saleType=Sale) ⭐️ 6.0/10

特斯拉公布了 Cybercab 的自主驾驶订阅协议：车辆售价 29,990 美元，但车主必须每月支付 299 美元的自主驾驶订阅费，否则车辆无法运行；特斯拉可提前一个月通知后调整该价格。欠费或违规使用可能导致订阅被暂停或取消，累计三次警告则会停用自动驾驶功能一周。 这让一次性的购车行为变成永久性的软件月费账单，而且车主一旦停付，车辆就基本无法使用，这比一次性买断 FSD 或可选的月度订阅都要激进得多。如果其他车企跟进，个人拥车经济账以及“软件锁定”车辆的二手残值都可能发生明显变化。 车辆通过地理围栏限制在指定区域内运行，未经授权车主不得将其接入网约车、配送或租赁平台。Electrek 指出，Cybercab 与用于 Robotaxi 服务的 Model Y 采用相同的 AI4 硬件并运行同一套自动驾驶软件，但面向普通车主的 FSD 仍需人类监督。

telegram · zaihuapd · 11月15日 01:10

**背景**: 特斯拉长期把 FSD（完全自动驾驶）辅助驾驶套件作为可选项出售，支持一次性买断或按月付费，并且仍要求驾驶员保持注意力。Cybercab 是特斯拉专门打造的双座无人驾驶出租车，没有方向盘和踏板，设计上就是在限定区域内自主运行，因此地理围栏与订阅制成为其核心机制。地理围栏是指利用定位数据划定虚拟边界，车辆在边界之外不得启用自动驾驶，这也是当前无人驾驶出租车队普遍采用的做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tesla.com/">Electric Cars, Solar &amp; Clean Energy | Tesla</a></li>
<li><a href="https://www.angeltranslation.com/glossary/geofencing/">Geofencing 地 理 围 栏 | Angel Translation</a></li>
<li><a href="https://www.163.com/dy/article/KDKPPS060511ADC6.html">小鹏第二代VLA 模 型发布， Robotaxi 无 人 驾 驶 明年试 运 营</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#Cybercab`, `#autonomous-driving`, `#subscription-model`, `#robotaxi`

---

<a id="item-5"></a>
## [FAA 全国停飞起因：铜线换光纤升级后路由器故障](https://www.theverge.com/transportation/1033898/faa-ground-stop-sean-duffy-faa-copper-wire) ⭐️ 6.0/10

美国交通部长 Sean Duffy 11 月 14 日表示，FAA 当周五下达的全国停飞源于一处偏远设施的例行维护——将老旧铜线更换为光纤，随后新装路由器出现故障。该故障路由器每 4 到 5 秒向其他路由器发出逾千次连接请求，干扰了雷达信号与飞机通信，导致数千架次航班停飞。 这起事件表明，在陈旧的通信链路中，仅仅一台行为异常的网络设备就可能让整个国家航空系统停摆，把一次例行现代化改造变成运营危机。它也为 FAA 向国会争取空管基础设施现代化资金提供了更有力的理由。 Duffy 表示根因尚未确定，可能是硬件故障、配置错误，也可能是负责该设施的承包商 L3Harris 的操作失误。故障模式并非简单的中断，而是连接请求风暴——每 4 到 5 秒逾千次请求，这正是下游雷达与语音链路出现劣化而非干净宕机的原因。

telegram · zaihuapd · 11月15日 02:10

**背景**: FAA 的空管网络仍大量依赖陈旧的铜缆和定制通信设备，其中部分已使用数十年，该机构多年来一直在将这些链路迁移到光纤。所谓“全国停飞”（ground stop）是当管制员无法确信能安全间隔飞机时，在全国或某区域紧急叫停起飞航班的指令。L3Harris 是美国主要的国防与通信承包商，为包括 FAA 相关基础设施在内的政府机构维护关键任务系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/L3Harris">L3Harris - Wikipedia</a></li>
<li><a href="https://www.l3harris.com/about-us">About Us | L3Harris ® Fast. Forward.</a></li>

</ul>
</details>

**标签**: `#network outage`, `#infrastructure reliability`, `#aviation systems`, `#router failure`, `#systems engineering`

---

<a id="item-6"></a>
## [美法官驳回美光、三星、SK 海力士撤销 DRAM 价格操纵诉讼的动议](https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge) ⭐️ 6.0/10

美国地区法官 Noël Wise 驳回了美光、三星和 SK 海力士要求撤销 DRAM 价格操纵集体诉讼的动议，认定原告提交的新证据使三家厂商的协同行为具有共谋的可能性。原告由 17 名个人和小企业组成，指控这三家供应商在一年内四次采取同步行动限制 DRAM 供应，导致价格上涨最多达 500%。 这一裁定让案件得以继续推进，而该案可能揭示主导全球 DRAM 供应的三家厂商如何决定产能与定价，这直接影响 PC、服务器和智能手机的内存成本。由于这三家公司掌控着 DRAM 市场的绝大部分份额，一旦被认定存在协同限产，将对硬件价格以及反垄断执法者如何看待高度集中的半导体市场中的平行产能决策产生广泛影响。 法官将三家公司的同步行为形容为“像编队飞行的鹰”，而非各自独立的商业判断，这正是驳回撤诉动议阶段的核心门槛问题。被告须在 12 月 7 日前作出回应，案件管理会议定于 2027 年 1 月举行，这意味着诉讼很可能还要持续数年才会进入审理或和解阶段。

telegram · zaihuapd · 11月15日 16:39

**背景**: DRAM（动态随机存取内存）是电脑、手机和服务器使用的主内存，其供应高度集中于三星、SK 海力士和美光三家厂商。在美国联邦民事诉讼中，依据《联邦民事诉讼规则》第 12\(b\)\(6\) 条提出的撤诉动议主张起诉状未能陈述可获救济的法律请求，此阶段法院须假定原告的事实主张为真，因此驳回动议只意味着共谋证据至少“可信”，而非已被证实。反垄断法认为，单纯的“平行行为”（即竞争对手各自独立做出相似决策）不足以构成违法，原告必须证明更多内容，例如平行行动加上暗示存在协议的证据。DRAM 行业此前也有先例：美国司法部曾在 2000 年代调查 DRAM 价格垄断，三星和当时的海力士在该案中认罪，海力士于 2005 年支付了 1.85 亿美元罚款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbeta.com.tw/articles/tech/1567250.htm">苹果供应商被指 操 纵 DRAM 价 格 三 星 、 SK ... - cnBeta.COM</a></li>
<li><a href="https://min.news/zh-hans/digital/5cacd8c8cb30a75dd106833c3a229b04.html">苹果供应商被指 操 纵 DRAM 价 格 三 星 、 SK ...</a></li>
<li><a href="https://www.law.cornell.edu/rules/frcp/rule_12">Rule 12 . Defenses and Objections: When and How Presented; Motion ...</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#antitrust`, `#semiconductor industry`, `#hardware supply chain`, `#price fixing`

---