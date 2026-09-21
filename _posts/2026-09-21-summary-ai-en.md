---
layout: default
title: "Horizon Summary: 2026-09-21 (EN)"
date: 2026-09-21 23:04:45 +0000
lang: en
report: ai
---

> From 266 items, 10 important content pieces were selected

---

1. [Microsoft used AI agents to port Copilot runtime from TypeScript to Rust](#item-1) ⭐️ 8.0/10
2. [Cloudflare Python Workers reach general availability after two-year preview](#item-2) ⭐️ 7.0/10
3. [Texas Governor Abbott Halts State Data Center Permits Pending Grid Audit](#item-3) ⭐️ 7.0/10
4. [British Columbia sues OpenAI over Tumbler Ridge mass shooting](#item-4) ⭐️ 7.0/10
5. [UN panel calls for stronger safeguards as AI agents advance](#item-5) ⭐️ 7.0/10
6. [Appeals Court Warns &\#x27;AI Slop&\#x27; Threatens Courts&\#x27; Ability to Function](#item-6) ⭐️ 7.0/10
7. [Developer Exposes OpenAI Ad Tracking Chain Tied to ChatGPT Accounts](#item-7) ⭐️ 7.0/10
8. [Alibaba&\#x27;s Qwen Team Open-Sources 7B Qwen-Image-2.1 Image Model](#item-8) ⭐️ 7.0/10
9. [Step 5 Preview: 600B Sparse MoE Flagship Activates Only 27B Parameters Per Inference](#item-9) ⭐️ 7.0/10
10. [Australia Calls for Slowing the Global AI Development Race](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Microsoft used AI agents to port Copilot runtime from TypeScript to Rust](https://www.aibase.com/news/31240) ⭐️ 8.0/10

Microsoft used AI agents to fully port the GitHub Copilot runtime from TypeScript to Rust, converting roughly 430,000 lines of TypeScript into about 800,000 lines of Rust. The migration reportedly cost around $120,000 in tokens plus three engineer-weeks of work, and delivered a claimed 15.9x performance improvement. This is a strong proof point that AI agents can carry out production-scale language migration rather than just small refactors, potentially compressing multi-year rewrite projects into weeks. If reproducible, it changes the economics of modernizing large legacy codebases and could push more engineering teams to consider agent-driven ports to faster languages like Rust. The ported runtime powers Copilot CLI, the Copilot App, the SDK, and cloud agents across VS Code, Visual Studio, Excel, Outlook, and PowerPoint. Note that the Rust codebase is nearly twice as large in line count as the TypeScript original, and the performance and cost figures come from an aggregator report rather than a detailed Microsoft engineering paper, so they should be treated as unverified.

aibase · AIbase · Sep 21, 18:01

**Background**: TypeScript running on Node.js is popular for AI and web services because it enables fast development, but it can be limited in startup time and throughput when services scale up. Rust offers comparable safety guarantees with much better runtime performance, though rewriting a large codebase by hand is normally expensive and risky. AI code migration typically works through agentic loops: engineers define migration rules and verification tests, and agents repeatedly translate, compile, test, and repair the code until the new codebase behaves like the original.

<details><summary>References</summary>
<ul>
<li><a href="https://www.augmentcode.com/guides/ai-code-migration">AI Code Migration: How Agent Loops Port Codebases Fast</a></li>
<li><a href="https://claude.com/blog/ai-code-migration">How Anthropic runs large-scale code migrations with Claude ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/agents/providers/github-copilot">GitHub Copilot Agents | Microsoft Learn</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Rust`, `#TypeScript`, `#code migration`, `#GitHub Copilot`

---

<a id="item-2"></a>
## [Cloudflare Python Workers reach general availability after two-year preview](https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/) ⭐️ 7.0/10

Cloudflare announced that Python Workers are now generally available, making Python a first-class, fully supported language on the Cloudflare Developer Platform after roughly two years in preview. The implementation runs Python compiled to WebAssembly via Pyodide inside Cloudflare&\#x27;s V8-based workerd runtime, and the release announcement is credited to Gyeongjae Choi, Dominik Picheta, and Hood Chatham — two of whom are Pyodide core maintainers. Python is one of the most widely used languages in the world, so making it a stable, supported option on a major serverless edge platform meaningfully lowers the barrier for developers who previously had to write Workers in JavaScript or TypeScript. It also signals continued corporate investment in Pyodide and the broader WebAssembly-based Python ecosystem, which could spill over into browsers and other Wasm runtimes. There are notable limitations: both multiprocessing and threading are non-functional inside the WebAssembly VM, and Cloudflare documents these restrictions for the standard library. The local development story is also distinctive — the pywrangler tool \(published on PyPI as workers-py\) simulates the whole stack locally, executing code with Pyodide in WebAssembly in V8 inside a 123MB workerd binary located at node\_modules/@cloudflare/workerd-darwin-arm64/bin/workerd.

rss · Simon Willison · Sep 21, 22:25

**Background**: Pyodide is a port of CPython to WebAssembly/Emscripten that lets Python and many of its packages run in constrained environments without a native interpreter. workerd is Cloudflare&\#x27;s open-source JavaScript and WebAssembly runtime that powers Cloudflare Workers both on the edge and in local development. WebAssembly \(Wasm\) is a low-level bytecode format designed to be portable, compact, and run at near-native speeds, which is why it can host a language runtime like CPython inside another runtime such as V8.

<details><summary>References</summary>
<ul>
<li><a href="https://pyodide.org/en/stable/?ref=more-than-numbers.ghost.io">Pyodide — Version 0.25.1</a></li>
<li><a href="https://blog.cloudflare.com/workerd-open-source-workers-runtime/?ref=console.dev/">Introducing workerd : the Open Source Workers runtime</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly/Guides/Concepts">WebAssembly concepts - WebAssembly | MDN</a></li>

</ul>
</details>

**Tags**: `#cloudflare-workers`, `#python`, `#webassembly`, `#serverless`, `#edge-computing`

---

<a id="item-3"></a>
## [Texas Governor Abbott Halts State Data Center Permits Pending Grid Audit](https://wabx.net/2026/09/21/texas-gov-abbott-halts-all-state-issued-permits-for-data-centers-until-grid-audit-is-complete/) ⭐️ 7.0/10

According to reports dated September 21, 2026, Texas Governor Greg Abbott has paused all state-issued permits for data centers until an audit of the state&\#x27;s electricity grid is completed. The reported action would freeze new state-level approvals for data center projects across Texas while the grid review is carried out. Texas is one of the largest data center markets in the United States and a major hub for AI infrastructure buildout, so pausing permits could delay projects, raise costs, and push investment toward other states. It also signals growing tension between surging AI-driven electricity demand and grid reliability, a debate playing out in many regions. The item is only a headline with no article body, and the source and date appear questionable, so key specifics — such as whether the pause covers only new permits or also renewals, whether it targets ERCOT interconnection or state environmental permits, and how long it would last — are unconfirmed. Notably, most large-load grid interconnection in Texas runs through ERCOT rather than through state-issued permits, so the practical reach of such a freeze is unclear.

gdelt · wabx.net · Sep 21, 22:30

**Background**: Most of Texas runs on a grid operated by ERCOT, an independent system operator that manages generation and transmission and conducts interconnection studies for large loads such as data centers. ERCOT has seen record demand growth in recent years, driven by data centers, cryptocurrency mining, and rapid population growth, prompting debates over how to share grid upgrade costs between industrial users and residential ratepayers. State environmental permits, such as air quality authorizations, are typically issued by the Texas Commission on Environmental Quality, which is separate from ERCOT&\#x27;s interconnection process — which is why the exact scope of a &\#x27;state-issued permit&\#x27; freeze matters.

**Tags**: `#Data Centers`, `#Energy Grid`, `#Regulation`, `#Texas`, `#AI Infrastructure`

---

<a id="item-4"></a>
## [British Columbia sues OpenAI over Tumbler Ridge mass shooting](https://theprovince.com/news/bc-lawsuit-against-openai-tumbler-ridge-mass-shooting) ⭐️ 7.0/10

The province of British Columbia has filed a lawsuit against OpenAI over the February 10, 2026 mass shooting in Tumbler Ridge, B.C., a remote town where nine people died, including the perpetrator. The report frames the filing as a legal action alleging a connection between the shooting and OpenAI, though the specific claims and requested damages are not detailed in the available content. This appears to be one of the first government-led lawsuits seeking to hold a major AI developer accountable for a violent real-world harm, which could set an early precedent for how AI companies are treated under tort and product-liability law. A ruling against OpenAI would push model providers toward stricter safety guardrails and could reshape how the entire industry assesses risks from downstream misuse. The shooting itself was carried out by a lone perpetrator, Jesse Van Rootselaar, a former student of Tumbler Ridge Secondary School, who killed her mother and half-brother at home before killing six people at the school and injuring 27 others. The provided report contains no technical, procedural or evidentiary detail about the legal theory British Columbia is advancing against OpenAI.

gdelt · theprovince.com · Sep 21, 22:30

**Background**: The Tumbler Ridge shooting took place on February 10, 2026, in a small town of roughly 2,400 residents in northeastern British Columbia, making it one of the deadliest mass shootings in Canadian history. AI liability is a fast-developing legal area: scholars note that AI systems are hard to fit into traditional liability frameworks because of their unpredictability and autonomy, and the American Law Institute is drafting Principles of the Law on Civil Liability for Artificial Intelligence, with some experts proposing products-liability rules as an interim approach. Lawsuits like this one test whether those emerging doctrines can be applied to a generative AI provider whose model was allegedly used in the run-up to a crime.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Tumbler_Ridge_shooting">2026 Tumbler Ridge shooting - Wikipedia</a></li>
<li><a href="https://www.cbc.ca/news/canada/british-columbia/livestory/active-shooter-alert-tumbler-ridge-secondary-school-bc-live-updates-9.7083740">Mass shooting in Tumbler Ridge, B.C., leaves 8 dead ... - CBC.ca 9 dead, including suspect, following shooting in Tumbler Ridge February 11-12, 2026 - Canada mass shooting at a school and ... What we know about Canada&#x27;s Tumbler Ridge mass shooting - BBC Tumbler Ridge Recap: Three shooting victims, their killer ... Tumbler Ridge shooting: key questions answered about deadly ...</a></li>
<li><a href="https://wp.nyu.edu/compliance_enforcement/2026/05/06/untangling-ai-liability/">Untangling AI Liability | Compliance and Enforcement</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI liability`, `#lawsuit`, `#AI safety`, `#mass shooting`

---

<a id="item-5"></a>
## [UN panel calls for stronger safeguards as AI agents advance](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9CNWdDTkRQZUpVM3duLXp2V0ZLMzVSeFdmQ00yV2R3Qk1CemNfNWM4MnFmaEIzc3Zhdk1qa05YbGdSTkVxQTU2SVlOLXBTR3VqbkZUcE9zbw?oc=5) ⭐️ 7.0/10

A United Nations panel has issued a call for stronger safeguards in response to the rapid advance of AI agents, according to a report from UN News. The panel warns that as these systems grow more capable, existing guardrails may no longer be sufficient to keep them safe and accountable. The call signals that multilateral bodies are moving AI agents onto the international governance agenda, which could shape compliance expectations for companies building and deploying autonomous systems. Because UN-level guidance often informs national regulation, the panel&\#x27;s recommendations may influence how agentic AI is developed, audited, and deployed across borders. The source item is only a headline and link, so the specific panel, the recommendations&\#x27; scope, and any proposed deadlines or enforcement mechanisms are not yet detailed. Notably, the framing targets &quot;AI agents&quot; specifically, rather than general-purpose AI or chatbots, which suggests the concern centers on systems that can take autonomous actions and use external tools.

google\_news · UN News · Sep 21, 22:18

**Background**: An AI agent is an AI program that can pursue goals, use software or other tools, and take actions with some level of autonomy, in contrast to a chatbot that simply answers questions. AI safety is the field concerned with ensuring AI systems operate reliably, avoid unintended harm, and remain under meaningful human control. As agents gain autonomy, the classic difficulty is that a system capable of acting on its own can also make mistakes or be misused at machine speed, which is why calls for safeguards tend to focus on oversight, transparency, and human-in-the-loop controls.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What are AI agents? - IBM</a></li>
<li><a href="https://www.truefoundry.com/blog/what-is-ai-safety">What Is AI Safety ? A Complete Guide for 2026</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#AI safety`, `#AI agents`, `#regulation`, `#UN policy`

---

<a id="item-6"></a>
## [Appeals Court Warns &\#x27;AI Slop&\#x27; Threatens Courts&\#x27; Ability to Function](https://news.google.com/rss/articles/CBMitwFBVV95cUxPTzFNMkcwR3VENkQ1V1VyVVFyUkdWZ2hCeXVfUTd2Z0ZqNzR6SWJ5OFFQNFoxTkhhdTVJOGY3VDlESzJERXBFdmFKMkItcF9DWmtJLV9TcHJNSXhvUi1peV85VnJ1c0JOQU9FUG5mV0loOUdtazlNNzBqbHJpWHdDUmd0LUROVUV1ZE1FdTlpdzNNR1R1c3RUb2RiMUVxWXRvX3N6ejdpOThiWEoxaTJaRURTenZ4bDg?oc=5) ⭐️ 7.0/10

An appeals court has publicly warned that &quot;AI slop&quot; — the flood of low-quality, mass-produced content generated by artificial intelligence — is threatening the courts&\#x27; ability to function, according to a report by the ABA Journal. The warning frames AI-generated material not merely as a nuisance but as a systemic risk to judicial operations. The statement signals that generative AI is now visibly straining a core public institution, moving the debate beyond style or content quality into the courts&\#x27; capacity to process cases fairly and on time. Judges, clerks, lawyers, and self-represented litigants could all be affected as dockets fill with unreliable AI-drafted filings, potentially prompting new disclosure rules and sanctions. The available report is a headline-level item from the ABA Journal, so the specific court, opinion, or order and any cited figures are not detailed in the summary provided. The warning nonetheless aligns with a broader pattern of courts confronting AI-hallucinated citations and boilerplate filings, a problem that has already led to sanctions in several high-profile cases.

google\_news · ABA Journal · Sep 21, 15:50

**Background**: &quot;AI slop&quot; refers to digital content produced with generative AI that is perceived as lacking effort, quality, or meaning, typically generated in high volume and often through tools such as ChatGPT, Gemini, or Perplexity. In the legal context, the danger is compounded by the tendency of large language models to &quot;hallucinate,&quot; inventing plausible-looking case citations and quotations that do not exist. Courts have responded with sanctions for lawyers who file such material and with standing orders requiring parties to disclose whether AI was used in preparing a filing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://www.merriam-webster.com/dictionary/ai+slop">AI SLOP Definition &amp; Meaning - Merriam-Webster</a></li>

</ul>
</details>

**Tags**: `#AI slop`, `#generative AI`, `#legal tech`, `#courts`, `#AI regulation`

---

<a id="item-7"></a>
## [Developer Exposes OpenAI Ad Tracking Chain Tied to ChatGPT Accounts](https://www.aibase.com/news/31234) ⭐️ 7.0/10

Independent security researchers have documented that OpenAI&\#x27;s advertising platform, Bazaar, sets a cross-site cookie named \_\_obi that carries a random ID bound to a user&\#x27;s ChatGPT account JWT. When a user later visits a third-party website that hosts an OpenAI ad pixel, that same \_\_obi cookie is sent back to OpenAI, allowing activity outside OpenAI&\#x27;s own domains to be linked to the ChatGPT account. The disclosure matters because ChatGPT accounts are tied to real identities and payment methods, so linking them to off-site browsing turns an AI assistant into a de-anonymizing advertising profile — a significant step for OpenAI&\#x27;s ad business and a potential regulatory issue under privacy regimes like GDPR. Millions of ChatGPT users who never opted into cross-site advertising tracking could be affected. The \_\_obi cookie is scoped to .openai.com, is written by the ad collector at bzr.openai.com, and appears to be one part of a larger pixel network — one analysis counted around 936 tracking pixels involved. Because the identifier is bound to the account JWT rather than a browser session, clearing cookies alone may not fully break the link while the user remains logged in.

aibase · AIbase · Sep 21, 16:01

**Background**: Cross-site tracking usually works through third-party cookies: an ad network drops an identifier on its own domain, then reads it back from partner sites where its pixels are embedded, stitching a browsing history together. JWT \(JSON Web Token\) is the standard, digitally signed token format used to carry a user&\#x27;s identity between a client and a server in stateless authentication systems like ChatGPT&\#x27;s. OpenAI launched its advertising efforts \(the Bazaar ad platform\) to monetize ChatGPT, and this research documents how the account layer and the ad layer are connected in practice.

<details><summary>References</summary>
<ul>
<li><a href="https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/">ChatGPT now knows what you do on other websites via ad collector</a></li>
<li><a href="https://www.nowadais.com/inside-the-__obi-cookie-how-openai-tracks-users-across-sites/">Inside The __ obi Cookie : How OpenAI Tracks Users Across Sites</a></li>
<li><a href="https://borncity.com/news/chatgpt-cookie-__obi-openai-verknuepft-nutzer-ueber-936-pixel/">ChatGPT- Cookie __ obi : OpenAI verknüpft Nutzer über 936 Pixel</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#OpenAI`, `#tracking`, `#security`, `#adtech`

---

<a id="item-8"></a>
## [Alibaba&\#x27;s Qwen Team Open-Sources 7B Qwen-Image-2.1 Image Model](https://www.aibase.com/news/31227) ⭐️ 7.0/10

Alibaba&\#x27;s Qwen team has released open-weight Qwen-Image-2.1, an image generation and editing model with only 7B vision parameters. The team claims it surpasses most closed-source models on internal benchmarks, while requiring only mainstream consumer GPUs such as an RTX 3090 to run. A compact, open-weight image model from a major lab lowers the hardware barrier for individual developers and small teams, letting them run generation and editing locally instead of paying per-call closed-source APIs. If independent evaluations confirm the performance claims, it would strengthen the argument that open-weight releases can compete with proprietary image systems at or near the frontier. The claim that Qwen-Image-2.1 beats most closed-source models rests on the Qwen team&\#x27;s internal benchmarks, and third-party evaluations are still pending, so the comparison should be treated as provisional. Being an open-weight release means the trained parameters are downloadable for local use, though that does not necessarily include the full training data or pipeline.

aibase · AIbase · Sep 21, 12:01

**Background**: Diffusion models are a class of generative models that learn to reverse a gradual noising process, and they now power widely used image tools such as Stable Diffusion, DALL·E 2 and Midjourney; beyond generation, they can also handle tasks like denoising, inpainting and outpainting. Open-weight models are ones whose trained parameters are publicly released so anyone can download, run, study and modify them on their own hardware. That is a notable step beyond fully proprietary APIs, but it falls short of fully open-source AI, which would also expose the data and code needed for reproducibility and auditing.

<details><summary>References</summary>
<ul>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.linkedin.com/posts/dabeer-ul-haq-qureshi-35964524a_diffusionmodels-generativeai-aiexplained-activity-7326505968534491137-8sMf">What are Diffusion Models in AI ? | Dabeer Ul Haq Qureshi... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#image-generation`, `#diffusion-models`, `#qwen`, `#generative-ai`

---

<a id="item-9"></a>
## [Step 5 Preview: 600B Sparse MoE Flagship Activates Only 27B Parameters Per Inference](https://www.aibase.com/news/31221) ⭐️ 7.0/10

Step5Preview was announced as a fully open flagship base model built for real-world agentic tasks, using a sparse mixture-of-experts \(MoE\) architecture with 600B total parameters that activates only about 27B parameters per inference. The release positions itself as pushing the Pareto frontier of capability, efficiency and cost for open-source flagship models, though it is described only as a preview with sparse technical detail. If the claimed activation ratio holds up in practice, Step5Preview could deliver near-flagship quality at a fraction of the inference cost, which matters a great deal for agentic workloads that chain many calls together and are therefore dominated by per-token serving economics. It also signals that leading open-weight labs are competing on cost-effectiveness and agent-readiness rather than raw parameter count alone. The key figure is the roughly 22:1 ratio between total parameters \(600B\) and activated parameters \(27B\), the classic sparse-MoE trade-off that grows model capacity without proportionally growing per-inference compute. Notably, the announcement provides no benchmark results, no tokenizer or context-length information, and no details on expert count or routing, and it explicitly labels the model a preview rather than a finished release.

aibase · AIbase · Sep 21, 10:01

**Background**: Mixture of experts \(MoE\) is an architecture that uses multiple specialized sub-networks, called experts, plus a routing or gating mechanism that selects only the relevant experts for each input token. In the sparse variant, only a small number of experts fire per token, so a model can hold an enormous number of parameters while the compute spent per token stays close to that of a much smaller dense model. Agentic tasks — where a model plans, calls tools and takes multi-step actions with limited human supervision — amplify this effect, because each task can trigger dozens of forward passes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sparse_mixture-of-experts">Sparse mixture-of-experts</a></li>
<li><a href="https://www.emergentmind.com/topics/sparse-mixture-of-experts-moe-83af7574-934b-46eb-8c18-2ab3dcb5aafa">Sparse Mixture of Experts (MoE)</a></li>
<li><a href="https://www.relativity.com/blog/agentic-ai-is-in-the-air/">Agentic AI is in the aiR | Relativity Blog</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#large language models`, `#sparse MoE`, `#open-source`, `#model release`

---

<a id="item-10"></a>
## [Australia Calls for Slowing the Global AI Development Race](https://www.maitlandmercury.com.au/story/9354719/australia-urges-slowdown-of-ai-race-in-global-statement/) ⭐️ 6.0/10

Australia has issued a global statement urging a slowdown in the international race to develop artificial intelligence, according to a local news report. The statement frames AI development as something that should be paced deliberately rather than driven purely by competitive speed. If a mid-sized, allied democracy publicly pushes for restraint rather than acceleration, it adds a distinct voice to the global AI governance debate and could help shift international norms away from a pure speed race. It is relevant to policymakers, frontier AI labs, and companies that will have to operate under whatever international expectations emerge. The available report is brief and does not specify how many countries endorsed the statement, which concrete measures it asks for, or whether it carries any binding force. It also does not clarify how a &quot;slowdown&quot; would be defined or measured in practice, which is typically the hardest part of any AI restraint proposal.

gdelt · maitlandmercury.com.au · Sep 21, 22:30

**Background**: AI governance has moved over the past few years from purely national principles to international statements and summits, where governments discuss frontier-model safety, evaluation, and risk alongside innovation and competitiveness. Countries differ sharply on the trade-off: some emphasise safety and caution, while others argue that slowing down cedes advantage to rivals. Australia does not host a leading frontier AI lab, but as a middle power it can still shape norms and participate in multilateral AI safety discussions. The phrase &quot;AI race&quot; reflects the framing that states and companies are competing for strategic and economic advantage in the technology.

**Tags**: `#AI regulation`, `#AI policy`, `#Australia`, `#AI safety`, `#global governance`

---