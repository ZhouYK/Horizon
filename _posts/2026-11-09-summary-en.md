---
layout: default
title: "Horizon Summary: 2026-11-09 (EN)"
date: 2026-11-09 23:04:47 +0000
lang: en
report: default
---

> From 260 items, 9 important content pieces were selected

---

1. [Unpatched iOS Sandbox Escape &\#x27;worse\_query&\#x27; Released, Hits iOS 26–27.3 Beta](#item-1) ⭐️ 8.0/10
2. [Cambridge AI-Designed Avian Flu Vaccine Shows Broad Protection in Animals](#item-2) ⭐️ 8.0/10
3. [Google unveils TPU 8tx and TPU 8i Max, escalating Nvidia challenge](#item-3) ⭐️ 8.0/10
4. [ByteDance Releases Seedream 5.5 With 100-Round Editing and Native Transparency](#item-4) ⭐️ 7.0/10
5. [OPPO, vivo, Xiaomi and Honor launch joint ADV developer verification for Android sideloading](#item-5) ⭐️ 7.0/10
6. [Leaked EU Digital Fairness Act draft targets addictive design and in-game virtual currency](#item-6) ⭐️ 7.0/10
7. [Epoch AI: Six Chinese AI Firms Earn About One-Tenth of OpenAI and Anthropic Revenue](#item-7) ⭐️ 6.0/10
8. [BYD Debuts Robotic Flash-Charging Arm in the UAE](#item-8) ⭐️ 6.0/10
9. [SnowLuma goes private after Tencent cease-and-desist letter](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Unpatched iOS Sandbox Escape &\#x27;worse\_query&\#x27; Released, Hits iOS 26–27.3 Beta](https://x.com/forcequitOS/status/2119475139528020218?) ⭐️ 8.0/10

On November 8, security researcher forcequitOS published a zero-day sandbox escape proof-of-concept called worse\_query, which works on iOS 26.0 through 26.7.2 as well as iOS 27.2 and the iOS 27.3 beta. The PoC, developed with @0xjohnny and positioned as the direct successor to bad\_query, lets an app reach system paths and modify application data, and it was reportedly submitted to Apple but remains unpatched. Because the flaw is public and still unpatched on shipping and beta firmware, any researcher — or attacker — can study the technique before Apple ships a fix, which is exactly the window in which real-world exploits tend to appear. It also lowers the barrier for iOS modification tooling, since third-party projects can build on the escape far faster than Apple can close it. Using worse\_query requires the host app to set up an App Group container, so it is not a self-contained exploit and is described by its author as a developer/research tool unrelated to jailbreaking. Community tools have already adopted it, but with limits: the Erosion customization toolbox notes that worse\_query cannot write to MobileGestalt on iOS 26.

telegram · zaihuapd · Nov 9, 02:36

**Background**: iOS runs every third-party app inside a sandbox, a kernel-enforced boundary that normally restricts the app to its own container and blocks access to other apps&\#x27; data and system directories; a sandbox escape is the technique for breaking out of that boundary. App Groups are a legitimate Apple feature that lets a developer&\#x27;s apps share a container, which here serves as the foothold the exploit needs. This is distinct from a jailbreak, which typically requires kernel-level code execution and full system compromise — worse\_query only widens what a normal app can reach. MobileGestalt, meanwhile, is the system configuration store that tools like the MobileGestalt editors GestaltX and Erosion modify to change region codes, device presets and other hidden settings.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/forcequitOS/worse_query">GitHub - forcequitOS/ worse_query : A sandbox escape for iOS 26 and...</a></li>
<li><a href="https://onejailbreak.com/blog/worse_query-sandbox-escape-for-ios-26-and-27/">worse_query Sandbox Escape for iOS 26 and 27 Released</a></li>
<li><a href="https://github.com/jailbreakdotparty/Erosion/blob/main/">GitHub - jailbreakdotparty/Erosion: iOS customization toolbox...</a></li>

</ul>
</details>

**Discussion**: Community reaction has been fast and pragmatic rather than alarmist: within about a day, tools such as the GestaltX MobileGestalt editor for iOS 27.x appeared, and the Erosion project documented where worse\_query falls short. The main caveat raised is capability, not intent — the escape alone does not grant MobileGestalt write access on iOS 26.

**Tags**: `#iOS security`, `#sandbox escape`, `#zero-day`, `#vulnerability disclosure`, `#mobile security`

---

<a id="item-2"></a>
## [Cambridge AI-Designed Avian Flu Vaccine Shows Broad Protection in Animals](https://www.cam.ac.uk/stories/ai-developed-vaccines-against-viruses) ⭐️ 8.0/10

A University of Cambridge-led team reported in a paper published online in Cell Reports Medicine in November 2026 that an AI-assisted designed avian influenza vaccine candidate produced broad-spectrum immune responses and protection in mice and ferrets. The candidate outperformed a comparator formulation based on WHO candidate vaccine viruses in those animal studies, and the team now plans to move into human clinical trials. If the approach holds up in humans, computationally designed antigens could shorten the months-long cycle of selecting and engineering vaccine strains for seasonal and pandemic flu, giving public health agencies a faster tool for outbreak response. It also points toward broadly protective influenza vaccines that would not need to be reformulated every time the virus drifts. The broad-spectrum antigen is entirely human-designed and does not exist in nature, and the protection claims so far rest only on animal immunogenicity and challenge data, with no evidence yet of efficacy in people. Ferrets are the standard model for influenza research because they develop respiratory disease and transmission patterns similar to humans, which makes the ferret results a meaningful but still preliminary signal.

telegram · zaihuapd · Nov 9, 03:00

**Background**: Vaccines work by delivering an antigen, a molecule that trains the immune system to recognize a pathogen; for influenza, that antigen is usually a surface protein from a circulating or candidate strain. Because flu viruses mutate constantly, the WHO coordinates a global network that selects candidate vaccine viruses \(CVVs\) each season, and manufacturers then grow vaccine in eggs or cells from those strains — a process that can take months. AI-assisted antigen design instead uses computational models to propose protein sequences that may provoke immunity against a wider range of viral variants, which researchers hope will cut design time and reduce reliance on strain-by-strain updating.

<details><summary>References</summary>
<ul>
<li><a href="https://www.news-medical.net/news/20261105/AI-designed-vaccine-provides-complete-protection-against-diverse-bird-flu-variants.aspx">AI - designed vaccine provides complete protection against diverse bird...</a></li>
<li><a href="https://ivr.cidrap.umn.edu/universal-influenza-vaccine-technology-landscape">Universal Influenza Vaccine Technology Landscape | CIDRAP</a></li>
<li><a href="https://www.creative-biolabs.com/blog/vaccine/a-vaccine-central-in-h5-antigenic-space-confers-broad-immunity/">A Vaccine Central in H5 Antigenic Space Confers Broad Immunity...</a></li>

</ul>
</details>

**Tags**: `#AI drug design`, `#vaccines`, `#avian influenza`, `#biomedical research`, `#public health`

---

<a id="item-3"></a>
## [Google unveils TPU 8tx and TPU 8i Max, escalating Nvidia challenge](https://www.bloomberg.com/news/articles/2026-11-09/google-escalates-nvidia-rivalry-with-new-versions-of-its-tpu-systems) ⭐️ 8.0/10

Google announced two new Tensor Processing Units, TPU 8tx and TPU 8i Max, targeting secure/regulated workloads and ultra-long-context AI applications respectively. The launch breaks Google&\#x27;s previous roughly two-year cadence for new TPU generations and expands its AI chip lineup within a single year. The move intensifies Google&\#x27;s challenge to Nvidia by turning TPU from a mostly internal accelerator into a broader portfolio aimed at specific workloads, including regulated data and long-context models. It gives cloud customers and AI labs more alternatives to Nvidia GPUs and could reduce dependence on a single AI hardware supplier. TPU 8tx is aimed at government agencies and tightly regulated industries handling classified data, and it will work alongside AMD chips; TPU 8i Max integrates two TPU chips in one package for long-context AI, aiming to deliver more compute and memory capacity. Google is also breaking its old two-year cadence, and customers cited include Apple, Meta, Oracle, and Anthropic.

telegram · zaihuapd · Nov 9, 13:36

**Background**: A TPU \(Tensor Processing Unit\) is Google&\#x27;s custom AI accelerator, an application-specific integrated circuit designed for neural-network workloads and usable through frameworks such as TensorFlow, JAX, and PyTorch. Nvidia&\#x27;s GPUs have long been the default hardware for training and running large AI models, but Google has positioned TPUs as a competing option, especially through its cloud. Long-context AI refers to models that process very large inputs, such as long documents or codebases, which puts pressure on memory capacity and compute.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/blogs/tpu-vs-gpu/">TPU vs GPU - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#Google TPU`, `#AI chips`, `#Nvidia`, `#semiconductors`, `#AI infrastructure`

---

<a id="item-4"></a>
## [ByteDance Releases Seedream 5.5 With 100-Round Editing and Native Transparency](https://seed.bytedance.com/zh/blog/%E7%94%9F%E6%88%90%E6%9B%B4%E7%9C%9F%E5%AE%9E-%E7%99%BE%E8%BD%AE%E7%BC%96%E8%BE%91%E6%9B%B4%E7%A8%B3%E5%AE%9A-seedream-5-5-%E5%8F%91%E5%B8%83) ⭐️ 7.0/10

ByteDance has released Seedream 5.5, an image creation model that supports up to 100 rounds of continuous editing on a single work and can natively generate assets with a transparent \(RGBA\) alpha channel, alongside improvements in photorealism and text rendering. ByteDance says internal evaluations show the model&\#x27;s usability rate in film/TV and office scenarios is more than double that of the previous version, and it is rolling out across Jimeng, Doubao, Doubao Work, and the Volcano Ark platform. Most image models treat editing as a short, lossy loop where quality degrades after a few passes, so demos that sustain 100 rounds matter for real production workflows such as storyboarding, key art, and marketing assets. Native transparency removes a manual cutout step that has long blocked designers from dropping generated assets straight into layered design and video pipelines, and the accompanying price cut on Volcano Ark makes ByteDance&\#x27;s offering more competitive against rival image APIs. According to Volcano Engine, the model went live on Volcano Ark on November 9 with pixel-level editing, multi-round consistency, and native RGBA transparent output, and billing is by input/output images with text tokens free — a 2K square edit costs ¥0.28, roughly 60% cheaper and 40% faster than before. ByteDance has not published benchmarks, a technical report, or detail on how identity and layout consistency are maintained across 100 edit steps, and the rollout to consumer apps is described as gradual.

telegram · zaihuapd · Nov 9, 08:34

**Background**: Seedream is the image generation model family from ByteDance&\#x27;s Seed team, and its previous major version, Seedream 4.0, unified text-to-image generation and instruction-based editing in a single model. Jimeng \(即梦\) is ByteDance&\#x27;s AI creation app for images and video, Doubao \(豆包\) is its consumer AI assistant, and Volcano Ark \(火山方舟\) is the company&\#x27;s model-as-a-service platform through which developers and enterprises call these models via API. An alpha channel is the transparency layer in formats like PNG, and image models have historically output only opaque images, forcing designers to cut subjects out by hand before compositing them.

<details><summary>References</summary>
<ul>
<li><a href="https://seedream.ai/seedream-5">Seedream 5 | AI Image Generator Online Free | Seedream .ai</a></li>

</ul>
</details>

**Tags**: `#image-generation`, `#ByteDance`, `#Seedream`, `#generative-ai`, `#image-editing`

---

<a id="item-5"></a>
## [OPPO, vivo, Xiaomi and Honor launch joint ADV developer verification for Android sideloading](https://mp.weixin.qq.com/s/ZiKBASSLzvsZ6WR2AUmFeg) ⭐️ 7.0/10

OPPO, vivo, Xiaomi and Honor jointly rolled out an ADV \(developer identity verification\) mechanism for Android sideloaded apps in mainland China, with each vendor recognizing verification results issued by the other three. Apps already registered and published on the four vendors&\#x27; open platforms are submitted for verification automatically, while apps that fail verification trigger an &quot;unverified&quot; warning at install time that users must manually dismiss to continue. The four vendors together account for a large majority of Android phones sold in mainland China, so an interoperable verification standard can meaningfully reduce the spread of repackaged or impersonating apps while adding friction to unverified sideloading. It also gives developers a single identity relationship that works across the major Chinese app stores, which matters for anyone distributing apps into China. Verification is not an outright block: unverified apps can still be installed after the user confirms the warning, and developers with apps already listed on the four open platforms need to do nothing extra because submission is automatic. The scope is limited to mainland China and to the four participating OEMs, so apps distributed through other channels or on other brands&\#x27; devices are unaffected for now.

telegram · zaihuapd · Nov 9, 11:44

**Background**: Sideloading means installing an Android app from outside an official app store, which historically required no identity check and made it easy to distribute tampered or impersonated builds. Google announced its own Android Developer Verification program in August 2025, under which only apps with verified developer identities will be installable on certified devices starting in 2026, with an &quot;advanced flow&quot; for sideloading. Because Google services and Play are largely absent in mainland China, Chinese OEMs run their own stores and have pursued a parallel, locally governed verification scheme through their joint mobile terminal ecosystem alliance.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2025/08/google-will-block-sideloading-of-unverified-android-apps-starting-next-year/">Google will block sideloading of unverified Android apps starting next...</a></li>
<li><a href="https://android.gadgethacks.com/news/how-android-sideloading-verification-rules-affect-f-droid-and-privacy-tools/">How Android Sideloading Verification Rules Affect... :: Gadget Hacks</a></li>

</ul>
</details>

**Tags**: `#Android`, `#sideloading`, `#app-security`, `#China-tech`, `#mobile-ecosystem`

---

<a id="item-6"></a>
## [Leaked EU Digital Fairness Act draft targets addictive design and in-game virtual currency](https://www.mlex.com/mlex/articles/2546584/digital-businesses-face-addictive-design-controls-under-draft-eu-consumer-law) ⭐️ 7.0/10

A leaked draft of the EU&\#x27;s Digital Fairness Act would require digital firms to let users switch off features that push compulsive or excessive use, such as autoplay and streak rewards, and would impose rules on subscriptions including cancellation buttons, renewal reminders and access to human customer service. It would also ban paid loot boxes, pay-to-win mechanics and profiling-based advertising aimed at minors, require in-game virtual currencies to display their real-currency value, and allow fines of up to 6% of global turnover; the European Commission is due to table the proposal on November 11 alongside a reform of the Consumer Protection Cooperation framework. This would be one of the first laws to regulate product design itself rather than just disclosures, directly touching monetization mechanics used across free-to-play games, subscription apps and consumer platforms. Because penalties scale to global turnover, compliance would matter for any company shipping consumer digital products in the EU, not just European firms. The draft also requires explicit user consent before a free trial converts into a paid subscription, and treats minors&\#x27; exposure to paid random-reward mechanics and targeted advertising as a distinct harm to be prohibited. The text is still only a proposal: both the European Parliament and EU member-state governments must agree before it can take effect, so the final scope and timing remain open.

telegram · zaihuapd · Nov 9, 16:42

**Background**: The draft builds on the EU&\#x27;s existing concerns about &quot;dark patterns&quot; — interface designs deliberately crafted to nudge or trick users into purchases, sign-ups or continued use. Paid loot boxes, a monetization model in which players buy randomised virtual items, have drawn particular scrutiny for their resemblance to gambling and their popularity among younger players, while &quot;pay-to-win&quot; describes free-to-play games where spending money buys competitive advantage. Mandating real-currency labels for virtual currency is meant to make it harder for players to lose track of how much real money they are spending on in-game purchases.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_pattern">Dark pattern</a></li>
<li><a href="https://en.wikipedia.org/wiki/Loot_box">Loot box</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pay-to-win">Pay-to-win</a></li>

</ul>
</details>

**Tags**: `#EU regulation`, `#consumer protection`, `#dark patterns`, `#game monetization`, `#tech policy`

---

<a id="item-7"></a>
## [Epoch AI: Six Chinese AI Firms Earn About One-Tenth of OpenAI and Anthropic Revenue](https://cn.nikkei.com/china/ccompany/64644-2026-11-09-10-14-47.html) ⭐️ 6.0/10

Epoch AI published an estimate putting OpenAI and Anthropic&\#x27;s combined AI-related annualized revenue at roughly $105 billion, while six leading Chinese AI firms — ByteDance, Alibaba/Qwen, Zhipu/GLM, Moonshot/Kimi, DeepSeek and MiniMax — together earn about $11 billion, or 10.5% of that figure. ByteDance accounted for the largest share on the Chinese side at approximately $4 billion in annualized revenue. The gap quantifies a split between usage and monetization: Chinese models are widely adopted because they are open-source and aggressively priced, but that strategy currently converts into far less revenue than the closed, subscription- and API-driven models of OpenAI and Anthropic. This has implications for how much capital Chinese labs can recycle into compute and talent, and for how the global AI market fragments along price and licensing lines. The figures are Epoch AI estimates drawn from data across different months and expressed as annualized revenue, so they are approximations rather than audited financials. The report also uses OpenRouter usage as a proxy for distribution: 75% of GLM-5 calls and about 70% of DeepSeek V4 Pro calls on the platform come from third-party providers rather than the model developers themselves, suggesting value is being captured by downstream resellers.

telegram · zaihuapd · Nov 9, 03:12

**Background**: Epoch AI is a nonprofit research institute founded in 2022 that studies the trajectory of AI through quantitative analysis of compute, data, algorithms and economics, and its estimates are widely cited by researchers and policymakers. OpenRouter is a US-based routing service that provides a single API for accessing many large language models, which makes its traffic a useful public proxy for real-world developer usage across vendors. GLM-5 is Zhipu AI&\#x27;s flagship mixture-of-experts foundation model with roughly 745 billion total parameters, representative of the strong Chinese open-weight models that can be resold and self-hosted by third parties.

<details><summary>References</summary>
<ul>
<li><a href="https://aiwiki.ai/wiki/epoch_ai">Epoch AI | AI Wiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter - Wikipedia</a></li>
<li><a href="https://glm5.ai/">GLM - 5 - Zhipu AI&#x27;s Flagship Foundation Model</a></li>

</ul>
</details>

**Tags**: `#AI industry`, `#China AI`, `#market analysis`, `#open-source LLM`, `#revenue`

---

<a id="item-8"></a>
## [BYD Debuts Robotic Flash-Charging Arm in the UAE](https://m.mydrivers.com/newsview/1164193.html) ⭐️ 6.0/10

BYD unveiled a robotic flash-charging arm in the UAE that automatically opens the charging port, grabs and inserts the connector, charges, then unplugs and closes the flap, letting drivers simply park and walk away. The demonstration showcased charging power of up to 1000 kW and, paired with BYD&\#x27;s second-generation Blade battery, claims of 5 minutes of rapid replenishment and a full charge in 9 minutes. The demo combines ultra-high-power charging with robotic automation, pointing toward a future where charging stations work more like self-service car washes with no human handling of cables, which matters for fleet operators, ride-hailing services and drivers who value convenience. It also signals BYD is exporting not just vehicles but a full charging-and-energy ecosystem to overseas markets like the Middle East. The site uses an integrated solar-storage-charging \(PV + battery storage + charger\) architecture and demonstrated a &quot;one-tap park-and-charge&quot; function in which the vehicle drives itself into the bay before the arm takes over. The 1000 kW peak and the 5-minute/9-minute figures are BYD&\#x27;s own demonstration claims and depend on the second-generation Blade battery plus ideal conditions, so real-world results will vary with state of charge, temperature and grid capacity.

telegram · zaihuapd · Nov 9, 05:20

**Background**: Blade battery is BYD&\#x27;s trademark cell-to-pack design, in which long, thin lithium iron phosphate \(LFP\) cells are arranged directly into the pack structure, improving safety and space efficiency; the second generation is positioned around much faster charging, with BYD citing capabilities such as 5-minute top-ups and only about 3 extra minutes needed at -30°C. &quot;Solar-storage-charging integration&quot; means a site pairs photovoltaic panels, a battery energy storage system and chargers under one energy management system, so stored solar power buffers the enormous demand spikes of ultra-fast charging and reduces strain on the local grid. A 1000 kW charger delivers roughly ten times the power of a typical 100 kW public fast charger, which is why robotic arms are attractive: the liquid-cooled cables involved are heavy and awkward for people to handle.

<details><summary>References</summary>
<ul>
<li><a href="https://post.smzdm.com/p/a03kg4g9/">post.smzdm.com/p/a03kg4g9</a></li>
<li><a href="https://m.elecfans.com/article/6440396.html">什么是 光 伏+ 储 能+ 充 电 桩 一 体 化 ， 光 储 充 一 站 式解决 方 案 - 电 子发烧友网</a></li>

</ul>
</details>

**Tags**: `#BYD`, `#EV charging`, `#robotics`, `#energy storage`, `#automotive tech`

---

<a id="item-9"></a>
## [SnowLuma goes private after Tencent cease-and-desist letter](https://telegram.me/zaihuapd/45023) ⭐️ 6.0/10

SnowLuma, an unofficial framework that bridges QQ&\#x27;s native NTQQ sessions to the OneBot v11 protocol, announced it will switch from public to private on November 9, 2026 after receiving a cease-and-desist letter from Tencent, and bid farewell to its users. The shutdown removes one of the more actively developed bridges between QQ and the OneBot ecosystem, forcing bot and AI-agent developers who relied on it to migrate or find alternatives. It also reinforces a familiar pattern in which unofficial protocol implementations live under constant legal risk from the platform they reverse-engineer. SnowLuma describes itself as a high-performance remote protocol framework that injects native logic into QQ processes and intercepts network traffic to expose a structured API. Its own user agreement already stated it has no affiliation with or authorization from Tencent, and warned that such unofficial protocol tools may violate platform terms and put accounts at risk.

telegram · zaihuapd · Nov 9, 14:57

**Background**: OneBot v11 is a widely used open standard that lets chatbot frameworks such as NoneBot talk to various chat platforms through a common HTTP/WebSocket interface. Because QQ has no official implementation of that standard, third-party projects like SnowLuma reverse-engineer the QQ client — in this case the newer NTQQ protocol — to translate its sessions into OneBot events, so bots written against OneBot can run on QQ without modification. This makes such bridges popular among hobbyists building chatbots and AI assistants, but also puts them at odds with Tencent&\#x27;s platform rules.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/SnowLuma/SnowLuma">GitHub - SnowLuma / SnowLuma : Next Remote Protocol Framework.</a></li>
<li><a href="https://deepwiki.com/SnowLuma/SnowLuma">SnowLuma / SnowLuma | DeepWiki</a></li>
<li><a href="https://onebots.pages.dev/protocol/onebot-v11/">OneBot V 11 协 议 - onebots</a></li>

</ul>
</details>

**Tags**: `#QQ`, `#OneBot`, `#chatbots`, `#legal-takedown`, `#reverse-engineering`

---