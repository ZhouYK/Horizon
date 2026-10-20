---
layout: default
title: "Horizon Summary: 2026-10-20 (ZH)"
date: 2026-10-20 23:03:27 +0000
lang: zh
report: default
---

> 从 168 条内容中筛选出 7 条重要资讯。

---

1. [DeepSeek 据称深度参与华为未来 AI 芯片设计](#item-1) ⭐️ 8.0/10
2. [DeepSeek 开源内部大规模推理框架 DeepInfer](#item-2) ⭐️ 8.0/10
3. [OpenAI 称新模型将 COBOL 迁移准确率提升至 97.9%](#item-3) ⭐️ 8.0/10
4. [英伟达被指封杀使用竞品芯片的小型云厂商，禁止其参加 GTC 柏林站](#item-4) ⭐️ 7.0/10
5. [小米 MiMo-V2.6-Pro 上线 WorkBuddy，宣称登顶全球开源智能指数](#item-5) ⭐️ 7.0/10
6. [X 调整推荐算法：优先停留时长与完读率](#item-6) ⭐️ 6.0/10
7. [工信部收紧准入规则，防范不合理创新汽车设计进入市场](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek 据称深度参与华为未来 AI 芯片设计](https://www.theinformation.com/articles/deepseek-shaping-huaweis-ai-chips-growing-challenge-nvidia) ⭐️ 8.0/10

据 The Information 报道，DeepSeek 正与华为紧密合作，参与设计计划于 2027 年及以后推出的未来 AI 芯片，华为工程师已长期驻场 DeepSeek 办公室。这种合作超出了常规的供应商沟通，把 DeepSeek 在模型计算和处理器间数据传输方面的建议直接纳入华为的芯片设计。 中国最受关注的 AI 实验室与旗舰芯片厂商之间异常深入的合作关系，可能显著降低中国在构建前沿模型时对英伟达硬件的依赖。如果成功，这将强化一条国产 AI 技术栈，而这条技术栈在受出口管制影响的全球 AI 基础设施与半导体供应链中正变得越来越重要。 据报道，双方的合作聚焦于 2027 年或更晚推出的芯片，同时 The Information 指出 DeepSeek 并未放弃英伟达，仍在设法获取其先进处理器。在现阶段参与协同设计，意味着 DeepSeek 关于模型实际计算方式、加速器之间如何交换数据的反馈，可能在芯片流片数年前就影响华为的架构。

telegram · zaihuapd · 10月20日 05:10

**背景**: DeepSeek 是一家总部位于杭州的 AI 公司，由对冲基金幻方量化资助，发布开源权重大语言模型，并凭借 2025 年 1 月的 DeepSeek-R1 引起全球关注。华为的 AI 加速器昇腾（Ascend）NPU 系列，是中国在训练和运行大模型方面替代英伟达 GPU 的主要国产方案。美国的出口限制使中国企业难以获得英伟达最先进的芯片，这为国产硬件与软件的协同设计创造了强烈动力，即由模型开发者直接与芯片设计者合作来优化性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_%28Company%29">DeepSeek (Company)</a></li>
<li><a href="https://ascend-tech.io/">ascend -tech.io | Huawei Ascend AI Accelerators for Enterprise</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-reportedly-acquired-two-million-ascend-910-ai-chips-from-tsmc-last-year-through-shell-companies">Huawei reportedly acquired two million Ascend 910 AI chips from...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Huawei`, `#DeepSeek`, `#semiconductors`, `#Nvidia`

---

<a id="item-2"></a>
## [DeepSeek 开源内部大规模推理框架 DeepInfer](https://github.com/deepseek-ai/DeepInfer) ⭐️ 8.0/10

10 月 20 日，DeepSeek 将其内部生产环境使用的大规模推理框架 DeepInfer 开源，并同步开源了配套的 Token 编解码组件 deepseek-recipe。基于该框架，DeepSeek V4.1 Flash 单一集群的吞吐达到 155 万亿 Tokens/天，且可同时运行在英伟达 GPU 与华为昇腾平台上。 能够支撑这种量级服务的推理框架通常被前沿实验室视为核心资产而闭源，因此开源它意味着对外公开了生产级服务栈背后的具体架构取舍，而不仅仅是研究成果。对英伟达与华为昇腾硬件的双重支持尤其值得关注，它为社区在硬件多元化与供应受限的环境下做高吞吐服务提供了一个少见的参考设计。 该框架具备分布式推理、推测解码与结构化输出等能力，并且可以让 KVCache 保留 72 小时以上。不过配套的公告内容较为简略：除了 155 万亿 Tokens/天这一核心数字外，并未给出详细的基准测试或设计文档，因此目前还无法对吞吐数据做独立验证。

telegram · zaihuapd · 10月20日 09:11

**背景**: 在规模化场景下服务大语言模型，本质上是一个显存与调度问题：KV Cache 保存已处理 token 的注意力键值，避免模型重复计算，而它的体积会随上下文长度和并发数增长，这正是长时缓存保留与分层缓存成为关键工程议题的原因。推测解码是一种相关的加速手段，由更小更快的草稿模型先行猜测若干 token，再由大模型一次性验证，从而在不改变输出分布的前提下降低延迟。用于展示 DeepInfer 吞吐的 DeepSeek V4.1 Flash 是当前 DeepSeek API 上的模型，原生支持多模态，并对 KV Cache 做了大幅压缩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linux.do/t/topic/3050218">Deepseek ... - LINUX DO</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.</a></li>
<li><a href="https://huggingface.co/blog/whisper-speculative-decoding">Speculative Decoding for 2x Faster Whisper Inference</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#open-source`, `#distributed systems`, `#DeepSeek`, `#Ascend/NVIDIA`

---

<a id="item-3"></a>
## [OpenAI 称新模型将 COBOL 迁移准确率提升至 97.9%](https://openai.com/index/low-resource-programming-languages/) ⭐️ 8.0/10

OpenAI 公布的结果显示，其最新模型系列在低资源编程语言上表现大幅提升：在覆盖 20 种语言的“从零构建 SQLite”测试中，GPT-6 Astra 将平均通过率从 GPT-5.6 Sol 的 26.8% 提升到 87.4%，而成本更低的 GPT-6 Luna 也达到 40.3%，API 成本下降 78%。在老旧 COBOL 代码向现代语言迁移的任务上，GPT-6.1 Sol 在低推理强度下准确率从 5.4% 升至 86.6%，成本降低 39%；在高推理强度下准确率高达 97.9%。 COBOL 至今仍支撑着银行、保险和政府机构的交易处理、薪资发放和批处理系统，但能够维护它的工程师越来越少，因此接近 98% 的迁移准确率将让大规模遗留系统现代化在商业上变得可行。成本下降的说法也表明，用大模型重写几十年前的代码库正从研究演示走向企业可落地的实用方案。 这些提升与推理强度明显相关：COBOL 迁移在低推理强度下为 86.6%，高推理强度下达到 97.9%，意味着最高准确率需要更高的推理成本；而廉价版 Luna 在多语言 SQLite 基准上仍明显落后（40.3% 对 87.4%）。配套的评测集已在 GitHub 开源，但模型名称（GPT-6 Astra、GPT-5.6 Sol、GPT-6.1 Sol、GPT-6 Luna）与具体数字均来自二手摘要，尚未经过独立复现验证。

telegram · zaihuapd · 10月20日 14:24

**背景**: COBOL（Common Business-Oriented Language）于 1959 年为商业数据处理而设计，如今仍广泛运行在大型机上处理大规模批处理与交易业务，尽管新开发几乎都用现代语言完成。由于代码大模型的训练数据绝大多数是 Python、Java、JavaScript 等主流语言，那些公开代码稀缺的“低资源编程语言”在代码生成和翻译任务上长期表现不佳。所谓遗留系统现代化，就是把这类老旧系统迁移到现代平台，这一过程成本高昂且高度依赖人工，AI 代码模型直到最近才开始涉足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/low-resource-programming-languages/">Advancing coding in low‑resource programming languages</a></li>
<li><a href="https://en.wikipedia.org/wiki/COBOL">COBOL - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/low-resource-programming-languages-lrpls">Low-Resource Programming Languages - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#COBOL`, `#code-migration`, `#LLM-evaluation`, `#legacy-modernization`

---

<a id="item-4"></a>
## [英伟达被指封杀使用竞品芯片的小型云厂商，禁止其参加 GTC 柏林站](https://x.com/SemiAnalysis_/status/2111162214891610496?s=20) ⭐️ 7.0/10

据报道，英伟达拒绝多家新兴云服务商参加即将在柏林举行的 GTC 大会，被拒原因并非技术不达标，而是这些厂商在自有云平台中引入了 AMD GPU、Google TPU 等竞品芯片。英伟达目前尚未就该事件公开置评，相关说法经由 SemiAnalysis 的一条帖子传播开来。 若情况属实，这意味着这家占据主导地位的 AI 芯片供应商把大会参会资格当作对客户施压的筹码，而这正是监管机构在 GPU 市场上已经在审视的一类行为。这同时让中小型 AI 云厂商陷入两难：一旦转向非英伟达硬件，就可能失去 GPU 优先供应、融资支持，甚至影响上市计划。 据称该限制并不适用于超大规模云厂商，因为它们拥有足够的采购体量和自研芯片能力，可以在谈判中与英伟达平起平坐。目前这一说法仅来自对 SemiAnalysis 推文的二手转述，既无一手信源，也未点名具体公司，英伟达同样没有作出回应。

telegram · zaihuapd · 10月20日 12:32

**背景**: GTC（GPU 技术大会）是英伟达面向开发者和客户的旗舰活动，能否受邀在某种程度上反映了厂商在该公司合作伙伴生态中的地位。此次涉及的云厂商属于“Neocloud”一类，即 CoreWeave、Nebius 这样专门出租 GPU 算力用于 AI 训练和推理、而非提供完整通用云服务的企业。Google TPU 是谷歌为深度学习负载专门设计的自研 ASIC 芯片，在大模型训练上是英伟达 GPU 的直接替代方案。值得注意的是，其中多家新兴云厂商还接受了英伟达的投资，其算力租赁业务也获得英伟达的收入兜底，这让事件带上了不同寻常的利益冲突色彩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group - Wikipedia</a></li>
<li><a href="https://news.qq.com/rain/a/20260525A07W6100">Neocloud 的订单 联想集团ISG的利润_腾讯 新 闻</a></li>
<li><a href="https://developer.aliyun.com/article/1650659">详解 TPU ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI infrastructure`, `#GPU market`, `#antitrust`, `#cloud providers`

---

<a id="item-5"></a>
## [小米 MiMo-V2.6-Pro 上线 WorkBuddy，宣称登顶全球开源智能指数](https://weibo.com/6486870325/5356179212995907) ⭐️ 7.0/10

小米技术宣布 Xiaomi MiMo-V2.6-Pro 正式上线 WorkBuddy 平台，称其在 Artificial Analysis 智能指数上获得 46 分、位列全球开源第一，并支持 1M 超长上下文、多智能体分工协作，以及对图像、视频、音频、文本的全模态联合理解。该模型面向长任务托管、深度研究、设计出稿、文档办公、小工具开发等长程工作流，目前已开放体验。 如果这一评测成绩站得住脚，一款中国开源旗舰模型将登上被广泛引用的第三方榜单首位，进一步证明开源模型在智能体与推理任务上已能对标闭源模型。这将直接影响开发者在长上下文、多模态智能体流水线中的基座模型选型，也会加剧整个开源大模型市场的价格竞争。 模型本体已于 2026-09-22 发布并开源，因此本次更多是其在 WorkBuddy 平台上的首次完整形态落地，而非全新发布；OpenRouter 显示其上下文窗口为 1,050,000 词元，定价约为每百万输入词元 0.4133 美元、每百万输出词元 0.8265 美元。小米的披露集中于模型能力本身，尚未详细说明 WorkBuddy 在底层如何做智能体调度、上下文隔离、失败重试与权限控制。

telegram · zaihuapd · 10月20日 13:40

**背景**: Artificial Analysis 智能指数是一个 0 到 100 分的综合评测，由智能体、编程、通用能力、科学推理四大类生产级基准加权平均得出，因此 46 分反映的是综合能力而非单项测试成绩。这里所说的“开源”通常指开放权重，即训练好的参数可以下载，但训练数据与代码未必公开。1M 词元上下文窗口指的是模型单次会话能容纳多少文本（约合上百万词元），这对长文档分析和多步智能体工作流至关重要；“全模态”是指同一个模型可同时处理图像、视频、音频与文本，“多智能体”则指 WorkBuddy 会把一个任务拆分给多个协作的模型实例完成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index v4.3.2 | Artificial Analysis</a></li>
<li><a href="https://openrouter.ai/xiaomi/mimo-v2.6-pro">MiMo - V 2 . 6 - Pro - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#llm`, `#open-source-models`, `#xiaomi`, `#multimodal`, `#long-context`

---

<a id="item-6"></a>
## [X 调整推荐算法：优先停留时长与完读率](https://x.com/rohanpaul_ai/status/2112419861767045586) ⭐️ 6.0/10

X 调整了「为你推荐」信息流背后的两阶段排序机制，新排序模型更看重用户停留时长以及帖子的完读率，马斯克称新模型「预测有效时长的能力大幅提升」。更早的检索阶段也发生变化：系统把用户和帖子转化为向量，从未关注的账号中拉取最相关内容，并按完读率筛选，用户通常读到一半就放弃的帖子更难进入推荐池。 停留时长和完读率奖励的是用户真正去读的内容，而不是只换来快速点击的内容，因此这一变化可能改变哪些帖子、哪类账号能在全球最大的公共社交平台之一上获得曝光。它也呼应了整个行业从单纯追求互动量转向优化持续注意力的趋势——YouTube 早前转向「预期观看时长」就是最典型的先例。 X 表示日活跃用户总时长从 8 月中旬约 4100 亿秒增至 10 月中旬约 5000 亿秒，但并未公布模型架构、评估方法或人均数据。向量检索阶段的一个明显好处是让冷启动内容和未关注账号在排序前就有机会被考虑，但按完读率筛选也可能压制那些读者很少读完的长文或论述复杂的帖子。

telegram · zaihuapd · 10月20日 07:29

**背景**: 大规模推荐系统通常采用级联架构：检索阶段先把数十亿候选内容收窄到几千条，排序阶段再为具体用户对这个小候选池排序。向量检索把用户和帖子表示为高维嵌入向量，并按相似度进行匹配，因此内容一经嵌入即可参与召回，即使还没有互动历史。所谓「停留时长」是指用户在划走之前停留在某条帖子上看了多久，它已成为 Instagram、TikTok、Facebook 以及 X 上的关键互动信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fylom.com/episode/45d1bb22-f76d-4b84-80a3-2ef23c48308e">How recommendation algorithms decide what billions of... — Fylom</a></li>
<li><a href="https://www.emergentmind.com/topics/vector-based-retrieval-systems">Vector-Based Retrieval Systems - emergentmind.com</a></li>
<li><a href="https://gtrsocials.com/social-media-knowledge-hub/dwell-time">Dwell Time: Capture Attention to Boost Social Media Reach</a></li>

</ul>
</details>

**标签**: `#recommendation-systems`, `#X/Twitter`, `#ranking-algorithms`, `#user-engagement`, `#social-media`

---

<a id="item-7"></a>
## [工信部收紧准入规则，防范不合理创新汽车设计进入市场](https://m.chinanews.com/wap/detail/chs/zw/10717890.shtml) ⭐️ 6.0/10

10 月 20 日，中国工业和信息化部表示将坚决防范不合理创新设计和未经充分研发测试验证的汽车产品进入市场，总工程师王卫明在发布会上称，对未按要求申报、测试验证不充分的产品不予准入。通知要求将隐藏式门把手、电吸门、虚拟操纵件等创新设计纳入准入管理，电吸门必须具备防夹功能，禁止行驶中使用零重力座椅、旋转座椅等，并将 22 项推荐性标准升级为强制性标准，可靠性测试里程不低于 3 万公里。 这是全球较早将隐藏式门把手、电吸门、零重力座椅等电动车时代热门设计当作安全隐患而非卖点来监管的举措之一，而把 22 项推荐性标准转为强制性标准，将直接改变所有在华销售车企的车型准入要求。由于隐藏式门把手已成为大量新能源车的标配，新规将迫使车企重新设计、增加成本与合规工作量，并可能为其他市场的监管者提供范本。 新规采取的是准入管理而非对相关设计的一刀切禁止：隐藏式门把手、电吸门、虚拟操纵件仍可使用，但必须按要求申报并通过验证，电吸门还须能检测并释放夹持物。可靠性验证里程不得低于 3 万公里，而 22 项标准由 GB/T（推荐性）转为 GB（强制性），依据《标准化法》具备法律强制力，不合规车型将无法取得上市销售所需的公告准入。

telegram · zaihuapd · 10月20日 12:48

**背景**: 中国汽车标准体系分为强制性的 GB 标准和推荐性的 GB/T 标准：前者覆盖安全、排放、节能、防盗等要求，是实施强制认证和公告管理的依据；后者主要作为质量与采购参考，不能单独用于否决车型准入。隐藏式门把手在国内销量靠前的新能源车型中渗透率约六成，但因在碰撞、断电或严寒结冰时可能无法弹出而饱受诟病；零重力座椅和旋转座椅则让乘员处于大角度后仰姿态，超出传统安全带与安全气囊的保护设计范围。工信部此次把这些分散的担忧打包进了统一的准入管理框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.21jingji.com/article/20260204/herald/88f713cb444da00b2c7b38b9e21b58f1.html">汽车帮热评： 全 球首禁！ 工信部开始整顿 全 隐 藏 式 门 把 手 - 21经济网</a></li>
<li><a href="https://www.toutiao.com/article/7652251570758877732/">零重力座椅有“新规” 把“躺平”关进安全的笼子 - 今日头条</a></li>
<li><a href="https://www.sohu.com/a/943644462_122413646">我国的强制性标准和推荐性标准是如何划分的？</a></li>

</ul>
</details>

**标签**: `#automotive safety`, `#regulation`, `#vehicle design`, `#MIIT`, `#standards`

---