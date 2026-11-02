---
layout: default
title: "Horizon Summary: 2026-11-02 (EN)"
date: 2026-11-02 23:04:11 +0000
lang: en
report: ai
---

> From 189 items, 10 important content pieces were selected

---

1. [Marvell to Acquire Lumentum in $115 Billion AI-Driven Merger](#item-1) ⭐️ 8.0/10
2. [OpenAI, Google, Microsoft and Anthropic Back Unified AI Crawler Opt-Out Token in robots.txt](#item-2) ⭐️ 8.0/10
3. [Meituan LongCat Releases LongCat-2.5, a 1.6T-Parameter Native Multimodal Model](#item-3) ⭐️ 8.0/10
4. [Tesla Optimus Adopts End-to-End Vision Model Derived From FSD](#item-4) ⭐️ 7.0/10
5. [DeepSeek open-sources MIT-licensed Super-agent prototype that finds its own work](#item-5) ⭐️ 7.0/10
6. [Census AI Survey Conflicts With &\#x27;Super Intelligence&\#x27; Renaming Order](#item-6) ⭐️ 6.0/10
7. [OpenAI Publicly Backs Amicus Briefs Defending Fair Use for AI Training](#item-7) ⭐️ 6.0/10
8. [Medicare&\#x27;s AI-assisted coverage review pilot hit early snags, documents show](#item-8) ⭐️ 6.0/10
9. [NYT Report Examines Anthropic&\#x27;s Scramble for AI Compute](#item-9) ⭐️ 6.0/10
10. [OpenAI and Microsoft Amicus Briefs Diverge in AI Copyright Case](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Marvell to Acquire Lumentum in $115 Billion AI-Driven Merger](https://news.google.com/rss/articles/CBMikwFBVV95cUxNUXZSWEtYd1FlQVdoMVZqY0YwcjVvMi1hTC15TXdyVGxJUVdWM3o5eHRXQkFDdTF6bVM4cUdZdGppbl9iVExpYlpnRG9reWN2RmZWSkphU2lSN3lfbjRvWDJRY0ZESXU1SkxTSkFlTzM3VVlaYldVRkk0enB2ZHZCSG9YSjM0bHRiUDJzTmdnZXJRS0E?oc=5) ⭐️ 8.0/10

Marvell Technology announced it will acquire optical-components maker Lumentum in a deal valued at $115 billion, a transaction The New York Times framed as driven by the AI boom. The merger combines Marvell&\#x27;s custom AI silicon and electro-optics business with Lumentum&\#x27;s datacom transceivers and optical component portfolio. The deal would create a much larger vertically integrated supplier of the optical and silicon plumbing that hyperscalers need to wire together AI training clusters, at a moment when interconnect bandwidth has become a primary bottleneck for scaling. It signals consolidation in the AI hardware supply chain and could reshape competitive dynamics for Broadcom, Coherent and other players in data-center optics. The $115 billion figure makes this one of the largest semiconductor deals ever attempted, and Nvidia had reportedly invested $2 billion each in Marvell and Lumentum earlier in the year, underlining how central optics has become to AI systems. The available report is headline-level, so financing structure, regulatory approval paths and antitrust scrutiny are not yet detailed.

google\_news · The New York Times · Nov 2, 18:48

**Background**: Marvell is a semiconductor company that designs custom accelerators \(ASICs\), networking silicon and electro-optics for cloud and data-center customers, and data-center revenue now makes up the bulk of its sales. Lumentum makes datacom transceivers and photonic components that convert electrical signals into light so servers and switches can communicate over fiber. As AI clusters grow to tens of thousands of GPUs, copper links hit distance and power limits, pushing designs toward optical interconnects — which is why optical component makers have become strategic acquisition targets.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/02/marvell-to-buy-lumentum-in-115-billion-deal-in-ai-data-center-bet-.html">Marvell to buy Lumentum in $115 billion deal in AI data - center bet</a></li>
<li><a href="https://www.lumentum.com/en/products/data-center/datacom-transceivers">Datacom Transceivers | Lumentum</a></li>
<li><a href="https://www.marvell.com/blogs/copper-and-optical-interconnects-in-ai-cluster.html">A Deep Dive into the Copper and Optical Interconnects Weaving ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#semiconductors`, `#M&amp;A`, `#Marvell`, `#Lumentum`

---

<a id="item-2"></a>
## [OpenAI, Google, Microsoft and Anthropic Back Unified AI Crawler Opt-Out Token in robots.txt](https://www.aibase.com/news/32011) ⭐️ 8.0/10

On November 1 it was reported that OpenAI, Google, Microsoft and Anthropic will jointly honor a new mechanism that lets site owners declare in a single place in their existing robots.txt that they refuse AI crawling, rather than negotiating with each company separately. The proposal, submitted to the IETF by Anthropic standards lead Kevin Kelley, defines a shared &quot;policy token&quot; — \`\_\_usage\_ai-training\` — that websites can use to signal that their content must not be used for AI training. Until now, opting out of AI scraping meant editing robots.txt rules per crawler or striking individual licensing deals, which favored large publishers with legal resources. A common signal endorsed by the four biggest model developers could become the default compliance baseline for AI data governance, shaping content licensing markets and exposing crawlers that ignore the declaration. The mechanism is documented as an IETF draft \(draft-kelley-aipref-training-preference-signal\), with the token vocabulary aligned to work underway in the IETF aipref working group; like all robots.txt directives, it is a request that crawlers must voluntarily obey and has no technical enforcement. Meta was notably not among the companies named as honoring the signal at the time of reporting, and the document is a draft rather than a finalized standard.

aibase · AIbase · Nov 2, 12:01

**Background**: robots.txt is a plain-text file at a site&\#x27;s root that has long told search engine crawlers which pages they may fetch, but it was designed for indexing, not for AI training, and it does not itself enforce anything — reputable crawlers simply choose to comply. The IETF is the volunteer standards body behind the core internet protocols such as TCP/IP, and it publishes drafts before anything becomes a formal standard, so a submission there is a step toward broad, interoperable adoption rather than an immediate rule. The aipref working group exists specifically to define machine-readable vocabulary for expressing content-usage preferences to AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out">The biggest names in AI are backing a new way to opt out ... | The Verge</a></li>
<li><a href="https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/">draft- kelley -aipref-training-preference-signal-00 - Machine-Readable...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Robots.txt">robots.txt - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI crawling`, `#robots.txt`, `#IETF`, `#web standards`, `#content opt-out`

---

<a id="item-3"></a>
## [Meituan LongCat Releases LongCat-2.5, a 1.6T-Parameter Native Multimodal Model](https://www.aibase.com/news/32006) ⭐️ 8.0/10

Meituan&\#x27;s LongCat team released LongCat-2.5 on November 2, a native multimodal model with 1.6 trillion total parameters and roughly 48 billion activated per token. It builds on LongCat-2.0 with stronger native visual understanding and agentic coding, and an online demo and API are available now, with weights promised for GitHub and HuggingFace. At 1.6 trillion parameters, LongCat-2.5 is one of the largest models released by a Chinese internet company, and its explicit targeting of long-horizon agent tasks signals a shift from chatbot-style assistants toward models designed to plan and execute multi-step workflows. The combination of an immediately usable API and a promise of open weights makes it relevant both to developers building agents and to the broader open-model ecosystem. The model encodes visual signals as multi-level discrete tokens so images and text are processed under a unified next-token prediction objective, using the LongCat-Next semantic alignment encoder together with residual quantization to retain fine-grained visual detail. The roughly 48B activated parameters per token imply a sparse mixture-of-experts architecture, and the weights were not yet live on GitHub or HuggingFace at the time of the announcement.

aibase · AIbase · Nov 2, 11:01

**Background**: Native multimodal models differ from earlier approaches that bolted a vision encoder onto a text-only LLM: instead, all modalities are converted into discrete tokens and fed into a single autoregressive backbone, so images are handled much like words. Meituan&\#x27;s LongCat-Next work introduced the Semantic-and-Aligned Encoder \(SAE\) paired with Residual Vector Quantization \(RVQ\), which produces hierarchical visual tokens that keep both high-level semantics and low-level detail. Long-horizon agent tasks refer to goals that require dozens or hundreds of sequential reasoning steps and tool calls, where errors can accumulate across the trajectory — a much harder test than single-turn question answering.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.27538">[2603.27538] LongCat-Next: Lexicalizing Modalities as ... LongCat-Next： LongCat-Next: Native Multimodal LLM - emergentmind.com LongCat-Next open-sourced: text, image, sound as tokens LongCat-Next: An Innovative Approach Integrating Modalities ...</a></li>
<li><a href="https://github.com/meituan-longcat/LongCat-Next">GitHub - meituan-longcat/LongCat-Next · GitHub</a></li>
<li><a href="https://www.ai21.com/glossary/ai-agent/what-are-long-horizon-tasks/">What are Long-Horizon Tasks? - AI21</a></li>

</ul>
</details>

**Tags**: `#multimodal LLM`, `#large language models`, `#agentic AI`, `#model release`, `#Meituan LongCat`

---

<a id="item-4"></a>
## [Tesla Optimus Adopts End-to-End Vision Model Derived From FSD](https://www.aibase.com/news/32017) ⭐️ 7.0/10

Tesla&\#x27;s Optimus humanoid robot reportedly now runs an end-to-end vision large model derived from the company&\#x27;s Full Self-Driving \(FSD\) stack, replacing previously hard-coded modular pipelines so that neural networks directly handle autonomous decision-making and limb control. The report claims this significantly improves the robot&\#x27;s adaptability in complex physical environments and brings its movement smoothness close to that of real humans. If accurate, this marks a meaningful architectural shift for Optimus from hand-engineered modular control to learned end-to-end policies, a direction Tesla has already pursued in autonomous driving and can now potentially reuse across its robot program. Success here would matter well beyond Tesla, since generalization and smooth whole-body motion remain the biggest bottlenecks for the entire humanoid robot industry. The report is brief and offers no technical specifics such as model size, training data volume, compute hardware, inference latency, or independent verification, and the claim of human-level movement smoothness is not quantified. A key caveat of end-to-end learned control is that it is harder to debug, interpret, and certify for safety than a modular pipeline with explicit perception, planning and control stages.

aibase · AIbase · Nov 2, 16:01

**Background**: Tesla&\#x27;s FSD is a vision-only autonomous driving system that, according to Tesla&\#x27;s own disclosures at ICCV 2025, has evolved into a multimodal large-model system whose inputs include video, navigation, vehicle state and audio, with outputs covering 3D occupancy and driving decisions. In robotics, a traditional modular pipeline splits perception, planning and control into separate hand-coded stages, whereas end-to-end learning trains a single neural network that maps sensor input directly to actions. Optimus is Tesla&\#x27;s humanoid robot program, and this report suggests the company is porting its FSD neural-network approach from cars to a bipedal platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.eeworld.com.cn/news/qcdz/eic711819.html">Tesla FSD V14 architecture and multimodal large model system ...</a></li>
<li><a href="https://www.linkedin.com/posts/knowgraph-ai_the-great-debate-in-autonomous-driving-end-to-end-activity-7461361198383566848-OZdH">End - to - End vs Modular Systems in Autonomous Driving | LinkedIn</a></li>
<li><a href="https://www.notateslaapp.com/news/2362/inside-teslas-fsd-patent-explains-how-fsd-works">Inside Tesla’s FSD: Patent Explains How FSD Works</a></li>

</ul>
</details>

**Tags**: `#humanoid robots`, `#Tesla Optimus`, `#end-to-end learning`, `#vision models`, `#robotics`

---

<a id="item-5"></a>
## [DeepSeek open-sources MIT-licensed Super-agent prototype that finds its own work](https://www.aibase.com/news/32016) ⭐️ 7.0/10

DeepSeek Harness published a technical article on Super-agent design and open-sourced an MIT-licensed research prototype called dsh-superagent-prototype. In internal deployments, the system&\#x27;s agent instances autonomously pick up work such as bug replication and code review, detecting bugs without being given explicit task prompts. Most agent frameworks today assume a human hands out each task, so shifting coordination into the agent system itself points toward agents that continuously monitor, triage and act on their own. If the pattern holds up, it could reshape how engineering teams handle routine maintenance work like bug triage and review, and it adds another concrete open-source contribution from DeepSeek to the fast-moving agent-infrastructure race. The architecture reportedly combines a Router, session-isolated Workers, event routing, persistent state, execution environments and a Watchdog component, with isolation used to keep each agent session&\#x27;s context and tool results from leaking into another. The team frames humans, not models, as the real bottleneck to multitasking, and stresses that this is a research prototype rather than a product.

aibase · AIbase · Nov 2, 15:01

**Background**: DeepSeek Harness is DeepSeek&\#x27;s open-source framework, released as a developer preview in August, that lets AI models use tools and carry out tasks through a modular, plug-in-based architecture. In agent terminology, a &quot;super-agent&quot; refers to a system that orchestrates many sub-agents rather than a single model answering one prompt, and session isolation is the practice of keeping each user&\#x27;s or task&\#x27;s conversation state separate when infrastructure is shared. The prototype builds on these ideas so that agents can notice work on their own instead of waiting for assignments.

<details><summary>References</summary>
<ul>
<li><a href="https://kingy.ai/blog/deepseek-super-agent-design-explained/">DeepSeek Super - agent Design Explained: Architecture and Results</a></li>
<li><a href="https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/007-architecture.md">dsh- superagent -prototype/docs/007- architecture .md at main...</a></li>
<li><a href="https://www.globaltimes.cn/page/202611/1373392.shtml">DeepSeek unveils ‘ Super - agent ’ design to handle... - Global Times</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#DeepSeek`, `#open-source`, `#code review`, `#research prototype`

---

<a id="item-6"></a>
## [Census AI Survey Conflicts With &\#x27;Super Intelligence&\#x27; Renaming Order](https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/) ⭐️ 6.0/10

Simon Willison re-ran the U.S. Census Bureau&\#x27;s Business Trends and Outlook Survey AI-adoption numbers using the October 22, 2026 release, producing an updated firm-size chart and noting that the Bureau now appears to conflict with Executive Order 14434. The order, signed September 29, 2026, directs federal agencies to replace &\#x27;AI&\#x27; with &\#x27;Super Intelligence&\#x27; \(SI\), while the Census survey still measures &\#x27;AI&\#x27; use. The mismatch highlights how a sweeping federal naming mandate can collide with statistical series that depend on stable terminology, potentially complicating public understanding and cross-agency data comparability. It also matters because the Census BTOS is widely cited by investors and analysts tracking AI adoption, so confusion around definitions or data continuity can distort the narrative about U.S. corporate AI uptake. The BTOS surveys 200,000 of 1.2 million businesses every two weeks, and the Census changed the question in November 2025 from AI used in producing goods or services to AI used in any business function, so the two series are explicitly not comparable. Willison&\#x27;s updated chart shows 40.7% for firms with 250+ employees versus 21.1% for 5–9 employees, but the published excerpt cuts off before he explains the full consequences of the Census Bureau&\#x27;s conflict with EO 14434.

rss · Simon Willison · Nov 2, 13:31

**Background**: The U.S. Census Bureau&\#x27;s Business Trends and Outlook Survey \(BTOS\) is a high-frequency, nationally representative survey that tracks business conditions, including AI use, every two weeks. In September 2025, Apollo Global Management published a chart based on BTOS data suggesting AI adoption was slowing at large companies; Simon Willison used that chart to test GPT-5 and Claude Code Interpreter. Executive Order 14434, &\#x27;Inaugurating the Era of Super Intelligence,&\#x27; was signed in September 2026 and directs federal agencies to replace &\#x27;Artificial Intelligence&\#x27; and &\#x27;AI&\#x27; with &\#x27;Super Intelligence&\#x27; and &\#x27;SI&\#x27; in their communications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.federalregister.gov/documents/2026/10/02/2026-20321/inaugurating-the-era-of-super-intelligence">Federal Register :: Inaugurating the Era of Super Intelligence</a></li>
<li><a href="https://cofabrix.com/blog/super-intelligence-si-explained">Is AI Now Called Super Intelligence ? The SI Order ... | CoFabrix</a></li>
<li><a href="https://usatimes.com/census-btos-ai-adoption-rate-firm-size-sector-2026/">The Census Bureau Asks 1.2 Million Businesses If They Use AI Every...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#government data`, `#executive order`, `#AI adoption`, `#data analysis`

---

<a id="item-7"></a>
## [OpenAI Publicly Backs Amicus Briefs Defending Fair Use for AI Training](https://news.google.com/rss/articles/CBMikAFBVV95cUxNVFRob3RuU0JHbGp3SDgyaFJTam1pckxUYUJtQ3paU2NYWkl5cWY5aGVxODV0NTR4TkNldVExZ2tFa1FGZ3ZaV25mWjZtbWljLVY0X0xoaUVzcF9rczlYLXphaTBTbE5YUXJfTFVaaU5ONmNFNVpBS2FvMjVGSVMwdTZsWV9xRWxZaWdjZ3NDV0g?oc=5) ⭐️ 6.0/10

OpenAI is publicly promoting a set of amicus curiae briefs filed in copyright litigation that argue training AI models on copyrighted works is protected by the fair use doctrine. The company is amplifying third-party legal arguments rather than making its case solely in its own court filings. The outcome of these cases will determine whether AI developers must license or pay for the data behind their models, which could reshape training costs and the economics of the entire generative AI industry. A ruling against fair use would affect every major model developer, not just OpenAI, and would ripple into how content owners are compensated. Amicus briefs are filed by parties who are not directly involved in a case but seek to educate or persuade the court on a legal question, so their weight depends heavily on who signed them and how the judge treats them. Fair use itself is a fact-specific, four-factor balancing test under U.S. copyright law, meaning courts may rule differently across cases rather than settle the question in one stroke.

google\_news · IPWatchdog · Nov 2, 22:04

**Background**: Fair use is a long-standing U.S. copyright doctrine that allows limited use of protected works without permission, judged by factors such as the purpose of the use, the nature of the work, how much was used, and the effect on the market. AI developers argue that ingesting copyrighted text and images to train models is transformative and thus fair, while authors, publishers and artists contend it amounts to uncompensated copying. Because no statute explicitly addresses AI training, courts are effectively deciding the rules case by case, and interested third parties file amicus briefs to influence that process.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bitlaw.com/ai/AI-training-fair-use.html">Fair Use and the Training of AI Models on Copyrighted Works</a></li>
<li><a href="https://copyrightalliance.org/policy/amicus-briefs/">Amicus Briefs | Copyright Alliance</a></li>
<li><a href="https://www.dentons.com/en/insights/articles/2025/june/11/can-copyrighted-material-be-used-to-train-ai-systems">Dentons - Can copyrighted material be used to train AI systems?</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#copyright`, `#fair use`, `#OpenAI`, `#legal`

---

<a id="item-8"></a>
## [Medicare&\#x27;s AI-assisted coverage review pilot hit early snags, documents show](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQLWJTVGhCbHJYTndzS3pSeUIteWRwMnEyQ3NjRlJVMldLWk80OGJnNTFLNWhfbnBNdlZ5MldSdGtqeThhMGt3aHh2T1AxaWFQbGhnc2NrdjFmLXk4NWxrZ1BHbFp2N3o2N3A4S1ZiM1E5bTlsZ01icXZxWUhKRFVmRlpGTzFBclBfRmJHMS0zT0ZnY0VwZ2xwaG9FTzNtT0ZYUG9MRFBhcXcweE01b0syaDE0dktQbzVDd2pFQ0sySDd6S3AweDZwdFIycURweEd0TkFGVQ?oc=5) ⭐️ 6.0/10

According to internal documents obtained through a Freedom of Information Act request and reported by Nextgov/FCW, the federal pilot program testing whether AI and other technologies can help Medicare curb wasteful spending ran into operational problems after what the outlet describes as a rushed launch. The pilot, run by the Centers for Medicare &amp; Medicaid Services, requires prior authorization for targeted services in six states, with contracted technology companies reviewing claims before payment is made. This is one of the most consequential real-world deployments of AI in a high-stakes government decision process, since the outputs feed directly into whether patients&\#x27; care gets paid for. Early friction in the pilot will shape how CMS and other payers justify algorithmic review, and it feeds an ongoing policy debate over automated decision-making in health coverage. The pilot applies to services flagged as high risk for fraud or abuse in six states, and the contractors involved include firms that already perform prior authorization work for Medicare Advantage plans. The reported problems stem from the program&\#x27;s compressed timeline rather than from a specific published error rate, and the documents were surfaced only via FOIA, meaning the official public account of the pilot&\#x27;s performance remains limited.

google\_news · Nextgov/FCW · Nov 2, 18:19

**Background**: Traditional Medicare has historically paid claims largely without prior authorization, unlike Medicare Advantage plans, which routinely require approval in advance and have already drawn scrutiny for using algorithms to speed those reviews. Prior authorization requires clinicians to get payer approval before delivering a service, and CMS estimates the process costs providers $20-50 per hour and consumes around 13 hours per week. The pilot extends that model, with AI assistance, into original Medicare for selected services, with the stated goal of cutting wasteful spending while avoiding harm to patients.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nextgov.com/artificial-intelligence/2026/11/medicares-ai-assisted-coverage-review-pilot-hit-early-snags-documents-show/416978/">Medicare’s AI-assisted coverage review pilot hit early snags ...</a></li>
<li><a href="https://schaeffer.usc.edu/research/medicare-experiment-ai-prior-authorization/">Medicare Is Experimenting With Having AI Review Claims</a></li>
<li><a href="https://www.aarp.org/medicare/original-medicare-ai-prior-authorization-pilot/">AI Prior Authorization Pilot Hits Original Medicare - AARP</a></li>

</ul>
</details>

**Tags**: `#AI in healthcare`, `#government AI policy`, `#Medicare`, `#AI deployment`, `#healthcare regulation`

---

<a id="item-9"></a>
## [NYT Report Examines Anthropic&\#x27;s Scramble for AI Compute](https://news.google.com/rss/articles/CBMihgFBVV95cUxQSzNBLTZEQWd3WGJtSVlvWW9BYnlFNW91WUowLUhCZFJ4NmREYU4tUG9hM1Jzb0RaOVNKczZPTUZQVHk3SHVSVlRFRGM4UnZtdHhMcnNWM1FLOWFUSzlGVXpiYUpPNElWcnpzWmliRUk4Z2JIaE0yeVFhc3NLcEZUdl9NdVN3Zw?oc=5) ⭐️ 6.0/10

The New York Times published a report titled &quot;Inside Anthropic&\#x27;s Hunt for A.I. Computing Power,&quot; focusing on how the AI company is working to secure the computing capacity needed to train and run its models. Compute has become a primary bottleneck for frontier AI labs, so Anthropic&\#x27;s ability to lock in chips, cloud capacity, and data-center deals directly affects its ability to compete with OpenAI, Google, and other leading model developers. The available item provides only the headline and a link, so the report&\#x27;s specific figures, suppliers, and deal terms cannot be verified from the supplied material.

google\_news · The New York Times · Nov 2, 18:01

**Background**: Anthropic is an AI safety and research company behind the Claude family of large language models. Training and serving frontier models requires enormous amounts of specialized chips, typically Nvidia GPUs, as well as large-scale cloud and data-center capacity. The New York Times report fits into a broader industry race among AI labs to secure long-term compute supplies, which has become a strategic constraint alongside talent and data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.feedtheai.com/what-is-ai-compute/">What Is AI Compute? Training vs Inference Explained</a></li>
<li><a href="https://ainowinstitute.org/publications/compute-and-ai">Computational Power and AI - AI Now Institute</a></li>
<li><a href="https://www.insidedeeptech.com/the-state-of-ai-infrastructure-2026-compute-power-and-constraints/">The State of AI Infrastructure 2026: Compute, Power, and ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#Anthropic`, `#compute`, `#industry news`, `#AI/ML`

---

<a id="item-10"></a>
## [OpenAI and Microsoft Amicus Briefs Diverge in AI Copyright Case](https://news.google.com/rss/articles/CBMi2gFBVV95cUxPaWhMUjMwenhTUkdMN1RiYzdJZXhycjNOdFlsQWNzdGxVNlpZZ2ZEa05vU05YWW1tVG1zbk54eWVVOGpuT19rUUN6UDhBVjVWOEhoanRFTFc1VVUyUDVibWhtdlMwcE1qRjZ1aEx3ODFnTVVtOWRucVRSZHZrTFFpR3htY1VFUTAwQi1DZUN2MmdCX2FsR2EyOHl5ck45Z3RIVXNJNlFfU1pqLWZHcTVqa3NQcW1KVmlXUC0tM0pQNi1BZ3BYdXotWjlCUFBZODZqVUtUMVIzakwzZ9IBWkFVX3lxTE82YlZRWW5EaVdhTVBadTdobU9uVHhWMHd1bXQtQjZMbW4xd0VvblNPVUxGMmh0QS1jdktRY0dmdDFPLU91S1RWUDBkdXhZdDA1WTgzZ190c0EtQQ?oc=5) ⭐️ 6.0/10

According to MLex, OpenAI and Microsoft have each submitted amicus curiae briefs in an ongoing AI copyright lawsuit, and their arguments reportedly diverge over how copyright law should treat creative incentives and market competition. The two companies, which are close partners and often co-defendants in training-data litigation, are said to be pressing different framings rather than a single unified position. Amicus briefs signal to courts how the wider industry wants copyright doctrine to be shaped, so any daylight between the two most prominent AI developers matters for how fair-use boundaries get drawn for model training. A split could also feed antitrust scrutiny of the OpenAI–Microsoft relationship, since competition arguments and copyright arguments are being bundled together. The source material available is only an MLex headline and summary, so the specific legal arguments, the court involved, and the case name were not disclosed. Notably, OpenAI and Microsoft are frequently aligned as co-defendants in training-data suits, which makes separate amicus filings — as opposed to joint briefing — an unusual and closely watched choice.

google\_news · MLex · Nov 2, 22:35

**Background**: American copyright litigation over generative AI centers on fair use, the doctrine in Section 107 of the U.S. Copyright Act that allows limited unlicensed use of copyrighted works, including for purposes such as criticism, research, or teaching. An amicus curiae, or &quot;friend of the court,&quot; brief is filed by a party that is not directly involved in a case but wants to offer the court context, expertise, or policy arguments. AI developers generally argue that training models on publicly available text and images is transformative fair use, while publishers, authors, and artists argue it amounts to uncompensated copying that undermines their markets.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Amicus_curiae">Amicus curiae - Wikipedia</a></li>
<li><a href="https://decreza.com/amicus-curiae-in-copyright-disputes/">Understanding the Role of Amicus Curiae in Copyright Disputes</a></li>
<li><a href="https://www.zyte.com/blog/what-ai-builders-need-to-know-about-the-training-data-copyright-debate/">What AI Builders Need to Know About the Training Data Copyright ...</a></li>

</ul>
</details>

**Tags**: `#AI copyright`, `#OpenAI`, `#Microsoft`, `#legal disputes`, `#competition policy`

---