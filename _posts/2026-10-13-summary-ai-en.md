---
layout: default
title: "Horizon Summary: 2026-10-13 (EN)"
date: 2026-10-13 23:04:27 +0000
lang: en
report: ai
---

> From 184 items, 10 important content pieces were selected

---

1. [Epic shifts unannounced Disney crossover shooter to AI-driven development, 2027 launch delayed indefinitely](#item-1) ⭐️ 8.0/10
2. [Geoffrey Huntley: Steer Coding Agents with Pre-Commit Hooks](#item-2) ⭐️ 7.0/10
3. [AI Moves From Arithmetic to Attacking Famous Open Math Problems](#item-3) ⭐️ 7.0/10
4. [MIT News: How Artificial Neural Networks Build Their Own Learning Machinery](#item-4) ⭐️ 7.0/10
5. [California Bans AI From Making Medical Decisions Autonomously](#item-5) ⭐️ 7.0/10
6. [Nature Paper Proposes Human-AI Collaboration for Real-Time Epilepsy Comanagement](#item-6) ⭐️ 7.0/10
7. [AWS Details Mixture-of-Experts Kernel Engineering on SageMaker AI](#item-7) ⭐️ 7.0/10
8. [Kroger to Cut 3,000 Corporate Jobs as It Leans Into AI](#item-8) ⭐️ 7.0/10
9. [OpenAI Reportedly Says Employee Caught Planting Listening Device](#item-9) ⭐️ 7.0/10
10. [IDC: NVIDIA&\#x27;s China AI Chip Share Falls to 34%, Huawei Climbs to 28%](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Epic shifts unannounced Disney crossover shooter to AI-driven development, 2027 launch delayed indefinitely](https://www.aibase.com/news/31607) ⭐️ 8.0/10

Bloomberg reports that Epic Games has moved an unannounced Disney crossover shooter — combining Marvel and Star Wars IPs — onto an AI-centric development pipeline, using Anthropic&\#x27;s Claude to write code directly and AI art workflows for visuals, with project leads telling the team to stop manual coding. The game&\#x27;s planned 2027 release has reportedly been delayed indefinitely. If accurate, this goes well beyond the usual AI-assisted coding and makes generative AI the backbone of a large AAA production, which could reshape how major studios staff, budget, and schedule games. It is also likely to intensify the industry debate over developer jobs, creative ownership, and quality control as AI moves from a helper tool to the center of the pipeline. According to the report, humans are kept only in guiding, managing, and reviewing roles rather than writing code or assets themselves, and the title remains officially unannounced, so nothing about its release timing or scope has been confirmed by Epic or Disney. The information comes from a Bloomberg report rather than an official announcement, and the indefinite delay suggests the AI-first approach has not yet delivered a shippable schedule.

aibase · AIbase · Oct 13, 16:01

**Background**: Epic Games is the studio behind Fortnite and the Unreal Engine, and a crossover shooter mixing Marvel and Star Wars characters would be an unusually large licensed project. Anthropic&\#x27;s Claude is a family of large language models widely used for coding tasks, while AI art workflows use image-generation models plus prompting and editing steps to produce consistent visual assets. Generative AI is already spreading through game development — one bibliometric study in the ACM Digital Library estimates that programmatic content generation can cut production costs by as much as 70% — but placing it at the core of a licensed AAA title is a much bigger commitment than using it for prototypes or background assets.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/resources/articles/claude-models-explained-choosing-the-best-model-for-your-use-case">Claude models explained: choosing the best model for your use ...</a></li>
<li><a href="https://www.imagine.art/workflow">AI-Powered Design Workflows |ImagineArt</a></li>

</ul>
</details>

**Tags**: `#AI in game development`, `#Epic Games`, `#Disney`, `#generative AI`, `#coding automation`

---

<a id="item-2"></a>
## [Geoffrey Huntley: Steer Coding Agents with Pre-Commit Hooks](https://simonwillison.net/2026/Oct/13/geoffrey-huntley/) ⭐️ 7.0/10

Geoffrey Huntley described a technique in which, instead of repeatedly editing AGENTS.md to steer a coding agent, he writes a pre-commit hook that scans the git diff for direct calls to observability modules that bypass his own diagnostics library. When such a violation is found, the hook fails the commit and injects a corrective prompt telling the agent to use the diagnostics library — which, he says, takes the agent from unreliable to &quot;ten out of ten.&quot; Simon Willison quoted the passage on his blog, highlighting it as a more durable alternative to prompt- or documentation-based agent steering. As coding agents write more production code, guidance expressed only in prompts or AGENTS.md files drifts out of sync and can be silently ignored, so deterministic, CI-enforced guardrails that the agent cannot bypass represent a meaningful shift in agentic engineering. It reframes agent steering as an enforced constraint, much like linting or type checking, and gives teams a reproducible way to keep agents aligned with internal conventions. The technique works because the failed commit and its message are fed back into the agent&\#x27;s own loop, so the correction arrives as actionable context rather than as advice a human must remember to repeat. It only applies to violations that are statically detectable in the diff — for example, imports of an observability package instead of the sanctioned diagnostics module — and it is inherently repo-specific, encoding each project&\#x27;s own library conventions. Note that the source is a short quoted passage rather than a full technical deep-dive.

rss · Simon Willison · Oct 13, 13:32

**Background**: AGENTS.md is a conventional, README-like file that gives AI coding agents persistent context about a repository, including style rules, safety rails and workflows; tools such as OpenAI&\#x27;s Codex CLI use it as the standard place for repo-level instructions. Git hooks are scripts that Git runs automatically at points in its workflow, and the pre-commit hook runs before a commit is created — if it exits with a non-zero status, Git aborts the commit entirely. Because commit failures are visible to whatever process is driving the repository, hooks are a natural chokepoint for enforcing policy, and tools like the pre-commit package manager make installing and running such hook scripts across languages easy.

<details><summary>References</summary>
<ul>
<li><a href="https://agents.md/">AGENTS . md</a></li>
<li><a href="https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks">Git - Git Hooks</a></li>
<li><a href="https://pre-commit.com/">pre-commit</a></li>

</ul>
</details>

**Tags**: `#coding-agents`, `#agentic-engineering`, `#git-hooks`, `#prompt-engineering`, `#generative-ai`

---

<a id="item-3"></a>
## [AI Moves From Arithmetic to Attacking Famous Open Math Problems](https://news.google.com/rss/articles/CBMinAFBVV95cUxNU0RGUE1VajZ0NWZfYWVGbGJOOXBoUi1kNnZXX2lGQjFmS0F4SERhN0VJbXJWc1BKSUl5ekNLbU96X2ZqWXdNNVF6YU1sRTFFZVFIZWpVLWN2NXRSWnRVUlUzam5qQ0xEaE13Z3ZpTmdWeTFMZnJNdkhkTVQ1UDRuNVNyOG8xZzFNV0lrbXFfMnpiWE5aMkw2TFYyUWM?oc=5) ⭐️ 7.0/10

A New York Times article reports that artificial intelligence has advanced from struggling with basic arithmetic to actively helping solve some of mathematics&\#x27; most famous open problems, prompting the field to reckon with what that shift means. The piece cites commentary from Steven Strogatz, a professor of mathematics, on how mathematicians are reassessing their relationship with AI. If AI can meaningfully contribute to open problems in mathematics, it signals a shift in how pure research is conducted — potentially accelerating discovery and changing what counts as a mathematician&\#x27;s core contribution. The development also raises uncomfortable questions about credit, verification, and whether AI-generated proofs can be trusted by the mathematical community. The available item is only a short teaser linking to the full New York Times article, so it does not specify which open problems were addressed, what methods were used, or how results were verified. Details on the AI systems involved, the role of human mathematicians, and peer review of any claimed results are therefore still unclear.

google\_news · Facebook · Oct 13, 19:30

**Background**: Mathematics has long been considered a benchmark of deep reasoning, and classic AI systems were notoriously weak at even simple arithmetic and symbolic manipulation. Recent years have seen systems such as DeepMind&\#x27;s AlphaGeometry, FunSearch and AlphaProof make progress on Olympiad-level problems and conjecture-driven search, while mathematicians like Terence Tao have begun experimenting with AI as a research assistant. This article frames the broader cultural moment in which mathematicians debate whether such tools are collaborators, competitors, or merely very capable pattern matchers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://www.wikiwand.com/en/Automated_theorem_proving">Automated theorem proving - Wikiwand</a></li>
<li><a href="https://grokipedia.com/page/Automated_theorem_proving">Automated theorem proving</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Mathematics`, `#Research`, `#Open Problems`, `#NYT`

---

<a id="item-4"></a>
## [MIT News: How Artificial Neural Networks Build Their Own Learning Machinery](https://news.google.com/rss/articles/CBMinAFBVV95cUxPbEdzZlpSZE5va0hVeUExZ2h5UU9oSEZrUTYxcElOd05xRDdTeVRMUV9HbkpiQWc2QTloaExDWW1Nc1VOdDVkSEY5a2VUWk9PR05ySXJnYVpRZFl3azB0WEZGTlUtVlJ3b3d5ME45VHZoc3VKMHR5TU1tWElFNEduMGc4VXYxZjF5bUNoRjVIc2NRTlVFLXpGekVqZlg?oc=5) ⭐️ 7.0/10

MIT News has published a research report titled &quot;How artificial neural networks build their own learning machinery,&quot; describing work that examines how artificial neural networks self-organize and construct their own learning mechanisms rather than relying solely on human-designed architectures and training procedures. Because only the headline and one-line summary are available, the specific algorithms, model names, and experimental results behind the work have not yet been confirmed. If networks can build or adapt their own learning machinery, it points toward systems that need less hand-tuning of architectures and training rules, which is directly relevant to meta-learning and automated machine learning research. Such capability could eventually lower the cost of adapting models to new tasks and domains, affecting AI researchers and practitioners who currently spend substantial effort on architecture and hyperparameter design. The claim sits at the intersection of meta-learning, where learning algorithms are applied to metadata about machine learning experiments, and self-organizing network approaches such as self-organizing maps, which are unsupervised techniques that arrange nodes into low-dimensional representations without labeled data. Since the item is a headline-only link, no quantitative results, benchmarks, or limitations have been verified.

google\_news · MIT News · Oct 13, 21:00

**Background**: Artificial neural networks are computing systems loosely inspired by biological brains, made of layers of interconnected nodes whose connection weights are adjusted during training. Traditionally, humans choose the architecture and the learning rule, and the network only optimizes the parameters within that fixed framework. Meta-learning, often described as &quot;learning to learn,&quot; studies how algorithms can improve their own learning process across many tasks, while self-organizing networks explore how structure can emerge from data itself. This news concerns research that tries to combine those ideas by having networks construct the machinery that drives their own learning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Meta-learning">Meta-learning</a></li>

</ul>
</details>

**Tags**: `#neural-networks`, `#meta-learning`, `#AI-research`, `#self-organization`, `#machine-learning`

---

<a id="item-5"></a>
## [California Bans AI From Making Medical Decisions Autonomously](https://news.google.com/rss/articles/CBMirgFBVV95cUxPdTBsVXV4MUJHZkZReFpJUnlPdzZtLWEtUnRVTllRMzVYaG80ajBNQmR3WlFVaXhaOEUtWEpHbHkxWTZvVDlfb0ZxZEZMQWV1RXBoa1ZoUnkxX3JuR1dLNjFObkNXTmhaNWhqcVZtR0F2X1FEZk90MFRfNGEzS05PQUFvV0JZZG91eUM5RGRWenF5THkxSDdrUWx1aG56TEtBLVRidzhxZWdNT0lnR2c?oc=5) ⭐️ 7.0/10

California has enacted a ban that prevents AI systems from making medical decisions on their own, according to a report by Governing. Under the new rule, an AI system can no longer serve as the sole decision-maker in a medical matter, and a human clinician must remain responsible for the final call. California is the largest U.S. state and the home base of most leading AI developers, so its rules frequently become de facto standards that shape products sold nationwide. This ban sets an early precedent for how &quot;human in the loop&quot; requirements will be applied to clinical AI, affecting diagnostic tool vendors, clinical decision-support startups, insurers that use algorithms, and the patients they serve. Because only a headline and link were available, the exact bill number, effective date, enforcement mechanism, and penalties remain unspecified, and it is unclear whether the ban covers all clinical decisions or narrower areas such as coverage and medical-necessity determinations. Such laws typically still permit AI as a decision-support tool, as long as a licensed professional reviews and authorizes the final decision.

google\_news · Governing · Oct 13, 20:11

**Background**: AI is already embedded in healthcare for tasks such as interpreting medical images, triaging patients, flagging sepsis risk, and automating insurance prior-authorization reviews. Concerns about algorithmic bias, errors, and unclear accountability have fueled demands for rules requiring a human to remain in the loop for consequential medical choices. California has been one of the most active U.S. states on AI legislation in recent sessions, and since federal oversight of medical AI remains fragmented, state laws often fill the gap.

**Tags**: `#AI regulation`, `#healthcare AI`, `#California law`, `#medical decision-making`, `#policy`

---

<a id="item-6"></a>
## [Nature Paper Proposes Human-AI Collaboration for Real-Time Epilepsy Comanagement](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1lUnU1bkhVSTJicWdwdkFpNC01LTY2MTZlVnZST1pqNUdsWVRtZFA3OGhMZHhaQWlwSmE1TG1YVG9naFc5SEZNc2xiWXNOeENoMGVqMG9rT0YxdmZPeDlV?oc=5) ⭐️ 7.0/10

A paper published in Nature presents a human-artificial intelligence collaboration framework for comanaging epilepsy in real time, positioning AI as a partner to clinicians rather than a standalone decision-maker. The item as surfaced provides only the title and a link, with no abstract, methodology, dataset details, or reported results. Epilepsy is a chronic neurological condition affecting roughly 50 million people worldwide, and many seizures are unpredictable, so real-time co-management could meaningfully change how quickly interventions occur. Placing a human clinician inside the loop also addresses a central concern in medical AI: how to keep expert judgment and accountability in the decision process while still gaining the speed and sensitivity of algorithmic detection. Because only the title and link are available, the specific algorithmic approach, the patient cohort, the latency of the real-time loop, and any clinical endpoints cannot be verified from the material provided. The framing as &quot;comanagement&quot; implies a shared-control design in which the AI and the clinician both contribute to decisions, rather than a fully automated closed-loop system.

google\_news · Nature · Oct 13, 10:23

**Background**: Epilepsy is a neurological disorder marked by recurrent, unprovoked seizures, and it is commonly managed with anti-seizure medication, surgery, or implanted neurostimulation devices. Real-time management typically relies on continuous monitoring signals such as electroencephalography \(EEG\) or wearable sensors, which can feed algorithms that detect or even predict seizure onset. Human-AI collaboration, often called human-in-the-loop AI, is an emerging paradigm in medical machine learning where the model handles rapid pattern recognition while a human expert retains authority over consequential actions. Nature is a long-established, peer-reviewed multidisciplinary journal, so publication there signals that the work passed independent scientific review.

**Tags**: `#AI in Healthcare`, `#Human-AI Collaboration`, `#Epilepsy`, `#Medical AI`, `#Real-time Systems`

---

<a id="item-7"></a>
## [AWS Details Mixture-of-Experts Kernel Engineering on SageMaker AI](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNZm5KczRMWk1BdGxMN1M0ZUsyMVdXeWxMUkt5WjhGWDJlc3pxOXZOYXVCUzEzemtnZ0hNM0FuTHFiei1YbEgxZ3Z4THRfSTE0YWpKWDFZNHlfV0h4bWlZZ3pXNTd0MXVHSDRlR2NlaWZHNnA1OHFOcDl5UkhaS21GdTVzWi1qZjk0R1FXVXMtOGU2RHp4RGUtSkllN05qX1dHVG5ReDFieEhjVk0?oc=5) ⭐️ 7.0/10

Amazon Web Services published a technical blog post covering Mixture-of-Experts \(MoE\) kernel engineering on Amazon SageMaker AI, walking through how low-level GPU kernels for MoE layers are designed and optimized on AWS&\#x27;s managed machine learning platform. The post is aimed at AI/ML systems practitioners who train or serve sparse MoE models rather than at general application developers. MoE architectures power many of today&\#x27;s frontier large language models, and their performance is often limited not by model design but by how efficiently the routing, gather/scatter and grouped matrix multiplication kernels run on the GPU. Practical guidance from a major cloud vendor on tuning these kernels directly affects training cost, inference latency, and how affordable it is to run large sparse models on SageMaker AI. Kernel engineering at this level typically involves hand-written or compiler-generated GPU kernels \(for example CUDA or Triton\) specialized for MoE operations such as token routing, permutation/gather-scatter of tokens to experts, and grouped GEMM, with trade-offs around memory bandwidth, expert load balancing and capacity factors. Because the summary only points to the blog post itself, concrete benchmark numbers, supported model sizes and framework versions should be verified in the original article.

google\_news · Amazon Web Services \(AWS\) · Oct 13, 15:17

**Background**: Mixture-of-Experts \(MoE\) is a machine learning technique in which multiple smaller &\#x27;expert&\#x27; networks each specialize in part of the problem space, and a gating or routing network decides which experts process each input token. This lets a model hold a very large total number of parameters while only activating a small fraction of them per token, which is why MoE has become popular for frontier LLMs. Amazon SageMaker AI is AWS&\#x27;s managed cloud platform, launched in 2017, for building, training and deploying machine learning models; this post sits at the intersection of the two, describing the systems-level kernel work needed to make MoE models run efficiently on that platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Amazon_SageMaker">Amazon SageMaker</a></li>

</ul>
</details>

**Tags**: `#Mixture-of-Experts`, `#Kernel Engineering`, `#Amazon SageMaker`, `#AI/ML Systems`, `#AWS`

---

<a id="item-8"></a>
## [Kroger to Cut 3,000 Corporate Jobs as It Leans Into AI](https://news.google.com/rss/articles/CBMizwFBVV95cUxPNjBtVEtZaXktdlhNWE1Sd3ltZVM5alB0RDUtYU44aXlJd04teEF0aVVzUEVRYXRIeWxyVjg4aHMzZzZ1c2dnNnhDY3NDMmJEamNveW5IWmJRbEpjS2FzUVpMcjI4dElnaURiMjFxXzBKVEJwNy0wMHo4SUdrWDNYM0QzT2tjblQxcm9tNkRFWDFoMENPamdxMlpVQUdlaDl3bjFuaEVQYzUteV8ycGVBbEs0S1pJdi0yU0ktamIwMXRrcFFiRDFCa05lejZtSUE?oc=5) ⭐️ 7.0/10

Kroger, one of the largest US grocery chains, announced it will lay off roughly 3,000 corporate employees over the next three years as it increases its use of artificial intelligence. Multiple local news outlets, including KATV and KLTV, reported the cuts as part of the company&\#x27;s broader push into AI-driven operations. This is one of the clearest examples yet of a major US retailer attributing white-collar job cuts directly to AI adoption, reinforcing fears that automation is moving beyond factories and warehouses into corporate and administrative roles. It could pressure other large retailers to follow suit and adds to the broader debate over AI&\#x27;s impact on employment. The reductions are concentrated in corporate and administrative positions rather than store-level staff, and are spread out over a three-year period starting from the announcement. The roughly 3,000 figure represents a substantial share of Kroger&\#x27;s corporate workforce, though the company has not detailed which specific departments or functions will be most affected.

google\_news · KATV · Oct 13, 19:40

**Background**: Kroger is one of the largest supermarket operators in the United States, employing hundreds of thousands of people across its grocery banners. In retail, AI is increasingly used for demand forecasting, inventory and supply-chain management, pricing, and customer service, which can reduce the need for corporate and analytical staff. Kroger has also been pursuing a major merger with rival Albertsons, a deal that has drawn regulatory scrutiny and added pressure to cut costs.

**Tags**: `#AI`, `#layoffs`, `#automation`, `#retail`, `#workforce`

---

<a id="item-9"></a>
## [OpenAI Reportedly Says Employee Caught Planting Listening Device](https://news.google.com/rss/articles/CBMif0FVX3lxTFBlU3Z6SEpSd0V3NmtRM1pfRk9IUW1JdDNmQlZsMGw3V1lNT2xkcHZtV3BSUm82NHFtSEtIY3ZISXBWRjdGRXI4YjlNWEhxVFQ1YzFVNkRuZWdwX2sySjA5dDJDMWY0ejZxRTlYWE1sQzhpNDdsbjJlSVlhWUtseTDSAX9BVV95cUxPWkZKZWwxLVQ0WWpJY2JfZm15SUtxbWVXUjNrMGxZZ0stSnRYZmY4eExFMEdDczFQX0FyTHNQc1hveTc2OG1VVGdRNDdSMk5Jb0htcUtLSXRLRDA0bzhYbGMxc01RekhLelFHREdxb2h5QlZlWWNXcXNtakNzYlo0?oc=5) ⭐️ 7.0/10

According to a Deutsche Welle \(DW.com\) report, OpenAI announced that an employee was caught planting a listening device. The available item contains only that headline, with no confirmed details about the individual, the location, the timing, or how the device was discovered. If accurate, this points to an insider security threat at one of the world&\#x27;s most prominent AI labs, where model weights, unreleased research and executive communications are highly sensitive assets. Such an incident could push AI companies toward stricter internal monitoring, device controls and employee vetting, and could also raise staff-privacy concerns about those very measures. The item available is only a headline with no verifiable specifics: no named suspect, no date, no statement on whether law enforcement was involved, and no description of the device or where it was found. Claims about the incident should therefore be treated as unconfirmed until OpenAI or another primary source publishes details.

google\_news · DW.com · Oct 13, 21:31

**Background**: OpenAI is the developer of ChatGPT and the GPT family of large language models, and it competes with Google, Anthropic, Meta and others in a field where technical know-how and model weights are enormously valuable. A &\#x27;listening device&\#x27; here refers to a covert audio-surveillance tool, such as a hidden microphone or bug, planted to record private conversations. Insider threats — employees, contractors or visitors misusing their access — are a recognized category of corporate security risk, and AI labs have been tightening physical and digital access controls as the value of their intellectual property has risen. DW.com is Deutsche Welle, Germany&\#x27;s publicly funded international broadcaster.

**Tags**: `#OpenAI`, `#security`, `#espionage`, `#privacy`, `#AI industry`

---

<a id="item-10"></a>
## [IDC: NVIDIA&\#x27;s China AI Chip Share Falls to 34%, Huawei Climbs to 28%](https://www.aibase.com/news/31617) ⭐️ 7.0/10

IDC reports that NVIDIA&\#x27;s share of China&\#x27;s data-center AI chip market fell to 34% in the first half of 2026, while Huawei rose to 28%. NVIDIA&\#x27;s China AI accelerator shipments totaled 678,000 units in January–June, down 44% year-over-year, as US export curbs constrained its supply. This signals a structural shift in the world&\#x27;s second-largest AI hardware market, where US export controls are effectively transferring share to domestic Chinese vendors instead of slowing them down. It also strengthens Beijing&\#x27;s push for self-sufficiency in AI silicon and reshapes the competitive landscape for the entire semiconductor supply chain. The share loss is driven directly by US export restrictions that limited NVIDIA&\#x27;s ability to supply Chinese customers, and CEO Jensen Huang has publicly criticized Washington&\#x27;s policy, arguing the curbs hand a roughly $50 billion market to local rivals. The figures cover only the data-center AI accelerator segment in the first six months of 2026 and do not include NVIDIA&\#x27;s other China businesses.

aibase · AIbase · Oct 13, 18:01

**Background**: China&\#x27;s data-center AI chip market refers to accelerators used to train and run AI models in cloud and enterprise data centers — a segment NVIDIA has long dominated worldwide with its data-center GPUs. Since 2022, the US has repeatedly tightened export controls on advanced AI chips sold to China, prompting NVIDIA to design downgraded China-specific parts and encouraging Huawei and other domestic firms to develop alternatives such as the Ascend series. Market-share numbers like these are closely watched as a barometer of how quickly China can substitute domestic silicon for US-designed hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/ai-accelerator">What is an AI accelerator? - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_processing_unit">Neural processing unit - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Huawei`, `#AI chips`, `#China`, `#export controls`

---