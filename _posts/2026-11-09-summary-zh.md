---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09 23:04:47 +0000
lang: zh
report: default
---

> 从 260 条内容中筛选出 9 条重要资讯。

---

1. [未修复的 iOS 沙盒逃逸 PoC「worse\_query」公开，波及 iOS 27.2 及 27.3 beta](#item-1) ⭐️ 8.0/10
2. [AI 辅助设计的禽流感候选疫苗在动物试验中显示广谱保护](#item-2) ⭐️ 8.0/10
3. [谷歌发布 TPU 8tx 与 TPU 8i Max，加速挑战英伟达](#item-3) ⭐️ 8.0/10
4. [字节跳动发布 Seedream 5.5，支持百轮连续编辑与原生透明通道](#item-4) ⭐️ 7.0/10
5. [OPPO、vivo、小米、荣耀联合上线 ADV 开发者身份验证](#item-5) ⭐️ 7.0/10
6. [欧盟《数字公平法案》草案泄露：拟限制成瘾性设计并要求游戏虚拟货币标明真实币值](#item-6) ⭐️ 7.0/10
7. [Epoch AI：中国六家 AI 企业营收约为 OpenAI 与 Anthropic 的十分之一](#item-7) ⭐️ 6.0/10
8. [比亚迪闪充机械臂在阿联酋亮相，充电功率达 1000 kW](#item-8) ⭐️ 6.0/10
9. [SnowLuma 收到腾讯律师函后宣布转为私有](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [未修复的 iOS 沙盒逃逸 PoC「worse\_query」公开，波及 iOS 27.2 及 27.3 beta](https://x.com/forcequitOS/status/2119475139528020218?) ⭐️ 8.0/10

11 月 8 日，研究者 forcequitOS 公开了名为 worse\_query 的零日沙盒逃逸概念验证代码，影响范围覆盖 iOS 26.0 至 26.7.2，以及 iOS 27.2（含 iOS 27.3 beta）。该 PoC 可访问系统路径并修改应用数据，作者虽已向苹果提交审核，但官方尚未发布修复。 一个可用的、已公开的逃逸手段同时影响当前正式版和活跃的测试版，意味着任何人都能在苹果修复前基于它继续开发，风险因此被显著放大。这也说明独立研究者突破 iOS 沙盒边界的速度仍快于官方修补速度，对安全团队、越狱相关开发者以及使用测试版系统的用户都有直接影响。 该漏洞是此前 bad\_query 研究的继任者，使用时需要目标应用配置 App Group，这在实际利用层面构成了限制。作者强调其仅供开发与研究用途、与越狱无关，但公开后已迅速衍生出 GestaltX 以及 KAMUI 一类 MobileGestalt 编辑器等下游工具。

telegram · zaihuapd · 11月9日 02:36

**背景**: iOS 将每个第三方应用限制在独立沙盒中，只能访问自身容器，无法读取其他应用的数据和大部分系统文件；突破这道边界通常是完整 iOS 利用链的第一步。App Group 本是苹果提供的正规机制，允许同一开发者的多个应用共享容器并通信，这也是该 PoC 需要预先配置 App Group 的原因。MobileGestalt 是 iOS 中保存设备配置与能力标志的子系统，因此能编辑它的工具可以修改区域代码、开启隐藏设置等。需要注意的是，沙盒逃逸并不等于越狱：它能带来容器外的文件访问能力，但本身并不提供内核代码执行，也不能绕过代码签名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/murk-sus/kamui-escape">GitHub - murk-sus/kamui- escape : KAMUI (神威) — iOS 27.x sandbox ...</a></li>
<li><a href="https://github.com/linnux-x/gestaltx">GitHub - linnux-x/ gestaltx : An MobileGestalt editor for iOS 27.x...</a></li>
<li><a href="https://senumy.com/ipa-library/gestaltx-ipa/">GestaltX IPA – MobileGestalt Editor for iOS 27 – Senumy</a></li>

</ul>
</details>

**社区讨论**: 社区反应迅速，开发者在数小时内就基于该原语构建出衍生工具，其中最典型的是 GestaltX 这类提供区域代码切换与设备预设的 MobileGestalt 编辑器。整体氛围既有对技术成果的热情，也伴随提醒用户谨慎对待建立在未修复漏洞之上的未经审核工具的声音。

**标签**: `#iOS security`, `#sandbox escape`, `#zero-day`, `#vulnerability disclosure`, `#mobile security`

---

<a id="item-2"></a>
## [AI 辅助设计的禽流感候选疫苗在动物试验中显示广谱保护](https://www.cam.ac.uk/stories/ai-developed-vaccines-against-viruses) ⭐️ 8.0/10

剑桥大学领衔的团队在 2026 年 11 月在线发表于《Cell Reports Medicine》的论文中报告，一款 AI 辅助设计的新型禽流感候选疫苗在小鼠和雪貂体内产生了广谱免疫应答与保护效果，表现优于研究中作为对照的、基于 WHO 候选疫苗病毒制备的制剂。团队下一步计划推进人体临床试验，验证其在人群中的表现，并为未来的应急使用做准备。 H5Nx 禽流感持续从禽类外溢到哺乳动物，因此一套能比传统“毒株匹配型”疫苗更快生成广谱保护性抗原的设计流程，有可能大幅缩短应对大流行威胁的反应时间。如果这种临床前优势在人体中得到验证，也将证明 AI 辅助抗原设计是可用于疫情准备的实用工具，而非纯学术探索。 团队指出，其通过计算设计的广谱抗原在自然界中并不存在，AI 辅助可加快应急情况下的抗原设计；对该工作的报道称其采用多抗原 panH5Nx 设计，结合计算与结构引导的 HA、NA 和 M2 抗原，以覆盖全球 H5Nx 的多样性。关键在于，这些结果仍属临床前阶段——对人的保护效果尚未得到证实，该候选疫苗仍需在临床试验中通过安全性与免疫原性检验。

telegram · zaihuapd · 11月9日 03:00

**背景**: 高致病性禽流感 H5N1 病毒——尤其是 2.3.4.4b 分支——已在野鸟和家禽中广泛传播，并多次感染哺乳动物（包括美国的奶牛），因此受到 WHO 与 CDC 的密切监测。传统流感疫苗的疫情准备依赖“候选疫苗病毒”（CVV）：由 WHO 合作中心和 CDC 筛选并分发给生产企业的种子毒株，使企业能够迅速启动生产。这类 CVV 是与流行毒株相匹配的，意味着随着病毒演化，保护范围可能变窄，而广谱的、经计算设计的抗原则正是为了弥补这一缺口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.genengnews.com/topics/infectious-diseases/bird-flu-vaccine-developed-using-ai-outperforms-current-stockpiled-vaccines-in-preclinical-tests/">Bird Flu Vaccine Developed Using AI Outperforms Current Stockpiled...</a></li>
<li><a href="https://www.cdc.gov/bird-flu/php/technical-report/h5n1-06052024.html">Technical Report: June 2024 Highly Pathogenic Avian Influenza ... | CDC</a></li>
<li><a href="https://cdn.who.int/media/docs/default-source/influenza/human-animal-interface-risk-assessments/influenza-at-the-human-animal-interface-summary-and-assessment--from-7-september-to-7-october-2026.pdf?sfvrsn=ffb871ef_3&amp;download=true">Influenza at the human-animal interface</a></li>

</ul>
</details>

**标签**: `#AI drug design`, `#vaccines`, `#avian influenza`, `#biomedical research`, `#public health`

---

<a id="item-3"></a>
## [谷歌发布 TPU 8tx 与 TPU 8i Max，加速挑战英伟达](https://www.bloomberg.com/news/articles/2026-11-09/google-escalates-nvidia-rivalry-with-new-versions-of-its-tpu-systems) ⭐️ 8.0/10

谷歌宣布推出两款新的张量处理单元（TPU）芯片——TPU 8tx 和 TPU 8i Max，打破了以往每两年才推出一款新处理器的节奏，转为面向不同场景的专用芯片布局。其中 TPU 8tx 面向政府机构和受严格监管、需处理机密数据的行业，并将与 AMD 芯片协同工作；TPU 8i Max 则针对超长上下文窗口的 AI 应用，把两颗 TPU 芯片集成在同一封装内，以提供更强算力和更大内存容量。 这一举动把 TPU 从单一的谷歌自用加速器扩展为覆盖云端 AI 训练、长上下文推理以及受监管/涉密部署的细分产品家族，从而加剧了与英伟达的竞争。在苹果、Meta、甲骨文和 Anthropic 等企业成为客户的背景下，谷歌正试图在 AI 算力仍是行业核心瓶颈之际，把 TPU 打造成英伟达 GPU 之外可信的替代方案。 TPU 8i Max 采用双芯片封装设计，以换取更强算力与更大内存，这一取舍明显是冲着上下文窗口极大的模型推理而非单纯的训练吞吐量去的。TPU 8tx 与 AMD 芯片搭配、并聚焦涉密工作负载，说明谷歌瞄准的是主权云与受监管行业的客户，而非通用商业 AI 训练市场。

telegram · zaihuapd · 11月9日 13:36

**背景**: 张量处理单元（TPU）是谷歌为机器学习负载定制的专用芯片（ASIC），2015 年首次在内部部署，此后通过 Google Cloud 向外提供；与作为通用并行处理器单独售卖硬件的英伟达 GPU 不同，TPU 主要是以云服务的形式被使用。模型的上下文窗口指它一次能处理的文本量（以 token 计），把窗口推到数十万甚至上百万 token 会显著抬高对底层芯片内存与带宽的要求。在晶体管微缩放缓的背景下，先进封装——把多个芯片裸片放进同一个封装——是芯片厂商当前提升性能的主要手段之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://segmentfault.com/a/1190000046072930">人工智能 - 长 上 下 文 大模型会让检索增强生成（RAG...</a></li>
<li><a href="https://www.51domino.com/blog/rag-vs-long-context-2026">RAG vs 长 上 下 文 窗 口 ：2026... - 51domino技术博客</a></li>

</ul>
</details>

**标签**: `#Google TPU`, `#AI chips`, `#Nvidia`, `#semiconductors`, `#AI infrastructure`

---

<a id="item-4"></a>
## [字节跳动发布 Seedream 5.5，支持百轮连续编辑与原生透明通道](https://seed.bytedance.com/zh/blog/%E7%94%9F%E6%88%90%E6%9B%B4%E7%9C%9F%E5%AE%9E-%E7%99%BE%E8%BD%AE%E7%BC%96%E8%BE%91%E6%9B%B4%E7%A8%B3%E5%AE%9A-seedream-5-5-%E5%8F%91%E5%B8%83) ⭐️ 7.0/10

字节跳动 Seed 团队发布图像创作模型 Seedream 5.5，支持对同一作品进行最多 100 轮连续编辑，并可原生生成带透明通道的素材。该模型同时提升了图像真实感与小字号文字渲染能力，正陆续上线即梦、豆包、豆包工作和火山方舟。 多轮编辑的稳定性和原生透明通道输出，正是生成式图像模型难以进入专业生产流程的关键短板，这两点的改善让模型更接近影视、设计和办公场景的实际可用状态。字节称其在影视、办公场景的可用率达到上一版本的两倍以上，而借助豆包、即梦的分发，这一能力可以触达规模极大的普通用户群体。 据火山引擎的发布信息，Seedream 5.5 支持像素级编辑、多轮一致性和原生 RGBA 透明输出，按输入/输出图片计费、文本 token 免费，一张 2K 方图的编辑成本约 0.28 元，比此前便宜约 60%、速度提升约 40%。字节并未公布标准化的基准测试数据，因此真实感与可用率的说法目前仍基于其自有的评测结果。

telegram · zaihuapd · 11月9日 08:34

**背景**: Seedream 是字节跳动 Seed 研究团队的图像生成与编辑模型系列，Seedream 5.5 属于该系列的迭代升级，而非全新架构。图像编辑模型长期存在“漂移”问题：每编辑一次细节就损失一点，因此能在同一张图上稳定完成 100 轮编辑是一个有意义的一致性里程碑。透明通道（alpha）输出之所以重要，是因为设计师需要可直接叠加到其他背景上的抠图素材，而不必再手工蒙版。火山方舟是字节面向开发者和企业提供的模型即服务平台，即梦和豆包则是面向普通用户的创作与对话应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5">Seed News - ByteDance Seed Team</a></li>

</ul>
</details>

**标签**: `#image-generation`, `#ByteDance`, `#Seedream`, `#generative-ai`, `#image-editing`

---

<a id="item-5"></a>
## [OPPO、vivo、小米、荣耀联合上线 ADV 开发者身份验证](https://mp.weixin.qq.com/s/ZiKBASSLzvsZ6WR2AUmFeg) ⭐️ 7.0/10

OPPO、vivo、小米、荣耀在中国大陆联合上线面向侧载应用的 Android 开发者身份验证（ADV）机制，并支持四方验证结果互认。已在四家开放平台注册上架的 APP 会自动提交验证，无需单独申请；未完成验证的应用在侧载安装时会弹出「未验证」提示，用户须手动确认后才能继续安装。 这四家厂商合计占据中国安卓手机市场的绝大部分份额，因此互认的验证标准实际上会成为第三方 APK 触达用户的事实性全国规则。它有望提升对恶意软件和诈骗的可追溯性，但也会给许多中国开发者和长尾应用分发所依赖的侧载渠道带来额外摩擦。 该机制的目标是为开发者与其应用建立可信关联，帮助用户判断应用来源与安全性，并由「移动智能终端生态联盟」统筹协调。值得注意的是，未验证应用并未被直接禁止安装——用户忽略提示后仍可继续安装——且该机制目前仅适用于中国大陆地区。

telegram · zaihuapd · 11月9日 11:44

**背景**: 中国安卓生态没有 Google Play，各家手机厂商各自运营应用商店，从网页侧载 APK 也是常见做法。与此同时，谷歌在 2025 年 8 月宣布，将从 2026 年起要求所有在安卓设备上分发应用的开发者完成身份验证，包括通过侧载或第三方商店在 Google Play 之外分发的情形。ADV 机制本质上是国产厂商对这一政策的平行回应，并针对由多个应用商店和直接 APK 分发主导的市场做了适配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://segmentfault.com/a/1190000047247951">android - Google突然“变脸“，2026... - SegmentFault 思否</a></li>
<li><a href="https://juejin.cn/post/7543362371340566571">谷歌 开 启 Android ...</a></li>
<li><a href="https://dayanzai.me/google-restricts-android-side-loading.html">Google 对 Android ...</a></li>

</ul>
</details>

**标签**: `#Android`, `#sideloading`, `#app-security`, `#China-tech`, `#mobile-ecosystem`

---

<a id="item-6"></a>
## [欧盟《数字公平法案》草案泄露：拟限制成瘾性设计并要求游戏虚拟货币标明真实币值](https://www.mlex.com/mlex/articles/2546584/digital-businesses-face-addictive-design-controls-under-draft-eu-consumer-law) ⭐️ 7.0/10

一份泄露的欧盟《数字公平法案》草案拟要求数字企业允许用户关闭自动播放、连续使用奖励等诱导强迫或过度使用的功能，并为在线订阅提供取消按钮、续费提醒和人工客服，在免费试用转为付费订阅前必须取得用户明确同意。草案还拟禁止面向未成年人的付费抽奖（开箱）、“付费获胜”机制和画像广告，并要求游戏虚拟货币标明真实币值，违规企业最高可被处以全球营业额 6% 的罚款；欧盟委员会定于 11 月 11 日正式提交该提案，同时改革消费者保护合作框架。 这可能是最早直接规范产品设计本身（而不只是信息披露）的法规之一，直指免费游戏、订阅类应用和社交平台背后的变现引擎，因此任何面向欧盟市场做消费级数字产品的团队都需要重新审视新手引导、付费墙和留存机制。最高达全球营业额 6% 的罚款使其合规压力可与《数字市场法案》和《通用数据保护条例》相比，而 11 月 11 日的提交时间表意味着 2026 年的产品路线图将面临实实在在的立法风险。 这些义务目前仍只是一份泄露的草案：文本还需经欧洲议会和欧盟各成员国批准，这一过程通常需要一年以上，且争议条款常被削弱或改写。对付费抽奖和“付费获胜”的禁令似乎专门针对未成年人而非全体玩家，而虚拟货币披露规则将迫使游戏在购买环节标明等值的真实货币金额。

telegram · zaihuapd · 11月9日 16:42

**背景**: 该草案针对的是所谓“暗黑模式”（dark patterns）——即刻意设计用来欺骗或施压用户的界面，这一术语由用户体验设计师 Harry Brignull 于 2010 年提出，自动播放、连续签到奖励和隐蔽的订阅取消入口都是典型例子。开箱（loot box）是一种消耗性虚拟道具，可随机开出其他虚拟物品，这套变现模式源自日本的扭蛋（gacha）游戏，批评者认为其性质接近赌博，尤其是面向儿童提供时。“付费获胜”（pay-to-win）指免费游戏中玩家可以花钱获得对他人不公平的竞争优势，2017 年《星球大战：前线 II》事件后此类做法遭到广泛批评。比利时、荷兰等部分欧盟国家已依据博彩法对开箱采取行动，但这将是首个在全欧盟层面以消费者保护而非博彩名义对其进行监管的尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_pattern">Dark pattern</a></li>
<li><a href="https://en.wikipedia.org/wiki/Loot_box">Loot box</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pay-to-win">Pay-to-win</a></li>

</ul>
</details>

**标签**: `#EU regulation`, `#consumer protection`, `#dark patterns`, `#game monetization`, `#tech policy`

---

<a id="item-7"></a>
## [Epoch AI：中国六家 AI 企业营收约为 OpenAI 与 Anthropic 的十分之一](https://cn.nikkei.com/china/ccompany/64644-2026-11-09-10-14-47.html) ⭐️ 6.0/10

Epoch AI 发布报告估算，OpenAI 与 Anthropic 的 AI 相关年化收入合计约 1050 亿美元，而字节跳动、阿里巴巴/Qwen、智谱/GLM、月之暗面/Kimi、DeepSeek、MiniMax 六家中国 AI 企业合计约 110 亿美元，约为前者的 10.5%。该估算依据不同月份的数据得出，其中字节跳动相关的年化收入约 40 亿美元，在上述中国企业中最高。 约 1:10 的收入差距直观说明，尽管中国模型在全球开发者中获得越来越多的使用，中国 AI 企业在商业化上仍明显落后于美国前沿实验室。这一对比也揭示了结构性差异：中国企业走的是开源、低价铺开的路线，而 OpenAI 与 Anthropic 依靠闭源、高毛利的模式获取收入。 Epoch AI 将开源权重分发和激烈的价格竞争视为中国模型被广泛采用的主要动力，并引用 OpenRouter 数据称，GLM-5 的调用量中有 75% 来自第三方服务，DeepSeek V4 Pro 也有约七成调用来自模型方之外。由于这些数字混合了不同月份的数据，且属于年化估算而非经审计的财务数据，应将其视为量级层面的比较，而非精确的市场份额。

telegram · zaihuapd · 11月9日 03:12

**背景**: Epoch AI 是一家追踪算力、模型能力与 AI 产业经济性的研究机构，由于多数实验室不披露详细营收数据，其估算被视为少数公开衡量 AI 收入规模的尝试之一，常被引用。“年化收入”是把最近一个月的收入乘以十二，反映的是运行速率而非全年总额。OpenRouter 是一个统一 API 平台，将开发者请求路由到来自众多提供方的数百个大模型，因此其流量数据为观察哪些模型真正被用于生产环境提供了难得窗口。此次对比出现的背景是，中国实验室正越来越多地发布可由第三方托管并低价转售的开源权重模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://www.codecademy.com/article/what-is-openrouter">What is OpenRouter ? A Guide with Practical Examples | Codecademy</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#China AI`, `#market analysis`, `#open-source LLM`, `#revenue`

---

<a id="item-8"></a>
## [比亚迪闪充机械臂在阿联酋亮相，充电功率达 1000 kW](https://m.mydrivers.com/newsview/1164193.html) ⭐️ 6.0/10

比亚迪近日在阿联酋首次公开展示了闪充机械臂，它可以自动完成打开充电口盖板、取枪、插枪、充电、拔枪、关盖板的全流程，车主把车停入车位后即可离开。现场演示的充电功率最高可达 1000 kW，配合第二代刀片电池，官方宣称可实现 5 分钟快速补能、9 分钟充满。 这一方案把超大功率充电与机器人自动化结合起来，指向“用户全程无需碰充电枪”的充电站形态，对车队运营、网约车以及海湾地区高温环境下的用车场景尤其有意义。如果 1000 kW 级别硬件能随光储充一体化站点一同推广，电动车补能时间将逼近燃油车加油体验，也会抬高竞争对手建设快充网络的门槛。 现场还展示了“一键泊充”功能，即车辆自主驶入车位后由机械臂接管充电，该站点采用光储充一体化方案。需要注意的是，这些数据来自官方展示而非第三方独立实测，实际能否跑到 1000 kW，还取决于车辆电池、剩余电量以及当地电网或储能缓冲的能力。

telegram · zaihuapd · 11月9日 05:20

**背景**: 比亚迪是一家总部位于深圳的汽车与电池制造商，其刀片电池采用长电芯的磷酸铁锂（LFP）结构，以安全性和空间利用率见长，第二代产品则主打更高的充电倍率。其汉 L 车型此前已宣传支持双枪 1000 kW 直流充电，因此这次亮相的机械臂本质上是在这套超快充平台上叠加的一层自动化装置。“光储充一体化”指的是站点把光伏发电、本地储能电池与充电桩结合起来，用以削峰填谷，缓解兆瓦级充电对电网造成的巨大瞬时负荷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BYD_Han_L">BYD Han L - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BYD_Auto">BYD Auto - Wikipedia</a></li>
<li><a href="https://www.byd.com/en">Electric Cars, Sedans and SUVs I BYD AUTO</a></li>

</ul>
</details>

**标签**: `#BYD`, `#EV charging`, `#robotics`, `#energy storage`, `#automotive tech`

---

<a id="item-9"></a>
## [SnowLuma 收到腾讯律师函后宣布转为私有](https://telegram.me/zaihuapd/45023) ⭐️ 6.0/10

SnowLuma 发布公告称已收到腾讯方面的律师函，项目将自 11 月 9 日起由公开仓库转为私有、不再对外公开，并向一路陪伴的用户道别。该项目此前已在用户协议中声明与腾讯无隶属关系、也未获授权。 这一关闭让机器人框架和 AI 智能体能够驱动真实 QQ 账号的较成熟桥接方案之一消失，依赖它搭建服务的小型开发者和爱好者不得不迁移或放弃原有方案。这也再次印证了中国聊天机器人生态中反复出现的模式：非官方协议实现始终面临平台方发起法律行动的威胁。 SnowLuma 通过 WebSocket、HTTP、WebUI、SDK 以及 MCP 等统一运行时，把桌面版 QQ 的原生会话翻译成标准的 OneBot v11 动作与事件，使下游框架可以把 QQ 当作任意兼容 OneBot 的平台来接入。由于它依赖逆向得到的原生会话而非官方 API，项目自身也提示此类工具可能违反平台条款，并给账号带来被限制或封禁的风险。

telegram · zaihuapd · 11月9日 14:57

**背景**: OneBot v11 是一套被广泛采用的标准化机器人接口，用于统一不同聊天平台的消息收发，让同一份机器人业务逻辑可以在多个框架之间移植。QQ 本身并未提供此类官方接口，因此社区项目长期通过逆向其协议或会话机制、挂钩 QQ 客户端来构建适配器，把 QQ 暴露为 OneBot 实现。这类适配器始终处于法律灰色地带——它们从未获得腾讯授权，而腾讯也多次施压要求其停止运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/SnowLuma/SnowLuma">GitHub - SnowLuma / SnowLuma : Next Remote Protocol Framework.</a></li>
<li><a href="https://snowluma.github.io/en/index.html">SnowLuma Docs · Bring native QQ sessions to your applications</a></li>
<li><a href="https://docs.astrbot.app/en/platform/aiocqhttp.html">Connect OneBot v 11 Protocol Implementations | AstrBot</a></li>

</ul>
</details>

**标签**: `#QQ`, `#OneBot`, `#chatbots`, `#legal-takedown`, `#reverse-engineering`

---