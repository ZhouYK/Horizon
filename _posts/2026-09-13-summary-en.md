---
layout: default
title: "Horizon Summary: 2026-09-13 (EN)"
date: 2026-09-13 23:03:54 +0000
lang: en
report: default
---

> From 145 items, 6 important content pieces were selected

---

1. [Homebrew 7.0.0 ships an official native macOS GUI](#item-1) ⭐️ 9.0/10
2. [Sam Altman Confirms OpenAI Will Not Go Public in 2026](#item-2) ⭐️ 7.0/10
3. [Beijing Bans Drone Ownership Citywide, Offers Buyback Before Nov 15](#item-3) ⭐️ 7.0/10
4. [CUDA&\#x27;s moat: AMD trails up to 42x on DeepSeek v4.1 Flash](#item-4) ⭐️ 7.0/10
5. [Kirin 9050 Pro review: 3D-stacked circuits boost performance and efficiency](#item-5) ⭐️ 6.0/10
6. [Leak: iOS 27 May Let Third-Party Models Like Claude Power Siri](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Homebrew 7.0.0 ships an official native macOS GUI](https://brew.sh/2026/09/13/homebrew-7.0.0/) ⭐️ 9.0/10

Homebrew announced version 7.0.0, headlined by an official native macOS graphical app alongside faster installations and upgrades, stronger sandboxing, built-in vulnerability checks and an advisory database. The release also ends support for macOS 10.15 and earlier, moves Intel Macs to Tier 3 with no new prebuilt bottles, and switches the Linux sandbox from Bubblewrap to Landlock. Homebrew is the de facto package manager for macOS developers, so a major-version change reshapes the toolchain for a huge user base: the GUI lowers the barrier for less terminal-savvy users, while tougher sandboxing and a bundled vulnerability database push security further into everyday dependency management. The platform cuts, especially Intel Macs dropping to Tier 3, will force many users to upgrade hardware or accept a degraded, community-only support path. Tier 3 means a configuration is not officially supported and may fail to work reliably even if basic installation succeeds, so Intel Mac users effectively lose new prebuilt binaries and must build from source. On Linux, the sandbox moves from Bubblewrap \(widely used by Flatpak\) to Landlock, a stackable Linux Security Module that lets unprivileged processes restrict their own filesystem access.

telegram · zaihuapd · Sep 13, 11:23

**Background**: Homebrew is a free, open-source package manager that installs command-line tools and applications on macOS \(and Linux\), colloquially known as &\#x27;brew&\#x27;. Historically it has been terminal-only, driven by the \`brew\` command and formulae written in Ruby, so an official native GUI is a notable departure from its traditional interface. Homebrew maintains formal &\#x27;support tiers&\#x27; to communicate how thoroughly a platform is tested: Tier 1 is fully supported and automated, while Tier 3 sits far outside the project&\#x27;s testing infrastructure. Sandboxing refers to restricting what processes can access on the system, a common technique for limiting the damage of a compromised or malicious package build.

<details><summary>References</summary>
<ul>
<li><a href="https://brew.sh/2026/09/13/homebrew-7.0.0/">Homebrew: 7.0.0</a></li>
<li><a href="https://docs.brew.sh/Support-Tiers">Homebrew Documentation: Support Tiers</a></li>
<li><a href="https://landlock.io/">Landlock : the Linux sandboxing mechanism</a></li>

</ul>
</details>

**Tags**: `#Homebrew`, `#package-manager`, `#macOS`, `#release`, `#security`

---

<a id="item-2"></a>
## [Sam Altman Confirms OpenAI Will Not Go Public in 2026](https://fortune.com/2026/09/12/sam-altman-openai-ipo-delay-ill-advised-moment-safety-concerns/) ⭐️ 7.0/10

OpenAI CEO Sam Altman confirmed that the company will not hold an IPO in 2026, saying that going public now would be ill-advised given current AI safety concerns and that the company will wait until the business and the broader social environment are ready. He added that OpenAI still has substantial safety and alignment work to complete and called for stronger cooperation between AI companies and governments. An explicit delay from the world&\#x27;s most prominent AI lab sets a cautionary tone for the whole sector, where investor expectations have been building around a wave of AI IPOs. It also ties capital-market timing directly to safety and alignment maturity, suggesting that frontier labs may be judged on governance readiness rather than growth alone, affecting employees, investors and partners holding illiquid stakes. Altman framed the decision as a matter of timing rather than a permanent rejection of going public, indicating an IPO would follow once the business and the social environment are prepared. The specific safety and alignment work still outstanding, or any target date beyond 2026, was not disclosed.

telegram · zaihuapd · Sep 13, 01:14

**Background**: An IPO, or initial public offering, is the process by which a privately held company sells shares to the public and lists on a stock exchange, giving early investors and employees a way to convert their stakes into cash while subjecting the firm to public reporting and shareholder pressure. OpenAI is one of the leading developers of large AI models and has been backed by major corporate investors; its unusual governance history, which began as a nonprofit, makes any listing a complicated and closely watched question for the industry.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#IPO`, `#AI safety`, `#Sam Altman`, `#industry news`

---

<a id="item-3"></a>
## [Beijing Bans Drone Ownership Citywide, Offers Buyback Before Nov 15](https://pc.bjd.com.cn/detail?id=s6aa5e790e4b039a8e2f101cd) ⭐️ 7.0/10

Beijing&\#x27;s 16th Municipal People&\#x27;s Congress Standing Committee approved a revised version of the 《北京市无人驾驶航空器管理规定》\(Beijing Regulations on the Administration of Unmanned Aircraft\), which designates the entire city as controlled airspace for unmanned aircraft, bans flying, and prohibits possessing, storing, or transporting drones and their core components into the municipality, effective November 15, 2026. To help residents dispose of existing equipment legally, the city opened three channels — on-site buyback, scrapping/recycling, and shipping out of the city — alongside a self-carry-out option, with tiered subsidies. This is one of the strictest drone rules adopted anywhere in China: it does not merely restrict flying but effectively outlaws private ownership and storage of drones and core components across an entire megacity. It directly affects hobbyists, commercial operators, aerial-photography businesses and the consumer drone supply chain — notably market leader DJI — and may set a precedent other Chinese cities follow. The subsidy is tiered by disposal date: from September 12 to October 31 the buyback subsidy is 30% of the transaction price with a cap of 3,000 yuan per unit, dropping to 15% with a 1,500 yuan cap from November 1 to 14. The text states the regulation takes effect on November 15, 2026, and it also covers core components, not just complete aircraft, so spare parts and key modules fall under the same possession and transport ban.

telegram · zaihuapd · Sep 13, 02:07

**Background**: China introduced the 《无人驾驶航空器飞行管理暂行条例》\(Interim Regulations on the Flight Management of Unmanned Aircraft\) in 2024, creating a national framework with real-name registration and a distinction between controlled airspace and non-controlled airspace, where flights in controlled airspace generally require prior approval. Beijing had already imposed tight restrictions around Tiananmen, the central axis and other sensitive zones; the revised municipal rule escalates this to a blanket citywide controlled-airspace designation plus ownership restrictions. In practice, &quot;controlled airspace&quot; means a drone cannot legally take off there without authorization, and combining that with a possession ban removes the usual assumption that owning a drone is legal as long as you do not fly it.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E5%B8%82%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6%E8%88%AA%E7%A9%BA%E5%99%A8%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A/67542534">北京市无人驾驶航空器管理规定_百度百科</a></li>
<li><a href="https://www.gov.cn/zhengce/content/202306/content_6888799.htm">无人驾驶航空器飞行管理暂行条例_航天、航空_中国政府网</a></li>
<li><a href="https://www.bjrd.gov.cn/zyfb/202603/t20260327_4568482.html">北京市无人驾驶航空器管理规定_重要发布_北京市人民代表大会常务委员...</a></li>

</ul>
</details>

**Tags**: `#drones`, `#regulation`, `#China policy`, `#UAV`, `#airspace`

---

<a id="item-4"></a>
## [CUDA&\#x27;s moat: AMD trails up to 42x on DeepSeek v4.1 Flash](https://x.com/SemiAnalysis_/status/2098618867035557984) ⭐️ 7.0/10

SemiAnalysis reports that AMD&\#x27;s DeepSeek v4.1 Flash container image shipped two days after CUDA-based vLLM support was available, and that it delivers up to 42x worse performance-per-dollar than NVIDIA B200/B300 and up to 14.8x worse than H200. The image works out of the box, but the gap is purely a software-optimization deficit rather than a hardware limitation. The result quantifies the practical cost of AMD&\#x27;s software ecosystem gap for a fast-moving LLM workload, showing that raw accelerator specs matter less than day-one framework optimization. For anyone planning inference hardware or stack budgets, it means AMD can look competitive on paper yet be far more expensive per unit of served throughput until its ROCm and framework support catches up. The comparison is expressed in performance-per-dollar rather than raw latency or throughput, so it folds in both GPU price and serving efficiency; the 42x figure applies to Blackwell B200/B300 while the 14.8x figure applies to the older Hopper H200. The crucial caveat is timing: AMD&\#x27;s image still worked immediately, so the deficit reflects optimization depth \(kernel tuning, quantization, batching\) rather than missing functionality.

telegram · zaihuapd · Sep 13, 05:55

**Background**: CUDA is NVIDIA&\#x27;s proprietary parallel-computing platform, and its roughly 6 million developer ecosystem means new model architectures are typically optimized on NVIDIA hardware on day one. vLLM is an open-source LLM inference and serving framework, originally from UC Berkeley&\#x27;s Sky Computing Lab, built around PagedAttention for KV-cache memory management, plus continuous batching and OpenAI-compatible APIs. DeepSeek v4.1 Flash is the latest fast-serving model release from Chinese AI lab DeepSeek, and getting an efficient serving image out for it quickly is a test of any vendor&\#x27;s software stack. AMD&\#x27;s equivalent stack is ROCm, which has historically lagged CUDA in framework coverage and kernel maturity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek-V4.1-Flash">DeepSeek-V4.1-Flash</a></li>
<li><a href="https://www.spheron.network/blog/mi355x-vs-h200-a-kernel-level-attention-benchmark-2026/">AMD vs NVIDIA Kernel Level Benchmark 2026: MI355X vs H200</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#AMD`, `#LLM Inference`, `#vLLM`, `#Hardware Performance`

---

<a id="item-5"></a>
## [Kirin 9050 Pro review: 3D-stacked circuits boost performance and efficiency](https://www.bilibili.com/video/BV1HEYv6XETo) ⭐️ 6.0/10

A short review summary claims Huawei&\#x27;s Kirin 9050 Pro uses microscopic 3D-stacked circuitry, with its 9-core/16-thread CPU consuming over 30% less power than the previous generation at the same 2.75 GHz clock, while the 3.1 GHz peak frequency shows no significant power increase. The Maleoon 955 GPU is said to deliver nearly 40% higher 3DMark scores, the NPU measures 67.7 TOPS in INT8, and the Mate XT 2 reportedly reaches Snapdragon 8 Elite-class gaming performance in three demanding mobile titles. If accurate, this would make the Kirin 9050 Pro one of the first mobile SoCs to ship a 3D-stacked circuit design, a packaging approach largely confined to memory and chiplet products in this class, potentially letting Huawei close the performance-per-watt gap with Qualcomm&\#x27;s flagship Snapdragon 8 Elite despite constrained access to advanced foundry nodes. It also signals that Huawei&\#x27;s in-house Maleoon GPU and NPU lines are maturing quickly, which matters for the competitive balance in China&\#x27;s premium smartphone market. The report provides no primary benchmark data, test methodology, or independent verification, only aggregate figures such as &gt;30% power reduction at equal clock, ~40% GPU uplift, and 67.7 TOPS INT8, and it is a brief repost of a bilibili review rather than a full technical analysis. The 3D-stacking claim is also notable because stacked dies typically require through-silicon vias \(TSVs\) or Cu-Cu bonding and raise thermal management and manufacturing-yield concerns in a power- and heat-constrained phone form factor.

telegram · zaihuapd · Sep 13, 13:22

**Background**: A 3D integrated circuit is a chip built by stacking multiple dies vertically and connecting them with through-silicon vias or Cu-Cu bonds, which shortens interconnect distances and can improve bandwidth and energy efficiency compared with a flat layout. Huawei&\#x27;s Kirin chips are designed by HiSilicon and use the in-house Maleoon GPU architecture, which replaced Arm&\#x27;s Mali graphics in the Kirin 9000S generation. INT8 is an 8-bit integer quantization format widely used in AI inference because it cuts memory and compute cost with limited accuracy loss, which is why NPU throughput is often quoted in INT8 TOPS rather than raw floating-point numbers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Three-dimensional_integrated_circuit">Three-dimensional integrated circuit - Wikipedia</a></li>
<li><a href="https://www.notebookcheck.net/HiSilicon-Maleoon-910-Benchmarks-and-Specs.803657.0.html">HiSilicon Maleoon 910 - Benchmarks and Specs - Notebookcheck An exploration of Huawei&#x27;s self-developed Maleoon 910 GPU ... Huawei&#x27;s self-developed GPU rookie Maleoon 910, what does Ma ... HiSilicon Maleoon 920 - Benchmarks and Specs - Notebookcheck Tech Huawei&#x27;s self-developed GPU killer, Ma Liang, Maleoon 910 GPU ...</a></li>
<li><a href="https://www.mathworks.com/company/technical-articles/what-is-int8-quantization-and-why-is-it-popular-for-deep-neural-networks.html">What Is int8 Quantization and Why Is It Popular for Deep ...</a></li>

</ul>
</details>

**Tags**: `#Huawei Kirin`, `#semiconductor`, `#3D stacking`, `#mobile SoC`, `#hardware benchmarks`

---

<a id="item-6"></a>
## [Leak: iOS 27 May Let Third-Party Models Like Claude Power Siri](https://x.com/itspdfu/status/2099122424209916015) ⭐️ 6.0/10

A leak claims that iOS 27 and macOS &quot;Golden Gate&quot; contain a private App Intents &quot;Model Delegation API&quot; that would let apps add Siri extensions and replace Siri&\#x27;s AI backend with third-party models such as Claude. The post says the capability is gated behind a private com.apple.developer.model-delegation entitlement. If accurate, this would mark the first time Apple opens Siri&\#x27;s intelligence layer to competing large language models, potentially letting providers such as Anthropic, OpenAI or Google plug directly into Apple&\#x27;s assistant instead of only through Apple Intelligence. That would reshape how AI assistants compete on Apple platforms and could give third-party model vendors access to hundreds of millions of iPhone and Mac users. The leak says Claude would show up in Siri&\#x27;s &quot;Ask…&quot; menu and could generate files such as CSV, while system-level actions like setting a reminder are handed back to Siri for execution. Since the described entitlement is private, ordinary developers cannot use it today, and the claim remains a single unverified post with no corroboration or technical documentation.

telegram · zaihuapd · Sep 13, 13:48

**Background**: App Intents is Apple&\#x27;s framework that lets an app describe its actions and content to the system so they can surface in Siri, Spotlight, Shortcuts and widgets. Siri is Apple&\#x27;s voice assistant, traditionally powered by Apple&\#x27;s own models, though Apple Intelligence has also routed some requests to ChatGPT with user consent. A &quot;model delegation&quot; API would essentially act as a routing layer that lets an app declare an external model as the handler for certain assistant queries, which is why the rumoured entitlement name is drawing attention.

<details><summary>References</summary>
<ul>
<li><a href="https://forums.macrumors.com/threads/apples-rumored-siri-extensions-quietly-shipped-in-macos-27-i-got-ask-claude-working.2486206/">Apple ’s rumored Siri Extensions quietly shipped... | MacRumors Forums</a></li>
<li><a href="https://developer.apple.com/documentation/appintents/">App Intents | Apple Developer Documentation</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Siri`, `#LLM Integration`, `#iOS`, `#Rumors`

---