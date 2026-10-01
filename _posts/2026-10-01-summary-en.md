---
layout: default
title: "Horizon Summary: 2026-10-01 (EN)"
date: 2026-10-01 23:03:30 +0000
lang: en
report: default
---

> From 154 items, 8 important content pieces were selected

---

1. [Reddit to Kill RSS Feeds and Public API Access Over AI Scraping](#item-1) ⭐️ 8.0/10
2. [OpenAI disrupts model-distillation campaign, links activity to Moonshot AI affiliates](#item-2) ⭐️ 8.0/10
3. [Google DeepMind Adds Watermarks to AI-Designed Proteins](#item-3) ⭐️ 8.0/10
4. [Tencent leases 100,000 AI chips from Oracle in $7B deal](#item-4) ⭐️ 8.0/10
5. [VS Code 1.140 adds multi-folder agent sessions and HydraFusion orchestration preview](#item-5) ⭐️ 6.0/10
6. [Geekerwan: Huawei&\#x27;s Kirin 9050 Pro Nearly Matches Snapdragon 8 Elite](#item-6) ⭐️ 6.0/10
7. [Pentagon Personnel System Breached, Exposing Data of Over 3 Million](#item-7) ⭐️ 6.0/10
8. [Cloudflare Opens Contest for Agent-Native Git Platform](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Reddit to Kill RSS Feeds and Public API Access Over AI Scraping](https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/) ⭐️ 8.0/10

Reddit announced it will end RSS feed support on November 13, 2026, and shut down public API access by March 2027, citing large-scale scraping and automated abuse, particularly by AI bots. The company also told moderators to migrate to its Discord Relay app and said third-party apps and bot developers must register by January 12, 2027 or lose API access. RSS and the public API have long been the main ways developers, researchers, moderators and news aggregators pull Reddit content programmatically, so ending both removes a widely used piece of open web infrastructure and cuts off social listening tools, academic research pipelines and AI assistants. It also signals a broader shift in which large platforms lock their data behind contracts and approvals to control who profits from it, potentially setting a precedent other sites will follow. No general replacement exists for the non-moderator RSS use cases; the recommended Discord Relay is a Reddit-hosted Devvit app that pushes selected subreddit events to Discord on Reddit&\#x27;s own terms, so data still leaves the platform but only through an approved channel. Old Reddit access is also being restricted to recently logged-in users, and the registration deadline for third-party developers is January 12, 2027.

telegram · zaihuapd · Oct 1, 00:27

**Background**: RSS \(Really Simple Syndication\) is a decades-old, open standard that lets a site publish its latest content as a structured XML feed, which anyone can subscribe to with a feed reader or script to get new posts without visiting the site or using an official app. Reddit&\#x27;s public API is the programmatic interface that third-party clients, bots, moderation tools and research projects use to read and interact with subreddits. Both mechanisms give access without requiring user-level authentication or commercial agreements, which is exactly what makes them hard to meter and monetize — and what makes them attractive to automated scrapers, including those collecting text to train AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/">Reddit is killing RSS feeds and ending public API access because of...</a></li>
<li><a href="https://mashable.com/tech/reddit-rss-feeds-public-api-shutdown-ai-scraping">Reddit is shutting down RSS and public API access . | Mashable</a></li>
<li><a href="https://savedelete.com/article/reddit-rss-api-shutdown/">Reddit Ends RSS and Public API: Dates and What... | SaveDelete</a></li>

</ul>
</details>

**Tags**: `#Reddit`, `#API`, `#RSS`, `#AI bots`, `#platform policy`

---

<a id="item-2"></a>
## [OpenAI disrupts model-distillation campaign, links activity to Moonshot AI affiliates](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/) ⭐️ 8.0/10

OpenAI announced it disrupted a coordinated model-distillation campaign that began in early July 2026, peaked on July 24-25, and involved roughly 16,000 requests from more than 4,000 users, with activity tied to over 15,000 users shut down by July 28. OpenAI attributed the core activity to individuals affiliated with Moonshot AI, the developer of the Kimi model, and said it shared information with industry peers and governments through channels such as the Frontier Model Forum. This is one of the first times a leading US lab has publicly named personnel linked to a specific Chinese AI company in connection with a distillation campaign, escalating intellectual-property and terms-of-service disputes between frontier labs. It also signals that model-distillation enforcement is shifting from quiet account bans toward public attribution and multi-stakeholder information sharing, which could affect how AI companies police API abuse and how labs in different jurisdictions cooperate. OpenAI describes the attackers as manipulating interactions to extract protected reasoning content, i.e. harvesting the model&\#x27;s outputs to imitate its capabilities rather than exploiting a software vulnerability. The disclosure gives request and account counts but no technical detail on the extraction methodology, the specific model accessed, or the evidence tying the activity to Moonshot AI personnel, and Moonshot AI has not been reported as responding publicly.

telegram · zaihuapd · Oct 1, 01:18

**Background**: Model distillation normally refers to training a smaller &quot;student&quot; model on outputs from a larger &quot;teacher&quot; model, a legitimate and common technique; so-called distillation attacks turn it against a commercial service by scraping large volumes of a proprietary model&\#x27;s outputs through APIs or chat interfaces, often with many fake accounts, to clone capabilities without paying for training. The Frontier Model Forum is a non-profit industry body founded in 2023 by Google, Microsoft, OpenAI, Anthropic, Amazon and Meta to coordinate safety and security practices for the most advanced models. Moonshot AI, founded in Beijing in 2023, is the developer of the Kimi assistant and long-context models and is one of China&\#x27;s best-known model developers.

<details><summary>References</summary>
<ul>
<li><a href="https://jangwook.net/zh/blog/zh/ai-distillation-attacks-enterprise-defense/">AI 模 型 蒸 馏 攻 击 实态——CTO必知的IP保护策略</a></li>
<li><a href="https://www.baike.com/wikiid/7626047374062010368">前 沿 模 型 论 坛 -快懂百科</a></li>
<li><a href="https://ai.puliot.com/houses/moonshot-kimi">世家 · 月 之 暗 面 （ Moonshot AI / Kimi ） | AI 史记</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#model-distillation`, `#AI-security`, `#Moonshot-AI`, `#AI-industry-news`

---

<a id="item-3"></a>
## [Google DeepMind Adds Watermarks to AI-Designed Proteins](https://arstechnica.com/science/2026/09/google-figures-out-how-to-watermark-ai-designed-proteins/) ⭐️ 8.0/10

Google DeepMind introduced SynthID Bio, a family of watermarking methods that embed detectable signatures into AI-generated protein sequences and structures, with the sequence approach integrated into ProteinMPNN&\#x27;s autoregressive decoding so that only watermarked amino acids that preserve function are accepted. For protein folding, it fine-tunes a small part of AlphaFold 3&\#x27;s diffusion network to build watermarking directly into the model weights, and the work is published alongside a Nature paper. As deep-learning protein design becomes easier to use, being able to trace whether a sequence came from a trusted AI model gives labs and biosecurity reviewers a provenance signal that could support screening, IP attribution, and misuse deterrence. It positions watermarking, already standard for AI images and text, as a potential tool for synthetic biology and the broader AI-for-science safety stack. The paper reports that watermarked proteins still bound their intended targets and that detection performed well in the tested settings, but the validation covers a specific design pipeline and only a small number of targets; short proteins, other design tools, and deliberate watermark removal or dilution remain open limitations. Critically, SynthID Bio is a provenance-verification mechanism, not a detector that can automatically judge whether a protein is dangerous.

telegram · zaihuapd · Oct 1, 03:40

**Background**: Protein design models such as ProteinMPNN take a desired protein backbone structure and generate amino acid sequences that fold into it, which makes it possible to design novel proteins computationally rather than discovering them in nature. AlphaFold 3, also from Google DeepMind, predicts the three-dimensional structures of proteins. SynthID is Google&\#x27;s existing family of watermarking techniques for AI-generated images, text, audio, and video, and SynthID Bio extends that idea to biological sequences; concerns that AI could be used to design harmful proteins are the main driver behind adding provenance signals at the point of generation.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/introducing-synthid-bio/">SynthID Bio: Watermarking methods for... — Google DeepMind</a></li>
<li><a href="https://github.com/google-deepmind/synthidbio">GitHub - google-deepmind/synthidbio: SynthID Bio is a family of...</a></li>
<li><a href="https://github.com/dauparas/ProteinMPNN">GitHub - dauparas/ ProteinMPNN : Code for the ProteinMPNN paper</a></li>

</ul>
</details>

**Tags**: `#AI biosecurity`, `#protein design`, `#watermarking`, `#DeepMind`, `#SynthID`

---

<a id="item-4"></a>
## [Tencent leases 100,000 AI chips from Oracle in $7B deal](https://www.ft.com/content/8799b33d-f07c-4a03-82f0-bf5d3d1d29e9) ⭐️ 8.0/10

Tencent has signed a five-year lease worth roughly $7 billion with Oracle for about 100,000 advanced AI chips that it is barred from buying directly in China, according to the Financial Times and Reuters. The deal is Tencent&\#x27;s largest overseas compute leasing arrangement to date and spans multiple data centers in Southeast Asia, with around 30% of the payment required upfront. The deal illustrates how Chinese tech giants are routing around US export controls by leasing restricted compute from American cloud providers instead of purchasing chips outright, keeping their AI model and agent development competitive. It also deepens Oracle&\#x27;s position as a major AI infrastructure landlord and highlights how export-control policy shapes where global AI compute is physically located. US rules prohibit Chinese firms from directly buying top-tier AI accelerators but do not forbid leasing them from overseas cloud providers, which is the loophole this contract exploits; roughly 30% of the $7 billion is due upfront, and the capacity is spread across multiple Southeast Asian data centers rather than a single site. Oracle, unlike the big three cloud providers, tends to lease data center capacity from partners such as Crusoe rather than building it all itself, so the underlying hardware supply chain involves third parties.

telegram · zaihuapd · Oct 1, 05:07

**Background**: Since 2022 the US has progressively restricted exports of advanced AI chips and chipmaking equipment to China, aiming to slow its AI development; Nvidia&\#x27;s most capable GPUs require licenses for Chinese buyers. A widely used workaround is for Chinese firms to rent compute housed in overseas data centers operated by US cloud providers — ByteDance reportedly did this for TikTok-related AI training. Oracle has aggressively expanded its AI cloud business, committing large sums to data center capacity largely through long-term leases.

<details><summary>References</summary>
<ul>
<li><a href="https://www.straitstimes.com/business/chinas-tencent-leases-100000-chips-from-us-tech-firm-oracle-to-accelerate-ai-push-report">Tencent leases 100,000 AI chips from Oracle to... | The Straits Times</a></li>
<li><a href="https://aiunderstanding.org/news/tencent-leases-100-000-ai-chips-from-oracle-in-7-billion-five-year-deal">Tencent leases 100,000 AI chips from Oracle in $7 billion five‑year deal</a></li>
<li><a href="https://mspoweruser.com/despite-us-sanctions-how-did-chinese-firm-bytedance-get-access-to-nvidias-ai-chips/">Despite US sanctions, how did Chinese firm ByteDance get access to...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Tencent`, `#Oracle`, `#export controls`, `#cloud computing`

---

<a id="item-5"></a>
## [VS Code 1.140 adds multi-folder agent sessions and HydraFusion orchestration preview](https://code.visualstudio.com/updates/v1_140) ⭐️ 6.0/10

Visual Studio Code 1.140 introduces a Copilot harness that lets a single agent session work across multiple folders, with the ability to delegate tasks to a remote agent host, and ships HydraFusion multi-model orchestration as a research preview. The release also adds cross-worktree reuse of ignored folders, improvements to Dev Containers and session management, and new enterprise AI version requirements plus Auto model default-tier controls. These changes push VS Code further toward agentic, multi-repository development workflows, where an assistant coordinates work across codebases and machines rather than answering questions in one file. HydraFusion in particular signals a shift from users picking a single model to the tooling routing tasks across several models for cost and quality reasons, which could reshape how developers pay for and evaluate AI coding assistants. Multi-folder sessions are experimental and disabled by default; each chat inside a multi-chat session can point at its own folder or worktree, and chats targeting the same folder share state such as terminals, tasks, changes and pull requests. HydraFusion reportedly drafts with cheaper models, escalates to stronger ones for hard problems, and cross-checks results across model families, with claims of up to 67% cost reduction while matching frontier-model quality.

telegram · zaihuapd · Oct 1, 09:33

**Background**: VS Code is Microsoft&\#x27;s free, cross-platform code editor and the most widely used development environment, shipping a feature update roughly every month. An &quot;agent harness&quot; is the runtime layer that sits between an agent&\#x27;s configuration \(prompts, tools, context\) and the underlying language model, deciding how the agent plans, calls tools and recovers from errors; VS Code already supports harnesses such as Local, GitHub Copilot, Anthropic Claude and OpenAI Codex. A &quot;worktree&quot; is a Git feature that lets multiple working directories share one repository history, which is useful when agents need isolated copies of the same codebase.

<details><summary>References</summary>
<ul>
<li><a href="https://code.visualstudio.com/updates/v1_140">Learn what&#x27;s new in Visual Studio Code 1.140</a></li>
<li><a href="https://visualstudiomagazine.com/articles/2026/09/30/vs-code-1-140-expands-agent-coordination-across-folders-and-machines.aspx">VS Code 1.140 Expands Agent Coordination Across Folders and...</a></li>
<li><a href="https://www.datastudios.org/post/github-launches-hydrafusion-multi-model-orchestration-dynamic-routing-lower-cost-coding-and-the">GitHub Launches HydraFusion : Multi - Model Orchestration , Dynamic...</a></li>

</ul>
</details>

**Tags**: `#VS Code`, `#GitHub Copilot`, `#AI Agents`, `#Multi-Model Orchestration`, `#Developer Tools`

---

<a id="item-6"></a>
## [Geekerwan: Huawei&\#x27;s Kirin 9050 Pro Nearly Matches Snapdragon 8 Elite](https://www.bilibili.com/video/BV1fHaB6WEh1/) ⭐️ 6.0/10

Geekerwan \(极客湾\) published test results for Huawei&\#x27;s Kirin 9050 Pro inside the Mate XT 2, reporting GeekBench 7 scores of 1813 single-core and 8159 multi-core, plus an NPU measurement of 67.7 TOPS. In gaming tests of Genshin Impact, Ananta \(异环\) and Wuthering Waves \(鸣潮\), the Mate XT 2 performed close to a Samsung tri-fold device running Qualcomm&\#x27;s Snapdragon 8 Elite and clearly better than the previous-generation Mate XTs. The result suggests Huawei can still close much of the performance gap with Qualcomm&\#x27;s flagship silicon even without access to leading-edge fabrication, which matters for the competitive balance of the Chinese flagship phone market and for how much pressure rests on chip designers rather than process nodes. It also gives buyers of Huawei&\#x27;s most expensive foldables a concrete reason to expect gaming and AI performance comparable to mainstream Android flagships. Geekerwan notes that the chip&\#x27;s manufacturing process and microarchitecture show essentially no obvious changes from the previous generation, so the CPU, GPU and NPU gains appear to come mainly from tuning rather than a new node or core design. The data is a single-device benchmark summary relayed through a Telegram channel, with no raw methodology or independent verification available at the time of reporting.

telegram · zaihuapd · Oct 1, 11:50

**Background**: Geekerwan is a well-known mainland Chinese tech review outlet that specializes in detailed chip benchmarks, including die analysis and power-efficiency measurements. The Kirin 9050 Pro is a HiSilicon mobile system-on-chip built for Huawei&\#x27;s flagship phones, and it appears in the Mate XT 2, a tri-fold device; HiSilicon is Huawei&\#x27;s chip design arm, and Huawei has been restricted from advanced foundry nodes by US export controls. GeekBench is a widely used cross-platform CPU/GPU benchmark whose seventh version adds machine-learning and content-creation workloads, while NPU refers to the on-chip neural processing unit, whose throughput is measured in TOPS \(trillions of operations per second\). The Snapdragon 8 Elite is Qualcomm&\#x27;s current flagship mobile platform and the usual performance yardstick for Android phones.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Geekerwan">Geekerwan</a></li>
<li><a href="https://grokipedia.com/page/Kirin_9050_Pro">Kirin 9050 Pro</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geekbench">Geekbench</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Kirin 9050 Pro`, `#Snapdragon 8 Elite`, `#mobile SoC`, `#benchmarks`

---

<a id="item-7"></a>
## [Pentagon Personnel System Breached, Exposing Data of Over 3 Million](https://www.techspot.com/news/114056-pentagon-data-breach-exposed-data-more-than-3.html) ⭐️ 6.0/10

The U.S. Department of Defense disclosed that an unauthorized party accessed a system at its Defense Manpower Data Center \(DMDC\) at some point between October 2025 and July 2026, exposing Social Security numbers and service information for roughly 3.06 million people — about 2.76 million living individuals and 294,000 deceased ones. This is one of the larger U.S. government breaches in recent years, and because Social Security numbers are effectively the master key to identity theft, the victims — service members, veterans, civilian employees, contractors and military family members — face long-term fraud and credit risk. The nine-month dwell time before detection also raises uncomfortable questions about the visibility and monitoring of DoD personnel infrastructure. The DoD says the vulnerability has since been patched, that no misuse of the data has been observed so far, and that it is offering identity protection and credit monitoring services to those affected. What remains undisclosed is how the intruders gained entry, how much data was actually viewed or stolen, and why the intrusion went undetected for roughly nine months.

telegram · zaihuapd · Oct 1, 14:16

**Background**: The Defense Manpower Data Center is an office under the Office of the Secretary of Defense that collates personnel, manpower, training and financial data for the U.S. military. It maintains records on individuals&\#x27; military status, including start and termination dates of service, covering active-duty and reserve personnel, retirees, civilian employees, contractors and dependents. Because Social Security numbers are widely used as identifiers in these government personnel records, the DMDC dataset is a high-value target, and its records are also used externally to verify military service for benefits such as the Servicemembers Civil Relief Act \(SCRA\).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Defense_Manpower_Data_Center">Defense Manpower Data Center - Wikipedia</a></li>
<li><a href="https://www.servicememberscivilreliefact.com/about-us/defense-manpower-data-center/">Defense Manpower Data Center ( DMDC ) - SRCA Centralized...</a></li>
<li><a href="https://govfacts.org/government/federal/agencies/defense/verifying-military-service-the-complete-guide-to-scra-and-dmdc-resources/">Verifying Military Service: The Complete Guide to SCRA and DMDC ...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data-breach`, `#government`, `#privacy`, `#defense`

---

<a id="item-8"></a>
## [Cloudflare Opens Contest for Agent-Native Git Platform](https://blog.cloudflare.com/next-git-platform-on-cloudflare/) ⭐️ 6.0/10

Cloudflare is inviting developers to build a next-generation Git platform designed for AI agent collaboration, based on Cloudflare Workers and the public-beta Artifacts service. Submissions must include a 5–10 minute demo video, permissively licensed source code \(MIT, Apache, or BSD\), and run instructions, with a deadline of October 14, 2026, and $25,000 in Cloudflare credits for the first-place team. AI agents increasingly need to create, fork, and merge repositories at machine speed, a workload that conventional Git hosting was never designed for. By seeding an agent-native Git platform on its own edge infrastructure, Cloudflare is pushing both the AI-agent tooling ecosystem and its own developer platform toward hosting the code workflows of autonomous software development. Artifacts is described as programmable, versioned, Git-compatible storage that can host tens of millions of repositories and fork from any remote, and developers are expected to layer on multi-agent parallel development, code review, change merging, and context management. Entries must be released under a permissive license such as MIT, Apache, or BSD, and the prize is awarded as Cloudflare credits rather than cash.

telegram · zaihuapd · Oct 1, 14:57

**Background**: Cloudflare Workers is Cloudflare&\#x27;s serverless platform that runs code across its global edge network, scaling automatically from zero to millions of requests with a free tier that includes limits such as 100,000 requests per day. Artifacts, currently in public beta, is Cloudflare&\#x27;s Git-compatible filesystem and storage layer built for agents: it lets programs create, store, version, and share filesystem artifacts, and hand off a URL to any standard Git client. The contest asks developers to combine these two pieces to reimagine Git hosting for a world where AI agents, not just humans, are the primary authors and reviewers of code.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cloudflare.com/products/artifacts/">Cloudflare Artifacts - Versioned Git-compatible storage for agents</a></li>
<li><a href="https://developers.cloudflare.com/artifacts/">Artifacts · Cloudflare Artifacts docs</a></li>
<li><a href="https://www.cloudflare.com/products/workers/">Cloudflare Workers - Global Serverless Functions Platform</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#Git`, `#AI Agents`, `#Developer Tools`, `#Contest`

---