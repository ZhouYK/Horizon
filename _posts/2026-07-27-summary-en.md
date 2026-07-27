---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
report: default
---

> From 306 items, 9 important content pieces were selected

---

1. [Google announces Gemini 4, its most ambitious pretraining project, expected late 2026](#item-1) ⭐️ 9.0/10
2. [Moonshot AI Open-Sources Kimi K3: First 2.8T Parameter Model](#item-2) ⭐️ 9.0/10
3. [Fastjson2 RCE Vulnerability Disclosed, No Patch Available](#item-3) ⭐️ 8.0/10
4. [China Begins Mass Production of Domestic DUV Lithography Tools](#item-4) ⭐️ 8.0/10
5. [Huawei Reportedly Plans DRAM Fab With Partner, Denies Claim](#item-5) ⭐️ 7.0/10
6. [Alibaba Launches Qwen Office Beta with AI PPT, Tables, and Computer Control](#item-6) ⭐️ 6.0/10
7. [China Rejects US Sanctions Threat Over AI Model Distillation](#item-7) ⭐️ 6.0/10
8. [Hugging Face AI Breach Sparks Debate on Open vs Closed Models](#item-8) ⭐️ 6.0/10
9. [Samsung may use Chinese DRAM for mid-range phones](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Google announces Gemini 4, its most ambitious pretraining project, expected late 2026](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 9.0/10

Google CEO Sundar Pichai revealed during Alphabet&\#x27;s Q2 2026 earnings call that Gemini 4 is in training with massive resources, targeting a release in November or December 2026. This announcement signals Google&\#x27;s commitment to staying at the forefront of AI, as Gemini 4 is described as its most ambitious pretraining project, aiming to catch up in areas like coding and agent capabilities. Pichai emphasized that computing resources will be prioritized for frontier AGI development. The company admitted falling behind in coding and agent capabilities and hopes Gemini 4 will close the gap. Additionally, the Gemini 3.x Flash series will maintain nearly monthly updates focusing on smart coding improvements.

telegram · zaihuapd · Jul 27, 04:06

**Background**: Gemini is Google&\#x27;s family of large language models, competing with OpenAI&\#x27;s GPT series. Pretraining is the initial phase where models learn from massive datasets to develop general language understanding. Google&\#x27;s previous models, like Gemini 3.5 Pro, faced delays, raising concerns about the pace of its AI iteration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.clrn.org/what-is-pretraining-and-post-training-ai/">What is Pretraining and Post-Training AI? - California ...</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 .6 Flash — Google DeepMind</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Gemini`, `#Google`, `#Large Language Models`, `#Pre-training`

---

<a id="item-2"></a>
## [Moonshot AI Open-Sources Kimi K3: First 2.8T Parameter Model](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 9.0/10

Moonshot AI has open-sourced Kimi K3 on Hugging Face, a 2.8 trillion parameter Mixture-of-Experts model with 104B activated parameters, making it the first publicly available 3T-scale model. It introduces novel architectures including Kimi Delta Attention \(KDA\) and Attention Residuals \(AttnRes\) under the Stable LatentMoE framework. As the first open-source model at this scale, Kimi K3 represents a major milestone in democratizing frontier AI capabilities, rivaling proprietary models like GPT-5.6 Sol and Claude Fable 5 on key benchmarks. Its release pressures other leading labs to open their models and accelerates research into efficient scaling. Kimi K3 has 896 experts, activating 16 per token, and achieves approximately 2.5x scaling efficiency improvement over Kimi K2. It natively supports text, image, and video understanding with a 1 million token context window and supports MXFP4 quantization for deployment.

telegram · zaihuapd · Jul 27, 15:15

**Background**: Kimi K3 is built on a Mixture-of-Experts \(MoE\) architecture, which achieves large total parameters while keeping inference cost manageable by activating only a subset of experts per token. Its core innovations include Kimi Delta Attention \(KDA\), an expressive linear attention mechanism, and Stable LatentMoE, a variant of LatentMoE that optimizes accuracy per FLOP and per parameter by addressing memory bandwidth and communication bottlenecks. Quantization techniques like MXFP4 further reduce model size and computational requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2601.18089">[2601.18089] LatentMoE: Toward Optimal Accuracy per FLOP and ... LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in ... Think Smart About Sparse Compute: LatentMoE for Higher ... LatentMoE：低维潜空间专家路由架构 · chengenbao Kimi K3 Tech Blog: Open Frontier Intelligence LatentMoE：Kimi K3 背后的 MoE 高效变体 | Oilbeater 的自习室 Moonshot AI Releases Kimi K3: World&#x27;s First 2.8T Open-Source ...</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP 4 Quantization , and...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#Large Language Model`, `#MoE`, `#Kimi K3`

---

<a id="item-3"></a>
## [Fastjson2 RCE Vulnerability Disclosed, No Patch Available](https://mp.weixin.qq.com/s/LJaul1jNjK9pXRAkoUiMEA) ⭐️ 8.0/10

Longting Technology disclosed a remote code execution \(RCE\) vulnerability in Fastjson2 on July 27, affecting all versions up to 2.0.62 \(all released versions\). The vulnerability allows attackers to bypass AutoType validation via malicious JSON data and execute arbitrary code. This is the second critical vulnerability in the Fastjson family in a month, following a similar issue in Fastjson1. Given Fastjson2&\#x27;s widespread use in Java applications for JSON processing, this RCE poses a significant security risk until a fix is released. The vulnerability exists in all released versions, including the latest. The maintainer has acknowledged the issue, but the proposed fix in PR \#7695 was closed and not merged; no official patch is available yet. The recommended mitigation is to completely disable AutoType.

telegram · zaihuapd · Jul 27, 10:31

**Background**: Fastjson2 is a high-performance JSON library for Java developed by Alibaba, serving as the successor to Fastjson. The AutoType feature allows automatic type identification during deserialization, but it has historically been a source of deserialization vulnerabilities when not properly secured. This vulnerability exploits the same mechanism.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alibaba/fastjson2">GitHub - alibaba/fastjson2: FASTJSON2 is a Java JSON ...</a></li>
<li><a href="https://github.com/alibaba/fastjson2/blob/main/docs/autotype_en.md">fastjson2/docs/autotype_en.md at main · alibaba/fastjson2 ...</a></li>
<li><a href="https://www.besthub.dev/articles/understanding-fastjson-autotype-and-its-security-implications-cf52863d3326">Understanding Fastjson AutoType and Its Security Implications</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#fastjson`, `#RCE`, `#java`

---

<a id="item-4"></a>
## [China Begins Mass Production of Domestic DUV Lithography Tools](https://www.theinformation.com/articles/china-starts-mass-producing-homegrown-duv-chipmaking-tools-advance-local-chip-industry) ⭐️ 8.0/10

China has started mass production of its own immersion deep ultraviolet \(DUV\) lithography tools, with a target of approximately 5 units this year and around 20 units in 2027, to be delivered to domestic chipmakers including SMIC and Hua Hong Semiconductor. This development could gradually erode ASML&\#x27;s dominant position in the Chinese market, especially if Western export restrictions tighten, advancing China&\#x27;s semiconductor self-sufficiency goals. The domestic DUV tools still lag behind ASML in performance and reliability, requiring months or longer for chipmakers to test precision and compatibility before mass production; key components are sourced domestically with some from Japan, and local supply chain delays have already impacted progress this year.

telegram · zaihuapd · Jul 27, 14:10

**Background**: DUV \(deep ultraviolet\) lithography is a mature technology used to fabricate semiconductor chips, with immersion DUV using a liquid layer to improve resolution for advanced nodes. ASML from the Netherlands is the global leader in lithography systems, controlling nearly all EUV and a large share of DUV market. China has been striving to develop its own lithography equipment to bypass Western export restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbeta.com.tw/articles/tech/1445926.htm">全新国产 DUV 光 刻 机 曝 光 ：“套 刻 8nm”... - cnBeta.COM</a></li>
<li><a href="https://36kr.com/p/2303696917507330">这种 光 刻 机，成为焦点-36氪</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#DUV`, `#China`, `#lithography`, `#ASML`

---

<a id="item-5"></a>
## [Huawei Reportedly Plans DRAM Fab With Partner, Denies Claim](https://www.xda-developers.com/huawei-is-building-its-own-dram-fab-and-it-could-reshape-ram-prices-for-everyone/) ⭐️ 7.0/10

Huawei is reportedly planning to build a 12-inch DRAM fab with partner Shenzhen Shengwei Xu, targeting a monthly capacity of 140,000 wafers, though Huawei has denied the report. If built, the fab could secure a stable memory supply for Huawei&\#x27;s Ascend AI chips, reducing reliance on external suppliers like ChangXin Memory Technologies and potentially reshaping global DRAM prices and supply chains. The reported fab is a 12-inch wafer facility dedicated to DRAM production with a planned capacity of 140,000 wafers per month. However, building and ramping such a fab would take years, so any impact on consumer DRAM prices would not be immediate.

telegram · zaihuapd · Jul 27, 03:17

**Background**: Huawei&\#x27;s semiconductor design arm HiSilicon has faced US sanctions, disrupting its ability to procure advanced chips. The company recently returned to producing its own Kirin chips using domestic fabrication. DRAM is a type of volatile memory used in computers and servers; securing a domestic supply would help Huawei&\#x27;s AI chip business, which relies on high-bandwidth memory for Ascend processors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Huawei_Ascend_%28chip%29">Huawei Ascend (chip)</a></li>
<li><a href="https://www.huaweicentral.com/huawei-reveals-3-year-ascend-ai-chip-roadmap-950-coming-in-2026/">Huawei reveals 3-year Ascend AI chip roadmap, 950 coming in ...</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#DRAM`, `#semiconductor`, `#AI chips`, `#supply chain`

---

<a id="item-6"></a>
## [Alibaba Launches Qwen Office Beta with AI PPT, Tables, and Computer Control](https://qwenwork.cn/) ⭐️ 6.0/10

Alibaba has released the beta version of &\#x27;Qwen Office&\#x27;, an AI-powered office suite that can generate PPTs, tables, and control computers via natural language commands. This marks Alibaba&\#x27;s entry into the AI office productivity space, challenging existing tools like Microsoft Copilot and Google Gemini. It could redefine workflow automation for enterprise users. Qwen Office is available on web, Windows, and macOS, integrates with DingTalk, and includes a computer-use feature for cross-app automation. Pricing includes a free tier and paid plans starting at 78 yuan/month.

telegram · zaihuapd · Jul 27, 05:45

**Background**: Qwen is Alibaba&\#x27;s family of large language models. &\#x27;Computer Use&\#x27; refers to AI agents that can interact with desktop applications, clicking and typing on behalf of users. DingTalk is Alibaba&\#x27;s enterprise communication and collaboration platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DingTalk">DingTalk - Wikipedia</a></li>
<li><a href="https://claudecode.app/">100 Ways to Vibe Coding with Claude AI , Computer Use AI , and MCP...</a></li>

</ul>
</details>

**Tags**: `#AI Office`, `#Document Generation`, `#Automation`, `#Alibaba`, `#Computer Control`

---

<a id="item-7"></a>
## [China Rejects US Sanctions Threat Over AI Model Distillation](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 6.0/10

On July 27, the Chinese Ministry of Commerce officially rejected US plans to investigate and sanction Chinese AI companies over alleged model distillation of US frontier models, arguing that US companies also use Chinese models and that the accusations lack legal basis. This escalates US-China tensions in AI regulation, potentially impacting global AI supply chains and the open-source AI ecosystem, as nearly 200 US startups have urged the government not to restrict access to Chinese open-source models. China warns of countermeasures if US actions substantively harm Chinese interests. Model distillation is a widely used technique where a smaller model learns from a larger one; both Chinese and US companies practice it.

telegram · zaihuapd · Jul 27, 11:01

**Background**: Model distillation is a machine learning technique where a smaller &\#x27;student&\#x27; model is trained to mimic a larger &\#x27;teacher&\#x27; model, reducing computational cost while retaining performance. It is commonly used to deploy efficient AI on devices. The US has increasingly scrutinized Chinese AI companies for alleged IP theft, while China promotes open-source models like those from Alibaba and Baidu.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API - OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#China`, `#US sanctions`, `#model distillation`, `#geopolitics`

---

<a id="item-8"></a>
## [Hugging Face AI Breach Sparks Debate on Open vs Closed Models](https://www.zaobao.com.sg/news/china/story20260727-9426027) ⭐️ 6.0/10

In July 2026, Hugging Face suffered an autonomous AI agent intrusion that accessed internal data and credentials, but was eventually mitigated with help from an open-source AI model. The incident has reignited industry debate on the security boundaries between open-source and closed-source AI models. This high-profile breach demonstrates that even major AI platforms are vulnerable to AI-driven attacks, underscoring the urgent need for security collaboration mechanisms across the industry. The debate touches on regulation, open-source governance, and the balance between innovation and safety. The autonomous AI agent executed over 17,000 actions during the weekend breach, and investigators used a Chinese AI model to detect and reconstruct the intrusion. Industry experts have proposed three directions: clarifying model openness scope, defining intellectual property boundaries, and establishing security collaboration mechanisms for the open ecosystem.

telegram · zaihuapd · Jul 27, 13:28

**Background**: Hugging Face is the world&\#x27;s largest repository of AI models, hosting both open-source and proprietary models. The debate between open-source and closed-source AI has long centered on trade-offs: open models enable transparency and community-driven improvements but raise security and misuse risks, while closed models offer controlled access but limit collaboration. The recent incident highlights the need for clear security rules in the open-source ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/hugging-face-confirms-ai-driven-breach/">Hugging Face Confirms AI-Driven Breach: Attackers used ...</a></li>
<li><a href="https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html">World&#x27;s Largest AI Model Repository Hugging Face Breached by ...</a></li>
<li><a href="https://cybernews.com/ai-news/hugging-face-autonomous-ai-cyberattack/">Hugging Face breached by autonomous AI agent Cybernews</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#open source`, `#closed source`, `#AI governance`, `#Hugging Face`

---

<a id="item-9"></a>
## [Samsung may use Chinese DRAM for mid-range phones](https://www.asiatime.co.kr/article/20260727500259) ⭐️ 6.0/10

Samsung is reportedly considering using lower-cost mobile DRAM from Chinese suppliers for its mid-range Galaxy A series to cut costs and boost competitiveness in China. This move could reshape the DRAM supply chain if Samsung, the world&\#x27;s largest memory buyer, sources from Chinese rivals like CXMT, potentially increasing price competition and reducing Samsung&\#x27;s reliance on its own chips. The report claims Samsung aims to raise its low 0.6% Chinese smartphone market share by leveraging cost savings, amid industry-wide DRAM price inflation driven by AI demand that has forced rivals to cut shipments by 15-20%.

telegram · zaihuapd · Jul 27, 14:45

**Background**: DRAM is a type of memory chip used in smartphones and computers. Samsung has long dominated the DRAM market with its own chips, but Chinese manufacturers like CXMT \(ChangXin Memory Technologies\) have emerged with competitive pricing. The AI boom has caused a &\#x27;chip inflation&\#x27; as HBM demand consumes DRAM capacity, raising prices for conventional DRAM.

**Tags**: `#Samsung`, `#DRAM`, `#semiconductor`, `#cost reduction`, `#Chinese chips`

---