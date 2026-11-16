---
layout: default
title: "Horizon Summary: 2026-11-16 (EN)"
date: 2026-11-16 23:03:48 +0000
lang: en
report: default
---

> From 179 items, 7 important content pieces were selected

---

1. [Alibaba Launches Qwen4-Max: 2.4T-Parameter Sparse MoE With Native Vision and 1M-Token Context](#item-1) ⭐️ 8.0/10
2. [US Extends Advanced AI Chip Export Controls to Remote Cloud Access](#item-2) ⭐️ 8.0/10
3. [Tencent Hunyuan Releases Hy4 flash: 224B-Parameter Multimodal MoE with 1M Context and Steep Price Cuts](#item-3) ⭐️ 7.0/10
4. [Amazon: Artex-Driven AI Agents Stole API Keys to Self-Fund LLM Calls](#item-4) ⭐️ 7.0/10
5. [Shandong University team claims first conditional proof of Goldbach&\#x27;s conjecture](#item-5) ⭐️ 7.0/10
6. [DeepSeek Caps App and Web Usage, Citing Insufficient Compute](#item-6) ⭐️ 6.0/10
7. [Grok Text Watermarking Now Off by Default in API](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Alibaba Launches Qwen4-Max: 2.4T-Parameter Sparse MoE With Native Vision and 1M-Token Context](https://mp.weixin.qq.com/s/pJUt0xwD6H-WMyzd8TjZaQ) ⭐️ 8.0/10

Alibaba&\#x27;s Tongyi Qianwen \(Qwen\) team officially released Qwen4-Max, a new flagship model built on a sparse Mixture-of-Experts architecture with 2.4 trillion total parameters, native vision understanding, and a context window of up to one million tokens. The model is already live on the Qwen AI platform and API, and the team says smaller Qwen4 series models with published weights will follow. A 2.4-trillion-parameter flagship with native multimodality and long context puts Alibaba&\#x27;s model directly in the race with top-tier frontier systems, while the roughly 58% drop in per-task cost makes agentic and long-document workloads meaningfully cheaper. The promise of open-weight smaller Qwen4 models also matters to developers who want to self-host rather than depend on a closed API. Qwen4-Max cuts the average cost per task from 26.58 yuan to 11.16 yuan \(a drop of nearly 58%\) and consumes roughly 50% fewer tokens, with API pricing lowered accordingly; the team also says its frontend coding ability ranks among the global leaders in the blind Code Arena evaluation. Notably, the future smaller Qwen4 models are described as open-weight rather than fully open-source, meaning the trained parameters will likely be downloadable while training code and data may remain undisclosed.

telegram · zaihuapd · Nov 16, 02:52

**Background**: A sparse Mixture-of-Experts \(MoE\) model splits its parameters into many &quot;expert&quot; subnetworks and uses a router to activate only the top-K experts for each token, so total parameter count can be enormous while the compute used per token stays comparatively small. A context window is the maximum amount of text \(measured in tokens\) a model can attend to at once, so a million-token window means whole codebases or book-length documents can be processed in one pass. &quot;Open weights&quot; is distinct from &quot;open source&quot;: it usually means the trained parameters are downloadable and runnable, but the license may restrict commercial use and the training code and data are typically not released.

<details><summary>References</summary>
<ul>
<li><a href="https://researchaudio.io/p/mixture-of-experts-moe-in-large-language-models">Mixture of Experts ( MoE ) in Large Language Models</a></li>
<li><a href="https://www.promptquorum.com/local-llms/open-weight-vs-open-source-ai-models">Open Weight vs Open Source AI Models 2026: Key Differences</a></li>
<li><a href="https://syntackle.com/blog/long-context-window-ai-model-catch/">A Million Token Context Window Isn&#x27;t What You Think It Is</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Qwen`, `#MoE`, `#open-weights`, `#model-release`

---

<a id="item-2"></a>
## [US Extends Advanced AI Chip Export Controls to Remote Cloud Access](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

On November 16, 2026, the US Commerce Department&\#x27;s Bureau of Industry and Security \(BIS\) issued an interim final rule that extends advanced AI chip and server export controls to remote access, closing the loophole whereby foreign firms rent US-made compute housed in third-country data centers instead of importing the hardware. The rule additionally requires licenses for re-exports of AI chips to Indonesia, Malaysia, Singapore, Thailand and Brazil. This closes the most significant remaining workaround in the US chip control regime: instead of shipping GPUs abroad, restricted buyers could simply rent them remotely, so the new licensing trigger on compute access directly affects Chinese and other embargoed-country firms&\#x27; ability to train frontier models. It also forces global cloud providers and multinationals to reassess where AI workloads physically run, adding a compliance layer to international AI infrastructure planning. According to TechCrunch, the remote-access provisions target companies based in the US&\#x27;s D:5 embargoed group, which covers China, Russia, Iran, North Korea and 18 other countries, and under the interim rule firms must obtain licenses to export AI chips if they may supply compute to China or other restricted destinations. Because it is an interim final rule, the controls take effect quickly, with public comment to follow rather than precede enforcement.

telegram · zaihuapd · Nov 16, 14:44

**Background**: The US controls exports of advanced semiconductors through the Export Administration Regulations \(EAR\), administered by BIS: shipping a controlled chip or server to a restricted destination or end user normally requires a license. A &quot;re-export&quot; is when a US-origin item — or a foreign-made item containing controlled US technology — is shipped from one foreign country to another, which is why Washington can impose licensing conditions on transactions that never touch US soil. The gap these rules address is that physical controls target the movement of hardware, whereas remote cloud access leaves the rack in place and moves only the workload, letting restricted users tap US-grade compute through data centers in third countries.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/16/us-tightens-ai-chip-export-controls-to-deter-chinese-companies-from-accessing-compute-remotely/">US tightens AI chip export controls to deter Chinese ...</a></li>
<li><a href="https://kpmg.com/us/en/taxnewsflash/news/2026/11/commerce-advanced-semiconductor-export-controls.html">U.S. Commerce restricts remote access to advanced ...</a></li>
<li><a href="https://media.bis.gov/learn-support/what-reexport">What is a reexport? | Bureau of Industry and Security</a></li>

</ul>
</details>

**Tags**: `#export-controls`, `#AI-chips`, `#policy`, `#semiconductors`, `#geopolitics`

---

<a id="item-3"></a>
## [Tencent Hunyuan Releases Hy4 flash: 224B-Parameter Multimodal MoE with 1M Context and Steep Price Cuts](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

On November 16, Tencent Hunyuan launched Hy4 flash, a multimodal Mixture-of-Experts model with 224B total parameters \(64B of which come from Engram\) and only 12B activated per token, supporting a 1M-token context window. API pricing is set at 0.5 yuan per million input tokens and 2 yuan per million output tokens, dropping to just 0.02 yuan on cache hits, and the model is already live on Tencent Cloud TokenHub, WorkBuddy, Yuanbao, WeCom, QQ, ima and Marvis, with OpenRouter and an open-source release planned. Hy4 flash pushes the Chinese LLM price war further by pairing long-context multimodal capability with per-task costs Tencent claims are 13x to 20x lower than its previous Hy models, which makes high-volume agent and everyday assistant workloads far cheaper to run. The planned open-sourcing also means the architecture and serving recipe could spread beyond Tencent&\#x27;s own products, pressuring rivals on both price and efficiency. Tencent claims Hy4 flash&\#x27;s WorkIndex cost per task is 1/13 that of Hy4 preview and 1/20 that of Hy4, with KV cache size just 1/24 of Hy3 and 1/6 of Hy4 thanks to end-to-end optimizations including hybrid attention, LatentMoE and Engram in pretraining. Promotional terms run until November 30 \(free WorkBuddy usage and 50% off API\), but the release is accompanied by no independent benchmark numbers, so the &quot;slightly better than Hy4 preview&quot; quality claim remains self-reported.

telegram · zaihuapd · Nov 16, 07:17

**Background**: Mixture-of-Experts \(MoE\) models split the feed-forward layers into many separate &quot;experts&quot; and route each token to only a few of them, so a model can hold a very large total parameter count while keeping the compute per token \(the &quot;activated&quot; parameters\) small. LatentMoE, a refinement of this design, first projects each token into a smaller latent dimension and runs the routed experts there before projecting back, cutting memory-bandwidth and communication overhead during serving. Engram is a conditional-memory module that adds a scalable lookup-style memory to the model, complementing sparsity in computation with sparsity in memory. The KV cache stores previously computed attention keys and values so that decoding only processes new tokens; its size is a major driver of inference memory cost, which is why the reported 1/24 reduction matters for serving long 1M-token contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://research.nvidia.com/labs/nemotron/LatentMoE/">Think Smart About Sparse Compute: LatentMoE for Higher ...</a></li>
<li><a href="https://matteogiardino.com/en/blog/deepseek-engram-explained-conditional-memory-scalable-lookup">DeepSeek Engram Explained: Scalable Lookup for Local LLMs</a></li>
<li><a href="https://medium.com/@foks.wang/what-is-an-llm-really-doing-during-inference-its-more-than-predicting-the-next-token-930dd4e2b889">What Is an LLM Really Doing During Inference ? It’s More... | Medium</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Tencent Hunyuan`, `#MoE`, `#multimodal`, `#API pricing`

---

<a id="item-4"></a>
## [Amazon: Artex-Driven AI Agents Stole API Keys to Self-Fund LLM Calls](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

Amazon Threat Intelligence reported that attackers used Artex, an open-source agentic AI penetration-testing framework written in Go, to drive autonomous AI agents that harvested exposed API keys from publicly reachable AI applications such as LiteLLM and Dify. The agents validated the stolen keys, pooled them into a shared repository, and used them to pay for further LLM inference; the campaign ran from October 3 and was disrupted on November 5 when AWS&\#x27;s MadPot honeypot network captured the activity. This is one of the first documented real-world cases of an autonomous AI agent chain not just attacking systems but monetizing stolen credentials to sustain its own compute costs, creating a self-funding attack loop. It signals a shift toward machine-speed offensive operations that directly threaten any organization exposing LLM gateways or inference APIs on the public internet. Amazon attributed the activity to a China-linked threat group with only moderate confidence, and cautioned that not all listed targets were actually compromised, with potentially affected AWS customers notified individually. AWS detected the campaign because the Artex agents sent their requests — along with their own campaign records — to MadPot sensors configured to masquerade as popular LLM inference APIs, though the reporting relays limited technical detail.

telegram · zaihuapd · Nov 16, 13:00

**Background**: Artex \(also written ARTEX\) is an open-source, Go-based framework that orchestrates large language models to automate tasks across the cyberattack lifecycle, effectively acting as an autonomous penetration-testing agent. LiteLLM and Dify are widely used open-source tools that sit in front of model traffic and hold provider API keys, so a leaked key from either can grant an attacker paid access to commercial LLM services. AWS&\#x27;s MadPot is a honeypot network operated since the late 2010s that lures attackers into fake targets so Amazon can study their tools and infrastructure and warn customers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime">Meet MadPot, a threat intelligence tool Amazon uses to ... How AWS threat intelligence deters threat actors Amazon Threat Intelligence observes threat actors running ... AWS’ MadPot Honeypot Operation Corrals Threat Actors AWS Pulls Back the Curtain on &#x27;MadPot,&#x27; Its Internal Security ... Amazon spins up AI honeypot, grabs ARTEX attack chain.</a></li>
<li><a href="https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html">Chinese Hackers Use AI-Powered ARTEX to Target Over 200...</a></li>
<li><a href="https://www.litellm.ai/security">Security | LiteLLM</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#cybercrime`, `#API key theft`, `#cloud security`, `#threat intelligence`

---

<a id="item-5"></a>
## [Shandong University team claims first conditional proof of Goldbach&\#x27;s conjecture](https://mrc.sdu.edu.cn/info/1018/2193.htm) ⭐️ 7.0/10

Li Jiamin and Liu Jianya of Shandong University have posted a paper claiming that, assuming the Generalized Riemann Hypothesis for Dirichlet L-functions together with one of two additional spectral hypotheses, every sufficiently large even number can be written as the sum of two primes, with both primes lying between one-third and two-thirds of that even number. The authors describe it as the first conditional proof of the binary Goldbach conjecture covering all sufficiently large even numbers, while stressing it is not unconditional and that GRH alone is not enough to yield the result. Goldbach&\#x27;s conjecture is one of the oldest unproved statements in mathematics, and any new route toward it — especially one that goes beyond the classical sieve and circle methods — is of real interest to analytic number theorists. If the argument survives scrutiny, it would establish a new conditional framework linking prime additive problems to spectral hypotheses, though the reliance on unproven assumptions means it does not settle the conjecture itself. The result is conditional on GRH for Dirichlet L-functions plus one of two additional spectral hypotheses, and the authors explicitly note that GRH alone is insufficient; the method is described as differing from the classical sieve and circle methods. The paper appears as a preprint-level announcement on the university&\#x27;s mathematics research center page and has not been peer-reviewed, so the claim should be treated as high-value but unverified.

telegram · zaihuapd · Nov 16, 16:01

**Background**: Goldbach&\#x27;s conjecture states that every even number greater than 2 is the sum of two primes; it has been attacked since the 1920s mainly through the circle method of Hardy and Littlewood and through sieve methods, which produced results such as Chen Jingrun&\#x27;s &\#x27;1+2&\#x27; theorem but never the full &\#x27;1+1&\#x27;. The Riemann Hypothesis concerns the zeros of the Riemann zeta function, and its generalization to Dirichlet L-functions — the GRH — asserts that all nontrivial zeros of those functions lie on the critical line with real part one-half; many conditional results in number theory are proved under this assumption. &\#x27;Spectral hypotheses&\#x27; here refer to additional unproved assumptions of a spectral/automorphic nature that the authors need on top of GRH.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/%E5%93%A5%E5%BE%B7%E5%B7%B4%E8%B5%AB%E7%8C%9C%E6%83%B3">哥德巴赫猜想 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/%E7%8B%84%E5%88%A9%E5%85%8B%E9%9B%B7L%E5%87%BD%E6%95%B8">狄 利 克 雷 L 函 数 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.baike.com/wikiid/2004433996556203846">广 义 黎 曼 猜 想 -快懂百科</a></li>

</ul>
</details>

**Tags**: `#Goldbach conjecture`, `#number theory`, `#analytic number theory`, `#conditional proof`, `#Riemann hypothesis`

---

<a id="item-6"></a>
## [DeepSeek Caps App and Web Usage, Citing Insufficient Compute](https://www.chinastarmarket.cn/detail/2535076) ⭐️ 6.0/10

DeepSeek has introduced usage restrictions on its App and web chat interface, citing insufficient compute capacity. According to user reports, long conversations inactive for more than 7 days are no longer retained, single-message input is capped at roughly 40,000 characters, and a daily conversation quota now triggers a &quot;server busy, usage limit reached&quot; message once exhausted. The change shows that even a leading Chinese LLM lab with free consumer chat is being forced into inference rationing, a signal that serving capacity rather than model quality is becoming the binding constraint. It affects millions of App and web users who rely on DeepSeek for long documents and multi-session work, and it may push heavier users toward the paid API or competing models. The limits are concrete and user-visible: a ~40k-character per-message cap, 7-day expiry for inactive long conversations, and a daily quota with an explicit capacity-related error message. Notably, these restrictions target the free consumer surfaces rather than the API, so developers integrating through the API are not directly affected by this particular policy change.

telegram · zaihuapd · Nov 16, 04:30

**Background**: DeepSeek is a Chinese AI lab known for releasing open-source frontier models and offering free chat through its own App and website. Running inference for a large free user base is expensive: every long conversation and long input consumes GPU memory and compute, and context windows in particular scale serving costs sharply. The AI industry more broadly is entering a period of compute scarcity, in which providers increasingly ration inference through quotas, shorter context, and tiered access rather than absorbing unlimited demand.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://www.baristalabs.io/blog/ai-inference-rationing-smb-planning-2026">AI Compute Scarcity and Inference Rationing: What SMBs Should Do</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#LLM infrastructure`, `#compute scarcity`, `#AI product policy`, `#China AI industry`

---

<a id="item-7"></a>
## [Grok Text Watermarking Now Off by Default in API](https://x.com/mark_k/status/2121975392554619298) ⭐️ 6.0/10

Grok&\#x27;s text watermarking is now disabled by default in the API, according to a post shared by Mark Kretschmann and confirmed by Elon Musk. Musk said watermarks will be turned on only when required by law or when a user explicitly requests them. Because developers building on Grok will no longer receive watermarked text by default, this shifts the burden of AI-content provenance onto application builders and their customers. It also contrasts with providers that treat watermarking as a default transparency measure and could affect platforms that rely on watermarks for moderation or compliance. The post does not specify which watermarking technique Grok uses, whether the change applies retroactively, or whether consumer-facing Grok products behave the same way. The &\#x27;legally required&\#x27; exception means default behavior will vary by jurisdiction, so developers should verify local disclosure rules before shipping.

telegram · zaihuapd · Nov 16, 09:55

**Background**: Text watermarking for AI systems embeds hidden, detectable signals in generated output so that AI-originated text can later be identified. Provenance standards such as C2PA provide an open technical framework for recording the origin and edit history of digital content. Some AI providers have adopted watermarking while removal tools have also appeared, highlighting the tension between transparency, usability, and enforcement.

<details><summary>References</summary>
<ul>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>
<li><a href="https://m.ithome.com/html/991384.htm">Anthropic 推出 AI 文 本 水 印 后，各类去 水 印 工 具开始涌现 - IT之家</a></li>

</ul>
</details>

**Tags**: `#AI watermarking`, `#Grok`, `#API policy`, `#content provenance`, `#AI regulation`

---