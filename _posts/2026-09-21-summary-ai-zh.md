---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21 23:04:45 +0000
lang: zh
report: ai
---

> 从 266 条内容中筛选出 10 条重要资讯。

---

1. [微软用 AI 智能体将 GitHub Copilot 运行时从 TypeScript 迁移到 Rust](#item-1) ⭐️ 8.0/10
2. [Cloudflare Python Workers 结束两年预览期正式 GA](#item-2) ⭐️ 7.0/10
3. [得州州长 Abbott 暂停数据中心州级许可，等待电网审计完成](#item-3) ⭐️ 7.0/10
4. [不列颠哥伦比亚省就坦布勒岭枪击案起诉 OpenAI](#item-4) ⭐️ 7.0/10
5. [联合国小组呼吁加强对先进 AI 代理的保障措施](#item-5) ⭐️ 7.0/10
6. [上诉法院警告「AI 垃圾内容」正威胁法院正常运作](#item-6) ⭐️ 7.0/10
7. [开发者曝光 OpenAI 广告追踪链：\_\_obi Cookie 跨站关联浏览足迹](#item-7) ⭐️ 7.0/10
8. [阿里 Qwen 团队开源 7B 参数图像模型 Qwen-Image-2.1](#item-8) ⭐️ 7.0/10
9. [Step 5 Preview：完全开源的 600B 稀疏 MoE，每次推理仅激活 27B 参数](#item-9) ⭐️ 7.0/10
10. [澳大利亚呼吁全球放缓 AI 开发竞赛](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [微软用 AI 智能体将 GitHub Copilot 运行时从 TypeScript 迁移到 Rust](https://www.aibase.com/news/31240) ⭐️ 8.0/10

微软利用 AI 智能体将 GitHub Copilot 运行时从 TypeScript 完全重写为超过 80 万行生产级 Rust 代码，将原本约 43 万行 TypeScript 转换过来，据称仅花费约 12 万美元的 token 成本和一个工程师三周的工作量，并分摊到 128 个 pull request 中。 这是一个极具说服力的例证，说明 AI 智能体可以在数周而非数年内完成生产级规模的编程语言迁移，可能重塑工程团队对性能关键型服务进行大规模重写的规划方式。 新的 Rust 运行时为 Copilot CLI、Copilot 应用、SDK 以及云端 Agent 提供支持，覆盖 VS Code、Visual Studio、Excel、Outlook 和 PowerPoint，据称实现了 15.9 倍的性能提升；整个迁移通过 128 个 pull request 分阶段合入并逐步发布。

aibase · AIbase · 9月21日 18:01

**背景**: Copilot 运行时最初使用基于 Node.js 的 TypeScript 编写，这种方式虽然能让功能开发非常迅速，却在规模化时限制了启动速度和服务性能。Rust 是一门编译型系统编程语言，在内存效率和执行速度上远优于 Node.js，因此成为重写性能敏感型服务的热门选择。GitHub 表示此次迁移是借助自家的 Copilot 应用和 Copilot CLI 完成的，也就是说大部分新 Rust 代码由 AI 智能体在人工审查下编写。AI 智能体能否可靠地完成代码迁移仍存争议，批评者指出大型复杂代码库依然需要大量人工介入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/">Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog</a></li>
<li><a href="https://virtuslab.com/blog/ai/agents-for-legacy-code-migration">Agents for Legacy Code migration</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Rust`, `#TypeScript`, `#code migration`, `#GitHub Copilot`

---

<a id="item-2"></a>
## [Cloudflare Python Workers 结束两年预览期正式 GA](https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/) ⭐️ 7.0/10

Cloudflare 宣布 Python Workers 正式 GA，在经历约两年的预览期后，Python 成为 Cloudflare Developer Platform 上的一等公民、获得完整支持的语言。该发布公告由 Gyeongjae Choi、Dominik Picheta 和 Hood Chatham 署名，其中两人是 Pyodide 的核心维护者。 Python 是数据、自动化与 AI 工具领域使用最广泛的语言之一，它在一线 serverless 边缘平台上成为稳定选项，大幅降低了这类开发者把代码部署到离用户更近位置的难度。这也表明 Cloudflare 正在加深对整个 Python 生态的投入，而不是把 Python 当作 JavaScript 优先运行时上的一个小众附加功能。 其实现方式是通过 Pyodide 把 Python 编译为 WebAssembly，并在 Cloudflare 基于 V8 的 workerd 运行时中执行，这意味着 multiprocessing 和 threading 在 WebAssembly 虚拟机中都不可用。本地开发体验也值得一提：pywrangler 工具（在 PyPI 上以容易混淆的名字 workers-py 发布）会在本地完整模拟整套技术栈，其中包括一个 123MB 的 workerd 二进制文件，在 V8 中执行 WebAssembly 里的 Pyodide。

rss · Simon Willison · 9月21日 22:25

**背景**: Pyodide 是把 CPython 移植到 WebAssembly/Emscripten 的项目，使 Python（包括 NumPy、pandas 等许多 C 扩展包）能在浏览器和 Node.js 中运行，最初由 Mozilla 在 2018 年创建。workerd 是 Cloudflare 开源的 JavaScript/Wasm 服务端运行时，与驱动 Cloudflare Workers 的代码同源，Wrangler 也用它做本地开发。Python Workers 把两者结合起来：Python 代码经 Pyodide 编译成 WebAssembly，再在 Cloudflare 边缘网络上的 workerd 中执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyodide.org/en/stable/index.html">Pyodide — Version 314.0.7</a></li>
<li><a href="https://github.com/cloudflare/workerd">GitHub - cloudflare / workerd : The JavaScript / Wasm runtime that...</a></li>
<li><a href="https://developers.cloudflare.com/changelog/2025-12-08-python-pywrangler/">Easy Python package management with Pywrangler · Changelog</a></li>

</ul>
</details>

**标签**: `#cloudflare-workers`, `#python`, `#webassembly`, `#serverless`, `#edge-computing`

---

<a id="item-3"></a>
## [得州州长 Abbott 暂停数据中心州级许可，等待电网审计完成](https://wabx.net/2026/09/21/texas-gov-abbott-halts-all-state-issued-permits-for-data-centers-until-grid-audit-is-complete/) ⭐️ 7.0/10

据一则标注日期为 2026 年 9 月 21 日的报道，得克萨斯州州长 Greg Abbott 已暂停所有由州政府签发的数据中心许可，直至对该州电网的审计完成。该消息仅有标题，没有正文、官方声明或机构确认，其来源与日期也被标注为存疑。 得克萨斯州已成为美国最大的数据中心和 AI 基础设施市场之一，因此全州范围的许可冻结可能推迟甚至打乱已规划的超大规模及 AI 训练园区建设。由于这类设施是新增电力需求增长最快的来源之一，这一举动可能标志着约束 AI 建设的瓶颈正从土地或税收优惠转向电网容量。 该报道未提供任何范围细节——尚不清楚暂停只涉及新申请、待批许可还是续期，也不清楚针对的是州级许可还是市县级许可。文中没有给出官方命令、执行机构名称、审计时间表或受影响项目数量，因此仅凭现有材料无法核实其实际影响。

gdelt · wabx.net · 9月21日 22:30

**背景**: 得克萨斯州大部分地区依赖由 ERCOT 运营的独立电网，该电网在很大程度上与东部和西部互联电网隔离，因此在输电监管上与其他州不同，不受同等的联邦管辖。数据中心通常通过 ERCOT 的并网排队机制获得电网接入，而州与地方许可则管轄项目的土地使用、用水和施工等方面。近年来，得州监管机构与立法者一直在讨论如何应对数据中心和加密货币挖矿带来的负荷激增预测，包括围绕大负荷并网规则和备用发电要求的提案。

**标签**: `#Data Centers`, `#Energy Grid`, `#Regulation`, `#Texas`, `#AI Infrastructure`

---

<a id="item-4"></a>
## [不列颠哥伦比亚省就坦布勒岭枪击案起诉 OpenAI](https://theprovince.com/news/bc-lawsuit-against-openai-tumbler-ridge-mass-shooting) ⭐️ 7.0/10

加拿大不列颠哥伦比亚省已就发生在该省坦布勒岭（Tumbler Ridge）的大规模枪击事件对 OpenAI 提起诉讼。该诉讼主张 OpenAI 的技术与这起袭击存在关联，使其成为由政府发起、而非私人当事人提起的法律行动。 该诉讼把关于人工智能责任的争论从私人民事诉讼升级为省级政府发起的法律行动，可能为“当模型被指用于策划或实施暴力时，AI 开发者应承担何种责任”确立先例。如果案件继续推进，其影响可能远超加拿大，波及聊天机器人开发商在监管与风险管理方面的预期。 目前可获得的报道只给出了核心事实——原告是不列颠哥伦比亚省，被告是 OpenAI，案件与坦布勒岭大规模枪击事件有关——并未详细说明具体法律主张、索赔金额或所引用的证据。在起诉文件本身公开之前，应将这些指控的具体范围视为尚未确认。

gdelt · theprovince.com · 9月21日 22:30

**背景**: 坦布勒岭是不列颠哥伦比亚省东北部的一个小型社区，当地发生的大规模枪击惨案在加拿大引发全国关注。OpenAI 是 ChatGPT 背后的公司，而 ChatGPT 是一款被广泛使用的对话式人工智能模型。这起诉讼反映出国际上围绕“人工智能责任”日益升温的争论：开发和部署生成式 AI 系统的企业，是否应当为那些据称与其系统使用方式相关、甚至涉及暴力行为的伤害承担法律责任。

**标签**: `#OpenAI`, `#AI liability`, `#lawsuit`, `#AI safety`, `#mass shooting`

---

<a id="item-5"></a>
## [联合国小组呼吁加强对先进 AI 代理的保障措施](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9CNWdDTkRQZUpVM3duLXp2V0ZLMzVSeFdmQ00yV2R3Qk1CemNfNWM4MnFmaEIzc3Zhdk1qa05YbGdSTkVxQTU2SVlOLXBTR3VqbkZUcE9zbw?oc=5) ⭐️ 7.0/10

根据联合国新闻报道，一个联合国小组呼吁，随着 AI 代理变得越来越先进，需要加强保障措施。但现有标题和摘要未详细说明具体建议或发布呼吁的小组名称。 这标志着国际政策对 AI 代理的关注日益增加，因为 AI 代理能够自主行动，带来安全、安保和问责风险。它可能影响未来的全球 AI 治理框架，并影响企业部署代理式 AI 系统的方式。 该新闻仅提供标题和一句话摘要，缺少关于是哪个联合国小组发出呼吁、提出了哪些具体保障措施或时间表的细节。技术读者应注意，AI 代理是代表用户追求目标并完成任务的软件系统，这使得设计强有力的保障措施颇具挑战。

google\_news · UN News · 9月21日 22:18

**背景**: AI 代理是使用 AI 代表用户追求目标并完成任务的软件系统，它们超越了简单的聊天机器人，能够采取行动。AI 安全是一个跨学科领域，专注于防止 AI 系统引发事故、被滥用或产生有害后果，包括确保 AI 系统按预期行为并监控风险。随着代理获得自主性，人们对失去人类控制和意外后果的担忧日益增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://cloud.google.com/discover/what-are-ai-agents">What are AI agents? Definition, examples, and types | Google Cloud</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#AI safety`, `#AI agents`, `#regulation`, `#UN policy`

---

<a id="item-6"></a>
## [上诉法院警告「AI 垃圾内容」正威胁法院正常运作](https://news.google.com/rss/articles/CBMitwFBVV95cUxPTzFNMkcwR3VENkQ1V1VyVVFyUkdWZ2hCeXVfUTd2Z0ZqNzR6SWJ5OFFQNFoxTkhhdTVJOGY3VDlESzJERXBFdmFKMkItcF9DWmtJLV9TcHJNSXhvUi1peV85VnJ1c0JOQU9FUG5mV0loOUdtazlNNzBqbHJpWHdDUmd0LUROVUV1ZE1FdTlpdzNNR1R1c3RUb2RiMUVxWXRvX3N6ejdpOThiWEoxaTJaRURTenZ4bDg?oc=5) ⭐️ 7.0/10

据《ABA Journal》报道，一家上诉法院发出警告称，由 AI 生成的低质量内容——即被广泛称为「AI 垃圾内容」（AI slop）的东西——正在威胁法院的正常运作能力。这一警告表明，法官和书记员正日益难以应对涌入司法系统的海量 AI 生成材料。 这是生成式 AI 在现实制度层面产生的一个显著后果：法院依赖真实可信的记录运作，而如今却被「生产成本极低、审核成本极高」的自动化内容所拖累。这会影响法官、书记员、律师和诉讼当事人，也会加大制定法律文书与诉讼程序中 AI 使用规则的紧迫性。 目前仅有标题和摘要可查，因此具体是哪家法院、涉及哪起案件以及提出了哪些补救措施尚不明确。但该警告符合一个更广泛的趋势：法院已多次因律师提交含 AI 虚构引用的文书而对其作出制裁，并出台强制披露生成式 AI 使用情况的常设命令。

google\_news · ABA Journal · 9月21日 15:50

**背景**: 「AI slop」指的是用生成式 AI 制作的数字内容，通常被认为投入少、质量低、意义不大，往往以极大规模产出，用于博取流量或钻搜索引擎和广告算法的空子。在法律场景中这一点尤其重要，因为大型语言模型会出现「幻觉」，即编造出看似合理但实际不存在的判例引用、法条或引文。法院的运作建立在可核验的记录与先例之上，因此大量不可靠的 AI 生成文本会让法官和书记员不得不花时间核查并剔除无效材料，而不是专注于审理案件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://theconversation.com/what-is-ai-slop-a-technologist-explains-this-new-and-largely-unwelcome-form-of-online-content-256554">What is AI slop ? A technologist explains this new and largely...</a></li>
<li><a href="https://adlibrary.com/glossary/ai-slop">What is AI Slop ? Definition &amp; Examples | AdLibrary</a></li>

</ul>
</details>

**标签**: `#AI slop`, `#generative AI`, `#legal tech`, `#courts`, `#AI regulation`

---

<a id="item-7"></a>
## [开发者曝光 OpenAI 广告追踪链：\_\_obi Cookie 跨站关联浏览足迹](https://www.aibase.com/news/31234) ⭐️ 7.0/10

安全研究人员披露，OpenAI 的广告平台 Bazaar 使用名为 \_\_obi 的跨站 Cookie 在第三方网站上追踪用户。根据该分析，ChatGPT 会生成一个与用户账户 JWT 绑定的随机标识符，并将其写入作用域为 .openai.com 的 \_\_obi Cookie；当用户在外部网站遇到 OpenAI 广告像素时，该 Cookie 会被发送至 bzr.openai.com。 这一披露引发了重大的隐私担忧，因为它把用户的 ChatGPT 账户身份与其在无关网站上的浏览行为关联起来，实际上把广告技术式的跨站追踪引入了 AI 助手领域。在 OpenAI 正积极发展 Bazaar 广告业务的背景下，该发现可能加剧监管审查，并削弱用户对处理敏感对话的 AI 平台的信任。 据报道，\_\_obi Cookie 的作用域被设置为 .openai.com，但同时配置了 SameSite=None 和 Secure 属性，这正是浏览器能将其附加到跨站请求上的原因。据披露的流程，ChatGPT 会生成 16 个随机字节，向 sync-token 请求一个签名的 JWT，其中包含账户 ID 和一个约 22 字符的 obi 代码，有效期约 60 秒，而最终写入的 Cookie 有效期约为一年，匿名用户同样会被下发。

aibase · AIbase · 9月21日 16:01

**背景**: OpenAI 的 Bazaar 是该公司推出的 AI 驱动广告平台，包含赞助智能体（sponsored agents）以及与 HubSpot、Shopify 等营销工具的集成。JWT（JSON Web Token，RFC 7519）是一种紧凑、URL 安全的开放标准，用 JSON 对象传输带签名的声明，常用于身份验证与身份断言。跨站追踪 Cookie 是网络广告行业的经典机制——当第三方像素或脚本被嵌入页面时，在某个域上设置的 Cookie 会随请求发送到另一个域，从而使广告网络能够把同一用户在不同网站上的活动关联起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.elseif.net/stories/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector-9a9e525">OpenAI ad collector links cross - site browsing to ChatGPT... — elseif</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/17191/openai-obi-cookie-tracks-chatgpt-users-across-sites">OpenAI&#x27;s __ obi Cookie Tracks ChatGPT Users Across Sites , Analysis...</a></li>
<li><a href="https://en.wikipedia.org/wiki/JSON_Web_Token">JSON Web Token - Wikipedia</a></li>

</ul>
</details>

**标签**: `#privacy`, `#OpenAI`, `#tracking`, `#security`, `#adtech`

---

<a id="item-8"></a>
## [阿里 Qwen 团队开源 7B 参数图像模型 Qwen-Image-2.1](https://www.aibase.com/news/31227) ⭐️ 7.0/10

阿里巴巴 Qwen 团队发布了开放权重的 Qwen-Image-2.1，这是一个统一支持文生图与图像编辑的模型，视觉参数规模约为 70 亿。团队声称其在内部基准测试中超越了大多数闭源模型，但第三方评测结果尚未出炉。 其重要意义在于，来自中国头部实验室的、具备竞争力的图像生成与编辑模型以开放权重形式进入社区，且规模小到足以让个人开发者和研究者本地运行。如果性能声明在独立测试中得到验证，将缩小可自由下载的模型与 OpenAI、Google 等闭源图像系统之间的差距。 由于该模型是开放权重而非完全开源，开发者可以下载、微调并自行部署训练好的权重，但训练数据和完整的训练细节可能不会公开。其硬件门槛较低，可在 RTX 3090 等主流消费级 GPU 上运行，同时已在发布首日获得 ComfyUI 支持，并可通过第三方 API 调用。

aibase · AIbase · 9月21日 12:01

**背景**: Qwen 是阿里巴巴的大模型系列，已经从文本大语言模型扩展到视觉与多模态系统。基于扩散的图像模型是通过从随机噪声出发、逐步去噪来生成清晰图像的，而像本次这样的“统一”模型还能接收输入图像以完成编辑任务。开放权重与开源之间的区别在此很关键：开放权重发布允许任何人运行模型，但通常不公开训练数据和完整流程，因此部分标题中的“开源”说法并不准确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen-Image-2.1">Qwen/ Qwen - Image - 2 . 1 · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen-Image-2.1">GitHub - QwenLM/ Qwen - Image - 2 . 1 : Qwen&#x27;s most powerful...</a></li>
<li><a href="https://neysa.ai/blog/open-weights-open-source/">Open Weights vs Open Source: What’s the Real Difference?</a></li>

</ul>
</details>

**标签**: `#open-source`, `#image-generation`, `#diffusion-models`, `#qwen`, `#generative-ai`

---

<a id="item-9"></a>
## [Step 5 Preview：完全开源的 600B 稀疏 MoE，每次推理仅激活 27B 参数](https://www.aibase.com/news/31221) ⭐️ 7.0/10

Step5Preview 是一个完全开源的旗舰基础模型，采用稀疏 MoE（混合专家）架构，总参数量达 600B，但每次推理仅激活 27B 参数，主要面向真实场景中的智能体（agentic）任务。官方将其定位为进一步推进能力、效率与成本三者之间的帕累托前沿，但目前仅以预览版形式发布，尚未公布基准测试结果。 该模型在保持庞大总参数量的同时，每个 token 仅激活约 4.5% 的参数，目标是以前所未有的低成本提供接近前沿水平的能力，这对需要大规模运行智能体工作流的开源开发者意义重大。如果其宣称的性能能够成立，将进一步缩小开源旗舰模型与闭源前沿模型在性价比上的差距。 其 600B 总参数、27B 激活参数的配置，激活比例与其他大型稀疏 MoE 旗舰模型（如 DeepSeek-V3 的 671B 总参数 / 37B 激活参数）大致相当。不过本次仅为预览版发布，技术细节较为稀疏，既没有基准测试数据，也尚未披露路由配置、上下文长度或授权条款等信息。

aibase · AIbase · 9月21日 10:01

**背景**: 稀疏 MoE（混合专家）是一种把模型的前馈层拆分成众多“专家”、并为每个 token 只路由到其中少数几个的架构，因此参数量可以大幅扩张，而每个输入所需的计算量并不会成比例增加。所谓“激活参数”（此处为 27B），指的是每个 token 实际参与运算的网络规模，它基本决定了推理成本。智能体 AI（agentic AI）指的是能够规划、调用工具并多步半自主行动的模型，而非只回答单轮问题；帕累托前沿则描述在质量与每 token 价格等相互竞争的目标之间所能达到的最优权衡曲线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apxml.com/courses/mixture-of-experts/chapter-1-moe-foundations-sparse-models/sparse-moe-paradigm">Sparse MoE Paradigm Overview</a></li>
<li><a href="https://www.cerebras.ai/blog/moe-guide-why-moe">MoE Fundamentals: Why Sparse Models Are the Future of AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#large language models`, `#sparse MoE`, `#open-source`, `#model release`

---

<a id="item-10"></a>
## [澳大利亚呼吁全球放缓 AI 开发竞赛](https://www.maitlandmercury.com.au/story/9354719/australia-urges-slowdown-of-ai-race-in-global-statement/) ⭐️ 6.0/10

澳大利亚发布了一份全球性声明，呼吁放缓各国在人工智能开发上的竞赛步伐。该声明将激烈竞争驱动的快速 AI 开发视为各国政府应共同应对的风险，而非应加速推进的目标。 这一呼吁表明，一些政府已将 AI 竞赛的速度本身视为安全问题，而不仅仅是关注具体模型的能力。若此类呼声获得更多响应，可能影响国际规范的形成、各国 AI 战略的制定，并对前沿实验室施加政治压力，要求其说明发布节奏的合理性。 目前可获得的报道是一则简短的本地新闻，并未说明该声明的具体签署方、确切措辞，也未提及是否包含任何具有约束力的承诺。与大多数此类国际声明一样，它更适合被理解为旨在塑造规范的非约束性外交表态，而非可强制执行的监管规定。

gdelt · maitlandmercury.com.au · 9月21日 22:30

**背景**: “AI 竞赛”一词指的是各国及主要科技公司之间竞相率先构建能力更强的人工智能系统的竞争态势，其背后往往是经济与战略利益的驱动。由于这种竞争会奖励速度，政府和研究者日益警告说，安全测试、监督与风险评估可能被抛在后面。国际声明与联合宣言是新兴技术领域设定共同预期的常见外交工具，但它们通常依赖自愿遵守与政治善意，而非法律强制力。澳大利亚作为一个对 AI 治理有积极关注的中等规模经济体，会借助此类声明与其他立场相近的政府一道表明自身立场。

**标签**: `#AI regulation`, `#AI policy`, `#Australia`, `#AI safety`, `#global governance`

---