---
layout: default
title: "Horizon Summary: 2026-11-07 (EN)"
date: 2026-11-07 23:03:30 +0000
lang: en
report: default
---

> From 159 items, 7 important content pieces were selected

---

1. [GitHub&\#x27;s Rubicon architecture pushes 7,200 times per second](#item-1) ⭐️ 8.0/10
2. [Microsoft Winds Down Oracle AI Compute Rental Deal as Older Nvidia GPUs Fall Short](#item-2) ⭐️ 7.0/10
3. [Claude Code said to leak login emails through outbound web searches](#item-3) ⭐️ 7.0/10
4. [Apple unveils HALO, a three-layer humanoid robot control system built on two Qwen models](#item-4) ⭐️ 7.0/10
5. [Anthropic Said to Launch IPO Roadshow Next Week, Targeting Week of Nov 16](#item-5) ⭐️ 6.0/10
6. [Turkey Uses AI to Recover 100 Looted Antiquities From the US](#item-6) ⭐️ 6.0/10
7. [SoftBank and ABB Weigh China Carve-Out to Salvage $5.4B Robotics Deal](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [GitHub&\#x27;s Rubicon architecture pushes 7,200 times per second](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) ⭐️ 8.0/10

GitHub introduced a new Git storage architecture codenamed Rubicon, which in internal testing sustained 5,000 AI agents collaborating on a single repository while handling up to 7,200 pushes per second with low read latency. The design moves Git objects into Azure Blob Storage, manages reference state through a Ref-CAS service, and uses virtual replicas for reads and writes while background compaction nodes pack data. GitHub is one of the world&\#x27;s largest code-hosting platforms, so re-architecting its storage layer signals how the platform expects workloads to change as autonomous AI agents, rather than humans, generate the bulk of repository traffic. If it scales beyond the current limited private preview, it could set a new bar for how code-hosting infrastructure handles high-concurrency, agent-driven development. Compaction no longer runs inline in the write path but runs entirely in the background on separate nodes that lease ownership over subsets of a repository&\#x27;s data, allowing compaction to scale horizontally and notifying virtual replicas of state changes via Ref-CAS. The virtual write replica also coalesces transactions on disjoint references into a single set of network I/Os to object storage, so a busy repository pays one round trip across many concurrent writes instead of one per write.

telegram · zaihuapd · Nov 7, 14:12

**Background**: Git stores a repository as a graph of immutable objects \(blobs, trees, commits\) plus mutable references such as branches and tags; conventionally those objects live in packfiles on a local filesystem, and repacking them is expensive and competes with live traffic. Rubicon instead separates the immutable object data \(placed in Azure Blob Storage\) from the reference state \(tracked by a compare-and-swap style service, Ref-CAS\), and fronts them with &\#x27;virtual replicas&\#x27; that present a normal Git interface to clients. This decoupling is what lets many writers hit the same repository concurrently, and it is aimed squarely at the agent era, where a single repository may see thousands of small automated pushes rather than occasional human commits.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/">Inside GitHub’s new Git storage architecture - The GitHub Blog</a></li>
<li><a href="https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/">The bridge to agent-scale Git infrastructure - The GitHub Blog</a></li>

</ul>
</details>

**Tags**: `#GitHub`, `#Git`, `#storage architecture`, `#distributed systems`, `#AI agents`

---

<a id="item-2"></a>
## [Microsoft Winds Down Oracle AI Compute Rental Deal as Older Nvidia GPUs Fall Short](https://www.bloomberg.com/news/articles/2026-11-06/microsoft-is-winding-down-oracle-deal-to-rent-ai-cloud-capacity) ⭐️ 7.0/10

Microsoft is reportedly phasing out its agreement to rent AI compute capacity from Oracle, having declined to renew contracts over the past few months, a move that briefly pushed Oracle shares down about 3%. People familiar with the matter said Oracle&\#x27;s hardware relies on older-generation Nvidia chips that no longer meet Microsoft&\#x27;s requirements. The decision signals that the newest Nvidia accelerators have become the baseline requirement for hyperscalers running large-scale AI workloads, potentially leaving owners of older GPU fleets with a shrinking pool of buyers. It also highlights how quickly AI cloud capacity deals can shift between major providers, and why Oracle&\#x27;s AI infrastructure ambitions are closely tied to how fast it refreshes its GPU inventory. The deal, announced in 2023, was used to support the AI-powered version of Bing, and Oracle has countered that AI infrastructure demand remains strong, noting it renewed GPU contracts in September for hardware purchased four years earlier at a price about 20% above the original. Microsoft declined to comment, and the arrangement is being wound down rather than abruptly cancelled.

telegram · zaihuapd · Nov 7, 02:00

**Background**: Renting AI compute has become a common arrangement because training and running large models requires enormous numbers of GPUs, and demand has at times outstripped supply, giving capacity owners strong bargaining power. Oracle Cloud Infrastructure offers large GPU clusters built with Nvidia hardware, which Microsoft rented to supplement its own Azure capacity for services such as Bing. Nvidia releases new data-center GPU generations every couple of years, and each generation typically delivers substantially better performance-per-dollar and power efficiency, so older cards become less attractive for demanding AI workloads even though they may still be resold or reused.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oracle.com/cn/ai-infrastructure/">AI 基础设施 | Oracle 中国</a></li>
<li><a href="https://www.oracle.com/cn/cloud/nvidia/">AI Anywhere with Oracle Cloud and NVIDIA | Oracle 中国</a></li>
<li><a href="https://m.pedaily.cn/news/524865">AI 大 模 型掀起 算 力 租 赁 潮|投资界</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#Oracle`, `#AI infrastructure`, `#Cloud computing`, `#Nvidia`

---

<a id="item-3"></a>
## [Claude Code said to leak login emails through outbound web searches](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 7.0/10

A developer report filed on the anthropics/claude-code GitHub issue tracker \(issue \#107757\) reveals that Claude Code was silently inserting the user&\#x27;s login email into outbound web requests, sending it to sites such as Wikipedia and the U.S. Securities and Exchange Commission and resulting in a flood of scam email. Anthropic engineers shipped a block in version 2.1.317, but it can still be bypassed with a Python script, and the company says the login email will be removed from the model context in the next release. Claude Code runs inside developers&\#x27; terminals and browsers on their behalf, so embedding an identity credential like a login email in the model context turns routine web lookups into a data-leak channel that reaches third parties. The case is a concrete example of AI agent safety risk in a widely used coding tool, and it shows how a fix for one quality problem can quietly create a privacy problem that affects many developers. The leak reportedly traces back to a deliberate design decision: Anthropic placed the login email in the model context to stop Claude from inventing a fake author name. The problem was first reported in July, and while version 2.1.317 blocks the known paths, scripted requests can still evade the filter, with a full removal from context promised for the next version.

telegram · zaihuapd · Nov 7, 08:09

**Background**: Claude Code is Anthropic&\#x27;s agentic coding tool that runs in the terminal or IDE, reading the codebase, editing files, running commands, and making web requests on the user&\#x27;s behalf. Like other LLM agents, it decides what to do by looking at its &quot;model context&quot; — the text the model can see — so any information placed there for output-quality reasons can also surface in tool calls and outbound network traffic. This is why a small prompt-level tweak can turn into an external data-disclosure issue once an agent is allowed to reach the open internet.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/ claude - code : Claude Code is an agentic coding ...</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#privacy`, `#Claude Code`, `#AI agents`, `#data leakage`

---

<a id="item-4"></a>
## [Apple unveils HALO, a three-layer humanoid robot control system built on two Qwen models](https://weibo.com/1642634100/RqjjGllvw) ⭐️ 7.0/10

Apple researchers submitted a paper to arXiv on November 4 disclosing HALO, a three-layer autonomous control system for humanoid robots, and validated it on a Unitree G1 by transferring motions learned in simulation into an unfamiliar real-world room. The top layer uses Qwen3.6-35B-A3B for task orchestration, the middle layer uses Qwen3.5-2B to generate actions, and the bottom layer is an RL-trained motion tracker; Apple has also released the code for data generation, model training, and deployment. The work shows a major consumer-tech player applying a hierarchical LLM-plus-RL stack to full humanoid control, splitting slow semantic planning from fast motor generation rather than relying on a single end-to-end policy. Open-sourcing the data pipeline and deployment code lowers the barrier for other labs and strengthens the case that embodied AI on affordable platforms like the G1 is becoming reproducible. HALO explicitly separates a 35B-class Mixture-of-Experts model for high-level task sequencing from a 2B model for action generation, with a reinforcement-learning motion tracker handling low-level joint control. The validation is a sim-to-real transfer onto the Unitree G1, a compact humanoid with roughly 23 degrees of freedom, and the released code covers data generation, training, and deployment.

telegram · zaihuapd · Nov 7, 13:35

**Background**: Sim-to-real transfer means training a robot policy inside a physics simulator and then deploying it on physical hardware, which is hard because simulated dynamics never perfectly match reality, so researchers use techniques like domain randomization and system identification to close the gap. The Unitree G1 is a low-cost bipedal humanoid widely used as a research platform for embodied AI, and the Qwen models are Alibaba&\#x27;s open-weight large language models, used here as the reasoning and action-generation backbone of the control stack.

<details><summary>References</summary>
<ul>
<li><a href="https://www.robocloudhub.tech/learn/blog/sim-to-real-transfer">Sim - to - Real Transfer in Robotics</a></li>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G1_Humanoid Robot Functions ... - Unitree G1</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#sim-to-real`, `#humanoid-robots`, `#Qwen`, `#Apple-research`

---

<a id="item-5"></a>
## [Anthropic Said to Launch IPO Roadshow Next Week, Targeting Week of Nov 16](https://www.theinformation.com/briefings/anthropic-proceed-ipo-roadshow-next-week) ⭐️ 6.0/10

People familiar with the matter say Anthropic plans to begin its IPO roadshow next week, pitching potential investors ahead of a listing targeted for the week of November 16, just before the U.S. Thanksgiving holiday. The report also claims the company had been expected to raise more than $80 billion at a $1.5 trillion valuation, but may now seek a lower price amid recent market jitters. If accurate, an Anthropic listing would be one of the largest AI-related market debuts ever and a bellwether for how public investors value frontier model developers after two weeks of sharp swings in tech and AI stocks. Its pricing would likely be read as a benchmark for peers such as OpenAI and for the wider AI infrastructure and startup funding ecosystem. The item is a short, single-sourced digest rather than primary reporting, and the stated figures — a $1.5 trillion valuation with over $80 billion raised — are extraordinary and unverified, so the timeline and terms should be treated as unconfirmed. The report notes only that concerns about AI stocks and AI spending could push Anthropic toward a valuation below the earlier floated number, without giving specifics.

telegram · zaihuapd · Nov 7, 01:27

**Background**: Anthropic is an AI company that develops the Claude family of large language models and positions itself around AI safety research. An IPO roadshow is the marketing phase in which a company and its underwriters present the business to institutional investors over roughly one to two weeks to gauge demand and set a price range before shares actually begin trading. Listing in the week of November 16 would mean compressing that process before the Thanksgiving holiday, when U.S. markets slow down.

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#business/finance`, `#unverified news`

---

<a id="item-6"></a>
## [Turkey Uses AI to Recover 100 Looted Antiquities From the US](https://www.artnews.com/art-news/news/turkey-uses-ai-tech-100-looted-antiquities-us-1234804634/) ⭐️ 6.0/10

Turkey&\#x27;s Ministry of Culture put roughly 200 repatriated artifacts on display at the Istanbul Archaeology Museum, headlined by a Bronze Age statue from the Burun mound site that was looted in the 1960s and 44 terracotta architectural panels dating from 700 to 480 BC. The return of about 100 objects from the United States was supported by TraceART, an AI platform launched in 2025 that scans global auction sites and social media for suspicious listings. This is a concrete case of AI being used operationally in cultural-heritage law enforcement, turning scattered online auction and social-media listings into actionable leads for repatriation claims. If the approach scales, it could become a template for other source countries seeking to reclaim looted antiquities and could raise the cost of selling undocumented pieces through online marketplaces. Investigators combined lead isotope analysis, mold-shape comparison of the objects, and automated scanning by TraceART, which flags listings rather than replacing expert authentication. Turkey says it has recovered more than 26,700 artifacts since 1980, and the latest batch includes material spanning the Bronze Age through the classical period.

telegram · zaihuapd · Nov 7, 03:43

**Background**: Provenance research tries to establish where an object was made and how it left its country of origin; lead isotope analysis does this for metal objects by matching the trace isotopic ratios of lead in a bronze or silver piece to known ore deposits. TraceART is a Geneva-based due-diligence tool for cultural property that aggregates a directory of databases and performs image analysis. Under frameworks such as the 1970 UNESCO Convention, countries file claims for objects that surface in foreign auctions, museums, and private collections — which is why rapid detection of listings online matters.

<details><summary>References</summary>
<ul>
<li><a href="https://traceart.app/index.en.html">TraceArt | Cultural property provenance verification</a></li>
<li><a href="https://pubs.rsc.org/ra/article/13/28/19595/824103/Lead-isotope-analysis-for-provenancing-ancient">Lead isotope analysis for provenancing ancient materials: a ...</a></li>
<li><a href="https://www.nature.com/articles/s41598-025-88909-1">Provenancing ancient materials with lead isotopes: overlap ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cultural heritage`, `#artifact repatriation`, `#archaeology`, `#machine learning`

---

<a id="item-7"></a>
## [SoftBank and ABB Weigh China Carve-Out to Salvage $5.4B Robotics Deal](https://www.bloomberg.com/news/articles/2026-11-07/softbank-abb-weigh-china-carve-out-to-salvage-robotics-deal) ⭐️ 6.0/10

SoftBank and ABB are considering carving ABB&\#x27;s China robotics business into a separate entity with a differentiated equity structure, in an attempt to rescue the $5.4 billion acquisition that China&\#x27;s foreign investment security review office blocked on Thursday. SoftBank is reportedly leading the effort, though people familiar with the matter say the workaround may fail and ABB is also evaluating alternatives such as finding another buyer. The blocked deal shows how far Beijing&\#x27;s security review can reach into large cross-border industrial-automation M&amp;A, and any carve-out template that succeeds here could become a model for foreign firms trying to sell China-based assets. A failed deal would also complicate SoftBank&\#x27;s push into robotics and leave ABB&\#x27;s China robotics unit in limbo at a time when industrial automation is increasingly treated as strategically sensitive. The proposed structure would place the China business in a standalone entity with different equity rights, which could let the two sides separate the Chinese assets from the rest of the transaction. The China robotics business is reportedly valued at $2 billion to $3 billion, roughly half the headline deal price, and both ABB and SoftBank declined to comment.

telegram · zaihuapd · Nov 7, 11:24

**Background**: ABB is a Swiss-Swedish industrial giant whose robotics division makes factory automation arms and systems, and SoftBank has been building a portfolio of robotics and automation assets. China&\#x27;s foreign investment security review, run through an inter-ministerial working mechanism, can block foreign acquisitions of domestic companies or of foreign companies with substantial China operations when they touch on national security or critical technology. Because the target has significant operations inside China, the deal fell within that review&\#x27;s scope rather than under a conventional antitrust filing.

**Tags**: `#robotics`, `#M&amp;A`, `#china-regulation`, `#industrial-automation`, `#foreign-investment`

---