---
layout: default
title: "Horizon Summary: 2026-10-30 (ZH)"
date: 2026-10-30 23:04:40 +0000
lang: zh
report: default
---

> 从 238 条内容中筛选出 8 条重要资讯。

---

1. [OpenVSX 上的 Claude Code 插件被投毒，波及 Cursor 扩展市场](#item-1) ⭐️ 8.0/10
2. [苹果 Apple 智能 11 月 4 日在中国开启测试，携手阿里千问](#item-2) ⭐️ 8.0/10
3. [DeepSeek 二轮融资 1055 亿元，估值超 6155 亿元](#item-3) ⭐️ 7.0/10
4. [百度网盘摇一摇广告被指改用磁力计绕过传感器权限](#item-4) ⭐️ 7.0/10
5. [投资者开始区分 AI 增长与 AI 现金创造](#item-5) ⭐️ 6.0/10
6. [盖洛普：美国员工敬业度跌至 29%，创 15 年来新低](#item-6) ⭐️ 6.0/10
7. [小米开源 0.8B 文档理解模型 Xiaomi-OCR-0](#item-7) ⭐️ 6.0/10
8. [Claude 将 Max 套餐更名为 Max 与 Ultra，验证版 Ultra 取消五小时用量限制](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenVSX 上的 Claude Code 插件被投毒，波及 Cursor 扩展市场](https://cursor.com/blog/claude-code-extension-security-notice) ⭐️ 8.0/10

Cursor 发布安全公告，确认 10 月 29 日其扩展市场（基于 Open VSX）中出现了被篡改的 &quot;Anthropic.claude-code&quot; 2.1.313 版本，而该版本并非由 Anthropic 官方构建。这个恶意扩展会收集主机信息并试图植入持久的 SSH 后门，最多可能影响 5,000 名用户，随后 Cursor 下架了该版本并暂时关闭了整个市场。 这是一起典型的针对开发者工具的软件供应链攻击：攻击者借用了可信且高知名度的扩展名称，直接把恶意代码送进开发者的机器，而那里往往存放着凭据、源代码和云环境访问权限。由于同一个 Open VSX 仓库为众多 VS Code 分支和 AI 编辑器提供扩展，这起事件说明市场信任机制与命名空间校验已经成为整个生态的单点故障。 根据公开分析，这个伪造版本会添加一个名为 &quot;svc-telemetry&quot; 的 SSH 密钥，并向攻击者服务器建立反向 SSH 隧道，但由于安装过程需要管理员权限，多数主机上的隧道建立失败。Cursor 已下架该版本、短暂下线整个市场，并在轮换密钥后重新上线，攻击者的服务器目前也已被关停。

telegram · zaihuapd · 10月30日 08:44

**背景**: Open VSX 是微软 VS Code Marketplace 的厂商中立开源替代方案，为 Eclipse Theia、VSCodium 以及 Cursor 等兼容 VS Code 的编辑器提供扩展发布与安装的仓库基础设施。扩展以编辑器自身的权限运行，因此一个被篡改的包无需额外漏洞就能读取文件、执行命令并接触凭据。正因如此，知名扩展名的发布权限成了高价值目标，此前 GlassWorm 系列攻击和 Nx Console 被入侵等事件都表明，攻击者正在同时试探微软市场和 Open VSX。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor">Trojanized Claude Code Extension Plants an SSH Backdoor</a></li>
<li><a href="https://github.com/eclipse-openvsx/openvsx">GitHub - eclipse-openvsx/openvsx: An open-source registry for ...</a></li>
<li><a href="https://explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026">Claude Code Extension 2.1.313 SSH Backdoor : What To... | explainx.ai</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#VS Code extensions`, `#Cursor`, `#malware`, `#security incident`

---

<a id="item-2"></a>
## [苹果 Apple 智能 11 月 4 日在中国开启测试，携手阿里千问](https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/) ⭐️ 8.0/10

苹果宣布，包括实时翻译、照片消除工具和写作工具在内的首批 Apple 智能功能将自 11 月 4 日起随最新的 iOS 开发者 Beta 版在中国开放测试，并将在 12 月 iOS 27.3 正式发布时面向中国用户推出。苹果还与阿里巴巴合作，在 Siri、写作工具和视觉智能中接入千问（通义千问）模型。 这标志着 Apple 智能在备受期待后终于进入中国市场——由于监管要求，苹果不得不依赖本土模型合作伙伴，而非自家基础模型或 OpenAI 的 ChatGPT。与阿里的合作让千问获得了庞大的消费级分发渠道，也为境外 AI 产品如何本地化落地中国树立了一个范本。 中国区其他苹果平台的支持将在获得必要审批后才会推出，而且本次更新并不包含下一代 Siri AI 功能。该功能仅面向在中国购买了支持 Apple 智能的 iPhone 用户，或设备定位与 Apple 账户国家/地区均设置为中国的用户提供。

telegram · zaihuapd · 10月30日 21:44

**背景**: Apple 智能是苹果的一整套 AI 功能，涵盖写作工具、通知摘要、图像生成与消除、视觉智能等，于 2024 年 WWDC 首次发布，依托端侧与服务器混合处理运行。由于中国要求生成式 AI 服务必须向监管部门备案并获批，苹果无法在中国提供自家模型或 ChatGPT 集成，因此转向了获批的本土合作伙伴。千问（通义千问）是阿里云的大语言模型系列，以开源权重版本被广泛使用，中国版 Apple 智能正是由本地部署的千问提供支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alibaba_qwen">Alibaba qwen</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri - Apple</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#China`, `#Alibaba Qwen`, `#iOS`, `#AI partnerships`

---

<a id="item-3"></a>
## [DeepSeek 二轮融资 1055 亿元，估值超 6155 亿元](https://www.theinformation.com/articles/behind-deepseeks-16-billion-funding-chinese-tech-titans-state-players) ⭐️ 7.0/10

据 The Information 披露，DeepSeek 完成第二轮融资，规模达 1055 亿元人民币（约合 160 亿美元），估值突破 6155 亿元，近 30 家投资方参与，包括腾讯（出资 100 亿元）、宁德时代及董事长曾毓群（合计 100 亿元）、长鑫存储、中芯国际、美团、vivo 和小红书等。本轮国资背景资金占比约 27%，远高于今年 6 月完成的首轮（约 510 亿元）的 2%。 这一融资规模和投资方阵容表明，DeepSeek 已成为中国人工智能战略中的“国家队”级资产，中芯国际、长鑫存储等半导体企业入股，意味着模型公司正与本土算力和存储供应链深度绑定。国资背景资金占比从 2% 跃升至约 27%，也说明政策层面正把前沿大模型研发视为战略重点，这可能改变其与阿里巴巴、字节跳动等资金雄厚的中国 AI 实验室之间的竞争格局。 本轮融资规模远超 6 月的约 510 亿元，估值超过 6155 亿元，但报道并未披露优先权、董事会席位等具体条款。投资方横跨互联网平台、动力电池、存储、晶圆代工和消费电子硬件，显示这是一次围绕国产 AI 基础设施的协同布局，而非单纯追求财务回报。

telegram · zaihuapd · 10月30日 12:37

**背景**: DeepSeek 是一家总部位于杭州的大模型公司，2023 年才成立，因 DeepSeek-V3 和 DeepSeek-R1 而广为人知，其训练和推理成本相较海外同类产品极低。大语言模型训练需要海量 GPU 算力和高带宽内存，这正是芯片与存储厂商会战略性地投资或供应大模型公司的原因。长鑫存储（CXMT）总部位于安徽合肥，是中国领先的 DRAM 制造商、按位出货量计算位列全球第四；中芯国际则是中国最大的晶圆代工企业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bianews.com/news/details?id=204884">关于 DeepSeek ，你需要知道的8件事</a></li>
<li><a href="https://zh.wikipedia.org/zh-sg/%E9%95%BF%E9%91%AB%E5%AD%98%E5%82%A8">长 鑫 存 储 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.weex.com/zh-CN/questions/article/what-is-cxmt-and-can-it-challenge-samsung-and-micron-semiconductor-rwa-architecture-bevydjmsunuvanqmhfmsfr3y">什 么 是 长 鑫 存 储 ( CXMT )... | WEEX问答</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI funding`, `#China tech`, `#LLM`, `#venture capital`

---

<a id="item-4"></a>
## [百度网盘摇一摇广告被指改用磁力计绕过传感器权限](https://www.landian.news/archives/127843.html) ⭐️ 7.0/10

有开发者用 AI 分析百度网盘 iOS 版（13.36.0，10 月 22 日发布）的广告跳转逻辑，发现框架中存在一个名为 NoShake（“没有运动”）的变体：它绕开 CoreMotion，改用 Core Location 的 CLHeading 读取磁力计数据来判断手机是否晃动。因此用户即便禁用了陀螺仪和加速度计权限，仍会因晃动而被跳转到广告页面；报告还提到在特定参数下等待约 1 秒就会自动执行广告点击。 这是一个典型的“对抗式”移动广告手法：用户以为关闭运动传感器权限就能阻止摇一摇广告，但磁力计并不在该权限范围内，导致用户授权与系统级传感器管控的意义被削弱。若此类做法被更多 App 效仿，可能侵蚀用户对 iOS 权限弹窗的信任，并促使苹果对传感器访问施加更严格的管控。 该分析仅针对单一 App 版本（iOS 版百度网盘 13.36.0），且借助 AI 辅助完成，尚未在其他 App 或 iOS 版本上得到独立验证。其核心手法依赖 startUpdatingHeading\(\)/CLHeading 的朝向更新，这会让磁力计持续工作并带来耗电代价；同时磁力计数据比加速度计噪声大得多，因此判定很可能采用较粗略的阈值而非精确运动感知。

telegram · zaihuapd · 10月30日 15:00

**背景**: 在 iOS 上，加速度、旋转速率等运动数据通常由 CoreMotion 框架提供，App 需获得用户授予的运动权限才能访问。而用于 GPS 与指南针功能的 Core Location 框架则另外提供 CLHeading，即由磁力计得出的罗盘朝向数据，它受定位权限管辖，而不受“运动与健身”开关控制。“摇一摇跳转广告”在国内是被广泛批评的移动端暗黑模式，手机轻微晃动就会打开第三方电商或游戏 App，不少用户曾尝试通过关闭运动传感器权限来阻止它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@robdeans/measuring-differences-of-degrees-using-cllocations-clheading-5f13f93756d7">Measuring Differences of Degrees Using CLLocation’s CLHeading</a></li>
<li><a href="https://newly.app/sensors/magnetometer-mobile-apps">Magnetometer in Mobile Apps: Compass and Heading — Newly</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/api/corelocation.clheading?view=net-ios-26.5-10.0">CLHeading Class (CoreLocation) | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#privacy`, `#mobile-ads`, `#iOS`, `#sensors`, `#dark-patterns`

---

<a id="item-5"></a>
## [投资者开始区分 AI 增长与 AI 现金创造](https://www.reddit.com/r/finance/comments/1xj1dfj/investors_are_beginning_to_distinguish_between_ai/) ⭐️ 6.0/10

在最新财报发布后，Microsoft 产生了 186 亿美元自由现金流，而 Alphabet 据称烧掉了约 90 亿美元；华尔街随即作出鲜明反应，Microsoft 盘后股价上涨超过 3%，Alphabet 则下跌近 10%。 这种分化表明，投资者不再把所有 AI 相关业务一视同仁，而是开始根据巨额 AI 资本开支能否转化为真实现金回报来给公司定价，这可能重塑大型科技公司的估值逻辑。 这一比较的核心是自由现金流，即经营现金流减去资本开支；因此，即使一家公司 AI 收入增长强劲，只要基础设施支出超过现金创造能力，仍可能出现现金净流出。市场反应也反映的是预期，而非对长期 AI 回报的最终裁决。

reddit · r/finance · /u/zexolyn · 10月30日 00:42

**背景**: 自由现金流是企业在满足经营需求和资本开支后剩余的现金，因此备受关注，因为它体现了可用于分红、回购、偿债或再投资的现金规模。大型科技公司正处于 AI 基础设施投资热潮中，美国最大的几家科技公司已给出数千亿美元级别的资本开支指引，其中很大一部分用于数据中心和 AI 芯片。这种支出即使在高收入增长时也可能压低短期自由现金流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Free_cash_flow">Free cash flow</a></li>
<li><a href="https://www.longtermwiki.com/wiki/E690">Financial Stability Risks from AI Capital Expenditure | Longterm Wiki</a></li>
<li><a href="https://medium.com/@tarifabeach/the-ai-industrial-turn-why-big-techs-2026-capital-spending-signals-a-structural-break-in-the-94362c49f384">The AI Industrial Turn: Why Big Tech’s 2026 Capital ... | Medium</a></li>

</ul>
</details>

**标签**: `#AI economics`, `#big tech`, `#free cash flow`, `#stock market`, `#AI capex`

---

<a id="item-6"></a>
## [盖洛普：美国员工敬业度跌至 29%，创 15 年来新低](https://www.gallup.com/workplace/716117/employee-engagement-below-30-first-time-years.aspx) ⭐️ 6.0/10

盖洛普最新职场调查显示，2026 年第三季度美国员工敬业度降至 29%，为 2011 年以来最低水平，较上一季度下滑 2 个百分点；同时“积极怠工”比例从 17%升至 18%，另有 53%的员工属于“不投入”状态。降幅在远程与混合办公员工中最大，在已经引入 AI 的组织中尤为明显。 敬业度是生产率、员工留存与缺勤率的先行指标，因此 15 年新低意味着实质性的经营风险，而非一时的士气波动——按盖洛普的换算口径，本季度相当于减少了约 320 万名敬业员工。更值得警惕的是，降幅最集中的地方恰好是远程办公与已引入 AI 的组织，这直接挑战了“这些安排必然提升效率”的假设。 目前只有 46%的员工表示清楚知道工作对自己的期望，低于此前水平；仅 37%的人感到上司或同事关心自己——这两项都是盖洛普 Q12 需求层级中的核心条目。盖洛普将每 1 个百分点的敬业度变化折算为约 160 万名美国员工，由此得出本季度敬业员工减少约 320 万人的结论。

telegram · zaihuapd · 10月30日 06:45

**背景**: 盖洛普用 Q12 问卷衡量敬业度，这 12 道题围绕一个职场需求层级展开，从最基本的角色清晰度，逐级上升到被认可、归属感和成长机会；受访者被划分为敬业、不投入和积极怠工三类。盖洛普自 2000 年代初就开始追踪美国这一指数，因此“2011 年以来最低”的对比才有意义，该指标也被人力资源与管理研究者广泛用作衡量员工状态的代理变量。关于 AI 落地的研究普遍发现，敬业度结果很大程度上取决于企业在引入技术时是否提供培训与支持，而非技术本身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gallup.com/workplace/356063/gallup-q12-employee-engagement-survey.aspx">Gallup&#x27;s Q12 Employee Engagement Survey</a></li>
<li><a href="https://www.gallup.com/workplace/321725/gallup-q12-meta-analysis-report.aspx">Q12 Meta-Analysis | 11th Edition - Gallup</a></li>
<li><a href="https://www.bsm.upf.edu/documents/2023-manuscript-ai-adoption-engagement.pdf">Manuscript_AI Adoption and Engagement - UPF-BSM</a></li>

</ul>
</details>

**社区讨论**: 围绕这条消息的讨论简短而带有质疑，读者对“AI 带来效率提升”的说法表示怀疑——既然敬业度下滑最严重的恰恰是那些引入 AI 的组织，那么当初承诺的效率提升究竟体现在哪里。

**标签**: `#employee-engagement`, `#remote-work`, `#AI-adoption`, `#workplace-trends`, `#Gallup`

---

<a id="item-7"></a>
## [小米开源 0.8B 文档理解模型 Xiaomi-OCR-0](https://x.com/XiaomiTech_/status/2116154468358316380) ⭐️ 6.0/10

小米开源了 Xiaomi-OCR-0，这是一个 0.8B 参数的统一视觉语言模型，面向文档解析与以 OCR 为核心的理解任务，并同步放出了模型权重、推理代码和演示。该模型基于 Qwen3.5-0.8B 构建，小米称其在 OmniDocBench v1.6 的文档解析评测中位居 10 亿参数以下模型第一，同时还支持关键信息提取和 OCR 视觉问答。 一个能在单一模型中完成解析、信息抽取和 OCR 视觉问答的 10 亿参数以下模型，对于端侧、边缘以及成本敏感的文档处理流水线很有吸引力——在这些场景中，前沿多模态模型要么太贵、要么体积太大而难以部署。同时，由大厂提供完整的开放权重和推理代码，也为开发者提供了一个可复现的基线，用来与更大的闭源 OCR 服务做对比。 根据技术报告和代码仓库，Xiaomi-OCR-0 以 Qwen3.5-0.8B 为起点，使用由自动化数据引擎构建的约 1.7 亿样本的 OCR 语料进行训练，该数据引擎结合了专家共识、基于渲染的校验和定向合成，并采用 Q-Mask 文本锚定、持续预训练（CPT）以及混合任务强化学习（Mix-RL）。所谓在 OmniDocBench v1.6 上位居 10 亿参数以下第一，目前是小米自己的说法，简短公告并未给出分任务消融实验、时延或显存占用数据，因此仍需第三方独立验证。

telegram · zaihuapd · 10月30日 16:00

**背景**: 传统 OCR 通常是由版面检测、文字识别和后处理组成的多阶段流水线，而近期的多模态视觉语言模型可以直接读取整页图像并输出结构化结果。OmniDocBench 在 CVPR 2025 上提出，用于在多样化 PDF 版面上评测文本、公式、表格和阅读顺序等文档解析能力，其总分由编辑距离、CDM 和 TEDS 等子指标综合而成。OCR 视觉问答（OCR-VQA）是一项相关任务，要求模型通过读取图像中的文字来回答问题，同时考验识别能力与对识别内容的推理能力。10 亿参数级别的小模型之所以重要，是因为它们有望在本地或廉价硬件上运行，而大量真实世界的文档处理恰恰发生在这些环境中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xiaomi-research/Xiaomi-OCR-0">GitHub - xiaomi-research/Xiaomi-OCR-0: Xiaomi-OCR-0 · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2609.36136">[2609.36136] Xiaomi-OCR-0 Technical Report - arXiv.org</a></li>
<li><a href="https://github.com/opendatalab/OmniDocBench">GitHub - opendatalab/OmniDocBench: [CVPR 2025] A ...</a></li>

</ul>
</details>

**标签**: `#open-source-models`, `#document-understanding`, `#OCR`, `#small-language-models`, `#multimodal`

---

<a id="item-8"></a>
## [Claude 将 Max 套餐更名为 Max 与 Ultra，验证版 Ultra 取消五小时用量限制](https://x.com/claudeai/status/2116220869479428500) ⭐️ 6.0/10

Anthropic 对 Claude Max 订阅套餐进行了更名：原来的 Max 5x 现在叫「Max」，Max 20x 现在叫「Ultra」，价格保持每月 100 美元和 200 美元不变，现有订阅者无需做任何操作。从 10 月 30 日起，已通过验证的 Ultra 账户不再受 5 小时用量限制，多数现有订阅者会优先被覆盖。 这次改名把容易混淆的 5x/20x 命名简化，让顶配套餐更容易与竞品对比；而取消 5 小时上限则直接针对那些在 Claude Code 中长时间运行智能体任务的超重度用户。这属于套餐设计与使用政策的调整而非模型升级，但会影响重度用户和团队最终选择付费哪一档。 即便对已通过验证的 Ultra 账户，每周用量限制依然保持不变，因此这次取消的是短周期滚动窗口的上限，而非总体用量上限。新账户在通过验证前仍会保留临时用量限制，用于防范欺诈与滥用，限制解除时用户会收到邮件通知。

telegram · zaihuapd · 10月30日 17:44

**背景**: Claude Max 是 Anthropic 位于标准 Pro 计划之上的高用量订阅档位，面向那些在高强度工作中很快撞到 Pro 用量上限的用户。原来的「5x」与「20x」标签指的是相对 Pro 用量额度的倍数，这一命名方式让不少用户难以理解。与 ChatGPT、Gemini 类似，Claude 过去一直采用两层限制结构：一个是短周期滚动窗口（例如五小时），另一个是每周上限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codepick.dev/zh/guides/claude-max-plan-value-analysis/">Claude Max 套 餐 性价比分析（2026... | CodePick</a></li>
<li><a href="https://maplefeather.com/article/chatgpt-plus-usage-limits-5hour-weekly-2026">ChatGPT 5 小 時上 限 回來了：Plus 額度怎麼 算 、我撞牆先做什麼 | 夜羽凌</a></li>
<li><a href="https://support.claude.com/zh-CN/articles/8325606-pro-%E8%AE%A1%E5%88%92%E6%98%AF%E4%BB%80%E4%B9%88">Pro 计 划 是 什 么 ？ | Anthropic Help Center</a></li>

</ul>
</details>

**标签**: `#anthropic`, `#claude`, `#ai-products`, `#pricing`, `#usage-limits`

---