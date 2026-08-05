---
layout: default
title: "Horizon Summary: 2026-08-05 (EN)"
date: 2026-08-05
lang: en
report: default
---

> From 281 items, 13 important content pieces were selected

---

1. [ChainDrop Worm Breaches Over 1,300 npm Packages](#item-1) ⭐️ 9.0/10
2. [SpaceX Commits Exclusively to Nvidia AI Architecture](#item-2) ⭐️ 8.0/10
3. [ByteDance Launches SeedRealtime, Native Full-Duplex Audio-Video Model for Doubao](#item-3) ⭐️ 8.0/10
4. [Unitree&\#x27;s STAR Market IPO Enters Inquiry Phase](#item-4) ⭐️ 8.0/10
5. [FFmpeg 9.0 Released with Animated WebP, Vulkan Filters, and AI-Assisted Development](#item-5) ⭐️ 8.0/10
6. [Exchanges Shut LAN Trading Lines; Nearby Data Center Rents Surge](#item-6) ⭐️ 8.0/10
7. [DeepSeek Restarts Second Funding Round at 500B Yuan Valuation](#item-7) ⭐️ 7.0/10
8. [Samsung and SK Hynix Test China&\#x27;s AMEC Chip Tools Amid US Export Controls](#item-8) ⭐️ 7.0/10
9. [Chinese Robot Vacuum Makers Grab 70% Global Market Share](#item-9) ⭐️ 7.0/10
10. [Oracle Cloud to Enforce Slimmer Always-Free Limits Starting August 18](#item-10) ⭐️ 6.0/10
11. [Coolapk Editor: Apple Never Sent Takedown Notices, Others Sent Tens of Thousands](#item-11) ⭐️ 6.0/10
12. [Beijing Engineer Gets 5 Years, 10 Months for Deleting 89 TB of AI Data](#item-12) ⭐️ 6.0/10
13. [Apple&\#x27;s Cost-Cut Push Fails as ChangXin Holds Firm on DRAM Prices](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [ChainDrop Worm Breaches Over 1,300 npm Packages](https://www.bleepingcomputer.com/news/security/massive-chaindrop-npm-supply-chain-attack-infects-hundreds-of-packages/) ⭐️ 9.0/10

A self-propagating worm named ChainDrop has compromised more than 1,300 npm packages, including popular cache libraries Keyv and Cacheable, with combined monthly downloads around 2 billion. The attack began after the Keyv maintainer&\#x27;s GitHub account was compromised, and malicious versions were published through legitimate GitHub Actions CI/CD workflows. This is a significant supply-chain attack because installing any poisoned package triggers credential theft and further package infection, affecting tens of thousands of downstream projects. Security teams must treat any system that installed affected versions as compromised and rotate tokens immediately to limit the worm&\#x27;s spread. The payload consists of a setup.mjs dropper and a Math\_Symbol.js credential stealer that execute automatically during npm install, harvesting GitHub, npm, AWS, and Kubernetes credentials. Researchers observed 444 packages and 2,212 poisoned versions within four hours starting from keyv@6.0.0; the npm-cache\[.\]com domain is a known indicator of compromise.

telegram · zaihuapd · Aug 5, 03:04

**Background**: npm is the default package manager for Node.js and one of the largest software registries in the world; packages are downloaded billions of times each month. In a software supply-chain attack, malicious code is injected into a trusted third-party component so that downstream users of that component are also infected. Worm-like attacks on package registries are especially dangerous because the malware can spread from one maintainer&\#x27;s packages to others through compromised credentials and automated build pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://www.stepsecurity.io/blog/chaindrop-npm-worm">ChainDrop npm Worm : Bun-loaded CI/CD credential... - StepSecurity</a></li>
<li><a href="https://suriq.io/blog/chaindrop-keyv-npm-worm-credential-theft">Self-spreading npm worm hits hundreds of packages, steals cloud and...</a></li>
<li><a href="https://www.csoonline.com/article/4205276/chaindrop-credential-stealing-worm-infects-over-400-npm-packages.html">ChainDrop credential stealing worm infects over 400 npm packages</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply-chain`, `#npm`, `#malware`, `#credential-theft`

---

<a id="item-2"></a>
## [SpaceX Commits Exclusively to Nvidia AI Architecture](https://wccftech.com/elon-musk-commits-spacex-exclusively-to-nvidia-gpus-citing-theyre-the-best/) ⭐️ 8.0/10

On August 4, Elon Musk announced during SpaceX&\#x27;s first earnings call that the company will exclusively use Nvidia AI systems, calling the Vera Rubin architecture the best AI computing architecture. SpaceX will deploy Nvidia Vera Rubin NVL72 racks in global ground data centers and in space, targeting over 2 gigawatts of AI compute by the end of the year and nearly 10 gigawatts by the end of 2027. This exclusive partnership positions Nvidia as the core AI compute provider for both terrestrial and orbital data centers, strengthening its dominance in the AI infrastructure market. It also signals a major step toward practical space-based AI computing, which could reduce energy and water use by leveraging solar power in orbit. The AI systems will support SpaceX&\#x27;s Starmind satellite project, with satellite launches expected to start next year to build orbital AI data centers. Nvidia has also introduced the Space-1 Vera Rubin module, designed for high-performance AI inference on satellites and in-orbit vehicles.

telegram · zaihuapd · Aug 5, 02:04

**Background**: Nvidia&\#x27;s Vera Rubin platform is a next-generation AI supercomputing architecture built for AI factory scale; the Vera Rubin NVL72 rack offers training with one-fourth the GPUs and inference at one-tenth the cost per million tokens versus Blackwell. Starmind is SpaceX&\#x27;s orbital computing network concept, potentially involving up to a million AI satellites powered by solar energy and connected to Earth via high-bandwidth laser links. The Space-1 Vera Rubin module is specifically engineered for space environments and delivers up to 25 times the AI compute of an H100 for orbital data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">Rack-Scale Agentic AI Supercomputer | NVIDIA Vera Rubin NVL72</a></li>
<li><a href="https://www.spacex.com/spacexai/starmind">SpaceX - AI Satellite</a></li>
<li><a href="https://techstartups.com/2026/08/04/nvidia-partners-with-spacex-to-build-starmind-ai-orbital-data-centers-in-space/">Nvidia partners with SpaceX to build Starmind AI orbital data ...</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#SpaceX`, `#Nvidia`, `#Space Computing`, `#AI`

---

<a id="item-3"></a>
## [ByteDance Launches SeedRealtime, Native Full-Duplex Audio-Video Model for Doubao](https://seed.bytedance.com/zh/blog/seedrealtime-%E9%9F%B3%E8%A7%86%E9%A2%91%E5%85%A8%E5%8F%8C%E5%B7%A5%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%8F%91%E5%B8%83-%E8%B5%B0%E5%90%91%E5%85%A8%E6%A8%A1%E6%80%81%E8%87%AA%E7%84%B6%E4%BA%A4%E4%BA%92) ⭐️ 8.0/10

On August 5, ByteDance released SeedRealtime, a native audio-video full-duplex model integrated into Doubao. Instead of chaining ASR, VLM, and TTS modules, the model unifies perception, understanding, decision-making, and expression in one end-to-end architecture for real-time multimodal interaction. SeedRealtime reduces conversational turn-taking issues by half compared with cascaded systems, notably cutting interruptions such as being cut off mid-sentence. This marks a shift toward native full-duplex interaction in consumer AI assistants, potentially raising the bar for real-time multimodal conversation. The model can watch, listen, and speak simultaneously over continuous audio, video, and text streams, and supports joint audio-video understanding, active environmental perception, and natural conversational pacing. It also removes the need for a separate VAD \(voice activity detection\) module to determine turn-taking, because turn decisions are made within the unified model.

telegram · zaihuapd · Aug 5, 04:42

**Background**: Traditional voice AI systems are typically cascaded: automatic speech recognition \(ASR\), a vision-language model \(VLM\), and text-to-speech \(TTS\) are chained together, which introduces latency and information loss between stages. Full-duplex communication means both parties can send and receive simultaneously, as in natural human conversation. By building a native full-duplex model, ByteDance aims to make assistant interactions feel continuous rather than turn-based.

<details><summary>References</summary>
<ul>
<li><a href="https://www.testingcatalog.com/bytedance-launches-seedrealtime-full-duplex-ai-model/">ByteDance launches SeedRealtime full-duplex AI model</a></li>
<li><a href="https://technode.com/2026/08/05/bytedance-launches-seedrealtime-full-duplex-audio-video-model/">ByteDance launches SeedRealtime full-duplex audio-video model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Duplex_%28telecommunications%29">Duplex (telecommunications) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#multimodal`, `#real-time conversation`, `#ByteDance`, `#full-duplex model`

---

<a id="item-4"></a>
## [Unitree&\#x27;s STAR Market IPO Enters Inquiry Phase](https://m.jrj.com.cn/madapter/stock/2026/08/05141758022724.shtml) ⭐️ 8.0/10

On August 5, 2026, Unitree Technology launched the preliminary inquiry for its STAR Market IPO, planning to raise 4.202 billion RMB by issuing 40.4464 million new shares \(10% of post-issuance total\). The expected issue price is about 104 RMB per share, implying a market valuation exceeding 40 billion RMB. This is a landmark IPO for a leading Chinese humanoid robotics company, giving investors a rare public-market entry into the rapidly growing embodied AI and robotics sector. A successful listing would provide significant capital for R&amp;D and mass production, further cementing China&\#x27;s STAR Market as a key venue for hard-tech financing. Unitree reported 2025 revenue of 1.699 billion RMB and net profit of 278 million RMB, and projects 2026 H1 revenue of 1.052 to 1.128 billion RMB, up 35.62% to 45.41% year-over-year. Online and offline subscription begins August 10, with the payment deadline on August 12.

telegram · zaihuapd · Aug 5, 07:40

**Background**: The STAR Market, launched in 2019, is China&\#x27;s NASDAQ-style board for technology and innovation enterprises, allowing listings with more flexible conditions. Unitree is well known for its quadruped and humanoid robots, such as the H1 and G1 series, and is a core player in China&\#x27;s embodied AI ecosystem. This IPO will help fund humanoid robot mass production and global expansion.

**Tags**: `#IPO`, `#robotics`, `#Unitree`, `#STAR Market`, `#funding`

---

<a id="item-5"></a>
## [FFmpeg 9.0 Released with Animated WebP, Vulkan Filters, and AI-Assisted Development](https://news.ycombinator.com/item?id=49166202) ⭐️ 8.0/10

FFmpeg 9.0 was released on August 3, 2026, introducing an animated WebP decoder and demuxer, the GPU-accelerated v360\_vulkan filter, a Playdate video encoder/muxer, HE-AAC 960 decoding, and an ONNX Runtime DNN backend. The development team also received six months of free Claude Max access from Anthropic&\#x27;s Claude for Open Source Program, using AI to help locate missing backports. This major release significantly expands FFmpeg&\#x27;s capabilities, notably adding GPU-accelerated 360-degree video processing and AI inference via ONNX Runtime, which benefits VR/immersive workflows and modern hardware. It also marks an interesting milestone in open-source development where AI tools like Claude are being integrated into the maintainer process. Animated WebP support is implemented as a decoder and demuxer, while the v360\_vulkan filter converts 360-degree spherical projections entirely on the GPU, improving performance over the CPU-only v360 filter. The Playdate encoder produces PDV format for the handheld device&\#x27;s 1-bit 400x240 display, and the ONNX Runtime backend was contributed by AMD to enhance AI model execution in the DNN filter.

telegram · zaihuapd · Aug 5, 10:32

**Background**: FFmpeg is a widely used open-source multimedia framework for decoding, encoding, transcoding, and streaming files. This 9.0 release marks the first major version since FFmpeg 8.1 &quot;Hoare&quot;, roughly five months earlier, and adds several hardware-acceleration and AI-related features. The Claude for Open Source Program provides free access to Anthropic&\#x27;s AI assistant for qualifying open-source projects, with the FFmpeg team using it to identify missing backports rather than writing code directly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/FFmpeg-9.0-Released">FFmpeg 9.0 Released With More Vulkan Acceleration... - Phoronix</a></li>
<li><a href="https://ubuntuhandbook.org/index.php/2026/08/ffmpeg-9-0-new-decoders-ubuntu-ppa/">FFmpeg 9.0 Released with New GPU Accelerated... | UbuntuHandbook</a></li>
<li><a href="https://thelinuxcamp.com/news/amd-introduces-onnx-runtime-backend-for-ffmpeg-s-dnn-filter-mqte6kmz">AMD Introduces ONNX Runtime Backend for FFmpeg &#x27;s DNN Filter</a></li>

</ul>
</details>

**Discussion**: Some community members expressed concerns about the safety review process for AI-assisted development, particularly how AI-generated contributions are vetted. The overall sentiment appears positive about the new features, but the AI usage in the project workflow remains a point of debate.

**Tags**: `#FFmpeg`, `#release`, `#multimedia`, `#AI`, `#open source`

---

<a id="item-6"></a>
## [Exchanges Shut LAN Trading Lines; Nearby Data Center Rents Surge](https://mp.weixin.qq.com/s/lH2IAcm1uX33Hw1H_EfPDg) ⭐️ 8.0/10

As of the evening of July 31, the Shanghai, Shenzhen, and Beijing stock exchanges closed their in-building LAN trading and market-data lines, requiring institutions to connect exclusively via WAN with two-way latency of no less than 2ms and to move servers out of exchange data centers. Rents for standard 4kW financial racks in Jinqiao, Waigaoqiao, and Zhangjiang have since jumped from about 7,000 yuan at the start of the year to around 10,000 yuan per month, with some prime locations seeing quoted prices double. This regulatory change reshapes China&\#x27;s low-latency trading infrastructure and directly affects high-frequency trading \(HFT\) strategies, because under price-time priority, physical distance to the exchange&\#x27;s matching engine determines order execution speed. The resulting surge in colocation prices shows a tangible market impact, while quantitative funds say they will simply follow the brokers in choosing new server locations. Only a small number of ultra-high-frequency strategies truly depend on speed competition, according to industry observers. Financial-grade third-party racks near Jinqiao number only in the thousands, and limited supply has triggered a bidding war for the remaining colocation space.

telegram · zaihuapd · Aug 5, 14:44

**Background**: A matching engine is the core component of a securities exchange that pairs buy and sell orders, typically following price-time priority: higher-priced buy orders and lower-priced sell orders are matched first, and among orders at the same price, earlier orders execute first. Historically, institutions could place servers inside the exchange data center and connect over LAN to achieve extremely low latency; the new rules force them onto WAN links with a minimum 2ms two-way latency and require servers to be moved out of exchange premises. Colocating in nearby third-party data centers helps minimize network distance and latency, which is why rents in adjacent areas have surged. Financial-grade racks are designed with the power, cooling, security, and reliability specifications required by financial institutions.

<details><summary>References</summary>
<ul>
<li><a href="https://hihuo.com/books/exchange/02-%E6%92%AE%E5%90%88%E5%BC%95%E6%93%8E%E5%8E%9F%E7%90%86.html">撮合引擎原理 | HiHuo</a></li>
<li><a href="https://cloud.tencent.com/developer/article/1470996">交易所撮合引擎原理及实现代码 -腾讯云开发者社区-腾讯云 Images 撮合系统是什么？把&quot;买卖双方配对成成交&quot;的那台发动机到底做了什么 设计撮合引擎 - Java教程 - 廖雪峰的官方网站 交易撮合引擎原理与实现【含源码】-CSDN博客 【金融科技工程】撮合引擎实现：撮合算法、价格优先时间优先、状态机...</a></li>
<li><a href="https://m.21jingji.com/article/20260731/herald/e2a50bbcd7c19f408929228d2ff31bbc.html">交 易 所 今晚关停 局 域 网 行情通道，量化高频遇“减速带” - 21财经</a></li>

</ul>
</details>

**Tags**: `#trading infrastructure`, `#low latency`, `#exchanges`, `#regulatory change`, `#HFT`

---

<a id="item-7"></a>
## [DeepSeek Restarts Second Funding Round at 500B Yuan Valuation](https://finance.sina.com.cn/wm/2026-08-05/doc-inimfmyv1554159.shtml) ⭐️ 7.0/10

DeepSeek has restarted its second-round financing with a pre-money valuation of 500 billion yuan, aiming to raise 50 billion yuan, with signing expected in late August. The round was paused in late July after founder Liang Wenfeng was dissatisfied with a leaked meeting transcript. This significant capital raise underscores strong investor confidence in leading AI startups, potentially fueling DeepSeek&\#x27;s expansion and competitive position in the LLM industry. The 43% valuation increase from the first round signals rapid growth and market validation. The first round closed in June with 50 billion yuan raised at a valuation exceeding 350 billion yuan. If the second round completes, total funding across both rounds will exceed 100 billion yuan, though some institutions that had been actively engaged have not yet received restart notices.

telegram · zaihuapd · Aug 5, 02:46

**Background**: DeepSeek is a Chinese AI startup focused on developing large language models. Pre-money valuation refers to the company&\#x27;s value before receiving new investment. The pause and restart of the financing round highlight the sensitivity and caution surrounding high-profile AI investments.

**Tags**: `#DeepSeek`, `#AI funding`, `#startup valuation`, `#LLM industry`

---

<a id="item-8"></a>
## [Samsung and SK Hynix Test China&\#x27;s AMEC Chip Tools Amid US Export Controls](https://www.reuters.com/world/china/samsung-sk-hynix-test-chinese-chip-tools-hedge-against-us-risks-2026-08-05/) ⭐️ 7.0/10

Reuters reports that Samsung Electronics and SK Hynix have been evaluating etching tools from Chinese supplier AMEC for their China fabs for about two years, as a hedge against tighter U.S. export controls. No decision on large-scale deployment has been made; Samsung denied the testing, while SK Hynix declined to comment. This marks a potential shift by major memory makers toward Chinese semiconductor equipment, which could reshape supply chains and validate China&\#x27;s domestic toolmakers. If adopted, it would be a strong endorsement for AMEC and could accelerate local substitution in China&\#x27;s roughly $28 billion wafer fab equipment market. AMEC has developed 54 types of high-end semiconductor equipment, including 26 plasma etching tools, and holds 1,200+ patents in etching technology. Chinese equipment is typically priced 20-30% lower than Western alternatives; Deutsche Bank forecasts domestic suppliers could take 25-30% of China&\#x27;s equipment market this year.

telegram · zaihuapd · Aug 5, 04:32

**Background**: The U.S. revoked the Validated End User status for Samsung and SK Hynix&\#x27;s China fabs in 2025, replacing it with annual licenses and raising concerns that maintenance of Western tools could be restricted. Etching equipment selectively removes material layers from silicon wafers and is a critical step in chip fabrication. Testing Chinese tools gives the Korean firms alternative options should export controls tighten further.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bis.doc.gov/index.php/documents/validated-end-user">Validated End User</a></li>
<li><a href="https://cnbizinsight.com/chinas-semiconductor-ip-barriers-patent-landscape-analysis-for-equipment-materials/">China Semiconductor IP Barriers: Equipment &amp; Materials Patent...</a></li>
<li><a href="https://technode.com/2026/08/03/chinas-amec-targets-more-than-100-high-end-semiconductor-equipment-types-within-five-years/">China’s AMEC targets more than 100 high-end semiconductor ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#supply chain`, `#export controls`, `#China`, `#chip equipment`

---

<a id="item-9"></a>
## [Chinese Robot Vacuum Makers Grab 70% Global Market Share](https://cn.nikkei.com/china/ccompany/63358-2026-08-05-08-31-00.html?start=0) ⭐️ 7.0/10

According to IDC, in the second half of 2025, five major Chinese manufacturers including Roborock and Ecovacs jointly held more than 70% of the global robot vacuum market. Roborock led with a 27% share and ranked first in the US, Germany, and South Korea, while iRobot filed for bankruptcy at the end of 2025. This marks a major power shift in a consumer robotics category once pioneered by iRobot. Chinese companies are winning not on price but on proprietary technology such as stair-climbing robots, reshaping the global smart home market. Roborock is developing the Saros Rover, unveiled at CES 2026 as the world&\#x27;s first robot vacuum with AI-powered wheel-leg architecture, designed to climb stairs and clean multi-level homes. Anker and DJI are also entering the category, while bankrupt iRobot has been acquired by a Chinese company.

telegram · zaihuapd · Aug 5, 11:32

**Background**: Robot vacuums are autonomous home cleaning devices that navigate and map rooms. For years iRobot&\#x27;s Roomba led the global market, but Chinese manufacturers like Roborock and Ecovacs gained an edge with advanced sensors, AI navigation, and features like self-emptying. Stair-climbing technology, shown at IFA 2025 by Eufy, Dreame, and MOVA and featured in Roborock&\#x27;s Saros Rover, is the next frontier for multi-floor homes.

<details><summary>References</summary>
<ul>
<li><a href="https://newsroom.roborock.com/gl/news/ces-2026-roborock-releases-the-world-s-first-robotic-vacuum-with-wheel-leg-architecture-as-it-joins-hands-with-real-madrid-football-club-">CES 2026: Roborock releases the world&#x27;s first robotic vacuum ...</a></li>
<li><a href="https://vacuumwars.com/the-rise-of-the-stair-climbing-robot-vacuum-ifa-2025/">The Rise of the Stair-Climbing Robot Vacuum: IFA 2025</a></li>
<li><a href="https://robohorizon.com/en-us/news/2026/01/roborock-saros-rover-the-robot-vacuum-that-finally-grew-legs/">Roborock Saros Rover: The Robot Vacuum That Finally … | …</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#smart home`, `#China tech`, `#market analysis`, `#consumer electronics`

---

<a id="item-10"></a>
## [Oracle Cloud to Enforce Slimmer Always-Free Limits Starting August 18](https://telegram.me/zaihuapd/42978) ⭐️ 6.0/10

Oracle Cloud has notified users that starting August 18, 2026, it will automatically terminate any Always Free compute instances exceeding the newly reduced limits of 2 Ampere A1 OCPUs and 12 GB of memory. This halves the previous allowance of 4 OCPUs and 24 GB. This policy change directly impacts users who provisioned free-tier instances under the old, larger allowance, potentially causing unexpected loss of services and data. It also signals that Oracle is tightening its free-tier offering, which may push affected users toward paid OCI services or rival clouds. The new Always Free compute limit is capped at 2 Ampere A1 OCPUs and 12 GB of memory, down from 4 OCPUs and 24 GB. Users must manually scale down their usage before August 18, 2026; after that date, Oracle will forcibly terminate any over-quota instances.

telegram · zaihuapd · Aug 4, 23:51

**Background**: Oracle Cloud&\#x27;s Always Free tier offers a set of resources that remain free for the lifetime of an account, including Arm-based Ampere A1 compute shapes. The Ampere A1 shapes use Ampere Altra processors, with OCPU standing for Oracle CPU, where one OCPU represents a single core. The reported change reduces the documented Ampere A1 allowance from 4 OCPUs and 24 GB to 2 OCPUs and 12 GB, affecting free-tier users who may have scaled up beyond the new limits.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm">Always Free Resources - Oracle</a></li>
<li><a href="https://linuxiac.com/oracle-quietly-cuts-free-tier-ampere-a1-resources-in-half/">Oracle Quietly Cuts Free Tier Ampere A1 Resources in Half</a></li>

</ul>
</details>

**Tags**: `#Oracle Cloud`, `#Free Tier`, `#Cloud Computing`, `#Policy Change`, `#Infrastructure`

---

<a id="item-11"></a>
## [Coolapk Editor: Apple Never Sent Takedown Notices, Others Sent Tens of Thousands](https://www.coolapk.com/feed/73075082?s=YmVlMmRhZjBiN2YxOWFnNmE3MmFmYjR6i1653) ⭐️ 6.0/10

In a recent Coolapk post, a platform editor claimed that over the years Coolapk has received an estimated tens of thousands of takedown requests from manufacturers, nearly one every day, and that Apple is the only company that never sent one. This anecdote highlights how aggressively some tech companies police negative reviews on community platforms, which can damage user trust and drive users to other brands. It also sets Apple apart as an outlier in its approach to handling online criticism. The editor said some manufacturers were so forceful that they attempted to &\#x27;gag&\#x27; users, forbidding any negative product mentions. The post advises users to express product flaws objectively and calmly, avoiding overly emotional language.

telegram · zaihuapd · Aug 5, 03:43

**Background**: Coolapk is a popular Chinese Android community and app store where users share apps, discuss products, and post reviews. A takedown letter \(下架函\) is a formal request from a company to a platform asking for content to be removed, often due to copyright or reputation concerns. Such requests are common in the tech industry as brands seek to manage their online image.

<details><summary>References</summary>
<ul>
<li><a href="https://appteka.store/apps/1d4r305924">Download CoolApk APK v16.5.1 for Android · Appteka</a></li>
<li><a href="https://www.baogaoting.com/files/%E4%B8%8B%E6%9E%B6%E5%87%BD.docx">baogaoting.com/files/ 下 架 函 .docx</a></li>

</ul>
</details>

**Tags**: `#content moderation`, `#tech industry`, `#censorship`, `#Coolapk`, `#Apple`

---

<a id="item-12"></a>
## [Beijing Engineer Gets 5 Years, 10 Months for Deleting 89 TB of AI Data](https://xinwen.bjd.com.cn/content/s6a728509e4b0e45f3fd5a25b.html) ⭐️ 6.0/10

Beijing&\#x27;s first criminal case for destroying an AI model system ended with an appeals court upholding the original verdict on June 26, 2026. Algorithm engineer Wang was sentenced to five years and ten months in prison plus a compensation order of over 204,000 yuan for deleting 89 TB of model and training data. This landmark ruling confirms that AI model training systems count as &\#x27;computer information systems&\#x27; under Chinese criminal law, extending criminal liability to the destruction of AI training data. The decision could reshape how tech companies protect their data assets and how employees handle data-management responsibilities. Wang ran deletion scripts for over 17 hours to free up storage for externally commissioned model training, which brought corporate R&amp;D projects to a standstill. The court also counted the labor and computing costs incurred during data recovery as part of the economic loss.

telegram · zaihuapd · Aug 5, 06:17

**Background**: Chinese criminal law criminalizes the destruction of computer information systems, but it was previously uncertain whether AI model systems fell within that definition. Prosecutors determined that because AI models and their training systems automatically process data, they qualify as &\#x27;computer information systems&\#x27; in the criminal sense. The case is significant because it treats AI training data as legally protected digital infrastructure and includes recovery expenses in the damage calculation.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E9%9D%9E%E6%B3%95%E5%88%A0%E9%99%A4%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83%E6%95%B0%E6%8D%AE%E6%A1%88/67654528">非法删除人工智能模型训练数据案_百度百科</a></li>
<li><a href="https://www.sohu.com/a/1059062485_479806">离谱！员工 17 小时删光公司 89TB AI 数据，成北京首例破坏 AI 模型刑...</a></li>
<li><a href="https://www.163.com/dy/article/JE8RU4FO05568RYX.html">163.com/dy/article/JE8RU4FO05568RYX.html</a></li>

</ul>
</details>

**Tags**: `#AI`, `#legal`, `#data-management`, `#cybercrime`, `#machine-learning`

---

<a id="item-13"></a>
## [Apple&\#x27;s Cost-Cut Push Fails as ChangXin Holds Firm on DRAM Prices](https://m.ddaily.co.kr/page/view/2026080513445474844) ⭐️ 6.0/10

Apple negotiated with Chinese memory maker ChangXin to supply mobile DRAM such as LPDDR5X at lower prices, but ChangXin refused to cut prices and quoted prices on par with or above Samsung and SK Hynix. This signals that Chinese memory makers no longer need Apple as a low-cost customer, and it strengthens Samsung and SK Hynix&\#x27;s pricing power in long-term contract negotiations. It may also force Apple to rethink its supply-chain strategy in a tightening DRAM market. ChangXin&\#x27;s leverage comes from large-volume purchases by domestic Chinese firms such as Huawei and Xiaomi, which are enough to absorb its capacity. Meanwhile, Samsung and SK Hynix are shifting production toward high-value AI memory like HBM, tightening supply of general-purpose DRAM.

telegram · zaihuapd · Aug 5, 08:27

**Background**: LPDDR5X is a low-power DRAM standard commonly used in smartphones and laptops. HBM is a 3D-stacked memory interface designed for high-bandwidth, high-performance computing and AI workloads. Because HBM offers higher margins, major makers allocate capacity to it, leaving less supply for conventional DRAM.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LPDDR">LPDDR - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://nemothia.com/lpddr5x-ai-inference-memory/">LPDDR 5 X Is AI&#x27;s New Inference Memory . The Shortage Came With It.</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#DRAM`, `#Apple`, `#supply-chain`, `#memory`

---