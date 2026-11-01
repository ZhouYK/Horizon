---
layout: default
title: "Horizon Summary: 2026-11-01 (EN)"
date: 2026-11-01 23:03:22 +0000
lang: en
report: default
---

> From 150 items, 5 important content pieces were selected

---

1. [OpenAI to merge ChatGPT and Codex quotas, metered by tokens](#item-1) ⭐️ 7.0/10
2. [Sam Altman Apologizes to Mathematicians but Vows to Keep Publishing AI Math Results](#item-2) ⭐️ 7.0/10
3. [CLEAR Report: AI &\#x27;Tokenizer Tax&\#x27; Makes Some Languages Up to 17x Costlier](#item-3) ⭐️ 7.0/10
4. [Germany&\#x27;s governing coalition debates introducing an AI tax](#item-4) ⭐️ 6.0/10
5. [xAI Adds Text Watermarks to Grok Output, Rolling Out Globally](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI to merge ChatGPT and Codex quotas, metered by tokens](https://x.com/thsottiaux/status/2116692529970311254) ⭐️ 7.0/10

OpenAI&\#x27;s Tibo \(thsottiaux\) announced that starting in December, ChatGPT and Codex usage quotas will be shared across the Plus, Pro, and Business plans, timed to the folding of Work&\#x27;s agentic capabilities into the main ChatGPT experience. Quota consumption will now be measured in tokens rather than message counts, with the more advanced the model and the more complex the task, the more quota consumed. This changes how a single subscription is consumed: developers and power users who previously treated Codex as a separate allowance will now draw from the same pool as their everyday chatting, so heavy agentic coding sessions can eat into the quota they rely on elsewhere. It also signals that OpenAI is consolidating ChatGPT, Codex, and Work into one agent-centric product with compute-based rather than message-based pricing. According to the announcement, instant chat does not consume quota, and users can see their combined remaining usage and reset time in settings; once the quota runs out they can wait for the reset, upgrade their plan, or purchase credits. Because metering is token-based, cost scales with model tier and task complexity, making long agent runs and advanced models the most expensive things to do.

telegram · zaihuapd · Nov 1, 01:29

**Background**: Codex is OpenAI&\#x27;s coding agent, included with ChatGPT plans, that can plan, build, refactor, review, and ship code, and it is typically used in long, token-hungry sessions. ChatGPT Work is OpenAI&\#x27;s agentic offering that pulls together tools, files, and context and can follow a task across applications for hours; its capabilities are now being merged into the main ChatGPT product. A token is the basic unit of text a language model reads and generates, and it is the standard basis for metering and billing model usage, which is why OpenAI is switching from counting messages to counting tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://www.cls.cn/detail/2422216">OpenAI推出 ChatGPT Work 智 能 体 可持续数小时跟进任务</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#Codex`, `#pricing`, `#token-based billing`

---

<a id="item-2"></a>
## [Sam Altman Apologizes to Mathematicians but Vows to Keep Publishing AI Math Results](https://futurism.com/artificial-intelligence/sam-altman-mathematicians-math-slop) ⭐️ 7.0/10

OpenAI CEO Sam Altman used a podcast appearance to directly address the disruption AI is causing in mathematics, apologizing to mathematicians whose work has been upended while insisting that OpenAI will keep publishing AI-generated mathematical results for the sake of humanity&\#x27;s understanding of the universe. The remarks follow OpenAI&\#x27;s claim that a swarm of roughly 10,000 AI agents solved a case of the Navier–Stokes problem, and its subsequent release of hundreds of unreviewed AI-generated proofs that prominent mathematicians described as difficult or impossible to understand. This is the first time a top AI lab leader has publicly acknowledged the collateral damage AI math pushes inflict on academic mathematicians, yet the promise to keep publishing unreviewed results signals the tension is unlikely to ease. It matters because it sets a precedent for how frontier labs release machine-generated science — potentially bypassing peer review and reshaping research priorities toward problems that suit AI methods. The disputed Navier–Stokes work was accompanied by a formalization in the Lean proof assistant, and OpenAI said it would not claim the $1 million Clay Millennium Prize for the result, which the Clay Mathematics Institute still lists as active. Critics&\#x27; core objection is that hundreds of released proofs have not been peer reviewed and are hard for humans to verify, prompting efforts such as a human audit of OpenAI&\#x27;s AI-generated proofs and the Leiden Declaration on AI and Mathematics.

telegram · zaihuapd · Nov 1, 02:54

**Background**: The Navier–Stokes equations describe fluid motion, and whether their solutions in three-dimensional space always stay smooth — or can blow up into a singularity in finite time — is one of the seven Millennium Prize Problems posed by the Clay Mathematics Institute in 2000. Mathematical results are traditionally validated through human-readable proofs vetted by peer review, whereas machine-generated proofs increasingly rely on formal verification in tools like Lean, which can check correctness but not necessarily explain the argument to a human. OpenAI&\#x27;s claim that thousands of cooperating AI agents produced the result adds a new wrinkle: the scale and opacity of such swarms make conventional review even harder.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_problem">Navier-Stokes problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Leiden_Declaration_on_Artificial_Intelligence_and_Mathematics">Leiden Declaration on Artificial Intelligence and Mathematics</a></li>
<li><a href="https://arxiv.org/html/2608.14673v3">A Human Audit of OpenAI’s AI-Generated Mathematical Proofs</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI for mathematics`, `#Sam Altman`, `#research integrity`, `#Navier-Stokes`

---

<a id="item-3"></a>
## [CLEAR Report: AI &\#x27;Tokenizer Tax&\#x27; Makes Some Languages Up to 17x Costlier](https://clear-languages.org/blog/the-tokenizer-tax) ⭐️ 7.0/10

The CLEAR research consortium published a report finding that mainstream AI tokenizers are heavily optimized for English and other high-resource languages, so identical content can consume up to 17 times more tokens in some languages. In its example, a sentence that takes 13 tokens in English requires 26 tokens in Malayalam and 78 in Amharic, with the study covering roughly 200 languages. Because most commercial LLM APIs bill per token and every model has a fixed context window, this disparity translates directly into higher costs, slower responses, and less usable context for speakers of under-served languages. It turns tokenization from a purely technical detail into a multilingual AI fairness and accessibility issue that affects both end users and developers building for non-English markets. The finding is a headline-level summary rather than a full methodology: the report gives illustrative token counts and a 17x maximum spread but does not expose, in the digest, which tokenizers or model families were benchmarked. Token inflation also varies by tokenizer vocabulary and by how aggressively a model falls back to byte-level encoding for scripts underrepresented in its training corpus, so the exact multiplier will differ across providers.

telegram · zaihuapd · Nov 1, 16:06

**Background**: Tokenization is the step that splits raw text into discrete units \(tokens\) before a language model processes it; modern LLMs typically use subword algorithms such as byte-pair encoding \(BPE\), which learn frequent character sequences from training data. Because that training data is overwhelmingly English and dominated by a handful of high-resource languages, the learned vocabulary covers common English words with single tokens while rarer scripts get chopped into many small fragments. NLP research has long distinguished &\#x27;high-resource&\#x27; from &\#x27;low-resource&\#x27; languages, a distinction driven by the volume of usable digitized text rather than by speaker population — Hindi or Amharic can be low-resource despite hundreds of millions of speakers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/what-is-tokenization">Tokenization in NLP: How It Works, Challenges, and Use... | DataCamp</a></li>
<li><a href="https://www.lifewood.com/blogs/high-resource-vs-low-resource-languages/">High-Resource vs Low-Resource Languages in AI Training</a></li>

</ul>
</details>

**Tags**: `#tokenization`, `#multilingual NLP`, `#LLM cost efficiency`, `#AI fairness`, `#research report`

---

<a id="item-4"></a>
## [Germany&\#x27;s governing coalition debates introducing an AI tax](https://www.tagesschau.de/inland/ministerin-prien-ki-steuer-100.html) ⭐️ 6.0/10

Germany&\#x27;s black-red governing coalition is debating whether and how to tax revenue generated by AI, with Family Minister and CDU deputy leader Karin Prien telling Der Stern that taxation becomes unavoidable once value creation is primarily driven by AI. Digital Minister Wildberger initially called for an AI tax to counter job losses before softening her position and saying growth should come first, while Economy Minister Reiche argues AI should be introduced before any tax and Chancellor Merz remains cautious. The debate signals that AI taxation is moving from academic and civil-society proposals into mainstream European policy discussion, and any German framework could set a precedent for how governments capture value from AI-driven productivity gains. It also matters for employers and workers, since the revenue would in principle fund social protection for those displaced by automation. No concrete legislative proposal exists yet: the SPD had already endorsed fair taxation of profits in September, but the coalition has not agreed on a base \(revenue versus profit\), a rate, or a timeline, and ministers openly disagree on sequencing. The idea echoes Bill Gates&\#x27; long-standing call for taxing robots and AI, and the open question is how to define and measure the AI-attributable share of a company&\#x27;s value creation without penalizing adoption.

telegram · zaihuapd · Nov 1, 03:55

**Background**: An &quot;AI tax&quot; \(sometimes framed as a &quot;robot tax&quot;\) is a proposed levy on the revenue or profits that firms generate through AI systems or automation, rather than on AI development itself. Supporters argue it offsets the erosion of payroll and corporate tax bases as machines take over work and funds retraining or social insurance; critics warn it would slow adoption and push investment abroad. Germany&\#x27;s current government is a grand coalition of the conservative CDU/CSU and the centre-left SPD, and its ministries have already staked out different positions, so the discussion remains at the stage of political signalling rather than draft law.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/German_governing_coalition">German governing coalition - Wikipedia</a></li>
<li><a href="https://baike.baidu.com/item/%E6%9C%BA%E5%99%A8%E4%BA%BA%E7%A8%8E/22085934">机器人税 - 百度百科 机器人税的理论争鸣和发展趋势问题研究 中国税务学会 - cti.ctax.org.cn 智能化时代征收AI机器人税的路径选择 以激励科技发展与防范劳动力市场... 如果AI抢走饭碗，谁来交税？ - 虎嗅网 人工智能时代机器人税征收探讨- - jjykj.com</a></li>
<li><a href="https://www.shuzhipunk.com/articles/vACCHgbXzcr">比尔·盖茨重申“机器人税”：对替代人类的AI征收等额薪资税</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#AI taxation`, `#Germany`, `#regulation`, `#employment`

---

<a id="item-5"></a>
## [xAI Adds Text Watermarks to Grok Output, Rolling Out Globally](https://x.com/AndrewCurran_/status/2116654648082022668) ⭐️ 6.0/10

xAI has announced that text generated by Grok now carries a watermark, and the feature is being rolled out globally. According to Andrew Curran, xAI was the last major model provider without text watermarking, so only ChatGPT in North America now remains without it. Text watermarking is becoming a de facto baseline for major model providers, and its adoption by the last holdout signals that AI content provenance is shifting from voluntary experiment to expected default. This matters for anyone publishing AI-assisted text, for detection tools and platforms trying to label synthetic content, and for compliance with transparency requirements emerging in regulation such as the EU AI Act. xAI&\#x27;s announcement gave no technical detail on the watermarking method, its robustness against paraphrasing or translation, or whether a public detection API will be offered. Text watermarks are generally statistical signals embedded during token sampling, which makes them fragile to rewriting and only detectable by parties holding the corresponding key.

telegram · zaihuapd · Nov 1, 04:39

**Background**: Unlike an image watermark, a text watermark is not a visible mark but a statistical pattern embedded in word choices that is imperceptible to readers yet detectable by an algorithm that knows the key. A common approach is the &\#x27;green list&\#x27; method: the model secretly favors a pseudo-random subset of vocabulary \(chosen by a keyed hash\) at each step, and a detector later runs a statistical test to see whether far more green-list tokens appear than chance would predict. Because such marks can be weakened by paraphrasing or editing, watermarking is usually discussed alongside provenance standards like C2PA, which attach cryptographically signed metadata to content rather than modifying the content itself.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kongchang.com/articles/jie-mi-aiwen-ben-shui-yin-ru-he-shi-bie-ji-qi-sheng-cheng-nei-rong">AI文本水印技术原理详解：绿名单机制与检测方法 - 控场AI</a></li>
<li><a href="https://gentang.github.io/zh/blog/watermarking_on_aigc/">Anthropic要在 文 本 中加 水 印 ，这是如何做到的呢？ · 小胖笔记</a></li>
<li><a href="https://c2pa.org/">C 2 PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**Tags**: `#AI watermarking`, `#content provenance`, `#xAI/Grok`, `#AI regulation`, `#industry news`

---