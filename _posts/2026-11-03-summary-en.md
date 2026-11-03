---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03 23:05:11 +0000
lang: en
report: default
---

> From 278 items, 6 important content pieces were selected

---

1. [Rumor: DeepSeek V5 May Be Trained on Huawei Ascend Chips](#item-1) ⭐️ 7.0/10
2. [New York Times Sues Brave Browser Over AI Content Scraping and Resale](#item-2) ⭐️ 7.0/10
3. [Nvidia reportedly caps Chinese customers at 49% of new data center business](#item-3) ⭐️ 7.0/10
4. [Shanghai&\#x27;s first AI compute theft case ends with suspended three-year sentence](#item-4) ⭐️ 6.0/10
5. [Putin Orders Private Data Centres to Reserve 10% of Capacity for State Use](#item-5) ⭐️ 6.0/10
6. [Apple Seeds iOS 27.3 Beta With Redesigned Health App and Always-On Watch AI](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Rumor: DeepSeek V5 May Be Trained on Huawei Ascend Chips](https://www.eet-china.com/mp/a536460.html) ⭐️ 7.0/10

Industry supply-chain sources cited in a report say DeepSeek&\#x27;s next-generation V5 model is planned to be trained on Huawei Ascend chips, a job previously handled by Nvidia hardware. Until now, Ascend chips were used mainly for running DeepSeek models \(inference\) rather than training them. If true, it would be the first time DeepSeek trains a flagship model on domestic Chinese silicon, a symbolic milestone for Huawei&\#x27;s Ascend ecosystem and for China&\#x27;s effort to reduce reliance on Nvidia. It could also push other Chinese AI labs to test Ascend for training, reshaping the country&\#x27;s AI hardware supply chain. The claim is an unconfirmed supply-chain rumor with no official confirmation from DeepSeek or Huawei, and no details on chip models, cluster size or training scale. Notably, at the end of September DeepSeek open-sourced Ascend-oriented infrastructure components, including the TileLang compiler tool, high-performance compute libraries and a distributed communication library, mirroring its earlier Nvidia-facing releases.

telegram · zaihuapd · Nov 3, 06:20

**Background**: Training and inference are different workloads: training builds a model by repeatedly processing massive datasets across thousands of chips, which demands far more compute, memory bandwidth and inter-chip communication than serving a finished model. Huawei&\#x27;s Ascend chips, based on its Da Vinci architecture, are China&\#x27;s leading domestic AI accelerators but have historically been seen as harder to program and less mature than Nvidia&\#x27;s CUDA ecosystem, especially for large-scale training. DeepSeek&\#x27;s open-source Ascend toolchain is significant because software maturity, not just raw chip performance, is the main barrier to moving training workloads off Nvidia.

<details><summary>References</summary>
<ul>
<li><a href="https://www.infoq.cn/article/t5i2Yv2z0LwIbK36lteR">DeepSeek 开源 昇 腾 平 台 基础设施组件，覆盖 TileLang... - InfoQ</a></li>
<li><a href="https://openbci-cn.com/m/article/20261002-9076.shtml">小时报| DeepSeek 开源 昇 腾 基础组件： 计 算 、 通 信 与 编 译 工 具 同步发 布</a></li>
<li><a href="https://www.alauda.cn/blog/1099/">模 型 训 练 和 推 理 的 区 别 ：资源消耗 与 工程差异 | 灵雀云博客</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Huawei Ascend`, `#AI training`, `#China AI`, `#hardware`

---

<a id="item-2"></a>
## [New York Times Sues Brave Browser Over AI Content Scraping and Resale](https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/) ⭐️ 7.0/10

On Monday, The New York Times sued privacy browser maker Brave in Manhattan federal court, alleging that Brave used undisclosed crawlers to build an index of more than 30 billion web pages and then sold access to that content to AI companies including Anthropic, Perplexity, Mistral, xAI and Cohere. The same day, other outlets including the New York Daily News and the Chicago Tribune filed similar suits, and the plaintiffs are seeking injunctions and damages; Brave has not yet responded. This case widens the AI copyright fight from model developers to the middlemen who supply training and retrieval data, putting crawler operators, RAG pipeline builders and dataset vendors directly in the legal crosshairs. If the theory holds, browser vendors and independent index builders may need explicit publisher licenses before selling web-scale corpora, reshaping the market for AI training data. The complaint alleges Brave&\#x27;s crawlers bypassed paywalls and blocked publishers&\#x27; ads while its browser marketed a “paywall blocker” feature covering “hundreds of top publishers,” and it targets Brave&\#x27;s resale of the index rather than the model outputs themselves — a distinct legal theory from output-based claims against AI labs. The reported scale of the index, over 30 billion pages, is central to the publishers&\#x27; argument that this was systematic copying rather than incidental indexing.

telegram · zaihuapd · Nov 3, 06:50

**Background**: Brave is a Chromium-based browser that markets itself on blocking ads and trackers, and it has offered a feature that removes paywalls — the subscriber-only gates publishers use to charge for articles, some of which are enforced on the server and thus harder to circumvent. AI companies need web-scale text corpora to train models and to power retrieval-augmented search, and that data typically comes from automated crawlers that identify themselves in robots.txt and are often governed by licenses. Publishers argue that crawler access for search indexing is not the same as harvesting content to resell as an AI data product.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/tech/1024588/brave-lawsuit-ai-scraping-new-york-times">The New York Times sues Brave web browser for AI scraping and...</a></li>
<li><a href="https://brave.com/">The browser that puts you first | Brave</a></li>
<li><a href="https://promptwatch.com/bots/mistralai-index">MistralAI- Index : AI Crawler Guide &amp; robots.txt | Promptwatch</a></li>

</ul>
</details>

**Tags**: `#AI copyright`, `#web scraping`, `#Brave browser`, `#publisher lawsuits`, `#AI training data`

---

<a id="item-3"></a>
## [Nvidia reportedly caps Chinese customers at 49% of new data center business](https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits) ⭐️ 7.0/10

According to a Financial Times report, Nvidia has asked data center operators worldwide to keep Chinese customers below 49% of new business, ensuring at least 51% comes from non-Chinese firms. The restriction reportedly applies globally but only to newly signed and future contracts, leaving existing leases untouched, and was communicated verbally by sales and regional teams rather than through any formal document. If accurate, this marks an unusual case of a US chip vendor self-imposing a China-related quota on its customers rather than acting on a published regulation, effectively extending export-control logic into commercial leasing decisions. It could reshape how AI cloud capacity is allocated globally and force Chinese AI firms to rely more heavily on domestic infrastructure or overseas partners willing to absorb the risk. The cap is described as covering only new and future contracts, so existing leases remain unaffected, and no written policy has surfaced, leaving the reported guidance unconfirmed and dependent on anonymous sourcing. Nvidia&\#x27;s response framed the issue around US policy encouraging cloud providers to serve global customers on US-based infrastructure, rather than confirming or denying a specific 49% figure.

telegram · zaihuapd · Nov 3, 16:19

**Background**: Since 2022 the US has progressively tightened export controls on advanced AI chips sold to China, forcing Nvidia to design China-specific parts and repeatedly adjust its product lineup while Washington and Beijing trade restrictions. Those rules formally govern the sale of chips and related technology; the reported 49% guidance instead targets the customer mix of data center operators that rent out GPU capacity, a channel not obviously covered by chip export rules. Nvidia has repeatedly argued that restricting US chips abroad risks pushing global AI development onto alternative hardware stacks, which colours how the company frames compliance measures.

**Tags**: `#Nvidia`, `#data centers`, `#US-China tech`, `#export controls`, `#AI infrastructure`

---

<a id="item-4"></a>
## [Shanghai&\#x27;s first AI compute theft case ends with suspended three-year sentence](https://www.thepaper.cn/newsDetail_forward_34389477) ⭐️ 6.0/10

A Shanghai court has sentenced a man surnamed Zong to three years in prison, suspended for three years, plus a 40,000 yuan fine, in the city&\#x27;s first case of forging signatures and stealing large-model compute. Zong bypassed the platform&\#x27;s protections, used more than 4 million accounts to farm new-user credits, illegally called model interfaces over 290,000 times, and resold the generated output for a profit of more than 34,000 yuan. This is the first criminal sentencing in Shanghai for &quot;compute arbitrage,&quot; signaling that prosecutors now treat abusing AI platform sign-up incentives and reselling model access as a computer-crime rather than a gray-market business. It puts AI service providers and security teams on notice that account-farming and API resale schemes carry real criminal exposure, not just terms-of-service violations. The conviction was for illegally obtaining computer information system data, and prosecutors emphasized that the scheme bore no compute costs of its own — the platform paid for every inference. Notably, the illicit profit \(about 34,000 yuan\) was small relative to the scale of abuse \(4 million accounts, 290,000+ API calls\), suggesting the volume of unauthorized access, not the revenue, drove the sentencing.

telegram · zaihuapd · Nov 3, 08:43

**Background**: AI platforms typically hand out free credits to new users to encourage trials, and they authenticate API requests with signed keys so that requests cannot be forged or replayed. So-called compute arbitrage exploits these mechanisms: actors mass-register accounts to harvest free credits, forge or reverse-engineer API signatures to make requests look legitimate, and then resell the resulting model output at a discount. Chinese lawyers have flagged three common variants — bulk registration for free compute, API relay/resale of overseas models, and shared high-tier memberships — all of which can touch criminal provisions such as illegal acquisition of computer information system data, copyright infringement, and fraud.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mankunlaw.com/insights/shao-shi-wei-lu-shi-ai-agent-suan-li-tao-li-mo-shi-ji-qi-fa-lu-feng-xian-fen-xi/">邵诗巍律师 | AI Agent算力套利模式及其法律风险分析</a></li>

</ul>
</details>

**Tags**: `#AI算力`, `#网络安全`, `#法律判例`, `#平台滥用`, `#黑产`

---

<a id="item-5"></a>
## [Putin Orders Private Data Centres to Reserve 10% of Capacity for State Use](https://www.reuters.com/technology/putin-orders-private-data-centres-set-aside-10-capacity-support-it-2026-11-02/) ⭐️ 6.0/10

Russian President Vladimir Putin signed a presidential decree requiring all non-state data centres in Russia to set aside 10% of their floor space and computing capacity for government use, with operators obliged to hand over access within 24 hours of receiving notice. The decree also tasks the Digital Development Ministry with conducting a nationwide inventory of available private data-centre capacity, and allows the government — with approval from the FSB — to temporarily draw on data-centre resources located outside Russia. The decree turns private cloud and colocation capacity into a state-reservable resource, raising compliance, overprovisioning and contract-risk costs for data-centre operators and their customers inside Russia. It is a concrete step in the broader trend of governments asserting sovereignty over computing infrastructure, and it creates geopolitical risk for foreign workloads that rely on servers located in Russia. The reservation covers both physical space and compute, and a dedicated government commission will be empowered to order operators to release the reserved resources; the decree does not, in the reported text, describe a compensation mechanism for operators. The extraterritorial clause — tapping facilities abroad with FSB approval — is unusual, and it is unclear how it would be enforced against foreign-owned providers.

telegram · zaihuapd · Nov 3, 10:58

**Background**: Russia has for years been building what it calls a &quot;sovereign internet,&quot; including a 2015 data-localisation law that requires personal data of Russian citizens to be stored on servers inside the country, and periodic tests of disconnecting the national network from the global internet. Data-centre capacity — space, power and servers available on demand — is the physical layer that cloud services and government portals run on, so requisitioning a share of it is a way to guarantee continuity of state IT systems during disruptions. Because sanctions have limited access to Western servers and chips, Russian operators already run tight on hardware, making a mandatory 10% set-aside more costly than it would be in a better-supplied market.

**Tags**: `#data centers`, `#tech policy`, `#cloud infrastructure`, `#digital sovereignty`, `#regulation`

---

<a id="item-6"></a>
## [Apple Seeds iOS 27.3 Beta With Redesigned Health App and Always-On Watch AI](https://www.macrumors.com/2026/11/03/ios-27-3-health-app/) ⭐️ 6.0/10

Apple released iOS 27.3 and watchOS 27.3 developer betas ahead of a December public launch, featuring a redesigned Health app with Insights and Longevity tabs plus a new &quot;health age&quot; metric. The update also adds always-on AI listening to Apple Watch Series 12 and Ultra 4 — Siri Recap, which turns conversation highlights into bulleted items, and Live Rewind, which shows the previous 15 seconds of speech as text — and begins testing a China-specific Apple Intelligence build branded &quot;Apple 智能与Siri&quot; in partnership with Alibaba&\#x27;s Qwen. The China build marks Apple&\#x27;s first Apple Intelligence rollout under China&\#x27;s generative-AI filing regime with a domestic model partner, opening the feature set to the company&\#x27;s largest iPhone market. Meanwhile, always-on listening on the wrist signals Apple&\#x27;s push toward ambient, context-aware AI in wearables, a direction that will shape how developers and privacy regulators think about continuous audio capture. Siri Recap and Live Rewind are English-only at launch, and Live Rewind only surfaces the preceding 15 seconds of transcribed speech rather than a full transcript. The China build ships a subset of features \(notification summaries, Genmoji and related tools\) and the Health app&\#x27;s language support expands to 11 languages, including Chinese.

telegram · zaihuapd · Nov 3, 18:50

**Background**: Apple Intelligence is Apple&\#x27;s umbrella term for its generative AI features, which run either on-device or through Private Cloud Compute; Genmoji, for instance, generates custom emoji from a text prompt or a photo. China requires generative AI services to complete a filing and approval process before public release, which is why Apple partnered with Alibaba&\#x27;s Qwen model family to bring the features to domestic iPhones. The new &quot;health age&quot; in the Health app is an estimate of physiological age derived from the metrics an iPhone and Apple Watch already collect, such as activity, sleep and heart data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/">Apple 智能即将登陆中国 - Apple (中国大陆)</a></li>
<li><a href="https://blog.csdn.net/gdwhkj/article/details/163444050">国行 Apple Intelligence 获批：苹果 AI 落地中国，隐私与本地化成为...</a></li>
<li><a href="https://www.aliyun.com/product/tongyi">千问大模型_AI大模型_一站式大模型推理和部署服务-阿里云</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#iOS`, `#Apple Intelligence`, `#Wearables`, `#Consumer Tech`

---