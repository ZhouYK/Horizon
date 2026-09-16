---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16 23:03:56 +0000
lang: en
report: default
---

> From 186 items, 6 important content pieces were selected

---

1. [1.7 Million Low-Quality Chinese Casino Sites Hide APT Attack Infrastructure](#item-1) ⭐️ 8.0/10
2. [Sina Cloud SAE shuts down permanently as Archive Team rescues Bilibili videos](#item-2) ⭐️ 8.0/10
3. [Micron Claims World&\#x27;s First 512GB DDR5 RDIMM, Targeting 2027 Production](#item-3) ⭐️ 8.0/10
4. [StepFun Releases StepAudio 3 Music: Full Songs from Natural Language](#item-4) ⭐️ 7.0/10
5. [WeChat 8.0.78 lets users forward chat records to ChatGPT](#item-5) ⭐️ 7.0/10
6. [Geekerwan: Apple&\#x27;s First 2nm Chip, A20 Pro, Debuts in iPhone 18 Pro](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [1.7 Million Low-Quality Chinese Casino Sites Hide APT Attack Infrastructure](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 8.0/10

A security firm has identified roughly 1.7 million low-quality Chinese-language casino and adult websites that masquerade as ordinary gambling or entertainment sites while actually serving as attack infrastructure, with some used for malware distribution and espionage. Since 2023, China-aligned APT groups have used a framework called PeckBirdy to hide malware command-and-control \(C2\) domains inside these poor-quality gambling sites and to trick users into downloading malicious programs through fake software updates. This reveals a novel detection-evasion technique: because the malicious traffic looks like ordinary gambling-site browsing, defenders may dismiss it as employee policy violations rather than an intrusion, allowing attackers to dwell undetected. It highlights how APT operators are industrializing the use of disposable, mass-registered websites as deniable infrastructure, which raises the bar for threat hunting and incident response. PeckBirdy is a JScript-based command-and-control framework that abuses legitimate built-in Windows binaries \(LOLBins\) so attacks blend into normal system activity, and it has been used against the gambling industry and Asian government entities across multiple environments. The volume of roughly 1.7 million casino sites means defenders face a very large, constantly shifting pool of domains to sift through, making signature-based blocking impractical.

telegram · zaihuapd · Sep 16, 07:31

**Background**: An advanced persistent threat \(APT\) is a stealthy, usually state-sponsored intrusion in which attackers gain access to a network and stay undetected for long periods, typically for espionage or disruption. Command-and-control \(C2\) infrastructure is the channel attackers use to send instructions to and receive data from compromised machines; hiding it behind innocuous-looking websites makes the traffic harder to flag. Low-quality gambling and adult sites are attractive cover because they are registered in bulk, change frequently, and any traffic to them is easily mistaken for non-work browsing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trendmicro.com/en/research/26/a/peckbirdy-script-framework.html">PeckBirdy: A Versatile Script Framework for LOLBins ...</a></li>
<li><a href="https://thehackernews.com/2026/01/china-linked-hackers-have-used.html">China-Linked Hackers Have Used the PeckBirdy JavaScript C2 ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_persistent_threat">Advanced persistent threat</a></li>

</ul>
</details>

**Tags**: `#网络安全`, `#APT`, `#恶意软件`, `#威胁情报`, `#C2基础设施`

---

<a id="item-2"></a>
## [Sina Cloud SAE shuts down permanently as Archive Team rescues Bilibili videos](https://tracker.archiveteam.org/sinavideo/#show-all) ⭐️ 8.0/10

Sina Cloud SAE, China&\#x27;s first PaaS platform, goes permanently offline at 24:00 on September 16, 2026, and all user data will be irreversibly deleted. About 420 TB of early Bilibili video source files still sat in its S3 buckets, and Archive Team&\#x27;s distributed rescue effort has already recovered roughly 680 TB, putting the project at 96.26% complete. This is a race against permanent data loss: once SAE&\#x27;s buckets are wiped, the early source files of Bilibili — a defining part of Chinese internet video culture — would be gone forever. It also marks the end of China&\#x27;s first public PaaS, showing how quickly early cloud platforms and the digital heritage hosted on them can vanish. The shutdown notice was sent to users on June 10, 2026, ending nearly 17 years of operation for a platform that once served close to a million developers. The rescue is a volunteer, distributed crawl coordinated through Archive Team&\#x27;s public tracker, and the reported ~680 TB recovered versus ~420 TB remaining reflects the scope of the buckets being mirrored, with 96.26% completion still leaving a non-trivial tail of data at risk.

telegram · zaihuapd · Sep 16, 15:00

**Background**: SAE \(Sina App Engine\) was launched in Alpha form on November 3, 2009, making it China&\#x27;s first public PaaS; it let developers deploy PHP apps with no server maintenance and provided distributed storage, MySQL, Memcache and cron services. Bilibili relied on that storage in its early years to hold video source files. Archive Team is a loose volunteer collective co-founded by Jason Scott in 2009 that rushes to copy content from online services facing shutdown, deletion or merger.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/SAE/73588">SAE（云计算平台）_百度百科 SinaAppEngine（SAE）– 免运维的云计算服务厂商 新浪云（SAE）宣布9月16日永久关停：国内首家PaaS平台17年历程落幕 sina - 首页- 新浪云计算企业服务 新浪云 - sinacloud.com SAE平台 - 百度百科</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive_Team">Archive Team - Wikipedia</a></li>
<li><a href="https://wiki.archiveteam.org/">Archiveteam</a></li>

</ul>
</details>

**Tags**: `#data-preservation`, `#cloud-computing`, `#internet-archive`, `#bilibili`, `#paas`

---

<a id="item-3"></a>
## [Micron Claims World&\#x27;s First 512GB DDR5 RDIMM, Targeting 2027 Production](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 8.0/10

Micron says it has demonstrated the world&\#x27;s first 512GB DDR5 RDIMM for servers, a module rated at up to 9200 MT/s that uses 3D-stacked DRAM chips and is being validated by AMD and Intel for future server platforms. Micron expects the part to be production-ready in 2027. Quadrupling the capacity of a single server memory module directly benefits memory-hungry workloads such as AI inference, large in-memory databases and virtualization, where per-socket memory capacity is often the limiting factor. The claim also signals that 3D-stacked DRAM, previously associated mainly with HBM, is moving toward mainstream server DIMMs. Micron says 24 of these modules can populate a system with 12 TB of memory, and that a single module draws 16W versus 44.2W for four 128GB modules — a reduction of more than 60%. The 2027 timeline means the part is not yet shipping, and Micron has not detailed pricing, DRAM process node, or how the 3D stacking is implemented.

telegram · zaihuapd · Sep 16, 16:15

**Background**: RDIMM \(registered DIMM\) is server memory that places a register between the DRAM chips and the memory controller, re-driving signals so a system can hold far more modules than unregistered memory would allow. MT/s \(megatransfers per second\) measures the effective data rate of DDR memory rather than clock frequency — DDR5-9200 would mean 9,200 million transfers per second. 3D-stacked DRAM bonds multiple DRAM dies vertically, typically using through-silicon vias, a technique popularized by HBM \(High Bandwidth Memory\); applying it to standard RDIMMs is what allows capacity to grow without simply adding more packages.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RDIMM">RDIMM</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.kingston.com/en/blog/pc-performance/mts-vs-mhz">MT/s vs MHz: A Better Measure for Memory Speed - Kingston ...</a></li>

</ul>
</details>

**Tags**: `#DDR5`, `#Micron`, `#Server Memory`, `#Hardware`, `#3D Stacking`

---

<a id="item-4"></a>
## [StepFun Releases StepAudio 3 Music: Full Songs from Natural Language](https://static.stepfun.com/blog/stepaudio3/music/) ⭐️ 7.0/10

StepFun has released StepAudio 3 Music, an AI music generation model that turns natural-language descriptions of style, vocals, emotion, instruments, key and tempo into complete 48 kHz stereo songs. According to the accompanying technical report, the system uses a Mixture-of-Experts autoregressive model that first drafts ABC notation as an intermediate arrangement plan \(ABC-COT\) before predicting music tokens. Music generation has become a crowded field, and StepAudio 3 Music claims state-of-the-art results on the Audiobox and MuQ-Similarity benchmarks while keeping the output controllable through plain language. If those claims hold up, it would make studio-quality, style-controllable songwriting available for short-video soundtracks, lyric-and-melody demos and game theme songs, directly competing with tools in the emerging text-to-music market. The pipeline combines an autoregressive \(AR\) stage with a Diffusion Transformer \(DiT\) stage, and the notable trick is the ABC-COT step: the model effectively writes sheet music as an arrangement plan so that harmony, rhythm and melodic structure are decided before audio tokens are generated. All reported benchmark numbers and quality claims come from the team&\#x27;s own technical report, so independent verification is still pending.

telegram · zaihuapd · Sep 16, 08:48

**Background**: ABC notation is a long-standing plain-text format for writing sheet music, widely used in folk-music archives; using it as an intermediate representation lets a language model plan musical structure explicitly rather than jumping straight from text to waveforms. In generative audio, autoregressive models excel at long, coherent sequences while diffusion models are strong at high-fidelity detail, so AR + DiT hybrids have become a popular recipe for producing multi-minute songs. Audiobox is Meta&\#x27;s audio generation and evaluation framework, and MuQ-Similarity is a metric derived from MuQ, a self-supervised music encoder from Tencent AI Lab built on Mel-RVQ tokenization and a Conformer architecture, used to judge how faithfully generated music matches a reference.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/stepaudio-3-music-drafts-abc-notation-before-530-tracks">StepAudio 3 Music drafts ABC notation before 5:30 tracks</a></li>
<li><a href="https://github.com/tencent-ailab/MuQ">GitHub - tencent-ailab/MuQ: Official repository of the paper ...</a></li>
<li><a href="https://github.com/multimodal-art-projection/YuE">GitHub - multimodal-art-projection/YuE: YuE2: frontier music ...</a></li>

</ul>
</details>

**Tags**: `#AI music generation`, `#generative audio`, `#MoE`, `#diffusion models`, `#StepFun`

---

<a id="item-5"></a>
## [WeChat 8.0.78 lets users forward chat records to ChatGPT](https://www.chaincatcher.com/article/2290109) ⭐️ 7.0/10

After upgrading mobile WeChat to version 8.0.78, users can multi-select chat records and choose &quot;forward to other apps,&quot; which now includes the option to hand them directly to ChatGPT and other third-party apps via &quot;select an app on this phone&quot; — not just Tencent&\#x27;s own Yuanbao and WorkBuddy — with a maximum of 100 messages per transfer. WeChat packages the selected conversations into a ZIP archive containing a time-ordered TXT file plus any attachments, and desktop WeChat has opened a similar entry point. This effectively turns WeChat chat history into an exportable data source for AI assistants, so users can drop conversations straight into ChatGPT, Claude or similar tools for summarization and analysis without copy-pasting. Given WeChat&\#x27;s enormous user base, it is a high-impact step toward mainstream AI-integrated workflows, but it also pushes private chat content outside Tencent&\#x27;s own AI ecosystem and raises fresh data-sharing and privacy questions. Each transfer is capped at 100 messages, and the exported ZIP contains a chronologically organized TXT file plus attachments, meaning recipients get a plain-text record rather than a structured database. Community developers have already built relay or bridging tools on top of this entry point to feed chat records into ChatGPT and Claude, though the news does not specify any built-in consent flow for the other participants in a conversation.

telegram · zaihuapd · Sep 16, 14:15

**Background**: WeChat is Tencent&\#x27;s flagship messaging app and one of the most widely used communication platforms in China, where chat history is normally locked inside the app. Tencent previously limited the &quot;forward to other apps&quot; option to its own AI products: Yuanbao, an AI assistant powered by the Hunyuan model and tied into the WeChat ecosystem, and WorkBuddy, an AI office assistant that executes tasks on a user&\#x27;s computer from WeChat commands. This update extends that same forwarding path to third-party AI apps such as ChatGPT, which is significant because it is the first time mainstream WeChat users have a native way to export conversations to outside AI tools.

<details><summary>References</summary>
<ul>
<li><a href="https://apps.apple.com/hk/app/yuanbao-ai-assistant/id6480446430?l=en-GB">Yuanbao- AI Assistant - App Store - Apple</a></li>
<li><a href="https://www.codebuddy.cn/docs/workbuddy/WeixinBot-Guide">WorkBuddy ... | 腾讯云代码助手 CodeBuddy – AI 代码编辑器</a></li>

</ul>
</details>

**Tags**: `#wechat`, `#ai-integration`, `#privacy`, `#chatgpt`, `#product-update`

---

<a id="item-6"></a>
## [Geekerwan: Apple&\#x27;s First 2nm Chip, A20 Pro, Debuts in iPhone 18 Pro](https://www.bilibili.com/video/BV1oZeA6fERD) ⭐️ 6.0/10

Apple has launched the iPhone 18 Pro series carrying the A20 Pro, its first 2nm flagship chip, which packs a 6-core CPU with a 20% faster top core, a 7-core GPU that is 40% faster, and dual 16-core neural engines, plus 50% more memory bandwidth than the A19 Pro. The announcement also covers an in-house C2 modem delivering 50% faster uploads and 15% lower power draw, and Apple&\#x27;s first custom N1 wireless chip supporting Wi-Fi 7 and Bluetooth 6. This marks Apple&\#x27;s move to the 2nm generation and the first time its flagship phone silicon has been paired with a fully self-developed modem and wireless chip, a combination that could reduce Apple&\#x27;s dependence on outside suppliers and reset performance expectations for the mobile semiconductor race. If the claimed gains hold up in independent testing, they pressure Android rivals and other chipmakers to match the new node and packaging sooner than planned. Apple says the A20 Pro uses a new packaging design borrowed from its M-series Mac chips and is paired with a vapor chamber three times larger in area, for up to 40% better sustained performance than the previous generation. The figures come from a third-party Geekerwan summary rather than independent benchmarks, and it includes no pricing, battery-life, or thermal-throttling test data.

telegram · zaihuapd · Sep 16, 13:24

**Background**: The &quot;2nm&quot; label refers to the next leading-edge chip manufacturing node after 3nm, which shrinks transistor dimensions to pack more logic onto a die while typically improving power efficiency. A vapor chamber \(VC\) is a flat heat-spreader that moves heat through a liquid-to-vapor phase change, and Apple&\#x27;s recent silicon efforts include bringing modem design in-house, with the C1 as its first-generation cellular modem and the C2 as its second. Geekerwan is a well-known Chinese hardware-review channel whose teardowns and benchmarks are widely cited in the tech community.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/705922476">你知道VC均热板是什么吗？ - 知乎</a></li>
<li><a href="https://www.wanji.org/ping-guo-you-yi-zhong-bang-xin-pin-pu-guang-you-6-da-sheng-ji/">苹 果 又一重磅新品曝光，有 6 大升级 | 玩机网 - 苹 果 的新闻和传言</a></li>
<li><a href="https://tech.tom.com/202602/1439212339.html">果 粉狂欢！ 苹 果 三大产品 线 即将更新_TOM科技</a></li>

</ul>
</details>

**Tags**: `#apple`, `#semiconductor`, `#mobile-chips`, `#hardware`, `#2nm`

---