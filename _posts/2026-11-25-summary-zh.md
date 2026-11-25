---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25 23:03:35 +0000
lang: zh
report: default
---

> 从 156 条内容中筛选出 8 条重要资讯。

---

1. [Minecraft Java 版曝高危 RCE：恶意资源包字体可执行任意代码](#item-1) ⭐️ 8.0/10
2. [美商务部被曝威胁英特尔交出 10% 股权](#item-2) ⭐️ 8.0/10
3. [SpaceX 与特斯拉各自组建特别委员会，洽谈 3.5 万亿美元全股票合并](#item-3) ⭐️ 7.0/10
4. [三星电子与 SK 海力士将采用长江存储 Xtacking 键合技术生产 3D NAND](#item-4) ⭐️ 7.0/10
5. [LeCun 抨击 Amodei 借 AI 风险论封杀开源模型](#item-5) ⭐️ 6.0/10
6. [SpaceX 放弃 7.38 亿美元 BEAD 补贴，改为免费发放星链终端](#item-6) ⭐️ 6.0/10
7. [OpenAI 押注网络安全，称其将成为比编程更大的业务板块](#item-7) ⭐️ 6.0/10
8. [美国收紧芯片漏洞后，亚洲数据中心转向美国客户兜售过剩算力](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Minecraft Java 版曝高危 RCE：恶意资源包字体可执行任意代码](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

11 月 22 日，一个名为 minecraft2shell 的概念验证项目被公开，显示服务器资源包中特制的 TrueType 字体可以触发 FreeType 2.14.3 及更早版本的原生越界写，从而在 Minecraft Java 版 26.3 Windows 客户端上执行任意代码。受影响的版本为 1.20.5 至 1.21.10 以及 26.1 至 26.4 快照，1.20.4 及更早版本与基岩版不受影响。 这是一个远程代码执行漏洞，受害者只需加入服务器或加载资源包即可被攻击，因此任何多人服务器运营者或连接不受信任服务器的玩家都面临风险。由于 Mojang 仍在使用 lwjgl-freetype 3.4.3 且暂无官方补丁，目前唯一的防御手段是禁用服务器资源包或安装社区临时修复。 漏洞根因位于 FreeType 的 hinting 处理路径，而非 Minecraft 自身的 Java 代码，这也是攻击能够从 Java 托管代码跨越到原生内存的原因。社区修复 m2sfix 1.0.0 已于 11 月 24 日发布，可作为 Java agent 或直接关闭 hinting 的 mod 使用；公开披露还建议玩家在官方修复发布前不要添加任何资源包，并将多人游戏服务器资源包权限设为“禁用”。

telegram · zaihuapd · 11月25日 12:46

**背景**: FreeType 是一个被广泛使用的开源 C 语言字体渲染库，Minecraft Java 版通过 lwjgl-freetype 这一 LWJGL 绑定来调用它完成文字光栅化。TrueType 字体可以携带 hinting 指令，即一段在渲染时调整字形的小型字节码程序，而 FreeType 以原生代码执行这些逻辑，因此畸形的字体文件能够破坏 Java 沙箱之外的内存。Minecraft 服务器可以向连接的客户端推送资源包（包括自定义字体），这就使字体文件成为原生漏洞的投递载体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://freetype.org/">The FreeType Project: a free , high-quality and portable Font engine</a></li>
<li><a href="https://vuldb.com/ja/vuln/299266">CVE -2025-27363 FreeType メモリ破損 (Nessus ID 232845)</a></li>
<li><a href="https://mcasset.cloud/1.21.4/1.21.4.json">View Minecraft json asset 1.21.4.json from version 1.21.4 via mcasset....</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#minecraft`, `#freetype`, `#rce`

---

<a id="item-2"></a>
## [美商务部被曝威胁英特尔交出 10% 股权](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 8.0/10

法庭文件显示，2025 年 8 月美国商务部一名律师在与英特尔首席财务官的电话中表示，不要“误以为这是一场谈判”，并称总统希望周五就宣布协议；他还说董事会可以拒绝，但提醒这将带来无法预测的后果。几天后英特尔董事会交出了这批股份，特朗普随后宣布美国政府“完全拥有并控制英特尔 10% 的股份”，且美方没有为此支付任何费用，这批股份现值约 110 亿美元。 这标志着美国产业政策的一次范式转变：华盛顿似乎并非通过立法或公开市场收购，而是以赤裸裸的施压手段取得了一家美国旗舰芯片企业的股权。这直接引发了对英特尔公司治理的质疑，也开了一个先例，可能笼罩着每一家依赖美国政府补贴、合同或出口许可的半导体企业。 据 WIRED 所依据的法庭文件，美方没有为这批股份支付任何费用，其现值约 110 亿美元，而且施压是通过电话口头进行的，并非书面协议。这些说法来自诉讼文件，因此具体措辞和法律定性仍存争议，目前也不清楚这 10% 股权附带何种正式条款、投票权或董事会席位。

telegram · zaihuapd · 11月25日 13:25

**背景**: 美国商务部是负责执行半导体产业政策的机构，掌管芯片补贴与出口管制，因此对英特尔这类企业拥有巨大的影响力。英特尔是美国最大的先进处理器制造商，也是华盛顿推动先进芯片制造留在本土的关键支柱。在美国，政府直接持有一家私营企业的股权极为罕见——传统上，政策扶持通过拨款、贷款、税收抵免和采购来实现，而非持股。

**标签**: `#semiconductors`, `#Intel`, `#US policy`, `#tech regulation`, `#geopolitics`

---

<a id="item-3"></a>
## [SpaceX 与特斯拉各自组建特别委员会，洽谈 3.5 万亿美元全股票合并](https://thenextweb.com/news/spacex-tesla-merger-five-directors-special-committees) ⭐️ 7.0/10

据报道，SpaceX 与特斯拉已各自选定五名董事组成特别委员会，就一项规模达 3.5 万亿美元的全股票合并展开谈判，并力争在年底前敲定交易。若交易达成，这将是企业史上规模最大的合并。 这笔交易若成真，将把马斯克旗下两家最有价值的公司合并为一个估值可与全球最大上市公司比肩的实体，从而重塑投资者对航天发射业务以及电动车与能源业务的估值方式。鉴于两家公司由同一人控制，交易还会在股东权利、公司治理和指数权重等方面引发高度集中的疑问。 这两个委员会仍需确定换股比例、争取股东支持，并防范类似马斯克此前交易引发的投资者诉讼；知情人士称，双方目前尚未接近达成协议。相关条款尚未得到两家公司确认，因此目前的估值与交易结构仍应视为传闻。

telegram · zaihuapd · 11月25日 00:41

**背景**: 在关联方交易（即两家公司共享控制人或管理层存在重叠的“利益冲突”交易）中，董事会通常会设立独立的特别委员会，评估交易条件对少数股东是否公平，因为这类决策不仅关乎商业价值，同样关乎决策过程的独立性。全股票合并意味着股东收到的是合并后公司的股份而非现金，因此核心谈判变量是换股比例，即把两家公司各自的股份折算为新公司股票的比例。此外，一家上市公司与 SpaceX 这样股权高度集中的公司合并，还会牵涉信息披露、估值以及上市安排等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gate.com/zh/learn/articles/how-special-committees-review-related-party-mergers">特别委员会如何审查关联方并购？从利益冲突到股东权益保护</a></li>
<li><a href="https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E/all-stock">ALL-STOCK在劍橋英語詞典中的解釋及翻譯</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Tesla`, `#Merger`, `#Musk`, `#Business`

---

<a id="item-4"></a>
## [三星电子与 SK 海力士将采用长江存储 Xtacking 键合技术生产 3D NAND](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

据报道，三星电子与 SK 海力士已通过交叉许可协议，同意在 3D NAND 闪存生产中采用长江存储（YMTC）Xtacking 键合技术的部分内容。三方均对此拒绝置评，但有观点认为，与传统 NAND 制造工艺相比，键合技术路线优势明显。 若消息得到证实，这将是一次罕见的技术流向逆转——全球两大主导存储厂商采用一家中国厂商首创的技术路线，而在过去，韩国企业长期引领工艺创新。同时，这也为“晶圆对晶圆混合键合”作为 3D NAND 的替代性微缩路径增添了说服力，尤其是在传统横向微缩与层数堆叠日益困难的情况下。 Xtacking 的做法是把存储单元阵列与控制外围电路（CMOS）分别制作在两片晶圆上，再通过键合工艺合二为一，两部分可以各自独立生产与优化。Omdia 一位高级分析师指出，这让厂商可以自行生产存储阵列，而把逻辑电路交给晶圆代工厂，从而用上更先进的制程。

telegram · zaihuapd · 11月25日 14:33

**背景**: 3D NAND 闪存通过垂直堆叠存储单元来提高密度，厂商传统上依靠增加层数和横向缩小特征尺寸来微缩。长江存储于 2018 年推出的 Xtacking 则把存储阵列晶圆与外围 CMOS 晶圆分开制造，再用细间距铜-铜互连键合在一起——这正是先进芯片封装中日益流行、用于替代硅通孔（TSV）的混合键合原理。由于逻辑部分与存储部分不再共享同一套热预算和工艺流程，两者可以各自采用最优制程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ymtc.com/en/technicalintroduction.html">About Xtacking ®- YMTC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://spectrum.ieee.org/hybrid-bonding">Hybrid Bonding: 3D Chip Tech to Save Moore&#x27;s Law - IEEE Spectrum</a></li>

</ul>
</details>

**标签**: `#3D NAND`, `#semiconductor manufacturing`, `#hybrid bonding`, `#YMTC`, `#memory industry`

---

<a id="item-5"></a>
## [LeCun 抨击 Amodei 借 AI 风险论封杀开源模型](https://x.com/ylecun/status/2124550037912920090) ⭐️ 6.0/10

11 月 22 日，Yann LeCun 在 X 上发帖，指责 Anthropic CEO Dario Amodei 自 GPT-2 时期起就靠渲染 AI 危险性来推动将开放模型定为非法，以维持自身掌控，并称 Amodei 当年离开 OpenAI 是因为在那里拿不到控制权。他还把这种做法比作奥斯曼帝国禁止阿拉伯语印刷，称之为「一种新形式的中世纪蒙昧主义」。 这场交锋让两位 AI 领域最具影响力的人物站到了「开放权重」与「闭源模型」政策之争的对立面，而这场争论正日益影响监管规则、许可方式以及谁能构建前沿系统。由于 LeCun 如今已自立门户创办实验室，他的抨击也表明开放阵营会继续把安全论调描绘成「监管俘获」。 这条帖子只是纯粹的社交媒体抨击，背后没有技术论证或附带分析支撑，其依据是关于 Amodei 动机的个人指控和一个历史类比，而非有关模型风险的证据。它出台的时机也恰逢以 Meta 为代表的开放权重阵营与以 OpenAI、Anthropic 为代表的闭源阵营不仅比拼基准成绩，还在争夺公众叙事主导权。

telegram · zaihuapd · 11月25日 01:30

**背景**: Yann LeCun 是法裔美国计算机科学家，凭借 1980 年代末在卷积神经网络（尤其是用于读取手写数字与支票的 LeNet）上的工作，与 Geoffrey Hinton、Yoshua Bengio 共同获得 2018 年图灵奖。他在 Meta 担任了 12 年首席 AI 科学家，2025 年 11 月离职后联合创办了总部位于巴黎、专注「世界模型」的 AMI Labs，该公司在 2026 年初融资超过 10 亿美元。争论的核心在于：公开发布模型权重究竟会带来不可接受的安全风险，还是能通过外部审查提升安全性——对于这个问题，闭源模型开发商 Anthropic 的答案远比 Meta 等开放权重支持者谨慎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Machine_Intelligence_Labs">Advanced Machine Intelligence Labs - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/LeNet">LeNet - Wikipedia</a></li>
<li><a href="https://humphreytheodore.com/writing/open-weight-ai-models-safety-regulatory-capture-2026">The Open Weight AI Fight Is About Regulatory Capture</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open source AI`, `#AI safety debate`, `#Yann LeCun`, `#industry commentary`

---

<a id="item-6"></a>
## [SpaceX 放弃 7.38 亿美元 BEAD 补贴，改为免费发放星链终端](https://x.com/SawyerMerritt/status/2125314062997467640) ⭐️ 6.0/10

SpaceX 已同意在美国国家电信与信息管理局（NTIA）的 BEAD 计划下签署一份「零支出协议」，放弃 7.38 亿美元联邦宽带补贴，联邦实际拨付金额为 0 美元。作为交换，该公司承诺向符合条件的美国家庭免费提供星链终端，保证至少 100 Mbps 下载、20 Mbps 上传的服务，推出低价月费套餐，并承诺服务 10 年。 这笔交易展示了一种新的公共宽带资金模式：运营商用现金换监管松绑，这可能成为其他 BEAD 申请方效仿的模板，并改变剩余补贴资金在农村覆盖上的投向。它同时强化了星链作为「无需补贴即免费」选项的地位，在难以覆盖的地区与光纤和有线运营商展开竞争。 SpaceX 并非完全豁免：它仍须遵守与其他 BEAD 受资助方相同的交付时间表，并继续接受网络性能测试，但可免于大部分财务审计、采购和行政报告义务。这些承诺期限为 10 年，并包含低价套餐要求，与 BEAD 拨款通常附带的可负担性条件相一致。

telegram · zaihuapd · 11月25日 02:17

**背景**: BEAD（宽带公平、接入与部署）计划由 2021 年《基础设施投资与就业法案》设立，拨款约 425 亿美元供各州资助宽带建设，其规则历来偏向光纤，并对高时延技术不利。星链等卫星运营商长期争取被认定为合格受资助方，理由是它们能覆盖铺设光纤成本过高的地点。BEAD 拨款通常附带大量审计、采购规则和报告义务，受资助方常抱怨这些要求成本高、进度慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://broadbandusa.ntia.gov/funding-programs/broadband-equity-access-and-deployment-bead-program">Broadband Equity Access and Deployment Program | BroadbandUSA</a></li>
<li><a href="https://www.fierce-network.com/broadband/ntia-toots-its-own-horn-regard-bead-or-it-swan-song">NTIA toots its own horn in regard to BEAD . Or is it a swan song?</a></li>
<li><a href="https://starlink.com/service-plans">Service Plans - Starlink</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#broadband-policy`, `#BEAD`, `#satellite-internet`

---

<a id="item-7"></a>
## [OpenAI 押注网络安全，称其将成为比编程更大的业务板块](https://www.theinformation.com/newsletters/ai-agenda/openais-roadmap-making-cyber-bigger-coding-remains-blurry) ⭐️ 6.0/10

OpenAI 正将网络安全定位为下一个主要增长引擎：公司高管称外界对网络安全市场规模超过 3000 亿美元的估算仍被严重低估，并认为网络安全将成为 OpenAI 比编程更大的业务板块。公司已推出面向安全研究的 GPT-6 Cyber，并持续扩大 Daybreak 受信访问计划，截至今年 9 月已覆盖数千名经过审核的防御者以及约 2000 个获批组织与工作空间。 如果 OpenAI 能把安全业务做成比编程更大的板块，其收入结构将从开发者工具转向直接与老牌安全厂商以及 Anthropic、Google 竞争。与此同时，强调“经审核、分层开放”的访问方式也说明，前沿实验室正把网络攻防能力视为需要按信任等级限量发放、而非公开售卖的产品。 Daybreak 按信任等级划分为 Daybreak Blue 与 Daybreak Red 等层级，能力更强的网络专用模型（如 GPT-5.6 Cyber 别名以及基于 GPT-6 Astra 的 GPT-6 Cyber）只向获批防御者开放，用于漏洞发现、漏洞利用验证、代码库分析与二进制逆向等获得授权的工作。报道同时指出，OpenAI 相对 Anthropic 和 Google 的竞争态势以及规模化商业化的路径仍不清晰。

telegram · zaihuapd · 11月25日 04:51

**背景**: GPT-6 Cyber 是 OpenAI GPT-6 Astra 模型的网络专用变体，经过专门的后训练以增强安全能力并减少拒答，从而能在授权范围内完成漏洞发现、漏洞利用开发与 Web 渗透测试等任务。Daybreak 则是管控这些模型的受信访问计划：机构需申请并通过审核，再被划入不同层级（Blue 与 Red），由此决定可以使用哪些网络能力与 API 模型。之所以要这样分级，是因为攻防安全能力具有两用性——能帮防御者打补丁的模型，同样能帮攻击者找漏洞。这一消息的背景是前沿模型竞争日趋拥挤，Anthropic 与 Google 也在向安全团队推销类似模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-cyber/">GPT‑6 Cyber: Advancing the frontier of aligned ... - OpenAI</a></li>
<li><a href="https://deploymentsafety.openai.com/gpt-6-cyber">GPT-6 Cyber System Card - OpenAI Deployment Safety Hub</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#cybersecurity`, `#AI industry strategy`, `#business`, `#AI agents`

---

<a id="item-8"></a>
## [美国收紧芯片漏洞后，亚洲数据中心转向美国客户兜售过剩算力](https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand) ⭐️ 6.0/10

美国政府收紧了一项曾让中国科技公司获得英伟达最先进芯片的出口漏洞后，亚洲多地数据中心运营商正争相把过剩的 AI 算力转售给美国买家。算力交易平台 Liquid Compute 首席执行官 Ronit Jain 表示，针对该地区先进 AI 加速器出口的新规，正冲击那些原本指望把算力租给中国客户的数据中心服务商。 这一转变显示出口管制正在重塑全球 AI 算力版图：那些为服务中国需求而在第三国建设的算力，如今必须寻找新买家，这可能在一定程度上缓解美国的 GPU 短缺或压低算力价格。同时，这也让外界开始关注那些商业模式依赖中国持续需求的亚洲新兴云服务商的财务健康。 美国工业与安全局（BIS）于 2026 年 11 月 18 日发布的临时最终规则，对向服务中国等受限国家客户的海外数据中心供应先进 GPU 设定了许可要求，并将管制范围扩大到另外五个国家的所有终端用户。Liquid Compute 自称在构建一个具备验证、清算与结算能力的受监管算力交易所，正把自己定位为将这类“闲置算力”与美国买家撮合的市场。

telegram · zaihuapd · 11月25日 11:35

**背景**: 美国对先进 AI 芯片的出口管制按国家安全风险把各国划分为不同层级，因此经由马来西亚、新加坡等中间层级地区转运的芯片，此前可以在不受对华严格限制的情况下运行，中国企业正是利用这一缺口在海外训练模型。2026 年 11 月的新规正式废止了此前的“AI 扩散规则”，代之以针对服务受限国家客户的海外数据中心的定向许可要求。许多亚洲数据中心运营商此前是基于中国 AI 公司会租用其算力的假设来建设或扩张产能，因此在规则收紧后风险敞口很大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.skadden.com/insights/publications/2026/11/ai-diffusion-2-bis-introduces-new-export-controls">‘AI Diffusion’ 2.0: BIS Introduces New Export Controls on ...</a></li>
<li><a href="https://abhs.in/blog/bytedance-36000-nvidia-b200-chips-malaysia-us-export-controls-2026">ByteDance Routes 36,000 Nvidia B200 Chips Through Malaysia to...</a></li>
<li><a href="https://liquidcompute.com/">Liquid Compute</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#export controls`, `#data centers`, `#Nvidia`, `#geopolitics`

---