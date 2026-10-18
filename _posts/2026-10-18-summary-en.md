---
layout: default
title: "Horizon Summary: 2026-10-18 (EN)"
date: 2026-10-18 23:01:54 +0000
lang: en
report: default
---

> From 35 items, 7 important content pieces were selected

---

1. [Google Research open-sources Harness², a recursive agent optimization framework](#item-1) ⭐️ 8.0/10
2. [Anthropic Lobbies for AI Safety Bill With $1B and 50-Death Thresholds](#item-2) ⭐️ 7.0/10
3. [Nature Study: Microplastics Generate Reactive Free Radicals in Watery Environments](#item-3) ⭐️ 7.0/10
4. [Reported 11-Day Breach at EY Exposed Goldman Sachs Wealth Clients](#item-4) ⭐️ 6.0/10
5. [Anthropic Consults Law Firms on Rules for AI Agents That Negotiate](#item-5) ⭐️ 6.0/10
6. [NVIDIA Speeds Up Kimi K3 Inference via Upstream vLLM Kernel Work](#item-6) ⭐️ 6.0/10
7. [US AI Infrastructure Boom Shows Cracks as $10T Buildout Faces Return Test](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Google Research open-sources Harness², a recursive agent optimization framework](https://github.com/google-research/harness2) ⭐️ 8.0/10

Google Research released Harness², an Apache 2.0 licensed, plug-and-play framework that recursively optimizes LLM agents without touching model weights, reporting gains of up to 11.5 points on WorkBuddy-Bench. It implements two connected levels of recursion \(task-level refinement of the current task&\#x27;s harness and a higher harness-level loop\), and supports both parallel and sequential recursion modes along with integrated benchmark suites. The release points to a practical alternative to fine-tuning for improving agent performance: gains come from better scaffolding and iterative self-refinement rather than gradient updates, which makes the approach cheaper, model-agnostic, and applicable to closed-weight APIs. For teams building coding or office-work agents, an Apache 2.0, benchmark-integrated harness from Google Research is an immediately usable baseline that could shift effort from model training toward harness engineering. The claimed gains are measured on WorkBuddy-Bench, a Tencent benchmark for coding agents covering Code, Web, Office, and Security work domains, and the 11.5-point figure is a best-case result rather than a uniform improvement. Recursion is described as refining the harness with contrastive feedback, and because it is plug-and-play the framework adds inference-time overhead in exchange for avoiding any weight updates or fine-tuning pipeline.

telegram · zaihuapd · Oct 18, 11:24

**Background**: An agent harness is the scaffolding around a base language model — system prompts, tool definitions, control flow, and retry/verification logic — that largely determines how well an LLM performs on multi-step tasks. Harness² belongs to a line of research on self-improving agents that adapt at inference time \(via memory, self-rewriting traces, or harness refinement\) instead of through fine-tuning, and WorkBuddy-Bench is a recently introduced multi-domain benchmark built from real developer, PM, QA, ops, and security tasks used to score such agents.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google-research/harness2">GitHub - google - research / harness 2 · GitHub</a></li>
<li><a href="https://huggingface.co/papers/2610.14224">Paper page - Harness ^2: Recursive Agent Harnessing for an Open...</a></li>
<li><a href="https://github.com/Tencent/workbuddy-bench">GitHub - Tencent/workbuddy-bench</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#agent framework`, `#recursive optimization`, `#Google Research`, `#open source`

---

<a id="item-2"></a>
## [Anthropic Lobbies for AI Safety Bill With $1B and 50-Death Thresholds](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model) ⭐️ 7.0/10

Anthropic is lobbying lawmakers to pass an AI safety bill that would only allow the US government to block a model&\#x27;s release if it could cause more than $1 billion in damages or more than 50 deaths or injuries. The draft would have independent, Commerce Department-registered third parties regularly evaluate labs and models, mandate reporting of bioweapon, AI cyberattack, or loss-of-control risks within 72 hours, and make the Commerce Department the only agency able to seek a stop order, subject to a federal judge&\#x27;s ruling. The proposal would write a very high bar for government intervention into law, effectively reserving federal stop powers for catastrophic scenarios and centralizing enforcement in a single agency. Because Anthropic is one of the leading frontier labs, its draft is likely to shape how the broader AI industry and lawmakers frame pre-deployment oversight in the United States. Notably, the bill would preempt other federal agencies — and potentially state regulators — from ordering a model halted, leaving the Commerce Department to seek a court order backed by third-party evaluation evidence within the 72-hour reporting window. The thresholds are far above the harms typically discussed in AI safety debates, which critics may argue makes the trigger nearly unreachable.

telegram · zaihuapd · Oct 18, 12:40

**Background**: Anthropic is a San Francisco-based AI public benefit corporation founded in 2021 by former OpenAI staff, including CEO Dario Amodei, and is the maker of the Claude model family. The company positions itself around AI safety research, so its lobbying on safety legislation carries unusual weight. In the US, there is still no comprehensive federal law governing frontier model releases; oversight has instead come piecemeal through executive orders, agency actions, and state-level bills, which is why a proposal defining a federal &quot;stop&quot; mechanism is significant.

<details><summary>References</summary>
<ul>
<li><a href="https://tech-insider.org/anthropic-ai-safety-bill-lawmakers-2026/">Anthropic Pitches $1B AI Safety Bill to Lawmakers</a></li>
<li><a href="https://www.gate.com/news/detail/anthropic-proposes-ai-safety-bill-with-1-billion-damage-threshold-25036808">Anthropic Proposes AI Safety Bill with $1 Billion Damage ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI regulation`, `#Anthropic`, `#AI governance`, `#tech policy`

---

<a id="item-3"></a>
## [Nature Study: Microplastics Generate Reactive Free Radicals in Watery Environments](https://futurism.com/health-medicine/microplastics-research-food-water-consumption-packaging) ⭐️ 7.0/10

A study published in Nature reports that commodity microplastics exhibit an &quot;intrinsic physicochemical activity&quot; in water, spontaneously generating reactive oxygen species \(free radicals\) rather than behaving as chemically inert material. The authors, including Columbia University professor Wei Min, argue that as plastics fragment and their surface area explodes, these radicals could chemically modify and damage biomolecules and cells. The finding challenges the long-held assumption that plastics are chemically inert, offering a mechanism by which microplastics could cause biological harm without releasing any additive or leached chemical. Because microplastics are ubiquitous in water, food packaging and the food supply chain — earlier work counted more than 240,000 particles per liter of bottled water — the result could reshape how regulators and researchers assess human health and environmental risk. The Nature paper attributes the effect to fundamental water–hydrophobe interactions — interfacial water restructuring, electrostatics and partial charge transfer — showing that reactive oxygen species generation increases with interfacial hydrophobicity and correlates strongly with interfacial electrostatics. The proposed mechanism is a functional hypothesis; the evidence comes largely from controlled lab experiments with plastic particles in water and serum rather than direct in-vivo human measurement, so dose–response relationships in real exposures remain unresolved.

telegram · zaihuapd · Oct 18, 13:55

**Background**: Microplastics are plastic fragments smaller than 5 millimeters, shed from packaging, textiles, tires and the breakdown of larger debris; their tiny size gives them an enormous surface-area-to-volume ratio relative to bulk plastic. Free radicals, including reactive oxygen species, are unstable molecules that readily react with DNA, proteins and lipids, and are linked to oxidative stress, aging and disease. Conventional toxicology has largely treated plastic particles as inert carriers whose danger came from the chemicals they absorb or leach, so the idea that the plastic surface itself drives chemistry in water is a significant shift.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-11141-y">Intrinsic physicochemical activity at microplastic–water ...</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/42875572/">Intrinsic physicochemical activity at microplastic-water ...</a></li>
<li><a href="https://www.newscientist.com/article/2593857-microplastics-may-produce-harmful-molecules-if-they-enter-our-blood/">Microplastics may produce harmful molecules if they... | New Scientist</a></li>

</ul>
</details>

**Tags**: `#microplastics`, `#environmental health`, `#reactive radicals`, `#Nature study`, `#public health`

---

<a id="item-4"></a>
## [Reported 11-Day Breach at EY Exposed Goldman Sachs Wealth Clients](https://www.reddit.com/r/finance/comments/1x9ft6s/how_an_11day_breach_at_ey_quietly_exposed_goldman/) ⭐️ 6.0/10

A post on Reddit&\#x27;s r/finance forum claims that an 11-day security breach at Ernst &amp; Young \(EY\) exposed client data belonging to Goldman Sachs&\#x27; wealth management business. The submission itself consists only of a headline and an outbound link, with no technical write-up, affected-record counts, or dates included in the text. The story matters because it points to third-party risk: banks such as Goldman Sachs routinely share client data with audit, tax, and consulting firms, so a compromise at a vendor can expose customers a bank never directly lost control of. If confirmed at scale, an incident like this could trigger regulatory notification obligations and erode client trust in wealth management relationships, where confidentiality is a core selling point. The reported duration of 11 days refers to how long the intrusion is said to have gone undetected, which is the detail most relevant to evaluating the breach. However, the post provides no information on what categories of data were taken, how the exposure was discovered, or whether affected clients were notified, so the claim remains unverified.

reddit · r/finance · /u/Akkeri · Oct 18, 22:06

**Background**: EY is one of the &\#x27;Big Four&\#x27; professional services firms and provides audit and advisory work to many of the world&\#x27;s largest financial institutions, which means its systems often hold sensitive client records. Wealth management arms like Goldman Sachs&\#x27; serve high-net-worth individuals and handle personal financial information, making them a high-value target for attackers. In the financial sector, data breaches typically trigger mandatory disclosure rules and supervisory scrutiny, which is why even unconfirmed reports about breaches attract attention.

**Tags**: `#cybersecurity`, `#data breach`, `#finance`, `#privacy`, `#incident reporting`

---

<a id="item-5"></a>
## [Anthropic Consults Law Firms on Rules for AI Agents That Negotiate](https://www.ft.com/content/f7c26ac0-f5f2-443a-86b2-39d62f7920a9?syn-25a6b1a6=1) ⭐️ 6.0/10

Anthropic is reportedly working with law firms and other legal institutions to define &quot;negotiation norms&quot; for AI agents that bargain over prices, resolve complaints and disputes, or negotiate salaries on a user&\#x27;s behalf. The company is also considering giving agents user-signed authorization documents that would formally delegate negotiating authority to the agent. If AI agents routinely bargain with other AI agents, the absence of shared norms and clear authorization could produce unfair outcomes, disputed deals and unclear legal accountability. Anthropic&\#x27;s move signals that agent-to-agent commerce is moving from demos toward something that needs rules, contracts and liability frameworks, which will affect merchants, employers, consumers and the platforms hosting these agents. Anthropic is reportedly hiring lawyers and humanities scholars as &quot;Conceptual Reasoning Fellows&quot; to improve Claude in domains where reliable training data is scarce, such as negotiation. Supporting research includes a Harvard Business School study by assistant professor Michelle Vaccaro that ran more than 180,000 agent-to-agent negotiations across scenarios including employment contracts and rental bargaining, and Anthropic&\#x27;s own internal experiment in which Claude agents bought and sold books in a simulated marketplace, where agents set to be &quot;ruthless&quot; held a slight edge.

telegram · zaihuapd · Oct 18, 07:07

**Background**: AI agents are software systems that can carry out multi-step tasks — such as comparing offers, haggling and closing a deal — with limited human supervision. Once such agents interact with each other rather than with people, questions arise about what they are permitted to concede, how a user proves an agent was authorized to act, and who is liable if a deal goes wrong. Researchers have proposed frameworks for authenticated, authorized and auditable delegation of authority to AI agents, which is roughly what a user-signed authorization document would try to formalize in practice.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ft.com/content/f7c26ac0-f5f2-443a-86b2-39d62f7920a9?syn-25a6b1a6=1">Anthropic turns to lawyers to help AI agents strike deals</a></li>
<li><a href="https://the-decoder.com/anthropic-consults-law-firms-to-set-fair-negotiation-norms-before-ai-agents-start-cutting-deals/">Anthropic consults law firms to set fair negotiation norms ...</a></li>
<li><a href="https://www.media.mit.edu/publications/authenticated-delegation-and-authorized-ai-agents/">Authenticated Delegation and Authorized AI Agents - MIT Media Lab</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#agent-to-agent negotiation`, `#AI governance`, `#Anthropic`, `#legal/regulatory`

---

<a id="item-6"></a>
## [NVIDIA Speeds Up Kimi K3 Inference via Upstream vLLM Kernel Work](https://x.com/SemiAnalysis_/status/2111627094878790023) ⭐️ 6.0/10

SemiAnalysis reported that NVIDIA achieved 423 tokens per second per user on the 2.8-trillion-parameter Kimi K3 model, a 1.68x speedup on identical hardware, using upstream vLLM optimizations. The work centers on decode-specific kernels written in CUTLASS&\#x27;s CuTe DSL by Benjamin from NVIDIA&\#x27;s CentML team, combined with megakernel fusion. The gains come from changes landed upstream in vLLM rather than a proprietary fork, so any vLLM user running large mixture-of-experts models on NVIDIA GPUs can potentially benefit. It also shows single-kernel decode designs are becoming a practical lever for squeezing throughput out of frontier-scale models that are otherwise memory-bandwidth bound. The 423 tok/s figure is per-user decode throughput, meaning it reflects single-stream latency-oriented performance rather than aggregate batched throughput. Megakernel fusion collapses the whole forward pass into one GPU kernel launch, which mainly pays off at small batch sizes where kernel launch overhead and memory bandwidth dominate; SemiAnalysis also noted NVIDIA is working on upstream vLLM support for models such as DeepSeek v4.1.

telegram · zaihuapd · Oct 18, 08:20

**Background**: vLLM is a widely used open-source LLM serving engine, and changes merged into its upstream repository propagate to a large share of production deployments. Decode — the phase where a model emits one token at a time — is memory-bandwidth bound, so vendors invest heavily in custom kernels instead of relying on generic GPU code. Megakernels take this further by fusing an entire transformer forward pass into a single kernel launch to eliminate launch overhead, while CuTe DSL is CUTLASS&\#x27;s Python-embedded language for authoring such high-performance GPU kernels. Kimi K3 is a 2.8-trillion-parameter model, and vLLM&\#x27;s own blog previously reported up to 370 tok/s per user with DSpark speculative decoding on 16 GB300 NVL72 GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-07-27-k3">Kimi K3 Is Here: Efficient Day-0 Support on vLLM | vLLM Blog</a></li>
<li><a href="https://github.com/BodhiHu/mirage-llm-megakernel">GitHub - BodhiHu/mirage-llm-megakernel: Mirage: Automatically ...</a></li>
<li><a href="https://theorempath.com/topics/megakernels">Megakernels. End-to-End Fused LLM Inference Kernels</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#NVIDIA`, `#kernel optimization`, `#Kimi K3`

---

<a id="item-7"></a>
## [US AI Infrastructure Boom Shows Cracks as $10T Buildout Faces Return Test](https://www.ft.com/content/9ea5a37d-15c9-4d5b-94d6-719048c9cd3c?syn-25a6b1a6=1) ⭐️ 6.0/10

Rising financing costs, permitting delays and growing public opposition have stalled at least 47 large US data-center projects since 2026, according to the Financial Times, which also cites estimates that only about 35% of planned US data-center projects are highly feasible. Markets reacted sharply: CoreWeave, the Nvidia-backed AI cloud provider, fell more than 11% on Friday, and the Philadelphia Semiconductor Index logged its eighth consecutive decline, matching its longest losing streak since 2006. The AI boom has been underpinned by projections of more than $10 trillion in US AI infrastructure spending between 2025 and 2032, so any sign that projects are slipping undermines the demand assumptions behind chipmakers, cloud providers and utilities alike. If financing and permitting bottlenecks persist, the market&\#x27;s willingness to fund the AI capex cycle could tighten, affecting everything from semiconductor order books to the valuations of AI-native cloud companies. The article frames financing pressure as the key bottleneck for AI infrastructure, with the semiconductor index&\#x27;s eight-session slide and CoreWeave&\#x27;s double-digit drop read as concrete market signals of repricing rather than isolated events. The roughly 35% feasibility figure suggests most announced data-center capacity may never be built as planned, and the piece is an industry-analysis digest rather than a technical deep dive.

telegram · zaihuapd · Oct 18, 08:52

**Background**: The AI buildout requires enormous physical infrastructure — GPU-dense data centers that consume large amounts of electricity and must be sited, permitted and connected to power grids before they can serve model training and inference workloads. CoreWeave is one such operator: an American cloud-computing company based in Livingston, New Jersey, that as of 2026 runs 51 AI data centers specialized for high parallel-computing performance through heavy use of GPUs. Companies like it sit downstream of Nvidia&\#x27;s chips and upstream of the AI developers renting compute, which is why financing conditions and project pipelines matter for the whole supply chain.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#industry analysis`, `#capex`, `#semiconductors`

---