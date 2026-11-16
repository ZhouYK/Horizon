---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16 23:03:48 +0000
lang: zh
report: default
---

> 从 179 条内容中筛选出 7 条重要资讯。

---

1. [阿里发布 Qwen4-Max：2.4 万亿参数稀疏 MoE 旗舰，支持百万级上下文](#item-1) ⭐️ 8.0/10
2. [美国将 AI 芯片出口管制延伸至远程云端访问](#item-2) ⭐️ 8.0/10
3. [腾讯混元发布 Hy4 flash：224B 多模态 MoE，主打日常任务性价比](#item-3) ⭐️ 7.0/10
4. [亚马逊称 AI 代理窃取 API 密钥为自身调用大模型“自筹资金”](#item-4) ⭐️ 7.0/10
5. [山东大学团队称首次条件性证明哥德巴赫猜想](#item-5) ⭐️ 7.0/10
6. [DeepSeek 以算力不足为由对 App 与网页版实施限额](#item-6) ⭐️ 6.0/10
7. [Grok 文本水印在 API 中改为默认关闭](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [阿里发布 Qwen4-Max：2.4 万亿参数稀疏 MoE 旗舰，支持百万级上下文](https://mp.weixin.qq.com/s/pJUt0xwD6H-WMyzd8TjZaQ) ⭐️ 8.0/10

阿里通义千问团队正式推出新一代旗舰模型 Qwen4-Max，采用全新稀疏 MoE 架构，总参数高达 2.4 万亿，原生支持视觉理解与百万 Token 长上下文。官方称其单任务平均费用从 26.58 元降至 11.16 元，降幅近 58%，Token 消耗也减少近 50%，API 定价同步下调。 2.4 万亿参数规模叠加显著降低的单任务成本，抬高了前沿大模型的价格竞争门槛；而后续将开源小尺寸 Qwen4 模型的承诺，也为开源社区提供了可预期的路线图。运行长上下文、编程与智能体任务的企业用户将从成本与上下文的双重提升中获益最多。 目前 Qwen4-Max 仍是仅通过 API 提供的闭源模型，后续较小规模的 Qwen4 系列被表述为“公开模型权重”，即权重可下载，但训练代码与数据大概率不会公开，与完全开源的模型仍有区别。团队还强调其前端编程能力在 Code Arena 人工盲测榜单中位居全球前列，并支持工具调用与分阶段的长程任务执行。

telegram · zaihuapd · 11月16日 02:52

**背景**: 混合专家（MoE）架构把模型拆分成众多专门的子网络（即“专家”），每个 Token 只被路由到其中少数几个，因此总参数量可以做得极大，而单 Token 计算量仍保持可控——这正是“稀疏”的含义。Code Arena 这类榜单依靠人类在真实编程任务上的盲测两两对比投票来排名，而非固定题库，因此厂商常以此作为实际编程能力的佐证。此外还需区分“开放权重”与“开源”：开放权重模型允许下载、运行和微调已训练的权重，但训练数据与训练代码往往并不公开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://www.llmcodearena.com/top-models">CodeArena – Which LLM codes best?</a></li>
<li><a href="https://www.promptquorum.com/local-llms/open-weight-vs-open-source-ai-models">Open Weight vs Open Source AI Models 2026: Key Differences</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Qwen`, `#MoE`, `#open-weights`, `#model-release`

---

<a id="item-2"></a>
## [美国将 AI 芯片出口管制延伸至远程云端访问](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

2026 年 11 月 16 日，美国商务部工业与安全局（BIS）发布临时最终规则，将先进 AI 芯片与服务器的出口管制延伸至远程访问，使境外实体无法再通过租用第三国数据中心的算力来绕开限制。该规则由财政部和国家安全委员会主导起草，同时要求向印度尼西亚、马来西亚、新加坡、泰国和巴西再出口先进 AI 芯片须申请许可。 这堵住了美国半导体出口管制中最重要的剩余漏洞：中国企业此前一直在东南亚等地租用数据中心算力，而不是直接购买芯片。这意味着云服务商、数据中心运营商和跨国 AI 企业如今必须核查算力的最终使用者，从而在全球 AI 基础设施规划中引入许可障碍与合规风险。 该规则属于 BIS 的临时最终规则，覆盖其所谓的先进“超级智能”（SI）芯片与服务器，重点是打击中国内地和澳门等受限地区实体通过租用云端算法规避管制的做法。由于是临时最终规则，它在 BIS 继续征求意见期间即已生效，因此许可范围与执行细节仍可能调整。

telegram · zaihuapd · 11月16日 14:44

**背景**: 美国的出口管制依据《出口管理条例》，限制哪些国家和企业可以购买先进的美国 AI 加速器，其中中国内地和澳门被列入限制最严格的类别。此前这些规则只管硬件的实体运输，因而留下缺口：受限实体仍可通过在不受限国家的数据中心远程租用算力，合法使用同样的芯片。新规出台前，英伟达的中国业务正受到强烈的政治审视，外界也担心受限算力正通过新加坡、马来西亚等枢纽被间接获取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology">www.bis.gov</a></li>
<li><a href="https://techcrunch.com/2026/11/16/us-tightens-ai-chip-export-controls-to-deter-chinese-companies-from-accessing-compute-remotely/">US tightens AI chip export controls to deter Chinese ...</a></li>
<li><a href="https://wccftech.com/the-u-s-shuts-chinas-access-to-advanced-chips-via-singapore-brazil-indonesia-malaysia-and-thailand-as-scott-bessent-gives-nvidia-10-days-to-show-it-did-not-goose-its-revenues/">The U.S. Shuts China&#x27;s Access To Advanced Chips Via Singapore...</a></li>

</ul>
</details>

**标签**: `#export-controls`, `#AI-chips`, `#policy`, `#semiconductors`, `#geopolitics`

---

<a id="item-3"></a>
## [腾讯混元发布 Hy4 flash：224B 多模态 MoE，主打日常任务性价比](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

腾讯混元于 11 月 16 日正式发布 Hy4 flash，这是一款多模态混合专家（MoE）模型，总参数 224B（其中 64B 为 Engram 参数），每 Token 仅激活 12B，支持 1M 上下文。其 API 定价为每百万 Token 输入 0.5 元、输出 2 元，命中缓存时输入仅需 0.02 元；官方称 WorkIndex 单任务成本为 Hy4 preview 的 1/13、Hy4 的 1/20，并计划开源。 极低的单 Token 价格叠加 1M 上下文与多模态输入，使 Hy4 flash 非常适合高频的日常智能体与办公场景，也将进一步加剧国内模型厂商的价格竞争。若官方承诺的开源落地，开源权重生态还将获得一个以成本效率而非跑分为核心目标的大规模稀疏 MoE 模型。 成本下降来自端到端优化：混合注意力、LatentMoE 架构以及预训练阶段的 Engram，使 KV 缓存体积分别约为 Hy3 的 1/24、Hy4 的 1/6。该模型已在腾讯云 TokenHub、WorkBuddy、元宝、企业微信、QQ、ima、Marvis 上线，并将登陆 OpenRouter；11 月 30 日前 WorkBuddy 限免、API 五折，不过除自研的 WorkIndex 指标外，腾讯并未公布独立的第三方评测数据。

telegram · zaihuapd · 11月16日 07:17

**背景**: 混合专家（MoE）模型把网络拆分成众多专家子网络，每个 Token 只路由到其中少数几个，因此总参数量可以很大而单 Token 计算量保持较小——这正是 224B 总参数、12B 激活参数的由来。LatentMoE 是一种针对推理时内存带宽与通信瓶颈进行优化的 MoE 变体，目标是在单位 FLOP 和单位参数下获得更高精度。Engram 指一种额外加入的、类似记忆的参数表，用于把事实性知识模式与稠密 Transformer 权重分开存储。KV 缓存是解码阶段复用上文所需的键值状态，压缩它对于低成本地提供 1M 长上下文服务至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/latentmoe">LatentMoE : Efficient Latent Mixture of Experts</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Tencent Hunyuan`, `#MoE`, `#multimodal`, `#API pricing`

---

<a id="item-4"></a>
## [亚马逊称 AI 代理窃取 API 密钥为自身调用大模型“自筹资金”](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

亚马逊威胁情报团队报告称，攻击者利用开源自主渗透测试框架 Artex 驱动 AI 代理，扫描 LiteLLM、One API、Dify 等暴露在公网的 AI 应用，窃取其中保存的上游模型供应商 API 密钥，验证后将可用密钥汇入共享池，用于支付后续的大模型调用费用。该活动自 2026 年 10 月 3 日持续至 11 月 5 日，最终因 AWS 的 MadPot 诱饵网络捕获了这些代理自身的活动记录而被阻断。 这是目前少数被公开记录的真实案例之一，展示了“闭环式”代理攻击经济：被盗凭证直接为攻击者自身的算力开销买单，从而消除了大规模 AI 驱动入侵的一大成本障碍。这提醒所有在公网自建 LLM 网关或代理服务的组织需要警惕，同时也表明攻击工具正在与 AI 代理框架融合。 亚马逊仅以“中等信心”将该行动归因于一个与中国相关的威胁组织，并指出并非所有被列入目标清单的系统都真的失陷，同时表示已通知可能受影响的 AWS 客户。Artex 的设计是把多个代理串成流水线：一个代理生成候选攻击手法，另一个代理充当严格评分者来验证输出，这种模式提升了代理攻击的可靠性但并非万无一失；目前公开的技术细节有限，且主要来自亚马逊自身的遥测数据。

telegram · zaihuapd · 11月16日 13:00

**背景**: Artex 是一个托管在 GitHub 上的开源（Go + Next.js，AGPL-3.0）多代理 LLM 渗透测试系统，通过串联多个代理来规划任务、调用工具并跨资产追踪发现结果。LiteLLM、Dify 和 One API 都是自托管的 LLM 网关，内部保存着 OpenAI、Anthropic 等上游供应商的 API 密钥，因此一旦实例暴露在公网且存在默认口令或泄露的密钥，攻击者就能拿到可用密钥并刷出高额账单。MadPot 是 AWS 长期运行的蜜罐与威胁情报系统，它向攻击者呈现诱饵服务，在不暴露真实客户负载的前提下记录其探测和滥用行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/">Amazon Threat Intelligence observes threat actors running ...</a></li>
<li><a href="https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html">Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify ...</a></li>
<li><a href="https://opensourcedex.com/tool/artex">ARTEX : Open Source AI Security &amp; Privacy — 2.1K on GitHub</a></li>

</ul>
</details>

**标签**: `#AI security`, `#cybercrime`, `#API key theft`, `#cloud security`, `#threat intelligence`

---

<a id="item-5"></a>
## [山东大学团队称首次条件性证明哥德巴赫猜想](https://mrc.sdu.edu.cn/info/1018/2193.htm) ⭐️ 7.0/10

山东大学李嘉民、刘建亚在论文中提出，在狄利克雷 L 函数广义黎曼猜想成立并满足两种附加谱假设之一的条件下，所有充分大的偶数都可写成两个素数之和，且两素数位于该偶数的三分之一至三分之二之间。作者称这是首个覆盖所有充分大偶数的二元哥德巴赫猜想条件性证明。 若经核实，这将是首个覆盖所有充分大偶数的二元哥德巴赫猜想条件性证明路径，而该问题近三个世纪以来一直未获无条件解决；论文还可能开辟经典筛法和圆法之外的新方法。但由于所依赖的假设仍未证明，这项目前只能视为有待同行评审的高价值声明，而非已确立的定理。 作者强调，单靠狄利克雷 L 函数的广义黎曼猜想并不足以推出结论，还必须假设两种附加谱假设之一，因此该证明并非无条件证明。论文称其方法不同于经典筛法和圆法，但目前尚未经过同行评审。

telegram · zaihuapd · 11月16日 16:01

**背景**: 哥德巴赫猜想断言每个大于 2 的偶数都可写成两个素数之和，其二元形式至今仍未解决。狄利克雷 L 函数的广义黎曼猜想是关于这类 L 函数零点位置的深远假设，可类比黎曼猜想，本身也未被证明。研究加性素数问题的经典工具包括筛法（用于估计素数模式）和 Hardy–Littlewood 圆法（通过素数上的指数和分析），而该论文称其方法不同于这两者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sieve_theory">Sieve theory - Wikipedia</a></li>
<li><a href="https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf">Multiplicative Number Theory II</a></li>
<li><a href="https://english.imr.cas.cn/research/researchprogress/202608/t20260818_1188023.html">Scientists Prove Generalized Riemann Hypothesis via Competing...</a></li>

</ul>
</details>

**标签**: `#Goldbach conjecture`, `#number theory`, `#analytic number theory`, `#conditional proof`, `#Riemann hypothesis`

---

<a id="item-6"></a>
## [DeepSeek 以算力不足为由对 App 与网页版实施限额](https://www.chinastarmarket.cn/detail/2535076) ⭐️ 6.0/10

据用户反馈及《科创板日报》报道，DeepSeek 以其算力不足为由，对 App 和网页版对话开始实施限额使用。具体措施包括：超过 7 天不活跃的长对话不再保留、单次输入文字上限缩短至约 4 万字，同时每日对话额度也设了上限，用满后会提示「因服务器繁忙，使用额度已达上限」。 这是中国头部大模型厂商少有的公开承认：当前制约面向消费者的服务的关键因素，已从模型能力转向推理算力。这说明大模型市场的竞争重心正在向服务成本与 GPU 供给能力转移，同时也直接影响那些依赖 DeepSeek 处理长文档或进行长时间对话的免费用户。 这些限制针对的是免费 App 与网页版，而非 API 接口；4 万字的单次输入上限实际上限定了用户单轮可提交的上下文长度，对长文档分析和代码审阅场景影响明显。7 天不活跃即不再保留对话，可减少服务端的会话历史存储压力，但官方并未说明每日额度的具体数值，也未说明付费用户是否豁免。

telegram · zaihuapd · 11月16日 04:30

**背景**: DeepSeek 是一家中国 AI 实验室，其模型（尤其是 R1 推理系列）被定位为性能对标 GPT-4 级别、而 API 价格却低得多。大语言模型不仅在训练阶段需要 GPU 算力，更关键的是推理阶段——即回答每一次用户提问的过程——也需要大量算力，而推理需求会随并发用户数和对话长度的增长而成倍上升。由于每多一点上下文长度、每多存一段会话都会占用显存与算力，在 GPU 供给紧张时，厂商往往通过限制输入长度、让会话过期、设置每日额度等方式来配额供给，而不是让所有用户的体验一起变差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnblogs.com/anai/p/18718383">人人都看得懂的 DeepSeek 入门科普 - AI 粉嫩特攻队 - 博客园</a></li>
<li><a href="https://blog.csdn.net/leafff123/article/details/154486865">一文了解-大语言模型训练 vs 推理：硬件算力需求数据对比_推理和训练...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1933527124200915888">为什么大语言模型都有上下文限制？ - 知乎</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM infrastructure`, `#compute scarcity`, `#AI product policy`, `#China AI industry`

---

<a id="item-7"></a>
## [Grok 文本水印在 API 中改为默认关闭](https://x.com/mark_k/status/2121975392554619298) ⭐️ 6.0/10

Grok 的隐形文本水印现已在 xAI 的 API 中默认关闭，马斯克本人确认了这一变化，并表示只有在法律强制要求或用户主动要求时才会开启水印。这意味着基于 Grok 构建应用的开发者默认会得到不带水印的输出，除非他们主动开启，或所处司法辖区强制要求对 AI 生成内容进行标注。 这一反转之所以重要，是因为 xAI 此前曾宣布自 11 月 7 日起，七个 Grok 模型的 API 输出将默认携带隐形水印以符合欧盟《人工智能法案》。如今默认值被翻转，合规责任实际上转移到了开发者和部署方身上。这也加剧了业界在 AI 内容溯源问题上的分化：一些厂商默认加水印，另一些则把它当作可选项。 根据此前的报道，Grok 的水印是在生成过程中嵌入到 token 选择里的，因此复制或轻度清洗文本都无法将其去除，而且最初的推行不需要开发者修改 API 请求。新默认值带来的实际后果是：是否开启、如何记录说明、以及所在地区的法律合规审查，都从平台自动处理变成了开发者自己的责任。

telegram · zaihuapd · 11月16日 09:55

**背景**: AI 水印是一种对模型输出进行细微修改的技术，使内容日后能被识别为 AI 生成。对于文本而言，这通常是通过影响模型选择 token 的概率分布来实现的，因此这种信号在统计上可被检测，但对人类读者来说是不可见的。水印与文件层面的溯源元数据（例如 C2PA 标准）不同，后者会附带关于内容如何被创建或修改的签名信息。监管要求，尤其是欧盟《人工智能法案》的透明度义务，已促使多家主要模型厂商默认开启文本水印，这也是 xAI 最初在 11 月 7 日推出该功能时将其定位为合规措施的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tsnmedia.org/grok-api-text-watermark/">Grok API Watermark Goes On by Default Nov 7 | TSN</a></li>
<li><a href="https://www.nextfor.ai/news/grok-api-text-watermark-default">Grok API Invisible Watermark : What Changes on November 7</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_watermarking">AI watermarking - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI watermarking`, `#Grok`, `#API policy`, `#content provenance`, `#AI regulation`

---