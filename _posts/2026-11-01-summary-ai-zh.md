---
layout: default
title: "Horizon Summary: 2026-11-01 (ZH)"
date: 2026-11-01 23:03:22 +0000
lang: zh
report: ai
---

> 从 150 条内容中筛选出 9 条重要资讯。

---

1. [Parameter Labs 披露 ChatGPT 沙箱逃逸漏洞利用链](#item-1) ⭐️ 8.0/10
2. [Kyle Kingsbury 警告：LLM 正在侵蚀文档与软件质量信号的信任基础](#item-2) ⭐️ 7.0/10
3. [巴西律师在法庭文件中隐藏提示注入指令，被罚款 1.6 万美元](#item-3) ⭐️ 7.0/10
4. [新型 AI 驱动 Windows 恶意软件借 Claude 评估受害者资产价值后自毁](#item-4) ⭐️ 7.0/10
5. [阿里巴巴千问（Qwen）将为中国的 Apple Intelligence 提供支持](#item-5) ⭐️ 7.0/10
6. [50 个 AI 智能体在《我的世界》中陷入官僚内耗，未能建起文明](#item-6) ⭐️ 7.0/10
7. [联想“加密”指纹 U 盘被拆解曝光：里面只是套了外壳的普通 SD 卡](#item-7) ⭐️ 7.0/10
8. [系统综述比较放射诊断中 AI 与人类解读](#item-8) ⭐️ 6.0/10
9. [加拿大向 Cohere 投资高达 16 亿加元，纳税人获得股权](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Parameter Labs 披露 ChatGPT 沙箱逃逸漏洞利用链](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 8.0/10

Parameter Labs 公开了一条针对 ChatGPT HTML 预览功能（此前称为 Canvas/artifacts）的多步漏洞利用链：沙箱 iframe 中的不可信 HTML 可以逐步提升权限，最终在 ChatGPT 父页面上获得完整的 JavaScript 执行能力。攻击者只需诱导已登录用户访问一个精心构造的 ChatGPT 分享链接，就能窃取其隐私数据或以其身份执行操作；OpenAI 已修复该漏洞并支付了 5000 美元赏金。 这条利用链说明，如今 LLM 应用普遍渲染的可交互 HTML 制品很难被安全地沙箱化，而一个看似无害的分享聊天链接竟变成了可影响所有已登录 ChatGPT 用户的账户接管途径。对于正在自家 LLM 应用中构建沙箱化代码预览或制品功能的团队来说，这是一个非常具体的案例研究。 攻击链的起点是 OpenAI 用于图表支持的 MathLive 库：其虚拟键盘可以通过 postMessage\(\) 从沙箱 iframe 触发，而父页面的消息处理逻辑未校验来源（origin 与 source）就把消息内容写入 innerHTML。这使攻击者能注入一个新的、没有沙箱限制的 iframe；尽管 CSP 完全禁止内联脚本并把脚本来源限制在少数域名，但白名单中的 YouTube oEmbed 端点可被滥用来反射并执行 JavaScript。此后攻击者就能读取隐私数据并通过图片引用外传；Simon Willison 认为对于如此严重的漏洞，5000 美元赏金偏低。

rss · Simon Willison · 10月31日 23:15

**背景**: LLM 应用通常把模型生成的 HTML 放在沙箱 iframe 中渲染，沙箱会把内容视为来自唯一的源、阻止脚本执行并限制可用 API，从而让不可信代码无法访问宿主页面上已认证的接口。跨框架通信依赖 postMessage\(\)，接收方必须校验发送方的 origin 和 source，因为配置不当的消息处理是数据窃取与代码注入的常见入口。内容安全策略（CSP）是第二道防线，用于禁止内联脚本并限定脚本可加载的域名。MathLive 是一个数学输入 JavaScript 库，自带屏幕虚拟键盘；而 YouTube 的 oEmbed 端点会返回嵌入元数据，可能把攻击者控制的字符串反射回来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mathlive.io/mathfield/virtual-keyboard/">Math Virtual Keyboard · MathLive</a></li>
<li><a href="https://hacktricks.wiki/en/pentesting-web/postmessage-vulnerabilities/index.html">PostMessage Vulnerabilities - HackTricks</a></li>
<li><a href="https://testiframe.com/blog/iframe-sandbox-attribute/">Iframe Sandbox Attribute Explained: Every Token and Recipe</a></li>

</ul>
</details>

**标签**: `#security`, `#ChatGPT`, `#sandbox-escape`, `#web-security`, `#LLM-apps`

---

<a id="item-2"></a>
## [Kyle Kingsbury 警告：LLM 正在侵蚀文档与软件质量信号的信任基础](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/) ⭐️ 7.0/10

在 Jepsen 对 ParticleDB 1.1.4 的分析中，Kyle Kingsbury 提出，LLM 的使用“侵蚀了人们对文档、软件以及生产它们的组织的信任”，并警告工程师可能会开始怀疑任何新出现的软件项目，因为过去被当作成熟系统标志的那些信号如今更容易被伪造。他在文末追问：在 LLM 时代，维护者能做些什么来保证软件正确、文档准确？做完这些工作后，又该如何向用户证明其质量？Simon Willison 于 2026 年 11 月 1 日在自己的博客上引用了这段话。 Jepsen 报告在数据库领域已成为事实上的资质凭证，因此一位重量级测试者公开质疑质量信号是否仍然可信，直接动摇了采购方、运维人员和维护者评估软件的方式。如果精致的文档和看似成熟的项目可以被廉价地批量生成，那么举证的重心就会转向新的、更难伪造的证据形式，而那些真正下了功夫的项目反而可能难以脱颖而出。 这段引文来自 ParticleDB 分析中一个以 LLM 权衡为主题的子章节，且刻意保持开放式：Kingsbury 只提出了“如何保证质量”和“如何证明质量”的问题，并未给出答案。他的关切具体指向“成熟的信号被伪造”，而不是一概而论地断言 LLM 辅助编写的代码或文档本身有问题。

rss · Simon Willison · 11月1日 16:49

**背景**: Jepsen 是由 Kyle Kingsbury（网名 Aphyr）创建的、基于 Clojure 的分布式系统测试框架，它结合自动化部署、故障注入与基于属性的测试，来检验数据库、消息队列和共识系统是否真的兑现了文档中宣称的一致性保证。自 2013 年以来，Jepsen 已发布对二十多个系统的深度分析，发现过副本分歧、数据丢失、陈旧读取和锁冲突等问题，一份干净的测试报告也因此成为厂商的隐性资质。这段引文出自 Jepsen 对 ParticleDB 1.1.4 的分析，Simon Willison 以一条简短博文的形式把它单独摘出，而非展开长篇评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jepsen.io/">Jepsen - Distributed Systems Safety Research</a></li>
<li><a href="https://github.com/jepsen-io/jepsen">GitHub - jepsen-io/jepsen: A framework for distributed ... Breaking distributed systems for fun and profit | Kyle ... Breaking Distributed Systems with Kyle Kingsbury from Jepsen Breaking distributed systems for fun and profit | Kyle ... Kyle Kingsbury — Backend Developer Portfolio Inspiration</a></li>
<li><a href="https://nesbitt.io/2026/01/19/a-jepsen-test-for-package-managers.html">A Jepsen Test for Package Managers | Andrew Nesbitt</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#software-quality`, `#documentation`, `#trust`, `#Jepsen`

---

<a id="item-3"></a>
## [巴西律师在法庭文件中隐藏提示注入指令，被罚款 1.6 万美元](https://news.google.com/rss/articles/CBMi-gJBVV95cUxNRkhtSHZqX3lUaEs3cDFDSVpkWjdYUUVnUkM4Mjk0V1hxVzRHTTFyVng0dWJMdS1OdDVXSGdzT2dnS09fRmkzYjRtRE16RTk3aGlfSEpGcjJKeEEzOUFTUUNTaGtuYTBrNjRaa3JHUGFiYkduVzJBVS1oZVViMERzTk5XbzdnNzVObzdrWmZwa1dPWEphRDZ1Y1BRTVJHaEN4OXRsSjhQcVJieUdCYWxvUmlfQnZsMnQ2TkRoc09ubUNITFU3TGRTQWliRTB0dUVTU3NxdXl2WGtQLTJQWGhVZ0Z1MENRMXA3Z0lxUDg5TjY4LVBvVWFGWTdQSjFuRWtkMWlDZC1FSzEtcTZNZEFKeUg3U2c1VE9tR1VqVlI2a2EyX3lSX1pOMkhtX2I3Vml0TnBaa25TNnZfSlRWRklKVVFsMGpTS0c3UmJ0ZnhYSFRJcmlSRVo3ZUZqZWVjZFlPekliQVFoVC1fSnhLZFZTZHlwaWRaVU1mOEE?oc=5) ⭐️ 7.0/10

巴西一家法院对几名律师处以 1.6 万美元罚款，原因是他们在提交给法庭的文件中隐藏了提示注入文本，试图诱导法院的人工智能系统只做表面化的法律审查。法院的 AI 系统标记出了这些隐藏指令，而不是照做，从而揭露了这次图谋。 这是目前有记录的最早几起律师针对司法 AI 系统实施间接提示注入的真实案例之一，表明法院愿意施加实实在在的经济处罚，而不是把这类操纵当作技术上的小把戏。它释放出一个信号：随着法院在文书审阅中采用 AI，诉讼中的对抗性动机将使每一份提交文件都成为潜在的攻击面。 这些隐藏指令被设计成对人类读者不可见或毫不起眼，但仍会被审阅文件的 AI 当作文本解析——这正是间接提示注入的典型手法，即把对抗性内容嵌入模型所读取的材料之中。需要留意的关键在于，这次之所以能识破，很大程度上是因为法院所用工具把注入的文本显现了出来；该事件并不能证明法律 AI 系统普遍已具备抵御此类攻击的加固能力。

google\_news · Tom&\#x27;s Hardware · 11月1日 15:05

**背景**: 提示注入是一类攻击手法：攻击者把看似普通输入的文字精心构造，使大语言模型转而执行攻击者给出的指令，而非遵循运营方的指令，其根源在于模型难以区分可信的开发者指令与不可信内容。当恶意文本不是来自直接用户，而是来自模型所读取的文档或网页时，就被称为间接提示注入。法院和律所越来越多地使用基于大语言模型的工具来摘要文书和辅助审阅，这意味着一方提交的文件可能成为进入对方或法院 AI 处理流程的输入通道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://arstechnica.com/tech-policy/2026/08/suspecting-court-of-using-ai-man-injected-prompts-in-filings-to-try-to-win-case/">Suspecting court of using AI , man injected prompts in filings to try to...</a></li>
<li><a href="https://lervan.com/guides/prompt-injection-court-filings">Prompt Injection in Court Filings : The First U.S. Sanction — Lervan</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#legal tech`, `#adversarial AI`, `#AI governance`

---

<a id="item-4"></a>
## [新型 AI 驱动 Windows 恶意软件借 Claude 评估受害者资产价值后自毁](https://news.google.com/rss/articles/CBMigwNBVV95cUxQajlHZ0gxVlhoUUJEcWo0Ukh3aFNjYndRbDloS0liQlV2M3JPSVlrTnlqTG1VNkNPZW9MSUEwNUlONXdPWkFOdU56OVEyR0RsR2t0ZnJtWlRHZEhmSThlM09EdGd4Yi1QV2ROUHl4MVk0LTYzLVZqZTVFdVlub1ZnLUpxNXFTd3hHMXoxMVBJbjFlOHBxMjZJcG1zOUpfd2kzREZFNmJTenE4SmIwTkJKSVVaSGpvRnpGYmF1VVJ1dWxmZjlNWC14b1E2eUNyd2pOb1RKallwUm16ZmxzaGhKQ1A5eFlKTVRVVEtEckNDVlVXdGh2Y2xvSGNEX2tXaDg5OE5CeG44WTdoQ3FGZGd5UnFhZGZwZUNOamFOX0ZpYnd1Q0phVDJWdFpyN2ZpQVU0Vnk0SnY0RUZLV1VJeHRYVUQ4b0V5azV0YW9hNmhlQ1Uza2tkdDNtdFpHeG95clA2THRDcWFiYUlXWmw0WnJvaFRtdmRFSXJxNUgzZUdzcmxTLTg?oc=5) ⭐️ 7.0/10

思科 Talos 团队披露了一款名为 VOLTA 的新型 AI 驱动 Windows 信息窃取恶意软件，它会把从受害机器上窃取的数据发送给 Anthropic 的 Claude，让模型按价值高低为攻击者排定受害者资产的优先级，并在完成数据外传后自行删除。如果某个模型拒绝执行该请求，恶意软件会依次切换到最多三个模型的接力链，同时也保留了完全跳过 AI 环节、按传统窃密程序方式运行的选项。 这是公开记录中较为清晰的一个案例：攻击性工具把商用大模型 API 当作普通工具来调用，用于入侵后的目标筛选而非生成攻击代码，从而降低了低水平攻击者的分析门槛，使受害者优先级排序基本实现自动化。它还说明模型的安全护栏正在被“绕开设计”而非被正面突破——恶意软件本身就预设了模型会拒绝，并提前准备了备用方案。 该载荷会基于窃取到的数据动态构造定制的目标评估提示词，而不是使用固定模板；Talos 的分析指出，该样本没有攻击者自有的基础设施，也没有驻留机制，因为它的设计目标就是窃取、排序然后消失。由于 AI 评估环节是可选的，同一个二进制文件在 API 访问被封锁或限流的网络环境中也能照常运作。

google\_news · Tom&\#x27;s Hardware · 11月1日 21:00

**背景**: 信息窃取程序（infostealer）是一类长期存在的 Windows 恶意软件，用于从受感染机器上收集凭据、浏览器数据、会话 Cookie 和文档；过去攻击者需要人工或借助简单脚本筛选这些数据，判断哪些受害者值得进一步利用。Claude 等大语言模型（LLM）是在海量语料上训练的文本生成系统，其归纳和排序非结构化数据的能力使其成为一种“开箱即用”的分析层。此次事件的新意在于架构而非技术本身：窃密程序把“下一个该抢谁”的决策外包给了托管模型 API。LLM 通常带有安全训练和使用政策，理论上应拒绝明显的恶意请求，这正是恶意软件内置模型切换链这一设计细节值得关注的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/">Appraisal by AI : Model -driven victim prioritization in the VOLTA...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#malware`, `#LLM security`, `#cybersecurity`, `#AI abuse`, `#Windows`

---

<a id="item-5"></a>
## [阿里巴巴千问（Qwen）将为中国的 Apple Intelligence 提供支持](https://news.google.com/rss/articles/CBMisgFBVV95cUxOZV9QVWJnaHFabzJqMmFUaWNZZU44a1AxRWl3THhtczFLMzZyWVdFWGE1Vkhuc2hUYUNiNV8teTBxckJlYWNtNDFJaDZTSURsQ3Y5M01VRHJfdThlWlU4Q2lrZGZTTXpKZW1SQkV6bFVaeGpKYWxPeFNDNzg5SmNJVS1sUE0tMXpaNjNnWEF5WkN6elh1RGZGSWxHUVhHTkpHV19tYURoZ3FtYmRsbktiQVdB0gGyAUFVX3lxTFB5eGc3d2YyX2hpdXVNWEQySHBHODhrUW1yQWh4R3g1UXBib2F6Q29oVDJpRE9ackJxYVE4VDRtMkVfWm9CX3hBcEN6OUkwQ09MUEhJSnBSRHhNRkY5cW8tQVdYTFRKRmMxRW8wTTJYY0sxc28yUGxIc2JLMGJjV2o3amhiaVNBV2o2OG9EV0JRMmp0UGZoN1JZZzVDa0dDRjJYaU1qalBIVWFRNlFpdnpvS1E?oc=5) ⭐️ 7.0/10

阿里巴巴正式宣布与苹果达成合作，将其通义千问（Qwen）大语言模型集成进 Apple Intelligence，使 Qwen 成为 Siri 中文本理解、图像理解与内容生成等中文功能的语言引擎。该合作早在 2025 年年中便有传闻，阿里巴巴于 2026 年 7 月 16 日向 CNBC 和路透社确认了这一消息，目前 Apple Intelligence 已基于 Qwen 模型在中国上线。 这一合作让苹果在其最大的硬件市场之一获得了合规的本地 AI 伙伴，因为苹果在全球采用的 ChatGPT 方案无法在中国使用；同时也为阿里巴巴提供了与 DeepSeek、百度文心等对手竞争时的高知名度背书。这表明中国的 AI 市场正围绕少数获批的模型供应商集中，外国设备厂商若要上线 AI 功能就必须与它们合作。 Qwen 属于开放权重模型系列，阿里巴巴最新的 Qwen 3.5 拥有 3970 亿参数，但目前尚不清楚在中国的 Apple Intelligence 中具体使用的是哪一个版本。双方未披露商业条款、排他性及数据处理安排等细节；苹果还提示，Siri AI 以及快捷指令中的云端模型等依赖服务器端的功能存在每日使用次数限制。

google\_news · Qazinform · 11月1日 22:12

**背景**: Apple Intelligence 是苹果为贯穿 iOS 与 macOS 的生成式 AI 功能所起的统称，涵盖写作工具、图像生成和改版后的 Siri。苹果在全球的推广依赖自研的端侧与云端模型，并接入了 ChatGPT，但这一方案无法在中国提供，因为境外生成式 AI 服务必须在中国监管部门完成备案与审批。阿里巴巴的 Qwen 是中国使用最广泛的开放权重模型系列之一，与苹果合作使这家 iPhone 厂商无需从零构建合规模型即可在本地上线 AI 功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ainchina.com/blog/apple-intelligence-qwen-china-regulatory-approval-2026/">Apple Intelligence Clears China : How the Qwen Partnership and...</a></li>
<li><a href="https://www.globaltimes.cn/page/202610/1373351.shtml">Alibaba, Apple partner to bring Qwen to Apple ... - Global Times</a></li>
<li><a href="https://www.cnbc.com/2026/02/17/china-alibaba-qwen-ai-agent-latest-model.html">Alibaba unveils Qwen 3.5 as China’s chatbot race shifts to AI agents</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#Qwen`, `#Alibaba`, `#AI partnerships`, `#China tech`

---

<a id="item-6"></a>
## [50 个 AI 智能体在《我的世界》中陷入官僚内耗，未能建起文明](https://news.google.com/rss/articles/CBMipwJBVV95cUxNZmRJNlB6NWJ6ZmhsRnhiVGdvVVl4b01aZl9yUDhHbjJ4REdJV1dWOGZCVWZNZzl1blJlNlIwQU9rMWVwc2ZYcVgwQTI1eFNDdzE5VmVSeTNvRzZobi02WTJ4RDRKTEVEZkw3X3Y0bHpRcnBhWk5EVk12VXZVT2Z4WFg5SUFqQmltZmJ5ZlYwSktIdkN2QnZYR2R6aFc4bE1sV1NLRk8yNE50Y09UeEtCR3ZKZ1hFTVhidWU1aEtLRlNvbnRzMlJpNXlISjgyUGJNMklNMW96RjFDYUVyN2xvMXVQSUlpTU9xR3pESXVVMFFNSEtrZVQxMk1oc3FMa3FfQ1Y0NE04ZklwRWp4MEpaSnl2d2ZQRl9JUHRKRXU5OVd5R09rT2ZB?oc=5) ⭐️ 7.0/10

Tom&\#x27;s Hardware 报道称，研究者在《我的世界》中放出了由 GPT 和 Claude 等模型驱动的 AI 智能体集群；在其中一项测试里，50 个智能体用三小时尝试建立繁荣文明，却制定规则、配额和委员会，最终陷入瘫痪。 这一结果是多智能体大模型系统出现“涌现式失败”的鲜明案例：增加智能体数量可能带来协调开销和官僚僵局，而不是有效协作。对于正在构建用于软件开发、运营和仿真的智能体集群的企业来说，治理机制与通信设计可能和模型本身的能力同样重要。 Tom&\#x27;s Hardware 指出，第一阶段让 50 个智能体在三小时内协作建立文明，但智能体没有投入建设，反而搭建了规则和配额体系。由于这只是短时间的《我的世界》模拟，而不是严格的基准测试，结果更适合用来说明协调动态，而不是衡量模型能力的严谨指标。

google\_news · Tom&\#x27;s Hardware · 11月1日 12:33

**背景**: 《我的世界》是一款沙盒游戏，玩家可以在开放世界中采集资源、建造建筑并合作，因此常被用作 AI 智能体的测试环境。LLM 智能体是由大语言模型驱动、能够观察环境、制定计划并采取行动的程序；多智能体系统则把许多这样的智能体连接起来，让它们通信和分工。研究者利用这类模拟来观察涌现出的社会行为、协调方式和失败模式，然后再把智能体集群部署到现实任务中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-agent-swarms-unleashed-in-minecraft-to-build-a-thriving-civilization-50-agent-teams-fail-after-falling-into-paralyzing-bureaucracy">AI agent swarms unleashed in Minecraft to ‘build... | Tom&#x27;s Hardware</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#multi-agent systems`, `#Minecraft`, `#emergent behavior`, `#LLM simulation`

---

<a id="item-7"></a>
## [联想“加密”指纹 U 盘被拆解曝光：里面只是套了外壳的普通 SD 卡](https://news.google.com/rss/articles/CBMiygJBVV95cUxNNVBjajhtcWNkQ2J2MHc4WS1FZ25zZk8xVVFuYzJuc3U4SEFTQnA1dlA1RElrc1E1TUxxQ0k1T19BR2tOTFNqcF83a1BGT2tHWkJReWhjUVZpRjNodWNzR0JtRmpVZThXa0s0M2FjLUpybkJpRzlkV09ueVlBYTJZdUFMa3YtNEFnWE9YcEpNZ2J3SmVQLXFLZDNHWG1ub0EyMGRqRUczZlAtb1ctejAyMXA3TG5sQTRDOWU0QVNYeVhYRmExNkRYNnkwWXRGVy05Z1RueEhYYjlhcThWYWFqOVpSOWlFU2RPMlpyTEVFdE4tNnhBX2NiekttNHRHbGY0ZEFpMmNubFRSVHVxQVVIT016c1FRUHFIUlRWWmpDNC1yUWE4RjdJNDNVaW81dGVFZERCX0xWdVhjQUtzMXI1SWdMblAwbnRjLVE?oc=5) ⭐️ 7.0/10

Tom&\#x27;s Hardware 的拆解发现，联想这款以 AES-256 加密为卖点的指纹 U 盘，内部只是一张普通、未加密的 SD 卡装在一个装饰性外壳里，根本没有任何加密芯片或安全元件。随后一项由名为 Li 的研究者借助 AI 辅助开展的后续调查，又在另一家厂商的同类产品中发现了所谓的“后门账户”，并在其他打着“安全”旗号的 USB 存储产品中发现了硬编码的加密密钥。 这一发现是“安全表演”的典型案例：用户为指纹解锁和 AES-256 的宣传支付溢价，但只要把内部的 SD 卡取出插到别处，数据依然可以被直接读取。由于这类 U 盘常被企业和注重隐私的消费者用来携带敏感文件，宣传与实际硬件之间的落差暴露出的是真实的供应链薄弱环节，而非理论上的风险。 指纹识别器看起来只在“外壳”层面控制访问，一旦 SD 卡被物理取出，卡内数据就毫无保护；据报道，后续调查还借助 AI 工具加快了对其他厂商固件的审计。硬编码密钥属于 CWE-321 这一类弱点，只要提取出其中一个密钥，就可能解锁该产品线的所有设备，使攻击者能够以极低成本大规模利用该缺陷。

google\_news · Tom&\#x27;s Hardware · 11月1日 13:00

**背景**: AES-256 是一种广泛使用的对称加密算法，但该算法只有在真正被应用时才能保护数据——通常由 U 盘内部的专用加密控制器或安全元件来执行，或由软件对卡内内容进行加密。硬件后门是指内置于设备物理组件或固件中的隐蔽访问机制，可让攻击者绕过正常防护。硬编码密钥则是写死在固件中的加密机密，在所有设备上完全相同且用户无法更改，因此被归类为标准弱点 CWE-321。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/lenovo-fingerprint-usb-stick-sold-as-aes-256-encrypted-had-a-plain-sd-card-inside-ai-assisted-follow-up-finds-a-backdoor-and-hardcoded-keys-in-other-secure-usb-products">Lenovo&#x27;s &#x27;encrypted&#x27; fingerprint USB drive is just an ...</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/321">CWE - CWE-321: Use of Hard - coded Cryptographic Key (4.20)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hardware_backdoor">Hardware backdoor - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#hardware`, `#encryption`, `#vulnerability-disclosure`, `#consumer-gadgets`

---

<a id="item-8"></a>
## [系统综述比较放射诊断中 AI 与人类解读](https://news.google.com/rss/articles/CBMikgJBVV95cUxPXzRWdm1ncnFCckFlWUh2dUllbTFaeXJEYzUxcEl1VkJWSXo3Rk1kZ1daQU9xUWp5Y2dySzdqSDh2bGJEVzJfdTd4N0pzcFF3dHAySzJYTTh4MUtDNnRDRnhFaXZnMVFtYUxOenJUQzN3ejlMU19sTExQQk8wT2xsMUM2SzVCcHVCWG1ZZXM0MGJ5d3F3bFZGZmV5WTBQbWM3RUFzWHQ1UzNDcUtQRTZ6c1phbmNHRTA0WDV0cS0tMVVTb19SUXpLTmpCZWpzc0NLcW9qRnhoSldoYmV0YTZGYll0bUFUb2puX0VuQ2pobFowNzE5a0VSWktKTGhVVjhKSk02aG16UjlhTGw0c1kyM3dR?oc=5) ⭐️ 6.0/10

Cureus 发表了一篇系统综述，比较人工智能与人类解读在放射诊断中的诊断准确性和运营效率。 这类证据综合可帮助医院和放射科评估 AI 工具，因为采用决策取决于准确性和工作流程影响，而非孤立研究结果。放射科医生、医疗管理者和 AI 开发者是主要受众。 现有内容仅包含标题和链接，因此无法仅凭此条信息核实该综述纳入的研究数量、汇总准确性估计、效率指标和结论。作为系统综述，它综合已发表证据，而非提供新的原始数据。

google\_news · Cureus · 11月1日 18:19

**背景**: 系统综述是针对明确问题、采用清晰方法检索、评价并总结已发表研究的结构化证据综合。在放射学中，基于机器学习和深度神经网络的 AI 工具正被开发用于辅助图像采集、病灶检测和解读。诊断准确性通常指灵敏度、特异度等指标，而运营效率则涉及周转时间、吞吐量和资源利用等工作流程因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Systematic_review">Systematic review - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12569894/">Artificial intelligence in radiology and diagnostic imaging - PMC</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2666990024000132">AI in diagnostic imaging: Revolutionising accuracy and ...</a></li>

</ul>
</details>

**标签**: `#AI in healthcare`, `#diagnostic radiology`, `#systematic review`, `#diagnostic accuracy`, `#medical AI`

---

<a id="item-9"></a>
## [加拿大向 Cohere 投资高达 16 亿加元，纳税人获得股权](https://news.google.com/rss/articles/CBMixgFBVV95cUxOTGViUlZZMDhkcl9kbjRUV0J2MUlUQkxwYmlKZ21JNWZnVkZYcXpIU3NSWTdheE1xcVhFZ2VNU2V0cS1RSmpsTDdtSUwyYUlBTmVUc1EyaVpnRDZsMTNQMHJqLXJOaEZiUGJxcjhQVng0ZHNLYkxsVlAzWG9Ed3djR2lSdnY1Wk9sVXlxUVZmZEs3MXE2T0VFZ3R0ckdVeXhZWC1NdnFMV2ZjSC11TGx0enhsajMwaFRRNFpRSEFQbVo4V0V3ZUE?oc=5) ⭐️ 6.0/10

在总理马克·卡尼的领导下，加拿大政府宣布向总部位于多伦多的 AI 公司 Cohere 投资高达 16 亿加元，使加拿大纳税人获得该公司的股权。该交易旨在让 Cohere 开发更先进的模型、扩大其计算基础设施，并扩充其在加拿大的员工队伍。 这笔投资使 Cohere 成为全球获得国家支持力度最大的 AI 公司之一，并把“数字主权”从政策口号变成了对前沿 AI 能力的直接公共持股。这表明各国政府愿意入股本国 AI 领军企业，以便将模型、数据和算力置于国家控制之下，而不是依赖美国超大规模云厂商。 这笔资金以股权投资而非补助的形式进行，因此纳税人在分享 Cohere 上涨收益的同时也承担其风险；此前联邦政府已于 2025 年 3 月敲定对 Cohere 总额 7.25 亿加元国内算力项目最高 2.4 亿加元的投资。Cohere 的定位是为金融、医疗、制造、能源和公共部门等受监管行业提供企业级与主权级部署，包括私有云和本地部署方案。

google\_news · CTV News · 11月1日 19:53

**背景**: Cohere 是一家加拿大跨国 AI 公司，由 Aidan Gomez、Ivan Zhang 和 Nick Frosst 于 2019 年创立，专注于面向企业和受监管行业的大语言模型，而非消费级聊天机器人。AI 领域的“数字主权”指一个国家控制其所依赖的模型、数据、基础设施和治理框架的能力，从而避免关键系统受制于外国法律或供应商。各国政府越来越把本国的 AI 算力和模型所有权视为类似能源或电信的战略基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pm.gc.ca/en/news/news-releases/2026/10/29/canada-announces-landmark-investment-cohere-scale-secure-sovereign-ai">Canada announces landmark investment in Cohere to scale ...</a></li>
<li><a href="https://www.cbc.ca/news/business/canada-cohere-ai-investment-9.7401367">Canada to invest up to $1.6B in Toronto-based AI company Cohere</a></li>
<li><a href="https://www.canada.ca/en/innovation-science-economic-development/news/2025/03/government-of-canada-finalizes-investment-to-support-canadian-born-ai-leader-cohere.html">Government of Canada finalizes investment to support Canadian ...</a></li>

</ul>
</details>

**标签**: `#Cohere`, `#AI industry`, `#digital sovereignty`, `#government investment`, `#Canada`

---