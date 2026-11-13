---
layout: default
title: "Horizon Summary: 2026-11-13 (EN)"
date: 2026-11-13 23:04:15 +0000
lang: en
report: default
---

> From 181 items, 7 important content pieces were selected

---

1. [Shanghai Releases Findings on Fatal Gene-Editing Case at Jiao Tong Medical School](#item-1) ⭐️ 8.0/10
2. [DeepSeek Opens Full-Suite Application API with Search, File and Voice Tools](#item-2) ⭐️ 8.0/10
3. [Python Early Contributor Tim Peters Dies at 74](#item-3) ⭐️ 7.0/10
4. [Microsoft Outlook, Teams and Copilot hit by 12-hour global outage](#item-4) ⭐️ 7.0/10
5. [OpenAI Launches ChatGPT Wallet With Amex, Mastercard and Visa](#item-5) ⭐️ 7.0/10
6. [Claude Code 2.1.323 adds experimental Code Mode for JavaScript tool calls](#item-6) ⭐️ 6.0/10
7. [Moonshot AI Restructures, Retiring Cayman Holdco to Pave Way for Hong Kong IPO](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Shanghai Releases Findings on Fatal Gene-Editing Case at Jiao Tong Medical School](https://mp.weixin.qq.com/s/p0iC3tcI1yr10EBl2NjUvg) ⭐️ 8.0/10

Shanghai authorities have concluded their investigation into a fatal experimental gene-editing treatment at Shanghai Jiao Tong University School of Medicine, finding deficiencies in preclinical research, ethics review and informed consent, plus about 1.06 million yuan improperly received by some personnel from the patient&\#x27;s family. The child, diagnosed with the rare Snijders Blok-Campeau syndrome, was injected in March 2025 and died of thrombotic microangiopathy; researchers Qiu and Yang were dismissed and barred from relevant qualifications for five years, and the involved institutions were ordered to rectify and face administrative penalties. The case is one of the most serious bioethics and scientific-integrity incidents in Chinese biomedical research since the 2018 He Jiankui affair, and the official findings set a benchmark for how personalized, &quot;n-of-1&quot; gene-editing therapies will be reviewed and policed. It signals tighter scrutiny of ethics committees, informed consent for desperate families, and institutional accountability at university-affiliated hospitals. The investigation found shortcomings across three fronts — preclinical evidence, ethics review and informed consent — and also uncovered financial misconduct, with roughly 1.06 million yuan received from the family. Notably, the case&\#x27;s paper was published in Nature in February 2026, after the patient&\#x27;s March 2025 death, raising further questions about publication and peer-review safeguards; the two named researchers received five-year disqualification rather than criminal referral as reported.

telegram · zaihuapd · Nov 13, 09:24

**Background**: Snijders Blok-Campeau syndrome is a rare autosomal dominant neurodevelopmental disorder caused by mutations in the CHD3 gene, characterized by impaired intellectual development, macrocephaly and speech difficulties, and it typically arises from de novo mutations. Thrombotic microangiopathy, the reported cause of death, is a pathology in which endothelial injury triggers thrombosis in capillaries and arterioles, producing thrombocytopenia, anemia and kidney failure; it can be caused by drug toxicities and is a known severe risk in experimental systemic therapies. Gene editing for such ultra-rare diseases is sometimes pursued as a bespoke, single-patient therapy, which challenges conventional trial design and ethics oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Snijders_Blok-Campeau_syndrome">Snijders Blok-Campeau syndrome</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thrombotic_microangiopathy">Thrombotic microangiopathy</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5266569/">Thrombotic microangiopathies: a general approach to diagnosis ...</a></li>

</ul>
</details>

**Tags**: `#gene editing`, `#bioethics`, `#clinical research regulation`, `#scientific misconduct`, `#China`

---

<a id="item-2"></a>
## [DeepSeek Opens Full-Suite Application API with Search, File and Voice Tools](https://mp.weixin.qq.com/s/78KBHc4-4N5b2vfL9SkutQ) ⭐️ 8.0/10

DeepSeek has opened a full-suite application API: developers simply toggle the relevant parameters in existing API calls to gain deep-thinking search, file input, link reading and voice conversation capabilities, with the server handling tool invocation and context stitching automatically. The V4.1-Flash model is already supported across three endpoints, and Search, Fetch, OCR, ASR and TTS can each be called individually, while DeepSeek also open-sourced a frontend demo that can import historical conversations. This shifts a large amount of plumbing — web search orchestration, document parsing, OCR, speech recognition and synthesis — from the developer to the API provider, so teams can build retrieval-augmented or multimodal assistants without stitching together multiple vendors. Together with the open-source chat-demo frontend, it effectively lets anyone self-host a DeepSeek web-style product on top of the API. Each capability is exposed as a standalone endpoint, so developers can call Search, Fetch, OCR, ASR or TTS directly and mix them into their own pipelines instead of using the bundled conversation mode. The company also published deepseek-ai/chat-demo with a hosted demo at deepseek-ai.github.io, though the announcement itself gives no pricing, rate-limit or latency details for the new tool-enabled mode.

telegram · zaihuapd · Nov 13, 14:27

**Background**: Large language models cannot natively reach real-time data or external systems, so modern APIs use tool calling \(function calling\): the application passes a set of tool definitions, the model decides when to call one, and the returned results are appended back into the conversation context — a loop usually called context stitching. DeepSeek is now offering this loop as a managed service, wrapping search, page fetching, OCR \(optical character recognition\), ASR \(automatic speech recognition\) and TTS \(text-to-speech\) behind its own endpoints, so the developer only sends a request and gets a finished answer.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek - V 4 . 1 - Flash : smarter, faster, more efficient.</a></li>
<li><a href="https://openrouter.ai/zh-CN/deepseek/deepseek-v4.1-flash">DeepSeek V 4 . 1 Flash - API 定价与基准测试 | OpenRouter</a></li>
<li><a href="https://juejin.cn/post/7571808096937181225">LLM 工具调用（Tool Calling）技术详解：原理、实践与关键问题解析LLM...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#API`, `#multimodal`, `#AI tools`, `#open source`

---

<a id="item-3"></a>
## [Python Early Contributor Tim Peters Dies at 74](https://x.com/Itsfoss/status/2120957452937998716) ⭐️ 7.0/10

Python creator Guido van Rossum announced that Tim Peters, one of Python&\#x27;s earliest and most influential contributors, passed away at the age of 74. Peters was Python&\#x27;s second real user, the author of the Timsort sorting algorithm, the writer of PEP 20 \(The Zen of Python\), and served 13 years on the Python Software Foundation board. Peters was a foundational figure whose work quietly underpins everyday Python: Timsort remains the default sorting algorithm behind sorted\(\) and list.sort\(\), and the Zen of Python still shapes how the language&\#x27;s design philosophy is taught. His death closes a chapter in Python&\#x27;s early history and is a significant loss for the global open-source community. Timsort, implemented by Peters in 2002 for Python, is a hybrid stable algorithm derived from merge sort and insertion sort that performs well on real-world data and was later adopted by Java 7 for object sorting. PEP 20 deliberately lists only 19 aphorisms, leaving the 20th slot open &quot;for Guido to fill in&quot;, a vacancy that has never been filled.

telegram · zaihuapd · Nov 13, 09:55

**Background**: Python is one of the world&\#x27;s most widely used programming languages, and its design decisions are documented through PEPs \(Python Enhancement Proposals\), the community&\#x27;s formal process for proposing and recording changes. Timsort is the sorting algorithm Python uses by default whenever you call sorted\(\) or list.sort\(\), chosen because it handles partially ordered real-world data efficiently. The Zen of Python is a set of short aphorisms such as &quot;Beautiful is better than ugly&quot; and &quot;Explicit is better than implicit&quot; that is famously readable by typing &quot;import this&quot; into a Python interpreter.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Timsort">Timsort - Wikipedia</a></li>
<li><a href="https://peps.python.org/pep-0020/">PEP 20 – The Zen of Python | peps.python.org</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zen_of_Python">Zen of Python - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Python`, `#open-source-community`, `#obituary`, `#Timsort`, `#PEP 20`

---

<a id="item-4"></a>
## [Microsoft Outlook, Teams and Copilot hit by 12-hour global outage](https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/) ⭐️ 7.0/10

On November 13, Microsoft Outlook, Teams and Copilot remained down in an outage lasting more than 12 hours that disrupted communications for businesses and governments worldwide. Microsoft attributed the incident to a server-side problem, said it found no evidence of malicious activity, and reported that it had widened the remediation effort and was seeing signs of recovery. Outlook and Teams are default communication infrastructure for a large share of enterprises and public agencies, so a multi-hour global outage cascades into missed deals, delayed government services and manual workarounds. It is the second Microsoft 365 disruption this year and renews scrutiny of the reliability and single-vendor risk of cloud productivity suites. Impact was concrete: parts of the Australian, Japanese and U.S. governments were affected, Euronext&\#x27;s email was disrupted, and some financial institutions in Taiwan fell back to fax to confirm trades. Microsoft has not published a root-cause analysis, and its statement describes only a server-side issue with no indication of a cyberattack.

telegram · zaihuapd · Nov 13, 12:21

**Background**: Microsoft 365 bundles Outlook \(email and calendar\), Teams \(chat and meetings\) and Copilot, the AI assistant that Microsoft has woven into these apps to draft text, summarize meetings and search work content. These are cloud services, so customers do not run them locally and cannot fail over to their own hardware when Microsoft&\#x27;s servers break. Cloud providers normally rely on high-availability clusters and failover mechanisms to shift traffic to healthy nodes automatically, which is exactly the machinery that appeared not to work fast enough here.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/Microsoft_Copilot">Microsoft Copilot - 维基百科，自由的百科全书</a></li>
<li><a href="https://dingstore.cn/contents/wiki/high-availability-cluster-overview/">邮箱百科： 什 么 是 高 可 用 集群 · Ding店—阿里钉钉旗下企业 服 务 平台</a></li>
<li><a href="https://juejin.cn/post/7003177066870882318">Nginx 挂了怎 么 办？ 怎 么 实现 高 可 用 ？ Hi...</a></li>

</ul>
</details>

**Tags**: `#Microsoft 365`, `#服务宕机`, `#Outlook`, `#Teams`, `#云服务可靠性`

---

<a id="item-5"></a>
## [OpenAI Launches ChatGPT Wallet With Amex, Mastercard and Visa](https://openai.com/index/introducing-chatgpt-wallet/) ⭐️ 7.0/10

OpenAI announced ChatGPT Wallet, a payment feature that lets AI agents inside ChatGPT complete purchases without ever handling the user&\#x27;s real card number, built in partnership with American Express, Mastercard and Visa. Starting today it is available in the US to ChatGPT Pro subscribers aged 18 and over through OpenAI&\#x27;s dots agents, and requires a US-issued card. This is one of the first mainstream deployments of agentic commerce by a major AI platform, turning chatbots from recommendation engines into actual buyers and pulling the three largest US card networks into the agent economy. If it works, it sets a template for how AI agents will transact on behalf of users across the web, and pressures rival assistants and merchants to support similar agent-driven checkout flows. Each purchase requires the user to review the item and amount and confirm with Face ID or a fingerprint, and the payment network issues a token that stands in for the real card number. The rollout is limited to US Pro subscribers on US-issued cards, and OpenAI says agents operate within users&\#x27; existing card protections rather than bypassing them.

telegram · zaihuapd · Nov 13, 15:43

**Background**: Payment tokenization replaces the 16-digit primary account number on a card with an algorithmically generated token that is only valid within a defined scope, so a merchant or agent never stores the real credential — the same idea behind Apple Pay and virtual card numbers. Agentic commerce extends this to AI agents that browse, select and buy on a user&\#x27;s behalf, using tokenized credentials scoped to a single transaction plus consent records showing the shopper approved the purchase. OpenAI&\#x27;s dots are its agents that can act across apps and services, and ChatGPT Wallet is the payment rail built for them.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-wallet/">Introducing ChatGPT Wallet | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/11/13/openai-chatgpt-wallet-dot-purchases.html">OpenAI &#x27;s ChatGPT Wallet allows &#x27; dots &#x27; AI agents to make purchases</a></li>
<li><a href="https://www.bigcommerce.com/articles/ecommerce/agentic-commerce/">Agentic Commerce : A New, AI -Powered Way to Buy and Sell</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tokenization_%28data_security%29">Tokenization (data security) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI agents`, `#agentic commerce`, `#payments`, `#fintech`

---

<a id="item-6"></a>
## [Claude Code 2.1.323 adds experimental Code Mode for JavaScript tool calls](https://code.claude.com/docs/en/changelog) ⭐️ 6.0/10

Claude Code released version 2.1.323 on November 12, adding an experimental &quot;Code Mode&quot; that lets Claude invoke tools by writing JavaScript rather than through the usual structured tool-call interface, with organizations able to turn the feature off. The same release tightened plugin management so that plugins whose declared version ranges do not match are no longer installed or updated, and \`plugin validate\` now performs type checking on TypeScript hooks. If Code Mode proves reliable, coding agents could chain many tool calls inside a single generated script instead of making dozens of sequential round trips, which would cut latency and token overhead on complex multi-step tasks. Because it is gated as experimental and can be disabled per organization, enterprises get a chance to evaluate the new interaction model before it becomes a default part of Claude Code&\#x27;s tooling contract. The feature is explicitly experimental and organization-controllable, and the release also bundles smaller changes such as .docx document upload support and a 30-second hook heartbeat. The plugin changes mean a plugin declaring a version range that the installed version falls outside will silently be skipped for install or update, so authors need to keep their version constraints accurate.

telegram · zaihuapd · Nov 13, 03:47

**Background**: Claude Code is Anthropic&\#x27;s agentic coding tool that runs in the terminal and IDE, reading files, editing code and executing commands on the developer&\#x27;s behalf. Tools in this model are discrete capabilities the model invokes through a structured call format, and hooks are user- or plugin-defined scripts that fire at lifecycle events such as before or after an edit. Code Mode changes the middle layer: instead of emitting one tool call at a time, Claude writes a short JavaScript program that calls the tools itself, an approach popularized by other agent frameworks to reduce per-call overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI coding agent and assistant</a></li>
<li><a href="https://www.datacamp.com/tutorial/claude-code">Claude Code Tutorial: Setup and Refactoring in Practice | DataCamp</a></li>
<li><a href="https://github.com/Siigari/claude-heartbeat">GitHub - Siigari/ claude - heartbeat : Keep Claude Code alive and...</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI coding agents`, `#developer tools`, `#plugin management`, `#experimental features`

---

<a id="item-7"></a>
## [Moonshot AI Restructures, Retiring Cayman Holdco to Pave Way for Hong Kong IPO](https://www.wsj.com/tech/chinas-moonshot-ai-restructures-to-pave-way-for-ipo-49f09abb) ⭐️ 6.0/10

Chinese AI startup Moonshot AI is completing a corporate restructuring in preparation for an initial public offering in Hong Kong, according to people familiar with the matter cited by The Wall Street Journal. As part of the move, its Cayman Islands holding company will be retired and the shares held by early USD investors will be transferred to the company&\#x27;s main onshore operating entity in China. The change signals that a leading Chinese AI lab is abandoning the classic offshore holding structure that Chinese tech companies long used to raise dollar capital and list in the US, opting instead for an onshore entity plus a Hong Kong listing. If it succeeds, it could become a template for other Chinese AI startups weighing how to give foreign and domestic investors liquidity amid tightening cross-border capital rules. The report is based on unnamed sources and Moonshot AI has not publicly confirmed the restructuring or disclosed a timetable or valuation for any listing. Moving early dollar-investor shares into a domestic operating entity can carry tax, foreign-exchange and regulatory complications, which is likely why the process is described as a multi-step restructuring rather than a simple redomiciliation.

telegram · zaihuapd · Nov 13, 11:29

**Background**: For decades, Chinese companies seeking overseas capital set up holding companies in the Cayman Islands, which offers a familiar legal system, tax neutrality and a well-understood path to listings on exchanges such as Nasdaq and the Hong Kong Stock Exchange. That offshore layer lets foreign investors hold shares in a non-mainland entity while the actual business and licenses stay in China, often through contractual arrangements. Moonshot AI, founded in Beijing in March 2023 by Yang Zhilin and Tsinghua classmates, is the company behind the Kimi model family and chatbot. A Hong Kong IPO would give its investors an exit route that does not depend on a US listing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cayman_Islands">Cayman Islands - Wikipedia</a></li>
<li><a href="https://nextomoro.com/moonshot-ai/">Moonshot AI | nextomoro | AI Research Lab Intelligence</a></li>
<li><a href="https://tracxn.com/d/companies/moonshot-ai/__wZzU6o3CAntBLbB5MXh7XINvgyVvzhQb4DNTaMgBTp4">Moonshot AI - 2026 Company Profile, Team, Funding... - Tracxn</a></li>

</ul>
</details>

**Tags**: `#Moonshot AI`, `#China AI`, `#IPO`, `#corporate restructuring`, `#industry news`

---