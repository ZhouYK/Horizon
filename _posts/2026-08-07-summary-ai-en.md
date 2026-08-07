---
layout: default
title: "Horizon Summary: 2026-08-07 (EN)"
date: 2026-08-07
lang: en
report: ai
---

> From 278 items, 10 important content pieces were selected

---

1. [AI Generates 700,000 Virus Genomes; 16 Phages Survive Lab Test](#item-1) ⭐️ 9.0/10
2. [ChatGPT Gains Access to 70+ Adobe Tools via OpenAI Partnership](#item-2) ⭐️ 8.0/10
3. [OpenAI Launches Open Agent Plugins Standard to Unify AI Agents](#item-3) ⭐️ 8.0/10
4. [ByteDance Bets on 50T-Parameter Model, Bans Distillation](#item-4) ⭐️ 8.0/10
5. [ChatGPT Free Tier Gets Unlimited GPT-5.6 Luna; Paid Users Get Sol](#item-5) ⭐️ 8.0/10
6. [ChatGPT Upgrade: GPT-5.6 Luna for Free Users, Unlimited Chat, Paid Thinking Controls](#item-6) ⭐️ 8.0/10
7. [Codex with GPT-5.6 Sol Ultra Builds Superior Raccoon Heist Game](#item-7) ⭐️ 7.0/10
8. [Nature review assesses AI in drug discovery: state, challenges, path forward](#item-8) ⭐️ 7.0/10
9. [AI and Chemistry Expand Battery Electrolyte Design Space](#item-9) ⭐️ 7.0/10
10. [Global AI Investment Forecast to Exceed $1 Trillion by 2026](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI Generates 700,000 Virus Genomes; 16 Phages Survive Lab Test](https://www.aibase.com/news/30192) ⭐️ 9.0/10

Researchers at Stanford and Arc Institute used the Evo genomic language model to generate about 700,000 candidate phage genomes, synthesized 285 of them, and confirmed 16 that replicate and kill E. coli. The findings were published in Science on August 6. This is a milestone in generative biology because it moves AI-driven design from individual proteins to complete, functional viral genomes validated by laboratory replication. It also raises dual-use biosecurity concerns, as the same capability could potentially be applied to harmful pathogens. Evo is a genomic language model trained at single-nucleotide resolution on large-scale genome data, and the team designed only DNA sequences as output. The 16 validated phages out of 285 synthesized sequences highlight both the capability and the still-low success rate of de novo genome generation.

aibase · AIbase · Aug 7, 14:47

**Background**: Genomic language models \(gLMs\) borrow techniques from natural language processing, treating DNA as a sequence of four letters \(A, C, G, T\) and learning the statistical patterns of real genomes. Evo is an autoregressive gLM designed to interpret and generate sequences from molecular to whole-genome scale. De novo gene and genome synthesis allows researchers to build entirely new DNA sequences without an existing template; this study applies that approach to bacteriophages, viruses that infect bacteria, to demonstrate end-to-end AI-generated biology.

<details><summary>References</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/science.ado9336">Sequence modeling and design from molecular to genome scale with Evo | Science</a></li>
<li><a href="https://arxiv.org/pdf/2407.11435">Genomic Language Models : Opportunities and Challenges</a></li>

</ul>
</details>

**Tags**: `#AI`, `#generative biology`, `#genomics`, `#viral genomes`, `#biosecurity`

---

<a id="item-2"></a>
## [ChatGPT Gains Access to 70+ Adobe Tools via OpenAI Partnership](https://www.aibase.com/news/30185) ⭐️ 8.0/10

Adobe expanded its partnership with OpenAI, letting ChatGPT users access more than 70 creative applications, including Photoshop and Premiere, through natural language commands. Built on the OpenAI Apps SDK, the integration will cover nearly the full Adobe suite starting August 6. This integration significantly expands ChatGPT&\#x27;s utility from a text assistant into a hub for professional creative workflows. Designers and video editors can now chain AI reasoning with tools like Photoshop and Premiere without switching apps, streamlining production pipelines and normalizing AI-native tool orchestration. The integration uses the OpenAI Apps SDK and the Model Context Protocol \(MCP\) to synchronize the server, model, and user interface. Users enable the tools through plugin settings, with partial access from last year and full coverage rolling out from August 6 across photo editing, video production, and PDF generation.

aibase · AIbase · Aug 7, 10:47

**Background**: OpenAI Apps SDK is OpenAI&\#x27;s official toolkit for creating connectors that plug into ChatGPT, using MCP to expose tools, resources, and UI. MCP standardizes the wire format, authentication, and metadata so ChatGPT can reason about external connectors in the same way as built-in tools. Adobe had already offered partial ChatGPT integration last year; this expansion brings nearly all of its creative suite under ChatGPT&\#x27;s natural-language command.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Apps_SDK">OpenAI Apps SDK</a></li>
<li><a href="https://github.com/openai/openai-apps-sdk-examples">GitHub - openai/openai-apps-sdk-examples: Example apps for the Apps SDK · GitHub</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#Adobe`, `#AI integration`, `#Creative tools`, `#OpenAI`

---

<a id="item-3"></a>
## [OpenAI Launches Open Agent Plugins Standard to Unify AI Agents](https://www.aibase.com/news/30183) ⭐️ 8.0/10

On the first anniversary of the GPT-5 series, OpenAI released the Agent Plugins standard 1.0.0, an open, vendor-neutral specification that packages reusable AI agent components into portable plugins. It defines a shared format covering Agent Skills and MCP servers, enabling compatible clients to discover and load them with the same rules across platforms. This move is significant because it aims to end fragmentation in intelligent agent plugins and could shape the interoperability standards for the AI ecosystem. Developers and tool vendors will benefit from portable agents that work across different clients, potentially accelerating adoption of AI agents in production environments. The 1.0.0 specification covers two component types: Agent Skills, which provide reusable instructions and resources, and MCP servers, which connect agents to external tools and services. The standard is still early-stage and not yet proven at scale, though it builds on existing protocols such as Anthropic&\#x27;s Model Context Protocol.

aibase · AIbase · Aug 7, 10:47

**Background**: AI agents rely on plugins to extend their capabilities, but incompatible formats across platforms have created fragmentation. The Model Context Protocol \(MCP\) is an open standard introduced by Anthropic in November 2024 that standardizes how applications provide tools and context to LLMs, often described as a &\#x27;USB-C port for AI applications&\#x27;. The Agent Plugins standard builds on this idea by packaging such components into portable plugins that any compatible client can load consistently, similar to how standardized browser extensions work.

<details><summary>References</summary>
<ul>
<li><a href="https://agent-plugins.org/">Agent Plugins</a></li>
<li><a href="https://vercel.com/blog/introducing-agent-plugins">Introducing Agent Plugins - Vercel</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#OpenAI`, `#interoperability`, `#standards`, `#plugins`

---

<a id="item-4"></a>
## [ByteDance Bets on 50T-Parameter Model, Bans Distillation](https://www.aibase.com/news/30181) ⭐️ 8.0/10

ByteDance is reportedly planning a frontier large language model with over 5 trillion parameters, a scale some sources describe as 50 trillion, far exceeding rivals such as Kimi K3 and Qwen3.8-Max. The early-stage project is led by Xiang Liang and Shen Ke, and ByteDance&\#x27;s Seed department is being restructured to support it, with an internal ban on knowledge distillation. This move signals ByteDance&\#x27;s determination to leapfrog current Chinese frontier-model leaders such as Moonshot AI&\#x27;s Kimi K3 \(2.8T parameters\) and Alibaba&\#x27;s Qwen3.8-Max \(2.4T parameters\). The internal distillation ban could also slow the common industry practice of compressing stronger models into cheaper student models, forcing more investment in original training and compute. If realized, the model would dwarf recent frontier releases — Kimi K3 has 2.8T parameters and Qwen3.8-Max has 2.4T. No training timeline or compute budget has been disclosed, and the plan could change during Seed&\#x27;s restructuring.

aibase · AIbase · Aug 7, 09:47

**Background**: Knowledge distillation is a machine learning technique where a large, high-capacity &\#x27;teacher&\#x27; model guides a smaller &\#x27;student&\#x27; model by letting it learn from the teacher&\#x27;s outputs, improving performance while reducing inference cost and deployment overhead. In China&\#x27;s LLM race, Moonshot AI recently released the open-sourced Kimi K3, a 2.8T-parameter model with a 1-million-token context window, while Alibaba released Qwen3.8-Max, a 2.4T-parameter mixture-of-experts model on August 3, 2026. ByteDance&\#x27;s reported plan appears aimed at surpassing both.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://openlm.ai/kimi-k3/">Kimi K3 - openlm.ai</a></li>
<li><a href="https://www.datacamp.com/blog/qwen3-8-max">Qwen3.8-Max: Features, Benchmarks, and Pricing | DataCamp</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Large Language Models`, `#ByteDance`, `#Industry News`, `#Model Training`

---

<a id="item-5"></a>
## [ChatGPT Free Tier Gets Unlimited GPT-5.6 Luna; Paid Users Get Sol](https://www.aibase.com/news/30180) ⭐️ 8.0/10

OpenAI has upgraded ChatGPT, giving free users unlimited access to GPT-5.6 Luna, the fastest and most affordable model, rolling out this week. Paid Plus/Pro users receive GPT-5.6 Sol, a more accurate and higher-quality flagship model, which Sam Altman says is greatly improved. This is a major update to one of the most widely used AI products, expanding access to a current frontier model at no cost while giving paying customers a meaningful accuracy boost. The tiered rollout may pressure competitors and reshape user expectations for AI assistants. GPT-5.6 spans three tiers: Sol \(flagship\), Terra \(mid-tier\), and Luna \(fastest/most affordable\). Per benchmarks, Sol scores 81.46 vs Luna&\#x27;s 66.59 on BenchAlign, and input pricing is $5.00/M vs $1.00/M tokens; the free tier includes only Luna for text chat.

aibase · AIbase · Aug 7, 09:47

**Background**: GPT-5.6 is OpenAI&\#x27;s latest large language model family, released on July 9, 2026, following a limited preview on June 26 due to government restrictions. It is designed to expand capabilities across enterprise work, coding, scientific research, and cybersecurity, with multi-tier pricing to serve different user needs. ChatGPT is OpenAI&\#x27;s popular AI chatbot, and the free tier typically uses older or smaller models, so giving free users unlimited access to a current model is a notable shift.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>
<li><a href="https://benchlm.ai/compare/gpt-5-6-luna-vs-gpt-5-6-sol">GPT - 5 . 6 Luna vs GPT - 5 . 6 Sol : Benchmarks, Pricing... | BenchLM.ai</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#GPT-5.6`, `#AI product update`, `#LLM`

---

<a id="item-6"></a>
## [ChatGPT Upgrade: GPT-5.6 Luna for Free Users, Unlimited Chat, Paid Thinking Controls](https://www.aibase.com/news/30179) ⭐️ 8.0/10

OpenAI announced a major ChatGPT overhaul: free and Go users will get GPT-5.6 Luna as the default model starting next week, with unlimited text chats and a new &quot;Think&quot; button for advanced reasoning. Paid Plus and Pro users gain a slider to adjust the AI&\#x27;s thinking depth per response. This marks a significant expansion of free-tier access to OpenAI&\#x27;s latest model family, potentially shifting user expectations for AI assistant availability. The thinking-depth control gives paid users more flexibility, reflecting a broader industry trend toward adjustable inference-time compute. GPT-5.6 Luna is positioned as a cost-efficient, nano-tier model with a 1,050,000-token context window and pricing of $0.10 per million input tokens and $0.60 per million output tokens. The news also notes that file upload and image generation details were not disclosed, and the &quot;Think&quot; button includes anti-abuse safeguards.

aibase · AIbase · Aug 7, 09:47

**Background**: GPT-5.6 Luna is the latest model in OpenAI&\#x27;s GPT-5.6 family, roughly corresponding to the nano tier used in earlier GPT-5 releases. It supports text and image input with text output, and scores 52 on the Artificial Analysis Intelligence Index, well above the median of 17. The thought-depth adjustment feature, previously rolled out to mobile apps, allows users to switch between quick answers and deeper reasoning depending on the task. This update is part of OpenAI&\#x27;s broader push to make advanced AI capabilities available across free and paid tiers.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.6-luna">GPT-5.6 Luna Model | OpenAI API</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-luna">GPT-5.6 Luna - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/models/gpt-5-6-luna">GPT-5.6 Luna (max) - Intelligence, Performance &amp; Price Analysis</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#OpenAI`, `#GPT-5.6`, `#AI product update`, `#language model`

---

<a id="item-7"></a>
## [Codex with GPT-5.6 Sol Ultra Builds Superior Raccoon Heist Game](https://simonwillison.net/2026/Aug/7/moonlight-mayhem/#atom-everything) ⭐️ 7.0/10

Simon Willison gave the exact same one-shot game prompt to Codex Desktop running GPT-5.6 Sol Ultra instead of Claude Fable 5, and it produced a much better game called &\#x27;Moonlight &amp; Mayhem.&\#x27; The project took 52 minutes and would have cost about $23.28 in API fees. This hands-on comparison demonstrates that OpenAI&\#x27;s latest coding model, when combined with Codex&\#x27;s sub-agent-based workflow, can outperform Anthropic&\#x27;s Claude Fable 5 on a realistic game-building task. It gives developers concrete evidence about which frontier models handle complex, long-horizon coding autonomously. The game puts you in a museum, rescuing two raccoon crewmates so they can stack up and steal a golden sardine. Codex failed to spot a bug where each raccoon had a giant black sphere eyeball; Willison fixed it by asking &\#x27;Why do the raccoons have huge black spheres on them?&\#x27; and then &\#x27;Fix it.&\#x27;

rss · Simon Willison · Aug 7, 19:18

**Background**: Codex is OpenAI&\#x27;s coding agent that runs in a desktop app, and GPT-5.6 Sol Ultra is OpenAI&\#x27;s top-tier coding model that can make aggressive use of sub-agents to parallelize tasks. Claude Fable 5 is Anthropic&\#x27;s publicly available &\#x27;Mythos-class&\#x27; model, released in June 2026 with safety classifiers. The original game premise came from a GPT-3 and DALL-E prompt Willison created four years ago, and he previously used the same prompt to one-shot a game with Claude Fable 5.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5</a></li>

</ul>
</details>

**Tags**: `#AI`, `#code generation`, `#LLM comparison`, `#game development`, `#GPT-5.6`

---

<a id="item-8"></a>
## [Nature review assesses AI in drug discovery: state, challenges, path forward](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5PRnBXREdkUzdBRklQY3VoTXdBbm96TU5uckNwS2ZhX2ZsUmc3eFdpREpSeXREZlFwZ0twM2o3RlAtajBNaEMyNWpzeTZMN2hpalBfT05xUzNzUVJkZ0t3?oc=5) ⭐️ 7.0/10

Nature published a comprehensive review article examining the current state, challenges, and future directions of artificial intelligence in drug discovery. It provides a broad synthesis rather than a single breakthrough result. As AI becomes increasingly integrated into pharmaceutical research, this authoritative review helps scientists and industry leaders distinguish real progress from hype. It outlines where AI can meaningfully accelerate drug discovery and what obstacles remain, shaping expectations across the healthcare sector. The review likely covers AI applications such as target identification, molecular generation, property prediction, and clinical trial design, while discussing limitations like data quality, reproducibility, and regulatory validation. It emphasizes the need for rigorous evaluation and interpretability in AI-driven drug discovery.

google\_news · Nature · Aug 7, 09:50

**Background**: Drug discovery is a long, expensive process with high failure rates. Machine learning, including deep learning and generative models, has been applied to shorten timelines and reduce costs by predicting drug properties and designing new molecules. As a leading scientific journal, Nature&\#x27;s review provides a credible benchmark for the field.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Virtual_screening">Virtual screening</a></li>
<li><a href="https://en.wikipedia.org/wiki/Molecular_docking">Molecular docking</a></li>
<li><a href="https://en.wikipedia.org/wiki/De_novo_drug_design">De novo drug design</a></li>

</ul>
</details>

**Tags**: `#AI`, `#drug discovery`, `#healthcare`, `#machine learning`

---

<a id="item-9"></a>
## [AI and Chemistry Expand Battery Electrolyte Design Space](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZW9DbFdpeTh0emlXSEkxaE9FdmFuTlhraFZQbWtwSGtVMWUwUWM0SWc3dkVHaVo1T01EZEphSnlzR0pZT1llVUluNzlHSFJhSE5NdXBfckFYTDZfWXdOVTIxNEhuQXlPVEFrMno4NHRuUnlWZTY2eUpWY3ZneHBnYkpOWHI3bFFORTZoclNuNGVuVlFOR0pWMzFVdTk?oc=5) ⭐️ 7.0/10

A Cornell Chronicle research article reports that combining artificial intelligence with chemistry can broaden the design space for battery electrolytes. This approach could open new possibilities for discovering and optimizing energy-storage materials. Battery electrolytes are critical to battery performance, safety, and longevity, so expanding their design space is important for next-generation energy storage. AI-driven exploration could accelerate the development of safer and higher-energy-density batteries, benefiting electric vehicles, portable electronics, and grid storage. The report emphasizes integrating AI with chemical insight instead of relying solely on blind trial-and-error screening, which can reduce the time and cost of electrolyte discovery. Specific electrolyte chemistries or performance metrics were not disclosed in the provided summary.

google\_news · Cornell Chronicle · Aug 7, 18:00

**Background**: Battery electrolytes are the conductive medium—often liquid, gel, or solid—that allows ions to move between electrodes during charge and discharge, directly affecting battery efficiency and safety. In materials science, the &\#x27;design space&\#x27; refers to the vast range of possible chemical compositions and structures that can be explored for a given application. Because this space is enormous, machine learning and AI are increasingly used to screen candidate materials and guide optimization, which is the approach highlighted in this Cornell work.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/role-electrolytes-batteries-chester-beard-lhnxc">The role Electrolytes play in batteries</a></li>
<li><a href="https://www.takomabattery.com/what-is-an-electrolyte/">What is an electrolyte - a component of battery - TYCORUN ENERGY</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0927025624006530">Exploring design space: Machine learning for multi-objective ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#chemistry`, `#battery`, `#electrolyte`, `#materials science`

---

<a id="item-10"></a>
## [Global AI Investment Forecast to Exceed $1 Trillion by 2026](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOeDZ2dUk3YUJGenFKNm9feDlCc3RxZU9jaXA0WkYxM21uY2dBVmpGXzVMVkQtSXpUbjNEVEJjSGY0M1ZWcExLZ0U1dFNfaVhRc3FSV0IwOXJRMWwwLXpkQTE5RWZvYXBIV1B3NVVvUTdscUlScm5id29aRnNXVEF1OU56T25qbnAwV3dVNUJTZDdaVF8tRHE1SExhb1g5TThkQ0tHbWxBNlI?oc=5) ⭐️ 7.0/10

Goldman Sachs forecasts that global artificial intelligence investment will surpass $1 trillion in 2026, highlighting the accelerating pace of AI spending. This projection underscores AI as one of the most significant investment opportunities in the coming years. This forecast signals that AI investment is expected to grow at an extraordinary scale, affecting technology companies, investors, and industries worldwide. It reflects the mainstreaming of AI as a core economic driver and could shape capital allocation decisions across the global economy. The forecast comes from Goldman Sachs, a leading global investment bank, and likely includes spending on AI infrastructure, research, and applications. The $1 trillion figure represents a substantial increase from current levels, though specifics of the calculation were not provided in the available content.

google\_news · Goldman Sachs · Aug 7, 18:56

**Background**: AI investment encompasses spending by companies and governments on artificial intelligence technologies, including computing power, data centers, software, and talent. Major investment banks like Goldman Sachs regularly produce forecasts to guide investors and policymakers. Projections of this scale indicate that AI is seen as a transformative technology with broad economic impact. The forecast may also reflect the rapid adoption of generative AI and large language models in recent years, driving the need for significant capital expenditure.

**Tags**: `#AI`, `#investment`, `#industry trends`, `#economics`, `#forecast`

---