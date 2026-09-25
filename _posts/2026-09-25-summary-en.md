---
layout: default
title: "Horizon Summary: 2026-09-25 (EN)"
date: 2026-09-25 23:03:06 +0000
lang: en
report: default
---

> From 143 items, 7 important content pieces were selected

---

1. [F-Droid 2.0 Released: Its Biggest Update in a Decade](#item-1) ⭐️ 8.0/10
2. [Anthropic&\#x27;s Project Swap: Claude agents trade books for 201 employees](#item-2) ⭐️ 8.0/10
3. [Google Cloud makes Gemini 3.8 Live with Live Avatar generally available](#item-3) ⭐️ 7.0/10
4. [Meta Muse zero-day lets local attackers hijack accounts](#item-4) ⭐️ 7.0/10
5. [OpenCode data pages allegedly leak unreleased frontier models](#item-5) ⭐️ 6.0/10
6. [Microsoft launches Copilot &\#x27;super app&\#x27; unifying chat, coding and agents](#item-6) ⭐️ 6.0/10
7. [PrismML brings tiny 1-bit LLMs to Qualcomm-powered smart glasses](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [F-Droid 2.0 Released: Its Biggest Update in a Decade](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 8.0/10

On September 24, 2026, F-Droid released version 2.0 of its official Android client, its largest update in ten years, after 14 beta releases. The release redesigns both the interface and the underlying code, condensing the app into three main areas — Discover, Search, and My Apps — and is rolling out to users over the coming weeks. As the flagship repository for free and open source Android software, F-Droid&\#x27;s modernization affects the whole FOSS Android ecosystem, since the client is the main gateway through which users discover and install libre apps outside of Google Play. Improved discovery and search — including better CJK text handling — could make the catalog far more accessible to non-English-speaking users who have long been underserved. The new client improves app discovery, categories, search and filtering, and can now search app descriptions, categories, and translated content, with enhanced Chinese, Japanese, and Korean text search. It also introduces a smoother install/update flow with background update checks, but drops support for Android 6 and, for now, does not support the F-Droid Privileged Extension.

telegram · zaihuapd · Sep 24, 23:58

**Background**: F-Droid is a free and open source \(FOSS\) app store and software repository for Android, serving a similar function to the Google Play Store but hosting only libre applications, and it flags &quot;anti-features&quot; such as advertising or user tracking in app descriptions. The Privileged Extension is an optional component that must be installed as a system &quot;priv-app&quot; with root privileges; it lets F-Droid install, update, and remove apps without requiring &quot;Unknown Sources&quot; to be enabled and enables silent background updates, much like Google Play. Dropping Android 6 and temporarily losing Privileged Extension support means some users on older devices or rooted/custom-ROM setups will not get the full 2.0 experience.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F-Droid</a></li>
<li><a href="https://f-droid.org/packages/org.fdroid.fdroid.privileged/">F - Droid Privileged Extension | F - Droid - Free and Open Source...</a></li>
<li><a href="https://github.com/f-droid/privileged-extension">GitHub - f - droid / privileged - extension : mirror of https...</a></li>

</ul>
</details>

**Tags**: `#F-Droid`, `#Android`, `#开源`, `#应用商店`, `#版本发布`

---

<a id="item-2"></a>
## [Anthropic&\#x27;s Project Swap: Claude agents trade books for 201 employees](https://www.anthropic.com/research/project-swap) ⭐️ 8.0/10

Anthropic ran an experiment in which 201 employees each brought a book, chatted briefly with Claude about their reading tastes, and then handed the resulting agent into an agent-only marketplace where the agents bargained with one another to swap books. After only about five minutes of conversation, Claude&\#x27;s ranking of each participant&\#x27;s book list matched the person&\#x27;s own preferences 61% of the time, and the participants reported an average satisfaction of 7.2/10. The study provides rare empirical evidence on how well LLM agents can infer human preferences and negotiate on their behalf, a capability that underlies emerging multi-agent systems and personalized AI assistants. It also suggests a plausible commercial path: participants said they would trust an agent with roughly 30% of their annual book budget. The market failed to reach optimal allocations mainly because the agents knew too little about their own participants rather than because they negotiated poorly, meaning better preference elicitation — not better bargaining — is the bottleneck. Stronger Claude models produced higher trade completion efficiency, and the 61% agreement figure shows meaningful but far-from-perfect preference capture from a five-minute chat.

telegram · zaihuapd · Sep 25, 04:40

**Background**: A multi-agent system is a computational setup in which multiple interacting intelligent agents solve problems that a single agent or monolithic system cannot handle well; since the rise of large language models, LLM-based multi-agent systems have become an active research area. Preference learning is the machine-learning subfield concerned with predicting what people like from observed rankings, pairwise comparisons, or ratings, rather than from absolute labels. Anthropic is the company behind the Claude family of large language models, which are also used in agentic tools such as Claude Code; Project Swap tests the same kinds of agents in an economic setting.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_system">Multi-agent system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Preference_learning">Preference learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Claude">Anthropic Claude</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#LLM`, `#Anthropic`, `#multi-agent systems`, `#preference learning`

---

<a id="item-3"></a>
## [Google Cloud makes Gemini 3.8 Live with Live Avatar generally available](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-8-live-with-live-avatar-is-now-generally-available) ⭐️ 7.0/10

On September 25, Google Cloud announced the general availability of Gemini 3.8 Live with Live Avatar, first previewed at Google Cloud Next 2026, adding lip-synchronized video avatars, speech-to-speech dialogue across 97 languages, and SynthID watermarking on generated audio and video. Custom avatar creation remains limited to an enterprise allowlist, and Gemini 3.8 Live Extended Thinking is still in private preview. This GA release gives developers a production-ready way to build conversational AI agents with real-time animated faces and multilingual voice interaction, which could accelerate adoption of virtual assistants, customer-service bots, and digital humans in enterprise applications. It also signals Google is pushing multimodal, avatar-based interaction as a differentiator against rivals such as OpenAI&\#x27;s real-time voice APIs. Live Avatar supports synchronized lip-syncing, contextual facial expressions, and switching among 97 languages without degrading video quality. All generated audio and video carry SynthID watermarks, and custom avatar creation is gated behind an enterprise allowlist, which limits who can use it at launch.

telegram · zaihuapd · Sep 25, 03:09

**Background**: Gemini Live is Google&\#x27;s real-time, multimodal conversational API that lets applications hold natural spoken dialogues with an AI model. Live Avatar extends this by generating a video persona whose lips and facial expressions match the synthesized speech, effectively creating a talking digital human. SynthID is Google DeepMind&\#x27;s watermarking technology that embeds imperceptible signals into AI-generated content so it can later be identified as synthetic, while an allowlist means only approved enterprise customers can access a feature. &quot;Extended Thinking&quot; refers to a mode in which the model spends more compute on reasoning before answering.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-8-live-with-live-avatar-is-now-generally-available">Gemini 3.8 Live with Live Avatar is now generally... | Google Cloud Blog</a></li>
<li><a href="https://www.androidauthority.com/gemini-live-avatar-3715280/">Google&#x27;s new Gemini Live Avatars want to make... - Android Authority</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-09-25-google-introduces-gemini-38-live-avatar-real-time-animated-persona-brings-interactive-visual-presenc">Google Gemini 3.8 Live Avatar Brings Real-Time AI Face | AIToolly</a></li>

</ul>
</details>

**Tags**: `#Google Cloud`, `#Gemini`, `#Generative AI`, `#Digital Avatars`, `#Multimodal AI`

---

<a id="item-4"></a>
## [Meta Muse zero-day lets local attackers hijack accounts](https://www.ithome.com/1/007/126.htm) ⭐️ 7.0/10

Security researcher Patrick Wardle disclosed a macOS zero-day in Meta Muse, dubbed &quot;Not-a-Mused,&quot; that lets an unprivileged local process modify an undocumented preference key \(endo\_voyager\_dictation\_endpoint\) via the defaults command, hijack accounts, and steal authentication tokens. Meta has already shipped a hotfix that removes the underlying debug functionality. The flaw affects an AI agent app that operates with broad permissions on a user&\#x27;s behalf, so a stolen token can cascade into email, calendar, and WhatsApp access — illustrating the emerging &quot;agent-as-attack-surface&quot; risk class. Because Muse was marketed partly on its security architecture \(Muse Secure VM\), the disclosure also dents trust in the safety claims of consumer AI agents. Exploitation requires only a local process, or tricking the user into running a terminal command, rather than sophisticated malware; the flaw lives in the app bundle com.meta.endo. The vulnerability abuses an undocumented dictation endpoint, and Meta&\#x27;s fix removes the debugging feature rather than altering the credential-handling design itself.

telegram · zaihuapd · Sep 25, 07:27

**Background**: Meta Muse is Meta&\#x27;s consumer AI agent app, launched on 8 September 2026 and currently US-only, that runs tasks in the background such as email, travel bookings, forms, bills, and purchases; it also has a Mac app. A zero-day is a vulnerability that is unknown to the vendor and therefore unpatched at the time of disclosure. Setting an undocumented preference key via the built-in &quot;defaults write&quot; command is a standard macOS mechanism that any local process can invoke, which is why the attack needed little sophistication.

<details><summary>References</summary>
<ul>
<li><a href="https://eyestech.in/meta-muse-zero-day-privilege-inversion-os-agents/">Meta Muse Zero-Day: Privilege Inversion in OS Agents</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/09/21/meta-muse-ai-app-flaw-lets-local-malware-redirect-dictation-traffic/5297980">Meta Muse AI app flaw lets local malware redirect dictation traffic</a></li>
<li><a href="https://tech.yahoo.com/cybersecurity/articles/muse-undocumented-endpoint-turns-macos-192808424.html">Muse ’s Undocumented Endpoint Turns macOS Agent Into a Local...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#macOS`, `#Meta`, `#zero-day`

---

<a id="item-5"></a>
## [OpenCode data pages allegedly leak unreleased frontier models](https://opencode.ai/zh/data/moonshot/kimi-k4) ⭐️ 6.0/10

Data pages on the OpenCode site were reportedly found to contain entries for several models that have never been publicly announced, including Kimi K4, GLM 5.5 Flash, GLM 5.4, DeepSeek V4.1 Pro, Tencent hy4, Qwen3.8 Max Preview and Meta&\#x27;s muse-spark-1.4-contributor. All of the listed pages currently show zero usage and zero unique users, leading observers to describe them as a probable leak of upcoming releases rather than live services. If the entries are genuine, they would pre-announce next-generation flagship models from Moonshot AI, Zhipu/Z.ai, DeepSeek, Alibaba&\#x27;s Qwen and Tencent well before their official launches, giving the industry an unusually early look at the 2026 model roadmap. Even unverified, such leaks shape developer expectations about upcoming API availability, pricing and capability jumps, and can affect how teams plan their model-selection and migration strategies. The evidence is thin: the pages reportedly show no usage statistics and no unique users, and there is no benchmark data, parameter count, context window or pricing information attached to any of the listed names. OpenCode itself is a widely used open-source terminal-based AI coding agent that routes requests to many providers, so provider/model catalog entries can appear before a model is officially launched, and nothing has been officially confirmed by Moonshot AI, Z.ai, DeepSeek, Alibaba, Tencent or Meta.

telegram · zaihuapd · Sep 25, 05:47

**Background**: OpenCode is an open-source, provider-agnostic AI coding agent that runs in the terminal and lets developers switch between many different LLMs, which means its catalog pages list models from dozens of vendors. Model aggregators and client tools frequently add placeholder entries for models before launch so that routing, pricing and quota systems are ready on day one, and these stubs are sometimes spotted by users before any announcement. Naming conventions matter here too: Kimi K3 is Moonshot AI&\#x27;s existing 2.8T-parameter open-weight multimodal reasoning model and GLM-5.3-Flash is Z.ai&\#x27;s first natively multimodal GLM-5-series model, so &\#x27;K4&\#x27; and &\#x27;GLM 5.5&\#x27; read as plausible successors rather than arbitrary strings.

<details><summary>References</summary>
<ul>
<li><a href="https://sanj.dev/post/open-source-cli-ai-agents-comparison/">Open Source CLI AI Agents: OpenCode , Aider, Goose, and Pi... | Sanj</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi - K 3 · Hugging Face</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.3-Flash">zai-org/ GLM - 5 .3- Flash · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI Models`, `#Leak`, `#LLM`, `#Industry News`, `#Rumor`

---

<a id="item-6"></a>
## [Microsoft launches Copilot &\#x27;super app&\#x27; unifying chat, coding and agents](https://www.theverge.com/news/1000532/microsoft-copilot-super-app-chat-coding-autopilot) ⭐️ 6.0/10

Microsoft officially unveiled a new Copilot &quot;super app&quot; that consolidates AI chat, coding and agent capabilities into three tabs: Home, Code and Autopilot. The personal AI assistant previously called Scout has been rebranded as Autopilot and repositioned as a cloud-based &quot;digital coworker.&quot; The release signals Microsoft&\#x27;s strategic bet that agentic AI — software that carries out multi-step work rather than just answering questions — will be the next front in the assistant wars, and it pushes Copilot from a chat sidebar toward a single workspace competing with the likes of ChatGPT, Claude and Cursor. Developers and knowledge workers already inside the Microsoft 365 ecosystem are the primary audience, since Code and Autopilot are aimed at building and delegating work tasks. Rollout is staggered rather than immediate: Home and Code will reach users on Microsoft&\#x27;s Frontier early-access program over the coming weeks, while Autopilot only opens a private preview later this month. The Code tab is described as being able to create apps or automations and share them with colleagues, and the announcement is largely a consolidation and rebranding \(Scout to Autopilot\) rather than a new technical breakthrough.

telegram · zaihuapd · Sep 25, 12:15

**Background**: Copilot is Microsoft&\#x27;s umbrella brand for AI assistants built on large language models, previously embedded across Word, Excel, Outlook, Teams and Windows. An AI agent, or &quot;agentic AI,&quot; refers to a system that can plan, use tools and execute multi-step tasks with limited human supervision, in contrast to a chatbot that mainly returns text answers. Microsoft has spent the past two years pushing agentic features into its productivity suite, and this &quot;super app&quot; is an attempt to give those separate features one entry point instead of scattering them across individual products.

<details><summary>References</summary>
<ul>
<li><a href="https://copilot.microsoft.com/">Microsoft Copilot</a></li>
<li><a href="https://m365.cloud.microsoft/">Microsoft 365 - Sign into Copilot</a></li>
<li><a href="https://juejin.cn/post/7568323565771145252">一文读懂！ Al Agent ( 智 能 体 ) 到底是个啥?一文读懂！ Al Agent ...</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#Copilot`, `#AI Agents`, `#Product Launch`, `#Developer Tools`

---

<a id="item-7"></a>
## [PrismML brings tiny 1-bit LLMs to Qualcomm-powered smart glasses](https://techcrunch.com/2026/09/24/prismml-brings-its-tiny-llms-to-qualcomm-powered-smart-glasses/) ⭐️ 6.0/10

AI lab PrismML has built a compact language model that runs locally on Qualcomm&\#x27;s Snapdragon AR1 Gen 1 smart-glasses platform, demoed at Qualcomm&\#x27;s Snapdragon Summit. The model, called Bonsai, uses a 2-billion-parameter 1-bit design tuned for both vision and language so wearers can ask real-time questions about what they are looking at; no shipping glasses have been announced yet. Running a multimodal LLM entirely on a glasses-class chip without a network round-trip is a meaningful step for on-device AI, since it addresses the latency, privacy, and battery constraints that have held back always-on wearable assistants. It also signals that Qualcomm is positioning the Snapdragon AR1 line as a viable host for generative AI, which could push more thin-and-light AR hardware toward local inference instead of cloud dependence. 1-bit models quantize weights down to a single bit, which drastically cuts memory footprint and compute cost but usually costs accuracy, so benchmark numbers matter — and PrismML has not published quality or latency figures for this 2B glasses variant. For comparison, PrismML&\#x27;s publicly documented Bonsai releases include an 8.2B model that is 1-bit end to end \(embeddings, attention, MLP layers, and LM head, with no higher-precision escape hatches\) and a 27B version, which suggests the 2B glasses model is a new, smaller point on the same design curve.

telegram · zaihuapd · Sep 25, 13:06

**Background**: Smart glasses have long been limited by the fact that they are tiny, battery-constrained devices, so most AI features either ran simple rules on-device or shipped data to the cloud. Large language models normally need many gigabytes of memory and a power-hungry GPU, which is why quantization — compressing model weights into fewer bits — has become a key research area. Qualcomm&\#x27;s Snapdragon AR1 Gen 1 is a 4nm class platform widely used in lightweight AR and audio glasses, and running a multimodal LLM directly on it would let the glasses answer questions about the wearer&\#x27;s surroundings instantly and privately.

<details><summary>References</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-8b">PrismML — Announcing 1 - bit Bonsai : The First Commercially Viable...</a></li>
<li><a href="https://gadgetsnow.indiatimes.com/tech-news/qualcomms-smart-glasses-bet-gets-serious-as-1-bit-ai-moves-onto-the-frame/articleshow/134445667.cms">Qualcomm ’s smart-glasses Bet Gets Serious as 1 -bit AI Moves Onto...</a></li>
<li><a href="https://www.datacamp.com/tutorial/run-bonsai-locally">Bonsai AI Tutorial: Run a 1 - Bit LLM Locally On an Old... | DataCamp</a></li>

</ul>
</details>

**Tags**: `#On-device AI`, `#LLM`, `#Smart Glasses`, `#Qualcomm`, `#TinyML`

---