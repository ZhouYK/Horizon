---
layout: default
title: "Horizon Summary: 2026-08-29 (EN)"
date: 2026-08-29 04:33:53 +0000
lang: en
report: ai
---

> From 292 items, 10 important content pieces were selected

---

1. [Tencent Open-Sources Hunyuan Hy4 Preview: 770B Parameters, 1M Context](#item-1) ⭐️ 9.0/10
2. [Tencent Hunyuan Open-Sources Hy4preview: 770B MoE with 1M Context](#item-2) ⭐️ 9.0/10
3. [Rumor of a bug is enough for AI agents to find exploits, OCaml maintainer finds](#item-3) ⭐️ 8.0/10
4. [Anthropic&\#x27;s new framework lets AI agents control hardware](#item-4) ⭐️ 8.0/10
5. [Tencent WorkBuddy Integrates Hunyuan Hy4 Preview, Free Trial Launches](#item-5) ⭐️ 8.0/10
6. [Tencent Open-Sources 770B-Parameter Hunyuan Hy4preview Model](#item-6) ⭐️ 8.0/10
7. [Anthropic Launches Model Hardware Standard MHS for AI Physical Control](#item-7) ⭐️ 8.0/10
8. [Anthropic Launches Model Hardware Standard for Physical AI](#item-8) ⭐️ 8.0/10
9. [Midjourney V8.2 Beta Adds Image Editing with Instruction Fine-Tuning](#item-9) ⭐️ 8.0/10
10. [116 Tech Giants Warn AI Cyber Attacks to Surge, Urge Prioritizing Defense](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Tencent Open-Sources Hunyuan Hy4 Preview: 770B Parameters, 1M Context](https://www.aibase.com/news/30698) ⭐️ 9.0/10

Tencent released the Hunyuan Hy4 preview as an open-source model with 770B total parameters \(49B active\) and a 1 million-token context window, claiming top-tier performance among open-source models. It is now available on Hugging Face, GitHub, ModelScope, GitCode, and integrated with Tencent Cloud TokenHub and OpenRouter. This release pushes the frontier of open-source LLMs by combining massive scale \(770B params\) with an extremely long context window, making it competitive with proprietary models. Developers and enterprises gain access to a state-of-the-art model through multiple major platforms, potentially accelerating AI adoption in Chinese and global markets. The model uses a Mixture-of-Experts \(MoE\) architecture, activating only 49B of 770B parameters per token to save computation. According to Tencent, blind tests show Hunyuan Hy4 beats GLM-5.3 and Kimi K3 in productivity, and it is accessible via OpenAI-compatible and Anthropic-compatible endpoints on TokenHub.

aibase · AIbase · Aug 28, 15:27

**Background**: Mixture-of-Experts \(MoE\) models divide their parameters into specialized &\#x27;experts&\#x27; and activate only a small subset per input, allowing a large total parameter count without proportional compute costs. Context length in LLMs refers to the maximum number of tokens the model can process at once, acting like short-term memory; a 1 million-token context lets the model handle entire codebases or long documents in a single pass. Tencent Cloud TokenHub is a unified LLM gateway that provides a single API key to access multiple models, including Tencent&\#x27;s Hunyuan series.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/ramses-engineering/not-one-brain-but-many-how-mixture-of-experts-moe-makes-ai-smarter-and-faster-568f41220852">Not One Brain, But Many: How Mixture of Experts ( MoE ) Makes AI ...</a></li>
<li><a href="https://daring-contributors-828702.framer.app/blog/ai-context-making-the-most-out-of-your-llm-context-length">Context length in LLMs: how to make the most out of it</a></li>
<li><a href="https://litellm.vercel.app/docs/providers/tencent">Tencent TokenHub | liteLLM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#open-source`, `#Tencent`, `#Hunyuan`

---

<a id="item-2"></a>
## [Tencent Hunyuan Open-Sources Hy4preview: 770B MoE with 1M Context](https://www.aibase.com/news/30694) ⭐️ 9.0/10

On August 28, Tencent Hunyuan released its open-source flagship model Hy4preview, featuring 770B total parameters with 49B activated and a context length of 1M tokens. The model is now available on HuggingFace, GitHub, ModelScope, Tencent Cloud TokenHub, and OpenRouter. This is a significant open-source LLM release from a major technology company, pushing the frontier of MoE scale and long-context processing. It likely accelerates both research and enterprise adoption, offering a high-capacity model that remains efficient at inference time. Hy4preview was built using expert data from fields such as software engineering, games, finance, and security. The 770B total / 49B activated parameter split indicates a sparse Mixture-of-Experts architecture, and it can be experienced through WorkBuddy/CodeBuddy, Yaobao, and IMA.

aibase · AIbase · Aug 28, 15:27

**Background**: Mixture of Experts \(MoE\) is a model architecture that divides a network into specialized sub-models, or &\#x27;experts,&\#x27; and activates only a subset of them for each token via routing. Dense models activate all parameters for every token, whereas sparse MoE models like Hy4preview keep total parameter counts large while limiting activated parameters to lower computational cost. Tencent Cloud TokenHub is a unified gateway that provides enterprises and developers with access to Tencent&\#x27;s Hunyuan series and mainstream third-party large models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/mixture-of-experts-architecture-glm-5-2-active-parameters">Mixture of Experts Architecture Explained : How GLM... | MindStudio</a></li>
<li><a href="https://www.linkedin.com/pulse/mixture-experts-moe-ai-breakthrough-making-large-language-banafa-xk01c">Mixture of Experts ( MoE ): The AI Breakthrough Making Large ...</a></li>
<li><a href="https://www.tencentcloud.com/products/tokenhub?lang=en&amp;pg=">LLM Service TokenHub</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Tencent Hunyuan`, `#open-source`, `#large language model`

---

<a id="item-3"></a>
## [Rumor of a bug is enough for AI agents to find exploits, OCaml maintainer finds](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) ⭐️ 8.0/10

Anil Madhavapeddy, a Cambridge professor and OCaml core maintainer, reports that within about ten minutes of security patches to OCaml projects being shared for discussion, his website fielded probes for percent-encoded traversal sequences, indicating automated AI agents are watching public repositories. He demonstrated that modern coding agents, including DeepSeek V4 Pro after Claude Fable refused the task, can turn a mere rumor of a bug into a working exploit. This shows that the window between vulnerability disclosure and active exploitation has collapsed from days to minutes, which is incompatible with existing open-source embargo practices. Maintainers and security teams must develop new processes for safely discussing and shipping patches, and the wider ecosystem should expect a surge in AI-driven exploit attempts and security disclosures. Nick Craig-Wood, rclone maintainer, confirms in Hacker News comments that rclone received about 20 security disclosures via GitHub in its first 10 years, but over 40 in the last month alone; roughly 75% contained something worth investigating. He also notes GitHub&\#x27;s CVE assignment time has grown from 2-3 days to 3-4 weeks, forcing point releases with &\#x27;CVE-PENDING&\#x27; in changelogs.

rss · Simon Willison · Aug 28, 22:12

**Background**: Percent-encoding is a mechanism for encoding characters in URIs, and directory traversal attacks use sequences like ../ or encoded variants to access files outside a web server&\#x27;s root directory; probes for percent-encoded traversal sequences indicate attackers are actively checking whether a patched vulnerability is exploitable. OCaml is a general-purpose, multi-paradigm programming language used in static analysis, formal methods, and systems programming. AI coding agents have become increasingly capable of analyzing code and patch diffs to find and exploit vulnerabilities automatically.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Directory_traversal_attack">Directory traversal attack - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OCaml">OCaml - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_%28product%29">DeepSeek (product)</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion features a confirmation from rclone maintainer Nick Craig-Wood, who describes a dramatic increase in security disclosures and time spent triaging, even with AI tools. The sentiment is alarmed but focused on practical implications: the embargo model is breaking, GitHub&\#x27;s CVE process is a bottleneck, and open-source maintainers need new support structures.

**Tags**: `#security`, `#AI agents`, `#software supply chain`, `#OCaml`, `#exploit discovery`

---

<a id="item-4"></a>
## [Anthropic&\#x27;s new framework lets AI agents control hardware](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQc1c5RE5HOUJ5Rlo0OXB3d0F0aVY3WFpqX29jcnAyblU1ZEs5Vy04MXpJNHNKeUprLXNOUlRpMkdPbmZkSVY1ZjVTU2pjM2J1d0VLQTc3b2lOU0dyWFZMVF93U285d1VGNE54UFdwb2wyWDZOV3JwdjdUbkJUVXIxRGNMWmtiR1g1cFZHcXN2ekJRZ0tPYlJXNHdfZzcyb085QUFwaU5sazhocVU?oc=5) ⭐️ 8.0/10

Anthropic has introduced a computer use framework in public beta, enabling AI agents to control computers by looking at the screen, moving a cursor, clicking buttons, and typing text. This capability is available today via the API as part of Claude 3.5 Sonnet, the first frontier AI model to offer computer use. This framework broadens AI automation beyond text and API-based tasks to any software interaction a human can perform, potentially transforming software testing, robotic process automation, and personal assistant capabilities. It also signals a trend where frontier AI models directly manipulate interfaces, increasing the practical scope of autonomous agents. The computer use tool is passed as part of the tools array in an API request, giving Claude four capabilities: screenshot analysis, cursor movement, clicking, and typing. The implementation is stateless and lacks an end-user personalization layer unless integrated into a broader agent framework, and Anthropic offers a Streamlit-based reference implementation.

google\_news · Computerworld · Aug 28, 18:06

**Background**: Computer use refers to an AI model&\#x27;s ability to operate a graphical user interface like a human, by interpreting screenshots and performing keyboard and mouse actions. Traditional AI automation relies on APIs or structured data, which limits it to services that expose such interfaces. Anthropic&\#x27;s computer use framework combines Claude 3.5 Sonnet&\#x27;s vision and reasoning capabilities to enable general-purpose UI navigation, opening up legacy and desktop applications to AI control. This was announced alongside model upgrades and is currently in public beta for developers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/3-5-models-and-computer-use">Introducing computer use , a new Claude 3.5 Sonnet, and Claude ...</a></li>
<li><a href="https://coda.io/@siddhant-sahu/openai-operator-deep-dive/anthropic-computer-use-21">Anthropic Computer Use · Autonomy Product Benchmarking</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI agents`, `#hardware control`, `#framework`, `#AI/ML`

---

<a id="item-5"></a>
## [Tencent WorkBuddy Integrates Hunyuan Hy4 Preview, Free Trial Launches](https://www.aibase.com/news/30699) ⭐️ 8.0/10

On August 28, Tencent WorkBuddy globally integrated Hunyuan&\#x27;s open-source flagship model Hy4preview, offering a two-week free trial. The model has also been open-sourced on Hugging Face and GitHub. This marks Tencent&\#x27;s push to deploy its most advanced open-source model in a mainstream productivity assistant, intensifying the race in AI-powered office and code-generation tools. It also gives developers and enterprises access to a 770B-parameter MoE model with a 1M-token context for real productivity scenarios. Hy4preview uses a Mixture-of-Experts architecture with 770B total parameters but only 49B activated per token, and supports a 1M-token context window. The two-week free trial applies to Hy4preview, while free access to Hunyuan Hy3 has been extended to September 30.

aibase · AIbase · Aug 28, 16:27

**Background**: Mixture-of-Experts \(MoE\) is a neural network architecture that divides a model into specialized sub-networks called experts and uses a router to activate only a small subset for each token. This technique allows massive total parameter counts while keeping computational costs manageable. Long context windows enable models to process entire documents or extended conversations at once, though performance can degrade with very long inputs. Hunyuan is Tencent&\#x27;s large language model family; open-sourcing on Hugging Face and GitHub allows broader community use and fine-tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent - Hunyuan / Hy 4 - preview · GitHub</a></li>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent / Hy 4 - preview · Hugging Face</a></li>
<li><a href="https://www.aibase.com/news/30694">Tencent Hunyuan launches open-source flagship model Hy 4 preview ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Tencent`, `#Hunyuan`, `#LLM`, `#Open Source`

---

<a id="item-6"></a>
## [Tencent Open-Sources 770B-Parameter Hunyuan Hy4preview Model](https://www.aibase.com/news/30697) ⭐️ 8.0/10

Tencent released the preview version of its Hunyuan flagship model, Hy4preview, with 770B total parameters and 49B active parameters, supporting a 1M context window. It is now open-sourced and ranks among top-tier open-source models in coding, office work, and science tasks. This release strengthens Tencent&\#x27;s position in the open-source AI race and provides developers with a high-performance, cost-efficient MoE model comparable to leading proprietary systems. It could accelerate enterprise adoption of open-source LLMs, especially in productivity-focused applications like coding and office automation. The model uses a Mixture-of-Experts architecture, activating only 49B of its 770B parameters per token, which reduces inference cost while retaining large model capacity. According to the announcement, it has already been applied in multiple fields within Tencent.

aibase · AIbase · Aug 28, 15:27

**Background**: Mixture-of-Experts \(MoE\) is an architecture that divides a neural network into specialized sub-networks called experts and uses a router to activate only the most relevant ones for each token. Unlike dense models that activate all parameters, MoE models can dramatically increase total parameter count without proportionally increasing compute, making them attractive for large-scale LLMs. Active parameters determine inference speed and cost, while total parameters affect storage and memory requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.18219">A Closer Look into Mixture - of - Experts in Large Language Models</a></li>
<li><a href="https://researchaudio.io/p/mixture-of-experts-moe-in-large-language-models">Mixture of Experts (MoE) in Large Language Models</a></li>
<li><a href="https://latenteast.com/insights/moe-total-vs-active-parameters">MoE Total vs Active Parameters , Explained | The Latent East</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#open-source`, `#Tencent`, `#Hunyuan`

---

<a id="item-7"></a>
## [Anthropic Launches Model Hardware Standard MHS for AI Physical Control](https://www.aibase.com/news/30693) ⭐️ 8.0/10

On August 27, Anthropic opened a research preview of the Model Hardware Standard \(MHS\), a shared specification developed with HHMI Janelia Research Campus that lets AI agents safely discover and operate physical devices such as microscopes, liquid handlers, robot arms, and quantum calibration rigs. MHS bridges virtual AI capabilities and real-world hardware, offering a common driver layer that could accelerate scientific research and advanced manufacturing. It raises the stakes for AI/robotics integration and operational security, as agents that control physical machines need robust permissions and monitoring. The standard is built around a shared vocabulary between a physical device and an agent, making hardware easier to discover, understand, and coordinate. According to Anthropic, MHS enables agents to autonomously reason about experimental steps, dynamically update parameters, and recover from unexpected hardware failures without human intervention, though it is currently a preview limited to early research labs and advanced manufacturers.

aibase · AIbase · Aug 28, 14:27

**Background**: A model hardware standard \(MHS\) is a shared specification that defines how AI agents discover, understand, and safely operate physical devices. Anthropic developed it with HHMI Janelia Research Campus to help AI accelerate scientific research and advanced manufacturing. An &\#x27;AI agent&\#x27; is a large-model-driven system that can reason about tasks, plan actions, and operate tools or equipment autonomously. MHS provides a common &\#x27;vocabulary&\#x27; between devices and agents, so different hardware can be controlled through a unified interface.

<details><summary>References</summary>
<ul>
<li><a href="https://modelhardwarestandard.com/">Model Hardware Standard</a></li>
<li><a href="https://www.jahanzaib.ai/blog/anthropic-model-hardware-standard-ai-agents-physical-world">AI Hardware Standard : What Anthropic &#x27;s MHS Actually Ships</a></li>
<li><a href="https://openclawlaunch.com/guides/model-hardware-standard">Model Hardware Standard (MHS) Explained: Anthropic MHS vs MCP</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#hardware standard`, `#Anthropic`, `#robotics`, `#AI safety`

---

<a id="item-8"></a>
## [Anthropic Launches Model Hardware Standard for Physical AI](https://www.aibase.com/news/30692) ⭐️ 8.0/10

On August 27, Anthropic introduced the Model Hardware Standard \(MHS\) as a research preview, a shared specification for AI agents to safely operate physical devices. This marks Anthropic&\#x27;s first public move into embodied AI, unifying control and communication for applications like robotics and autonomous vehicles. This extends Anthropic&\#x27;s interoperability approach from software \(MCP\) to physical hardware, potentially influencing how AI systems interact with the physical world. If adopted, MHS could become a common protocol for robotics and autonomous systems, lowering integration barriers across the industry. MHS is initially offered to scientific research labs and advanced manufacturers, with built-in safety checks and human approval for high-risk decisions. It is similar in spirit to the Model Context Protocol but targets physical devices rather than data and software tools.

aibase · AIbase · Aug 28, 14:27

**Background**: Embodied AI refers to the integration of artificial intelligence into physical systems such as robots and autonomous vehicles, enabling them to perceive and act in the real world. Anthropic previously developed the Model Context Protocol \(MCP\) to standardize how AI models connect to data and tools; MHS applies a similar unified orchestration approach to hardware. The research preview gives AI agents a &\#x27;body&\#x27; to operate physical devices, with safeguards to maintain human oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-hardware-standard-research-preview">Previewing the Model Hardware Standard \ Anthropic</a></li>
<li><a href="https://dev.to/alifar/anthropic-mhs-brings-ai-agents-to-biotech-labs-and-quantum-hardware-57h6">Anthropic MHS Brings AI Agents to Biotech Labs... - DEV Community</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI ? | NVIDIA Glossary</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#hardware standard`, `#embodied AI`, `#robotics`, `#AI infrastructure`

---

<a id="item-9"></a>
## [Midjourney V8.2 Beta Adds Image Editing with Instruction Fine-Tuning](https://www.aibase.com/news/30690) ⭐️ 8.0/10

Midjourney has released the V8.2 beta, its first image editing model that moves beyond text-only generation. The update adds instruction fine-tuning, multi-image reference, and inpainting capabilities for more precise and controllable visual creation. This update is significant because Midjourney is one of the most widely used AI image generation tools, and adding editing capabilities expands its utility for professional creators. It reflects a broader industry move toward more interactive and controllable generative models rather than one-shot generation. The V8.2 beta is described as a &\#x27;beta test&\#x27; of the first V8.2 image editing model, integrating instruction fine-tuning, multi-image reference, and inpainting. These features allow users to edit existing images, reference multiple images for style or content, and fill in or replace specific regions.

aibase · AIbase · Aug 28, 11:27

**Background**: Instruction fine-tuning is a method used to adapt pre-trained models to follow specific instructions, often turning a base model into a chat-style assistant. Image inpainting is a technique that fills in missing or damaged parts of an image, and is commonly used in photo editing and restoration. Multi-image reference allows a model to take multiple images as input, enabling it to blend styles, subjects, or elements from different sources. Midjourney&\#x27;s new editing model combines these techniques to bring professional-grade editing into a generative AI tool.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Image_inpainting">Image inpainting</a></li>
<li><a href="https://hackernoon.com/100-days-of-ai-day-13-how-instruction-finetuning-improves-a-pre-trained-llm?ref=hackernoon.com">100 Days of AI , Day 13: How Instruction Finetuning ... | HackerNoon</a></li>
<li><a href="https://magichour.ai/tools/multi-reference-image-generator">Multi - Reference Image Generator - Free Online | Magic Hour</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Midjourney`, `#Image Editing`, `#Generative Models`, `#Creative Tools`

---

<a id="item-10"></a>
## [116 Tech Giants Warn AI Cyber Attacks to Surge, Urge Prioritizing Defense](https://www.aibase.com/news/30683) ⭐️ 8.0/10

A coalition of 116 leading AI and technology entities, including OpenAI, Anthropic, Microsoft, Google, and Amazon, issued a collective warning that AI-enabled cyber attacks will intensify in the coming months. They urged governments and companies to prioritize cybersecurity defenses and accelerate trusted access programs before model releases. This rare industry-wide consensus from leading AI and tech companies signals a systemic shift in the threat landscape, where AI lowers the barrier for sophisticated cyber attacks. It could pressure policymakers to mandate pre-release security reviews and accelerate defensive AI deployments across critical infrastructure. The warning specifically calls for strengthening defenses and speeding up trusted access programs, which give vetted security researchers early access to capable AI models for defensive work. Notably, OpenAI already runs a Trusted Access for Cyber program with Microsoft, and the signatories stress that traditional measures like multi-factor authentication and patching remain highly effective.

aibase · AIbase · Aug 28, 09:27

**Background**: AI-enabled cyber attacks use techniques like deepfakes, polymorphic malware, and adaptive phishing to bypass traditional defenses. A trusted access program is a framework where AI developers grant vetted security researchers early access to capable models, so they can identify vulnerabilities and build defenses before public release. Despite the sophistication of AI-driven intrusions, most attacks still exploit familiar weaknesses such as weak credentials and unpatched systems.

<details><summary>References</summary>
<ul>
<li><a href="https://logicity.in/en/blog/openai-launches-trusted-access-program-for-microsoft-cyber-defense">OpenAI Launches Trusted Access Program for Microsoft... | Logicity</a></li>
<li><a href="https://abnormal.ai/glossary/ai-enabled-cyberattacks">What Are AI - Enabled Cyberattacks ? Why They&#x27;re... | Abnormal AI</a></li>
<li><a href="https://www.linkedin.com/pulse/why-ai-enabled-cyberattacks-signal-deeper-governance-failure-d9b8c">Why AI - Enabled Cyberattacks Signal a Deeper Governance Failure...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#policy`, `#tech industry`, `#risk warning`

---