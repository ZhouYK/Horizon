---
layout: default
title: "Horizon Summary: 2026-07-26 (EN)"
date: 2026-07-26
lang: en
report: ai
---

> From 137 items, 10 important content pieces were selected

---

1. [Nvidia and SK Group announce $500B AI partnership for memory and factories](#item-1) ⭐️ 9.0/10
2. [Black Forest Labs Releases Flux3 with Native Audio-Video Sync](#item-2) ⭐️ 9.0/10
3. [Ruff v0.16.0 Expands Default Rules to 413, Breaking CI](#item-3) ⭐️ 8.0/10
4. [Kimi K3: Chinese AI Model Stirs Silicon Valley Concern](#item-4) ⭐️ 8.0/10
5. [Tech Giants Back Open-Weight AI Models](#item-5) ⭐️ 8.0/10
6. [Columbia University Explores Why AI Chatbots Fail as Therapists](#item-6) ⭐️ 8.0/10
7. [Silicon Valley Divided on Restricting Chinese AI Talent](#item-7) ⭐️ 8.0/10
8. [Fields Medalist Zimmermann Joins OpenAI for AI Safety](#item-8) ⭐️ 8.0/10
9. [XPeng Humanoid Robot Begins Trial Production in Guangzhou](#item-9) ⭐️ 8.0/10
10. [Google Q2 CapEx Doubles to Record $44.9B on AI Infrastructure](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Nvidia and SK Group announce $500B AI partnership for memory and factories](https://news.google.com/rss/articles/CBMirwJBVV95cUxNdFVPajJESWc0ZHlxdk1Rdkhja3E4NXktbU12VFBNVWFFQzlRZ3R0bElJNVV1RlRsRUpkcXR5Q0hZWEVNQ0NzQVpjUU8tenlDaVp6VEVMMnhtQjlTd21KTVd4M0Vkd3JuUDZEX3QyUU5EUzAtTlJOUF9iMDg2OThmdHcwaFlvYWgxeVpjSlMwdnRBV1ppRklFQmh6OHdqSEpYT005U2h2Q3hVcjc5eEdmNXdEaExRb2o4THc1Vmt4dXJkRkI3N2g4eS04RE90VTRocU1CcE5zeXd5X0ZFeE5YcjJOMmxfMkpYOHkzOG1Sd0lROVZITDRieWthbG5MN2ljQ3V0b1BkdE10WFMwMUNEMXBrN1g3WjhsWWZ5VmR5YUdfTkYycVhGMUp3emlhZXc?oc=5) ⭐️ 9.0/10

Nvidia and SK Group have entered a $500 billion partnership to develop next-generation memory technologies and build massive AI factories, aimed at supercharging AI infrastructure. This unprecedented investment highlights the critical need for advanced memory and computing infrastructure to support the explosive growth of AI workloads. The partnership could significantly accelerate AI deployment across industries by combining SK Group&\#x27;s memory expertise with Nvidia&\#x27;s AI platforms. The partnership likely involves SK Group&\#x27;s High Bandwidth Memory \(HBM\) technology, which is essential for AI processing, and Nvidia&\#x27;s DGX SuperPOD AI factory solutions. The $500 billion scale makes it one of the largest tech partnerships in history.

google\_news · Tom&\#x27;s Hardware · Jul 25, 13:55

**Background**: High Bandwidth Memory \(HBM\) is a 3D-stacked DRAM technology that delivers massive data throughput, critical for AI and high-performance computing workloads. Nvidia&\#x27;s DGX SuperPOD is a turnkey AI infrastructure solution integrating compute, networking, and storage into an &\#x27;AI factory.&\#x27; This partnership aims to combine these technologies at an enormous scale to meet growing AI demands.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.micron.com/products/memory/hbm">High-bandwidth memory (HBM) | Micron Technology Inc.</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/dgx-superpod/">DGX SuperPOD : AI Infrastructure for Enterprise Deployments | NVIDIA</a></li>

</ul>
</details>

**Tags**: `#AI`, `#hardware`, `#partnership`, `#memory`, `#infrastructure`

---

<a id="item-2"></a>
## [Black Forest Labs Releases Flux3 with Native Audio-Video Sync](https://www.aibase.com/news/29874) ⭐️ 9.0/10

Black Forest Labs has released Flux3, a multimodal foundation model that natively generates up to 20 seconds of synchronized audio and video in a single pass using its Self-Flow architecture. This is a major advancement in generative AI as it is the first foundation model to seamlessly integrate native audio generation with video, potentially transforming media production, virtual reality, and content creation. Flux3 employs separate encoders and decoders for image, video, audio, and motion, unified under the Self-Flow flow matching framework, and it outperforms previous models like Luma and Runway in audio-visual synchronization.

aibase · AIbase · Jul 25, 08:43

**Background**: The Self-Flow architecture is a self-supervised flow matching framework that aligns multimodal generation and understanding within a single model. Flow matching is a generative modeling paradigm that combines aspects of continuous normalizing flows and diffusion models, enabling efficient training and high-quality outputs. This approach allows Flux3 to handle multiple modalities \(image, video, audio\) without separate specialized models.

<details><summary>References</summary>
<ul>
<li><a href="https://bfl.ai/blog/flux-3">FLUX 3 - Real World Models: Towards Multimodal Flow Models as the...</a></li>
<li><a href="https://flux-3ai.org/">Flux 3 — Black Forest Labs&#x27; Multimodal AI for Images, Video &amp; Audio</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#audio-visual generation`, `#foundation model`, `#generative AI`, `#Flux3`

---

<a id="item-3"></a>
## [Ruff v0.16.0 Expands Default Rules to 413, Breaking CI](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Astral released Ruff v0.16.0 on July 23, 2026, expanding the default rule set from 59 to 413 rules. This caused many CI workflows with unpinned Ruff dependencies to fail due to new lint checks. This major update significantly increases the default lint coverage for Python projects without additional configuration, catching many syntax errors and runtime issues. Developers must now pin their Ruff version to avoid unexpected CI failures. The update increased the total number of rules in Ruff from 708 to 968, with 413 now enabled by default. New rules include DTZ005 \(datetime.now\(\) without timezone\) and BLE001 \(blind exception catch\).

rss · Simon Willison · Jul 25, 22:44

**Background**: Ruff is a high-performance Python linter and code formatter written in Rust, developed by Astral. It is designed to replace multiple traditional linters like Flake8 and is significantly faster. With the v0.16.0 release, Ruff&\#x27;s default rule set was expanded to cover more potential issues without requiring configuration.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/">An extremely fast Python linter and code formatter, written in Rust.</a></li>

</ul>
</details>

**Tags**: `#Ruff`, `#Python`, `#linting`, `#release`, `#Astral`

---

<a id="item-4"></a>
## [Kimi K3: Chinese AI Model Stirs Silicon Valley Concern](https://news.google.com/rss/articles/CBMiswFBVV95cUxOVlhNQ1NiUVI1eGN0bXF5S01TTm1tQlJWYjZsUWFZRkxxY0xJdVFTRlhNSzBJa01tT2I3TmE1TGtjX3dqbGJRRHZJOFlqbGJTOWdnMFJlMFVqYV9FVmFtWU5jUmVlT0lrc0Y5b25nTWlJZEwzRTNOMUpxb2pMR3F4NlVzZWp2UXlDZlBEMWxnelpsQWdQSDFXNGtJQXVzWlVZTmswQl9MQ2ZjaEpEYlpNd0xiWdIBxwFBVV95cUxOQW5CUzROYzFIVlEtblVsdzQ1Sm0teWhvdnU4M1F0SHkzeFRmdW51YU11TEZCS3VlVVpEUUl4by1mbVhYZzRkOHdpY2R6N0k3cEhaUHUxdkl1c3l2cDFFOXpQbUdBV25rUkhyR2dZMkRSUmtVN0dDbzhZeFF5V3VSNTNMbHlpSDJ3WlhNTEtET3RlRDJlZWJJaWh5enpiOXF2NGFxWlJrbXlhaWlvM0x4V2pLMEF6MWdLMi1aS25iQXJUOG9iMGFN?oc=5) ⭐️ 8.0/10

Kimi K3 is a 2.8 trillion-parameter model from Chinese startup Kimi, featuring a 1-million-token context window and native vision capabilities, released as the world&\#x27;s first open 3T-class AI model. This breakthrough signals China&\#x27;s growing competitiveness in frontier AI, potentially challenging US dominance and reshaping the global AI landscape, particularly in agentic coding and knowledge work. The model uses novel architectures including Delta Attention and Attention Residuals, and is designed for long-horizon tasks such as building multiplayer 3D games and creating professional slides.

google\_news · EL PAÍS English · Jul 26, 04:00

**Background**: Large language models \(LLMs\) like Kimi K3 are AI systems trained on vast text data to generate human-like responses. Parameter count \(e.g., 2.8 trillion\) roughly indicates model capacity, while context window size \(1 million tokens\) determines how much text the model can process at once. OpenAI and other US firms have traditionally led LLM development, but Chinese companies are rapidly closing the gap.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://openlm.ai/kimi-k3/">Kimi K3 - openlm.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#China`, `#Silicon Valley`, `#competition`

---

<a id="item-5"></a>
## [Tech Giants Back Open-Weight AI Models](https://news.google.com/rss/articles/CBMipAFBVV95cUxOS0hQcXlIMVB5UFFwVXM1Y0pZQm5XOXBzUmNveTg4RjZCc2RNdjdOVFV4U2JDZWdrTTRuTVROZ3lodE5FRVpielNWTVUyaFJkQlhHLVZmSVBWc1BRUHhNS1dNUjNTZ1lCb0drYk9pQ2hLQUtIUXlQUUc4eDNGVGYxOVQ5S1JSaDF0Q3BKSFFncDBKYUZCVV9fTm1aZXd6bjZKanB2dg?oc=5) ⭐️ 8.0/10

Meta, Microsoft, Nvidia, IBM, and other major tech companies have announced their support for open-weight AI models, marking a collective push towards more transparent and collaborative AI development. This endorsement from industry leaders could accelerate the adoption of open-weight models, potentially democratizing access to advanced AI and fostering innovation across sectors. Open-weight AI models have publicly available trained parameters \(weights\), allowing developers to download, use, and build upon them, though they may still have usage restrictions.

google\_news · AI News · Jul 26, 02:47

**Background**: Open-weight AI models are a step beyond closed-source models, as the trained parameters are made public, enabling deeper inspection and customization. However, they are not always fully open-source, as the training data and code may remain proprietary. This initiative by major tech companies signals a shift towards greater openness in AI, balancing transparency with commercial interests.

<details><summary>References</summary>
<ul>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://openai.com/global-affairs/open-weights-and-ai-for-all/">Open weights and AI for all | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open source`, `#industry news`, `#Meta`, `#Microsoft`

---

<a id="item-6"></a>
## [Columbia University Explores Why AI Chatbots Fail as Therapists](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5qSDNDZHVzUmtwbzkybUFpRGV2MWN4ZVpoRW13Q2ZtRWdMc3U2VEZyLVNYZnNEeHZLMEpzWElCYnhWRmticlBRRWFXRkNuZWJxQ2xDMFVKN1FqaGRpQkx3ZkU3Tmkta1U?oc=5) ⭐️ 8.0/10

An article from Columbia University critically analyzes why AI chatbots are inadequate and potentially harmful replacements for human therapists in mental health care. With increasing use of AI chatbots for mental health support, understanding their limitations is crucial to prevent harm and ensure ethical deployment. The article highlights that AI chatbots lack genuine empathy, fail to form a therapeutic alliance, and cannot handle complex or crisis situations appropriately, violating core mental health ethics standards.

google\_news · Columbia University · Jul 26, 04:56

**Background**: The therapeutic alliance, a collaborative relationship between therapist and client, is a key predictor of positive outcomes in therapy. AI chatbots, despite simulating conversation, cannot establish this bond due to lack of genuine understanding and emotional connection. Research shows that such tools often fail to recognize subtle cues and can provide inappropriate advice, leading to potential harm.

<details><summary>References</summary>
<ul>
<li><a href="https://www.psychologytoday.com/us/blog/some-assembly-required/202510/therapy-using-ai-chatbots-is-not-just-risky-its-dangerous">When AI Therapy Goes Wrong - Psychology Today</a></li>
<li><a href="https://www.brown.edu/news/2025-10-21/ai-mental-health-ethics">New study: AI chatbots systematically violate mental health ...</a></li>
<li><a href="https://mental.jmir.org/2025/1/e69294">JMIR Mental Health - Does the Digital Therapeutic Alliance ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mental health`, `#ethics`, `#chatbot`

---

<a id="item-7"></a>
## [Silicon Valley Divided on Restricting Chinese AI Talent](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMGg1N0lvWXlpTm43VlhleE5IZmNpNDhTTWFZbzBnV1lUY1FCa212cl93ZkVtU00waTNFMnhib0RnaFl1MVBvZEpVbVVwUmlod1FMTV9Qazh4NjVVNThXTnZXN3U0RFBXU1Rwd3JLcjNPSjYxN0gzbzR0bkdUMmg4NElGRVVHZzdDSE5N?oc=5) ⭐️ 8.0/10

The New York Times reports a split in Silicon Valley over policies to restrict Chinese AI researchers and engineers from entering the United States, highlighting differing views on national security versus talent flow. This debate affects the global AI talent pipeline and U.S. competitiveness, as restrictions could hinder innovation while aiming to protect intellectual property and national security. The split reflects a broader tension between tech companies that rely on foreign talent and policymakers concerned about espionage and technology transfer. No specific policy proposals are detailed in the article.

google\_news · The New York Times · Jul 25, 13:00

**Background**: The U.S. has tightened visa restrictions for Chinese nationals in sensitive fields amid growing geopolitical rivalry. Silicon Valley has historically benefited from a global talent pool, including many Chinese researchers who have contributed to AI advancements. This debate places national security concerns against the industry&\#x27;s need for top talent.

**Discussion**: No community comments are available for this news item.

**Tags**: `#AI`, `#geopolitics`, `#immigration`, `#technology policy`, `#Silicon Valley`

---

<a id="item-8"></a>
## [Fields Medalist Zimmermann Joins OpenAI for AI Safety](https://www.aibase.com/news/29878) ⭐️ 8.0/10

Fields Medalist Jakob Zimmermann has announced he will join OpenAI to focus on AI safety research. This move signals a growing convergence of top mathematical talent with AI safety, highlighting the increasing importance of rigorous mathematical thinking in addressing AI alignment challenges. Zimmermann was recognized for proving a core o-minimality conjecture, a result in model theory with applications in Diophantine geometry. He will join OpenAI&\#x27;s safety team.

aibase · AIbase · Jul 25, 08:43

**Background**: The Fields Medal is the highest honor in mathematics, awarded every four years to mathematicians under 40. O-minimality is a concept from model theory that studies &\#x27;tame&\#x27; structures, and has been used in proofs of important conjectures like the André-Oort conjecture.

<details><summary>References</summary>
<ul>
<li><a href="https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n3-p11-p.pdf">O-minimality and the André-Oort conjecture for Cn O-minimality and the André-Oort conjecture for $\mathbb {C ... O-minimality and Diophantine geometry - University of Oxford [2502.03071] Hodge theory and o-minimality at CIRM - arXiv.org O-minimality and the André-Oort conjecture for C... [1409.0771] O-minimality and certain atypical intersections</a></li>
<li><a href="https://people.maths.ox.ac.uk/pila/OminimalAO.pdf">O-minimality and the Andr e-Oort conjecture for Cn</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#Fields Medal`, `#mathematics`, `#research`

---

<a id="item-9"></a>
## [XPeng Humanoid Robot Begins Trial Production in Guangzhou](https://www.aibase.com/news/29875) ⭐️ 8.0/10

XPeng&\#x27;s humanoid robot has entered small-batch trial production at its Guangzhou factory, with Chairman He Xiaopeng personally overseeing the robot business as CEO, targeting mass production by 2026. This marks a significant step toward commercializing humanoid robots, a field with immense potential in manufacturing and service industries. XPeng&\#x27;s move could accelerate competition and innovation in the humanoid robotics sector, especially in China. The mass production line is undergoing final integration, and XPeng aims to officially achieve mass production of humanoid robots by 2026. The trial production is a critical validation phase before scaling up.

aibase · AIbase · Jul 25, 08:43

**Background**: Humanoid robots are robots designed to resemble and mimic human motions, often used for tasks in manufacturing, healthcare, and service. XPeng, primarily known as an electric vehicle manufacturer, has been investing in robotics as a strategic diversification. Small-batch trial production is a typical step before full-scale mass production, allowing companies to test manufacturing processes and refine designs.

<details><summary>References</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2ljM3JLN0VCSGdHa19uNzBCV0ZpZ0FQAQ?hl=en-US&amp;gl=US&amp;ceid=US:en">Google News - Xpeng &#x27;s robot debut in Shenzhen - Overview</a></li>
<li><a href="https://parametric-architecture.com/xpeng-iron-next-gen-humanoid-robot/">XPENG IRON: China’s Next-Gen Humanoid Robot That Moves Like...</a></li>

</ul>
</details>

**Tags**: `#humanoid robots`, `#manufacturing`, `#XPeng`, `#robotics`, `#AI`

---

<a id="item-10"></a>
## [Google Q2 CapEx Doubles to Record $44.9B on AI Infrastructure](https://www.aibase.com/news/29870) ⭐️ 8.0/10

Alphabet&\#x27;s Q2 2025 capital expenditure doubled year-over-year to $44.9 billion, driven by aggressive investment in AI infrastructure, while Google Cloud revenue surged 82% to $24.8 billion and operating profit margin nearly doubled. This signals Google&\#x27;s massive bet on AI as a core revenue driver, with cloud profitability improving rapidly, reinforcing the trend of hyperscalers competing fiercely in AI compute. The annualized capital expenditure run rate is approximately $18 billion per quarter. Google Cloud&\#x27;s operating profit margin nearly doubled, indicating that heavy investments in computing power are translating into strong profits.

aibase · AIbase · Jul 25, 08:43

**Background**: Capital expenditure for tech companies includes investments in data centers, servers, and networking equipment needed for AI workloads. Google has been expanding its AI infrastructure, including TPU chips and data centers, to support services like Gemini and Cloud AI. The strong cloud results reflect growing enterprise adoption of Google Cloud&\#x27;s AI offerings.

**Tags**: `#AI infrastructure`, `#cloud computing`, `#capital expenditure`, `#Google`, `#financial results`

---