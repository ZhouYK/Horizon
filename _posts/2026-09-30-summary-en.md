---
layout: default
title: "Horizon Summary: 2026-09-30 (EN)"
date: 2026-09-30 23:04:10 +0000
lang: en
report: default
---

> From 192 items, 10 important content pieces were selected

---

1. [Apple&\#x27;s New CEO Ternus Pushes to Speed Up and Streamline the Company](#item-1) ⭐️ 8.0/10
2. [DeepSeek Open-Sources Huawei Ascend Base Components](#item-2) ⭐️ 8.0/10
3. [Cloudflare to Become a Public Certificate Authority](#item-3) ⭐️ 8.0/10
4. [Trump and Six AI Giants Sign Voluntary AI Safety Agreement](#item-4) ⭐️ 7.0/10
5. [Microsoft Uses Outsourced Workers to Review Copilot Image Prompts](#item-5) ⭐️ 7.0/10
6. [Kimi K3 Becomes First Chinese Open Model in OpenAI Enterprise Billing](#item-6) ⭐️ 7.0/10
7. [Bilibili open-sources Index-Translate multilingual translation models covering 150 languages](#item-7) ⭐️ 7.0/10
8. [McDonald&\#x27;s reportedly uses AI for store-by-store dynamic burger pricing](#item-8) ⭐️ 6.0/10
9. [Tencent Reportedly Secretly Building Consumer AI Agent App &\#x27;Handy Bot&\#x27;](#item-9) ⭐️ 6.0/10
10. [Apple Reportedly to Unveil Smart Home Hub on October 13](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Apple&\#x27;s New CEO Ternus Pushes to Speed Up and Streamline the Company](https://www.bloomberg.com/news/articles/2026-09-29/apple-s-new-ceo-moves-to-overhaul-company-to-run-faster-and-leaner) ⭐️ 8.0/10

Apple&\#x27;s newly installed CEO John Ternus, just weeks into the job, has begun driving an internal overhaul aimed at accelerating product development, widening the product line, and making the organization leaner and more engineering-focused. According to Bloomberg and Reuters, Apple is weighing a move away from its rigid spring-and-fall release cadence toward more flexible, year-round launches, while trimming some middle-management roles and shortening the decision chain between engineering teams and top executives. Apple&\#x27;s release cadence and management structure have been among the most imitated templates in the consumer electronics industry, so any shift toward faster, less seasonal launches could ripple through supply chains, app developers, and rival hardware makers that plan around Apple&\#x27;s calendar. It also signals that the company is looking for new revenue streams and more value out of existing products rather than relying on its traditional annual blockbuster cycle. The overhaul reportedly targets a shorter decision chain between engineering teams and senior leadership, with some middle-management positions being cut, and Ternus is described as exploring new revenue sources and ways to monetize existing products. Notably, the change to the launch schedule is still under consideration rather than finalized, and no specific product timelines, headcount figures, or dates have been disclosed.

telegram · zaihuapd · Sep 30, 01:07

**Background**: Apple has long organized its year around a predictable rhythm, most famously a September iPhone event plus spring updates for Macs and iPads, a cadence that lets suppliers, carriers, and developers plan far in advance. John Ternus is a longtime Apple hardware executive who led hardware engineering and oversaw major product lines including the iPhone, Mac, and iPad as well as the company&\#x27;s transition to its own Apple silicon chips, so his push for a more engineering-driven, faster-moving Apple is consistent with that background. He took over as CEO following the long tenure of Tim Cook, whose era was defined by operational scale and a tightly choreographed annual product calendar.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/">Tim Cook to become Apple Executive Chairman John Ternus to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/John_Ternus">John Ternus - Wikipedia</a></li>
<li><a href="https://eonsr.com/en/apples-strategic-shift-in-product-release-cycles/">Apple’s strategic shift in product release cycles - EONSR</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#leadership`, `#corporate restructuring`, `#product strategy`, `#tech industry`

---

<a id="item-2"></a>
## [DeepSeek Open-Sources Huawei Ascend Base Components](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 8.0/10

On September 30, DeepSeek open-sourced a suite of base components for Huawei&\#x27;s Ascend platform, covering the TileLang high-level kernel language and compiler toolchain, compute libraries and a distributed communication library, mirroring the components it already ships for NVIDIA GPUs. The release includes DeepGEMM Ascend, DeepEP Ascend, TileKernels, FlashMLA and DeepSelect, and DeepSeek says these components reach near hardware-limit performance in multiple benchmarks while it works with Huawei on a 128-card Ascend 950 supernode deployment. This is one of the most direct attempts yet to reproduce the CUDA software advantage on Chinese domestic accelerators, giving Ascend users a production-grade GEMM, attention and expert-parallel communication stack rather than leaving them to hand-write kernels. If the claimed performance holds, it lowers the cost of training and serving large models on hardware that is not subject to NVIDIA export controls, which matters to Chinese labs, cloud providers and anyone hedging against GPU supply risk. DeepGEMM Ascend is a port that is fully API-compatible with the original DeepGEMM and supports BF16, FP8 and FP4 GEMM as well as MQA logits and MegaMoE, with the team reporting 99.8% of the hardware limit on GEMM and 98% on MegaMoE. DeepEP Ascend supplies high-throughput, low-latency expert-parallel all-to-all kernels for MoE dispatch and combine, including FP8 dispatch and deferred epilogues; however, the announcement itself is brief and originates from Telegram/WeChat reposts, so independent verification is still limited.

telegram · zaihuapd · Sep 30, 03:09

**Background**: TileLang is a domain-specific tiling language that lets developers write GPU/NPU kernels in Python-like syntax and explicitly place tile buffers within the hardware memory hierarchy, rather than relying on opaque compiler optimisations; it is often described as an alternative path to CUDA for non-NVIDIA chips. DeepGEMM is DeepSeek&\#x27;s high-performance matrix multiplication \(GEMM\) library, the core primitive behind transformer compute, while DeepEP is its expert-parallel communication library used to move tokens between experts in Mixture-of-Experts models. Huawei&\#x27;s Ascend NPUs are China&\#x27;s leading domestic AI accelerators, and a &\#x27;supernode&\#x27; refers to a scale-up design that links many NPUs, in this case 128 Ascend 950 chips, through a high-bandwidth interconnect so they behave like one large machine.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepGEMM-Ascend">GitHub - deepseek-ai/DeepGEMM-Ascend: DeepGEMM-Ascend: clean ...</a></li>
<li><a href="https://github.com/deepseek-ai/DeepEP-Ascend">GitHub - deepseek-ai/DeepEP-Ascend: A high-performance ...</a></li>
<li><a href="https://tilelang.com/get_started/overview.html">The Tile Language: A Brief Introduction - TileLang 0.1.14 documentation</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Huawei Ascend`, `#Open Source`, `#AI Infrastructure`, `#TileLang`

---

<a id="item-3"></a>
## [Cloudflare to Become a Public Certificate Authority](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 8.0/10

Cloudflare announced plans to become a public certificate authority, having applied to join the Chrome, Apple, Microsoft, and Mozilla root certificate programs and signed an agreement with GlobalSign to acquire a widely trusted root certificate. The company has not yet begun issuing certificates, but says the new CA will prioritize ACME-based automated issuance and renewal, with production Merkle Tree Certificates \(MTC\) targeted for Q1 2027 to serve a post-quantum internet. Cloudflare is one of the largest providers of web infrastructure and termination points for TLS traffic, so its entry into the public CA market could reshape certificate issuance by pushing down costs and making full automation the default rather than an add-on. Its roadmap also puts a major industry player behind Merkle Tree Certificates, which could accelerate the web PKI&\#x27;s transition to post-quantum cryptography well before quantum computers threaten today&\#x27;s RSA and ECC signatures. The plan is an announcement rather than a shipping product: Cloudflare still needs to be accepted into the browser root programs, and it has not issued any certificates yet. The Q1 2027 MTC target is a future milestone, and MTC itself is still an experimental IETF draft format rather than a finalized standard.

telegram · zaihuapd · Sep 30, 06:26

**Background**: A public certificate authority is a organization whose root certificates are trusted by browsers and operating systems, allowing it to issue TLS/SSL certificates that prove a website&\#x27;s identity. To gain that trust, a CA must be audited and accepted into root programs run by Google, Apple, Microsoft, and Mozilla, which is why acquiring an already-trusted root from GlobalSign is a key step. The ACME protocol \(used by Let&\#x27;s Encrypt\) automates domain validation, issuance, and renewal so certificates can be deployed at very low cost without manual work. Merkle Tree Certificates are a proposed alternative to traditional X.509 certificates: instead of signing each certificate individually, the CA batches many certificates into a single Merkle tree and signs only the tree root, letting browsers verify inclusion with a short proof — an approach that keeps certificate sizes small even with the large signatures that post-quantum algorithms require.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment">Automatic Certificate Management Environment - Wikipedia</a></li>
<li><a href="https://www.sectigo.com/blog/what-are-merkle-tree-certificates-mtcs">What are Merkle Tree Certificates (MTCs)? | Sectigo® Official</a></li>
<li><a href="https://www.encryptionconsulting.com/about-merkle-tree-certificates/">Merkle Tree Certificates: Rethinking the WebPKI for the Post ...</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#Public CA`, `#PKI`, `#ACME`, `#Post-Quantum`

---

<a id="item-4"></a>
## [Trump and Six AI Giants Sign Voluntary AI Safety Agreement](https://www.zaobao.com.sg/news/world/story20260930-9758185) ⭐️ 7.0/10

On September 29, US President Trump signed a one-page AI agreement with the heads of Google, Anthropic, Meta, OpenAI, xAI and Nvidia, and posted the document on Truth Social, describing it as &quot;morally binding.&quot; The agreement requires companies to build a four-layer control mechanism: cooperating with independent external auditors to evaluate their AI control systems, establishing an independent board committee for oversight, and monitoring AI capabilities and alignment for cyber, biological and chemical risks during both model training and deployment. The signing brings the six most influential AI developers and chip suppliers into a single, publicly announced safety framework endorsed at the presidential level, which could set norms for how frontier labs handle catastrophic-risk oversight. Because the commitments are voluntary and self-described as moral rather than legal, the announcement is likely to shape industry expectations and public debate more than it imposes enforceable obligations. The document is only one page long, is characterized by Trump as &quot;morally binding,&quot; and contains no penalty, verification or enforcement mechanism beyond the internal and external reviews it describes. The four-layer structure covers internal controls run by company teams, independent external audit or evaluation bodies that check whether monitoring and detection systems actually work, and a board-level independent committee that receives reports and must ensure identified problems are remediated.

telegram · zaihuapd · Sep 30, 02:30

**Background**: AI alignment refers to closing the gap between what humans actually want and what a model is optimized to do, and it is a core research area as models grow more capable. Independent external auditing, in the form proposed by labs such as Anthropic, would give third-party evaluators near-internal access so safety checks become continuous rather than occasional spot checks. The key distinction here is legal versus moral bindingness: moral commitments rely on public opinion and internal conviction rather than state enforcement, so they lack the compulsory force of a contract or statute. The agreement follows earlier voluntary arrangements, such as the White House pre-release review framework agreed with OpenAI, Anthropic and Google.

<details><summary>References</summary>
<ul>
<li><a href="https://news.mydrivers.com/1/1154/1154817.htm">美国白宫发布人工智能协议：特朗普与黄仁勋、马斯克等六家CEO...</a></li>
<li><a href="https://juejin.cn/post/7684583207288225855">Anthropic CEO突然喊踩刹车，OpenAI罕见力挺： AI ...</a></li>
<li><a href="https://wenku.baidu.com/view/932ab727a66925c52cc58bd63186bceb19e8eda1.html">约束力是什么意思？3分钟搞懂物理、法律与道德中的约束力区别</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#AI Policy`, `#Regulation`, `#Tech Industry`, `#Governance`

---

<a id="item-5"></a>
## [Microsoft Uses Outsourced Workers to Review Copilot Image Prompts](https://www.404media.co/humans-reading-copilot-prompts-images/) ⭐️ 7.0/10

According to reporting by 404 Media \(also covered by The Verge\), Microsoft employs hundreds of outsourced contract workers whose job is to review the prompts, requests, and private photos users submit to Microsoft Copilot in order to improve its image generation and editing features. The report says these reviewers are exposed to large volumes of disturbing material, including sexualized &quot;upskirt&quot; images and potentially illegal animal sacrifice footage. The story shows that conversations and uploads sent to Copilot are not truly private, which could affect how hundreds of millions of users share data with AI assistants. It also spotlights the labor and ethics side of AI deployment, since the human moderators absorbing this content are outsourced contractors with limited protections. The reviewers are described as being flooded with graphic and sometimes potentially illegal imagery, and the reporting characterizes the work as causing severe psychological trauma and exploitation of the outsourced staff. Microsoft is not depicted as automatically flagging these cases for users or giving them a clear way to opt out of human review of their prompts and photos.

telegram · zaihuapd · Sep 30, 07:13

**Background**: Microsoft Copilot is Microsoft&\#x27;s generative AI assistant, which can create and edit images from text prompts. Like many cloud AI services, it collects user prompts and uploaded files to evaluate and improve model quality, and that evaluation is often done by human reviewers rather than by automation alone. Content moderation for such products is commonly outsourced to contract workers who screen high volumes of user-generated material. This item fits into a wider debate about whether AI companies properly disclose human review of user data and protect the people doing that work.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Copilot">Microsoft Copilot</a></li>
<li><a href="https://hai.stanford.edu/news/privacy-ai-era-how-do-we-protect-our-personal-information">Privacy in an AI Era: How Do We Protect Our Personal ...</a></li>

</ul>
</details>

**Tags**: `#AI privacy`, `#content moderation`, `#Microsoft Copilot`, `#AI ethics`, `#outsourced labor`

---

<a id="item-6"></a>
## [Kimi K3 Becomes First Chinese Open Model in OpenAI Enterprise Billing](https://36kr.com/newsflashes/4005691489112198) ⭐️ 7.0/10

US AI infrastructure company Baseten announced that enterprise users can now run Kimi K3 inside OpenAI&\#x27;s Codex coding tool, with usage costs charged directly against their existing OpenAI enterprise purchase commitments rather than requiring a separate vendor procurement process. This makes Kimi K3 the first Chinese open-source model to enter OpenAI&\#x27;s enterprise paid settlement channel. It signals a notable shift in enterprise AI procurement: companies can adopt a leading Chinese open-weight model without going through a new vendor onboarding, security review or budget approval cycle. It also marks an unusual cross-platform integration in which a non-OpenAI model rides on OpenAI&\#x27;s commercial billing rails, potentially loosening the grip of single-vendor model lock-in for large buyers. Kimi K3 is Moonshot AI&\#x27;s open-weight model, reported to have around 2.8 trillion parameters and a 1 million token context window, which is what makes it attractive for agentic coding workloads like Codex. Baseten, founded in 2019 and headquartered in San Francisco, supplies the inference infrastructure that serves the model, but the announcement gives no details on pricing, latency, regional availability or which enterprise tiers are covered.

telegram · zaihuapd · Sep 30, 11:23

**Background**: OpenAI Codex is OpenAI&\#x27;s AI coding agent that helps engineering teams plan, write, refactor and review code, and enterprises typically buy access through annual committed-spend contracts. Kimi K3 is developed by China&\#x27;s Moonshot AI and released with open weights, meaning third parties such as Baseten can host and serve it on their own infrastructure. Baseten is an AI inference infrastructure provider that packages open models for production enterprise deployment, so routing Kimi K3 through it lets customers consume a Chinese model while drawing down budget they have already committed to OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/Baseten/64303191">Baseten - 百度百科</a></li>
<li><a href="https://openai.com/zh-Hans-CN/codex/">Codex | OpenAI 打造的 AI 编码助手</a></li>
<li><a href="https://rar.design/posts/kimi-k3-designer-guide">Kimi ... - RAR 設計攻略</a></li>

</ul>
</details>

**Tags**: `#Kimi K3`, `#OpenAI Codex`, `#Enterprise AI`, `#Chinese LLM`, `#Baseten`

---

<a id="item-7"></a>
## [Bilibili open-sources Index-Translate multilingual translation models covering 150 languages](https://www.ithome.com/1/008/914.htm) ⭐️ 7.0/10

On September 30, Bilibili&\#x27;s Index LLM team released the Index-Translate family of multilingual translation models, publishing the weights of three text models — 2B, 9B, and a 35B-A3B preview — on both Hugging Face and ModelScope, with support for 150 languages. It gives the open machine-translation ecosystem a substantive, immediately downloadable model family that spans from lightweight on-device sizes to a large mixture-of-experts variant, rather than a single research checkpoint, and it signals that a Chinese consumer-internet company is investing seriously in open multilingual translation. The models are built on Qwen3.5 and accept translation instructions covering terminology, formatting, and content that must be preserved, and the family extends beyond plain text to speech translation, syllable-controllable translation, and long-document translation; the 35B-A3B variant is a Mixture-of-Experts design with roughly 3B active parameters, and the largest text model is still labeled a preview.

telegram · zaihuapd · Sep 30, 14:08

**Background**: Machine translation \(MT\) is the task of automatically converting text from one language to another, and open-weight MT models let anyone run or fine-tune translation locally instead of paying for a closed API. Qwen3.5 is Alibaba&\#x27;s open-weight foundation model series, released under permissive licenses, that many teams use as a base for domain-specific models. Mixture-of-Experts \(MoE\) is an architecture in which only a small subset of a model&\#x27;s parameters is activated per token — hence a &quot;35B-A3B&quot; model has 35 billion total parameters but activates about 3 billion — which makes large models cheaper to serve. Bilibili&\#x27;s Index team is already known in the open-source community for models such as the lightweight Index-1.9B language model and the IndexTTS speech synthesis system.

<details><summary>References</summary>
<ul>
<li><a href="https://www.openai-hub.com/news/2235/">B站开源 Index - Translate 翻译模型：覆盖150种语言 - OpenAI Hub</a></li>
<li><a href="https://echora.audio/models/indextts">IndexTTS: Bilibili Open - Source Zero-Shot Voice Cloning TTS</a></li>
<li><a href="https://qwen-ai.com/">Qwen AI — Open-Source LLMs, Vision, Audio &amp; Coding Models (2026)</a></li>

</ul>
</details>

**Tags**: `#open-source-models`, `#machine-translation`, `#multilingual-nlp`, `#llm`, `#moE`

---

<a id="item-8"></a>
## [McDonald&\#x27;s reportedly uses AI for store-by-store dynamic burger pricing](https://www.engadget.com/2272211/mcdonalds-is-reportedly-using-ai-to-dynamically-price-its-burgers/) ⭐️ 6.0/10

McDonald&\#x27;s is reportedly using AI-driven pricing tools to adjust menu prices store by store across the US and some overseas markets, with the algorithm estimating each location&\#x27;s customers&\#x27; willingness to pay. Two Fresno, California stores roughly 3 km apart were cited selling a Big Mac for $5.69 and $6.89 respectively — a 21% gap for the same item in the same city. The story pushes dynamic pricing — long common in airlines, hotels and ride-hailing — into mass-market fast food, raising questions about price fairness and whether consumers will accept paying more for the same burger depending on which store they walk into. It also signals how AI recommendation and optimization systems are spreading into everyday retail operations, with franchisees potentially caught between corporate pricing strategy and customer backlash. McDonald&\#x27;s denied the reporting as speculation containing inaccurate information, saying its pricing tool only makes recommendations and is not mandatory; however, multiple franchisees claimed they were pressured to adopt it, and the company reportedly tracks whether stores follow the algorithm&\#x27;s suggested prices. The mechanism is essentially a willingness-to-pay estimation model, the same class of revenue-management technique used in airline and hotel pricing.

telegram · zaihuapd · Sep 30, 01:37

**Background**: Dynamic pricing, also called surge or demand pricing, is a revenue-management strategy in which businesses flex prices based on current market demand, typically charging more at peak times and less off-peak. It is standard in hospitality, tourism, entertainment, electricity and public transport, and is powered by algorithms that weigh competitor pricing, supply and demand, and other market signals. Because customers often perceive it as price gouging, its expansion into sectors like fast food tends to stir public controversy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_pricing">Dynamic pricing</a></li>
<li><a href="https://priceva.com/blog/optimizing-prices-with-machine-learning">Optimizing Prices with Machine Learning (ML) | Priceva</a></li>
<li><a href="https://fastercapital.com/content/Willingness-to-Pay--Price-and-Preference--Estimating-Willingness-to-Pay-through-Discrete-Choice.html">Willingness to Pay : Price and Preference: Estimating ... - FasterCapital</a></li>

</ul>
</details>

**Tags**: `#AI`, `#dynamic pricing`, `#retail`, `#McDonald&\#x27;s`, `#business ethics`

---

<a id="item-9"></a>
## [Tencent Reportedly Secretly Building Consumer AI Agent App &\#x27;Handy Bot&\#x27;](https://mp.weixin.qq.com/s/p9jYzMELaVodd5V3ZqaOnw) ⭐️ 6.0/10

Tencent is reportedly secretly developing a personal AI agent product called &quot;Handy Bot&quot;, which is planned to launch as a standalone app and has already appeared on WeChat as a service account whose bio reads &quot;Your Personal AI Agent&quot;. The product is said to still be in closed beta, with the report explicitly noting that official announcements should be treated as authoritative. If confirmed, it would mark Tencent&\#x27;s entry into the consumer personal-agent race alongside Alibaba&\#x27;s Qwen and ByteDance&\#x27;s Doubao, following Meta&\#x27;s Muse push, intensifying competition over who owns the default AI entry point on users&\#x27; devices. Control of that entry point could reshape how hundreds of millions of users search, shop and complete tasks online. The report is short and uncorroborated, offering no technical specifics such as the underlying model, supported platforms, or a launch date, and the only concrete artifact is the WeChat service account. Tencent has a strong distribution channel in WeChat, which makes a WeChat-first soft launch plausible but also means the final shape of the standalone app is still unknown.

telegram · zaihuapd · Sep 30, 02:06

**Background**: A &quot;personal AI agent&quot; \(个人智能体\) is software that takes a high-level goal from a user and then works on it in the background, planning steps and calling tools rather than just answering single questions. Meta popularized the consumer version of this idea with Muse, announced in September 2026 as a personal agent that runs on a dedicated &quot;Muse Secure VM&quot; to isolate the agent and the user&\#x27;s data. In China, Alibaba&\#x27;s Qwen and ByteDance&\#x27;s Doubao are pursuing similar directions, and a WeChat service account \(服务号\) is a lightweight, official account type that brands use to push messages and offer services inside WeChat before shipping a full app.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/muse/">Muse: Meta&#x27;s personal AI agent, features &amp; capabilities</a></li>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse: The World’s First Personal AI Agent Built ...</a></li>
<li><a href="https://lilys.ai/zh/notes/ai-agents-20251225/2025-agent-ai-deep-dive">【万字揭秘】 2025年最大风口： Agent 智 能 体 到底是什么?</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Tencent`, `#Industry News`, `#Consumer AI`, `#China Tech`

---

<a id="item-10"></a>
## [Apple Reportedly to Unveil Smart Home Hub on October 13](https://www.bloomberg.com/news/articles/2026-09-30/apple-is-finally-ready-to-enter-its-next-big-category-the-smart-home) ⭐️ 6.0/10

Bloomberg reports that Apple plans to hold a launch event on October 13 to introduce its first screen-based smart home hub, a roughly 6-inch device codenamed J490, alongside refreshed HomePod mini and Apple TV models and a new version of its Siri AI assistant. Apple has not announced the products and declined to comment on the report. If accurate, this would mark Apple&\#x27;s formal entry into the screen-based smart home hub category long dominated by Amazon&\#x27;s Echo Show and Google&\#x27;s Nest Hub, and would tie Apple&\#x27;s home strategy tightly to a rebuilt Siri. It signals that Apple sees the home as its next major product category, a market where it has so far lagged behind rivals. The hub is said to identify household members through voice or facial recognition, then display personalized content and control connected devices. The report is based on anonymous insiders and remains unconfirmed, and no pricing, availability, or detailed technical specifications have been disclosed.

telegram · zaihuapd · Sep 30, 12:56

**Background**: A smart home hub is a central device that controls and coordinates connected appliances such as lights, locks, thermostats and cameras; Amazon&\#x27;s Echo Show and Google&\#x27;s Nest Hub added touchscreens to make these controls and video calls more visual. Apple already competes in this space with HomeKit, the HomePod and the Home app, but has never shipped a screen-equipped hub of its own. Siri, Apple&\#x27;s voice assistant, has widely been seen as trailing rivals in conversational AI, making a revamped AI-powered Siri central to whether a new hub can succeed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/retail-consumer/apple-plans-make-push-into-smart-home-market-oct-13-bloomberg-news-reports-2026-09-30/">Apple plans to launch new smart-home hub on Oct 13, Bloomberg ...</a></li>
<li><a href="https://www.ithome.com/0/904/355.htm">苹果 HomePad 带屏音箱曝光：定位 AI 智能家居中枢，能“刷脸”识别你的...</a></li>
<li><a href="https://www.studioglobal.ai/zh-cn/discover/answers/what-is-apple-s-internally-codenamed-j490-smart-6ab0e0bbc309f91ae0f26f35">苹果 J490 智能家居中枢：一块以 Siri AI 为核心的家庭屏幕</a></li>

</ul>
</details>

**Tags**: `#apple`, `#smart-home`, `#hardware`, `#siri`, `#industry-news`

---