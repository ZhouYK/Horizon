---
layout: default
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22 23:31:41 +0000
lang: zh
report: default
---

> 从 251 条内容中筛选出 6 条重要资讯。

---

1. [任天堂单日下架 400 余个 Switch 模拟器仓库](#item-1) ⭐️ 8.0/10
2. [皮尤：ChatGPT 后 35%新网页有 AI 痕迹](#item-2) ⭐️ 8.0/10
3. [开源 AI 模型加速追赶，每代追平时间减半](#item-3) ⭐️ 8.0/10
4. [美国联盟敦促 FTC 调查 AI 公司销毁书籍行为](#item-4) ⭐️ 8.0/10
5. [苹果裁员逾 200 人，涉及 Siri 与 Vision Pro 团队，聚焦 AI 与新设备](#item-5) ⭐️ 7.0/10
6. [Take-Two 追查 GTA 6 泄密者，传票要求微软交出 Discord 全员设备 ID](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [任天堂单日下架 400 余个 Switch 模拟器仓库](https://torrentfreak.com/nintendo-wipes-out-400-switch-emulator-repos-in-single-day-github-sweep/) ⭐️ 8.0/10

这次史无前例的单日大规模下架行动表明，任天堂正积极利用 DMCA 反规避条款打击模拟器项目，可能对开源模拟器开发产生寒蝉效应。大规模清除分支仓库的做法，可能开创版权方一次性铲除整个模拟器社区的先例。 下架通知援引了 Yuzu 和解案作为先例，但这两起案件均未经过法院的实质性裁决。suyu 是已停止开发的 Yuzu 模拟器的社区分支，而 Skyline 则是一个已停止更新的实验性安卓模拟器。

telegram · zaihuapd · 8月22日 00:28

**背景**: 任天堂 Switch 模拟器是开源程序，允许用户在其他设备上运行 Switch 游戏，通常需要使用任天堂未授权的密钥解密游戏文件。DMCA 的反规避条款规定，绕过技术保护措施属于违法行为，这为任天堂要求下架相关解密代码提供了法律依据。最流行的 Switch 模拟器 Yuzu 于 2024 年与任天堂达成和解，而 suyu 是社区为继续开发而创建的 Yuzu 分支。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://suyu.dev/">Suyu Emulator — A Familiar Nintendo Switch Emulator</a></li>
<li><a href="https://en.wikipedia.org/wiki/DMCA_anti-circumvention">DMCA anti-circumvention</a></li>
<li><a href="https://github.com/suyu-emu">Follow Their Code on GitHub. | Suyu Emulator</a></li>

</ul>
</details>

**标签**: `#DMCA`, `#Nintendo`, `#Emulator`, `#GitHub`, `#Open Source`

---

<a id="item-2"></a>
## [皮尤：ChatGPT 后 35%新网页有 AI 痕迹](https://www.independent.co.uk/tech/ai-webpages-internet-dead-internet-theory-b3037019.html) ⭐️ 8.0/10

皮尤研究中心对近 50 万个英文网页的分析显示，10%的页面有明显 AI 生成痕迹。在 ChatGPT 发布后新发布的页面中，这一比例升至 35%。 这项研究为 AI 对网络内容日益增长的影响提供了具体、数据驱动的证据，支持了&\#x27;死互联网理论&\#x27;的担忧。它表明相当一部分新增网络信息可能是机器撰写的，影响读者、研究人员和平台审核。 AI 写作特征也在增加：破折号使用约翻倍，牛津逗号增加 63%，聊天机器人常用词翻倍。.com 网站的 AI 痕迹约为.org 网站的两倍，是.edu/.gov 网站的十倍。

telegram · zaihuapd · 8月22日 05:48

**背景**: &\#x27;死互联网理论&\#x27;认为，如今的互联网（尤其是社交媒体）上大部分内容和活动由人工智能、机器人和企业议程主导，而非真实的人类互动。皮尤的分析基于大量英文网页样本，为 AI 文本的普遍程度提供了实证证据，使这一常停留在传闻层面的讨论有了数据支撑。ChatGPT 于 2022 年底发布，使 AI 文本生成变得广泛可用，研究也将其与新页面中 AI 内容比例骤升联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory - Wikipedia</a></li>
<li><a href="https://ui.adsabs.harvard.edu/abs/2025arXiv250200007M/abstract">The Dead Internet Theory: A Survey on Artificial Interactions and the Future of Social Media - ADS</a></li>
<li><a href="https://www.unsw.edu.au/newsroom/news/2024/05/-the-dead-internet-theory-makes-eerie-claims-about-an-ai-run-web-the-truth-is-more-sinister">The ‘dead internet theory’ makes eerie claims about an AI-run web. The truth is more sinister</a></li>

</ul>
</details>

**标签**: `#AI`, `#web content`, `#Pew Research`, `#ChatGPT`, `#internet`

---

<a id="item-3"></a>
## [开源 AI 模型加速追赶，每代追平时间减半](https://newsletter.semianalysis.com/p/are-open-models-catching-up) ⭐️ 8.0/10

独立 AI 研究机构 SemiAnalysis 发布报告称，开源大语言模型正在以更快的速度缩小与闭源领先者的差距，每代实现能力追平所需的时间都减半。例如，Kimi K2.6 在 4.8 个月内追上 Opus 4.5，GLM-5.2 在 6 个月内超过 GPT-5.2。 这种加速追赶的趋势表明，模型层本身可能正在商品化，直接威胁到 Anthropic 等闭源实验室的“护城河”——据报道，Anthropic 来自编程和智能体任务的年化收入超过 650 亿美元。这也标志着 AI 产业竞争格局的重大变化，可能削弱前沿模型提供商长期的定价权。 报告指出，GLM 5.3、Kimi K3 等开源模型已能胜任许多曾为 Anthropic 带来收入增长的编程和智能体任务。但基准测试并非全部：Anthropic 的产品化能力——包括打包、工具链和企业服务集成——仍是其防御性优势。

telegram · zaihuapd · 8月22日 08:26

**背景**: 开源 AI 模型（如中国公司月之暗面（Moonshot AI）的 Kimi 和智谱（Z.ai）的 GLM）会公开发布模型权重，任何人都可以运行或微调；而 Anthropic、OpenAI 等闭源提供商则对其架构和权重保密。历史上，闭源模型一直处于性能前沿，但开源权重模型如今已能更快地接近甚至追平闭源水平。SemiAnalysis 将大模型的发展历史划分为早期扩展、推理和智能体三个时代，发现追平时间大幅缩短，其中智能体时代追赶速度最快。中国 AI 生态系统在发布有竞争力的开源权重模型方面发挥了核心作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://startedbywomen.com/companies/semianalysis">SemiAnalysis | Started by Women</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K2.6">Kimi K2.6</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.2">GLM-5.2</a></li>

</ul>
</details>

**标签**: `#open-source`, `#AI models`, `#LLM`, `#competitive analysis`

---

<a id="item-4"></a>
## [美国联盟敦促 FTC 调查 AI 公司销毁书籍行为](https://www.axios.com/2026/08/21/ftc-ai-companies-book-destruction-investigate) ⭐️ 8.0/10

8 月 21 日，十余个美国倡导团体联名致信联邦贸易委员会（FTC），敦促其对购买、扫描并销毁实体书以训练模型的人工智能公司展开调查，认为该行为构成《联邦贸易委员会法》第 5 条下的不公平竞争手段。 此举将 AI 训练数据争议从版权法延伸至竞争监管领域，或为 AI 公司获取稀缺数据的方式开创先例。若 FTC 启动调查，可能重塑整个 AI 行业的数据获取做法，并影响 Anthropic、谷歌、微软和 OpenAI 等主要企业。 信件援引 Anthropic 耗资数百万美元购书、切除书脊并扫描页面以喂养 Claude 的案例，同时指出谷歌、微软和 OpenAI 也面临类似版权诉讼。团体强调不反对 AI 训练本身，而是反对囤积并销毁实体书的做法。

telegram · zaihuapd · 8月22日 15:40

**背景**: AI 公司依赖海量文本来训练大语言模型，而实体书提供了许多在网上无法免费获取的高质量内容。购买并销毁书籍可使单一公司独占这些内容，实际上将文化珍品移出市场。《联邦贸易委员会法》第 5 条禁止不公平的竞争方法，其中包括抬高竞争对手成本、构筑护城河的行为。若该请求被受理，AI 版权之争将延伸至竞争执法领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude (AI)</a></li>

</ul>
</details>

**标签**: `#AI`, `#FTC`, `#competition`, `#training data`, `#regulation`

---

<a id="item-5"></a>
## [苹果裁员逾 200 人，涉及 Siri 与 Vision Pro 团队，聚焦 AI 与新设备](https://www.bloomberg.com/news/articles/2026-08-21/apple-cuts-jobs-in-siri-vision-pro-immersive-video-and-gaming-teams) ⭐️ 7.0/10

苹果正在 Siri、Vision Pro、沉浸式视频和游戏团队裁员逾 200 人，其中 Vision Pro 部门约 100 人，Siri 与软件团队约 100 人。苹果表示将增设新岗位，仅影响有限的现有职位。 这一重组表明苹果正从表现不佳的硬件和助手项目转向 AI 与新设备开发这一战略重点。这可能会重塑 Siri 和 Vision Pro 的路线图，并对 AR/VR 和语音助手生态产生广泛影响。 Vision Pro 游戏团队基本被关停，沉浸式视频内容团队被缩减，智能系统体验团队的部分岗位被裁撤。裁员共影响 200 多人，但苹果表示将增设新职位。

telegram · zaihuapd · 8月22日 12:31

**背景**: Siri 是苹果的语音助手，与 Alexa 和 Google Assistant 竞争；Vision Pro 则是苹果发布的混合现实头显，被视为新的计算平台。苹果一直在将投资转向生成式 AI 和未来设备，此次人才调整反映了这一整体产品战略。

**标签**: `#Apple`, `#AI`, `#Siri`, `#Vision Pro`, `#Layoffs`

---

<a id="item-6"></a>
## [Take-Two 追查 GTA 6 泄密者，传票要求微软交出 Discord 全员设备 ID](https://www.tomshardware.com/video-games/console-gaming/take-two-subpoenas-microsoft-for-windows-device-ids-of-everyone-in-three-discord-servers-in-gta-6-leak-hunt) ⭐️ 6.0/10

8 月 20 日，Take-Two 在纽约南区联邦法院提交两份 DMCA 传票，要求微软和 Discord 在 9 月 4 日前交出 GTA 6 泄密者「CyberLeek」的身份信息。传票要求提供自 6 月 1 日以来在三个指定 Discord 服务器发言的所有账号的 Windows MachineGuid 设备标识、IP 地址、手机号，甚至 OneDrive 的内容。 这一事件意义重大，因为传票范围远超追查单一泄密者，波及三个 Discord 服务器中所有成员的个人数据，包括无关用户。这可能对游戏社区讨论产生寒蝉效应，并为发行商利用 DMCA 传票追查泄密者开创法律先例。 这两份 DMCA 传票依据《数字千年版权法》第 512\(h\) 条提交，要求提供 6 月 1 日以来活跃账号的数据。被点名的服务器之一是澳大利亚创作者 DarkViperAU（本名 Matthew Judge）的服务器，他已否认对泄密事件知情。

telegram · zaihuapd · 8月22日 11:41

**背景**: DMCA 传票是美国《数字千年版权法》下的一种法律工具，允许版权持有人强迫在线服务提供商披露涉嫌侵权用户的身份。Windows MachineGuid 是存储在注册表中的唯一设备标识，与操作系统安装绑定，常用于跨账号和服务识别特定电脑。Take-Two 是《侠盗猎车手》的发行商，本周发生了 GTA 6 实机画面泄露事件，促使该公司采取法律行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nextofwindows.com/the-best-way-to-uniquely-identify-a-windows-machine">The Best Way To Uniquely Identify A Windows Machine</a></li>
<li><a href="https://www.vondranlegal.com/when-is-a-dmca-subpoena-proper-to-clerk-of-court">DMCA Subpoena Law Firm - 512(h) | Vondran Legal</a></li>

</ul>
</details>

**标签**: `#privacy`, `#legal`, `#GTA6`, `#Discord`, `#subpoena`

---