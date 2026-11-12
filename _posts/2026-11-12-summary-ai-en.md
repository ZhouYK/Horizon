---
layout: default
title: "Horizon Summary: 2026-11-12 (EN)"
date: 2026-11-12 23:03:38 +0000
lang: en
report: ai
---

> From 187 items, 10 important content pieces were selected

---

1. [Baidu Unveils ERNIE 5.5 Flash Preview, Promises Open Weights by November 25](#item-1) ⭐️ 8.0/10
2. [OpenAI Codex Comes to Amazon Bedrock for Enterprise Rollouts](#item-2) ⭐️ 7.0/10
3. [Claude API Adds Per-Message Effort Control Mid-Conversation](#item-3) ⭐️ 7.0/10
4. [Runway Open-Sources 27B Praxis-1 World Action Model Under Apache 2.0](#item-4) ⭐️ 7.0/10
5. [CACM Explores the Shift From Single Intelligent Agents to Agent Societies](#item-5) ⭐️ 6.0/10
6. [186 Fake AI Domains Funnel Victims Into ClickFix Scams and Browser Hijackers](#item-6) ⭐️ 6.0/10
7. [Google adapts TPU silicon into specialized systems for AI agents and security](#item-7) ⭐️ 6.0/10
8. [Matrix-Game4.0 brings 60 FPS AI game-world generation to browser on one consumer GPU](#item-8) ⭐️ 6.0/10
9. [Anthropic Upgrades Claude Connectors With Full-Screen Interactive Apps](#item-9) ⭐️ 6.0/10
10. [Alibaba Teases Qwen4 With New Core Architecture and a Preview in the Qwen App](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Baidu Unveils ERNIE 5.5 Flash Preview, Promises Open Weights by November 25](https://www.aibase.com/news/32278) ⭐️ 8.0/10

Baidu released ERNIE 5.5 Flash Preview, the first post-trained model built on its previously released ERNIE 5.5 Flash Base, featuring 280 billion total parameters, 14 billion active parameters per token, and a 1 million-token context window. Baidu has pledged to publish the full model weights by November 25, pending that deadline. If Baidu follows through, it would release one of the largest open-weight models to date, strengthening the open-source ecosystem and intensifying competition with Chinese and Western labs that increasingly ship large models with permissive or open licenses. Developers and enterprises that cannot afford closed API lock-in would gain a powerful long-context option they can self-host and fine-tune. The 14B active parameters indicate the model uses a mixture-of-experts architecture, keeping inference costs far below what a full 280B dense model would require, and Baidu highlights coding, agentic tasks, 3D modeling, and content creation as strengths. Caveats remain: &quot;preview&quot; status means behavior and weights could change, and an advertised 1M-token context does not guarantee reliable reasoning across the full window.

aibase · AIbase · Nov 12, 16:01

**Background**: Large language models are typically built in two stages: pretraining on massive text corpora to learn general patterns, then post-training — supervised fine-tuning, reinforcement learning from human feedback and similar techniques — to turn the raw base model into an aligned, instruction-following assistant. A context window is the amount of text a model can read and reason over in a single request, so a 1M-token window allows whole codebases, books, or long document sets to be processed at once. &quot;Open weights&quot; means the trained parameters are downloadable, allowing self-hosting and fine-tuning, though this is distinct from fully open-source releases that also disclose training data and code. ERNIE is Baidu&\#x27;s flagship model family, and open-sourcing a model of this scale would mark a significant shift in its strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://ernie.baidu.com/zh/release/ernie-5-5-flash-preview/">Introducing ERNIE 5.5 Flash Preview · ERNIE</a></li>
<li><a href="https://openrouter.ai/baidu/ernie-5.5-flash-preview:free">ERNIE-5.5-Flash-Preview (free) - API Pricing &amp; Providers</a></li>
<li><a href="https://pytorch.org/blog/a-primer-on-llm-post-training/">A Primer on LLM Post-Training - PyTorch</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-source models`, `#Baidu ERNIE`, `#long-context`, `#AI industry news`

---

<a id="item-2"></a>
## [OpenAI Codex Comes to Amazon Bedrock for Enterprise Rollouts](https://news.google.com/rss/articles/CBMigwFBVV95cUxNaTMtak5LN2ZUam9haGF5ekhPR1hvdFNyU2lybEN0YU0xdWtnNFBEZ2o4clJNT050OXZXWXJtRm9iOFZLVHI5SEc1aWdmb3NHM1Y4UE5MdUc5MlNPaGE2SEJ6cjhyeUlEaGFNeUxUeVRYTGQzeUZNdDB4YmZfNENOVDVsZw?oc=5) ⭐️ 7.0/10

AWS has published a guide announcing that OpenAI Codex can now run with Amazon Bedrock as its model backend, letting enterprises roll out the coding agent on AWS infrastructure. A companion OpenAI Help Center article confirms Codex supports OpenAI models served through Bedrock, along with the local workflows and client settings required to configure it. The integration lets enterprises keep Codex traffic inside their existing AWS accounts, so billing, IAM permissions, logging and data-governance policies apply the same way they do to other Bedrock workloads. It also marks a notable shift in cloud AI competition, since OpenAI models become purchasable through the platform of its chief rival in cloud infrastructure. AWS frames the announcement as a practical guide for platform, security and finance teams, covering access, governance and cost decisions rather than new model capabilities. The OpenAI documentation notes that only certain models and local workflows are supported when Codex is pointed at Bedrock, so teams must verify model availability and credential setup before migrating.

google\_news · Amazon Web Services \(AWS\) · Nov 11, 23:35

**Background**: OpenAI Codex is an AI coding agent that writes, reviews and maintains code, and it can be used both inside IDEs and as a standalone agent. Amazon Bedrock is AWS&\#x27;s managed service that provides access to foundation models from multiple providers through a single API, with built-in scaling, security and governance controls. Previously, using Codex meant consuming OpenAI&\#x27;s own API directly; routing it through Bedrock moves procurement and policy enforcement into the customer&\#x27;s AWS environment.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock/">OpenAI Codex on Amazon Bedrock | Artificial Intelligence</a></li>
<li><a href="https://help.openai.com/en/articles/20001252-use-codex-with-amazon-bedrock">Use Codex with Amazon Bedrock - OpenAI Help Center</a></li>
<li><a href="https://help.openai.com/en/articles/20001253-configure-codex-with-amazon-bedrock">Configure Codex with Amazon Bedrock - OpenAI Help Center</a></li>

</ul>
</details>

**Tags**: `#OpenAI Codex`, `#Amazon Bedrock`, `#AWS`, `#AI coding`, `#cloud AI`

---

<a id="item-3"></a>
## [Claude API Adds Per-Message Effort Control Mid-Conversation](https://www.aibase.com/news/32271) ⭐️ 7.0/10

Anthropic has shipped a beta capability in the Claude API that lets developers change the effort level partway through a conversation by inserting a role: &quot;system&quot; message with empty content and a new output\_config.effort value, without touching the request&\#x27;s top-level configuration. The change takes effect from the next user message that carries new input, requires the mid-conversation-output-config-2026-07-01 beta header, and keeps the prompt cache intact. Until now effort was fixed for the whole session, forcing teams to either pay for maximum depth on every turn or restart a conversation — and lose the cached prefix — to switch. Mid-conversation control lets builders spend high effort on the hard reasoning steps and drop to cheaper, faster levels for routine turns, directly improving the cost/latency tradeoff for agentic and multi-step applications. Effort lives in output\_config.effort, defaults to high on most models and medium on Opus 5.5, and returns an error rather than silently downgrading when a model/level combination is unsupported. The feature is documented as supported across Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5, and on Amazon Bedrock, Google Cloud and Azure, though it remains in beta.

aibase · AIbase · Nov 12, 12:01

**Background**: Claude models expose an &quot;effort&quot; parameter that trades response depth against speed and token cost, similar to reasoning-budget controls in other LLM APIs; it is set in the output\_config object of a request. Prompt caching, configured via cache\_control breakpoints with 5-minute or 1-hour TTLs, lets repeated prompt prefixes be reused so cached input costs far less and responses start faster. Because a cached prefix only matches if the earlier part of the request is byte-identical, any change to top-level parameters used to invalidate the cache — which is exactly why Anthropic routed the mid-conversation override through an in-band system message instead of the top-level field.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/effort-per-message">Per-message effort - Claude Platform Docs</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/effort">Effort - Claude Platform Docs</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching">Prompt caching - Claude Platform Docs - Anthropic</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude API`, `#LLM infrastructure`, `#API design`, `#cost optimization`

---

<a id="item-4"></a>
## [Runway Open-Sources 27B Praxis-1 World Action Model Under Apache 2.0](https://www.aibase.com/news/32267) ⭐️ 7.0/10

Runway has released Praxis-1, a 27-billion-parameter world action model built on a Mixture-of-Experts Diffusion Transformer architecture, with full model weights plus inference and fine-tuning code under the Apache 2.0 license, permitting commercial use. Runway claims the model tops an authoritative robotics leaderboard and says it can be fine-tuned on a user&\#x27;s own embodiment and run on their own hardware. Fully open weights plus training/inference code for a model of this size is still rare in embodied AI, where leading robotics foundation models have tended to stay behind closed APIs, so Praxis-1 lowers the barrier for academic labs and startups that cannot train such models from scratch. If the leaderboard claim holds up, it also signals that video-pretrained world models are becoming a practical route to real robot control rather than a research curiosity. The release includes all weights, inference code and fine-tuning code, and Runway explicitly frames the model as turning video pretraining into control for real robots. Beyond the parameter count and architecture name, however, the announcement offers no benchmark numbers, no named leaderboard, no evaluation protocol and no independent verification, and the 27B total may not reflect the per-token active parameter count typical of MoE designs.

aibase · AIbase · Nov 12, 11:01

**Background**: A world action model \(WAM\) combines a predictive world model — one that forecasts how a scene will evolve — with action generation, so a single learned system can both imagine the consequences of a movement and output the control signals to execute it. This differs from vision-language-action \(VLA\) policies, which map observations and instructions directly to actions without an explicit predictive model, and the two lines of work have been converging in recent research. Mixture-of-Experts \(MoE\) architectures route each input token to a small subset of expert subnetworks, keeping total capacity large while limiting compute per token, and diffusion models generate outputs through iterative denoising rather than a single forward pass. Runway is best known as a generative video company, making a robotics control model an extension of its video-pretraining expertise.

<details><summary>References</summary>
<ul>
<li><a href="https://runway.com/">Runway | Intelligent tools for scaling content and teams.</a></li>
<li><a href="https://www.linkedin.com/company/runwayml">Runway | LinkedIn</a></li>
<li><a href="https://arxiv.org/abs/2609.16074">[2609.16074] World-Action Models for Robot Learning and ...</a></li>

</ul>
</details>

**Tags**: `#open-source AI`, `#robotics`, `#embodied intelligence`, `#world models`, `#Runway`

---

<a id="item-5"></a>
## [CACM Explores the Shift From Single Intelligent Agents to Agent Societies](https://news.google.com/rss/articles/CBMieEFVX3lxTE0wRHpsYjlKNjZvOHVNNnJEN2tYS2FwWDVWX3lSUWR6aUNjbS1zOHdVS2ViVTkyeElWOGFuaC1yczdDZElQMDVTUVhuSWRES2htYmV5enNEbm9CSDRsSlcxZ0d4aUVLRG9rYjNHOVNMT3lNdUFfN0ZHTQ?oc=5) ⭐️ 6.0/10

Communications of the ACM, the flagship magazine of the Association for Computing Machinery, has published an article titled &quot;From Intelligent Agents to Agent Societies&quot; that frames the field&\#x27;s evolution from standalone intelligent agents toward societies of interacting agents. The piece appears as a conceptual overview rather than a product announcement, and only the title and publication venue are currently available, with no abstract or body text disclosed. Publication in CACM signals that multi-agent and agent-society research is being treated as a maturing, mainstream topic rather than a niche subfield, which matters as industry frameworks for coordinated LLM agents proliferate. It could give practitioners and researchers a shared vocabulary for describing systems where many autonomous agents cooperate, compete, or self-organize. Because only the title and venue are available, specific claims, architectures, benchmarks, or case studies in the article cannot be verified, and readers should treat the headline framing as a research narrative rather than an empirical result. The article is best understood as positioning work in the long tradition of distributed artificial intelligence and multi-agent systems, where agents may hold individual goals or shared goals.

google\_news · Communications of the ACM · Nov 12, 20:59

**Background**: An intelligent agent is a software or robotic entity that perceives its environment and takes actions to achieve goals, typically with some degree of autonomy and reasoning. A multi-agent system \(MAS\) is a computational system composed of multiple interacting intelligent agents, which can solve problems that are difficult or impossible for a single agent or a monolithic system to handle, through cooperation, competition, or coordination. The related term distributed artificial intelligence \(DAI\) traditionally distinguishes multi-agent systems, where entities may arise from different interests and hold individual goals, from DAI systems whose entities share common goals. The phrase &quot;agent societies&quot; extends this idea by borrowing from sociology and artificial life: large populations of agents whose collective behavior, norms, and interactions become the object of study.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_system">Multi-agent system - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Distributed_artificial_intelligence">Distributed artificial intelligence - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/multi-agent-system-in-ai/">Multi Agent System in AI - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#agent societies`, `#AI agents`, `#distributed AI`, `#CACM`

---

<a id="item-6"></a>
## [186 Fake AI Domains Funnel Victims Into ClickFix Scams and Browser Hijackers](https://news.google.com/rss/articles/CBMiggFBVV95cUxOUlkxU1FZT2s0bUk0MVdJc1YtNGF5XzBCTGo5NGZsSS1FZzhSWGtQa0taWkpzT19ScW8zSDktX3FLbXVCVUxybjNsTWlsakNBcGN3c0Y0VlIxbkxlTUZuTDVPUzFCV29SaDEzenNROHR1U1c0UVNqMGdic1gzRjVpN1JB?oc=5) ⭐️ 6.0/10

Researchers uncovered a campaign operating 186 AI-themed domains that pose as legitimate artificial-intelligence services but instead redirect visitors to ClickFix social-engineering lures, browser malware, and search hijackers. Rather than exploiting software flaws, the operation relies on fake CAPTCHA checks and error prompts that convince users to paste and run malicious commands themselves. The campaign shows how attackers are hijacking the current enthusiasm for AI tools, using plausible-looking chatbot and model download sites to reach both consumers and employees who search for AI services. Because ClickFix needs no exploit and no malicious attachment, traditional email-filter and patch-based defenses offer little protection, making user awareness a critical control. The infrastructure spans 186 domains that chain together multiple monetization and infection paths — ClickFix command-execution lures, browser-based malware, and search hijackers that alter a victim&\#x27;s homepage, new-tab page, and default search engine. ClickFix itself is a social-engineering technique that has been tracked in campaigns since early 2024, typically delivering infostealer payloads and other malware after the user runs a pasted PowerShell or shell command.

google\_news · The Hacker News · Nov 12, 15:15

**Background**: ClickFix gets its name from the fake &quot;fix it&quot; prompts it displays: a page claims there is a browser error, a Cloudflare-style human check, or a required update, and instructs the visitor to open a run dialog and paste a command that actually downloads malware. Because the victim performs the action, the technique bypasses many security controls that look for exploits or malicious files. Separately, browser hijackers are unwanted programs that silently modify browser settings — such as the homepage, default search engine, or installed extensions — to force traffic to attacker-controlled search pages and ads, while AI-themed domains exploit users&\#x27; habit of typing plausible AI product names in search engines or the address bar.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/">Think before you Click(Fix): Analyzing the ClickFix social ...</a></li>
<li><a href="https://www.ctm360.com/reports/clickfix-beyond">ClickFix Malware Report 2026: Attacks &amp; Mitigation | CTM360</a></li>
<li><a href="https://www.sitepoint.com/dont-hijack-my-browser/">Don&#x27;t Hijack My Browser — SitePoint</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#malware`, `#phishing`, `#browser hijacking`, `#AI-themed domains`

---

<a id="item-7"></a>
## [Google adapts TPU silicon into specialized systems for AI agents and security](https://news.google.com/rss/articles/CBMi7gJBVV95cUxNUFdBQlBXR3dOb0dJUUh5Rk9wX19ucEY1QlB5cnVtOXhvSk9Xd21KWW9xcXdQc2RuQ3lMY0RVOHl0cDhVNUh4Q0N5Q2xlWWRxRmpSYjRnWHJ6X19XOEFKVFB3N28yMjJlUTdPMy1CWG5wNFdVMTZncEZmN2tvSWVaa0pIMURmOE5sM0ZsbTY5MzBHamZxelByenBwSFUwWFhjb3VwTWZLaWlDTlVXd1ZaMWZ5RnQ4VHZKLUNnLTdkYmpoeUxUc3Zld0VZcExsQ1JoNU80MkhNYzhCR2dHNy1LdFlmVmxfUm9qUndLb2VhdUhDcDVia3ZuckI3NlpqWGJPNGtOdHo3R2JyWnB6Yy1VQnJNYkhiWUoxMnlXZXlRUi01YnVPMndFSWVqSHl0LTVIdUxQSEhFZ0daYTlsZktKN3p2UHFzVWlfendrbUNMSmUydUJWZjd0RkN0dzNYS1d0Zm5oQ3BycXlMVWtiOWc?oc=5) ⭐️ 6.0/10

Google is reportedly reworking its Tensor Processing Unit \(TPU\) silicon into specialized systems aimed at AI agent workloads and security applications, according to Tom&\#x27;s Hardware. The report describes a shift toward purpose-built systems rather than only general-purpose AI accelerators. If confirmed, this would extend TPUs beyond general model training and inference toward hardware tailored for autonomous AI agents and security-sensitive AI tasks, potentially influencing how Google designs and deploys future AI infrastructure. It also signals that AI hardware competition may increasingly focus on specialized system-level designs rather than raw accelerator performance alone. The report provides no technical specifications, product names, availability dates, or performance figures, so it is unclear whether these are new chip variants, system-level integrations, or software-defined configurations. The details therefore remain unconfirmed and limited to the headline-level description.

google\_news · Tom&\#x27;s Hardware · Nov 12, 11:00

**Background**: Google&\#x27;s TPUs are custom ASICs designed to accelerate the matrix operations used by neural networks, and they have been used for both inference and, since the second generation, training. AI agents are software systems that can plan, reason, and take actions autonomously to accomplish goals, which can place different demands on hardware than simple model inference. The news suggests Google may be creating more specialized hardware or system designs rather than relying only on general-purpose AI accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://lilys.ai/en/notes/google-tpu-20251127/tpu-ml-live">TPU Machine Learning (LIVE)</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What are AI agents? - IBM</a></li>

</ul>
</details>

**Tags**: `#Google TPU`, `#AI hardware`, `#AI agents`, `#security`, `#specialized systems`

---

<a id="item-8"></a>
## [Matrix-Game4.0 brings 60 FPS AI game-world generation to browser on one consumer GPU](https://www.aibase.com/news/32285) ⭐️ 6.0/10

Matrix-Game4.0 has reportedly launched on Reactor, enabling browser-based “generate while you play” game-world generation at 60 FPS on a single consumer-grade GPU. If the demo is reproducible, real-time neural world generation on ordinary hardware could make AI-driven interactive environments far more accessible, shifting them from offline experiments toward playable browser experiences for game developers and players. The report offers few benchmarks or caveats, but Skywork AI’s Matrix-Game 4.0 pairs an executable game engine—handling gameplay, physics and player input—with a causal video model that turns low-poly RGB frames into detailed visuals in a streaming pipeline; the specific GPU model, resolution, latency and public availability are not specified.

aibase · AIbase · Nov 12, 18:01

**Background**: Matrix-Game is Skywork AI’s open-source series of interactive world models; version 4 combines a conventional game engine with a neural video model so that the engine manages simulation and controls while the model handles visual synthesis. Reactor is a browser platform for live-generated worlds, including WorldPlay2, which generates every frame in real time from a single input image. “Generate while you play” means the world is synthesized on the fly in response to player input rather than being fully pre-rendered.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/SkyworkAI/Matrix-Game">Matrix-Game 4.0 - GitHub</a></li>
<li><a href="https://www.reactor.inc/worldplay2">WorldPlay2 — Reactor</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#real-time rendering`, `#game AI`, `#browser gaming`, `#GPU acceleration`

---

<a id="item-9"></a>
## [Anthropic Upgrades Claude Connectors With Full-Screen Interactive Apps](https://www.aibase.com/news/32279) ⭐️ 6.0/10

Anthropic upgraded Claude&\#x27;s connectors so that connected apps can now be opened beside a conversation and expanded to full screen, letting users edit content directly alongside Claude instead of relying on a small side preview. The feature is rolling out to web and desktop plans, shifting connector usage from passive previews to full-screen interactive workflows. This turns connectors from read-only context sources into working surfaces, which matters for users who chain Claude with tools like Asana, Adobe, HubSpot or Atlassian and previously had to switch tabs to do real work. It also strengthens Anthropic&\#x27;s position in the broader race among AI assistants to become the place where work actually happens rather than just where it is discussed. The change is a UX-level enhancement rather than a new model or API capability, and it is being rolled out gradually to web and desktop rather than to all clients or mobile at once. Since connectors are built on the Model Context Protocol \(MCP\), the interactive UI is delivered through MCP Apps, meaning the depth of interaction still depends on how each third-party tool implements its connector.

aibase · AIbase · Nov 12, 16:01

**Background**: Claude connectors are integrations built on the Model Context Protocol \(MCP\), an open standard that lets Claude read from and act inside external software such as project management, CRM or creative tools. Earlier connector experiences typically surfaced as a side preview pane, so users could see tool content but had limited room to work in it. Interactive connectors, delivered as MCP Apps, render a live UI directly inside the conversation so no tab-switching is needed. This update extends that model by allowing the embedded app to take over the full screen next to the chat.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/resources/articles/interactive-tools-in-claude">Interactive connectors and MCP Apps | Claude by Anthropic</a></li>
<li><a href="https://blog.buildfastwithai.com/claude-connectors-creative-tools-2026">Claude Connectors for Creative Tools: All 9 Explained (2026)</a></li>
<li><a href="https://themeisle.com/blog/claude-connectors/">Claude Connectors Explained: How to Add a Custom Connector</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#AI assistants`, `#product update`, `#developer tools`

---

<a id="item-10"></a>
## [Alibaba Teases Qwen4 With New Core Architecture and a Preview in the Qwen App](https://www.aibase.com/news/32274) ⭐️ 6.0/10

Alibaba has officially announced that its next-generation Qwen4 large model is launching soon, promising a new core architecture along with across-the-board upgrades to performance, knowledge understanding, semantic parsing, and complex long-context handling. A preview version of the model has already been integrated into the Qwen app, giving users early hands-on access before the full release. Qwen is one of the most widely adopted open-weight model families, so a generational jump to Qwen4 would ripple across developers and enterprises that build on its API or self-hosted weights. Stronger long-context and complex-reasoning capabilities would also put Alibaba in closer competition with rival frontier models in agentic and multi-step task workloads. The announcement is a teaser: Alibaba has not disclosed architecture specifics, parameter counts, benchmark results, or a firm release date, and the information comes via an aggregator rather than an official Alibaba publication. Search reports indicate the early-access build is branded Qwen4-Max-Preview and is positioned for complex multistep tasks, coding, and autonomous agent operation.

aibase · AIbase · Nov 12, 15:01

**Background**: Qwen, also known as Tongyi Qianwen, is Alibaba Cloud&\#x27;s family of large and small language models that are largely released with open weights, and it has become a staple in the open-source AI community alongside models like Llama and DeepSeek. Prior Qwen3 models introduced hybrid &quot;thinking&quot; and &quot;non-thinking&quot; modes that let users trade off reasoning depth against speed and cost. Long-context handling is a key battleground for LLMs because models often degrade at retrieving information from the middle of very long inputs, a problem documented in research such as &quot;Lost in the Middle&quot;.

<details><summary>References</summary>
<ul>
<li><a href="https://mobidevices.com/en/alibaba-qwen-4-max">Alibaba launches flagship AI model Qwen 4 Max</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1">Qwen - Alibaba Cloud</a></li>

</ul>
</details>

**Tags**: `#qwen`, `#llm`, `#alibaba`, `#model-release`, `#ai-announcements`

---