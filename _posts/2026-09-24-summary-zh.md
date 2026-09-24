---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24 23:04:00 +0000
lang: zh
report: default
---

> 从 153 条内容中筛选出 6 条重要资讯。

---

1. [Anthropic 工程师称 Claude 写作变差：内容更像写给 AI 看](#item-1) ⭐️ 7.0/10
2. [OpenAI 称苹果 ChatGPT 集成表现不佳，合作出现裂痕](#item-2) ⭐️ 7.0/10
3. [OpenAI 发布心理健康基准 MentalHealthBench](#item-3) ⭐️ 7.0/10
4. [Claude Code 云会话正式上线，Pro/Max 用户可领最高 250 美元额度](#item-4) ⭐️ 6.0/10
5. [三大运营商暂停金融分期业务，“0 元购机”全面停办](#item-5) ⭐️ 6.0/10
6. [美国 ITC 对 DRAM 设备启动 337 调查](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 工程师称 Claude 写作变差：内容更像写给 AI 看](https://tech.ifeng.com/c/8wfFOVTfzvZ) ⭐️ 7.0/10

Anthropic 工程师杰克逊·克尼恩公开解释称，Claude 后续模型之所以写作风格退化，是因为强化学习的奖励机制更偏向数学、代码以及面向其他 AI 模型的技术解释，导致输出更像写给 AI 而非人类阅读。他表示问题根源在于奖励设计，模型需要增加对简洁易懂表达的奖励，并称 Claude Opus 5.5 已改善这种平衡，但尚不能确定是否超越 Opus 4.6。 这番表态罕见地由内部人士承认，外界广泛抱怨的“Claude 腔”退化并非偶发问题，而是奖励优化的直接副产物，这对所有用大模型写文章、写文档或产出面向客户内容的用户都至关重要。它也点出了整个行业的矛盾：当模型越来越依赖 AI 生成数据或可验证任务来训练和评估时，面向人类的写作质量可能在不知不觉中下滑。 克尼恩把强化学习奖励机制视为核心原因：数学和代码的答案可以被自动验证并打分，而优秀的文字表达很难稳定地量化奖励，于是模型被推向密集、技术化、便于机器阅读的输出。他指出 Opus 5.5 已在这些能力之间取得更好的平衡，但目前还不能确定它明显优于 Opus 4.6，相关改进仍在继续。

telegram · zaihuapd · 9月24日 02:00

**背景**: 现代大语言模型在训练后期会经历包含强化学习的后训练阶段：先用人偏好数据训练出一个奖励模型，由它给模型输出打分，模型则学习产出得分更高的内容。这就是让 Claude、ChatGPT 等模型变得好用的 RLHF（基于人类反馈的强化学习），而较新的“可验证奖励强化学习”则依赖数学、代码这类有客观正确答案、可自动判分的任务。由于文风和可读性远比一个正确的公式或跑通的测试更难自动评分，奖励设计就可能无意中教会模型为“评分者”（包括其他 AI 系统）而写，而不是为人而写。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://www.ibm.com/think/topics/llm-reinforcement-learning">LLM Reinforcement Learning | IBM</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5.5">Claude Opus 5 . 5 - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#LLM`, `#Reinforcement Learning`, `#AI Writing Quality`

---

<a id="item-2"></a>
## [OpenAI 称苹果 ChatGPT 集成表现不佳，合作出现裂痕](https://www.ft.com/content/256c4b36-a6c8-49ee-aa15-81cb089b2ced) ⭐️ 7.0/10

在 2026 年 9 月 23 日提交的一份法庭文件中，OpenAI 称苹果的 ChatGPT 集成「表现严重不佳」，并对用户兴趣寥寥表示失望。该文件出自 xAI 提起的反垄断诉讼，此时两家公司的关系已经恶化。 这一披露公开证实了苹果与 OpenAI 在 2024 年达成的旗舰合作已经破裂，同时恰逢苹果转向谷歌 Gemini 重建 Siri。它也为反垄断审查提供了素材，因为默认分发位置决定了哪些 AI 助手能触达主流用户。 OpenAI 指出，该集成默认关闭、需要多步操作才能激活，这是采用率低的原因。双方关系进一步恶化：苹果已对 OpenAI 提起商业秘密诉讼，并在今年 1 月与谷歌合作，用 Gemini 重建 Siri 的 AI 能力。

telegram · zaihuapd · 9月24日 05:15

**背景**: Apple 智能是苹果在 2024 年推出的一套端侧与云端 AI 功能，当年 WWDC 上宣布的 ChatGPT 集成旨在让 Siri 把某些复杂问题转交给 OpenAI 的模型处理。按照协议，ChatGPT 免费且无需账号即可使用，只有在用户同意后才会转发请求，这种设计意在保护隐私，但也增加了使用门槛。在 AI 助手市场，默认设置影响巨大，因为大多数用户从不更改设置，而这正是埃隆·马斯克的 xAI 提起的反垄断诉讼的核心争议点之一。

**标签**: `#OpenAI`, `#Apple`, `#ChatGPT`, `#Antitrust`, `#AI Partnerships`

---

<a id="item-3"></a>
## [OpenAI 发布心理健康基准 MentalHealthBench](https://openai.com/zh-Hans-CN/index/introducing-mentalhealthbench/) ⭐️ 7.0/10

OpenAI 发布了开放基准 MentalHealthBench，由来自 22 个国家的 80 多名持证心理健康专家共同参与制定，用于评估 AI 模型在真实心理健康对话中的回应表现。该基准包含 1215 段真实场景对话，衡量安全性、收集背景信息、维护用户自主权以及提供可行建议等行为，并覆盖成人、青少年、照护者和临床人员等多种场景。 现有的心理健康评测大多只关注紧急或危机场景，而 MentalHealthBench 把范围扩展到人们实际会向聊天机器人提出的日常情绪困扰与临床类对话。随着数以百万计的用户向通用 AI 寻求情感支持，一个公开且由专家参与制定的评测标准，为模型开发者、研究人员和监管机构提供了在高风险领域中衡量安全性与质量的共同标尺。 该基准以公共资源的形式开放发布，评估的是安全性、背景信息收集、支持用户自主权和提供可行建议这四项核心行为，而不只是对拒答或危机升级做简单打分。OpenAI 表示结果显示前沿模型在心理健康对话中的表现稳步提升，但同时明确强调 ChatGPT 不能替代专业治疗。

telegram · zaihuapd · 9月24日 06:00

**背景**: 基准测试是一套标准化的评测集合，让研究人员能够在明确定义的任务上比较不同 AI 系统；在 AI 安全领域，它把“有帮助但不能有害”这类模糊目标转化为可量化的分数。心理健康之所以成为敏感的测试场景，是因为聊天机器人正越来越多地被用于情感支持，而幻觉、过度自信的建议或过于严苛的拒答都可能造成伤害。由于 MentalHealthBench 中的对话均为合成并由专家设计，它力求在覆盖真实对话场景的同时不暴露真实患者的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-mentalhealthbench/">Introducing MentalHealthBench | OpenAI</a></li>
<li><a href="https://www.unite.ai/openai-debuts-mentalhealthbench-for-ai-mental-health-conversations/">OpenAI Debuts MentalHealthBench for AI Mental Health Conversations</a></li>
<li><a href="https://cdn.openai.com/ctf-cdn/MentalHealthBench_A_Comprehensive_Benchmark_of_AI_Capabilities_in_Realistic_Mental_Health_Conversations.pdf">[PDF] MentalHealthBench: An Expert-Informed Benchmark of AI Capabilities in Realistic Mental Health Conversations - OpenAI</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#mental health`, `#benchmark`, `#OpenAI`, `#evaluation`

---

<a id="item-4"></a>
## [Claude Code 云会话正式上线，Pro/Max 用户可领最高 250 美元额度](https://code.claude.com/docs/en/claude-code-on-the-web) ⭐️ 6.0/10

Anthropic 的 Claude Code 云会话正式结束研究预览，面向 Pro、Max、Team 及 Enterprise 用户开放，用户合上笔记本后任务仍可在云端继续运行，并可随时从浏览器、手机、桌面应用或终端查看和接管。现有订阅用户可领取一次性额度：Pro 用户 100 美元、Max 用户 250 美元，可通过官方领取页登录领取，也可在 Claude Code 中执行 /claim-credit。 把 Agent 的执行位置从本地机器搬到云端，意味着 Claude Code 从交互式终端助手变成了可以持续在后台干活的“常驻工人”，这对大型重构、全量测试扫描、多步骤构建-修复循环这类耗时任务尤其重要——过去这些任务一旦会话结束就会中断。同时这也让 Anthropic 更直接地与其他云端托管编码 Agent 竞争，顺应了开发者 Agent 向异步、常驻方向演进的趋势。 该额度仅限用于 Cloud sessions，领取截止时间为太平洋时间 10 月 7 日 23:59，额度有效期至 11 月 4 日 23:59；资格需登录后按账号情况及条款判定，并非所有用户都能领取。Anthropic 的受支持地区名单目前不含中国大陆、香港和澳门，因此这些地区的用户无法领取该优惠。

telegram · zaihuapd · 9月24日 02:45

**背景**: Claude Code 是 Anthropic 推出的 Agent 式编程工具，能够读写文件、执行 shell 命令，并代替用户完成多步骤的开发任务。它最初在本地终端中运行，因此 Agent 的工作与启动它的机器和会话绑定在一起。云会话把执行过程搬到 Anthropic 的云端基础设施上，任务可以无人值守地持续运行，之后还能从任意客户端恢复接管。发放一次性体验额度，是 Anthropic 推广新上线能力的常见做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/puxu-msft/my-claude-plugins/blob/main/claude-remote-3rd/ROADMAP.md">my-claude-plugins/claude-remote-3rd/ROADMAP.md at main - GitHub</a></li>
<li><a href="https://af.net/realtime/anthropic-unveils-may-2026-updates-for-claude-code-enhancing-developer-experience-and-safety/">Anthropic Unveils May 2026 Updates for Claude Code Enhancing Developer Experience and Safety | AIFOD</a></li>
<li><a href="https://www.hubwiz.com/blog/claude-code-routines/">Claude Code 新命令：Routines - 汇智网 | Software 2.0</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#anthropic`, `#ai-agents`, `#developer-tools`, `#cloud-computing`

---

<a id="item-5"></a>
## [三大运营商暂停金融分期业务，“0 元购机”全面停办](https://finance.sina.com.cn/jjxw/2026-09-24/doc-inisxhnx5270778.shtml) ⭐️ 6.0/10

自 2026 年 9 月 24 日起，中国移动、中国电信、中国联通暂停新受理旗下金融分期购机业务，即被宣传为“0 元购机”的和包信用购、橙分期、沃分期全面停办。三大运营商客服已确认暂停，已办理的老用户不受影响，原有分期合约继续生效并按协议正常履约。 此类业务此前是消费者投诉的重灾区，所谓“免费领手机”实际上是让用户办理分期贷款，因此三家运营商同时叫停可能会改变中国合约机的销售模式，并显著减少消费者金融纠纷。此举也释放出对运营商用于销售硬件的消费信贷和融资租赁渠道加强审视的信号。 三大运营商官方暂未发布正式回应，客服多称系“产品升级”，且未给出明确恢复时间；据报道，此次暂停仅针对新增办理，存量合约不受影响。此前投诉集中在未充分告知贷款协议、限制改套餐或销号以及高额违约金等问题上。

telegram · zaihuapd · 9月24日 08:46

**背景**: 在传统的合约机模式中，运营商通过补贴手机价格，换取用户在一定期限（通常为 24 个月）内承诺使用指定档位套餐。近年来这类业务越来越多地通过消费金融和融资租赁机构运作，例如橙分期由甜橙融资租赁（上海）有限公司运营，因此看起来是免费或优惠领手机，法律上却是用户需要偿还的贷款或租赁，批评者认为这一性质并未始终被清晰告知。由于债务关系落在金融机构而非仅运营商处，违约或提前终止可能影响用户的信用记录并产生高额违约金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.3dmgame.com/news/202609/3954492.html">三大运营商叫停 “0元购机” 实为金融 分 期 购机_3DM单机</a></li>
<li><a href="https://waphn.189.cn/hd/zifeizq/wap/zfzx/yxhdHYcfq.html">橙 分 期</a></li>

</ul>
</details>

**标签**: `#中国电信运营商`, `#金融分期`, `#消费者权益`, `#行业监管`, `#0元购机`

---

<a id="item-6"></a>
## [美国 ITC 对 DRAM 设备启动 337 调查](https://mp.weixin.qq.com/s/YtQiGdMulacmBbG6_pC_HQ) ⭐️ 6.0/10

2026 年 9 月 23 日，美国国际贸易委员会（ITC）投票决定对特定 DRAM（动态随机存取存储器）设备及其下游产品和组件启动 337 调查。该调查源于 Netlist 于 2026 年 8 月 11 日提交的立案申请，其指控相关产品侵犯多项美国专利，并请求发布有限排除令和禁止令，美光、慧与（HPE）、联想和超微（Supermicro）被列为被告。 由于 337 调查的救济手段是进口排除令而非单纯的损害赔偿，一旦裁定被告侵权，可能直接限制相关 DRAM 组件以及采用这些组件制造的服务器和 PC 进入美国市场，从而波及内存供应链和整机厂商的产品规划。此案也表明 Netlist 仍在持续推进其专利变现策略，目标直指头部存储原厂及其下游系统厂商。 Netlist 请求的具体救济措施是有限排除令（即在边境阻止侵权产品进口）以及对被列名公司的禁止令；此外，ITC 的 337 程序通常比地方法院的专利诉讼节奏更快。值得注意的是，DRAM 市场长期由美光、SK 海力士和三星三家供应商主导，因此涉及美光的纠纷对全球内存供应具有格外重要的影响。

telegram · zaihuapd · 9月24日 10:25

**背景**: DRAM 是一种易失性半导体存储器，每个数据位以电荷形式存储在微小的电容中，是计算机、服务器和显卡的主内存；由于电荷会逐渐泄漏，DRAM 必须定期刷新。美国 1930 年《关税法》第 337 条授权 ITC 调查进口中的不公平做法（最常见的是专利侵权），并可发布排除令阻止侵权产品进入美国。Netlist 是一家美国内存模组与知识产权公司，曾多次就其专利起诉主要存储原厂；而慧与、联想和超微属于下游系统厂商，它们为服务器和 PC 采购 DRAM 芯片与模组，因此在诉状中被列为被控技术的使用者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DRAM">DRAM</a></li>
<li><a href="https://www.goodwinlaw.com/en/insights/publications/2026/09/insights-lifesciences-tsemnc-itc-trade-secret-litigation-underused-forum">ITC Trade Secret Litigation: An Underused Forum | Insights &amp; Resources</a></li>
<li><a href="https://lexdana.ai/insights/itc">ITC / Section 337 — LexDana Insights · LexDana</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#ITC Section 337`, `#patent litigation`, `#semiconductor industry`, `#supply chain`

---