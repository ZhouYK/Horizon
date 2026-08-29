---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29 04:33:53 +0000
lang: zh
report: ai
---

> 从 292 条内容中筛选出 10 条重要资讯。

---

1. [腾讯开源混元 Hy4 预览版：770B MoE，百万上下文](#item-1) ⭐️ 9.0/10
2. [腾讯混元开源旗舰模型 Hy4preview：770B 参数与 1M 上下文](#item-2) ⭐️ 9.0/10
3. [漏洞传闻足以让 AI 代理发现安全漏洞，OCaml 维护者发现](#item-3) ⭐️ 8.0/10
4. [Anthropic 推出框架，让 AI 智能体控制硬件](#item-4) ⭐️ 8.0/10
5. [腾讯元宝接入混元 Hy4preview，开启两周免费试用](#item-5) ⭐️ 8.0/10
6. [腾讯开源混元 Hy4preview：770B 参数旗舰模型](#item-6) ⭐️ 8.0/10
7. [Anthropic 发布模型硬件标准 MHS，AI 智能体迈向物理设备控制](#item-7) ⭐️ 8.0/10
8. [Anthropic 发布具身 AI 硬件标准 MHS](#item-8) ⭐️ 8.0/10
9. [Midjourney V8.2 推出图像编辑模型，支持指令微调和画布扩展](#item-9) ⭐️ 8.0/10
10. [AI 巨头警告网络攻击将加剧 呼吁各国优先防御](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [腾讯开源混元 Hy4 预览版：770B MoE，百万上下文](https://www.aibase.com/news/30698) ⭐️ 9.0/10

腾讯在 Hugging Face、GitHub、ModelScope 和 Gitcode 上开源了混元 Hy4 预览版模型，总参数 770B，激活参数 49B，上下文窗口达 100 万 token。该模型还接入了腾讯云 TokenHub 和 OpenRouter，据称在生产力任务的盲测中优于 GLM-5.3 和 Kimi K3。 这次发布将 770B 参数的开源模型带给社区，可能挑战现有开源 LLM 的性能上限，让开发者更容易触达顶级规模。百万 token 的上下文使得处理整本书或大型代码库成为可能，对基于开源模型进行研究的科研人员和企业而言意义重大。 混元 Hy4 预览版采用混合专家（MoE）架构，每个 token 仅激活 770B 参数中的 49B，从而在规模与推理效率之间取得平衡。该模型托管在 Hugging Face、GitHub、ModelScope 和 Gitcode 等多个平台，并可通过腾讯云 TokenHub 和 OpenRouter 访问。

aibase · AIbase · 8月28日 15:27

**背景**: 混合专家（MoE）是一种架构，它对于每个 token 只稀疏激活模型参数中的一小部分，从而使得非常大的模型能以比同规模稠密模型更低的计算成本运行。上下文长度（即上下文窗口）指的是模型一次能处理的最大 token 数量；更长的上下文使模型能够处理更长的文档或将更大的代码库保留在内存中。这两个概念正是混元 Hy4 预览版核心特性的基础：巨大参数量和百万 token 上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://researchaudio.io/p/mixture-of-experts-moe-in-large-language-models">Mixture of Experts ( MoE ) in Large Language Models</a></li>
<li><a href="https://datanorth.ai/blog/context-length">LLM Context Length &amp; Context Window Explained (2026)</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open-source`, `#Tencent`, `#Hunyuan`

---

<a id="item-2"></a>
## [腾讯混元开源旗舰模型 Hy4preview：770B 参数与 1M 上下文](https://www.aibase.com/news/30694) ⭐️ 9.0/10

8 月 28 日，腾讯混元发布了开源旗舰大语言模型 Hy4preview，总参数量达 7700 亿，激活参数为 490 亿，上下文长度达 100 万 token。该模型已在 HuggingFace、GitHub、ModelScope、腾讯云 TokenHub 和 OpenRouter 等平台上线。 这是一次来自顶级科技公司的重要开源发布，巨大的参数量和超长上下文有望推动真实生产力应用。它为开发者在开放权重大模型生态中提供了强有力的新选择，并可能加剧中国及全球 AI 实验室之间的竞争。 Hy4preview 采用了混合专家（MoE）架构，每个 token 只激活 770B 参数中的 49B，从而降低了推理成本。该模型基于软件工程、游戏、金融和安全等领域的专家数据构建，用户还可通过 WorkBuddy/CodeBuddy、元宝和 IMA 进行体验。

aibase · AIbase · 8月28日 15:27

**背景**: 混合专家（MoE）是一种使用多个专门子模型（即“专家”）来提升模型质量的技术，与同等总规模的密集模型相比，其计算成本更低。在 MoE 模型中，每个 token 只激活一部分参数，因此“激活参数”指的是在前向传播中实际使用的参数。100 万 token 的上下文窗口允许模型一次处理整本书长度的文档，但如何有效利用超长上下文中的信息仍是一个待解决的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts? | IBM</a></li>
<li><a href="https://www.mindstudio.ai/blog/claude-1m-token-context-window-ai-agents">Claude 1M Token Context Window: What It Means for AI Agents and Long-Running Tasks | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Tencent Hunyuan`, `#open-source`, `#large language model`

---

<a id="item-3"></a>
## [漏洞传闻足以让 AI 代理发现安全漏洞，OCaml 维护者发现](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) ⭐️ 8.0/10

剑桥大学教授、OCaml 核心维护者 Anil Madhavapeddy 报告称，OCaml 项目的安全补丁在讨论后约十分钟内，他的网站就收到了针对百分号编码路径遍历序列的探测，表明自动化 AI 代理在监视公开仓库。他展示了现代编码智能体仅凭一个漏洞传闻就能发现可利用的漏洞——在 Claude Fable 拒绝任务后，他改用 DeepSeek V4 Pro 完成演示。 这表明漏洞披露与主动利用之间的时间窗口已从数天缩短到数分钟，与现有开源保密发布（embargo）实践不相容。维护者和安全团队必须制定新的流程来安全地讨论和发布补丁，整个生态也应预料到 AI 驱动的利用尝试和安全报告将激增。 rclone 维护者 Nick Craig-Wood 在 Hacker News 评论中证实，rclone 项目头十年通过 GitHub 收到约 20 份安全披露，而仅上个月就收到超过 40 份；其中约 75% 含有值得调查的内容。他还指出，GitHub 分配 CVE 的时间从 2-3 天延长到 3-4 周，导致点版本发布时只能先在更新日志中标注“CVE-PENDING”。

rss · Simon Willison · 8月28日 22:12

**背景**: 百分号编码（percent-encoding）是一种在 URI 中对字符进行编码的机制，而目录遍历攻击利用 ../ 或其编码变体来访问 Web 服务器根目录之外的文件；针对百分号编码路径遍历序列的探测表明攻击者正积极检查补丁漏洞是否可被利用。OCaml 是一种多范式通用编程语言，常用于静态分析、形式化方法和系统编程。AI 编码智能体已具备越来越强的自动分析代码与补丁差异、发现并利用漏洞的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Directory_traversal_attack">Directory traversal attack - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OCaml">OCaml - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_%28product%29">DeepSeek (product)</a></li>

</ul>
</details>

**社区讨论**: Hacker News 讨论中，rclone 维护者 Nick Craig-Wood 证实安全披露数量剧增，即使使用 AI 工具进行分诊，也耗费了大量时间。讨论情绪警觉但务实，聚焦于实际影响：保密发布模式正在失效，GitHub 的 CVE 流程成为瓶颈，开源维护者需要新的支持机制。

**标签**: `#security`, `#AI agents`, `#software supply chain`, `#OCaml`, `#exploit discovery`

---

<a id="item-4"></a>
## [Anthropic 推出框架，让 AI 智能体控制硬件](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQc1c5RE5HOUJ5Rlo0OXB3d0F0aVY3WFpqX29jcnAyblU1ZEs5Vy04MXpJNHNKeUprLXNOUlRpMkdPbmZkSVY1ZjVTU2pjM2J1d0VLQTc3b2lOU0dyWFZMVF93U285d1VGNE54UFdwb2wyWDZOV3JwdjdUbkJUVXIxRGNMWmtiR1g1cFZHcXN2ekJRZ0tPYlJXNHdfZzcyb085QUFwaU5sazhocVU?oc=5) ⭐️ 8.0/10

Anthropic 宣布了一个新框架，允许 AI 智能体直接控制硬件设备。这标志着 AI 自动化从纯软件领域扩展到物理系统控制。 这可能催生广泛的现实世界自动化应用场景，从 IT 基础设施管理到机器人技术和设备故障排除。这也标志着行业趋势正朝着赋予 AI 智能体对物理系统更多自主权的方向发展。 该框架旨在与 Anthropic 的 AI 模型配合使用，可能主要面向企业开发者。关于支持的硬件类型和集成方式等更多技术细节，公告中尚未详细说明。

google\_news · Computerworld · 8月28日 18:06

**背景**: AI 智能体是利用大型语言模型自主执行任务的软件程序，例如浏览网页或调用 API。将这种能力扩展到硬件，可以让智能体与物理世界交互，例如向计算机或机器人发送指令。这反映了 AI 行业正推动智能体从聊天式工具向能够执行现实世界任务的可操作系统的更广泛趋势。

**标签**: `#Anthropic`, `#AI agents`, `#hardware control`, `#framework`, `#AI/ML`

---

<a id="item-5"></a>
## [腾讯元宝接入混元 Hy4preview，开启两周免费试用](https://www.aibase.com/news/30699) ⭐️ 8.0/10

8 月 28 日，腾讯元宝在全球范围内率先集成混元开源旗舰模型 Hy4preview，并提供两周免费试用。该模型已在 Hugging Face 等平台开源。 这标志着腾讯以高参数旗舰模型进入竞争激烈的开源大模型领域，强化了其在企业和生产力场景中的 AI 生态。这也表明将先进开源模型整合到消费级助手产品中的行业趋势。 Hy4preview 采用混合专家（MoE）架构，总参数 7700 亿，每个 token 激活 490 亿参数，支持 100 万 token 上下文。Hy4preview 的免费试用期为两周，而混元 Hy3 的免费访问已延长至 9 月 30 日。

aibase · AIbase · 8月28日 16:27

**背景**: 混元是腾讯推出的大语言模型系列，Hy4 preview 是其新一代 MoE 旗舰模型。MoE 架构通过为每个输入只激活部分专家，使模型规模扩大而不按比例增加计算量。100 万 token 的上下文窗口让模型能一次性处理超长文档。开源此类模型能让全球开发者自由使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent-Hunyuan/Hy4-preview · GitHub</a></li>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/Hy4-preview · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Tencent`, `#Hunyuan`, `#LLM`, `#Open Source`

---

<a id="item-6"></a>
## [腾讯开源混元 Hy4preview：770B 参数旗舰模型](https://www.aibase.com/news/30697) ⭐️ 8.0/10

腾讯发布了混元旗舰模型 Hy4preview 的预览版，总参数 770B、激活参数 49B，支持 1M 上下文，并已开源。在内部盲测中，它在编程、办公、科学等任务上的综合表现超过同类竞品，跻身开源模型第一梯队。 此举使腾讯模型直接跻身开源 AI 第一梯队，让开发者可以无限制地使用前沿规模的 MoE 架构。这也凸显了大厂将最强模型以开放权重形式发布的新趋势，可能重塑大语言模型生态的竞争格局。 该模型采用 Mixture-of-Experts（MoE）架构，每次 token 只激活 770B 参数中的 49B，保证了推理效率。消息还提到 Hy4preview 已在腾讯内部多个领域应用，但公告中未提供量化评测结果和具体许可证条款。

aibase · AIbase · 8月28日 15:27

**背景**: Mixture of Experts（MoE）是一种神经网络设计，它将前馈层拆分为多个专门的“专家”子网络，并通过路由器只为每个 token 激活最相关的几个专家。密集模型每次推理会激活全部参数，而 MoE 模型总参数虽高、激活参数却较低，从而降低计算成本。这使得千亿级参数模型也可以在常见硬件上运行并保持较强性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts ( MoE )</a></li>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between Total and...</a></li>
<li><a href="https://researchaudio.io/p/mixture-of-experts-moe-in-large-language-models">Mixture of Experts ( MoE ) in Large Language Models</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open-source`, `#Tencent`, `#Hunyuan`

---

<a id="item-7"></a>
## [Anthropic 发布模型硬件标准 MHS，AI 智能体迈向物理设备控制](https://www.aibase.com/news/30693) ⭐️ 8.0/10

Anthropic 发布了模型硬件标准（MHS），这是一套让 AI 智能体安全操作物理设备的共享规范，目前以研究预览形式提供给部分科研实验室和先进制造商。MHS 源自与霍华德·休斯医学研究所（HHMI）Janelia 研究园区的合作，目标是让 AI 智能体无需定制集成即可发现、读取并控制不同厂商的硬件。 MHS 意义重大，因为它连接了虚拟 AI 智能体与物理设备，降低了在科研和制造领域将 AI 接入真实设备的工程成本。如果该标准被广泛采用，有望加速药物发现实验、显微镜操作、机械臂控制以及量子计算机激光校准等任务。 该标准提供了一套通用接口，AI 智能体可据此发现、读取和控制设备，工程师无需再为每台设备单独构建集成方案。MHS 目前仍处于预览阶段，仅向首批研究实验室和先进制造商开放。

aibase · AIbase · 8月28日 14:27

**背景**: AI 智能体是由大语言模型驱动的软件系统，能够规划和执行任务。此前，让这类智能体操作物理仪器需要为每台机器编写定制软件，成本高且难以规模化。MHS 旨在将设备控制标准化，使同一个智能体能够操作多种工具，并把安全性作为关键重点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-hardware-standard-research-preview">Previewing the Model Hardware Standard \ Anthropic</a></li>
<li><a href="https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/">Anthropic&#x27;s new hardware standard lets AI agents control the physical world - Ars Technica</a></li>
<li><a href="https://modelhardwarestandard.com/">Model Hardware Standard</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#hardware standard`, `#Anthropic`, `#robotics`, `#AI safety`

---

<a id="item-8"></a>
## [Anthropic 发布具身 AI 硬件标准 MHS](https://www.aibase.com/news/30692) ⭐️ 8.0/10

8 月 27 日，Anthropic 推出了 Model Hardware Standard（MHS）研究预览版，这是一项让 AI 智能体安全操作实体设备的共享规范。这标志着 Anthropic 首次公开进入具身 AI 领域，覆盖机器人、自动驾驶车辆和科学仪器等设备。 此举将 Anthropic 在互操作性方面的努力从软件扩展到物理系统，可能影响 AI 智能体在机器人和自主系统中控制硬件的方式。如果被广泛采用，MHS 可能成为 AI 驱动的科学研究和先进制造的基础层。 MHS 支持对机械臂、显微镜等设备进行统一控制和通信，并在驱动器层面（智能体之下）强制执行安全限制。该项目始于 Anthropic 与 HHMI Janelia 研究园区的合作，目前正向首批科研实验室和先进制造商开放预览。

aibase · AIbase · 8月28日 14:27

**背景**: 具身 AI 是指嵌入物理实体、通过传感器感知环境并通过执行器采取行动的 AI 系统。Anthropic 此前推出了用于软件互操作的 Model Context Protocol（MCP），而 MHS 被视为对应的硬件标准，让模型拥有操作实体机器的“身体”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-hardware-standard-research-preview">Previewing the Model Hardware Standard \ Anthropic</a></li>
<li><a href="https://modelhardwarestandard.com/">Model Hardware Standard</a></li>
<li><a href="https://coursiv.io/blog/model-hardware-standard">Model Hardware Standard : AI Agents Meet Hardware | Coursiv Blog</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#hardware standard`, `#embodied AI`, `#robotics`, `#AI infrastructure`

---

<a id="item-9"></a>
## [Midjourney V8.2 推出图像编辑模型，支持指令微调和画布扩展](https://www.aibase.com/news/30690) ⭐️ 8.0/10

Midjourney 发布了 V8.2 图像编辑模型的测试版，突破了仅限文本生成的传统模式，集成了指令微调、多图像参考和修复（inpainting）功能。这使得专业视觉创作更加精确和可控。 此次更新对依赖 AI 图像生成的专业人士意义重大，为编辑流程带来了更强的控制力和精确度。它标志着生成式 AI 从单纯的图像生成向功能完善的编辑工具转变。 该模型支持指令微调，用户可以通过特定提示引导模型，并支持修复功能，用于填充或替换图像的局部区域。它还包含画布扩展功能，让创作者能够在原始尺寸之外扩展图像。

aibase · AIbase · 8月28日 11:27

**背景**: 指令微调是一种用于改进大型语言模型的技术，通过在带标注的指令提示和期望输出数据集上训练模型来完成。多图像参考允许模型从多个源图像中提取并组合视觉元素。图像修复是一种计算机视觉技术，用于填充图像中缺失或损坏的部分，常用于移除物体或修复旧照片。这些功能共同实现了更精确、专业级的图像编辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/instruction-tuning">What Is Instruction Tuning ? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Inpainting">Inpainting - Wikipedia</a></li>
<li><a href="https://www.rundiffusion.com/multi-image-prompt-guide">Multi - Image Prompt Guide: How to Target, Annotate, and Reference ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Midjourney`, `#Image Editing`, `#Generative Models`, `#Creative Tools`

---

<a id="item-10"></a>
## [AI 巨头警告网络攻击将加剧 呼吁各国优先防御](https://www.aibase.com/news/30683) ⭐️ 8.0/10

OpenAI、Anthropic、微软、谷歌、亚马逊等 116 家机构联合发出警告，称 AI 驱动的网络攻击将在未来数月加剧，呼吁政府和企业在发布模型前将网络安全列为最高优先事项，并加速可信访问计划。 这一前所未有的跨行业共识标志着 AI 安全讨论从能力转向防御，可能促使监管机构和企业在一波预期的攻击浪潮前加强系统防护。 该警告特别呼吁加快部署可信访问计划，让安全研究人员在模型公开发布前进行测试，并强调政府和企业共同承担抵御 AI 驱动威胁的责任。

aibase · AIbase · 8月28日 09:27

**背景**: AI 驱动的网络攻击利用深度伪造、多态恶意软件和自适应钓鱼等技术绕过传统防护。尽管这些攻击相当复杂，但仍有许多利用常见的弱点，如凭证管理不善，因此多因素认证和补丁更新等基本安全措施依然有效。安全团队还会开展 AI 红队测试，由授权专家模拟真实攻击，在部署前发现 AI 系统的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://abnormal.ai/glossary/ai-enabled-cyberattacks">What Are AI - Enabled Cyberattacks ? Why They&#x27;re... | Abnormal AI</a></li>
<li><a href="https://www.linkedin.com/pulse/why-ai-enabled-cyberattacks-signal-deeper-governance-failure-d9b8c">Why AI - Enabled Cyberattacks Signal a Deeper Governance Failure...</a></li>
<li><a href="https://medium.com/@kalkinetra/why-ai-red-teaming-is-essential-the-non-negotiable-layer-of-safety-77631d36623b">Why AI Red Teaming is Essential: The Non-Negotiable... | Medium</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#policy`, `#tech industry`, `#risk warning`

---