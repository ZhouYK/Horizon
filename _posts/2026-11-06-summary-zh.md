---
layout: default
title: "Horizon Summary: 2026-11-06 (ZH)"
date: 2026-11-06 23:04:08 +0000
lang: zh
report: default
---

> 从 199 条内容中筛选出 13 条重要资讯。

---

1. [百度开源文心 5.5 Flash Base：2800 亿参数 MoE 基座模型](#item-1) ⭐️ 8.0/10
2. [月之暗面拟在欧洲租用逾 8000 颗英伟达 Blackwell GPU](#item-2) ⭐️ 7.0/10
3. [长江存储第四座武汉工厂国产设备占比拟达 70%](#item-3) ⭐️ 7.0/10
4. [淘宝 MNN 团队开源 0.3B 端侧语言模型](#item-4) ⭐️ 7.0/10
5. [Anthropic 通过 Plaid 让 Claude 读取银行与信用卡账户](#item-5) ⭐️ 6.0/10
6. [印度计划 24 个月内推出自研 GPU 芯片](#item-6) ⭐️ 6.0/10
7. [广电总局重申扶持真人微短剧，收紧对 AI 剧的规范](#item-7) ⭐️ 6.0/10
8. [六部门发文：加快具身智能等前沿技术进入养老领域](#item-8) ⭐️ 6.0/10
9. [特斯拉将于明年年中逐步停产 Cybertruck，为 Cybercab 腾出产能](#item-9) ⭐️ 6.0/10
10. [欧盟指控 TikTok 推荐算法造成有害“兔子洞”效应](#item-10) ⭐️ 6.0/10
11. [研究者发现苹果 iPhone 键盘隐藏约 10 万条禁推荐词](#item-11) ⭐️ 6.0/10
12. [Telegram 13.2 支持在聊天内直接运行 HTML 互动消息](#item-12) ⭐️ 6.0/10
13. [美国司法部「超级智能特别工作组」正式启动运作](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [百度开源文心 5.5 Flash Base：2800 亿参数 MoE 基座模型](https://www.news.cn/info/20261105/f3bbdb6854f5441ca9fb34062f213875/c.html) ⭐️ 8.0/10

百度正式开源了最新基座模型文心 5.5 Flash Base，采用 MoE 架构，总参数量 2800 亿，每个 Token 激活 140 亿参数，预训练使用了 33.5 万亿 Token。该模型预训练上下文最长为 128K，而在微调与推理阶段可支持最长 100 万 Token 的上下文。 2800 亿总参数、140 亿激活参数的组合，让开发者能以相对低廉的推理成本获得接近大模型质量的基座模型；而开放权重意味着社区可以自行微调和私有化部署这家中国头部厂商的前沿模型，而不必只通过 API 调用。100 万 Token 的推理上下文也让百度加入了超长上下文竞赛，这类能力正日益被视为检索增强生成（RAG）流程的替代或补充方案。 百度表示围绕“效率”主线，在注意力机制、专家路由及训练目标等环节做了系统性优化，以提升资源利用效率。不过该发布说明并未给出基准测试成绩、模型许可条款，也没有披露专家数量或路由算法的细节，因此其质量与部署成本仍有待独立评测验证。

telegram · zaihuapd · 11月6日 05:41

**背景**: 混合专家（MoE）模型把前馈层拆分成许多独立的“专家”子网络，每个 Token 只被路由到其中一小部分，因此模型的总参数量可以远超稠密模型，而每个 Token 的计算量却小得多——这就是“总参数”与“激活参数”的区别。专家路由是决定每个 Token 访问哪些专家的“门控”机制，其设计直接影响吞吐量、负载均衡和训练稳定性。上下文窗口指模型一次能处理的文本量（以 Token 计），近几代模型已从数千扩展到数十万乃至更长，从而减少了对分块、滑动窗口和检索等变通手段的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://www.emergentmind.com/topics/moe-expert-routing-analysis">MoE Expert Routing Analysis</a></li>
<li><a href="https://www.ibm.com/think/topics/context-window">What is a context window ? | IBM</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoE`, `#open-source`, `#Baidu ERNIE`, `#long context`

---

<a id="item-2"></a>
## [月之暗面拟在欧洲租用逾 8000 颗英伟达 Blackwell GPU](https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html) ⭐️ 7.0/10

据 CNBC 报道，月之暗面（Moonshot AI）正与欧洲新兴云厂商（neocloud）洽谈租用超过 8000 颗英伟达 Blackwell GPU，主要用于推理，也涉及部分训练。据称该交易要求月之暗面比非中国买家多支付 30% 至 50% 的预付款。 这表明中国 AI 实验室正通过海外云算力绕过美国出口管制，因为管制禁止 Blackwell 直接销往中国，这可能使“算力出海”成为一种常态化规避路径。若被效仿，将加大美国出口管制的执行难度，并推高中国模型公司的算力成本。 这些 GPU 将通过远程云服务使用，而非进口到中国，30% 至 50% 的溢价是预付款要求，而非标准租金水平。该报道基于匿名知情人士，未披露具体欧洲供应商；白宫今年 7 月曾称月之暗面通过泰国设施获取过 Blackwell 芯片。

telegram · zaihuapd · 11月6日 05:02

**背景**: Blackwell 是英伟达继 Hopper 之后的 GPU 架构，面向生成式 AI 和高性能计算设计；美国出口管制禁止将 Blackwell 等先进芯片出口到中国。Neocloud 是围绕高端 GPU 集群建立的新型云服务商，按 GPU 小时出租算力。推理是让训练好的模型处理新请求并给出结果，训练则是构建模型本身的过程，通常更耗算力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_%28microarchitecture%29">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://builtin.com/articles/ai-neocloud-demand">What Is a Neocloud ? How AI Compute Is Changing Cloud ... | Built In</a></li>
<li><a href="https://www.cloudflare.com/learning/ai/inference-vs-training/">AI inference vs. training: What is AI inference? - Cloudflare</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Nvidia`, `#export controls`, `#Moonshot AI`, `#GPU compute`

---

<a id="item-3"></a>
## [长江存储第四座武汉工厂国产设备占比拟达 70%](https://www.reuters.com/world/china/chinas-top-flash-memory-chipmaker-targets-more-homegrown-tools-new-factory-2026-11-06/) ⭐️ 7.0/10

中国最大闪存芯片制造商长江存储（YMTC）计划自 2027 年起在武汉建设第四座工厂，目标将国产设备采购比例提升至至少 60%、最高 70%，高于第三座工厂目前超过 50%的水平。新工厂将生产超过 300 层的先进 NAND 闪存，主要面向数据中心与人工智能存储需求。 此举是中国领先存储工厂中尝试的最高国产设备比例之一，因而成为衡量中国芯片供应链在美国出口管制下能实现多大程度本土化的风向标。长江存储在中国 NAND 市场份额已升至 38.5%、超过三星，若三座新厂全部投产其产能有望翻倍，其设备选择将同时影响国产与海外设备厂商的需求格局。 清洗、抛光（CMP）与刻蚀设备预计将成为国产采购的主要增量，而光刻、检测等先进设备仍将依赖海外供应商。新工厂 300 层以上的 NAND 目标，使其进入 SK 海力士等领先供应商自 2025 年前后一直在推进的同一代际区间。

telegram · zaihuapd · 11月6日 08:34

**背景**: 3D NAND 闪存通过垂直堆叠存储单元而非横向缩小尺寸来提升密度，因此堆叠层数已成为衡量密度与成本的核心指标，并支撑着 AI 训练、推理以及冷数据归档等负载。长江存储于 2016 年在武汉成立，从事 3D NAND 的设计与制造，以晶圆、裸片以及旗下消费品牌致钛（Zhitai）对外销售。制造此类芯片需要薄膜沉积、等离子刻蚀、晶圆清洗、化学机械抛光等晶圆制造设备，而该市场长期由少数美国、日本和荷兰厂商主导。美国出口管制限制了中国获取先进芯片制造设备的能力，这正是长江存储推动国产设备验证与替代的主要动因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.06363v1">The future of 3D NAND flash technology - arXiv.org</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zhitai">Zhitai - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lam_Research">Lam Research - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductor-industry`, `#NAND-flash`, `#china-tech`, `#export-controls`, `#AI-infrastructure`

---

<a id="item-4"></a>
## [淘宝 MNN 团队开源 0.3B 端侧语言模型](https://www.ithome.com/1/023/212.htm) ⭐️ 7.0/10

11 月 6 日，淘宝 MNN 团队开源了约 3 亿参数的端侧语言模型 MNN-Pocket-0.3B，可在手机上完全离线运行，官方称在 iPhone 18 Pro 上平均解码速度约 350 token/s，INT4 部署文件仅 173 MB。团队通过采用 28 层结构并把词表从 151K 精简到 64K，达成了峰值内存低于 300 MB、解码超过 200 token/s 的设计目标，并按预训练、后训练、端侧部署分别开源了多个版本。 这是小模型与端侧推理浪潮中一个颇具参考价值的工程样本：一个体积不到 200 MB、离线即可达到数百 token/s 的模型，意味着语音助手、输入法、本地智能体等场景无需网络往返、无需支付云端推理成本，也不必把用户数据传出设备。该模型出自阿里淘宝团队，也说明大型电商与消费级应用厂商已把端侧大模型当作可落地的产品能力，而非研究演示。 官方数据来自 iPhone 18 Pro 这一特定高端机型，在中低端或较旧手机上实际速度大概率会明显下降；同时 0.3B 规模的模型更适合摘要、改写、意图识别等收窄任务，而非开放式复杂推理。对其他工程师最有价值的细节是把词表从 151K 大幅压缩到 64K，这直接削减了在小模型上占比过高的词嵌入与输出层参数，此外还同时放出了 INT4 权重以及预训练、后训练等不同阶段的检查点。

telegram · zaihuapd · 11月6日 15:13

**背景**: MNN 是阿里巴巴开源的高效轻量级深度学习推理框架，官方称其已支撑淘宝、天猫、优酷、钉钉等 30 多个生产应用的端侧 AI 能力。INT4 量化把模型权重从 16 位浮点压缩为 4 位整数，可将文件体积和内存带宽需求降低约四倍，代价是少量精度损失，这也是语言模型能塞进几百 MB 手机内存的关键。完全端侧运行意味着推理在本地完成、不发起网络请求，用模型能力换取更低的延迟、更好的隐私保护与离线可用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/alibaba/MNN">GitHub - alibaba/MNN: MNN: A blazing-fast, lightweight ...</a></li>
<li><a href="https://deepwiki.com/alibaba/MNN">alibaba/MNN | DeepWiki</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**标签**: `#on-device AI`, `#edge inference`, `#small language models`, `#model compression`, `#MNN`

---

<a id="item-5"></a>
## [Anthropic 通过 Plaid 让 Claude 读取银行与信用卡账户](https://www.theverge.com/ai-artificial-intelligence/1027652/anthropic-claude-plaid-personal-finance) ⭐️ 6.0/10

Anthropic 为 Claude 推出了个人理财功能，通过 Plaid 将 Claude 连接到用户的银行和信用卡账户，用户可以询问本月钱花在哪里，并获得按房租水电、购物、餐饮等类别划分的支出概览。该功能本周起以测试形式向美国 Pro、Max 和 Ultra 付费订阅用户开放。 这是大型 AI 实验室首次将通用助手直接接入用户本人的金融账户之一，标志着 AI 智能体从单纯回答问题迈向处理敏感个人数据的重要一步。此举让 Anthropic 同时与记账理财应用以及争夺“真实世界任务”的竞品助手形成竞争，也让用户对聊天机器人数据处理的信任程度成为关注焦点。 该功能为只读权限：Claude 无法转账、管理资金或提供投资建议，但可以查看账户余额、信用额度以及最长两年的交易记录。此次上线仅限美国地区的 Pro、Max 和 Ultra 付费订阅用户参与测试，因此可用范围与具体行为后续可能调整。

telegram · zaihuapd · 11月6日 00:54

**背景**: Plaid 是一家金融数据聚合服务商，应用通过它来关联用户的银行账户并获取交易数据，通常流程是用户在授权页面用银行账户完成验证，而不是把账号密码交给第三方，许多记账和支付类应用都依赖这一机制。由于读取金融数据的 AI 智能体可能造成数据泄露或滥用，安全从业者一般建议把此类访问限定为只读权限，并采用 OAuth 等标准授权框架，而不是授予完整的账户控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://plaid.com/products/auth/">Auth: Instant bank verification API | Plaid</a></li>
<li><a href="https://wezom.com/blog/plaid-integration-explained">Plaid Integration: How It Works , Use Cases &amp; Implementation</a></li>
<li><a href="https://www.okta.com/blog/ai/ai-agent-authorization-gap/">AI Agent Security: The Authorization Gap | Okta Secures AI</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI agents`, `#personal finance`, `#Plaid`, `#privacy`

---

<a id="item-6"></a>
## [印度计划 24 个月内推出自研 GPU 芯片](https://www.tomshardware.com/tech-industry/semiconductors/india-targets-creating-homegrown-gpus-within-2-years-and-plans-to-commercialize-indigenous-shakti-and-vega-risc-v-processors-sees-ai-boom-as-a-potential-repeat-of-the-y2k-opportunity-for-its-it-industry) ⭐️ 6.0/10

印度电子和信息技术部秘书 S. Krishnan 于 11 月 4 日表示，在「印度半导体使命 2.0」框架下，印度计划用约 24 个月时间开发出一款本土 GPU 芯片，并计划把基于 RISC-V 的 SHAKTI 与 VEGA 处理器推向商用市场。他把 AI 视为印度 IT 产业类似「千年虫」时期的新机遇，并称印度半导体市场规模目前约 500 亿美元，到 2030 年有望接近 1000 亿美元。 自研 GPU 计划若推进，将使印度与美中一样加入 AI 加速芯片的竞逐，从而不再只是全球半导体供应链中的设计外包与封测组装环节。同时，把 SHAKTI 和 VEGA 推向商用也意味着印度的 RISC-V 成果将从纯学术研究走向市场化，这对关注 AI 基础设施中 Arm 与 x86 替代方案的人来说颇具意义。 该表态没有提及任何制造伙伴、代工厂或芯片供应商，也未给出 GPU 的架构、性能目标或制程节点，因此执行层面的不确定性很高。值得注意的是，印度自家的旗舰 RISC-V 核心此前是在位于昌迪加尔的印度空间研究组织半导体实验室完成流片的，而非商业先进制程代工厂，这凸显了自研 GPU 计划必须跨越的制造短板。

telegram · zaihuapd · 11月6日 02:00

**背景**: SHAKTI 是印度理工学院马德拉斯分校 RISE 团队主导的开源处理器系列，涵盖基础型、多核型与实验型核心，目标是产出可量产的处理器、SoC 和开发板，其中 Moushik、RIMO 等设计已在印度空间研究组织的 SCL 完成制造。VEGA 则是印度高级计算发展中心（C-DAC）的自主 RISC-V 微处理器产品线，包括 64 位超标量乱序多核设计，如双核的 AS2161 DHRUV64 以及可启动完整 Linux 的 THEJAS64 系统级芯片。「印度半导体使命 2.0」是印度芯片激励计划的下一阶段，重点在于完善本土价值链与供应链韧性；而 GPU 比 CPU 核心难度更高，因为它除了硬件还需要完整的软件栈（驱动、编译器、库）配合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SHAKTI_%28microprocessor%29">SHAKTI (microprocessor) - Wikipedia</a></li>
<li><a href="https://vegaprocessors.in/">C-DAC | Vegaprocessors</a></li>
<li><a href="https://shakti.org.in/">Shakti Processor | Home</a></li>

</ul>
</details>

**标签**: `#India semiconductors`, `#GPU`, `#RISC-V`, `#AI hardware`, `#semiconductor policy`

---

<a id="item-7"></a>
## [广电总局重申扶持真人微短剧，收紧对 AI 剧的规范](https://www.ithome.com/1/023/215.htm) ⭐️ 6.0/10

11 月 5 日，国家广播电视总局相关负责人重申，微短剧领域要扶持真人剧、规范 AI 剧，并要求平台落实“凡播必审、全量人审”。该负责人还要求优化算法，持续打击 AI 洗稿、盗版翻拍以及未经授权使用肖像、声音等侵权行为。 这一表态意味着，在数量上已占据市场主体的 AI 微短剧将面临人工审核的瓶颈和更高的合规成本，可能抑制低成本 AI 内容流水线，而有利于具备正规审核能力的制作机构。这也为监管方如何把既有的播出审核义务套用到生成式 AI 视频内容上，提供了一个较早的政策先例。 广电总局在会上公布的数据显示，今年前 8 个月上线微短剧 43 万部，其中 AI 剧占比超过九成；该负责人强调 AI 应辅助精品创作、真人创作仍是微短剧主体，规范 AI 剧需守住版权和伦理底线。“全量人审”这一要求值得注意，因为它意味着平台层面不能仅靠全自动或抽样式审核来处理海量 AI 生成视频。

telegram · zaihuapd · 11月6日 06:40

**背景**: 微短剧是一种竖屏、节奏快、篇幅短的剧集形态，通常有几十到上百集、每集一两分钟，主要通过国内短视频和流媒体平台分发，如今已成为大众化、低成本的制作形式。国家广播电视总局是中国广播、电视和网络视听内容的最高主管部门，正在为这一形态建立专门规则，其中包括《微短剧发展管理办法》，对创作、推广、播出单位的备案、许可和内容审核义务作出规定。生成式视频工具让这类剧集可以低成本批量生产，这正是 AI 剧数量远超真人剧、监管聚焦审核、版权与肖像声音权益的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nrta.gov.cn/art/2026/6/24/art_113_73514.html">国家广播电视总局 公告公示 国家广播电视总局关于《微短剧发展管理办...</a></li>
<li><a href="https://www.gov.cn/gongbao/2026/issue_13006/202609/content_7082247.html">国家广播电视总局令（第16号） 微短剧发展管理办法__2026年第27号国务...</a></li>
<li><a href="https://baike.baidu.com/item/AI%E6%B4%97%E7%A8%BF/68808502">AI洗稿（利用人工智能技术洗稿的科研诚信问题）_百度百科</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#generative AI`, `#content moderation`, `#China policy`, `#media industry`

---

<a id="item-8"></a>
## [六部门发文：加快具身智能等前沿技术进入养老领域](https://api3.cls.cn/share/article/2527197?sv=859&amp;amp;os=web) ⭐️ 6.0/10

11 月 4 日，民政部等六部门印发《关于培育多元场景 促进适老用品产品消费的若干措施》，提出加快推进具身智能、大语言模型、脑机接口、外骨骼等前沿技术在养老领域的应用，并研发升级失能照护、康复护理、精神陪护智能设备。文件还鼓励智能养老服务机器人加快落地，推广“以租代售”等租赁模式，并培育银发 MALL、银龄市集等消费场景。 这是一项顶层政策信号，有望把国家科技项目资源和采购需求导向面向中国快速老龄化人口的机器人、人工智能企业。这意味着具身智能与辅助硬件可能从实验室演示走向有补贴的养老机构和消费渠道，从而影响中国“银发经济”的近期走向。 措施以国家重大科技项目为牵引，但并未给出具体资金规模、时间表或认证标准，落地仍待后续细则。文件强调“以租代售”等租赁模式值得关注，因为护理机器人和外骨骼单价较高，一直是其在机构养老中普及的主要障碍。

telegram · zaihuapd · 11月6日 07:31

**背景**: 具身智能指将人工智能嵌入机器人、人形机器人和自动驾驶车辆等物理系统，使其能够在真实世界中感知和行动，而不仅仅处理数据。脑机接口旨在将神经信号与外部设备连接，已有研究探索其在老年人认知与运动康复中的用途；外骨骼则为使用者提供物理支撑，帮助稳定步态、恢复行动能力。中国人口正在快速老龄化，政府多次推动智能养老技术，以缓解护理人员和养老机构的压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI? | NVIDIA Glossary</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11737249/">Brain computer interfaces for cognitive enhancement in older ...</a></li>
<li><a href="https://biologyinsights.com/exoskeleton-for-elderly-how-they-assist-seniors/">Exoskeleton for Elderly: How They Assist Seniors</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#embodied AI`, `#elderly care`, `#robotics`, `#China`

---

<a id="item-9"></a>
## [特斯拉将于明年年中逐步停产 Cybertruck，为 Cybercab 腾出产能](https://www.theverge.com/transportation/1028542/tesla-cybertruck-winding-down-production-2027) ⭐️ 6.0/10

特斯拉 CEO Elon Musk 周五在 X 上发文称，公司将在明年年中（据 The Verge 报道为 2027 年年中）于得州超级工厂“逐步停止”Cybertruck 的生产，以便该工厂把产能转向产量更高的 Cybercab。得州超级工厂是目前已知唯一组装 Cybertruck 的基地，官方并未提及是否会把生产转移到其他地点。 这一决定实际上承认了特斯拉最具标志性的车型未能打开大众市场——其累计交付量约 7 万辆，而最初的目标是年销约 25 万辆。这也标志着一次战略转向：特斯拉正把稀缺的工厂空间从低销量的消费级皮卡，转移到支撑其自动驾驶与网约车野心的 Cybercab 无人驾驶出租车上。 自 2023 年上市以来，Cybertruck 的销量从未接近其最初预测的年销 25 万辆，最高累计交付量估计仅约 7 万辆。特斯拉尚未说明 Cybertruck 的生产是否会转移到其他工厂，也未明确该车型是否会彻底停产，而且这一时间表目前仍只是 Musk 的口头表态，并非详细的生产计划。

telegram · zaihuapd · 11月6日 12:28

**背景**: 得州超级工厂是特斯拉的总部所在地和在美国最大的制造中心，负责生产 Model Y，同时也是 Cybertruck 的产地。Cybercab 是特斯拉专为无人驾驶网约车设计的双座车型，于 2024 年 10 月发布，没有方向盘和踏板，采用纯视觉自动驾驶方案，2026 年初投产，并于当年晚些时候在奥斯汀开始提供付费公开载客服务。由于两款车共用同一组装基地，停产 Cybertruck 是特斯拉为 Cybercab 腾出场区和产线的最直接方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tesla.com/giga-texas">Giga Texas | Tesla</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab</a></li>

</ul>
</details>

**标签**: `#特斯拉`, `#Cybertruck`, `#电动汽车`, `#制造业`, `#行业动态`

---

<a id="item-10"></a>
## [欧盟指控 TikTok 推荐算法造成有害“兔子洞”效应](https://www.cnbc.com/2026/11/06/eu-charges-tiktok-harmful-algorithmic-rabbit-hole-effects.html) ⭐️ 6.0/10

欧盟委员会依据《数字服务法》正式指控 TikTok 的推荐系统违规，称该平台未能采取有效措施应对“为你推荐”信息流所带来的风险。监管机构要求 TikTok 调整算法，使其更多依据用户的明确偏好，改进用户控制选项并定期对算法进行测试；若问题未能解决，母公司字节跳动明年可能面临最高相当于全球年营收 6% 的罚款。 这是迄今针对核心推荐算法最直接的监管挑战之一，可能迫使字节跳动改变“为你推荐”信息流在欧洲的内容排序方式。一旦作出最终裁定，将为《数字服务法》的系统性风险条款如何适用于以提升互动为目标的 AI 信息流树立先例，进而影响所有依赖类似排序机制的大型平台。 此次指控属于更广泛《数字服务法》调查中的初步认定，而非最终裁决，欧盟委员会认为持续推送相似内容可能影响心理健康。所要求的整改措施——提高用户明确偏好的权重、改进控制选项、定期测试算法——已超出单纯删除内容的范畴，直接针对排序设计本身。

telegram · zaihuapd · 11月6日 14:03

**背景**: 欧盟《数字服务法》于 2023 年 8 月起对大型在线平台全面生效，要求 Google、Meta、亚马逊等企业评估并缓解其服务造成的“系统性风险”，其中心理健康风险是重点之一。“兔子洞”效应指的是：推荐算法不断推送与用户此前互动内容相似的视频，可能逐步把人引向更小众甚至更极端的内容。TikTok 的“为你推荐”信息流高度依赖算法：新上传的视频会先被推送给一小批依据过往行为选出的测试用户，随后再根据互动信号扩大推荐范围，而不只依赖关注关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/23845672/eu-digital-services-act-explained">The EU ’s Digital Services Act is now in effect... | The Verge</a></li>
<li><a href="https://www.wired.com/story/tiktok-finally-explains-for-you-algorithm-works/">How TikTok &#x27;s &#x27; For You &#x27; Algorithm Works | WIRED</a></li>
<li><a href="https://www.themeadows.com/blog/social-medias-problems-with-predatory-algorithms/">Social Media &#x27;s Problem With Predatory Algorithms | Meadows...</a></li>

</ul>
</details>

**标签**: `#EU Digital Services Act`, `#TikTok`, `#recommendation algorithms`, `#platform regulation`, `#content moderation`

---

<a id="item-11"></a>
## [研究者发现苹果 iPhone 键盘隐藏约 10 万条禁推荐词](https://thenextweb.com/news/apple-iphone-keyboard-hidden-list) ⭐️ 6.0/10

独立研究者 Derik Kauffman 发现苹果系统中约 10 万条词条不会被 iPhone 键盘推荐，其中包括「Dictator Trump」「Sleepy Joe」等政治表达。这些限制并不阻止用户手动输入，但会屏蔽自动补全和滑行输入的建议。 这一发现引发了透明度与平台治理层面的质疑，因为输入法这一关键环节会悄然影响哪些词更容易被写出、哪些词需要额外费力。电子前哨基金会的批评表明，民权团体认为即便技术上并未封禁任何内容，未公开的屏蔽词清单本身也构成言论方面的隐忧。 苹果表示键盘的设计初衷是避免推荐冒犯性语言，但未解释政治词汇为何被纳入清单；该清单只影响联想推荐，并不会彻底阻止用户输入。电子前哨基金会的 David Greene 认为这份清单不应保密，用户应当被告知相关内容并有权自行修改。

telegram · zaihuapd · 11月6日 15:25

**背景**: 智能手机键盘依赖自动纠错和预测输入模型，在用户打字时对下一个可能出现的词进行排序推荐，滑行输入功能则通过手势轨迹预测整词，进一步扩展了这一机制。平台通常会维护内部屏蔽词清单，以免系统推荐侮辱性或冒犯性词汇。由于这些清单随操作系统一同分发且鲜有公开文档说明，外部研究者只能通过检查设备文件来了解其内容，本次发现的词条集合正是由此而来。

**标签**: `#privacy`, `#Apple`, `#censorship`, `#keyboard`, `#platform-transparency`

---

<a id="item-12"></a>
## [Telegram 13.2 支持在聊天内直接运行 HTML 互动消息](https://play.google.com/store/apps/details?id=org.telegram.messenger&amp;amp;hl=en_US) ⭐️ 6.0/10

Telegram 的 Android、iOS 与 macOS 客户端已升级至 13.2 版（Desktop 端为 7.4 版），开发者可以用 HTML、CSS 和 JavaScript 制作互动消息，直接在聊天窗口中运行，而无需另外打开 Mini App。本次更新还为群组与机器人话题新增了「侧边栏」布局，话题列表从屏幕右侧展开。 这一改动把类似 Mini App 的交互能力直接嵌入消息流，用户无需离开对话即可玩小游戏或使用小工具，从而降低了 Telegram 机器人生态的使用门槛。对机器人开发者和群组管理员而言，这是一条更轻量的互动内容路径，不过它仍属于客户端的功能迭代，而非平台层面的重大变革。 这类聊天内消息由客户端负责渲染，官方给出的例子包括支持触控操作并能保存进度的小游戏。侧边栏话题布局已在频道私聊和「收藏」中自动启用，而新特性需要用户升级到 13.2 / 7.4 版客户端才能使用。

telegram · zaihuapd · 11月6日 15:56

**背景**: Telegram Mini App 是用 HTML、CSS 和 JavaScript 编写的网页应用，需挂载到机器人上，通常以全屏浮层的形式覆盖在聊天界面之上启动，这也是目前平台上大多数互动机器人和小游戏的运行方式。话题（Topics）则是群组内类似论坛的分线程对话，Telegram 一直在尝试用不同方式在界面上呈现话题列表。本次更新把两者结合起来：一方面让基于网页的交互内容直接内嵌渲染，另一方面为分线程聊天提供了新的导航布局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iturrit.com/en/blog/telegram-mini-apps-2026-top-20-recommendations">Telegram Mini App 是 什 么 ？ 2026 必玩 20 个推荐应用；2026...</a></li>
<li><a href="https://www.telegwam.com/telegramminiapps/">telegram 官网迷你小程序 Mini Apps 开发指南 - Telegram 官网下载</a></li>
<li><a href="https://iturrit.com/blog/telegram-tips-secrets-improve-communication">Telegram Android 显示模式切换： 侧 边 栏 布 局 与液态玻璃对比 - Turrit</a></li>

</ul>
</details>

**标签**: `#Telegram`, `#interactive messages`, `#HTML/CSS/JS`, `#messaging platforms`, `#Mini Apps`

---

<a id="item-13"></a>
## [美国司法部「超级智能特别工作组」正式启动运作](https://www.theregister.com/ai-and-ml/2026/11/06/dojs-super-intelligence-task-force-up-and-running/5308074) ⭐️ 6.0/10

美国司法部宣布，其「超级智能特别工作组」（SINTF）已正式开始运作；该工作组由 10 月 13 日签署的一份总统备忘录授权设立，由国家情报总监领导，职责是维护美国在人工智能领域的领先地位并反制外国对 AI 的「滥用」。 该机构将把司法部涉 AI 的刑事与民事案件集中统筹，并参与阻止所谓「繁重监管」的立法建议，因此成为观察美国政府如何塑造 AI 规则的重要信号。它把检察官与情报官员而非技术监管者置于 AI 治理的核心位置，这可能会影响 AI 开发者、部署方以及任何可能面临 AI 相关执法的主体。 目前公开细节很少：成员名单、预算和执法范围均未披露，国防部 CTO Emil Michael 表示 AI 监管的具体内容将在本月稍晚公布。值得注意的是，该工作组设在司法部之下，却由国家情报总监领导，这一安排需要执法部门与情报界之间进行密切的跨机构协调。

telegram · zaihuapd · 11月6日 17:01

**背景**: 美国司法部是负责提起联邦刑事起诉并在民事诉讼中为政府辩护的联邦机构，因此让其牵头一个以 AI 为焦点的特别工作组，意味着 AI 问题正被当作执法与国家安全事务来处理，而不再只是纯技术政策议题。在此语境下，「特别工作组」是一种为协调跨部门事务而设立的临时性跨机构组织；而「超级智能」指的是假想中未来在广泛领域大幅超越人类能力的 AI 系统——尽管这类系统目前并不存在，该词却越来越多地被用于有关前瞻性监管的政策讨论中。

**标签**: `#AI policy`, `#regulation`, `#US DOJ`, `#national security`, `#superintelligence`

---