---
layout: default
title: "Horizon Summary: 2026-08-27 (ZH)"
date: 2026-08-27 04:33:18 +0000
lang: zh
report: default
---

> 从 333 条内容中筛选出 8 条重要资讯。

---

1. [我国首次实现地月双向高速激光通信，下行速率 100 Mbps](#item-1) ⭐️ 9.0/10
2. [阿里发布 Qwen3.8-Flash MoE 模型，称性能比肩 Opus 4.6](#item-2) ⭐️ 8.0/10
3. [Z.ai 发布 GLM-5.3-Flash：320B MoE，价格降至十分之一](#item-3) ⭐️ 8.0/10
4. [谷歌推出 Gemini 3.5 Transcribe，支持 85+语言并去除语气词](#item-4) ⭐️ 8.0/10
5. [英伟达洽谈收购 Hugging Face，估值超 130 亿美元](#item-5) ⭐️ 8.0/10
6. [高通力推 AI 原生 6G 与 Token 即服务，剑指 150 亿美元数据中心营收](#item-6) ⭐️ 7.0/10
7. [Claude 桌面端新增内置浏览器，自动操作网页](#item-7) ⭐️ 7.0/10
8. [Telegram 推出欢迎消息、消息按钮与礼物签名](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [我国首次实现地月双向高速激光通信，下行速率 100 Mbps](https://www.stdaily.com/web/gdxw/2026-08/26/content_570163.html) ⭐️ 9.0/10

我国在超过 40 万公里的地月距离上，利用 DRO-A 卫星首次实现了双向高速激光通信。试验初步实现了上行 1.25 Mbps、下行 100 Mbps 的速率，由中国科学院空间应用工程与技术中心牵头完成。 这一里程碑标志着我国空间激光通信从近地轨道迈入地月空间，为深空任务提供快得多的数据回传能力。它有望成为未来月球探测、月球基地以及星际间高清图像与视频传输的关键技术。 下行速率达到 100 Mbps，约为传统 5 Mbps 微波链路的 20 倍：传输一张 8K 月面高清图像只需约 12 秒，而传统方式需 4 到 5 分钟。试验依托 DRO-A 卫星实施，该卫星属于中国的远距离逆行轨道（DRO）试验任务。

telegram · zaihuapd · 8月27日 00:33

**背景**: 空间激光通信利用聚焦光束而非无线电波传输数据，带宽远高于传统微波，但对发射端和接收端的精确对准要求极高。地月平均距离约 38.4 万公里，给光束指向与捕获带来巨大挑战。此前 NASA 的 LCRD 等演示均在近地轨道开展，而在地月距离上实现双向、Mbps 级速率的激光链路是一个重要跨越。DRO-A/B 卫星在发射时曾被报道因上面级故障未能进入预定轨道，因此本次试验也体现了在复杂环境下的在轨恢复与运行能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.globaltimes.cn/page/202608/1369111.shtml">China achieves 1st two-way laser communication ... - Global Times</a></li>
<li><a href="https://www.nperakis.com/post/dro-resonant-orbits">China&#x27;s DRO constellation &amp; resonant orbits</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laser_communication_in_space">Laser communication in space - Wikipedia</a></li>

</ul>
</details>

**标签**: `#space communication`, `#laser communication`, `#deep space`, `#China`, `#DRO-A`

---

<a id="item-2"></a>
## [阿里发布 Qwen3.8-Flash MoE 模型，称性能比肩 Opus 4.6](https://x.com/Alibaba_Qwen/status/2092591393424515114) ⭐️ 8.0/10

阿里通义团队发布了 Qwen3.8-Flash，这是一款 125B 参数的混合专家（MoE）模型，每 token 仅激活 6B 参数，同时开源了作为 Qwen4 架构预览的 Qwen3.8-Flash-Next。阿里称其性能比肩 Anthropic Opus 4.6 和 DeepSeek V4-Flash，定价为每百万输入 tokens 0.16 美元、每百万输出 tokens 0.47 美元。 这一发布意义重大，因为它以极低的成本和激活参数带来了号称前沿水平的性能，可能让高端 AI 能力更加普及。这也加剧了开源权重模型厂商之间的竞争，并可能在性价比上对闭源模型形成压力。 该模型原生上下文窗口为 262K tokens，可扩展至 1M。阿里表示其训练成本约为 Qwen3.7-Plus 的九分之一，编码和办公任务表现更优，不过这些基准测试说法尚未得到独立验证。

telegram · zaihuapd · 8月26日 13:36

**背景**: 混合专家（MoE）模型会将任务分配给专门化的专家子网络，每个 token 只激活其中一小部分参数。这使得像 Qwen3.8-Flash 这样的模型总参数量可达 125B，但只有 6B 参数处于激活状态，从而与同能力的稠密模型相比大幅降低推理计算量和成本。这一技术细节很重要：总参数量影响模型的知识量和内存占用，而激活参数量决定推理速度和计算成本，这正是阿里声称以极低价格实现 Opus 级别性能的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between Total and Active Parameters | by Burak Kılıç | Medium</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#MoE`, `#LLM`, `#AI`, `#open-source`

---

<a id="item-3"></a>
## [Z.ai 发布 GLM-5.3-Flash：320B MoE，价格降至十分之一](http://z.ai/) ⭐️ 8.0/10

Z.ai 发布了 GLM-5 系列首款原生多模态模型 GLM-5.3-Flash，总参数 320B，激活参数仅 18B。限时优惠期间，API 输入价格降至每百万 Tokens 0.075 美元，约为上代十分之一；官方称其在编程和智能体基准上超越 GLM-5.2，并接近 Claude Opus 4.8。 此次发布意义重大：它把大型 MoE 模型与激进降价结合，使前沿性能对开发者更可负担。结合国产 AI 芯片与稀疏+线性注意力混合设计，也体现出行业在推进比主流英伟达 GPU 更便宜、更高效的推理方案。 原价分别为每百万输入 Tokens 0.15 美元、缓存输入 0.03 美元、输出 0.50 美元；限时优惠价分别为 0.075 美元、0.015 美元和 0.25 美元，缓存存储暂时免费。模型混合使用稀疏与线性注意力，据称在国产芯片上端到端推理性能提升 3 倍，并在匿名测试期间成为当周最受欢迎模型。

telegram · zaihuapd · 8月26日 14:23

**背景**: 混合专家（MoE）架构对每个 token 只激活部分参数，因此 320B 总参数、18B 激活参数的模型，其服务成本更接近 18B 稠密模型，同时保留完整网络的很大容量。稀疏注意力通过只关注有限位置，降低标准注意力的二次方复杂度；线性注意力则以更低复杂度压缩全局上下文，二者结合旨在提升长序列处理效率。这解释了为何 GLM-5.3-Flash 的“总参数 vs 激活参数”和混合注意力设计是其性能与定价主张的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://latenteast.com/insights/moe-total-vs-active-parameters">MoE Total vs Active Parameters , Explained | The Latent East</a></li>
<li><a href="https://www.linkedin.com/pulse/llm-architecture-sparse-vs-linear-attention-haris-lubis-zjaoc">LLM Architecture -&gt; Sparse vs . Linear Attention</a></li>

</ul>
</details>

**标签**: `#GLM`, `#AI`, `#LLM`, `#model release`, `#pricing`

---

<a id="item-4"></a>
## [谷歌推出 Gemini 3.5 Transcribe，支持 85+语言并去除语气词](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 8.0/10

谷歌发布了新的语音转文字模型 Gemini 3.5 Transcribe，可将原始音频转换为润色后的格式化文本。它支持超过 85 种语言，可去除“嗯”“呃”等语气词，并将接入 Chrome、Search Live、Gemini Live、Docs、Keep 和 Gmail，同时提供 API。 此次发布可能显著改善语音识别工作流程，提供更干净、更准确的转录文本，便于后续使用。它还将人工智能驱动的转录直接融入谷歌生态系统，影响使用该 API 的开发者以及在谷歌服务中使用该功能的普通用户。 该模型可以学习自定义词汇，识别订单号等字母数字串，并能对预录音频中最多 3 名说话者生成词级时间戳。它已为 Gboard 的 Rambler 功能提供支持，并将进入 Chrome 网页输入框及其他谷歌产品。

telegram · zaihuapd · 8月27日 01:02

**背景**: 传统的语音识别模型通常难以应对背景噪音、复杂行话以及“嗯”“呃”等语气词，这会影响转录质量。Gemini 3.5 Transcribe 专为直接将原始音频转换为准确、润色后的格式化文本而设计，解决了这些常见痛点。它属于谷歌 Gemini Audio 模型系列，反映了将先进语音转文字能力整合到消费级和企业级产品中的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Intelligent transcription with Gemini 3.5 Transcribe</a></li>
<li><a href="https://9to5google.com/2026/08/26/gemini-3-5-transcribe/">Google launches Gemini 3.5 Transcribe, which powers Gboard Rambler &amp; is coming to Chrome</a></li>
<li><a href="https://arstechnica.com/ai/2026/08/google-announces-gemini-3-5-transcribe-for-ai-powered-speech-to-text/">Google announces Gemini 3.5 Transcribe for AI-powered speech-to-text - Ars Technica</a></li>

</ul>
</details>

**标签**: `#speech recognition`, `#Gemini`, `#Google`, `#AI models`, `#transcription`

---

<a id="item-5"></a>
## [英伟达洽谈收购 Hugging Face，估值超 130 亿美元](https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8) ⭐️ 8.0/10

据知情人士透露，英伟达正在洽谈以超过 130 亿美元的估值收购 Hugging Face。双方尚未达成协议，谈判仍可能破裂。 这一交易若达成，将使英伟达掌控最知名的开源 AI 平台，可能重塑 AI 生态系统。它也可能加剧关于开源中立性以及大型科技公司对 AI 开发影响力的争论。 英伟达已是 Hugging Face 的股东，曾参与其 2023 年 2.35 亿美元融资，当时估值为 45 亿美元。Hugging Face 此前拒绝了英伟达 5 亿美元的投资要约，微软也曾进行过谈判，但目前已停止。

telegram · zaihuapd · 8月27日 02:03

**背景**: Hugging Face 是一家美国公司，提供分享机器学习模型、数据集和 AI 应用的开放平台。开源 AI 平台被视为重要基础设施，因为它们让开发者能够使用并基于社区贡献的模型进行开发。英伟达是 AI 训练芯片的主导厂商，因此收购 Hugging Face 可能将其影响力从硬件扩展到 AI 的软件和社区层面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://www.analyticsinsight.net/artificial-intelligence/hugging-face-how-its-open-ai-platform-became-a-target-for-big-tech">Hugging Face: How its Open AI Platform Became a Target for ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Hugging Face`, `#Acquisition`, `#AI`, `#Open Source`

---

<a id="item-6"></a>
## [高通力推 AI 原生 6G 与 Token 即服务，剑指 150 亿美元数据中心营收](https://finance.sina.com.cn/jjxw/2026-08-26/doc-inipsezr5961972.shtml) ⭐️ 7.0/10

高通在圣地亚哥 6G 媒体日上表示，6G 的真正分水岭是 AI 写入网络底层逻辑，将催生豆包 AI 手机等智能体 AI 设备。高通还发布了 Dragonfly 产品线和 HBC 高带宽计算架构，目标 2029 财年数据中心营收超 150 亿美元，并收购了 AI 基础设施公司 Modular。 这标志着电信行业战略转向：运营商未来可能从卖流量转向卖算力和 Token，重塑移动商业模式。高通大举扩张数据中心业务，可能挑战英伟达等现有巨头，因为 AI 正从云端走向边缘和设备端。 HBC 架构通过硅通孔将加速器直接堆叠在 LPDDR DRAM 下方，宣称无需昂贵的 HBM 和硅中介层即可实现高达 6 倍的 HBM 效率。6G 标准预计 2028 年确定；此次收购的 Modular 旗下 BentoML 框架已被超 1 万家机构（含 50 多家财富 500 强企业）用于 AI 模型部署。

telegram · zaihuapd · 8月27日 02:31

**背景**: Token 即服务（TaaS）是一种新兴计费模式，企业按使用量以 Token 计价方式消费 AI 算力，而非为固定基础设施付费。HBC（高带宽计算）是高通提出的近内存 AI 架构，利用硅通孔将计算单元堆叠在 DRAM 之下，旨在突破内存墙瓶颈。高通传统上是移动芯片厂商，如今正向数据中心 AI 基础设施转型；6G 预计将成为首个围绕 AI 而非单纯网速设计的移动通信代际。Modular 是一家 AI 基础设施初创公司，以其 MAX 平台和 BentoML 模型服务框架而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-stack.ai/en/whats-taas">What is Token-as-a-Service (TaaS)? A New Model for Resource ...</a></li>
<li><a href="https://wccftech.com/qualcomm-hbc-stacks-compute-beneath-dram-to-smash-the-ai-memory-wall/">Qualcomm &#x27;s HBC Stacks Compute Beneath DRAM To Smash The AI...</a></li>
<li><a href="https://ailectures.site/modular-bentoml-joins-modular/">Modular : BentoML Joins Modular - AI Lectures</a></li>

</ul>
</details>

**标签**: `#6G`, `#AI`, `#Qualcomm`, `#Token-as-a-Service`, `#Data Center`

---

<a id="item-7"></a>
## [Claude 桌面端新增内置浏览器，自动操作网页](https://claude.com/blog/cowork-built-in-browser) ⭐️ 7.0/10

Anthropic 的 Claude Cowork 桌面应用现已内置浏览器，当任务涉及网站时会在侧边栏自动打开，Claude 可导航网页、阅读、点击和输入，无需安装扩展。该功能本周起向 Pro、Max 和 Team 计划推送并默认开启，Enterprise 管理员今天起可启用。 此次更新将 Claude 的智能体能力扩展到实时网页交互，无需自定义连接器或扩展即可实现表单填写和门户操作。它让 Cowork 成为知识工作者更完整的桌面智能体，同时隔离的浏览器可保护用户的个人标签页、书签和密码隐私。 内置浏览器与用户的常规浏览器相互隔离，无法看到标签页、书签和密码。它支持无连接器操作，即使用户的门户没有专用连接器，Claude 也能与之交互；此次推送覆盖 Pro、Max 和 Team 计划，Enterprise 管理员今天起可启用该功能。

telegram · zaihuapd · 8月27日 03:06

**背景**: Claude Cowork 是 Anthropic 推出的桌面应用，让用户把多步骤任务交给 Claude 完成，目前在桌面端运行，Web 和移动端处于测试阶段。它可以处理用户选定的文件和工具，而基于 Model Context Protocol（MCP）的 Claude 连接器让模型能够使用外部数据库和应用。内置浏览器让 Claude 在操作网页时无需安装扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Cowork">Claude Cowork</a></li>
<li><a href="https://claude.com/product/cowork">Claude Cowork | Claude by Anthropic</a></li>

</ul>
</details>

**标签**: `#Claude`, `#AI agents`, `#browser automation`, `#Anthropic`, `#desktop app`

---

<a id="item-8"></a>
## [Telegram 推出欢迎消息、消息按钮与礼物签名](https://telegram.org/blog/welcome-messages-buttons-TG-13) ⭐️ 6.0/10

Telegram 发布了新更新，为群组和频道新增仅新成员可见的欢迎消息，并同步推出消息按钮、富文本编辑和礼物签名功能。开发者可以在单条消息中加入多个按钮，用于问卷、游戏和商品浏览等互动。 这次更新为社群管理员提供了更强大的入群欢迎和互动工具，也让开发者能在 Telegram 内构建更具交互性的体验。这也延续了 Telegram 通过快速迭代功能来与其他消息平台竞争的惯例。 欢迎消息可包含多条消息、媒体和富文本，且仅对新成员显示。富文本编辑器现在支持插入文档、文件和音乐，礼物市场也允许购买者为礼物添加签名和评论。

telegram · zaihuapd · 8月27日 00:05

**背景**: Telegram 是一款基于云的消息应用，支持群组、频道和带公开 Bot API 的机器人。该服务经常通过更新为用户和开发者增加新功能，本次发布延续了这一传统。欢迎消息可以帮助社群管理员自动问候新成员。

**标签**: `#Telegram`, `#product update`, `#messaging`, `#features`

---