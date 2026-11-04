---
layout: default
title: "Horizon Summary: 2026-11-04 (ZH)"
date: 2026-11-04 23:04:30 +0000
lang: zh
report: ai
---

> 从 188 条内容中筛选出 10 条重要资讯。

---

1. [OpenAI 员工用 GPT-6 Astra 一周内完成硬件设计](#item-1) ⭐️ 8.0/10
2. [Anthropic 研发 FlashProve，用密码学证明 AI 输出究竟出自哪个模型](#item-2) ⭐️ 8.0/10
3. [百度发布 Apollo World 物理 AI 世界模型，并启用新一代端到端 Robotaxi 架构](#item-3) ⭐️ 7.0/10
4. [普林斯顿 SSoN 基准发布：人类准确率 83.3%，最强视觉语言模型仅 39.7%](#item-4) ⭐️ 7.0/10
5. [欧盟总法律顾问：Gemini 绕过付费墙使用新闻内容或构成侵权](#item-5) ⭐️ 7.0/10
6. [Anthropic 据称开源 FlashProve：用零知识证明验证 LLM 权重真伪](#item-6) ⭐️ 7.0/10
7. [Datasette Apps 0.3a0 发布，强化与 Datasette Agent 的权限感知集成](#item-7) ⭐️ 6.0/10
8. [Datasette Agent 0.5a0 新增侧边面板，支持对话式构建应用](#item-8) ⭐️ 6.0/10
9. [AWS 详解面向生产级 AI 智能体的四层上下文工程框架](#item-9) ⭐️ 6.0/10
10. [Google 将对拒绝其 AI 工具的学区关闭搜索服务](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 员工用 GPT-6 Astra 一周内完成硬件设计](https://www.aibase.com/news/32089) ⭐️ 8.0/10

据报道，OpenAI 在 11 月 3 日的博客中展示了两名团队成员利用业余时间，在不到一周内用 GPT-6 Astra 设计出一款与 Codex 交互的测试设备，模型承担了外观、外壳、元器件选型、PCB 布局和固件等工作。随后一家工厂在不到一个月内生产出了小批量样机。 如果得到证实，这将是 LLM 完成端到端硬件协同设计（涵盖机械、电路与固件）的早期具体案例，而不仅仅是辅助完成孤立任务。这可能大幅压缩通常需要多学科团队和数月迭代的开发周期，也意味着智能体式 AI 正从软件领域向实体产品开发延伸。 据报道，这项工作把机械、电路与软件的协作整合到同一个对话中，模型负责从外观、外壳到 PCB 布局与固件的全部环节。但需注意：该消息来自二次聚合来源，没有独立验证，所用工厂、设备规格和成本等具体细节均未披露。

aibase · AIbase · 11月4日 18:01

**背景**: GPT-6 Astra 是 OpenAI GPT-6 模型家族的一员，该系列自 2026 年 9 月 4 日起向公众开放，并被定位为能力较强的智能体模型——在衡量 AI 智能体完成真实软件中复杂专业任务的 Agents&\#x27; Last Exam 基准上得分为 59.3%。测试设备所交互的 Codex 是 OpenAI 的编程智能体，于 2025 年 4 月以 CLI 形式发布，到 2026 年 3 月周活跃用户已超过 200 万。传统硬件开发需要机械工程师、电子工程师和固件开发者分别在 CAD、EDA 和代码工具链之间协同；而这里的说法是 Astra 在同一个对话线程内完成了这种协同设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://kie.ai/gpt-6-astra">GPT - 6 Astra API - Try OpenAI GPT - 6 on Kie AI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6 Astra`, `#AI hardware design`, `#LLM agents`, `#PCB design`

---

<a id="item-2"></a>
## [Anthropic 研发 FlashProve，用密码学证明 AI 输出究竟出自哪个模型](https://www.aibase.com/news/32086) ⭐️ 8.0/10

Anthropic 公布了 FlashProve —— 一套开源的“可证明推理”（provable inference）系统，利用密码学（具体为 zkSNARK）为每一条输出生成数学证明，证实该输出确实由指定的模型生成。官方在拥有 4000 亿参数的混合专家模型 Llama 4 Maverick 上做了演示：在单块 NVIDIA H100 GPU 上以约每秒 110 个 token 的速度生成证明，GPU 开销约为 72 倍，证明体积约 19 MB。 该方案直指业内长期存在却鲜少公开的问题——模型掉包、刷高基准测试成绩，以及把请求偷偷路由到更便宜模型的隐藏后门——让用户可以验证究竟是哪个模型在回答自己。一旦技术成熟，它有望成为 AI 可问责性、可信基准评测和可审计 API 服务的基础设施，影响整个生态。 证明的生成过程无需暴露模型的专有权重，实现以 Apache 2.0 协议开源，并通过 Lean 进行形式化校验。但需要强调，这只是一个研究原型：Anthropic 表示暂无产品化部署计划，而且约 72 倍的计算开销意味着“证明”的成本仍远高于普通推理。

aibase · AIbase · 11月4日 17:01

**背景**: zkSNARK（零知识简洁非交互式知识论证）允许一方在不重跑计算、也不暴露底层数据的前提下，证明某项计算被正确执行——Anthropic 将其类比为可验证发件人的密码学邮件签名。用在大型语言模型上时，被证明的“计算”就是模型对提示词的完整前向推理，因此一份有效证明即意味着这些 token 确实由所声称的那个模型（且只有它）生成。这一点之所以重要，是因为目前 API 客户根本无法核查服务商是否在收取旗舰模型费用的同时，偷偷用小模型或廉价模型作答。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/provable-inference">Progress on provable inference for large language models</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/anthropic-flashprove-cryptographic-model-verification">Anthropic unveils cryptographic tool to verify model outputs</a></li>
<li><a href="https://shattered.io/anthropic-flashprove-provable-inference-72x-overhead-2026/">Anthropic FlashProve: Provable Inference at 72x [2026]</a></li>

</ul>
</details>

**标签**: `#AI verification`, `#cryptography`, `#Anthropic`, `#AI trust and safety`, `#model provenance`

---

<a id="item-3"></a>
## [百度发布 Apollo World 物理 AI 世界模型，并启用新一代端到端 Robotaxi 架构](https://www.aibase.com/news/32087) ⭐️ 7.0/10

11 月 3 日，百度在深圳举办的 AI Day · Apollo 活动上首次公开了面向物理 AI 的世界模型 Apollo World，该模型可模拟可交互的道路环境，用于自动驾驶车辆的训练与测试。百度智能驾驶首席架构师王亮表示，已有约 100 辆 Apollo Go 无人驾驶出租车运行在新一代端到端架构上，累计全无人驾驶安全里程接近 100 万公里。 这一发布把“世界模型”这一研究概念与真实的商业化 Robotaxi 车队联系起来，表明百度正将无人驾驶服务从模块化、基于规则的流水线转向数据驱动的端到端驾驶。若该路线可规模化，Apollo World 生成的仿真里程有望大幅降低验证与扩张 Robotaxi 运营的成本和时间，无论是在中国还是百度的海外拓展中。 百度称 Apollo World 每天可生成高达 10 万公里的仿真驾驶数据，并已用于支持 Apollo Go 的全球 Robotaxi 业务拓展，但公司并未公布基准测试结果、详细架构规格或第三方安全统计数据。该端到端系统直接从驾驶数据中学习驾驶策略，并预测转向、油门、刹车等控制信号，而不再依赖分别工程化的感知与规划模块。

aibase · AIbase · 11月4日 17:01

**背景**: 世界模型是一类学习环境演化内部表征的 AI 系统，使智能体能够在行动之前预测自身行为的后果，这也是业界所称“物理 AI”（即嵌入机器人、汽车等真实世界机器中的 AI）的核心要素。传统自动驾驶技术栈是模块化的：感知、定位、规划和控制被构建为相互独立的阶段；而端到端方法则将原始传感器输入送入单一学习模型，直接输出驾驶决策。Robotaxi 是这一转变最早落地的商业应用之一，因为车队能产生海量真实驾驶数据，且在无驾驶员运营前必须证明安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technode.com/2026/11/04/baidu-launches-apollo-world-model-to-train-robotaxis-in-simulated-environments/">Baidu launches Apollo World model to train robotaxis in ...</a></li>
<li><a href="https://www.reuters.com/technology/chinas-baidu-launches-ai-model-simulating-road-environment-robotaxis-2026-11-03/">China&#x27;s Baidu launches AI model simulating road environment ...</a></li>
<li><a href="https://www.orcarouter.ai/blog/baidu-apollo-world-driving-world-model">Apollo World: Baidu&#x27;s Robotaxi Simulator, Explained</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#world models`, `#physical AI`, `#robotaxi`, `#Baidu Apollo`

---

<a id="item-4"></a>
## [普林斯顿 SSoN 基准发布：人类准确率 83.3%，最强视觉语言模型仅 39.7%](https://www.aibase.com/news/32081) ⭐️ 7.0/10

普林斯顿大学人工智能实验室发布了新的空间智能基准 SSoN，该测试剥离动态交互与动作控制的干扰，专门评估静态跨视角下的三维空间理解能力。在四选一的室内“找出异常”题目中，人类准确率达到 83.3%，而主流视觉语言模型最高仅为 39.7%，其中多数甚至低于随机猜测基线。 如此巨大的人机差距说明，在常规视觉语言基准上的高分并不能转化为真正的三维场景理解能力，而这种能力对机器人、具身智能以及任何需要在真实物理空间中推理的智能体都至关重要。由于多数模型在四选一任务中低于 25% 的随机水平，这一结果反映的是系统性失败，而非仅仅“能力偏弱”。 SSoN 共包含 1000 道题目和 4000 张图像，取自七个场景来源和六类编辑操作；任务要求模型判断四张视角图中哪一张不可能属于同一个未改变的三维场景，并用跨视角证据解释其中的矛盾。由于题目为四选一的选择题，25% 的随机基线使得多数模型低于基线的表现格外值得关注。

aibase · AIbase · 11月4日 16:01

**背景**: 视觉语言模型（VLM）等多模态大模型通常在二维图像—文本任务上训练和评测，例如图像描述与视觉问答，这些任务对空间推理的要求有限。跨视角空间理解——即从不同位置拍摄的多张照片推断同一三维场景的布局——是一项更困难的能力，需要在大脑中重建几何结构并发现不同视角之间的矛盾。SSoN 这类基准旨在排除视频动态、机器人控制等干扰因素，单独测量这一能力差距，从而更清晰地反映模型对三维空间究竟理解到什么程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/32081">Princeton AI Lab launches SSoN benchmark: human accuracy 83.3 ...</a></li>
<li><a href="https://eu.36kr.com/en/p/4054651667813510">Princeton AI Lab&#x27;s Spatial Intelligence Benchmark Test ...</a></li>
<li><a href="https://github.com/sson-benchmark/SSoN">GitHub - sson-benchmark/SSoN</a></li>

</ul>
</details>

**标签**: `#AI benchmarks`, `#spatial reasoning`, `#vision-language models`, `#3D understanding`, `#Princeton AI Lab`

---

<a id="item-5"></a>
## [欧盟总法律顾问：Gemini 绕过付费墙使用新闻内容或构成侵权](https://www.aibase.com/news/32076) ⭐️ 7.0/10

欧盟法院总法律顾问在一起由匈牙利网站运营者起诉谷歌的案件中正式发表了意见，指出 Gemini 若非法绕过付费墙获取新闻报道，或在其回答中以可识别的方式再现新闻报道的具体表达，就可能构成版权侵权。该意见为人工智能处理新闻内容划定了版权边界，但它属于咨询性意见，而非最终判决。 这一意见是欧盟版权法如何适用于生成式人工智能与新闻出版业的重要信号，并可能影响 AI 开发者构建依赖付费新闻的检索与摘要功能的方式。如果欧盟法院采纳总法律顾问的论证，那些呈现新闻文本的聊天助手可能需要改变其内容获取与再现方式。 该意见区分了两类责任触发情形：一是绕过付费墙获取内容，二是在聊天机器人回答中再现新闻报道中可识别的具体表达，这涉及出版商的复制权。值得注意的是，总法律顾问的意见并不具有约束力，但欧盟法院在最终裁决中往往会采纳此类意见。

aibase · AIbase · 11月4日 12:01

**背景**: 欧盟法院（CJEU）是欧盟范围内解释欧盟法律的最高司法机构，其总法律顾问会在判决作出前发表说理充分的意见，为法官提供指引。根据欧盟版权法，作者与出版商享有排他的复制权，未经许可复制受保护内容可能构成侵权。付费墙是一种要求先付费或订阅才能查看内容的技术屏障，而绕过它把内容送入人工智能系统，正是本案中总法律顾问指出的问题所在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/">Gemini — Google DeepMind</a></li>
<li><a href="https://gemini.google/us/about/?hl=en">Gemini – Your AI assistant from Google</a></li>

</ul>
</details>

**标签**: `#AI copyright`, `#EU law`, `#Gemini`, `#news publishing`, `#paywalls`

---

<a id="item-6"></a>
## [Anthropic 据称开源 FlashProve：用零知识证明验证 LLM 权重真伪](https://www.aibase.com/news/32073) ⭐️ 7.0/10

据 aibase 报道，Anthropic 与零知识证明研究者开源了 FlashProve：单张 H100 约 39 分钟生成模型“权重指纹”，每次对话生成约 19 MB 证明，普通 CPU 可用 cp\_verify 在 17 秒内完成验证。 如果这些说法成立，模型买家无需拿到权重、也无需运行 GPU，就能以密码学方式发现“模型套壳”和降级服务——即付费购买顶级模型却被偷偷换成更便宜的模型。这可能成为 AI 供应链信任与问责的一项重要基础能力。 报道称该证明系统使用 zkSNARK，每次请求约进行 2000 次 sumcheck，并以 BLAKE2 作为安全基础；但该文是简略的聚合式报道，没有链接论文或代码仓库，正文被截断，也未给出安全审计或限制说明，因此这些工程数据应视为未经独立验证。

aibase · AIbase · 11月4日 12:01

**背景**: zkSNARK 是一种简洁的非交互式零知识证明，能让证明者在不泄露底层数据的情况下说服验证者某个陈述为真。sumcheck（求和校验）协议是高效零知识论证系统的核心组件之一，使验证者无需逐项计算就能检查关于多变量多项式的求和声明。BLAKE2 是 RFC 7693 标准化的密码学哈希函数，因速度快、安全性好而被广泛用于生成指纹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Zkvers/substrate-zk/blob/master/zk-tutorials/ZKSNARKS.md">substrate-zk/zk-tutorials/ ZKSNARKS .md at master · Zkvers/substrate-zk</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sum-check_protocol">Sum - check protocol - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BLAKE_%28hash_function%29">BLAKE (hash function)</a></li>

</ul>
</details>

**标签**: `#zero-knowledge-proofs`, `#zkSNARK`, `#LLM security`, `#model verification`, `#AI supply chain`

---

<a id="item-7"></a>
## [Datasette Apps 0.3a0 发布，强化与 Datasette Agent 的权限感知集成](https://simonwillison.net/2026/Nov/4/datasette-apps/) ⭐️ 6.0/10

Datasette Apps 0.3a0 正式发布，改进了在 Datasette 内部托管和编辑自定义 HTML 应用的方式，并加深了与 Datasette Agent 的集成。现在用户可以在 Agent 聊天消息中输入“\#”来引用应用，自动补全的候选仅限于该用户有权限查看的应用；同时新增 app\_add\_stored\_queries\(\) 和 app\_remove\_stored\_queries\(\) 两个工具，让 Agent 能够管理某个应用可以调用哪些存储查询。 由于这类应用通常由 LLM Agent 生成而非手工编写，新增的权限校验显得尤为重要：app\_create\(\) 现在会检查每个被请求的存储查询是否存在、用户是否有权查看，并在授予写查询权限前要求用户明确批准。这降低了 Agent 悄悄暴露数据或提升为写权限的风险，使依赖 Datasette 的数据记者和研究人员在使用 Agent 辅助构建应用时更加安全。 为应用授予写查询权限需要用户事先批准，Agent 工具输出的“View app”按钮以及“\#”应用链接现在都会在 Datasette Agent 面板中以全屏方式打开应用。该版本仍是 0.3a0 alpha，API 和行为可能继续调整。

rss · Simon Willison · 11月4日 00:29

**背景**: Datasette 是一个用于探索和发布数据的开源工具，它把 SQLite 数据库封装成可交互的网站和配套 API。Datasette Agent 是构建在 Datasette 之上、由 LLM Python 库驱动的可扩展 AI 助手，让用户可以用对话方式查询数据。Datasette Apps 进一步扩展了这一能力，允许在 Datasette 内部托管自定义 HTML 应用，这些应用可以手写，但更便捷的方式是通过 Agent 由 LLM 生成。存储查询是保存在 Datasette 内部数据库中的 SQL 查询；Datasette 1.0a31 引入了带权限的写查询和用户保存的存储查询，这正是这些应用所调用的机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://datasette.io/blog/2026/datasette-agent/">Datasette Agent , an extensible AI assistant for... - Datasette Blog</a></li>
<li><a href="https://datasette.io/blog/2026/sql-write-queries/">SQL write queries and stored queries in Datasette 1.0a31</a></li>

</ul>
</details>

**标签**: `#datasette`, `#llm-agents`, `#developer-tools`, `#release`, `#sqlite`

---

<a id="item-8"></a>
## [Datasette Agent 0.5a0 新增侧边面板，支持对话式构建应用](https://simonwillison.net/2026/Nov/3/datasette-agent/) ⭐️ 6.0/10

Datasette Agent 0.5a0 正式发布，新增名为“panel”（侧边面板）的功能，可让智能体对话窗口保持打开，并与 Datasette 的表页或查询页等页面并排显示。配合 datasette-apps 插件，这意味着用户可以用提示词直接生成一个由数据库驱动的应用，然后在这个应用旁边的聊天窗口中持续修改它。 这一改动把对话式提示与被构建的产物紧密连接起来，使 Datasette 从单纯的数据探索工具，变成一个可以就地生成并迭代应用的开发环境。这也反映出一种更广泛的趋势：LLM 智能体正被直接嵌入开发工具之中，而不是存在于单独的聊天标签页里。 发布说明中用分屏的“LLM Price Explorer”应用演示了该面板：这个应用完全通过对话生成，随后又通过对话改成了暗色终端风格的主题，过程中调用了 app\_create、app\_render、app\_view 和 app\_str\_replace 等工具，模型标签为“gpt-6-luna”。该版本仍是早期的 0.5 alpha，托管版本可在 agent.datasette.io 通过 GitHub 账号登录试用。

rss · Simon Willison · 11月3日 23:13

**背景**: Datasette 是 Simon Willison 开发的开源工具，可以把任意形态的数据拿来进行分析和探索，并发布为交互式网站和 API。Datasette Agent 是在 Datasette 之上叠加 LLM 智能体对话的配套项目，而 datasette-apps 插件则允许用户直接在 Datasette 内部创建并托管单文件的 HTML、JavaScript 和 CSS 应用，并提供创建、查看、编辑和删除应用等权限控制。此前这些部分相对独立，而新的 panel 功能把聊天窗口与生成的应用放到了同一个视图里。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://github.com/datasette/datasette-apps">GitHub - datasette/ datasette - apps : Apps that live inside Datasette</a></li>
<li><a href="https://datasette.io/blog/2026/datasette-apps/">Host applications inside Datasette with Datasette ... - Datasette Blog</a></li>

</ul>
</details>

**标签**: `#datasette`, `#LLM agents`, `#AI tooling`, `#open source release`, `#database apps`

---

<a id="item-9"></a>
## [AWS 详解面向生产级 AI 智能体的四层上下文工程框架](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNckI2RW5SeGRMQmt0NlVlRUhPT3lLdFRLVldSelVscGg4eWZIYmtDWkp4STlmbXJVRWFhcWRpV0tOZ3ZwSTJ6TmtxY2tNclF6dnJUZnVCdWt3cVB4N0tLc0lzbFZLUDRMMWJzaUNWbHVNZkpMTDJ4S0gtZ1o3bU5XS3lCeHVZVW9YNnRmVG5Udzg1d253aWdEVS16QnNqcnkwUE9LMUItaGJjY1V4TkI3bmp5NlR4bG4xTjljTWFzWWF0RGpHY0VMQ1RpTjNMRWtDWnl4a3RuOXRSaDZ0allHR04ybUV3cXM?oc=5) ⭐️ 6.0/10

AWS 发布了一篇技术博客，提出了一个四层上下文工程框架，分别涵盖架构、提示词、基于文件的工具以及验证智能体，并以 Deep Insight 的实际代码作为示例加以说明；Deep Insight 是一个基于 Strands Agents SDK 和 Amazon Bedrock AgentCore 构建的开源多智能体数据分析方案。文章指出，在生产环境的智能体中，真正的瓶颈是上下文管理，而不是模型能力本身。 构建大模型智能体的团队逐渐意识到，把一切都塞进提示词窗口既昂贵又不可靠，因此来自主流云厂商的、有代码支撑的可复用模式为从业者提供了一份具体蓝图。这种分层方法旨在显著降低 token 消耗，从而降低成本，同时提升长时间运行的智能体工作流的可靠性。 该模式将上下文隔离、对提示词进行精细控制，并把体量庞大的数据外置为通过工具访问的文件，而不是一直放在上下文窗口中，同时加入验证智能体来检查中间结果。不过它只是厂商撰写的、围绕单一合作伙伴实现的案例研究，并非与其它方案进行基准对比的评测，因此其结果应被视为示例性的，而非可直接推广的结论。

google\_news · Amazon Web Services \(AWS\) · 11月4日 16:30

**背景**: 上下文工程指的是动态构建、管理和优化 AI 智能体完成任务所需的全部信息，其范围超出了基础的提示词撰写。检索增强生成（RAG）通过检索相关文档作为知识 grounding 层，但业界越来越认为，对于在动态环境中运行、需要即时组装和裁剪上下文的智能体而言，仅靠 RAG 是不够的。Deep Insight 是一个开源的多智能体数据分析系统，AWS 将其作为参考实现；而 Strands Agents SDK 与 Bedrock AgentCore 则是 AWS 用于构建和运行智能体的工具链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/machine-learning/four-layers-of-context-engineering-for-production-ai-agents-how-deep-insight-applies-them-in-working-code/">Four layers of context engineering for production AI agents ...</a></li>
<li><a href="https://creati.ai/ai-news/2026-11-04/aws-shows-how-deep-insight-uses-four-layers-of-context-engineering-for-production-ai-agents/">AWS Shows How Deep Insight Uses Four Layers of Context ...</a></li>
<li><a href="https://thecontextgraph.co/memos/why-rag-is-not-enough-for-production-ai-agents">Why RAG Is Not Enough for Production AI ... | The Context Graph</a></li>

</ul>
</details>

**标签**: `#context engineering`, `#AI agents`, `#LLM applications`, `#RAG`, `#AWS`

---

<a id="item-10"></a>
## [Google 将对拒绝其 AI 工具的学区关闭搜索服务](https://news.google.com/rss/articles/CBMipwFBVV95cUxNeTNiaHNHN2xUN0RXTm9TYkNRdXd1QUpKc1ZhSWFrMTJiUkgzeVl1RXZuWnRka3lHVTQ4RUtRcHNoTU1jelJYaDE5eUZBM3VIdDdtMWtaRkFITHZmLVVCeFctNHFpSXBQdHlnSm9ST0lhNDVkSHZ1dnpxUHVVZUltZFlJWDJpS3Q1ck1KZEdZVFRkTnJ5VzR3MjhnaTlGeThkbWRscU9WQQ?oc=5) ⭐️ 6.0/10

据报道，Google 计划对拒绝采用其 AI 工具的学区关闭 Google 搜索服务，这意味着这些学区使用学校管理账号的学生将无法使用搜索，而会看到一条由学校显示的消息，说明该服务不可用。该政策由《纽约时报》和 Engadget 等多家媒体报道，其背景是 Google 已将 AI Overviews 和 AI Mode 直接整合进搜索体验之中。 学校通过 Chromebook 和 Workspace for Education 成为 Google 生态中规模最大、最难以脱离的用户群体之一，因此把基础搜索访问权与 AI 采用挂钩，将使 Google 对那些担心学生数据、准确性或课堂政策的学区拥有巨大的影响力。此举出现在 Google 本就面临严峻反垄断压力的时期，可能加剧外界关于该公司利用某一市场的主导地位来强制推广另一市场产品的指责。 据 Engadget 报道，在封禁 AI 工具的学校中，学生“将无法使用搜索”，而是会看到一条带有学校标识的消息，说明该服务不可用；而 Google 则坚称学校可以在不启用 Gemini 的情况下继续开启搜索。据报道，该政策适用于学校管理的账号而非个人 Google 账号，并且针对的是如今已嵌入搜索的 AI 功能，而不是作为独立产品的传统网页搜索结果。

google\_news · WBAY · 11月4日 16:48

**背景**: Google 一直在将生成式 AI 引入 Google Workspace for Education 以及搜索本身，如今 AI Overviews 和 AI Mode 会在搜索结果顶部生成摘要式答案。由于这些功能由管理控制台设置控制，学校 IT 管理员必须决定是否对学生启用它们，而许多学区出于隐私、偏见和学术诚信方面的顾虑，对 AI 一直持谨慎态度。Google 对搜索的控制以及 Chrome/Chromebook 在美国课堂中的占有率，早已引起反垄断审查，包括 2024 年的一项裁决认定其非法维持搜索垄断地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html">Google Will Turn Off Search for Schools That Reject A . I .</a></li>
<li><a href="https://www.engadget.com/2305432/google-says-that-students-in-schools-that-ban-ai-wont-have-access-to-search/">Google Says Students In Schools That Ban AI Won&#x27;t Have Access To...</a></li>
<li><a href="https://www.reuters.com/legal/us-judge-rules-google-broke-antitrust-law-search-case-2024-08-05/">reuters.com/legal/us-judge-rules- google -broke- antitrust -law-search...</a></li>

</ul>
</details>

**标签**: `#Google`, `#AI policy`, `#education technology`, `#antitrust`, `#digital access`

---