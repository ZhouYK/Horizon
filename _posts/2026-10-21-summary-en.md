---
layout: default
title: "Horizon Summary: 2026-10-21 (EN)"
date: 2026-10-21 23:03:37 +0000
lang: en
report: default
---

> From 172 items, 9 important content pieces were selected

---

1. [Node.js Ships Critical Security Releases Fixing Brotli RCE and TLS/DNS Flaws](#item-1) ⭐️ 8.0/10
2. [AMD FSR Upscaling 4.1 Expands to RX 6000 GPUs, Handhelds and Xbox, With Vulkan Support Coming](#item-2) ⭐️ 7.0/10
3. [Uber&\#x27;s AutoClean AI agents have deleted 16,000+ stale feature flags](#item-3) ⭐️ 7.0/10
4. [Intel and AMD Unify x86 PyTorch Optimizations in oneDNN](#item-4) ⭐️ 7.0/10
5. [NVIDIA Expands Isaac Platform with Humanoid Reference Frameworks and Isaac Lab 3.0](#item-5) ⭐️ 7.0/10
6. [OpenAI Models Coming to Google Cloud Model Garden](#item-6) ⭐️ 7.0/10
7. [SpaceX to attempt first full recovery of Starship and Super Heavy next month](#item-7) ⭐️ 6.0/10
8. [Unitree unveils H2-X humanoid robot with claimed 8-hour battery life](#item-8) ⭐️ 6.0/10
9. [Go Urgently Patches crypto/x509 to Reject Certs From Compromised CA](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Node.js Ships Critical Security Releases Fixing Brotli RCE and TLS/DNS Flaws](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) ⭐️ 8.0/10

The Node.js project published security releases for its 26.x, 24.x, and 22.x lines, patching 10 vulnerabilities with a maximum severity rating of High. The most serious is an out-of-bounds write in the Brotli decoder \(CVE-2026-111497\) that can lead to remote code execution, alongside TLS non-canonical IP address handling issues \(CVE-2026-106069 and CVE-2026-106072\), a DNS resolution null-byte validation flaw \(CVE-2026-105482\), and a TLS IP normalization regression \(CVE-2026-105483\). Because Brotli is one of the standard HTTP compression encodings that Node.js servers can accept from clients, an out-of-bounds write in its decoder means a remotely reachable memory-corruption bug with RCE potential in a runtime that underpins a huge share of production web backends. With the flaws spanning three active release lines plus end-of-life versions, teams running Node.js in exposed services need to identify affected deployments and upgrade promptly rather than waiting for a routine dependency bump. Beyond the four high-severity items, the release also carries medium- and low-severity fixes covering areas such as the HTTP proxy, cryptographic snapshot, zlib, and permission handling. Node.js notes that end-of-life versions are also affected by these vulnerabilities but will not receive patches, so users on those lines must move to a supported release to be protected.

telegram · zaihuapd · Oct 21, 14:49

**Background**: Brotli is a compression algorithm originally developed by Google and now widely supported by browsers and servers as an HTTP content encoding, typically negotiated via the br token in the Accept-Encoding and Content-Encoding headers. Like most decompressors, the Brotli decoder is a complex parser that consumes attacker-controlled bytes, which makes memory-safety bugs in it a classic remote attack surface. An &quot;out-of-bounds write&quot; means the code writes data past the end of an allocated buffer, corrupting adjacent memory and potentially letting an attacker redirect program execution. Node.js bundles Brotli support in core, so both servers accepting compressed request bodies and applications calling the Brotli APIs directly can be exposed.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoftedge.github.io/edgevr/posts/Beyond-Images-Bringing-Rust-Brotli-to-Edge-Network-Stack/">Beyond Images: Bringing Rust Brotli to Edge Network Stack</a></li>
<li><a href="https://dailycve.com/netty-dns-codec-input-validation-bypass-cvenot-disclosed-critical/">Netty, DNS Codec Input Validation Bypass, CVE(Not disclosed ...</a></li>

</ul>
</details>

**Tags**: `#nodejs`, `#security`, `#vulnerability`, `#remote-code-execution`, `#patching`

---

<a id="item-2"></a>
## [AMD FSR Upscaling 4.1 Expands to RX 6000 GPUs, Handhelds and Xbox, With Vulkan Support Coming](https://newsroom.amd.com/news/amd-fsr-upscaling-4-1-boosts-frames-image-quality/) ⭐️ 7.0/10

AMD announced that FSR Upscaling 4.1, its machine-learning-based upscaler, now runs on Radeon RX 6000 series GPUs, Ryzen AI Max processors, Ryzen AI 9 laptops and Z2 Extreme handhelds, with Xbox Series X\|S support arriving soon. The rollout comes with the Adrenalin 26.10.1 driver, and AMD also confirmed that Vulkan API support for FSR 4.1 is in the works. FSR 4 was originally locked to RX 9000 series cards, so extending it to the large installed base of RX 6000 GPUs and to consoles and handhelds dramatically widens the number of players who can use the improved ML upscaler. It also strengthens AMD&\#x27;s position against Nvidia DLSS by offering better image quality on hardware people already own rather than requiring an upgrade. AMD claims FSR 4.1 delivers a noticeable image-quality improvement over FSR 3.1, and games can enable it either through native in-game integration or driver-level controls, though some game menus still label the feature with its older &quot;FSR 4&quot; name. Owners of unsupported hardware will automatically fall back to FidelityFX Super Resolution 3.1.5 through the FSR API.

telegram · zaihuapd · Oct 21, 04:40

**Background**: FSR \(FidelityFX Super Resolution\) is AMD&\#x27;s upscaling technology that renders a game at a lower internal resolution and reconstructs a sharper, higher-resolution image, boosting frame rates. FSR 4, introduced in 2025, moved from a purely analytical algorithm to a machine-learning model, but it initially required RDNA 4-based RX 9000 GPUs before being extended to RX 7000 cards in July 2026. The RX 6000 series, built on the older RDNA 2 architecture, is AMD&\#x27;s previous-generation line that also introduced hardware ray tracing to Radeon cards. Vulkan is a low-overhead, cross-platform graphics and compute API derived from AMD&\#x27;s Mantle, widely used by games and engines as an alternative to DirectX 12.

<details><summary>References</summary>
<ul>
<li><a href="https://newsroom.amd.com/news/amd-fsr-upscaling-4-1-boosts-frames-image-quality/">AMD FSR Upscaling 4 . 1 Boosts Frames and Image... - AMD Newsroom</a></li>
<li><a href="https://gpuopen.com/amd-fsr-sdk/">AMD FSR SDK - AMD GPUOpen</a></li>
<li><a href="https://www.amd.com/en/products/graphics/ecosystems/vulkan.html">AMD Vulkan™ Graphics API</a></li>

</ul>
</details>

**Tags**: `#AMD FSR`, `#GPU Upscaling`, `#Gaming Graphics`, `#Vulkan API`, `#Driver Release`

---

<a id="item-3"></a>
## [Uber&\#x27;s AutoClean AI agents have deleted 16,000+ stale feature flags](https://www.uber.com/us/en/blog/ai-code-cleanup/) ⭐️ 7.0/10

Uber published a blog post detailing AutoClean, an internal system that connects to its feature flag management platform, detects stale flags, and automatically generates clean, tested code diffs for human review. Uber says the system has already removed more than 16,000 flags and over one million lines of code across its production monorepos. Stale feature flags are a near-universal form of tech debt that silently bloats codebases and slows every engineer down, yet manual cleanup rarely gets prioritized. AutoClean demonstrates a production-proven pattern — deterministic transforms plus LLM agents plus verification gates — for applying agentic automation to codebase-wide refactors at a scale far beyond a demo. The pipeline runs in three stages: an AI agent paired with Uber&\#x27;s deterministic PolyglotPiranha transformation tool rewrites the code, the system then repairs CI failures through repeated validation, and finally static checks plus a multi-agent verification layer called CodeCourt review the diff before a human engineer makes the single judgment call on whether the flag should go. Uber&\#x27;s accompanying industrial paper reports that the system produced engineer-approved flag-removal PRs for 45 of 50 \(90%\) stale flags evaluated, at roughly $4.79 and 13.8 minutes per cleanup; PolyglotPiranha itself cannot rewrite code embedded in string literals or templated DSL fragments, which is part of why the agent layer exists.

telegram · zaihuapd · Oct 21, 06:45

**Background**: A feature flag is a runtime toggle that lets teams ship code disabled and turn it on later for specific users or experiments; once an experiment concludes, the flag and all its branching logic become dead weight that must be removed by hand. Uber runs large monorepos spanning many languages, so that cleanup is both tedious and risky at scale. PolyglotPiranha is Uber&\#x27;s open-source DSL-based toolset for automating large-scale code transformations, typically used for exactly this kind of flag cleanup. The remaining gap — code shapes the DSL can&\#x27;t express — is where LLM-based agents take over, followed by automated review to keep human reviewers focused on intent rather than mechanical correctness.

<details><summary>References</summary>
<ul>
<li><a href="https://www.uber.com/us/en/blog/ai-code-cleanup/">Using AI to Delete Code : Agentic Tech Debt Cleanup at Uber</a></li>
<li><a href="https://github.com/uber/piranha">GitHub - uber/ piranha : A tool for refactoring code related to feature...</a></li>
<li><a href="https://conf.researchr.org/details/icsme-2026/icsme-2026-industry-track/8/Automating-Feature-Flag-Cleanup-at-Scale-with-Multi-Agent-LLM-Systems-An-Industrial-">Automating Feature Flag Cleanup at Scale with Multi-Agent LLM...</a></li>

</ul>
</details>

**Tags**: `#ai-agents`, `#tech-debt`, `#feature-flags`, `#code-automation`, `#software-engineering`

---

<a id="item-4"></a>
## [Intel and AMD Unify x86 PyTorch Optimizations in oneDNN](https://mp.weixin.qq.com/s/JcEFssHmhyL0drohofQNkg) ⭐️ 7.0/10

Intel and AMD announced that they are merging their respective PyTorch-oriented x86 CPU optimizations into the open-source oneDNN deep learning library, with AMD contributing its ZenDNN optimizations and joining the UXL Foundation steering committee. The two companies are also collaborating on next-generation x86 AI compute extension instructions, which will be integrated into PyTorch through oneDNN in the future. Historically, Intel and AMD shipped separate, vendor-specific acceleration paths for deep learning on x86, forcing frameworks and developers to deal with fragmented backends. Consolidating these optimizations into a single upstream library means PyTorch users can get tuned CPU inference performance on either vendor&\#x27;s hardware without maintaining separate code paths, which lowers the barrier to running AI workloads on commodity x86 servers. The integration centers on oneDNN, the oneAPI Deep Neural Network Library now hosted under the UXL Foundation, and on AMD&\#x27;s ZenDNN inference acceleration library, which targets the Zen CPU architecture and primarily AMD EPYC server processors. The announcement is high-level and does not specify release versions, timelines, or measured performance gains, and the work on next-generation x86 AI instruction extensions is still forward-looking rather than shipping today.

telegram · zaihuapd · Oct 21, 08:55

**Background**: oneDNN is an open-source library of building blocks that deep learning frameworks such as PyTorch and TensorFlow call into to get optimized performance on CPUs and GPUs, so improvements there benefit every framework that adopts it. ZenDNN is AMD&\#x27;s equivalent library of inference primitives tuned for its Zen cores. The UXL Foundation, launched in September 2023 under the Linux Foundation, governs the open oneAPI standards and projects that compete with Nvidia&\#x27;s CUDA and AMD&\#x27;s own ROCm in cross-architecture accelerated computing.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/uxlfoundation/oneDNN">GitHub - uxlfoundation/ oneDNN : oneAPI Deep Neural Network Library...</a></li>
<li><a href="https://github.com/amd/ZenDNN">GitHub - amd/ZenDNN</a></li>
<li><a href="https://www.amd.com/en/developer/zendnn.html">AMD Zen Deep Neural Network (ZenDNN)</a></li>

</ul>
</details>

**Discussion**: Discussion was minimal: the only visible comment was a joking reference comparing the unlikely Intel-AMD partnership to a historic political coalition, suggesting amusement at two longtime rivals collaborating rather than any technical critique.

**Tags**: `#x86`, `#oneDNN`, `#PyTorch`, `#AI inference`, `#hardware ecosystem`

---

<a id="item-5"></a>
## [NVIDIA Expands Isaac Platform with Humanoid Reference Frameworks and Isaac Lab 3.0](https://nvidianews.nvidia.com/news/nvidia-advances-isaac-platform-for-general-purpose-robotics-with-new-reference-humanoid-frameworks-simulation-pipelines-and-data) ⭐️ 7.0/10

At GTC, NVIDIA announced a major expansion of its Isaac open robotics development platform, adding new humanoid reference frameworks, simulation pipelines, and training data tools that span data generation, AI training, simulation testing, and real-world deployment. The update includes Isaac Lab 3.0 with multi-GPU training support, plus a new asset library containing over 2,000 simulation assets and a human motion dataset. By bundling reference hardware designs, large-scale simulation assets, and GPU-accelerated training tooling into one open stack, NVIDIA is lowering the barrier to entry for general-purpose humanoid robotics and pushing developers toward its ecosystem rather than bespoke pipelines. CEO Jensen Huang framed the moment as a &quot;ChatGPT moment&quot; for robots, signaling that the company sees humanoids as the next major workload for its AI compute business. Isaac Lab 3.0 is an open-source, GPU-accelerated simulation framework for robot learning that supports multiple physics engines and renderers, including NVIDIA Isaac Sim with RTX rendering and the Newton backend for fast simulation without a full renderer. Notably, the Isaac GR00T Reference Humanoid Robot built on this stack is expected to be available from Unitree in late 2026, meaning most developers will work in simulation for now rather than with physical reference hardware.

telegram · zaihuapd · Oct 21, 11:21

**Background**: Isaac is NVIDIA&\#x27;s open robotics development platform, and Isaac Lab is the simulation framework within it where robot policies are trained, typically through reinforcement learning or learning from demonstrations. Because collecting real-world robot data is slow and expensive, developers train in physics simulation and then transfer the resulting policies to physical machines — a process known as sim-to-real transfer, which depends heavily on simulation fidelity and asset diversity. Humanoid robots are especially hard to train because they have many degrees of freedom, which is why multi-GPU training and thousands of pre-built assets matter for productivity.

<details><summary>References</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-advances-isaac-platform-for-general-purpose-robotics-with-new-reference-humanoid-frameworks-simulation-pipelines-and-data">NVIDIA Advances Isaac Platform for General-Purpose Robotics With...</a></li>
<li><a href="https://developer.nvidia.com/isaac/lab">Isaac Lab | NVIDIA Developer</a></li>
<li><a href="https://docs.nvidia.com/isaaclab/isaac-lab">Welcome to Isaac Lab! | Isaac Lab - NVIDIA Documentation Hub</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Isaac`, `#humanoid robotics`, `#simulation`, `#AI training`

---

<a id="item-6"></a>
## [OpenAI Models Coming to Google Cloud Model Garden](https://openai.com/index/openai-models-google-cloud/) ⭐️ 7.0/10

OpenAI and Google Cloud announced a partnership to bring OpenAI&\#x27;s frontier models and Codex agent workflows into Google Cloud&\#x27;s Model Garden, where enterprises can purchase them through Cloud Marketplace and offset the cost against their GCP committed spend. The models are also slated to appear in Google Antigravity and Gemini Agent, with general availability expected within a few weeks. This makes Google Cloud the only hyperscale provider offering Gemini, Claude and GPT side by side on a single enterprise platform, which meaningfully simplifies multi-model procurement and governance for large customers. It also signals a pragmatic thaw between two fierce AI competitors, and gives OpenAI a second enterprise distribution channel beyond Azure while OpenAI stresses that Microsoft remains its primary cloud partner. Access is packaged through Model Garden and billed via Marketplace so that existing GCP committed-spend contracts can cover OpenAI usage, and the OpenAI models join a catalog of more than 200 first-party, third-party and open models. Codex, OpenAI&\#x27;s coding agent for planning, building, refactoring and reviewing code, is being positioned as an agent workflow rather than a plain model endpoint, and the Antigravity and Gemini Agent integrations are described as forthcoming rather than live.

telegram · zaihuapd · Oct 21, 13:40

**Background**: Google Cloud Model Garden is a catalog inside Google&\#x27;s Gemini enterprise platform where teams can discover, customize and deploy pre-trained models from Google and its partners, rather than negotiating separate contracts with each vendor. Google Antigravity is Google&\#x27;s AI-centric software development platform, launched in November 2025 alongside Gemini 3, in which agents write, run and test code with varying degrees of autonomy and which already supports models from Anthropic and OpenAI. Cloud Marketplace committed-spend arrangements are a common way large enterprises consume their pre-negotiated cloud budgets, so getting OpenAI models onto that billing rail removes a major procurement obstacle.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers/?hl=en">Google Cloud brings OpenAI models to customers | Google Cloud ...</a></li>
<li><a href="https://cloud.google.com/model-garden">Model Garden in Gemini platform | Google Cloud</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Google Cloud`, `#Model Garden`, `#enterprise AI`, `#cloud partnership`

---

<a id="item-7"></a>
## [SpaceX to attempt first full recovery of Starship and Super Heavy next month](https://www.theverge.com/science/1014913/spacex-will-try-catching-starship-and-its-booster-for-first-time-musk-says) ⭐️ 6.0/10

Elon Musk said during SpaceX&\#x27;s earnings call that the company will attempt to recover both the Starship upper stage and the Super Heavy booster on the same flight next month, which would mark the first complete recovery of an orbital launch vehicle. He acknowledged the first attempt may fail but expects better odds on subsequent flights. Full reuse of both stages is the core economic premise of Starship: bringing the booster and ship back intact could sharply cut launch costs and raise flight cadence, which matters for SpaceX&\#x27;s Starlink expansion and NASA&\#x27;s Artemis lunar lander plans. Success would also make Starship the first fully reusable orbital rocket, a step beyond Falcon 9&\#x27;s partial reuse. Last month&\#x27;s flight was cut short after one engine shut down early, ending the mission in about three hours with neither stage recovered. Catching the Super Heavy booster relies on the chopstick arms on the launch tower, while the ship must survive reentry using its heat shield tiles before being recovered.

telegram · zaihuapd · Oct 21, 06:00

**Background**: Starship is SpaceX&\#x27;s two-stage, fully reusable super heavy-lift vehicle, consisting of the Super Heavy booster and the Starship spacecraft, both powered by Raptor engines burning liquid methane and liquid oxygen. SpaceX has developed it through an iterative test-flight campaign, and Super Heavy boosters have already been caught by the tower and in some cases flown again, but the upper stage has not yet been recovered intact. Musk&\#x27;s stated goal is to reuse both stages to lower launch costs and enable missions to the Moon and Mars.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship</a></li>
<li><a href="https://en.wikipedia.org/wiki/Super_Heavy_Booster_10">Super Heavy Booster 10</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Super_Heavy">SpaceX Super Heavy - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#reusable-rockets`, `#aerospace`, `#spaceflight`

---

<a id="item-8"></a>
## [Unitree unveils H2-X humanoid robot with claimed 8-hour battery life](https://m.weibo.cn/detail/5356475359693858) ⭐️ 6.0/10

On October 21, Unitree Technology announced a new humanoid robot called the H2-X &quot;Kung Fu Legend Guardian,&quot; claiming a maximum battery life of about 8 hours along with dramatic physical feats such as lifting a car with its bare hands, kicking a car door inward, and serving as a &quot;personal bodyguard.&quot; The company did not disclose detailed hardware specifications, offering only the battery-life figure as a comparison point against the existing H2. Battery life is one of the biggest practical bottlenecks keeping humanoid robots out of full-shift real-world work, so a jump from roughly 3 hours to 8 hours would meaningfully change how such robots can be deployed in security, inspection, and industrial scenarios. Unitree is one of the highest-profile and highest-volume humanoid robotics companies, so its product claims tend to shape expectations for the whole embodied-AI sector. Unitree has not published the H2-X&\#x27;s actuator, sensor, weight, or compute specifications, and the announcement relies on promotional demonstration footage rather than independently verified benchmarks. The company cites the H2 as a reference point: 182 cm tall, 31 degrees of freedom, and roughly 3 hours of battery life, while the standard H2 is listed at around $29,900 on Unitree&\#x27;s online store.

telegram · zaihuapd · Oct 21, 10:32

**Background**: Unitree Robotics is a Chinese company known for quadruped robots such as the Go2 and for progressively cheaper humanoid models including the G1, H1, and H2. In humanoid robotics, &quot;degrees of freedom&quot; refers to the number of independently actuated joints — a typical full-size humanoid has roughly 28 to 56, so the H2&\#x27;s 31 DoF sits at the lower end and reflects a design optimized for cost and robustness rather than dexterous manipulation. Battery life has become a headline spec because legged robots draw large amounts of power while balancing and walking, which is why most current full-size humanoids run for only a few hours per charge.

<details><summary>References</summary>
<ul>
<li><a href="https://shop.unitree.com/products/unitree-h2">Unitree H 2 – UnitreeRobotics</a></li>
<li><a href="https://www.smashingrobotics.com/how-many-degrees-of-freedom-does-a-humanoid-robot-have/">Degrees of Freedom in a Humanoid Robot: How Many DoF (October ...</a></li>
<li><a href="https://www.unitree.com/h1/">Universal humanoid robot H1_Bipedal Robot_Humanoid ... - unitree</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#humanoid-robots`, `#Unitree`, `#hardware`, `#product-announcement`

---

<a id="item-9"></a>
## [Go Urgently Patches crypto/x509 to Reject Certs From Compromised CA](https://access.redhat.com/security/cve/cve-2026-111943) ⭐️ 6.0/10

Go shipped an urgent fix to its crypto/x509 certificate verification code for CVE-2026-111943 \(CVSS 3.1 score 6.8\), because the verifier failed to reject intermediate certificates chained to a compromised certificate authority. The flaw is classified as a Trust Anchor Compromise weakness \(CWE-295\), and Red Hat rates it as an &\#x27;Important&\#x27; severity issue. Any Go-based client or server that relies on the standard library&\#x27;s TLS certificate verification could be tricked into accepting an unauthorized certificate, allowing an attacker to impersonate a legitimate server and intercept encrypted traffic. Because crypto/x509 sits in the standard library, the impact reaches a very broad swath of Go services rather than a single project. Exploitation requires the attacker to hold a certificate issued by the distrusted intermediate CA and to occupy a specific network position, and Red Hat notes it is unlikely to be abused at large scale. The vulnerability primarily manifests in environments where the system root store has not been updated with the distrust information; mitigation steps are listed in the security advisory.

telegram · zaihuapd · Oct 21, 15:26

**Background**: TLS certificates are validated through a chain of trust: a leaf certificate is signed by an intermediate CA, which in turn chains up to a root CA in the operating system or application&\#x27;s trust store. When a certificate authority is compromised or misbehaves, vendors distribute distrust entries so that chains passing through it are rejected — but software must correctly honor those entries. A man-in-the-middle attack exploits any gap in that validation, letting an attacker present a seemingly valid certificate for a domain it does not own and decrypt or alter the traffic.

<details><summary>References</summary>
<ul>
<li><a href="https://app.opencve.io/cve/CVE-2026-111943">CVE-2026-111943 - Vulnerability Details - OpenCVE</a></li>
<li><a href="https://access.redhat.com/security/cve/cve-2026-111943">CVE-2026-111943 - Red Hat Customer Portal</a></li>
<li><a href="https://pkg.go.dev/crypto/x509">x509 package - crypto/x509 - Go Packages</a></li>

</ul>
</details>

**Discussion**: A group commenter framed the issue as not a remotely exploitable coding flaw in Go itself, but rather the compromise of an Indian certificate authority combined with Go&\#x27;s failure to block the resulting certificates during validation.

**Tags**: `#Go`, `#security-vulnerability`, `#TLS/certificates`, `#man-in-the-middle`, `#crypto/x509`

---