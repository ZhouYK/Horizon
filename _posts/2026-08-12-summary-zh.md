---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
report: default
---

> 从 357 条内容中筛选出 8 条重要资讯。

---

1. [xAI 发布 Grok 4.6，聚焦长时间运行的智能体任务](#item-1) ⭐️ 9.0/10
2. [Qwen 开源 Qwen3.8-2.4T-A95B，总参数 2.4T 的 MoE 模型](#item-2) ⭐️ 9.0/10
3. [LTX 发布开源视频模型 LTX-2.5，单张 RTX 5090 即可本地运行](#item-3) ⭐️ 8.0/10
4. [腾讯 Q2 营收超预期，AI 资本开支使自由现金流转负](#item-4) ⭐️ 7.0/10
5. [微信发布 WeLM，以资源效率为核心的大语言模型家族](#item-5) ⭐️ 7.0/10
6. [马斯克：未来所有特斯拉将搭载星链，Cybercab 率先集成](#item-6) ⭐️ 6.0/10
7. [Codex 活跃用户突破 1000 万，团队预告明日惊喜](#item-7) ⭐️ 6.0/10
8. [企业级 SSD 占 NAND 出货量 48%，长江存储首进全球前三](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [xAI 发布 Grok 4.6，聚焦长时间运行的智能体任务](https://x.ai/news/grok-4-6) ⭐️ 9.0/10

2026 年 8 月 12 日，xAI 发布 Grok 4.6，作为 Grok 4.5 的增量升级，强化了长时间运行的智能体交互和视觉任务，并在 Artificial Analysis 智能指数上与 GPT-5.6 Sol 持平。该模型即日起上线 Cursor、Grok Build 和 API，定价为每百万输入 token 2 美元、每百万输出 token 6 美元，另有双倍价格的快速版。 此次发布表明 xAI 在独立智能体基准上与 OpenAI 正面竞争，同时通过 Cursor 和 API 让生产级模型广泛可用。聚焦长时间运行的智能体任务，回应了行业的关键瓶颈——这类工作负载需要比简单单次调用更稳健的基础设施。 Grok 4.6 提供双倍价格的快速版，并且 xAI 在首周为 Grok Build 和 Cursor 用户赠送双倍用量。Artificial Analysis 智能指数综合了九项基准，并衡量每项任务所需的输出 token 数，以反映实际智能体性能。

telegram · zaihuapd · 8月12日 15:54

**背景**: Grok 是 xAI（SpaceXAI）开发的系列大语言模型，于 2023 年 11 月首次推出，并已集成到 X 社交网络和特斯拉 Optimus 机器人中。Grok Build 是 xAI 的 vibe coding 工具，可将自然语言提示转化为原型，并将大型任务委派给并行运行的专业子代理。长时间运行的智能体任务是指可运行 30 分钟至数小时甚至数天的自主多步骤工作流，需要任务队列、持久化执行和人在回路等基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_Build">Grok Build</a></li>
<li><a href="https://www.openlegion.ai/en/learn/ai-agent-long-running-tasks">AI Agent Long Running Tasks : Queues, Checkpoints... | OpenLegion</a></li>

</ul>
</details>

**标签**: `#AI`, `#Grok`, `#xAI`, `#language models`, `#agentic AI`

---

<a id="item-2"></a>
## [Qwen 开源 Qwen3.8-2.4T-A95B，总参数 2.4T 的 MoE 模型](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 在 Hugging Face 上开源了 MoE 模型 Qwen3.8-2.4T-A95B，总参数量 2.4 万亿、激活参数 95 亿。该模型原生支持 262,144 tokens 的上下文长度，可扩展至 1,010,000 tokens。 此次发布将有史以来最大的开源模型之一带给社区，推动可自由用于研究和商业使用的模型前沿。MoE 架构在如此大的规模下仍能保持可接受的推理成本，因此更多团队可以试验和部署一个 2.4T 参数的模型。 该模型采用混合专家（MoE）设计，每个 token 仅激活 2.4T 参数中的 95B，大幅降低了计算开销。Hugging Face 上的公告内容简短，未提供训练数据细节或基准测试结果，尚需进一步评估。

telegram · zaihuapd · 8月12日 16:13

**背景**: 混合专家（MoE）是一种将模型的前馈网络拆分为多个“专家”子模型的技术；路由器会为每个 token 选择使用哪些专家，因此任何时候只有总参数中的一部分处于激活状态。这使得 MoE 模型的总参数可以远超稠密模型，而推理时的运行成本大致相同。总参数量反映模型的完整规模，激活参数量则反映每次推理步骤实际使用的参数数量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts ( MoE )</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters : What’s the Difference ?</a></li>
<li><a href="https://www.linkedin.com/pulse/mixture-experts-moe-ai-breakthrough-making-large-language-banafa-xk01c">Mixture of Experts ( MoE ): The AI Breakthrough Making Large ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对此次发布表现出兴奋，有评论者提到当晚还发布了多个重要模型，包括微信的 WeLM、Qwen 3.8 Max 开源权重、DeepSeek v4 Pro 正式版和 Grok 4.6。总体情绪是期待和热烈，但片段中未出现批判性分析或担忧。

**标签**: `#Qwen`, `#LLM`, `#open-source`, `#MoE`, `#AI`

---

<a id="item-3"></a>
## [LTX 发布开源视频模型 LTX-2.5，单张 RTX 5090 即可本地运行](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX 发布了开源视频生成基础模型 LTX-2.5，权重、训练代码和推理管线全部开放，可在单张 RTX 5090 上本地运行。该模型支持文生视频和图生视频，在 98 个提示词的瑕疵评测中，LTX-2.5 Pro 在十款模型中排名第一。 这一发布意义重大，因为降低了高质量 AI 视频生成的门槛，个人和小公司无需云服务成本就能在消费级硬件上本地运行一个具竞争力的模型。对年收入低于 1000 万美元的公司提供免费商用许可，可能加速开源视频生成生态的采用和创新。 LTX-2.5 引入了一种新的扩散视频解码器，并使用 Gemma 4 12B 文本编码器，改进多镜头连贯性和提示词遵循。该模型可一次生成多镜头场景并导出电影级 EXR，但仅对年收入低于 1000 万美元的公司免费商用。

telegram · zaihuapd · 8月12日 02:15

**背景**: 视频生成模型能够根据文本或图像提示生成动态画面，但大多数最先进的系统都是闭源的，且需要强大的云端 GPU。LTX-2.5 属于开源权重视频模型中日益增长的一类，能够在消费级硬件上运行，类似 Stable Diffusion 推动图像生成普及的过程。发布中提到的扩散解码器本身是一个小型扩散模型，在潜在表征的条件下对像素进行去噪，而非传统的卷积解码器。来自 Google Gemma 家族的 Gemma 4 12B 文本编码器是一种多模态模型，帮助系统理解和遵循文本提示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-5">LTX - 2 . 5 : LTX&#x27;s Latest AI Open-Source Foundation Model | LTX</a></li>
<li><a href="https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/ltx2/pipeline_ltx2_diffusion_decode.py">diffusers/src/diffusers/pipelines/ltx2/pipeline_ltx2_ diffusion _ decode .py...</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/">Introducing Gemma 4 12B</a></li>

</ul>
</details>

**标签**: `#AI`, `#video-generation`, `#open-source`, `#deep-learning`, `#generative-models`

---

<a id="item-4"></a>
## [腾讯 Q2 营收超预期，AI 资本开支使自由现金流转负](https://wallstreetcn.com/articles/3779275) ⭐️ 7.0/10

腾讯公布 2026 年第二季度营收 2048 亿元，同比增长 11%，略超彭博预期。资本支出同比近翻三倍至 528 亿元，导致自由现金流为-138 亿元。 该业绩凸显了 AI 相关资本开支对大型科技公司的巨大压力：腾讯尽管营收超预期，自由现金流仍转负。这反映了整个行业 AI 基础设施投资正吞噬现金流的趋势，可能促使投资者重新评估腾讯短期盈利能力和资本配置。 净利润仅增长 0.7%至 560 亿元，低于市场预期。公司称剔除 AI 算力预付款后自由现金流为 376 亿元；分业务看，营销服务收入增长 22%，本土游戏增长 17%，国际游戏受汇率影响下降 0.8%。

telegram · zaihuapd · 8月12日 10:30

**背景**: 腾讯是中国最大的互联网公司之一，营收覆盖游戏、营销服务、金融科技和云服务。自由现金流是科技投资者密切关注的指标，衡量企业在资本开支后产生的现金。腾讯正大力投资 AI 基础设施，包括为算力预付资金，这暂时拖累自由现金流。WorkBuddy 是腾讯云推出的 AI 办公助手，属于能自主规划并交付多模态复杂任务的 AI 智能体；它在中国桌面端 AI 办公智能体中月访问量排名第一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.codebuddy.cn/work/">WorkBuddy - AI Agent 办公新范式</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#earnings`, `#AI capex`, `#finance`, `#technology`

---

<a id="item-5"></a>
## [微信发布 WeLM，以资源效率为核心的大语言模型家族](https://x.com/Weixin_WeChat/status/2087509298310209718) ⭐️ 7.0/10

微信团队发布了以资源效率为核心的通用大语言模型家族 WeLM。其中 WeLM-80B（3B 激活参数）已应用于微信 AI 智能体，而基于 MoE 架构的 WeLM-617B（23B 激活参数）正在研发中。 此次发布展示了在消费级平台上高效运行大语言模型的可行路径，在降低推理成本的同时保有模型能力。这对微信海量用户意义重大，也反映出行业向资源感知型 LLM 部署迈进的趋势。 WeLM-80B 每次推理仅激活 800 亿参数中的 3B；研发中的 WeLM-617B 采用混合专家（MoE）架构，激活 23B 参数。已部署的模型支持对话搜索、微信原生功能操作以及小程序服务调用。

telegram · zaihuapd · 8月12日 13:58

**背景**: 传统大语言模型对每个 token 都会激活全部参数，随着模型规模增大推理成本会非常高。混合专家（MoE）架构通过将模型划分为多个专门化的专家、每个 token 只激活其中一部分，从而大幅降低计算成本并保持模型容量。因此，激活参数数量往往比总参数量更能反映实际部署成本。微信作为拥有数亿用户的超级应用，需要在规模化场景中部署高效 AI 模型以提供智能助手等功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.weex.com/news/detail/wechat-launches-welm-large-model-series-to-drive-ai-application-implementation-c0pmz8w994lglikkdnsi3ndr">WeChat Launches WeLM Large Model Series to... | WEEX Crypto News</a></li>
<li><a href="https://www.gate.com/news/detail/wechat-releases-welm-large-language-model-series-with-welm-80b-active-in-ai-23402318">WeChat Releases WeLM Large Language Model Series... | Gate News</a></li>
<li><a href="https://chizkidd.github.io/2026/08/10/MoE-2/">Mixture of Experts ( MoE ): How Transformers Scale Without Activating...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#WeLM`, `#MoE`, `#WeChat`, `#AI`

---

<a id="item-6"></a>
## [马斯克：未来所有特斯拉将搭载星链，Cybercab 率先集成](https://www.techspot.com/news/113429-elon-musk-every-tesla-have-starlink-starting.html) ⭐️ 6.0/10

马斯克在财报电话会上宣布，所有未来特斯拉车型都将集成星链卫星连接（至少在星链覆盖的市场）。特斯拉 Robotaxi 官方账号还展示了首台车顶集成星链 V5 天线的 Cybercab 原型车。 这将把特斯拉车辆直接接入 SpaceX 的卫星网络，让每辆特斯拉都能获得用于自动驾驶、视频流和车队运营的持续连接。一旦大规模部署，可能给其他车企和电信运营商在车载连接与偏远地区覆盖方面带来压力。 集成的天线为星链 V5，下行速率可超过 375 Mbps，安装在 Cybercab 的车顶后部。Cybercab 是一款专用自动驾驶车辆，没有方向盘和踏板；马斯克称乘客途中可观看 4K 视频，但尚未公布量产时间。

telegram · zaihuapd · 8月12日 03:53

**背景**: 星链是 SpaceX 的近地轨道卫星互联网星座，旨在为服务不足和偏远地区提供高速连接。Cybercab 是特斯拉专门打造的无人驾驶出租车，于 2024 年发布，计划无需驾驶员即可运营；这次发布表明特斯拉希望通过星链让这类车辆在任何地方都保持联网。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hypebeast.com/2026/8/tesla-cybercab-debuts-with-integrated-starlink-v5">Tesla Cybercab With Starlink V 5 Antenna Revealed | Hypebeast</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#Starlink`, `#Satellite Internet`, `#EV`, `#Autonomous Vehicles`

---

<a id="item-7"></a>
## [Codex 活跃用户突破 1000 万，团队预告明日惊喜](https://x.com/thsottiaux/status/2087423996115681767) ⭐️ 6.0/10

据 Tibo 在 X 平台发文，OpenAI 的编程智能体 Codex 活跃用户已突破 1000 万。Tibo 同时预告，明天将公布一个惊喜。 突破 1000 万活跃用户，使 Codex 成为最广泛采用的 AI 编程工具之一，显示出 AI 辅助软件开发正在进入主流。此前的预告暗示 OpenAI 可能很快推出新功能或新公告，从而影响 AI 编程领域的竞争格局。 Tibo 提到，团队此前承诺在 Codex 每增加 100 万活跃用户时就进行一次重置或标记，直至达到 1000 万。如今用户量已大幅超过这一数字，因此在惊喜公布前团队一直保持沉默。

telegram · zaihuapd · 8月12日 08:01

**背景**: OpenAI Codex 是 OpenAI 开发的一套由 AI 驱动的编程智能体，用于自动化软件工程任务，让开发者可以把功能开发和修复 Bug 等工作交给它。Codex 已发展为一款可通过命令行界面和云端环境工作的编程智能体，并集成到现代开发工作流中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>

</ul>
</details>

**标签**: `#Codex`, `#OpenAI`, `#AI coding`, `#milestone`, `#announcement`

---

<a id="item-8"></a>
## [企业级 SSD 占 NAND 出货量 48%，长江存储首进全球前三](https://china.counterpointresearch.com/%e6%9c%8d%e5%8a%a1%e5%99%a8%e9%9c%80%e6%b1%82%e6%8e%a8%e5%8d%87%e4%bc%81%e4%b8%9a%e7%ba%a7-ssd-%e5%8d%a0-nand-%e5%87%ba%e8%b4%a7%e9%87%8f%e7%99%be%e5%88%86%e4%b9%8b-48/) ⭐️ 6.0/10

根据 Counterpoint Research 的报告，2026 年第二季度企业级 SSD 占全球 NAND 出货量的 48%，同比接近翻倍，行业营收同比增长五倍。长江存储首次以 14%的份额超越铠侠，跻身全球 NAND 供应商前三。 这一激增凸显了 AI 推理工作负载正在重塑存储市场，使企业级 SSD 成为 NAND 位元的主要消耗者。长江存储的崛起也标志着存储竞争格局的转变，但其偏消费级的产品结构限制了其营收排名。 三星以 25%的份额领跑，SK 海力士以 22%位居第二，长江存储以 14%位列第三。尽管出货量份额排名第三，但长江存储因产品偏消费级，营收仅排第五；Counterpoint 预计到年底企业级 SSD 将消耗超过一半的 NAND 位元总量。

telegram · zaihuapd · 8月12日 11:00

**背景**: NAND 闪存是一种非易失性存储技术，广泛用于 SSD、存储卡和智能手机，通过在浮栅晶体管中存储电荷来保存数据。企业级 SSD 是为数据中心和服务器设计的高性能、大容量硬盘，通常采用 NVMe/PCIe 接口。AI 推理工作负载——即运行已训练模型进行预测的过程——需要海量快速存储，从而推动了对企业级 SSD 的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NAND_flash_memory">NAND flash memory</a></li>
<li><a href="https://grokipedia.com/page/Samsung_Enterprise_NVMe_SSD">Samsung Enterprise NVMe SSD</a></li>
<li><a href="https://www.linkedin.com/pulse/what-ai-inference-workloads-why-growing-rapidly-naddodnetworking-m5lbc">What are AI Inference Workloads ? Why AI Inference Workloads Are...</a></li>

</ul>
</details>

**标签**: `#NAND`, `#SSD`, `#Enterprise Storage`, `#AI`, `#Market Share`

---