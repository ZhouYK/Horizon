---
layout: default
title: "Horizon Summary: 2026-09-18 (EN)"
date: 2026-09-18 23:04:14 +0000
lang: en
report: ai
---

> From 188 items, 10 important content pieces were selected

---

1. [Rust Team Warns of Targeted Attacks on Prominent Rustaceans](#item-1) ⭐️ 8.0/10
2. [Alibaba&\#x27;s Qwen3.8-Omni-Flash: Native Multimodal, 1M Context, 98% Cheaper Audio](#item-2) ⭐️ 8.0/10
3. [Figure Releases Helix 2.5, Lifting Zero-Shot Home Chores to 56%](#item-3) ⭐️ 8.0/10
4. [Claude Code Adds AGENTS.md Support as CLAUDE.md Fallback](#item-4) ⭐️ 7.0/10
5. [Thomas Ptacek: Use LLMs as Copyeditors, Never Adopt Their Phrasing](#item-5) ⭐️ 7.0/10
6. [US Military&\#x27;s AI-Generated False Intel Report Reportedly Caused Close Call](#item-6) ⭐️ 7.0/10
7. [Kimi K3 Now Available on Amazon Bedrock](#item-7) ⭐️ 7.0/10
8. [Anthropic Taps Accenture as First Embedded AI Safety Evaluator](#item-8) ⭐️ 7.0/10
9. [Deep learning designs dual-function materials to detect and capture toxic sulfur gases](#item-9) ⭐️ 7.0/10
10. [Anthropic warns AI systems are increasingly capable of building their own successors](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Rust Team Warns of Targeted Attacks on Prominent Rustaceans](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) ⭐️ 8.0/10

On September 17, 2026, Adam Harvey and the crates security team published a warning — amplified by Simon Willison — that an ongoing campaign is targeting rust-lang members and the owners of popular crates in order to compromise their devices and accounts and use them to publish malware. The attackers set up video calls framed as job, project, or contract opportunities, then use them as a vector to get the target to install something \(such as a purportedly missing audio codec\) or to execute a command, for example one planted on the clipboard. Because a single compromised maintainer account can push a malicious release of a crate that thousands of downstream projects depend on, this campaign threatens the integrity of the open-source software supply chain that nearly all modern software — Rust-based or not — ultimately relies on. Developers and security teams need to treat maintainer identity and release approval as high-value attack surface, not just a code-quality concern. The documented lure techniques are a fake &quot;missing audio codec&quot; install prompt and a command placed on the clipboard for the victim to run, both delivered during a video call that appears legitimate. This exact playbook was already used successfully in the August 2026 supply chain attack against the arrayref crate and others; Simon Willison notes that dependency cooldowns — delaying upgrades to new releases for a few days so someone else can spot the attack first — are currently the best available defense.

rss · Simon Willison · Sep 17, 23:59

**Background**: Rust&\#x27;s packages are called crates, and they are published to crates.io and consumed through Cargo, Rust&\#x27;s package manager; &quot;Rustacean&quot; is the community&\#x27;s nickname for Rust developers. Ownership of a crate on crates.io grants publishing rights to it, which means compromising one owner&\#x27;s account or laptop can be enough to ship malware to every project that depends on that crate. Supply chain attacks of this kind work by attacking the people rather than the code, since the dependency graph of any large project includes dozens or hundreds of individual maintainers whose accounts are all potential entry points.

<details><summary>References</summary>
<ul>
<li><a href="https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack?trk=article-ssr-frontend-pulse_little-text-block">Rust Supply-Chain Attack: arrayref , internment, and... - StepSecurity</a></li>
<li><a href="https://doc.rust-lang.org/rust-by-example/crates.html">Crates - Rust By Example</a></li>
<li><a href="https://docs.rs/crate/arrayref/latest">arrayref 0.3.9 - Docs.rs</a></li>

</ul>
</details>

**Tags**: `#security`, `#rust`, `#supply-chain-attack`, `#social-engineering`, `#open-source`

---

<a id="item-2"></a>
## [Alibaba&\#x27;s Qwen3.8-Omni-Flash: Native Multimodal, 1M Context, 98% Cheaper Audio](https://www.aibase.com/news/31158) ⭐️ 8.0/10

On the 18th, Alibaba&\#x27;s Qwen team launched Qwen3.8-Omni-Flash, a native omni-modal model that accepts text, image, audio and video inputs with a context window of up to 1 million tokens. The team reports an average improvement of over 25% across 29 benchmarks versus its predecessor, alongside a 98% reduction in audio processing cost, with the model now available on Qwen AI. Cutting audio cost by 98% while supporting million-token context could make long-form audio and video agentic applications — video editing, MV creation, film commentary and AV-to-text summarization — economically practical rather than demo-only. It also sharpens Alibaba&\#x27;s position in the race toward &quot;any-to-any&quot; omni-modal models alongside systems such as Google&\#x27;s Gemini Omni. The key architectural claim is that Qwen3.8-Omni-Flash natively integrates multimodal understanding and agent capabilities at the model level, rather than concatenating separate speech and image recognition modules, and the release mentions roughly 30 evaluations covering coding, GUI and audio-video agentic tasks. As the report comes from a single aggregator with no published benchmark breakdown or pricing table, the 25% and 98% figures should be treated as vendor claims pending independent verification.

aibase · AIbase · Sep 18, 14:01

**Background**: Earlier &quot;multimodal&quot; systems were usually pipelines: a speech recognizer and an image captioner converted audio and pictures into text, which a language model then processed, losing tone, timing and visual nuance along the way. A native omni-modal model instead handles several modalities inside one architecture, which is what enables tasks like understanding a film clip or operating a graphical user interface directly. The context window is the amount of information a model can attend to at once; 1 million tokens corresponds to very long documents or hours of transcribed audio, and a GUI agent is an AI that perceives and clicks through on-screen interfaces rather than calling APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://aimlapi.com/blog/what-is-gemini-omni-googles-any-to-any-multimodal-ai">What Is Gemini Omni? Google&#x27;s Any-to-Any Multimodal AI</a></li>
<li><a href="https://medium.com/@deferare/is-gemma-4-truly-a-native-multimodal-model-dissecting-the-architecture-c2231689735c">Is Gemma 4 Truly a Native Multimodal Model ? | Medium</a></li>
<li><a href="https://www.linkedin.com/posts/farhat-boughizene-95737a96_for-the-past-several-months-ive-been-working-activity-7450991547388510208-xjFZ">Anthropic&#x27;s 1 M Token Context Window : A Breakthrough... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#Multimodal AI`, `#Qwen`, `#Alibaba`, `#Large Language Models`, `#AI Model Release`

---

<a id="item-3"></a>
## [Figure Releases Helix 2.5, Lifting Zero-Shot Home Chores to 56%](https://www.aibase.com/news/31151) ⭐️ 8.0/10

Figure has released Helix 2.5, which it describes as its most advanced humanoid robot neural network, a single foundation model pretrained on Index, Figure&\#x27;s dataset of human behavior. In tests across 30 previously unseen homes in the Bay Area, zero-shot success on chores such as tidying living rooms, folding towels and making beds rose from 9% to 56%. The result targets the core bottleneck for humanoid robots in the real world: generalizing to messy, unfamiliar environments without collecting data or fine-tuning on site. A jump of this size from human-behavior pretraining suggests robot policies can scale the way large language models scale, rather than relying on teleoperation and per-task engineering. Figure isolated Index&\#x27;s contribution by comparing policies with identical task-specific data, architecture and downstream training, varying only whether they received Index pretraining, and it reports that each of the 30 homes and the objects in them were entirely unseen, with zero data collected there and zero fine-tuning. Even so, a 56% success rate means roughly two in five attempts still fail, so reliability remains well short of what commercial home deployment would require.

aibase · AIbase · Sep 18, 11:01

**Background**: Humanoid robot foundation models aim to give one neural network a general set of physical skills, much like a language model handles many text tasks. Zero-shot generalization means the robot attempts new tasks in new places without extra training data or fine-tuning, a long-standing weak point in robot learning. Figure AI&\#x27;s Helix is a vision-language-action model family that maps camera input and instructions to whole-body motion, and Index is Figure&\#x27;s collection of human behavior data used to pretrain it, so the robot can learn skills from human video instead of only from robot teleoperation recordings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization">Helix 2.5: Zero-Shot 30-Home Generalization - figure.ai</a></li>
<li><a href="https://www.humanoidsdaily.com/news/figure-helix-2-5-30-unseen-homes">Figure’s Helix 2.5 Takes on Chores in 30 Unseen... | Humanoids Daily</a></li>
<li><a href="https://startupfortune.com/figure-ais-helix-25-robot-made-beds-in-30-homes-it-had-never-seen/">Figure AI&#x27;s Helix 2.5 Robot Made Beds in 30 Homes It Had ...</a></li>

</ul>
</details>

**Tags**: `#humanoid robotics`, `#foundation models`, `#robot learning`, `#zero-shot generalization`, `#Figure AI`

---

<a id="item-4"></a>
## [Claude Code Adds AGENTS.md Support as CLAUDE.md Fallback](https://simonwillison.net/2026/Sep/18/thariq-shihipar/) ⭐️ 7.0/10

Thariq Shihipar announced that Claude Code now supports AGENTS.md: starting in version 2.1.277, if a folder contains no CLAUDE.md, Claude will check for and use AGENTS.md instead. The feature is implemented as a built-in &quot;mod&quot; — part of Claude Code&\#x27;s upcoming harness-customization system — with its source published in the anthropics/claude-code repository. This marks Anthropic&\#x27;s adoption of the cross-tool AGENTS.md convention, meaning developers can maintain a single project-instruction file that works across Claude Code, Codex CLI, Cursor, Copilot and other agents instead of duplicating instructions per tool. It&\#x27;s a meaningful step toward interoperability in the fast-growing AI coding-agent ecosystem, where fragmented configuration formats have been a recurring friction point. AGENTS.md is only a fallback: CLAUDE.md still takes precedence when both files exist in the same folder, so existing Claude Code workflows are unaffected. Because support is built as a mod rather than hard-coded behavior, users will reportedly be able to build custom versions of project instructions themselves, and the built-in mods ship inside the binary without imposing any policy of their own.

rss · Simon Willison · Sep 18, 19:09

**Background**: CLAUDE.md is a file developers place in a project root to give Claude Code persistent context — project conventions, build commands, architecture notes — so the agent behaves consistently across sessions. AGENTS.md serves the same purpose but as a tool-agnostic standard: it originated at OpenAI and is now stewarded by the Linux Foundation&\#x27;s Agentic AI Foundation, and as of mid-2026 it ships in 28+ tools and appears in over 60,000 open-source repositories. &quot;Mods&quot; are Anthropic&\#x27;s emerging mechanism for customizing the Claude Code harness — the surrounding agent scaffolding — of which four currently ship built into the product.

<details><summary>References</summary>
<ul>
<li><a href="https://vibecoding.app/blog/agents-md-guide">AGENTS.md Guide (2026): Copilot, Cursor &amp; More</a></li>
<li><a href="https://github.com/anthropics/claude-code/tree/main/mods">claude-code/mods at main · anthropics/claude-code · GitHub</a></li>
<li><a href="https://code.claude.com/docs/en/memory">How Claude remembers your project - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AGENTS.md`, `#AI coding agents`, `#Anthropic`, `#developer tools`

---

<a id="item-5"></a>
## [Thomas Ptacek: Use LLMs as Copyeditors, Never Adopt Their Phrasing](https://simonwillison.net/2026/Sep/17/how-to-write-with-an-llm/) ⭐️ 7.0/10

Thomas Ptacek published a piece titled &quot;How To Write With An LLM&quot; arguing that large language models should be used as copyeditors rather than writing assistants, anchored by his &quot;Rule Number One: You may not use a single word an LLM suggests to you.&quot; Simon Willison endorsed the principle, noting that he refuses to let LLMs write his blog content but does use them for fact-checking, spelling, grammar, and as an occasional thesaurus. It offers a concrete, memorable discipline for the growing number of writers, developers, and knowledge workers who already use AI in their drafting workflow, at a moment when readers are increasingly sensitive to the telltale style of AI-generated prose. The rule draws a practical line between using models to sharpen your own writing and letting them substitute for your voice. Ptacek shows a screenshot of his personal LLM copyediting tool and shares a prompt to help readers build their own, and he later posted his full system prompt in a comment on Hacker News. Willison links his own proofreading prompt and says the never-use-a-suggested-phrase rule feels right both because LLM text has a distinctive &quot;weird smell&quot; and because the strictness itself keeps him disciplined.

rss · Simon Willison · Sep 17, 23:37

**Background**: Large language models are transformer-based neural networks trained on enormous text corpora to generate, summarize, translate, and analyze language, and they now underpin mainstream chatbots such as ChatGPT, Claude, and Gemini. Prompt engineering is the practice of structuring natural-language instructions, including system prompts and few-shot examples, to steer a model toward a desired output. Because these models tend to produce statistically smooth, recognizable prose, writers worry that leaning on them for sentences rather than for corrections erodes their individual style.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_engineering">Prompt engineering</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI writing`, `#prompt engineering`, `#AI ethics`, `#writing workflow`

---

<a id="item-6"></a>
## [US Military&\#x27;s AI-Generated False Intel Report Reportedly Caused Close Call](https://news.google.com/rss/articles/CBMijAFBVV95cUxQNURhdTZha1pnekJvMjV5cE9VQ0tpQmZuSXVfbFVzLVBDbDY1b28zMUluUVNzMUlPZnE2Qk5OLXRVcUVsRkVfZ3d2ZVpvaW9JOGFZUE00SV9uQ0xWcE5QOGlzXzB2bkRaWjZiZVpKblZBU2tsOTdvMllIdTRKb21ScUlwNlIzSDdaTFR0Rg?oc=5) ⭐️ 7.0/10

CNN reported exclusively, citing sources, that the US military experienced a close call after an AI system produced a false intelligence report; a related headline states the erroneous AI report &quot;almost started a war&quot; between the US and China. The story centers on how an unreliable AI output fed into a high-stakes military intelligence workflow rather than being caught before it influenced decision-making. The incident is a concrete, real-world illustration that AI &quot;hallucinations&quot; are not merely an academic or consumer-facing nuisance but can carry geopolitical and life-and-death consequences when deployed in defense and intelligence settings. It will likely intensify pressure on governments and vendors to define verification, human-review and accountability requirements before AI is embedded deeper into military command and analysis pipelines. Details remain thin because the item is essentially a headline and one-line summary, so the specific model, vendor, service branch and exact timeline of the incident are not established in the available material. What is technically notable is that hallucinations are typically described as fluent, confident outputs that are false or unsupported by source material, and that many safety guardrails are implemented as per-request filters rather than as end-to-end checks on how an output is later used.

google\_news · CNN · Sep 18, 16:55

**Background**: In AI, a hallucination is generated content that is false, unsupported, or inconsistent with the information the output is supposed to be based on; the term is closely associated with large language models \(LLMs\), which can produce plausible-sounding statements, citations and summaries that are simply wrong. Researchers commonly separate factuality, meaning correspondence with independently verifiable facts, from faithfulness, meaning consistency with a supplied source or context — an output can be faithful to a flawed source yet false in the real world. Because incorrect material is expressed in the same confident, fluent style as correct material, hallucinations are fundamentally a reliability problem, and documented cases range from fabricated academic references to bogus judicial decisions and inaccurate summaries. Military adoption of AI has grown alongside these concerns, with debate about how far automated analysis should be trusted in command, targeting and intelligence workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_hallucination">AI hallucination</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_%28artificial_intelligence%29">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://memu.pro/blog/openai-military-safety-guardrails">OpenAI Publishes Its Military Contract Red Lines — Safety ... | MemU</a></li>

</ul>
</details>

**Tags**: `#ai-safety`, `#military-ai`, `#hallucination`, `#ai-governance`, `#defense-technology`

---

<a id="item-7"></a>
## [Kimi K3 Now Available on Amazon Bedrock](https://news.google.com/rss/articles/CBMijAFBVV95cUxPZEc4TDRPSkJzZUl2bHJoNm5HNkhpcGtBX2U0V1l3dVJDRlh5YkpwRkZaTDkwcDBfZVN3UU1ackFYY0NPMU5sRU5LVVFmRHhySUJwVjZlWXlNTkw4b0swYW1zUVZQSldHV19aTzBfeC1waGFOeGd0MThBOEo5bnVFSDl2VkIxSndKVWZYWA?oc=5) ⭐️ 7.0/10

AWS announced that Moonshot AI&\#x27;s Kimi K3 is now available on Amazon Bedrock, adding the 2.8-trillion-parameter model to the managed service&\#x27;s catalog of foundation models. The listing follows K3&\#x27;s release and expands the set of frontier models that Bedrock customers can call through a single unified API. It gives enterprise customers a way to use one of the strongest Chinese open-weights models without leaving AWS, and it signals the continued normalization of Chinese frontier models inside major US cloud marketplaces. This matters for teams weighing model choice against procurement, compliance and data-residency constraints, since Bedrock offers a governed, serverless path rather than direct third-party API access. Kimi K3 is a 2.8-trillion-parameter model — reportedly the largest open-weights model ever released — built on Moonshot&\#x27;s Kimi Delta Attention and Attention Residuals, with multimodal image and video input and a &quot;Swarm&quot; deep-research mode using hundreds of sub-agents. Its custom license requires revenue sharing of up to 30% for inference providers earning more than US$20 million annually, a condition that could shape how third-party clouds and resellers package it.

google\_news · Amazon Web Services \(AWS\) · Sep 18, 16:52

**Background**: Amazon Bedrock is a serverless AWS service launched in 2023 that exposes foundation models from multiple AI vendors through a unified API, competing with Microsoft Foundry and Google Cloud&\#x27;s equivalent offerings. Kimi is a chatbot and model family from the Chinese company Moonshot AI, which ships open-weights models; K2 at roughly one trillion parameters arrived in July 2025, followed by K2.5 in January 2026 and K2.6 in April 2026. K3&\#x27;s performance is reported to have led the Chinese field and rivalled frontier models from OpenAI and Anthropic, and Kimi models have been used as bases or for post-training by US projects such as Cursor&\#x27;s Composer 2 and Cognition AI&\#x27;s Devin.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Amazon_Bedrock">Amazon Bedrock</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3?ref=apifox.com">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Tags**: `#AWS Bedrock`, `#Kimi K3`, `#LLM`, `#Cloud AI`, `#Model Release`

---

<a id="item-8"></a>
## [Anthropic Taps Accenture as First Embedded AI Safety Evaluator](https://news.google.com/rss/articles/CBMipgFBVV95cUxNSnN4LUdjc1JEOHpBaU9kc2hlb3BmX2Nmb1NodlYwbnZ0R1BlRWtxWld2cW1ZdWlMZnQwYWk3bGl0d0JlR3RuZU5PaTE3YkhmRm1JamZfcndhcWZCM3RlN1ZXb09qQ1RJUjRKSmFKS2lxNk9PMTZoR3lfMkVTOXVpaVdpY2JVX3k3N1hiSGREQ3ZtZFdudUkzYm9JLUdiZG1Bc05FSXZR?oc=5) ⭐️ 7.0/10

Anthropic announced on September 18, 2026 that it has selected consulting giant Accenture as its first &quot;embedded evaluator,&quot; placing Accenture staff inside the company to independently test the safety of its frontier AI models. Both firms committed to investing at least $1 billion each over the next five years — roughly $2 billion in total — to build capacity for independent frontier-AI evaluation. This is the first concrete implementation of Anthropic CEO Dario Amodei&\#x27;s proposal to put third-party evaluators inside frontier labs, turning a public safety argument into an operational governance arrangement. If rival labs adopt similar embedded oversight, independent evaluation could shift from a voluntary gesture into an industry norm, changing how AI risks are audited and disclosed. Accenture&\#x27;s role is built around its newly acquired AI division Faculty, and the money is framed as long-term capacity building rather than a one-off audit engagement. A key open question is how much weight an evaluator paid by the lab it evaluates can carry, since neither company has published the specific standards, metrics, or escalation procedures the embedded team will use.

google\_news · The Washington Post · Sep 18, 22:49

**Background**: Frontier AI labs have traditionally evaluated their own models internally, which critics argue creates a conflict of interest when the same organization both builds and grades the technology. On September 12, 2026, Anthropic CEO Dario Amodei published an essay titled &quot;We Must Pace the Frontier,&quot; proposing a three-step plan to deliberately pace the speed of AI development — not an immediate halt to training — so that safety controls can keep up with capabilities. &quot;Embedded evaluation,&quot; the model now being tested with Accenture, means outside experts work on-site inside the lab and get access to models before or around deployment rather than reviewing them after the fact.

<details><summary>References</summary>
<ul>
<li><a href="https://www.washingtonpost.com/technology/2026/09/18/anthropic-picks-consulting-firm-monitor-ai-safety/">Anthropic picks consulting firm to monitor AI safety - The ...</a></li>
<li><a href="https://www.anthropic.com/news/accenture-embedded-evaluation">Partnering with Accenture on embedded evaluation \ Anthropic</a></li>
<li><a href="https://www.cnbc.com/2026/09/18/anthropic-accenture-ai-safety.html">Anthropic selects Accenture as first embedded evaluator in ...</a></li>
<li><a href="https://darioamodei.com/post/we-must-pace-the-frontier">We Must Pace the Frontier - Dario Amodei</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#Anthropic`, `#AI governance`, `#industry news`, `#responsible AI`

---

<a id="item-9"></a>
## [Deep learning designs dual-function materials to detect and capture toxic sulfur gases](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBRTEVadTNTVzRQNHFTRkNKYjMzeWpyZk0tc0xoa3NtSm1BZ0V3Y1g3NWR1TTBxOFh2T3ViZVF3QW9tNjFUZ3JBXzVKeHB2cnAzQ2JJX2RlQmprSzlj?oc=5) ⭐️ 7.0/10

Scientists have used deep learning methods to design new materials that can simultaneously detect and capture toxic sulfur gases, according to a report highlighted by EurekAlert\!. The work demonstrates a multifunctional material design approach in which a single computational pipeline identifies candidates that both sense and absorb hazardous sulfur-containing gases. Toxic sulfur gases such as hydrogen sulfide and sulfur dioxide are common industrial and environmental hazards, so materials that combine real-time sensing with capture could simplify monitoring and remediation into a single step. The result also adds to the growing evidence that AI-driven screening can shorten the traditionally slow, trial-and-error process of discovering functional materials. The approach relies on deep learning models to predict material properties and screen large candidate spaces before experimental validation, rather than testing compounds one by one. As with most computational materials studies, the practical value will depend on whether the predicted candidates can be synthesized at scale and remain stable under real operating conditions such as humidity, temperature and gas concentration.

google\_news · EurekAlert\! · Sep 18, 21:19

**Background**: Deep learning has become a major tool in materials discovery: models such as graph neural networks can learn from databases of known crystal structures and predict which hypothetical compounds are likely to be stable or have desired properties, an approach popularized by systems like Google DeepMind&\#x27;s GNoME, which screened millions of candidate crystals. This falls under the broader &\#x27;AI for Science&\#x27; trend, in which machine learning is applied across chemistry, physics and biology to accelerate discovery. Sulfur gases such as hydrogen sulfide \(H2S\) are both highly toxic and corrosive, which is why sensing and capture materials are an active area of research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/d42473-025-00161-3">AI for Science 2025 | Nature Research Custom</a></li>
<li><a href="https://github.com/google-deepmind/materials_discovery">GitHub - google-deepmind/ materials _ discovery · GitHub</a></li>
<li><a href="https://www.technologynetworks.com/informatics/news/deep-learning-algorithm-could-remove-materials-discovery-bottleneck-339063">Deep Learning Algorithm Could Remove Materials Discovery ...</a></li>

</ul>
</details>

**Tags**: `#deep learning`, `#materials science`, `#toxic gas detection`, `#AI for science`, `#sulfur gases`

---

<a id="item-10"></a>
## [Anthropic warns AI systems are increasingly capable of building their own successors](https://news.google.com/rss/articles/CBMiygFBVV95cUxQNG50OEZHWS00Vmp5clkxR3hKR1RIY0NuLW1pbXhwaV9wNlg2TGUyeU5lemR5Zll1a2NhOTB6cUQ5R3RCM21wNTJ1X2ppWXJTX0djVHpWVUJjUFA4em1qa0NHMDVWVWc4U3pMM0FfZFMyeERkNVBSY2tYX0hRaTFXTkFrNlVoeXgtLXY5SURZLWZ1MG5UX1pmbzRjWGZIMGRCSFhrQWxia1E1ZzBGOUE1VDJnLTdJdXFiREpmc1N3Y1pZM1MwcGJTaGJR?oc=5) ⭐️ 7.0/10

On Thursday, AI developer Anthropic stated that AI systems are becoming increasingly capable of building future versions of themselves, saying its own Claude model is helping to build the next version of itself. The statement adds to mounting concerns about the risks of increasingly powerful AI technology. Anthropic is one of the largest frontier AI labs, so its public warning lends weight to AI-safety arguments about self-improvement that have long been treated as speculative. If accepted by policymakers and other labs, such warnings could shape future safety evaluations, deployment rules and regulation of frontier models. The claim was reported only as a brief news snippet, with no technical evidence, benchmark data or description of how much of the work is autonomous versus human-directed; Anthropic currently describes Claude as assisting with engineering tasks rather than independently rewriting its own architecture. Notably, decades of research on recursive self-improvement have so far shown no sign of the hypothesized &quot;intelligence explosion&quot; resulting in superintelligence.

google\_news · LinkedIn · Sep 18, 19:23

**Background**: Recursive self-improvement is a hypothesized process in which an AI system rewrites its own code to make itself more capable, potentially entering a feedback loop that accelerates its own improvement — an idea tied to I. J. Good&\#x27;s 1965 &quot;intelligence explosion&quot; model and the broader technological-singularity hypothesis. In practice, today&\#x27;s models are used mainly to write and debug code, and critics such as Stuart Russell and Peter Norvig argue that technological progress tends to follow an S-curve that levels off rather than accelerating without limit.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-improving_AI">Self-improving AI</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#Anthropic`, `#self-improving AI`, `#recursive self-improvement`, `#AI risk`

---