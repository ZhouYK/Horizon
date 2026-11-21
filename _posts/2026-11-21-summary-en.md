---
layout: default
title: "Horizon Summary: 2026-11-21 (EN)"
date: 2026-11-21 23:02:33 +0000
lang: en
report: default
---

> From 41 items, 9 important content pieces were selected

---

1. [Zhejiang University Achieves First Real-Hardware QRAM on a Superconducting Chip](#item-1) ⭐️ 9.0/10
2. [TSMC Pauses 16nm-and-Below Chip Orders From Chinese Firms](#item-2) ⭐️ 8.0/10
3. [Microsoft brings RDMA over USB4 to Windows to pool PCs for local AI](#item-3) ⭐️ 8.0/10
4. [Oral daraxonrasib plus chemo yields 60.7% response in first-line pancreatic cancer](#item-4) ⭐️ 8.0/10
5. [OpenAI Boosts Anti-Distillation Defenses, Extraction Success Falls to 0.2%](#item-5) ⭐️ 7.0/10
6. [OpenRouter warns MiniMax model prompts may have been read by third parties](#item-6) ⭐️ 7.0/10
7. [Trump Proposes Hefty Tax on US Firms Building AI Data Centers Abroad](#item-7) ⭐️ 6.0/10
8. [Debian maintainers form gaming hardware team, eye dedicated distro](#item-8) ⭐️ 6.0/10
9. [China&\#x27;s Data Administration to Standardize Token Metering, Billing and Quality Assessment](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Zhejiang University Achieves First Real-Hardware QRAM on a Superconducting Chip](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 9.0/10

A Zhejiang University team reported the world&\#x27;s first real-hardware implementation of quantum random access memory \(QRAM\), running 4-bit and 8-bit data-retrieval prototypes on its self-fabricated superconducting chip &quot;Tianmu-2&quot; with accuracies of 80.9% and 60.4% respectively, with the results published in Nature Physics. QRAM is a long-sought hardware building block that many quantum algorithms — quantum machine learning, quantum database search and linear-algebra routines — assume but have never had on real hardware, so a working superconducting demonstration shifts it from proposal to experiment. Achieving it on a domestic 100-qubit-class chip also shows that memory-style quantum architectures, not just gate-based computation, are becoming testable in practice. The team reports that its optimized circuit is more than 30% shallower than an unoptimized scheme and that the architecture, for the first time, was experimentally shown to possess local noise resilience. Accuracy falls clearly as the address width grows from 4 to 8 bits \(80.9% to 60.4%\), which highlights the scaling challenge the team says it will tackle next.

telegram · zaihuapd · Nov 21, 08:31

**Background**: A quantum random access memory lets a quantum computer query memory addresses that are themselves in superposition, returning the stored data coherently — something classical RAM cannot do. Most designs, such as the bucket-brigade QRAM, arrange qubits in a tree so that one query touches only a logarithmic number of them, which is why circuit depth \(the number of sequential gate time steps\) is the key cost metric for these schemes. QRAM is widely assumed by algorithms such as Grover-based database search and quantum machine-learning routines, but until now it had only been studied theoretically or in small proof-of-principle photonic experiments. Tianmu-2 is a 100-qubit superconducting chip developed by Zhejiang University&\#x27;s superconducting quantum team together with Hangzhou Logic Bit Technology.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/en/item/Tianmu-2/4929794">Tianmu-2_Baiduwiki - 百度百科</a></li>
<li><a href="https://www.emergentmind.com/topics/quantum-ram-qram">Quantum RAM : Bucket-Brigade Approach</a></li>
<li><a href="https://www.quera.com/glossary/circuit-depth">What Is Circuit Depth ? Performance &amp; Optimization</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#quantum hardware`, `#Nature Physics`

---

<a id="item-2"></a>
## [TSMC Pauses 16nm-and-Below Chip Orders From Chinese Firms](https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls) ⭐️ 8.0/10

TSMC has notified customers that it is pausing advanced-node orders — 16nm and below — from Chinese companies, and will not supply such chips without a prior US export license or exemption. Chinese firms are now effectively confined to older nodes such as 28nm and 40nm, which rules out the high-bandwidth memory needed for AI data-center hardware. The move closes a loophole that let Chinese chip designers reach TSMC&\#x27;s advanced nodes through the foundry&\#x27;s own exemption screening, tightening the practical ceiling on China&\#x27;s AI accelerator and data-center silicon. Because TSMC manufactures for most of the world&\#x27;s leading chip designers, the restriction ripples across Chinese AI chip startups, their cloud customers, and the global supply chain. The key procedural change is that TSMC can no longer self-assess whether a customer&\#x27;s design qualifies for an exemption — Chinese customers must now apply in advance for US approval. The US approved list reportedly includes Apple, AMD and Nvidia, but no Chinese company, and TSMC has said it will comply with the new rules.

telegram · zaihuapd · Nov 21, 02:01

**Background**: Chip manufacturing nodes such as 16nm and 28nm describe generations of photolithography and transistor technology: smaller numbers generally mean denser, faster and more power-efficient transistors, with 16nm being TSMC&\#x27;s FinFET generation introduced in the mid-2010s. TSMC is a pure-play foundry, meaning it manufactures chips designed by other companies rather than selling its own branded processors, which is why US export rules aimed at restricting China&\#x27;s access to advanced computing are enforced largely at the foundry step. High-bandwidth memory \(HBM\) is a stacked DRAM technology that feeds data to AI accelerators at very high bandwidth, and it is typically packaged alongside chips built on advanced nodes — so cutting off those nodes also cuts off practical access to HBM-based AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_16_12nm">16nm Technology - Taiwan Semiconductor Manufacturing Company ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/14_nm_process">14 nm process - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#TSMC`, `#export-controls`, `#China`, `#AI-hardware`

---

<a id="item-3"></a>
## [Microsoft brings RDMA over USB4 to Windows to pool PCs for local AI](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

Microsoft released a developer preview of RDMA over USB4 on Windows that lets two or more PCs connected by ordinary USB4 cables share memory and GPU compute to run a single local AI model. In a demo, three AMD Ryzen AI Max+ 395 systems ran the Qwen3-235B-A22B model at 4-bit quantization at roughly 18.5 tokens per second, and the feature will ship to testers through Windows Insider. This lowers the barrier to running very large local models: previously you needed dedicated high-speed networking gear such as Thunderbolt networking, RDMA-capable NICs or InfiniBand to cluster machines, but now commodity laptops and mini-PCs with USB4 can act as a small inference cluster on a desk. For developers and privacy-conscious users who want to keep models on-premises, it offers a cheaper alternative to buying a single workstation with an enormous amount of VRAM. The preview reportedly delivers about four times lower latency than Ethernet tunnelled over USB4, and it preserves the familiar RDMA API so existing code does not need a rewrite; however it is still a developer preview pushed via Windows Insider, and performance depends on USB4 link quality, driver support and how well the model is split across machines. The demo model, Qwen3-235B-A22B, is a mixture-of-experts design with 235B total but only about 22B active parameters per token, which makes it far more practical to shard than a dense model of the same size.

telegram · zaihuapd · Nov 21, 06:13

**Background**: RDMA \(Remote Direct Memory Access\) lets one machine read and write another machine&\#x27;s memory directly, bypassing the operating system&\#x27;s networking stack, which is why it is the backbone of data-centre AI clusters and delivers far lower latency than ordinary TCP/IP networking. USB4 is the latest USB standard \(built on the Thunderbolt 3 protocol\) and provides PCIe tunnelling at 40 Gbps, enough to carry RDMA traffic over a plain cable. Distributed inference means splitting a single model&\#x27;s layers or tensors across multiple machines so that combined memory and compute can hold a model too large for any one device. Quantization to 4-bit compresses model weights to roughly four bits each, cutting memory use several-fold at some cost in accuracy, which is what makes a 235B-parameter model fit into a handful of consumer machines.

<details><summary>References</summary>
<ul>
<li><a href="https://techcommunity.microsoft.com/blog/microsoftusbblog/introducing-rdma-over-usb4%C2%AE-on-windows-run-larger-local-ai-models-across-pcs/4574602">Introducing RDMA over USB4® on Windows: run larger local AI ...</a></li>
<li><a href="https://windowsreport.com/windows-pcs-can-now-team-up-over-usb4-to-run-ai-models-that-wont-fit-on-one-machine/">Windows PCs Can Now Team Up Over USB4 to Run AI Models That ...</a></li>
<li><a href="https://shiftdelete.net/en/microsoft-rdma-usb4-windows-ai-cluster">RDMA Over USB4: Windows PCs Can Now Share One Large AI Model</a></li>

</ul>
</details>

**Tags**: `#RDMA`, `#USB4`, `#Windows`, `#Local AI`, `#Distributed Inference`

---

<a id="item-4"></a>
## [Oral daraxonrasib plus chemo yields 60.7% response in first-line pancreatic cancer](https://event.eortc.org/ena2026/2026/11/20/metastatic-pancreatic-cancer-responds-well-to-initial-treatment/) ⭐️ 8.0/10

At the EORTC-NCI-AACR \(ENA 2026\) meeting in Barcelona on November 20, investigators presented late-breaking data from a single-arm phase I/II study in which 61 previously untreated patients with metastatic pancreatic ductal adenocarcinoma received oral daraxonrasib 200 mg once daily plus gemcitabine/nab-paclitaxel. The regimen produced a confirmed objective response rate of 60.7%, a complete response rate of 8.2% \(roughly 1 in 12 patients\), a 90.2% disease control rate, median progression-free survival of 12.8 months, and a 12-month overall survival rate of 76.6% at a median follow-up of 18.3 months. Metastatic pancreatic cancer is among the most lethal solid tumors, and a response rate above 60% with roughly one in twelve patients achieving a complete response would be a major step for a disease where historical one-year survival on chemotherapy sits at roughly 22%–48%. The drug&\#x27;s August 26 FDA approval in pretreated patients, based on phase III RMC-302, plus ongoing phase III validation in the first-line setting, make these early results potentially practice-changing if confirmed in a randomized trial. The study is a single-arm phase I/II trial with no chemotherapy control, and the principal investigator explicitly cautioned that efficacy comparisons must await the ongoing phase III trial; historical chemotherapy benchmarks include 35% one-year survival in MPACT and 48% with mFOLFIRINOX, so claims of being far superior to chemotherapy are premature. Mechanistically, daraxonrasib is an oral RAS\(ON\) multi-selective inhibitor that binds active, GTP-bound RAS and covers multiple KRAS/NRAS mutations rather than targeting a single variant such as G12C.

telegram · zaihuapd · Nov 21, 11:24

**Background**: KRAS mutations drive the majority of pancreatic cancers, but for years the only approved KRAS drugs targeted the G12C variant found mainly in lung cancer, and those agents bind the inactive, GDP-bound form of the protein. RAS\(ON\) inhibitors take a different approach, locking onto the active GTP-bound RAS, and daraxonrasib \(also known as RMC-6236\) is a multi-selective version that covers many mutant RAS forms as well as wild-type RAS. Gemcitabine plus nab-paclitaxel is a standard first-line chemotherapy backbone for metastatic pancreatic cancer, established by the MPACT trial, and serves as the combination partner in this study.

<details><summary>References</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1186/s40164-026-00833-w">Daraxonrasib and the era of pan- RAS inhibition : mechanisms ...</a></li>
<li><a href="https://www.icliniq.com/articles/drug-and-supplements/daraxonrasib">What is Daraxonrasib ?</a></li>
<li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa1304369">Increased Survival in Pancreatic Cancer with nab-Paclitaxel ...</a></li>

</ul>
</details>

**Tags**: `#pancreatic cancer`, `#oncology`, `#KRAS inhibitor`, `#clinical trial`, `#daraxonrasib`

---

<a id="item-5"></a>
## [OpenAI Boosts Anti-Distillation Defenses, Extraction Success Falls to 0.2%](https://openai.com/index/combatting-adversarial-distillation/) ⭐️ 7.0/10

OpenAI published a post on November 20 stating that GPT-6.2 Astra and Sol have strengthened protections for reasoning chains, with red-team tests showing success at extracting reasoning from historical requests falling from 54.0% to 0.2%. OpenAI also said it takes enforcement action against thousands to tens of thousands of distillation accounts each week and has reported suspected DeepSeek distillation to Congress. The change signals that leading AI labs are treating reasoning traces and model capabilities as valuable intellectual property that needs active technical and policy defenses. If the claimed reduction holds, it could make unauthorized model copying harder and set expectations for how API providers police distillation, affecting competitors, developers, and AI security practices. The 54.0% to 0.2% figure is a self-reported red-team result specifically about extracting reasoning from historical requests, not a general measure of all model extraction. OpenAI describes a layered approach combining model training, safeguards, detection, and enforcement, but the brief post provides limited technical detail or independent verification.

telegram · zaihuapd · Nov 21, 01:30

**Background**: Adversarial distillation refers to extracting an AI model’s capabilities at scale through unauthorized access, often to build competing models, and it has become a focus of U.S. policy discussions around industrial-scale model extraction. Reasoning-chain extraction is especially sensitive because step-by-step rationales can reveal how a model solves problems and can be used to train another model. Defenses include anti-distillation sampling, which alters token distributions during decoding, as well as training-time modifications, detection systems, and account enforcement.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/combatting-adversarial-distillation/">Combatting adversarial distillation - OpenAI</a></li>
<li><a href="https://www.cnas.org/publications/reports/adversarial-distillation">Adversarial Distillation | CNAS</a></li>
<li><a href="https://antidistillation.com/">Antidistillation Sampling</a></li>

</ul>
</details>

**Tags**: `#AI model security`, `#adversarial distillation`, `#OpenAI`, `#model extraction`, `#IP protection`

---

<a id="item-6"></a>
## [OpenRouter warns MiniMax model prompts may have been read by third parties](https://news.ycombinator.com/item?id=50585962) ⭐️ 7.0/10

OpenRouter sent an email notice warning users that prompts sent to MiniMax models may have been read by third parties. Security researchers planted unique test URLs in prompts sent to MiniMax models between July and October 2026, and third parties accessed those URLs 40 to 130 hours after submission. OpenRouter is a widely used routing layer that many developers rely on to reach dozens of models through a single API, so a leak at one upstream provider can silently expose secrets belonging to users who never dealt with that provider directly. Anyone who sent credentials, keys, or proprietary code to MiniMax endpoints through OpenRouter should assume compromise and rotate those secrets. OpenRouter attributed the problem to MiniMax and its forwarding partners AtlasCloud, Novita, and StreamLake, and has removed the &quot;zero data retention&quot; label from the affected endpoints. The notice advises users with sensitive credentials in their prompts to change API keys and passwords, and no corresponding announcement had been published on OpenRouter&\#x27;s public website at the time of reporting.

telegram · zaihuapd · Nov 21, 06:53

**Background**: OpenRouter is an AI routing service \(now owned by Stripe\) that lets developers send one API request and have it dispatched to many different models and inference providers. MiniMax is a Chinese AI company offering a family of proprietary foundation models with API access via HTTP, the Anthropic SDK, and the OpenAI SDK; requests to it can pass through intermediary resellers such as AtlasCloud, Novita, and StreamLake. &quot;Zero data retention&quot; \(ZDR\) is a contractual label meaning the provider promises not to store prompts or outputs beyond what is needed for abuse monitoring — an important guarantee for companies sending confidential data to LLMs. The test-URL technique used here works by embedding a unique, rarely visited link in a prompt; if that link is later fetched from an unknown IP, it proves someone else read and acted on the prompt content.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter - Wikipedia</a></li>
<li><a href="https://platform.minimax.io/docs/api-reference/api-overview">API Overview - MiniMax API Docs Models - MiniMax API Docs MiniMax API: Get Your Key, Base URL and First Request 接口概览 - MiniMax 开放平台文档中心 OpenAI SDK - MiniMax 开放平台文档中心 minimaxAPI详情-阿里云帮助中心</a></li>
<li><a href="https://www.onvo.ai/blog/zero-data-retention-llm-explained">Zero Data Retention for LLMs: What It Means and How to Verify It</a></li>

</ul>
</details>

**Tags**: `#security`, `#privacy`, `#LLM APIs`, `#data-retention`, `#OpenRouter/MiniMax`

---

<a id="item-7"></a>
## [Trump Proposes Hefty Tax on US Firms Building AI Data Centers Abroad](https://apnews.com/article/trump-artificial-intelligence-data-centers-f1ac03b73d13445400eeed8631d9d879) ⭐️ 6.0/10

At a White House press conference on November 20, President Trump said he plans to impose a &quot;massive tax&quot; on US technology companies that build AI data centers outside the United States, and noted he had not yet shared the plan with officials inside his own government. He also urged American communities to accept data centers and to negotiate directly with developers so that the developers pay the host communities. The proposal signals that AI infrastructure is now being treated as a strategic national asset in the US-China technology rivalry, and if enacted it could reshape where hyperscalers such as Microsoft, Google, Amazon and Meta build their next-generation capacity. It also injects regulatory uncertainty into overseas projects, particularly in the Middle East and Asia, where US firms have announced large AI data center investments. The idea remains only a public statement: no legislative text, tax rate, enforcement mechanism or timeline has been released, and Trump said he had not yet informed officials within his own administration. Any such levy would face practical questions, including how to define an &quot;AI data center&quot; and whether the US could tax profits or equipment shipped abroad without conflicting with existing tax treaties.

telegram · zaihuapd · Nov 21, 03:26

**Background**: Training and serving large AI models requires vast clusters of GPUs, which in turn need enormous amounts of electricity and cooling — a single cutting-edge data center campus can draw as much power as a small city. US technology companies have therefore been siting new capacity abroad, in places such as the Gulf states and Southeast Asia, where land, power and permits are cheaper and faster to secure. At the same time, many US communities have pushed back against local projects over concerns about grid strain, water use and noise, which is the tension Trump addressed when he urged communities to negotiate payments from developers.

**Tags**: `#AI infrastructure`, `#data centers`, `#policy regulation`, `#US-China AI competition`, `#Trump administration`

---

<a id="item-8"></a>
## [Debian maintainers form gaming hardware team, eye dedicated distro](https://www.ithome.com/1/030/390.htm) ⭐️ 6.0/10

Debian maintainer Karamtoth has formed a &quot;Debian Gaming Hardware Team&quot; that is testing gaming hardware and emulators, exploring ways to get Debian running on gaming handhelds and consoles, and plans to eventually ship a dedicated edition for hardware integrators and enthusiasts that boots straight into a gaming mode. If the plan materializes, Debian could become a credible alternative to the Fedora- and Arch-based gaming distributions that currently dominate handheld gaming devices, giving hardware vendors and tinkerers a more conservative, long-term-supported base to build on. The effort is an early-stage community initiative rather than an official Debian release project, and it must contend with Debian&\#x27;s roughly two-year major release cadence, which makes support for new gaming hardware and GPUs lag behind rolling-release distributions.

telegram · zaihuapd · Nov 21, 09:10

**Background**: Debian is one of the oldest community-run Linux distributions and serves as the upstream base for derivatives such as Ubuntu and many others, prized for stability and its strict free-software policies. Its conservative release model means kernel and driver versions in a stable release can be years behind, which is a problem for gaming hardware that needs recent GPU drivers and kernel features. Meanwhile, handheld gaming PCs like the Steam Deck popularized gaming-focused Linux distributions, most notably Arch-based SteamOS, alongside Fedora-based alternatives such as Bazzite and Nobara.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gamingonlinux.com/2026/11/debian-linux-forms-a-debian-gaming-hardware-team-for-testing-handhelds-and-consoles/">Debian Linux forms a Debian Gaming Hardware... | GamingOnLinux</a></li>
<li><a href="https://www.techpowerup.com/355046/debian-linux-forms-gaming-hardware-team-for-handheld-and-bleeding-edge-hardware-testing">Debian Linux Forms Gaming Hardware Team for... | TechPowerUp</a></li>
<li><a href="https://itsfoss.com/linux-gaming-distributions/">11 Best Linux Gaming Distributions in 2025</a></li>

</ul>
</details>

**Tags**: `#Debian`, `#Linux gaming`, `#Linux distributions`, `#handheld gaming`, `#open source`

---

<a id="item-9"></a>
## [China&\#x27;s Data Administration to Standardize Token Metering, Billing and Quality Assessment](https://www.cls.cn/detail/2540805) ⭐️ 6.0/10

At the opening ceremony of the 2026 World Computing Conference in Changsha, Hunan on November 20, 2026, National Data Administration \(NDA\) director Liu Liehong said the agency will expand token \(词元\) service application scenarios and put in place standards for token metering, billing and quality assessment. He framed tokens as the &quot;value anchor&quot; of the digital-intelligent economy and said the new rules should steer the industry toward regulated development and &quot;resolutely avoid low-quality duplicated construction.&quot; Tokens are the basic billing unit for almost all commercial LLM APIs, so unified metering and quality standards could reshape how model and API services are priced, compared and procured across China&\#x27;s AI market. It also signals that Beijing intends to treat token production as measurable digital infrastructure rather than leaving pricing and quality claims entirely to vendors. Liu described the rise of &quot;token factories&quot; \(词元工厂\) that turn compute rental, model supply and data capabilities into token production services, arguing that token quality depends on the underlying model while output efficiency tests the factory&\#x27;s engineering. The announcement offered no technical specifications, thresholds or timeline, so the concrete metrics for metering and quality grading remain undefined.

telegram · zaihuapd · Nov 21, 10:19

**Background**: Token is the term for the small chunks of text that large language models read and generate, and it is the unit on which API usage is metered and billed. In March 2026 the National Data Administration officially adopted the Chinese name 词元 for &quot;token&quot; and began pushing for a metering rule system to give AI services a fair, transparent settlement unit. Around that framing, operators have started building so-called token factories — for example Lenovo&\#x27;s hybrid token factory and the Wuxiang Yungu facility in Nanning — that aggregate heterogeneous compute and dispatch models to mass-produce tokens, similar to utilities selling electricity.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E8%AF%8D%E5%85%83%E8%AE%A1%E9%87%8F%E8%A7%84%E5%88%99%E4%BD%93%E7%B3%BB/68389330">词元计量规则体系_百度百科</a></li>
<li><a href="https://www.ithome.com/1/030/418.htm">国家数据局：将积极拓展词元服务应用场景，健全词元计量计费、质量测...</a></li>
<li><a href="https://www.zgeo.com.cn/news/lenovo-token-factory-ai-infrastructure">联想万全混合 词 元 工 厂 ：AI基础设施转向Token运营 | 智脑时代 ZGEO</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#tokenization`, `#China tech regulation`, `#AI infrastructure`, `#standards`

---