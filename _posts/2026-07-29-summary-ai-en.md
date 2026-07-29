---
layout: default
title: "Horizon Summary: 2026-07-29 (EN)"
date: 2026-07-29
lang: en
report: ai
---

> From 334 items, 10 important content pieces were selected

---

1. [Google Disbands Nobel-Winning AlphaFold Team, Focuses on Gemini](#item-1) ⭐️ 9.0/10
2. [AI Worm Self-Replicates Through Microsoft Word Copilot](#item-2) ⭐️ 8.0/10
3. [Claude Mythos finds cryptographic weaknesses in HAWK and AES](#item-3) ⭐️ 8.0/10
4. [Agentic AI Accountability: Who Is Responsible?](#item-4) ⭐️ 8.0/10
5. [Microsoft Azure reaches $100B annual revenue](#item-5) ⭐️ 8.0/10
6. [MCP v5 Overhaul: Stateless Architecture for Serverless AI](#item-6) ⭐️ 8.0/10
7. [Amazon Halts Nova Model Development, Pivots to Athena Platform](#item-7) ⭐️ 8.0/10
8. [ChatGPT blocks mimicking living authors&\#x27; styles](#item-8) ⭐️ 8.0/10
9. [1,100+ AI Employees Urge US to Slow Down; Altman Backs](#item-9) ⭐️ 8.0/10
10. [Apple Credits Claude and Codex in Security Update](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google Disbands Nobel-Winning AlphaFold Team, Focuses on Gemini](https://www.aibase.com/news/29980) ⭐️ 9.0/10

Google DeepMind has quietly disbanded the Nobel Prize-winning AlphaFold team, reassigning key researchers including original paper authors to other projects, shifting focus towards the Gemini AI model. This strategic pivot from a landmark scientific achievement to a generative AI project may slow progress in computational biology and raises concerns about the sustainability of breakthrough research teams in corporate settings. AlphaFold, developed by Demis Hassabis and John Jumper, won the 2024 Nobel Prize in Chemistry for predicting protein structures; most original authors have been reassigned over the past year, effectively breaking up the team.

aibase · AIbase · Jul 29, 16:06

**Background**: AlphaFold is an AI system that accurately predicts protein 3D structures from amino acid sequences, solving a grand challenge in biology. It has been widely adopted in drug discovery and molecular biology. Gemini is Google&\#x27;s multimodal AI model designed to compete with OpenAI&\#x27;s GPT-4 and other large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AlphaFold`, `#Google DeepMind`, `#Gemini`, `#AI research team restructuring`, `#Nobel Prize`

---

<a id="item-2"></a>
## [AI Worm Self-Replicates Through Microsoft Word Copilot](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 8.0/10

Security researcher Håkon Måløy discovered a new prompt injection attack that turns Microsoft Word&\#x27;s Copilot into a self-replicating worm, where hidden instructions in a document cause Copilot to propagate the attack to other documents. This attack demonstrates a new class of security risk for AI-assisted productivity tools, potentially allowing attackers to spread malware across organizations simply by sharing infected documents. The attack uses hidden white-on-white text that includes instructions for Copilot to manipulate the current document and copy the hidden instructions into new documents, enabling self-replication without the original document. It was responsibly disclosed to Microsoft over 144 days ago, but no full mitigation exists yet.

rss · Simon Willison · Jul 29, 18:43

**Background**: Prompt injection is a security exploit where malicious input causes a large language model \(LLM\) to ignore its intended instructions and follow the attacker&\#x27;s commands. In this variant, the attacker embeds hidden prompts in a document; when Copilot processes that document, it may execute those prompts, leading to unintended actions. The concept of self-replicating AI worms has been previously demonstrated in email assistants \(e.g., Morris II\), but this is the first such attack targeting a word processor&\#x27;s AI assistant.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html">Researchers Build Self - Replicating AI Worm That Operates Entirely...</a></li>

</ul>
</details>

**Tags**: `#prompt injection`, `#security`, `#AI`, `#Microsoft Word`, `#self-replicating worm`

---

<a id="item-3"></a>
## [Claude Mythos finds cryptographic weaknesses in HAWK and AES](https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything) ⭐️ 8.0/10

Anthropic researchers used Claude Mythos, a powerful LLM, to discover mathematical weaknesses in the HAWK cryptographic scheme and a reduced-round version of AES-128. The model worked semi-autonomously for 60 hours on HAWK and generated a billion tokens over three days for AES, with human prompting to encourage persistence. This demonstrates AI&\#x27;s potential to assist in cryptographic research, though the weaknesses found have no practical impact on current systems. The study highlights that careful prompt engineering can coax LLMs into solving hard problems, opening new avenues for AI-assisted mathematical discovery. The total estimated API cost for the experiments was ~$100,000. The researchers also created a new evaluation benchmark, CryptanalysisBench, in collaboration with ETH Zurich, Tel Aviv University, and University of Haifa, described in a paper on arXiv.

rss · Simon Willison · Jul 28, 22:45

**Background**: Claude Mythos is Anthropic&\#x27;s most powerful LLM, designed for advanced research tasks but not publicly released due to safety concerns. HAWK is a cryptographic protocol used in blockchain contexts; reduced-round AES refers to studying AES with fewer than the standard 10 rounds to understand attack techniques. Cryptanalysis involves finding weaknesses in cryptographic algorithms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hash_%28cryptography%29">Hash (cryptography)</a></li>
<li><a href="https://www.ai-jarvis.eu/anthropics-mythos-found-flaws-aes-and-hawk-cryptography-100000-attack">Anthropic&#x27;s Mythos Found Flaws in AES and HAWK Cryptography ...</a></li>
<li><a href="https://www.geeksforgeeks.org/computer-networks/advanced-encryption-standard-aes/">Advanced Encryption Standard ( AES ) - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#AI research`, `#prompt engineering`, `#security`, `#Claude`

---

<a id="item-4"></a>
## [Agentic AI Accountability: Who Is Responsible?](https://news.google.com/rss/articles/CBMiakFVX3lxTFBlVnBhYnNPYjVqX0pnSTRwdThUYXJQUnZsZ0ZuRnlDZHRIS1piWl9fTU1oS0xBeGR2dU56X2FMYVhpbG1RQkZzY1ZRLXRzNzhpSk5MTms1aW5CV05BUVRIeWVTbmVqTVhBbXc?oc=5) ⭐️ 8.0/10

An article published by Communications of the ACM examines the critical question of accountability in agentic AI systems, which autonomously pursue goals over multiple steps without per-step human approval. As agentic AI becomes more prevalent in decision-making roles, establishing clear accountability frameworks is essential for trust, safety, and regulatory compliance. Agentic AI differs from single-turn AI by its autonomous, multi-step goal pursuit, introducing unique challenges for assigning responsibility when errors or unintended actions occur.

google\_news · Communications of the ACM · Jul 29, 20:30

**Background**: Agentic AI refers to systems that can autonomously plan, use tools, and take actions to accomplish goals without needing human approval for each step. This capability is distinct from traditional AI models that respond to individual prompts. Accountability frameworks, such as the NIST AI Risk Management Framework, are emerging to address risks and ensure ethical AI practices.

<details><summary>References</summary>
<ul>
<li><a href="https://free.ai/glossary/agentic-ai/?lang=lv">What is Agentic AI ? | Free. ai</a></li>
<li><a href="https://verifywise.ai/lexicon/model-accountability-frameworks">Model accountability frameworks - VerifyWise AI Lexicon</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#agentic AI`, `#accountability`, `#AI governance`

---

<a id="item-5"></a>
## [Microsoft Azure reaches $100B annual revenue](https://news.google.com/rss/articles/CBMitwFBVV95cUxPQ3gtNkFkdUk3ck5PdGZTVkI0eHhGTk56UkZWZzhqdzE5RWl4cVF2UjFJb19pTGFkYkdQWEFyRWZzcDF0aThvMnYxRk1nQWMwYVFCZEJNSXFkZFZ3NlBzS3BoeHFva2UtSXd4cENYUGo0V0hPdjJzYWhSamFJRDMzQkpLMm5FM2NIYVNkXzFaWl9pZmY1ZGlmWTNuWXdwang0Z2xnWTBzMHdrWGVCTGpLR3haZzhVcTQ?oc=5) ⭐️ 8.0/10

Microsoft Azure&\#x27;s annual revenue surpassed $100 billion for the first time, driven by record AI spending that impacted cash flow. This milestone underscores Azure&\#x27;s dominance in cloud computing and the massive scale of AI infrastructure investment, signaling that AI workloads are becoming a primary growth driver for cloud providers. The revenue milestone was reported alongside a 31.6% profit jump, but increased AI spending \(e.g., on data centers\) reduced cash flow. Azure&\#x27;s growth is heavily tied to enterprise adoption of AI services like OpenAI models hosted on its platform.

google\_news · GeekWire · Jul 29, 20:51

**Background**: Azure is Microsoft&\#x27;s cloud computing platform, competing with Amazon Web Services and Google Cloud. AI workloads require significant computational resources, driving demand for cloud infrastructure. Microsoft has invested heavily in OpenAI and integrated its models into Azure, fueling growth but also requiring large capital expenditures.

**Tags**: `#Microsoft Azure`, `#cloud computing`, `#AI infrastructure`, `#financial performance`

---

<a id="item-6"></a>
## [MCP v5 Overhaul: Stateless Architecture for Serverless AI](https://www.aibase.com/news/29983) ⭐️ 8.0/10

Anthropic released version 5 of the Model Context Protocol \(MCP\), shifting from a stateful, persistent-connection model to a fully stateless architecture, eliminating the need for persistent connections and reengineering the communication mechanism. This overhaul significantly improves scalability and suitability for serverless deployments, enabling AI applications to integrate tools and data more flexibly without maintaining ongoing connections. It marks a major evolution in how AI models interact with external systems, potentially accelerating adoption across cloud and edge environments. The stateless redesign means each request is self-contained, eliminating the complexity of connection management. However, this may require reimplementation of existing MCP clients and servers. The protocol remains open-source and is adopted by major AI providers like OpenAI and Google DeepMind.

aibase · AIbase · Jul 29, 18:06

**Background**: MCP is an open standard introduced by Anthropic in November 2024 to standardize how AI applications \(like LLMs\) connect to external data sources and tools, often described as a &\#x27;USB-C port for AI&\#x27;. Previous versions relied on persistent connections for context sharing, which limited scalability in serverless environments. This v5 update addresses that limitation by adopting a stateless model.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://docs.anthropic.com/en/docs/mcp">Model Context Protocol ( MCP ) - Anthropic</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#protocol`, `#Anthropic`, `#stateless architecture`, `#AI`

---

<a id="item-7"></a>
## [Amazon Halts Nova Model Development, Pivots to Athena Platform](https://www.aibase.com/news/29978) ⭐️ 8.0/10

Amazon has halted active development of most Nova models, including flagship models and video/image generators, shifting resources to integrate third-party models via its Athena platform. This strategic pivot indicates challenges in competing with leading proprietary models and underscores Amazon&\#x27;s bet on infrastructure and model integration as a key differentiator in the AI market. Existing Nova models will remain in maintenance mode for current customers; the AGI division and related labs have been disbanded. Amazon Athena is being repurposed as a unified platform to aggregate cutting-edge third-party models.

aibase · AIbase · Jul 29, 15:06

**Background**: Amazon Nova is a family of foundation models introduced in late 2025, covering text, image, and video generation. Amazon Athena is traditionally a serverless interactive query service for analyzing data in S3; the new direction repurposes it for model integration, leveraging AWS&\#x27;s infrastructure strengths.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/nova/">Amazon Nova foundation models – frontier intelligence and industry leading price-performance</a></li>
<li><a href="https://www.aboutamazon.com/news/aws/aws-agentic-ai-amazon-bedrock-nova-models">Meet new Amazon Nova AI models that help build ...</a></li>
<li><a href="https://aws.amazon.com/athena/">Interactive SQL - Serverless Query Service - Amazon Athena - AWS</a></li>

</ul>
</details>

**Tags**: `#AI strategy`, `#Amazon`, `#Nova models`, `#infrastructure`, `#model integration`

---

<a id="item-8"></a>
## [ChatGPT blocks mimicking living authors&\#x27; styles](https://www.aibase.com/news/29973) ⭐️ 8.0/10

OpenAI silently updated ChatGPT to refuse requests that mimic the distinct style of living authors, such as copying openings or stylistic traits, to reduce copyright risks. This policy change affects many users who rely on style imitation for creative projects, and highlights growing legal pressures around AI-generated content and copyright. The restriction is already active and applies only to living authors; it does not block mimicking the style of public domain or deceased authors. The change was made silently without a public announcement.

aibase · AIbase · Jul 29, 15:06

**Background**: Text style transfer involves modifying the linguistic style of a text while preserving its core content, and large language models like ChatGPT can perform this via prompting. However, replicating a living author&\#x27;s distinctive style raises copyright concerns because the model may have been trained on that author&\#x27;s works without explicit permission. OpenAI&\#x27;s new restriction aims to mitigate legal risks by refusing such direct style imitation requests.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/07/chatgpt-stops-cloning-famous-writers-voices-but-may-capture-a-similar-feeling/">ChatGPT starts blocking direct requests to copy an author&#x27;s style</a></li>
<li><a href="https://arxiv.org/abs/2406.05885">[2406.05885] Are Large Language Models Actually Good at Text Style Transfer?</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#OpenAI`, `#copyright`, `#AI policy`, `#writing style`

---

<a id="item-9"></a>
## [1,100+ AI Employees Urge US to Slow Down; Altman Backs](https://www.aibase.com/news/29972) ⭐️ 8.0/10

Over 1,100 employees from leading AI firms including OpenAI, Anthropic, Google, and Meta signed an open letter called &\#x27;Steering the Frontier,&\#x27; urging the U.S. government to support international cooperation and develop AI governance tools, even calling for a deliberate slowdown if necessary. OpenAI CEO Sam Altman rarely publicly backed the initiative, along with Anthropic&\#x27;s CEO and co-founders. This unprecedented show of industry consensus from AI employees, with rare backing from a top CEO like Altman, signals a growing urgency for regulation and safety measures. It could pressure policymakers to act and shape the global debate on responsible AI development. The open letter, part of the &\#x27;Steering the Frontier&\#x27; initiative, explicitly calls for international governance tools and a potential slowdown in AI progress. The list of signatories includes employees from multiple major AI firms, highlighting broad internal concern about AI risks.

aibase · AIbase · Jul 29, 14:06

**Background**: AI safety has been a growing concern, with previous open letters from experts calling for pauses in development. Frontier AI refers to the most advanced and powerful AI systems, which pose potential risks if not properly aligned with human values. &\#x27;Steering the Frontier&\#x27; is a new initiative focused on ensuring these systems are developed safely and with proper governance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alpha-matica.com/post/pillar-3-alignment-and-control-steering-frontier-ai-toward-human-intent-in-an-accelerating-world">Pillar 3: Alignment and Control – Steering Frontier AI Toward Human...</a></li>
<li><a href="https://www.techtarget.com/searchenterpriseai/tip/The-best-AI-governance-tools-and-platforms">The best AI governance tools and platforms in 2026 | TechTarget</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#Regulation`, `#OpenAI`, `#Anthropic`, `#Policy`

---

<a id="item-10"></a>
## [Apple Credits Claude and Codex in Security Update](https://www.aibase.com/news/29970) ⭐️ 8.0/10

Apple has credited AI models from Anthropic, OpenAI, and NVIDIA in its first security update that acknowledges AI contributions. Specifically, Claude, Codex Security, and NVIDIA&\#x27;s AI red team helped uncover multiple vulnerabilities. This marks a significant milestone in the integration of AI into cybersecurity, as one of the largest tech companies officially recognizes AI&\#x27;s role in vulnerability discovery. It could encourage wider adoption of AI-powered security testing across the industry. The vulnerabilities were fixed in Apple&\#x27;s system update, and the AI tools used include Anthropic&\#x27;s Claude, OpenAI&\#x27;s Codex Security \(released in March 2026\), and NVIDIA&\#x27;s AI red teaming tools. This is the first time Apple has publicly credited AI in a security advisory.

aibase · AIbase · Jul 29, 12:06

**Background**: AI models are increasingly used in cybersecurity for tasks like code review and vulnerability detection. Claude is a large language model developed by Anthropic, while Codex Security is an AI-powered application security agent by OpenAI that scans GitHub repositories for issues. NVIDIA&\#x27;s AI red team uses machine learning to simulate attacks and find weaknesses. Apple&\#x27;s recognition highlights the growing trend of incorporating AI into security workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://github.com/openai/codex-security">GitHub - openai / codex - security : SDKs and CLI for Codex Security</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#Apple`, `#vulnerability detection`, `#Claude`, `#Codex`

---