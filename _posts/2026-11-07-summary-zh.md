---
layout: default
title: "Horizon Summary: 2026-11-07 (ZH)"
date: 2026-11-07 23:03:30 +0000
lang: zh
report: default
---

> 从 159 条内容中筛选出 7 条重要资讯。

---

1. [GitHub 新架构 Rubicon 实现每秒 7200 次推送](#item-1) ⭐️ 8.0/10
2. [微软逐步终止甲骨文 AI 算力租赁协议](#item-2) ⭐️ 7.0/10
3. [Claude Code 被指在联网请求中泄露用户登录邮箱](#item-3) ⭐️ 7.0/10
4. [苹果披露人形机器人系统 HALO，三层架构由两个千问模型驱动](#item-4) ⭐️ 7.0/10
5. [传 Anthropic 下周启动 IPO 路演，目标 11 月 16 日当周挂牌](#item-5) ⭐️ 6.0/10
6. [土耳其借助 AI 从美国追回 100 件流失文物](#item-6) ⭐️ 6.0/10
7. [软银与 ABB 拟分拆中国业务，挽救 54 亿美元机器人交易](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [GitHub 新架构 Rubicon 实现每秒 7200 次推送](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) ⭐️ 8.0/10

GitHub 公布了一套代号为“Rubicon”的全新 Git 存储架构，目标是支撑数千个 AI 智能体同时操作同一个仓库。在内部压力测试中，单个仓库可承载 5000 个智能体并发协作，推送速率最高达到每秒 7200 次，同时读取延迟保持在较低水平。 智能体驱动的开发正在改变“繁忙仓库”的形态，而沿用二十年、服务人类开发者提交的引用式存储设计正逐渐成为瓶颈。如果 Rubicon 能按宣称的规模落地，GitHub 就能在不拖累人类开发者体验的前提下，承接这类高并发、机器生成的新型负载。 Rubicon 把可变的引用更新与不可变的 Git 对象分开处理：引用由名为 Ref-CAS 的复制日志服务管理，每次更新都是一次 compare-and-swap，只锁定涉及的引用，并在日志副本中多数派记录后即可见；而 Git 对象则存放在 Azure Blob Storage 中。一批可随时销毁的“虚拟副本”负责读写、无需加入 quorum，缓存从对象存储预热并在后台与真实状态对账；另有独立的压缩节点在后台合并 pack 包。目前该架构处于有限私有预览阶段。

telegram · zaihuapd · 11月7日 14:12

**背景**: 在标准 Git 仓库中，分支、标签等引用以纯文本文件形式存放在 .git/refs 目录下，所有对象被打包在单机文件中；每次推送都必须一致地更新这些引用，因此很难水平扩展。Ref-CAS 用一个基于多数派复制的日志加上 compare-and-swap 语义来替代它，这也是分布式数据库中用来解决写冲突的常见原语。GitHub 表示这套架构已在实际产品底层运行，意味着它是渐进式上线而非独立服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/">Inside GitHub’s new Git storage architecture - The GitHub Blog</a></li>
<li><a href="https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/">The bridge to agent-scale Git infrastructure - The GitHub Blog</a></li>
<li><a href="https://daily.dev/posts/inside-github-s-new-git-storage-architecture-ttbgyxfiu">Inside GitHub’s new Git storage architecture - daily.dev</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Git`, `#storage architecture`, `#distributed systems`, `#AI agents`

---

<a id="item-2"></a>
## [微软逐步终止甲骨文 AI 算力租赁协议](https://www.bloomberg.com/news/articles/2026-11-06/microsoft-is-winding-down-oracle-deal-to-rent-ai-cloud-capacity) ⭐️ 7.0/10

据报道，微软正逐步终止向甲骨文租用 AI 算力的协议，近几个月未续签合同，导致甲骨文股价一度下跌约 3%。知情人士称，甲骨文硬件使用老一代英伟达芯片，已不符合微软的要求。 此举凸显出 AI 云竞争越来越依赖最新一代 GPU，即便整体 AI 基础设施需求依旧强劲，较旧的租赁算力也可能贬值。这可能给甲骨文的 AI 云业务带来压力，同时强化超大规模云厂商快速更新硬件的周期。 甲骨文称 AI 基础设施需求依旧强劲，并于 9 月以高于原价 20% 的价格续签了四年前采购的 GPU 合同，微软则拒绝置评。该协议最初于 2023 年宣布，用于支撑 Bing 搜索的 AI 版本。

telegram · zaihuapd · 11月7日 02:00

**背景**: AI 算力租赁是指云厂商在其他公司自有数据中心无法及时满足需求时，向其出租 GPU 容量；微软此前曾用甲骨文算力补充 Bing 的 AI 工作负载。英伟达数据中心 GPU 已历经多代发展，例如 2020 年的 A100、2022 年的 H100 和 2024 年的 H200，新一代芯片在大模型训练和推理方面通常拥有更大显存和更高性能。因此，当客户的 AI 工作负载需要最新硬件时，较旧的 GPU 可能变得不再适用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mercatus-ai.com/blog/a100-vs-h100-vs-h200">A 100 vs H 100 vs H200: Complete Cost &amp; Performance Comparison for...</a></li>
<li><a href="https://enzu.com/nvidia-data-center-gpus.php">NVIDIA Data Center GPUs Compared: Best GPU for LLMs (2026)</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Oracle`, `#AI infrastructure`, `#Cloud computing`, `#Nvidia`

---

<a id="item-3"></a>
## [Claude Code 被指在联网请求中泄露用户登录邮箱](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 7.0/10

Anthropic 的 claude-code GitHub 仓库上的一份开发者报告显示，Claude Code 一直在未告知用户的情况下把用户登录邮箱填入对外网络请求，其中包括发往 Wikipedia 和美国证券交易委员会（SEC）的请求，报告者称这导致其每天收到大量垃圾与诈骗邮件。Anthropic 一名工程师确认了这一行为，称此前为解决 Claude 乱填作者名的问题才把登录邮箱放进模型上下文；2.1.317 版已加入拦截，但仍可被 Python 脚本绕过，公司计划在后续版本中从上下文中移除该邮箱。 Claude Code 是一款被广泛使用的智能体式编程工具，这种把用户账号标识悄悄发往第三方网站的设计，对每个使用它的开发者而言都是实实在在的数据泄露风险，而不只是报告者一人的问题。这也凸显了会联网、会填表单的 AI 智能体普遍面临的安全课题：凡是被放进模型上下文的内容都可能出现在对外请求中，而据报道存在的绕过方式说明这类泄露在事后很难彻底修补。 据报道，邮箱泄露问题最早在今年 7 月就有人报告；2.1.317 版新增的拦截在 Claude Code 运行 Python 脚本直接发起请求时仍可被绕过。根因在于把登录邮箱放进模型上下文这一有意的设计取舍，因此 Anthropic 计划在下一个版本中直接移除上下文里的登录邮箱，而不是仅仅过滤对外请求。

telegram · zaihuapd · 11月7日 08:09

**背景**: Claude Code 是 Anthropic 推出的智能体式编程工具，运行在终端中，可以代替用户执行命令、运行脚本以及抓取网页等操作。大语言模型只能依据其上下文窗口内的内容行动，而这一窗口能容纳的文本量有限，因此开发者常会向上下文补充额外信息以引导模型输出。在本例中，Anthropic 把用户登录邮箱加入上下文，是为了让模型填对作者或联系方式字段，但同一信息随后出现在了智能体发往外部网站的请求里。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Context_window">Context window - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI security`, `#privacy`, `#Claude Code`, `#AI agents`, `#data leakage`

---

<a id="item-4"></a>
## [苹果披露人形机器人系统 HALO，三层架构由两个千问模型驱动](https://weibo.com/1642634100/RqjjGllvw) ⭐️ 7.0/10

苹果研究团队 11 月 4 日在预印本平台 arXiv 提交题为《Perceptive Humanoid Motion from Simulation》的论文，披露了人形机器人自主控制系统 HALO，该系统以语言指令和第一视角图像为输入完成任务编排与全身动作执行。HALO 采用三层架构：上层用千问 Qwen3.6-35B-A3B 负责任务编排，中层用 Qwen3.5-2B 生成动作，底层是经强化学习训练的动作跟踪器，并已在宇树 G1 机器人上完成验证，数据生成、模型训练与部署代码均已公开。 这项工作显示大型消费科技公司正把大语言模型当作人形机器人的“规划大脑”，并与仿真训练出的底层控制相结合，而这套组合正逐渐成为通用机器人自主能力的主流路线。团队公开了完整的数据生成、训练与部署流程，显著降低了其他实验室复现和扩展该方法的门槛；同时实验选用了市售的宇树 G1 而非自研硬件，使结果在同领域之间更具可比性。 该系统把高层推理与底层控制解耦：大参数量的千问模型依据语言指令和图像进行任务排序，小参数量千问模型将其转化为具体动作，再由强化学习训练的动作跟踪器在真机上执行，并演示了在陌生真实室内房间中的仿真到现实迁移。据报道其在 G1 上的成功率约为 91%，相关代码已在苹果公开的 ml-halo 代码仓库中发布。

telegram · zaihuapd · 11月7日 13:35

**背景**: 仿真到现实迁移（sim-to-real）指的是先在物理仿真器中训练控制策略，再部署到真实硬件上。这是机器人学习领域广泛采用的范式，因为仿真可以进行真机无法承受的大规模并行试错，难点在于仿真物理与真实世界永远存在差距。人形机器人的全身控制之所以困难，是因为双足机器人必须在移动时协调数十个关节以保持平衡，因此研究者常把问题拆成一个“想做什么”的慢速规划器和一个“保持身体稳定”的快速跟踪器。在这项工作中，规划器是一个大语言模型，这种由 LLM 把自然语言指令拆解为可执行步骤的设计正变得越来越常见。实验所用的宇树 G1 是杭州宇树科技推出的紧凑型双足人形机器人，因其价格相对低廉而被广泛用作研究平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/apple-aiml-research/ml-halo">GitHub - apple-aiml-research/ml-halo: HALO: Perceptive ...</a></li>
<li><a href="https://ai.42how.com/en/article/ee6a8f15-db79-4091-9a86-3bc31de6c02f">Apple Integrates Humanoid Perception Into Simulation for Zero ...</a></li>
<li><a href="https://www.gate.com/news/detail/apple-discloses-halo-robot-control-system-with-91-success-rate-on-november-25471644">Apple Discloses HALO Robot Control System with 91% Success ...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#sim-to-real`, `#humanoid-robots`, `#Qwen`, `#Apple-research`

---

<a id="item-5"></a>
## [传 Anthropic 下周启动 IPO 路演，目标 11 月 16 日当周挂牌](https://www.theinformation.com/briefings/anthropic-proceed-ipo-roadshow-next-week) ⭐️ 6.0/10

一份 Telegram 科技资讯摘要援引匿名知情人士称，Anthropic 计划于下周启动 IPO 路演，并拟在 11 月 16 日当周、美国感恩节假期之前挂牌上市。该消息还称，公司可能寻求低于此前传出的 1.5 万亿美元估值，而按该估值原本预计募资逾 800 亿美元。 若消息属实，Anthropic 上市将成为史上规模最大的 AI 相关 IPO 之一，也是检验公开市场投资者对前沿 AI 实验室兴趣的标志性事件，并会对 OpenAI 等同行以及更广泛的 AI 基础设施产业链产生连带影响。若最终估值下调，则意味着近期 AI 股票的剧烈波动正开始压缩一级市场的估值预期。 该说法来自一份简短的资讯摘要，没有具名信源，也未提及承销商、上市文件或交易所等细节，更无一手报道佐证，因此 1.5 万亿美元估值和 800 亿美元募资额应被视为未经证实，且相对于常规 IPO 规模而言异常之高。摘要虽标注原始来源为 The Information 与新浪网，但这些数字本身尚未获得独立确认。

telegram · zaihuapd · 11月7日 01:27

**背景**: IPO 路演是公司在上市前与承销商一同向机构投资者推介股票的营销行程，通常持续一到两周，之后股票才开始交易。Anthropic 是一家以 AI 安全为宗旨的公司，开发 Claude 系列大语言模型，与 OpenAI 和谷歌形成竞争；该公司此前一直依靠私募资本融资，因此公开上市将意味着从风险投资转向公开市场融资。

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#business/finance`, `#unverified news`

---

<a id="item-6"></a>
## [土耳其借助 AI 从美国追回 100 件流失文物](https://www.artnews.com/art-news/news/turkey-uses-ai-tech-100-looted-antiquities-us-1234804634/) ⭐️ 6.0/10

土耳其文化部在伊斯坦布尔考古博物馆展出了约 200 件从美国追回的文物，其中重点包括 1960 年代在布尔本古城遭盗掘的青铜时代雕像，以及 44 件公元前 700 至 480 年的陶制建筑板。此次追索综合运用了铅同位素分析、模具形状比对，以及 2025 年启用的 AI 平台 TraceART——该平台会扫描全球拍卖网站和社交媒体以发现被非法交易的文物。 这是 AI 在软件与科研之外领域的一次具体落地，表明自动化的全网监测能够切实加快文物追索进程。如果这一做法得到推广，可能会改变博物馆、拍卖行和海关对文物来源进行尽职调查的方式——这一领域过去长期依赖缓慢的人工考证。 其技术路径是混合式的：铅同位素分析为金属器物的矿石来源建立“指纹”，模具形状比对把铸造器物关联到特定作坊，而 AI 层只负责在拍卖网站和社交媒体上缩小可疑拍品的范围。这些线索仍需通过科学检测以及法律和外交程序加以确认，因此该平台加快的是“发现”环节，而非直接证明来源。报道称，自 1980 年以来土耳其已追回逾 26700 件文物。

telegram · zaihuapd · 11月7日 03:43

**背景**: 文物走私难以监管，因为被盗文物往往在多年后带着薄弱的来源文件出现在合法拍卖会上，因此“来源”（provenance，即一件器物有据可查的流传历史）是任何追索主张的核心。铅同位素分析是一种成熟的考古测年与溯源技术：由于不同矿区的铅同位素比值存在差异，将器物的同位素特征与已知矿藏数据库比对，可以推断其金属原料的产地。模具形状比对与类型学比对对铸造器和陶器起到类似作用，可将其关联到已知作坊或遗址组合。TraceArt 这类平台的目标，就是把第一轮筛查自动化——将拍卖信息与社交媒体内容同失窃记录和已知器物类型数据库进行比对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://traceart.app/index.en.html">TraceArt | Cultural property provenance verification</a></li>
<li><a href="https://link.springer.com/article/10.1007/s12520-009-0013-4">Lead isotopes and archaeometallurgy | Archaeological and...</a></li>

</ul>
</details>

**标签**: `#AI`, `#cultural heritage`, `#artifact repatriation`, `#archaeology`, `#machine learning`

---

<a id="item-7"></a>
## [软银与 ABB 拟分拆中国业务，挽救 54 亿美元机器人交易](https://www.bloomberg.com/news/articles/2026-11-07/softbank-abb-weigh-china-carve-out-to-salvage-robotics-deal) ⭐️ 6.0/10

软银与 ABB 正考虑把 ABB 机器人业务的中国部分分拆为一个股权结构不同的独立实体，以挽救本周四被中国外商投资安全审查工作机制办公室叫停的 54 亿美元收购交易。据知情人士称，该方案由软银主导推进，但可能失败，ABB 同时也在评估其他选项，包括另寻买家。 这笔交易被叫停，说明中国的安全审查能够深度介入大型跨境工业自动化并购；如果分拆方案成功，可能成为外资出售在华资产的一种模板。若交易最终失败，软银进军机器人领域的布局将受挫，ABB 的中国机器人业务也将陷入悬而未决的状态，而工业自动化正日益被视为战略敏感领域。 拟议架构是把中国业务装入一个拥有不同股权权利的独立实体，从而将这部分中国资产与交易其余部分切割开来。据报道，该中国机器人业务估值约 20 亿至 30 亿美元，约为交易总价的一半，ABB 与软银均拒绝置评。

telegram · zaihuapd · 11月7日 11:24

**背景**: ABB 是一家瑞士-瑞典工业巨头，其机器人部门生产工厂自动化机械臂与系统，而软银近年一直在构建机器人与自动化资产组合。中国的外商投资安全审查由跨部门工作机制执行，当交易涉及国家安全或关键技术时，可叫停外资收购本国企业，或收购在华业务规模较大的外国企业。由于标的有相当规模的在华业务，这笔交易落入该安全审查范围，而非普通的反垄断申报程序。

**标签**: `#robotics`, `#M&amp;A`, `#china-regulation`, `#industrial-automation`, `#foreign-investment`

---