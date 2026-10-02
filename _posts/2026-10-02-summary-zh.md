---
layout: default
title: "Horizon Summary: 2026-10-02 (ZH)"
date: 2026-10-02 23:03:27 +0000
lang: zh
report: default
---

> 从 160 条内容中筛选出 8 条重要资讯。

---

1. [arXiv 全面限投：每人每月仅限 2 篇](#item-1) ⭐️ 7.0/10
2. [Google Research 发布 Cogentic 多智能体系统，自动发现数学证明](#item-2) ⭐️ 7.0/10
3. [Anthropic 为 Claude Code 推出 mods 自定义功能](#item-3) ⭐️ 7.0/10
4. [Anthropic 提议澳大利亚允许用受版权作品训练 AI](#item-4) ⭐️ 6.0/10
5. [香港多名 Claude 用户账号遭停用](#item-5) ⭐️ 6.0/10
6. [美三大运营商拟建合资企业，用卫星填补偏远网络盲区](#item-6) ⭐️ 6.0/10
7. [Sub2API 曝出计费绕过漏洞，0.2.13 已修复](#item-7) ⭐️ 6.0/10
8. [树莓派再度涨价：2 GB 版 Pi 4 售价升至 67.50 美元](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [arXiv 全面限投：每人每月仅限 2 篇](https://www.huxiu.com/article/4895127.html) ⭐️ 7.0/10

自 10 月 1 日起，arXiv 将规定每位提交者每个自然月最多只能提交 2 篇论文，覆盖计算机、数学、物理等全部学科，且被拒稿件同样占用当月额度。该新规出台的背景是 9 月投稿量达到 40363 篇，创下 arXiv 35 年来的历史新高，其中 AI 分类论文两年内增长超过 6 倍。 arXiv 是计算机、数学和物理领域最主要的预印本平台，因此这一上限将直接改变研究者——尤其是高产作者和大型实验室——规划与安排发布节奏的方式，同时也表明大量低质量 AI 生成论文已成为开放科学基础设施面临的一场系统性危机。这可能会把部分产出引流到其他预印本平台、期刊或会议论文集，并为其他平台树立可效仿的先例。 每月 2 篇的限制只统计实际执行提交操作的人，而非全部合著者，因此多作者论文不会牵连所有署名者；但被拒稿件仍会占用提交者当月的额度。该规则均匀适用于 arXiv 所有分类，而非专门针对 AI 领域，并且执法对象是提交者的账户，而不是某位研究者所署名的论文总数。

telegram · zaihuapd · 10月2日 06:21

**背景**: arXiv 是一个免费、不经过同行评审的预印本平台，于 1991 年上线，研究者会在正式期刊发表之前或同时把论文草稿发布在这里；它已成为物理学、数学以及大部分计算机科学和机器学习新成果事实上的第一发布地。由于在 arXiv 上发布只经过较为轻量的审核而非完整同行评审，平台依赖人工审核员来筛查垃圾投稿、抄袭和非科学内容。生成式 AI 工具的迅速普及使大规模生产看似像模像样的论文变得非常廉价，从而压垮了这些志愿与专职审核力量。

**标签**: `#arXiv`, `#academic-publishing`, `#AI-research`, `#preprints`, `#open-science`

---

<a id="item-2"></a>
## [Google Research 发布 Cogentic 多智能体系统，自动发现数学证明](https://arxiv.org/abs/2609.40324v1) ⭐️ 7.0/10

Google Research 公布了名为 Cogentic 的多智能体系统，采用“证明—验证”循环：多个独立证明器分头探索，专门组件进行对抗式验证，已确认的结果被写入可持续复用的验证账本。据称该系统以 Gemini 为基础模型，在在线学习、拍卖理论和机制设计领域的 5 个开放问题上产出新证明，并均由领域专家独立验证，详见配套论文。 如果结果经得起检验，这将是 AI 用于数学研究的又一里程碑：通用的大模型智能体流水线能够产出经专家核验、可发表的新定理，而不仅仅是辅助人类数学家或解答竞赛题。它也表明“多智能体编排 + 对抗式自检”是提升开放式推理任务可靠性的可行路径，这一范式可能扩散到其他科研与验证场景。 据描述，Cogentic 仅从问题陈述出发、无需专家提示即可工作，其设计强调对抗式验证、可长期复用的已确认结果账本以及对推理效率的考量。但需注意：该消息目前主要来自聚合式社交投稿，所引用的 arXiv 编号（2609.40324v1）看起来日期异常且未被核实，因此无论是证明本身还是专家验证，都无法仅凭现有材料独立确认。

telegram · zaihuapd · 10月2日 12:04

**背景**: 自动定理证明传统上依赖 Isabelle、Coq、Lean 等交互式证明助手，并用神经网络或检索增强方法辅助补全证明步骤。近期“AI for math”工作则用大语言模型直接提出证明，但模型输出可能隐藏细微错误，因此必须经过形式化检查器或人类专家的验证。此次涉及的开放问题属于理论计算机科学：在线学习研究反馈受限下的序贯决策，拍卖理论分析竞价规则与收益，机制设计则研究如何制定规则使自利参与者产生良好整体行为。这里的“多智能体”指给多个大模型实例分配不同角色或搜索方向，再汇总并校验各自结果，而不是由单一模型一次性作答。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.40324">Cogentic: Multi-Agent Orchestration for Automated Proof Discovery</a></li>
<li><a href="https://agihunt.info/en/e/1a0f9cea5c8b68af181e13c5f80">Google&#x27;s Cogentic Multi - Agent System Tackles… · AGI Hunt</a></li>

</ul>
</details>

**标签**: `#multi-agent-systems`, `#automated-theorem-proving`, `#AI-for-mathematics`, `#LLM-agents`, `#Google-Research`

---

<a id="item-3"></a>
## [Anthropic 为 Claude Code 推出 mods 自定义功能](https://claude.com/blog/claude-code-mods) ⭐️ 7.0/10

2026 年 10 月 1 日，Anthropic 发布了 Claude Code 的 mods 功能：开发者只需编写少量 JavaScript/TypeScript 代码模块，就能改写提示词、拦截高风险命令、新增自定义界面或替换内置功能，需 Claude Code 2.1.287 及以上版本。Mods 随插件分发，可在 CLI 和桌面版中通过 /plugin 安装，且默认开启。 mods 让这款被广泛使用的 AI 编程助手变成可扩展平台，团队可以自行封装工作流、安全护栏和界面，而无需等待 Anthropic 官方排期。由于部分内置功能（以 /diff 为起点）已被改写为 mods，这一变化还表明 Claude Code 正向“插件优先”的架构转型，为第三方生态打开空间。 mods 拥有与 Claude Code 相同的权限，且官方明确表示不设沙箱隔离，因此提醒用户只安装可信来源的 mod；用户也可以直接让 Claude Code 自己编写 mod。该功能在 9 月 14 日的帖子中已有预告，此次发布在 X 上的帖子获得约 130 万次浏览，并伴随 Token Weather、Blast Radius、Replay Theater 等后续 mod 出现。

telegram · zaihuapd · 10月2日 12:32

**背景**: Claude Code 是 Anthropic 推出的命令行与桌面端 AI 编程助手，可以读取代码仓库、执行命令并直接修改文件。mods 通过插件（plugin，即用户安装的扩展打包单元）分发，使用 TypeScript（JavaScript 的类型化超集，常用于工具链开发）编写。作为对照，DeepSeek 开源的 DeepSeek Harness 智能体框架（v0.1 开发者预览版，2026 年 8 月 13 日发布）也基于类似的“一切皆插件”理念，其 Cordis 组件模型支持动态增删插件而不破坏正在运行的应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/claude-code-mods">Customize Claude Code with mods in TypeScript | Claude by ...</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/08/14/deepseeks-innovative-harness-treats-everything-as-a-plug-in/5288095">DeepSeek&#x27;s innovative harness treats everything as a plug-in</a></li>
<li><a href="https://bazaarlink.ai/en/blog/claude-code-mods-typescript-customize-en">Claude Code Mods: Customize Behavior and UI with TypeScript</a></li>

</ul>
</details>

**社区讨论**: DeepSeek Harness 团队负责人崔添翼在 X 上引用 Anthropic 员工的帖子表示祝贺，并阐释了该功能与 DeepSeek Harness“一切皆插件”设计的相似性。中文科技社区的反应整体轻松且正面，被概括为“好的设计心有灵犀”。

**标签**: `#Claude Code`, `#Anthropic`, `#Developer Tools`, `#AI Coding`, `#Extensibility`

---

<a id="item-4"></a>
## [Anthropic 提议澳大利亚允许用受版权作品训练 AI](https://www.theguardian.com/technology/2026/oct/02/anthropic-ai-opt-out-australia-copyright-abc-cannibalisation-of-news) ⭐️ 6.0/10

Anthropic 正推动澳大利亚政府有条件地允许科技公司在“退出（opt-out）”机制下使用澳大利亚受版权保护的作品训练 AI 模型，并将在下周与 OpenAI 高管一同出席议会人工智能联合委员会听证会。澳大利亚广播公司 ABC 和 SBS 则明确反对，要求 AI 公司接受版权、隐私等监管并补偿媒体，ABC 还警告新闻业可能被“蚕食”。 这是对“退出（opt-out）模式”能否成为全球 AI 训练数据默认规则的一次关键检验——该模式让权利人主动声明保留权利，而非要求 AI 公司事先取得授权。澳大利亚的最终决定可能影响欧盟、英国、香港等地的类似立法讨论，并直接重塑 AI 开发者与新闻出版商之间的商业关系。 澳大利亚政府已排除设立宽泛的文本与数据挖掘（TDM）豁免，但仍在讨论其他版权安排，因此 Anthropic 的提议比全面豁免更为有限。对 opt-out 机制的主要批评在于，它把声明保留权利的行政负担转嫁给个人创作者和中小权利人，他们必须主动标记自己的作品才能避免被纳入训练数据。

telegram · zaihuapd · 10月2日 03:34

**背景**: 生成式 AI 模型需要以海量文本和图像语料进行训练，其中大量内容受版权保护，全球法院与立法机构至今仍在判定这种使用是否合法。一种折中方案是“退出（opt-out）”机制：默认允许训练，除非权利人明确声明保留权利；另一种方案则是文本与数据挖掘（TDM）豁免，直接使出于机器学习目的的抓取行为合法化。欧盟、英国、香港等司法辖区都讨论过不同版本的 opt-out 方案，而澳大利亚议会人工智能联合委员会目前正在同时听取 AI 开发者和媒体机构的意见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bennettschool.cam.ac.uk/blog/ai-ip/">Government’s proposed ‘opt-out’ model for training AI goes ...</a></li>
<li><a href="https://blog.galalaw.com/post/102k8jn/to-opt-out-or-not-to-opt-out-the-question-of-the-opt-out-model-for-ai-traini">To Opt Out or not to Opt Out? – The Question of the “Opt-out ...</a></li>
<li><a href="https://www.lexology.com/library/detail.aspx?g=dfba3e60-068f-45fb-8b3c-c82c8412096e">The New Gold Rush: Text and Data Mining Exemptions to... - Lexology</a></li>

</ul>
</details>

**标签**: `#AI copyright`, `#AI regulation`, `#Anthropic`, `#policy`, `#Australia`

---

<a id="item-5"></a>
## [香港多名 Claude 用户账号遭停用](https://www.newmobilelife.com/2026/10/01/claude-bans-hk-user/) ⭐️ 6.0/10

10 月 1 日，香港多名 Claude 用户在登录时遇到“账号停用”或“拒绝访问”提示，其中部分用户还是已付费的 Claude Pro 订阅者。相关情况迅速在当地科技社群和讨论区传播，但 Anthropic 至今未作出公开回应。 这一事件表明 AI 服务商在落实地区可用性限制时可能相当强硬，付费订阅者也可能在已付钱的情况下失去访问权限。对于身处未开放地区、依赖 VPN 使用 AI 服务的用户来说同样重要，因为类似的风控检查可能扩散到其他服务商和工具。 受影响用户和网络工程师推测，封禁可能与商业 VPN 数据中心 IP 段、支付与地区信息不一致，以及频繁切换 VPN 节点有关。具体触发原因尚未得到确认，也不清楚这些封禁是永久性的还是可以申诉解除。

telegram · zaihuapd · 10月2日 04:19

**背景**: Claude 是 Anthropic 开发的 AI 助手，和许多 AI 服务一样，它只在官方支持的部分国家和地区提供。身处未开放地区的用户常通过商业 VPN 访问，但 VPN 通常会经由公开可查的数据中心 IP 段转发流量，这类 IP 很容易被风控系统识别。此外，服务方往往会交叉核对比账单国家、支付方式和账号所在地区，这些信息不一致时就可能被判定为规避地区限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shop.deeper.network/blogs/newsletters/why-do-websites-know-i-m-using-a-vpn-2026-guide">Why Do Websites Know I’m Using a VPN ? (2026 Guide)</a></li>
<li><a href="https://support.apple.com/en-us/118283">Change your Apple Account country or region - Apple Support</a></li>
<li><a href="https://microesim.com/blogs/microesim-blogs/tiktok-region-locked-in-china-why-your-esim-supports-tiktok-but-still-blocks-you">TikTok Region-Locked in China? Why Your eSIM... - MicroEsim</a></li>

</ul>
</details>

**社区讨论**: 讨论主要集中在本港科技群组与论坛，整体情绪以焦虑和互相求助为主，而非深度分析，用户们交流哪些节点和支付方式触发了封禁。也有人对“VPN 导致封禁”的说法提出质疑，指出并非所有被停用的账号都使用相同配置，同时普遍对 Anthropic 迟迟没有官方说明感到不满。

**标签**: `#Anthropic`, `#Claude`, `#Hong Kong`, `#Account Bans`, `#Regional Restrictions`

---

<a id="item-6"></a>
## [美三大运营商拟建合资企业，用卫星填补偏远网络盲区](https://www.ithome.com/1/009/320.htm) ⭐️ 6.0/10

美国三大移动运营商 AT&amp;T、T-Mobile 和 Verizon 宣布达成合作意向，计划成立合资企业，利用卫星技术识别网络覆盖盲区，重点改善偏远及农村地区的连接质量。三家还希望借此提升自然灾害等紧急情况下的通信可靠性，并提高频谱资源的使用效率，但该合作目前仍处于筹备阶段。 美国三大运营商平时竞争激烈，此次愿意共同出资做基础设施相当罕见，若成行将加速卫星方案在农村用户和应急救援场景中的落地。这也可能改变美国移动网络向那些修建地面基站始终不划算的地区扩展的方式。 目前关键细节基本空白：公告仅确认了合作意向，并未公布合资架构、卫星合作方或星座方案、所用频段、覆盖范围、服务模式以及时间表。公告中提到的“频谱效率”暗示运营商也在考虑用卫星链路缓解网络拥塞或复用已有授权频谱，而不仅仅是新增覆盖点。

telegram · zaihuapd · 10月2日 09:07

**背景**: 卫星直连手机（Direct-to-Cell，简称 D2D）技术让普通 LTE/5G 手机可以像连接蜂窝基站一样直接与卫星通信，而无需专用卫星电话。该技术正由 3GPP 在非地面网络（NTN）工作项下进行标准化，从 Release 17 开始，通过改造 5G 接入网机制来适应卫星的高时延、快速移动波束和多普勒频偏。频谱效率则是衡量单位无线电带宽能传输多少数据的指标，通常以比特每秒每赫兹（bit/s/Hz）表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.3gpp.org/technologies/ntn-overview">Non-Terrestrial Networks (NTN) - 3GPP</a></li>
<li><a href="https://blog.csdn.net/yugangnj/article/details/157804164">一文读懂 3GPP NTN 标准：卫星如何真正“变成”5G 网络的一部分？_3gpp ...</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/%E9%A0%BB%E8%AD%9C%E6%95%88%E7%8E%87">频谱效率 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#telecom`, `#satellite-communication`, `#rural-connectivity`, `#industry-news`, `#US-carriers`

---

<a id="item-7"></a>
## [Sub2API 曝出计费绕过漏洞，0.2.13 已修复](https://github.com/Wei-Shaw/sub2api) ⭐️ 6.0/10

一则 Telegram 安全警告指出，Sub2API 0.2.12 及更早版本存在一处计费逻辑缺陷：在特定配置条件下，请求可以正常返回却不被计费。该帖随后更新确认，0.2.13 版本已修复此问题。 对于把 Sub2API 当作 API 网关自建部署的用户来说，计费与配额统计是防止白嫖和滥用的关键环节，该缺陷可能导致收入静默流失，或让某些 Key 在不被扣费的情况下消耗容量。虽然影响范围仅限于这一特定开源项目的使用者，但它也说明 AI 代理网关中的计费逻辑缺陷会多快地侵蚀访问控制与成本核算。 该漏洞被描述为计费逻辑缺陷，而非远程代码执行或认证绕过，并且只在特定配置条件下触发，表现为请求成功但没有产生计费记录。公告建议用户关注计费与对账数据中“请求成功却不计费”的异常、加强对异常 Key 行为的监控，并跟进上游修复进展；披露者称其结论来自社区反馈加上频道对代码的审计。

telegram · zaihuapd · 10月2日 10:52

**背景**: Sub2API 是一个开源的 AI API 代理/网关，可把 Claude、OpenAI、Gemini、Antigravity 等服务的订阅统一到一个入口，代码托管在 GitHub 的 Wei-Shaw/sub2api 仓库。这类网关通常用用户发放的 API Key 做鉴权，并按调用量扣减配额或余额，因此计费模块实际上也是访问控制体系的一部分。一旦该模块出现缺陷，调用方就能消耗模型资源而不被扣费，对运营者而言既造成成本损失，也带来滥用监控难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Sub2API">Sub2API</a></li>
<li><a href="https://github.com/Wei-Shaw/sub2api/issues/5350">OAuth Account Takeover via Pending Exchange Bypass in sub2api</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#billing`, `#Sub2API`, `#open-source`

---

<a id="item-8"></a>
## [树莓派再度涨价：2 GB 版 Pi 4 售价升至 67.50 美元](https://www.theregister.com/personal-tech/2026/10/02/once-a-35-computer-the-2-gb-raspberry-pi-4-now-costs-6750/5300774) ⭐️ 6.0/10

树莓派将 2 GB 版 Pi 4 与 Pi 5 的价格各上调 12.50 美元，现售价分别为 67.50 美元和 77.50 美元，理由是内存成本上涨。官方表示待内存价格回落后会重新降价，但同时警告短缺状况可能持续到 2028 年。 曾经以 35 美元为卖点的开发板如今价格几乎翻倍，这给爱好者、学生以及基于树莓派做产品的工业嵌入式开发者都带来了成本压力。这也说明当前 DRAM 供应紧张已从服务器和 PC 蔓延到最廉价的单板计算机。 树莓派官方建议用户考虑 Pi 3B 等较旧型号，或重新评估项目实际需要多少内存；CEO 则承诺若内存价格回落就会降价。但这一承诺可能很久才能兑现：美光已警告内存短缺可能持续到 2028 年。

telegram · zaihuapd · 10月2日 13:18

**背景**: 树莓派是一系列低成本、信用卡大小的单板计算机，最初由英国为计算机科学教育而开发，后来广泛用于工业自动化、机器人、物联网设备和嵌入式系统。2 GB 版 Pi 4 曾经售价 35 美元，疫情期间涨到 45 美元时被称作临时措施，但此后价格一路走高。其背后是 2025 年开始的全球内存供应短缺，主要因为 AI 数据中心需求吞噬了 DRAM 和 NAND 的产能，媒体戏称为“RAMmageddon”（内存末日）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Raspberry_Pi">Raspberry Pi</a></li>
<li><a href="https://en.wikipedia.org/wiki/2025%E2%80%93present_global_memory_supply_shortage">2025–present global memory supply shortage - Wikipedia</a></li>
<li><a href="https://www.techrepublic.com/article/news-micron-memory-shortage-2028-ai-demand/">Micron Warns Memory Shortage Will Get Worse Through 2028</a></li>

</ul>
</details>

**标签**: `#Raspberry Pi`, `#hardware pricing`, `#memory shortage`, `#embedded systems`, `#supply chain`

---