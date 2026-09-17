---
layout: default
title: "Horizon Summary: 2026-09-17 (EN)"
date: 2026-09-17 23:03:45 +0000
lang: en
report: default
---

> From 186 items, 7 important content pieces were selected

---

1. [MiMo-V2.6 Enters Large-Scale RL Training, Details to Be Open-Sourced](#item-1) ⭐️ 7.0/10
2. [GLM&\#x27;s Infra Agent Builds Its Own Inference Stack on 100k+ Accelerators](#item-2) ⭐️ 7.0/10
3. [Apple Reportedly Weighs Nvidia-Powered AI Servers for 2029](#item-3) ⭐️ 6.0/10
4. [PS5 Linux Dev Quits After LLM-Assisted &\#x27;Slop Kiddies&\#x27; Report Hypervisor Exploit to Sony](#item-4) ⭐️ 6.0/10
5. [Kimi Launches Finance-Specific AI, Deployed at ICBC and CITIC Securities](#item-5) ⭐️ 6.0/10
6. [BYD Plans Four European Plants to Localize EV Production](#item-6) ⭐️ 6.0/10
7. [Apple M5 Ultra benchmark leak: Metal score tops RTX 5090](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [MiMo-V2.6 Enters Large-Scale RL Training, Details to Be Open-Sourced](https://x.com/_LuoFuli/status/2100296686719610932) ⭐️ 7.0/10

Fuli Luo, who leads Xiaomi&\#x27;s MiMo team, announced on X that after nearly half a year of research the team is running large-scale reinforcement learning training on MiMo-V2.6, scaling up three dimensions simultaneously: compute \(roughly 2 billion tokens per step\), environments \(multi-task agentic RL\), and judge compute. She said the technical details will be open-sourced in the coming weeks. It signals that a hardware vendor&\#x27;s model team is investing seriously in RL post-training scaled along compute, environment diversity, and reward-model compute — the same axes that frontier labs treat as the current bottleneck for agentic capability. If the recipes are actually open-sourced, it would give the open-source community a rare look at production-grade multi-task agentic RL rather than just benchmark numbers. The disclosed scale figure is about 2 billion tokens per RL step, and the training is described as multi-task agentic RL, meaning the model is trained across several agent environments rather than one. Notably absent are concrete benchmark results, model size, training duration, or a release date — this is a progress teaser, and the promise of open-sourced details is still only a promise.

telegram · zaihuapd · Sep 17, 01:52

**Background**: MiMo is Xiaomi&\#x27;s in-house large language model series; the previous MiMo-V2.5 release emphasized agency and multimodality, and was accompanied by a TTS model series. Reinforcement learning post-training — where a model generates outputs, receives a reward signal, and is updated toward higher-reward behavior — has become the standard way to sharpen reasoning and agentic skills after pretraining. &quot;Judge compute&quot; refers to the compute spent on the evaluator models in an LLM-as-a-judge setup, which scores the model&\#x27;s outputs; scaling this judge is one way to make reward signals more reliable for hard tasks such as code correctness or multi-step planning.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/">mimo .xiaomi.com</a></li>
<li><a href="https://github.com/THUDM/AgentRL">GitHub - THUDM/AgentRL: Scaling Agentic Reinforcement Learning ...</a></li>
<li><a href="https://deepwiki.com/llm-as-a-judge/Awesome-LLM-as-a-judge/1.2-thinking-llm-as-a-judge:-test-time-scaling">Thinking LLM-as-a-Judge: Test-Time Scaling | llm-as-a-judge ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Reinforcement Learning`, `#Agentic AI`, `#Open Source`, `#MiMo`

---

<a id="item-2"></a>
## [GLM&\#x27;s Infra Agent Builds Its Own Inference Stack on 100k+ Accelerators](https://z.ai/blog/glm-built-its-inference-infrastructure) ⭐️ 7.0/10

GLM \(Z.ai\) announced that its production inference service for GLM-5.3-Flash has been deployed across more than 100,000 domestic Chinese AI accelerators, largely built with the help of an Infra Agent powered by GLM-5.3. The team says the system went from model adaptation to launch in under two weeks and delivered roughly a 3x end-to-end throughput improvement. This is a notable industry claim that an LLM-driven agent can help engineer the very infrastructure it runs on, a practical step toward the long-discussed idea of recursive self-improvement. If reproducible, it could reshape how large-scale inference clusters are built and optimized, and it highlights the growing maturity of China&\#x27;s domestic AI accelerator ecosystem. The team claims it established a &quot;dense feedback&quot; loop using layered testing, logging, tracing, and benchmarking so the agent could continuously localize problems and refine code. Crucially, GLM explicitly caveats that this does not yet amount to recursive self-improvement, and the announcement is a corporate blog post offering limited technical depth on how the agent actually worked.

telegram · zaihuapd · Sep 17, 08:38

**Background**: Recursive self-improvement \(RSI\) is a hypothesized process in which an AI system rewrites its own code to iteratively boost its own capabilities, potentially leading to an intelligence explosion; numerous attempts have been made but none have shown such a runaway effect. AI inference serving refers to the infrastructure that hosts trained models and exposes them as low-latency APIs, typically requiring efficient GPU/accelerator scheduling and kernel optimization. &quot;Domestic AI accelerators&quot; here means China-made AI chips, a response to export restrictions on advanced foreign hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://vc.ru/ai/3143789-z-ai-optimizirovala-infrastrukturu-inference-s-pomoshchyu-glm-5-3">Z.ai раскрыла, как GLM -5.3 участвовала... — AI на vc.ru</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#LLM agents`, `#inference serving`, `#self-improvement`, `#AI accelerators`

---

<a id="item-3"></a>
## [Apple Reportedly Weighs Nvidia-Powered AI Servers for 2029](https://www.reuters.com/technology/apple-considers-nvidia-tech-return-server-market-information-reports-2026-09-16/) ⭐️ 6.0/10

According to a report by The Information, Apple is considering re-entering the enterprise server market with AI servers built around its own M8 Ultra chip, and may adopt Nvidia&\#x27;s NVLink Fusion interconnect technology. The servers are said to come in two-chip and four-chip configurations aimed at AI developers, enterprises, and government customers, with an earliest launch around 2029. If it happens, this would be Apple&\#x27;s first dedicated server hardware since it discontinued the Xserve in 2011, marking a significant strategic shift toward enterprise AI infrastructure. The potential use of Nvidia interconnect technology would also signal a notable thaw in the historically tense relationship between Apple and Nvidia, and could give Apple a foothold in the fast-growing rack-scale AI compute market. The project is still speculative and could be cancelled, or Apple could drop the Nvidia technology entirely. The M8 Ultra is expected to be Apple&\#x27;s first chip built on a 1.4nm process, per Bloomberg&\#x27;s reporting on Apple&\#x27;s silicon roadmap, and NVLink Fusion would let Apple&\#x27;s custom silicon link into Nvidia&\#x27;s rack-scale architecture rather than remaining a closed, Apple-only system.

telegram · zaihuapd · Sep 17, 02:40

**Background**: Nvidia introduced NVLink Fusion in 2025 as a way to break from its practice of keeping its proprietary NVLink interconnect closed inside its own products, allowing customers to integrate third-party CPUs and custom accelerators into Nvidia&\#x27;s rack-scale AI systems. Apple&\#x27;s only prior foray into purpose-built servers was the Xserve, introduced in 2002 with PowerPC G4 chips and later moving to PowerPC G5 and Intel Xeon processors before being discontinued in 2011. Apple has since relied on Mac hardware and cloud partners for its own infrastructure, so a return to selling servers would be a major departure.

<details><summary>References</summary>
<ul>
<li><a href="https://m.guancha.cn/CaiJing/2026_09_17_900978.shtml">苹果要造服务器，还要用 英 伟 达 的 NVLink ？ -观察者网</a></li>
<li><a href="https://developer-nvidia-cn.nproxy.org/blog/integrating-custom-compute-into-rack-scale-architecture-with-nvidia-nvlink-fusion">借助 NVIDIA NVLink Fusion 将半定制计算平台集成到机架级架构</a></li>
<li><a href="https://zh.wikipedia.org/wiki/Xserve">Xserve - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#NVIDIA`, `#AI Servers`, `#Hardware`, `#Industry News`

---

<a id="item-4"></a>
## [PS5 Linux Dev Quits After LLM-Assisted &\#x27;Slop Kiddies&\#x27; Report Hypervisor Exploit to Sony](https://www.techpowerup.com/352739/ps5-linux-dev-drops-project-after-slop-kiddies-cash-in-on-crucial-exploit) ⭐️ 6.0/10

PS5 Linux developer Andy Nguyen announced he is leaving the PS5 hacking scene and stopping work on PS5 Linux, which also shelved the planned PS5 Pro support. He said a group of LLM-scripting newcomers he calls &\#x27;Slop Kiddies&\#x27; discovered the last remaining PS5 Pro hypervisor exploit and reported it to Sony, and the code that does exist has already been published on GitHub under GPL-3.0 without the PS5 Pro work. Because that hypervisor bug appears to have been the only one left, its disclosure to Sony likely closes off PS5 Pro Linux and homebrew for the foreseeable future, ending a project that had already shown Linux running on a retail PS5. More broadly, the episode is an early example of LLM-assisted vulnerability hunting colliding with long-standing disclosure norms in the console hacking community, where researchers often hoard a bug to time its public release. Hypervisor exploits are the highest-value class of bug here: they let an attacker escape the guest environment Sony enforces and take control of the machine, which is exactly what is needed to boot Linux on a PS5. Nguyen had reportedly intended to hold the bug back until the launch of GTA 6 so that users could both play the game and run Linux, a plan that the early report to Sony has now made very difficult to execute.

telegram · zaihuapd · Sep 17, 07:43

**Background**: Modern PlayStation consoles do not run games directly on the hardware; they boot into a hypervisor, a small privileged layer that isolates the main operating system and enforces Sony&\#x27;s security checks. To install Linux or other homebrew software, hackers must first break out of that layer, which is why a hypervisor exploit is treated as the key that unlocks the whole platform. Nguyen&\#x27;s PS5 Linux effort was one of the scene&\#x27;s most visible projects — he demonstrated Linux running on a standard PS5 and even got GTA V working on it earlier in 2026 — and &\#x27;slop kiddies&\#x27; is scene slang for newcomers who mass-produce low-effort tools and scripts, increasingly with the help of large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gamingonlinux.com/2026/09/ps5-linux-dev-quits-after-the-only-hypervisor-bug-left-was-reported-to-sony/">PS 5 Linux dev quits after &quot;the only hypervisor bug...&quot; | GamingOnLinux</a></li>
<li><a href="https://ixbt.games/en/news/2026/09/16/436306-razrabotcik-linux-dlia-ps5-obieiavil-ob-uxode-so-sceny-vzloma-iz-za-nubov-i-maloletnix-vaibkoderov.html">Linux developer for PS 5 announces departure from hacking scene due...</a></li>
<li><a href="https://hardwear.io/wp-content/uploads/2026/03/Byepervisor__Breaking_PS5_Hypervisor_Security.pdf">Byepervisor: Breaking PS5 Hypervisor Security (2) - hardwear.io</a></li>

</ul>
</details>

**Tags**: `#PS5`, `#Linux`, `#Security`, `#Exploit`, `#LLM`

---

<a id="item-5"></a>
## [Kimi Launches Finance-Specific AI, Deployed at ICBC and CITIC Securities](https://www.cnfin.com/cmjj-lb/detail/20260917/4471293_1.html) ⭐️ 6.0/10

Moonshot AI&\#x27;s Kimi has launched an AI solution tailored to the financial industry, with dozens of leading Chinese institutions — including ICBC, CITIC Securities, CICC and E Fund — reportedly already using or co-developing related capabilities. The company claims the solution cuts financial modeling effort from 5–15 person-days down to 2–4 person-days, and shortens deep industry research report production from 10–20 days to 2–4 days. This marks a shift by a leading Chinese model vendor from general-purpose chatbot competition toward packaged vertical enterprise products, targeting one of the most compliance-sensitive and high-value industries. If the efficiency claims hold up, it could accelerate adoption of domestic large models in banking, securities and asset management, where data sensitivity has long slowed AI deployment. The solution integrates more than ten authoritative data sources and nine finance-specific professional skills, and includes compliance controls such as data classification, access authorization and mandatory human review. Notably, the announcement offers no technical detail on the underlying models or agent architecture, and the efficiency figures come from company materials without independent verification.

telegram · zaihuapd · Sep 17, 10:51

**Background**: Kimi is the AI assistant developed by Moonshot AI \(月之暗面\), one of China&\#x27;s prominent large-model startups. &quot;Vertical AI&quot; refers to models and products built for a specific industry rather than general-purpose use, a direction many vendors have pursued as raw model-capability competition matures. China&\#x27;s financial sector is tightly regulated and handles sensitive client and market data, so vendors must typically pair model capability with data governance and human-in-the-loop processes to win institutional contracts.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/%E6%9C%88%E4%B9%8B%E6%9A%97%E9%9D%A2_%28%E5%85%AC%E5%8F%B8%29">月之暗面 (公司) - 维基百科，自由的百科全书</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1991189725457958445">2026 AI 垂直领域展望：从通用到专精，场景深耕成破局关键</a></li>
<li><a href="https://www.moonshot.ai/">Moonshot AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#enterprise-ai`, `#fintech`, `#Kimi`, `#vertical-ai`

---

<a id="item-6"></a>
## [BYD Plans Four European Plants to Localize EV Production](https://www.bloomberg.com/news/articles/2026-09-17/china-s-byd-targets-four-european-plants-to-anchor-regional-push) ⭐️ 6.0/10

BYD is planning to build three vehicle assembly plants and one battery plant in Europe as part of a long-term localization push, having already started production at its first European passenger-car plant in Hungary. The company says it will decide on the location of its second plant before the end of this year. Local manufacturing lets BYD sidestep EU trade barriers and tariffs on Chinese-made EVs while shortening supply chains and improving its standing with European regulators and customers. As one of the world&\#x27;s largest EV makers, its investment decisions also put pressure on legacy European automakers and signal how Chinese OEMs intend to compete directly on European soil. BYD currently favors acquiring and retrofitting existing European factories rather than building greenfield sites from scratch, a faster and cheaper route to local capacity. In the first half of this year, overseas revenue surpassed its China domestic revenue for the first time, and the company&\#x27;s Europe head said local production will be essential to meeting its long-term European targets as volumes grow.

telegram · zaihuapd · Sep 17, 11:54

**Background**: BYD is China&\#x27;s largest electric-vehicle manufacturer and has been expanding aggressively overseas to sustain growth as competition in its home market intensifies. The European Union has imposed countervailing duties on Chinese-built EVs, which makes local assembly far more attractive economically. Hungary, where BYD&\#x27;s first European passenger-car plant is located, has positioned itself as a hub for Chinese battery and EV investment in the region.

**Tags**: `#BYD`, `#electric vehicles`, `#Europe`, `#manufacturing`, `#localization`

---

<a id="item-7"></a>
## [Apple M5 Ultra benchmark leak: Metal score tops RTX 5090](https://browser.geekbench.com/v7/gpu/171745) ⭐️ 6.0/10

A leaked Geekbench 7 GPU result claims Apple&\#x27;s unreleased M5 Ultra scored 360,019 in the Metal test, edging past the RTX 5090&\#x27;s 350,160 OpenCL score, while the RTX 5090 leads in the Vulkan test with 375,290. The same leak lists an 80-core GPU, 1.2 TB/s memory bandwidth, and up to 512 GB of unified memory. If accurate, it would mean Apple&\#x27;s integrated GPU can trade blows with NVIDIA&\#x27;s flagship discrete card on Apple&\#x27;s own API, a notable signal for Mac users running local AI inference and Metal-optimized creative workloads. The large unified memory pool is arguably the bigger story, since it lets models far larger than a 32 GB consumer GPU can hold run on a single machine. The numbers are not directly comparable: the Metal score comes from Apple&\#x27;s proprietary API while the RTX 5090 figures are from OpenCL and Vulkan, and Geekbench charts only publish GPUs with at least five unique submitted results, so a single leak entry is unverified. The 512 GB unified memory figure likely refers to a top-end configuration that would also put the machine well into workstation pricing territory.

telegram · zaihuapd · Sep 17, 15:20

**Background**: Metal is Apple&\#x27;s proprietary low-level graphics and compute API, comparable to Vulkan and Direct3D 12, but because it is closed and Apple writes its own drivers, it is only benchmarked on Apple \(and some AMD\) GPUs. Apple Silicon uses a unified memory architecture where the CPU, GPU and Neural Engine share one high-bandwidth pool instead of separate system RAM and VRAM, which is why Apple GPUs can be paired with far more memory than typical discrete cards. Geekbench is a synthetic cross-platform benchmark whose Metal, OpenCL and Vulkan results use different code paths and drivers, so scores across APIs are generally not apples-to-apples.

<details><summary>References</summary>
<ul>
<li><a href="https://browser.geekbench.com/metal-benchmarks">Metal Benchmarks - Geekbench</a></li>
<li><a href="https://www.xda-developers.com/apple-silicon-unified-memory/">What is Unified Memory and how does it work on Apple Silicon?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vulkan">Vulkan - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Apple M5 Ultra`, `#GPU benchmarks`, `#Geekbench`, `#local AI`, `#hardware leak`

---