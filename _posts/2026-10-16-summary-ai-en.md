---
layout: default
title: "Horizon Summary: 2026-10-16 (EN)"
date: 2026-10-16 23:04:10 +0000
lang: en
report: ai
---

> From 166 items, 10 important content pieces were selected

---

1. [Quanta Profiles Push to Make AI Benchmarking a Rigorous Science](#item-1) ⭐️ 8.0/10
2. [Anthropic&\#x27;s Claude Code team: AI review shifts human code review to risk-based checks](#item-2) ⭐️ 7.0/10
3. [AWS launches Reflection Beam, an open-weight model for agentic coding](#item-3) ⭐️ 7.0/10
4. [AI Meets Life-Cycle Assessment for Sustainable Materials Discovery](#item-4) ⭐️ 7.0/10
5. [Mini Brain Organoids &\#x27;Read&\#x27; Braille, Advancing Biohybrid Computing](#item-5) ⭐️ 7.0/10
6. [Terry Tao Profiled in NYT Debate on AI&\#x27;s Future in Math](#item-6) ⭐️ 7.0/10
7. [Citizen Science Groups Grapple With AI Slop Flooding Their Data](#item-7) ⭐️ 6.0/10
8. [AMA issues governance framework for agentic AI in healthcare](#item-8) ⭐️ 6.0/10
9. [Orlando mother settles lawsuit with AI company over son&\#x27;s suicide](#item-9) ⭐️ 6.0/10
10. [France 24: Books Scanned and Destroyed to Train AI](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Quanta Profiles Push to Make AI Benchmarking a Rigorous Science](https://news.google.com/rss/articles/CBMinAFBVV95cUxPMXlhU1kzY09uSjZ3ZkVzWTRGNDFNeHZYRlBPcGRkVHEtTGRhQUJlLVRUZHJHQXpzekdSWGNITDRIWms4LUxwbldZU09pQ01wLTBzY0hkYVoxbnpvWVItTEtsWE4yLV9NS280amEwMVNnRnR6Sl9jNlZZVFQycEVHNVFjTXd4VEhDRkpFT1hKWE5MVWRGTGRMTngtUUU?oc=5) ⭐️ 8.0/10

Quanta Magazine published a profile of a researcher who is campaigning to turn AI benchmarking from what he calls a &quot;dark art&quot; into a genuine scientific discipline. The piece frames today&\#x27;s model evaluation practices — ad hoc task sets, scoring rules and reporting protocols — as methodologically weak and in need of standardization. Benchmark scores drive model launches, funding, regulation and purchasing decisions, so weak methodology can mislead the entire AI ecosystem. If evaluation becomes a reproducible science, researchers, labs and policymakers will be able to compare models fairly instead of relying on numbers that may not replicate. The article&\#x27;s concerns line up with widely documented benchmarking problems: benchmark contamination \(test data leaking into training\), sensitivity to prompt formatting and scoring choices, randomness across runs, and multiple-hypothesis testing that inflates apparent gains. Programs such as Epoch AI&\#x27;s FrontierMath illustrate the trend toward carefully curated, contamination-resistant benchmarks for advanced capabilities.

google\_news · Quanta Magazine · Oct 16, 16:59

**Background**: AI benchmarking is the practice of evaluating and comparing models using standardized tasks, datasets, prompts, scoring rules and reporting protocols, usually to rank relative performance on leaderboards. Because large language models are stochastic and their training data is often undisclosed, results can be hard to reproduce — a long-standing concern in machine learning research, where reproducibility means rerunning an experiment and getting the same results. Quanta Magazine is a publication known for accessible, in-depth coverage of mathematics, physics and computer science, so a profile there signals that benchmarking methodology is being taken seriously as a research topic in its own right.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/ai-benchmarking">AI benchmarking</a></li>
<li><a href="https://epoch.ai/frontiermath">FrontierMath: LLM Benchmark for Advanced AI Math... | Epoch AI</a></li>

</ul>
</details>

**Tags**: `#AI benchmarking`, `#machine learning evaluation`, `#reproducibility`, `#AI research`, `#Quanta Magazine`

---

<a id="item-2"></a>
## [Anthropic&\#x27;s Claude Code team: AI review shifts human code review to risk-based checks](https://simonwillison.net/2026/Oct/16/code-review/) ⭐️ 7.0/10

In a post on Anthropic&\#x27;s claude.dev blog, Claude Code team members Addy Osmani, Morgan Westlee Lunt and Qing Wang argue that asking &quot;did a human read the code?&quot; is an imprecise proxy for the better question: &quot;what could go wrong with this change, and which check—automated or human—is the right one to catch it?&quot; They say review now runs continuously, more like spellcheck while you write, so most changes have already been reviewed and fixed by Claude at least once before a human looks. This reframes human code review from a mandatory end-of-process gate into a risk-targeted activity, which could change how engineering teams staff, time and measure review as AI-generated and agent-written code becomes routine. If widely adopted, it shifts the value of senior engineers away from reading every diff toward defining what actually matters in their part of the codebase. The post describes REVIEW.md files written by code owners that tell reviewers what matters in their area and are deliberately kept short, plus a separate check of whether reviewers actually follow those files. It also notes that Claude catches most routine mistakes before a human is asked to look, freeing team attention for higher-level design and correctness questions; the excerpt in the news item itself is brief and contains no benchmarks or measured defect-rate data.

rss · Simon Willison · Oct 16, 22:06

**Background**: Claude Code is Anthropic&\#x27;s agentic coding tool that runs in the terminal, IDEs and the web, able to read a codebase, edit files and run commands. Traditionally, code review means opening a pull request and waiting for a colleague to read the diff before it can be merged—a gate at the end of the development road. Continuous AI review inverts that model: an AI agent inspects changes as they are written, so the human reviewer arrives later and focuses on the changes that carry the most risk. &quot;Risk-based checks&quot; means deciding, per change, which verification method is most likely to catch the failure mode at hand rather than applying one uniform process to everything.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.dev/blog/solving-code-review-at-anthropic/">How the Claude Code team does code review / claude.dev Blog</a></li>
<li><a href="https://code.claude.com/docs/en/how-claude-code-works">How Claude Code works - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#AI code review`, `#Claude Code`, `#Anthropic`, `#software engineering`, `#developer productivity`

---

<a id="item-3"></a>
## [AWS launches Reflection Beam, an open-weight model for agentic coding](https://news.google.com/rss/articles/CBMivgFBVV95cUxPSElxZ0NWWkFqY3FmY29PN3JhMHRxSVo3eEJMLUYxMmtNNVl2LUlzNjZsU05heFlmby1aWFh4ZFRCRTRobDMwdjZvdGI1NlNCb1ZGRS0zMUdqQjJvRFpQb0JoN1NFLXhGdzI1WFl0Z0UtRWNVNWYySEZDV05GdGhzZHhsdU1BT3Z2Y09uWUo2TXZJZEY4ekotQVJYM0hWQ3VyWHJvSnU2WFU0T2JLVTNGSkVlcTk0c2M5amhJN01n?oc=5) ⭐️ 7.0/10

Amazon Web Services announced Reflection Beam, an open-weight model purpose-built for agentic coding workloads running on AWS. Beam comes from Reflection AI, a Brooklyn-based startup whose first open-weight release is a sparse Mixture-of-Experts model with 501 billion total parameters and 23 billion active parameters, designed for coding, reasoning and agentic tasks. It signals that frontier-grade open-weight models are being folded directly into mainstream cloud platforms, giving enterprises a way to run autonomous coding agents on AWS infrastructure with more control, auditability and self-hosting options. It also positions a US lab as a counterweight to the wave of Chinese open-weight coding models such as DeepSeek, Qwen and Kimi that have dominated that segment. Beam uses a sparse Mixture-of-Experts architecture with 501B total parameters but only 23B active per token, which keeps inference compute far lower than its headline size suggests. Note that &quot;open-weight&quot; means only the trained parameters are released — rights to fine-tune, modify or redistribute depend on the license, and full training data or source code are typically not included.

google\_news · Amazon Web Services \(AWS\) · Oct 16, 15:23

**Background**: Open-weight models are AI systems whose learned parameters are published so others can download and run them, as opposed to fully proprietary models accessible only through an API; this differs from &quot;open source AI,&quot; which also releases code, data and documentation. &quot;Agentic coding&quot; refers to AI agents that do more than autocomplete: they plan, call tools, execute code, run tests and iterate on a codebase semi-autonomously, which raises both productivity gains and quality risk. AWS is the largest cloud provider, so hosting a model like Beam matters because it determines how easily enterprises can deploy agents inside their existing, governed infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://reflection.ai/blog/introducing-beam">Introducing Beam: Reflection’s 501B open-weight model</a></li>
<li><a href="https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/">Reflection debuts Beam, an open-weight AI model to rival ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**Tags**: `#Agentic coding`, `#Open-weight models`, `#AWS`, `#AI agents`, `#LLM`

---

<a id="item-4"></a>
## [AI Meets Life-Cycle Assessment for Sustainable Materials Discovery](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5vVHdtU29sd1FMbVJMRFBNclhrTlZYZlJfX2JnS2RGc29vUmF2NGs2TGlFVWtDRUdMTEVRaWMxakVMWkY4aTRiWkhVWC03MldoZVdndm9iNlFzbXNUQk5Z?oc=5) ⭐️ 7.0/10

A Nature article titled &quot;Artificial intelligence for life-cycle-aware sustainable materials discovery&quot; outlines how machine learning can be integrated with life-cycle assessment \(LCA\) so that newly discovered materials are screened not only for performance but also for environmental impact across their entire lifespan. The work frames life-cycle awareness as a first-class objective inside AI-driven materials discovery pipelines rather than an after-the-fact check. Materials discovery has traditionally optimized for function and cost, which can produce high-performance materials whose extraction, processing or disposal causes substantial environmental harm; embedding LCA into AI screening could steer the field toward genuinely sustainable alternatives. This matters for researchers, industry R&amp;D teams and policymakers who increasingly need defensible sustainability claims backed by quantitative analysis rather than post-hoc marketing. The approach hinges on combining predictive ML models for material properties with life-cycle inventory and impact data, which introduces challenges such as sparse or inconsistent LCA datasets, differing system boundaries, and the difficulty of extrapolating environmental impacts for materials that do not yet exist at scale. Readers should note that life-cycle-aware screening is only as reliable as the underlying inventory data and the assumptions used to model future production routes.

google\_news · Nature · Oct 16, 10:14

**Background**: Life-cycle assessment \(LCA\) is a methodological framework for evaluating the environmental impacts of a product or process across all stages of its life cycle, from raw material extraction through manufacturing, distribution, use and end-of-life disposal. In parallel, AI-driven materials discovery uses machine learning models, trained on databases of known compounds and simulations, to predict promising new materials far faster than trial-and-error experimentation; efforts such as Google DeepMind&\#x27;s have generated millions of candidate structures. This article sits at the intersection of those two fields, asking how environmental sustainability criteria can be built into the AI search itself.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Life-cycle_assessment">Life-cycle assessment - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/earth-and-planetary-sciences/life-cycle-assessment">Life Cycle Assessment - an overview | ScienceDirect Topics</a></li>
<li><a href="https://gave.pages.dev/posts/ai-for-materials-science-google-deepmind/">Ai For Materials Science Google Deepmind | gave</a></li>

</ul>
</details>

**Tags**: `#AI for Science`, `#Materials Discovery`, `#Sustainability`, `#Machine Learning`, `#Life-Cycle Assessment`

---

<a id="item-5"></a>
## [Mini Brain Organoids &\#x27;Read&\#x27; Braille, Advancing Biohybrid Computing](https://news.google.com/rss/articles/CBMizwFBVV95cUxNTlYwaVZfbHZfT1BsQ3lhWndiRUFNWGRKZ3lZY05ZS2h1RHhyWVR0RmwtLURMbnZndFBnUVFjd1M0dTI3RHA2TXdDZXNFSU41eHdFcGJzYkk1czZJbjR2UWhrTjdQTEttTUJ3bzQ5TnM0UkRPUWh2N0R4cGh3UVdMd3VzT01iX2Vtb1hxUnFoOXExcm9TX1Q1WUNtZmllZ3drM3R5U3RvNzdsTDJ3V05KYzJ1Wmx6THFDZU5MMHhaVm1OQ2YtN0JQdkJ3ekNZb3c?oc=5) ⭐️ 7.0/10

Researchers have demonstrated that miniature brain organoids — lab-grown clusters of human neural tissue — can respond to and effectively &\#x27;read&\#x27; Braille-like patterns of raised dots, marking a key milestone in biohybrid computing. The work was highlighted by Frontiers, suggesting the organoids can translate structured tactile input into detectable neural signals. If living neural tissue can reliably encode external inputs, it could serve as a low-energy, highly plastic computing substrate that complements silicon hardware, potentially enabling new kinds of sensing, learning and computation. This matters for researchers in neuroscience, biocomputing and neuromorphic engineering exploring alternatives to conventional chips. The experiments use cerebral organoids grown from pluripotent stem cells into three-dimensional cultures, whose cytoarchitecture resembles parts of the embryonic human brain; the system still lacks sensory organs, blood vessels and full brain architecture, so its ability to generalise beyond simple patterns like Braille remains an open question.

google\_news · Frontiers · Oct 16, 04:01

**Background**: Brain organoids, also called cerebral organoids, are self-assembled three-dimensional tissue cultures derived from pluripotent stem cells that mimic aspects of the developing human brain, and they are widely used to model neurological disease in vitro because human brain physiology differs substantially from that of animal models. Biohybrid systems integrate such biological material with artificial electronic or mechanical components, combining the adaptability of living tissue with the precision of engineered hardware; biohybrid computing is a young field exploring whether neurons and other cells can perform useful computation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain_organoid">Brain organoid</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biohybrid_system">Biohybrid system - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#biohybrid computing`, `#brain organoids`, `#neuroscience`, `#biocomputing`, `#Braille`

---

<a id="item-6"></a>
## [Terry Tao Profiled in NYT Debate on AI&\#x27;s Future in Math](https://news.google.com/rss/articles/CBMib0FVX3lxTE5obDJaUW0zTDU0Q2RqRGd6QlRabDFENjNiMTJtR0ZLOXkycWhXNjVlT2Vxc1hFRWhacTd6MEFyM01fU1c5UmNxME82N1VVVDFCWnBKWVZ0bDdvVXRZLXFXaldhNF83RG1keHVIV04xVQ?oc=5) ⭐️ 7.0/10

The New York Times has published a profile of mathematician Terence Tao, framing him as a leading voice in the debate over how artificial intelligence will reshape mathematics. The item available here consists only of the headline and a link, so no article text, quotes, or specific claims from the piece are accessible. Tao is one of the most influential mathematicians alive, so his stance carries weight in shaping how the research community regards AI as a tool for doing mathematics. The debate matters beyond academia because advances in AI-driven reasoning and proof automation could eventually influence how mathematical results are discovered, verified, and taught. Because only a headline and link are provided, the article&\#x27;s specific arguments, examples, and interviewees cannot be summarized here. The likely context is Tao&\#x27;s publicly documented experimentation with large language models such as GPT-4 and with the Lean proof assistant, which he has discussed in his blog and talks.

google\_news · The New York Times · Oct 16, 20:15

**Background**: Terence Tao is an Australian-American mathematician at UCLA who received the Fields Medal in 2006 and is known for work spanning harmonic analysis, partial differential equations, additive combinatorics, and number theory. He also maintains a widely read research blog where he has written extensively about AI tools and their possible role in mathematics. Two technologies central to this debate are large language models, which generate plausible mathematical text but can also produce convincing errors, and formal proof assistants like Lean, which let mathematicians write proofs that a computer can verify step by step. Much of the discussion in the field concerns whether these tools will serve as assistants to human mathematicians or eventually automate substantial parts of mathematical discovery.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2015/07/26/magazine/the-singular-mind-of-terry-tao.html">The Singular Mind of Terry Tao - The New York Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving - Wikipedia</a></li>
<li><a href="https://www.ebsco.com/research-starters/biography/terence-tao">Terence Tao | Biography | Research Starters | EBSCOhost</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#Terry Tao`, `#research`, `#future of math`

---

<a id="item-7"></a>
## [Citizen Science Groups Grapple With AI Slop Flooding Their Data](https://news.google.com/rss/articles/CBMie0FVX3lxTE0tOHlmZ29mTmVUOUU1OGJ6NW0yRWo1c1lrVFV0VmNSd2FwMzViZGNtNWIyVHVmaVUwTERmeFVKZkhwN1R5Z0xmWHlDSS1IaG1kaUNoY3lnQUd5cVgzN3pIRGZGR3Y1V29Gc2hSbnRfX0NPRi1EVWZSM1RxMA?oc=5) ⭐️ 6.0/10

The New York Times reports that citizen science groups are struggling with the rise of AI-generated low-quality content — commonly called &quot;AI slop&quot; — that is contaminating their data and disrupting their volunteer-driven workflows. The article describes how projects that depend on crowdsourced contributions are now having to filter out machine-generated submissions. Citizen science projects rely on the assumption that volunteers contribute genuine observations and classifications, so an influx of AI-generated junk threatens both the scientific validity of their datasets and the trust that keeps volunteers engaged. This reflects a broader ecosystem-wide problem, as Wikipedia, open-source repositories, survey platforms and social media all now spend significant effort detecting and removing machine-generated noise. The article focuses on the operational strain rather than any specific technical fix, and at present there is no standard, widely agreed method for separating authentic volunteer contributions from AI-generated ones. Notably, researchers publishing in early 2026 noted that &quot;AI slop&quot; has so far resisted formal definition, which makes automated detection and platform policy enforcement even harder.

google\_news · The New York Times · Oct 16, 18:36

**Background**: Citizen science refers to research in which non-professional volunteers partner with scientists to collect, classify or analyze data, spanning fields such as astronomy, ecology, environmental monitoring and public health; well-known examples include Zooniverse projects and distributed-computing efforts like SETI@home. &quot;AI slop&quot; is the informal term for poor-quality, mass-produced text or images generated by machine-learning models and posted online in large volumes. Because citizen science platforms are designed to accept contributions at scale from anonymous or lightly vetted participants, they are structurally exposed to this kind of low-effort, high-volume noise.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_science">Citizen science - Wikipedia</a></li>
<li><a href="https://www.zooniverse.org/projects">Projects | Zooniverse</a></li>

</ul>
</details>

**Tags**: `#AI slop`, `#citizen science`, `#data quality`, `#crowdsourcing`, `#AI-generated content`

---

<a id="item-8"></a>
## [AMA issues governance framework for agentic AI in healthcare](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPWHpsNFBWMDdsUVpza0hwN3BMeUZnSEhhdkNIWWNNS01KUWg2ZFZpLU5KSktYUFo2alVPQTJRQlV6eEZqdWo4cU50R2hXc19hb29pU1c3ZzJSVkl4dTY0Nk5yc3ZtUDRRV09NN1lsUmRmSmJrZTRxTXoyTU1fZGF3bEZ0MFlNQUVCTWQ3Wm9SUWpoNjdjSTRMTnBVQkkydTI5T2lJUG9BTHlSNzRnOGloTncyWXowOC1CcFJ0cDFTY0NCdw?oc=5) ⭐️ 6.0/10

The American Medical Association \(AMA\) has rolled out a governance framework for agentic AI solutions in healthcare, as reported by Fierce Healthcare. The move marks an institutional effort by the largest U.S. physician organization to set expectations for how autonomous, goal-seeking AI systems should be overseen in clinical settings. Because agentic AI systems can plan and take actions across software systems with limited human supervision, their entry into clinical workflows raises questions about accountability, safety, and liability that existing rules do not clearly answer. Guidance from a body as influential as the AMA can shape how hospitals and vendors design, procure, and audit these tools, and may become a de facto benchmark for responsible deployment across the healthcare industry. The framework is governance guidance rather than binding regulation, and reporting so far is headline-level, so specific provisions on human oversight, audit trails, and accountability are not yet detailed in public coverage. Definitions of agentic AI themselves remain unsettled, with common descriptions ranging from systems that pursue goals with limited supervision \(IBM\) to those that blend reasoning and execution to plan workflows, select tools, and act across systems \(Microsoft\).

google\_news · Fierce Healthcare · Oct 16, 18:00

**Background**: Agentic AI refers to AI systems that actively pursue goals through their own actions rather than only generating content for a human to act on. In healthcare, this could mean software that autonomously schedules follow-ups, queries patient records, or drafts clinical documentation, which collides with strict privacy rules such as HIPAA and with FDA oversight of clinical AI tools. The AMA is the largest U.S. physicians&\#x27; association and is known for publishing the CPT coding system and medical ethics guidance, giving its recommendations significant weight among clinicians, hospitals, and health-tech vendors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is agentic AI? - IBM</a></li>
<li><a href="https://agentic.ai/what-is-agentic-ai">What Is Agentic AI? Definition, 6 Levels &amp; Examples (2026)</a></li>
<li><a href="https://www.microsoft.com/en-us/software-development-companies/resources/articles/what-is-agentic-ai">What is Agentic AI? | Software Development Companies</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#agentic AI`, `#healthcare AI`, `#policy`, `#responsible AI`

---

<a id="item-9"></a>
## [Orlando mother settles lawsuit with AI company over son&\#x27;s suicide](https://news.google.com/rss/articles/CBMixwFBVV95cUxONGhRNVZTeFFpQk5FZHlfcDVFSDRqLS1fbThkMFlaWEVUdFY2N3RNZHdlSGpYMjBlVUtONDFEb0gyRGhIZ25WSlBrTDJQWmlCSzEtUzYzX2xaWGdpcGduZTJnNndHWW1SQTUwWDFUdmt5emxXWURpa2JpVzR3N1VvTDV3UVlIN2VGekowMm5VbTROR3NjZkNoQ3ZaWVBPbThHOUw5SVNBeVJ3Wjl3amlZdkgxYnRwRlBMeFdVZWxDNGRhNVNxdy1n?oc=5) ⭐️ 6.0/10

A mother in Orlando, Florida has settled her lawsuit against an AI company over the suicide of her 14-year-old son, according to a report by WKMG. The settlement closes one of the most closely watched wrongful-death cases involving a consumer AI chatbot, though the terms of the agreement have not been publicly detailed. Because a settlement avoids a final court ruling, the case leaves unresolved the central legal question of whether an AI chatbot counts as a &quot;product&quot; for liability purposes, but it still signals that AI companies now face real financial and reputational exposure when emotionally engaging chatbots are used by minors. The item is currently only a headline, so the settlement amount, the specific company named, and whether any safety commitments were included in the agreement are not confirmed in the available content. The case has nonetheless been cited by legal analysts as part of a broader wave of AI product-liability litigation, alongside state-level actions such as the 2025 Nevada attorney general suit against a messaging-app company.

google\_news · WKMG · Oct 16, 21:50

**Background**: Consumer companion chatbots built on large language models are designed to hold long, empathetic conversations, and critics argue these engagement-maximizing design choices can be harmful to vulnerable teenagers. The underlying lawsuit grew out of a 2024 wrongful-death complaint that press coverage widely linked to the companion-chatbot service Character.AI, filed after a 14-year-old boy developed a deep emotional attachment to an AI character and later took his own life. Under U.S. law, plaintiffs typically must argue that a chatbot is a defective &quot;product&quot; and that its maker failed to warn users of foreseeable risks, a legal theory courts are only beginning to test.

<details><summary>References</summary>
<ul>
<li><a href="https://www.klgates.com/thought-leadership/AI-Product-Liability-The-Next-Wave-of-Litigation-3-27-2026">AI Product Liability: The Next Wave of Litigation | HUB | K&amp;L ...</a></li>
<li><a href="https://www.awkolaw.com/when-the-chatbot-becomes-the-defendant/">Product Liability For AI Chatbots: What Changed - awkolaw.com</a></li>
<li><a href="https://www.winstontaylor.com/insights/is-an-ai-chatbot-a-product">Is an AI chatbot a “product”? - Winston Taylor</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI ethics`, `#legal`, `#chatbots`, `#product liability`

---

<a id="item-10"></a>
## [France 24: Books Scanned and Destroyed to Train AI](https://news.google.com/rss/articles/CBMixAFBVV95cUxQT2N5ak5YY2JzWFEzOGdsM2owZlNCNEYxSFd0SmdZZnhMVEtSdW9vN2Z1Q1RQS2IzTE9RT0RHUmNzeTQwSWNpMHg0SS1kYUpuYlJEUXhuZVlZeGM5N3g0ZTl2X2F6ZFRSa0JGUmVHSXdFU0JSQ0dON0t5d19DcFkxWXBPdzUzOXNEenAyZDZaQ2lxbUh2ZHhvWU84OEY5Q0VVRlRjV2lTb0U0cmFsR0lZdk9MbmdPcldEeGxTVzJ0YmpKVlYz?oc=5) ⭐️ 6.0/10

France 24 aired a Focus report examining how physical books are being cut apart, scanned and then discarded so their text can be fed into artificial intelligence training pipelines. The segment highlights the industrial-scale practice of destructive book scanning by commercial AI data vendors, whose digitized output often ends up in large text corpora used to train models. The report puts a visible, physical face on the debate over AI training data, showing that the copyright and fair-use fights are not abstract but involve real books being permanently destroyed. It matters to authors, publishers, libraries and AI developers, and it feeds into ongoing litigation and licensing disputes over whether AI firms should pay for the books they train on. Destructive scanning typically means the book&\#x27;s spine is sliced off and its loose pages are fed through a high-speed scanner, which is far faster and cheaper than handling intact volumes but leaves the physical copy unusable. Notable corpora built this way include the Books3 dataset, which contained roughly 196,640 books by authors such as Stephen King, Margaret Atwood and Zadie Smith and was later taken down after anti-piracy pressure in 2023.

google\_news · France 24 · Oct 16, 09:31

**Background**: Book scanning, or digitization, converts physical books into images, electronic text or e-books, and large-scale projects such as Project Gutenberg, Google Books and the Open Content Alliance have made millions of volumes searchable online. Destructive scanning is a well-known variant in which the binding is removed so pages can pass through automated, high-throughput scanners capable of thousands of pages per hour. Large language models like those behind modern chatbots are trained on enormous text corpora, and books are prized because they offer long, coherent, high-quality prose; when such corpora are assembled from scanned or pirated books, they raise unresolved copyright questions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Destructive_book_scanning">Destructive book scanning</a></li>
<li><a href="https://www.aiaaic.org/aiaaic-repository/ai-algorithmic-and-automation-incidents/books3-dataset">AIAAIC - Books3 dataset</a></li>
<li><a href="https://interestingengineering.com/innovation/anti-piracy-group-shuts-down-books3-a-popular-dataset-for-ai-models">Anti-piracy group shuts down Books3, a popular dataset for AI ...</a></li>

</ul>
</details>

**Tags**: `#AI training data`, `#copyright`, `#books`, `#ethics`, `#media`

---