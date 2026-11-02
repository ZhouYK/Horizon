---
layout: default
title: "Horizon Summary: 2026-11-02 (ZH)"
date: 2026-11-02 23:04:11 +0000
lang: zh
report: default
---

> 从 189 条内容中筛选出 5 条重要资讯。

---

1. [ChatGPT 分享链接漏洞可劫持已登录会话](#item-1) ⭐️ 8.0/10
2. [Anthropic 前三季度营收 332 亿美元，净亏损 1040 亿美元](#item-2) ⭐️ 8.0/10
3. [WIRED 调查：400 多个 AI 应用暗藏色情深伪生成功能](#item-3) ⭐️ 7.0/10
4. [阿布扎比与 OpenAI 签署四项协议，推进「机器可读政府」](#item-4) ⭐️ 7.0/10
5. [瑞典连锁超市 ICA 遭网络攻击，冷柜被远程调至 50°C](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [ChatGPT 分享链接漏洞可劫持已登录会话](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 8.0/10

安全公司 Parameter 披露了一个 ChatGPT 分享链接漏洞：攻击者构造的恶意链接可在任何已登录用户打开后，于其会话中执行攻击者代码，读取私密对话并将其外传至外部服务器。OpenAI 已于 10 月 26 日修复该漏洞，将其定级为 P1，并向研究团队支付了 5000 美元赏金。 ChatGPT 拥有数以亿计的用户，其中许多人习惯点击他人发来的分享链接，因此这种“一键点击、无需安装”即可接管账号的漏洞，对任何曾在对话中粘贴过敏感资料的人都构成严重威胁。该案例还说明，AI 智能体的预览与渲染功能正在成为同类平台上一片新的、范围很广的攻击面。 该漏洞源于分享链接的预览功能与图表组件之间的消息处理缺陷，因此受害者只需打开链接即可，无需安装应用或进行其他交互。OpenAI 将其定为 P1（最高优先级）问题；相对其影响而言，5000 美元的赏金并不算高，而此次披露本身对利用细节的描述也较为简略。

telegram · zaihuapd · 11月2日 10:24

**背景**: ChatGPT 的分享功能会为一段对话生成公开链接，任何人都可以打开这些链接，包括同时登录着自己 ChatGPT 账号的用户。现代 Web 应用通常会在内嵌框架中渲染这类共享内容，并通过 postMessage 之类的跨框架消息机制在组件之间通信；如果接收方没有严格校验消息来源和载荷，攻击者提供的内容就可能被当作可信指令执行。所谓“账号接管”，是指攻击者获得了在受害者已认证会话中操作的能力，从而不仅能看到被分享的那段对话，还可能读取整个对话历史。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html">A Shared ChatGPT Link Could Run Attacker Code in Your Session ...</a></li>
<li><a href="https://labs.cloudsecurityalliance.org/research/csa-research-note-chatgpt-share-link-session-hijack-20261031/">One Click Into Someone Else’s ChatGPT: Cross-Frame Messaging ...</a></li>
<li><a href="https://aicybr.com/blog/chatgpt-shared-link-session-takeover-parameter-labs-october-2026">ChatGPT Shared-Link Session Takeover: October 2026 Fix ...</a></li>

</ul>
</details>

**标签**: `#security`, `#ChatGPT`, `#vulnerability`, `#account-takeover`, `#AI`

---

<a id="item-2"></a>
## [Anthropic 前三季度营收 332 亿美元，净亏损 1040 亿美元](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) ⭐️ 8.0/10

Anthropic 周一更新 IPO 招股书，披露 2026 年前三季度营收达到 332.4 亿美元，同比增长约 1200%，其中第三季度营收约 170 亿美元。同期公司净亏损达到 1040 亿美元，远高于去年同期的 251 亿美元。 这份招股书罕见地详细展示了一家领先前沿 AI 实验室的财务状况，既体现出营收爆发式增长，也暴露出巨额成本。约 8954 亿美元的累计算力和基础设施承诺，凸显前沿 AI 的资本密集程度，并可能影响投资者在潜在 IPO 前对 AI 公司的估值方式。 Anthropic 表示，上半年净亏损主要受可转换债券及衍生负债公允价值变动影响，因此并不完全代表实际经营现金消耗。公司还披露累计采购及租赁承诺约 8954 亿美元，几乎全部用于算力和基础设施。

telegram · zaihuapd · 11月2日 15:12

**背景**: Anthropic 是一家开发 Claude 系列大语言模型的 AI 实验室，目前正通过 IPO 招股书筹备上市；在美国市场，这类文件通常被称为 S-1。公司会在其中披露营收、亏损和合同义务，供投资者评估业务。可转换债券和衍生负债的公允价值变动可能带来大额账面收益或亏损，即使没有实际现金流动。算力承诺则是未来需要支付的合同义务，通常用于购买云服务、芯片和数据中心容量，以训练和运行 AI 模型。

**标签**: `#Anthropic`, `#AI industry`, `#IPO`, `#financials`, `#compute infrastructure`

---

<a id="item-3"></a>
## [WIRED 调查：400 多个 AI 应用暗藏色情深伪生成功能](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 7.0/10

WIRED 于 11 月 2 日发布的调查揭示了一个由 400 多个相互关联的应用与网站组成的网络：它们以宠物画像、语言学习等普通 AI 工具为伪装，却在特定条件下静默加载色情深伪界面，允许用户上传他人照片生成露骨图像或视频。在被联系后，苹果下架了 19 款应用，谷歌在此前已移除 9 月仍在 Google Play 上架的 27 款应用中的大部分（这些应用累计下载超过 35 万次），Meta 则表示已阻止 209 款相关应用的广告投放。 这一事件说明应用商店审核并不足以挡住未经同意的私密影像：开发者可以先提交无害的安装包，在通过审核后再远程替换为滥用性内容，从而让任何人（包括未成年人，因为不少应用被标注为适合所有年龄）都能通过主流商店和广告网络接触到深伪脱衣工具。这也迫使苹果、谷歌和 Meta 不只审查首次提交，还要监管审核通过后的行为与广告供应链。 研究人员通过共享代码、托管信息、域名和广告追踪数据将这些应用与网站串连起来，并依据中文代码、托管线索和域名，把该网络与中文开发者以及一家在香港注册的公司联系起来；相关运营方未回应置评请求，WIRED 也说明这种关联属于媒体与研究人员的调查判断，而非已被证实的事实。报道侧重该网络的规模与协同运作方式，并未详细披露检测方法。

telegram · zaihuapd · 11月2日 12:45

**背景**: 色情深伪通常由所谓的“脱衣”应用生成，这类工具利用机器学习模型去除照片中的衣物，如今成本低廉、获取门槛很低，常被用来在未经同意的情况下侵害女性。移动应用商店依赖上架前的审核流程，而这种模式长期存在“远程内容替换”的漏洞：开发者先提交一个无害的应用，待审核通过后再更换目标网页或加载的内容。广告追踪标识和共享代码库是调查人员识别同一批运营者所控应用网络的常用手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mjtsai.com/blog/2023/02/15/swapping-app-data-after-review/">Michael Tsai - Blog - Swapping App Data After Review</a></li>
<li><a href="https://en.wikipedia.org/wiki/Deepfake_pornography">Deepfake pornography - Wikipedia</a></li>
<li><a href="https://www-wired-com.nproxy.org/story/deepfake-nudify-technology-is-getting-darker-and-more-dangerous/">Deepfake ‘Nudify’ Technology Is Getting Darker—and More Dangerous</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#deepfakes`, `#content moderation`, `#app store policy`, `#privacy &amp; ethics`

---

<a id="item-4"></a>
## [阿布扎比与 OpenAI 签署四项协议，推进「机器可读政府」](https://thenextweb.com/news/openai-abu-dhabi-deals-machine-readable-government-mubadala) ⭐️ 7.0/10

阿布扎比于周一与 OpenAI 签署了四项协议，其中「机器可读政府」计划将政策法规转化为 AI 可读格式，以便官员核查许可与证书申请。其余协议包括穆巴达拉与 OpenAI、G42 旗下 Inception42 合作开展投资分析，Inception42 另签五年协议向阿联酋政府、企业和学校提供模型，以及 ADNOC 成为首家使用 OpenAI Frontier 平台的能源公司。 这笔交易是国家级政府围绕 AI 可读政策重构行政流程最具体的案例之一，有望成为其他国家推进主权 AI 的样板。同时，在美欧监管机构仍在讨论如何治理公共部门 AI 使用之际，它进一步加深了 OpenAI 与海湾国家及其龙头企业之间的绑定关系。 「机器可读政府」计划已在食品进口场景试点，最终决定权仍掌握在官员手中而非 AI。其余协议涵盖穆巴达拉的投资分析工作、Inception42 覆盖政府、企业和学校的五年模型供应协议，以及 ADNOC 对 Frontier 平台的使用——这是 OpenAI 于 2026 年初推出的企业级产品，用于构建、部署和监控 AI 智能体。

telegram · zaihuapd · 11月2日 15:55

**背景**: 「机器可读政府」指的是把法律、法规和行政程序数字化为结构化的格式，让软件乃至 AI 模型能直接解析，而不必依赖人工阅读 PDF 和手册。OpenAI 于 2026 年初推出的 Frontier 是一个用于构建、部署和监控 AI 智能体的企业平台。Inception42 是阿布扎比 G42 集团旗下应用 AI 部门，以阿拉伯语导向的 Jais 系列模型闻名；穆巴达拉是阿布扎比主要主权财富基金之一，ADNOC 则是该酋长国的国家石油公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/25321">OpenAI Launches Frontier Platform : Building AI Colleagues to...</a></li>
<li><a href="https://inception42.ai/">Inception AI | Pioneering Industry-Specific AI Solutions</a></li>
<li><a href="https://smarterx.ai/smarterxblog/openai-frontier">OpenAI ’s Frontier Platform is Where AI Agents Become Your...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Abu Dhabi`, `#Government AI`, `#AI Governance`, `#Digital Policy`

---

<a id="item-5"></a>
## [瑞典连锁超市 ICA 遭网络攻击，冷柜被远程调至 50°C](https://x.com/InsiderGeo/status/2117164877701595165) ⭐️ 6.0/10

瑞典连锁超市 ICA 表示，多家门店夜间遭到网络攻击，冷藏柜和冷冻柜被远程设定为 50°C，斯约博（Sjöbo）、托梅利拉（Tomelilla）等地的门店受到影响。相关门店当天上午暂停营业，预计在当地时间 9 点左右重新开门，ICA 已就此向顾客致歉。 这起事件是物联网/OT 攻击造成现实世界后果的具体案例：原本普通的门店制冷设备被变成了食品安全与经济损失风险，而不再是单纯的数据泄露。近几周法国和美国也出现了针对企业的类似攻击，说明攻击者正有意把目标对准运营技术系统，而不只是窃取数据。 目前披露的信息没有说明攻击的具体技术路径——究竟是凭据泄露、暴露在公网的远程管理接口被利用，还是楼宇管理系统被攻破——也没有说明受影响门店的确切数量。把制冷设备设为 50°C 会使冷藏和冷冻食品迅速进入温度危险区间，若未在营业前及时发现，可能造成大规模食品变质。

telegram · zaihuapd · 11月2日 13:52

**背景**: 现代超市普遍依赖联网的制冷控制器和楼宇管理系统，以便跨门店远程监控和调节温度。这些便利功能本身也构成了攻击面：一旦账号或底层网络被攻破，入侵者就能像技术人员一样修改温度设定值。OT/ICS 安全与传统 IT 安全的逻辑不同，其首要关注点是可用性和物理安全，而非数据机密性，因此被篡改的温控设备可能立刻造成实实在在的损害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackernoon.com/iot-security-threats-in-retail-how-do-we-eliminate-them-iz7j366m">IoT Security Threats in Retail : How Do We Eliminate... | HackerNoon</a></li>
<li><a href="https://www.linkedin.com/pulse/invisible-fragility-cybersecurity-otics-challenges-digital-meda-6edhf">The Invisible Fragility: Cybersecurity in OT / ICS and the Challenges of...</a></li>
<li><a href="https://nrfprotect.nrf.com/session/2216">Connected, not compromised: Securing Retail IoT | NRF PROTECT</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#IoT security`, `#OT/ICS`, `#retail`, `#cyberattack`

---