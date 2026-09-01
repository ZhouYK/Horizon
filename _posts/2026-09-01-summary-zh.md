---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01 23:07:39 +0000
lang: zh
report: default
---

> 从 301 条内容中筛选出 8 条重要资讯。

---

1. [Virtualizor 更新通道遭 BGP 劫持，恶意更新植入 root 后门](#item-1) ⭐️ 8.0/10
2. [Claude Fable 5.1 正式发布，1M 上下文窗口与缓存读取降价](#item-2) ⭐️ 8.0/10
3. [高通自 9 月 1 日起芯片涨价两位数](#item-3) ⭐️ 7.0/10
4. [纸杯遇热释放微塑料：PLA 内衬释出量比 PE 高 12 倍](#item-4) ⭐️ 6.0/10
5. [VLC 累计下载突破 70 亿，并移植至亚马逊 Vega OS](#item-5) ⭐️ 6.0/10
6. [努比亚“豆包手机 2”获入网许可，9 月上市](#item-6) ⭐️ 6.0/10
7. [日本放宽加班规定 45 小时上限不再强制](#item-7) ⭐️ 6.0/10
8. [瑞银：中国 EUV 落后 ASML 约十年，浸润式 DUV 或 2 至 5 年量产](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Virtualizor 更新通道遭 BGP 劫持，恶意更新植入 root 后门](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 8.0/10

2026 年 8 月 28 日至 30 日期间，攻击者劫持了 Virtualizor 更新基础设施的 BGP 路由，并通过有效 TLS 证书投递了恶意更新包。Virtualizor 官方确认，只有在该时间窗口内更新的少量安装受影响。 这一事件表明，BGP 劫持可以将软件更新分发变成供应链攻击载体，即使软件本身没有漏洞也难以幸免。hypervisor 控制面板是高价值目标，因为宿主机上的 root 后门会危及所有托管的虚拟机和网站。 独立取证显示，恶意包会写入 root SSH 密钥、安装 Java 载荷并创建持久化服务。AlbaHost 在 34 台 hypervisor 中发现 5 台存在入侵指标，Softaculous 表示目前没有证据表明其他产品受影响。

telegram · zaihuapd · 9月1日 06:05

**背景**: BGP（边界网关协议）是互联网上在不同自治系统之间传递流量的路由协议；BGP 劫持是指攻击者通告自己并不合法拥有的 IP 前缀，从而将发往这些前缀的流量引导至攻击者控制的基础设施。Virtualizor 是 Softaculous 开发的一款基于 Web 的 VPS 控制面板，托管服务商用它来管理 hypervisor 和虚拟机。由于更新通过互联网获取，一旦路由被劫持，攻击者只要再获得或滥用 TLS 证书，就可能向用户投递恶意内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/virtualizor-compromise/">BGP Hijack Diverts Softaculous Traffic to Deliver Malicious Virtualizor ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/BGP_hijacking">BGP hijacking</a></li>
<li><a href="https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/">What Is BGP Hijacking ?</a></li>

</ul>
</details>

**标签**: `#security`, `#BGP hijacking`, `#supply chain attack`, `#Virtualizor`, `#rootkit`

---

<a id="item-2"></a>
## [Claude Fable 5.1 正式发布，1M 上下文窗口与缓存读取降价](https://platform.claude.com/docs/en/models/fable-5-1/overview) ⭐️ 8.0/10

2026 年 9 月 1 日，Anthropic 正式发布 Claude Fable 5.1，该模型支持 1M tokens 上下文窗口和 128K tokens 最大输出，输入与输出定价仍分别为每百万 tokens 10 美元和 50 美元，与上代持平。缓存读取价格降至原来的四分之一，而 Claude Mythos 5.1 仍仅限 Project Glasswing 参与者邀请使用。 此次发布之所以重要，是因为它在不涨价的前提下大幅扩展了长时程智能体和复杂推理任务可用的上下文长度，同时将缓存读取成本降低了 75%。这加剧了前沿模型提供商在上下文窗口规模和推理成本方面的竞争压力，直接惠及运行高频 token 负载的开发者与企业。 缓存读取降价适用于被复用的前缀 token，但写入附加费与最小可缓存前缀要求仍然适用。Mythos 5.1 仅限 Project Glasswing 使用——这是 Anthropic 的网络安全项目，早期模型曾被称为 Claude Mythos Preview 或 Mythos2 Preview。

telegram · zaihuapd · 9月1日 17:54

**背景**: Claude Fable 是 Anthropic 的前沿模型系列；Fable 5.1 面向跨数十至数千步骤、持续数分钟到数天的长时程智能体负载。通过提示词缓存（prompt caching），提供商可以对被复用前缀中的 token 收取低得多的费用，Anthropic 的缓存读取通常比普通输入 token 便宜约 90%。Project Glasswing 是 Anthropic 的一项计划，旨在用专注于网络安全的前沿模型保护 AI 时代的关键软件，Mythos 5.1 延续了这一仅限特定访问的系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youngju.dev/blog/2026-07-08-llm-caching-explained.en">LLM Caching , Explained — Why Prompt Caching and Prefix Caches ...</a></li>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Claude`, `#AI model`, `#context window`, `#pricing`, `#release`

---

<a id="item-3"></a>
## [高通自 9 月 1 日起芯片涨价两位数](https://www.macrumors.com/2026/08/31/qualcomm-chip-price-increase/) ⭐️ 7.0/10

高通宣布，对 2026 年 9 月 1 日后出货的全系列芯片涨价，涨幅达两位数。CEO 克里斯蒂亚诺·安蒙表示，公司无法继续自行承担不断上升的供应商成本。 作为全球最大的移动芯片供应商之一，高通涨价将直接影响苹果及众多设备厂商，很可能推高智能手机和联网设备的成本。此举也反映出整个半导体供应链面临的通胀压力。 具体涨幅将与客户逐一协商，因此实际调价幅度可能因客户而异。尽管涨价，苹果仍继续为 iPhone 17 系列采购高通调制解调器芯片。

telegram · zaihuapd · 9月1日 04:10

**背景**: 高通为智能手机提供连接蜂窝网络的调制解调器芯片，长期是苹果 iPhone 的关键供应商。近年来，制造成本上升和供应链中断迫使许多半导体企业提价。高通与客户之间的协商，反映了移动硬件行业复杂的利益平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.sina.cn/csj/2018-11-05/doc-ihmutuea7064783.d.html?oid=5_iqq&amp;vt=4">高通与苹果决裂背后， 基 带 芯 片 到底是啥？_ 手机新浪网</a></li>
<li><a href="https://www.21ic.com/a/974018.html">最强梳理！ 基 带 与射频到底干什么用的？ - 21ic电子网</a></li>

</ul>
</details>

**标签**: `#Qualcomm`, `#chip pricing`, `#hardware`, `#supply chain`, `#Apple`

---

<a id="item-4"></a>
## [纸杯遇热释放微塑料：PLA 内衬释出量比 PE 高 12 倍](https://news.uq.edu.au/2026-08-takeaway-cups-release-microplastics-your-coffee) ⭐️ 6.0/10

昆士兰大学的一项研究发现，一次性纸杯在盛装热饮时会释放出数百万个微塑料颗粒。内衬为聚乳酸（PLA）的纸杯释放的颗粒总质量约为内衬为聚乙烯（PE）纸杯的 12 倍，每毫升约 430 万个纳米颗粒，而 PE 纸杯约为 270 万个。 这一发现意义重大，因为纸杯无处不在，而且它挑战了人们对“可降解”PLA 产品的既有认知。同时，由于摄入塑料颗粒对健康的影响尚不明确，这也凸显了制定监管指南的必要性。 该研究比较了 PE 内衬与 PLA 内衬纸杯，发现 PLA 内衬释放的颗粒总质量约为 PE 内衬的 12 倍。尽管释放量更高，但研究人员强调这并不意味着应停用纸杯，而是呼吁出台安全指南或产品标签警示。

telegram · zaihuapd · 9月1日 00:45

**背景**: 微塑料是指尺寸在 1 微米到 5 毫米之间的塑料颗粒，而纳米塑料更小，小于 1 微米。一次性纸杯通常有一层薄薄的塑料内衬——常见的是聚乙烯（PE）或聚乳酸（PLA）——用于防水。PLA 是一种以玉米、木薯等可再生植物为原料制成的生物基塑料，被宣传为可降解。当热饮倒入这类纸杯时，内衬会脱落微小的塑料碎片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cn-plas.com/txtsjyl/4527.html">Nature_Works_Ingeo_ PLA 聚 乳 酸 生物降解 材 料 -科思德塑胶</a></li>
<li><a href="http://www.baolin1998.com/news/hangyedongtai/88.html">PE ...</a></li>
<li><a href="https://www.kepuchina.cn/article/articleinfo?business_type=100&amp;classify=0&amp;ar_id=488844">kepuchina.cn/article/articleinfo?business_type=100&amp;classify=0&amp;ar_id...</a></li>

</ul>
</details>

**标签**: `#microplastics`, `#environment`, `#PLA`, `#food safety`, `#research`

---

<a id="item-5"></a>
## [VLC 累计下载突破 70 亿，并移植至亚马逊 Vega OS](https://techcrunch.com/2026/08/31/vlc-crosses-7-billion-downloads/) ⭐️ 6.0/10

非营利组织 VideoLAN 开发的开源媒体播放器 VLC 累计下载量已突破 70 亿次，覆盖所有平台，并正在移植到亚马逊 Fire TV 设备的 Vega OS 系统上。 这一里程碑表明 VLC 仍是使用最广泛的开源项目之一，用户群持续扩大。移植到 Vega OS 使 VLC 进入亚马逊下一代流媒体设备，进一步拓展其在电视和机顶盒媒体播放领域的角色。 这一 70 亿次下载里程碑距离 2025 年 1 月达到 60 亿次约 18 个月。公告还显示，VLC 4 仍在开发中，而 Vega OS 移植是持续平台扩展计划的一部分。

telegram · zaihuapd · 9月1日 03:43

**背景**: VLC 是由 VideoLAN 项目开发的免费开源跨平台媒体播放器，以支持多种音视频格式和流媒体协议而闻名。亚马逊的 Vega OS 是面向 Fire TV 设备的新款基于 Linux 的操作系统，采用 React Native 和 Web 技术构建，在新硬件上取代了基于 Android 的旧版 Fire OS。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLC_media_player">VLC media player</a></li>
<li><a href="https://www.oxagile.com/article/vega-os-overview/">What is Amazon Vega OS ( Operating System )? Vega OS Release...</a></li>
<li><a href="https://www.stork.ai/blog/amazons-secret-os-is-replacing-android">Amazon &#x27;s Vega OS : The Post-Android Future for Fire TV... | Stork.AI</a></li>

</ul>
</details>

**标签**: `#VLC`, `#VideoLAN`, `#open-source`, `#media-player`, `#milestone`

---

<a id="item-6"></a>
## [努比亚“豆包手机 2”获入网许可，9 月上市](https://mp.weixin.qq.com/s/u7KXxdvmh8hjf8cVbQZOKg) ⭐️ 6.0/10

努比亚 AI 智能体手机 NaviX Ultra（豆包手机二代）已获得入网许可，将于 9 月上市。该机由努比亚与字节跳动联合打造，其“努比亚豆包手机大模型”已于 7 月 8 日完成生成式 AI 服务备案。 这标志着首批完成端侧生成式 AI 备案的手机终端之一，显示 AI 智能体手机正成为手机厂商与 AI 公司竞争的新焦点。努比亚与字节跳动的合作可能加速大模型在消费终端落地，并改变用户的手机交互方式。 该机提供蓝境、幻梦、黑色、白色四款配色。其端侧大模型于 7 月 8 日完成生成式 AI 服务备案，成为首批完成手机端侧大模型备案的终端产品之一。

telegram · zaihuapd · 9月1日 11:18

**背景**: 在中国，生成式 AI 服务须先向网信部门备案才能对公众提供服务。端侧大模型直接在手机硬件上运行推理，可提升隐私保护并减少对云端的依赖。字节跳动的豆包是面向消费者的 AI 助手及模型生态系统，这款手机将豆包助手集成进专用硬件，与此前的 ZTE×豆包 AI 手机类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anythingllm.com/">AnythingLLM — On - device AI for productivity | Local &amp; Private</a></li>
<li><a href="https://global.chinadaily.com.cn/a/202608/26/WS6a8e5d64e4b06d4aa055a8a4.html">China &#x27;s water sector secures first generative AI ... - Chinadaily.com.cn</a></li>
<li><a href="https://imastudio.com/blog/what-is-doubao">What Is Doubao AI ? International Version Name, Dola, Seedream...</a></li>

</ul>
</details>

**标签**: `#AI`, `#smartphone`, `#Nubia`, `#Doubao`, `#edge AI`

---

<a id="item-7"></a>
## [日本放宽加班规定 45 小时上限不再强制](https://www.orientaldaily.com.my/news/international/2026/09/01/844683) ⭐️ 6.0/10

日本自 9 月 1 日起放宽加班规定，劳动标准监察机构不再强制企业遵守每月 45 小时的加班上限。此举是政府为刺激经济而推行的增长战略的一部分。 这项政策变动可能加剧日本的过劳文化，影响包括科技业在内的各行各业劳动者。批评者担心这会增加过劳死风险，而政府则称其有助于刺激经济增长。 新规源于首相高市早苗政府 7 月通过的增长战略。目前约 40%的日本企业允许每月最多加班 100 小时，尽管官员提醒超过 45 小时会增加过劳死风险。

telegram · zaihuapd · 9月1日 12:56

**背景**: 日本一直有法定加班上限，目的是防止过劳死（karoshi）。此前每月 45 小时的上限是劳动标准监察机构执行的规定。新政策放宽了执行，体现了经济增长优先与劳动者保护之间的张力。日本的工作文化以长时间劳动著称，政府一直试图在竞争力和劳动者福祉之间取得平衡。

**标签**: `#Japan`, `#labor policy`, `#overtime`, `#work culture`, `#policy change`

---

<a id="item-8"></a>
## [瑞银：中国 EUV 落后 ASML 约十年，浸润式 DUV 或 2 至 5 年量产](https://thenextweb.com/news/ubs-china-asml-euv-decade-immersion-duv-dutch-export-licence) ⭐️ 6.0/10

瑞银分析师估计，中国光刻项目大致相当于 ASML 2004 年的水平，十年内难以造出可行的 EUV 替代品。他们预计中国能在 2 到 5 年内实现浸润式 DUV 光刻机的大规模量产，尽管这类设备受荷兰出口许可管制。 该预测凸显了半导体光刻领域持续存在的技术差距，这是中国芯片制造雄心的关键瓶颈。它也表明针对浸润式 DUV 和 EUV 等先进设备的出口管制颇为有效，正在重塑全球芯片供应链。 ASML 的浸润式 DUV 设备单台售价接近 9000 万美元，EUV 系统则超过 2 亿美元。2025 年第三季度，中国占 ASML 净销售额的 42%，凸显了其市场对中国需求的依赖。

telegram · zaihuapd · 9月1日 13:58

**背景**: 光刻技术利用光线在硅晶圆上刻画微芯片图案，光波长决定了可达到的最小特征尺寸。DUV 光刻使用深紫外光（如 193nm 氟化氩激光）制造较不先进的制程节点，而 EUV 使用 13.5nm 光线打印最小特征。ASML 目前是唯一能生产并销售 EUV 系统用于芯片制造的公司，其浸润式 DUV 设备也受到针对中国的荷兰出口管制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EUV_lithography">EUV lithography</a></li>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products | ASML</a></li>
<li><a href="https://www.asml.com/en/products/duv-lithography-systems">DUV lithography systems | Products</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#lithography`, `#ASML`, `#China`, `#EUV`

---