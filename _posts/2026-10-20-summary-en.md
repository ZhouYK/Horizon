---
layout: default
title: "Horizon Summary: 2026-10-20 (EN)"
date: 2026-10-20 23:03:27 +0000
lang: en
report: default
---

> From 168 items, 7 important content pieces were selected

---

1. [DeepSeek Reportedly Co-Designs Huawei&\#x27;s Future AI Chips](#item-1) ⭐️ 8.0/10
2. [DeepSeek Open-Sources DeepInfer, Its Internal Large-Scale Inference Framework](#item-2) ⭐️ 8.0/10
3. [OpenAI&\#x27;s New Models Reportedly Hit 97.9% Accuracy on COBOL Migration](#item-3) ⭐️ 8.0/10
4. [NVIDIA reportedly bars small cloud providers from GTC Berlin over AMD, Google TPU use](#item-4) ⭐️ 7.0/10
5. [Xiaomi MiMo-V2.6-Pro Launches on WorkBuddy, Claims Top Open-Source Ranking](#item-5) ⭐️ 7.0/10
6. [X retunes recommendation algorithm to favor dwell time and completion rate](#item-6) ⭐️ 6.0/10
7. [China&\#x27;s MIIT Tightens Market Entry Rules for &\#x27;Innovative&\#x27; Car Designs](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek Reportedly Co-Designs Huawei&\#x27;s Future AI Chips](https://www.theinformation.com/articles/deepseek-shaping-huaweis-ai-chips-growing-challenge-nvidia) ⭐️ 8.0/10

According to The Information, DeepSeek is working closely with Huawei on the design of future AI chips slated for 2027 and beyond, with Huawei engineers having been stationed at DeepSeek&\#x27;s offices for an extended period. DeepSeek&\#x27;s feedback on model computation and inter-processor data transfer is reportedly being folded directly into the chip designs — a deeper relationship than the usual supplier-customer dialogue. This kind of vertical co-design — where a model developer helps shape the silicon it will run on — could help China build frontier AI models with far less reliance on Nvidia hardware. If it works, it strengthens Huawei&\#x27;s Ascend ecosystem as a genuine domestic alternative at a time when U.S. export controls limit Chinese access to top-end Nvidia accelerators. The collaboration reportedly covers upcoming chips for 2027 and later, and the article notes that DeepSeek has not abandoned Nvidia — it is still seeking access to the company&\#x27;s advanced processors. The disclosure comes from people familiar with the matter cited by The Information, and neither Huawei nor DeepSeek has publicly confirmed the arrangement.

telegram · zaihuapd · Oct 20, 05:10

**Background**: DeepSeek is a Hangzhou-based AI lab, funded and owned by the quantitative hedge fund High-Flyer, known for releasing open-weight models such as R1 at remarkably low training cost. Huawei designs its Ascend AI processors through its HiSilicon chip subsidiary, which builds them on a proprietary Da Vinci compute architecture. Because U.S. export controls block Chinese firms from buying Nvidia&\#x27;s most advanced GPUs, domestic accelerators like Ascend have become strategically important, and software and model-level tuning has become a key battleground for making that hardware competitive.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_%28Company%29">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Huawei_Ascend_%28chip%29">Huawei Ascend (chip)</a></li>
<li><a href="https://www.jademond.com/glossary/ascend-ai">Huawei Ascend AI Chips : Specs, History, and 2026 Roadmap...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Huawei`, `#DeepSeek`, `#semiconductors`, `#Nvidia`

---

<a id="item-2"></a>
## [DeepSeek Open-Sources DeepInfer, Its Internal Large-Scale Inference Framework](https://github.com/deepseek-ai/DeepInfer) ⭐️ 8.0/10

On October 20, DeepSeek open-sourced DeepInfer, the high-performance inference framework that powers its own production services, alongside a companion token codec component called deepseek-recipe. The release claims that a single cluster running the V4.1 Flash model reaches 155 trillion tokens per day of throughput, and it supports distributed inference, speculative decoding, and structured output on both NVIDIA and Huawei Ascend hardware. Most labs keep their production serving stack proprietary, so open-sourcing DeepInfer exposes the real architectural choices DeepSeek makes for serving at scale, giving the community a reference design rather than a research prototype. Its explicit support for Huawei Ascend alongside NVIDIA is also notable, since hardware diversity is a growing constraint for teams building large inference clusters outside the US ecosystem. The published capabilities include distributed inference, speculative decoding, structured output, and a KVCache that can be retained for more than 72 hours, which matters for long-running agent-style workloads that reuse context. However, the announcement is sparse on design documentation and benchmarks, so the 155 trillion tokens/day figure and the NVIDIA/Ascend parity claims currently rest largely on DeepSeek&\#x27;s own statement rather than reproducible third-party measurements.

telegram · zaihuapd · Oct 20, 09:11

**Background**: Inference is the stage where a trained model actually answers requests, and at DeepSeek&\#x27;s scale the bottleneck is not just single-GPU speed but how to keep thousands of accelerators busy while batching, scheduling, and caching efficiently — that is what a distributed inference framework like DeepInfer handles. Speculative decoding, one of the features it lists, accelerates generation by having a small draft model propose several tokens ahead and letting the large target model verify them in parallel, yielding speedups without changing output quality. The companion deepseek-recipe package is the official library that converts API requests \(messages, chat completions, images\) into DeepSeek V4/V4.1 prompt and token encoding and streams responses back, so the two pieces together cover both the serving engine and the request/token layer.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepInfer">GitHub - deepseek -ai/ DeepInfer : DeepInfer : High-performance...</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-recipe">GitHub - deepseek-ai/ deepseek - recipe · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2401.07851">[2401.07851] Unlocking Efficiency in Large Language Model ... Unlocking Efficiency in Large Language Model Inference: An Introduction to Speculative Decoding for Reducing Latency ... Speculative Decoding: 20-50% Faster LLM Inference Speculative Decoding: Achieving 2-3x LLM Inference Speedup Co-Designing AI Models Using Speculative Decoding for Faster ...</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#open-source`, `#distributed systems`, `#DeepSeek`, `#Ascend/NVIDIA`

---

<a id="item-3"></a>
## [OpenAI&\#x27;s New Models Reportedly Hit 97.9% Accuracy on COBOL Migration](https://openai.com/index/low-resource-programming-languages/) ⭐️ 8.0/10

According to a secondhand summary, OpenAI&\#x27;s newest model family dramatically improves coding performance on low-resource languages such as COBOL, Fortran and Visual Basic: in a 20-language SQLite-from-scratch test, &quot;GPT-6 Astra&quot; reportedly raised average pass rate from 26.8% \(GPT-5.6 Sol\) to 87.4%, while the cheaper &quot;GPT-6 Luna&quot; reached 40.3% at 78% lower API cost. On COBOL-to-modern-language migration, &quot;GPT-6.1 Sol&quot; allegedly jumped from 5.4% to 86.6% accuracy at low reasoning effort \(39% cheaper\) and up to 97.9% at high reasoning effort, with the accompanying evaluation suite open-sourced on GitHub. Legacy COBOL still underpins a huge share of banking, insurance and government systems, and migration projects are notoriously slow and expensive, so a jump from single-digit to near-100% translation accuracy would materially change the economics of modernization. It also signals that frontier labs are now optimizing for long-tail, low-resource languages rather than only Python and JavaScript, and the open-sourced benchmark gives researchers a shared yardstick for code LLM evaluation. The figures come from a Chinese-language Telegram channel summary, and the model names \(GPT-6 Astra, GPT-5.6 Sol, GPT-6 Luna, GPT-6.1 Sol\) are unverified and do not match any publicly announced OpenAI release. The results also illustrate a clear accuracy-per-dollar tradeoff: cost falls sharply at low reasoning effort while accuracy still rises substantially, with the best numbers requiring high reasoning effort, and no independent replication has been published yet.

telegram · zaihuapd · Oct 20, 14:24

**Background**: Low-resource programming languages are languages with little representation in public code and training corpora — COBOL, Fortran, Visual Basic, APL and various domain-specific languages — which makes LLMs markedly worse at writing and translating them than at Python or JavaScript. COBOL in particular dates back to 1959 and still runs much of the world&\#x27;s financial and administrative infrastructure, so &quot;COBOL-to-modern-language migration&quot; \(translating and refactoring legacy code into Java, Python or Go\) is a long-standing, labor-intensive industry problem. Modern reasoning models expose adjustable &quot;reasoning effort&quot; settings, where more internal computation tokens yield higher accuracy at higher cost, making the cost/accuracy tradeoff a central practical concern.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2410.03981v2">A Survey on LLM -based Code Generation for Low - Resource and...</a></li>
<li><a href="https://andrew.ooo/answers/how-to-choose-llm-reasoning-effort-level-2026-guide/">How to Choose LLM Reasoning Effort Levels (2026) - andrew.ooo</a></li>
<li><a href="https://skillmd.ai/tutorials/run-on/cursor-ai/cobol-modernization/">Run cobol -modernization on Cursor AI | SkillMD.ai</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#COBOL`, `#code-migration`, `#LLM-evaluation`, `#legacy-modernization`

---

<a id="item-4"></a>
## [NVIDIA reportedly bars small cloud providers from GTC Berlin over AMD, Google TPU use](https://x.com/SemiAnalysis_/status/2111162214891610496?s=20) ⭐️ 7.0/10

According to a SemiAnalysis report circulating on X and Telegram, NVIDIA refused to let several emerging cloud providers attend its upcoming GTC Berlin conference because those providers had deployed competitor chips such as AMD GPUs and Google TPUs in their own cloud platforms, not for any technical shortcoming. NVIDIA has not publicly commented on the allegation. The claim points to a notable use of leverage by a dominant AI accelerator supplier that is simultaneously a major investor in the same small clouds, raising fresh antitrust and vendor-lock-in questions as AMD, Google and others try to build an alternative to CUDA-based NVIDIA capacity. The restriction reportedly does not apply to hyperscalers, which have enough purchasing volume and in-house silicon to negotiate on equal terms; the report is a secondary relay with no primary sourcing or on-record confirmation, so the scope, formal basis and number of affected firms remain unverified.

telegram · zaihuapd · Oct 20, 12:32

**Background**: NVIDIA GTC \(GPU Technology Conference\) is the company&\#x27;s flagship annual developer and partner event, which has expanded from GPU computing into AI and cloud topics and now runs regional editions such as GTC Berlin. Neo-clouds like CoreWeave and Nebius rent out GPU capacity for AI training and have grown rapidly on NVIDIA hardware; NVIDIA has reportedly made roughly $2 billion strategic investments in each and backstops some of their compute-leasing revenue, giving it substantial influence over their purchasing and roadmap decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E8%8B%B1%E4%BC%9F%E8%BE%BEGTC">英伟达GTC - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI infrastructure`, `#GPU market`, `#antitrust`, `#cloud providers`

---

<a id="item-5"></a>
## [Xiaomi MiMo-V2.6-Pro Launches on WorkBuddy, Claims Top Open-Source Ranking](https://weibo.com/6486870325/5356179212995907) ⭐️ 7.0/10

Xiaomi announced that its MiMo-V2.6-Pro model is now live on the WorkBuddy platform, claiming a score of 46 on the Artificial Analysis Intelligence Index — which it says ranks first among open-source models worldwide. The release also touts 1M-token ultra-long context, multi-agent task division and collaboration, and omni-modal joint understanding across images, video, audio, and text. If the claim holds, this puts a Chinese open-weight model at the top of one of the most closely watched independent model leaderboards, which could shift how developers and enterprises evaluate open-source options against closed flagship APIs. The combination of 1M-token context, multi-agent orchestration, and omni-modal input is specifically aimed at long-horizon agentic workloads rather than simple chat use cases. The announcement is a short promotional post with no benchmark breakdown, evaluation methodology, model size, licensing terms, or pricing disclosed, so the index ranking cannot be independently verified from the post itself. Xiaomi&\#x27;s own model page describes MiMo-V2.6-Pro as a trillion-parameter flagship omni-modal reasoning model, and the broader V2.6 series also includes a Flash variant plus an &quot;UltraSpeed&quot; version claiming up to 20x output speed for latency-sensitive use.

telegram · zaihuapd · Oct 20, 13:40

**Background**: The Artificial Analysis Intelligence Index is a composite benchmark that aggregates around ten separate evaluations to give a single holistic score across mathematics, science, coding, and reasoning, and it is widely cited as a neutral way to compare models across vendors. Xiaomi&\#x27;s MiMo family is the company&\#x27;s in-house large-model line, and the V2.6 series is described as natively omni-modal, meaning the models are trained to handle multiple input modalities rather than having separate vision or audio modules bolted on. WorkBuddy is the agent-style platform where the model is being offered for hands-on use in long-horizon workflows such as long-task hosting, deep research, design drafting, document work, and small tool development. Note that the search results describe a separate Tencent product also named WorkBuddy, so the platform named in Xiaomi&\#x27;s post should not be confused with it.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>
<li><a href="https://mimo.mi.com/models/en-US/mimo-v2.6-pro">Xiaomi MiMo-V2.6 Series: 3 New Models Officially Released</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index v4.3.2</a></li>

</ul>
</details>

**Tags**: `#llm`, `#open-source-models`, `#xiaomi`, `#multimodal`, `#long-context`

---

<a id="item-6"></a>
## [X retunes recommendation algorithm to favor dwell time and completion rate](https://x.com/rohanpaul_ai/status/2112419861767045586) ⭐️ 6.0/10

X has reworked the two-stage ranking mechanism behind its &quot;For You&quot; feed, with the new ranking model weighting user dwell time and post completion rate more heavily; Elon Musk claimed the new model&\#x27;s ability to predict effective time spent is greatly improved. The retrieval stage also changed: the system now embeds users and posts as vectors to pull relevant content from accounts a user doesn&\#x27;t follow, filtering by completion rate so posts that are usually abandoned halfway are less likely to enter the recommendation pool. The change shifts X&\#x27;s optimization target away from clicks and likes toward time actually spent reading, which directly shapes which posts reach millions of users and how creators are incentivized to write. X reports total daily active user time rising from roughly 410 billion seconds in mid-August to about 500 billion seconds in mid-October, a metric Musk has used to argue the platform&\#x27;s engagement is recovering. The system is described as a two-stage pipeline: an earlier retrieval stage that uses vector similarity to surface candidates from outside a user&\#x27;s follow graph, followed by a ranking model that predicts dwell time and completion. Completion rate now acts as a filter in retrieval, so slow-burn or long-form posts that readers commonly drop early may be disadvantaged regardless of how relevant they are, and the reported time-spent figures come from X itself rather than independent measurement.

telegram · zaihuapd · Oct 20, 07:29

**Background**: Large-scale feeds are typically split into retrieval and ranking: retrieval cheaply narrows billions of candidate posts down to a manageable pool, and ranking then orders that pool with a heavier model. Vector-based retrieval represents users and posts as high-dimensional embeddings and matches them by similarity, which lets the system recommend content from accounts a user has never followed. This mirrors a broader industry shift toward &quot;expected watch time&quot; style objectives, a move YouTube made years ago to favor retention over raw clicks.

<details><summary>References</summary>
<ul>
<li><a href="https://fylom.com/episode/45d1bb22-f76d-4b84-80a3-2ef23c48308e">How recommendation algorithms decide what billions of... — Fylom</a></li>
<li><a href="https://www.emergentmind.com/topics/vector-based-retrieval-systems">Vector-Based Retrieval Systems - emergentmind.com</a></li>
<li><a href="https://redis.io/tutorials/building-a-two-tower-recommendation-system-with-redis-vl/">Two-Tower Recommendation System with RedisVL: Vector Search Guide</a></li>

</ul>
</details>

**Tags**: `#recommendation-systems`, `#X/Twitter`, `#ranking-algorithms`, `#user-engagement`, `#social-media`

---

<a id="item-7"></a>
## [China&\#x27;s MIIT Tightens Market Entry Rules for &\#x27;Innovative&\#x27; Car Designs](https://m.chinanews.com/wap/detail/chs/zw/10717890.shtml) ⭐️ 6.0/10

On October 20, China&\#x27;s Ministry of Industry and Information Technology \(MIIT\) announced it will block automotive products with unreasonable innovative designs or insufficient R&amp;D and testing validation from entering the market. Chief Engineer Wang Weiming said at a press conference that products not declared as required or lacking adequate test validation will be denied market access, and the notice brings hidden door handles, soft-close doors and virtual controls under entry management while upgrading 22 recommended standards to mandatory status. The move shifts safety scrutiny from after-sales recalls to the pre-market approval stage, directly affecting how Chinese EV makers design door handles, doors, seats and touch-based controls. Because China is the world&\#x27;s largest auto market and a design trendsetter, the mandatory standards could become a de facto reference for global regulators and for suppliers exporting Chinese-designed vehicles. The notice requires soft-close doors to include anti-pinch protection, bans the use of zero-gravity or rotating seats while the vehicle is in motion, and mandates reliability testing of no less than 30,000 kilometers. Twenty-two previously recommended \(voluntary\) standards are raised to mandatory status, meaning non-compliant models cannot be type-approved for sale.

telegram · zaihuapd · Oct 20, 12:48

**Background**: Hidden \(flush\) door handles and soft-close doors have become signature features of Chinese smart EVs, but they rely on electronic actuation and can trap occupants or fail to open in a crash or power loss. Zero-gravity seats recline occupants into a near-weightless posture that is comfortable when parked but offers poor restraint protection while driving. China&\#x27;s standards system distinguishes recommended \(GB/T\) standards from mandatory \(GB\) ones, and only the latter are enforceable as market-entry conditions — so reclassifying 22 standards is what gives this notice real teeth.

<details><summary>References</summary>
<ul>
<li><a href="https://c.m.163.com/news/a/KKS5HK2R0512D3VJ.html?spss=backflow-index-hotlist">安 全 至上，对 汽 车 隐 藏 式 门 把 手 说“不”| 新京报快评</a></li>
<li><a href="https://www.jfdaily.com/wx/detail.do?id=908220">让 安 全 不再“ 隐 形”， 隐 藏 式 车 门 把 手 将有国家标准</a></li>
<li><a href="https://hqtime.huanqiu.com/article/4TKvz1uNN0z">汽 车 零 重 力 座 椅 热销 舒适与安全该如何兼顾</a></li>

</ul>
</details>

**Tags**: `#automotive safety`, `#regulation`, `#vehicle design`, `#MIIT`, `#standards`

---