---
layout: default
title: "Horizon Summary: 2026-10-16 (EN)"
date: 2026-10-16 23:04:10 +0000
lang: en
report: default
---

> From 166 items, 5 important content pieces were selected

---

1. [Investors Cut Anthropic IPO Valuation Expectations to $1.5 Trillion](#item-1) ⭐️ 8.0/10
2. [Kuaishou&\#x27;s Kling 4.0 AI video model rolls out globally](#item-2) ⭐️ 7.0/10
3. [StepFun releases Step 5 Preview, a 600B sparse MoE agent flagship](#item-3) ⭐️ 7.0/10
4. [Apple&\#x27;s First Foldable iPhone Duo Sells Out in a Minute, Premarket Stock Jumps 2%](#item-4) ⭐️ 7.0/10
5. [Court Documents Reveal Telegram Handed User Data to U.S. Law Enforcement](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Investors Cut Anthropic IPO Valuation Expectations to $1.5 Trillion](https://www.reuters.com/business/finance/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-2026-10-15/) ⭐️ 8.0/10

Reuters reports that some investors have lowered their expected valuation for Anthropic&\#x27;s initial public offering from about $2 trillion to roughly $1.5 trillion. The downgrade came despite Anthropic posting $16.8 billion in third-quarter revenue, up 45% quarter-over-quarter, along with adjusted profitability and positive quarterly cash flow. The revision suggests that even the strongest AI labs may face more disciplined public-market pricing, with investors weighing growth durability rather than headline revenue alone. It could act as a valuation stress test for other AI companies, including Chinese players such as Zhipu AI, MiniMax, Moonshot AI&\#x27;s Kimi and DeepSeek, shifting attention toward revenue sustainability, gross margins and capital efficiency. The cited reasons for the cut are slowing growth, intensifying price competition among models, and heavy compute investment pressure — meaning the cost of training and serving frontier models is rising faster than investors are willing to capitalize. Notably, the reduction happened even though the company was reported as adjusted-profitable with positive quarterly cash flow, suggesting valuation sentiment is driven more by forward expectations than current results.

telegram · zaihuapd · Oct 16, 15:46

**Background**: Anthropic is a US AI lab known for its Claude family of large language models, and an IPO \(initial public offering\) is the process by which a private company lists shares on a public stock exchange; the &\#x27;expected IPO valuation&\#x27; is the price tag investors think the company will carry when it lists. Private AI companies are typically valued on forecasts of revenue growth, gross margin and cash burn rather than current earnings, which is why a slower growth outlook or rising compute costs can quickly move those expectations. The article frames this as a read-across to Chinese AI firms: Zhipu AI \(北京智谱华章\) is one of the largest of China&\#x27;s &\#x27;six little tigers&\#x27; AI startups, MiniMax \(上海稀宇科技\) builds multimodal models and consumer apps such as Talkie and Hailuo AI, Moonshot AI is the developer behind the Kimi assistant, and DeepSeek is a model developer known for low-cost, high-efficiency models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MiniMax_Group">MiniMax Group - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E7%A8%80%E5%AE%87%E7%A7%91%E6%8A%80">MiniMax - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.iplaysoft.com/moonshot-kimi.html">Kimi ( 月 之 暗 面 Moonshot AI )...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#Valuation`, `#Reuters`

---

<a id="item-2"></a>
## [Kuaishou&\#x27;s Kling 4.0 AI video model rolls out globally](https://mp.weixin.qq.com/s/Dn2jAxV0m6kpt7y4edRvdg) ⭐️ 7.0/10

On October 15, Kuaishou&\#x27;s Kling 4.0 officially launched in full on klingai.com, accompanied by a redesigned creation interface intended to give users more flexible and free-form control. The company also said 4K and 1080p 10-bit HDR output formats are coming, that Kling 4.0 capabilities are already accessible through MCP and CLI, and that API services for enterprises and developers will open soon. Kling is one of the leading commercial text-to-video models, so a full 4.0 rollout plus 10-bit HDR export and MCP/CLI hooks pushes AI video generation closer to professional post-production pipelines rather than remaining a novelty demo. Opening a developer and enterprise API also signals that video generation is moving from consumer apps into integrated production tooling and automated workflows. The announcement is brief and promotional: no benchmark scores, resolution/frame-rate specifics, pricing, or exact release dates for the 4K/1080p 10-bit HDR output and the developer API are given, only that they are coming soon. 10-bit HDR matters because it delivers far more color gradation and brightness range than standard 8-bit SDR, which is what professional color grading workflows expect.

telegram · zaihuapd · Oct 16, 04:30

**Background**: Kling is Kuaishou&\#x27;s text-to-video and image-to-video generation model, competing with tools such as OpenAI&\#x27;s Sora, Runway and Google&\#x27;s Veo. MCP, or Model Context Protocol, is an open standard introduced by Anthropic in November 2024 that lets AI applications connect to external tools, systems and data sources in a uniform way, so MCP support means Kling can be called from AI assistants and agent workflows rather than only through a web page. A CLI, or command-line interface, similarly allows developers to script video generation into automated pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://en.wikipedia.org/wiki/HDR10">HDR10 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI video generation`, `#Kling`, `#multimodal AI`, `#model release`, `#developer API`

---

<a id="item-3"></a>
## [StepFun releases Step 5 Preview, a 600B sparse MoE agent flagship](https://huggingface.co/stepfun-ai/Step-5-Preview) ⭐️ 7.0/10

StepFun \(阶跃星辰\) published Step 5 Preview on Hugging Face, a flagship sparse Mixture-of-Experts model with 600 billion total parameters and 27 billion active parameters per token, supporting up to a 1M-token context window and native text, image, and video input. The company reports leading results on software engineering, long-horizon agent execution, and domain-expert tasks, especially in finance. This is a frontier-scale release aimed squarely at agentic and software-engineering workloads, and it shows Chinese labs continuing to ship very large sparse MoE flagships that target the same use cases as top closed models. Because the model is downloadable and deployable behind an OpenAI-compatible API, it could give agent builders a self-hostable alternative for long-context, tool-using workloads. Notable specifics include the 600B-total / 27B-active sparsity ratio, the 1M-token context, multimodal input, and serving via vLLM or SGLang with an OpenAI-compatible API under the StepFun Model License 1.0. The caveats are that this is explicitly a &\#x27;Preview&\#x27; release from a single vendor, and the performance claims come with no independent benchmarks or third-party evaluation attached.

telegram · zaihuapd · Oct 16, 06:36

**Background**: Mixture-of-Experts \(MoE\) models split the network into many specialized &\#x27;expert&\#x27; sub-networks and route each token to only a few of them; sparse activation means the model can have huge total capacity \(600B parameters\) while only computing a small fraction \(27B\) per token, keeping inference cost far below a dense model of the same size. A context window of 1M tokens lets the model ingest very long documents or extended agent trajectories in one pass, which matters for long-horizon agent tasks where state accumulates over many steps. Serving such models typically requires dedicated inference engines: vLLM is a Berkeley-origin open-source framework built around PagedAttention for high-throughput serving, and SGLang is an open-source framework from LMSYS-affiliated researchers optimized for structured generation and agentic workloads; both expose OpenAI-style APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">VLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/SGLang">SGLang</a></li>
<li><a href="https://www.emergentmind.com/topics/extreme-sparsity-mixture-of-experts-moe-architecture">Extreme- Sparsity MoE Architecture</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoE`, `#AI Agents`, `#Multimodal`, `#Model Release`

---

<a id="item-4"></a>
## [Apple&\#x27;s First Foldable iPhone Duo Sells Out in a Minute, Premarket Stock Jumps 2%](https://api3.cls.cn/share/article/2507193?os=android&amp;amp;sv=8.8.4&amp;amp;app=cailianpress) ⭐️ 7.0/10

Apple&\#x27;s first foldable phone, the iPhone Duo, sold out across all configurations within one minute of going on sale, according to a report from Cailian Press. The sellout helped push Apple&\#x27;s US premarket shares up more than 2%, with the stock poised to open at a record high. This is Apple&\#x27;s long-awaited entry into the foldable phone category, a segment rivals like Samsung and Huawei have led for years, so a fast sellout signals real demand and could accelerate mainstream adoption of foldables. The immediate stock reaction also shows investors treating the launch as a potential new growth driver for Apple&\#x27;s iPhone business, which has matured in recent years. The report gives no pricing, configuration, regional availability or shipment-volume figures, so it is unclear whether the one-minute sellout reflects massive demand or a deliberately limited first batch. Premarket trading is also thin and can exaggerate price moves, so the 2% gain should be read as an early signal rather than a settled market verdict.

telegram · zaihuapd · Oct 16, 12:45

**Background**: Foldable phones work by wrapping a flexible OLED display around a precision hinge, letting one device switch between phone and tablet sizes; the hinge must hold position at multiple angles while withstanding repeated folding. Apple had been the most notable holdout among major smartphone makers, with Samsung, Huawei and others shipping foldables for several years. Premarket trading refers to buying and selling shares before the regular US session opens at 9:30 a.m. ET, and is typically thinner and more volatile than normal hours.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kingsresearch.com/blog/magic-of-foldable-displays">How Foldable Displays Work: Flexible OLED, Hinges &amp; Glass</a></li>
<li><a href="https://www.investopedia.com/terms/p/premarket.asp">Pre-Market Trading Explained: Benefits, Risks, and Opportunities</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#foldable phone`, `#iPhone Duo`, `#market reaction`, `#consumer tech`

---

<a id="item-5"></a>
## [Court Documents Reveal Telegram Handed User Data to U.S. Law Enforcement](https://www.404media.co/heres-what-telegram-giving-data-to-the-u-s-government-looks-like/) ⭐️ 7.0/10

Newly released court documents show that Telegram provided a user&\#x27;s phone number, user ID, and IP address to U.S. law enforcement in response to a U.S. court order, describing the disclosure in its letter as &quot;voluntary&quot; while refusing to acknowledge U.S. jurisdiction. The case concerns Mahmoud Al-Muhtadi, accused of involvement in the October 7, 2023 attacks on Israel, and the documents state that as of January, Telegram had disclosed data on 2,253 users to U.S. authorities. The disclosure directly contradicts Telegram&\#x27;s long-cultivated reputation as a privacy-first messaging platform that resists government data requests, and it raises hard questions about how much user data the company actually holds and how readily it complies with law enforcement. It also matters for the broader debate over platform governance and surveillance, since users in many jurisdictions rely on Telegram precisely because they assume it will not hand over identifying information. Telegram&\#x27;s letter characterizes the handover as voluntary even while the company denies being subject to U.S. jurisdiction, a combination that is legally unusual and could complicate future challenges to similar orders. The figure of 2,253 users whose data was disclosed as of January suggests this is not an isolated case but part of a broader pattern of compliance with U.S. legal demands.

telegram · zaihuapd · Oct 16, 14:57

**Background**: Telegram is a messaging app widely used for its end-to-end encrypted chats and its policy of storing little user data, and it has historically refused or publicly resisted government requests for information, at times ignoring court orders from countries it said had no jurisdiction over it. Its founder, Pavel Durov, built the platform&\#x27;s reputation around that stance, and the company only revised its privacy policy in September 2024 to allow IP addresses and phone numbers to be shared with authorities in response to valid legal requests. These newly released documents therefore show that the gap between Telegram&\#x27;s public positioning and its actual practice with U.S. law enforcement is wider than many users assumed.

**Tags**: `#Telegram`, `#privacy`, `#surveillance`, `#law enforcement`, `#data disclosure`

---