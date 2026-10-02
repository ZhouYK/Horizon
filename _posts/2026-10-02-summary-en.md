---
layout: default
title: "Horizon Summary: 2026-10-02 (EN)"
date: 2026-10-02 23:03:27 +0000
lang: en
report: default
---

> From 160 items, 8 important content pieces were selected

---

1. [arXiv Caps Submissions at Two Papers Per Person Per Month](#item-1) ⭐️ 7.0/10
2. [Google Research&\#x27;s Cogentic Orchestrates Multi-Agent Proof Discovery](#item-2) ⭐️ 7.0/10
3. [Anthropic Adds Mods to Claude Code for TypeScript Customization](#item-3) ⭐️ 7.0/10
4. [Anthropic Urges Australia to Allow AI Training on Copyrighted Works](#item-4) ⭐️ 6.0/10
5. [Multiple Claude Users in Hong Kong Report Account Suspensions](#item-5) ⭐️ 6.0/10
6. [US carriers AT&amp;T, T-Mobile, Verizon plan satellite joint venture](#item-6) ⭐️ 6.0/10
7. [Sub2API billing bypass flaw fixed in version 0.2.13](#item-7) ⭐️ 6.0/10
8. [Raspberry Pi raises prices again: 2 GB Pi 4 now costs $67.50](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [arXiv Caps Submissions at Two Papers Per Person Per Month](https://www.huxiu.com/article/4895127.html) ⭐️ 7.0/10

arXiv announced that starting October 1, each submitter may upload at most two papers per calendar month, a rule that applies across all disciplines including computer science, mathematics, and physics. Rejected submissions still consume that month&\#x27;s quota. The cap directly reshapes daily publishing practice for the global research community, since arXiv is the default venue for pre-publication dissemination in AI/ML, physics and mathematics. It is also an explicit institutional admission that the flood of low-quality, AI-generated preprints has become unsustainable and can no longer be absorbed by volunteer moderation. For multi-author papers, only the person who actually submits the manuscript is charged with the submission; co-authors are not affected by the limit. The trigger was a record 40,363 submissions in September — a 35-year high — with AI-category papers growing more than sixfold in two years and consuming scarce human moderation capacity.

telegram · zaihuapd · Oct 2, 06:21

**Background**: arXiv is the world&\#x27;s largest preprint server, where researchers post papers publicly before or instead of formal peer review, making it the primary channel for rapid sharing in physics, mathematics and computer science. Because posting on arXiv is free and near-instant, the platform has become a target for automated and LLM-generated manuscripts that add little scientific value. Moderation there has historically relied on volunteer and part-time moderators who screen submissions by subject area.

**Tags**: `#arXiv`, `#academic-publishing`, `#AI-research`, `#preprints`, `#open-science`

---

<a id="item-2"></a>
## [Google Research&\#x27;s Cogentic Orchestrates Multi-Agent Proof Discovery](https://arxiv.org/abs/2609.40324v1) ⭐️ 7.0/10

Google Research has introduced Cogentic, a multi-agent harness built on Gemini that splits proof discovery into roles — an orchestrator that decides what to work on, multiple provers drafting proofs in parallel, and dedicated verifiers that adversarially check the results — with confirmed findings written into a persistent verification ledger. The team reports that Cogentic produced new results on five open problems in online learning, auction theory, and mechanism design, all independently validated by domain experts and elaborated in companion papers. If the claims hold up, Cogentic represents a shift from using LLMs to solve already-solved textbook problems toward automated discovery on genuinely open research questions, which is the bar that recent AI-for-mathematics milestones such as AlphaProof and AlphaGeometry have been measured against. A working &\#x27;prove-and-adversarially-verify&\#x27; loop would also give theoretical computer science and economics a practical assistive tool, potentially compressing the time between posing a conjecture and obtaining a publishable proof. Cogentic&\#x27;s outputs are natural-language proofs rather than machine-checked formal proofs in Lean or Coq, so correctness rests on human expert review plus the system&\#x27;s own adversarial verifier and ledger rather than on a formal kernel. Caveats worth noting: the result is currently circulating via a single aggregated social post with no independent corroboration, and the cited arXiv identifier \(2609.40324v1\) appears future-dated, so the paper&\#x27;s existence and peer-review status should be confirmed at the source before treating the five results as established.

telegram · zaihuapd · Oct 2, 12:04

**Background**: Automated theorem proving has traditionally relied on formal proof assistants such as Lean and Coq, where every step is checked by a machine but human guidance is often needed to find the overall strategy. Recent work such as Prover Agent combines LLMs for informal reasoning with a formal assistant for feedback, while other systems explore multi-agent setups in which a separate &\#x27;adversarial&\#x27; agent is tasked solely with finding errors in proposed proofs. Cogentic extends this line of work by organizing many such agents around an orchestrator and a persistent verification ledger, targeting open problems in theoretical computer science rather than benchmark problem sets.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.40324v1">Cogentic: Multi-Agent Orchestration for Automated Proof Discovery</a></li>
<li><a href="https://academy.dair.ai/papers/cogentic-multi-agent-orchestration-for-automated-proof-discovery-2609.40324">Cogentic: Multi-Agent Orchestration for Automated Proof ...</a></li>
<li><a href="https://arxiv.org/abs/2506.19923">[2506.19923] Prover Agent: An Agent-Based Framework for ... Prover Agent: An Agent-Based Framework for Formal ... GitHub - RiccardoBiosas/LeanGPT: Experiments with interactive ... GitHub - Jiahao004/DeepTheorem ICML Prover Agent: An Agent-based Framework for Formal ... Prover Agent: An Agent-based Framework for Formal ... Prover Agent: An Agent-based Framework for Formal ...</a></li>

</ul>
</details>

**Tags**: `#multi-agent-systems`, `#automated-theorem-proving`, `#AI-for-mathematics`, `#LLM-agents`, `#Google-Research`

---

<a id="item-3"></a>
## [Anthropic Adds Mods to Claude Code for TypeScript Customization](https://claude.com/blog/claude-code-mods) ⭐️ 7.0/10

Anthropic launched mods for Claude Code, small TypeScript functions that let developers rewrite prompts, block risky commands, add custom UI panes, or replace built-in features. Mods ship as plugins and are initially supported in the CLI and desktop app, with some built-in features already converted into mods and more migrations planned. This turns Claude Code from a closed agentic coding tool into an extensible platform, letting teams enforce their own policies and workflows without waiting on Anthropic. It also mirrors the plugin-centric architecture competitors like DeepSeek Harness are betting on, signaling that extensibility is becoming a key battleground for AI coding agents. Mods run with the same permissions as Claude Code and are not sandboxed, so the official guidance is to install only from trusted sources; users can also ask Claude Code to write a mod for them. Mods are distributed through the plugin system, meaning they can be shared and reused across projects rather than being one-off local scripts.

telegram · zaihuapd · Oct 2, 12:32

**Background**: Claude Code is Anthropic&\#x27;s agentic coding tool that runs in the terminal or desktop, understands a codebase, and executes tasks through natural-language commands. Historically, users could influence its behavior mainly through configuration files and prompts; mods introduce a proper extension API written in TypeScript, similar to how editors like VS Code expose plugins. DeepSeek Harness, an open-source agent harness from DeepSeek AI, is built on an explicit &\#x27;everything-is-a-plugin&\#x27; architecture, which makes the two designs directly comparable.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/blog/claude-code-mods">Customize Claude Code with mods in TypeScript | Claude by ...</a></li>
<li><a href="https://code.claude.com/docs/en/plugins/mods/overview">Mods overview - Claude Code Docs</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">DeepSeek Harness - GitHub</a></li>

</ul>
</details>

**Discussion**: The included commentary is brief: DeepSeek Harness team lead Cui Tianyi quote-tweeted an Anthropic employee&\#x27;s post to offer congratulations, and pointed out how similar the feature is to DeepSeek Harness&\#x27;s &\#x27;everything-is-a-plugin&\#x27; design. Community members responded lightheartedly that good designs converge, without any substantial technical debate or criticism.

**Tags**: `#Claude Code`, `#Anthropic`, `#Developer Tools`, `#AI Coding`, `#Extensibility`

---

<a id="item-4"></a>
## [Anthropic Urges Australia to Allow AI Training on Copyrighted Works](https://www.theguardian.com/technology/2026/oct/02/anthropic-ai-opt-out-australia-copyright-abc-cannibalisation-of-news) ⭐️ 6.0/10

Anthropic is proposing that the Australian government conditionally permit tech companies to train AI models on Australian copyrighted works under an &quot;opt-out&quot; regime, in which rights holders would have to actively request exclusion rather than grant permission in advance. The push comes as public broadcasters ABC and SBS oppose loosening copyright rules, demanding that AI companies accept copyright and privacy regulation and compensate media, with ABC warning that journalism risks being &quot;cannibalised.&quot; The decision will help define whether opt-out becomes the global default for AI training data or whether licensing and compensation regimes prevail, directly affecting AI developers, publishers, and creators far beyond Australia. Because major labs including Anthropic and OpenAI are lobbying in person at a parliamentary hearing, the Australian debate is becoming a test case for how democracies balance AI competitiveness against creators&\#x27; rights. The Australian government has already ruled out creating a text and data mining \(TDM\) exemption in copyright law, so the debate now centres on alternative arrangements such as conditional opt-out rules. An opt-out model places the compliance burden on rights holders, who must discover that their work was used and actively register a reservation, a point critics argue makes it weak protection in practice.

telegram · zaihuapd · Oct 2, 03:34

**Background**: Generative AI models are trained on very large corpora of text, images and audio that are often scraped from the open web, raising the legal question of whether such ingestion infringes copyright and whether it can be covered by a text and data mining exception. The EU, UK and Japan have adopted some form of TDM exception, while Australia&\#x27;s government has declined to follow that path; opt-out mechanisms such as machine-readable rights reservations \(for example in robots.txt\) are the main alternative model being debated worldwide. Australia&\#x27;s Joint Select Committee on Artificial Intelligence was established in August 2026 to examine AI&\#x27;s opportunities and risks, following Prime Minister Anthony Albanese&\#x27;s pledge to build a single national AI framework led by an Office of AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spruson.com/australia-on-ai-copyright-text-and-data-mining-exemption/">Australia ’s position on AI and copyright - Text and Data Mining ...</a></li>
<li><a href="https://www.aph.gov.au/Parliamentary_Business/Committees/Joint/Artificial_Intelligence">Joint Select Committee on Artificial Intelligence</a></li>

</ul>
</details>

**Tags**: `#AI copyright`, `#AI regulation`, `#Anthropic`, `#policy`, `#Australia`

---

<a id="item-5"></a>
## [Multiple Claude Users in Hong Kong Report Account Suspensions](https://www.newmobilelife.com/2026/10/01/claude-bans-hk-user/) ⭐️ 6.0/10

On October 1, multiple Claude users in Hong Kong reported that they could not log in, receiving &quot;account suspended&quot; or &quot;access denied&quot; messages, and some of those affected were paying Claude Pro subscribers. The reports spread through local tech communities and forums, where affected users and network engineers speculated that commercial VPN data-center IPs, payment and region verification, and frequent switching of VPN nodes may be the cause, while Anthropic has not yet publicly responded. This shows that even paying subscribers can be locked out when access depends on VPN workarounds, and it highlights how regional availability policies can abruptly cut users off from a tool they rely on for work. It also underscores a growing trend of AI services enforcing region and risk controls more aggressively, which affects anyone in unsupported markets who accesses these tools through VPNs. The suspected triggers are technical rather than content-related: VPN servers hosted in cloud data centers use IP ranges that services can easily identify and flag, and rapid switching between nodes can look like bot or account-sharing behavior. Notably, the bans are unconfirmed by Anthropic, so the exact enforcement rule, whether affected accounts can be appealed, and whether paid time is refunded all remain unclear.

telegram · zaihuapd · Oct 2, 04:19

**Background**: Claude is Anthropic&\#x27;s AI assistant, and Anthropic restricts Claude&\#x27;s availability to a list of supported countries and regions, so users elsewhere often connect through a VPN to sign up and log in. VPNs typically route traffic through data centers owned by cloud providers, which makes their IP addresses recognizable and easily blocked; many online services also cross-check payment methods, billing country, and login location to detect circumvention. Because frequent node switching creates login patterns that resemble fraud or bot activity, risk-control systems may suspend accounts automatically rather than after a human review.

<details><summary>References</summary>
<ul>
<li><a href="https://veepn.com/blog/residential-vs-datacenter-ip/">Residential vs. Datacenter IP: Why VPNs Get Blocked - VeePN</a></li>
<li><a href="https://sunsetbrowser.app/blog/vpn-account-risk-control-rescue-guide-en">How to Rescue a VPN-Flagged Account: 2026 Self-Audit and ...</a></li>
<li><a href="https://www.ippriv.com/blog/how-websites-detect-and-block-vpns">How Websites Detect and Block VPNs (And How to Avoid It in ...</a></li>

</ul>
</details>

**Discussion**: Discussion in local Hong Kong tech communities and forums is largely composed of affected users seeking help, with peers trading theories about VPN IPs, payment checks, and node switching rather than debating the policy itself. The overall tone is practical and frustrated, and there is no official reply from Anthropic to anchor the claims.

**Tags**: `#Anthropic`, `#Claude`, `#Hong Kong`, `#Account Bans`, `#Regional Restrictions`

---

<a id="item-6"></a>
## [US carriers AT&amp;T, T-Mobile, Verizon plan satellite joint venture](https://www.ithome.com/1/009/320.htm) ⭐️ 6.0/10

AT&amp;T, T-Mobile, and Verizon announced they have reached a preliminary agreement of intent to form a joint venture that would use satellite technology to identify network coverage gaps and improve connectivity in remote and rural areas. The carriers also aim to boost communications reliability during emergencies such as natural disasters and to use spectrum resources more efficiently, but no details on the venture&\#x27;s structure, satellite plan, coverage scope, or service model have been released. It is unusual for the three largest US mobile operators — normally fierce competitors — to cooperate on infrastructure, and such a joint effort could accelerate the convergence of satellite and terrestrial networks while improving rural and emergency connectivity for millions of underserved users. It also signals that satellite-based coverage, long a niche for specialized providers, is becoming a mainstream part of US carrier strategy. The announcement is only a statement of intent: the joint venture&\#x27;s ownership split, satellite technology or partner selection, target coverage areas, timeline, and commercial model all remain undisclosed. It is also unclear whether the carriers intend to use satellites mainly as backhaul for remote cell sites or to deliver direct-to-device service to ordinary handsets, two technically very different approaches.

telegram · zaihuapd · Oct 2, 09:07

**Background**: Mobile networks rely on terrestrial cell towers, and building towers in remote or sparsely populated areas is often uneconomical, which creates coverage gaps that satellites can help fill. Satellites are typically used in one of two ways: as backhaul that connects a remote cell site to the core network, or as part of a non-terrestrial network \(NTN\) that links directly to user devices. Low-earth-orbit \(LEO\) constellations are especially relevant here because, compared with traditional geostationary satellites, they offer lower latency and stronger signals, and the telecom industry is already working to standardize NTN support in 5G and future 6G systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.p1sec.com/blog/satellite-connectivity-in-mobile-networks-bridging-gaps-for-remote-and-critical-operations">Satellite connectivity for LTE and 5G coverage - p1sec.com</a></li>
<li><a href="https://diversedaily.com/satellite-communication-for-mobile-networks-how-satellites-enhance-mobile-communication-networks/">Satellite Communication for Mobile Networks: How Satellites ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2095809925003236">Evolution of Satellite Communication Systems Toward 5G/6G for ...</a></li>

</ul>
</details>

**Tags**: `#telecom`, `#satellite-communication`, `#rural-connectivity`, `#industry-news`, `#US-carriers`

---

<a id="item-7"></a>
## [Sub2API billing bypass flaw fixed in version 0.2.13](https://github.com/Wei-Shaw/sub2api) ⭐️ 6.0/10

A community Telegram post warned that Sub2API versions up to 0.2.12 contain a billing-logic flaw that, under certain configurations, lets requests return successfully without being charged, and the same post was later updated to confirm that version 0.2.13 fixes the issue. Operators who run Sub2API as an API proxy could silently lose revenue or mis-bill downstream users, and the bug erodes trust in the usage accounting that the entire subscription-to-API conversion model depends on, so anyone self-hosting should upgrade promptly. The flaw only triggers under specific configuration conditions and is silent in nature — requests succeed but no billing record is generated — so users are advised to audit billing and reconciliation data, watch for anomalous Key usage, and track upstream fixes; the advisory provides no CVE identifier or technical root-cause analysis.

telegram · zaihuapd · Oct 2, 10:52

**Background**: Sub2API is an open-source AI API proxy that turns subscription accounts for Claude, OpenAI, Gemini, and Antigravity into API endpoints, so operators can share or resell model access. Because it sits between end users and upstream providers, it must track per-key usage accurately in order to charge correctly; a logic bug in that accounting path means usage can go unrecorded even though the request itself succeeds. The project is hosted on GitHub at Wei-Shaw/sub2api.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Sub2API">Sub2API</a></li>
<li><a href="https://www.sub2api.com/">Home - Sub2API</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#billing`, `#Sub2API`, `#open-source`

---

<a id="item-8"></a>
## [Raspberry Pi raises prices again: 2 GB Pi 4 now costs $67.50](https://www.theregister.com/personal-tech/2026/10/02/once-a-35-computer-the-2-gb-raspberry-pi-4-now-costs-6750/5300774) ⭐️ 6.0/10

Raspberry Pi has raised prices on two of its most popular boards, adding $12.50 to both the 2 GB Raspberry Pi 4 \(now $67.50\) and the Raspberry Pi 5 \(now $77.50\), citing higher memory costs. The company is advising customers to consider older models such as the Pi 3B or to reassess how much RAM their projects actually need. The Raspberry Pi was long defined by its $35 price point, so a 2 GB Pi 4 costing nearly double that erodes the low-cost appeal that made it the default choice for schools, hobbyists, and embedded developers. Since Raspberry Pi boards are widely used in industrial and commercial products, the increase propagates into the bill of materials for a large number of small hardware businesses. Raspberry Pi CEO Eben Upton has said prices will come back down once memory prices fall, but Micron has warned the DRAM/NAND supply crunch could persist into 2028, driven largely by AI datacenter demand for HBM crowding out conventional memory capacity. The current $67.50 price is the result of a climb that started with a pandemic-era &quot;temporary&quot; increase from $35 to $45 that was never reversed.

telegram · zaihuapd · Oct 2, 13:18

**Background**: Raspberry Pi is a family of low-cost single-board computers originally launched in 2012 at a $35 target price, widely used for education, hobby projects, and as embedded controllers in commercial hardware. The 2 GB Raspberry Pi 4 arrived in 2020 at $35, while the newer Pi 5 offers a faster processor and requires a stronger 5V/4A USB-C power supply. The current price pressure comes from the broader memory market: AI training and inference have driven huge demand for high-bandwidth memory \(HBM\), tightening supply and raising prices for the standard DRAM and NAND used in devices like the Pi.

<details><summary>References</summary>
<ul>
<li><a href="https://thenextweb.com/news/micron-record-quarter-memory-shortage-2028">Micron sees the memory shortage tightening into 2028 after a record...</a></li>
<li><a href="https://www.rockpapershotgun.com/ram-shortages-are-only-getting-worse-and-will-last-until-at-least-2028-micron-boss-declares-from-atop-a-mountain-of-money">RAM shortages are only getting worse and will last until at ...</a></li>
<li><a href="https://forums.pimoroni.com/t/raspberry-pi-3-vs-4-vs-5-comprehensive-comparison-guide/26533">Raspberry Pi 3 vs 4 vs 5: Comprehensive Comparison Guide</a></li>

</ul>
</details>

**Tags**: `#Raspberry Pi`, `#hardware pricing`, `#memory shortage`, `#embedded systems`, `#supply chain`

---