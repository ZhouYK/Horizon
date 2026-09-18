---
layout: default
title: "Horizon Summary: 2026-09-18 (ZH)"
date: 2026-09-18 23:04:14 +0000
lang: zh
report: ai
---

> 从 188 条内容中筛选出 10 条重要资讯。

---

1. [Rust 安全团队警告针对知名维护者的定向攻击](#item-1) ⭐️ 8.0/10
2. [阿里发布 Qwen3.8-Omni-Flash：原生多模态，音频成本降低 98%](#item-2) ⭐️ 8.0/10
3. [Figure 发布 Helix 2.5，零样本家庭任务成功率从 9% 提升至 56%](#item-3) ⭐️ 8.0/10
4. [Claude Code 以内置 mod 形式支持 AGENTS.md](#item-4) ⭐️ 7.0/10
5. [Ptacek：绝不要使用 LLM 建议的任何措辞](#item-5) ⭐️ 7.0/10
6. [美军因 AI 生成虚假情报报告而险些酿成事端](#item-6) ⭐️ 7.0/10
7. [Moonshot AI 的 2.8 万亿参数 Kimi K3 上线 Amazon Bedrock](#item-7) ⭐️ 7.0/10
8. [Anthropic 聘请埃森哲担任首个嵌入式 AI 安全评估方，并承诺投入 10 亿美元](#item-8) ⭐️ 7.0/10
9. [深度学习助力设计可同时检测与捕获有毒硫气体的材料](#item-9) ⭐️ 7.0/10
10. [Anthropic 警告：AI 系统正越来越多地构建自身的下一代版本](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Rust 安全团队警告针对知名维护者的定向攻击](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) ⭐️ 8.0/10

2026 年 9 月 17 日，Adam Harvey 与 crates 安全团队发布警告称，有一场持续进行的攻击活动正针对 rust-lang 成员和热门 crate 的所有者，试图入侵他们的设备与账号，以便利用这些账号发布恶意软件。攻击者会以工作、项目或合同机会为名义安排一次视频通话，然后借此让目标安装某些东西（例如号称缺失的音频编解码器），或执行某条命令，比如把命令放进剪贴板诱导目标粘贴执行。 由于几乎所有现代软件都依赖开源包，依赖链中拥有发布权限的人本身就是攻击面，因此一名维护者被攻陷就可能把恶意代码推送给成千上万的下游项目。此次警告紧跟在 2026 年 8 月一次得逞的供应链攻击之后，说明该手法已被实际验证有效，维护者和安全团队必须把这类主动上门的“招聘式”通话视为真实威胁。 警告指出，该活动专门针对 rust-lang 成员与热门 crate 的所有者，其投递方式是社工而非技术漏洞利用；它紧随 2026 年 8 月 20 日 arrayref 被入侵事件，当时 0.3.10 版本引入了一个仿冒名称的依赖 proc-macro1，其构建脚本会下载并运行远程二进制文件。该恶意版本以及 internment@0.8.7、append-only-vec@0.1.9 在发布约 86 分钟后被从 crates.io 移除。

rss · Simon Willison · 9月17日 23:59

**背景**: Rust 是一门强调内存安全的系统编程语言，其用户和贡献者被非正式地称为 Rustacean，其包生态以 crates.io 注册表为核心，项目会自动从其中拉取库作为依赖。供应链攻击并不直接攻破目标代码，而是攻陷某个维护者账号或某个上游包，从而让恶意代码被下游所有项目自动引入。crate 所有者发布的版本会被任何依赖它的项目获取，因此单个热门维护者的账号被接管，影响范围可以极其广泛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustsec.org/advisories/RUSTSEC-2026-0260.html">RUSTSEC-2026-0260: arrayref: `arrayref` 0.3.10 was removed ...</a></li>
<li><a href="https://lib.rs/crates/arrayref">arrayref — Rust library // Lib.rs Malicious Rust Crate arrayref Runs a Build-Time Payload Rust Supply Chain Attack on arrayref: Significant Overlap ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rustacean">Rustacean</a></li>

</ul>
</details>

**标签**: `#security`, `#rust`, `#supply-chain-attack`, `#social-engineering`, `#open-source`

---

<a id="item-2"></a>
## [阿里发布 Qwen3.8-Omni-Flash：原生多模态，音频成本降低 98%](https://www.aibase.com/news/31158) ⭐️ 8.0/10

阿里巴巴通义千问团队发布了原生全模态模型 Qwen3.8-Omni-Flash，可同时接受文本、图像、音频和视频四种输入，上下文窗口最高支持 100 万 Token，并已在 Qwen AI 上线。相比上一代模型，它在 29 项基准测试中平均提升超过 25%，同时将音频处理成本降低了 98%。 此次发布表明阿里正从将语音与视觉模块简单拼接的做法，转向用单一模型原生地理解并操作多种模态，这对开发视频剪辑、MV 创作、影视解说以及音视频转写与对话等智能体应用的开发者意义重大。音频成本下降 98% 加上百万级上下文，也让多模态智能体在生产规模上更接近经济可行的临界点。 最值得注意的设计变化在于，多模态理解与智能体能力是在模型层面原生集成的，而不是通过拼接语音识别和图像识别流水线来实现。官方称共有约 30 项评测，覆盖编程、GUI 交互以及音视频智能体任务；不过 &quot;Flash&quot; 这一命名暗示它是一款偏向效率的版本，其定价和完整基准数据目前尚未广泛公布。

aibase · AIbase · 9月18日 14:01

**背景**: 所谓 &quot;原生&quot; 多模态模型，是指用单一网络同时训练模型去看、听、阅读并跨文本、图像、音频、视频进行推理，而不是把多个专用模型串联起来，这通常能保留更多跨模态上下文并降低延迟与成本。文中提到的 &quot;100 万 Token 上下文窗口&quot;，指的是模型在一次会话中能够同时关注的信息上限，包括提示词、文档、对话历史和此前的输出。阿里通义千问（Qwen）是使用广泛的商用与开源模型系列，与 Google 的 Gemini、Anthropic 的 Claude 等同样在推进任意模态互转能力的模型存在竞争关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/audio/2605.25343">Toward Native Multimodal Modeling : A Roadmap | alphaXiv</a></li>
<li><a href="https://devtk.ai/en/blog/llm-context-window-explained/">LLM Context Windows Explained: 4K to 1M Tokens (2026)</a></li>
<li><a href="https://aimlapi.com/blog/what-is-gemini-omni-googles-any-to-any-multimodal-ai">What Is Gemini Omni? Google&#x27;s Any-to-Any Multimodal AI</a></li>

</ul>
</details>

**标签**: `#Multimodal AI`, `#Qwen`, `#Alibaba`, `#Large Language Models`, `#AI Model Release`

---

<a id="item-3"></a>
## [Figure 发布 Helix 2.5，零样本家庭任务成功率从 9% 提升至 56%](https://www.aibase.com/news/31151) ⭐️ 8.0/10

Figure 发布了 Helix 2.5，这是一个单一的人形机器人基础模型，能够在 30 个从未见过的家庭中完成三项长时序家务行为——整理客厅、叠毛巾和铺床，且在这些环境中不做任何数据采集、微调或适配。通过在 Figure 的 Index 人类行为数据上进行预训练，该模型在陌生家庭中的零样本成功率从 9% 提升到了 56%。 这代表人形机器人在零样本泛化能力上的一次大幅跃升：以往模型一旦换到新家庭往往就会失效，而一个无需按家庭微调、就能在 30 个陌生住宅中工作的单一基础模型，让具身智能更接近可实际部署的通用家务机器人。这也增强了 Figure 在人形机器人商业化竞赛中相对 Tesla Optimus 等对手的竞争力。 测试环境和被操作物体在训练中完全未出现过，机器人必须仅凭预训练知识解决完整的感知与控制问题，不能在现场进行微调、示教或适配。公布的基准是三项全身长时序任务（整理、叠毛巾、铺床），56% 是一个总体零样本成功率，而非各任务均已饱和，也就是说仍有大约五分之二的尝试会失败。

aibase · AIbase · 9月18日 11:01

**背景**: 零样本泛化指的是一套训练好的策略能够在训练中从未见过的任务、物体或环境中直接完成任务，无需额外微调或示教。基础模型是指先在海量数据上预训练、再复用到多种任务上的大型神经网络，正是这一思路让大语言模型具备了通用性。Figure 的 Index 是一个众包数据平台，付费向普通人征集真实日常活动的视频；据 Figure 称，它已在 100 多个国家收集了数百万条视频上传，Helix 正是基于这些人类行为数据预训练的。Helix 2.5 是 Figure 机器人 AI 技术栈的最新版本，用于驱动该公司的人形机器人硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization">Helix 2.5: Zero - Shot 30-Home Generalization</a></li>
<li><a href="https://www.humanoidsdaily.com/news/figure-ai-unveils-index-crowdsourcing-real-world-human-video-to-train-helix">Figure AI Unveils Index: Crowdsourcing Real-World Human Video to Train Helix | Humanoids Daily</a></li>
<li><a href="https://theaiinsider.tech/2026/09/17/figure-unveils-helix-2-5-with-zero-shot-humanoid-generalization-across-30-homes/">Figure Unveils Helix 2.5 With Zero-Shot Humanoid Generalization Across 30 Homes</a></li>

</ul>
</details>

**标签**: `#humanoid robotics`, `#foundation models`, `#robot learning`, `#zero-shot generalization`, `#Figure AI`

---

<a id="item-4"></a>
## [Claude Code 以内置 mod 形式支持 AGENTS.md](https://simonwillison.net/2026/Sep/18/thariq-shihipar/) ⭐️ 7.0/10

据 Anthropic 的 Thariq Shihipar 介绍，从 Claude Code 2.1.277 版本开始，如果某个文件夹中没有 CLAUDE.md 文件，Claude 就会转而查找并使用 AGENTS.md 文件。该支持以一个内置 mod 的形式发布，属于 Claude Code 即将推出的 mods（用于定制 Claude Code harness）体系的一部分，其源码已在 anthropics/claude-code 仓库中公开。 这标志着 AGENTS.md 作为跨工具约定取得了一次重要胜利：开发者现在可以只维护一份指令文件，就能在多个编码智能体之间通用，而不必为每个工具单独维护厂商专属配置。这也表明 Anthropic 正在开放 Claude Code 的内部机制以供第三方定制，而不是把项目指令锁定在专有格式中。 AGENTS.md 仅作为回退选项：当同一个文件夹中同时存在两个文件时，CLAUDE.md 仍然优先，因此现有的 Claude Code 项目不受影响。该功能基于 Claude Code mods 构建——这类插件的行为写在用 TypeScript 编写的 hooks 模块中——用户也可以按同样的方式自行构建定制版的项目指令。

rss · Simon Willison · 9月18日 19:09

**背景**: CLAUDE.md 是一个 Markdown 配置文件，Claude Code 会在每次会话开始时自动读取，它相当于持久的项目记忆，用来描述代码库结构、编码风格和工作流规则。AGENTS.md 则是一种类似但跨工具的开放 Markdown 格式，同样提交到 Git 仓库中，许多编码智能体都会读取它来了解在仓库中应如何行事。由于不同厂商为同一个想法采用了不同的文件名，AGENTS.md 便作为共享标准的尝试而出现，而 Claude Code 对它的采纳是迈向互操作性的重要一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agents.md/">AGENTS.md</a></li>
<li><a href="https://github.com/agentsmd/agents.md">GitHub - agentsmd/agents.md: AGENTS.md — a simple, open format for guiding coding agents</a></li>
<li><a href="https://claude.com/blog/using-claude-md-files">Using CLAUDE.MD files: Customizing Claude Code for your ...</a></li>
<li><a href="https://github.com/anthropics/claude-code/tree/main/mods">claude-code/mods at main · anthropics/claude-code · GitHub</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AGENTS.md`, `#AI coding agents`, `#Anthropic`, `#developer tools`

---

<a id="item-5"></a>
## [Ptacek：绝不要使用 LLM 建议的任何措辞](https://simonwillison.net/2026/Sep/17/how-to-write-with-an-llm/) ⭐️ 7.0/10

Thomas Ptacek 发表了题为《How To Write With An LLM》的文章，主张 LLM 应当被当作文字编辑（copyeditor）而非写作助手使用，并提出了严格的“第一条规则”：你不得采用 LLM 建议给你的任何一个词。Simon Willison 在短文里表示认同，并说明他不会让 LLM 为自己的博客撰写内容，但会用它们做事实核查、拼写与语法检查，偶尔也当作同义词词典使用。 它为所有在写作流程中使用 AI 的人提供了一条易记且可操作的准则：享受 LLM 带来的机械性便利，但拒绝它的文风输出，从而让文字不会染上那种一眼可辨的“AI 味”。当 LLM 辅助写作逐渐成为技术写作和专业出版的默认做法时，这类维护个人声音与作者责任的规范就变得越来越重要。 在文章后半部分，Ptacek 展示了他个人 LLM 文字编辑工具的截图，并给出了一段提示词，帮助读者搭建自己的版本；Willison 的文章还提到，Ptacek 在 Hacker News 的一条评论中公开了自己的完整系统提示词。Willison 同时把自己那套校对提示词（收录在其 agentic engineering patterns 指南中）链接给读者。

rss · Simon Willison · 9月17日 23:37

**背景**: 诸如 GPT、Claude 之类的大语言模型（LLM）已被广泛用于起草和润色文字，但它们的输出往往带有可辨识的文风特征——常被称作“AI 味”，例如滥用过渡词、句子过于四平八稳和爱加模糊限定。Ptacek 的提议在“机械性辅助”（核对事实、修正标点、给你提供可参考的同义词）与“生成式代笔”（让模型把自己的措辞塞进你的文章）之间划出了界线。Simon Willison 是长期深入撰写 LLM 话题的知名博主和开源开发者，Thomas Ptacek 则是知名安全工程师、Latacora 联合创始人。

**标签**: `#LLM`, `#AI writing`, `#prompt engineering`, `#AI ethics`, `#writing workflow`

---

<a id="item-6"></a>
## [美军因 AI 生成虚假情报报告而险些酿成事端](https://news.google.com/rss/articles/CBMijAFBVV95cUxQNURhdTZha1pnekJvMjV5cE9VQ0tpQmZuSXVfbFVzLVBDbDY1b28zMUluUVNzMUlPZnE2Qk5OLXRVcUVsRkVfZ3d2ZVpvaW9JOGFZUE00SV9uQ0xWcE5QOGlzXzB2bkRaWjZiZVpKblZBU2tsOTdvMllIdTRKb21ScUlwNlIzSDdaTFR0Rg?oc=5) ⭐️ 7.0/10

CNN 独家报道称，一名美军分析人员先是依赖 AI 系统生成了一份最终被证实为虚假的情报结论，随后又第二次使用 AI 把这份结论包装成军方一向信任的标准情报报告并正式对外分发。这份错误报告引发了一次险情，后续报道甚至称该事件“几乎引发美中开战”，并涉及一艘与中国有关的船只。 这是一个 AI 幻觉在最高风险领域造成实际作战风险的典型案例，因为一条捏造的结论可能升级为核大国之间的军事对抗。它为“AI 辅助分析必须人工复核”、更严格的数据来源与审计追踪要求，以及当 AI 生成情报影响决策时如何界定责任，提供了有力的现实论据。 据报道，同一套流程中出现了两次失误：AI 不仅被用来得出错误的分析结论，还被用来把它套进军方天然信任的标准报告模板，这似乎压制了对内容本身的审查。美国太平洋特种作战司令部和五角大楼均未回应 CNN 的置评请求，涉事的具体 AI 模型或供应商也尚未公开确认。

google\_news · CNN · 9月18日 16:55

**背景**: AI 幻觉指的是听起来合理但事实上错误甚至完全捏造的输出，这是大语言模型一种已被充分记录的通病，根源在于模型预测的是“看起来可能的文本”而非经过核实的事实。各国军队近年越来越多地将这类模型用于情报搜集、战场推演和目标分析，因为它们处理海量数据的速度远超人类分析员。然而情报报告本身带有“经人工核实、值得信赖”的隐含预设，而联合国等国际机构也只是最近才开始就军事领域负责任使用 AI 展开非正式讨论，因此正式规则与问责机制仍很不成熟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://edition.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship">Exclusive: US military had close call after using AI for false...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_%28artificial_intelligence%29">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-hallucinations">What are AI hallucinations? - IBM</a></li>

</ul>
</details>

**标签**: `#ai-safety`, `#military-ai`, `#hallucination`, `#ai-governance`, `#defense-technology`

---

<a id="item-7"></a>
## [Moonshot AI 的 2.8 万亿参数 Kimi K3 上线 Amazon Bedrock](https://news.google.com/rss/articles/CBMijAFBVV95cUxPZEc4TDRPSkJzZUl2bHJoNm5HNkhpcGtBX2U0V1l3dVJDRlh5YkpwRkZaTDkwcDBfZVN3UU1ackFYY0NPMU5sRU5LVVFmRHhySUJwVjZlWXlNTkw4b0swYW1zUVZQSldHV19aTzBfeC1waGFOeGd0MThBOEo5bnVFSDl2VkIxSndKVWZYWA?oc=5) ⭐️ 7.0/10

AWS 宣布，中国实验室 Moonshot AI 的旗舰模型 Kimi K3 现已在 Amazon Bedrock 上线，进一步扩充了这项托管服务所提供的前沿模型阵容。公告本身只是一则简短的上线通知，并未附带定价、吞吐量或基准测试数据。 已经在使用 AWS 的企业开发者，现在可以通过与其他厂商相同的 Bedrock API 调用 Moonshot AI 最强的模型，而无需自行搭建和运维推理基础设施。这也凸显出中国前沿实验室正迅速借助西方超大规模云厂商的应用市场来分发模型。 据公开资料，Kimi K3 是一个拥有 2.8 万亿参数的模型，具备原生视觉能力与 100 万 token 的上下文窗口，面向长周期编码、知识工作与深度推理场景；有报道称其于 2026 年 7 月 16 日公开发布，并承诺在 7 月 27 日前开放全部开源权重。Bedrock 的上线公告并未说明支持的区域、定价档位，也没有交代托管端点所采用的量化方式。

google\_news · Amazon Web Services \(AWS\) · 9月18日 16:52

**背景**: Amazon Bedrock 是 AWS 推出的全托管、无服务器服务，通过统一 API 对外提供多家厂商的基础模型，于 2023 年 4 月发布，并在 2023 年 9 月 28 日正式可用。Kimi K3 是中国 AI 公司 Moonshot AI 的最新旗舰模型，该公司因 Kimi 助手而为人熟知。上下文窗口指的是模型一次能够处理的文本量，100 万 token 的窗口意味着可以在单次请求中处理极其庞大的代码库或文档集合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.ai/ai-models/kimi-k3">Kimi K3: 2.8T Open Model for Coding &amp; Knowledge Work</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Amazon_Bedrock">Amazon Bedrock - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AWS Bedrock`, `#Kimi K3`, `#LLM`, `#Cloud AI`, `#Model Release`

---

<a id="item-8"></a>
## [Anthropic 聘请埃森哲担任首个嵌入式 AI 安全评估方，并承诺投入 10 亿美元](https://news.google.com/rss/articles/CBMipgFBVV95cUxNSnN4LUdjc1JEOHpBaU9kc2hlb3BmX2Nmb1NodlYwbnZ0R1BlRWtxWld2cW1ZdWlMZnQwYWk3bGl0d0JlR3RuZU5PaTE3YkhmRm1JamZfcndhcWZCM3RlN1ZXb09qQ1RJUjRKSmFKS2lxNk9PMTZoR3lfMkVTOXVpaVdpY2JVX3k3N1hiSGREQ3ZtZFdudUkzYm9JLUdiZG1Bc05FSXZR?oc=5) ⭐️ 7.0/10

Anthropic 已选定咨询公司埃森哲（Accenture）作为其首个“嵌入式评估方”，独立监督其 AI 安全实践，并承诺为相关安全与监督工作投入约 10 亿美元。此举被视为其 CEO 达里奥·阿莫代伊（Dario Amodei）近期发表的《We Must Pace the Frontier》（我们必须为前沿减速）慢化提案的首个具体落地，该提案主张让第三方评估人员常驻前沿 AI 实验室内部。 在各国政府和研究者不断呼吁加强 AI 治理之际，这是对前沿 AI 实验室能否真正接受外部安全监督的一次重要检验。如果 Anthropic 的模式行之有效，可能会成为 OpenAI、Google DeepMind 等公司被迫效仿的范本；而如果评估方缺乏真正的独立性和权限，则可能演变为整个行业的公信力问题。 所谓嵌入式评估方，其核心特征是能够持续、深入地接触实验室的内部系统——包括仍在开发中的模型——而不仅仅是拿到一个成品模型进行短期的外部测试。报道中引用的安全专家提醒，嵌入式评估方虽有价值但存在局限，其独立性取决于由谁付费、能公开什么内容，以及是否有权上报甚至叫停某次部署。

google\_news · The Washington Post · 9月18日 22:49

**背景**: Anthropic、OpenAI 等前沿 AI 实验室过去主要依靠内部红队测试，以及在模型发布前进行短期的外部评估。阿莫代伊在随笔中主张，仅靠自愿自律已不足够，并提出三部分方案：在模型开发过程中进行独立监督、推动全行业监管，最终实现全球监管，同时尽量保住商业利益和美国的 AI 领先地位。Anthropic 选择埃森哲这一大型主流咨询公司、而非专业安全非营利组织，颇具意味，因为它把企业级的审计实践引入了过去由 AI 研究机构主导的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/">Anthropic and OpenAI want to embed safety evaluators . | TechCrunch</a></li>
<li><a href="https://www.bbc.com/news/articles/c14dpgm0rg4o">Anthropic boss Dario Amodei calls for AI development to slow down</a></li>
<li><a href="https://www.businessinsider.com/what-is-embedded-evaluator-ai-apocalypse-dario-amodei-hire-2026-9">What Is an Embedded Evaluator , the Top Job AI ... - Business Insider</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Anthropic`, `#AI governance`, `#industry news`, `#responsible AI`

---

<a id="item-9"></a>
## [深度学习助力设计可同时检测与捕获有毒硫气体的材料](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBRTEVadTNTVzRQNHFTRkNKYjMzeWpyZk0tc0xoa3NtSm1BZ0V3Y1g3NWR1TTBxOFh2T3ViZVF3QW9tNjFUZ3JBXzVKeHB2cnAzQ2JJX2RlQmprSzlj?oc=5) ⭐️ 7.0/10

据 EurekAlert\! 报道，科学家利用深度学习设计出既能检测又能捕获有毒硫气体的材料。该工作指向一类多功能材料，可在感知有害气体的同时将其吸附，而不再依赖彼此独立的传感器与吸附剂。 将检测与捕获功能集于一种材料，有望简化工业界监测与治理有害硫排放的方式，减少对分离式传感器和洗涤系统的依赖。这也进一步表明，AI 驱动的材料设计能够缩短传统上缓慢、依赖试错的功能材料发现周期。 目前可获得的摘要并未说明具体的材料体系、模型架构或所用数据集，也未说明候选材料是否在计算筛选之外经过了实验验证。与大多数机器学习材料研究一样，预测结果的可靠性在很大程度上取决于底层训练数据的质量与覆盖范围。

google\_news · EurekAlert\! · 9月18日 21:19

**背景**: 硫化氢（H2S）和二氧化硫（SO2）等有毒硫气体是炼油、采矿及其他工业过程的常见副产物，即使低浓度暴露也会危害健康。传统上，检测这类气体与捕获这类气体由两类不同技术完成：化学传感器与多孔吸附材料。深度学习是指用大规模计算或实测材料性质数据训练神经网络，使研究者能够在计算机上筛选海量假想化合物并挑出少数最有前景的候选者，这一路径通常被称为“AI for science”或 AI 驱动的材料发现。

**标签**: `#deep learning`, `#materials science`, `#toxic gas detection`, `#AI for science`, `#sulfur gases`

---

<a id="item-10"></a>
## [Anthropic 警告：AI 系统正越来越多地构建自身的下一代版本](https://news.google.com/rss/articles/CBMiygFBVV95cUxQNG50OEZHWS00Vmp5clkxR3hKR1RIY0NuLW1pbXhwaV9wNlg2TGUyeU5lemR5Zll1a2NhOTB6cUQ5R3RCM21wNTJ1X2ppWXJTX0djVHpWVUJjUFA4em1qa0NHMDVWVWc4U3pMM0FfZFMyeERkNVBSY2tYX0hRaTFXTkFrNlVoeXgtLXY5SURZLWZ1MG5UX1pmbzRjWGZIMGRCSFhrQWxia1E1ZzBGOUE1VDJnLTdJdXFiREpmc1N3Y1pZM1MwcGJTaGJR?oc=5) ⭐️ 7.0/10

Anthropic 在周四表示，AI 系统正越来越有能力构建自身的未来版本，这加剧了人们对这项强大技术所带来的风险的担忧。后续报道指出，Anthropic 自家的模型 Claude 正在帮助构建它自己的下一个版本。 这一警告来自顶尖前沿 AI 实验室之一，而且针对的是自家产品，这使得长期以来关于递归式自我改进的 AI 安全担忧获得了不同寻常的分量。如果 AI 系统真的承担起越来越多的 AI 研发工作，能力提升的速度可能会超过安全、评估或治理机制的跟进速度。 该报道只是一则简短的新闻，而非技术论文，没有提供任何基准测试、时间表或量化证据来说明 Anthropic 的研发工作中目前有多大比例被交给 AI 系统。值得注意的是，Anthropic 设有专门介绍递归式自我改进的页面，其中表示它正把越来越多的 AI 研发工作交给 AI 系统本身来完成，并称这加快了其工作进度。

google\_news · LinkedIn · 9月18日 19:23

**背景**: 递归式自我改进（RSI）是一种假想过程，即 AI 系统提升自身智能或提升自身改进能力，从而可能带来快速且不断累积的能力增长，有时被称为“智能爆炸”。在 AI 发展史的绝大部分时间里，研发周期的每一步都由人类驱动——写代码、调模型、设计实验；但近期研究显示，AI 系统正越来越多地参与自身的改进，例如修改输出、演化自己的运行框架、用自己生成的数据训练，甚至亲自开展 AI 研究。迄今为止没有任何 RSI 尝试显示出智能爆炸或超级智能的迹象，但研究者警告，这类系统可能以难以预料的方式演化，并有可能超出人类的控制或理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2607.07663v1">Recursive Self-Improvement in AI: From Bounded Self ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Anthropic`, `#self-improving AI`, `#recursive self-improvement`, `#AI risk`

---