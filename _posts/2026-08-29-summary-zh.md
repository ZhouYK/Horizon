---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29 04:33:53 +0000
lang: zh
report: default
---

> 从 292 条内容中筛选出 6 条重要资讯。

---

1. [腾讯混元发布 Hy4 preview：开源 770B 参数 MoE 大模型](#item-1) ⭐️ 8.0/10
2. [长鑫科技上半年净利 776 亿扭亏为盈，创历史纪录](#item-2) ⭐️ 8.0/10
3. [智谱开源 GLM-5.3，主打智能体编程与网络防御](#item-3) ⭐️ 8.0/10
4. [OpenAI 终止向 Cursor 供应模型，2026 年 11 月停服](#item-4) ⭐️ 8.0/10
5. [美国 FTC 调查 YouTube 封号，称内容政策或误导用户](#item-5) ⭐️ 7.0/10
6. [谷歌员工内测 Gemini 3.8 Flash 预览版，测试者称明显更优](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [腾讯混元发布 Hy4 preview：开源 770B 参数 MoE 大模型](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 8.0/10

2026 年 8 月 28 日，腾讯发布了迄今最强开源模型 Hy4 preview，总参数量 770B（活跃参数 49B），上下文窗口为 1M token。在 203 个工程任务的盲评中，Hy4 preview 以 2.99 分略胜 GLM-5.3（2.92）和 Kimi K3（2.94），已上线腾讯云、GitHub、Hugging Face、ModelScope、OpenRouter 等平台。 Hy4 preview 表明，开源模型能够在复杂工程任务上与顶级专有及竞品开源系统一较高下。其 1M 上下文窗口与混合专家（MoE）设计，标志着大模型正朝着更大规模、更高效率的方向发展，能够胜任长周期软件工程、文档处理和科学研究等工作负载。 Hy4 preview 采用混合专家（MoE）架构：总参数 770B，但每个 token 仅激活 49B 参数，既保持了大规模能力又降低了推理成本。API 定价为每 1M 输入 token 0.834 美元、每 1M 输出 token 2.501 美元，模型主打长周期软件工程、文档办公与科学研究场景。

telegram · zaihuapd · 8月28日 06:11

**背景**: 传统稠密（dense）大语言模型对每个 token 都会激活全部参数，随着模型变大，计算成本急剧上升。混合专家（MoE）模型则将网络拆分为多个专门的子网络（即&\#x27;expert&\#x27;），并通过路由器（router）为每个输入只激活最相关的专家，从而以最小计算实现大规模扩展。在 MoE 模型中，总参数表示全部可学习的权重，而活跃参数是单次前向传播中实际使用的子集，决定推理速度和计算成本。1M token 的上下文窗口可以让模型一次性处理超长文档或代码库，这对需要捕捉长距离依赖的工程和科研任务至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://researchaudio.io/p/mixture-of-experts-moe-in-large-language-models">Mixture of Experts ( MoE ) in Large Language Models</a></li>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between Total and...</a></li>
<li><a href="https://www.sciencetimes.com/articles/51540/20241101/pushing-the-boundaries-of-contextual-understanding.htm">Pushing the Boundaries of Contextual Understanding</a></li>

</ul>
</details>

**标签**: `#AI模型`, `#开源`, `#腾讯混元`, `#大语言模型`

---

<a id="item-2"></a>
## [长鑫科技上半年净利 776 亿扭亏为盈，创历史纪录](https://telegram.me/zaihuapd/43468) ⭐️ 8.0/10

长鑫科技披露 2026 年上半年营业收入 1503.1 亿元，同比增长 873.64%；归母净利润 776.05 亿元，上年同期亏损 23.32 亿元，实现扭亏为盈。主营业务毛利率达 84.84%。 这一里程碑表明中国在 DRAM 生产领域的能力不断提升，而 DRAM 是由三星、SK 海力士和美光主导的战略性存储芯片品类。强劲盈利能力可为后续扩产提供资金，助力降低中国对进口存储的依赖，并在 AI 驱动的 DRAM 需求中重塑竞争格局。 一季度归母净利润 247.62 亿元，二季度归母净利润 528.43 亿元，环比增长 113%。经营活动现金流量净额 1311.56 亿元，同比增长 2985.64%；基本每股收益 1.2893 元。

telegram · zaihuapd · 8月28日 11:34

**背景**: DRAM（动态随机存取存储器）是一种易失性半导体存储器，每个比特存储在一个由电容和晶体管组成的存储单元中，需要定期刷新。它广泛用作计算机、显卡和便携设备的主内存；全球 DRAM 市场历来由三星、SK 海力士和美光主导。2026 年初，由于 AI 相关需求激增，DRAM 和 NAND 价格大幅上涨，HBM 的生产正在挤压普通 DRAM 产能。长鑫科技是中国领先的 DRAM 制造商，其业绩既反映了存储价格上涨，也体现了中国推动半导体自主化的努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DRAM">DRAM</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#DRAM`, `#financial results`, `#memory chips`, `#China tech`

---

<a id="item-3"></a>
## [智谱开源 GLM-5.3，主打智能体编程与网络防御](http://z.ai/) ⭐️ 8.0/10

智谱 AI 发布了开源大模型 GLM-5.3，它与 GLM-5.2 共用同一基础模型，全部提升来自后训练。该模型在 Terminal Bench 2.1 上得分 88.2，在 DeepSWE 上得分 66.9，在复杂编程和长周期任务上大幅领先 GLM-5.2。 此次发布为开源大模型生态带来了具有竞争力的智能体编程能力，可能让更多开发者和企业能够构建自主编码智能体。自定义许可证还引入了值得关注的商业限制：年营收超过 100 亿美元的大型模型即服务提供商须通过 Z.AI 的安全审查，这可能影响 GLM-5.3 的大规模部署方式。 根据自定义 GLM-5.3 许可证，个人和中小企业可自由使用、微调与商用该模型，但连续 12 个月营收超过 100 亿美元且对外提供模型即服务的公司，须先通过 Z.AI 的安全审查。所有性能提升均来自后训练，而非新的基础模型。

telegram · zaihuapd · 8月28日 15:32

**背景**: 后训练是预训练之后的阶段，通过监督微调（SFT）和强化学习等技术来塑造模型对指令和任务的响应方式。智能体编程将 AI 模型视为能够感知、推理、规划和行动的智能体，通常以极少的人工干预自主处理编码任务。Terminal Bench 2.1 和 DeepSWE 是编码智能体基准，分别评估工具调用忠实度和真实世界软件工程性能；例如，Artificial Analysis 编码智能体指数就是取 DeepSWE、Terminal-Bench v2.1 和 SWE-Atlas-QnA 得分的平均值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.deeplearning.ai/courses/fine-tuning-and-reinforcement-learning-for-llms-intro-to-post-training/lesson/fwxgd0/where-post-training-%28fine-tuning-and-rl%29-fits-into-llm-training">Fine-tuning &amp; RL for LLMs: Intro to Post - training - DeepLearning.AI</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-programming-future-ai-unicodax-unicodax-uv4xf">Agentic Programming : The Future of AI at Unicodax</a></li>
<li><a href="https://artificialanalysis.ai/agents/coding-agents">AI Coding Agent Benchmarks &amp; Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open-source`, `#agentic programming`, `#GLM`

---

<a id="item-4"></a>
## [OpenAI 终止向 Cursor 供应模型，2026 年 11 月停服](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10

OpenAI 宣布将终止通过 Cursor 提供 OpenAI 模型的合同，建议停服日期为 2026 年 11 月 12 日。这一决定是在 SpaceX 收购 Cursor 之后做出的，并采用了合同允许的最大通知期。 这是一个影响重大的人工智能编程工具商业决策，说明收购可能导致现有合作关系破裂。同时，它也凸显了 OpenAI 对马斯克旗下公司能否遵守合同条款的担忧，因为有违反协议的先例。 OpenAI 表示无法确信 SpaceX 会遵守服务条款，并提到马斯克旗下公司在收购 Twitter 后违反合同，以及今年早些时候 xAI 在宣誓下承认违反 OpenAI 服务条款的事实。双方的定制协议允许 OpenAI 在控制权变更后的有限时间内取消合作，而两方已合作近四年。

telegram · zaihuapd · 8月29日 02:24

**背景**: Cursor 是一款基于熟悉 VS Code 平台的 AI 优先代码编辑器，提供多行编辑、智能重写等由 AI 模型驱动的功能。OpenAI 曾通过定制协议向 Cursor 提供模型，而由埃隆·马斯克领导的 SpaceX 最近收购了 Cursor。OpenAI 的决定涉及控制权变更的合同条款，也体现了 OpenAI 与马斯克之间日益紧张的局势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/">AI Coding Agent for Building Ambitious Software | Cursor</a></li>
<li><a href="https://www.cursor.com/features">Features | Cursor - The AI -first Code Editor</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Cursor`, `#SpaceX`, `#AI`, `#Business`

---

<a id="item-5"></a>
## [美国 FTC 调查 YouTube 封号，称内容政策或误导用户](https://www.bloomberg.com/news/articles/2026-08-27/us-ftc-probing-youtube-over-social-media-policies) ⭐️ 7.0/10

美国联邦贸易委员会（FTC）正在调查 Alphabet 旗下 YouTube 的封号及内容执行行为是否违反消费者保护法。知情人士透露，这项始于去年的调查已进入最后阶段，并正在为可能提起的诉讼做准备。 这项调查可能导致针对全球最大视频平台之一的大型诉讼，或迫使 YouTube 使其执行做法与其声明政策保持一致。这也表明监管机构对科技行业内容审核的审查力度加大，对用户权利和平台问责制具有潜在影响。 调查重点在于 YouTube 封禁或降级内容时是否违反其自身用户政策，以及用户是否被误导，以为自己可以发布某些内容，结果内容被下架或账号被封。YouTube 和 FTC 均拒绝置评，且公司尚未被正式指控存在不当行为。

telegram · zaihuapd · 8月28日 07:48

**背景**: FTC 是美国负责执行消费者保护法的机构，包括禁止不公平或欺骗性商业行为的规则。YouTube 的内容政策规定了用户可以上传什么内容，但执行决定可能不一致或不够透明，使人担心平台的行为可能与其公开承诺相矛盾。这类调查可能导致同意令、罚款或要求改变商业行为的法院命令。

**标签**: `#FTC`, `#YouTube`, `#content moderation`, `#consumer protection`, `#regulatory investigation`

---

<a id="item-6"></a>
## [谷歌员工内测 Gemini 3.8 Flash 预览版，测试者称明显更优](https://www.businessinsider.com/google-employees-testing-next-gemini-flash-3-8-model-2026-8) ⭐️ 6.0/10

谷歌员工已通过内部编码平台 Jetski 开始测试 Gemini 3.8 Flash 预览版，一位测试者称其明显优于 3.7 Flash。谷歌拒绝置评，该模型尚未登陆公开 API 或 Vertex AI。 这表明谷歌正优先以更快的节奏推出更小、更便宜的 Flash 模型，而非一再延期旗舰大模型，可能改变开发者使用 Gemini 的方式。Flash 模型的快速迭代可能加剧高性价比 AI 模型市场的竞争。 Gemini 3.6 Flash 于 2026 年 7 月发布，约三周后发布 3.7 Flash；CEO 桑达尔·皮查伊曾表示计划近乎每月推新。预览版通过 Jetski 提供，这是谷歌内部用于在真实负载下试用早期构建的平台。

telegram · zaihuapd · 8月28日 09:38

**背景**: Gemini Flash 是谷歌 DeepMind 推出的快速、高性价比多模态模型系列，与 Pro 和 Deep Think 等版本并列，面向智能体工作流和编码场景。Jetski 这类内部试用平台在 AI 实验室中很常见，让员工可在公开 API 或云上线前运行早期构建。据报道，谷歌旗舰 Gemini 模型一再延期，因此转向更快推出 Flash 系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shattered.io/gemini-3-8-flash-preview-google-testing-2026/">Google Tests Gemini 3.8 Flash 14 Days After 3.7</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_%28language_model%29">Gemini (language model ) - Wikipedia</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.7 Flash — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#Gemini`, `#Google`, `#AI`, `#Large Language Models`

---