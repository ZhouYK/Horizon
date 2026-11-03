---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03 23:05:11 +0000
lang: zh
report: default
---

> 从 278 条内容中筛选出 6 条重要资讯。

---

1. [传闻称 DeepSeek V5 计划采用华为昇腾芯片训练](#item-1) ⭐️ 7.0/10
2. [《纽约时报》起诉 Brave：抓取内容转售 AI 公司](#item-2) ⭐️ 7.0/10
3. [传英伟达要求全球数据中心将中国企业业务占比限制在 49% 以内](#item-3) ⭐️ 7.0/10
4. [上海首例盗用 AI 算力案宣判，男子获刑三年缓刑三年](#item-4) ⭐️ 6.0/10
5. [普京签署总统令：俄罗斯私营数据中心须预留 10% 算力供政府调用](#item-5) ⭐️ 6.0/10
6. [苹果推送 iOS 27.3 测试版：健康 App 重做、手表 AI 听录、国行 Apple 智能](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [传闻称 DeepSeek V5 计划采用华为昇腾芯片训练](https://www.eet-china.com/mp/a536460.html) ⭐️ 7.0/10

据产业链人士向国内媒体透露，DeepSeek 下一代大模型 V5 计划基于华为昇腾芯片进行训练，而此前昇腾芯片主要用于 DeepSeek 模型的推理任务。这一传闻出现在 DeepSeek 于 9 月底开源面向昇腾算力平台的基础设施组件之后，这些组件包括编译工具、计算库和分布式通信库，与此前面向英伟达平台开源的组件一一对应。 如果消息属实，这将意味着中国前沿模型训练从英伟达转向国产芯片，对目前主要在推理场景得到验证的华为昇腾软硬件生态而言是一个里程碑。这也会对整个 AI 硬件格局产生影响，因为美国的出口管制使中国实验室获取英伟达高端加速器变得困难。 该说法尚未得到证实，来源是匿名的产业链人士，而非 DeepSeek 或华为官方，且未披露模型规模、所用芯片型号、集群规模或时间表等细节。此前开源的昇腾组件——编译工具、计算库与分布式通信库——被视为其加速转向昇腾的具体证据，因为迁移训练负载恰恰需要这类软件栈支撑。

telegram · zaihuapd · 11月3日 06:20

**背景**: 华为昇腾是华为自研的 AI 处理器系列及配套的软硬件计算平台，主要用于中国数据中心内的 AI 模型训练与推理。DeepSeek 是一家中国 AI 实验室，其模型以开放权重方式发布，产品线从 671B 参数、采用混合专家（MoE）架构的 DeepSeek-V3，延伸到后来的 V4 系列，例如采用因果编码器-解码器（CED）架构的 V4.1-Flash。训练前沿模型通常需要大规模加速器集群以及成熟的软件栈（编译器、计算库和集合通信库），这正是 DeepSeek 此前发布与昇腾对应的组件被外界解读为训练准备、而非单纯推理适配的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jademond.com/glossary/ascend-ai">Huawei Ascend AI Chips: Specs, History, and 2026 Roadmap ...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V3-Base">deepseek -ai/ DeepSeek - V 3-Base · Hugging Face</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek - V 4.1-Flash: smarter, faster, more efficient.</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Huawei Ascend`, `#AI training`, `#China AI`, `#hardware`

---

<a id="item-2"></a>
## [《纽约时报》起诉 Brave：抓取内容转售 AI 公司](https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/) ⭐️ 7.0/10

《纽约时报》周一起诉主打隐私保护的浏览器厂商 Brave Software，指其使用未披露的爬虫建立起超过 300 亿网页的索引，过程中绕过付费墙并屏蔽出版商的广告，随后又将该索引的访问权出售给 Anthropic、Perplexity、Mistral、xAI、Cohere 等 AI 公司。同一天，《纽约每日新闻》《芝加哥论坛报》等媒体也在同一法院提起类似诉讼，Brave 尚未作出回应。 这是首批将矛头指向浏览器厂商、而非纯粹 AI 开发者的重要诉讼之一，其核心主张是“抓取—转售”这一数据管道本身即构成侵权，可能为 AI 训练数据供应链的授权规则确立判例。运行爬虫、RAG 流水线或数据经纪业务的公司将面临更明确的法律风险，而出版商则获得了一个绕过模型厂商、直接追责中间商的诉讼模板。 诉状提出三条独立的侵权主张——通过未披露的爬虫进行未经授权的抓取、绕过付费墙，以及屏蔽广告使出版商流失收入——并同时寻求禁令与金钱赔偿。Brave 一直宣传其搜索产品运行在自有独立索引之上，而非依赖 Google 或 Bing 的索引，而这一资产恰恰被出版商指为建立在其内容之上。

telegram · zaihuapd · 11月3日 06:50

**背景**: Brave 是一款 2016 年发布的免费开源 Chromium 内核浏览器，以隐私保护为卖点：默认拦截广告与追踪器，并通过 Basic Attention Token 奖励那些选择观看其自有广告的用户。为降低对科技巨头的依赖，Brave 围绕自建的独立网页索引打造了 Brave Search，而非向 Google 或 Bing 授权搜索结果。自建索引需要持续抓取全网内容，而大量新闻网站的内容处于付费墙之后或依赖广告变现，这种组合使基于爬虫的索引建设与出版商的版权及合同权利正面冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brave_browser">Brave browser</a></li>
<li><a href="https://brave.com/search/">What is Brave Search? | Brave</a></li>
<li><a href="https://www.stackmatix.com/blog/brave-search-seo">Brave Search SEO: How to Rank on Brave&#x27;s Independent Index</a></li>

</ul>
</details>

**标签**: `#AI copyright`, `#web scraping`, `#Brave browser`, `#publisher lawsuits`, `#AI training data`

---

<a id="item-3"></a>
## [传英伟达要求全球数据中心将中国企业业务占比限制在 49% 以内](https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits) ⭐️ 7.0/10

据《金融时报》报道，英伟达已要求全球数据中心运营商把来自中国企业的业务占比控制在 49% 以内，以确保至少 51% 的业务来自非中国企业。据称该要求适用于全球范围，但仅针对新签及未来合同，已签订的租赁协议不受影响。 这属于罕见的情况：一家芯片厂商实质上充当了美国出口政策的执行层，把合规义务转嫁给全球各地的云服务商和数据中心运营商。如果这种做法扩散，中国 AI 企业租用海外算力的渠道将受到更严格约束，而这正是规避芯片出口限制的主要变通方式之一。 据报道，该规定由英伟达销售团队和区域团队口头传达，并无正式文件，因此其确切范围和可执行性都不明确。英伟达的公开回应并未确认 49% 这一门槛，而是强调美国芯片是美国模型与应用厂商参与全球竞争的基础，并指出现行美国政策鼓励云服务商基于美国基础设施承接各地业务。

telegram · zaihuapd · 11月3日 16:19

**背景**: 美国的出口管制禁止英伟达向中国客户出售其最先进的 AI 加速卡，该公司为此推出了性能受限的中国特供版本以符合规定。由于管制针对的是硬件销售而非硬件的使用地点，中国企业此前可以通过境外数据中心租用 GPU 算力。49/51 的客户结构门槛实际上会把限制从销售环节延伸到使用环节；在英伟达或相关运营商正式确认之前，应将其视为尚未证实的报道。

**标签**: `#Nvidia`, `#data centers`, `#US-China tech`, `#export controls`, `#AI infrastructure`

---

<a id="item-4"></a>
## [上海首例盗用 AI 算力案宣判，男子获刑三年缓刑三年](https://www.thepaper.cn/newsDetail_forward_34389477) ⭐️ 6.0/10

上海市徐汇区人民法院对全市首例利用 AI 伪造签名、盗用大模型算力案作出一审判决，以非法获取计算机信息系统数据罪判处宗某某有期徒刑三年、缓刑三年，并处罚金 4 万元。宗某某绕过平台防护机制，使用 400 多万个账号批量领取新用户积分，非法调用接口 29 万余次，并通过转卖生成服务获利 3.4 万余元。 这是上海法院首次将针对 AI 平台的“算力套利”行为入刑，确立了模型推理能力属于受法律保护的计算机信息系统资源、而非可随意攫取的公共资源的判例。这提醒 AI 服务商及其安全团队：薅积分、转卖 API 等行为如今可能被追究刑事责任，也为企业在封号之外选择报案提供了可参照的法律依据。 该案定罪依据是“非法获取计算机信息系统数据罪”而非盗窃罪，且涉案金额与规模严重失衡：400 多万个账号、29 万余次调用仅换来约 3.4 万元的转卖收入；检方强调，此类“算力套利”不承担任何算力成本，成本实际由按次向上游模型厂商付费的平台承担。三年刑期全部缓刑，并处罚金 4 万元，意味着只要宗某某在缓刑考验期内不违规便无需实际入狱。

telegram · zaihuapd · 11月3日 08:43

**背景**: 大模型聚合平台通常会向新用户赠送可用于生成图片或视频的免费积分，而平台自身需按调用次数向上游模型厂商支付算力费用。“算力套利”正是利用这一价差形成的灰产：账号农场批量注册以收割新人福利，逆向工程或伪造签名绕过客户端校验，再把获得的调用权限通过 API 中间层或“拼车”订阅低价转卖。由于这类操作不承担任何真实算力成本，损失由平台吸收，利润则归转卖者所有。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/linux_do_channel/554341">LINUX DO Channel – Telegram</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2023063229929112866">邵诗巍律师 | AI Agent算力套利模式及其法律风险分析</a></li>
<li><a href="https://blog.csdn.net/weixin_28678151/article/details/169206868">AI Agent商业化中的算力套利与灰色产业链解析-CSDN博客</a></li>

</ul>
</details>

**标签**: `#AI算力`, `#网络安全`, `#法律判例`, `#平台滥用`, `#黑产`

---

<a id="item-5"></a>
## [普京签署总统令：俄罗斯私营数据中心须预留 10% 算力供政府调用](https://www.reuters.com/technology/putin-orders-private-data-centres-set-aside-10-capacity-support-it-2026-11-02/) ⭐️ 6.0/10

俄罗斯总统普京签署总统令，要求俄罗斯境内所有非国有数据中心预留 10% 的场地和计算能力供政府调用。俄数字发展部须对全国私营数据中心的可用场地与算力进行清查，运营商在接到通知后必须在 24 小时内提供使用权限。 该总统令实质上把俄罗斯私营云与数据中心资源变成了国家战略储备，使政府能够提前一天通知即征用基础设施。这直接影响运营商、其企业客户及外国合作方对容量规划、服务保障以及俄境内商业合同可执行性的判断。 政府将成立专门委员会，有权要求数据中心释放预留资源；此外，经俄罗斯联邦安全局（FSB）批准，政府还可临时调用位于境外的数据中心资源。据报道内容，总统令未明确补偿条款，且该要求针对的是 10% 的预留额度，而非全面接管数据中心设施。

telegram · zaihuapd · 11月3日 10:58

**背景**: 俄罗斯多年来持续推进“数字主权”，试图降低对外国平台的依赖，并在制裁与跨境网络中断的情况下维持关键 IT 服务运转。数据中心是这一努力的物理底座，承载着政府门户、银行、电信和云服务商。国家对私营算力提出预留要求，与其他司法辖区在紧急状态下要求服务商优先保障关键服务的做法有相似之处。

**标签**: `#data centers`, `#tech policy`, `#cloud infrastructure`, `#digital sovereignty`, `#regulation`

---

<a id="item-6"></a>
## [苹果推送 iOS 27.3 测试版：健康 App 重做、手表 AI 听录、国行 Apple 智能](https://www.macrumors.com/2026/11/03/ios-27-3-health-app/) ⭐️ 6.0/10

苹果向开发者推送了 iOS 27.3 与 watchOS 27.3 测试版，正式版计划于 12 月上线。此次更新重做了健康 App，新增 Insights 与 Longevity 标签页以及「健康年龄」指标，并为 Apple Watch Series 12 和 Ultra 4 带来常开的 AI 监听功能 Siri Recap 与 Live Rewind，同时国行设备上的 Apple 智能也已开始与阿里千问合作测试。 国行版本的测试意味着苹果在漫长的监管等待后，首次将 Apple 智能推向全球最大的智能手机市场，而选择与本土厂商合作而非使用自研模型，也说明 AI 功能的落地将越来越多地受地区合规要求左右。常开监听功能则让 Apple Watch 进一步迈向「环境 AI」，这一转变势必会引发关于隐私与续航取舍的讨论。 初期 Live Rewind 只能回看前 15 秒的转写文字，且两项监听功能均仅支持英文，中文用户暂时无法使用。国行版本显示为「Apple 智能与 Siri」，仅提供通知摘要、Genmoji 等部分功能，而健康 App 的语言支持则扩展至包括中文在内的 11 种语言。

telegram · zaihuapd · 11月3日 18:50

**背景**: Apple Intelligence 是苹果对生成式 AI 功能的统称，部分在设备端运行，部分依托其「私有云计算」服务器，涵盖根据文字描述生成自定义表情的 Genmoji、AI 通知摘要等能力。中国监管要求境外 AI 服务必须与获批的本土厂商合作，这正是苹果选择阿里千问的原因——千问是阿里云自研的大模型家族，覆盖文本、代码、图像、音频与超长文档处理。全新的「健康年龄」指标会把 Apple Watch 记录的心率、睡眠、活动量与最大摄氧量等数据整合成一个估算值，再与用户的实际年龄对比，而不是把各项数字分散呈现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.aliyun.com/article/1759898">通义 千 问 Qwen ...</a></li>
<li><a href="https://emojipedia.org/zh/genmoji">Genmoji - Apple &#x27;s AI Emoji Generator for iOS 18.2, Now Available...</a></li>
<li><a href="https://www.sohu.com/a/1074313239_122480024">Apple Watch 新功能HealthAge：你的健康年龄可能比实际年龄更老</a></li>

</ul>
</details>

**标签**: `#Apple`, `#iOS`, `#Apple Intelligence`, `#Wearables`, `#Consumer Tech`

---