---
layout: default
title: "Horizon Summary: 2026-11-11 (ZH)"
date: 2026-11-11 23:04:30 +0000
lang: zh
report: default
---

> 从 191 条内容中筛选出 8 条重要资讯。

---

1. [Stripe 宣布将 OpenRouter 并入旗下，构建 AI 经济基础设施](#item-1) ⭐️ 8.0/10
2. [报道称 Alice Huang 协助 24 万颗被禁英伟达芯片流入中国](#item-2) ⭐️ 8.0/10
3. [美国 FCC 批准 SpaceX 收购全美 800 兆赫兹频谱](#item-3) ⭐️ 7.0/10
4. [字节跳动筹备类 Muse 智能体，拟投 700 亿美元加码 Seedance](#item-4) ⭐️ 7.0/10
5. [微软专利拟付费使用闲置设备训练 AI](#item-5) ⭐️ 6.0/10
6. [苹果支持社区论坛将于 2026 年 11 月 20 日永久关闭](#item-6) ⭐️ 6.0/10
7. [腾讯元宝搜索正式上线：基于大模型重构搜索链路](#item-7) ⭐️ 6.0/10
8. [AMD 用 AI 驱动的 Mext 把冷内存页换到 NVMe，宣称可省 83% 服务器成本](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Stripe 宣布将 OpenRouter 并入旗下，构建 AI 经济基础设施](https://x.com/stripe/status/2120240651778355306) ⭐️ 8.0/10

Stripe 在 X 上宣布 OpenRouter 已并入旗下，称这是其为 AI 搭建经济基础设施的一部分，将与企业一起探索新模型、优化 token 路由与用量。公告未披露交易金额、交易结构或时间表。 OpenRouter 是被广泛使用的大模型网关，可在数百个模型之间路由请求；将其与 Stripe 的支付和计量体系结合，可能把模型接入、用量计量与计费整合到同一层。这会影响依赖多模型路由的 AI 应用开发者，也会影响在该类市场上争夺流量的模型提供商。 Stripe 强调的重点是模型探索、token 路由与用量优化，但公告没有给出任何技术或商业细节，例如定价是否调整、API 是否延续、整合计划如何。OpenRouter 的路由决策依赖价格、延迟、可用性等实时市场数据，而这正是计费平台可以变现的用量信号。

telegram · zaihuapd · 11月11日 09:45

**背景**: OpenRouter 本身不是大模型，而是一个 API 网关：它把多家模型提供商聚合到一个平台，让开发者用一个 API Key、一种调用格式就能访问不同模型，并在数百个模型间切换或自动路由。Token 路由指的是决定每个请求交由哪个模型或后端处理，在成本、延迟与质量之间做权衡。Stripe 近年将自己定位为 AI 的&quot;经济基础设施&quot;提供方，刚推出一大批围绕 AI 计费、计量和智能体商业的新功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2090100975419778549">OpenRouter 是什么：一个 API 网关如何统一调用 500+ 个模型</a></li>
<li><a href="https://stripe.com/zh-us/newsroom/news/sessions-2026">Stripe 连发 288 项新品，完善 AI 经济基础设施</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#acquisitions`, `#Stripe`, `#OpenRouter`, `#LLM routing/billing`

---

<a id="item-2"></a>
## [报道称 Alice Huang 协助 24 万颗被禁英伟达芯片流入中国](https://www.tomshardware.com/tech-industry/policy/alice-huang-reportedly-instrumental-in-securing-over-usd7-5-billion-of-nvidia-ai-gpu-imports-during-three-year-relationship-with-jensen-huang-helped-move-240-000-banned-chips-into-china-mostly-h100-and-h200) ⭐️ 8.0/10

《The Information》的一项调查称，据传与英伟达 CEO 黄仁勋有私人关系的黄乐（Alice Huang）利用这层关系，在约三年时间里协助约 24 万颗受出口管制的英伟达 AI GPU（主要为 H100 和 H200）流入中国，相关进口金额约 75 亿美元。报道称这一网络的核心是 2023 年获得英伟达“首选云合作伙伴”地位的中国公司上海世纪利通，以及总部位于新加坡的云服务商 Megaspeed。 如果这一说法得到证实，其规模——25 万颗、价值数十亿美元的顶级加速卡——将使其成为已知规模最大的规避美国对华半导体出口管制的案例之一，可能引发国会审查、收紧对云服务合作伙伴和分销商的许可规则，并给整个 AI 硬件供应链带来新的合规负担。此事还直接冲击英伟达，而该公司的中国业务和政治处境本就承受着巨大压力。 报道描述了一个横跨中国和新加坡的公司网络，据称由黄乐、其丈夫和姐妹专门为采购英伟达芯片而搭建，芯片经由第三方云服务商转运，而非直接卖给中国买家。英伟达表示未发现其芯片被走私进入中国的证据，并称已就 Megaspeed 问题与美国政府沟通；Megaspeed 否认存在不当行为，称检查未发现违规，且上述指控尚未在法庭上得到证实。

telegram · zaihuapd · 11月11日 14:41

**背景**: 自 2022 年 10 月起、并在 2023 年 10 月进一步收紧后，美国商务部禁止在无许可证情况下向中国出口 H100、H200 等先进 AI 加速卡，而此类许可证通常不会获批。英伟达随后推出针对中国市场的降规版本（A800、H800、H20），但这些产品后来同样受到限制。由于中国境内对英伟达高端硬件的需求依旧巨大，于是出现了通过海外中间商、云租赁或壳公司采购芯片的灰色市场。“首选云合作伙伴”身份之所以重要，是因为它能让企业优先获得稀缺的英伟达 GPU 配额。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/09/megaspeed-nvidia-jensen-huang-alice-huang.html">What is Megaspeed ? Nvidia customer in spotlight after Jensen’s affair</a></li>
<li><a href="https://www.dw.com/en/megaspeed-and-the-battle-to-go-high-end-nvidia-chips-into-china/a-79909129">Megaspeed : Nvidia partner at the center of the spy affair</a></li>
<li><a href="https://www.rfi.fr/cn/%E5%9B%BD%E9%99%85/20261110-%E4%BF%A1%E6%81%AF%E6%8A%A5-%E8%8B%B1%E4%BC%9F%E8%BE%BEceo%E4%B8%8E%E6%B6%89%E8%B0%8D%E6%83%85%E4%BA%BA%E5%90%91%E4%B8%AD%E5%9B%BD%E8%BE%93%E9%80%81%E4%BA%8675%E4%BA%BF%E7%BE%8E%E5%85%83%E8%8A%AF%E7%89%87">《信息报》： 英 伟 达 CEO... - RFI - 法国国际广播电台</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI chips`, `#export controls`, `#China`, `#semiconductor policy`

---

<a id="item-3"></a>
## [美国 FCC 批准 SpaceX 收购全美 800 兆赫兹频谱](https://wap.cj.sina.cn/7x24/5206981) ⭐️ 7.0/10

美国联邦通信委员会（FCC）批准了 SpaceX 通过与 Grain Management 交易收购全美 800 兆赫兹频谱的申请，SpaceX 由此获得 546 组成对牌照，覆盖近乎全部美国人口。这意味着 SpaceX 在几乎所有市场都握有低频段资源，部分覆盖区域的频谱资源最高可达 89 兆赫兹。 低频段频谱是实现广域覆盖和室内穿透最经济的手段，因此这一批准实质性增强了 SpaceX 的 Starlink 手机直连卫星（direct-to-cell）野心，使其更接近成为全国性移动运营商。与此同时，Verizon、AT&amp;T 和 T-Mobile 均拒绝向 SpaceX 开放其网络，这可能使频谱所有权成为美国无线市场竞争的焦点。 这 546 组成对牌照属于频分双工（FDD）式的成对频块，上、下行各占一段信道；800 兆赫兹信号穿墙能力强，且几乎适配所有智能手机，因此 SpaceX 无需新硬件即可触达现有手机用户。代价在于容量：低频段信道承载的数据量远低于中频段或毫米波，因此这批频谱更适合基础覆盖与消息类业务，而非高速宽带。

telegram · zaihuapd · 11月11日 02:14

**背景**: 无线电频谱通常分为低、中、高频段：低频段（如 800 兆赫兹，大致覆盖 790–862 兆赫兹）传播距离远、穿透建筑能力强，但容量有限；中频段和毫米波则速度快但覆盖范围小。由于双向移动通信需要为上、下行分别提供通道，监管机构通常以“成对频块”的形式发放牌照，一个频块用于上行、另一个用于下行。美国的 800 兆赫兹频段历史上用于蜂窝通信和公共安全通信，FCC 曾花费多年对该频段进行重新配置，以避免对急救人员的通信造成干扰。因此，拥有全国性低频段牌照，是任何希望在不密集建站的情况下提供手机业务的运营商（无论卫星还是地面）的先决条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fcc.gov/general/800-mhz-spectrum">800 MHz Spectrum - Federal Communications Commission 800 MHz Cellular Service - Federal Communications Commission SpaceX buys 800 MHz spectrum to launch Starlink Mobile carrier What Is 800 MHz? Mobile Spectrum Explained 800 MHz Spectrum 800 MHz Spectrum for Private LTE &amp; 5G Networks | Black &amp; Veatch</a></li>
<li><a href="https://en.wikipedia.org/wiki/800_MHz_frequency_band">800 MHz frequency band - Wikipedia</a></li>
<li><a href="https://summitridgegroup.com/wp-content/uploads/Spectrum-Handbook-2018.pdf">The Spectrum Handbook 2018</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#FCC`, `#spectrum`, `#telecom`, `#satellite connectivity`

---

<a id="item-4"></a>
## [字节跳动筹备类 Muse 智能体，拟投 700 亿美元加码 Seedance](https://www.bloomberg.com/news/articles/2026-11-11/bytedance-prepares-muse-like-agent-in-push-to-close-ai-gap) ⭐️ 7.0/10

据报道，字节跳动计划在未来数周发布一款类似 Meta Muse 的 AI 助手，并将最多投入 700 亿美元打造其 Seedance 视频 AI 平台。联合创始人张一鸣在内部全员会上表示，至少要到 2029 或 2030 年才能在前沿领域与 Anthropic、OpenAI 比肩。 该计划表明，字节跳动正从 AI 视频生成的领先地位升级到更广泛的通用 AI 智能体竞赛，其资本投入规模可与美国顶尖实验室相提并论。若得以执行，这将加剧与 OpenAI、Anthropic 的竞争，并重塑 AI 智能体与创作类视频工具的市场格局。 据报道，张一鸣向字节跳动 AI 团队提出了该计划，并表示公司不主张依赖模型蒸馏来缩小差距。报道中的 700 亿美元投入专门用于 Seedance，而 2029 至 2030 年的时间点则被设定为达到前沿水平的目标。

telegram · zaihuapd · 11月11日 12:31

**背景**: Muse 是 Meta 于 2026 年 9 月 8 日发布的个人 AI 智能体，旨在代替用户执行长时间任务，而不是像聊天机器人那样只完成单轮问答。Seedance 是字节跳动的视频与音频生成模型，2026 年 7 月 31 日发布的 Seedance 2.5 可根据文本、图像和参考素材生成最长 30 秒、带同步音频的视频。模型蒸馏是一种将大型模型的知识迁移到小型模型的技术，常用于降低高性能模型的使用成本；字节跳动表示不主张依赖该技术，说明其更倾向于自研前沿模型训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muse_%28AI_agent%29">Muse (AI agent) - Wikipedia</a></li>
<li><a href="https://www.seedance.tv/seedance-2-5">Seedance 2.5 AI Video Generator — Up to 30s Video ... | Seedance</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>

</ul>
</details>

**标签**: `#ByteDance`, `#AI agents`, `#OpenAI`, `#AI video`, `#industry news`

---

<a id="item-5"></a>
## [微软专利拟付费使用闲置设备训练 AI](https://www.techspot.com/news/114499-microsoft-patent-describes-paying-you-train-ai-idle.html) ⭐️ 6.0/10

微软提交了一项专利，描述了一套可监测已授权用户设备（包括服务器、台式机和智能手机）的系统，在设备低负载或闲置时向其分发 AI 训练任务。作为回报，参与用户可获得现金、软件商店积分或模型优先体验等补偿。 该专利表明微软至少在探索利用消费级设备的富余算力来训练 AI，这可能成为昂贵且耗电的数据中心 GPU 之外的一种廉价补充。如果真正落地，普通玩家的硬件（以及他们的电费）将被纳入 AI 训练的供应链，这与分布式计算项目长期倡导的思路一脉相承。 据对该申请的报道，专利名为《Opportunistic Micro-training on Edge Devices Using Spare GPU Utilization》（利用闲置 GPU 在边缘设备上进行机会式微训练），由 Microsoft Technology Licensing 于 2025 年 4 月提交，描述了将大型训练任务拆分为微任务的做法。系统会依据 CPU、GPU、内存、温度和功耗等指标判断设备可提供的资源，再由中心服务汇总回收的结果——但目前没有任何迹象表明相关产品即将推出。

telegram · zaihuapd · 11月11日 04:45

**背景**: 训练大型 AI 模型通常需要网络互联紧密的数据中心 GPU 集群，因为把模型拆分到多台机器上对网络延迟和硬件差异极其敏感。分布式与联邦式方法试图绕开这一限制，把训练拆成可独立计算、事后合并的小块，例如微任务或梯度更新。此类专利在业界很常见，往往最终并不会变成产品，主要反映公司在探索哪些方向——在这里就是如何把消费级硬件上本会浪费的算力变现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://videocardz.com/newz/microsoft-could-pay-gamers-for-using-spare-gpu-capacity-to-train-ai">Microsoft patent describes turning idle gaming GPUs into paid ...</a></li>
<li><a href="https://explainx.ai/blog/microsoft-patent-idle-gaming-gpu-micro-training-us-20260349820-2026">Microsoft Idle GPU Patent: Pay Gamers to Train AI? | explainx ...</a></li>
<li><a href="https://wccftech.com/microsoft-could-pay-gamers-to-train-ai-using-their-idle-gpus-new-patent-reveals/">Microsoft Could Pay Gamers to Train AI Using Their Idle GPUs ...</a></li>

</ul>
</details>

**标签**: `#AI training`, `#distributed computing`, `#Microsoft`, `#patents`, `#crowdsourcing`

---

<a id="item-6"></a>
## [苹果支持社区论坛将于 2026 年 11 月 20 日永久关闭](https://www.macrumors.com/2026/11/10/apple-support-community-closing-november-20/) ⭐️ 6.0/10

苹果宣布 Apple Support Community 论坛将于 2026 年 11 月 20 日永久关闭，目前站点已转为只读状态，不再接受新帖和回复。苹果对媒体表示，这一决定是在评估自身策略与客户需求后作出的，而 11 月 20 日之后论坛内容是否保留目前尚不明确。 该论坛是互联网上历史最悠久的厂商支持社区之一，它的关闭意味着大量由用户贡献的排障知识档案将失去依托，而许多苹果用户多年来正是依赖这些内容解决问题。这也反映出苹果在点对点用户互助支持上的策略转向，可能把用户推向官方支持渠道、Reddit 或第三方站点。 该社区的历史至少可追溯到 1998 年，最初名为 Apple Tech Exchange，后来曾叫 Apple Discussions，并于 2011 年以现名重新上线，引入了用户个人资料和声誉系统。由于站点已只读且档案去留未确认，有观察者建议用户尽快保存有价值的帖子。

telegram · zaihuapd · 11月11日 05:45

**背景**: Apple Support Community 是一个由苹果用户互相帮助排查 Mac、iPhone 及软件问题的网络论坛，而非由苹果员工坐镇的官方客服渠道。这类由厂商运营的社区论坛在 1990 年代末逐渐流行，用以分摊支持成本；此类内容常在高技术问题的搜索结果中排名靠前，因此其消失意味着相当一部分“集体记忆”的流失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/11/10/end-of-an-era-apple-support-community-forums-will-permanently-close-on-november-20/">End of an era: Apple Support Community forums to... - 9to5Mac</a></li>
<li><a href="https://www.macworld.com/article/3282552/apple-suddenly-shutters-its-support-community-forums-and-wont-say-why.html">Apple suddenly shutters its Support Community forums and won ...</a></li>
<li><a href="https://tech.yahoo.com/ai/apple-intelligence/articles/apple-shutting-down-support-community-185824210.html">Apple Is Shutting Down Its Support Community Forums After 28 ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#community-platforms`, `#tech-news`, `#customer-support`, `#platform-shutdown`

---

<a id="item-7"></a>
## [腾讯元宝搜索正式上线：基于大模型重构搜索链路](https://finance.sina.com.cn/roll/2026-11-11/doc-iniyixxw5252798.shtml) ⭐️ 6.0/10

11 月 11 日，腾讯全新搜索产品“元宝搜索”正式上线，用户可通过 so.qq.com 使用，也能在最新版 QQ 浏览器中切换体验。该产品基于元宝大模型重构搜索链路，覆盖全网网页与学术文献，接入 157 个权威信源，并可搜索公众号等腾讯生态内容。 此举让腾讯正式加入中国日益激烈的 AI 搜索竞争，大模型搜索正被定位为传统链接式结果的替代方案。腾讯的差异化优势在于独家的公众号内容资源，这是竞争对手难以索引的语料，可能改变腾讯生态内用户获取信息的方式。 搜索结果优先展示权威机构与官方来源，广告被单独标注为“相关广告”且可收起，这在中国搜索产品中是较为少见的透明度设计。输入方式为多模态，支持文字、语音和拍照搜索，而非仅限文本输入。

telegram · zaihuapd · 11月11日 09:00

**背景**: 元宝是腾讯面向消费者的 AI 助手应用，于 2024 年 5 月 30 日首次发布，基于腾讯自研的混元大模型系列，同时整合了 DeepSeek 等模型的能力，功能涵盖智能对话、AI 搜索、文档总结、写作与多模态交互。元宝搜索把这一助手延伸为独立的搜索入口，既部署在自有域名上，也嵌入到腾讯长期运营的 QQ 浏览器中。所谓“157 个权威信源”，指的是一份经过筛选的官方与机构站点白名单，模型在生成答案时会优先采用这些来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiwiki.ai/wiki/tencent_yuanbao">Tencent Yuanbao - AI Wiki</a></li>
<li><a href="https://baike.baidu.com/en/item/Yuanbao/1845971">Yuanbao（An AI assistant application launched by Tencent ...</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#AI Search`, `#LLM`, `#Product Launch`, `#China Tech`

---

<a id="item-8"></a>
## [AMD 用 AI 驱动的 Mext 把冷内存页换到 NVMe，宣称可省 83% 服务器成本](https://www.theregister.com/systems/2026/11/11/amd-where-were-going-we-dont-need-as-much-dram/5308953) ⭐️ 6.0/10

AMD 把收购来的 Mext 技术产品化为一套纯软件的内存分层方案，用 AI 模型在操作系统或应用察觉之前，把冷内存页在 DRAM 与更便宜的 NVMe 闪存之间换入换出。AMD 称用闪存替代一半 DRAM 仍能保留最高 99% 的性能，最多可把企业服务器成本降低 83%，且 Mext 需在购买 Epyc 服务器时一并购买授权。 DRAM 价格高企与供应紧张已成为制约服务器成本结构的主要因素，一层能让闪存承接冷数据的软件有可能改变企业在更新集群时的内存规划方式。如果这些说法成立，它还会强化 AMD 的主张：Epyc 平台加 Mext 相比单纯多买内存能带来更好的总体拥有成本。 Mext 以单一安装包形式提供，包含三个组件：MEXT 驱动、AI 引擎和 MEXT 守护进程，并在 AMD 的服务器路线图中与基于 LPDDR5X 的 &quot;Verano&quot; 内存以及 CXL 3.1 分层方案并列。这些醒目的数字均为厂商估算，尚无独立基准测试验证，而且该方案需要随 Epyc 硬件捆绑购买额外软件授权，并非免费功能。

telegram · zaihuapd · 11月11日 11:15

**背景**: 内存分层是一个已有概念：当内存使用率上升到一定程度（VMware 的实现大约在 80% 使用率时启动），虚拟化层会把不活跃的“冷”页面从高速 DRAM 迁移到较慢的 NVMe 存储上，把热数据保留在内存中。代价是延迟——一次 DRAM 访问大约在 100 纳秒量级，而从现代 NVMe SSD 随机读取 4K 数据大约需要 20–70 微秒，慢了几个数量级。AMD 的不同之处在于用 AI 模型预测哪些页面即将被需要，从而主动而非被动地迁移。这一方案出现的背景是 DRAM 变得异常昂贵且供应紧张，让“少买内存”突然成为一个有吸引力的选项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/software/mext.html">AMD MEXT Predictive Memory Software</a></li>
<li><a href="https://mashdigi.com/intl/en/amd-epyc-mext-technology-reduce-tco-dram-cost/">Solving the Memory Shortage and Price Crisis: How AMD’s MEXT ...</a></li>
<li><a href="https://simplyblock.io/glossary/nvme-latency/">NVMe Latency: Typical Numbers and What Drives Them | simplyblock</a></li>

</ul>
</details>

**标签**: `#AMD`, `#memory tiering`, `#NVMe`, `#AI`, `#server cost`

---