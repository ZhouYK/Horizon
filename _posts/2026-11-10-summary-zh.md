---
layout: default
title: "Horizon Summary: 2026-11-10 (ZH)"
date: 2026-11-10 23:04:00 +0000
lang: zh
report: default
---

> 从 193 条内容中筛选出 11 条重要资讯。

---

1. [谷歌 DeepMind 公开开放最强模型 Gemini 4 Carbon，称霸 CursorBench 4.0](#item-1) ⭐️ 9.0/10
2. [Anthropic 拟募 693 亿美元的 IPO 文件被撤回](#item-2) ⭐️ 8.0/10
3. [Fireworks 遭新攻击，客户数据外泄](#item-3) ⭐️ 8.0/10
4. [Anthropic 改白名单制：中国大陆及港澳不在名单内，11 月 12 日生效](#item-4) ⭐️ 8.0/10
5. [OpenAI 部署“控制室”系统，35 秒内叫停高风险 AI 智能体任务](#item-5) ⭐️ 7.0/10
6. [阿里平头哥据称计划 2027 年港交所 IPO，拟募资 20 至 30 亿美元](#item-6) ⭐️ 7.0/10
7. [Claude Code 本地设置文件泄露 2,539 个真实凭据](#item-7) ⭐️ 7.0/10
8. [马斯克：Grok 4.8 预训练完成，进入强化学习阶段](#item-8) ⭐️ 7.0/10
9. [稀宇科技开源 MiniMax H3 Image，4K 图像生成进入十秒级](#item-9) ⭐️ 7.0/10
10. [苹果 Logic Pro 推出 49.99 美元 AI 用量包](#item-10) ⭐️ 6.0/10
11. [台积电 10 月营收达 5868.9 亿新台币，同比增长 59.7%](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [谷歌 DeepMind 公开开放最强模型 Gemini 4 Carbon，称霸 CursorBench 4.0](https://deepmind.google/models/model-cards/gemini-4-carbon/) ⭐️ 9.0/10

谷歌 DeepMind 正式面向公众发布新旗舰模型 Gemini 4 Carbon，主打网络安全、长时程智能体工作流，并覆盖复杂知识工作、软件工程与科学推理。官方称其在包括 CursorBench 4.0 在内的多项基准上排名第一，成本比次优外部模型低 2 倍以上；该模型已通过 Gemini API、Google AI Studio 与 Gemini for business 上线。 一款性能与对手持平甚至更强、价格却只有约一半的前沿模型，可能重塑运行编码智能体与长时程自主工作流的经济性，并在基准排名与单位 token 成本两方面同时向 Anthropic 和 OpenAI 施压。构建智能体式软件流水线的企业受益最大，因为 token 开销会随智能体循环的长度和重复次数成倍放大。 Gemini 4 Carbon 与 Gemini 4 Argon 同价：输入 2 美元/百万 token、输出 10 美元/百万 token；谷歌同时在 Antigravity 中预览 /swarm 多智能体协作模式。需要注意的是，本条消息源为简短摘要，未包含完整模型卡；而第三方榜单统计显示，它在 CursorBench 4.0 上对 Claude Fable 5.2 的领先幅度不足一个百分点，因此“排名第一”的说法优势相当微弱。

telegram · zaihuapd · 11月10日 15:48

**背景**: CursorBench 4.0 是由 Cursor（Anysphere）维护的智能体式编程基准，题目取自真实的 Cursor 编程会话任务，并在 Cursor 的生产级智能体框架内评测，因此它衡量的是模型作为“编程智能体”而非聊天助手的表现。“长时程智能体工作流”指模型能够自主规划并执行多步操作——修改多个文件、调用工具、验证结果——而无需人工介入。Antigravity 是谷歌的智能体式开发环境，其中 /swarm 一类功能可让多个智能体分工处理多文件重构等大型任务。大模型按每百万 token 计价，而智能体在一次任务中会反复循环调用，成本会快速累积，因此 2 倍的价格差对智能体场景意义重大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://benchgen.com/benchmarks/cursor/cursorbench-4-0">CursorBench 4.0 — Benchgen</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/pricing">Gemini Developer API pricing | Gemini API | Google AI for Developers</a></li>
<li><a href="https://antigravity.google/docs/teamwork/">Teamwork agent teams (/teamwork) | Google Antigravity Docs</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#LLM Release`, `#Google DeepMind`, `#AI Agents`, `#Model Pricing`

---

<a id="item-2"></a>
## [Anthropic 拟募 693 亿美元的 IPO 文件被撤回](https://www.reuters.com/business/anthropic-aims-raise-up-693-billion-blockbuster-ipo-2026-11-10/) ⭐️ 8.0/10

Anthropic 向多家银行散发的证券文件显示，其计划以每股 70 至 80 美元发行约 8.67 亿股 A 类股，最高募资 693 亿美元。随后公司通过邮件称定价信息不准确，撤回了该文件，并表示将发布更新版本，同时拒绝置评。 若消息属实，这一募资规模将跻身史上最大 IPO 之列，并让 Anthropic 成为上市公司，使外部投资者得以直接押注这家领先的 AI 模型开发商。文件中提及的谷歌、英伟达、AMD、博通、美光、微软和台积电参与配售，说明 AI 芯片与云计算供应链将 Anthropic 的业务视为具有战略意义。 原文件还列出一项规模 260 亿美元的私募配售，按发行价由谷歌、英伟达、AMD、博通、美光、微软和台积电参与，路演预计于本周二启动。但由于公司自认定价信息不准确并撤回文件，发行股数、价格区间和募资总额均应视为尚未确认。

telegram · zaihuapd · 11月10日 06:25

**背景**: Anthropic 是一家 AI 研究公司，以大语言模型 Claude 系列著称，是 OpenAI 的主要竞争对手之一。IPO（首次公开发行）指私人公司向公众出售股份并在证券交易所上市的过程，描述发行条款的文件通常在路演前分发给银行和潜在投资者，而路演是管理层向投资者推介发行方案的市场推广行程。私募配售则是指在公开市场之外，向选定的机构投资者定向出售股份。

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#funding`, `#Reuters`

---

<a id="item-3"></a>
## [Fireworks 遭新攻击，客户数据外泄](https://finance.sina.com.cn/stock/usstock/c/2026-11-10/doc-iniyfzhx2605532.shtml) ⭐️ 8.0/10

Fireworks 确认遭遇新一轮黑客攻击，部分客户账单信息、模型权重和数据集外泄，目前正与 Palo Alto Networks 旗下 Unit 42 联合调查。Harvey 表示其客户数据未受影响，但其他客户和终端用户是否泄露仍不清楚。 此次泄露发生在许多公司依赖运行模型的主流 AI 推理平台上，而模型权重和数据集外泄对 AI 客户尤为敏感。据报道部分大客户正考虑迁移，这可能在一个至少 300 亿美元估值的融资计划启动之际对 Fireworks 的业务造成打击。 知情人士称，部分每年支付数百万美元的大客户正考虑迁移到其他供应商。Fireworks 的年化营收在今年 7 月已达到 10 亿美元，原计划本周启动新一轮融资，目标估值至少 300 亿美元。

telegram · zaihuapd · 11月10日 13:00

**背景**: Fireworks AI 是一家云推理和模型训练平台，由 Meta PyTorch 团队的七名工程师于 2022 年创立，CEO 为 Lin Qiao。模型权重是机器学习模型在训练过程中学到的数值参数；在大语言模型中，权重存储了从训练数据中学到的知识，因此属于有价值的知识产权。Unit 42 是 Palo Alto Networks 旗下的威胁研究与事件响应团队，企业常在遭遇严重网络攻击时邀请其参与调查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://siliconvalleyinvestclub.com/companies/fireworks-ai/">Fireworks AI — Company profile — Silicon Valley Investclub</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models ? | Analytics Vidhya</a></li>
<li><a href="https://www.paloaltonetworks.com/unit42/about">About Unit 42: Our Mission and Team - Palo Alto Networks</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#security breach`, `#data leakage`, `#Fireworks AI`, `#industry news`

---

<a id="item-4"></a>
## [Anthropic 改白名单制：中国大陆及港澳不在名单内，11 月 12 日生效](https://www.anthropic.com/legal/supported-regions) ⭐️ 8.0/10

Anthropic 发布新的《支持地区政策》，把产品可用范围改为白名单制：Claude.ai、Claude Code、Cowork、API，以及通过云平台和授权经销商提供的 Claude 模型，仅在名单所列的 185 个国家和地区可用，并于 11 月 12 日生效。中国大陆、香港、澳门均不在名单内，中国台湾则在名单之中。 这是一家头部 AI 实验室正式切断大片开发者市场的动作，被排除地区的工程师和企业若通过 API 或云市场构建在 Claude 模型之上，将失去受支持的访问渠道；跨国企业也必须先审查员工出差、实体注册地和股权结构，才能允许员工使用 Claude。这也说明 AI 厂商正在把访问控制收紧到传统出口管制清单之外。 三条禁止条款比名单本身更严格：人身处不支持地区时使用即属违规（包括支持地区公司员工出差期间），在不支持地区注册或设总部的实体及其人员无论身处何地均被禁止使用，被不支持地区主体直接或间接多数持股或控制的公司同样在限制范围内。值得注意的是，该名单并非照抄美国制裁清单——伊拉克、利比亚、索马里、苏丹、巴勒斯坦等国在列；属地随母国计入，例如波多黎各按美国处理，而乌克兰则排除克里米亚、顿涅茨克、赫尔松、卢甘斯克、扎波罗热五个地区。

telegram · zaihuapd · 11月10日 13:44

**背景**: Anthropic 是 Claude 系列模型背后的 AI 公司，用户可通过 claude.ai 网页聊天、在终端中运行的智能编码工具 Claude Code、面向办公与桌面任务的 AI 助手 Cowork，以及开发者 API 来使用这些模型。此前可用范围通常以“不支持或受制裁国家”的方式来描述，新政策则把逻辑反过来：只有明确列入名单的地区才受支持。这类地区条款之所以重要，是因为如今访问控制越来越多地通过账号核查和 IP 地理位置来实现，而不仅仅依靠合同约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/legal/supported-regions">Supported Regions Policy - Anthropic</a></li>
<li><a href="https://www.nodeseek.com/post-1044612-1">Anthropic 改白名单制：中国大陆及港澳不在名单内，11 月 12 日生效</a></li>
<li><a href="https://www.panewslab.com/zh/articles/01a1c5e8-ab66-7155-a601-cc8dbbbede93">Anthropic地区新白名单11月12日生效，未支持地区控股企业禁用Claude |...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#Anthropic`, `#Claude`, `#compliance`, `#geo-restrictions`

---

<a id="item-5"></a>
## [OpenAI 部署“控制室”系统，35 秒内叫停高风险 AI 智能体任务](https://interestingengineering.com/ai-robotics/openai-control-room-35-second-model-shutdown) ⭐️ 7.0/10

OpenAI 已在其研究基础设施内部部署名为“控制室”（Control Room）的系统，可在收到停止指令后最迟 35 秒内阻止有风险的 AI 智能体任务继续获取模型输出。所有训练、评估和数据处理任务都带有唯一任务 ID，推理引擎在处理请求前会先确认该任务是否仍被授权继续。 这是头部实验室首次就“如何真正在运行中切断智能体任务”给出具体且技术细节充分的安全工程披露，而不只是事后检测问题。随着自主智能体能力增强并被赋予工具调用权限，一套快速可靠的“急停开关”正在成为内部治理与外部监管的基本要求。 拦截发生在推理引擎处理请求之前，因此即使系统其他部分出现故障，被叫停的任务也拿不到输出；此外，所有前沿强化学习任务还配备独立的模型监控器，用于发现可疑行为并报警。OpenAI 承认授权请求的缓存仍会带来延迟，并表示正努力将这部分开销降至 0。

telegram · zaihuapd · 11月10日 05:47

**背景**: AI 智能体是能够在多个步骤中自主行动的模型——调用工具、编写并执行代码、浏览网页——这意味着一次行为异常的运行可能以超过人类反应速度造成损害。传统的安全手段主要聚焦于过滤单次请求的输入输出，而“急停开关”针对的是整个任务，因此需要在训练、评估与推理服务等基础设施之间追踪工作负载身份。与之配套的，是 OpenAI 用于发现前沿模型失准行为的分层监控体系，目标是在事件升级前完成干预。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/control-room/">Control Room : A central system to track and stop model... | OpenAI</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-control-room-35-second-model-shutdown">OpenAI launches Control Room with a 35-second kill switch for agents</a></li>
<li><a href="https://openai.com/index/how-we-detect-frontier-model-misalignment/">How we detect frontier model misalignment | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#AI agents`, `#infrastructure`, `#model monitoring`

---

<a id="item-6"></a>
## [阿里平头哥据称计划 2027 年港交所 IPO，拟募资 20 至 30 亿美元](https://weibo.com/1642634100/RqIoQv9m9) ⭐️ 7.0/10

据新浪科技援引微博消息，阿里巴巴旗下芯片子公司平头哥计划于 2027 年在香港交易所 IPO，拟募资至少 20 亿至 30 亿美元（约合 156 亿至 234 亿港元）。阿里巴巴方面目前尚未官方确认该消息。 若消息属实，这将成为近年来港股市场规模最大的半导体 IPO 之一，并为阿里巴巴的芯片业务提供公开市场融资渠道。同时，在半导体成为 AI 基础设施与技术自主核心的背景下，这笔 IPO 也将检验投资者对中国半导体资产的兴趣。 阿里巴巴 CEO 吴泳铭在 2026 财年 Q3 财报电话会上表示，平头哥“已经成功商业化”，芯片出货量超过 47 万片，年化营收规模超过 100 亿元人民币。该 IPO 消息仍未获官方确认，且 2027 年的时间表意味着募资规模、估值和上市时机仍可能变化。

telegram · zaihuapd · 11月10日 08:31

**背景**: 平头哥半导体成立于 2018 年，是阿里巴巴集团的全资芯片业务主体，由阿里收购的中天微系统与达摩院芯片团队整合而成。其产品线涵盖玄铁 RISC-V 处理器 IP、基于 Arm 架构的 5nm 倚天 710 服务器 CPU，以及含光 800 AI 推理芯片。这些产品支撑阿里云的数据中心布局，也反映了中国推动自研半导体的整体趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.t-head.cn/product?id=6">平头哥半导体</a></li>
<li><a href="https://www.ithome.com/0/581/322.htm">阿里巴巴 平 头 哥 发布自研 CPU 芯 片 倚 天 710：采用 5nm...</a></li>
<li><a href="http://www.hansenfluid.com/news/hangguang_800.htm">阿里云自研 AI 芯片主要包括平头哥 PPU和含光 800两大产品线，分别面...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#Alibaba`, `#T-Head`, `#IPO`, `#Hong Kong`

---

<a id="item-7"></a>
## [Claude Code 本地设置文件泄露 2,539 个真实凭据](https://www.ithome.com/1/024/888.htm) ⭐️ 7.0/10

安全公司 Apiiro 发现，1,994 个公开 GitHub 代码库中共暴露了 2,539 个真实凭据，涉及数据库密码、云服务密钥、API Token 和 SSH root 登录信息。问题根源在于 Claude Code 的“不再询问”授权机制：被批准的 Shell 命令会以明文原样写入 .claude/settings.local.json 等本地设置文件，若这些文件没有被 Git 忽略，凭据就会随提交一起进入公开仓库。Anthropic 表示正在研究防护措施，并考虑内置密钥扫描功能。 Claude Code 是目前使用最广泛的 AI 编程代理之一，这种把日常授权操作悄悄转化为已提交密钥的、工具特有的泄露路径，会让大量开发者及其所在组织面临风险。这也说明代理式工具会制造出全新的供应链暴露面，而传统的 .gitignore 习惯与代码评审流程根本无法覆盖。 已有超过 10 万份 Claude Code 本地设置文件被上传至公开仓库，其中约 1,100 份含有敏感信息；该问题早在 2025 年 8 月就已在 anthropics/claude-code 仓库的 issue \#5544 中被报告，请求对密钥进行脱敏或将其排除在允许列表之外。这并非可远程利用的漏洞，而是一种持久化设计选择带来的后果，因此受影响的用户必须轮换凭据并清理 Git 历史，而不仅仅是升级版本。

telegram · zaihuapd · 11月10日 11:20

**背景**: Claude Code 是 Anthropic 推出的命令行编程代理，可以在获得授权后于开发者本机执行 Shell 命令。为避免反复弹窗询问，它提供了“记住该命令”的选项，把已批准的指令写入项目级设置文件。由于开发者习惯将项目配置提交到 Git，任何嵌入在被记住命令中的凭据——例如传给 psql 的连接串或环境变量里的 Token——都会变成公开可读的信息。而传统密钥扫描工具和 .gitignore 规则通常只覆盖源码文件和 env 文件，并不针对代理自动生成的配置文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-code-settings-secret-leak-20261108/">Approved Once, Leaked Forever: Secrets in Claude Code ...</a></li>
<li><a href="https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github/">Claude Code is accidentally exposing secrets all over GitHub</a></li>
<li><a href="https://www.techspot.com/news/114500-claude-code-dont-ask-again-button-leaking-passwords.html">Claude Code&#x27;s &quot;don&#x27;t ask again&quot; button is leaking passwords ...</a></li>

</ul>
</details>

**标签**: `#security`, `#credential-leakage`, `#claude-code`, `#ai-coding-tools`, `#github`

---

<a id="item-8"></a>
## [马斯克：Grok 4.8 预训练完成，进入强化学习阶段](https://x.com/elonmusk/status/2120088070443655190) ⭐️ 7.0/10

马斯克宣布，xAI 的 Grok 4.8 已完成预训练，目前进入强化学习阶段，评测分数已开始上升。他还表示，团队弃用了 JAX 与 SGLang，用 C/C++ 从零重写了整个强化学习与推理栈，因此多花了一些时间，并计划本周晚些时候向 Bot 用户灰度发布。 这一表态既是 xAI 新模型的重要节点，也公开质疑了以 Python 为主流的标准机器学习工具链：放弃 JAX、SGLang 这类成熟框架、改用手写 C/C++ 是一次颇具争议的工程押注，其他实验室势必密切关注。若重写后的技术栈确实能在强化学习训练效率上取得优势，将为前沿模型开发中采用更底层、性能更可调的基础设施提供有力论据。 马斯克称 Grok 4.8 与 4.7“几乎没有相似之处”，但同时坦言目前还不算惊艳，只是基础已经打对。他未给出任何基准测试数据、架构细节或明确时间表，仅提到“本周晚些”向 Bot 用户灰度发布，因此这些说法仍无法验证。

telegram · zaihuapd · 11月10日 12:28

**背景**: 预训练是构建大语言模型过程中第一个、也是最耗费算力的阶段，模型在这一阶段从海量文本语料中学习通用规律；之后的强化学习阶段则用于强化推理能力并使输出与人类偏好对齐，常见方法包括 RLHF、PPO 和 DPO。JAX 是 Google 推出的 Python 库，面向高性能数值计算和大规模机器学习，在训练场景中被广泛使用。SGLang 是一个开源的大模型服务框架，以 RadixAttention 等加速推理的技术著称，正属于 xAI 声称已用自研 C/C++ 代码取代的那类优化推理引擎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JAX_%28software%29">JAX (software) - Wikipedia</a></li>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/sglang">SGLang · Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2509.16679v1">Reinforcement Learning Meets Large Language Models: A Survey ...</a></li>

</ul>
</details>

**标签**: `#xAI`, `#Grok`, `#reinforcement-learning`, `#LLM`, `#AI-industry-news`

---

<a id="item-9"></a>
## [稀宇科技开源 MiniMax H3 Image，4K 图像生成进入十秒级](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) ⭐️ 7.0/10

稀宇科技发布 MiniMax H3 Image 图像模型并开放权重，可在约 10 秒内生成 4096×4096（约 1600 万像素）的 4K 图像，支持文生图、最多 16 张参考图的多图参考以及图像编辑。官方同步推出 Highspeed 高速版本，称标准模式速度约为主流工具的 1.5 至 2 倍、高速模式达 3 至 4 倍；模型已上线 Hugging Face 与开放平台 API，并接入 MiniMax Code、海螺等产品。 在这一分辨率与速度下开放权重，意味着原本只能依赖闭源 API 的团队也能自建 4K、多图参考的生成能力，这对构建生成式图像流水线、设计工具以及电商与广告素材生产的开发者都很有价值。开源权重、托管 API 与激进的单图定价（4K 单张约 0.069 美元，发布首周优惠价约 0.034 美元）三项叠加，也会加剧国内外闭源图像模型面临的竞争压力。 该模型主打的能力是复杂指令理解、最多 16 张参考图的融合，以及原生 4K 下更精细的画面细节表现（而非先低分辨率再放大），标准模式 4K 输出约 0.069 美元一张，首周约 0.034 美元。此次发布更像是产品与研究层面的里程碑而非全新架构，公告本身给出的基准测试数据很少，因此其真实质量相对现有模型究竟如何，仍缺乏第三方验证。

telegram · zaihuapd · 11月10日 15:39

**背景**: 稀宇科技（MiniMax）是一家中国 AI 初创公司，以海螺（Hailuo）视频与图像生成产品以及自研大语言模型而知名。基于扩散的图像模型通过从随机噪声出发、反复去噪，逐步逼近文本提示所描述的图像；“开放权重”意味着训练好的参数被公开，其他人可以下载、自行部署并微调，而不只是调用托管 API。多图参考生成（用多张输入图片作为风格、主体或构图引导）已成为重要的差异化能力，因为它能让创作者在一批图片中保持角色与品牌素材的一致性。原生生成 4096×4096 分辨率非常消耗算力，因此约 10 秒的延迟以及更快的 Highspeed 版本才值得关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agihunt.info/story/1a1c13c35af29c2f7f2c85a0c71">MiniMax H 3 - Image ：从早期访问到 开 源发布 · AGI Hunt 专题</a></li>
<li><a href="https://lean.shengsuanyun.com/apidocs/hot/vyecfuqv7rgzuzbws86f78wvh-minimax-h3-image">MiniMax 发布 H 3 - Image 图像 模 型 并 开 放 权 重 - 胜算云 API 文档</a></li>
<li><a href="https://hailuoai.video/tools/minimax-h3">Hailuo AI Video &amp; Image Generator for Creators Online</a></li>

</ul>
</details>

**标签**: `#image-generation`, `#open-source-models`, `#diffusion-models`, `#multimodal`, `#MiniMax`

---

<a id="item-10"></a>
## [苹果 Logic Pro 推出 49.99 美元 AI 用量包](https://www.theverge.com/tech/1030084/apple-intelligence-usage-packs-ai-features-creator-studio-logic-pro) ⭐️ 6.0/10

苹果在 Logic Pro 中新增了“购买更多用量”选项，一次性售价 49.99 美元，使其成为首个对 Apple Intelligence 额外用量收费的应用。该用量包用于补充那些依赖 OpenAI 或 Gemini 等云端模型、设有额度上限的 AI 功能的配额，并预计本月把同样的模式扩展到 Pixelmator Pro 和 Final Cut Pro。 这是苹果首次为 Apple Intelligence 的使用单独定价，标志着从“AI 随设备免费附赠”转向对云端 AI 功能按用量计费。如果该模式推广到 Pixelmator Pro 和 Final Cut Pro，专业创作者将成为第一批为 AI 工作流按次付费的群体，而其他厂商也会密切关注用户对这种“应用之外再为 AI 付费”模式的反应。 该用量包仅限购买账户本人使用，未用完的额度可以逐月结转，但 12 个月后过期作废。这条消息来自 The Verge 的简短报道而非技术详解，因此诸如额度包具体包含多少额度、哪些具体功能会消耗额度等细节尚不清楚。

telegram · zaihuapd · 11月10日 01:53

**背景**: Apple Intelligence 是苹果 AI 功能的统一品牌，于 2024 年 6 月的 WWDC 上发布，并随 iOS 18、iPadOS 18 和 macOS Sequoia 一同提供；在 Mac 上它要求使用 Apple 芯片，不支持 Intel 机型。它结合了设备端处理与服务器端计算，包含写作工具、图像生成以及与 ChatGPT 的集成。由于部分能力依赖 OpenAI 或 Gemini 等第三方云端模型，每次请求都会产生实际的调用成本，这正是需要推出按量计费用量包、而无法完全免费开放的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri - Apple</a></li>

</ul>
</details>

**标签**: `#apple`, `#ai-pricing`, `#logic-pro`, `#apple-intelligence`, `#product-news`

---

<a id="item-11"></a>
## [台积电 10 月营收达 5868.9 亿新台币，同比增长 59.7%](https://pr.tsmc.com/chinese/news/3349) ⭐️ 6.0/10

台积电公布 10 月合并营收约 5868.9 亿新台币，较上月增长 14.7%，较去年同期大幅增长 59.7%。今年 1 至 10 月累计营收约 4 兆 4856 亿新台币，同比增长 43.3%。 作为全球最大的晶圆代工厂，台积电的月度营收是观察半导体需求的重要先行指标，尤其是 AI 加速器和先进制程芯片的需求。接近 60%的同比增速表明 AI 基础设施支出依然强劲，并持续传导至整条供应链。 该数据属于初步的月度营收披露，并非完整财报，因此没有按制程节点、平台或利润率进行的拆分。增长既受益于去年同期基数，也体现了环比动能，14.7%的月增幅说明增长在加速而非一次性冲高。

telegram · zaihuapd · 11月10日 08:07

**背景**: 台积电是一家纯晶圆代工厂，为苹果、英伟达、AMD、高通等公司代工其设计的芯片，因此其营收常被视为整个电子与计算需求的晴雨表。公司会在季度财报之前按月公布以新台币计的合并营收，投资者借此观察 3 纳米、5 纳米等先进制程的走势以及 AI 硬件需求的变化。

**标签**: `#TSMC`, `#semiconductors`, `#earnings`, `#AI hardware`, `#Taiwan`

---