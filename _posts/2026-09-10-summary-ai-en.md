---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10 23:05:38 +0000
lang: en
report: ai
---

> From 280 items, 10 important content pieces were selected

---

1. [Shopify Drops React Native for Native Swift and Kotlin, Citing AI Agents](#item-1) ⭐️ 8.0/10
2. [Calif Research Claims WeWorm Is First Zero-Click Worm Spread via WeChat Calls](#item-2) ⭐️ 8.0/10
3. [Anthropic blocks AI misuse that could have aided biological weapons](#item-3) ⭐️ 8.0/10
4. [California Enacts AI Safety Laws Backed by OpenAI and Anthropic](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4.1 Flash: 552B MoE Model Outperforms V4 Pro](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4.1 Flash: 552B MoE Multimodal Model Beats Pro on Vision](#item-6) ⭐️ 8.0/10
7. [Anthropic blocks AI misuse that could have aided biological weapons](#item-7) ⭐️ 7.0/10
8. [Pentagon in Talks to Lend $5B to AI Cloud Startup Fluidstack](#item-8) ⭐️ 7.0/10
9. [Anthropic Says It Blocked Possible Attempts to Use AI for Biological Weapons](#item-9) ⭐️ 7.0/10
10. [OpenAI Shifts Stance, Backs National AI Safety Rules](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Shopify Drops React Native for Native Swift and Kotlin, Citing AI Agents](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify announced on its engineering blog that it is moving its mobile apps off React Native and back to fully separate native codebases — Swift for iOS and Kotlin for Android — explicitly citing AI coding agents as the reason. The company also said it is finding new homes for the React Native libraries react-native-skia and flash-list, while its smaller restyle library will be archived at the end of 2026. This is a notable reversal: Shopify was one of the most prominent enterprise adopters of React Native and a major maintainer of its library ecosystem, so its retreat challenges the long-standing &\#x27;go cross-platform to save effort&\#x27; orthodoxy. If AI agents really do absorb enough duplicate implementation and translation work, other large engineering organizations may re-evaluate the trade-off between a single JavaScript codebase and platform-specific code. Shopify notes that in 2020 it chose React Native to stop building the same features twice, let developers work across the stack, and spend less time chasing feature parity; the cost of maintaining two platforms has not disappeared, but agents can now handle enough implementation, translation, testing, and review work that it is no longer the deciding factor. The announcement is a single-company case study rather than a proven industry-wide shift, and Shopify&\#x27;s own framing gives full credit to React Native for the six years it was used.

rss · Simon Willison · Sep 10, 21:11

**Background**: React Native is an open-source framework, originally released by Meta in 2015, that lets developers write a single JavaScript/React codebase and deploy near-native apps to both iOS and Android. Going &\#x27;native&\#x27; instead means writing and maintaining two separate codebases, Swift on iOS and Kotlin on Android, which usually yields better platform fidelity and performance at the cost of duplicated effort. AI coding agents such as Cursor have become mainstream tools that write, translate, test, and review code across languages, which is the lever Shopify says changed the economics.

<details><summary>References</summary>
<ul>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://cursor.com/">AI Coding Agent for Building Ambitious Software | Cursor</a></li>

</ul>
</details>

**Tags**: `#mobile-development`, `#react-native`, `#ai-agents`, `#engineering-strategy`, `#swift-kotlin`

---

<a id="item-2"></a>
## [Calif Research Claims WeWorm Is First Zero-Click Worm Spread via WeChat Calls](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 8.0/10

Calif Research published a demo of WeWorm, which it describes as the first zero-click worm to spread through WeChat voice calls on both iOS and Android, compromising a victim&\#x27;s account without the call ever being answered. The team says it used AI assistance to find the bug and write the first remote code execution \(RCE\) exploit in roughly two days, then spent about one more week turning it into a self-spreading worm. If verified, this would show that AI can compress exploit development from months of skilled team work into days, dramatically lowering the barrier to building large-scale self-propagating malware against a messaging platform with over a billion users. It also raises urgent questions for platform vendors about how quickly they can patch a zero-click RCE chain that requires no user interaction at all. The attack is genuinely zero-click: the victim does not need to answer the call or touch the phone, and even if they do answer, they hear nothing while the exploit still succeeds, with accounts reportedly hijacked in seconds. Calif says it privately reported the vulnerability to Tencent, and the public material so far is only a short demo announcement rather than technical documentation that outside researchers can verify.

rss · Simon Willison · Sep 10, 00:56

**Background**: WeChat is Tencent&\#x27;s messaging and social app with well over a billion users, and voice calling is one of its core features. A zero-click attack means no interaction from the victim is required, while a worm is malware that copies itself and spreads automatically to other users, which is what makes this combination unusually dangerous. Remote code execution \(RCE\) is a class of vulnerability that lets an attacker run arbitrary code on someone else&\#x27;s device, typically serving as the entry point for installing further malware or stealing data.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm - First 0-Click Worm Spreading Through WeChat Calls Across iOS and Android</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">&quot;Zero-click&quot; WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://cybernews.com/editorial/emergence-of-ai-worms/">Zero-click malware: the emergence of AI worms | Cybernews</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI-assisted exploitation`, `#zero-click worm`, `#WeChat`, `#remote code execution`

---

<a id="item-3"></a>
## [Anthropic blocks AI misuse that could have aided biological weapons](https://www.sandiegouniontribune.com/2026/09/10/anthropic-threat-report/) ⭐️ 8.0/10

Anthropic reported in a company threat report that it detected and blocked misuse of its AI systems that could have supported the development of biological weapons. The disclosure comes from the company&\#x27;s own threat-intelligence reporting rather than from an external regulator or law-enforcement action. This is a notable AI safety and biosecurity development from a major frontier lab, because it illustrates the kind of concrete misuse scenario that policymakers and safety researchers have long warned about when granting broad access to powerful models. How Anthropic handled and disclosed the case could shape industry norms for threat reporting and influence emerging AI-biosafety regulation. The information available so far comes from Anthropic&\#x27;s threat report and does not include technical specifics such as the model versions involved, the number of accounts, or the assessed capability level of the actors. As with any vendor self-disclosure, the details are reported by the company itself and have not been independently verified by outside researchers or authorities.

gdelt · sandiegouniontribune.com · Sep 10, 22:30

**Background**: Anthropic is an AI company that develops the Claude family of large language models and positions AI safety as central to its mission, so it periodically publishes reports describing attempted misuse of its systems. A central concern in AI safety is &\#x27;uplift&\#x27;: whether a model can give someone without specialized training information or guidance that meaningfully raises their ability to cause harm, particularly in sensitive domains such as biosecurity. Biological weapons development is widely treated as one of the highest-severity risk categories for AI misuse, which is why frontier labs, governments, and biosecurity experts monitor it closely.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biosecurity">Biosecurity</a></li>
<li><a href="https://en.wikipedia.org/wiki/Threat_intelligence">Threat intelligence</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#biosecurity`, `#Anthropic`, `#threat intelligence`, `#misuse prevention`

---

<a id="item-4"></a>
## [California Enacts AI Safety Laws Backed by OpenAI and Anthropic](https://www.aibase.com/news/30960) ⭐️ 8.0/10

California Governor Gavin Newsom signed a package of artificial intelligence regulatory laws that require frontier large models to conduct strengthened safety risk assessments, transparency disclosures, and safeguards against catastrophic cyberattacks. Under the new rules, models with trillions of parameters must undergo red team drills and third-party audits before they can be launched. This is one of the most concrete state-level AI safety regimes enacted in the United States, and the unusual public endorsement from OpenAI and Anthropic signals that leading labs may prefer predictable compliance rules over a patchwork of uncertain regulation. Because California hosts most major AI developers, the requirements could effectively become a de facto national standard and shape AI safety compliance practices well beyond the state&\#x27;s borders. The obligations apply specifically to frontier models at the trillion-parameter scale, which must complete red team exercises and independent third-party audits prior to deployment rather than after release. The reporting does not specify effective dates, the exact parameter thresholds, penalties for non-compliance, or which bodies will certify the auditors, and third-party audits are inherently limited in what they can detect about societal or unforeseen harms.

aibase · AIbase · Sep 10, 16:01

**Background**: Red teaming in AI is the practice of systematically probing a model by simulating adversarial attacks and edge cases to surface vulnerabilities, harmful outputs, and failure modes before deployment. Third-party audits bring in independent reviewers to check a system against legal, ethical, and technical standards, since self-assessment by the developer may not be trusted. The trillion-parameter threshold matters because parameter count is a rough proxy for model capability — the more capable a model is, the greater its potential to cause harm if misused. California is the home base of OpenAI, Anthropic, Google, and Meta, so state legislation there tends to set the tone for US AI policy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.respan.ai/glossary/red-teaming">What is Red Teaming ? | AI &amp; LLM Glossary | Respan</a></li>
<li><a href="https://www.warden-ai.com/resources/third-party-ai-audit">Third-Party AI Governance Auditing: Scope and Evidence ...</a></li>
<li><a href="https://eu.36kr.com/en/p/3934639009372033">10 Trillion Parameter Large Language Models : Why They’re Destined...</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#AI safety`, `#California policy`, `#OpenAI`, `#Anthropic`

---

<a id="item-5"></a>
## [DeepSeek V4.1 Flash: 552B MoE Model Outperforms V4 Pro](https://www.aibase.com/news/30957) ⭐️ 8.0/10

DeepSeek officially released V4.1 Flash, a 552B-parameter Mixture-of-Experts model built on a new asymmetric Causal-Encoder-Decoder architecture with only 8B active parameters for input and 16B for output. The model adds native multimodal vision and, according to DeepSeek, beats its own flagship V4 Pro on benchmarks while cutting HBM usage to roughly one quarter and dramatically lowering inference cost. The release pushes the cost-efficiency frontier for large MoE models, and analysts report the new Causal Encoder-Decoder design cuts cache-hit costs to roughly $0.003 per token — an estimated 80% reduction in agentic workload costs — which could reset pricing across the agent economy. It also signals that DeepSeek is willing to retire its own flagship tier quickly, forcing competitors to compete on efficiency rather than raw parameter count. The asymmetric design means the input path \(8B active parameters\) and output path \(16B active parameters\) are intentionally unequal, which the company credits for a smaller KV cache and lower memory pressure; HBM footprint reportedly drops to a quarter of previous levels. The gains come from new pretraining methods plus larger-scale reinforcement learning post-training, though the claims are vendor-reported and have not yet been independently benchmarked.

aibase · AIbase · Sep 10, 14:01

**Background**: Mixture-of-Experts \(MoE\) models split a large network into many specialized sub-networks \(&\#x27;experts&\#x27;\) and activate only a few per token, so total parameter count can be huge while compute per token stays small. HBM \(High Bandwidth Memory\) is the vertically stacked DRAM used on AI accelerator packages, and its capacity and bandwidth are a major cost and bottleneck for serving large models. Encoder-decoder architectures traditionally encode input into a representation and decode output from it; DeepSeek&\#x27;s &\#x27;asymmetric&\#x27; variant makes those two halves different in size and role, targeting cheaper inference rather than symmetric mirror-image modules. A KV cache stores previously computed attention keys and values so that repeated or long-context requests don&\#x27;t need full recomputation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>
<li><a href="https://forkast.news/deepseeks-new-architecture-slashes-agentic-costs-by-80/">DeepSeek’s New Architecture Slashes Agentic Costs by 80%</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#MoE`, `#AI model release`, `#multimodal`, `#efficiency`

---

<a id="item-6"></a>
## [DeepSeek V4.1 Flash: 552B MoE Multimodal Model Beats Pro on Vision](https://www.aibase.com/news/30955) ⭐️ 8.0/10

DeepSeek has released DeepSeek V4.1 Flash, described as its smallest lightweight multimodal model, built on a 552B-parameter Mixture-of-Experts \(MoE\) architecture with a novel Causal-Encoder-Decoder design. According to the release, its native visual understanding now fully exceeds the Pro version while also improving inference speed and throughput. If the claims hold up, a smaller, cheaper model outperforming a larger Pro-tier sibling on native vision signals a shift in how multimodal capability is scaled — favoring architecture efficiency over raw parameter count, which would lower the cost barrier for AI/ML practitioners deploying vision-language workloads. It also intensifies competition among Chinese labs and the broader open-weight model ecosystem, where DeepSeek has already been pushing aggressive price-performance. Despite being labeled the smallest lightweight model, V4.1 Flash reportedly carries 552B total parameters under a sparse MoE design, so only a subset of experts is activated per token — keeping compute costs far below a dense model of comparable size. DeepSeek claims the architecture has potential to scale to larger models, but independent benchmarks and real-world throughput numbers have not yet been widely verified.

aibase · AIbase · Sep 10, 14:01

**Background**: Mixture-of-Experts \(MoE\) is a machine learning technique in which multiple &\#x27;expert&\#x27; sub-networks divide the problem space, with a routing mechanism activating only a few experts per input; this lets models be pretrained with far less compute than dense models of the same quality. The Causal-Encoder-Decoder design DeepSeek introduces here blends two common paradigms: encoder-decoder models that process input bidirectionally before generating output, and decoder-only models \(the basis of most modern LLMs\) that generate text autoregressively. Applying a causal-style design to multimodal vision input is the core architectural claim behind the efficiency and capability gains.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://www.unite.ai/decoder-based-large-language-models-a-complete-guide/">Decoder -Based Large Language Models: A Complete Guide – Unite.AI</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#multimodal AI`, `#MoE`, `#model release`, `#AI/ML`

---

<a id="item-7"></a>
## [Anthropic blocks AI misuse that could have aided biological weapons](https://www.twincities.com/2026/09/10/anthropic-threat-report/) ⭐️ 7.0/10

Anthropic reported that it detected and blocked attempts to misuse its AI systems for activity that could have supported the development of biological weapons, according to a threat report covered by news outlets. The company framed the blocked activity as a real-world case of misuse prevention rather than a hypothetical risk scenario. The disclosure is significant because it moves the debate over AI-enabled biosecurity risk from speculation to documented enforcement, and it puts pressure on other frontier labs to publish comparable threat data. It matters to policymakers, biosecurity experts, and AI developers evaluating how powerful models should be gated against dual-use misuse. The public account is a news report and does not detail the specific biological techniques, model version, or the number of accounts involved, so the technical severity of the blocked attempt cannot be independently assessed from what was released. Anthropic&\#x27;s approach relies on detection systems and use-policy enforcement, and the company has argued that its safety evaluations are intended to catch such misuse before it escalates.

gdelt · twincities.com · Sep 10, 22:30

**Background**: Anthropic is an AI lab that develops the Claude family of large language models, and like other frontier labs it publishes threat intelligence about how its systems are abused. Frontier models can be dual-use: the same knowledge that helps with legitimate research in biology or chemistry could, in the wrong hands, lower barriers to harmful work such as weapon development. Because of this, labs increasingly use classifiers, monitoring, and account bans, and the topic has become central to AI safety and biosecurity policy discussions worldwide.

**Tags**: `#AI safety`, `#biosecurity`, `#Anthropic`, `#AI misuse`, `#policy`

---

<a id="item-8"></a>
## [Pentagon in Talks to Lend $5B to AI Cloud Startup Fluidstack](https://news.google.com/rss/articles/CBMitwFBVV95cUxNQm56T2dLMnFMeVp3a0tJY2s1eVdLalpSQ2c4bXBGQ2dOclF3a0dCVjhDYldvcEJMbEQ5TUQ5RXJuZXllZ1FvR3phRVlGNHhBazR0LXlaTy1DQmdXUENkQ1hLcWZrZlh0Ni0zdVVhSEhNdGxSckNpbHpiMi1GbUM0aUhSOFluSkZ0aG9WVG9DZ0pzQm13d2ZjRG9hZEZrdFRYUTU3bHoyWmhVYjNXUFN4TGtZRGdXbmM?oc=5) ⭐️ 7.0/10

The Pentagon is reportedly in talks to lend up to $5 billion to Fluidstack, an AI cloud and data center startup, according to a Wall Street Journal report cited by Reuters. The deal, if completed, would mark one of the largest known direct government financings of a private AI infrastructure company. A loan of this size would signal that the US government is moving beyond grants and contracts toward directly bankrolling the AI compute buildout, tying national-security demand to private data center capacity. It could reshape how AI cloud startups finance gigawatt-scale construction and intensify competition with hyperscalers such as AWS, Microsoft and Google for scarce GPU capacity. The talks are reported but not finalized, and no terms, interest rate or timeline have been disclosed. The report comes as Fluidstack is separately said to be in talks for a roughly $1 billion funding round at an $18 billion valuation, and the company says it is leading deployment of Anthropic&\#x27;s $50 billion compute buildout.

google\_news · Reuters · Sep 10, 22:01

**Background**: Fluidstack originated in 2017 as an Oxford University spinout running a marketplace that matched AI compute demand with idle GPU resources, and it now positions itself as building &quot;civilization-scale&quot; AI infrastructure, promising gigawatts of compute deployed within months. AI cloud providers like Fluidstack rent out large clusters of GPUs for training foundation models and running inference, an expensive business that depends on massive upfront capital. The Pentagon has been expanding its AI and cloud programs as part of broader defense modernization, making compute capacity a national-security asset.

<details><summary>References</summary>
<ul>
<li><a href="https://fluidstack.io/">Fluidstack</a></li>
<li><a href="https://www.royco.ai/companies/fluidstack">Fluidstack — Company Profile, Funding &amp; Valuation | Royco</a></li>

</ul>
</details>

**Tags**: `#Pentagon`, `#AI infrastructure`, `#cloud computing`, `#defense funding`, `#Fluidstack`

---

<a id="item-9"></a>
## [Anthropic Says It Blocked Possible Attempts to Use AI for Biological Weapons](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOb3RxODh4LWhOS0o0UFBGNUhHODA0Z2dqbTcyTlFmYVRwRzJVVnhKMFl4U2dqQUQwZXV6d0c1c0gwRHZXeF9wOFRTN2xCengtRnRuR0tJLUNDTlI3VjAyekRzRngwMWY4M01hSUVwWURFUFAxdkRjRC1HZUM3cG9YTnZ4UVFNcVlnT200?oc=5) ⭐️ 7.0/10

Anthropic reported that it detected and blocked potential efforts by users to leverage its AI systems for building biological weapons, according to a New York Times report. The disclosure frames the incidents as misuse attempts that were caught and stopped by the company&\#x27;s safety and monitoring systems. This is one of the clearest public examples of a frontier AI lab reporting concrete biosecurity-related misuse, which could shape how regulators, policymakers, and other AI developers approach mandatory reporting and access controls for dangerous capabilities. It also signals that AI models are increasingly treated as a national-security-relevant technology rather than just a commercial product. The available coverage is a headline-level report with no published technical detail, so the number of accounts involved, the specific model or models, the timeframe, and what exactly the blocked activity entailed remain unclear. Anthropic has not publicly specified whether law enforcement was notified or whether the attempts involved any real-world biological capability beyond requesting information.

google\_news · The New York Times · Sep 10, 21:50

**Background**: Anthropic is an AI company that develops the Claude family of large language models, and like other leading labs it maintains usage policies and monitoring systems intended to prevent misuse of its models. A recurring concern in AI safety research is that large language models could lower barriers to harmful knowledge, including information relevant to creating biological or chemical weapons, which is why labs conduct threat intelligence and red-teaming work. Biosecurity experts and governments have increasingly focused on whether AI could help actors with limited expertise acquire dangerous capabilities, prompting calls for screening, reporting, and stricter safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biosecurity">Biosecurity</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#biosecurity`, `#Anthropic`, `#AI risk`, `#national security`

---

<a id="item-10"></a>
## [OpenAI Shifts Stance, Backs National AI Safety Rules](https://news.google.com/rss/articles/CBMiugFBVV95cUxQLWRvMF9uc0JNaTV5dkthSV9KV0tnODBHUUxnbDlOZzJhYk9aZHZvNVhPLTRkQXpvOE1NNkRXN0Niek5kR0Vwc0FzeWJzRFNMVDd1eGh3RWlzc1RKOXZwTmhpQ3lyZWtJR0xqLW55aU5BSGJzM05zVjkwLXZ2YndNcG1JamVDY1kwY3Z3X3h5Q2dScmF4ZUNYX0NPejZZTTI3NE5ld2hSYlJtakVYazlRVXBydExpMDRVMEE?oc=5) ⭐️ 7.0/10

According to a Baltimore Sun report, OpenAI has changed its position and is now publicly calling for national artificial intelligence safety rules. The move marks a reversal from the company&\#x27;s earlier preference for lighter-touch, industry-led oversight of AI development. As one of the most prominent frontier AI labs, OpenAI&\#x27;s endorsement of national regulation could lend political momentum to federal rulemaking and shape the compliance baseline that other developers, startups, and enterprises must eventually meet. It also intensifies the debate over whether federal rules should override the growing patchwork of state-level AI laws. The available item is only a headline and link, so the specific scope of OpenAI&\#x27;s proposal — such as which agency would enforce the rules, what evaluation or reporting requirements would apply, and whether federal rules should preempt state laws — is not specified. Technically minded readers should treat the announcement as a policy positioning statement rather than a detailed compliance framework.

google\_news · Baltimore Sun · Sep 10, 15:19

**Background**: AI regulation in the United States has largely been split between federal guidance and a fast-growing set of state laws, with proposals ranging from transparency and risk-assessment duties to outright restrictions on certain model training practices. OpenAI previously opposed California&\#x27;s SB 1047 frontier-model safety bill in 2024 and had called for international coordination on regulating superintelligent systems, so its stated preference has often favored broad frameworks over strict state-by-state rules. The European Union&\#x27;s AI Act, which imposes tiered obligations based on model risk, is the most prominent existing example of comprehensive AI regulation and is frequently cited as a template in these debates.

**Tags**: `#AI policy`, `#AI regulation`, `#OpenAI`, `#AI safety`, `#governance`

---