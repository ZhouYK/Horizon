---
layout: default
title: "Horizon Summary: 2026-10-25 (EN)"
date: 2026-10-25 23:03:02 +0000
lang: en
report: default
---

> From 144 items, 6 important content pieces were selected

---

1. [Critical Brotli Flaw CVE-2026-111497 Spreads to Python HTTP Libraries](#item-1) ⭐️ 8.0/10
2. [a16z index: GPU rental prices surge across every generation, even the A100](#item-2) ⭐️ 7.0/10
3. [Sogou Input Method OPPO Custom Build Flagged by Google Play Protect](#item-3) ⭐️ 6.0/10
4. [Tesla to Build In-House AI Maps, Debuting With FSD v15](#item-4) ⭐️ 6.0/10
5. [GEEKCON Shanghai Drone Challenge Halted After Vendor Calls Police](#item-5) ⭐️ 6.0/10
6. [Apple Reportedly to Unveil First Touchscreen MacBook Pro on Wednesday](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Critical Brotli Flaw CVE-2026-111497 Spreads to Python HTTP Libraries](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 8.0/10

A critical vulnerability in Google&\#x27;s Brotli decoder, tracked as CVE-2026-111497 and rated CVSS 4.0 score 9.2, affects Brotli versions 1.0.3 through 1.2.0 and has expanded beyond Node.js to Python packages. Python&\#x27;s Brotli must be upgraded to 1.2.1 and brotlicffi to 1.2.1.0, while Node.js fixes ship in 22.23.4, 24.22.1 and 26.12.1; the flaw was initially disclosed as Node2Shell and later renamed HTTP2Shell. Brotli is embedded in browsers, web servers and HTTP client stacks across nearly every language ecosystem, so an unauthenticated remote attacker who can feed a crafted compressed stream could trigger memory corruption, data leakage, crashes or potentially arbitrary code execution. Because the vulnerable code sits in widely deployed HTTP components rather than a niche library, patches need to propagate through Python and Node.js dependency chains quickly. The bug lies in DecodeBlockTypeAndLength\(\), which handles block switches where a Brotli stream changes which Huffman tree it uses. OpenAI is credited with discovering the issue in February, and public proof-of-concept exploit code has since appeared; the advisory itself is brief and does not offer a deep technical analysis.

telegram · zaihuapd · Oct 25, 02:42

**Background**: Brotli is a lossless compression algorithm and data format developed by Google that shrinks data for storage or transmission, which software then decompresses to recover the original bytes; it is comparable to gzip/deflate but generally achieves better ratios, and browsers use it for compressed HTTP responses. Python projects access it either through the C-extension Brotli package or through brotlicffi, a CFFI binding to the same reference library. This is not Brotli&\#x27;s first decoder flaw: CVE-2020-8927 was a buffer overflow triggered by oversized one-shot decompression requests, showing that decoder input handling has been a recurring risk area.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497">Node2Shell Brotli vuln ( CVE - 2026 - 111497 ) evolves to HTTP2Shell, as...</a></li>
<li><a href="https://github.com/python-hyper/brotlicffi">GitHub - python-hyper/brotlicffi: Python bindings to the ... brotli · PyPI GitHub - python-hyper/brotlicffi: Python bindings to the ... brotlicffi - Anaconda.org brotlicffi: Python CFFI Bindings for Brotli Compression brotlicffi 1.2.1.0 on PyPI - Libraries.io - security ...</a></li>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2020-8927/">CVE-2020-8927: Google Brotli Buffer Overflow Vulnerability</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#Brotli`, `#Python`, `#Node.js`

---

<a id="item-2"></a>
## [a16z index: GPU rental prices surge across every generation, even the A100](https://x.com/a16z/status/2113741008550990191) ⭐️ 7.0/10

An a16z-tracked GPU rental price index, set to 100 on January 1, 2026, shows that by October 19 the seven-day moving average had climbed to roughly 265 for the H200 \(+160%\), 225 for the B200 \(+120%\), 165 for the RTX PRO 6000 workstation card \(+65%\) and 137 for the H100 SXM \(+35%\). Even the A100 SXM4, a GPU launched in 2020, edged up to about 102 — slightly above its level at the start of the year. Rental prices are the clearest real-time signal of AI compute supply and demand, and a broad double-digit rise across the newest, previous-generation and even five-year-old datacenter GPUs points to system-wide scarcity rather than demand for frontier chips alone. That directly raises costs for startups training or serving models, squeezes neoclouds and resellers, and pushes capacity planning toward older or non-datacenter hardware. The figures are index levels from a seven-day moving average rather than raw dollar-per-hour rates, so they capture trend direction and relative magnitude rather than absolute rental cost. Notably, the index also tracks the RTX PRO 6000 Blackwell workstation card, whose 65% jump hints that demand is spilling over from datacenter parts into professional/workstation GPUs, while the A100&\#x27;s mere ~2% gain suggests older silicon is absorbing residual demand rather than being bid up aggressively.

telegram · zaihuapd · Oct 25, 06:39

**Background**: The GPUs in the index span several NVIDIA architectures: the A100 \(Ampere, 2020\) was the workhorse of the first large-language-model training wave; the H100 \(Hopper, 2022–2023\) became the standard for generative AI training and inference; the H200 is a Hopper refresh with faster HBM3e memory and more of it; the B200 is a Blackwell-generation datacenter GPU; and the RTX PRO 6000 is a Blackwell workstation card used for local AI work. Because buying these chips outright is expensive and lead times are long, most companies rent them by the GPU-hour from hyperscalers, specialized &\#x27;neocloud&\#x27; providers, or marketplace aggregators. An index that normalizes each rental record to a per-hour, per-GPU rate across providers therefore works as a proxy for how tight the overall AI compute market is.

<details><summary>References</summary>
<ul>
<li><a href="https://computingpower.org/hardware/h100-vs-a100">NVIDIA GPU Comparison: B200 vs H200 vs H100 vs A100</a></li>
<li><a href="https://grokipedia.com/page/NVIDIA_RTX_Pro_6000_Blackwell">NVIDIA RTX Pro 6000 Blackwell — Grokipedia</a></li>
<li><a href="https://www.silicondata.com/products/silicon-index">GPU Rental Price Indices | Silicon Data</a></li>

</ul>
</details>

**Tags**: `#gpu-pricing`, `#ai-infrastructure`, `#compute-market`, `#hardware`, `#cloud-costs`

---

<a id="item-3"></a>
## [Sogou Input Method OPPO Custom Build Flagged by Google Play Protect](https://telegram.me/zaihuapd/44689) ⭐️ 6.0/10

ColorOS users reported that the Sogou Input Method build customized for OPPO devices was detected by Google Play Protect as a harmful app \(PHA\), which automatically revoked its sensitive permissions, disabled the app, and displayed a warning that it could pry into SMS messages, photos, recordings, and call logs. When asked about the alert, OPPO customer service reportedly said the issue is being actively worked on and suggested users could temporarily turn off Play Protect in the meantime. A preinstalled keyboard on millions of OPPO/ColorOS devices being flagged as a privacy risk raises serious questions about how OEM-customized builds of popular apps are vetted, especially since an input method sees essentially everything the user types. More troubling, advising users to disable Play Protect—Android&\#x27;s most widely deployed malware defense—removes protection against all other apps and sets a risky precedent for how vendors handle security alerts. The flagged package is the OPPO-specific customization rather than the public Sogou Input Method release, and OEM preinstalled builds are typically signed and configured separately from store-distributed versions, which can affect how detection heuristics classify them—though Play Protect&\#x27;s warning specifically cites access to SMS, photos, recordings, and call logs. The original report is brief and offers no technical analysis of whether the detection reflects genuine permission overreach or a false positive triggered by the customized signature.

telegram · zaihuapd · Oct 25, 09:59

**Background**: Google Play Protect is Android&\#x27;s built-in malware defense, powered by machine learning and running automatic daily scans of apps on the device; it can block installations, disable apps, and strip permissions when it identifies potentially harmful applications \(PHAs\). Because it is baked into Google Mobile Services, it is the most widely deployed mobile threat protection service in the world. Input methods \(IMEs\) are inherently privileged software that handles all keystrokes, and Chinese third-party keyboards have historically requested broad permission sets, making them a frequent subject of privacy scrutiny. Preinstalled OEM customizations ship outside the Play Store and therefore do not go through Google&\#x27;s Play policy review process.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.google.com/android/play-protect?hl=zh-cn">Play Protect | Google for Developers</a></li>
<li><a href="https://developers.google.com/android/play-protect/cloud-based-protections?hl=zh-cn">云端保护 | Play Protect | Google for Developers</a></li>

</ul>
</details>

**Tags**: `#mobile security`, `#privacy`, `#Android`, `#Play Protect`, `#Sogou`

---

<a id="item-4"></a>
## [Tesla to Build In-House AI Maps, Debuting With FSD v15](https://www.digitaltoday.co.kr/en/view/118497/tesla-to-build-in-house-maps-and-navigation-to-address-fsd-limits) ⭐️ 6.0/10

Tesla is developing an in-house AI-based mapping and navigation system built on road data collected by its vehicle fleet, with the first deployment planned for FSD v15, where it will initially be used during the trip departure and arrival phases. Over the following months it is expected to expand into general navigation and parking, and will support voice commands and personalized route preferences. This reverses Tesla&\#x27;s long-held &quot;maps-free&quot; position on FSD and marks a meaningful strategic shift: fleet-scale map data could fix chronic weaknesses such as speed-limit recognition, parking and route selection, while giving Tesla a proprietary data asset that rivals relying on HD maps have long treated as essential. Because it is tied to FSD v15, it also gives the company a concrete milestone for its next major autonomy release. The rollout is explicitly phased — departure/arrival handling first in v15, then navigation and parking over the following months — and Tesla has not published a ship date, while earlier reporting indicates FSD v15 is targeted for late 2026 to early 2027 and will run on existing Hardware 4 computers. The item itself is a short news digest with no technical detail on how the AI maps are generated, validated, or reconciled with the vision-only driving stack.

telegram · zaihuapd · Oct 25, 10:57

**Background**: Tesla&\#x27;s FSD has historically followed a vision-only, end-to-end neural network philosophy, with Elon Musk arguing that autonomous driving should not depend on maps because maps go stale and do not scale. Most other robotaxi and autonomous-vehicle programs instead rely on HD maps — centimeter-level lane geometry, traffic signals and semantic landmarks used as a prior for localization and planning. Research literature describes map evolution in three stages: high-definition maps, lightweight \(&quot;lite&quot;\) maps, and implicit maps learned by neural networks, and Tesla&\#x27;s move suggests it now sees fleet-collected, AI-generated maps as complementary to vision rather than contradictory to it. The shift reportedly follows shareholder criticism that FSD struggles with speed-limit recognition, parking and route selection.

<details><summary>References</summary>
<ul>
<li><a href="https://gettesla.com/articles/what-tesla-has-actually-confirmed-about-fsd-v15">Tesla FSD v15: What Tesla Has Actually Confirmed So Far</a></li>
<li><a href="https://www.notateslaapp.com/news/4679/tesla-ai-chief-talks-about-whats-coming-in-fsd-v15">Tesla VP Talks About What&#x27;s Coming in FSD V15</a></li>
<li><a href="https://arxiv.org/abs/2509.12632">Maps for Autonomous Driving: Full-process Survey and Frontiers AI maps: The digital infrastructure driving autonomous ... (PDF) Maps for Autonomous Driving: Full-process Survey and ... The Role Of Maps In The Age Of Autonomous Vehicles - Forbes Autonomous Vehicle Mapping, HD Maps &amp; Localization Autonomous Vehicle HD Map Technology Landscape 2026</a></li>

</ul>
</details>

**Tags**: `#autonomous-driving`, `#tesla`, `#fsd`, `#ai-maps`, `#navigation`

---

<a id="item-5"></a>
## [GEEKCON Shanghai Drone Challenge Halted After Vendor Calls Police](https://tech.ifeng.com/c/8xSZe56UAz6) ⭐️ 6.0/10

At GEEKCON Shanghai, which closed on the evening of October 24, a drone attack-and-defense challenge reportedly prompted a leading drone manufacturer to call the police, and relevant personnel were taken away while the event was briefly suspended. The challenge required contestants to break through GPS-based no-fly restrictions and gain full control of a drone. The episode highlights the fragile boundary between white-hat vulnerability research and vendor or legal responses in China, raising the risk that security researchers could face police involvement for demonstrating flaws that manufacturers would rather not see exposed. It could push Chinese vendors and conference organizers to formalize clearer rules of engagement and coordinated disclosure channels for hardware and IoT targets. The account comes from a short, unverified report circulating on Telegram rather than a primary disclosure or official statement, and it names no specific vendor or affected drone model. The challenge itself reflects a well-known weakness class: drones rely on GNSS signals and geofencing logic that can be spoofed or jammed, and on radio links that researchers have repeatedly shown can be hijacked for full control.

telegram · zaihuapd · Oct 25, 13:29

**Background**: GEEKCON is an annual Chinese security geek event held every October 24 and long sponsored by major firms such as Huawei, Tencent Security and Ant Group. Coordinated vulnerability disclosure, also called responsible disclosure, is the practice of reporting a flaw privately to the vendor and only publishing details after a patch window has been agreed. Drone makers such as DJI implement geofencing systems that define where flight is restricted — around airports, power plants and prisons — precisely so that third parties cannot simply fly into sensitive airspace.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure - Wikipedia</a></li>
<li><a href="https://www.dji.com/global/flysafe/geo-map">Geo Zone Map - Fly Safe - DJI | DJI Official</a></li>
<li><a href="https://github.com/nicholasaleks/Awesome-Drone-Hacking">GitHub - nicholasaleks/Awesome-Drone-Hacking: A list of ...</a></li>

</ul>
</details>

**Tags**: `#security-research`, `#responsible-disclosure`, `#drone-security`, `#china-tech`, `#conference-news`

---

<a id="item-6"></a>
## [Apple Reportedly to Unveil First Touchscreen MacBook Pro on Wednesday](https://www.bloomberg.com/news/newsletters/2026-10-25/apple-to-unveil-touch-screen-macbook-pro-executive-promotions-in-box-checker) ⭐️ 6.0/10

Bloomberg reports that Apple will unveil its first touchscreen MacBook Pro on Wednesday, making it the first Mac to support touch input and to ship with an OLED display, while also adding the Dynamic Island. The machine is said to come in 14-inch and 16-inch versions, with a starting price higher than the current $2,499. This is a reversal of a position Apple executives defended for years, when they publicly argued that touchscreen laptops were ergonomically wrong, so the move signals a meaningful shift in the company&\#x27;s product philosophy. Because the MacBook Pro anchors the Mac ecosystem for professional users, a touch-enabled OLED flagship could reshape expectations for premium laptops and pressure Windows PC makers who already ship touch displays. According to the report, touch will serve as a supplement to the keyboard and trackpad rather than replacing them, and the shift is characterized as driven more by revenue and marketing considerations than by a technical breakthrough. The item stops short of technical specifics such as the touch layer, refresh rate, hinge design, or whether macOS gains new touch-oriented interface elements, and it remains an unconfirmed report rather than an official Apple announcement.

telegram · zaihuapd · Oct 25, 14:25

**Background**: OLED \(organic light-emitting diode\) is a display technology in which each pixel emits its own light from organic compounds, allowing deeper blacks and higher contrast than backlit LCD panels and enabling thinner, more flexible screens. The Dynamic Island is the pill-shaped interactive cutout Apple introduced with the iPhone 14 Pro in 2022, which expands to show live activities, alerts, and background tasks. Historically Apple kept macOS and iPadOS separate and resisted adding touch to the Mac, positioning the iPad as its touch-first computing device.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AMOLED">AMOLED - Wikipedia</a></li>
<li><a href="https://www.cnet.com/culture/internet/apple-iphone-14-pros-dynamic-island-notches-praise-jokes/">Apple iPhone&#x27;s &#x27; Dynamic Island &#x27; Feature Has Internet... - CNET</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#MacBook Pro`, `#触屏`, `#OLED`, `#硬件发布`

---