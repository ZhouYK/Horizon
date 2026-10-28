---
layout: default
title: "Horizon Summary: 2026-10-28 (ZH)"
date: 2026-10-28 23:03:30 +0000
lang: zh
report: default
---

> 从 172 条内容中筛选出 6 条重要资讯。

---

1. [Google 发布 Gemini 4 Carbon：主打网络安全与长时程自主任务的前沿模型](#item-1) ⭐️ 9.0/10
2. [谷歌提出睡眠框架，助大模型持续学习不遗忘](#item-2) ⭐️ 8.0/10
3. [长鑫存储拟量产 HBM3E，良率仅两三成](#item-3) ⭐️ 7.0/10
4. [Anthropic 招聘经理取消编程面试，称 Claude 写代码强于候选人](#item-4) ⭐️ 6.0/10
5. [调研：79%企业 GPU 半数时间闲置，91%的 AI 投入未经 ROI 审计](#item-5) ⭐️ 6.0/10
6. [苹果发布新款 MacBook Pro：首发 PROLED XDR 屏并首次加入触控](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Google 发布 Gemini 4 Carbon：主打网络安全与长时程自主任务的前沿模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) ⭐️ 9.0/10

Google 发布了 Gemini 4 Carbon，称其是迄今为止最强的前沿模型，主打网络安全与长时程任务能力。相比上一代 Gemini 4 Argon，Google 声称其安全代码生成成功率提升超过 2 倍、无依据声称减少约 2 倍、高严重性错位警报下降近 80%，并在 SEC-bench Pro 网络安全基准上以 88.2% 的成绩领先。 这次发布说明前沿实验室正把优化目标转向可持续自主运行的工程任务与网络防御，而不再只是对话或单次代码生成。由于同一套能力既可用于发现漏洞也可用于利用漏洞，先向经过审核的防御方开放、并接受美国政府预发布测试的做法，很可能成为此类两用网络安全模型的典型治理方式。 Gemini 4 Carbon 目前以 introductory 价格推出：输入每百万 token 收费 2 美元、输出每百万 token 收费 10 美元，与 Argon 相同，但 Google 表示后续价格将翻倍；开放范围也从部分网络安全防御者和可信合作伙伴，逐步扩展至开发者、企业和消费者。这些基准与安全方面的亮眼数字均为 Google 自行公布，尚未经过独立验证。

telegram · zaihuapd · 10月28日 17:09

**背景**: 长时程智能体任务（long-horizon agentic task）指的是自主模型围绕一个开放式目标，执行数十乃至数百个交织的推理步骤、工具调用和状态更新，它对规划、记忆和鲁棒性的要求远高于单次提示。SEC-bench Pro 是一项基准测试，要求编码智能体在 V8、SpiderMonkey 等浏览器引擎或 Linux 内核中找出已披露的漏洞，并用可触发崩溃的概念验证程序加以证明，而且测试前会预先告知漏洞的大致位置与类型。Gemini 4 Argon 是上一代模型，Carbon 据称沿用了 Argon 的多层安全体系，包括抗提示注入和思维链监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/">Introducing Gemini 4 Carbon</a></li>
<li><a href="https://klu.ai/benchmarks/sec-bench-pro">SEC - Bench Pro — Klu</a></li>
<li><a href="https://www.emergentmind.com/topics/long-horizon-agentic-tasks">Long-Horizon Agentic Tasks Overview - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#Google Gemini`, `#LLM release`, `#cybersecurity`, `#agentic AI`, `#model safety`

---

<a id="item-2"></a>
## [谷歌提出睡眠框架，助大模型持续学习不遗忘](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) ⭐️ 8.0/10

Google Research 提出了一种“睡眠框架”，在持续学习中插入离线巩固阶段，让大语言模型在主动交互与离线“睡眠”阶段之间周期性切换，把短期上下文巩固为长期参数。在包含 1000 万 token 长上下文、持续翻译和数学推理等测试中，该方法据称超过了 GPT-4 和标准监督微调（SFT）等基线。 灾难性遗忘是大模型在部署后持续吸收新知识的主要障碍之一，因为在新数据上微调往往会侵蚀模型已经学会的能力。一个既能缓解遗忘、又能追平甚至超越强基线的方法，有望让模型在生产环境中不断更新，而不是在训练完成后被冻结。 该机制依赖主动阶段与离线巩固阶段的循环切换，而非单纯对新数据做梯度更新，谷歌报告其在 1000 万 token 长上下文、持续翻译和数学推理任务上相较 GPT-4 与 SFT 基线取得提升。不过作为研究博客的发布，其计算开销、基准测试细节以及巩固过程能否在生产规模下奏效，仍需独立复现来检验。

telegram · zaihuapd · 10月28日 01:46

**背景**: 灾难性遗忘是指神经网络在新数据上训练时往往会丧失此前习得的能力，这对被期望在部署后继续学习的大语言模型而言是一个长期难题。持续学习的目标是让模型按顺序吸收新任务而不抹掉旧任务，而受大脑在睡眠中重放并巩固记忆所启发的“离线巩固”，是该领域最有前景的解法之一，与之并列的还有基于 LoRA 的更新和长上下文记忆等技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.turingpost.com/p/continual-learning-llms-ai-models-sleep">Continual Learning in LLMs: Why AI Models Need Sleep</a></li>
<li><a href="https://python.plainenglish.io/understanding-catastrophic-forgetting-and-hallucinations-in-large-language-models-a-beginners-4ac2d957ee94">Understanding Catastrophic Forgetting and Hallucinations in Large ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#continual-learning`, `#catastrophic-forgetting`, `#Google Research`, `#long-context`

---

<a id="item-3"></a>
## [长鑫存储拟量产 HBM3E，良率仅两三成](https://www.reuters.com/world/china/chinas-cxmt-start-advanced-ai-memory-production-despite-poor-yields-sources-say-2026-10-28/) ⭐️ 7.0/10

据路透社独家报道，长鑫存储（CXMT）已向多家国内 AI 芯片设计公司送样 HBM3E 高带宽内存，并计划在未来两个月内启动限量生产。但其良率仅为 20% 至 30%，远低于 SK 海力士约 70% 的水平。 在美國出口管制限制获取 SK 海力士、三星和美光产品的情况下，高带宽内存已成为中国 AI 加速器最紧的瓶颈，因此即便是低良率的国产 HBM3E 供应，也可能让国内 AI 芯片设计公司及其云客户维持出货。这也表明中国存储产业正从大宗 DRAM 迈向长期由韩美厂商主导的先进封装与堆叠存储领域。 在测试中，长鑫存储的 HBM3E 性能更接近 SK 海力士上一代 HBM3，而非真正的 HBM3E 水平，且预计售价将高于海外同类产品。该报道基于两名匿名消息人士，篇幅简短，未披露堆叠层数、带宽或封装工艺等技术细节。

telegram · zaihuapd · 10月28日 06:19

**背景**: 高带宽内存（HBM）是一种堆叠式 DRAM 技术，多颗 DRAM 裸片垂直互连后紧邻 AI 加速器放置，可提供远超传统服务器内存的带宽。HBM3E 是 HBM3 的扩展版本，将每针脚速率提升至约 8-9.6 Gbps，从而实现更高容量和能效，并被 NVIDIA H200 等加速器采用。长鑫存储成立于 2016 年，总部位于安徽合肥，是中国领先的 DRAM 制造商，过去主要聚焦于面向手机、PC 和服务器的大宗 DRAM，而非先进堆叠存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.fibermall.com/blog/hbm-hbm2-hbm3.htm">HBM vs HBM2 vs HBM3 vs HBM3e | FiberMall</a></li>

</ul>
</details>

**标签**: `#HBM3E`, `#semiconductors`, `#CXMT`, `#AI hardware`, `#export controls`

---

<a id="item-4"></a>
## [Anthropic 招聘经理取消编程面试，称 Claude 写代码强于候选人](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/) ⭐️ 6.0/10

Anthropic 招聘经理 Felix Rieseberg 表示，他本月已停止在面试中考察编程题，因为 Claude 现在解这类题比候选人更好，写代码不再是有效的筛选标准。他还认为，执行力成本下降后资历不再决定影响力，并建议初级工程师瞄准业务目标，用一个周末做出单一原型来争取支持。 一家领先 AI 实验室的招聘经理公开放弃编程面试，是一个值得关注的行业信号：如果 AI 模型在算法题上稳定胜过候选人，雇主就必须围绕判断力、产品感知和真实成果重新设计技术评估方式。相关建议也重塑了初级工程师的职业策略——他们可能越来越被以交付出的原型而非工作年限来衡量。 Rieseberg 以 Claude Code 的图形界面作为新模式的例证：两名新人用一个周末做出原型，约八天后就发布了首个公开版本。这一说法属于个人经验，且来自单一招聘经理，反映的是某个团队的筛选理念，而非 Anthropic 全公司层面的正式招聘政策。

telegram · zaihuapd · 10月28日 01:46

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，最早于 2023 年 3 月以聊天机器人形式发布，并采用该公司的“宪法式 AI”方法训练。Claude Code 是 Anthropic 的智能体式编程工具，能读取代码库、编辑文件并为开发者执行命令。编程面试（通常是算法与数据结构题）长期以来是软件工程岗位的默认筛选手段，因此取消它属于对既有惯例的突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://claude.ai/">Claude</a></li>

</ul>
</details>

**标签**: `#hiring`, `#AI`, `#Anthropic`, `#Claude`, `#software-engineering-careers`

---

<a id="item-5"></a>
## [调研：79%企业 GPU 半数时间闲置，91%的 AI 投入未经 ROI 审计](https://venturebeat.com/infrastructure/ai-bubble-update-79-of-companies-say-their-gpus-sit-idle-at-least-half-the-time-yet-most-plan-new-ai-platforms) ⭐️ 6.0/10

VentureBeat 发布的一项企业调研显示，79%的受访企业其 GPU 平均利用率不足 50%，91% 的 AI 基础设施投资从未经过财务部门正式的 ROI（投资回报率）审计。尽管如此，处于低利用率状态的受访企业中有 70% 仍计划在未来 12 个月内继续采购并部署新的 AI 计算平台。 这组数据表明，企业 AI 支出更多由“技术焦虑”和军备竞赛驱动，而非经过测算的回报，意味着大量资本被投入到产出有限的硬件上。若这一模式具有普遍性，将进一步强化“AI 建设存在泡沫成分”的判断，也会迫使 CFO 与基础设施负责人用真实的利用率数据来为预算辩护。 该调研并未公开样本量、行业构成以及利用率的具体测量方式等方法论细节，因此这些数字更应被视为方向性参考而非定论。此外，GPU 利用率本身就是一个出了名难以定义的指标——短暂的内存或计算峰值可能被记为“繁忙”，即使实际有效吞吐很低。

telegram · zaihuapd · 10月28日 02:37

**背景**: GPU 利用率指图形处理器实际处于工作状态的时间占比，它是控制 AI 基础设施成本的核心杠杆：闲置的加速卡照样消耗电力、机架空间和折旧，却不产生任何产出。由于 AI 集群通常按峰值需求配置，平均利用率往往远低于峰值，因此高效的运营方会在调度、批处理和多方共享上投入。所谓 ROI 审计，则是把基础设施支出正式对应到可衡量的业务成果上——当 AI 预算被当作“战略押注”而非明细投资来审批时，许多企业往往会跳过这一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lakefs.io/blog/gpu-utilization/">GPU Utilization: What Is It, Benefits and Best Practices</a></li>
<li><a href="https://www.mercatus-ai.com/blog/gpu-utilization">GPU Utilization: The Most Important Metric in AI ...</a></li>
<li><a href="https://resiliotech.com/blog/how-to-build-business-case-ai-infrastructure-investment">How to Build a Business Case for AI Infrastructure ... | Resilio Tech</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#GPU utilization`, `#enterprise AI`, `#ROI`, `#cloud computing`

---

<a id="item-6"></a>
## [苹果发布新款 MacBook Pro：首发 PROLED XDR 屏并首次加入触控](https://www.apple.com/newsroom/2026/10/apple-unveils-groundbreaking-macbook-pro-with-proled-xdr-display/) ⭐️ 6.0/10

苹果发布新款 MacBook Pro，首发搭载 PROLED XDR 显示屏——这是一块串联 OLED 面板，峰值亮度可达 2000 尼特、对比度达 1000 万:1，同时首次为 Mac 加入触控输入。14 英寸与 16 英寸机型搭载 M5 Pro/M5 Max 芯片，机身更薄更轻，续航最长 24 小时，10 月 28 日开启预售、11 月 6 日正式开售，14 英寸版起售价 22999 元、16 英寸版 27999 元。 在 Mac 上加入触控，推翻了苹果多年来公开坚持的“笔记本不应配备触摸屏”立场，也意味着 Mac 应用开发者未来可能需要同时为直接触控操作与传统的指针、键盘交互做设计。串联 OLED 面板还把笔记本的 HDR 亮度与对比度推向了新水平，这对视频调色、照片编辑、HDR 内容制作等对色彩要求严苛的专业工作流意义重大。 根据苹果的技术资料，PROLED XDR 显示屏支持 ProMotion，刷新率最高可达 120Hz 同时兼顾续航；其串联 OLED 结构通过堆叠两层 RGB 发光层来提升亮度和面板寿命。需要注意：上述规格来自转发 Apple Newsroom 的 Telegram 频道及第三方报道，关于触控实现方式、定价和实际续航的独立评测与实机验证尚未出现。

telegram · zaihuapd · 10月28日 17:16

**背景**: 串联 OLED（Tandem OLED，也称堆叠式 OLED）是一种在单块 OLED 面板中叠放两层 RGB 发光层的显示技术；与传统的单层 OLED 相比，由于每一层只需承担更小的发光压力就能达到目标亮度，因此可以实现更高的亮度和更长的使用寿命。苹果以 PROLED XDR 之名推出该实现，它是前几代 MacBook Pro 所用 mini-LED 背光 Liquid Retina XDR 显示屏的演进。M5 Pro 与 M5 Max 是苹果自研芯片家族的最新成员，接替高端 MacBook Pro 产品线中的 M4 Pro/M4 Max。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/macbook-pro/proled-xdr-display/">MacBook Pro with PROLED XDR Display - Apple</a></li>
<li><a href="https://www.techpowerup.com/354229/apple-unveils-groundbreaking-macbook-pro-with-proled-xdr-display-and-touch-for-the-first-time-on-mac">Apple Unveils Groundbreaking MacBook Pro With PROLED XDR ...</a></li>
<li><a href="https://www.lgdisplay.com/eng/technology/tandem-oled">Tandem OLED | LG디스플레이 | LG Display</a></li>

</ul>
</details>

**标签**: `#Apple`, `#MacBook Pro`, `#hardware`, `#OLED display`, `#touchscreen`

---