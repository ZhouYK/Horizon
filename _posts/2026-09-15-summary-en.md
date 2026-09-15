---
layout: default
title: "Horizon Summary: 2026-09-15 (EN)"
date: 2026-09-15 23:04:07 +0000
lang: en
report: default
---

> From 188 items, 7 important content pieces were selected

---

1. [Sanders Bill Would Ban Superintelligent AI, With 20-Year Prison Terms](#item-1) ⭐️ 8.0/10
2. [MediaTek unveils Dimensity 9600 Pro, first phone chip on TSMC 2nm](#item-2) ⭐️ 8.0/10
3. [Project Lily: OpenAI Contractors Read Real ChatGPT Chats](#item-3) ⭐️ 8.0/10
4. [Data fears push Nvidia, Palantir and Booz Allen to restrict AI model use](#item-4) ⭐️ 7.0/10
5. [China Issues 15th Five-Year Plan for Electronics Manufacturing](#item-5) ⭐️ 7.0/10
6. [Google Opens Anthropic&\#x27;s Claude to All Engineers Internally](#item-6) ⭐️ 7.0/10
7. [Gemini distillation service lets a teacher model train a student model](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Sanders Bill Would Ban Superintelligent AI, With 20-Year Prison Terms](https://www.techspot.com/news/113831-new-bernie-sanders-bill-would-ban-superintelligent-ai.html) ⭐️ 8.0/10

US Senator Bernie Sanders and a House co-sponsor have introduced the &quot;Ban Artificial Superintelligence Act,&quot; which would permanently prohibit the development and deployment of superintelligent AI and pause advanced AI development until federal regulators establish safety rules. Violators would face up to 20 years in prison, while companies could face a &quot;corporate death penalty&quot; in the form of forced dissolution. Although it is only a proposal rather than enacted law, the bill pushes the idea of banning superintelligence into mainstream US federal politics, potentially shaping the terms of the AI regulation debate and pressuring frontier labs and lawmakers to take a position. It also calls for an international agreement to block superintelligence globally, which would directly affect the most advanced AI developers if it ever gained traction. Beyond the ban and criminal penalties, the bill would create a cabinet-level agency to monitor dangerous capabilities in frontier AI systems at every stage of development and to oversee the removal of those capabilities. It remains a legislative proposal, so its prospects for passage and its exact final text are still uncertain.

telegram · zaihuapd · Sep 15, 04:26

**Background**: Superintelligence refers to a hypothetical AI agent whose intellect surpasses that of the most gifted human minds; no such system exists today. &quot;Frontier AI&quot; describes the most advanced general-purpose models available at any given moment, which is the class of systems such a bill would target. AI safety research studies risks ranging from accidental failures to deliberate misuse, and proposals to ban or pause superintelligence development have been debated by researchers and policymakers for years.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence">Superintelligence - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/artificial-superintelligence">What Is Artificial Superintelligence? - IBM</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#AI safety`, `#superintelligence`, `#policy`, `#tech governance`

---

<a id="item-2"></a>
## [MediaTek unveils Dimensity 9600 Pro, first phone chip on TSMC 2nm](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 8.0/10

On September 15, MediaTek launched the Dimensity 9600 Pro, its first smartphone processor manufactured on TSMC&\#x27;s 2nm process, alongside a second chip, the 3nm Dimensity 9600M. MediaTek says the 9600 Pro packs a dedicated AI processor that improves the performance of handling user prompts — the stage before the model starts generating output — by 51% over the previous generation, and that the first phones using both chips will go on sale soon. This marks the arrival of TSMC&\#x27;s 2nm node in the flagship smartphone segment, putting MediaTek among the first to ship a 2nm mobile chip and raising competitive pressure on Qualcomm and Apple in the Android flagship market. It also reflects the industry&\#x27;s push to run large language models locally on phones, where AI prompt processing speed directly shapes how responsive on-device assistants feel. The headline 51% figure refers specifically to prompt processing, also called prefill — the compute-bound first phase of LLM inference in which the whole prompt is processed in one parallel pass to build the KV cache — rather than to token generation speed. It is worth noting that &quot;2nm&quot; is a marketing node name with no direct relation to any actual physical feature size, and MediaTek has not yet disclosed clock speeds, core configuration, or which smartphone makers will use the chips first.

telegram · zaihuapd · Sep 15, 08:57

**Background**: Chip process nodes such as 3nm and 2nm describe successive generations of semiconductor manufacturing technology; TSMC&\#x27;s 2nm node \(N2\) is its most advanced production process and is expected to keep the company ahead of Samsung and Intel for several years. Modern smartphone chips pair general CPU and GPU cores with a neural processing unit \(NPU\), a specialized accelerator for AI workloads such as running language models on the device. On-device inference happens in two phases: prefill \(prompt processing, which is compute-bound\) and decode \(token generation, which is memory-bandwidth-bound\), so a large prefill speedup mainly improves how quickly an assistant begins responding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_processing_unit">Neural processing unit - Wikipedia</a></li>
<li><a href="https://www.runlocalai.co/glossary/prefill">Prefill ( Prompt Processing ) — AI glossary</a></li>

</ul>
</details>

**Tags**: `#MediaTek`, `#Dimensity 9600 Pro`, `#TSMC 2nm`, `#mobile chips`, `#AI processors`

---

<a id="item-3"></a>
## [Project Lily: OpenAI Contractors Read Real ChatGPT Chats](https://www.404media.co/inside-project-lily-the-humans-reading-your-chatgpt-chats/) ⭐️ 8.0/10

404 Media reported that OpenAI is employing hundreds of contractors under an internal program code-named &quot;Project Lily&quot; to read a massive stream of real users&\#x27; ChatGPT prompts and full conversations, rating the model&\#x27;s replies and suggesting corrections. OpenAI confirmed it tries to strip personal information before handing data to reviewers but admits sensitive details may still be visible, and Anthropic acknowledged it likewise uses human review to improve its models. The report exposes a common but rarely discussed practice across the AI industry: real user conversations, not just synthetic or opted-in data, are being read by human workers to fine-tune model behavior. It raises significant privacy and AI-ethics questions about what users implicitly consent to when they chat with an assistant, and could invite regulatory scrutiny over data handling and the labor conditions of contract annotation workers. The reviewers work as contractors rather than full-time employees, and their job is to grade model responses and propose improvements — a workflow central to how large language models are refined. OpenAI stresses that it attempts to remove personal information before review, but its own acknowledgement that sensitive details can slip through means the anonymization is imperfect rather than guaranteed.

telegram · zaihuapd · Sep 15, 11:56

**Background**: Large language models like ChatGPT are typically improved through human feedback: people read or compare model outputs, rate them and flag problems, and those judgments are used to fine-tune the model so it becomes safer and more helpful. This kind of work is part of the broader &quot;data labeling&quot; industry, in which a largely contract-based workforce annotates text, audio and images for AI developers. Because real conversations are the most representative of actual usage, companies often prefer them over synthetic examples — but that also means private user content can flow into the review pipeline.

<details><summary>References</summary>
<ul>
<li><a href="https://www.404media.co/inside-project-lily-the-humans-reading-your-chatgpt-chats/">Inside ‘ Project Lily ’: The Humans Reading Your ChatGPT Chats</a></li>
<li><a href="https://insightsintegration.com/project-lily-explained-why-openai-contractors-are-reviewing-chatgpt-conversations/">Project Lily Explained: Why OpenAI Contractors... - Insights Integration</a></li>
<li><a href="https://aiweekly.co/alerts/404-media-openai-project-lily-hires-hundreds-of-contractors-to-read-real">404 Media: OpenAI &#x27; Project Lily &#x27; Hires Hundreds of... | AI Weekly</a></li>

</ul>
</details>

**Tags**: `#AI privacy`, `#OpenAI`, `#data labeling`, `#AI ethics`, `#content moderation`

---

<a id="item-4"></a>
## [Data fears push Nvidia, Palantir and Booz Allen to restrict AI model use](https://www.theinformation.com/articles/anthropic-data-fears-prompt-nvidia-palantir-booz-allen-restrict-model-use) ⭐️ 7.0/10

Nvidia, Palantir and Booz Allen Hamilton have begun restricting or scaling back their use of AI models from Anthropic and other vendors, and are demanding contractual assurances that suppliers will not misuse customer data. The move reflects rising corporate anxiety that model providers could learn from, retain, or otherwise expose clients&\#x27; proprietary information. These are three of the most technically sophisticated and defense-adjacent enterprises in the United States, so their reluctance signals real friction in enterprise AI adoption and eroding trust between model vendors and large customers. If more sensitive-industry firms follow, it could slow third-party model deployment, favor self-hosted or open-weight alternatives, and put pressure on vendors to offer stronger zero-retention guarantees. The restrictions appear to apply specifically to models used for sensitive business work rather than all AI usage, with the core concerns being data retention policies and the risk that a vendor could indirectly learn from customer intellectual property. Notably, the friction is not about model capability or performance but about data governance contracts, meaning even a technically superior model may fail enterprise procurement on trust grounds alone.

telegram · zaihuapd · Sep 15, 01:02

**Background**: Large language model vendors typically log customer prompts and outputs by default, often retaining them for around 30 days for abuse monitoring and sometimes using them to improve future models. Enterprises handling trade secrets, defense work, or regulated data worry this pipeline constitutes intellectual property leakage, since inputs and AI-generated outputs can both expose confidential information. In response, some vendors now offer zero data retention agreements or self-hosted deployment options, but these often come with higher cost, reduced feature sets, or stricter contractual negotiation. The dispute illustrates a broader tension in enterprise AI: capability gains are increasingly easy to buy, while enforceable data guarantees remain hard to secure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.teleskope.ai/post/zero-data-retention">Zero Data Retention: What It Means for AI Security | Teleskope Blog</a></li>
<li><a href="https://gimmal.com/data-retention-policies-in-the-ai-era-whats-changing/">Data Retention Policies in the AI Era: What&#x27;s Changing? - Gimmal</a></li>
<li><a href="https://www.stradlinglaw.com/news-insights/the-data-defense-dilemma-protecting-trade-secrets-from-internal-ai-leakage.html">Protecting Trade Secrets from Internal AI Leakage - Stradling</a></li>

</ul>
</details>

**Tags**: `#AI privacy`, `#enterprise AI`, `#data governance`, `#Anthropic`, `#model adoption`

---

<a id="item-5"></a>
## [China Issues 15th Five-Year Plan for Electronics Manufacturing](https://www.secrss.com/articles/93961) ⭐️ 7.0/10

China&\#x27;s Ministry of Industry and Information Technology \(MIIT\) and the National Development and Reform Commission \(NDRC\) jointly issued the 15th Five-Year Plan for the electronic information manufacturing industry, setting out 17 key tasks. The plan calls for improving advanced process node capabilities, achieving breakthroughs in high-end smartphone core chips and high-performance PC chips, and expanding the adoption of domestic operating systems such as OpenHarmony, while also promoting RISC-V, AI chips and terminals, and BeiDou-related development. As a top-level national planning document, it signals that China will keep directing state resources toward semiconductor self-sufficiency and domestic OS adoption through 2030, shaping investment and procurement decisions across chip design, foundry, and software ecosystems. Companies in the semiconductor supply chain, handset and PC makers, and OpenHarmony/RISC-V developers are the most directly affected, and the plan&\#x27;s emphasis on domestic operating systems could accelerate divergence from the Android/Windows-dominated global stack. The plan sets quantitative targets for 2030, including operating revenue of large-scale enterprises exceeding 30 trillion yuan and an R&amp;D investment intensity of 3.5%. It bundles advanced process capability, high-end mobile and PC chips, domestic OS adoption, RISC-V, AI chips, and BeiDou into one 17-task framework, but remains a planning document rather than a concrete technical breakthrough or shipped product.

telegram · zaihuapd · Sep 15, 03:10

**Background**: China&\#x27;s Five-Year Plans are top-level government blueprints that set priorities for the following five years; the &quot;15th Five-Year Plan&quot; covers 2026–2030, and these documents strongly influence subsidies, state procurement, and industrial policy. OpenHarmony is an open-source operating system derived from Huawei&\#x27;s HarmonyOS and donated to the OpenAtom Foundation, positioned as a domestic alternative to Android in phones, IoT, and industrial devices. RISC-V is a free, open instruction set architecture originally developed at UC Berkeley that allows chip designers to build processors without licensing fees, making it attractive for reducing reliance on foreign IP. Advanced process nodes such as 7nm, 5nm, and 3nm refer to semiconductor fabrication generations defined by shrinking transistor feature sizes, and China&\#x27;s access to these nodes has been restricted by export controls.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenHarmony">OpenHarmony - Wikipedia</a></li>
<li><a href="https://riscv.org/">Home - RISC - V International</a></li>
<li><a href="https://openharmonyos.org/">OpenHarmony OS Research</a></li>

</ul>
</details>

**Tags**: `#China-tech-policy`, `#semiconductors`, `#OpenHarmony`, `#RISC-V`, `#AI-chips`

---

<a id="item-6"></a>
## [Google Opens Anthropic&\#x27;s Claude to All Engineers Internally](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 7.0/10

Google has opened Anthropic&\#x27;s Claude Opus 5, its most capable coding model, to engineers company-wide for internal development, but only through Google&\#x27;s internal Antigravity platform. Previously Google barred most employees from using external coding tools such as Claude Code and OpenAI&\#x27;s Codex, requiring them to use its own Gemini instead. This is a notable reversal of a long-standing internal policy and a signal that even a frontier lab with its own flagship model feels competitive pressure in AI coding tools. It is especially striking because Google is a major Anthropic investor, having announced plans earlier this year to invest up to $40 billion in the company, so the move blurs the line between competitor and backer. Claude access is provided as a per-employee quota and framed as a supplement, while Google says Gemini remains the primary model for internal development. Access is also constrained to the Antigravity platform rather than being a free-for-all on any external tool, which keeps Google&\#x27;s internal workflow and data within its own environment.

telegram · zaihuapd · Sep 15, 05:31

**Background**: Anthropic&\#x27;s Claude is a family of large language models, with Claude Opus 5 positioned as its most capable model for coding and complex knowledge work, and Claude Code as an AI-driven coding assistant that can work across an entire codebase. Google Antigravity, launched in late 2025 alongside the Gemini 3 model, is Google&\#x27;s AI-powered integrated development environment \(IDE\) that lets developers manage agents at a higher, task-oriented level. Google has invested heavily in Anthropic even while competing with it through Gemini, making the relationship both collaborative and rivalrous.

<details><summary>References</summary>
<ul>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>
<li><a href="https://enter.converge.ai/zh/blog/what-is-google-antigravity">什 么 是 Google Antigravity ？ 2026 年 AI 编程工具详解 | Enter</a></li>
<li><a href="https://code.claude.com/docs/zh-TW/overview">概述- Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#AI coding tools`, `#Google`, `#Anthropic`, `#Claude`, `#industry news`

---

<a id="item-7"></a>
## [Gemini distillation service lets a teacher model train a student model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/distillation?hl=zh-cn) ⭐️ 6.0/10

Google Cloud&\#x27;s Gemini distillation service now lets a larger teacher model generate answers and reasoning traces that are used to train a smaller student model, reducing latency and cost. During the early-access period it supports gemini-3.1-pro as the teacher and gemini-2.5-flash as the student. Managed distillation lowers the barrier for teams that want to keep Gemini-quality behavior while cutting inference latency and cost, which is a key concern as enterprises move LLM workloads from prototypes into production. It also signals that major cloud vendors are productizing optimization techniques that previously required custom, self-managed training pipelines. Adoption is gated: a project must be added to an allowlist and run in the us-central1 region, and the dataset must be a JSONL prompt set stored in Cloud Storage. Only text input is supported, so multimodal distillation is not available yet.

telegram · zaihuapd · Sep 15, 05:57

**Background**: Distillation is a long-standing machine-learning technique in which a large, expensive &quot;teacher&quot; model transfers its knowledge to a smaller &quot;student&quot; model, which then handles inference at lower latency and cost. Traditionally this required teams to build their own training infrastructure; cloud-managed versions package that pipeline as a service. JSONL is a common text-based data format in which each line is a separate JSON object, widely used for large machine-learning datasets and logs.

<details><summary>References</summary>
<ul>
<li><a href="https://labelyourdata.com/articles/machine-learning/model-distillation">Model Distillation : Teacher-Student Training Guide... | Label Your Data</a></li>
<li><a href="https://mayurji.github.io/blog/2022/10/22/Knowledge-Distillation">Knowledge Distillation, aka. Teacher - Student Model</a></li>
<li><a href="https://jsonltools.com/what-is-jsonl">What Is JSONL? Format, Examples &amp; Uses [2026]</a></li>

</ul>
</details>

**Tags**: `#Model Distillation`, `#Gemini`, `#Google Cloud`, `#LLM Optimization`, `#Model Training`

---