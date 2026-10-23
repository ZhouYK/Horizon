---
layout: default
title: "Horizon Summary: 2026-10-23 (ZH)"
date: 2026-10-23 23:03:20 +0000
lang: zh
report: default
---

> 从 163 条内容中筛选出 5 条重要资讯。

---

1. [Kimi 发布 K3.1-Pro：三万亿参数开放权重模型，支持百万级上下文](#item-1) ⭐️ 8.0/10
2. [字节跳动火山引擎发布 Seedance 2.5 4K 模型，面向大荧幕场景](#item-2) ⭐️ 7.0/10
3. [国办发文：减缓 AI 应用就业替代影响](#item-3) ⭐️ 7.0/10
4. [PHP 基金会建议暂时禁用 session.upload\_progress 以防范 RCE 漏洞](#item-4) ⭐️ 7.0/10
5. [瑞典政府办公室封禁 ChatGPT 与 Claude](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Kimi 发布 K3.1-Pro：三万亿参数开放权重模型，支持百万级上下文](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 8.0/10

Kimi（月之暗面）正式发布 K3.1-Pro，这是 K3.1 系列的首款模型，定位为其目前最强的三万亿参数级开放权重模型，支持 100 万 token 上下文，并同步推出速度为标准版 2—3 倍的 Highspeed 版本。模型现已接入 Kimi、Work、Code 和 API，完整权重计划于 2026 年 11 月 4 日前发布。 这是首个即将开放权重的模型在与闭源前沿模型的较量中取得如此接近的成绩：Artificial Analysis 给 K3.1-Pro 打出 55 分，超过 GPT-6 Astra、Claude Fable 5.1 和 Gemini 4 Argon（均为 53 分），仅次于 Claude Opus 5.5（58 分）。其定价为每百万输入 token 2 美元、每百万输出 token 10 美元，约为 Claude Opus 5.5 的一半，让接近前沿的能力进入自托管与成本敏感团队的视野。 官方数据显示，Terminal-Bench 4.0 得分 65.7%（高于 GPT-6 Astra 的 58.2%，略低于 Claude Opus 5.5 的 66.4%），内部长任务编程测试从 K3 的 55.95% 升至 61.2%，BenchCAD 工具辅助得分 92.7%；内部高难度测试中陈述级幻觉率从 23.4% 降至 8.3%，但原文明确强调这并不代表日常使用中的错误率。Highspeed 版本除缓存命中的输入 token 外价格翻倍，且权重尚未开放下载，目前只能通过 API 使用。

telegram · zaihuapd · 10月23日 17:14

**背景**: “开放权重”指训练好的参数可供下载，但比开源更弱：训练代码与数据通常不公开，许可证还可能对商用或大规模使用设限，这一区别在 2026 年的旗舰模型发布中格外重要。Terminal-Bench 4.0 是由 Laude Institute 及斯坦福相关贡献者推出的智能体编程基准，其 66 项任务在真实终端环境中执行软件、科学和运维工作。BenchCAD 衡量的是模型能否根据图纸或文字生成可执行的参数化 CAD 程序，而非仅仅描述几何形状。Artificial Analysis 是独立评测机构，使用自有的测试框架横向对比各模型，因此其 55 分被认为比厂商自报数据更具中立性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/terminalbench-4-0">Terminal-Bench 4.0 Benchmark - Artificial Analysis</a></li>
<li><a href="https://benchcad.com/">BenchCAD — a benchmark for programmatic CAD</a></li>
<li><a href="https://www.deai.org/news/open-weight-vs-open-source">Open - Weight vs Open - Source AI Models : The Difference That Bites...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Kimi`, `#open-weight models`, `#coding benchmarks`, `#AI release`

---

<a id="item-2"></a>
## [字节跳动火山引擎发布 Seedance 2.5 4K 模型，面向大荧幕场景](https://mp.weixin.qq.com/s/yUa8oh-IWfl5lDQzGSKWeg) ⭐️ 7.0/10

字节跳动旗下火山引擎正式发布 Seedance 2.5 4K 模型，官方称其为 Seedance 系列中最强版本，并针对人物表情、细微动作与画面细节做了专项训练。模型新增 Draft 模式，可先用 480P 样片快速验证分镜，满意后再生成 4K 正片，同时支持 10-bit 色深。 这一发布推动生成式视频进一步走向专业影视制作流程——在影视场景中，色深、面部细节的细腻度以及“低成本预览到高质量成片”的工作流，比单纯的视频时长更重要。如果试用范围从目前少量企业客户逐步扩大，可能会改变影视工作室制作分镜与预可视化的方式。 10-bit 色深可带来更平滑的色彩过渡，并在出现色彩断层前为调色保留更多空间，这是 HDR 与电影级后期的基本要求。目前模型仅面向部分企业客户试用，官方并未公布定价、具体分辨率与帧率规格，也未说明是否会开放公共 API。

telegram · zaihuapd · 10月23日 08:27

**背景**: Seedance 是字节跳动 Seed 团队推出的生成式视频模型系列，Seedance 2.5 被定位为新一代音视频联合生成模型，面向 30 秒级叙事，并具备参考控制与编辑能力。火山引擎则是字节跳动面向企业的“云+AI”服务平台，也是这些模型触达商业客户的渠道。色深指每个像素每个色彩通道用多少比特来记录：8-bit 是 SDR 的基准，10-bit 是 HDR 的基准并越来越多用于专业摄像机与调色流程，12-bit 则是电影与杜比视界的更高规格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/seedance2_5">Seedance 2.5 - seed.bytedance.com</a></li>
<li><a href="https://aicatalog.app/tools/bytedance-volcengine/">ByteDance Volcengine ( 火 山 引 擎 ) Review, Pricing... | AI Catalog</a></li>
<li><a href="https://filmdaft.com/what-is-bit-depth-definition-8-bit-vs-10-bit-vs-12-bit/">Bit Depth | Definition and 8-Bit vs 10-Bit vs 12-Bit Video ...</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#ByteDance`, `#Seedance`, `#generative AI`, `#4K video`

---

<a id="item-3"></a>
## [国办发文：减缓 AI 应用就业替代影响](https://mp.weixin.qq.com/s/St8URoMYcV-voM7kLAK3Bw) ⭐️ 7.0/10

国务院办公厅印发《关于适应人工智能技术发展助力构建就业友好型发展方式的意见》，明确提出要减缓人工智能应用对就业的替代影响。文件要求优先在劳动力紧缺、环境高危等岗位推广 AI，同时稳慎把握其在劳动密集型行业应用的范围、力度和节奏。 这是中国较早将 AI 对劳动力市场的冲击作为治理议题、而非单纯产业竞争力议题的国家级政策文件，意味着 AI 在制造、物流、服务等行业的扩散可能面临节奏把控式的柔性审视。这将影响大规模部署自动化的企业、制定就业政策的地方政府，以及劳动密集型行业中的大量劳动者。 文件鼓励企业探索建立&quot;失业缓冲期&quot;制度，提前告知受影响劳动者，并为其提供转型转岗和再就业支持。文件将 AI 推广设定为有条件的——与劳动力紧缺和高危岗位挂钩——而非无差别的普及目标。

telegram · zaihuapd · 10月23日 12:54

**背景**: 中国一直在制造业和公共服务领域大力推进&quot;人工智能+&quot;的产业落地，但制造业装配、物流、客服等劳动密集型行业吸纳了大量就业人口。自动化和生成式 AI 工具在这些领域的快速部署，引发了人们对大规模失业和社会稳定的担忧。中国的就业政策历来以&quot;稳就业&quot;为优先，这份文件将这一逻辑延伸到 AI 应用上，要求监管部门和企业在部署速度与劳动力市场吸纳能力之间保持协调。

**标签**: `#AI policy`, `#employment`, `#China regulation`, `#labor market`, `#AI adoption`

---

<a id="item-4"></a>
## [PHP 基金会建议暂时禁用 session.upload\_progress 以防范 RCE 漏洞](https://x.com/ThePHPF/status/2113580383875019242) ⭐️ 7.0/10

PHP 基金会建议用户在下一个 PHP 版本发布之前，将 session.upload\_progress.enabled 设置为 0，以缓解编号为 CVE-2026-115560 的远程代码执行（RCE）漏洞。据称只有当应用在运行时把非默认的 serialize\_handler 切换为“php”时才可能受到影响。 这是一个由 PHP 基金会自身披露的远程代码执行类漏洞，因此任何在运行时改变会话序列化方式的应用都需要立即处置，而不能干等下一个补丁版本。该临时建议只需修改配置、无需升级 PHP，对受影响部署而言是一项成本很低但价值很高的缓解措施。 该风险取决于上传进度功能与旧式“php”会话序列化器的组合使用，因此默认配置未必存在漏洞，影响面被描述为相对有限。基金会此前也曾因 CVE-2026-109619 建议保持该功能处于禁用状态，说明上传进度相关处理代码中可能存在反复出现的问题模式。

telegram · zaihuapd · 10月23日 13:46

**背景**: 当 session.upload\_progress.enabled 开启时，PHP 会把正在进行中的文件上传信息写入用户会话，页面即可通过单独的 XHR 请求轮询上传进度。PHP 会话可以由不同的处理器序列化，包括 php、php\_binary 和 php\_serialize，它们的存储格式各不相同，其中 php 处理器以“键名\|serialize\(值\)”的形式存储数据。以往的 PHP 安全研究表明，序列化格式混用，或把攻击者可控的数据写入会话文件，可以与本地文件包含（LFI）或对象注入利用链结合，从而实现代码执行，这正是此类漏洞通往 RCE 的经典路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.php.net/manual/en/session.upload-progress.php">PHP: Session Upload Progress - Manual</a></li>
<li><a href="https://www.cnblogs.com/hf99/p/9746038.html">关于php的session.serialize_handler的问题 - HF9 - 博客园 php session序列化,深入解析PHP中SESSION反序列化机制 PHP反序列化基础之session反序列化 - 赟希 - 博客园 PHP Session反序列化学习-腾讯云开发者社区-腾讯云 PHP Session 序列化机制及其引发的安全漏洞 | FunVerse Log PHP Session反序列化学习-腾讯云开发者社区-腾讯云</a></li>
<li><a href="https://mrxn.net/jswz/php-session-upload_progress-rce-fixes-ways.html">PHP “php2shell”（CVE-2026-109618/109619）：从 session.upload ...</a></li>

</ul>
</details>

**标签**: `#PHP`, `#security`, `#CVE`, `#RCE`, `#vulnerability-disclosure`

---

<a id="item-5"></a>
## [瑞典政府办公室封禁 ChatGPT 与 Claude](https://www.sverigesradio.se/artikel/chat-gpt-och-claude-forbjuder-regeringskansliet) ⭐️ 6.0/10

瑞典政府办公室（Regeringskansliet）宣布从下周一起在员工工作电脑上封禁 ChatGPT 和 Claude，要求员工改用包括微软 Copilot 在内的已批准 AI 工具。该机构数字化主管在内部网站上表示，使用未签订合约的 AI 服务可能危及信息安全。 此举使瑞典中央政府行政机构加入了越来越多限制未经批准生成式 AI 服务的公共部门行列，表明官方 AI 政策正从鼓励尝试转向以采购合规和数据保护为核心。这可能促使更多瑞典机构乃至欧洲公共部门统一采用经过审核、有合同保障的工具。 此次封禁是在此前限制 DeepSeek 之后作出的，瑞典税务局和国家机构事务局（SiS）已实施类似禁令，而瑞典执行局（Kronofogden）正在研究是否跟进。部分员工仍可通过自研平台访问 ChatGPT 和 Claude。

telegram · zaihuapd · 10月23日 14:11

**背景**: 瑞典政府办公室（Regeringskansliet）是支撑首相与内阁大臣施政的政府机构联合体。处理敏感或机密信息的公共机构越来越担心，面向消费者的 AI 聊天机器人会在缺乏合同保障的情况下把数据存储和处理在境外服务器上，因此这些机构更青睐微软 Copilot 等附带正式数据处理协议的企业级工具。Claude 是 Anthropic 开发的大语言模型系列，ChatGPT 是 OpenAI 的聊天机器人，而 DeepSeek 是一家中国 AI 公司，其开放权重模型已在多个欧洲政府中受到审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude (AI)</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#ChatGPT`, `#Claude`, `#data security`, `#public sector`

---