---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22 23:03:18 +0000
lang: en
report: ai
---

> From 142 items, 8 important content pieces were selected

---

1. [Amazon Nears $7.5 Billion Deal to Acquire AI Startup Decart](#item-1) ⭐️ 8.0/10
2. [mod\_wsgi Creator Graham Dumpleton Releases Muru, an AI-Assisted Rust ASGI/WSGI Server](#item-2) ⭐️ 7.0/10
3. [OpenAI Chief Scientist Reportedly Calls for Industry Limits on AI Development](#item-3) ⭐️ 7.0/10
4. [Dev fits 367K-parameter AI language model on a floppy for 486DX and Pentium PCs](#item-4) ⭐️ 7.0/10
5. [Signal Blocks AI Agents From Reading Your Screen](#item-5) ⭐️ 6.0/10
6. [Nvidia Chip Sales Reportedly Targeted in California Criminal Probe](#item-6) ⭐️ 6.0/10
7. [South Korea&\#x27;s education minister resigns amid national AI cheating panic](#item-7) ⭐️ 6.0/10
8. [Chinese open-weight AI models push into the U.S. market](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Amazon Nears $7.5 Billion Deal to Acquire AI Startup Decart](https://news.google.com/rss/articles/CBMisgFBVV95cUxOZlcwRzJaaUdqUEpSSWNPa2U5N3VLRS1EQXhtRGxGWU1CMFFsLXhiX2xzcXlUWnNKTkVINVVSVkN1aHFwcUstbTZsckFLSmFYVHJwVlgzdXM5UFhZbFhEa09fVWNEZXc0cEJrT1B3c0hLSVBINEx3Sk9tOW9od2V3WjFLRmN4Mm1jSFBZNWNXelVHSU12dEkzTV84V1lrT0pydUJUUGpZYlQ3Vk05bXRzTkhn?oc=5) ⭐️ 8.0/10

Amazon is reportedly in advanced talks to acquire Decart, an Israeli AI startup building real-time world models, for roughly $7.5 billion. Neither Amazon nor Decart has publicly confirmed the deal, which was reported by PYMNTS.com. If completed, the deal would rank among Amazon&\#x27;s largest AI acquisitions and signal that hyperscalers now view real-time world models as a strategic battleground alongside large language models. It would also mark a dramatic valuation jump for Decart and could push rivals like Google, Microsoft and Meta to pursue similar targets. The reported price would represent a steep premium over Decart&\#x27;s last known private valuation, and the talks could still collapse since no agreement has been confirmed. Decart&\#x27;s pitch is efficiency: generative video and simulated environments rendered frame by frame at millisecond latency, which is far more demanding than conventional one-shot image or video generation.

google\_news · PYMNTS.com · Nov 22, 22:41

**Background**: Decart is an Israeli AI research lab that builds real-time world models — generative AI systems that produce interactive video and simulated environments frame by frame with very low latency — and is backed by Sequoia and Benchmark. World models are increasingly seen as foundational for robotics, games, and interactive media, because they let a model simulate how an environment responds to actions rather than just generate a static clip. Amazon has been steadily expanding its AI footprint through its own model and chip efforts as well as large investments in outside AI companies, making a deal of this size consistent with its broader strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Decart">Decart - Wikipedia</a></li>
<li><a href="https://decart.ai/">Decart - The Live AI Lab the World Runs On</a></li>
<li><a href="https://decart.ai/about">Decart AI Lab | About Our Mission &amp; Generative AI Research</a></li>

</ul>
</details>

**Tags**: `#Amazon`, `#Decart`, `#AI startup`, `#acquisition`, `#M&amp;A`

---

<a id="item-2"></a>
## [mod\_wsgi Creator Graham Dumpleton Releases Muru, an AI-Assisted Rust ASGI/WSGI Server](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, who started mod\_wsgi 20 years ago, has published Muru \(github.com/muruhq/muru\), a new Rust-based server for running both ASGI and WSGI Python applications in development and production. He documented the work as it happened in a series of roughly nineteen blog posts published between 2026-11-04 and 2026-11-22, covering everything from worker internals to HTTPS in development and a per-page debug toolbar. The project carries unusual credibility because its author spent two decades on mod\_wsgi, the long-standing Apache module for hosting WSGI apps, and much of the Python web deployment world still relies on incumbent servers such as Gunicorn and Uvicorn. If Muru matures as promised, it could offer a single, Rust-speed alternative that handles synchronous and asynchronous apps together while fitting natively into container and Kubernetes workflows. The write-ups describe design choices such as &quot;import once, fork many&quot; worker startup, running WSGI and ASGI side by side with a muru.wsgi\_to\_asgi bridge object in the WSGI environ, releases instead of restarts, canary deployments without a service mesh, scaling to zero, scheduled overlays, and tracing surfaced in a debug toolbar. Muru also ships an MCP server so AI coding agents can deploy each change as a release, test it, inspect what Muru observed on failure, and roll back — but the project is very new and has not yet seen broad independent validation.

rss · Simon Willison · Nov 21, 23:56

**Background**: WSGI \(Web Server Gateway Interface\) is the long-standing Python standard that defines how a web server hands requests to a synchronous Python application, and mod\_wsgi is the Apache module Graham Dumpleton created 20 years ago to implement it. ASGI \(Asynchronous Server Gateway Interface\) is its successor, supporting both async and sync applications as well as long-lived connections such as WebSockets. Muru is notable for being written in Rust rather than Python or C, and for being developed in tandem with AI coding agents — Dumpleton addresses that directly in a post titled &quot;AI as a lifestyle choice,&quot; noting that judging what still isn&\#x27;t good enough remains his job.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/muruhq/muru">GitHub - muruhq/ muru : Routing edge, control plane and Python...</a></li>
<li><a href="https://grahamdumpleton.me/posts/2026/11/twenty-years-of-mod-wsgi/">Twenty years of mod_wsgi, and what comes next - Graham Dumpleton</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface">Asynchronous Server Gateway Interface - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#python`, `#asgi`, `#wsgi`, `#rust`, `#web-servers`

---

<a id="item-3"></a>
## [OpenAI Chief Scientist Reportedly Calls for Industry Limits on AI Development](https://news.google.com/rss/articles/CBMiswFBVV95cUxQMjVTYVIwT3huVU8teHdXRHdnWGxOUTI5d1J6elZhWktVMVpSZDhhRmk5eV82c0JuRDBSUWNHdl84Z253WDJDbmd6SXhiNlFsdkxhM2gxWTVoTnY2ZkdrZ0dVam1OVXNSZWIwUnBQaTU4bEhJNTZValFSQ1Naam1xb1FkTklSZXI2Ums4d19sUjVheGtLNGhUWjFPcEVyd0ZIRmJlX0FqNXF5cHpCR2pjczF5WQ?oc=5) ⭐️ 7.0/10

According to Bloomberg, OpenAI&\#x27;s chief scientist has urged the AI industry to impose limits on how far development should go, publicly aligning a senior figure at the leading AI lab with the case for restraint. The report is based on a headline-level disclosure, with the full details of his remarks, the specific limits proposed and the venue not included in the available excerpt. A senior executive at OpenAI endorsing limits carries weight because the company sits at the frontier of model development, and such statements can shape how competitors, regulators and investors frame the safety-versus-speed debate. It also adds momentum to AI governance discussions at a time when policymakers in the US, EU and elsewhere are drafting rules for frontier models. The available material is only a link and headline from Bloomberg, so the concrete scope of the proposed limits — whether voluntary industry commitments, compute thresholds, pre-deployment testing or licensing — is not yet known. Readers should treat the specifics as unconfirmed until the full article or the primary remarks are available.

google\_news · Bloomberg.com · Nov 22, 19:40

**Background**: OpenAI&\#x27;s chief scientist role has been held by Jakub Pachocki since 2024, when he succeeded co-founder Ilya Sutskever, who left to start the safety-focused startup Safe Superintelligence. Debates over limiting AI development have intensified since 2023, when figures such as Elon Musk and Yoshua Bengio signed an open letter calling for a pause on training systems more powerful than GPT-4, while critics argued such pauses are impractical and merely cede ground to rivals. Frontier labs have since shifted toward a mix of voluntary commitments, internal safety frameworks referred to as &\#x27;preparedness&\#x27; or &\#x27;responsible scaling&\#x27; policies, and external testing agreements with governments.

**Tags**: `#AI governance`, `#AI safety`, `#OpenAI`, `#AI regulation`, `#industry policy`

---

<a id="item-4"></a>
## [Dev fits 367K-parameter AI language model on a floppy for 486DX and Pentium PCs](https://news.google.com/rss/articles/CBMi-wJBVV95cUxNVFdRcVJUSlZKaDM5RmpfNzBxdEtSWDJJY1VMbWlRUnM4ejVldWsxa1RDM3hKY3N3ckptR0dzdjROWks0ZWVQLS1NaGZxZjBYTmg1alc3NlNLSEQyRFhwTENTcFNlN1o2akVaQmRYM0s1LURaQ2RyWTVsdGdqbWxnZlJiMDV4ZG5zREpRR0FYZlpKRnI1T2ZTZF91V2pTZDQwWHNIZHBEVTZCMmRoOUwxSDJDUFF5bi1kTzRta0huRF91RVc5T2xMMjV5UnJqQ3cxcF9BblVVMExicVg5U09uZFR3dXpqVTAxckpTUHZiOHUwREVRRHhxMzJLc0d6Y2FVRWktQ2VucnFmd2htQ0U0NVd4UXZ4aS1xeTdaUmdpNjRfVXdnVTVaVS1uZE91VXZRMmN1MzB2LWZicTdSNEVlTlhwWXNmUkhxWXhOeTF4NXhBMjVxTXNoQWQ5Ync4MmdiSTJZbHR3Yjl6YUpTRmZZSnBBWmk3VTNsZ3RJ?oc=5) ⭐️ 7.0/10

A developer released Tiny 2.1, a question-answering transformer with only 367,000 parameters that fits on a 1.44MB floppy disk and needs just 540KB of memory to run, allowing it to execute on vintage 486DX and Pentium-era PCs. The program answers questions by speaking through the machine&\#x27;s built-in PC speaker rather than a sound card or display. The demo shows how far aggressive model compression can push inference down the hardware ladder, hinting at a future where small language models run on extremely constrained microcontrollers and embedded devices. It also serves as a playful stress test of just how little compute a working transformer actually requires. The headline numbers are a 367K-parameter network and a 540KB memory footprint, small enough to sit on a floppy image yet still perform a question-answering task. Output is limited to synthesized speech via the PC speaker, so responses are short, low-fidelity and far from a general-purpose chatbot in capability.

google\_news · Tom&\#x27;s Hardware · Nov 22, 11:00

**Background**: Transformers are neural network architectures built on multi-head attention that convert text into tokens and process them in parallel, and they underpin nearly all modern large language models. Because full-size models need gigabytes of memory, researchers use model compression techniques such as pruning, quantization and knowledge distillation to shrink them. Typical large language models have billions of parameters; 367,000 is roughly a millionth of that scale. The 486DX and Pentium are Intel CPUs from the late 1980s and early 1990s with only a few megabytes of RAM, making them a classic target for retrocomputing demos.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_%28deep_learning%29">Transformer (deep learning) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_compression">Model compression - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2105.10059v1">Model Compression - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#retrocomputing`, `#language-models`, `#model-compression`, `#edge-ai`, `#transformers`

---

<a id="item-5"></a>
## [Signal Blocks AI Agents From Reading Your Screen](https://news.google.com/rss/articles/CBMinAFBVV95cUxNOXlLaURHYWlxOG1ZWmNrRXppRUYxY1A4aG50dnFNTTZvMWNRbmRqSjZBYlpaNWdEbFpVaXAtbXlKSXpsRmlBSTRqdm0xR2IybzdBazh1QjBvVVZManNFdzFMY0JvaXRnZzlmYW5OREJseUxlTERDaFZKT0QxM0RGRU16d0dkeW5vSGtVcThQLVR0UkN4YXUtVEJWYU7SAaIBQVVfeXFMT0ViVkJhek9LWXlFM2FhVUxEYmFodlhNS2xTMG1OOG9VTndjMDJVSDhIZ1pSRW5fNU5ab3U5NVA5aEJwd2ZRbHhLa1JYYlBWRmhSVE1pcm5oV2F2cUZSUmpWdFpmMlZSM3FtQ2ZLTmctMVZhdEVpTVpVN3FyWlZYaGdEUS1YZkY0Z3NQOU1NanpkUHlXUWxIQTYwNXRIZ2xkdTVB?oc=5) ⭐️ 6.0/10

Security Affairs reports that Signal is implementing protections designed to stop AI agents from reading users&\#x27; screens, though the report provides no technical details or version information. The move appears aimed at preventing apps from using screen-reading capabilities to access content displayed in the messaging app. Signal is a widely used end-to-end encrypted messenger, so blocking screen-reading agents could reduce a new data-exposure path as AI assistants gain the ability to operate phones and inspect on-screen content. The change may affect both malicious scrapers and legitimate accessibility tools, highlighting a growing tension between AI automation and user privacy. The report does not specify how Signal detects or blocks AI agents, which platforms are affected, or whether legitimate accessibility services such as screen readers will still work. On Android, screen-reading is typically enabled through accessibility services, a powerful API that can inspect UI content and interact with apps.

google\_news · Security Affairs · Nov 22, 18:33

**Background**: Android accessibility services are intended to help users with disabilities by reading screen content, providing switch access, or enabling voice control. Because these services can inspect and act on other apps&\#x27; interfaces, they have also been abused by malware and automation tools to scrape sensitive information. Screen-capture protection is a broader mobile security control that tries to prevent unauthorized recording or reading of displayed content, though it must be balanced against accessibility needs.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.android.com/guide/topics/ui/accessibility/service">Create an accessibility service | Android Developers</a></li>
<li><a href="https://attack.mitre.org/techniques/T1513/">Screen Capture, Technique T1513 - Mobile | MITRE ATT&amp;CK®</a></li>
<li><a href="https://mobilerasp.net/controls/screen-overlay-and-capture-protection.html">Screen Overlay and Capture Protection - Mobile RASP</a></li>

</ul>
</details>

**Tags**: `#Signal`, `#privacy`, `#AI agents`, `#screen security`, `#mobile security`

---

<a id="item-6"></a>
## [Nvidia Chip Sales Reportedly Targeted in California Criminal Probe](https://news.google.com/rss/articles/CBMilgFBVV95cUxQdXBFZ3kwbUFveDNEMENUZnc4RUxCaXRNUHhxVDN5anE3cVZNRUJkT2pJTWQxVFBVRWdtTUNsSDI5S2xXOUhXM092QWRJZEtFUkduMnVjR01XdGY1NnB6bUJ2RlBoQ3pMM2ZRSTdNbl9WbDJTQmIxTXpEQ2FkMlNBRlNVZ3FMQVlXR25KOTlpdGdSNlJnOXc?oc=5) ⭐️ 6.0/10

PYMNTS.com reports that Nvidia&\#x27;s chip sales are the target of a criminal probe in California, but the available item provides only a headline and link with no further details. The report matters because Nvidia is a central supplier of AI accelerators and GPUs, so even a preliminary legal inquiry could draw regulatory and investor attention to its sales practices and supply chain. The report does not identify the investigating agency, the scope of the probe, any specific allegations, or whether charges have been filed, so the claim should be treated as unconfirmed until primary sources or Nvidia comment emerges.

google\_news · PYMNTS.com · Nov 22, 22:46

**Background**: Nvidia designs GPUs and AI accelerators that are widely used in data centers, gaming, and AI model training. A criminal probe is generally conducted by prosecutors or law enforcement and can concern alleged violations of laws such as export controls, fraud, or antitrust, depending on the facts. California is home to major technology companies and has both state and federal law enforcement presence, but the headline alone does not establish which authority is involved.

**Tags**: `#Nvidia`, `#semiconductor industry`, `#legal investigation`, `#AI hardware`, `#California`

---

<a id="item-7"></a>
## [South Korea&\#x27;s education minister resigns amid national AI cheating panic](https://news.google.com/rss/articles/CBMiVkFVX3lxTE84anQya1hDT2RteTRMN2gtc3dPZTJWczZnY2RJTkx1Q1FCY215RG5IZno2Rm9fZ1g2aURROHYtMFdBSEhOZW1MWUpBVkI3eXZHTW5IaFd3?oc=5) ⭐️ 6.0/10

South Korea&\#x27;s education minister has resigned after the country was swept by nationwide alarm over students using generative AI tools to cheat in schoolwork and exams. The resignation turns what began as a classroom integrity problem into a full-blown political and policy crisis at the top of the education ministry. A single country losing its top education official to an AI-cheating scandal shows that generative AI is now a governance problem, not just a technology one, and it will likely accelerate moves toward AI-detection rules, assessment reform, and restrictions on AI tools in schools. Other governments and exam boards weighing similar policies will be watching South Korea as an early test case. The reporting available is headline-level and does not specify the minister&\#x27;s name, the exact date of the resignation, or which specific incidents triggered the panic, so the precise mechanisms of the cheating and any announced policy responses remain unconfirmed. What is clear is that the pressure came from a broad public and parental reaction rather than from a single isolated case.

google\_news · Ynetnews · Nov 22, 17:31

**Background**: Generative AI chatbots such as those built on large language models can produce essays, solve math problems, and answer exam questions on demand, which makes traditional homework and take-home assessments very hard to trust. South Korea is one of the world&\#x27;s most intensely education-focused societies, with heavy reliance on high-stakes exams and a large private tutoring market, so any perceived threat to fair assessment quickly becomes a national issue. Many education systems are still debating whether to ban such tools, detect their use, or redesign assessments around them.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theedadvocate.org/the-ai-cheating-crisis-top-tools-colleges-are-using-to-fight-back/">The AI Cheating Crisis: Top Tools Colleges Are Using to Fight ...</a></li>
<li><a href="https://www.gse.harvard.edu/ideas/usable-knowledge/26/10/ai-cheating-crisis-schools-isnt-only-what-you-think">The AI Cheating Crisis in Schools Isn’t (Only) What You Think</a></li>
<li><a href="https://www.researchgate.net/publication/374034239_Keyword_analysis_of_Artificial_Intelligence_Education_policy_in_South_Korea">Keyword Analysis of Artificial Intelligence Education Policy ...</a></li>

</ul>
</details>

**Tags**: `#AI cheating`, `#education policy`, `#South Korea`, `#academic integrity`, `#generative AI`

---

<a id="item-8"></a>
## [Chinese open-weight AI models push into the U.S. market](https://news.google.com/rss/articles/CBMilAFBVV95cUxPaFFzWWZEcm1aRGpHRDRxRDBUbTBQVkFDRDZxOW91MDB4U3RNTGJrVkZhcElVWHJhR096Z0JvdmpZMjBkV215T2JtZzY5ZjREeXZfUDIteV9KcnRCZ2NrQllNdzJ0ODFFaGtNUkRDbzU1R2l3VDFpSW0xTDB2MEcxekEzT0E3TjdnZms0aTFNU1dsUEhv?oc=5) ⭐️ 6.0/10

Asia Times reports that Chinese developers of open-weight AI models are increasingly targeting the American market, turning freely downloadable model weights into a competitive push against U.S. AI vendors. The piece frames this as a market-entry story rather than a single product launch, describing how Chinese labs are gaining traction with U.S. developers and businesses. Because open-weight models can be downloaded, self-hosted and fine-tuned without paying per-token API fees, they give U.S. startups and enterprises a low-cost alternative to closed American frontier models, pressuring pricing and market share at the application layer. This also turns model distribution into a geopolitical issue, as Washington weighs whether broadly licensed Chinese models should face the same scrutiny as Chinese hardware and software. The key distinction is between open-weight models, which publish trained parameters that anyone can download, run and fine-tune, and truly open-source AI, which also releases training data and code; many popular Chinese releases fall into the former category and carry license terms that can restrict commercial use, redistribution or use above certain scale. The Asia Times analysis focuses on market dynamics and competitive pressure rather than benchmark comparisons, so it does not establish how these models perform against leading U.S. systems.

google\_news · Asia Times · Nov 22, 03:42

**Background**: Open-weight models are AI systems whose trained parameters are published for download, letting developers run them on their own hardware — even offline — and adapt them to specific tasks. This differs from closed models such as those offered only through vendor APIs, where usage is metered and the underlying weights stay private. The open-weight approach has become a major competitive lever for Chinese AI labs, since it lets them spread adoption quickly among developers outside China even when they lack the cloud distribution and enterprise sales channels of U.S. providers. Regulators and companies are still sorting out how licenses, data provenance and national-security concerns apply to models that can be freely redistributed across borders.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnet.com/tech/services-and-software/what-are-open-weight-ai-models/">What Are Open - Weight AI Models ? - CNET</a></li>
<li><a href="https://chainofthought.show/ai-decoded/open-weight-vs-open-source-ai/">Open - Weight vs . Open - Source AI Models — Chain of Thought</a></li>
<li><a href="https://bestllmfor.com/guides/open-weight-vs-open-source-llm/">Open - Weight vs Open - Source LLMs: What You Can Do | BestLLMfor</a></li>

</ul>
</details>

**Tags**: `#AI models`, `#open-weight`, `#China`, `#market competition`, `#geopolitics`

---