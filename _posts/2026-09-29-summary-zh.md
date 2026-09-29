---
layout: default
title: "Horizon Summary: 2026-09-29 (ZH)"
date: 2026-09-29 23:03:59 +0000
lang: zh
report: default
---

> 从 191 条内容中筛选出 7 条重要资讯。

---

1. [AMD 将以 82 亿美元收购李飞飞的 World Labs](#item-1) ⭐️ 9.0/10
2. [OpenAI 开发者大会：Dots 智能体、GPT-6.1 Sol 等 20 余项更新](#item-2) ⭐️ 8.0/10
3. [甲骨文就星际之门新墨西哥数据中心发出不可抗力通知](#item-3) ⭐️ 7.0/10
4. [Cloudflare 发布 cf 命令行工具，让 AI Agent 直通全部 API](#item-4) ⭐️ 7.0/10
5. [中国生成式人工智能用户规模突破 7 亿人](#item-5) ⭐️ 6.0/10
6. [OpenAI Codex 明天重开 200 美元 Pro 订阅，实际额度约减半](#item-6) ⭐️ 6.0/10
7. [谷歌修复导致 iOS 应用启动崩溃的 Firebase 问题](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [AMD 将以 82 亿美元收购李飞飞的 World Labs](https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute) ⭐️ 9.0/10

AMD 宣布以约 82 亿美元（约 551 亿元人民币）的全股票交易收购李飞飞于 2024 年联合创办的世界模型 AI 公司 World Labs。该交易预计在年底前完成，但仍需通过监管审批；李飞飞将加入 AMD，出任执行副总裁兼首席科学家，直接向 CEO 苏姿丰汇报。 这是芯片厂商对 AI 初创公司规模最大的收购之一，表明 AMD 不只想在 GPU 上、更想在模型与物理 AI 层面与英伟达竞争，而世界模型被广泛视为机器人与具身智能的关键使能技术。这桩交易还让 AMD 获得一位极具影响力的研究领军人物，以及一项可与自家 Instinct 加速器和 ROCm 软件栈搭配的稀缺模型资产。 本次交易以 AMD 股票而非现金支付，且仍需获得监管批准，目标是在年底前完成交割；李飞飞将直接向苏姿丰汇报。World Labs 成立于 2024 年，定位为“空间智能”公司，其模型能够感知、生成、推理并与三维虚拟与物理世界交互，相关技术还可用于生成机器人训练所需的模拟环境。

telegram · zaihuapd · 9月29日 03:59

**背景**: AI 中的“世界模型”是指能够构建环境内部表征、并预测环境如何随动作变化的系统，可模拟物理规律、物体交互和因果关系等动态；与单纯的预测式语言模型不同，它让智能体无需反复在真实世界试错即可进行规划与行动，因此世界模型在机器人、自动驾驶和交互式视频生成中处于核心地位。李飞飞是斯坦福大学教授、也是现代计算机视觉领域的关键人物，她于 2024 年联合创办 World Labs，主攻这一“空间智能”前沿方向。AMD 是英伟达在 AI 加速器领域的主要挑战者，而英伟达凭借 CUDA 软件生态和 Isaac Sim 机器人仿真平台建立了广泛优势，因此拥有一支前沿世界模型团队，是 AMD 从模型侧进攻这一护城河的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.worldlabs.ai/about">About - World Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_%28artificial_intelligence%29">World model (artificial intelligence)</a></li>
<li><a href="https://developer.nvidia.com/isaac/sim">Isaac Sim - Robotics Simulation and Synthetic... | NVIDIA Developer</a></li>

</ul>
</details>

**标签**: `#AMD`, `#World Labs`, `#Fei-Fei Li`, `#AI acquisition`, `#world models`, `#robotics`

---

<a id="item-2"></a>
## [OpenAI 开发者大会：Dots 智能体、GPT-6.1 Sol 等 20 余项更新](https://openai.com/zh-Hant/index/devday-2026-recap/) ⭐️ 8.0/10

在 DevDay 2026 开发者大会上，OpenAI 发布了 20 余项更新：核心是常驻智能体 Dots，可全天候自主运转、学习用户习惯并主动接管长线复杂任务；同时推出两款新模型——专精编程与电脑操控的 GPT-6.1 Sol（以约五分之一的价格获得接近 Astra 的智能水平）和速度最高提升 8 倍（API 提升 6 倍）的 Astra Ultrafast。此外还包括原生支持电脑操控与 AWS Bedrock 托管的 Agents API、面向预设有限选项分类与路由的轻量实时 Decisions API、“Sign in with ChatGPT”第三方工具账号互通（如 Devin、Notion），以及算力额度为 Plus 的 25 倍、专享 Astra Ultrafast 的全新 Pro 500 档位。 这批更新标志着 OpenAI 从“售卖模型调用”转向“售卖常驻的自主智能体”，让智能体长期嵌入用户的工作流——这正是当前 OpenAI、Anthropic 与各家智能体平台竞争的主战场。同时把模型、智能体 API、受限输出的决策接口以及订阅额度互通打包进第三方应用，是一次范围极广的生态圈地，可能让开发者和终端用户更深度地绑定在 OpenAI 的技术栈上。 第三方分析指出，Dots 基于 GPT-6 Astra，为每个智能体配置独立的云端计算机和浏览器，可连接数千款第三方应用，并在 ChatGPT 既有防护之上叠加了额外的权限保障层，因此审批模型的粒度直接决定了能安全委派多少工作。Decisions API 与 TypeSafe 的 Jev 瞄准同一“受限选项”场景，据称由 Luna 模型驱动，且与 Jev 不同之处在于支持图像输入，但单次调用成本和速率限制尚不明确；另外需要注意，本条快讯本身是二手摘要，没有一手文档或基准数据支撑。

telegram · zaihuapd · 9月29日 17:52

**背景**: 所谓“常驻”或“always-on”智能体，与聊天助手的区别在于它在后台持续运行、拥有独立的算力环境和浏览器，并自主推进目标而无需人工逐步提示——这是 OpenAI 自推出 Agents SDK（其实验性 Swarm 库的生产级继任者）以来一直在推进的形态。Agents API 则把这类智能体封装进受管的会话状态和长任务执行流程中，这也解释了 OpenAI 为何要搭配 AWS Bedrock 这样的云端托管伙伴。所谓“Decisions API”是一个更窄的概念：模型不返回自由文本，而必须在开发者给定的候选项中选出一个答案，因此在分类、路由和智能体动作选择上更便宜也更可靠。“Sign in with ChatGPT”则是一种类似 OAuth 的身份层，让外部工具直接调用用户已有的 ChatGPT 订阅额度，而不必另开账号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dragapp.com/blog/openai-dots/">OpenAI Dots and Email: What a Dot Can Do With Your Inbox (2026)</a></li>
<li><a href="https://thenewstack.io/openai-decision-api-luna/">OpenAI answers TypeSafe&#x27;s Jev with a Decision API ... - The New Stack</a></li>
<li><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></li>

</ul>
</details>

**标签**: `#openai`, `#llm-agents`, `#api`, `#model-release`, `#developer-tools`

---

<a id="item-3"></a>
## [甲骨文就星际之门新墨西哥数据中心发出不可抗力通知](https://www.bloomberg.com/news/articles/2026-09-24/oracle-cites-force-majeure-to-shield-itself-on-controversial-data-center) ⭐️ 7.0/10

甲骨文已向星际之门位于新墨西哥州多尼亚安娜县的 Project Jupiter 数据中心开发方发出不可抗力通知，原因是该项目配套的 2.45GW 微电网迟迟拿不到环境与供电审批。甲骨文希望借此在外部因素导致延期时推迟部分付款，而该项目的 2028 年投运目标已受到威胁。 这一动作表明超大型 AI 数据中心建设正遭遇实质性阻力：制约因素越来越不是芯片，而是电力与审批，并且影响已蔓延至融资端——该项目的 180 亿美元银团贷款据报已出现折价交易。由于星际之门是 OpenAI 约 5000 亿美元基础设施计划的旗舰载体，此处的延期可能重塑整个 AI 算力竞赛的进度预期。 争议核心是为园区供电的 2.45GW 微电网，审批延误会危及原定的 2028 年投运目标（公开提到的完工预期最晚已到 2029 年 11 月）。星际之门多数站点仍处于土建、审批或能源采购阶段，只有得克萨斯州阿比林园区实现规模化投产，而得州也已暂停对新数据中心项目的审批。

telegram · zaihuapd · 9月29日 05:46

**背景**: 星际之门计划（Stargate Project）是 OpenAI、甲骨文、软银和 MGX 于 2025 年 1 月宣布成立的合资项目，计划在约四年内投入最多 5000 亿美元在美国建设 AI 基础设施，Project Jupiter 就是其规划中的新墨西哥州圣特蕾莎园区。微电网是一种由互联负载和分布式电源组成的本地化电力系统，既可独立运行也可与主电网并网，对 AI 园区颇具吸引力，因为它比新建公用事业输电线路更快落地，但仍需通过环境与并网审批。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.enr.com/articles/63720-oracle-invokes-force-majeure-as-new-mexico-project-jupiter-power-work-faces-hurdles">Oracle Invokes Force Majeure as New Mexico Project Jupiter Power Work Faces Hurdles</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stargate_LLC">Stargate LLC - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/microgrid">What Is a Microgrid? | IBM</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#Oracle`, `#Stargate`, `#energy policy`

---

<a id="item-4"></a>
## [Cloudflare 发布 cf 命令行工具，让 AI Agent 直通全部 API](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) ⭐️ 7.0/10

Cloudflare 发布了名为 cf 的新命令行工具开放测试版，让开发者和 AI Agent 可以在终端中调用 Cloudflare 的全部 API。与仅覆盖约 280 种操作的现有 Wrangler CLI 不同，cf 直接由 Cloudflare 的 API Schema 自动生成，覆盖超过 3,000 项 API 操作，并默认以 JSON 作为输出格式。 通过把数千个 Cloudflare API 端点转化为可发现、机器可读的命令，cf 大幅降低了自主 Agent 端到端配置和运维云基础设施的门槛。这也反映出整个行业正把 AI Agent 视为一等用户，而不再只为人手操作设计开发者工具。 该工具内置命令搜索和引导式发现机制，方便 Agent 自动找到所需操作并以程序化方式处理结果；Cloudflare 给出的示例显示，同一个 Agent 可用 cf 创建并部署 Worker、监控服务、配置 Access 与 WAF 策略，甚至购买域名。目前它仍处于开放测试阶段，因此在正式发布前接口和覆盖范围仍可能调整。

telegram · zaihuapd · 9月29日 13:46

**背景**: Cloudflare 是主要的 CDN、DNS 与安全服务商，其 Wrangler CLI 长期是构建和部署 Cloudflare Workers（该公司的无服务器边缘计算平台）的标准方式。Cloudflare Access 是其 Cloudflare One 安全平台中的零信任网络访问组件，WAF 则指其 Web 应用防火墙。新的 cf 工具并非要取代 Wrangler，而是一个由 Schema 驱动、覆盖整个 Cloudflare API 的更广泛接口，围绕便于 AI Agent 解析和执行动作的 JSON 输出而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/">Overview · Cloudflare Workers docs</a></li>
<li><a href="https://www.npmjs.com/package/wrangler">wrangler - NPM</a></li>
<li><a href="https://grokipedia.com/page/Cloudflare_Access">Cloudflare Access</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#CLI`, `#AI Agents`, `#API Automation`, `#Developer Tools`

---

<a id="item-5"></a>
## [中国生成式人工智能用户规模突破 7 亿人](https://ysxw.cctv.cn/article.html?toc_style_id=feeds_default&amp;amp;item_id=187569887152346976&amp;amp;channelId=1119) ⭐️ 6.0/10

9 月 29 日，中国互联网络信息中心（CNNIC）发布《生成式人工智能应用发展报告（2026）》。报告显示，截至 2026 年上半年，中国生成式人工智能用户规模突破 7 亿人，普及率超过 50.0%。报告同时指出，智能问答是最主要的应用场景，76.0%的用户用它来回答问题；AI 综合助手与 AI 效率办公的使用次数同比增长均超过 100%；中国智能算力规模达到 2185 EFLOPS，同比增长 177%。 普及率突破 50%意味着生成式人工智能在中国已从早期尝鲜者的小众技术转变为大众化主流工具，这将深刻影响面向数亿用户的产品设计、内容分发、教育和办公软件形态。与此同时，智能算力同比增长 177%也表明中国 AI 基础设施的建设速度足以支撑这一需求，是全球 AI 产业的重要宏观指标。 这些核心数字属于基于调查的采用率统计，而非技术突破：76.0%的用户依赖智能问答，而 AI 综合助手与 AI 效率办公是增长最快的类别，使用次数同比增长超过 100%。算力数据 2185 EFLOPS 衡量的是 AI 加速浮点运算性能（1 EFLOPS 等于每秒 10^18 次运算），而在现有摘要中报告并未说明其具体统计口径与方法。

telegram · zaihuapd · 9月29日 06:39

**背景**: CNNIC（中国互联网络信息中心）是中国官方背景的互联网管理机构，最为人熟知的是其半年发布一次的全国互联网发展统计报告以及负责.cn 域名体系的管理，其数据通常被视为权威行业口径。这里的“生成式人工智能用户”指使用过聊天机器人、AI 助手等生成式 AI 产品的互联网用户，普及率即该群体在中国整体网民中的占比。EFLOPS 是算力单位，1 EFLOPS 等于每秒 10^18 次浮点运算，而中国的“智能算力”特指面向 AI 优化的加速算力，而非通用 CPU 算力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wipo.int/wipolex/en/legislation/details/7914">Rules for the China Internet Network Information Center (CNNIC) Domain Name Dispute Resolution Policy, China, WIPO Lex</a></li>
<li><a href="https://blog.csdn.net/qq_16498553/article/details/123491738">什么是 EFLOPS ？ -CSDN博客</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#China AI Market`, `#AI Adoption`, `#Industry Report`, `#AI Compute`

---

<a id="item-6"></a>
## [OpenAI Codex 明天重开 200 美元 Pro 订阅，实际额度约减半](https://x.com/thsottiaux/status/2104823812042940713) ⭐️ 6.0/10

OpenAI 的 Codex 负责人 Tibo（Thibault Sottiaux）预告，Codex Pro 200 美元订阅将于明天重新向新用户开放，同时用量改为按等值 API 花费折算，实际额度大约只有旧版 Pro 200 美元方案的一半。他还确认，此前引发争议的 5 小时限制不会恢复，并且本周 GPT-6 Sol 与 GPT-6 Luna 的 API 价格已降至原价的 50%。 这标志着 OpenAI 对其旗舰编程智能体的商业化计费逻辑发生实质性转变：名义额度缩水，但公司押注于更便宜、更高效的模型，让开发者用每一美元完成更多工作，而不是靠虚高的 API 标价把订阅包装成“超值”。对于把 Codex 深度嵌入开发流程的团队来说，这既影响预算，也影响每周用量的节奏安排，同时释放出“按需购买 API 与订阅之间的价差将逐步缩小”的信号。 最关键的技术变化是额度不再以固定配额表示，而是按 API 花费等值折算，因此每周额度能撑多久，直接取决于用户使用哪个模型以及消耗多少 token。取消 5 小时限制意味着用户可以按自己的节奏把每周额度用完；Tibo 还承诺不会虚抬 API 标价，并表示明天会公布另一项不增加用量的新权益。

telegram · zaihuapd · 9月29日 06:50

**背景**: Codex 是 OpenAI 推出的一套 AI 编程智能体，可让开发者把写功能、重构代码、调试等软件工程任务交给它完成，并以 ChatGPT 订阅档位的形式出售，其中就包括 200 美元的 Pro 方案。旧方案用滚动 5 小时窗口限制用量，许多重度用户认为这种安排很别扭，因为工作必须被切分到不同时间段。改为按 API 花费折算额度，意味着订阅与实际模型的 token 定价直接挂钩，因此本周 GPT-6 Sol 与 GPT-6 Luna 降价 50% 会直接提升每一美元订阅费所能完成的工作量——这两个模型属于 GPT-6 家族中侧重编程与专业工作的版本，与能力更强的 Astra 一同发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>

</ul>
</details>

**标签**: `#OpenAI Codex`, `#subscription pricing`, `#AI coding tools`, `#quota changes`, `#GPT-6`

---

<a id="item-7"></a>
## [谷歌修复导致 iOS 应用启动崩溃的 Firebase 问题](https://github.com/firebase/firebase-ios-sdk/issues/16728) ⭐️ 6.0/10

谷歌确认，Google Analytics for Firebase 的 iOS 服务端返回了格式错误的数据，导致大量集成该组件的 iOS 应用在启动时崩溃。事故始于（2026 年）9 月 28 日 17:41（美国太平洋夏令时），当日 19:52 已完成服务端修复推送。谷歌表示开发者无需更新 SDK 或应用；受缓存影响，部分应用在修复后最长仍可能继续崩溃约 4 小时，残余问题会自行消退。 这起事故说明，一个带有服务端下发组件的第三方 SDK 可以在开发者完全没有改代码的情况下，同时让大量互不相关的应用集体崩溃，使分析类库变成了平台级的可用性风险。对任何使用 Firebase 的移动端团队都有警示意义：应用方无法在本地缓解崩溃，只能等待谷歌后端修复逐步生效。 问题根源是 Google Analytics for Firebase 后端下发的异常数据，而不是 Firebase iOS SDK 本身，因此修复完全在服务端完成，无需发布新的客户端版本。修复后最长约 4 小时的“长尾”被归因于客户端缓存：已经缓存了错误数据的设备会持续崩溃，直到缓存刷新，因此实际影响时间窗口比约两小时的修复耗时更长。

telegram · zaihuapd · 9月29日 16:29

**背景**: Firebase 是谷歌推出的后端即服务（BaaS）平台，为 iOS、Android、JavaScript、Unity 等平台的移动与 Web 应用提供数据库、身份验证、托管、分析等服务。Google Analytics for Firebase 是许多应用都会集成的分析 SDK，它会自动采集事件和用户属性并上传到谷歌服务器用于报表。由于这类 SDK 会在应用启动时从后端拉取配置或数据，一旦服务端响应出错，问题会在应用自身代码执行之前爆发，这正是此类故障格外严重的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Firebase">Firebase</a></li>
<li><a href="https://defold.com/assets/googleanalyticsforfirebase/">Google Analytics for Firebase - Defold</a></li>
<li><a href="https://stackoverflow.com/questions/64712951/difference-between-google-analytics-and-firebase-analytics">Difference between Google analytics and Firebase analytics - Stack Overflow</a></li>

</ul>
</details>

**标签**: `#Firebase`, `#iOS`, `#Google Analytics`, `#Outage/Incident`, `#Mobile Development`

---