---
layout: default
title: "Horizon Summary: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
report: default
---

> 从 336 条内容中筛选出 9 条重要资讯。

---

1. [AI 发现 NIST 后量子候选算法 HAWK 严重弱点](#item-1) ⭐️ 9.0/10
2. [谷歌 DeepMind 发布 Gemini Robotics 2，实现机器人全身智能控制](#item-2) ⭐️ 9.0/10
3. [美国参议员警告苹果不要采购中国内存芯片](#item-3) ⭐️ 8.0/10
4. [Google DeepMind 解散 AlphaFold 团队，核心成员跳槽 Anthropic](#item-4) ⭐️ 8.0/10
5. [欧盟启动 AI 超级工厂招标，拟撬动 300 亿欧元投资](#item-5) ⭐️ 8.0/10
6. [英国监管机构拟强制苹果开放 App Store 外部支付](#item-6) ⭐️ 7.0/10
7. [澳大利亚起诉 Telegram 涉恐内容，最高罚款 5460 万澳元](#item-7) ⭐️ 7.0/10
8. [美委员会代表团访华遭华为、DeepSeek 等拒见](#item-8) ⭐️ 6.0/10
9. [滴滴通报上半年反舞弊：50 余人被清退，40 余人移送公安](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [AI 发现 NIST 后量子候选算法 HAWK 严重弱点](https://startupfortune.com/claude-mythos-broke-hawk-and-the-nist-post-quantum-timeline-may-not-survive-it/) ⭐️ 9.0/10

Anthropic 的 Claude Mythos Preview 模型在约 60 小时内发现了后量子签名算法 HAWK 的严重弱点，将其有效密钥强度从 2^64 降至 2^38，而人类专家此前两年未能发现。 这一突破表明，AI 可以大幅加速密码分析，可能改变后量子密码标准化的时间表，并推动更快地采用抗量子算法。 该攻击花费了约 10 万美元的 API 费用，且不是多项式时间攻击，因此更大的密钥尺寸仍然安全；HAWK 尚未被撤回，该发现仅影响 256 位变体。

telegram · zaihuapd · 7月30日 05:47

**背景**: NIST 正在领导多轮标准化流程，选择能够抵御量子计算机攻击的后量子密码算法。HAWK 是“附加数字签名”阶段第 3 轮中的一种基于格的数字签名候选算法。Claude Mythos Preview 是 Anthropic 开发的 AI 模型，在网络安全（包括漏洞发现）方面具有专门能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/">Mythos attack on 3rd-round PQC algorithm candidate puts it ...</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post - Quantum Cryptography | CSRC</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#AI`, `#post-quantum`, `#NIST`, `#cybersecurity`

---

<a id="item-2"></a>
## [谷歌 DeepMind 发布 Gemini Robotics 2，实现机器人全身智能控制](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 9.0/10

谷歌 DeepMind 发布了 Gemini Robotics 2 系列模型，首次实现对完整人形机器人的全身智能控制，包括行走、下蹲和抓取等动作。该系列包含视觉-语言-动作模型、具身推理模型 ER 2 以及可快速适配的端侧模型。 这标志着具身 AI 的重大飞跃，将感知、推理和控制统一到人形机器人的单一框架中。多机器人协作和开放 API 降低了开发门槛，有望加速智能机器人在制造、医疗和服务行业的实际部署。 ER 2 可通过 Gemini API 和 Google AI Studio 访问，而 VLA 和端侧模型面向早期合作伙伴开放。ASIMOV-Agentic 安全基准测试模型的安全工具拒绝能力和有人靠近时自动停止的能力。

telegram · zaihuapd · 7月30日 16:14

**背景**: Gemini Robotics 2 基于谷歌 DeepMind 之前的 RT-2 等工作构建，RT-2 是一种视觉-语言-动作（VLA）模型，可直接从视觉和文本输入输出机器人动作。具身推理模型（ER）作为高层规划器，负责管理持续数分钟的多步任务。端侧模型允许通过少量示例快速适配新的机器人平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision_language_action_model">Vision language action model</a></li>
<li><a href="https://arstechnica.com/ai/2026/07/google-reveals-gemini-robotics-2-0-promising-improved-dexterity-and-safety/">Google reveals Gemini Robotics 2.0, promising... - Ars Technica</a></li>
<li><a href="https://www.humanoidsdaily.com/news/google-deepmind-unveils-gemini-robotics-2-bringing-whole-body-intelligence-and-multi-robot-teams-to-physical-ai">Google DeepMind Unveils Gemini Robotics... | Humanoids Daily</a></li>

</ul>
</details>

**标签**: `#robotics`, `#deepmind`, `#embodied AI`, `#humanoid`, `#machine learning`

---

<a id="item-3"></a>
## [美国参议员警告苹果不要采购中国内存芯片](https://www.bloomberg.com/news/articles/2026-07-29/senators-warn-apple-not-to-buy-memory-chips-from-chinese-firms) ⭐️ 8.0/10

美国两党参议员致信苹果 CEO 蒂姆·库克，要求苹果放弃向中国长鑫存储（CXMT）和长江存储（YMTC）采购内存芯片的计划，即使仅用于在中国市场销售的设备也不允许。此举正值全球内存供应吃紧、价格上涨之际，苹果已于 2026 年 6 月上调了多款产品的价格。 这突显了中美科技脱钩的升级，直接影响苹果的供应链战略，可能削弱其获取低成本内存芯片的能力。如果苹果遵从，可能会面临更高的成本或供应限制；如果不遵从，则可能招致政治反弹。 参议员要求苹果在 8 月 21 日前承诺不采用长鑫存储和长江存储的芯片，并说明资格认证及技术信息共享情况。两家公司均被五角大楼列入与中国军方有关的实体名单。

telegram · zaihuapd · 7月30日 06:12

**背景**: 长鑫存储（CXMT）是一家中国 DRAM 制造商，长江存储（YMTC）则生产 3D NAND 闪存。美国政府以军民融合为由将它们列入实体清单，限制美国公司在没有许可证的情况下与其交易。苹果作为内存芯片的重要买家，一直在与这些公司谈判以在全球缺货背景下实现供应多元化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/10406299355">美国政府对华136家半导体制裁名单汇总（含中文翻译）</a></li>

</ul>
</details>

**标签**: `#Apple`, `#semiconductors`, `#US-China trade`, `#supply chain`, `#memory chips`

---

<a id="item-4"></a>
## [Google DeepMind 解散 AlphaFold 团队，核心成员跳槽 Anthropic](https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33?syn-25a6b1a6=1) ⭐️ 8.0/10

Google DeepMind 已解散其获得诺贝尔奖的 AlphaFold 团队，大部分研究人员被重新分配到 Gemini 和 Isomorphic Labs 等项目，而三位核心成员 John Jumper、Jonas Adler 和 Alexander Pritzel 已加入竞争对手 Anthropic。 此举标志着 DeepMind 在 AI 研究优先级的战略转变，可能减缓蛋白质结构预测的进展，同时 Anthropic 获得顶尖人才以推进其自身 AI 能力。 近四分之一原 AlphaFold 论文作者已完全离开 DeepMind。内部转岗包括 Gemini、酶设计、核聚变和基因组学等角色，以及 Alphabet 旗下的药物研发公司 Isomorphic Labs。

telegram · zaihuapd · 7月30日 07:45

**背景**: AlphaFold 是 DeepMind 开发的 AI 系统，能从氨基酸序列高精度预测蛋白质结构，使 Demis Hassabis 和 John Jumper 获得 2024 年诺贝尔化学奖。最初于 2020 年发布的 AlphaFold 2 彻底改变了计算生物学。此次解散反映了 DeepMind 将资源重新分配到其他 AI 研究领域，如大语言模型和药物发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>

</ul>
</details>

**标签**: `#AlphaFold`, `#Google DeepMind`, `#Anthropic`, `#AI research`, `#Nobel Prize`

---

<a id="item-5"></a>
## [欧盟启动 AI 超级工厂招标，拟撬动 300 亿欧元投资](https://www.wsj.com/world/europe/eu-opens-call-for-creation-of-local-ai-gigafactories-c286213d) ⭐️ 8.0/10

欧盟委员会启动招标，计划建设最多七座 AI 超级工厂，预计撬动约 300 亿欧元总投资，其中 100 亿欧元来自欧盟和成员国资金。投标截止日期为 11 月 12 日，中标结果预计 2027 年 7 月公布，项目须在签约后 18 个月内投入运营。 这一重大投资旨在通过建设本地 AI 基础设施，提升欧盟在人工智能领域的竞争力，以追赶美国和中国。它可能加速欧洲的 AI 发展，并减少对外部计算资源的依赖。 招标分为选址和扩建两个阶段，最多支持七座工厂。预计总投资为 300 亿欧元，其中仅 100 亿欧元来自公共资金，其余来自私人投资。

telegram · zaihuapd · 7月30日 11:50

**背景**: AI 超级工厂是成千上万甚至几十万块 GPU 高效协同的大规模集群，用于训练大型 AI 模型，类似于 AI 的“数字产品生产线”。欧盟正寻求建立自己的 AI 计算能力，以在全球竞争中立足并减少对外国基础设施的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260730-%E6%AC%A7%E7%9B%9F%E5%90%AF%E5%8A%A8300%E4%BA%BF%E6%AC%A7%E5%85%83ai%E8%B6%85%E7%BA%A7%E5%B7%A5%E5%8E%82%E8%AE%A1%E5%88%92-%E6%B3%95%E5%9B%BD%E7%A7%AF%E6%9E%81%E5%8F%82%E4%B8%8E">欧盟启动300亿欧元AI超级工厂计划 法国积极参与 - RFI - 法国国际广播...</a></li>
<li><a href="https://news.qq.com/rain/a/20260730A0A4XF00">欧盟计划投资 100 亿欧元建设 7 座 AI 超级工厂，发力追赶中美</a></li>
<li><a href="https://m.jiemian.com/article/12602364.html">200亿欧元，13个超级工厂，欧盟加码投资AI | 界面 · 财经号</a></li>

</ul>
</details>

**标签**: `#AI`, `#EU`, `#infrastructure`, `#investment`, `#policy`

---

<a id="item-6"></a>
## [英国监管机构拟强制苹果开放 App Store 外部支付](https://www.macrumors.com/2026/07/29/app-store-uk-rules-highly-intrusive/) ⭐️ 7.0/10

英国竞争与市场管理局（CMA）提议要求苹果允许开发者在 App Store 内使用外部支付方式，旨在降低费用并增加竞争。苹果强烈反对，称这些规则属于“高度介入”且等同于定价管制。 这一监管举措可能从根本上改变 App Store 商业模式，有可能降低苹果向开发者收取的 30%佣金。如果实施，将为全球其他监管机构树立先例，影响苹果的收入和整个应用生态系统。 CMA 提议苹果仍可向开发者收费，但费用必须“公平合理”且低于现有佣金。相关方案同样适用于谷歌，CMA 仍在评估意见，尚未作出最终决定。

telegram · zaihuapd · 7月30日 02:10

**背景**: App Store 是苹果 iOS 应用的主要分发平台，苹果要求所有数字商品的应用内购买必须使用其自有支付系统，并收取 15%至 30%的佣金。这一做法在美国、欧盟等多个国家面临反垄断审查，监管机构认为其抑制了竞争并推高了价格。

**标签**: `#app-store`, `#regulation`, `#UK`, `#Apple`, `#antitrust`

---

<a id="item-7"></a>
## [澳大利亚起诉 Telegram 涉恐内容，最高罚款 5460 万澳元](https://www.reuters.com/world/asia-pacific/australia-begins-legal-action-against-telegram-over-alleged-pro-terror-material-2026-07-30/) ⭐️ 7.0/10

澳大利亚网络监管机构 eSafety 专员办公室对 Telegram 提起诉讼，指控其未能删除宣扬恐怖主义的内容，寻求最高 5460 万澳元（约 3800 万美元）的民事罚款。诉讼称，2025 年 7 月至 10 月间，用户举报的 12 条涉恐帖文中，Telegram 未删除其中 10 条，也未封禁相关账号。 此案可能为澳大利亚乃至全球的即时通讯平台内容审核义务树立重要先例。它凸显了平台安全措施与言论自由之间的张力，可能影响未来的监管政策。 投诉涉及 2025 年 7 月至 10 月间报告的 12 条帖文，其中 10 条据称仍可访问，相关账号未被封禁。Telegram 否认指控并计划在法庭上抗辩，称自 2026 年以来已移除数千个极端主义群组。

telegram · zaihuapd · 7月30日 03:45

**背景**: 澳大利亚 eSafety 专员办公室是政府机构，负责在线安全监管，有权根据《在线安全法》强制删除内容。Telegram 是一款流行的加密通讯应用，因其宽松的审核政策而在全球面临托管极端主义内容的审查。

**标签**: `#content moderation`, `#Telegram`, `#regulation`, `#terrorism`, `#Australia`

---

<a id="item-8"></a>
## [美委员会代表团访华遭华为、DeepSeek 等拒见](https://tech.ifeng.com/c/8v7fL2j6ajG) ⭐️ 6.0/10

2026 年 7 月下旬，美国美中经济与安全审查委员会（USCC）代表团访问北京、杭州和上海，寻求与华为、DeepSeek 等中国头部科技企业会面，但遭到相关企业集体拒绝。 这是 USCC 自 2019 年以来首次正式访华，凸显两国在科技与安全领域的信任恶化。中企的拒绝表明，它们不愿与一个历史上主张对华限制贸易政策的机构进行接触。 USCC 代表团访问了三座中国城市，但未能获得华为、腾讯、阿里巴巴、百度及 DeepSeek 等公司的会面。该委员会承认，拒绝本身就是一个数据点。

telegram · zaihuapd · 7月30日 03:40

**背景**: 美中经济与安全审查委员会（USCC）是美国国会于 2000 年设立的两党委员会，负责监督美中贸易关系的国家安全影响。该委员会长期推动对华芯片出口管制、扩大实体清单以及 AI 技术限制。DeepSeek 是一家中国 AI 初创公司，以开发成本效益高的大语言模型而闻名，其性能可与 GPT-4 等西方竞品抗衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.voachinese.com/a/uscc-delegation-completes-china-visit-says-honest-disagreement-aired-20260727/8178607.html">美 中 经 济 安 全 审 查 委 员 会 代表团结束访 中 ，主席薛瑞福：坦诚表达分歧</a></li>
<li><a href="https://sputniknews.cn/20260728/1072512811.html">美 国 会 下属机构访华想参观 中 国科技企业被拒 - 2026年7月28...</a></li>

</ul>
</details>

**标签**: `#地缘政治`, `#华为`, `#DeepSeek`, `#科技竞争`

---

<a id="item-9"></a>
## [滴滴通报上半年反舞弊：50 余人被清退，40 余人移送公安](https://finance.sina.com.cn/tech/2026-07-30/doc-inikqiyi1231947.shtml) ⭐️ 6.0/10

滴滴发布 2026 上半年反舞弊通报，披露 50 余人因触犯公司“高压线”政策被解除或清退，40 余人因涉嫌违法犯罪被移送公安机关。 这一通报凸显了滴滴对公司治理和舞弊零容忍的承诺，可能增强利益相关者的信任，并为中国科技行业的反腐败实践树立标杆。 舞弊案件包括收受好处费、弄虚作假、侵占资产和泄露机密等。滴滴还对 40 余家合作方追究违约责任，并鼓励举报，最高奖励 100 万元。

telegram · zaihuapd · 7月30日 07:18

**背景**: 滴滴的“高压线”政策是一项内部反舞弊制度，严格禁止贿赂、侵占等不当行为，与腾讯等中国科技公司的类似政策一致。这类政策在大型企业中常见，用于遏制腐败并确保合规。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.ithome.com/html/983463.htm">滴 滴 发布 2026 上半年反舞弊情况通报，40...</a></li>
<li><a href="https://baike.baidu.com/item/%E8%85%BE%E8%AE%AF%E9%AB%98%E5%8E%8B%E7%BA%BF/64031407">腾讯高压线_百度百科</a></li>

</ul>
</details>

**标签**: `#corporate governance`, `#anti-fraud`, `#ride-hailing`, `#China tech`

---