---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
report: default
---

> From 357 items, 8 important content pieces were selected

---

1. [xAI Releases Grok 4.6 with Enhanced Agent and Vision Capabilities](#item-1) ⭐️ 9.0/10
2. [Qwen Open-Sources 2.4T-Parameter MoE Model with 95B Active Parameters](#item-2) ⭐️ 9.0/10
3. [LTX Releases Open-Source Video Model LTX-2.5, Runs on RTX 5090](#item-3) ⭐️ 8.0/10
4. [Tencent Q2 Revenue Beats, but AI Capex Drives Free Cash Flow Negative](#item-4) ⭐️ 7.0/10
5. [WeChat Releases WeLM, a Resource-Efficient LLM Family](#item-5) ⭐️ 7.0/10
6. [Musk: All Future Teslas to Get Starlink, Starting with Cybercab](#item-6) ⭐️ 6.0/10
7. [OpenAI Codex Reaches 10 Million Users; Tibo Teases Surprise](#item-7) ⭐️ 6.0/10
8. [Enterprise SSDs Hit 48% of NAND Shipments; YMTC Enters Top 3](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [xAI Releases Grok 4.6 with Enhanced Agent and Vision Capabilities](https://x.ai/news/grok-4-6) ⭐️ 9.0/10

xAI released Grok 4.6 on August 12, 2026, building on Grok 4.5 with enhanced long-running agent, interaction, and vision capabilities. The model matches GPT-5.6 Sol on the Artificial Analysis Intelligence Index and is immediately available via Cursor, Grok Build, and the API. This release is significant because it brings xAI&\#x27;s flagship model to parity with a top competitor on a comprehensive independent index, while emphasizing long-running agentic workflows that are becoming central to real-world AI use. Developers and enterprises using Cursor, Grok Build, or the API gain a competitively priced option for agent-heavy applications. Pricing is $2 per million input tokens and $6 per million output tokens, with a faster tier at double the price. For the first week, Grok 4.6 offers double usage allowances on Grok Build and Cursor.

telegram · zaihuapd · Aug 12, 15:54

**Background**: Grok is a series of large language models developed by xAI, launched in 2023 by Elon Musk, with versions adding image generation, web search, and agentic coding tools. Long-running agent tasks are autonomous multi-step workflows that run from minutes to hours, requiring checkpointing, queues, and other infrastructure beyond simple request-response loops. The Artificial Analysis Intelligence Index is an independent benchmark that compares model performance across nine tasks, including agentic reasoning. Grok Build is xAI&\#x27;s tool for vibe coding, where larger tasks are delegated to parallel subagents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_Build">Grok Build</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://www.openlegion.ai/en/learn/ai-agent-long-running-tasks">AI Agent Long Running Tasks : Queues, Checkpoints... | OpenLegion</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Grok`, `#xAI`, `#language models`, `#agentic AI`

---

<a id="item-2"></a>
## [Qwen Open-Sources 2.4T-Parameter MoE Model with 95B Active Parameters](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen has released the open weights for Qwen3.8-2.4T-A95B \(also referred to as Qwen 3.8-Max\) on Hugging Face, a Mixture-of-Experts model with 2.4 trillion total parameters and 95 billion active parameters. The model supports a native context length of 262,144 tokens, extendable to 1,010,000 tokens. This is one of the largest open-weight models ever released, bringing near-frontier capabilities to the open ecosystem. It could significantly lower the barrier for developers and researchers to run or fine-tune a massive MoE model, and signals an accelerating trend of major labs open-sourcing their flagship models. The model uses a Mixture-of-Experts architecture, so its 2.4T total parameters are not all active on every token; only 95B are activated, which helps keep inference cost manageable. The Hugging Face page details that the context length can be extended from 262,144 to 1,010,000 tokens.

telegram · zaihuapd · Aug 12, 16:13

**Background**: Mixture of Experts \(MoE\) is a neural network architecture in which a large model is composed of many smaller &quot;expert&quot; sub-models, and a router directs each input to only a few experts. This design gives the model a high total parameter count while keeping the per-token computational cost closer to the active parameter count. Qwen is Alibaba&\#x27;s open-source LLM family, and this release continues a pattern of frontier models becoming openly available under permissive licenses.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen 3 . 8 - 2 . 4 T - A 95 B , a 2 . 4 T -Parameter Model , with...</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/ Qwen 3 . 8 - 2 . 4 T - A 95 B · Hugging Face</a></li>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between Total and...</a></li>

</ul>
</details>

**Discussion**: Community members expressed excitement about the release, with one commenter noting that the evening saw multiple major model releases, including WeLM from WeChat, Qwen 3.8 Max open weights, DeepSeek v4 Pro, and Grok 4.6. The overall sentiment is one of anticipation and high energy, though no critical analysis or concerns were shared in the snippets.

**Tags**: `#Qwen`, `#LLM`, `#open-source`, `#MoE`, `#AI`

---

<a id="item-3"></a>
## [LTX Releases Open-Source Video Model LTX-2.5, Runs on RTX 5090](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX released LTX-2.5, an open-source video generation foundation model with fully open weights, training code, and inference pipeline. It can run locally on a single RTX 5090, and companies with annual revenue under $10 million can use it commercially for free. This is a significant milestone for AI video generation because it makes a powerful open-source video model accessible on consumer hardware, lowering the barrier for developers and small studios. It also combines text-to-video, image-to-video, and multi-shot consistency, potentially reshaping the open-source video model landscape. LTX-2.5 uses a new diffusion video decoder that enhances decoding quality and adopts the Gemma 4 12B text encoder for better prompt following. In a 98-prompt text-to-video artifact evaluation, LTX 2.5 Pro ranked first among ten models.

telegram · zaihuapd · Aug 12, 02:15

**Background**: Open-source video generation models are rare because training and running them typically requires large GPU clusters. This release continues a trend of smaller open models becoming usable on single high-end consumer GPUs like the RTX 5090, thanks to efficient architectures and optimization techniques. Gemma 4 12B is Google&\#x27;s open model with a unified transformer that directly processes vision and audio inputs.

<details><summary>References</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-5">LTX - 2 . 5 : LTX&#x27;s Latest AI Open-Source Foundation Model | LTX</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/">Introducing Gemma 4 12 B</a></li>

</ul>
</details>

**Tags**: `#AI`, `#video-generation`, `#open-source`, `#deep-learning`, `#generative-models`

---

<a id="item-4"></a>
## [Tencent Q2 Revenue Beats, but AI Capex Drives Free Cash Flow Negative](https://wallstreetcn.com/articles/3779275) ⭐️ 7.0/10

Tencent reported Q2 2026 revenue of RMB 204.8 billion, up 11% year-over-year and slightly above Bloomberg consensus. Capital expenditures nearly tripled to RMB 52.8 billion due to AI spending, pushing free cash flow to -RMB 13.8 billion. This highlights the growing financial pressure on Chinese tech giants from AI infrastructure investments, even when core revenues are healthy. It underscores the industry-wide trade-off between aggressive AI capex and near-term cash flow. Net profit rose only 0.7% to RMB 56 billion, missing market expectations. Excluding AI computing prepayments, free cash flow was RMB 37.6 billion; marketing services revenue led growth at 22%.

telegram · zaihuapd · Aug 12, 10:30

**Background**: Tencent is a Chinese internet conglomerate whose businesses span gaming, advertising, and cloud services. AI infrastructure investment, including prepayments for computing power, is increasingly affecting conventional cash flow metrics. WorkBuddy, Tencent&\#x27;s desktop AI office assistant, has ranked first in monthly visits among Chinese desktop AI office agents.

<details><summary>References</summary>
<ul>
<li><a href="https://www.workbuddy.cn/">WorkBuddy - AI Agent 办 公 新范式</a></li>
<li><a href="https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260812-%E8%B4%B9%E5%8A%A0%E7%BD%97%E6%8A%A5-%E4%B8%AD%E5%9B%BDai%E4%BA%A7%E4%B8%9A%E7%AA%81%E9%A3%9E%E7%8C%9B%E8%BF%9B%EF%BC%8C%E4%BB%8E%E8%8A%AF%E7%89%87%E5%88%B0%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%97%A0%E4%B8%8D%E9%A2%A0%E8%A6%86%E7%A1%85%E8%B0%B7%E7%9A%84%E6%A0%BC%E5%B1%80">费加罗报：中国 AI ... - RFI - 法国国际广播电台</a></li>

</ul>
</details>

**Tags**: `#Tencent`, `#earnings`, `#AI capex`, `#finance`, `#technology`

---

<a id="item-5"></a>
## [WeChat Releases WeLM, a Resource-Efficient LLM Family](https://x.com/Weixin_WeChat/status/2087509298310209718) ⭐️ 7.0/10

On August 12, the WeChat team released WeLM, a general-purpose large language model family. It includes WeLM-80B \(3B active parameters\), already deployed in WeChat&\#x27;s AI assistant Xiaowei, and the upcoming MoE-based WeLM-617B \(23B active parameters\). This release highlights a pragmatic focus on resource efficiency for large language models, enabling deployment across WeChat&\#x27;s massive user scenarios. The mix of dense and MoE architectures could make advanced AI more accessible and affordable for real-world products. WeLM-80B activates only 3B parameters during inference, while the MoE-based WeLM-617B activates 23B parameters. WeLM-80B currently powers the Xiaowei AI agent for dialogue, search, native WeChat operations, and mini-program services; WeLM-617B targets complex tasks such as mini-program smart development.

telegram · zaihuapd · Aug 12, 13:58

**Background**: Large language models \(LLMs\) typically require enormous compute for training and inference, which limits their practical adoption. Mixture of Experts \(MoE\) architecture splits a large model into many specialized sub-models and routes each input to only a few experts, enabling sparse activation and much lower computation at runtime. This allows models with hundreds of billions of parameters to run with only a fraction of their parameters active, making large-scale AI more feasible in real applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.weex.com/news/detail/wechat-launches-welm-large-model-series-to-drive-ai-application-implementation-c0pmz8w994lglikkdnsi3ndr">WeChat Launches WeLM Large Model Series to... | WEEX Crypto News</a></li>
<li><a href="https://www.gate.com/news/detail/wechat-releases-welm-large-language-model-series-with-welm-80b-active-in-ai-23402318">WeChat Releases WeLM Large Language Model Series... | Gate News</a></li>
<li><a href="https://ai.plainenglish.io/mixture-of-expert-architecture-7be02b74f311?gi=cd7fcbceef49">Mixture of Expert Architecture . Definitions and Applications included...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#WeLM`, `#MoE`, `#WeChat`, `#AI`

---

<a id="item-6"></a>
## [Musk: All Future Teslas to Get Starlink, Starting with Cybercab](https://www.techspot.com/news/113429-elon-musk-every-tesla-have-starlink-starting.html) ⭐️ 6.0/10

Elon Musk announced on an earnings call that all future Tesla models will include Starlink connectivity, beginning with the Cybercab. The Cybercab was shown with an integrated Starlink V5 antenna in the rear roof. This ties SpaceX&\#x27;s satellite internet directly into Tesla&\#x27;s product line, giving vehicles connectivity outside terrestrial cell coverage. It is especially important for the Cybercab robotaxi, which needs always-on signals for navigation, service, and fleet management, and could set a new standard for vehicle connectivity. The Cybercab has no steering wheel or pedals and uses a Starlink V5 antenna mounted in the rear roof, which supports speeds up to 375 Mbps. Musk says passengers can stream 4K video in transit, but no production timeline has been announced.

telegram · zaihuapd · Aug 12, 03:53

**Background**: Starlink is SpaceX&\#x27;s low Earth orbit satellite internet constellation, designed to provide broadband in areas without reliable ground infrastructure. The Cybercab is a purpose-built two-passenger autonomous EV, unveiled in concept form in October 2024 and in pilot production since February 2026. The newer V5 dish uses fewer antenna elements in a smaller, lighter enclosure, making it cheaper and easier to manufacture at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab</a></li>
<li><a href="https://hypebeast.com/2026/8/tesla-cybercab-debuts-with-integrated-starlink-v5">Tesla Cybercab With Starlink V 5 Antenna Revealed | Hypebeast</a></li>
<li><a href="https://otontechnology.com/starlink-v5-dish-smaller-lighter-efficient/">SpaceX&#x27;s Starlink V 5 Ships With Half the Antenna Elements</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#Starlink`, `#Satellite Internet`, `#EV`, `#Autonomous Vehicles`

---

<a id="item-7"></a>
## [OpenAI Codex Reaches 10 Million Users; Tibo Teases Surprise](https://x.com/thsottiaux/status/2087423996115681767) ⭐️ 6.0/10

OpenAI&\#x27;s Codex has surpassed 10 million active users. In a post on X, Tibo noted the milestone and teased that a surprise will be announced tomorrow. This is a significant milestone for OpenAI&\#x27;s AI coding product, showing strong mainstream adoption of AI-assisted software development. It also signals that OpenAI may soon make an announcement that could affect how Codex usage limits or product features are managed. Earlier, Tibo said he would trigger a Codex limit reset for each additional one million active users, up to 10 million. The team has remained silent since crossing the threshold, and the promised reset and the upcoming surprise may be connected.

telegram · zaihuapd · Aug 12, 08:01

**Background**: Codex is OpenAI&\#x27;s AI coding agent that can generate code from natural language prompts and runs in ChatGPT and a terminal-based CLI. To manage heavy demand, OpenAI periodically resets usage limits for Codex, and community-run trackers log these resets. This milestone of 10 million active users highlights how quickly AI coding tools have grown in just a few years.

<details><summary>References</summary>
<ul>
<li><a href="https://codex-resets.com/">Codex Limit Reset Tracker &amp; History | Codex Resets</a></li>
<li><a href="https://codex-reset.com/timeline">Codex Reset Timeline: Verified History, Hours, and Official Windows</a></li>
<li><a href="https://digg.com/tech/74z2hfxi">OpenAI Resets Limits for Codex and ChatGPT Work Users · Digg</a></li>

</ul>
</details>

**Tags**: `#Codex`, `#OpenAI`, `#AI coding`, `#milestone`, `#announcement`

---

<a id="item-8"></a>
## [Enterprise SSDs Hit 48% of NAND Shipments; YMTC Enters Top 3](https://china.counterpointresearch.com/%e6%9c%8d%e5%8a%a1%e5%99%a8%e9%9c%80%e6%b1%82%e6%8e%a8%e5%8d%87%e4%bc%81%e4%b8%9a%e7%ba%a7-ssd-%e5%8d%a0-nand-%e5%87%ba%e8%b4%a7%e9%87%8f%e7%99%be%e5%88%86%e4%b9%8b-48/) ⭐️ 6.0/10

According to a Counterpoint report, enterprise SSDs accounted for 48% of global NAND shipments in Q2 2026, nearly double year-over-year, driven by AI inference workloads. YMTC overtook Kioxia to rank third in market share with 14%, behind Samsung \(25%\) and SK Hynix \(22%\). This marks a structural shift in the NAND market, as AI-driven data center demand now dominates bit shipments and is expected to push enterprise SSDs past half of all NAND consumption by year-end. The ranking change also shows Chinese memory maker YMTC rapidly gaining share among top-tier suppliers. The report notes that despite YMTC&\#x27;s third-place shipment share, its revenue ranks only fifth because its product mix skews toward consumer-grade SSDs. Industry revenue in the quarter grew fivefold year over year.

telegram · zaihuapd · Aug 12, 11:00

**Background**: NAND flash is a type of non-volatile memory used in SSDs and other storage devices, retaining data without power. AI inference, the process of running trained models to make predictions, requires rapid, repeated data access, which is driving demand for high-performance enterprise SSDs in data centers. Enterprise SSDs are optimized for server workloads and typically command higher prices than consumer drives.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flash_memory">Flash memory - Wikipedia</a></li>
<li><a href="https://gcore.com/learning/what-is-ai-inference">What is AI inference and how does it work? | Gcore</a></li>

</ul>
</details>

**Tags**: `#NAND`, `#SSD`, `#Enterprise Storage`, `#AI`, `#Market Share`

---