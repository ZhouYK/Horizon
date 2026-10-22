---
layout: default
title: "Horizon Summary: 2026-10-22 (EN)"
date: 2026-10-22 23:03:34 +0000
lang: en
report: default
---

> From 171 items, 9 important content pieces were selected

---

1. [Australian Court Orders Apple to Open iPhone to Third-Party App Stores](#item-1) ⭐️ 8.0/10
2. [333 Backdoored Tor Exit Nodes Taken Offline After Ebury Infection](#item-2) ⭐️ 8.0/10
3. [Banned Nvidia B300 Chips Reportedly Found in Chinese State-Linked Data Center Deal](#item-3) ⭐️ 8.0/10
4. [Anthropic ships Claude API 2026-10-21, removing temperature, top\_p and top\_k](#item-4) ⭐️ 7.0/10
5. [Trump: Data center builders should pay communities a &\#x27;dividend&\#x27; and self-generate power](#item-5) ⭐️ 7.0/10
6. [Study: Smart TVs Keep Reporting Viewing Data After ACR Is Disabled](#item-6) ⭐️ 7.0/10
7. [miHoYo and Tsinghua Open-Source GameScaling, a 0.8B–27B Vision-Language Game Control Model](#item-7) ⭐️ 7.0/10
8. [Oracle Issues Critical Java SE Security Alert for JSSE Flaw](#item-8) ⭐️ 7.0/10
9. [XPeng IRON humanoid robot re-infers vision every 0.2 seconds with second-gen VLA model](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Australian Court Orders Apple to Open iPhone to Third-Party App Stores](https://9to5mac.com/2026/10/21/apple-must-open-iphone-to-alternative-app-stores-in-australia-after-epic-games-ruling/) ⭐️ 8.0/10

Australia&\#x27;s Federal Court ruled that Apple must let Australian iPhone users install apps from third-party app stores and websites \(sideloading\), and must permit alternative payment methods and external payment links, starting March 1, 2027. The ruling stems from Epic Games&\#x27; antitrust suit, and Fortnite is set to return to the Australian App Store immediately. This is the first time a court outside the EU&\#x27;s regulatory framework has ordered Apple to unbundle iOS app distribution and payments, making it a precedent that other regulators and litigants can cite. If upheld, it would reshape app-distribution economics in a major market and force Apple to maintain yet another region-specific version of iOS, on top of the changes already required by the EU&\#x27;s Digital Markets Act. The judge found that Apple holds substantial market power in iOS app distribution and in-app payments, and that its restrictions substantially lessened competition in violation of Australian competition law. Apple says it will appeal and seek a stay of execution, so the March 1, 2027 deadline could still slip, and the immediate return of Fortnite suggests parts of the remedy take effect sooner than the broader compliance date.

telegram · zaihuapd · Oct 22, 06:54

**Background**: Epic Games sued Apple in Australia after Fortnite was removed from the App Store in 2020 for bypassing Apple&\#x27;s in-app purchase system, mirroring parallel litigation in the United States and elsewhere. Australian competition law, enforced by the Australian Competition and Consumer Commission \(ACCC\) and litigated in the Federal Court, prohibits conduct that substantially lessens competition and allows courts to impose behavioural and structural remedies. The case parallels the EU&\#x27;s Digital Markets Act, which since 2024 has forced Apple to allow alternative app marketplaces and payment options in Europe, as well as similar moves in Japan and the UK. &\#x27;Sideloading&\#x27; refers to installing apps from sources other than the platform&\#x27;s official store, which iOS has historically blocked outside of enterprise and developer workarounds.

<details><summary>References</summary>
<ul>
<li><a href="https://www.junhe.com/legal-updates/2760">反垄断调查国别研究系列文章：澳大利亚篇</a></li>
<li><a href="https://www.lexology.com/library/detail.aspx?g=7bbd5871-2e39-4731-8199-a54ea3c2fe49">反垄断调查国别研究系列文章：澳大利亚篇 - Lexology</a></li>

</ul>
</details>

**Tags**: `#antitrust`, `#apple`, `#app-store`, `#regulation`, `#epic-games`

---

<a id="item-2"></a>
## [333 Backdoored Tor Exit Nodes Taken Offline After Ebury Infection](https://kaba.cx/posts/20261020_Tor/) ⭐️ 8.0/10

A Tor operator scripted a scan of roughly 3,000 exit relays and found 333 of them — about 10% of all exits — infected with the Ebury backdoor, which redirected SSH connections on port 22 to 12 interception servers to harvest credentials. The nodes were flagged as BadExit on October 4 and all went offline the following day. Because exit relays are the point where Tor traffic leaves the anonymity network, a backdoored exit can silently intercept and rewrite traffic for any user routed through it, and at roughly one in ten exits the exposure was broad. The incident shows that Tor&\#x27;s exit population remains a soft target for credential-theft operations, affecting anyone who relied on Tor to reach SSH or unencrypted services. The attackers compromised the servers back in August and also blocked certain ports so the relays would preferentially collect unencrypted email traffic, but the initial intrusion vector is still undetermined. The scan covered roughly 3,000 exits, so the 333 malicious relays represent a lower bound on infection rather than a complete census.

telegram · zaihuapd · Oct 22, 14:52

**Background**: Tor is a volunteer-run anonymity network that routes traffic through three relays; the last one, the exit relay, decrypts the traffic and forwards it to the public internet, which is why rogue exits can snoop on unencrypted protocols or perform man-in-the-middle attacks. The Tor Project counters this with the BadExit flag: a relay carrying it is never chosen as an exit, effectively removing it from service as an exit node. Ebury is a long-lived Linux backdoor associated with the Windigo group \(documented by ESET\) that is used to hijack SSH connections and steal credentials and has historically spread through compromised hosting providers.

<details><summary>References</summary>
<ul>
<li><a href="https://hackerncoder.pages.torproject.net/support/zh-CN/relay-operators/what-is-the-bad-exit-flag/">BadExit标签是什么？ | Tor Project | 支持</a></li>
<li><a href="https://salivity.github.io/tor/article/understanding-the-tor-bad-exit-flag">Understanding the Tor BadExit Flag - tor</a></li>
<li><a href="https://www.secrss.com/articles/6975">攻防最前线：ESET发现21个Linux 恶 意 软 件</a></li>

</ul>
</details>

**Tags**: `#Tor`, `#Ebury`, `#malware`, `#cybersecurity`, `#credential theft`

---

<a id="item-3"></a>
## [Banned Nvidia B300 Chips Reportedly Found in Chinese State-Linked Data Center Deal](https://theinference.org/article/china-s-state-money-bought-banned-nvidia-b300-servers-then-redacted-the-receipts) ⭐️ 8.0/10

A Chinese state-controlled semiconductor leasing group reportedly financed the purchase of 32 ASUS servers equipped with export-banned Nvidia B300 chips for AI company Rongyao Shitu Technology, as part of a larger 700-plus server order worth more than 3 billion RMB intended for China Mobile&\#x27;s Ningxia hub. After the filing drew scrutiny, the leasing group resubmitted documents with the hardware descriptions redacted, prompting Nvidia to say it is investigating with its manufacturing partners and ASUS to state that it complies with export controls. If confirmed, this would be one of the clearest cases of the most restricted tier of US AI hardware reaching a Chinese state-linked deployment at scale, putting export-control enforcement and the compliance obligations of Nvidia&\#x27;s OEM partners under intense scrutiny. It also signals that demand for frontier compute in China remains strong enough to work around restrictions, with implications for US-China tech policy and AI compute supply chains. The B300 is Nvidia&\#x27;s Blackwell Ultra-class accelerator subject to the strictest US export tier and effectively banned for sale to China, while Nvidia has prepared a down-spec&\#x27;d B30A variant specifically for the Chinese market. The redaction of hardware details from a resubmitted filing — rather than a denial that the chips exist — is the central anomaly that triggered the Nvidia and ASUS investigations.

telegram · zaihuapd · Oct 22, 15:22

**Background**: US export controls bar the sale of the most advanced AI accelerators, such as Nvidia&\#x27;s top-tier Blackwell parts, to Chinese customers, on the grounds that they could support military or strategic AI development. To keep serving China legally, Nvidia has designed reduced-performance China-specific chips such as the H20 and the newer B30A, which fall under thresholds set by Washington. Chinese AI firms have meanwhile sought frontier compute through overseas cloud access and third-party intermediaries, gaps that US lawmakers have been pressing to close.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/nvidia-blackwell-b30a-china-faster-than-h20-half-the-performance-blackwell-ultra-b300/">NVIDIA Preps Blackwell B30A For China: Faster Than H20 But Half...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-next-gen-b300-gpus-have-1-400w-tdp-deliver-50-percent-more-ai-horsepower-report">Nvidia &#x27;s next-gen B 300 GPUs have 1,400W TDP... | Tom&#x27;s Hardware</a></li>
<li><a href="https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html">China AI firms tap Nvidia power overseas as U . S . weighs crackdown</a></li>

</ul>
</details>

**Tags**: `#export-controls`, `#nvidia`, `#semiconductors`, `#china`, `#ai-hardware`

---

<a id="item-4"></a>
## [Anthropic ships Claude API 2026-10-21, removing temperature, top\_p and top\_k](https://x.com/ClaudeDevs/status/2113013247209021918) ⭐️ 7.0/10

Anthropic released Claude API version 2026-10-21, its first official version update since 2023, and the new version no longer accepts the temperature, top\_p and top\_k sampling parameters — requests that still include them now fail with HTTP 400. The official SDKs and the ant CLI now default to the new version, the authentication header has switched to Authorization: Bearer, and the older 2023-06-01 version remains supported rather than being deprecated. This is a breaking change to one of the most widely used LLM APIs, so any application, agent framework or evaluation harness that hard-codes sampling parameters will start receiving 400 errors as soon as it upgrades its SDK. It also signals a broader shift in API design away from exposing low-level sampling knobs, which could push developers toward prompt-level or model-level controls and prompt other providers to follow suit. The removal appears to be a hard rejection rather than a silent ignore, since leftover temperature values in request bodies will break existing calls, and the switch to an Authorization: Bearer header means older code that used the previous auth header style also needs updating. Because 2023-06-01 is explicitly not deprecated, teams can pin the old version as a short-term migration path, but the SDK/CLI defaults have already flipped, so pinned versions must be set explicitly.

telegram · zaihuapd · Oct 22, 03:54

**Background**: Sampling parameters are the knobs in an LLM request body that reshape the model&\#x27;s next-token probability distribution: temperature scales overall randomness \(typically 0–2\), top\_p keeps only the tokens whose cumulative probability reaches a threshold, and top\_k caps the candidate set to the K most likely tokens. Developers have long used them to trade off creativity against determinism, so removing them from a major commercial API is unusual. The Authorization: Bearer header comes from the OAuth 2.0 framework, where a client sends the word Bearer followed by an access token to prove it is authorized to call a service; it is the de-facto standard for HTTP API authentication. The ant CLI is Anthropic&\#x27;s official command-line client for the Claude API, which builds request bodies from typed flags or piped YAML instead of hand-written JSON.

<details><summary>References</summary>
<ul>
<li><a href="https://ai-tldr.dev/learn/llm-apis/api-basics/sampling-parameters-explained/">Temperature, Top-P, Top-K: LLM Sampling Parameters | AI/TLDR</a></li>
<li><a href="https://github.com/anthropics/anthropic-cli">GitHub - anthropics/anthropic-cli: The CLI for the Claude API</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude API`, `#breaking changes`, `#LLM tooling`, `#API design`

---

<a id="item-5"></a>
## [Trump: Data center builders should pay communities a &\#x27;dividend&\#x27; and self-generate power](https://www.reuters.com/business/retail-consumer/trump-says-companies-should-pay-dividend-communities-make-data-centers-popular-2026-10-21/) ⭐️ 7.0/10

On Oct. 21, Trump posted on Truth Social that companies building data centers should pay host communities a &quot;dividend&quot; to gain local support, and that large data centers must generate their own electricity and share or sell surplus power locally. The remarks elevate data center energy and water use from a local zoning issue to a national political issue, and they signal that future AI infrastructure deals may be expected to include community payouts and self-generation commitments. Trump offered no details on how the dividend would be calculated, who would enforce it, or whether it would become formal policy; the post instead framed financial agreements as the reason once-unpopular data centers become &quot;extremely popular.&quot;

telegram · zaihuapd · Oct 22, 05:39

**Background**: Data centers, especially those supporting AI workloads, consume large amounts of electricity and water for cooling, and local opposition has grown over higher utility bills, water scarcity, and land use. Community benefits agreements \(CBAs\) — legally binding contracts between developers and local coalitions or municipalities — have emerged as a governance tool to guarantee local benefits in exchange for support. The debate is also drawing in corporate pledges: Anthropic said it would commit 5% of its shares to a public benefit fund, and Elon Musk pledged a SpaceX share for every American child.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wri.org/technical-perspectives/community-benefits-agreements-data-centers">Powering Progress: How Community Benefits Agreements Can...</a></li>
<li><a href="https://www.brookings.edu/articles/why-community-benefit-agreements-are-necessary-for-data-centers/">Why community benefit agreements are necessary for data centers</a></li>
<li><a href="https://upward.news/p/musk-pledges-a-spacex-share-for-every-american-kid">Musk Pledges a SpaceX Share for Every American Kid</a></li>

</ul>
</details>

**Tags**: `#data-centers`, `#AI-infrastructure`, `#energy-policy`, `#regulation`, `#tech-industry`

---

<a id="item-6"></a>
## [Study: Smart TVs Keep Reporting Viewing Data After ACR Is Disabled](https://watchingthewatchers.github.io/watchingthewatchers/index.html) ⭐️ 7.0/10

A controlled study of 12 smart TVs from 10 vendors, spanning 5,943 experiments, found that some models continue transmitting content-related telemetry even after automatic content recognition \(ACR\) is switched off in the settings menu. Two platforms were notably worse: VIDAA OS sends data, including a non-resettable device ID and audio fingerprints, over plaintext MQTT, while Vizio&\#x27;s WatchFree+ embeds program titles in unencrypted DNS queries that users cannot opt out of. The findings suggest that the privacy toggle users are told to flip may be largely cosmetic, undermining a core assumption of consumer consent in smart TVs. Because the data leaves the device in plaintext on at least two platforms, it is also visible to anyone on the local network or upstream path, which turns a tracking issue into an eavesdropping and fingerprinting risk that affects every household using these sets. The study is empirical and reproducible, covering 12 televisions across 10 vendors with 5,943 controlled experiments, and it singles out two distinct leakage paths: application-layer payloads sent unencrypted over MQTT, and content identifiers exposed at the DNS-resolution layer. It is a focused measurement study of the US market rather than an industry-wide audit, so the results characterize the specific models tested rather than every smart TV on the market.

telegram · zaihuapd · Oct 22, 09:50

**Background**: Automatic content recognition \(ACR\) is a technology that identifies what is playing on a screen — a show, an ad, or a song — by sampling audio or video and matching it against a database, similar in principle to how Shazam identifies music. TV makers use ACR to profile viewing habits for advertising and analytics, and audio fingerprinting, which reduces a sound clip to a compact digital signature, is one of the main techniques involved. MQTT is a lightweight publish–subscribe messaging protocol designed for bandwidth-constrained IoT devices, and while it supports encrypted transport, it does not require it — so plaintext deployment is common. This study asks a simple question: does turning ACR off in the settings actually stop the identification and reporting?

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_content_recognition">Automatic content recognition - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/MQTT_protocol">MQTT protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Audio_fingerprinting">Audio fingerprinting</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#smart-tv`, `#security-research`, `#data-tracking`, `#ACR`

---

<a id="item-7"></a>
## [miHoYo and Tsinghua Open-Source GameScaling, a 0.8B–27B Vision-Language Game Control Model](https://arxiv.org/abs/2610.28698v1) ⭐️ 7.0/10

miHoYo&\#x27;s Honkai AI team, together with Tsinghua University and other collaborators, released GameScaling, a family of vision-language action models built by continued pre-training Qwen3.5 on keyboard-and-mouse gameplay and spanning 0.8B to 27B parameters. Each inference step predicts the next 200 milliseconds of keyboard and mouse actions, and the team published a scaling study covering 120 training configurations, releasing eight checkpoints plus an inference client under Apache-2.0. This is a rare large-scale, openly licensed checkpoint release for game-playing agents, giving the game-AI and embodied-agent research communities a reproducible baseline instead of a closed demo. The accompanying scaling analysis on data volume, data diversity and model size offers practical guidance for anyone training action models, and an Apache-2.0 inference client lowers the barrier to experimentation considerably. The study found that more data consistently improves in-domain performance, while greater data diversity mainly helps transfer to similar games and yields only limited gains on very different game worlds. Eight checkpoints and an inference client are released under Apache-2.0, but the training code is withheld, which limits full end-to-end reproducibility.

telegram · zaihuapd · Oct 22, 11:32

**Background**: GameScaling builds on Qwen3.5, a unified vision-language model family from Alibaba&\#x27;s Qwen team that handles image and video understanding alongside text. Rather than predicting a single action per frame, the model uses a technique known as action chunking: it emits a short sequence of future inputs \(here, 200 milliseconds of keyboard and mouse signals\) at once, which produces smoother and more temporally consistent control — the same idea widely used in robot policy learning such as the Action Chunking Transformer.

<details><summary>References</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.5">Qwen</a></li>
<li><a href="https://claru.ai/glossary/action-chunking">Action Chunking for Robot Policies — Definition | Claru</a></li>

</ul>
</details>

**Tags**: `#game AI`, `#vision-language models`, `#open-source`, `#scaling laws`, `#agents`

---

<a id="item-8"></a>
## [Oracle Issues Critical Java SE Security Alert for JSSE Flaw](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html) ⭐️ 7.0/10

Oracle published a security alert for CVE-2026-91403, a critical vulnerability in the JSSE component of Java SE with a CVSS score of 9.1 that can be exploited remotely over the network without authentication. The flaw affects a broad range of releases, including Java SE 8u511, 11.0.33, 17.0.21, 21.0.13, 25.0.5 and 27.0.1 as well as several GraalVM versions, and Oracle has released patches for the affected versions. Because Java runs on a huge share of enterprise back-end servers, build pipelines and client desktops, an unauthenticated, network-reachable 9.1-rated flaw in a core security component creates a large, easily enumerated attack surface. Any organization running affected JDKs should treat patching as urgent, since the advisory affects everything from the still widely deployed Java 8 line up to the newest JDK 27. Oracle notes the vulnerability can be exploited through APIs in the affected component, for example via a web service that supplies data to those APIs, and that it also applies to deployments running sandboxed Java Web Start applications or applets that load untrusted code. The advisory describes impact on confidentiality and integrity, and the CVSS number reflects severity rather than actual risk, so exposure depends on whether the JSSE-dependent code path is reachable in a given deployment.

telegram · zaihuapd · Oct 22, 12:30

**Background**: JSSE \(Java Secure Socket Extension\) is the part of the Java standard library that implements TLS/SSL and the underlying cryptographic handshakes, so it is what most Java applications silently rely on for encrypted network traffic such as HTTPS and secure database connections. CVSS is an industry framework that scores vulnerabilities from 0.0 to 10.0 based on factors such as attack vector, complexity, required privileges and impact; anything at 9.0 or above is classified as critical. GraalVM is Oracle&\#x27;s polyglot runtime built on the JDK, which is why the advisory covers it alongside standard Java SE releases.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oracle.com/security-alerts/alert-cve-2026-91403.html">Oracle Security Alert Advisory - CVE-2026-91403</a></li>
<li><a href="https://cve.halosecurity.com/cve-advisory/cve-2026-91403-oracle-java-se-jsse-vulnerability-allows-unauthorized-data">CVE-2026-91403: Oracle Java SE JSSE Vulnerability Allows ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System">Common Vulnerability Scoring System - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Java`, `#security-vulnerability`, `#CVE`, `#Oracle`, `#patching`

---

<a id="item-9"></a>
## [XPeng IRON humanoid robot re-infers vision every 0.2 seconds with second-gen VLA model](https://www.ithome.com/1/016/667.htm) ⭐️ 6.0/10

XPeng announced that its second-generation VLA \(Vision-Language-Action\) model has been deployed on-device in its IRON humanoid robot, allowing it to re-infer from the camera feed every 0.2 seconds and predict motion changes up to 6 seconds ahead. This lets IRON adapt mid-gesture during handshakes or high-fives, for example when a person suddenly clenches their fist or shifts the position of their palm. The 0.2-second re-inference loop points to a broader shift in embodied AI: instead of running large models in the cloud, robots need tightly coupled, low-latency on-device perception-and-control loops to interact safely with people in real time. XPeng&\#x27;s stated plan to mass-produce humanoid robots by the end of 2026 and begin deliveries in the first half of 2027 puts a Chinese automaker among the growing field of companies racing to commercialize general-purpose robots. XPeng has said IRON runs on its in-house Turing AI chips \(reported at a combined 2,250 TOPS\) with all-solid-state batteries, and the first deployment scenarios are stores and shopping malls rather than factories. Notably, the 0.2-second re-inference and 6-second prediction figures are XPeng&\#x27;s own claims and have not yet been independently benchmarked.

telegram · zaihuapd · Oct 22, 13:37

**Background**: A VLA model is essentially a vision-language model with an added action output: it takes in camera images and language instructions, and directly generates robot control commands, an approach popularized by Google&\#x27;s RT-2 in 2023. Running such a model &quot;on-device&quot; means the compute sits on the robot itself rather than in a data center, which matters because wireless latency and connectivity would make real-time physical interaction unreliable. Re-inference frequency is therefore a key metric — the faster a policy can be recomputed from fresh camera frames, the more gracefully a robot can react to unpredictable human behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7">XPENG Shares Achievements in Physical AI Emergence: Unveils ...</a></li>
<li><a href="https://robotsatlas.com/robots/xpeng-iron">XPENG IRON | Robots Atlas</a></li>
<li><a href="https://www.understandingai.org/p/how-google-taught-llms-to-control">How Google taught LLMs to control robots and started a robotics boom</a></li>

</ul>
</details>

**Tags**: `#humanoid robotics`, `#embodied AI`, `#VLA models`, `#on-device inference`, `#XPeng`

---