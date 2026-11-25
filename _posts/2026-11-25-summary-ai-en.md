---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25 23:03:35 +0000
lang: en
report: ai
---

> From 156 items, 8 important content pieces were selected

---

1. [Tencent Hunyuan open-sources Hy4 Flash GGUF weights, running a 224B model on a 64GB Mac mini](#item-1) ⭐️ 8.0/10
2. [OpenAI&\#x27;s GPT-6 designs proteins without a specialized biology model, ~10% show binding](#item-2) ⭐️ 8.0/10
3. [Simon Willison maps three LLM inflection points in twelve months](#item-3) ⭐️ 7.0/10
4. [PrismML&\#x27;s Ternary Bonsai 2.5 27B Keeps 93.7% of Coding Ability at One-Ninth the Size](#item-4) ⭐️ 7.0/10
5. [LibreOffice&\#x27;s TDF sets strict AI coding rules requiring disclosure and human understanding](#item-5) ⭐️ 7.0/10
6. [Jensen Huang’s Nvidia Return Reignites Washington Fight Over China Chip Access](#item-6) ⭐️ 6.0/10
7. [EU Reportedly Plans €50 Billion Investment in Artificial Intelligence](#item-7) ⭐️ 6.0/10
8. [Ant Group Releases Medical AI Guard Model MedGuard and Open Risk Dataset](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Tencent Hunyuan open-sources Hy4 Flash GGUF weights, running a 224B model on a 64GB Mac mini](https://www.aibase.com/news/32527) ⭐️ 8.0/10

On November 25, Tencent Hunyuan open-sourced GGUF quantized weights and inference code for its 224B-parameter Hy4 Flash model through its AngelSlim compression toolkit. The release ships four quantization tiers \(Q4\_K\_M, Q3\_K, IQ2-AH and two Spark 4-bit variants\), shrinking the original ~410.27 GiB checkpoint to as little as ~125.73 GiB — about 30% of the original size — with the smallest build running on a 64GB Mac mini via the Strata offload framework. A 224B-class model running locally on consumer hardware — and on a Mac mini at that — marks a notable step for on-device LLM inference, since it moves huge models out of the datacenter and into the hands of individual developers and privacy-sensitive users. The reported score drop of no more than 0.4 points on benchmarks like DeepSWE v1.1 suggests that aggressive low-bit quantization is no longer necessarily a large quality sacrifice. The intermediate Q3\_K build occupies roughly 144.70 GiB, and measured throughput includes 89 tokens/s at 10K context on a 48GB VRAM device and 47 tokens/s at 32K context with Q3\_K on a 128GB M5 Max. The catch is that only the very smallest tiers can fit a 64GB machine, and then only by streaming weights through Strata&\#x27;s offload mechanism, so users should expect far lower token rates than the VRAM figures above.

aibase · AIbase · Nov 25, 16:01

**Background**: GGUF is the file format used by llama.cpp and many other local inference engines to store quantized model weights; its naming scheme, such as Q4\_K\_M or IQ2, indicates how many bits are spent per weight, with k-quants using block-wise scaling and i-quants using more aggressive codebook-style compression. Lower-bit files are much smaller and faster to load but typically lose accuracy, which is why vendor-published size/quality tables matter. AngelSlim is Tencent Hunyuan&\#x27;s model compression toolkit, which consolidates quantization, speculative decoding, token pruning and distillation. Offload frameworks like Strata keep only active layers in GPU memory and spill the rest to system RAM or NVMe, which is how a model far larger than available memory can still generate tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent/AngelSlim">GitHub - Tencent / AngelSlim : Model compression toolkit engineered...</a></li>
<li><a href="https://stratallm.org/">Strata LLM – Run 125B+ MoE Models on 12GB VRAM Consumer GPUs ...</a></li>
<li><a href="https://www.myaihardware.com/deep-dive/gguf-quantization-formats-complete-guide-k-quants-i-quants">GGUF Quantization Formats | MyAIHardware</a></li>

</ul>
</details>

**Tags**: `#LLM quantization`, `#GGUF`, `#Tencent Hunyuan`, `#local inference`, `#open-source AI`

---

<a id="item-2"></a>
## [OpenAI&\#x27;s GPT-6 designs proteins without a specialized biology model, ~10% show binding](https://www.aibase.com/news/32513) ⭐️ 8.0/10

On November 24, OpenAI released a preprint exploring whether general chat models can stand in for specialized biological models, reporting that the GPT-6 series can design protein three-dimensional structures and amino acid sequences using only reasoning and general-purpose coding tools. In a collaboration with Onava, 322 miniature binding proteins built from GPT-6.2 designs and covering five targets were taken from computation into wet-lab experiments, with roughly 10% showing evidence of binding. This suggests that broad reasoning models may be able to absorb tasks that until now required dedicated protein-design systems, potentially lowering the barrier for labs that lack specialized structural-biology tooling. It also heats up a brewing competition between frontier AI labs — Anthropic has made similar claims for Claude — over whether general models can do real biological design work. The roughly 10% binding rate is modest and sits near the commonly cited 10–15% human baseline for binder design campaigns, well below the 35% success rate Anthropic claimed for Claude-designed proteins, though these figures come from different targets, assays and screening methods. OpenAI also says redesigned antibodies retained binding, and the report so far rests on a preprint plus a company blog post rather than a peer-reviewed paper.

aibase · AIbase · Nov 25, 11:01

**Background**: Proteins are chains of amino acids that fold into three-dimensional shapes, and &\#x27;binding proteins&\#x27; or &\#x27;binders&\#x27; are small proteins engineered to attach tightly to a specific target molecule — the basis for many drugs and diagnostics. Miniature binding proteins are short scaffold proteins that are cheaper to synthesize and easier to engineer than full antibodies. De novo design of such binders has historically relied on physics-based tools like Rosetta or specialized deep-learning systems such as RFdiffusion and ProteinMPNN, which is why a general chat model doing this with plain reasoning and code is notable.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT-6 models demonstrate intrinsic protein - design ... | OpenAI</a></li>
<li><a href="https://www.nature.com/articles/s41586-022-04654-9">Design of protein-binding proteins from the target structure ...</a></li>
<li><a href="https://admix.software/blog/claude-protein-design-wet-lab">Claude Designed Disease-Targeting Proteins That... | Admix Blog</a></li>

</ul>
</details>

**Tags**: `#AI biology`, `#protein design`, `#GPT-6`, `#LLM reasoning`, `#wet-lab validation`

---

<a id="item-3"></a>
## [Simon Willison maps three LLM inflection points in twelve months](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 7.0/10

Simon Willison published a retrospective built around his AI Engineer Code Summit keynote, arguing that the past twelve months contained three major inflection points in LLM and coding-agent capability. He dates the first to November 24, 2025, the release of Claude Opus 4.5 — exactly one year before the post — which he says was the first model that made Claude Code reliably correct by default. Willison is one of the most closely read voices on LLM tooling, and his framing gives developers a vocabulary for judging new models instead of just tracking benchmark charts. The claim that a single model release turned a coding agent from a chore into a genuine accelerant speaks directly to how quickly AI-assisted software development has shifted from novelty to daily workflow. Willison notes that Opus 4.5 landed in the same month as OpenAI&\#x27;s GPT-5.1 Instant, GPT-5.1 Thinking, GPT-5.1-Codex and GPT-5.1-Codex-Max, which had a similar effect on the Codex agent, and that the December holidays gave people time to experiment before adopting the tools for real work in January. He defines &quot;Fable class models&quot; as systems that, once you state a goal and supply the necessary tools, can solve the problem through brute force — citing Claude Fable spinning up its own pyobjc-framework-Quartz screenshot mechanism and a CORS-enabled localhost logging server to debug a Safari display glitch.

rss · Simon Willison · Nov 24, 23:02

**Background**: Claude Code is Anthropic&\#x27;s terminal-based coding agent, introduced on February 24, 2025 alongside Claude 3.7 Sonnet — meaning it was about nine months old when Opus 4.5 shipped. Anthropic&\#x27;s Claude models are generally released in three tiers named Haiku, Sonnet and Opus, with Opus being the most capable. According to Willison&\#x27;s account, Anthropic announced Claude Mythos in April 2026 but withheld it from general release because its improved cybersecurity skills let it both find and exploit vulnerabilities; Claude Fable 5 was the safeguarded version eventually shipped to the public.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4.5">Claude Opus 4.5</a></li>
<li><a href="https://grokipedia.com/page/Comparison_of_Claude_Opus_45_and_Grok_Code_Fast_1">Comparison of Claude Opus 4.5 and Grok Code Fast 1</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#coding agents`, `#AI engineering`, `#Claude Opus`, `#retrospective`

---

<a id="item-4"></a>
## [PrismML&\#x27;s Ternary Bonsai 2.5 27B Keeps 93.7% of Coding Ability at One-Ninth the Size](https://www.aibase.com/news/32522) ⭐️ 7.0/10

PrismML released Ternary Bonsai 2.5 27B, an upgrade to its September Bonsai 2 27B built on Qwen3.8 27B, in which every language-model weight is ternary \(-1, 0, +1\). The model keeps the same 5.9GB footprint — roughly one-ninth of a 53.8GB full-precision model — while scoring 75.6 on SWE-bench Verified versus 80.6 for the full-precision baseline, retaining about 93.7% of agentic coding performance. The result suggests that extreme 1.58-bit-style quantization can preserve most real-world coding-agent capability, making a 27B-class agentic model practical on consumer hardware and on-device tools where 5.9GB of memory is affordable but 54GB is not. If it holds up, this narrows the gap between compressed local models and full-precision server deployments for private-repository and tool-use workflows. According to PrismML&\#x27;s documentation, the underlying hybrid-attention architecture is unchanged from Qwen3.8-27B, and each ternary weight carries an FP16 scale per group of 128, so the compression comes from weight precision rather than structural pruning. The 75.6 vs 80.6 gap means roughly 6.3% of coding performance is lost, and the company positions the release specifically around multi-turn tool use and multi-step task execution rather than raw benchmark parity.

aibase · AIbase · Nov 25, 15:01

**Background**: Ternary quantization is an extreme compression technique that constrains each model weight to one of just three values, -1, 0 or +1, instead of the wide range used by 4-bit or 8-bit integer formats; because log2\(3\) is about 1.58, it is often called 1.58-bit. Standard 16-bit models store each weight with far more precision, so ternary models can shrink memory roughly an order of magnitude, but they typically require quantization-aware training or careful scaling to avoid accuracy collapse. SWE-bench Verified is a human-validated subset of 500 real GitHub issue tasks, and it is the most-cited benchmark for AI coding agents because each task requires reading a real codebase, writing a patch and passing the project&\#x27;s test suite.

<details><summary>References</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-2-5-27b">PrismML — Introducing Ternary Bonsai 2.5 27B: Powering ...</a></li>
<li><a href="https://docs.prismml.com/models/bonsai-2-5-27b">Ternary Bonsai 2.5 27B - Bonsai - docs.prismml.com</a></li>
<li><a href="https://www.swebench.com/verified.html">SWE-bench Verified</a></li>

</ul>
</details>

**Tags**: `#LLM compression`, `#ternary quantization`, `#coding agents`, `#SWE-bench`, `#model efficiency`

---

<a id="item-5"></a>
## [LibreOffice&\#x27;s TDF sets strict AI coding rules requiring disclosure and human understanding](https://www.aibase.com/news/32515) ⭐️ 7.0/10

The Document Foundation \(TDF\), the maintainer of LibreOffice, has introduced strict new rules regulating large language models and AI-assisted programming. The core requirement is that developers must not only disclose their use of AI but also understand every line of code, passing a human explanation gate before AI-assisted code is accepted. This is a notable governance policy from a major open-source project, and it could set a precedent for how other projects handle AI-generated contributions. It directly addresses risks such as black-box logic, hard-to-maintain code, insufficient review, and unclear human accountability in open-source development. The policy does not appear to ban AI-assisted coding outright; instead, it imposes disclosure and human-understanding obligations on contributors. A technically minded reader should note that enforcement details, such as how the human explanation gate is reviewed and what evidence of understanding is required, are not fully specified in the announcement.

aibase · AIbase · Nov 25, 11:01

**Background**: The Document Foundation is a non-profit organization that supports the development of LibreOffice, a free and open-source office suite. Large language models are increasingly used in software engineering for code generation, but research and practitioner experience point to risks around maintainability, security, hallucinations, and licensing. Many open-source projects have therefore begun adopting AI contribution policies that require disclosure, human sign-off, and maintainer review.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/The_Document_Foundation">The Document Foundation - Wikipedia</a></li>
<li><a href="https://kindatechnical.com/open-source-contribution/ai-contribution-policies.html">Project Policies on AI-Generated Contributions - kindatechnical()</a></li>
<li><a href="https://arxiv.org/abs/2601.20879">[2601.20879] A Survey on Large Language Model Impact on ... SE Perspective on LLMs: Biases in Code Generation, Code ... How secure is AI-generated code: a large-scale comparison of ... Scalable code generation with large language models: an open ... A dual perspective review on large language models and code ... Quality assurance of LLM-generated code: Addressing non ...</a></li>

</ul>
</details>

**Tags**: `#open source`, `#LibreOffice`, `#AI-assisted programming`, `#code quality`, `#governance`

---

<a id="item-6"></a>
## [Jensen Huang’s Nvidia Return Reignites Washington Fight Over China Chip Access](https://www.thenews.com.pk/latest/1425062-jensen-huangs-return-to-nvidia-reignites-washington-fight-over-chinas-chip-access) ⭐️ 6.0/10

Jensen Huang’s return to Nvidia has reignited a Washington policy fight over China’s access to the company’s advanced AI chips. The renewed debate comes as U.S. officials tighten restrictions on how Chinese firms can obtain Nvidia processors through third countries such as those in Southeast Asia. Nvidia is the central supplier of AI accelerators, so U.S. export-control decisions directly shape the global AI race, Nvidia’s revenue prospects, and the computing options available to Chinese AI labs. Huang’s return puts a high-profile CEO back at the center of a debate that affects chipmakers, cloud providers, and governments well beyond Washington. The policy fight is unfolding alongside separate scrutiny of how restricted Nvidia accelerators reach China, with analysts estimating that more than 1.5 GW of banned hardware was tracked there in recent years. Nvidia’s board is also reportedly investigating whether Huang was the target of a foreign intelligence effort, adding a security dimension to the export-control debate.

gdelt · thenews.com.pk · Nov 25, 14:15

**Background**: Nvidia is the leading supplier of GPUs used to train and run AI models, and its most advanced accelerators are subject to U.S. export controls intended to limit China’s AI and military capabilities. Washington has repeatedly expanded those rules, including curbs on third-country transshipment, while Nvidia has sought to design compliant chips for the Chinese market. Jensen Huang’s public stance and his meetings in Washington are closely watched because they can signal whether enforcement or engagement will dominate U.S. policy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1">Alice Huang’s links to the chip underworld</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/mass-smuggling-of-nvidia-ai-gpus-could-be-the-underlying-cause-of-jensen-huangs-departure-analysts-claim-more-than-1-5-gigawatts-of-banned-chips-tracked-to-china-despite-export-controls">Mass smuggling of up to 1.5 million Nvidia AI GPUs... | Tom&#x27;s Hardware</a></li>
<li><a href="https://www.businessinsider.com/jensen-huang-china-stance-comments-nvidia-spying-probe-2026-11">What Jensen Huang Has Said About China As... - Business Insider</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#China chip access`, `#export controls`, `#AI hardware`, `#US policy`

---

<a id="item-7"></a>
## [EU Reportedly Plans €50 Billion Investment in Artificial Intelligence](https://www.diariolibre.com/mundo/europa/2026/11/25/ue-planea-invertir-50000-millones-de-euros-en-inteligencia-artificial/3731128) ⭐️ 6.0/10

The European Union is reportedly preparing a €50 billion investment plan aimed at artificial intelligence, according to a report from Diario Libre. The announcement, if confirmed, would represent one of the largest single public funding commitments to AI in Europe to date. A public commitment of this size signals that Brussels intends to treat AI capacity as strategic infrastructure rather than a purely private-sector matter. It could reshape funding for European AI startups, research labs and compute infrastructure, and influence how the bloc positions itself against the United States and China in the global AI race. Details remain scarce: the report does not specify a timeline, budget breakdown, funding instruments, or which programs would receive the money. It is also unclear whether the €50 billion would be new spending or a repackaging of existing EU research and digital programs, so the figures should be treated as preliminary until official documentation is published.

gdelt · diariolibre.com · Nov 25, 14:15

**Background**: The European Union has been building out its AI policy framework through measures such as the AI Act, the first comprehensive law regulating AI systems by risk level, and through programs that fund research and high-performance computing. Despite strong academic research, Europe has lagged the US and China in producing large-scale AI models and in private investment, which has fueled a policy debate about whether public money should close that gap. Large public funding packages of this kind are typically channeled through multi-year EU budget frameworks or joint initiatives with member states and industry.

**Tags**: `#AI policy`, `#EU funding`, `#artificial intelligence`, `#investment`, `#technology governance`

---

<a id="item-8"></a>
## [Ant Group Releases Medical AI Guard Model MedGuard and Open Risk Dataset](https://www.aibase.com/news/32523) ⭐️ 6.0/10

On November 25, Ant Group released LingSante MedGuard, a medical AI safety guard model, and opened a risk evaluation dataset aimed at catching domain-specific medical failure modes such as lab values being assigned to the wrong test or hidden errors propagating through clinical outputs. Medical AI is increasingly used for patient consultation and clinical decision support, where generic guardrails may miss incorrect medical scores, unsupported clinical claims, or inapplicable guidelines. A domain-specific medical guard model and open risk evaluation set could help developers and providers test and constrain these systems before deployment. MedGuard is described as a capability-enhanced unified medical guardrail that learns from a medical guardrail teacher and six specialized medical capability experts, producing Safe/Unsafe judgments with supporting reasons across medical safety, compliance, and ethics. It is designed to check clinical claims against evidence, verify calculations, and apply medical requirements under their intended conditions, though public details on model size, license, and benchmark results remain limited.

aibase · AIbase · Nov 25, 15:01

**Background**: Guardrails are safety layers that screen AI inputs and outputs to block harmful, non-compliant, or otherwise risky responses, but general-purpose guardrails are not built to verify clinical evidence, medical calculations, or guideline applicability. Ant Group’s LingSante family is a set of medical AI models; MedGuard focuses specifically on medical-safety, regulatory-compliance, and bioethics risks, while companion models such as LingSante-Pulse target broader health-risk assessment.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.25509">[2611.25509] LingSante MedGuard Technical Report - arXiv.org</a></li>
<li><a href="https://arxiv.org/pdf/2611.25509">LingSante MedGuard Technical Report - arXiv.org</a></li>
<li><a href="https://www.unite.ai/ant-group-begins-open-weight-release-of-lingsante-medical-ai-models/">Ant Group Begins Open-Weight Release of LingSante Medical AI ...</a></li>

</ul>
</details>

**Tags**: `#Medical AI`, `#AI Safety`, `#Guardrails`, `#Evaluation Dataset`, `#Ant Group`

---