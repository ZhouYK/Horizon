---
layout: default
title: "Horizon Summary: 2026-11-20 (ZH)"
date: 2026-11-20 23:04:23 +0000
lang: zh
report: ai
---

> 从 184 条内容中筛选出 10 条重要资讯。

---

1. [Anthropic 数学家 Levent Alpöge 称与 Claude 共同证明黎曼猜想](#item-1) ⭐️ 9.0/10
2. [拉维·瓦基尔宣布广义黎曼猜想的“纯人类”证明草案](#item-2) ⭐️ 8.0/10
3. [黑客利用自主 AI 智能体 Cairn 发现零日漏洞并接管服务器](#item-3) ⭐️ 8.0/10
4. [谷歌以每分钟约 6 美元开放 Genie 4 可玩世界生成 API](#item-4) ⭐️ 8.0/10
5. [OpenAI 助力 AMD 旗舰 GPU 设计 PPA 提升 14%](#item-5) ⭐️ 7.0/10
6. [腾讯开源 Hy4：7700 亿参数 MoE 模型，支持超 100 万 token 上下文](#item-6) ⭐️ 7.0/10
7. [OpenAI 的 dots 助手走出聊天框，自带云端电脑](#item-7) ⭐️ 7.0/10
8. [ChatPRD 创始人 Claire Vo 因代币欺诈关闭免费试用](#item-8) ⭐️ 6.0/10
9. [《自然》评论文章探讨 AI 缩小癫痫诊疗差距的潜力与风险](#item-9) ⭐️ 6.0/10
10. [特朗普考虑惩罚在海外建设 AI 数据中心的美国公司](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 数学家 Levent Alpöge 称与 Claude 共同证明黎曼猜想](https://simonwillison.net/2026/Nov/20/levent-alpoge/) ⭐️ 9.0/10

2026 年 11 月 20 日，数学家 Levent Alpöge 发布了一篇个人短文（alpo.ge/remark.pdf），声称他与 Anthropic 的 Claude 共同发现了黎曼猜想的证明，且该方法可推广至广义黎曼猜想，他并预计假以时日还能解决扩展黎曼猜想。他还声称这些论证已在无额外假设的前提下完成形式化，据《科学美国人》报道，形式化后的证明文稿超过 25 万页。 黎曼猜想自 1859 年提出以来始终悬而未决，被普遍视为数学中最著名的未解难题，因此若证明成立，将重塑数论的诸多分支，并一举证明 AI 辅助数学发现能够达到最高水准。而机器可检验的形式化更将成为证明助手的里程碑，说明大模型生成的论证可以被推进到内核验证的严格程度，而不只是停留在非形式化的草稿阶段。 该声明完全以个人 PDF 形式自行发布，既未经同行评审，也未投稿期刊或获得独立确认，而且作者本人对扩展黎曼猜想的表述只是“预期”而非已完成的结果。最关键的检验点在于形式化本身：如果该证明确实用 Lean 之类的证明助手编码，那么验证工作就退化为对内核进行类型检查，这比用传统方式审阅 25 万页文字要快得多，也更能一锤定音。

rss · Simon Willison · 11月20日 16:30

**背景**: 黎曼猜想由波恩哈德·黎曼于 1859 年提出，断言黎曼 ζ 函数的所有非平凡零点实部均为二分之一；其重要性在于这些零点的位置精确控制着素数如何分布。广义黎曼猜想把同一断言推广到由狄利克雷特征构造的狄利克雷 L 函数上，而扩展黎曼猜想则将其应用于数域的戴德金 ζ 函数，乃至更一般的整体 L 函数。形式化验证是指把证明编码进证明助手，由计算机逐步检查直至公理层面的每一步推理，从而不给隐藏漏洞或未声明假设留下空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://cacm.acm.org/research/formally-verified-mathematics/">Formally Verified Mathematics – Communications of the ACM</a></li>

</ul>
</details>

**标签**: `#AI for mathematics`, `#Riemann Hypothesis`, `#Anthropic Claude`, `#LLM reasoning`, `#formal verification`

---

<a id="item-2"></a>
## [拉维·瓦基尔宣布广义黎曼猜想的“纯人类”证明草案](https://simonwillison.net/2026/Nov/20/ravi-vakil/) ⭐️ 8.0/10

拉维·瓦基尔在其 Math 216 博客上宣布，亚历山德罗·马苏洛（Alessandro Masullo）提出了一份广义黎曼猜想的证明，而布莱恩·康拉德（Brian Conrad）已对此密切审查数月，并给出了大量反馈意见，目前正被纳入修改。由于目前看来结果站得住脚，瓦基尔决定立刻公开当前这份尚未打磨的草稿，而不是按原计划先花约一年时间把马苏洛请到斯坦福完善写作后再公布。 广义黎曼猜想是数学中最核心的未解难题之一：一个正确的证明将解决一大类 L 函数上的黎曼假设，并对素数分布、解析数论以及涉及密码学的算法产生连锁性影响。如果该证明成立，它将成为数十年来数论领域最重要的成果之一。 这一公告明确是对草稿的“仓促发布”，瓦基尔本人称该草稿本需要一年的打磨时间；他还特别强调这项工作完全由人类完成、没有 AI 参与，这很可能是为了预先澄清近期一些 AI 辅助证明声明引发的猜测。康拉德的审阅仅被描述为“目前看起来不错”，因此该证明尚未得到更广泛数学界的验证。

rss · Simon Willison · 11月20日 19:21

**背景**: 黎曼假设由波恩哈德·黎曼于 1859 年提出，猜想黎曼 ζ 函数的所有非平凡零点都位于实部为 1/2 的竖直直线上；若成立，就能精确刻画素数的分布规律。广义黎曼假设则把同一命题从 ζ 函数推广到更广泛的一类全局 L 函数（包括狄利克雷 L 级数），这些函数编码了等差数列中的素数等算术信息。目前数论中大量定理只能在“假设 GRH 成立”的条件下得到证明，因此一个无条件证明将一次性升级一大批结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/">Hurried Announcement: Alessandro Masullo GRH | Math 216 ...</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#Generalized Riemann Hypothesis`, `#number theory`, `#proof`, `#research announcement`

---

<a id="item-3"></a>
## [黑客利用自主 AI 智能体 Cairn 发现零日漏洞并接管服务器](https://news.google.com/rss/articles/CBMiugFBVV95cUxPZGVzUFN6Uk45UC1rS1JqSUc0b2tyLWhHSXR2a2hKX08xWlZjcW9veHpJM2FRQUVuM1JRSk5LSEpZSkpBa2RkVklXTHBvclFHN09oa3dYMjBDeU9ScTRWelNYeW1fdk1iVDFFaVcxSVp1ZDNtOER5aDdnblhYelZMeWxzZjVIYkFYU2haQU1kVVhTV1l6dFdaeG0zMkI3MElBZURWNFkwUXFJeW4yVTBDYm9TQUFwNWQzM1E?oc=5) ⭐️ 8.0/10

攻击者利用开源自主 AI 渗透测试框架 Cairn，在一款名为 MONAI Label 的开源医学影像 AI 应用中发现了零日漏洞，并利用该漏洞完全控制了某所大学的服务器。据 BleepingComputer 与 The Register 报道，此次入侵基本在没有人工干预的情况下完成，并被归因于一个与中国有关的攻击组织。 这是首批被公开记录的案例之一：AI 智能体自主完成了从漏洞发现到完全接管服务器的完整链条，大幅降低了发动高级入侵的技术门槛。若这一模式被复制，防御方——尤其是大学、医疗机构等资源有限的单位——将不得不面对以机器速度推进的多阶段攻击，而非以往按人力节奏展开的入侵。 Cairn 最初是作为面向防御方的研究与问题求解引擎而开发的：只要给出起点和目标，它便会协调多个 AI 智能体寻找通往目标的路径，而这些能力如今被转用于攻击用途。此次被攻破的目标是 MONAI Label——一款开源的医学影像 AI 标注应用，这表明攻击者瞄准的是 AI/机器学习基础设施，而非传统的 Web 软件。

google\_news · BleepingComputer · 11月20日 17:30

**背景**: 零日漏洞是指厂商尚不知晓、因而在被利用时还没有补丁的漏洞。自主 AI 智能体是由大模型驱动的系统，能够自主规划、调用工具并执行多步骤任务，人类只需极少监督；将其用于渗透测试，便可自行串联侦察、漏洞发现与漏洞利用。Cairn 把这一能力打包成开源框架，安全研究人员称其在网络犯罪群体中越来越受欢迎。MONAI Label 则是基于 MONAI 医学影像框架构建的开源工具，可让临床医生和研究人员借助 AI 完成影像标注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-use-autonomous-ai-tool-cairn-to-find-zero-day-take-over-server/">Hackers use autonomous AI tool Cairn to find zero-day, take ...</a></li>
<li><a href="https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382">China attackers deployed AI agents that autonomously found ...</a></li>
<li><a href="https://shiftdelete.net/en/cairn-ai-agents-zero-day-server-takeover">Hackers Used Cairn AI Agents to Find a Zero-Day and Take</a></li>

</ul>
</details>

**标签**: `#AI security`, `#autonomous agents`, `#zero-day vulnerabilities`, `#cybersecurity`, `#vulnerability research`

---

<a id="item-4"></a>
## [谷歌以每分钟约 6 美元开放 Genie 4 可玩世界生成 API](https://www.aibase.com/news/32435) ⭐️ 8.0/10

11 月 19 日，谷歌通过 Gemini API 和 Google AI Studio 向开发者开放了 Genie 4 的实时可玩世界生成能力；前一天，面向符合条件的 Google AI Ultra 订阅用户，Project Genie 也已解锁。开发者可以输入文本、图像或两者组合，生成 720p/24fps 的交互式世界，键盘输入响应时间约为 0.2–0.5 秒。 这是前沿实验室首次将实时、可交互的世界生成作为按量计费的开发者 API 出售，可能改变游戏工作室的原型制作流程，以及仿真、机器人团队和生成式媒体工具的工作方式。按分钟计费的模式也表明，推理成本高昂的世界模型正被产品化为一种按使用量付费的云服务，而不只是研究演示。 生成的世界为 720p、24fps，并带有同步的环境音效和角色对白，输出内容还嵌入 SynthID 水印，以便日后识别 AI 生成内容。API 价格约为每分钟 6 美元，这意味着对于长时间或持续运行的会话来说，成本是实实在在的约束。

aibase · AIbase · 11月20日 15:01

**背景**: 世界模型是一类机器学习系统，它会在内部构建对某个环境的表征，包括物理规律、空间关系以及事物随时间的变化方式，从而预测接下来会发生什么。谷歌 DeepMind 的 Genie 系列于 2024 年首次推出，最初使用电子游戏画面训练，用于生成可交互的虚拟世界；早期版本只能生成二维环境，后续版本提升了分辨率与记忆能力并支持三维场景，Waymo 还基于 Genie 3 改造出用于模拟自动驾驶出租车极端场景的仿真器。SynthID 是谷歌的隐形水印技术，会把可检测的信号直接嵌入 AI 生成的图像、音频或视频中，以提升透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Genie">Google Genie</a></li>
<li><a href="https://deepmind.google/models/genie/">Genie 4 — Google DeepMind</a></li>
<li><a href="https://labs.google/projectgenie">Project Genie</a></li>

</ul>
</details>

**标签**: `#Google Genie`, `#Generative AI`, `#Game Development`, `#World Models`, `#API Release`

---

<a id="item-5"></a>
## [OpenAI 助力 AMD 旗舰 GPU 设计 PPA 提升 14%](https://news.google.com/rss/articles/CBMiqgJBVV95cUxNUGdyZW9IT1FpNVFKckhfR0N6dTQ2U0JFUm5UbUczQTlUREs4VTYwYXdLYlB3VXVZZ29ROHZxQkR4TnRqVHMtRWdpZ3VuVTJBd2x6QWk4ZlZNWENfLTY3bE1MN25UdEt0NWJ2a254cXZ0MXNwV3oxVEVlemFodVJyTGxBRUFLTjE5N1c1TUZXTTFlOXpZTnVTWk5UUjRiSHJHSHJwWThPVk41SlZ0dXZidERpTXhwWWJweXJOWkNOYVZlYlJwcVZndDdEUUNCV1ktOGR1ZUx2V1gyQnFaT050M2hhT3JnMEF1NFFsaUxPZDBHRWh1Y18xTThXNG8xT05NSGZIaXNnQWVQejVrVUhKb2tyT01ndVhZa19LUG9iTlM0V3JoYlVkQXdB?oc=5) ⭐️ 7.0/10

据 Tom&\#x27;s Hardware 报道，OpenAI 帮助 AMD 将其即将推出的旗舰 GPU 设计在 PPA 指标上提升了 14%，OpenAI 的 GPT 模型也被用于帮助优化 AMD 的新款 CPU。该报道仅提供了标题层面的信息，没有披露具体是哪款 GPU、处于哪个设计阶段，也没有说明这一提升是如何衡量的。 如果这一说法准确，它表明前沿 AI 模型正从炒作走向实实在在的半导体设计收益，可能帮助 AMD 缩小与 Nvidia 的差距，并改变芯片团队使用 AI 辅助工程的方式。在芯片设计中，14%的 PPA 提升相当可观，因为即便是个位数百分比的改进也可能意义重大。 PPA 代表功耗、性能和面积，是评估芯片设计的核心权衡指标，因此 14%的 PPA 提升可能指的是这些指标的综合改善，而不是某一项指标的统一加速。现有报道中没有包含独立验证、基准测试数据或详细的方法说明。

google\_news · Tom&\#x27;s Hardware · 11月20日 13:02

**背景**: 在芯片设计中，PPA（功耗、性能、面积）是衡量设计优劣的标准框架：更低的功耗、更高的性能和更小的面积都是追求目标，但它们之间需要相互权衡。AI 辅助设计是一个新兴领域，大语言模型和其他 AI 系统可帮助工程师探索电路、处理器核心和工具配置。OpenAI 最近发布了利用其模型优化电路和处理器核心的研究，同时还与 AMD 建立了大规模 GPU 合作伙伴关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.synopsys.com/glossary/what-is-power-performance-area-ppa.html">What is PPA (Power, Performance, and Area)? | Synopsys</a></li>
<li><a href="https://openai.com/index/advancing-chip-design-with-our-models/">Advancing chip design with OpenAI models</a></li>

</ul>
</details>

**标签**: `#AI for chip design`, `#AMD`, `#OpenAI`, `#GPU`, `#semiconductors`

---

<a id="item-6"></a>
## [腾讯开源 Hy4：7700 亿参数 MoE 模型，支持超 100 万 token 上下文](https://www.aibase.com/news/32446) ⭐️ 7.0/10

11 月 20 日，腾讯在 GitHub、Hugging Face、ModelScope 和 GitCode 上发布了 Hy4 的模型权重，至此混元大模型全系列（Hy3 preview、Hy3、Hy4 preview、Hy4、Hy4 flash）均已开放权重。Hy4 于 11 月 4 日首次发布，采用混合专家（MoE）架构，总参数 7700 亿、激活参数 490 亿，上下文窗口超过 100 万 token。 这使得腾讯成为少数几家公开前沿级旗舰模型权重的中国大厂之一，为开源模型生态提供了一个大规模 MoE 的新选择，可与现有开源模型形成竞争。对于无力承担闭源 API 成本、或希望自行托管长上下文应用的开发者而言，他们获得了一整套可直接下载部署的“旗舰+高性价比”模型组合。 由于采用稀疏 MoE 设计，Hy4 每个 token 仅激活 7700 亿参数中的 490 亿，因此尽管仍需存储全部权重，推理成本却远低于总参数量所暗示的水平。该报道来自资讯聚合站点，内容较为简略，并未披露基准测试成绩、许可证条款，也未说明标题中提到的安全评估的具体细节。

aibase · AIbase · 11月20日 17:01

**背景**: 混合专家（MoE）模型将网络拆分为许多被称为“专家”的专用子网络，由路由器为每个 token 只激活其中最相关的部分；这使得模型可以在保持单 token 计算量较小的同时达到极大的总规模，因此 MoE 模型通常同时标注总参数量和激活参数量。上下文窗口指的是模型一次能够处理的文本长度，100 万 token 的窗口大致相当于数十万词，可用于一次性分析整个代码库或整本书规模的文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters: What’s the Difference?</a></li>
<li><a href="https://www.mindstudio.ai/blog/1m-token-context-window-vs-rag-claude">Does a 1 M Token Context Window Replace RAG? | MindStudio</a></li>

</ul>
</details>

**标签**: `#open-weights`, `#Tencent Hunyuan`, `#Mixture-of-Experts`, `#large language models`, `#long context`

---

<a id="item-7"></a>
## [OpenAI 的 dots 助手走出聊天框，自带云端电脑](https://www.aibase.com/news/32430) ⭐️ 7.0/10

11 月 20 日，OpenAI 产品负责人 Thibault Sottiaux 宣布，在 DevDay 2026 上首次亮相的常驻助手 dots 开始邀请部分 ChatGPT Plus 用户参与测试，同时向所有 Business Standard 用户开放。其核心特性是内置的一台云端电脑，用户可设定目标、补充上下文、连接应用，并让任务在后台 7×24 小时持续执行。 这标志着产品从对话式聊天机器人转向能够在用户关闭页面后继续工作的代理型助手，可能改变知识工作者委派多步骤任务的方式。OpenAI 将其直接推向付费的 Plus 与 Business 套餐而非停留在候补名单式的演示阶段，也说明常驻型智能体正在从实验品变成正式的产品类别。 根据 OpenAI 官方说明，每个 dot 都拥有独立的云端电脑、浏览器、记忆与访问权限，并通过操作审核与批准流程以及内置安全机制来保证用户始终掌握控制权。此次上线是分阶段的——Plus 用户仅限受邀测试，Business Standard 用户则全面开放——因此长时间后台任务在真实环境中的稳定性仍有待大规模验证。

aibase · AIbase · 11月20日 11:01

**背景**: 所谓给 AI 助手配一台“云端电脑”，是指智能体运行在远程沙箱机器中而非聊天窗口内，因此即使使用者离线，它也能打开浏览器、读写文件并调用第三方应用——Cursor 的云端 agent 等编程工具也采用类似思路。dots 由 OpenAI 内部的编程工具演化而来，官方将其定位为用户能力的延伸，能够“在你工作的地方工作”，并以权限控制与审批环节作为主要的安全防线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-dots/">Introducing dots | OpenAI</a></li>
<li><a href="https://www.vellum.ai/blog/official-openai-dots-breakdown">Official OpenAI Dots Breakdown (2026)</a></li>
<li><a href="https://techcrunch.com/2026/10/26/how-openai-turned-its-coding-tools-into-dots-an-always-on-personal-assistant/">How OpenAI turned its coding tools into dots , an... | TechCrunch</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI assistants`, `#cloud computing`, `#ChatGPT`, `#product launch`

---

<a id="item-8"></a>
## [ChatPRD 创始人 Claire Vo 因代币欺诈关闭免费试用](https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/) ⭐️ 6.0/10

AI 产品管理工具 ChatPRD 的创始人 Claire Vo 发布视频及配套推文，描述了其产品遭遇的大量代币欺诈：一些团伙循环注册免费试用并套用促销码，再通过 ChatPRD 的智能体“打隧道”转售底层 AI 用量，或在上面运营商业化业务。因此她决定彻底取消免费试用。 这是来自创始人层面的一手案例，说明免费额度与试用滥用已成为 AI 产品实实在在的成本负担——每一次被滥用的请求都直接对应厂商自掏腰包的 GPU 开销。它也释放出一个信号：曾帮助 AI SaaS 产品增长的慷慨免费试用，在缺乏有力风控的情况下可能难以为继。 据称有滥用者直接告诉 Claire，他们靠循环注册免费试用和促销码、再通过她的智能体“打隧道”来制作游戏地图，以此资助一家国际化的 Roblox 与 Fortnite 地图工作室。她还发现智能体中反复出现“骑自行车的鹈鹕”SVG 生成请求，这很可能是在探测产品底层使用的是哪个模型，因为不同模型家族的输出带有可识别的特征。

rss · Simon Willison · 11月20日 02:49

**背景**: ChatPRD 是一个帮助产品经理把想法转化为产品需求文档的 AI 平台，自 GPT-4 时代起就已上线。这里的“代币欺诈”指的是攻击者获取自己从未付费的 AI 算力——手段包括批量薅取免费试用、转售访问权限，或借合法产品的智能体“打隧道”直连底层模型。由于 AI 推理每次请求都有真实成本，这类滥用会直接转化为厂商的经济损失，而不只是损失广告曝光。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sardine.ai/blog/token-fraud">Token fraud: 4 ways fraudsters steal AI compute</a></li>
<li><a href="https://www.stigg.io/blog-posts/token-fraud-the-nicest-card-on-the-internet-is-stealing-your-compute">AI Token Fraud: How It Happens and How to Stop It | Stigg</a></li>
<li><a href="https://fingerprint.com/blog/ai-token-abuse/">AI Token Abuse: What It Is and How to Prevent It</a></li>

</ul>
</details>

**标签**: `#AI`, `#token fraud`, `#abuse prevention`, `#SaaS`, `#free trials`

---

<a id="item-9"></a>
## [《自然》评论文章探讨 AI 缩小癫痫诊疗差距的潜力与风险](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5aYmdPX3Y0ampBdXhNcTBvTmNyc0FVaDZhem8xZ1ViR0JBWHZuUng0anJrbUZhdHduRktfbFVHY1hkZThZek4wTGRGZVdScVpSam1TR2RaVmV4S0lqZC13?oc=5) ⭐️ 6.0/10

《自然》发表的一篇评论文章探讨了人工智能如何有助于缩小癫痫诊疗中的差距，同时警告称，如果部署不当，同样的技术也可能固化既有的不平等。文章将这一问题定调为一把双刃剑式的机遇，而非单纯的技术解决方案。 癫痫是全球最常见的神经系统疾病之一，但很大一部分需要治疗的人从未获得适当诊疗，在低收入和中等收入国家尤为突出。由于 AI 工具越来越多地被视为将专家级能力延伸到医疗资源匮乏地区的手段，其设计与验证方式将直接决定它们是缩小还是扩大健康不平等。 该评论的核心论据在于，AI 模型会继承其训练数据中的偏差——例如主要来自资源充足医院的脑电图和影像数据集，可能难以泛化到其他人群，而算法输出还容易被误认为是客观的。由于目前仅能看到标题和摘要，全文中的具体案例与建议无法在此核实。

google\_news · Nature · 11月20日 10:54

**背景**: 所谓&quot;癫痫诊疗差距&quot;（epilepsy treatment gap），指的是需要治疗却未能获得适当诊疗的癫痫患者所占比例；系统综述显示，这一差距在发展中国家最大，主要源于神经科医生、诊断设备和可负担药物的短缺。癫痫领域的 AI 研究主要集中于基于脑电图（EEG）记录的癫痫发作自动检测与预测，深度学习模型在某些分类任务上已能达到甚至超过人类判读者的水平。与此同时，关于医疗 AI 偏差的文献记录了不具代表性的数据集、标注方式和部署环境如何导致系统性误差，使模型在代表性不足的群体上表现更差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10910960/">Treatment gaps in epilepsy - PMC</a></li>
<li><a href="https://www.nature.com/articles/s41746-023-00858-z">Bias in AI-based models for medical applications: challenges ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10071471/">EEG seizure detection: concepts, techniques, challenges, and ...</a></li>

</ul>
</details>

**标签**: `#AI in healthcare`, `#health equity`, `#epilepsy`, `#medical AI`, `#clinical disparities`

---

<a id="item-10"></a>
## [特朗普考虑惩罚在海外建设 AI 数据中心的美国公司](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPaXVJaktzUll1dHcwbTVtdnJjTjBDZjNVcFNic1hUbEFreS1fZ2lSLTlta2VVdEpwRFViVVhuUEVFcDBaTnNKbG0zeVBvaTc0dWNtTm1kRTNzcGMzemhWdmdWZ0FseWpLUUY3REFSLU1BWjF2cDNyVEFwMElpMmZobjFGcFgtY0pwaEFTdC1KcnpUWHBMR045SmFjeldEZWxHMEF4NUNwWGltcDc3SS1WMUJLekVjVFBZZ1FPZHVWZzQ0NnVqeG5UeEJNWXd4ZDRUYy1DLUlUa1A?oc=5) ⭐️ 6.0/10

《华盛顿邮报》报道称，特朗普政府正在考虑对在海外建设人工智能数据中心的美国公司实施惩罚，BBC 则将这一表态描述为可能对相关项目下达禁令。该提议是在政府因整体 AI 基础设施政策而遭遇行业反弹的背景下浮出水面的。 如果最终落地，此类惩罚措施可能阻止美国超大规模云厂商和 AI 实验室将算力部署在电力更廉价的国家，从而重塑全球 AI 算力的地理分布。这也意味着 AI 算力正从纯商业决策被重新定义为受限制的国家战略资产。 目前具体细节仍然有限：各家报道对措施究竟属于惩罚、关税还是彻底禁止说法不一，执行机制、时间表和法律依据也均未明确。此外，“美国公司”和“海外 AI 数据中心”将如何界定、盟友国家是否会被豁免，目前也不清楚。

google\_news · The Washington Post · 11月20日 22:44

**背景**: AI 数据中心耗电量极大，美国运营商近年来越来越多地转向海湾地区、东南亚和欧洲，以获取更廉价的电力、更快的审批流程，并满足当地的数据主权要求。与此同时，特朗普政府一直推动加快本土数据中心和电力设施建设，将 AI 算力领域的领先地位视为国家安全问题。美国此前对先进 AI 芯片的出口管制已经限制了英伟达硬件的销售去向，而这一提议相当于把同样的逻辑从芯片延伸到数据中心设施本身。

**标签**: `#AI policy`, `#data centers`, `#regulation`, `#tech industry`, `#infrastructure`

---