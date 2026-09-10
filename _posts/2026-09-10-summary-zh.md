---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10 23:05:38 +0000
lang: zh
report: default
---

> 从 280 条内容中筛选出 8 条重要资讯。

---

1. [蚂蚁国际携手 Visa 与 Mastercard 制定 AI 代理支付标准](#item-1) ⭐️ 8.0/10
2. [DeepSeek V4.1 Flash 发布：552B 因果编码器-解码器，原生视觉](#item-2) ⭐️ 8.0/10
3. [苹果发布 iPhone 18 Pro、首款折叠机 iPhone Duo、Watch S12 与 AirPods 5](#item-3) ⭐️ 7.0/10
4. [DeepSeek 合并快速、专家、识图模式，V4.1 Flash 即将发布](#item-4) ⭐️ 7.0/10
5. [HBM 短缺加剧，中国 AI 芯片厂商集体涨价](#item-5) ⭐️ 7.0/10
6. [腾讯混元开源音频编辑模型 AuK，并推出提速约 4.5 倍的 AuK-Flash](#item-6) ⭐️ 7.0/10
7. [DeepSeek 发布 DeepSelect：面向 DSA 与采样器的高性能 TopK 内核](#item-7) ⭐️ 6.0/10
8. [OpenAI 结束每年 1 美元政府试点，转为按用量定价](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [蚂蚁国际携手 Visa 与 Mastercard 制定 AI 代理支付标准](https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html) ⭐️ 8.0/10

2026 年 9 月 10 日，蚂蚁国际宣布与 Visa 和 Mastercard 合作，共同制定 AI 代理支付的通用标准，核心是一套“了解你的代理”（Know Your Agent，KYA）框架。三方表示，该框架将把 AI 代理关联到有效的法律实体，评估其行为并监测风险，同时让已在一家支付机构完成注册的代理无需在其他机构重复注册。 如果被广泛采纳，统一的 KYA 标准将让 AI 代理能够在卡组织、数字钱包、代理平台和线上商城之间自由迁移，从而消除代理驱动型购物在信任与接入方面的主要瓶颈。三方援引麦肯锡的预测称，到 2030 年 AI 代理可能处理全球 3 万亿至 5 万亿美元的消费者商业交易，因此谁定义了代理支付的身份与风险规则，谁就为一个规模巨大的市场设定了游戏规则。 KYA 被定位为代理经济中对应人类银行 KYC 的机制，通常包含签名身份头、用户签名的支付授权、代理信誉评分以及基于目录的吊销机制，使商户在结算前既能验证代理本身，也能验证其背后的授权用户。这一合作仍处于早期阶段：蚂蚁国际、Visa 和 Mastercard 已启动开发工作，但尚未公布详细的技术规范、时间表或治理规则。

telegram · zaihuapd · 9月10日 03:00

**背景**: 代理式商务（agentic commerce）指的是由 AI 代理代替用户去检索、比价并完成下单的线上购物模式。Visa 已于 2026 年 6 月 10 日将支付网络接入 ChatGPT，使 AI 代理能够在任何接受 Visa 的商户完成购买，用户只需绑定卡片并设定消费限额。由于这类代理是自主行动的，卡组织如今需要一种方式来确认代理的合法身份并追溯到可追责的个人或企业——这正是 KYC 当年为人类账户解决的问题。蚂蚁国际则是中国蚂蚁集团的海外业务板块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technode.com/2026/09/10/ant-international-visa-and-mastercard-develop-know-your-agent-framework-for-ai-payments/">Ant International, Visa and Mastercard develop Know-Your ...</a></li>
<li><a href="https://techjournal.org/agentic-commerce-ai-agents-shopping-payments">Agentic Commerce: How AI Agents Now Shop &amp; Pay for You (2026)</a></li>
<li><a href="https://eco.com/support/en/articles/14846277-know-your-agent-kya-identity-for-agent-payments">Know Your Agent (KYA): Identity for Agent Payments | Support</a></li>

</ul>
</details>

**标签**: `#AI payments`, `#Fintech`, `#Standards`, `#AI agents`, `#Visa/Mastercard`

---

<a id="item-2"></a>
## [DeepSeek V4.1 Flash 发布：552B 因果编码器-解码器，原生视觉](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 8.0/10

DeepSeek 正式发布 V4.1 Flash，这是其全新模型结构系列中最小尺寸的模型，采用 552B 参数的 Causal-Encoder-Decoder 结构，输入、输出激活参数分别为 8B 和 16B，并原生支持多模态视觉理解。该模型已上线 DeepSeek API，模型名为 deepseek-flash，新价格于 2026 年 9 月 10 日 12:00 生效；9 月 14 日 12:00 后，deepseek-v4-pro 的请求将被路由至 V4.1 Flash 并按该模型价格计费。 如果得到验证，一个总参数 552B、单次仅激活 8B/16B 参数的模型，将代表业界在“低成本高能力”方向上迈出的重要一步，而原生视觉能力也会让 DeepSeek 的最低价位档在多模态任务上具备竞争力。将 deepseek-v4-pro 的请求自动路由至 V4.1 Flash 会直接影响现有 API 用户，他们需要重新验证生产环境中的输出质量与成本假设。 公告给出了具体的计费规则：新价格于 2026 年 9 月 10 日 12:00 生效，而自 9 月 14 日 12:00 起 deepseek-v4-pro 的调用会被静默重定向至 V4.1 Flash，这实际上是一次模型替换而不只是价格调整。值得注意的是，公告中的日期指向未来，且没有配套的技术报告、基准测试表格或第三方评测，因此其架构与性能主张仍未经独立验证。

telegram · zaihuapd · 9月10日 05:54

**背景**: 在 Transformer 术语中，Causal-Encoder-Decoder 指的是把双向读取上下文的编码器与从左到右因果生成 token 的解码器结合起来，这种混合结构常用于既需要理解（例如图像或长提示）又需要生成的场景。“激活参数”指每次前向计算中真正参与运算的那部分权重，是混合专家（MoE）等稀疏化设计推广开来的技巧；总参数 552B、激活仅 8B-16B 意味着每个 token 大部分权重处于闲置状态，从而降低算力消耗和成本。原生多模态视觉则意味着模型可以直接接受图像输入，而无需外挂独立的视觉模块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.labellerr.com/blog/exploring-architectures-and-configurations-for-large-language-models-llms/">Large Language Model Architecture Explained [Updated]</a></li>
<li><a href="https://www.unite.ai/decoder-based-large-language-models-a-complete-guide/">Decoder -Based Large Language Models : A Complete Guide – Unite.AI</a></li>
<li><a href="https://www.explainx.ai/blog/llm-model-parameters-billions-explained">What are parameters in a large language model? Billions ...</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#llm`, `#model-release`, `#multimodal`, `#ai-infrastructure`

---

<a id="item-3"></a>
## [苹果发布 iPhone 18 Pro、首款折叠机 iPhone Duo、Watch S12 与 AirPods 5](https://www.apple.com.cn/iphone-18-pro/) ⭐️ 7.0/10

苹果在昨晚的发布会上一口气推出了 iPhone 18 Pro、可折叠的 iPhone Duo、Apple Watch Series 12 与 Watch Ultra 4，以及 AirPods 5，并公布了新品的国行售价和发售日期。同时，仍在售的多款旧型号价格上调。 这是苹果今年规模最大的一次硬件更新，也是它首次进入折叠屏手机品类——这一形态此前由三星、华为等对手主导多年。此次发布将定调整个假日季的高端智能手机市场，影响中国市场的运营商和渠道促销，也反映出苹果在该地区的定价策略。 iPhone Duo 是苹果首款折叠屏 iPhone，国行版本不设实体 SIM 卡槽，仅可通过 eSIM 激活；它搭载 A20 Pro 芯片、4800 万像素融合式双摄系统，并采用迄今为止最大的 iPhone 显示屏，支持最高 120Hz 的 ProMotion 自适应刷新率和最高 3000 尼特的户外峰值亮度。原始 Telegram 帖子只是苹果官网链接的汇总，并未提供独立的技术分析或跑分数据。

telegram · zaihuapd · 9月10日 01:20

**背景**: 苹果每年 9 月都会举办大型硬件发布会，iPhone 18 系列（含 iPhone Duo）构成第二十代 iPhone 产品线，接替 iPhone 17 Pro 和 iPhone 17 Pro Max。折叠屏手机采用铰链连接的柔性屏幕，展开后可获得接近平板大小的显示面积，这一形态此前由三星和华为率先普及。在中国市场，苹果销售“国行”版本机型，配有本地定价与保修，而近几代 iPhone 在该地区已逐步转向仅支持 eSIM 的设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/IPhone_Duo">IPhone Duo - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.apple.com.cn/iphone-duo/">iPhone Duo - Apple (中国大陆)</a></li>
<li><a href="https://www.apple.com.cn/shop/buy-iphone/iphone-duo">购买 iPhone Duo - Apple (中 国 大陆)</a></li>

</ul>
</details>

**标签**: `#Apple`, `#hardware`, `#product-launch`, `#consumer-tech`, `#iPhone`

---

<a id="item-4"></a>
## [DeepSeek 合并快速、专家、识图模式，V4.1 Flash 即将发布](https://www.ithome.com/1/000/602.htm) ⭐️ 7.0/10

DeepSeek 宣布将快速、专家、识图三种模式合并为统一的“智能模式”，用户无需再手动切换，模型会自动判断任务复杂度，并在输入图片时激活视觉能力。公司同时表示计划在 2026 年 9 月 10 日前后发布 V4.1 Flash，称经内外测试其在性能、费用、速度和总用时上全面超越 V4 Pro；此前的多模态视觉模型 V4-Flash-Vision-Exp 已上线 API 平台。 这次合并消除了长期以来用户必须自行猜测该用哪一档模型的摩擦点，让 DeepSeek 朝着一体化自动路由的交互形态靠拢，与 OpenAI、Google 的做法趋同。如果 V4.1 Flash 确实在成本与速度上优于 V4 Pro、质量上不落下风，将会对竞争对手的定价形成压力，并让开发者和自部署用户以更低成本获得接近前沿水平的推理能力。 为保证兼容，原有的 deepseek-v4-flash 与 deepseek-v4-flash-vision-exp 接口会临时路由到 V4.1 Flash；第三方早期测试报告其吞吐可达约每秒 400 token，且价格更低。另有消息称旧的 V4 Pro 通道将在 9 月 14 日前后切换下线，因此 API 使用者应提前确认路由与弃用时间表，再迁移生产环境的工作负载。

telegram · zaihuapd · 9月10日 02:25

**背景**: DeepSeek 是推出开放权重模型 DeepSeek-V4 与 R1 系列的中国 AI 实验室，其 2025 年的发布因以极低成本实现有竞争力的性能而受到全球关注。其产品线此前按模式拆分：快速廉价档、较慢的“专家”推理档，以及支持视觉的变体，用户每次提问前都要先做选择。将这些模式合并为可自动判断难度并处理图片的单一模式，属于产品层面的简化，而 V4.1 Flash 正是支撑这一统一界面的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>
<li><a href="https://www.geeky-gadgets.com/deepseek-v4-1-flash-review/">DeepSeek V4.1 Flash Review and Performance Test - Geeky Gadgets</a></li>
<li><a href="https://www.digitalapplied.com/blog/deepseek-v4-1-flash-pro-routing-prices-early-tests">DeepSeek V4.1 Flash: Benchmarks, Prices and Pro Cutoff</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI Models`, `#Multimodal`, `#LLM`, `#Model Release`

---

<a id="item-5"></a>
## [HBM 短缺加剧，中国 AI 芯片厂商集体涨价](https://www.reuters.com/world/asia-pacific/chinas-ai-chipmakers-raise-prices-high-bandwidth-memory-shortage-bites-2026-09-10/) ⭐️ 7.0/10

随着全球高带宽存储器（HBM）供应持续紧张，华为、寒武纪等中国 AI 芯片厂商已开始上调产品价格：华为昇腾 950DT 的报价较两个月前上涨约 20%—50%，部分老款芯片上涨约 30%，寒武纪新一代思元 690 也预计涨价约 20%—30%。路透社报道称，本轮涨价由 HBM 供应短缺叠加美国出口限制共同推动。 这轮涨价说明，制约中国国产 AI 算力扩张的核心瓶颈正从逻辑芯片设计转向存储供应，而这一环节很难被快速国产替代。对于已经拿不到英伟达高端芯片的中国云厂商和 AI 实验室来说，加速器涨价会直接抬高训练与推理成本，可能拖慢国产大模型的扩展节奏。 HBM 目前仅由 SK 海力士、三星和美光三家供应，而这三家都受美国对华出口管制影响；由于 HBM 采用 3D 堆叠并与计算裸片共同封装，其囤货难度也远高于普通 DRAM。报道中的涨幅属于渠道报价或市场询价区间，并非官方指导价，实际合同价格可能因采购量和客户不同而有差异。

telegram · zaihuapd · 9月10日 09:29

**背景**: 高带宽存储器（HBM）通过把多层 DRAM 裸片垂直堆叠、用超宽接口互联，并与 AI 加速器封装在同一基板上，从而让 GPU/NPU 能以足够高的带宽为计算单元输送数据，支撑大模型训练与推理。由于它与芯片共同封装，AI 加速器无法简单地用普通服务器内存替代，因此 HBM 被称为 AI 硬件的“内存墙”。华为昇腾 950 系列采用华为自研的 HBM 级存储，寒武纪思元 690 则是其最新的数据中心加速器，性能定位对标英伟达 H100 级别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.techradar.com/pro/huawei-ascend-950-vs-nvidia-h200-vs-amd-mi300-instinct-how-do-they-compare">Huawei ’s Ascend 950 goes head-to-head with... | TechRadar</a></li>
<li><a href="https://aiwiki.ai/wiki/cambricon_siyuan_690">Cambricon Siyuan 590/ 690 | AI Wiki</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#HBM`, `#China Semiconductor`, `#Supply Chain`, `#Export Controls`

---

<a id="item-6"></a>
## [腾讯混元开源音频编辑模型 AuK，并推出提速约 4.5 倍的 AuK-Flash](https://x.com/TencentHunyuan/status/2097996926876795197) ⭐️ 7.0/10

腾讯混元正式发布开源音频编辑模型 AuK，可通过自然语言指令配合参考音频，统一完成语音生成与编辑，支持零样本文本转语音、音色/风格/情绪编辑、去口音以及多人语音分离等功能。同时发布的 AuK-Flash 采用 4 步推理，在匹配条件下速度约为原模型的 4.5 倍，代码、模型权重与演示均已上线。 AuK 把过去需要 TTS、音色转换、语音增强、音源分离、韵律编辑等多个专用工具拼成的流水线，整合进一个可跟随指令的模型中，有望显著降低语音编辑类产品的工程成本。由于权重、代码以及微调流程均已公开，这是一次可立即使用的开源贡献，而非仅发布闭源 API。 该模型覆盖五大类任务：语音生成、内容编辑、增强与分离、副语言属性编辑（音色、风格、情绪、口音）以及声学编辑。AuK-Flash 的 4 步推理之所以能提速，部分原因在于省去了无分类器引导（classifier-free guidance）；发布内容包含 Gradio 演示、ComfyUI 节点、微调流程以及 Hugging Face Spaces 网页演示，权重同时托管在 Hugging Face 与 ModelScope 上。

telegram · zaihuapd · 9月10日 11:56

**背景**: 零样本语音合成指模型无需针对特定说话人做微调，仅凭一小段参考音频就能用从未见过的新音色生成语音。指令驱动的音频编辑则是较新的方向，它把大语言模型「遵循提示词」的范式搬到音频上，用户可以直接说「去掉口音」或「把语气改得更悲伤」，而不必调校底层信号参数。无分类器引导（classifier-free guidance）是一种常见的推理技巧，能提升生成质量，但每步都需要额外的前向计算，因此去掉它是加速生成的常规做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/AuK">Tencent-Hunyuan/ AuK : AuK : An Open-Source Foundational Model for...</a></li>
<li><a href="https://huggingface.co/tencent/AuK-Flash">tencent/ AuK - Flash · Hugging Face</a></li>
<li><a href="https://auk-project.github.io/">AuK — An Open-Source Foundational Model for Speech Generation...</a></li>

</ul>
</details>

**标签**: `#audio-editing`, `#open-source-models`, `#text-to-speech`, `#tencent-hunyuan`, `#speech-generation`

---

<a id="item-7"></a>
## [DeepSeek 发布 DeepSelect：面向 DSA 与采样器的高性能 TopK 内核](https://github.com/deepseek-ai/DeepSelect) ⭐️ 6.0/10

DeepSeek-AI 发布了 DeepSelect v1.0.0，这是一套开源的高性能 GPU TopK 内核库，专门面向 DeepSeek 稀疏注意力（DSA）和采样器场景。据官方说明，该内核相比原生 torch.topk 可提速 2 至 20 倍。 TopK 选择既是长上下文稀疏注意力的关键步骤，也是采样阶段的关键算子，因此这一单点内核提速 2 至 20 倍，有可能直接转化为 LLM 推理吞吐和首 token 延迟上的可观收益。DeepSeek 将其开源，等于为推理与系统工程师部署 DSA 类模型提供了一个可直接接入的优化方案，而不必自行重写这部分算子。 该库面向两类不同场景：DSA 内部的 top-k token 选择，以及采样阶段；2 至 20 倍的提速是一个区间，说明实际收益高度依赖 batch size、序列长度、k 取值以及 GPU 架构。与大多数手工调优内核一样，真正落地时需要确认自身推理栈的 shape 与数据类型与已发布内核所支持的范围相匹配。

telegram · zaihuapd · 9月10日 07:28

**背景**: DeepSeek 稀疏注意力（DSA）是随 DeepSeek-V3.2-Exp 一同引入的注意力机制：先用一个轻量的“lightning indexer”为候选 token 打分，然后每个 query 只关注得分最高的少量 token，从而降低长上下文注意力的平方级开销。这一设计使得 TopK 选择成为每一层、每一个解码步都要执行的热点路径。而 GPU 上的 TopK 由于数据分散、各行长度不一、访存压力大，一直很难高效并行化，这也正是 DeepSelect 这类专用内核比算子本身的简单外表更重要的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.02556">[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open ... DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models DeepSeek Sparse Attention (DSA) — NVIDIA cuDNN DeepSeek Sparse Attention | deepseek-ai/DeepSeek-V3.2-Exp ... LLMs-from-scratch/ch04/09_dsa at main · rasbt/LLMs ... - GitHub GitHub - Open-Superintelligence-Lab/deepseek-sparse-attention ... DeepSeek Sparse Attention (DSA) - AI Wiki</a></li>
<li><a href="https://docs.nvidia.com/deeplearning/cudnn/latest/fe-oss-apis/dsa.html">DeepSeek Sparse Attention (DSA) — NVIDIA cuDNN</a></li>

</ul>
</details>

**标签**: `#GPU Kernels`, `#LLM Inference`, `#Sparse Attention`, `#CUDA Optimization`, `#DeepSeek`

---

<a id="item-8"></a>
## [OpenAI 结束每年 1 美元政府试点，转为按用量定价](https://www.gelonghui.com/live/2662128) ⭐️ 6.0/10

美国总务管理局（GSA）的声明显示，OpenAI 将结束此前允许政府机构每年以 1 美元使用其模型的试点计划，改为按用量收费，同时联邦工作人员可按标准价格五折使用相关工具。GSA 表示，试点期间约有 350 万名联邦雇员使用了 ChatGPT，累计节省约 14 亿美元。 这一变化意味着象征性的高额补贴安排告一段落，OpenAI 的公共部门业务转向常规的按量付费合同，可能成为其他面向政府销售的 AI 厂商效仿的模板。这也说明生成式 AI 工具在联邦机构中已从试验性试用转变为常规的预算项目，成本与用量成为采购的核心议题。 此次定价调整只针对美国联邦政府客户；联邦雇员享受的五折优惠是在标准价格基础上计算，而非此前的每年 1 美元固定费用。14 亿美元的节省数字由 GSA 提供，对应的是试点期间的补贴安排，属于估算值而非经过审计的数据。

telegram · zaihuapd · 9月10日 15:51

**背景**: 美国总务管理局（GSA）是负责政府采购、共享服务和工作场所政策的联邦机构，通常由政府统一谈判并公布面向全政府的软件采购协议。OpenAI 政府版是一项旨在把先进 AI 工具带给美国公共服务人员的计划，每年 1 美元的试点是其中最具象征意义的定价举措。按用量定价意味着客户根据实际使用量付费——对 AI 服务而言通常按 token、API 调用次数或席位数计量，而不是缴纳固定订阅费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/zh-Hans-CN/global-affairs/introducing-openai-for-government/">隆重推出 OpenAI 政 府 版 | OpenAI</a></li>
<li><a href="https://www.phppan.com/2025/01/midjourney-vs-openai-subscription-and-pay-as-you-go-pricing/">Midjourney 和 OpenAI 的定价逻辑给我们的启示 | 潘锦的空间</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI policy`, `#government procurement`, `#pricing`, `#ChatGPT`

---