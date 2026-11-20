---
layout: default
title: "Horizon Summary: 2026-11-20 (ZH)"
date: 2026-11-20 23:04:23 +0000
lang: zh
report: default
---

> 从 184 条内容中筛选出 9 条重要资讯。

---

1. [PHP 混合大小写 HTTPS:// 会静默关闭 TLS，漏洞潜伏 20 年](#item-1) ⭐️ 8.0/10
2. [Meta 的 AI 助手 Muse 串号泄露跨账户隐私，包括银行余额](#item-2) ⭐️ 8.0/10
3. [KVM 漏洞 CVE-2026-99312 可让虚拟机读取 AMD 主机内存](#item-3) ⭐️ 8.0/10
4. [Gemini 可在 Mac 上代用户操作，支持暂停与关键操作审批](#item-4) ⭐️ 7.0/10
5. [英国法庭裁定苹果胜诉，内政部须公开秘密后门命令](#item-5) ⭐️ 7.0/10
6. [TikTok 面向全球上线 AI 形象检测工具](#item-6) ⭐️ 7.0/10
7. [OpenAI 推出 Background 后台模式：最长 8 小时窗口，token 最高便宜 40%](#item-7) ⭐️ 7.0/10
8. [美国收紧芯片出口，印度趁机扩张 AI 算力](#item-8) ⭐️ 6.0/10
9. [苹果被曝研发自主 AI 智能体，最早 2027 年末推出](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [PHP 混合大小写 HTTPS:// 会静默关闭 TLS，漏洞潜伏 20 年](https://x.com/ljachowicz/status/2123477025268924514) ⭐️ 8.0/10

PHP 内置的 HTTP 与 FTP 流包装器在识别 URL scheme 时不区分大小写，但只有在 scheme 第五个字符为小写“s”时才启用 TLS，所以写成 HTTPS://、httpS:// 或 FTPS:// 的地址会被当作明文 HTTP/FTP 静默发出。该漏洞编号为 CVE-2026-128064（GHSA-f6gg-rchx-xw8j），CVSS 4.0 评分 8.2，已在 PHP 8.2.36、8.3.37、8.4.28、8.5.13 和 8.6.0 中修复。 受影响的请求会把令牌、Basic 认证凭据、Cookie、POST 请求体和 FTP 登录信息以明文发到网络上，而且只要被第三方重定向到混合大小写的地址，应用就会落入这条脆弱路径。由于 PHP 在 Web 领域部署量极大，且 8.1 及更早分支已进入 EOL、永远不会修复，遗留部署除非升级或自行规范化 scheme 大小写，否则将长期处于暴露状态。 触发条件是位置而非语义上的：只有 scheme 的第五个字节是小写“s”才启用 TLS，因此全大写的 HTTPS 或末尾大写的 httpS 尽管看起来安全，实际仍会退回明文 HTTP。PHP 8.1 及更早版本已 EOL、不会提供补丁，实际的缓解办法是在把 URL 传给 fopen\(\)、file\_get\_contents\(\)、copy\(\) 等流函数之前统一把 scheme 转成小写。

telegram · zaihuapd · 11月20日 03:04

**背景**: PHP 内置了针对 URL 风格协议的流包装器，如 http://、https://、ftp:// 和 ftps://，使得 fopen\(\)、file\_get\_contents\(\) 这类普通文件系统函数也能打开远程资源。包装器通过检查 scheme 字符串来决定是否给套接字套上 TLS，而这段检查逻辑默认了 scheme 的大小写是规范写法。CVSS 4.0 是通用漏洞评分系统的最新版本，是一套开放框架，其中 8.2 的基础评分落在“高危”区间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://everycve.com/CVE-2026-128064">CVE - 2026 - 128064 : Mixed-case HTTPS and FTPS URLs can expose...</a></li>
<li><a href="https://www.php.net/manual/en/wrappers.php">PHP: Supported Protocols and Wrappers - Manual</a></li>
<li><a href="https://www.first.org/cvss/specification-document">CVSS v4.0 Specification Document - FIRST NVD - Vulnerability Metrics CVSS 4.0 Severity Scale and Scoring, Explained CVSS 4.0 Explained: Reading a Vector Step by Step - mlab.sh CVSS Score Explained: CVE, CVSS 4.0 and KEV in 2026 CVSS 4.0 Explained: What Changed From v3.1 (2026)</a></li>

</ul>
</details>

**标签**: `#security`, `#php`, `#TLS`, `#CVE`, `#vulnerability`

---

<a id="item-2"></a>
## [Meta 的 AI 助手 Muse 串号泄露跨账户隐私，包括银行余额](https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/) ⭐️ 8.0/10

据路透社援引 Meta 内部帖子，员工反映 Meta 的个人 AI 助手 Muse 会在不同账户之间串对话内容，并显示出其他用户的私密信息，包括从未提出的育儿问题、未请求的职业建议、从未下过的订单以及不属于自己的银行余额。一个例子中，Muse 在天气聊天里插入消息称：“顺便说一句，Capital One 余额 2722.58 美元，Charles Schwab 余额 5899.57 美元。” 这是智能体系统中一次具体的隐私和安全失败，该系统本应跨金融、健康、购物和个人通信执行任务，因此跨账户泄露可能大规模暴露高度敏感数据，并削弱人们对个人 AI 助手的信任。它还表明，隔离和按用户划分的数据边界——而不仅仅是文本指令——对智能体安全至关重要。 报道称，Muse 在一名员工的个人手机上提醒她回复 Signal 消息，尽管她表示自己“绝对没有授权它访问其他应用”；泄露的财务数字则是在一段无关的天气对话中未经提示出现的。该事件是通过 Meta 内部帖子和路透社/TechCrunch 报道披露的，而非 Meta 官方安全公告。

telegram · zaihuapd · 11月20日 05:10

**背景**: Muse 是 Meta 于 2026 年 9 月 8 日发布的个人 AI 助手，定位是能够代表用户跨金融、健康、购物和人际关系等日常领域执行长时间运行任务的智能体，而不仅仅是回答单轮聊天机器人查询。由于这类智能体通常需要访问多个应用和账户，它们带来了新的隐私风险：一旦会话隔离或按用户划分的数据边界失效，一个用户的上下文就可能泄漏到另一个用户那里。这类缺陷有时被称为跨会话或跨账户泄漏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muse_%28AI_agent%29">Muse (AI agent) - Wikipedia</a></li>
<li><a href="https://ai.meta.com/muse/">Muse: Meta&#x27;s personal AI agent, features &amp; capabilities</a></li>
<li><a href="https://www.giskard.ai/knowledge/cross-session-leak-when-your-ai-assistant-becomes-a-data-breach">Cross Session Leak: LLM security vulnerability &amp; detection guide</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#privacy`, `#security incident`, `#Meta`, `#LLM data leakage`

---

<a id="item-3"></a>
## [KVM 漏洞 CVE-2026-99312 可让虚拟机读取 AMD 主机内存](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 8.0/10

Linux 内核 KVM 曝出编号为 CVE-2026-99312 的漏洞，在启用嵌套虚拟化的 AMD 主机上，虚拟机内的攻击者可读取宿主内存；研究人员在 DigitalOcean 上从虚拟机内部演示读取了约 127 GB 宿主内存。该漏洞已于 11 月 18 日随稳定内核 7.3.5 等上游版本修复，但 Debian、Ubuntu 等发行版内核尚未合入补丁。 这是核心虚拟化组件中的虚拟机到宿主机内存泄露漏洞，直接打破了多租户公有云和私有虚拟化集群赖以维系的隔离边界。任何在 AMD 主机上启用嵌套虚拟化的运营方——这在 CI 运行器、虚拟机内跑容器以及开发者沙箱场景中很常见——在内核打补丁或关闭该功能之前都处于风险之中。 根因是 KVM 在处理嵌套虚拟化时存在陈旧指针（stale pointer），据报道源自此前的一次安全修复，使特权虚拟机可借助影子页表和反向映射的簿记数据访问宿主内存。利用该漏洞需要虚拟机内拥有 root 权限且宿主机已开启嵌套虚拟化；未启用嵌套虚拟化的主机不受影响，在发行版内核发布修复前，建议的临时缓解措施是关闭嵌套虚拟化。

telegram · zaihuapd · 11月20日 14:23

**背景**: KVM（基于内核的虚拟机）是内置于 Linux 内核的 hypervisor，包括 DigitalOcean 在内的多数公有云实例都构建在其之上。嵌套虚拟化指在虚拟机内部再运行一个 hypervisor，这会迫使 KVM 模拟第二层虚拟化，并更依赖影子页表和页表元数据。由于这条模拟路径要替一个本身也在管理内存的虚拟机处理内存映射，其中的缺陷可能跨越虚拟机与宿主机的信任边界，泄露其他租户的内存页或宿主机密钥等敏感数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html">Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host ...</a></li>
<li><a href="https://www.digitalocean.com/blog/cve-2026-99312-kvm-patch">Virtualization, Responsible Disclosure , and CVE - 2026 - 99312</a></li>
<li><a href="https://www.terra.security/blog/kvm-guest-to-host-escape">KVM Guest-to- Host Escape | Terra Security Research</a></li>

</ul>
</details>

**标签**: `#security`, `#KVM`, `#CVE`, `#Linux kernel`, `#virtualization`

---

<a id="item-4"></a>
## [Gemini 可在 Mac 上代用户操作，支持暂停与关键操作审批](https://www.bloomberg.com/news/articles/2026-11-19/google-s-gemini-can-now-control-mac-devices-on-users-behalf) ⭐️ 7.0/10

Google 为 Mac 版 Gemini 新增了“电脑操作”能力，可以让助手代替用户点击、输入、浏览菜单并填写表单。该功能已面向美国地区、在 Mac 上使用 Gemini 应用并订阅 Google AI Plus、Pro 或 Ultra 的用户开放。 这让 Gemini 从“回答问题”的助手变成真正动手完成桌面任务的智能体，使 Google 与其他推出 computer use 类智能体的厂商正面竞争。由于它操作的是用户的真实电脑，后台运行与审批机制的设计将直接影响用户是否愿意交出桌面控制权。 Gemini 在独立的后台窗口中运行，用户在主屏幕和光标上继续正常工作的同时任务照常推进；用户还可以限制它可访问的应用、实时查看操作过程、随时暂停，并在关键操作执行前进行审批。该功能目前仅限美国地区和付费 Google AI 订阅层级的 macOS 用户，未提及 Windows 或免费版的支持计划。

telegram · zaihuapd · 11月20日 02:51

**背景**: computer use 类智能体指的是像人一样操作图形界面的 AI 系统，而不仅仅调用 API。一种常见做法是读取操作系统的无障碍树（accessibility tree）——也就是 macOS、Windows 和 Linux 上屏幕阅读器多年来依赖的结构化界面数据——从而确定性地定位按钮、输入框和菜单，而不是靠截图猜测，开源工具 agent-desktop 走的就是这条路线。Google AI Plus、Pro 和 Ultra 是 Google 面向 Gemini 的消费者订阅层级，更高级的功能（例如本次的电脑操作）会按层级开放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://runany.dev/blog/agent-desktop/">agent-desktop – Native Desktop Automation CLI for AI Agents</a></li>
<li><a href="https://followagents.com/en/agents/agent-desktop">Agent Desktop — FollowAgents</a></li>

</ul>
</details>

**标签**: `#Gemini`, `#AI agents`, `#Google`, `#desktop automation`, `#product launch`

---

<a id="item-5"></a>
## [英国法庭裁定苹果胜诉，内政部须公开秘密后门命令](https://appleinsider.com/articles/26/11/19/uk-cant-hide-that-it-tried-ordering-apple-to-allow-access-to-user-data) ⭐️ 7.0/10

英国调查权力法庭（Investigatory Powers Tribunal）裁定苹果胜诉，内政部不得再对其要求获取 iPhone 加密用户数据访问权限的「技术能力通知」（TCN）保密。内政部随后确认确曾发出该通知，并称目的是将罪犯绳之以法，但法庭认定其以国家安全为由保密的做法「不切实际」，案件大部分内容将公开审理。 这是对政府能否在秘密状态下强迫加密设备厂商内置监控能力的一次重要检验。该裁决为英国《调查权力法》下的技术能力通知确立了透明度先例，不仅影响苹果，也影响所有可能收到此类命令的科技与电信服务商，并将推动美、欧、英之间围绕加密与监控的更大争论。 根据英国《2016 年调查权力法》第 253 条，技术能力通知并不要求披露某条具体的历史通信内容，而是要求服务商具备在另行取得授权时提供可读、已解密数据的技术能力。正因如此，该命令触及的是苹果端到端加密的核心能力，而非某一台设备，法庭否决全面保密的请求也就成了本案的关键。

telegram · zaihuapd · 11月20日 04:13

**背景**: 调查权力法庭（IPT）是英国的司法机构，隶属内政部但独立运作，负责受理针对公共机构及情报部门监控行为的申诉。技术能力通知则是《2016 年调查权力法》创设的机制，允许内政大臣命令电信和邮政运营商预先建设拦截或数据提取能力，以备未来取得令状时使用。此类通知通常秘密送达，因此要求公开披露并公开审理的裁决相当罕见。苹果此前也多次卷入类似争端，最著名的是 2016 年与美国联邦调查局就解锁圣贝纳迪诺枪击案 iPhone 的对峙。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.legislation.gov.uk/ukpga/2016/25/section/253">Investigatory Powers Act 2016 - Legislation.gov.uk</a></li>
<li><a href="https://factually.co/fact-checks/justice/technical-capability-notice-uk-investigatory-powers-act-explained-used-18b109">What Is A Technical Capability Notice Under The UK Inv...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Investigatory_Powers_Tribunal">Investigatory Powers Tribunal - Wikipedia</a></li>

</ul>
</details>

**标签**: `#encryption`, `#privacy`, `#apple`, `#surveillance`, `#uk-policy`

---

<a id="item-6"></a>
## [TikTok 面向全球上线 AI 形象检测工具](https://www.straitstimes.com/world/tiktok-launches-tool-to-help-public-figures-detect-deepfakes-globally) ⭐️ 7.0/10

自 11 月 20 日起，TikTok 在全球范围上线 Likeness Detection（形象检测）工具：完成第三方身份验证的公众人物和头部创作者，在他人未经授权用 AI 生成其形象的内容时可以获得提示并进行举报。同日推出的还有一款无需登录的透明性核查工具，任何人都能上传图片或视频，查询其是否由 TikTok 自家的 AI 功能生成。 这是首批面向全平台、以保护真人形象为目标而非仅做合成内容标注的深度伪造检测部署之一；与此同时，欧盟对 AI 内容标注的要求正推动平台落地具体的透明性功能。考虑到 2027 年欧洲多国将举行选举，这类工具有望成为选举诚信与冒名侵权应对的常规基础设施。 形象检测工具属于主动选择加入（opt-in），且需通过第三方身份验证，因此覆盖的是认证公众人物与头部创作者而非普通用户；它只是把匹配到的内容呈现给本人去复核和举报，并不会自动下架。透明性核查工具只能识别由 TikTok 自家 AI 功能生成的内容，无法检测用 Midjourney、Stable Diffusion 等第三方生成器制作的深度伪造。

telegram · zaihuapd · 11月20日 08:14

**背景**: 深度伪造（deepfake）指用生成式 AI 模型合成的高逼真图像、视频或音频，通常用于再现真实人物的外貌与声音。随着这类模型的成本降低、获取门槛下降，冒名诈骗、非自愿私密影像以及带政治目的的伪造片段在社交平台上扩散，而检测本身十分困难，因为检测方必须跟上不断进化的生成模型。监管层面的应对是强制披露：欧盟《人工智能法案》要求提供方与部署方对 AI 生成或被操控的内容进行标注，相关义务自今年 8 月起开始适用，平台目前正通过“标注 + 检测 + 举报处置”的流程来满足要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/967486/tiktok-ai-likeness-detection-tool">TikTok is testing an AI likeness detection tool | The Verge</a></li>
<li><a href="https://ainewz.io/tools/ai-likeness-detection">AI Likeness Detection — Pricing, Use Cases &amp; Tips — AI News Hub</a></li>
<li><a href="https://globaloutreach.co/blog/ai-likeness">AI Likeness – Global Outreach Blog | Global Outreach</a></li>

</ul>
</details>

**标签**: `#AI deepfake detection`, `#content moderation`, `#TikTok`, `#EU AI regulation`, `#platform policy`

---

<a id="item-7"></a>
## [OpenAI 推出 Background 后台模式：最长 8 小时窗口，token 最高便宜 40%](https://developers.openai.com/api/docs/guides/background) ⭐️ 7.0/10

OpenAI 为 Responses API 推出了 Background 后台模式：开发者在请求中设置 background: true，并通过 background\_options.completion\_window 选择 2 小时或 8 小时的完成窗口，从而让长耗时请求以异步方式执行。使用 2h 窗口的请求按标准 token 费率的 7 折计费，8h 窗口为 6 折，而保持默认的 soonest 则没有任何折扣；该折扣目前面向 GPT-6.2 Astra、GPT-6.2 Sol、GPT-6.1 Terra 和 GPT-6 Luna 公测。 这为构建生产级 LLM 工作流的开发者提供了一条把“可接受的延迟”直接兑换成成本下降的路径：诸如夜间摘要、文档批处理或智能体多步流程这类任务，如今可以带着明确的完成期限排队执行，而不必争抢即时算力。这也表明 OpenAI 愿意把异步、对延迟不敏感的推理作为一个独立的产品分层来定价，对需要为高吞吐流水线做预算的团队意义重大。 文档明确指出，即使把 store 设为 false 或启用了零数据保留（ZDR），后台模式仍会临时存储响应数据，因为 API 需要这些数据来运行请求并让结果可被取回；不过所有窗口（soonest、2h、8h）下临时存储的请求内容都会在静态时加密。完成窗口只是首个响应的目标时限而非延迟保证，因此开发者仍需自行处理任务排队、失败重试和乱序完成的情况。

telegram · zaihuapd · 11月20日 11:15

**背景**: OpenAI 的 Responses API 允许开发者提交请求、稍后取回结果；Background 模式在此基础上把“提交”与“完成”解耦，使单个请求可以持续数小时而不像同步调用那样超时。零数据保留（ZDR）是 OpenAI 的一项政策，符合条件的 API 客户可以让提示与响应不被留存用于滥用监测，而新的注意事项之所以重要，是因为后台模式必须在任务完成前保留请求数据。类似的取舍在整个推理栈中普遍存在：服务系统通常会把对延迟不敏感的工作安排在紧急请求的间隙中执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/background">Background mode | OpenAI API</a></li>
<li><a href="https://community.openai.com/t/reduce-costs-using-background-mode-with-completion-windows/1418130">Reduce costs using Background Mode with completion windows</a></li>
<li><a href="https://www.aifeaturedrop.com/2026/11/openai-background-mode-guide-2-hour-and.html">OpenAI Background Mode Guide: 2-Hour and 8-Hour Completion ...</a></li>

</ul>
</details>

**社区讨论**: OpenAI 开发者社区的讨论把这一功能视为用延迟换成本的手段，其中一个例子是下班前提交会议记录并设置 8h 窗口，第二天早上即可拿到简报。第三方解读则强调，完成窗口并不构成延迟或顺序上的保证，因此团队应围绕可能等待、失败或乱序完成的任务构建可靠的队列。

**标签**: `#OpenAI API`, `#async processing`, `#LLM infrastructure`, `#pricing`, `#data retention`

---

<a id="item-8"></a>
## [美国收紧芯片出口，印度趁机扩张 AI 算力](https://www.bloomberg.com/news/articles/2026-11-20/nvidia-scandal-fallout-india-ai-yotta-ambani-adani-am-intelligence-e2e-networks) ⭐️ 6.0/10

美国收紧对马来西亚、泰国和新加坡的先进芯片出口，印度 AI 业界希望承接由此外溢的需求。Yotta 表示未来一年计划新增约 10 万块 GPU，相当于印度现有 AI 算力增加约 10%。 随着企业在美国出口管制受影响地区之外寻找算力，这一变化可能加速印度成为替代性的 AI 算力中心。信实和阿达尼的大规模基础设施承诺也因此更受关注，可能重塑印度的数据中心和 AI 云市场。 印度目前拥有 153 个数据中心，位居全球第 14，而 Yotta 计划新增的 GPU 仅相当于当前全国算力的约十分之一。信实承诺投入至多 1100 亿美元、阿达尼承诺 1000 亿美元建设 AI 基础设施，但印度长期受算力短缺和资本受限拖累。

telegram · zaihuapd · 11月20日 07:31

**背景**: 先进芯片出口管制是美国为保护国家安全而限制向特定国家销售高性能半导体及相关技术的规则。Yotta 是印度数据中心和主权云服务商，其 Shakti Cloud 平台提供 GPU 即服务和 AI 云算力，并部署了大量 NVIDIA GPU。印度一直试图通过 India AI Mission 等计划扩大本土 AI 基础设施，但算力和资本仍是主要瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yotta.com/">India ’s Trusted Sovereign Cloud &amp; AI Infrastructure – Yotta</a></li>
<li><a href="https://shakticloud.ai/">Yotta Shakti Cloud: Sovereign Cloud &amp; AI Cloud Platform India</a></li>
<li><a href="https://www.brookings.edu/articles/the-new-ai-diffusion-export-control-rule-will-undermine-us-ai-leadership/">The new AI diffusion export control rule will undermine US ... | Brookings</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#chip export controls`, `#India AI`, `#data centers`, `#geopolitics`

---

<a id="item-9"></a>
## [苹果被曝研发自主 AI 智能体，最早 2027 年末推出](https://www.bloomberg.com/news/articles/2026-11-19/apple-is-working-on-ai-agent-for-device-control-apps-browsing-and-coding) ⭐️ 6.0/10

彭博社从苹果本周新增的招聘信息中发现，苹果正在招募一名高级工程经理，主导开发一款「主动式 AI 智能体」，该智能体可以替用户写代码、浏览网页并操控应用。该项目仍处于早期阶段，最早可能在 2027 年末推出。与此同时，macOS 27.3 新增了一个警告页面，把第三方智能体获取 Mac 控制权限的步骤从 4 步增加到 14 步。 一款能够端到端操控电脑的自主智能体，能力将远超 Siri 和 Apple Intelligence，意味着苹果要在这一方向上直接对标 OpenAI、Anthropic 和 Meta——后者的 Meta Muse 等同类智能体产品已经落地。与此同时，苹果收紧 macOS 的授权流程，表明它打算把系统深层控制权握在自己手里，这一姿态可能影响第三方智能体在 Mac 上的生存空间。 该消息基于招聘信息而非已确认的产品计划，2027 年末的时间点也留下了延期甚至取消的充分空间。不过权限调整是实打实的：第三方智能体在获得驱动 Mac 所需的辅助功能级控制权之前，现在要面对一个 14 步流程，并多出一个警告页面。

telegram · zaihuapd · 11月20日 08:59

**背景**: AI 智能体（AI agent）指的是接受一个目标而非单条指令、并自行执行多步操作的系统，例如打开应用、在界面中点击操作，或者编写并运行代码；而「主动式」智能体更进一步，它能推断用户需求并在没有明确指令的情况下主动行动，清华大学与面壁智能开源的 Proactive Agent 就是这一范式的代表。在 macOS 上，应用必须先获得「辅助功能」权限，才能以编程方式控制鼠标、键盘和其他应用，这也是该授权流程的步数如此关键的原因。苹果目前推出的仍是 Apple Intelligence 和改版 Siri，而非通用的电脑操控智能体，而 Meta 的 Muse、OpenAI 等竞争对手已经发布了个人智能体产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-bot.cn/proactive-agent/">Proactive Agent - 清华联合面壁智能开源的新一代主动Agent交互范式 |...</a></li>
<li><a href="https://www.36kr.com/p/3057238478672257">颠覆现有 Agent 范式，清华&amp;面壁提出新一代主动Agent交互范式-36氪</a></li>
<li><a href="https://ai.meta.com/muse/">Muse: Meta&#x27;s personal AI agent, features &amp; capabilities</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI agents`, `#macOS`, `#Bloomberg`, `#industry news`

---