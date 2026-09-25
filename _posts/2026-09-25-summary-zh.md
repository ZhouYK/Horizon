---
layout: default
title: "Horizon Summary: 2026-09-25 (ZH)"
date: 2026-09-25 23:03:06 +0000
lang: zh
report: default
---

> 从 143 条内容中筛选出 7 条重要资讯。

---

1. [F-Droid 发布 2.0：十年来最大规模更新](#item-1) ⭐️ 8.0/10
2. [Anthropic 实验：Claude 代理替员工在市场换书](#item-2) ⭐️ 8.0/10
3. [Google Cloud 正式发布 Gemini 3.8 Live 与 Live Avatar](#item-3) ⭐️ 7.0/10
4. [Meta Muse 被曝&quot;Not-a-Mused&quot;零日漏洞，可劫持 macOS 账户](#item-4) ⭐️ 7.0/10
5. [OpenCode 数据页疑似泄露多款未公开模型](#item-5) ⭐️ 6.0/10
6. [微软发布 Copilot 超级应用，整合聊天、编码与智能体](#item-6) ⭐️ 6.0/10
7. [PrismML 将 1-bit Bonsai 大模型带入高通骁龙智能眼镜](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [F-Droid 发布 2.0：十年来最大规模更新](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 8.0/10

2026 年 9 月 24 日，F-Droid 项目发布了官方 Android 客户端 2.0 版本，这是约十年来规模最大的一次更新，此前已经过 14 次测试版发布。新版重做了界面和底层代码，把应用简化为“发现、搜索、我的应用”三大区域，并将在未来数周内陆续推送给用户。 F-Droid 是自由开源 Android 软件的主要分发渠道，因此界面现代化和应用发现能力的提升，会直接影响用户找到并采用开源应用、而非专有商店应用的难易程度。搜索能力（尤其是对中日韩文字支持的加强）的改进，也降低了非英语用户的使用门槛，而这一群体在开源应用市场中长期被忽视。 本次更新改进了应用发现、分类、搜索和筛选功能，现在可以检索应用描述、分类以及翻译内容，并加强了对中日韩文字的搜索支持；同时还带来了更顺畅的安装更新流程和后台检查更新。有两点值得注意：2.0 暂不支持 F-Droid Privileged Extension，并且放弃了对 Android 6 的支持。

telegram · zaihuapd · 9月24日 23:58

**背景**: F-Droid 是一个由社区维护的自由开源 Android 应用目录：它从源代码构建应用并自行签名，用户通过其官方客户端即可获取可复现、无广告、无追踪的软件，而不必依赖 Google Play。F-Droid Privileged Extension 是一个独立组件，需要以系统 &quot;priv-app&quot; 的形式安装（通常需要 root 权限），安装后 F-Droid 就能在不开启“未知来源”的情况下自行安装、更新和删除应用，也无需用户逐次确认安装，功能类似于 Google Play 的便利性。由于该扩展工作在系统层面，其适配往往会滞后于客户端的大版本发布；而放弃 Android 6 意味着仍在使用 Marshmallow 的设备将无法获得 2.0 客户端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://f-droid.org/packages/org.fdroid.fdroid.privileged/">F - Droid Privileged Extension | F - Droid - Free and Open Source...</a></li>
<li><a href="https://github.com/f-droid/privileged-extension">GitHub - f - droid / privileged - extension : mirror of https...</a></li>

</ul>
</details>

**标签**: `#F-Droid`, `#Android`, `#开源`, `#应用商店`, `#版本发布`

---

<a id="item-2"></a>
## [Anthropic 实验：Claude 代理替员工在市场换书](https://www.anthropic.com/research/project-swap) ⭐️ 8.0/10

Anthropic 用 201 名员工做了一项实验：每人先与 Claude 就自己带来的一本书进行简短聊天，随后由 Claude 代理组成的市场替他们互相议价换书，最终带回各自想读的书。仅凭约五分钟的对话，Claude 对书单的排序就与参与者本人的偏好有 61% 的一致度，而且模型越强，成交效率越高。 这项研究以量化方式证明，LLM 代理能够通过简短对话推断人的偏好，并在多代理议价市场中据此行动，这对个性化助手、自动谈判以及代理之间的交易设计都有直接参考价值。它还表明用户愿意把真实决策和预算交给代理：参与者表示愿意把约三成的年度购书预算交给代理打理。 市场未能达到最优配置，主因是代理对参与者的了解不足，而非谈判能力差；参与者的平均满意度为 7.2/10。61% 的书单排序一致度衡量的是偏好推断能力，而非最终的匹配质量，因此“推断偏好”与“真实偏好”之间的差距仍是关键瓶颈。

telegram · zaihuapd · 9月25日 04:40

**背景**: 多代理系统（multi-agent system）指由多个相互作用的智能代理共同完成目标的计算系统，随着大语言模型的发展，它已成为构建专业化 AI 代理团队的实用方式。偏好学习（preference learning）是机器学习的一个分支，研究如何从排序、两两比较和评分中预测偏好，而不是预测绝对标签——这正是代理替人参与谈判所必需的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_system">Multi-agent system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Preference_learning">Preference learning</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM`, `#Anthropic`, `#multi-agent systems`, `#preference learning`

---

<a id="item-3"></a>
## [Google Cloud 正式发布 Gemini 3.8 Live 与 Live Avatar](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-8-live-with-live-avatar-is-now-generally-available) ⭐️ 7.0/10

9 月 25 日，Google Cloud 宣布 Gemini 3.8 Live with Live Avatar 正式全面可用，在 Gemini 实时语音能力之上新增唇形同步的视频头像，并支持 97 种语言的语音到语音对话。配套的 Gemini 3.8 Live Extended Thinking 模型（提供高推理能力的音频到音频处理）仍处于私有预览阶段。 这次发布把此前仅处于预览状态的实验性功能变成了可用于生产的企业级产品，开发者可以构建不仅能说话、还能呈现对话头像的智能体，而不再局限于纯语音交互。由于同时提供美国和欧洲端点、预置吞吐量以及严格的数据治理，它面向的是客服、培训、虚拟主播等企业级场景，而非个人爱好者的小型演示。 自定义头像需要通过企业白名单审核，所有生成的音频和视频都带有 Google DeepMind 的隐形溯源技术 SynthID 水印。Google Cloud 尚未公布头像生成链路的定价或延迟数据，而推理能力更强的 Extended Thinking 版本仍未向大众开放。

telegram · zaihuapd · 9月25日 03:09

**背景**: Gemini Live 是 Google 面向低延迟对话场景的模型系列，它原生处理语音，而不是先把音频转成文字再转回语音，因此能够实现自然的轮流对话和情感语调。Live Avatar 在此基础上进一步生成同步的视觉形象，让智能体除了声音之外还有一张“脸”。SynthID 是 Google DeepMind 的水印系统，会把难以察觉的信号嵌入 AI 生成的图像、音频、文本和视频中，便于日后识别合成内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-8-live-with-live-avatar-is-now-generally-available">Gemini 3.8 Live with Live Avatar is now generally available | Google Cloud Blog</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/">Introducing Gemini 3.8 Live with Live Avatar</a></li>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#Google Cloud`, `#Gemini`, `#Generative AI`, `#Digital Avatars`, `#Multimodal AI`

---

<a id="item-4"></a>
## [Meta Muse 被曝&quot;Not-a-Mused&quot;零日漏洞，可劫持 macOS 账户](https://www.ithome.com/1/007/126.htm) ⭐️ 7.0/10

安全研究员 Patrick Wardle 披露了 Meta 旗下 macOS 应用 Muse 的一个零日漏洞，并将其命名为&quot;Not-a-Mused&quot;。攻击者可通过修改隐藏的语音/听写配置项劫持账户并窃取认证 Token，Meta 事后已发布热修复，移除了相关的调试功能。 由于 Muse 以用户身份运行并拥有较广的系统与账户权限，一旦认证 Token 被窃取，攻击者即可访问邮件、日历和 WhatsApp 等关联服务，使这个 AI 智能体本身成为高价值攻击面。该事件也折射出随着 AI 助手在用户设备上获得越来越深的权限，&quot;智能体即攻击面&quot;正在成为一类新的普遍风险。 据技术分析，该漏洞位于 macOS 应用包 com.meta.endo 中，攻击者只需通过 \`defaults write\` 修改一个未公开的偏好设置键（endo\_voyager\_dictation\_endpoint），或诱导用户执行一条终端命令即可利用，无需复杂的恶意软件。Meta 的修复方式是移除该调试能力而非发布完整的补丁版本，因此用户应尽快把 Muse 更新到最新版本。

telegram · zaihuapd · 9月25日 07:27

**背景**: Muse 是 Meta 于 2026 年 9 月推出的个人 AI 智能体应用，官方将其定位为安全、私密、能主动帮用户完成任务的助手，上线六天内下载量约 90.2 万次并登顶 App Store。Patrick Wardle 是知名的 macOS 安全研究员，他此前披露的多个本地权限与偏好设置键漏洞均促使厂商发布补丁。与经典的远程漏洞不同，&quot;本地&quot;漏洞要求攻击者已在目标机器上运行代码，或诱导用户执行命令，通常危害等级较低，但在定向攻击中风险显著上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eyestech.in/meta-muse-zero-day-privilege-inversion-os-agents/">Meta Muse Zero-Day: Privilege Inversion in OS Agents</a></li>
<li><a href="https://tech.yahoo.com/cybersecurity/articles/muse-undocumented-endpoint-turns-macos-192808424.html">Muse ’s Undocumented Endpoint Turns macOS Agent Into a Local...</a></li>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for Everyone</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#macOS`, `#Meta`, `#zero-day`

---

<a id="item-5"></a>
## [OpenCode 数据页疑似泄露多款未公开模型](https://opencode.ai/zh/data/moonshot/kimi-k4) ⭐️ 6.0/10

OpenCode 的模型数据页上出现了多个从未官方发布的模型条目，包括 Kimi K4、GLM 5.5 Flash、GLM 5.4、DeepSeek V4.1 Pro、腾讯 hy4、Qwen3.8 Max Preview 以及 Meta muse-spark-1.4-contributor。这些页面目前均显示无使用量、独立用户为 0，因此该发现被描述为疑似泄露而非正式发布。 如果这些条目属实，它们将暗示中国和美国的几家头部前沿模型实验室即将发布新版本，让社区提前一窥其命名与版本规划。即便未经证实，这一事件也说明一个被广泛使用的开发者平台的元数据，可能会意外成为传递路线图信号的渠道。 目前证据相当薄弱：这些页面没有基准测试成绩、参数量、价格或上下文窗口等信息，且每个列出的模型都显示消耗 token 为 0、独立用户为 0。这些链接遵循 OpenCode 常规的单模型数据路径格式（例如 opencode.ai/zh/data/moonshot/kimi-k4），Meta 那条条目也同样存在于 OpenCode 的俄语区域页面下，说明这些页面是在所有语言版本中批量生成的，而非单条误发的链接。

telegram · zaihuapd · 9月25日 05:47

**背景**: OpenCode 是一个快速成长的开源 AI 编程智能体，GitHub 星标已超过 16 万，同时还运营着一个名为 Zen 的精选模型目录，专门针对编程智能体场景做测试与基准评估。除此之外，它还会公开每个受支持模型的数据页，记录 token 使用量、周排名、成本、缓存占比和会话数等信息，这些未公开模型的名称正是因此暴露出来。涉及的名字都属于知名模型家族：Moonshot AI 的 Kimi、智谱的 GLM、DeepSeek、阿里的 Qwen、腾讯的 Hy（原混元，采用开放权重的混合专家架构），以及 Meta 的 Muse Spark 推理模型系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://www.siliconflow.com/models/hy4-preview">SiliconFlow – AI Infrastructure for LLMs &amp; Multimodal Models</a></li>
<li><a href="https://openrouter.ai/meta/muse-spark-1.3">Muse Spark 1 .3 - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Leak`, `#LLM`, `#Industry News`, `#Rumor`

---

<a id="item-6"></a>
## [微软发布 Copilot 超级应用，整合聊天、编码与智能体](https://www.theverge.com/news/1000532/microsoft-copilot-super-app-chat-coding-autopilot) ⭐️ 6.0/10

微软今日正式发布新版 Copilot「超级应用」，将 AI 聊天、编码与智能体能力整合到 Home、Code、Autopilot 三个标签页中。此前名为 Scout 的个人 AI 助手正式更名为 Autopilot，定位为云端「数字同事」。 此举把微软此前分散的多个 Copilot 入口收拢为统一的智能体前端，清晰表明微软把下一阶段 AI 战略押注在自主智能体而非单纯的聊天问答上。最直接受影响的是 Frontier 早期访问用户、开发者，以及正在评估微软云端「数字同事」与其他厂商智能体平台的企业客户。 Home 与 Code 将在未来数周内向 Frontier 用户推送，Autopilot 则于本月晚些时候开启私有预览；Code 允许用户创建应用或自动化流程并分享给同事。总体来看，此次发布更多是整合与更名（Scout 变为 Autopilot），而非底层技术的全新突破。

telegram · zaihuapd · 9月25日 12:15

**背景**: Microsoft Copilot 是微软旗下 AI 助手的统一品牌，既包括面向消费者的聊天应用，也包括嵌入 Word、Excel、Outlook、Teams 等 Microsoft 365 应用的 Copilot Chat 体验。Frontier 是微软的早期访问计划，让报名用户提前试用 Agent Builder 等实验性 Copilot 功能。这里的「智能体（agent）」指的是能够自主执行多步骤任务的 AI——例如创建应用、运行自动化流程或充当长期在线的同事——而不再只是回答单轮提问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.inside.com.tw/article/42479-microsoft-copilot-home-code-autopilot-usage-based-billing">微 軟 Copilot 推出 Home、Code 與數位 同 事 Autopilot ... - INSIDE</a></li>
<li><a href="https://copilot.cloud.microsoft/">Copilot | ИИ-чат для работы</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Copilot`, `#AI Agents`, `#Product Launch`, `#Developer Tools`

---

<a id="item-7"></a>
## [PrismML 将 1-bit Bonsai 大模型带入高通骁龙智能眼镜](https://techcrunch.com/2026/09/24/prismml-brings-its-tiny-llms-to-qualcomm-powered-smart-glasses/) ⭐️ 6.0/10

AI 实验室 PrismML 发布了一个 20 亿参数的 1-bit Bonsai 视觉语言模型，可完全本地运行在高通 Snapdragon AR1 Gen 1 智能眼镜平台上，并在高通 Snapdragon Summit 上做了演示。该模型由一个 17 亿参数的 1-bit 语言模型和一个 3 亿参数的 4-bit 视觉编码器组成，佩戴者无需经过云端往返即可就眼前所见进行实时提问。 这表明激进的 1-bit 量化可以把多模态大模型推理推到日常智能眼镜这类功耗和内存都极其受限的硬件上，而这一品类此前严重依赖手机连接或云端算力。如果该方案在生产环境中站得住脚，端侧视觉助手将在可穿戴设备、AR 设备以及其他对延迟、隐私和续航敏感的边缘硬件上真正变得可行。 Bonsai 是一个真正的端到端 1-bit 模型——嵌入层、注意力层、MLP 层和语言模型输出头全部为 1-bit，没有保留高精度“逃生通道”；PrismML 声称相比全精度可实现约 14 倍的内存占用缩减，且精度几乎无损（8B 模型体积约 1.15 GB，1.7B 模型在 iPhone 17 Pro Max 上约 130 tokens/秒）。此次眼镜演示的上下文长度仅为 1024 tokens，且 PrismML 尚未公布哪款智能眼镜会搭载该模型。

telegram · zaihuapd · 9月25日 13:06

**背景**: TinyML 是机器学习的一个分支，专注于在微控制器和边缘设备等低功耗、资源受限的嵌入式系统上运行模型，以牺牲部分原始能力换取低延迟和不依赖云连接的独立性。量化通过以更低精度存储权重来压缩模型；传统方案很少低于约 2 bit，因此端到端 1-bit 网络是一种相当激进的做法。Snapdragon AR1 Gen 1 是高通专为轻量级 AR 和智能眼镜设计的芯片平台，其电池、散热和内存条件都极为苛刻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/bonsai-1-bit-vlm-smart-glasses-snapdragon">Bonsai on Smart Glasses: A 2B 1 -Bit VLM on Snapdragon</a></li>
<li><a href="https://prismml.com/news/bonsai-8b">PrismML — Announcing 1 - bit Bonsai : The First Commercially Viable...</a></li>
<li><a href="https://rits.shanghai.nyu.edu/ai/prismmls-1-bit-bonsai-llms-8b-model-in-1-15-gb/">PrismML’s 1 - Bit Bonsai LLMs: 8B Model in 1.15 GB</a></li>

</ul>
</details>

**标签**: `#On-device AI`, `#LLM`, `#Smart Glasses`, `#Qualcomm`, `#TinyML`

---