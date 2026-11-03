---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03 23:05:11 +0000
lang: zh
report: ai
---

> 从 278 条内容中筛选出 10 条重要资讯。

---

1. [Qwen 3.8 27B 可在本地解读模型原始权重，呼应「权重空间编程」论文](#item-1) ⭐️ 9.0/10
2. [视频中的飞机背景音可通过 ADS-B 数据精确定位拍摄地点](#item-2) ⭐️ 7.0/10
3. [《自然》文章综述机器学习与人工智能在精准医疗预测建模中的新兴应用](#item-3) ⭐️ 7.0/10
4. [阿里巴巴在乌镇峰会宣布开源 470 余个 Qwen 模型](#item-4) ⭐️ 7.0/10
5. [AWS 演示 ServiceNow 与 Bedrock AgentCore Gateway 的 OBO 令牌交换](#item-5) ⭐️ 6.0/10
6. [谷歌据报威胁切断拒绝 AI 工具学校的搜索访问](#item-6) ⭐️ 6.0/10
7. [ROSS Intelligence 请求美国上诉法院重审 Westlaw 人工智能版权案](#item-7) ⭐️ 6.0/10
8. [微软 AI 负责人：若 AI 显现意识迹象应停止开发](#item-8) ⭐️ 6.0/10
9. [美国科技巨头隐性 AI 债务半年激增 90%至 3.2 万亿美元](#item-9) ⭐️ 6.0/10
10. [LG 新能源将电池产能转向 AI 数据中心储能](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qwen 3.8 27B 可在本地解读模型原始权重，呼应「权重空间编程」论文](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 9.0/10

Simon Willison 报告称，在他笔记本电脑上本地运行的 Qwen 3.8 27B 能够解读模型的原始权重——即阅读一个小型策略网络以浮点数形式导出的参数文本，并推断出该网络是在哪款游戏上训练的。这用一个消费级开源权重模型复现了 Rikiya Takehi、Jayden Teoh、Alex Zhang 和 Omar Khattab 近期论文《Sparks of Weight-Space Programming》中最引人注目的「不使用工具」示例之一，该论文此前是在 GPT-6 Astra 上展示这一能力的。 如果一个在笔记本上运行的 27B 开源权重模型就能解读原始权重，那么这项此前只在前沿模型上展示过的能力便变得大众可及，从而降低了模型可解释性研究、直接权重编辑以及无梯度模型修复的门槛。这也说明本地模型与开源模型正在缩小差距，而这些任务此前被视为只有前沿实验室才具备的推理能力。 论文最引人注目的论断是：GPT-6 Astra 找出了导致 Qwen3.5-0.8B 陷入推理循环的权重缺陷，并通过原生编辑仅 0.016% 的权重将其修复，使 MATH-500 从 7.9% 提升到 48.1%，IFEval 提升三倍——全程无需梯度或训练循环。Willison 刻意只聚焦于「不使用工具」的权重解读任务，并指出相关提示词是自包含的、已发布在 RikiyaT/lm\_understand-logs 这个 GitHub 仓库中，任何人都可以用他 LLM 工具的 -f/--fragment 选项重新运行。

rss · Simon Willison · 11月3日 16:29

**背景**: 神经网络的「权重」就是它学到的参数——对于这些小型游戏网络而言，本质上就是一串没有任何标签说明的浮点数列表。「权重空间编程」（Weight-Space Programming）是论文作者创造的术语，指 LLM 直接分析这堆数字，推断网络各部分在计算什么，并相应修改数值，而不是去写训练代码。Qwen 3.8 27B 是阿里于 2026 年 8 月以 Apache 2.0 协议发布的开源权重模型，而 GPT-6 Astra 是 OpenAI 于 2026 年 9 月发布的前沿模型，也是最初实验的对象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read...</a></li>
<li><a href="https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/">Qwen 3.8 27B on my laptop can interpret model weights , too</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区反应明显分化：spaCy 作者 Matthew Honnibal 认为该论文具有误导性，因为它把纯粹的权重解读与借助工具的权重编辑混为一谈；Sean Goedecke 则拆解了 Qwen3.5-0.8B 那个例子，指出它不过是重复了普通机器学习研究者会采取的步骤。Willison 在论述框架上基本认同这些批评者，同意这两个问题应当分开讨论，但他认为「不使用工具」的权重解读结果才是真正更有意思的那一个。

**标签**: `#LLMs`, `#weight-space programming`, `#model interpretability`, `#local inference`, `#AI research`

---

<a id="item-2"></a>
## [视频中的飞机背景音可通过 ADS-B 数据精确定位拍摄地点](https://simonwillison.net/2026/Nov/3/a-sound-that-leaks-your-exact-location/) ⭐️ 7.0/10

安全研究者 Colsto 发布了一段 YouTube 视频，演示如何从录音中提取几乎听不见的飞机背景噪声，并分析出每架飞机的多普勒曲线。将这些曲线以及不同航班之间的时间间隔与公开的 ADS-B 航班追踪数据交叉比对，就能反推出音频或视频的精确录制地点。Simon Willison 称其为&quot;天才般的 OSINT 手法&quot;，该内容随后在 Lobste.rs 上引发讨论。 这把一个长期被忽视的环境杂音变成了定位信标：即使视频的元数据被清除、画面中没有任何地标，只要使用了普通麦克风录音，发布者就可能泄露自己的精确物理位置。这对记者、活动人士和普通内容创作者都构成切实的隐私风险，也为 OSINT 工具箱在图像定位之外增添了新的手段。 该方法依赖于高质量的公开航班数据和有利条件：飞机必须飞得足够近，其多普勒频移才能在录音中被测量出来，而且这一分析依赖 ADS-B 广播信号，而并非所有飞机都始终发送该信号，历史数据也未必被完整存档。Simon Willison 指出该技术利用飞机的速度、距离以及不同航班之间的间隔来定位，而一个名为 DOPPLERGEIST 的开源项目已经将这类声学定位自动化。

rss · Simon Willison · 11月3日 05:32

**背景**: ADS-B（广播式自动相关监视）是飞机持续广播自身身份、位置、高度和速度的系统，其数据被各类公开航班追踪服务所使用。多普勒效应是指声源靠近或远离听者时，接收频率发生变化的物理现象——就像救护车驶过时音调的变化——把这种频移随时间画成曲线，就得到包含飞机轨迹和最近接近点的多普勒曲线。由于每架飞机的航迹都是已知且有记录的，把从录音中提取出的多普勒曲线与某个具体航班匹配，就能有效约束麦克风必须所在的位置范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_Dependent_Surveillance%E2%80%93Broadcast">Automatic Dependent Surveillance–Broadcast - Wikipedia</a></li>
<li><a href="https://github.com/1337isnot1337/DOPPLERGEIST">GitHub - 1337isnot1337/DOPPLERGEIST: A tool to geolocate audio ...</a></li>
<li><a href="https://orbitalfocus.uk/Tracking/Doppler.php">Satellite Tracking - Doppler Measurement</a></li>

</ul>
</details>

**标签**: `#OSINT`, `#privacy`, `#audio-analysis`, `#ADS-B`, `#geolocation`

---

<a id="item-3"></a>
## [《自然》文章综述机器学习与人工智能在精准医疗预测建模中的新兴应用](https://news.google.com/rss/articles/CBMiX0FVX3lxTE16NWIxdF9vMHNNVGpKbVl4V1dNc1V6VFFNaDU3czQ0TmFoTVFOTWk5RDhJT1N1WmJhVmpUVnl3M25ZazVndVFpYnNYOW5CVXZuMlI1emF3WW94dHdhUDdF?oc=5) ⭐️ 7.0/10

《自然》发表了一篇题为《机器学习与人工智能在精准医疗预测建模中的新兴应用》的文章，系统梳理了机器学习和人工智能方法如何被用于构建精准医疗中的预测模型。文章将这些技术定位为“新兴应用”，而非已经成熟的临床标准，说明该领域仍处于探索阶段。 精准医疗的核心在于把海量、异构的患者数据转化为关于疾病风险、进展和治疗反应的个体化预测，而这正是机器学习最擅长的方向。一篇发表在《自然》上的综述之所以重要，是因为它有助于设定研究议程、指出哪些人工智能方法正在走向临床落地，并提醒人们关注这些模型在真正应用于患者之前必须解决的验证与公平性问题。 由于目前公开可获取的信息只有标题和发表平台，文章所讨论的数据集、模型架构、基准测试结果以及验证策略等具体内容尚无法确认。读者应将其视为对新兴应用的高层次综述，而非某个单一新模型或临床试验的成果报告。

google\_news · Nature · 11月3日 17:18

**背景**: 精准医疗是一种针对个体患者定制预防与治疗方案的思路，通常把基因组和分子层面的数据与临床记录、影像以及生活方式信息结合起来，而不是依赖“一刀切”的诊疗指南。在此语境下，预测建模指的是利用统计与计算方法，为特定患者估计疾病易感性、可能的药物反应或不良事件风险等结果。机器学习（包括深度学习及相关人工智能技术）之所以在此具有吸引力，是因为它能够在规模庞大、质量参差的数据中捕捉传统统计模型难以刻画的复杂非线性模式。这篇《自然》文章探讨的正是这类模型如何开始在精准医疗的各个方向落地，以及从有前景的研究结果到常规临床使用之间还存在哪些障碍。

**标签**: `#machine learning`, `#precision medicine`, `#predictive modeling`, `#healthcare AI`, `#Nature`

---

<a id="item-4"></a>
## [阿里巴巴在乌镇峰会宣布开源 470 余个 Qwen 模型](https://www.aibase.com/news/32046) ⭐️ 7.0/10

在 11 月 3 日开幕的 2026 年世界互联网大会乌镇峰会上，阿里巴巴集团主席蔡崇信表示，公司已开源超过 470 个 Qwen 模型，全球累计下载量突破 40 亿次，并衍生出超过 33 万个衍生模型。蔡崇信认为，在 AI 需求持续上升而算力供给紧张的背景下，只有开源才能让 AI 真正普及。 这一数据使阿里巴巴的 Qwen 系列跻身全球规模最大的开放权重模型生态之一，对创业公司、研究机构和企业如何基于基础模型进行二次开发具有举足轻重的影响。蔡崇信将开源定位为中小企业和发展中国家的必需品，也进一步凸显了其与美国闭源、仅提供 API 的模型厂商之间的路线差异。 此次公布只是对生态累计数据的简要披露，并非发布新模型，也没有说明具体许可证条款、基准测试成绩，或哪些参数规模的模型贡献了主要下载量和衍生模型。Qwen 覆盖从适合边缘设备的小参数模型到超大规模旗舰系统的众多开放权重模型，部分较新版本的许可证带有研究用途或商业使用的附加条件。

aibase · AIbase · 11月3日 14:01

**背景**: Qwen（通义千问）是阿里云推出的大语言模型与多模态模型系列，主要以开放权重方式发布，任何人都可以下载、运行并微调。在开放权重生态中，“衍生模型”指通过对现有模型进行微调或其他改造而构建的新模型，因此衍生模型数量多说明开发者不只是下载模型，而是在其上积极进行二次开发。阿里巴巴正以开放权重路线对标 OpenAI、Anthropic 等将模型权重封闭、仅通过 API 售卖访问权限的厂商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1">Qwen - Alibaba Cloud</a></li>
<li><a href="https://huggingface.co/blog/daya-shankar/open-source-llms">Best Open-Source LLM Models in 2026: Coding, Local, Agentic ...</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#Alibaba Qwen`, `#LLM releases`, `#AI adoption`, `#China tech`

---

<a id="item-5"></a>
## [AWS 演示 ServiceNow 与 Bedrock AgentCore Gateway 的 OBO 令牌交换](https://news.google.com/rss/articles/CBMitwFBVV95cUxNNGFWNmVfdHl0UjFyNXRaLVVHSFZxMUJnUnE2SEpYMjlRdm5PNUJtcU5DbTJGdG93WENBNEh0Y2JMcV9oTFBkYnhSVENnWDJ1V1JZb1pvWjV3SkdYMWREalJSUV9iTVdQVnJaWGt6eTVDVktpeXN5YmJ5RjNVR3VYR3lDaWxfOEFmc0JmUUJZS1lVZEFzMVFBXzVLdS1xTjVpazc1djFvN2pqXzV0UFJYZWhrX2VRTm8?oc=5) ⭐️ 6.0/10

AWS 发布了一篇技术博客，详细介绍了如何配置 Amazon Bedrock AgentCore Gateway 来执行 on-behalf-of（OBO）令牌交换，使 AI 代理能够以已登录用户的身份调用 ServiceNow，并以 Microsoft Entra ID 作为身份提供方。文章给出了完整配置步骤，说明如何将用户身份从代理经由托管网关一路传递到受 OAuth 2.0 保护的 ServiceNow API。 企业级代理只有在以正确的用户权限（而非共享的超级账号凭据）行动时才有价值，因此一套有文档、基于标准的委派模式可以降低代理进入生产环境的安全与合规门槛。由于 ServiceNow 是 IT 与 HR 工作流的核心记录系统，这一模式很可能被在 AWS 上构建代理自动化的团队广泛借鉴。 该实现依赖 OAuth 2.0 Token Exchange（RFC 8693）语义：网关将传入的用户令牌提交给身份提供方，换回一个面向 ServiceNow 的下游令牌，而不是用静态客户端凭据冒充用户。这是一篇厂商教程而非产品发布，读者需注意它依赖正确配置的 Entra ID 应用注册、ServiceNow OAuth 提供方以及网关目标凭据。

google\_news · Amazon Web Services \(AWS\) · 11月3日 16:47

**背景**: on-behalf-of 令牌交换是一种 OAuth 2.0 模式：中间层服务把从用户处获得的一个访问令牌，换成对下游 API 有效的新令牌，从而在跨服务调用时保留原用户的身份与授权范围，而不是把所有请求都归结到一个服务账号上。Amazon Bedrock AgentCore Gateway 是一项全托管的 AI 网关，为代理访问工具、其他代理和大语言模型提供统一的安全入口。ServiceNow 通过受 OAuth 2.0 保护的 REST API 开放其平台能力，因此代理必须先取得范围正确的令牌，才能读取或修改记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway/">ServiceNow on-behalf-of token exchange with Bedrock AgentCore ...</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html">Amazon Bedrock AgentCore Gateway: A secure AI gateway for ...</a></li>
<li><a href="https://oauth.net/2/token-exchange/">Token Exchange — OAuth 2.0</a></li>

</ul>
</details>

**标签**: `#AWS`, `#Bedrock AgentCore`, `#token exchange`, `#ServiceNow`, `#AI agents`

---

<a id="item-6"></a>
## [谷歌据报威胁切断拒绝 AI 工具学校的搜索访问](https://news.google.com/rss/articles/CBMimwFBVV95cUxPMTJTT21ORUV6YU5BVzlrTGp1RWh6UkF5UjlZekp3ZkpWczJJa01FcTFXZE9CTFJiNDRNdkxiNGZaRHh5YjVSZEFrR19QWmVRVU11WU9uZGlnb0J6RkFLRF96bkFCOVRKV0NkM2RsbzNveU9vd3N5Y1hKci1ITE5aRXhCRWlkNHplZV9VZG1iNWh6amxDeEl5SnVXZ9IBoAFBVV95cUxOd1REeXBYNGROYkEzUjFaR2hWQnZUVmZZS2I2bG9yRXRpSnE1MTJhMHRRMVozMmlWaWpXXzVkUUZicTdwY2ZyV2k5TEZSVExGVHpLSnZzQnZsMng1dDVZZkhMZWRzRWthYjZKb0hxc3NlejBzbG9rYUlzX0JNMU52LWF4VjcyOVVsUWdmd182LTdSV3czWlhWanYzZ0pMNGpN?oc=5) ⭐️ 6.0/10

据 ABC News 和 CBS News 报道，谷歌将切断拒绝采用其 AI 工具的学校的学生搜索访问权限，作为与其教育产品捆绑的条件。 若属实，此举将把谷歌搜索作为推动 Gemini 进入课堂的筹码，并加剧外界对教育科技领域捆绑销售和反垄断问题的担忧。 相关报道尚未说明涉及哪些具体 AI 工具、哪些搜索产品以及时间表，谷歌也未确认已公开相关政策；受影响的服务似乎与 Google Workspace for Education 相关，其 Fundamentals 版本对符合条件的教育机构免费，而 Standard 和 Plus 为付费版本。

google\_news · ABC News - Breaking News, Latest News and Videos · 11月3日 21:38

**背景**: Google Workspace for Education 是谷歌面向学校提供的课堂与生产力套件，包含 Classroom、文档等服务和搜索访问。Gemini for Education 则是谷歌用于备课、研究和学习的 AI 助手。反垄断中的“搭售”指企业将一种产品的获取条件与另一种产品捆绑；当占主导地位的企业利用市场力量排挤竞争对手时，这类安排可能受到审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://edu.google.com/ai/gemini-for-education/">Empower Learning with Gemini for Education - Google for Education</a></li>
<li><a href="https://knowledge.workspace.google.com/admin/getting-started/editions/google-workspace-for-education-faq">Google Workspace for Education FAQ</a></li>
<li><a href="https://businesslawreview.uchicago.edu/online-archive/potential-antitrust-implications-tying-hardware-ai">The Potential Antitrust Implications of Tying Hardware with AI</a></li>

</ul>
</details>

**标签**: `#Google`, `#AI in education`, `#antitrust`, `#tech policy`, `#Search`

---

<a id="item-7"></a>
## [ROSS Intelligence 请求美国上诉法院重审 Westlaw 人工智能版权案](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQVlpSeFllQ2xDRC01a3o4UkdQVy1xb1hBU0tmUnJIQWtsMmM2RndmMlVoYW9VRGNkdnNiQmktWkktYUdQQ1lPMVR5SHVnYUpFWkdVTWY5c0h4VmswXzdJQW1PMlVRcHlsMFl3Z2dxQ1c3aDBveXUycWZaTkNtNzh2RHdGUUVXYVp3Vy0tZkxHTjBuSUE0VmxKQlhBQ1NqQ093SS1ENmxzcjdiRDBaRnNzVTZ6QnQwa1VZZWRWbmhqRGlPOUlmb0RQUGQ0elpHV3BzNEt1VF930gFaQVVfeXFMTlBJdGVnbmNoWTRlSzZpMWF4NTF2bk5GVU95aGdfbFBKVEVhZmVJVWZhcExYbWJFZjlwd09sV2JwT1BXYU1kTFNnOW91SUhROTdkS2NfcnRiTGF3?oc=5) ⭐️ 6.0/10

据 MLex 报道，ROSS Intelligence 已向美国一家联邦上诉法院提出请求，要求重新审理（据报道为复核或再次听证）其与汤森路透（Thomson Reuters）之间围绕使用 Westlaw 内容训练其人工智能法律检索工具的长年版权纠纷。该申请是在此案此前一系列裁决之后提出的，案件核心在于：复制 Westlaw 由律师撰写的判例摘要（headnotes）来打造竞品 AI 产品是否被允许。 这是美国最早关于“受版权保护的材料能否用作 AI 训练数据”的合理使用之争之一，因此其结果可能为生成式 AI 开发者确立先例，影响范围远超法律检索领域，包括他们如何获得授权或抓取专业数据库。无论最终如何裁决，都会受到专有数据集出版商以及基于这些数据构建产品的 AI 公司的高度关注。 争议焦点在于 Westlaw 的“判例摘要”（headnotes）——由律师撰写的简短判例要点——据称 ROSS 是通过一家法律数据供应商获取的；同时争论 ROSS 的使用是否具有“转化性”，因为其产品与 Westlaw 直接竞争。此次上诉请求的具体依据（例如申请合议庭重审或全院庭审）由 MLex 在其付费墙后报道，现有材料中并未给出完整裁判文书原文。

google\_news · MLex · 11月3日 20:51

**背景**: 汤森路透于 2020 年起诉 ROSS Intelligence，指控这家初创公司通过复制 Westlaw 的判例摘要、而非自行分析来构建其 AI 法律研究助手；ROSS 则主张其属于合理使用，因为这些文本被用作训练数据，并未直接展示给用户。2023 年，特拉华州一家联邦法院在简易判决中驳回了该合理使用抗辩，此后案件一直处于上诉程序中。更大的背景是美国涌现出一波 AI 版权诉讼——包括作家和新闻出版商起诉 OpenAI、Anthropic 和 Meta——法院已开始区分“使用合法获取的材料进行训练”与“复制盗版或专有内容”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://legal.thomsonreuters.com/en/westlaw">Westlaw – Legal Research Platforms | Thomson Reuters</a></li>
<li><a href="https://www.rossintelligence.com/about-us">About Us - ROSS Intelligence</a></li>
<li><a href="https://www.arl.org/blog/training-generative-ai-models-on-copyrighted-works-is-fair-use/">Training Generative AI Models on Copyrighted Works Is Fair Use ...</a></li>

</ul>
</details>

**标签**: `#AI law`, `#copyright`, `#legal tech`, `#ROSS Intelligence`, `#Westlaw`

---

<a id="item-8"></a>
## [微软 AI 负责人：若 AI 显现意识迹象应停止开发](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPSkhPbUZZN19BZWNLaWdlODZyeTdwQUIxNDZ5RzBtSWh1c3pLNV9yR3l2eXVVNG0zZkgyUmJ4aXdfM1NFUGdvY3pGakc4Q0hQdnNjTk5ZRHBsUldDZHZXUXUyUTJOLUhnRGthMlFyaWIyQ0hHeXhyMmFzTmNFdzZQWnNDazluVHRNNTM3c29HWFJDT1lYZktOVWRBcTJETWFiS203Xy16QUFVTm1IOHU2VktDd0pzNTgwTFRLRFpNWWtIMG5iQlBnYm9DN1g0Wi1fZ2Jr0gHYAUFVX3lxTE1QSWFheXZZbjVLdGNEOHJsei1XMG5jVm1HQTkteGd6a09kUy1NSlA0ZGZhSjJFYnVOZG55dVdjcGtPMzYyc3JURy16bU1XR0JoT1hleHNHUngyajhGWVNkS016cGVXV3dzMS05Wm1hWFpwM1gwVHY4YUZBOTh5aXFEeklXYXNBVDRoOXJvSzZ6T0Z3enpsYzNGYk1KMFh1TWMzZTZJOVBXUzU0RlRkRU85cDJ5VExIUS1VUy1JVlFnRDVwUEpHNjNTenhQZ1VmYVp1a1ZYUDhSXw?oc=5) ⭐️ 6.0/10

据报道，微软 AI 负责人表示，如果人工智能系统开始显现意识迹象，就应停止 AI 开发。Wccftech 报道了这一说法，但目前链接内容只有标题，没有更多细节。 这一表态为 AI 安全与 AI 福祉辩论增添了重要的行业声音；相关讨论常围绕生存风险或先进系统的道德地位来主张暂停或放缓开发。若被视为政策信号，它可能影响 AI 实验室如何设定内部停止条件，以及监管机构如何开展前沿模型监督。 该报道没有说明什么算作“意识迹象”、由谁以及如何作出判断，也没有说明暂停是临时还是永久。研究人员提出的是基于理论推导的指标清单，而非单一的决定性意识测试，相关科学问题仍存在很大争议。

google\_news · Wccftech · 11月3日 12:20

**背景**: AI 意识是一个 speculative（推测性）但日益受到讨论的话题：目前尚无公认的科学测试来判断机器是否具有意识，研究人员也警告，流畅的行为可能模仿自我意识，却不能证明存在内在体验。一种有影响力的方法是依据人类意识理论提取“指标属性”，用清单式评估而非单一的是否通过测试来考察 AI 系统。这场辩论还与 AI 福祉和政策问题相关，涉及先进系统的道德地位，以及开发者应在何时暂停或重新评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.science.org/content/article/if-ai-becomes-conscious-how-will-we-know">If AI becomes conscious, how will we know? - Science | AAAS</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1364661325002864">Identifying indicators of consciousness in AI systems</a></li>
<li><a href="https://arxiv.org/pdf/2408.04771">AI Consciousness and Public Perceptions: Four Futures...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI consciousness`, `#Microsoft`, `#AI ethics`, `#AI policy`

---

<a id="item-9"></a>
## [美国科技巨头隐性 AI 债务半年激增 90%至 3.2 万亿美元](https://news.google.com/rss/articles/CBMixwFBVV95cUxQY2ZaWEJmWkg2SkRXRVB0Y3VReEpxb0FWYlFIT3ZoMllPSWRPNjlpcGdrTjdET19TUjdXXzhIdzZpcnFucXB1dUNmZGpmSlBwYXRxR0dZNXRPMk5XeVlKTTUtb2ZaODlJYUh4WlA3NFp5MmswdEhnanFsRF95dlVYNDBJUWxTOWdWSmp6eWxPNE1tNUJXdU1iZVQxaDRpdEVYMG9XdEpQS1U4aFo3aFdXUHduZjlRMlFJelhwMEJLSTZ0cWx0NGFF?oc=5) ⭐️ 6.0/10

据《日经亚洲》报道，美国科技巨头与 AI 相关的隐性债务或表外债务在六个月内增长约 90%，规模达到约 3.2 万亿美元。这一数字涵盖了支撑 AI 基础设施建设、但并未直接体现在公司主资产负债表上的借款与融资承诺。 债务驱动的 AI 基础设施快速扩张，使人们开始质疑：如果回报跟不上支出，当前的 AI 资本开支热潮还能否持续。规模庞大且透明度较低的债务负担，可能放大风险，波及数据中心运营商、贷款机构以及暴露于 AI 供应链的投资者。 所报道的数字涵盖合资企业、租赁和项目融资等表外结构，而非公司直接借款，这也是其被称为“隐性”债务的原因。该报道仅给出了总体规模和增速，对具体涉及哪些公司、金融工具或会计处理方式披露有限。

google\_news · Nikkei Asia · 11月3日 20:02

**背景**: 表外债务是指未直接记入公司资产负债表的负债或融资安排，通常只在财报脚注中披露，这使外部机构难以评估其真实杠杆水平。随着 AI 需求激增，数据中心建设越来越多地通过合资企业、特殊目的载体和项目融资来完成，而非公司直接举债。近期报道援引布鲁金斯学会的研究估计，到 2032 年美国 AI 基础设施投资可能高达 10.3 万亿美元，而越来越多的财务风险正从大型科技公司自身的资产负债表转移出去。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Off-balance-sheet">Off - balance - sheet - Wikipedia</a></li>
<li><a href="https://seekingalpha.com/news/4646489-ai-buildout-could-cost-10_3t-as-financing-risks-move-off-big-tech-balance-sheets">AI buildout could cost $10.3T as financing risks move... | Seeking Alpha</a></li>
<li><a href="https://www.aoshearman.com/en/insights/data-center-insights/how-data-center-financing-rewrites-the-rulebook">Data center financing : funding the next AI infrastructure wave</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#tech finance`, `#capex`, `#debt markets`, `#industry analysis`

---

<a id="item-10"></a>
## [LG 新能源将电池产能转向 AI 数据中心储能](https://www.aibase.com/news/32058) ⭐️ 6.0/10

LG 新能源首席财务官李昌实（Lee Chang-sil）在 11 月 3 日的财报电话会议上表示，公司的软包式储能系统（ESS）产能将在年底前超过 50GWh，并在明年突破 70GWh，标志着公司正从增长放缓的电动汽车业务转移重心。公司第三季度 ESS 在手订单达到 160GWh，并正在与公用事业公司和超大规模数据中心运营商进行谈判。 这一举措表明，AI 数据中心的建设正成为足够大的需求来源，足以让电池制造产能从电动汽车领域重新分配，这可能缓解电动汽车电池制造商面临的产能过剩压力。如果其他主要电芯厂商跟进，储能有望在电动汽车普及放缓的背景下成为整个行业的结构性增长市场。 这些产能数据具体指的是软包（pouch）电芯，这是一种采用扁平柔性封装的设计，通常因散热效率和空间利用率较高而受青睐，有别于圆柱形或方形电芯。160GWh 是在手订单规模而非营收，而与公用事业公司及超大规模数据中心运营商的交易目前仍被描述为洽谈中，尚未签署。

aibase · AIbase · 11月3日 18:01

**背景**: 软包电芯是锂离子电池三大主要形态之一（另外两种是圆柱形和方形），采用柔性箔材封装，适合堆叠式、高空间利用率的电池包。储能系统（ESS）如电池储能系统（BESS）可以帮助数据中心削峰填谷、平滑功率波动，并整合备用电源或可再生能源。超大规模数据中心——拥有数千台服务器、耗电规模达数十至数百兆瓦的设施——正推动电力需求快速增长，尤其是在 AI 训练负载方面，这使得现场储能和电网级储能成为运营商的重点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.batterydesign.net/battery-cell/formats/pouch-cells/">Pouch Cells - Battery Design</a></li>
<li><a href="https://elehub.com/data-center-energy-storage/">Data Center Energy Storage: The Role of BESS in Reliable and ...</a></li>
<li><a href="https://www.ibm.com/think/topics/data-centers">What Is a Data Center ? | IBM</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#energy storage`, `#data centers`, `#LG Energy Solution`, `#EV batteries`

---