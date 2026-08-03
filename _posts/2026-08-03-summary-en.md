---
layout: default
title: "Horizon Summary: 2026-08-03 (EN)"
date: 2026-08-03
lang: en
report: default
---

> From 348 items, 6 important content pieces were selected

---

1. [AI Chip Count Set to Double Every 9 Months, Reaching 200 Million by 2028](#item-1) ⭐️ 7.0/10
2. [Apple Caps Bug Reports as AI-Generated Submissions Swamp System](#item-2) ⭐️ 7.0/10
3. [Chinese Police AI Trains to Spot Bitcoin Laundering with Near 90% Accuracy](#item-3) ⭐️ 7.0/10
4. [WeChat Adds Crowdsourced Shaking Intensity and Location Updates to Earthquake Alerts](#item-4) ⭐️ 6.0/10
5. [AMD Zen 6 Rumored to Add Per-Core Optimizations to Reduce Game Microstutters](#item-5) ⭐️ 6.0/10
6. [US States Move to Repeal Data Center Tax Breaks, Raising AI Infrastructure Costs](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [AI Chip Count Set to Double Every 9 Months, Reaching 200 Million by 2028](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html) ⭐️ 7.0/10

According to Epoch AI, the global number of AI chips is projected to double every nine months, rising from roughly 20 million today to about 200 million by the end of 2028 — a tenfold increase. IDC separately forecasts that global AI infrastructure investment will exceed $1 trillion in 2029, up from $318 billion last year. This projection underscores how deeply the AI boom is reshaping the semiconductor and data-center industries, with trillion-dollar spending implications. It also highlights geopolitical stakes — the U.S. controls about 80% of global AI compute — and raises urgent questions about energy consumption and whether infrastructure spending will outpace actual profitability. Epoch AI estimates there are currently about 20 million AI chips worldwide, with the count doubling every nine months; Google alone is believed to have four times as many AI chips as all Chinese companies combined. Economists warn that the current pace of spending may exceed near-term profits, and that historical infrastructure booms have often ended in bubble bursts.

telegram · zaihuapd · Aug 2, 01:01

**Background**: The boom is driven by &\#x27;scaling laws&\#x27; — empirical findings, popularized by OpenAI&\#x27;s 2020 Kaplan et al. paper, that AI model performance improves predictably as compute, data, and parameters grow. Epoch AI is a research institute that tracks and forecasts AI compute trends for policymakers. Massive data-center construction is needed to train and run increasingly large models, but it also drives up electricity prices and triggers environmental debate.

<details><summary>References</summary>
<ul>
<li><a href="https://epoch.ai/">Epoch AI</a></li>
<li><a href="https://ai.plainenglish.io/scaling-laws-in-ai-why-bigger-models-keep-winning-60d6ecc0f360">Scaling Laws in AI : Why Bigger Models Keep Winning</a></li>
<li><a href="https://epochai.substack.com/about">About - Epoch AI</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#semiconductors`, `#data centers`, `#scaling laws`, `#industry analysis`

---

<a id="item-2"></a>
## [Apple Caps Bug Reports as AI-Generated Submissions Swamp System](https://www.ft.com/content/4532122d-90f2-4433-9df6-ca99d8a141d2?syn-25a6b1a6=1) ⭐️ 7.0/10

In June, Apple quietly limited the number of concurrent vulnerability reports a researcher can submit, adding a 30-day cooldown, to stem a flood of low-quality, AI-generated security submissions. Italian startup Bynario says it found more than 50 macOS vulnerabilities with ChatGPT in three weeks—including a privilege-escalation chain—but was blocked by the new caps; Apple later reached out and reviewed its findings. This highlights AI&\#x27;s double-edged role in cybersecurity: it lets researchers find more bugs cheaply, but also overwhelms human-run bug bounty programs with noise. It also shows Apple—and by extension the whole industry—shifting policies and using AI tools themselves to keep pace, with this week&\#x27;s patch volume roughly five times the usual level. Bynario&\#x27;s findings reportedly included a privilege-escalation chain that could let an attacker take full control of a Mac, yet the company could not file it under the new limits. Apple says it has reviewed Bynario&\#x27;s submissions and is also deploying AI defense tools, crediting Anthropic and OpenAI&\#x27;s models for helping discover vulnerabilities fixed in the latest security update.

telegram · zaihuapd · Aug 2, 05:50

**Background**: Bug bounty programs pay researchers to report vulnerabilities before attackers exploit them. Privilege escalation is a common attack step where low-level access is expanded to gain administrative or root control. AI-assisted vulnerability discovery is surging, with industry reports showing record CVE volumes and vendors attributing the jump to LLM-based analysis and fuzzing tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Privilege_escalation">Privilege escalation - Wikipedia</a></li>
<li><a href="https://www.beyondtrust.com/blog/entry/privilege-escalation-attack-defense-explained">What Is Privilege Escalation? Attacks &amp; Defense Guide | BeyondTrust</a></li>
<li><a href="https://www.vulncheck.com/blog/ai-assisted-vulnerability-discovery">The First CVE Wave: Signs That AI-Assisted Vulnerability ...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AI安全`, `#漏洞报告`, `#安全政策`, `#Bug Bounty`

---

<a id="item-3"></a>
## [Chinese Police AI Trains to Spot Bitcoin Laundering with Near 90% Accuracy](https://www.scmp.com/news/china/science/article/3362493/chinese-police-ai-algorithm-tracks-bitcoin-money-laundering-90-accuracy) ⭐️ 7.0/10

Researchers from People&\#x27;s Public Security University of China developed an AI framework combining memory modules and large language models to detect illegal cryptocurrency transactions. The system identifies Bitcoin money laundering with nearly 90% accuracy, as published in the May issue of peer-reviewed Journal of Intelligence. This marks a notable application of LLMs and memory modules to blockchain forensics, giving regulators an interpretable and scalable tool for tracing anonymous cross-border crypto laundering. It also reflects an intensified Chinese crackdown on virtual currency-linked financial crime. The framework is designed for explainability and generalizability, according to the research team. Supreme People&\#x27;s Procuratorate data cited in the report shows prosecutors indicted 3,259 suspects in virtual currency and underground bank money laundering cases nationwide in 2025.

telegram · zaihuapd · Aug 2, 08:22

**Background**: Large language models \(LLMs\) are AI systems trained on vast text data that can understand and generate human-like text; memory modules let such models retain and retrieve information over long sequences. In blockchain forensics, Bitcoin transactions are recorded on a public ledger, so AI can analyze transaction patterns to flag suspicious activity despite pseudonymity. This work is part of a broader trend using machine learning and explainable AI for cryptocurrency investigations and compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nationpress.com/sciencetech/china-ai-flags-bitcoin-laundering-at-90-percent">China police AI detects Bitcoin laundering at 90% accuracy</a></li>
<li><a href="https://bingx.com/en/flash-news/post/china-researchers-report-ai-tool-spots-illegal-bitcoin-transactions-with-nearly-accuracy-journal-of-intelligence-study-says">Chinese researchers build AI tool to trace Bitcoin-linked ...</a></li>
<li><a href="https://communities.springernature.com/posts/decoding-the-dark-ai-and-ml-in-the-dark-web-cybercrime-and-cryptocurrency-forensics">Decoding the dark: AI and ML in the dark web cybercrime and cryptocurrency forensics | Research Communities by Springer Nature</a></li>

</ul>
</details>

**Tags**: `#AI`, `#blockchain`, `#money laundering`, `#LLM`, `#law enforcement`

---

<a id="item-4"></a>
## [WeChat Adds Crowdsourced Shaking Intensity and Location Updates to Earthquake Alerts](https://news.cctv.com/2026/08/02/ARTIrixWuCmLM2TuZigvQ8rX260802.shtml) ⭐️ 6.0/10

On August 2, 2026, WeChat launched two new earthquake early warning features: &quot;Shaking Intensity Convergence&quot; \(震感汇聚\) and &quot;Location Update&quot; \(位置更新\). The former lets users report felt shaking after an earthquake via a mini-program, generating a shaking intensity distribution map; the latter prompts users to update their alert subscription location when traveling. This is significant because it turns WeChat&\#x27;s existing 60 million-subscriber earthquake alert service into a participatory sensing network, improving shake map accuracy while making alerts location-aware. It also demonstrates how a mainstream messaging platform can integrate crowdsourced disaster response features at national scale. Since launching in August 2024, WeChat&\#x27;s national earthquake early warning service has issued more than 700 alerts and has over 60 million subscribers; combined with OS-level warnings from Huawei, Xiaomi, and vivo, the public warning system reaches more than 400 million users. The new features rely on mini-program interaction and algorithmic processing of user-reported shaking intensity.

telegram · zaihuapd · Aug 2, 10:16

**Background**: Earthquake early warning systems detect fast P-waves to issue alerts before stronger shaking arrives, but shaking intensity varies by location due to distance, rupture direction, and local geology. Crowdsourced platforms like the USGS &quot;Did You Feel It?&quot; system collect individual shaking reports to quickly map damage extent, a concept WeChat&\#x27;s new &quot;Shaking Intensity Convergence&quot; now applies in China. Location-aware alerts matter because warning time and intensity differ between a user&\#x27;s home region and the area where they currently are.

<details><summary>References</summary>
<ul>
<li><a href="https://earthquake.usgs.gov/data/dyfi/">Did You Feel It? - USGS Earthquake Hazards Program</a></li>
<li><a href="https://en.wikipedia.org/wiki/Earthquake_early_warning_system">Earthquake early warning system - Wikipedia</a></li>
<li><a href="https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity">Earthquake Magnitude, Energy Release, and Shaking Intensity | U.S. Geological Survey</a></li>

</ul>
</details>

**Tags**: `#earthquake warning`, `#crowdsourcing`, `#emergency response`, `#WeChat`, `#public safety`

---

<a id="item-5"></a>
## [AMD Zen 6 Rumored to Add Per-Core Optimizations to Reduce Game Microstutters](https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets) ⭐️ 6.0/10

According to a rumor from Tom&\#x27;s Hardware, AMD&\#x27;s next-generation Zen 6 processors will introduce several per-core optimizations, including improved CPPC Performance Priority, FloorPerf, and HighestFreq, to reduce microstutters and improve 1% low FPS in games. The featured improvements are not yet officially confirmed. If the rumor holds, these optimizations could substantially improve gaming smoothness by more intelligently allocating power, thermals, and thread scheduling across cores. This would benefit gamers and could strengthen AMD&\#x27;s competitive position in the CPU market. The rumored features include FloorPerf to lower background core frequency during throttling, HighestFreq to keep the core running the game&\#x27;s main thread at its highest frequency, per-core EPP boost, and PQOS with a new IBS memory analyzer to limit background tasks&\#x27; use of memory bandwidth and L3 cache. Some features may only be available on high-end or mobile products.

telegram · zaihuapd · Aug 2, 14:05

**Background**: AMD&\#x27;s Zen architecture powers Ryzen desktop and mobile processors. CPPC \(Collaborative Power and Performance Control\) is an interface that allows the operating system to communicate with CPU power management to improve scheduling decisions. Microstutters are small frame-time hitches that harm perceived smoothness in games, while 1% lows refer to the average frame time of the slowest 1% of frames, a metric used to gauge performance consistency. These optimizations are part of AMD&\#x27;s ongoing efforts to refine scheduling and power management.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets">AMD &#x27;s upcoming Zen 6 processors could fix... | Tom&#x27;s Hardware</a></li>
<li><a href="https://wccftech.com/amd-new-cppc-highestfreq-ends-os-frequency-guesswork-letting-os-see-true-ryzen-boost-clocks/">AMD&#x27;s New CPPC HighestFreq Ends OS Frequency Guesswork ...</a></li>
<li><a href="https://docs.amd.com/api/khub/documents/QHwot6p6UzlLz7yGEmfENw/content">AMD64 Zen 6 Platform Quality of Service (PQOS) Extensions</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Zen 6`, `#CPU`, `#Gaming Performance`, `#Hardware`

---

<a id="item-6"></a>
## [US States Move to Repeal Data Center Tax Breaks, Raising AI Infrastructure Costs](https://theinformation.com/articles/exclusive-data-center-costs-set-rise-u-s-states-move-repeal-tax-breaks) ⭐️ 6.0/10

Several US states are moving to repeal or tighten tax incentives for data centers, a change reported exclusively by The Information. The shift could raise costs for AI infrastructure and influence where future data centers are built. The proposed repeal could significantly increase the cost of building and operating data centers, which are the physical backbone of AI and cloud computing. This may affect the economics of AI deployment for major tech companies and alter the geographic distribution of new infrastructure. The tax breaks previously helped attract data center investment by exempting purchases of servers, electricity, and other costs. Some local governments are already tightening abatements, such as a Michigan township that recently approved a much smaller tax break for a $43 billion Oracle-OpenAI data center by using a lower property valuation.

telegram · zaihuapd · Aug 3, 00:42

**Background**: Data centers are physical facilities housing servers and IT equipment, and hyperscale data centers — massive facilities used by cloud providers like AWS and Microsoft Azure — consume enormous amounts of electricity and water. Many US states and localities have long offered tax abatements to attract these projects, but the rapid growth of AI-driven data centers has intensified concerns over rising energy demand, infrastructure strain, and lost tax revenue, prompting some policymakers to reconsider the incentives.

<details><summary>References</summary>
<ul>
<li><a href="https://goodjobsfirst.org/wp-content/uploads/2026/04/Data-Center-Tax-Abatements-Why-States-and-Localities-Must-Disclose-These-Soaring-Revenue-Losses.pdf">Data Center Tax Abatements</a></li>
<li><a href="https://www.mlive.com/news/ann-arbor/2026/07/township-near-ann-arbor-approves-much-smaller-tax-break-for-43b-oracle-openai-data-center.html">Township near Ann Arbor approves much smaller tax ... - mlive.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperscale_data_center">Hyperscale data center</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#tax policy`, `#cloud computing`, `#economics`

---