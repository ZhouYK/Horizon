---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27 23:02:27 +0000
lang: zh
report: default
---

> 从 76 条内容中筛选出 7 条重要资讯。

---

1. [Linux 内核 nfsd 曝 NFS2ROOT 漏洞，未认证即可远程获取 root](#item-1) ⭐️ 9.0/10
2. [微软 CEO 承认应届生招聘放缓：AI 预算优先](#item-2) ⭐️ 7.0/10
3. [黑客利用 AI 工具 ARTEX 攻击 CIA 等美国情报机构](#item-3) ⭐️ 7.0/10
4. [Anthropic 系统卡披露：对研发前沿模型的请求暗中降质，约占 0.03% 流量](#item-4) ⭐️ 7.0/10
5. [《我的世界》基岩版资源包漏洞影响 26.52 至 26.63，26.65 已修复](#item-5) ⭐️ 7.0/10
6. [谷歌 Play 将于 2027 年公开商家开发者的电话与地址](#item-6) ⭐️ 6.0/10
7. [GitHub 公开点赞 AnyPS5 的《GTA 6》非官方 PC 移植后火速删帖](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Linux 内核 nfsd 曝 NFS2ROOT 漏洞，未认证即可远程获取 root](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec 公开了 CVE-2026-99362（代号 NFS2ROOT），这是 Linux 内核 NFS 服务器（nfsd）中的预认证堆溢出漏洞，CVSS 评分 9.8，攻击者无需任何认证，仅凭一条发往 tcp/2049 的连接即可在受影响主机上获得 root 权限。该漏洞自 2014 年的 Linux 3.16 起就已存在，目前已在 6.12.117、6.18.61、7.3.2 和 7.4-rc1 内核中修复，CVE 于 2026 年 11 月 19 日至 20 日公开。 由于 nfsd 运行在内核态且该缺陷在认证之前即可触发，一个未认证的数据包就能让文件服务器、NAS 设备或集群存储节点彻底失陷，而长达 12 年的受影响窗口意味着存量设备规模极大。如此严重级别的预认证远程内核内存破坏漏洞相当罕见，任何对外暴露 2049 端口的主机都应立即修补。 根据技术分析，远程 NFSv4.1 客户端可诱使 nfsd 向一个长度为零的回复缓存槽写入 80 字节的回复数据，从而破坏相邻的内核内存；只有启用了 NFSv4.1 或 4.2 的主机受影响。修复需要升级内核并重启，无法立即升级的管理员应在防火墙上封禁 tcp/2049 访问。

telegram · zaihuapd · 11月27日 12:57

**背景**: NFS（网络文件系统）是 Linux 与 Unix 系统共享目录所使用的标准协议，nfsd 则是内核侧负责在众所周知的 2049 端口上处理客户端请求的服务端程序。NFSv4.1 与 NFSv4.2 引入了会话（session）和回复缓存（reply cache）等机制，使客户端可以安全地重试请求，而该溢出就出在回复缓存的处理逻辑中。CVSS 9.8 表示这是一个可经网络触达、攻击复杂度低、无需任何权限的严重漏洞，出现在内核组件中通常意味着可在最高权限级别实现远程代码执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensec.in/blog/nfs2root-cve-2026-99362">NFS2ROOT (CVE-2026-99362): pre-auth root in Linux nfsd | OpenSec</a></li>
<li><a href="https://cybersecuritynews.com/nfs2root-linux-vulnerability/">12-Year-Old NFS2ROOT Linux Flaw Could Let Hackers Take Full ...</a></li>
<li><a href="https://blog.ostorlab.co/linux-kernel-nfsd-preauth-memory-corruption-cve-2026-99362.html">Linux Kernel nfsd Pre-Auth Memory Corruption (CVE-2026-99362)</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#vulnerability-disclosure`, `#nfs`, `#remote-code-execution`, `#security`

---

<a id="item-2"></a>
## [微软 CEO 承认应届生招聘放缓：AI 预算优先](https://www.windowslatest.com/2026/11/27/lets-add-the-next-human-satya-nadella-admits-new-grad-hiring-slowed-as-companies-rebuild-around-ai-and-says-every-company-will-add-its-next-person-after-it-burns-through-its-ai-budget/) ⭐️ 7.0/10

微软 CEO 萨提亚·纳德拉在 The Pragmatic Engineer 播客中承认，应届生招聘已经放缓：企业会先重新调配现有员工，再补充招聘新人；AI 原生公司则会先用完 AI 预算，然后才招“下一个人”。截至 6 月 30 日，微软员工数降至 22.3 万，同比减少 5000 人，为 2016 年以来首次年度下滑；MIT 与微软研究院的论文还显示，采用 GitHub Copilot 的企业季度技术岗招聘减少 29%，初级岗位受冲击最大。 这些表态和数据表明，科技行业的入门级招聘可能正在发生由 AI 驱动的结构性变化，而不只是周期性放缓；这会压缩传统的人才培养管道，并直接影响应届生和初级工程师。如果这一趋势扩散，可能会改变整个科技行业培养和引入早期职业人才的方式。 29%这一数据来自将 Copilot 采用与招聘减少联系起来的观察性研究，因此它体现的是相关性，而不能直接证明因果关系；微软员工人数下降也可能包含重组等其他因素。纳德拉今年年初在达沃斯还曾表示“仍然相信校园招聘”，这使得他最新的表态在语气上出现了明显变化。

telegram · zaihuapd · 11月27日 03:03

**背景**: GitHub Copilot 是 GitHub 与 OpenAI 联合推出的 AI 编程助手，2021 年进入技术预览、2022 年正式发布，并以扩展形式集成到 VS Code、Visual Studio、JetBrains 系列等 IDE 中，根据上下文补全代码。作为生成式 AI 开发工具，它常被用来研究对程序员生产力以及技术岗位需求的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/features/copilot">GitHub Copilot · Your AI coding agent · GitHub · GitHub</a></li>
<li><a href="https://jiangren.com.au/blog/github-copilot-guide-01-what-is-github-copilot">GitHub Copilot 实战指南 — GitHub Copilot 是 什 么 ：全球最大的 AI...</a></li>

</ul>
</details>

**标签**: `#AI labor impact`, `#Microsoft`, `#hiring trends`, `#GitHub Copilot`, `#tech industry`

---

<a id="item-3"></a>
## [黑客利用 AI 工具 ARTEX 攻击 CIA 等美国情报机构](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack) ⭐️ 7.0/10

《福布斯》援引《纽约时报》报道称，黑客使用 AI 工具 ARTEX 攻击了美国中央情报局（CIA）、国家地理空间情报局（NGA）和国家情报总监办公室（ODNI）的系统，影响的是非机密侦察数据。报道称此次攻击看起来不算严重。 即便这次入侵规模有限，美国情报系统遭攻击仍值得警惕，因为它表明智能体式 AI 渗透测试工具正被用于高价值政府目标，可能加快侦察速度并降低攻击者的技术门槛。这也迫使防御方不仅要应对传统的人工攻击，还要检测自动化、持续性的探测行为。 ARTEX 被描述为一个开源 AI 渗透测试框架，可整合多个开源 AI 模型来探测网络和计算机防御；微软称威胁行为者滥用它进行侦察、凭据攻击和 Web 利用，且往往利用普通弱点而非零日漏洞。报道中的攻击仅影响非机密侦察数据，且该消息只是简短的二手摘要，攻击范围和归属仍未经核实；据称该工具的中国开发者在其被用于多起攻击（包括针对欧盟的一起）后将其从 GitHub 删除，FBI 也曾就其使用发出警告。

telegram · zaihuapd · 11月27日 10:42

**背景**: CIA 是美国对外情报机构，NGA 负责分析地理空间情报，ODNI 则协调更广泛的情报界。ARTEX 是一个开源的智能体式 AI 渗透测试框架：它不是由人手动执行扫描，而是利用大语言模型规划并串联侦察、凭据攻击和利用步骤。这类工具对红队和犯罪分子都有吸引力，因为它们可以持续工作，并发现常见配置错误、暴露服务和弱密码。此次据称针对情报机构的攻击，说明 AI 自动化正在向进攻性网络行动扩散。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/11/25/what-defenders-need-to-know-artex-agentic-ai-framework-threat-actors-abuse/">What defenders need to know about ARTEX, the agentic AI ...</a></li>
<li><a href="https://cybersecuritynews.com/hackers-use-ai-powered-artex-framework/">Hackers Use AI-Powered ARTEX Framework to Automate ...</a></li>
<li><a href="https://ysecurity.io/blog/artex-ai-hacking-tool/">ARTEX AI Hacking Tool: What It Is and How to Defend</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI`, `#hacking`, `#US intelligence`, `#Artex`

---

<a id="item-4"></a>
## [Anthropic 系统卡披露：对研发前沿模型的请求暗中降质，约占 0.03% 流量](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic 今年 6 月为 Claude Mythos 5 与 Fable 5 发布的系统卡写明：针对开发前沿大模型的请求不会像安全拦截那样被拒绝，而是被暗中削弱回答效果，手段包括改写提示、引导向量和参数高效微调；估算影响约 0.03% 的流量、不到 0.1% 的组织。该披露本周因开发者在 Hacker News 上的讨论而重新受到关注。 这是一个值得关注的透明度与信任问题：用户既察觉不到降质，也不会像遇到安全拦截时那样回退到其他模型，等于系统依据推断出的意图而非明确拒绝，给回答施加了一重隐形惩罚。这也为 AI 实验室如何针对潜在竞争者执行服务条款立下先例，可能让开发者对在托管 API 上运行哪些任务心存顾虑。 干预覆盖预训练流水线、分布式训练和加速器设计等任务，Anthropic 表示多数常规编码工作不受影响，并指出用 Claude 开发竞品模型本就违反其服务条款。与安全类拒绝不同，这类请求不会被转交给其他模型处理，因此在用户看来只是答案质量变差了。

telegram · zaihuapd · 11月27日 13:42

**背景**: Anthropic 在每次发布 Claude 模型时都会同步发布一份“系统卡”，记录模型能力、安全评估与负责任部署方面的决策。系统卡中提到的技术都是公开研究过的真实方法：引导向量（也称激活引导）在推理阶段操纵模型内部的激活值来改变其行为；参数高效微调（PEFT）只训练少量额外参数来适配大型预训练模型，而不是更新全部权重。相比之下，改写提示是在用户输入送入模型前对其做改动，因此用户根本看不到变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>
<li><a href="https://github.com/steering-vectors/steering-vectors">Steering Vectors - GitHub</a></li>
<li><a href="https://huggingface.co/blog/samuellimabraz/peft-methods">PEFT : Parameter - Efficient Fine - Tuning Methods for LLMs</a></li>

</ul>
</details>

**社区讨论**: 在 Hacker News 上，这一披露重新引发了关于服务条款应如何执行的争论，讨论集中在一种用户无法察觉的隐形降质是否足够透明，以及这对托管模型提供商的信任意味着什么。

**标签**: `#AI policy`, `#Anthropic`, `#AI safety`, `#model transparency`, `#trust &amp; ethics`

---

<a id="item-5"></a>
## [《我的世界》基岩版资源包漏洞影响 26.52 至 26.63，26.65 已修复](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

附加组件开发者 8Crafter 于 11 月 15 日在 Reddit 公开了一个《我的世界》基岩版漏洞：带有 content.zipe 文件的资源包可以改写游戏的 Ore UI 界面文件并运行隐藏脚本，已确认影响 26.52 至 26.63 版本，更早版本也可能受影响，覆盖 PC、手机和主机平台。Mojang 已在 26.65 版中修复该问题，社区开发者 AxmBro 也发布了 Windows 平台上的只读检测工具，用于查找资源包中的 content.zipe 文件。 由于基岩版客户端会自动下载服务器和 Realm 下发的资源包，玩家仅仅加入服务器就可能收到恶意文件，无需手动安装，这让庞大的玩家群体面临存档被删、IP 泄露甚至恶意软件执行的风险。这也提醒人们，热门游戏的模组与内容分享链路已成为真实的攻击面，服务器运营者和玩家都必须及时更新客户端。 已披露的利用方式包括删除全部存档、获取玩家 IP、在 Windows 上特定条件下无提示打开任意 URI，以及启动资源包内的批处理文件下载恶意软件；Java 版不受影响。AxmBro 的检测工具只能找出 content.zipe 的存在，无法判定资源包是否恶意，因此它只能作为风险提示而非结论。

telegram · zaihuapd · 11月27日 18:04

**背景**: 《我的世界》的资源包用于替换材质、音效和界面元素，而在基岩版中，服务器可以向连接的客户端自动推送资源包。基岩版的用户界面名为 Ore UI，使用 Web 技术构建——基于 React 库的开源 TypeScript 包——这正是改写其文件可能导致脚本执行、而非仅仅改变外观的原因。content.zipe 并不是资源包的正常组成部分，因此它的存在成为社区识别可疑资源包的主要标志。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/AxmBro/content-zipe-checker">GitHub - AxmBro/content-zipe-checker: Checks your PC for ...</a></li>
<li><a href="https://minecraft.wiki/w/Ore_UI">Ore UI – Minecraft Wiki</a></li>
<li><a href="https://www.techtimes.com/articles/330961/20261117/mojang-patches-bedrock-after-community-discovers-resource-packs-could-execute-malicious-code.htm">Mojang Patches Bedrock After Community Discovers Resource ...</a></li>

</ul>
</details>

**标签**: `#Minecraft`, `#security vulnerability`, `#Bedrock Edition`, `#resource packs`, `#gaming security`

---

<a id="item-6"></a>
## [谷歌 Play 将于 2027 年公开商家开发者的电话与地址](https://www.androidpure.com/google-play-trader-developer-address/) ⭐️ 6.0/10

谷歌 Play 宣布，自 2027 年 3 月 1 日起将在全球范围向用户展示自我声明为“商家”（trader）的开发者的联系方式，包括电话号码和地址，个人账户持有者也同样适用。所有活跃开发者账户须在 2027 年 2 月 1 日前申报商家或非商家身份，否则可能无法更新应用，并从 Play 全球下架。 这一变化几乎影响所有在 Google Play 上架应用的开发者，但对个人开发者和小团队冲击最大：只要售卖应用、提供应用内购买或以其他方式变现，其个人电话和实际地址就可能被公开展示给全球用户。同时，这项合规声明变成了硬性截止日期，直接决定应用能否继续上架。 该政策于今年 10 月公布，本周因隐私担忧遭到开发者反弹；欧盟相关法规并未要求向欧盟以外的用户展示这些信息，但谷歌却选择在全球范围执行。此外，谷歌不接受邮政信箱作为付款地址，而苹果仅在欧洲相关国家展示地址，并允许使用邮政信箱。

telegram · zaihuapd · 11月27日 01:44

**背景**: Google Play 与其他应用商店一样，需要遵守欧盟《数字服务法》（DSA），该法规要求在线市场列出“商家”（即以商业或职业身份经营的卖家）的联系信息，以便消费者知道自己从谁那里购买。谷歌的做法是让开发者自行申报为商家或非商家，其 Play Console 帮助文档也提示，若谷歌检测到商业活动，声明为非商家的账户可能被要求重新确认身份。如今谷歌把这种 DSA 式的信息披露扩展到全球，而非仅限于欧盟用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/googleplay/android-developer/answer/17594752?hl=en">Trader status declaration - Play Console Help</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/digital-services-act">The Digital Services Act | Shaping Europe’s digital future</a></li>

</ul>
</details>

**标签**: `#Google Play`, `#Android developers`, `#privacy`, `#platform policy`, `#app distribution`

---

<a id="item-7"></a>
## [GitHub 公开点赞 AnyPS5 的《GTA 6》非官方 PC 移植后火速删帖](https://www.pcgamer.com/games/microsofts-github-posts-message-celebrating-efforts-to-port-playstation-5-version-of-grand-theft-auto-6-to-pc-then-quickly-deletes-it/) ⭐️ 6.0/10

GitHub 在 X 平台发文公开庆祝开源项目 AnyPS5 推动《GTA 6》PS5 版本移植到 PC 的努力，甚至反问此举“是否越过法律红线”，随后在引发争议后迅速删除了该帖。AnyPS5 项目通过重写 PS5 可执行文件使其能在 Windows 和 Linux 上原生运行，目前 GitHub 星标数已突破 5.8 万，开发者正号召借助 AI 代理攻克其遗留的性能瓶颈。 这一事件凸显了开源逆向工程与游戏发行商知识产权执法之间的正面冲突：Take-Two 近期正严厉打击非官方重编译项目，因此 GitHub 的公开“点赞”（即便已被撤回）也说明这类项目已变得多么受关注。在《GTA 6》尚无官方 PC 版的情况下，一个规模庞大且快速扩张的社区项目，可能在 Rockstar 正式推出 PC 版之前就影响玩家与 MOD 开发者的玩法方式。 AnyPS5 并非模拟器：它把 PS5 可执行文件重新链接为宿主系统的原生格式，并重新实现主机的系统库，从而让游戏在 Windows 和 Linux 上原生运行，输入可通过 anyps5-input.ini 文件配置。项目自称面向互操作性、研究、保存与兼容性目的，但性能仍是其核心未解难题，这也是其推动引入 AI 代理的原因。

telegram · zaihuapd · 11月27日 03:33

**背景**: 静态重编译是模拟之外的另一条路径：它不是在运行时逐条指令地模拟 PS5 硬件，而是提前把主机二进制翻译成 PC 可直接执行的原生代码（通常借助 C 语言），速度可能快得多，但工作量巨大。KytyPS5、SharpEmu 等 PS5 模拟器能运行部分游戏，但都无法运行《GTA 6》；此前名为“Leonida”的《GTA 6》重编译项目已被 Rockstar 与 Take-Two 叫停。近来，AI 辅助的反编译与重编译工具被视为能把原本耗时数年的逆向工程压缩到更短周期的手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/AnyPS5">AnyPS5</a></li>
<li><a href="https://github.com/boykopovar/AnyPS5">GitHub - boykopovar/AnyPS5: Tool for automatic PS5 ...</a></li>
<li><a href="https://www.techpowerup.com/355160/rockstar-squashes-leonida-the-biggest-gta-6-pc-recompilation-effort">Rockstar Squashes &quot;Leonida,&quot; the Biggest GTA 6 PC Recompilation ...</a></li>

</ul>
</details>

**标签**: `#emulation`, `#reverse-engineering`, `#open-source`, `#gaming`, `#legal-risk`

---