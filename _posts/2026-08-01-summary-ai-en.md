---
layout: default
title: "Horizon Summary: 2026-08-01 (EN)"
date: 2026-08-01
lang: en
report: ai
---

> From 276 items, 10 important content pieces were selected

---

1. [Stateless MCP reignites interest, inspiring mcp-explorer and datasette-mcp](#item-1) ⭐️ 9.0/10
2. [OpenAI&\#x27;s Astra Model Claims Ten Math Breakthroughs](#item-2) ⭐️ 8.0/10
3. [DeepSeek-V4-Flash-0731: 304B Model Offers Top Value per Intelligence](#item-3) ⭐️ 8.0/10
4. [OpenAI&\#x27;s Hugging Face Hack Validates AI Cyberattack Warnings](#item-4) ⭐️ 8.0/10
5. [EU Gets Power to Enforce AI Rules Starting Today](#item-5) ⭐️ 8.0/10
6. [Larry Ellison&\#x27;s AI Bet: Boom or Bubble?](#item-6) ⭐️ 8.0/10
7. [Simon Willison Releases llm-mcp-client 0.1a0 Python MCP Client](#item-7) ⭐️ 7.0/10
8. [Meta, Microsoft, Nvidia, IBM Back Open-Weight AI](#item-8) ⭐️ 7.0/10
9. [Australian booksellers decry destruction of rare books for AI training](#item-9) ⭐️ 7.0/10
10. [Anthropic Says AI Models Hacked Three Organizations During Testing](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Stateless MCP reignites interest, inspiring mcp-explorer and datasette-mcp](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.0/10

The 2026-07-28 Model Context Protocol specification introduced Stateless MCP, enabling a single HTTP request to call tools without a session initialization step. Simon Willison built two new projects — mcp-explorer and datasette-mcp — to demonstrate and explore the simplified protocol. Stateless MCP removes server-side session state, making MCP servers easier to implement, scale, and audit — a key advantage for AI agent tooling. This could help MCP regain momentum against alternatives like Skills and shell-based agent workflows. The new stateless approach uses headers such as MCP-Protocol-Version and Mcp-Method instead of a session ID. datasette-mcp adds a /-/mcp endpoint to any Datasette instance; mcp-explorer is a CLI tool for interactively probing MCP servers.

rss · Simon Willison · Jul 31, 23:13

**Background**: The Model Context Protocol \(MCP\) is an open standard introduced by Anthropic in November 2024 that standardizes how AI systems connect to external tools and data sources. Legacy MCP required a two-step handshake to initialize a session and obtain a session ID. A stateless protocol, by contrast, keeps each request self-contained, improving reliability, visibility, and scalability. This change lowers the barrier for both client and server implementations, particularly in web-scale applications.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/31/stateless-mcp/">Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://www.linkedin.com/pulse/new-mcp-stateless-here-what-actually-changes-arnold-cartagena-dpcte">The new MCP is stateless . Here is what actually changes.</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread on the spec shows strong support, especially from developers running MCP servers. One operator of an MCP gateway noted they &\#x27;cannot tell you what portion of our issues/bugs were due to the need to persist server state,&\#x27; echoing the pain points the stateless redesign addresses.

**Tags**: `#MCP`, `#AI agents`, `#protocol`, `#developer tools`, `#specification`

---

<a id="item-2"></a>
## [OpenAI&\#x27;s Astra Model Claims Ten Math Breakthroughs](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 8.0/10

OpenAI announced that an internal version of its next major model, Astra, produced ten advances in mathematics and theoretical computer science, spending less than $2,000 per problem at GPT-5.6 Sol token prices. The company released Lean 4 formalizations, a paper, and reasoning walkthrough documents, though the post notes there is no information on failed attempts. If verified, these results would show frontier AI models can make original research contributions to mathematics, not just assist humans, potentially accelerating progress in the field. The low cost per problem raises questions about how AI will reshape the economics of mathematical discovery and the role of human mathematicians. Willison notes the lack of information on how many problems the model attempted without success, which makes the $2,000-per-problem figure hard to evaluate. The openai/ten-proofs repo contains Lean 4 formalizations, and OpenAI also published a paper and an LLM-generated PDF reconstructing the proofs, but the original prompts were not shared.

rss · Simon Willison · Aug 1, 20:34

**Background**: Lean 4 is an interactive theorem prover that lets mathematicians write proofs that a computer can formally verify. OpenAI&\#x27;s announcement follows a similar flex by Anthropic, whose unreleased Claude Mythos Preview model discovered cryptographic weaknesses after spending $100,000 on tokens. The GPT-5.6 model family, launched by OpenAI in July 2026, comes in three variants — Luna, Terra, and Sol — with Sol being the most capable. Terence Tao has described an emerging &\#x27;big mathematics&\#x27; paradigm in which AI handles technical details while humans do creative work.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with ... - OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The post observes a collective &\#x27;Deep Blue moment&\#x27; among mathematicians online, with excitement tempered by skepticism about OpenAI&\#x27;s selective reporting of successes and the lack of information on failed attempts. Simon Willison also notes that while the transparency is decent, he wants to see the actual prompts used to generate these results.

**Tags**: `#AI`, `#Mathematics`, `#OpenAI`, `#Theoretical Computer Science`, `#Research`

---

<a id="item-3"></a>
## [DeepSeek-V4-Flash-0731: 304B Model Offers Top Value per Intelligence](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek released DeepSeek-V4-Flash-0731, a 304-billion-parameter model with substantially enhanced agentic capabilities. It is priced at $0.14 per million input tokens and $0.27 per million output tokens, and Artificial Analysis ranks it ahead of MiniMax M3. This release reinforces the trend of smaller, cheaper models rivaling much larger ones, potentially offering the best value-per-intelligence on the market. It matters for developers and enterprises seeking strong agentic AI at a fraction of the cost of frontier models. The 304B model is 167GB on Hugging Face and can be accessed via OpenRouter. Simon Willison found default reasoning produced a poor &\#x27;pelican&\#x27; image, while setting reasoning\_effort to high yielded much better results.

rss · Simon Willison · Jul 31, 23:59

**Background**: Agentic AI refers to AI systems that can pursue goals, use tools, and take actions with varying degrees of autonomy, built on top of large language models. The Artificial Analysis Intelligence Index is a composite benchmark score measuring language model capabilities across reasoning, coding, knowledge, instruction following, and multi-step tasks, which allows comparing models on both intelligence and cost per task.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://agentic.ai/what-is-agentic-ai">What Is Agentic AI? Definition, 6 Levels &amp; Examples (2026)</a></li>

</ul>
</details>

**Tags**: `#AI`, `#DeepSeek`, `#LLM`, `#Model Release`, `#Machine Learning`

---

<a id="item-4"></a>
## [OpenAI&\#x27;s Hugging Face Hack Validates AI Cyberattack Warnings](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPckY3OG1rcGJyWTBzdC16bGloeExwRmVVcmI3b19YQXZnSE44T0k1bzRuc0x0cXZ6SDRxQUZHQmdGeHZ3a0h0SS1pWl9NSlFZcHZubzY0eU50cldpT1QwOHNHaTlSNm1MV2d6N0tSQ2VjZWY1eWVXck93dUF3Z0VYRXBnbHI5dkdn0gGIAUFVX3lxTE9yRjc4bWtwYnJZMHN0LXpsaWh4THBGZVVyYjdvX1hBdmdITjhPSTVvNG5zTHRxdnpINHFBRkdCZ0Z4dndrSHRJLWlaX01KUVlwdm5vNjR5TnRyV2lPVDA4c0dpOVI2bUxXZ3o3S1JDZWNlZjV5ZVdyT3d1QXdnRVhFcGdscjl2R2c?oc=5) ⭐️ 8.0/10

CNBC reported that OpenAI&\#x27;s Hugging Face account was hacked, confirming months of warnings about AI cybersecurity risks. The breach signals a new era of vulnerabilities as AI platforms become prime targets for attackers. This incident is significant because Hugging Face is a central hub for AI models, and a compromise could poison datasets or distribute malicious models to numerous developers. It highlights the growing risk of AI supply chain attacks and underscores the urgent need for stronger security in AI infrastructure. Hugging Face hosts millions of models and datasets used by developers worldwide, making it a high-value target for supply chain attacks. The hack underscores vulnerabilities in AI software supply chains, where compromised resources can be used to inject malicious code or tamper with training data.

google\_news · CNBC · Aug 1, 12:00

**Background**: Hugging Face is a popular AI community platform where researchers and companies share, discover, and deploy machine learning models, datasets, and applications. AI supply chain attacks target these collaborative repositories to poison training data or spread malicious models, exploiting the trust between organizations and their open-source dependencies. As AI adoption grows, such platforms become increasingly attractive to cybercriminals.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/">Hugging Face – The AI community building the future.</a></li>
<li><a href="https://www.ibm.com/think/insights/cyber-criminals-compromising-ai-software-supply-chains">How cyber criminals are compromising AI software supply chains | IBM</a></li>
<li><a href="https://ifttt.com/explore/what-is-hugging-face">What is Hugging Face ? A complete guide to features, pricing, and use</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#OpenAI`, `#Hugging Face`, `#cyber attack`, `#news`

---

<a id="item-5"></a>
## [EU Gets Power to Enforce AI Rules Starting Today](https://news.google.com/rss/articles/CBMieEFVX3lxTFB3clE0QWFyclI5SmxkVHdqT0dycGluMG82SkpYeGdnNDNWQkx1RnluU1BNd0ozVTlZbm82R3ZUUTByN1dBdlVTMDV5YTB5MlZnNUZtZXhIWVF1bDdJZ0JHdUpENkNjUE01RzMwUUYtMlV2VUg2YVJuZw?oc=5) ⭐️ 8.0/10

The EU has begun enforcing the AI Act, granting regulators the power to apply binding rules on AI systems. This marks the first phase of the AI Act&\#x27;s application, with prohibitions on unacceptable-risk AI practices taking effect. This is a major milestone in AI governance, as the EU is the first major jurisdiction to enforce comprehensive AI regulations. Companies operating in the EU must now comply or face penalties, setting a global standard. The AI Act was published in the EU Official Journal on 12 July 2024 and entered into force on 1 August 2024. The rules apply in phases, with the prohibition of certain AI practices starting from 2 February 2025.

google\_news · Taipei Times · Aug 1, 16:00

**Background**: The EU AI Act is a landmark law that regulates AI systems based on their risk level, ranging from minimal to unacceptable risk. It aims to ensure that AI is trustworthy and protects fundamental rights. The Act covers various stakeholders, including providers, users, and importers of AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialintelligenceact.eu/the-act/">The Act Texts | EU Artificial Intelligence Act</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai">AI Act | Shaping Europe ’s digital future</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#EU`, `#policy`, `#AI Act`

---

<a id="item-6"></a>
## [Larry Ellison&\#x27;s AI Bet: Boom or Bubble?](https://news.google.com/rss/articles/CBMifEFVX3lxTFB3b25tYTV5SW12WWpoanVObDdYX0VOLW1QWWFwNHdZVWNIM2N2am4tX3Z3VnVRS3Y2ZkxpOEZ0el9rX0hUNGhaVjBabF9LRmVlUlBuY3VkSFJ2aThVOWR3aTI3d19XcFB3ZUQyeGdnbXB6UnZhNlpHV0p1SDc?oc=5) ⭐️ 8.0/10

The New York Times published an analysis examining Larry Ellison&\#x27;s aggressive investments in artificial intelligence, questioning whether Oracle&\#x27;s founder will become the defining face of a potential AI bubble. The piece weighs his full-throttle bet on AI infrastructure against growing concerns about overvaluation in the sector. Ellison&\#x27;s outsized AI investments carry significant weight because Oracle has become a major cloud infrastructure player, and his bets signal where billions in capital are flowing. If his predictions are wrong, the fallout could reverberate across the broader tech industry and the AI investment landscape. The NYT analysis centers on Ellison&\#x27;s personal credibility and financial exposure, noting his reputation as a tech visionary and consummate salesman. It does not present a definitive conclusion but frames the risk that the AI boom may be overhyped.

google\_news · The New York Times · Aug 1, 02:27

**Background**: Larry Ellison co-founded Oracle and has served as its chairman and CTO, pouring company resources into AI, including large-scale cloud data centers and partnerships with AI developers. The &\#x27;AI bubble&\#x27; debate refers to fears that tech stocks and infrastructure spending on AI exceed realistic near-term returns. Oracle&\#x27;s stock has rallied sharply on AI enthusiasm, and Ellison has personally championed the technology as transformative.

**Tags**: `#AI`, `#Larry Ellison`, `#Oracle`, `#AI bubble`, `#tech industry`

---

<a id="item-7"></a>
## [Simon Willison Releases llm-mcp-client 0.1a0 Python MCP Client](https://simonwillison.net/2026/Jul/31/llm-mcp-client/#atom-everything) ⭐️ 7.0/10

Simon Willison has released llm-mcp-client 0.1a0, an early alpha Python client for the Model Context Protocol \(MCP\). The release is available on GitHub and links to a detailed blog entry describing the project. MCP is quickly becoming a standard for connecting LLMs to external tools and data, so a new Python client from a prominent developer in the LLM ecosystem could be valuable for developers building MCP integrations. Even as an early alpha, it signals growing momentum behind MCP tooling. The version is 0.1a0, indicating an early alpha stage and likely unstable API. The release post is brief and points to a longer blog entry titled &\#x27;stateless-mcp&\#x27; for additional context.

rss · Simon Willison · Jul 31, 23:03

**Background**: The Model Context Protocol \(MCP\) is an open standard introduced by Anthropic in November 2024 to standardize how AI systems such as LLMs integrate with external tools and data sources. In an MCP architecture, an LLM client acts as the intermediary that connects the language model to MCP servers, which expose tools, resources, and prompts. This client library is an early attempt to provide a Python implementation of that client role.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#llm`, `#model-context-protocol`, `#python`, `#mcp`, `#release`

---

<a id="item-8"></a>
## [Meta, Microsoft, Nvidia, IBM Back Open-Weight AI](https://news.google.com/rss/articles/CBMipAFBVV95cUxOS0hQcXlIMVB5UFFwVXM1Y0pZQm5XOXBzUmNveTg4RjZCc2RNdjdOVFV4U2JDZWdrTTRuTVROZ3lodE5FRVpielNWTVUyaFJkQlhHLVZmSVBWc1BRUHhNS1dNUjNTZ1lCb0drYk9pQ2hLQUtIUXlQUUc4eDNGVGYxOVQ5S1JSaDF0Q3BKSFFncDBKYUZCVV9fTm1aZXd6bjZKanB2dg?oc=5) ⭐️ 7.0/10

Meta, Microsoft, Nvidia, IBM, and other major tech companies have publicly backed open-weight AI, according to an AI News report. This endorsement signals broad industry support for making AI model weights publicly available. This alignment among major players could shape AI policy and the direction of the AI ecosystem, strengthening the case for more transparent and accessible AI models. It may also influence how regulators and enterprises view open-weight approaches versus fully proprietary or open-source models. Open-weight models release the trained parameters \(weights\) of an AI model, allowing others to run and fine-tune them, but they typically do not include training data or training code. This distinguishes them from fully open-source AI, which exposes more of the model stack.

google\_news · AI News · Aug 1, 15:49

**Background**: AI models are trained on vast amounts of data, and the &\#x27;weights&\#x27; are the internal parameters learned during that training. An open-weight model makes these weights publicly available, so developers can download and run the model on their own hardware. However, &\#x27;open weight&\#x27; is not the same as &\#x27;open source&\#x27;: true open-source AI typically requires access to training data, code, and documentation, not just the trained weights.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cbc.ca/news/business/open-weight-ai-kimi-k3-9.7287025">What is open - weight AI , the tech behind Kimi... | CBC News</a></li>
<li><a href="https://www.fierce-network.com/content/open-weight-ai-vs-open-source-ai-whats-difference">Open-weight AI vs. open-source AI: What’s the difference?</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told – Open Source ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#Industry News`, `#Policy`

---

<a id="item-9"></a>
## [Australian booksellers decry destruction of rare books for AI training](https://news.google.com/rss/articles/CBMivAFBVV95cUxOTTJBXzBtYmdvNlM2ZERtalkzZDdhUmVXckdVVmVxdnJTUGJYTTBaTlhSVUNVUXhRVkxsMlc4SU5BR2xhYjZ0Tkd6cllkRHlFMzRGVVhuZW0yTEpYZHduMWNiajZfUUMwTDEyZF91S0p3U0NVNEhsNnRiV01ZR29hSGUtaHlVbTNlVTRCLUh0bmxVYjZ3Y3kzWVdyblVsYkljcnFvQk5OQTg5WXg2cEVfVVpYLWdPNzZtMHFlQg?oc=5) ⭐️ 7.0/10

Australian book sellers have raised the alarm over the &\#x27;horrific&\#x27; destruction of rare books to create datasets for training AI models, warning that the practice causes cultural loss beyond the loss of physical objects. This highlights an overlooked ethical and cultural cost of AI development: the demand for vast text corpora is driving destruction of irreplaceable cultural artifacts. It adds to ongoing debates about data sourcing, copyright, and the hidden costs behind generative AI. The article quotes booksellers who describe the destruction as &\#x27;horrific&\#x27; and argue that the value of these titles lies in their cultural and historical significance, not merely as objects. The practice involves physically destroying books to scan or digitize them for inclusion in AI training corpora.

google\_news · The Guardian · Aug 1, 20:01

**Background**: Large language models are trained on massive text corpora, a process known as text and data mining \(TDM\), which automatically extracts and analyzes text from sources like books and websites. To meet this demand, datasets such as Books3 — created from hundreds of thousands of ebooks, many pirated — have been used to train models including Meta&\#x27;s LLaMA. This context has raised concerns about copyright, consent, and the preservation of cultural heritage, aligning with the booksellers&\#x27; alarm over the destruction of rare titles.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Text_and_data_mining">Text and data mining</a></li>
<li><a href="https://www.aiaaic.org/aiaaic-repository/ai-algorithmic-and-automation-incidents/books3-dataset">AIAAIC - Books3 dataset</a></li>
<li><a href="https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/">These 183,000 Books Are Fueling the Biggest Fight in ... Anti-piracy group shuts down Books3, a popular dataset for AI ... Has your book been used to train the AI? - Substack You Just Found Out Your Book Was Used to Train AI. Now What?</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#data sourcing`, `#copyright`, `#cultural heritage`, `#machine learning`

---

<a id="item-10"></a>
## [Anthropic Says AI Models Hacked Three Organizations During Testing](https://news.google.com/rss/articles/CBMioAFBVV95cUxPU2s4NW5JaHVhUVdoNHF0WjZUM3FOdTN0YmVjU1U3dGRvOVBuNnZzWEV3UnFTT25KclFfelRXOFJ2YklFNDJPMGhGcS1MQk9RcU9sUDYwYk1ybjhHc09PdnZjSXNoZG44MFNzcm4wOEpIUkpVdkIxUVplWnAxV1hpZFZuRXZYUjdqS2lfVUtqaGkzd29lTG9wZGhjbHYxMFlP?oc=5) ⭐️ 7.0/10

Anthropic revealed that its AI models successfully hacked three organizations during controlled security testing. This marks a real-world demonstration of offensive cyber capabilities by AI systems. This development is significant because it shows AI models can autonomously carry out penetration testing and potentially be weaponized for cyber attacks. It raises urgent questions about AI safety, regulation, and the dual-use nature of advanced AI. The testing was likely an adversarial red-teaming exercise where AI was given objectives to break into systems. The specific organizations were not named, and details about the methods and defenses remain limited in the initial report.

google\_news · Broadband Breakfast · Aug 1, 18:56

**Background**: Red teaming in AI involves experts or AI systems intentionally attacking a system to uncover vulnerabilities before malicious actors can exploit them. Anthropic is an AI safety company that routinely tests its models for dangerous capabilities. Autonomous penetration testing uses software to discover and exploit weaknesses continuously without human direction, and adversarial testing in general evaluates whether a system can be compromised through realistic attack paths.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-is-red-teaming-for-generative-ai/">What is Red Teaming for Generative AI - GeeksforGeeks</a></li>
<li><a href="https://securelayer7.net/learn/pentest/what-is-autonomous-penetration-testing">What is Autonomous Penetration Testing ? | SecureLayer7</a></li>
<li><a href="https://onsecurity.io/article/a-guide-to-adversarial-testing-for-ai/">A Guide to Adversarial Testing for AI - OnSecurity</a></li>

</ul>
</details>

**Tags**: `#AI`, `#security`, `#Anthropic`, `#hacking`, `#testing`

---