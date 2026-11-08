---
layout: default
title: "Horizon Summary: 2026-11-08 (EN)"
date: 2026-11-08 23:03:12 +0000
lang: en
report: ai
---

> From 132 items, 7 important content pieces were selected

---

1. [SQLite parse\_number\(\) extension: C vs Rust on speed, size, and complexity](#item-1) ⭐️ 7.0/10
2. [Nvidia Probes Reported Chinese Intelligence Targeting of CEO Jensen Huang](#item-2) ⭐️ 7.0/10
3. [Report: Licensed Nvidia Chip Buyers in China Have Empty Offices, Military Ties](#item-3) ⭐️ 7.0/10
4. [Homelabber runs 2.8T-parameter Kimi K3 on CPU using second-gen Optane, warns of DRAM-burning heat](#item-4) ⭐️ 7.0/10
5. [AP: U.S. AI Safety Institute staff now report to the White House, sparking independence fears](#item-5) ⭐️ 6.0/10
6. [AI Predicts Thousands of Mitochondrial Protein Interactions Tied to Disease](#item-6) ⭐️ 6.0/10
7. [RBA Speech Asks What Happens to the Economy as AI &\#x27;Intelligence&\#x27; Gets Cheaper](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [SQLite parse\_number\(\) extension: C vs Rust on speed, size, and complexity](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 7.0/10

Simon Willison published a research report comparing a SQLite loadable extension that adds a parse\_number\(\) function — one that turns strings like -$1,234.56 or &\#x27;12.5%&\#x27; into summable, sortable numbers — implemented in both C and Rust. After an initial version where the Rust builds \(321 KB with Rusqlite, 298 KB with sqlite-loadable-rs\) were far larger but faster than the 14 KB C build, he prompted Claude to write a hand-rolled C number parser that ended up beating both Rust versions. The experiment gives a concrete, reproducible data point for the long-running C-versus-Rust debate: Rust&\#x27;s ergonomics and safety frameworks cost hundreds of kilobytes of binary size, but the performance gap can be closed — or reversed — with careful C. For developers shipping SQLite extensions, it shows both that loadable extensions are a practical way to push custom parsing logic into the database, and that language choice should hinge on measurement rather than assumption. Measured as net cost per row over 2 million rows, the first C version \(using strtod\) cost 67 ns on mixed data, 25 ns on integers only and 106 ns on decimals only; the rewritten C parser dropped that to 19/16/18 ns, versus 46/36/55 ns for Rusqlite and 41/32/47 ns for sqlite-loadable-rs. The initial Rust advantage came from its string-to-float conversion being roughly twice as fast as C&\#x27;s strtod, and the extension returns NULL for any input it cannot parse.

rss · Simon Willison · Nov 8, 22:26

**Background**: SQLite supports run-time loadable extensions: shared libraries that are loaded with sqlite3\_load\_extension\(\) and register new functions, virtual tables, or VFSes through an init entry point. Application-defined SQL functions are normally registered via the sqlite3\_create\_function\(\) family of C APIs, which is why a custom scalar function like parse\_number\(\) is a natural first extension project. Rust developers rarely call that C API directly; they use wrappers such as Rusqlite or sqlite-loadable-rs, which add convenience and safety at the cost of extra compiled code. The C standard library&\#x27;s strtod\(\) is the traditional way to convert text to a double, and its speed relative to Rust&\#x27;s float parsing is the crux of this comparison.

<details><summary>References</summary>
<ul>
<li><a href="https://sqlite.org/loadext.html">Run-Time Loadable Extensions - SQLite</a></li>
<li><a href="https://github.com/asg017/sqlite-loadable-rs">GitHub - asg017/sqlite-loadable-rs: A framework for writing ...</a></li>
<li><a href="https://www.sqlite.org/appfunc.html">Application-Defined SQL Functions</a></li>

</ul>
</details>

**Tags**: `#SQLite`, `#Rust`, `#C`, `#extensions`, `#performance`

---

<a id="item-2"></a>
## [Nvidia Probes Reported Chinese Intelligence Targeting of CEO Jensen Huang](https://news.google.com/rss/articles/CBMilAFBVV95cUxQaHdZZkpucG9aOVF5R2JPeHljWV85XzlhbUxnbUREYWlKQzBiR1UzeWxwaF9EMnpDajI1aXlmMlo0aENzeGdyRzJDSEtJR0xVanhFSkN3bXE0R1FYV2VWZHdIV1A1MmFlczN4VnRZcVZ5QV9xdUlxZXVlZVl3eHRqVWxsVmE1dktHZzdnelB0ZjUwejJj?oc=5) ⭐️ 7.0/10

The New York Times reported that Nvidia has opened an investigation into CEO Jensen Huang&\#x27;s relationship with a person alleged to be a Chinese spy, with NBC News framing the story as Nvidia probing reports that Huang was targeted by Chinese intelligence. Several other outlets, including The Detroit News, quickly picked up the report, though Nvidia and Huang have not issued a public statement. Nvidia is the world&\#x27;s most valuable chipmaker and the linchpin of the U.S. AI buildout, so a national-security controversy around its CEO could touch export-control debates, government contracts, and investor confidence in the company&\#x27;s leadership. It also lands amid already heightened U.S.-China tensions over semiconductors, raising the political stakes well beyond a routine corporate matter. Details remain sparse: available coverage consists largely of headlines, with no disclosed scope, timeline, or findings from the probe and no confirmation of who the individual in question is or what the relationship involved. It is also unclear whether investigators believe Huang was a witting participant or an unwitting target of a foreign intelligence or talent-recruitment effort.

google\_news · The New York Times · Nov 8, 22:05

**Background**: Jensen Huang co-founded Nvidia in 1993 and has led it as CEO since, turning it from a graphics-card maker into the dominant supplier of the GPUs that power modern AI training and inference. Because those chips are central to the U.S.-China technology rivalry, Nvidia has been at the center of successive American export controls on advanced semiconductors, and U.S. officials have repeatedly warned about Chinese talent-recruitment and influence programs aimed at people in strategic industries. When allegations of this kind surface, boards typically retain outside counsel or a compliance function to review whether company policies, disclosure obligations, or security protocols were breached.

**Tags**: `#Nvidia`, `#Jensen Huang`, `#national security`, `#semiconductors`, `#corporate investigation`

---

<a id="item-3"></a>
## [Report: Licensed Nvidia Chip Buyers in China Have Empty Offices, Military Ties](https://news.google.com/rss/articles/CBMi6wJBVV95cUxONjlUN25OeGR5Y3ZBZGFzYU5ZR3ExemVBSENRSzRwcUdDUXlIV3JTZEZUcHpMaGZtaktka3p1WUQxNGU3WTZmV1VuS3R3RUFyWW8xZGRhaTZxQTB5N2F1VnRPS1ljSHJrQl9QeWRzVjhuckZrMTlLQm91YjI5S2ZPb1E1TTl3ZzNGbHFrX091ODBjVWlSNkphb3dmMHZrRDRLRGxmZXlQNEQ2RDJjUVVXQlJjVGVNOW90cVpWZHhhNTB2azJKLXdtRFdjdENrSVB3Sk8xcXRBTUM3V3B2WEcxY2M4clZZRlV2T2ljVlhtY0NNWkVCR0prbGR0NmpCUTRrZGw1Smx4eWhDUEJya3ozR1p4b2Y4bjN6MThQTGNUYjdPY25qUE5ubUNrSjQ1TDhseXpMSjluVEZ2Vkc0NjdWcnBVUGFZQnVxVXpzMlhhbExNOVc2SDFXV0VEeDJ0LTQwOWdBQXBYcHFqMUE?oc=5) ⭐️ 7.0/10

A Tom&\#x27;s Hardware investigation found that two Chinese companies granted licenses to buy restricted Nvidia AI chips have empty offices, unknown addresses, and apparent ties to Chinese military suppliers already under U.S. sanctions. The findings raise questions about whether U.S. export-control licensing vetting can be circumvented, increasing the risk that advanced AI chips intended for civil use could be diverted to military-linked entities. The report is based on an investigation rather than technical testing; it identifies shell-like corporate footprints—empty offices and undisclosed addresses—as red flags in the license-approval process for Nvidia chips banned from normal export to China.

google\_news · Tom&\#x27;s Hardware · Nov 8, 13:00

**Background**: Since 2022, the U.S. has restricted exports of advanced AI chips such as Nvidia&\#x27;s A100 and H100 to China, requiring licenses to prevent military and surveillance uses. Nvidia later created the China-specific H20 to stay under U.S. performance thresholds, and Washington periodically adjusts licensing policy. U.S. agencies also maintain lists of Chinese military-linked companies, which can complicate approvals for buyers with such ties.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/world/2022/sep/01/us-blocks-sales-of-some-ai-chips-to-china-as-tech-crackdown-intensifies">US blocks sales of some AI chips to China as tech... | The Guardian</a></li>
<li><a href="https://www.nytimes.com/2025/04/15/technology/nvidia-h20-chip-china-restrictions.html">Nvidia Says U.S. Will Restrict Sales of More of Its A.I. Chips to China ...</a></li>
<li><a href="https://sanctionsnews.bakermckenzie.com/us-government-updates-1260h-list-of-chinese-military-companies/">US Government Updates 1260H List of Chinese Military ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI chips`, `#export controls`, `#China`, `#sanctions`

---

<a id="item-4"></a>
## [Homelabber runs 2.8T-parameter Kimi K3 on CPU using second-gen Optane, warns of DRAM-burning heat](https://news.google.com/rss/articles/CBMihwNBVV95cUxOVmZreDJxdElUVnFWT3lOV24tNGxvRi1sQkd0ZFdfSkx1OWRZX2VXTUg2MUtOV0N2Z3A3TTFYZ3RTVVZHczdMbUwtOWhzU0RQWWUwaHN1ZkNhLTV4ZTlOcW5HNVg3cUQ5M3F1UVhETDdYdHQ3V2RTMFcxb093OUxSWHJXQUlJUTFkUEUwMU5TSE9sWWZTQUlWNVJkWHBpNVdMNi1FZm51aHpnNDIycENVWmdkZm5xUmlSYXhuMEV5WHJfcVBNMmQ4MTYzX3dNeXRCc1Y3YjBsVmhyanZRSHh4c2FfaWluX3FRLWdjQ3liQ3BmMFhoaWY5T3N3WmMyUnBPWjhvdEZvTFpQRW9UY3ZyY1pEM2MyZ25haVJpWmstYzBuTkNOV3BVb184bXItdHBLd1J3dEh1b2NHX3VUMHR6cmZPSnprYWY3NnhEdmxIUnlQWm1TLTZLUExfX1NseDg0Nm1tZWIzalNWNENQc3dSSDAyTTRuekNNM2RYY2l1aWZVLVRnSWlF?oc=5) ⭐️ 7.0/10

A Reddit homelab builder reported running Moonshot AI&\#x27;s 2.8-trillion-parameter Kimi K3 model entirely on CPU using second-generation Intel Optane PMem 200 modules and a 40-core 3rd-gen Xeon Scalable processor, with no GPU for inference. The builder warned that Optane&\#x27;s extreme heat can &\#x27;burn out&\#x27; adjacent DRAM and used blower fans to keep nearby memory from melting. This shows that very large open-weight models can be made runnable on repurposed server hardware without GPUs, which is notable for cost-sensitive homelabs and for debates about AI infrastructure concentration. It also highlights a practical thermal hazard when mixing Optane persistent memory with ordinary DRAM in dense systems. The system used Intel Optane PMem 200, a 2020-era persistent-memory DIMM available in 128GB, 256GB, and 512GB capacities and rated up to 3200 MT/s on Ice Lake Xeon platforms; the builder chose it because it cost &\#x27;a fraction&\#x27; of equivalent DRAM amid high memory prices. Kimi K3 is a Mixture-of-Experts model, so despite its 2.8T total parameters only a subset is active per token, but CPU-only inference still trades throughput for capacity.

google\_news · Tom&\#x27;s Hardware · Nov 8, 12:20

**Background**: Intel Optane persistent memory is a byte-addressable non-volatile memory that fits into DDR4 DIMM slots on supported Xeon platforms, and can operate in Memory Mode \(with DRAM acting as a cache\) or App Direct mode. Intel discontinued its Optane business in 2022, but large capacities of PMem 200/300 modules remain available on the secondary market, making them attractive for memory-capacity-hungry workloads. Kimi K3, from Chinese AI startup Moonshot AI, is an open-weight Mixture-of-Experts model with 2.8 trillion total parameters, and its sparse activation pattern is what makes CPU-only inference on a machine with terabytes of Optane capacity conceivable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servethehome.com/intel-optane-dc-persistent-memory-guide-for-pmem-100-pmem-200-and-pmem-300-optane-dimms/">Intel Optane DC Persistent Memory Guide for PMem 100 PMem 200 ... Intel Optane™ Persistent Homelab Builder Runs 2.8T-Parameter AI Model on Optane Memory ... Intel® Optane™ Persistent Memory 200 Series - 2 | Performance ... Homelabber uses second-gen Optane memory sticks to run a 2.8 ...</a></li>
<li><a href="https://www.gate.com/news/detail/INTC/homelab-builder-runs-28t-parameter-ai-model-on-optane-memory-with-cpu-only-25489775">Homelab Builder Runs 2.8T-Parameter AI Model on Optane Memory ...</a></li>
<li><a href="https://en.inithtml.com/resources/kimi-k3-the-2-8-trillion-parameter-ai-model-ushering-in-a-new-era-of-frontier-intelligence/">Moonshot AI Kimi K3 Model : 2 . 8 Trillion Parameters and Architecture...</a></li>

</ul>
</details>

**Tags**: `#Optane`, `#AI inference`, `#homelab`, `#hardware cooling`, `#LLM systems`

---

<a id="item-5"></a>
## [AP: U.S. AI Safety Institute staff now report to the White House, sparking independence fears](https://news.google.com/rss/articles/CBMizwFBVV95cUxOdmZYc2w5LXZFeVMtNEtZWUR2cURFcUhqbVA4Rk5sNXZBVnlFOWdXZ3RSenBJVG5YLWwtM2hNUWcwaUo0aFVMdTNlLTdxQVRMM1k0RlBwSVJmMk1wbWRyeHdkX19nUGZ2TGhKdTl3eWxBdG10bU1iMHU1dTYxeGpYYk5rZF9JejdRbjllTGdSRW1FNUNnVHhiUzZITGxiRlk4OW95bkN6V0wwYzFWYXZFNWxkU1I2c1RLYzBMVnhlX2ZNaWUzQ3hIRDM4TzBhLXPSAdQBQVVfeXFMTnU1Q19ObTZjMTdYTHZseGk4ek1GMHNsaEs0REFFRE85Y013bzNmVU5PMXVOdk9KMWZZdUNkSlRJZ1VvN1FFdHRJY0llWmMySHJ3WThkYzFBcW1jSXhBSU1OV3cyRFZLYUxEQ09mdHRQNlllSmE3dU5TWjNWU1A2MGh4TC1rRm5lQzRiWlJOQmlNT3ZOaXphdWJ1ZXNLVmxWamNvcFdXODJlb0p3Y1VDbFlzTVdYRGZkY3ZsUHdGUGFWNXdQQnlGOThSVmNTaXhiS1NITFE?oc=5) ⭐️ 6.0/10

According to Associated Press reporting cited by PBS, staff at the U.S. center for AI safety are now reporting to the White House rather than through their prior departmental chain of command, a shift that has prompted concerns about the center&\#x27;s independence. The change moves day-to-day oversight of the government&\#x27;s main AI safety evaluation body closer to the executive office. The institute&\#x27;s credibility rests on being seen as a neutral, science-based evaluator of frontier AI models, and shifting its reporting line toward the White House could blur the line between technical assessment and political decision-making. If researchers, labs, and international counterparts perceive the body as politicized, it may weaken voluntary testing agreements and undermine the U.S. position in global AI governance debates. The reporting is attributed to AP sources rather than an announced policy document, so the precise scope of the change — whether it covers all staff, only leadership, or just coordination functions — is not fully specified, and it is unclear whether formal oversight or congressional notification requirements were involved. The center in question is the U.S. AI Safety Institute housed within the Department of Commerce&\#x27;s National Institute of Standards and Technology \(NIST\).

google\_news · PBS · Nov 8, 18:05

**Background**: The U.S. AI Safety Institute \(AISI\) was established inside NIST, part of the Department of Commerce, following the Biden administration&\#x27;s 2023 executive order on safe, secure, and trustworthy AI, and it was tasked with advancing the science of AI safety and evaluating advanced &\#x27;frontier&\#x27; models. NIST is the federal government&\#x27;s main body for developing science-based technical standards, and AISI has published draft guidance for developers on evaluating and mitigating risks from generative AI and dual-use foundation models. It also formed the TRAINS taskforce in November 2024 to assess AI risks to national security across government agencies, and it convenes the AI Safety Institute Consortium \(AISIC\) with industry and academic partners. Because AI safety institutes are meant to act as independent, technically grounded evaluators, their placement within government — and how close they sit to political leadership — is a recurring subject of debate in AI governance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_safety_institute">Artificial intelligence safety institute - Wikipedia</a></li>
<li><a href="https://www.nist.gov/document/aisi-strategic-vision-document">U.S. Artificial Intelligence Safety Institute at NIST</a></li>
<li><a href="https://www.nist.gov/news-events/news/2024/11/us-ai-safety-institute-establishes-new-us-government-taskforce-collaborate">U.S. AI Safety Institute Establishes New U.S. Government ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#US policy`, `#AI governance`, `#White House`, `#regulatory independence`

---

<a id="item-6"></a>
## [AI Predicts Thousands of Mitochondrial Protein Interactions Tied to Disease](https://news.google.com/rss/articles/CBMirgFBVV95cUxOaDBKZmdKb3dVSzJNaVBJZGo5MHl3ZHdzMW9qYnBBTUtTWllBMTlQaW43UzZDYVhPZzE1Z09OMExMNzIxWGxLcFFob011aUV4LXNxZ1R6b1VsT3dmNnpxeF9HcFE2dUJZbmFRbUZrR2k2eDJWS29UNkpPLVNPaHI0ejRTNVZ5emV4QnRrM0gtUWY4N3Z0Tm9pNVo2elpfZ1dPbG1XUGVkMEpRM3dQQlE?oc=5) ⭐️ 6.0/10

A peer-reviewed study published in Nature Communications, titled &quot;The predicted interactome of the human mitochondrial proteome,&quot; reports that researchers computationally screened every possible pairing among roughly 1,100 human mitochondrial proteins — more than 630,000 combinations — to identify likely interactions. The team repurposed AlphaFold-Multimer as a classification model, dubbed MitoMatch, to predict whether two proteins interact based on their predicted interface, producing thousands of candidate interactions with links to human disease. Pathogenic mutations have been identified in nearly 30% of the roughly 1,100 mitochondrial proteins, causing both common diseases and rare inborn errors of metabolism, so a proteome-wide interaction map gives researchers a systematic set of hypotheses instead of one-at-a-time guesses. It also shows how structure-prediction models like AlphaFold can be turned into large-scale discovery tools for the human interactome, potentially narrowing the experimental work needed to find disease mechanisms and drug targets. The interactions are computational predictions rather than experimentally confirmed bindings, so they serve as prioritized candidates that still require wet-lab validation such as co-immunoprecipitation or affinity assays. The approach hinges on converting AlphaFold-Multimer&\#x27;s structural confidence at the protein-protein interface into a binary interaction score, and its scope is bounded by the ~1,100 proteins defined as the human mitochondrial proteome.

google\_news · Bioengineer.org · Nov 8, 18:43

**Background**: Protein-protein interactions \(PPIs\) govern how cells carry out nearly every function, and mapping them is essential for understanding protein function, pathways and disease mechanisms. Experimental PPI detection at whole-proteome scale is costly and labor-intensive, so deep-learning methods such as AlphaFold and its derivatives — which predict the 3D structure of proteins and protein complexes — have come to dominate computational PPI modeling. Mitochondria are the cell&\#x27;s energy-producing organelles and are unusual in that most of their proteins are encoded by nuclear genes and imported from the cytosol, making a complete parts list and interaction map especially useful.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41467-026-77112-z">The predicted interactome of the human mitochondrial proteome</a></li>
<li><a href="https://scienmag.com/ai-predicts-thousands-of-mitochondrial-protein-interactions-linked-to-human-diseases/">AI Predicts Thousands of Mitochondrial Protein Interactions ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1359644625000959">Computational methods for modeling protein–protein ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#protein interactions`, `#mitochondria`, `#disease research`, `#computational biology`

---

<a id="item-7"></a>
## [RBA Speech Asks What Happens to the Economy as AI &\#x27;Intelligence&\#x27; Gets Cheaper](https://news.google.com/rss/articles/CBMiakFVX3lxTE9qWTFiTFlWZm9BRnRKQUZDdThvU0dBU3hjZFY4UV9EQnMyTlpkeXdBSlIwSjMyckZvQ2QwWEhZdGZlSnptWFpZbV9aWGxwY2RKVFh0OXhNV3VkaTdsRjlGMkp4bG0ya0ZMSHc?oc=5) ⭐️ 6.0/10

The Reserve Bank of Australia has published a speech titled &quot;What Happens to the Economy as &\#x27;Intelligence&\#x27; Gets Cheaper?&quot;, which examines how rapidly falling costs of artificial intelligence could flow through the economy. Rather than treating AI as a narrow tech-sector story, the speech frames machine intelligence as an increasingly cheap economic input whose price curve may reshape productivity, prices and labour demand. Central banks are beginning to treat AI as a macroeconomically relevant shock rather than a curiosity, because sharp declines in the cost of a general-purpose input can move inflation, wages and measured productivity. How the RBA frames this matters for monetary policy debate, since cheaper intelligence could plausibly dampen services inflation, displace certain types of labour demand, and complicate how output and productivity are measured. The item is only a title and link to the central bank&\#x27;s speech page, so the specific scenarios, quantitative estimates and the identity and date of the speaker could not be verified from the available material. The framing deliberately echoes the &quot;falling cost of intelligence&quot; argument popularised by AI developers, which compares AI capability to commodities whose unit price drops sharply over time.

google\_news · Reserve Bank of Australia · Nov 8, 22:30

**Background**: The Reserve Bank of Australia is the country&\#x27;s central bank, responsible for setting the cash rate to meet its inflation and employment objectives, and it publishes speeches by senior officials as part of its public communication. The idea that &quot;intelligence&quot; is getting cheaper refers to the steeply falling cost of AI inference and capability per unit — a trend that economists often compare to general-purpose technologies such as electricity or computing power, which reshaped whole industries once they became cheap and abundant. Central banks care about such shifts because they affect potential growth, the natural rate of interest, and how quickly wages and prices respond to demand.

**Tags**: `#AI economics`, `#macroeconomics`, `#productivity`, `#labor markets`, `#central banking`

---