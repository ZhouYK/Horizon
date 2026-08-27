---
layout: default
title: "Horizon Summary: 2026-08-27 (EN)"
date: 2026-08-27 04:33:18 +0000
lang: en
report: default
---

> From 333 items, 8 important content pieces were selected

---

1. [China Achieves First Two-Way High-Speed Laser Link Over Earth-Moon Distance](#item-1) ⭐️ 9.0/10
2. [Alibaba Qwen Releases Qwen3.8-Flash, a 125B MoE Model with 6B Active Parameters](#item-2) ⭐️ 8.0/10
3. [Z.ai Releases GLM-5.3-Flash with 18B Active Parameters at 10x Lower Price](#item-3) ⭐️ 8.0/10
4. [Google launches Gemini 3.5 Transcribe for multilingual smart transcription](#item-4) ⭐️ 8.0/10
5. [Nvidia in talks to acquire Hugging Face at $13B+ valuation](#item-5) ⭐️ 8.0/10
6. [Qualcomm Announces AI-Native 6G, Token-as-a-Service Model, and Data Center Expansion](#item-6) ⭐️ 7.0/10
7. [Claude Cowork Desktop App Adds Built-In Browser for Web Automation](#item-7) ⭐️ 7.0/10
8. [Telegram Adds Welcome Messages, Buttons, and Signed Gifts on 13th Anniversary](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [China Achieves First Two-Way High-Speed Laser Link Over Earth-Moon Distance](https://www.stdaily.com/web/gdxw/2026-08/26/content_570163.html) ⭐️ 9.0/10

The Technology and Engineering Center for Space Utilization under the Chinese Academy of Sciences announced it has established a two-way laser link spanning more than 400,000 kilometers between Earth and the Moon. This is China&\#x27;s first two-way high-speed laser communication over the Earth-Moon distance, achieving a downlink of 100 Mbps and an uplink of 1.25 Mbps. This breakthrough moves space laser communication from near-Earth orbits to cislunar space, promising dramatically faster data return from lunar and deep-space missions. Compared with traditional microwave links, laser communication offers 10 to 100 times higher transmission rates, enabling rapid delivery of high-definition lunar imagery and real-time video. The demonstration was carried out using the DRO-A satellite, which had been rescued after its March 2024 launch failure and entered a distant retrograde orbit around the Moon in July 2024. According to the report, an 8K lunar image would take about 12 seconds to download via the 100 Mbps laser link, versus roughly 4 to 5 minutes over a 5 Mbps microwave downlink.

telegram · zaihuapd · Aug 27, 00:33

**Background**: Space laser communication uses laser beams as carriers, which operate at much higher frequencies \(tens of THz\) than radio frequency \(hundreds of MHz\), providing 10–100 times higher data rates with smaller, lighter, and lower-power terminals. NASA&\#x27;s Psyche mission, launched in October 2023, carried the Deep Space Optical Communications \(DSOC\) payload to test laser links at distances of 0.06–2.7 AU. China&\#x27;s DRO-A satellite is an experimental lunar-orbiting spacecraft; after its initial launch anomaly, it was placed into a distant retrograde orbit through orbital reconstruction and a lunar gravity assist in July 2024. This experiment thus also validates the health and capabilities of the DRO-A platform.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/994/732.htm">地 月 “ 信 息高速路” 通 了：我国成功建立超过 40 万公里双向 激 光 链路 - IT...</a></li>
<li><a href="https://baike.baidu.com/item/DRO-A%E5%8D%AB%E6%98%9F/64160567">DRO-A卫星_百度百科</a></li>
<li><a href="https://www.spacejournal.cn/hwyjggc/cn/article/doi/10.3788/IRLA20240247">深空激光通信发展现状与趋势分析（封面文章·特邀）</a></li>

</ul>
</details>

**Tags**: `#space communication`, `#laser communication`, `#deep space`, `#China`, `#DRO-A`

---

<a id="item-2"></a>
## [Alibaba Qwen Releases Qwen3.8-Flash, a 125B MoE Model with 6B Active Parameters](https://x.com/Alibaba_Qwen/status/2092591393424515114) ⭐️ 8.0/10

Alibaba&\#x27;s Qwen team released Qwen3.8-Flash, a multimodal Mixture-of-Experts model with 125B total parameters and only 6B active per token, and open-sourced Qwen3.8-Flash-Next as a preview of the Qwen4 architecture. The company claims performance comparable to Anthropic Opus 4.6 and DeepSeek V4-Flash at far lower cost. The release strengthens the open-source segment of the LLM ecosystem with a highly efficient MoE design that claims frontier-level performance at commodity prices. A pricing of $0.16 and $0.47 per million input/output tokens could pressure commercial API providers and benefit developers running large-scale inference workloads. The model has a native 262K context length expandable to 1M, and the open-sourced Qwen3.8-Flash-Next is meant as a preview of the Qwen4 architecture. Alibaba says training cost is about one-ninth of Qwen3.7-Plus while delivering better coding and office-task performance, although the benchmark claims have not been independently verified.

telegram · zaihuapd · Aug 26, 13:36

**Background**: Mixture of Experts \(MoE\) is a machine learning technique that divides a model into multiple specialized sub-networks, or &quot;experts&quot;, and activates only a subset of them for each input, improving efficiency while keeping a large total parameter count. This design allows models like Qwen3.8-Flash to have 125B total parameters but only 6B active parameters per token, reducing inference cost. Total parameters roughly indicate model size, while active parameters determine the computation used during each forward pass.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts? - IBM</a></li>
<li><a href="https://www.explainx.ai/blog/llm-model-parameters-billions-explained">What are parameters in a large language model? Billions ...</a></li>

</ul>
</details>

**Tags**: `#Qwen`, `#MoE`, `#LLM`, `#AI`, `#open-source`

---

<a id="item-3"></a>
## [Z.ai Releases GLM-5.3-Flash with 18B Active Parameters at 10x Lower Price](http://z.ai/) ⭐️ 8.0/10

Z.ai released GLM-5.3-Flash, a native multimodal mixture-of-experts \(MoE\) model with 320B total parameters and 18B active parameters. The API price drops to about one-tenth of the previous generation, with a limited-time offer of $0.075 per million input tokens, $0.015 for cached input, and $0.25 for output. This release makes high-performance multimodal AI inference dramatically cheaper, potentially accelerating adoption in coding agents and other applications. Its ability to run entirely on domestic Chinese AI chips with 3x improved end-to-end inference performance could reduce dependence on NVIDIA GPUs and reshape the AI infrastructure landscape. GLM-5.3-Flash uses a hybrid architecture combining sparse and linear attention with Manifold-Constrained Hyper-Connections \(mHC\), which reduces long-context serving costs while preserving long-context capabilities. It reportedly beats GLM-5.2 on coding and agent benchmarks and approaches Claude Opus 4.8; the promotional prices revert to $0.15/$0.03/$0.50 afterward.

telegram · zaihuapd · Aug 26, 14:23

**Background**: Mixture-of-experts \(MoE\) is a machine learning technique where a model is divided into multiple specialized sub-networks, and only a subset \(the active parameters\) is used for each input token. This allows models to have enormous total parameter counts while keeping inference efficient. Hybrid sparse and linear attention architectures combine local sparse attention with linear-complexity mechanisms to handle long sequences more efficiently than standard quadratic attention. GLM is a series of large language models developed by Chinese AI company Z.ai \(formerly Zhipu AI\).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/hybrid-sparse-and-linear-attention-mechanisms">Hybrid Sparse &amp; Linear Attention - emergentmind.com</a></li>
<li><a href="https://arxiv.org/abs/2507.06457">[2507.06457] A Systematic Analysis of Hybrid Linear Attention Every Attention Matters: An Efficient Hybrid Architecture for ... Z.ai releases GLM-5.3-Flash, a 320B parameter hybrid sparse ... LLM Architecture -&gt; Sparse vs. Linear Attention - LinkedIn A Visual Guide to Attention Variants in Modern LLMs</a></li>

</ul>
</details>

**Tags**: `#GLM`, `#AI`, `#LLM`, `#model release`, `#pricing`

---

<a id="item-4"></a>
## [Google launches Gemini 3.5 Transcribe for multilingual smart transcription](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 8.0/10

Google announced Gemini 3.5 Transcribe, a speech-to-text model built on Gemini audio understanding, with API availability in Google AI Studio and Gemini Enterprise. It automatically recognizes over 85 languages, removes filler words such as &quot;um&quot; and &quot;uh&quot;, and can format unstructured speech into structured text. This marks a major upgrade to Google&\#x27;s transcription stack, affecting speech-recognition workflows for developers, enterprises, and everyday users. By plugging into Search Live, Gemini Live, Docs, Keep, Gmail, and Chrome, it could make automatic transcription and voice editing more ubiquitous across Google products. The model supports custom vocabulary for alphanumeric strings like order numbers, provides word-level timestamps for up to three speakers in pre-recorded audio, and allows editing content through voice commands. It also uses utterance-based language detection and smart transcription to clean up speech disfluencies.

telegram · zaihuapd · Aug 27, 01:02

**Background**: Gemini 3.5 Transcribe is a speech-to-text model based on Gemini&\#x27;s audio understanding capabilities, providing low-latency transcription with speaker diarization. Speaker diarization is the process of partitioning an audio stream into segments according to speaker identity, answering &quot;who spoke when&quot;, which is distinct from automatic speech recognition&\#x27;s &quot;what was said&quot;. Removing filler words and adding timestamps make raw transcripts easier to read and more useful for meeting notes, subtitles, and search.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Introducing Gemini 3 . 5 Transcribe</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe">Gemini 3 . 5 Transcribe | Gemini API | Google AI for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speaker_diarisation">Speaker diarisation</a></li>

</ul>
</details>

**Tags**: `#speech recognition`, `#Gemini`, `#Google`, `#AI models`, `#transcription`

---

<a id="item-5"></a>
## [Nvidia in talks to acquire Hugging Face at $13B+ valuation](https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8) ⭐️ 8.0/10

Nvidia is reportedly in talks to acquire open-source AI platform Hugging Face at a valuation exceeding $13 billion. No agreement has been reached, and negotiations could still fall through. If completed, this acquisition would combine Nvidia&\#x27;s dominance in AI hardware with Hugging Face&\#x27;s central role in the open-source AI ecosystem, potentially reshaping how AI models are developed and distributed. It would also signal a major shift in the competitive landscape, affecting developers, startups, and cloud providers that rely on Hugging Face&\#x27;s platform. Nvidia is already a shareholder in Hugging Face, having participated in its $235 million funding round in 2023, which valued the company at $4.5 billion. Hugging Face previously rejected a $500 million investment offer from Nvidia last year, and Microsoft also held talks before they reportedly stopped.

telegram · zaihuapd · Aug 27, 02:03

**Background**: Hugging Face is a New York-based company known for its Transformers library and its large open-source community, which hosts tens of thousands of machine learning models and datasets. Nvidia is the leading designer of GPUs and AI accelerators that power most AI training and inference workloads. An acquisition would give Nvidia direct control over the most popular distribution hub for open-source AI models, deepening its influence beyond hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/hugging-face">What is Hugging Face? - IBM</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Hugging Face`, `#Acquisition`, `#AI`, `#Open Source`

---

<a id="item-6"></a>
## [Qualcomm Announces AI-Native 6G, Token-as-a-Service Model, and Data Center Expansion](https://finance.sina.com.cn/jjxw/2026-08-26/doc-inipsezr5961972.shtml) ⭐️ 7.0/10

At its San Diego 6G media day, Qualcomm executive vice president Ma Dejia said 6G&\#x27;s defining shift is AI built into the network architecture, enabling &\#x27;agentic AI devices&\#x27; and pushing operators toward compute- and token-as-a-service business models; the 6G standard is expected around 2028. The company also expanded its data center push with the Dragonfly product line and HBC high-bandwidth compute architecture, targeting over $15 billion in data center revenue by fiscal 2029 and completing the acquisition of AI infrastructure firm Modular. This announcement signals a fundamental shift in telecom business models from selling connectivity and data to selling AI compute and tokens, and it positions Qualcomm to compete aggressively in the data center AI inference market against incumbents like Nvidia and AMD. It also gives concrete form to 6G&\#x27;s &\#x27;AI-native&\#x27; vision, affecting operators, device makers, and developers in the coming decade. Qualcomm&\#x27;s HBC architecture stacks compute beneath DRAM to address the AI memory wall and inference decode bottleneck, enabling lower-power, lower-latency token generation, while the Dragonfly line targets data center AI inference accelerators. Ma Dejia cited Doubao&\#x27;s AI phone as an example of an agentic AI device and described token-based billing as an evolution beyond gigabytes and throughput/SLA-based models.

telegram · zaihuapd · Aug 27, 02:31

**Background**: 6G is the successor to 5G mobile networks, with its standards expected to be set around 2028 and AI considered a core design element rather than just an application layer. Token-as-a-service is a usage-based billing model that meters AI compute in tokens — the text/data units processed by large language models — similar to how AI APIs are priced today, while compute-as-a-service lets operators sell access to raw compute capacity. Qualcomm&\#x27;s HBC \(high-bandwidth compute\) is a near-memory computing architecture that places compute close to DRAM to overcome the &\#x27;AI memory wall,&\#x27; where the speed of moving data between memory and logic chips becomes the bottleneck for large-model inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.qualcomm.com/news/onq/2026/07/qualcomm-hbc-near-memory-computing">Near-Memory Computing and the AI Memory Wall | Qualcomm</a></li>
<li><a href="https://www.qualcomm.com/data-center/expertise/ai-accelerators">Data Center AI Inference Accelerators | Dragonfly - Qualcomm</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-33191-6_6">Business Models in 5G/6G Mobile Communications - Springer What is Token-as-a-Service (TaaS)? A New Model for Resource ... From gigabytes to tokens: The evolution of telecom business ... Tokenization as a Service (TaaS): A Business Guide [2026]</a></li>

</ul>
</details>

**Tags**: `#6G`, `#AI`, `#Qualcomm`, `#Token-as-a-Service`, `#Data Center`

---

<a id="item-7"></a>
## [Claude Cowork Desktop App Adds Built-In Browser for Web Automation](https://claude.com/blog/cowork-built-in-browser) ⭐️ 7.0/10

Anthropic has added a built-in browser to its Claude Cowork desktop app, allowing Claude to autonomously navigate websites, read content, click, and type in a sidebar. The feature is rolling out this week to Pro, Max, and Team plans with default-on behavior, while Enterprise admins can enable it starting today. This significantly expands Claude&\#x27;s agentic capabilities to real-world web tasks without requiring browser extensions or connectors, lowering the barrier for non-technical users to automate workflows. The privacy-isolated browser design also addresses key security concerns around AI agents accessing personal browsing data, making AI-powered web automation more trustworthy. The built-in browser is fully isolated from the user&\#x27;s regular browser, meaning it cannot see tabs, bookmarks, or saved passwords. The feature works without connectors for many portals and is enabled by default on supported plans; Enterprise controls provide admin-level enablement and oversight.

telegram · zaihuapd · Aug 27, 03:06

**Background**: Claude Cowork is Anthropic&\#x27;s desktop AI agent aimed at non-technical users; it can read, edit, and create files, organize desktops, and complete multi-step office tasks. The new built-in browser is part of Cowork&\#x27;s push to handle web tasks natively, complementing Anthropic&\#x27;s connector system — MCP-based integrations that connect Claude to apps like Google Workspace and Microsoft 365. The feature is rolling out across paid plans, building on Anthropic&\#x27;s broader Claude family of large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/cowork">Claude Cowork | Claude by Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Cowork">Claude Cowork</a></li>
<li><a href="https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities">Use connectors to extend Claude&#x27;s capabilities | Anthropic ...</a></li>

</ul>
</details>

**Tags**: `#Claude`, `#AI agents`, `#browser automation`, `#Anthropic`, `#desktop app`

---

<a id="item-8"></a>
## [Telegram Adds Welcome Messages, Buttons, and Signed Gifts on 13th Anniversary](https://telegram.org/blog/welcome-messages-buttons-TG-13) ⭐️ 6.0/10

Telegram released a new update featuring welcome messages that only new members can see, multiple buttons within a single message, rich text support, and the ability to sign gift purchases. The update coincides with Telegram&\#x27;s 13th anniversary. The update gives group and channel admins a better way to onboard new members and gives developers more tools for creating interactive experiences like quizzes, games, and product browsing. It also deepens the social aspect of Telegram&\#x27;s gift marketplace. Welcome messages support multiple messages, media, and rich text, and can be set as the first contact for new members. Buttons can be attached to messages for various interactive uses, while gifts bought in the marketplace can now include a signature and comment.

telegram · zaihuapd · Aug 27, 00:05

**Background**: Telegram is a cloud-based messaging app known for frequent feature updates and strong bot support. Welcome messages are messages shown only to new subscribers or group members, while message buttons are typically rendered as inline keyboards that let bots offer interactive options. Rich text formatting and Telegram Stars, the in-app currency for digital goods, are also part of the platform&\#x27;s broader ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://telegram.org/blog/welcome-messages-buttons-TG-13">Welcome Messages, Buttons in Messages and Signed Gifts</a></li>
<li><a href="https://core.telegram.org/api/bots/buttons">Bot buttons</a></li>

</ul>
</details>

**Tags**: `#Telegram`, `#product update`, `#messaging`, `#features`

---